---
title: "The swing: ghost parity gives consistency, not chirality (a no-go for chiral selection in the matter Krein sector)"
status: active
doc_type: result
created: 2026-06-28
depends_on:
  - canon/ghost-parity-krein-synthesis.md
  - canon/h2-base-index-chirality.md
tests:
  - tests/generation-sector/swing_ghost_parity_chiral_selection.py
  - tests/generation-sector/t1a_kinematic_chirality_kill.py
---

# The swing: ghost parity gives consistency, not chirality

## What was tested

The "profound bridge" hoped that GU's matter Krein sector and Turok-Bateman's ghost-parity quantization of
quadratic gravity are the same problem with one shared `Z2`, and that this `Z2` could turn the vectorlike
self-dual triplet into three physical chiral generations. The swing tests that hope directly by splitting it
into two questions that turn out to have different answers (`swing_ghost_parity_chiral_selection.py`, on the
`(9,5)` triplet sector).

> **CORRECTION (A0 audit, 2026-06-28).** Where this doc or its siblings frame the Krein move as inside the
> single-group class, that is RETRACTED: by the Weyl unitarian trick the indefinite Krein form exists only
> because the internal gauge group is non-compact (SO(5,5), not SO(10)), so dropping Hilbert positivity is
> a SCOPE-EXIT (negating DG-A3), not an inside-class enrichment. The "internal block is non-compact SO(5,5)"
> note already anticipates this. The no-go and the consistent positive-norm sector are unaffected.

## Result: the bridge splits

**Positivity (the bridge HOLDS).** The physical (`J = +1`) sector of the Krein form is positive-definite
(`min K-eig = +1.000`); a consistent positive-norm Hilbert sector exists, and a ghost-parity-preserving
Krein-unitary toy dynamics is well defined (`S^dagger K S = K`, residual `2.7e-14`). So GU's matter sector
*does* admit a consistent indefinite-metric quantization of the Turok-Bateman type: the ghost parity earns
its positivity role. (Construction note: in the `(9,5)` build the internal block is the non-compact
`SO(5,5)`, so `sign(K)` need not commute with those generators; that gauge-equivariance print is an artifact
of the non-compact internal, not a physical failure, and the no-go below does not depend on it.)

**Chiral selection (a NO-GO).** The same ghost parity provably cannot make the physical sector net-chiral.
The Krein form on the triplet is purely cross-chirality (`||K(+,+)|| = ||K(-,-)|| = 1.8e-14`, machine-checked
here and in T1a across `(9,5),(7,7),(14,0)`), so every maximal positive-norm subspace is a graph of a
chirality-exchanging isometry and is exactly half left and half right. Net chirality is therefore `0` for the
canonical fundamental symmetry `sign(K)` (`-2.4e-15`) and for all eight sampled gauge-equivariant ghost
parities (`max |net| = 1.07e-14`). This is index conservation: a Krein-unitary dynamics cannot move the
chiral index, and the index is fixed at `0` by the cross-chirality structure.

## Verdict

**The profound positive is refuted.** Ghost parity supplies *consistency* (a positive-norm physical sector,
the genuine bridge to indefinite-metric quantization) but provably *not chirality*. So the chiral generation
count cannot come from GU's own ghost-parity quantization; it is necessarily external, an imported unit of
topological flux (an index), exactly as `canon/h2-base-index-chirality.md` concludes by the parity argument.
The two routes to a chiral 3 that T1a and H2 left standing are now both characterized: a base index (even on
every native channel; odd only with imported flux) and a ghost-parity dynamics (consistent, but cannot
chiralize). Neither is GU-internal.

**What survives is a novel no-go, not a profound positive.** The honest, publishable result is the negative:
*in the cross-chirality Krein structure of a Clifford Rarita-Schwinger matter sector, a ghost-parity (Turok-
Bateman type) quantization yields a consistent positive-norm theory but cannot supply a net chiral count; the
chirality is necessarily an external index.* This connects indefinite-metric quantization to the chirality
problem and sharpens, rather than evades, the obstruction. It is the favored outcome the six-axis
Distler-Garibaldi candidate already predicted (`canon/six-axis-candidate-krein-positivity-dg.md`): a
`G`-equivariant generation-mirror swap is a reality structure, so its physical eigenspace carries net index
`0`.

## Honest scope

Kinematic and machine-checked: the positive-definiteness, the cross-chirality, the net-`0` over the sampled
ghost parities. The no-go rests on the cross-chirality of `K` (exact) plus the structural graph argument
(maximal positive-norm subspaces of a hyperbolic form are 50/50). Still open, and unchanged by the swing:
whether GU's unbuilt source action realizes a ghost parity at all (no dynamics exists to check); and the
external-flux route remains available (it is simply not GU-internal). The swing closes the *internal* chiral
-selection question in the negative; it does not claim the external route is unavailable.
