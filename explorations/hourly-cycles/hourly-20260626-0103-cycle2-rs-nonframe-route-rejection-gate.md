---
title: "Hourly 20260626 0103 Cycle 2 RS Nonframe Route Rejection Gate"
date: "2026-06-25"
run_id: "hourly-20260626-0103"
cycle: 2
lane: "RS"
doc_type: "frontier_gate"
artifact_id: "RSNonframeRouteRejectionGate_0103_C2_RS_V1"
verdict: "blocked_nonframe_routes_rejected"
owned_path: "explorations/hourly-20260626-0103-cycle2-rs-nonframe-route-rejection-gate.md"
---

# Hourly 20260626 0103 Cycle 2 RS Nonframe Route Rejection Gate

## 1. Verdict

Verdict: **blocked**.

Cycle 1 classified the remaining RS evidence branches. This lane consumes that
classifier and records the downstream rejection rule: no non-frame route can
stand in for `RSBrowserCaptureToolchainAndFirstFrameReceipt_V1`.

Decision state:

```text
cycle1_consumed: true
target_import_used: false
approved_capture_toolchain_admitted: true
nonframe_route_firewall_active: true
challenge_page_rejected_as_evidence: true
metadata_route_rejected: true
thumbnail_route_rejected: true
transcript_route_rejected: true
unchecksummed_screenshot_rejected: true
external_immutable_frame_package_found: false
accepted_evidence_branch_count: 0
first_frame_receipt_admitted: false
frame_manifest_allowed: false
typed_rs_intake_allowed: false
proof_restart_allowed: false
claim_status_consistency_triggered: false
```

## 2. Sources Read First

| source | use |
|---|---|
| `explorations/hourly-20260626-0103-cycle1-rs-evidence-route-classifier.md` | Consumed the branch classifier. |
| `explorations/hourly-20260626-0002-cycle2-rs-first-frame-execution-gate.md` | Inherited the challenge-page rejection. |
| `automation/evidence/hourly-20260625-2202-rs-fbozsslxfvi/README.md` | Preserved the evidence directory policy. |

## 3. Strongest Positive Construction Attempt

The rule that survives cycle 2 is:

```text
acceptable RS visual evidence =
  timestamp-verified target-window frame
  OR lawful immutable external frame package
```

Everything else is a locator, aid, or rejected temporary artifact:

```text
challenge page
title/oEmbed metadata
thumbnail
transcript/caption
unchecksummed screenshot
```

Those objects can help find source material, but they cannot enter the typed RS
operator/generation/index lane.

## 4. First Exact Obstruction

The first exact missing field remains:

```text
RSBrowserCaptureToolchainAndFirstFrameReceipt_V1.source_timestamp_verification_result
```

No non-frame route can fill that field.

## 5. Constructive Next Object

The next object remains:

```text
RSBrowserCaptureToolchainAndFirstFrameReceipt_V1
```

It should be attempted only through a target-frame branch or immutable external
frame package branch.

## 6. Claim-Status Consistency Result

No claim status changes. No frame evidence, manifest, typed intake, or proof
restart is admitted.

## 7. JSON Summary

```json
{
  "artifact_id": "RSNonframeRouteRejectionGate_0103_C2_RS_V1",
  "run_id": "hourly-20260626-0103",
  "cycle": 2,
  "lane": "RS",
  "artifact_path": "explorations/hourly-20260626-0103-cycle2-rs-nonframe-route-rejection-gate.md",
  "verdict_class": "blocked_nonframe_routes_rejected",
  "cycle1_consumed": true,
  "target_import_used": false,
  "claim_status_consistency_triggered": false,
  "approved_capture_toolchain_admitted": true,
  "nonframe_route_firewall_active": true,
  "challenge_page_rejected_as_evidence": true,
  "metadata_route_rejected": true,
  "thumbnail_route_rejected": true,
  "transcript_route_rejected": true,
  "unchecksummed_screenshot_rejected": true,
  "external_immutable_frame_package_found": false,
  "accepted_evidence_branch_count": 0,
  "first_frame_receipt_admitted": false,
  "frame_manifest_allowed": false,
  "typed_rs_intake_allowed": false,
  "proof_restart_allowed": false,
  "first_missing_field": "RSBrowserCaptureToolchainAndFirstFrameReceipt_V1.source_timestamp_verification_result",
  "constructive_next_object": "RSBrowserCaptureToolchainAndFirstFrameReceipt_V1"
}
```
