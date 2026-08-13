---
title: "Hourly 20260625 0103 Cycle 1 QFT Single-Mode Source Extraction Certificate"
date: "2026-06-25"
status: exploration/certificate_attempt
doc_type: qft_single_mode_source_extraction_certificate
verdict: "BLOCKED_AT_MISSING_SOURCE_PROJECTOR_P_FIN_B"
owned_path: "explorations/hourly-20260625-0103-cycle1-qft-single-mode-source-extraction-certificate.md"
companion_audit:
  - "tests/hourly_20260625_0103_cycle1_qft_single_mode_source_extraction_audit.py"
depends_on:
  - "RESEARCH-POSTURE.md"
  - "process/runbooks/five-lane-frontier-run.md"
  - "explorations/hourly-cycle3-qft-source-mode-packet-validator-2026-06-25.md"
  - "explorations/hourly-cycle2-qft-effect-typed-source-mode-packet-2026-06-25.md"
  - "explorations/hourly-cycle2-qft-source-mode-quotient-data-ledger-2026-06-24.md"
  - "explorations/mission-a-qft-state-space-extraction-2026-06-24.md"
---

# Hourly 20260625 0103 Cycle 1 QFT Single-Mode Source Extraction Certificate

## 1. Verdict

Verdict: **blocked**.

This artifact attempts the one-mode pilot promised by the QFT source-mode packet
validator:

```text
SingleModeSourceExtractionCertificate_V1
sector_id = QFT-SSX-PS-LR-QUASIFREE-v0
intended_slot = V_L[1] inside K_b = V_L direct_sum V_R
```

The pilot does not construct a raw source representative, physical source
representative, local support proof, local algebra inclusion, `P_fin^b` image,
or final effect/projection/finality/loss record. Current repo sources name the
target representation carrier and specify the packet gate, but they do not
supply the first required extraction map:

```text
P_fin^b: F_phys^b(O) -> K_b
```

with `gu-derived:` provenance. The exact first obstruction is therefore:

```text
missing_source_projector_P_fin_b_for_single_mode_extraction
```

The block occurs before any honest claim that `V_L[1]` is occupied by a local
physical source mode. Ordinary Pati-Salam labels, identity Gram data, Bell
states, Pauli controls, free vacua, target-fitted covariances, and CHSH fixtures
are not source representatives for this certificate.

## 2. What Was Derived Directly From Repo Sources

`RESEARCH-POSTURE.md` supplies the governing rule: pursue GU reconstruction
constructively, but do not call compatibility a derivation and do not hide target
data inside the reconstruction.

`process/runbooks/five-lane-frontier-run.md` supplies the lane discipline:
produce a decision-grade artifact, identify the first exact obstruction, and
avoid overclaiming beyond the named source files.

`hourly-cycle3-qft-source-mode-packet-validator-2026-06-25.md` supplies the
validator order and the one-mode pilot request. It establishes that a packet can
only be admitted after `P_fin^b` exists, has `gu-derived:` provenance, and local
mode records carry raw representatives, images in `K_b`, local evidence,
provenance, and effect/projection/finality/loss statuses.

`hourly-cycle2-qft-effect-typed-source-mode-packet-2026-06-25.md` supplies the
effect-typed packet contract:

```text
EffectTypedSourceProjectorPFinBWithLocalModeRecords
```

and the allowed effect, projection, finality, and loss status vocabularies.

`hourly-cycle2-qft-source-mode-quotient-data-ledger-2026-06-24.md` supplies the
finite carrier and dependency order:

```text
K_b = V_L direct_sum V_R
V_L = (4,2,1),      dim_C V_L = 8
V_R = (4bar,1,2),  dim_C V_R = 8
dim_C K_b = 16

P_fin^b plus local source mode records
  -> H_raw
  -> removed representatives R_b
  -> Q_b
  -> H_phys = Q_b^* H_raw Q_b
```

It also records that `P_fin^b`, the local records, `H_raw`, `R_b`, `Q_b`, and
positivity certificates are missing from current sources.

`mission-a-qft-state-space-extraction-2026-06-24.md` supplies the broader
state-space context: positive physical pairing, two-point state, GNS state,
finite `rho_AB`, admissible observables, and CHSH are downstream gates. None of
them may be imported into the source-mode slot.

The direct one-mode supply table is:

| one-mode field | current status for `V_L[1]` |
|---|---|
| `sector_id` | available as `QFT-SSX-PS-LR-QUASIFREE-v0` |
| `K_b` carrier | available as representation carrier only |
| intended slot | selectable as label `V_L[1]` |
| exact base field | acceptable only as symbolic-exact shell; no matrix data supplied |
| `source_projector_P_fin_b` | missing |
| projector provenance | missing |
| raw representative | not reachable before `P_fin^b` |
| physical representative | not reachable before `P_fin^b` |
| local support/local algebra inclusion | not reachable before source representative |
| image in `K_b` | not source-certified |
| gu-derived provenance | missing for the mode |
| source operator/section/constraint reference | missing for the mode |
| target import flag | must remain false; no imported source substituted |
| effect status | unassigned because no source mode exists |
| projection status | unassigned because no source mode exists |
| finality status | unassigned because no source mode exists |
| loss status | unassigned because no source mode exists |
| positive finite seed | not promoted |
| covariance, `rho_AB`, CHSH | not promoted |

## 3. The Strongest Positive Result

The strongest positive result is a well-typed **single-slot extraction shell**:

```text
pilot_id:
  single_mode_source_extraction_certificate_v1_for_QFT_SSX_PS_LR_QUASIFREE_v0_V_L_1

sector_id:
  QFT-SSX-PS-LR-QUASIFREE-v0

carrier:
  K_b = V_L direct_sum V_R
  V_L = (4,2,1), dim_C V_L = 8
  V_R = (4bar,1,2), dim_C V_R = 8
  dim_C K_b = 16

intended_slot:
  representation_slot = V_L
  slot_index = 1
```

This is not a source mode. It is only a target slot in the representation
carrier that a future GU-derived source extraction map would have to hit.

The validator reaches these steps for the shell:

| validator step | result |
|---|---|
| 1. sector id | passes by repo label |
| 2. carrier is `K_b` with `8 + 8` split | passes as representation carrier |
| 3. exact base field | treated as symbolic-exact shell only; no numerical source matrix data supplied |
| 4. `source_projector_P_fin_b` exists | blocks |

No later step can be honestly evaluated for the one-mode pilot. In particular,
the certificate cannot test local support, local algebra inclusion, effect
typing, projection status, finality status, loss status, raw Gram data, quotient
compatibility, positivity, covariance, `rho_AB`, or CHSH.

## 4. The First Exact Obstruction Or Missing Proof Object

The first exact obstruction is:

```text
P_fin^b: F_phys^b(O) -> K_b
```

with source-level provenance:

```text
gu-derived:<operator/section/constraint/extraction-rule>
```

For the selected one-mode pilot, this means the missing proof object is:

```text
SingleModePFinBImageCertificate(V_L[1]):
  domain_element:
    raw_or_physical_representative in F_raw^b(O) or F_phys^b(O)
  local_evidence:
    local support in O or inclusion in A_b(O)
  extraction:
    P_fin^b(domain_element) = basis vector or exact coordinate in V_L[1]
  provenance:
    gu-derived source operator/section/constraint reference
```

The current repo does not supply any of those fields. This is first because the
repo can name `K_b` and choose the intended slot, but it cannot say which local
physical source mode maps to that slot. A `V_L[1]` label by itself is not a raw
representative, not a physical representative, not a local observable input, and
not a source-mode image.

This block is earlier than:

```text
raw_representative
physical_representative
local_support_or_local_algebra_inclusion
effect_type
projection_status
finality_status
loss_status
H_raw
R_b
Q_b
H_phys
positivity_certificate
source_covariance
rho_AB
CHSH
```

## 5. The Constructive Next Object That Would Remove Or Test The Obstruction

The constructive next object is a one-mode extraction witness:

```text
SingleModePFinBImageCertificate_V1
```

It must emit:

```text
sector_id:
  QFT-SSX-PS-LR-QUASIFREE-v0

selected_slot:
  V_L[1]

source_projector_P_fin_b:
  domain: F_phys^b(O)
  codomain: K_b
  exact extraction rule or exact map data
  provenance: gu-derived:<operator/section/constraint/extraction-rule>

mode_record:
  raw_representative or physical_representative
  local support or local algebra inclusion
  exact image in K_b occupying V_L[1]
  source operator/section/constraint reference
  target_import_flag = false
  effect_type
  projection_status
  finality_status
  loss_status
```

A successful one-mode witness would only show that the source extraction
mechanism can inhabit one intended slot. It would not promote a positive finite
seed. The seed gate still needs all 16 local mode records, `H_raw`, removed
representatives, `Q_b`, exact quotient compatibility, and an exact nonzero PSD
certificate for `H_phys`.

## 6. What This Means For The Relevant GU Claim

The relevant GU claim remains open but blocked at source extraction:

```text
QFT source-mode recovery branch:
  open
  not refuted by this artifact
  not promoted by this artifact
  blocked before one certified local source mode is available
```

