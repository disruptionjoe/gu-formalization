# papers/candidates/

Papers that have **graduated out of `papers/drafts/`** and are staged for publication, but are **not yet
public**. A folder here means: Joe has explicitly said he intends to publish this paper, and it has passed
the light staging gate below. It does **not** mean it has been submitted or posted.

Recorded exceptions: *Located, Not Forced* v1.0.0 was published on 2026-07-23,
and *Compact-Image Obstructions* v1.0.0 was published on 2026-08-03. Their
active source and reproducibility trees remain at the existing paths to avoid
breaking verified scripts, package references, and provenance links. Their
posted status is authoritatively recorded in `../published/INDEX.md`.

## Lifecycle (the three stages)

1. **`papers/drafts/`** -- work in progress. All drafts, notes, and **previous/superseded versions** of a
   paper live and stay here. Edit freely.
2. **`papers/candidates/`** (this folder) -- a paper graduates here **only when Joe has explicitly
   said he wants to publish it.** The current version moves; its earlier versions stay in `papers/drafts/`.
   Treat as near-final; substantive changes should be deliberate.
3. **`papers/published/`** (sibling folder) -- the public record. A paper moves up here **only after Joe
   informs that it has actually been published** (arXiv id / DOI / live URL recorded). Append-mostly.

A paper moves rightward as its status advances. It lives in exactly one of these stages at a time, so the
folder a paper is in always tells the truth about where it stands.

## The light staging gate

Kept deliberately light (not a hostile-referee deep-dive). A draft enters this folder only after a one-pass
check that:

1. **The title matches the theorem-grade core** -- the headline claims only what is actually proven.
2. **No retracted or downgraded wording leaks in** -- grades (theorem / computed / reconstruction / gated /
   open) are stated explicitly; nothing reads stronger than its evidence.
3. **Every external citation resolves** -- author, title, arXiv id correct.
4. **The single sharpest open issue is acknowledged in-text.**
5. **No overlap with another staged candidate** -- if two drafts share a core, only the hardened carrier
   stages.

Each candidate should carry a `STAGING-NOTES.md` recording its scope, honest grade, open items, and the gate
pass. Missing staging notes in the inventory below are cleanup debt, not an implicit publication decision.

## Currently staged

This table is inventory only. Folder membership is the status signal; updating this map does not publish,
submit, reclassify, or advance a paper.

| candidate folder | paper / packet | staging note |
|---|---|---|
| [`good-stable-compactification-no-go/`](good-stable-compactification-no-go/) | **Published v1.0.0** — "Compact-Image Obstructions for a Hyperbolic Grading in Sp(32,32): Neutral, Grading-Even, and Extremal Order Parameters." DOI [`10.5281/zenodo.21779705`](https://doi.org/10.5281/zenodo.21779705); source and reproducibility tree retained at this stable path. | [`STAGING-NOTES.md`](good-stable-compactification-no-go/STAGING-NOTES.md); [`FINAL-RELEASE-RECEIPT-v1.0.0.md`](good-stable-compactification-no-go/FINAL-RELEASE-RECEIPT-v1.0.0.md) |
| [`generation-number-boundary-odd-primary/`](generation-number-boundary-odd-primary/) | Generation Number Boundary Odd Primary; boundary / odd-primary location packet. | [`STAGING-NOTES.md`](generation-number-boundary-odd-primary/STAGING-NOTES.md) |
| [`generation-number-located-not-forced/`](generation-number-located-not-forced/) | Generation Number Located Not Forced; class-wide forcing no-go and `{1,3}` reduction. | [`STAGING-NOTES.md`](generation-number-located-not-forced/STAGING-NOTES.md) |
| [`keep-and-grade-loop-cost/`](keep-and-grade-loop-cost/) | Keep And Grade Loop Cost; loop-cost / keep-and-grade packet. | [`STAGING-NOTES.md`](keep-and-grade-loop-cost/STAGING-NOTES.md) |
| [`located-not-forced/`](located-not-forced/) | **Published v1.0.0** — "Located, Not Forced: A Scoped Two-Primary Audit of a Clifford Rarita-Schwinger Generation Carrier." DOI [`10.5281/zenodo.21515143`](https://doi.org/10.5281/zenodo.21515143); source tree retained at this stable path. | [`STAGING-NOTES.md`](located-not-forced/STAGING-NOTES.md) |
| [`observer-value-selection/`](observer-value-selection/) | Observer Value Selection candidate (broader physical-realization draft; distinct from the published theorem paper). | [`STAGING-NOTES.md`](observer-value-selection/STAGING-NOTES.md) |
| [`one-residual-complete-picture/`](one-residual-complete-picture/) | One Residual Complete Picture; one-residual synthesis candidate. | [`STAGING-NOTES.md`](one-residual-complete-picture/STAGING-NOTES.md) |
| [`six-axis-testability/`](six-axis-testability/) | "Six-Axis Testability" white paper; a methods / position proposal separate from the mathematical-result papers. Its empirical benchmark is unexecuted. | [`STAGING-NOTES.md`](six-axis-testability/STAGING-NOTES.md) |
| [`uv-structure-fourth-order-gravity/`](uv-structure-fourth-order-gravity/) | UV Structure Fourth Order Gravity candidate. | [`STAGING-NOTES.md`](uv-structure-fourth-order-gravity/STAGING-NOTES.md) |
