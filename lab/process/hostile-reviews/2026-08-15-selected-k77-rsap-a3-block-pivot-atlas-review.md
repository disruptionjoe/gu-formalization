---
title: "Hostile review: selected-K77 complete split-A3 block-pivot atlas"
status: complete
reviewed_artifact: explorations/conditional-build/selected-k77-rsap-a3-block-pivot-atlas-2026-08-15.md
created: "2026-08-15"
verdict: PASS_WITH_FIRST_SINGULAR_JUMP_REQUIRED
---

# Hostile review

## Strongest overclaim

The dangerous sentence is “there are `306` split components.” There are not.
The number counts inertia-labelled sectors of a redundant finite block-pivot
cover. Different pivot skeletons overlap, and the underlying signature-`(2,2)`
form space is not being decomposed into `306` connected pieces. The artifact
states this at every use of the census.

## Strongest coverage attack

Permutation scalar-`LDL^T` charts do not cover every nonsingular symmetric
form. An invertible symmetric matrix can have every diagonal entry zero, so no
permutation creates a scalar first pivot. The completion succeeds only because
it admits `2 x 2` pivots. When the active Schur complement has zero diagonal,
nonsingularity guarantees a nonzero off-diagonal entry and hence a block
`[[0,b],[b,0]]` with determinant `-b^2`. The determinant factorization keeps
the residual Schur complement nonsingular, completing the induction.

## Primitive and topology attack

Some block-inertia domains need not be contractible. The proof does not use
contractibility. It uses the naturality of the tautological one-form under an
actual cotangent lift, which is a strict global identity on every overlap.
Therefore a loop inside a block chart cannot manufacture the missing
primitive defect. This is stronger and more appropriate than extending the
predecessor's positive-log-cell argument by analogy.

## Moment-map attack

The probe does not encode fifteen nonlinear `sl4` moment functions in every
block coordinate system. The invariant statement is that the charts describe
the same point of `T*(SL4/SO(2,2))`, whose cotangent moment map is globally
defined; coordinate transition cannot change it. The exact certificate checks
the finite cover, discrete actions, a genuinely nonlinear rational cotangent
overlap and triple closure. This supports atlas naturality, not a new formula
for the moment image.

## Scope attack

Covering the whole cotangent factor closes its restriction to the split
regular moment locus. It does not construct a compact or mixed `A3` real form
and does not cross a singular centralizer jump. In particular, no result here
supplies the required `91 -> 90` differential-rank loss on the first target
wall.

## Verdict

Accept at the stated grade: the complete split-`A3` regular cotangent/moment
atlas closes through a finite signed block-pivot cover, and its transition
cocycles are strict. Require a separate first singular-jump construction
before any all-strata RSAP claim.
