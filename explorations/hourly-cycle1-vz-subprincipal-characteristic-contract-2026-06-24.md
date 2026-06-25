---
title: "Hourly Cycle 1 VZ Subprincipal Characteristic Contract"
date: 2026-06-24
status: exploration/hourly_cycle1_gate
doc_type: vz_subprincipal_characteristic_contract
verdict: "UNDERDEFINED_CONDITIONAL__ACTUAL_OPERATOR_AND_FC_VZ_4_NOT_COMPUTABLE_YET"
owned_path: "explorations/hourly-cycle1-vz-subprincipal-characteristic-contract-2026-06-24.md"
companion_audit: "tests/hourly_cycle1_vz_subprincipal_characteristic_contract_audit.py"
depends_on:
  - "RESEARCH-POSTURE.md"
  - "process/runbooks/five-lane-frontier-run.md"
  - "roadmap/objection-triage-register.md"
  - "explorations/cycle1-vz-subprincipal-eblock-proof-gate-2026-06-24.md"
  - "explorations/cycle2-vz-actual-operator-e-block-certificate-2026-06-24.md"
  - "explorations/vz-proof-grade-closure-attempt-2026-06-24.md"
  - "explorations/vz-e-block-independent-rederivation-2026-06-24.md"
  - "canon/no-go-class-relative-map.md"
---

# Hourly Cycle 1 VZ Subprincipal Characteristic Contract

## 1. Verdict

The current repo data cannot yet compute spacelike-characteristic absence for the actual
GU Rarita-Schwinger operator.

The gate remains:

```text
FC-VZ-1: open for the actual GU operator
FC-VZ-4: underdefined / open for the actual section-pulled subprincipal problem
full VZ evasion: not claimed
```

This is not a negative result against GU. It is a contract boundary. The typed-spine
principal-symbol model gives a coherent conditional construction, and its Q-sector
E-block arithmetic is strong once the displayed operator is granted. But the repo still
lacks the actual operator certificate and the actual 4D section-pulled subprincipal
Schur symbol with extrinsic-curvature terms.

The exact first obstruction is:

```text
source-closed actual D_GU^epsilon 0/1-sector operator certificate
```

The exact first FC-VZ-4 obstruction, downstream of that certificate, is:

```text
sigma_0_inv(S_Rs_4D_full)(x, eta)
with II_s^H = s*(theta), Z_A, Poisson/invariant-subprincipal corrections,
and the gamma-trace constraint source K_mu_nu included.
```

Until those objects exist, the repo cannot decide whether the actual GU RS dynamics has
no spacelike characteristics. It can only state the conditional typed-spine route and the
rollback tests below.

## 2. What Prior VZ Files Establish

The required context establishes a useful but conditional stack.

`RESEARCH-POSTURE.md` and the five-lane runbook require explicit assumptions,
falsification conditions, and no promotion from compatibility to derivation. That rule is
load-bearing here: the typed VZ mechanism may be the right GU route, but it must earn its
operator provenance.

`roadmap/objection-triage-register.md` records OBJ-VZ as a live objection: the principal
symbol result may be overturned by subprincipal/extrinsic-curvature order, and the 14D
leg is gated on FC-VZ-1.

`explorations/cycle1-vz-subprincipal-eblock-proof-gate-2026-06-24.md` correctly refuses
full VZ closure. It separates the conditional typed principal result from FC-VZ-1 and
FC-VZ-4, and names the missing section-pulled subprincipal Schur object.

`explorations/cycle2-vz-actual-operator-e-block-certificate-2026-06-24.md` sharpens the
FC-VZ-1 definition:

```text
E_actual^epsilon(y, xi)
  = P_Q_out^epsilon sigma_1(D_GU^epsilon)(y, xi) I_Q_in^epsilon.
```

It also clarifies that formal E-block inverse arithmetic is not the same as extracting
`E_actual` from the actual GU operator.

`explorations/vz-proof-grade-closure-attempt-2026-06-24.md` gives the strongest positive
typed-spine theorem. If the actual 0/1 principal block is

```text
sigma_1(D_roll)(xi)(u, psi) = (i_xi psi, xi tensor u + F_xi psi)
```

with `F_xi = sigma_1(Phi_2 o d_A)(xi)` and `lambda_d != 0`, then the typed 14D
spin-3/2 Schur principal symbol has no non-null kernel. This is conditional on the
typed spine being the actual operator.

`explorations/vz-e-block-independent-rederivation-2026-06-24.md` rederives the
`1/14`, `13/7`, and `13/98` coefficients from the gamma-trace projector and gives a
determinant-free E-kernel proof. It also refuses an FC-VZ-1 upgrade because the canonical
actual operator is still missing.

