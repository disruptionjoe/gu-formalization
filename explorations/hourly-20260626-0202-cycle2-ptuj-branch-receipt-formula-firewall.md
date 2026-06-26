---
title: "Hourly 20260626 0202 Cycle 2 PTUJ Branch Receipt Formula Firewall"
date: "2026-06-25"
run_id: "hourly-20260626-0202"
cycle: 2
lane: "PTUJ"
doc_type: "frontier_gate"
artifact_id: "PTUJBranchReceiptFormulaFirewall_0202_C2_PTUJ_V1"
verdict: "blocked_formula_visibility_firewalled_before_branch_receipt"
owned_path: "explorations/hourly-20260626-0202-cycle2-ptuj-branch-receipt-formula-firewall.md"
---

# Hourly 20260626 0202 Cycle 2 PTUJ Branch Receipt Formula Firewall

## 1. Verdict

Verdict: **blocked**.

Cycle 1 enforced the official/custodian versus lawful-local branch split and
found no complete branch. This lane tests whether formula visibility can be
evaluated from the official locator plus local schema. It cannot.

Decision state:

```text
cycle1_consumed: true
target_import_used: false
branch_bifurcation_enforced: true
accepted_branch_count: 0
accepted_receipt_count: 0
branch_purity_invariant_satisfied: false
formula_visibility_firewall_active: true
formula_visibility_allowed: false
keating_ptuj_identity_comparison_allowed: false
proof_restart_allowed: false
claim_status_consistency_triggered: false
```

## 2. Sources Read First

| source | use |
|---|---|
| `explorations/hourly-20260626-0202-cycle1-ptuj-asset-custody-bifurcation-gate.md` | Consumed incomplete branches. |
| `explorations/hourly-20260626-0103-cycle2-ptuj-cross-branch-assembly-firewall.md` | Inherited cross-branch rejection. |
| `explorations/hourly-20260625-0601-cycle2-keating-shiab-projection-formula-asset-packet-spec.md` | Checked formula asset packet requirements. |
| `sources/media-index.md` | Confirmed PTUJ locator is not source-asset custody. |

## 3. Strongest Positive Construction Attempt

The strongest allowed order is:

```text
one_complete_branch_pure_PTUJ_source_packet
  -> SingleCompletePTUJBranchReceipt_V1
  -> PTUJFormulaVisibilityAudit_V1
  -> Keating/PTUJ identity comparison
```

The route has not reached the first step. Formula visibility cannot be audited
against metadata, captions, a missing sheet, or a branch schema with no bytes.

## 4. First Exact Obstruction

The first exact obstruction is:

```text
SingleCompletePTUJBranchReceipt_V1.branch_purity_invariant_satisfied_false
```

The missing producer remains:

```text
one_complete_branch_pure_PTUJ_source_packet_for_SingleCompletePTUJBranchReceipt_V1
```

## 5. Constructive Next Object

Produce one complete branch:

```text
OfficialTzSEvmqxu48FormulaSourceAssetPacket_V1
```

or:

```text
LawfulLocalTzSEvmqxu48FrameExtractor_V1
```

but do not combine partial fields across those branches.

## 6. Claim-Status Consistency Result

No claim status changes. No formula visibility or proof restart is admitted.

## 7. JSON Summary

```json
{
  "artifact_id": "PTUJBranchReceiptFormulaFirewall_0202_C2_PTUJ_V1",
  "run_id": "hourly-20260626-0202",
  "cycle": 2,
  "lane": "PTUJ",
  "artifact_path": "explorations/hourly-20260626-0202-cycle2-ptuj-branch-receipt-formula-firewall.md",
  "verdict_class": "blocked_formula_visibility_firewalled_before_branch_receipt",
  "cycle1_consumed": true,
  "target_import_used": false,
  "claim_status_consistency_triggered": false,
  "branch_bifurcation_enforced": true,
  "accepted_branch_count": 0,
  "accepted_receipt_count": 0,
  "branch_purity_invariant_satisfied": false,
  "formula_visibility_firewall_active": true,
  "formula_visibility_allowed": false,
  "keating_ptuj_identity_comparison_allowed": false,
  "proof_restart_allowed": false,
  "first_obstruction": "SingleCompletePTUJBranchReceipt_V1.branch_purity_invariant_satisfied_false",
  "constructive_next_object": "one_complete_branch_pure_PTUJ_source_packet_for_SingleCompletePTUJBranchReceipt_V1"
}
```
