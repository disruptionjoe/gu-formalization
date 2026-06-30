---
title: "Hourly 20260625 2202 Cycle 1 PTUJ Branch Source Byte Preflight"
date: "2026-06-25"
run_id: "hourly-20260625-2202"
cycle: 1
lane: "PTUJ"
doc_type: "frontier_gate"
artifact_id: "PTUJBranchSourceBytePreflight_2202_C1_L3_V1"
verdict: "blocked"
owned_path: "explorations/hourly-20260625-2202-cycle1-ptuj-branch-source-byte-preflight.md"
---

# Hourly 20260625 2202 Cycle 1 PTUJ Branch Source Byte Preflight

## 1. Verdict

Verdict: **blocked**.

The lane retests the first PTUJ producer object:

```text
SingleCompletePTUJBranchReceipt_V1
```

The repo still has zero complete branch-local PTUJ receipts. The strongest
current PTUJ state is a schema with two allowed branches, not a source packet.

## 2. Sources Read First

| source | use |
|---|---|
| `explorations/hourly-20260625-2104-cycle1-ptuj-single-complete-branch-receipt-attempt.md` | Branch schema and predecessor search. |
| `explorations/hourly-20260625-2104-cycle2-ptuj-branch-local-source-packet-gate.md` | Exact missing fields for official and lawful-local branches. |
| `explorations/hourly-20260625-2104-cycle3-proof-restart-transition-matrix.md` | Confirms PTUJ remains before formula visibility. |
| `RESEARCH-POSTURE.md` | Blocks cross-branch assembly and target import. |

## 3. Strongest Positive Construction Attempt

The positive structure is a two-branch intake schema:

| branch | required object | current status |
|---|---|---|
| official/custodian | `OfficialTzSEvmqxu48FormulaSourceAssetPacket_V1.source_asset_object_manifest` | locator context only |
| lawful local | `LawfulLocalTzSEvmqxu48FrameExtractor_V1.toolchain_identity_and_output_manifest` | schema only |

Either branch could close `SingleCompletePTUJBranchReceipt_V1` if it supplied
all required fields in one branch-local packet. Cross-branch assembly remains
forbidden.

## 4. First Exact Obstruction

The first missing field is:

```text
lawful_basis_for_a_concrete_source_byte_object
```

There is no concrete source-byte object tied to `TzSEvmqxu48`, no decoding or
frame extraction output manifest, and no checksum row. The official branch also
lacks a custodian source asset object manifest.

## 5. Constructive Next Object

Produce exactly one complete branch-local packet:

```text
OfficialTzSEvmqxu48FormulaSourceAssetPacket_V1.source_asset_object_manifest
```

or:

```text
LawfulLocalTzSEvmqxu48FrameExtractor_V1.toolchain_identity_and_output_manifest
```

Only after one branch closes may a future lane run PTUJ formula visibility or
Keating/Shiab identity comparison.

## 6. Claim-Status Consistency

No claim status changes. PTUJ formula visibility and IG selector use remain
blocked.

## 7. Machine-Readable JSON Summary

```json
{
  "run_id": "hourly-20260625-2202",
  "cycle": 1,
  "lane": "PTUJ",
  "artifact_path": "explorations/hourly-20260625-2202-cycle1-ptuj-branch-source-byte-preflight.md",
  "verdict_class": "blocked",
  "target_import_used": false,
  "claim_status_consistency_triggered": false,
  "decision_target": "SingleCompletePTUJBranchReceipt_V1",
  "accepted_receipt_count": 0,
  "accepted_branch_count": 0,
  "official_branch_accepted": false,
  "lawful_local_branch_accepted": false,
  "cross_branch_assembly_allowed": false,
  "formula_visibility_allowed": false,
  "proof_restart_allowed": false,
  "first_obstruction": "lawful_basis_for_a_concrete_source_byte_object",
  "constructive_next_object": "one_complete_branch_local_PTUJ_source_packet_for_SingleCompletePTUJBranchReceipt_V1"
}
```
