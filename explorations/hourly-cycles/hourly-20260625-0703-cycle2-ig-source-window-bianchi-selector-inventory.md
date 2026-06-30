---
title: "Hourly 20260625 0703 Cycle 2 IG Source Window Bianchi Selector Inventory"
date: "2026-06-25"
run_id: "hourly-20260625-0703"
cycle: 2
lane: 5
doc_type: ig_source_window_bianchi_selector_inventory
artifact_id: "SourceWindowFormulaInventoryAndBianchiSelectorForShiab_V1"
verdict: "PREPARES_SELECTOR_THEOREM_RIVALS_NOT_ELIMINATED"
owned_path: "explorations/hourly-20260625-0703-cycle2-ig-source-window-bianchi-selector-inventory.md"
companion_audit: "tests/hourly_20260625_0703_cycle2_ig_source_window_bianchi_selector_inventory_audit.py"
---

# Hourly 20260625 0703 Cycle 2 IG Source Window Bianchi Selector Inventory

## 1. Verdict

Verdict: **blocked / prepares selector theorem**.

The current repo source object now supports a direct inventory of the required
manuscript formula windows:

```text
Section 8:   equations 8.1-8.7, PDF pages 41-42
Section 9.1: equations 9.2-9.6, PDF pages 43-44
Summary:     equations 12.2-12.7, PDF pages 55-57
```

The inventory strengthens the positive case that the manuscript contains a real
Shiab operator family, a typed displayed Shiab map, and explicit Bianchi/highest
weight selector language. It does **not** eliminate the Cycle 1 rival classes,
because the same source window says the historical representation-theory notes
that picked the operator are not located and must be recovered or reconstructed.

Decision state:

```text
artifact_id: SourceWindowFormulaInventoryAndBianchiSelectorForShiab_V1
accepted_receipt_count: 0
selector_identity_passed: false
eliminated_rival_count: 0
surviving_rival_count: 6
proof_restart_allowed: false
first_obstruction: missing recovered representation-theory/highest-weight/Bianchi selector calculation
```

This is a source-window upgrade over the prior rival matrix, not a selector
closure.

## 2. Specific GU Claim/Bridge Under Test

Claim under test:

```text
The author manuscript formula windows 8.1-8.7, 9.2-9.6, and 12.2-12.7
source-force the Shiab/Bianchi selector needed to identify the displayed
Shiab candidate with SourceForcedCodomainSelectorForK_IG and eliminate
source-natural rival operator classes.
```

Bridge being tested:

```text
Section 8 operator family and Bianchi/highest-weight selector language
  -> Section 9.1 displayed Shiab formula and first-order bosonic action
  -> Summary projection-removal / Einstein-Ricci comparison equations
  -> typed K_IG selector fields
  -> rival-class elimination
  -> SourceForcedCodomainSelectorForK_IG identity
```

The bridge reaches an inventory-ready selector theorem premise. It does not
reach a source-emitted selector theorem.

## 3. Owned Path And Sources Read First

Owned output path:

```text
explorations/hourly-20260625-0703-cycle2-ig-source-window-bianchi-selector-inventory.md
```

Owned audit path:

```text
tests/hourly_20260625_0703_cycle2_ig_source_window_bianchi_selector_inventory_audit.py
```

Sources read first:

| source | role in this artifact |
| --- | --- |
| `RESEARCH-POSTURE.md` | Requires constructive pursuit but forbids promoting compatibility or hosted structure into derivation. |
| `process/runbooks/five-lane-frontier-run.md` | Requires a decision-grade lane result, exact obstruction, and no "hosted by" to "selected by" jump. |
| `explorations/hourly-20260625-0703-cycle1-ig-rival-selector-eliminator-recheck.md` | Supplies the immediate prior Cycle 1 rival recheck and next object name. |
| `explorations/hourly-20260625-0601-cycle2-ig-selector-rival-eliminator-matrix.md` | Supplies the six rival classes and missing eliminator object. |
| `explorations/hourly-20260625-0601-cycle1-author-manuscript-ig-selector-identity-packet.md` | Supplies the required identity target `SourceForcedCodomainSelectorForK_IG` and candidate locator framing. |
| `canon/shiab-existence-cl95.md` | Supports real Shiab existence in a Cl(9,5) setting but leaves equivariant uniqueness open. |
| `Geometric_UnityDraftApril1st2021.pdf` | Current local manuscript source; SHA-256 checked as `3f28d742234a9841fc8e51ff172053200aa3eddf3ece38154a3328b9ebd186d4`. |

