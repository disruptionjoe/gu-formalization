---
title: "Hourly 20260625 0601 Cycle 1 Oxford Portal Formula Frame Packet Spec"
date: "2026-06-25"
run: "hourly-20260625-0601"
cycle: 1
lane: 5
doc_type: visual_formula_acquisition_spec_gate
artifact_id: "OxfordPortalPowerPointFormulaFramePacket_V1"
verdict: "BLOCKED_FORMULA_FRAME_PACKET_MISSING_ZERO_ACCEPTED_VISUAL_RECEIPTS"
owned_path: "explorations/hourly-20260625-0601-cycle1-oxford-portal-formula-frame-packet-spec.md"
companion_audit: "tests/hourly_20260625_0601_cycle1_oxford_portal_formula_frame_packet_spec_audit.py"
---

# Hourly 20260625 0601 Cycle 1 Oxford Portal Formula Frame Packet Spec

## 1. Verdict

Verdict: **blocked**.

`OxfordPortalPowerPointFormulaFramePacket_V1` is the next required acquisition
object. The repo has exact Oxford/Portal PowerPoint locators at `02:33:43`,
`02:35:10`, `02:36:12`, `02:38:53`, and `02:40:19`, but it does not have the
official frame captures, displayed formula/rule transcriptions, provenance
checks, target-import screen, or family identity checks needed to accept any
visual formula receipt.

Current decision:

```text
accepted_visual_formula_receipt_count: 0
proof_restart_allowed: false
claim_promotion_allowed: false
family_identity_status: blocked
first_missing_object: OxfordPortalPowerPointFormulaFramePacket_V1
```

This is a visual formula acquisition dependency hole, not a proof restart. The
source-native locators are useful, but no current repo source already suffices
as an accepted `PrimarySourceReceiptInstance_V1` or visual formula receipt.

## 2. What Was Derived Directly From Repo/Source Surfaces

Directly derived from the repo artifacts read for this lane:

| source surface | direct content used | sufficiency decision |
|---|---|---|
| `RESEARCH-POSTURE.md` | constructive acquisition is allowed, but compatibility, source adjacency, and target imports cannot be inflated into proof | requires disciplined gate rather than promotion |
| `five-lane-frontier-run.md` | verdict vocabulary requires exact obstruction, impact, falsification, and next computation | verdict must stay `blocked` until the missing object exists |
| `three-cycle-fifteen-hole-run.md` | quality holes should name a missing proof/source object whose resolution changes the map | this lane names the packet and per-anchor fields |
| `OxfordPortalExactSourceLocatorExecution_V1` | official Oxford/Portal pages were reachable; strongest locators are `02:33:43`, `02:35:10`, `02:36:12`, `02:38:53`, `02:40:19`; accepted receipts remain zero | locator only; not sufficient |
| `VisualFormulaAcquisitionDependencyGate_V1` | first missing object is `OxfordPortalPowerPointFormulaFramePacket_V1`; visual capture and formula transcription precede family identity | establishes packet ordering |
| `Hourly20260625_0502_ThreeCycleFifteenHoleSynthesis_V1` | no GU mathematical or physical claim was promoted; all family identity checks remain unpassed | proof restart remains blocked |

What the current repo already suffices for:

- It suffices to prioritize a frame acquisition pass over broad proof work.
- It suffices to identify which five anchors must be captured.
- It suffices to keep `accepted_visual_formula_receipt_count` at `0`.
- It suffices to block proof restart and claim promotion.

What the current repo does not suffice for:

- It does not provide official images or stable archived frame objects.
- It does not provide displayed formula/rule transcriptions.
- It does not prove identity to `D_GU^epsilon` 0/1, `d_RS,-1`, or
  `SourceForcedCodomainSelectorForK_IG`.
- It does not open a DGU/VZ, RS, IG, or QFT proof route.

## 3. Strongest Positive Acquisition Attempt

