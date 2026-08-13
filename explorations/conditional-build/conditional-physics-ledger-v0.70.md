# Conditional physics ledger v0.70

## Meter

```text
Ledger v0.70 — 82/82 active target rows mapped (100%)
32 SAME · 19 DIFFERS · 26 NEEDS · 5 OVER-DETERMINED
Residue — 84 continuous + >=19 function-valued + 9 forks
Quotients ranked — 5 scoped
```

## Migration from v0.69

An ordinary scalar boundary counterterm cannot cancel the v0.69 moment map:
`theta -> theta + delta B` leaves `Omega=delta theta` unchanged because
`delta^2 B=0`. The two unextended horns remain conditional choices. Small or
Dirichlet gauge sets the endpoint parameter to zero; requiring zero charge for
arbitrary endpoint gauge instead forces both endpoint momenta to zero. The
checked source and current action select neither horn.

A minimal edge extension is now exact. One new boundary coordinate per
endpoint, transforming with the endpoint gauge parameter, fixes the two edge
coefficients uniquely to `(-1,+1)`. For one normal direction the extended
six-dimensional two-form has rank four and its two-dimensional kernel equals
the gauge span. Its four-dimensional quotient is nondegenerate.

Tensoring with all ten nonzero K77 normal weights gives an extended dimension
of 60, rank 40, characteristic gauge kernel 20, and quotient dimension/rank
40. This adds one scoped conditional quotient. It is not a global labelled
`Y14` edge bundle, physical BFV phase space, polarization, charge algebra, or
common analytic domain.

Five rows migrate in distance, evidence and mapping grade: `LT-GR1`,
`LT-GR2b`, `LT-GR3`, `LT-GR5`, and `LT-GR6`. The quotient count moves from
four to five. Verdicts, global continuous/function-valued residue, forks,
P1/P2/P3, canon and public posture are unchanged. The boundary-coordinate
cost is 20; coefficient freedom is zero.

## Frontier

```text
headline_delta: SCOPED_QUOTIENT_PLUS_ONE
frontier_conditions_closed: 3
frontier_conditions_opened: 1
remaining_named_conditions: 2
```

Next lift the two edge cells to a full labelled `Y14` boundary bundle and
prove tilted-inhomogeneous-gauge equivariance, overlap cocycle closure and the
global moment-map identity—or source/action-select a physical boundary domain.
Only then open full BFV charge algebra, polarization and common-domain work.

Machine truth: `lab/process/conditional-physics-ledger-v0.70.json`.
