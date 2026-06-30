---
title: "Hourly 20260626 1102 Cycle 2 ProductAB Official PTUJ Packet Verifier"
date: "2026-06-26"
run_id: "hourly-20260626-1102"
cycle: 2
lane: 4
doc_type: "frontier_run_lane_artifact"
artifact_id: "OfficialTzSEvmqxu48FormulaSourceAssetPacketVerifier_1102_C2_L4_V1"
verdict: "negative_official_ptuj_locator_present_packet_absent"
owned_path: "explorations/hourly-20260626-1102-cycle2-productab-official-ptuj-packet-verifier.md"
claim_status_change: false
---

# Hourly 20260626 1102 Cycle 2 ProductAB Official PTUJ Packet Verifier

## 1. Verdict

Verdict: **blocked / negative official-packet receipt**.

This lane defines and applies:

```text
OfficialTzSEvmqxu48FormulaSourceAssetPacketVerifier_V1
```

The verifier accepts only an official-branch packet that converts the known
Pull That Up Jamie locator into a formula-bearing source asset packet. Applying
it to the current repo state and to the cycle-1 public locator evidence rejects
the candidate:

```text
official_ptuj_locator_present: true
official_ptuj_packet_present: false
formula_bearing_source_asset_present: false
```

The first exact failing field is:

```text
OfficialTzSEvmqxu48FormulaSourceAssetPacket_V1.formula_bearing_source_asset_or_content_bytes
```

The locator `TzSEvmqxu48`, the official PTUJ page identity, captions, oEmbed
metadata, thumbnails, watch/embed URLs, and prior ProductAB/K_IG motivation do
not satisfy this field. No visible formula transcription is allowed, no
ProductAB member is emitted, and no ProductAB-driven `K_IG` restart is allowed.

## 2. What Was Derived Directly From Repo/Public Sources

Repo-derived constraints:

| source | direct consequence |
|---|---|
| `RESEARCH-POSTURE.md` | Source evidence cannot be replaced by compatibility, target behavior, or optimism. Hidden target import is forbidden. |
| `process/runbooks/five-lane-frontier-run.md` | The lane must make a decision-grade artifact, identify the first missing object, and avoid claim-status inflation. |
| `explorations/hourly-20260626-1003-cycle2-productab-branch-pure-accepted-payload-verifier.md` | A PTUJ/Keating payload requires branch-local content/source bytes or a source package, checksum/custody, bounded visibility, and anti-target-import guard. |
| `explorations/hourly-20260626-1003-cycle3-productab-one-branch-payload-decision.md` | The prior repo-local decision had zero accepted branches and kept ProductAB and `K_IG` locked. |
| `explorations/hourly-20260626-1102-cycle1-productab-one-branch-payload-acquisition.md` | Cycle 1 established the official PTUJ locator `TzSEvmqxu48` and rejected it as locator/caption/oEmbed only, with no formula-bearing payload. |
| `sources/media-index.md` | `GU-MEDIA-2021-PULL-THAT-UP-JAMIE` is a provenance map entry, metadata-checked only; it is not proof or a source-byte packet. |

Cycle-1 public locator evidence consumed, without rerunning broad acquisition:

| public surface reported by cycle 1 | admitted here | not admitted here |
|---|---|---|
| Official PTUJ page `https://geometricunity.org/pull-that-up-jamie/` | Official page locator; PTUJ collection role; embedded YouTube id `TzSEvmqxu48`; caption naming Shiab Projection in the GR/gauge-theory visual context. | Formula-bearing source asset bytes, frame checksums, decoded frame manifest, visibility scope, or official source packet. |
| YouTube oEmbed for `TzSEvmqxu48` | Title, author/channel, thumbnail URL, iframe/embed metadata. | Formula-bearing source content; reproducible source bytes; custody/checksum object. |
| Prior repo-local file and source inventory checks | Historical packet contracts and negative receipts only. | Current accepted official packet or source asset object. |

Current repo-state checks in this lane:

| check | result |
|---|---|
| assigned output precheck | file was absent before this lane wrote it |
| `sources/` inventory | markdown ledgers only; no media/source-byte/still/sheet/source package |
| targeted search for `OfficialTzSEvmqxu48FormulaSourceAssetPacket`, `TzSEvmqxu48`, formula-source fields, checksum/custody, and visibility terms | prior artifacts/tests/ledgers only; no accepted packet object |
| broad filename scan for PTUJ, `TzSEvmqxu48`, source bytes, manifests, checksums, frames, stills, sheets, and Keating terms | historical artifacts/tests plus one unrelated RS evidence policy directory; no official PTUJ source asset packet |

