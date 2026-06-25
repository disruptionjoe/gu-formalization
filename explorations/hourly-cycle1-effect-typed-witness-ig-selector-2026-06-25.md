---
title: "Hourly Cycle 1 Effect-Typed Witness Transport for IG Selector"
status: draft
doc_type: hourly_cycle1_effect_typed_witness_ig_selector
verdict: "CONDITIONAL_UNDERDEFINED_K_IG_SELECTOR_NOT_EMITTED"
owned_path: "explorations/hourly-cycle1-effect-typed-witness-ig-selector-2026-06-25.md"
optional_audit: "tests/hourly_cycle1_effect_typed_witness_ig_selector_audit.py"
created_at: "2026-06-25"
---

# Hourly Cycle 1 Effect-Typed Witness Transport for IG Selector

## 1. Verdict

Verdict:

```text
CONDITIONAL / UNDERDEFINED.
```

An `EffectTypedWitnessTransport` interface can reduce the IG/theta blocker to a typed
source/projection/finality/loss contract. It does not close the blocker, because the first
missing proof object remains a source-side witness selector for `K_IG` and the associated
IG field degrees.

Current decision:

```text
EffectTypedWitnessTransport interface emitted: YES, as a contract.
K_IG_selector emitted by repo sources: NO.
K_IG = D_A U source-selected: NO.
theta/FLRW coefficient derivation: NO.
dark-energy or Lambda derivation: NO.
```

The result is positive in the narrow sense that the previous missing object can be made
machine-checkable: any future claimed selector must provide typed source witnesses, a
projection to the IG/theta sector, a finality or uniqueness rule, and an explicit loss
ledger. The result is not positive in the stronger sense of deriving the selector.

## 2. What was derived directly from repo sources

The read sources directly support the following.

1. `RESEARCH-POSTURE.md` requires constructive obstruction handling: when a derivation
   blocks, name the mathematical object that would remove the obstruction, keep rollback
   conditions explicit, and do not treat compatibility as derivation.

2. `process/runbooks/five-lane-frontier-run.md` requires a decision-grade lane result with
   a verdict, strongest positive construction, first exact obstruction, constructive next
   object, and anti-overclaim discipline.

3. `gu-typed-operator-action-spine-2026-06-24.md` fixes the typed action spine at proposal
   level: `Y = Met_Lor(X)`, fixed baseline `g_Y`, `G = Sp(64)`, `P -> Y`, dynamical
   connection `A`, section `s`, IG data `epsilon,beta`, and
   `theta = A - Gamma(epsilon) - Ad(epsilon^-1) beta`. It also records the binding warning
   that free `beta` plus only a theta norm gives `theta = 0`.

4. The same spine says the nonzero-theta route needs one of the named branches. For the
   dynamical route, Branch 3 requires an `S_IG`/`S_IG_dyn` slot and generally changes the
   connection source to a total current `theta_eff`, not bare `theta`.

5. `hourly-cycle1-source-forced-theta-coefficient-packet-2026-06-24.md` blocks the
   theta/FLRW packet before `scalar_theta_mode`, `Z_theta`, `C_Rtheta`, and `xi_eff`.
   It names `SourceForcedIGDynamicsSelector` as the first missing object on the strongest
   Branch 3 route.

6. `hourly-cycle2-source-forced-ig-dynamics-selector-v0-2026-06-24.md` refines the first
   missing datum to `K_IG_selector`: a source-side rule selecting `K_IG`, field degrees,
   and then downstream `Q_IG`, `Z_U`, `V_src`, `S_cross_src`, boundary data, current, and
   conservation data.

7. The strongest candidate already on the table is:

   ```text
   U in Omega^1(Y,ad P),
   P_IG in Omega^2(Y,ad P),
   K_IG(U;A) = D_A U,
   D_A^*F_A = theta_eff
   ```

   but the source files only make this coherent. They do not make it source-forced.

## 3. The strongest positive result

The strongest positive construction is the following interface.

```text
EffectTypedWitnessTransport:
  SourceWitnesses
    -> ProjectedIGWitnessPacket
    -> FinalityCertificate
    -> LossLedger
    -> SelectorDecision
```

The minimal typed contract is:

```text
SourceWitnesses =
  carrier_witness:
    Y = Met_Lor(X), g_Y, G = Sp(64), P -> Y
  action_spine_witness:
    s, A, epsilon, beta, U, theta, allowed variation status
  branch_witness:
    Branch_3_dynamical_IG_total_current or named replacement
  source_rule_witness:
    locality, gauge covariance, allowed order, allowed field degrees,
    allowed pairings, variational boundary class, target_inputs_seen = []

ProjectedIGWitnessPacket =
  projected_source_to_IG_sector,
  candidate field degree of U,
  candidate parent degree of P_IG,
  candidate K_IG,
  candidate Q_IG,
  candidate S_IG_dyn or parent action,
  candidate current terms.

FinalityCertificate =
  uniqueness theorem, terminal/final object property, or explicit source axiom
  selecting exactly one IG packet before targets.

LossLedger =
  data forgotten by projection,
  competing operators not eliminated,
  normalizations not fixed,
  boundary terms not fixed,
  cross terms not fixed,
  target-quarantine status.
```

Under the strongest optimistic construction, the projected packet tries:

```text
K_IG(U;A) = D_A U
U in Omega^1(Y,ad P)
P_IG in Omega^2(Y,ad P)
```

This makes a well-typed parent slot:

```text
int_Y <P_IG, D_A U>_{Q_IG}
```

and, if selected, would place the connection equation in total-current form:

```text
D_A^*F_A = theta_eff.
```

This is the strongest positive result: `EffectTypedWitnessTransport` turns the old blocker
into a typed checklist with a precise pass/fail boundary. A valid future selector must
transport enough source-side evidence to make `D_A U` final or uniquely selected among
the admissible IG operators. The current repo sources do not provide that finality
certificate.

## 4. The first exact obstruction or missing proof object

The first exact obstruction is:

```text
K_IGWitnessFinalityCertificate.
```

Equivalent spelling:

```text
K_IG_selector:
  GU source geometry / tau-plus / typed action spine / effect witnesses
    -> selected K_IG(U;A,epsilon,s) and selected field degrees.
```

The obstruction is not that `D_A U` is ill-typed. It is well typed. The obstruction is
that the transport loses or lacks the source evidence needed to distinguish:

```text
D_A U is a natural admissible Branch 3 operator
```

from:

```text
D_A U is the GU-selected Branch 3 operator.
```

The earliest missing proof object is therefore not `Q_IG`, not `Z_U`, not `theta_eff`, and
not an FLRW scalar reduction. Those are downstream. They depend on the selected operator,
field degree, normalization, and variational boundary class.

Downstream dependency order:

| order | object | status after this interface |
|---:|---|---|
| 1 | `K_IGWitnessFinalityCertificate` / `K_IG_selector` | missing |
| 2 | selected field degrees for `U` and `P_IG` | candidate only |
| 3 | `Q_IG` in the same transported normalization | missing |
| 4 | `Z_U` before target comparison | missing |
| 5 | `V_src` and `S_cross_src` selected or excluded | missing |
| 6 | variational `boundary_data` | missing |
| 7 | exact `S_IG_dyn` or parent action | template only |
| 8 | exact `J_IG` and complete `theta_eff` | schematic only |
| 9 | Noether/projected conservation proof | not written |
| 10 | FLRW scalar-mode and coefficient packet | not emitted |

## 5. The constructive next object that would remove or test the obstruction

Build:

```text
K_IGWitnessSelectionTest_V1.
```

Required contents:

1. Enumerate the admissible IG operators preserved by the source/projection/finality/loss
   interface at the same differential order as `D_A U`.
2. State the exact effect types: source effects, projection effects, finality effects, and
   loss effects.
3. Prove one of the following:

   ```text
   FINAL: D_A U is terminal/unique/final among admissible transported IG witnesses.
   AXIOMATIC: a named primary/source axiom explicitly selects D_A U.
   MULTIPLE: at least two inequivalent operators survive the same witness transport.
   NONE: no admissible dynamical IG operator survives the transport.
   ```

4. If `FINAL` or `AXIOMATIC`, derive the parent field degree of `P_IG`, selected `Q_IG`,
   boundary class, and exact first-order parent action.
