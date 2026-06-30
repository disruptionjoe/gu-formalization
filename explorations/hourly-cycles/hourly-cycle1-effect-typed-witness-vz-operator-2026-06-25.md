---
title: "Hourly Cycle 1 Effect-Typed Witness Transport VZ Operator"
date: 2026-06-25
status: exploration/hourly_cycle1_gate
doc_type: effect_typed_witness_vz_operator_contract
verdict: "BLOCKED_CONDITIONAL__EFFECT_TYPED_WITNESS_TRANSPORT_REDUCES_OBLIGATIONS_BUT_ACTUAL_DGU_01_OPERATOR_CERTIFICATE_MISSING"
owned_path: "explorations/hourly-cycle1-effect-typed-witness-vz-operator-2026-06-25.md"
companion_audit: "tests/hourly_cycle1_effect_typed_witness_vz_operator_audit.py"
depends_on:
  - "RESEARCH-POSTURE.md"
  - "process/runbooks/five-lane-frontier-run.md"
  - "explorations/hourly-cycle2-vz-actual-operator-certificate-gate-2026-06-24.md"
  - "explorations/hourly-cycle1-vz-subprincipal-characteristic-contract-2026-06-24.md"
  - "explorations/vz-proof-grade-closure-attempt-2026-06-24.md"
---

# Hourly Cycle 1 Effect-Typed Witness Transport VZ Operator

## 1. Verdict: blocked / conditional

An `EffectTypedWitnessTransport` interface can reduce the Velo-Zwanziger blocker to a
typed source/projection/finality/loss contract over the actual GU 0/1 operator, section
pullback, and subprincipal characteristic gate.

It cannot close the blocker. The first exact obstruction remains:

```text
ActualDGU01OperatorCertificate
```

The strongest decision is therefore:

```text
blocked / conditional

conditional positive result:
  If ActualDGU01OperatorCertificate supplies the source-closed actual D_GU^epsilon
  0/1 operator with the typed D_roll principal block, a != 0, b != 0,
  lambda_d != 0, all Q projectors, the Phi_d/Phi_F order split, and no unaudited
  harmful first-order loss terms, then EffectTypedWitnessTransport transports the
  existing typed-spine FC-VZ-1 algebra to the actual operator interface.

blocked part:
  Current repo sources still identify only a typed-spine candidate, not the actual
  source/action/Euler-Lagrange operator selected by GU. FC-VZ-4 also remains open until
  the same actual operator is pulled to a section and its invariant subprincipal
  coupled characteristic matrix is computed.
```

This artifact does not claim VZ closure, hyperbolicity, causality, or absence of
spacelike characteristics for the actual GU Rarita-Schwinger operator.

## 2. What was derived directly from repo sources

`RESEARCH-POSTURE.md` requires constructive attempts and exact rollback conditions. It
also forbids promoting compatibility into derivation. That rule is decisive here: a
transport interface may organize the missing data, but it does not create source
provenance for the actual operator.

`process/runbooks/five-lane-frontier-run.md` requires a decision-grade lane result with a
clear verdict, the strongest positive result, the first exact obstruction, and a next
object or computation.

`explorations/hourly-cycle2-vz-actual-operator-certificate-gate-2026-06-24.md` establishes
the upstream gate:

```text
ActualDGU01OperatorCertificate:
  missing source-closed certificate

current available operator:
  D_roll typed-spine candidate only

FC-VZ-1:
  open for the actual GU operator

FC-VZ-4:
  open for the actual section-pulled subprincipal and constraint system
```

It also specifies the certificate fields that must be sourced from the primary GU
operator/action/Euler-Lagrange derivation: rolled-up domain and codomain, chirality,
`sigma_1(D_GU^epsilon)`, coefficients `a`, `b`, `lambda_d`, the `Phi_2`/`Phi_d`/`Phi_F`
order split, Q projectors, lower-order `Z_A` ledger, section pullback, and constraint
blocks.

`explorations/hourly-cycle1-vz-subprincipal-characteristic-contract-2026-06-24.md`
establishes the downstream 4D gate:

