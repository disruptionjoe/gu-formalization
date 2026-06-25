---
title: "Hourly Cycle 3 Loop Convergence / False-Negative Calibration"
date: 2026-06-24
status: exploration/calibration
doc_type: hourly_cycle3_loop_convergence_false_negative_calibration
verdict: "UNDER_INSTRUMENTED_WITH_LOCAL_BLOCKER_CONVERGENCE"
owned_path: "explorations/hourly-cycle3-loop-convergence-false-negative-calibration-2026-06-24.md"
companion_audit: "tests/hourly_cycle3_loop_convergence_false_negative_calibration_audit.py"
depends_on:
  - "RESEARCH-POSTURE.md"
  - "process/runbooks/five-lane-frontier-run.md"
  - "process/loop-adversarial-log.md"
  - "roadmap/objection-triage-register.md"
  - "explorations/cycle3-single-surviving-prediction-census-2026-06-24.md"
  - "explorations/hourly-cycle1-observer-shadow-phi-obs-contract-2026-06-24.md"
  - "explorations/hourly-cycle1-qft-finite-quotient-gram-gate-2026-06-24.md"
  - "explorations/hourly-cycle1-rs-effective-rank-certificate-2026-06-24.md"
  - "explorations/hourly-cycle1-source-forced-theta-coefficient-packet-2026-06-24.md"
  - "explorations/hourly-cycle1-vz-subprincipal-characteristic-contract-2026-06-24.md"
  - "explorations/hourly-cycle2-fixed-data-phi-obs-sector-ledger-2026-06-24.md"
  - "explorations/hourly-cycle2-qft-source-mode-quotient-data-ledger-2026-06-24.md"
  - "explorations/hourly-cycle2-rs-physical-quotient-brst-complex-gate-2026-06-24.md"
  - "explorations/hourly-cycle2-source-forced-ig-dynamics-selector-v0-2026-06-24.md"
  - "explorations/hourly-cycle2-vz-actual-operator-certificate-gate-2026-06-24.md"
---

# Hourly Cycle 3 Loop Convergence / False-Negative Calibration

## 1. Verdict

**Verdict: UNDER_INSTRUMENTED_WITH_LOCAL_BLOCKER_CONVERGENCE.**

The current loop should not be called converged. The bounded sample shows
useful local convergence toward sharper obstruction objects, and it does not
show a recent false-negative over-deflation problem. But it is still
under-instrumented for a decision-grade convergence claim because the repo lacks
a stable per-item state-transition ledger.

Current read:

```text
resolved gain: 0
blocked/underdefined precision gain: 9 hourly artifacts
bounded no-go / negative-selector gain: 1 hourly artifact
open precision gain: 10 hourly artifacts with named next proof objects or blockers
same-session circularity pressure: present in 2/2 adversarial log runs
recent false-negative verdict: no false-negative found in the bounded sample
overall loop classification: under-instrumented, locally converging on blockers
```

This is not thrashing in the narrow "oscillating between upgrades and
downgrades" sense: the current hourly artifacts do not upgrade claims and then
retract them. They mostly refuse promotion and name smaller gates. The apparent
churn is largely correction of prior verdict inflation plus repeated discovery
that source-selection data is missing.

It is also not full convergence. A loop can repeatedly sharpen blockers while
still failing to close the central GU reconstruction gates. The sample supports
"better calibrated and less inflated" more strongly than "mathematically
convergent."

## 2. Metric Definitions

The metrics below separate mathematical closure from calibration progress.

