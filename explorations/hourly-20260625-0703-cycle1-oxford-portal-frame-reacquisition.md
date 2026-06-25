---
title: "Hourly 20260625 0703 Cycle 1 Oxford Portal Frame Reacquisition"
date: "2026-06-25"
run_id: "hourly-20260625-0703"
cycle: 1
lane: 1
doc_type: oxford_portal_frame_reacquisition
artifact_id: "OxfordPortalPowerPointFormulaFrameReacquisition_V1"
verdict: "CONDITIONAL_EXECUTED_SOURCE_HOSTED_FRAME_PACKET_ZERO_ACCEPTED_ROUTING_RECEIPTS"
owned_path: "explorations/hourly-20260625-0703-cycle1-oxford-portal-frame-reacquisition.md"
companion_audit: "tests/hourly_20260625_0703_cycle1_oxford_portal_frame_reacquisition_audit.py"
---

# Hourly 20260625 0703 Cycle 1 Oxford Portal Frame Reacquisition

## 1. Verdict

Verdict: **conditional**.

`OxfordPortalPowerPointFormulaFramePacket_V1` has been partially executed as a
source-hosted frame reacquisition packet. The official Oxford page was fetched
live on 2026-06-25, and the embedded stills around the five required anchors
were located, fetched, checksummed, and visually inspected from a temporary
working directory outside the repo.

This is enough to open `VisualFormulaReceiptCandidatePacket_V1` rows as
candidate rows. It is not enough to accept any row for routing.

Decision state:

```text
artifact_id: OxfordPortalPowerPointFormulaFrameReacquisition_V1
accepted_receipt_count: 0
accepted_for_routing_count: 0
proof_restart_allowed: false
first_obstruction: displayed formulas exist, but no row yet supplies the required family object plus identity check for DGU_VZ, RS, or IG
```

The positive change is real: the prior packet was an acquisition spec with no
executed frame evidence. This packet records official hosted frame URLs,
SHA-256 checksums, and source-preserving transcriptions. The limiting condition
is also real: the repo still lacks a family identity proof from any displayed
object to `operator_source_primary_action_or_EL for D_GU^epsilon 0/1`,
`source.action_or_operator for d_RS,-1`, or
`SourceForcedCodomainSelectorForK_IG`.

## 2. Specific GU Claim/Bridge Under Test

Bridge under test:

```text
official Oxford/Portal displayed PowerPoint formulas
  -> VisualFormulaReceiptCandidatePacket_V1 rows
  -> accepted source/formula receipt rows for DGU_VZ, RS, or IG
  -> family-limited proof restart reconsideration
```

The strongest target bridge is the DGU/VZ bridge:

```text
Gauge invariant bosonic Einstein replacement on Y
  -> actual source primary action/operator/EL object for D_GU^epsilon 0/1
```

The executed frames support the left side as a source-displayed formula
surface. They do not supply the right side. In particular, the displayed
bosonic equation is not identified in this artifact with an actual
`D_GU^epsilon` 0/1 action, operator, Euler-Lagrange equation, principal symbol,
or coefficient packet.

## 3. Owned Output Path and Sources Read First

Owned output path:

```text
explorations/hourly-20260625-0703-cycle1-oxford-portal-frame-reacquisition.md
```

Companion audit:

```text
tests/hourly_20260625_0703_cycle1_oxford_portal_frame_reacquisition_audit.py
```

Required sources read first:

- `RESEARCH-POSTURE.md`
- `process/runbooks/five-lane-frontier-run.md`
- `explorations/hourly-20260625-0601-cycle3-next-frontier-object-dependency-dag.md`
- `explorations/hourly-20260625-0601-cycle3-visual-acquisition-sequencing-gate.md`
- `explorations/hourly-20260625-0502-cycle1-oxford-portal-exact-source-locator-execution.md`
- `explorations/hourly-20260625-0203-cycle1-oxford-portal-receipt-mining-packet.md`
- `sources/media-index.md`

Additional repo-local context read:

- `explorations/hourly-20260625-0601-cycle1-oxford-portal-formula-frame-packet-spec.md`
- `explorations/hourly-20260625-0502-cycle3-visual-formula-acquisition-dependency-gate.md`

Live/source access actually used:

- `https://geometricunity.org/2013-oxford-lecture/` fetched successfully.
- `https://theportal.group/a-portal-special-presentation-geometric-unity-a-first-look/` fetched successfully.
- `https://geometricunity.org/` fetched successfully as the official release
  landing page.

No YouTube video frames were downloaded. `yt-dlp` and `ffmpeg` were not
available in the local command path checked for this run. The execution used
the official pages' embedded still images, not a fresh video-frame extraction.

## 4. Strongest Positive Construction Attempt

