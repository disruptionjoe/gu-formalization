---
title: "Hourly 20260625 2302 Cycle 2 PTUJ Branch Purity Audit Gate"
date: "2026-06-25"
run_id: "hourly-20260625-2302"
cycle: 2
lane: "PTUJ"
doc_type: "frontier_gate"
artifact_id: "PTUJBranchPurityAuditGate_2302_C2_LPTUJ_V1"
verdict: "blocked"
owned_path: "explorations/hourly-20260625-2302-cycle2-ptuj-branch-purity-audit-gate.md"
---

# Hourly 20260625 2302 Cycle 2 PTUJ Branch Purity Audit Gate

## Verdict

Verdict: **blocked**.

Cycle 1 produced the correct producer contract. Cycle 2 turns it into an
admission gate:

```text
SingleCompletePTUJBranchReceipt_V1 is acceptable iff exactly one allowed PTUJ
branch is complete, every accepted field belongs to that same branch, all
branch-required fields are present inside that branch, and no target data,
downstream formula visibility, or cross-branch field assembly is used.
```

The current repo cannot satisfy this invariant. The official/custodian branch
still has no admitted custodian formula-bearing source asset manifest. The
lawful-local branch still has no concrete lawful source byte object, no
toolchain identity, no decode scope, no output manifest, and no checksums.

Decision state:

```text
branch_purity_invariant_defined: true
branch_purity_invariant_satisfied: false
accepted_branch_count: 0
accepted_receipt_count: 0
official_branch_complete: false
lawful_local_branch_complete: false
mixed_branch_packet_rejected: true
cross_branch_assembly_allowed: false
formula_visibility_allowed: false
proof_restart_allowed: false
target_import_used: false
```

This is not a formula-visibility result, not a Keating/Shiab comparison result,
and not a PTUJ no-go. It is a producer-layer admission gate.

## Direct Source Derivation

From `RESEARCH-POSTURE.md`, target data, compatibility, metadata, and process
discipline cannot be promoted into a reconstruction receipt. A blocked
derivation must name the constructive object that would remove the obstruction.

From `process/runbooks/five-lane-frontier-run.md`, this lane must produce a
decision-grade result, name the first missing proof or source object, and avoid
turning "compatible with" into "derived from".

From
`explorations/hourly-20260625-2302-cycle1-ptuj-single-branch-producer-contract.md`,
the cycle 1 contract is:

```text
SingleCompletePTUJBranchReceipt_V1 is admissible iff exactly one allowed
producer branch supplies every required field inside that same branch, with
target_import_used == false and cross_branch_assembly_allowed == false.
```

That contract is consumed here as the direct predecessor and sharpened into the
following machine-checkable invariant:

```text
branch_purity_accepts(receipt) :=
  branch_candidate_count == 2
  and accepted_branch_count == 1
  and accepted_receipt_count == 1
  and exactly_one(
        official_branch_complete,
        lawful_local_branch_complete
      )
  and all_required_fields_for_accepted_branch_present == true
  and all_accepted_fields_belong_to_the_accepted_branch == true
  and official_fields_used_in_lawful_local_branch == false
  and lawful_local_fields_used_in_official_branch == false
  and target_import_used == false
  and cross_branch_assembly_allowed == false
  and metadata_as_receipt_allowed == false
  and formula_visibility_used_to_backfill_producer_fields == false
  and downstream_proof_need_used_as_receipt_field == false
```

From
`explorations/hourly-20260625-2202-cycle2-ptuj-branch-exclusivity-gate.md`,
the official/custodian branch and lawful-local branch are alternatives, not
parts of a composite receipt. A mixed packet is rejected even if its fields are
individually useful.

From
`explorations/hourly-20260625-2104-cycle2-ptuj-branch-local-source-packet-gate.md`,
the two allowed branch objects and field ledgers are:

| branch | branch object | current first missing field |
|---|---|---|
| official/custodian | `OfficialTzSEvmqxu48FormulaSourceAssetPacket_V1.source_asset_object_manifest` | `custodian_source_asset_record` |
| lawful local | `LawfulLocalTzSEvmqxu48FrameExtractor_V1.toolchain_identity_and_output_manifest` | `lawful_basis_for_a_concrete_source_byte_object` |

Focused current-tree checks performed for this lane:

| check | result | consequence |
|---|---|---|
| `git status --short` | Only preexisting untracked `automation/tmp/` was reported before this artifact was added. | No unrelated current change was treated as a PTUJ receipt. |
| Target path existence check | The assigned artifact path did not already exist. | This lane created only its owned file. |
| Non-artifact `rg` for `TzSEvmqxu48`, `SingleCompletePTUJBranchReceipt_V1`, branch object names, source bytes, and output manifests excluding `explorations/`, `tests/`, and `automation/tmp/` | No hits. | The repo has no non-artifact PTUJ source-byte, source-asset, or output-manifest object to admit. |
| Non-artifact file-name scan for PTUJ, `TzSEvmqxu48`, source-byte, manifest, custodian, formula-source, extractor, and checksum terms excluding `explorations/`, `tests/`, and `automation/tmp/` | No hits. | No candidate producer asset is present outside historical notes and tests. |
| PTUJ accepted-count scan | Hits for count `1` were rollback or would-change conditions in prior PTUJ artifacts, not actual accepted rows. Current PTUJ summaries report zero accepted counts. | No earlier PTUJ artifact supplies an accepted branch receipt. |
| `sources/media-index.md` | `GU-MEDIA-2021-PULL-THAT-UP-JAMIE` is a metadata-checked pointer to visuals, not a formal source receipt. | Official orientation exists, but not source-asset admission. |

## Strongest Positive Attempt

The strongest positive result is a complete, auditable intake predicate, not an
accepted packet. It is strong because it can reject every known bypass while
leaving both legitimate producer routes open.

Official/custodian branch attempt:

```text
candidate_branch:
  OfficialTzSEvmqxu48FormulaSourceAssetPacket_V1.source_asset_object_manifest

positive_material:
  target_video_id: TzSEvmqxu48
  source_surface: GU-MEDIA-2021-PULL-THAT-UP-JAMIE
  source_surface_status: metadata-checked
  target_import_guard: present as a rule
```

Required official branch fields:

| field | status |
|---|---|
| `custodian_source_asset_record` | missing |
| `asset_kind` | missing |
| `immutable_locator_or_path` | not admitted as a source asset object |
| `content_access` | missing |
| `checksum_or_custody_record` | missing |
| `formula_visibility_scope` | missing |
| `target_import_guard` | present as a guard, not sufficient for acceptance |

Lawful-local branch attempt:

```text
candidate_branch:
  LawfulLocalTzSEvmqxu48FrameExtractor_V1.toolchain_identity_and_output_manifest

positive_material:
  branch_schema: present in prior PTUJ gates
  target_import_guard: present as a rule
```

Required lawful-local branch fields:

| field | status |
|---|---|
| `lawful_basis` | missing for any concrete source byte object |
| `source_byte_object` | missing |
| `source_byte_checksum` | missing |
| `acquisition_tool_identity` | missing |
| `decoder_tool_identity` | missing |
| `decode_scope` | missing |
| `output_manifest` | missing |
| `output_checksums` | missing |
| `target_import_guard` | present as a guard, not sufficient for acceptance |

The strongest mixed attempt is:

```text
official target/provenance locator
+ lawful-local branch schema
+ downstream need for formula visibility or proof restart
```

The branch-purity gate rejects it. Official locator/provenance metadata cannot
serve as lawful-local source bytes, output paths, or toolchain identity. A
lawful-local schema cannot serve as official content access, checksum evidence,
or custodian asset custody. Downstream proof pressure supplies no producer
field.

