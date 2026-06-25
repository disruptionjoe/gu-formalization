---
title: "Hourly 20260625 0103 Cycle 2 QFT P_fin^b Source Projector Locator"
date: "2026-06-25"
status: exploration/locator
doc_type: qft_pfin_b_source_projector_locator
verdict: "ABSENT_PROJECTOR_REPRESENTATION_LABELS_AND_CONTROL_DATA_ONLY"
owned_path: "explorations/hourly-20260625-0103-cycle2-qft-pfin-b-source-projector-locator.md"
companion_audit:
  - "tests/hourly_20260625_0103_cycle2_qft_pfin_b_source_projector_locator_audit.py"
depends_on:
  - "RESEARCH-POSTURE.md"
  - "process/runbooks/five-lane-frontier-run.md"
  - "explorations/hourly-20260625-0103-cycle1-qft-single-mode-source-extraction-certificate.md"
  - "explorations/hourly-cycle3-qft-source-mode-packet-validator-2026-06-25.md"
  - "explorations/hourly-cycle2-qft-effect-typed-source-mode-packet-2026-06-25.md"
  - "explorations/mission-a-qft-state-space-extraction-2026-06-24.md"
  - "sources/claim-ledger.md"
  - "sources/media-claim-mining-report-v1.md"
---

# Hourly 20260625 0103 Cycle 2 QFT P_fin^b Source Projector Locator

## 1. Verdict

Verdict: **absent projector; representation labels and control data only**.

This locator searched for a repo-local source projector

```text
P_fin^b: F_phys^b(O) -> K_b
```

or for a credible repo-local source extraction rule that could produce it. Current
sources do not contain the map, exact map data, or an extraction rule with
`gu-derived:` provenance. They contain:

1. the intended finite carrier
   `K_b = V_L direct_sum V_R`, with `V_L=(4,2,1)`, `V_R=(4bar,1,2)`,
   and `dim_C K_b = 16`;
2. packet and validator contracts that require `P_fin^b`;
3. one-mode and 16-mode blockers that say the projector is missing;
4. CHSH/Bell/Pauli/free-vacuum style controls that are explicitly not source data;
5. media claim ledgers that provide provenance discipline, not formal projector data.

The first exact missing object is therefore:

```text
P_fin^b: F_phys^b(O) -> K_b
with gu-derived provenance and exact source extraction rule or exact map data.
```

This block occurs before local mode records, raw representatives, local support proofs,
`H_raw`, quotient representatives, matrix positivity, covariance, `rho_AB`, CHSH, or Bell
claims.

## 2. Direct Source Derivations

`RESEARCH-POSTURE.md` supplies the guardrail: pursue the GU reconstruction
constructively, but do not call compatibility a derivation and do not hide target data
inside a reconstruction.

`process/runbooks/five-lane-frontier-run.md` supplies the lane standard: produce a
decision-grade artifact, identify the first exact obstruction, and avoid overclaiming.

`hourly-20260625-0103-cycle1-qft-single-mode-source-extraction-certificate.md` attempts
the one-mode pilot for `V_L[1]` and blocks at missing `P_fin^b`. It treats `V_L[1]` as an
intended representation slot only, not as an inhabited local source mode.

`hourly-cycle3-qft-source-mode-packet-validator-2026-06-25.md` gives the validator order:
sector and carrier labels can be checked first, then the packet blocks at step 4 because
`source_projector_P_fin_b` is absent.

`hourly-cycle2-qft-effect-typed-source-mode-packet-2026-06-25.md` specifies the
`EffectTypedSourceProjectorPFinBWithLocalModeRecords` contract. It states that the
contract is specified but uninhabited by current sources.

`mission-a-qft-state-space-extraction-2026-06-24.md` places covariance, local algebra
state, finite `rho_AB`, observables, and CHSH downstream of physical field complexes,
positive pairing, and source-derived state data. These downstream objects cannot be used
to backfill `P_fin^b`.

`sources/claim-ledger.md` is a provenance ledger template and explicitly says media claims
are not mathematical evidence unless connected to formal definitions, theorem statements,
or published literature.

