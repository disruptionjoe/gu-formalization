---
title: "Hourly 20260626 1102 Cycle 1 DGU External Seed Acquisition Packet"
date: "2026-06-26"
run_id: "hourly-20260626-1102"
cycle: 1
lane: 1
doc_type: "frontier_run_lane_artifact"
artifact_id: "ExternalUCSDDGU01BranchPureSourceAssetSeedAcquisitionPacket_1102_C1_L1_V1"
verdict: "closed_scoped_negative_no_branch_pure_external_seed_present"
owned_path: "explorations/hourly-20260626-1102-cycle1-dgu-external-seed-acquisition-packet.md"
claim_status_change: false
---

# Hourly 20260626 1102 Cycle 1 DGU External Seed Acquisition Packet

## 1. Verdict

Verdict: **closed / scoped negative acquisition receipt**.

`ExternalUCSDDGU01BranchPureSourceAssetSeedAcquisitionPacket_V1` was attempted
against repo-local sources and lightweight public lookup surfaces. No current
repo-local object or easily attributable public source found in this pass
instantiates exactly one accepted seed branch for
`BranchPureUCSDDGU01SourceAssetSeed_V1`.

Decision state:

```text
seed_attempted: true
branch_pure_seed_present: false
official_still_seed_present: false
lawful_local_video_seed_present: false
alternate_equivalent_seed_present: false
producer_positive_rerun_allowed: false
frame_retry_allowed: false
same_operator_retry_allowed: false
target_import_used: false
claim_status_change: false
```

This is not a DGU mathematical failure. It is a scoped negative acquisition
receipt. The current record contains official UCSD event metadata, a public
YouTube/Portal video locator surface, transcript windows, and prior locator-only
execution ledgers. Those objects are useful acquisition handles, but none is a
branch-pure seed.

## 2. What Was Derived Directly From Repo Sources

Direct repo-derived facts:

| repo source | direct fact used |
|---|---|
| `RESEARCH-POSTURE.md` | Constructive source pursuit is allowed, but target data, compatibility, and desired downstream success cannot become evidence. |
| `process/runbooks/five-lane-frontier-run.md` | This lane must decide the gate, name the exact obstruction, preserve terrain and kill conditions, and avoid compatibility-as-derivation. |
| `explorations/hourly-20260626-1003-cycle3-dgu-source-asset-seed-decision.md` | Current repo-local artifacts do not instantiate `BranchPureUCSDDGU01SourceAssetSeed_V1`; all seed branches were absent. |
| `explorations/hourly-20260626-1003-cycle2-dgu-branch-pure-source-asset-producer.md` | The seed must select exactly one branch: official UCSD still/frame, lawful-local UCSD video/source bytes, or alternate-equivalent source asset with pre-target equivalence. |
| `explorations/hourly-20260626-0904-cycle3-dgu-ucsd-frame-acquisition-preconditions.md` | Official-still, lawful-local-video, and alternate-equivalent acquisition branches were all not ready. |
| `literature/weinstein-ucsd-2025-04-transcript.md` | The local raw transcript gives UCSD talk context and DGU-relevant windows, especially `[00:32:46]-[00:36:13]` and `[00:49:16]-[00:50:09]`; it is text, not a visual asset. |
| `sources/media-index.md` | `GU-MEDIA-KEATING-QG-FBOZSSLXFVI` points to `https://youtu.be/fBozSSLxFvI` and is marked metadata-checked / timestamp-needed. |
| `automation/evidence/hourly-20260625-2202-rs-fbozsslxfvi/README.md` | The local evidence directory is policy-only: zero persisted frames, zero crops, zero OCR, zero checksums. |
| `explorations/hourly-20260625-1503-cycle2-rs-ucsd-visual-locator-unavailability-packet.md` | A stable public YouTube locator exists for the video, but no captured/checksummed visual object or unavailability packet exists. |
| `explorations/hourly-20260625-1802-cycle1-rs-ucsd-capture-stack-execution-ledger.md` | Prior execution reached the YouTube locator/oEmbed but blocked at missing source bytes or lawful reproducible acquisition route. |

