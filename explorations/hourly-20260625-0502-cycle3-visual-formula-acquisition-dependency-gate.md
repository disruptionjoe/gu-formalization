---
title: "Hourly 20260625 0502 Cycle 3 Visual Formula Acquisition Dependency Gate"
date: "2026-06-25"
run: "hourly-20260625-0502"
cycle: 3
lane: 4
doc_type: visual_formula_acquisition_dependency_gate
artifact_id: "VisualFormulaAcquisitionDependencyGate_V1"
verdict: "CONDITIONAL_DEPENDENCY_GATE_NO_ACCEPTED_VISUAL_RECEIPTS"
owned_path: "explorations/hourly-20260625-0502-cycle3-visual-formula-acquisition-dependency-gate.md"
companion_audit: "tests/hourly_20260625_0502_cycle3_visual_formula_acquisition_dependency_gate_audit.py"
---

# Hourly 20260625 0502 Cycle 3 Visual Formula Acquisition Dependency Gate

## 1. Verdict

Verdict: **conditional dependency gate; no accepted visual/formula receipts**.

The two remaining visual source-object paths are not interchangeable source
notes. Each has a different minimal object and a different promotion gate:

| source path | minimal missing visual/formula object | current state | affected families |
|---|---|---|---|
| Oxford/Portal PowerPoint formula anchors | `OxfordPortalPowerPointFormulaFramePacket_V1` containing exact official frames plus formula transcription around the named anchors | locator only; no formula-frame packet | `DGU_VZ`, `RS`, with `IG` adjacency |
| Keating/Pull That Up Jamie Shiab projection assets | `KeatingPullThatUpJamieShiabProjectionFormulaAssetPacket_V1`, or the original `KeatingRevealed_ShiabProjectionSheet_V1`, with exact formula/rule or identity proof | quarantined locator/candidate only | `IG`, with `DGU_VZ`, `RS`, and `QFT` only if the captured object emits those family objects |

Decision:

```text
accepted_visual_formula_receipt_count: 0
proof_restart_allowed: false
claim_promotion_allowed: false
first_missing_object: OxfordPortalPowerPointFormulaFramePacket_V1
keating_minimal_object: KeatingPullThatUpJamieShiabProjectionFormulaAssetPacket_V1 or KeatingRevealed_ShiabProjectionSheet_V1
dependency_rule: visual capture and formula transcription are necessary but not sufficient; provenance, target-import cleanliness, and family identity are all required before acceptance.
```

This gate does not promote the Oxford swervature/displasion locator, the
Keating Shiab/projection locator, the Pull That Up Jamie visual/caption, or the
author-manuscript Shiab formula candidate. It decides what must be captured
next and which checks must pass before any row can move from
`locator`/`quarantined` to `accepted_for_routing`.

## 2. Direct Inputs From Cycle-1/2 Source Locator Artifacts

Direct predecessor inputs:

| predecessor artifact | direct input used here |
|---|---|
| `OxfordPortalExactSourceLocatorExecution_V1` | Official Oxford/Portal transcript surfaces contain PowerPoint anchors at `02:33:43`, `02:35:10`, `02:36:12`, `02:38:53`, and `02:40:19`; the strongest DGU/VZ locator is the `GU Equations: Swervature and Displasion` section around `02:35:10`-`02:36:12`; no accepted receipt exists. |
| `KeatingSourceSurfaceReceiptExecution_V1` | The strongest Keating source-side locator is the Portal Group transcript window `01:41:43`-`01:42:50`, where Shiab/projection calculations are discussed but the paper sheet is missing; no accepted receipt exists. |
| `KeatingRevealed_ShiabProjectionSheetRetrievalGate_V1` | The missing `KeatingRevealed_ShiabProjectionSheet_V1` was not located; Pull That Up Jamie asset `TzSEvmqxu48` and author draft pages 41-44 are positive but not accepted; manuscript equivalence is not proved. |
| `AuthorManuscriptIGSelectorReceiptGate_V1` | The manuscript emits strong IG/Shiab formula locators, including `Shiab_candidate_circ_epsilon:Omega^2(Y,ad)->Omega^{d-1}(Y,ad)`, but not the representation-theory/Bianchi selector or family identity needed for `SourceForcedCodomainSelectorForK_IG`. |

