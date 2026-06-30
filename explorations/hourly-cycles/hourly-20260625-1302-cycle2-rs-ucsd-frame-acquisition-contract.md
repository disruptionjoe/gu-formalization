---
title: "Hourly 20260625 1302 Cycle 2 RS UCSD Frame Acquisition Contract"
date: "2026-06-25"
run_id: "hourly-20260625-1302"
cycle: 2
lane: 4
doc_type: rs_ucsd_frame_acquisition_contract
artifact_id: "RS_UCSD_FRAME_ACQUISITION_CONTRACT"
verdict: "BLOCKED_FRAME_ACQUISITION_REMAINS_FIRST_MISSING_SOURCE_OBJECT"
owned_path: "explorations/hourly-20260625-1302-cycle2-rs-ucsd-frame-acquisition-contract.md"
companion_audit: "tests/hourly_20260625_1302_cycle2_rs_ucsd_frame_acquisition_contract.py"
---

# Hourly 20260625 1302 Cycle 2 RS UCSD Frame Acquisition Contract

## 1. Verdict

Verdict: **blocked**.

The current repo-local UCSD transcript is enough to reject a transcript-only
promotion of `UCSDTypedRSMinusOneOperator_V1`. It is not enough to demote the
whole UCSD RS route, because the first missing source object is still the exact
frame or slide sequence for the rolled-operator window.

Decision state:

```text
transcript_window_present: true
frame_sequence_present: false
acquisition_contract_complete: true
transcript_only_promotion_rejected: true
scoped_ucsd_demotion_justified: false
accepted_rs_receipt_count: 0
proof_restart_allowed: false
generation_restart_allowed: false
```

The repo may say: the transcript alone does not supply a typed pure-RS
`d_RS,-1` receipt. The repo may not yet say: the UCSD visual source route has
failed. That stronger decision requires acquisition or documented unavailability
of the frame sequence specified below.

## 2. What Was Derived Directly From Repo Sources

Read first and used:

- `RESEARCH-POSTURE.md`
- `process/runbooks/five-lane-frontier-run.md`
- `explorations/hourly-20260625-1302-cycle1-rs-ucsd-frame-packet.md`
- `tests/hourly_20260625_1302_cycle1_rs_ucsd_frame_packet_audit.py`
- `literature/weinstein-ucsd-2025-04-transcript.md`
- `explorations/hourly-20260625-0803-cycle2-rs-ucsd-typed-operator-source-origin-classifier.md`

Direct repo-derived facts:

| source fact | repo-local status | acquisition implication |
|---|---|---|
| UCSD transcript window `[00:32:07]-[00:37:41]` exists. | present | use as timestamp spine for visual capture |
| `[00:32:07]` introduces `Y^14`, the metric-bundle setting, and pullback data. | transcript present | capture the slide immediately before and after this transition |
| `[00:32:46]` says pulling back spinor-valued zero-forms and one-forms gives three generations. | transcript present | capture any displayed representation table or generation row |
| `[00:34:27]` names the de Rham/Dirac/Einstein complex and the middle-map issue. | transcript present | capture the displayed complex and middle-map formula |
| `[00:35:30]` mines connection information for a minimally coupled exterior derivative. | transcript present | capture formula fields for the coupled differential |
| `[00:36:13]` gives the rolled Dirac/de Rham/Rarita-Schwinger gadget and symbol from two-forms to one-forms. | transcript present | capture the symbol, operator label, and source/target spaces |
| `[00:37:41]` exits into grand-unification and normal-bundle numerology. | transcript present | capture the terminal frame to bound the RS window |
| Cycle 1 found no repo-local UCSD slide, frame, screenshot, crop, OCR row, video frame, or deck for this window. | absent | frame acquisition remains open |
| The 0803 classifier found a source-origin surface, but not a typed source-origin operator rule. | conditional/underdefined | acceptance requires pure-RS typing and quotient data |

## 3. The Strongest Positive Result