## First Obstruction

The first obstruction is:

```text
no_single_branch_local_packet_instantiates_all_required_fields_for_SingleCompletePTUJBranchReceipt_V1
```

The first missing field by branch is:

| branch | first missing field | first missing object |
|---|---|---|
| official/custodian | `custodian_source_asset_record` | `OfficialTzSEvmqxu48FormulaSourceAssetPacket_V1.source_asset_object_manifest` |
| lawful local | `lawful_basis_for_a_concrete_source_byte_object` | `LawfulLocalTzSEvmqxu48FrameExtractor_V1.toolchain_identity_and_output_manifest` |

The first rule obstruction for any proposed composite is:

```text
all_accepted_fields_belong_to_the_accepted_branch == false
```

When that predicate is false, `SingleCompletePTUJBranchReceipt_V1` must be
rejected even if the composite contains a plausible locator, schema, and
downstream motivation.

## Constructive Next Object

The constructive next object is:

```text
one_complete_branch_pure_PTUJ_source_packet_for_SingleCompletePTUJBranchReceipt_V1
```

It may instantiate exactly one of:

```text
OfficialTzSEvmqxu48FormulaSourceAssetPacket_V1.source_asset_object_manifest
LawfulLocalTzSEvmqxu48FrameExtractor_V1.toolchain_identity_and_output_manifest
```

Minimum official/custodian object:

```text
custodian_source_asset_record
asset_kind
immutable_locator_or_path
content_access
checksum_or_custody_record
formula_visibility_scope
target_import_guard
```

Minimum lawful-local object:

```text
lawful_basis
source_byte_object
source_byte_checksum
acquisition_tool_identity
decoder_tool_identity
decode_scope
output_manifest
output_checksums
target_import_guard
```

Acceptance requires the object to close one branch completely. A packet that
borrows even one producer field from the other branch is not an admitted
receipt.

## PTUJ Proof Meaning

This gate says what a PTUJ producer receipt would mean. It would mean:

```text
exactly one PTUJ source branch is branch-pure and complete enough to inspect
```

It would not mean:

```text
PTUJ formula visible
Keating/Shiab identity established
IG selector route derived
proof restart allowed
GU physics claim promoted
```

Formula visibility is a downstream audit over an already accepted branch
packet. It cannot be used to backfill producer fields. Proof restart remains
blocked until there is an accepted branch receipt, a separate formula visibility
audit, and any later identity/comparison gate required by the route.

## Next Computation

The next computation should be a branch-purity audit over a proposed packet,
not OCR, formula comparison, or proof restart. The audit should parse a packet
with two branch rows and assert:

```text
accepted_branch_count == 1
accepted_receipt_count == 1
exactly_one(official_branch_complete, lawful_local_branch_complete)
all_required_fields_for_accepted_branch_present == true
all_accepted_fields_belong_to_the_accepted_branch == true
official_fields_used_in_lawful_local_branch == false
lawful_local_fields_used_in_official_branch == false
target_import_used == false
cross_branch_assembly_allowed == false
metadata_as_receipt_allowed == false
formula_visibility_used_to_backfill_producer_fields == false
```

If no proposed packet exists, the next work item is source production: choose
one branch and produce the missing source asset or lawful-local byte/toolchain
output manifest to completion.

## Claim-Status Result

No claim status change is made.

This artifact defines an admission invariant and applies it to the current repo
state. It preserves the blocked PTUJ producer state and does not promote,
demote, or re-scope a canon, active-research, roadmap, paper, or specification
claim. Therefore the claim-status consistency workflow is not triggered.

Current downstream state:

```text
PTUJ source packet gate: blocked
PTUJ formula visibility: blocked
Keating comparison: blocked
IG selector route from PTUJ: blocked
proof restart: blocked
global no-go promoted: false
```

## JSON Summary

