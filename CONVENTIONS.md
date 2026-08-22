# Conventions

[← Home](README.md)

How this repo is put together, so it stays consistent over a build that will take years.
Publishing is `git push`. GitHub renders the markdown with its default styling, no build step,
no Pages, no wiki.

## Repo layout

```
README.md              Entry point: the boat, phase table, links to everything
CONVENTIONS.md         This file
CONTRIBUTING.md        How third parties can submit corrections and additions
LICENSE                CC BY-NC-SA 4.0, full text
.github/
  PULL_REQUEST_TEMPLATE.md
  ISSUE_TEMPLATE/      Errata, correction and tip forms
build_log/
  README.md            Chronological index of every entry, grouped by phase
  _template.md         Copy this for a new entry
  007-set-up-the-build-frame.md   One entry per work session or discrete job
  images/
    007-set-up-the-build-frame/    Photos for that entry, and only that entry
reference/
  README.md            Index of the reference section
  tools.md
  bill-of-materials.md Includes Amazon affiliate links
  plan-modifications.md
  plans-errata.md
  techniques.md
  glossary.md
  costs.md
  mistakes.md
  images/              Images used by the reference pages
research/              Notes worked out before and during the build
  README.md            Index of the topic pages
  center-board.md      One page per topic
  images/              Every research image, flat (from the Logseq export)
images/                Repo-level images only (hero shot, plan overview)
scripts/
  new-entry.sh         Scaffolds a new entry + its image folder
  extract-research.py  Splits pasted Logseq outline sections into topic pages
  optimize-images.py   Resizes/re-encodes the images/ folders for a sane repo size
```

## Entry files

- Named `NNN-short-slug.md`, zero-padded, monotonically increasing. Numbers never change once
  pushed — links elsewhere depend on them.
- The number is the order the work happened in.
- One entry per session or per discrete job. A three-day fairing marathon can be one entry.
- Every entry starts with a nav line and ends with the same nav line.
- No metadata table: dates, hours, plans references and material lists are deliberately kept out
  of the published entries.
- Don't renumber to insert work you forgot. Add it at the end with the real date, and link to it
  from the entry it belongs near.

## New entry

```sh
scripts/new-entry.sh "fitting the bulkheads"
```

That creates `build_log/NNN-fitting-the-bulkheads.md` from the template and
`build_log/images/NNN-fitting-the-bulkheads/`. Then, by hand:

1. Fill in the entry.
2. Add a row to the right phase table in `build_log/README.md`.
3. Update the phase table and the "at a glance" numbers in `README.md`.
4. Fix the `Next entry →` link in the previous entry.
5. `git add -A && git commit -m "log: fitting the bulkheads" && git push`

## Photos

- Live in `build_log/images/<entry-slug>/`, referenced relatively.
- **Plain markdown only — no `<img>` tags, no table layouts.** Chosen deliberately: only plain
  markdown previews in a local editor, and it avoids the borders and zebra striping GitHub puts
  on multi-row tables. GitHub already wraps every image in a link to the full-size original, and
  scales it down on narrow screens, so the HTML forms buy nothing.

  ```markdown
  ![Alt text describing the photo](images/<entry-slug>/group-01-what-it-shows.jpg)
  *Caption. What to look at, and why it matters.*
  ```

  **No blank line between the image and its caption** — that keeps them in one paragraph, so the
  caption sits tight underneath. A blank line adds a paragraph gap and the caption starts reading
  as body text. Do leave a blank line after the caption, before the next prose.
- Don't set a display width. There is no markdown syntax for it, `style` and `class` are stripped,
  and `{width=480}`-style attributes render as literal text.
- Named `group-NN-what-it-shows.jpg`, numbered in the order they appear in the entry.
- Always `.jpg`, never `.jpeg`. One extension, so links stay predictable. No spaces or
  parentheses in filenames: markdown links break on both.
- **Optimize before committing.** Drop new photos into the right `images/` folder, then run:
  ```sh
  scripts/optimize-images.py --dry-run   # report what would change
  scripts/optimize-images.py             # do it
  ```
  It resizes to 1600px on the longest edge, re-encodes at JPEG quality 82, strips metadata, and
  sweeps all three image folders (`build_log/images`, `research/images`, `reference/images`).
  Photographic PNGs become `.jpg` and any markdown links to them are rewritten; low-colour images
  stay PNG so diagrams and screenshots keep crisp edges. PDFs, SVGs and video are never touched.
  It is safe to re-run — already-optimized files are left alone.

  This matters because git keeps every version of every binary forever. One unoptimized batch of
  camera files is permanent repo weight. For scale: the first import was 855MB and came out at
  79MB, visually indistinguishable at the sizes GitHub displays.
- Raw camera files are gitignored. Keep originals outside the repo, or in `originals/`.
- Always write a real caption. GitHub shows alt text as the caption when the image fails to load,
  and it's what makes the log followable.
- Videos don't belong in the repo. Link out to them.

## Links

- Always relative, never absolute GitHub URLs. They keep working if the repo is renamed, forked,
  or cloned.
- Link to the reference section instead of re-explaining a technique in an entry.
- A `TODO` marker is a fine placeholder. Grep for them before you call a section done:
  ```sh
  grep -rn TODO --include='*.md' .
  ```

## Affiliate links

- Only in `reference/bill-of-materials.md` and `reference/tools.md`, marked *(aff)* in the table.
- Format: `https://www.amazon.com/dp/ASIN?tag=YOURTAG-20`
- The disclosure at the bottom of `README.md` needs to stay there.
- Recommend only what you actually used.

## Writing style

- Sentence case for every heading, page title and link label — capitalise only the first word
  and proper nouns (Long Steps, Welsford, CNC).
- End every bullet with a full stop, even a short fragment. Mixed punctuation across a list
  looks like an oversight; consistent punctuation reads as deliberate.
- Second person for instructions, first person for what happened.
- Real numbers: measurements, hours, litres of epoxy, dollars.
- Write down the mistake. It's the most useful thing in the log.