| metric | definition | what counts | what does not count |
|---|---|---|---|
| `resolved_gain` | Count of sampled artifacts that close or promote a claim to proof-grade / resolved status. | A closed proof, verified computation, or explicitly promoted result with rollback conditions. | A conditional route, host-only compatibility, or named future computation. |
| `blocked_or_underdefined_precision_gain` | Count of sampled artifacts that replace a vague open claim with a named blocked or underdefined object. | `ActualDGU01OperatorCertificate`, `SourceProjectorPFinBWithLocalModeRecords`, `d_RS,-1`, `K_IG_selector`, and similar exact blockers. | Merely saying "more work needed." |
| `bounded_no_go_or_negative_selector_gain` | Count of sampled artifacts that rule out a bounded class of candidate routes. | Current instantiated Type II_1 fixed-data / C3-D4 selector candidates fail as explanatory selectors. | A global no-go against GU or against all possible future selector classes. |
| `open_precision_gain` | Count of sampled artifacts that keep a claim open but attach a first exact missing proof object, field, or gate. | Any hourly artifact that leaves a branch open while naming its next proof object. | An unstructured OPEN label. |
| `repeated_blocker_rate` | Fraction of hourly artifact instances whose blocker family appears in more than one sampled artifact. | Repeated family examples: QFT source-mode quotient, RS physical quotient, VZ actual operator, IG/theta source selector, Phi_obs target provenance. | Repetition without improved specificity, if a later state-transition ledger shows no refinement. |
| `downgrade_upgrade_churn` | Ratio of explicit downgrade or blocked-upgrade events to explicit upgrade events in the same bounded sample. | Log-listed verdict-inflation corrections, same-session upgrade blocks, and candidate demotions. | Open blockers that are not transitions from a prior higher verdict. |
| `same_session_circularity_pressure` | Rate at which adversarial logs find flags raised and closed in the same session without external verification. | The two adversarial-log runs both record same-session self-resolution pressure. | A later artifact that cites a same-session file only as context while refusing promotion. |
| `false_negative_rate` | Fraction of audited recent demotions that look over-deflated relative to the proof state. | A demotion would count as false-negative if the source already supplied the proof object demanded by the demotion. | A demotion because the required source object is absent, target-smuggled, or same-session only. |

The current sample can compute these as a bounded calibration read. It cannot
compute true loop convergence, because it lacks stable item IDs and prior-to-new
verdict transitions for every lane.

## 3. Current Sample / Readout From Loop Log And Hourly Cycles

### 3.1 Sample boundary

This read uses three source classes:

| source class | count | role in this read |
|---|---:|---|
| adversarial-log runs | 2 | process-level failure modes, issue counts, same-session pressure |
| hourly Cycle 1/2 artifacts | 10 | current blocker and demotion sample |
| Cycle 3 prediction-census candidates | 10 | current central-prediction status |

The adversarial log records:

| run | completed | fixed | issues total | critical/moderate | minor |
|---|---:|---:|---:|---:|---:|
| 2026-06-23 run A | 10/10 | 8 | 10 | 8 | 2 |
| 2026-06-23 run B | 9/9 | 11 | 14 | 11 | 3 |
| total | 19/19 | 19 | 24 | 19 | 5 |

So the process loop is finding and correcting many review issues. That is
calibration progress, not mathematical closure. The log does not provide enough
transition data to say how many research claims moved from OPEN to RESOLVED or
from RESOLVED back to OPEN across stable item IDs.

### 3.2 Net status gain vector for the hourly artifacts

| lane family | sampled artifacts | current read | counted gain |
|---|---:|---|---|
| Phi_obs / fixed-data selector / target provenance | 2 | underdefined contract and no current fixed-data selector | 1 underdefined precision, 1 bounded negative-selector gain |
| QFT source-mode quotient / finite Gram | 2 | both blocked before source projector, modes, raw Gram, quotient, and positivity | 2 blocked precision gains |
| RS effective rank / BRST quotient | 2 | both underdefined before physical module, BRST differential, H-linear trace, and source-selected background | 2 underdefined precision gains |
| theta / IG source-forced dynamics | 2 | both blocked or underdefined before `SourceForcedIGDynamicsSelector` / `K_IG_selector` | 2 blocked/underdefined precision gains |
| VZ actual operator / subprincipal gate | 2 | both underdefined or blocked before actual `D_GU` 0/1 operator and section-pulled subprincipal certificates | 2 underdefined precision gains |

Exclusive count over the ten hourly artifacts:

```text
resolved_gain = 0
blocked_or_underdefined_precision_gain = 9
bounded_no_go_or_negative_selector_gain = 1
open_precision_gain = 10
net_research_closure_claimed = false
```

The count is exclusive for the first three rows: the fixed-data Phi_obs ledger is
counted as the single bounded negative-selector result rather than also counted
as blocked. The `open_precision_gain` count is non-exclusive: all ten artifacts
leave central claims open while naming a sharper proof object or blocker.

