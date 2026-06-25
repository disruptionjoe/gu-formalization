---
title: "Cycle 1 Observer-Shadow Phi_obs Contract Gate"
date: "2026-06-24"
status: exploration
doc_type: observer_shadow_phi_obs_contract_gate
verdict: "UNDERDEFINED_CONTRACT_GATE"
owner: "Cycle 1 Worker"
depends_on:
  - "RESEARCH-POSTURE.md"
  - "process/runbooks/five-lane-frontier-run.md"
  - "explorations/cycle3-connes-control-load-bearing-audit-2026-06-24.md"
  - "explorations/type-ii1-selector-or-nogo-theorem-2026-06-24.md"
  - "explorations/sm-gauge-higgs-finite-control-extraction-ledger-2026-06-24.md"
  - "explorations/finite-control-provenance-audit-2026-06-24.md"
  - "canon/type-ii1-spectral-sm-checklist.md"
---

# Cycle 1 Observer-Shadow Phi_obs Contract Gate

## 1. Verdict

**Verdict: UNDERDEFINED_CONTRACT_GATE.**

The repo cannot currently declare an exact finite Connes-channel observer map

```text
Phi_obs^CC:
  GU / Type II1 substrate data
  -> (A_F, H_F, D_F, J_F, gamma_F; G_SM/Z_6; K_SM; generation split)
```

because no target-free operation in the cited sources produces the finite Connes algebra
`A_F = C + H + M_3(C)`, the global SM gauge quotient `G_SM/Z_6`, the finite one-generation
module, or exactly three generation sectors. Existing Type II1 constructions can host or
embed finite CC data only after those data are supplied.

The repo also cannot currently declare a GU-native replacement observer shadow. A
replacement shadow is allowed in principle, but the cited sources do not specify a
replacement observer algebra or gauge object, chiral representation list, generation
decomposition, Higgs/action package, and anomaly certificate that can replace the finite
Connes controls.

The strongest positive result is therefore a **Phi_obs contract gate**:

```text
observer-facing SM claim
  requires either
    exact finite Connes-channel Phi_obs^CC
  or
    declared replacement-shadow Phi_obs^rep with equal or stronger controls.
```

Finite Connes control is not a primary GU substrate axiom. It is a target-facing control
case, observer-shadow certificate, and anti-smuggling comparator. GU may remain
quaternionic or Type II1/semifinite at substrate level, but any observer-facing Standard
Model claim must pass through an explicit `Phi_obs` contract.

## 2. Exact finite Connes-channel vs replacement-shadow decision

Current decision:

```text
phi_obs_decision:
  exact_finite_connes_channel: false
  replacement_shadow_declared: false
  current_status: contract_only_underdefined
  allowed_current_claim: no observer-facing SM derivation; contract gate only
```

| option | current decision | reason | promotion requirement |
|---|---|---|---|
| Exact finite Connes-channel `Phi_obs^CC` | Not declared | The repo lacks a functorial target-free map from GU/Type II1 data to the finite CC tuple. Current positive lanes import or host `A_F`, `H_F`, `K_SM`, and generation count. | Define `Phi_obs^CC` from fixed substrate data, verify real/grading/order-one controls, compute `A_F`, `G_SM/Z_6`, `K_SM`, and generation split without forbidden target inputs. |
| GU-native replacement shadow `Phi_obs^rep` | Not declared | No replacement codomain has been specified. "Not finite CC" is not a control package. | Specify the replacement observer algebra/gauge object, chiral fermion list, Higgs/action data, anomaly certificate, and rollback conditions at least as strong as the finite control case. |
| Contract gate | Declared | The cited sources jointly require finite-control shadow or declared replacement shadow before physics-facing claims. | Maintain provenance ledger and audits until one of the two observer-shadow modes is constructed. |

The decision is not that GU must literally become the finite Connes model. The decision is
that the observer-facing claim must name what the observer sees and prove that the visible
data are selected rather than smuggled in.

## 3. What was derived directly from repo sources

The following points are direct consequences of the read-first source set.

