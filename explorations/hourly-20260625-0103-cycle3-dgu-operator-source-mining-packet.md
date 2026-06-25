---
title: "Hourly 20260625 0103 Cycle 3 DGU Operator Source Mining Packet"
date: "2026-06-25"
run: "hourly-20260625-0103"
cycle: "3"
lane: "4"
doc_type: dgu_operator_source_mining_packet
artifact_id: "DGUOperatorSourceMiningPacket_V1"
verdict: "BLOCKED_PACKET_READY_NO_ACTUAL_DGU01_SOURCE_RECEIPT"
owned_path: "explorations/hourly-20260625-0103-cycle3-dgu-operator-source-mining-packet.md"
companion_audit: "tests/hourly_20260625_0103_cycle3_dgu_operator_source_mining_packet_audit.py"
---

# Hourly 20260625 0103 Cycle 3 DGU Operator Source Mining Packet

## 1. Verdict

Verdict: **blocked / packet ready**.

`DGUOperatorSourceMiningPacket_V1` does not promote an actual
`D_GU^epsilon` 0/1 operator claim. It is the decision packet required to
resolve the next source receipt:

```text
DGU01OperatorSourceReceipt_V1
```

Current decision:

```text
receipt_status: not_accepted
packet_status: ready_for_source_mining
first_exact_obstruction: operator_source_primary_action_or_EL
next_gate: ActualDGU01OperatorCertificateInstance_V1 only after receipt acceptance
```

The source miner must find a primary GU action, primary GU operator definition,
or Euler-Lagrange derivation that emits the actual 0/1-sector operator. Typed
spine, transcript hint, reconstruction algebra, and VZ backend computations are
admissible comparison material only after the source receipt is present.

## 2. Direct Derivations From Repo Sources

`RESEARCH-POSTURE.md` permits aggressive constructive reconstruction but
forbids compatibility-as-derivation, verdict inflation, and hiding imported
target data inside a reconstruction.

`process/runbooks/five-lane-frontier-run.md` requires a decision-grade artifact:
verdict, direct derivations, strongest positive result, first exact obstruction,
constructive next object, claim impact, and next proof step.

`explorations/hourly-20260625-0103-cycle2-dgu-primary-source-locator.md`
establishes the local DGU/VZ blocker:

```text
locator_decision: REJECT_NO_PRIMARY_SOURCE_EMITS_ACTUAL_DGU01_OPERATOR
first_missing_source_receipt: operator_source_primary_action_or_EL
```

It also identifies the strongest current candidate shape, not as a receipt:

```text
D_roll^epsilon(u, psi)
  =
  (d_A^* psi, d_A u + lambda_d Phi_2(d_A psi)) + Z_A^epsilon(u, psi)

sigma_1(D_roll^epsilon)(xi)(u, psi)
  =
  (i_xi psi, xi tensor u + lambda_d F_xi psi)
```

`explorations/hourly-20260625-0103-cycle2-primary-gu-source-receipt-availability-ledger.md`
generalizes the same DGU/VZ result across the family ledger: the repo has a
typed-spine candidate and conditional algebra, but no primary source receipt
for `operator_source_primary_action_or_EL`.

`sources/media-index.md` gives provenance discipline. Media entries may supply
chronology, terminology, and timestamped claim surfaces. They are not proof, and
mathematical claims require transcript, timestamp, and exact context.

`sources/media-contributor-tasks-v1.md` confirms that contributor tasks should
claim-mine source surfaces with exact timestamp rows and should not invent
missing formal content.

These sources derive this packet's rule:

```text
source-first sequence:
  primary source locator
  -> exact source fragment or derivation cell
  -> emitted actual 0/1 operator
  -> source-derived symbol and fields
  -> comparison to typed spine
  -> certificate instance gate
```

## 3. Accepted Primary Evidence Packet

The receipt may accept only one of these primary evidence classes:

