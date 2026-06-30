---
title: "Hourly 20260626 1302 Cycle 3 QFT Source Anchor Triad Receipt Spec"
date: "2026-06-26"
run_id: "hourly-20260626-1302"
cycle: 3
lane: 5
doc_type: "frontier_run_lane_artifact"
artifact_id: "QFTSameContextSourceAnchorTriadReceipt_1302_C3_L5_V1"
verdict: "receipt_spec_defined_uninhabited"
owned_path: "explorations/hourly-20260626-1302-cycle3-qft-source-anchor-triad-receipt-spec.md"
claim_status_change: false
---

# Hourly 20260626 1302 Cycle 3 QFT Source Anchor Triad Receipt Spec

## 1. Verdict

Verdict: **closed spec / receipt uninhabited**.

This lane defines the lower object demanded by the QFT candidate verifier:

```text
QFTSameContextSourceAnchorTriadReceipt_V1
```

No receipt is present. Cover declarations, local records, `BrSch`, and carrier
work remain locked.

Decision flags:

```text
source_anchor_triad_receipt_spec_defined: true
source_anchor_triad_receipt_present: false
source_context_anchor_present: false
same_context_source_locator_present: false
cover_vocabulary_authority_present: false
admissibility_authority_present: false
roles_type_over_same_context: false
dependency_DAG_allowed: false
same_context_candidate_allowed: false
qft_cover_declaration_retry_allowed: false
carrier_work_allowed: false
target_import_used: false
claim_status_change: false
```

## 2. Required Receipt Fields

```text
receipt_id:
  QFTSameContextSourceAnchorTriadReceipt_V1

source_context_anchor:
  source id, locator, context type, and source-side relation to the intended
  QFT branch.

same_context_source_locator:
  located source row over the anchor.

cover_vocabulary_authority:
  authority row licensing domains, index set, overlaps, and restriction maps
  over the same anchor.

admissibility_authority:
  source-side cover formation predicate over the same anchor.

dependency_DAG:
  allowed source-side edges and explicit absence of downstream edges from local
  records, BrSch, carrier viability, anomaly, SM, Bell, EFT, or target QFT.
```

## 3. First Exact Obstruction

First exact obstruction:

```text
QFTSameContextSourceAnchorTriadReceipt_V1.absent
```

This precedes the same-context candidate packet and the edge verifier.

## 4. Terrain and Guard

Terrain classification:

```text
descent-quotient; provenance-verifier; dependency-DAG packet
```

Forbidden shortcut:

```text
Do not choose the anchor from carrier viability, local record success, anomaly
success, or target QFT behavior.
```

Kill condition:

```text
If locator, cover vocabulary authority, and admissibility authority cannot be
typed over one source anchor, the same-context edge remains absent.
```

## 5. Impact and Next Step

Impact if closed: it would allow a QFT same-context candidate packet to be
submitted without downstream provenance smuggling.

Next meaningful proof/computation step:

```text
Instantiate QFTSameContextSourceAnchorTriadReceipt_V1, then populate
QFTSameContextLocatorAuthorityCandidatePacket_V1 and rerun the edge verifier.
```

Claim-status consistency result: no status changed.

## 6. JSON Summary

```json
{
  "artifact_id": "QFTSameContextSourceAnchorTriadReceipt_1302_C3_L5_V1",
  "run_id": "hourly-20260626-1302",
  "cycle": 3,
  "lane": 5,
  "artifact_path": "explorations/hourly-20260626-1302-cycle3-qft-source-anchor-triad-receipt-spec.md",
  "verdict_class": "receipt_spec_defined_uninhabited",
  "source_anchor_triad_receipt_spec_defined": true,
  "source_anchor_triad_receipt_present": false,
  "source_context_anchor_present": false,
  "same_context_source_locator_present": false,
  "cover_vocabulary_authority_present": false,
  "admissibility_authority_present": false,
  "roles_type_over_same_context": false,
  "dependency_DAG_allowed": false,
  "same_context_candidate_allowed": false,
  "qft_cover_declaration_retry_allowed": false,
  "carrier_work_allowed": false,
  "target_import_used": false,
  "claim_status_change": false,
  "first_exact_obstruction": "QFTSameContextSourceAnchorTriadReceipt_V1.absent",
  "constructive_next_object": "QFTSameContextSourceAnchorTriadReceipt_V1",
  "unlocks_if_inhabited": "QFTSameContextLocatorAuthorityCandidatePacket_V1",
  "terrain": [
    "descent-quotient",
    "provenance-verifier",
    "dependency-DAG-packet"
  ],
  "forbidden_shortcut": "carrier_local_record_anomaly_or_target_QFT_success_as_source_anchor",
  "kill_condition": "roles_not_typed_over_one_source_anchor_keep_same_context_edge_absent"
}
```