| source | direct use in this gate |
|---|---|
| `RESEARCH-POSTURE.md` | The repo pursues GU reconstruction as a working hypothesis, but forbids target smuggling, verdict inflation, compatibility-as-derivation, and hidden imported data. |
| `five-lane-frontier-run.md` | This artifact must make a decision, identify the first missing proof object, state rollback conditions, and avoid treating hosted data as selected data. |
| `cycle3-connes-control-load-bearing-audit` | Finite Connes control is load-bearing for observer-facing SM shadow claims, not as a mandatory primary GU substrate law. It requires exact finite channel or declared replacement shadow. |
| `type-ii1-selector-or-nogo-theorem` | Current instantiated Type II1 selector classes are host-only or no-go as explanatory SM selectors. Fixed-data rigidity remains open but uninstantiated. |
| `sm-gauge-higgs-finite-control-extraction-ledger` | The GU carrier derives a quaternionic ambient carrier and relative Pati-Salam one-generation branch, and hosts Higgs quantum numbers. It does not derive the full SM finite-control package. |
| `finite-control-provenance-audit` | The first forbidden target is `A_F`; if bypassing finite CC, the first gauge-level failure is `G_SM/Z_6`. Target data must be classified as derived, hosted, imported, failed, or open. |
| `type-ii1-spectral-sm-checklist` | A Type II1 or non-embeddable internal extension is not constructed. It must preserve or replace finite CC controls, and the naive GU section-pullback route does not supply them. |

No source read for this gate proves that SM gauge, Higgs, or three-generation data are
derived from current GU or Type II1 data. The positive repo content is branch evidence,
hosting capacity, and a sharply specified selector/shadow obstruction.

## 4. Strongest positive contract

The minimum `Phi_obs` contract for any observer-facing SM claim is:

```text
Phi_obs contract:
  name:
    Phi_obs^CC or Phi_obs^rep
  domain:
    fixed GU / Type II1 substrate data, with all inputs listed
  codomain:
    observer-facing algebra/gauge/fermion/Higgs/action/anomaly data
  selection rule:
    explicit map or functor, not a target table lookup
  provenance:
    every target datum marked derived, derived_relative, hosted, imported, failed, or open
  rollback:
    exact conditions under which the observer-facing claim demotes
```

Required fields:

| field | minimum content |
|---|---|
| `observer_algebra_or_gauge_object` | Either `A_F = C + H + M_3(C)` and its gauge quotient for exact finite CC, or the replacement algebra/gauge object. |
| `chiral_fermion_representation_list` | The visible chiral fermions, including conjugation convention and whether right-handed neutrino content is present. |
| `generation_decomposition` | The sector decomposition and whether the count is selected, imported, hosted, or open. |
| `real_structure_and_grading_signs` | The observer-facing `J`, `gamma`, KO signs, and whether the GU quaternionic sign is retained, twisted, or forgotten. |
| `dirac_and_first_order_control` | `D`, bounded commutators, order-zero/order-one or declared replacement first-order condition. |
| `higgs_scalar_and_action_status` | Higgs quantum-number slot, physical scalar map, potential/action status, and whether EWSB is derived, imported, or open. |
| `anomaly_freed_hopkins_input` | The actual observer-facing mode list used for perturbative and global anomaly checks. |
| `substrate_mode_policy` | Which GU/Type II1 modes are forgotten, retained, projected, or shown invisible, with no deletion by fiat. |
| `target_data_provenance` | Row-by-row status for `A_F`, `G_SM/Z_6`, `K_SM/T_1`, `T_3`, Higgs, spectral action, and anomaly shadow. |
| `replacement_tests` | Nearest `n = 2,4` or structural replacements for any visible-three or target-looking feature. |
| `rollback_conditions` | Target-smuggling and overclaim conditions that demote the claim. |

Minimum target-data provenance ledger:

| target datum | current status | required promotion object | target-smuggling rollback |
|---|---|---|---|
| `A_F = C + H + M_3(C)` | missing; imported in current finite CC host lanes | Target-free selector or `Phi_obs^CC` computation producing the finite algebra from fixed data. | Any proof that supplies `A_F`, its summands, or the finite CC tuple as an input is host/import only. |
| `G_SM/Z_6` | missing; failed as target-free current output | Gauge selector deriving local Lie algebra plus global central quotient. | Naming `G_SM`, using the central `Z_6` as target input, or citing finite CC inner fluctuations after importing `A_F`. |
| One-generation module `K_SM/T_1` | relative branch evidence only; finite module imported in CC lanes | Observer map that outputs the chiral module and hypercharge lattice without attaching `K_SM`. | External `K_SM`, ordinary SM fermion table, or anomaly-free packet used as input. |
| Exactly three generations `T_3` | not selected by current Type II1 classes | Fixed-data rigidity, standard-invariant, index, or Connes-channel obstruction that blocks `n != 3`. | `n = 3`, `C3`, index 3, D4 arms, three projections, `dim H_F = 96`, or `K_SM tensor C^3` supplied as input. |
| Higgs scalar and potential | quantum-number slot hosted; physical scalar/action open | Gauge-covariant section projection plus effective potential/action computation. | Physical Higgs doublet, nonzero projection, negative mass squared, or Mexican-hat potential inserted from target physics. |
| Anomaly/Freed-Hopkins shadow | conditional for exactly ordinary SM shadow; full GU/Type II1 shadow open | Complete anomaly computation for the actual observer-facing mode list. | Assuming ordinary anomaly-free SM content, deleting extra modes, or using anomaly cancellation to select the packet. |
| Spectral action / low-energy Lagrangian | not recovered from current substrate data | Finite spectral action through exact `Phi_obs^CC`, or replacement action with matching control. | Citing the finite spectral action after importing finite CC data as if it were GU-derived. |

