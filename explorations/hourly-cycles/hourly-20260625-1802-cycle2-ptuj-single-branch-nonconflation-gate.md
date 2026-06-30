---
title: "Hourly 20260625 1802 Cycle 2 PTUJ Single Branch Nonconflation Gate"
date: "2026-06-25"
run_id: "hourly-20260625-1802"
cycle: 2
lane: 1
doc_type: ptuj_single_branch_nonconflation_gate
artifact_id: "PTUJ_SINGLE_BRANCH_NONCONFLATION_GATE_1802_C2_L1_V1"
verdict: "blocked"
owned_path: "explorations/hourly-20260625-1802-cycle2-ptuj-single-branch-nonconflation-gate.md"
companion_audit: "tests/hourly_20260625_1802_cycle2_ptuj_single_branch_nonconflation_gate_audit.py"
---

# Hourly 20260625 1802 Cycle 2 PTUJ Single Branch Nonconflation Gate

## 1. Verdict.

Verdict: **blocked**.

PTUJ branch admission cannot be achieved by assembling partial fields from the
official/custodian branch and partial fields from the lawful local branch. It
also cannot be achieved by treating metadata, locator continuity, oEmbed/watch
surfaces, thumbnail/storyboard continuity, schema continuity, or downstream
Keating/GU use as a receipt.

The single-branch nonconflation rule is:

```text
PTUJ acceptance requires exactly one complete branch receipt. A receipt is
accepted only when all required fields for one branch are present inside that
same branch, with target import unused and metadata-as-receipt promotion false.
Cross-branch assembly is not an admissible receipt.
```

Decision state:

```text
branch_candidate_count: 2
accepted_branch_count: 0
accepted_receipt_count: 0
cross_branch_conflation_allowed: false
metadata_as_receipt_allowed: false
formula_visibility_allowed: false
keating_comparison_allowed: false
proof_restart_allowed: false
```

This is not a PTUJ formula-negative result. It blocks before a formula-bearing
PTUJ source object is admitted.

## 2. What was derived directly from repo sources.

| source | directly derived fact |
| --- | --- |
| `RESEARCH-POSTURE.md` | The repo may pursue GU constructively, but must not promote compatibility, process discipline, metadata, or target data into proof evidence. |
| `process/runbooks/five-lane-frontier-run.md` | A lane must name an exact obstruction or missing proof/source object, and must not let "compatible with" become "derived from". |
| `process/runbooks/three-cycle-fifteen-hole-run.md` | A quality hole may separate currently conflated branches and must identify the next object whose production would change the state. |
| `explorations/hourly-20260625-1702-cycle2-ptuj-branch-field-completion-matrix.md` | PTUJ has exactly two allowed branch candidates, both with zero accepted receipts; at least one full branch must be completed before formula visibility or Keating comparison. |
| `explorations/hourly-20260625-1802-cycle1-ptuj-branch-field-completion-receipt.md` | The 1802 cycle 1 receipt attempt found zero accepted branches and zero accepted receipts; official/custodian metadata and lawful local schema remain insufficient. |
| `tests/hourly_20260625_1802_cycle1_ptuj_branch_field_completion_receipt_audit.py` | The predecessor audit enforces two branch rows, zero accepted counts, no metadata-as-receipt promotion, and no proof restart unless exactly one branch is accepted. |

The two branch candidates inherited by this gate are:

1. `official_custodian_formula_source_asset`: a custodian formula-bearing source asset packet.
2. `lawful_local_byte_toolchain_output_manifest`: a lawful local source-byte, toolchain, decode-scope, output-manifest packet.

Both are admissible branch types. Neither is currently complete.

## 3. Strongest positive construction attempt.

The strongest positive construction is the mixed-field attempt:

```text
official/custodian locator and provenance continuity
+ lawful local branch schema and target-import guard
+ downstream desire to compare with Keating material
```

This construction has real orientation value. It identifies the PTUJ target
surface (`TzSEvmqxu48`), preserves a custodian-context path for an official
asset, and preserves the schema for a lawful local acquisition/decode/output
receipt. It also keeps the target-import guard explicit.

However, the construction does not yield an accepted receipt, because its
fields live in different branches and some of them are metadata-only:

| attempted component | branch home | admissible role | why it does not accept |
| --- | --- | --- | --- |
| `TzSEvmqxu48` locator and official/custodian context | official/custodian | target and provenance orientation | not a formula-bearing source asset with content access and custody/checksum |
| thumbnail, storyboard, oEmbed, watch-page continuity | official/custodian metadata surface | weak continuity evidence | metadata or preview surfaces are not a source object receipt |
| lawful local branch schema | lawful local | receipt shape | a schema is not source bytes, a decoder identity, a decode scope, outputs, or checksums |
| target-import guard | both branches | necessary firewall | necessary but not sufficient for acceptance |
| Keating comparison need | downstream consumer | proof motivation | downstream use cannot supply a PTUJ receipt field |

The positive result is therefore a rule, not an acceptance: a branch may inherit
only its own complete field set. Partial official/custodian metadata cannot
complete the lawful local branch, and partial lawful local schema cannot
complete the official/custodian branch.

## 4. First exact obstruction/missing object.

The first exact obstruction is:

```text
no_single_branch_contains_all_required_receipt_fields
```

The first rule obstruction is:

```text
cross_branch_assembly_is_not_a_receipt
```

The official/custodian branch remains missing:

```text
custodian_source_asset_record
asset_kind
immutable_locator_or_path
content_access
checksum_or_custody_record
formula_visibility_scope
```

The lawful local branch remains missing:

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

The block would be falsified by producing a single branch packet in which every
required field for that branch is present and internally tied to the same PTUJ
source object, while `target_import_used == false` and
`metadata_as_receipt_allowed == false`.

## 5. Constructive next object.

The next object is a **single complete branch receipt**:

```text
SingleCompletePTUJBranchReceipt_V1
```

It may instantiate exactly one of these forms:

1. `OfficialTzSEvmqxu48FormulaSourceAssetPacket_V1.source_asset_object_manifest`
2. `LawfulLocalTzSEvmqxu48FrameExtractor_V1.toolchain_identity_and_output_manifest`

Minimum acceptance condition:

```text
branch_candidate_count == 2
accepted_branch_count == 1
accepted_receipt_count == 1
all_required_fields_for_the_accepted_branch_present == true
all_accepted_fields_belong_to_the_same_branch == true
cross_branch_conflation_allowed == false
metadata_as_receipt_allowed == false
target_import_used == false
```

The current run does not produce that object. It names it as the exact next
source object needed.

## 6. Consequence for PTUJ formula visibility, Keating comparison, proof restart.

PTUJ formula visibility remains blocked. The repo has a target and branch
contract, but not a source object that may be inspected for a formula.

Keating comparison remains blocked. A comparison needs an admitted PTUJ source
branch plus a visible formula, frame, source asset, or decoded output. Metadata
continuity alone cannot be compared to Keating content as PTUJ formula
evidence.

Proof restart remains forbidden. There are zero accepted PTUJ branch receipts,
and cross-branch assembly may not be used to manufacture the one accepted
receipt required for restart.

## 7. Next proof/source step.

Run a producer step, not a downstream proof step:

```text
produce_SingleCompletePTUJBranchReceipt_V1_for_exactly_one_branch
```

The producer must either obtain an official/custodian formula-bearing source
asset packet with content access, custody/checksum, and formula visibility
scope, or obtain a lawful local source-byte/toolchain/decode/output manifest
with source and output checksums. After that one object exists, run a separate
PTUJ formula visibility audit.

## 8. Machine-readable JSON summary.