The strongest positive attempt is to instantiate one
`VisualFormulaReceiptCandidatePacket_V1` row per anchor after acquiring the
official frame. Each row must preserve the source display before any target
normalization.

| anchor | candidate family impact | required displayed formula/rule fields |
|---|---|---|
| `02:33:43` | IG primary adjacency; possible DGU/VZ precondition if the frame actually displays a Shiab operator with domain/codomain and choice rule | exact operator name; domain and codomain; contraction target; selection or rival-elimination rule if displayed; all ambiguous symbols marked; no target-derived codomain fill-in |
| `02:35:10` | DGU/VZ strongest positive locator; possible IG adjacency through Shiab applied to curvature | exact swervature formula; curvature input object; Shiab application rule; whether the displayed object is action, operator, EL equation, tensor identity, or explanatory shorthand; any coefficient/sign/index conventions |
| `02:36:12` | DGU/VZ strongest equation locator | exact displayed `swervature = displasion` or equivalent rule; definition of displasion if visible; base space (`Y` or pullback relation to `X`) if displayed; whether equation is an EL equation, replacement field equation, or schematic identity |
| `02:38:53` | RS adjacency; possible DGU/VZ/fermionic bridge if a Dirac/Rarita-Schwinger rule is visible | exact Dirac square, Rarita-Schwinger, spin-3/2, gauge, Noether, BRST, or operator formula if displayed; source/target and degree data if a differential appears; whether it can be typed as `source.action_or_operator for d_RS,-1` |
| `02:40:19` | DGU/VZ pullback-to-`X` check; possible RS adjacency through Dirac piece; IG only if a selector/projection rule is displayed | exact pullback rule from `Y` to `X`; bundle/map notation; relation to Einstein/Yang-Mills/Maxwell recovery if formulaic; any displayed Dirac-square or projection rule; no acceptance from prose-only explanation |

For every anchor, the required packet fields are:

| field | requirement |
|---|---|
| `candidate_id` | stable row id keyed by timestamp and displayed object |
| `source_ids` | `GU-MEDIA-2013-OXFORD`, `GU-MEDIA-2020-PORTAL-SPECIAL`, and/or `GU-POD-2020-PORTAL-SPECIAL` |
| `exact_anchor` | timestamp plus section/slide/frame label if available |
| `frame_capture` | official frame image or stable archive reference |
| `frame_checksum_or_archive_id` | hash, archive id, or explicit unavailable marker |
| `formula_or_rule_transcription` | displayed source formula/rule, preserving notation |
| `transcription_uncertainty` | illegible, inferred, cropped, or ambiguous symbols |
| `visual_object_type` | slide frame, transcript-still, official video frame, or archived frame |
| `target_data_seen` | must be empty for a clean candidate |
| `family_candidates` | DGU/VZ, RS, IG, or none, with QFT excluded unless a finite projector is displayed |
| `family_identity_status` | blocked, failed, or passed after source intake; blocked before frame/formula capture |
| `accepted_for_routing` | false unless provenance, transcription, target cleanliness, and family identity all pass |

## 4. First Exact Obstruction/Missing Visual/Formula Object

The first exact obstruction is:

```text
OxfordPortalPowerPointFormulaFramePacket_V1 is missing.
```

The missing object is not a new mathematical proof. It is an acquisition packet
with five official frame captures and source-preserving formula/rule
transcriptions. Without that packet, the repo cannot tell whether the Oxford
PowerPoint displays:

- an actual `operator_source_primary_action_or_EL for D_GU^epsilon 0/1`;
- a `source.action_or_operator for d_RS,-1`;
- a `SourceForcedCodomainSelectorForK_IG`;
- only explanatory notation that remains locator evidence.

Family identity is blocked because there is no captured formula object to
compare. Target-import cleanliness alone would not close this obstruction.

## 5. Impact If Closed

If the packet is acquired and at least one row passes provenance, transcription,
target-import, and family identity checks, the impact is family-limited:

- DGU/VZ could move from official locator to accepted receipt candidate if
  `02:35:10` or `02:36:12` displays an actual action/operator/EL object or a
  formula sufficient to identify `D_GU^epsilon` 0/1.
