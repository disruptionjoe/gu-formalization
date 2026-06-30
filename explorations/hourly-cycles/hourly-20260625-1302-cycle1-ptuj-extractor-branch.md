---
title: "Hourly 20260625 1302 Cycle 1 PTUJ Extractor Branch"
date: "2026-06-25"
run_id: "hourly-20260625-1302"
cycle: 1
lane: 1
doc_type: ptuj_extractor_branch_gate
artifact_id: "LawfulLocalTzSEvmqxu48FrameExtractorBranchDecision_V1"
verdict: "BLOCKED_NO_CURRENT_REPO_LOCAL_LAWFUL_REPRODUCIBLE_EXTRACTOR_BRANCH"
owned_path: "explorations/hourly-20260625-1302-cycle1-ptuj-extractor-branch.md"
companion_audit: "tests/hourly_20260625_1302_cycle1_ptuj_extractor_branch_audit.py"
---

# Hourly 20260625 1302 Cycle 1 PTUJ Extractor Branch

## 1. Verdict: blocked.

`LawfulLocalTzSEvmqxu48FrameExtractor_V1` is not currently derivable or
admissible from repo-local sources.

The 0803 lawful acquisition contract defines this as one branch of
`LawfulLocalTzSEvmqxu48FrameExtractorOrSourceAsset_V1`. This lane tests only
the extractor branch, not the fallback official source-asset branch. The branch
requires lawful basis, toolchain identity, input locator, decode scope, output
manifest, source/frame checksums, formula-visibility evidence or a complete
formula-negative audit, and target-import guard.

Current decision state:

```text
extractor_branch_exists: false
official_asset_branch_exists: false
branches_conflated: false
accepted_receipt_count: 0
proof_restart_allowed: false
claim_promotion_allowed: false
```

This is not a scoped route fail. The contract is precise enough to test, but
the required repo-local extractor object is absent.

## 2. What was derived directly from repo sources.

Required sources read first:

| source | derived fact |
| --- | --- |
| `RESEARCH-POSTURE.md` | Metadata, compatibility, process discipline, and target agreement cannot become proof evidence. |
| `process/runbooks/five-lane-frontier-run.md` | A lane must identify the first exact obstruction and avoid promotion from hosted or compatible material. |
| `explorations/hourly-20260625-0803-cycle2-ptuj-lawful-acquisition-contract-matrix.md` | The accepted acquisition object has exactly two branches: local extractor or official source asset. Neither was present at 0803. |
| `explorations/hourly-20260625-0803-cycle3-next-frontier-dependency-dag.md` | `PTUJ_EXTRACTOR_BRANCH` is an upstream source-object lane; `PTUJ_FORMULA_PACKET` is sequential and must wait. |
| `tests/hourly_20260625_0803_cycle2_ptuj_lawful_acquisition_contract_matrix_audit.py` | The audit invariant is zero accepted receipts unless a fully source-backed extractor or asset exists. |

Additional repo-local checks performed in this lane:

| check | result | implication |
| --- | --- | --- |
| `rg` for `TzSEvmqxu48`, `LawfulLocalTzSEvmqxu48FrameExtractor`, `OfficialTzSEvmqxu48FormulaSourceAssetPacket`, `yt-dlp`, `yt_dlp`, `youtube-dl`, `ffmpeg`, `oEmbed`, `storyboard`, `thumbnail`, and `caption` | Found prior markdown/audit evidence and contract rows, but no admitted extractor object or PTUJ source-asset package. | Repo has locator/history evidence, not a current extractor branch. |
| repo-local file scan under `automation`, `sources`, and `explorations` for PTUJ/TzSEvmqxu48 media or source files | Found prior PTUJ artifacts and unrelated RS temporary images; no local `TzSEvmqxu48` media/source file was found. | There is no local input asset to decode as part of this branch. |
| `Get-Command yt-dlp`, `Get-Command youtube-dl`, `Get-Command ffmpeg` | All unresolved. | The local command-line extraction/decoding stack is absent. |
| Python `importlib.util.find_spec("yt_dlp")` | `False`. | The Python extractor module is absent. |
| `Get-Command python` | Python exists at `C:\Users\joe\AppData\Local\Programs\Python\Python314\python.exe`. | Python alone is not a lawful video extractor or decoder. |

The repo also contains prior positive locator evidence: `TzSEvmqxu48` is the
Pull That Up Jamie visual-aid video id, the official PTUJ page caption names
Shiab Projection, Keating points to a missing projection sheet, and manuscript
pages 41-44 remain adjacent Shiab material. None of those is an extractor.

## 3. The strongest positive result.

The strongest positive result is a complete negative branch decision, not a
receipt:

```text
The extractor branch has a precise acceptance contract, and current repo-local
checks show exactly which branch fields are still empty.
```

