---
title: "Hourly 20260626 0103 Cycle 2 PTUJ Cross-Branch Assembly Firewall"
date: "2026-06-25"
run_id: "hourly-20260626-0103"
cycle: 2
lane: "PTUJ"
doc_type: "frontier_gate"
artifact_id: "PTUJCrossBranchAssemblyFirewall_0103_C2_PTUJ_V1"
verdict: "blocked_cross_branch_assembly_forbidden"
owned_path: "explorations/hourly-20260626-0103-cycle2-ptuj-cross-branch-assembly-firewall.md"
---

# Hourly 20260626 0103 Cycle 2 PTUJ Cross-Branch Assembly Firewall

## 1. Verdict

Verdict: **blocked**.

Cycle 1 showed that neither PTUJ branch has a complete field set. This lane
tests the common escape hatch: assembling official/custodian metadata with
lawful-local toolchain schema. That mixed packet is rejected.

Decision state:

```text
cycle1_consumed: true
target_import_used: false
official_branch_complete: false
lawful_local_branch_complete: false
mixed_packet_rejected: true
cross_branch_firewall_active: true
branch_purity_invariant_defined: true
branch_purity_invariant_satisfied: false
accepted_branch_count: 0
accepted_receipt_count: 0
formula_visibility_allowed: false
proof_restart_allowed: false
claim_status_consistency_triggered: false
```

## 2. Sources Read First

| source | use |
|---|---|
| `explorations/hourly-20260626-0103-cycle1-ptuj-branch-packet-field-ledger.md` | Consumed the two branch field ledgers. |
| `explorations/hourly-20260626-0002-cycle2-ptuj-branch-purity-recheck-gate.md` | Inherited the branch-purity invariant. |
| `sources/media-index.md` | Checked that metadata remains metadata only. |

## 3. Strongest Positive Construction Attempt

A mixed packet would look like:

```text
official metadata locator
+ lawful-local extraction schema
+ no admitted byte object
+ no source asset custody
+ no checksum/output manifest
```

This fails both branches. It is not an official/custodian asset receipt because
no source asset record is present. It is not a lawful-local receipt because no
lawful byte object or output manifest is present.

## 4. First Exact Obstruction

The obstruction is:

```text
SingleCompletePTUJBranchReceipt_V1.branch_purity_invariant_satisfied = false
```

The branch count remains:

```text
accepted_branch_count = 0
accepted_receipt_count = 0
```

## 5. Constructive Next Object

The next object remains exactly one complete branch:

```text
one_complete_branch_pure_PTUJ_source_packet_for_SingleCompletePTUJBranchReceipt_V1
```

## 6. Claim-Status Consistency Result

No claim status changes. Formula visibility and proof restart remain blocked.

## 7. JSON Summary

```json
{
  "artifact_id": "PTUJCrossBranchAssemblyFirewall_0103_C2_PTUJ_V1",
  "run_id": "hourly-20260626-0103",
  "cycle": 2,
  "lane": "PTUJ",
  "artifact_path": "explorations/hourly-20260626-0103-cycle2-ptuj-cross-branch-assembly-firewall.md",
  "verdict_class": "blocked_cross_branch_assembly_forbidden",
  "cycle1_consumed": true,
  "target_import_used": false,
  "claim_status_consistency_triggered": false,
  "official_branch_complete": false,
  "lawful_local_branch_complete": false,
  "mixed_packet_rejected": true,
  "cross_branch_firewall_active": true,
  "branch_purity_invariant_defined": true,
  "branch_purity_invariant_satisfied": false,
  "accepted_branch_count": 0,
  "accepted_receipt_count": 0,
  "formula_visibility_allowed": false,
  "proof_restart_allowed": false,
  "first_obstruction": "SingleCompletePTUJBranchReceipt_V1.branch_purity_invariant_satisfied_false",
  "constructive_next_object": "one_complete_branch_pure_PTUJ_source_packet_for_SingleCompletePTUJBranchReceipt_V1"
}
```
