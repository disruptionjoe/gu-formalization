---
title: "Cycle 2 Source-Forced S_IG_dyn Action Gate"
date: "2026-06-24"
status: exploration/gate
doc_type: cycle2_source_forced_s_ig_dyn_action_gate
verdict: "FORMAL_TEMPLATE_EXISTS_BUT_SOURCE_FORCED_S_IG_DYN_REMAINS_UNDERDEFINED"
owned_path: "explorations/cycle-gates-and-audits/cycle2-source-forced-s-ig-dyn-action-gate-2026-06-24.md"
optional_audit: "tests/cycle2_source_forced_s_ig_dyn_action_audit.py"
depends_on:
  - "RESEARCH-POSTURE.md"
  - "process/runbooks/five-lane-frontier-run.md"
  - "explorations/cycle-gates-and-audits/cycle1-branch3-dynamical-ig-current-gate-2026-06-24.md"
  - "explorations/dark-energy-cosmology/mission-a-lambda-dark-energy-provenance-2026-06-24.md"
  - "explorations/cycle-gates-and-audits/gu-minimal-action-spec-2026-06-24.md"
  - "explorations/misc/gu-closed-loop-action-ig-branch-2026-06-24.md"
  - "explorations/misc/ig-dynamics-nonzero-theta-action-gate-2026-06-24.md"
  - "explorations/geometry-curvature-emergence/stress-energy-shadow-emergence-certificate-2026-06-24.md"
  - "explorations/cycle-gates-and-audits/gu-typed-operator-action-spine-2026-06-24.md"
  - "explorations/cycle-gates-and-audits/primary-gu-interface-contract-2026-06-24.md"
  - "explorations/firewall-and-two-geometries/source-geometry-not-quantized-gravity-contract-2026-06-24.md"
---

# Cycle 2 Source-Forced `S_IG_dyn` Action Gate

## 1. Verdict

Verdict:

```text
UNDERDEFINED.
```

More precisely:

```text
formal gauge-invariant Branch 3 action template: YES
source-forced Branch 3 action existence theorem: NO
current promotion status: do not promote
first missing object: SourceForcedIGDynamicsSelector
```

Cycle 1 identified the first missing Branch 3 object as a source-forced
`S_IG_dyn`. Pushing one level deeper changes the shape of the obstruction but does not
close it. A legitimate local action template can be written whose variation produces an
IG current `J_IG`, a total source `theta_eff`, and a Noether contract for total-current
conservation. However, the required sources do not select that action from GU source
geometry. The typed action spine and source-geometry contracts explicitly leave
`S_IG` / `S_IG_dyn` as an open slot.

Therefore existing action-spine/source-geometry files are sufficient for a typed
candidate, but not sufficient for an existence theorem that the candidate is forced by GU
rather than chosen as a model.

This artifact does not claim that GU derives Lambda, cancels Lambda, derives dark energy,
or derives a dark-energy equation of state. It also does not claim a generated
`Z_theta`, `C_Rtheta`, or `xi_eff`.

## 2. Candidate Action Functional And Allowed Source Terms

Use the Branch 3 dynamical variables:

```text
Y = Met_Lor(X), with fixed g_Y in the current baseline
G = Sp(64)
P -> Y
A in Conn(P)
epsilon = IG/gauge variable
beta in Omega^1(Y, ad P)
U = Ad(epsilon^-1) beta in Omega^1(Y, ad P)
theta = A - Gamma(epsilon) - U
P_IG in Omega^2(Y, ad P)          for the first-order parent form
s: X -> Y                         observer/metric section
```

The cleanest candidate is the first-order parent action:

```text
S_IG_dyn^parent[A,epsilon,U,P_IG;s]
  =
    int_Y <P_IG, D_A U>
  - 1/(2 Z_U) int_Y <P_IG, P_IG>
  - int_Y V_src(U, epsilon)
  - c_theta/2 int_Y <theta, theta>
  + S_cross_src[A,epsilon,U,P_IG,s]
  + S_boundary.
```

Here `P_IG` has degree 2 because `U` is a 1-form and `D_A U` is a 2-form. Eliminating
`P_IG` gives the second-order template:

```text
S_IG_dyn^2nd
  =
  - Z_U/2 int_Y <D_A U, D_A U>
  - int_Y V_src(U, epsilon)
  - c_theta/2 int_Y <theta, theta>
  + S_cross_src
  + S_boundary.
```

This is a legitimate gauge-covariant template if:

```text
A -> g^-1 A g + g^-1 d g
U -> Ad(g^-1) U
P_IG -> Ad(g^-1) P_IG
theta -> Ad(g^-1) theta
Gamma(epsilon) transforms as a connection reference
the pairings are Ad-invariant
the boundary term kills integrations by parts under the declared boundary data.
```

Allowed source terms are only these:

| term | current status | allowed only if |
|---|---|---|
| `-c_theta/2 int <theta,theta>` | typed by existing action notes | `Gamma(epsilon)` is independent of `A` in the needed variation and free beta is not the only IG equation. |
| `int <P_IG,D_A U> - 1/(2Z_U)int<P_IG,P_IG>` | legitimate template | source geometry selects the first-order parent field, its degree, pairing, and `Z_U`. |
| `-Z_U/2 int<D_A U,D_A U>` | equivalent template after eliminating `P_IG` | `D_A U` is the source-forced kinetic operator, not just a convenient choice. |
| `-int V_src(U,epsilon)` | open slot | `V_src` is fixed by invariant source geometry before target data. |
| `S_cross_src[A,epsilon,U,P_IG,s]` | open slot | every cross term has primary/source provenance and a fixed coefficient. |
| `S_boundary` | required data | boundary conditions are part of the variational problem. |

Source-forcing rule:

```text
The branch must supply a map

SourceForcedIGDynamicsSelector:
  I_GU source data
    -> (field degree of U and P_IG,
        kinetic operator K_IG,
        invariant pairing Q_IG,
        Z_U normalization,
        V_src,
        S_cross_src,
        boundary data)

before any black-hole, Lambda, dark-energy, DESI/Rubin, or xi_eff target is consulted.
```

Target-fitting exclusion:

```text
The following are not allowed inputs to S_IG_dyn:
  bare Lambda;
  bare 4D R[g] theta^2;
  an R theta^2 term inserted to obtain xi_eff;
  a potential V chosen to fit w_0, w_a, DESI/Rubin windows, or xi_eff ~= -0.6;
  cross terms chosen to cancel Schwarzschild/Kerr residuals after seeing the residual;
  boundary data chosen to fit the observed dark-energy scale.
```

The current repository contains the typed domain and the candidate templates. It does not
contain the `SourceForcedIGDynamicsSelector`.

## 3. Variation/Current Contract: `delta S_IG_dyn / delta A`, `J_IG`, `theta_eff`

Use the parent action because it exposes the current without hiding it in second-order
notation. With the sign convention above:

```text
delta_A theta = delta A
delta_A(D_A U) = [delta A, U]
```

so the source-sector connection variation has the schematic form:

```text
delta_A S_IG_dyn
  =
  int_Y <
    - c_theta theta
    + J_IG
    + J_cross,
    delta A
  >
  + boundary.
```

Thus:

```text
delta S_IG_dyn / delta A
  =
  - c_theta theta + J_IG + J_cross.
```

For the parent term:

```text
J_IG = ad_U^dagger(P_IG)
```

which is written schematically in the existing notes as:

```text
J_IG = [U, P_IG]
```

with the exact sign and form-degree convention fixed by the chosen pairing. The other
parent equations are:

```text
E_P:
  D_A U - Z_U^-1 P_IG = 0

E_U:
  - D_A^* P_IG + V_U + c_theta theta + E_U^cross = 0

E_epsilon:
  c_theta L_epsilon^* theta + V_epsilon + E_epsilon^cross
  + possible Gamma(epsilon) terms = 0.
```

After adding the Yang-Mills variation, and suppressing spinor/section terms that are zero
only in a proved vacuum reduction, the connection equation is:

```text
E_A =
  g_A^-2 D_A^* F_A
  - c_theta theta
  + J_IG
  + J_cross
  + J_Psi
  + J_section
  = 0.
```

Define the total source:

```text
theta_eff =
  g_A^2(
    c_theta theta
    - J_IG
    - J_cross
    - J_Psi
    - J_section
  ).
```

Then the connection equation can be written:

```text
D_A^* F_A = theta_eff.
```

This is the strongest valid Branch 3 contract. It is not the old bare-theta source law.
Any Branch 3 artifact that keeps `D_A^*F_A = theta` while retaining a nonzero `J_IG`
has lost track of its own variation.

## 4. Conservation Identity Needed And What Proves It

The required conservation target is:

```text
D_A^* theta_eff = 0
```

