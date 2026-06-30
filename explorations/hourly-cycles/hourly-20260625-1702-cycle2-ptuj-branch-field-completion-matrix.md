---
title: "Hourly 20260625 1702 Cycle 2 PTUJ Branch Field Completion Matrix"
date: "2026-06-25"
run_id: "hourly-20260625-1702"
cycle: 2
lane: 1
doc_type: ptuj_branch_field_completion_matrix
artifact_id: "PTUJ_BRANCH_FIELD_COMPLETION_MATRIX_1702_C2_L1_V1"
verdict: "blocked"
owned_path: "explorations/hourly-20260625-1702-cycle2-ptuj-branch-field-completion-matrix.md"
companion_audit: "tests/hourly_20260625_1702_cycle2_ptuj_branch_field_completion_matrix_audit.py"
---

# Hourly 20260625 1702 Cycle 2 PTUJ Branch Field Completion Matrix

## 1. Verdict.

Verdict: **blocked**.

Cycle 1's PTUJ blocker converts into a strict two-branch field-completion
matrix with zero accepted branches. The two allowed branches remain:

1. official/custodian formula-bearing source asset; and
2. lawful local byte/toolchain/output manifest.

Both branches have only the target-import guard as a present admissibility
field. The official branch also has locator/provenance metadata, but that is
metadata-only and cannot be promoted into a source asset receipt. The local
branch has a schema from predecessor artifacts, but the schema is not a byte
object, toolchain identity, decode scope, or output manifest.

Decision state:

```text
accepted_branch_count: 0
accepted_receipt_count: 0
formula_visibility_allowed: false
keating_identity_allowed: false
proof_restart_allowed: false
target_import_used: false
metadata_as_receipt_promotion: false
```

The exact fields that must be produced before formula visibility or Keating
identity can start are:

```text
Official branch:
custodian_source_asset_record
asset_kind
immutable_locator_or_path
content_access
checksum_or_custody_record
formula_visibility_scope

Local branch:
lawful_basis
source_byte_object
source_byte_checksum
acquisition_tool_identity
decoder_tool_identity
decode_scope
output_manifest
output_checksums
```

At least one full branch must be completed. Mixing partial fields across the
two branches does not create an accepted receipt.

## 2. Sources read and directly derived facts.

| source | directly derived fact |
| --- | --- |
| `RESEARCH-POSTURE.md` | Process discipline, compatibility, and provenance are not proof evidence; target data must not be hidden inside reconstruction. |
| `process/runbooks/five-lane-frontier-run.md` | The lane must name the exact missing object and prevent hosted/compatible material from becoming derived. |
| `process/runbooks/three-cycle-fifteen-hole-run.md` | A quality hole must expose the missing proof/source object whose closure would change the reconstruction state. |
| `explorations/hourly-20260625-1702-cycle1-ptuj-accepted-source-object-branch-receipt.md` | Cycle 1 records zero accepted receipts and rejects both official/custodian and lawful local branches. |
| `tests/hourly_20260625_1702_cycle1_ptuj_accepted_source_object_branch_receipt_audit.py` | The predecessor audit enforces two branch rows, zero accepted branch count, no proof restart, no target import, and no metadata-as-source promotion. |
| `explorations/hourly-20260625-1602-cycle2-ptuj-source-object-admission-packet.md` | The exact branch targets and required fields are already specified, but no current repo object satisfies either branch. |

Focused repo-local checks performed in this lane:

| check | result | consequence |
| --- | --- | --- |
| `git status --short --branch` | Only existing untracked `automation/tmp/` material was visible outside this owned scope. | No parallel-worker file was edited. |
| `rg --files` filtered for PTUJ, `TzSEvmqxu48`, Pull That Up Jamie, media extensions, manifests, and checksum terms. | Found prior PTUJ artifacts and audits; no local PTUJ media bytes, frame packet, checksum manifest, source package, or formula-bearing asset candidate. | No local branch field can be marked present except the target-import guard. |
| Text scan for PTUJ/source-object/accepted-branch/formula-visibility/Keating terms. | Found only prior blocked decisions and receipt contracts. | No branch can be promoted by newer repo evidence. |

Derived facts:

1. `TzSEvmqxu48` remains the target PTUJ locator.
2. Locator, oEmbed, thumbnail, caption, storyboard, and official-page
   provenance records are metadata or preview evidence only.
