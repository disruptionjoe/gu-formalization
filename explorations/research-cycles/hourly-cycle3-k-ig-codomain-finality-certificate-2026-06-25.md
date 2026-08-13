---
title: "Hourly Cycle 3 K_IG Codomain and Finality Certificate V1"
status: draft
doc_type: hourly_cycle3_k_ig_codomain_finality_certificate
verdict: "MULTIPLE_NO_CODOMAIN_FINALITY_RULE"
owned_path: "explorations/hourly-cycle3-k-ig-codomain-finality-certificate-2026-06-25.md"
optional_audit: "tests/hourly_cycle3_k_ig_codomain_finality_certificate_audit.py"
created_at: "2026-06-25"
---

# Hourly Cycle 3 K_IG Codomain and Finality Certificate V1

## 1. Verdict

Verdict:

```text
MULTIPLE / UNDERDEFINED.
```

`K_IG = D_A U` remains the strongest exterior-derivative witness in the current typed
Branch 3 host. It is not final, not axiomatic, and not uniquely selected by the assigned
repo sources.

Cycle 3 does not eliminate the non-exterior candidate classes from Cycle 2. The exact
reason is now sharper:

```text
The current source interface has no CodomainFinalityRule that fixes the IG witness
codomain to exterior 2-forms, fixes the matching parent momentum degree, and proves that
projection/loss data cannot retain coderivative, symmetric, projected, or lower-order
dressed alternatives.
```

Decision table:

| decision | current status | reason |
|---|---:|---|
| `FINAL` | no | no terminal, universal, or uniqueness theorem selects the exterior codomain |
| `AXIOMATIC` | no | no primary/source axiom says the IG witness must be `D_A U` in `Omega^2(Y, ad P)` |
| `MULTIPLE` | yes | at least five first-order local gauge-covariant classes survive current constraints |
| `NONE` | no | `D_A U` is well typed and admissible as an exterior candidate |

No theta/FLRW coefficient packet, dark-energy result, Lambda result, `Z_theta`,
`C_Rtheta`, or `xi_eff` result is claimed here.

## 2. What was derived directly from repo sources

The assigned sources directly support the following.

1. `RESEARCH-POSTURE.md` treats GU as a reconstruction hypothesis and requires explicit
   assumptions, proof/speculation labels, rollback conditions, and constructive obstruction
   handling. Compatibility is not derivation.
2. `process/runbooks/five-lane-frontier-run.md` requires decision-grade lane outputs,
   not summary-only notes, and asks for the first exact missing proof object when a gate
   remains blocked or underdefined.
3. `explorations/gu-typed-operator-action-spine-2026-06-24.md` fixes the proposal-level
   carrier and action spine:

   ```text
   Y = Met_Lor(X), fixed g_Y, G = Sp(64), P -> Y,
   A dynamical, epsilon and beta IG data,
   U = Ad(epsilon^-1) beta,
   theta = A - Gamma(epsilon) - U.
   ```

4. The same typed spine makes the free-beta warning binding: free `beta` plus only a
   theta norm gives `theta = 0`, so the nonzero-theta route needs fixed/constrained IG data
   or a real dynamical `S_IG` branch.
5. `explorations/hourly-cycle1-effect-typed-witness-ig-selector-2026-06-25.md` reduces
   the blocker to a source/projection/finality/loss contract. It does not emit a
   `K_IG` selector.
6. `explorations/hourly-cycle2-k-ig-witness-selection-test-2026-06-25.md` proves the
   current selector state is `MULTIPLE`: `D_A U` is admissible, but coderivative,
   symmetric, projected, and lower-order-dressed classes are not eliminated by the
   current interface.

Therefore the Cycle 3 certificate must decide a codomain/finality question before any
target comparison or downstream coefficient work.

## 3. Strongest positive construction attempt

Assume the strongest Branch 3 typing already available:

```text
U in Omega^1(Y, ad P)
A an Sp(64) connection on P -> Y
D_A the induced covariant exterior derivative
target_inputs_seen = []
```

Then the exterior construction is:

```text
K_ext(U; A) = D_A U in Omega^2(Y, ad P)
P_IG in Omega^2(Y, ad P)
S_parent,ext = int_Y <P_IG, D_A U>_{Q_IG}
```

This construction is the best current positive witness because it is local, first order,
gauge-covariant, representation-natural once `A` is given, and has a clean exterior parent
degree. It also matches the Cycle 2 strongest template.

The attempted codomain finality proof would need this implication:

```text
source witnesses + projection witnesses + loss ledger
  => admitted IG witness codomain is Omega^2(Y, ad P)
  => the only first-order principal symbol allowed is exterior covariant derivative
  => lower-order additions are either fixed by source data or forbidden.
```

The assigned sources do not supply that implication. They supply admissibility of the
exterior construction, not codomain finality.

