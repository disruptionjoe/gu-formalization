---
artifact_type: conditional_physics_ledger_migration
created: 2026-08-10
status: CURRENT_APPEND_ONLY_LEDGER_V0_143
predecessor: lab/process/conditional-physics-ledger-v0.142.json
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# Conditional physics ledger v0.143

## Progress meter

```text
Ledger v0.143 — 82/82 mapped (100%)
32 SAME · 19 DIFFERS · 26 NEEDS · 5 OVER-DETERMINED
Residue — 84 continuous; conditional parent range 84..86
Function-valued slots — >=19
Open discrete forks — 9
Scoped quotients — 5
Frontier — 1 condition closed · 1 opened · 3 named conditions remain
```

## Migration

v0.142 remains immutable. Five rows move in distance/evidence only after the
v0.15 normalized global zero-mode projector is composed with the v0.142
one-amplitude family.

The projector `Q=1-Pi0` conditionally screens independent constant source
shifts. It adds no equation for the nonzero VEV amplitude. `ell` reads the
amplitude; `T in im Q` forces the constant VEV to zero; `ell(T)=c` selects the
supplied `c`. Fredholm compatibility of `Q rho` is automatic and independent
of the amplitude.

## Rows moved

- `LT-GR1`: conditional source-shift screening is exact; amplitude, common
  domain and observed Hilbert stress remain open.
- `LT-GR2b`: retain the local dynamic VEV; do not project the VEV field itself
  into `im Q` if a nonzero constant mode is required.
- `LT-GR2c`: the existing projector adds zero amplitude equations.
- `LT-GR2d`: screening and magnitude selection are now explicitly separate.
- `LT-GR6`: projected source response does not supply observed Hilbert stress.

No verdict, residue, quotient, coefficient, datum, P1/P2/P3, canon verdict or
public posture changes.

## Next gate

Build the common Green/Krein and coupled BV--BFV domain, then derive an
action-owned amplitude-dependent global solvability, determinant,
boundary-charge or stability condition. Retain an explicitly typed external
value as a separate conditional horn and count its constraint surplus.

Evidence:

- `selected-k77-global-projector-amplitude-layer0-2026-08-10.md`;
- `lab/process/selected-k77-global-projector-amplitude-layer0.json`;
- `lab/process/hostile-reviews/2026-08-10-selected-k77-global-projector-amplitude-layer0-review.md`.
