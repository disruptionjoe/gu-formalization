---
title: "Hourly 20260625 2202 Cycle 3 PTUJ Proof Restart Classifier"
date: "2026-06-25"
run_id: "hourly-20260625-2202"
cycle: 3
lane: "PTUJ"
doc_type: "closeout_gate"
artifact_id: "PTUJProofRestartClassifier_2202_C3_L3_V1"
verdict: "blocked"
owned_path: "explorations/hourly-20260625-2202-cycle3-ptuj-proof-restart-classifier.md"
---

# Hourly 20260625 2202 Cycle 3 PTUJ Proof Restart Classifier

## 1. Verdict

Verdict: **blocked**.

No PTUJ branch-local packet was admitted in cycles 1 or 2. The route is still
before formula visibility, Keating comparison, and IG selector use.

## 2. Sources Read First

| source | use |
|---|---|
| `explorations/hourly-20260625-2202-cycle1-ptuj-branch-source-byte-preflight.md` | Branch packet absence. |
| `explorations/hourly-20260625-2202-cycle2-ptuj-branch-exclusivity-gate.md` | Cross-branch assembly firewall. |
| `explorations/hourly-20260625-2104-cycle3-proof-restart-transition-matrix.md` | Predecessor transition state. |

## 3. Strongest Positive Result

The strongest positive result is the branch-exclusivity firewall: a future PTUJ
receipt must be exactly one complete branch packet. Partial official and
lawful-local rows cannot be assembled into a receipt.

## 4. First Exact Obstruction

The first missing object is:

```text
one_complete_branch_local_PTUJ_source_packet_for_SingleCompletePTUJBranchReceipt_V1
```

## 5. Constructive Next Object

Complete either the official/custodian source asset branch or the lawful-local
source-byte/toolchain/output branch. Do not run formula visibility before that.

## 6. Claim-Status Consistency

No status edit is made. PTUJ contributes no accepted receipt in this run.

## 7. Machine-Readable JSON Summary

```json
{
  "run_id": "hourly-20260625-2202",
  "cycle": 3,
  "lane": "PTUJ",
  "artifact_path": "explorations/hourly-20260625-2202-cycle3-ptuj-proof-restart-classifier.md",
  "verdict_class": "blocked",
  "target_import_used": false,
  "claim_status_consistency_triggered": false,
  "cycle1_consumed": true,
  "cycle2_consumed": true,
  "accepted_receipt_count": 0,
  "accepted_branch_count": 0,
  "cross_branch_assembly_allowed": false,
  "formula_visibility_allowed": false,
  "proof_restart_allowed": false,
  "first_missing_object": "one_complete_branch_local_PTUJ_source_packet_for_SingleCompletePTUJBranchReceipt_V1",
  "constructive_next_object": "SingleCompletePTUJBranchReceipt_V1"
}
```
