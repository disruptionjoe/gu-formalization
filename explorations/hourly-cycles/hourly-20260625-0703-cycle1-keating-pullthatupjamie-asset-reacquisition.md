---
title: "Hourly 20260625 0703 Cycle 1 Keating Pull That Up Jamie Asset Reacquisition"
date: "2026-06-25"
run_id: "hourly-20260625-0703"
cycle: 1
lane: 2
doc_type: keating_pullthatupjamie_asset_reacquisition
artifact_id: "KeatingPullThatUpJamieShiabProjectionFormulaAssetPacketExecution_V1"
verdict: "BLOCKED_CAPTION_AND_MANUSCRIPT_FORMULA_ONLY_NO_EXECUTED_ASSET_RECEIPT"
owned_path: "explorations/hourly-20260625-0703-cycle1-keating-pullthatupjamie-asset-reacquisition.md"
companion_audit: "tests/hourly_20260625_0703_cycle1_keating_pullthatupjamie_asset_reacquisition_audit.py"
---

# Hourly 20260625 0703 Cycle 1 Keating Pull That Up Jamie Asset Reacquisition

## 1. Verdict

Verdict: **blocked**.

`KeatingPullThatUpJamieShiabProjectionFormulaAssetPacket_V1` was executed as a
source reacquisition attempt, but it did not become an accepted asset receipt
packet. The repo and live source checks now establish a stronger source record:

```text
locator_window: 01:41:43-01:42:50
official_pull_that_up_jamie_video_id: TzSEvmqxu48
official_pull_that_up_jamie_title: Geometric Unity for General Relativity & Gauge Theory
official_pull_that_up_jamie_caption_status: Shiab Projection caption present
youtube_oembed_status: reachable metadata and thumbnail only
thumbnail_frame_status: visual ship/connection frame, no visible formula
manuscript_formula_status: generic Shiab formula present on pages 41-44
accepted_receipt_count: 0
accepted_for_routing_count: 0
proof_restart_allowed: false
```

The route is not closed for IG selector identity review. The first obstruction
is still the absence of an actual source-visible formula sheet, legible video
frame sequence, or manuscript-equivalence proof identifying the generic Shiab
formula with the missing highest-weight/Bianchi projection calculation.

## 2. Specific GU Claim/Bridge Under Test

The bridge under test is:

```text
Keating Revealed / Pull That Up Jamie Shiab-projection source material
  -> SourceForcedCodomainSelectorForK_IG
  -> IG selector identity review
```

The acceptance question is not whether the words "Shiab Projection" occur. They
do occur. The acceptance question is whether the source now supplies one of:

1. the original `KeatingRevealed_ShiabProjectionSheet_V1`;
2. a legible Pull That Up Jamie frame/source asset containing the formula or
   projection rule;
3. a manuscript-equivalence proof that pages 41-44 are the same source object
   as the missing representation-theory projection calculation and identify
   `SourceForcedCodomainSelectorForK_IG`.

None of those three objects is available in this run.

## 3. Owned Output Path And Sources Read First

Owned output path:

```text
explorations/hourly-20260625-0703-cycle1-keating-pullthatupjamie-asset-reacquisition.md
```

Companion audit path:

```text
tests/hourly_20260625_0703_cycle1_keating_pullthatupjamie_asset_reacquisition_audit.py
```

Required sources read first:

| source | role in this decision |
| --- | --- |
| `RESEARCH-POSTURE.md` | Keeps acquisition constructive but forbids compatibility or locator inflation. |
| `process/runbooks/five-lane-frontier-run.md` | Supplies verdict vocabulary and no-proof-restart discipline. |
| `explorations/hourly-20260625-0601-cycle3-next-frontier-object-dependency-dag.md` | Names this packet as an upstream source/formula object, not proof replay. |
| `explorations/hourly-20260625-0601-cycle3-visual-acquisition-sequencing-gate.md` | Allows Keating raw retrieval in parallel but forbids accepted routing before capture/transcription/provenance/identity. |
| `explorations/hourly-20260625-0601-cycle2-keating-shiab-projection-formula-asset-packet-spec.md` | Defines required fields for this packet and the identity obstruction. |
| `explorations/hourly-20260625-0502-cycle1-keating-source-surface-receipt-execution.md` | Supplies the prior Keating locator candidate and missing-sheet obstruction. |
| `explorations/hourly-20260625-0203-cycle1-keating-toe-receipt-mining-packet.md` | Confirms earlier modern-media rows were locator-only, not accepted receipts. |
| `sources/media-index.md` | Supplies official source IDs and media-use discipline. |

