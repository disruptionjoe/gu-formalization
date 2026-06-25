---
title: "Hourly Cycle 2 VZ Actual 0/1 Operator Certificate Gate"
date: 2026-06-24
status: exploration/hourly_cycle2_gate
doc_type: vz_actual_operator_certificate_gate
verdict: "UNDERDEFINED_BLOCKED__ACTUAL_DGU_01_OPERATOR_CERTIFICATE_MISSING_TYPED_SPINE_ONLY"
owned_path: "explorations/hourly-cycle2-vz-actual-operator-certificate-gate-2026-06-24.md"
companion_audit: "tests/hourly_cycle2_vz_actual_operator_certificate_gate_audit.py"
depends_on:
  - "RESEARCH-POSTURE.md"
  - "process/runbooks/five-lane-frontier-run.md"
  - "explorations/hourly-cycle1-vz-subprincipal-characteristic-contract-2026-06-24.md"
  - "explorations/cycle2-vz-actual-operator-e-block-certificate-2026-06-24.md"
  - "explorations/vz-proof-grade-closure-attempt-2026-06-24.md"
  - "explorations/vz-proof-grade-verification-gate-2026-06-24.md"
  - "explorations/vz-e-block-independent-rederivation-2026-06-24.md"
  - "explorations/gu-typed-operator-action-spine-2026-06-24.md"
  - "canon/no-go-class-relative-map.md"
---

# Hourly Cycle 2 VZ Actual 0/1 Operator Certificate Gate

## 1. Verdict

The current repo sources do not yet identify the actual GU Rarita-Schwinger
0/1-sector operator. They identify a coherent typed-spine candidate and strong
conditional Clifford algebra for that candidate.

The missing object is:

```text
ActualDGU01OperatorCertificate
```

Until that certificate exists, the VZ gate status is:

```text
actual_operator: not source-closed
available operator: D_roll typed-spine candidate
FC-VZ-1: open for the actual GU operator
FC-VZ-4: open for the actual section-pulled subprincipal and constraint system
full_vz_evasion_claim: false
```

This is not a refutation of the GU VZ route. It is a certificate boundary. The typed
spine may still be the right operator, but the repo has not yet proved that it is the
operator selected by the actual GU source/action/Euler-Lagrange system.

The decision for this lane is therefore:

```text
UNDERDEFINED / BLOCKED on actual operator provenance.
Only typed-spine candidates are currently identified.
```

## 2. Actual operator certificate fields

The required certificate is a source-closed operator object. It must start from the
actual GU operator/action and then state the 0/1-sector symbol, not start from the
displayed VZ matrix.

The certificate fields should be:

```text
certificate_id:
  ActualDGU01OperatorCertificate

operator_source:
  primary GU source/action/Euler-Lagrange derivation for D_GU^epsilon

rolled_up_domain:
  E_roll^epsilon = S^epsilon plus (T^*Y tensor S^{-epsilon})

rolled_up_codomain:
  F_roll^epsilon = S^{-epsilon} plus (T^*Y tensor S^epsilon)

base_and_cone:
  Y = Met_Lor(X), dim Y = 14, signature(g_Y) = (9,5)
  q = g_Y^{-1}(xi, xi)
  xi ranges over all real mixed horizontal/vertical covectors
  non-null cone is q != 0

Clifford_convention:
  G = gamma(xi)
  G^2 = q Id

chirality_and_projectors:
  Gamma_{-epsilon}: T^*Y tensor S^{-epsilon} -> S^epsilon
  j_epsilon: S^epsilon -> T^*Y tensor S^{-epsilon}
  Q_in^epsilon = S^epsilon plus Im(j_epsilon)
  Q_out^epsilon = S^{-epsilon} plus Im(j_{-epsilon})
  I_Q_in^epsilon and P_Q_out^epsilon with normalization fixed

actual_principal_symbol:
  sigma_1(D_GU^epsilon)(y, xi) on the rolled-up 0/1 sector

coefficients:
  a = coefficient of i_xi psi in the scalar output
  b = coefficient of xi tensor u in the one-form output
  lambda_d = coefficient of Phi_d := Phi_2 o d_A in the one-form output

extra_order_one_terms:
  every additional 0/1 first-order term, projected to Q and R sectors,
  either proved absent or included in a new kernel proof

E_block_source:
  E_actual^epsilon(y, xi)
    = P_Q_out^epsilon sigma_1(D_GU^epsilon)(y, xi) I_Q_in^epsilon

coordinate_convention:
  exactly one of trace-coordinate or embedded-coordinate matrix notation

order_split:
  Phi_2 is zero-order algebraic shiab
  Phi_d := Phi_2 o d_A is first-order differential composite
  F_xi := sigma_1(Phi_d)(xi) is the principal-symbol one-form block
  Phi_F := Phi_2(F_A tensor -) is zero-order curvature insertion
  Z_A contains all lower-order connection, curvature, mass, gauge, theta,
      section-pullback, and constraint-source terms unless a reduction proves
      that one becomes effective order one

section_pullback:
  s^*D_GU^epsilon and the induced 4D domain/codomain after horizontal/normal split

constraint_blocks:
  gamma-trace constraint subsystem, Q/R Schur blocks, and K_mu_nu source ledger

subprincipal_payload:
  sigma_0_inv(S_Rs_4D_full)(x, eta), including II_s^H, Z_A, Phi_F,
  spin/gimmel connection, Poisson corrections, gauge fixing, mass terms,
  and constraint-source terms
```

The `Phi_d`/`Phi_F` convention is load-bearing:

```text
Phi_d supplies F_xi and the spin-3/2 Schur principal block.
Phi_F is lower order in the RS field and cannot supply F_xi.
```

The minimal E-block invertibility condition is not the same as the full Schur condition:

```text
FC-VZ-1 minimal E-kernel proof needs a != 0, b != 0, q != 0, and G^2 = q Id.
The typed spin-3/2 Schur route also needs the actual lambda_d != 0 and the actual
projected R-sector Schur symbol.
```

## 3. What prior VZ files establish

`RESEARCH-POSTURE.md` and the five-lane runbook require explicit assumptions,
rollback conditions, and no promotion from compatibility to derivation. That rule is
binding here.

`explorations/hourly-cycle1-vz-subprincipal-characteristic-contract-2026-06-24.md`
already names the source-closed actual `D_GU^epsilon` certificate as the first
obstruction and keeps FC-VZ-4 open for the actual section-pulled subprincipal matrix.

`explorations/cycle2-vz-actual-operator-e-block-certificate-2026-06-24.md` defines
the actual E-block:

```text
E_actual^epsilon(y, xi)
  = P_Q_out^epsilon sigma_1(D_GU^epsilon)(y, xi) I_Q_in^epsilon.
```

It also clarifies that `a` and `b` are enough for the minimal E-block kernel argument,
while `lambda_d` is load-bearing for the spin-3/2 Schur route.

`explorations/vz-proof-grade-closure-attempt-2026-06-24.md` proves a strong conditional
typed-spine result: if the actual operator has the rolled-up principal block

```text
sigma_1(D_roll^epsilon)(xi)(u, psi)
  =
  (i_xi psi, xi tensor u + F_xi psi)
```

with nonzero `lambda_d`, then the typed 14D spin-3/2 Schur symbol has no non-null
kernel. The file does not prove that `D_roll` is the actual GU operator.

`explorations/vz-proof-grade-verification-gate-2026-06-24.md` keeps the earlier
E-block arithmetic below promotion and requires independent operator-level derivation
before upgrading the 14D leg.

`explorations/vz-e-block-independent-rederivation-2026-06-24.md` rederives the
`1/14`, `13/7`, and `13/98` coefficients from the gamma-trace projector, but it is still
conditional on the canonical principal symbol.

`explorations/gu-typed-operator-action-spine-2026-06-24.md` supplies the best current
typed carrier proposal:

```text
D_roll^epsilon(u, psi)
  =
  (d_A^* psi, d_A u + Phi_2(d_A psi)) + Z_A^epsilon(u, psi).
```

It explicitly says this is a canonical proposal, not proof-grade closure of the actual
GU operator/action.

`canon/no-go-class-relative-map.md` keeps the VZ row conditional: the 14D leg is gated
on FC-VZ-1, and the 4D leg is principal-symbol level only while FC-VZ-4 remains open.

## 4. Strongest positive operator-certificate attempt

The strongest positive attempt is to promote the typed spine to a source-closed
principal-symbol certificate.

Assume the actual 0/1-sector operator has the same principal part as:

```text
D_roll^epsilon(u, psi)
  =
  (d_A^* psi, d_A u + lambda_d Phi_2(d_A psi)) + Z_A^epsilon(u, psi)
```

so that:

```text
sigma_1(D_GU^epsilon)(y, xi)(u, psi)
  =
  (
    a i_xi psi,
    b xi tensor u + lambda_d F_xi psi
  )
```

after projecting away or separately proving harmless every extra first-order 0/1 term.

In trace coordinates, the target Q-sector block is then:

```text
E_coord^epsilon(xi)
  =
  [[0,        a (1/14) G],
   [b G,      lambda_d (13/7) G]].
```

For `q != 0`, `G^2 = q Id`, `a != 0`, and `b != 0`, the direct kernel proof is:

```text
top row:    a (1/14) G s = 0, so s = 0
bottom row: b G phi = 0, so phi = 0
```

finite-dimensional equal-rank fibers then give invertibility. This would close the
actual E-block part of FC-VZ-1 if and only if the block is extracted from actual
`D_GU^epsilon`.

For the spin-3/2 Schur route, the same certificate must also identify the actual
one-form-to-one-form principal block. If it is the typed `lambda_d F_xi` block with
`lambda_d != 0`, the determinant-free typed Schur proof can be replayed for the actual
operator. If `lambda_d = 0`, the minimal E-block may still invert, but the current typed
spin-3/2 Schur mechanism collapses.

The positive attempt therefore reaches this conditional statement:

```text
If ActualDGU01OperatorCertificate proves the typed principal block with a != 0,
b != 0, lambda_d != 0, and no extra harmful first-order Q/R terms, then FC-VZ-1
can be replayed against the actual operator. FC-VZ-4 still remains to be computed
from the same operator after section pullback.
```

## 5. First exact missing proof object

The first missing proof object is not another inverse for the displayed E-block. It is:

```text
ActualDGU01OperatorCertificate:
  a source-closed 0/1-sector principal-symbol certificate for D_GU^epsilon.
```

It must prove all of the following in one convention:

```text
1. D_GU^epsilon has the rolled-up domain/codomain stated above.
2. sigma_1(D_GU^epsilon)(y, xi) has the actual 0/1 block.
3. a, b, and lambda_d are fixed by the actual source/action, not chosen for VZ.
4. Phi_d and Phi_F are separated by differential order.
5. Q_in, Q_out, Gamma, j, I_Q_in, and P_Q_out are fixed with chiral typing.
6. E_actual is projected from sigma_1(D_GU^epsilon), not imported as a toy matrix.
7. Extra first-order 0/1 terms are absent or included in a fresh all-covector kernel proof.
8. The proof quantifies over all real mixed horizontal/vertical non-null covectors.
```

After that object, the first FC-VZ-4 proof object is:

```text
ActualDGUSectionSubprincipalCertificate:
  sigma_0_inv(S_Rs_4D_full)(x, eta)
```

computed from the same actual `D_GU^epsilon`, with:

```text
S_Rs_4D_full = A_s_full - B_s_full (E_s_full)^(-1) C_s_full.
```

The first term to audit in that downstream object is:

```text
II_s^H = s^*(theta)
```

together with curved horizontal/normal frame derivatives and the `K_mu_nu` gamma-trace
constraint source.

## 6. Impact for FC-VZ-1/FC-VZ-4 and no-go map wording

