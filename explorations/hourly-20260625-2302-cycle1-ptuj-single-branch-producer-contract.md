---
title: "Hourly 20260625 2302 Cycle 1 PTUJ Single Branch Producer Contract"
date: "2026-06-25"
run_id: "hourly-20260625-2302"
cycle: 1
lane: "PTUJ"
doc_type: "frontier_gate"
artifact_id: "PTUJSingleBranchProducerContract_2302_C1_LPTUJ_V1"
verdict: "blocked"
owned_path: "explorations/hourly-20260625-2302-cycle1-ptuj-single-branch-producer-contract.md"
---

# Hourly 20260625 2302 Cycle 1 PTUJ Single Branch Producer Contract

## 1. Verdict

Verdict: **blocked**.

The current repo cannot admit a complete `SingleCompletePTUJBranchReceipt_V1`
under either allowed PTUJ producer branch:

1. the official/custodian formula-source asset branch; or
2. the lawful-local source-byte/toolchain/output branch.

The contract is now sharp enough to apply:

```text
SingleCompletePTUJBranchReceipt_V1 is admissible iff exactly one allowed
producer branch supplies every required field inside that same branch, with
target_import_used == false and cross_branch_assembly_allowed == false.
```

No such branch-local packet exists in the current tree. The repo has branch
schemas, provenance orientation, and prior negative gates, but not an admitted
custodian source asset record, not a lawful local source-byte object, not an
admitted toolchain, and not an output manifest with checksums.

Decision state:

```text
accepted_branch_count: 0
accepted_receipt_count: 0
official_branch_checked: true
lawful_local_branch_checked: true
official_custodian_asset_record_admitted: false
lawful_source_byte_object_admitted: false
lawful_toolchain_admitted: false
output_manifest_admitted: false
cross_branch_assembly_allowed: false
formula_visibility_allowed: false
proof_restart_allowed: false
target_import_used: false
```

This is not a formula-visible result, not a Keating/Shiab identity result, and
not a proof restart. It is a producer-contract admission gate.

## 2. What was derived directly from repo sources

From `RESEARCH-POSTURE.md`:

- Compatibility, metadata, and target expectation cannot be promoted into a
  derivation or receipt.
- Failed producer attempts should name the constructive object that would
  remove the obstruction.
- Target data cannot be hidden inside a reconstruction.

From `process/runbooks/five-lane-frontier-run.md`:

- This lane must make a decision-grade verdict and name the first exact missing
  proof or source object.
- `blocked` is the right verdict when the object is specified enough to test but
  absent from the repo.

From the required PTUJ predecessor artifacts:

| source | direct use |
|---|---|
| `explorations/hourly-20260625-2104-cycle1-ptuj-single-complete-branch-receipt-attempt.md` | Defined the target as `SingleCompletePTUJBranchReceipt_V1`, with zero accepted receipts and no formula visibility. |
| `explorations/hourly-20260625-2104-cycle2-ptuj-branch-local-source-packet-gate.md` | Fixed the two allowed branch objects and the required field ledgers for each branch. |
| `explorations/hourly-20260625-2202-cycle1-ptuj-branch-source-byte-preflight.md` | Confirmed the lawful-local first missing field as `lawful_basis_for_a_concrete_source_byte_object` and no source bytes/output manifest. |
| `explorations/hourly-20260625-2202-cycle2-ptuj-branch-exclusivity-gate.md` | Confirmed official and lawful-local fields cannot be assembled together. |
| `explorations/hourly-20260625-2202-cycle3-ptuj-proof-restart-classifier.md` | Confirmed proof restart remains blocked before a complete branch-local packet. |

Additional current-tree checks performed in this lane:

| check | result | consequence |
|---|---|---|
| `rg` for `SingleCompletePTUJBranchReceipt_V1`, `OfficialTzSEvmqxu48`, `LawfulLocalTzSEvmqxu48`, `TzSEvmqxu48`, `source_byte_object`, and `output_manifest` | Found historical markdown/audit objects and blockers, not a newly admitted packet. | No predecessor can be promoted into the current receipt. |
| File-name scan for `TzSEvmqxu48`, `PTUJ`, `pull...jamie`, `source_byte`, `output_manifest`, and `checksum` | Found only prior PTUJ exploration and audit files. | No source-byte, frame, manifest, or checksum artifact appears as a repo-local asset. |
| Same file-name scan excluding `explorations/` and `tests/` | Returned no candidate files. | There is no non-artifact producer asset to admit. |
| `sources/media-index.md` read | `GU-MEDIA-2021-PULL-THAT-UP-JAMIE` is `metadata-checked` and explicitly a pointer to visuals, not a formal source receipt. | Official orientation exists, but source asset admission does not. |
| Accepted-count/proof-restart search excluding the required PTUJ predecessor files | Positive receipt/proof-restart strings belonged to non-PTUJ routes or historical hypothetical rollback conditions. | No actual PTUJ accepted receipt is present. |

