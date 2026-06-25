---
title: "Hourly Cycle 3 QFT Source-Mode Packet Validator"
date: "2026-06-25"
status: exploration/validator
doc_type: qft_source_mode_packet_validator
verdict: "BLOCKED_NO_CURRENT_EFFECT_TYPED_SOURCE_MODE_PACKET_RECORD"
owned_path: "explorations/hourly-cycle3-qft-source-mode-packet-validator-2026-06-25.md"
companion_audit:
  - "tests/hourly_cycle3_qft_source_mode_packet_validator_audit.py"
depends_on:
  - "RESEARCH-POSTURE.md"
  - "process/runbooks/five-lane-frontier-run.md"
  - "explorations/hourly-cycle2-qft-effect-typed-source-mode-packet-2026-06-25.md"
  - "explorations/hourly-cycle1-effect-typed-witness-qft-modes-2026-06-25.md"
  - "explorations/hourly-cycle2-qft-source-mode-quotient-data-ledger-2026-06-24.md"
---

# Hourly Cycle 3 QFT Source-Mode Packet Validator

## 1. Verdict

Verdict: **blocked**.

This artifact specifies `EffectTypedSourceModePacketValidator_V1`, a decision-grade
validator for effect-typed QFT source-mode packets over the current Pati-Salam left/right
finite carrier

```text
K_b = V_L direct_sum V_R
V_L = (4,2,1),      dim_C V_L = 8
V_R = (4bar,1,2),  dim_C V_R = 8
dim_C K_b = 16.
```

The validator can accept a future packet only far enough to promote:

```text
PositiveFiniteOneParticleSeed(K_b)
```

It does not promote QFT recovery, covariance, `rho_AB`, CHSH, Bell violation, positive
finite seed, or positivity closure from current sources.

When the validator is run conceptually against current repo supply, no acceptable packet
record exists. The strongest positive construction is a well-typed packet shell plus
exact decision table. The first exact obstruction is:

```text
source_projector_P_fin_b is absent, so no record can be admitted as an effect-typed
QFT source-mode packet.
```

This obstruction occurs before checking the 16 local mode records, `H_raw`, removed
representatives, `Q_b`, quotient compatibility, or positivity.

## 2. What Was Derived Directly From Repo Sources

`RESEARCH-POSTURE.md` supplies the governing research discipline: pursue the GU
reconstruction constructively, but do not call compatibility a derivation and do not hide
target data inside a reconstruction.

`process/runbooks/five-lane-frontier-run.md` supplies the worker standard: make a
decision-grade artifact, identify the first exact obstruction, and avoid overclaiming
beyond the named sources.

`hourly-cycle2-qft-source-mode-quotient-data-ledger-2026-06-24.md` supplies the finite
carrier, the formal quotient-Gram equation, and the source-mode ledger requirement:

```text
P_fin^b: F_phys^b(O) -> K_b
exactly 16 local gu-derived source records
H_phys = Q_b^* H_raw Q_b
```

It also records that `P_fin^b`, the 16 local mode records, `H_raw`, removed
representatives, `Q_b`, and positivity certificate are missing.

`hourly-cycle1-effect-typed-witness-qft-modes-2026-06-25.md` refines the missing source
object by requiring effect type, projection status, finality status, and loss status
before finite witness transport can be promoted.

`hourly-cycle2-qft-effect-typed-source-mode-packet-2026-06-25.md` specifies the packet
contract named:

```text
EffectTypedSourceProjectorPFinBWithLocalModeRecords
```

It decides that the contract is specified but uninhabited by current sources. It also
sets the key downstream guardrail: even a clean accepted packet promotes only a positive
finite one-particle seed, not covariance, a QFT state, `rho_AB`, or CHSH.

The direct repo-derived supply table is therefore:

| item | current repo status |
|---|---|
| `sector_id` | named as `QFT-SSX-PS-LR-QUASIFREE-v0` |
| `K_b` | named 16-dimensional representation carrier |
| `P_fin^b` | required and absent |
| 16 local mode records | required and absent |
| effect/projection/finality/loss fields | required by contract, absent as records |
| local support/local algebra evidence | required and absent |
| `H_raw` | required and absent |
| removed representatives | required and absent |
| `Q_b` | required and absent |
| `H_phys` | formal equation only, not computable |
| exact positivity certificate | required and absent |
| covariance, `rho_AB`, CHSH | downstream and not supplied |

## 3. Strongest Positive Construction Attempt

The strongest positive construction is the validator itself. It has two layers:

1. a packet-admission layer that decides whether a candidate is a source packet, an
   import/control, a failed packet, or blocked by missing data;