The strongest positive result is a complete acquisition contract for the next
source computation. The contract can decide the UCSD RS route without relying on
impressionistic transcript language.

Required frame windows:

| window id | exact time interval | required capture density | reason |
|---|---|---|---|
| `ucsd_rs_context_y14` | `[00:32:07]-[00:32:46]` | first visible slide change, plus one frame every 5 seconds | anchors `Y^14`, `X^4`, metric-bundle, and pullback context |
| `ucsd_rs_generation_pullback` | `[00:32:46]-[00:34:27]` | all slide changes, plus any frame with representation text | checks whether generation language is displayed as formula, table, or prose |
| `ucsd_rs_complex_middle_map` | `[00:34:27]-[00:35:30]` | all formula frames, plus before/after frames for each formula | checks de Rham/Dirac/Einstein complex and `Omega^1 -> Omega^(d-1)` |
| `ucsd_rs_coupled_derivative` | `[00:35:30]-[00:36:13]` | all formula frames, plus one frame every 3 seconds | checks exterior derivative, connection source, and inhomogeneous gauge group labels |
| `ucsd_rs_rolled_symbol` | `[00:36:13]-[00:37:41]` | all frames with diagrams or formulas, plus one frame every 2 seconds | checks rolled operator, RS labels, symbol `Omega^2(E) -> Omega^1(E)`, and any quotient/projection |

The capture set must include at least one frame immediately before `[00:32:07]`
and one immediately after `[00:37:41]` so that the packet can prove the RS
window was not clipped at a formula boundary.

Required frame/slide fields:

| field | required content |
|---|---|
| `source_id` | UCSD April 2025 talk source identifier, including URL, archive locator, local video path, or slide-deck path |
| `source_kind` | one of `official_video`, `archived_video`, `local_video`, `official_slide_deck`, `speaker_slide_deck`, `secondary_capture` |
| `capture_method` | command, software, or manual method used to extract frames or slides |
| `timestamp_window` | one of the required windows above |
| `frame_timestamp` | exact timestamp for each captured frame, with second-level precision or better |
| `slide_number` | slide/page number when available; otherwise `null` with explanation |
| `artifact_path` | repo-local path for full frame or slide image |
| `crop_paths` | repo-local paths for formula crops, complex diagrams, and relevant labels |
| `sha256_full_frame` | SHA-256 checksum of each full-frame image or slide artifact |
| `sha256_crop` | SHA-256 checksum of each formula crop |
| `ocr_text_raw` | raw OCR text, preserving errors |
| `transcription_normalized` | human-normalized formula/prose transcription |
| `transcription_reviewer` | reviewer id or `single_worker_unreviewed` |
| `visible_operator_name` | exact displayed operator name or `absent` |
| `visible_domain` | exact displayed source/domain space or `absent` |
| `visible_codomain` | exact displayed target/codomain space or `absent` |
| `visible_degree_or_slot` | displayed degree, slot, or `d_RS,-1` equivalent, or `absent` |
| `visible_rule_kind` | displayed action, differential, operator, symbol, or map type |
| `visible_rs_projection_or_quotient` | displayed `P_RS`, quotient, RS-only projection, family certificate, or `absent` |
| `intake_decision` | `accepted_for_typed_operator_test`, `rejected_aggregate_only`, `quarantined_low_quality`, or `missing` |
| `decision_reason` | short reason tied to visible fields, not interpretation alone |

Checksum and transcription requirements:

- Full frames and crops must be immutable artifacts with SHA-256 checksums.
- OCR must be kept raw; normalized transcription must not replace it.
- Formula transcription must preserve domains, codomains, arrows, degree labels,
  subscripts, superscripts, and visible operator names.
- A crop can support acceptance only if the full-frame checksum and crop checksum
  are both present.
- A frame sequence can support rejection only if it covers the required window
  densely enough to rule out missed formula frames or provides a documented
  slide-deck page sequence for the same interval.
- Any secondary capture must be quarantined unless it can be matched to the
  transcript time window and checked against a full-frame or deck source.

