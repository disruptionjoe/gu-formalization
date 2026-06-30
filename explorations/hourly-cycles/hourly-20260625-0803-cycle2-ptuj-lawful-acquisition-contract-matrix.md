---
title: "Hourly 20260625 0803 Cycle 2 PTUJ Lawful Acquisition Contract Matrix"
date: "2026-06-25"
run_id: "hourly-20260625-0803"
cycle: 2
lane: 1
doc_type: ptuj_lawful_acquisition_contract_matrix
artifact_id: "LawfulLocalTzSEvmqxu48FrameExtractorOrSourceAsset_V1"
verdict: "BLOCKED_CONTRACT_DEFINED_NO_ACCEPTABLE_PATH_PRESENT"
owned_path: "explorations/hourly-20260625-0803-cycle2-ptuj-lawful-acquisition-contract-matrix.md"
companion_audit: "tests/hourly_20260625_0803_cycle2_ptuj_lawful_acquisition_contract_matrix_audit.py"
---

# Hourly 20260625 0803 Cycle 2 PTUJ Lawful Acquisition Contract Matrix

## 1. Verdict.

Verdict: **blocked**.

This lane consumes the cycle-1 blocker by defining the exact acceptance contract
for:

```text
LawfulLocalTzSEvmqxu48FrameExtractorOrSourceAsset_V1
```

The repo has no acceptable path today. It has a source identity, official page
locator, oEmbed/watch/thumbnail metadata from prior runs, Keating missing-sheet
locator evidence, adjacent manuscript candidate material, and prior
low-resolution storyboard negative evidence. It does not have either admitted
contract branch:

```text
1. LawfulLocalTzSEvmqxu48FrameExtractor_V1
2. OfficialTzSEvmqxu48FormulaSourceAssetPacket_V1
```

Decision state:

```text
accepted_source_asset_count: 0
accepted_formula_receipt_count: 0
accepted_frame_packet_count: 0
accepted_receipt_count: 0
proof_restart_allowed: false
claim_promotion_allowed: false
```

No source reachability check is repeated here. The cycle-1 and 0711 artifacts
already provide the live/tool/source state. This artifact is the acquisition
contract and matrix for deciding when PTUJ metadata can be converted into a
formula-bearing source asset packet.

## 2. Specific GU claim or bridge under test.

Bridge under test:

```text
Pull That Up Jamie official visual-aid entry / YouTube id TzSEvmqxu48
  -> lawful local extractor or fallback official formula source asset
  -> formula-bearing frame/source asset packet
  -> identity to KeatingRevealed_ShiabProjectionSheet_V1 or source equivalent
  -> possible review against SourceForcedCodomainSelectorForK_IG
```

This bridge is not testing whether the official PTUJ caption names Shiab
Projection. Prior artifacts already establish that source-locator fact. This
bridge tests whether the repo can admit a source-clean, formula-bearing object
strong enough to start the selector-family identity review.

## 3. Sources read first.

Required sources read first:

| source | role in this contract |
| --- | --- |
| `RESEARCH-POSTURE.md` | Supplies the Mission A posture and forbids promotion from compatibility, metadata, or target agreement. |
| `process/runbooks/five-lane-frontier-run.md` | Supplies verdict vocabulary and decision-grade lane expectations. |
| `explorations/hourly-20260625-0803-cycle1-ptuj-lawful-source-asset-admission-gate.md` | Supplies the immediate blocker: no lawful local extractor or formula-bearing source asset. |
| `explorations/hourly-20260625-0711-cycle1-keating-ptuj-shiab-asset-execution.md` | Supplies the PTUJ/Keating source identity triangle and zero-receipt state. |
| `explorations/hourly-20260625-0711-cycle2-ptuj-frame-capture-feasibility-gate.md` | Supplies the missing local extraction stack and no direct official mp4/webm/source asset finding. |
| `sources/media-index.md` | Supplies the relevant source ids and media-use discipline. |

## 4. Strongest positive construction/contract.

The strongest positive construction is a two-branch admission contract:

```text
LawfulLocalTzSEvmqxu48FrameExtractorOrSourceAsset_V1
  = LawfulLocalTzSEvmqxu48FrameExtractor_V1
    OR OfficialTzSEvmqxu48FormulaSourceAssetPacket_V1
```

