---
artifact_type: conditional_physics_ledger_summary
created: 2026-08-12
ledger: lab/process/conditional-physics-ledger-v0.223.json
status: CURRENT_APPEND_ONLY_LEDGER_V0_223
---

# Conditional physics ledger v0.223

```text
Ledger v0.223 — 82/82 target rows mapped (100%)
32 SAME · 19 DIFFERS · 26 NEEDS · 5 OVER-DETERMINED
Residue: 84 continuous + >=19 function-valued + 9 discrete forks
Tightness: T4x1 T3x3 T2x1 · scoped quotients: 5
Headline delta: none
Frontier: 3 conditions closed · 1 sharpened gate opened · 1 remains
```

## What changed

The conditional observer pairing `Q_u` now composes with both the principal
kinetic response and the actual source-owned residual family.  On
`span{S_q,H_q}` it gives exact Gram `diag(160,2)`, replacing the trace-`H_q`
comparator's `diag(192,0)`.  The displaced-torsion residual is therefore
non-null under the same pairing that repairs principal rank.

The exact restricted potential becomes

```text
c(u) [80(rho+r^2/3)^2+kappa^2 r^2],
c(u)=sum_mu u_mu^2.
```

Its nonzero branch is

```text
r^2=-3rho-9kappa^2/160,
rho < -3kappa^2/160.
```

On the future unit hyperboloid, `c(u)=1+2|v|^2`; the positive branch locally
selects the rest representative and time orientation selects its future sign.

## Append-only migration

`RA-E1`, `RA-E3`, and `LT-SM6` move in distance/evidence only.  Verdicts,
reason kinds, residue, forks, five quotients, P1/P2/P3, canon and public
posture do not move.

## Layer-0 fence

Keep distinct:

- trace-`H_q` comparator and conditional observer-`H_u` pairing;
- source `Q_B` and repository candidate `Q_u`;
- local constrained observer representative and global observer section;
- line selection and the supplied time orientation selecting its sign;
- restricted radial/observer stationarity and complete coupled Euler closure;
- old Hodge-adapted `e3` coefficient and its required moving-`Q_u` recompute;
- two `C^(32,32)` carrier halves, their block subgroup, full `U(64,64)` and
  independent connection fields.

## Next gate

Insert moving `Q_u` into the Hodge-adapted normal-contact calculation on the
shifted branch.  Then derive the complete metric, section, Shiab, gauge and
connection Euler equations and test source ownership, global descent,
preboundary/domain and the contact discriminant.