or a precisely weaker projected observer conservation theorem.

For Branch 3 the proof should come from the source-sector gauge Noether identity, not from
assuming a generic Yang-Mills double-divergence identity. Infinitesimal local gauge
variation gives a formal identity of the shape:

```text
D_A^*(
  c_theta theta
  - J_IG
  - J_cross
  - J_Psi
  - J_section
)
=
  N_U(E_U)
  + N_P(E_P)
  + N_epsilon(E_epsilon)
  + N_s(E_s)
  + N_Psi(E_Psi)
  + boundary_terms.
```

Therefore:

```text
D_A^* theta_eff = 0
```

follows only after all of the following are supplied:

1. local `Sp(64)` gauge invariance of the written `S_IG_dyn + S_cross_src`;
2. transformation rules for `epsilon`, `U`, `P_IG`, `s`, and `Psi`;
3. boundary conditions that remove the gauge-variation boundary term;
4. the full non-connection EL equations required by the identity;
5. the exact sign and adjoint conventions in the `J_IG` definition.

This is a real theorem contract, but it is not yet a theorem in the repo. The existing
files say Branch 3 should use total-current language; they do not write the fixed
source-sector Noether identity for a source-forced action.

## 5. Why This Does Or Does Not Generate `Z_theta`, `C_Rtheta`, `xi_eff`

The candidate action does not generate the dark-energy coefficient packet by itself.

It introduces or permits:

```text
Z_U
V_src(U,epsilon)
J_IG
theta_eff
```

It does not yet compute:

```text
Z_theta
C_Rtheta
xi_eff = C_Rtheta / Z_theta.
```

Those are observer-reduction quantities, not labels on the parent action. To obtain them
one must additionally supply:

```text
s_FLRW: X -> Y
observer projection Pi_obs
homogeneous scalar mode s^*U or s^*theta_eff = b_raw(t) u_0
representation type and normalization of u_0
fiber/normal integration measure
quadratic expansion of the same source-forced action
canonical normalization B = sqrt(Z_theta) b_raw
curvature coefficient C_Rtheta in the reduced 4D action
residual ledger for non-scalar or higher-derivative terms.
```

Only then can the reduced action be read as:

```text
S_2[b_raw,g]
  =
  int_X sqrt(-g) [
    -1/2 Z_theta g^mu nu partial_mu b_raw partial_nu b_raw
    -1/2 (C_M + C_Rtheta R[g]) b_raw^2
    + residuals
  ].
```

Nothing in the current source files selects `u_0`, computes the projection measure, or
derives `C_Rtheta`. The parent coefficient `Z_U` is not automatically the observer
wavefunction factor `Z_theta`; it becomes `Z_theta` only after section pullback,
mode selection, and integration.

Therefore the candidate action can host a future computation of `Z_theta`, `C_Rtheta`,
and `xi_eff`, but it does not generate them in the present repo state.

## 6. First Exact Obstruction Or No-Go

There is no no-go theorem against all Branch 3 dynamical IG actions. The parent action
above is a mathematically legitimate gauge-covariant template.

The no-go is narrower and source-relative:

```text
Given the currently read action-spine and source-geometry files, there is no existence
theorem for a source-forced S_IG_dyn.
```

The first exact obstruction is:

```text
missing SourceForcedIGDynamicsSelector.
```

Equivalently, the missing term/operator/map is:

```text
K_IG and its selector:

K_IG(U;A,epsilon,s) = D_A U              candidate only

SourceForcedIGDynamicsSelector(I_GU)
  must prove that K_IG is D_A U, or replace it by the actual source-forced operator,
  and must fix Q_IG, Z_U, V_src, S_cross_src, field degrees, and boundary data.
```

Ordered missing objects:

| order | missing object | why it is first or downstream |
|---:|---|---|
| 1 | `SourceForcedIGDynamicsSelector` | Without it, `S_IG_dyn` is a permitted model, not a source-forced action. |
| 2 | `K_IG` | `D_A U` is natural, but not selected or proved unique. |
| 3 | `Q_IG`, degree of `P_IG`, and `Z_U` | The current normalization and pairing decide the current and positivity. |
| 4 | `V_src` and `S_cross_src` | These terms decide masses, curvature couplings, and section-current corrections. |
| 5 | exact `J_IG` | It depends on the chosen parent/kinetic/cross terms. |
| 6 | exact `theta_eff` | It is the connection-current sum, not just `c_theta theta - [U,P_IG]` if other currents exist. |
| 7 | source-sector Noether identity | Needed to prove total-current conservation. |
| 8 | FLRW projection packet | Needed before `Z_theta`, `C_Rtheta`, or `xi_eff` exist. |

