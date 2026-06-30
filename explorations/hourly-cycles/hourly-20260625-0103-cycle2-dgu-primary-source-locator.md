---
title: "Hourly 20260625-0103 Cycle 2 DGU Primary Source Locator"
date: "2026-06-25"
run: "hourly-20260625-0103"
cycle: "2"
lane: "4"
doc_type: dgu_primary_source_locator
locator_id: "DGUPrimarySourceLocator_V1"
verdict: "UNDERDEFINED_BLOCKED__NO_PRIMARY_SOURCE_EMITS_ACTUAL_DGU01_OPERATOR"
owned_path: "explorations/hourly-20260625-0103-cycle2-dgu-primary-source-locator.md"
companion_audit: "tests/hourly_20260625_0103_cycle2_dgu_primary_source_locator_audit.py"
---

# Hourly 20260625-0103 Cycle 2 DGU Primary Source Locator

## 1. Verdict

Verdict: **underdefined / blocked**.

`DGUPrimarySourceLocator_V1` does not locate a repo-local primary GU action,
primary GU operator definition, or Euler-Lagrange derivation that emits the
actual `D_GU^epsilon` operator on the rolled-up 0/1 sector.

The strongest positive source chain remains:

```text
UCSD transcript primary hint:
  Dirac-DeRham-Einstein complex, ordinary derivative from one-forms to
  two-forms, ship-in-a-bottle map back to one-forms

older reconstruction algebra:
  D_GU = (d + d*) tensor 1_S + Phi
  D_GU(u, psi) = (d_A^* psi, d_A u + Phi(d_A psi))

typed-spine proposal:
  D_roll^epsilon(u, psi)
    =
    (d_A^* psi, d_A u + lambda_d Phi_2(d_A psi)) + Z_A^epsilon(u, psi)
```

That chain supplies a **primary hint plus reconstruction target**, not a
source receipt. The current locator decision is therefore:

```text
locator_decision: REJECT_NO_PRIMARY_SOURCE_EMITS_ACTUAL_DGU01_OPERATOR
DGU01OperatorSourceReceipt_V1_can_accept: false
first_missing_source_receipt: operator_source_primary_action_or_EL
```

This artifact does **not** claim actual operator identification, FC-VZ-1
closure, FC-VZ-4 closure, VZ evasion, hyperbolicity, causality, or absence of
spacelike characteristics.

## 2. Direct Source Derivations

`RESEARCH-POSTURE.md` allows constructive reconstruction but forbids
compatibility-as-derivation and verdict inflation.

`process/runbooks/five-lane-frontier-run.md` requires a decision-grade lane
artifact, exact obstruction, rollback conditions, and separation of hosted,
conditional, imported, and derived objects.

`literature/weinstein-ucsd-2025-04-transcript.md` and
`papers/Transcript into the impossible.md` are the strongest primary-source
surfaces read here. They provide:

```text
[00:05:43] GU has a first-order theory and a second-order square.
[00:34:27] GU creates a Dirac-DeRham-Einstein complex.
[00:35:30] connection information supplies a minimally coupled exterior derivative.
[00:36:13] a ship-in-a-bottle map knocks the two-form output back to one-forms.
[00:48:49] the linearized field content is zero-forms and one-forms valued in
           ad or spinors.
```

These are primary hints for the rolled-up complex. They do not provide a
fully typed `D_GU^epsilon` 0/1-sector formula, coefficient `lambda_d`,
principal symbol, Q projectors, chirality convention, or extra first-order term
ledger.

`explorations/generation-count-cl95-dirac-derham-2026-06-22.md` writes a
reconstruction-grade operator:

```text
D_GU = (d + d*) tensor 1_S + Phi
D_GU(u, psi) = (d_A^* psi, d_A u + Phi(d_A psi))
```

It labels the block as reconstruction from the transcript and standard
Dirac-DeRham reasoning. It is not a primary action/operator/Euler-Lagrange
source receipt.

`explorations/vz1-schur-complement-symbol-2026-06-23.md` computes from the
rolled-up reconstruction model:

```text
sigma_D(xi)(u, psi) = (i_xi psi, xi tensor u + F_xi psi)
F_xi := sigma(Phi o d_A)(xi)
```