2. a finite-seed layer that runs only after packet admission and can promote only a
   positive finite one-particle seed.

### Validator Inputs

`EffectTypedSourceModePacketValidator_V1` expects a candidate packet with these top-level
fields:

```text
packet_id
sector_id
carrier
base_field
source_projector_P_fin_b
local_mode_records
raw_Gram_H_raw
removed_representatives_R_b
Q_b
quotient_compatibility
H_phys
forbidden_import_screen
decision_log
```

The packet must declare:

```text
sector_id = QFT-SSX-PS-LR-QUASIFREE-v0
carrier = K_b=V_L direct_sum V_R
V_L = (4,2,1), dim_C V_L = 8
V_R = (4bar,1,2), dim_C V_R = 8
dim_C K_b = 16
```

Each local mode record must contain:

```text
mode_id
label
raw_representative
image_in_K_b
representation_slot in {V_L, V_R}
slot_index in {1,...,8}
local_support_or_local_algebra_inclusion
gu_derived_provenance
source_operator_or_section_reference
target_import_flag = false
effect_type
projection_status
finality_status
loss_status
```

Allowed effect types:

```text
source_mode
quotient_constraint
local_observer_input
pairing_input
covariance_input_candidate
observable_input_candidate
```

Allowed projection statuses:

```text
raw
projected
quotient_survivor
quotient_removed
```

Allowed finality statuses:

```text
final
provisional
killed_by_EOM
killed_by_gauge
killed_by_constraint
killed_by_ghost
killed_by_null
unresolved
```

Allowed loss statuses:

```text
no_loss
quotient_removed
locality_lost
positivity_lost
provenance_lost
tensor_factorization_not_supplied
observable_admissibility_not_supplied
```

### Validator Steps

The validator runs in this exact order.

| step | check | decision on failure |
|---|---|---|
| 1 | `sector_id` is exactly `QFT-SSX-PS-LR-QUASIFREE-v0` | fail |
| 2 | carrier is the named 16-dimensional `K_b` with `8 + 8` split | fail |
| 3 | `base_field` is exact (`QQ`, `QQ_i`, number field, or symbolic exact) | blocked |
| 4 | `source_projector_P_fin_b` exists as `F_phys^b(O) -> K_b` | blocked |
| 5 | projector provenance begins `gu-derived:` and names operator/section/constraint data | import |
| 6 | exactly 16 local mode records exist | blocked |
| 7 | every mode has unique `(representation_slot, slot_index)` and covers `V_L[1..8]`, `V_R[1..8]` | fail |
| 8 | every mode has a raw representative and exact image in `K_b` | blocked |
| 9 | every mode has local support or local algebra inclusion | fail |
| 10 | every mode provenance begins `gu-derived:` and target import flag is false | import |
| 11 | every mode has valid effect, projection, finality, and loss status | blocked |
| 12 | forbidden import screen is clean | import |
| 13 | `H_raw` is exact `16 x 16`, Hermitian, and source-provenanced | blocked or fail |
| 14 | removed representatives cover `EOM_b`, `Gauge_b`, `Constraint_b`, `Ghost_b`, `Null_b`, or prove each empty | blocked |
| 15 | `Q_b` is exact `16 x r` and full-column-rank | blocked or fail |
| 16 | exact quotient compatibility `R_b^* H_raw Q_b = 0` holds | fail |
| 17 | `H_phys = Q_b^* H_raw Q_b` is computed exactly | fail |
| 18 | `H_phys` is Hermitian | fail |
| 19 | exact certificate proves `H_phys >= 0` | fail |
| 20 | exact certificate proves `rank(H_phys) > 0` | fail |
| 21 | accepted packet promotes only `PositiveFiniteOneParticleSeed(K_b)` | accept |

### Decision Vocabulary

The validator uses four operational outcomes:

```text
accept:
  all source, locality, quotient, and positivity checks pass; promote positive finite
  one-particle seed only

block:
  a required proof object or exact datum is absent

fail:
  supplied exact data contradict the required algebraic or structural check

import:
  supplied data enter from controls, target QFT/Bell fixtures, ordinary labels, or
  non-GU provenance instead of a gu-derived source path
```

### Strongest Positive Candidate Tried Today

The strongest current candidate is:

```text
sector_id = QFT-SSX-PS-LR-QUASIFREE-v0
carrier = K_b=(4,2,1) direct_sum (4bar,1,2), dim_C K_b=16
basis_label_pattern = e^L_{a alpha}, e^R_{bar a dot alpha}
```

