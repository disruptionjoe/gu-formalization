---
title: "Hourly 20260625 0711 Cycle 3 Receipt Transition Matrix"
status: draft
doc_type: exploration
run_id: "hourly-20260625-0711"
cycle: 3
lane: 2
artifact_id: "ReceiptTransitionMatrixAfter0711_V1"
verdict: "ZERO_TRANSITIONS_TO_ACCEPTED_ROUTING_OR_PROOF_RESTART"
---

# Hourly 20260625 0711 Cycle 3 Receipt Transition Matrix

## 1. Verdict

Verdict: **blocked; zero cycle 1-2 candidate rows transition to
`accepted_for_routing` or `proof_restart_ready`**.

The 0711 cycle 1-2 artifacts improved source location, frame verification, and
cell/spec typing, but they did not produce the missing source-clean identity
objects required for routing. The strongest positive rows remain candidates:
verified Oxford frames, source-hosted or manuscript-hosted formula surfaces,
caption/metadata locators, scoped RS negatives, and one underdefined finite
local QFT extraction specification.

No candidate transitions to accepted routing because every route fails before
the admission gate:

```text
accepted_for_routing requires accepted_receipt_count > 0
and route-specific family identity / selector / operation status passed.
```

In the cycle 1-2 artifacts, all accepted counts are zero and all proof-restart
flags are false.

## 2. What was derived from cycle 1-2 artifacts

This matrix is derived from:

- `hourly-20260625-0711-cycle1-oxford-portal-frame-capture-execution.md`:
  five official Oxford/Portal PNG frame anchors were reachable, checksum
  matched prior source-hosted rows, and remained candidate-only.
- `hourly-20260625-0711-cycle2-oxford-frame-dgu-vz-family-identity-test.md`:
  the `02:35:10` and `02:36:12` Oxford DGU/VZ anchors were tested against a
  DGU 0/1 family-identity gate and remained blocked.
- `hourly-20260625-0711-cycle1-keating-ptuj-shiab-asset-execution.md` and
  `hourly-20260625-0711-cycle2-ptuj-frame-capture-feasibility-gate.md`:
  PTUJ/Keating surfaces were reachable only as captions, oEmbed/thumbnail
  metadata, transcript locators, or adjacent manuscript candidates; no
  formula-bearing frame/source-asset packet was captured.
- `hourly-20260625-0711-cycle1-ig-rival-eliminator-source-identity.md` and
  `hourly-20260625-0711-cycle2-ig-visual-manuscript-selector-bridge.md`:
  IG Shiab candidates were triangulated across manuscript, Oxford, and
  PTUJ/Keating locators, but no source-forced selector or rival eliminator was
  emitted.
- `hourly-20260625-0711-cycle1-dgu-bosonic-to-01-identity-rule-search.md`:
  six manuscript bosonic/adjacent objects were located, but none supplied a
  source-clean identity rule to actual `D_GU^epsilon` 0/1 data.
- `hourly-20260625-0711-cycle1-rs-manual-image-formula-diagram-audit.md` and
  `hourly-20260625-0711-cycle2-rs-equation-1010-cell-typing-gate.md`:
  equation 10.10 remained a scoped RS fail; image-level and cell-level passes
  found mixed `/S`/`ad`/operator-like material, not a pure RS minus-one rule.
- `hourly-20260625-0711-cycle2-qft-finite-local-extraction-spec-gate.md`:
  a finite local extraction map was attempted but remained underdefined before
  any matrix, state, or Bell/QFT computation.

Counting policy: a row below is a normalized route-candidate row. Repeated
cycle checks of the same PTUJ/Oxford surface are folded unless the later cycle
adds a different route test. The Oxford `02:33:43` visual surface appears once
as an Oxford anchor row and once as an IG bridge row because those are different
route gates.

## 3. Transition matrix/table