## 3. Packet Verifier Predicate And Field Table

Definition:

```text
OfficialTzSEvmqxu48FormulaSourceAssetPacketVerifier_V1(P, E) accepts iff
  identity_fields_accept(P, E)
  and official_branch_purity_accepts(P)
  and formula_source_asset_accepts(P)
  and checksum_or_custody_accepts(P)
  and decode_requirements_accept(P)
  and visibility_scope_accepts(P)
  and anti_smuggling_accepts(P).
```

The field order is intentional. The locator fields are checked first because
cycle 1 already supplies them. The first missing field after locator identity is
the formula-bearing source asset/content object. Downstream checksum, decode,
and visibility predicates remain required for any future packet, but are not
used to rescue a missing source asset.

Required field table:

| order | field | required value | acceptance predicate | current status |
|---:|---|---|---|---|
| F01 | `schema_id` | `OfficialTzSEvmqxu48FormulaSourceAssetPacket_V1` | Exact schema id, not a generic PTUJ note. | absent in current packet because no packet exists; verifier can still evaluate locator evidence as candidate input |
| F02 | `branch_id` | `official_ptuj` | Exactly one branch; no lawful-local or Keating fields. | present as intended branch for this lane |
| F03 | `source_id` | `GU-MEDIA-2021-PULL-THAT-UP-JAMIE` | Matches `sources/media-index.md` PTUJ entry. | present as locator identity |
| F04 | `official_locator_evidence` | Official PTUJ page locator plus `video_id: TzSEvmqxu48`; oEmbed/embed metadata may be attached as locator evidence. | Locator must identify the official PTUJ item and the video id; metadata remains metadata. | present from cycle-1 evidence |
| F05 | `formula_bearing_source_asset_or_content_bytes` | Official/custodian asset package, still/frame source asset, source-byte object, or equivalent content-access object for `TzSEvmqxu48` that could contain a visible formula/projection rule. | Must be content-bearing, branch-local, immutable enough for custody/hash, and not merely a page, caption, iframe, thumbnail URL, oEmbed JSON, transcript description, manuscript formula, or target behavior. | **first failure: missing** |
| F06 | `asset_kind_and_scope` | Declared kind such as official source video bytes, official still package, official frame export, or custodian source package, with bounded timestamp/frame/page/sheet scope. | Scope must be attached to the F05 asset, not borrowed from another branch or manuscript. | not evaluated because F05 fails |
| F07 | `checksum_or_custody_record` | SHA-256 or stronger hash for bytes/outputs, or a concrete official/custodian custody record that identifies the exact asset version. | Verifier recomputes checksums when bytes are local; custody records must bind exact asset identity, source, date/version if available, and locator/path. | not evaluated because F05 fails |
| F08 | `decode_manifest_if_local_or_video_source` | Decoder/extractor identity, version, command/options, decode scope, output manifest, output checksums, dimensions, and frame/timestamp mapping. | Required for local source bytes or decoded frames; not needed only if the official packet itself is a still/sheet/source package with direct content and custody. | not evaluated because F05 fails |
| F09 | `formula_visibility_scope` | Bounded frame/timestamp/region/page/sheet statement saying where the formula or projection rule is visible, or an accepted explicit-absence statement after packet/decode acceptance. | Visibility must be inspected only after F05-F08 pass; it must not cite manuscript/Oxford/Keating text as if visible inside `TzSEvmqxu48`. | not evaluated because F05 fails |
| F10 | `visible_formula_transcription_payload` | Optional downstream transcription of visible formula/rule rows from F09. | Allowed only after packet acceptance through F09; not part of locator admission. | disallowed |
| F11 | `anti_target_import_guard` | Declaration and audit receipt that no field was selected, normalized, completed, or accepted using ProductAB target row action, alpha/beta coefficients, chirality, anomaly cancellation, generation count, dark-energy behavior, or `K_IG` usefulness. | Fails on target selection, cross-branch assembly, or backfilling formula identity from downstream behavior. | currently clean only because no formula/member selection was run |

Acceptance predicate:

```text
accept(P) =
  P.F01 == OfficialTzSEvmqxu48FormulaSourceAssetPacket_V1
  and P.F02 == official_ptuj
  and P.F03 == GU-MEDIA-2021-PULL-THAT-UP-JAMIE
  and P.F04.video_id == TzSEvmqxu48
  and content_bearing(P.F05)
  and branch_local(P.F05, P.F02)
  and asset_scope_bound(P.F06, P.F05)
  and checksum_or_custody_bound(P.F07, P.F05)
  and decode_reproducible_or_not_needed(P.F08, P.F05)
  and visibility_scope_bound(P.F09, P.F05, P.F08)
  and no_visible_transcription_before_acceptance(P.F10)
  and anti_target_import_guard(P.F11).
```

