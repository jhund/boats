# Photo layout options

Scratch page for choosing how to present photos. Every option uses the same real photos from entry
[012](012-prepare-and-install-doublers.md), so the comparison is fair. Pick the ones you want,
then delete this file and record the choice in [CONVENTIONS.md](../CONVENTIONS.md).

**Two facts that shape everything below**, both confirmed against GitHub's rendering API:

1. GitHub wraps *every* image — markdown or raw `<img>` — in `<a target="_blank">` pointing at the
   file. Click-to-open-full-size is automatic. Never wrap an image in your own `<a>`: you'd lose
   the `target="_blank"` and the original would replace the page instead of opening in a new tab.
2. `style` and `class` are stripped, and markdown has no size syntax, so **`width` on a raw
   `<img>` is the only way to control display size**. Percentages and pixels both work.

---

## A — Plain markdown

The baseline. Fills the content column (~900px), clickable, works in every renderer.

![Doublers cut from 9mm ply](images/012-prepare-and-install-doublers/doublers-01-cut.jpg)

*Doublers cut out and labelled before any epoxy work.*

> Note the blank line before the caption. Without it, the caption joins the image's paragraph and
> flows onto the same line — fine for a full-width image, wrong for a narrow one. See option B.

---

## B — Sized, with caption directly beneath

The workhorse. `width` sets the display size; `<br>` puts the caption on its own line; `<sub>`
makes it visibly a caption rather than body text.

<p>
<img src="images/012-prepare-and-install-doublers/doublers-03-epoxy-coated.jpg" width="480" alt="Doublers after epoxy coating"><br>
<sub>All doublers coated, both faces, standing on nails to drain.</sub>
</p>

---

## C — Centred

Same as B with `align="center"` on the paragraph. Reads more like a published figure; costs you
the ragged-left rhythm of the page.

<p align="center">
<img src="images/012-prepare-and-install-doublers/doublers-04-glue-b3-to-b4.jpg" width="520" alt="Gluing the B3 doubler"><br>
<sub>B3 doubler glued and clamped. Packing tape stops squeeze-out bonding the pad to the work.</sub>
</p>

---

## D — Table figure: caption boxed with the photo

The caption cannot drift from its photo — they share a cell. GitHub draws a border, which reads as
a figure frame. Heavier, so worth reserving for photos that carry a real point.

<table>
<tr><td>
<img src="images/012-prepare-and-install-doublers/doublers-08-b3-glued.jpg" width="500" alt="B3 doubler glued"><br>
<sub><b>Fig 1.</b> B3 done, curing overnight. The gap at the top edge closed up once the last
clamp went on — worth checking before the epoxy goes off.</sub>
</td></tr>
</table>

---

## E — Two-up: before / after

For pairs where the comparison *is* the point. Percentage widths stay readable on a phone.

<table>
<tr>
<td width="50%"><img src="images/012-prepare-and-install-doublers/doublers-02-expoxy-prep.jpg" width="100%" alt="Before epoxy"></td>
<td width="50%"><img src="images/012-prepare-and-install-doublers/doublers-03-epoxy-coated.jpg" width="100%" alt="After epoxy"></td>
</tr>
<tr>
<td><sub>Sanded and ready to coat.</sub></td>
<td><sub>Two coats on, wet-on-tacky.</sub></td>
</tr>
</table>

---

## F — Three-up strip for a sequence

Tighter. Good for a three-step process where no single frame needs to be large.

<table>
<tr>
<td width="33%"><img src="images/012-prepare-and-install-doublers/doublers-05-glue-b3-aft.jpg" width="100%" alt="Aft side"></td>
<td width="33%"><img src="images/012-prepare-and-install-doublers/doublers-06-glue-b3-fwd.jpg" width="100%" alt="Forward side"></td>
<td width="33%"><img src="images/012-prepare-and-install-doublers/doublers-07-glue-b3-side.jpg" width="100%" alt="Side view"></td>
</tr>
<tr>
<td><sub>Aft face.</sub></td>
<td><sub>Forward face.</sub></td>
<td><sub>From the side — clamp spacing.</sub></td>
</tr>
</table>

---

## G — Text beside photo

For a step where the explanation carries the weight and the photo is a reference. Markdown inside
a table cell only renders if the cell content is surrounded by blank lines, as below.

<table>
<tr>
<td width="55%">

