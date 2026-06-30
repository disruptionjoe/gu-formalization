---
title: "Hourly Cycle 3 FR3-GU Filtered-Readout Witness Gate"
date: "2026-06-24"
status: exploration_gate
doc_type: frontier_gate
verdict: "PARK_OBJ_TAF_WITNESS_NOT_INSTANTIATED"
owned_path: "explorations/hourly-cycle3-fr3-gu-filtered-readout-witness-gate-2026-06-24.md"
companion_audit:
  - "tests/hourly_cycle3_fr3_gu_filtered_readout_witness_gate_audit.py"
depends_on:
  - "RESEARCH-POSTURE.md"
  - "process/runbooks/five-lane-frontier-run.md"
  - "explorations/cycle3-taf-transport-or-close-gate-2026-06-24.md"
  - "explorations/time-as-finality-crosswalk/reciprocal-bridge-ten-lens-review-2026-06-24.md"
  - "explorations/time-as-finality-crosswalk/fr3-filtered-sheaf-non-collapse-example-2026-06-22.md"
  - "active-research/signed-readout/theorem-statement-v1-2026-06-23.md"
  - "explorations/hourly-cycle2-qft-source-mode-quotient-data-ledger-2026-06-24.md"
---

# Hourly Cycle 3 FR3-GU Filtered-Readout Witness Gate

## 1. Verdict

Verdict: **park**.

Current sources do not instantiate a FR3-GU filtered-readout witness where a GU
readout changes with the filtration while the final object is fixed.

They do establish three useful pieces:

1. FR3 supplies a genuine transient class in a filtered sheaf:
   `omega_1 in H^1(S^1, C_{S^1})`, with `H^1(S^1, C_{S^1}) != 0` and
   `H^1(S^1, F) = 0` for the final flasque sheaf `F`.
2. The signed-readout theorem supplies a named GU readout candidate:
   `R_GU = R_w^GU-gen : E_GU -> Z`, the monotone Z-valued GU generation-count
   readout with all weights `+1` and `R_GU(e_max) = 24`, conditional on the
   theorem's GU-instance gates.
3. The QFT source-mode ledger supplies a useful anti-import discipline: do not
   treat channels, controls, target states, identity pairings, or observer
   fixtures as source-derived GU theorem inputs.

The missing object is still the theorem-transport object:

```text
Theta_tau : H^1(X, F_tau) -> Input(R_GU)
```

where `Input(R_GU)` must be an actual input to the GU readout theorem, such as
the evidence state `e in E_GU`, the weight function `w_GU`, or a named theorem
hypothesis that changes the readout. Without `Theta_tau`, the expression
`R_GU(F_tau)` is ill-typed: `R_GU` consumes signed-readout evidence data, while
FR3 supplies sheaf cohomology of intermediate record sheaves.

Decision:

```text
PARK_OBJ_TAF_AS_EXPLORATION_ONLY
FR3_GU_FILTERED_READOUT_WITNESS_NOT_INSTANTIATED
NO_GU_THEOREM_TRANSPORT_CLAIM
```

This is not a dismissal of the FR3 object. It is a contract-level decision:
the formal transient exists, but it has not been connected to a GU theorem
input.

## 2. Witness Contract Fields

A passing witness would have to supply all fields below and then prove
filtration-sensitive readout:

```text
same final object:
  colim_tau F_tau = colim_tau F'_tau = F_final

transient class:
  omega_tau in H^1(X, F_tau)

readout sensitivity:
  R_GU(F_tau, omega_tau) != R_GU(F'_tau, 0)

anti-absorption:
  the difference is not only final Cech cohomology, rate/cadence policy,
  a chosen measurement channel, or imported target data.
```

The strongest current contract filling is:

| field | current filling | status |
|---|---|---|
| `R_GU` | `R_w^GU-gen : E_GU = N_0^{(V_exp)} -> Z`, all `w(v)=+1`, `R_GU(e_max)=24` | named, but not coupled to filtered sheaves |
| final object | `F = AllFunctions_{S^1,C}`, the flasque sheaf of all C-valued set-theoretic functions | supplied by FR3 |
| filtration A | `F^A_1 = C_{S^1} subset F^A_2 = F` | supplied by FR3 |
| filtration B | `F^B_1 = 0 subset F^B_2 = F` | admissible same-final control filtration |
| same final object | `F^A_2 = F^B_2 = F` | passes |
| transient class | `omega_1 != 0` in `H^1(S^1, C_{S^1}) ~= C` | supplied by FR3 |
| death in final object | image of `omega_1` in `H^1(S^1, F)` is `0` because `F` is flasque | supplied by FR3 |
| anti-final-cohomology absorption | transient is not determined by `H^1(S^1,F)` | passes for FR3 object |
| anti-rate absorption | index is filtration content, not speed or cadence | passes for FR3 object |
| anti-channel/import absorption | QFT ledger forbids treating a channel/control/target fixture as GU source data | guard available |
| readout sensitivity | no value of `R_GU` changes because `E_GU`, `w_GU`, and `e_max` are unchanged | fails / missing proof object |

