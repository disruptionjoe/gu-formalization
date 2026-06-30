---
title: "Hourly 20260626 1102 Cycle 1 ProductAB One Branch Payload Acquisition"
date: "2026-06-26"
run_id: "hourly-20260626-1102"
cycle: 1
lane: 4
doc_type: "frontier_run_lane_artifact"
artifact_id: "OneBranchFormulaBearingPTUJOrKeatingPayloadAcquisition_1102_C1_L4_V1"
verdict: "closed_scoped_negative_no_one_branch_payload_present_after_public_check"
owned_path: "explorations/hourly-20260626-1102-cycle1-productab-one-branch-payload-acquisition.md"
claim_status_change: false
---

# Hourly 20260626 1102 Cycle 1 ProductAB One Branch Payload Acquisition

## 1. Verdict

Verdict: **closed scoped negative / no one-branch payload present**.

This lane attempted `OneBranchFormulaBearingPTUJOrKeatingPayload_V1` against the
current repo-local corpus and against easily attributable public pages without
downloading large media. The public checks sharpen the official PTUJ and Keating
locators, but they do not instantiate any accepted branch:

| branch | acquisition decision |
|---|---|
| `official_ptuj` | locator/caption/oEmbed only; no official formula-bearing source packet |
| `lawful_local_ptuj` | no repo-local or newly acquired source bytes, extractor, output manifest, or checksums |
| `keating_sheet` | transcript locates a missing representation-theory sheet; no sheet package or scan |

No visible formula transcription is allowed, no ProductAB member is emitted, and
no `K_IG` restart is allowed from this route.

Decision state:

```text
payload_attempted: true
one_branch_payload_present: false
official_ptuj_packet_present: false
lawful_local_ptuj_extractor_present: false
keating_sheet_package_present: false
visible_formula_transcription_allowed: false
productab_member_emitted: false
productab_kig_restart_allowed: false
target_import_used: false
claim_status_change: false
```

## 2. What Was Derived Directly From Repo/Public Sources

Repo source discipline:

| source | direct consequence |
|---|---|
| `RESEARCH-POSTURE.md` | Locators, compatibility, captions, and target behavior cannot be inflated into source evidence. |
| `process/runbooks/five-lane-frontier-run.md` | The lane must decide the first missing object and avoid status changes. |
| `explorations/hourly-20260626-1003-cycle3-productab-one-branch-payload-decision.md` | The prior repo-local decision had zero accepted branches and named the three branch objects. |
| `explorations/hourly-20260626-1003-cycle2-productab-branch-pure-accepted-payload-verifier.md` | Acceptance requires exactly one complete branch with source/content bytes or sheet package, custody/checksum, visibility scope, and anti-target-import guard. |
| `explorations/hourly-20260626-1003-cycle1-productab-formula-bearing-source-asset-gate.md` | The first obstruction was `content_access_or_source_bytes_missing`. |
| `explorations/hourly-20260626-0904-cycle3-productab-formula-visibility-prereq.md` | Formula visibility is disallowed before content/source bytes, checksum/custody, decode manifest if local, and bounded scope. |
| `sources/media-index.md` | PTUJ and Keating entries are provenance maps, not proof objects; PTUJ is metadata-checked, Keating surfaces need timestamp/source mining before technical use. |

Repo-local checks in this lane:

| check | result |
|---|---|
| owned output precheck | assigned file was absent before this lane wrote it |
| `sources/` inventory | markdown ledgers only; no media/source-byte/sheet package |
| exact and fuzzy file search for PTUJ, `TzSEvmqxu48`, Keating, `fBozSSLxFvI`, Shiab, projection, and ProductAB packet names | prior artifacts/tests and one policy-only RS evidence directory; no accepted payload file |
| `automation/evidence/hourly-20260625-2202-rs-fbozsslxfvi/README.md` | directory policy only, `persisted_frame_count: 0`; not a PTUJ/ProductAB payload |

