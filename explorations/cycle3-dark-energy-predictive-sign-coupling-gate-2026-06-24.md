---
title: "Cycle 3 Dark-Energy Predictive Sign/Nonminimal-Coupling Gate"
date: "2026-06-24"
status: exploration/gate
doc_type: cycle3_dark_energy_predictive_sign_coupling_gate
verdict: "TARGET_SENSITIVE_FIT_WINDOW_FOR_DESI_NOT_GU_PREDICTION"
owned_path: "explorations/cycle3-dark-energy-predictive-sign-coupling-gate-2026-06-24.md"
optional_audit: "tests/cycle3_dark_energy_predictive_sign_coupling_audit.py"
depends_on:
  - "RESEARCH-POSTURE.md"
  - "process/runbooks/five-lane-frontier-run.md"
  - "roadmap/objection-triage-register.md"
  - "explorations/mission-a-lambda-dark-energy-provenance-2026-06-24.md"
  - "explorations/cycle2-source-forced-s-ig-dyn-action-gate-2026-06-24.md"
  - "explorations/dark-energy-oq3a-slow-roll-ic-sign-2026-06-23.md"
  - "explorations/dark-energy-w-window-mechanism-2026-06-23.md"
  - "explorations/flrw-theta-xi-branch-reduction-2026-06-24.md"
---

# Cycle 3 Dark-Energy Predictive Sign/Nonminimal-Coupling Gate

## 1. Verdict

Current decision:

```text
The dark-energy lane does not currently contain a GU prediction of DESI or of dark
energy.

It contains:
  1. a conditional minimal theta-field control that predicts w_a > 0 under the
     scalar, minimal-coupling, slow-roll-attractor assumptions; and
  2. a DESI-compatible nonminimal-coupling window, xi_eff < -0.319 and
     xi_eff near -0.6, that is currently a phenomenological target window, not
     a GU-derived coefficient.
```

The decision-grade split is:

| object | current status | decision |
|---|---|---|
| Minimal theta scalar with `xi = 0` | conditional model prediction | sign-stable `w_a > 0`; discordant with the repo DESI target sign. |
| Nonminimal `xi R theta^2` route | mechanism/window | reaches `w_a < 0` only if `xi_eff < -0.319`; DESI ratio near `xi_eff ~= -0.6`; not predicted. |
| GU source provenance | missing | no current branch emits `Z_theta`, `C_Rtheta`, or `xi_eff = C_Rtheta / Z_theta`. |

Therefore OBJ-DESI is not closed as a positive empirical prediction. It is a sharp
gate:

```text
minimal route: predictive sign mismatch;
nonminimal route: alive only as a source-provenance challenge;
current DESI compatibility: fit/window, not GU prediction.
```

The lane may be promoted only if the nonminimal coefficient is generated before
DESI/Rubin target values are consulted. A coefficient chosen because it lands near
`xi_eff ~= -0.6` remains a fit even if it matches the observed CPL ratio.

## 2. Minimal theta-field sign status

The minimal theta-field computation is the only part of the lane that behaves like a
prediction in the ordinary model-building sense. Under the assumptions:

```text
s^*theta is a homogeneous scalar mode;
the effective action is minimally coupled, xi = 0;
M_KK = 2 sqrt(2) H_0;
initial data are the slow-roll attractor from z >> z_osc;
the CPL readout uses w_a = dw_DE/dz at z = 0.
```

the repository computations give:

```text
w_a > 0.
```

This is not merely a target fit. The sign is stable across the frozen `z = 3` control
and the slow-roll-attractor control, and the mechanism scan reproduces the baseline
positive ratio. In that narrow sense, the minimal theta model predicts a sign.

But this is not yet a full GU dark-energy prediction because the upstream source
certificate is missing. The scalar character of `s^*theta`, the normalization, the
same-branch action, and the coefficient packet are not derived from a closed GU source
object. The accurate status is:

```text
minimal theta scalar control: sign-predictive, conditional, DESI-sign-discordant;
GU dark-energy prediction: not established.
```

If future DESI/Rubin-grade evidence robustly requires `w_a < 0` in the same CPL
convention, then the minimal theta scalar route is empirically falsified as a
DESI-sign explanation. That does not by itself falsify every nonminimal GU route; it
does kill the claim that the minimal theta sector explains the sign.

## 3. Nonminimal `xi R theta^2` window status

The mechanism search identifies one route that reaches the DESI sign:

```text
xi_eff < -0.319       gives w_a < 0;
xi_eff ~= -0.6        gives the repo DESI-ratio match at reconstruction grade.
```

Minimal and familiar reference values do not work:

```text
xi = 0          wrong sign;
xi = +1/6       wrong sign;
xi = -1/6       wrong sign.
```

So the nonminimal mechanism is real as FLRW dynamics, but it is not a prediction. It is
a window in one free coefficient. Its current epistemic status is:

```text
phenomenological_control / target-sensitive fitting window.
```

The reason is structural. The branch-reduction file reports:

```text
No currently written viable action branch generates negative xi_eff.
```

Branch 4 kills the theta mode. Branches 1, 2A, 2B, and 3 leave `Z_theta` and
`C_Rtheta` undefined. Branch 3 is the strongest physical route, but it first requires a
source-forced `S_IG_dyn` and total-current reduction. A bare inserted `R theta^2` term is
not evidence for GU provenance.

Thus the nonminimal window should be cited only as:

```text
The unique identified FLRW mechanism capable of reaching the DESI sign, conditional on
a future source-derived negative xi_eff.
```

It should not be cited as:

```text
a GU-predicted DESI dark-energy sign.
```

## 4. Source provenance needed for `xi`

The exact source object needed is:

```text
ThetaXiSourceCoefficientCertificate(branch)
```

It is a same-branch coefficient certificate. It would make `xi_eff` predicted rather
than fit only if it emits the coefficient before target comparison.

Minimum fields:

```text
branch_lock:
  fixed source branch, variation space, boundary data, observer projection,
  and section/pullback regime;

source_action:
  written source-forced action or operator/action pair;
  for Branch 3, this includes SourceForcedIGDynamicsSelector and S_IG_dyn;
  for Branch 2A, this includes the derived A-independent Phi and tangent certificate;

current_and_conservation:
  full Euler-Lagrange tuple;
  bare theta current only if the branch really preserves it;
  theta_eff total current for Branch 3;
  Noether/Bianchi conservation proof for the same current;

scalar_projection:
  proof that s^*theta or s^*theta_eff has a homogeneous scalar mode b_raw(t) u_0;
  proof that the mode is not spin-2, pure gauge, constrained away, or killed by beta;
  fixed normalization and fiber/normal measure;

quadratic_reduction:
  S_2[b_raw,g] =
    int_X sqrt(-g) [
      -1/2 Z_theta g^mu nu partial_mu b_raw partial_nu b_raw
      -1/2 (C_M + C_Rtheta R[g]) b_raw^2
      + named residuals
    ];

canonical_readout:
  Z_theta > 0;
  B = sqrt(Z_theta) b_raw;
  xi_eff = C_Rtheta / Z_theta;

anti_fitting_log:
  coefficient emitted before DESI/Rubin windows are opened;
  dummy-target and withheld-target checks passed;
  target values not used in Phi, S_IG_dyn, V, u_0, boundary data, or normalization.
```

The first missing upstream object for Branch 3 remains:

```text
SourceForcedIGDynamicsSelector
```

But `SourceForcedIGDynamicsSelector` alone is not enough to predict `xi`. It must feed the
larger `ThetaXiSourceCoefficientCertificate`, because `xi_eff` is an observer-reduction
quantity:

```text
xi_eff = C_Rtheta / Z_theta.
```

## 5. DESI/Rubin anti-fitting protocol

The anti-fitting protocol is mandatory if this lane is to become empirical rather than
curve-fitting.

1. Branch freeze.

   ```text
   Select the source branch, variation rules, boundary data, scalar projection,
   and action packet before consulting DESI/Rubin values.
   ```

2. Target quarantine.

   ```text
   DESI/Rubin CPL windows, xi_eff thresholds, and ratio targets are not inputs to
   Phi, S_IG_dyn, V, cross terms, u_0, normalization, or boundary data.
   ```

3. Coefficient lock.

   ```text
   Emit Z_theta, C_Rtheta, xi_eff, M_eff, amplitude rules, and phase rules with a
   provenance row before observational comparison.
   ```

4. Replacement check.

   ```text
   Re-run the derivation with a dummy target and with the target withheld. The
   coefficient packet must be unchanged.
   ```

5. Negative controls.

   ```text
   Minimal xi = 0 must remain the positive-w_a control.
   Conformal xi = +1/6 must remain a control, not a target-selected escape.
   Bare inserted R theta^2 remains provenance-failed.
   Free beta remains theta-killing.
   ```

6. Post-lock comparison.

   ```text
   Only after the packet is locked compare xi_eff with -0.319, xi ~= -0.6,
   DESI/Rubin likelihoods, w_0, w_a, and f_0.
   ```

7. Rollback on leakage.

   ```text
   Any upstream use of the target window demotes the result to phenomenological
   control, no matter how well the final number matches.
   ```

## 6. First exact obstruction or falsifier

