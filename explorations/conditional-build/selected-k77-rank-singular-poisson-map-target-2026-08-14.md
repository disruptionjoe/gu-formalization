---
title: "Selected-K77 rank-singular all-charge Poisson-map target"
status: active_research
doc_type: construction_result
created: "2026-08-14"
registry: lab/process/selected-k77-rank-singular-poisson-map-target.json
probe: tests/channel-swings/selected_k77_rank_singular_poisson_map_target_probe.py
grade: "EXACT TARGET-CLASS AND LOWER-BOUND RESULT; NO ALL-CHARGE CONSTRUCTION"
canon_verdict_change: none
---

# Selected-K77 rank-singular all-charge Poisson-map target

## Result first

The below-182 carrier question now has a precise weaker target. Seek a smooth
surjective Poisson map

\[
J:(M,\omega)\longrightarrow\mathfrak{so}(7,7)^*
\]

that is a submersion over the regular coadjoint locus and is allowed to lose
differential rank on singular strata. Call this an **RSAP map**: a
regular-submersive, all-charge Poisson map.

This is strictly weaker than an all-charge Poisson submersion and strictly
stronger than the existing generally disconnected regular-semisimple atlas,
which does not cover singular charges. It is also distinct from a map whose
domain is a stratified symplectic space rather than one smooth symplectic
manifold.

Every RSAP domain obeys

\[
\dim M\ge 98,
\]

because its restriction over the rank-84 regular locus is a Poisson
submersion and the exact regular bound is `91+7=98`. The zero-orbit bound 182
does not transfer: RSAP explicitly permits `dJ` to lose rank there, so the
submersion hypothesis used by that bound is absent.

Thus the honest smooth RSAP search interval is

```text
98 <= dim(M) < 182
```

for a genuinely smaller candidate. No existence claim is made.

## Differential-topology control

Surjectivity does not imply submersivity at every value. The exact toy map

```text
J(q,p)=q^3 : (R^2,dq wedge dp) -> (R, zero Poisson)
```

is surjective and Poisson, but `dJ=3q^2 dq` vanishes over the singular value
zero. This does not model `so(7,7)*`; it is the planted control preventing the
all-charge submersion inequality from being applied after its hypothesis has
been removed.

## First executable construction gate

The current 98-dimensional union `Spin_0(7,7) x C` covers the complete
regular-semisimple locus chamber by chamber. The first RSAP gate is not the
zero orbit. It is one codimension-one discriminant wall shared by adjacent
real Cartan chambers.

A candidate wall attachment must provide:

1. one smooth even-dimensional symplectic chart containing both adjacent
   regular pieces and a preimage of the wall;
2. a Poisson map agreeing with the existing moment maps on both regular sides;
3. controlled rank loss only on the wall, with no loss of surjectivity onto
   that local target neighborhood;
4. matching pullback symplectic forms and moment components on overlaps; and
5. a proof that the attachment does not silently become a stratified domain.

An exact obstruction at any one condition kills that wall attachment, not the
entire RSAP class. A passing wall chart opens the next orbit-type wall; only a
compatible cover through every singular stratum, including zero, produces an
all-charge RSAP realization.

No edge action, quantization, physical subcarrier, ledger, canon or public-
posture move follows.
