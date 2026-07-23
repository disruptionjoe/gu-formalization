# Submission Runbook -- Located, Not Forced

**Prepared:** 2026-07-09; hardened 2026-07-23. **Paper version:** v2.13 working draft.
**Status:** HARDENING COMPLETE FOR MARKDOWN; FINAL PUBLICATION RECONCILE DEFERRED.
**Purpose:** a single linear checklist Joe can follow when he sits down to submit. This consolidates the
Joe-side steps that had accumulated across the readiness passes in `STAGING-NOTES.md` (v2.4 through v2.10).
`STAGING-NOTES.md` remains the full history; this file is the do-this-then-this.

This runbook prepares a submission. It is **not** authorization to submit. No agent performs any step here --
every action below is Joe's. Agents do not touch arXiv, inspect or update the arXiv account, or post anything.

---

## Where the paper stands

- Headline result is **theorem-grade and GU-independent**; honesty discipline clean.
- Both publication-gating work cards are **closed**: `WC-ENUM-COMPLETENESS` (class-C census complete, computed
  grade) and `WC-ANTILINEAR-BOUND` (index-nullity theorem over the null-eigenspace class). Neither ever gated
  the title claim.
- **Three independent adversarial reviews** rate the paper arXiv-ready in current form (hep-th / math-ph /
  math.AT). The generation **count stays OPEN**; three generations is explicitly not claimed.
- `.md` is the canonical hardening draft. Reconcile `.tex`, rebuild the PDF, and regenerate the release
  package only when final publication preparation resumes.
- At canon grade the open frontier remains the function-space analytic residual. Current exploration-grade
  evidence narrows it to the true-`Y14` fiber pushforward/source action. That calculation is
  **post-publication research**, is disclosed in-text, and does not gate this release.

---

## Pre-flight (verify before starting -- 5 minutes)

1. **Canon + git state.** Confirm the four staged RESULTS files are promoted in `CANON.md` and the tree is
   committed/pushed (JoeOps records this at commit `2abd12c`; verify it still holds so the public repo the
   paper's Data Availability section points to is current). If anything is uncommitted, commit + push first --
   the paper cites the public repo as its reproducibility backbone.
2. **Reproducibility harness green.** From a clean checkout:
   `python papers/candidates/located-not-forced/reproduce_all.py` should exit 0 (31/31 checks). This is what an
   external reviewer will run; confirm it before they do. **Pre-verified 2026-07-23: 31/31 passed, exit 0
   (~23s in the pinned research environment), with no runtime warning.**
3. **`.tex`/`.md` parity.** Deferred by design during Markdown hardening. This is a publication gate, not a
   current research-draft gate.

---

## Step 1 -- Endorsement (DO THIS FIRST; longest lead time; MANDATORY)

Per arXiv's **updated policy of 2026-01-21**, an independent researcher with no institutional affiliation
**must** obtain a personal endorsement for `hep-th`. Institutional email alone no longer qualifies, and there is
no bypass -- you cannot "just post it" to arXiv. (Sources verified 2026-07-09:
`blog.arxiv.org/2026/01/21/attention-authors-updated-endorsement-policy`, `info.arxiv.org/help/endorsement.html`.)

The good news: it's **one** endorser, one targeted email, and arXiv forbids mass-emailing them anyway. Your own
bibliography contains the eligible candidates (Wan-Wang-Yau, Juven Wang, García-Etxebarria & Montero).

- **Full step + copy-paste request note + who to ask:** `ENDORSER-REQUEST-DRAFT.md` (this folder).
- Start the arXiv submission first to receive your endorsement code, then send the note to one endorser.
- **Joe-only.** Agents do not inspect/modify the arXiv account or send the request.

### Step 1b (parallel) -- post publicly today with no endorsement

If you want it live and citable immediately while the endorsement lead time runs, post to **Zenodo** (DOI, no
gate, reputable). This does not block arXiv or a journal later. Checklist: `ZENODO-RELEASE-CHECKLIST.md`.
Avoid viXra-style no-gate dumps -- they undercut the qualified/serious posture.

## Step 2 -- Compile and preview

A preliminary v2.13 source compiled locally with Tectonic and was visually checked, but the Markdown has
changed since. At final publication time, reconcile the TeX from the canonical Markdown, then compile and
inspect:

- the front-matter `\fbox` (the five load-bearing caveats box -- it is tall);
- the wide Section 7 display equation;
- the Section 11 `longtable`;
- all references resolve (embedded bibliography, single file, no external `.bib`).

The source is intended to remain a **single self-contained `.tex`** with an embedded bibliography. Do not
reuse the preliminary PDF as the article of record.

## Step 3 -- Shortened metadata abstract

The in-PDF abstract (~2,950 chars) **exceeds arXiv's 1,920-char metadata limit**. Paste the plain-text version
below into the arXiv abstract field instead (no LaTeX macros; character-count it before submitting -- target
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

## Step 4 -- Submit

- **Upload:** the single `.tex` (no separate bibliography).
- **License:** arXiv nonexclusive-distribution 1.0 (preserves journal options).
- **Primary category:** `hep-th`. **Cross-list:** `math-ph`, `math.AT`.
- **Title:** Located, Not Forced: Two-Primary Obstructions Cannot Force the Fermion Generation Count in a
  Clifford Rarita-Schwinger Sector.
- **Authors:** Joseph Hernandez (Independent Researcher).
- **Comments field:** note the reproducibility repo + that the count is not claimed (short, factual).

## Step 5 -- Post-live bookkeeping

Once it is confirmed live:

- Move this folder up to `papers/published/` and record the arXiv id here.
- Update the path references flagged in the readiness review: `README`, `RESEARCH-PROGRAM`, `papers/README`, the
  tri-repo division-of-labor doc, and canon `depends_on` frontmatter.

---

## Known risks (already mitigated in-text)

- **Moderation hold / `gen-ph` reclassification.** First-time submitter on a GU-adjacent subject. Mitigations
  are in the text: the GU-independence framing, the explicit "does not claim three generations" box, and the
  internal-verification caveat. Nothing to do pre-submission; just expect it as a possibility.
- **The internal-verification ceiling (caveat e)** is the paper's honest known weakness -- only external human
  replication breaks it. `reproduce_all.py` + `REVIEWER.md` make that one command away; the optional
  `HARDENING-QUEUE.md` items (H1-H9) lower the external-review barrier further but **do not gate submission**.

## Not authorized by this runbook

arXiv submission by an agent · external account inspection/update · any posting, emailing, or announcement ·
claim promotion or claim-status change · editing the frozen submission paper without maintainer go.
