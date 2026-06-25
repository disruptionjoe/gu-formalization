---
title: "Hourly Cycle 1 Loop State Transition Ledger Contract"
date: "2026-06-25"
status: exploration/contract
doc_type: hourly_cycle1_loop_state_transition_ledger_contract
verdict: "CONDITIONAL_FUTURE_INSTRUMENTATION_CONTRACT_WITH_RETROACTIVE_PROOF_BLOCKED"
owned_path: "explorations/hourly-cycle1-loop-state-transition-ledger-contract-2026-06-25.md"
companion_audit: "tests/hourly_cycle1_loop_state_transition_ledger_contract_audit.py"
depends_on:
  - "RESEARCH-POSTURE.md"
  - "process/runbooks/five-lane-frontier-run.md"
  - "explorations/hourly-cycle3-loop-convergence-false-negative-calibration-2026-06-24.md"
  - "explorations/hourly-three-cycle-fifteen-hole-synthesis-2026-06-24.md"
  - "process/loop-adversarial-log.md"
---

# Hourly Cycle 1 Loop State Transition Ledger Contract

## 1. Verdict

**Verdict: conditional.**

`LoopStateTransitionLedger_v1` can be specified as a minimal machine-readable contract
for future GU automation runs. The contract is strong enough to distinguish closure,
same-status refinement, repetition, downgrade, false negative, and same-session
circularity at row level, provided each future worker emits stable item IDs and both
pre-run and post-run verdict state.

It cannot be used retroactively as a convergence proof for the 2026-06-24 run family.
The first exact obstruction is the absence of stable pre-state rows: prior artifacts name
blockers in prose, but they do not consistently emit `item_id`, `previous_verdict`,
`new_verdict`, `transition_type`, same-session guard state, and proof-object identity in
one comparable ledger.

## 2. What Was Derived Directly From Repo Sources

From `RESEARCH-POSTURE.md`:

- GU work is a research hypothesis, not an already-proved claim.
- Future work should construct missing objects aggressively while preserving proof labels,
  falsification conditions, rollback conditions, dependency tracking, correction logs,
  and independent verification where feasible.
- Forbidden moves include verdict inflation, calling compatibility a derivation,
  optimistic rescue, target-data smuggling, and treating process discipline as physics
  evidence.

From `process/runbooks/five-lane-frontier-run.md`:

- A worker result must be decision-grade and must identify exact missing proof objects.
- Verdicts have controlled meanings: `closed`, `conditional`, `blocked`, `fail`,
  `no-go`, and `underdefined`; `host` and `import` are non-promotion labels.
- Parallel lanes must avoid overlapping files, added audits must pass, and artifacts must
  separate real closure from exact deferral.

From `explorations/hourly-cycle3-loop-convergence-false-negative-calibration-2026-06-24.md`:

- The current loop is under-instrumented but locally converging on named blockers.
- The named missing artifact is `LoopStateTransitionLedger_v1`.
- The minimal row needs stable item identity, lane family, session ID, artifact path,
  previous and new verdicts, transition type, first missing object, blocker family,
  evidence basis, same-session guard, target-import guard, and audit path.
- Same-session flags must be deferred unless closed by later-session or external
  verification.

From `explorations/hourly-three-cycle-fifteen-hole-synthesis-2026-06-24.md`:

- The three-cycle run produced fifteen quality holes, not major claim closure.
- The next proof objects include `K_IG_selector`, `d_RS,-1`,
  `ActualDGU01OperatorCertificate`, `SourceProjectorPFinBWithLocalModeRecords`,
  `SUBSTRATE_TO_OBSERVER_EXTRACTOR_CERTIFICATE`, `FilteredReadoutCoupling_GU`, and
  `LoopStateTransitionLedger_v1`.
- The loop should not rerun vague blockers without recording whether the next pass
  narrows, closes, repeats, or discovers an upstream blocker.

