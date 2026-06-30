---
title: "Hourly 20260625 1503 Cycle 2 PTUJ Official Source Asset Branch"
date: "2026-06-25"
run_id: "hourly-20260625-1503"
cycle: 2
lane: 1
doc_type: ptuj_official_source_asset_branch
artifact_id: "OfficialTzSEvmqxu48FormulaSourceAssetPacketDecision_1503_Cycle2_Lane1_V1"
verdict: "blocked"
owned_path: "explorations/hourly-20260625-1503-cycle2-ptuj-official-source-asset-branch.md"
companion_audit: "tests/hourly_20260625_1503_cycle2_ptuj_official_source_asset_branch_audit.py"
---

# Hourly 20260625 1503 Cycle 2 PTUJ Official Source Asset Branch

## 1. Verdict.

Verdict: **blocked**.

`OfficialTzSEvmqxu48FormulaSourceAssetPacket_V1` cannot be accepted from the
current repo sources plus the source-safe online checks performed here.

The official/custodian branch remains distinct from the local extractor branch,
but the tested branch does not currently provide a bypass. The official Pull
That Up Jamie page exposes a normal YouTube embed for `TzSEvmqxu48` and a page
description naming Shiab Projection. YouTube oEmbed, watch-page reachability,
and thumbnail reachability confirm metadata and locator continuity. None of
those objects is a formula source asset, custodian media object, immutable
source package, checksummed source page asset, or source locator that can be
inspected without local extraction.

Decision state:

```text
official_asset_present: false
custodian_source_asset_present: false
source_asset_packet_accepted: false
local_extractor_required: true
visibility_audit_enabled: false
proof_restart_allowed: false
```

This is not a formula-negative decision. It is a source-object admission
decision: the branch that could bypass local extraction is still missing the
first source object it would need.

## 2. What was derived directly from repo sources and source-safe lookup.

Required sources read first:

| source | direct derivation |
| --- | --- |
| `RESEARCH-POSTURE.md` | Locator evidence, metadata continuity, and target compatibility cannot become a source receipt or proof restart. |
| `process/runbooks/five-lane-frontier-run.md` | The lane must name the first exact missing object and avoid promotion from hosted/compatible material. |
| `process/runbooks/three-cycle-fifteen-hole-run.md` | This is a quality-hole lane only if it separates the official-source bypass from the local extractor branch. |
| `explorations/hourly-20260625-1503-cycle1-ptuj-toolchain-source-byte-manifest.md` | Cycle 1 left the local extractor blocked and preserved the official/custodian source-asset branch as distinct. |
| `explorations/hourly-20260625-1302-cycle2-ptuj-toolchain-manifest-gate.md` | The local branch lacks toolchain, source bytes, and output manifest; this lane tests whether an official source asset bypass exists. |
| `sources/media-index.md` | `GU-MEDIA-2021-PULL-THAT-UP-JAMIE` is an official visual-aid page and provenance map entry, not proof or source bytes by itself. |

Additional directly relevant PTUJ branch history read:

| source | direct derivation |
| --- | --- |
| `explorations/hourly-20260625-0803-cycle1-ptuj-lawful-source-asset-admission-gate.md` | Earlier admission gate found neither a lawful local extractor nor direct formula source asset. |
| `explorations/hourly-20260625-0711-cycle2-ptuj-frame-capture-feasibility-gate.md` | Earlier live checks found official page HTML, oEmbed, watch page, and thumbnail reachability, but no direct mp4/webm or formula packet. |

Source-safe online checks performed in this lane:

| check | inspected locator | observed object | accepted as formula source asset? |
| --- | --- | --- | --- |
| Official page text fetch | `https://geometricunity.org/pull-that-up-jamie/` | HTTP 200 HTML; page includes the heading `Geometric Unity for General Relativity & Gauge Theory`, `TzSEvmqxu48`, an iframe, and Shiab Projection descriptive text. | no |
| Official page link/src parse | same page | `https://www.youtube.com/embed/TzSEvmqxu48?feature=oembed` plus other YouTube embed URLs; no `.mp4`, `.webm`, `.m4v`, `.mov`, archive package, or custodian asset URL found. | no |
| YouTube oEmbed | `https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v=TzSEvmqxu48&format=json` | HTTP 200 JSON with title, author, iframe HTML, and thumbnail URL. | no |
| YouTube watch HEAD | `https://www.youtube.com/watch?v=TzSEvmqxu48` | HTTP 200 `text/html` watch page. | no |
| YouTube thumbnail HEAD | `https://img.youtube.com/vi/TzSEvmqxu48/maxresdefault.jpg` | HTTP 200 `image/jpeg`, content length `54692`. | no |

