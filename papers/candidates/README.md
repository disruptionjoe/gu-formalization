# papers/candidates/

Papers that have **graduated out of `papers/drafts/`** and are staged for publication, but are **not yet
public**. A folder here means: Joe has explicitly said he intends to publish this paper, and it has passed
the light staging gate below. It does **not** mean it has been submitted or posted.

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

Each candidate carries a `STAGING-NOTES.md` recording its scope, honest grade, open items, and the gate pass.

## Currently staged

- **`located-not-forced/`** -- "Located, Not Forced: Two-Primary Obstructions Cannot Force the Fermion
  Generation Count in a Clifford Rarita-Schwinger Sector." The program's lead result. `.tex` is the arXiv
  submission source.
- **`six-axis-testability/`** -- "Six-Axis Testability" white paper. A methods/position proposal (separate
  track from the mathematical-result papers). Its empirical benchmark is unexecuted; see its STAGING-NOTES.
