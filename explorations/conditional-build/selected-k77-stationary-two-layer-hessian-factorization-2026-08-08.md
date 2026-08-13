---
artifact_type: conditional_build_result
created: 2026-08-08
status: STATIONARY_FIRST_DERIVATIVE_REDUCTION_EXACT__COMMON_FIELD_DUPSILON_AND_K_OWNER_OPEN
source_return: SOURCE-CONFIRMS__RESIDUAL_NORM_SQUARE_AND_FIRST_SOLUTION_REDUNDANCY__SOURCE-SILENT__COMMON_FIELD_DUPSILON_BLOCKS_PAIRING_AND_PHYSICAL_COMPLEX
ledger: lab/process/conditional-physics-ledger-v0.82.json
canon_verdict_change: none
---

# Selected K77 stationary two-layer Hessian factorization

## Result in plain English

The full two-layer Hessian is not yet constructed, but its next construction
is substantially smaller than v0.81's wording suggested.

For the second action

```text
I2 = 1/2 <Upsilon, K Upsilon>,
```

at a background satisfying the **complete** first-layer equation
`Upsilon*=0`, the bulk quadratic operator is exactly

```text
H2 = (D Upsilon)^! K* (D Upsilon).
```

Derivatives of the residual pairing/receiver and second derivatives of
`Upsilon` multiply `Upsilon*` and drop at this stationary gate. Therefore the
next wave must not brute-force the full second derivative of every moving
object. It must construct the first derivative `J=D Upsilon` once on the
common action-owned field tangent, verify `J R=0` for the complete
diffeomorphism generator, derive the actual residual pairing/formal adjoint,
and only then form `J^! K J` and its Green concomitant.

This does **not** freeze the geometry. The source residual is a sum of
nonzero curvature and augmented-torsion constituents. Even when they cancel
in total, physical metric movement of Shiab and Hodge contributes

```text
(D Shiab) F_A* + (D Hodge)(kappa T*)
```

inside `D Upsilon`. Common equivariant co-motion acts on total `Upsilon*` and
vanishes; independent physical operator movement does not. That distinction
is load-bearing.

## Layer 0

| object | role | forbidden substitution |
| --- | --- | --- |
| first-action Hessian | Euler/Schur endomorphism on the first-layer field tangent | raw `D Upsilon` |
| `D Upsilon` | map from common field tangent to the typed residual carrier | second-action Hessian |
| second-action Hessian | `(D Upsilon)^! K* (D Upsilon)` at `Upsilon*=0` | isolated ten-by-ten metric diagnostic |
| moving pairing/receiver | its value `K*` and dependent chain rule remain | its derivative as a stationary bulk-Hessian term |
| physical Shiab/Hodge movement | constituent terms inside `D Upsilon` | pure target/frame co-motion |
| observation | dependent receiver/evaluation unless separately varied by the action | an invented independent Hessian column |
| Ward radical | `J R=0`, hence `H2 R=0` | BV/BFV quotient or physical state space |

The v0.81 `34 x 34` first-layer Schur Hessian is not retyped as `D Upsilon`.
The repo does not yet provide an explicit identification of its codomain with
the residual carrier, and the two actions are distinct.

## Exact theorem and controls

An exact nonlinear two-field fixture has:

- `Upsilon(0)=0`;
- nonzero `D2 Upsilon`;
- nonzero derivatives of a moving indefinite pairing;
- stationary Hessian exactly `J^T K J`; and
- an off-shell point where that reduction fails.

A separate block fixture splits metric, connection and matter/grade fields.
No individual block is Ward-basic, while their combined `J R` vanishes and
the Gram Hessian is symmetric and Ward-basic. Deleting a live block fires the
planted control.

The Krein control is equally important: an injective `J` can have
`J^T K J=0` on an isotropic image for indefinite `K`. Thus the factorization
does not determine the physical kernel, energy sign or domain until the
actual residual pairing and analytic domain are built.

## Lightweight divergent preassessment

1. **Layer-0 semantics:** separate first Euler Hessian, residual Jacobian and second Hessian.
2. **Variational bicomplex:** use the on-shell second-variation identity, not an informal square.
3. **Symplectic geometry:** retain the Green concomitant and presymplectic boundary obligation.
4. **Krein/operator theory:** indefinite `K` can add isotropic kernel; positivity is unavailable.
5. **Complex/analytic geometry:** a real Gram operator does not choose a contour or holomorphic polarization.
6. **Path-integral/QFT:** a quadratic fluctuation operator is not a measure, determinant or unitarity result.
7. **Microlocal PDE:** Ward closure precedes characteristic and hyperbolicity tests.
8. **Differential geometry:** independent physical Shiab/Hodge motion survives inside `D Upsilon`.
9. **Source criticism:** source owns the norm-square grammar, not the K77 block map.
10. **Constraint accounting:** no field, coefficient, quotient or datum is added.

All ten lenses select the same efficient gate: construct `D Upsilon`, not the
untyped full second derivative of the action.

## Hostile review disposition

The hostile review fired two fences:

- the summary must say the stationary factorization is composed from an
  already-proved theorem, not newly discovered here; and
- the efficiency reduction must not delete independent physical
  `(D Shiab)F_A*` or `(D Hodge)T*` terms by confusing residual-zero with
  constituent-zero.

It also rejected promoting a Ward-basic Gram matrix to a symplectic/BFV
quotient or a path-integral contour.

## Progress and next gate

```text
Ledger v0.82 — 82/82 active rows mapped (100%)
32 SAME · 19 DIFFERS · 26 NEEDS · 5 OVER-DETERMINED
Residue — 84 continuous + >=19 function-valued + 9 forks
Scoped quotients ranked — 5

headline_delta: none
frontier_conditions_closed: 4
  - second-layer stationary bulk Hessian needs only D Upsilon and K*
  - D2 Upsilon and D K/receiver terms drop at Upsilon*=0
  - physical Shiab/Hodge operator movement remains inside D Upsilon
  - observation is a dependent receiver, not a free action column
frontier_conditions_opened: 0
remaining_named_conditions: 3
  - construct every action-owned common-field block of D Upsilon
  - derive K*, the formal adjoint and Green concomitant; verify J R=0
  - compute coupled characteristic/Green/Krein and boundary BV-BFV classes
```

No verdict, residue, quotient, external datum, canon or public posture moves.
P1/P2/P3 remain unused. Curt remains formally separate.

## Verification

- main exact SymPy route: `42/42 PASS`;
- independent Sage/QQ route: `8/8 PASS`;
- planted off-shell, deleted-block, constituent-zero and indefinite-Krein
  controls all fire in the intended direction.

## Next gate

`ASSEMBLE_SELECTED_COMMON_FIELD_DUPSILON_BLOCK_MATRIX__VERIFY_JR_ZERO__DERIVE_K_ADJOINT_AND_GREEN_CONCOMITANT__THEN_FORM_STATIONARY_GRAM_HESSIAN`.
