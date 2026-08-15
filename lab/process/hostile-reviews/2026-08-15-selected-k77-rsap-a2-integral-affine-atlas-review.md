---
title: "Hostile review: compact-A2 integral-affine atlas"
status: complete
doc_type: hostile_review
created: "2026-08-15"
target: explorations/conditional-build/selected-k77-rsap-a2-integral-affine-atlas-2026-08-15.md
verdict: PASS_WITH_REAL_FORM_AND_HIGHER_STRATUM_CONTINUATION
---

# Hostile review: compact-A2 integral-affine atlas

## Strongest overclaim

Atlas closure does not resurrect a global diagonalizing section and does not
erase the nonzero fixed-charge Hopf period. It uses the two Cartan angles that
the full 98D carrier already owns. The result is therefore a global
multi-chart classical symplectic/moment construction, not one exact relative
orbit chart, a prequantization, or an all-strata RSAP.

## Strongest contrary construction or mistyping

The dangerous shortcut is to add `phi dmu` by hand while leaving its owner
untyped. Here its owner is the existing conjugate Cartan coordinate. In local
common-refinement polarization the pair is `t dmu`; globally it is the
root-Cartan angle already inside `Spin_0(7,7)`. Its transition is inverse to
the diagonalizer clutching. No new dimension or external line bundle is
introduced.

## Triple-overlap challenge

Local logarithms do not themselves form a real-valued Cech cocycle: their
triple sum is `2 pi n_ijk`. The construction would fail if the conjugate were
an unquotiented real coordinate. It is a Cartan angle modulo the coroot
lattice, so the integer translation is identity. Both simple-root generators
and their sum are checked, as are the Weyl involutions and braid relation.

## Prequantum-integrality challenge

No condition `mu in weight lattice` is used. Such a condition would be needed
to exponentiate the fixed-charge orbit class as a prequantum line. The present
cancellation is instead the canonical cotangent cancellation between a
bundle transition and its existing conjugate angle, valid for every real
regular charge. The paper states no quantization result.

## Singular-smoothness challenge

Vanishing `mu_alpha d tau_alpha` at a wall is necessary for circle collapse,
not by itself a proof of every higher-stratum smooth chart. The prior compact
`A1` and principal `A2` homogeneous factors separately supply the smooth local
models and rank schedules. This packet proves their lattice, primitive and
moment compatibility. Split/mixed globalizations and higher root subsystems
remain the next gates.

## Reproducibility seam

The executable certificate checks the exact `A2` root arithmetic, the full
one-form coefficient identity, integer triple closure, Weyl cotangent lifts,
dimension/rank schedules, collapse residues, registry pointers and claim
ceilings. It does not use floating-point monodromy sampling.

## Verdict

`PASS_WITH_REAL_FORM_AND_HIGHER_STRATUM_CONTINUATION`. The compact `A2`
multi-chart atlas closes at classical symplectic, moment, lattice and first
collapse-compatibility grade. The single-section obstruction remains intact.
