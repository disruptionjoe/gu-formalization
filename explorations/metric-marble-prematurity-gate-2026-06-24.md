---
title: "Metric / Marble Prematurity Gate"
date: "2026-06-24"
status: exploration/gate
doc_type: metric_shadow_extraction_gate
verdict: "GATE_SPECIFIED; METRIC_AS_SHADOW_ALLOWED_ONLY_CONDITIONALLY; NOT_CERTIFIED"
owned_path: "explorations/metric-marble-prematurity-gate-2026-06-24.md"
audit_script: "tests/metric_marble_prematurity_audit.py"
depends_on:
  - "process/runbooks/five-lane-frontier-run.md"
  - "explorations/source-geometry-not-quantized-gravity-contract-2026-06-24.md"
  - "explorations/gr-shadow-recovery-certificate-2026-06-24.md"
  - "explorations/primary-gu-interface-contract-2026-06-24.md"
  - "explorations/exact-schwarzschild-kerr-el-gate-2026-06-24.md"
  - "explorations/gu-action-4d-physics-gate-2026-06-24.md"
  - "explorations/observer-finality-physical-forcing-gate-2026-06-24.md"
  - "explorations/quantum-gravity-reframing-no-go-map-2026-06-24.md"
---

# Metric / Marble Prematurity Gate

## 1. Verdict

The steelman is admissible as a gate, not as a completed result:

```text
Einstein's marble/wood complaint can be sharpened inside GU.
The 4D metric/geometric marble may itself be too early in the explanatory stack.
Here "marble" means the principled curvature/metric structure, especially `G_mu_nu[g]`.
The term `Lambda g_mu_nu` is treated separately as a geometric-side patch until its source
provenance is supplied. Both the marble side, the Lambda/dark-energy patch slot, and the
wood side, T_shadow, may have to be recovered or demoted as observer-facing shadows of a
deeper source geometry.
```

Current decision:

```text
METRIC-MARBLE-PREMATURITY:
  status: specified_open / not_final
  proof_grade: gate_specification
  metric-as-shadow: allowed only after explicit extraction
  current repo status: not certified
```

This gate does not say that GU has solved Einstein's complaint. It says only that GU may
legitimately refuse to make the 4D metric the first primitive, provided it then pays the
full extraction bill:

```text
source object
  -> section map
  -> induced observer metric
  -> induced variation space
  -> projected Einstein tensor
  -> covariance/invariance and causality/locality
  -> boundary data
  -> exact solution witnesses.
```

The current repo has the right schema language from the source-geometry and GR-shadow
contracts, but it does not yet contain the proof object that certifies the 4D metric or
Einstein tensor as derived shadows.

## 2. What "Marble Is Premature" Means And Does Not Mean

Plain English:

Einstein's complaint was that GR's curvature side looks like marble: clean geometry. The
right side looks like wood: phenomenological stress-energy added from outside. The
cosmological term `Lambda g_mu_nu` complicates the picture because it sits on the left but
can behave like a fixed patch rather than principled marble. The heterodox GU possibility
is stronger and riskier: perhaps even the marble is an observer-level material, and the
Lambda/dark-energy patch is either zero, imported, phenomenological, or dynamically
source-derived.
The metric, curvature, and Einstein tensor may be late, classical shadows of a source
geometry whose primitive data live before the 4D observer's split into geometry and matter.

Meaning:

- The 4D metric `g_mu_nu` is treated as an extracted field, normally `g = s^* g_Y`, not as
  the first fundamental GU input.
- The Einstein tensor `G[g]` is treated as a projected diagnostic of the source
  Euler-Lagrange tuple, not as the starting equation of motion.
- `Lambda_eff g_mu_nu` is not treated as automatic marble. It needs a
  `LambdaDarkEnergyProvenanceCertificate` if claimed as source-derived.
- Matter/stress-energy on the right side must also be a shadow, a controlled import, or a
  named failure. Hiding source residuals inside `T_mu_nu` is not allowed.
- The marble/wood split becomes a downstream observer split. It is recovered only if the
  same source branch derives the metric side, the source side, conservation, and boundary
  data.

Does not mean:

- It does not mean GR is false, optional, or merely aesthetic.
- It does not mean 4D covariance, causality, locality, and exact black-hole recovery can be
  weakened.
- It does not mean the Einstein-Hilbert action may be inserted as a rescue while still
  claiming metric-as-shadow.
- It does not mean a bare `Lambda`, fitted `xi_eff`, or dark-energy fluid may be inserted
  as a source-derived geometric term.
- It does not mean a weak-field `O(M/r)` pass is an exact GR pass.
- It does not mean source geometry automatically solves QFT recovery, measurement, anomaly
  compatibility, or the Standard Model finite-control problem.
- It does not mean the current repo has proved metric-as-shadow. It has not.

Allowed current citation:

```text
GU may keep open the possibility that the 4D metric and Einstein tensor are
observer-facing shadows of source geometry. This is a gate and research posture,
not a certified recovery theorem.
```

Forbidden current citation:

```text
GU has shown that the metric is only a shadow.
GU solves Einstein's marble/wood problem by making marble and wood emergent.
Weak-field Schwarzschild proves the metric shadow.
```

## 3. Required Metric-Shadow Extraction Gate

Metric-as-shadow passes only if one branch supplies every stage below. Missing any stage
leaves the claim at `specified_open` or demotes it to `import`.

### 3.1 Source Object

The source object must be fixed before target metrics are named:

```text
G_src =
  (Y, g_Y, P, S, A, D_GU, S_GU,
   IG_data, section_space, variation_space,
   boundary_data, observer_access, reduction_rules).
```

Minimum required fields:

```text
X, Y = Met_Lor(X), g_Y, P -> Y, Sp(64), S, Phi_2,
s, A, F_A, epsilon, beta or U, theta, Psi,
B_s = II_s^H, j_s, branch key.
```

The source action/operator must be source-closed. Cross terms, potentials, `R theta^2`,
bare `Lambda`, and Einstein-Hilbert sectors are not allowed as rescue knobs unless they are
primary-sourced with fixed coefficients before the GR target is tested.

If a Lambda/dark-energy term is claimed, this gate requires:

```text
Lambda_eff status:
  zero,
  imported constant,
  phenomenological control,
  or source-derived dynamic term.

Source-derived requires:
  same branch-fixed S_GU/D_GU,
  generated coefficients such as Z_theta, C_Rtheta, or xi_eff,
  no DESI/Rubin target input during derivation,
  conservation and exact-GR compatibility.
```

### 3.2 Section Map

The metric extraction map must be explicit:

```text
s: X -> Y
s^*: fields on Y -> observer fields on X
```

with at least:

```text
g = s^* g_Y
P_s = s^* P
A_s = s^* A
theta_s = s^* theta
Psi_s = s^* Psi, when used
B_s = II_s^H.
```

The section cannot be picked merely because it gives Schwarzschild, Kerr, FLRW, or another
desired metric. It must be admitted by the same branch's source equations and boundary
conditions.

### 3.3 Induced Metric

The observer metric must be an output:

```text
g_shadow = s^* g_Y,
signature(g_shadow) = Lorentzian in the claimed observer regime,
metric constants and normalizations inherited from source data.
```

The pass condition is:

```text
metric_imported = false
metric_is_induced_by_section = true
metric_variations_are_induced_from_source = true
```

The fail condition is:

```text
g_mu_nu is supplied as an independent 4D GR metric,
or varied by an independent Einstein-Hilbert principle,
or selected from a target solution before the source branch is solved.
```

### 3.4 Variation Space

The allowed variations must be branch-fixed:

```text
delta s, delta A, delta Psi,
delta epsilon and delta beta or delta U/P_IG according to the branch,
delta lambda in constrained branches.
```

The 4D metric variation must be the image of source variations:

```text
delta g = D(s^* g_Y)[delta s, delta source data],
not an independent arbitrary delta g used to import the Einstein equation.
```

The IG rule is load-bearing:

```text
free beta + only |theta|^2  =>  theta = 0.
```

Therefore a branch cannot claim nonzero theta, a bare source law, or theta dark energy if
its actual variation space contains free `beta` with only the theta norm.

### 3.5 Projected Einstein Tensor

The source Euler-Lagrange tuple must be derived first:

```text
E_s = 0
E_A = 0
E_IG = 0
E_Psi = 0
E_lambda = 0, when constrained.
```

Only then may the 4D projection be formed:

```text
Pi_4D(E_s, E_A, E_IG, E_Psi)
  =
  G_mu_nu[g]
  + Lambda_eff g_mu_nu
  - kappa_eff T_mu_nu^shadow
  - R_mu_nu^shadow
  = 0.
```

For an exact GR-shadow claim:

```text
R_mu_nu^shadow = 0
```

in the declared regime. If residuals remain, they must be named as controlled modified
gravity predictions or as failures. They may not be moved to the wood side as hidden
matter.

The Einstein tensor is allowed here as a projected observer tensor. It is not allowed as
the unearned primary marble of the branch.

### 3.6 Covariance, Invariance, Causality, And Locality

The extraction must respect:

```text
4D diffeomorphism covariance of the observer metric,
Sp(64) gauge equivariance of source fields and constraints,
section-gauge compatibility,
normalization invariance for j_s and II_s^H,
branch-specific Noether/Bianchi identities.
```

The projected conservation law must be derived:

```text
source Noether/Bianchi identity
  -> nabla^mu T_mu_nu^shadow = 0
```

or replaced by an explicitly stated conserved total current in Branch 3 language.

Causality/locality obligations are not optional. The induced observer light cones must be
well-defined in the claimed regime, local source data must determine local observer data up
to the stated gauge/diffeomorphism equivalence, and the branch must not introduce
spacelike/acausal characteristic behavior into the observer shadow.

### 3.7 Boundary Data

The branch must state domain and boundary data before the exact solution test:

```text
Schwarzschild exterior domain r > 2M,
Kerr exterior domain with |a| < M,
ADM mass and Kerr angular momentum,
finite gauge/action boundary data,
section boundary variations,
asymptotic Lambda sector if nonzero,
matter boundary data if matter is claimed.
```

Constants such as `G_N`, `Lambda_eff`, `kappa_eff`, `Z_theta`, and any source-to-matter
normalization must be inherited from the source branch, not fitted after the target
solution is selected.

### 3.8 Exact Solutions

The exact vacuum witnesses are:

```text
(s_BH, A_BH, epsilon_BH, beta_BH or U_BH, lambda_BH if needed, Psi_BH = 0)
```

such that:

```text
s_BH^* g_Y = g_BH up to diffeomorphism/gauge
g_BH in {Schwarzschild(M), Kerr(M,a)}
T_matter = 0
Lambda = 0 unless an explicit asymptotic Lambda branch is stated
finite action and finite boundary data
E_s = E_A = E_IG = E_Psi = 0
R_mu_nu^shadow = 0.
```

Exact Schwarzschild alone is not enough. Kerr is a separate rotating, non-conformally-flat
test. Weak-field Schwarzschild remains valuable, but it is downstream and bounded:

```text
O(M/r) compatibility != exact metric-shadow recovery.
```

## 4. Failure Modes

| failure mode | symptom | decision | rollback |
|---|---|---|---|
| Metric imported | `g_mu_nu` is supplied as an independent 4D metric, or the section is chosen only because it hits a target metric. | `import`, not metric shadow | Demote to GR-compatible ansatz or ordinary metric-first branch. |
| Einstein-Hilbert inserted as rescue | A 4D `int sqrt(-g) R[g]` term is added after the source branch fails. | `rescue_import` | Treat as a different metric-first theory unless the term is primary-sourced before targets. |
| Bare Lambda counted as marble | `Lambda g_mu_nu`, fitted `xi_eff`, or a dark-energy fluid is inserted because the cosmology target needs it. | `patch_import_or_target_fit` | Demote to patch/import/phenomenological control until `LambdaDarkEnergyProvenanceCertificate(branch)` closes. |
| Weak field promoted to exact | `R_fail = 0 at O(M/r)` is cited as exact Schwarzschild/Kerr recovery. | `overclaim` | Keep only bounded weak-field compatibility. |
| Hidden matter relabeling | `Q^TF(B_s)`, gauge residuals, multiplier currents, or section residuals are moved to `T_mu_nu` in a vacuum test. | `fail_vacuum_shadow` | Name the residual as modified gravity or fail exact vacuum GR for that branch. |
| Causality loss | The source/operator branch gives acausal observer characteristics or ill-defined light cones. | `fail_physical_shadow` | Roll back metric-as-shadow and VZ/observer citations for that branch. |
| Covariance/invariance loss | The extraction depends on gauge fixing, section coordinates, or non-equivariant constraints. | `fail_extraction` | Rebuild the map equivariantly or demote to gauge-fixed control. |
| Target-fitted branch | `Phi`, cross terms, potentials, or constants are chosen because Schwarzschild, Kerr, `xi_eff`, or `n=3` need them. | `target_inserted` | Demote to phenomenological target search. |

