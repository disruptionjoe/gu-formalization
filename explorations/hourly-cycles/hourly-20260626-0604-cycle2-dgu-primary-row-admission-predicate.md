---
title: "Hourly 20260626 0604 Cycle 2 DGU Primary Row Admission Predicate"
date: "2026-06-26"
run_id: "hourly-20260626-0604"
cycle: 2
lane: 1
doc_type: "frontier_run_lane_artifact"
artifact_id: "DGUPrimaryRowAdmissionPredicate_0604_C2_V1"
verdict: "predicate_defined_no_row_admitted"
owned_path: "explorations/hourly-20260626-0604-cycle2-dgu-primary-row-admission-predicate.md"
companion_audit: "tests/hourly_20260626_0604_cycle2_admission_predicates_audit.py"
claim_status_change: false
---

# Hourly 20260626 0604 Cycle 2 DGU Primary Row Admission Predicate

## 1. Verdict

Verdict: **predicate defined / no primary row admitted**.

Cycle 1 found no broader source-surface receipt for actual `D_GU^epsilon` 0/1.
This lane converts that blocker into an admission predicate:

```text
DGUPrimaryRowAdmissionPredicate_V1
```

Predicate status:

```text
predicate_defined: true
row_admitted_by_predicate: false
minimum_required_fields_count: 11
source_surfaces_can_be_retested: true
same_operator_witness_allowed: false
proof_restart_allowed: false
target_import_used: false
```

## 2. Predicate

A candidate row is admitted only if all fields pass:

| field | admission rule |
|---|---|
| `source_id` | primary or source-equivalent GU surface, not downstream repo reconstruction |
| `source_locator` | stable page, frame, timestamp, transcript window, or checksum |
| `sector_rule_id` | source-emitted 0/1 sector rule, not adjacent terminology |
| `operator_family_id` | actual `D_GU^epsilon`, not typed `D_roll` replay |
| `domain_handle` | source-specified input space |
| `codomain_handle` | source-specified output space |
| `coefficient_policy` | source-specified, explicitly absent, or not admitted |
| `projector_policy` | source-specified sector/projector rule |
| `symbol_or_lower_order_policy` | source-specified principal/lower-order data or declared absent |
| `family_identity_evidence` | source row is identical to actual `D_GU^epsilon` 0/1 |
| `anti_target_smuggling_screen` | no VZ, RS, K3, generation, exact-GR, theta, or target success input |

First hard failure for current sources:

```text
sector_rule_id + family_identity_evidence
```

## 3. Strongest Positive Attempt

The 0502 and 0604 source sweeps plus the 0711 rendered images supply candidate
locators, not admitted rows. A future candidate can now be tested row-by-row
instead of being rejected by prose.

The strongest candidate class remains:

```text
source locator with actual DGU 0/1 adjacency, pending sector_rule_id and family identity.
```

## 4. Obstruction And Next Object

The obstruction is not lack of a checklist. The checklist now exists. The
obstruction is an empty candidate set satisfying it.

Next object:

```text
PositivePrimarySourceDGU01SectorRuleRowCandidate_V1
```

Rollback / falsification condition:

```text
If a primary source candidate fills all predicate fields without target input,
the scoped negative receipt is replaced by a positive candidate row and the
same-operator witness becomes evaluable.
```

## 5. Terrain And Claim-Status Result

Terrain: `provenance-verifier`.

No claim status changed. No canon, roadmap, or status file was edited.

## 6. JSON Summary

```json
{
  "artifact_id": "DGUPrimaryRowAdmissionPredicate_0604_C2_V1",
  "run_id": "hourly-20260626-0604",
  "cycle": 2,
  "lane": 1,
  "artifact_path": "explorations/hourly-20260626-0604-cycle2-dgu-primary-row-admission-predicate.md",
  "verdict_class": "predicate_defined_no_row_admitted",
  "predicate_defined": true,
  "row_admitted_by_predicate": false,
  "minimum_required_fields_count": 11,
  "first_failed_fields": ["sector_rule_id", "family_identity_evidence"],
  "same_operator_witness_allowed": false,
  "proof_restart_allowed": false,
  "target_import_used": false,
  "claim_status_consistency_triggered": false,
  "next_frontier_object": "PositivePrimarySourceDGU01SectorRuleRowCandidate_V1"
}
```