The strongest positive construction is a five-anchor candidate packet whose
rows now have official source-hosted frame URLs, checksums, and displayed
formula transcriptions.

| anchor | official hosted frame used | sha256 | displayed source content | candidate impact | routing decision |
| --- | --- | --- | --- | --- | --- |
| `02:33:43` | `https://geometricunity.org/wp-content/uploads/2021/03/vlcsnap-2021-03-08-12h08m05s3871.png` | `sha256:21bb2f7ef3a6a22db7a9650afc1aca8597e66af2c94e48e621da077ba8cdc1b0` | Example of a Shiab operator: `\odot_g \mu_1 = [Ad(e^{-1}, \Phi_3)^\wedge, \mu_1]` with uncertainty only in the precise typography of the left circled operator and hat placement. | IG adjacency; possible DGU/VZ precondition. | Not accepted. No displayed domain/codomain, selector rule, or rival eliminator for `K_IG`. |
| `02:35:10` | `https://geometricunity.org/wp-content/uploads/2021/03/vlcsnap-2021-03-08-12h09m15s4661.png` | `sha256:60b4041ca6dcdfbe002c9ec9a5cd7f57cd31cafd612813e6c12845b4677c340b` | Gauge invariant bosonic Einstein replacement on `Y`: `\odot F_\omega + E(T_\omega,\odot) = -* T_\omega`, with labels "Swerved Curvature", "Quadratic Eddy = E_\omega", "Offset Torsion", and "Displasion = J_\omega"; total swervature labelled `S_\omega`. | Strongest DGU/VZ visual candidate. | Not accepted. It is a bosonic replacement equation, not an identified actual `D_GU^epsilon` 0/1 action/operator/EL object. |
| `02:36:12` | `https://geometricunity.org/wp-content/uploads/2021/03/vlcsnap-2021-03-08-12h10m30s7951.png` | `sha256:50d76531c2112fa25338069ef620b067bb865d9044c939d6bd688df9257a0731` | Condensed current equation: `S_\omega = J_\omega`, introduced by the slide text "The Swervature equals the Displasion." | DGU/VZ visual candidate. | Not accepted. It is a schematic or condensed displayed equation without the family identity data needed for `D_GU^epsilon` 0/1. |
| `02:38:53` | `https://geometricunity.org/wp-content/uploads/2021/03/vlcsnap-2021-03-08-12h11m11s1871.png` | `sha256:4db0982b7d664bdeaaf2b98f8011240fbbce98b8fd13126723f8b72395462f41` | `Y`-fermions under pullback to `X`: `(2.14) V \otimes S_V = S_V \oplus R_V`; `(2.15) S_V = S_{X \oplus Y} = S_X \otimes S_Y`; `(2.16) R_V = R_{X \oplus Y} = (R_X \otimes S_Y) \oplus (S_X \otimes R_Y) \oplus (S_X \otimes S_Y)`. | RS/generation visual candidate. | Not accepted. It displays a representation decomposition, not a source action/operator/differential/Noether/BRST rule for `d_RS,-1`. |
| `02:40:19` | `https://geometricunity.org/wp-content/uploads/2021/03/vlcsnap-2021-03-08-12h13m36s3901.png` | `sha256:88e99e732418dfb2a52544cd5bc41198f2e809b54795a91260c357cd959468a8` | Summary slide states that the Einsteinian replacement must be pulled back to `X`, Yang-Mills/Maxwell comes from a Dirac square, the Dirac piece contains R-S field content, there are only two generations, the quartic Higgs piece comes from Dirac squaring of a quadratic, the metric acts as field and observer pullback, and Pati-Salam is naturally `Spin(6) x Spin(4)` on the normal bundle under the stated signature condition. | DGU/VZ and RS adjacency; generation and gauge-structure locator. | Not accepted. It is summary prose, not a displayed family formula with identity to the required objects. |

This is the strongest positive result because it changes the artifact from
"capture these five frames" to "these five source-hosted frames were located,
fetched, hashed, and transcribed at candidate-row granularity."

## 5. First Exact Obstruction or Missing Proof/Source Object

The first exact obstruction is:

```text
No captured/transcribed Oxford/Portal frame supplies both a required family object
and a family identity check.
```

Per family:

- DGU/VZ: the `02:35:10` and `02:36:12` frames display bosonic replacement
  equations, but this artifact does not identify them with an actual
  `D_GU^epsilon` 0/1 action, operator, Euler-Lagrange object, principal symbol,
  coefficient packet, or source certificate.
- RS: the `02:38:53` frame displays Rarita-Schwinger-adjacent spinor
  decompositions, but no RS action, differential, gauge rule, Noether identity,
  or BRST rule for `d_RS,-1`.
- IG: the `02:33:43` frame displays one Shiab operator formula, but no
  source-forced codomain selector, no domain/codomain row, and no
  representation-theory/Bianchi rival eliminator for `K_IG`.
