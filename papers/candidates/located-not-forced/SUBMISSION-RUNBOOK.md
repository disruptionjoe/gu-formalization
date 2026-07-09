# Submission Runbook — Located, Not Forced

**Prepared:** 2026-07-09. **Paper version:** v2.10. **Status:** READY (staged; not submitted).
**Purpose:** a single linear checklist Joe can follow when he sits down to submit. This consolidates the
Joe-side steps that had accumulated across the readiness passes in `STAGING-NOTES.md` (v2.4 through v2.10).
`STAGING-NOTES.md` remains the full history; this file is the do-this-then-this.

This runbook prepares a submission. It is **not** authorization to submit. No agent performs any step here —
every action below is Joe's. Agents do not touch arXiv, inspect or update the arXiv account, or post anything.

---

## Where the paper stands

- Headline result is **theorem-grade and GU-independent**; honesty discipline clean.
- Both publication-gating work cards are **closed**: `WC-ENUM-COMPLETENESS` (class-C census complete, computed
  grade) and `WC-ANTILINEAR-BOUND` (index-nullity theorem over the null-eigenspace class). Neither ever gated
  the title claim.
- **Three independent adversarial reviews** rate the paper arXiv-ready in current form (hep-th / math-ph /
  math.AT). The generation **count stays OPEN**; three generations is explicitly not claimed.
- `.tex` is the arXiv source; `.md` is the readable copy; both in sync at v2.10.
- The one open frontier (`WC-FUNCTION-SPACE-EXT`, the analytic APS/end + family-index residual) is
  **post-publication** and disclosed in-text as caveat (c)/(e). It does not gate.

---

## Pre-flight (verify before starting — 5 minutes)

1. **Canon + git state.** Confirm the four staged RESULTS files are promoted in `CANON.md` and the tree is
   committed/pushed (JoeOps records this at commit `2abd12c`; verify it still holds so the public repo the
   paper's Data Availability section points to is current). If anything is uncommitted, commit + push first —
   the paper cites the public repo as its reproducibility backbone.
2. **Reproducibility harness green.** From a clean checkout:
   `python papers/candidates/located-not-forced/reproduce_all.py` should exit 0 (31/31 checks). This is what an
   external reviewer will run; confirm it before they do.
3. **`.tex`/`.md` parity.** Both at v2.10 per `STAGING-NOTES.md`; no action unless a later edit desynced them.

---

## Step 1 — Endorsement check (DO THIS FIRST; longest lead time)

A first-time submitter without an institutional email likely needs an **endorser** for `hep-th`.

- Log into the arXiv account and check whether it can submit to `hep-th`.
- If an endorser is required, that is a person-to-person request with turnaround measured in days — start it
  before touching anything else so it runs in parallel with the mechanical steps.
- **Joe-only.** Agents do not inspect or modify the arXiv account.

## Step 2 — One Overleaf compile

No TeX toolchain on this machine, so compile once on Overleaf and confirm zero errors. Visually check:

- the front-matter `\fbox` (the five load-bearing caveats box — it is tall);
- the wide Section 7 display equation;
- the Section 11 `longtable`;
- all references resolve (embedded bibliography, single file, no external `.bib`).

The source is a **single self-contained `.tex`** with `\pdfoutput=1` set — no multi-file upload needed.

## Step 3 — Shortened metadata abstract

The in-PDF abstract (~2,950 chars) **exceeds arXiv's 1,920-char metadata limit**. Paste the plain-text version
below into the arXiv abstract field instead (no LaTeX macros; character-count it before submitting — target
< 1,920). Adjust if the account's counter differs.

> We study the chirality and generation structure of an explicit real Clifford Rarita-Schwinger sector: the
> gamma-traceless rank-3/2 field of a real Clifford module Cl(p,q) with p+q=14 on a 128-dimensional spinor, with
> one generation identified with the 16 of Spin(10). The sector is motivated by, and reconstructed from, the
> matter proposal of Geometric Unity (GU); every GU-specific step is marked, and no theorem-grade result depends
> on GU being correct. We prove a two-primary meta-theorem: no enumerated obstruction to a net chiral generation
> count in this sector is an odd-prime congruence (the enumeration is complete for a delimited class C of
> covariant, sector-interior structures; completeness over the full function-space theory remains open). We also
> prove an index-conservation theorem: every linear Krein-isometric operator on the generation triplet conserves
> the net chiral index at zero, and the antilinear leg is closed over a delimited class. Via pi_3^s = Z/24 = Z/8
> + Z/3, every sector-interior obstruction lives in the 2-primary summand, so the generation count is external by
> structure (modulo an open analytic residual): an odd count is necessarily supplied by external background data
> coupled through the index theorem. We do not claim three generations; the "located, not forced" reading is
> contingent on a torsion-theoretic treatment of the obstruction data. All verification reported here is internal
> to the AI-directed process that produced it; no result has yet been independently replicated or peer-reviewed.

## Step 4 — Submit

- **Upload:** the single `.tex` (no separate bibliography).
- **License:** arXiv nonexclusive-distribution 1.0 (preserves journal options).
- **Primary category:** `hep-th`. **Cross-list:** `math-ph`, `math.AT`.
- **Title:** Located, Not Forced: Two-Primary Obstructions Cannot Force the Fermion Generation Count in a
  Clifford Rarita-Schwinger Sector.
- **Authors:** Joe Hernandez.
- **Comments field:** note the reproducibility repo + that the count is not claimed (short, factual).

## Step 5 — Post-live bookkeeping

Once it is confirmed live:

- Move this folder up to `papers/published/` and record the arXiv id here.
- Update the path references flagged in the readiness review: `README`, `RESEARCH-PROGRAM`, `papers/README`, the
  tri-repo division-of-labor doc, and canon `depends_on` frontmatter.

---

## Known risks (already mitigated in-text)

- **Moderation hold / `gen-ph` reclassification.** First-time submitter on a GU-adjacent subject. Mitigations
  are in the text: the GU-independence framing, the explicit "does not claim three generations" box, and the
  internal-verification caveat. Nothing to do pre-submission; just expect it as a possibility.
- **The internal-verification ceiling (caveat e)** is the paper's honest known weakness — only external human
  replication breaks it. `reproduce_all.py` + `REVIEWER.md` make that one command away; the optional
  `HARDENING-QUEUE.md` items (H1-H9) lower the external-review barrier further but **do not gate submission**.

## Not authorized by this runbook

arXiv submission by an agent · external account inspection/update · any posting, emailing, or announcement ·
claim promotion or claim-status change · editing the frozen submission paper without maintainer go.