3. No official/custodian formula-bearing source asset manifest is present.
4. No lawful local PTUJ source-byte object, byte checksum, acquisition tool
   identity, decoder identity, decode scope, output manifest, or output checksum
   set is present.
5. Formula visibility and Keating identity comparison are downstream of one
   accepted branch receipt, not ways to construct the source object.

## 3. Strongest positive construction attempt.

The strongest positive construction is not a receipt. It is a complete
admission matrix that separates the two admissible branches and assigns every
required field one of four statuses:

```text
present
missing
blocked
metadata_only
```

For the official/custodian branch, the strongest candidate is:

```text
official_PTUJ_provenance_and_TzSEvmqxu48_locator_metadata_continuity
```

This supplies a target locator and some custodian-context metadata. It does not
identify a formula-bearing source asset, provide content access, provide a
checksum/custody record, or define the formula visibility scope.

For the lawful local branch, the strongest candidate is:

```text
prior_schema_for_lawful_source_byte_toolchain_decode_scope_and_output_manifest
```

This supplies the shape of a valid receipt. It does not supply the lawful bytes,
checksum, acquisition tool, decoder, decode scope, output manifest, or output
checksums.

The constructive gain is therefore precision: the blocker is no longer "get
PTUJ" in general. It is a finite missing-field set for two mutually sufficient
branch completions.

## 4. First exact obstruction/missing field set.

The first exact obstruction is:

```text
no_branch_has_all_required_fields_present_without_metadata_as_receipt_promotion
```

The official/custodian branch is blocked by this missing field set:

```text
custodian_source_asset_record
asset_kind
immutable_locator_or_path
content_access
checksum_or_custody_record
formula_visibility_scope
```

The lawful local branch is blocked by this missing field set:

```text
lawful_basis
source_byte_object
source_byte_checksum
acquisition_tool_identity
decoder_tool_identity
decode_scope
output_manifest
output_checksums
```

The first field that prevents formula visibility is `content_access` in the
official branch or `source_byte_object` plus `decode_scope` in the lawful local
branch. The first field that prevents Keating identity is
`formula_visibility_scope` in the official branch or `output_manifest` plus
`output_checksums` in the lawful local branch.

## 5. Constructive next object.

The constructive next object is:

```text
PTUJ_BRANCH_FIELD_COMPLETION_RECEIPT
```

Minimum success condition:

```text
accepted_branch_count == 1
accepted_receipt_count == 1
exactly_one_branch_row.status == "accepted"
all_required_fields_for_that_branch.status == "present"
target_import_used == false
metadata_as_receipt_promotion == false
```

If completed through the official/custodian branch, the receipt must include a
formula-bearing asset record with content access, checksum or custody, and
formula visibility scope. If completed through the lawful local branch, the
receipt must include the lawful source-byte object, checksummed source bytes,
acquisition and decoder identities, decode scope, checksummed output manifest,
and output checksums.

## 6. Consequence for PTUJ/GU claims.

PTUJ remains blocked before formula visibility. This result does not refute GU,
does not show the formula is absent, and does not compare PTUJ with any Keating
sheet. It only says the repo has not yet produced the source object required to
inspect PTUJ content.

Promotion firewall:

```text
PTUJ_formula_visibility_allowed: false
Keating_identity_allowed: false
IG_selector_route_allowed: false
proof_restart_allowed: false
target_import_used: false
metadata_as_receipt_promotion: false
```

Downstream PTUJ/GU claims remain non-evaluable from this route until one branch
is fully completed.

## 7. Next computation/proof step.

The next step is source-object production, not proof replay:

```text
Produce one complete PTUJ_BRANCH_FIELD_COMPLETION_RECEIPT row for either the
official/custodian branch or the lawful local branch, then run a separate PTUJ
formula visibility audit.
```

The visibility audit should not start until the branch matrix has exactly one
accepted row.

## 8. Machine-readable JSON summary with branch_rows and field_rows.

