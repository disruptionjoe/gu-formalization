---
title: "Hourly 20260626 1003 Cycle 2 DGU Branch-Pure Source Asset Producer"
date: "2026-06-26"
run_id: "hourly-20260626-1003"
cycle: 2
lane: 1
doc_type: "frontier_run_lane_artifact"
artifact_id: "OfficialOrLawfulUCSDDGU01FrameSourceAssetProducer_1003_C2_L1_V1"
verdict: "closed_scoped_negative_branch_pure_producer_specified_and_executed"
owned_path: "explorations/hourly-20260626-1003-cycle2-dgu-branch-pure-source-asset-producer.md"
claim_status_change: false
---

# Hourly 20260626 1003 Cycle 2 DGU Branch-Pure Source Asset Producer

## 1. Verdict

Verdict: **closed / scoped negative producer execution**.

The branch-pure producer predicate can be specified and executed repo-locally:

```text
OfficialOrLawfulUCSDDGU01FrameSourceAssetProducer_V1
  -> ACCEPT OfficialOrLawfulUCSDDGU01FrameSourceAsset_V1
  -> EMIT NegativeOfficialOrLawfulUCSDDGU01FrameSourceAssetReceipt_V1
```

Current execution emits the negative receipt:

```text
producer_predicate_specified: true
producer_executed_repo_locally: true
accept_asset_emitted: false
negative_receipt_emitted: true
branch_purity_enforced: true
frame_retry_allowed: false
same_operator_retry_allowed: false
target_import_used: false
claim_status_change: false
```

This is not a DGU no-go. It is a repo-local source-asset decision. The repo has
UCSD transcript windows and prior negative manifest/precondition records, but
it still lacks a branch-pure source asset identity for the UCSD DGU01 visual
windows.

## 2. What Was Derived Directly From Repo Sources

The producer consumed repo-local source and coordination artifacts only. No
external media was acquired, and no new general asset search was performed.

Direct derivations:

| repo source | direct fact used by the producer |
|---|---|
| `RESEARCH-POSTURE.md` | The run may pursue constructive objects, but must not hide target data inside reconstruction evidence. |
| `process/runbooks/five-lane-frontier-run.md` | A lane must name the exact missing object, terrain, forbidden shortcut, invariant, and kill condition without overclaiming. |
| `explorations/remaining-math-topography-ledger-v0-2026-06-26.md` | DGU same-operator is provenance-verifier plus spectral-phase terrain; the shortcut is calling two formulae the same without source handles. |
| `explorations/hourly-20260626-1003-cycle1-dgu-official-lawful-frame-source-asset-gate.md` | The exact obstruction is `OfficialOrLawfulUCSDDGU01FrameSourceAsset_V1.source_asset_identity_absent`; all three acquisition branches were absent. |
| `explorations/hourly-20260626-0904-cycle3-dgu-ucsd-frame-acquisition-preconditions.md` | Official still, lawful-local video, and alternate-equivalent branches are separated and all remain not ready. |
| `explorations/hourly-20260626-0904-cycle2-dgu-visual-frame-asset-manifest.md` | No UCSD source video, official still rows, extracted frame manifest, frame checksums, or visual transcription rows were present for the visual manifest. |
| `explorations/hourly-20260626-0904-cycle1-dgu-ucsd-visual-frame-rows.md` | Transcript windows are source-positive, but the visual frame asset manifest is missing, so same-operator and proof restart stay locked. |
| `explorations/sequential-goal-1-dgu-source-row-same-operator-2026-06-26.md` | `DGU01SameOperatorWitness_V1` is unevaluable until a primary source row with an actual operator handle exists. |
| `sources/media-index.md` | UCSD/recent lecture surfaces are candidate/backlog provenance pointers, not admitted source assets. |
| `sources/media-mining-coverage-gaps-v1.md` | Modern surfaces need transcript/timestamp/source verification before formal use. |

The narrow current-state execution checked only names explicitly tied to
`UCSD` or `DGU01`. It found no repo-local `UCSD`/`DGU01` media or checksum
file with a frame/video/still extension, and no emitted true acceptance signal
for the official, lawful-local, or alternate-equivalent asset branch. A quoted
`ACCEPT OfficialOrLawfulUCSDDGU01FrameSourceAsset_V1` label in the prior cycle
is not an emitted acceptance.