From `process/loop-adversarial-log.md`:

- Recent adversarial review found same-session self-resolution pressure in both sampled
  runs.
- A flag raised in session `N` cannot be closed merely by a different file in session `N`.
- Candidate selection without dismissing alternatives should remain open, not
  conditionally resolved.
- Canon-level resolved claims depending on reconstruction-grade assumptions must be
  downgraded or guarded.

## 3. The Strongest Positive Result

The strongest positive construction is a row-level transition contract, not a global
dashboard. The dashboard is derivable only after rows exist.

### 3.1 Minimal Schema

Each row in `LoopStateTransitionLedger_v1` is one attempted transition for one stable
repo-local claim, gate, or proof object in one run session.

Required row fields:

```json
{
  "ledger_version": "LoopStateTransitionLedger_v1",
  "row_id": "session-local unique row id",
  "item_id": "stable repo-local claim/gate/proof-object id",
  "lane_family": "qft|rs|vz|ig_theta|phi_obs|generation|dark_energy|freed_hopkins|substrate|taf|process|other",
  "session_id": "run or hourly cycle id",
  "cycle_index": 1,
  "artifact_path": "path/to/artifact.md",
  "audit_path": "path/to/audit.py or null",
  "previous_state": {
    "verdict": "unknown|open|blocked|underdefined|conditional|closed|fail|no-go|host|import",
    "missing_object_id": "stable object id or null",
    "blocker_family": "stable blocker-family tag or null",
    "evidence_basis": "none|prose_only|source_derived|verified_computation|external_verification|same_session|target_import"
  },
  "new_state": {
    "verdict": "open|blocked|underdefined|conditional|closed|fail|no-go|host|import",
    "missing_object_id": "stable object id or null",
    "blocker_family": "stable blocker-family tag or null",
    "evidence_basis": "prose_only|source_derived|verified_computation|external_verification|same_session|target_import"
  },
  "transition_type": "new_item|closure|same_status_refinement|repetition|downgrade|false_negative|same_session_circularity|upgrade_without_closure",
  "transition_basis": "short reason for classification",
  "refinement_delta": {
    "narrower_missing_object": true,
    "closed_prior_missing_object": false,
    "introduced_upstream_blocker": false,
    "unchanged_blocker": false
  },
  "guards": {
    "same_session": {
      "flag_raised_session_id": "session id or null",
      "flag_closed_session_id": "session id or null",
      "external_verification_id": "id or null",
      "later_session_verification_id": "id or null",
      "deferred_verification_required": true,
      "same_session_closure_attempted": false
    },
    "target_import": {
      "target_inputs_seen": [],
      "target_import_detected": false
    },
    "false_negative": {
      "demotion_or_nonpromotion": true,
      "required_object_already_present": false,
      "over_deflation_detected": false
    }
  },
  "source_refs": [
    "repo path or object id used as evidence"
  ]
}
```

This is minimal because every required distinction in the assignment needs at least one
corresponding observable:

| distinction | required observable |
|---|---|
| closure | previous non-closed verdict, new `closed`, source-derived or verified evidence, no same-session or target-import violation |
| same-status refinement | same verdict, changed missing object or blocker, refinement delta records a narrower object or upstream blocker |
| repetition | same verdict and same missing object/blocker with `unchanged_blocker = true` |
| downgrade | verdict rank moves away from closure, or resolved/conditional language is demoted to open/blocked/underdefined/fail/no-go |
| false negative | demotion or non-promotion occurs even though the demanded proof object is already present in admissible evidence |
| same-session circularity | flag is raised and closed in the same session without external or later-session verification |

### 3.2 Transition Classifier

The contract uses a deterministic classifier with this precedence order:

1. `same_session_circularity` if a flag is raised and closed in the same session without
   `external_verification_id` or `later_session_verification_id`.
2. `false_negative` if a downgrade or non-promotion demands an object that is already
   present in admissible source-derived, verified, external, or later-session evidence.