`canon/no-go-class-relative-map.md` currently says the VZ row is conditional:
14D is gated on FC-VZ-1, and 4D is only principal-symbol level with FC-VZ-4 still open.
That wording should remain in force.

## 3. Strongest Positive Construction Attempt

The best positive construction is to make the typed-spine proposal into the actual
operator and then compute the actual section-pulled subprincipal object.

The typed-spine candidate is:

```text
D_roll^epsilon(u, psi)
  =
  (d_A^* psi, d_A u + lambda_d Phi_2(d_A psi))
  + Z_A^epsilon(u, psi).
```

The order split must stay explicit:

```text
Phi_2                      zero-order algebraic shiab
Phi_d := Phi_2 o d_A       first-order differential composite
Phi_F := Phi_2(F_A tensor -)  zero-order curvature insertion
F_xi := sigma_1(Phi_d)(xi) principal-symbol block
Z_A                        all lower-order terms
```

If the actual operator has coefficients `a != 0` for `d_A^* psi` and `b != 0` for
`d_A u`, the Q-sector E-block has the direct non-null kernel proof:

```text
q = g_Y^{-1}(xi, xi) != 0
G = gamma(xi)
G^2 = q Id
E_actual(phi, s) = 0
top row gives G s = 0, hence s = 0
bottom row gives G phi = 0, hence phi = 0
```

If the actual operator also has `lambda_d != 0` in the one-form-to-one-form `Phi_d`
block, the typed Schur route gives a non-null-kernel-free 14D spin-3/2 principal symbol.

For FC-VZ-4, the strongest possible continuation is to pull the actual operator to a
section and form the full effective RS Schur operator:

```text
S_Rs_4D_full
  =
  A_s_full - B_s_full (E_s_full)^(-1) C_s_full.
```

The subprincipal characteristic contract must then compute:

```text
sigma_0_inv(S_Rs_4D_full)(x, eta)
```

including:

```text
A_s^(0), B_s^(0), C_s^(0), E_s^(0)
E_s^(1)^(-1) Schur corrections
Poisson bracket and invariant-subprincipal corrections
II_s^H = s*(theta)
curved horizontal/normal frame derivatives
Phi_F, spin/gimmel connection, mass, gauge-fixing, and other Z_A terms
gamma-trace constraint source K_mu_nu
```

The positive pass condition is not that every zero-order term vanishes. The pass
condition is:

```text
the actual section-pulled characteristic polynomial has no real non-null roots,
and all II_s^H / K_mu_nu terms enter only as transport, amplitude, or constrained-source
terms that do not change the characteristic cone.
```

## 4. First Exact Obstruction Or Missing Proof Object

The first obstruction in dependency order is the actual operator certificate:

```text
ACTUAL-OPERATOR certificate:
  D_GU^epsilon has the relevant 0/1 principal block,
  its coefficients a, b, lambda_d are fixed,
  Phi_2, Phi_d, Phi_F, and F_xi are separated,
  chirality domains and Q-sector projectors are fixed,
  and every lower-order term is assigned to Z_A with its order recorded.
```

Without this object, FC-VZ-1 is a theorem about the typed-spine model, not about the
actual GU operator. Without FC-VZ-1, the 14D Schur complement and the later 4D Schur
calculation are not proof objects for the actual route.

The first exact FC-VZ-4 proof object is:

```text
ACTUAL-SUBPRINCIPAL certificate:
  sigma_0_inv(S_Rs_4D_full)(x, eta)
```

computed from the same actual `D_GU^epsilon` and not from a free schematic Dirac-type
operator.

The first missing term to audit inside that object is:

```text
II_s^H = s*(theta) and its curved horizontal/normal frame derivative contribution,
including the K_mu_nu source in the gamma-trace constraint system.
```

That is the first term because the existing 14D subprincipal note argues generally that
zero-order terms do not change characteristics, but FC-VZ-4 is specifically about whether
section curvature or constraint propagation turns such data into an effective first-order
spacelike characteristic after pullback and Schur reduction.

## 5. What Would Falsify Or Demote The VZ Evasion Route

FC-VZ-1 is falsified or demoted if any of the following occurs:

```text
actual D_GU lacks Phi_d in the relevant 0/1 principal block
coefficient a of d_A^* psi is zero
coefficient b of d_A u is zero
actual Q-sector is not S plus Im(j), or has extra principal components with non-null kernel
there exists real xi with g_Y^{-1}(xi,xi) != 0 and ker E_actual^epsilon(y,xi) != 0
the proof covers only sample or pure covectors and misses mixed horizontal/vertical covectors
```

