---
artifact_type: conditional_build_result
created: 2026-08-08
status: VARPI_BLOCK_EXACT__FIXED_EPSILON_RANK4_METRIC_IMPORT_REJECTED__PHYSICAL_METRIC_EPSILON_K_OPEN
source_return: SOURCE-CONFIRMS__VARPI_DIRECTION_AND_EPSILON_FIELD__SOURCE-SILENT__PHYSICAL_METRIC_EPSILON_FRECHET_BLOCKS_AND_RESIDUAL_PAIRING
ledger: lab/process/conditional-physics-ledger-v0.83.json
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# Selected K77 common-field D-Upsilon varpi block

## Result in plain English

One real block of the stationary two-layer construction is now assembled.

The source varies an independent connection `varpi` and prints the resulting
raw residual

```text
Upsilon = Shiab(F_A) + Hodge(kappa T).
```

Restricting the repo's already exact all-grade response to the actual
24-dimensional horizontal Lorentz-connection carrier gives an injective
`D_varpi Upsilon` block of rank 24. Its finite output support has 56
coordinates:

```text
grade 1: 22
grade 2: 24
grade 5: 10
```

On timelike, spacelike and null covectors, the metric diffeomorphism orbit has
rank four but its independent-`varpi` component has rank three. Because the
raw response is injective, the residual response of those connection columns
also has rank three. The missing gauge-parameter directions are exact:

```text
timelike:  (1,0,0,0)
spacelike: (0,1,0,0)
null:      (1,0,0,1)
```

A metric response can always be made to cancel those three orbit directions,
but that determines only four gauge-orbit values and leaves six transverse
metric columns arbitrary. The resulting extension is a diagnostic Ward fit,
not the physical metric derivative of Shiab/Hodge.

This produces the decisive fork. On the fixed-`epsilon` `(g,varpi)` horn,
`J R=0` forces `rank(J_g D)<=3`. Consequently any stationary metric Gram load
`J_g^! K J_g D` also has rank at most three. The earlier selected metric-only
diagnostic has exact Ward-load rank four, so it cannot simply be imported as
the common-field Gram `g-g` block on that horn.

The source action, however, also owns the group-valued field `epsilon`. That
is a live constructive escape: its Fréchet block could supply the fourth orbit
response. It has not been built. The next wave must therefore construct the
physical metric and source-`epsilon` blocks together, rather than hardening the
old metric diagnostic or fitting a fourth column.

## Layer 0

| written phrase | object used here | object kept distinct |
| --- | --- | --- |
| first-action Hessian | zero-jet `34 x 34` endomorphism on local `(g,varpi)` variables | raw residual Jacobian |
| `D_varpi Upsilon` | Fréchet derivative of the raw residual along the independent connection | the full stationary Gram Hessian |
| `Xi=D_omega Upsilon` | exterior-covariant prolongation/redundant equation printed by the source | the missing Fréchet derivative `D_epsilon Upsilon` |
| metric response | physical derivative of Shiab/Hodge plus the dependent observation normal jet | an orbit-only left-inverse completion |
| old rank-four metric diagnostic | selected second-layer metric restriction | an automatically valid common-field `g-g` block |
| source `epsilon` | group-valued action variable | N1's separately named soldering object, or a supplied external datum |
| Ward cancellation | `J R=0` on the common field tangent | reduced phase space, Green domain or BV-BFV theorem |

The new homonym check is load-bearing: the `D` in the source's
`D_omega Upsilon` is not the field derivative with respect to `epsilon`.

## Exact construction

The all-grade predecessor declared the complete K77 one-form carrier before
reading any target and proved its response has rank 1,470. The present gate
does not invert a new target. It selects the source horizontal subcarrier

```text
delta varpi_mu in span{gamma_ab : mu,a,b=0..3, a<b},
```

with dimension `4*6=24`, and directly applies the same raw-residual response.
Exact sparse arithmetic gives rank 24 and the 56-coordinate support above.

Let `D` be the rank-four metric diffeomorphism symbol and `C=L D` the actual
rank-three connection component from the source-variable lift. For each causal
class,

