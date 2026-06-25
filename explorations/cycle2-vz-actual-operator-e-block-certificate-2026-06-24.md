---
title: "Cycle 2 VZ Actual-Operator E-Block Certificate"
date: 2026-06-24
status: exploration/cycle2_gate
doc_type: vz_actual_operator_e_block_certificate
verdict: "ACTUAL_OPERATOR_E_BLOCK_CERTIFICATE_OPEN__TYPED_SPINE_FORMAL_BLOCK_TESTED_ONLY"
owned_path: "explorations/cycle2-vz-actual-operator-e-block-certificate-2026-06-24.md"
companion_audit: "tests/cycle2_vz_actual_operator_e_block_audit.py"
depends_on:
  - "RESEARCH-POSTURE.md"
  - "process/runbooks/five-lane-frontier-run.md"
  - "explorations/cycle1-vz-subprincipal-eblock-proof-gate-2026-06-24.md"
  - "explorations/vz-e-block-independent-rederivation-2026-06-24.md"
  - "explorations/vz-proof-grade-closure-attempt-2026-06-24.md"
  - "explorations/vz-principal-symbol-convention-reconciliation-2026-06-24.md"
  - "tests/vz_typed_symbol_gate.py"
---

# Cycle 2 VZ Actual-Operator E-Block Certificate

## 1. Verdict

FC-VZ-1 is still not closed for the actual GU operator.

The current repo has a good typed-spine algebra certificate for the proposed block, but it
does not yet have the source-closed operator certificate saying that the actual 0/1-sector
`D_GU` has that block. The correct status is:

```text
formal typed-spine E-block: tested in the Clifford quotient G^2 = q
toy/embedded inverse arithmetic: valid for the displayed block
actual GU E-block: open, because E_actual(xi) has not been extracted from source-closed D_GU
FC-VZ-1: explicit open actual-operator certificate
full VZ evasion claim: false
```

This is not a negative result against GU. It is a sharper proof obligation. To close the
actual-operator E-block gate, the repo must exhibit the operator-level map

```text
E_actual^epsilon(y, xi)
  :=
  P_Q,out^epsilon sigma_1(D_GU^epsilon)(y, xi) I_Q,in^epsilon
```

and prove by direct Clifford algebra that it is invertible for every real non-null
`xi in T_y^*Y`, with `q = g_Y^{-1}(xi, xi) != 0`.

The important refinement from Cycle 1 is this: E-block invertibility itself mainly needs
the codifferential/gradient off-diagonal coefficients to be nonzero. The coefficient of
`Phi_d := Phi_2 o d_A` is load-bearing for the spin-3/2 Schur symbol and the `13/98`
entry, but not by itself required for the minimal two-row E-kernel argument. Therefore
FC-VZ-1 should not be closed by citing `lambda_d != 0` alone, and VZ should not be
upgraded by citing an E inverse alone.

## 2. What current E-block tests prove

The current audit `tests/vz_typed_symbol_gate.py` proves the following finite algebra
facts over the quotient algebra

```text
Q(q)[G] / (G^2 - q).
```

It verifies:

```text
1. The typed-spine rational coefficients in dimension n = 14:
   scalar_to_trace_embedded = 1/14
   trace_to_scalar = 1/14
   trace_to_trace_coordinate = 13/7
   trace_to_trace_embedded = 13/98

2. The proposed embedded E-block inverse is two-sided:
   E_embed * E_embed^{-1} = Id
   E_embed^{-1} * E_embed = Id

3. The trace-coordinate E-block inverse is also two-sided.

4. The typed-spine spin-3/2 Schur coefficients are:
   -G psi_A + 16 xi_A G chi / q - gamma_A chi.

5. If lambda_d = 0, the tested E-block remains invertible off q = 0, but the effective
   spin-3/2 Schur principal symbol collapses.
```

Those are real checks, but their scope is not the actual GU operator. They prove the
formal typed-spine or toy/embedded inverse after the block has already been supplied.
They do not prove:

```text
actual_operator_has_this_E_block
actual_D_GU_contains_the_required_0_1_principal_terms
actual_Q_sector_is_exactly_S_plus_Im_j_with_no_extra_principal_component
actual_chirality_domains_match_the_tested_G_maps
actual_signature_convention_is_the_same_G^2_equals_q_convention
actual_non_null_cone_has_no_mixed_horizontal_vertical_exception
```