For FC-VZ-1:

```text
status: open for the actual GU operator
reason: E_actual has not been extracted from source-closed D_GU^epsilon
current positive evidence: typed-spine algebra and independent coefficient rederivation
not enough: formal inverse of a displayed block
```

For FC-VZ-4:

```text
status: open for the actual section-pulled operator
reason: sigma_0_inv(S_Rs_4D_full)(x, eta) has not been computed from actual D_GU
current positive evidence: principal-symbol and lower-order ledgers are coherent
not enough: the claim that zero-order terms are harmless before the actual
            section-pulled Schur/constraint matrix is written
```

The no-go map wording should remain capped:

```text
VZ remains conditional at 14D, gated on actual-operator FC-VZ-1.
The 4D leg remains principal-symbol level only.
FC-VZ-4 remains open until the actual section-pulled subprincipal and constraint
characteristic matrix is computed.
The rollback condition is a non-null kernel or spacelike characteristic in that
actual matrix after II_s^H and K_mu_nu terms are included.
```

The map may continue to say that GU has a coherent conditional route through
Clifford-module non-decoupling. It should not say that the actual GU RS operator has
been shown free of spacelike characteristics.

## 7. Rollback/falsification conditions

FC-VZ-1 rolls back or fails if:

```text
actual D_GU^epsilon lacks the rolled-up 0/1 block
a = 0 for the d_A^* psi / i_xi psi scalar output
b = 0 for the d_A u / xi tensor u one-form output
actual Q-sector is not S plus Im(j), or has extra first-order components
E_actual has a nontrivial kernel for some real q != 0 covector
the proof checks only pure horizontal or pure vertical covectors
trace-coordinate and embedded-coordinate conventions are mixed
hidden first-order terms are placed in Z_A without projection or kernel audit
```

The spin-3/2 Schur route rolls back even if the minimal E-block survives when:

```text
lambda_d = 0
Phi_F is substituted for Phi_d as if it supplied F_xi
the actual R-sector Schur block differs from the typed-spine one and has a non-null kernel
```

FC-VZ-4 rolls back or fails if:

```text
there exists eta != 0 with g_s^{-1}(eta, eta) != 0 and
  ker sigma_1(S_Rs_4D_full)(x, eta) != 0

II_s^H = s^*(theta), curved frame splitting, or Codazzi-type pullback terms enter
  the effective order-one symbol

K_mu_nu or the gamma-trace constraint subsystem changes the characteristic cone

the sourced symmetric-hyperbolic estimate for phi = Gamma^{4D} Psi fails in a way
  that creates a spacelike characteristic

a standalone GU RS Lagrangian is derived whose actual characteristic matrix has
  VZ spacelike roots
```

The no-go map wording must roll back if it upgrades the VZ row before these gates close.

## 8. Next meaningful computation

The next meaningful computation is extraction, not another restatement of the existing
typed-spine inverse.

1. Build `ActualDGU01OperatorCertificate` from primary GU operator/action sources.
   It must output the rolled-up domain/codomain, `sigma_1(D_GU^epsilon)`, `a`, `b`,
   `lambda_d`, the `Phi_d`/`Phi_F` order split, Q projectors, and every extra
   first-order 0/1 term.
2. Compute
   `E_actual^epsilon = P_Q_out^epsilon sigma_1(D_GU^epsilon) I_Q_in^epsilon`
   in exactly one coordinate convention.
3. Run an all-covector Clifford kernel or two-sided-inverse audit for every real
   `q != 0`, including mixed horizontal/vertical covectors.
4. If FC-VZ-1 closes, compute the actual spin-3/2 Schur symbol
   `S_R^epsilon = A_actual - B_actual E_actual^{-1} C_actual`.
5. Pull the same actual operator to a section and compute
   `sigma_0_inv(S_Rs_4D_full)(x, eta)` with `II_s^H`, `Phi_F`, `Z_A`,
   spin/gimmel connection, mass/gauge-fixing terms, Poisson corrections, and
   the `K_mu_nu` constraint source.
