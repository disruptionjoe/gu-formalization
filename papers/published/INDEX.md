---
title: "Publications index — the canonical record of what has actually been posted publicly"
status: canon
doc_type: publications-ledger
owner: gu-formalization
updated: "2026-07-22"
purpose: >-
  Single source of truth for which of this repo's artifacts are PUBLICLY POSTED (DOI / arXiv / URL).
  Other surfaces (Drafting Factory, project management) READ this; they do not maintain a competing
  posted-status truth. Reconcile against the live venue (Zenodo) via the runbook when status is in question.
reconcile_with: lab/process/runbooks/publication-status-reconciliation.md
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

## Reconciliation log

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