Public checks in this lane:

| public surface | derived object | why it is not a payload |
|---|---|---|
| `https://geometricunity.org/pull-that-up-jamie/` | Official PTUJ collection page. It identifies the videos as visual aids and the `Geometric Unity for General Relativity & Gauge Theory` entry describes a `Shiab Projection` operation. HTML inspection found the embedded YouTube id `TzSEvmqxu48`. | It is a locator/caption page. It does not provide source bytes, frame checksums, a decoded output manifest, or a formula-bearing packet. |
| YouTube oEmbed for `TzSEvmqxu48` | Title `Geometric Unity for General Relativity & Gauge Theory`, author `The Portal Clips`, thumbnail URL, and iframe embed metadata. | oEmbed is metadata only; thumbnail/embed HTML is not a formula-bearing source packet. |
| Apple Podcasts page for `Eric Weinstein: Geometric Unity...REVEALED! Part 1` | Published 2021-04-09, length 59 minutes, episode 135, show description links to GeometricUnity.org and `pullthatupjamie.com`; page exposes audio enclosure metadata. | Podcast metadata/audio locator is not a Keating sheet scan/source package and does not provide formula-bearing sheet fields. |
| The Portal Group transcript for the Keating conversation | At `01:41:43` to `01:42:50`, the transcript says the Shiab operator is one of the objects Weinstein is still trying to locate and describes old representation-theory calculations on perforated printer paper with yellow highlighter. | This is a strong missing-object locator. It explicitly does not supply the sheet, source package, formula image, or checksum/custody object. |
| Search queries for exact `TzSEvmqxu48`, `Shiab Projection`, and Keating sheet/source terms | Returned PTUJ page, Apple/Portal metadata/transcript surfaces, YouTube pages, and secondary discussions. | No result supplied an official packet, local source bytes, extractor manifest, or sheet package. |

No large media was downloaded. The only public fetches were HTML/oEmbed/metadata
and search-result pages.

## 3. Branch Acquisition Table

| branch | strongest branch-pure acquisition attempted | fields present | first missing accepting field | branch accepted |
|---|---|---|---|---|
| `official_ptuj` | Official PTUJ page plus `TzSEvmqxu48` oEmbed metadata | source id, official page locator, embed locator, caption naming Shiab Projection, video title/channel metadata | `OfficialTzSEvmqxu48FormulaSourceAssetPacket_V1.formula_bearing_source_asset_or_content_bytes` | false |
| `lawful_local_ptuj` | Repo-local source/extractor search only; no media download attempted | prior schema names and negative receipts | `LawfulLocalTzSEvmqxu48FrameExtractor_V1.source_byte_object` plus checksum/decode/output manifest | false |
| `keating_sheet` | Apple metadata plus Portal Group transcript missing-sheet window | episode identity, timestamped missing-sheet locator, description of representation-theory projection calculations | `KeatingRevealed_ShiabProjectionSheet_V1.source_package_or_sheet_scan` | false |

Accepted branch count:

```text
accepted_branch_count: 0
```

## 4. Strongest Positive Construction Attempt

The strongest branch-pure construction is an `official_ptuj` locator packet:

```text
OfficialTzSEvmqxu48FormulaSourceAssetLocator_V1 := {
  branch_id: "official_ptuj",
  public_page: "https://geometricunity.org/pull-that-up-jamie/",
  official_page_status: "http_200",
  page_role: "collection_of_visual_aids_for_GU",
  entry_title: "Geometric Unity for General Relativity & Gauge Theory",
  video_id: "TzSEvmqxu48",
  embed_url: "https://www.youtube.com/embed/TzSEvmqxu48?feature=oembed",
  oembed_title: "Geometric Unity for General Relativity & Gauge Theory",
  oembed_author: "The Portal Clips",
  caption_result: "names Shiab Projection operation in GR/gauge-theory compatibility context",
  no_cross_branch_assembly: true,
  target_import_used: false
}
```

