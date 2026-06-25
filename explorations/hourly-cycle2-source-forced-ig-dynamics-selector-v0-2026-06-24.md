---
title: "Hourly Cycle 2 SourceForcedIGDynamicsSelector V0 Gate"
date: "2026-06-24"
status: exploration/gate
doc_type: hourly_cycle2_source_forced_ig_dynamics_selector_v0
verdict: "UNDERDEFINED_NO_SOURCE_FORCED_IG_DYNAMICS_SELECTOR_EMITTED"
owned_path: "explorations/hourly-cycle2-source-forced-ig-dynamics-selector-v0-2026-06-24.md"
optional_audit: "tests/hourly_cycle2_source_forced_ig_dynamics_selector_v0_audit.py"
depends_on:
  - "RESEARCH-POSTURE.md"
  - "process/runbooks/five-lane-frontier-run.md"
  - "explorations/hourly-cycle1-source-forced-theta-coefficient-packet-2026-06-24.md"
  - "explorations/cycle2-source-forced-s-ig-dyn-action-gate-2026-06-24.md"
  - "explorations/gu-minimal-action-spec-2026-06-24.md"
  - "explorations/gu-closed-loop-action-ig-branch-2026-06-24.md"
  - "explorations/ig-dynamics-nonzero-theta-action-gate-2026-06-24.md"
  - "explorations/gu-typed-operator-action-spine-2026-06-24.md"
---

# Hourly Cycle 2 SourceForcedIGDynamicsSelector V0 Gate

## 1. Verdict

Verdict:

```text
UNDERDEFINED.
```

More precisely:

```text
SourceForcedIGDynamicsSelector_V0 emitted by current repo sources: NO
legitimate Branch 3 action template exists: YES
source-forced selection of that template: NO
target comparison permission: NO
first exact missing source datum: source selection rule for K_IG and field degrees
```

The current repo sources are strong enough to write a lawful Branch 3 dynamical-IG
template. They are not strong enough to say that GU source geometry selects that template
before target comparison.

The selector gate therefore blocks before any theta/FLRW coefficient packet. In particular,
this file makes no positive derivation claim for dark energy, Lambda, `Z_theta`,
`C_Rtheta`, or `xi_eff`.

Current selector field status:

| selector field | current repo status | decision |
|---|---|---|
| `K_IG` | candidate `D_A U` is natural and gauge-covariant, but not source-selected or unique | not selected |
| `Q_IG` | Ad-invariant pairings are available as typed ingredients, but no source normalization is fixed for the IG kinetic sector | not selected |
| `Z_U` | appears as a template coefficient only | not selected |
| `V_src` | open slot for source potential | not selected |
| `S_cross_src` | open slot for source cross terms | not selected |
| `field_degrees` | candidate `U in Omega^1(Y,ad P)` and `P_IG in Omega^2(Y,ad P)` are available for `K_IG=D_A U`, but not source-forced | not selected |
| `boundary_data` | required by the variational problem, but only named as an obligation | not selected |

This is a constructive obstruction, not a no-go theorem against all dynamical IG actions.
It says only that the current source files do not yet contain the exact selector datum
needed to distinguish "this action is a legitimate model" from "this action is forced by
GU source geometry."

## 2. Candidate selector input/output signature

The attempted selector has this typed shape:

```text
SourceForcedIGDynamicsSelector_V0:
  SourceData_GU
    -> SourceForcedIGDynamicsPacket
```

where the minimal input side is:

```text
SourceData_GU =
  carrier:
    X, Y = Met_Lor(X), g_Y, G = Sp(64), P -> Y
  action spine:
    s: X -> Y, A, epsilon, beta, U = Ad(epsilon^-1) beta,
    theta = A - Gamma(epsilon) - U,
    baseline S_YM + S_theta + S_W + S_DD slots
  source rules:
    local Sp(64) gauge covariance,
    admissible IG variation status,
    source geometry / tau-plus / typed operator constraints,
    allowed invariant pairings,
    allowed field degrees,
    variational boundary class
  quarantine:
    target_inputs_seen = []
```

The required output side is:

```text
SourceForcedIGDynamicsPacket =
  selector_status,
  field_degrees,
  K_IG,
  Q_IG,
  Z_U,
  V_src,
  S_cross_src,
  boundary_data,
  source_forced_action_or_parent_action,
  derived_current_terms,
  conservation_contract,
  target_quarantine_log,
  decision.
```

For Branch 3, the natural parent-action output would be:

```text
S_IG_dyn^parent[A,epsilon,U,P_IG;s]
  =
    int_Y <P_IG, K_IG(U;A,epsilon,s)>_{Q_IG}
  - 1/(2 Z_U) int_Y <P_IG, P_IG>_{Q_IG}
  - int_Y V_src(U, epsilon, s)
  - c_theta/2 int_Y <theta, theta>
  + S_cross_src[A,epsilon,U,P_IG,s]
  + S_boundary[boundary_data].
```

If the selector chose:

```text
K_IG(U;A,epsilon,s) = D_A U,
```

then the corresponding parent field degree would be:

```text
U in Omega^1(Y,ad P),
P_IG in Omega^2(Y,ad P).
```

That is the strongest candidate tried here. It remains candidate-level because the current
sources do not prove that this is the source-selected operator rather than a well-formed
choice.

## 3. What current sources actually fix

The required sources fix the following before targets.

| item | fixed by current sources? | status |
|---|---:|---|
| `Y = Met_Lor(X)` | yes | carrier fixed at proposal/reconstruction level |
| `g_Y` | yes in baseline | fixed gimmel carrier, unless a future primary source varies it |
| `G = Sp(64)` and `P -> Y` | yes | typed gauge carrier |
| `A` | yes | dynamical connection |
| `epsilon,beta,U` | partly | objects named; variation status remains branch-dependent |
| `theta = A - Gamma(epsilon) - U` | yes | derived distortion/source object |
| free-beta obstruction | yes | free `beta` with only `|theta|^2` kills nonzero theta |
| Branch 3 action template | yes | legitimate total-current template can be written |
| Branch 3 source law if template is chosen | yes, conditionally | `D_A^* F_A = theta_eff`, not bare theta |
| target-fitting exclusions | yes | bare Lambda, bare `R theta^2`, DESI/Rubin-window fitting are excluded |
| `S_IG` / `S_IG_dyn` source-forced existence | no | explicit open slot |
| theta/FLRW coefficients | no | no `Z_theta`, `C_Rtheta`, or `xi_eff` emitted |

What is fixed is therefore a typed action spine and a legal model class. What is not fixed
is the source-side selector from GU geometry to one member of that class.

The strongest current Branch 3 statement is:

```text
If a source-forced Branch 3 action selects K_IG, Q_IG, Z_U, V_src, S_cross_src,
field degrees, and boundary data, then its A-variation must be treated as a total-current
equation D_A^*F_A = theta_eff.
```

The current sources do not establish:

```text
GU source geometry selects K_IG = D_A U.
GU source geometry selects Q_IG.
GU source geometry selects Z_U.
GU source geometry selects V_src.
GU source geometry selects S_cross_src.
GU source geometry selects field degrees and boundary data.
```

## 4. Strongest positive selector construction attempt

The strongest possible `SourceForcedIGDynamicsSelector_V0` attempt is the following.

Step 1: Choose the only currently well-typed Branch 3 variable package:

```text
U = Ad(epsilon^-1) beta in Omega^1(Y,ad P),
theta = A - Gamma(epsilon) - U.
```

Step 2: Demand local gauge covariance, locality, first-order dynamics, and no target inputs.
This makes the candidate operator:

```text
K_IG(U) = D_A U.
```

Step 3: Pair it with the canonical parent degree:

```text
P_IG in Omega^2(Y,ad P),
int_Y <P_IG, D_A U>.
```

Step 4: Use an Ad-invariant `Q_IG` induced from the `Sp(64)` pairing and `g_Y` Hodge data,
carry a positive kinetic normalization `Z_U`, and leave only source-forced invariant
potential/cross terms:

```text
V_src(U,epsilon,s),
S_cross_src[A,epsilon,U,P_IG,s].
```

Step 5: Require boundary data that make the variation and Noether identity well-defined:

```text
either fixed fields on the boundary,
or fixed conjugate fluxes,
or a named mixed/APS/asymptotic variational class.
```