The repo currently hosts the intended representation carrier and has a precise
validator for a future packet. It does not derive the finite source projector,
one local source representative, a local algebra inclusion, a physical pairing,
a covariance, a density matrix, admissible observables, or a Bell/CHSH
violation.

If GU is correct along this branch, a `P_fin^b` extraction rule should be
constructible from the physical field complex, section/localization data,
constraints, and quotient/effect typing. If every candidate extraction for
`V_L[1]` requires importing ordinary labels, identity metrics, free-vacuum data,
Bell states, Pauli settings, or CHSH targets, this branch should be demoted to
control plumbing for this gate.

## 7. Next Meaningful Proof Or Computation Step

Attempt one exact local extraction record before any 16-mode Gram computation:

```text
1. Fix a source branch b, observer region O, section, and physical field complex.
2. Define or refute P_fin^b: F_phys^b(O) -> K_b with gu-derived provenance.
3. Produce one raw or physical representative f_1 for V_L[1].
4. Prove local support in O or local algebra inclusion for f_1.
5. Compute P_fin^b(f_1) exactly and show it occupies V_L[1].
6. Attach source operator/section/constraint provenance.
7. Assign effect_type, projection_status, finality_status, and loss_status.
8. Run the validator through the one-mode fields only.
```

The result should be one of:

| outcome | meaning |
|---|---|
| `closed_single_mode_source_extraction_only` | one source mode is inhabited; continue to 16-mode packet |
| `blocked_missing_P_fin_b` | no extraction map yet |
| `blocked_missing_representative` | extractor exists but no local source representative is supplied |
| `fail_locality` | representative is not local or not in the local algebra |
| `import_control` | source data came from target labels, identity Gram, Bell/Pauli/free-vacuum/CHSH fixtures, or ordinary Pati-Salam labels |

## 8. Machine-Readable JSON Summary