- RS could move from adjacency to accepted receipt candidate if `02:38:53` or
  nearby frames emit a typed action/operator/differential/gauge/Noether/BRST
  rule for `d_RS,-1`.
- IG could move from Shiab/projection vocabulary to candidate identity work if
  `02:33:43` or `02:40:19` displays a source-forced selector or projection rule.
- QFT remains unaffected unless a frame unexpectedly emits a finite projector
  `P_fin^b: F_phys^b(O) -> K_b`.

Closing the packet does not itself prove any downstream GU claim. It only
creates source-native receipt rows eligible for family identity checking and,
after that, possible family-limited proof restart.

## 6. Falsification/Demotion Condition

Demote the Oxford/Portal PowerPoint path for these family gates if a clean
packet is acquired and all five anchors fail the required formula-object test:

```text
frame captures are official and legible,
formula/rule transcriptions are complete or uncertainty-marked,
target_data_seen is empty,
and no anchor emits the required DGU/VZ, RS, or IG family object.
```

That demotion would be source-scope limited. It would say Oxford/Portal remains
a terminology/provenance locator for these anchors, not an accepted family
receipt. It would not create a global no-go for GU, DGU/VZ, RS, IG, or QFT,
because other source surfaces may still emit the missing objects.

## 7. Next Meaningful Acquisition/Computation Step

Next step:

```text
Acquire OxfordPortalPowerPointFormulaFramePacket_V1 before restarting proof work.
```

Execution order:

1. Capture official frames at `02:33:43`, `02:35:10`, `02:36:12`, `02:38:53`,
   and `02:40:19`.
2. Hash or archive each captured frame, or record why no checksum/archive id is
   available.
3. Transcribe only displayed formula/rule content, marking uncertainty instead
   of normalizing to repo target notation.
4. Emit one `VisualFormulaReceiptCandidatePacket_V1` row per displayed
   formula/rule object.
5. Run target-import and family-identity checks before any receipt routes to
   proof work.

## 8. Machine-Readable JSON Summary

