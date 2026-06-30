---
title: "Hourly Cycle 2 Actual DGU Operator Certificate Schema"
date: "2026-06-25"
cycle: "2-of-3"
run: "3-1-5-4"
doc_type: actual_dgu_operator_certificate_schema
verdict: "UNDERDEFINED_BLOCKED__SCHEMA_SPECIFIED_BUT_SOURCE_CLOSED_ACTUAL_DGU_01_OPERATOR_MISSING"
owned_path: "explorations/hourly-cycle2-actual-dgu-operator-certificate-schema-2026-06-25.md"
companion_audit: "tests/hourly_cycle2_actual_dgu_operator_certificate_schema_audit.py"
---

# Hourly Cycle 2 Actual DGU Operator Certificate Schema

## 1. Verdict

Verdict: **underdefined / blocked**.

This artifact gives the promised machine-checkable schema for
`ActualDGU01OperatorCertificate`. The schema is decision-grade: it separates
source, projection, finality, and loss fields; it specifies accept/fail outcomes;
and it names exact rollback conditions for the actual GU 0/1 operator gate.

The strongest positive construction is conditional:

```text
If a primary GU action/operator/Euler-Lagrange derivation supplies a source-closed
D_GU^epsilon whose 0/1 principal symbol equals the typed spine on the stated
domain, with a != 0, b != 0, lambda_d != 0, and with all additional first-order
terms either absent or included in a fresh kernel/characteristic audit, then the
typed FC-VZ-1 E-block proof can be replayed against E_actual.
```

That construction cannot yet be instantiated from the current sources read here.
The first exact obstruction remains the missing source-closed certificate:

```text
ActualDGU01OperatorCertificate.source.operator_source_primary_action_or_EL
```

This artifact does **not** claim actual GU Rarita-Schwinger operator
identification, FC-VZ-1 closure for actual `D_GU`, FC-VZ-4 closure, VZ evasion,
hyperbolicity, causality, or absence of spacelike characteristics.

## 2. What Was Derived Directly From Repo Sources

`RESEARCH-POSTURE.md` requires explicit assumptions, falsification or rollback
conditions, dependency tracking, and promotion criteria. It also requires a
constructive obstruction response: state what object would remove the block and
what computation distinguishes construction from rescue.

`process/runbooks/five-lane-frontier-run.md` requires an owned decision-grade
artifact, not a summary-only note. It also fixes the allowed verdict vocabulary
and warns not to promote "compatible with" to "derived from" or "hosted by" to
"selected by".

`explorations/hourly-cycle1-effect-typed-witness-vz-operator-2026-06-25.md`
promises a machine-checkable `ActualDGU01OperatorCertificate` with fields for
source, operator formula, domains/codomains, chirality, Clifford conventions,
the 0/1 principal symbol, coefficients `a`, `b`, `lambda_d`, order splitting,
projectors, `E_actual`, all-real mixed covector quantification, loss terms,
section pullback, constraints, and rollback conditions. It also fixes the first
obstruction as source provenance.

`explorations/hourly-cycle2-vz-actual-operator-certificate-gate-2026-06-24.md`
adds concrete field content: the certificate must start from the actual GU
operator/action/Euler-Lagrange source, not from the displayed VZ matrix. It fixes
the rolled-up domain/codomain, base and cone data, Clifford relation
`G^2 = q Id`, Q-sector projectors, the definition
`E_actual = P_Q_out sigma_1(D_GU^epsilon) I_Q_in`, the `Phi_d`/`Phi_F` order
split, section-pullback payload, constraint blocks, and rollback cases.

`explorations/vz-proof-grade-closure-attempt-2026-06-24.md` supplies the typed
spine result only under typed assumptions: the Q-sector E-block is invertible for
all real non-null 14D covectors and the spin-3/2 Schur route needs
`lambda_d != 0`. It also states the sharp operator-gate failure: if
`lambda_d = 0`, the typed spin-3/2 Schur symbol route fails even if the Q-sector
E-block survives.

## 3. Strongest Positive Construction Attempt

The schema below is the strongest positive construction available from the
current repo sources. It is a certificate type plus a blocked current instance.
The type is usable by later proofs and by audits; the current instance records
why the gate does not yet pass.

### Certificate Type