5. If `MULTIPLE`, keep the selector underdefined and forbid target-ranking the survivors.
6. If `NONE`, demote the Branch 3 dynamical-IG route and return to constrained/fixed IG
   branches.
7. Run the replacement-target check: replacing DESI/Rubin, `xi_eff`, Lambda, black-hole
   residual, or any other empirical target labels must not change the selected packet.

Pass condition:

```text
The same source witnesses select K_IG, field degrees, Q_IG, Z_U, V_src/S_cross_src status,
boundary data, and a parent action before targets.
```

Fail or block condition:

```text
The effect-typed transport preserves admissibility but does not prove finality.
```

## 6. What this means for the relevant GU claim

The relevant GU claim is not promoted.

Allowed current statement:

```text
The IG/theta blocker can be expressed as an effect-typed witness-transport contract.
The current repo still lacks the witness finality certificate that would select K_IG and
field degrees before target comparison.
```

Forbidden current statements:

```text
EffectTypedWitnessTransport derives dark energy.
EffectTypedWitnessTransport derives Lambda.
EffectTypedWitnessTransport derives Z_theta, C_Rtheta, or xi_eff.
K_IG = D_A U is source-forced because it is natural.
Branch 3 has emitted the theta/FLRW coefficient packet.
```

Impact:

```text
Branch 3 remains the strongest coherent host for a future nonzero-theta total-current
route, but it is still only a host. The selector is now more precisely testable, not
closed.
```

This is a constructive obstruction in the posture sense. If GU is correct along this
route, the next object should be a finality or source-selection theorem for the IG
witness transport. If that theorem fails by multiple surviving operators, the route
remains underdefined. If no operators survive, the Branch 3 route fails.

## 7. Next meaningful proof or computation step

Run `K_IGWitnessSelectionTest_V1` before any theta/FLRW or cosmology comparison.

Concrete sequence:

1. Define the category or typed preorder of admissible transported IG witnesses.
2. List all first-order local gauge-covariant candidates matching the Branch 3 variation
   status and the transported source witnesses.
3. Compute what the projection forgets and record it in the loss ledger.
4. Test whether source/finality effects eliminate every candidate except `D_A U`.
5. If they do, write the selected parent action and derive `J_IG`.
6. If they do not, stop at underdefined selector status.
7. Only after a selected action exists, attempt `theta_eff` conservation and the FLRW
   scalar coefficient packet.

## 8. Machine-readable JSON summary

