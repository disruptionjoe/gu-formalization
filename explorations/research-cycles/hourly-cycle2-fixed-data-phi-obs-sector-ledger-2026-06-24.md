---
title: "Cycle 2 Fixed-Data Phi_obs Sector Ledger"
date: "2026-06-24"
status: exploration
doc_type: fixed_data_phi_obs_sector_ledger
verdict: "NO_CURRENT_FIXED_DATA_PHI_OBS_SELECTOR"
owner: "Cycle 2 Worker"
depends_on:
  - "RESEARCH-POSTURE.md"
  - "process/runbooks/five-lane-frontier-run.md"
  - "explorations/hourly-cycle1-observer-shadow-phi-obs-contract-2026-06-24.md"
  - "explorations/type-ii1-selector-or-nogo-theorem-2026-06-24.md"
  - "explorations/type-ii1-selector-anti-smuggling-theorem-2026-06-24.md"
  - "explorations/type-ii1-selector-candidate-2026-06-24.md"
  - "explorations/cycle3-connes-control-load-bearing-audit-2026-06-24.md"
  - "canon/type-ii1-spectral-sm-checklist.md"
---

# Cycle 2 Fixed-Data Phi_obs Sector Ledger

## 1. Verdict

**Verdict: NO_CURRENT_FIXED_DATA_PHI_OBS_SELECTOR.**

The current repo has no fixed-data `Phi_obs` selector that computes any of the
four finite-control targets

```text
T_A = A_F = C + H + M_3(C)
T_G = SU(3) x SU(2) x U(1) / Z_6
T_1 = one SM generation module with the 16 Weyl fermions and hypercharges
T_3 = exactly three equivalent generation sectors
```

from target-free Type II_1 data.

The C3/D4 construction and the surrounding Type II_1 candidates establish a
useful negative control: after an order-3, index-3, or three-arm object is
chosen, they provide a clean threefold sector label set with equal trace or
Markov weight. They do not select the finite Connes algebra, the SM gauge
quotient, the one-generation SM module, or three physical generations. The same
sector-readout proof works after the nearest `n = 2` and `n = 4` replacements.

Current target-status ledger:

| target | current status | decision reason | promotion proof object |
|---|---|---|---|
| `T_A` | `not_selected_imported_in_hosts` | Every current finite-control host begins after `A_F` or its finite tuple is supplied. C3/D4 sector data has no algebra-selection mechanism. | Target-free `Phi_obs(X) = A_F` or replacement observer algebra, with no `A_F`, summand list, or finite CC tuple in the input. |
| `T_G` | `not_selected` | Inner-fluctuation/gauge recovery needs the observer algebra first; C3/D4 and trace projections output sector labels, not a compact SM gauge quotient. | Gauge selector deriving the Lie algebra and global `Z_6` quotient from fixed data. |
| `T_1` | `not_selected_imported_if_used` | The one-generation finite module, hypercharge lattice, and representation packet are external to current Type II_1 sector data. | `Phi_obs` image theorem producing the chiral module and hypercharges without attaching `K_SM`. |
| `T_3` | `failed_for_current_instantiated_candidates_open_empty_for_fixed_data` | C3/D4, `C_n`, equal projections, and external `K_SM tensor C^n` transport a chosen count; no fixed-data theorem forces three. | Fixed-data standard-invariant, index, or Connes-channel rigidity theorem with named obstruction for `n = 2,4`. |

Thus the live decision is:

```text
C3/D4: no-go as an explanatory selector.
All current instantiated Type II_1 candidates: host-only or no-go as selectors.
Fixed-data rigidity selector: open only as an uninstantiated theorem target.
Phi_obs: contract-only until its target-free image is constructed.
```

## 2. Fixed-data selector ledger fields

A real fixed-data sector selector must start from

```text
X = (N subset M, tau, A, H, D, J, gamma, Phi_obs)
```

where `X` is fixed by independent Type II_1 spectral-SM requirements, not by
choosing the desired finite-control output.

Allowed fixed-data sources include finite-index subfactor data, a faithful normal
trace, a semifinite spectral triple, real-even signs, order-zero/order-one
conditions, tau-compactness, bounded or twisted commutators, Breuer-Fredholm or
cyclic-cohomology constraints, standard-invariant rigidity, and a declared
observer map.

Forbidden selector inputs include:

```text
A_F, finite_CC_tuple, G_SM, central_Z6, K_SM, n_equals_3, C3, index_3,
D4_arms, three_projections, dim_H_F_96, ordinary_anomaly_free_SM_shadow,
physical_Higgs_data
```

