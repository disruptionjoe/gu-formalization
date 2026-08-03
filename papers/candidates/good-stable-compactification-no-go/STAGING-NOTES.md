---
title: "Staging notes: Compact-Image Obstructions for a Hyperbolic Grading in Sp(32,32)"
status: "v1.0.0 post-ready; release package verified"
updated: "2026-08-03"
---

# Staging notes

## Publication decision

Joe approved the mathematical title and the removal of the detailed GU
application. The paper is a standalone finite-dimensional result. The v0.5
hostile specialist pass found no fatal issue and independently confirmed the
concrete calculation, but identified eleven hardening actions. All are
dispositioned in v0.6. The final v1.0.0 hostile rerun found no unresolved
hardening potential. Its version-bound receipt is in
`review/adversarial-saturation-receipt-v1.0.0.md`.

## Theorem-grade core

For a faithful finite-dimensional tested representation:

- vectors fixed by an unbounded one-parameter group retain that group in their
  stabilizer;
- operators commuting with its infinitesimal generator retain the same group;
- maximal or minimal weight vectors retain the corresponding unipotent
  subgroup when `ad(Z)` and `dR(Z)` are real diagonalizable and the
  sign-matched eigenspace sum has a witness with nonzero nilpotent defining
  image.

Each stabilizer therefore has non-relatively-compact represented image and
cannot preserve a positive-definite inner product on the tested module.

## Concrete specialization

The `Sp(32,32)` matrix model is now self-contained. Its `ad(Z)` decomposition is

```text
8256 = 2080 + 4096 + 2080,
```

and both nonzero eigenspaces consist of mutually annihilating square-zero
matrices. The isotropic basis identifies the associated `|1|` parabolic and
abelian nilradical. SageMath, an independent exact property suite, and a narrow
Lean kernel accompany the written proof.

## Claim grade

- **Theorem-grade:** Proposition 1, Lemma 2, Theorem 3, and Corollary 6 under
  their written hypotheses.
- **Exact standard-structure specialization:** the quaternionic matrix model,
  dimensions, compact centralizer, and full three-grading calculation.
- **Mechanized:** seven narrow Lean declarations and two exact concrete
  certificate suites, with exact scope disclosed.
- **Open by scope:** non-extremal vectors, alternative positivity predicates,
  infinite-dimensional extensions, and all physical-model dictionaries.

## Current release boundary

Joe approved TeX, PDF, metadata, and archive preparation after the clean final
hostile passes. The resulting `zenodo-package-v1.0.0/` passed standalone
source-archive checks and page-by-page PDF visual QA. Public posting remains a
separate explicit action.
