---
title: "Hourly 20260625 2028 Cycle 3 Receipt Transition Matrix"
date: "2026-06-25"
run_id: "hourly-20260625-2028"
cycle: 3
lane: 2
doc_type: receipt_transition_matrix
artifact_id: "ReceiptTransitionMatrixAfter2028_C3_L2_V1"
verdict: "zero_accepted_transitions"
owned_path: "explorations/hourly-20260625-2028-cycle3-receipt-transition-matrix.md"
---

# Hourly 20260625 2028 Cycle 3 Receipt Transition Matrix

## 1. Verdict

Verdict: **zero accepted transitions**.

No route moved from candidate producer object to accepted receipt, accepted for
routing, proof-ready route, or downstream replay.

## 2. Matrix

| route | candidate object | accepted receipt? | transition fired? | missing transition witness |
|---|---|---:|---:|---|
| PTUJ | `PTUJ_SINGLE_COMPLETE_BRANCH_RECEIPT` | false | false | `SingleCompletePTUJBranchReceipt_V1` |
| IG | `IG_PRODUCT_B_FULL_D7_SUMMAND_MULTIPLICITY_DIMENSION_RECEIPT` | false | false | `ProductBFullD7SummandMultiplicityDimensionTableReceipt_V1` |
| DGU | `DGU_SOURCE_EMITTED_SECTOR_RULE_AND_SAME_OPERATOR_RECEIPT` | false | false | `SourceEmittedDGU01SectorRuleAndSameOperatorReceipt_V1` |
| RS | `RS_LAWFUL_SOURCE_ACQUISITION_ROUTE_OR_BROWSER_CAPTURE_ROUTE` | false | false | `RSLawfulSourceAcquisitionRouteOrBrowserCaptureRouteForFBozSSLxFvIWindow_V1` |
| QFT | `QFT_SOURCE_DEFINED_IOTA_B_AND_TYPED_R_RAW_B_O_RECEIPT` | false | false | `QFTSourceDefinedIotaBAndTypedRRawBOReceipt_V1` |

## 3. Exact Decision

All transitions remain pre-acceptance. The firewalls added in cycle 2 make the
missing witness order explicit; they do not create accepted evidence.

## 4. Machine-readable JSON summary

```json
{
  "artifact_id": "ReceiptTransitionMatrixAfter2028_C3_L2_V1",
  "run_id": "hourly-20260625-2028",
  "cycle": 3,
  "lane": 2,
  "artifact_path": "explorations/hourly-20260625-2028-cycle3-receipt-transition-matrix.md",
  "owned_path": "explorations/hourly-20260625-2028-cycle3-receipt-transition-matrix.md",
  "verdict_class": "zero_accepted_transitions",
  "accepted_receipt_count": 0,
  "accepted_transition_count": 0,
  "accepted_for_routing_count": 0,
  "proof_ready_count": 0,
  "proof_restart_allowed": false,
  "claim_promotion_allowed": false,
  "target_import_used": false,
  "route_rows": [
    {"route": "PTUJ", "accepted_transition": false, "missing_transition_witness": "SingleCompletePTUJBranchReceipt_V1"},
    {"route": "IG", "accepted_transition": false, "missing_transition_witness": "ProductBFullD7SummandMultiplicityDimensionTableReceipt_V1"},
    {"route": "DGU", "accepted_transition": false, "missing_transition_witness": "SourceEmittedDGU01SectorRuleAndSameOperatorReceipt_V1"},
    {"route": "RS", "accepted_transition": false, "missing_transition_witness": "RSLawfulSourceAcquisitionRouteOrBrowserCaptureRouteForFBozSSLxFvIWindow_V1"},
    {"route": "QFT", "accepted_transition": false, "missing_transition_witness": "QFTSourceDefinedIotaBAndTypedRRawBOReceipt_V1"}
  ],
  "claim_status_consistency_triggered": false
}
```