- QFT: none of the five frames displays a finite projector
  `P_fin^b: F_phys^b(O) -> K_b`.

There is also a preservation limitation: this run did not add repo-local image
files or archive IDs. It records official hosted URLs and live-computed SHA-256
checksums. If the integration standard requires repo-local image possession,
that remains a separate acquisition step.

## 6. What Would Change If the Hole Closed

If the family-identity hole closed for one row:

- DGU/VZ could move from a source-hosted visual candidate to an accepted
  receipt candidate for the bosonic sector, followed by a separate test of
  whether and how that sector maps to actual `D_GU^epsilon` 0/1.
- RS could move from representation-decomposition adjacency to source-emitted
  operator/differential routing only if a displayed or nearby frame supplies an
  actual RS action/operator/differential rule.
- IG could move from Shiab vocabulary/formula adjacency to selector identity
  work only if the Shiab operator is accompanied by a source-forced codomain
  selector or a rival-eliminating rule.

Even then, proof restart would not be automatic. The next state would be
family identity review, then proof-restart readiness classification.

## 7. What Would Falsify or Demote the Route

Demote the Oxford/Portal frame route for these five anchors if an integration
review agrees that:

```text
the official hosted frames and checksums are adequate,
the transcriptions above are source-preserving,
the target-import guard is clean,
and none of the frames emits the required DGU_VZ, RS, IG, or QFT family object.
```

That demotion would be scoped. It would demote these frames to
terminology/provenance/adjacency evidence, not a global no-go for GU or for
other source surfaces.

Falsify this conditional positive route more sharply if the official hosted
stills are shown to be non-official, mismatched to the timestamps, altered, or
not stable enough to serve as source objects. In that case, this packet falls
back to the earlier acquisition-spec state and must be replaced by a video-frame
extraction or archive-backed source object.

## 8. Next Meaningful Computation or Proof/Source Step

Next source step:

```text
Promote these five rows into a formal VisualFormulaReceiptCandidatePacket_V1
ledger, preserving source URLs, checksums, timestamp anchors, transcriptions,
uncertainty fields, and accepted_for_routing=false.
```

Next mathematical step:

```text
Build BosonicOxfordReplacementToDGU01IdentityTest_V1.
```

That test should decide whether the displayed bosonic replacement equation can
be typed as, or bridged to, the actual `D_GU^epsilon` 0/1 object without target
import. Until that bridge exists, downstream VZ or DGU proof replay remains
forbidden.

## 9. JSON Summary

