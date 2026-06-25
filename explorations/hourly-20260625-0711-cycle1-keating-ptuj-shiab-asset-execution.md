---
title: "Hourly 20260625 0711 Cycle 1 Keating PTUJ Shiab Asset Execution"
date: "2026-06-25"
run_id: "hourly-20260625-0711"
cycle: 1
lane: 2
doc_type: keating_ptuj_shiab_asset_execution
artifact_id: "KeatingPullThatUpJamieShiabProjectionFormulaAssetPacketExecution_0711_V1"
verdict: "BLOCKED_SOURCE_SURFACES_RECHECKED_NO_FORMULA_ASSET_CAPTURED"
owned_path: "explorations/hourly-20260625-0711-cycle1-keating-ptuj-shiab-asset-execution.md"
companion_audit: "tests/hourly_20260625_0711_cycle1_keating_ptuj_shiab_asset_execution_audit.py"
---

# Hourly 20260625 0711 Cycle 1 Keating PTUJ Shiab Asset Execution

## 1. Verdict

Verdict: **blocked**.

This lane executed the Keating/Pull That Up Jamie Shiab Projection formula-asset
acquisition gate as far as the repo-local and live-source tooling permitted in
this run. It did not acquire an accepted formula asset, frame packet, sheet scan,
or manuscript-equivalence proof.

Decision state:

```text
artifact: KeatingPullThatUpJamieShiabProjectionFormulaAssetPacketExecution_0711_V1
target_packet: KeatingPullThatUpJamieShiabProjectionFormulaAssetPacket_V1
pull_that_up_jamie_asset: PullThatUpJamie_GUForGRGaugeTheory_TzSEvmqxu48
keating_window: 01:41:43-01:42:50
accepted_receipt_count: 0
accepted_for_routing_count: 0
formula_sheet_frame_captured: false
target_import_clean: true
family_identity_checks_passed: 0
SourceForcedCodomainSelectorForK_IG_accepted: false
proof_restart_allowed: false
```

The source surfaces remain acquisition-positive but receipt-negative. The
official Pull That Up Jamie page names the Shiab Projection entry and the
`TzSEvmqxu48` video identity is confirmed by YouTube oEmbed metadata. The
Keating transcript window explicitly points to the missing representation-theory
projection sheet. Neither surface emits a source-visible formula/projection
rule in the text or metadata available to this run.

## 2. What Was Derived Directly From Repo/Source Surfaces

`RESEARCH-POSTURE.md` permits aggressive acquisition of high-value missing
objects, but forbids turning compatibility, public framing, or target agreement
into proof evidence.

`process/runbooks/five-lane-frontier-run.md` and
`process/runbooks/three-cycle-fifteen-hole-run.md` require a decision-grade
artifact with the first exact obstruction and no proof restart from locator-only
evidence.

The 0601 synthesis fixes the current frontier:

```text
accepted_receipt_count = 0
proof_restart_allowed = false
KeatingPullThatUpJamieShiabProjectionFormulaAssetPacket_V1 is a next frontier object
```

The 0601 Keating packet spec defines the acceptance target. A successful packet
must contain source provenance, exact locator, visual/sheet/asset capture,
formula or rule transcription, target-import cleanliness, identity to the
missing sheet or source-proven equivalent, and family identity to
`SourceForcedCodomainSelectorForK_IG`.

`sources/media-index.md` supplies the relevant source IDs:

| source_id | repo role | 0711 state |
| --- | --- | --- |
| `GU-POD-2021-KEATING-REVEALED-1` | Keating Revealed source surface | source window remains a missing-sheet locator |
| `GU-POD-2021-KEATING-REVEALED-2` | paired Keating Revealed source surface | same source-family locator state |
| `GU-MEDIA-2021-PULL-THAT-UP-JAMIE` | official visual support page | caption/metadata source surface rechecked |
| `GU-MEDIA-2021-DRAFT-RELEASE` | acquired author manuscript | adjacent formula candidate only; identity not proved |

Live source-surface state checked in this lane:

| attempt_id | retrieval | result | receipt status |
| --- | --- | --- | --- |
| `PTUJ_PAGE_OPEN_0711` | `https://geometricunity.org/pull-that-up-jamie/` | reachable; page says the videos are visual aids; the `Geometric Unity for General Relativity & Gauge Theory` entry states a Shiab Projection operation in caption prose | locator/caption only; not accepted |
| `PTUJ_HTML_SCAN_0711` | `Invoke-WebRequest` over the same page; searched for `TzSEvmqxu48`, `youtube`, `mp4`, `webm`, `iframe`, `Shiab Projection` | HTML exposes `iframe`, `youtube`, `TzSEvmqxu48`, and `Shiab Projection`; no direct `mp4`/`webm` or formula-bearing source asset was exposed by the search | embed metadata only; not accepted |
| `YOUTUBE_OEMBED_0711` | `https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v=TzSEvmqxu48&format=json` | reachable JSON confirms title `Geometric Unity for General Relativity & Gauge Theory`, author `The Portal Clips`, embed URL, and thumbnail URL | metadata only; not accepted |
| `YOUTUBE_WATCH_ATTEMPT_0711` | `https://www.youtube.com/watch?v=TzSEvmqxu48` via `Invoke-WebRequest` | request timed out after 60 seconds in local tooling | first stream/frame acquisition obstruction |
| `YTDLP_CHECK_0711` | `python -m yt_dlp --version` | local Python reports `No module named yt_dlp` | no local video frame extractor available |
| `KEATING_TRANSCRIPT_OPEN_0711` | `https://theportal.group/into-the-impossible-eric-weinstein-geometric-unity-revealed/` | reachable transcript; the `01:41:43`-`01:42:50` window says the Shiab operator exists in general but the favored representation-theory projection calculations are on a paper sheet he has not found | positive missing-sheet locator; not accepted |
| `MANUSCRIPT_CONTEXT_0711` | 0601 author-manuscript identity packet plus local `Geometric_UnityDraftApril1st2021.pdf` presence | repo has acquired manuscript object and adjacent pages 41-44 formula surface; the 0601 identity packet says the selector/rival-eliminator object is missing | quarantined manuscript candidate; not accepted |

The live web references used for this artifact were:

- Pull That Up Jamie page: `https://geometricunity.org/pull-that-up-jamie/`.
- YouTube oEmbed endpoint for `TzSEvmqxu48`.
- The Portal Group Keating Revealed transcript:
  `https://theportal.group/into-the-impossible-eric-weinstein-geometric-unity-revealed/`.

## 3. Strongest Positive Acquisition/Identity Attempt

The strongest positive attempt is still a three-surface identity triangle:

| surface | positive acquisition/identity fact | why it remains insufficient |
| --- | --- | --- |
| Pull That Up Jamie official page | The page is official for GU visual aids and contains the `Geometric Unity for General Relativity & Gauge Theory` caption saying the GR/gauge-theory incompatibility is addressed by creating a Shiab Projection operation. The local HTML scan found `TzSEvmqxu48` and an iframe. | Caption prose and iframe identity do not expose a formula, projection rule, frame checksum, or source asset package. |
| YouTube oEmbed for `TzSEvmqxu48` | oEmbed confirms the title, channel, iframe embed URL, and thumbnail URL for `PullThatUpJamie_GUForGRGaugeTheory_TzSEvmqxu48`. | oEmbed is metadata. It does not provide video frames, subtitles, a transcript, or a formula-bearing image. |
| Keating Revealed transcript window | The `01:41:43`-`01:42:50` transcript window names the Shiab operator, representation-theory calculations, projections, yellow highlighter, and perforated printer-paper sheet. | The transcript says the sheet has not been found; it is direct evidence of the missing object, not the object. |
| Author manuscript pages 41-44 | The repo has already recorded a strong typed Shiab candidate and operator-choice vicinity in the acquired 2021 manuscript. | The 0601 identity packet blocks because the representation-theory/Bianchi selector and rival eliminators are not source-emitted. |

This is the strongest possible source-clean attempt from the surfaces available
in this run. It establishes that the `TzSEvmqxu48` object identity is real and
that the official caption names Shiab Projection. It does not establish
`SourceForcedCodomainSelectorForK_IG`, because there is no captured formula/rule
and no identity proof to the missing Keating sheet.

Receipt rows after execution:

| candidate_receipt_id | source_surface | asset_or_locator | formula_or_rule_transcribed | accepted_for_routing | status_reason |
| --- | --- | --- | --- | --- | --- |
| `PTUJ_TzSEvmqxu48_OfficialCaptionMetadata_0711` | `GU-MEDIA-2021-PULL-THAT-UP-JAMIE` | page caption, iframe/video id, oEmbed metadata | false | false | caption/metadata only |
| `KeatingRevealed_014143_014250_MissingSheetLocator_0711` | `GU-POD-2021-KEATING-REVEALED-1/2` | transcript window | false | false | transcript points to missing sheet |
| `AuthorManuscriptPages41To44_AdjacentShiabCandidate_0711` | `GU-MEDIA-2021-DRAFT-RELEASE` | acquired manuscript candidate from prior packets | true, as adjacent generic Shiab candidate | false | identity to missing sheet and `SourceForcedCodomainSelectorForK_IG` not proved |

## 4. First Exact Obstruction or Missing Object

The first exact obstruction in this execution is:

```text
No lawful/local retrieval path in this run produced a formula-bearing frame,
sheet scan/photo, source asset package, or manuscript-equivalence proof for
KeatingPullThatUpJamieShiabProjectionFormulaAssetPacket_V1.
```

The first operational obstruction was:

```text
YOUTUBE_WATCH_ATTEMPT_0711 timed out after 60 seconds, and yt_dlp is not
available locally, so the run could not extract or inspect frame sequences from
TzSEvmqxu48.
```

The first mathematical/source obstruction remains:

```text
KeatingRevealed_ShiabProjectionSheet_V1 is missing, and no inspected source
object identifies the caption/metadata/manuscript candidate with
SourceForcedCodomainSelectorForK_IG.
```

The obstruction is not target-import contamination. This run did not use DESI,
dark-energy, FLRW, QFT, generation-count, or other target-facing outcomes to
select the source object. The obstruction is missing source capture plus missing
family identity.

## 5. Impact If Closed

If a later run closes this gate, the immediate impact is one source-receipt
candidate for IG selector review, not a downstream proof.

Closure would require:

| required field | closure condition |
| --- | --- |
| `visual_or_sheet_or_asset_capture` | source-stable frame sequence, original animation asset, or sheet scan/photo with checksum/archive id |
| `formula_or_rule_transcription` | exact visible formula/projection/rule text with uncertainty marked |
| `identity_to_missing_sheet` | proof that the captured object is the Keating sheet or a source-proven equivalent |
| `target_import_clean` | no target-facing physics used for source selection, normalization, or branch choice |
| `family_identity_check` | explicit identity or non-identity to `SourceForcedCodomainSelectorForK_IG` |

Only after those fields pass could IG selector identity review begin. Even then,
theta/FLRW, dark-energy, QFT extraction, DGU/VZ, RS, or prediction claims would
remain untouched until a separate proof-restart gate passes.

## 6. Falsification/Demotion Condition

Demote this route from blocked acquisition to scoped source-route fail if a
complete frame/source retrieval pass establishes all of the following:

- `KeatingRevealed_ShiabProjectionSheet_V1` remains unrecovered.
- `TzSEvmqxu48` contains no formula, projection rule, sheet view, or source text
  beyond animation/caption material.
- No source asset linked from the Pull That Up Jamie page contains legible
  Shiab/projection formula data.
- The author manuscript remains only an adjacent typed Shiab candidate and
  cannot supply representation-theory/Bianchi rival eliminators.
- Any bridge to `SourceForcedCodomainSelectorForK_IG` requires target-imported
  physical outcomes or reconstruction preference.

That demotion would be local to the Keating/Pull That Up Jamie route. It would
not be a global GU no-go.

## 7. Next Meaningful Acquisition/Computation Step

The next meaningful step is:

```text
FrameLevelPullThatUpJamieTzSEvmqxu48FormulaCaptureAndManuscriptIdentityCheck_V1
```

Concrete next action:

1. Use a lawful video acquisition path with `yt-dlp` or an equivalent approved
   local extractor to fetch `TzSEvmqxu48` metadata and frame thumbnails without
   modifying shared repo paths.
2. Extract frames around any text-bearing moments and compute checksums for
   candidate formula frames.
3. OCR/manual-transcribe only visible source text and mark illegible portions.
4. Compare any formula-bearing frame to the author manuscript pages 41-44
   Shiab formulas and to the Keating missing-sheet description.