Input constraints from posture and runbook:

- Constructive source acquisition is allowed and useful.
- A source-native locator, caption, or formula vicinity is not an accepted
  receipt.
- Target outcomes cannot select, normalize, or identify the source object.
- No proof restart is allowed until source intake and family identity both pass.

## 3. Visual/Formula Dependency Graph or Table

Dependency table:

| state | required object/check | Oxford/Portal status | Keating/Pull That Up Jamie status | promotion implication |
|---|---|---|---|---|
| `locator_found` | exact timestamp/page/asset locator | yes: `02:33:43`, `02:35:10`, `02:36:12`, `02:38:53`, `02:40:19` | yes: Keating `01:41:43`-`01:42:50`; Pull That Up Jamie `TzSEvmqxu48` | may prioritize acquisition only |
| `visual_frame_captured` | official frame/image capture with source URL, timestamp/frame id, and checksum or stable archive id | missing | missing for formula-bearing frame/source asset package | required before formula transcription |
| `formula_transcribed` | exact formula/rule text plus uncertainty marks from the captured visual | missing | missing for Pull That Up Jamie and missing sheet; manuscript formula exists but is not identity-proved to the visual object | required before family routing |
| `source_provenance_clean` | official source/custodian and exact visual object identity | not yet established for frames | partial: official page/video id exists, but formula asset package/sheet provenance missing | required before receipt candidate can be intake-clean |
| `target_import_clean` | `target_data_seen: []` or explicit quarantine of target-facing data | must be checked | clean for Keating Shiab window and manuscript candidate; DESI/dark-energy remains acquisition-only | required but not sufficient |
| `family_identity_checked` | source-emitted object matches the required family object | not possible before frames/formula | not passed; manuscript/Pull That Up Jamie identity to missing sheet not proved | required for accepted receipt |
| `accepted_for_routing` | all prior states pass; row emits a family object | false | false | only then can a candidate leave quarantine |

Dependency graph:

```text
exact locator
  -> visual frame/source asset capture
  -> formula/rule transcription
  -> source provenance certificate
  -> target-import cleanliness certificate
  -> family identity check
  -> accepted_for_routing receipt
  -> proof restart may be reconsidered
```

The graph is ordered. Formula transcription without visual provenance is not
acceptable. Provenance without formula/rule emission is only locator evidence.
Target-import cleanliness without family identity leaves the row quarantined.
Family identity cannot be checked against a paraphrase, caption, or
target-normalized reconstruction.

## 4. First Exact Missing Visual/Formula Object

The first exact missing object for this cycle is:

```text
OxfordPortalPowerPointFormulaFramePacket_V1
```

Minimum contents:

| field | requirement |
|---|---|
| `source_ids` | `GU-MEDIA-2013-OXFORD`, `GU-MEDIA-2020-PORTAL-SPECIAL`, and/or `GU-POD-2020-PORTAL-SPECIAL` as applicable |
| `anchor_ids` | `OxfordPortal_PPT_023343_ShiabOperator`, `OxfordPortal_PPT_023510_Swervature`, `OxfordPortal_PPT_023612_Displasion`, `OxfordPortal_PPT_023853_RSDiracAdjacency`, `OxfordPortal_PPT_024019_PullbackToX` |
| `frame_capture` | screenshot/frame image or stable archive reference for each captured anchor |
| `visual_formula_transcription` | exact displayed formula/rule content, with illegible portions marked |
| `frame_provenance` | official URL, timestamp, access date, capture method, and checksum/archive id if available |
| `target_import_cleanliness` | explicit statement that no target result selected or normalized the transcription |
| `family_identity_precheck` | proposed mapping to `DGU_VZ`, `RS`, or `IG`, with non-matches marked |

Why this is first: Oxford/Portal currently has a source-native equation-shaped
official PowerPoint locator for DGU/VZ. The predecessor artifact already says
transcript text alone is insufficient and the next useful test is image/formula
capture around the PowerPoint anchors. Capturing this packet can decide whether
the displayed equation emits an actual action/operator/EL object, an RS rule, or
only a public explanatory formula.

