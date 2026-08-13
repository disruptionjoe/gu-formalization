---
artifact_type: conditional_physics_ledger_summary
created: 2026-08-12
ledger_version: "0.207"
run_id: RUN-20260812-131002-gu-i2b-global-primalizer-descent
---

# Conditional physics ledger v0.207

The action-owned `H_q`-fixed Euler primalizer now globalizes on the admitted
associated residual bundle.  A chosen global Spin frame is unnecessary: the
two central signs of each local Spin lift give the same adjoint transport, and
`tau_q` and `P_+=(1+tau_q)/2` obey exact direct/sequential descent on a
noncommuting three-patch cocycle across all `392` real target coordinates.

The pure-frame moving term is also exact:

```text
dot P_+ = (1/2)[L,tau].
```

It has rank `56`, satisfies differentiated projector and action-adjoint
identities, and cannot be frozen: doing so fails on `56` basis directions.
Moving-projector and moving-residual terms restore first-variation covariance.

This does not identify source `epsilon`, choose the full `U(64,64)` versus
two-`U(32,32)` connection parent, or assemble arbitrary trace-`q`, Hodge,
Shiab, connection, observation and field variations.  The complete
Euler/preboundary construction and physical vacuum remain open.

```text
Ledger v0.207 — 82/82 target rows mapped (100%)
32 SAME · 19 DIFFERS · 26 NEEDS · 5 OVER-DETERMINED
Residue: 84 continuous + >=19 function-valued + 9 discrete forks
Tightness: T4x1 T3x3 T2x1 · scoped quotients: 5
Headline delta: none
Frontier: 1 named condition closed · 0 opened · 1 remains
Rows migrated: RA-E1, RA-E3, LT-SM6
```

Next: assemble the complete arbitrary-field derivative packet and derive the
Euler and presymplectic preboundary classes, running full-`U(64,64)` and the
block-two-half reduction as separate action-parent comparators.