That candidate reaches step 4 and blocks. It does not contain `P_fin^b`, so it is not a
source packet. Adding an identity Gram, empty removed representatives, identity `Q_b`, a
Bell state, Pauli controls, a standard free vacuum, or a fitted covariance would convert
the candidate into import/control data, not a GU-derived packet.

## 4. First Exact Obstruction Or Missing Proof Object

The first exact obstruction is:

```text
P_fin^b: F_phys^b(O) -> K_b
```

with `gu-derived:` provenance.

Why this is first:

```text
The validator can verify the named sector and carrier from current files.
The next required object is the finite source projector.
Current files require that projector but do not supply it.
Without the projector, the 16 representation slots cannot be certified as images of local
physical source modes.
```

The next checks cannot be reached honestly:

```text
exactly_16_local_mode_records
local_support_or_local_algebra_inclusion
effect_type/projection_status/finality_status/loss_status
H_raw
removed_representatives_R_b
Q_b
R_b^* H_raw Q_b = 0
H_phys = Q_b^* H_raw Q_b
H_phys >= 0
rank(H_phys) > 0
```

Therefore no current repo record is accepted. No current repo record fails at a later
matrix check, because no current repo record reaches the matrix stage as a source packet.

## 5. Constructive Next Object

The next constructive object is not another CHSH fixture. It is:

```text
EffectTypedSourceProjectorPFinBWithLocalModeRecords_V1
```

It must emit:

```text
source_projector_P_fin_b:
  domain: F_phys^b(O)
  codomain: K_b
  exact map data or extraction rule
  gu-derived provenance

local_mode_records:
  exactly 16 records
  one record for each V_L[1..8] and V_R[1..8] slot
  raw representative
  image in K_b
  local support or local algebra inclusion
  gu-derived provenance
  source operator/section/constraint reference
  target_import_flag = false
  effect_type
  projection_status
  finality_status
  loss_status
```

Only after that object exists should the repo attempt the raw Gram and quotient layer:

```text
H_raw
R_b with EOM_b/Gauge_b/Constraint_b/Ghost_b/Null_b roles
Q_b
R_b^* H_raw Q_b = 0
H_phys = Q_b^* H_raw Q_b
exact psd and nonzero-rank certificate
```

## 6. Impact On GU Claim

This validator sharpens the current GU reconstruction status without weakening the
Mission A posture.

Positive impact:

```text
The repo now has an exact acceptance/block/fail/import procedure for QFT source-mode
packets in the K_b sector.
```

Current limitation:

```text
The validator finds no accepted packet in current repo supply.
```

Meaning for the GU claim:

```text
The QFT source-mode recovery branch remains open but blocked at source extraction.
The current sources host the intended finite carrier and specify the packet gate.
They do not derive the finite source projector, local source modes, positive physical
pairing, covariance, density matrix, or Bell/CHSH violation.
```

If GU is correct along this branch, the missing object should be constructible from the
physical field complex, source-local algebra, and quotient/effect typing data. If that
object cannot be constructed without importing target QFT or Bell fixtures, this branch
should be demoted or refuted at the source-mode packet gate.

## 7. Next Meaningful Proof/Computation Step

Build the minimal source extraction record for one local mode first, then generalize to
all 16 slots.

The immediate next proof/computation step is:

```text
SingleModeSourceExtractionCertificate:
  choose one intended slot, for example V_L[1]
  construct a raw representative in F_raw^b(O) or a physical representative in F_phys^b(O)
  prove local support or local algebra inclusion
  map it through a candidate P_fin^b into the selected K_b slot
  attach gu-derived provenance and effect/projection/finality/loss statuses
  run the validator through steps 1-11 for that one-mode pilot
```

A successful one-mode pilot would not promote a finite seed. It would only test whether
the currently missing source extraction mechanism exists. The 16-mode packet and matrix
quotient/positivity stages should follow only after the pilot has real source
inhabitants.

## 8. Machine-Readable JSON Summary

