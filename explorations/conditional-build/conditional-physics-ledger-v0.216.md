---
artifact_type: conditional_physics_ledger_summary
created: 2026-08-12
ledger: lab/process/conditional-physics-ledger-v0.216.json
status: CURRENT_APPEND_ONLY_LEDGER_V0_216
---

# Conditional physics ledger v0.216

```text
Ledger v0.216 — 82/82 target rows mapped (100%)
32 SAME · 19 DIFFERS · 26 NEEDS · 5 OVER-DETERMINED
Residue: 84 continuous + >=19 function-valued + 9 discrete forks
Tightness: T4x1 T3x3 T2x1 · scoped quotients: 5
Headline delta: none
Frontier: 3 conditions closed · 1 sharper action/observation gate opened · 3 remain
```

## What changed

The v0.215 observer-Hermitian rank-four response is not a frame artifact.
The exact normalized Spin boost transports `u`, the fields and `H_u`
together, intertwines the correct adjoint

```text
A sharp_u = H_u^-1 A^dagger H_u,
```

and preserves all 256 live response pairings.  The inverse is load-bearing:
after a noncompact frame change the Hermitian form transforms by congruence,
so blindly reusing `H A^dagger H` manufactures a false failure.

This exact naturality does not make the action independent of `u`.  The
fixed-field boost still changes `8` to `328/9`.  The built observation
projector selects a Lorentzian four-plane but retains the full Lorentz
stabilizer; its fixed-vector space is zero, and the same projector admits
different unit timelike directions.  Therefore neither the coarse observation
data nor forgetting `u` owns the repair.

## Scoped migrations

- `RA-E1`: diagonal Spin/frame naturality is exact.  Construct the complete
  `epsilon_IG`/`SO(3)` flag or a constrained-`u` Euler/Ward equation; coupled
  contact and the physical vacuum remain open.
- `RA-E3`: the allowed one-form carrier passes the associated-family gate,
  while coarse observer ownership and vertical basicness fail.  Scalar descent
  and Yukawa placement remain open.
- `LT-SM6`: the restricted potential and associated rank-four pairing coexist;
  `u` action ownership, contact, preboundary, domain and spectrum remain open.

No verdict, residue, fork, quotient, parameter, selector, field or external
datum changes.  The conditional observer cost remains three function-valued
degrees before equations and is unbooked.  P1/P2/P3 remain unchanged and
unused.

## Layer-0 fence

Diagonal frame naturality, vertical basicness, coarse observation-plane
selection, full `epsilon_IG` flag selection and dynamical `u` selection are
five different statements.  The current wave settles only the first and
refutes the second and coarse third.

Keep source `C^(32,32)+C^(32,32)` carrier halves distinct from a derived
`U(32,32)xU(32,32)` subgroup, the full `U(64,64)` parent and independent
connection fields.  The associated Hermitian form is also not a positive
Hilbert majorant or a complete action/Green form.

## Next gate

Construct the smallest richer observation flag that could reduce the Lorentz
stabilizer to `SO(3)`, and derive the constrained `u` Euler/Ward equation of
the selected action.  If neither determines or removes `u`, price the
three-function observer field by constraint surplus.  Retain the coupled
metric/section/gauge contact parent as the independent comparator.
