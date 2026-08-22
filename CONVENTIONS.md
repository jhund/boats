# Conventions

[← Home](README.md)

How this repo is put together, so it stays consistent over a build that will take years.
Publishing is `git push`. GitHub renders the markdown with its default styling, no build step,
no Pages, no wiki.

## Repo layout

```
README.md              Entry point: the boat, phase table, links to everything
CONVENTIONS.md         This file
build_log/
  README.md            Chronological index of every entry, grouped by phase
  _template.md         Copy this for a new entry
  001-build-frame.md   One entry per work session or discrete job
  images/
    001-build-frame/   Photos for that entry, and only that entry
reference/
  README.md            Index of the reference section
  tools.md
  materials.md         Includes Amazon affiliate links
  techniques.md
  glossary.md
  costs.md
  mistakes.md
images/                Repo-level images only (hero shot, plan overview)
scripts/
  new-entry.sh         Scaffolds a new entry + its image folder
```

## Entry files

- Named `NNN-short-slug.md`, zero-padded, monotonically increasing. Numbers never change once
  pushed — links elsewhere depend on them.
- The number is the order the work happened in. The date lives in the metadata table.
- One entry per session or per discrete job. A three-day fairing marathon can be one entry.
- Every entry starts with a nav line and the metadata table from `_template.md`, and ends with the
  same nav line.
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

- Live in `build_log/images/<entry-slug>/`, referenced relatively: `![Caption](images/<entry-slug>/01-thing.jpg)`.
- Named `NN-what-it-shows.jpg`, numbered in the order they appear in the entry.
- **Resize before committing.** Longest edge ~1600px, JPEG quality ~80, under ~500KB. Git keeps
  every version of every binary forever; full-size camera files will make this repo unclonable.
  ```sh
  # macOS, in place on a copy
  sips -Z 1600 *.jpg
  # or with ImageMagick
  magick mogrify -resize 1600x1600\> -quality 80 *.jpg
  ```
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

- Only in `reference/materials.md` and `reference/tools.md`, marked *(aff)* in the table.
- Format: `https://www.amazon.com/dp/ASIN?tag=YOURTAG-20`
- The disclosure at the bottom of `README.md` needs to stay there.
- Recommend only what you actually used.

## Writing style

- Second person for instructions, first person for what happened.
- Real numbers: measurements, hours, litres of epoxy, dollars.
- Write down the mistake. It's the most useful thing in the log.