Source obligations for closing the gate:

```text
O1. Primary or source-geometry argument fixes the IG dynamical field content.
O2. The kinetic/parent operator is local, gauge-covariant, and selected before targets.
O3. Pairings and signs are fixed in the same normalization as the connection equation.
O4. Potential and cross terms are geometry-forced or absent, not fitted.
O5. Boundary terms make the variation and Noether identity well-defined.
O6. Free-beta collapse is avoided by the written dynamics, not by prose.
O7. The full current `J_IG` and total source `theta_eff` are derived.
O8. `D_A^*theta_eff=0` is proved from a written Noether identity.
O9. Any FLRW coefficient is computed only after the action packet is locked.
```

## 7. Impact For Branch 3/Dark Energy

Branch 3 remains the strongest honest dynamical route because it can make nonzero IG/theta
data differential rather than algebraically killed by free beta. Its cost is unchanged:
the source is a total current.

Allowed current statement:

```text
Branch 3 has a legitimate formal action template that would yield
D_A^*F_A = theta_eff if source-forced and varied with the stated field content.
```

Forbidden current statements:

```text
Branch 3 derives Lambda.
Branch 3 derives dark energy.
Branch 3 derives xi_eff.
Branch 3 has computed Z_theta or C_Rtheta.
Branch 3 keeps bare D_A^*F_A = theta while retaining dynamical IG current J_IG.
The parent action is source-forced merely because it is natural.
```

For dark energy, this means:

```text
Lambda/dark-energy provenance is still blocked before coefficient generation.
```

The blocker is earlier than the cosmology window. The project does not yet have the
source-forced action whose current would be conserved, whose observer projection would
define a scalar mode, and whose quadratic reduction would define `xi_eff`.

## 8. Next Meaningful Computation

Build:

```text
SourceForcedIGDynamicsPacket_V0.
```

Minimum computation:

1. Try to derive `K_IG` from the source carrier:

   ```text
   Is D_A U the unique first-order local gauge-covariant IG operator
   compatible with the typed spine, g_Y, and the declared field degrees?
   ```

   If yes, record the assumptions. If not, list the competing operators and keep the
   branch underdefined.

2. Fix the parent action data:

   ```text
   degree(P_IG), pairing Q_IG, sign, Z_U, V_src, S_cross_src, S_boundary.
   ```

3. Derive the EL tuple with signs:

   ```text
   E_A, E_U, E_P, E_epsilon, E_s, E_Psi.
   ```

4. Read off:

   ```text
   J_IG,
   theta_eff,
   source-sector Noether identity,
   on-shell or projected conservation status.
   ```

5. Run an anti-fitting negative control:

   ```text
   Replace DESI/Rubin or xi_eff target windows by dummy targets.
   The selected action packet must be unchanged.
   ```

6. Only then run FLRW:

   ```text
   choose u_0 from source constraints,
   compute Z_theta,
   compute C_Rtheta,
   set xi_eff = C_Rtheta / Z_theta,
   compare to target windows after the coefficients are locked.
   ```

Pass condition:

```text
SourceForcedIGDynamicsSelector is supplied, S_IG_dyn is fixed before targets,
J_IG and theta_eff are derived by variation, and D_A^*theta_eff is proved by a written
Noether identity.
```

Rollback conditions:

```text
S_IG_dyn_absent;
S_IG_dyn_template_only;
SourceForcedIGDynamicsSelector_missing;
K_IG_not_selected;
Z_U_or_V_src_target_fitted;
S_cross_src_chosen_after_residual_or_target;
J_IG_not_derived_from_delta_A;
theta_eff_missing_total_current_terms;
bare_theta_source_retained_in_Branch_3;
Noether_identity_not_written;
total_current_conservation_not_proved;
Z_theta_or_C_Rtheta_claimed_without_FLRW_reduction;
xi_eff_fitted_not_generated;
bare_Lambda_inserted;
bare_Rtheta_inserted;
DESI_Rubin_window_used_upstream;
dark_energy_derivation_claimed_before_action_packet_closes.
```

## 9. Machine-Readable JSON Summary