Repo inventory checks found no DGU/UCSD-target local media object in the scoped
paths inspected. Existing `automation/tmp/.../pdf_page_*.png` files are
manuscript page images from another route, not UCSD DGU01 video or still frames.

## 3. Strongest Positive Acquisition Attempt

The strongest positive attempt was the alternate-equivalent assembly attempt:

```text
UCSD official event metadata
  + public YouTube locator for fBozSSLxFvI
  + Portal/Portal Wiki metadata describing the UCSD lecture
  + local transcript windows
  -> candidate acquisition handle only
```

Public lookup register:

| URL | source class | exact role in this packet | seed result |
|---|---|---|---|
| `https://astro.ucsd.edu/events/index.html` | official UCSD / metadata only | UCSD Astronomy & Astrophysics events page lists Eric Weinstein, "From Dark to Geometric Energy: Replacing the Cosmological Constant in light of recent findings", Mayer Hall/Mayer Room, April 28, 2025. | Reject as seed: official event metadata, not an official still/frame locator or source bytes. |
| `https://www.youtube.com/watch?v=fBozSSLxFvI` | public YouTube locator / custodian-adjacent metadata only | Public watch surface for the Keating video found by search and already indexed in repo. | Reject as seed: remote locator only; no lawful-local bytes, no checksum, no frame manifest. |
| `https://www.youtube.com/watch?v=fBozSSLxFvI&t=1966s` | public timestamp locator / metadata only | Start locator for transcript window `[00:32:46]-[00:36:13]`. | Reject as seed: timestamp locator is not captured visual evidence. |
| `https://www.youtube.com/watch?v=fBozSSLxFvI&t=2956s` | public timestamp locator / metadata only | Start locator for transcript window `[00:49:16]-[00:50:09]`. | Reject as seed: timestamp locator is not captured visual evidence. |
| `https://theportal.wiki/wiki/From_Dark_to_Geometric_Energy_-_A_Sector_of_Geometric_Unity_%28YouTube_Content%29` | secondary/custodian-adjacent metadata only | Records title, host as University of California, San Diego, length `00:50:40`, release date May 22, 2025, and says no edited transcript exists. | Reject as seed: secondary metadata and link aggregator only. |
| `https://theportal.group/from-dark-to-geometric-energy-a-sector-of-geometric-unity/` | Portal Group metadata / thumbnail page | Describes the lecture as held live at UCSD in April 2025 and embeds a promotional image URL. | Reject as seed: metadata and promotional page, not UCSD official still/frame or local source bytes. |
| `https://theportal.group/wp-content/uploads/2025/05/20250522-Brian-Keating-UCSD-lecture-fBozSSLxFvI.jpg` | promotional thumbnail image / not UCSD official | Thumbnail-like promotional image for the Portal Group page. | Reject as seed: not an official UCSD DGU01 frame/still and not equivalent to the target visual windows. |
| `https://theportal.wiki/images/f/f0/20250522-Brian-Keating-UCSD-lecture-%28fBozSSLxFvI%29.jpg` | secondary thumbnail mirror / not UCSD official | Portal Wiki image for the same content page. | Reject as seed: not an official UCSD DGU01 frame/still and no pre-target equivalence to DGU01 windows. |

Branch attempt table:

| seed branch | strongest available candidate | first failed atom |
|---|---|---|
| official UCSD still/frame | Official UCSD event listing confirms the seminar context and title. | No official UCSD still/frame locator, immutable frame ID, official slide image, or UCSD-hosted target-window visual object. |
| lawful-local UCSD video/source bytes | Repo has a public YouTube locator and a policy directory for future evidence. | No repo-local video/source-byte path, no lawful local acquisition route, no source SHA-256, no extracted frame manifest. |
| alternate-equivalent asset | YouTube/Portal locator plus transcript windows is a plausible acquisition handle. | No pre-target equivalence proof tying an alternate asset to UCSD DGU01 visual windows, and no captured/checksummed alternate visual packet. |