Required ledger fields:

| field | what must be supplied | current C3/D4 or repo status |
|---|---|---|
| `X_fixedness_certificate` | Proof that `(N subset M, tau, A, H, D, J, gamma, Phi_obs)` is independently forced or selected before target readout. | Missing. C3/D4 starts with an order-3/index-3/three-arm feature. |
| `sector_idempotents` | Canonical idempotents or sector objects from the standard invariant/Jones tower, not a chosen projection partition. | C3 Fourier projections or D4 arms exist only after the visible threefold object is chosen. |
| `Markov_traces` | Trace or Markov-weight computation for all sector idempotents. | Equal weights are available for C3/D4, but the same computation gives `1/n` weights for `C_n`. |
| `fusion_equivalence` | Equivalence as standard-invariant sectors or Connes correspondences, not only Murray-von Neumann equivalence by equal trace. | Not established at physical strength. Equal trace in a factor is too cheap. |
| `spectral_compatibility` | Sectorwise compatibility with `J`, `gamma`, `D`, order-zero, order-one, tau-compactness, and bounded or twisted commutators. | Not computed from C3/D4 alone. The checks pass only after importing or tensoring spectral data. |
| `Connes_channel_image` | `Phi_obs(q_i)` and `Phi_obs(X)` computed without supplying `A_F`, `G_SM`, `K_SM`, or the generation count. | Missing. Current images attach `K_SM` and finite CC data externally. |
| `anomaly_shadow` | Actual observer-facing mode list after `Phi_obs`, with perturbative/global/Freed-Hopkins status for that list. | Conditional only for externally attached ordinary SM copies; no new Type II_1 shadow has been checked. |
| `replacement_n2_n4_tests` | Nearest `X_2`, `X_4`, and preferably `X_n` replacements, with the first obstruction for every `n != 3`. | Fails for C3/D4: `C_2` and `C_4` replacements work with the same proof. |
| `target_statuses` | Row-by-row status for `T_A`, `T_G`, `T_1`, and `T_3`: selected, relative, hosted, imported, failed, or open. | All current rows are non-selected; `T_3` is failed for instantiated candidates and open-empty for fixed data. |

Decision rule:

```text
No row may be promoted from hosted/imported/failed/open to selected unless the
corresponding proof object is target-free and the n = 2,4 replacements fail by a
named spectral, index, standard-invariant, anomaly, or Connes-channel obstruction.
```

## 3. What current Type II1 candidates establish

| candidate class | strongest established object | `T_A` | `T_G` | `T_1` | `T_3` | selector verdict |
|---|---|---|---|---|---|---|
| Imported finite CC host | Semifinite or hyperfinite host of supplied finite CC data. | imported | imported through `A_F` | imported through `H_F`/`K_SM` | imported as copied finite Hilbert space | `HOST_ONLY` |
| Equal-trace projection split | `p_1,...,p_n` with equal `tau` in a diffuse II_1 factor. | no | no | no | no; any `n` works | `NO_GO_TRACE_EQUIVALENCE` |
| `C_n` crossed-product sectors | Fourier idempotents in `R crossed_product C_n`. | no | no | no | no; returns chosen `n` | `NO_GO_CARDINALITY_TRANSPORT` |
| C3/D4 visible-three toy | Three equal Markov-weight arms or projections after choosing C3/index 3/D4. | no | no | no | no; replacement works | `NO_GO_FOR_C3D4` |
| KO-6/order-one finite-control filter | Real-even sign and first-order requirements. | no; algebra still needed | no; group still needs algebra | necessary filter only | no | `NECESSARY_NOT_SUFFICIENT` |
| Breuer-Fredholm/index filter | Possible trace-index or cyclic-cohomology lattice target. | no instance | no instance | no instance | open only if a theorem forces a three-sector split | `OPEN_FILTER_NO_INSTANCE` |
| Fixed-data standard-invariant selector | Hypothetical `X` not parameterized by target count or CC data. | no instance | no instance | no instance | open-empty | `OPEN_EMPTY` |
| Non-embeddable selector | Speculative new invariant unavailable in hyperfinite toys. | no instance | no instance | no instance | no instance | `SPECULATIVE_NO_INSTANCE` |

This is a selector ledger, not a host ledger. Hosting finite Connes data inside a
Type II_1 ambient algebra can be mathematically useful, but it does not explain
a finite-control target unless the target appears as the image of `Phi_obs`
rather than as an argument to the construction.

## 4. Strongest positive ledger construction attempt

