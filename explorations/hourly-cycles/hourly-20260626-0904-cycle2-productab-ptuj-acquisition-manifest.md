---
title: "Hourly 20260626 0904 Cycle 2 ProductAB PTUJ Acquisition Manifest"
date: "2026-06-26"
run_id: "hourly-20260626-0904"
cycle: 2
lane: 4
doc_type: "frontier_run_lane_artifact"
artifact_id: "PTUJBranchPureSourceAssetAcquisitionManifest_0904_C2_L4_V1"
verdict: "negative_no_branch_pure_acquisition_manifest"
owned_path: "explorations/hourly-20260626-0904-cycle2-productab-ptuj-acquisition-manifest.md"
claim_status_change: false
---

# Hourly 20260626 0904 Cycle 2 ProductAB PTUJ Acquisition Manifest

## 1. Verdict

Verdict: **scoped negative; no branch-pure acquisition manifest exists**.

Cycle 1 narrowed the ProductAB/PTUJ blocker to:

```text
PTUJBranchPureSourceAssetAcquisitionManifest_V1
```

This cycle found no manifest for any branch. Existing rows identify the PTUJ
video, the official page, oEmbed metadata, and the Keating missing-sheet
locator. They do not preserve a source-byte object, official still package,
decoded output manifest, frame checksums, or Keating sheet source package.

Decision state:

```text
ptuj_acquisition_manifest_attempted: true
official_branch_manifest_present: false
lawful_local_branch_manifest_present: false
keating_sheet_manifest_present: false
decoded_output_manifest_present: false
frame_checksums_present: false
formula_visibility_scope_present: false
acquisition_manifest_admitted: false
formula_visibility_audit_allowed: false
productab_member_emitted: false
target_import_used: false
claim_status_consistency_triggered: false
```

## 2. Strongest Positive Construction Attempt

The strongest positive manifest fields already in the repo are metadata:

```text
target_video_id: TzSEvmqxu48
official PTUJ page identity
YouTube oEmbed title/channel/embed URL
Keating missing-sheet transcript window
```

They establish route identity. They do not establish formula-bearing content
access or branch-pure custody.

## 3. First Exact Obstruction

First exact obstruction:

```text
PTUJBranchPureSourceAssetAcquisitionManifest_V1.content_access_or_source_bytes
is absent.
```

Without content access or source bytes, no formula visibility audit can begin.

## 4. Terrain And Guard

Terrain:

```text
provenance-verifier
```

Forbidden shortcut:

```text
Do not treat oEmbed, captions, prior manuscript formulas, or Oxford stills as
the missing PTUJ/Keating source asset.
```

## 5. Impact And Next Step

ProductAB remains locked:

```text
formula_visibility_audit_allowed: false
productab_member_emitted: false
```

Next meaningful object:

```text
PTUJFormulaVisibilityPrerequisiteGate_V1
```

It should say exactly which branch inputs are required before visibility,
transcription, and manuscript/Oxford identity checks can legally run.

## 6. JSON Summary

```json
{
  "artifact_id": "PTUJBranchPureSourceAssetAcquisitionManifest_0904_C2_L4_V1",
  "run_id": "hourly-20260626-0904",
  "cycle": 2,
  "lane": 4,
  "artifact_path": "explorations/hourly-20260626-0904-cycle2-productab-ptuj-acquisition-manifest.md",
  "verdict_class": "negative_no_branch_pure_acquisition_manifest",
  "ptuj_acquisition_manifest_attempted": true,
  "official_branch_manifest_present": false,
  "lawful_local_branch_manifest_present": false,
  "keating_sheet_manifest_present": false,
  "decoded_output_manifest_present": false,
  "frame_checksums_present": false,
  "formula_visibility_scope_present": false,
  "acquisition_manifest_admitted": false,
  "formula_visibility_audit_allowed": false,
  "productab_member_emitted": false,
  "first_exact_obstruction": "PTUJBranchPureSourceAssetAcquisitionManifest_V1.content_access_or_source_bytes_absent",
  "constructive_next_object": "PTUJFormulaVisibilityPrerequisiteGate_V1",
  "terrain": ["provenance-verifier"],
  "target_import_used": false,
  "claim_status_consistency_triggered": false,
  "claim_status_change": false
}
```