```json
{
  "artifact": "PTUJBranchPurityAuditGate_2302_C2_LPTUJ_V1",
  "artifact_id": "PTUJBranchPurityAuditGate_2302_C2_LPTUJ_V1",
  "run_id": "hourly-20260625-2302",
  "cycle": 2,
  "lane": "PTUJ",
  "artifact_path": "explorations/hourly-20260625-2302-cycle2-ptuj-branch-purity-audit-gate.md",
  "decision_target": "SingleCompletePTUJBranchReceipt_V1",
  "verdict": "blocked",
  "verdict_class": "blocked_branch_purity_gate",
  "target_import_used": false,
  "claim_status_consistency_triggered": false,
  "cycle1_producer_contract_consumed": true,
  "branch_purity_invariant_defined": true,
  "branch_purity_invariant_satisfied": false,
  "current_repo_can_satisfy_branch_purity_invariant": false,
  "branch_candidate_count": 2,
  "accepted_branch_count": 0,
  "accepted_receipt_count": 0,
  "official_branch_complete": false,
  "lawful_local_branch_complete": false,
  "official_branch_accepted": false,
  "lawful_local_branch_accepted": false,
  "mixed_branch_packet_rejected": true,
  "cross_branch_assembly_allowed": false,
  "formula_visibility_allowed": false,
  "proof_restart_allowed": false,
  "metadata_as_receipt_allowed": false,
  "formula_visibility_used_to_backfill_producer_fields": false,
  "downstream_proof_need_used_as_receipt_field": false,
  "branch_purity_invariant": {
    "accepted_branch_count_required": 1,
    "accepted_receipt_count_required": 1,
    "exactly_one_branch_complete_required": true,
    "all_required_fields_for_accepted_branch_present_required": true,
    "all_accepted_fields_belong_to_the_accepted_branch_required": true,
    "official_fields_used_in_lawful_local_branch_allowed": false,
    "lawful_local_fields_used_in_official_branch_allowed": false,
    "target_import_used_allowed": false,
    "cross_branch_assembly_allowed": false,
    "metadata_as_receipt_allowed": false,
    "formula_visibility_backfill_allowed": false
  },
  "branch_rows": [
    {
      "row_id": "official_custodian_formula_source_asset",
      "branch_object": "OfficialTzSEvmqxu48FormulaSourceAssetPacket_V1.source_asset_object_manifest",
      "complete": false,
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
      "first_missing_field": "custodian_source_asset_record"
    },
    {
      "row_id": "lawful_local_byte_toolchain_output_manifest",
      "branch_object": "LawfulLocalTzSEvmqxu48FrameExtractor_V1.toolchain_identity_and_output_manifest",
      "complete": false,
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
      "first_missing_field": "lawful_basis_for_a_concrete_source_byte_object",
      "first_missing_object": "source_byte_object",
      "first_missing_manifest": "output_manifest"
    }
  ],
  "first_missing_field": "official:custodian_source_asset_record;lawful_local:lawful_basis_for_a_concrete_source_byte_object",
  "first_obstruction": "no_single_branch_local_packet_instantiates_all_required_fields_for_SingleCompletePTUJBranchReceipt_V1",
  "rule_obstruction": "all_accepted_fields_belong_to_the_accepted_branch_false_for_mixed_packets",
  "constructive_next_object": "one_complete_branch_pure_PTUJ_source_packet_for_SingleCompletePTUJBranchReceipt_V1",
  "constructive_next_branch_objects": [
    "OfficialTzSEvmqxu48FormulaSourceAssetPacket_V1.source_asset_object_manifest",
    "LawfulLocalTzSEvmqxu48FrameExtractor_V1.toolchain_identity_and_output_manifest"
  ],
  "non_artifact_candidate_files_found": 0,
  "next_computation": "run_branch_purity_audit_on_a_proposed_single_branch_packet_or_produce_one_complete_branch_local_packet_first"
}
```