```text
rank C = rank(D_varpi Upsilon C) = 3.
```

Using any left inverse of `D` constructs a diagnostic `J_g` satisfying

```text
J_g D + D_varpi Upsilon C = 0.
```

The complementary projector has rank six. Changing `J_g` there leaves the
Ward-orbit equality unchanged, which is the planted nonidentifiability
control.

An independent Sage/QQ route proves the rank factorization:

```text
rank(J_g^! K J_g D) <= rank(J_g D) <= 3
```

for an indefinite residual pairing as well. Positivity is not used.

## Source return

The checked 2021 action source supplies:

- `I1B` on inhomogeneous gauge data and `MET(X)`;
- `T=varpi-epsilon^-1 d0 epsilon`;
- the `varpi+s alpha` variation and its residual `Upsilon`; and
- `Xi=D_omega Upsilon` as a redundant equation.

It does not supply the complete active `D_g Upsilon`, `D_epsilon Upsilon`,
K77 residual pairing, formal adjoint, Green concomitant, or equality with the
repo's metric/full-II diagnostic.

```text
SOURCE-CONFIRMS: varpi direction and epsilon as a source field
SOURCE-SILENT:   physical metric/epsilon Frechet blocks and residual pairing
```

## Specialist preassessment and hostile review

- **Differential geometry:** the actual connection lift is `L D`; an orbit
  extension does not define the transverse metric derivative.
- **Symplectic geometry:** bulk `J R=0` is necessary but does not construct a
  reduced presymplectic or BFV class.
- **Variational PDE:** form the Gram operator only after every common-field
  block and its formal adjoint are typed.
- **Krein/operator theory:** the rank obstruction is independent of
  positivity; physical kernel and energy remain open.
- **Complex/path-integral:** no contour, polarization, determinant or measure
  is selected by this finite block.
- **Source criticism:** `D_omega` and `D_epsilon` are different operations.
- **Repo archaeology:** the old rank-four metric load and rank-three actual
  source lift already coexisted; the new source-owned residual block makes
  their consequence exact.
- **Constraint accounting:** no field, coefficient, quotient or datum is
  added; `epsilon` was already in the source action.

Hostile review keeps the conclusion horn-scoped. It rejects the stronger
sentence “the old metric diagnostic is impossible”: it is impossible only as
the fixed-`epsilon` two-field Gram block. A nonzero source-`epsilon` response
is the explicit revival trigger.

## Progress meter

```text
Ledger v0.83 — 82/82 active rows mapped (100%)
32 SAME · 19 DIFFERS · 26 NEEDS · 5 OVER-DETERMINED
Residue — 84 continuous + >=19 function-valued + 9 forks
Scoped quotients ranked — 5

headline_delta: none
frontier_conditions_closed: 3
  - actual horizontal D_varpi Upsilon block assembled
  - its causal diffeomorphism interface and six-column transverse freedom counted
  - fixed-epsilon import of the rank-four metric diagnostic rejected
frontier_conditions_opened: 0
remaining_named_conditions: 2
  - construct physical metric plus source-epsilon D-Upsilon blocks and prove complete J R=0
  - derive K*, formal adjoint and Green concomitant, then form/test the stationary Gram complex
```

No verdict, residue, quotient, external datum, canon or public posture moves.
P1/P2/P3 remain unused. Curt remains formally separate.

## Verification

- exact actual-carrier probe: `68/68 PASS`;
- independent Sage/QQ factorization: `15/15 PASS`;
- planted full-carrier collapse, orbit-to-physical promotion and rank-four
  fixed-epsilon import all reject.

## Next gate

`CONSTRUCT_PHYSICAL_METRIC_PLUS_SOURCE_EPSILON_DUPSILON_BLOCKS__VERIFY_COMPLETE_JR_ZERO__DERIVE_RESIDUAL_K_ADJOINT_AND_GREEN_CONCOMITANT__THEN_FORM_STATIONARY_GRAM_HESSIAN`.
