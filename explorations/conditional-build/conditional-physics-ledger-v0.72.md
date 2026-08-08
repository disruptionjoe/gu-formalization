# Conditional physics ledger v0.72

## Meter

```text
Ledger v0.72 — 82/82 active target rows mapped (100%)
32 SAME · 19 DIFFERS · 26 NEEDS · 5 OVER-DETERMINED
Residue — 84 continuous + >=19 function-valued + 9 forks
Quotients ranked — 5 scoped
```

## Migration from v0.71

The missing universal group-edge construction is now explicit. Let a boundary
configuration `x` and edge frame `u` transform by simultaneous right
multiplication, and let the cotangent variable transform contragrediently:
`x -> xh`, `u -> uh`, `p -> p h^-T`. Then
`q=xu^-1` and `pi=p u^T` are exactly invariant.

On a generic exact `GL(2,Q)` fixture, the pullback of the canonical two-form on
`(q,pi)` has rank eight on the twelve-dimensional extended space. Its
four-dimensional characteristic kernel equals exactly the simultaneous right
`gl(2)` orbit, so the eight-dimensional quotient is symplectic. At the identity
`delta q=delta x-delta u`, and the canonical potential becomes
`Tr(p^T(delta x-delta u))`, recovering the v0.70 minus sign rather than merely
matching coordinate counts.

The typed differential bridge is also exact but deliberately narrow. The base
Maurer-Cartan form `u^-1 d u` transforms as
`h^-1(u^-1 d u)h+h^-1 d h`, including noncommuting triple overlaps. Its
curvature vanishes identically, so it realizes only the `A0=0` flat/pure-gauge
tilted component. It is not an arbitrary olive/varpi connection, and base `d`
is not field-space `delta`.

The v0.70 local rank-40 quotient remains valid and conditional; this wave
refines it rather than booking a sixth quotient. The theorem is universal and
finite. It does not yet instantiate the actual K77 `H`-representation,
action-owned preboundary potential and invariant trace, nonzero `A0`, global
moment map, BFV polarization/charges or a common analytic domain.

Five rows migrate in distance, evidence and mapping grade: `LT-GR1`,
`LT-GR2b`, `LT-GR3`, `LT-GR5`, and `LT-GR6`. Verdicts, coverage, residue,
forks, the five scoped quotients, P1/P2/P3, canon and public posture are
unchanged.

## Frontier

```text
headline_delta: NONE
frontier_conditions_closed: 3
frontier_conditions_opened: 1
remaining_named_conditions: 2
```

Next instantiate this dressing on the actual K77 `H`-representation and
action-owned preboundary potential with its invariant trace. Extend the bridge
from the `A0=0` flat component to the full `tau_A0` law and prove the global
`H`-bundle moment map/kernel descent. Only then open full BFV charge algebra,
polarization and common-domain work.

Machine truth: `lab/process/conditional-physics-ledger-v0.72.json`.