The strongest positive result is therefore:

```text
PublicAcquisitionHandleForUCSDDGU01_V1:
  official_event_metadata_present: true
  public_video_locator_present: true
  transcript_window_tie_present: true
  branch_pure_seed_present: false
```

## 4. First Exact Obstruction Or Missing Proof/Source Object

The first exact obstruction is:

```text
ExternalUCSDDGU01BranchPureSourceAssetSeedAcquisitionPacket_V1
  .selected_branch
  .minimum_branch_source_object
is absent for every accepted branch.
```

Expanded branch failures:

```text
official_still_seed.official_ucsd_still_or_frame_locator_or_immutable_id = absent
lawful_local_video_seed.repo_local_video_or_source_byte_path_with_sha256 = absent
alternate_equivalent_seed.pre_target_equivalence_to_ucsd_dgu01_windows = absent
```

The obstruction is earlier than frame extraction, OCR, visual-row
transcription, actual operator identity, same-operator equality, VZ safety,
exact-GR recovery, theta recovery, or family/generation claims.

## 5. Constructive Next Object That Would Remove Or Test The Obstruction

The next object should be branch-specific and should select only one branch.

Highest-value next object:

```text
DGU01LawfulSourceAcquisitionRouteOrOfficialFrameLocator_V1
```

It should emit exactly one of:

| branch | minimum object to emit |
|---|---|
| official still/frame | `OfficialUCSDDGU01StillOrFrameLocatorReceipt_V1`: UCSD-hosted still/frame/slide URL or immutable ID, official authority label, target-window tie, and immutability/checksum policy. |
| lawful-local video/source bytes | `LawfulLocalFBozSSLxFvIDGU01SourceByteOrViewportCaptureRoute_V1`: lawful acquisition basis, tool names/versions/commands, local source or captured frame paths, SHA-256 values, and transcript-window extraction policy. |
| alternate-equivalent source asset | `AlternateEquivalentDGU01VisualAssetWithPreTargetEquivalence_V1`: alternate asset identity, custody/locator/checksum, and a pre-target equivalence proof to the UCSD DGU01 windows before any target physics is used. |

The most direct test is to ask UCSD/department archives or the event host for
an official recording, slide deck, or still/frame locator. If that fails or is
not available, the next controlled route is a lawful public-viewport capture
route against `fBozSSLxFvI` with checksummed outputs.

## 6. Meaning For DGU Visual-Row/Same-Operator Claims

Allowed statement:

```text
The repo has official UCSD event metadata, a public video locator, and local
transcript windows for the UCSD DGU01 search. It does not have a branch-pure
source asset seed.
```

Not allowed:

```text
The repo has an official UCSD DGU01 still/frame seed.
The repo has a lawful-local UCSD DGU01 video/source-byte seed.
The repo has an alternate-equivalent DGU01 seed.
The branch-pure producer may rerun positively now.
UCSD DGU01 visual rows may be retried now.
DGU01 same-operator equality may be retried now.
Downstream DGU/VZ/RS/K3/exact-GR/theta success supplies source evidence.
```

The DGU visual-row and same-operator route remains source-blocked at seed
level. This packet changes no claim status.

## 7. Next Meaningful Acquisition/Proof Step

Do not run a frame retry or same-operator retry next. Run one acquisition gate:

```text
DGU01LawfulSourceAcquisitionRouteOrOfficialFrameLocator_V1
  -> BranchPureUCSDDGU01SourceAssetSeed_V1
  -> OfficialOrLawfulUCSDDGU01FrameSourceAssetProducer_V1
```

The next worker should choose one branch before collecting fields. The
recommended order is:

1. Test the official branch: look for or request a UCSD-hosted event recording,
   official slide/still URL, or frame locator for the April 28, 2025 seminar.
