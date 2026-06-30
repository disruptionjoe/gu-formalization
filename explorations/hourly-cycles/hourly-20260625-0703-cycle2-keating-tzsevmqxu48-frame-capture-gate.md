---
title: "Hourly 20260625 0703 Cycle 2 Keating TzSEvmqxu48 Frame Capture Gate"
date: "2026-06-25"
run_id: "hourly-20260625-0703"
cycle: 2
lane: 2
doc_type: keating_tzsevmqxu48_frame_capture_gate
artifact_id: "FrameLevelPullThatUpJamieTzSEvmqxu48FormulaCaptureAndManuscriptIdentityCheck_V1"
verdict: "BLOCKED_FRAME_STREAM_DECODE_STORYBOARD_NEGATIVE_ZERO_ACCEPTED_RECEIPTS"
owned_path: "explorations/hourly-20260625-0703-cycle2-keating-tzsevmqxu48-frame-capture-gate.md"
companion_audit: "tests/hourly_20260625_0703_cycle2_keating_tzsevmqxu48_frame_capture_gate_audit.py"
---

# Hourly 20260625 0703 Cycle 2 Keating TzSEvmqxu48 Frame Capture Gate

## 1. Verdict

Verdict: **blocked / frame-level negative at available resolution**.

This run advanced the prior caption-only check to an actual YouTube watch-page
and storyboard acquisition attempt for video id `TzSEvmqxu48`. The strongest
available frame-level object was the YouTube storyboard grid: 69 one-second
source-derived thumbnails for a 68-second video, plus the public `hqdefault`
thumbnail. Those frames show a ship/connection/curvature animation and visible
labels, not a formula sheet or equation-bearing frame.

The run did **not** acquire decoded full-resolution video frames. The watch page
exposed one direct progressive `itag 18` MP4 stream URL, but a local ffmpeg
attempt and a Python requests download attempt both received HTTP 403 from the
media host. Native local tooling also lacked `yt-dlp`, `youtube-dl`, `ffmpeg`,
OpenCV, PyAV, imageio, moviepy, and decord before a temporary ffmpeg dependency
was staged outside the repo. The temporary ffmpeg binary still could not fetch
the stream because the media host denied access.

Decision state:

```text
video_id: TzSEvmqxu48
formula_bearing_frame_found: false
accepted_receipt_count: 0
proof_restart_allowed: false
first_obstruction: full-resolution stream/frame decoding blocked by YouTube
  media-host HTTP 403 and no repo-local accepted formula-bearing frame object
```

## 2. Specific GU Claim/Bridge Under Test

Bridge under test:

```text
Pull That Up Jamie video TzSEvmqxu48
  -> legible Shiab/projection formula-bearing frame or source asset
  -> comparison with manuscript equations 8.1, 8.7, 9.2, 9.3
  -> identity to the missing highest-weight/Bianchi Shiab selector sheet
  -> SourceForcedCodomainSelectorForK_IG receipt review
```

The gate is not testing whether the official page uses the phrase "Shiab
Projection"; it does. The gate tests whether the video/source asset itself
emits a formula-bearing frame or sheet that can be compared to the manuscript
and to the missing highest-weight/Bianchi selector requirement.

## 3. Owned Path And Sources Read First

Owned path:

```text
explorations/hourly-20260625-0703-cycle2-keating-tzsevmqxu48-frame-capture-gate.md
```

Companion audit:

```text
tests/hourly_20260625_0703_cycle2_keating_tzsevmqxu48_frame_capture_gate_audit.py
```

Required sources read first:

| source | use in this decision |
| --- | --- |
| `RESEARCH-POSTURE.md` | Allows constructive source pursuit but forbids locator/caption inflation. |
| `process/runbooks/five-lane-frontier-run.md` | Supplies blocked/conditional verdict discipline and no-proof-restart rules. |
| `explorations/hourly-20260625-0703-cycle1-keating-pullthatupjamie-asset-reacquisition.md` | Supplies prior caption/oEmbed/thumbnail result and the next object name. |
| `explorations/hourly-20260625-0601-cycle3-visual-acquisition-sequencing-gate.md` | Requires capture before transcription, identity, accepted routing, or proof restart. |
| `explorations/hourly-20260625-0601-cycle2-keating-shiab-projection-formula-asset-packet-spec.md` | Defines packet fields and `SourceForcedCodomainSelectorForK_IG` identity requirement. |
| `explorations/hourly-20260625-0502-cycle1-keating-source-surface-receipt-execution.md` | Supplies the missing Keating sheet obstruction and `01:41:43`-`01:42:50` locator. |
| `sources/media-index.md` | Confirms Pull That Up Jamie is a visual pointer and not proof without timestamp/context. |