Step 6: Derive the connection current. If the candidate is accepted, the current has the
schematic parent form:

```text
J_IG = ad_U^dagger(P_IG)
```

and the connection equation becomes:

```text
D_A^* F_A = theta_eff
```

with `theta_eff` equal to the theta term plus all IG, cross, spinor, and section currents
in the chosen normalization.

This attempt is mathematically coherent. It is not source-forced. The move from
"local first-order gauge-covariant operator" to "`K_IG = D_A U` is the GU-selected
operator" is an added selection principle. The read sources do not supply that principle
or a uniqueness theorem ruling out competing local, projected, constrained, section-coupled,
or higher-order IG operators.

Therefore the strongest positive output is a selector contract:

```text
SourceForcedIGDynamicsSelector_V0 is now precisely specified as a missing source map.
```

It is not an emitted selector.

## 5. First exact obstruction or missing source datum

The first exact missing source datum is:

```text
a source-side rule selecting the IG dynamical operator K_IG and field degrees.
```

Equivalently:

```text
K_IG_selector:
  GU source geometry / tau-plus / typed action spine
    -> K_IG(U;A,epsilon,s) and the degree of U and P_IG.
```

The current sources name `U` and permit the candidate `D_A U`, but they do not provide a
source datum saying:

```text
U must be a 1-form dynamical IG field,
P_IG must be a 2-form parent momentum,
and the selected first-order operator must be D_A U.
```

This is first because the downstream selector fields depend on it:

| downstream datum | why it depends on the first missing datum |
|---|---|
| `Q_IG` | pairing and Hodge degree depend on the selected operator and field degree |
| `Z_U` | normalization is meaningful only after the kinetic term is fixed |
| `V_src` | source potential is constrained by the selected field representation |
| `S_cross_src` | admissible cross terms depend on the selected field content and order |
| `boundary_data` | boundary class depends on the differential order and parent variables |
| `J_IG` | current is the A-variation of the selected kinetic/cross terms |
| `theta_eff` | total source depends on all selected current terms |
| FLRW projection | scalar mode and coefficient packet depend on the locked action |

Ordered obstruction chain:

| order | missing object or datum | current status |
|---:|---|---|
| 1 | `K_IG_selector` and source-forced field degrees | absent |
| 2 | `Q_IG` selected in the same normalization | absent |
| 3 | `Z_U` selected before targets | absent |
| 4 | `V_src` selected or proved absent | absent |
| 5 | `S_cross_src` selected or proved absent | absent |
| 6 | `boundary_data` for the variational problem | absent |
| 7 | full `S_IG_dyn` or first-order parent action | template only |
| 8 | exact `J_IG` and complete `theta_eff` | schematic only |
| 9 | total-current Noether or projected conservation proof | theorem contract only |
| 10 | FLRW scalar-mode survival and quadratic coefficient packet | not emitted |

If a future source says that the correct branch is constrained Branch 2A rather than
dynamical Branch 3, this selector attempt should be demoted as the wrong branch rather
than patched into a source-forced result.

## 6. Impact for Branch 3 and theta coefficient packet

Branch 3 remains the strongest honest host for a future theta/FLRW coefficient packet
because it can make nonzero IG data differential and can replace the bare theta source by
a conserved total current. The current gate does not upgrade Branch 3 to a prediction.

Allowed current statement:

```text
Branch 3 has a coherent total-current action template, but current sources do not select
K_IG, Q_IG, Z_U, V_src, S_cross_src, field degrees, or boundary data before target
comparison.
```

Forbidden current statements:

```text
Do not state that Branch 3 has derived Lambda.
Do not state that Branch 3 has derived dark energy.
Do not state that Branch 3 has derived Z_theta.
Do not state that Branch 3 has derived C_Rtheta.
Do not state that Branch 3 has derived xi_eff.
The candidate K_IG = D_A U is source-forced merely because it is natural.
The theta/FLRW coefficient packet may be compared to DESI/Rubin before source lock.
```

To emit a later theta/FLRW coefficient packet, the repo would need:

1. `SourceForcedIGDynamicsSelector`: source-selects `K_IG`, `Q_IG`, `Z_U`, `V_src`,
   `S_cross_src`, field degrees, and boundary data.
