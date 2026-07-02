---
title: "Hourly 20260625 1302 Cycle 2 PTUJ Toolchain Manifest Gate"
date: "2026-06-25"
run_id: "hourly-20260625-1302"
cycle: 2
lane: 1
doc_type: ptuj_toolchain_manifest_gate
artifact_id: "LawfulLocalTzSEvmqxu48ToolchainManifestGate_V1"
verdict: "BLOCKED_NO_ADMISSIBLE_TOOLCHAIN_SOURCE_BYTE_MANIFEST"
owned_path: "explorations/hourly-20260625-1302-cycle2-ptuj-toolchain-manifest-gate.md"
companion_audit: "tests/hourly_20260625_1302_cycle2_ptuj_toolchain_manifest_gate_audit.py"
---

# Hourly 20260625 1302 Cycle 2 PTUJ Toolchain Manifest Gate

## 1. Verdict: blocked.

`LawfulLocalTzSEvmqxu48FrameExtractor_V1` cannot be admitted from the current
repo-local environment and files.

No current toolchain/source-byte combination is admissible. The repo has a
precise branch contract and locator evidence for `TzSEvmqxu48`, but it does not
currently have an admitted extractor executable/module, an admitted decoder, a
repo-local source media/package object, or a decoded frame/source manifest with
checksums.

Decision state:

```text
admitted_toolchain_count: 0
admitted_manifest_count: 0
accepted_receipt_count: 0
proof_restart_allowed: false
ig_selector_routing_allowed: false
external_download_performed: false
```

This is not a formula-packet failure and not a global no-go. It is a source and
toolchain manifest gate: the required object is specified well enough to test,
but the current repo-local inputs do not satisfy it.

## 2. What was derived directly from repo sources and local environment checks.

Required sources read first:

| source | derived fact |
| --- | --- |
| `RESEARCH-POSTURE.md` | Metadata, compatibility, and process discipline cannot be promoted into proof evidence or source receipts. |
| `process/runbooks/five-lane-frontier-run.md` | A lane must make a decision, name the first exact obstruction, and avoid converting hosted or compatible material into derivation. |
| `explorations/hourly-20260625-1302-cycle1-ptuj-extractor-branch.md` | Cycle 1 isolated the missing object as `LawfulLocalTzSEvmqxu48FrameExtractor_V1.toolchain_identity_and_output_manifest`. |
| `tests/hourly_20260625_1302_cycle1_ptuj_extractor_branch_audit.py` | The prior audit requires zero receipts unless the extractor branch is fully source-backed. |
| `explorations/hourly-20260625-0803-cycle2-ptuj-lawful-acquisition-contract-matrix.md` | The admissible acquisition object has two distinct branches: lawful local extractor or official source asset; this lane tests the local extractor manifest gate. |

Current local checks performed in this lane:

| check | observed result | implication |
| --- | --- | --- |
| `Get-Command python,yt-dlp,youtube-dl,ffmpeg -ErrorAction SilentlyContinue` | Only `python.exe` resolved, at `AppData\Local\Programs\Python\Python314\python.exe`. | Python is available, but the required extraction/decoding command stack is not. |
| Python `importlib.util.find_spec("yt_dlp")` and `shutil.which(...)` for `yt-dlp`, `youtube-dl`, `ffmpeg` | `yt_dlp` module unavailable; all three executables unresolved. | There is no local admitted YouTube acquisition module or `ffmpeg` decoder. |
| `rg` over repo text for `TzSEvmqxu48`, extractor/source-asset object names, `yt-dlp`, `yt_dlp`, `youtube-dl`, `ffmpeg`, `storyboard`, `thumbnail`, `caption`, and `oEmbed` | Found prior markdown/audit contract rows, source locators, and non-receipt evidence; found no admitted extractor object with current command/version/output manifest. | The repo contains the decision history and locators, not an admissible toolchain manifest. |
| `rg --files` filtered for PTUJ/TzSEvmqxu48/media/frame/source extensions and names | Found prior exploration/test artifacts and unrelated RS temporary images; no repo-local `TzSEvmqxu48` source media/package bytes or decoded frame manifest. | There are no source bytes to decode under this branch. |

No external media was downloaded or required for this gate. The question here is
whether current repo-local environment and files already admit the extractor
branch; they do not.

## 3. The strongest positive result.

The strongest positive result is a decision-grade negative admission test with a
minimal closing manifest.

The current repo state is useful because it distinguishes three things that must
not be conflated:

| object | current status | admissibility consequence |
| --- | --- | --- |
| `TzSEvmqxu48` locator and PTUJ/Keating context | Present as prior source-locator evidence. | Useful for provenance, not source bytes. |
| Local Python runtime | Present. | Useful for audit/test execution, not a video extractor or decoder. |
| `LawfulLocalTzSEvmqxu48FrameExtractor_V1.toolchain_identity_and_output_manifest` | Absent. | Blocks local extractor admission. |

