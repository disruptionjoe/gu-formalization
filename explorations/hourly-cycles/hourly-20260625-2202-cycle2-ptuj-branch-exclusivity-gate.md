---
title: "Hourly 20260625 2202 Cycle 2 PTUJ Branch Exclusivity Gate"
date: "2026-06-25"
run_id: "hourly-20260625-2202"
cycle: 2
lane: "PTUJ"
doc_type: "frontier_gate"
artifact_id: "PTUJBranchExclusivityGate_2202_C2_L3_V1"
verdict: "blocked"
owned_path: "explorations/hourly-20260625-2202-cycle2-ptuj-branch-exclusivity-gate.md"
---

# Hourly 20260625 2202 Cycle 2 PTUJ Branch Exclusivity Gate

## 1. Verdict

Verdict: **blocked**.

Cycle 1 confirmed that `SingleCompletePTUJBranchReceipt_V1` is absent. Cycle 2
tests whether the two PTUJ branches can be legally assembled together. They
cannot. The official/custodian branch and lawful-local byte/toolchain branch
are alternatives; mixing locator fields from one with missing source bytes from
the other would create an import.

## 2. Sources Read First

| source | use |
|---|---|
| `explorations/hourly-20260625-2202-cycle1-ptuj-branch-source-byte-preflight.md` | Cycle 1 blocker. |
| `explorations/hourly-20260625-2104-cycle2-ptuj-branch-local-source-packet-gate.md` | Branch field matrix. |
| `explorations/hourly-20260625-0703-cycle3-claim-promotion-firewall.md` | Keating/PTUJ visual capture firewall. |
| `RESEARCH-POSTURE.md` | No cross-branch rescue or target import. |

## 3. Strongest Positive Construction Attempt

The branch exclusivity rule is now explicit:

```text
accepted PTUJ receipt = exactly one complete branch-local packet
forbidden PTUJ receipt = official locator fields + lawful-local missing byte placeholders
```

This is useful because it prevents a later worker from combining partial
locators, captions, storyboard negatives, and local toolchain schemas into a
false branch receipt.

## 4. First Exact Obstruction

The first exact obstruction remains:

```text
SingleCompletePTUJBranchReceipt_V1.complete_single_branch_manifest
```

The official branch lacks a custodian source asset object manifest. The lawful
local branch lacks a concrete source byte object, decode scope, outputs, and
checksums.

## 5. Constructive Next Object

The next lane should produce one branch packet only:

```text
OfficialTzSEvmqxu48FormulaSourceAssetPacket_V1
```

or:

```text
LawfulLocalTzSEvmqxu48FrameExtractor_V1
```

If neither branch can be completed, PTUJ remains blocked before formula
visibility.

## 6. Claim-Status Consistency

No status edit is made. This is a firewall over evidence assembly, not a claim
promotion or demotion.

## 7. Machine-Readable JSON Summary

```json
{
  "run_id": "hourly-20260625-2202",
  "cycle": 2,
  "lane": "PTUJ",
  "artifact_path": "explorations/hourly-20260625-2202-cycle2-ptuj-branch-exclusivity-gate.md",
  "verdict_class": "blocked_branch_exclusivity",
  "target_import_used": false,
  "claim_status_consistency_triggered": false,
  "cycle1_branch_preflight_consumed": true,
  "decision_target": "SingleCompletePTUJBranchReceipt_V1",
  "accepted_receipt_count": 0,
  "accepted_branch_count": 0,
  "official_branch_accepted": false,
  "lawful_local_branch_accepted": false,
  "cross_branch_assembly_allowed": false,
  "mixed_branch_packet_rejected": true,
  "formula_visibility_allowed": false,
  "proof_restart_allowed": false,
  "first_obstruction": "SingleCompletePTUJBranchReceipt_V1.complete_single_branch_manifest",
  "constructive_next_object": "one_complete_branch_local_PTUJ_source_packet_for_SingleCompletePTUJBranchReceipt_V1"
}
```