2. Written `S_IG_dyn` or parent action in that exact selection.
3. Full EL tuple, including `E_A`, `E_U`, `E_P`, `E_epsilon`, `E_s`, and `E_Psi` as
   applicable.
4. Exact `J_IG` and complete `theta_eff`.
5. Gauge Noether or projected conservation proof for `D_A^* theta_eff = 0`.
6. FLRW scalar-mode survival certificate for the same branch.
7. Quadratic FLRW reduction of the same locked action.
8. Emitted coefficients:

```text
Z_theta,
C_Rtheta,
xi_eff = C_Rtheta / Z_theta.
```

9. Target quarantine log proving:

```text
target_inputs_seen = []
```

before coefficient emission.

Only after those objects exist may a later file compare `xi_eff` with any dark-energy,
DESI/Rubin, or `w_0,w_a` target window.

## 7. Rollback/falsification conditions

Rollback conditions for this selector gate:

```text
K_IG_chosen_by_simplicity_not_source
K_IG_not_unique_under_allowed_source_rules
field_degrees_not_source_selected
Q_IG_not_selected
Z_U_target_fitted
V_src_target_fitted
S_cross_src_chosen_after_residual_or_target
boundary_data_chosen_after_target
S_IG_dyn_template_promoted_without_selector
J_IG_not_derived_from_delta_A
theta_eff_missing_total_current_terms
Noether_identity_not_written
total_current_conservation_not_proved
bare_theta_source_retained_in_Branch_3
bare_Lambda_inserted
bare_Rtheta_inserted
Z_theta_or_C_Rtheta_claimed_without_FLRW_reduction
xi_eff_fitted_not_generated
dark_energy_derivation_claimed_before_selector_closes
DESI_Rubin_window_used_upstream
xi_eff_threshold_used_upstream
xi_eff_target_value_used_upstream
replacement_or_withheld_target_check_changes_selector
```

Falsification or demotion conditions:

```text
F1. A primary GU source fixes a different IG action branch, such as constrained Branch 2A.
F2. The actual GU operator has no dynamical IG kinetic slot.
F3. Free beta with only |theta|^2 is the actual source action, killing nonzero theta.
F4. The only way to select K_IG, V_src, S_cross_src, or boundary data uses target windows.
F5. The selected Branch 3 action fails to produce a conserved total current.
F6. The locked FLRW reduction has no scalar theta mode.
F7. The locked FLRW reduction emits no `C_Rtheta`, or emits `Z_theta <= 0` without a
    gauge-removal explanation.
```

These are not pessimistic add-ons. They are the checks that keep a constructive Branch 3
search from becoming target-fitting.

## 8. Next meaningful proof/computation step

The next meaningful step is not another cosmology comparison. It is a source-side selector
test:

```text
K_IGSourceSelectionTest_V0.
```

Minimum task:

1. List all local gauge-covariant IG operators compatible with the typed spine and the
   declared variation status up to the same differential order as `D_A U`.
2. Decide whether GU source geometry, tau-plus geometry, or the typed action/operator spine
   uniquely selects one of them.
3. If the selected operator is `D_A U`, record the assumptions and derive the parent degree
   of `P_IG`.
4. If more than one operator survives, keep the selector underdefined and do not choose
   by target performance.
5. Only after `K_IG` and field degrees are fixed, select or refute `Q_IG`, `Z_U`, `V_src`,
   `S_cross_src`, and `boundary_data`.
6. Run the replacement-target check:

```text
replace DESI/Rubin, xi_eff, black-hole residual, and Lambda targets by dummy labels;
the selected packet must not change.
```

Pass condition:

```text
Source geometry selects a complete IG dynamics packet before targets:
K_IG, Q_IG, Z_U, V_src, S_cross_src, field degrees, boundary data.
```

Block condition:

```text
The source geometry supplies only a legal template class and no selector.
```

Only a pass should feed a later `SourceForcedThetaFLRWCoefficientPacket`.

## 9. Machine-readable JSON summary

