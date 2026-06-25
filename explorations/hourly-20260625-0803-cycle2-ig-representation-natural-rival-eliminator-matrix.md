---
title: "Hourly 20260625 0803 Cycle 2 IG Representation-Natural Rival Eliminator Matrix"
date: "2026-06-25"
run_id: "hourly-20260625-0803"
cycle: 2
lane: 2
doc_type: ig_representation_natural_rival_eliminator_matrix
artifact_id: "CombinedSourceRepresentationTheoryBianchiRivalEliminatorForK_IG_V1"
verdict: "BLOCKED_MATRIX_BUILT_ZERO_SOURCE_NATURAL_RIVAL_ELIMINATIONS"
owned_path: "explorations/hourly-20260625-0803-cycle2-ig-representation-natural-rival-eliminator-matrix.md"
companion_audit: "tests/hourly_20260625_0803_cycle2_ig_representation_natural_rival_eliminator_matrix_audit.py"
---

# Hourly 20260625 0803 Cycle 2 IG Representation-Natural Rival Eliminator Matrix

## 1. Verdict

Verdict: **blocked**.

This artifact builds
`CombinedSourceRepresentationTheoryBianchiRivalEliminatorForK_IG_V1` as a
decision matrix, but it does not close the selector gate. The assigned sources
support a source-motivated search for a Shiab/Bianchi/highest-weight selector.
They do not supply a source-natural criterion that selects the `K_IG` codomain
selector and eliminates representation-natural rival classes without target
import.

Decision state:

```text
artifact: CombinedSourceRepresentationTheoryBianchiRivalEliminatorForK_IG_V1
required_object: SourceForcedCodomainSelectorForK_IG
matrix_status: built_as_blocking_inventory_not_acceptance_receipt
verdict_class: blocked
source_natural_eliminations_today: 0
all_representation_natural_rivals_eliminated: false
accepted_selector_packet_count: 0
accepted_receipt_count: 0
accepted_for_routing_count: 0
family_identity_status: failed_missing_witness
target_import_selector_detected: false
target_import_selector_allowed: false
proof_restart_allowed: false
claim_promotion_allowed: false
```

The key distinction is now explicit: Shiab exists in the Cl(9,5) canon, and the
sources motivate a Shiab-like middle map, but existence is not selection. A
source-natural Bianchi/highest-weight criterion has not yet selected the
`K_IG` codomain selector against rival operators.

## 2. Specific GU Claim or Bridge Under Test

Bridge under test:

```text
source-side representation/highest-weight/Bianchi structure
  -> selection of a unique or controlled Shiab/projection/contraction operator
  -> elimination of all representation-natural rivals
  -> family identity to SourceForcedCodomainSelectorForK_IG
```

Acceptance would require all of the following from primary sources, recovered
notes, or a source-equivalent reconstruction that does not use downstream
physics to choose the answer:

- a candidate operator family under comparison;
- a representation-theory or highest-weight decomposition;
- a Bianchi identity selection criterion;
- the selected Shiab/projection/contraction formula or family member;
- principal symbol class and parent momentum degree;
- projector policy and projection-loss behavior;
- lower-order rigidity policy;
- eliminators for every representation-natural rival class;
- formula identity among manuscript, Oxford, PTUJ/Keating, and UCSD surfaces
  when those surfaces are used as evidence;
- family identity to `SourceForcedCodomainSelectorForK_IG`;
- a target-import screen proving that the selected source object was not chosen
  by dark-energy, generation-count, QFT, FLRW, or other target success data.

## 3. Sources Read First

Required sources read first:

| source | direct contribution to this gate |
| --- | --- |
| `RESEARCH-POSTURE.md` | Requires truth-tracking discipline and forbids converting compatibility, hosted structure, or target agreement into derivation. |
| `process/runbooks/five-lane-frontier-run.md` | Requires decision-grade verdict, exact obstruction, and consistent use of blocked/fail/no-go vocabulary. |
| `explorations/hourly-20260625-0803-cycle1-ig-bianchi-highest-weight-selector-packet-gate.md` | Incoming cycle-1 state: source-motivated selector shell, zero accepted selector packets, missing combined rival eliminator. |
| `explorations/hourly-20260625-0711-cycle1-ig-rival-eliminator-source-identity.md` | Manuscript hosts a strong Shiab candidate and names representation/highest-weight/Bianchi history, but the notes are absent. |
| `explorations/hourly-20260625-0711-cycle2-ig-visual-manuscript-selector-bridge.md` | Manuscript, Oxford, and PTUJ/Keating triangulate a candidate vicinity but not a selector proof. |
| `canon/shiab-existence-cl95.md` | Establishes a natural Cl(9,5) Shiab operator exists, while explicitly leaving uniqueness of equivariant maps open. |
| `literature/weinstein-ucsd-2025-04-transcript.md` | Supplies current Bianchi/contraction/omega-one-to-omega-d-minus-one motivation and the middle-map problem, not a rival eliminator. |

