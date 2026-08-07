---
run_id: GUH-20260731T143243Z-g2-field-space-native-variational-shiab
status: complete
repository: gu-formalization
workflow: joe-directed-north-star-construction
mode: execute
run_type: progress
lane_id: "1"
work_item: G2-FIELD-SPACE-NATIVE-VARIATIONAL-SHIAB
starting_revision: fc397c90b8f04f11540e73b8fff860dec0be2277
opened_at: 2026-07-31T14:32:43Z
closed_at: 2026-07-31T14:42:35Z
claim_status_change: none
canon_change: none
public_posture_change: none
external_action_authorization: github_commit_and_push_only
---

# G2 field space and native variational Shiab

## Objective

Declare the complete field/graph policy downstream of G1 and construct the
native density-dual curvature contraction needed by the first-order source
action. Test the source's cyclic/transgression simplification. If it fails,
do not stop at the failed author formula: derive and retain the exact
slot-symmetrized Euler geometry emitted by the written action, with its
moving-reference and boundary obligations.

## Layer-0 precondition

| term | object A | object B | mark |
| --- | --- | --- | --- |
| Shiab | spinorial `Lambda2 tensor S -> Lambda1 tensor S` | bosonic density-dual `Omega2(adP)->Omega13(ad*P)` | `HOMONYM`; only the second can enter this action slot |
| Shiab current | a fixed linear curvature contraction `S(F)` | the complete Euler covector of an action containing `S` | `HOMONYM`; equal only after Helmholtz/cyclic identities |
| exact | differential of a written functional | de Rham exact, gauge Noether, or source redundancy `Xi=D Upsilon` | `HOMONYM`; G2 tests only variational exactness |
| `epsilon` | source gauge transformation | G1 moving LC-equipped reduction `epsilon_red` | `HOMONYM`; use the G1 gauge action and graph map |
| `B` | independently varied connection | graph composite `A_LC(epsilon_red,g_DW)` | construction fork; G2 must choose |
| curvature | arbitrary full-adjoint curvature | pointwise algebraic-Riemann/Levi--Civita curvature | `HOMONYM`; RB1c's grade-three response differs on these strata |

## Native/comparator fork

- Native: `Y^14=Met(X^4)`, trace-reversed fibre `(6,4)`, total `(9,5)`,
  `G=Sp(32,32;H)`, right-`H`, Krein pairing, moving Spin reduction.
- Source comparator: the draft's `Y^(7,7)/U(64,64)`-type presentation.
- Hostile standard comparator: positive-Hilbert/complex-only contraction or
  raw `(7,3)` fibre. A success there cannot transfer silently.

## Selected field policy to test

1. `A` (the native endpoint represented by source `varpi`) is a free
   connection.
2. `epsilon_red` is a varied moving LC-equipped reduction.
3. `B=A_LC(epsilon_red,g_DW)` is graph constrained, not independently
   varied.
4. `T=A-B` is a derived adjoint-valued one-form.
5. `S_epsilon=S_tr,epsilon` is the RB1c trace-line-adapted native
   density-dual contraction, moved with the reduction.
6. `g_DW` and the observation section are fields of the complete theory;
   G2 records their graph arrows and leaves their full Euler terms to G3.
7. G1's `Gamma_epsilon^A0` is a hostile comparator only; `A0` is not added to
   the selected action.
8. The N1 independent `U`, P1, P2, and P3 are not identified with `B`, `T`,
   or the Shiab packet.

## Candidate action

With `q(T,T)` the symmetric polarization of the connection quadratic term,
test

```text
I_1[A,epsilon_red,g_DW]
 = integral T wedge S_epsilon(
       F_B + (1/2) D_B T + (1/3) q(T,T))
   + (kappa_1/2) integral T wedge flat(T).
```

The coefficients and field dependencies are frozen before computing.

## Pre-registered expected verdict

RB1c already makes a nonzero native `S_tr,epsilon` available, including on
the scalar algebraic-Riemann stratum, but its fixed-linear cyclic identity
failed. The source simplification

```text
E_T = S_epsilon(F_(B+T)) + kappa_1 flat(T)
```