```text
ActualDGU01OperatorCertificate

schema_version:
  ACTUAL_DGU_01_OPERATOR_CERTIFICATE_SCHEMA_V1

certificate_id:
  ActualDGU01OperatorCertificate

decision:
  one of:
    ACCEPT_ACTUAL_OPERATOR_CERTIFICATE
    FAIL_SOURCE_PROVENANCE
    FAIL_OPERATOR_DIFFERENCE
    FAIL_DOMAIN_CODOMAIN
    FAIL_CONVENTION_MIX
    FAIL_COEFFICIENT_ZERO
    FAIL_PROJECTOR_DATA
    FAIL_E_KERNEL
    FAIL_LOSS_LEDGER
    FAIL_SECTION_PULLBACK_PAYLOAD
    FAIL_CONSTRAINT_PAYLOAD
    BLOCKED_MISSING_SOURCE_OBJECT

source:
  operator_source_primary_action_or_EL:
    required: true
    accept_if: primary GU action/operator/Euler-Lagrange derivation identifies
      D_GU^epsilon before using typed VZ output
    fail_if: absent, only typed-spine proposal, only compatibility argument,
      or only displayed VZ matrix

  actual_operator_formula:
    required: true
    accept_if: complete 0/1-sector formula for D_GU^epsilon is stated with
      normalization and epsilon/chirality conventions
    fail_if: D_roll is assumed, imported, or normalized after target fitting

  rolled_up_domain:
    required_value: E_roll^epsilon = S^epsilon plus (T^*Y tensor S^-epsilon)

  rolled_up_codomain:
    required_value: F_roll^epsilon = S^-epsilon plus (T^*Y tensor S^epsilon)

  base_and_cone:
    required_values:
      Y: Met_Lor(X)
      dim_Y: 14
      signature_g_Y: (9,5)
      covectors: all real mixed horizontal/vertical covectors xi
      q: g_Y^{-1}(xi, xi)
      non_null_condition: q != 0

  signature_and_clifford_convention:
    required_values:
      G: gamma(xi)
      relation: G^2 = q Id

  chirality_domain_codomain:
    required: true
    accept_if: Gamma_-epsilon, j_epsilon, Q_in^epsilon, Q_out^epsilon,
      I_Q_in^epsilon, and P_Q_out^epsilon are fixed with one normalization
    fail_if: chirality is inferred only after the E-block proof

  coordinate_convention:
    required: true
    allowed_values:
      - trace_coordinate_matrix
      - embedded_coordinate_matrix
    fail_if: trace and embedded coordinate conventions are mixed in one proof

  sigma_1_D_GU_0_1_sector:
    required: true
    accept_if: principal symbol is computed from actual D_GU^epsilon
    fail_if: copied from typed spine without source derivation

  coefficients:
    coefficient_a:
      source: coefficient of i_xi psi in scalar output
      accept_if: source-derived and nonzero
      fail_if: a = 0 or not source-derived
    coefficient_b:
      source: coefficient of xi tensor u in one-form output
      accept_if: source-derived and nonzero
      fail_if: b = 0 or not source-derived
    coefficient_lambda_d:
      source: coefficient of Phi_d := Phi_2 o d_A in one-form output
      accept_if: source-derived and nonzero
      fail_if: lambda_d = 0 or not source-derived

projection:
  Q_in_Q_out_projectors:
    required: true
    definitions:
      Q_in^epsilon: S^epsilon plus Im(j_epsilon)
      Q_out^epsilon: S^-epsilon plus Im(j_-epsilon)
    accept_if: inclusions/projections are explicit and normalized
    fail_if: projectors are only named or convention-dependent

  spin_3_2_projector:
    required: true
    accept_if: R-sector projector is explicit and compatible with Q/R split
    fail_if: spin-3/2 Schur route uses an implicit projector

  E_actual_definition:
    required_value: E_actual^epsilon(y, xi) =
      P_Q_out^epsilon sigma_1(D_GU^epsilon)(y, xi) I_Q_in^epsilon

  Schur_blocks:
    required:
      - A_actual
      - B_actual
      - C_actual
      - E_actual
      - S_R^epsilon = A_actual - B_actual E_actual^{-1} C_actual
    fail_if: blocks are typed-spine-only or not projected from actual D_GU

  all_real_mixed_covector_domain:
    required: true
    accept_if: kernel audit quantifies over every real mixed 14D covector with q != 0
    fail_if: audit checks only pure horizontal or pure vertical covectors

finality:
  FC-VZ-1:
    status_before_certificate: open
    accept_if:
      - source accepted
      - projection accepted
      - a != 0
      - b != 0
      - lambda_d != 0 for the spin-3/2 Schur route
      - E_actual has no non-null kernel for every real mixed 14D covector
      - extra first-order Q/R terms are absent or included in the same proof
    fail_if:
      - source fails
      - E_actual has nontrivial kernel at some real q != 0 covector
      - lambda_d = 0 for the Schur route
      - Phi_F is substituted for Phi_d as the source of F_xi

  FC-VZ-4:
    status_before_certificate: open
    required_follow_on_object: ActualSectionPulledSubprincipalCharacteristicCertificate
    accept_if:
      - actual section-pulled coupled RS/constraint characteristic roots are
        confined to the null cone
      - sigma_0_inv(S_Rs_4D_full)(x, eta) includes all listed lower-order and
        constraint-source payloads
    fail_if:
      - a spacelike characteristic exists for the actual section-pulled operator
      - K_mu_nu or gamma-trace constraints change the characteristic cone

loss:
  order_split:
    Phi_2: zero-order algebraic shiab
    Phi_d: first-order differential composite Phi_2 o d_A
    F_xi: sigma_1(Phi_d)(xi), the principal-symbol one-form block
    Phi_F: zero-order curvature insertion Phi_2(F_A tensor -)
    Z_A: lower-order ledger unless a reduction proves effective order one

  extra_order_one_terms:
    required: complete list of every additional 0/1 first-order term projected
      to Q and R sectors
    accept_if: each term is proved absent or included in a new kernel proof
    fail_if: hidden first-order terms are placed in Z_A without audit

  section_pullback_rule:
    required: s^*D_GU^epsilon and induced 4D domain/codomain after horizontal
      and normal split
    fail_if: II_s^H, curved frame splitting, theta, or Codazzi-type terms enter
      the effective first-order symbol without characteristic audit

  constraint_blocks:
    required:
      - gamma-trace constraint subsystem
      - Q/R Schur blocks
      - K_mu_nu source ledger
    fail_if: constraint source changes characteristic cone or is omitted

rollback_conditions:
  - ActualDGU01OperatorCertificate_missing
  - operator_source_primary_action_or_EL_missing
  - actual_operator_differs_from_D_roll_typed_spine
  - actual_D_GU_0_1_block_absent
  - rolled_up_domain_or_codomain_mismatch
  - trace_coordinate_and_embedded_coordinate_conventions_mixed
  - coefficient_a_zero
  - coefficient_b_zero
  - coefficient_lambda_d_zero
  - Phi_d_not_present_as_order_one_source_of_F_xi
  - Phi_F_used_as_F_xi_principal_block
  - Q_in_Q_out_projectors_missing_or_unnormalized
  - proof_checks_only_pure_horizontal_or_pure_vertical_covectors
  - hidden_first_order_terms_placed_in_Z_A_without_projection_or_kernel_audit
  - extra_first_order_Q_or_R_term_has_non_null_kernel
  - non_null_E_actual_kernel_found
  - actual_R_sector_Schur_block_differs_and_has_non_null_kernel
  - section_pullback_payload_missing
  - II_s_H_enters_effective_first_order_symbol
  - K_mu_nu_constraint_source_changes_characteristic_cone
  - gamma_trace_constraint_system_has_spacelike_characteristic
  - spacelike_characteristic_found_for_actual_section_pulled_operator
  - standalone_GU_RS_Lagrangian_has_VZ_spacelike_roots
```