## 3. Strongest positive construction attempt

The strongest positive construction is a producer contract with two mutually
exclusive admissible branches. The contract can be stated, but no instance can
be accepted.

### Official/custodian branch attempt

Candidate object:

```text
OfficialTzSEvmqxu48FormulaSourceAssetPacket_V1.source_asset_object_manifest
```

Positive material currently available:

```text
target_video_id: TzSEvmqxu48
source_surface: GU-MEDIA-2021-PULL-THAT-UP-JAMIE
surface_status: metadata-checked
target_import_guard: present as a rule
```

Required official branch fields:

| required field | current admission state |
|---|---|
| `custodian_source_asset_record` | missing |
| `asset_kind` | missing |
| `immutable_locator_or_path` | metadata-only at best; not an admitted source asset object |
| `content_access` | missing |
| `checksum_or_custody_record` | missing |
| `formula_visibility_scope` | missing |
| `target_import_guard` | present as a rule, but not sufficient |

Official branch result:

```text
accepted: false
first_missing_field: custodian_source_asset_record
first_missing_object: OfficialTzSEvmqxu48FormulaSourceAssetPacket_V1.source_asset_object_manifest
```

The official/custodian route remains live as a possible future route, but the
current repo supplies only orientation metadata. Orientation metadata does not
identify an inspectable, formula-bearing source object with custody, content
access, checksum or custody record, and visibility scope.

### Lawful-local source-byte/toolchain/output branch attempt

Candidate object:

```text
LawfulLocalTzSEvmqxu48FrameExtractor_V1.toolchain_identity_and_output_manifest
```

Positive material currently available:

```text
branch_schema: present in prior PTUJ gates
target_import_guard: present as a rule
```

Required lawful-local branch fields:

| required field | current admission state |
|---|---|
| `lawful_basis` | missing for any concrete byte object |
| `source_byte_object` | missing |
| `source_byte_checksum` | missing |
| `acquisition_tool_identity` | missing |
| `decoder_tool_identity` | missing |
| `decode_scope` | missing |
| `output_manifest` | missing |
| `output_checksums` | missing |
| `target_import_guard` | present as a rule, but not sufficient |

Lawful-local branch result:

```text
accepted: false
first_missing_field: lawful_basis_for_a_concrete_source_byte_object
first_missing_object: source_byte_object
first_missing_manifest: output_manifest
```

The lawful-local route also remains live as a possible future route, but the
current repo contains no lawful source bytes or source package for
`TzSEvmqxu48`, no checksum for such bytes, no admitted acquisition or decoder
tool identity, no decode scope, and no generated output manifest.

### Rejected mixed construction

The strongest tempting mixed construction is:

```text
official target/provenance locator
+ lawful-local branch schema
+ downstream formula/proof need
```

That construction is rejected. It is not one branch-local producer packet. The
official branch cannot borrow the lawful-local schema as source content, and
the lawful-local branch cannot borrow official metadata as source bytes,
toolchain identity, output paths, or checksums.

## 4. First exact obstruction or missing proof object

Common obstruction:

```text
no_single_branch_local_packet_instantiates_all_required_fields_for_SingleCompletePTUJBranchReceipt_V1
```

First missing field by branch:

| branch | first missing field | first missing object |
|---|---|---|
| official/custodian | `custodian_source_asset_record` | `OfficialTzSEvmqxu48FormulaSourceAssetPacket_V1.source_asset_object_manifest` |
| lawful local | `lawful_basis_for_a_concrete_source_byte_object` | `LawfulLocalTzSEvmqxu48FrameExtractor_V1.toolchain_identity_and_output_manifest` |

This gate blocks at the producer layer. It does not reach a mathematical proof
object for the formula because the source object carrying the candidate formula
has not yet been admitted.

## 5. Constructive next object

Produce exactly one complete branch-local packet:

```text
one_complete_branch_local_PTUJ_source_packet_for_SingleCompletePTUJBranchReceipt_V1
```

The next object may take either branch, but must not combine branches.

Official/custodian route:

```text
OfficialTzSEvmqxu48FormulaSourceAssetPacket_V1.source_asset_object_manifest
```

Required minimum contents:

```text
custodian_source_asset_record
asset_kind
immutable_locator_or_path
content_access
checksum_or_custody_record
formula_visibility_scope
target_import_guard
```

Lawful-local route:

```text
LawfulLocalTzSEvmqxu48FrameExtractor_V1.toolchain_identity_and_output_manifest
```

Required minimum contents:

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

Admission invariant for either route:

```text
accepted_branch_count == 1
accepted_receipt_count == 1
all_accepted_fields_belong_to_the_same_branch == true
target_import_used == false
cross_branch_assembly_allowed == false
metadata_as_receipt_allowed == false
formula_visibility_used_to_backfill_producer_fields == false
```

## 6. What this means for formula visibility/proof restart