| route | normalized candidate rows | route-specific status after 0711 cycle 1-2 | accepted_for_routing | proof_restart_ready | decisive route status |
|---|---:|---|---:|---:|---|
| Oxford anchors | 5 | 3 `verified_frame_candidate`; 2 `blocked_identity` | 0 | 0 | frames verified, identity missing |
| PTUJ / Keating | 4 | 3 `caption_metadata_only`; 1 `hosted_candidate` | 0 | 0 | no formula-bearing frame/source-asset packet |
| IG bridge / rival eliminator | 10 | 1 `verified_frame_candidate`; 1 `caption_metadata_only`; 8 `hosted_candidate` | 0 | 0 | no source-forced selector/rival eliminator |
| DGU bosonic-to-0/1 | 6 | 6 `blocked_identity` | 0 | 0 | no bosonic-to-actual-DGU-0/1 identity rule |
| RS equation 10.10 | 13 | 13 `scoped_fail` | 0 | 0 | no pure RS minus-one source rule |
| QFT finite local extraction | 1 | 1 `underdefined_spec` | 0 | 0 | missing finite local extraction operation |
| **Total** | **39** | see status counts below | **0** | **0** | no transition closed |

Status counts:

| status | count |
|---|---:|
| `verified_frame_candidate` | 4 |
| `caption_metadata_only` | 4 |
| `hosted_candidate` | 9 |
| `blocked_identity` | 8 |
| `scoped_fail` | 13 |
| `underdefined_spec` | 1 |
| `accepted_for_routing` | 0 |
| `proof_restart_ready` | 0 |

Route-specific notes:

- Oxford anchors: `02:33:43`, `02:38:53`, and `02:40:19` remain verified frame
  candidates only. `02:35:10` and `02:36:12` were additionally tested as
  DGU/VZ candidates and blocked on family identity.
- PTUJ: the official page, YouTube/oEmbed/thumbnail surface, and Keating
  transcript window remain caption/metadata/locator-only rows. The author
  manuscript pages 41-44 row is a hosted adjacent candidate, not an accepted
  PTUJ frame receipt.
- IG bridge: manuscript and Oxford surfaces host plausible Shiab/projection
  candidates, and PTUJ/Keating gives a locator, but the selector and rival
  eliminator are missing.
- DGU: six manuscript objects are useful locators, but every row is blocked
  before actual `D_GU^epsilon` 0/1 domain/codomain/action/operator data.
- RS: the image-level row and twelve equation-10.10 cell rows fail locally for
  RS minus-one routing.
- QFT: the finite local extraction route is not yet a valid reconstruction
  spec because `P_fin^b: F_phys^b(O) -> K_b` is not source-defined.

## 4. First exact obstruction to transition

The first exact obstruction is not image reachability or a lack of candidate
surfaces. It is the missing route-specific admission object:

```text
Source-clean family identity / selector / extraction operation sufficient to
turn a hosted or verified surface into an accepted receipt.
```

By route:

| route | first exact obstruction |
|---|---|
| Oxford anchors | `FamilyIdentityForVerifiedOxfordPortalFrames_V1`; for DGU/VZ anchors, source-clean identity to actual `D_GU^epsilon` 0/1 data |
| PTUJ / Keating | `LawfulLocalTzSEvmqxu48FrameExtractorOrSourceAsset_V1` plus a formula-bearing frame/source-asset packet and equivalence to the IG selector |
| IG bridge | `CombinedSourceRepresentationTheoryBianchiRivalEliminatorForK_IG_V1` |
| DGU | `BosonicToDGU01SectorIdentityRule_V1` |
| RS | pure RS source action/operator rule for `d_RS,-1` with source, target, degree/slot, rule kind, and family identity |
| QFT | `SourceDefinedFiniteLocalExtractionOperation_V1` |

This obstruction occurs before any proof restart. It also occurs before
downstream physics claims such as generation counts, theta/FLRW routing, local
mode matrices, positivity, covariance, `rho_AB`, CHSH, or Bell violation.

## 5. Impact if any transition closes

If one row transitions to `accepted_for_routing`, the effect is route-local but
important:

- Oxford/DGU closure would permit a DGU/VZ proof branch to restart from actual
  source-clean 0/1 data rather than from visually compatible bosonic frames.
- PTUJ/IG closure would upgrade the Shiab/projection surfaces from hosted or
  caption-only evidence to a candidate source-forced codomain selector for
  `K_IG`.
- RS closure would replace a scoped negative result with a runnable RS
  generation-count route.
