---
title: "Hourly 20260625 2104 Cycle 2 PTUJ Branch Local Source Packet Gate"
date: "2026-06-25"
run_id: "hourly-20260625-2104"
cycle: 2
lane: "1 PTUJ"
doc_type: ptuj_branch_local_source_packet_gate
artifact_id: "PTUJBranchLocalSourcePacketGate_2104_C2_L1_V1"
verdict: "blocked"
owned_path: "explorations/hourly-20260625-2104-cycle2-ptuj-branch-local-source-packet-gate.md"
---

# Hourly 20260625 2104 Cycle 2 PTUJ Branch Local Source Packet Gate

## 1. Verdict.

Verdict: **blocked**.

This lane attempted the next PTUJ source packet gate for:

```text
SingleCompletePTUJBranchReceipt_V1
```

No branch-local source packet can be constructed from the current repo state.
The official/custodian branch still has only target/provenance orientation and
no admitted formula-bearing source asset packet. The lawful local branch still
has a receipt schema and target-import guard, but no admitted source-byte
object, toolchain identity, decode scope, output manifest, or checksums.

Decision state:

```text
accepted_receipt_count: 0
official_branch_accepted: false
lawful_local_branch_accepted: false
cross_branch_assembly_allowed: false
metadata_as_receipt_allowed: false
formula_expectation_as_receipt_allowed: false
thumbnail_caption_oembed_as_receipt_allowed: false
ig_product_b_as_receipt_allowed: false
target_import_used: false
```

This is a scoped negative packet, not a PTUJ formula-negative result. It blocks
only the producer/source-packet gate before formula visibility, Keating
comparison, or proof restart.

## 2. Specific claim/bridge under test.

The bridge under test is:

```text
one complete branch-local PTUJ source packet
  -> SingleCompletePTUJBranchReceipt_V1
  -> later PTUJFormulaVisibilityAudit_V1
```

The gate admits exactly one of two branch-local packet forms:

1. `OfficialTzSEvmqxu48FormulaSourceAssetPacket_V1.source_asset_object_manifest`
2. `LawfulLocalTzSEvmqxu48FrameExtractor_V1.toolchain_identity_and_output_manifest`

The claim under test is not that the formula is visible, correct, Keating-like,
or useful for an IG route. The only tested claim is whether one complete PTUJ
branch-local source packet exists without target import and without assembling
fields across branches.

## 3. Sources read first.

| source | use in this decision |
|---|---|
| `RESEARCH-POSTURE.md` | Preserved the constructive Mission A posture while rejecting metadata, compatibility, and target data as evidence. |
| `process/runbooks/five-lane-frontier-run.md` | Supplied verdict vocabulary and the requirement to name the first exact obstruction. |
| `process/runbooks/three-cycle-fifteen-hole-run.md` | Required a quality hole with rollback condition, next object, and claim-status consistency result. |
| `explorations/hourly-20260625-2104-cycle1-ptuj-single-complete-branch-receipt-attempt.md` | Confirmed the immediately prior PTUJ attempt ended with zero accepted receipts and two incomplete branches. |
| `explorations/hourly-20260625-2104-cycle1-ig-product-b-d7-table-receipt-attempt.md` | Read only as a firewall: its Product B receipt is not a PTUJ source field and is not imported here. |
| `tests/hourly_20260625_2104_cycle1_receipt_attempts_audit.py` | Confirmed the cycle 1 audit treats PTUJ as blocked with `accepted_receipt_count == 0` and no cross-branch assembly. |
| `explorations/hourly-20260625-1802-cycle2-ptuj-single-branch-nonconflation-gate.md` | Supplied the nonconflation rule: a receipt must be complete inside one branch. |

Additional focused checks after the required first reads:

| check | result |
|---|---|
| `rg` for `SingleCompletePTUJBranchReceipt`, `OfficialTzSEvmqxu48`, `LawfulLocalTzSEvmqxu48`, `source_byte_object`, and `output_manifest` | Found prior markdown/audit blockers, not a branch-local source packet. |
| `rg` over PTUJ markdown for accepted count one | Found only the rollback/falsification condition in the cycle 1 packet, not an actual accepted PTUJ receipt. |
| `rg` over PTUJ audits for source-byte and official-source fields | Existing audits assert zero accepted receipts and absent local byte/output manifests. |
| `sources/media-index.md` lookup | `GU-MEDIA-2021-PULL-THAT-UP-JAMIE` is `metadata-checked` and marked as a pointer to visuals, not a formal source receipt. |
| file search for `*TzSEvmqxu48*` | Found only historical markdown/audit files, not source bytes, frame outputs, or manifests. |

## 4. Strongest positive construction attempt.

The strongest admissible attempt is to test both branches independently and
reject any field not local to that branch.

### Official/custodian asset branch

Positive material currently available:

```text
target_video_id: TzSEvmqxu48
media_index_surface: GU-MEDIA-2021-PULL-THAT-UP-JAMIE
branch_kind: official/custodian formula-bearing source asset
target_import_guard: present as a rule
```

This identifies the PTUJ target surface and keeps the official branch live, but
it does not construct a formula-bearing source asset packet. The media-index row
is explicitly metadata/provenance orientation. It does not provide content
access, an asset kind, a checksum, a custody record, or a formula visibility
scope.

Official branch field ledger:

| required branch-local field | status | reason not accepted |
|---|---|---|
| `custodian_source_asset_record` | absent | No admitted custodian source object or asset record is present. |
| `asset_kind` | absent | No branch-local source video package, frame sequence, sheet, page, or equivalent source asset is typed. |
| `immutable_locator_or_path` | absent as a receipt field | Public/provenance locators remain metadata; no immutable source object path is admitted. |
| `content_access` | absent | No inspectable source asset content is admitted under this branch. |
| `checksum_or_custody_record` | absent | No checksum, size, custody chain, or stable source-object verification exists. |
| `formula_visibility_scope` | absent | No frame, timecode, sheet/page id, or source-scope audit range is admitted. |
| `target_import_guard` | present | Necessary guard, but not a source asset field. |

Official branch result:

```text
accepted: false
first_missing_field: custodian_source_asset_record
first_obstruction: no_official_or_custodian_formula_source_asset_manifest
```

### Lawful local byte/toolchain branch

Positive material currently available:

```text
branch_schema: LawfulLocalTzSEvmqxu48FrameExtractor_V1.toolchain_identity_and_output_manifest
target_import_guard: present as a rule
```

This branch is well specified as a required future packet, but the current repo
does not contain the source byte object or generated output manifest needed to
instantiate it.

Lawful local field ledger:

| required branch-local field | status | reason not accepted |
|---|---|---|
| `lawful_basis` | absent for a concrete byte object | No concrete repo-local source object is attached to a lawful acquisition basis. |
| `source_byte_object` | absent | No local `TzSEvmqxu48` source bytes or source package are admitted. |
| `source_byte_checksum` | absent | No source byte object exists to checksum. |
| `acquisition_tool_identity` | absent | No admitted acquisition command, executable, version, or provenance is present. |
| `decoder_tool_identity` | absent | No admitted decoder/extractor identity is present. |
| `decode_scope` | absent | No frame/time/window/full-asset decode scope is admitted. |
| `output_manifest` | absent | No generated frame/source output paths, sizes, dimensions, commands, or timecodes are admitted. |
| `output_checksums` | absent | No outputs exist to checksum. |
| `target_import_guard` | present | Necessary guard, but not a local source/tool/output field. |

Lawful local branch result:

```text
accepted: false
first_missing_field: lawful_basis_for_a_concrete_source_byte_object
first_missing_object: source_byte_object
first_missing_manifest: output_manifest
first_obstruction: no_lawful_local_byte_toolchain_output_manifest
```

### Explicitly rejected pseudo-constructions

The following do not produce receipt fields:

```text
IG Product B D7 table result
formula expectations
Keating/Shiab target expectations
thumbnails
captions
oEmbed/watch-page metadata
cross-branch assembly of official metadata plus local schema
```

The strongest positive result is therefore not a packet admission. It is a
branch-local exclusion: each branch has a precise first missing object, and no
permitted construction can move a field from one branch to the other.

## 5. First exact obstruction/missing object.

The first exact obstruction is:

```text
no_branch_local_source_packet_instantiates_all_required_fields_for_either_allowed_PTUJ_branch
```

The first official/custodian missing object is:

```text
OfficialTzSEvmqxu48FormulaSourceAssetPacket_V1.source_asset_object_manifest
```

with missing fields:

```text
custodian_source_asset_record
asset_kind
immutable_locator_or_path
content_access
checksum_or_custody_record
formula_visibility_scope
```

The first lawful local missing object is:

```text
LawfulLocalTzSEvmqxu48FrameExtractor_V1.toolchain_identity_and_output_manifest
```

with missing fields:

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

The earliest concrete missing field by branch-local packet order is:

```text
official branch: custodian_source_asset_record
lawful local branch: lawful_basis_for_a_concrete_source_byte_object
```

## 6. What would change if closed.

If exactly one branch-local source packet closed, the PTUJ route would move to:

```text
accepted_receipt_count: 1
accepted_branch_count: 1
SingleCompletePTUJBranchReceipt_V1: admitted
PTUJFormulaVisibilityAudit_V1: allowed as the next sequential gate
```

Closure would not prove a formula, prove a Keating identity, select an IG
family route, or authorize proof restart. It would only allow the next audit to
inspect the admitted source content or decoded outputs under the branch-local
scope and checksums.

## 7. Rollback/falsification condition.

Rollback this blocked verdict if a single branch-local packet is produced with
all required fields for one branch and the following invariants hold:

```text
accepted_receipt_count == 1
accepted_branch_count == 1
exactly_one_branch_accepted == true
all_accepted_fields_belong_to_the_same_branch == true
target_import_used == false
cross_branch_assembly_allowed == false
metadata_as_receipt_allowed == false
formula_expectation_as_receipt_allowed == false
```

Reject the packet even if it appears useful downstream if any of these occur:

```text
official metadata is used as local source bytes
local schema is used as official content access
thumbnails, captions, watch pages, or oEmbed data are promoted into source assets
IG Product B data is used as a PTUJ receipt field
formula or Keating expectations select or normalize the source object
downstream formula visibility backfills producer/source-packet fields
```

## 8. Next meaningful source/proof step.

The next step is source-object production, not formula comparison:

```text
produce_one_branch_local_PTUJ_source_packet_for_SingleCompletePTUJBranchReceipt_V1
```

Two valid routes remain:

1. Produce `OfficialTzSEvmqxu48FormulaSourceAssetPacket_V1.source_asset_object_manifest`
   with a custodian source asset record, asset kind, stable locator/path,
   content access, checksum or custody record, and formula visibility scope.
2. Produce `LawfulLocalTzSEvmqxu48FrameExtractor_V1.toolchain_identity_and_output_manifest`
   with lawful basis, source byte object, source checksum, acquisition and
   decoder identities, decode scope, output manifest, and output checksums.

The route should pick one producer branch and complete it end-to-end. Running a
visibility audit before this object exists would repeat the current block.

## 9. Claim-status consistency result.

No claim status change is made.

This artifact does not promote, demote, or re-scope a canon, active-research,
roadmap, or paper claim. It preserves the already-blocked PTUJ producer gate and
sharpens the missing branch-local fields. Therefore the claim-status
consistency workflow is **not triggered** by this lane.

Current downstream state:

```text
PTUJ source packet gate: blocked
PTUJ formula visibility: blocked
Keating comparison: blocked
IG selector route from PTUJ: blocked
proof restart: blocked
claim promotion allowed: false
global no-go promoted: false
```

## 10. Machine-readable JSON summary.

```json
{
  "artifact": "PTUJBranchLocalSourcePacketGate_2104_C2_L1_V1",
  "artifact_id": "PTUJBranchLocalSourcePacketGate_2104_C2_L1_V1",
  "run_id": "hourly-20260625-2104",
  "cycle": 2,
  "lane": "1 PTUJ",
  "route": "PTUJ",
  "artifact_path": "explorations/hourly-20260625-2104-cycle2-ptuj-branch-local-source-packet-gate.md",
  "decision_target": "SingleCompletePTUJBranchReceipt_V1",
  "verdict_class": "blocked",
  "accepted_receipt_count": 0,
  "accepted_branch_count": 0,
  "target_import_used": false,
  "claim_status_consistency_triggered": false,
  "official_branch_accepted": false,
  "lawful_local_branch_accepted": false,
  "cross_branch_assembly_allowed": false,
  "metadata_as_receipt_allowed": false,
  "formula_expectation_as_receipt_allowed": false,
  "thumbnail_caption_oembed_as_receipt_allowed": false,
  "ig_product_b_result_used_as_receipt_field": false,
  "branch_packets": [
    {
      "row_id": "official_custodian_formula_source_asset",
      "branch_object": "OfficialTzSEvmqxu48FormulaSourceAssetPacket_V1.source_asset_object_manifest",
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
      "first_missing_field": "custodian_source_asset_record",
      "first_obstruction": "no_official_or_custodian_formula_source_asset_manifest"
    },
    {
      "row_id": "lawful_local_byte_toolchain_output_manifest",
      "branch_object": "LawfulLocalTzSEvmqxu48FrameExtractor_V1.toolchain_identity_and_output_manifest",
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
      "first_missing_manifest": "output_manifest",
      "first_obstruction": "no_lawful_local_byte_toolchain_output_manifest"
    }
  ],
  "first_obstruction": "no_branch_local_source_packet_instantiates_all_required_fields_for_either_allowed_PTUJ_branch",
  "constructive_next_object": "one_complete_branch_local_PTUJ_source_packet_for_SingleCompletePTUJBranchReceipt_V1",
  "constructive_next_branch_objects": [
    "OfficialTzSEvmqxu48FormulaSourceAssetPacket_V1.source_asset_object_manifest",
    "LawfulLocalTzSEvmqxu48FrameExtractor_V1.toolchain_identity_and_output_manifest"
  ],
  "rollback_condition": "one_and_only_one_branch_local_packet_supplies_all_required_fields_with_target_import_unused_and_no_metadata_formula_expectation_ig_product_b_or_cross_branch_promotion",
  "next_meaningful_step": "produce_one_complete_official_custodian_or_lawful_local_PTUJ_source_packet_then_run_separate_formula_visibility_audit"
}
```