## 5. Branch Robustness And Rollback Table

| branch/object | metric-shadow status | robustness | rollback trigger | allowed citation after rollback |
|---|---|---|---|---|
| Source-geometry primary | `specified_open` | Best steelman posture if `G_src` and extraction maps are explicit. | No source-closed action/operator or no reduction map. | Interface program only. |
| Branch 2A constrained IG | `candidate` | Strongest conservative route for bare `D_A^*F_A = theta` if `Phi(epsilon,beta,s)` and `D_A Phi = 0` are derived. | `Phi` missing, A-dependent, non-covariant, or target-fitted; tangent space still contains all beta variations. | Branch underdefined; no bare-source metric shadow. |
| Branch 2B constrained IG | `candidate_corrected_source` | May keep nonzero theta with multiplier current. | Prose continues to cite bare theta source after `(D_A Phi)^*lambda` enters. | Corrected-source branch only. |
| Branch 3 dynamical IG | `candidate_total_current` | Honest fallback if `S_IG-dyn` is written and conserved total current is derived. | `S_IG-dyn` absent or `theta_eff` not used in source law. | Total-current proposal only. |
| Background/Stueckelberg | `thin_candidate` | Allows nonzero theta as spurion/background. | Noether cost or omitted variations invalidate projected conservation. | Spurion control, not full metric shadow. |
| Operator spine only | `insufficient` | Types principal-symbol/VZ questions if primary `D_GU` contains the load-bearing block. | Used to claim exact GR without an action and section EL tuple. | Operator control only. |
| Willmore-only section action | `branch_fail_for_exact_GR` | Useful negative control. | Exact Schwarzschild/Kerr claimed without coupled cancellations. | Weak-field/control language only. |
| Bare free-beta theta norm | `rejected_for_nonzero_theta` | Negative result is robust: free beta kills theta. | Nonzero theta, theta dark energy, or bare source law is cited anyway. | Reject nonzero-theta branch. |
| Metric-first GR comparison | `comparison_import` | Useful benchmark and observer target. | Treated as GU derivation rather than comparison. | External GR target/control. |

Robust conclusion:

```text
Metric-as-shadow is not robustly proved in any current branch.
The robust positive result is only permission to ask the question.
The robust negative controls are:
  free beta kills nonzero theta;
  Willmore-only exact black-hole recovery fails;
  weak-field recovery is not exact recovery.
```

## 6. Claim Certificate Table