### 3.3 Repeated blocker rate

Every sampled hourly artifact belongs to a blocker family that appears twice in
the ten-artifact sample. Therefore:

```text
repeated_blocker_rate = 10 / 10 = 1.00
```

That looks dangerous if repetition means the loop is circling. Here, the
repetition mostly means Cycle 2 sharpened Cycle 1's blockers:

| family | Cycle 1 object | Cycle 2 refinement |
|---|---|---|
| QFT | `SourceDerivedFiniteQuotientGramData` | `SourceProjectorPFinBWithLocalModeRecords` |
| RS | physical/effective rank certificate missing | `d_RS,-1` source-defined gauge/BRST differential |
| VZ | source-closed actual `D_GU` 0/1 certificate | `ActualDGU01OperatorCertificate` plus downstream section certificate |
| IG/theta | `SourceForcedIGDynamicsSelector` | `K_IG_selector` as first missing source datum |
| Phi_obs | finite Connes-channel / replacement shadow contract | fixed-data selector ledger and C3/D4 negative control |

So the repeated blocker rate is high, but it is not by itself evidence of
thrashing. It becomes thrashing only if the next loop repeats the same families
without either closing one named proof object or recording why no narrower
object exists.

### 3.4 Downgrade / upgrade churn

The adversarial log gives a lower-bound count of explicit demotion or
blocked-upgrade events:

| source | explicit events counted | examples |
|---|---:|---|
| run A | 4 | two RESOLVED grade mismatches, E-block same-session circularity, norm-fiber contradiction labeled closed |
| run B | 5 | VZ-01 same-session block, H3-01 partial re-resolution, generation candidate baseline demotion, dark-energy canon assumption demotion, shiab gap caution |
| total lower bound | 9 | correction pressure, not proof closure |

Current hourly sample:

```text
explicit upgrades = 0
explicit current non-promotion / demotion gates = 10
downgrade_upgrade_ratio = undefined because upgrades = 0
```

This is not ordinary churn. There is no observed upgrade/downgrade oscillation
inside the current hourly sample. The pressure is one-directional: stop calling
things resolved until the source object exists.

### 3.5 Same-session circularity pressure

The same-session issue is severe in the adversarial log:

```text
adversarial log runs with same-session circularity pressure = 2 / 2
same-session pressure rate = 1.00
```

The current hourly artifacts do not attempt same-session closure of the sampled
central gates, but their JSON summaries also do not carry a uniform
`same_session_guard` field. The guard is a rule in prose, not yet a
machine-readable transition invariant.

## 4. False-Negative Audit: Were Recent Demotions Warranted?

**False-negative verdict: NO_FALSE_NEGATIVE_FOUND_IN_BOUNDED_SAMPLE.**

The recent OPEN/BLOCKED demotions look warranted in this bounded sample. They
are not demoting proved results. They are demoting or refusing promotion because
the source-side object has not been supplied, the closure is same-session only,
or the candidate imports target data.

| demotion / non-promotion | current status | false-negative read |
|---|---|---|
| generation count Candidate A vs Candidate B | OPEN; rank 4 and rank 8 remain undismissed until physical RS rank is source-derived | warranted; selecting three generations before the physical rank would import the target |
| dark-energy / theta `xi_eff` route | BLOCKED before source-forced action and coefficient packet | warranted; no `Z_theta`, `C_Rtheta`, or `xi_eff` has been emitted from the source side |
| VZ closure | CONDITIONAL / BLOCKED before actual operator and subprincipal certificates | warranted; typed-spine algebra is positive evidence but not the actual GU operator |
| QFT / CHSH | BLOCKED before source projector, modes, raw Gram, quotient, positive state, covariance, and observables | warranted; identity Gram, Bell state, Pauli controls, and free vacuum are controls/imports unless source-derived |
| Type II_1 / Phi_obs selector language | no current fixed-data selector; instantiated candidates host or fail as selectors | warranted; C3/D4 and finite-control data do not select target SM data without imports |
| same-session self-resolution | upgrade blocked until later verification or formal demotion | warranted; file separation is not independent verification |
| Cycle 3 prediction census | no current concrete surviving empirical prediction | warranted; every candidate is still reconstruction-grade, source-dependent, or control-only |

