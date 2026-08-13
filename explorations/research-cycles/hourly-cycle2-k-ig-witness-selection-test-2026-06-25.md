---
title: "Hourly Cycle 2 K_IG Witness Selection Test V1"
status: draft
doc_type: hourly_cycle2_k_ig_witness_selection_test
verdict: "MULTIPLE_SURVIVING_OPERATORS_NO_FINALITY_CERTIFICATE"
owned_path: "explorations/hourly-cycle2-k-ig-witness-selection-test-2026-06-25.md"
optional_audit: "tests/hourly_cycle2_k_ig_witness_selection_test_audit.py"
created_at: "2026-06-25"
---

# Hourly Cycle 2 K_IG Witness Selection Test V1

## 1. Verdict

Verdict:

```text
MULTIPLE.
```

The current sources do not make `K_IG = D_A U` final. They also do not make it axiomatic,
and they do not eliminate all admissible first-order local gauge-covariant IG operators.

Decision table:

| decision | current status | reason |
|---|---:|---|
| `FINAL` | no | no uniqueness, terminal, or final-object theorem is present |
| `AXIOMATIC` | no | no primary/source axiom explicitly selects `D_A U` |
| `MULTIPLE` | yes | at least two inequivalent first-order local gauge-covariant classes survive the stated interface |
| `NONE` | no | `D_A U` itself is a well-typed admissible candidate |

The strongest allowed statement is:

```text
D_A U is the best current exterior-derivative candidate for a Branch 3 dynamical IG
template, but current repo sources leave the K_IG selector underdefined because multiple
operator classes survive before targets.
```

This file does not claim theta/FLRW coefficients, dark energy, Lambda, `Z_theta`,
`C_Rtheta`, or `xi_eff`.

## 2. What was derived directly from repo sources

The following constraints are read directly from the assigned sources.

1. `RESEARCH-POSTURE.md` requires constructive obstruction handling and forbids treating
   compatibility as derivation.
2. `process/runbooks/five-lane-frontier-run.md` requires a decision-grade artifact with a
   verdict, a strongest positive attempt, the first exact obstruction, and guardrails.
3. `gu-typed-operator-action-spine-2026-06-24.md` fixes the proposal-level carrier and
   typed action spine:

   ```text
   Y = Met_Lor(X), g_Y fixed baseline, G = Sp(64), P -> Y,
   A dynamical, epsilon,beta IG data,
   U = Ad(epsilon^-1) beta,
   theta = A - Gamma(epsilon) - U.
   ```

4. The same spine makes the free-beta warning binding: free `beta` with only a theta norm
   gives `theta = 0`, so a nonzero-theta route must use fixed/constrained IG data or a
   real dynamical `S_IG`.
5. `hourly-cycle2-source-forced-ig-dynamics-selector-v0-2026-06-24.md` identifies the first
   missing datum as a source-side rule selecting `K_IG` and field degrees. It names
   `D_A U` as the natural candidate, not as a selected operator.
6. `hourly-cycle1-effect-typed-witness-ig-selector-2026-06-25.md` refines the blocker to a
   source/projection/finality/loss interface. A future selector must prove `FINAL`,
   provide an `AXIOMATIC` source rule, decide `MULTIPLE`, or decide `NONE`.

Therefore the selection test must operate before any target comparison and before any
theta/FLRW coefficient packet.

## 3. Strongest positive construction attempt

Assume the strongest Branch 3 typing already available:

```text
U in Omega^1(Y, ad P)
A an Sp(64) connection on P -> Y
D_A the induced covariant exterior derivative
target_inputs_seen = []
```

Then the cleanest first-order parent slot is:

```text
K_ext(U;A) = D_A U in Omega^2(Y, ad P)
P_IG in Omega^2(Y, ad P)
int_Y <P_IG, D_A U>_{Q_IG}.
```

This construction is strong because it uses only the connection and the gauge representation,
is local, is first order in `U`, is gauge-covariant, and has a canonical parent degree once
the exterior codomain is chosen.

However, the source/projection/finality/loss interface does not state that the exterior
codomain must be chosen. With only the current source data, the minimal surviving
candidate classes are:

| class id | schematic operator class | output degree | survives? | why not eliminated |
|---|---|---:|---:|---|
| `EXT_DERIVATIVE` | `D_A U` | 2-form | yes | local, first-order, gauge-covariant, and already used by the strongest template |
| `CODERIVATIVE_TRACE` | `D_A^* U` or metric trace of `nabla_A U` | 0-form | yes | `g_Y` and the connection allow it; no source rule fixes the parent degree to 2 |
| `SYMMETRIC_DERIVATIVE` | `Sym(nabla_A U)`, optionally trace-free | symmetric 2-tensor with `ad P` value | yes | local first-order gauge covariance survives if the Levi-Civita/gimmel connection is admitted |
| `PROJECTED_DERIVATIVE` | `Pi_s,epsilon(nabla_A U)` or `Pi_s,epsilon(D_A U)` | projected source sector | yes as a class | section/epsilon projectors are named source data, but no projector/finality rule is fixed |
| `LOWER_ORDER_DRESSED_EXTERIOR` | `D_A U + L_s,epsilon(U)` | 2-form | yes as an affine class | lower-order source-natural terms are not ruled out by first-order symbol data alone |