- QFT closure would create the first legitimate finite local extraction
  computation input; only then could matrix/state/QFT recovery tests begin.

None of those impacts is currently available, because no row has crossed the
accepted-routing gate.

## 6. Falsification/demotion condition

Demote a route-specific candidate class if a complete lawful source pass
continues to satisfy the current negative condition:

- Oxford/DGU: no source-emitted DGU 0/1 sector identity, actual operator/action
  formula, domain/codomain, coefficient packet, projector policy, and family
  identity.
- PTUJ: all lawful frame/source-asset extraction attempts remain caption,
  oEmbed, thumbnail, transcript, or adjacent manuscript only.
- IG: no source-emitted representation-theory/Bianchi selector, rival
  eliminators, or family identity to `SourceForcedCodomainSelectorForK_IG`.
- RS: cell-by-cell equation 10.10 typing continues to find only mixed `/S`,
  `ad`, or underdefined operator-like labels and no pure RS minus-one rule.
- QFT: no source-defined `F_phys^b(O)`, extraction/projector/quotient rule,
  `K_b` codomain, naturality proof, or finite-stability test can be supplied
  without target import.

These are scoped demotions, not global GU no-go claims.

## 7. Next computation/classifier step

Build a small receipt classifier with this order:

1. `source_surface_kind`: frame, caption/oEmbed/thumbnail, transcript locator,
   manuscript formula, manuscript diagram cell, or spec attempt.
2. `formula_or_rule_transcribed`: true only when an actual formula/rule is
   transcribed, not merely named by a caption.
3. `family_identity_status`: passed, blocked, failed, or not runnable.
4. `route_required_object`: selector, identity rule, RS operator, or finite
   local extraction operation.
5. `transition_allowed`: true only if accepted receipt count is positive and
   the route-required object is source-clean and passed.

The immediate classifier target is:

```text
RouteCandidateReceiptClassifier0711_V1
input: normalized candidate rows in this artifact
output: accepted_for_routing candidates, demotions, and exact missing object
```

## 8. Machine-readable JSON summary