The positive route is therefore exact: if a future run supplies both a lawful
source-byte object and a deterministic toolchain/output manifest, the gate can
be rerun without changing the branch contract.

## 4. The first exact obstruction or missing source/tool object.

The first exact obstruction is:

```text
LawfulLocalTzSEvmqxu48FrameExtractor_V1.toolchain_identity_and_output_manifest
```

The first missing source/tool objects are:

```text
1. admitted_acquisition_tool_identity
2. admitted_decoder_tool_identity
3. repo_local_TzSEvmqxu48_source_bytes_or_source_package
4. decoded_frame_or_source_output_manifest_with_checksums
```

Expanded obstruction:

```text
No admissible local extractor branch exists because the repo-local environment
has no yt-dlp/youtube-dl/yt_dlp equivalent, no ffmpeg or equivalent decoder, no
TzSEvmqxu48 media/source bytes, and no frame/source output manifest with
timecodes, dimensions, sizes, checksums, and extraction commands.
```

This obstruction precedes any formula-bearing packet, Keating missing-sheet
identity review, or `SourceForcedCodomainSelectorForK_IG` selector-family
routing.

## 5. The constructive next object that would remove or test the obstruction.

The exact minimum manifest that would close this gate is:

```text
LawfulLocalTzSEvmqxu48FrameExtractor_V1.toolchain_identity_and_output_manifest
```

Minimum required fields:

| field | required content |
| --- | --- |
| `lawful_basis` | The repo-use basis for acquiring or using the specific `TzSEvmqxu48` bytes, tied to `GU-MEDIA-2021-PULL-THAT-UP-JAMIE` or an official/custodian source record. |
| `source_byte_object` | Repo-local path or immutable archive/package locator for the source video/source package, with byte size and checksum. |
| `acquisition_tool_identity` | Exact executable/module name, version, provenance/install source, and command line; if no acquisition was needed because bytes were supplied, record that distinction. |
| `decoder_tool_identity` | Exact decoder/extractor executable/module name, version, provenance/install source, and command line. |
| `input_locator` | `TzSEvmqxu48`, official PTUJ locator/source id, and any archive/package id used to obtain the bytes. |
| `decode_scope` | Full asset or explicit time-window/sampling rule, including oversampling rule around text/scene transitions. |
| `output_manifest` | Frame/source segment paths, timecodes or page/segment locators, dimensions, file sizes, checksums, and the command that generated each output class. |
| `visibility_audit_status` | One of `formula_bearing`, `formula_negative_complete_audit`, or `insufficient_resolution`, with illegible material marked rather than inferred. |
| `target_import_guard` | Confirmation that downstream physics targets, DESI/dark-energy expectations, and selector-family outcomes did not select or normalize the source object. |

This manifest would remove the present toolchain/source-byte obstruction. It
would not by itself create a formula receipt; a formula-bearing or complete
formula-negative frame/source audit is still a separate packet decision.

## 6. What this means for PTUJ formula packet and IG selector routing.

`TzSEvmqxu48_FormulaBearingFrameOrSourceAssetPacket_V1` remains blocked before
construction. The formula packet has no admissible input branch from the current
repo-local environment.

IG selector routing remains closed:

| routing predicate | status |
| --- | --- |
| admitted local extractor branch | false |
| admitted local toolchain/source-byte manifest | false |
| admitted official source-asset branch | false |
| formula-bearing frame/source packet | false |
| complete formula-negative full-resolution audit | false |
| identity to `KeatingRevealed_ShiabProjectionSheet_V1` or source equivalent | false |
| `SourceForcedCodomainSelectorForK_IG` accepted from PTUJ/Keating route | false |
| proof restart allowed | false |

Captions, oEmbed data, thumbnails, storyboard previews, locator rows, and
Keating missing-sheet references remain non-receipt evidence. They may guide
lawful source acquisition, but they cannot be promoted into a formula packet or
selector-family identity.

## 7. Next meaningful proof/source computation step.

The next meaningful step is not downstream proof replay. It is one source
computation:

```text
Build or stage the minimum toolchain/source-byte manifest for
LawfulLocalTzSEvmqxu48FrameExtractor_V1, then run a checksummed extraction
audit over the produced frame/source outputs.
```

If the repo receives lawful source bytes first, use those bytes and record that
no network acquisition command is part of the manifest. If the repo receives an
approved local acquisition stack first, record versions, provenance, exact
commands, downloaded/source-byte checksums, and decoded output checksums before
any formula or selector claim is evaluated.

## 8. Machine-readable JSON summary.