The first exact obstruction is:

```text
missing ThetaXiSourceCoefficientCertificate(branch).
```

The first Branch 3 sub-obstruction is:

```text
missing SourceForcedIGDynamicsSelector.
```

The first falsifier for the DESI-sign route is one of the following source-side
outcomes:

```text
1. no FLRW scalar mode survives;
2. Z_theta <= 0 and no gauge reduction removes the bad mode;
3. C_Rtheta is zero, positive, or too weak so that xi_eff >= -0.319;
4. theta_eff is not conserved from the written action;
5. the only way to obtain xi_eff < -0.319 is to insert R theta^2 or choose data after
   seeing the DESI/Rubin target;
6. the source-generated branch predicts a locked (w_0, w_a) pair excluded by the
   DESI/Rubin likelihood after all predeclared nuisance parameters are fixed.
```

The cleanest mathematical kill condition is:

```text
For every source-forced branch with a surviving scalar theta mode and Z_theta > 0,
xi_eff = C_Rtheta / Z_theta >= -0.319.
```

That would kill the only identified DESI-sign mechanism in the current theta-field lane.

The cleanest empirical kill condition for the minimal route is:

```text
DESI/Rubin-grade data robustly require w_a < 0 in the same convention and exclude the
minimal theta prediction w_a > 0.
```

The cleanest empirical kill condition for a future source-generated nonminimal route is:

```text
The locked source-generated xi_eff, f_0, and phase/amplitude packet predict a
predeclared (w_0, w_a) region excluded by the joint DESI/Rubin likelihood.
```

## 7. Impact for GU empirical usefulness

This lane is empirically useful now as a falsification and coefficient-selection gate, not
as positive evidence.

Positive impact:

```text
The dark-energy problem has been compressed to a small number of exact source objects:
SourceForcedIGDynamicsSelector and ThetaXiSourceCoefficientCertificate.
```

Negative impact:

```text
The DESI-compatible result currently depends on choosing a sizable negative xi. Without
source provenance, this is the kind of target-sensitive fit the research posture forbids
promoting.
```

If GU ultimately emits `xi_eff < -0.319` before target comparison, the lane becomes a real
empirical test. If it emits `xi_eff ~= -0.6` with the full anti-fitting protocol satisfied,
the result would be high-information support for the reconstruction branch. If it emits
`xi_eff >= -0.319` or no scalar mode, then the DESI-sign dark-energy route fails cleanly.

Current bottom line:

```text
GU empirical usefulness from this lane is potential, not achieved.
```

## 8. Next meaningful computation

Do not run another cosmology scan first. The next computation is geometric/source-side:

```text
ThetaXiSourceCoefficientPacket_V0.
```

Inputs:

```text
fixed Branch 3 S_IG_dyn candidate or fixed Branch 2A Phi certificate;
fixed variation space and boundary data;
fixed observer projection;
no DESI/Rubin target values;
no bare Lambda;
no bare inserted R theta^2.
```

Outputs:

```text
source-forced or source-failed action verdict;
EL tuple;
theta or theta_eff current;
Noether conservation status;
surviving scalar mode or no-scalar verdict;
Z_theta;
C_Rtheta;
xi_eff = C_Rtheta / Z_theta;
rollback/falsification row;
post-lock comparison permission.
```

Pass condition:

```text
The same source branch emits Z_theta > 0 and C_Rtheta before targets, so xi_eff is
read off rather than chosen.
```

Decision table:

| output | decision |
|---|---|
| no scalar mode | theta-FLRW KG route inapplicable. |
| `Z_theta <= 0` | scalar route fails unless the bad mode is pure gauge/removed. |
| `xi_eff >= -0.319` | DESI-sign nonminimal route absent for that branch. |
| `xi_eff < -0.319` emitted before targets | DESI-sign mechanism becomes source-predicted; compare after lock. |
| `xi_eff ~= -0.6` emitted before targets | DESI-ratio branch becomes high-information empirical candidate. |
| target value appears upstream | demote to phenomenological control. |

## 9. Machine-readable JSON summary

