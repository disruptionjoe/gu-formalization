---
title: "Hourly 20260626 1003 Cycle 3 DGU Source Asset Seed Decision"
date: "2026-06-26"
run_id: "hourly-20260626-1003"
cycle: 3
lane: 1
doc_type: "frontier_run_lane_artifact"
artifact_id: "BranchPureUCSDDGU01SourceAssetSeedDecision_1003_C3_L1_V1"
verdict: "closed_scoped_negative_no_branch_pure_seed_present"
owned_path: "explorations/hourly-20260626-1003-cycle3-dgu-source-asset-seed-decision.md"
claim_status_change: false
---

# Hourly 20260626 1003 Cycle 3 DGU Source Asset Seed Decision

## 1. Verdict

Verdict: **closed / scoped negative for repo-local seed existence**.

The object consumed from cycle 2 was:

```text
BranchPureUCSDDGU01SourceAssetSeed_V1
```

The seed was attempted, but no repo-local artifact now instantiates it. The
only current appearances of `BranchPureUCSDDGU01SourceAssetSeed_V1` are as the
cycle-2 constructive next object and rerun trigger, not as an accepted seed
with one selected branch and minimum source fields.

Decision state:

```text
seed_attempted: true
branch_pure_seed_present: false
official_still_seed_present: false
lawful_local_video_seed_present: false
alternate_equivalent_seed_present: false
producer_positive_rerun_allowed: false
external_source_acquisition_required: true
frame_retry_allowed: false
same_operator_retry_allowed: false
target_import_used: false
claim_status_change: false
```

Therefore the cycle-2 producer should not be rerun positively on current
repo-local artifacts. A rerun without a new seed would deterministically repeat
the same first failure: no selected branch has source-asset identity. The final
next frontier is external/source acquisition under a branch-pure seed packet,
not another frame-row, same-operator, or downstream DGU retry.

## 2. What Was Derived Directly From Repo Sources

This decision used the assigned read-first sources plus a narrow repo-local
inventory check for the exact seed, producer, and UCSD/DGU01 source-identity
terms. No external media was acquired and no broad web/media search was
repeated.

Direct derivations:

| repo source or check | direct fact used |
|---|---|
| `RESEARCH-POSTURE.md` | Constructive next objects are allowed, but target data cannot be hidden inside source evidence. |
| `process/runbooks/five-lane-frontier-run.md` | The lane must decide the object, name the first missing proof object, preserve terrain/kill conditions, and avoid compatibility-as-derivation. |
| `explorations/hourly-20260626-1003-cycle2-dgu-branch-pure-source-asset-producer.md` | Defines `BranchPureUCSDDGU01SourceAssetSeed_V1` as the next object and requires exactly one branch: official still, lawful-local video, or alternate-equivalent source asset. |
| `explorations/hourly-20260626-1003-cycle1-dgu-official-lawful-frame-source-asset-gate.md` | Records all three acquisition branches absent at the source-asset gate and names `source_asset_identity` as the first obstruction. |
| `explorations/hourly-20260626-0904-cycle3-dgu-ucsd-frame-acquisition-preconditions.md` | Separates official still, lawful-local video, and alternate-equivalent branches; all were not ready. |
| Exact object search | `BranchPureUCSDDGU01SourceAssetSeed_V1` is present only as a proposed next object/rerun trigger, not as a seed instance. |
| Narrow UCSD/DGU01 path inventory | UCSD/DGU01-named repo files are prior artifacts, audits, transcripts, and source-route notes; no local video/still/source-byte/checksum package satisfying the seed fields was found. |

The derived repo-local positives remain useful but insufficient:

```text
UCSD transcript windows: present as locator hints
branch-pure producer predicate: specified
negative source-asset receipt: available from cycle 2
source-acquisition branch schema: specified
```

None of these is a seed instance. A transcript window can tie a future seed to
the UCSD time base, but it is not a still locator, a local video/source-byte
path, a checksum, custody evidence, or an alternate-equivalence proof.

## 3. Strongest Positive Construction Attempt

The strongest attempted construction was to assemble a branch-pure seed from
current repo-local artifacts without borrowing across branches.

Required seed predicate:

```text
BranchPureUCSDDGU01SourceAssetSeed_V1 accepts iff:
  exactly_one(selected_branch in {
    official_still_seed,
    lawful_local_video_seed,
    alternate_equivalent_seed
  })
  and selected_branch carries its minimum identity/custody/locator fields
  and no unselected branch donates missing fields
  and no downstream target claim supplies source evidence
```

Branch attempt table:

| branch | strongest available repo-local candidate | first failed atom |
|---|---|---|
| official still seed | UCSD transcript and source-index references identify a lecture context and windows. | No official UCSD still/frame locator or immutable official ID is present. |
| lawful-local video seed | Prior artifacts specify what a lawful local UCSD video/source-byte object would need. | No repo-local UCSD video/source-byte path with lawful basis and SHA-256 is present. |
| alternate-equivalent seed | Oxford/manuscript/adjacent artifacts remain comparison surfaces and some non-UCSD objects have their own custody/checksums. | No source-stable pre-target equivalence proof ties an alternate asset to the UCSD DGU01 visual windows. |

The official branch comes closest because the transcript provides a UCSD time
base. It still fails before branch acceptance: a timecoded transcript locator
does not identify an official still/frame asset and does not supply custody or
immutability for any visual object.

The alternate branch also fails early. Adjacent Oxford/manuscript payloads
cannot be used as a UCSD seed unless a source-stable equivalence proof is
present before any target physics, typed operator success, or same-operator
claim enters the record.

## 4. First Exact Obstruction/Missing Object

The first exact obstruction is:

```text
BranchPureUCSDDGU01SourceAssetSeed_V1
  .selected_branch
  .source_asset_identity_or_immutable_locator
is absent.
```

Equivalently:

```text
not exists seed_instance such that
  seed_instance.object_id = BranchPureUCSDDGU01SourceAssetSeed_V1
  and exactly_one(seed_instance.branch_kind)
  and seed_instance.branch_kind in {
    official_still_seed,
    lawful_local_video_seed,
    alternate_equivalent_seed
  }
  and seed_instance.selected_branch.minimum_identity_custody_locator_fields_present
```

This is earlier than checksum recomputation, frame extraction, OCR, visual
payload transcription, sector-rule identification, actual operator handle, or
same-operator equality. The repo lacks the seed instance itself.

Minimum missing branch atoms:

| seed branch | missing atom |
|---|---|
| official still seed | `official_ucsd_still_or_frame_locator_or_immutable_id` |
| lawful-local video seed | `repo_local_ucsd_video_or_source_byte_path_with_sha256` |
| alternate-equivalent seed | `alternate_asset_identity_with_pre_target_equivalence_to_ucsd_dgu01_windows` |

## 5. Constructive Next Object

The constructive next object is now acquisition-facing:

```text
ExternalUCSDDGU01BranchPureSourceAssetSeedAcquisitionPacket_V1
```

It should produce exactly one of these seed branches:

| branch | minimum required fields |
|---|---|
| official still seed | official UCSD still/frame locator or immutable official ID; official authority label; transcript-window tie. |
| lawful-local video seed | local source-byte path; lawful basis for local possession/use; source SHA-256; transcript-window extraction policy. |
| alternate-equivalent seed | alternate asset identity; custody/checksum/immutable locator; pre-target equivalence proof to the UCSD DGU01 windows. |

If this packet emits a valid seed, the next action is:

```text
BranchPureUCSDDGU01SourceAssetSeed_V1
  -> rerun OfficialOrLawfulUCSDDGU01FrameSourceAssetProducer_V1
```

If it cannot emit one, the correct output is a negative acquisition receipt,
not a proof restart.

## 6. Meaning For DGU/Same-Operator/Visual-Row Claims

Allowed statement:

```text
The repo has a branch-pure source-asset producer and a precise seed predicate.
Current repo-local artifacts do not instantiate the seed.
```

Not allowed:

```text
The repo has an official UCSD DGU01 still/frame seed.
The repo has a lawful-local UCSD DGU01 video/source-byte seed.
The repo has an alternate equivalent UCSD DGU01 source seed.
The cycle-2 producer can be rerun positively now.
UCSD DGU01 frame/visual rows can be retried now.
DGU01 same-operator equality can be retried now.
Downstream DGU/VZ/RS/K3/exact-GR/theta branches can restart from UCSD DGU01 now.
```

DGU remains source-blocked at the seed layer. This decision does not promote,
demote, or otherwise change any claim status.

## 7. Next Meaningful Proof/Computation Step

Do not run frame retry or same-operator retry next. The next meaningful step is
source acquisition:

```text
ExternalUCSDDGU01BranchPureSourceAssetSeedAcquisitionPacket_V1
  -> BranchPureUCSDDGU01SourceAssetSeed_V1
  -> OfficialOrLawfulUCSDDGU01FrameSourceAssetProducer_V1
```

The acquisition packet should be narrow and branch-pure. It should either:

1. acquire an official still/frame locator or immutable ID;
2. acquire a lawful-local UCSD video/source-byte object with checksum and
   extraction policy; or
3. acquire an alternate source asset plus a pre-target equivalence proof to the
   UCSD DGU01 visual windows.

Only after one branch emits a valid seed should the producer be rerun. Only
after the producer accepts should `UCSDDGU01FrameOutputManifest_V1` or any
same-operator witness be evaluated.

## 8. Terrain Classification, Forbidden Shortcut, Invariant, Kill Condition

Terrain:

```text
primary: provenance-verifier
secondary: source-acquisition intake
blocked downstream: visual-row extraction, same-operator equality,
  spectral-phase and exact-GR/theta proof routes
```