Rejection predicates:

```text
reject(P) if F05 is absent.
reject(P) if F05 is only locator/caption/oEmbed/embed/watch-page/thumbnail metadata.
reject(P) if F05 is a formula from manuscript, Oxford, Keating, or target behavior.
reject(P) if any required field is assembled across official, lawful-local, and Keating branches.
reject(P) if checksum/custody does not bind the same asset as F05.
reject(P) if local decode outputs lack reproducible manifest/checksums.
reject(P) if visibility scope is unbounded or points outside the accepted asset.
reject(P) if ProductAB or `K_IG` target success influences field selection.
```

## 4. Application To Current Evidence

Candidate assembled only from current admissible evidence:

```text
OfficialTzSEvmqxu48FormulaSourceAssetLocator_V1 := {
  branch_id: "official_ptuj",
  source_id: "GU-MEDIA-2021-PULL-THAT-UP-JAMIE",
  official_page_locator: "https://geometricunity.org/pull-that-up-jamie/",
  page_role: "official visual-aid collection",
  video_id: "TzSEvmqxu48",
  oembed_title: "Geometric Unity for General Relativity & Gauge Theory",
  oembed_author: "The Portal Clips",
  caption_role: "Shiab Projection visual locator",
  target_import_used: false,
  no_cross_branch_assembly: true
}
```

Verifier application:

| field | candidate value | decision |
|---|---|---|
| F01 `schema_id` | locator object only, not packet object | not a complete packet; continue only to locate first content failure |
| F02 `branch_id` | `official_ptuj` | pass for branch choice |
| F03 `source_id` | `GU-MEDIA-2021-PULL-THAT-UP-JAMIE` | pass for source identity |
| F04 `official_locator_evidence` | official PTUJ page plus `TzSEvmqxu48` locator/oEmbed metadata from cycle 1 | pass as locator evidence |
| F05 `formula_bearing_source_asset_or_content_bytes` | no official/custodian formula-bearing asset, source bytes, still package, decoded frame package, or content-access object in current repo/cycle-1 locator evidence | **fail** |

The verifier stops at F05. It does not evaluate F06-F10 as live satisfied
fields, because there is no asset to checksum, decode, scope, or transcribe.

Current decision:

```text
OfficialTzSEvmqxu48FormulaSourceAssetPacketVerifier_V1(candidate) = reject
first_failed_field = F05.formula_bearing_source_asset_or_content_bytes
```

## 5. First Exact Obstruction Or Missing Object

First exact obstruction:

```text
OfficialTzSEvmqxu48FormulaSourceAssetPacket_V1.formula_bearing_source_asset_or_content_bytes
is absent.
```

This is narrower than the earlier one-branch obstruction. The official locator
is present, so the missing object is not another locator and not another search
summary. It is the content-bearing official packet field that turns the locator
into a packet.

Downstream missing fields remain real but secondary:

```text
checksum_or_custody_record: blocked by missing F05
decode_output_manifest_if_video_source_is_local: blocked by missing F05
formula_visibility_scope: blocked by missing F05-F08
visible_formula_transcription_payload: disallowed
ProductAB_member: disallowed
ProductAB_K_IG_restart: disallowed
```

## 6. Constructive Next Object

Acquire exactly this next object:

```text
OfficialTzSEvmqxu48FormulaSourceAssetPacket_V1.formula_bearing_source_asset_or_content_bytes
```

The object must be official-branch and content-bearing. Acceptable examples:

```text
official/custodian source video bytes for TzSEvmqxu48 with exact custody/hash
official/custodian still or frame package from TzSEvmqxu48 with exact custody/hash
official source asset package containing the Shiab Projection visual with exact custody/hash
```

Minimum packet shape for the next acquisition:

```text
OfficialTzSEvmqxu48FormulaSourceAssetPacket_V1 := {
  schema_id: "OfficialTzSEvmqxu48FormulaSourceAssetPacket_V1",
  branch_id: "official_ptuj",
  source_id: "GU-MEDIA-2021-PULL-THAT-UP-JAMIE",
  video_id: "TzSEvmqxu48",
  official_locator_evidence,
  formula_bearing_source_asset_or_content_bytes,
  asset_kind_and_scope,
  checksum_or_custody_record,
  decode_manifest_if_local_or_video_source,
  formula_visibility_scope,
  anti_target_import_guard
}
```