## 3. Strongest Positive Construction Attempt

The strongest construction is a branch-pure producer with three mutually
exclusive input branches.

### Producer Inputs

Common public inputs:

```text
predicate_id: OfficialOrLawfulUCSDDGU01FrameSourceAssetProducer_V1
target_asset_id: OfficialOrLawfulUCSDDGU01FrameSourceAsset_V1
repo_root
run_id
cycle
allowed_transcript_windows:
  - 00:32:46-00:36:13
  - 00:49:16-00:50:09
allowed_branch_kind:
  - official_ucsd_still
  - lawful_local_ucsd_video
  - alternate_equivalent_source_asset
forbidden_inputs:
  - downstream VZ/RS/K3/exact-GR/theta success
  - target generation count
  - typed D_roll comparison success
  - same-operator success
  - manuscript/Oxford payload without an equivalence proof
```

Branch-specific inputs:

| branch | required producer input |
|---|---|
| `official_ucsd_still` | official UCSD still/frame locator or immutable official ID, source authority label, transcript-window tie, still/frame checksum if local or official immutability basis if remote, visible payload rows or explicit absence rows, anti-target-import declaration |
| `lawful_local_ucsd_video` | repo-local UCSD video/source-byte path, lawful local acquisition basis, source SHA-256, extraction command/tool identity, extracted frame/crop/OCR output paths, output SHA-256 values, frame-window manifest, visible payload rows or explicit absence rows |
| `alternate_equivalent_source_asset` | alternate source identity, custody/lawful basis, source checksum or immutable locator, source-stable equivalence proof to the UCSD DGU01 visual windows, frame/output manifest, visible payload rows or explicit absence rows |

### Verifier Predicate

Let:

```text
Official(b) =
  official_locator_or_id_present
  and official_authority_accepted
  and immutable_locator_or_checksum_present
  and transcript_window_tie_present
  and visible_payload_or_explicit_absence_rows_present

LawfulLocal(b) =
  repo_local_source_bytes_present
  and lawful_basis_present
  and source_sha256_recomputable
  and extraction_manifest_present
  and frame_outputs_checksum_recomputable
  and frame_window_mapping_present
  and visible_payload_or_explicit_absence_rows_present

AlternateEquivalent(b) =
  alternate_source_identity_present
  and alternate_custody_or_lawful_basis_present
  and alternate_checksum_or_immutable_locator_present
  and equivalence_to_ucsd_dgu01_windows_pre_target
  and alternate_frame_output_manifest_present
  and visible_payload_or_explicit_absence_rows_present

NoTargetImport =
  no field is filled from downstream target physics, typed D_roll success,
  same-operator success, generation count, DESI/theta/exact-GR output, or
  Oxford/manuscript adjacency without a source-stable equivalence proof

BranchPure =
  exactly_one(Official, LawfulLocal, AlternateEquivalent) is selected
  and all selected-branch fields are supplied inside that branch
  and all unselected branches are ignored rather than used as field donors

Accept =
  BranchPure and NoTargetImport and
  (Official(selected) or LawfulLocal(selected) or AlternateEquivalent(selected))
```

Retry flags are derived, not hand-set:

```text
frame_retry_allowed := accept_asset_emitted

same_operator_retry_allowed :=
  accept_asset_emitted
  and accepted_frame_or_visual_row_manifest_present
  and source_row_actual_operator_handle_present
```

For the current run, `Accept` evaluates false before payload transcription,
operator-handle, or same-operator tests begin.

### Repo-Local Execution Trace

| branch | first evaluated atom | current value | producer result |
|---|---|---:|---|
| `official_ucsd_still` | official UCSD still/frame identity present | false | reject branch |
| `lawful_local_ucsd_video` | repo-local UCSD video/source-byte identity present | false | reject branch |
| `alternate_equivalent_source_asset` | alternate source asset identity plus pre-target equivalence proof present | false | reject branch |
| common guard | target import used | false | guard passed, but no branch accepts |
| producer output | any branch accepts | false | emit negative receipt |