Forbidden shortcut:

```text
Do not treat transcript timestamps, source-index metadata, prior negative
receipts, Oxford/manuscript adjacency, typed D_roll compatibility, or desired
downstream physical success as a UCSD DGU01 source-asset seed.
```

Invariant:

```text
A valid seed selects exactly one branch and supplies that branch's minimum
source identity, custody/lawful basis, and locator/checksum fields before any
producer-positive, frame-retry, or same-operator-retry flag can be true.
```

Kill condition:

```text
If no repo-local artifact instantiates exactly one seed branch with minimum
identity/custody/locator fields, then BranchPureUCSDDGU01SourceAssetSeed_V1
is absent; producer_positive_rerun_allowed, frame_retry_allowed, and
same_operator_retry_allowed remain false.
```

## 9. Certificate/Witness Shape

Positive seed certificate:

| field | required content |
|---|---|
| public inputs | object ID, run ID, selected branch kind, UCSD DGU01 transcript windows, acquisition policy, anti-target-import declaration. |
| witness | selected branch identity plus custody/lawful basis and locator/checksum fields; for local video, source path, SHA-256, and extraction policy; for alternate source, equivalence proof. |
| verifier predicate | exactly-one-branch selection, branch-local field completeness, checksum or official immutability where applicable, transcript-window tie, no cross-branch field borrowing. |
| semantic lift | A valid seed authorizes only a producer rerun; it does not prove visual payload, sector identity, operator identity, same-operator equality, VZ safety, generation count, exact GR, or theta recovery. |
| anti-smuggling guard | Reject if any seed field is supplied from typed `D_roll`, downstream physics success, Oxford/manuscript adjacency without equivalence, or a desired DGU/same-operator conclusion. |

Negative seed receipt emitted by this decision:

```text
receipt_id: NegativeBranchPureUCSDDGU01SourceAssetSeedReceipt_V1
predicate_id: BranchPureUCSDDGU01SourceAssetSeed_V1
run_id: hourly-20260626-1003
cycle: 3
lane: 1
scope: repo-local assigned sources plus narrow exact-object/source-identity inventory
seed_attempted: true
branch_pure_seed_present: false
official_still_seed_present: false
lawful_local_video_seed_present: false
alternate_equivalent_seed_present: false
first_failed_atom: selected_branch.source_asset_identity_or_immutable_locator_absent
producer_positive_rerun_allowed: false
external_source_acquisition_required: true
frame_retry_allowed: false
same_operator_retry_allowed: false
target_import_used: false
claim_status_change: false
```

## 10. JSON Summary

```json
{
  "artifact_id": "BranchPureUCSDDGU01SourceAssetSeedDecision_1003_C3_L1_V1",
  "run_id": "hourly-20260626-1003",
  "cycle": 3,
  "lane": 1,
  "artifact_path": "explorations/hourly-20260626-1003-cycle3-dgu-source-asset-seed-decision.md",
  "object_tested": "BranchPureUCSDDGU01SourceAssetSeed_V1",
  "verdict_class": "closed_scoped_negative_no_branch_pure_seed_present",
  "seed_attempted": true,
  "branch_pure_seed_present": false,
  "official_still_seed_present": false,
  "lawful_local_video_seed_present": false,
  "alternate_equivalent_seed_present": false,
  "producer_positive_rerun_allowed": false,
  "external_source_acquisition_required": true,
  "frame_retry_allowed": false,
  "same_operator_retry_allowed": false,
  "target_import_used": false,
  "claim_status_change": false,
  "first_exact_obstruction": "BranchPureUCSDDGU01SourceAssetSeed_V1.selected_branch.source_asset_identity_or_immutable_locator_absent",
  "constructive_next_object": "ExternalUCSDDGU01BranchPureSourceAssetSeedAcquisitionPacket_V1",
  "next_meaningful_step": "source_acquisition_then_seed_instantiation_then_producer_rerun",
  "negative_receipt_id": "NegativeBranchPureUCSDDGU01SourceAssetSeedReceipt_V1",
  "producer_id": "OfficialOrLawfulUCSDDGU01FrameSourceAssetProducer_V1",
  "producer_rerun_condition": "valid_branch_pure_seed_present",
  "terrain": {
    "primary": "provenance-verifier",
    "secondary": "source-acquisition intake",
    "forbidden_shortcut": "transcript_timestamps_source_index_prior_negative_receipts_oxford_manuscript_adjacency_typed_D_roll_or_downstream_success_as_UCSD_DGU01_seed",
    "invariant": "exactly_one_branch_with_minimum_identity_custody_lawful_basis_locator_or_checksum_before_positive_rerun_or_retry_flags",
    "kill_condition": "no_repo_local_branch_pure_seed_instance_with_minimum_fields"
  }
}
```