5. Run `ManuscriptShiabProjectionIdentityCheck_V1` only after a formula-bearing
   source object exists.

Until then, `proof_restart_allowed` remains `false`.

## 8. Machine-readable JSON summary

```json
{
  "artifact": "KeatingPullThatUpJamieShiabProjectionFormulaAssetPacketExecution_0711_V1",
  "version": "2026-06-25",
  "run_id": "hourly-20260625-0711",
  "cycle": 1,
  "lane": 2,
  "verdict": "BLOCKED_SOURCE_SURFACES_RECHECKED_NO_FORMULA_ASSET_CAPTURED",
  "verdict_class": "blocked",
  "target_packet": "KeatingPullThatUpJamieShiabProjectionFormulaAssetPacket_V1",
  "required_object": "SourceForcedCodomainSelectorForK_IG",
  "object_ids": {
    "execution_artifact_id": "KeatingPullThatUpJamieShiabProjectionFormulaAssetPacketExecution_0711_V1",
    "target_packet_id": "KeatingPullThatUpJamieShiabProjectionFormulaAssetPacket_V1",
    "pull_that_up_jamie_asset_id": "PullThatUpJamie_GUForGRGaugeTheory_TzSEvmqxu48",
    "missing_sheet_id": "KeatingRevealed_ShiabProjectionSheet_V1",
    "manuscript_candidate_id": "ManuscriptShiabOperatorFormulaCandidate_V1",
    "manuscript_identity_check_id": "ManuscriptShiabProjectionIdentityCheck_V1",
    "next_frontier_object": "FrameLevelPullThatUpJamieTzSEvmqxu48FormulaCaptureAndManuscriptIdentityCheck_V1"
  },
  "required_source_surfaces": [
    "GU-POD-2021-KEATING-REVEALED-1",
    "GU-POD-2021-KEATING-REVEALED-2",
    "GU-MEDIA-2021-PULL-THAT-UP-JAMIE",
    "GU-MEDIA-2021-DRAFT-RELEASE"
  ],
  "source_surfaces": [
    {
      "surface_id": "KeatingRevealedTranscriptWindow",
      "source_ids": [
        "GU-POD-2021-KEATING-REVEALED-1",
        "GU-POD-2021-KEATING-REVEALED-2"
      ],
      "source_url": "https://theportal.group/into-the-impossible-eric-weinstein-geometric-unity-revealed/",
      "locator": "01:41:43-01:42:50",
      "retrieval_status": "reachable_transcript_window",
      "receipt_status": "locator_only_missing_sheet",
      "formula_or_rule_transcribed": false,
      "accepted_for_routing": false
    },
    {
      "surface_id": "PullThatUpJamie_GUForGRGaugeTheory_TzSEvmqxu48",
      "source_ids": [
        "GU-MEDIA-2021-PULL-THAT-UP-JAMIE"
      ],
      "source_url": "https://geometricunity.org/pull-that-up-jamie/",
      "video_id": "TzSEvmqxu48",
      "oembed_url": "https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v=TzSEvmqxu48&format=json",
      "retrieval_status": "page_and_oembed_reachable_html_exposes_iframe_video_id_caption",
      "receipt_status": "caption_metadata_only",
      "formula_or_rule_transcribed": false,
      "accepted_for_routing": false
    },
    {
      "surface_id": "AuthorManuscriptPages41To44",
      "source_ids": [
        "GU-MEDIA-2021-DRAFT-RELEASE"
      ],
      "local_object": "Geometric_UnityDraftApril1st2021.pdf",
      "retrieval_status": "local_pdf_present_prior_identity_packet_read",
      "receipt_status": "quarantined_adjacent_formula_candidate",
      "formula_or_rule_transcribed": true,
      "identity_to_missing_sheet_proved": false,
      "accepted_for_routing": false
    }
  ],
  "retrieval_attempts": [
    {
      "attempt_id": "PTUJ_PAGE_OPEN_0711",
      "surface_id": "PullThatUpJamie_GUForGRGaugeTheory_TzSEvmqxu48",
      "method": "web_open",
      "result": "reachable_caption_surface",
      "accepted_receipt": false
    },
    {
      "attempt_id": "PTUJ_HTML_SCAN_0711",
      "surface_id": "PullThatUpJamie_GUForGRGaugeTheory_TzSEvmqxu48",
      "method": "Invoke-WebRequest_html_pattern_scan",
      "result": "found_iframe_youtube_TzSEvmqxu48_Shiab_Projection_no_direct_video_asset",
      "accepted_receipt": false
    },
    {
      "attempt_id": "YOUTUBE_OEMBED_0711",
      "surface_id": "PullThatUpJamie_GUForGRGaugeTheory_TzSEvmqxu48",
      "method": "oembed_json",
      "result": "reachable_metadata_thumbnail_embed_only",
      "accepted_receipt": false
    },
    {
      "attempt_id": "YOUTUBE_WATCH_ATTEMPT_0711",
      "surface_id": "PullThatUpJamie_GUForGRGaugeTheory_TzSEvmqxu48",
      "method": "Invoke-WebRequest_watch_page",
      "result": "timed_out_after_60_seconds",
      "accepted_receipt": false
    },
    {
      "attempt_id": "YTDLP_CHECK_0711",
      "surface_id": "PullThatUpJamie_GUForGRGaugeTheory_TzSEvmqxu48",
      "method": "python_module_check",
      "result": "yt_dlp_not_installed",
      "accepted_receipt": false
    },
    {
      "attempt_id": "KEATING_TRANSCRIPT_OPEN_0711",
      "surface_id": "KeatingRevealedTranscriptWindow",
      "method": "web_open",
      "result": "reachable_missing_sheet_locator",
      "accepted_receipt": false
    }
  ],
  "receipt_state": {
    "accepted_receipt_count": 0,
    "accepted_for_routing_count": 0,
    "accepted_receipts": [],
    "quarantined_candidate_receipt_count": 3,
    "formula_sheet_frame_captured": false,
    "family_identity_checks_passed": 0,
    "SourceForcedCodomainSelectorForK_IG_accepted": false,
    "proof_restart_allowed": false,
    "claim_promotion_allowed": false
  },
  "target_import_guard": {
    "target_data_seen": [],
    "target_import_clean": true,
    "target_import_clean_sufficient_for_acceptance": false,
    "target_outcome_used_to_select_or_normalize_source_object": false
  },
  "first_exact_obstruction": {
    "id": "NoFormulaBearingFrameSheetAssetOrEquivalenceProof_0711",
    "operational_obstruction": "YOUTUBE_WATCH_ATTEMPT_0711 timed out after 60 seconds and yt_dlp is not available locally, so this run could not extract or inspect frame sequences from TzSEvmqxu48.",
    "source_obstruction": "KeatingRevealed_ShiabProjectionSheet_V1 remains missing, and no inspected source object identifies the caption/metadata/manuscript candidate with SourceForcedCodomainSelectorForK_IG.",
    "missing_objects": [
      "KeatingRevealed_ShiabProjectionSheet_V1",
      "legible_TzSEvmqxu48_formula_frame_sequence",
      "source_asset_package_with_formula_or_projection_rule",
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
    "KeatingRevealed_ShiabProjectionSheet_V1_remains_unrecovered_after_complete_source_search",
    "TzSEvmqxu48_contains_no_formula_projection_rule_sheet_view_or_source_text",
    "PullThatUpJamie_page_links_no_formula_bearing_source_asset",
    "manuscript_pages_41_44_cannot_supply_representation_theory_Bianchi_rival_eliminators",
    "bridge_to_SourceForcedCodomainSelectorForK_IG_requires_target_import"
  ],
  "next_meaningful_acquisition_or_computation_step": "FrameLevelPullThatUpJamieTzSEvmqxu48FormulaCaptureAndManuscriptIdentityCheck_V1: install/use a lawful local video extractor, capture text-bearing frames with checksums, transcribe only visible source text, and compare any formula-bearing frame to manuscript pages 41-44 before family identity review.",
  "forbidden_promotions": {
    "SourceForcedCodomainSelectorForK_IG_accepted": false,
    "Keating_or_PullThatUpJamie_selects_K_IG": false,
    "PullThatUpJamie_visual_proves_projection_rule": false,
    "manuscript_formula_identical_to_missing_sheet": false,
    "family_identity_passed": false,
    "proof_restart": false,
    "downstream_physics_claim": false
  }
}
```
