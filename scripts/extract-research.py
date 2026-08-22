#!/usr/bin/env python3
"""Extract `- ### ` sections pasted into research/README.md into their own pages,
then rebuild the index from whatever pages exist.

Usage: scripts/extract-research.py [--dry-run]

Paste new Logseq outline sections anywhere below the index in research/README.md,
each starting with a top-level `- ### Title` line, then run this. Section bodies are
copied verbatim; only an H1 and a back-link are added.
"""
import pathlib, re, sys

DRY = '--dry-run' in sys.argv
root = pathlib.Path(__file__).resolve().parent.parent
rdir = root/'research'
idx  = rdir/'README.md'

slug = lambda t: re.sub(r'[^a-z0-9]+', '-', t.lower()).strip('-')
lines = idx.read_text().split('\n')

# --- locate pasted sections ---
marks = [i for i, l in enumerate(lines) if l.startswith('- ### ')]
sections = []
for k, i in enumerate(marks):
    end = marks[k+1] if k+1 < len(marks) else len(lines)
    body = lines[i+1:end]
    while body and not body[-1].strip():
        body.pop()
    sections.append((lines[i][6:].strip(), body))

created, skipped = [], []
for title, body in sections:
    p = rdir/f"{slug(title)}.md"
    if p.exists():
        skipped.append(p.name)
        continue
    if not DRY:
        p.write_text(f"# {title}\n\n[← Research index](README.md)\n\n" + "\n".join(body) + "\n")
    created.append(p.name)

# --- rebuild index: keep the prose header, regenerate the topic list ---
try:
    head_end = next(i for i, l in enumerate(lines) if l.strip() == '## Topics')
except StopIteration:
    sys.exit("research/README.md has no '## Topics' heading — refusing to rewrite it.")
header = lines[:head_end+1]

pages = [p for p in rdir.glob('*.md') if p.name.lower() != 'readme.md']
topics = sorted(
    (p.read_text().split('\n')[0].lstrip('#').strip(), p.name) for p in pages
)
out = header + [''] + [f"- [{t}]({n})" for t, n in topics] + [
    '', '---', '',
    f"*{len(topics)} topics, extracted from a Logseq outline. Not yet edited for final copy.*",
]
if not DRY:
    idx.write_text('\n'.join(out) + '\n')

print(f"created {len(created)}: {', '.join(created) or '—'}")
if skipped:
    print(f"skipped {len(skipped)} (page already exists): {', '.join(skipped)}")
print(f"index lists {len(topics)} topics" + (" (dry run, nothing written)" if DRY else ""))