Applying the accepted-payload verifier rejects this object:

```text
accepted_branch_payload(locator_packet) = false
```

Reason: it is not a formula-bearing payload. It does not contain source bytes,
decoded frames, frame checksums, output manifests, an official still/source
asset package, bounded formula visibility, or a visible formula/projection-rule
object. The public Keating transcript was not merged into this packet because
that would assemble across branches.

The strongest `keating_sheet` construction is also non-accepting: the transcript
locates the missing sheet and describes it, but the sheet itself is absent.

## 5. First Exact Obstruction Or Missing Object

Global first obstruction:

```text
OneBranchFormulaBearingPTUJOrKeatingPayload_V1.accepted_branch_payload
has no accepting branch because no branch-local formula-bearing content/source
object or Keating sheet package is present.
```

Branch-local first missing objects:

| branch | first exact missing object |
|---|---|
| `official_ptuj` | `OfficialTzSEvmqxu48FormulaSourceAssetPacket_V1.formula_bearing_source_asset_or_content_bytes` |
| `lawful_local_ptuj` | `LawfulLocalTzSEvmqxu48FrameExtractor_V1.source_byte_object` |
| `keating_sheet` | `KeatingRevealed_ShiabProjectionSheet_V1.source_package_or_sheet_scan` |

Downstream fields such as formula visibility scope, transcription, ProductAB
identity, and `K_IG` restart are not evaluated because the payload fails at
branch materialization.

## 6. Constructive Next Object

The cleanest next object is a branch-pure official PTUJ packet, because the
official page already identifies `TzSEvmqxu48`:

```text
OfficialTzSEvmqxu48FormulaSourceAssetPacket_V1 := {
  branch_id: "official_ptuj",
  source_id: "GU-MEDIA-2021-PULL-THAT-UP-JAMIE",
  video_id: "TzSEvmqxu48",
  official_or_custodian_asset_record,
  formula_bearing_source_asset_or_content_bytes,
  checksum_or_custody_record,
  frame_or_asset_scope,
  decode_output_manifest_if_video_source_is_local,
  output_checksums_if_decoded,
  formula_visibility_scope,
  anti_target_import_guard
}
```

Equivalent acceptable next objects remain:

```text
LawfulLocalTzSEvmqxu48FrameExtractor_V1
KeatingRevealed_ShiabProjectionSheet_V1
```

Only one branch should be supplied. A packet that combines PTUJ page identity,
Keating transcript language, manuscript formulas, Oxford stills, and ProductAB
target behavior remains invalid.

## 7. Meaning For ProductAB/K_IG Claims

ProductAB and `K_IG` claims do not advance.

Permitted state:

```text
visible_formula_transcription_allowed: false
productab_member_emitted: false
productab_kig_restart_allowed: false
claim_status_change: false
```

This is not a global disproof of PTUJ, Keating, ProductAB, Shiab, or `K_IG`. It
is a provenance lock: the repo and checked public pages still do not admit a
formula-bearing one-branch payload. ProductAB source/member tests remain
sequentially downstream of that acquisition.

## 8. Terrain Classification, Forbidden Shortcut, Invariant, Kill Condition

Terrain classification:

```text
provenance-verifier
```

Downstream terrain remains locked:

```text
formula_visibility_after_one_branch_payload
ProductAB_identity_after_visible_transcription
K_IG_restart_after_ProductAB_member_receipt
```

Forbidden shortcut:

```text
Do not treat PTUJ locators, captions, iframe HTML, thumbnails, oEmbed metadata,
podcast metadata, transcript descriptions of a missing sheet, manuscript
formulas, Oxford stills, ProductAB target behavior, alpha/beta coefficients,
chirality, anomaly cancellation, generation count, dark-energy behavior, or
K_IG usefulness as the missing branch payload.
```