Additional local source surfaces inspected:

| local surface | result |
| --- | --- |
| `tmp_pdf_text_pages/page-041.txt` | Page 41 contains the family of Shiab operators and a generic contraction form, including equation `(8.1)`. |
| `tmp_pdf_text_pages/page-042.txt` | Page 42 defines invariant-subspace basis data and records the highest-weight/Bianchi operator-choice memory. |
| `tmp_pdf_text_pages/page-043.txt` | Page 43 contains `(9.2)` and `(9.3)` plus the footnote that the settled-on Shiab operator cannot be located. |
| `tmp_pdf_text_pages/page-044.txt` | Page 44 repeats the bosonic-sector Shiab formula in the action context. |

Live source access actually fetched:

| live source | fetched object | result |
| --- | --- | --- |
| `https://geometricunity.org/pull-that-up-jamie/` | rendered page and raw HTML | Official page exposes the Pull That Up Jamie entry titled `Geometric Unity for General Relativity & Gauge Theory`, the embed id `TzSEvmqxu48`, and caption text naming `Shiab Projection`. It does not expose a formula/sheet frame in text. |
| `https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v=TzSEvmqxu48&format=json` | YouTube oEmbed JSON | Confirms title, channel `The Portal Clips`, iframe URL, and thumbnail URL. It is metadata, not a formula asset. |
| `https://i.ytimg.com/vi/TzSEvmqxu48/hqdefault.jpg` | thumbnail image | Reachable thumbnail inspected temporarily; it shows the ship/connection visual and no legible formula/projection rule. |
| `https://theportal.group/into-the-impossible-eric-weinstein-geometric-unity-revealed/` | official transcript page | Confirms the `01:41:43`-`01:42:50` window names the missing Shiab/projection calculations and says the paper sheet has not been found. |

`yt-dlp` was checked and is not installed in this environment, so this run did
not acquire timestamped YouTube frames or subtitles from the video stream.

## 4. Strongest Positive Construction Attempt

The strongest positive construction is a three-surface packet:

| surface | positive object acquired or confirmed | why it still does not accept |
| --- | --- | --- |
| Keating Revealed transcript | Official transcript locates the missing source object at `01:41:43`-`01:42:50`: a Shiab operator and representation-theory projection calculation on old perforated printer paper. | The transcript is explicit that the calculation sheet is not located; it emits no selector formula. |
| Pull That Up Jamie page/video | Official GU page embeds `TzSEvmqxu48` and captions it as creating a Shiab Projection operation preserving the masts when curvature is made into a connection/d-1 form. | The page and oEmbed supply caption and metadata. The thumbnail is a visual mnemonic, not a formula/sheet/frame receipt. |
| Author manuscript pages 41-44 | Local manuscript extraction supplies generic Shiab constructions: `(8.1)`, invariant basis `(8.7)`, `Omega^2(Y^{7,7}, ad) -> Omega^{d-1}(Y^{7,7}, ad)` in `(9.2)`, and the concrete Einsteinian contraction `(9.3)`. | The manuscript itself says the highest-weight/Bianchi-selected operator was not located; generic formulas do not identify the missing sheet or `SourceForcedCodomainSelectorForK_IG`. |

This is decision-useful because the packet is now more specific than the prior
specification. It has official source provenance for the Pull That Up Jamie
asset and a manuscript formula candidate. It still fails at the identity and
asset-capture gate.