```json
{
  "artifact": "SingleModeSourceExtractionCertificate_V1",
  "run_id": "hourly-20260625-0103",
  "cycle": 1,
  "lane": 3,
  "sector_id": "QFT-SSX-PS-LR-QUASIFREE-v0",
  "verdict": "BLOCKED_AT_MISSING_SOURCE_PROJECTOR_P_FIN_B",
  "status": "blocked",
  "one_mode_pilot_attempted": true,
  "selected_slot": {
    "representation_slot": "V_L",
    "slot_index": 1,
    "slot_label": "V_L[1]",
    "role": "intended_target_slot_only"
  },
  "carrier": {
    "formula": "K_b=V_L direct_sum V_R",
    "V_L": "(4,2,1)",
    "V_R": "(4bar,1,2)",
    "dim_C_V_L": 8,
    "dim_C_V_R": 8,
    "dim_C_K_b": 16,
    "status": "representation_carrier_only"
  },
  "derived_directly_from_sources": [
    "Mission_A_posture_and_no_target_smuggling_guardrails",
    "five_lane_decision_grade_worker_contract",
    "Cycle3_validator_promises_single_mode_pilot",
    "Cycle3_validator_requires_source_projector_before_mode_admission",
    "Cycle2_packet_contract_EffectTypedSourceProjectorPFinBWithLocalModeRecords",
    "Cycle2_quotient_ledger_requires_P_fin_b_and_16_local_source_records",
    "K_b_as_16_dimensional_Pati_Salam_LR_representation_carrier",
    "H_phys_equals_Q_star_H_raw_Q_formal_equation_only",
    "Mission_A_places_covariance_rho_AB_and_CHSH_downstream"
  ],
  "validator_steps_reached": [
    {
      "step": 1,
      "check": "sector_id_matches_QFT_SSX_PS_LR_QUASIFREE_v0",
      "result": "pass"
    },
    {
      "step": 2,
      "check": "carrier_is_16_dimensional_K_b_with_8_plus_8_split",
      "result": "pass_as_representation_carrier"
    },
    {
      "step": 3,
      "check": "base_field_is_exact",
      "result": "symbolic_exact_shell_only_no_source_matrix_data"
    },
    {
      "step": 4,
      "check": "source_projector_P_fin_b_exists_from_F_phys_b_O_to_K_b",
      "result": "blocked"
    }
  ],
  "validator_first_block_step": 4,
  "one_mode_required_fields": [
    "sector_id",
    "carrier",
    "selected_slot",
    "source_projector_P_fin_b",
    "projector_gu_derived_provenance",
    "raw_representative_or_physical_representative",
    "local_support_or_local_algebra_inclusion",
    "image_in_K_b",
    "mode_gu_derived_provenance",
    "source_operator_or_section_reference",
    "target_import_flag_false",
    "effect_type",
    "projection_status",
    "finality_status",
    "loss_status"
  ],
  "one_mode_field_status": {
    "sector_id": "available",
    "carrier": "available_as_representation_carrier_only",
    "selected_slot": "available_as_intended_label_only",
    "source_projector_P_fin_b": "missing",
    "projector_gu_derived_provenance": "missing",
    "raw_representative_or_physical_representative": "not_reachable_before_P_fin_b",
    "local_support_or_local_algebra_inclusion": "not_reachable_before_source_representative",
    "image_in_K_b": "not_source_certified",
    "mode_gu_derived_provenance": "missing",
    "source_operator_or_section_reference": "missing",
    "target_import_flag_false": true,
    "effect_type": "unassigned_no_source_mode",
    "projection_status": "unassigned_no_source_mode",
    "finality_status": "unassigned_no_source_mode",
    "loss_status": "unassigned_no_source_mode"
  },
  "allowed_effect_types": [
    "source_mode",
    "quotient_constraint",
    "local_observer_input",
    "pairing_input",
    "covariance_input_candidate",
    "observable_input_candidate"
  ],
  "allowed_projection_statuses": [
    "raw",
    "projected",
    "quotient_survivor",
    "quotient_removed"
  ],
  "allowed_finality_statuses": [
    "final",
    "provisional",
    "killed_by_EOM",
    "killed_by_gauge",
    "killed_by_constraint",
    "killed_by_ghost",
    "killed_by_null",
    "unresolved"
  ],
  "allowed_loss_statuses": [
    "no_loss",
    "quotient_removed",
    "locality_lost",
    "positivity_lost",
    "provenance_lost",
    "tensor_factorization_not_supplied",
    "observable_admissibility_not_supplied"
  ],
  "first_exact_obstruction": {
    "id": "missing_source_projector_P_fin_b_for_single_mode_extraction",
    "formal_name": "P_fin^b_from_F_phys_b_O_to_K_b_with_gu_derived_provenance",
    "validator_step": 4,
    "current_status": "missing",
    "why_first": [
      "sector_id_can_be_named_from_current_sources",
      "K_b_and_V_L_1_can_be_named_as_representation_labels",
      "no_current_source_supplies_a_map_from_F_phys_b_O_to_K_b",
      "without_P_fin_b_V_L_1_is_not_certified_as_an_image_of_a_local_physical_source_mode"
    ],
    "blocks_fields": [
      "raw_representative_or_physical_representative",
      "local_support_or_local_algebra_inclusion",
      "image_in_K_b",
      "mode_gu_derived_provenance",
      "effect_type",
      "projection_status",
      "finality_status",
      "loss_status"
    ]
  },
  "constructive_next_object": {
    "id": "SingleModePFinBImageCertificate_V1",
    "selected_slot": "V_L[1]",
    "must_emit": [
      "P_fin_b_from_F_phys_b_O_to_K_b",
      "gu_derived_projector_provenance",
      "raw_or_physical_representative",
      "local_support_or_local_algebra_inclusion",
      "exact_image_in_K_b_occupying_V_L_1",
      "source_operator_section_constraint_reference",
      "target_import_flag_false",
      "effect_type",
      "projection_status",
      "finality_status",
      "loss_status"
    ],
    "does_not_promote_by_itself": [
      "PositiveFiniteOneParticleSeed_K_b",
      "quasifree_covariance",
      "QFT_state",
      "rho_AB",
      "CHSH_violation",
      "Bell_violation"
    ]
  },
  "forbidden_imports": [
    "ordinary_Pati_Salam_labels_as_source_data",
    "identity_Gram_as_GU_derivation",
    "Bell_state_as_GU_state",
    "Pauli_controls_as_GU_observables",
    "standard_free_vacuum_as_GU_source",
    "Hadamard_or_Fock_vacuum_as_GU_source",
    "target_fitted_covariance_or_CHSH_state",
    "direct_sum_K_b_as_tensor_product_rho_AB_without_reduction_map",
    "ordinary_SM_labels_as_physical_Gram"
  ],
  "positive_promotions": {
    "single_mode_source_extraction_closed": false,
    "sixteen_mode_packet_admitted": false,
    "positive_finite_seed_promoted": false,
    "qft_recovered": false,
    "covariance_promoted": false,
    "rho_AB_supplied": false,
    "chsh_promoted": false,
    "bell_violation_claimed": false,
    "positivity_closure_claimed": false
  },
  "impact_on_GU_claim": "QFT_source_mode_recovery_branch_open_but_blocked_before_one_certified_local_source_mode",
  "next_meaningful_step": "Construct_or_refute_SingleModePFinBImageCertificate_V1_for_V_L_1"
}
```
