---
title: "Hourly Cycle 2 QFT Effect-Typed Source Mode Packet Contract"
date: "2026-06-25"
status: exploration/contract
doc_type: qft_effect_typed_source_mode_packet_contract
verdict: "UNDERDEFINED_PACKET_CONTRACT_SPECIFIED_BUT_UNINHABITED"
owned_path: "explorations/hourly-cycle2-qft-effect-typed-source-mode-packet-2026-06-25.md"
companion_audit:
  - "tests/hourly_cycle2_qft_effect_typed_source_mode_packet_audit.py"
depends_on:
  - "RESEARCH-POSTURE.md"
  - "process/runbooks/five-lane-frontier-run.md"
  - "explorations/hourly-cycle1-effect-typed-witness-qft-modes-2026-06-25.md"
  - "explorations/hourly-cycle2-qft-source-mode-quotient-data-ledger-2026-06-24.md"
  - "explorations/mission-a-qft-state-space-extraction-2026-06-24.md"
---

# Hourly Cycle 2 QFT Effect-Typed Source Mode Packet Contract

## 1. Verdict

Verdict: **underdefined packet contract specified but uninhabited**.

This lane builds the decision-grade packet contract promised by Cycle 1:

```text
EffectTypedSourceProjectorPFinBWithLocalModeRecords
```

The contract is exact enough to accept or reject a future source packet for the
Pati-Salam left/right finite carrier

```text
K_b = V_L direct_sum V_R
V_L = (4,2,1),      dim_C V_L = 8
V_R = (4bar,1,2),  dim_C V_R = 8
dim_C K_b = 16.
```

The strongest positive construction is a validator/schema for the packet. It can promote
only the following conditional result:

```text
Clean accepted packet
  -> PositiveFiniteOneParticleSeed(K_b) only
```

It does not claim QFT recovery, covariance, rho_AB, CHSH, Bell violation, or positivity
closure. Current required repo sources do not inhabit the packet because they do not
supply `P_fin_b`, exactly 16 local source mode records, `H_raw`, removed representatives,
`Q_b`, or an exact positivity certificate for `H_phys`.

The first exact obstruction remains earlier than any Bell or covariance computation:

```text
No effect-typed source projector and 16 gu-derived local mode records exist in the
current source set.
```

## 2. What Was Derived Directly From Repo Sources

`RESEARCH-POSTURE.md` supplies the research posture: pursue the GU reconstruction
constructively, but do not call compatibility a derivation and do not hide target data
inside a reconstruction.

`process/runbooks/five-lane-frontier-run.md` supplies the decision standard: exact
obstruction, rollback conditions, scoped edits, and no overclaiming.

`hourly-cycle1-effect-typed-witness-qft-modes-2026-06-25.md` derives the interface-level
blocker:

```text
EffectTypedSourceProjectorPFinBWithLocalModeRecords
```

It also requires effect typing, projection status, finality status, and loss status before
quotient-Gram data may be promoted.

`hourly-cycle2-qft-source-mode-quotient-data-ledger-2026-06-24.md` supplies the finite
carrier and source-mode ledger dependency:

```text
P_fin_b: F_phys^b(O) -> K_b
exactly 16 local gu-derived source records
H_phys = Q_b^* H_raw Q_b
```

It marks `H_raw`, removed representatives, `Q_b`, and positivity as missing from current
sources.

`mission-a-qft-state-space-extraction-2026-06-24.md` establishes that even a positive
finite seed would be downstream of a positive physical pairing and two-point state before
GNS, finite `rho_AB`, admissible observables, or CHSH claims can be evaluated.

The direct repo-derived facts used here are therefore:

| object | direct status |
|---|---|
| `K_b` | named 16-dimensional representation carrier |
| `P_fin_b` | required source projector, absent |
| local mode records | exactly 16 required, absent |
| `gu-derived:` provenance | required for every record, absent |
| effect/projection/finality/loss fields | required by Cycle 1, absent as source data |
| `H_raw` | required raw Gram, absent |
| removed representatives | required for EOM/gauge/constraint/ghost/null roles, absent |
| `Q_b` | required quotient representative matrix, absent |
| `H_phys` | formal equation only, not computable |
| covariance, `rho_AB`, CHSH | not supplied and not promoted |

## 3. Strongest Positive Construction Attempt

The strongest positive object is a fully specified packet schema plus validator. A packet
is accepted only if all source, mode, projection, quotient, and positivity fields are
present with exact data and acceptable provenance.

### Packet Schema

```text
EffectTypedSourceProjectorPFinBWithLocalModeRecords:
  packet_id:
    effect_typed_source_projector_pfin_b_for_QFT_SSX_PS_LR_QUASIFREE_v0

  sector_id:
    QFT-SSX-PS-LR-QUASIFREE-v0

  carrier:
    formula: K_b=V_L direct_sum V_R
    V_L: (4,2,1)
    V_R: (4bar,1,2)
    dim_C_K_b: 16

  base_field:
    QQ | QQ_i | number_field | symbolic_exact

  source_projector_P_fin_b:
    domain: F_phys^b(O)
    codomain: K_b
    map_data: exact formula, matrix, or extraction rule
    provenance: gu-derived:<operator/section/constraint/reference>
    status: source_supplied

  local_mode_records:
    exactly 16 records
```

Each local mode record must have this schema:

```text
mode_record:
  mode_id: stable unique string
  label: human readable label
  raw_representative:
    source_space: F_raw^b(O) | Sol_raw^b(O) | F_phys^b(O)
    expression: exact source representative or source expression reference
  image_in_K_b:
    coordinates: exact 16-vector or exact basis coordinate reference
    representation_slot: V_L | V_R
    slot_index: 1..8 within the selected representation slot
  locality:
    local_support: explicit O-support statement
    local_algebra_inclusion: explicit A_b(O) inclusion or source-local proxy
  provenance:
    prefix: gu-derived:
    source_operator_or_section_reference: nonempty
    target_import_flag: false
  effect_type:
    one of allowed_effect_types
  projection_status:
    one of allowed_projection_statuses
  finality_status:
    one of allowed_finality_statuses
  loss_status:
    one of allowed_loss_statuses
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

The projection and positivity portion must have this schema:

```text
raw_Gram_H_raw:
  shape: 16 x 16
  entries: exact
  Hermitian: certified
  provenance: gu-derived:<physical pairing/current/reference>

removed_representatives_R_b:
  matrix: exact 16 x m matrix, possibly m=0
  columns:
    each has removed_id, role, exact_vector, provenance, empty_role_proof if empty
  required_roles:
    EOM_b
    Gauge_b
    Constraint_b
    Ghost_b
    Null_b

Q_b:
  shape: 16 x r
  entries: exact
  full_column_rank: certified
  provenance: gu-derived:<quotient representative rule/reference>

quotient_compatibility:
  check: R_b^* H_raw Q_b = 0
  status: exact_pass

H_phys:
  definition: Q_b^* H_raw Q_b
  entries: exact or computed_exactly_from_H_raw_and_Q_b
  Hermitian: certified
  positivity: exact_psd_certificate
  rank: positive integer
  rank_positive: true
