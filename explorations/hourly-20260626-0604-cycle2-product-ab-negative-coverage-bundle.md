---
title: "Hourly 20260626 0604 Cycle 2 Product A/B Negative Coverage Bundle"
date: "2026-06-26"
run_id: "hourly-20260626-0604"
cycle: 2
lane: 4
doc_type: "frontier_run_lane_artifact"
artifact_id: "ProductABOperatorMemberNegativeCoverageBundle_0604_C2_V1"
verdict: "scoped_negative_bundle_defined_no_member_admitted"
owned_path: "explorations/hourly-20260626-0604-cycle2-product-ab-negative-coverage-bundle.md"
companion_audit: "tests/hourly_20260626_0604_cycle2_admission_predicates_audit.py"
claim_status_change: false
---

# Hourly 20260626 0604 Cycle 2 Product A/B Negative Coverage Bundle

## 1. Verdict

Verdict: **scoped negative bundle defined / no operator member admitted**.

Cycle 1 found no ProductAB-specific operator member. This lane turns that into a
coverage bundle rather than a global negative.

Decision state:

```text
negative_coverage_bundle_defined: true
operator_member_admitted: false
negative_is_global_no_go: false
surfaces_accounted_count: 4
locator_receipt_admitted: false
binding_gate_allowed: false
alpha_beta_identity_allowed: false
kig_restart_allowed: false
target_import_used: false
```

## 2. Scoped Coverage

| surface | scoped result |
|---|---|
| author manuscript | Shiab/Bianchi shell, no ProductB -> ProductA member |
| Oxford portal frames | visual candidate anchors, no ProductAB member identity |
| PTUJ/Keating | missing sheet locator, no formula-bearing member |
| UCSD transcript | Bianchi/contraction motivation, no located member |

The bundle is scoped to the above source surfaces. It is not a claim that no
ProductAB member exists in any future recovered notes, video frame, or alternate
source.

## 3. Obstruction And Next Object

First failed field:

```text
operator_member_id
```

Next object:

```text
RecoveredNotesOrFrameProductABMemberCandidate_V1
```

It must include a stable source locator and bind direction/domain/codomain
before any row-coefficient work is allowed.

## 4. Terrain And Claim-Status Result

Terrain: `provenance-verifier`, `spectral-phase`, `descent-quotient`.

No claim status changed.

## 5. JSON Summary

```json
{
  "artifact_id": "ProductABOperatorMemberNegativeCoverageBundle_0604_C2_V1",
  "run_id": "hourly-20260626-0604",
  "cycle": 2,
  "lane": 4,
  "artifact_path": "explorations/hourly-20260626-0604-cycle2-product-ab-negative-coverage-bundle.md",
  "verdict_class": "scoped_negative_bundle_defined_no_member_admitted",
  "negative_coverage_bundle_defined": true,
  "operator_member_admitted": false,
  "negative_is_global_no_go": false,
  "surfaces_accounted_count": 4,
  "locator_receipt_admitted": false,
  "binding_gate_allowed": false,
  "alpha_beta_identity_allowed": false,
  "kig_restart_allowed": false,
  "target_import_used": false,
  "claim_status_consistency_triggered": false,
  "first_failed_field": "operator_member_id",
  "next_frontier_object": "RecoveredNotesOrFrameProductABMemberCandidate_V1"
}
```