Additional manuscript-source comparison targets, read-only:

| source | use |
| --- | --- |
| `Geometric_UnityDraftApril1st2021.pdf` equation targets `8.1`, `8.7`, `9.2`, `9.3` | Comparison targets named by prior Keating/IG source-receipt artifacts; no same-cycle worker result is required for this lane's decision. |

## 4. Strongest Positive Construction Attempt

The strongest construction attempt was to move from caption metadata to actual
frame/source acquisition:

| attempt_id | object fetched or tested | exact result | receipt status |
| --- | --- | --- | --- |
| `official_page_embed_caption` | `https://geometricunity.org/pull-that-up-jamie/` | HTTP 200. The page embeds `TzSEvmqxu48` and captions the visual as a "Shiab Projection" operation preserving mast properties when curvature is made into a connection/d-1 form. No formula asset or sheet is exposed in HTML. | not accepted |
| `youtube_oembed_metadata` | YouTube oEmbed for `TzSEvmqxu48` | Confirms title `Geometric Unity for General Relativity & Gauge Theory`, channel `The Portal Clips`, thumbnail URL, and iframe. Metadata only. | not accepted |
| `youtube_watch_player_response` | YouTube watch page `ytInitialPlayerResponse` | HTTP 200. Confirms `videoId=TzSEvmqxu48`, title, author, `lengthSeconds=68`, playability `OK`, zero caption tracks, storyboard metadata present, one progressive 360p format, and adaptive formats. | not accepted |
| `youtube_storyboard_level_2` | Storyboard level 2, 160x90 cells, 69 frames at 1 second interval | Three storyboard sheets fetched with HTTP 200. SHA-256 values: `d71c89fd35ced851ce9865a2c293cc12d3d819982fadf3a0e17daf0a38670249`, `b3a83e3a6b54b40e278858a881b676bc7e5dad0ac73e43c3280f0250da42aee3`, `e0fc9bb0e20fe85238308181ef2757005e53dc88bcfc8c67e1f64bbdeb0c4589`. Visual inspection shows diagram animation only, no formula-bearing frame at this resolution. | not accepted |
| `youtube_hqdefault_thumbnail` | `https://i.ytimg.com/vi/TzSEvmqxu48/hqdefault.jpg` | HTTP 200. SHA-256 `77c16b5134312bb1ad033d2529d0126db61b15cb40e9cba6f3dae07cca227c0e`. Shows "Connections" label, "Shiab Projection" side label, and copyright text, not a formula. | not accepted |
| `direct_mp4_stream_decode` | `itag 18`, `video/mp4`, 640x360, 30 fps, approx 67.5 s | Watch page exposed a direct URL, but ffmpeg read returned `Server returned 403 Forbidden`; Python requests download returned HTTP 403. No decoded full-resolution frame was acquired. | blocked |

Temporary tooling note: a temporary `imageio-ffmpeg` dependency was installed
under the system temp directory only, outside the repo, after native `ffmpeg`
was not found. It did not change the project worktree and did not overcome the
YouTube media-host 403.

The positive result is therefore a bounded negative frame scan: all available
thumbnail/storyboard frames are non-formula visual animation frames. This is
stronger than a caption-only check, but weaker than a full-resolution video
frame audit.

## 5. First Exact Obstruction Or Missing Source Object

First exact obstruction:

```text
No decoded full-resolution frame sequence or formula-bearing source asset for
TzSEvmqxu48 was acquired; direct stream/frame decoding blocked at YouTube media
host HTTP 403 after the watch page exposed stream metadata.
```

The missing source object remains:

```text
LegiblePullThatUpJamieTzSEvmqxu48FormulaFrameOrSourceAsset_V1
```

If the video truly contains a formula, the minimal unblocking artifact is not
another caption. It is one of:

1. an archived/downloaded copy of `TzSEvmqxu48` that can be decoded locally;
2. a stable source frame image at a precise timecode with checksum;
3. the underlying Pull That Up Jamie source asset or animation project file;
4. the original Keating Shiab/projection sheet scan/photo.