```

### Acceptance Decisions

The packet is **accepted as `PositiveFiniteOneParticleSeed(K_b)` only** if all of the
following hold:

1. `sector_id` is `QFT-SSX-PS-LR-QUASIFREE-v0`.
2. `carrier.dim_C_K_b` is exactly 16 with `8 + 8` split as above.
3. `base_field` is exact, not floating point only.
4. `P_fin_b` maps `F_phys^b(O)` to `K_b` with `gu-derived:` provenance.
5. There are exactly 16 local mode records.
6. Every record has `gu-derived:` provenance and no target import flag.
7. Every record has local support or local algebra inclusion.
8. Every record has effect type, projection status, finality status, and loss status.
9. Each `V_L` and `V_R` representation slot has exactly 8 occupied slot indices.
10. `H_raw` is exact, 16 x 16, Hermitian, and source-provenanced.
11. Removed roles `EOM_b`, `Gauge_b`, `Constraint_b`, `Ghost_b`, and `Null_b` are each
    represented or source-proved empty.
12. `Q_b` is exact, 16 x r, and full column rank.
13. `R_b^* H_raw Q_b = 0` holds exactly.
14. `H_phys = Q_b^* H_raw Q_b` holds exactly.
15. `H_phys` is Hermitian, positive semidefinite, and nonzero rank by exact certificate.
16. The forbidden import screen is clean.

### Fail, Block, Import, And Promotion Decisions

| condition | decision |
|---|---|
| missing `P_fin_b` | blocked |
| `P_fin_b` lacks `gu-derived:` provenance | import |
| not exactly 16 local mode records | blocked |
| duplicate or missing `V_L`/`V_R` slot indices | fail_mode_slot_accounting |
| any mode lacks local support/local algebra inclusion | fail_local_observer_input |
| any mode lacks effect/projection/finality/loss status | blocked_at_effect_typed_packet |
| any mode provenance does not begin `gu-derived:` | import |
| any forbidden target string supplies source data | import_control_or_rollback |
| `H_raw` missing | blocked_at_raw_Gram |
| `H_raw` not Hermitian | fail_raw_Gram |
| removed roles absent without empty-role proof | blocked_at_removed_representatives |
| `Q_b` missing | blocked_at_Q_b |
| `Q_b` not full column rank | fail_quotient_execution |
| `R_b^* H_raw Q_b != 0` | fail_quotient_leakage |
| `H_phys != Q_b^* H_raw Q_b` | fail_physical_Gram_computation |
| `H_phys` has negative physical norm | fail_finite_seed |
| `rank(H_phys) = 0` | fail_nontrivial_seed_or_quotient_erased_branch |
| clean exact `H_phys >= 0` and nonzero rank | promote_positive_finite_one_particle_seed_only |
| source covariance later supplied | advance_to_covariance_gate_not_CHSH |
| `rho_AB` and GU-admissible observables later supplied | run_CHSH_gate_without_weakening_provenance |

This is the strongest positive construction because it would turn a future packet into a
deterministic decision object. It is not an inhabited witness today.

## 4. First Exact Obstruction Or Missing Proof Object

The first exact obstruction is the missing source inhabitant:

```text
EffectTypedSourceProjectorPFinBWithLocalModeRecords
```

The repo can name the 16-dimensional carrier and the formal quotient equation. It cannot
identify the 16 local source modes occupying that carrier. Since those source modes are
absent, the packet cannot assign their effect type, projection status, finality status,
or loss status. Without those records, `H_raw` would be a matrix on labels rather than a
source-derived physical Gram. Without `H_raw`, removed representatives, and `Q_b`,
`H_phys` is not computable.

Current source supply:

```text
P_fin_b: missing
exactly_16_local_mode_records: missing
gu_derived_mode_provenance: missing
effect_type: missing
projection_status: missing
finality_status: missing
loss_status: missing
H_raw: missing
removed_representatives_R_b: missing
Q_b: missing
H_phys_positivity: not computable
```

This obstruction is prior to covariance, state extraction, finite `rho_AB`, and CHSH.
Supplying an identity Gram, Bell state, Pauli settings, free vacuum, Hadamard/Fock state,
Stinespring/CPTP channel, or target-fitted covariance would be control/import data unless
the source packet above derives it.

## 5. Constructive Next Object

The next object is the actual packet instance:

```text
effect_typed_source_projector_pfin_b_for_QFT_SSX_PS_LR_QUASIFREE_v0
```

It should contain:

```text
1. Exact base field.
2. Exact P_fin_b from F_phys^b(O) to K_b.
3. Exactly 16 local mode records.
4. Eight V_L records and eight V_R records with unique slot indices.
5. gu-derived provenance for every source mode.
6. Local support or local algebra inclusion for every source mode.
7. Effect type, projection status, finality status, and loss status for every mode.
8. Exact H_raw from the GU physical pairing/current.
9. Removed representatives for EOM, gauge, constraint, ghost, and null roles, or exact
   source proofs that a role is empty.