So existing tests are best read as a reusable algebra backend. They are not yet an
actual-operator E-block certificate.

## 3. Actual-operator E-block certificate definition

Fix a point `y in Y` and a chirality `epsilon in {+,-}`. The certificate must start from
the actual operator, not from the displayed matrix.

The carrier convention is:

```text
Y = Met_Lor(X), dim Y = 14
signature(g_Y) = (9,5)
Clifford convention: gamma(alpha) gamma(beta) + gamma(beta) gamma(alpha)
  = 2 g_Y^{-1}(alpha, beta) Id
G := gamma(xi)
q := g_Y^{-1}(xi, xi)
G^2 = q Id
```

The typed 0/1 spine is:

```text
D_GU^epsilon:
  Gamma(S^epsilon plus (T^*Y tensor S^{-epsilon}))
    ->
  Gamma(S^{-epsilon} plus (T^*Y tensor S^epsilon)).
```

The proposed typed-spine principal block is:

```text
sigma_1(D_roll^epsilon)(xi)(u, psi)
  =
  (
    i_xi psi,
    xi tensor u + lambda_d F_xi psi
  )

(F_xi psi)_A
  =
  xi_A gamma^B psi_B - G psi_A.
```

The actual certificate must not assume this. It must prove that the actual
`sigma_1(D_GU^epsilon)(xi)` has the needed Q-block after projection.

Define the gamma-trace maps:

```text
Gamma_{-epsilon}: T^*Y tensor S^{-epsilon} -> S^epsilon
Gamma_{-epsilon}(psi) = gamma^A psi_A

j_epsilon: S^epsilon -> T^*Y tensor S^{-epsilon}
j_epsilon(s)_A = (1/14) gamma_A s

Gamma_{-epsilon} j_epsilon = Id_{S^epsilon}
```

The input and output Q spaces are not literally the same chiral bundle:

```text
Q_in^epsilon
  =
  S^epsilon plus Im(j_epsilon)
  subset S^epsilon plus (T^*Y tensor S^{-epsilon})

Q_out^epsilon
  =
  S^{-epsilon} plus Im(j_{-epsilon})
  subset S^{-epsilon} plus (T^*Y tensor S^epsilon).
```

Let `I_Q,in^epsilon` be the inclusion and let `P_Q,out^epsilon` be the projection onto
the scalar plus gamma-trace output sector. Then the actual E-block is:

```text
E_actual^epsilon(y, xi)
  =
  P_Q,out^epsilon sigma_1(D_GU^epsilon)(y, xi) I_Q,in^epsilon
  :
  Q_in^epsilon -> Q_out^epsilon.
```

The certificate closes only when this object is computed from the actual `D_GU` and then
shown invertible on the non-null cone.

A convenient exact target is the trace-coordinate matrix. For input coordinates
`(phi, s) in S^epsilon plus S^epsilon`, meaning `(phi, j_epsilon(s))`, the typed-spine
target is:

```text
E_coord^epsilon(xi)
  =
  [[0,        a (1/14) G],
   [b G,      lambda_d (13/7) G]]
  :
  S^epsilon plus S^epsilon -> S^{-epsilon} plus S^{-epsilon}.
```

Here `a` is the principal coefficient of the `d_A^* psi` block and `b` is the principal
coefficient of the `d_A u` block. The typed proposal has:

```text
a = 1
b = 1
lambda_d = 1
```

In embedded one-form notation the same target is:

```text
E_embed^epsilon(xi)
  =
  [[0,        a (1/14) G],
   [b (1/14) G, lambda_d (13/98) G]].
```

The proof file must choose one convention before writing an inverse. Mixing
trace-coordinate and embedded-coordinate entries is a proof-grade failure.

The direct kernel proof obligation is:

```text
Assume q != 0, a != 0, b != 0, and G^2 = q Id.
If E_coord^epsilon(xi)(phi, s) = 0, then:
  top row: a (1/14) G s = 0, so s = 0;
  bottom row with s = 0: b G phi = 0, so phi = 0.
Therefore ker E_coord^epsilon(xi) = 0.
Finite-dimensional equal-rank chiral fibers then give invertibility.
```