```json
{
  "artifact": "ReceiptTransitionMatrixAfter0711_V1",
  "run_id": "hourly-20260625-0711",
  "cycle": 3,
  "lane": 2,
  "source_cycles": [1, 2],
  "verdict": "ZERO_TRANSITIONS_TO_ACCEPTED_ROUTING_OR_PROOF_RESTART",
  "verdict_class": "blocked",
  "row_count": 39,
  "status_counts": {
    "verified_frame_candidate": 4,
    "caption_metadata_only": 4,
    "hosted_candidate": 9,
    "blocked_identity": 8,
    "scoped_fail": 13,
    "underdefined_spec": 1,
    "accepted_for_routing": 0,
    "proof_restart_ready": 0
  },
  "route_counts": {
    "Oxford_anchors": 5,
    "PTUJ_Keating": 4,
    "IG_bridge": 10,
    "DGU": 6,
    "RS": 13,
    "QFT": 1
  },
  "transition_counts": {
    "candidate_rows_total": 39,
    "accepted_for_routing": 0,
    "proof_restart_ready": 0,
    "transitioned_to_accepted_for_routing": 0,
    "transitioned_to_proof_restart_ready": 0
  },
  "accepted_for_routing": [],
  "proof_restart_ready": [],
  "transition_decision": {
    "any_candidate_transitioned_to_accepted_for_routing": false,
    "why_not": "Every cycle 1-2 route lacks the route-specific source-clean family identity, selector, RS rule, or finite local extraction operation required to turn a candidate surface into an accepted receipt."
  },
  "route_status": {
    "Oxford_anchors": {
      "row_count": 5,
      "status_counts": {
        "verified_frame_candidate": 3,
        "blocked_identity": 2
      },
      "accepted_for_routing": 0,
      "proof_restart_ready": 0,
      "first_obstruction": "FamilyIdentityForVerifiedOxfordPortalFrames_V1, with DGU/VZ anchors blocked on identity to actual D_GU_epsilon_0_1 data"
    },
    "PTUJ_Keating": {
      "row_count": 4,
      "status_counts": {
        "caption_metadata_only": 3,
        "hosted_candidate": 1
      },
      "accepted_for_routing": 0,
      "proof_restart_ready": 0,
      "first_obstruction": "LawfulLocalTzSEvmqxu48FrameExtractorOrSourceAsset_V1 plus formula-bearing frame/source-asset packet is missing"
    },
    "IG_bridge": {
      "row_count": 10,
      "status_counts": {
        "verified_frame_candidate": 1,
        "caption_metadata_only": 1,
        "hosted_candidate": 8
      },
      "accepted_for_routing": 0,
      "proof_restart_ready": 0,
      "first_obstruction": "CombinedSourceRepresentationTheoryBianchiRivalEliminatorForK_IG_V1 is missing"
    },
    "DGU": {
      "row_count": 6,
      "status_counts": {
        "blocked_identity": 6
      },
      "accepted_for_routing": 0,
      "proof_restart_ready": 0,
      "first_obstruction": "BosonicToDGU01SectorIdentityRule_V1 is missing"
    },
    "RS": {
      "row_count": 13,
      "status_counts": {
        "scoped_fail": 13
      },
      "accepted_for_routing": 0,
      "proof_restart_ready": 0,
      "first_obstruction": "Pure RS source action/operator rule for d_RS,-1 is absent from equation 10.10"
    },
    "QFT": {
      "row_count": 1,
      "status_counts": {
        "underdefined_spec": 1
      },
      "accepted_for_routing": 0,
      "proof_restart_ready": 0,
      "first_obstruction": "SourceDefinedFiniteLocalExtractionOperation_V1 is missing"
    }
  },
  "candidate_rows": [
    {
      "row_id": "OXFORD_023343_SHIAB_OPERATOR",
      "route": "Oxford_anchors",
      "source_artifact": "hourly-20260625-0711-cycle1-oxford-portal-frame-capture-execution.md",
      "candidate": "OxfordPortal_PPT_023343_ShiabOperator",
      "status": "verified_frame_candidate",
      "accepted_for_routing": false,
      "proof_restart_ready": false,
      "reason_not_accepted": "verified frame but family identity remains blocked"
    },
    {
      "row_id": "OXFORD_023510_SWERVATURE",
      "route": "Oxford_anchors",
      "source_artifact": "hourly-20260625-0711-cycle2-oxford-frame-dgu-vz-family-identity-test.md",
      "candidate": "OxfordPortal_PPT_023510_Swervature",
      "status": "blocked_identity",
      "accepted_for_routing": false,
      "proof_restart_ready": false,
      "reason_not_accepted": "DGU/VZ family identity to actual D_GU_epsilon_0_1 data not established"
    },
    {
      "row_id": "OXFORD_023612_DISPLASION",
      "route": "Oxford_anchors",
      "source_artifact": "hourly-20260625-0711-cycle2-oxford-frame-dgu-vz-family-identity-test.md",
      "candidate": "OxfordPortal_PPT_023612_Displasion",
      "status": "blocked_identity",
      "accepted_for_routing": false,
      "proof_restart_ready": false,
      "reason_not_accepted": "DGU/VZ family identity to actual D_GU_epsilon_0_1 data not established"
    },
    {
      "row_id": "OXFORD_023853_RS_DIRAC_ADJACENCY",
      "route": "Oxford_anchors",
      "source_artifact": "hourly-20260625-0711-cycle1-oxford-portal-frame-capture-execution.md",
      "candidate": "OxfordPortal_PPT_023853_RSDiracAdjacency",
      "status": "verified_frame_candidate",
      "accepted_for_routing": false,
      "proof_restart_ready": false,
      "reason_not_accepted": "verified frame but no accepted RS/generation family object emitted"
    },
    {
      "row_id": "OXFORD_024019_PULLBACK_TO_X",
      "route": "Oxford_anchors",
      "source_artifact": "hourly-20260625-0711-cycle1-oxford-portal-frame-capture-execution.md",
      "candidate": "OxfordPortal_PPT_024019_PullbackToX",
      "status": "verified_frame_candidate",
      "accepted_for_routing": false,
      "proof_restart_ready": false,
      "reason_not_accepted": "verified prose frame, not an accepted formula/rule receipt"
    },
    {
      "row_id": "PTUJ_OFFICIAL_PAGE_EMBED",
      "route": "PTUJ_Keating",
      "source_artifact": "hourly-20260625-0711-cycle2-ptuj-frame-capture-feasibility-gate.md",
      "candidate": "PullThatUpJamie_GUForGRGaugeTheory_TzSEvmqxu48",
      "status": "caption_metadata_only",
      "accepted_for_routing": false,
      "proof_restart_ready": false,
      "reason_not_accepted": "official page exposes iframe/video id and Shiab caption, not video frames or formula text"
    },
    {
      "row_id": "PTUJ_YOUTUBE_OEMBED_THUMBNAIL",
      "route": "PTUJ_Keating",
      "source_artifact": "hourly-20260625-0711-cycle2-ptuj-frame-capture-feasibility-gate.md",
      "candidate": "YouTube_TzSEvmqxu48",
      "status": "caption_metadata_only",
      "accepted_for_routing": false,
      "proof_restart_ready": false,
      "reason_not_accepted": "oEmbed/thumbnail reachable but no formula-bearing frame extracted"
    },
    {
      "row_id": "PTUJ_KEATING_TRANSCRIPT_WINDOW",
      "route": "PTUJ_Keating",
      "source_artifact": "hourly-20260625-0711-cycle1-keating-ptuj-shiab-asset-execution.md",
      "candidate": "KeatingRevealedTranscriptWindow",
      "status": "caption_metadata_only",
      "accepted_for_routing": false,
      "proof_restart_ready": false,
      "reason_not_accepted": "transcript/window locator only; missing projection sheet"
    },
    {
      "row_id": "PTUJ_AUTHOR_MANUSCRIPT_ADJACENT",
      "route": "PTUJ_Keating",
      "source_artifact": "hourly-20260625-0711-cycle1-keating-ptuj-shiab-asset-execution.md",
      "candidate": "AuthorManuscriptPages41To44",
      "status": "hosted_candidate",
      "accepted_for_routing": false,
      "proof_restart_ready": false,
      "reason_not_accepted": "adjacent manuscript candidate not proved identical to missing PTUJ/Keating source asset"
    },
    {
      "row_id": "IG_AUTHOR_MANUSCRIPT_SHIAB",
      "route": "IG_bridge",
      "source_artifact": "hourly-20260625-0711-cycle2-ig-visual-manuscript-selector-bridge.md",
      "candidate": "AuthorManuscript2021",
      "status": "hosted_candidate",
      "accepted_for_routing": false,
      "proof_restart_ready": false,
      "reason_not_accepted": "typed Shiab candidate but selector statement missing"
    },
    {
      "row_id": "IG_OXFORD_023343_VISUAL",
      "route": "IG_bridge",
      "source_artifact": "hourly-20260625-0711-cycle2-ig-visual-manuscript-selector-bridge.md",
      "candidate": "OxfordPortal023343VerifiedFrame",
      "status": "verified_frame_candidate",
      "accepted_for_routing": false,
      "proof_restart_ready": false,
      "reason_not_accepted": "verified visual formula candidate but typography/selector identity unresolved"
    },
    {
      "row_id": "IG_KEATING_PTUJ_LOCATOR",
      "route": "IG_bridge",
      "source_artifact": "hourly-20260625-0711-cycle2-ig-visual-manuscript-selector-bridge.md",
      "candidate": "KeatingPullThatUpJamieLocator",
      "status": "caption_metadata_only",
      "accepted_for_routing": false,
      "proof_restart_ready": false,
      "reason_not_accepted": "locator for missing representation projection sheet"
    },
    {
      "row_id": "IG_CLASS_MANUSCRIPT_CODOMAIN",
      "route": "IG_bridge",
      "source_artifact": "hourly-20260625-0711-cycle1-ig-rival-eliminator-source-identity.md",
      "candidate": "ManuscriptIGShiabCodomainCandidate_Sections5_8_9_Summary_V1",
      "status": "hosted_candidate",
      "accepted_for_routing": false,
      "proof_restart_ready": false,
      "reason_not_accepted": "source-hosted candidate not selected by rival eliminator"
    },
    {
      "row_id": "IG_CLASS_DISPLAYED_SHIAB_CODOMAIN",
      "route": "IG_bridge",
      "source_artifact": "hourly-20260625-0711-cycle1-ig-rival-eliminator-source-identity.md",
      "candidate": "displayed_shiab_codomain",
      "status": "hosted_candidate",
      "accepted_for_routing": false,
      "proof_restart_ready": false,
      "reason_not_accepted": "source-hosted candidate not selected by rival eliminator"
    },
    {
      "row_id": "IG_CLASS_EXTERIOR_COVARIANT_DERIVATIVE",
      "route": "IG_bridge",
      "source_artifact": "hourly-20260625-0711-cycle1-ig-rival-eliminator-source-identity.md",
      "candidate": "exterior_covariant_derivative",
      "status": "hosted_candidate",
      "accepted_for_routing": false,
      "proof_restart_ready": false,
      "reason_not_accepted": "rival class survives because no source eliminator selects the displayed Shiab candidate"
    },
    {
      "row_id": "IG_CLASS_SCALAR_TRACE_DIVERGENCE",
      "route": "IG_bridge",
      "source_artifact": "hourly-20260625-0711-cycle1-ig-rival-eliminator-source-identity.md",
      "candidate": "scalar_trace_divergence_coderivative",
      "status": "hosted_candidate",
      "accepted_for_routing": false,
      "proof_restart_ready": false,
      "reason_not_accepted": "rival class survives because no source eliminator selects the displayed Shiab candidate"
    },
    {
      "row_id": "IG_CLASS_SYMMETRIC_DERIVATIVE",
      "route": "IG_bridge",
      "source_artifact": "hourly-20260625-0711-cycle1-ig-rival-eliminator-source-identity.md",
      "candidate": "symmetric_derivative",
      "status": "hosted_candidate",
      "accepted_for_routing": false,
      "proof_restart_ready": false,
      "reason_not_accepted": "rival class survives because no source eliminator selects the displayed Shiab candidate"
    },
    {
      "row_id": "IG_CLASS_PROJECTED_DERIVATIVE",
      "route": "IG_bridge",
      "source_artifact": "hourly-20260625-0711-cycle1-ig-rival-eliminator-source-identity.md",
      "candidate": "projected_derivative",
      "status": "hosted_candidate",
      "accepted_for_routing": false,
      "proof_restart_ready": false,
      "reason_not_accepted": "rival class survives because no source eliminator selects the displayed Shiab candidate"
    },
    {
      "row_id": "IG_CLASS_LOWER_ORDER_DRESSED",
      "route": "IG_bridge",
      "source_artifact": "hourly-20260625-0711-cycle1-ig-rival-eliminator-source-identity.md",
      "candidate": "lower_order_dressed_class",
      "status": "hosted_candidate",
      "accepted_for_routing": false,
      "proof_restart_ready": false,
      "reason_not_accepted": "rival class survives because no source eliminator selects the displayed Shiab candidate"
    },
    {
      "row_id": "DGU_SECTION_8_SHIAB_CONTRACTION",
      "route": "DGU",
      "source_artifact": "hourly-20260625-0711-cycle1-dgu-bosonic-to-01-identity-rule-search.md",
      "candidate": "section_8_pdf_pages_41_44 Shiab/circle-dot_epsilon contraction operators",
      "status": "blocked_identity",
      "accepted_for_routing": false,
      "proof_restart_ready": false,
      "reason_not_accepted": "identity to actual D_GU_epsilon_0_1 missing"
    },
    {
      "row_id": "DGU_SECTION_9_1_I1_B",
      "route": "DGU",
      "source_artifact": "hourly-20260625-0711-cycle1-dgu-bosonic-to-01-identity-rule-search.md",
      "candidate": "section_9_1_pdf_pages_43_44 I_1^B and bosonic Euler-Lagrange setup",
      "status": "blocked_identity",
      "accepted_for_routing": false,
      "proof_restart_ready": false,
      "reason_not_accepted": "identity to actual D_GU_epsilon_0_1 missing"
    },
    {
      "row_id": "DGU_SECTION_9_2_I2_B",
      "route": "DGU",
      "source_artifact": "hourly-20260625-0711-cycle1-dgu-bosonic-to-01-identity-rule-search.md",
      "candidate": "section_9_2_pdf_page_45 I_2^B and D_omega_star Upsilon_omega equation",
      "status": "blocked_identity",
      "accepted_for_routing": false,
      "proof_restart_ready": false,
      "reason_not_accepted": "identity to actual D_GU_epsilon_0_1 missing"
    },
    {
      "row_id": "DGU_SECTION_9_3_FERMIONIC_DIRAC",
      "route": "DGU",
      "source_artifact": "hourly-20260625-0711-cycle1-dgu-bosonic-to-01-identity-rule-search.md",
      "candidate": "section_9_3_pdf_page_46 fermionic Dirac-like slash_D_omega display",
      "status": "blocked_identity",
      "accepted_for_routing": false,
      "proof_restart_ready": false,
      "reason_not_accepted": "identity to actual D_GU_epsilon_0_1 missing"
    },
    {
      "row_id": "DGU_SECTION_10_DEFORMATION_COMPLEX",
      "route": "DGU",
      "source_artifact": "hourly-20260625-0711-cycle1-dgu-bosonic-to-01-identity-rule-search.md",
      "candidate": "section_10_pdf_pages_47_48 bosonic deformation complex delta_1/delta_2",
      "status": "blocked_identity",
      "accepted_for_routing": false,
      "proof_restart_ready": false,
      "reason_not_accepted": "identity to actual D_GU_epsilon_0_1 missing"
    },
    {
      "row_id": "DGU_SECTION_12_1_PROJECTED_REDUCED_EQUATIONS",
      "route": "DGU",
      "source_artifact": "hourly-20260625-0711-cycle1-dgu-bosonic-to-01-identity-rule-search.md",
      "candidate": "section_12_1_pdf_page_55 projected reduced equations",
      "status": "blocked_identity",
      "accepted_for_routing": false,
      "proof_restart_ready": false,
      "reason_not_accepted": "identity to actual D_GU_epsilon_0_1 missing"
    },
    {
      "row_id": "RS_IMAGE_1010_MANUAL_AUDIT",
      "route": "RS",
      "source_artifact": "hourly-20260625-0711-cycle1-rs-manual-image-formula-diagram-audit.md",
      "candidate": "equation_10_10_manual_image_formula_diagram",
      "status": "scoped_fail",
      "accepted_for_routing": false,
      "proof_restart_ready": false,
      "reason_not_accepted": "image audit found no hidden pure RS minus-one cell"
    },
    {
      "row_id": "RS_E1010_N1",
      "route": "RS",
      "source_artifact": "hourly-20260625-0711-cycle2-rs-equation-1010-cell-typing-gate.md",
      "candidate": "E1010-N1",
      "status": "scoped_fail",
      "accepted_for_routing": false,
      "proof_restart_ready": false,
      "reason_not_accepted": "mixed /S plus ad node, not pure RS minus-one rule"
    },
    {
      "row_id": "RS_E1010_N2",
      "route": "RS",
      "source_artifact": "hourly-20260625-0711-cycle2-rs-equation-1010-cell-typing-gate.md",
      "candidate": "E1010-N2",
      "status": "scoped_fail",
      "accepted_for_routing": false,
      "proof_restart_ready": false,
      "reason_not_accepted": "mixed /S plus ad node, not pure RS minus-one rule"
    },
    {
      "row_id": "RS_E1010_N3",
      "route": "RS",
      "source_artifact": "hourly-20260625-0711-cycle2-rs-equation-1010-cell-typing-gate.md",
      "candidate": "E1010-N3",
      "status": "scoped_fail",
      "accepted_for_routing": false,
      "proof_restart_ready": false,
      "reason_not_accepted": "ad node, not RS"
    },
    {
      "row_id": "RS_E1010_N4",
      "route": "RS",
      "source_artifact": "hourly-20260625-0711-cycle2-rs-equation-1010-cell-typing-gate.md",
      "candidate": "E1010-N4",
      "status": "scoped_fail",
      "accepted_for_routing": false,
      "proof_restart_ready": false,
      "reason_not_accepted": "mixed /S plus ad node, not pure RS minus-one rule"
    },
    {
      "row_id": "RS_E1010_N5",
      "route": "RS",
      "source_artifact": "hourly-20260625-0711-cycle2-rs-equation-1010-cell-typing-gate.md",
      "candidate": "E1010-N5",
      "status": "scoped_fail",
      "accepted_for_routing": false,
      "proof_restart_ready": false,
      "reason_not_accepted": "/S target, not pure /R RS"
    },
    {
      "row_id": "RS_E1010_A1",
      "route": "RS",
      "source_artifact": "hourly-20260625-0711-cycle2-rs-equation-1010-cell-typing-gate.md",
      "candidate": "E1010-A1",
      "status": "scoped_fail",
      "accepted_for_routing": false,
      "proof_restart_ready": false,
      "reason_not_accepted": "operator-like label with zeta contraction, not RS rule"
    },
    {
      "row_id": "RS_E1010_A2",
      "route": "RS",
      "source_artifact": "hourly-20260625-0711-cycle2-rs-equation-1010-cell-typing-gate.md",
      "candidate": "E1010-A2",
      "status": "scoped_fail",
      "accepted_for_routing": false,
      "proof_restart_ready": false,
      "reason_not_accepted": "nu aggregate mixing label, not source RS rule"
    },
    {
      "row_id": "RS_E1010_A3",
      "route": "RS",
      "source_artifact": "hourly-20260625-0711-cycle2-rs-equation-1010-cell-typing-gate.md",
      "candidate": "E1010-A3",
      "status": "scoped_fail",
      "accepted_for_routing": false,
      "proof_restart_ready": false,
      "reason_not_accepted": "mixed connection/spinor diagram source, not pure RS"
    },
    {
      "row_id": "RS_E1010_A4",
      "route": "RS",
      "source_artifact": "hourly-20260625-0711-cycle2-rs-equation-1010-cell-typing-gate.md",
      "candidate": "E1010-A4",
      "status": "scoped_fail",
      "accepted_for_routing": false,
      "proof_restart_ready": false,
      "reason_not_accepted": "zeta aggregate/operator-like label, not RS rule"
    },
    {
      "row_id": "RS_E1010_A5",
      "route": "RS",
      "source_artifact": "hourly-20260625-0711-cycle2-rs-equation-1010-cell-typing-gate.md",
      "candidate": "E1010-A5",
      "status": "scoped_fail",
      "accepted_for_routing": false,
      "proof_restart_ready": false,
      "reason_not_accepted": "nu plus adjoint component, not RS"
    },
    {
      "row_id": "RS_E1010_A6",
      "route": "RS",
      "source_artifact": "hourly-20260625-0711-cycle2-rs-equation-1010-cell-typing-gate.md",
      "candidate": "E1010-A6",
      "status": "scoped_fail",
      "accepted_for_routing": false,
      "proof_restart_ready": false,
      "reason_not_accepted": "mixed connection/spinor/epsilon source, not pure RS"
    },
    {
      "row_id": "RS_E1010_A7",
      "route": "RS",
      "source_artifact": "hourly-20260625-0711-cycle2-rs-equation-1010-cell-typing-gate.md",
      "candidate": "E1010-A7",
      "status": "scoped_fail",
      "accepted_for_routing": false,
      "proof_restart_ready": false,
      "reason_not_accepted": "0-to-d operator-like label, not RS minus-one"
    },
    {
      "row_id": "QFT_FINITE_LOCAL_EXTRACTION_SPEC",
      "route": "QFT",
      "source_artifact": "hourly-20260625-0711-cycle2-qft-finite-local-extraction-spec-gate.md",
      "candidate": "P_fin^b: F_phys^b(O) -> K_b",
      "status": "underdefined_spec",
      "accepted_for_routing": false,
      "proof_restart_ready": false,
      "reason_not_accepted": "source-defined finite local extraction operation is missing"
    }
  ],
  "next_classifier_step": "RouteCandidateReceiptClassifier0711_V1"
}
```