Direct implications:

- The canon existence result is usable as existence background only.
- The UCSD transcript strengthens the search target around Bianchi identity,
  Einstein-style contraction, and the missing middle map.
- The manuscript/Oxford/PTUJ surfaces remain candidate/locator surfaces unless
  the representation-theory selector calculation is recovered or reconstructed.

## 4. Candidate/Rival Family Matrix

The matrix below treats "representation-natural" broadly: rivals are included
when the assigned sources make them natural from curvature forms, contraction,
Hodge/star analogies, projection language, symmetric products, lower-order
dressing freedom, or formula-surface ambiguity.

| row id | candidate/rival family | source-natural reason | eliminator field required | source-natural eliminator found today? | status today |
| --- | --- | --- | --- | ---: | --- |
| `displayed_or_canon_shiab_clifford_contraction` | Cl(9,5) Shiab/Clifford contraction candidate | Canon proves a natural equivariant map exists; manuscript/UCSD motivate a Shiab middle map. | multiplicity/uniqueness or Bianchi highest-weight selection plus identity to `K_IG` | no | hosted/canon-exists, not selected |
| `exterior_covariant_derivative` | exterior/covariant derivative family | UCSD and manuscript work in curvature-form and minimally coupled exterior-derivative context. | representation/Bianchi rule excluding direct derivative-type rivals as codomain selector | no | live |
| `einstein_ricci_contraction_analog` | Einstein/Ricci-style contraction family | UCSD emphasizes Einstein's contraction from curvature to one-form-like/gauge-potential-like data. | source rule distinguishing Shiab from contraction-only analogs | no | live |
| `hodge_star_or_dimension_shift_analog` | Hodge/star or dimension-shift analog | UCSD frames Einstein as making a four-manifold behave like a three-dimensional Hodge-star route. | dimension/signature/representation criterion ruling out star-like alternatives | no | live |
| `symmetric_product_or_derivative` | symmetric product or symmetric derivative family | Manuscript appendix and prior packets identify symmetric-product tools in the Shiab workshop. | highest-weight decomposition showing symmetric branch cannot satisfy the Bianchi selector | no | live |
| `projection_dependent_shiab_variant` | projection-dependent Shiab variants | PTUJ/Keating and prior bridge name Shiab Projection, but not its exact projector policy. | intrinsic projector, loss behavior, and selected projected formula | no | live |
| `lower_order_dressed_variant` | lower-order dressed or torsion/gauge-deformed variants | IG machinery permits gauge, torsion, and curvature dressing unless source rigidity forbids it. | lower-order rigidity theorem or source-side normalization rule | no | live |
| `oxford_visual_formula_variant` | Oxford 02:33:43 visual formula variant | Official visual frame is a verified Shiab-like formula candidate with typography uncertainty. | formula identity to manuscript/canon/notes selector, or controlled non-identity | no | blocked by identity witness |
| `ptuj_missing_sheet_variant` | PTUJ/Keating missing-sheet variant | Locator points to representation/projection calculations on a missing Shiab Projection sheet. | recovered sheet or source-equivalent calculation, then identity test | no | blocked by missing asset/notes |
| `ucsd_middle_map_variant` | UCSD omega-one to omega-d-minus-one middle-map variant | UCSD names the middle-map problem and the Shiab operator role in the rolled-up complex. | explicit UCSD formula or source-equivalent selector calculation tied to `K_IG` | no | motivated but under-specified |

Matrix result:

```text
candidate_rows_considered: 10
source_natural_rival_rows: 9
source_natural_eliminations_today: 0
selected_K_IG_codomain_selector_today: false
```