## 5. Constructive Next Acquisition Object and Acceptance Fields

Constructive next acquisition object:

```text
VisualFormulaReceiptCandidatePacket_V1
```

It has two concrete instantiations:

| packet id | minimal acquisition object | acceptance target |
|---|---|---|
| `OxfordPortalPowerPointFormulaFramePacket_V1` | official PowerPoint frames and formula transcriptions at the five Oxford anchors | decide whether any frame emits `operator_source_primary_action_or_EL for D_GU^epsilon 0/1`, `source.action_or_operator for d_RS,-1`, or an IG selector-adjacent rule |
| `KeatingPullThatUpJamieShiabProjectionFormulaAssetPacket_V1` | original Pull That Up Jamie visual asset/frame/source package for `TzSEvmqxu48`, or the original missing paper sheet, with exact formula/rule | decide whether the object supplies `SourceForcedCodomainSelectorForK_IG` or proves identity to the manuscript Shiab candidate |

Required acceptance fields for any candidate:

| field | required content |
|---|---|
| `candidate_id` | stable object id, not a prose title |
| `source_ids` | source ids from the media index or acquired manuscript object |
| `exact_locator` | timestamp/frame id/page/equation/asset id |
| `visual_object_type` | frame, slide, source asset package, sheet scan/photo, or manuscript-equivalent identity proof |
| `source_provenance` | official URL/custodian, capture method, access date, checksum/archive id if available |
| `formula_or_rule_transcription` | source-emitted displayed formula/rule, not normalized target notation |
| `transcription_uncertainty` | list of illegible, inferred, or ambiguous pieces |
| `target_data_seen` | must be empty for a clean source candidate, otherwise quarantine |
| `target_import_clean` | boolean; cleanliness is required but does not imply acceptance |
| `family_candidates` | families the object could affect, with required object for each |
| `family_identity_check` | pass/fail/blocked check against each required family object |
| `accepted_for_routing` | true only if provenance, transcription, target cleanliness, and family identity all pass |
| `proof_restart_allowed` | false in this packet; proof restart is a later downstream decision |
| `claim_promotion_allowed` | false unless an integration artifact explicitly promotes after intake |

## 6. Claim Impact and Forbidden Promotions

Claim impact:

- The Oxford/Portal PowerPoint path is the first visual/formula acquisition
  dependency because it may emit DGU/VZ formula content not present in transcript
  text.
- The Keating/Pull That Up Jamie path remains the first IG visual identity path:
  it can only help if it supplies the projection calculation, a formula/rule, or
  an identity proof connecting the visual asset/manuscript formula to the missing
  representation-theory/Bianchi selector.
- RS and QFT are affected only conditionally. They remain blocked unless the
  captured visual object itself emits an RS action/operator rule or the finite
  projector `P_fin^b`.

Forbidden promotions from this gate:

```text
Oxford swervature/displasion is not accepted as D_GU^epsilon 0/1.
Oxford Rarita-Schwinger adjacency is not accepted as d_RS,-1.
Keating or Pull That Up Jamie does not select K_IG.
The Pull That Up Jamie visual does not prove the projection rule.
The manuscript Shiab formula is not identical to the missing Keating sheet.
QFT P_fin^b is not supplied.
No DESI, dark-energy, FLRW, VZ, CHSH, Bell, or rho_AB target result may select the source object.
No proof restart is allowed.
No GU mathematical or physical claim is promoted.
```

## 7. Next Meaningful Acquisition/Computation Step

Next step:

```text
Acquire OxfordPortalPowerPointFormulaFramePacket_V1 first.
```

Execution order:

1. Capture official frames around `02:33:43`, `02:35:10`, `02:36:12`,
   `02:38:53`, and `02:40:19` from the Oxford/Portal PowerPoint section.
2. Transcribe only displayed formula/rule content; mark illegible or inferred
   symbols instead of normalizing them.
3. Create one `VisualFormulaReceiptCandidatePacket_V1` row per candidate
   formula object.