```json
{
  "artifact": "PTUJ_SINGLE_BRANCH_NONCONFLATION_GATE_1802_C2_L1_V1",
  "artifact_id": "PTUJ_SINGLE_BRANCH_NONCONFLATION_GATE_1802_C2_L1_V1",
  "run_id": "hourly-20260625-1802",
  "cycle": 2,
  "lane": 1,
  "verdict": "blocked",
  "verdict_class": "blocked",
  "owned_path": "explorations/hourly-20260625-1802-cycle2-ptuj-single-branch-nonconflation-gate.md",
  "companion_audit": "tests/hourly_20260625_1802_cycle2_ptuj_single_branch_nonconflation_gate_audit.py",
  "target_video_id": "TzSEvmqxu48",
  "gate": "PTUJ_SINGLE_BRANCH_NONCONFLATION_GATE",
  "branch_candidate_count": 2,
  "branch_candidates": [
    {
      "row_id": "official_custodian_formula_source_asset",
      "branch_object": "OfficialTzSEvmqxu48FormulaSourceAssetPacket_V1.source_asset_object_manifest",
      "status": "rejected_blocked",
      "accepted": false,
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
      "metadata_only_inputs": [
        "TzSEvmqxu48_locator_continuity",
        "official_custodian_context",
        "thumbnail_storyboard_oembed_watch_page_surfaces"
      ],
      "metadata_as_receipt_allowed": false,
      "formula_visibility_allowed": false,
      "proof_restart_allowed": false
    },
    {
      "row_id": "lawful_local_byte_toolchain_output_manifest",
      "branch_object": "LawfulLocalTzSEvmqxu48FrameExtractor_V1.toolchain_identity_and_output_manifest",
      "status": "rejected_blocked",
      "accepted": false,
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
      "metadata_only_inputs": [
        "receipt_schema_without_bytes_tools_or_outputs"
      ],
      "metadata_as_receipt_allowed": false,
      "formula_visibility_allowed": false,
      "proof_restart_allowed": false
    }
  ],
  "attempted_mixed_construction": {
    "official_partial_fields": [
      "locator_continuity",
      "custodian_context_metadata",
      "preview_surface_metadata"
    ],
    "lawful_local_partial_fields": [
      "receipt_schema",
      "target_import_guard"
    ],
    "downstream_consumer_pressure": [
      "Keating_comparison",
      "proof_restart"
    ],
    "accepted": false,
    "rejection_reason": "cross_branch_assembly_is_not_a_receipt"
  },
  "accepted_branch_count": 0,
  "accepted_receipt_count": 0,
  "single_complete_branch_required": true,
  "exactly_one_complete_branch_required_for_acceptance": true,
  "cross_branch_conflation_allowed": false,
  "branch_conflation_allowed": false,
  "metadata_as_receipt_allowed": false,
  "metadata_as_receipt_promotion": false,
  "metadata_or_locator_continuity_as_receipt_allowed": false,
  "locator_continuity_as_receipt_allowed": false,
  "schema_as_receipt_allowed": false,
  "target_import_guard": true,
  "target_import_used": false,
  "proof_restart_allowed": false,
  "formula_visibility_allowed": false,
  "keating_comparison_allowed": false,
  "ig_selector_route_allowed": false,
  "first_obstruction": "no_single_branch_contains_all_required_receipt_fields",
  "rule_obstruction": "cross_branch_assembly_is_not_a_receipt",
  "falsifies_block_if": {
    "object_id": "SingleCompletePTUJBranchReceipt_V1",
    "accepted_branch_count": 1,
    "accepted_receipt_count": 1,
    "all_required_fields_for_one_branch_present": true,
    "all_accepted_fields_belong_to_same_branch": true,
    "target_import_used": false,
    "metadata_as_receipt_allowed": false,
    "cross_branch_conflation_allowed": false
  },
  "next_object": {
    "id": "SingleCompletePTUJBranchReceipt_V1",
    "description": "a single complete branch receipt for exactly one PTUJ branch",
    "is_single_complete_branch_receipt": true,
    "accepted_branch_count_required": 1,
    "accepted_receipt_count_required": 1,
    "allowed_instantiations": [
      "OfficialTzSEvmqxu48FormulaSourceAssetPacket_V1.source_asset_object_manifest",
      "LawfulLocalTzSEvmqxu48FrameExtractor_V1.toolchain_identity_and_output_manifest"
    ],
    "forbidden_instantiation": "mixed_official_metadata_plus_lawful_local_schema",
    "must_not_use": [
      "cross_branch_assembly",
      "metadata_as_receipt",
      "locator_continuity_as_receipt",
      "downstream_keating_or_proof_restart_need_as_receipt"
    ]
  },
  "ptuj_formula_visibility": "blocked_until_single_complete_branch_receipt_is_accepted",
  "keating_comparison": "blocked_until_single_complete_branch_receipt_and_formula_visibility_audit",
  "proof_restart": "forbidden_until_exactly_one_complete_branch_receipt_is_accepted",
  "next_proof_source_step": "produce_SingleCompletePTUJBranchReceipt_V1_for_exactly_one_branch_then_run_separate_formula_visibility_audit"
}
```
