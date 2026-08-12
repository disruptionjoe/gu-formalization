---
artifact_type: conditional_physics_ledger_summary
created: 2026-08-12
ledger_version: "0.203"
run_id: RUN-20260812-110014-gu-i2b-full-unitary-image-covariance
---

# Conditional physics ledger v0.203

The v0.202 rank theorem was stronger than its own fence.  The phase-completed
`Cl(7,7)` basis is exactly the complete pointwise `u(64,64)` algebra:

```text
8,256 real-phase + 8,128 imaginary-phase = 16,384 directions.
```

Only Clifford grades `0,2,4` can reach the grade-one displasion target through
the selected Shiab.  Therefore v0.202's `99,463` columns already exhaust every
relevant full-unitary pointwise direction.  Their image has rank `364`; the
target raises it to `365`, both at q13 and at a held-out q12 representative.
The block `u(32,32)+u(32,32)` subgroup cannot restore a target absent from its
full parent's image.

```text
Ledger v0.203 — 82/82 target rows mapped (100%)
32 SAME · 19 DIFFERS · 26 NEEDS · 5 OVER-DETERMINED
Residue: 84 continuous + >=19 function-valued + 9 discrete forks
Tightness: T4x1 T3x3 T2x1 · scoped quotients: 5
Headline delta: none
Frontier: 2 named conditions closed · 0 opened · 3 remain
Rows migrated: RA-E1, RA-E3, LT-SM6
```

Next: compute derivatives of moving `H_q`, Hodge and Shiab in the global
source-full connection, then assemble the complete first-shell and
second-action Euler/preboundary equations.  Another pointwise coefficient-bank
search is no longer informative.
