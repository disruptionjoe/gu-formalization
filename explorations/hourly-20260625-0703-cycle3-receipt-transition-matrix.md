---
title: "Hourly 20260625 0703 Cycle 3 Receipt Transition Matrix"
date: "2026-06-25"
run_id: "hourly-20260625-0703"
cycle: 3
lane: 1
doc_type: receipt_transition_matrix
artifact_id: "ReceiptTransitionMatrixAfterHourly20260625_0703_V1"
verdict: "NO_TRANSITIONS_ZERO_ACCEPTED_RECEIPTS"
owned_path: "explorations/hourly-20260625-0703-cycle3-receipt-transition-matrix.md"
companion_audit: "tests/hourly_20260625_0703_cycle3_receipt_transition_matrix_audit.py"
---

# ReceiptTransitionMatrixAfterHourly20260625_0703_V1

## 1. Verdict

Verdict: **blocked transition gate; zero rows transition**.

Across the ten cycle 1 and cycle 2 artifacts for run
`hourly-20260625-0703`, I count **68 explicit candidate/source/visual/acquisition
rows**. None transitions to:

- `accepted_receipt`;
- `accepted_for_routing`;
- `family_identity_passed`;
- `proof_restart_allowed`;
- `global_no_go`;
- `claim_promotion`.

The run improved source state in several places: Oxford official stills became
checksummed visual candidates, TOE/Jaimungal captions became a transiently
searched QFT surface, Keating storyboard/thumbnail capture became a scoped
negative, and RS alternate public-source search extended the negative ledger.
Those are locator positives and scoped negatives. They do not satisfy the
family identity, source-emitted rule, or complete negative-coverage conditions
needed for a transition.

## 2. Specific Claim/Bridge Under Test

The gate under test is:

```text
Do any cycle 1-2 candidate/source/visual/acquisition rows now have enough
source-clean payload to become accepted receipts, accepted routing rows,
family-identity-passed rows, proof-restart permissions, global no-go promotions,
or claim-promotion permissions?
```

The answer is no. The bridge fails before proof replay: every positive row is
still a locator, hosted candidate, generic formula, visual candidate, partial
acquisition, or scoped negative.

## 3. Owned Path And Sources Read First

Owned output path:

```text
explorations/hourly-20260625-0703-cycle3-receipt-transition-matrix.md
```

Companion audit:

```text
tests/hourly_20260625_0703_cycle3_receipt_transition_matrix_audit.py
```

Sources read first:

- `RESEARCH-POSTURE.md`
- `process/runbooks/five-lane-frontier-run.md`
- `process/runbooks/three-cycle-fifteen-hole-run.md`
- `explorations/hourly-20260625-0703-cycle1-ig-rival-selector-eliminator-recheck.md`
- `explorations/hourly-20260625-0703-cycle1-keating-pullthatupjamie-asset-reacquisition.md`
- `explorations/hourly-20260625-0703-cycle1-oxford-portal-frame-reacquisition.md`
- `explorations/hourly-20260625-0703-cycle1-qft-alternate-primary-source-query-execution.md`
- `explorations/hourly-20260625-0703-cycle1-rs-equation-1010-image-level-recheck.md`
- `explorations/hourly-20260625-0703-cycle2-ig-source-window-bianchi-selector-inventory.md`
- `explorations/hourly-20260625-0703-cycle2-keating-tzsevmqxu48-frame-capture-gate.md`
- `explorations/hourly-20260625-0703-cycle2-oxford-bosonic-dgu01-identity-test.md`
- `explorations/hourly-20260625-0703-cycle2-qft-complete-transcript-frame-acquisition-gate.md`
- `explorations/hourly-20260625-0703-cycle2-rs-alternate-source-minus-one-rule-search.md`

## 4. Strongest Positive Construction Attempt

The strongest positive construction is the cycle 1 Oxford source-hosted visual
packet plus the cycle 2 Oxford DGU identity test. Five official stills now have
source URLs, timestamps, checksums, and transcriptions. Two of those rows
display the bosonic replacement equations near `02:35:10` and `02:36:12`.

That is the closest row family to routing because it is not merely a transcript
locator: it is source-hosted visual content with stable frame-level evidence.
However, cycle 2 explicitly tests the required category change from bosonic
gauge-field equation to actual `D_GU^epsilon` 0/1 operator/action/EL family and
does not find the missing sector rule, domain, codomain, chirality convention,
coefficient packet, principal symbol, projectors, or family identity.

The strongest IG positive construction is the manuscript/Oxford/Keating Shiab
cluster: manuscript pages host generic Shiab formulas, Oxford hosts a visual
Shiab operator candidate, and Keating/Pull That Up Jamie locates a missing
Shiab projection sheet/frame route. Cycle 2 strengthens the source-window
inventory but still does not recover the representation-theory/highest-weight/
Bianchi selector calculation.

The strongest RS and QFT positives are not formula receipts. RS has field-content
and representation rows but no source-emitted minus-one rule. QFT has transcript
and frame/caption locator rows but no `F_phys^b(O) -> K_b` finite projector or
typed local-mode payload.

## 5. First Exact Obstruction

The first exact obstruction is a cross-family receipt identity obstruction:

```text
No counted row supplies both source-clean payload and the family identity object
required to route it as the relevant GU proof input.
```

By family:

- IG: no recovered representation-theory/highest-weight/Bianchi selector
  calculation eliminates rival Shiab/codomain classes or identifies the hosted
  Shiab map with `SourceForcedCodomainSelectorForK_IG`.
- DGU/VZ: no source-clean identity ties Oxford bosonic equations to the actual
  `D_GU^epsilon` 0/1 family with domain, codomain, sector, coefficients,
  principal symbol, projectors, and family identity.
- RS: no source emits a field/parameter rule for `d_RS,-1` with source, target,
  degree/slot, RS field component, and rule kind.
- QFT: no inspected or acquired surface emits `F_phys^b(O)`, `K_b`, `P_fin^b`,
  and typed local-mode records.
- Global no-go: scoped negatives do not cover every declared source variant with
  complete transcript/frame/formula coverage and notation-variant logs.

## 6. What Would Change If Closed

If one row closed as an accepted receipt, the matrix would change only locally:

- `accepted_receipt_count` would increase for that row's family.
- `proof_restart_allowed` would still require the accepted row to pass family
  identity and target-import screens.
- claim promotion would remain false until a downstream proof gate derives the
  relevant mathematical or physical claim from the accepted receipt.

If the global negative bundle closed instead, a global no-go promotion could be
considered for the specific family covered by complete negative evidence. No
cycle 1-2 artifact supplies that bundle.

## 7. Falsification/Demotion Condition

Falsify this zero-transition matrix if any row in the cycle 1-2 artifacts is
shown to contain an already-counted source-clean payload plus the required
family identity fields. The correction must identify the exact row, artifact,
payload, identity witness, target-import screen, and transition being changed.

Demote the positive source-route families if their next acquisition passes
complete the corresponding negative evidence:

- Keating/Pull That Up Jamie: no formula-bearing sheet/frame/asset exists or can
  be source-identified with the missing Shiab projection calculation.
- Oxford DGU/VZ: no neighboring source text or visual row supplies the
  `D_GU^epsilon` 0/1 identity packet.
- RS: all declared primary/public variants lack an RS minus-one rule after
  timestamped transcript/frame acquisition.
- QFT: all declared surfaces lack `P_fin^b` payload after complete
  transcript/frame/formula coverage.

## 8. Next Meaningful Computation

Next frontier object:

```text
ReceiptTransitionMatrixSourceCompletionQueue_V1
```

The queue should run the next source-completion objects in sequence, not as a
proof restart:

1. `RecoveredBianchiHighestWeightSelectorForShiab_V1`
2. `DecodableTzSEvmqxu48ArchiveOrSourceAssetWithFormulaFrameAudit_V1`
3. `OxfordBosonicTwoAnchorDGU01IdentityPacket_V1`
4. `FrameAndFormulaCompletionBundleForQFTPFinBDeclaredSurfaces_V1`
5. `TimestampedTranscriptAcquisitionForModernRSSurfaces_V1`

## 9. JSON Summary