That file is useful algebra, but it assumes the operator model. It does not
source-close actual `D_GU^epsilon`.

`explorations/gu-typed-operator-action-spine-2026-06-24.md` gives the best
typed candidate and explicitly labels it `CANONICAL_PROPOSAL_NOT_PROOF_GRADE`.

`explorations/primary-gu-interface-contract-2026-06-24.md` records that the
repo has a typed operator spine but no source-closed primary action/operator.
It also states that the VZ route may cite only a `D_GU` whose first-order
0/1 block contains `Phi_d = Phi_2 o d_A`.

`explorations/goal-draft-primary-gu-action-operator-spec-2026-06-24.md`
requests exactly the missing object: a primary typed `D_GU` and `S_GU`
specification.

`explorations/hourly-20260625-0103-cycle1-dgu-01-operator-source-receipt.md`
and `explorations/hourly-cycle3-dgu-operator-source-receipt-inventory-2026-06-25.md`
already reject typed-spine-only material as a primary source receipt. This
locator pass independently confirms that no searched repo-local primary source
removes the missing field.

`sources/claim-ledger.md` is still a template ledger with no populated DGU
operator receipt rows. `sources/media-claim-mining-report-v1.md` reports
coverage gaps and explicitly warns that media claims are not mathematical
evidence without formal connections.

## 3. Source Locator Decision Table

| Source or object | Category | Locator result | Emits actual `D_GU^epsilon` 0/1 operator? | Acceptable for `DGU01OperatorSourceReceipt_V1`? | Decision reason |
|---|---|---:|---:|---:|---|
| UCSD transcript / local duplicate | primary transcript hint | found | no | no | Names first-order GU, Dirac-DeRham-Einstein complex, and ship-in-a-bottle rollback; does not emit typed formula, coefficients, projectors, or principal symbol. |
| `generation-count-cl95-dirac-derham-2026-06-22.md` | reconstruction algebra | found | no | no | Writes `D_GU` formula, but explicitly as reconstruction from transcript and standard operator theory. |
| `vz1-schur-complement-symbol-2026-06-23.md` | reconstruction algebra backend | found | no | no | Computes symbol and Schur data after assuming rolled-up operator model. |
| `gu-typed-operator-action-spine-2026-06-24.md` | typed-spine proposal | found | no | no | Best typed `D_roll` candidate, explicitly not proof-grade primary closure. |
| `primary-gu-interface-contract-2026-06-24.md` | governance/interface contract | found | no | no | States primary action/operator remains underdefined. |
| `goal-draft-primary-gu-action-operator-spec-2026-06-24.md` | draft goal | found | no | no | Defines deliverables for the missing source object rather than supplying it. |
| `sources/claim-ledger.md` | claim-ledger template | found | no | no | No populated source row for primary DGU action/operator/EL. |
| `sources/media-claim-mining-report-v1.md` | process/source coverage note | found | no | no | Warns that media claims require formal connections; no operator receipt. |
| Primary GU action/operator/EL derivation cell | missing source receipt | not found | no | no | This is the first missing source receipt. |

## 4. Strongest Positive Result

The strongest positive result is a target shape for a future receipt:

```text
candidate_id:
  D_roll_typed_spine_candidate

operator_candidate:
  D_roll^epsilon(u, psi)
    =
    (d_A^* psi, d_A u + lambda_d Phi_2(d_A psi)) + Z_A^epsilon(u, psi)

principal_candidate:
  sigma_1(D_roll^epsilon)(xi)(u, psi)
    =
    (i_xi psi, xi tensor u + lambda_d F_xi psi)

order_split:
  Phi_2: zero-order algebraic shiab
  Phi_d := Phi_2 o d_A: first-order differential composite
  F_xi := sigma_1(Phi_d)(xi): VZ first-order principal block
  Phi_F := Phi_2(F_A tensor -): zero-order curvature insertion
```

The positive result is decision-useful because it says exactly what a future
primary source must emit. It is not sufficient for actual operator
identification.

## 5. First Exact Obstruction

The first exact obstruction is:

```text
ActualDGU01OperatorCertificate.source.operator_source_primary_action_or_EL
```