```json
{
  "artifact": "OxfordPortalPowerPointFormulaFramePacket_V1",
  "version": "2026-06-25",
  "run": "hourly-20260625-0601",
  "cycle": 1,
  "lane": 5,
  "verdict": "BLOCKED_FORMULA_FRAME_PACKET_MISSING_ZERO_ACCEPTED_VISUAL_RECEIPTS",
  "verdict_class": "blocked",
  "artifact_identity": {
    "owned_path": "explorations/hourly-20260625-0601-cycle1-oxford-portal-formula-frame-packet-spec.md",
    "companion_audit": "tests/hourly_20260625_0601_cycle1_oxford_portal_formula_frame_packet_spec_audit.py",
    "artifact_id": "OxfordPortalPowerPointFormulaFramePacket_V1"
  },
  "current_repo_source_suffices": false,
  "accepted_visual_formula_receipt_count": 0,
  "accepted_receipts": [],
  "proof_restart_allowed": false,
  "claim_promotion_allowed": false,
  "family_identity_status": "blocked",
  "family_identity_blocked": true,
  "first_exact_obstruction": {
    "id": "OxfordPortalPowerPointFormulaFramePacket_V1",
    "missing": true,
    "description": "official frame captures plus displayed formula/rule transcriptions are missing, so family identity cannot be checked"
  },
  "required_timestamps": [
    "02:33:43",
    "02:35:10",
    "02:36:12",
    "02:38:53",
    "02:40:19"
  ],
  "per_anchor_acquisition_spec": [
    {
      "timestamp": "02:33:43",
      "anchor_id": "OxfordPortal_PPT_023343_ShiabOperator",
      "candidate_family_impact": ["IG", "DGU_VZ_if_operator_precondition_displayed"],
      "required_displayed_formula_or_rule_fields": [
        "operator_name",
        "domain_and_codomain",
        "contraction_target",
        "selection_or_rival_elimination_rule_if_displayed",
        "uncertainty_marks"
      ],
      "accepted_for_routing": false
    },
    {
      "timestamp": "02:35:10",
      "anchor_id": "OxfordPortal_PPT_023510_Swervature",
      "candidate_family_impact": ["DGU_VZ", "IG_adjacency"],
      "required_displayed_formula_or_rule_fields": [
        "swervature_formula",
        "curvature_input_object",
        "shiab_application_rule",
        "object_kind_action_operator_EL_tensor_or_shorthand",
        "coefficient_sign_index_conventions"
      ],
      "accepted_for_routing": false
    },
    {
      "timestamp": "02:36:12",
      "anchor_id": "OxfordPortal_PPT_023612_Displasion",
      "candidate_family_impact": ["DGU_VZ"],
      "required_displayed_formula_or_rule_fields": [
        "swervature_equals_displasion_rule",
        "displasion_definition_if_visible",
        "base_space_Y_or_pullback_relation",
        "equation_kind_EL_replacement_field_equation_or_schematic_identity"
      ],
      "accepted_for_routing": false
    },
    {
      "timestamp": "02:38:53",
      "anchor_id": "OxfordPortal_PPT_023853_RSDiracAdjacency",
      "candidate_family_impact": ["RS", "DGU_VZ_fermionic_bridge_if_displayed"],
      "required_displayed_formula_or_rule_fields": [
        "dirac_square_or_rarita_schwinger_formula_if_displayed",
        "spin_3_2_or_gauge_data",
        "source_target_and_degree_for_any_differential",
        "action_operator_noether_BRST_or_rule_type"
      ],
      "accepted_for_routing": false
    },
    {
      "timestamp": "02:40:19",
      "anchor_id": "OxfordPortal_PPT_024019_PullbackToX",
      "candidate_family_impact": ["DGU_VZ", "RS_adjacency", "IG_if_selector_or_projection_displayed"],
      "required_displayed_formula_or_rule_fields": [
        "pullback_rule_from_Y_to_X",
        "bundle_or_map_notation",
        "formulaic_recovery_relation_if_displayed",
        "dirac_square_or_projection_rule_if_displayed"
      ],
      "accepted_for_routing": false
    }
  ],
  "required_packet_fields": [
    "candidate_id",
    "source_ids",
    "exact_anchor",
    "frame_capture",
    "frame_checksum_or_archive_id",
    "formula_or_rule_transcription",
    "transcription_uncertainty",
    "visual_object_type",
    "target_data_seen",
    "family_candidates",
    "family_identity_status",
    "accepted_for_routing"
  ],
  "family_required_objects": {
    "DGU_VZ": "operator_source_primary_action_or_EL for D_GU^epsilon 0/1",
    "RS": "source.action_or_operator for d_RS,-1",
    "IG": "SourceForcedCodomainSelectorForK_IG",
    "QFT": "P_fin^b: F_phys^b(O) -> K_b only if a finite projector is displayed"
  },
  "impact_if_closed": {
    "DGU_VZ": "may move to accepted receipt candidate only if displayed formula identifies actual D_GU^epsilon 0/1 action operator or EL object",
    "RS": "may move to accepted receipt candidate only if displayed formula identifies d_RS,-1 action operator differential gauge Noether or BRST rule",
    "IG": "may move to selector identity work only if displayed formula source-forces selector or projection rule",
    "QFT": "unchanged unless displayed frame unexpectedly emits P_fin^b"
  },
  "falsification_or_demotion_condition": "Demote Oxford/Portal PowerPoint anchors to terminology/provenance locators if official legible captures with clean transcriptions and empty target_data_seen emit no required DGU_VZ RS or IG family object.",
  "next_meaningful_step": "Acquire official frames at 02:33:43, 02:35:10, 02:36:12, 02:38:53, and 02:40:19, transcribe displayed formula/rule content, and run target-import plus family-identity checks before any proof restart."
}
```
