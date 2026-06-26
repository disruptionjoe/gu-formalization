---
title: "Hourly 20260626 0002 Cycle 1 RS Approved Capture Toolchain Receipt"
date: "2026-06-25"
run_id: "hourly-20260626-0002"
cycle: 1
lane: "RS"
doc_type: "frontier_gate"
artifact_id: "ApprovedBrowserCaptureToolchainForFBozSSLxFvIWindow_0002_C1_RS_V1"
verdict: "conditional_toolchain_admitted_no_frame"
owned_path: "explorations/hourly-20260626-0002-cycle1-rs-approved-capture-toolchain-receipt.md"
---

# Hourly 20260626 0002 Cycle 1 RS Approved Capture Toolchain Receipt

## 1. Verdict

Verdict: **conditional / toolchain admitted, no frame admitted**.

This lane closes the exact field that blocked the 2302 RS route:

```text
ApprovedBrowserCaptureToolchainForFBozSSLxFvIWindow_V1.capture_tool_identity
```

The current Windows environment contains two browser executables outside PATH.
This artifact admits Chrome as the preferred capture producer and Edge as a
fallback producer for future public viewport capture attempts:

```text
Chrome: C:\Program Files\Google\Chrome\Application\chrome.exe
Chrome version: 149.0.7827.156
Edge: C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe
Edge version: 149.0.4022.80
```

The object admitted here is only the toolchain and policy row. It does not
persist a frame, does not compute a frame digest, does not run crop/OCR, and
does not admit typed RS intake.

Decision state:

```text
target_import_used: false
directory_policy_row_consumed: true
capture_tool_identity_admitted: true
approved_capture_toolchain_admitted: true
capture_operation_rule_defined: true
source_timestamp_verification_rule_defined: true
output_root_binding_defined: true
hash_rule_defined: true
first_frame_persisted: false
persisted_frame_count: 0
typed_rs_intake_allowed: false
proof_restart_allowed: false
claim_status_consistency_triggered: false
```

## 2. Sources Read First

| source | use |
|---|---|
| `RESEARCH-POSTURE.md` | Prevented transcript/title/locator metadata from becoming typed evidence. |
| `process/runbooks/five-lane-frontier-run.md` | Required the lane to distinguish an admitted producer from downstream frame evidence. |
| `explorations/hourly-20260625-2302-cycle3-rs-manifest-transition-gate.md` | Inherited the exact first missing object and field. |
| `explorations/hourly-20260625-2302-cycle2-rs-first-frame-receipt-gate.md` | Inherited the first-frame dependency on an approved toolchain. |
| `explorations/hourly-20260625-2302-cycle1-rs-capture-toolchain-producer-contract.md` | Inherited the minimum fields for `ApprovedBrowserCaptureToolchainForFBozSSLxFvIWindow_V1`. |
| `automation/evidence/hourly-20260625-2202-rs-fbozsslxfvi/README.md` | Consumed the admitted directory/policy row and target window. |

Environment checks found Chrome and Edge at stable local executable paths, with
version strings from the executable metadata. The existing evidence directory
still contains only `README.md`; no previous frame, crop, OCR, checksum, or
manifest is being promoted by this artifact.

## 3. Strongest Positive Construction Attempt

The admitted toolchain receipt is:

| field | value |
|---|---|
| `object_id` | `ApprovedBrowserCaptureToolchainForFBozSSLxFvIWindow_V1` |
| `preferred_capture_tool_identity` | `C:\Program Files\Google\Chrome\Application\chrome.exe`, version `149.0.7827.156` |
| `fallback_capture_tool_identity` | `C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe`, version `149.0.4022.80` |
| `source_video_id` | `fBozSSLxFvI` |
| `source_window` | `[00:32:07]-[00:37:41]` |
| `capture_route` | public browser viewport route |
| `target_url_rule` | `https://www.youtube.com/watch?v=fBozSSLxFvI&t=1927s` for the first-frame attempt |
| `output_root_binding` | `automation/evidence/hourly-20260625-2202-rs-fbozsslxfvi` |
| `first_frame_output_path_rule` | future receipt must persist one full-frame PNG under the bound output root |
| `hash_rule` | compute SHA-256 over persisted bytes with `Get-FileHash -Algorithm SHA256` |
| `immutability_rule` | any byte change requires a new artifact id and digest |
| `target_import_firewall` | title, transcript, locator metadata, and unchecksummed screenshots cannot become typed RS evidence |