6. Form the coupled RS/constraint characteristic matrix. Pass only if real
   characteristics remain confined to the null cone.

## 9. Machine-readable JSON summary

```json
{
  "artifact": "hourly-cycle2-vz-actual-operator-certificate-gate-2026-06-24",
  "verdict": "UNDERDEFINED_BLOCKED__ACTUAL_DGU_01_OPERATOR_CERTIFICATE_MISSING_TYPED_SPINE_ONLY",
  "actual_operator_status": "typed_spine_candidates_only_actual_DGU_not_identified",
  "full_vz_evasion_claim": false,
  "actual_operator_certificate": {
    "name": "ActualDGU01OperatorCertificate",
    "status": "missing_source_closed_certificate",
    "current_repo_identification": "D_roll_typed_spine_candidate_only",
    "decides_actual_operator": false,
    "required_fields": [
      "operator_source_primary_action_or_EL",
      "rolled_up_domain",
      "rolled_up_codomain",
      "chirality_domain_codomain",
      "signature_and_clifford_convention",
      "sigma_1_D_GU_0_1_sector",
      "coefficient_a_of_i_xi_psi",
      "coefficient_b_of_xi_tensor_u",
      "coefficient_lambda_d_of_Phi_d",
      "Phi_2_Phi_d_Phi_F_F_xi_order_split",
      "connection_Z_A_lower_order_ledger",
      "section_pullback_s_star_D_GU",
      "constraint_blocks_gamma_trace_K_mu_nu",
      "E_actual_source_P_Q_out_sigma_1_D_GU_I_Q_in",
      "Q_in_Q_out_projectors",
      "coordinate_convention_trace_or_embedded",
      "all_real_mixed_covectors",
      "extra_first_order_terms_absent_or_kernel_audited"
    ],
    "rolled_up_domain": "E_roll^epsilon=S^epsilon plus T^*Y tensor S^{-epsilon}",
    "rolled_up_codomain": "F_roll^epsilon=S^{-epsilon} plus T^*Y tensor S^epsilon",
    "E_actual_definition": "E_actual^epsilon(y,xi)=P_Q_out^epsilon sigma_1(D_GU^epsilon)(y,xi) I_Q_in^epsilon",
    "minimal_E_conditions": [
      "a_nonzero",
      "b_nonzero",
      "q_nonzero",
      "G_squared_equals_q_Id",
      "actual_projected_Q_block_has_no_extra_non_null_kernel"
    ],
    "schur_conditions": [
      "lambda_d_nonzero",
      "actual_R_sector_Schur_symbol_computed",
      "no_extra_first_order_R_Q_terms_with_non_null_kernel"
    ]
  },
  "phi_conventions": {
    "must_keep_separate": true,
    "Phi_2": {
      "order": 0,
      "role": "algebraic_shiab"
    },
    "Phi_d": {
      "order": 1,
      "definition": "Phi_2 o d_A",
      "role": "source_of_F_xi_principal_block"
    },
    "F_xi": {
      "order": 1,
      "definition": "sigma_1(Phi_d)(xi)",
      "role": "one_form_to_one_form_principal_symbol"
    },
    "Phi_F": {
      "order": 0,
      "definition": "Phi_2(F_A tensor -)",
      "role": "curvature_insertion_not_source_of_F_xi"
    }
  },
  "order_split": {
    "principal_order_one_terms": [
      "d_A_star_principal_i_xi",
      "d_A_principal_xi_tensor",
      "Phi_d_principal_F_xi"
    ],
    "lower_order_Z_A_terms": [
      "connection_coefficients",
      "spin_gimmel_connection",
      "possible_chirality_mixing_connection_coefficients",
      "mass_terms",
      "gauge_fixing_terms",
      "Phi_F_zero_order_curvature_insertion",
      "theta_IG_terms",
      "section_pullback_terms",
      "II_s_H_unless_effective_order_one_is_proved",
      "gamma_trace_constraint_sources"
    ]
  },
  "FC-VZ-1": {
    "status": "open_actual_operator_certificate_missing",
    "first_missing_proof_object": "ActualDGU01OperatorCertificate",
    "source_required": "E_actual_projected_from_sigma_1_D_GU",
    "visibility_required": true,
    "rollback_conditions": [
      "actual_D_GU_lacks_rolled_up_0_1_block",
      "coefficient_a_zero",
      "coefficient_b_zero",
      "actual_Q_sector_has_extra_first_order_component_with_non_null_kernel",
      "non_null_E_actual_kernel_found",
      "mixed_covectors_not_quantified",
      "trace_and_embedded_coordinate_conventions_mixed",
      "hidden_first_order_terms_placed_in_Z_A"
    ]
  },
  "FC-VZ-4": {
    "status": "open_actual_section_pulled_subprincipal_constraint_gate_missing",
    "first_missing_proof_object": "ActualDGUSectionSubprincipalCertificate",
    "required_object": "sigma_0_inv(S_Rs_4D_full)(x,eta)",
    "visibility_required": true,
    "required_terms": [
      "A_s_full",
      "B_s_full",
      "C_s_full",
      "E_s_full",
      "E_s_inverse_Schur_corrections",
      "II_s_H_equals_s_star_theta",
      "curved_horizontal_normal_frame_derivatives",
      "Phi_F_zero_order_curvature_insertion",
      "Z_A_lower_order_ledger",
      "spin_gimmel_connection",
      "mass_and_gauge_fixing_terms",
      "Poisson_and_invariant_subprincipal_corrections",
      "constraint_blocks_gamma_trace_K_mu_nu",
      "coupled_RS_constraint_characteristic_matrix"
    ],
    "rollback_conditions": [
      "spacelike_characteristic_found_for_actual_section_pulled_operator",
      "II_s_H_enters_effective_first_order_symbol",
      "K_mu_nu_constraint_source_changes_characteristic_cone",
      "gamma_trace_constraint_system_has_spacelike_characteristic",
      "standalone_GU_RS_Lagrangian_has_VZ_spacelike_roots"
    ]
  },
  "prior_files_establish": {
    "typed_spine_operator": "canonical_proposal_not_actual_operator_certificate",
    "typed_E_block_arithmetic": "conditional_formal_block_tested",
    "typed_schur_symbol": "conditional_on_actual_lambda_d_nonzero_and_actual_block",
    "subprincipal_contract": "names_actual_section_pulled_missing_object",
    "no_go_map": "conditional_14D_and_4D_principal_symbol_only"
  },
  "no_go_map_wording": {
    "status_cap": "conditional_14D_gated_on_FC_VZ_1_and_4D_principal_symbol_only",
    "must_keep_visible": [
      "FC-VZ-1_actual_operator_certificate_open",
      "FC-VZ-4_actual_subprincipal_constraint_gate_open",
      "actual_operator_status_typed_spine_candidate_only",
      "rollback_if_spacelike_characteristics_appear"
    ],
    "forbidden_until": [
      "actual_D_GU_0_1_operator_certificate_closed",
      "actual_E_block_all_non_null_covectors_closed",
      "actual_section_pulled_subprincipal_constraint_matrix_closed"
    ]
  },
  "forbidden_claims": [
    "actual_GU_RS_operator_identified_from_current_sources",
    "FC-VZ-1_closed_for_actual_D_GU",
    "FC-VZ-4_closed_for_actual_section_pulled_operator",
    "full_VZ_evasion_closed",
    "Phi_F_supplies_F_xi_principal_block"
  ],
  "next_meaningful_computation": [
    "extract_source_closed_actual_D_GU_0_1_operator_certificate",
    "project_E_actual_from_sigma_1_D_GU",
    "run_all_real_mixed_covector_Clifford_kernel_audit",
    "compute_actual_spin_three_halves_Schur_symbol",
    "compute_actual_section_pulled_sigma_0_inv_S_Rs_4D_full",
    "build_coupled_RS_constraint_characteristic_matrix"
  ]
}
```
