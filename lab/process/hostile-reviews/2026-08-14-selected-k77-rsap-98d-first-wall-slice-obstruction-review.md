---
title: "Hostile review — RSAP 98D first-wall slice construction"
status: complete
doc_type: hostile_review
created: "2026-08-14"
verdict: SURVIVES_AS_ONE_LOCAL_SPLIT_ROOT_WALL_ATTACHMENT
---

# Hostile review: RSAP 98D first-wall slice construction

## Verdict

`SURVIVES_AS_ONE_LOCAL_SPLIT_ROOT_WALL_ATTACHMENT`.

The cotangent homogeneous-space factor supplies the exact missing nonlinear
geometry. The product is symplectic of dimension `98`, is Poisson, is locally
surjective, and realizes the required rank changes. The result is local to one
generic split-root wall and cannot be promoted to a global RSAP.

## Charge 1: the “wall” was dimensionally misstated

A rank-`82` subregular locus is not a codimension-one hypersurface in the full
`91`-dimensional target. It is codimension one in the Cartan/invariant base and
codimension three in the full target. The construction uses the complete
`sl(2,R)^*` transverse factor, so the correction strengthens rather than kills
the local attachment.

## Charge 2: tangent sharpness was being mistaken for a nonlinear map

The predecessor supplied only symplectic vector spaces saturating the rank
bound. Here the carrier is the genuine smooth cotangent bundle
`T*(SL(2,R)/A)`, its moment map is the canonical equivariant cotangent moment
map, and its full coadjoint saturation is `sl(2,R)^*`. The exact block identity
`dJ Pi dJ^T=pi` is a certificate of that nonlinear construction, not its
definition.

## Charge 3: the new chart might fail to match the old chamber atlas

On each hyperbolic regular component, an `A` gauge sends the annihilator
covector to `lambda(E+F)` and fixed conjugation sends `E+F` to the split Cartan
generator. The tautological cotangent potential then becomes the old
`<lambda,g^-1dg>` potential. Both signs of `lambda` are present. The regular
overlaps therefore match; at zero the gauge fails while the cotangent bundle
itself remains smooth, which is precisely the desired attachment.

## Charge 4: transverse surjectivity might cover only the split side

The off-diagonal annihilator plane contains split, elliptic, nilpotent and zero
representatives. Trace/determinant classification and equivariance give full
coadjoint saturation. Thus the chart covers a target neighborhood, not only
two Cartan rays.

## Charge 5: one wall was being promoted to all charges

No compatibility is proved for other real wall types, simultaneous root
vanishing, deeper singular strata or zero charge. In particular, the eventual
rank-`49` ceiling at zero remains entirely unconstructed. Global RSAP existence
stays open and the `182`-dimensional cotangent group remains the known
all-charge fallback.

## Consequence

Accept the first split-root wall attachment. Next classify the complete
rank-`82` wall family and prove pairwise and first triple overlap cocycles.
Reject every physical, action-owned, stationary, quantum, ledger, canon or
public-posture promotion.
