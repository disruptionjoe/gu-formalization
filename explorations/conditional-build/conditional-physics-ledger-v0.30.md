---
artifact_type: conditional_physics_ledger_summary
created: 2026-08-06
status: CURRENT_APPEND_ONLY_LEDGER__ACTION_SPIN_LC_RANK9_SCOPE_CORRECTION__STATIONARY_SELECTED_METRIC_HESSIAN_EXACT__DIFFEO_WARD_TOTALIZATION_OPEN
machine_ledger: lab/process/conditional-physics-ledger-v0.30.json
predecessor: explorations/conditional-build/conditional-physics-ledger-v0.29.md
---

# Conditional physics ledger v0.30

## Meter

```text
Ledger v0.30 — 82/82 active target rows mapped (100%)
33 SAME · 19 DIFFERS · 24 NEEDS · 6 OVER-DETERMINED
Residue — 84 continuous + >=19 function-valued + 9 forks
Quotients ranked — 4 scoped
```

The denominator, verdicts, reason kinds, revival triggers, residue and quotient
count do not change. Five distances migrate.

## What moved

Layer 0 separates two objects that v0.29 had allowed to travel together. The
coordinate Christoffel symbol still has the previously proved rank-ten
principal map. The connection used by the selected action is the
symmetric-frame spin Levi-Civita connection; its principal map instead has
rank nine and exact longitudinal kernel `span{k tensor k}` for timelike,
spacelike and null covectors.

On the full algebraically stationary branch, the selected-action metric
Hessian pulled through that spin map is now exact. For positive `kappa_1`, its
rank/inertia is `9/(3,6,1)` on the timelike orbit, `9/(6,3,1)` on the
spacelike orbit, and `6/(3,3,4)` on the null orbit. The full algebraic gradient
vanishes there, so the second spin-connection and observation jets contribute
zero to this Hessian by the second-order chain rule. They remain live off shell
and at cubic order.

The isolated spin-connection block is not diffeomorphism-radical: its exact
cross residual against the ordinary metric gauge image has rank three on all
three causal orbits. Direct curvature, full-II, defect and observation terms
must therefore be assembled before any Ward, BV, physical or BFV promotion.

`LT-GR1`, `LT-GR2b`, `LT-GR5`, `LT-GR6`, and `LT-SM8` receive distance-only
migrations.

## Current highest-information gates

1. **Ward totalization:** assemble the direct curvature/full-II/defect and
   observation blocks with the exact stationary spin-LC Hessian, then cancel
   or retain the rank-three diffeomorphism residual. Do not restore the
   coordinate-Christoffel rank-ten statement to the action spin map.
2. **Physical quotient and domain:** only after that totalization, build odd
   BV, the global Krein/Green domain and unrestricted BFV.
3. **Second-layer/observer owner map:** separately construct or refute
   `I2B <-> ||II||^2`, then compare moving cubic, Euler and preboundary classes
   for `LT-GR3`.

P1/P2/P3 remain unused. Curt remains formally separate and no third lane is
promoted.