```json
{
  "artifact": "LawfulLocalTzSEvmqxu48ToolchainManifestGate_V1",
  "run_id": "hourly-20260625-1302",
  "cycle": 2,
  "lane": 1,
  "verdict": "BLOCKED_NO_ADMISSIBLE_TOOLCHAIN_SOURCE_BYTE_MANIFEST",
  "verdict_class": "blocked",
  "target_branch": "LawfulLocalTzSEvmqxu48FrameExtractor_V1",
  "target_manifest": "LawfulLocalTzSEvmqxu48FrameExtractor_V1.toolchain_identity_and_output_manifest",
  "target_video_id": "TzSEvmqxu48",
  "target_asset_id": "PullThatUpJamie_GUForGRGaugeTheory_TzSEvmqxu48",
  "checked_tools": [
    {
      "name": "python",
      "kind": "executable",
      "available": true,
      "source": "C:\\Users\\joe\\AppData\\Local\\Programs\\Python\\Python314\\python.exe",
      "admitted_for_extraction": false
    },
    {
      "name": "yt-dlp",
      "kind": "executable",
      "available": false,
      "source": null,
      "admitted_for_extraction": false
    },
    {
      "name": "youtube-dl",
      "kind": "executable",
      "available": false,
      "source": null,
      "admitted_for_extraction": false
    },
    {
      "name": "ffmpeg",
      "kind": "executable",
      "available": false,
      "source": null,
      "admitted_for_extraction": false
    },
    {
      "name": "yt_dlp",
      "kind": "python_module",
      "available": false,
      "source": null,
      "admitted_for_extraction": false
    }
  ],
  "local_environment_checks": {
    "get_command_python_yt_dlp_youtube_dl_ffmpeg": "python_only_resolved",
    "python_importlib_yt_dlp_find_spec": false,
    "shutil_which_yt_dlp": null,
    "shutil_which_youtube_dl": null,
    "shutil_which_ffmpeg": null
  },
  "repo_local_source_bytes_present": false,
  "repo_local_source_byte_objects": [],
  "repo_local_decoded_output_manifest_present": false,
  "repo_local_decoded_output_manifests": [],
  "repo_local_formula_bearing_packet_present": false,
  "official_source_asset_branch_present": false,
  "external_download_required_for_this_gate": false,
  "external_download_performed": false,
  "network_acquisition_attempted": false,
  "admitted_toolchain_count": 0,
  "admitted_manifest_count": 0,
  "accepted_receipt_count": 0,
  "accepted_receipts": [],
  "proof_restart_allowed": false,
  "claim_promotion_allowed": false,
  "ig_selector_routing_allowed": false,
  "metadata_storyboard_caption_not_accepted": true,
  "non_receipt_evidence": [
    {
      "object_type": "PTUJ_caption_text",
      "accepted_as_formula_receipt": false
    },
    {
      "object_type": "YouTube_oEmbed_JSON",
      "accepted_as_formula_receipt": false
    },
    {
      "object_type": "YouTube_thumbnail",
      "accepted_as_formula_receipt": false
    },
    {
      "object_type": "low_resolution_storyboard_frames",
      "accepted_as_formula_receipt": false
    },
    {
      "object_type": "Keating_missing_sheet_locator",
      "accepted_as_formula_receipt": false
    }
  ],
  "first_exact_obstruction": {
    "id": "LawfulLocalTzSEvmqxu48FrameExtractor_V1.toolchain_identity_and_output_manifest",
    "missing_source_tool_objects": [
      "admitted_acquisition_tool_identity",
      "admitted_decoder_tool_identity",
      "repo_local_TzSEvmqxu48_source_bytes_or_source_package",
      "decoded_frame_or_source_output_manifest_with_checksums"
    ],
    "description": "No admissible local extractor branch exists because no current toolchain/source-byte/output-manifest combination is present."
  },
  "minimum_manifest_to_close_gate": {
    "id": "LawfulLocalTzSEvmqxu48FrameExtractor_V1.toolchain_identity_and_output_manifest",
    "would_close_this_gate": true,
    "would_create_formula_receipt_by_itself": false,
    "required_fields": [
      "lawful_basis",
      "source_byte_object",
      "acquisition_tool_identity",
      "decoder_tool_identity",
      "input_locator",
      "decode_scope",
      "output_manifest",
      "visibility_audit_status",
      "target_import_guard"
    ]
  },
  "ptuj_formula_packet_and_ig_routing": {
    "formula_packet_status": "blocked_before_construction",
    "formula_packet_required_before_keating_identity_review": true,
    "keating_sheet_identity_passed": false,
    "source_forced_codomain_selector_for_k_ig_accepted": false,
    "routing_allowed": false
  },
  "forbidden_promotions": {
    "metadata_oembed_caption_storyboard_accepted_as_formula_receipt": false,
    "metadata_converted_to_formula_packet_without_source_bytes": false,
    "storyboard_preview_promoted_to_full_route_fail": false,
    "python_runtime_promoted_to_extractor_toolchain": false,
    "locator_promoted_to_source_bytes": false,
    "formula_asset_captured": false,
    "SourceForcedCodomainSelectorForK_IG_accepted": false,
    "family_identity_passed": false,
    "proof_restart": false,
    "downstream_physics_claim": false,
    "global_no_go": false
  }
}
```