The strongest possible over-deflation worry is that the loop may be using
OPEN/BLOCKED labels for live constructive leads. That worry is real at the
portfolio level, but it is not a false-negative finding here. Each demoted lead
still names a promotion condition. The demotion is against current proof grade,
not against pursuing the route.

## 5. Strongest Positive Convergence Finding

The strongest positive finding is that the loop is converging on exact first
obstructions. In the ten hourly artifacts, every lane family has a named next
object:

| family | first object now visible |
|---|---|
| QFT | `SourceProjectorPFinBWithLocalModeRecords`, then raw Gram and quotient representatives |
| RS | source-defined gauge/BRST differential `d_RS,-1` and a common H-linear physical module |
| VZ | `ActualDGU01OperatorCertificate`, then `ActualDGUSectionSubprincipalCertificate` |
| IG/theta | `K_IG_selector` inside `SourceForcedIGDynamicsSelector` |
| Phi_obs | fixed-data `Phi_obs` selector or declared replacement observer shadow with target-provenance rows |

This is a real convergence signal because it turns broad objections into
computable or falsifiable proof objects. It also aligns with the Mission A
posture: build the missing source objects or kill routes cleanly.

The finding is limited. It is convergence of problem statements and blocker
granularity, not convergence of mathematical claims to closure.

## 6. First Exact Obstruction Or Missing Metric

The first missing artifact is:

```text
LoopStateTransitionLedger_v1
```

It must be a machine-readable file, not prose inside each artifact. Minimum row
schema:

```json
{
  "item_id": "stable repo-local claim or gate id",
  "lane_family": "qft|rs|vz|ig_theta|phi_obs|generation|dark_energy|other",
  "session_id": "run or hourly cycle id",
  "artifact_path": "path/to/artifact.md",
  "previous_verdict": "resolved|conditional|open|blocked|underdefined|no-go|unknown",
  "new_verdict": "resolved|conditional|open|blocked|underdefined|no-go",
  "transition_type": "upgrade|downgrade|same_status_refinement|new_item",
  "first_missing_object_id": "stable object id or null",
  "blocker_family": "stable blocker-family tag",
  "evidence_basis": "source_derived|verified_computation|same_session|external_verification|target_import|prose_only",
  "flag_raised_session_id": "session id or null",
  "flag_closed_session_id": "session id or null",
  "same_session_guard": {
    "can_close_same_session_flags": false,
    "external_verification_id": "id or null",
    "deferred_verification_required": true
  },
  "target_import_guard": {
    "target_inputs_seen": [],
    "target_import_detected": false
  },
  "audit_path": "path/to/audit.py or null"
}
```

Without this ledger, `resolved_gain`, `downgrade_upgrade_churn`, and
`false_negative_rate` remain bounded estimates. The loop can report local
calibration, but it cannot prove convergence or distinguish repeated useful
refinement from slow thrashing.

## 7. Impact For Future Automation Runs

Future automation runs should keep the current deflation guard. The recent
demotions are warranted, and relaxing them would reintroduce verdict inflation.

The next automation improvement should be instrumentation, not a softer verdict
policy:

1. Add `LoopStateTransitionLedger_v1` rows for every lane before and after a run.
2. Require each worker JSON summary to include `item_id`, `previous_verdict`,
   `new_verdict`, `transition_type`, `blocker_family`,
   `first_missing_object_id`, and `same_session_guard`.
3. For repeated blocker families, require the worker to state whether the run
   closed a prior blocker, narrowed it, repeated it unchanged, or discovered a
   new upstream blocker.
4. Treat same-session closures as `DEFERRED_VERIFICATION` unless an external
   computation or later-session artifact is cited by ID.
5. Report two separate dashboards: mathematical closure and calibration
   hygiene. Combining them hides the difference between progress and cleanup.

Operational classification for the next run:

```text
loop_status = UNDER_INSTRUMENTED
calibration_status = IMPROVING
research_closure_status = NOT_YET_CONVERGED
false_negative_status = NO_FALSE_NEGATIVE_FOUND_IN_SAMPLE
next_required_artifact = LoopStateTransitionLedger_v1
```

## 8. Machine-Readable JSON Summary