Minimum fields needed to unblock acceptance:

```text
video_id
source_url_or_archive_id
capture_method
frame_timecode_or_asset_locator
frame_or_asset_checksum
visible_formula_or_rule_transcription
identity_to_missing_sheet
comparison_to_equations_8_1_8_7_9_2_9_3
highest_weight_bianchi_selector_status
target_data_seen = []
```

## 6. What Would Change If Closed

If a legible formula-bearing frame/source asset were captured, this lane could
move from source acquisition to formula identity review.

The first comparison would be:

| manuscript object | comparison required if a frame is found |
| --- | --- |
| equation `8.1` | Does the frame show the same schematic Shiab contraction family or a selected member of it? |
| equation `8.7` | Does the frame identify invariant basis elements `{Phi_i}` or the representation-theory data used to choose them? |
| equation `9.2` | Does the frame show the typed map `Omega^2(Y^{7,7}, ad) -> Omega^{d-1}(Y^{7,7}, ad)` or a source-equivalent codomain rule? |
| equation `9.3` | Does the frame show the displayed Einstein/Ricci-like Shiab formula or a source-equivalent formula? |
| missing highest-weight/Bianchi sheet | Does the frame supply the missing selector calculation or prove identity to the old sheet discussed in the Keating window? |

Only after those fields were present could the artifact become an accepted
receipt candidate for `SourceForcedCodomainSelectorForK_IG`. Closure would not
itself prove IG, theta/FLRW, dark energy, QFT, DGU/VZ, or RS claims.

## 7. Falsification/Demotion Condition

Demote this route to scoped source-route `fail` if a complete full-resolution
video/frame audit or source-asset audit shows all of:

- every `TzSEvmqxu48` frame is diagram/caption/animation only;
- no frame contains a formula, projection rule, or sheet;
- the official Pull That Up Jamie page exposes no separate source asset with
  the missing formula;
- the manuscript remains the only formula source and still lacks the
  recovered highest-weight/Bianchi selector calculation;
- no identity proof connects manuscript equations `8.1`, `8.7`, `9.2`, `9.3`
  to the missing Keating sheet.

That would falsify only this Pull That Up Jamie frame route. It would not
falsify the existence of Shiab, GU, or a possible IG selector reconstruction
from a different source.

## 8. Next Meaningful Computation/Source Step

Next meaningful step:

```text
Acquire a decodable archive/local copy of TzSEvmqxu48 or the underlying Pull
That Up Jamie source asset, then extract full-resolution frames at 1 fps and
around every visible text transition.
```

Execution details for the next step:

1. Use `yt-dlp` with current YouTube support, browser cookies if permitted, or
   an official archive copy to acquire the 68-second video.
2. Decode frames at 1 fps and at scene/text transitions, preserving timecode,
   checksum, and source URL/archive id.
3. OCR/manual-inspect only frames with legible text or mathematical notation.
4. If a formula-bearing frame appears, compare it against manuscript equations
   `8.1`, `8.7`, `9.2`, `9.3`.
5. Treat the frame as accepted only if it also supplies identity fields for the
   missing highest-weight/Bianchi sheet or `SourceForcedCodomainSelectorForK_IG`.

Until then:

```text
formula_bearing_frame_found = false
accepted_receipt_count = 0
proof_restart_allowed = false
```

## 9. JSON Summary