| claim | current status / proof grade | dependencies | forbidden inputs | closure condition | rollback condition | exact citation language |
|---|---|---|---|---|---|---|
| `MARBLE-PREMATURITY` | `specified_open` / `gate_specification` | Source-geometry contract; GR-shadow schema; primary interface; exact-GR gate. | "GR is false"; "metric irrelevant"; "source geometry solves physics by name." | A branch-fixed source object and extraction certificate exist. | Used as a proof instead of a gate. | "The 4D metric may be too early in GU's explanatory stack; this is an open gate, not a certified result." |
| `METRIC-AS-SHADOW` | `not_certified` / `missing_extraction_theorem` | Source object, section map, induced metric, induced variation, projected Einstein tensor, invariance, boundary data, exact witnesses. | Imported metric; independent 4D Einstein-Hilbert rescue; target-fitted section. | `MetricShadowExtractionTheorem(branch)` closes. | Any gate stage missing or imported. | "Metric-as-shadow is allowed only conditionally; the current repo has not proved it." |
| `PROJECTED-EINSTEIN-TENSOR` | `blocked` / `projection_open` | Full source EL tuple; `Pi_4D`; conservation; fixed constants; no hidden residuals. | Starting from `G[g]` as the primary GU equation; moving residuals to matter. | Projection identity gives `G + Lambda g - kappa T_shadow - R_shadow = 0` with controlled `R_shadow`. | Projection requires independent `delta g` or hidden matter. | "The Einstein tensor may be used as an observer projection only after the source EL tuple is derived." |
| `LAMBDA-PATCH` | `open_patch_slot` / `missing_provenance_certificate` | Branch-fixed source action/operator; generated coefficient; conservation; exact-GR compatibility; DESI/Rubin anti-fitting test. | Bare `Lambda`; fitted `xi_eff`; target-tuned fluid or potential; moving residuals into `Lambda_eff`. | `LambdaDarkEnergyProvenanceCertificate(branch)` identifies the term as zero, import, control, or source-derived dynamic output. | Coefficient is inserted, fitted after target data, or not generated by the cited branch. | "`Lambda g_mu_nu` is a patch slot, not automatic marble; source derivation remains open." |
| `GR-RECOVERY` | `still_owed` / `specification_open` | Written `S_GU`; fixed IG branch; full EL tuple; exact Schwarzschild/Kerr; weak-field/macroscopic limits from the same branch. | Weak-field as exact; Kerr by spherical analogy; Willmore-only recovery. | Schwarzschild and Kerr witnesses satisfy the full vacuum source tuple. | Either exact witness fails or cancellation uses target-fitted terms. | "Exact GR recovery remains open; weak-field compatibility does not certify metric-as-shadow." |
| `MARBLE-AND-WOOD-SHADOWS` | `allowed_as_steelman` / `not_final` | Metric shadow plus derived `T_shadow`, source conservation, matter/SM/QFT certificates when claimed. | Hidden matter relabeling; stress-energy imported without provenance. | Both left and right observer sides are recovered from one source branch. | Wood side is imported or used to absorb unexplained source residuals. | "GU may seek a source geometry whose observer projection yields both geometry and stress-energy; this has not been shown." |
| `CAUSAL-LOCAL-SHADOW` | `owed` / `physical_consistency_gate` | Covariant extraction, local dependence, well-defined light cones, no acausal characteristics, observer-finality measurement bridge when quantum claims are made. | Ignoring causality because the metric is emergent; observer language as physics escape. | Causality/locality or a precise replacement condition is derived for the shadow. | Acausal characteristics or nonlocal uncontrolled projection. | "Metric prematurity does not weaken causality or locality obligations." |

## 7. First Exact Missing Proof Object

The first exact missing proof object is:

```text
MetricShadowExtractionTheorem(branch)
```

Required input:

```text
branch_fixed_S_GU_or_operator_action_pair
branch_fixed_variation_space
section_space and section boundary data
IG source rule or total-current rule
g_Y, j_s, II_s^H normalizations
source covariance/gauge invariance data
causality/locality hypothesis
```

Required output:

```text
1. Source EL tuple:
   E_s = E_A = E_IG = E_Psi = 0.

2. Section extraction:
   g = s^* g_Y and observer fields are derived from source data.

3. Induced variation theorem:
   admissible delta g are exactly the image of allowed source variations in the
   claimed regime, or the missing directions are named in a loss ledger.

4. Projection identity:
   Pi_4D(E_source)
     = G[g] + Lambda_eff g - kappa_eff T_shadow - R_shadow.

5. Invariance and conservation:
   source gauge/diffeomorphism invariance projects to observer covariance and
   a branch-specific conserved stress/source law.

6. Causality/locality theorem:
   observer light cones and local propagation are well-defined, or deviations are
   explicitly bounded and named.

7. Exact witnesses:
   Schwarzschild and Kerr source-field witnesses solve the full vacuum tuple with
   finite boundary data and R_shadow = 0.
```

Relation to the existing GR-shadow file:

```text
MetricShadowExtractionTheorem(branch)
  contains the metric-prematurity part.
ELProjectedGRShadowTheorem(branch)
  is its exact-GR specialization and first child blocker.
```

Until this object exists, "marble is premature" is a disciplined research gate, not a
claim about completed GU physics.