3. `closure` if the previous verdict was not closed, the new verdict is `closed`, and both
   same-session and target-import guards pass.
4. `downgrade` if the new verdict is lower than the previous verdict in the proof-status
   partial order and the false-negative guard does not fire.
5. `same_status_refinement` if verdict is unchanged but the missing object or blocker is
   narrowed, a prior missing object is closed, or a new upstream blocker is identified.
6. `repetition` if verdict, missing object, blocker family, and admissible evidence class
   are unchanged.
7. `upgrade_without_closure` for non-closed improvement such as `blocked` to
   `conditional`.
8. `new_item` when no prior row exists.

The proof-status order is intentionally partial, not total. `closed` is above all open
states. `conditional` is above `open`, `blocked`, and `underdefined` only when the named
condition is an explicit upstream object. `fail` and `no-go` are not lower than `blocked`;
they are decision states for bounded classes and require an explicit class boundary.
`host` and `import` are non-promotion states.

### 3.3 Example Row Family

The following rows are artificial examples shaped by the current repo blockers. They are
not retroactive claims about what the old runs proved; they show how future runs should
record transitions.

```json
[
  {
    "ledger_version": "LoopStateTransitionLedger_v1",
    "row_id": "3-1-5-4-c1-rs-001",
    "item_id": "RS_PHYSICAL_QUOTIENT_RANK_GATE",
    "lane_family": "rs",
    "session_id": "3-1-5-4-cycle1-2026-06-25",
    "cycle_index": 1,
    "artifact_path": "explorations/example-rs.md",
    "audit_path": "tests/example_rs_audit.py",
    "previous_state": {
      "verdict": "underdefined",
      "missing_object_id": "physical_effective_rank_certificate",
      "blocker_family": "rs_physical_quotient_rank",
      "evidence_basis": "prose_only"
    },
    "new_state": {
      "verdict": "underdefined",
      "missing_object_id": "d_RS_minus_1_source_defined_gauge_BRST_differential",
      "blocker_family": "rs_physical_quotient_rank",
      "evidence_basis": "source_derived"
    },
    "transition_type": "same_status_refinement",
    "transition_basis": "same verdict but the first missing object is narrowed to the source-defined BRST differential",
    "refinement_delta": {
      "narrower_missing_object": true,
      "closed_prior_missing_object": false,
      "introduced_upstream_blocker": false,
      "unchanged_blocker": false
    },
    "guards": {
      "same_session": {
        "flag_raised_session_id": null,
        "flag_closed_session_id": null,
        "external_verification_id": null,
        "later_session_verification_id": null,
        "deferred_verification_required": false,
        "same_session_closure_attempted": false
      },
      "target_import": {
        "target_inputs_seen": [],
        "target_import_detected": false
      },
      "false_negative": {
        "demotion_or_nonpromotion": true,
        "required_object_already_present": false,
        "over_deflation_detected": false
      }
    },
    "source_refs": [
      "explorations/hourly-cycle2-rs-physical-quotient-brst-complex-gate-2026-06-24.md"
    ]
  },
  {
    "ledger_version": "LoopStateTransitionLedger_v1",
    "row_id": "3-1-5-4-c1-qft-002",
    "item_id": "QFT_SOURCE_MODE_QUOTIENT_GATE",
    "lane_family": "qft",
    "session_id": "3-1-5-4-cycle1-2026-06-25",
    "cycle_index": 1,
    "artifact_path": "explorations/example-qft.md",
    "audit_path": "tests/example_qft_audit.py",
    "previous_state": {
      "verdict": "blocked",
      "missing_object_id": "SourceProjectorPFinBWithLocalModeRecords",
      "blocker_family": "qft_source_mode_quotient",
      "evidence_basis": "prose_only"
    },
    "new_state": {
      "verdict": "blocked",
      "missing_object_id": "SourceProjectorPFinBWithLocalModeRecords",
      "blocker_family": "qft_source_mode_quotient",
      "evidence_basis": "prose_only"
    },
    "transition_type": "repetition",
    "transition_basis": "same verdict, same missing object, same blocker family, and no stronger evidence basis",
    "refinement_delta": {
      "narrower_missing_object": false,
      "closed_prior_missing_object": false,
      "introduced_upstream_blocker": false,
      "unchanged_blocker": true
    },
    "guards": {
      "same_session": {
        "flag_raised_session_id": null,
        "flag_closed_session_id": null,
        "external_verification_id": null,
        "later_session_verification_id": null,
        "deferred_verification_required": false,
        "same_session_closure_attempted": false
      },
      "target_import": {
        "target_inputs_seen": [],
        "target_import_detected": false
      },
      "false_negative": {
        "demotion_or_nonpromotion": true,
        "required_object_already_present": false,
        "over_deflation_detected": false
      }
    },
    "source_refs": [
      "explorations/hourly-cycle2-qft-source-mode-quotient-data-ledger-2026-06-24.md"
    ]
  },
  {
    "ledger_version": "LoopStateTransitionLedger_v1",
    "row_id": "3-1-5-4-c1-vz-003",
    "item_id": "VZ_ACTUAL_OPERATOR_CERTIFICATE_GATE",
    "lane_family": "vz",
    "session_id": "3-1-5-4-cycle1-2026-06-25",
    "cycle_index": 1,
    "artifact_path": "explorations/example-vz.md",
    "audit_path": "tests/example_vz_audit.py",
    "previous_state": {
      "verdict": "conditional",
      "missing_object_id": "ActualDGU01OperatorCertificate",
      "blocker_family": "vz_actual_operator_subprincipal",
      "evidence_basis": "prose_only"
    },
    "new_state": {
      "verdict": "closed",
      "missing_object_id": null,
      "blocker_family": null,
      "evidence_basis": "verified_computation"
    },
    "transition_type": "closure",
    "transition_basis": "actual operator certificate supplied and audited outside the same-session guard",
    "refinement_delta": {
      "narrower_missing_object": false,
      "closed_prior_missing_object": true,
      "introduced_upstream_blocker": false,
      "unchanged_blocker": false
    },
    "guards": {
      "same_session": {
        "flag_raised_session_id": "3-1-5-4-cycle0-2026-06-24",
        "flag_closed_session_id": "3-1-5-4-cycle1-2026-06-25",
        "external_verification_id": "audit:vz_actual_operator_certificate:sha256-placeholder",
        "later_session_verification_id": null,
        "deferred_verification_required": false,
        "same_session_closure_attempted": false
      },
      "target_import": {
        "target_inputs_seen": [],
        "target_import_detected": false
      },
      "false_negative": {
        "demotion_or_nonpromotion": false,
        "required_object_already_present": true,
        "over_deflation_detected": false
      }
    },
    "source_refs": [
      "specifications/example-actual-dgu-operator-certificate.json",
      "tests/example_vz_audit.py"
    ]
  },
  {
    "ledger_version": "LoopStateTransitionLedger_v1",
    "row_id": "3-1-5-4-c1-gen-004",
    "item_id": "GENERATION_COUNT_BASELINE_SELECTION_GATE",
    "lane_family": "generation",
    "session_id": "3-1-5-4-cycle1-2026-06-25",
    "cycle_index": 1,
    "artifact_path": "explorations/example-generation.md",
    "audit_path": null,
    "previous_state": {
      "verdict": "conditional",
      "missing_object_id": "rank_H_candidate_dismissal",
      "blocker_family": "generation_candidate_selection",
      "evidence_basis": "same_session"
    },
    "new_state": {
      "verdict": "open",
      "missing_object_id": "source_defined_physical_rank_selector",
      "blocker_family": "generation_candidate_selection",
      "evidence_basis": "prose_only"
    },
    "transition_type": "downgrade",
    "transition_basis": "two undismissed candidates remain; baseline selection was verdict inflation",
    "refinement_delta": {
      "narrower_missing_object": true,
      "closed_prior_missing_object": false,
      "introduced_upstream_blocker": true,
      "unchanged_blocker": false
    },
    "guards": {
      "same_session": {
        "flag_raised_session_id": "2026-06-23-run-B",
        "flag_closed_session_id": null,
        "external_verification_id": null,
        "later_session_verification_id": null,
        "deferred_verification_required": true,
        "same_session_closure_attempted": false
      },
      "target_import": {
        "target_inputs_seen": [
          "three_generation_target"
        ],
        "target_import_detected": true
      },
      "false_negative": {
        "demotion_or_nonpromotion": true,
        "required_object_already_present": false,
        "over_deflation_detected": false
      }
    },
    "source_refs": [
      "process/loop-adversarial-log.md"
    ]
  },
  {
    "ledger_version": "LoopStateTransitionLedger_v1",
    "row_id": "3-1-5-4-c1-theta-005",
    "item_id": "THETA_XI_EFFECTIVE_COEFFICIENT_GATE",
    "lane_family": "ig_theta",
    "session_id": "3-1-5-4-cycle1-2026-06-25",
    "cycle_index": 1,
    "artifact_path": "explorations/example-theta.md",
    "audit_path": "tests/example_theta_audit.py",
    "previous_state": {
      "verdict": "blocked",
      "missing_object_id": "K_IG_selector",
      "blocker_family": "ig_theta_source_forced_selector",
      "evidence_basis": "prose_only"
    },
    "new_state": {
      "verdict": "blocked",
      "missing_object_id": "K_IG_selector",
      "blocker_family": "ig_theta_source_forced_selector",
      "evidence_basis": "source_derived"
    },
    "transition_type": "false_negative",
    "transition_basis": "example class: a future audit finds the demanded K_IG_selector was already present in admissible source evidence",
    "refinement_delta": {
      "narrower_missing_object": false,
      "closed_prior_missing_object": false,
      "introduced_upstream_blocker": false,
      "unchanged_blocker": false
    },
    "guards": {
      "same_session": {
        "flag_raised_session_id": null,
        "flag_closed_session_id": null,
        "external_verification_id": "audit:theta_selector_presence:sha256-placeholder",
        "later_session_verification_id": null,
        "deferred_verification_required": false,
        "same_session_closure_attempted": false
      },
      "target_import": {
        "target_inputs_seen": [],
        "target_import_detected": false
      },
      "false_negative": {
        "demotion_or_nonpromotion": true,
        "required_object_already_present": true,
        "over_deflation_detected": true
      }
    },
    "source_refs": [
      "specifications/example-k-ig-selector.json",
      "tests/example_theta_audit.py"
    ]
  },
  {
    "ledger_version": "LoopStateTransitionLedger_v1",
    "row_id": "3-1-5-4-c1-process-006",
    "item_id": "SAME_SESSION_FLAG_CLOSURE_GATE",
    "lane_family": "process",
    "session_id": "3-1-5-4-cycle1-2026-06-25",
    "cycle_index": 1,
    "artifact_path": "explorations/example-same-session.md",
    "audit_path": null,
    "previous_state": {
      "verdict": "blocked",
      "missing_object_id": "external_or_later_session_verification",
      "blocker_family": "same_session_circularity",
      "evidence_basis": "same_session"
    },
    "new_state": {
      "verdict": "conditional",
      "missing_object_id": "external_or_later_session_verification",
      "blocker_family": "same_session_circularity",
      "evidence_basis": "same_session"
    },
    "transition_type": "same_session_circularity",
    "transition_basis": "flag raised and closed in same session without external or later-session verification",
    "refinement_delta": {
      "narrower_missing_object": false,
      "closed_prior_missing_object": false,
      "introduced_upstream_blocker": false,
      "unchanged_blocker": true
    },
    "guards": {
      "same_session": {
        "flag_raised_session_id": "3-1-5-4-cycle1-2026-06-25",
        "flag_closed_session_id": "3-1-5-4-cycle1-2026-06-25",
        "external_verification_id": null,
        "later_session_verification_id": null,
        "deferred_verification_required": true,
        "same_session_closure_attempted": true
      },
      "target_import": {
        "target_inputs_seen": [],
        "target_import_detected": false
      },
      "false_negative": {
        "demotion_or_nonpromotion": false,
        "required_object_already_present": false,
        "over_deflation_detected": false
      }
    },
    "source_refs": [
      "process/loop-adversarial-log.md"
    ]
  }
]
```

