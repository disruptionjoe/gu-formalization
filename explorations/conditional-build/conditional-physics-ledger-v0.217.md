---
artifact_type: conditional_physics_ledger_summary
created: 2026-08-12
ledger: lab/process/conditional-physics-ledger-v0.217.json
status: CURRENT_APPEND_ONLY_LEDGER_V0_217
---

# Conditional physics ledger v0.217

```text
Ledger v0.217 — 82/82 target rows mapped (100%)
32 SAME · 19 DIFFERS · 26 NEEDS · 5 OVER-DETERMINED
Residue: 84 continuous + >=19 function-valued + 9 discrete forks
Tightness: T4x1 T3x3 T2x1 · scoped quotients: 5
Headline delta: none
Frontier: 2 control/prior-art conditions closed · 0 opened · 2 remain
```

## What changed

V0.216's ownership conclusion survives, but one control coefficient did not.
Its naturality theorem correctly transports `u`, the fields and `H_u`
together and uses the inverse-Hermitian adjoint

```text
A sharp_u = H_u^-1 A^dagger H_u,
```

and preserves all 256 live response pairings.  Its fixed-field basicness
control, however, inherited the old involutive shortcut from v0.215 after a
noncompact congruence where `H_u^2 != 1`.

With the correct inverse adjoint, the exact fixed-field blocks are
`-328/9 I4, +8 I4, +8 I4, +8 I4`, with all mixed blocks zero.  They still
differ from the adapted response, so forgetting `u` is still not basic.  The
coarse observation projector still selects only a Lorentzian four-plane and
no unit timelike vector.  No v0.216 ownership conclusion changes.

The prior-art return changes the successor.  RB4 already constructs the
moving-`u` family and its `SO(3)` stabilizer; RB5 already refutes descent of a
complete flag from the coarse epsilon plane.  RB6/RB7 tested older W177/action
grammars, not the current `SC-ACT-04` selected action.  Rebuilding another
minimal `SO(3)` flag would therefore duplicate work.

## Append-only correction

- `RA-E1`, `RA-E3`, and `LT-SM6` retain exactly their v0.216 row meanings.
- The basicness-control block location/sign is corrected.
- The duplicate richer-flag successor is retired in favor of the current
  `SC-ACT-04` constrained-`u` Euler/Ward equation with the section chain rule.

No verdict, residue, fork, quotient, parameter, selector, field or external
datum changes.  The conditional observer cost remains three function-valued
degrees before equations and is unbooked.  P1/P2/P3 remain unchanged and
unused.

## Layer-0 fence

Diagonal frame naturality, vertical basicness, coarse observation-plane
selection, existence of the RB4 moving-`u`/`SO(3)` family, ownership of a
refined epsilon flag, and dynamical `u` selection are different statements.
The correction preserves naturality and nonbasicness but fixes the response
coefficients.  RB4 existence does not supply ownership; RB5 says the coarse
plane does not supply a complete flag.

Keep source `C^(32,32)+C^(32,32)` carrier halves distinct from a derived
`U(32,32)xU(32,32)` subgroup, the full `U(64,64)` parent and independent
connection fields.  The associated Hermitian form is also not a positive
Hilbert majorant or a complete action/Green form.

## Next gate

Vary the current `SC-ACT-04` selected action with respect to constrained `u`,
including the section chain rule, and derive its Euler/Ward equation.  If it
does not determine or remove `u`, price the three-function observer field by
constraint surplus.  Retain the coupled metric/section/gauge contact parent as
the independent comparator; do not substitute another RB4-style existence
construction for action ownership.