```json
{
  "artifact": "FrameLevelPullThatUpJamieTzSEvmqxu48FormulaCaptureAndManuscriptIdentityCheck_V1",
  "run_id": "hourly-20260625-0703",
  "cycle": 2,
  "lane": 2,
  "artifact_id": "FrameLevelPullThatUpJamieTzSEvmqxu48FormulaCaptureAndManuscriptIdentityCheck_V1",
  "verdict": "BLOCKED_FRAME_STREAM_DECODE_STORYBOARD_NEGATIVE_ZERO_ACCEPTED_RECEIPTS",
  "video_id": "TzSEvmqxu48",
  "capture_attempts": [
    {
      "attempt_id": "official_page_embed_caption",
      "source": "https://geometricunity.org/pull-that-up-jamie/",
      "method": "requests_get_html",
      "status": "http_200_embed_and_caption_no_formula_asset",
      "formula_bearing_frame_or_asset": false,
      "accepted_receipt": false
    },
    {
      "attempt_id": "youtube_oembed_metadata",
      "source": "https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v=TzSEvmqxu48&format=json",
      "method": "curl_get_json",
      "status": "metadata_thumbnail_iframe_only",
      "formula_bearing_frame_or_asset": false,
      "accepted_receipt": false
    },
    {
      "attempt_id": "youtube_watch_player_response",
      "source": "https://www.youtube.com/watch?v=TzSEvmqxu48",
      "method": "requests_get_parse_ytInitialPlayerResponse",
      "status": "playability_ok_length_68_seconds_zero_caption_tracks_storyboard_present_streamingData_present",
      "formula_bearing_frame_or_asset": false,
      "accepted_receipt": false
    },
    {
      "attempt_id": "youtube_storyboard_level_2",
      "source": "https://i.ytimg.com/sb/TzSEvmqxu48/storyboard3_L2/M*.jpg",
      "method": "requests_get_storyboard_rs_token_visual_inspection",
      "status": "69_one_second_storyboard_frames_acquired_no_formula_visible_at_160x90",
      "sheet_sha256": [
        "d71c89fd35ced851ce9865a2c293cc12d3d819982fadf3a0e17daf0a38670249",
        "b3a83e3a6b54b40e278858a881b676bc7e5dad0ac73e43c3280f0250da42aee3",
        "e0fc9bb0e20fe85238308181ef2757005e53dc88bcfc8c67e1f64bbdeb0c4589"
      ],
      "formula_bearing_frame_or_asset": false,
      "accepted_receipt": false
    },
    {
      "attempt_id": "youtube_hqdefault_thumbnail",
      "source": "https://i.ytimg.com/vi/TzSEvmqxu48/hqdefault.jpg",
      "method": "curl_download_visual_inspection",
      "status": "thumbnail_acquired_connections_visual_no_formula",
      "sha256": "77c16b5134312bb1ad033d2529d0126db61b15cb40e9cba6f3dae07cca227c0e",
      "formula_bearing_frame_or_asset": false,
      "accepted_receipt": false
    },
    {
      "attempt_id": "direct_mp4_stream_decode",
      "source": "youtube_watch_player_response_itag_18_url",
      "method": "temporary_imageio_ffmpeg_and_python_requests",
      "status": "blocked_http_403_forbidden_from_youtube_media_host_no_decoded_frames",
      "format": "video/mp4; codecs=\"avc1.42001E, mp4a.40.2\"; 640x360; 30fps; approx_67_5s",
      "formula_bearing_frame_or_asset": false,
      "accepted_receipt": false
    }
  ],
  "formula_bearing_frame_found": false,
  "accepted_receipt_count": 0,
  "accepted_receipts": [],
  "proof_restart_allowed": false,
  "first_obstruction": "Full-resolution frame decoding for TzSEvmqxu48 is blocked by YouTube media-host HTTP 403 after watch-page stream metadata exposure; available storyboard and thumbnail frames show no formula-bearing frame or source asset.",
  "next_frontier_object": "DecodableTzSEvmqxu48ArchiveOrSourceAssetWithFormulaFrameAudit_V1",
  "companion_audit": "tests/hourly_20260625_0703_cycle2_keating_tzsevmqxu48_frame_capture_gate_audit.py",
  "manuscript_comparison": {
    "equations_checked_if_frame_found": ["8.1", "8.7", "9.2", "9.3"],
    "frame_formula_available_for_comparison": false,
    "highest_weight_bianchi_sheet_requirement": "missing_recovered_selector_calculation_or_identity_to_old_keating_sheet",
    "identity_fields_present": false,
    "identity_to_SourceForcedCodomainSelectorForK_IG": false
  },
  "minimal_unblocking_artifact": "Decodable archive/local copy of TzSEvmqxu48 or Pull That Up Jamie source asset with stable URL/archive id, frame timecode, checksum, visible formula transcription, and identity fields tying the formula to manuscript equations 8.1, 8.7, 9.2, 9.3 and the missing highest-weight/Bianchi selector sheet.",
  "target_import_guard": {
    "target_data_seen": [],
    "target_import_clean": true,
    "target_import_clean_sufficient_for_acceptance": false
  }
}
```