## 4. First exact obstruction or missing proof object

The first exact obstruction is:

```text
CodomainFinalityRuleForK_IG
```

Operationally:

```text
CodomainFinalityRuleForK_IG:
  SourceWitnesses
  + ProjectionWitnesses
  + LossLedger
  + BoundaryClass
    -> selected codomain, parent momentum degree, principal-symbol class,
       projector policy, and lower-order policy.
```

This rule is missing before `Q_IG`, parent action normalization, boundary variation,
current extraction, conservation, and any physical reduction.

Candidate-class handling:

| class id | current codomain | eliminated? | exact missing rule |
|---|---|---:|---|
| `EXT_DERIVATIVE` | `Omega^2(Y, ad P)` | no | selected if exterior 2-form codomain is source-forced |
| `CODERIVATIVE_TRACE` | `Omega^0(Y, ad P)` or trace sector | no | need a source axiom requiring positive exterior degree and excluding contraction/trace witnesses |
| `SYMMETRIC_DERIVATIVE` | `Sym^2 T^*Y tensor ad P` or trace-free variant | no | need a rule that antisymmetric exterior degree is the only parent-coupled derivative codomain |
| `PROJECTED_DERIVATIVE` | projected IG/source sector | no | need a projector/loss theorem proving projections cannot select a different first-order class |
| `LOWER_ORDER_DRESSED_EXTERIOR` | `Omega^2(Y, ad P)` | no | need a lower-order policy fixing or forbidding source-natural affine additions |

The first obstruction is not type failure. It is non-uniqueness caused by absent codomain,
parent-degree, projection-loss, and lower-order policies.

## 5. Constructive next object

Build:

```text
SourceForcedK_IGCodomainFinalityTheorem_V1
```

It should be a theorem or explicit source axiom package with these fields:

1. `admissible_category`: objects are source-grounded IG witness packets with codomain,
   parent momentum degree, operator class, boundary class, projector policy, and
   lower-order policy.
2. `morphisms_or_preorder`: maps preserve gauge covariance, locality, source projection,
   and loss accounting without target input.
3. `codomain_selector`: proves or asserts that the selected IG witness codomain is
   `Omega^2(Y, ad P)`.
4. `elimination_lemmas`: one lemma each for coderivative/trace, symmetric derivative,
   projected derivative, and lower-order-dressed exterior alternatives.
5. `finality_or_axiom_certificate`: proves `D_A U` is final/unique, or cites the exact
   source axiom that selects it.
6. `replacement_target_check`: replacing target labels leaves the selected packet
   unchanged.

Pass condition:

```text
Exactly one candidate class survives, with selected codomain, parent momentum degree,
boundary class, and lower-order policy before targets.
```

Fail condition:

```text
More than one class survives the source/projection/loss interface.
```

## 6. Impact on GU claim

The relevant GU claim is not promoted.

Allowed current claim:

```text
The typed GU action spine hosts a coherent exterior Branch 3 candidate
K_IG = D_A U, but the current source/projection/finality/loss interface does not select
that candidate uniquely.
```

Forbidden current claim pattern:

```text
Naturalness of D_A U is enough to make it source-forced.
Target performance can choose among surviving K_IG candidates.
Branch 3 has emitted a downstream coefficient packet.
```

Impact:

```text
Branch 3 remains a coherent host, not selected GU dynamics. The next gate is a
codomain/finality theorem or source axiom, not a target-facing computation.
```

## 7. Next meaningful proof/computation step

The next meaningful step is not numerical and not target-facing. It is a source-side
classification proof:

```text
For each surviving candidate class C, specify:
  source inputs,
  codomain,
  parent momentum degree,
  boundary terms,
  projection/loss behavior,
  lower-order freedom,
  and the exact source rule that would eliminate or select it.
```

Then prove one of:

```text
FINAL: D_A U is terminal/unique/final in the admissible witness category.
AXIOMATIC: a named source axiom selects D_A U and excludes the alternatives.
MULTIPLE: more than one class survives; selector remains underdefined.
NONE: no admissible dynamical IG witness survives.
```

Until that is done, downstream physics claims remain blocked by the selector.

## 8. Machine-readable JSON summary