Branch A, local extractor contract:

| field | required acceptance content |
| --- | --- |
| `contract_branch` | `lawful_local_extractor`. |
| `lawful_basis` | Source URL or archive/custodian basis already tied to `GU-MEDIA-2021-PULL-THAT-UP-JAMIE`; no target-facing physics used to select the asset. |
| `input_locator` | `TzSEvmqxu48`, watch/embed/source URL, and exact official page/source id. |
| `toolchain_identity` | Executable/module names, versions, install/source provenance, and command lines for acquisition and frame extraction. |
| `decode_scope` | Time interval or complete asset scope, sampling plan, and any text/scene-transition oversampling rule. |
| `output_manifest` | Frame filenames, timecodes, dimensions, file sizes, checksums, and extraction command for each frame/source segment. |
| `formula_visibility_evidence` | Visible formula/projection-rule/sheet text transcribed from frame pixels, or a complete formula-negative frame/source audit. |
| `target_import_guard` | Explicit statement that no DESI, dark-energy, QFT, generation-count, or reconstruction target outcome selected or normalized the source object. |

Branch B, fallback official source-asset contract:

| field | required acceptance content |
| --- | --- |
| `contract_branch` | `official_source_asset`. |
| `custodian_or_source_surface` | Official PTUJ page, official archive, original animation/source package, sheet scan/photo package, or source-custodian delivery record. |
| `asset_locator` | Stable URL/archive id/file id/package id plus source id, preferably `GU-MEDIA-2021-PULL-THAT-UP-JAMIE` or a cited official successor. |
| `provenance_chain` | Who/what supplied the asset, acquisition date, relation to `TzSEvmqxu48`, and any license/access note sufficient for repo-local use. |
| `asset_manifest` | File names, media types, dimensions/pages/duration when applicable, checksums, and package structure. |
| `formula_visibility_evidence` | Legible formula/projection-rule/sheet content or a complete formula-negative inspection over the delivered asset. |
| `identity_basis` | If not literally a video frame, the source-emitted basis for treating the object as the PTUJ visual aid, original animation, Keating sheet, or source-proven equivalent. |
| `target_import_guard` | Same target-import guard as Branch A. |

Accepted conversion target:

```text
TzSEvmqxu48_FormulaBearingFrameOrSourceAssetPacket_V1
```

Minimum fields for that packet:

| packet field | required content |
| --- | --- |
| `source_asset_branch` | `lawful_local_extractor` or `official_source_asset`. |
| `source_ids` | Must include the controlling source ids from `sources/media-index.md`. |
| `input_asset_manifest` | Source/video/package identity plus checksums or stable archive identifiers. |
| `formula_asset_manifest` | Frame/page/sheet/image files, dimensions, checksums, and locators. |
| `formula_or_rule_transcription` | Exact visible text/formula/rule transcription with illegible parts marked. |
| `visibility_status` | `formula_bearing`, `formula_negative_complete_audit`, or `insufficient_resolution`; metadata-only is not allowed. |
| `identity_to_missing_sheet_or_equivalent` | Pass/fail/blocked comparison to `KeatingRevealed_ShiabProjectionSheet_V1` or source-proven equivalent. |
| `selector_family_review_state` | Not started until a formula-bearing object exists; no implicit pass from captions or metadata. |

## 5. Field-by-field acquisition matrix.

