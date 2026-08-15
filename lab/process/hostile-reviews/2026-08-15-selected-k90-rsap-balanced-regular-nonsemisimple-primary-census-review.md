---
title: "Hostile review: K90 balanced regular-nonsemisimple primary census"
status: complete
reviewed_artifact: explorations/conditional-build/selected-k90-rsap-balanced-regular-nonsemisimple-primary-census-2026-08-15.md
created: "2026-08-15"
verdict: PASS_COMPLETE_REGULAR_NONSEMISIMPLE_LOCUS__SINGULAR_MIXED_JORDAN_AND_ZERO_NEIGHBORHOOD_OPEN
---

# Hostile review

## Two positive controls presented as an exhaustion attack

K90 does not extrapolate the K89 `[5,1]` and `[3,1]` controls. It implements
the complete four-species real skew-adjoint primary grammar and enumerates all
dimension, signature, Jordan-size and sign-characteristic combinations at
ambient rank seven. The result is `547` signed structural configurations.

## Complex Jordan partitions mistaken for real orbits attack

The census retains real versus imaginary versus loxodromic primary type,
both pure-imaginary sign characteristics, zero-primary signed rows and total
signature `(7,7)`. It calls the result a structural-family count, not an
individual adjoint-orbit count; the continuous spectral parameters remain
continuous.

## `m=1` overcount attack

At zero rank one the regular zero partition is `[1,1]`. Its two rows are
equal, so swapping their signs does not create a new signed partition. The
census uses three unordered sign multisets rather than four ordered pairs.

## Blockwise involutions do not sum to the balanced signature attack

The probe does not stop at separate block existence. It searches all
blockwise grading choices and checks the total restricted signature. Every one
of the `547` configurations reaches `(3,4)|(4,3)`.

## Non-diagonal grading basis attack

Real and loxodromic reversing involutions exchange paired generalized
eigenspaces, so elementary orthogonal generators are not individually
homogeneous. The probe therefore projects each complete local orthogonal basis
with `Y+RYR` and `Y-RYR` before computing the fixed adjoint rank. All `88`
canonical signed and graded primary-block variants are tested.

## Zero-primary hidden fixed centralizer attack

The extra centralizer direction on `[2m-1,1]` joins the singleton to the
long-chain endpoints. It is fixed when the two grading colors agree. The
census explicitly requires opposite colors, verifies that local fixed
centralizer is zero, and then rechecks balanced signature existence for all
`547` assembled configurations.

## Numerical rank attack

Finite-field reduction gives every canonical primary block its exact regular
centralizer dimension and proves its fixed centralizer is zero. Coprime
primary decomposition makes the global centralizer the direct sum of those
local centralizers; the rank-unit equation makes its dimension seven. Hence
all `547` rows have ambient/fixed/moving ranks `84/42/42`. A repeated-parameter
whole-matrix mutation independently detects the expected rank loss.

## Regularity smuggled in by generic parameters attack

Distinct nonzero primary parameters are part of the declared regular grammar.
A mutation repeats two real primary values; its centralizer enlarges and its
adjoint rank drops below `84`, placing it outside the certified table and
inside the next singular census.

## Regular plus nilpotent implies neighborhood attack

False. K88 covers regular semisimple elements, K89 pure nilpotents, and K90
regular mixed elements. Singular semisimple centralizers can carry nilpotent
orbits on multiplicity spaces that none of those results classify. The
singular mixed-Jordan locus remains open, so zero-neighborhood coverage,
surjectivity and RSAP remain open.

## Verdict

Accept complete regular-nonsemisimple image coverage and rank-91
submersivity. Advance the exact gate to singular semisimple centralizers with
internal nilpotent orbits; do not repeat regular-Cartan or pure-nilpotent
comparators.
