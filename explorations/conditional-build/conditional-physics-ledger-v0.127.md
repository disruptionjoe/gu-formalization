---
artifact_type: conditional_physics_ledger_migration
created: 2026-08-10
status: CURRENT_APPEND_ONLY_LEDGER_V0_127
predecessor: lab/process/conditional-physics-ledger-v0.126.json
canon_verdict_change: none
---

# Conditional physics ledger v0.127

## Progress meter

```text
Ledger v0.127 — 82/82 mapped (100%)
32 SAME · 19 DIFFERS · 26 NEEDS · 5 OVER-DETERMINED
Residue — 84 continuous; conditional parent range 84..86
Function-valued slots — >=19
Open discrete forks — 9
Scoped quotients — 5
```

## Migration

v0.126 remains immutable. Six Lagrangian rows move in distance only after all
`51` infinitesimal generators of `so(1,3)+so(6,4)` preserve the exact rank-594
grade-two tangent fiber. Its source-natural decomposition is

```text
160 + 180 + 60 + 184 + 10 = 594,
```

with the `184` block equal to `H tensor (R id_N + so(6,4))` and the final `10`
the canonical normal contraction copy. It therefore defines an associated
subbundle conditional on a supplied observation reduction. A mixed ambient
generator expands `594 -> 727`, so ambient-Spin(7,7) invariance and a global
observation reduction are not claimed.

The exact basis is now a small dependency-hashed bank consumed without
replaying its heavy producer. No verdict, residue, quotient, coefficient,
datum, P1/P2/P3, canon or posture changes.

## Rows moved

- `LT-GR1`: natural principal tangent built; lower-order/jet closure and the
  global observation reduction remain open.
- `LT-GR2b`: both branches share the natural tangent; physical-horn selection
  and global descent remain open.
- `LT-GR2c`: the subbundle supplies no scale or normalization.
- `LT-GR3`: build the lower-order/jet first-action Hessian on the exact
  five-block tangent before comparing expanded parents.
- `LT-GR5`: augmented-torsion field ownership advances without a quotient.
- `LT-GR6`: endpoint charge survives; trace, domain, Hilbert stress and
  coupled BV-BFV remain open.

Evidence:

- `explorations/conditional-build/selected-k77-observation-stabilizer-subbundle-2026-08-10.md`;
- `lab/process/selected-k77-observation-stabilizer-subbundle.json`;
- primary exact probe `78/78 PASS`;
- independent Sage/FLINT `12/12 PASS`.