2. If no official visual locator is available, test the lawful-local branch:
   construct a lawful public-viewport capture route for the two DGU windows of
   `fBozSSLxFvI`, without downloading large media.
3. Use the alternate-equivalent branch only if a pre-target equivalence proof
   can be written before any DGU/VZ/RS/K3/exact-GR/theta success is considered.

## 8. Terrain Classification

Terrain:

```text
primary: provenance-verifier/source-acquisition
secondary: public-locator triage
blocked downstream: visual-row extraction, same-operator equality,
  actual DGU operator identity, VZ, RS, K3, exact-GR, theta
```

Forbidden shortcut:

```text
Do not treat UCSD event metadata, transcript timestamps, YouTube watch URLs,
Portal/Portal Wiki metadata, promotional thumbnails, reachable oEmbed status,
prior locator-only ledgers, or downstream target success as a UCSD DGU01
source-asset seed.
```

First invariant:

```text
A valid seed must select exactly one branch and satisfy that branch's minimum
source object fields before producer_positive_rerun_allowed,
frame_retry_allowed, or same_operator_retry_allowed can become true.
```

Kill condition:

```text
If the current scope lacks an official UCSD still/frame locator, a lawful-local
video/source-byte object with checksum, and an alternate-equivalent asset with
pre-target equivalence to UCSD DGU01 windows, then the acquisition packet must
emit a negative receipt and keep all retry flags false.
```

## 9. Certificate/Witness Shape

Positive seed certificate:

| field | required content |
|---|---|
| public inputs | packet ID, run ID, selected branch, source URLs or local paths, transcript windows, acquisition scope, no-target-import declaration. |
| witness | For official branch: UCSD official visual locator or immutable ID. For lawful-local branch: local source/capture paths, lawful basis, commands, versions, SHA-256 values. For alternate branch: alternate asset identity plus custody/checksum/locator and pre-target equivalence proof. |
| verifier predicate | Exactly one branch selected; all selected-branch fields complete; no fields borrowed from unselected branches; checksum or official immutability present where applicable; transcript-window tie present. |
| semantic lift | A valid seed authorizes only the branch-pure producer rerun. It does not prove visual payload, sector row, actual operator identity, same-operator equality, VZ safety, RS quotient, K3/family count, exact GR, or theta recovery. |
| anti-smuggling guard | Reject if any required source field comes from typed `D_roll`, downstream physics success, manuscript/Oxford adjacency without equivalence, desired same-operator result, or target-generation count. |

Negative acquisition receipt emitted here:

```text
receipt_id: NegativeExternalUCSDDGU01BranchPureSourceAssetSeedAcquisitionReceipt_V1
predicate_id: ExternalUCSDDGU01BranchPureSourceAssetSeedAcquisitionPacket_V1
run_id: hourly-20260626-1102
cycle: 1
lane: 1
scope: repo-local assigned sources plus lightweight public lookup, no large media download
official_event_metadata_present: true
public_video_locator_present: true
promotional_thumbnail_locator_present: true
official_still_seed_present: false
lawful_local_video_seed_present: false
alternate_equivalent_seed_present: false
first_failed_atom: selected_branch.minimum_branch_source_object_absent_for_all_accepted_branches
producer_positive_rerun_allowed: false
frame_retry_allowed: false
same_operator_retry_allowed: false
target_import_used: false
claim_status_change: false
```

## 10. JSON Summary

