---
artifact_type: hostile_review
created: 2026-08-14
target: explorations/conditional-build/selected-k77-sr1d-nonparallel-source-graph-cokernel-2026-08-14.md
verdict: SURVIVES_AS_FIXED_POINT_ONE_JET_TWO_JET_CLASS_KILL__DISTINCT_CANONICAL_FIRST_JETS_REMAIN_OPEN
---

# Hostile review: SR-1D nonparallel source-graph cokernel

## Verdict

`SURVIVES_AS_FIXED_POINT_ONE_JET_TWO_JET_CLASS_KILL__DISTINCT_CANONICAL_FIRST_JETS_REMAIN_OPEN`.

The obstruction is an exact factorization, not a failed numerical solve. On
the fixed one-jet, the momentum derivative and differentiated translation row
are the same linear map. Requiring the source field equation therefore kills
the entire candidate metric-graph image.

## Strongest attacks

### Only the parallel second jet was evaluated

Rejected. The arbitrary correction `h_m` is retained symbolically. Its
responses are `j1E_T=A h_m`, `j1E_B=2A h_m` and `j1p=A h_m`. The conclusion
holds on the kernel of the differentiated translation equation, independently
of which kernel representative is chosen.

### The map could be zero because the second-jet variables were mistyped

Rejected. The `196 x 9,555` map has rank `195`, and a planted unconstrained
cell fires both translation and momentum. The constrained image is zero
because `A h_m=0` is imposed, not because `A` is dead.

### Bianchi or Spencer freedom could restore the trace

Rejected. Those conditions restrict the translation-compatible domain
further. They cannot give a nonzero image under a map already zero on the
larger kernel of `A`.

### Primitive epsilon might allow a nonzero momentum derivative

Rejected in this class. Primitive epsilon is weaker here: its formal-adjoint
term factors through `j1p`, and the independent moving-Shiab term is already
zero on the fixed one-jet. Differentiated translation has already forced the
full common-basis `j1p` to zero.

### The graph map itself was not reconstructed for every kernel vector

Rejected as unnecessary. The fixed-`varpi` Levi-Civita graph is a linear
formal adjoint applied after `j1p`. Exact zero of the full `14 x 196` input
annihilates it under any sign or basis convention. The predecessor's planted
momentum derivative proves the graph is live off that zero input.

### A higher jet could change first-order metric stationarity

Rejected over the declared fixed one-jet. The graph return depends on the
first derivative of the Euler momentum, which is fixed by the second jet.
Higher prolongation cannot change this already-nonzero first variation while
leaving the lower jet fixed.

### This kills every canonical Zorro background

Rejected. A distinct point/first-jet branch can change the affine base and the
relation between `j1p` and `j1E_T`. A different source-derived reconstruction
can change `B_Z`. The result covers only the two exact SR-1C roots with their
declared thirteen-cell first-jet correction.

## Required successor

Move to `SR-1E`: construct or exhaust a genuinely distinct canonical
point/first-jet branch and recompute the complete source rows. The first
discriminator is whether its on-shell `j1p` retains a component independent
of differentiated translation. Do not spend another solve on second jets over
the now-exhausted SR-1C one-jet, and do not enter VRS-6 without a stationary
background.