is therefore expected to fail for this candidate. The written functional
should nevertheless have an exact Euler covector. The expected constructive
repair is not a fitted coefficient: `1/2` and `1/3` normalize the two and
three field slots, producing the symmetric part of `S D_B` and the complete
symmetric polarization of the cubic form. This action-native Euler packet is
expected to survive even though it does not factor through one linear
curvature-to-source map.

## Kill conditions

1. A zero bosonic Hom result on the chosen trace-adapted full-adjoint carrier
   kills the selected map; a zero same-`Lambda2` result alone does not.
2. Failure of native right-`H`, Krein reality, moving-reduction covariance,
   or trace-reversed Hodge degree kills the native map.
3. Independent free variation of `B` that adds an unowned equation or forces
   `T=0` kills that field policy. The selected graph policy must not vary `B`
   independently.
4. Omitting `delta epsilon`, `delta g_DW`, graph-chain, density, Hodge, or
   boundary responses kills a claim of complete variation.
5. Failure of the fixed-linear cyclic/transgression identity kills the
   simplified source `Upsilon`, not automatically the written action.
6. Failure of exact finite-difference agreement for the full unsimplified
   variation kills the variational completion.
7. A claimed repaired linear `S(F)` must fail if a planted pair has zero
   polarized curvature but nonzero polarized Euler response.
8. Free left/right coefficients, a chosen complex unit, inert soldering, or
   an additive background are forbidden repairs.
9. The source action may not be placed beside the N1 YM/parent/bridge family
   without a declared replacement map; double counting kills the record.
10. No form degree, Clifford grade, complex length, or stabilizer component
    may be read as chirality, index, or observed generation count.

## Constraint-surplus policy

The `1/2,1/3` coefficients are source-supplied and charged as guidance. Their
slot-normalization role is testable but not counted as a repo-derived
parameter fit. Algebraically dependent variation identities are counted once.
Global surplus remains uncomputable until G3 prices the metric/reduction
domain and G7--G9 price the physical projections and datum.

## Planned outputs

- a full source field/graph/dependency specification;
- a native linear-Shiab versus action-native Euler dossier;
- a machine-readable certificate;
- an exact transgression/Helmholtz probe with cyclic positive control,
  noncyclic native-shaped plant, moving-insertion covariance, and exact
  slot-symmetrized variation;
- roadmap/navigation updates; and
- validation, commit, push, and closing receipt.

## Boundary

G2 does not claim the complete G3 Euler/Noether/BV--BFV packet, a selected
global reduction, ambient domain, N1/source identity, VEV, Higgs, stationary
vacuum, anomaly closure, index, count, cosmological amplitude, or PP3 result.

## Completed result

G2 closes as a **conditional construction pass with a source-formula
correction**.

- The selected fields are `A`, `epsilon_red`, and the complete metric/section
  packet. `B=A_LC(epsilon_red,g_DW)` is graph constrained and `T=A-B` is
  derived; no independent `B` equation was introduced.
- The native trace-adapted density-dual map is installed in the fourteen-form
  source action with its right-`H`, Krein, moving-reduction, and trace-reversed
  type inherited from RB1c.
- The fixed-linear source simplification is killed for this map by the failed
  cyclic/Helmholtz conditions.
- Exact variation of the written action survives and gives
  `S_epsilon(F_B) + 1/2(L+L^!)T + M_epsilon(T,T) + kappa_1 flat(T)`.
  The two-input `M_epsilon` cannot in general be replaced by one linear map of
  the polarized curvature.
- The `1/2` and `1/3` coefficients are verified as two-slot and three-slot
  normalizations, but remain Eric/source guidance rather than independent
  surplus.

## Validation

- `g2_native_variational_shiab_probe.py`: 13 exact checks plus 9 planted
  failures, 22 PASS.
- G1 derivative-cocycle regression: 29 PASS.
- RB1b, RB1c, and RB2 source-action regressions: PASS with their historical
  branch-local verdicts unchanged.
- Python compilation, JSON parsing, test-inventory audit, and `git diff
  --check`: PASS.

## Next swing

G3 must vary the corrected action, not the killed compressed source. It must
carry the graph responses of `epsilon_red`, `g_DW`, the observation section,
`B`, the Hodge/density data, and the boundary potential into the coupled
Noether identities and minimal BV--BFV test.
