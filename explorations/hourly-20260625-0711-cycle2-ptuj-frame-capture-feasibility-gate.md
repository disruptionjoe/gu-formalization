---
title: "Hourly 20260625 0711 Cycle 2 PTUJ Frame Capture Feasibility Gate"
date: "2026-06-25"
run_id: "hourly-20260625-0711"
cycle: 2
lane: 2
doc_type: ptuj_frame_capture_feasibility_gate
artifact_id: "FrameLevelPullThatUpJamieTzSEvmqxu48FormulaCaptureFeasibilityGate_V1"
verdict: "BLOCKED_TOOL_SOURCE_ACQUISITION_NO_FORMULA_FRAME_PACKET"
owned_path: "explorations/hourly-20260625-0711-cycle2-ptuj-frame-capture-feasibility-gate.md"
companion_audit: "tests/hourly_20260625_0711_cycle2_ptuj_frame_capture_feasibility_gate_audit.py"
---

# Hourly 20260625 0711 Cycle 2 PTUJ Frame Capture Feasibility Gate

## 1. Verdict

Verdict: **blocked**.

The repo/local tooling cannot now produce a formula-bearing frame/source-asset
packet for `TzSEvmqxu48`. The first exact blocker is still tool/source
acquisition:

```text
No installed local frame-extraction stack and no direct source asset URL were
available in this run; only official page HTML, YouTube embed/oEmbed metadata,
watch-page reachability, and thumbnail reachability were obtained.
```

Decision state:

```text
artifact: FrameLevelPullThatUpJamieTzSEvmqxu48FormulaCaptureFeasibilityGate_V1
target_video_id: TzSEvmqxu48
target_asset_id: PullThatUpJamie_GUForGRGaugeTheory_TzSEvmqxu48
accepted_formula_asset_count: 0
accepted_frame_packet_count: 0
formula_bearing_frame_captured: false
source_asset_packet_captured: false
proof_restart_allowed: false
```

This cycle improves the operational state over a timed-out-only watch attempt:
the YouTube watch URL responded to a HEAD request, and the YouTube thumbnail URL
responded. That is not a capture packet. A thumbnail, caption, iframe, or
oEmbed receipt is explicitly inadmissible for the requested formula frame.

## 2. What was derived directly from repo/source surfaces

`RESEARCH-POSTURE.md` allows aggressive pursuit of high-value missing source
objects but forbids claim promotion from compatibility, locator evidence, or
target agreement.

`process/runbooks/five-lane-frontier-run.md` requires a decision-grade lane with
the first exact obstruction and no promotion from undercaptured evidence.

The cycle-1 execution artifact,
`KeatingPullThatUpJamieShiabProjectionFormulaAssetPacketExecution_0711_V1`,
already established:

- the official Pull That Up Jamie page is acquisition-positive but
  receipt-negative;
- `TzSEvmqxu48` is the video id for `Geometric Unity for General Relativity &
  Gauge Theory`;
- the Keating transcript window `01:41:43-01:42:50` points to a missing
  representation-theory Shiab/projection sheet;
- `accepted_receipt_count = 0`;
- `proof_restart_allowed = false`.

The 0601 packet spec fixes the acceptance target:
`KeatingPullThatUpJamieShiabProjectionFormulaAssetPacket_V1` must contain a
source-stable visual/sheet/asset capture, exact formula/rule transcription,
target-import cleanliness, identity to the missing sheet or source-proven
equivalent, and family identity to `SourceForcedCodomainSelectorForK_IG`.

`sources/media-index.md` supplies the source ids used here:

| source_id | role in this gate | admissibility state |
| --- | --- | --- |
| `GU-MEDIA-2021-PULL-THAT-UP-JAMIE` | official visual-aid page and caption surface | source locator only |
| `GU-POD-2021-KEATING-REVEALED-1` | Keating transcript/source-family locator | missing-sheet locator only |
| `GU-POD-2021-KEATING-REVEALED-2` | paired Keating source-family locator | missing-sheet locator only |
| `GU-MEDIA-2021-DRAFT-RELEASE` | author manuscript surface from prior packet | adjacent candidate, not a PTUJ frame packet |

