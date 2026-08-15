---
title: "Hostile review: mixed-A2 factor and adjacent-transition type gate"
status: complete
doc_type: hostile_review
created: "2026-08-15"
target: explorations/conditional-build/selected-k77-rsap-a2-mixed-real-form-and-transition-gate-2026-08-15.md
verdict: PASS_WITH_CLAIM_NARROWING
---

# Hostile review: mixed-A2 factor and adjacent-transition type gate

## Strongest overclaim

Completing the three-real-form principal-pair census does not construct an
adjacent-chart atlas. The result was narrowed to a transverse-factor theorem;
pairwise transitions, the noncommuting triple, deeper strata, zero charge and
global RSAP remain explicitly open.

## Strongest contrary construction or counterexample

Indefinite self-adjoint operators can have non-real spectrum and defective
Jordan blocks, so an ordinary spectral-theorem argument would be false. The
mixed proof instead uses the complete pseudo-Hermitian canonical families:
real Jordan blocks, real semisimple blocks, and a real `2x2` block for a
non-real conjugate pair. Exact controls include the regular nilpotent and the
non-real-pair regular semisimple cases. No uncovered three-dimensional
spectral type was found.

## Weakest reproducibility or propagation seam

The executable certificate validates canonical representatives and stabilizer
ranks, while completeness of the representative list is theorem-level. The
write-up now states that dependence directly. Propagation was also narrowed:
the transition comparison cannot reuse the orthogonal-factor permutation
argument because four dimensions move between the leaf and transverse blocks.

## Transition challenge

The naive instruction to compare the `A1` and `A2` cotangent potentials is
ill-typed: their bare transverse domains have dimensions 16 and 20. The review
requires an explicit 20D common refinement
`O_4 x X_4 x T*R^6 -> X_10 x T*R^5`; absent that map, the honest verdict is
`TYPE-MISSING`, not “cocycle failed” and not “cocycle passed.”

## Verdict

`PASS_WITH_CLAIM_NARROWING`. The mixed factor is constructed at the same exact
grade as the split and compact factors. Adjacent gluing advances to a named,
dimension-checked common-refinement object but remains open.
