---
title: "Hourly Cycle 1 Effect-Typed Witness Transport For QFT Modes"
date: "2026-06-25"
status: exploration/contract
doc_type: effect_typed_witness_transport_qft_modes
verdict: "CONDITIONAL_INTERFACE_BLOCKED_AT_EFFECT_TYPED_SOURCE_PROJECTOR_WITH_LOCAL_MODE_RECORDS"
owned_path: "explorations/hourly-cycle1-effect-typed-witness-qft-modes-2026-06-25.md"
companion_audit:
  - "tests/hourly_cycle1_effect_typed_witness_qft_modes_audit.py"
depends_on:
  - "RESEARCH-POSTURE.md"
  - "process/runbooks/five-lane-frontier-run.md"
  - "explorations/hourly-cycle2-qft-source-mode-quotient-data-ledger-2026-06-24.md"
  - "explorations/hourly-cycle1-qft-finite-quotient-gram-gate-2026-06-24.md"
  - "explorations/mission-a-qft-state-space-extraction-2026-06-24.md"
---

# Hourly Cycle 1 Effect-Typed Witness Transport For QFT Modes

## 1. Verdict

Verdict: **conditional**.

An `EffectTypedWitnessTransport` interface can reduce the current QFT/CHSH blocker to a
typed contract over finite source modes, projection data, finality data, and loss data.
It cannot close the blocker from the required repo sources.

The strongest honest result is:

```text
EffectTypedWitnessTransport(K_b):
  conditionally well-specified as a contract
  not inhabited by current source data

first missing inhabitant:
  EffectTypedSourceProjectorPFinBWithLocalModeRecords

current promotion:
  no positive finite seed
  no covariance
  no QFT state extraction
  no Alice/Bob tensor reduction
  no CHSH violation
```

This is a useful reduction, not a proof of physics. It turns the missing
`SourceProjectorPFinBWithLocalModeRecords` into a stricter typed object: the projector and
16 local modes must carry effect provenance, projection compatibility, finality status,
and declared loss before quotient-Gram data can be promoted.

## 2. What Was Derived Directly From Repo Sources

`RESEARCH-POSTURE.md` supplies the guardrail: pursue the GU reconstruction aggressively,
but do not convert compatibility into derivation or hide target data inside the source.

`process/runbooks/five-lane-frontier-run.md` fixes the worker contract: identify the exact
missing proof object, state rollback conditions, and avoid overclaiming.

`hourly-cycle1-qft-finite-quotient-gram-gate-2026-06-24.md` establishes the finite carrier
and matrix gate:

```text
K_b = V_L direct_sum V_R
V_L = (4,2,1),       dim_C V_L = 8
V_R = (4bar,1,2),   dim_C V_R = 8
dim_C K_b = 16
H_phys = Q_b^* H_raw Q_b
```

It also establishes that `H_raw`, `Q_b`, removed representatives, local mode provenance,
and `H_phys` are missing.

`hourly-cycle2-qft-source-mode-quotient-data-ledger-2026-06-24.md` sharpens the first
missing object to:

```text
SourceProjectorPFinBWithLocalModeRecords
```

with `P_fin^b`, exactly 16 local `gu-derived:` mode records, local support/local algebra
provenance, `H_raw`, removed-direction representatives, `Q_b`, and a positivity
certificate still absent.

`mission-a-qft-state-space-extraction-2026-06-24.md` gives the downstream state-space
pipeline: a positive physical pairing and two-point/quasifree state would be needed
before GNS, finite `rho_AB`, admissible observables, unitarity, locality, anomaly, or
CHSH gates can be promoted.

Therefore the derived source facts are limited to:

| object | direct source status |
|---|---|
| `K_b` | named 16-dimensional Pati-Salam LR representation carrier |
| quotient formula | formal equation `H_phys = Q_b^* H_raw Q_b` |
| source projector | required but absent |
| 16 local mode records | required but absent |
| effect/finality/loss typing | not yet supplied by prior files |
| positive finite seed | not established |
| covariance or QFT state | not established |
| CHSH data | controls and ansatz only, not GU-derived |

## 3. The Strongest Positive Result

The strongest construction is a typed interface, not an inhabited witness.

Define a finite transport packet:

```text
EffectTypedWitnessTransport(b, K_b):
  SourceModes:
    P_fin^b: F_phys^b(O) -> K_b
    mode_records[16]

  Projection:
    H_raw
    R_b with EOM/Gauge/Constraint/Ghost/Null roles
    Q_b
    H_phys = Q_b^* H_raw Q_b

  Finality:
    status of each mode/effect after projection:
      final
      killed_by_EOM
      killed_by_gauge
      killed_by_constraint
      killed_by_ghost
      killed_by_null
      unresolved

  Loss:
    explicit loss ledger from source to quotient:
      no_loss
      quotient_removed
      locality_lost
      positivity_lost
      provenance_lost
      tensor_factorization_not_supplied
      observable_admissibility_not_supplied
```

This interface is stronger than the prior source-mode ledger because it forces every
candidate witness to state what survived, what was removed, and what has not been
transported. It blocks a common false positive:

```text
source labels exist
  -> choose identity Gram
  -> choose Bell or Pauli data
  -> report QFT/CHSH progress
```

The typed transport rejects that route. Representation labels can populate a carrier
slot, but they do not populate the source, projection, finality, or loss slots.

The minimal positive theorem schema is:

```text
If an EffectTypedWitnessTransport packet supplies:
  1. P_fin^b and exactly 16 local gu-derived mode records,
  2. effect provenance for each mode,
  3. H_raw from the source physical pairing,
  4. removed-direction representatives with roles,
  5. full-column-rank Q_b,
  6. R_b^* H_raw Q_b = 0,
  7. H_phys = Q_b^* H_raw Q_b,
  8. exact H_phys >= 0 and rank(H_phys) > 0,
  9. finality/loss ledgers showing no hidden target input,
then the packet promotes only:
  PositiveFiniteOneParticleSeed(K_b).
```

It still does not promote a covariance, QFT state, Alice/Bob tensor-product state, or CHSH
violation.

## 4. First Exact Obstruction Or Missing Proof Object

The first exact obstruction is:

```text
EffectTypedSourceProjectorPFinBWithLocalModeRecords
```

It must refine the prior missing object by adding effect typing and transport statuses:

```text
P_fin^b:
  F_phys^b(O) -> K_b

mode_records:
  exactly 16 records m_i

each record contains:
  label
  raw representative in F_raw^b(O) or Sol_raw^b(O)
  image in K_b
  representation slot in V_L or V_R
  local support or local algebra inclusion
  provenance beginning gu-derived:
  source operator/section/constraint reference
  effect_type
  projection_status
  finality_status
  loss_status
```

Why this is first:

```text
The repo can name K_b.
The repo can name the quotient-Gram equation.
The repo cannot identify the 16 local source modes occupying K_b.
Therefore it also cannot assign effect types, finality statuses, or loss statuses to
those modes.
```

Without this object, an `EffectTypedWitnessTransport` value would be a type declaration
with no source inhabitants. `H_raw`, `Q_b`, `H_phys`, covariance, and CHSH data would then
be imported control data if inserted.

## 5. Constructive Next Object

The next object should be a finite source packet, not another Bell fixture:

```text
EffectTypedSourceProjectorPFinBWithLocalModeRecords:
  packet_id:
    effect_typed_source_projector_pfin_b_for_QFT_SSX_PS_LR_QUASIFREE_v0

  base_field:
    QQ, QQ_i, number_field, or symbolic_exact

  P_fin_b:
    explicit source projector/extractor

  mode_records:
    exactly 16 local source records

  effect_types:
    source_mode
    quotient_constraint
    local_observer_input
    pairing_input
    covariance_input_candidate
    observable_input_candidate

  projection_statuses:
    raw
    projected
    quotient_survivor
    quotient_removed

  finality_statuses:
    final
    provisional
    killed_by_EOM
    killed_by_gauge
    killed_by_constraint
    killed_by_ghost
    killed_by_null
    unresolved

  loss_statuses:
    no_loss
    quotient_removed
    locality_lost
    positivity_lost
    provenance_lost
    tensor_factorization_not_supplied
    observable_admissibility_not_supplied
```

Once supplied, the next computation is the same finite quotient-Gram computation as the
prior ledgers, but with stricter typed checks:

```text
1. verify exactly 16 local modes;
2. verify every mode provenance begins gu-derived:;
3. verify local support or local algebra inclusion;
4. reject Bell, Pauli, free-vacuum, Hadamard, Fock, identity-pairing, target, CHSH,
   Stinespring, and CPTP source shortcuts;
5. verify effect_type, projection_status, finality_status, and loss_status are present;
6. compute/check H_raw, R_b, Q_b, and H_phys if supplied;
7. promote only PositiveFiniteOneParticleSeed(K_b) if the quotient-Gram certificate is
   exact, positive semidefinite, nonzero rank, and source-derived.
```