Equivalently, the first missing source receipt is:

```text
operator_source_primary_action_or_EL
```

The missing receipt must be one of:

```text
primary_GU_action
primary_GU_operator_definition
Euler_Lagrange_derivation_from_primary_action
```

and it must emit, before any VZ replay:

```text
D_GU^epsilon on S^epsilon plus T^*Y tensor S^-epsilon
sigma_1(D_GU^epsilon)(y, xi)
source-derived a, b, lambda_d
Phi_2/Phi_d/F_xi/Phi_F order split
Q_in/Q_out projectors
chirality and coordinate conventions
complete extra first-order 0/1 term ledger
```

## 6. Constructive Next Object

The constructive next object is still:

```text
DGU01OperatorSourceReceipt_V1
```

It should accept only if a primary action/operator/EL source emits the actual
0/1-sector operator. If it accepts, the follow-on object is:

```text
ActualDGU01OperatorCertificateInstance_V1
```

The next source-extraction packet should be:

```text
1. Locate a primary GU action/operator/EL source cell.
2. Extract the actual D_GU^epsilon 0/1 operator.
3. Compute sigma_1(D_GU^epsilon) from that source.
4. Compare it to D_roll without changing conventions after the fact.
5. Record all coefficient and extra-term differences.
6. Emit ActualDGU01OperatorCertificateInstance_V1 only after receipt acceptance.
```

## 7. GU Claim Impact

`DGU01OperatorSourceReceipt_V1` **cannot accept** on current repo-local sources.

Current claim impact:

```text
actual operator identification: not claimed
source receipt for actual D_GU^epsilon 0/1 sector: rejected
typed-spine route: coherent candidate only
FC-VZ-1 for actual D_GU: open
FC-VZ-4 for actual section-pulled operator: open
VZ evasion: not claimed
hyperbolicity: not claimed
causality: not claimed
absence of spacelike characteristics: not claimed
```

The transcript materially supports the existence of a rolled-up
Dirac-DeRham-Einstein program, and the typed spine turns that into a sharp
test object. The missing step is source provenance for the actual operator.

## 8. Next Proof Step

The next proof step is source localization and extraction, not another
typed-spine Schur calculation:

```text
source target:
  primary_GU_action_or_operator_or_EL_for_D_GU_epsilon_0_1

minimum pass condition:
  source emits D_GU^epsilon 0/1 formula and sigma_1(D_GU^epsilon)

minimum fail condition:
  only transcript hints, typed-spine proposal, or reconstruction algebra are available
```

If the primary source emits `Phi_d` with nonzero `lambda_d`, the typed VZ
backend becomes replayable against actual-source data. If it emits only
`Phi_F(A)` or sets `lambda_d = 0`, the current `F_xi` VZ route fails for the
actual operator and must be rebuilt.

## 9. Machine-Readable JSON Summary