Invariant:

```text
Exactly one branch must carry a formula-bearing source/content object or sheet
package, checksum or custody, decode/output manifest if local, bounded formula
visibility scope, and anti-target-import guard before transcription or ProductAB
member selection.
```

Kill condition:

```text
Reject the payload if it is cross-branch assembled, if acceptance depends on
ProductAB/K_IG target behavior, or if a complete accepted branch has no visible
formula/projection rule in its declared scope.
```

## 9. Certificate/Witness Shape

| field | required content |
|---|---|
| public inputs | selected branch id; source id; stable locator/path; custody or lawful acquisition basis; checksum algorithm; decoder/extractor identity if local |
| witness | official source asset, source bytes, decoded frame outputs, or Keating sheet package; checksums; bounded timestamp/frame/page/sheet region; visible formula/projection rows or explicit absence rows |
| verifier predicate | exactly-one-branch purity; checksum/custody verification; decode reproducibility if local; bounded formula visibility; no cross-branch assembly; anti-target-import guard |
| semantic lift | permission to run visible formula transcription and then ProductAB source/member/identity tests |
| anti-smuggling guard | fail if any field is selected, normalized, completed, or accepted using ProductAB target row action, alpha/beta coefficients, chirality, anomaly cancellation, generation count, dark-energy behavior, or `K_IG` usefulness |
| negative receipt | branch attempted; first missing object; missing field list; strongest positive repo/public evidence; reason metadata/descriptive surfaces do not satisfy payload acceptance |

## 10. JSON Summary

```json
{
  "artifact_id": "OneBranchFormulaBearingPTUJOrKeatingPayloadAcquisition_1102_C1_L4_V1",
  "run_id": "hourly-20260626-1102",
  "cycle": 1,
  "lane": 4,
  "artifact_path": "explorations/hourly-20260626-1102-cycle1-productab-one-branch-payload-acquisition.md",
  "verdict": "closed_scoped_negative_no_one_branch_payload_present_after_public_check",
  "payload_attempted": true,
  "one_branch_payload_present": false,
  "official_ptuj_packet_present": false,
  "lawful_local_ptuj_extractor_present": false,
  "keating_sheet_package_present": false,
  "visible_formula_transcription_allowed": false,
  "productab_member_emitted": false,
  "productab_kig_restart_allowed": false,
  "target_import_used": false,
  "claim_status_change": false,
  "accepted_branch_count": 0,
  "public_web_checked": true,
  "large_media_downloaded": false,
  "official_ptuj_public_locator_present": true,
  "official_ptuj_video_id": "TzSEvmqxu48",
  "official_ptuj_first_missing_object": "OfficialTzSEvmqxu48FormulaSourceAssetPacket_V1.formula_bearing_source_asset_or_content_bytes",
  "lawful_local_ptuj_first_missing_object": "LawfulLocalTzSEvmqxu48FrameExtractor_V1.source_byte_object",
  "keating_sheet_first_missing_object": "KeatingRevealed_ShiabProjectionSheet_V1.source_package_or_sheet_scan",
  "first_exact_obstruction": "OneBranchFormulaBearingPTUJOrKeatingPayload_V1.accepted_branch_payload.branch_local_formula_bearing_content_or_sheet_package_absent",
  "constructive_next_object": "OfficialTzSEvmqxu48FormulaSourceAssetPacket_V1_or_one_equivalent_branch_pure_payload",
  "terrain": "provenance-verifier",
  "forbidden_shortcut": "locator_caption_metadata_transcript_description_or_target_behavior_as_payload",
  "invariant": "exactly_one_branch_with_formula_bearing_source_content_or_sheet_package_checksum_or_custody_decode_manifest_if_local_visibility_scope_and_anti_target_import_guard",
  "kill_condition": "reject_if_cross_branch_assembled_target_selected_or_complete_branch_has_no_visible_formula_or_projection_rule"
}
```