```json
{
  "artifact": "OxfordPortalPowerPointFormulaFrameReacquisition_V1",
  "run_id": "hourly-20260625-0703",
  "cycle": 1,
  "lane": 1,
  "artifact_id": "OxfordPortalPowerPointFormulaFrameReacquisition_V1",
  "verdict": "conditional",
  "verdict_code": "CONDITIONAL_EXECUTED_SOURCE_HOSTED_FRAME_PACKET_ZERO_ACCEPTED_ROUTING_RECEIPTS",
  "accepted_receipt_count": 0,
  "accepted_for_routing_count": 0,
  "proof_restart_allowed": false,
  "claim_promotion_allowed": false,
  "candidate_rows_opened": true,
  "candidate_packet_id": "VisualFormulaReceiptCandidatePacket_V1",
  "owned_path": "explorations/hourly-20260625-0703-cycle1-oxford-portal-frame-reacquisition.md",
  "companion_audit": "tests/hourly_20260625_0703_cycle1_oxford_portal_frame_reacquisition_audit.py",
  "sources_read_first": [
    "RESEARCH-POSTURE.md",
    "process/runbooks/five-lane-frontier-run.md",
    "explorations/hourly-20260625-0601-cycle3-next-frontier-object-dependency-dag.md",
    "explorations/hourly-20260625-0601-cycle3-visual-acquisition-sequencing-gate.md",
    "explorations/hourly-20260625-0502-cycle1-oxford-portal-exact-source-locator-execution.md",
    "explorations/hourly-20260625-0203-cycle1-oxford-portal-receipt-mining-packet.md",
    "sources/media-index.md"
  ],
  "live_sources_fetched": [
    {
      "url": "https://geometricunity.org/2013-oxford-lecture/",
      "status": "fetched_200",
      "role": "official Oxford transcript page with embedded frame stills"
    },
    {
      "url": "https://theportal.group/a-portal-special-presentation-geometric-unity-a-first-look/",
      "status": "fetched_200",
      "role": "Portal Group transcript mirror with parallel embedded stills"
    },
    {
      "url": "https://geometricunity.org/",
      "status": "fetched_200",
      "role": "official GU release landing page"
    }
  ],
  "anchors": [
    {
      "timestamp": "02:33:43",
      "anchor_id": "OxfordPortal_PPT_023343_ShiabOperator",
      "frame_url": "https://geometricunity.org/wp-content/uploads/2021/03/vlcsnap-2021-03-08-12h08m05s3871.png",
      "checksum_or_archive_id": "sha256:21bb2f7ef3a6a22db7a9650afc1aca8597e66af2c94e48e621da077ba8cdc1b0",
      "transcription": "\\odot_g \\mu_1 = [Ad(e^{-1}, \\Phi_3)^\\wedge, \\mu_1]",
      "transcription_uncertainty": ["precise typography of circled operator", "hat placement"],
      "family_candidates": ["IG", "DGU_VZ_precondition"],
      "required_family_object_emitted": false,
      "accepted_for_routing": false
    },
    {
      "timestamp": "02:35:10",
      "anchor_id": "OxfordPortal_PPT_023510_Swervature",
      "frame_url": "https://geometricunity.org/wp-content/uploads/2021/03/vlcsnap-2021-03-08-12h09m15s4661.png",
      "checksum_or_archive_id": "sha256:60b4041ca6dcdfbe002c9ec9a5cd7f57cd31cafd612813e6c12845b4677c340b",
      "transcription": "\\odot F_\\omega + E(T_\\omega, \\odot) = -* T_\\omega; total swervature S_\\omega; displasion J_\\omega",
      "transcription_uncertainty": ["whether slide label J_omega is calligraphic J", "whether equation is schematic replacement or typed field equation"],
      "family_candidates": ["DGU_VZ"],
      "required_family_object_emitted": false,
      "accepted_for_routing": false
    },
    {
      "timestamp": "02:36:12",
      "anchor_id": "OxfordPortal_PPT_023612_Displasion",
      "frame_url": "https://geometricunity.org/wp-content/uploads/2021/03/vlcsnap-2021-03-08-12h10m30s7951.png",
      "checksum_or_archive_id": "sha256:50d76531c2112fa25338069ef620b067bb865d9044c939d6bd688df9257a0731",
      "transcription": "S_\\omega = J_\\omega",
      "transcription_uncertainty": ["whether J is calligraphic", "family identity to D_GU_epsilon_0_1 absent"],
      "family_candidates": ["DGU_VZ"],
      "required_family_object_emitted": false,
      "accepted_for_routing": false
    },
    {
      "timestamp": "02:38:53",
      "anchor_id": "OxfordPortal_PPT_023853_RSDiracAdjacency",
      "frame_url": "https://geometricunity.org/wp-content/uploads/2021/03/vlcsnap-2021-03-08-12h11m11s1871.png",
      "checksum_or_archive_id": "sha256:4db0982b7d664bdeaaf2b98f8011240fbbce98b8fd13126723f8b72395462f41",
      "transcription": "(2.14) V \\otimes S_V = S_V \\oplus R_V; (2.15) S_V = S_{X \\oplus Y} = S_X \\otimes S_Y; (2.16) R_V = R_{X \\oplus Y} = (R_X \\otimes S_Y) \\oplus (S_X \\otimes R_Y) \\oplus (S_X \\otimes S_Y)",
      "transcription_uncertainty": ["font makes R/S distinction visually delicate but context labels Rarita-Schwinger content"],
      "family_candidates": ["RS", "generation_structure"],
      "required_family_object_emitted": false,
      "accepted_for_routing": false
    },
    {
      "timestamp": "02:40:19",
      "anchor_id": "OxfordPortal_PPT_024019_PullbackToX",
      "frame_url": "https://geometricunity.org/wp-content/uploads/2021/03/vlcsnap-2021-03-08-12h13m36s3901.png",
      "checksum_or_archive_id": "sha256:88e99e732418dfb2a52544cd5bc41198f2e809b54795a91260c357cd959468a8",
      "transcription": "summary prose: Einsteinian replacement piece must be pulled back to X; Yang-Mills Maxwell piece comes from a Dirac square; Dirac piece contains R-S field content; two generations; quartic Higgs from Dirac squaring; metric as field and observer pullback; Pati-Salam naturally Spin(6) x Spin(4) on normal bundle under signature 1,3",
      "transcription_uncertainty": ["prose summary, not formula row"],
      "family_candidates": ["DGU_VZ", "RS", "generation_structure"],
      "required_family_object_emitted": false,
      "accepted_for_routing": false
    }
  ],
  "first_obstruction": "Displayed formulas exist, but no row supplies the required family object plus family identity check for DGU_VZ, RS, IG, or QFT.",
  "next_frontier_object": "BosonicOxfordReplacementToDGU01IdentityTest_V1",
  "proof_restart_allowed_reason": "No accepted receipt and no family identity check passed.",
  "repo_local_frame_files_added": false,
  "source_hosted_checksums_recorded": true
}
```