## 6. What This Means For The Relevant GU Claim

For the GU reconstruction claim, this lane says:

```text
The QFT/CHSH blocker can be organized as a typed source/projection/finality/loss contract.
That organization is constructively useful.
It does not derive the missing finite source modes or the quotient-Gram data.
```

The relevant GU claim is not refuted by this lane. It is also not promoted. The current
status is conditional: if GU supplies the effect-typed source projector and the finite
quotient-Gram packet, the branch can advance to a positive finite one-particle seed test.
If the clean packet yields negative physical norm, gauge leakage, rank-zero quotient, or
lost locality/provenance, this Pati-Salam LR quasifree finite seed branch fails or
demotes to control plumbing.

Nothing in this result supports the following promotions:

```text
Bell violation
QFT state extraction
source covariance
positivity closure
Alice/Bob tensor product
GU-admissible observables
```

## 7. Next Meaningful Proof Or Computation Step

Build or refute the exact packet:

```text
EffectTypedSourceProjectorPFinBWithLocalModeRecords
```

with 16 local records and then run the quotient-Gram computation. The decision table is:

| condition | decision |
|---|---|
| no `P_fin^b` | blocked |
| not exactly 16 local modes | blocked |
| any mode lacks `gu-derived:` provenance | blocked/import |
| any mode lacks local support or local algebra inclusion | fail local observer input |
| effect/finality/loss fields absent | blocked at witness transport typing |
| `H_raw` absent after modes exist | blocked at raw Gram |
| `Q_b` or removed representatives absent | blocked at quotient representatives |
| `R_b^* H_raw Q_b != 0` | fail quotient leakage |
| `H_phys` negative after quotient | fail finite seed |
| `rank(H_phys) = 0` | fail nontrivial seed or quotient-erased branch |
| clean positive nonzero quotient | promote positive finite one-particle seed only |
| source covariance later supplied | advance to covariance gate, not CHSH |
| `rho_AB` and GU-admissible observables later supplied | then run CHSH gate without weakening provenance |

## 8. Machine-Readable JSON Summary

