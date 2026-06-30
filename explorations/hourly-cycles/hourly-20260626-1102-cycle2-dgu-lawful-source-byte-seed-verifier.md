---
title: "Hourly 20260626 1102 Cycle 2 DGU Lawful Source Byte Seed Verifier"
date: "2026-06-26"
run_id: "hourly-20260626-1102"
cycle: 2
lane: 1
doc_type: "frontier_run_lane_artifact"
artifact_id: "LawfulLocalUCSDDGU01SourceByteSeedVerifier_1102_C2_L1_V1"
verdict: "closed_scoped_negative_verifier_defined_no_lawful_local_source_byte_seed_present"
owned_path: "explorations/hourly-20260626-1102-cycle2-dgu-lawful-source-byte-seed-verifier.md"
claim_status_change: false
---

# Hourly 20260626 1102 Cycle 2 DGU Lawful Source Byte Seed Verifier

## 1. Verdict

Verdict: **closed / scoped negative verifier application**.

This artifact defines and applies:

```text
LawfulLocalUCSDDGU01SourceByteSeedVerifier_V1
```

as the lawful-local branch verifier for:

```text
BranchPureUCSDDGU01SourceAssetSeed_V1
```

The verifier is defined and was applied to current repo state. No current
repo-local object passes it.

Decision state:

```text
verifier_defined: true
verifier_applied: true
lawful_local_source_byte_seed_present: false
source_byte_path_present: false
sha256_present: false
lawful_basis_present: false
extraction_policy_present: false
branch_pure_seed_present: false
producer_positive_rerun_allowed: false
frame_retry_allowed: false
same_operator_retry_allowed: false
target_import_used: false
claim_status_change: false
```

This is not a DGU mathematical failure. It is a source-byte provenance gate.
The prior cycle-1 acquisition packet found public locator and metadata handles,
but no branch-pure seed. This cycle converts that scoped negative into an
executable lawful-local seed verifier and shows that the lawful-local branch
still has no passing witness.

## 2. What Was Derived Directly From Repo Sources

Direct derivations:

| repo source or check | direct fact used |
|---|---|
| `RESEARCH-POSTURE.md` | Constructive source pursuit is allowed, but target data and downstream success cannot become source evidence. |
| `process/runbooks/five-lane-frontier-run.md` | The lane must decide the gate, name the first missing object, preserve terrain, invariant, shortcut, and kill condition, and avoid compatibility-as-derivation. |
| `explorations/hourly-20260626-1102-cycle1-dgu-external-seed-acquisition-packet.md` | Cycle 1 found official event metadata, a public YouTube locator, transcript windows, and Portal metadata, but no official still seed, lawful-local video/source-byte seed, or alternate-equivalent seed. |
| `explorations/hourly-20260626-1003-cycle3-dgu-source-asset-seed-decision.md` | `BranchPureUCSDDGU01SourceAssetSeed_V1` is absent in current repo-local artifacts; the lawful-local branch requires a local source-byte path, lawful basis, source SHA-256, and transcript-window extraction policy. |
| `explorations/hourly-20260626-1003-cycle2-dgu-branch-pure-source-asset-producer.md` | The producer accepts only a branch-pure source asset; official still, lawful-local source bytes, and alternate-equivalent asset are mutually exclusive branches. |
| `explorations/hourly-20260626-0904-cycle3-dgu-ucsd-frame-acquisition-preconditions.md` | Official-still, lawful-local-video, and alternate-equivalent branches were all not ready. |
| `explorations/hourly-20260626-0904-cycle2-dgu-visual-frame-asset-manifest.md` | Current repo had no UCSD source video, official still rows, extracted frame set, frame checksum manifest, or visual transcription rows. |
| `explorations/hourly-20260626-1003-cycle1-dgu-official-lawful-frame-source-asset-gate.md` | Minimum source-asset fields include source identity, custody or lawful basis, source checksum, frame locator or extraction policy, extraction manifest, and anti-smuggling guard. |
| `sources/media-index.md` | `GU-MEDIA-KEATING-QG-FBOZSSLXFVI` points to `https://youtu.be/fBozSSLxFvI` and is metadata-checked / timestamp-needed; it is a locator, not source bytes. |
| `automation/evidence/hourly-20260625-2202-rs-fbozsslxfvi/README.md` | The existing `fBozSSLxFvI` evidence directory is policy-only with `persisted_frame_count: 0`; it admits no browser capture toolchain row, frame, crop, OCR output, or checksum artifact. |
| Narrow repo-local inventory | No file path matching UCSD/DGU01/`fBozSSLxFvI`/Keating with video, still, frame, JSON manifest, CSV manifest, or checksum-bearing package was found. |