This is the strongest positive attempt because it converts the prior obstruction
from an informal "asset absent" statement into an executable, branch-pure
accept/reject predicate with explicit retry semantics.

## 4. First Exact Obstruction/Missing Object

The first exact obstruction is:

```text
OfficialOrLawfulUCSDDGU01FrameSourceAssetProducer_V1
  .selected_branch
  .source_asset_identity
is absent for every branch.
```

Equivalently:

```text
source_asset_identity notin
  OfficialUCSDStillIdentity
  union LawfulLocalUCSDVideoOrSourceByteIdentity
  union AlternateEquivalentSourceAssetIdentityWithPreTargetEquivalence
```

Because this atom is false, the producer does not reach checksum
recomputation, frame extraction, OCR, visible payload transcription, sector
rule ID, actual operator handle, or same-operator equality.

## 5. Constructive Next Object

The constructive next object is smaller than another visual-row retry:

```text
BranchPureUCSDDGU01SourceAssetSeed_V1
```

It must contain exactly one of:

| seed branch | minimum seed fields |
|---|---|
| official still seed | official UCSD still/frame locator or immutable official ID, authority label, transcript-window tie |
| lawful-local video seed | local source-byte path, lawful basis, source SHA-256, transcript-window extraction policy |
| alternate-equivalent seed | alternate asset identity, custody/checksum/locator, and a pre-target equivalence proof to the UCSD DGU01 windows |

Once this seed exists, the same producer can be rerun. Without it, retrying
frame transcription or same-operator work only repeats the same first failure.

## 6. Meaning For DGU/Same-Operator/Visual-Row Claims

Allowed statement:

```text
The repo can now state and execute a branch-pure UCSD DGU01 source-asset
producer predicate. Its current repo-local execution emits the negative
source-asset receipt.
```

Not allowed:

```text
The repo contains an official UCSD DGU01 frame/still asset.
The repo contains a lawful-local UCSD DGU01 video/source-byte object.
The repo contains an alternate equivalent UCSD DGU01 source asset.
UCSD DGU01 visual rows may be retried.
DGU01 same-operator equality may be retried.
Any DGU/VZ/RS/K3/exact-GR/theta route may restart from UCSD DGU01.
```

DGU remains source-blocked at this branch. The result does not promote,
demote, or otherwise change any claim status.

## 7. Next Meaningful Proof/Computation Step

Do not run a same-operator worker next. The next meaningful step is to produce
or reject the seed object:

```text
BranchPureUCSDDGU01SourceAssetSeed_V1
  -> rerun OfficialOrLawfulUCSDDGU01FrameSourceAssetProducer_V1
```

If a seed is supplied and the producer accepts, the next computation is:

```text
UCSDDGU01FrameOutputManifest_V1
```

with source checksums, extraction commands, frame/output checksums, frame-window
mapping, and visible payload rows or explicit absence rows. Only after that can
a DGU01 sector-row or same-operator witness be evaluated.

## 8. Terrain Classification, Forbidden Shortcut, Invariant, Kill Condition

Terrain:

```text
primary: provenance-verifier
secondary: source-identity intake
blocked downstream: spectral-phase, microlocal-subprincipal,
  noncompact-aps-end, smooth-variational exact-GR/theta recovery
```

Forbidden shortcut:

```text
Do not treat transcript timestamps, source-index metadata, Oxford/manuscript
adjacency, typed D_roll compatibility, or downstream target success as a UCSD
DGU01 source asset identity.
```

Invariant:

```text
Every accepted asset must select exactly one branch and carry all identity,
custody/lawful-basis, checksum-or-immutable-locator, frame-window, payload, and
anti-smuggling fields inside that branch before any visual-row or same-operator
retry flag is true.
```

Kill condition:

```text
If the declared repo-local scope lacks an official still/frame identity, a
lawful-local video/source-byte identity, and an alternate equivalent source
asset identity with pre-target equivalence proof, the producer must emit
NegativeOfficialOrLawfulUCSDDGU01FrameSourceAssetReceipt_V1 and keep retry
flags false.
```