```text
sigma_0_inv(S_Rs_4D_full)(x, eta)
```

must be computed from the actual section-pulled operator with `II_s^H = s*(theta)`,
curved horizontal/normal frame derivatives, `Z_A`, `Phi_F`, spin/gimmel connection,
mass/gauge-fixing terms, Poisson and invariant-subprincipal corrections, and the
`K_mu_nu` gamma-trace constraint source. The pass condition is a real characteristic
test for the actual coupled RS/constraint system, not a principal-symbol slogan.

`explorations/vz-proof-grade-closure-attempt-2026-06-24.md` establishes the strongest
available positive algebra. For the typed-spine principal block

```text
sigma_D(xi)(u, psi) = (i_xi psi, xi tensor u + lambda_d F_xi psi)
```

with nonzero typed coefficients, the Q-sector E-block and spin-3/2 Schur principal
symbol close conditionally over real non-null mixed 14D covectors. The same file also
states that if the actual operator has `lambda_d = 0`, the typed Schur route fails as a
VZ closure mechanism.

## 3. The strongest positive result

The strongest positive construction is a typed transport interface that treats the VZ
route as a witness movement problem rather than as an immediate closure claim.

```text
EffectTypedWitnessTransport

Input:
  source:
    ActualDGU01OperatorCertificate

  typed_model:
    D_roll typed-spine algebra already audited for the conditional FC-VZ-1 symbol

  projections:
    P_Q_in, P_Q_out
    spin-3/2 projector
    section pullback s*
    gamma-trace/constraint projection

  finality targets:
    FC-VZ-1 actual E-block non-null-kernel certificate
    FC-VZ-4 actual section-pulled coupled characteristic certificate

  loss ledger:
    terms that may be harmless transport/amplitude/lower-order data
    terms that may change the effective first-order symbol or constraints

Output:
  a typed witness chain saying exactly which conditional typed-spine facts may be
  transported to the actual GU operator, and exactly where transport must stop.
```

The interface has four typed stages.

```text
Stage S: Source witness
  source(D_GU^epsilon)
  proves the actual 0/1 operator and coefficients from GU source/action/EL data.

Stage P: Projection witness
  projects sigma_1(D_GU^epsilon) to Q-sector and spin-3/2 blocks:
    E_actual = P_Q_out sigma_1(D_GU^epsilon) I_Q_in
    S_R^epsilon = A_actual - B_actual E_actual^(-1) C_actual

Stage F: Finality witness
  proves the intended gate:
    FC-VZ-1 for all real non-null mixed 14D covectors
    FC-VZ-4 for the actual section-pulled coupled RS/constraint characteristic matrix

Stage L: Loss witness
  records every term not visible in the typed principal model:
    Phi_F zero-order insertion
    Z_A lower-order data
    II_s^H section geometry
    spin/gimmel connection
    mass and gauge-fixing terms
    Poisson and invariant-subprincipal corrections
    K_mu_nu gamma-trace constraint source
    any extra first-order Q/R coupling
```

This is stronger than another summary because it gives a pass/fail interface for the
missing proof object. If `ActualDGU01OperatorCertificate` exists and matches the typed
principal block with `lambda_d != 0`, the interface says how to replay the typed-spine
kernel proof against the actual operator. If the certificate is absent, or if it supplies
`lambda_d = 0`, or if extra first-order loss terms enter the Q-sector or section-pulled
constraint symbol with non-null kernel, the transport stops at the exact failed witness.

The positive result is not that GU has evaded VZ. The positive result is that the blocker
has been narrowed to a typed source/projection/finality/loss contract whose first input
is now unambiguous.

## 4. The first exact obstruction or missing proof object

The first obstruction in dependency order is still source provenance:

```text
ActualDGU01OperatorCertificate
```

The transport interface needs this certificate before it can bind any typed-spine witness
to the actual GU operator. The missing certificate must provide:

```text
operator_source:
  primary GU source/action/Euler-Lagrange derivation for D_GU^epsilon

operator_identity:
  proof that the actual 0/1-sector operator has the typed rolled-up domain/codomain
  and the displayed principal block

coefficients:
  a != 0
  b != 0
  lambda_d != 0

order_split:
  Phi_2 order 0
  Phi_d order 1 with F_xi = sigma_1(Phi_2 o d_A)(xi)
  Phi_F order 0 and not the source of F_xi

projection_data:
  P_Q_in, P_Q_out, spin-3/2 projector, chirality conventions,
  trace/embedded coordinate convention, and all-real mixed-covector quantification

loss_data:
  complete first-order and lower-order term ledger, including explicit proof that
  any extra first-order Q/R terms are absent or kernel-audited
```

Without this object, `EffectTypedWitnessTransport` cannot decide whether the typed
principal model is the actual GU model. It can only state a conditional functor-like
contract:

```text
typed witness over D_roll
  transports to actual witness over D_GU^epsilon
only after
  source(D_GU^epsilon) identifies D_roll as the actual 0/1 principal operator
  and loss(D_GU^epsilon) proves that no hidden first-order term changes the gate.
```

The second obstruction is downstream and remains FC-VZ-4:

```text
ActualSectionPulledSubprincipalCharacteristicCertificate
```

This object must compute the section-pulled invariant subprincipal Schur/constraint
matrix from the same actual operator. It cannot be replaced by the 14D typed principal
symbol.

## 5. The constructive next object that would remove or test the obstruction

The next constructive object should be a certificate with explicit machine-checkable
fields, not another prose reconciliation:

```text
ActualDGU01OperatorCertificate

Fields:
  certificate_id
  source_document_or_derivation
  actual_operator_formula
  rolled_up_domain
  rolled_up_codomain
  chirality_domain_codomain
  signature_and_clifford_convention
  trace_or_embedded_coordinate_convention
  sigma_1_D_GU_0_1_sector
  coefficient_a
  coefficient_b
  coefficient_lambda_d
  Phi_2_Phi_d_Phi_F_order_split
  Q_in_Q_out_projectors
  spin_3_2_projector
  E_actual = P_Q_out sigma_1(D_GU^epsilon) I_Q_in
  all_real_mixed_covector_domain
  extra_first_order_terms_absent_or_audited
  lower_order_Z_A_ledger
  section_pullback_rule
  constraint_blocks_gamma_trace_K_mu_nu
  rollback_conditions
```

Once that object exists, the immediate computation is:

```text
1. Project E_actual from sigma_1(D_GU^epsilon).
2. Run the all-real mixed-covector non-null kernel audit.
3. If that passes, form S_R^epsilon = A_actual - B_actual E_actual^(-1) C_actual.
4. Pull the same actual operator to a section.
5. Compute sigma_0_inv(S_Rs_4D_full)(x, eta) and the coupled RS/constraint
   characteristic matrix with all listed loss terms.
6. Pass FC-VZ-4 only if real characteristic roots are confined to the null cone.
```

This object would remove the first obstruction if it proves that the typed-spine
principal block is source-selected by GU. It would test the obstruction if it instead
finds `lambda_d = 0`, missing Q-sector coupling, a different principal block, or an extra
first-order loss term.

## 6. What this means for the relevant GU claim

The relevant GU claim should remain capped as:

```text
GU has a coherent conditional VZ route through Clifford-module non-decoupling,
provided the actual 0/1 operator certificate matches the typed-spine principal block
and the actual section-pulled subprincipal characteristic gate passes.
```

It should not be promoted to:

```text
the actual GU RS operator has been identified from current sources
FC-VZ-1 is closed for actual D_GU
FC-VZ-4 is closed for the actual section-pulled operator
full_VZ_evasion_closed
hyperbolicity_established
causality_established
absence_of_spacelike_characteristics_proved
Phi_F supplies the F_xi principal block
```

The transport interface improves the situation because it cleanly separates four claims:

```text
source:
  Is the displayed typed operator actually D_GU^epsilon?

projection:
  Does the actual operator project to the audited Q-sector and spin-3/2 blocks?

finality:
  Do FC-VZ-1 and FC-VZ-4 close over the actual operator domains?

loss:
  Do lower-order, section, and constraint terms stay harmless, or do they change the
  characteristic problem?
```

That separation is useful for Mission A: it gives a precise constructive object GU would
need if the route is correct, and it gives clean rollback conditions if the route fails.

## 7. Next meaningful proof or computation step

The next meaningful step is to build the source certificate and audit it, then only
afterward run the transport.

```text
Primary next step:
  Construct ActualDGU01OperatorCertificate from primary GU operator/action sources.

Immediate audit:
  Check that sigma_1(D_GU^epsilon) has the typed 0/1 principal block with
  a != 0, b != 0, lambda_d != 0, correct Q projectors, all-real mixed-covector
  quantification, and a complete loss ledger.

If the audit passes:
  Apply EffectTypedWitnessTransport to replay the typed-spine FC-VZ-1 proof against
  E_actual and then compute the actual section-pulled FC-VZ-4 characteristic matrix.

If the audit fails:
  Demote this typed VZ route at the exact failed field, especially if lambda_d = 0 or
  an extra first-order term introduces a non-null kernel.
```

## 8. Machine-readable JSON summary