No large media was downloaded. No binary source asset was created. The thumbnail
was checked only by HEAD metadata and was not treated as a source asset.

## 3. The strongest positive result.

The strongest positive result is a confirmed official-page-to-YouTube locator
chain:

```text
GU-MEDIA-2021-PULL-THAT-UP-JAMIE
  -> official PTUJ HTML section "Geometric Unity for General Relativity & Gauge Theory"
  -> iframe src https://www.youtube.com/embed/TzSEvmqxu48?feature=oembed
  -> YouTube oEmbed title "Geometric Unity for General Relativity & Gauge Theory"
```

This is useful provenance. It confirms that the repo's target id and title are
stable against a current text fetch, and it confirms that the official PTUJ page
is the right source surface to query for this asset.

It does **not** construct `OfficialTzSEvmqxu48FormulaSourceAssetPacket_V1`.
The positive chain ends at locator metadata. It does not supply a source media
object, source package, source page with embedded immutable asset bytes, frame
sequence, sheet scan, formula-bearing still image, or checksummed asset locator.

## 4. The first exact obstruction or missing source object.

The first exact obstruction is:

```text
OfficialTzSEvmqxu48FormulaSourceAssetPacket_V1.source_asset_object
```

Expanded first missing object:

```text
An official or custodian-provided TzSEvmqxu48 source asset, source package,
source page asset, sheet scan/photo, or immutable asset locator with enough
source stability and content access to inspect formula-bearing material without
requiring the repo-local extractor/toolchain branch.
```

The inspected locators stop here:

| inspected object | why it stops |
| --- | --- |
| official PTUJ page | Exposes descriptive text and a YouTube iframe, not a direct source asset package. |
| YouTube embed URL | Normal iframe locator, not source bytes or immutable inspectable asset. |
| YouTube watch page | HTML playback page, not admitted source media or frame output. |
| YouTube oEmbed | Metadata receipt only. |
| YouTube thumbnail URL | Preview image endpoint only; not a formula source asset and not inspected as one. |

Therefore the first missing object is not a new downstream proof object. It is
the source object that would let this branch bypass local extraction in the
first place.

## 5. The constructive next object that would remove or test the obstruction.

The constructive next object is:

```text
OfficialTzSEvmqxu48FormulaSourceAssetPacket_V1.source_asset_object_manifest
```

Minimum admissible fields:

| field | required content |
| --- | --- |
| `custodian` | Official GU site, creator, archive, source-page maintainer, or other named custodian of the exact asset. |
| `asset_kind` | Source video package, source animation file, frame sequence, sheet scan/photo, or formula-bearing still/source page asset. |
| `immutable_locator` | Stable archive URL, content-addressed locator, versioned source package locator, or repo-local path if supplied lawfully. |
| `content_access` | A way to inspect the actual source content without treating normal webpage/watch/oEmbed/thumbnail metadata as the asset. |
| `checksums_or_custody_record` | SHA-256/size if bytes are present, or a source-custody record sufficient to request/obtain them. |
| `formula_visibility_scope` | Exact timecode, page asset, frame id, sheet id, or full-asset audit scope. |
| `target_import_guard` | Confirmation that DESI/dark-energy/selector outcomes did not select or normalize the asset. |

If this object is supplied, the PTUJ visibility audit can run from the official
branch without first constructing the local extractor manifest. If it is not
supplied, the next admissible route remains the local extractor/source-byte
manifest from Cycle 1.

## 6. What this means for PTUJ visibility audit, formula packet, and Keating identity.