Thus the contract is named but not satisfied. The absent field is not another
example of filtered sheaf non-collapse; it is the map from that non-collapse
into the signed-readout theorem's domain.

## 3. What Current FR3/Signed-Readout/QFT Sources Establish

`RESEARCH-POSTURE.md` and the five-lane runbook set the standard: pursue
high-information GU reconstruction targets, but do not promote compatibility
to derivation, do not hide target data inside a reconstruction, and identify
the first exact missing proof object.

`cycle3-taf-transport-or-close-gate-2026-06-24.md` already found no current
TAF-to-GU theorem transport. Its wake trigger was exactly this FR3-GU
filtered-readout witness:

```text
named GU readout
two filtrations with the same final object
computed transient class
proof that the GU readout differs
anti-absorption check
```

`reciprocal-bridge-ten-lens-review-2026-06-24.md` gives the theorem-shaped
interface:

```text
S : Compat_G^MLTT -> FiltSh(C)
R : FiltSh(C) -> ReadoutValues
```

but it explicitly says promotion requires a GU-relevant readout sensitive to
the filtration, not only to the final sheaf.

`fr3-filtered-sheaf-non-collapse-example-2026-06-22.md` establishes the
filtered object itself. On `X = S^1`, with `F = AllFunctions_{S^1,C}` flasque:

```text
H^1(S^1, C_{S^1}) ~= C != 0
H^1(S^1, F) = 0
```

So a transient class can exist at an intermediate filtration stage and die in
the final sheaf. FR3 also establishes that this is structural filtration data,
not issuance rate data.

`active-research/signed-readout/theorem-statement-v1-2026-06-23.md` supplies
the readout theorem. Its GU instance is the monotone side:

```text
E_GU = N_0^{(V_exp)}
w(v) = +1 for every GU mode event v
R_GU(e_max) = sum_v 1 = 24
```

The theorem proves monotone provenance and a signed-readout boundary. It does
not define `R_GU` on filtered sheaves, transient Cech classes, or observer
record filtrations.

`hourly-cycle2-qft-source-mode-quotient-data-ledger-2026-06-24.md` supplies the
anti-import screen. It blocks promotion when the apparent readout change is
inserted through an identity Gram, Bell state, Pauli control, free vacuum,
Hadamard/Fock state, target CHSH state, Stinespring/CPTP channel, or a silent
direct-sum-to-tensor-product import. That discipline applies here: a chosen
observer channel from `omega_1` to a numerical readout is not a GU theorem
transport unless the source branch derives the channel.

## 4. Strongest Positive Witness Attempt

The strongest positive attempt is the following conditional schema.

Keep the final record object fixed:

```text
F_final = F = AllFunctions_{S^1,C}
```

Compare two filtrations:

```text
Filtration A:
  F^A_1 = C_{S^1}
  F^A_2 = F
  omega_1 in H^1(S^1, F^A_1) ~= C, omega_1 != 0

Filtration B:
  F^B_1 = 0
  F^B_2 = F
  H^1(S^1, F^B_1) = 0
```

Both end at the same flasque final sheaf. They differ at the intermediate
record stage. This is a real FR3 separation.

Now name the GU readout:

```text
R_GU = R_w^GU-gen : E_GU -> Z
R_GU(e) = sum_v n_v w(v)
w(v) = +1
R_GU(e_max) = 24
```

For a passing transport, one would need a derived connector such as:

```text
Theta_A,1(omega_1) = delta_A in E_GU or Delta w_GU
Theta_B,1(0)       = delta_B in E_GU or Delta w_GU
R_GU(e_max + delta_A) != R_GU(e_max + delta_B)
```

No current source supplies `Theta`. If `E_GU`, `w_GU`, and `e_max` are left as
the signed-readout theorem defines them, then the two filtrations do not change
the GU readout:

```text
R_GU^A = R_GU(e_max) = 24
R_GU^B = R_GU(e_max) = 24
```

The attempted witness therefore has a real transient class but no
readout-sensitive theorem input. Any numerical difference assigned at this
point would be imported by hand.

## 5. First Exact Obstruction or Missing Proof Object

The first exact obstruction is a domain mismatch:

```text
FR3 data:
  omega_tau in H^1(X, F_tau)

Signed-readout GU theorem input:
  e in E_GU = N_0^{(V_exp)}
  w_GU : V_exp -> Z

Missing:
  a typed, source-derived map from the first object to the second.
```

The missing proof object is:

```text
FilteredReadoutCoupling_GU

data:
  X_rec, F_tau, F'_tau, F_final
  R_GU : E_GU -> Z or another named GU theorem readout
  Theta_tau : H^1(X_rec, F_tau) -> Input(R_GU)
  Theta'_tau : H^1(X_rec, F'_tau) -> Input(R_GU)

conditions:
  colim F_tau = colim F'_tau = F_final
  omega_tau != 0 and dies or changes in H^1(X_rec, F_final)
  R_GU(Theta_tau(omega_tau)) != R_GU(Theta'_tau(0))
  Theta is derived from GU source data, not a chosen observer channel
  the readout difference survives the anti-absorption checks
```

Until that object exists, `S : Compat_G^MLTT -> FiltSh(C)` and
`R : FiltSh(C) -> ReadoutValues` remain a proposed interface. They are not a
GU theorem transport.

## 6. Park/Pursue/Close Decision for OBJ-TAF

Decision: **park**, not pursue.

OBJ-TAF remains parked because the wake-triggered witness is not instantiated.
The current sources justify retaining one precise open contract, not opening a
live GU theorem lane:

```text
Open contract:
  build FilteredReadoutCoupling_GU or close the route

Current lane state:
  FR3 object real
  R_GU named
  same-final filtrations named
  omega_tau named
  anti-absorption guard available
  readout sensitivity absent
```

Do not cite this artifact as evidence that TAF changes a GU theorem. It only
records the exact missing object needed for such a claim.

Close condition:

```text
If the next attempt again supplies only filtered-sheaf non-collapse plus
readout analogy, with no FilteredReadoutCoupling_GU, close OBJ-TAF for GU
theorem-transport purposes and retain only observer-protocol hygiene.
```

Pursue condition:

```text
Pursue only if a source-derived Theta_tau maps the transient class into an
actual input of R_GU and proves a readout difference for two filtrations with
the same final object.
```

## 7. Rollback/Falsification Conditions

| condition | decision |
|---|---|
| no named `R_GU` | invalid witness contract |
| no two filtrations with the same final object | invalid same-final witness |
| no computed `omega_tau` | invalid transient-class witness |
| `omega_tau` is only `H^1(X,F_final)` | absorbed by final Cech cohomology |
| the index is rate, cadence, deadline, or observer latency | absorbed by rate/protocol language |
| the readout change is supplied by a chosen channel or measurement fixture | rollback imported channel |
| the readout change uses Bell, Pauli, identity Gram, free-vacuum, Hadamard/Fock, CHSH target, Stinespring, or CPTP data as source | rollback target import |
| `R_GU` consumes unchanged `E_GU`, `w_GU`, and `e_max` | no witness; readout invariant |
| `Theta_tau` is noncanonical or chosen to force the target value | rollback target fitting |
| the two filtrations have different final objects | fail fixed-final-object condition |
| `R_GU` differs only because final sheaves differ | fail same-final sensitivity |
| a clean `Theta_tau` is source-derived and changes `R_GU` under same-final filtrations | pursue OBJ-TAF as theorem transport |

The falsification-friendly negative result is:

```text
For the currently named R_GU = R_w^GU-gen, the FR3 transient alone does not
change the readout. With no coupling map, both filtrations leave R_GU = 24.
```

## 8. Machine-Readable JSON Summary

