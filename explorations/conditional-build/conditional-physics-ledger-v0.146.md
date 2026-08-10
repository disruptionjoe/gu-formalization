---
artifact_type: conditional_physics_ledger_migration
created: 2026-08-10
status: CURRENT_APPEND_ONLY_LEDGER_V0_146
predecessor: lab/process/conditional-physics-ledger-v0.145.json
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# Conditional physics ledger v0.146

## Progress meter

```text
Ledger v0.146 — 82/82 mapped (100%)
32 SAME · 19 DIFFERS · 26 NEEDS · 5 OVER-DETERMINED
Residue — 84 continuous; conditional parent range 84..86
Function-valued slots — >=19
Open discrete forks — 9
Scoped quotients — 5
Frontier — 1 condition closed · 1 opened · 3 named conditions remain
```

## Migration

v0.145 remains immutable. Five rows move in distance/evidence only after its
sole named quadratic revival is tested on the exact nonzero source family.

The source curvature commutes with four-plane chirality and therefore
preserves the chiral split, but it has exact rank-three nonzero components in
both `su(2)+` and `su(2)-`. Thus `D_B P_sd=0` is insufficient to select one
factor, and membership in the self-dual factor forces `t=0`. The current-action
self-dual P3 revival is killed.

A replacement remains possible only as a new construction: explicitly embed
P3's auxiliary `SU(2)` bundle into the tangential source parent, restrict the
first action before variation, and recompute its complete Euler/BV/domain
bank. Projecting the already-solved full-parent family is not that action.

## Rows moved

- `LT-GR1`: the current-action self-dual revival dies; a new restricted action,
  common domain and observed Hilbert stress remain open.
- `LT-GR2b`: the local dynamic carrier survives only as the unreduced carrier;
  its nonzero curvature is not one-factor valued.
- `LT-GR2c`: replace `D_B P_sd=0` with an explicit P3-to-source principal-
  bundle diagonal and restricted-action Euler recomputation.
- `LT-GR2d`: neither current-action quadratic horn selects magnitude; sign,
  units, radiative response and cosmology remain open.
- `LT-GR6`: any reduced sector must come from a newly varied action before
  observation or physical-domain claims.

No verdict, residue, quotient, coefficient, datum, P1/P2/P3, canon verdict or
public posture changes.

## Next gate

Construct or kill the explicit P3-to-source `SU(2)+` principal-bundle
diagonal. If it exists without a free continuous normalization, restrict `I1`
to its connection space before variation and recompute every Euler row,
presymplectic/BV constraint and common-domain condition. Do not reuse the old
two-factor nonzero family inside the reduced action.

Evidence:

- `selected-k77-p3-selfdual-source-reduction-2026-08-10.md`;
- `lab/process/selected-k77-p3-selfdual-source-reduction.json`;
- `lab/process/hostile-reviews/2026-08-10-selected-k77-p3-selfdual-source-reduction-review.md`.