```json
{
  "artifact_id": "ExternalUCSDDGU01BranchPureSourceAssetSeedAcquisitionPacket_1102_C1_L1_V1",
  "run_id": "hourly-20260626-1102",
  "cycle": 1,
  "lane": 1,
  "artifact_path": "explorations/hourly-20260626-1102-cycle1-dgu-external-seed-acquisition-packet.md",
  "object_tested": "ExternalUCSDDGU01BranchPureSourceAssetSeedAcquisitionPacket_V1",
  "verdict_class": "closed_scoped_negative_no_branch_pure_external_seed_present",
  "seed_attempted": true,
  "branch_pure_seed_present": false,
  "official_still_seed_present": false,
  "lawful_local_video_seed_present": false,
  "alternate_equivalent_seed_present": false,
  "producer_positive_rerun_allowed": false,
  "frame_retry_allowed": false,
  "same_operator_retry_allowed": false,
  "target_import_used": false,
  "claim_status_change": false,
  "public_web_search_used": true,
  "large_media_downloaded": false,
  "official_event_metadata_present": true,
  "public_video_locator_present": true,
  "promotional_thumbnail_locator_present": true,
  "first_exact_obstruction": "ExternalUCSDDGU01BranchPureSourceAssetSeedAcquisitionPacket_V1.selected_branch.minimum_branch_source_object_absent_for_all_accepted_branches",
  "first_failed_atoms_by_branch": {
    "official_still_seed": "official_ucsd_still_or_frame_locator_or_immutable_id_absent",
    "lawful_local_video_seed": "repo_local_video_or_source_byte_path_with_sha256_absent",
    "alternate_equivalent_seed": "pre_target_equivalence_to_ucsd_dgu01_windows_absent"
  },
  "constructive_next_object": "DGU01LawfulSourceAcquisitionRouteOrOfficialFrameLocator_V1",
  "negative_receipt_id": "NegativeExternalUCSDDGU01BranchPureSourceAssetSeedAcquisitionReceipt_V1",
  "producer_id": "OfficialOrLawfulUCSDDGU01FrameSourceAssetProducer_V1",
  "source_urls_checked": [
    {
      "url": "https://astro.ucsd.edu/events/index.html",
      "classification": "official_ucsd_metadata_only",
      "accepted_as_seed": false
    },
    {
      "url": "https://www.youtube.com/watch?v=fBozSSLxFvI",
      "classification": "public_youtube_locator_metadata_only",
      "accepted_as_seed": false
    },
    {
      "url": "https://www.youtube.com/watch?v=fBozSSLxFvI&t=1966s",
      "classification": "public_youtube_timestamp_locator_metadata_only",
      "accepted_as_seed": false
    },
    {
      "url": "https://www.youtube.com/watch?v=fBozSSLxFvI&t=2956s",
      "classification": "public_youtube_timestamp_locator_metadata_only",
      "accepted_as_seed": false
    },
    {
      "url": "https://theportal.wiki/wiki/From_Dark_to_Geometric_Energy_-_A_Sector_of_Geometric_Unity_%28YouTube_Content%29",
      "classification": "secondary_metadata_only",
      "accepted_as_seed": false
    },
    {
      "url": "https://theportal.group/from-dark-to-geometric-energy-a-sector-of-geometric-unity/",
      "classification": "portal_group_metadata_thumbnail_page",
      "accepted_as_seed": false
    },
    {
      "url": "https://theportal.group/wp-content/uploads/2025/05/20250522-Brian-Keating-UCSD-lecture-fBozSSLxFvI.jpg",
      "classification": "promotional_thumbnail_not_ucsd_official_frame",
      "accepted_as_seed": false
    },
    {
      "url": "https://theportal.wiki/images/f/f0/20250522-Brian-Keating-UCSD-lecture-%28fBozSSLxFvI%29.jpg",
      "classification": "secondary_thumbnail_not_ucsd_official_frame",
      "accepted_as_seed": false
    }
  ],
  "terrain": {
    "primary": "provenance-verifier/source-acquisition",
    "secondary": "public-locator triage",
    "forbidden_shortcut": "event_metadata_transcript_timestamps_youtube_urls_portal_metadata_promotional_thumbnails_reachable_oembed_or_downstream_success_as_seed",
    "first_invariant": "exactly_one_branch_with_branch_local_minimum_source_object_fields_before_any_positive_rerun_or_retry_flag",
    "kill_condition": "no_official_frame_no_lawful_local_source_bytes_no_alternate_equivalent_pre_target_proof"
  }
}
```