| evidence class | required content | accepted as receipt? |
|---|---|---:|
| `primary_GU_action` | A primary GU action whose first variation or named Euler-Lagrange equation emits the actual `D_GU^epsilon` 0/1 block. | yes |
| `primary_GU_operator_definition` | A primary GU source directly defining the actual `D_GU^epsilon` operator on the 0/1 rolled-up sector. | yes |
| `Euler_Lagrange_derivation_from_primary_action` | A derivation cell from a primary action to the actual 0/1 operator, with variations and conventions fixed. | yes |
| `primary_timestamped_formal_statement` | A primary transcript or video timestamp that states the formal operator/action/EL formula sufficiently to fill all receipt fields below. | yes, only if formula-complete |

Minimum locator fields:

```text
source_id
source_kind
source_status
primary_url_or_repo_path
timestamp_or_page_or_equation_locator
exact_context
transcript_or_manuscript_fragment
receipt_kind
emitted_formula_or_derivation_cell
extractor_notes
```

Source status must be one of:

```text
primary_official_manuscript
primary_official_lecture_or_video
primary_official_transcript
primary_author_derivation_cell
```

Secondary summaries, community notes, repo reconstructions, and typed-spine
proposals may help locate the source but cannot satisfy the receipt.

## 4. Required Formula And Symbol Fields

The receipt must fill these mathematical fields before
`ActualDGU01OperatorCertificateInstance_V1` can be opened:

| field | required value or derivation |
|---|---|
| `domain_0_1` | The source-defined 0/1 sector domain, including whether it is `S^epsilon plus T^*Y tensor S^-epsilon` or a different actual domain. |
| `codomain_0_1` | The source-defined codomain and chirality target. |
| `D_GU_epsilon_formula` | The actual operator formula, not a normalized typed-spine replacement. |
| `principal_symbol_sigma_1` | `sigma_1(D_GU^epsilon)(y, xi)` computed from the source formula. |
| `a_coefficient` | Source-derived coefficient for the degree-lowering/codifferential block, if present. |
| `b_coefficient` | Source-derived coefficient for the degree-raising/exterior block, if present. |
| `lambda_d` | Source-derived coefficient of the first-order `Phi_2 o d_A` contribution, including the possibility that the source sets it to zero. |
| `Phi_2` | Zero-order algebraic ship-in-a-bottle map, if present. |
| `Phi_d` | First-order composite `Phi_2 o d_A`, if present. |
| `F_xi` | Principal symbol of `Phi_d`, not of the zero-order curvature insertion. |
| `Phi_F` | Zero-order curvature insertion `Phi_2(F_A tensor -)`, separately tracked from `F_xi`. |
| `Q_in` | Source-fixed input projection or inclusion convention. |
| `Q_out` | Source-fixed output projection or rolled-up projection convention. |
| `chirality_convention` | `epsilon`, `-epsilon`, spinor bundle, and sign conventions. |
| `coordinate_convention` | Trace-coordinate versus embedded-coordinate convention, with no post hoc switching. |
| `extra_first_order_terms` | Complete list of all additional first-order 0/1 terms, or a source-backed proof that none exist. |
| `lower_order_terms` | Lower-order terms, separated from the principal symbol. |
| `normalization_policy` | Whether coefficients are source-normalized, gauge-normalized, or still raw. |

The pass condition is not that the source agrees with `D_roll^epsilon`. The pass
condition is that the actual source-derived operator is explicit enough to be
compared to `D_roll^epsilon` without changing conventions after extraction.

## 5. Rejection Conditions

Reject the receipt immediately if any of these conditions holds:

```text
typed_spine_only
transcript_hint_only
reconstruction_algebra_only
conditional_VZ_backend_only
media_summary_without_exact_formula
community_transcript_without_primary_video_check_for_formula_claim
operator_formula_absent
actual_0_1_block_absent
domain_or_codomain_absent
principal_symbol_absent_or_not_computable
a_b_lambda_d_not_source_derived
Phi_d_and_Phi_F_conflated
F_xi_derived_from_zero_order_Phi_F
Q_in_Q_out_missing
chirality_convention_missing
coordinate_convention_missing_or_switched
extra_first_order_terms_unlisted
typed_spine_used_as_primary_source
receipt_claim_depends_on_target_VZ_success
```