## 4. The First Exact Obstruction Or Missing Proof Object

The first exact obstruction is:

```text
HistoricalPreStateTransitionRows_v1
```

The proposed ledger can classify future transitions because it observes both the prior
state and the new state under a stable `item_id`. It cannot prove retroactive convergence
from existing prose artifacts because the previous runs did not emit enough comparable
pre-state records.

The obstruction is not merely missing JSON formatting. It is missing pre-state evidence:

- stable item IDs are not universal across all prior blockers;
- old verdicts are sometimes prose labels rather than normalized enum values;
- same-session flags are known from the adversarial log but not row-linked to every
  claim-level artifact;
- false-negative detection requires checking whether the demanded object was already
  present before demotion, but prior runs do not consistently record the demanded object
  and admissible evidence basis before the transition;
- repeated blocker detection needs exact equality of `missing_object_id` and
  `blocker_family`, while prior artifacts often improve those names inside prose.

Therefore the strongest valid retroactive claim remains the Cycle 3 result: local blocker
precision improved in a bounded sample. A convergence proof would require a complete
historical transition ledger, not only this contract.

## 5. The Constructive Next Object That Would Remove Or Test The Obstruction

The next object is:

```text
HistoricalPreStateTransitionRows_v1
```

It should be a backfilled ledger for one bounded run family, with one row per stable
claim/gate before and after each cycle. It would not automatically prove convergence, but
it would test whether retrospective classification is possible without inventing state
not present in the artifacts.