The strongest current attempt remains the C3/D4 negative control, written in
ledger form.

Candidate:

```text
X_C3 = (R subset R crossed_product C3, tau, A, H, D, J, gamma, Phi_obs)
```

where `R` is a II_1 factor and the spectral data are either unspecified or
externally tensor-attached.

Sector readout:

```text
e_k = (1/3) * sum_{g=0}^{2} omega^(-kg) u_g,  k = 0,1,2
sum_k e_k = 1
tau(e_k) = 1/3
e_i e_j = 0 for i != j
```

The D4 arm version supplies analogous equal Markov-weight sector labels in the
standard-invariant/Jones-tower reading.

Best-case ledger:

| ledger field | best positive result | failure point |
|---|---|---|
| sector idempotents | Three idempotents/arms can be named after the C3/D4 object is chosen. | The count is visible in the input object. |
| Markov traces | Equal weights are available. | Equal weights persist for `C_n` and for arbitrary equal-trace projection splits. |
| fusion/equivalence | There is symmetry among character labels or arms; ambient projections of equal trace are Murray-von Neumann equivalent. | This is not equivalence of SM representation content or a Connes-correspondence theorem. |
| spectral compatibility | One can tensor the same spectral data onto every sector. | The spectral data are imported; the test does not distinguish `n = 3` from `n = 2,4`. |
| Connes-channel image | A map can be written after attaching `A_F` and `K_SM`: `e_k |-> K_SM`. | This imports `T_A` and `T_1`, and makes `T_3` a copied-label count. |
| anomaly shadow | `n` externally attached ordinary SM generations are anomaly-safe copywise. | Copywise anomaly cancellation holds for arbitrary `n`; it does not select three. |
| replacements | `C_2` and `C_4` analogs exist and produce equal Fourier idempotents. | No first obstruction appears for `n = 2` or `n = 4`. |

The strongest honest positive statement is therefore:

```text
C3/D4 gives a clean sector-label laboratory and a reusable negative control.
It does not select T_A, T_G, T_1, or T_3 without target inputs.
```

## 5. First exact obstruction or missing proof object

For current C3/D4 data, the first exact obstruction is:

```text
PHI_OBS_IMAGE_WITHOUT_TARGET_INPUT:
  define Phi_obs(e_k) and Phi_obs(X_C3)
  without A_F, K_SM, G_SM, finite_CC_tuple, or n = 3 as inputs.
```

This object is absent. If `A_F` and `K_SM` are attached externally, the first
remaining obstruction for a relative generation-count claim is:

```text
N_NEQ_3_REPLACEMENT_OBSTRUCTION:
  prove why the same ledger fails for X_2 and X_4.
```

This obstruction is also absent. The nearest replacements are explicit:

```text
X_2 = (R subset R crossed_product C2, tau, ...)
X_4 = (R subset R crossed_product C4, tau, ...)
```

and both provide equal Fourier idempotents, equal trace weights, external
`K_SM tensor C^n` images if `K_SM` is attached, and copywise anomaly safety for
ordinary SM packets. Therefore the attempted proof reads off the input
cardinality rather than deriving `T_3`.

For the fixed-data class, the first missing object is even earlier:

```text
FIXED_DATA_X_CERTIFICATE:
  a named X = (N subset M, tau, A, H, D, J, gamma, Phi_obs)
  fixed by independent Type II_1 spectral-SM constraints and not by target data.
```

No current file supplies such an `X`.

## 6. Impact for Phi_obs and Type II1 selector claims

`Phi_obs` remains a contract gate. The exact finite Connes-channel route is not
constructed, and no replacement observer shadow with equal controls has been
declared.

Impact ledger:

| claim | current status | allowed statement |
|---|---|---|
| `PHI_OBS` | `contract_only_underdefined` | A future observer-facing SM claim must provide exact finite channel data or a declared replacement shadow. |
| `TYPEII1-HOST` | `conditional_host` | Type II_1 can host imported finite-control data under the stated spectral checks. |
| `TYPEII1-SELECTOR` | `negative_filter_current_classes` | Current instantiated selector classes do not compute `T_A`, `T_G`, `T_1`, or `T_3`. |
| C3/D4 | `toy_failure_negative_control` | It is a good ledger test case, not an explanatory generation selector. |
| Fixed-data rigidity | `open_empty` | A positive theorem is still conceivable but has no repo instance. |
| SM gauge/Higgs/anomaly claims | `not_promoted` | Gauge, Higgs, and anomaly claims remain branch/host/conditional until the actual observer shadow is computed. |

