# Contributing

This is one person's build log for a Welsford Long Steps, written so that the next builder can
follow along. Other builders have already made it better than I could on my own — Joel Bergen and
Mark Baker both turned up errors in the plans that are now in
[Plans errata](reference/plans-errata.md). More of that, please.

You don't need to be an expert. If you got stuck where I got stuck, that's worth writing down.

## The most useful contributions

Roughly in order of how much they help the next builder:

1. **Plans errata.** A dimension that doesn't work, a contradiction between sheets, a part that
   won't fit as drawn. Add it to [Plans errata](reference/plans-errata.md) with the sheet and item
   number, what you measured, and what you did instead.
2. **Corrections to anything factual.** A wrong dimension, a wrong epoxy ratio, a technique
   described in a way that would cause a failure. These matter most, because someone will act on
   them.
3. **Techniques and tips.** Something you worked out the hard way →
   [Techniques](reference/techniques.md).
4. **Glossary terms.** The word you had to look up → [Glossary](reference/glossary.md).
5. **Materials and suppliers.** Where to get something, in what quantity →
   [Bill of materials](reference/bill-of-materials.md).
6. **Typos, broken links, sentences that don't parse.** Always welcome.

## What to leave alone

- **The build log entries.** Files under `build_log/` are my first-person account of what I did on
  a particular day. Please don't rewrite them in your own voice. If something in one is wrong or
  unclear, open an issue or add a correction to the relevant reference page, and I'll fold it in.
- **Affiliate links.** The Amazon links in the bill of materials and tools pages carry my referral
  tag. Please don't add, change or remove affiliate links. Plain product links are welcome.
- **Decisions already built into the boat.** "You should have used X instead" is genuinely
  interesting as an issue or a note in [Plan modifications](reference/plan-modifications.md), but
  it isn't a change to a hull that already exists.

## Please don't reproduce the plans

The plans are John Welsford's copyright and are deliberately **not** in this repo. Buy them from
him — that's how designers of small boats stay in business.

Quoting a specific dimension in order to report an error is fine, and necessary. Posting plan
sheets, CAD files, DXFs, or enough dimensions that someone could build from them is not, and I'll
decline that pull request.

## How to submit

Standard GitHub flow. There's nothing to install and nothing to build — it's plain markdown.

```sh
# fork on GitHub, then
git clone https://github.com/<you>/<repo>.git
git checkout -b errata-bulkhead-2-doubler
# make your change
git commit -am "errata: B-2 doubler width contradicts sheet 8"
git push origin errata-bulkhead-2-doubler
```

Then open a pull request describing what changed and why. If it's a correction, say how you know —
"I measured mine", "my sheet 3 shows 675", "the designer told me".

**One topic per pull request.** Small and focused gets merged quickly; a sweeping rewrite of six
pages will sit there while I work out what I think about each part of it.

**Not comfortable with git?** Two easier routes: open an issue, or click the pencil icon on any
page here on GitHub — it will make the fork, the branch and the pull request for you.

## Before you open a pull request

- [ ] Skim [CONVENTIONS.md](CONVENTIONS.md). The house style is sentence case headings, a full stop
      on every bullet, plain markdown for photos, and relative links only.
- [ ] Links are relative (`../reference/techniques.md`), never absolute `github.com` URLs — they
      break when the repo is renamed or forked.
- [ ] Photos: put them in the right `images/` folder, run `scripts/optimize-images.py`, use `.jpg`,
      and no spaces or parentheses in filenames. Write a real caption.
- [ ] Only photos you took yourself, or that you have permission to publish here.
- [ ] If you're relaying someone else's finding, credit them.

There's no CI on this repo, so the checklist is the review.

## Credit

Contributions are credited by name where they land, the way Joel's and Mark's are. Tell me how
you'd like to be named — or say if you'd rather not be named at all, which is fine.

## Licensing of contributions

This repository is licensed under [CC BY-NC-SA 4.0](LICENSE). By opening a pull request you agree
that your contribution is published under that same licence, and that you have the right to do so —
which mainly means: your own words, and photos you took yourself.

If you're relaying something another builder told you, say so, and don't paste text they wrote
without their say-so.

## Questions

Open an issue. A question that took you an hour to answer is exactly the kind of thing that belongs
in this log.