Only rows marked `derived` by such a ledger may support observer-facing SM emergence
language. `derived_relative`, `hosted`, `imported`, `failed`, and `open` rows must be cited
with those limits.

## 5. First exact obstruction or missing proof object

The first decision object is:

```text
P0:
  Choose exact finite Connes-channel Phi_obs^CC
  or declare a GU-native replacement-shadow Phi_obs^rep.
```

The repo has not supplied either object.

If the exact finite Connes-channel route is chosen, the first local bridge check is:

```text
FC-EPSILON:
  verify J_twisted D_GU = + D_GU J_twisted
  on the full pulled-back GU operator, including shiab, section-pullback, and mixing terms.
```

Passing `FC-EPSILON` would only make KO-6 contact plausible. It would not select the finite
algebra. The first target-data missing object would still be:

```text
A_F-SELECTOR:
  fixed GU / Type II1 data
  -> A_F = C + H + M_3(C)
  without naming A_F, C, H, M_3(C), finite CC tuple, or SM target data in the input.
```

If the replacement-shadow route is chosen, the first missing object is:

```text
REPLACEMENT-CODOMAIN:
  a specified observer algebra/gauge object and chiral matter/action/anomaly package
  that replaces finite CC controls rather than merely bypassing them.
```

Rollback conditions for target smuggling:

1. Roll back to `host/import` if `A_F`, finite CC tuple, `G_SM/Z_6`, `K_SM`, `n = 3`, `C3`,
   index 3, D4 arms, three projections, `dim H_F = 96`, ordinary anomaly-free SM content,
   or physical Higgs data appear as selector inputs.
2. Roll back a generation selector if the same proof works after `n = 2` or `n = 4`
   replacement, or if no named obstruction blocks those replacements.
3. Roll back an anomaly claim if extra GU/Type II1 modes survive in the observer shadow and
   no complete anomaly computation is supplied.
4. Roll back a Higgs emergence claim if the proof only shows an ambient representation slot
   and not a nonzero section-specific scalar plus potential/action.
5. Roll back exact finite CC contact if `FC-EPSILON` fails for the proposed twisted real
   structure.
6. Roll back any claim that treats finite Connes control as a primary GU substrate axiom
   rather than as an observer-facing certificate or comparator.

## 6. Impact for Type II1/SM selector claims

| claim family | impact |
|---|---|
| `TYPEII1-HOST` | Still conditionally useful, but only as host/import until `Phi_obs` computes the observer-facing data without target inputs. |
| `TYPEII1-SELECTOR` | Negative for current instantiated classes. Fixed-data rigidity remains open but empty and must include `Phi_obs`, replacement tests, and provenance rows. |
| Exact finite Connes-channel | Underdefined. The repo has controls and obstruction names, not a constructed exact channel. |
| Replacement observer shadow | Underdefined. It is permitted by the Cycle 3 reframing, but no replacement control package is specified. |
| SM gauge group | Not derived. Pati-Salam branch evidence is real but does not select `G_SM/Z_6`. |
| Higgs sector | Hosted at quantum-number level; physical scalar, projection, potential, and EWSB remain open. |
| Generation count | Not selected by current Type II1 classes. GU RS/index routes are separate open analytic gates, not closure here. |
| Anomaly/Freed-Hopkins compatibility | Conditional only after the actual observer-facing mode list is known. Exact ordinary SM shadow passes; extra visible modes require a new computation. |

This gate therefore blocks observer-facing SM promotion while preserving the constructive
Mission A target: build the missing observer-shadow object rather than making finite CC a
substrate axiom.

## 7. Next meaningful proof or computation

The next meaningful step is not another visible-three toy or another statement that the
ambient carrier contains useful representation slots. The next step must construct or
reject an observer map.

Priority order:

1. **Mode declaration.** Decide whether the next lane attempts `Phi_obs^CC` or
   `Phi_obs^rep`. A claim that does not choose a mode remains contract-only.
2. **Exact-channel first check.** If exact finite CC is chosen, compute `FC-EPSILON` for
   the proposed `J_twisted` against the full pulled-back `D_GU`.
