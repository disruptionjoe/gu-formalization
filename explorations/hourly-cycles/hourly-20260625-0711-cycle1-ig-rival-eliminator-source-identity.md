---
title: "Hourly 20260625 0711 Cycle 1 IG Rival Eliminator Source Identity"
date: "2026-06-25"
run_id: "hourly-20260625-0711"
cycle: 1
lane: 3
doc_type: ig_rival_eliminator_source_identity
artifact_id: "IGRivalEliminatorSourceIdentity_0711_Cycle1_V1"
verdict: "BLOCKED_HOSTED_CANDIDATE_ZERO_ACCEPTED_RECEIPTS"
owned_path: "explorations/hourly-20260625-0711-cycle1-ig-rival-eliminator-source-identity.md"
companion_audit: "tests/hourly_20260625_0711_cycle1_ig_rival_eliminator_source_identity_audit.py"
---

# Hourly 20260625 0711 Cycle 1 IG Rival Eliminator Source Identity

## 1. Verdict

Verdict: **blocked / host**.

The acquired 2021 author manuscript does not emit
`ManuscriptRepresentationTheoryBianchiRivalEliminatorForShiab_V1`. It hosts a
strong Shiab candidate, and it explicitly points toward representation theory,
highest weights, and Bianchi identity as the historical selection route. But
the manuscript also says the original calculation/notes cannot be located, and
the checked formula windows do not supply the rival eliminators or family
identity needed to identify the displayed Shiab candidate with
`SourceForcedCodomainSelectorForK_IG`.

Decision state:

```text
required_object: SourceForcedCodomainSelectorForK_IG
missing_object: ManuscriptRepresentationTheoryBianchiRivalEliminatorForShiab_V1
candidate_status: hosted_strong_candidate_not_selected
accepted_receipt_count: 0
family_identity_status: failed_missing_witness
proof_restart_allowed: false
```

Do not promote `K_IG` selection from this manuscript surface.

## 2. What Was Derived Directly From Repo/Manuscript Sources

Repo posture/runbooks require a decision-grade gate and forbid turning
"hosted by" into "selected by". The 0601 synthesis identifies IG as blocked by
`ManuscriptRepresentationTheoryBianchiRivalEliminatorForShiab_V1`, with zero
accepted receipts and no proof restart. The prior IG identity packet and rival
matrix identify the candidate row as
`ManuscriptIGShiabCodomainCandidate_Sections5_8_9_Summary_V1` and the required
target object as `SourceForcedCodomainSelectorForK_IG`.

The local manuscript object was checked directly:

```text
manuscript_object_id: AcquiredAuthorManuscriptObject_V1:GU-MEDIA-2021-DRAFT-RELEASE
file: Geometric_UnityDraftApril1st2021.pdf
sha256: 3f28d742234a9841fc8e51ff172053200aa3eddf3ece38154a3328b9ebd186d4
page_count_observed: 69
tooling: pypdf text extraction plus Get-FileHash
```

Direct manuscript locators:

| locator | source-derived content | gate relevance |
| --- | --- | --- |
| Section 5.3-5.4, PDF p. 33 | `G = H semidirect N`, `N = Omega^1(ad(P_H))`, right/left actions on connections | IG ambient group/action context |
| Section 8, PDF pp. 41-42 | family of Shiab operators, invariant subspaces, operator-choice discussion | strongest source location for the missing selector calculation |
| Section 9.1, PDF pp. 43-44 | displayed Shiab map `Omega^2(Y,ad) -> Omega^{d-1}(Y,ad)` and Einstein/Ricci-like contraction formula | strongest typed candidate |
| Summary 12.1/12.4, PDF pp. 55-57 | redundancy removal, projection context, gauge-covariant Weyl-killing comparison | downstream consistency/context, not selector proof |
| Appendix, PDF pp. 65-66 | wedge, Hodge star, contraction, bracket, symmetric product, volume-form tools | construction toolkit, not a rival eliminator |

The decisive Section 8/9 facts are source-negative for this gate:

- PDF p. 42 says the Bianchi identity was able to choose the operator in
  different circumstances, but the old notes cannot be located.