This does not demote the whole Type II_1 program. It demotes selector language
for current data and makes the next proof obligation concrete.

## 7. Rollback/falsification conditions

Roll back any future fixed-data selector claim to `host`, `import`, or `failed`
if any of these conditions fire:

1. The selector input contains `A_F`, `finite_CC_tuple`, `G_SM`, `Z_6`, `K_SM`,
   `n = 3`, `C3`, index 3, D4 arms, three projections, `dim H_F = 96`, ordinary
   anomaly-free SM content, or physical Higgs data.
2. The sector equivalence proof uses only equal trace, equal Markov weight, or
   ambient Murray-von Neumann equivalence.
3. `Phi_obs(q_i)` is defined by externally attaching `K_SM`, `A_F`, or ordinary
   SM finite spectral data.
4. The proof remains valid after `n = 2` or `n = 4` replacement, with only
   `C^3` changed to `C^n`.
5. Spectral compatibility with `J`, `gamma`, `D`, order-zero, order-one,
   tau-compactness, and bounded or twisted commutators is not checked on the
   actual sector decomposition.
6. Extra observer-facing Type II_1 or GU modes survive without a complete anomaly
   computation.
7. Non-embeddability is cited but the selector image is reproducible in the
   hyperfinite `C_n` family or has no observer-facing effect.
8. The finite Connes control case is treated as a primary GU substrate axiom
   rather than as an observer-facing certificate or comparator.

Positive falsification of this negative ledger would require a named `X`, a
target-free `Phi_obs`, selected target rows, and a first obstruction for the
nearest `n = 2,4` replacements.

## 8. Next meaningful computation

The next computation should not be another visible triple. The meaningful work
is a fixed-data sector ledger for a named candidate that survives the input
filters.

Minimum next packet:

1. Build a candidate inventory with columns: candidate `X`, source of fixedness,
   target claimed, where `3` enters, imported CC data, nearest replacement, and
   preliminary verdict.
2. Reject immediately any candidate whose fixedness starts from `C3`, index 3,
   D4 arms, three chosen projections, `K_SM tensor C^3`, or `dim H_F = 96`.
3. For the best surviving non-C3 candidate, compute sector idempotents, Markov
   traces, fusion/equivalence classes, standard-invariant automorphism orbit,
   Breuer-Fredholm or cyclic-cohomology values, and spectral compatibility.
4. Define `Phi_obs` on the actual sectors, listing selected and imported data.
5. Run `X_2`, `X_4`, and available `X_n` replacements and name the first failure
   for every `n != 3`.
6. Only then update `TYPEII1-SELECTOR`; otherwise leave it as a negative filter
   and keep `TYPEII1-HOST` as the conditional positive lane.

If no candidate survives the fixedness inventory, the correct next status is:

```text
NO_CANDIDATE_SURVIVES_FIXEDNESS_FILTER
```

not another C3/D4-style search.

## 9. Machine-readable JSON summary