The future capture command shape is:

```text
"C:\Program Files\Google\Chrome\Application\chrome.exe"
  --headless=new
  --disable-gpu
  --no-first-run
  --user-data-dir=<owned temporary profile>
  --window-size=1280,720
  --screenshot=<owned first-frame output path>
  "https://www.youtube.com/watch?v=fBozSSLxFvI&t=1927s"
```

This is enough to admit the producer identity and output/hash rules. It is not
enough to admit a first frame because no screenshot has been produced or
independently verified in this lane.

## 4. First Exact Obstruction

The previous obstruction:

```text
ApprovedBrowserCaptureToolchainForFBozSSLxFvIWindow_V1.capture_tool_identity
```

is now closed for the local Chrome/Edge producer identities.

The new first downstream missing field is:

```text
RSBrowserCaptureToolchainAndFirstFrameReceipt_V1.first_frame_output_path
```

with its coupled verification fields:

```text
capture_operation_instance
source_timestamp_verification_result
first_frame_sha256
immutability_after_hash
```

## 5. Constructive Next Object

The next object is:

```text
RSBrowserCaptureToolchainAndFirstFrameReceipt_V1
```

It must use the approved Chrome or Edge toolchain to persist exactly one
full-frame artifact, verify that the capture belongs to the requested video
window, compute SHA-256, and record immutability. No crop/OCR/typed RS intake is
allowed before that object is admitted.

## 6. Claim-Status Consistency Result

No mathematical claim status changes. This artifact admits only a local
producer/toolchain receipt for future evidence capture. It does not admit media
content, typed RS data, generation/index data, or proof restart, so the
claim-status consistency workflow is not triggered.

## 7. JSON Summary

```json
{
  "artifact_id": "ApprovedBrowserCaptureToolchainForFBozSSLxFvIWindow_0002_C1_RS_V1",
  "run_id": "hourly-20260626-0002",
  "cycle": 1,
  "lane": "RS",
  "artifact_path": "explorations/hourly-20260626-0002-cycle1-rs-approved-capture-toolchain-receipt.md",
  "verdict_class": "conditional_toolchain_admitted_no_frame",
  "target_import_used": false,
  "claim_status_consistency_triggered": false,
  "directory_policy_row_consumed": true,
  "directory_policy_row_admitted": true,
  "chrome_capture_tool_found": true,
  "edge_capture_tool_found": true,
  "capture_tool_identity_admitted": true,
  "approved_capture_toolchain_admitted": true,
  "capture_operation_rule_defined": true,
  "source_timestamp_verification_rule_defined": true,
  "output_root_binding_defined": true,
  "hash_rule_defined": true,
  "immutability_rule_defined": true,
  "first_frame_persisted": false,
  "persisted_frame_count": 0,
  "first_frame_sha256_admitted": false,
  "crop_or_ocr_allowed": false,
  "typed_rs_intake_allowed": false,
  "generation_restart_allowed": false,
  "proof_restart_allowed": false,
  "closed_field": "ApprovedBrowserCaptureToolchainForFBozSSLxFvIWindow_V1.capture_tool_identity",
  "first_missing_field": "RSBrowserCaptureToolchainAndFirstFrameReceipt_V1.first_frame_output_path",
  "constructive_next_object": "RSBrowserCaptureToolchainAndFirstFrameReceipt_V1",
  "preferred_capture_tool": {
    "name": "Chrome",
    "path": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
    "version": "149.0.7827.156"
  },
  "fallback_capture_tool": {
    "name": "Edge",
    "path": "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe",
    "version": "149.0.4022.80"
  }
}
```
