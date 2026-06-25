---
artifact: "IGSelectorRivalEliminatorMatrix_V1"
doc_type: ig_selector_rival_eliminator_matrix
run_id: "hourly-20260625-0601"
cycle: 2
lane: 1
verdict: "BLOCKED_HOSTED_CANDIDATE_ZERO_ACCEPTED_RECEIPTS"
owned_path: "explorations/hourly-20260625-0601-cycle2-ig-selector-rival-eliminator-matrix.md"
companion_audit: "tests/hourly_20260625_0601_cycle2_ig_selector_rival_eliminator_matrix_audit.py"
---

# IG Selector Rival-Eliminator Matrix

## 1. Verdict

Verdict: **blocked / host**.

The manuscript candidate hosts Shiab and a typed displayed Shiab codomain. It
does **not** source-force `SourceForcedCodomainSelectorForK_IG`, because the
source material available in the prior receipt-gate and identity-packet artifacts
does not emit the representation-theory/Bianchi/projection rival-eliminator rule
needed to select that codomain and reject competing source-natural operator
classes.

Normalized status:

```text
verdict_class: blocked
host_status: hosted_candidate_not_selected
required_object: SourceForcedCodomainSelectorForK_IG
accepted_receipt_count: 0
family_identity_checks_passed: 0
proof_restart_allowed: false
first_exact_missing_eliminator_object: ManuscriptRepresentationTheoryBianchiRivalEliminatorForShiab_V1
```

This is not a demotion of Shiab's presence in the manuscript. It is a refusal to
promote a hosted Shiab/codomain candidate into a source-forced IG selector.

## 2. Source Facts Read Directly

From
`explorations/hourly-20260625-0502-cycle2-author-manuscript-ig-selector-receipt-gate.md`:

- The source object is
  `AcquiredAuthorManuscriptObject_V1:GU-MEDIA-2021-DRAFT-RELEASE`, with
  `sha256:3f28d742234a9841fc8e51ff172053200aa3eddf3ece38154a3328b9ebd186d4`.
- The manuscript gives a strong IG/Shiab construction surface.
- Section 5.3-5.4 emits inhomogeneous gauge group action and augmented torsion
  construction data.
- Section 8, eqs. 8.1-8.7, is recorded as a family of Shiab operators,
  invariant-subspace basis, and operator-choice discussion.
- Section 9.1, eqs. 9.2-9.6, is recorded as a typed Shiab operator
  `Omega^2(Y, ad) -> Omega^{d-1}(Y, ad)` and an explicit Einstein-like formula.
- Summary eqs. 12.2-12.7 are recorded as projection-removal equations and
  comparison to Einstein-Ricci projection.
- The receipt gate records `accepted_receipt_count: 0` and
  `proof_restart_allowed: false`.

From
`explorations/hourly-20260625-0601-cycle1-author-manuscript-ig-selector-identity-packet.md`:

- The required object is `SourceForcedCodomainSelectorForK_IG`.
- The candidate row is
  `ManuscriptIGShiabCodomainCandidate_Sections5_8_9_Summary_V1`.
- The displayed Shiab surface is normalized as a candidate
  `Omega^2(Y, ad) -> Omega^{d-1}(Y, ad)`.
- The identity packet records the missing rule as a
  source-emitted representation-theory/Bianchi selection rule identifying the
  displayed Shiab codomain with `SourceForcedCodomainSelectorForK_IG`.
- Rival eliminators, projection-loss behavior, lower-order policy, and family
  identity are all recorded as missing.

From `process/runbooks/five-lane-frontier-run.md`:

- `blocked` means the repo lacks enough specified structure to evaluate the
  claim.
- `host` means the repo has room for the structure but does not derive or select
  it.
- The runbook forbids turning "compatible with" into "derived from" and
  "hosted by" into "selected by".

## 3. Strongest Positive Attempt

The strongest positive reading is:

1. Treat the manuscript's inhomogeneous gauge and torsion material as the source
   domain context for an IG witness family.
2. Treat Section 8 as the source location where a Shiab operator family and
   operator-choice discussion may have been intended to select a preferred
   object.
