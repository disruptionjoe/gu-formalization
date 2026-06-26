---
title: "Hourly 20260626 0604 Cycle 2 KIG Rival Class Eliminator Preorder"
date: "2026-06-26"
run_id: "hourly-20260626-0604"
cycle: 2
lane: 3
doc_type: "frontier_run_lane_artifact"
artifact_id: "KIGRivalClassEliminatorPreorder_0604_C2_V1"
verdict: "preorder_defined_multiple_classes_survive"
owned_path: "explorations/hourly-20260626-0604-cycle2-kig-rival-class-eliminator-preorder.md"
companion_audit: "tests/hourly_20260626_0604_cycle2_admission_predicates_audit.py"
claim_status_change: false
---

# Hourly 20260626 0604 Cycle 2 KIG Rival Class Eliminator Preorder

## 1. Verdict

Verdict: **preorder defined / multiple classes survive**.

Cycle 1 found no exterior-codomain finality axiom. This lane defines a
source-only preorder for candidate `K_IG` classes. It does not select `D_A U`.

Decision state:

```text
preorder_defined: true
singleton_survivor: false
surviving_class_count: 5
d_a_u_still_strongest_candidate: true
d_a_u_source_forced: false
branch3_admitted: false
target_import_used: false
```

## 2. Preorder

Each candidate class is compared by:

```text
codomain_finality
parent_momentum_degree_finality
boundary_class_control
projector_loss_control
lower_order_rigidity
source_locator_strength
target_independence
```

Survivors:

| class | reason it survives |
|---|---|
| `EXT_DERIVATIVE` | strongest local gauge-covariant exterior candidate |
| `CODERIVATIVE_TRACE` | no source axiom excludes contraction/trace codomains |
| `SYMMETRIC_DERIVATIVE` | no source axiom excludes symmetric gradient data |
| `PROJECTED_DERIVATIVE` | projection-loss theorem absent |
| `LOWER_ORDER_DRESSED_EXTERIOR` | lower-order rigidity theorem absent |

## 3. Obstruction And Next Object

The first failed preorder field is:

```text
eliminator_for_all_non_exterior_classes
```

Next object:

```text
KIGExteriorSingletonSurvivalCertificate_V1
```

That certificate must either eliminate all non-exterior rivals or admit that
Branch 3 remains underdefined.

## 4. Terrain And Claim-Status Result

Terrain: `local-gauge-operator-selection`, guarded by `provenance-verifier`.

No claim status changed.

## 5. JSON Summary

```json
{
  "artifact_id": "KIGRivalClassEliminatorPreorder_0604_C2_V1",
  "run_id": "hourly-20260626-0604",
  "cycle": 2,
  "lane": 3,
  "artifact_path": "explorations/hourly-20260626-0604-cycle2-kig-rival-class-eliminator-preorder.md",
  "verdict_class": "preorder_defined_multiple_classes_survive",
  "preorder_defined": true,
  "singleton_survivor": false,
  "surviving_class_count": 5,
  "d_a_u_still_strongest_candidate": true,
  "d_a_u_source_forced": false,
  "branch3_admitted": false,
  "surviving_classes": [
    "EXT_DERIVATIVE",
    "CODERIVATIVE_TRACE",
    "SYMMETRIC_DERIVATIVE",
    "PROJECTED_DERIVATIVE",
    "LOWER_ORDER_DRESSED_EXTERIOR"
  ],
  "target_import_used": false,
  "claim_status_consistency_triggered": false,
  "first_failed_field": "eliminator_for_all_non_exterior_classes",
  "next_frontier_object": "KIGExteriorSingletonSurvivalCertificate_V1"
}
```