```json
{
  "artifact": "HOURLY_CYCLE1_EFFECT_TYPED_WITNESS_IG_SELECTOR",
  "version": "2026-06-25",
  "mission_posture": "Mission_A_constructive_obstruction",
  "verdict": "conditional_underdefined",
  "interface_name": "EffectTypedWitnessTransport",
  "interface_emitted_as_contract": true,
  "selector_emitted_by_repo_sources": false,
  "K_IG_source_selected": false,
  "candidate_K_IG": "D_A U",
  "candidate_K_IG_status": "well_typed_admissible_template_not_source_forced",
  "target_comparison_permitted": false,
  "target_inputs_seen_before_selector": [],
  "transport_contract": {
    "source_effects_required": [
      "carrier_witness",
      "action_spine_witness",
      "branch_witness",
      "source_rule_witness",
      "target_inputs_seen_empty"
    ],
    "projection_effects_required": [
      "project_to_IG_sector",
      "preserve_variation_status",
      "preserve_field_degrees",
      "preserve_allowed_pairings",
      "record_projection_loss"
    ],
    "finality_effects_required": [
      "uniqueness_theorem",
      "terminal_or_final_object_property",
      "or_explicit_source_axiom_selecting_one_packet"
    ],
    "loss_effects_required": [
      "competing_operators_not_eliminated",
      "normalization_loss",
      "boundary_data_loss",
      "cross_term_loss",
      "target_quarantine_log"
    ]
  },
  "derived_from_sources": [
    "research_posture_requires_constructive_obstruction_and_no_compatibility_as_derivation",
    "five_lane_run_requires_decision_grade_artifact_and_exact_missing_object",
    "typed_spine_fixes_theta_as_A_minus_Gamma_epsilon_minus_U",
    "free_beta_plus_theta_norm_forces_theta_zero",
    "Branch_3_requires_S_IG_dyn_and_total_current_theta_eff",
    "theta_FLRW_packet_blocks_before_scalar_theta_mode_Z_theta_C_Rtheta_xi_eff",
    "prior_selector_gate_identifies_K_IG_selector_and_field_degrees_as_first_missing_datum"
  ],
  "strongest_positive_result": {
    "type": "typed_contract_not_selector",
    "candidate_branch": "Branch_3_dynamical_IG_total_current",
    "candidate_field_degrees": {
      "U": "Omega^1(Y,ad P)",
      "P_IG": "Omega^2(Y,ad P)"
    },
    "candidate_parent_slot": "int_Y <P_IG,D_A U>_{Q_IG}",
    "candidate_source_law_if_selected": "D_A^*F_A=theta_eff",
    "positive_derivation_claim": false
  },
  "first_exact_obstruction": {
    "id": "K_IGWitnessFinalityCertificate",
    "equivalent_id": "K_IG_selector",
    "missing_status": true,
    "blocks_before": "Q_IG_Z_U_theta_eff_FLRW_coefficients",
    "needed_to_distinguish": "D_A_U_admissible_template_from_D_A_U_GU_selected_operator"
  },
  "ordered_missing_objects": [
    "K_IGWitnessFinalityCertificate",
    "selected_field_degrees_for_U_and_P_IG",
    "Q_IG_selected_in_same_normalization",
    "Z_U_selected_before_targets",
    "V_src_and_S_cross_src_selected_or_excluded",
    "boundary_data",
    "source_forced_S_IG_dyn_or_parent_action",
    "J_IG",
    "theta_eff",
    "Noether_or_projected_conservation_proof",
    "FLRWScalarModeSurvivalCertificate",
    "FLRWQuadraticReductionPacket",
    "Z_theta",
    "C_Rtheta",
    "xi_eff"
  ],
  "anti_overclaim": {
    "GU_derives_dark_energy": false,
    "GU_derives_Lambda": false,
    "GU_derives_Z_theta": false,
    "GU_derives_C_Rtheta": false,
    "GU_derives_xi_eff": false,
    "EffectTypedWitnessTransport_derives_selector": false,
    "Branch_3_emits_theta_FLRW_packet": false,
    "candidate_naturalness_counts_as_source_selection": false
  },
  "rollback_conditions": [
    "K_IG_chosen_by_naturalness_not_source",
    "EffectTypedWitnessTransport_promoted_from_contract_to_selector_without_finality",
    "projection_loss_hides_competing_operator",
    "field_degrees_not_source_selected",
    "Q_IG_not_selected",
    "Z_U_target_fitted",
    "V_src_or_S_cross_src_chosen_after_target",
    "boundary_data_chosen_after_target",
    "S_IG_dyn_template_promoted_without_selector",
    "theta_eff_asserted_without_delta_A_current",
    "Noether_identity_not_written",
    "bare_theta_source_retained_in_Branch_3",
    "bare_Lambda_inserted",
    "bare_Rtheta_inserted",
    "Z_theta_or_C_Rtheta_claimed_without_FLRW_reduction",
    "xi_eff_fitted_not_generated",
    "dark_energy_derivation_claimed_before_selector_closes",
    "DESI_Rubin_window_used_upstream",
    "replacement_or_withheld_target_check_changes_selector"
  ],
  "constructive_next_object": {
    "id": "K_IGWitnessSelectionTest_V1",
    "do_next": true,
    "avoid_next": "theta_FLRW_or_cosmology_comparison_before_witness_finality",
    "required_outputs": [
      "admissible_operator_list",
      "effect_type_signature",
      "projection_loss_ledger",
      "finality_or_source_axiom_status",
      "selected_or_multiple_or_none_decision",
      "replacement_target_check",
      "downstream_selector_fields_if_final"
    ],
    "possible_decisions": [
      "FINAL",
      "AXIOMATIC",
      "MULTIPLE",
      "NONE"
    ]
  },
  "claim_impact": {
    "relevant_GU_claim_promoted": false,
    "Branch_3_status": "coherent_host_not_selected",
    "selector_status": "more_precisely_testable_not_closed",
    "theta_FLRW_packet_status": "blocked_downstream_of_K_IG_selector"
  }
}
```