Typed-spine evidence has a useful role, but only as comparison evidence:

```text
accepted_use:
  candidate_shape
  field checklist
  comparison target after source extraction
  rollback trigger when actual source differs

rejected_use:
  primary source receipt
  actual operator identification
  source-derived coefficient proof
  FC-VZ closure for actual D_GU
```

## 6. Strongest Positive Packet

The strongest positive packet available before a source receipt is a mining
template, not a mathematical theorem:

```text
candidate_id: D_roll_typed_spine_candidate
candidate_status: coherent_candidate_not_receipt

candidate_formula:
  D_roll^epsilon(u, psi)
    =
    (d_A^* psi, d_A u + lambda_d Phi_2(d_A psi)) + Z_A^epsilon(u, psi)

candidate_principal_symbol:
  sigma_1(D_roll^epsilon)(xi)(u, psi)
    =
    (i_xi psi, xi tensor u + lambda_d F_xi psi)

field_packet:
  domain_0_1, codomain_0_1, D_GU_epsilon_formula,
  sigma_1(D_GU_epsilon), a, b, lambda_d,
  Phi_2, Phi_d, F_xi, Phi_F,
  Q_in, Q_out, chirality, coordinates,
  extra_first_order_terms, lower_order_terms
```

This is decision-useful because it tells the next worker exactly what to extract
from primary sources and exactly when to reject an apparent source.

## 7. First Exact Obstruction

The first exact obstruction remains:

```text
operator_source_primary_action_or_EL
```

Expanded certificate path:

```text
ActualDGU01OperatorCertificate.source.operator_source_primary_action_or_EL
```

No downstream object can close earlier than this. In particular, the following
objects must remain unopened or explicitly conditional:

```text
ActualDGU01OperatorCertificateInstance_V1
FC_VZ_1_actual_D_GU_closure
FC_VZ_4_actual_section_pulled_operator_closure
VZ_evasion_for_actual_D_GU
hyperbolicity_certificate
causality_certificate
absence_of_spacelike_characteristics_certificate
```

## 8. Constructive Next Object

The constructive next object is:

```text
DGU01OperatorSourceReceipt_V1
```

Minimum schema:

```text
receipt_id
source_id
source_kind
source_status
locator
receipt_kind
exact_fragment
emitted_actual_operator_formula
domain_0_1
codomain_0_1
principal_symbol_sigma_1
coefficients: a, b, lambda_d
order_split: Phi_2, Phi_d, F_xi, Phi_F
projectors: Q_in, Q_out
chirality_convention
coordinate_convention
extra_first_order_terms
lower_order_terms
comparison_to_D_roll
acceptance_decision
rollback_conditions_triggered
nonclaims
next_gate
```

If and only if `acceptance_decision = accepted`, open:

```text
ActualDGU01OperatorCertificateInstance_V1
```

That certificate instance should then compare the actual source operator to the
typed-spine candidate and decide whether the VZ backend is replayable, must be
modified, or fails for the actual operator.

## 9. GU Impact

Current impact:

```text
actual_D_GU_operator_identification: not_claimed
DGU01OperatorSourceReceipt_V1: not_accepted
typed_spine_status: coherent_candidate_only
FC_VZ_1_for_actual_D_GU: open
FC_VZ_4_for_actual_section_pulled_operator: open
VZ_evasion: not_claimed
hyperbolicity: not_claimed
causality: not_claimed
absence_of_spacelike_characteristics: not_claimed
```

If the primary source emits nonzero `lambda_d` and no obstructing extra
first-order terms, the typed VZ backend becomes eligible for actual-operator
replay. If the primary source emits no `Phi_d` first-order block, sets
`lambda_d = 0`, or adds symbol-relevant terms outside the typed spine, the
existing typed VZ route is not an actual-operator closure and must be rebuilt.

