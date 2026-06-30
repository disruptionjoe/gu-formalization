---
title: "Hourly 20260626 0202 Cycle 1 PTUJ Asset Custody Bifurcation Gate"
date: "2026-06-25"
run_id: "hourly-20260626-0202"
cycle: 1
lane: "PTUJ"
doc_type: "frontier_gate"
artifact_id: "PTUJAssetCustodyBifurcationGate_0202_C1_PTUJ_V1"
verdict: "blocked_no_branch_complete_asset_custody"
owned_path: "explorations/hourly-20260626-0202-cycle1-ptuj-asset-custody-bifurcation-gate.md"
---

# Hourly 20260626 0202 Cycle 1 PTUJ Asset Custody Bifurcation Gate

## 1. Verdict

Verdict: **blocked**.

The PTUJ route has two admissible producer branches: official/custodian source
asset or lawful-local byte/toolchain/output manifest. This lane tests whether
the official Pull That Up Jamie locator and the local branch schema can be
merged into a complete receipt. They cannot.

Decision state:

```text
target_import_used: false
official_locator_present: true
official_custodian_asset_manifest_found: false
official_formula_visibility_scope_found: false
lawful_local_source_byte_object_found: false
lawful_local_toolchain_identity_found: false
lawful_local_output_manifest_found: false
branch_bifurcation_enforced: true
accepted_branch_count: 0
accepted_receipt_count: 0
cross_branch_assembly_allowed: false
formula_visibility_allowed: false
proof_restart_allowed: false
claim_status_consistency_triggered: false
```

## 2. Sources Read First

| source | use |
|---|---|
| `sources/media-index.md` | Confirmed `GU-MEDIA-2021-PULL-THAT-UP-JAMIE` is metadata-checked only. |
| `explorations/hourly-20260625-0601-cycle2-keating-shiab-projection-formula-asset-packet-spec.md` | Inherited the formula asset packet specification. |
| `explorations/hourly-20260626-0002-cycle1-ptuj-branch-source-packet-mining.md` | Inherited zero accepted PTUJ branches. |
| `explorations/hourly-20260626-0103-cycle1-ptuj-branch-packet-field-ledger.md` | Inherited the branch field ledger. |
| `process/runbooks/five-lane-frontier-run.md` | Applied exact obstruction and no-padding discipline. |

## 3. Strongest Positive Construction Attempt

The official/custodian branch has a real locator:

```text
source_id: GU-MEDIA-2021-PULL-THAT-UP-JAMIE
candidate asset: PullThatUpJamie_GUForGRGaugeTheory_TzSEvmqxu48
claimed role: visual aid for GR/gauge-theory compatibility and Shiab projection motifs
```

The lawful-local branch has a real schema:

```text
source bytes -> checksum -> toolchain identity -> decode command
  -> output manifest -> output checksums -> formula visibility scope
```

Neither branch is complete. The official locator is not a byte manifest, and
the local schema is not a lawful byte object. Combining them would hide the
first missing field in each branch.

## 4. First Exact Obstruction

The official/custodian branch blocks at:

```text
OfficialTzSEvmqxu48FormulaSourceAssetPacket_V1.source_asset_object_manifest
```

The lawful-local branch blocks at:

```text
LawfulLocalTzSEvmqxu48FrameExtractor_V1.source_byte_object
```

## 5. Constructive Next Object

The next object remains:

```text
one_complete_branch_pure_PTUJ_source_packet_for_SingleCompletePTUJBranchReceipt_V1
```

It must be one of:

```text
official/custodian: source asset object manifest + custody + formula visibility scope
lawful-local: byte object + checksum + toolchain + output manifest + formula visibility scope
```

## 6. What This Means For The GU Claim

PTUJ cannot reach formula visibility. The route is not falsified globally; it
is blocked at source custody. A future packet would materially change the route
because it would permit a real formula visibility audit.

## 7. Claim-Status Consistency Result

No claim status changes. No branch receipt or formula visibility claim is
admitted, so the claim-status consistency workflow is not triggered.

## 8. JSON Summary

```json
{
  "artifact_id": "PTUJAssetCustodyBifurcationGate_0202_C1_PTUJ_V1",
  "run_id": "hourly-20260626-0202",
  "cycle": 1,
  "lane": "PTUJ",
  "artifact_path": "explorations/hourly-20260626-0202-cycle1-ptuj-asset-custody-bifurcation-gate.md",
  "verdict_class": "blocked_no_branch_complete_asset_custody",
  "target_import_used": false,
  "claim_status_consistency_triggered": false,
  "official_locator_present": true,
  "official_custodian_asset_manifest_found": false,
  "official_formula_visibility_scope_found": false,
  "lawful_local_source_byte_object_found": false,
  "lawful_local_toolchain_identity_found": false,
  "lawful_local_output_manifest_found": false,
  "branch_bifurcation_enforced": true,
  "accepted_branch_count": 0,
  "accepted_receipt_count": 0,
  "cross_branch_assembly_allowed": false,
  "formula_visibility_allowed": false,
  "proof_restart_allowed": false,
  "first_missing_fields": [
    "OfficialTzSEvmqxu48FormulaSourceAssetPacket_V1.source_asset_object_manifest",
    "LawfulLocalTzSEvmqxu48FrameExtractor_V1.source_byte_object"
  ],
  "constructive_next_object": "one_complete_branch_pure_PTUJ_source_packet_for_SingleCompletePTUJBranchReceipt_V1"
}
```