- Footnote 10 on PDF p. 43 says the settled Shiab operator was chosen for
  Bianchi-identity properties, but again says it cannot now be located.
- PDF p. 43 displays a candidate Shiab formula and says it annihilates Weyl
  curvature, but does not prove uniqueness against rival operator classes.
- PDF p. 57 repeats the gauge-covariant Weyl-killing comparison, but it remains
  comparison/context rather than a selector-family identity proof.

## 3. Strongest Positive Construction Attempt

The strongest positive construction is:

1. Use Section 5.3-5.4 as the IG source environment: inhomogeneous gauge group,
   affine connection action, and augmented torsion context.
2. Use Section 8 as a source declaration that the author historically selected
   Shiab operators by representation-theory/highest-weight methods using the
   Bianchi identity.
3. Use Section 9.1 as the displayed candidate:
   `Shiab: Omega^2(Y,ad) -> Omega^{d-1}(Y,ad)`.
4. Use the Summary and appendix as evidence that projection, contraction,
   Hodge-star, bracket, symmetric-product, and Weyl-killing considerations are
   part of the intended Shiab workshop.
5. Try to normalize this candidate into the repo target
   `SourceForcedCodomainSelectorForK_IG`.

This succeeds only as a hosted-candidate construction:

```text
candidate_row_id: ManuscriptIGShiabCodomainCandidate_Sections5_8_9_Summary_V1
candidate_family: IG
candidate_map: Omega^2(Y,ad)->Omega^{d-1}(Y,ad)
positive_status: source-located typed Shiab candidate
negative_status: no source-emitted rival eliminator or family identity
```

Rival-class screen:

| rival class | manuscript-positive surface | source eliminator found? | status |
| --- | --- | ---: | --- |
| exterior/covariant derivative | curvature-form input makes this natural | no | survives |
| scalar/trace/divergence/coderivative | Einstein/Ricci comparison makes contraction natural | no | survives |
| symmetric derivative | not source-selected, but not excluded | no | survives |
| projected derivative | projection/removal context exists | no | survives |
| lower-order dressed class | torsion, gauge, curvature dressing is plausible | no | survives |
| displayed Shiab codomain | typed in Section 9.1 | no family-identity witness | hosted only |

The positive attempt therefore proves only that the manuscript is the right
place to look for the object. It does not prove that the object is present.

## 4. First Exact Obstruction Or Missing Object

The first exact obstruction is:

```text
missing source-emitted representation-theory/Bianchi rival eliminator selecting
the displayed Shiab candidate and identifying it with
SourceForcedCodomainSelectorForK_IG
```

Required missing object:

```text
ManuscriptRepresentationTheoryBianchiRivalEliminatorForShiab_V1
```

It must provide, from the manuscript or an accepted manuscript-adjacent primary
source:

- candidate/operator family under comparison;
- representation-theory/highest-weight or equivalent decomposition;
- Bianchi identity selection criterion;
- selected Shiab formula or family member;
- explicit bridge from the selected Shiab map to the `K_IG` codomain-selector
  schema;
- parent momentum degree;
- principal-symbol class;
- projector policy and projection-loss behavior;
- lower-order rigidity/freedom policy;
- eliminators for exterior/covariant derivative, scalar/divergence,
  symmetric-derivative, projected-derivative, and lower-order dressed rivals;
- family identity witness to `SourceForcedCodomainSelectorForK_IG`.

The manuscript checked here states that the relevant historical calculation is
absent. That makes the obstruction exact rather than merely unsearched.

## 5. Impact If Closed

If `ManuscriptRepresentationTheoryBianchiRivalEliminatorForShiab_V1` were
recovered and passed, the immediate impact would be narrow but important:

```text
accepted_receipt_count_would_be: 1
family_identity_status_would_be: passed
SourceForcedCodomainSelectorForK_IG_source_identity: available
proof_restart_possible_only_after_receipt_and_identity: true
downstream_physics_promoted_by_this_packet_alone: false
```

It would allow a family-limited IG proof restart gate to be considered. It
would not by itself prove theta/FLRW behavior, dark-energy recovery, QFT state
space, or any global GU claim.

## 6. Falsification/Demotion Condition