Minimum acceptance test:

1. Pick one bounded family, such as the ten hourly Cycle 1/2 blocker artifacts.
2. Assign stable `item_id` values before reading later cycle results.
3. Backfill `previous_state` only from earlier artifacts and logs.
4. Backfill `new_state` only from the target artifact.
5. Mark any inferred field as `unknown` rather than filling it from later knowledge.
6. Run the same classifier used for future rows.
7. Report how many rows are classifiable, ambiguous, or blocked by missing pre-state.

If most rows require inference from later synthesis, the retroactive convergence route
fails and future-only instrumentation is the correct path. If most rows are classifiable
from earlier files alone, a bounded retrospective convergence audit becomes possible.

## 6. What This Means For The Relevant GU Claim

This artifact makes no new physics claim and promotes no GU reconstruction gate.

It improves the process layer needed to evaluate GU reconstruction work. Future
automation can distinguish mathematical closure from blocker refinement, repeated
failure, downgrade hygiene, false-negative over-deflation, and same-session circularity.
That matters because the current GU frontier contains many named missing proof objects;
without transition rows, repeated discovery of those objects can be mistaken either for
convergence or for useless churn.

The GU-relevant claim is therefore conditional:

```text
Future run convergence metrics are meaningful only after LoopStateTransitionLedger_v1
rows exist for the relevant claim/gate family.
```