4. Run source provenance, target-import, and family-identity checks before
   routing any row.
5. Then acquire `KeatingPullThatUpJamieShiabProjectionFormulaAssetPacket_V1`
   or `KeatingRevealed_ShiabProjectionSheet_V1` and test identity to the
   manuscript Shiab candidate without using target outcomes.

Proof work should not restart during this acquisition step. The computation is
source intake and identity checking, not GU derivation.

## 9. Machine-Readable JSON Summary

```json
{
  "artifact": "VisualFormulaAcquisitionDependencyGate_V1",
  "version": "2026-06-25",
  "run": "hourly-20260625-0502",
  "cycle": 3,
  "lane": 4,
  "verdict": "CONDITIONAL_DEPENDENCY_GATE_NO_ACCEPTED_VISUAL_RECEIPTS",
  "verdict_class": "conditional",
  "artifact_identity": {
    "owned_path": "explorations/hourly-20260625-0502-cycle3-visual-formula-acquisition-dependency-gate.md",
    "companion_audit": "tests/hourly_20260625_0502_cycle3_visual_formula_acquisition_dependency_gate_audit.py",
    "object_id": "VisualFormulaAcquisitionDependencyGate_V1:hourly-20260625-0502-cycle3-lane4"
  },
  "accepted_visual_formula_receipt_count": 0,
  "accepted_receipts": [],
  "proof_restart_allowed": false,
  "claim_promotion_allowed": false,
  "no_claim_promotion": true,
  "dependency_order": [
    "exact_locator",
    "visual_frame_or_source_asset_capture",
    "formula_or_rule_transcription",
    "source_provenance_certificate",
    "target_import_cleanliness_certificate",
    "family_identity_check",
    "accepted_for_routing",
    "proof_restart_reconsideration"
  ],
  "state_dependencies": {
    "visual_capture_required_before_formula_transcription": true,
    "formula_transcription_required_before_family_identity": true,
    "source_provenance_required_before_acceptance": true,
    "target_import_cleanliness_required_before_acceptance": true,
    "target_import_cleanliness_sufficient_for_acceptance": false,
    "family_identity_required_before_acceptance": true,
    "accepted_receipt_required_before_proof_restart": true
  },
  "visual_formula_objects": [
    {
      "object_id": "OxfordPortalPowerPointFormulaFramePacket_V1",
      "source_path": "Oxford/Portal PowerPoint formula anchors",
      "current_status": "missing_visual_formula_packet_locator_only",
      "minimal_object_needed": "official PowerPoint frame captures with formula/rule transcription and provenance",
      "priority": 1,
      "source_ids": [
        "GU-MEDIA-2013-OXFORD",
        "GU-MEDIA-2020-PORTAL-SPECIAL",
        "GU-POD-2020-PORTAL-SPECIAL"
      ],
      "required_anchor_ids": [
        "OxfordPortal_PPT_023343_ShiabOperator",
        "OxfordPortal_PPT_023510_Swervature",
        "OxfordPortal_PPT_023612_Displasion",
        "OxfordPortal_PPT_023853_RSDiracAdjacency",
        "OxfordPortal_PPT_024019_PullbackToX"
      ],
      "required_timestamps": [
        "02:33:43",
        "02:35:10",
        "02:36:12",
        "02:38:53",
        "02:40:19"
      ],
      "families_affected": [
        "DGU_VZ",
        "RS",
        "IG"
      ],
      "family_required_objects": {
        "DGU_VZ": "operator_source_primary_action_or_EL for D_GU^epsilon 0/1",
        "RS": "source.action_or_operator for d_RS,-1",
        "IG": "SourceForcedCodomainSelectorForK_IG if the frame emits a selector/projection rule"
      },
      "can_affect_QFT": false,
      "acceptance_requires": [
        "frame_capture",
        "visual_formula_transcription",
        "source_provenance",
        "target_import_cleanliness",
        "family_identity_check"
      ],
      "accepted_for_routing": false
    },
    {
      "object_id": "KeatingPullThatUpJamieShiabProjectionFormulaAssetPacket_V1",
      "alternate_or_upstream_object_id": "KeatingRevealed_ShiabProjectionSheet_V1",
      "source_path": "Keating/Pull That Up Jamie Shiab projection assets",
      "current_status": "quarantined_locator_and_manuscript_candidate_only",
      "minimal_object_needed": "original visual/source asset package, legible frame, sheet scan/photo, or manuscript-equivalent identity proof with exact formula/rule",
      "priority": 2,
      "source_ids": [
        "GU-POD-2021-KEATING-REVEALED-1",
        "GU-POD-2021-KEATING-REVEALED-2",
        "GU-MEDIA-2021-PULL-THAT-UP-JAMIE",
        "GU-MEDIA-2021-DRAFT-RELEASE"
      ],
      "required_object_ids": [
        "KeatingRevealed_ShiabProjectionSheet_V1",
        "PullThatUpJamie_GUForGRGaugeTheory_TzSEvmqxu48",
        "ManuscriptShiabOperatorFormulaCandidate_V1",
        "ManuscriptShiabProjectionIdentityCheck_V1"
      ],
      "required_locators": [
        "Keating Revealed transcript 01:41:43-01:42:50",
        "Pull That Up Jamie video_id TzSEvmqxu48",
        "2021 draft pages 41-44 Sections 8 and 9.1"
      ],
      "families_affected": [
        "IG",
        "DGU_VZ",
        "RS",
        "QFT"
      ],
      "family_required_objects": {
        "IG": "SourceForcedCodomainSelectorForK_IG",
        "DGU_VZ": "operator_source_primary_action_or_EL for D_GU^epsilon 0/1 only if the visual emits action/operator/EL content",
        "RS": "source.action_or_operator for d_RS,-1 only if the visual emits RS differential/action content",
        "QFT": "P_fin^b: F_phys^b(O) -> K_b only if the visual emits a finite projector/extraction rule"
      },
      "acceptance_requires": [
        "visual_or_sheet_or_asset_capture",
        "formula_or_rule_transcription",
        "source_provenance",
        "target_import_cleanliness",
        "manuscript_or_sheet_identity_check",
        "family_identity_check"
      ],
      "accepted_for_routing": false
    }
  ],
  "first_exact_missing_visual_formula_object": {
    "id": "OxfordPortalPowerPointFormulaFramePacket_V1",
    "reason_first": "The predecessor Oxford locator already identifies official PowerPoint formula anchors where transcript text is insufficient; frame/formula capture is the next object needed to test DGU_VZ and RS receipt identity.",
    "required_before_any_candidate_moves_to_accepted": true
  },
  "constructive_next_acquisition_object": {
    "id": "VisualFormulaReceiptCandidatePacket_V1",
    "first_instance": "OxfordPortalPowerPointFormulaFramePacket_V1",
    "second_instance": "KeatingPullThatUpJamieShiabProjectionFormulaAssetPacket_V1",
    "required_acceptance_fields": [
      "candidate_id",
      "source_ids",
      "exact_locator",
      "visual_object_type",
      "source_provenance",
      "formula_or_rule_transcription",
      "transcription_uncertainty",
      "target_data_seen",
      "target_import_clean",
      "family_candidates",
      "family_identity_check",
      "accepted_for_routing",
      "proof_restart_allowed",
      "claim_promotion_allowed"
    ]
  },
  "forbidden_promotions": [
    "Oxford swervature/displasion accepted as D_GU^epsilon 0/1",
    "Oxford Rarita-Schwinger adjacency accepted as d_RS,-1",
    "Keating or Pull That Up Jamie selects K_IG",
    "Pull That Up Jamie visual proves projection rule",
    "manuscript Shiab formula identical to missing Keating sheet",
    "QFT P_fin^b supplied",
    "target outcome selects source object",
    "proof restart",
    "GU mathematical or physical claim promoted"
  ],
  "next_meaningful_step": "Acquire OxfordPortalPowerPointFormulaFramePacket_V1 first, transcribe displayed formula/rule content, and run provenance, target-import, and family-identity checks before any receipt routing or proof restart."
}
```