| required field | current repo state | accepted today? | missing content needed |
| --- | --- | --- | --- |
| `target_video_id` | `TzSEvmqxu48` is identified by prior PTUJ artifacts and media-index context. | yes, locator only | Nothing for locator identity. |
| `source_ids` | `GU-MEDIA-2021-PULL-THAT-UP-JAMIE`, `GU-POD-2021-KEATING-REVEALED-1`, `GU-POD-2021-KEATING-REVEALED-2`, `GU-MEDIA-2021-DRAFT-RELEASE`. | yes, provenance map only | Nothing for source indexing. |
| `lawful_basis` | Official page/source locators exist. | no | A lawful local extractor basis or official/custodian asset package with provenance. |
| `toolchain_identity` | Cycle-1 records Python present but no admitted `yt_dlp`, `yt-dlp`, `youtube-dl`, or `ffmpeg`. | no | Exact tools/modules, versions, commands, and acquisition/extraction provenance. |
| `direct_source_asset` | Prior artifacts found no direct official mp4/webm/source package exposed by the page. | no | Official archive/package/sheet/photo/source asset with manifest and checksums. |
| `source_asset_checksums` | No accepted source video/source package checksums. | no | Checksums for video bytes, source package, image frames, or official delivered files. |
| `frame_or_asset_manifest` | Prior storyboard/thumbnail metadata exists, but not accepted as a source asset packet. | no | Frame/page/sheet files with timecodes/locators, dimensions, sizes, checksums. |
| `formula_visibility_evidence` | Captions/metadata name Shiab Projection; no admitted formula-bearing frame/source asset. | no | Legible pixel/page/sheet formula or explicit complete formula-negative audit. |
| `KeatingRevealed_ShiabProjectionSheet_V1` | Keating transcript points to the missing sheet, but the sheet is unrecovered. | no | Sheet scan/photo or source-proven equivalent with identity basis. |
| `manuscript_identity_to_selector` | Manuscript pages 41-44 are adjacent candidates only. | no | Source-emitted identity or comparison proof to `SourceForcedCodomainSelectorForK_IG`. |
| `target_import_guard` | Prior artifacts report target import clean. | yes, necessary only | Still insufficient without source asset/formula packet. |
| `accepted_receipt_count` | `0`. | yes, zero state | Remains zero until a contract branch is actually satisfied. |
| `proof_restart_allowed` | `false`. | yes, blocked state | Turns true only after formula packet plus selector-family identity gate, not at acquisition alone. |

Explicit non-acceptance matrix:

| object type | current use | accepted as formula receipt? | reason |
| --- | --- | --- | --- |
| PTUJ caption text | Locator/terminology. | no | Caption is not formula pixels/source bytes. |
| YouTube oEmbed JSON | Video identity metadata. | no | Metadata is not a frame/source asset. |
| YouTube watch-page reachability | Addressability. | no | HTML reachability is not video/frame acquisition. |
| YouTube thumbnail | Preview/metadata. | no | Thumbnail is not an accepted formula-bearing packet. |
| Low-resolution storyboard frames | Prior bounded negative at preview resolution. | no | Formula-negative at low resolution and not full source decode. |
| Keating transcript window | Missing-sheet locator. | no | It identifies the missing object but does not supply it. |
| Manuscript pages 41-44 | Adjacent Shiab candidate. | no | Identity to missing sheet and selector family is not proved. |

## 6. First exact obstruction or missing object.

The first exact obstruction is the absence of either admitted branch of:

```text
LawfulLocalTzSEvmqxu48FrameExtractorOrSourceAsset_V1
```

Exact missing object names:

```text
LawfulLocalTzSEvmqxu48FrameExtractor_V1
OfficialTzSEvmqxu48FormulaSourceAssetPacket_V1
TzSEvmqxu48_FormulaBearingFrameOrSourceAssetPacket_V1
KeatingRevealed_ShiabProjectionSheet_V1
manuscript_equivalence_proof_to_SourceForcedCodomainSelectorForK_IG
```

The first missing field class is not a better caption interpretation. It is a
source-bearing artifact with provenance, manifest, checksums, and visible
formula/projection-rule evidence or a complete formula-negative audit.

## 7. Impact if closed.

If either branch of the contract closes, the route advances from acquisition
gating to source-packet inspection.

| closure object | immediate impact | what it still would not prove |
| --- | --- | --- |
| `LawfulLocalTzSEvmqxu48FrameExtractor_V1` | Enables deterministic local frame extraction and checksummed frame manifests for `TzSEvmqxu48`. | Does not itself create a formula receipt. |
| `OfficialTzSEvmqxu48FormulaSourceAssetPacket_V1` | Enables source-stable inspection without relying on live playback. | Does not itself identify the object with `SourceForcedCodomainSelectorForK_IG`. |
| `TzSEvmqxu48_FormulaBearingFrameOrSourceAssetPacket_V1` | Creates a candidate formula-bearing source packet. | Does not itself prove downstream IG, theta/FLRW, dark-energy, QFT, DGU/VZ, RS, or generation claims. |
| `KeatingRevealed_ShiabProjectionSheet_V1` or equivalent | Enables a missing-sheet identity check. | Does not itself pass selector-family identity. |