### Current Blocked Instance

```text
certificate_id: ActualDGU01OperatorCertificate
schema_version: ACTUAL_DGU_01_OPERATOR_CERTIFICATE_SCHEMA_V1
decision: BLOCKED_MISSING_SOURCE_OBJECT

source.operator_source_primary_action_or_EL:
  status: missing_from_sources_read

source.actual_operator_formula:
  status: not_instantiated
  reason: typed-spine candidate exists, but source-selected actual D_GU^epsilon
    has not been derived from primary GU action/operator/EL data here

projection.E_actual_definition:
  status: schema_defined_not_instantiated

finality.FC-VZ-1:
  status: open_actual_operator_certificate_missing

finality.FC-VZ-4:
  status: open_actual_section_pulled_subprincipal_characteristic_certificate_missing

loss:
  status: required_not_computed_for_actual_operator
```

This is the strongest positive construction because it preserves every typed
result that could be transported while refusing to identify the actual operator
without source provenance.

## 4. First Exact Obstruction Or Missing Proof Object

The first obstruction is not determinant algebra, another random matrix check,
or a restatement of the typed spine. It is the source-provenance field:

```text
ActualDGU01OperatorCertificate.source.operator_source_primary_action_or_EL
```

The missing proof object must cite or derive the primary GU action/operator and
prove that its 0/1 sector contains the actual first-order block