3. Treat Section 9.1 as the strongest typed codomain candidate:
   `Omega^2(Y, ad) -> Omega^{d-1}(Y, ad)`.
4. Treat the Summary projection-removal material as downstream evidence that the
   author cared about projection loss and Einstein/Ricci comparison.
5. Ask whether any source-emitted rule eliminates rival codomain/operator
   classes and therefore forces `SourceForcedCodomainSelectorForK_IG`.

The rival-eliminator matrix is:

| rival class | candidate shape tested | manuscript positive surface | manuscript eliminator found? | matrix status |
| --- | --- | --- | --- | --- |
| exterior derivative | exterior/covariant derivative class for a curvature-like IG witness | Shiab input is typed from `Omega^2(Y, ad)`, compatible with curvature-form input | no source-emitted rule excluding plain exterior/covariant derivative class | survives |
| scalar/divergence | scalar, trace, divergence, or coderivative contraction class | Einstein/Ricci-like comparison makes contraction-style readings source-natural | no representation/Bianchi rule excluding scalar, trace, divergence, or coderivative alternatives | survives |
| symmetric derivative | symmetric-gradient or strain-like derivative class | no direct positive selector, but still a source-natural rival until excluded | no source-emitted antisymmetry, Bianchi, or representation rule eliminating the class | survives |
| projected derivative | derivative followed by projection or projection-removal policy | Summary projection-removal equations supply downstream projection context | no projector policy selecting one projected class or proving projection-loss behavior for `K_IG` | survives |
| lower-order dressed classes | selected principal part plus algebraic, torsion, gauge, or curvature lower-order dressing | augmented torsion and group-action material make lower-order dressing plausible | no lower-order policy or normalization uniqueness rule | survives |
| displayed Shiab codomain | displayed Shiab candidate `Omega^2(Y, ad) -> Omega^{d-1}(Y, ad)` | strongest hosted codomain candidate in Section 9.1 and adjacent Shiab family material | source emits the candidate, but no rival eliminator or family identity to `SourceForcedCodomainSelectorForK_IG` | hosted candidate, not selected |

Positive result: the matrix identifies the displayed Shiab codomain as the best
hosted candidate and the only row with a directly typed manuscript codomain. It
does not accept the row, because no rival class is eliminated by a source-emitted
selector rule.

## 4. First Exact Obstruction

The first exact obstruction is the missing source object:

```text
ManuscriptRepresentationTheoryBianchiRivalEliminatorForShiab_V1
```

This object must emit, from the manuscript or manuscript-adjacent source packet:

- a representation-theory, highest-weight, Bianchi, or equivalent selection
  criterion;
- the selected Shiab formula or family member;
- the selected `K_IG` codomain or an explicit bridge from the Shiab
  input/output type to the `K_IG` selector schema;
- a projector policy and projection-loss behavior;
- a lower-order freedom policy;
- explicit eliminators for exterior derivative, scalar/divergence, symmetric
  derivative, projected derivative, and lower-order dressed rival classes;
- a family identity witness to `SourceForcedCodomainSelectorForK_IG`.

Until this object exists, the manuscript row remains a hosted candidate, not an
accepted selector receipt.

## 5. Impact If Closed

If `ManuscriptRepresentationTheoryBianchiRivalEliminatorForShiab_V1` were
recovered and checked, the manuscript row could be upgraded from a quarantined
or blocked hosted candidate to a conditional or accepted IG selector receipt.

The immediate impact would be narrow:

- `accepted_receipt_count` for this matrix would become `1`.
- `family_identity_checks_passed` would become `1`.
- `SourceForcedCodomainSelectorForK_IG` would have a source-side selector
  candidate with rival eliminators.
- IG proof restart could become allowed only after the receipt and family
  identity are both accepted.

It would not by itself prove the downstream physical recovery. It would close
the codomain/operator selector gate that currently blocks that proof path.

## 6. Falsification/Demotion Condition

Demote or falsify the hosted-candidate reading if any of the following is
established:

- Section 8 does not actually contain a representation-theory, highest-weight,
  Bianchi, invariant-subspace, or operator-choice surface.