```json
{
  "artifact": "CYCLE3_DARK_ENERGY_PREDICTIVE_SIGN_COUPLING_GATE",
  "version": "2026-06-24",
  "verdict": "target_sensitive_fit_window_for_DESI_not_GU_prediction",
  "verdict_class": "conditional_minimal_prediction_plus_nonminimal_fit_window",
  "gu_predicts_desi_dark_energy": false,
  "gu_dark_energy_prediction_status": "not_established",
  "current_lane_status": {
    "minimal_theta": "conditional_sign_prediction_wrong_DESI_sign",
    "nonminimal_xi": "phenomenological_window_not_predicted",
    "source_provenance": "missing"
  },
  "minimal_theta_field_sign": {
    "wa_sign": "positive",
    "wa_expression": "w_a > 0",
    "predictive_status": "conditional_minimal_scalar_model_prediction",
    "assumptions": [
      "s_star_theta_scalar",
      "xi_equals_0",
      "M_KK_equals_2_sqrt_2_H0",
      "slow_roll_attractor_initial_conditions",
      "CPL_readout_w_a_equals_dw_DE_dz_at_z0"
    ],
    "DESI_sign_status": "discordant_with_repo_DESI_target",
    "full_GU_provenance": false
  },
  "nonminimal_xi_window": {
    "term": "xi R theta^2",
    "canonical_formula": "xi_eff = C_Rtheta / Z_theta",
    "negative_wa_threshold": -0.319,
    "DESI_ratio_match": -0.6,
    "window_status": "reaches_DESI_sign_as_FLRW_mechanism",
    "prediction_status": "not_predicted_currently",
    "xi_generated_by_current_branch": false,
    "minimal_xi_status": "wrong_sign",
    "conformal_xi_status": "wrong_sign"
  },
  "source_provenance_needed": {
    "exact_object": "ThetaXiSourceCoefficientCertificate",
    "branch3_first_subobject": "SourceForcedIGDynamicsSelector",
    "required_outputs": [
      "written_source_forced_action_or_operator_action_pair",
      "full_Euler_Lagrange_tuple",
      "theta_or_theta_eff_current",
      "Noether_conservation_proof",
      "FLRW_scalar_mode_u0",
      "mode_normalization",
      "Z_theta",
      "C_Rtheta",
      "xi_eff",
      "anti_fitting_log"
    ],
    "makes_xi_predicted_if": "xi_eff_is_emitted_before_DESI_Rubin_targets_and_survives_replacement_checks"
  },
  "DESI_Rubin_anti_fitting_protocol": [
    "branch_freeze",
    "target_quarantine",
    "coefficient_lock",
    "replacement_withheld_target_check",
    "negative_controls",
    "post_lock_likelihood_comparison",
    "rollback_on_target_leakage"
  ],
  "first_exact_obstruction": {
    "id": "missing_ThetaXiSourceCoefficientCertificate",
    "branch3_subobstruction": "missing_SourceForcedIGDynamicsSelector",
    "coefficient_status": "no_generated_Z_theta_C_Rtheta_xi_eff",
    "current_DESI_compatibility": "fit_window"
  },
  "rollback_conditions": [
    "target_leakage_into_source_construction",
    "source_forced_xi_missing",
    "bare_Rtheta_inserted",
    "no_FLRW_scalar_mode",
    "Z_theta_nonpositive_unresolved",
    "theta_eff_not_conserved",
    "xi_generated_above_negative_window",
    "full_GU_provenance_missing",
    "DESI_Rubin_fit_used_as_input"
  ],
  "falsification_conditions": [
    "minimal_route_falsified_if_robust_same_convention_data_require_w_a_negative",
    "DESI_sign_route_killed_if_all_source_forced_scalar_branches_have_xi_eff_greater_equal_minus_0_319",
    "theta_KG_route_killed_if_s_star_theta_is_not_scalar_or_is_constrained_away",
    "nonminimal_route_demoted_if_negative_xi_requires_target_selected_Rtheta2",
    "future_source_generated_route_falsified_if_locked_w0_wa_region_excluded_by_joint_DESI_Rubin_likelihood"
  ],
  "impact_for_GU_empirical_usefulness": {
    "current_positive_evidence": false,
    "current_usefulness": "sharp_falsification_and_coefficient_gate",
    "promotion_requires": "source_generated_xi_eff_before_target_comparison"
  },
  "next_meaningful_computation": {
    "id": "ThetaXiSourceCoefficientPacket_V0",
    "do_next": true,
    "avoid_next": "another_unproven_cosmology_scan",
    "pass_condition": "same_branch_emits_Z_theta_positive_and_C_Rtheta_before_targets"
  }
}
```

## Sources read

- `RESEARCH-POSTURE.md`
- `process/runbooks/five-lane-frontier-run.md`
- `roadmap/objection-triage-register.md`
- `explorations/mission-a-lambda-dark-energy-provenance-2026-06-24.md`
- `explorations/cycle2-source-forced-s-ig-dyn-action-gate-2026-06-24.md`
- `explorations/dark-energy-oq3a-slow-roll-ic-sign-2026-06-23.md`
- `explorations/dark-energy-w-window-mechanism-2026-06-23.md`
- `explorations/flrw-theta-xi-branch-reduction-2026-06-24.md`