This proof is direct. It does not use `det(M) = det(E) det(S_R)`, and it does not require
`lambda_d != 0`. The Schur spin-3/2 VZ route still requires the actual one-form block
data, including `lambda_d`, because `lambda_d = 0` collapses the tested spin-3/2
principal Schur symbol.

## 4. Cone, signature, domain/codomain, and typed-spine requirements

The relevant cone is the real non-null cone in the 14D cotangent fiber:

```text
NonNull_y(Y) = {xi in T_y^*Y : q = g_Y^{-1}(xi, xi) != 0}.
```

The null cone `q = 0` is the expected characteristic locus. Failure of E-invertibility
there is not a VZ-kill by itself. A failure on the non-null cone is a kill condition for
FC-VZ-1.

The certificate must explicitly fix:

```text
signature:       signature(g_Y) = (9,5)
Clifford sign:   G^2 = g_Y^{-1}(xi, xi) Id, not an unstated opposite sign
base cone:       xi ranges over all real T_y^*Y covectors, including mixed horizontal/vertical
domain:          Q_in^epsilon = S^epsilon plus Im(j_epsilon)
codomain:        Q_out^epsilon = S^{-epsilon} plus Im(j_{-epsilon})
projection:      P_Q,out^epsilon is scalar plus gamma-trace output projection
inclusion:       I_Q,in^epsilon is scalar plus gamma-trace input inclusion
operator source: sigma_1(D_GU^epsilon), not a free 2 by 2 toy matrix
coordinate rule: trace-coordinate or embedded-coordinate matrix, not both at once
```

The typed-spine embedding requirement is:

```text
D_GU^epsilon must agree at principal order on the 0/1 sector with the coefficient form

sigma_1(D_GU^epsilon)(xi)(u, psi)
  =
  (
    a i_xi psi,
    b xi tensor u + lambda_d F_xi psi + K_QQ^epsilon(xi) psi + K_RQ^epsilon(xi) psi
  )

where the projected Q-to-Q part is exactly the displayed E_actual block, and any extra
first-order terms have been projected and shown either absent or harmless.
```

The minimal E-invertibility certificate needs `a != 0` and `b != 0`. The stronger VZ
Schur certificate also needs the actual projected spin-3/2 block and, for the current
typed-spine formula, `lambda_d != 0`.

## 5. Failure modes that would kill FC-VZ-1

The following are rollback or kill conditions for FC-VZ-1:

```text
1. A real non-null covector xi with q != 0 and ker E_actual^epsilon(y, xi) != 0.

2. The actual principal coefficient a of d_A^* psi vanishes on the relevant 0/1 block.

3. The actual principal coefficient b of d_A u vanishes on the relevant 0/1 block.

4. The actual Q-sector is not S^epsilon plus Im(j_epsilon), or has extra principal
   components that change the projected E-block and create a non-null kernel.

5. The actual Clifford convention does not satisfy G^2 = q Id in signature (9,5), or the
   sign convention is changed without changing the inverse/kernel proof accordingly.

6. The actual block uses a different gamma-trace normalization, so the displayed matrix
   is not the matrix of E_actual in the chosen coordinates.

7. A mixed horizontal/vertical non-null covector falls outside the certificate because the
   proof only checked pure horizontal or pure vertical samples.

8. First-order lower-block terms hidden in Z_A, gauge fixing, section pullback, or
   chirality mixing alter P_Q sigma_1(D_GU) I_Q.

9. The proof closes only by determinant circularity rather than a direct kernel or
   two-sided inverse argument after E_actual is computed.
```

The following are not FC-VZ-1 kills by themselves, but they prevent a broader VZ upgrade:

```text
1. lambda_d = 0. E may remain invertible off q = 0, but the typed spin-3/2 Schur
   principal symbol used for VZ evasion collapses.

2. E fails at q = 0. That is the expected null characteristic behavior, not a spacelike
   failure.

3. Phi_F := Phi_2(F_A tensor -) exists only as a zero-order curvature insertion. That term
   does not supply the F_xi principal block and cannot justify the 13/98 entry.
```

## 6. Impact for VZ evasion and what remains for FC-VZ-4

The actual-operator E-block certificate would be useful, but it would not by itself prove
full VZ evasion.

