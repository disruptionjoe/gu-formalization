---
artifact_type: conditional_build_result
created: 2026-08-08
status: VARPI_EQUATION_DUAL_GREEN_EXACT__COMMON_FIELD_ASSEMBLY_FAILS_CLOSED__OPERATOR_ADJOINT_NEEDS_FIELD_RIESZ
source_return: SOURCE-CONFIRMS_NORM_SQUARE_ADJOINT_ARENA_AND_SOURCE_FIELDS__SOURCE-SILENT_KLOC_FIELD_RIESZ_FULL_DEPSILON_AND_ANALYTIC_DOMAIN
ledger: lab/process/conditional-physics-ledger-v0.96.json
canon_verdict_change: none
---

# Selected K77 common-field formal-adjoint and Green gate

## Result in plain English

The calculation found one real construction and one important ownership
error.

On the actual 24-component horizontal `varpi` carrier, the selected raw
residual has four live first-derivative coefficient matrices, each of exact
rank `13`, and a live zero-order matrix of rank `24`. Pairing this operator
with the conditional local K77 residual bilinear from v0.92 gives the exact
covector-valued formal adjoint

```text
J = A^mu partial_mu + B,
J_K^! = -partial_mu((A^mu)^T K .) + B^T K,
G^mu(u,v) = u^T (A^mu)^T K v.
```

The Green identity holds coefficientwise in all four directions, and the
current is nonzero in all four. An independent Sage calculation reproduces
the derivative sign, boundary term and Riesz nonuniqueness.

The full three-field common operator does **not** yet exist. The prior queue
called `D_g`, `D_varpi` and `D_epsilon` “owned,” but those words hid three
different grades of ownership:

- `D_varpi Upsilon` is an actual coefficient bank on the residual carrier;
- `D_g Upsilon` is geometrically and rank-complete locally, but has not been
  emitted on that same residual-coordinate coefficient bank; and
- the repo owns a primitive epsilon **Euler covector** and a four-column
  gamma-epsilon **Ward orbit**, not the full lower-order/nonlinear
  `D_epsilon Upsilon` field derivative.

Therefore the preregistered common-field assembly fails closed. This is not a
failure of the source action; it is a correction to the build inventory.

## Layer 0

| phrase | exact object | not the same as |
| --- | --- | --- |
| `D_varpi Upsilon` | actual 24-column horizontal source Frechet bank | full 1,470-column all-grade tangent |
| completed `D_g` | local source-coordinate geometry and ranks | serialized common residual-coordinate coefficients |
| primitive epsilon Euler | `D_B^!(E_B-E_T)+(D_epsilon S)^!K_S` | `D_epsilon Upsilon` |
| gamma-epsilon response | four principal Ward-orbit columns at `Upsilon*=0` | full primitive epsilon field bank |
| equation dual | canonical field covector `J_K^!v` | field-valued adjoint operator |
| Green concomitant | integration-by-parts current | presymplectic/BFV current |

The last distinction is mathematically load-bearing. A residual pairing maps
the residual to its dual, so composing it with `J^T` naturally produces a
field **covector**. Turning that covector into a field vector requires a
nondegenerate pairing on field space. Two exact finite Riesz choices give two
different vectors for the same covector. The coordinate identity is not a
source-owned choice.

## Exact coefficient result

The actual source-horizontal bank has:

```text
domain dimension:       24
principal ranks:        13, 13, 13, 13
principal supports:     32, 32, 32, 32
zero-order rank:         24
Green identities:       4/4 exact and nonvacuous
```

The wrong-sign algebraic transpose fails the planted integration-by-parts
control. The symmetric residual Gram is also kept distinct from an
antisymmetric presymplectic form.

## Specialist and hostile disposition

- **Differential geometry:** a rank-complete geometric partial is not yet a
  composable coefficient bank.
- **Variational PDE:** the derivative minus sign and boundary concomitant are
  exact; the result is local and formal.
- **Symplectic geometry:** Green comes first; antisymmetrization, basicness and
  BFV reduction remain open.
- **Krein/operator theory:** `K_loc` is nondegenerate but indefinite; it gives
  an equation dual, not positivity or a field-space Riesz map.
- **Complex/path-integral:** no contour, determinant, measure, saddle or
  reflection positivity follows.
- **Source criticism:** the source confirms the norm-square/adjoint arena and
  fields; it is silent on this `K_loc`, the missing field banks, field Riesz
  map and analytic domain.

The hostile review accepts the source-`varpi` theorem and rejects the claimed
full common-field ownership.

## Progress meter

```text
Ledger v0.96 — 82/82 active rows mapped (100%)
32 SAME · 19 DIFFERS · 26 NEEDS · 5 OVER-DETERMINED
Residue — 84 continuous; conditional action-parent range 84..86
           + >=19 function-valued + 9 forks
Scoped quotients ranked — 5

headline_delta: none
frontier_conditions_closed: 4
  - actual four-direction varpi principal coefficient bank emitted
  - actual varpi zero-order coefficient bank emitted
  - K_loc equation-dual and nonzero Green identity proved
  - field-Riesz nonuniqueness typed exactly
frontier_conditions_opened: 2
  - common-coordinate D_g bank must be emitted
  - full primitive D_epsilon bank must be constructed
remaining_named_conditions: 3
  - emit D_g on the common residual-coordinate carrier
  - construct full D_epsilon and prove common J R=0
  - derive a field-space Riesz map or retain covector-valued adjoint language
```

No verdict, residue, quotient, datum, canon or public posture moves.
P1/P2/P3 remain unused. The selected Spin-native parent, the product of two
`U(32,32)` Weyl halves, and the full `U(64,64)` comparator remain three
distinct action-parent questions.

## Next gate

Emit the complete local `D_g Upsilon` coefficients on the same residual basis,
construct the lower-order/nonlinear primitive `D_epsilon Upsilon` bank, and
verify the full common-field `J R=0`. Then either derive a geometrically owned
field-space Riesz map or keep the adjoint honestly covector-valued before any
stationary Gram, Einstein, symplectic, BFV, domain or quantum promotion.

## Evidence

- `tests/channel-swings/selected_k77_common_field_formal_adjoint_green_probe.py`
- `tests/channel-swings/selected_k77_common_field_formal_adjoint_green_independent.sage`
- `lab/process/selected-k77-common-field-formal-adjoint-green.json`
- `lab/process/hostile-reviews/2026-08-08-selected-k77-common-field-formal-adjoint-green-review.md`
