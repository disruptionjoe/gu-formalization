---
title: "Mission A Lambda/Dark-Energy Provenance Construction Attempt"
date: "2026-06-24"
status: exploration/construction_attempt
doc_type: mission_a_lambda_dark_energy_provenance
verdict: "CERTIFICATE_TARGET_DEFINED; STRONGEST_DYNAMIC_ROUTE_IS_BRANCH_3_THETA_EFF; BLOCKED_BEFORE_SOURCE_GENERATED_COEFFICIENTS"
owned_path: "explorations/dark-energy-cosmology/mission-a-lambda-dark-energy-provenance-2026-06-24.md"
optional_audit: "tests/mission_a_lambda_dark_energy_provenance_audit.py"
depends_on:
  - "RESEARCH-POSTURE.md"
  - "process/runbooks/five-lane-frontier-run.md"
  - "explorations/cycle-gates-and-audits/marble-wood-local-minimum-open-avenues-ledger-2026-06-24.md"
  - "explorations/cycle-gates-and-audits/unified-marble-wood-source-closure-map-2026-06-24.md"
  - "explorations/cycle-gates-and-audits/metric-marble-prematurity-gate-2026-06-24.md"
  - "explorations/geometry-curvature-emergence/stress-energy-shadow-emergence-certificate-2026-06-24.md"
  - "explorations/dark-energy-cosmology/flrw-theta-xi-branch-reduction-2026-06-24.md"
  - "canon/dark-energy-theta-divergence-free.md"
  - "canon/theta-field-flrw-dark-energy-eos.md"
  - "explorations/misc/constraint-first-ig-tangent-space-gate-2026-06-24.md"
---

# Mission A Lambda/Dark-Energy Provenance Construction Attempt

## 1. Verdict

Mission A should treat Lambda/dark energy as a high-value construction target. The
strongest current construction target is not a bare cosmological constant and not a
phenomenological CPL fluid. It is a branch-fixed theta/IG dynamic sector whose observer
projection can produce a conserved dark-energy-like term with generated coefficients.

Current decision:

```text
LambdaDarkEnergyProvenanceCertificate(branch): specified here, not closed.

Strongest dynamic candidate:
  Branch 3 dynamical IG / total current,
  with source law rewritten around theta_eff.

Current proof status:
  conditional construction target,
  blocked before source-generated Z_theta, C_Rtheta, and xi_eff.

Explicit non-claims:
  no bare Lambda is derived;
  no fitted xi_eff is source-derived;
  no DESI/Rubin target window may be used upstream;
  no broad Lambda derivation or cancellation claim is licensed.
```

The branch verdict is constructive but not promotional:

```text
Branch 2A: best conservative bare-theta template, but missing Phi.
Branch 2B: possible corrected-current branch, not bare theta.
Branch 3: strongest dynamic dark-energy shape, but S_IG-dyn is unwritten.
Free beta: fails for nonzero theta; theta = 0.
Phenomenological xi scan: useful control only.
```

If GU is substantially correct in the strong same-source sense, a certificate of the form
below must eventually exist. If it cannot be built, the Lambda/dark-energy branch rolls
back to import/control/phenomenology, not to a GU-derived result.

## 2. If GU Is Correct, What Lambda/Dark-Energy Object Must Exist

The required object is:

```text
LambdaDarkEnergyProvenanceCertificate(branch)
```

It is branch-local. It cannot mix a metric shadow from one source branch, a theta scalar
from another branch, and a DESI/Rubin-fitted coefficient from a third branch.

Minimum certificate fields:

```text
branch_lock:
  fixed G_src, D_GU, S_GU or operator/action pair
  fixed IG variation rule
  fixed section space, boundary data, and observer regime

term_origin:
  exact source term in S_GU or D_GU
  source Euler-Lagrange equation where it enters
  no bare Lambda
  no post-target R[g] theta^2 insertion

mode_survival:
  proof that the theta/IG mode is not killed by the beta variation
  branch-specific source current: bare theta, corrected current, or theta_eff
  proof that the FLRW mode survives constraints and is scalar if a scalar KG reduction is used

coefficient_chain:
  source normalization -> raw field b_raw
  quadratic action -> Z_theta and C_Rtheta
  canonical field B = sqrt(Z_theta) b_raw if Z_theta > 0
  xi_eff = C_Rtheta / Z_theta
  mass/curvature terms fixed before target data

conservation:
  source Noether/Bianchi identity
  branch source law
  projected observer conservation
  no imposed 4D conservation as a substitute

projection_and_placement:
  Pi_4D projection to observer equation
  explicit decision whether the term is on the geometric side, stress side, or residual side
  no double counting between Lambda_eff g_mu_nu and T_mu_nu^theta

anti_fitting_log:
  derivation completed before DESI/Rubin-style target windows are consulted
  target data used only after coefficients are locked
  replacement/withheld-target checks recorded

rollback_ledger:
  exact condition that demotes each term to import, control, residual, fail, or open
```