```json
{
  "artifact": "K_IGCodomainAndFinalityCertificate_V1",
  "version": "2026-06-25",
  "mission_posture": "Mission_A_constructive_obstruction",
  "verdict": "MULTIPLE_NO_CODOMAIN_FINALITY_RULE",
  "decision": {
    "FINAL": false,
    "AXIOMATIC": false,
    "MULTIPLE": true,
    "NONE": false
  },
  "candidate_D_A_U_status": "admissible_strongest_exterior_candidate_not_final_not_axiomatic",
  "target_inputs_seen_before_selector": [],
  "target_comparison_permitted": false,
  "derived_from_sources": [
    "research_posture_requires_explicit_assumptions_labels_rollback_and_constructive_obstruction",
    "five_lane_run_requires_decision_grade_artifact_and_first_exact_missing_proof_object",
    "typed_spine_fixes_Y_gY_G_P_A_epsilon_beta_U_theta_at_proposal_level",
    "free_beta_plus_theta_norm_forces_theta_zero",
    "effect_typed_witness_transport_requires_source_projection_finality_loss_contract",
    "cycle2_witness_selection_test_found_multiple_surviving_candidate_classes"
  ],
  "strongest_positive_construction": {
    "candidate": "K_ext(U;A)=D_A U",
    "codomain": "Omega^2(Y,ad P)",
    "parent_degree_if_chosen": "P_IG in Omega^2(Y,ad P)",
    "parent_slot": "int_Y <P_IG,D_A U>_{Q_IG}",
    "positive_claim": "admissible_coherent_exterior_template",
    "selection_claim": false
  },
  "surviving_candidate_classes": [
    {
      "id": "EXT_DERIVATIVE",
      "schematic_operator": "D_A U",
      "codomain": "Omega^2(Y,ad P)",
      "eliminated": false,
      "survives": true,
      "missing_rule": "source_forces_exterior_2_form_codomain_and_selects_exterior_derivative"
    },
    {
      "id": "CODERIVATIVE_TRACE",
      "schematic_operator": "D_A^* U_or_metric_trace_of_nabla_A_U",
      "codomain": "Omega^0(Y,ad P)_or_trace_sector",
      "eliminated": false,
      "survives": true,
      "missing_rule": "source_axiom_excludes_contraction_trace_and_zero_form_codomain"
    },
    {
      "id": "SYMMETRIC_DERIVATIVE",
      "schematic_operator": "Sym(nabla_A U)_possibly_trace_free",
      "codomain": "Sym^2_TstarY_tensor_adP_or_trace_free_variant",
      "eliminated": false,
      "survives": true,
      "missing_rule": "antisymmetric_exterior_degree_is_only_parent_coupled_derivative_codomain"
    },
    {
      "id": "PROJECTED_DERIVATIVE",
      "schematic_operator": "Pi_s_epsilon(nabla_A U)_or_Pi_s_epsilon(D_A U)",
      "codomain": "projected_IG_source_sector",
      "eliminated": false,
      "survives": true,
      "missing_rule": "projection_loss_theorem_excludes_projected_first_order_classes"
    },
    {
      "id": "LOWER_ORDER_DRESSED_EXTERIOR",
      "schematic_operator": "D_A U_plus_L_s_epsilon(U)",
      "codomain": "Omega^2(Y,ad P)",
      "eliminated": false,
      "survives": true,
      "missing_rule": "lower_order_policy_fixes_or_forbids_source_natural_affine_additions"
    }
  ],
  "first_exact_obstruction": {
    "id": "CodomainFinalityRuleForK_IG",
    "missing": true,
    "description": "no source rule fixes selected codomain parent_momentum_degree principal_symbol_class projector_policy and lower_order_policy",
    "blocks_before": [
      "Q_IG",
      "parent_action_normalization",
      "boundary_variation",
      "current_extraction",
      "conservation_proof",
      "physical_reduction"
    ]
  },
  "constructive_next_object": {
    "id": "SourceForcedK_IGCodomainFinalityTheorem_V1",
    "required_outputs": [
      "admissible_category_or_preorder",
      "codomain_selector",
      "parent_momentum_degree_selector",
      "elimination_lemmas_for_non_exterior_classes",
      "projection_loss_theorem",
      "lower_order_policy",
      "finality_or_axiom_certificate",
      "replacement_target_check"
    ],
    "pass_condition": "exactly_one_candidate_class_survives_before_targets",
    "fail_condition": "more_than_one_candidate_class_survives_source_projection_loss_interface"
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
  "claim_impact": {
    "relevant_GU_claim_promoted": false,
    "Branch_3_status": "coherent_host_not_selected_dynamics",
    "selector_status": "underdefined_due_to_missing_codomain_finality_rule",
    "next_gate": "source_side_codomain_finality_not_target_computation"
  },
  "next_meaningful_step": "classify_each_surviving_candidate_by_source_inputs_codomain_parent_degree_boundary_projection_loss_and_lower_order_policy_then_prove_final_axiomatic_multiple_or_none"
}
```

## Sources read

- `RESEARCH-POSTURE.md`
- `process/runbooks/five-lane-frontier-run.md`
- `explorations/hourly-cycle2-k-ig-witness-selection-test-2026-06-25.md`
- `explorations/hourly-cycle1-effect-typed-witness-ig-selector-2026-06-25.md`
- `explorations/gu-typed-operator-action-spine-2026-06-24.md`