- The Section 9.1 Shiab operator is only a readout or comparison map and is not
  intended as a `K_IG` selector candidate.
- The Summary projection-removal equations are only downstream physical
  comparison and supply no selector-relevant projection policy.
- A source-natural rival class remains admissible even after all recovered
  representation/Bianchi/projection rules are applied.
- The displayed Shiab codomain cannot be bridged into the
  `SourceForcedCodomainSelectorForK_IG` schema without importing a non-source
  assumption.

## 7. Next Meaningful Source/Proof Computation

Run a formula-window extraction and comparison proof task:

1. Re-extract Section 8 eqs. 8.1-8.7, Section 9.1 eqs. 9.2-9.6, and Summary
   eqs. 12.2-12.7 from the acquired manuscript object.
2. Build a typed operator-family inventory: domain, codomain, principal symbol,
   projector, lower-order terms, and required geometric data.
3. For each rival class in this matrix, search only for source-emitted
   eliminators: representation decomposition, Bianchi identity, projection
   policy, uniqueness/normalization rule, or explicit exclusion.
4. If all rival eliminators and the family identity are present, promote the
   object to receipt review.
5. If any eliminator remains missing, keep `accepted_receipt_count: 0` and route
   the next source task to the missing representation-theory/Bianchi calculation
   packet.

## 8. Machine-Readable JSON Summary