Live source/tool facts checked in this cycle:

| attempt_id | method | result | accepted? |
| --- | --- | --- | --- |
| `PTUJ_HTML_SCAN_0711_C2` | `Invoke-WebRequest` on `https://geometricunity.org/pull-that-up-jamie/` | HTTP 200; HTML length 72505; contains `TzSEvmqxu48`, `youtube`, `iframe`, and `Shiab Projection`; no `.mp4` or `.webm` link found | no |
| `YOUTUBE_OEMBED_0711_C2` | YouTube oEmbed for `TzSEvmqxu48` | HTTP 200; confirms title, author, thumbnail URL, and embed iframe | no |
| `YOUTUBE_WATCH_HEAD_0711_C2` | HEAD request to `https://www.youtube.com/watch?v=TzSEvmqxu48` | HTTP 200 text/html watch page reachable | no |
| `YOUTUBE_THUMBNAIL_HEAD_0711_C2` | HEAD request to `https://img.youtube.com/vi/TzSEvmqxu48/maxresdefault.jpg` | HTTP 200 image/jpeg; content length 54692 | no |
| `LOCAL_TOOL_CHECK_0711_C2` | `python -m yt_dlp`, `ffmpeg`, `yt-dlp`, `youtube-dl` | Python 3.14.3 present; `yt_dlp` module missing; `ffmpeg`, `yt-dlp`, and `youtube-dl` not recognized | no |
| `LOCAL_ASSET_SEARCH_0711_C2` | repo search for local `TzSEvmqxu48`/PTUJ assets | no matching local asset file found | no |

The web surfaces checked directly were the official Pull That Up Jamie page,
YouTube oEmbed for `TzSEvmqxu48`, the YouTube watch URL, the YouTube thumbnail
URL, and the Portal Group Keating Revealed transcript.

## 3. Strongest positive capture attempt

The strongest positive capture attempt is the current four-part operational
triangle:

| surface | positive fact | why it is not accepted |
| --- | --- | --- |
| Official PTUJ page HTML | The page is reachable and embeds `youtube.com/embed/TzSEvmqxu48?feature=oembed`; caption text names `Shiab Projection`. | HTML exposes an iframe/caption, not video bytes, frames, formula text, or a source asset package. |
| YouTube oEmbed | The video title is `Geometric Unity for General Relativity & Gauge Theory`; the provider returns thumbnail and iframe metadata. | oEmbed is metadata. It is explicitly not an accepted selector receipt. |
| YouTube watch URL | The watch page is reachable by HEAD. | A reachable HTML page is not frame extraction and does not supply formula-bearing frames. |
| YouTube thumbnail URL | The thumbnail endpoint is reachable as JPEG. | A thumbnail is metadata/preview material and was not accepted as a frame/source asset; no formula was captured or transcribed. |

This attempt proves feasibility only up to "the video identity is live and
addressable." It does not prove the repo can currently extract frame sequences,
and it does not emit any formula, projection rule, sheet scan, or manuscript
equivalence proof.

Receipt rows after this cycle:

| candidate_receipt_id | source_surface | asset_or_locator | formula_or_rule_transcribed | accepted_for_routing | reason |
| --- | --- | --- | --- | --- | --- |
| `PTUJ_TzSEvmqxu48_EmbedCaption_0711_C2` | `GU-MEDIA-2021-PULL-THAT-UP-JAMIE` | official page caption and embed id | false | false | caption/iframe only |
| `YouTube_TzSEvmqxu48_OEmbed_0711_C2` | YouTube oEmbed | title, iframe, thumbnail metadata | false | false | metadata only |
| `YouTube_TzSEvmqxu48_WatchReachable_0711_C2` | YouTube watch URL | watch page HEAD 200 | false | false | no frames or video stream captured |
| `YouTube_TzSEvmqxu48_ThumbnailReachable_0711_C2` | YouTube thumbnail URL | JPEG HEAD 200 | false | false | thumbnail metadata/preview, no formula asset accepted |
| `KeatingRevealed_014143_014250_MissingSheet_0711_C2` | Keating transcript | missing-sheet locator | false | false | source says the representation-theory sheet was not found |