The current repo can claim a contract for future instrumentation. It cannot claim
retroactive convergence for the old three-cycle run.

## 7. Next Meaningful Proof Or Computation Step

Implement the ledger in the next run wrapper:

- require each worker artifact JSON summary to include one `LoopStateTransitionLedger_v1`
  row or a declared reason no stable prior item exists;
- run a classifier audit before integration;
- reject same-session closure rows unless they cite external or later-session
  verification;
- report closure and calibration dashboards separately;
- attempt `HistoricalPreStateTransitionRows_v1` only as a bounded audit, not as proof
  inflation.

## 8. Machine-Readable JSON Summary

```json
{
  "artifact": "hourly_cycle1_loop_state_transition_ledger_contract",
  "version": "2026-06-25",
  "verdict": "conditional",
  "classification": "future_instrumentation_contract_supplied_retroactive_convergence_proof_blocked",
  "contract_id": "LoopStateTransitionLedger_v1",
  "contract_supplied": true,
  "retroactive_convergence_proof_claimed": false,
  "major_gu_claim_promoted": false,
  "derived_directly_from_sources": {
    "research_posture": [
      "construct_missing_objects_but_preserve_proof_labels",
      "forbid_verdict_inflation",
      "forbid_target_data_smuggling",
      "process_discipline_is_not_physics_evidence"
    ],
    "five_lane_frontier_run": [
      "decision_grade_artifacts_required",
      "exact_missing_proof_object_required",
      "controlled_verdict_vocabulary_required"
    ],
    "cycle3_loop_calibration": [
      "LoopStateTransitionLedger_v1_named_as_missing",
      "same_session_guard_required",
      "transition_fields_required_for_future_workers",
      "bounded_sample_does_not_prove_convergence"
    ],
    "three_cycle_synthesis": [
      "fifteen_quality_holes_not_major_closure",
      "future_runs_must_record_close_narrow_repeat_or_upstream_blocker",
      "LoopStateTransitionLedger_v1_is_next_frontier_process_object"
    ],
    "loop_adversarial_log": [
      "same_session_self_resolution_pressure_present",
      "candidate_selection_without_dismissal_stays_open",
      "reconstruction_grade_assumptions_cannot_support_resolved_canon_claims"
    ]
  },
  "required_row_fields": [
    "ledger_version",
    "row_id",
    "item_id",
    "lane_family",
    "session_id",
    "cycle_index",
    "artifact_path",
    "audit_path",
    "previous_state",
    "new_state",
    "transition_type",
    "transition_basis",
    "refinement_delta",
    "guards",
    "source_refs"
  ],
  "required_state_fields": [
    "verdict",
    "missing_object_id",
    "blocker_family",
    "evidence_basis"
  ],
  "required_guard_fields": {
    "same_session": [
      "flag_raised_session_id",
      "flag_closed_session_id",
      "external_verification_id",
      "later_session_verification_id",
      "deferred_verification_required",
      "same_session_closure_attempted"
    ],
    "target_import": [
      "target_inputs_seen",
      "target_import_detected"
    ],
    "false_negative": [
      "demotion_or_nonpromotion",
      "required_object_already_present",
      "over_deflation_detected"
    ]
  },
  "transition_types_required": [
    "closure",
    "same_status_refinement",
    "repetition",
    "downgrade",
    "false_negative",
    "same_session_circularity"
  ],
  "transition_types_optional": [
    "new_item",
    "upgrade_without_closure"
  ],
  "classifier_precedence": [
    "same_session_circularity",
    "false_negative",
    "closure",
    "downgrade",
    "same_status_refinement",
    "repetition",
    "upgrade_without_closure",
    "new_item"
  ],
  "example_rows": [
    {
      "row_id": "3-1-5-4-c1-rs-001",
      "item_id": "RS_PHYSICAL_QUOTIENT_RANK_GATE",
      "transition_type": "same_status_refinement",
      "previous_verdict": "underdefined",
      "new_verdict": "underdefined",
      "previous_missing_object_id": "physical_effective_rank_certificate",
      "new_missing_object_id": "d_RS_minus_1_source_defined_gauge_BRST_differential",
      "guard_pass": true
    },
    {
      "row_id": "3-1-5-4-c1-qft-002",
      "item_id": "QFT_SOURCE_MODE_QUOTIENT_GATE",
      "transition_type": "repetition",
      "previous_verdict": "blocked",
      "new_verdict": "blocked",
      "previous_missing_object_id": "SourceProjectorPFinBWithLocalModeRecords",
      "new_missing_object_id": "SourceProjectorPFinBWithLocalModeRecords",
      "guard_pass": true
    },
    {
      "row_id": "3-1-5-4-c1-vz-003",
      "item_id": "VZ_ACTUAL_OPERATOR_CERTIFICATE_GATE",
      "transition_type": "closure",
      "previous_verdict": "conditional",
      "new_verdict": "closed",
      "previous_missing_object_id": "ActualDGU01OperatorCertificate",
      "new_missing_object_id": null,
      "guard_pass": true
    },
    {
      "row_id": "3-1-5-4-c1-gen-004",
      "item_id": "GENERATION_COUNT_BASELINE_SELECTION_GATE",
      "transition_type": "downgrade",
      "previous_verdict": "conditional",
      "new_verdict": "open",
      "previous_missing_object_id": "rank_H_candidate_dismissal",
      "new_missing_object_id": "source_defined_physical_rank_selector",
      "guard_pass": true
    },
    {
      "row_id": "3-1-5-4-c1-theta-005",
      "item_id": "THETA_XI_EFFECTIVE_COEFFICIENT_GATE",
      "transition_type": "false_negative",
      "previous_verdict": "blocked",
      "new_verdict": "blocked",
      "previous_missing_object_id": "K_IG_selector",
      "new_missing_object_id": "K_IG_selector",
      "guard_pass": false,
      "over_deflation_detected": true
    },
    {
      "row_id": "3-1-5-4-c1-process-006",
      "item_id": "SAME_SESSION_FLAG_CLOSURE_GATE",
      "transition_type": "same_session_circularity",
      "previous_verdict": "blocked",
      "new_verdict": "conditional",
      "previous_missing_object_id": "external_or_later_session_verification",
      "new_missing_object_id": "external_or_later_session_verification",
      "guard_pass": false,
      "same_session_closure_attempted": true
    }
  ],
  "first_exact_obstruction": {
    "id": "HISTORICAL_PRE_STATE_TRANSITION_ROWS_V1",
    "name": "HistoricalPreStateTransitionRows_v1",
    "why_first": "retroactive convergence proof requires stable prior-state rows, not only later prose synthesis",
    "missing_components": [
      "universal_stable_item_ids",
      "normalized_previous_verdicts",
      "row_linked_same_session_flags",
      "pre_transition_required_object_presence",
      "exact_missing_object_and_blocker_equality_for_repetition"
    ]
  },
  "constructive_next_object": {
    "id": "HISTORICAL_PRE_STATE_TRANSITION_ROWS_V1",
    "purpose": "bounded backfill test for whether retrospective classification is possible without inventing prior state",
    "acceptance_test": [
      "choose_bounded_run_family",
      "assign_stable_item_ids_before_using_later_results",
      "backfill_previous_state_only_from_earlier_artifacts",
      "backfill_new_state_only_from_target_artifact",
      "mark_inferred_fields_unknown",
      "run_same_classifier",
      "report_classifiable_ambiguous_and_blocked_rows"
    ]
  },
  "impact_for_gu_claim": {
    "new_physics_claim": false,
    "future_convergence_metrics_condition": "LoopStateTransitionLedger_v1 rows exist for the relevant claim_or_gate_family",
    "old_three_cycle_convergence_status": "not_retroactively_proved",
    "process_gain": "future automation can separate closure, refinement, repetition, downgrade hygiene, false negatives, and same-session circularity"
  },
  "next_meaningful_step": "add LoopStateTransitionLedger_v1 row emission and classifier audit to the next run wrapper"
}
```