FC-VZ-4 is falsified or demoted if any of the following occurs:

```text
there exists real eta with g_s^{-1}(eta,eta) != 0 and
  ker sigma_1(S_Rs_4D_full)(x,eta) != 0 for the actual section-pulled operator

the actual characteristic matrix for the coupled RS/gamma-trace system has a real non-null
  root after II_s^H or K_mu_nu is included

II_s^H, a curved frame derivative, or a constraint-propagation term enters the effective
  order-one symbol rather than the order-zero transport ledger

the sourced symmetric-hyperbolic estimate for phi = Gamma^4D Psi fails in a way that
  produces a spacelike characteristic for the constraint subsystem

a standalone 4D GU RS Lagrangian is derived whose VZ characteristic matrix has
  spacelike roots
```

The exact falsification condition for the characteristic gate is therefore:

```text
exists (x, eta) with eta != 0 and g_s^{-1}(eta,eta) != 0 such that the actual
section-pulled RS characteristic matrix, including II_s^H and constraint blocks,
has nontrivial kernel.
```

## 6. Impact For No-Go-Class-Relative Map Wording

The no-go map should not be strengthened on the basis of the current repo data.

Recommended wording cap:

```text
VZ remains conditional at 14D, gated on actual-operator FC-VZ-1.
The 4D leg remains principal-symbol level only.
FC-VZ-4 is underdefined/open until the actual section-pulled subprincipal and
extrinsic-curvature characteristic matrix is computed.
The rollback condition is a non-null kernel or spacelike characteristic in that actual
matrix after II_s^H / K_mu_nu terms are included.
```

The map can continue to say that GU has a coherent conditional evasion route via
Clifford-module non-decoupling. It should not say the actual GU RS operator has been
shown free of spacelike characteristics until FC-VZ-1 and FC-VZ-4 both close against the
actual operator.

## 7. Next Meaningful Computation

The next computation should be an extraction and characteristic audit, not another
summary.

1. Write the source-closed actual-operator certificate for `D_GU^epsilon` on the 0/1
   sector. It must output `sigma_1(D_GU^epsilon)`, coefficients `a`, `b`, `lambda_d`,
   chirality domains, Q-sector projectors, and a complete `Z_A` lower-order ledger.
2. Extract `E_actual^epsilon = P_Q_out sigma_1(D_GU^epsilon) I_Q_in` and run a symbolic
   non-null kernel proof over all real mixed 14D covectors.
3. Pull the same operator to a section and compute
   `S_Rs_4D_full = A_s - B_s E_s^(-1) C_s`.
4. Compute `sigma_0_inv(S_Rs_4D_full)` with `II_s^H`, curved frame splitting,
   `Phi_F`, spin/gimmel connection, mass/gauge-fixing terms, Poisson corrections, and
   the `K_mu_nu` gamma-trace source.
5. Form the actual coupled characteristic matrix for the RS and constraint subsystem.
   Pass only if its real characteristic roots are confined to the null cone.

## 8. Machine-Readable JSON Summary

