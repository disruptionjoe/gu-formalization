---
title: "Hourly 20260626 0002 Cycle 2 RS First Frame Execution Gate"
date: "2026-06-25"
run_id: "hourly-20260626-0002"
cycle: 2
lane: "RS"
doc_type: "frontier_gate"
artifact_id: "RSFirstFrameExecutionGate_0002_C2_RS_V1"
verdict: "blocked_public_route_challenge_not_target_frame"
owned_path: "explorations/hourly-20260626-0002-cycle2-rs-first-frame-execution-gate.md"
---

# Hourly 20260626 0002 Cycle 2 RS First Frame Execution Gate

## 1. Verdict

Verdict: **blocked after executable toolchain; first-frame receipt not admitted**.

Cycle 1 admitted a Chrome/Edge browser capture toolchain. This lane executed the
Chrome headless command shape against the public YouTube route for
`fBozSSLxFvI&t=1927s`. The absolute-path attempt produced a PNG, but visual
inspection shows the PNG is a Google/YouTube reCAPTCHA unusual-traffic page,
not a video frame from `[00:32:07]-[00:37:41]`.

The screenshot is therefore a rejected temp artifact, not an admitted evidence
frame. It remains under `automation/tmp/` and is not promoted into
`automation/evidence/`.

Decision state:

```text
target_import_used: false
cycle1_toolchain_consumed: true
approved_capture_toolchain_admitted: true
headless_capture_executed: true
temp_png_produced: true
temp_png_sha256_computed: true
challenge_page_captured: true
source_timestamp_verification_passed: false
first_frame_receipt_admitted: false
first_frame_persisted_as_evidence: false
typed_rs_intake_allowed: false
proof_restart_allowed: false
claim_status_consistency_triggered: false
```

## 2. Sources Read First

| source | use |
|---|---|
| `explorations/hourly-20260626-0002-cycle1-rs-approved-capture-toolchain-receipt.md` | Consumed the admitted Chrome/Edge toolchain. |
| `explorations/hourly-20260625-2302-cycle3-rs-manifest-transition-gate.md` | Inherited the required first-frame and manifest order. |
| `automation/evidence/hourly-20260625-2202-rs-fbozsslxfvi/README.md` | Preserved the existing directory/policy row. |
| `RESEARCH-POSTURE.md` | Prevented the temp challenge page from becoming target evidence. |
| `process/runbooks/five-lane-frontier-run.md` | Applied exact-obstruction and no-overclaim discipline. |

## 3. Strongest Positive Construction Attempt

The successful part of the execution:

| field | result |
|---|---|
| `capture_tool_identity` | Chrome `C:\Program Files\Google\Chrome\Application\chrome.exe`, version `149.0.7827.156` |
| `target_url` | `https://www.youtube.com/watch?v=fBozSSLxFvI&t=1927s` |
| `temp_output_path` | `automation/tmp/hourly-20260626-0002-rs-first-frame-attempt/fbozsslxfvi-003207-chrome-abs.png` |
| `temp_output_length` | `18665` bytes |
| `temp_output_sha256` | `CBF88D773CF9A4DBF4BA6D0DFA167C1C59AC4CE0E491256B3B6CDA4F1C21702A` |
| `visual_classification` | reCAPTCHA/unusual-traffic page, not target-window video frame |

This closes an execution unknown: the headless browser can write PNG bytes, and
the repo can hash them. It does not close the evidence problem because the bytes
are not the requested source-window frame.

## 4. First Exact Obstruction

The first missing evidence field is:

```text
RSBrowserCaptureToolchainAndFirstFrameReceipt_V1.source_timestamp_verification_result
```

The temp PNG fails that field because it does not show the target video frame or
player timestamp. Consequently the coupled fields remain unadmitted:

```text
first_frame_output_path
first_frame_sha256
immutability_after_hash
```

## 5. Constructive Next Object

The next object remains:

```text
RSBrowserCaptureToolchainAndFirstFrameReceipt_V1
```

but a future attempt must use an approved public route that avoids the
challenge page or supplies a lawful external immutable frame package with
provenance. The next positive receipt must persist a target-window frame under
`automation/evidence/`, not a temp challenge screenshot.

## 6. Claim-Status Consistency Result

No claim status changes. This lane admits no frame evidence, no crop/OCR row,
no typed RS intake, and no proof restart.

## 7. JSON Summary

```json
{
  "artifact_id": "RSFirstFrameExecutionGate_0002_C2_RS_V1",
  "run_id": "hourly-20260626-0002",
  "cycle": 2,
  "lane": "RS",
  "artifact_path": "explorations/hourly-20260626-0002-cycle2-rs-first-frame-execution-gate.md",
  "verdict_class": "blocked_public_route_challenge_not_target_frame",
  "target_import_used": false,
  "claim_status_consistency_triggered": false,
  "cycle1_consumed": true,
  "cycle1_toolchain_consumed": true,
  "approved_capture_toolchain_admitted": true,
  "capture_tool_identity_admitted": true,
  "headless_capture_executed": true,
  "temp_png_produced": true,
  "temp_png_sha256_computed": true,
  "challenge_page_captured": true,
  "source_timestamp_verification_passed": false,
  "first_frame_receipt_admitted": false,
  "first_frame_persisted_as_evidence": false,
  "persisted_frame_count": 0,
  "crop_or_ocr_allowed": false,
  "typed_rs_intake_allowed": false,
  "generation_restart_allowed": false,
  "proof_restart_allowed": false,
  "temp_output_path": "automation/tmp/hourly-20260626-0002-rs-first-frame-attempt/fbozsslxfvi-003207-chrome-abs.png",
  "temp_output_sha256": "CBF88D773CF9A4DBF4BA6D0DFA167C1C59AC4CE0E491256B3B6CDA4F1C21702A",
  "first_missing_field": "RSBrowserCaptureToolchainAndFirstFrameReceipt_V1.source_timestamp_verification_result",
  "constructive_next_object": "RSBrowserCaptureToolchainAndFirstFrameReceipt_V1"
}
```