```json
{
  "artifact": "PTUJ_BRANCH_FIELD_COMPLETION_MATRIX_1702_C2_L1_V1",
  "artifact_id": "PTUJ_BRANCH_FIELD_COMPLETION_MATRIX_1702_C2_L1_V1",
  "run_id": "hourly-20260625-1702",
  "cycle": 2,
  "lane": 1,
  "verdict": "blocked",
  "verdict_class": "blocked",
  "owned_path": "explorations/hourly-20260625-1702-cycle2-ptuj-branch-field-completion-matrix.md",
  "companion_audit": "tests/hourly_20260625_1702_cycle2_ptuj_branch_field_completion_matrix_audit.py",
  "target_video_id": "TzSEvmqxu48",
  "target_asset_id": "PullThatUpJamie_GUForGRGaugeTheory_TzSEvmqxu48",
  "accepted_branch_count": 0,
  "accepted_receipt_count": 0,
  "proof_restart_allowed": false,
  "target_import_used": false,
  "target_import_used_for_selection": false,
  "target_import_guard": true,
  "formula_visibility_allowed": false,
  "keating_identity_allowed": false,
  "ptuj_formula_promotion_allowed": false,
  "ig_selector_route_allowed": false,
  "claim_promotion_allowed": false,
  "metadata_as_receipt_promotion": false,
  "admission_rule": {
    "accept_if_all_required_fields_present": true,
    "accepted_branch_count_required_for_restart": 1,
    "exactly_one_accepted_branch_required": true,
    "branch_conflation_allowed": false,
    "metadata_or_locator_can_satisfy_source_object": false,
    "schema_can_satisfy_object": false
  },
  "branch_rows": [
    {
      "row_id": "official_custodian_formula_source_asset",
      "branch": "official_custodian",
      "target_object": "OfficialTzSEvmqxu48FormulaSourceAssetPacket_V1.source_asset_object_manifest",
      "strongest_current_candidate": "official_PTUJ_provenance_and_TzSEvmqxu48_locator_metadata_continuity",
      "status": "rejected_blocked",
      "accepted": false,
      "blocked": true,
      "accepted_receipt_count": 0,
      "required_field_count": 7,
      "present_required_field_count": 1,
      "missing_required_field_count": 6,
      "metadata_only_field_count": 2,
      "blocked_field_count": 4,
      "required_fields_present": [
        "target_import_guard"
      ],
      "required_fields_missing": [
        "custodian_source_asset_record",
        "asset_kind",
        "immutable_locator_or_path",
        "content_access",
        "checksum_or_custody_record",
        "formula_visibility_scope"
      ],
      "metadata_only_fields": [
        "custodian_context_metadata",
        "ordinary_locator_metadata"
      ],
      "blocked_fields": [
        "content_access",
        "checksum_or_custody_record",
        "formula_visibility_scope",
        "immutable_locator_or_path"
      ],
      "first_missing_field": "custodian_source_asset_record",
      "first_obstruction": "official_branch_has_locator_metadata_but_no_formula_bearing_source_asset_manifest",
      "formula_visibility_allowed": false,
      "keating_identity_allowed": false,
      "proof_restart_allowed": false
    },
    {
      "row_id": "lawful_local_byte_toolchain_output_manifest",
      "branch": "lawful_local",
      "target_object": "LawfulLocalTzSEvmqxu48FrameExtractor_V1.toolchain_identity_and_output_manifest",
      "strongest_current_candidate": "prior_schema_for_lawful_source_byte_toolchain_decode_scope_and_output_manifest",
      "status": "rejected_blocked",
      "accepted": false,
      "blocked": true,
      "accepted_receipt_count": 0,
      "required_field_count": 9,
      "present_required_field_count": 1,
      "missing_required_field_count": 8,
      "metadata_only_field_count": 1,
      "blocked_field_count": 7,
      "required_fields_present": [
        "target_import_guard"
      ],
      "required_fields_missing": [
        "lawful_basis",
        "source_byte_object",
        "source_byte_checksum",
        "acquisition_tool_identity",
        "decoder_tool_identity",
        "decode_scope",
        "output_manifest",
        "output_checksums"
      ],
      "metadata_only_fields": [
        "receipt_schema"
      ],
      "blocked_fields": [
        "source_byte_object",
        "source_byte_checksum",
        "acquisition_tool_identity",
        "decoder_tool_identity",
        "decode_scope",
        "output_manifest",
        "output_checksums"
      ],
      "first_missing_field": "lawful_basis",
      "first_obstruction": "lawful_local_branch_has_schema_but_no_source_bytes_toolchain_or_outputs",
      "formula_visibility_allowed": false,
      "keating_identity_allowed": false,
      "proof_restart_allowed": false
    }
  ],
  "field_rows": [
    {
      "branch_row_id": "official_custodian_formula_source_asset",
      "field": "custodian_source_asset_record",
      "status": "missing",
      "required": true,
      "current_evidence": "official_PTUJ_page_and_TzSEvmqxu48_locator_context_only",
      "metadata_only": true,
      "receipt_promoted": false,
      "must_produce_before_formula_visibility": true,
      "must_produce_before_keating_identity": true
    },
    {
      "branch_row_id": "official_custodian_formula_source_asset",
      "field": "asset_kind",
      "status": "missing",
      "required": true,
      "current_evidence": "no_source_video_package_frame_sequence_sheet_scan_still_or_source_page_asset_named",
      "metadata_only": false,
      "receipt_promoted": false,
      "must_produce_before_formula_visibility": true,
      "must_produce_before_keating_identity": true
    },
    {
      "branch_row_id": "official_custodian_formula_source_asset",
      "field": "immutable_locator_or_path",
      "status": "blocked",
      "required": true,
      "current_evidence": "ordinary_webpage_embed_watch_and_oembed_locators_do_not_identify_a_source_asset",
      "metadata_only": true,
      "receipt_promoted": false,
      "must_produce_before_formula_visibility": true,
      "must_produce_before_keating_identity": true
    },
    {
      "branch_row_id": "official_custodian_formula_source_asset",
      "field": "content_access",
      "status": "blocked",
      "required": true,
      "current_evidence": "no_inspectable_formula_bearing_content_access_method",
      "metadata_only": false,
      "receipt_promoted": false,
      "must_produce_before_formula_visibility": true,
      "must_produce_before_keating_identity": true
    },
    {
      "branch_row_id": "official_custodian_formula_source_asset",
      "field": "checksum_or_custody_record",
      "status": "blocked",
      "required": true,
      "current_evidence": "no_checksum_size_or_custody_record_for_a_source_asset",
      "metadata_only": false,
      "receipt_promoted": false,
      "must_produce_before_formula_visibility": true,
      "must_produce_before_keating_identity": true
    },
    {
      "branch_row_id": "official_custodian_formula_source_asset",
      "field": "formula_visibility_scope",
      "status": "blocked",
      "required": true,
      "current_evidence": "no_timecode_frame_id_sheet_id_source_page_id_or_full_asset_audit_scope",
      "metadata_only": false,
      "receipt_promoted": false,
      "must_produce_before_formula_visibility": true,
      "must_produce_before_keating_identity": true
    },
    {
      "branch_row_id": "official_custodian_formula_source_asset",
      "field": "target_import_guard",
      "status": "present",
      "required": true,
      "current_evidence": "predecessor_and_current_lane_state_downstream_physics_was_not_used_to_select_or_normalize_source_object",
      "metadata_only": false,
      "receipt_promoted": false,
      "must_produce_before_formula_visibility": false,
      "must_produce_before_keating_identity": false
    },
    {
      "branch_row_id": "lawful_local_byte_toolchain_output_manifest",
      "field": "lawful_basis",
      "status": "missing",
      "required": true,
      "current_evidence": "no_lawful_basis_attached_to_any_concrete_repo_local_byte_object",
      "metadata_only": false,
      "receipt_promoted": false,
      "must_produce_before_formula_visibility": true,
      "must_produce_before_keating_identity": true
    },
    {
      "branch_row_id": "lawful_local_byte_toolchain_output_manifest",
      "field": "source_byte_object",
      "status": "blocked",
      "required": true,
      "current_evidence": "no_repo_local_TzSEvmqxu48_source_bytes_or_source_package",
      "metadata_only": false,
      "receipt_promoted": false,
      "must_produce_before_formula_visibility": true,
      "must_produce_before_keating_identity": true
    },
    {
      "branch_row_id": "lawful_local_byte_toolchain_output_manifest",
      "field": "source_byte_checksum",
      "status": "blocked",
      "required": true,
      "current_evidence": "no_source_byte_object_so_no_sha256_or_size",
      "metadata_only": false,
      "receipt_promoted": false,
      "must_produce_before_formula_visibility": true,
      "must_produce_before_keating_identity": true
    },
    {
      "branch_row_id": "lawful_local_byte_toolchain_output_manifest",
      "field": "acquisition_tool_identity",
      "status": "blocked",
      "required": true,
      "current_evidence": "no_admitted_acquisition_executable_module_version_provenance_or_command_line",
      "metadata_only": false,
      "receipt_promoted": false,
      "must_produce_before_formula_visibility": true,
      "must_produce_before_keating_identity": true
    },
    {
      "branch_row_id": "lawful_local_byte_toolchain_output_manifest",
      "field": "decoder_tool_identity",
      "status": "blocked",
      "required": true,
      "current_evidence": "no_admitted_decoder_extractor_executable_module_version_provenance_or_command_line",
      "metadata_only": false,
      "receipt_promoted": false,
      "must_produce_before_formula_visibility": true,
      "must_produce_before_keating_identity": true
    },
    {
      "branch_row_id": "lawful_local_byte_toolchain_output_manifest",
      "field": "decode_scope",
      "status": "blocked",
      "required": true,
      "current_evidence": "no_full_asset_or_time_window_sampling_rule",
      "metadata_only": false,
      "receipt_promoted": false,
      "must_produce_before_formula_visibility": true,
      "must_produce_before_keating_identity": true
    },
    {
      "branch_row_id": "lawful_local_byte_toolchain_output_manifest",
      "field": "output_manifest",
      "status": "blocked",
      "required": true,
      "current_evidence": "no_generated_frame_or_source_output_paths_timecodes_dimensions_sizes_or_commands",
      "metadata_only": false,
      "receipt_promoted": false,
      "must_produce_before_formula_visibility": true,
      "must_produce_before_keating_identity": true
    },
    {
      "branch_row_id": "lawful_local_byte_toolchain_output_manifest",
      "field": "output_checksums",
      "status": "blocked",
      "required": true,
      "current_evidence": "no_output_manifest_so_no_output_sha256_set",
      "metadata_only": false,
      "receipt_promoted": false,
      "must_produce_before_formula_visibility": true,
      "must_produce_before_keating_identity": true
    },
    {
      "branch_row_id": "lawful_local_byte_toolchain_output_manifest",
      "field": "target_import_guard",
      "status": "present",
      "required": true,
      "current_evidence": "predecessor_and_current_lane_state_downstream_physics_was_not_used_to_select_or_normalize_source_object",
      "metadata_only": false,
      "receipt_promoted": false,
      "must_produce_before_formula_visibility": false,
      "must_produce_before_keating_identity": false
    }
  ],
  "first_obstruction": "no_branch_has_all_required_fields_present_without_metadata_as_receipt_promotion",
  "first_exact_obstruction": {
    "official_branch_missing_fields": [
      "custodian_source_asset_record",
      "asset_kind",
      "immutable_locator_or_path",
      "content_access",
      "checksum_or_custody_record",
      "formula_visibility_scope"
    ],
    "local_branch_missing_fields": [
      "lawful_basis",
      "source_byte_object",
      "source_byte_checksum",
      "acquisition_tool_identity",
      "decoder_tool_identity",
      "decode_scope",
      "output_manifest",
      "output_checksums"
    ]
  },
  "next_object": "PTUJ_BRANCH_FIELD_COMPLETION_RECEIPT",
  "constructive_next_object": "PTUJ_BRANCH_FIELD_COMPLETION_RECEIPT",
  "next_object_explicit": true,
  "next_computation_or_proof_step": "produce_one_complete_branch_field_completion_receipt_then_run_separate_PTUJ_formula_visibility_audit",
  "ptuj_gu_claim_consequence": {
    "formula_packet_status": "blocked_before_source_object_completion",
    "visibility_audit_enabled": false,
    "keating_identity_status": "not_evaluable_until_one_branch_field_set_is_complete",
    "ig_selector_route_status": "not_admissible_without_PTUJ_source_packet_and_identity_bridge",
    "major_gu_claim_promoted": false,
    "global_no_go_promoted": false,
    "proof_restart_allowed": false
  },
  "promotion_firewall": {
    "metadata_as_receipt_promotion": false,
    "locator_as_source_object": false,
    "oembed_as_source_object": false,
    "thumbnail_as_source_object": false,
    "caption_as_source_object": false,
    "storyboard_as_source_object": false,
    "schema_as_source_object": false,
    "target_physics_as_source_selector": false,
    "ptuj_formula_promotion": false,
    "keating_identity_promotion": false,
    "proof_restart": false
  }
}
```
