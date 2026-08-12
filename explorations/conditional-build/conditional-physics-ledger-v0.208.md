---
artifact_type: conditional_physics_ledger_summary
created: 2026-08-12
ledger_version: "0.208"
run_id: RUN-20260812-133651-gu-i2b-full-trace-orbit-derivative
---

# Conditional physics ledger v0.208

The action-owned `H_q`-fixed Euler primalizer already globalizes on the
admitted associated residual bundle.  This version computes its complete
derivative over the fixed-norm normalized tautological trace orbit.

All `91` infinitesimal `so(6,4)` directions split exactly into a
`78`-dimensional trace stabilizer and a `13`-dimensional trace orbit.  In every
orbit direction,

```text
dot P_+ = (1/2)[L,tau].
```

has rank `56`, satisfies differentiated projector and action-adjoint
identities, and cannot be frozen: doing so fails on `56` basis directions per
orbit direction.  The 13 derivative images jointly span all `392` real target
coordinates, and moving-projector plus moving-residual terms restore
first-variation covariance with zero extra datum.

This does not identify source `epsilon`, choose the full `U(64,64)` action
parent, or assemble arbitrary DeWitt, Hodge, Shiab, connection, observation
and field variations.  The source statement `C^(32,32) + C^(32,32)` is a
carrier split; its block-preserving `U(32,32) x U(32,32)` subgroup is not
automatically two source-declared connection fields.  The complete
Euler/preboundary construction and physical vacuum remain open.

```text
Ledger v0.208 — 82/82 target rows mapped (100%)
32 SAME · 19 DIFFERS · 26 NEEDS · 5 OVER-DETERMINED
Residue: 84 continuous + >=19 function-valued + 9 discrete forks
Tightness: T4x1 T3x3 T2x1 · scoped quotients: 5
Headline delta: none
Frontier: 1 named condition closed · 0 opened · 1 remains
Rows migrated: RA-E1, RA-E3, LT-SM6
```

Next: assemble the remaining independent physical derivative packet and
derive the Euler and presymplectic preboundary classes.  Keep the full
`U(64,64)` principal parent, source `C^(32,32) + C^(32,32)` carrier split,
derived block-preserving subgroup and independent connection fields distinct.