Extraction note: `pdftotext` was unavailable in the local shell, so the
manuscript windows were read with Python `pypdf` text extraction against the
local PDF. The extraction is sufficient for equation labels and operator
inventory, but not a typeset-image proof check.

## 4. Strongest Positive Construction Attempt

The strongest construction is now sharper than "the manuscript hosts Shiab."
The source windows give a coherent operator chain:

| window | equation(s) | extracted inventory |
| --- | --- | --- |
| Section 8 | `8.1` | A schematic Shiab contraction operator acting on a gauge-covariant `ad`-valued differential form `eta`; it uses conjugated invariant forms `epsilon^{-1} Phi_r epsilon`, wedge/Hodge operations, and commutator or anticommutator brackets. |
| Section 8.1 | `8.2` | Vector-space identification between exterior forms and the Clifford algebra over `T*X`. |
| Section 8.1 | `8.3` | A map from exterior forms on `T*Y` into a Clifford/matrix algebra is asserted for a `(7,7)` inherited metric in the manuscript notation. |
| Section 8.1 | `8.4` | Inclusion/complexification diagram relating real and complex Clifford/matrix algebra presentations. |
| Section 8.1 | `8.5` | A decomposition of the `so(64,64)`-side into exterior-degree summands, presented as the commuting/invariant part. |
| Section 8.1 | `8.6` | A complementary `u(64,64)/so(64,64)` exterior-degree list requiring factors of `i` inside complexification. |
| Section 8.1 | `8.7` | Defines a basis `{Phi_i}` for invariant subspaces of `[Lambda^i(R^{7,7}) tensor u(64,64)]^{Spin(7,7)}`. |
| Section 8.2 | prose after `8.7` | The author says the operator choice was historically made by representation theory / highest weights, with the Bianchi identity selecting the best operator in different circumstances, but the original notes are not located. |
| Section 9.1 | `9.2` | Displays the typed Shiab map `Omega^2(Y^{7,7}, ad) -> Omega^{d-1}(Y^{7,7}, ad)`. |
| Section 9.1 | `9.3` | Gives a displayed Einstein/Ricci-like Shiab formula on an `ad`-valued 2-form `xi`, with Ricci-like and scalar-like terms and Weyl annihilation language nearby. |
| Section 9.1 | `9.4` | Inserts the Shiab into a first-order bosonic action pairing shifted torsion with the Hodge-star/Shiab applied to metric curvature plus Chern-Simons-like terms, plus a torsion quadratic term. |
| Section 9.1 | `9.5` | Euler-Lagrange output is typed as a pair in `Omega^{d-1}(ad) oplus Omega^d(ad)`. |
| Section 9.1 | `9.6` | Records redundancy as `Xi = D_omega Upsilon_omega`, so the second equation need not be considered if `Upsilon_omega = 0`. |
| Summary | `12.2` | First-order reduced Euler-Lagrange equation after removal of redundancy through projections: `Pi(dI_1) = (delta_omega)^2 = Upsilon_omega = 0`. |
| Summary | `12.3` | Second related Lagrangian equation `Pi(dI_2) = D_omega^* Upsilon_omega = 0`, automatically satisfied if the first-order theory holds. |
| Summary | `12.4` | Chern-Simons / GU comparison: the GU action uses shifted torsion, Hodge star, Shiab, metric curvature, and Chern-Simons-like torsion terms. |
| Summary | `12.5` | Defines connection one-forms by measuring the ordinary and GU connections relative to a reference/trivial or Levi-Civita connection. |
| Summary | `12.6` | Defines displaced torsion relative to the gauge-transformed Levi-Civita spin connection. |
| Summary | `12.7` | Self-dual Yang-Mills analogy: first-order curvature equation implies the Yang-Mills equation by the Bianchi identity. |

Typed operator rows:

| id | domain | codomain | principal symbol | parent momentum degree | projection behavior | lower-order freedom | required geometric data | Bianchi/highest-weight selector language |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `shiab_schematic_8_1` | gauge-covariant `ad`-valued differential form `eta` | form degree set by Hodge/wedge recipe; not fully fixed in `8.1` | zero-order algebraic contraction in the field being acted on; no derivative of `eta` is displayed | not source-forced for `K_IG`; schematic family member | no projector policy in `8.1` | bracket choice, invariant form degree, signs, and possible sums remain free | invariant forms `Phi_r`, gauge element `epsilon`, Hodge star, metric, `ad` bundle | selector language not in formula itself; later prose says Bianchi/highest weights historically chose operators |
| `invariant_basis_8_7` | invariant subspaces `[Lambda^i(R^{7,7}) tensor u(64,64)]^{Spin(7,7)}` | basis elements `{Phi_i}` for Shiab construction | algebraic representation data; no differential principal symbol | none | no projection policy | degree `i` and real/complex factor choices remain available | Spin(7,7) representation, metric signature, Clifford/matrix algebra identifications | highest-weight selector is referenced as historical method, but the calculation is missing |
| `displayed_shiab_9_2_9_3` | `Omega^2(Y^{7,7}, ad)`; explicitly an `ad`-valued 2-form `xi` | `Omega^{d-1}(Y^{7,7}, ad)` | zero-order in `xi`: wedge/Hodge/conjugated invariant-form contraction, not a derivative operator | parent momentum degree remains unforced for `K_IG`; it acts on curvature-like 2-form data | kills Weyl curvature contribution according to adjacent text; no full projector/loss theorem | choice of Shiab operator is acknowledged as one among other possibilities; no uniqueness rule | `Y`, `(7,7)` manuscript metric, `ad`, `epsilon`, `Phi_1`, `Phi_2`, Hodge star | footnote/prose says settled operator was chosen for Bianchi properties, but the source does not supply the recovered selection proof |
| `bosonic_action_9_4` | bosonic fields `(epsilon_Y, varpi_Y, g_X)` through shifted torsion, metric curvature, and connection data | real-valued first-order bosonic action | action contains first-order connection/torsion/curvature ingredients; Shiab part is algebraic on curvature input | action-level degree is not the `K_IG` selector degree; no source-forced selector field | embeds Einstein/Ricci-like projection through Shiab; no source selector for projector policy | torsion quadratic coefficient and Chern-Simons-like lower-order terms appear | Levi-Civita spin connection, gauge-rotated connection, shifted torsion, metric, trace pairing | no independent eliminator; it uses the chosen Shiab candidate |
| `el_redundancy_9_5_9_6_12_2_12_3` | variations of first- and second-order Lagrangians | `Omega^{d-1}(ad) oplus Omega^d(ad)` and projected equations | differential relation `Xi = D_omega Upsilon_omega`; first/second order relation is present | does not select `K_IG`; it is an equation-redundancy relation | explicit projection `Pi` removes redundancy in Summary equations | `D_omega` and `D_omega^*` are named but not typed enough to fix lower-order freedom | variational calculus, projected Euler-Lagrange equations, connection-dependent differential | Bianchi-style implication is analogized in `12.7`; not a Shiab rival eliminator |
| `cs_gu_comparison_12_4_12_7` | Chern-Simons connection one-form and GU shifted torsion/connection data | action comparison and first-order-to-second-order implication | exterior-derivative/covariant-derivative pattern appears in comparison, but no unique Shiab principal-symbol selector | not source-forced for `K_IG` | says Shiab kills Weyl like Einstein-Ricci projection but gauge-covariantly; no complete projection-loss behavior | comparison leaves choices of connection, torsion, and Shiab instantiation | reference connection, Levi-Civita spin connection, gauge transform, shifted torsion, curvature | `12.7` explicitly uses Bianchi identity for first-order implication; it supports the selector motif but does not recover the missing Shiab choice calculation |

Positive construction attempt:

```text
Use 8.7 to enumerate invariant building blocks Phi_i.
Use the Section 8.2 prose as the intended selector theorem statement:
  highest-weight / Bianchi identity chooses the operator.
Use 9.2-9.3 as the candidate selected operator.
Use 9.4-9.6 and 12.2-12.7 as evidence that this operator is tied to
  first-order equations, redundancy removal, Weyl-killing projection behavior,
  and Bianchi-style square-root logic.
```

This construction is strong enough to define the next theorem target:

```text
RecoveredBianchiHighestWeightSelectorForShiab_V1
```

