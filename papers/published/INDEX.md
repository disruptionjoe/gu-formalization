---
title: "Publications index — the canonical record of what has actually been posted publicly"
status: canon
doc_type: publications-ledger
owner: gu-formalization
updated: "2026-08-03"
purpose: >-
  Single source of truth for which of this repo's artifacts are PUBLICLY POSTED (DOI / arXiv / URL).
  Other surfaces (Drafting Factory, project management) READ this; they do not maintain a competing
  posted-status truth. Reconcile against the live venue (Zenodo) via the runbook when status is in question.
reconcile_with: lab/methods/publication-status-reconciliation.md
---

# Publications index

The authoritative list of this repository's artifacts that are **actually posted publicly** — a live DOI /
arXiv id / URL, verified against the venue, not merely "post-ready." Folder membership in `published/` plus
an entry here is the status signal.

**Rule:** a paper is POSTED iff it appears in this table with a verified DOI/URL. "post-ready" is NOT
posted. Joe posts artifacts himself, often out-of-band — so when posting status is in question, reconcile
against Zenodo (see the runbook) and add what is found here.

## Posted artifacts

| id | title | type | DOI (version) | concept DOI | posted | author name used | source folder | venue |
|---|---|---|---|---|---|---|---|---|
| OVST | A Diagonal No-Go for Self-Valuations and an Invariance Classification | preprint | 10.5281/zenodo.21343484 | 10.5281/zenodo.21343483 | 2026-07-13 | Hernandez, Joe | `published/observer-value-selection-theorem/` | Zenodo |
| LNF | Located, Not Forced: A Scoped Two-Primary Audit of a Clifford Rarita-Schwinger Generation Carrier | preprint | 10.5281/zenodo.21515143 | 10.5281/zenodo.21515142 | 2026-07-23 | Hernandez, Joseph | `candidates/located-not-forced/` | Zenodo |
| CIO | Compact-Image Obstructions for a Hyperbolic Grading in Sp(32,32): Neutral, Grading-Even, and Extremal Order Parameters | preprint | 10.5281/zenodo.21779705 | 10.5281/zenodo.21779704 | 2026-08-03 | Hernandez, Joseph | `candidates/good-stable-compactification-no-go/` | Zenodo |

## Reconciliation log

- **2026-08-03** — Published and inspected *Compact-Image Obstructions*
  v1.0.0 at `10.5281/zenodo.21779705`. The public record shows Joseph
  Hernandez, Independent Researcher; the PDF as the default 13-page preview;
  CC BY 4.0; the repository and exact source-revision links; and all 15
  manifest-listed files. Every Zenodo-reported MD5 matches the frozen local
  artifact. The concept DOI is `10.5281/zenodo.21779704`; the complete receipt
  is `papers/candidates/good-stable-compactification-no-go/FINAL-RELEASE-RECEIPT-v1.0.0.md`.
- **2026-07-23** — Published and inspected LNF v1.0.0 at
  `10.5281/zenodo.21515143`. The public record shows Joseph Hernandez,
  Independent Researcher; `main.pdf` as the default 18-page preview; the
  verified ZIP supplement; CC BY 4.0; and the repository in both the software
  and related-work fields. Public MD5 values match the frozen local artifacts.
  The concept DOI is `10.5281/zenodo.21515142`.
- **2026-07-22** — Reconciled against Zenodo (author searches `"Hernandez, Joe"` and `"Hernandez, Joseph"`;
  title searches). **Result: OVST is the ONLY posted artifact.** Fixed three drifted surfaces:
  1. This repo: OVST was still under `candidates/` and `published/` was empty — moved OVST to `published/`
     and created this ledger.
  2. `joe-project-management/records/work-items.yaml` (WI-070): mis-attributed DOI `21343484` to the
     generation-count "obstruction paper" and marked it published. That DOI is **OVST**; the generation-count
     paper (`located-not-forced` / `generation-number-located-not-forced`) is **NOT posted**. Corrected.
  3. The "Hernandez, Joseph" Zenodo hit (`10.5281/zenodo.21244606`, an education/pedagogy paper from
     Batangas) is a DIFFERENT person — not this author. Screened out.
- Ready for Joe to post (GO): `located-not-forced` (**deferral LIFTED; GO-to-post ratified 2026-07-22,
  publish FIRST**; Joe-side mechanical submission steps remain) and PP3 dark-energy pre-registration (frozen
  v0.3 2026-07-22). Sequence: after LNF, the odd-primary boundary paper (Part II, cites LNF). Other
  candidates remain in progress.
  **[SUPERSEDED — reconciled 2026-08-03 (audit F-02): BOTH items published 2026-07-23.**
  LNF v1.0.0: DOI `10.5281/zenodo.21515143` (concept `…21515142`), receipt
  `papers/candidates/located-not-forced/FINAL-RELEASE-RECEIPT-v1.0.0.md`, source tag `lnf-v1.0.0`.
  PP3 v1.0.0: DOI `10.5281/zenodo.21502234`, receipt in
  `drafting-factory/production/pp3-preregistration-note/ZENODO-PUBLICATION-RECEIPT-2026-07-23.md`
  (GU source commit `15c7e63`). Cross-reference: the Factory's AI-research-methodology paper
  (v0.5.0, DOI `10.5281/zenodo.21711582`, published 2026-07-31) cites five gu-formalization
  canon/posture files as its GU-METHOD-RECEIPTS case study.]