Proof restart remains forbidden until a formula-bearing packet and the relevant
selector-family identity review both pass.

## 8. Falsification/demotion condition.

Demote the PTUJ acquisition route from `blocked` to scoped source-route `fail`
only if a complete admitted acquisition path establishes all of:

- A lawful full-resolution extraction or official source-asset audit is complete.
- No frame/source/page/sheet asset contains legible Shiab formula,
  projection-rule text, sheet view, or source formula content.
- The official PTUJ page, linked assets, archive/custodian assets, and source
  package path expose no formula-bearing object.
- `KeatingRevealed_ShiabProjectionSheet_V1` remains unrecovered.
- Manuscript pages 41-44 remain adjacent candidates only, with no source-emitted
  identity to the missing sheet or `SourceForcedCodomainSelectorForK_IG`.
- Any claimed bridge would require target-facing physical outcomes or
  reconstruction preference.

That demotion would be local to the PTUJ/Keating acquisition route. It would not
be a global GU no-go.

## 9. Next meaningful source/computation step.

Next object:

```text
LawfulLocalTzSEvmqxu48FrameExtractorOrSourceAsset_V1
```

Concrete next step:

1. Stage either an approved local `yt-dlp` plus `ffmpeg` extraction path or an
   official/custodian source asset package in a coordinator-owned output path.
2. Record lawful basis, exact URLs/archive ids, commands, versions, file
   manifests, and checksums.
3. Convert only extracted frames/source pages/source package files into
   `TzSEvmqxu48_FormulaBearingFrameOrSourceAssetPacket_V1`.
4. Mark the packet `formula_bearing`, `formula_negative_complete_audit`, or
   `insufficient_resolution`; never mark metadata/oEmbed/caption/thumbnail as a
   formula receipt.
5. Start Keating sheet and `SourceForcedCodomainSelectorForK_IG` identity review
   only after a formula-bearing packet exists.

## 10. Machine-readable JSON summary.