The matrix therefore consumes cycle 1's blocker by making the rival family and
required eliminator fields explicit. It does not remove the blocker.

## 5. Strongest Positive Eliminator Attempt

The strongest positive attempt is a three-step eliminator:

1. Use `canon/shiab-existence-cl95.md` to secure a natural real Shiab/Clifford
   contraction in the Cl(9,5) setting, avoiding the old complexification gap.
2. Use UCSD 2025 to motivate why a curvature-to-one-form or
   omega-one-to-omega-d-minus-one middle map is structurally central: the
   Bianchi identity gives automatic divergence-free structure, Einstein's
   contraction is a guiding analogy, and the rolled-up complex needs a middle
   operator.
3. Use the 2021 manuscript, Oxford visual frame, and PTUJ/Keating locator as
   source surfaces that point toward a historical representation/highest-weight
   Bianchi calculation selecting a Shiab/projection operator.

This attempt reaches:

```text
positive_result: source_natural_candidate_family_and_required_eliminator_fields_identified
shiab_existence_status: canon_in_Cl95_setting
selector_status: not_source_forced
eliminator_status: not_obtained
```

The attempt fails as a selector proof for one exact reason: the source-natural
criterion is not present. The canon file itself warns that uniqueness of
equivariant maps is open. The manuscript states the historical calculation is
not located. The visual and PTUJ surfaces are candidates/locators. UCSD provides
motivation and analogy, not an executable highest-weight eliminator.

## 6. First Exact Obstruction or Missing Object

The first exact obstruction is not the absence of Shiab. It is the absence of a
source-natural selector theorem:

```text
SourceNaturalBianchiHighestWeightSelectorTheoremForK_IG_V1 is missing.
```

This is the exact next object inside the broader combined matrix. It must
provide:

- the full source-natural operator family under comparison;
- the representation or highest-weight decomposition;
- the Bianchi identity condition as a selection rule;
- the selected formula or controlled selected family;
- multiplicity of relevant equivariant hom-spaces, especially whether the Cl(9,5)
  Shiab/Clifford contraction is unique or one of several maps;
- principal symbol class;
- parent momentum degree;
- projector policy;
- projection-loss behavior;
- lower-order rigidity policy;
- per-rival eliminators for every row in the matrix above;
- source-surface identity rules for manuscript, Oxford, PTUJ/Keating, and UCSD;
- family identity to `SourceForcedCodomainSelectorForK_IG`;
- a target-import screen.

Until that theorem, recovered source packet, or sharper successor exists, the
combined matrix remains a blocking inventory rather than an accepted receipt.

## 7. Impact if Closed

If the missing selector theorem closed, the impact would be significant but
scoped:

```text
accepted_selector_packet_count_would_be: 1
accepted_receipt_count_would_be: 1
accepted_for_routing_count_would_be: 1
source_natural_eliminations_would_equal_rival_rows: true
family_identity_status_would_be: passed
SourceForcedCodomainSelectorForK_IG_source_identity_available: true
proof_restart_possible_only_after_receipt_identity_and_rival_elimination: true
downstream_physics_promoted_by_packet_alone: false
```

Closure would allow a family-limited `K_IG` proof-restart readiness review. It
would not by itself prove the cosmological sector, dark-energy formula, FLRW
reduction, generation count, QFT extraction, or a global GU claim.

## 8. Falsification/Demotion Condition

Demote this source route from blocked to scoped fail if a complete source or
source-equivalent reconstruction establishes any of the following:

- the representation/highest-weight/Bianchi calculation selects a rival instead
  of the `K_IG` codomain selector;
- the relevant equivariant hom-space has multiple source-natural maps and no
  source-side rule distinguishes them;
- a derivative, contraction, Hodge/star, symmetric, projected, dressed, Oxford,
  PTUJ, or UCSD middle-map rival remains admissible after the recovered rule is
  applied;
- the Cl(9,5) Shiab/Clifford contraction is merely an existence witness and not
  the source-selected operator;
- the manuscript and Oxford formulas are not source-identical or controlled
  members of the same family;
- the PTUJ/Keating sheet is unrecovered, non-formula, or about a different
  object after source acquisition is exhausted;
- identity to `SourceForcedCodomainSelectorForK_IG` requires target physics,
  downstream success data, or repo preference.

Those demotion conditions are route-local. They would not prove a global IG or
GU no-go.