Acceptance decision for `UCSDTypedRSMinusOneOperator_V1`:

```text
ACCEPT_FOR_TYPED_OPERATOR_TEST only if the acquired frames or slides visibly
supply a source surface plus operator name or formula, domain, codomain,
degree/slot or source-equivalent minus-one position, rule kind, and a
pure-RS projection/quotient/family certificate separating RS from aggregate
Dirac/de Rham/spinor-valued form data.
```

Rejection decisions:

```text
REJECT_TRANSCRIPT_ONLY_PROMOTION now:
  The transcript alone is aggregate and underdefined.

REJECT_AGGREGATE_ONLY after acquisition:
  Frames are acquired and visibly contain only aggregate Dirac/de Rham/RS
  language, without pure-RS domain, codomain, slot, and quotient/projection.

QUARANTINE_LOW_QUALITY after acquisition:
  Frames exist but are too low-resolution, clipped, non-checksummed, or
  insufficiently timestamped to support acceptance or rejection.

MISSING remains current:
  No repo-local frame sequence, slide deck, screenshot, crop, OCR row, or video
  frame exists for the required windows.
```

## 4. The First Exact Obstruction Or Missing Source Object

The first exact obstruction is still:

```text
UCSDFrameSequenceForRolledOperatorWindow_V1 is absent for [00:32:07]-[00:37:41].
```

The current transcript cannot fill these acceptance-critical fields:

| `UCSDTypedRSMinusOneOperator_V1` field | current transcript-only state |
|---|---|
| `source_surface` | transcript timestamp present; frame/slide locator absent |
| `operator_name` | informal aggregate phrase present; displayed formal name absent |
| `domain` | spinor-valued form motif present; pure-RS source space absent |
| `codomain` | spinor-valued one-form target motif present; pure-RS target absent |
| `degree_or_slot` | form-degree movement present; `d_RS,-1` or equivalent slot absent |
| `rule_kind` | differential-symbol composite motif present; accepted source rule absent |
| `RS_only_purity` | fails at transcript-only level because the language is aggregate |
| `relation_to_equation_10_10` | independent route; does not repair equation `10.10` |
| `family_identity` | not runnable without `P_RS`, quotient, or family certificate |

## 5. The Constructive Next Object That Would Remove Or Test The Obstruction

The constructive next object is:

```text
UCSDFrameSequenceForRolledOperatorWindow_V1
```

Minimum acceptance payload:

```text
source_id
source_kind
capture_method
required_frame_windows
full_frame_artifact_paths
crop_artifact_paths
sha256_full_frame_values
sha256_crop_values
ocr_text_raw
transcription_normalized
visible_complex_transcription
visible_middle_map_transcription
visible_symbol_transcription
visible_operator_name
visible_domain
visible_codomain
visible_degree_or_slot
visible_rs_projection_or_quotient
intake_decisions
```

This object removes the current obstruction in either direction. If it contains
the required pure-RS fields, the next lane can attempt a typed operator packet.
If it covers the window and shows only aggregate language, the repo can demote
the UCSD visual route to aggregate-only for this RS gate.

## 6. What This Means For RS `d_RS,-1`, Quotient, And Generation-Count Restart

For `d_RS,-1`:

```text
accepted_rs_receipt_count remains 0.
```

For the RS quotient:

```text
No repo-local source currently supplies a source-defined P_RS, RS quotient, or
family identity certificate tied to the UCSD rolled-operator window.
```

For proof and generation restart:

```text
proof_restart_allowed: false
generation_restart_allowed: false
```

The transcript's two-plus-one generation language remains source-hosted
motivation, not an index proof, not a physical quotient, and not a restart
license. Any restart must wait for a typed operator receipt and downstream
family-identity/quotient checks.

## 7. Next Meaningful Proof/Source Computation Step

Perform source acquisition before proof reconstruction:

```text
Acquire UCSDFrameSequenceForRolledOperatorWindow_V1 for [00:32:07]-[00:37:41],
with dense capture across the five required subwindows, full-frame and crop
checksums, raw OCR, normalized transcription, and intake decisions.
```

Then run this binary source computation:

```text
If visible pure-RS domain/codomain/slot/quotient data exist:
  instantiate UCSDTypedRSMinusOneOperator_V1 as a candidate receipt pending
  family identity.

If the acquired visual source is aggregate-only:
  demote the UCSD visual route for the RS d_RS,-1 receipt while preserving the
  transcript as source-hosted motivation.

If the visual source cannot be acquired or verified:
  keep the route blocked at frame acquisition.
```

## 8. Machine-Readable JSON Summary

```json
{
  "artifact": "RS_UCSD_FRAME_ACQUISITION_CONTRACT",
  "version": "2026-06-25",
  "run_id": "hourly-20260625-1302",
  "cycle": 2,
  "lane": 4,
  "verdict": "BLOCKED_FRAME_ACQUISITION_REMAINS_FIRST_MISSING_SOURCE_OBJECT",
  "verdict_class": "blocked",
  "family": "RS",
  "target_object": "UCSDTypedRSMinusOneOperator_V1",
  "required_object": "source.action_or_operator for d_RS,-1",
  "required_frame_windows": [
    {
      "id": "ucsd_rs_context_y14",
      "start": "00:32:07",
      "end": "00:32:46",
      "required_capture_density": "slide_changes_plus_one_frame_every_5_seconds",
      "required_fields": [
        "Y14_context",
        "X4_slice",
        "metric_bundle",
        "pullback_context"
      ]
    },
    {
      "id": "ucsd_rs_generation_pullback",
      "start": "00:32:46",
      "end": "00:34:27",
      "required_capture_density": "slide_changes_plus_representation_text_frames",
      "required_fields": [
        "spinor_zero_forms",
        "spinor_one_forms",
        "generation_language",
        "displayed_representation_table_if_any"
      ]
    },
    {
      "id": "ucsd_rs_complex_middle_map",
      "start": "00:34:27",
      "end": "00:35:30",
      "required_capture_density": "all_formula_frames_plus_before_after_context",
      "required_fields": [
        "de_Rham_Dirac_Einstein_complex",
        "Omega1_to_Omega_d_minus_1_middle_map",
        "displayed_domain",
        "displayed_codomain"
      ]
    },
    {
      "id": "ucsd_rs_coupled_derivative",
      "start": "00:35:30",
      "end": "00:36:13",
      "required_capture_density": "all_formula_frames_plus_one_frame_every_3_seconds",
      "required_fields": [
        "minimally_coupled_exterior_derivative",
        "connection_information",
        "inhomogeneous_gauge_group_labels"
      ]
    },
    {
      "id": "ucsd_rs_rolled_symbol",
      "start": "00:36:13",
      "end": "00:37:41",
      "required_capture_density": "all_formula_or_diagram_frames_plus_one_frame_every_2_seconds",
      "required_fields": [
        "rolled_operator_label",
        "Rarita_Schwinger_label",
        "Omega2_to_Omega1_symbol",
        "pure_RS_projection_or_quotient_if_any"
      ]
    }
  ],
  "required_frame_or_slide_fields": [
    "source_id",
    "source_kind",
    "capture_method",
    "timestamp_window",
    "frame_timestamp",
    "slide_number",
    "artifact_path",
    "crop_paths",
    "sha256_full_frame",
    "sha256_crop",
    "ocr_text_raw",
    "transcription_normalized",
    "transcription_reviewer",
    "visible_operator_name",
    "visible_domain",
    "visible_codomain",
    "visible_degree_or_slot",
    "visible_rule_kind",
    "visible_rs_projection_or_quotient",
    "intake_decision",
    "decision_reason"
  ],
  "checksum_requirements": {
    "full_frame_sha256_required": true,
    "crop_sha256_required": true,
    "raw_ocr_retained": true,
    "normalized_transcription_retained": true,
    "formula_fields_must_preserve_domains_codomains_arrows_degrees_subscripts": true,
    "secondary_capture_quarantined_until_matched_to_source": true
  },
  "acceptance_decisions": {
    "accepted_for_typed_operator_test": {
      "allowed": true,
      "requires": [
        "source_surface_with_frame_or_slide_locator",
        "visible_operator_name_or_formula",
        "visible_domain",
        "visible_codomain",
        "visible_degree_or_slot",
        "visible_rule_kind",
        "visible_rs_projection_or_quotient_or_family_certificate",
        "checksummed_full_frame_and_crop",
        "raw_ocr_and_normalized_transcription"
      ],
      "effect": "candidate_receipt_pending_family_identity"
    },
    "rejected_transcript_only_promotion": {
      "current_decision": true,
      "reason": "Transcript hosts aggregate rolled-operator language but lacks frame locator, displayed formula fields, pure-RS domain, pure-RS codomain, d_RS_minus_1 slot, P_RS quotient, and family identity."
    },
    "rejected_aggregate_only_after_acquisition": {
      "current_decision": false,
      "requires": [
        "frame_sequence_present",
        "required_windows_covered",
        "visible_material_contains_only_aggregate_Dirac_de_Rham_RS_language",
        "pure_RS_typing_absent"
      ]
    },
    "quarantined_low_quality": {
      "current_decision": false,
      "trigger": "frames_exist_but_are_low_resolution_clipped_non_checksummed_or_insufficiently_timestamped"
    },
    "missing": {
      "current_decision": true,
      "reason": "No repo-local UCSD frame sequence, slide deck, screenshot, crop, OCR row, or video frame exists for the required windows."
    }
  },
  "transcript_window_present": true,
  "transcript_window": "[00:32:07]-[00:37:41]",
  "frame_sequence_present": false,
  "frame_sequence_artifacts": [],
  "transcript_only_promotion_rejected": true,
  "acquisition_contract_complete": true,
  "scoped_ucsd_demotion_justified": false,
  "scoped_ucsd_demotion_scope": "not_justified_for_full_ucsd_visual_route_until_frame_sequence_is_acquired_or_documented_unavailable",
  "transcript_only_demote_to_motivation": true,
  "first_missing_source_object": {
    "id": "UCSDFrameSequenceForRolledOperatorWindow_V1",
    "window": "[00:32:07]-[00:37:41]",
    "exists": false,
    "why_first": "Without frames or slides, the repo cannot inspect displayed operator name, domain, codomain, slot, symbol, or RS quotient fields."
  },
  "typed_operator_status": {
    "ucsd_typed_operator_exists": false,
    "accepted_as_typed_operator": false,
    "accepted_as_rs_minus_one_receipt": false,
    "pure_rs_domain_present": false,
    "pure_rs_codomain_present": false,
    "minus_one_slot_present": false,
    "rs_projection_or_quotient_present": false,
    "family_identity_runnable": false
  },
  "accepted_rs_receipt_count": 0,
  "proof_restart_allowed": false,
  "generation_restart_allowed": false,
  "generation_count_promotion_allowed": false,
  "forbidden_promotions": [
    "transcript_hosted_language_as_typed_pure_RS_operator",
    "ucsd_transcript_as_d_RS_minus_1_receipt",
    "ucsd_route_demoted_without_frame_acquisition_or_documented_unavailability",
    "accepted_RS_receipt_without_frame_sequence_or_typed_operator",
    "RS_family_identity_passed",
    "RS_quotient_or_P_RS_found",
    "proof_restart_allowed",
    "generation_restart_allowed",
    "two_plus_one_generation_language_as_index_proof",
    "equation_10_10_repaired_by_UCSD_transcript"
  ],
  "next_meaningful_step": "Acquire UCSDFrameSequenceForRolledOperatorWindow_V1 for 00:32:07-00:37:41 with checksummed frames, crops, raw OCR, normalized transcription, and intake decisions."
}
```