Allowed outputs:

```text
Lambda_eff = 0
Lambda_eff = imported_constant
Lambda_eff = phenomenological_control
Lambda_eff = source_derived_constant_trace_from_same_branch
dark_energy_term = source_derived_dynamic_theta_IG_term
```

Only the last two could count as source-derived, and only if they come from the same fixed
source branch. A constant-looking output is still not a bare Lambda if and only if its value
and placement are generated by the branch before target data.

## 3. Candidate Source-Derived Route From Theta/IG Data

### 3.1 Branch Choice

The strongest dynamic route is Branch 3, the dynamical IG / total-current branch.

Reason:

- Free beta with only the theta norm kills the mode: `theta = 0`.
- Branch 2A would preserve the bare source equation, but the required
  `Phi(epsilon,beta,s)=0` tangent certificate is absent.
- Branch 2B can keep a nonzero current, but the multiplier corrects the source law.
- Branch 3 is the first route in which nonzero theta/IG can be genuinely differential
  rather than algebraically projected away.

This choice has a cost: the certificate must stop citing bare theta as the conserved source.
It must use the total current:

```text
D_A^* F_A = theta_eff
theta_eff = c_theta theta - J_IG + possible written section/current terms.
```

### 3.2 Required Fields

Candidate branch data:

```text
G_src =
  (Y, g_Y, P -> Y, Sp(64), S, A, F_A,
   s: X -> Y, epsilon, U or P_IG, theta, Psi,
   section data B_s = II_s^H,
   boundary data, observer access, reduction rules)

theta = A - Gamma(epsilon) - U
U = Ad(epsilon^-1) beta
```

The action shape to construct is:

```text
S_GU^3 =
  S_YM[A]
  + S_section[s,A,epsilon,U,Psi]
  + S_IG-dyn[A,epsilon,U]
  + S_Psi_or_matter_if_source_selected

S_IG-dyn =
  - Z_U/2 int_Y |D_A U|^2
  - int_Y V(U,epsilon)
  - c_theta/2 int_Y |theta|^2
```

or the first-order parent:

```text
S_IG-dyn,parent =
  int_Y <P_IG, D_A U>
  - 1/(2 Z_U) int_Y |P_IG|^2
  - int_Y V(U,epsilon)
  - c_theta/2 int_Y |theta|^2.
```

In this artifact, `Z_U` and `V` are not claimed as derived. They are slots that must be
source-forced by the branch. If they are chosen for a target equation of state, the route
is phenomenological control.

### 3.3 Coefficient Chain

The certificate must compute the coefficient chain in this order:

```text
written S_GU^3
  -> source EL tuple (E_s, E_A, E_U or E_P, E_epsilon, E_Psi)
  -> total source current theta_eff
  -> observer projection through s
  -> FLRW homogeneous mode b_raw(t) u_0
  -> quadratic action S_2[b_raw,g]
  -> Z_theta, C_M, C_Rtheta
  -> B = sqrt(Z_theta) b_raw
  -> xi_eff = C_Rtheta / Z_theta
  -> post-derivation comparison to target windows.
```

The FLRW quadratic target form is:

```text
S_eff[b_raw,g] =
  int_X sqrt(-g) [
    -1/2 Z_theta g^mu_nu partial_mu b_raw partial_nu b_raw
    -1/2 (C_M + C_Rtheta R[g]) b_raw^2
    + higher terms
    + residuals explicitly named
  ].
```

If `Z_theta <= 0`, the scalar route fails or becomes a ghost/control unless the gauge
reduction removes the bad mode. If `Z_theta = 0`, there is no canonical scalar. If
`C_Rtheta` is inserted as a bare `R theta^2` term after the target is known, the term is a
failed provenance attempt.

### 3.4 Conservation

The conservation route must be full-action Noether, not an imposed FLRW identity:

```text
full source gauge invariance of S_GU^3
  -> D_A^* E_A + coupled Noether terms = 0
  -> on shell, conserved total current theta_eff
  -> Pi_obs conservation of the observer dark-energy/stress term
```

The canon divergence-free theta file supplies useful reconstruction-grade structure:
theta is dynamic and equivariant, and the Noether-second-theorem route is structurally
sound if theta is the relevant Euler-Lagrange sector. For Branch 3, that language must be
rewritten: the conserved object is the total current generated by the written dynamic IG
action, not generally bare theta.

### 3.5 FLRW Reduction

The branch may enter the FLRW dark-energy gate only after the mode is derived:

```text
g = -dt^2 + a(t)^2 gamma_ij dx^i dx^j
s^* theta_eff or s^* U contains b_raw(t) u_0
u_0 is homogeneous and isotropic
u_0 is scalar under the observer symmetry if a scalar KG equation is used
```

The current theta-field canon can be used as a conditional control for what the FLRW
calculation would mean after the coefficient chain closes. It cannot by itself supply:

- source-derived `B_i` or amplitude;
- source-derived phase/initial condition;
- source-derived `xi_eff`;
- a proof that `s^*theta` is scalar rather than spin-2 or constrained away;
- a source-derived constant Lambda component.

The candidate dynamic observer term, after successful reduction, would have schematic
stress form:

```text
T_mu_nu^theta_eff =
  partial_mu B partial_nu B
  - 1/2 g_mu_nu (partial B)^2
  - 1/2 M_eff^2 B^2 g_mu_nu
  + xi_eff curvature-coupling stress terms
  + controlled higher/residual terms.
```

This is a reconstruction target, not a derived stress tensor today.

## 4. Term Classification

| term or step | classification | reason | rollback condition |
|---|---|---|---|
| `theta = A - Gamma(epsilon) - Ad(epsilon^-1) beta` / `A - Gamma(epsilon) - U` | derived/reconstruction | Current theta/IG definition and equivariance spine are canon-safe, with variational identification still owed. | If the written branch uses a different IG splitting, rederive before citation. |
| Theta is dynamic, not forced constant by metric compatibility | derived/reconstruction | Canon divergence-free file distinguishes theta from `Lambda g_mu_nu`. | If theta is not the relevant source/EL sector, cosmology claims lose support. |
| `D_A^* theta = 0` for bare theta | reconstruction/conditional | Noether route depends on unproved structural identification. | If Assumption 3 fails, bare-theta conservation is not established. |
| Branch 2A `Phi(epsilon,beta,s)=0` | fail/open | Required tangent certificate is absent. | If no natural A-independent Phi exists, stop using bare-theta Branch 2A. |
| Branch 2B multiplier current | reconstruction/open | Possible nonzero source, but not bare theta. | If multiplier terms contribute, all bare-theta language must be replaced. |
| Branch 3 `S_IG-dyn` | reconstruction target | Strongest dynamic shape, action unwritten. | If `S_IG-dyn` is not primary-sourced, route stays control/import. |
| Branch 3 `theta_eff = c_theta theta - J_IG` | reconstruction target | Correct current language for dynamical IG. | If `theta_eff` is not conserved from full Noether identity, dark-energy term is not certified. |
| `Z_U`, potential `V(U,epsilon)` | import until sourced | Needed to write dynamics but not fixed in current repo evidence. | If chosen for DESI/Rubin windows, classify as target-fit control. |
| FLRW mode `b_raw(t) u_0` | reconstruction/open | Needed for scalar reduction, not yet derived from branch constraints. | If no scalar mode survives, KG dark-energy route is inapplicable. |
| `Z_theta` | fail/open | Undefined in current branch data. | If absent, negative xi route cannot be evaluated. |
| `C_Rtheta` | fail/open | Undefined; no bare `R theta^2` term allowed as rescue. | If inserted by hand, provenance fails. |
| `xi_eff = C_Rtheta / Z_theta` | fail/open | Formula specified, coefficient not generated. | If fitted or target-selected, demote to phenomenological control. |
| DESI/Rubin target windows | control | Useful only after derivation. | If used upstream, certificate fails anti-fitting. |
| Bare `Lambda g_mu_nu` | fail/import | Patch term unless same branch generates it. | If inserted as constant, not GU-derived. |
| Umbilic/constant trace component | reconstruction target/import | Could be source-derived only if produced by branch normalization/boundary data. | If amplitude is chosen after cosmology target, demote to import/control. |
| `T_mu_nu^theta_eff` | reconstruction target | Stress shape can be written only after variation/projection/conservation. | If residuals are moved into it, hidden-matter failure. |

