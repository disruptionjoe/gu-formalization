---
artifact_type: exact_first_action_euler_obstruction
created: 2026-08-14
status: SELECTED_K77_CANONICAL_ZORRO_ZERO_T_FIRST_ACTION_TWO_JET_OBSTRUCTED__SYMMETRIC_DT_REPAIR_EXCLUDED_BEFORE_BIANCHI
lane_id: SRC-RES-COH-01
source_claims: [SC-ACT-01, SC-ACT-04, SC-ACT-05]
probe: tests/channel-swings/selected_k77_zorro_first_action_euler_gate_probe.py
registry: lab/process/selected-k77-zorro-first-action-euler-gate.json
hostile_review: lab/process/hostile-reviews/2026-08-14-selected-k77-zorro-first-action-euler-gate-review.md
canon_verdict_change: none
ledger_row_changes: none
---

# Selected-K77 canonical-Zorro first-action Euler gate

## Result first

The canonical `T=F_varpi=0` residual-first branch does **not** extend to a
stationary first-action two-jet for the repository-selected K77 Shiab.  The
previous Run correctly admitted the printed residual and its first
prolongation.  It had not yet imposed the translation Euler covector actually
obtained by varying the transgression action.

For

```text
bar F = F_B + (1/2)D_B T + (1/3)T^2,
I1B    = <T,S(bar F)> + (kappa/2)<T,*T>,
```

the selected noncyclic Shiab gives

```text
E_T = S(bar F) + L_T^! S^!T + *kappa T,
L_T X = (1/2)D_B X + (1/3)(XT+TX).
```

At the predecessor point value `T=0`, the second term does not disappear as
a jet: integration by parts makes it depend on `DT`.  On the pure
antisymmetric representative `DT_(r;k)^ij=-(1/2)(F_BZ)_(rk)^ij`, the direct
`S(F_BZ/2)` contribution has 14 live grade-one Euler cells.  The exact
formal-adjoint companion occupies nine of them with coefficient ratio `1/7`.
Their sum still has all 14 cells nonzero.

The contrary construction was tested on the complete allowed grade-two
symmetric correction

```text
Q_(r;k)^ij = Q_(k;r)^ij,
DT = -(1/2)F_BZ + Q.
```

There are `105*91=9,555` rational variables.  The exact action map has 196
typed output rows.  Its forced target is outside the image: a 14-supported
left-cokernel covector annihilates every one of the 9,555 columns and evaluates
to one on the target.  The certificate uses only action rows and no Bianchi
row.  Therefore differential Bianchi and Spencer holonomicity cannot rescue
the family; adding their 5,096 equations only preserves the inconsistency.

This is the first action-stationarity obstruction for the explicit canonical
residual-first branch.  It is not a no-go for GU, for every Zorro completion,
or for nonzero-`T` stationary branches.

## What this corrects

The source separately prints a translation endpoint

```text
Upsilon_print = S(F_varpi) + *kappa T.
```

On the selected noncyclic full-domain Shiab, repository archaeology had
already proved that this printed endpoint is not the derivative of the same
transgression action.  The prior point/two-jet construction solved
`Upsilon_print=0` and `D Upsilon_print=0`; it did not solve `E_T=0`.

The new result does not retract the signed-permutation Shiab theorem, the
Bianchi-compatible inverse, or the symmetric second-`varpi`-jet right inverse.
Those remain exact statements about the printed residual complex.  What is
retracted is only their use as a candidate stationary first-action branch.

## Exact certificate

The probe reuses the native moving-Shiab and canonical Zorro curvature
backends, then constructs the formal adjoint of

```text
S : Omega^2(Cl1) -> Omega^13(Cl2)
```

entrywise under the existing exterior/Krein pairing.  It has 1,274
signed-permutation entries.  The direct action term uses the complementary
selected component on the canonical `Cl2` curvature.  All arithmetic is exact
over `QQ`.

The affine system has:

| quantity | exact value |
| --- | ---: |
| symmetric `DT` variables | 9,555 |
| action output rows | 196 |
| differential-Bianchi rows | 5,096 |
| sparse matrix nonzeros | 17,836 |
| pure-representative direct support | 14 |
| pure-representative adjoint support | 9 |
| total Euler support | 14 |
| left-cokernel certificate support | 14 action + 0 Bianchi |

The certificate equations are checked directly:

```text
A^T lambda = 0,
lambda(target) = 1.
```

They prove inconsistency without a numerical rank threshold or fitted
coefficient.

## Downstream chain

The primitive-epsilon and dependent metric/observation rows are not the first
obstruction on this family.  A nonzero independent translation Euler covector
already violates first-action stationarity.  Fixed Dirichlet data remove the
known preboundary flux but cannot cancel that bulk row.

Those downstream adjoints remain meaningful only after a genuinely different
candidate reaches `E_T=0`.  The two honest reopeners are:

1. a nonzero-`T` source/action branch whose full Euler equation is solved; or
2. an explicitly derived different connection-grade/Zorro reconstruction
   whose additional typed jet variables can hit the 14-dimensional cokernel.

Merely dropping Bianchi, changing the symmetric representative, or returning
to the printed endpoint cannot reopen this branch.

## Hostile ceiling

The obstruction is local, formal, selected-product and reconstruction scoped.
It freezes the canonical pure-vertical Zorro/DeWitt curvature, the selected
`comm/symi/symi` Shiab, the `T=F_varpi=0` point value, and grade-two symmetric
`DT` corrections.  A larger Clifford-grade connection tangent is not silently
excluded.  No open-background no-go, source-preferred Shiab theorem, total
deformation complex, physical cohomology, superposition law, positivity or
empirical prediction follows.

`SR-1` remains `BACKGROUND-MISSING`; `SR-2` remains blocked.  No ledger,
canon, residue, quotient, datum, scheduled-priority or public-posture change
is licensed.

Reproduce with:

```bash
sage -python tests/channel-swings/selected_k77_zorro_first_action_euler_gate_probe.py
```

The exact probe passes `35/35`.