Demote the manuscript-Shiab route if any of these are established:

- the Section 8 operator-choice language is only retrospective commentary and
  not a recoverable source-side selector claim;
- the Section 9.1 Shiab operator is only an output/readout comparison map, not
  a `K_IG` selector candidate;
- the p. 57 Weyl-killing/gauge-covariance comparison is downstream motivation
  rather than a selector policy;
- a source-natural rival remains admissible after any recovered
  representation/Bianchi calculation is applied;
- the bridge from `Omega^2(Y,ad)->Omega^{d-1}(Y,ad)` to
  `SourceForcedCodomainSelectorForK_IG` imports target physics or repo
  preference rather than source identity.

Those conditions keep the row quarantined or turn this manuscript route into a
scoped fail. They do not establish a global IG or GU no-go.

## 7. Next Meaningful Proof/Source Step

The next meaningful step is source acquisition, not proof replay:

```text
next_object: PrimarySourceOrRecoveredNotes_BianchiHighestWeightShiabSelectorPacket_V1
```

Required contents:

1. image/text capture of the missing highest-weight/Bianchi calculation, or a
   source-equivalent reconstruction explicitly tied to the author manuscript;
2. typed inventory of all candidate Shiab operators in the family;
3. representation/Bianchi selection criterion;
4. per-rival eliminator table;
5. bridge into `SourceForcedCodomainSelectorForK_IG`;
6. independent family-identity check.

Until that object exists, keep `accepted_receipt_count = 0` and
`proof_restart_allowed = false`.

## 8. Machine-Readable JSON Summary