## 5. Anti-Fitting Protocol For DESI/Rubin-Style Target Windows

The anti-fitting rule is part of the certificate, not an afterthought.

Required protocol:

1. Branch freeze.

   ```text
   S_GU, variation space, boundary rules, scalar projection, and normalization are fixed
   before DESI/Rubin-style windows are opened.
   ```

2. Coefficient provenance lock.

   ```text
   Z_theta, C_Rtheta, M_eff, xi_eff, amplitude rules, and phase rules are emitted from
   the branch computation with a timestamp/provenance row.
   ```

3. Target quarantine.

   ```text
   Values such as xi_eff < -0.319, xi_eff ~= -0.6, DESI ratio windows, or Rubin forecast
   windows are not inputs to Phi, u_0, V(U), Z_U, boundary conditions, or the scalar ansatz.
   ```

4. Replacement check.

   ```text
   The same branch must produce the same coefficients if the DESI/Rubin window is replaced
   by a dummy target or withheld target.
   ```

5. Negative-control branches.

   ```text
   Free beta must still kill theta.
   Bare R theta^2 insertion must still fail provenance.
   Phenomenological xi scans must remain labeled control.
   ```

6. Post-derivation comparison only.

   ```text
   Only after the coefficient chain closes may the output be compared with
   xi_eff < -0.319, xi_eff ~= -0.6, w_0, w_a, or future survey windows.
   ```

7. Rollback on leakage.

   ```text
   Any target value used upstream demotes the result to phenomenological control, even if
   the final number lands in the observed window.
   ```

## 6. First Exact Obstruction Or Missing Proof Object

For the strongest dynamic route, the first exact missing proof object is:

```text
DynamicIGDarkEnergyCoefficientPacket(branch_3)
```

Required contents:

```text
1. Written gauge-invariant S_IG-dyn or first-order parent action.
2. Proof that Z_U, V(U,epsilon), and any lower-order terms are source-forced, not
   target-selected.
3. Full source EL tuple including E_A and E_U/E_P.
4. Derivation of theta_eff and its Noether conservation.
5. Observer projection through the same section map used for the metric shadow.
6. Surviving FLRW scalar mode u_0 with normalization and representation type.
7. Quadratic action expansion yielding Z_theta and C_Rtheta.
8. Exact placement ledger: geometric correction, stress-energy term, residual, or fail.
9. Exact-GR compatibility check so the term does not rescue black-hole failures.
```

The coefficient chain currently stops before item 1. Therefore no source-derived
`xi_eff`, no source-derived dynamic dark-energy stress tensor, and no source-derived
constant Lambda replacement are certified.

For the bare-theta conservative route, the first obstruction remains:

```text
Branch2AConstraintTangentCertificate:
  gauge-covariant A-independent Phi(epsilon,beta,s)=0,
  D_beta Phi,
  K_beta proper,
  D_A Phi = 0,
  no target-selected conormal directions.
```

Without it, Branch 2A cannot preserve bare `D_A^*F_A = theta` with nonzero theta.

## 7. Constructive Next Computation

Do the dynamic IG coefficient computation before any new cosmology scan:

```text
Computation:
  Branch3LambdaPacket_V0

Input:
  fixed S_YM,
  fixed section action terms already admitted by the source branch,
  candidate S_IG-dyn or first-order parent,
  no bare Lambda,
  no bare R[g] theta^2,
  no DESI/Rubin target values.

Output:
  E_A, E_U/E_P, E_s, E_epsilon;
  theta_eff and conservation identity;
  FLRW scalar-mode survival or no-scalar verdict;
  Z_theta, C_Rtheta, xi_eff if scalar survives;
  provenance classification for each term;
  exact rollback condition.
```

Pass/fail outcomes:

| outcome | decision |
|---|---|
| `Z_theta > 0`, generated `C_Rtheta`, conserved `theta_eff`, exact-GR compatible | conditional source-derived dynamic candidate; compare to target windows after lock. |
| `Z_theta <= 0` or ghost after gauge reduction | fail scalar dark-energy route unless removed as gauge. |
| no scalar `u_0` survives | KG theta dark-energy route inapplicable. |
| generated `xi_eff >= -0.319` | DESI-sign negative-w_a mechanism absent for that branch; still a valid prediction/control. |
| generated `xi_eff < -0.319` before target opening | promote only the coefficient certificate, not broad Lambda solution. |
| coefficient depends on inserted `R theta^2`, potential tuning, or target-selected boundary data | phenomenological control, not provenance. |