## 10. Next Step

Run source mining in this exact order:

```text
1. Search primary official GU manuscripts, lecture/video transcripts, and
   author derivation cells for an action/operator/EL formula.
2. Record source locator, timestamp/page/equation, exact context, and fragment.
3. Extract the actual 0/1 operator before comparing it to D_roll.
4. Compute sigma_1(D_GU^epsilon) from the extracted formula.
5. Fill coefficients, order split, projectors, chirality, coordinates, and
   extra first-order term ledger.
6. Apply rejection conditions.
7. If accepted, emit DGU01OperatorSourceReceipt_V1 and only then open
   ActualDGU01OperatorCertificateInstance_V1.
```

Do not replay VZ closure against typed-spine-only evidence.

## 11. Machine-Readable JSON Summary

```json
{
  "artifact": "DGUOperatorSourceMiningPacket_V1",
  "run": "hourly-20260625-0103",
  "cycle": 3,
  "lane": 4,
  "verdict": "BLOCKED_PACKET_READY_NO_ACTUAL_DGU01_SOURCE_RECEIPT",
  "verdict_class": "blocked_packet_ready",
  "receipt_status": "not_accepted",
  "packet_status": "ready_for_source_mining",
  "first_exact_obstruction": "operator_source_primary_action_or_EL",
  "certificate_source_path": "ActualDGU01OperatorCertificate.source.operator_source_primary_action_or_EL",
  "constructive_next_object": "DGU01OperatorSourceReceipt_V1",
  "next_gate_if_accepted": "ActualDGU01OperatorCertificateInstance_V1",
  "accepted_primary_evidence_classes": [
    {
      "evidence_class": "primary_GU_action",
      "required_content": "primary GU action whose first variation or named Euler-Lagrange equation emits the actual D_GU^epsilon 0/1 block",
      "accepted_as_receipt": true
    },
    {
      "evidence_class": "primary_GU_operator_definition",
      "required_content": "primary GU source directly defining the actual D_GU^epsilon operator on the 0/1 rolled-up sector",
      "accepted_as_receipt": true
    },
    {
      "evidence_class": "Euler_Lagrange_derivation_from_primary_action",
      "required_content": "derivation cell from a primary action to the actual 0/1 operator with variations and conventions fixed",
      "accepted_as_receipt": true
    },
    {
      "evidence_class": "primary_timestamped_formal_statement",
      "required_content": "primary transcript or video timestamp that states the formal operator/action/EL formula sufficiently to fill all receipt fields",
      "accepted_as_receipt": true
    }
  ],
  "accepted_source_statuses": [
    "primary_official_manuscript",
    "primary_official_lecture_or_video",
    "primary_official_transcript",
    "primary_author_derivation_cell"
  ],
  "minimum_locator_fields": [
    "source_id",
    "source_kind",
    "source_status",
    "primary_url_or_repo_path",
    "timestamp_or_page_or_equation_locator",
    "exact_context",
    "transcript_or_manuscript_fragment",
    "receipt_kind",
    "emitted_formula_or_derivation_cell",
    "extractor_notes"
  ],
  "required_formula_symbol_fields": [
    "domain_0_1",
    "codomain_0_1",
    "D_GU_epsilon_formula",
    "principal_symbol_sigma_1",
    "a_coefficient",
    "b_coefficient",
    "lambda_d",
    "Phi_2",
    "Phi_d",
    "F_xi",
    "Phi_F",
    "Q_in",
    "Q_out",
    "chirality_convention",
    "coordinate_convention",
    "extra_first_order_terms",
    "lower_order_terms",
    "normalization_policy"
  ],
  "typed_spine_policy": {
    "status": "comparison_material_only",
    "accepted_uses": [
      "candidate_shape",
      "field_checklist",
      "comparison_target_after_source_extraction",
      "rollback_trigger_when_actual_source_differs"
    ],
    "rejected_uses": [
      "primary_source_receipt",
      "actual_operator_identification",
      "source_derived_coefficient_proof",
      "FC_VZ_closure_for_actual_D_GU"
    ]
  },
  "rejection_conditions": [
    "typed_spine_only",
    "transcript_hint_only",
    "reconstruction_algebra_only",
    "conditional_VZ_backend_only",
    "media_summary_without_exact_formula",
    "community_transcript_without_primary_video_check_for_formula_claim",
    "operator_formula_absent",
    "actual_0_1_block_absent",
    "domain_or_codomain_absent",
    "principal_symbol_absent_or_not_computable",
    "a_b_lambda_d_not_source_derived",
    "Phi_d_and_Phi_F_conflated",
    "F_xi_derived_from_zero_order_Phi_F",
    "Q_in_Q_out_missing",
    "chirality_convention_missing",
    "coordinate_convention_missing_or_switched",
    "extra_first_order_terms_unlisted",
    "typed_spine_used_as_primary_source",
    "receipt_claim_depends_on_target_VZ_success"
  ],
  "strongest_positive_packet": {
    "candidate_id": "D_roll_typed_spine_candidate",
    "candidate_status": "coherent_candidate_not_receipt",
    "candidate_formula": "D_roll^epsilon(u,psi)=(d_A^* psi,d_A u + lambda_d Phi_2(d_A psi)) + Z_A^epsilon(u,psi)",
    "candidate_principal_symbol": "sigma_1(D_roll^epsilon)(xi)(u,psi)=(i_xi psi,xi tensor u + lambda_d F_xi psi)",
    "packet_use": "source_mining_template_and_comparison_target_only"
  },
  "source_first_sequence": [
    "primary_source_locator",
    "exact_source_fragment_or_derivation_cell",
    "emitted_actual_0_1_operator",
    "source_derived_symbol_and_fields",
    "comparison_to_typed_spine",
    "receipt_acceptance_decision",
    "ActualDGU01OperatorCertificateInstance_V1_gate"
  ],
  "nonclaims": {
    "actual_D_GU_operator_identification": false,
    "DGU01OperatorSourceReceipt_V1_accepted": false,
    "ActualDGU01OperatorCertificateInstance_V1_opened": false,
    "FC_VZ_1_for_actual_D_GU_closed": false,
    "FC_VZ_4_for_actual_section_pulled_operator_closed": false,
    "VZ_evasion_claimed": false,
    "hyperbolicity_claimed": false,
    "causality_claimed": false,
    "absence_of_spacelike_characteristics_claimed": false
  },
  "receipt_schema": [
    "receipt_id",
    "source_id",
    "source_kind",
    "source_status",
    "locator",
    "receipt_kind",
    "exact_fragment",
    "emitted_actual_operator_formula",
    "domain_0_1",
    "codomain_0_1",
    "principal_symbol_sigma_1",
    "coefficients_a_b_lambda_d",
    "order_split_Phi_2_Phi_d_F_xi_Phi_F",
    "projectors_Q_in_Q_out",
    "chirality_convention",
    "coordinate_convention",
    "extra_first_order_terms",
    "lower_order_terms",
    "comparison_to_D_roll",
    "acceptance_decision",
    "rollback_conditions_triggered",
    "nonclaims",
    "next_gate"
  ],
  "next_step": [
    "search_primary_official_GU_sources_for_action_operator_EL_formula",
    "record_locator_and_exact_fragment",
    "extract_actual_0_1_operator_before_comparison",
    "compute_sigma_1_from_extracted_formula",
    "fill_coefficients_order_split_projectors_chirality_coordinates_extra_terms",
    "apply_rejection_conditions",
    "emit_DGU01OperatorSourceReceipt_V1_only_if_accepted",
    "open_ActualDGU01OperatorCertificateInstance_V1_only_after_receipt_acceptance"
  ]
}
```