```json
{
  "artifact": "IGSelectorRivalEliminatorMatrix_V1",
  "object_id": "IGSelectorRivalEliminatorMatrix_V1:GU-MEDIA-2021-DRAFT-RELEASE:IG",
  "run_id": "hourly-20260625-0601",
  "cycle": 2,
  "lane": 1,
  "artifact_identity": {
    "artifact_id": "IGSelectorRivalEliminatorMatrix_V1",
    "owned_path": "explorations/hourly-20260625-0601-cycle2-ig-selector-rival-eliminator-matrix.md",
    "companion_audit": "tests/hourly_20260625_0601_cycle2_ig_selector_rival_eliminator_matrix_audit.py"
  },
  "verdict": "BLOCKED_HOSTED_CANDIDATE_ZERO_ACCEPTED_RECEIPTS",
  "verdict_class": "blocked",
  "host_status": "hosted_candidate_not_selected",
  "family": "IG",
  "source_id": "GU-MEDIA-2021-DRAFT-RELEASE",
  "manuscript_object_id": "AcquiredAuthorManuscriptObject_V1:GU-MEDIA-2021-DRAFT-RELEASE",
  "manuscript_sha256": "3f28d742234a9841fc8e51ff172053200aa3eddf3ece38154a3328b9ebd186d4",
  "required_object": "SourceForcedCodomainSelectorForK_IG",
  "candidate_row_id": "ManuscriptIGShiabCodomainCandidate_Sections5_8_9_Summary_V1",
  "candidate_status": "hosted_strong_candidate_not_selected",
  "displayed_shiab_codomain": "Omega^2(Y,ad)->Omega^{d-1}(Y,ad)",
  "accepted_receipts": [],
  "accepted_receipt_count": 0,
  "family_identity_checks_passed": 0,
  "proof_restart_allowed": false,
  "claim_promotion_allowed": false,
  "source_facts": [
    "Section_5_3_5_4_inhomogeneous_gauge_group_action_and_augmented_torsion",
    "Section_8_eqs_8_1_8_7_Shiab_operator_family_invariant_subspace_operator_choice_surface",
    "Section_9_1_eqs_9_2_9_6_typed_Shiab_operator_Omega2_to_Omega_d_minus_1",
    "Summary_eqs_12_2_12_7_projection_removal_Einstein_Ricci_comparison",
    "prior_receipt_gate_zero_accepted_receipts",
    "prior_identity_packet_missing_source_emitted_representation_theory_Bianchi_selection_rule"
  ],
  "rival_classes": [
    {
      "id": "exterior_derivative",
      "label": "exterior derivative",
      "candidate_shape": "exterior_or_covariant_derivative_class_for_curvature_like_IG_witness",
      "positive_surface": "Shiab_input_typed_from_Omega2_Y_ad_is_compatible_with_curvature_form_input",
      "manuscript_eliminator_found": false,
      "status": "survives"
    },
    {
      "id": "scalar_divergence",
      "label": "scalar/divergence",
      "candidate_shape": "scalar_trace_divergence_or_coderivative_contraction_class",
      "positive_surface": "Einstein_Ricci_like_comparison_makes_contraction_style_readings_source_natural",
      "manuscript_eliminator_found": false,
      "status": "survives"
    },
    {
      "id": "symmetric_derivative",
      "label": "symmetric derivative",
      "candidate_shape": "symmetric_gradient_or_strain_like_derivative_class",
      "positive_surface": "no_direct_positive_selector_but_not_excluded_by_source_rules",
      "manuscript_eliminator_found": false,
      "status": "survives"
    },
    {
      "id": "projected_derivative",
      "label": "projected derivative",
      "candidate_shape": "derivative_followed_by_projection_or_projection_removal_policy",
      "positive_surface": "Summary_projection_removal_equations_supply_downstream_projection_context",
      "manuscript_eliminator_found": false,
      "status": "survives"
    },
    {
      "id": "lower_order_dressed_classes",
      "label": "lower-order dressed classes",
      "candidate_shape": "selected_principal_part_plus_algebraic_torsion_gauge_or_curvature_lower_order_dressing",
      "positive_surface": "augmented_torsion_and_group_action_material_make_lower_order_dressing_plausible",
      "manuscript_eliminator_found": false,
      "status": "survives"
    },
    {
      "id": "displayed_shiab_codomain",
      "label": "displayed Shiab codomain",
      "candidate_shape": "Omega^2(Y,ad)->Omega^{d-1}(Y,ad)",
      "positive_surface": "strongest_hosted_codomain_candidate_in_Section_9_1_and_adjacent_Shiab_family_material",
      "manuscript_eliminator_found": false,
      "status": "hosted_candidate_not_selected"
    }
  ],
  "all_rivals_eliminated_by_source": false,
  "first_exact_obstruction": "missing source-emitted representation-theory/Bianchi/projection rival-eliminator object selecting the displayed Shiab codomain and eliminating rival codomain/operator classes for SourceForcedCodomainSelectorForK_IG",
  "first_exact_missing_eliminator_object": {
    "id": "ManuscriptRepresentationTheoryBianchiRivalEliminatorForShiab_V1",
    "missing": true,
    "obstruction_type": "missing_source_object",
    "must_provide": [
      "representation_theory_or_highest_weight_selector",
      "Bianchi_identity_selection_criterion",
      "selected_Shiab_formula_or_family_member",
      "selected_K_IG_codomain_or_bridge",
      "projector_policy",
      "projection_loss_behavior",
      "lower_order_freedom_policy",
      "exterior_derivative_eliminator",
      "scalar_divergence_eliminator",
      "symmetric_derivative_eliminator",
      "projected_derivative_eliminator",
      "lower_order_dressed_class_eliminator",
      "family_identity_to_SourceForcedCodomainSelectorForK_IG"
    ]
  },
  "impact_if_closed": {
    "accepted_receipt_count_would_be": 1,
    "family_identity_checks_passed_would_be": 1,
    "proof_restart_possible_only_after_receipt_and_identity": true,
    "downstream_physics_promoted_by_matrix_alone": false
  },
  "falsification_or_demotion_conditions": [
    "Section_8_lacks_operator_choice_or_representation_Bianchi_surface",
    "Section_9_1_Shiab_is_readout_only_not_K_IG_selector_candidate",
    "Summary_projection_removal_is_downstream_only",
    "source_natural_rival_class_survives_after_recovered_rules",
    "bridge_to_SourceForcedCodomainSelectorForK_IG_requires_imported_non_source_assumption"
  ],
  "next_meaningful_step": "re-extract Section 8, Section 9.1, and Summary formula windows, then test each rival class for a source-emitted representation-theory, Bianchi, projection, uniqueness, or lower-order eliminator"
}
```