```text
d_A u + lambda_d Phi_2(d_A psi)
```

with `lambda_d != 0`, under the same chirality, Clifford, Q/R, and coordinate
conventions used by the E-block and Schur proofs.

If the primary source instead gives `lambda_d = 0`, the typed spin-3/2 Schur
route fails at the exact field `source.coefficients.coefficient_lambda_d`. If the
primary source gives a different first-order Q/R block, the certificate fails at
`projection.Schur_blocks` or `loss.extra_order_one_terms` until a new kernel
proof is supplied.

## 5. Constructive Next Object

The next object is not a prose reconciliation. It is a filled certificate:

```text
ActualDGU01OperatorCertificateInstance_V1
```

Minimum contents:

1. A primary GU action/operator/Euler-Lagrange citation or derivation for
   `D_GU^epsilon`.
2. The actual 0/1 principal symbol `sigma_1(D_GU^epsilon)` on
   `E_roll^epsilon -> F_roll^epsilon`.
3. Fixed chirality, Clifford, Q/R, and coordinate conventions.
4. Source-derived coefficients `a`, `b`, and `lambda_d`.
5. Explicit `P_Q_out sigma_1(D_GU^epsilon) I_Q_in`.
6. A kernel audit over every real mixed 14D covector with `q != 0`.
7. A complete first-order loss ledger, including Q/R extra terms.
8. Section-pullback and constraint payloads sufficient to start the FC-VZ-4
   characteristic certificate.

## 6. Impact On GU Claim

The GU claim status is unchanged but sharper:

```text
actual_operator: not source-closed
FC-VZ-1 for actual D_GU: open
FC-VZ-4 for actual section-pulled operator: open
VZ evasion: not claimed
hyperbolicity: not claimed
causality: not claimed
absence of spacelike characteristics: not claimed
```

The positive impact is that the route now has a machine-checkable admission
gate. A future worker can either fill the certificate and replay the typed
FC-VZ-1 proof, or fail the route at a named field without ambiguity.

## 7. Next Meaningful Proof Or Computation Step

Build `ActualDGU01OperatorCertificateInstance_V1` from the primary GU operator
source. The first computation after source extraction is:

```text
1. Compute sigma_1(D_GU^epsilon) on the rolled-up 0/1 sector.
2. Project E_actual = P_Q_out sigma_1(D_GU^epsilon) I_Q_in.
3. Record source-derived a, b, and lambda_d.
4. Audit E_actual for non-null kernel over all real mixed 14D covectors.
5. If and only if that passes, form the actual R-sector Schur symbol and start
   the section-pulled FC-VZ-4 characteristic certificate with the full loss ledger.
```

## 8. Machine-Readable JSON Summary

