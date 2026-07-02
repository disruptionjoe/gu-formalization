---
title: "Hourly 20260625 0803 Cycle 1 PTUJ Lawful Source Asset Admission Gate"
date: "2026-06-25"
run_id: "hourly-20260625-0803"
cycle: 1
lane: 1
doc_type: ptuj_lawful_source_asset_admission_gate
artifact_id: "LawfulLocalTzSEvmqxu48FrameExtractorOrSourceAsset_V1"
verdict: "BLOCKED_NO_LAWFUL_LOCAL_EXTRACTOR_OR_FORMULA_SOURCE_ASSET"
owned_path: "explorations/hourly-20260625-0803-cycle1-ptuj-lawful-source-asset-admission-gate.md"
companion_audit: "tests/hourly_20260625_0803_cycle1_ptuj_lawful_source_asset_admission_gate_audit.py"
---

# Hourly 20260625 0803 Cycle 1 PTUJ Lawful Source Asset Admission Gate

## 1. Verdict.

Verdict: **blocked**.

`LawfulLocalTzSEvmqxu48FrameExtractorOrSourceAsset_V1` is not currently
admitted. The repo has source locators, metadata, prior low-resolution
storyboard inspection, and a missing-sheet locator, but it does not have either
of the two objects this gate needs:

```text
1. a lawful local extractor that can decode TzSEvmqxu48 into frame images with
   command/version/provenance fields; or
2. a direct source asset package, sheet scan/photo, or frame image containing a
   visible Shiab/projection formula.
```

Decision state:

```text
artifact: LawfulLocalTzSEvmqxu48FrameExtractorOrSourceAsset_V1
target_video_id: TzSEvmqxu48
accepted_receipt_count: 0
accepted_for_routing_count: 0
formula_bearing_source_asset_admitted: false
lawful_local_extractor_admitted: false
proof_restart_allowed: false
claim_promotion_allowed: false
```

This is not a demotion to route fail. The previous 0703 artifact produced a
bounded negative at storyboard/thumbnail resolution and a full-stream HTTP 403
blocker. The present gate is narrower: it asks whether the repo now has enough
source material or lawful local acquisition machinery to admit a
formula-bearing frame/source asset. It does not.

## 2. Specific GU claim or bridge under test.

Bridge under test:

```text
Pull That Up Jamie official page / YouTube id TzSEvmqxu48
  -> lawful local frame extractor or direct source asset
  -> formula-bearing frame/source packet
  -> identity to Keating missing Shiab/projection sheet or source equivalent
  -> SourceForcedCodomainSelectorForK_IG review
```

The gate is not testing whether the Pull That Up Jamie caption names "Shiab
Projection"; prior artifacts established that it does. The gate is testing
admission: whether a source-clean, locally auditable acquisition path or
formula-bearing source object exists now.

## 3. Owned output path and sources read first.

Owned output path:

```text
explorations/hourly-20260625-0803-cycle1-ptuj-lawful-source-asset-admission-gate.md
```

Companion audit:

```text
tests/hourly_20260625_0803_cycle1_ptuj_lawful_source_asset_admission_gate_audit.py
```

Sources read first:

| source | role in this gate |
| --- | --- |
| `RESEARCH-POSTURE.md` | Mission A posture; forbids proof inflation from compatibility, metadata, or target agreement. |
| `process/runbooks/five-lane-frontier-run.md` | Verdict vocabulary, worker contract, no-proof-restart discipline. |
| `explorations/hourly-20260625-0711-three-cycle-fifteen-hole-synthesis.md` | Establishes `LawfulLocalTzSEvmqxu48FrameExtractorOrSourceAsset_V1` as the next PTUJ/Keating frontier object. |
| `explorations/hourly-20260625-0711-cycle1-keating-ptuj-shiab-asset-execution.md` | Establishes caption/oEmbed/transcript/manuscript locators but zero formula-bearing asset receipts. |
| `explorations/hourly-20260625-0711-cycle2-ptuj-frame-capture-feasibility-gate.md` | Establishes missing local extractor/toolchain and no direct source asset from official page metadata. |
| `sources/media-index.md` | Supplies source ids and use discipline for Pull That Up Jamie, Keating, and the draft release. |