| downstream object | consequence |
| --- | --- |
| PTUJ visibility audit | Not enabled. The current objects are locators and metadata, not inspectable source content. |
| `TzSEvmqxu48_FormulaBearingFrameOrSourceAssetPacket_V1` | Blocked before construction. No formula-bearing official source asset or decoded frame packet exists. |
| Keating identity | Not evaluable. There is still no source asset to compare to `KeatingRevealed_ShiabProjectionSheet_V1` or manuscript pages. |
| `SourceForcedCodomainSelectorForK_IG` / proof restart | Closed for this route. No PTUJ source packet, no Keating/source identity, and no family identity pass. |

This branch remains source-positive as a search direction: the official PTUJ
page is the right provenance surface and may lead to a custodian request. It is
not receipt-positive.

## 7. Next meaningful source computation step.

The next meaningful source computation is not another metadata fetch. It is a
custody/object query:

```text
Ask for or locate an official/custodian source package for the PTUJ visual aid
"Geometric Unity for General Relativity & Gauge Theory" with video id
TzSEvmqxu48, or an official still/sheet/source page asset for the Shiab
Projection segment, then record an immutable locator and checksum/custody
manifest.
```

If that fails, return to the local extractor branch and construct:

```text
LawfulLocalTzSEvmqxu48FrameExtractor_V1.toolchain_identity_and_output_manifest
```

That branch remains required unless the official/custodian source-asset object
is supplied.

## 8. Machine-readable JSON summary.

