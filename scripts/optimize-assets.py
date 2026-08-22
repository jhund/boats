#!/usr/bin/env python3
"""Shrink the repo's image folders for git: resize to 1600px, re-encode photos as JPEG,
leave screenshots/line art as PNG, then rewrite affected markdown links.

Usage: scripts/optimize-assets.py [--dry-run]

Photos (many unique colours) become .jpg; images with few colours stay .png so
diagrams and UI screenshots keep crisp edges. PDFs and SVGs are never touched.
"""
import pathlib, re, subprocess, sys, urllib.parse
from concurrent.futures import ThreadPoolExecutor

DRY   = '--dry-run' in sys.argv
MAX   = 1600      # longest edge
QUAL  = 82        # jpeg quality
PHOTO = 20000     # unique colours above which an image is treated as a photo

root   = pathlib.Path(__file__).resolve().parent.parent
DIRS   = [root/'research/images', root/'reference/images', root/'build_log/images']
RASTER = {'.png', '.jpg', '.jpeg', '.webp'}
SKIP   = {'.mov', '.mp4', '.pdf', '.svg'}   # never touched

def sh(*a):
    return subprocess.run(a, capture_output=True, text=True).stdout.strip()

def plan(p):
    # only PNGs are candidates for JPEG conversion, so only they need a colour count
    # (counting unique colours on a 4000px photo is slow and pointless otherwise)
    if p.suffix.lower() != '.png':
        return p, None, p
    colors = sh('magick', str(p), '-format', '%k', 'info:')
    try: colors = int(colors)
    except ValueError: colors = PHOTO + 1          # unreadable → treat as photo
    return p, colors, (p.with_suffix('.jpg') if colors > PHOTO else p)

def convert(job):
    src, colors, dst = job
    before = src.stat().st_size
    if DRY:
        return src, dst, before, before
    if dst.suffix.lower() in ('.jpg', '.jpeg'):
        # flatten any alpha onto white so transparency doesn't turn black
        sh('magick', str(src), '-resize', f'{MAX}x{MAX}>', '-background', 'white',
           '-alpha', 'remove', '-alpha', 'off', '-strip', '-quality', str(QUAL),
           '-interlace', 'Plane', str(dst))
    else:
        sh('magick', str(src), '-resize', f'{MAX}x{MAX}>', '-strip',
           '-define', 'png:compression-level=9', str(dst))
    if dst != src and dst.exists() and dst.stat().st_size > 0:
        src.unlink()
    return src, dst, before, dst.stat().st_size if dst.exists() else before

imgs = [p for d in DIRS if d.is_dir()
        for p in d.rglob('*') if p.is_file() and p.suffix.lower() in RASTER]
with ThreadPoolExecutor(max_workers=8) as ex:
    jobs = list(ex.map(plan, imgs))
    results = list(ex.map(convert, jobs))

renames = {s.name: d.name for s, d, _, _ in results if s.name != d.name}
before  = sum(r[2] for r in results)
after   = sum(r[3] for r in results)

# --- rewrite markdown links for anything renamed ---
touched = 0
if renames and not DRY:
    for md in root.rglob('*.md'):
        s = str(md)
        if '.git/' in s or s.startswith(str(root/'_temp')) or '/images/' in s: continue
        txt = orig = md.read_text()
        for old, new in renames.items():
            if old in txt:
                txt = txt.replace(old, new)
        if txt != orig:
            md.write_text(txt); touched += 1

print(f"{len(results)} images: {before/1e6:.0f} MB → {after/1e6:.0f} MB "
      f"({100*(1-after/before):.0f}% smaller)")
print(f"converted to jpeg: {len(renames)}   left in original format: {len(results)-len(renames)}")
print(f"markdown files updated: {touched}" + ("  (dry run)" if DRY else ""))