The exact list is intentionally class-level, not coefficient-level. The current interface
has not fixed `Q_IG`, parent momentum degree, boundary class, allowed projectors, or
lower-order source terms. Those omissions are precisely why coefficient enumeration would
be fake precision.

The positive result is therefore a narrowing, not a selection:

```text
D_A U is admissible and remains the strongest exterior-derivative witness, but the
admissible first-order local gauge-covariant class is not a singleton.
```

## 4. First exact obstruction or missing proof object

The first exact obstruction is:

```text
K_IGWitnessFinalityCertificate
```

with the more operational form:

```text
K_IGWitnessSelectionRule:
  source witnesses + projection witnesses + loss ledger
    -> one selected codomain, parent degree, operator class, and lower-order policy.
```

The obstruction occurs before `Q_IG`, `Z_U`, `V_src`, `S_cross_src`, boundary data,
`J_IG`, `theta_eff`, and FLRW reduction.

The earliest missing proof object must do at least one of the following:

1. Prove that the typed source category has `D_A U` as a terminal/final object among
   admissible IG witnesses.
2. Cite a primary/source axiom selecting the exterior derivative codomain and excluding
   coderivative, symmetric, projected, and lower-order-dressed alternatives.
3. Prove that all non-exterior candidates violate a stated source/projection/loss rule.

No assigned source supplies any of these.

The first obstruction is not ill-typedness. `D_A U` is well typed. The obstruction is
non-uniqueness under the currently declared source interface.

## 5. Constructive next object

Build:

```text
K_IGCodomainAndFinalityCertificate_V1.
```

It should contain:

1. A typed category or preorder of admissible IG witnesses, including codomain and parent
   momentum degree.
2. A rule deciding whether the exterior codomain is source-forced.
3. An explicit policy for `D_A^* U`, `Sym(nabla_A U)`, projected derivatives, and
   lower-order-dressed exterior derivatives.
4. A projection-loss proof showing that no eliminated candidate is being hidden by the
   source-to-IG projection.
5. A target replacement check proving that target labels cannot change the selected
   operator packet.

Promotion condition:

```text
Only if that object selects one operator class and its parent degree before targets may
the repo attempt Q_IG, Z_U, parent action, current, and theta/FLRW reductions.
```

## 6. Impact on GU claim

The relevant GU claim is not promoted.

Allowed current claim:

```text
The current typed GU action spine admits a coherent Branch 3 exterior-derivative candidate
K_IG = D_A U, but the source/projection/finality/loss interface leaves multiple
first-order local gauge-covariant IG operator classes alive.
```

Forbidden current claims:

```text
GU derives dark energy.
GU derives Lambda.
GU derives Z_theta.
GU derives C_Rtheta.
GU derives xi_eff.
D_A U is source-forced because it is natural.
Branch 3 emits a theta/FLRW coefficient packet.
Target performance selects K_IG.
```

Impact:

```text
Branch 3 remains a coherent host. It is not yet a selected GU dynamics. The first gate is
now a codomain/finality selection theorem, not a cosmology computation.
```

## 7. Next meaningful proof/computation step

Do not run a theta/FLRW comparison next. The next meaningful step is a formal elimination
or finality proof for the surviving candidate classes.

Concrete next step:

```text
For each candidate class C in
  EXT_DERIVATIVE,
  CODERIVATIVE_TRACE,
  SYMMETRIC_DERIVATIVE,
  PROJECTED_DERIVATIVE,
  LOWER_ORDER_DRESSED_EXTERIOR,
write its source inputs, codomain, parent momentum degree, boundary terms, and projection
loss. Then prove source elimination of every class except one, or keep MULTIPLE.
```

If the result remains `MULTIPLE`, the selector stays underdefined. If it becomes `FINAL`
or `AXIOMATIC`, the selected packet must include field degrees, `Q_IG`, boundary class,
and first-order parent action before any target comparison.

## 8. Machine-readable JSON summary

