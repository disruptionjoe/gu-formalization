---
artifact_type: conditional_physics_ledger_migration
created: 2026-08-09
status: CURRENT_APPEND_ONLY_LEDGER_V0_126
predecessor: lab/process/conditional-physics-ledger-v0.125.json
canon_verdict_change: none
---

# Conditional physics ledger v0.126

## Progress meter

```text
Ledger v0.126 — 82/82 mapped (100%)
32 SAME · 19 DIFFERS · 26 NEEDS · 5 OVER-DETERMINED
Residue — 84 continuous; conditional parent range 84..86
Function-valued slots — >=19
Open discrete forks — 9
Scoped quotients — 5
```

## Migration

v0.125 remains immutable. Six Lagrangian rows move in distance only after the
metric/epsilon off-slice covector image is K-lifted and closed under the exact
grade-two first-action Hessian.

The successive ranks belong to different objects: `89` is one fixed-symbol
covector image, `174` its invariant tangent, and `464` the closure of only the
three stored causal representatives. Exact spatial covariance adds the fourth
observed basis covector. The full `X^4` symbol family and both stationary
branches close on one rank-`594` grade-two source subspace, so the least known
local-principal tangent is `321 + 594 = 915`, proper inside the `1,571`
low-grade coordinates.

No current action-derived differential owns a quotient of the leakage. The
matched-`q` Noether result is a four-parameter kernel identity, while primitive
epsilon boundary transformations retain a live moment map. A future BV
differential remains open but cannot be supplied by relabelling either fact.

## Rows moved

- `LT-GR1`: the local-principal tangent is exactly narrowed to `915`; lower
  order, derivative jets and its global source-natural subbundle remain open.
- `LT-GR2b`: both exact branches share the same local-principal tangent;
  physical-horn selection and observation descent remain open.
- `LT-GR2c`: tangent closure supplies no scale, amplitude or normalization.
- `LT-GR3`: build the lower-order/jet first-action Hessian on `915`, then
  compare expanded parents without inventing a relative coefficient.
- `LT-GR5`: augmented-torsion principal closure advances; the BV differential,
  trace and analytic domain remain open.
- `LT-GR6`: endpoint charge survives; gauge/ghost, `Dmax/Dmin`, BV-BFV and
  Hilbert-stress reduction remain open.

No verdict, residue, quotient, P1/P2/P3, canon or public posture changes.

Evidence:

- `explorations/conditional-build/selected-k77-minimal-hessian-tangent-closure-2026-08-09.md`;
- `lab/process/selected-k77-minimal-hessian-tangent-closure.json`;
- primary exact probe `48/48 PASS`;
- independent Sage/FLINT `19/19 PASS`.
