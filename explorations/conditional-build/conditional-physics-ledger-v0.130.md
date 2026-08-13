---
artifact_type: conditional_physics_ledger_migration
created: 2026-08-10
status: CURRENT_APPEND_ONLY_LEDGER_V0_130
predecessor: lab/process/conditional-physics-ledger-v0.129.json
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# Conditional physics ledger v0.130

## Progress meter

```text
Ledger v0.130 — 82/82 mapped (100%)
32 SAME · 19 DIFFERS · 26 NEEDS · 5 OVER-DETERMINED
Residue — 84 continuous; conditional parent range 84..86
Function-valued slots — >=19
Open discrete forks — 9
Scoped quotients — 5
```

## Migration

v0.129 remains immutable. Six Lagrangian rows move in distance only after the
fixed-frame parent result is composed with the source-owned epsilon-moved
Clifford frame.

The transported rank-`8,128` Spin projector and recomputed Euler operator obey
exact noncommuting cocycle descent on all `16,384` directions. Both moving Spin
total `113,893` and full-U total `229,477` globalize. The two `C^(32,32)` halves
form a moving `8,192+8,192` block/coset reduction inside source full
`U(64,64)` `P_H`; they are not a second principal parent by notation. Ordinary
observation value pullback gives totals `32,613` and `65,637` but selects neither
internal carrier.

The remaining decisive condition is action ownership of `P_epsilon u=u` and/or
`D_varpi chi_epsilon=0`, including the moving-projector first variation and the
complement Euler equation. No verdict, residue, quotient, coefficient, datum,
P1/P2/P3, canon or posture changes.

## Rows moved

- `LT-GR1`: both carrier bundles globalize; action-owned reduction, observation
  domain and spectrum remain open.
- `LT-GR2b`: full `P_H` plus the moving two-half reduction is typed; the Spin
  tangent constraint and physical horn remain open.
- `LT-GR2c`: neither moving parent bundle supplies a normalization or scale.
- `LT-GR3`: moving Euler covariance is exact; fixed-frame full force is
  re-scoped, while action-parent ownership remains open.
- `LT-GR5`: the moving augmented-torsion carrier globalizes; reduction, BV and
  domain work remain.
- `LT-GR6`: the full connection is typed as block connection plus
  bifundamental/coset one-form; trace, domain and Hilbert-stress work remain.

Evidence:

- `explorations/conditional-build/selected-k77-moving-parent-bundle-observation-reduction-2026-08-10.md`;
- `lab/process/selected-k77-moving-parent-bundle-observation-reduction.json`;
- primary exact probe `39/39 PASS`;
- independent Sage exact route `15/15 PASS`.