## 8. Machine-Readable Summary

```json
{
  "artifact": "METRIC_MARBLE_PREMATURITY_GATE",
  "version": "2026-06-24",
  "verdict": "GATE_SPECIFIED_METRIC_AS_SHADOW_CONDITIONAL_NOT_CERTIFIED",
  "current_status": "specified_open_not_final",
  "metric_shadow_proven": false,
  "core_interpretation": "Einstein_marble_and_wood_may_both_be_observer_shadows_of_source_geometry",
  "allowed_citation": "GU may keep open the possibility that the 4D metric and Einstein tensor are observer-facing shadows of source geometry; this is a gate, not a certified recovery theorem.",
  "required_gate_stages": [
    {
      "stage": "source_object",
      "required": [
        "G_src",
        "S_GU_or_operator_action_pair",
        "D_GU",
        "IG_data",
        "section_space",
        "variation_space",
        "boundary_data"
      ],
      "current_status": "underdefined"
    },
    {
      "stage": "section_map",
      "required": [
        "s_X_to_Y",
        "s_star_fields",
        "section_admitted_by_source_EL",
        "no_target_selected_section"
      ],
      "current_status": "typed_schema_only"
    },
    {
      "stage": "induced_metric",
      "required": [
        "g_equals_s_star_g_Y",
        "lorentzian_observer_regime",
        "constants_from_source",
        "metric_imported_false"
      ],
      "current_status": "not_certified"
    },
    {
      "stage": "variation_space",
      "required": [
        "delta_g_induced_from_source",
        "branch_fixed_delta_epsilon_beta_or_U",
        "free_beta_theta_collapse_handled",
        "loss_ledger"
      ],
      "current_status": "branch_dependent_open"
    },
    {
      "stage": "projected_einstein_tensor",
      "required": [
        "full_source_EL_tuple",
        "Pi_4D_projection",
        "G_plus_Lambda_minus_kappa_T_minus_R_shadow",
        "Lambda_eff_zero_imported_control_or_source_derived",
        "R_shadow_control"
      ],
      "current_status": "blocked_missing_projection_theorem"
    },
    {
      "stage": "covariance_invariance",
      "required": [
        "4D_diffeomorphism_covariance",
        "Sp64_gauge_equivariance",
        "Noether_Bianchi_projection",
        "j_s_II_s_H_normalization_invariance"
      ],
      "current_status": "owed"
    },
    {
      "stage": "causality_locality",
      "required": [
        "well_defined_observer_light_cones",
        "local_source_to_observer_dependence",
        "no_acausal_characteristics",
        "replacement_condition_if_nonstandard"
      ],
      "current_status": "owed"
    },
    {
      "stage": "boundary_data",
      "required": [
        "Schwarzschild_domain",
        "Kerr_domain",
        "ADM_mass",
        "Kerr_angular_momentum",
        "finite_action_gauge_boundary_data"
      ],
      "current_status": "not_instantiated"
    },
    {
      "stage": "exact_solutions",
      "required": [
        "exact_Schwarzschild_witness",
        "exact_Kerr_witness",
        "full_vacuum_EL_tuple_zero",
        "R_shadow_zero",
        "no_hidden_matter"
      ],
      "current_status": "not_passed"
    }
  ],
  "failure_modes": [
    {
      "id": "metric_imported",
      "decision": "import_not_shadow",
      "rollback": "demote_to_GR_compatible_ansatz_or_metric_first_branch"
    },
    {
      "id": "EH_inserted_as_rescue",
      "decision": "rescue_import",
      "rollback": "treat_as_different_metric_first_theory_unless_primary_sourced"
    },
    {
      "id": "bare_Lambda_counted_as_marble",
      "decision": "patch_import_or_target_fit",
      "rollback": "demote_to_patch_import_or_phenomenological_control_until_LambdaDarkEnergyProvenanceCertificate_closes"
    },
    {
      "id": "weak_field_promoted_to_exact",
      "decision": "overclaim",
      "rollback": "keep_only_bounded_weak_field_compatibility"
    },
    {
      "id": "hidden_matter_relabeling",
      "decision": "fail_vacuum_shadow",
      "rollback": "name_modified_gravity_residual_or_fail_exact_vacuum_GR"
    },
    {
      "id": "causality_loss",
      "decision": "fail_physical_shadow",
      "rollback": "roll_back_metric_shadow_and_dependent_physical_claims"
    },
    {
      "id": "covariance_invariance_loss",
      "decision": "fail_extraction",
      "rollback": "demote_to_gauge_fixed_control"
    },
    {
      "id": "target_fitted_branch",
      "decision": "target_inserted",
      "rollback": "demote_to_phenomenological_target_search"
    }
  ],
  "branches": [
    {
      "id": "source_geometry_primary",
      "metric_shadow_status": "specified_open",
      "rollback_trigger": "no_source_closed_action_operator_or_reduction_map"
    },
    {
      "id": "branch_2a_constrained_ig",
      "metric_shadow_status": "candidate_underdefined",
      "rollback_trigger": "Phi_missing_A_dependent_non_covariant_or_target_fitted"
    },
    {
      "id": "branch_2b_constrained_ig",
      "metric_shadow_status": "candidate_corrected_source",
      "rollback_trigger": "bare_theta_source_claimed_despite_multiplier_current"
    },
    {
      "id": "branch_3_dynamical_ig",
      "metric_shadow_status": "candidate_total_current",
      "rollback_trigger": "S_IG_dyn_absent_or_theta_eff_not_used"
    },
    {
      "id": "background_stueckelberg",
      "metric_shadow_status": "thin_candidate",
      "rollback_trigger": "Noether_cost_or_omitted_variations_break_conservation"
    },
    {
      "id": "operator_spine_only",
      "metric_shadow_status": "insufficient",
      "rollback_trigger": "used_for_exact_GR_without_action_section_EL"
    },
    {
      "id": "willmore_only",
      "metric_shadow_status": "branch_fail_for_exact_GR",
      "rollback_trigger": "exact_black_hole_claim_without_full_coupled_EL"
    },
    {
      "id": "bare_free_beta_theta_norm",
      "metric_shadow_status": "rejected_for_nonzero_theta",
      "rollback_trigger": "nonzero_theta_or_bare_source_claimed"
    }
  ],
  "claim_certificates": [
    {
      "id": "MARBLE-PREMATURITY",
      "status": "specified_open",
      "proof_grade": "gate_specification",
      "forbidden_inputs": [
        "GR_false",
        "metric_irrelevant",
        "source_geometry_by_name_only"
      ],
      "rollback_condition": "used_as_proof_instead_of_gate"
    },
    {
      "id": "METRIC-AS-SHADOW",
      "status": "not_certified",
      "proof_grade": "missing_extraction_theorem",
      "forbidden_inputs": [
        "imported_metric",
        "independent_Einstein_Hilbert_rescue",
        "target_fitted_section"
      ],
      "rollback_condition": "any_gate_stage_missing_or_imported"
    },
    {
      "id": "PROJECTED-EINSTEIN-TENSOR",
      "status": "blocked",
      "proof_grade": "projection_open",
      "forbidden_inputs": [
        "G_g_as_primary_GU_equation",
        "hidden_residuals_moved_to_matter"
      ],
      "rollback_condition": "projection_requires_independent_delta_g_or_hidden_matter"
    },
    {
      "id": "LAMBDA-PATCH",
      "status": "open_patch_slot",
      "proof_grade": "missing_provenance_certificate",
      "forbidden_inputs": [
        "bare_Lambda",
        "fitted_xi_eff",
        "target_tuned_dark_energy_fluid_or_potential",
        "residuals_moved_to_Lambda_eff"
      ],
      "rollback_condition": "coefficient_inserted_fitted_after_target_data_or_not_generated_by_cited_branch"
    },
    {
      "id": "GR-RECOVERY",
      "status": "still_owed",
      "proof_grade": "specification_open",
      "forbidden_inputs": [
        "weak_field_as_exact",
        "Kerr_by_spherical_analogy",
        "Willmore_only_recovery"
      ],
      "rollback_condition": "Schwarzschild_or_Kerr_witness_fails_full_vacuum_tuple"
    },
    {
      "id": "MARBLE-AND-WOOD-SHADOWS",
      "status": "allowed_as_steelman_not_final",
      "proof_grade": "not_final",
      "forbidden_inputs": [
        "hidden_matter_relabeling",
        "stress_energy_import_without_provenance"
      ],
      "rollback_condition": "wood_side_imported_or_absorbs_unexplained_residuals"
    },
    {
      "id": "CAUSAL-LOCAL-SHADOW",
      "status": "owed",
      "proof_grade": "physical_consistency_gate",
      "forbidden_inputs": [
        "emergence_used_to_ignore_causality",
        "observer_language_as_physics_escape"
      ],
      "rollback_condition": "acausal_characteristics_or_uncontrolled_nonlocal_projection"
    }
  ],
  "forbidden_claims": [
    "metric_shadow_already_proven",
    "GU_solves_marble_wood_problem",
    "weak_field_Schwarzschild_proves_metric_shadow",
    "Einstein_Hilbert_rescue_counts_as_shadow",
    "bare_Lambda_counts_as_principled_marble",
    "fitted_xi_eff_counts_as_source_derived_dark_energy",
    "hidden_matter_counts_as_vacuum_GR",
    "emergent_metric_weakens_causality"
  ],
  "rollback_conditions": [
    "metric_imported",
    "Einstein_Hilbert_inserted_as_rescue",
    "bare_Lambda_or_fitted_xi_eff_inserted_as_marble",
    "weak_field_promoted_to_exact",
    "hidden_matter_required",
    "covariance_or_invariance_loss",
    "causality_or_locality_loss",
    "Schwarzschild_or_Kerr_full_EL_failure",
    "branch_2a_Phi_missing_or_target_fitted",
    "branch_3_total_current_not_used",
    "bare_free_beta_nonzero_theta_claimed"
  ],
  "first_missing_proof_object": {
    "id": "MetricShadowExtractionTheorem",
    "child_blocker": "ELProjectedGRShadowTheorem",
    "requires": [
      "branch_fixed_S_GU_or_operator_action_pair",
      "branch_fixed_variation_space",
      "section_extraction",
      "induced_metric_and_variation",
      "Pi_4D_projection_identity",
      "LambdaDarkEnergyProvenanceCertificate_if_nonzero_Lambda_eff_claimed",
      "covariance_invariance_conservation",
      "causality_locality_theorem",
      "Schwarzschild_and_Kerr_witness_fields"
    ]
  },
  "next_step": "attempt_branch_2a_metric_shadow_extraction_for_exact_Schwarzschild_then_Kerr_or_switch_to_branch_3_total_current"
}
```