## 9. Next Meaningful Proof/Source Step

Next object:

```text
SourceNaturalBianchiHighestWeightSelectorTheoremForK_IG_V1
```

Next meaningful step:

1. Compute or recover the representation/highest-weight decomposition of the
   source-natural Shiab/projection/contraction candidate family.
2. Determine the multiplicity of the relevant equivariant hom-space containing
   the Cl(9,5) Shiab/Clifford contraction.
3. State the Bianchi identity criterion as an operator-selection rule.
4. Apply the rule row-by-row to the rival matrix above.
5. Only after every rival is eliminated, test family identity to
   `SourceForcedCodomainSelectorForK_IG`.

Until then:

```text
accepted_selector_packet_count: 0
accepted_receipt_count: 0
proof_restart_allowed: false
```

## 10. Machine-readable JSON summary

```json
{
  "artifact": "CombinedSourceRepresentationTheoryBianchiRivalEliminatorForK_IG_V1",
  "artifact_id": "CombinedSourceRepresentationTheoryBianchiRivalEliminatorForK_IG_V1",
  "run_id": "hourly-20260625-0803",
  "cycle": 2,
  "lane": 2,
  "verdict": "BLOCKED_MATRIX_BUILT_ZERO_SOURCE_NATURAL_RIVAL_ELIMINATIONS",
  "verdict_class": "blocked",
  "owned_path": "explorations/hourly-20260625-0803-cycle2-ig-representation-natural-rival-eliminator-matrix.md",
  "companion_audit": "tests/hourly_20260625_0803_cycle2_ig_representation_natural_rival_eliminator_matrix_audit.py",
  "family": "IG",
  "required_object": "SourceForcedCodomainSelectorForK_IG",
  "matrix_status": "built_as_blocking_inventory_not_acceptance_receipt",
  "sources_read_first": [
    "RESEARCH-POSTURE.md",
    "process/runbooks/five-lane-frontier-run.md",
    "explorations/hourly-20260625-0803-cycle1-ig-bianchi-highest-weight-selector-packet-gate.md",
    "explorations/hourly-20260625-0711-cycle1-ig-rival-eliminator-source-identity.md",
    "explorations/hourly-20260625-0711-cycle2-ig-visual-manuscript-selector-bridge.md",
    "canon/shiab-existence-cl95.md",
    "literature/weinstein-ucsd-2025-04-transcript.md"
  ],
  "claim_under_test": "source_side_representation_highest_weight_Bianchi_structure_selects_K_IG_codomain_selector_and_eliminates_representation_natural_rivals_without_target_import",
  "shiab_existence_status": "canon_exists_in_Cl95_setting",
  "shiab_existence_sufficient_for_selection": false,
  "canon_open_uniqueness_issue": true,
  "candidate_rows_considered": 10,
  "source_natural_rival_rows": 9,
  "candidate_rival_family_matrix": [
    {
      "id": "displayed_or_canon_shiab_clifford_contraction",
      "family": "Cl95_Shiab_Clifford_contraction_candidate",
      "source_natural_reason": "canon_proves_natural_equivariant_map_exists_and_sources_motivate_Shiab_middle_map",
      "required_eliminator_field": "multiplicity_uniqueness_or_Bianchi_highest_weight_selection_plus_identity_to_K_IG",
      "source_natural_eliminator_found": false,
      "status": "hosted_or_canon_exists_not_selected"
    },
    {
      "id": "exterior_covariant_derivative",
      "family": "exterior_or_covariant_derivative",
      "source_natural_reason": "curvature_form_and_minimally_coupled_exterior_derivative_context",
      "required_eliminator_field": "representation_Bianchi_rule_excluding_direct_derivative_type_rivals",
      "source_natural_eliminator_found": false,
      "status": "live_not_eliminated"
    },
    {
      "id": "einstein_ricci_contraction_analog",
      "family": "Einstein_Ricci_style_contraction",
      "source_natural_reason": "UCSD_emphasizes_Einstein_contraction_from_curvature_to_one_form_like_data",
      "required_eliminator_field": "source_rule_distinguishing_Shiab_from_contraction_only_analogs",
      "source_natural_eliminator_found": false,
      "status": "live_not_eliminated"
    },
    {
      "id": "hodge_star_or_dimension_shift_analog",
      "family": "Hodge_star_or_dimension_shift_analog",
      "source_natural_reason": "UCSD_frames_Einstein_as_four_manifold_analog_of_three_dimensional_Hodge_star_route",
      "required_eliminator_field": "dimension_signature_representation_criterion_ruling_out_star_like_alternatives",
      "source_natural_eliminator_found": false,
      "status": "live_not_eliminated"
    },
    {
      "id": "symmetric_product_or_derivative",
      "family": "symmetric_product_or_symmetric_derivative",
      "source_natural_reason": "manuscript_appendix_and_prior_packets_identify_symmetric_product_tools",
      "required_eliminator_field": "highest_weight_decomposition_showing_symmetric_branch_cannot_satisfy_Bianchi_selector",
      "source_natural_eliminator_found": false,
      "status": "live_not_eliminated"
    },
    {
      "id": "projection_dependent_shiab_variant",
      "family": "projection_dependent_Shiab_variants",
      "source_natural_reason": "PTUJ_Keating_and_prior_bridge_name_Shiab_Projection_without_exact_projector_policy",
      "required_eliminator_field": "intrinsic_projector_loss_behavior_and_selected_projected_formula",
      "source_natural_eliminator_found": false,
      "status": "live_not_eliminated"
    },
    {
      "id": "lower_order_dressed_variant",
      "family": "lower_order_dressed_or_torsion_gauge_deformed_variants",
      "source_natural_reason": "IG_machinery_permits_gauge_torsion_and_curvature_dressing_unless_source_rigidity_forbids_it",
      "required_eliminator_field": "lower_order_rigidity_theorem_or_source_side_normalization_rule",
      "source_natural_eliminator_found": false,
      "status": "live_not_eliminated"
    },
    {
      "id": "oxford_visual_formula_variant",
      "family": "Oxford_023343_visual_formula_variant",
      "source_natural_reason": "official_visual_frame_is_verified_Shiab_like_formula_candidate_with_typography_uncertainty",
      "required_eliminator_field": "formula_identity_to_manuscript_canon_notes_selector_or_controlled_non_identity",
      "source_natural_eliminator_found": false,
      "status": "blocked_missing_identity_witness"
    },
    {
      "id": "ptuj_missing_sheet_variant",
      "family": "PTUJ_Keating_missing_sheet_variant",
      "source_natural_reason": "locator_points_to_representation_projection_calculations_on_missing_Shiab_Projection_sheet",
      "required_eliminator_field": "recovered_sheet_or_source_equivalent_calculation_then_identity_test",
      "source_natural_eliminator_found": false,
      "status": "blocked_missing_asset_or_notes"
    },
    {
      "id": "ucsd_middle_map_variant",
      "family": "UCSD_omega_one_to_omega_d_minus_one_middle_map_variant",
      "source_natural_reason": "UCSD_names_middle_map_problem_and_Shiab_operator_role_in_rolled_up_complex",
      "required_eliminator_field": "explicit_UCSD_formula_or_source_equivalent_selector_calculation_tied_to_K_IG",
      "source_natural_eliminator_found": false,
      "status": "motivated_but_under_specified"
    }
  ],
  "rival_coverage_required_ids": [
    "displayed_or_canon_shiab_clifford_contraction",
    "exterior_covariant_derivative",
    "einstein_ricci_contraction_analog",
    "hodge_star_or_dimension_shift_analog",
    "symmetric_product_or_derivative",
    "projection_dependent_shiab_variant",
    "lower_order_dressed_variant",
    "oxford_visual_formula_variant",
    "ptuj_missing_sheet_variant",
    "ucsd_middle_map_variant"
  ],
  "source_natural_eliminations_today": 0,
  "all_representation_natural_rivals_eliminated": false,
  "selected_K_IG_codomain_selector_today": false,
  "accepted_selector_packets": [],
  "accepted_selector_packet_count": 0,
  "accepted_receipts": [],
  "accepted_receipt_count": 0,
  "accepted_for_routing_count": 0,
  "family_identity_status": "failed_missing_witness",
  "family_identity_checks_passed": 0,
  "source_forced_K_IG_selection": false,
  "proof_restart_allowed": false,
  "claim_promotion_allowed": false,
  "strongest_positive_eliminator_attempt": {
    "status": "source_natural_candidate_family_and_required_eliminator_fields_identified",
    "uses_canon_shiab_existence": true,
    "uses_ucsd_bianchi_contraction_middle_map_motivation": true,
    "uses_manuscript_oxford_ptuj_selector_locator_triangle": true,
    "selector_status": "not_source_forced",
    "eliminator_status": "not_obtained"
  },
  "first_exact_obstruction": {
    "id": "SourceNaturalBianchiHighestWeightSelectorTheoremForK_IG_V1",
    "status": "missing",
    "obstruction_type": "missing_source_natural_selector_theorem",
    "description": "Shiab existence and source motivation do not provide a Bianchi/highest-weight rule that selects the K_IG codomain selector and eliminates representation-natural rivals.",
    "within_broader_artifact": "CombinedSourceRepresentationTheoryBianchiRivalEliminatorForK_IG_V1",
    "blocks_acceptance_for": "SourceForcedCodomainSelectorForK_IG",
    "blocks_proof_restart": true,
    "must_provide": [
      "full_source_natural_operator_family_under_comparison",
      "representation_or_highest_weight_decomposition",
      "Bianchi_identity_selection_rule",
      "selected_formula_or_controlled_selected_family",
      "equivariant_hom_space_multiplicity",
      "principal_symbol_class",
      "parent_momentum_degree",
      "projector_policy",
      "projection_loss_behavior",
      "lower_order_rigidity_policy",
      "per_rival_eliminators_for_matrix_rows",
      "source_surface_identity_rules",
      "family_identity_to_SourceForcedCodomainSelectorForK_IG",
      "target_import_screen"
    ]
  },
  "target_import_screen": {
    "target_data_seen": [],
    "target_import_detected": false,
    "target_import_selector_detected": false,
    "target_import_selector_allowed": false,
    "target_import_clean": true,
    "target_import_clean_sufficient_for_acceptance": false,
    "downstream_physics_used_to_select_source_object": false,
    "target_imported_physics_recorded": []
  },
  "proof_restart_rule": {
    "allowed_if": "accepted_selector_packet_count_gt_0_and_family_identity_status_passed_and_all_representation_natural_rivals_eliminated_and_target_import_selector_detected_false",
    "accepted_selector_packet_condition": false,
    "family_identity_condition": false,
    "rival_elimination_condition": false,
    "target_import_condition": true,
    "proof_restart_allowed": false
  },
  "impact_if_closed": {
    "accepted_selector_packet_count_would_be": 1,
    "accepted_receipt_count_would_be": 1,
    "accepted_for_routing_count_would_be": 1,
    "source_natural_eliminations_would_equal_rival_rows": true,
    "family_identity_status_would_be": "passed",
    "SourceForcedCodomainSelectorForK_IG_source_identity_available": true,
    "proof_restart_possible_only_after_receipt_identity_and_rival_elimination": true,
    "downstream_physics_promoted_by_packet_alone": false
  },
  "falsification_or_demotion_conditions": [
    "representation_highest_weight_Bianchi_calculation_selects_a_rival_instead_of_K_IG_codomain_selector",
    "relevant_equivariant_hom_space_has_multiple_source_natural_maps_and_no_source_side_rule_distinguishes_them",
    "any_derivative_contraction_hodge_symmetric_projected_dressed_oxford_ptuj_or_ucsd_middle_map_rival_remains_admissible_after_recovered_rule",
    "Cl95_Shiab_Clifford_contraction_is_existence_witness_only_not_source_selected_operator",
    "manuscript_and_Oxford_formulas_are_not_source_identical_or_controlled_family_members",
    "PTUJ_Keating_sheet_unrecovered_non_formula_or_different_object_after_source_acquisition_exhausted",
    "identity_to_SourceForcedCodomainSelectorForK_IG_requires_target_physics_downstream_success_data_or_repo_preference"
  ],
  "next_object": "SourceNaturalBianchiHighestWeightSelectorTheoremForK_IG_V1",
  "next_meaningful_step": "Compute_or_recover_the_representation_highest_weight_decomposition_and_equivariant_hom_space_multiplicity_for_the_source_natural_Shiab_projection_contraction_family_state_the_Bianchi_selector_rule_apply_it_to_each_matrix_row_then_test_family_identity_to_SourceForcedCodomainSelectorForK_IG."
}
```