Candidate receipt rows:

| candidate_id | source | locator | formula_or_rule_visible | provenance | accepted_for_routing | reason |
| --- | --- | --- | --- | --- | --- | --- |
| `KeatingRevealed_ShiabProjectionLocator_014143_014250` | The Portal Group transcript | `01:41:43`-`01:42:50` | no | official transcript URL | false | Names the missing sheet but does not emit it. |
| `PullThatUpJamie_GUForGRGaugeTheory_TzSEvmqxu48_MetadataReceipt` | official GU page + YouTube oEmbed | page heading and video id `TzSEvmqxu48` | no | official GU page, YouTube oEmbed, thumbnail URL | false | Caption and thumbnail only; no formula frame captured. |
| `ManuscriptShiabFormulaPages41To44_Candidate` | local manuscript text extraction | pages 41-44 | yes, generic Shiab formula | local extracted text from acquired manuscript object | false | Formula exists, but identity to the missing highest-weight/Bianchi projection sheet is not proved. |

## 5. First Exact Obstruction Or Missing Proof/Source Object

The first exact obstruction is:

```text
No actual formula/sheet/frame for KeatingPullThatUpJamieShiabProjectionFormulaAssetPacket_V1
has been captured with provenance and identity to SourceForcedCodomainSelectorForK_IG.
```

More specifically:

```text
KeatingRevealed_ShiabProjectionSheet_V1 remains missing, and the Pull That Up
Jamie `TzSEvmqxu48` source access available in this run supplied only caption,
metadata, and a non-formula thumbnail. The manuscript supplies a generic Shiab
formula but also preserves the missing-note obstruction for the representation-
theory/highest-weight/Bianchi-selected operator.
```

The obstruction is not target-import risk in this run. Target-facing data was
not used to select the candidate. The obstruction is missing source identity and
missing asset content.

## 6. What Would Change If The Hole Closed

If the hole closed, the immediate change would be source-routing readiness, not
proof promotion.

The packet could become one accepted IG receipt only if a recovered asset gives:

| required field | closure condition |
| --- | --- |
| `visual_or_sheet_or_asset_capture` | scan/photo/frame/source asset package with stable URL or checksum/archive id. |
| `formula_or_rule_transcription` | exact visible formula/projection rule, uncertainty marked. |
| `identity_to_missing_sheet` | proof that the object is the old Keating sheet or source-proven equivalent. |
| `family_identity_check` | explicit comparison to `SourceForcedCodomainSelectorForK_IG`. |
| `target_import_clean` | no DESI/dark-energy/FLRW/rank-generation/QFT outcome used to identify the source object. |

Then IG could start selector identity review. Downstream theta/FLRW, dark-energy,
QFT, DGU/VZ, RS, or prediction work would still require a separate proof restart
gate.

## 7. What Would Falsify Or Demote The Route

Demote this route from `blocked` to a scoped source-route `fail` if a complete
frame/source retrieval pass shows all of the following:

- the original Keating sheet remains unrecovered;
- `TzSEvmqxu48` contains only animation/caption/mnemonic material and no
  formula or projection rule;
- no source asset linked from the official Pull That Up Jamie page supplies a
  legible Shiab/projection formula;
- manuscript pages 41-44 remain the only formula source and cannot eliminate
  rival Shiab selectors or identify the missing Bianchi-selected operator.

That demotion would be scoped to this Keating/Pull That Up Jamie route. It would
not be a global no-go for GU or even for IG selector reconstruction from other
primary surfaces.

## 8. Next Meaningful Computation Or Proof/Source Step

The next step is not a proof restart. It is a frame-level source acquisition
step:

1. Acquire the actual `TzSEvmqxu48` video stream or a stable archive copy.
2. Extract frames across the full video and especially any frame containing
   text, formulas, or labels beyond the title/thumbnail.
3. Compute checksums for extracted frame candidates and run OCR/manual
   transcription only on frames with legible source text.