```json
{
  "artifact": "DGUPrimarySourceLocator_V1",
  "run": "hourly-20260625-0103",
  "cycle": "2",
  "lane": "4",
  "verdict": "UNDERDEFINED_BLOCKED__NO_PRIMARY_SOURCE_EMITS_ACTUAL_DGU01_OPERATOR",
  "verdict_class": "underdefined_blocked",
  "locator_decision": "REJECT_NO_PRIMARY_SOURCE_EMITS_ACTUAL_DGU01_OPERATOR",
  "DGU01OperatorSourceReceipt_V1_can_accept": false,
  "can_emit_actual_dgu_certificate_instance": false,
  "first_exact_obstruction": "ActualDGU01OperatorCertificate.source.operator_source_primary_action_or_EL",
  "first_missing_source_receipt": "operator_source_primary_action_or_EL",
  "source_categories": [
    "primary_transcript_hint",
    "typed_spine_proposal",
    "reconstruction_algebra",
    "governance_interface_contract",
    "draft_goal",
    "claim_ledger_template",
    "process_source_coverage_note",
    "missing_primary_action_operator_EL_receipt"
  ],
  "source_locator_decision_table": [
    {
      "source": "literature/weinstein-ucsd-2025-04-transcript.md",
      "category": "primary_transcript_hint",
      "locator_result": "found",
      "emits_actual_D_GU_epsilon_0_1_operator": false,
      "acceptable_for_DGU01OperatorSourceReceipt_V1": false,
      "decision_reason": "Primary hints for first-order GU, Dirac-DeRham-Einstein complex, and ship-in-a-bottle rollback; no typed actual 0_1 operator formula, coefficients, projectors, or principal symbol."
    },
    {
      "source": "papers/Transcript into the impossible.md",
      "category": "primary_transcript_hint_duplicate",
      "locator_result": "found",
      "emits_actual_D_GU_epsilon_0_1_operator": false,
      "acceptable_for_DGU01OperatorSourceReceipt_V1": false,
      "decision_reason": "Local duplicate transcript surface confirms hints but not a source receipt."
    },
    {
      "source": "explorations/generation-count-cl95-dirac-derham-2026-06-22.md",
      "category": "reconstruction_algebra",
      "locator_result": "found",
      "emits_actual_D_GU_epsilon_0_1_operator": false,
      "acceptable_for_DGU01OperatorSourceReceipt_V1": false,
      "decision_reason": "Writes D_GU formula at reconstruction grade from transcript and standard Dirac-DeRham reasoning."
    },
    {
      "source": "explorations/vz1-schur-complement-symbol-2026-06-23.md",
      "category": "reconstruction_algebra_backend",
      "locator_result": "found",
      "emits_actual_D_GU_epsilon_0_1_operator": false,
      "acceptable_for_DGU01OperatorSourceReceipt_V1": false,
      "decision_reason": "Computes symbol after assuming the rolled-up operator model."
    },
    {
      "source": "explorations/gu-typed-operator-action-spine-2026-06-24.md",
      "category": "typed_spine_proposal",
      "locator_result": "found",
      "emits_actual_D_GU_epsilon_0_1_operator": false,
      "acceptable_for_DGU01OperatorSourceReceipt_V1": false,
      "decision_reason": "Best typed D_roll candidate but explicitly canonical proposal, not proof-grade primary closure."
    },
    {
      "source": "explorations/primary-gu-interface-contract-2026-06-24.md",
      "category": "governance_interface_contract",
      "locator_result": "found",
      "emits_actual_D_GU_epsilon_0_1_operator": false,
      "acceptable_for_DGU01OperatorSourceReceipt_V1": false,
      "decision_reason": "States primary action/operator remains underdefined."
    },
    {
      "source": "explorations/goal-draft-primary-gu-action-operator-spec-2026-06-24.md",
      "category": "draft_goal",
      "locator_result": "found",
      "emits_actual_D_GU_epsilon_0_1_operator": false,
      "acceptable_for_DGU01OperatorSourceReceipt_V1": false,
      "decision_reason": "Specifies the missing deliverable rather than supplying it."
    },
    {
      "source": "sources/claim-ledger.md",
      "category": "claim_ledger_template",
      "locator_result": "found",
      "emits_actual_D_GU_epsilon_0_1_operator": false,
      "acceptable_for_DGU01OperatorSourceReceipt_V1": false,
      "decision_reason": "No populated DGU operator receipt rows."
    },
    {
      "source": "sources/media-claim-mining-report-v1.md",
      "category": "process_source_coverage_note",
      "locator_result": "found",
      "emits_actual_D_GU_epsilon_0_1_operator": false,
      "acceptable_for_DGU01OperatorSourceReceipt_V1": false,
      "decision_reason": "Coverage note and warning, not formal mathematical receipt."
    },
    {
      "source": "primary_GU_action_operator_or_EL_derivation_cell",
      "category": "missing_primary_action_operator_EL_receipt",
      "locator_result": "not_found",
      "emits_actual_D_GU_epsilon_0_1_operator": false,
      "acceptable_for_DGU01OperatorSourceReceipt_V1": false,
      "decision_reason": "First missing source receipt."
    }
  ],
  "strongest_positive_result": {
    "candidate": "D_roll^epsilon(u,psi)=(d_A^* psi, d_A u + lambda_d Phi_2(d_A psi)) + Z_A^epsilon(u,psi)",
    "principal_candidate": "sigma_1(D_roll^epsilon)(xi)(u,psi)=(i_xi psi, xi tensor u + lambda_d F_xi psi)",
    "candidate_status": "coherent_typed_spine_candidate_not_source_receipt",
    "requires_primary_source_receipt": true,
    "requires_actual_sigma_1_D_GU": true,
    "requires_source_derived_a_b_lambda_d": true,
    "requires_extra_first_order_terms_audited": true,
    "accepted_as_receipt": false
  },
  "direct_source_derivations": {
    "transcript_hints": [
      "first_order_theory_and_second_order_square",
      "Dirac_DeRham_Einstein_complex",
      "minimally_coupled_exterior_derivative_from_connection_information",
      "ship_in_a_bottle_maps_two_forms_back_to_one_forms",
      "linearized_zero_forms_and_one_forms_valued_in_ad_or_spinors"
    ],
    "typed_spine_proposals": [
      "D_roll_typed_candidate",
      "Phi_2_Phi_d_F_xi_Phi_F_order_split",
      "Z_A_lower_order_ledger"
    ],
    "reconstruction_algebra": [
      "D_GU_equals_d_plus_d_star_tensor_one_plus_Phi",
      "rolled_up_D_GU_u_psi_formula",
      "principal_symbol_sigma_D_xi_assuming_rolled_up_model"
    ],
    "actual_source_receipts": []
  },
  "receipt_acceptance_conditions": [
    "source_locator_present",
    "source_status_primary",
    "operator_source_primary_action_or_EL_present",
    "actual_D_GU_epsilon_0_1_formula_emitted",
    "sigma_1_D_GU_epsilon_computed_from_source",
    "a_b_lambda_d_source_derived",
    "Phi_2_Phi_d_F_xi_Phi_F_order_split_preserved",
    "Q_in_Q_out_projectors_fixed",
    "chirality_convention_fixed",
    "coordinate_convention_fixed",
    "extra_first_order_terms_listed_or_kernel_audited",
    "typed_spine_candidate_not_used_as_primary_source",
    "reconstruction_algebra_not_used_as_primary_source",
    "transcript_hint_not_used_as_full_operator_receipt"
  ],
  "explicit_nonclaims": {
    "actual_operator_identification": false,
    "FC_VZ_1_closed_for_actual_D_GU": false,
    "FC_VZ_4_closed_for_actual_section_pulled_operator": false,
    "VZ_evasion_closed": false,
    "hyperbolicity_established": false,
    "causality_established": false,
    "absence_of_spacelike_characteristics_proved": false
  },
  "rollback_conditions": [
    "operator_source_primary_action_or_EL_missing",
    "typed_spine_candidate_as_primary_source",
    "typed_spine_only",
    "transcript_hint_only",
    "reconstruction_algebra_only",
    "actual_operator_formula_absent",
    "actual_D_GU_0_1_block_absent",
    "actual_operator_differs_from_D_roll_typed_spine",
    "rolled_up_domain_or_codomain_mismatch",
    "coefficient_a_not_source_derived",
    "coefficient_b_not_source_derived",
    "coefficient_lambda_d_not_source_derived",
    "coefficient_lambda_d_zero",
    "Phi_d_not_present_as_order_one_source_of_F_xi",
    "Phi_F_used_as_F_xi_principal_block",
    "Q_in_Q_out_projectors_missing_or_unnormalized",
    "extra_first_order_terms_not_audited",
    "trace_coordinate_and_embedded_coordinate_conventions_mixed"
  ],
  "constructive_next_object": "DGU01OperatorSourceReceipt_V1",
  "follow_on_object_if_accepted": "ActualDGU01OperatorCertificateInstance_V1",
  "next_proof_step": [
    "locate_primary_GU_action_operator_or_EL_source_cell",
    "extract_actual_D_GU_epsilon_0_1_operator",
    "compute_sigma_1_D_GU_epsilon_from_source",
    "derive_source_coefficients_a_b_lambda_d",
    "list_or_audit_extra_first_order_terms",
    "compare_actual_operator_to_D_roll_without_convention_change",
    "emit_ActualDGU01OperatorCertificateInstance_V1_only_after_receipt_acceptance"
  ]
}
```