The relevant positive repo facts remain:

```text
public_video_locator_present: true
official_event_metadata_present: true
transcript_window_tie_present: true
lawful_local_source_byte_seed_present: false
```

The first three are handles for a future acquisition route. They are not a
lawful-local source-byte seed.

## 3. Verifier Predicate And Field Table

`LawfulLocalUCSDDGU01SourceByteSeedVerifier_V1` accepts a candidate `S` if and
only if all required atoms below are true inside the lawful-local branch.

Predicate:

```text
AcceptLawfulLocalSourceByteSeed(S) :=
  S.object_id = LawfulLocalUCSDDGU01SourceByteSeed_V1
  and S.parent_seed_id = BranchPureUCSDDGU01SourceAssetSeed_V1
  and S.selected_branch = lawful_local_ucsd_source_bytes
  and ExactlyOneBranchSelected(S)
  and SourceBytePathPresent(S)
  and SourceByteObjectReadableOrDeclaredImmutableInRepo(S)
  and SourceByteScopeTargetsUCSDDGU01Windows(S)
  and LawfulBasisPresent(S)
  and CustodyRecordPresent(S)
  and SourceSHA256PresentAndRecomputable(S)
  and ExtractionPolicyPresent(S)
  and ExtractionPolicyIsPreTarget(S)
  and TranscriptWindowTiePresent(S)
  and OutputManifestPolicyPresent(S)
  and AntiCrossBranchRuleSatisfied(S)
  and NoTargetImport(S)
```

Minimum field table:

| field | required content | rejection if absent or invalid |
|---|---|---|
| `object_id` | `LawfulLocalUCSDDGU01SourceByteSeed_V1` | Reject if the object is only a locator, policy row, transcript row, or producer schema. |
| `parent_seed_id` | `BranchPureUCSDDGU01SourceAssetSeed_V1` | Reject if the object does not instantiate the lawful-local branch of the branch-pure seed. |
| `selected_branch` | exactly `lawful_local_ucsd_source_bytes` | Reject if official-still, lawful-local, and alternate-equivalent fields are mixed. |
| `source_id` | stable source id, normally `GU-MEDIA-KEATING-QG-FBOZSSLXFVI` or successor UCSD source id | Reject if it only identifies a downstream claim or non-UCSD comparison surface. |
| `source_url_or_locator` | public locator for provenance, such as `https://youtu.be/fBozSSLxFvI` | Reject if this is the only source field; locator-only is not source bytes. |
| `source_byte_path` | repo-local path to the acquired source bytes or source-byte package | Reject if the path is missing, non-local, not readable, or points only to a markdown policy row. |
| `source_byte_kind` | video/source package/container type and byte-length | Reject if type and byte count are unspecified. |
| `lawful_basis` | concise basis for local possession and analysis, including capture/download/public-viewport policy and any relevant constraints | Reject if lawful possession/use is assumed but not recorded. |
| `custody_record` | acquisition actor or tool, UTC timestamp, command or method, source locator, destination path, and no-target-import declaration | Reject if custody is just "found online" or inherited from a sibling branch. |
| `sha256` | lowercase 64-hex SHA-256 for the source-byte object | Reject if missing, malformed, inherited from another asset, or not recomputable from the local path. |
| `checksum_verification` | command/tool used to recompute SHA-256 and observed match | Reject if the checksum is written but no verification method is supplied. |
| `transcript_windows` | DGU target windows tied before extraction, including `[00:32:46]-[00:36:13]` and `[00:49:16]-[00:50:09]` if both are in scope | Reject if windows are chosen after seeing target formula success. |
| `extraction_policy` | pre-target method mapping transcript windows to frame/sample/crop intervals, frame rate or sampling rule, output names, and allowed tools | Reject if extraction is manual, target-seeking, or unspecified. |
| `output_manifest_policy` | required future frame/crop/OCR output paths, SHA-256 values, and explicit-absence rows | Reject if source bytes exist but no path exists from bytes to reviewable outputs. |
| `anti_cross_branch_declaration` | official-still and alternate-equivalent branches are siblings only, not field donors | Reject if missing lawful-local fields are borrowed from official metadata, Portal thumbnails, Oxford/manuscript assets, or alternate equivalence claims. |
| `anti_smuggling_guard` | no seed field is filled from typed `D_roll`, same-operator success, VZ/RS/K3/exact-GR/theta/DESI success, generation count, or desired formula content | Reject if downstream target content supplies provenance. |