```json
{
  "artifact": "LawfulLocalTzSEvmqxu48AcquisitionContractMatrix_V1",
  "version": "2026-06-25",
  "run_id": "hourly-20260625-0803",
  "cycle": 2,
  "lane": 1,
  "verdict": "BLOCKED_CONTRACT_DEFINED_NO_ACCEPTABLE_PATH_PRESENT",
  "verdict_class": "blocked",
  "target_admission_object": "LawfulLocalTzSEvmqxu48FrameExtractorOrSourceAsset_V1",
  "target_video_id": "TzSEvmqxu48",
  "target_asset_id": "PullThatUpJamie_GUForGRGaugeTheory_TzSEvmqxu48",
  "formula_packet_target": "TzSEvmqxu48_FormulaBearingFrameOrSourceAssetPacket_V1",
  "required_identity_object": "SourceForcedCodomainSelectorForK_IG",
  "repo_has_acceptable_path_today": false,
  "source_reachability_check_repeated": false,
  "sources_read_first": [
    "RESEARCH-POSTURE.md",
    "process/runbooks/five-lane-frontier-run.md",
    "explorations/hourly-20260625-0803-cycle1-ptuj-lawful-source-asset-admission-gate.md",
    "explorations/hourly-20260625-0711-cycle1-keating-ptuj-shiab-asset-execution.md",
    "explorations/hourly-20260625-0711-cycle2-ptuj-frame-capture-feasibility-gate.md",
    "sources/media-index.md"
  ],
  "required_source_surfaces": [
    "GU-MEDIA-2021-PULL-THAT-UP-JAMIE",
    "GU-POD-2021-KEATING-REVEALED-1",
    "GU-POD-2021-KEATING-REVEALED-2",
    "GU-MEDIA-2021-DRAFT-RELEASE"
  ],
  "contract_branches": [
    {
      "branch_id": "LawfulLocalTzSEvmqxu48FrameExtractor_V1",
      "contract_branch": "lawful_local_extractor",
      "accepted_today": false,
      "required_fields": [
        "contract_branch",
        "lawful_basis",
        "input_locator",
        "toolchain_identity",
        "decode_scope",
        "output_manifest",
        "formula_visibility_evidence",
        "target_import_guard"
      ],
      "missing_fields": [
        "lawful_basis_for_local_extraction",
        "toolchain_identity",
        "decode_scope",
        "output_manifest",
        "source_asset_checksums",
        "formula_visibility_evidence"
      ]
    },
    {
      "branch_id": "OfficialTzSEvmqxu48FormulaSourceAssetPacket_V1",
      "contract_branch": "official_source_asset",
      "accepted_today": false,
      "required_fields": [
        "contract_branch",
        "custodian_or_source_surface",
        "asset_locator",
        "provenance_chain",
        "asset_manifest",
        "formula_visibility_evidence",
        "identity_basis",
        "target_import_guard"
      ],
      "missing_fields": [
        "official_or_custodian_source_asset",
        "asset_manifest",
        "source_asset_checksums",
        "formula_visibility_evidence",
        "identity_basis"
      ]
    }
  ],
  "formula_packet_required_fields": [
    "source_asset_branch",
    "source_ids",
    "input_asset_manifest",
    "formula_asset_manifest",
    "formula_or_rule_transcription",
    "visibility_status",
    "identity_to_missing_sheet_or_equivalent",
    "selector_family_review_state"
  ],
  "acquisition_matrix": [
    {
      "field": "target_video_id",
      "current_state": "TzSEvmqxu48_identified",
      "accepted_today": true,
      "acceptance_scope": "locator_only"
    },
    {
      "field": "source_ids",
      "current_state": "required_media_index_source_ids_identified",
      "accepted_today": true,
      "acceptance_scope": "provenance_map_only"
    },
    {
      "field": "lawful_basis",
      "current_state": "official_page_locator_exists_no_admitted_extraction_or_asset_basis",
      "accepted_today": false
    },
    {
      "field": "toolchain_identity",
      "current_state": "prior_cycle_records_no_admitted_yt_dlp_youtube_dl_or_ffmpeg_stack",
      "accepted_today": false
    },
    {
      "field": "direct_source_asset",
      "current_state": "no_direct_official_mp4_webm_or_source_package_found_by_prior_artifacts",
      "accepted_today": false
    },
    {
      "field": "source_asset_checksums",
      "current_state": "no_accepted_source_video_or_package_checksums",
      "accepted_today": false
    },
    {
      "field": "frame_or_asset_manifest",
      "current_state": "prior_storyboard_thumbnail_metadata_not_accepted",
      "accepted_today": false
    },
    {
      "field": "formula_visibility_evidence",
      "current_state": "caption_metadata_names_shiab_projection_no_formula_bearing_asset",
      "accepted_today": false
    },
    {
      "field": "KeatingRevealed_ShiabProjectionSheet_V1",
      "current_state": "missing_sheet_locator_only",
      "accepted_today": false
    },
    {
      "field": "manuscript_identity_to_selector",
      "current_state": "adjacent_manuscript_candidate_identity_not_proved",
      "accepted_today": false
    },
    {
      "field": "target_import_guard",
      "current_state": "target_import_clean_but_insufficient_without_source_asset",
      "accepted_today": true,
      "acceptance_scope": "necessary_not_sufficient"
    },
    {
      "field": "accepted_receipt_count",
      "current_state": 0,
      "accepted_today": true,
      "acceptance_scope": "zero_state_only"
    },
    {
      "field": "proof_restart_allowed",
      "current_state": false,
      "accepted_today": true,
      "acceptance_scope": "blocked_state_only"
    }
  ],
  "non_accepted_receipt_types": [
    {
      "object_type": "PTUJ_caption_text",
      "accepted_as_formula_receipt": false,
      "reason": "caption_is_locator_or_terminology_not_formula_pixels_or_source_bytes"
    },
    {
      "object_type": "YouTube_oEmbed_JSON",
      "accepted_as_formula_receipt": false,
      "reason": "metadata_is_not_frame_or_source_asset"
    },
    {
      "object_type": "YouTube_watch_page_reachability",
      "accepted_as_formula_receipt": false,
      "reason": "html_reachability_is_not_video_or_frame_acquisition"
    },
    {
      "object_type": "YouTube_thumbnail",
      "accepted_as_formula_receipt": false,
      "reason": "preview_image_is_not_accepted_formula_packet"
    },
    {
      "object_type": "low_resolution_storyboard_frames",
      "accepted_as_formula_receipt": false,
      "reason": "prior_preview_resolution_negative_is_not_full_source_decode"
    },
    {
      "object_type": "Keating_transcript_window",
      "accepted_as_formula_receipt": false,
      "reason": "missing_sheet_locator_does_not_supply_the_sheet"
    },
    {
      "object_type": "manuscript_pages_41_to_44",
      "accepted_as_formula_receipt": false,
      "reason": "adjacent_candidate_identity_to_missing_sheet_and_selector_not_proved"
    }
  ],
  "missing_objects": [
    "LawfulLocalTzSEvmqxu48FrameExtractor_V1",
    "OfficialTzSEvmqxu48FormulaSourceAssetPacket_V1",
    "TzSEvmqxu48_FormulaBearingFrameOrSourceAssetPacket_V1",
    "KeatingRevealed_ShiabProjectionSheet_V1",
    "manuscript_equivalence_proof_to_SourceForcedCodomainSelectorForK_IG"
  ],
  "receipt_state": {
    "accepted_source_asset_count": 0,
    "accepted_formula_receipt_count": 0,
    "accepted_frame_packet_count": 0,
    "accepted_receipt_count": 0,
    "accepted_for_routing_count": 0,
    "accepted_receipts": [],
    "metadata_or_caption_receipt_accepted": false,
    "thumbnail_receipt_accepted": false,
    "storyboard_receipt_accepted": false,
    "formula_asset_captured": false,
    "proof_restart_allowed": false,
    "claim_promotion_allowed": false
  },
  "first_exact_obstruction": {
    "id": "LawfulLocalTzSEvmqxu48FrameExtractorOrSourceAsset_V1",
    "obstruction_type": "contract_branches_missing",
    "description": "Neither the lawful local extractor branch nor the fallback official formula source asset branch is present with manifest, provenance, checksums, and formula visibility evidence."
  },
  "sufficient_to_convert_metadata_to_formula_packet": [
    "admitted_lawful_local_extractor_or_official_source_asset_branch",
    "source_or_frame_asset_manifest_with_checksums",
    "visible_formula_or_projection_rule_transcription_or_complete_formula_negative_audit",
    "identity_basis_to_TzSEvmqxu48_or_official_source_equivalent",
    "target_import_guard",
    "blocked_or_passed_identity_review_against_KeatingRevealed_ShiabProjectionSheet_V1_before_selector_review"
  ],
  "impact_if_closed": {
    "would_enable_formula_packet_audit": true,
    "would_create_receipt_by_contract_closure_alone": false,
    "proof_restart_possible_by_contract_closure_alone": false,
    "downstream_physics_promoted_by_contract_closure_alone": false
  },
  "falsification_or_demotion_condition": [
    "complete_admitted_full_resolution_extraction_or_official_source_asset_audit_finds_no_formula_projection_rule_sheet_view_or_source_formula_content",
    "official_page_linked_assets_archive_and_custodian_paths_expose_no_formula_bearing_object",
    "KeatingRevealed_ShiabProjectionSheet_V1_remains_unrecovered",
    "manuscript_pages_41_44_remain_adjacent_without_source_emitted_identity",
    "bridge_to_SourceForcedCodomainSelectorForK_IG_requires_target_import"
  ],
  "next_meaningful_step": {
    "next_object": "LawfulLocalTzSEvmqxu48FrameExtractorOrSourceAsset_V1",
    "description": "Stage either an approved local yt-dlp plus ffmpeg extraction path or an official/custodian source asset package, then record provenance, commands, versions, manifests, checksums, and visible formula evidence before any selector-family review."
  },
  "forbidden_promotions": {
    "caption_or_oembed_selector_receipt_accepted": false,
    "metadata_converted_to_formula_packet_without_source_asset": false,
    "thumbnail_receipt_accepted": false,
    "storyboard_preview_promoted_to_full_route_fail": false,
    "formula_asset_captured": false,
    "SourceForcedCodomainSelectorForK_IG_accepted": false,
    "family_identity_passed": false,
    "proof_restart": false,
    "downstream_physics_claim": false,
    "global_no_go": false
  }
}
```
