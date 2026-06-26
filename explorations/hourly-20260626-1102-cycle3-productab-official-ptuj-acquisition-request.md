---
title: "Hourly 20260626 1102 Cycle 3 ProductAB Official PTUJ Acquisition Request"
date: "2026-06-26"
run_id: "hourly-20260626-1102"
cycle: 3
lane: 4
doc_type: "frontier_run_lane_artifact"
artifact_id: "OfficialTzSEvmqxu48FormulaSourceAssetAcquisitionRequest_1102_C3_L4_V1"
verdict: "closed_request_defined_ready_missing_official_formula_source_asset"
owned_path: "explorations/hourly-20260626-1102-cycle3-productab-official-ptuj-acquisition-request.md"
claim_status_change: false
---

# Hourly 20260626 1102 Cycle 3 ProductAB Official PTUJ Acquisition Request

## 1. Verdict

Verdict: **closed request definition / acquisition still blocked at first source object**.

This lane defines the next-frontier request:

```text
OfficialTzSEvmqxu48FormulaSourceAssetAcquisitionRequest_V1
```

The request is decision-ready. It says exactly what must be acquired to move
from the official Pull That Up Jamie locator to an accepted official PTUJ
formula-source packet. It does not acquire new source material, download media,
transcribe a visible formula, emit a ProductAB member, or restart `K_IG`.

Current decision:

```text
official_ptuj_locator_present: true
acquisition_request_ready: true
accepted_official_ptuj_packet_present: false
first_missing_source_object:
  OfficialTzSEvmqxu48FormulaSourceAssetPacket_V1.formula_bearing_source_asset_or_content_bytes
visible_formula_transcription_allowed: false
productab_member_emitted: false
productab_kig_restart_allowed: false
claim_status_change: false
```

The immediate frontier is not another locator search. The first exact object to
acquire is the official/custodian formula-bearing source asset or equivalent
content bytes for `TzSEvmqxu48`, bound to custody or checksum.

## 2. What Was Derived Directly From Repo/Public Sources

No new web/source acquisition was performed in this cycle. The public-source
facts below are inherited only through the cycle-1 and cycle-2 artifacts.

| source | directly derived fact used here |
|---|---|
| `RESEARCH-POSTURE.md` | Compatibility, captions, target behavior, and optimism cannot replace a source witness. Hidden target import remains forbidden. |
| `process/runbooks/five-lane-frontier-run.md` | The lane must identify the exact missing object, keep claim status stable, and avoid turning hosted/compatible material into derivation. |
| `sources/media-index.md` | `GU-MEDIA-2021-PULL-THAT-UP-JAMIE` is a provenance-map entry for official visual aids, metadata-checked only, not proof or source bytes. |
| `explorations/hourly-20260626-1003-cycle3-productab-one-branch-payload-decision.md` | The repo-local one-branch payload gate had zero accepted branches and kept visible transcription, ProductAB, and `K_IG` locked. |
| `explorations/hourly-20260626-1102-cycle1-productab-one-branch-payload-acquisition.md` | Cycle 1 established the official PTUJ page locator, the embedded YouTube id `TzSEvmqxu48`, oEmbed/title/channel metadata, and the caption role; it also found no formula-bearing payload. |
| `explorations/hourly-20260626-1102-cycle2-productab-official-ptuj-packet-verifier.md` | Cycle 2 narrowed the official PTUJ failure to `formula_bearing_source_asset_or_content_bytes`; checksum, decode, visibility, transcription, ProductAB, and `K_IG` remain downstream. |

Known locator-level facts:

| field | status | source basis | admission limit |
|---|---|---|---|
| official PTUJ page | known | cycle-1 public locator evidence | locator only |
| `source_id` | known as `GU-MEDIA-2021-PULL-THAT-UP-JAMIE` | `sources/media-index.md` and cycle 1/2 | provenance map, not source asset |
| video id | known as `TzSEvmqxu48` | cycle-1 PTUJ/oEmbed evidence | identifies target media item only |
| title/channel/oEmbed metadata | known | cycle-1 public metadata | metadata only |
| caption role | known as Shiab Projection visual locator context | cycle-1 PTUJ page evidence | does not supply formula bytes or transcription |
| official packet content | missing | cycle-2 verifier | first failing field |

## 3. Acquisition Request Packet Fields And Known/Missing Table

Definition:

```text
OfficialTzSEvmqxu48FormulaSourceAssetAcquisitionRequest_V1 :=
  a branch-pure request for the first missing official PTUJ source object
  needed to instantiate
  OfficialTzSEvmqxu48FormulaSourceAssetPacket_V1.
```

The request is not itself the accepted packet. It is the exact acquisition
instruction for the missing packet field. It becomes successful only when the
requested source object arrives with custody/checksum and enough scope to run
the packet verifier.