```json
{
  "artifact": "OfficialTzSEvmqxu48FormulaSourceAssetPacketDecision_1503_Cycle2_Lane1_V1",
  "artifact_id": "OfficialTzSEvmqxu48FormulaSourceAssetPacketDecision_1503_Cycle2_Lane1_V1",
  "run_id": "hourly-20260625-1503",
  "cycle": 2,
  "lane": 1,
  "verdict": "blocked",
  "verdict_class": "blocked",
  "owned_path": "explorations/hourly-20260625-1503-cycle2-ptuj-official-source-asset-branch.md",
  "companion_audit": "tests/hourly_20260625_1503_cycle2_ptuj_official_source_asset_branch_audit.py",
  "target_video_id": "TzSEvmqxu48",
  "target_asset_id": "PullThatUpJamie_GUForGRGaugeTheory_TzSEvmqxu48",
  "target_branch": "OfficialTzSEvmqxu48FormulaSourceAssetPacket_V1",
  "tested_branch_distinct_from_local_extractor": true,
  "local_extractor_branch": "LawfulLocalTzSEvmqxu48FrameExtractor_V1.toolchain_identity_and_output_manifest",
  "explicit_fields": {
    "official_asset_present": false,
    "custodian_source_asset_present": false,
    "locator_only_count": 5,
    "metadata_receipt_count": 4,
    "source_asset_packet_accepted": false,
    "local_extractor_required": true,
    "visibility_audit_enabled": false,
    "target_import_used": false,
    "proof_restart_allowed": false
  },
  "official_asset_present": false,
  "custodian_source_asset_present": false,
  "locator_only_count": 5,
  "metadata_receipt_count": 4,
  "source_asset_packet_accepted": false,
  "local_extractor_required": true,
  "visibility_audit_enabled": false,
  "target_import_used": false,
  "proof_restart_allowed": false,
  "claim_promotion_allowed": false,
  "accepted_receipt_count": 0,
  "accepted_formula_asset_count": 0,
  "source_safe_lookup_performed": true,
  "large_media_downloaded": false,
  "binary_asset_created": false,
  "source_safe_lookups": [
    {
      "check_id": "OFFICIAL_PTUJ_HTML_1503_C2_L1",
      "locator": "https://geometricunity.org/pull-that-up-jamie/",
      "method": "text_html_fetch_and_pattern_check",
      "observed": "http_200_html_length_72505_contains_TzSEvmqxu48_youtube_iframe_shiab_geometric_unity_for_general_relativity",
      "accepted_as_source_asset": false,
      "object_class": "official_page_locator_and_description"
    },
    {
      "check_id": "OFFICIAL_PTUJ_SRC_PARSE_1503_C2_L1",
      "locator": "https://geometricunity.org/pull-that-up-jamie/",
      "method": "href_src_parse_for_media_or_asset_locators",
      "observed": "youtube_embed_TzSEvmqxu48_found_no_mp4_webm_m4v_mov_archive_or_source_package_url",
      "accepted_as_source_asset": false,
      "object_class": "embed_locator"
    },
    {
      "check_id": "YOUTUBE_OEMBED_1503_C2_L1",
      "locator": "https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v=TzSEvmqxu48&format=json",
      "method": "small_json_metadata_fetch",
      "observed": "http_200_title_author_iframe_thumbnail_url",
      "accepted_as_source_asset": false,
      "object_class": "metadata"
    },
    {
      "check_id": "YOUTUBE_WATCH_HEAD_1503_C2_L1",
      "locator": "https://www.youtube.com/watch?v=TzSEvmqxu48",
      "method": "head_request",
      "observed": "http_200_text_html",
      "accepted_as_source_asset": false,
      "object_class": "watch_page_locator"
    },
    {
      "check_id": "YOUTUBE_THUMBNAIL_HEAD_1503_C2_L1",
      "locator": "https://img.youtube.com/vi/TzSEvmqxu48/maxresdefault.jpg",
      "method": "head_request",
      "observed": "http_200_image_jpeg_content_length_54692",
      "accepted_as_source_asset": false,
      "object_class": "thumbnail_metadata"
    }
  ],
  "inspected_remote_locators": [
    "https://geometricunity.org/pull-that-up-jamie/",
    "https://www.youtube.com/embed/TzSEvmqxu48?feature=oembed",
    "https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v=TzSEvmqxu48&format=json",
    "https://www.youtube.com/watch?v=TzSEvmqxu48",
    "https://img.youtube.com/vi/TzSEvmqxu48/maxresdefault.jpg"
  ],
  "non_source_asset_objects": [
    "normal_webpage_link",
    "youtube_embed_iframe",
    "youtube_watch_page",
    "youtube_oembed_json",
    "youtube_thumbnail",
    "caption_or_page_description",
    "metadata",
    "locator_only"
  ],
  "first_exact_obstruction": {
    "id": "OfficialTzSEvmqxu48FormulaSourceAssetPacket_V1.source_asset_object",
    "description": "No official or custodian-provided source asset, source package, source page asset, sheet scan/photo, or immutable inspectable asset locator was found.",
    "missing_object": "official_or_custodian_TzSEvmqxu48_source_asset_with_content_access_and_checksum_or_custody_record"
  },
  "constructive_next_object": {
    "id": "OfficialTzSEvmqxu48FormulaSourceAssetPacket_V1.source_asset_object_manifest",
    "would_bypass_local_extractor_requirement": true,
    "required_fields": [
      "custodian",
      "asset_kind",
      "immutable_locator",
      "content_access",
      "checksums_or_custody_record",
      "formula_visibility_scope",
      "target_import_guard"
    ]
  },
  "ptuj_visibility_audit": {
    "enabled": false,
    "blocked_by": "no_inspectable_official_or_custodian_source_asset",
    "enabled_if_official_source_asset_manifest_exists": true,
    "enabled_if_local_extractor_manifest_exists": true
  },
  "formula_packet_status": "blocked_before_construction",
  "keating_identity_status": "not_evaluable_without_ptuj_formula_source_asset_or_frame_packet",
  "ig_selector_route_status": "closed_no_ptuj_source_packet_or_keating_identity",
  "target_import_guard": {
    "target_import_used": false,
    "target_data_seen": [],
    "target_outcome_used_to_select_or_normalize_source_object": false
  },
  "forbidden_promotions": {
    "normal_webpage_link_as_formula_source_asset": false,
    "youtube_watch_page_as_formula_source_asset": false,
    "youtube_oembed_as_formula_source_asset": false,
    "caption_as_formula_source_asset": false,
    "thumbnail_as_formula_source_asset": false,
    "storyboard_as_formula_source_asset": false,
    "metadata_as_formula_source_asset": false,
    "locator_only_as_source_bytes": false,
    "proof_restart": false
  },
  "next_meaningful_source_computation_step": "locate_or_request_official_custodian_source_package_or_formula_bearing_still_sheet_asset_for_TzSEvmqxu48_then_record_immutable_locator_checksum_or_custody_manifest"
}
```