3. **Target-free selector.** Build fixed data
   `(N subset M, tau, A, H, D, J, gamma, Phi_obs)` not parameterized by `A_F`, `G_SM`,
   `K_SM`, or `n = 3`, then compute whether `Phi_obs` selects `A_F` or `G_SM/Z_6`.
4. **Replacement codomain.** If finite CC is not chosen, write the replacement observer
   algebra/gauge/matter/Higgs/action/anomaly package and prove which finite controls it
   preserves or replaces.
5. **Replacement audit.** For any generation-sector output, run the nearest `n = 2,4`
   replacements and identify the first obstruction.
6. **Anomaly-shadow audit.** Once `Phi_obs` is explicit, list all observer-facing modes and
   run anomaly/Freed-Hopkins checks on that actual list.

## 8. Machine-readable JSON summary

```json
{
  "artifact": "hourly_cycle1_observer_shadow_phi_obs_contract",
  "date": "2026-06-24",
  "verdict": "UNDERDEFINED_CONTRACT_GATE",
  "finite_connes_control_role": "target_facing_certificate_not_primary_GU_substrate_axiom",
  "no_observer_facing_sm_derivation_claim": true,
  "phi_obs_decision": {
    "exact_finite_connes_channel": false,
    "replacement_shadow_declared": false,
    "current_status": "contract_only_underdefined",
    "allowed_current_claim": "requires_explicit_Phi_obs_before_observer_facing_SM_claim"
  },
  "phi_obs_contract": {
    "required_fields": [
      "observer_algebra_or_gauge_object",
      "chiral_fermion_representation_list",
      "generation_decomposition",
      "real_structure_and_grading_signs",
      "dirac_and_first_order_control",
      "higgs_scalar_and_action_status",
      "anomaly_freed_hopkins_input",
      "substrate_mode_policy",
      "target_data_provenance",
      "replacement_tests",
      "rollback_conditions"
    ],
    "allowed_modes": [
      "exact_finite_connes_channel",
      "replacement_shadow"
    ],
    "status_vocabulary": [
      "derived",
      "derived_relative",
      "hosted",
      "imported",
      "failed",
      "open"
    ]
  },
  "first_missing_objects": [
    "P0_choose_exact_finite_Connes_channel_or_declared_replacement_shadow",
    "FC_EPSILON_for_exact_channel_KO6_contact",
    "A_F_selector_without_forbidden_target_input",
    "REPLACEMENT_CODOMAIN_for_non_CC_shadow"
  ],
  "target_data_provenance_current": {
    "A_F": "missing_imported_in_current_host_lanes",
    "G_SM_Z6": "missing_failed_as_target_free_current_output",
    "K_SM_T1": "relative_branch_evidence_but_not_finite_module_selector",
    "T3_generations": "not_selected_by_current_Type_II1_classes",
    "Higgs": "hosted_quantum_numbers_physical_scalar_and_potential_open",
    "Anomaly_shadow": "conditional_on_actual_observer_mode_list",
    "Spectral_action": "not_recovered_from_current_substrate_data"
  },
  "forbidden_target_inputs": [
    "A_F",
    "finite_CC_tuple",
    "G_SM_Z6",
    "central_Z6",
    "K_SM",
    "n_equals_3",
    "C3",
    "index_3",
    "D4_arms",
    "three_projections",
    "dim_H_F_96",
    "ordinary_anomaly_free_SM_shadow",
    "physical_Higgs_data"
  ],
  "rollback_conditions": [
    "target_data_used_as_selector_input",
    "n2_or_n4_replacement_proof_still_works",
    "extra_observer_modes_without_anomaly_computation",
    "Higgs_slot_without_physical_projection_and_action",
    "FC_EPSILON_fails_for_exact_CC_contact",
    "finite_Connes_control_treated_as_primary_GU_substrate_axiom"
  ],
  "selector_claim_impacts": {
    "TYPEII1_HOST": "conditional_host_import_until_Phi_obs_computes_visible_data",
    "TYPEII1_SELECTOR": "negative_for_current_instantiated_classes_fixed_data_open_empty",
    "SM_GAUGE": "not_derived",
    "HIGGS": "hosted_quantum_numbers_physical_sector_open",
    "GENERATIONS": "not_selected_by_current_Type_II1_classes",
    "ANOMALY": "conditional_on_explicit_observer_shadow"
  },
  "next_actions": [
    "declare_exact_channel_or_replacement_mode",
    "compute_FC_EPSILON_if_exact_CC_route",
    "build_target_free_Phi_obs_selector_and_provenance_ledger",
    "specify_replacement_codomain_if_non_CC_route",
    "run_n2_n4_replacement_audit",
    "run_anomaly_shadow_audit_on_actual_visible_modes"
  ]
}
```