```json
{
  "artifact": "hourly-cycle1-effect-typed-witness-vz-operator-2026-06-25",
  "verdict": "BLOCKED_CONDITIONAL__EFFECT_TYPED_WITNESS_TRANSPORT_REDUCES_OBLIGATIONS_BUT_ACTUAL_DGU_01_OPERATOR_CERTIFICATE_MISSING",
  "full_vz_evasion_claim": false,
  "hyperbolicity_claim": false,
  "causality_claim": false,
  "spacelike_characteristic_absence_claim": false,
  "effect_typed_witness_transport": {
    "status": "interface_specified_transport_blocked_on_actual_operator_certificate",
    "can_reduce_blocker_to_contract": true,
    "can_close_vz_without_actual_operator_certificate": false,
    "input_required_first": "ActualDGU01OperatorCertificate",
    "typed_model_available": "D_roll_typed_spine_candidate_only",
    "actual_operator_identified": false,
    "stages": [
      "source",
      "projection",
      "finality",
      "loss"
    ]
  },
  "source_contract": {
    "required_object": "ActualDGU01OperatorCertificate",
    "status": "missing_source_closed_certificate",
    "required_fields": [
      "operator_source_primary_action_or_EL",
      "actual_operator_formula",
      "rolled_up_domain",
      "rolled_up_codomain",
      "chirality_domain_codomain",
      "signature_and_clifford_convention",
      "trace_or_embedded_coordinate_convention",
      "sigma_1_D_GU_0_1_sector",
      "coefficient_a_nonzero",
      "coefficient_b_nonzero",
      "coefficient_lambda_d_nonzero",
      "Phi_2_Phi_d_Phi_F_order_split",
      "Q_in_Q_out_projectors",
      "spin_3_2_projector",
      "E_actual_definition",
      "all_real_mixed_covector_domain",
      "extra_first_order_terms_absent_or_audited",
      "lower_order_Z_A_ledger",
      "section_pullback_rule",
      "constraint_blocks_gamma_trace_K_mu_nu",
      "rollback_conditions"
    ],
    "E_actual_definition": "P_Q_out sigma_1(D_GU^epsilon) I_Q_in"
  },
  "projection_contract": {
    "status": "conditional_on_source_contract",
    "required_projectors": [
      "P_Q_in",
      "P_Q_out",
      "spin_3_2_projector",
      "section_pullback_s_star",
      "gamma_trace_constraint_projection"
    ],
    "required_blocks": [
      "A_actual",
      "B_actual",
      "C_actual",
      "E_actual",
      "S_R_epsilon_equals_A_actual_minus_B_actual_E_actual_inverse_C_actual"
    ],
    "all_real_mixed_covectors_required": true
  },
  "finality_contract": {
    "status": "conditional_not_closed",
    "FC-VZ-1": {
      "status": "open_actual_operator_certificate_missing",
      "pass_condition": "E_actual_has_no_non_null_kernel_for_all_real_mixed_14D_covectors",
      "first_missing_proof_object": "ActualDGU01OperatorCertificate"
    },
    "FC-VZ-4": {
      "status": "open_actual_section_pulled_subprincipal_characteristic_certificate_missing",
      "required_object": "ActualSectionPulledSubprincipalCharacteristicCertificate",
      "pass_condition": "actual_coupled_RS_constraint_characteristic_roots_confined_to_null_cone",
      "first_missing_proof_object": "sigma_0_inv_S_Rs_4D_full_from_actual_D_GU"
    }
  },
  "loss_contract": {
    "status": "required_not_computed_for_actual_operator",
    "terms_to_classify": [
      "Phi_F_zero_order_curvature_insertion",
      "Z_A_lower_order_ledger",
      "II_s_H_equals_s_star_theta",
      "curved_horizontal_normal_frame_derivatives",
      "spin_gimmel_connection_terms",
      "mass_and_gauge_fixing_terms",
      "Poisson_and_invariant_subprincipal_corrections",
      "constraint_blocks_gamma_trace_K_mu_nu",
      "extra_first_order_Q_or_R_terms"
    ],
    "harmless_only_if": "proved_transport_amplitude_or_constrained_source_not_effective_first_order_characteristic_change"
  },
  "strongest_positive_result": {
    "claim": "EffectTypedWitnessTransport gives a precise source_projection_finality_loss contract for transporting typed-spine FC-VZ-1 algebra to actual D_GU",
    "requires_actual_operator_certificate": true,
    "requires_lambda_d_nonzero": true,
    "requires_no_harmful_extra_first_order_loss_terms": true,
    "does_not_close_full_vz": true
  },
  "first_exact_obstruction": "ActualDGU01OperatorCertificate",
  "second_obstruction": "ActualSectionPulledSubprincipalCharacteristicCertificate",
  "constructive_next_object": "ActualDGU01OperatorCertificate_with_machine_checkable_source_projection_finality_loss_fields",
  "relevant_gu_claim_status": "coherent_conditional_route_only_not_actual_vz_closure",
  "forbidden_claims": [
    "actual_GU_RS_operator_identified_from_current_sources",
    "FC-VZ-1_closed_for_actual_D_GU",
    "FC-VZ-4_closed_for_actual_section_pulled_operator",
    "full_VZ_evasion_closed",
    "hyperbolicity_established",
    "causality_established",
    "absence_of_spacelike_characteristics_proved",
    "Phi_F_supplies_F_xi_principal_block"
  ],
  "rollback_conditions": [
    "ActualDGU01OperatorCertificate_missing",
    "actual_operator_differs_from_D_roll_typed_spine",
    "coefficient_a_zero",
    "coefficient_b_zero",
    "coefficient_lambda_d_zero",
    "Phi_d_not_present_as_order_one_source_of_F_xi",
    "Phi_F_used_as_F_xi_principal_block",
    "extra_first_order_Q_or_R_term_has_non_null_kernel",
    "non_null_E_actual_kernel_found",
    "spacelike_characteristic_found_for_actual_section_pulled_operator",
    "II_s_H_enters_effective_first_order_symbol",
    "K_mu_nu_constraint_source_changes_characteristic_cone",
    "gamma_trace_constraint_system_has_spacelike_characteristic"
  ],
  "next_meaningful_proof_or_computation": [
    "construct_ActualDGU01OperatorCertificate_from_primary_GU_action_or_EL_sources",
    "project_E_actual_from_sigma_1_D_GU",
    "run_all_real_mixed_covector_non_null_kernel_audit",
    "compute_actual_section_pulled_sigma_0_inv_S_Rs_4D_full",
    "build_actual_coupled_RS_constraint_characteristic_matrix",
    "classify_loss_terms_as_harmless_or_characteristic_changing"
  ]
}
```