4. Compare any formula-bearing frame to manuscript equations `(8.1)`, `(8.7)`,
   `(9.2)`, `(9.3)`, and page 43 footnote 10.
5. Only after a formula-bearing asset exists, run
   `ManuscriptShiabProjectionIdentityCheck_V1` against
   `SourceForcedCodomainSelectorForK_IG`.

Until then:

```text
accepted_receipt_count = 0
accepted_for_routing_count = 0
proof_restart_allowed = false
```

## 9. JSON Summary

```json
{
  "artifact": "KeatingPullThatUpJamieShiabProjectionFormulaAssetPacketExecution_V1",
  "run_id": "hourly-20260625-0703",
  "cycle": 1,
  "lane": 2,
  "artifact_id": "KeatingPullThatUpJamieShiabProjectionFormulaAssetPacketExecution_V1",
  "verdict": "blocked",
  "accepted_receipt_count": 0,
  "accepted_for_routing_count": 0,
  "proof_restart_allowed": false,
  "locator_window": "01:41:43-01:42:50",
  "asset_requirements": [
    "KeatingRevealed_ShiabProjectionSheet_V1 scan/photo or source-proven equivalent",
    "legible Pull That Up Jamie frame/source asset from TzSEvmqxu48 containing formula_or_rule_transcription",
    "manuscript-equivalence proof tying pages 41-44 to the missing highest-weight/Bianchi projection calculation",
    "provenance fields: source URL, capture method, access date, checksum or archive id, and transformation chain",
    "family identity check to SourceForcedCodomainSelectorForK_IG",
    "target_import_clean true with target_data_seen empty"
  ],
  "first_obstruction": "No actual formula/sheet/frame has been captured with provenance and identity to SourceForcedCodomainSelectorForK_IG; Pull That Up Jamie currently supplies caption/metadata/thumbnail only, while manuscript pages 41-44 supply a generic Shiab formula but preserve the missing highest-weight/Bianchi operator-choice obstruction.",
  "next_frontier_object": "FrameLevelPullThatUpJamieTzSEvmqxu48FormulaCaptureAndManuscriptIdentityCheck_V1",
  "companion_audit": "tests/hourly_20260625_0703_cycle1_keating_pullthatupjamie_asset_reacquisition_audit.py",
  "source_surfaces": [
    {
      "surface_id": "KeatingRevealedTranscriptWindow",
      "source_url": "https://theportal.group/into-the-impossible-eric-weinstein-geometric-unity-revealed/",
      "locator": "01:41:43-01:42:50",
      "object_status": "missing_sheet_named",
      "formula_or_rule_emitted": false,
      "accepted_for_routing": false
    },
    {
      "surface_id": "PullThatUpJamie_GUForGRGaugeTheory_TzSEvmqxu48",
      "source_url": "https://geometricunity.org/pull-that-up-jamie/",
      "video_id": "TzSEvmqxu48",
      "oembed_url": "https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v=TzSEvmqxu48&format=json",
      "thumbnail_url": "https://i.ytimg.com/vi/TzSEvmqxu48/hqdefault.jpg",
      "object_status": "caption_metadata_thumbnail_only",
      "formula_or_rule_emitted": false,
      "accepted_for_routing": false
    },
    {
      "surface_id": "AuthorManuscriptPages41To44",
      "local_pages": [
        "tmp_pdf_text_pages/page-041.txt",
        "tmp_pdf_text_pages/page-042.txt",
        "tmp_pdf_text_pages/page-043.txt",
        "tmp_pdf_text_pages/page-044.txt"
      ],
      "object_status": "generic_shiab_formula_candidate",
      "formula_or_rule_emitted": true,
      "identity_to_missing_sheet_proved": false,
      "accepted_for_routing": false
    }
  ],
  "actual_formula_sheet_frame_available": false,
  "accepted_receipts": [],
  "target_import_guard": {
    "target_data_seen": [],
    "target_import_clean": true,
    "target_import_clean_sufficient_for_acceptance": false
  }
}
```