Glue one doubler at a time. Mix the epoxy to a mayonnaise consistency with silica — thin enough to
wet the ply, thick enough that it won't run out of the joint while you fuss with clamps.

Dry-fit and mark the clamp positions **first**. Once there's epoxy on the part you have maybe ten
minutes in a warm shop, and that is not the moment to find you're one clamp short.

</td>
<td width="45%">
<img src="images/012-prepare-and-install-doublers/doublers-09-glue-lower.jpg" width="100%" alt="Lower doublers glued"><br>
<sub>Lower doublers, all clamped up.</sub>
</td>
</tr>
</table>

---

## H — Collapsed gallery

Keeps a long entry readable — the reader gets the narrative, and the full photographic record is
one click away. This is the answer for entries like 010 with 50+ photos.

<details>
<summary><b>The rest of the doubler glue-ups</b> (6 photos)</summary>
<br>
<table>
<tr>
<td width="33%"><img src="images/012-prepare-and-install-doublers/doublers-10-prep-b2-upper.jpg" width="100%"><br><sub>B2 upper, prepped.</sub></td>
<td width="33%"><img src="images/012-prepare-and-install-doublers/doublers-11-glue-b2.jpg" width="100%"><br><sub>B2 glued.</sub></td>
<td width="33%"><img src="images/012-prepare-and-install-doublers/doublers-12-glue-b4.jpg" width="100%"><br><sub>B4 glued.</sub></td>
</tr>
<tr>
<td width="33%"><img src="images/012-prepare-and-install-doublers/doublers-13-b1-to-b2.jpg" width="100%"><br><sub>B1 to B2.</sub></td>
<td width="33%"><img src="images/012-prepare-and-install-doublers/doublers-14-b2-to-b3.jpg" width="100%"><br><sub>B2 to B3.</sub></td>
<td width="33%"><img src="images/012-prepare-and-install-doublers/doublers-15-b9to-transom.jpg" width="100%"><br><sub>B9 through to the transom.</sub></td>
</tr>
</table>
</details>

---

## I — Text beside photo

In table to limit width, but markdown image format

<table>
<tr>
<td width="50%">

![Doublers cut from 9mm ply](images/012-prepare-and-install-doublers/doublers-01-cut.jpg)

</td>
<td width="50%">

Glue one doubler at a time. Mix the epoxy to a mayonnaise consistency with silica — thin enough to
wet the ply, thick enough that it won't run out of the joint while you fuss with clamps.

Dry-fit and mark the clamp positions **first**. Once there's epoxy on the part you have maybe ten
minutes in a warm shop, and that is not the moment to find you're one clamp short.

</td>
</tr>
<tr>
<td>

### A list for steps without a photo

- item 1
- item 2
- item 3

Some more text

</td>
<td width="50%">

Glue one doubler at a time. Mix the epoxy to a mayonnaise consistency with silica — thin enough to
wet the ply, thick enough that it won't run out of the joint while you fuss with clamps.

Dry-fit and mark the clamp positions **first**. Once there's epoxy on the part you have maybe ten
minutes in a warm shop, and that is not the moment to find you're one clamp short.

</td>
</tr>


</table>

Testing a skinny image with raw markdown

![image caption](images/001-my-prior-boatbuilding-experience/canoes-2-skeleton.jpg)

---

## What does not work

Confirmed by posting each form to GitHub's markdown API and reading the HTML it returns. The three
lines below should render as an image followed by visible literal braces — proof, when you push
this page, that the attribute syntax isn't available.

![braces equals](images/012-prepare-and-install-doublers/doublers-01-cut.jpg){width=480}

![braces colon](images/012-prepare-and-install-doublers/doublers-01-cut.jpg){width: 480}

![braces kramdown](images/012-prepare-and-install-doublers/doublers-01-cut.jpg){: width="480"}

Also unavailable:

| Attempt | What GitHub does |
|---|---|
| `{width=480}` / `{width: 480}` / `{: width="480"}` | passed through as literal text |
| `style="width:480px"` | attribute stripped |
| `class="thumb"` | attribute stripped |
| `<figure>` / `<figcaption>` | **both tags stripped**; the caption escapes as bare body text |
| Your own `<a href>` around an image | works, but loses GitHub's `target="_blank"` |

## What does work

`<img width>` (px or %), `<table>` with `width` on `<td>`, `<p align="center">`, `<br>`, `<sub>`,
`<b>`, `<em>`, `<details>` / `<summary>`. Images are auto-linked inside all of them.