PTUJ formula visibility is still not allowed. The repo must first admit one
complete branch-local producer receipt. Only then can a separate
`PTUJFormulaVisibilityAudit_V1` inspect the admitted source asset or decoded
outputs under the recorded scope and checksums.

Proof restart is also not allowed. A proof restart would require at least:

```text
accepted SingleCompletePTUJBranchReceipt_V1
+ successful formula visibility audit
+ downstream identity/comparison gate
+ target-import screen
+ named restart object
```

None of those downstream objects can be inferred from the current producer
contract. A blocked producer contract preserves the existing block; it does not
promote a PTUJ no-go and does not demote GU globally.

## 7. Next meaningful proof or computation step

The next meaningful step is source production, not formula comparison:

```text
choose_one_branch_and_build_the_packet_to_completion
```

For the official/custodian route, obtain or record a custodian source asset
manifest with content access, asset kind, stable locator/path, custody or
checksum evidence, and formula visibility scope.

For the lawful-local route, create a lawful local packet with an explicit basis
for using a concrete `TzSEvmqxu48` source-byte object, source checksum,
acquisition and decoder identities, decode scope, output manifest, and output
checksums.

A useful computation after that object exists would be a small audit that
asserts the receipt fields all belong to one branch and that
`accepted_receipt_count == 1`. Running OCR, Keating comparison, or proof restart
before that object exists repeats the same block.

## 8. Claim-status consistency result

No claim status change is made.

This artifact preserves the blocked PTUJ producer state and sharpens the
contract for future admission. It does not promote, demote, or re-scope any
canon, active-research, roadmap, paper, or specification claim. Therefore the
claim-status consistency workflow is not triggered by this lane.

Consistency result:

```text
claim_status_consistency_triggered: false
PTUJ_source_packet_gate: blocked
PTUJ_formula_visibility: blocked
Keating_comparison: blocked
IG_selector_route_from_PTUJ: blocked
proof_restart: blocked
global_no_go_promoted: false
```

## 9. Machine-readable JSON summary

```json
{
  "artifact": "PTUJSingleBranchProducerContract_2302_C1_LPTUJ_V1",
  "artifact_id": "PTUJSingleBranchProducerContract_2302_C1_LPTUJ_V1",
  "run_id": "hourly-20260625-2302",
  "cycle": 1,
  "lane": "PTUJ",
  "artifact_path": "explorations/hourly-20260625-2302-cycle1-ptuj-single-branch-producer-contract.md",
  "verdict_class": "blocked_producer_contract",
  "decision_target": "SingleCompletePTUJBranchReceipt_V1",
  "target_import_used": false,
  "claim_status_consistency_triggered": false,
  "official_branch_checked": true,
  "lawful_local_branch_checked": true,
  "official_branch_admitted": false,
  "lawful_local_branch_admitted": false,
  "official_custodian_asset_record_admitted": false,
  "lawful_source_byte_object_admitted": false,
  "lawful_toolchain_admitted": false,
  "output_manifest_admitted": false,
  "accepted_branch_count": 0,
  "accepted_receipt_count": 0,
  "cross_branch_assembly_allowed": false,
  "formula_visibility_allowed": false,
  "proof_restart_allowed": false,
  "metadata_as_receipt_allowed": false,
  "formula_visibility_used_to_backfill_producer_fields": false,
  "first_missing_field": "official:custodian_source_asset_record;lawful_local:lawful_basis_for_a_concrete_source_byte_object",
  "first_missing_field_by_branch": {
    "official_custodian": "custodian_source_asset_record",
    "lawful_local": "lawful_basis_for_a_concrete_source_byte_object"
  },
  "first_obstruction": "no_single_branch_local_packet_instantiates_all_required_fields_for_SingleCompletePTUJBranchReceipt_V1",
  "constructive_next_object": "one_complete_branch_local_PTUJ_source_packet_for_SingleCompletePTUJBranchReceipt_V1",
  "constructive_next_branch_objects": [
    "OfficialTzSEvmqxu48FormulaSourceAssetPacket_V1.source_asset_object_manifest",
    "LawfulLocalTzSEvmqxu48FrameExtractor_V1.toolchain_identity_and_output_manifest"
  ],
  "official_required_missing_fields": [
    "custodian_source_asset_record",
    "asset_kind",
    "immutable_locator_or_path",
    "content_access",
    "checksum_or_custody_record",
    "formula_visibility_scope"
  ],
  "lawful_local_required_missing_fields": [
    "lawful_basis",
    "source_byte_object",
    "source_byte_checksum",
    "acquisition_tool_identity",
    "decoder_tool_identity",
    "decode_scope",
    "output_manifest",
    "output_checksums"
  ],
  "current_tree_non_artifact_candidate_files": 0,
  "next_meaningful_step": "choose_one_branch_and_produce_a_complete_branch_local_packet_before_formula_visibility_or_proof_restart"
}
```