```json
{
  "artifact": "IGRivalEliminatorSourceIdentity_0711_Cycle1_V1",
  "object_id": "IGRivalEliminatorSourceIdentity_0711_Cycle1_V1:GU-MEDIA-2021-DRAFT-RELEASE:IG",
  "run_id": "hourly-20260625-0711",
  "cycle": 1,
  "lane": 3,
  "verdict": "BLOCKED_HOSTED_CANDIDATE_ZERO_ACCEPTED_RECEIPTS",
  "verdict_class": "blocked",
  "host_status": "hosted_candidate_not_selected",
  "family": "IG",
  "source_id": "GU-MEDIA-2021-DRAFT-RELEASE",
  "manuscript_object_id": "AcquiredAuthorManuscriptObject_V1:GU-MEDIA-2021-DRAFT-RELEASE",
  "manuscript_file": "Geometric_UnityDraftApril1st2021.pdf",
  "manuscript_sha256": "3f28d742234a9841fc8e51ff172053200aa3eddf3ece38154a3328b9ebd186d4",
  "manuscript_page_count_observed": 69,
  "source_tooling": [
    "Get-FileHash SHA256",
    "pypdf PdfReader text extraction"
  ],
  "required_object": "SourceForcedCodomainSelectorForK_IG",
  "searched_missing_object": "ManuscriptRepresentationTheoryBianchiRivalEliminatorForShiab_V1",
  "searched_missing_object_found": false,
  "candidate_row_id": "ManuscriptIGShiabCodomainCandidate_Sections5_8_9_Summary_V1",
  "candidate_status": "hosted_strong_candidate_not_selected",
  "candidate_map": "Omega^2(Y,ad)->Omega^{d-1}(Y,ad)",
  "candidate_locators": [
    "Section 5.3-5.4 PDF page 33",
    "Section 8 PDF pages 41-42",
    "Section 9.1 PDF pages 43-44",
    "Summary 12.1 and 12.4 PDF pages 55-57",
    "Appendix Other Elements of Shiab Constructions PDF pages 65-66"
  ],
  "source_positive_findings": [
    "inhomogeneous_gauge_group_and_connection_action_context",
    "Shiab_operator_family_and_operator_choice_discussion",
    "representation_theory_highest_weight_Bianchi_route_named",
    "typed_displayed_Shiab_candidate",
    "Weyl_killing_gauge_covariant_comparison",
    "appendix_lists_construction_tools"
  ],
  "source_negative_findings": [
    "historical_representation_theory_Bianchi_notes_not_located_in_manuscript",
    "no_explicit_rival_eliminator_table",
    "no_family_identity_witness_to_SourceForcedCodomainSelectorForK_IG",
    "no_projector_policy_or_projection_loss_behavior_for_K_IG_selector",
    "no_lower_order_rigidity_policy"
  ],
  "rival_classes": [
    {
      "id": "exterior_covariant_derivative",
      "label": "exterior/covariant derivative",
      "source_eliminator_found": false,
      "status": "survives"
    },
    {
      "id": "scalar_trace_divergence_coderivative",
      "label": "scalar/trace/divergence/coderivative",
      "source_eliminator_found": false,
      "status": "survives"
    },
    {
      "id": "symmetric_derivative",
      "label": "symmetric derivative",
      "source_eliminator_found": false,
      "status": "survives"
    },
    {
      "id": "projected_derivative",
      "label": "projected derivative",
      "source_eliminator_found": false,
      "status": "survives"
    },
    {
      "id": "lower_order_dressed_class",
      "label": "lower-order dressed class",
      "source_eliminator_found": false,
      "status": "survives"
    },
    {
      "id": "displayed_shiab_codomain",
      "label": "displayed Shiab codomain",
      "source_eliminator_found": false,
      "status": "hosted_candidate_not_selected"
    }
  ],
  "candidate_classes": [
    "ManuscriptIGShiabCodomainCandidate_Sections5_8_9_Summary_V1",
    "displayed_shiab_codomain",
    "exterior_covariant_derivative",
    "scalar_trace_divergence_coderivative",
    "symmetric_derivative",
    "projected_derivative",
    "lower_order_dressed_class"
  ],
  "all_rivals_eliminated_by_source": false,
  "accepted_receipts": [],
  "accepted_receipt_count": 0,
  "family_identity_status": "failed_missing_witness",
  "family_identity_checks_passed": 0,
  "proof_restart_allowed": false,
  "claim_promotion_allowed": false,
  "source_forced_K_IG_selection": false,
  "first_exact_obstruction": "missing source-emitted representation-theory/Bianchi rival eliminator selecting the displayed Shiab candidate and identifying it with SourceForcedCodomainSelectorForK_IG",
  "first_exact_obstruction_object": {
    "id": "ManuscriptRepresentationTheoryBianchiRivalEliminatorForShiab_V1",
    "missing": true,
    "obstruction_type": "missing_source_object",
    "must_provide": [
      "candidate_operator_family_under_comparison",
      "representation_theory_or_highest_weight_decomposition",
      "Bianchi_identity_selection_criterion",
      "selected_Shiab_formula_or_family_member",
      "bridge_to_SourceForcedCodomainSelectorForK_IG",
      "parent_momentum_degree",
      "principal_symbol_class",
      "projector_policy",
      "projection_loss_behavior",
      "lower_order_rigidity_policy",
      "exterior_covariant_derivative_eliminator",
      "scalar_trace_divergence_coderivative_eliminator",
      "symmetric_derivative_eliminator",
      "projected_derivative_eliminator",
      "lower_order_dressed_class_eliminator",
      "family_identity_to_SourceForcedCodomainSelectorForK_IG"
    ]
  },
  "impact_if_closed": {
    "accepted_receipt_count_would_be": 1,
    "family_identity_status_would_be": "passed",
    "proof_restart_possible_only_after_receipt_and_identity": true,
    "downstream_physics_promoted_by_packet_alone": false
  },
  "falsification_or_demotion_conditions": [
    "Section_8_operator_choice_language_is_not_a_recoverable_selector_claim",
    "Section_9_1_Shiab_is_readout_only_not_K_IG_selector_candidate",
    "Weyl_killing_gauge_covariance_is_downstream_motivation_only",
    "source_natural_rival_survives_recovered_rules",
    "bridge_to_SourceForcedCodomainSelectorForK_IG_imports_target_physics_or_repo_preference"
  ],
  "next_meaningful_step": "acquire or reconstruct the missing highest-weight/Bianchi Shiab selector calculation as a primary-source-tied packet and rerun rival elimination plus family identity",
  "next_object": "PrimarySourceOrRecoveredNotes_BianchiHighestWeightShiabSelectorPacket_V1"
}
```