```json
{
  "artifact": "hourly-cycle1-vz-subprincipal-characteristic-contract-2026-06-24",
  "verdict": "UNDERDEFINED_CONDITIONAL__ACTUAL_OPERATOR_AND_FC_VZ_4_NOT_COMPUTABLE_YET",
  "full_vz_evasion_claim": false,
  "spacelike_characteristic_absence_computable_now": false,
  "gates": {
    "FC-VZ-1": {
      "name": "actual GU E-block invertibility on the non-null 14D cone",
      "status": "open_actual_operator_certificate_missing",
      "load_bearing_dependency": "E_actual^epsilon=P_Q_out sigma_1(D_GU^epsilon) I_Q_in",
      "first_missing_proof_object": "source_closed_actual_D_GU_0_1_operator_certificate",
      "rollback_conditions": [
        "actual_D_GU_lacks_Phi_d",
        "coefficient_a_of_d_A_star_psi_zero",
        "coefficient_b_of_d_A_u_zero",
        "actual_Q_sector_has_extra_principal_component_with_non_null_kernel",
        "non_null_E_actual_kernel_found",
        "mixed_horizontal_vertical_covectors_not_quantified"
      ]
    },
    "FC-VZ-4": {
      "name": "subprincipal/extrinsic-curvature spacelike-characteristic gate",
      "status": "underdefined_actual_section_pulled_operator_missing",
      "load_bearing_dependency": "sigma_0_inv(S_Rs_4D_full) from actual D_GU",
      "first_missing_proof_object": "actual_section_pulled_subprincipal_Schur_characteristic_matrix",
      "rollback_conditions": [
        "spacelike_characteristic_found_for_actual_section_pulled_operator",
        "II_s_H_enters_effective_first_order_symbol",
        "K_mu_nu_constraint_source_changes_characteristic_cone",
        "gamma_trace_constraint_system_has_spacelike_characteristic",
        "standalone_GU_RS_Lagrangian_has_VZ_characteristics"
      ]
    }
  },
  "actual_operator": {
    "status": "missing_source_closed_certificate",
    "first_missing_operator": "D_GU^epsilon 0/1-sector principal block plus Z_A lower-order ledger",
    "required_fields": [
      "sigma_1_D_GU_0_1_sector",
      "coefficient_a_of_d_A_star_psi",
      "coefficient_b_of_d_A_u",
      "coefficient_lambda_d_of_Phi_d",
      "Phi_2_Phi_d_Phi_F_F_xi_order_separation",
      "chirality_domains",
      "Q_sector_projectors",
      "coordinate_convention_trace_or_embedded",
      "Z_A_lower_order_ledger",
      "all_real_mixed_horizontal_vertical_covectors"
    ],
    "rollback_conditions": [
      "actual_D_GU_lacks_Phi_d",
      "a_times_b_equals_zero",
      "lambda_d_zero_demotes_spin_three_halves_Schur_route",
      "non_null_E_actual_kernel_found"
    ]
  },
  "subprincipal": {
    "status": "missing_actual_section_pulled_invariant_subprincipal_symbol",
    "required_object": "sigma_0_inv(S_Rs_4D_full)(x,eta)",
    "required_terms": [
      "A_s_0",
      "B_s_0",
      "C_s_0",
      "E_s_0",
      "E_s_1_inverse_Schur_corrections",
      "Poisson_bracket_corrections",
      "invariant_subprincipal_correction",
      "Phi_F_zero_order_curvature_insertion",
      "spin_gimmel_connection_terms",
      "mass_gauge_fixing_and_Z_A_terms",
      "gamma_trace_constraint_source_K_mu_nu"
    ],
    "pass_condition": "actual_coupled_characteristic_roots_confined_to_null_cone",
    "rollback_conditions": [
      "spacelike_characteristic_found_for_actual_section_pulled_operator",
      "subprincipal_reduction_changes_effective_order_one_symbol",
      "gamma_trace_constraint_system_has_spacelike_characteristic"
    ]
  },
  "extrinsic_curvature": {
    "status": "not_computed_for_actual_operator",
    "first_missing_term": "II_s_H_equals_s_star_theta_with_curved_horizontal_normal_frame_derivatives",
    "required_terms": [
      "II_s_H_equals_s_star_theta",
      "curved_horizontal_normal_frame_derivatives",
      "K_mu_nu_constraint_source",
      "Codazzi_section_pullback_terms"
    ],
    "rollback_conditions_if_spacelike_characteristics_appear": [
      "II_s_H_enters_effective_first_order_symbol",
      "K_mu_nu_constraint_source_changes_characteristic_cone",
      "spacelike_characteristic_found_for_actual_section_pulled_operator"
    ]
  },
  "first_exact_obstruction": "source_closed_actual_D_GU_0_1_operator_certificate_missing",
  "first_missing_term": "II_s_H_and_K_mu_nu_in_actual_section_pulled_subprincipal_characteristic_matrix",
  "exact_falsification_condition": "exists real spacelike or other non-null eta with eta != 0 and g_s_inverse_eta_eta != 0 such that the actual section-pulled RS characteristic matrix including II_s_H and constraint blocks has nontrivial kernel",
  "no_go_map_wording": {
    "status_cap": "conditional_14D_and_4D_principal_symbol_only",
    "must_keep_visible": [
      "FC-VZ-1_actual_operator_E_block_open",
      "FC-VZ-4_actual_subprincipal_extrinsic_curvature_gate_open",
      "rollback_if_spacelike_characteristics_appear"
    ],
    "forbidden_upgrade_until": [
      "FC-VZ-1_closed_for_actual_D_GU",
      "FC-VZ-4_closed_for_actual_section_pulled_operator"
    ]
  },
  "next_meaningful_computation": [
    "source_closed_actual_D_GU_0_1_operator_certificate",
    "E_actual_extraction_and_non_null_kernel_audit",
    "actual_section_pulled_S_Rs_4D_full_construction",
    "sigma_0_inv_S_Rs_4D_full_with_II_s_H_Z_A_Poisson_and_K_mu_nu",
    "coupled_RS_constraint_characteristic_matrix_non_null_kernel_test"
  ]
}
```