It is not strong enough to accept the selector, because the actual
highest-weight/Bianchi eliminator calculation is not in the extracted window.

## 5. First Exact Obstruction Or Missing Proof/Source Object

First obstruction:

```text
The manuscript gives the selector language but not the selector calculation.
```

More exactly:

```text
RecoveredBianchiHighestWeightSelectorForShiab_V1 is missing.
```

The missing object must provide:

| required field | why the current source window does not close it |
| --- | --- |
| candidate family under comparison | Section 8 lists tools and invariant forms, but not the full compared family. |
| representation/highest-weight calculation | The source says highest-weight methods were used historically, but the notes are missing. |
| Bianchi identity selection criterion | The source says Bianchi picked the best operator or guaranteed perpendicularity/automatic equations, but does not state the criterion. |
| selected formula proof | `9.3` displays a formula, but the source does not prove it is the uniquely selected formula. |
| family identity to `SourceForcedCodomainSelectorForK_IG` | The displayed map is a Shiab map on curvature-like input, not yet the source-forced `K_IG` codomain selector. |
| principal-symbol / momentum-degree selector | Shiab is zero-order on curvature input; the parent `K_IG` degree and principal-symbol class are not forced. |
| projection-loss behavior | Weyl-killing and redundancy projection are stated locally, but not a full projector policy for `K_IG`. |
| lower-order freedom policy | Section 8 and 9 explicitly leave multiple Shiab/operator possibilities open. |
| rival eliminators | Exterior derivative, coderivative/trace, symmetric derivative, projected derivative, lower-order dressed exterior, and displayed Shiab codomain are not eliminated by a source-emitted theorem. |

Therefore the exact decision is:

```text
inventory complete enough for the next selector theorem;
rival elimination not complete enough for proof restart.
```

## 6. What Would Change If Closed

If `RecoveredBianchiHighestWeightSelectorForShiab_V1` were supplied from source
notes or reconstructed proof and passed audit:

- `accepted_receipt_count` for this lane could become `1`.
- `selector_identity_passed` could become `true` if the selected formula is
  proved identical to the `SourceForcedCodomainSelectorForK_IG` row.
- `eliminated_rival_count` would need to become `6`, or surviving rows would
  need to be proved harmless equivalences of the same selected operator.
- The manuscript IG row could move from "hosted candidate" to "conditional
  selector receipt."
- Proof restart could become family-limited and conditional.

This would still not prove downstream theta/FLRW, dark energy, or physical
recovery. It would only close the source-side IG selector gate.

## 7. Falsification/Demotion Condition

Demote this route if any of the following occurs:

- A typeset image audit shows the extracted formula labels or operator windows
  were misread.
- The missing historical notes, if found, select a different operator than the
  displayed `9.3` formula.
- The Bianchi/highest-weight calculation does not eliminate all source-natural
  rival classes.
- The displayed Shiab is only an Einstein/Ricci comparison/readout map and does
  not bridge to `SourceForcedCodomainSelectorForK_IG`.
- The `(7,7)` manuscript Shiab source cannot be reconciled with the repo canon
  Cl(9,5) Shiab setting without changing the selected operator class.
- Any bridge to the selector requires target physics, desired coefficients, or
  downstream success as input.

No global GU no-go follows from those outcomes. The demotion would be local to
this manuscript-window selector bridge.

## 8. Next Meaningful Computation/Proof/Source Step

The next step is not another broad source search. It is a narrow theorem packet:

```text
RecoveredBianchiHighestWeightSelectorForShiab_V1
```

It should:

1. Treat `{Phi_i}` from `8.7` as candidate invariant building blocks.
2. Reconstruct the highest-weight/intertwiner space for the Shiab family.
3. State the Bianchi condition as an algebraic or differential constraint on
   that candidate space.
4. Check whether the displayed `9.3` operator is selected uniquely up to scalar.
5. Translate the result into the `SourceForcedCodomainSelectorForK_IG` fields:
   domain, codomain, parent momentum degree, principal symbol, projection
   behavior, lower-order freedom, and geometric data.
6. Rerun the six rival classes against the resulting theorem.

## 9. JSON Summary