If the actual certificate closes with `a != 0`, `b != 0`, and the displayed Q-sector
projection, then FC-VZ-1 can move from open to closed for E-invertibility. The next
principal-symbol question would be the actual spin-3/2 Schur block:

```text
S_R^epsilon(xi)
  =
  A_actual^epsilon(xi)
  - B_actual^epsilon(xi) E_actual^epsilon(xi)^{-1} C_actual^epsilon(xi).
```

For the current typed-spine Schur formula, that step needs the actual one-form-to-one-form
`Phi_d` coefficient. If `lambda_d = 0`, E-invertibility survives but the proposed VZ
principal-symbol evasion route fails.

FC-VZ-4 remains live either way. It asks whether the 4D section-pulled effective dynamics
can generate VZ-style spacelike behavior through subprincipal, extrinsic-curvature,
constraint-propagation, or effective first-order terms. The remaining object is still:

```text
sigma_0^inv(S_{R_s}^{4D,full})(x, eta)
```

with the actual section pullback, `II_s^H`, spin/gimmel connection terms, `Phi_F`, mass
terms, gauge-fixing terms, Poisson-bracket/invariant-subprincipal corrections, and the
full `Z_A` ledger. Closing the 14D E-block does not close this 4D/subprincipal gate.

Therefore the present impact is:

```text
VZ evasion status: not upgraded
FC-VZ-1: explicit actual-operator certificate remains open
FC-VZ-4: open and unaffected except that it may use E_actual^{-1} if FC-VZ-1 later closes
full VZ evasion claim: false
```

## 7. Next meaningful computation

The next computation should extract `E_actual` from a primary operator object. It should
not start by re-testing the already supplied inverse.

Required matrix/operator data:

```text
1. The actual 0/1-sector principal symbol sigma_1(D_GU^epsilon)(y, xi), with all
   first-order terms and coefficients.

2. The coefficients:
   a = coefficient of i_xi psi in the scalar output;
   b = coefficient of xi tensor u in the one-form output;
   lambda_d = coefficient of Phi_2(d_A psi) in the one-form output.

3. A yes/no separation of:
   Phi_2                  algebraic zero-order shiab
   Phi_d := Phi_2 o d_A   first-order differential composite
   Phi_F := Phi_2(F_A tensor -) zero-order curvature insertion
   F_xi := sigma_1(Phi_d)(xi)

4. The exact chiral gamma-trace projectors Gamma, j, P_Q,in, P_Q,out and their
   normalizations in signature (9,5).

5. The projected matrix:
   E_actual^epsilon(y, xi) = P_Q,out sigma_1(D_GU^epsilon)(y, xi) I_Q,in
   in one chosen convention, trace-coordinate or embedded-coordinate.

6. A formal Clifford quotient or faithful Cl(9,5) representation check proving the direct
   kernel or two-sided inverse for every q != 0.

7. A non-null mixed-covector audit showing the proof quantified over all real
   xi in T_y^*Y, not only sample covectors.
```

The smallest useful follow-on audit would accept the extracted coefficients
`a`, `b`, `lambda_d` and the projected Q-matrix, then verify:

```text
q != 0 and a*b != 0 implies ker E_actual(xi) = 0.
```

If the extraction yields any first-order Q-block not matching the typed target, the audit
should stop and require a new kernel proof for that actual matrix.

## 8. Machine-readable JSON summary