## 4. First exact obstruction/missing object

The first exact operational obstruction is:

```text
LocalFrameExtractionToolchainForTzSEvmqxu48_V1 is missing: no yt_dlp module,
no yt-dlp executable, no youtube-dl executable, and no ffmpeg executable were
available; the official page did not expose a direct downloadable video asset.
```

The first exact source object still missing is:

```text
TzSEvmqxu48_FormulaBearingFrameOrSourceAssetPacket_V1, with frame/source
checksums, exact time/frame locators, and visible formula/projection-rule
transcription.
```

The first exact mathematical/source identity object still missing is:

```text
KeatingRevealed_ShiabProjectionSheet_V1 or a source-proven equivalent that can
be tested against SourceForcedCodomainSelectorForK_IG.
```

Therefore the gate is blocked before any proof restart. The obstruction is not
caption interpretation and not target import. It is absence of an accepted
formula-bearing source object.

## 5. Impact if closed

Closing this gate would produce one admissible source packet for IG selector
review, not a downstream physics proof.

Closure would require:

| required object | minimum content |
| --- | --- |
| `LocalFrameExtractionToolchainForTzSEvmqxu48_V1` or source asset equivalent | lawful local method that extracts frame images/source bytes without writing uncontrolled repo assets |
| `TzSEvmqxu48_FormulaBearingFrameOrSourceAssetPacket_V1` | checksummed frames/source asset, exact time/frame locator, visible formula/rule transcription, and uncertainty marks |
| `ManuscriptShiabProjectionIdentityCheck_V1` | comparison to manuscript pages 41-44 only after a source object exists |
| `SourceForcedCodomainSelectorForK_IG` identity check | explicit pass/fail against the required IG selector family |

If closed, the repo could replace caption-only PTUJ evidence with a real visual
receipt candidate. The packet alone would not promote theta/FLRW, dark energy,
QFT extraction, DGU/VZ, RS, or generation-count claims.

## 6. Falsification/demotion condition

Demote the PTUJ frame-capture route from blocked acquisition to scoped
source-route fail if a complete lawful extraction/source-asset pass shows all
of the following:

- the `TzSEvmqxu48` frame sequence contains no legible formula, projection rule,
  sheet view, or source text relevant to Shiab Projection;
- the official PTUJ page and linked assets expose no direct formula-bearing
  source package;
- the Keating representation-theory sheet remains unrecovered;
- the author manuscript remains only an adjacent Shiab candidate, not a
  source-proven equivalent to the missing sheet or PTUJ frame;
- any identity bridge to `SourceForcedCodomainSelectorForK_IG` requires
  target-facing physics or reconstruction preference.

That would fail this source route only. It would not be a global GU no-go.

## 7. Next meaningful acquisition step

Next object:

```text
LawfulLocalTzSEvmqxu48FrameExtractorOrSourceAsset_V1
```

Concrete next step:

1. Acquire an approved local frame-extraction path, such as `yt-dlp` plus
   `ffmpeg`, or obtain a direct source asset package from an official custodian.
2. Extract candidate text-bearing frames for `TzSEvmqxu48` into a controlled
   scratch/output path selected by the coordinator, not this lane.
3. Record checksums, frame/time locators, and the extraction command/version.
4. Accept only visible formula/projection-rule content from frames/source
   bytes. Do not accept captions, oEmbed, thumbnails, or page metadata.
5. Only after a formula-bearing packet exists, run the manuscript/sheet identity
   check against `SourceForcedCodomainSelectorForK_IG`.

Until this object exists, `proof_restart_allowed` remains `false`.

## 8. Machine-readable JSON summary