`sources/media-claim-mining-report-v1.md` is a mining status report. It records coverage
gaps and methodology, but supplies no formal source projector, local mode record, or
matrix datum.

The repo-local search also found nearby QFT artifacts that mention `P_fin^b`; those hits
classify it as required/missing or as a future object, not as a supplied projector.

## 3. Strongest Positive Result

The strongest positive result is a **source-projector locator decision table** for current
repo supply:

| candidate surface | locator status | decision |
|---|---|---|
| `K_b = V_L direct_sum V_R` | representation carrier only | not a projector |
| Pati-Salam labels `(4,2,1)` and `(4bar,1,2)` | representation labels only | not source images |
| `EffectTypedSourceProjectorPFinBWithLocalModeRecords` | contract/schema | uninhabited |
| cycle 3 packet validator | validator/check order | blocks at missing projector |
| cycle 1 one-mode certificate | one-slot pilot | blocks at missing projector |
| state-space extraction pipeline | downstream state route | cannot supply finite source projector today |
| CHSH/Bell/Pauli fixtures | executable controls/imports | forbidden as source data |
| media claim ledger/report | provenance/process records | no formal map data |

This is positive because it narrows the branch to one exact pre-matrix object and prevents
later finite-state or Bell-control data from being misfiled as source extraction.

## 4. First Exact Obstruction

The first exact obstruction is:

```text
source_projector_P_fin_b:
  domain: F_phys^b(O)
  codomain: K_b
  content: exact formula, exact matrix, or exact extraction rule
  provenance: gu-derived:<operator/section/constraint/extraction-reference>
```

Why this is first:

```text
The repo can name the sector and the 16-dimensional representation carrier.
The next required object is the map from physical local source data into that carrier.
No current source gives such a map or a derivation rule.
Without it, the 16 slots are labels, not certified images of local physical source modes.
```

This obstruction is earlier than:

```text
exactly_16_local_mode_records
raw_representatives
local_support_or_local_algebra_inclusion
effect_type/projection_status/finality_status/loss_status
H_raw
removed_representatives_R_b
Q_b
H_phys = Q_b^* H_raw Q_b
H_phys >= 0
rank(H_phys) > 0
covariance
rho_AB
CHSH
Bell violation
```

No matrix positivity test can honestly run, because there is no source-derived finite mode
domain on which `H_raw` is known to be a physical Gram matrix.

## 5. Constructive Next Object

The constructive next object is:

```text
PFinBSourceProjectorExtractionRule_V1
```

It must emit:

```text
sector_id:
  QFT-SSX-PS-LR-QUASIFREE-v0

source_projector_P_fin_b:
  domain: F_phys^b(O)
  codomain: K_b
  exact map data or exact extraction rule
  gu-derived provenance

pilot_mode_record:
  selected slot, for example V_L[1]
  raw or physical representative
  local support or local algebra inclusion
  exact image in K_b under P_fin^b
  source operator/section/constraint reference
  target_import_flag = false
  effect_type
  projection_status
  finality_status
  loss_status
```

After one pilot mode is real, the next packet object is the 16-mode version:

```text
EffectTypedSourceProjectorPFinBWithLocalModeRecords_V1
```

Only after that should the branch compute `H_raw`, removed representatives, `Q_b`,
`H_phys`, and exact PSD/nonzero-rank certificates.

## 6. GU Claim Impact

The QFT finite-source branch remains **open but blocked at source extraction**.

Current sources host a carrier and specify a future acceptance gate. They do not derive a
finite source projector, local source modes, source physical Gram, positive finite seed,
covariance, finite density matrix, admissible observables, CHSH violation, or Bell
violation.

Impact by claim:

| claim | current impact |
|---|---|
| finite source projector | absent |
| local source modes | not reachable before projector |
| matrix positivity | not reachable before local source records and `H_raw` |
| positive finite one-particle seed | not promoted |
| QFT recovery | not promoted |
| covariance/state extraction | not promoted |
| `rho_AB` | not supplied |
| CHSH/Bell | controls only; not promoted |

If a future artifact supplies `P_fin^b` only by importing Pati-Salam labels, an identity
Gram, a free vacuum, Pauli controls, a Bell state, or a target-fitted covariance, the
locator should classify that artifact as **import/control**, not as source extraction.