```json
{
  "artifact": "SourceWindowFormulaInventoryAndBianchiSelectorForShiab_V1",
  "run_id": "hourly-20260625-0703",
  "cycle": 2,
  "lane": 5,
  "artifact_id": "SourceWindowFormulaInventoryAndBianchiSelectorForShiab_V1",
  "verdict": "PREPARES_SELECTOR_THEOREM_RIVALS_NOT_ELIMINATED",
  "inventoried_windows": [
    {
      "window_id": "section_8_eqs_8_1_8_7",
      "source": "Geometric_UnityDraftApril1st2021.pdf",
      "pdf_pages": "41-42",
      "equations": ["8.1", "8.2", "8.3", "8.4", "8.5", "8.6", "8.7"],
      "status": "present",
      "selector_relevance": "Shiab family, invariant Phi_i basis, highest-weight/Bianchi operator-choice language"
    },
    {
      "window_id": "section_9_1_eqs_9_2_9_6",
      "source": "Geometric_UnityDraftApril1st2021.pdf",
      "pdf_pages": "43-44",
      "equations": ["9.2", "9.3", "9.4", "9.5", "9.6"],
      "status": "present",
      "selector_relevance": "typed displayed Shiab map, Einstein/Ricci-like formula, bosonic action, Euler-Lagrange redundancy"
    },
    {
      "window_id": "summary_eqs_12_2_12_7",
      "source": "Geometric_UnityDraftApril1st2021.pdf",
      "pdf_pages": "55-57",
      "equations": ["12.2", "12.3", "12.4", "12.5", "12.6", "12.7"],
      "status": "present",
      "selector_relevance": "projection-removal, Chern-Simons/GU comparison, displaced torsion, Bianchi square-root analogy"
    }
  ],
  "operator_rows": [
    {
      "id": "shiab_schematic_8_1",
      "domain": "gauge_covariant_ad_valued_differential_form_eta",
      "codomain": "form_degree_set_by_wedge_hodge_recipe_not_fully_fixed_in_8_1",
      "principal_symbol": "zero_order_algebraic_contraction_no_derivative_of_eta_displayed",
      "parent_momentum_degree": "not_source_forced_for_K_IG",
      "projection_behavior": "no_projector_policy_in_8_1",
      "lower_order_freedom": "bracket_choice_invariant_form_degree_signs_and_sums_free",
      "required_geometric_data": ["Phi_r", "epsilon", "Hodge_star", "metric", "ad_bundle"],
      "bianchi_highest_weight_selector_language": "not_in_formula_but_later_prose_says_Bianchi_highest_weights_historically_chose_operators",
      "rival_eliminator_found": false
    },
    {
      "id": "invariant_basis_8_7",
      "domain": "Spin_7_7_invariant_subspaces_Lambda_i_R_7_7_tensor_u_64_64",
      "codomain": "basis_elements_Phi_i_for_Shiab_construction",
      "principal_symbol": "algebraic_representation_data_no_differential_symbol",
      "parent_momentum_degree": "none",
      "projection_behavior": "no_projection_policy",
      "lower_order_freedom": "degree_i_and_real_complex_factor_choices_available",
      "required_geometric_data": ["Spin_7_7_representation", "metric_signature", "Clifford_matrix_identifications"],
      "bianchi_highest_weight_selector_language": "highest_weight_selector_referenced_as_historical_method_calculation_missing",
      "rival_eliminator_found": false
    },
    {
      "id": "displayed_shiab_9_2_9_3",
      "domain": "Omega^2(Y^{7,7},ad)",
      "codomain": "Omega^{d-1}(Y^{7,7},ad)",
      "principal_symbol": "zero_order_in_xi_wedge_hodge_conjugated_invariant_form_contraction",
      "parent_momentum_degree": "curvature_like_2_form_input_but_K_IG_parent_degree_not_forced",
      "projection_behavior": "annihilates_Weyl_curvature_by_adjacent_text_no_full_projector_loss_theorem",
      "lower_order_freedom": "one_choice_among_other_possibilities_no_uniqueness_rule",
      "required_geometric_data": ["Y", "7_7_metric_in_manuscript", "ad", "epsilon", "Phi_1", "Phi_2", "Hodge_star"],
      "bianchi_highest_weight_selector_language": "footnote_says_settled_operator_chosen_for_Bianchi_properties_but_proof_not_supplied",
      "rival_eliminator_found": false
    },
    {
      "id": "bosonic_action_9_4",
      "domain": "bosonic_fields_epsilon_Y_varpi_Y_g_X_through_shifted_torsion_metric_curvature_connection_data",
      "codomain": "real_valued_first_order_bosonic_action",
      "principal_symbol": "action_contains_first_order_connection_torsion_curvature_ingredients_Shiab_algebraic_on_curvature_input",
      "parent_momentum_degree": "action_level_degree_not_K_IG_selector_degree",
      "projection_behavior": "embeds_Einstein_Ricci_like_projection_through_Shiab_no_source_selector_policy",
      "lower_order_freedom": "torsion_quadratic_coefficient_and_Chern_Simons_like_terms_present",
      "required_geometric_data": ["Levi_Civita_spin_connection", "gauge_rotated_connection", "shifted_torsion", "metric", "trace_pairing"],
      "bianchi_highest_weight_selector_language": "uses_chosen_Shiab_candidate_no_independent_eliminator",
      "rival_eliminator_found": false
    },
    {
      "id": "el_redundancy_9_5_9_6_12_2_12_3",
      "domain": "variations_of_first_and_second_order_Lagrangians",
      "codomain": "Omega^{d-1}(ad)_oplus_Omega^d(ad)_and_projected_equations",
      "principal_symbol": "differential_relation_Xi_equals_D_omega_Upsilon_omega",
      "parent_momentum_degree": "does_not_select_K_IG",
      "projection_behavior": "explicit_Pi_removes_redundancy_in_summary_equations",
      "lower_order_freedom": "D_omega_and_D_omega_star_named_not_typed_enough_to_fix_lower_order_freedom",
      "required_geometric_data": ["variational_calculus", "projected_Euler_Lagrange_equations", "connection_dependent_differential"],
      "bianchi_highest_weight_selector_language": "Bianchi_style_implication_analogized_in_12_7_not_Shiab_rival_eliminator",
      "rival_eliminator_found": false
    },
    {
      "id": "cs_gu_comparison_12_4_12_7",
      "domain": "Chern_Simons_connection_one_form_and_GU_shifted_torsion_connection_data",
      "codomain": "action_comparison_and_first_order_to_second_order_implication",
      "principal_symbol": "exterior_or_covariant_derivative_pattern_present_but_no_unique_Shiab_principal_symbol_selector",
      "parent_momentum_degree": "not_source_forced_for_K_IG",
      "projection_behavior": "Shiab_kills_Weyl_like_Einstein_Ricci_projection_gauge_covariantly_no_complete_projection_loss_behavior",
      "lower_order_freedom": "comparison_leaves_connection_torsion_and_Shiab_instantiation_choices",
      "required_geometric_data": ["reference_connection", "Levi_Civita_spin_connection", "gauge_transform", "shifted_torsion", "curvature"],
      "bianchi_highest_weight_selector_language": "12_7_uses_Bianchi_identity_for_first_order_implication_but_not_missing_Shiab_choice_calculation",
      "rival_eliminator_found": false
    }
  ],
  "rival_classes": [
    {"id": "exterior_derivative", "status": "survives", "eliminated_by_source": false},
    {"id": "coderivative_trace_scalar", "status": "survives", "eliminated_by_source": false},
    {"id": "symmetric_derivative", "status": "survives", "eliminated_by_source": false},
    {"id": "projected_derivative", "status": "survives", "eliminated_by_source": false},
    {"id": "lower_order_dressed_exterior", "status": "survives", "eliminated_by_source": false},
    {"id": "displayed_shiab_codomain", "status": "hosted_candidate_not_selected", "eliminated_by_source": false}
  ],
  "eliminated_rival_count": 0,
  "surviving_rival_count": 6,
  "selector_identity_passed": false,
  "accepted_receipt_count": 0,
  "proof_restart_allowed": false,
  "first_obstruction": "missing recovered representation-theory/highest-weight/Bianchi selector calculation selecting the displayed Shiab formula and eliminating rival classes",
  "missing_source_object": "RecoveredBianchiHighestWeightSelectorForShiab_V1",
  "next_frontier_object": "RecoveredBianchiHighestWeightSelectorForShiab_V1",
  "companion_audit": "tests/hourly_20260625_0703_cycle2_ig_source_window_bianchi_selector_inventory_audit.py"
}
```