```json
{
  "artifact": "HOURLY_CYCLE3_FR3_GU_FILTERED_READOUT_WITNESS_GATE",
  "date": "2026-06-24",
  "verdict": "PARK_OBJ_TAF_WITNESS_NOT_INSTANTIATED",
  "status": "park",
  "obj_taf_decision": "park",
  "witness_instantiated": false,
  "readout_sensitivity_instantiated": false,
  "gu_theorem_transport_claim": false,
  "taf_changes_gu_proof_obligation": false,
  "not_an_analogy_note": true,
  "contract_level_attempt_completed": true,
  "witness_contract": {
    "R_GU": {
      "id": "R_GU_signed_readout_generation_count",
      "formal_name": "R_w^GU-gen",
      "domain": "E_GU=N_0^(V_exp)",
      "codomain": "Z",
      "formula": "R_GU(e)=sum_v n_v w(v)",
      "weights": "w(v)=+1_for_all_v",
      "readout_value_if_independent": 24,
      "source": "active-research/signed-readout/theorem-statement-v1-2026-06-23.md",
      "status": "named_not_coupled_to_filtered_sheaves"
    },
    "final_object": {
      "id": "F_all_functions_S1_C",
      "space": "S^1",
      "description": "flasque_sheaf_of_all_C_valued_set_theoretic_functions",
      "H1_final": "0"
    },
    "two_filtrations": [
      {
        "id": "filtration_A_FR3_transient",
        "stages": [
          "C_S1",
          "F_all_functions_S1_C"
        ],
        "final_object": "F_all_functions_S1_C",
        "intermediate_H1": "H^1(S^1,C_S1)=C_nonzero",
        "has_transient_class": true
      },
      {
        "id": "filtration_B_same_final_control",
        "stages": [
          "zero_sheaf",
          "F_all_functions_S1_C"
        ],
        "final_object": "F_all_functions_S1_C",
        "intermediate_H1": "H^1(S^1,0)=0",
        "has_transient_class": false
      }
    ],
    "same_final_object": true,
    "omega_tau": {
      "id": "omega_1",
      "stage": "tau=1",
      "group": "H^1(S^1,C_S1)",
      "value": "nonzero_generator_or_nonzero_class_in_C",
      "dies_in_final_H1": true,
      "image_in_H1_final": "0"
    },
    "anti_absorption": {
      "not_final_H1_absorption": true,
      "not_rate_or_cadence": true,
      "not_chosen_channel_or_target_import": true,
      "qft_import_screen_applied": true,
      "readout_sensitivity_check": "failed_missing_FilteredReadoutCoupling_GU"
    }
  },
  "current_sources_establish": {
    "research_posture": "constructive_GU_reconstruction_with_no_target_smuggling",
    "five_lane_runbook": "decision_grade_artifact_with_exact_obstruction_required",
    "cycle3_taf_gate": "no_current_TAF_to_GU_transport_and_FR3_wake_trigger_defined",
    "reciprocal_bridge": "proposed_S_to_FiltSh_and_R_to_ReadoutValues_interface_only",
    "FR3": "transient_filtered_sheaf_class_exists_and_is_structural_not_rate",
    "signed_readout": "R_GU_generation_count_readout_named_but_domain_is_E_GU_not_FiltSh",
    "qft_ledger": "anti_import_screen_for_channels_controls_targets_and_identity_data"
  },
  "strongest_positive_witness_attempt": {
    "final_object_fixed": true,
    "filtration_difference_computed": true,
    "transient_class_computed": true,
    "R_GU_named": true,
    "required_connector": "Theta_tau:H^1(X,F_tau)->Input(R_GU)",
    "connector_supplied_by_current_sources": false,
    "result": "conditional_schema_only",
    "readout_under_current_inputs": {
      "filtration_A": 24,
      "filtration_B": 24,
      "different": false
    }
  },
  "first_exact_obstruction": {
    "id": "FilteredReadoutCoupling_GU",
    "type": "missing_typed_theorem_transport",
    "why_first": "domain_mismatch_between_FR3_H1_transient_and_signed_readout_E_GU_inputs",
    "missing_map": "Theta_tau:H^1(X,F_tau)->Input(R_GU)",
    "input_side": "omega_tau_in_H^1(X,F_tau)",
    "output_side_options": [
      "evidence_state_e_in_E_GU",
      "weight_function_w_GU",
      "named_GU_theorem_hypothesis",
      "source_derived_observer_shadow_readout_input"
    ],
    "required_properties": [
      "typed_domain_codomain",
      "same_final_object_preserved",
      "nonzero_transient_changes_R_GU",
      "source_derived_not_chosen_channel",
      "not_rate_or_cadence_restatement",
      "not_final_Cech_cohomology_only",
      "not_target_fitted"
    ]
  },
  "obj_taf_decision_detail": {
    "current_decision": "park",
    "do_not_claim": [
      "TAF_changes_GU_theorem",
      "FR3_transient_implies_GU_generation_readout_change",
      "observer_finality_bypasses_GU_no_go",
      "chosen_channel_counts_as_theorem_transport"
    ],
    "pursue_condition": "source_derived_FilteredReadoutCoupling_GU_with_R_GU_difference",
    "close_condition": "next_attempt_has_only_noncollapse_plus_readout_analogy_without_Theta_tau"
  },
  "rollback_falsification_conditions": [
    "missing_named_R_GU_invalid_contract",
    "missing_two_same_final_filtrations_invalid_contract",
    "missing_omega_tau_invalid_contract",
    "omega_tau_only_final_H1_absorbed_by_final_Cech",
    "rate_cadence_deadline_or_latency_absorption",
    "chosen_channel_or_measurement_fixture_import",
    "Bell_Pauli_identity_Gram_free_vacuum_Hadamard_Fock_CHSH_target_Stinespring_CPTP_import",
    "unchanged_E_GU_w_GU_e_max_implies_R_GU_invariant",
    "noncanonical_Theta_tau_target_fitting",
    "different_final_objects_fail_same_final_condition",
    "clean_source_derived_Theta_tau_with_R_GU_difference_promotes_to_pursue"
  ],
  "next_meaningful_object": "FilteredReadoutCoupling_GU"
}
```