The branch is strong operationally because the next successful object is not
ambiguous. A future `LawfulLocalTzSEvmqxu48FrameExtractor_V1` must provide:

| branch field | current repo-local state |
| --- | --- |
| `branch_id` | Named and contracted. |
| `contract_branch` | `lawful_local_extractor`, distinct from `official_source_asset`. |
| `lawful_basis` | Not supplied for an actual local acquisition. |
| `input_locator` | `TzSEvmqxu48` and official PTUJ locator are known, locator-only. |
| `toolchain_identity` | Missing: no `yt-dlp`, `youtube-dl`, `ffmpeg`, or `yt_dlp` module. |
| `decode_scope` | Missing: no accepted frame range, sampling rule, or full-asset decode plan tied to a runnable toolchain. |
| `output_manifest` | Missing: no frame filenames, timecodes, dimensions, sizes, or checksums. |
| `formula_visibility_evidence` | Missing: no source-backed full-resolution formula-bearing frame or complete formula-negative audit. |
| `target_import_guard` | Satisfied as a guard only; no target data was used, but that does not admit the branch. |

## 4. The first exact obstruction or missing proof/source object.

The first exact missing object is:

```text
LawfulLocalTzSEvmqxu48FrameExtractor_V1.toolchain_identity_and_output_manifest
```

Expanded obstruction:

```text
No repo-local lawful reproducible extractor branch exists because the repo has
no admitted extractor executable/module, no acquisition command, no ffmpeg
decoder, no source video/package bytes, no decoded frame manifest, and no frame
checksums for TzSEvmqxu48.
```

This obstruction precedes `TzSEvmqxu48_FormulaBearingFrameOrSourceAssetPacket_V1`.
It also precedes Keating sheet identity and any `SourceForcedCodomainSelectorForK_IG`
review.

## 5. The constructive next object that would remove or test the obstruction.

The constructive next object is:

```text
LawfulLocalTzSEvmqxu48FrameExtractor_V1
```

Minimum content:

| field | required content |
| --- | --- |
| `lawful_basis` | A source URL/archive/custodian basis tied to `GU-MEDIA-2021-PULL-THAT-UP-JAMIE`, with repo-use provenance. |
| `toolchain_identity` | Exact executable/module names, versions, source/install provenance, and commands. |
| `input_locator` | `TzSEvmqxu48`, official PTUJ source id, and the exact acquired media/source locator. |
| `decode_scope` | Complete asset or time-window sampling rule, with oversampling around text/scene transitions. |
| `output_manifest` | Frame paths, timecodes, dimensions, file sizes, checksums, and extraction commands. |
| `visibility_audit` | Visible formula/projection-rule transcription, or a complete full-resolution formula-negative audit. |
| `target_import_guard` | Confirmation that no downstream physics target selected or normalized the source object. |

This object would test the obstruction. It would not, by itself, create a
formula receipt.

## 6. What this means for PTUJ/Keating and IG selector routing.

PTUJ/Keating remains blocked before routing. The route has useful source
locators, but no accepted extractor branch, no official formula asset branch,
no formula-bearing packet, and no identity to the Keating missing sheet.

IG selector routing must stay closed:

| routing predicate | status |
| --- | --- |
| accepted extractor branch | false |
| accepted official source asset branch | false |
| accepted formula-bearing frame/source packet | false |
| identity to `KeatingRevealed_ShiabProjectionSheet_V1` or source equivalent | false |
| identity to `SourceForcedCodomainSelectorForK_IG` | false |
| proof restart allowed | false |

Metadata/oEmbed/storyboard/caption evidence can locate the video and prior
attempts. It cannot become a formula receipt, a selector receipt, or a scoped
route failure without a complete admitted extraction/source-asset audit.

## 7. Next meaningful proof/source computation step.

The next meaningful computation is not downstream proof replay. It is a
source-object construction or a deterministic negative test of that construction:

1. Stage an approved repo-local `yt-dlp` plus `ffmpeg` stack, or an equivalent
   lawful extractor, in a coordinator-owned path.
2. Record versions, commands, lawful basis, and source locator.
3. Decode `TzSEvmqxu48` into a checksummed frame manifest.
4. Mark the result as `formula_bearing`, `formula_negative_complete_audit`, or
   `insufficient_resolution`.
5. Only then consider a PTUJ/Keating sheet identity review.

## 8. Machine-readable JSON summary.