## 7. Next Proof Step

Build or refute `PFinBSourceProjectorExtractionRule_V1` before any matrix stage.

The next proof step is:

```text
1. Fix a source branch b, observer region O, section, and physical field complex.
2. Define F_phys^b(O) after equations, gauge, constraint, ghost, and null treatment.
3. Produce an exact rule P_fin^b: F_phys^b(O) -> K_b.
4. Prove the rule is gu-derived from named operator/section/constraint data.
5. Apply it to one local representative and certify the image, locality, and effect
   status.
6. Generalize only after the one-mode certificate passes.
```

Expected honest outcomes:

| outcome | meaning |
|---|---|
| `closed_projector_rule_only` | projector exists; continue to one-mode and 16-mode records |
| `blocked_missing_F_phys_b_O` | physical source domain is not defined |
| `blocked_missing_projector_rule` | no source-to-carrier map exists |
| `fail_projector_not_local_or_not_well_defined` | supplied rule does not descend to physical local data |
| `import_control` | rule uses target labels, Bell/CHSH fixtures, identity Gram, or standard QFT vacuum data |

## 8. Machine-Readable JSON Summary

```json
{
  "artifact": "PFinBSourceProjectorLocator_V1",
  "run_id": "hourly-20260625-0103",
  "cycle": 2,
  "lane": 3,
  "verdict": "ABSENT_PROJECTOR_REPRESENTATION_LABELS_AND_CONTROL_DATA_ONLY",
  "status": "blocked",
  "projector_found": false,
  "credible_extraction_rule_found": false,
  "accepted_source_projector_exists": false,
  "positive_finite_seed_promoted": false,
  "qft_recovered": false,
  "covariance_promoted": false,
  "rho_AB_supplied": false,
  "chsh_promoted": false,
  "bell_violation_claimed": false,
  "positivity_closure_claimed": false,
  "not_a_qft_or_chsh_promotion": true,
  "target_projector": {
    "id": "source_projector_P_fin_b",
    "formal_name": "P_fin^b_from_F_phys_b_O_to_K_b",
    "domain": "F_phys^b(O)",
    "codomain": "K_b",
    "required_provenance": "gu-derived",
    "current_status": "missing"
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
    "Cycle1_single_mode_certificate_blocks_at_missing_P_fin_b",
    "Cycle3_validator_blocks_at_source_projector_step_4",
    "Cycle2_packet_contract_is_specified_but_uninhabited",
    "Mission_A_places_covariance_rho_AB_CHSH_downstream",
    "claim_ledger_is_provenance_template_not_formal_evidence",
    "media_claim_mining_report_supplies_no_projector_data",
    "repo_local_search_found_only_required_or_missing_projector_mentions"
  ],
  "source_locator_statuses": [
    {
      "source": "RESEARCH-POSTURE.md",
      "status": "guardrail_only",
      "contains_projector": false,
      "contains_extraction_rule": false,
      "decision": "no_target_smuggling_guardrail"
    },
    {
      "source": "process/runbooks/five-lane-frontier-run.md",
      "status": "process_only",
      "contains_projector": false,
      "contains_extraction_rule": false,
      "decision": "decision_grade_lane_contract"
    },
    {
      "source": "explorations/hourly-20260625-0103-cycle1-qft-single-mode-source-extraction-certificate.md",
      "status": "blocked_certificate",
      "contains_projector": false,
      "contains_extraction_rule": false,
      "decision": "explicit_missing_P_fin_b_for_one_mode"
    },
    {
      "source": "explorations/hourly-cycle3-qft-source-mode-packet-validator-2026-06-25.md",
      "status": "validator_only",
      "contains_projector": false,
      "contains_extraction_rule": false,
      "decision": "blocks_at_source_projector_step_4"
    },
    {
      "source": "explorations/hourly-cycle2-qft-effect-typed-source-mode-packet-2026-06-25.md",
      "status": "contract_only",
      "contains_projector": false,
      "contains_extraction_rule": false,
      "decision": "packet_contract_uninhabited"
    },
    {
      "source": "explorations/mission-a-qft-state-space-extraction-2026-06-24.md",
      "status": "downstream_state_pipeline",
      "contains_projector": false,
      "contains_extraction_rule": false,
      "decision": "covariance_rho_AB_CHSH_downstream_not_projector"
    },
    {
      "source": "sources/claim-ledger.md",
      "status": "provenance_template",
      "contains_projector": false,
      "contains_extraction_rule": false,
      "decision": "media_claims_not_mathematical_evidence"
    },
    {
      "source": "sources/media-claim-mining-report-v1.md",
      "status": "process_report",
      "contains_projector": false,
      "contains_extraction_rule": false,
      "decision": "no_formal_projector_or_mode_data"
    },
    {
      "source": "repo_local_rg_search",
      "status": "locator_search",
      "contains_projector": false,
      "contains_extraction_rule": false,
      "decision": "hits_are_missing_required_or_future_contract_mentions"
    }
  ],
  "classification": {
    "current_sources_contain_projector": false,
    "current_sources_contain_only_representation_labels": true,
    "current_sources_contain_import_or_control_data": true,
    "current_sources_contain_credible_extraction_rule": false,
    "classification_basis": [
      "K_b_and_V_L_V_R_are_named_as_representation_carrier",
      "packet_and_validator_files_require_P_fin_b_but_mark_it_missing",
      "state_and_CHSH_files_are_downstream_or_control_surfaces",
      "media_files_are_provenance_or_process_not_formal_projector_data"
    ]
  },
  "current_repo_supply": {
    "sector_id": "available",
    "carrier_K_b": "available_as_representation_carrier_only",
    "representation_labels": "available_as_labels_only",
    "source_projector_P_fin_b": "missing",
    "credible_source_extraction_rule": "missing",
    "local_mode_records": "not_reachable_before_P_fin_b",
    "raw_representatives": "not_reachable_before_P_fin_b",
    "local_support_or_local_algebra_inclusion": "not_reachable_before_P_fin_b",
    "H_raw": "not_reachable_before_local_source_records",
    "Q_b": "not_reachable_before_H_raw_and_removed_representatives",
    "H_phys": "not_computable",
    "positivity_certificate": "not_reachable",
    "rho_AB": "missing_downstream",
    "CHSH": "control_only_not_promoted"
  },
  "first_exact_obstruction": {
    "id": "source_projector_P_fin_b",
    "formal_name": "P_fin^b_from_F_phys_b_O_to_K_b_with_gu_derived_provenance",
    "current_status": "missing",
    "blocks_before": [
      "exactly_16_local_mode_records",
      "raw_representatives",
      "local_support_or_local_algebra_inclusion",
      "effect_projection_finality_loss_statuses",
      "H_raw",
      "removed_representatives_R_b",
      "Q_b",
      "H_phys",
      "matrix_positivity",
      "covariance",
      "rho_AB",
      "CHSH"
    ],
    "why_first": [
      "sector_and_K_b_can_be_named_from_current_sources",
      "no_current_source_supplies_a_map_from_F_phys_b_O_to_K_b",
      "without_P_fin_b_the_16_slots_are_representation_labels_not_source_mode_images",
      "matrix_positivity_requires_source_mode_records_and_H_raw"
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
    "ordinary_SM_or_Pati_Salam_labels_as_physical_Gram",
    "media_claim_as_formal_projector"
  ],
  "constructive_next_object": {
    "id": "PFinBSourceProjectorExtractionRule_V1",
    "then": "EffectTypedSourceProjectorPFinBWithLocalModeRecords_V1",
    "must_emit": [
      "F_phys_b_O_definition_after_quotients",
      "P_fin_b_from_F_phys_b_O_to_K_b",
      "exact_map_data_or_exact_extraction_rule",
      "gu_derived_projector_provenance",
      "one_pilot_local_representative",
      "local_support_or_local_algebra_inclusion",
      "exact_image_in_K_b",
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
  "GU_claim_impact": "QFT_finite_source_branch_open_but_blocked_at_missing_P_fin_b",
  "next_proof_step": "Build_or_refute_PFinBSourceProjectorExtractionRule_V1_before_local_mode_records_and_matrix_positivity"
}
```