Checksum, custody, and extraction-policy requirements are conjunctive. A local
path without SHA-256 fails. SHA-256 without lawful basis fails. Local bytes and
SHA-256 without a pre-target extraction policy fail. A public URL plus an
extraction idea fails because no local source-byte object exists.

Rejection cases:

| candidate class | verifier decision |
|---|---|
| YouTube watch URL or timestamp URL only | reject: locator only, no local source bytes, no checksum. |
| UCSD event metadata | reject: official metadata belongs to the official-still sibling branch and is not source bytes. |
| Portal/Portal Wiki metadata or thumbnail | reject: metadata or promotional image, no lawful-local source-byte custody. |
| transcript window only | reject: text time base, not visual source bytes. |
| policy directory with zero persisted frames | reject: future evidence policy only, no source-byte object. |
| unchecksummed screenshot or unrecorded manual capture | reject: no recomputable source SHA-256 and no custody. |
| Oxford/manuscript/rendered page asset | reject: alternate/comparison surface unless a separate pre-target equivalence proof is supplied; cannot donate lawful-local fields. |
| downstream DGU/VZ/RS/K3/exact-GR/theta success | reject: target import. |

What a passing verifier would unlock:

```text
LawfulLocalUCSDDGU01SourceByteSeedVerifier_V1 accepts
  -> BranchPureUCSDDGU01SourceAssetSeed_V1 lawful-local branch accepts
  -> producer_positive_rerun_allowed = true
  -> rerun OfficialOrLawfulUCSDDGU01FrameSourceAssetProducer_V1
```

It would not itself unlock frame retry or same-operator retry. Those require the
producer to accept and then emit an admitted frame/output manifest with payload
rows or explicit absence rows:

```text
frame_retry_allowed :=
  accepted OfficialOrLawfulUCSDDGU01FrameSourceAsset_V1
  and admitted UCSDDGU01FrameOutputManifest_V1

same_operator_retry_allowed :=
  frame_retry_allowed
  and source_row_actual_operator_handle_present
```

## 4. Application To Current Repo State

Application scope:

```text
assigned read-first files
plus narrow repo-local inventory for lawful-local source-byte evidence:
  LawfulLocalUCSDDGU01 terms
  lawful-local/source-byte/source bytes terms
  BranchPureUCSDDGU01SourceAssetSeed_V1 terms
  fBozSSLxFvI/UCSD/DGU01/Keating path terms
  local media/manifest/checksum path names matching those terms
```

Current candidates and decisions:

| candidate | strongest lawful-local field supplied | first failed verifier atom |
|---|---|---|
| `sources/media-index.md` row `GU-MEDIA-KEATING-QG-FBOZSSLXFVI` | public YouTube locator and metadata-checked source id | `source_byte_path_present = false` |
| `explorations/hourly-20260626-1102-cycle1-dgu-external-seed-acquisition-packet.md` | acquisition receipt with URL register and scoped negative | not a seed instance; `source_byte_path_present = false` |
| `automation/evidence/hourly-20260625-2202-rs-fbozsslxfvi/README.md` | future evidence directory policy tied to `fBozSSLxFvI` | `persisted_frame_count = 0`; no source bytes, no checksum, no extraction output |
| `literature/weinstein-ucsd-2025-04-transcript.md` | transcript windows and UCSD time base | transcript text is not visual source bytes |
| prior DGU source-asset gates | verifier/producer schemas and negative receipts | schemas are not source-byte witnesses |
| Oxford/manuscript/rendered page assets referenced by prior gates | comparison surfaces with separate custody in other routes | sibling/alternate surfaces only; no pre-target equivalence proof to UCSD DGU01 visual windows and no lawful-local UCSD source bytes |