```json
{
  "artifact": "CYCLE2_SOURCE_FORCED_S_IG_DYN_ACTION_GATE",
  "version": "2026-06-24",
  "mission_posture": "Mission_A_constructive_obstruction",
  "verdict": "underdefined",
  "verdict_detail": "formal_template_exists_but_source_forced_existence_theorem_not_available",
  "promotion_decision": {
    "promoted": false,
    "from": "Branch_3_candidate_total_current_template",
    "to": "source_forced_action_existence_theorem",
    "reason": "SourceForcedIGDynamicsSelector_missing"
  },
  "explicit_non_claims": {
    "GU_derives_Lambda": false,
    "GU_cancels_Lambda": false,
    "GU_derives_dark_energy": false,
    "GU_derives_Z_theta": false,
    "GU_derives_C_Rtheta": false,
    "GU_derives_xi_eff": false,
    "bare_Lambda_source_derived": false,
    "bare_Rtheta_source_derived": false
  },
  "candidate_action": {
    "legitimate_formal_template": true,
    "source_forced": false,
    "parent_form": "int<P_IG,D_A U>-1/(2Z_U)int<P_IG,P_IG>-int V_src(U,epsilon)-c_theta/2 int<theta,theta>+S_cross_src+S_boundary",
    "second_order_form": "-Z_U/2 int<D_A U,D_A U>-int V_src(U,epsilon)-c_theta/2 int<theta,theta>+S_cross_src+S_boundary",
    "field_degrees": {
      "U": "Omega^1(Y,adP)",
      "P_IG": "Omega^2(Y,adP)_if_K_IG_equals_D_A_U"
    },
    "allowed_source_terms": [
      "theta_norm",
      "parent_kinetic_pairing",
      "second_order_D_A_U_kinetic_after_eliminating_P_IG",
      "V_src_if_source_forced",
      "S_cross_src_if_primary_sourced",
      "S_boundary"
    ],
    "excluded_target_fit_terms": [
      "bare_Lambda",
      "bare_4D_Rtheta2",
      "xi_eff_selected_term",
      "DESI_Rubin_selected_potential",
      "black_hole_residual_selected_cross_term",
      "dark_energy_scale_selected_boundary_data"
    ]
  },
  "source_forcing_target_fitting_separation": {
    "source_forcing_requires": [
      "SourceForcedIGDynamicsSelector",
      "K_IG_selected_before_targets",
      "Q_IG_and_Z_U_fixed_before_targets",
      "V_src_fixed_before_targets",
      "S_cross_src_fixed_before_targets",
      "boundary_data_fixed_before_targets"
    ],
    "target_fitting_forbidden_inputs": [
      "Lambda_value",
      "dark_energy_equation_of_state",
      "DESI_Rubin_window",
      "xi_eff_target",
      "Schwarzschild_Kerr_residual_after_evaluation"
    ],
    "replacement_target_check_required": true
  },
  "variation_current_contract": {
    "delta_S_IG_dyn_delta_A": "-c_theta theta + J_IG + J_cross",
    "J_IG_parent": "ad_U_dagger(P_IG)_schematically_[U,P_IG]",
    "E_P": "D_A U - Z_U^-1 P_IG = 0",
    "E_U": "-D_A^*P_IG + V_U + c_theta theta + E_U_cross = 0",
    "E_A_full": "g_A^-2 D_A^*F_A - c_theta theta + J_IG + J_cross + J_Psi + J_section = 0",
    "theta_eff": "g_A^2(c_theta theta - J_IG - J_cross - J_Psi - J_section)",
    "source_law": "D_A^*F_A=theta_eff"
  },
  "conservation_contract": {
    "target": "D_A^*theta_eff=0",
    "proving_identity": "source_sector_gauge_Noether_identity",
    "identity_shape": "D_A^*(c_theta theta - J_IG - all_currents)=N_U(E_U)+N_P(E_P)+N_epsilon(E_epsilon)+N_s(E_s)+N_Psi(E_Psi)+boundary_terms",
    "current_status": "not_written_for_source_forced_action",
    "requires": [
      "local_Sp64_gauge_invariance",
      "field_transformation_rules",
      "boundary_terms_vanish",
      "non_connection_EL_equations",
      "exact_current_signs_and_pairings"
    ]
  },
  "coefficient_generation": {
    "Z_theta_generated": false,
    "C_Rtheta_generated": false,
    "xi_eff_generated": false,
    "reason": "FLRW_projection_packet_missing",
    "needed_before_coefficients": [
      "s_FLRW",
      "Pi_obs",
      "scalar_mode_u0",
      "mode_normalization",
      "projection_measure",
      "quadratic_reduction",
      "canonical_normalization",
      "residual_ledger"
    ]
  },
  "first_exact_obstruction": {
    "id": "SourceForcedIGDynamicsSelector",
    "missing_term_operator_map": "selector_for_K_IG_Q_IG_Z_U_V_src_S_cross_src_field_degrees_boundary_data",
    "candidate_operator": "K_IG(U)=D_A U",
    "candidate_operator_status": "natural_but_not_source_selected_or_unique",
    "no_go_scope": "no_existence_theorem_from_current_sources_not_no_go_against_all_dynamical_IG_actions"
  },
  "ordered_missing_objects": [
    "SourceForcedIGDynamicsSelector",
    "K_IG",
    "Q_IG_degree_P_IG_Z_U",
    "V_src_and_S_cross_src",
    "J_IG",
    "theta_eff",
    "source_sector_Noether_identity",
    "FLRW_projection_packet"
  ],
  "source_obligations": [
    "fix_IG_dynamical_field_content",
    "select_local_gauge_covariant_kinetic_operator_before_targets",
    "fix_pairings_signs_and_normalizations",
    "force_or_exclude_potential_and_cross_terms",
    "state_boundary_terms",
    "avoid_free_beta_collapse_by_written_dynamics",
    "derive_J_IG_and_theta_eff",
    "prove_D_A_star_theta_eff_conservation",
    "compute_FLRW_coefficients_only_after_action_lock"
  ],
  "branch3_impact": {
    "allowed_statement": "Branch_3_has_a_legitimate_formal_total_current_template",
    "current_dark_energy_status": "blocked_before_source_forced_action_and_coefficients",
    "source_law_rewrite_required": true,
    "bare_theta_source_retained": false
  },
  "next_computation": {
    "id": "SourceForcedIGDynamicsPacket_V0",
    "steps": [
      "derive_or_refute_K_IG_equals_D_A_U_from_source_carrier",
      "fix_parent_action_data",
      "derive_EL_tuple",
      "read_off_J_IG_theta_eff_and_Noether_identity",
      "run_replacement_target_anti_fitting_check",
      "only_then_compute_FLRW_Z_theta_C_Rtheta_xi_eff"
    ],
    "pass_condition": "S_IG_dyn_fixed_before_targets_J_IG_theta_eff_derived_and_D_A_star_theta_eff_proved"
  },
  "rollback_conditions": [
    "S_IG_dyn_absent",
    "S_IG_dyn_template_only",
    "SourceForcedIGDynamicsSelector_missing",
    "K_IG_not_selected",
    "Z_U_or_V_src_target_fitted",
    "S_cross_src_chosen_after_residual_or_target",
    "J_IG_not_derived_from_delta_A",
    "theta_eff_missing_total_current_terms",
    "bare_theta_source_retained_in_Branch_3",
    "Noether_identity_not_written",
    "total_current_conservation_not_proved",
    "Z_theta_or_C_Rtheta_claimed_without_FLRW_reduction",
    "xi_eff_fitted_not_generated",
    "bare_Lambda_inserted",
    "bare_Rtheta_inserted",
    "DESI_Rubin_window_used_upstream",
    "dark_energy_derivation_claimed_before_action_packet_closes"
  ]
}
```

## Sources Read

- `RESEARCH-POSTURE.md`
- `process/runbooks/five-lane-frontier-run.md`
- `explorations/cycle-gates-and-audits/cycle1-branch3-dynamical-ig-current-gate-2026-06-24.md`
- `explorations/dark-energy-cosmology/mission-a-lambda-dark-energy-provenance-2026-06-24.md`
- `explorations/cycle-gates-and-audits/gu-minimal-action-spec-2026-06-24.md`
- `explorations/misc/gu-closed-loop-action-ig-branch-2026-06-24.md`
- `explorations/misc/ig-dynamics-nonzero-theta-action-gate-2026-06-24.md`
- `explorations/geometry-curvature-emergence/stress-energy-shadow-emergence-certificate-2026-06-24.md`
- `explorations/cycle-gates-and-audits/gu-typed-operator-action-spine-2026-06-24.md`
- `explorations/cycle-gates-and-audits/primary-gu-interface-contract-2026-06-24.md`
- `explorations/firewall-and-two-geometries/source-geometry-not-quantized-gravity-contract-2026-06-24.md`