```json
{
  "artifact": "HOURLY_CYCLE2_ACTUAL_DGU_OPERATOR_CERTIFICATE_SCHEMA",
  "schema_version": "ACTUAL_DGU_01_OPERATOR_CERTIFICATE_SCHEMA_V1",
  "verdict": "UNDERDEFINED_BLOCKED__SCHEMA_SPECIFIED_BUT_SOURCE_CLOSED_ACTUAL_DGU_01_OPERATOR_MISSING",
  "verdict_class": "underdefined_blocked",
  "decision_for_current_sources": "BLOCKED_MISSING_SOURCE_OBJECT",
  "certificate": {
    "name": "ActualDGU01OperatorCertificate",
    "current_instance_status": "schema_defined_not_instantiated",
    "first_missing_field": "source.operator_source_primary_action_or_EL",
    "required_groups": [
      "source",
      "projection",
      "finality",
      "loss",
      "rollback_conditions"
    ]
  },
  "source_required_fields": [
    "operator_source_primary_action_or_EL",
    "actual_operator_formula",
    "rolled_up_domain",
    "rolled_up_codomain",
    "base_and_cone",
    "signature_and_clifford_convention",
    "chirality_domain_codomain",
    "coordinate_convention",
    "sigma_1_D_GU_0_1_sector",
    "coefficient_a_nonzero",
    "coefficient_b_nonzero",
    "coefficient_lambda_d_nonzero"
  ],
  "projection_required_fields": [
    "Q_in_Q_out_projectors",
    "spin_3_2_projector",
    "E_actual_definition",
    "Schur_blocks",
    "all_real_mixed_covector_domain"
  ],
  "finality_required_fields": {
    "FC-VZ-1": {
      "status": "open_actual_operator_certificate_missing",
      "accept_if": "E_actual_has_no_non_null_kernel_for_all_real_mixed_14D_covectors_and_required_coefficients_are_source_derived_nonzero",
      "fail_if": "source_fails_or_non_null_E_actual_kernel_found_or_lambda_d_zero_for_Schur_route"
    },
    "FC-VZ-4": {
      "status": "open_actual_section_pulled_subprincipal_characteristic_certificate_missing",
      "required_follow_on_object": "ActualSectionPulledSubprincipalCharacteristicCertificate",
      "accept_if": "actual_coupled_RS_constraint_characteristic_roots_confined_to_null_cone",
      "fail_if": "spacelike_characteristic_found_or_constraint_source_changes_characteristic_cone"
    }
  },
  "loss_required_fields": [
    "Phi_2_Phi_d_Phi_F_order_split",
    "extra_order_one_terms",
    "lower_order_Z_A_ledger",
    "section_pullback_rule",
    "constraint_blocks_gamma_trace_K_mu_nu"
  ],
  "strongest_positive_construction": {
    "claim": "schema permits transport of typed FC-VZ-1 proof only after source-closed actual D_GU certificate is filled",
    "requires_actual_operator_certificate": true,
    "requires_a_nonzero": true,
    "requires_b_nonzero": true,
    "requires_lambda_d_nonzero": true,
    "requires_all_real_mixed_covectors": true,
    "requires_no_harmful_extra_first_order_loss_terms": true,
    "does_not_close_full_vz": true
  },
  "first_exact_obstruction": "ActualDGU01OperatorCertificate.source.operator_source_primary_action_or_EL",
  "constructive_next_object": "ActualDGU01OperatorCertificateInstance_V1",
  "explicit_non_claims": {
    "actual_GU_RS_operator_identified_from_current_sources": false,
    "FC-VZ-1_closed_for_actual_D_GU": false,
    "FC-VZ-4_closed_for_actual_section_pulled_operator": false,
    "VZ_evasion_closed": false,
    "hyperbolicity_established": false,
    "causality_established": false,
    "absence_of_spacelike_characteristics_proved": false
  },
  "rollback_conditions": [
    "ActualDGU01OperatorCertificate_missing",
    "operator_source_primary_action_or_EL_missing",
    "actual_operator_differs_from_D_roll_typed_spine",
    "actual_D_GU_0_1_block_absent",
    "rolled_up_domain_or_codomain_mismatch",
    "trace_coordinate_and_embedded_coordinate_conventions_mixed",
    "coefficient_a_zero",
    "coefficient_b_zero",
    "coefficient_lambda_d_zero",
    "Phi_d_not_present_as_order_one_source_of_F_xi",
    "Phi_F_used_as_F_xi_principal_block",
    "Q_in_Q_out_projectors_missing_or_unnormalized",
    "proof_checks_only_pure_horizontal_or_pure_vertical_covectors",
    "hidden_first_order_terms_placed_in_Z_A_without_projection_or_kernel_audit",
    "extra_first_order_Q_or_R_term_has_non_null_kernel",
    "non_null_E_actual_kernel_found",
    "actual_R_sector_Schur_block_differs_and_has_non_null_kernel",
    "section_pullback_payload_missing",
    "II_s_H_enters_effective_first_order_symbol",
    "K_mu_nu_constraint_source_changes_characteristic_cone",
    "gamma_trace_constraint_system_has_spacelike_characteristic",
    "spacelike_characteristic_found_for_actual_section_pulled_operator",
    "standalone_GU_RS_Lagrangian_has_VZ_spacelike_roots"
  ],
  "next_meaningful_step": [
    "extract_source_closed_actual_D_GU_0_1_operator_certificate",
    "compute_E_actual_from_sigma_1_D_GU",
    "audit_E_actual_over_all_real_mixed_non_null_14D_covectors",
    "classify_extra_first_order_loss_terms",
    "only_then_start_actual_section_pulled_FC_VZ_4_characteristic_certificate"
  ]
}
```