Additional repo-local context read because it directly controls this gate:

| source | role in this gate |
| --- | --- |
| `explorations/hourly-20260625-0703-cycle2-keating-tzsevmqxu48-frame-capture-gate.md` | Supplies strongest prior frame-level attempt: storyboard/thumbnail negative at available resolution and full-stream HTTP 403 blocker. |
| `tests/hourly_20260625_0711_cycle2_ptuj_frame_capture_feasibility_gate_audit.py` | Supplies deterministic audit pattern and fields that must not be inflated. |

## 4. What was derived directly from repo sources.

Direct repo-derived facts:

| fact | repo basis | admission implication |
| --- | --- | --- |
| `TzSEvmqxu48` is the Pull That Up Jamie video id for `Geometric Unity for General Relativity & Gauge Theory`. | 0711 cycle-1 and cycle-2 PTUJ artifacts plus `sources/media-index.md`. | Source identity is known, but identity is not a formula asset. |
| The official Pull That Up Jamie page is an official visual-aid source surface and the caption names Shiab Projection. | `GU-MEDIA-2021-PULL-THAT-UP-JAMIE` rows and prior PTUJ artifacts. | Caption/iframe/oEmbed are locator metadata only. |
| The Keating `01:41:43-01:42:50` window points to representation-theory/projection calculations on a paper sheet that was not found. | 0711 cycle-1 artifact and media-index Keating source ids. | This is a positive missing-object locator, not the missing object. |
| Manuscript pages 41-44 are adjacent Shiab candidate material. | Prior PTUJ/IG artifacts. | They remain quarantined because identity to the missing sheet and `SourceForcedCodomainSelectorForK_IG` is not proved. |
| The 0703 frame gate acquired storyboard/thumbnail material and found no formula at available resolution, while full-resolution decoding was blocked by YouTube media-host HTTP 403. | `hourly-20260625-0703-cycle2-keating-tzsevmqxu48-frame-capture-gate.md`. | Stronger than metadata, but still not an accepted frame/source asset. |
| The 0711 feasibility gate found no installed local frame-extraction stack and no direct mp4/webm asset exposed by the official page. | `hourly-20260625-0711-cycle2-ptuj-frame-capture-feasibility-gate.md`. | The named lawful-local acquisition object is still missing. |

Current repo-local checks in this lane:

| check | result | admission implication |
| --- | --- | --- |
| `Get-Command python, ffmpeg, yt-dlp, youtube-dl` | Python present at `AppData\Local\Programs\Python\Python314\python.exe`; `ffmpeg`, `yt-dlp`, and `youtube-dl` not resolved. | No local video decoder/downloader stack was admitted. |
| `python -m yt_dlp --version` | Python reported `No module named yt_dlp`. | No Python `yt_dlp` extractor module was available. |
| repo file search for `TzSEvmqxu48`, Pull That Up Jamie/PTUJ, Keating/Shiab assets | Found prior markdown/audit artifacts and Shiab notes, but no local `TzSEvmqxu48` media file or PTUJ source asset package. | No repo-local formula-bearing video/source asset exists under the searched names. |
| narrow live-source HEAD recheck on repo-listed URLs | The PowerShell HEAD wrapper returned non-admission errors for the official PTUJ page, YouTube oEmbed, YouTube thumbnail, and Keating transcript. | This does not change the verdict; live success was not required and no receipt was admitted from the failed recheck. |

## 5. Strongest positive construction/admission attempt.

The strongest positive construction is a source-identity and acquisition-chain
attempt, not a receipt:

| candidate object | positive support | why it is not admitted |
| --- | --- | --- |
| `PullThatUpJamie_GUForGRGaugeTheory_TzSEvmqxu48` | Official PTUJ page and YouTube metadata identify the visual aid and caption it as Shiab Projection. | Caption, iframe, oEmbed, watch-page metadata, and thumbnails are not formula-bearing source assets. |
| `TzSEvmqxu48_storyboard_thumbnail_scan_0703` | Prior artifact acquired 69 one-second storyboard frames at 160x90 plus thumbnail checksums and found no formula visible at that resolution. | Storyboard frames are low-resolution preview material and were formula-negative; they do not close full-resolution source acquisition. |
| `KeatingRevealed_ShiabProjectionSheetLocator_014143_014250` | Transcript window gives a precise missing-sheet locator for representation-theory/projection calculations. | The sheet remains missing; a locator is not a scan/photo/formula. |
| `AuthorManuscriptPages41To44_AdjacentShiabCandidate` | Manuscript has adjacent Shiab formulas/codomain material from prior packets. | No source-emitted identity to the missing Keating sheet or `SourceForcedCodomainSelectorForK_IG`. |
| local extraction machinery | Python exists locally. | Missing `yt_dlp` module, `yt-dlp`, `youtube-dl`, and `ffmpeg`; Python alone is not an extractor. |

The strongest admissible statement is therefore:

```text
The source route is well located, and prior attempts have non-formula
storyboard evidence plus a full-stream blocker. The repo does not currently
possess the lawful local extractor/source asset object needed for formula-frame
admission.
```

## 6. First exact obstruction or missing object.

The first exact missing object is:

```text
LawfulLocalTzSEvmqxu48FrameExtractorOrSourceAsset_V1
```

Minimum admissible fields for that object:

| field | required content |
| --- | --- |
| `acquisition_mode` | either `local_extractor` or `direct_source_asset`; not caption/oEmbed/thumbnail metadata. |
| `lawful_basis` | source URL already present in repo sources, official archive/custodian package, or locally provided asset with provenance. |
| `toolchain` | command, executable/module versions, and decode/extraction path if using a local extractor. |
| `asset_locator` | video id, archive id, frame timecode/range, source package id, or sheet scan/photo id. |
| `checksums` | checksums for extracted frames, source asset, or sheet/photo file. |
| `formula_or_rule_visibility` | visible formula/projection-rule text, or an explicit formula-negative result after complete frame/source inspection. |
| `target_import_guard` | no target-facing physics outcomes used to select, normalize, or accept the object. |

The first downstream missing source object is:

```text
TzSEvmqxu48_FormulaBearingFrameOrSourceAssetPacket_V1
```

The first downstream identity object remains:

```text
KeatingRevealed_ShiabProjectionSheet_V1
```

or a source-proven equivalent that can be compared to:

```text
SourceForcedCodomainSelectorForK_IG
```

## 7. Impact if closed.

If `LawfulLocalTzSEvmqxu48FrameExtractorOrSourceAsset_V1` closes, the route
would move from acquisition gating to source-packet inspection. The immediate
impact would be:

| closure result | impact |
| --- | --- |
| lawful local extractor admitted | The repo can decode and audit `TzSEvmqxu48` frames locally, preserving versions, commands, timecodes, and checksums. |
| direct source asset admitted | The repo can inspect an official/source-stable PTUJ asset without relying on live remote playback. |
| formula-bearing frame/source found | A candidate visual formula receipt can be built for comparison to manuscript pages and the Keating missing sheet. |
| full audit formula-negative | The PTUJ video route can be demoted to scoped source-route fail, if the page/assets/sheet routes are also exhausted. |

Closure of this admission gate would not itself prove or promote IG, theta/FLRW,
dark energy, QFT extraction, DGU/VZ, RS, or generation-count claims. It would
only unlock a later formula-packet and family-identity review.

## 8. Falsification/demotion condition.

Demote the PTUJ/Keating route from blocked admission to scoped source-route
`fail` only after a complete lawful extraction/source-asset audit shows all of:

- `TzSEvmqxu48` is fully decoded or source-equivalent frames/assets are fully
  inspected.
- No frame/source asset contains a legible Shiab formula, projection rule,
  sheet view, or source text beyond caption/animation labels.
- The official Pull That Up Jamie page and linked source assets expose no
  formula-bearing package.
- `KeatingRevealed_ShiabProjectionSheet_V1` remains unrecovered.
- Manuscript pages 41-44 remain adjacent candidate material only, without
  representation-theory/Bianchi rival eliminators or identity to
  `SourceForcedCodomainSelectorForK_IG`.
- Any claimed bridge would require target-facing physical outcomes or
  reconstruction preference.

That demotion would be local to the PTUJ/Keating source route. It would not be a
global GU no-go or a no-go for the existence of a Shiab selector from other
sources.

## 9. Next meaningful computation or proof/source step.

Next meaningful step:

```text
Acquire or stage LawfulLocalTzSEvmqxu48FrameExtractorOrSourceAsset_V1 in a
coordinator-owned scratch/output path, then run a deterministic frame/source
packet audit.
```

Concrete source/computation step:

1. Obtain an approved local extractor stack, minimally `yt-dlp` plus `ffmpeg`,
   or obtain an official archive/source asset package from a source custodian.
2. Record command lines, versions, source URL/archive id, and legal/provenance
   basis.
3. Decode the 68-second `TzSEvmqxu48` asset at 1 fps and around every text or
   scene transition; store checksums and exact timecodes in the assigned output
   path for that future lane.
4. OCR/manual-inspect only visible source text or formula-like notation.
5. If a formula-bearing frame/source object appears, compare it to manuscript
   equations `8.1`, `8.7`, `9.2`, `9.3` and the Keating missing-sheet locator.
6. Only after that comparison, run a family identity check against
   `SourceForcedCodomainSelectorForK_IG`.

Until step 1 or a direct source asset exists:

```text
accepted_receipt_count = 0
proof_restart_allowed = false
claim_promotion_allowed = false
```

## 10. Machine-readable JSON summary.