```json
{
  "artifact": "cycle2-vz-actual-operator-e-block-certificate-2026-06-24",
  "verdict": "ACTUAL_OPERATOR_E_BLOCK_CERTIFICATE_OPEN__TYPED_SPINE_FORMAL_BLOCK_TESTED_ONLY",
  "full_vz_evasion_claim": false,
  "fc_vz_1_explicit": true,
  "fc_vz_1_status": "open_actual_operator_E_block_certificate_not_closed",
  "fc_vz_4_status": "open_subprincipal_section_pulled_gate_not_closed",
  "actual_vs_toy_separated": true,
  "toy_or_embedded_e_block_status": {
    "status": "tested_formal_typed_spine_block_only",
    "test_file": "tests/vz_typed_symbol_gate.py",
    "proves": [
      "rational_coefficients_1_14_13_7_13_98_for_typed_spine",
      "two_sided_inverse_in_formal_quotient_G_squared_equals_q",
      "trace_and_embedded_coordinate_inverse_arithmetic",
      "lambda_d_zero_keeps_E_invertible_but_collapses_spin_three_halves_Schur_symbol"
    ],
    "does_not_prove": [
      "actual_D_GU_has_this_E_block",
      "actual_Q_sector_exact",
      "actual_chirality_domains",
      "actual_non_null_mixed_covector_quantification"
    ]
  },
  "actual_operator_e_block_status": {
    "status": "open_not_proved",
    "definition": "E_actual^epsilon(y,xi)=P_Q_out^epsilon sigma_1(D_GU^epsilon)(y,xi) I_Q_in^epsilon",
    "domain": "Q_in^epsilon=S^epsilon plus Im(j_epsilon) subset S^epsilon plus T^*Y tensor S^{-epsilon}",
    "codomain": "Q_out^epsilon=S^{-epsilon} plus Im(j_{-epsilon}) subset S^{-epsilon} plus T^*Y tensor S^epsilon",
    "cone": "q=g_Y^{-1}(xi,xi)!=0 for real xi in T_y^*Y",
    "signature": "signature(g_Y)=(9,5), Clifford convention G^2=q Id",
    "minimal_invertibility_conditions": [
      "a_coefficient_of_d_A_star_nonzero",
      "b_coefficient_of_d_A_u_nonzero",
      "G_squared_equals_q_Id",
      "q_nonzero",
      "actual_projected_Q_block_matches_certificate_matrix_or_has_own_kernel_proof"
    ]
  },
  "certificate_target_matrix": {
    "trace_coordinate": "[[0, a*(1/14)*G], [b*G, lambda_d*(13/7)*G]]",
    "embedded_coordinate": "[[0, a*(1/14)*G], [b*(1/14)*G, lambda_d*(13/98)*G]]",
    "typed_spine_coefficients": {
      "a": "1",
      "b": "1",
      "lambda_d": "1"
    }
  },
  "required_matrix_operator_data": [
    "actual_sigma_1_D_GU_0_1_sector",
    "coefficient_a_of_i_xi_psi",
    "coefficient_b_of_xi_tensor_u",
    "coefficient_lambda_d_of_Phi_2_d_A_psi",
    "Phi_2_Phi_d_Phi_F_F_xi_order_separation",
    "chiral_Gamma_j_P_Q_in_P_Q_out_normalizations",
    "one_coordinate_convention_trace_or_embedded",
    "all_extra_first_order_Q_block_terms_or_proof_absent",
    "all_real_mixed_horizontal_vertical_covectors_quantified"
  ],
  "rollback_conditions": [
    "actual_operator_E_block_has_non_null_kernel",
    "coefficient_a_of_d_A_star_vanishes",
    "coefficient_b_of_d_A_u_vanishes",
    "actual_Q_sector_not_S_plus_Im_j_or_has_extra_principal_component",
    "signature_or_Clifford_convention_not_G_squared_equals_q_Id",
    "gamma_trace_normalization_differs_without_rederived_inverse",
    "mixed_horizontal_vertical_non_null_covector_not_covered",
    "hidden_first_order_Z_A_or_gauge_fixing_terms_modify_Q_block",
    "determinant_circularity_used_instead_of_direct_E_actual_kernel_proof"
  ],
  "non_rollbacks_but_no_vz_upgrade": [
    "lambda_d_zero_E_may_still_invert_but_spin_three_halves_Schur_route_collapses",
    "E_failure_on_q_equals_zero_expected_null_locus",
    "Phi_F_zero_order_does_not_supply_F_xi_or_13_98_entry"
  ],
  "fc_vz_4_remaining": [
    "compute_sigma_0_inv_S_Rs_4D_full",
    "include_II_s_H",
    "include_Z_A_lower_order_ledger",
    "include_Phi_F_mass_spin_connection_gauge_fixing_terms",
    "prove_no_effective_first_order_spacelike_characteristic"
  ],
  "next_meaningful_computation": [
    "extract_E_actual_from_primary_D_GU",
    "compute_P_Q_out_sigma_1_D_GU_I_Q_in",
    "run_formal_Clifford_kernel_audit_for_actual_matrix",
    "then_compute_actual_spin_three_halves_Schur_symbol"
  ]
}
```
