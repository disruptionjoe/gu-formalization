# Conditional physics ledger v0.171

```text
Ledger v0.171 — 82/82 target rows mapped (100%)
32 SAME · 19 DIFFERS · 26 NEEDS · 5 OVER-DETERMINED
Residue: 84 continuous + >=19 function-valued + 9 discrete forks
Tightness: T4x1 T3x3 T2x1 · scoped quotients: 5
Frontier: 1 condition closed · 2 opened · 6 named conditions remain
```

## What changed

The v0.170 `ker N` restriction was tested against the actual normal Green
coefficient for the source action's independent barred and unbarred fermions.
Its unique Green adjoint is

```text
Nsharp = A^(-T) N^T A^T.
```

The natural two-kernel domain `ker Nsharp x ker N` has exact rank-`128`
radicals on both sides. The perfect algebraic dual is
`Vbar/im Nsharp`, dimension `1792`, but it is not source/action-owned as gauge
or BV and the naive observation map has rank `128` on the quotient directions.
It therefore does not descend. The observed-x dual kernel itself retains rank
`512`, while the two mixed-center samples retain `640`.

Six rows migrate in distance and evidence only: `RA-D4`, `RA-F1`, `RA-F2`,
`RA-G2`, `LT-SM3`, and `AC-F1`. Verdicts, residue, forks, quotients, P1/P2/P3,
canon verdicts and public posture do not move.

## Interpretation

The restriction route is neither wholly dead nor promoted. It survives as
one-sided flat principal evolution data, but direct promotion to a complete
action domain fails. The only algebraically perfect dual presently requires
an unowned quotient that identifies observably live directions.

## Ranked successor

1. Compare `im Nsharp` with the existing action-owned small-gauge
   characteristic image and boundary moment map.
2. Assemble the full moving boson-fermion preboundary form and test whether an
   owned coisotropic/BFV reduction plus a basic modified observation exists.
3. If no owned image matches, shift priority to the separate source-admitted
   wedge-Shiab/nonzero-southeast semisimple operator completion rather than
   fitting a quotient.

Machine-readable truth remains
`lab/process/conditional-physics-ledger-v0.171.json`.