## 9. Next Meaningful Proof/Computation Step

Do one branch-fixed extraction attempt:

```text
Attempt MetricShadowExtractionTheorem for Branch 2A on exact Schwarzschild.
```

Minimum packet:

1. Derive or reject an A-independent, gauge-equivariant
   `Phi(epsilon,beta,s)=0` whose tangent space does not contain all beta variations.
2. If Branch 2A survives, write the full Branch 2A source tuple and the induced metric
   variation map `delta source -> delta g`.
3. Compute the projected section equation and identify the exact term whose projection is
   `G[g]`.
4. Test exact Schwarzschild with finite boundary data. Do not use the weak-field pass as a
   substitute.
5. If Schwarzschild passes, test Kerr with angular-momentum boundary data.
6. If Branch 2A cannot be sourced, switch explicitly to Branch 3 and rewrite all source
   language in terms of `theta_eff` and a conserved total current.

This is the first step that can decide whether metric/geometric marble is genuinely late
in GU, or whether the project must fall back to a metric-first import for the GR sector.

## Sources Read

- `process/runbooks/five-lane-frontier-run.md`
- `explorations/source-geometry-not-quantized-gravity-contract-2026-06-24.md`
- `explorations/gr-shadow-recovery-certificate-2026-06-24.md`
- `explorations/primary-gu-interface-contract-2026-06-24.md`
- `explorations/exact-schwarzschild-kerr-el-gate-2026-06-24.md`
- `explorations/gu-action-4d-physics-gate-2026-06-24.md`
- `explorations/observer-finality-physical-forcing-gate-2026-06-24.md`
- `explorations/quantum-gravity-reframing-no-go-map-2026-06-24.md`