Do not substitute a lawful-local extractor, Keating sheet locator, manuscript
formula, Oxford still, target ProductAB behavior, or `K_IG` usefulness for this
official object. Those are different branches or downstream tests.

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

This is not a global disproof of PTUJ, Shiab Projection, ProductAB, or `K_IG`.
It is a provenance decision. The repo can say that an official PTUJ locator
exists, but it cannot say that an official PTUJ formula-bearing packet exists.
Therefore no visible formula, ProductAB member, ProductAB-to-Oxford identity
claim, or `K_IG` restart may be promoted from this route.

## 8. Terrain Classification, Forbidden Shortcut, Invariant, Kill Condition

Terrain:

```text
provenance-verifier
```

Forbidden shortcut:

```text
Do not treat official page locators, captions, embed URLs, oEmbed JSON,
thumbnails, watch-page/player metadata, transcript descriptions, manuscript
formulas, Oxford stills, ProductAB target behavior, alpha/beta coefficients,
chirality, anomaly cancellation, generation count, dark-energy behavior, or
K_IG usefulness as the official TzSEvmqxu48 formula source asset packet.
```

Invariant:

```text
The official PTUJ branch must carry its own formula-bearing source asset/content
object before checksum/custody, decode, visibility, transcription, ProductAB
member selection, or K_IG restart can run.
```

Kill condition:

```text
Reject the official packet if the accepted official asset has no visible
formula/projection rule in its declared scope, if the packet is assembled across
branches, or if any field is selected by downstream ProductAB/K_IG target
behavior.
```

## 9. Certificate/Witness Shape

| component | required content |
|---|---|
| public inputs | `branch_id: official_ptuj`; `source_id: GU-MEDIA-2021-PULL-THAT-UP-JAMIE`; `video_id: TzSEvmqxu48`; official PTUJ page locator; checksum algorithm; custody basis; decoder identity if local/video-derived |
| witness | official/custodian source asset bytes or official asset package; byte size/media type; immutable locator/path; checksum or custody record; decoded output manifest and output checksums if local; bounded frame/timestamp/region/page/sheet visibility scope |
| verifier predicate | official branch identity; formula-bearing content object presence; checksum/custody binding; decode reproducibility when applicable; bounded visibility; no cross-branch assembly; anti-target-import guard |
| semantic lift | only after acceptance, allow visible formula transcription; only after transcription, allow ProductAB identity/member tests; only after ProductAB receipt, reconsider any `K_IG` restart route |
| anti-smuggling guard | fail if any packet field is supplied from Keating sheet language, manuscript/Oxford formulas, lawful-local tooling, ProductAB target row action, alpha/beta coefficients, chirality, anomaly cancellation, generation count, dark-energy behavior, or `K_IG` usefulness |
| negative receipt | official locator present; first failed field `formula_bearing_source_asset_or_content_bytes`; no checksum/custody/decode/visibility evaluation; transcription/member/restart disallowed |

## 10. JSON Summary

```json
{
  "artifact_id": "OfficialTzSEvmqxu48FormulaSourceAssetPacketVerifier_1102_C2_L4_V1",
  "run_id": "hourly-20260626-1102",
  "cycle": 2,
  "lane": 4,
  "artifact_path": "explorations/hourly-20260626-1102-cycle2-productab-official-ptuj-packet-verifier.md",
  "verdict": "negative_official_ptuj_locator_present_packet_absent",
  "verifier_defined": true,
  "verifier_applied": true,
  "official_ptuj_locator_present": true,
  "official_ptuj_packet_present": false,
  "formula_bearing_source_asset_present": false,
  "source_bytes_or_official_asset_present": false,
  "checksum_or_custody_present": false,
  "formula_visibility_scope_present": false,
  "visible_formula_transcription_allowed": false,
  "productab_member_emitted": false,
  "productab_kig_restart_allowed": false,
  "target_import_used": false,
  "claim_status_change": false,
  "first_failed_field": "OfficialTzSEvmqxu48FormulaSourceAssetPacket_V1.formula_bearing_source_asset_or_content_bytes",
  "constructive_next_object": "OfficialTzSEvmqxu48FormulaSourceAssetPacket_V1.formula_bearing_source_asset_or_content_bytes",
  "terrain": "provenance-verifier",
  "forbidden_shortcut": "locator_caption_oembed_thumbnail_metadata_transcript_manuscript_oxford_or_target_behavior_as_official_formula_source_asset",
  "invariant": "official_ptuj_branch_requires_own_formula_bearing_source_asset_before_checksum_decode_visibility_transcription_productab_or_kig",
  "kill_condition": "reject_if_no_visible_formula_in_accepted_official_asset_or_if_cross_branch_or_target_selected"
}
```