```json
{
  "artifact": "LawfulLocalTzSEvmqxu48FrameExtractorBranchDecision_V1",
  "run_id": "hourly-20260625-1302",
  "cycle": 1,
  "lane": 1,
  "verdict": "BLOCKED_NO_CURRENT_REPO_LOCAL_LAWFUL_REPRODUCIBLE_EXTRACTOR_BRANCH",
  "verdict_class": "blocked",
  "target_branch": "LawfulLocalTzSEvmqxu48FrameExtractor_V1",
  "parent_contract": "LawfulLocalTzSEvmqxu48FrameExtractorOrSourceAsset_V1",
  "target_video_id": "TzSEvmqxu48",
  "target_asset_id": "PullThatUpJamie_GUForGRGaugeTheory_TzSEvmqxu48",
  "repo_local_lawful_reproducible_extractor_branch_exists": false,
  "official_asset_branch_tested_by_this_lane": false,
  "branches_conflated": false,
  "branch_fields": {
    "contract_branch": "lawful_local_extractor",
    "lawful_basis_present": false,
    "input_locator_present": true,
    "toolchain_identity_present": false,
    "decode_scope_present": false,
    "output_manifest_present": false,
    "source_asset_checksums_present": false,
    "formula_visibility_evidence_present": false,
    "target_import_guard_present": true
  },
  "toolchain_availability": {
    "python_available": true,
    "python_source": "C:\\Users\\joe\\AppData\\Local\\Programs\\Python\\Python314\\python.exe",
    "yt_dlp_module_available": false,
    "yt_dlp_executable_available": false,
    "youtube_dl_executable_available": false,
    "ffmpeg_available": false,
    "admitted_extraction_command_present": false
  },
  "repo_local_asset_availability": {
    "local_tzsevmqxu48_media_file_found": false,
    "official_formula_source_asset_package_found": false,
    "decoded_frame_manifest_found": false,
    "formula_bearing_frame_or_source_asset_found": false
  },
  "branch_distinctions": {
    "extractor_branch_id": "LawfulLocalTzSEvmqxu48FrameExtractor_V1",
    "official_asset_branch_id": "OfficialTzSEvmqxu48FormulaSourceAssetPacket_V1",
    "extractor_branch_accepted": false,
    "official_asset_branch_accepted": false,
    "extractor_branch_is_not_official_asset_branch": true,
    "official_asset_branch_would_not_supply_toolchain_identity": true
  },
  "non_receipt_evidence": [
    {
      "object_type": "PTUJ_caption_text",
      "accepted_as_formula_receipt": false,
      "use": "locator_and_terminology_only"
    },
    {
      "object_type": "YouTube_oEmbed_JSON",
      "accepted_as_formula_receipt": false,
      "use": "metadata_identity_only"
    },
    {
      "object_type": "YouTube_watch_page_or_embed_reachability",
      "accepted_as_formula_receipt": false,
      "use": "addressability_only"
    },
    {
      "object_type": "YouTube_thumbnail",
      "accepted_as_formula_receipt": false,
      "use": "preview_only"
    },
    {
      "object_type": "low_resolution_storyboard_frames",
      "accepted_as_formula_receipt": false,
      "use": "prior_preview_negative_not_full_decode"
    },
    {
      "object_type": "Keating_missing_sheet_locator",
      "accepted_as_formula_receipt": false,
      "use": "missing_object_locator_only"
    }
  ],
  "accepted_receipt_count": 0,
  "accepted_receipts": [],
  "proof_restart_allowed": false,
  "claim_promotion_allowed": false,
  "first_exact_obstruction": {
    "id": "LawfulLocalTzSEvmqxu48FrameExtractor_V1.toolchain_identity_and_output_manifest",
    "missing_object": "LawfulLocalTzSEvmqxu48FrameExtractor_V1",
    "description": "No admitted extractor executable/module, acquisition command, ffmpeg decoder, source video bytes, decoded frame manifest, or frame checksums exist for TzSEvmqxu48."
  },
  "constructive_next_object": {
    "id": "LawfulLocalTzSEvmqxu48FrameExtractor_V1",
    "would_remove_or_test_obstruction": true,
    "would_create_receipt_by_itself": false,
    "required_fields": [
      "lawful_basis",
      "toolchain_identity",
      "input_locator",
      "decode_scope",
      "output_manifest",
      "visibility_audit",
      "target_import_guard"
    ]
  },
  "ptuj_keating_ig_routing": {
    "ptuj_keating_route_status": "blocked_before_routing",
    "formula_packet_required_before_identity_review": true,
    "keating_sheet_identity_passed": false,
    "source_forced_codomain_selector_for_k_ig_accepted": false,
    "ig_selector_routing_allowed": false
  },
  "forbidden_promotions": {
    "metadata_oembed_caption_storyboard_accepted_as_formula_receipt": false,
    "metadata_converted_to_formula_packet_without_source_asset": false,
    "extractor_branch_conflated_with_official_asset_branch": false,
    "official_asset_branch_conflated_with_extractor_branch": false,
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