```json
{
  "artifact": "HOURLY_CYCLE2_SOURCE_FORCED_IG_DYNAMICS_SELECTOR_V0",
  "version": "2026-06-24",
  "mission_posture": "Mission_A_constructive_obstruction",
  "verdict": "underdefined",
  "selector_name": "SourceForcedIGDynamicsSelector_V0",
  "selector_emitted_by_repo_sources": false,
  "legitimate_action_template_exists": true,
  "source_forced_selection_exists": false,
  "target_comparison_permitted": false,
  "target_inputs_seen_before_selector": [],
  "first_exact_missing_source_datum": {
    "id": "K_IG_selector",
    "description": "source-side rule selecting the IG dynamical operator K_IG and field degrees",
    "candidate": "K_IG(U)=D_A U",
    "candidate_status": "natural_gauge_covariant_template_not_source_selected",
    "blocks": [
      "Q_IG",
      "Z_U",
      "V_src",
      "S_cross_src",
      "boundary_data",
      "J_IG",
      "theta_eff",
      "FLRW_coefficient_packet"
    ]
  },
  "selector_signature": {
    "input": [
      "X",
      "Y=Met_Lor(X)",
      "g_Y",
      "G=Sp(64)",
      "P_to_Y",
      "s",
      "A",
      "epsilon",
      "beta",
      "U=Ad(epsilon^-1)beta",
      "theta=A-Gamma(epsilon)-U",
      "local_gauge_covariance",
      "admissible_IG_variation_status",
      "source_geometry_rules",
      "target_inputs_seen_empty"
    ],
    "output": [
      "selector_status",
      "field_degrees",
      "K_IG",
      "Q_IG",
      "Z_U",
      "V_src",
      "S_cross_src",
      "boundary_data",
      "source_forced_action_or_parent_action",
      "derived_current_terms",
      "conservation_contract",
      "target_quarantine_log",
      "decision"
    ]
  },
  "selector_fields": {
    "K_IG": {
      "required": true,
      "selected": false,
      "candidate": "D_A U",
      "status": "candidate_only_not_source_forced"
    },
    "Q_IG": {
      "required": true,
      "selected": false,
      "candidate": "Ad_invariant_pairing_plus_g_Y_Hodge_data",
      "status": "typed_pairing_available_but_no_source_normalization"
    },
    "Z_U": {
      "required": true,
      "selected": false,
      "candidate": "positive_kinetic_normalization",
      "status": "template_coefficient_only"
    },
    "V_src": {
      "required": true,
      "selected": false,
      "candidate": "source_invariant_potential",
      "status": "open_slot"
    },
    "S_cross_src": {
      "required": true,
      "selected": false,
      "candidate": "source_forced_cross_terms",
      "status": "open_slot"
    },
    "field_degrees": {
      "required": true,
      "selected": false,
      "candidate": "U_in_Omega1_adP_and_P_IG_in_Omega2_adP_if_K_IG_equals_D_A_U",
      "status": "candidate_only_depends_on_K_IG_selection"
    },
    "boundary_data": {
      "required": true,
      "selected": false,
      "candidate": "fixed_fields_or_fixed_fluxes_or_named_mixed_variational_class",
      "status": "required_obligation_not_selected"
    }
  },
  "current_sources_fix": [
    "carrier_Y_Met_Lor_X",
    "baseline_g_Y",
    "G_Sp64_and_P_to_Y",
    "A_as_dynamical_connection",
    "theta_definition",
    "free_beta_obstruction",
    "Branch_3_total_current_template_as_legitimate_template",
    "target_fitting_exclusions"
  ],
  "current_sources_do_not_fix": [
    "K_IG",
    "Q_IG",
    "Z_U",
    "V_src",
    "S_cross_src",
    "field_degrees",
    "boundary_data",
    "source_forced_S_IG_dyn",
    "Z_theta",
    "C_Rtheta",
    "xi_eff"
  ],
  "strongest_positive_construction": {
    "branch": "Branch_3_dynamical_IG_total_current",
    "candidate_K_IG": "D_A U",
    "candidate_parent_action": "int<P_IG,K_IG(U)>-1/(2Z_U)int<P_IG,P_IG>-int V_src-c_theta/2int<theta,theta>+S_cross_src+S_boundary",
    "candidate_current": "J_IG=ad_U_dagger(P_IG)",
    "candidate_source_law": "D_A^*F_A=theta_eff",
    "construction_status": "coherent_template_not_source_forced"
  },
  "target_quarantine": {
    "required": true,
    "target_inputs_seen": [],
    "known_targets_quarantined_until_after_selector_and_coefficients": [
      "Lambda",
      "dark_energy_equation_of_state",
      "DESI_Rubin_windows",
      "xi_eff_less_than_minus_0_319",
      "xi_eff_near_minus_0_6",
      "Schwarzschild_Kerr_residuals"
    ],
    "replacement_target_check_required": true,
    "rule": "selector_outputs_must_not_change_when_targets_are_replaced_by_dummy_labels"
  },
  "derived_claims": {
    "GU_derives_dark_energy": false,
    "GU_derives_Lambda": false,
    "GU_derives_Z_theta": false,
    "GU_derives_C_Rtheta": false,
    "GU_derives_xi_eff": false,
    "Branch_3_derives_dark_energy": false,
    "selector_derives_theta_FLRW_packet": false
  },
  "theta_flrw_packet_requirements_later": [
    "SourceForcedIGDynamicsSelector",
    "source_locked_S_IG_dyn_or_parent_action",
    "full_EL_tuple",
    "exact_J_IG",
    "complete_theta_eff",
    "Noether_or_projected_conservation_proof_for_theta_eff",
    "FLRW_scalar_mode_survival_certificate",
    "quadratic_FLRW_reduction",
    "Z_theta",
    "C_Rtheta",
    "xi_eff_equals_C_Rtheta_over_Z_theta",
    "target_inputs_seen_empty_before_coefficient_emission"
  ],
  "rollback_conditions": [
    "K_IG_chosen_by_simplicity_not_source",
    "K_IG_not_unique_under_allowed_source_rules",
    "field_degrees_not_source_selected",
    "Q_IG_not_selected",
    "Z_U_target_fitted",
    "V_src_target_fitted",
    "S_cross_src_chosen_after_residual_or_target",
    "boundary_data_chosen_after_target",
    "S_IG_dyn_template_promoted_without_selector",
    "J_IG_not_derived_from_delta_A",
    "theta_eff_missing_total_current_terms",
    "Noether_identity_not_written",
    "total_current_conservation_not_proved",
    "bare_theta_source_retained_in_Branch_3",
    "bare_Lambda_inserted",
    "bare_Rtheta_inserted",
    "Z_theta_or_C_Rtheta_claimed_without_FLRW_reduction",
    "xi_eff_fitted_not_generated",
    "dark_energy_derivation_claimed_before_selector_closes",
    "DESI_Rubin_window_used_upstream",
    "xi_eff_threshold_used_upstream",
    "xi_eff_target_value_used_upstream",
    "replacement_or_withheld_target_check_changes_selector"
  ],
  "next_meaningful_step": {
    "id": "K_IGSourceSelectionTest_V0",
    "do_next": true,
    "avoid_next": "cosmology_target_comparison_before_source_selector",
    "pass_condition": "source_geometry_selects_complete_IG_dynamics_packet_before_targets",
    "block_condition": "source_geometry_supplies_only_legal_template_class_and_no_selector",
    "required_outputs": [
      "operator_list",
      "selection_or_nonuniqueness_decision",
      "field_degree_decision",
      "Q_IG_decision",
      "Z_U_decision",
      "V_src_decision",
      "S_cross_src_decision",
      "boundary_data_decision",
      "replacement_target_check"
    ]
  }
}
```

## Sources read

- `RESEARCH-POSTURE.md`
- `process/runbooks/five-lane-frontier-run.md`
- `explorations/hourly-cycle1-source-forced-theta-coefficient-packet-2026-06-24.md`
- `explorations/cycle2-source-forced-s-ig-dyn-action-gate-2026-06-24.md`
- `explorations/gu-minimal-action-spec-2026-06-24.md`
- `explorations/gu-closed-loop-action-ig-branch-2026-06-24.md`
- `explorations/ig-dynamics-nonzero-theta-action-gate-2026-06-24.md`
- `explorations/gu-typed-operator-action-spine-2026-06-24.md`