10. Exact full-column-rank Q_b.
11. Exact quotient compatibility check R_b^* H_raw Q_b = 0.
12. Exact H_phys computation and positivity/rank certificate.
```

The validator should emit one of four top-level outcomes:

```text
accepted_positive_finite_seed_only
blocked_missing_source_or_quotient_data
fail_inconsistent_packet_or_negative_seed
import_control_or_rollback
```

## 6. Impact On GU Claim

This artifact improves the GU reconstruction program by converting an interface-level
missing object into an exact packet contract and decision table. It does not prove the
object exists.

Impact:

```text
GU QFT finite-seed branch:
  more sharply testable
  not promoted

PositiveFiniteOneParticleSeed(K_b):
  promotable only after a clean packet exists
  not promoted by current sources

QFT recovery:
  not claimed

covariance:
  not claimed

rho_AB:
  not supplied

CHSH or Bell violation:
  not claimed

positivity closure:
  not claimed
```

If a future source packet fails local provenance, quotient compatibility, or positivity,
that is a real failure of this finite seed branch. If the packet remains absent, the
branch is blocked, not refuted.

## 7. Next Meaningful Proof/Computation Step

Implement or refute the packet instance and run the exact validation in this order:

```text
1. Extract P_fin_b from the physical field complex.
2. Emit exactly 16 local source mode records.
3. Check gu-derived provenance and local support/local algebra inclusion.
4. Check effect type, projection status, finality status, and loss status.
5. Compute H_raw from the source physical pairing/current.
6. Emit removed representatives or empty-role proofs for EOM/gauge/constraint/ghost/null.
7. Compute exact full-column-rank Q_b.
8. Check R_b^* H_raw Q_b = 0.
9. Compute H_phys = Q_b^* H_raw Q_b.
10. Certify H_phys >= 0 and rank(H_phys) > 0 exactly.
11. Promote only PositiveFiniteOneParticleSeed(K_b), then stop.
```

The following are later gates and must not be inferred from this packet:

```text
source covariance
QFT state or GNS state extraction
rho_AB
Alice/Bob tensor product reduction
GU-admissible observables
CHSH violation or Bell violation
```

## 8. Machine-Readable JSON Summary

```json
{
  "artifact": "HOURLY_CYCLE2_QFT_EFFECT_TYPED_SOURCE_MODE_PACKET",
  "version": "2026-06-25",
  "sector_id": "QFT-SSX-PS-LR-QUASIFREE-v0",
  "packet_contract_id": "EffectTypedSourceProjectorPFinBWithLocalModeRecords",
  "packet_id": "effect_typed_source_projector_pfin_b_for_QFT_SSX_PS_LR_QUASIFREE_v0",
  "verdict": "UNDERDEFINED_PACKET_CONTRACT_SPECIFIED_BUT_UNINHABITED",
  "status": "underdefined",
  "contract_specified": true,
  "packet_inhabited_by_current_sources": false,
  "positive_seed_promoted": false,
  "qft_recovered": false,
  "covariance_promoted": false,
  "rho_AB_supplied": false,
  "chsh_promoted": false,
  "bell_violation_claimed": false,
  "positivity_closure_claimed": false,
  "not_a_chsh_or_qft_recovery_claim": true,
  "derived_directly_from_sources": [
    "Mission_A_posture_and_no_target_smuggling_guardrails",
    "five_lane_decision_grade_worker_contract",
    "Cycle1_promised_EffectTypedSourceProjectorPFinBWithLocalModeRecords",
    "K_b_as_16_dimensional_Pati_Salam_LR_representation_carrier",
    "P_fin_b_and_16_local_modes_are_required",
    "H_phys_equals_Q_star_H_raw_Q_formal_equation",
    "H_raw_removed_representatives_Q_b_and_H_phys_positivity_are_missing",
    "PositivePhysicalTwoPointCertificate_is_downstream_for_state_space",
    "CHSH_and_Bell_data_are_not_promoted_from_current_sources"
  ],
  "carrier": {
    "formula": "K_b=V_L direct_sum V_R",
    "V_L": "(4,2,1)",
    "V_R": "(4bar,1,2)",
    "dim_C_V_L": 8,
    "dim_C_V_R": 8,
    "dim_C_K_b": 16,
    "status": "representation_carrier_only_until_packet_is_inhabited"
  },
  "required_schema": {
    "top_level_fields": [
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
      "decision"
    ],
    "source_projector_P_fin_b": [
      "domain_F_phys_b_O",
      "codomain_K_b",
      "exact_map_data",
      "gu_derived_provenance",
      "source_supplied_status"
    ],
    "local_mode_record_fields": [
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
    "projection_fields": [
      "H_raw_exact_16_by_16",
      "H_raw_Hermitian_certificate",
      "removed_representatives_R_b",
      "removed_direction_roles",
      "Q_b_exact_16_by_r",
      "Q_b_full_column_rank_certificate",
      "R_star_H_raw_Q_equals_zero",
      "H_phys_equals_Q_star_H_raw_Q",
      "H_phys_psd_certificate",
      "H_phys_positive_rank_certificate"
    ],
    "required_removed_roles": [
      "EOM_b",
      "Gauge_b",
      "Constraint_b",
      "Ghost_b",
      "Null_b"
    ]
  },
  "allowed_values": {
    "base_field": [
      "QQ",
      "QQ_i",
      "number_field",
      "symbolic_exact"
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
    ]
  },
  "acceptance_conditions": [
    "sector_id_matches_QFT_SSX_PS_LR_QUASIFREE_v0",
    "carrier_is_16_dimensional_with_8_plus_8_split",
    "base_field_is_exact",
    "P_fin_b_maps_F_phys_b_O_to_K_b_with_gu_derived_provenance",
    "exactly_16_local_mode_records",
    "all_mode_provenance_starts_gu_derived",
    "all_modes_have_local_support_or_local_algebra_inclusion",
    "all_modes_have_effect_projection_finality_and_loss_statuses",
    "V_L_and_V_R_each_have_exactly_8_unique_slots",
    "H_raw_is_exact_16_by_16_Hermitian_and_source_provenanced",
    "all_removed_roles_represented_or_source_proved_empty",
    "Q_b_is_exact_16_by_r_and_full_column_rank",
    "R_star_H_raw_Q_equals_zero_exactly",
    "H_phys_equals_Q_star_H_raw_Q_exactly",
    "H_phys_is_Hermitian_psd_and_nonzero_rank_by_exact_certificate",
    "forbidden_import_screen_is_clean"
  ],
  "decision_table": {
    "missing_P_fin_b": "blocked",
    "P_fin_b_lacks_gu_derived_provenance": "import",
    "not_exactly_16_local_mode_records": "blocked",
    "duplicate_or_missing_V_L_V_R_slot_indices": "fail_mode_slot_accounting",
    "missing_local_support_or_local_algebra": "fail_local_observer_input",
    "missing_effect_projection_finality_or_loss_status": "blocked_at_effect_typed_packet",
    "mode_provenance_not_gu_derived": "import",
    "forbidden_target_string_supplies_source_data": "import_control_or_rollback",
    "missing_H_raw": "blocked_at_raw_Gram",
    "H_raw_not_Hermitian": "fail_raw_Gram",
    "removed_roles_absent_without_empty_role_proof": "blocked_at_removed_representatives",
    "missing_Q_b": "blocked_at_Q_b",
    "Q_b_not_full_column_rank": "fail_quotient_execution",
    "R_star_H_raw_Q_nonzero": "fail_quotient_leakage",
    "H_phys_not_equal_Q_star_H_raw_Q": "fail_physical_Gram_computation",
    "H_phys_negative": "fail_finite_seed",
    "H_phys_rank_zero": "fail_nontrivial_seed_or_quotient_erased_branch",
    "clean_H_phys_psd_nonzero_rank": "promote_positive_finite_one_particle_seed_only",
    "source_covariance_later_supplied": "advance_to_covariance_gate_not_CHSH",
    "rho_AB_and_GU_admissible_observables_later_supplied": "run_CHSH_gate_without_weakening_provenance"
  },
  "current_source_supply": {
    "P_fin_b": "missing",
    "exactly_16_local_mode_records": "missing",
    "gu_derived_mode_provenance": "missing",
    "effect_type": "missing",
    "projection_status": "missing",
    "finality_status": "missing",
    "loss_status": "missing",
    "H_raw": "missing",
    "removed_representatives_R_b": "missing",
    "Q_b": "missing",
    "H_phys": "not_computable",
    "H_phys_positivity": "not_computable",
    "source_covariance": "missing",
    "rho_AB": "missing",
    "GU_admissible_observables": "missing"
  },
  "forbidden_target_imports": [
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
  "anti_overclaim_guards": {
    "QFT_recovery": "not_claimed",
    "source_covariance": "not_claimed",
    "rho_AB": "not_supplied",
    "CHSH": "not_claimed",
    "Bell_violation": "not_claimed",
    "positivity_closure": "not_claimed"
  },
  "strongest_positive_construction_attempt": {
    "kind": "packet_schema_and_validator",
    "contract_accepts_future_clean_packet": true,
    "contract_is_inhabited_today": false,
    "promotes_today": [],
    "conditional_promotes_if_clean_packet_supplied": [
      "PositiveFiniteOneParticleSeed_K_b"
    ],
    "does_not_promote_even_if_positive_seed": [
      "quasifree_covariance",
      "QFT_state",
      "rho_AB",
      "Alice_Bob_tensor_product_reduction",
      "GU_admissible_observables",
      "CHSH_violation",
      "Bell_violation"
    ]
  },
  "first_exact_obstruction": {
    "id": "EffectTypedSourceProjectorPFinBWithLocalModeRecords",
    "why_first": "the_repo_names_K_b_and_H_phys_equals_Q_star_H_raw_Q_but_not_the_16_local_source_modes_or_their_effect_typed_fate",
    "missing_fields": [
      "P_fin_b",
      "exactly_16_local_mode_records",
      "gu_derived_mode_provenance",
      "effect_type",
      "projection_status",
      "finality_status",
      "loss_status",
      "H_raw",
      "removed_representatives_R_b",
      "Q_b",
      "H_phys_positivity"
    ],
    "current_status": "missing"
  },
  "constructive_next_object": {
    "id": "effect_typed_source_projector_pfin_b_for_QFT_SSX_PS_LR_QUASIFREE_v0",
    "validator_outputs": [
      "accepted_positive_finite_seed_only",
      "blocked_missing_source_or_quotient_data",
      "fail_inconsistent_packet_or_negative_seed",
      "import_control_or_rollback"
    ],
    "next_steps": [
      "extract_P_fin_b_from_physical_field_complex",
      "emit_exactly_16_local_source_mode_records",
      "check_gu_derived_provenance_and_local_support",
      "check_effect_projection_finality_and_loss_status",
      "compute_H_raw_from_source_physical_pairing",
      "emit_removed_representatives_or_empty_role_proofs",
      "compute_exact_full_column_rank_Q_b",
      "check_R_star_H_raw_Q_equals_zero",
      "compute_H_phys_equals_Q_star_H_raw_Q",
      "certify_H_phys_psd_and_positive_rank_exactly",
      "promote_only_PositiveFiniteOneParticleSeed_K_b"
    ]
  }
}
```