If no source-forced `S_IG-dyn` can be written, perform the tau-plus slice audit specified by
the constraint-first gate. If that audit does not produce a true Branch 2A slice, the
dark-energy route should remain open/control rather than cycling through fitted scalars.

## 8. Claim Certificate Table And Machine-Readable Summary

| claim | status | proof grade | allowed citation | forbidden citation | rollback condition |
|---|---|---|---|---|---|
| `LambdaDarkEnergyProvenanceCertificate` | specified_open | certificate specification | "The certificate required for a GU dark-energy provenance claim is specified." | "The certificate is closed." | Any required branch/action/coefficient/conservation field is missing. |
| `BRANCH3_THETA_EFF_DYNAMIC_ROUTE` | strongest_candidate_open | reconstruction target | "Branch 3 is the strongest current dynamic route because it can make IG differential." | "Branch 3 derives dark energy." | `S_IG-dyn` absent, target-selected, or not conserved. |
| `BARE_THETA_BRANCH2A_ROUTE` | underdefined | conditional theorem only | "Bare theta survives only if a derived A-independent Phi exists." | "Bare theta is branch-robust." | Missing Phi, full beta tangent, or target-selected constraint. |
| `FREE_BETA_THETA_DARK_ENERGY` | fail | branch reduction | "Free beta plus only the theta norm kills the theta mode." | "Free beta supports nonzero theta dark energy." | None; branch rejected for nonzero theta. |
| `XI_EFF_PROVENANCE` | open/fail_current | coefficient gate | "xi_eff must be generated as C_Rtheta/Z_theta." | "xi_eff is fitted or inserted as source geometry." | `Z_theta`/`C_Rtheta` undefined or target-fitted. |
| `DESI_RUBIN_COMPARISON` | control_only | post-derivation test | "Survey windows test locked coefficients." | "Survey windows select Phi, u_0, V, or xi_eff." | Any target leakage upstream. |
| `BARE_LAMBDA` | forbidden_as_derivation | import/control/fail | "A bare constant may be an explicit import/control." | "A bare constant is GU source provenance." | Constant inserted without branch generation. |
| `SOURCE_DERIVED_CONSTANT_TRACE` | open | reconstruction target | "A constant-looking source trace would need the same provenance as any dynamic term." | "Umbilic language supplies the observed value." | Normalization or amplitude fitted after target data. |
| `T_THETA_EFF` | open | stress-energy reconstruction target | "A theta_eff stress term is possible only after variation, projection, conservation, and positivity." | "Residuals are theta stress." | Hidden residual relabeling or nonconservation. |