```json
{
  "artifact": "K_IGWitnessSelectionTest_V1",
  "version": "2026-06-25",
  "mission_posture": "Mission_A_constructive_obstruction",
  "verdict": "MULTIPLE",
  "decision": {
    "FINAL": false,
    "AXIOMATIC": false,
    "MULTIPLE": true,
    "NONE": false
  },
  "candidate_D_A_U_status": "admissible_strongest_exterior_derivative_candidate_not_final_not_axiomatic",
  "target_inputs_seen_before_selector": [],
  "target_comparison_permitted": false,
  "derived_from_sources": [
    "research_posture_requires_constructive_obstruction_and_forbids_compatibility_as_derivation",
    "five_lane_run_requires_decision_grade_artifact",
    "typed_spine_fixes_Y_gY_G_P_A_epsilon_beta_U_theta_at_proposal_level",
    "free_beta_plus_theta_norm_forces_theta_zero",
    "source_forced_ig_dynamics_selector_identifies_K_IG_and_field_degrees_as_first_missing_datum",
    "effect_typed_witness_transport_requires_final_axiomatic_multiple_or_none_decision"
  ],
  "surviving_candidate_classes": [
    {
      "id": "EXT_DERIVATIVE",
      "schematic_operator": "D_A U",
      "codomain": "Omega^2(Y,ad P)",
      "parent_degree_if_chosen": "P_IG in Omega^2(Y,ad P)",
      "survives": true,
      "status": "strongest_positive_candidate"
    },
    {
      "id": "CODERIVATIVE_TRACE",
      "schematic_operator": "D_A^* U_or_metric_trace_of_nabla_A_U",
      "codomain": "Omega^0(Y,ad P)",
      "parent_degree_if_chosen": "P_IG in Omega^0(Y,ad P)",
      "survives": true,
      "status": "not_eliminated_because_codomain_parent_degree_not_source_fixed"
    },
    {
      "id": "SYMMETRIC_DERIVATIVE",
      "schematic_operator": "Sym(nabla_A U)_possibly_trace_free",
      "codomain": "Sym^2 T^*Y tensor adP_or_trace_free_variant",
      "parent_degree_if_chosen": "matching_symmetric_parent",
      "survives": true,
      "status": "not_eliminated_if_gY_Levi_Civita_source_connection_is_allowed"
    },
    {
      "id": "PROJECTED_DERIVATIVE",
      "schematic_operator": "Pi_s_epsilon(nabla_A U)_or_Pi_s_epsilon(D_A U)",
      "codomain": "projected_IG_source_sector",
      "parent_degree_if_chosen": "matching_projected_parent",
      "survives": true,
      "status": "class_survives_because_projector_and_loss_policy_are_not_fixed"
    },
    {
      "id": "LOWER_ORDER_DRESSED_EXTERIOR",
      "schematic_operator": "D_A U_plus_L_s_epsilon(U)",
      "codomain": "Omega^2(Y,ad P)",
      "parent_degree_if_chosen": "P_IG in Omega^2(Y,ad P)",
      "survives": true,
      "status": "affine_class_not_eliminated_by_first_order_symbol_data_alone"
    }
  ],
  "first_exact_obstruction": {
    "id": "K_IGWitnessFinalityCertificate",
    "operational_id": "K_IGWitnessSelectionRule",
    "missing": true,
    "description": "source witnesses plus projection witnesses plus loss ledger do not select one codomain parent degree operator class and lower_order_policy",
    "blocks_before": [
      "Q_IG",
      "Z_U",
      "V_src",
      "S_cross_src",
      "boundary_data",
      "J_IG",
      "theta_eff",
      "FLRW_reduction",
      "Z_theta",
      "C_Rtheta",
      "xi_eff"
    ]
  },
  "strongest_positive_construction": {
    "candidate": "K_ext(U;A)=D_A U",
    "parent_slot": "int_Y <P_IG,D_A U>_{Q_IG}",
    "positive_claim": "admissible_coherent_template",
    "selection_claim": false
  },
  "anti_overclaim": {
    "GU_derives_dark_energy": false,
    "GU_derives_Lambda": false,
    "GU_derives_Z_theta": false,
    "GU_derives_C_Rtheta": false,
    "GU_derives_xi_eff": false,
    "Branch_3_emits_theta_FLRW_packet": false,
    "D_A_U_source_forced_by_naturalness": false,
    "target_performance_selects_K_IG": false
  },
  "constructive_next_object": {
    "id": "K_IGCodomainAndFinalityCertificate_V1",
    "required_outputs": [
      "typed_category_or_preorder_of_admissible_IG_witnesses",
      "codomain_and_parent_degree_rule",
      "elimination_or_finality_proof_for_competing_classes",
      "projection_loss_proof",
      "target_replacement_check"
    ]
  },
  "claim_impact": {
    "relevant_GU_claim_promoted": false,
    "Branch_3_status": "coherent_host_not_selected_dynamics",
    "selector_status": "underdefined_due_to_multiple_survivors",
    "next_gate": "codomain_finality_selection_not_cosmology"
  }
}
```

## Sources read

- `RESEARCH-POSTURE.md`
- `process/runbooks/five-lane-frontier-run.md`
- `explorations/hourly-cycle1-effect-typed-witness-ig-selector-2026-06-25.md`
- `explorations/hourly-cycle2-source-forced-ig-dynamics-selector-v0-2026-06-24.md`
- `explorations/gu-typed-operator-action-spine-2026-06-24.md`