```json
{
  "artifact": "hourly_cycle2_fixed_data_phi_obs_sector_ledger",
  "date": "2026-06-24",
  "verdict": "NO_CURRENT_FIXED_DATA_PHI_OBS_SELECTOR",
  "explicit_verdict": "C3_D4_and_current_instantiated_Type_II1_candidates_do_not_select_T_A_T_G_T_1_or_T_3_without_target_inputs; fixed_data_rigidity_remains_open_empty",
  "no_sm_generation_selector_promotion": true,
  "fixed_data_X_fields": [
    "N_subset_M",
    "tau",
    "A",
    "H",
    "D",
    "J",
    "gamma",
    "Phi_obs"
  ],
  "required_sector_ledger_fields": [
    "X_fixedness_certificate",
    "sector_idempotents",
    "Markov_traces",
    "fusion_equivalence",
    "spectral_compatibility",
    "Connes_channel_image",
    "anomaly_shadow",
    "replacement_n2_n4_tests",
    "target_statuses"
  ],
  "target_selection_status": {
    "T_A": {
      "status": "not_selected_imported_in_hosts",
      "reason": "current hosts supply A_F or the finite_CC_tuple as input",
      "required_promotion_object": "target_free_Phi_obs_X_to_A_F_or_declared_replacement_observer_algebra"
    },
    "T_G": {
      "status": "not_selected",
      "reason": "no fixed_data gauge selector derives SU3_SU2_U1_mod_Z6",
      "required_promotion_object": "gauge_selector_deriving_local_Lie_algebra_and_global_Z6_quotient"
    },
    "T_1": {
      "status": "not_selected_imported_if_used",
      "reason": "K_SM_one_generation_module_and_hypercharge_lattice_are_external_to_current_sector_data",
      "required_promotion_object": "Phi_obs_image_theorem_for_chiral_module_and_hypercharges_without_K_SM_input"
    },
    "T_3": {
      "status": "failed_for_current_instantiated_candidates_open_empty_for_fixed_data",
      "reason": "C3_D4_Cn_trace_and_external_attachment_routes_transport_a_chosen_count",
      "required_promotion_object": "fixed_data_three_sector_rigidity_with_n2_n4_obstruction"
    }
  },
  "current_candidates": {
    "imported_finite_CC_host": "HOST_ONLY",
    "equal_trace_projection_split": "NO_GO_TRACE_EQUIVALENCE",
    "C_n_crossed_product": "NO_GO_CARDINALITY_TRANSPORT",
    "C3_D4_visible_three": "NO_GO_FOR_C3D4",
    "KO6_order_one_filter": "NECESSARY_NOT_SUFFICIENT",
    "Breuer_Fredholm_index_filter": "OPEN_FILTER_NO_INSTANCE",
    "fixed_data_standard_invariant": "OPEN_EMPTY",
    "non_embeddable_selector": "SPECULATIVE_NO_INSTANCE"
  },
  "strongest_attempt": {
    "candidate": "C3_D4_negative_control",
    "sector_idempotents": "three_idempotents_or_arms_after_visible_threefold_object_is_chosen",
    "Markov_traces": "equal_weights_available_but_parametric_in_n",
    "fusion_equivalence": "not_physical_Connes_correspondence_or_SM_representation_equivalence",
    "spectral_compatibility": "only_after_importing_or_tensoring_spectral_data",
    "Connes_channel_image": "external_attachment_of_A_F_and_K_SM",
    "anomaly_shadow": "copywise_only_for_imported_ordinary_SM_packets",
    "verdict": "negative_control_not_selector"
  },
  "replacement_tests": {
    "n_equals_2": {
      "candidate": "C2_crossed_product_or_two_arm_replacement",
      "result": "same_proof_works_no_obstruction",
      "selector_effect": "fails_T3_selection"
    },
    "n_equals_4": {
      "candidate": "C4_crossed_product_or_four_arm_replacement",
      "result": "same_proof_works_no_obstruction",
      "selector_effect": "fails_T3_selection"
    },
    "n_arbitrary": {
      "candidate": "C_n_or_equal_trace_n_partition",
      "result": "same_cardinality_readout_family",
      "selector_effect": "count_transport"
    }
  },
  "forbidden_target_inputs": [
    "A_F",
    "finite_CC_tuple",
    "G_SM",
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
  "first_missing_proof_objects": [
    "FIXED_DATA_X_CERTIFICATE",
    "PHI_OBS_IMAGE_WITHOUT_TARGET_INPUT",
    "N_NEQ_3_REPLACEMENT_OBSTRUCTION",
    "SECTORWISE_SPECTRAL_COMPATIBILITY_PROOF",
    "ACTUAL_OBSERVER_MODE_ANOMALY_SHADOW"
  ],
  "rollback_conditions": [
    "target_data_used_as_selector_input",
    "trace_or_Murray_von_Neumann_equivalence_only",
    "external_K_SM_or_A_F_attachment",
    "n2_or_n4_replacement_proof_still_works",
    "sectorwise_spectral_compatibility_not_checked",
    "extra_visible_modes_without_anomaly_computation",
    "decorative_non_embeddability_only",
    "finite_Connes_control_treated_as_primary_GU_substrate_axiom"
  ],
  "claim_impacts": {
    "PHI_OBS": "contract_only_underdefined",
    "TYPEII1_HOST": "conditional_host",
    "TYPEII1_SELECTOR": "negative_filter_current_classes",
    "C3_D4": "toy_failure_negative_control",
    "fixed_data_rigidity": "open_empty",
    "SM_gauge_Higgs_anomaly": "not_promoted"
  },
  "next_computation": [
    "candidate_inventory_with_fixedness_filter",
    "reject_visible_three_and_imported_CC_inputs",
    "sector_idempotent_Markov_trace_fusion_equivalence_ledger_for_best_survivor",
    "define_target_free_Phi_obs_on_actual_sectors",
    "run_X2_X4_Xn_replacement_tests",
    "update_TYPEII1_SELECTOR_only_after_selected_target_and_replacement_obstruction"
  ]
}
```