```json
{
  "artifact": "ReceiptTransitionMatrixAfterHourly20260625_0703_V1",
  "run_id": "hourly-20260625-0703",
  "cycle": 3,
  "lane": 1,
  "artifact_id": "ReceiptTransitionMatrixAfterHourly20260625_0703_V1",
  "verdict": "NO_TRANSITIONS_ZERO_ACCEPTED_RECEIPTS",
  "rows": [
    {"row_id":"c1_ig_rival_exterior_derivative","source_artifact":"ManuscriptRepresentationTheoryBianchiRivalEliminatorForShiab_Recheck_V1","row_kind":"candidate_rival_class","family":"IG","positive_status":"admissible exterior/covariant derivative candidate","first_obstruction":"source rule selecting exterior 2-form codomain and eliminating rivals missing","accepted_receipt":false,"accepted_for_routing":false,"family_identity_passed":false,"proof_restart_allowed":false,"global_no_go":false,"claim_promotion":false},
    {"row_id":"c1_ig_rival_coderivative_trace_scalar","source_artifact":"ManuscriptRepresentationTheoryBianchiRivalEliminatorForShiab_Recheck_V1","row_kind":"candidate_rival_class","family":"IG","positive_status":"contraction-style reading source-natural","first_obstruction":"rule excluding contraction/trace/zero-form codomains missing","accepted_receipt":false,"accepted_for_routing":false,"family_identity_passed":false,"proof_restart_allowed":false,"global_no_go":false,"claim_promotion":false},
    {"row_id":"c1_ig_rival_symmetric_derivative","source_artifact":"ManuscriptRepresentationTheoryBianchiRivalEliminatorForShiab_Recheck_V1","row_kind":"candidate_rival_class","family":"IG","positive_status":"first-order gauge-covariant derivative not source-excluded","first_obstruction":"representation/Bianchi rule forcing antisymmetric exterior degree missing","accepted_receipt":false,"accepted_for_routing":false,"family_identity_passed":false,"proof_restart_allowed":false,"global_no_go":false,"claim_promotion":false},
    {"row_id":"c1_ig_rival_projected_derivative","source_artifact":"ManuscriptRepresentationTheoryBianchiRivalEliminatorForShiab_Recheck_V1","row_kind":"candidate_rival_class","family":"IG","positive_status":"projection-removal context exists","first_obstruction":"projector/loss theorem excluding projected classes missing","accepted_receipt":false,"accepted_for_routing":false,"family_identity_passed":false,"proof_restart_allowed":false,"global_no_go":false,"claim_promotion":false},
    {"row_id":"c1_ig_rival_lower_order_dressed_exterior","source_artifact":"ManuscriptRepresentationTheoryBianchiRivalEliminatorForShiab_Recheck_V1","row_kind":"candidate_rival_class","family":"IG","positive_status":"lower-order dressing plausible","first_obstruction":"lower-order rigidity or normalization policy missing","accepted_receipt":false,"accepted_for_routing":false,"family_identity_passed":false,"proof_restart_allowed":false,"global_no_go":false,"claim_promotion":false},
    {"row_id":"c1_ig_rival_displayed_shiab_codomain","source_artifact":"ManuscriptRepresentationTheoryBianchiRivalEliminatorForShiab_Recheck_V1","row_kind":"candidate_rival_class","family":"IG","positive_status":"hosted displayed Shiab codomain candidate","first_obstruction":"family identity to SourceForcedCodomainSelectorForK_IG and rival eliminators missing","accepted_receipt":false,"accepted_for_routing":false,"family_identity_passed":false,"proof_restart_allowed":false,"global_no_go":false,"claim_promotion":false},
    {"row_id":"c1_keating_revealed_transcript_window","source_artifact":"KeatingPullThatUpJamieShiabProjectionFormulaAssetPacketExecution_V1","row_kind":"source_surface","family":"IG","positive_status":"official transcript names missing sheet window","first_obstruction":"sheet/formula not emitted","accepted_receipt":false,"accepted_for_routing":false,"family_identity_passed":false,"proof_restart_allowed":false,"global_no_go":false,"claim_promotion":false},
    {"row_id":"c1_keating_pull_that_up_jamie_metadata","source_artifact":"KeatingPullThatUpJamieShiabProjectionFormulaAssetPacketExecution_V1","row_kind":"source_surface","family":"IG","positive_status":"official page/oEmbed/thumbnail metadata","first_obstruction":"caption and thumbnail only; no formula frame","accepted_receipt":false,"accepted_for_routing":false,"family_identity_passed":false,"proof_restart_allowed":false,"global_no_go":false,"claim_promotion":false},
    {"row_id":"c1_keating_author_manuscript_pages_41_44","source_artifact":"KeatingPullThatUpJamieShiabProjectionFormulaAssetPacketExecution_V1","row_kind":"source_surface","family":"IG","positive_status":"generic Shiab formulas visible","first_obstruction":"identity to missing highest-weight/Bianchi sheet not proved","accepted_receipt":false,"accepted_for_routing":false,"family_identity_passed":false,"proof_restart_allowed":false,"global_no_go":false,"claim_promotion":false},
    {"row_id":"c1_oxford_anchor_023343_shiab_operator","source_artifact":"OxfordPortalPowerPointFormulaFrameReacquisition_V1","row_kind":"visual_anchor","family":"IG_DGU_VZ_precondition","positive_status":"source-hosted Shiab visual candidate with checksum","first_obstruction":"no domain/codomain selector rule or K_IG rival eliminator","accepted_receipt":false,"accepted_for_routing":false,"family_identity_passed":false,"proof_restart_allowed":false,"global_no_go":false,"claim_promotion":false},
    {"row_id":"c1_oxford_anchor_023510_swervature","source_artifact":"OxfordPortalPowerPointFormulaFrameReacquisition_V1","row_kind":"visual_anchor","family":"DGU_VZ","positive_status":"source-hosted bosonic replacement equation","first_obstruction":"not identified as actual D_GU_epsilon 0/1 object","accepted_receipt":false,"accepted_for_routing":false,"family_identity_passed":false,"proof_restart_allowed":false,"global_no_go":false,"claim_promotion":false},
    {"row_id":"c1_oxford_anchor_023612_displasion","source_artifact":"OxfordPortalPowerPointFormulaFrameReacquisition_V1","row_kind":"visual_anchor","family":"DGU_VZ","positive_status":"source-hosted S_omega = J_omega frame","first_obstruction":"family identity to D_GU_epsilon 0/1 absent","accepted_receipt":false,"accepted_for_routing":false,"family_identity_passed":false,"proof_restart_allowed":false,"global_no_go":false,"claim_promotion":false},
    {"row_id":"c1_oxford_anchor_023853_rs_dirac_adjacency","source_artifact":"OxfordPortalPowerPointFormulaFrameReacquisition_V1","row_kind":"visual_anchor","family":"RS","positive_status":"source-hosted representation decomposition frame","first_obstruction":"not a source action/operator/differential/Noether/BRST rule for d_RS_minus_1","accepted_receipt":false,"accepted_for_routing":false,"family_identity_passed":false,"proof_restart_allowed":false,"global_no_go":false,"claim_promotion":false},
    {"row_id":"c1_oxford_anchor_024019_pullback_summary","source_artifact":"OxfordPortalPowerPointFormulaFrameReacquisition_V1","row_kind":"visual_anchor","family":"DGU_VZ_RS_QFT","positive_status":"source-hosted summary/provenance frame","first_obstruction":"summary prose lacks displayed family formula identity","accepted_receipt":false,"accepted_for_routing":false,"family_identity_passed":false,"proof_restart_allowed":false,"global_no_go":false,"claim_promotion":false},
    {"row_id":"c1_qft_surface_oxford_portal_special","source_artifact":"QFTAlternatePrimarySourceQueryBundle_V1","row_kind":"inspected_surface","family":"QFT","positive_status":"projection/QFT-adjacent locators","first_obstruction":"no F_phys_b, K_b, P_fin_b, or typed modes","accepted_receipt":false,"accepted_for_routing":false,"family_identity_passed":false,"proof_restart_allowed":false,"global_no_go":false,"claim_promotion":false},
    {"row_id":"c1_qft_surface_pull_that_up_jamie","source_artifact":"QFTAlternatePrimarySourceQueryBundle_V1","row_kind":"inspected_surface","family":"QFT_IG","positive_status":"Shiab/projection locator","first_obstruction":"no finite projector payload","accepted_receipt":false,"accepted_for_routing":false,"family_identity_passed":false,"proof_restart_allowed":false,"global_no_go":false,"claim_promotion":false},
    {"row_id":"c1_qft_surface_keating_revealed","source_artifact":"QFTAlternatePrimarySourceQueryBundle_V1","row_kind":"inspected_surface","family":"QFT_IG","positive_status":"geometry/projection transcript locator","first_obstruction":"no finite local source-mode records","accepted_receipt":false,"accepted_for_routing":false,"family_identity_passed":false,"proof_restart_allowed":false,"global_no_go":false,"claim_promotion":false},
    {"row_id":"c1_qft_surface_keating_conversation","source_artifact":"QFTAlternatePrimarySourceQueryBundle_V1","row_kind":"inspected_surface","family":"QFT","positive_status":"observerse/Pati-Salam carrier context","first_obstruction":"no P_fin_b map","accepted_receipt":false,"accepted_for_routing":false,"family_identity_passed":false,"proof_restart_allowed":false,"global_no_go":false,"claim_promotion":false},
    {"row_id":"c1_qft_surface_toe_jaimungal","source_artifact":"QFTAlternatePrimarySourceQueryBundle_V1","row_kind":"inspected_surface","family":"QFT","positive_status":"modern transcript/query locator","first_obstruction":"no acquired finite-projector payload","accepted_receipt":false,"accepted_for_routing":false,"family_identity_passed":false,"proof_restart_allowed":false,"global_no_go":false,"claim_promotion":false},
    {"row_id":"c1_qft_surface_keating_desi_ucsd","source_artifact":"QFTAlternatePrimarySourceQueryBundle_V1","row_kind":"inspected_surface","family":"QFT","positive_status":"field-content/pullback/Pati-Salam context","first_obstruction":"no K_b target or P_fin_b rule","accepted_receipt":false,"accepted_for_routing":false,"family_identity_passed":false,"proof_restart_allowed":false,"global_no_go":false,"claim_promotion":false},
    {"row_id":"c1_qft_surface_jre_backlog","source_artifact":"QFTAlternatePrimarySourceQueryBundle_V1","row_kind":"inspected_surface","family":"QFT","positive_status":"declared source backlog row","first_obstruction":"not acquired/inspected enough for receipt","accepted_receipt":false,"accepted_for_routing":false,"family_identity_passed":false,"proof_restart_allowed":false,"global_no_go":false,"claim_promotion":false},
    {"row_id":"c1_qft_surface_prior_manuscript_packet","source_artifact":"QFTAlternatePrimarySourceQueryBundle_V1","row_kind":"inspected_surface","family":"QFT","positive_status":"prior packet reviewed as locator context","first_obstruction":"no source-emitted finite projector object","accepted_receipt":false,"accepted_for_routing":false,"family_identity_passed":false,"proof_restart_allowed":false,"global_no_go":false,"claim_promotion":false},
    {"row_id":"c1_rs_asset_01","source_artifact":"ManualImageLevelRSFormulaDiagramAudit_V1","row_kind":"inspected_asset","family":"RS","positive_status":"equation 10.10/image-level RS-adjacent asset","first_obstruction":"no stable RS-only d_RS_minus_1 source rule","accepted_receipt":false,"accepted_for_routing":false,"family_identity_passed":false,"proof_restart_allowed":false,"global_no_go":false,"claim_promotion":false},
    {"row_id":"c1_rs_asset_02","source_artifact":"ManualImageLevelRSFormulaDiagramAudit_V1","row_kind":"inspected_asset","family":"RS","positive_status":"RS-adjacent manuscript/visual asset","first_obstruction":"source space, target space, and minus-one slot missing","accepted_receipt":false,"accepted_for_routing":false,"family_identity_passed":false,"proof_restart_allowed":false,"global_no_go":false,"claim_promotion":false},
    {"row_id":"c1_rs_asset_03","source_artifact":"ManualImageLevelRSFormulaDiagramAudit_V1","row_kind":"inspected_asset","family":"RS","positive_status":"RS-adjacent manuscript/visual asset","first_obstruction":"pure RS field component and rule kind missing","accepted_receipt":false,"accepted_for_routing":false,"family_identity_passed":false,"proof_restart_allowed":false,"global_no_go":false,"claim_promotion":false},
    {"row_id":"c1_rs_asset_04","source_artifact":"ManualImageLevelRSFormulaDiagramAudit_V1","row_kind":"inspected_asset","family":"RS","positive_status":"RS-adjacent manuscript/visual asset","first_obstruction":"family identity to d_RS_minus_1 not proved","accepted_receipt":false,"accepted_for_routing":false,"family_identity_passed":false,"proof_restart_allowed":false,"global_no_go":false,"claim_promotion":false},
    {"row_id":"c1_rs_asset_05","source_artifact":"ManualImageLevelRSFormulaDiagramAudit_V1","row_kind":"inspected_asset","family":"RS","positive_status":"RS-adjacent manuscript/visual asset","first_obstruction":"does not isolate gauge/BRST operator rule","accepted_receipt":false,"accepted_for_routing":false,"family_identity_passed":false,"proof_restart_allowed":false,"global_no_go":false,"claim_promotion":false},
    {"row_id":"c1_rs_asset_06","source_artifact":"ManualImageLevelRSFormulaDiagramAudit_V1","row_kind":"inspected_asset","family":"RS","positive_status":"RS-adjacent manuscript/visual asset","first_obstruction":"target-import-clean source rule absent","accepted_receipt":false,"accepted_for_routing":false,"family_identity_passed":false,"proof_restart_allowed":false,"global_no_go":false,"claim_promotion":false},
    {"row_id":"c1_rs_asset_07","source_artifact":"ManualImageLevelRSFormulaDiagramAudit_V1","row_kind":"inspected_asset","family":"RS","positive_status":"RS-adjacent manuscript/visual asset","first_obstruction":"representation evidence not operator receipt","accepted_receipt":false,"accepted_for_routing":false,"family_identity_passed":false,"proof_restart_allowed":false,"global_no_go":false,"claim_promotion":false},
    {"row_id":"c1_rs_asset_08","source_artifact":"ManualImageLevelRSFormulaDiagramAudit_V1","row_kind":"inspected_asset","family":"RS","positive_status":"RS-adjacent manuscript/visual asset","first_obstruction":"diagram does not emit quotient semantics","accepted_receipt":false,"accepted_for_routing":false,"family_identity_passed":false,"proof_restart_allowed":false,"global_no_go":false,"claim_promotion":false},
    {"row_id":"c1_rs_asset_09","source_artifact":"ManualImageLevelRSFormulaDiagramAudit_V1","row_kind":"inspected_asset","family":"RS","positive_status":"RS-adjacent manuscript/visual asset","first_obstruction":"not enough source typing for receipt","accepted_receipt":false,"accepted_for_routing":false,"family_identity_passed":false,"proof_restart_allowed":false,"global_no_go":false,"claim_promotion":false},
    {"row_id":"c1_rs_asset_10","source_artifact":"ManualImageLevelRSFormulaDiagramAudit_V1","row_kind":"inspected_asset","family":"RS","positive_status":"RS-adjacent manuscript/visual asset","first_obstruction":"minus-one differential not source-emitted","accepted_receipt":false,"accepted_for_routing":false,"family_identity_passed":false,"proof_restart_allowed":false,"global_no_go":false,"claim_promotion":false},
    {"row_id":"c1_rs_asset_11","source_artifact":"ManualImageLevelRSFormulaDiagramAudit_V1","row_kind":"inspected_asset","family":"RS","positive_status":"RS-adjacent manuscript/visual asset","first_obstruction":"operator/action/Noether/BRST rule missing","accepted_receipt":false,"accepted_for_routing":false,"family_identity_passed":false,"proof_restart_allowed":false,"global_no_go":false,"claim_promotion":false},
    {"row_id":"c1_rs_asset_12","source_artifact":"ManualImageLevelRSFormulaDiagramAudit_V1","row_kind":"inspected_asset","family":"RS","positive_status":"RS-adjacent manuscript/visual asset","first_obstruction":"receipt remains failed for d_RS_minus_1","accepted_receipt":false,"accepted_for_routing":false,"family_identity_passed":false,"proof_restart_allowed":false,"global_no_go":false,"claim_promotion":false},
    {"row_id":"c2_ig_window_section_8","source_artifact":"SourceWindowFormulaInventoryAndBianchiSelectorForShiab_V1","row_kind":"source_window","family":"IG","positive_status":"Section 8 operator/invariant material inventoried","first_obstruction":"selector calculation not recovered","accepted_receipt":false,"accepted_for_routing":false,"family_identity_passed":false,"proof_restart_allowed":false,"global_no_go":false,"claim_promotion":false},
    {"row_id":"c2_ig_window_section_9","source_artifact":"SourceWindowFormulaInventoryAndBianchiSelectorForShiab_V1","row_kind":"source_window","family":"IG","positive_status":"Section 9 Shiab formula window inventoried","first_obstruction":"displayed formula not uniquely selected","accepted_receipt":false,"accepted_for_routing":false,"family_identity_passed":false,"proof_restart_allowed":false,"global_no_go":false,"claim_promotion":false},
    {"row_id":"c2_ig_window_summary_12","source_artifact":"SourceWindowFormulaInventoryAndBianchiSelectorForShiab_V1","row_kind":"source_window","family":"IG","positive_status":"Summary projection/Bianchi context inventoried","first_obstruction":"no full projector policy for K_IG","accepted_receipt":false,"accepted_for_routing":false,"family_identity_passed":false,"proof_restart_allowed":false,"global_no_go":false,"claim_promotion":false},
    {"row_id":"c2_ig_operator_8_1","source_artifact":"SourceWindowFormulaInventoryAndBianchiSelectorForShiab_V1","row_kind":"operator_row","family":"IG","positive_status":"operator row inventoried","first_obstruction":"candidate family and selector proof incomplete","accepted_receipt":false,"accepted_for_routing":false,"family_identity_passed":false,"proof_restart_allowed":false,"global_no_go":false,"claim_promotion":false},
    {"row_id":"c2_ig_operator_8_7","source_artifact":"SourceWindowFormulaInventoryAndBianchiSelectorForShiab_V1","row_kind":"operator_row","family":"IG","positive_status":"invariant basis/operator row inventoried","first_obstruction":"highest-weight/Bianchi selection criterion missing","accepted_receipt":false,"accepted_for_routing":false,"family_identity_passed":false,"proof_restart_allowed":false,"global_no_go":false,"claim_promotion":false},
    {"row_id":"c2_ig_operator_9_2","source_artifact":"SourceWindowFormulaInventoryAndBianchiSelectorForShiab_V1","row_kind":"operator_row","family":"IG","positive_status":"typed Shiab map row inventoried","first_obstruction":"family identity to SourceForcedCodomainSelectorForK_IG missing","accepted_receipt":false,"accepted_for_routing":false,"family_identity_passed":false,"proof_restart_allowed":false,"global_no_go":false,"claim_promotion":false},
    {"row_id":"c2_ig_operator_9_3","source_artifact":"SourceWindowFormulaInventoryAndBianchiSelectorForShiab_V1","row_kind":"operator_row","family":"IG","positive_status":"displayed Einstein/Ricci-like formula inventoried","first_obstruction":"selected formula proof missing","accepted_receipt":false,"accepted_for_routing":false,"family_identity_passed":false,"proof_restart_allowed":false,"global_no_go":false,"claim_promotion":false},
    {"row_id":"c2_ig_operator_12_2_12_7","source_artifact":"SourceWindowFormulaInventoryAndBianchiSelectorForShiab_V1","row_kind":"operator_row","family":"IG","positive_status":"projection/Bianchi summary row inventoried","first_obstruction":"does not recover missing Shiab choice calculation","accepted_receipt":false,"accepted_for_routing":false,"family_identity_passed":false,"proof_restart_allowed":false,"global_no_go":false,"claim_promotion":false},
    {"row_id":"c2_ig_operator_missing_sheet","source_artifact":"SourceWindowFormulaInventoryAndBianchiSelectorForShiab_V1","row_kind":"operator_row","family":"IG","positive_status":"missing-sheet requirement isolated","first_obstruction":"recovered representation-theory calculation absent","accepted_receipt":false,"accepted_for_routing":false,"family_identity_passed":false,"proof_restart_allowed":false,"global_no_go":false,"claim_promotion":false},
    {"row_id":"c2_ig_rival_exterior_derivative","source_artifact":"SourceWindowFormulaInventoryAndBianchiSelectorForShiab_V1","row_kind":"candidate_rival_class","family":"IG","positive_status":"rival remains source-natural","first_obstruction":"not eliminated by source","accepted_receipt":false,"accepted_for_routing":false,"family_identity_passed":false,"proof_restart_allowed":false,"global_no_go":false,"claim_promotion":false},
    {"row_id":"c2_ig_rival_coderivative_trace_scalar","source_artifact":"SourceWindowFormulaInventoryAndBianchiSelectorForShiab_V1","row_kind":"candidate_rival_class","family":"IG","positive_status":"rival remains source-natural","first_obstruction":"not eliminated by source","accepted_receipt":false,"accepted_for_routing":false,"family_identity_passed":false,"proof_restart_allowed":false,"global_no_go":false,"claim_promotion":false},
    {"row_id":"c2_ig_rival_symmetric_derivative","source_artifact":"SourceWindowFormulaInventoryAndBianchiSelectorForShiab_V1","row_kind":"candidate_rival_class","family":"IG","positive_status":"rival remains source-natural","first_obstruction":"not eliminated by source","accepted_receipt":false,"accepted_for_routing":false,"family_identity_passed":false,"proof_restart_allowed":false,"global_no_go":false,"claim_promotion":false},
    {"row_id":"c2_ig_rival_projected_derivative","source_artifact":"SourceWindowFormulaInventoryAndBianchiSelectorForShiab_V1","row_kind":"candidate_rival_class","family":"IG","positive_status":"rival remains source-natural","first_obstruction":"not eliminated by source","accepted_receipt":false,"accepted_for_routing":false,"family_identity_passed":false,"proof_restart_allowed":false,"global_no_go":false,"claim_promotion":false},
    {"row_id":"c2_ig_rival_lower_order_dressed_exterior","source_artifact":"SourceWindowFormulaInventoryAndBianchiSelectorForShiab_V1","row_kind":"candidate_rival_class","family":"IG","positive_status":"rival remains source-natural","first_obstruction":"not eliminated by source","accepted_receipt":false,"accepted_for_routing":false,"family_identity_passed":false,"proof_restart_allowed":false,"global_no_go":false,"claim_promotion":false},
    {"row_id":"c2_ig_rival_displayed_shiab_codomain","source_artifact":"SourceWindowFormulaInventoryAndBianchiSelectorForShiab_V1","row_kind":"candidate_rival_class","family":"IG","positive_status":"hosted Shiab candidate remains","first_obstruction":"identity and rival elimination missing","accepted_receipt":false,"accepted_for_routing":false,"family_identity_passed":false,"proof_restart_allowed":false,"global_no_go":false,"claim_promotion":false},
    {"row_id":"c2_keating_official_page_embed_caption","source_artifact":"FrameLevelPullThatUpJamieTzSEvmqxu48FormulaCaptureAndManuscriptIdentityCheck_V1","row_kind":"capture_attempt","family":"IG","positive_status":"HTTP 200 page caption confirms Shiab Projection visual","first_obstruction":"HTML exposes no formula asset/sheet","accepted_receipt":false,"accepted_for_routing":false,"family_identity_passed":false,"proof_restart_allowed":false,"global_no_go":false,"claim_promotion":false},
    {"row_id":"c2_keating_youtube_oembed_metadata","source_artifact":"FrameLevelPullThatUpJamieTzSEvmqxu48FormulaCaptureAndManuscriptIdentityCheck_V1","row_kind":"capture_attempt","family":"IG","positive_status":"oEmbed metadata confirms video identity","first_obstruction":"metadata only","accepted_receipt":false,"accepted_for_routing":false,"family_identity_passed":false,"proof_restart_allowed":false,"global_no_go":false,"claim_promotion":false},
    {"row_id":"c2_keating_watch_player_response","source_artifact":"FrameLevelPullThatUpJamieTzSEvmqxu48FormulaCaptureAndManuscriptIdentityCheck_V1","row_kind":"capture_attempt","family":"IG","positive_status":"watch-page stream/storyboard metadata exposed","first_obstruction":"zero caption tracks and no decoded formula frame","accepted_receipt":false,"accepted_for_routing":false,"family_identity_passed":false,"proof_restart_allowed":false,"global_no_go":false,"claim_promotion":false},
    {"row_id":"c2_keating_storyboard_level_2","source_artifact":"FrameLevelPullThatUpJamieTzSEvmqxu48FormulaCaptureAndManuscriptIdentityCheck_V1","row_kind":"capture_attempt","family":"IG","positive_status":"three storyboard sheets fetched with checksums","first_obstruction":"160x90 storyboard shows diagram animation only, no formula-bearing frame","accepted_receipt":false,"accepted_for_routing":false,"family_identity_passed":false,"proof_restart_allowed":false,"global_no_go":false,"claim_promotion":false},
    {"row_id":"c2_keating_hqdefault_thumbnail","source_artifact":"FrameLevelPullThatUpJamieTzSEvmqxu48FormulaCaptureAndManuscriptIdentityCheck_V1","row_kind":"capture_attempt","family":"IG","positive_status":"thumbnail checksum and labels captured","first_obstruction":"not a formula or source rule","accepted_receipt":false,"accepted_for_routing":false,"family_identity_passed":false,"proof_restart_allowed":false,"global_no_go":false,"claim_promotion":false},
    {"row_id":"c2_keating_direct_mp4_stream_decode","source_artifact":"FrameLevelPullThatUpJamieTzSEvmqxu48FormulaCaptureAndManuscriptIdentityCheck_V1","row_kind":"capture_attempt","family":"IG","positive_status":"direct stream URL exposed","first_obstruction":"ffmpeg and requests blocked by HTTP 403; no frame acquired","accepted_receipt":false,"accepted_for_routing":false,"family_identity_passed":false,"proof_restart_allowed":false,"global_no_go":false,"claim_promotion":false},
    {"row_id":"c2_oxford_dgu_anchor_023510_swervature","source_artifact":"BosonicOxfordReplacementToDGU01IdentityTest_V1","row_kind":"identity_anchor","family":"DGU_VZ","positive_status":"bosonic replacement equation candidate","first_obstruction":"sector/domain/codomain/chirality/coefficient/principal-symbol/projector/family identity packet missing","accepted_receipt":false,"accepted_for_routing":false,"family_identity_passed":false,"proof_restart_allowed":false,"global_no_go":false,"claim_promotion":false},
    {"row_id":"c2_oxford_dgu_anchor_023612_displasion","source_artifact":"BosonicOxfordReplacementToDGU01IdentityTest_V1","row_kind":"identity_anchor","family":"DGU_VZ","positive_status":"condensed swervature/displasion equation candidate","first_obstruction":"actual D_GU_epsilon 0/1 identity missing","accepted_receipt":false,"accepted_for_routing":false,"family_identity_passed":false,"proof_restart_allowed":false,"global_no_go":false,"claim_promotion":false},
    {"row_id":"c2_qft_toe_jaimungal","source_artifact":"CompleteTranscriptAndFrameAcquisitionForQFTFiniteProjector_V1","row_kind":"acquired_surface","family":"QFT","positive_status":"transient YouTube captions fetched and searched","first_obstruction":"no finite domain-target-map payload; frames not acquired","accepted_receipt":false,"accepted_for_routing":false,"family_identity_passed":false,"proof_restart_allowed":false,"global_no_go":false,"claim_promotion":false},
    {"row_id":"c2_qft_keating_desi_ucsd","source_artifact":"CompleteTranscriptAndFrameAcquisitionForQFTFiniteProjector_V1","row_kind":"acquired_surface","family":"QFT","positive_status":"complete local modern transcript available and queried","first_obstruction":"geometry/pullback/Pati-Salam locators only; no P_fin_b","accepted_receipt":false,"accepted_for_routing":false,"family_identity_passed":false,"proof_restart_allowed":false,"global_no_go":false,"claim_promotion":false},
    {"row_id":"c2_qft_keating_revealed_conversation","source_artifact":"CompleteTranscriptAndFrameAcquisitionForQFTFiniteProjector_V1","row_kind":"acquired_surface","family":"QFT_IG","positive_status":"transcript surfaces searchable; visual route scoped","first_obstruction":"no P_fin_b and visual formula/sheet identity missing","accepted_receipt":false,"accepted_for_routing":false,"family_identity_passed":false,"proof_restart_allowed":false,"global_no_go":false,"claim_promotion":false},
    {"row_id":"c2_qft_oxford_portal","source_artifact":"CompleteTranscriptAndFrameAcquisitionForQFTFiniteProjector_V1","row_kind":"acquired_surface","family":"QFT_DGU_RS_IG","positive_status":"official frame packet plus caption hits available","first_obstruction":"no F_phys_b to K_b projector or typed mode records","accepted_receipt":false,"accepted_for_routing":false,"family_identity_passed":false,"proof_restart_allowed":false,"global_no_go":false,"claim_promotion":false},
    {"row_id":"c2_rs_manuscript_prior","source_artifact":"AlternatePrimarySourceSearchForSourceEmittedRSMinusOneRule_V1","row_kind":"searched_surface","family":"RS","positive_status":"prior manuscript/image audits contain RS-adjacent hits","first_obstruction":"scoped manuscript route already failed","accepted_receipt":false,"accepted_for_routing":false,"family_identity_passed":false,"proof_restart_allowed":false,"global_no_go":false,"claim_promotion":false},
    {"row_id":"c2_rs_oxford_transcript","source_artifact":"AlternatePrimarySourceSearchForSourceEmittedRSMinusOneRule_V1","row_kind":"searched_surface","family":"RS","positive_status":"RS representation/field-content transcript windows","first_obstruction":"representation field content only","accepted_receipt":false,"accepted_for_routing":false,"family_identity_passed":false,"proof_restart_allowed":false,"global_no_go":false,"claim_promotion":false},
    {"row_id":"c2_rs_portal_special_transcript","source_artifact":"AlternatePrimarySourceSearchForSourceEmittedRSMinusOneRule_V1","row_kind":"searched_surface","family":"RS","positive_status":"same RS field-content window","first_obstruction":"no field/parameter rule","accepted_receipt":false,"accepted_for_routing":false,"family_identity_passed":false,"proof_restart_allowed":false,"global_no_go":false,"claim_promotion":false},
    {"row_id":"c2_rs_portal_wiki_mirror","source_artifact":"AlternatePrimarySourceSearchForSourceEmittedRSMinusOneRule_V1","row_kind":"searched_surface","family":"RS","positive_status":"primary-adjacent mirror confirms same windows","first_obstruction":"mirror adds no new rule","accepted_receipt":false,"accepted_for_routing":false,"family_identity_passed":false,"proof_restart_allowed":false,"global_no_go":false,"claim_promotion":false},
    {"row_id":"c2_rs_portal_wiki_x_index","source_artifact":"AlternatePrimarySourceSearchForSourceEmittedRSMinusOneRule_V1","row_kind":"searched_surface","family":"RS","positive_status":"Spin-3/2 prediction language","first_obstruction":"particle prediction not operator rule","accepted_receipt":false,"accepted_for_routing":false,"family_identity_passed":false,"proof_restart_allowed":false,"global_no_go":false,"claim_promotion":false},
    {"row_id":"c2_rs_live_exact_notation_search","source_artifact":"AlternatePrimarySourceSearchForSourceEmittedRSMinusOneRule_V1","row_kind":"searched_surface","family":"RS","positive_status":"exact notation queries executed","first_obstruction":"no primary GU hit emitting d_RS_minus_1","accepted_receipt":false,"accepted_for_routing":false,"family_identity_passed":false,"proof_restart_allowed":false,"global_no_go":false,"claim_promotion":false},
    {"row_id":"c2_rs_declared_modern_media_backlog","source_artifact":"AlternatePrimarySourceSearchForSourceEmittedRSMinusOneRule_V1","row_kind":"searched_surface","family":"RS","positive_status":"declared unavailability rows recorded","first_obstruction":"not checked enough for accepted receipt; global no-go blocked","accepted_receipt":false,"accepted_for_routing":false,"family_identity_passed":false,"proof_restart_allowed":false,"global_no_go":false,"claim_promotion":false}
  ],
  "accepted_receipt_count": 0,
  "accepted_for_routing_count": 0,
  "family_identity_checks_passed": 0,
  "proof_restart_allowed": false,
  "global_no_go_promoted": false,
  "claim_promotion_allowed": false,
  "first_obstruction": "No counted row supplies both source-clean payload and the family identity object required to route it as the relevant GU proof input.",
  "next_frontier_object": "ReceiptTransitionMatrixSourceCompletionQueue_V1",
  "companion_audit": "tests/hourly_20260625_0703_cycle3_receipt_transition_matrix_audit.py"
}
```