```json
{
  "artifact": "EffectTypedSourceModePacketValidator_V1",
  "verdict": "BLOCKED_NO_CURRENT_EFFECT_TYPED_SOURCE_MODE_PACKET_RECORD",
  "status": "blocked",
  "validator_specified": true,
  "packet_record_exists_in_current_repo_supply": false,
  "accepted_packet_exists": false,
  "positive_seed_promoted": false,
  "qft_recovered": false,
  "covariance_promoted": false,
  "rho_AB_supplied": false,
  "chsh_promoted": false,
  "bell_violation_claimed": false,
  "positivity_closure_claimed": false,
  "not_a_chsh_or_qft_recovery_claim": true,
  "K_b": {
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
    "Cycle2_packet_contract_EffectTypedSourceProjectorPFinBWithLocalModeRecords",
    "Cycle1_effect_projection_finality_loss_typing_requirement",
    "K_b_as_16_dimensional_Pati_Salam_LR_representation_carrier",
    "P_fin_b_and_16_local_modes_are_required",
    "H_phys_equals_Q_star_H_raw_Q_formal_equation",
    "H_raw_removed_representatives_Q_b_and_H_phys_positivity_are_missing",
    "current_contract_is_specified_but_uninhabited",
    "CHSH_Bell_covariance_and_rho_AB_are_not_promoted_from_current_sources"
  ],
  "validator_inputs": [
    "packet_id",
    "sector_id",
    "carrier",
    "base_field",
    "source_projector_P_fin_b",
    "local_mode_records",
    "raw_Gram_H_raw",
    "removed_representatives_R_b",
    "Q_b",
    "quotient_compatibility",
    "H_phys",
    "forbidden_import_screen",
    "decision_log"
  ],
  "mode_record_fields": [
    "mode_id",
    "label",
    "raw_representative",
    "image_in_K_b",
    "representation_slot",
    "slot_index",
    "local_support_or_local_algebra_inclusion",
    "gu_derived_provenance",
    "source_operator_or_section_reference",
    "target_import_flag_false",
    "effect_type",
    "projection_status",
    "finality_status",
    "loss_status"
  ],
  "effect_types": [
    "source_mode",
    "quotient_constraint",
    "local_observer_input",
    "pairing_input",
    "covariance_input_candidate",
    "observable_input_candidate"
  ],
  "projection_statuses": [
    "raw",
    "projected",
    "quotient_survivor",
    "quotient_removed"
  ],
  "finality_statuses": [
    "final",
    "provisional",
    "killed_by_EOM",
    "killed_by_gauge",
    "killed_by_constraint",
    "killed_by_ghost",
    "killed_by_null",
    "unresolved"
  ],
  "loss_statuses": [
    "no_loss",
    "quotient_removed",
    "locality_lost",
    "positivity_lost",
    "provenance_lost",
    "tensor_factorization_not_supplied",
    "observable_admissibility_not_supplied"
  ],
  "validator_steps": [
    {
      "step": 1,
      "check": "sector_id_matches_QFT_SSX_PS_LR_QUASIFREE_v0",
      "failure_decision": "fail"
    },
    {
      "step": 2,
      "check": "carrier_is_16_dimensional_K_b_with_8_plus_8_split",
      "failure_decision": "fail"
    },
    {
      "step": 3,
      "check": "base_field_is_exact",
      "failure_decision": "blocked"
    },
    {
      "step": 4,
      "check": "source_projector_P_fin_b_exists_from_F_phys_b_O_to_K_b",
      "failure_decision": "blocked"
    },
    {
      "step": 5,
      "check": "P_fin_b_has_gu_derived_provenance",
      "failure_decision": "import"
    },
    {
      "step": 6,
      "check": "exactly_16_local_mode_records_exist",
      "failure_decision": "blocked"
    },
    {
      "step": 7,
      "check": "mode_slots_uniquely_cover_V_L_1_to_8_and_V_R_1_to_8",
      "failure_decision": "fail"
    },
    {
      "step": 8,
      "check": "every_mode_has_raw_representative_and_exact_image_in_K_b",
      "failure_decision": "blocked"
    },
    {
      "step": 9,
      "check": "every_mode_has_local_support_or_local_algebra_inclusion",
      "failure_decision": "fail"
    },
    {
      "step": 10,
      "check": "every_mode_has_gu_derived_provenance_and_no_target_import",
      "failure_decision": "import"
    },
    {
      "step": 11,
      "check": "every_mode_has_valid_effect_projection_finality_and_loss_status",
      "failure_decision": "blocked"
    },
    {
      "step": 12,
      "check": "forbidden_import_screen_is_clean",
      "failure_decision": "import"
    },
    {
      "step": 13,
      "check": "H_raw_is_exact_16_by_16_Hermitian_and_source_provenanced",
      "failure_decision": "blocked_or_fail"
    },
    {
      "step": 14,
      "check": "removed_representatives_cover_EOM_Gauge_Constraint_Ghost_Null_or_prove_empty",
      "failure_decision": "blocked"
    },
    {
      "step": 15,
      "check": "Q_b_is_exact_16_by_r_and_full_column_rank",
      "failure_decision": "blocked_or_fail"
    },
    {
      "step": 16,
      "check": "R_star_H_raw_Q_equals_zero_exactly",
      "failure_decision": "fail"
    },
    {
      "step": 17,
      "check": "H_phys_equals_Q_star_H_raw_Q_exactly",
      "failure_decision": "fail"
    },
    {
      "step": 18,
      "check": "H_phys_is_Hermitian",
      "failure_decision": "fail"
    },
    {
      "step": 19,
      "check": "H_phys_has_exact_psd_certificate",
      "failure_decision": "fail"
    },
    {
      "step": 20,
      "check": "H_phys_has_positive_rank_certificate",
      "failure_decision": "fail"
    },
    {
      "step": 21,
      "check": "accepted_packet_promotes_positive_finite_one_particle_seed_only",
      "failure_decision": "none"
    }
  ],
  "decision_table": {
    "missing_sector_or_wrong_sector": "fail",
    "wrong_carrier_or_dimension": "fail",
    "missing_base_field": "blocked",
    "missing_P_fin_b": "blocked",
    "P_fin_b_lacks_gu_derived_provenance": "import",
    "not_exactly_16_local_mode_records": "blocked",
    "duplicate_or_missing_V_L_V_R_slot_indices": "fail",
    "missing_raw_representative_or_image": "blocked",
    "missing_local_support_or_local_algebra": "fail",
    "mode_provenance_not_gu_derived": "import",
    "missing_effect_projection_finality_or_loss_status": "blocked",
    "forbidden_target_string_supplies_source_data": "import",
    "missing_H_raw": "blocked",
    "H_raw_not_Hermitian": "fail",
    "removed_roles_absent_without_empty_role_proof": "blocked",
    "missing_Q_b": "blocked",
    "Q_b_not_full_column_rank": "fail",
    "R_star_H_raw_Q_nonzero": "fail",
    "H_phys_not_equal_Q_star_H_raw_Q": "fail",
    "H_phys_negative": "fail",
    "H_phys_rank_zero": "fail",
    "clean_H_phys_psd_nonzero_rank": "accept_positive_finite_one_particle_seed_only"
  },
  "forbidden_imports": [
    "identity_Gram_as_GU_derivation",
    "Bell_state_as_GU_state",
    "Pauli_controls_as_GU_observables",
    "standard_free_vacuum_as_GU_source",
    "Hadamard_or_Fock_vacuum_as_GU_source",
    "target_fitted_covariance_or_CHSH_state",
    "Stinespring_or_CPTP_channel_as_GU_source_without_derivation",
    "direct_sum_K_b_as_tensor_product_rho_AB_without_reduction_map",
    "ordinary_SM_or_Pati_Salam_labels_as_physical_Gram"
  ],
  "current_repo_supply_run": {
    "candidate": "strongest_current_carrier_and_basis_label_shell",
    "sector_id": "available",
    "carrier": "available_as_representation_carrier_only",
    "basis_label_pattern": "available_as_labels_only",
    "base_field": "missing",
    "source_projector_P_fin_b": "missing",
    "local_mode_records": "missing",
    "H_raw": "missing",
    "removed_representatives_R_b": "missing",
    "Q_b": "missing",
    "H_phys": "not_computable",
    "positivity_certificate": "missing",
    "first_obstruction_step": 4,
    "first_obstruction": "missing_source_projector_P_fin_b",
    "decision": "blocked",
    "accepted_record_exists": false
  },
  "first_exact_obstruction": {
    "id": "source_projector_P_fin_b",
    "formal_name": "P_fin^b_from_F_phys_b_O_to_K_b_with_gu_derived_provenance",
    "validator_step": 4,
    "current_status": "missing",
    "why_first": [
      "sector_id_and_K_b_can_be_named_from_current_sources",
      "P_fin_b_is_the_next_required_validator_object",
      "without_P_fin_b_the_16_slots_are_only_representation_labels_not_source_mode_images"
    ]
  },
  "constructive_next_object": {
    "id": "EffectTypedSourceProjectorPFinBWithLocalModeRecords_V1",
    "first_pilot": "SingleModeSourceExtractionCertificate",
    "must_emit": [
      "P_fin_b_from_F_phys_b_O_to_K_b",
      "gu_derived_projector_provenance",
      "exactly_16_mode_records",
      "raw_representatives",
      "images_in_K_b",
      "unique_V_L_and_V_R_slot_coverage",
      "local_support_or_local_algebra_inclusion",
      "source_operator_section_constraint_reference",
      "target_import_flag_false",
      "effect_type",
      "projection_status",
      "finality_status",
      "loss_status"
    ]
  },
  "impact_on_GU_claim": "QFT_source_mode_recovery_branch_open_but_blocked_at_source_extraction",
  "next_meaningful_step": "Build_SingleModeSourceExtractionCertificate_then_generalize_to_16_mode_packet"
}
```
