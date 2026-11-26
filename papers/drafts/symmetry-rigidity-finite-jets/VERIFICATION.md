---
title: Verification and reproduction of the symmetry-rigidity draft
status: process
doc_type: verification-note
created: '2026-11-26'
---

# Verification boundary

The main manuscript is a written proof. Analytic CK existence, orbit saturation, spin geometry and physical interpretation are **not** claimed to be fully Lean-formalized.

## Mathematical custody

The prior reviewed results and certificates are pinned at `6b03209312a9ae4a73798e45fb909601c9c148b3`:

- [Rotation-rigidity report](../../../explorations/conditional-build/source-action-rotation-rigidity-2026-11-26.md), [exact certificate](../../../lab/process/source-action-rotation-rigidity.json), and [finite Lean core](../../../Lean/GUFormalization/RotationRigidity.lean).
- [Covariant-jet report](../../../explorations/conditional-build/source-action-covariant-jet-ambiguity-2026-11-26.md), [exact certificate](../../../lab/process/source-action-covariant-jet-ambiguity.json), and [finite Lean core](../../../Lean/GUFormalization/CovariantJetAmbiguity.lean).

Their 306 and488 finite controls and9 and13 Lean lemmas were verified in the preceding proof waves. Their code and proof-assistant files are unchanged in this drafting wave; certificate hashes are checked rather than presenting old checks as new execution. The manuscript adds a self-contained ordinary local Dirac example and strengthens the exposition of the germ-domain argument. Those written derivations received two mathematical checks and a hostile editorial check, recorded in [review](review.md).

The appendix separates the finite algebra from the analytic proof. Normal trace invariants do not count particles, and the ordinary Dirac example is not evidence that GU selects that operator.

## Primary literature and novelty

1. [Bock et al., publisher PDF](https://ems.press/content/serial-article-files/38405), Proposition3.3, p.1172; [DOI](https://doi.org/10.4171/rmi/708). Equivariant CK and representation-based polynomial construction are prior methods.
2. [Brackx et al., preprint](https://arxiv.org/abs/1101.4516), [author full text](https://www.karlin.mff.cuni.cz/~soucek/soubory_clanku/CK_Hermit.pdf). Analytic and compatible polynomial CK extension.
3. [Xu and Sabadini, full text](https://link.springer.com/article/10.1007/s00006-024-01314-1), Theorems2.10-2.11. Restricted-class uniqueness is a contrary comparison, not an exception hidden from the reader.

The contribution is presented as a specific metric-fibre rigidity/filtered-ambiguity synthesis. A bounded primary-source search does not establish worldwide priority. No venue recommendation or external review is used as an execution prerequisite.

## Rebuild and inspect

From the repository root, with Tectonic installed and its standard LaTeX/font bundle cached:

```sh
bash papers/drafts/symmetry-rigidity-finite-jets/build.sh
pdfinfo papers/drafts/symmetry-rigidity-finite-jets/manuscript.pdf
pdftotext -layout papers/drafts/symmetry-rigidity-finite-jets/manuscript.pdf /tmp/symmetry-paper.txt
pdftoppm -scale-to 1300 -png papers/drafts/symmetry-rigidity-finite-jets/manuscript.pdf /tmp/symmetry-paper-page
```

A fresh Tectonic installation may need one ordinary network-enabled compilation to populate missing standard fonts. This machine's restricted macOS process initially failed during system-configuration access; compilation completed through the normal authorized host execution after standard resources were available. No source or validation requirement was bypassed.

Final output:10 pages, searchable text, no undefined citations/references, no overfull or underfull boxes. All ten rendered pages were inspected. PDF timestamps may differ across rebuilds; bitwise reproducibility is not asserted. Current artifact hashes and claim-to-premise mapping are in [the premise ledger](CLAIM-AND-PREMISE-LEDGER.json).

## Repository checks

Required checks: unchanged scientific verdicts, choice snapshot and program_focus; exact admitted footprint; draft lifecycle retained; frontmatter population; relevant native program-focus/typed-carrier/claim/source-routing/Lean-inventory/currency gates; local links; LaTeX labels/citations; diff whitespace; final publication attestation. These validate custody and packaging, not the analytic mathematics.
