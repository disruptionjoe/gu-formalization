# Conditional physics ledger v0.75

## Meter

```text
Ledger v0.75 — 82/82 active target rows mapped (100%)
32 SAME · 19 DIFFERS · 26 NEEDS · 5 OVER-DETERMINED
Residue — 84 continuous + >=19 function-valued + 9 forks
Quotients ranked — 5 scoped
```

## Migration from v0.74

The proposed coefficient weld has been tested and rejected at Layer 0.
The selected source-shaped action is not quadratic in the K77 contact variable:
on the exact noncyclic fixture,

```text
I(C,zT) = -(4/3) z^3 + (300/7) z^2 - 5 z.
```

Its action-derived `E_B-E_T` is already nonzero at `T=0`, so no fixed linear
map `KT` can equal that coefficient throughout the selected configuration
family.  A second inequivalent indefinite matrix `K2=diag(-2,5,7)` also passes
the same exact contact Hessian, Ward-kernel, Green and endpoint symplectic
tests as the v0.69 fixture `K=diag(-1,2,3)`, while giving a different `KT`.
Those controls prove a universal contact theorem, not a unique GU Legendre
map.

The following results survive unchanged:

- endpoint cotangent variables are legitimate independent coordinates;
- the direct-sum endpoint construction still recovers the local `40/40`
  quotient;
- a single holonomy still compresses it to `20/40` and therefore fails;
- the generic two-connection contact/Ward theorem remains exact.

What is retracted is only the claim that `p=KT` is selected-action-owned.  A
one-background symmetric `9x9` fit would have 45 parameters but only rank-nine
constraints, leaving 36 free directions; it can fit any target and supplies
no information.  The actual coefficient must instead be assembled directly
as the oriented boundary trace or normal restriction of `E_B-E_T` across all
ten selected K77 directions, with the observation receiver included.

Five rows migrate in distance, evidence and mapping grade: `LT-GR1`,
`LT-GR2b`, `LT-GR3`, `LT-GR5`, and `LT-GR6`.  Verdicts, coverage, residue,
forks, five scoped quotients, P1/P2/P3, canon and public posture are unchanged.

## Frontier

```text
headline_delta: NONE
frontier_conditions_closed: 2
frontier_conditions_opened: 1
remaining_named_conditions: 2
```

Next assemble the actual all-ten selected-action `i_n(E_B-E_T)` boundary bank
with the observation receiver.  Only then reuse the already-independent
endpoint cotangent dressing and attempt full `tau_A0`, global BFV and the
common domain.

Machine truth: `lab/process/conditional-physics-ledger-v0.75.json`.