```json
{
  "artifact": "HOURLY_CYCLE1_EFFECT_TYPED_WITNESS_QFT_MODES",
  "version": "2026-06-25",
  "sector_id": "QFT-SSX-PS-LR-QUASIFREE-v0",
  "interface_id": "EffectTypedWitnessTransport",
  "verdict": "CONDITIONAL_INTERFACE_BLOCKED_AT_EFFECT_TYPED_SOURCE_PROJECTOR_WITH_LOCAL_MODE_RECORDS",
  "status": "conditional",
  "qft_recovered": false,
  "positive_seed_promoted": false,
  "covariance_promoted": false,
  "qft_state_extraction_promoted": false,
  "chsh_promoted": false,
  "bell_violation_claimed": false,
  "positivity_closure_claimed": false,
  "not_a_chsh_or_qft_recovery_claim": true,
  "derived_directly_from_sources": [
    "Mission_A_posture_and_no_target_smuggling_guardrails",
    "five_lane_decision_grade_worker_contract",
    "K_b_as_16_dimensional_Pati_Salam_LR_representation_carrier",
    "finite_formula_H_phys_equals_Q_star_H_raw_Q",
    "SourceProjectorPFinBWithLocalModeRecords_is_prior_missing_object",
    "H_raw_Q_b_removed_representatives_H_phys_are_missing",
    "PositivePhysicalTwoPointCertificate_is_downstream_for_state_space",
    "CHSH_fixtures_are_controls_or_ansatz_not_GU_derived"
  ],
  "K_b": {
    "formula": "K_b=V_L direct_sum V_R",
    "V_L": "(4,2,1)",
    "V_R": "(4bar,1,2)",
    "dim_C_V_L": 8,
    "dim_C_V_R": 8,
    "dim_C_K_b": 16,
    "status": "representation_carrier_only_until_effect_typed_source_modes_and_quotient_Gram_data_are_supplied"
  },
  "strongest_positive_result": {
    "kind": "typed_interface_contract",
    "interface": "EffectTypedWitnessTransport",
    "can_reduce_blocker_to_contract": true,
    "is_inhabited_by_current_sources": false,
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
      "CHSH_violation"
    ]
  },
  "transport_contract": {
    "required_slots": [
      "source_modes",
      "projection",
      "finality",
      "loss"
    ],
    "source_modes": [
      "P_fin_b",
      "exactly_16_local_mode_records",
      "gu_derived_provenance",
      "local_support_or_local_algebra_inclusion",
      "source_operator_section_constraint_reference"
    ],
    "projection": [
      "H_raw",
      "R_b_removed_representatives",
      "removed_direction_roles",
      "Q_b",
      "R_star_H_raw_Q_equals_zero",
      "H_phys_equals_Q_star_H_raw_Q",
      "H_phys_psd_nonzero_rank_certificate"
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
    "effect_types": [
      "source_mode",
      "quotient_constraint",
      "local_observer_input",
      "pairing_input",
      "covariance_input_candidate",
      "observable_input_candidate"
    ]
  },
  "first_exact_obstruction": {
    "id": "EffectTypedSourceProjectorPFinBWithLocalModeRecords",
    "refines_prior_missing_object": "SourceProjectorPFinBWithLocalModeRecords",
    "why_first": "the_repo_names_K_b_and_the_quotient_Gram_equation_but_not_the_16_local_source_modes_or_their_effect_fate",
    "must_emit": [
      "P_fin_b_from_F_phys_b_O_to_K_b",
      "exactly_16_mode_records",
      "raw_representatives",
      "representation_slots",
      "local_support_or_local_algebra_inclusion",
      "provenance_beginning_gu_derived",
      "source_operator_section_constraint_reference",
      "effect_type",
      "projection_status",
      "finality_status",
      "loss_status"
    ],
    "current_status": "missing"
  },
  "current_source_supply": {
    "P_fin_b": "missing",
    "exactly_16_local_mode_records": "missing",
    "effect_typing_for_modes": "missing",
    "projection_status_for_modes": "missing",
    "finality_status_for_modes": "missing",
    "loss_status_for_modes": "missing",
    "H_raw": "missing",
    "R_b_removed_representatives": "missing",
    "Q_b": "missing",
    "H_phys": "not_computable",
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
    "Bell_violation": "not_claimed",
    "QFT_state_extraction": "not_claimed",
    "source_covariance": "not_claimed",
    "positivity_closure": "not_claimed",
    "Alice_Bob_tensor_product": "not_claimed",
    "GU_admissible_observables": "not_claimed"
  },
  "decision_table": {
    "missing_P_fin_b": "blocked",
    "not_exactly_16_local_modes": "blocked",
    "missing_gu_derived_provenance": "blocked_or_import",
    "missing_local_support": "fail_local_observer_input",
    "missing_effect_finality_loss_fields": "blocked_at_witness_transport_typing",
    "missing_H_raw_after_modes": "blocked_at_raw_Gram",
    "missing_Q_b_or_removed_representatives": "blocked_at_quotient_representatives",
    "R_star_H_raw_Q_nonzero": "fail_quotient_leakage",
    "H_phys_negative": "fail_finite_seed",
    "H_phys_rank_zero": "fail_nontrivial_seed_or_quotient_erased_branch",
    "clean_positive_nonzero_quotient": "promote_positive_finite_one_particle_seed_only",
    "source_covariance_later_supplied": "advance_to_covariance_gate_not_CHSH",
    "rho_AB_and_GU_admissible_observables_later_supplied": "run_CHSH_gate_without_weakening_provenance"
  },
  "constructive_next_object": {
    "id": "EffectTypedSourceProjectorPFinBWithLocalModeRecords",
    "packet_id": "effect_typed_source_projector_pfin_b_for_QFT_SSX_PS_LR_QUASIFREE_v0",
    "input_packet": "EffectTypedSourceModePacket",
    "steps": [
      "verify_exactly_16_local_modes",
      "verify_all_mode_provenance_starts_gu_derived",
      "verify_local_support_or_local_algebra_inclusion",
      "reject_forbidden_source_strings",
      "verify_effect_type_projection_status_finality_status_and_loss_status",
      "verify_H_raw_equals_H_raw_star_if_supplied",
      "verify_removed_roles_present_or_source_proved_empty_if_supplied",
      "verify_Q_b_full_column_rank_if_supplied",
      "verify_R_star_H_raw_Q_equals_zero_if_supplied",
      "compute_H_phys_equals_Q_star_H_raw_Q_if_supplied",
      "certify_H_phys_positive_semidefinite_exactly_if_supplied",
      "verify_rank_H_phys_positive_if_supplied",
      "emit_decision_table_outcome"
    ],
    "first_promotable_output": "PositiveFiniteOneParticleSeed_K_b",
    "not_yet": [
      "quasifree_covariance",
      "QFT_state",
      "rho_AB",
      "CHSH_violation"
    ]
  }
}
```