Field evaluation:

| verifier field | current value | reason |
|---|---:|---|
| `object_id = LawfulLocalUCSDDGU01SourceByteSeed_V1` | false | no current artifact instantiates this object. |
| `parent_seed_id = BranchPureUCSDDGU01SourceAssetSeed_V1` | false | current appearances are proposed next objects or verifier text, not a positive seed instance. |
| `selected_branch = lawful_local_ucsd_source_bytes` | false | no branch-pure seed has selected the lawful-local branch. |
| `source_url_or_locator` | true | `sources/media-index.md` and cycle 1 record `https://youtu.be/fBozSSLxFvI`. |
| `source_byte_path` | false | no repo-local video/source-byte path was found. |
| `source_byte_kind_and_size` | false | no source-byte object exists to type or size. |
| `lawful_basis` | false | no local possession/use basis for source bytes is recorded. |
| `custody_record` | false | no acquisition method, actor/tool, timestamp, destination path, or custody chain for local bytes is recorded. |
| `sha256` | false | no SHA-256 exists for UCSD DGU01 local source bytes. |
| `checksum_verification` | false | no source-byte hash can be recomputed without source bytes. |
| `transcript_window_tie` | true | transcript windows are present and used as target windows. |
| `extraction_policy` | false | no pre-target extraction command/policy tied to a local source-byte object is present. |
| `output_manifest_policy` | partial | prior gates define required manifest shape, but no lawful-local seed carries it with source bytes. |
| `anti_cross_branch_declaration` | true in this artifact | the verifier forbids sibling branches from donating lawful-local fields. |
| `anti_smuggling_guard` | true in this artifact | the verifier rejects target import. |

Result:

```text
AcceptLawfulLocalSourceByteSeed(current_repo) = false
```

No current object passes. The first failure is before checksum and extraction:

```text
LawfulLocalUCSDDGU01SourceByteSeedVerifier_V1.source_byte_path_present = false
```

Because the source-byte path is absent, the SHA-256, custody, lawful basis, and
extraction policy cannot be satisfied for this branch.

## 5. First Exact Obstruction Or Missing Object

The first exact obstruction is:

```text
LawfulLocalUCSDDGU01SourceByteSeed_V1.source_byte_path
```

More explicitly:

```text
not exists S such that
  S.object_id = LawfulLocalUCSDDGU01SourceByteSeed_V1
  and S.parent_seed_id = BranchPureUCSDDGU01SourceAssetSeed_V1
  and S.selected_branch = lawful_local_ucsd_source_bytes
  and S.source_byte_path is repo-local and readable
  and S.sha256 is recomputable from S.source_byte_path
  and S.lawful_basis is recorded
  and S.extraction_policy is pre-target and transcript-window-bounded
```

This obstruction is earlier than frame extraction, OCR, visible formula
transcription, source-row payload, actual operator handle, same-operator
equality, VZ safety, RS physical-symbol replay, K3/family readout, exact-GR
recovery, or theta recovery.

## 6. Constructive Next Object

The constructive next object is:

```text
LawfulLocalUCSDDGU01SourceByteSeedCandidate_V1
```

Minimum object shape:

```yaml
object_id: LawfulLocalUCSDDGU01SourceByteSeedCandidate_V1
parent_seed_id: BranchPureUCSDDGU01SourceAssetSeed_V1
selected_branch: lawful_local_ucsd_source_bytes
source_id: GU-MEDIA-KEATING-QG-FBOZSSLXFVI
source_url_or_locator: https://youtu.be/fBozSSLxFvI
source_byte_path: <repo-local path to source bytes or source-byte package>
source_byte_kind: <video/container/source package type>
source_byte_size: <integer bytes>
lawful_basis: <recorded basis for local possession/use and analysis>
custody_record:
  acquired_at_utc: <timestamp>
  acquired_by_or_tool: <tool/person/process>
  acquisition_method: <command or public-viewport/source-byte method>
  destination_path: <repo-local path>
  no_target_import: true
sha256: <64 lowercase hex>
checksum_verification:
  command_or_tool: <sha256 command/tool>
  verified_at_utc: <timestamp>
  observed_match: true
transcript_windows:
  - "[00:32:46]-[00:36:13]"
  - "[00:49:16]-[00:50:09]"
extraction_policy:
  policy_id: UCSDDGU01PreTargetWindowExtractionPolicy_V1
  selection_rule: transcript_window_bounded_pre_target
  sampling_rule: <frame/time sampling rule>
  output_manifest_required: true
anti_cross_branch_declaration:
  official_still_branch_is_sibling_not_donor: true
  alternate_equivalent_branch_is_sibling_not_donor: true
anti_smuggling_guard:
  downstream_target_import_used: false
```

The first positive rerun is not a visual-row rerun. It is:

```text
LawfulLocalUCSDDGU01SourceByteSeedCandidate_V1
  -> LawfulLocalUCSDDGU01SourceByteSeedVerifier_V1
  -> BranchPureUCSDDGU01SourceAssetSeed_V1
  -> OfficialOrLawfulUCSDDGU01FrameSourceAssetProducer_V1
```

## 7. Meaning For DGU Frame/Same-Operator Claims

Allowed statement:

```text
The repo has a public UCSD/Keating video locator, transcript windows, branch-pure
producer and seed schemas, and now a lawful-local source-byte seed verifier.
The lawful-local seed does not currently pass because no local source-byte path
with SHA-256, lawful basis, custody, and extraction policy exists.
```

Not allowed:

```text
The repo has a lawful-local UCSD DGU01 source-byte seed.
The repo has an official UCSD DGU01 still/frame seed.
The repo has an alternate-equivalent DGU01 seed.
The branch-pure source-asset producer may rerun positively now.
UCSD DGU01 frame extraction may retry now.
DGU01 same-operator equality may retry now.
Downstream DGU/VZ/RS/K3/exact-GR/theta success supplies missing source custody.
```

This artifact changes no claim status. It only sharpens the lawful-local branch
gate and keeps producer, frame, and same-operator retry flags false.

## 8. Terrain Classification, Forbidden Shortcut, Invariant, Kill Condition

Terrain:

```text
primary: provenance-verifier/source-byte custody
secondary: extraction-policy gate
blocked downstream: visual-row extraction, same-operator equality,
  spectral-phase and microlocal-subprincipal routes, noncompact-APS/K3-family
  readout, smooth-variational exact-GR/theta recovery
```

Forbidden shortcut:

```text
Do not treat YouTube locators, timestamp URLs, UCSD event metadata,
Portal/Portal Wiki metadata, promotional thumbnails, transcript text,
directory policy rows, official-still sibling fields, alternate-equivalent
sibling fields, Oxford/manuscript comparison assets, or downstream target
success as lawful-local UCSD DGU01 source bytes.
```

Invariant:

```text
The lawful-local branch accepts only if one repo-local source-byte object carries
its own lawful basis, custody record, recomputable SHA-256, transcript-window
tie, and pre-target extraction policy. Sibling branches may coexist, but they
cannot donate missing lawful-local fields.
```

Kill condition:

```text
If no repo-local source-byte path exists for the UCSD DGU01 lawful-local branch,
then LawfulLocalUCSDDGU01SourceByteSeedVerifier_V1 must reject before checksum,
extraction, frame retry, or same-operator evaluation.
```

## 9. Certificate/Witness Shape

Positive certificate shape:

| field | required content |
|---|---|
| public inputs | verifier id, parent seed id, run id, selected branch, source id, public locator, transcript windows, acquisition policy, anti-target-import declaration |
| witness | repo-local source-byte path, byte type and size, lawful basis, custody record, SHA-256, checksum verification command/result, pre-target extraction policy |
| verifier predicate | exactly one branch selected; local source path exists; SHA-256 recomputes; lawful basis and custody are present; extraction policy is pre-target and bounded to transcript windows; no sibling branch field borrowing; no downstream target import |
| semantic lift | accepted lawful-local seed authorizes only branch-pure seed acceptance and producer rerun; it does not prove frame payload, sector identity, actual operator identity, same-operator equality, VZ/RS/K3/exact-GR/theta claims, or generation count |
| anti-smuggling guard | reject if any required field is supplied by official metadata, Portal thumbnails, Oxford/manuscript adjacency, typed `D_roll`, same-operator success, target physics, DESI/theta/exact-GR success, or desired displayed formula content |

Negative witness emitted here:

```text
receipt_id: NegativeLawfulLocalUCSDDGU01SourceByteSeedVerifierReceipt_V1
predicate_id: LawfulLocalUCSDDGU01SourceByteSeedVerifier_V1
run_id: hourly-20260626-1102
cycle: 2
lane: 1
scope: repo-local assigned sources plus narrow lawful-local source-byte inventory
source_locator_present: true
transcript_window_tie_present: true
source_byte_path_present: false
sha256_present: false
lawful_basis_present: false
custody_record_present: false
extraction_policy_present: false
lawful_local_source_byte_seed_present: false
branch_pure_seed_present: false
first_failed_atom: LawfulLocalUCSDDGU01SourceByteSeed_V1.source_byte_path
producer_positive_rerun_allowed: false
frame_retry_allowed: false
same_operator_retry_allowed: false
target_import_used: false
claim_status_change: false
```

## 10. JSON Summary

```json
{
  "artifact_id": "LawfulLocalUCSDDGU01SourceByteSeedVerifier_1102_C2_L1_V1",
  "run_id": "hourly-20260626-1102",
  "cycle": 2,
  "lane": 1,
  "artifact_path": "explorations/hourly-20260626-1102-cycle2-dgu-lawful-source-byte-seed-verifier.md",
  "object_defined": "LawfulLocalUCSDDGU01SourceByteSeedVerifier_V1",
  "object_tested": "LawfulLocalUCSDDGU01SourceByteSeed_V1",
  "parent_seed": "BranchPureUCSDDGU01SourceAssetSeed_V1",
  "verdict_class": "closed_scoped_negative_verifier_defined_no_lawful_local_source_byte_seed_present",
  "verifier_defined": true,
  "verifier_applied": true,
  "lawful_local_source_byte_seed_present": false,
  "source_byte_path_present": false,
  "sha256_present": false,
  "lawful_basis_present": false,
  "custody_record_present": false,
  "extraction_policy_present": false,
  "branch_pure_seed_present": false,
  "producer_positive_rerun_allowed": false,
  "frame_retry_allowed": false,
  "same_operator_retry_allowed": false,
  "target_import_used": false,
  "claim_status_change": false,
  "source_locator_present": true,
  "transcript_window_tie_present": true,
  "first_exact_obstruction": "LawfulLocalUCSDDGU01SourceByteSeed_V1.source_byte_path_absent",
  "constructive_next_object": "LawfulLocalUCSDDGU01SourceByteSeedCandidate_V1",
  "producer_id": "OfficialOrLawfulUCSDDGU01FrameSourceAssetProducer_V1",
  "negative_receipt_id": "NegativeLawfulLocalUCSDDGU01SourceByteSeedVerifierReceipt_V1",
  "anti_cross_branch_rule": "official_still_and_alternate_equivalent_branches_are_siblings_not_donors_for_lawful_local_fields",
  "terrain": {
    "primary": "provenance-verifier/source-byte custody",
    "secondary": "extraction-policy gate",
    "forbidden_shortcut": "youtube_locator_timestamp_url_ucsd_metadata_portal_metadata_thumbnail_transcript_policy_row_sibling_branch_field_oxford_manuscript_asset_or_downstream_success_as_lawful_local_source_bytes",
    "invariant": "one_repo_local_source_byte_object_with_lawful_basis_custody_recomputable_sha256_transcript_window_tie_and_pre_target_extraction_policy",
    "kill_condition": "no_repo_local_source_byte_path_means_verifier_rejects_before_checksum_extraction_frame_retry_or_same_operator_evaluation"
  }
}
```