```json
{
  "artifact": "hourly_cycle3_loop_convergence_false_negative_calibration",
  "version": "2026-06-24",
  "verdict": "UNDER_INSTRUMENTED_WITH_LOCAL_BLOCKER_CONVERGENCE",
  "classification": "under_instrumented",
  "convergence_claimed": false,
  "thrashing_claimed": false,
  "metrics_partial": true,
  "bounded_sample_only": true,
  "sample_counts": {
    "adversarial_log_runs": 2,
    "adversarial_log_items_completed": 19,
    "adversarial_log_issues_total": 24,
    "adversarial_log_issues_fixed": 19,
    "adversarial_log_critical_or_moderate_issues": 19,
    "adversarial_log_minor_issues": 5,
    "hourly_artifacts": 10,
    "cycle3_census_candidates": 10
  },
  "metric_definitions": {
    "resolved_gain": "sampled artifacts that close or promote a claim to proof-grade or resolved status",
    "blocked_or_underdefined_precision_gain": "sampled artifacts that replace a vague open claim with a named blocked or underdefined object",
    "bounded_no_go_or_negative_selector_gain": "sampled artifacts that rule out a bounded class of candidate routes without claiming a global GU no-go",
    "open_precision_gain": "sampled artifacts that keep a claim open but attach a first exact missing proof object, field, or gate",
    "repeated_blocker_rate": "hourly artifact instances whose blocker family appears more than once divided by hourly artifact count",
    "downgrade_upgrade_churn": "explicit downgrade or blocked-upgrade events divided by explicit upgrade events in the bounded sample",
    "same_session_circularity_pressure": "adversarial-log runs with same-session self-resolution pressure divided by adversarial-log run count",
    "false_negative_rate": "audited recent demotions judged over-deflated divided by audited recent demotions"
  },
  "net_status_gain": {
    "resolved_gain": 0,
    "blocked_or_underdefined_precision_gain": 9,
    "bounded_no_go_or_negative_selector_gain": 1,
    "open_precision_gain": 10,
    "net_research_closure_claimed": false,
    "interpretation": "local blocker precision improved, but no sampled central claim was resolved"
  },
  "repeated_blocker_rate": {
    "hourly_artifact_instances_in_repeated_families": 10,
    "hourly_artifact_count": 10,
    "rate": 1.0,
    "family_count": 5,
    "families": [
      {
        "family": "phi_obs_fixed_data_target_provenance",
        "artifact_count": 2,
        "cycle1_object": "finite_Connes_channel_or_replacement_shadow_contract",
        "cycle2_refinement": "fixed_data_selector_ledger_and_C3_D4_negative_control"
      },
      {
        "family": "qft_source_mode_quotient",
        "artifact_count": 2,
        "cycle1_object": "SourceDerivedFiniteQuotientGramData",
        "cycle2_refinement": "SourceProjectorPFinBWithLocalModeRecords"
      },
      {
        "family": "rs_physical_quotient_rank",
        "artifact_count": 2,
        "cycle1_object": "physical_effective_rank_certificate",
        "cycle2_refinement": "d_RS_minus_1_source_defined_gauge_BRST_differential"
      },
      {
        "family": "ig_theta_source_forced_selector",
        "artifact_count": 2,
        "cycle1_object": "SourceForcedIGDynamicsSelector",
        "cycle2_refinement": "K_IG_selector"
      },
      {
        "family": "vz_actual_operator_subprincipal",
        "artifact_count": 2,
        "cycle1_object": "source_closed_actual_D_GU_0_1_operator_certificate",
        "cycle2_refinement": "ActualDGU01OperatorCertificate"
      }
    ]
  },
  "downgrade_upgrade_churn": {
    "explicit_log_downgrade_or_blocked_upgrade_events_lower_bound": 9,
    "current_hourly_explicit_upgrades": 0,
    "current_hourly_nonpromotion_or_demotion_gates": 10,
    "ratio": "undefined_zero_upgrades",
    "interpretation": "one_directional_deflation_and_blocker_refinement_not_observed_upgrade_downgrade_oscillation"
  },
  "same_session_guard": {
    "guard_required": true,
    "can_close_same_session_flags": false,
    "adversarial_log_runs_with_same_session_pressure": 2,
    "adversarial_log_runs": 2,
    "same_session_pressure_rate": 1.0,
    "hourly_artifacts_with_same_session_closure_attempts_found": 0,
    "missing_machine_readable_same_session_field_in_prior_hourlies": true,
    "next_required_field": "same_session_guard",
    "required_decision": "DEFERRED_VERIFICATION_unless_external_or_later_session_verification_exists"
  },
  "false_negative_audit": {
    "verdict": "NO_FALSE_NEGATIVE_FOUND_IN_BOUNDED_SAMPLE",
    "recent_demotions_warranted": true,
    "recent_demotions_over_deflated": false,
    "audited_demotions_count": 7,
    "over_deflated_count": 0,
    "false_negative_rate": 0.0,
    "audited_demotions": [
      {
        "id": "generation_count_candidate_A_baseline_to_OPEN",
        "warranted": true,
        "reason": "rank_H_4_and_rank_H_8_remain_undismissed_until_physical_RS_rank_is_source_derived"
      },
      {
        "id": "dark_energy_theta_xi_eff_to_BLOCKED",
        "warranted": true,
        "reason": "source_forced_action_Z_theta_C_Rtheta_and_xi_eff_not_emitted"
      },
      {
        "id": "vz_full_closure_to_CONDITIONAL_BLOCKED",
        "warranted": true,
        "reason": "typed_spine_algebra_is_not_actual_DGU_operator_or_section_pulled_subprincipal_certificate"
      },
      {
        "id": "qft_chsh_to_BLOCKED",
        "warranted": true,
        "reason": "source_projector_modes_H_raw_Q_b_positive_state_covariance_and_observables_missing"
      },
      {
        "id": "type_ii1_phi_obs_selector_to_NO_CURRENT_SELECTOR",
        "warranted": true,
        "reason": "current_candidates_host_or_import_target_data_and_do_not_fixed_data_select_SM_packet"
      },
      {
        "id": "same_session_self_resolution_to_DEFERRED_VERIFICATION",
        "warranted": true,
        "reason": "same_session_file_boundary_is_not_independent_verification"
      },
      {
        "id": "cycle3_prediction_census_to_NO_CURRENT_SURVIVING_PREDICTION",
        "warranted": true,
        "reason": "all_candidates_remain_reconstruction_grade_source_dependent_control_only_or_blocked"
      }
    ]
  },
  "strongest_positive_convergence_finding": {
    "finding": "all_ten_hourly_artifacts_name_first_obstruction_or_missing_object",
    "claim_scope": "blocker_granularity_not_mathematical_closure",
    "families_with_named_next_objects": [
      "qft_source_projector_mode_quotient_packet",
      "rs_source_defined_gauge_BRST_differential",
      "vz_actual_DGU_operator_certificate",
      "ig_theta_K_IG_selector",
      "phi_obs_fixed_data_selector_or_replacement_shadow"
    ]
  },
  "first_exact_missing_metric_artifact": {
    "id": "LOOP_STATE_TRANSITION_LEDGER_V1",
    "name": "LoopStateTransitionLedger_v1",
    "why_missing_first": "without stable item-level prior and new verdict rows, convergence and churn cannot be computed beyond bounded estimates",
    "required_fields": [
      "item_id",
      "lane_family",
      "session_id",
      "artifact_path",
      "previous_verdict",
      "new_verdict",
      "transition_type",
      "first_missing_object_id",
      "blocker_family",
      "evidence_basis",
      "flag_raised_session_id",
      "flag_closed_session_id",
      "same_session_guard",
      "target_import_guard",
      "audit_path"
    ]
  },
  "impact_for_future_automation_runs": {
    "keep_deflation_guard": true,
    "relax_verdict_policy": false,
    "add_transition_ledger": true,
    "require_worker_transition_fields": true,
    "separate_dashboards": [
      "mathematical_closure",
      "calibration_hygiene"
    ],
    "next_operational_status": {
      "loop_status": "UNDER_INSTRUMENTED",
      "calibration_status": "IMPROVING",
      "research_closure_status": "NOT_YET_CONVERGED",
      "false_negative_status": "NO_FALSE_NEGATIVE_FOUND_IN_SAMPLE",
      "next_required_artifact": "LoopStateTransitionLedger_v1"
    }
  }
}
```