## 9. Certificate/Witness Shape

Positive certificate shape:

| field | required content |
|---|---|
| public inputs | predicate ID, run ID, selected branch, transcript windows, source locator/path, acquisition policy, no-target-import declaration |
| witness | selected branch identity, custody or lawful basis, checksum or immutable official locator, extraction command and output manifest if local, visible payload rows or explicit absence rows, equivalence proof if alternate |
| verifier predicate | branch purity, checksum recomputation or official immutability, transcript-window mapping, payload row presence or explicit absence, no cross-branch field borrowing, no downstream target-field use |
| semantic lift | acceptance authorizes only UCSD DGU01 frame/visual-row manifest retry; it does not prove sector identity, actual operator identity, same-operator equality, VZ/RS safety, generation count, exact GR, or theta recovery |
| anti-smuggling guard | reject if any required source field is filled from typed `D_roll`, downstream physical success, Oxford/manuscript adjacency alone, or a desired sector/family/generation conclusion |

Negative receipt shape emitted by this run:

```text
receipt_id: NegativeOfficialOrLawfulUCSDDGU01FrameSourceAssetReceipt_V1
predicate_id: OfficialOrLawfulUCSDDGU01FrameSourceAssetProducer_V1
run_id: hourly-20260626-1003
cycle: 2
lane: 1
scope: repo-local read-first artifacts plus narrow UCSD/DGU01 asset-identity check
official_ucsd_still_identity_present: false
lawful_local_ucsd_video_or_source_byte_identity_present: false
alternate_equivalent_source_asset_identity_present: false
first_failed_atom: selected_branch.source_asset_identity_absent_for_all_branches
target_import_used: false
frame_retry_allowed: false
same_operator_retry_allowed: false
claim_status_change: false
```

## 10. JSON Summary

```json
{
  "artifact_id": "OfficialOrLawfulUCSDDGU01FrameSourceAssetProducer_1003_C2_L1_V1",
  "run_id": "hourly-20260626-1003",
  "cycle": 2,
  "lane": 1,
  "artifact_path": "explorations/hourly-20260626-1003-cycle2-dgu-branch-pure-source-asset-producer.md",
  "verdict_class": "closed_scoped_negative_branch_pure_producer_specified_and_executed",
  "producer_id": "OfficialOrLawfulUCSDDGU01FrameSourceAssetProducer_V1",
  "target_asset_id": "OfficialOrLawfulUCSDDGU01FrameSourceAsset_V1",
  "negative_receipt_id": "NegativeOfficialOrLawfulUCSDDGU01FrameSourceAssetReceipt_V1",
  "producer_predicate_specified": true,
  "producer_executed_repo_locally": true,
  "accept_asset_emitted": false,
  "negative_receipt_emitted": true,
  "branch_purity_enforced": true,
  "frame_retry_allowed": false,
  "same_operator_retry_allowed": false,
  "target_import_used": false,
  "claim_status_change": false,
  "official_ucsd_still_identity_present": false,
  "lawful_local_ucsd_video_or_source_byte_identity_present": false,
  "alternate_equivalent_source_asset_identity_present": false,
  "first_exact_obstruction": "OfficialOrLawfulUCSDDGU01FrameSourceAssetProducer_V1.selected_branch.source_asset_identity_absent_for_all_branches",
  "constructive_next_object": "BranchPureUCSDDGU01SourceAssetSeed_V1",
  "next_meaningful_step": "produce_branch_pure_source_asset_seed_then_rerun_producer",
  "terrain": {
    "primary": "provenance-verifier",
    "secondary": "source-identity intake",
    "forbidden_shortcut": "transcript_timestamps_source_index_metadata_oxford_manuscript_adjacency_typed_D_roll_or_downstream_success_as_UCSD_DGU01_source_asset",
    "invariant": "exactly_one_branch_with_identity_custody_checksum_or_immutable_locator_frame_window_payload_and_no_target_import_before_retry_flags",
    "kill_condition": "no_branch_source_asset_identity_in_declared_repo_local_scope"
  }
}
```