Required request fields:

| order | field | required content | known/missing decision |
|---:|---|---|---|
| R01 | `request_schema_id` | `OfficialTzSEvmqxu48FormulaSourceAssetAcquisitionRequest_V1` | known by this artifact |
| R02 | `target_packet_schema_id` | `OfficialTzSEvmqxu48FormulaSourceAssetPacket_V1` | known from cycle 2 |
| R03 | `request_purpose` | acquire the first missing official PTUJ formula-bearing source object; do not transcribe or normalize formulas yet | known by this artifact |
| R04 | `branch_id` | exactly `official_ptuj` | known |
| R05 | `source_id` | `GU-MEDIA-2021-PULL-THAT-UP-JAMIE` | known |
| R06 | `official_locator` | official PTUJ page locator inherited from cycle 1 | known as locator |
| R07 | `video_id` | `TzSEvmqxu48` | known |
| R08 | `locator_metadata` | title, channel/author, embed/oEmbed, thumbnail, caption context, if attached | known but metadata only |
| R09 | `requested_packet_field` | `OfficialTzSEvmqxu48FormulaSourceAssetPacket_V1.formula_bearing_source_asset_or_content_bytes` | known as first missing field |
| R10 | `requested_source_object_kind` | one official/custodian content-bearing asset for `TzSEvmqxu48`: source video bytes, official still/frame export, official source asset package, or equivalent official content-access object | missing; this is the first source object to acquire |
| R11 | `asset_identity_binding` | immutable locator/path or custodian record binding the source object to `TzSEvmqxu48` and the official PTUJ branch | missing, downstream of R10 |
| R12 | `asset_scope` | declared media/page/sheet/frame/timestamp/region scope for the acquired object | missing, downstream of R10 |
| R13 | `checksum_or_custody_record` | SHA-256 or stronger checksum for bytes/exports, or a concrete official/custodian custody record identifying the exact asset version | missing, downstream of R10 |
| R14 | `decode_manifest_if_video_or_local` | decoder/extractor identity, version, command/options, frame/timestamp map, output manifest, dimensions, and output checksums if local decoding is needed | missing, conditional on R10 kind |
| R15 | `formula_visibility_scope_request` | ask only for bounded visibility coordinates after an accepted asset exists; frame/timestamp/region/page/sheet scope or explicit absence after inspection | missing; cannot be filled from locator metadata |
| R16 | `visible_formula_transcription_payload` | absent in the acquisition request | barred until R10-R15 are accepted |
| R17 | `anti_target_import_guard` | certify no field is selected, completed, normalized, or accepted using ProductAB row action, alpha/beta coefficients, chirality, anomaly cancellation, generation count, dark-energy behavior, or `K_IG` usefulness | required; currently clean because no formula/member selection occurs |
| R18 | `forbidden_substitutes` | page/caption/oEmbed/embed/thumbnail/transcript descriptions, manuscript/Oxford formulas, Keating sheet language, lawful-local tooling, ProductAB behavior, or `K_IG` utility cannot satisfy R10 | known by this artifact |
| R19 | `acceptance_verifier` | apply `OfficialTzSEvmqxu48FormulaSourceAssetPacketVerifier_V1` after R10-R15 arrive | known from cycle 2 |

Minimum successful acquisition response:

```text
OfficialTzSEvmqxu48FormulaBearingSourceObject_V1 := {
  branch_id: "official_ptuj",
  source_id: "GU-MEDIA-2021-PULL-THAT-UP-JAMIE",
  video_id: "TzSEvmqxu48",
  source_object_kind: one_of(
    "official_or_custodian_source_video_bytes",
    "official_or_custodian_still_or_frame_export",
    "official_source_asset_package",
    "official_equivalent_content_access_object"
  ),
  immutable_asset_locator_or_path,
  byte_size_or_package_description,
  media_type_or_package_type,
  exact_version_or_custody_basis,
  checksum_or_custody_record,
  declared_asset_scope,
  decode_manifest_if_needed,
  anti_target_import_guard
}
```

Reject the response if it supplies only metadata, only a locator, only a
thumbnail, only transcript prose, a cross-branch formula, or a ProductAB/`K_IG`
target-motivated reconstruction.

## 4. Strongest Positive Construction Attempt

The strongest construction available from cycle 1/2 is a filled acquisition
request whose identity and locator fields are known and whose source-object
field is explicitly missing:

```text
OfficialTzSEvmqxu48FormulaSourceAssetAcquisitionRequest_V1 := {
  request_schema_id: "OfficialTzSEvmqxu48FormulaSourceAssetAcquisitionRequest_V1",
  target_packet_schema_id: "OfficialTzSEvmqxu48FormulaSourceAssetPacket_V1",
  branch_id: "official_ptuj",
  source_id: "GU-MEDIA-2021-PULL-THAT-UP-JAMIE",
  official_locator: "https://geometricunity.org/pull-that-up-jamie/",
  video_id: "TzSEvmqxu48",
  locator_metadata_status: "present_locator_only",
  requested_packet_field:
    "formula_bearing_source_asset_or_content_bytes",
  requested_source_object_kind:
    "official_or_custodian_content_bearing_asset_for_TzSEvmqxu48",
  checksum_or_custody_required: true,
  formula_visibility_scope_required_after_asset_acceptance: true,
  visible_formula_transcription_payload: null,
  target_import_used: false,
  productab_member_emitted: false,
  productab_kig_restart_allowed: false
}
```

This is positive because it is now a precise, branch-pure request. It is not an
accepted packet because the requested source object has not been acquired.

The request can be applied immediately as a procurement/checklist artifact:

```text
request_identity_accepts: true
locator_fields_accept: true
first_requested_source_object_present: false
accepted_packet_can_be_emitted: false
```

## 5. First Exact Obstruction Or Missing Object

First exact obstruction:

```text
OfficialTzSEvmqxu48FormulaSourceAssetPacket_V1.formula_bearing_source_asset_or_content_bytes
is absent.
```

First exact source object to acquire next:

```text
OfficialTzSEvmqxu48FormulaBearingSourceObject_V1
```

where this object is the content-bearing realization of the packet field:

```text
OfficialTzSEvmqxu48FormulaSourceAssetPacket_V1.formula_bearing_source_asset_or_content_bytes
```

This object must be official-branch, content-bearing, and bound to custody or
checksum. It cannot be replaced by:

```text
PTUJ page locator
caption or visual-aid description
oEmbed or iframe metadata
thumbnail URL
YouTube watch/embed page metadata
Keating transcript language
manuscript/Oxford formula text
lawful-local extractor contract
ProductAB target row behavior
K_IG usefulness
```

Downstream missing objects remain real but are blocked behind the first source
object:

```text
asset_scope
checksum_or_custody_record
decode_manifest_if_video_or_local
formula_visibility_scope
visible_formula_transcription_payload
ProductAB_member
ProductAB_K_IG_restart
```

## 6. Constructive Next Object

Acquire exactly this object and nothing broader:

```text
OfficialTzSEvmqxu48FormulaBearingSourceObject_V1
```

Acquisition instruction:

| acquisition slot | required value |
|---|---|
| object id | `OfficialTzSEvmqxu48FormulaBearingSourceObject_V1` |
| packet field satisfied | `OfficialTzSEvmqxu48FormulaSourceAssetPacket_V1.formula_bearing_source_asset_or_content_bytes` |
| branch | `official_ptuj` only |
| source id | `GU-MEDIA-2021-PULL-THAT-UP-JAMIE` |
| media id | `TzSEvmqxu48` |
| acceptable contents | official/custodian video bytes, official/custodian still or frame export, official source asset package, or official equivalent content-access object |
| required binding | immutable path/locator or custodian record tying the exact object to the official PTUJ media item |
| required integrity | checksum for bytes/exports or custody record for official/custodian object |
| required scope | enough bounded media/frame/timestamp/region/page scope to test whether a formula/projection rule is visible |
| barred contents | any cross-branch formula or target-derived reconstruction |

The acquisition response should be submitted to the cycle-2 verifier, not to a
ProductAB normalizer. Only if the verifier accepts the official source object
may the repo proceed to visibility inspection and transcription.

## 7. Meaning For Visible Formula/ProductAB/K_IG Claims

The official PTUJ route remains before formula visibility.

Permitted state:

```text
visible_formula_transcription_allowed: false
productab_member_emitted: false
productab_kig_restart_allowed: false
target_import_used: false
claim_status_change: false
```

The repo may now say that the next acquisition request is defined and ready.
It may not say that the formula-bearing official source asset is present. It
may not infer a visible formula from the official page, caption, oEmbed,
thumbnail, manuscript, Oxford visual, Keating transcript, ProductAB target
behavior, or `K_IG` usefulness.

No ProductAB member can be emitted from this route until this sequence succeeds:

```text
official source object acquired
-> custody/checksum accepted
-> decode/manifest accepted if needed
-> bounded formula visibility scope accepted
-> visible transcription allowed
-> ProductAB identity/member tests allowed
-> ProductAB-to-K_IG restart reconsidered
```

## 8. Terrain Classification, Forbidden Shortcut, Invariant, Kill Condition

Terrain classification:

```text
provenance-acquisition-request
```

Downstream locked terrain:

```text
formula_visibility_after_official_source_asset
ProductAB_identity_after_visible_transcription
K_IG_restart_after_ProductAB_member_receipt
```

Forbidden shortcut:

```text
Do not treat a locator, caption, embed/oEmbed record, thumbnail, transcript
description, manuscript formula, Oxford still, Keating sheet description,
lawful-local extractor contract, ProductAB target behavior, alpha/beta
coefficient behavior, chirality, anomaly cancellation, generation count,
dark-energy behavior, or K_IG usefulness as the official TzSEvmqxu48 formula
source object.
```

Invariant:

```text
The official PTUJ branch must carry its own content-bearing source object for
TzSEvmqxu48 before checksum/custody, decode, visibility, transcription,
ProductAB member selection, or K_IG restart can run.
```

Kill condition:

```text
Reject the official PTUJ route if the acquired official object is only metadata,
cannot be bound to custody/checksum, is cross-branch assembled, is selected by
ProductAB/K_IG target behavior, or contains no visible formula/projection rule
inside its declared accepted scope.
```

## 9. Certificate/Witness Shape

| component | required content |
|---|---|
| public inputs | `request_schema_id`; `target_packet_schema_id`; `branch_id: official_ptuj`; `source_id: GU-MEDIA-2021-PULL-THAT-UP-JAMIE`; official PTUJ locator; `video_id: TzSEvmqxu48`; checksum algorithm; custody basis; decoder identity if needed |
| witness | official/custodian content-bearing source object; byte size or package description; media/package type; immutable locator/path or custodian record; checksum or custody record; declared asset scope; decode manifest and output checksums if local/video-derived |
| verifier predicate | request identity; official branch purity; source-object content bearing; binding to `TzSEvmqxu48`; checksum/custody binding; decode reproducibility when applicable; bounded visibility scope before transcription; no cross-branch assembly; anti-target-import guard |
| semantic lift | after packet acceptance, inspect formula visibility; after visibility, allow transcription; after transcription, run ProductAB identity/member tests; after ProductAB receipt, reconsider `K_IG` restart |
| anti-smuggling guard | fail if any field is filled from Keating sheet language, manuscript/Oxford formulas, lawful-local tooling, ProductAB target row action, alpha/beta coefficients, chirality, anomaly cancellation, generation count, dark-energy behavior, or `K_IG` usefulness |
| negative receipt | locator present; request ready; first source object absent; no checksum/custody/decode/visibility evaluation; visible transcription, ProductAB member, and `K_IG` restart disallowed |

## 10. JSON Summary

```json
{
  "artifact_id": "OfficialTzSEvmqxu48FormulaSourceAssetAcquisitionRequest_1102_C3_L4_V1",
  "request_schema_id": "OfficialTzSEvmqxu48FormulaSourceAssetAcquisitionRequest_V1",
  "run_id": "hourly-20260626-1102",
  "cycle": 3,
  "lane": 4,
  "artifact_path": "explorations/hourly-20260626-1102-cycle3-productab-official-ptuj-acquisition-request.md",
  "verdict": "closed_request_defined_ready_missing_official_formula_source_asset",
  "request_defined": true,
  "request_applied": true,
  "request_application_scope": "applied_to_cycle1_cycle2_locator_and_verifier_evidence_only",
  "external_source_acquisition_performed": false,
  "official_ptuj_locator_present": true,
  "acquisition_request_ready": true,
  "formula_bearing_source_asset_present": false,
  "source_bytes_or_official_asset_present": false,
  "checksum_or_custody_present": false,
  "formula_visibility_scope_present": false,
  "visible_formula_transcription_allowed": false,
  "productab_member_emitted": false,
  "productab_kig_restart_allowed": false,
  "target_import_used": false,
  "claim_status_change": false,
  "first_missing_source_object": "OfficialTzSEvmqxu48FormulaBearingSourceObject_V1",
  "first_missing_packet_field": "OfficialTzSEvmqxu48FormulaSourceAssetPacket_V1.formula_bearing_source_asset_or_content_bytes",
  "constructive_next_object": "OfficialTzSEvmqxu48FormulaBearingSourceObject_V1",
  "terrain": "provenance-acquisition-request",
  "forbidden_shortcut": "locator_caption_oembed_thumbnail_transcript_manuscript_oxford_keating_lawful_local_contract_or_target_behavior_as_official_formula_source_object",
  "invariant": "official_ptuj_branch_requires_own_content_bearing_source_object_for_TzSEvmqxu48_before_checksum_decode_visibility_transcription_productab_or_kig",
  "kill_condition": "reject_if_metadata_only_no_custody_or_checksum_cross_branch_target_selected_or_no_visible_formula_in_accepted_scope"
}
```