```json
{
  "artifact": "LawfulLocalTzSEvmqxu48FrameExtractorOrSourceAsset_V1",
  "version": "2026-06-25",
  "run_id": "hourly-20260625-0803",
  "cycle": 1,
  "lane": 1,
  "verdict": "BLOCKED_NO_LAWFUL_LOCAL_EXTRACTOR_OR_FORMULA_SOURCE_ASSET",
  "verdict_class": "blocked",
  "owned_path": "explorations/hourly-20260625-0803-cycle1-ptuj-lawful-source-asset-admission-gate.md",
  "companion_audit": "tests/hourly_20260625_0803_cycle1_ptuj_lawful_source_asset_admission_gate_audit.py",
  "target_video_id": "TzSEvmqxu48",
  "target_asset_id": "PullThatUpJamie_GUForGRGaugeTheory_TzSEvmqxu48",
  "target_admission_object": "LawfulLocalTzSEvmqxu48FrameExtractorOrSourceAsset_V1",
  "downstream_formula_packet": "TzSEvmqxu48_FormulaBearingFrameOrSourceAssetPacket_V1",
  "downstream_missing_sheet": "KeatingRevealed_ShiabProjectionSheet_V1",
  "required_identity_object": "SourceForcedCodomainSelectorForK_IG",
  "sources_read_first": [
    "RESEARCH-POSTURE.md",
    "process/runbooks/five-lane-frontier-run.md",
    "explorations/hourly-20260625-0711-three-cycle-fifteen-hole-synthesis.md",
    "explorations/hourly-20260625-0711-cycle1-keating-ptuj-shiab-asset-execution.md",
    "explorations/hourly-20260625-0711-cycle2-ptuj-frame-capture-feasibility-gate.md",
    "sources/media-index.md"
  ],
  "additional_repo_context": [
    "explorations/hourly-20260625-0703-cycle2-keating-tzsevmqxu48-frame-capture-gate.md",
    "tests/hourly_20260625_0711_cycle2_ptuj_frame_capture_feasibility_gate_audit.py"
  ],
  "required_source_surfaces": [
    "GU-MEDIA-2021-PULL-THAT-UP-JAMIE",
    "GU-POD-2021-KEATING-REVEALED-1",
    "GU-POD-2021-KEATING-REVEALED-2",
    "GU-MEDIA-2021-DRAFT-RELEASE"
  ],
  "source_coverage": [
    {
      "surface_id": "PullThatUpJamie_GUForGRGaugeTheory_TzSEvmqxu48",
      "source_ids": ["GU-MEDIA-2021-PULL-THAT-UP-JAMIE"],
      "source_url": "https://geometricunity.org/pull-that-up-jamie/",
      "video_id": "TzSEvmqxu48",
      "repo_derived_state": "official_visual_aid_caption_and_embed_locator_only",
      "formula_bearing_source_asset_admitted": false,
      "accepted_receipt": false
    },
    {
      "surface_id": "YouTube_TzSEvmqxu48_MetadataAndPriorStoryboard",
      "source_ids": ["GU-MEDIA-2021-PULL-THAT-UP-JAMIE"],
      "watch_url": "https://www.youtube.com/watch?v=TzSEvmqxu48",
      "oembed_url": "https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v=TzSEvmqxu48&format=json",
      "thumbnail_url": "https://img.youtube.com/vi/TzSEvmqxu48/maxresdefault.jpg",
      "repo_derived_state": "metadata_and_prior_storyboard_thumbnail_material_not_formula_receipt_full_stream_decode_blocked_http_403",
      "formula_bearing_source_asset_admitted": false,
      "accepted_receipt": false
    },
    {
      "surface_id": "KeatingRevealedTranscriptWindow",
      "source_ids": ["GU-POD-2021-KEATING-REVEALED-1", "GU-POD-2021-KEATING-REVEALED-2"],
      "source_url": "https://theportal.group/into-the-impossible-eric-weinstein-geometric-unity-revealed/",
      "locator": "01:41:43-01:42:50",
      "repo_derived_state": "missing_sheet_locator_only",
      "formula_bearing_source_asset_admitted": false,
      "accepted_receipt": false
    },
    {
      "surface_id": "AuthorManuscriptPages41To44",
      "source_ids": ["GU-MEDIA-2021-DRAFT-RELEASE"],
      "repo_derived_state": "adjacent_shiab_candidate_identity_to_missing_sheet_not_proved",
      "formula_bearing_source_asset_admitted": false,
      "accepted_receipt": false
    }
  ],
  "current_lane_checks": [
    {
      "check_id": "LOCAL_COMMAND_RESOLUTION_0803_C1_L1",
      "method": "Get-Command python ffmpeg yt-dlp youtube-dl",
      "result": "python_present_ffmpeg_missing_yt_dlp_executable_missing_youtube_dl_missing",
      "accepted_receipt": false
    },
    {
      "check_id": "PYTHON_YTDLP_MODULE_CHECK_0803_C1_L1",
      "method": "python -m yt_dlp --version",
      "result": "No module named yt_dlp",
      "accepted_receipt": false
    },
    {
      "check_id": "LOCAL_ASSET_SEARCH_0803_C1_L1",
      "method": "repo_file_search_for_TzSEvmqxu48_PTUJ_PullThatUpJamie_Keating_Shiab",
      "result": "prior_markdown_audit_and_shiab_notes_found_no_local_TzSEvmqxu48_media_or_PTUJ_source_asset_package",
      "accepted_receipt": false
    },
    {
      "check_id": "SOURCE_URL_HEAD_RECHECK_0803_C1_L1",
      "method": "Invoke-WebRequest_HEAD_on_repo_listed_source_urls",
      "result": "powershell_head_wrapper_returned_non_admission_errors_for_all_checked_urls_not_used_for_acceptance",
      "accepted_receipt": false
    }
  ],
  "tool_state": {
    "python_available": true,
    "python_source": "C:\\Users\\joe\\AppData\\Local\\Programs\\Python\\Python314\\python.exe",
    "yt_dlp_module_available": false,
    "yt_dlp_executable_available": false,
    "youtube_dl_executable_available": false,
    "ffmpeg_available": false,
    "lawful_local_extractor_admitted": false
  },
  "asset_state": {
    "direct_source_asset_package_found": false,
    "local_tzsevmqxu48_media_file_found": false,
    "formula_bearing_frame_captured": false,
    "formula_bearing_source_asset_admitted": false,
    "keating_missing_sheet_recovered": false,
    "manuscript_equivalence_proof_to_selector_found": false
  },
  "receipt_state": {
    "accepted_receipt_count": 0,
    "accepted_for_routing_count": 0,
    "accepted_receipts": [],
    "accepted_formula_asset_count": 0,
    "accepted_frame_packet_count": 0,
    "formula_asset_captured": false,
    "thumbnail_or_caption_receipt_accepted": false,
    "family_identity_checks_passed": 0,
    "proof_restart_allowed": false,
    "claim_promotion_allowed": false,
    "global_no_go_promoted": false
  },
  "first_exact_obstruction": {
    "id": "LawfulLocalTzSEvmqxu48FrameExtractorOrSourceAsset_V1",
    "obstruction_type": "admission_gate_missing_object",
    "description": "The repo currently has neither an admitted lawful local extractor toolchain nor a direct formula-bearing source asset for TzSEvmqxu48.",
    "missing_objects": [
      "LawfulLocalTzSEvmqxu48FrameExtractorOrSourceAsset_V1",
      "TzSEvmqxu48_FormulaBearingFrameOrSourceAssetPacket_V1",
      "KeatingRevealed_ShiabProjectionSheet_V1",
      "manuscript_equivalence_proof_to_SourceForcedCodomainSelectorForK_IG"
    ]
  },
  "impact_if_closed": {
    "would_enable_formula_packet_audit": true,
    "would_create_accepted_receipt_by_itself": false,
    "would_allow_family_identity_review_only_after_formula_packet": true,
    "downstream_physics_promoted_by_gate_alone": false
  },
  "falsification_or_demotion_condition": [
    "complete_lawful_full_resolution_extraction_or_source_asset_audit_finds_no_formula_projection_rule_sheet_view_or_source_text",
    "official_PTUJ_page_and_linked_assets_expose_no_formula_bearing_package",
    "KeatingRevealed_ShiabProjectionSheet_V1_remains_unrecovered",
    "manuscript_pages_41_44_remain_adjacent_without_selector_identity",
    "bridge_to_SourceForcedCodomainSelectorForK_IG_requires_target_import"
  ],
  "next_meaningful_step": {
    "next_object": "LawfulLocalTzSEvmqxu48FrameExtractorOrSourceAsset_V1",
    "description": "Install or stage an approved local extractor such as yt-dlp plus ffmpeg, or obtain an official source asset package; then decode or inspect with checksums and timecodes before any formula or selector identity claim."
  },
  "target_import_guard": {
    "target_data_seen": [],
    "target_import_clean": true,
    "target_import_clean_sufficient_for_acceptance": false,
    "target_outcome_used_to_select_or_normalize_source_object": false
  },
  "forbidden_promotions": {
    "caption_or_oembed_selector_receipt_accepted": false,
    "thumbnail_receipt_accepted": false,
    "storyboard_negative_promoted_to_full_route_fail": false,
    "formula_asset_captured": false,
    "SourceForcedCodomainSelectorForK_IG_accepted": false,
    "family_identity_passed": false,
    "proof_restart": false,
    "downstream_physics_claim": false,
    "global_no_go": false
  }
}
```