```json
{
  "artifact": "MISSION_A_LAMBDA_DARK_ENERGY_PROVENANCE",
  "version": "2026-06-24",
  "verdict": "CERTIFICATE_TARGET_DEFINED_BRANCH3_THETA_EFF_BLOCKED_BEFORE_COEFFICIENTS",
  "current_status": "specified_open_not_derived",
  "mission_posture": "Mission_A_construction_attempt_with_rollback",
  "lambda_dark_energy_provenance_certificate": {
    "id": "LambdaDarkEnergyProvenanceCertificate",
    "required": true,
    "current_status": "specified_not_closed",
    "branch_local": true,
    "same_source_required": true,
    "no_bare_lambda": true,
    "no_fitted_xi_eff": true,
    "no_desi_rubin_target_input": true,
    "broad_lambda_solution_claimed": false,
    "allowed_outputs": [
      "Lambda_eff_zero",
      "imported_constant",
      "phenomenological_control",
      "source_derived_constant_trace_from_same_branch",
      "source_derived_dynamic_theta_IG_term"
    ]
  },
  "candidate_route": {
    "strongest_dynamic_route": "Branch_3_dynamical_IG_total_current",
    "source_law": "D_A^*F_A=theta_eff",
    "theta_eff": "c_theta theta - J_IG_plus_written_currents",
    "current_status": "action_unwritten_coefficients_undefined",
    "reason_selected": [
      "free_beta_kills_theta",
      "Branch_2A_missing_Phi",
      "Branch_2B_corrects_source_law",
      "Branch_3_can_make_IG_differential"
    ],
    "required_fields": [
      "Y",
      "g_Y",
      "P_to_Y",
      "A",
      "F_A",
      "s",
      "epsilon",
      "U_or_P_IG",
      "theta",
      "S_IG_dyn",
      "boundary_data",
      "observer_projection"
    ],
    "coefficient_chain": [
      "S_GU_branch",
      "source_EL_tuple",
      "theta_eff",
      "Pi_obs",
      "b_raw_u0",
      "S_2_FLRW",
      "Z_theta",
      "C_Rtheta",
      "xi_eff"
    ]
  },
  "term_classifications": {
    "theta_definition": "derived_reconstruction",
    "bare_theta_divergence_free": "conditional_reconstruction",
    "Branch_2A_Phi": "open_missing",
    "Branch_2B_multiplier_current": "open_corrected_source",
    "Branch_3_S_IG_dyn": "reconstruction_target_unwritten",
    "theta_eff_conservation": "open",
    "Z_theta": "undefined",
    "C_Rtheta": "undefined",
    "xi_eff": "undefined_not_generated",
    "DESI_Rubin_windows": "control_only",
    "bare_Lambda": "forbidden_as_source_derivation",
    "T_theta_eff": "open_reconstruction_target"
  },
  "anti_fitting_protocol": [
    "branch_freeze_before_targets",
    "coefficient_provenance_lock",
    "target_quarantine",
    "replacement_withheld_target_check",
    "negative_control_branches",
    "post_derivation_comparison_only",
    "rollback_on_target_leakage"
  ],
  "first_obstruction": {
    "dynamic_route": "missing_DynamicIGDarkEnergyCoefficientPacket",
    "bare_theta_route": "missing_Branch2AConstraintTangentCertificate",
    "coefficient_status": "no_generated_Z_theta_C_Rtheta_xi_eff",
    "conservation_status": "no_total_current_proof_from_written_S_IG_dyn"
  },
  "constructive_next_computation": {
    "id": "Branch3LambdaPacket_V0",
    "must_emit": [
      "written_S_IG_dyn_or_parent_action",
      "source_EL_tuple",
      "theta_eff",
      "Noether_conservation_identity",
      "FLRW_scalar_survival_or_no_scalar_verdict",
      "Z_theta",
      "C_Rtheta",
      "xi_eff",
      "term_provenance_ledger",
      "rollback_conditions"
    ],
    "forbidden_inputs": [
      "bare_Lambda",
      "bare_Rtheta_insert",
      "fitted_xi_eff",
      "DESI_Rubin_target_window",
      "hidden_residual_relabeling"
    ]
  },
  "claim_status": {
    "GU_dark_energy_derived": false,
    "GU_Lambda_cancelled": false,
    "source_derived_dynamic_candidate_constructed": false,
    "certificate_shape_defined": true,
    "strongest_next_route_identified": true
  },
  "rollback_conditions": [
    "S_IG_dyn_absent_or_not_source_forced",
    "Z_U_or_V_target_selected",
    "theta_eff_not_conserved",
    "no_FLRW_scalar_mode",
    "Z_theta_nonpositive_unresolved",
    "C_Rtheta_inserted_by_hand",
    "xi_eff_fitted_after_target_data",
    "DESI_Rubin_target_used_upstream",
    "exact_GR_requires_hidden_dark_energy_residual",
    "bare_Lambda_inserted_as_source_derivation"
  ]
}
```

## Sources Read

- `RESEARCH-POSTURE.md`
- `process/runbooks/five-lane-frontier-run.md`
- `explorations/cycle-gates-and-audits/marble-wood-local-minimum-open-avenues-ledger-2026-06-24.md`
- `explorations/cycle-gates-and-audits/unified-marble-wood-source-closure-map-2026-06-24.md`
- `explorations/cycle-gates-and-audits/metric-marble-prematurity-gate-2026-06-24.md`
- `explorations/geometry-curvature-emergence/stress-energy-shadow-emergence-certificate-2026-06-24.md`
- `explorations/dark-energy-cosmology/flrw-theta-xi-branch-reduction-2026-06-24.md`
- `canon/dark-energy-theta-divergence-free.md`
- `canon/theta-field-flrw-dark-energy-eos.md`
- `explorations/misc/constraint-first-ig-tangent-space-gate-2026-06-24.md`