```json
{
  "artifact": "FrameLevelPullThatUpJamieTzSEvmqxu48FormulaCaptureFeasibilityGate_V1",
  "version": "2026-06-25",
  "run_id": "hourly-20260625-0711",
  "cycle": 2,
  "lane": 2,
  "verdict": "BLOCKED_TOOL_SOURCE_ACQUISITION_NO_FORMULA_FRAME_PACKET",
  "verdict_class": "blocked",
  "target_video_id": "TzSEvmqxu48",
  "target_asset_id": "PullThatUpJamie_GUForGRGaugeTheory_TzSEvmqxu48",
  "target_packet": "KeatingPullThatUpJamieShiabProjectionFormulaAssetPacket_V1",
  "required_object": "SourceForcedCodomainSelectorForK_IG",
  "required_source_surfaces": [
    "GU-MEDIA-2021-PULL-THAT-UP-JAMIE",
    "GU-POD-2021-KEATING-REVEALED-1",
    "GU-POD-2021-KEATING-REVEALED-2",
    "GU-MEDIA-2021-DRAFT-RELEASE"
  ],
  "source_surfaces": [
    {
      "surface_id": "PullThatUpJamie_GUForGRGaugeTheory_TzSEvmqxu48",
      "source_ids": [
        "GU-MEDIA-2021-PULL-THAT-UP-JAMIE"
      ],
      "source_url": "https://geometricunity.org/pull-that-up-jamie/",
      "video_id": "TzSEvmqxu48",
      "retrieval_status": "page_reachable_html_exposes_iframe_video_id_and_shiab_projection_caption",
      "formula_or_rule_transcribed": false,
      "accepted_for_routing": false
    },
    {
      "surface_id": "YouTube_TzSEvmqxu48",
      "source_ids": [
        "GU-MEDIA-2021-PULL-THAT-UP-JAMIE"
      ],
      "watch_url": "https://www.youtube.com/watch?v=TzSEvmqxu48",
      "oembed_url": "https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v=TzSEvmqxu48&format=json",
      "thumbnail_url": "https://img.youtube.com/vi/TzSEvmqxu48/maxresdefault.jpg",
      "video_id": "TzSEvmqxu48",
      "retrieval_status": "watch_head_oembed_and_thumbnail_head_reachable",
      "formula_or_rule_transcribed": false,
      "accepted_for_routing": false
    },
    {
      "surface_id": "KeatingRevealedTranscriptWindow",
      "source_ids": [
        "GU-POD-2021-KEATING-REVEALED-1",
        "GU-POD-2021-KEATING-REVEALED-2"
      ],
      "source_url": "https://theportal.group/into-the-impossible-eric-weinstein-geometric-unity-revealed/",
      "locator": "01:41:43-01:42:50",
      "retrieval_status": "reachable_missing_sheet_locator",
      "formula_or_rule_transcribed": false,
      "accepted_for_routing": false
    },
    {
      "surface_id": "AuthorManuscriptPages41To44",
      "source_ids": [
        "GU-MEDIA-2021-DRAFT-RELEASE"
      ],
      "retrieval_status": "prior_packet_adjacent_candidate_only",
      "formula_or_rule_transcribed": true,
      "identity_to_missing_sheet_proved": false,
      "accepted_for_routing": false
    }
  ],
  "retrieval_attempts": [
    {
      "attempt_id": "PTUJ_HTML_SCAN_0711_C2",
      "method": "Invoke-WebRequest_html_scan",
      "result": "http_200_contains_TzSEvmqxu48_youtube_iframe_shiab_projection_no_mp4_no_webm",
      "accepted_receipt": false
    },
    {
      "attempt_id": "YOUTUBE_OEMBED_0711_C2",
      "method": "youtube_oembed_json",
      "result": "http_200_title_author_iframe_thumbnail_metadata_only",
      "accepted_receipt": false
    },
    {
      "attempt_id": "YOUTUBE_WATCH_HEAD_0711_C2",
      "method": "Invoke-WebRequest_HEAD_watch_url",
      "result": "http_200_text_html_watch_page_reachable",
      "accepted_receipt": false
    },
    {
      "attempt_id": "YOUTUBE_THUMBNAIL_HEAD_0711_C2",
      "method": "Invoke-WebRequest_HEAD_thumbnail_url",
      "result": "http_200_image_jpeg_content_length_54692",
      "accepted_receipt": false
    },
    {
      "attempt_id": "LOCAL_TOOL_CHECK_0711_C2",
      "method": "python_yt_dlp_ffmpeg_yt_dlp_youtube_dl_version_checks",
      "result": "python_3_14_3_present_yt_dlp_module_missing_ffmpeg_yt_dlp_youtube_dl_not_recognized",
      "accepted_receipt": false
    },
    {
      "attempt_id": "LOCAL_ASSET_SEARCH_0711_C2",
      "method": "repo_file_search",
      "result": "no_local_TzSEvmqxu48_or_PTUJ_source_asset_file_found",
      "accepted_receipt": false
    }
  ],
  "capture_state": {
    "formula_bearing_frame_captured": false,
    "source_asset_packet_captured": false,
    "accepted_formula_asset_count": 0,
    "accepted_frame_packet_count": 0,
    "accepted_receipt_count": 0,
    "accepted_for_routing_count": 0,
    "accepted_receipts": [],
    "metadata_receipt_count": 4,
    "thumbnail_or_caption_receipt_accepted": false,
    "formula_asset_captured": false,
    "claim_promotion_allowed": false,
    "proof_restart_allowed": false
  },
  "tool_state": {
    "python_version": "3.14.3",
    "yt_dlp_module_available": false,
    "yt_dlp_executable_available": false,
    "youtube_dl_executable_available": false,
    "ffmpeg_available": false,
    "direct_mp4_or_webm_url_found": false
  },
  "target_import_guard": {
    "target_data_seen": [],
    "target_import_clean": true,
    "target_import_clean_sufficient_for_acceptance": false,
    "target_outcome_used_to_select_or_normalize_source_object": false
  },
  "first_exact_obstruction": {
    "id": "LocalFrameExtractionToolchainForTzSEvmqxu48_V1",
    "obstruction_type": "tool_source_acquisition",
    "operational_obstruction": "No yt_dlp module, no yt-dlp executable, no youtube-dl executable, no ffmpeg executable, and no direct mp4/webm source asset URL from the official page.",
    "missing_next_object": "LawfulLocalTzSEvmqxu48FrameExtractorOrSourceAsset_V1",
    "missing_source_objects": [
      "TzSEvmqxu48_FormulaBearingFrameOrSourceAssetPacket_V1",
      "KeatingRevealed_ShiabProjectionSheet_V1",
      "manuscript_equivalence_proof_to_SourceForcedCodomainSelectorForK_IG"
    ]
  },
  "impact_if_closed": {
    "would_create_ig_receipt_candidate": true,
    "accepted_visual_formula_receipt_count_would_be": 1,
    "proof_restart_possible_only_after_receipt_and_family_identity": true,
    "downstream_physics_promoted_by_packet_alone": false
  },
  "falsification_or_demotion_condition": [
    "complete_lawful_extraction_finds_no_formula_projection_rule_sheet_view_or_source_text_in_TzSEvmqxu48",
    "official_PTUJ_page_and_linked_assets_expose_no_formula_bearing_source_package",
    "KeatingRevealed_ShiabProjectionSheet_V1_remains_unrecovered",
    "manuscript_pages_41_44_remain_adjacent_not_source_equivalent",
    "bridge_to_SourceForcedCodomainSelectorForK_IG_requires_target_import"
  ],
  "next_meaningful_acquisition_step": {
    "next_object": "LawfulLocalTzSEvmqxu48FrameExtractorOrSourceAsset_V1",
    "description": "Acquire an approved local frame extractor such as yt-dlp plus ffmpeg or obtain an official source asset package, then capture checksummed formula-bearing frames before any manuscript or selector identity check."
  },
  "forbidden_promotions": {
    "caption_or_oembed_selector_receipt_accepted": false,
    "thumbnail_receipt_accepted": false,
    "formula_asset_captured": false,
    "SourceForcedCodomainSelectorForK_IG_accepted": false,
    "family_identity_passed": false,
    "proof_restart": false,
    "downstream_physics_claim": false
  }
}
```
