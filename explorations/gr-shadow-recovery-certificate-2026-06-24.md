---
title: "GR Shadow Recovery Certificate"
date: "2026-06-24"
status: exploration/certificate
doc_type: gr_shadow_recovery_certificate
verdict: "CERTIFICATE_SPECIFIED; TRUE_GR_SHADOW_NOT_CURRENTLY_CERTIFIED"
owned_path: "explorations/gr-shadow-recovery-certificate-2026-06-24.md"
audit_script: "tests/gr_shadow_recovery_certificate_audit.py"
depends_on:
  - "explorations/primary-gu-interface-contract-2026-06-24.md"
  - "explorations/constraint-first-ig-tangent-space-gate-2026-06-24.md"
  - "explorations/exact-schwarzschild-kerr-el-gate-2026-06-24.md"
  - "explorations/gu-action-4d-physics-gate-2026-06-24.md"
  - "explorations/gu-minimal-action-spec-2026-06-24.md"
  - "explorations/gu-closed-loop-action-ig-branch-2026-06-24.md"
  - "canon/schwarzschild-weak-field-rfail.md"
  - "explorations/live-claim-dag-fault-finality-ledger-2026-06-24.md"
---

# GR Shadow Recovery Certificate

## 1. Verdict

The steelman premise is admissible but not yet certified:

```text
GU need not quantize the 4D GR metric as a fundamental field.
It may instead recover GR as an observer-facing shadow of source geometry.
```

However, the current repo does not yet contain the certificate that would make that
recovery decision-grade. The right current status is:

```text
GR-SHADOW:
  specified_open / not_final
  certificate schema written here
  no current true GR shadow certificate

ACTION-GR:
  open / specification / not_final
  exact Schwarzschild/Kerr not passed

Weak-field Schwarzschild:
  conditionally resolved inside the canon's O(M/r) scope
  not an exact nonlinear GR recovery
```

A true GR shadow is stronger than "the induced metric looks GR-like in one limit." It
requires a fixed source-geometry variational principle whose extracted observer metric
satisfies the projected 4D Einstein equations, with derived conservation and exact
solution witnesses, without making the GR metric the fundamental quantized object.

Current blocking facts:

- The full `S_GU` and IG variation branch are not closed.
- Free `beta` with only the theta norm forces `theta = 0`.
- Branch 2A is the strongest conservative route, but its constraint
  `Phi(eps,beta,s)=0` has not been derived.
- Willmore-only exact Schwarzschild fails; Kerr remains at least equally dangerous.
- The weak-field canon is a bounded leading-order compatibility result, not an exact
  GR-shadow theorem.

## 2. Certificate Schema

Define:

```text
GRShadowRecoveryCertificate =
  source field content
  -> section/metric extraction
  -> 4D Euler-Lagrange projection
  -> conservation/source law
  -> exact solution tests
  -> weak-field and macroscopic limit.
```

The certificate is valid only when all six stages are supplied in one branch, with the
same fields, same normalizations, same variation rules, and no target-fitted terms.

### 2.1 Source Field Content

The source theory must state the source fields before any GR target is tested:

```text
X                         smooth oriented 4-manifold
Y = Met_Lor(X)             14D metric bundle over X
g_Y                       fixed gimmel metric in the current baseline
P -> Y                    principal Sp(64)-bundle
S                         quaternionic spinor bundle
Phi_2                     fixed algebraic shiab map
s: X -> Y                  section; observer metric is g = s^*g_Y
A                         Sp(64) connection on P
F_A                       curvature of A
eps                       IG/gauge variable
beta or U                 IG translation/dynamical field
theta                     A - Gamma(eps) - Ad(eps^-1) beta
Psi                       spinor/form-spinor field
B_s                       II_s^H, horizontal-normalized section second fundamental form
j_s                       normal-to-ad(P_s) soldering normalization
branch                    background, constrained IG, dynamical IG, or rejected free beta
```

Required decisions:

| item | certificate requirement | current status |
|---|---|---|
| `D_GU` | primary-sourced operator, not just a typed proposal | typed proposal only for relevant spine |
| `S_GU` | written action with signs, coefficients, and boundary terms | open specification |
| IG variation | background, Branch 2A/2B constraint, or Branch 3 dynamics | blocked; 2A not derived |
| source fields | fixed before target metrics are named | partially typed |
| cross terms | primary-sourced with fixed coefficients | absent in baseline; not allowed as rescue knobs |

### 2.2 Section / Metric Extraction

The observer metric must be an output:

```text
g = s^* g_Y.
```

The certificate must show that the extracted metric is not varied as a fundamental
quantized GR metric. Its variations are induced by the source-theory variation of `s`
and any source fields that enter the section geometry. The extraction map must also
produce the observer-facing fields:

```text
A_s       = s^* A
theta_s   = s^* theta
Psi_s     = s^* Psi, when a 4D spinor shadow is used
B_s       = II_s^H
j_s(B_s)  = soldered normal/ad(P_s) source data
```

The extraction passes only if:

```text
metric_is_shadow = true
section_variation_is_part_of_source_EL = true
all 4D constants and normalizations are inherited from source data
```

It fails if the 4D Einstein-Hilbert action, a bare 4D cosmological constant, or the target
GR metric is inserted as an independent fundamental sector merely to recover GR.

### 2.3 4D Euler-Lagrange Projection

The full source EL tuple must be derived first:

```text
E_s = 0
E_A = 0
E_eps = 0
E_beta or E_U/P = 0
E_Psi = 0
E_lambda = 0          only in constrained branches
```

Only then may it be projected to an observer-facing equation on `X`:

```text
Pi_4D(E_s,E_A,E_IG,E_Psi) =
  G_mu nu[g]
  + Lambda_eff g_mu nu
  - kappa_eff T_mu nu^shadow
  - R_mu nu^shadow
  = 0.
```

For an exact GR shadow:

```text
R_mu nu^shadow = 0
```

for the declared regime, or it must be a controlled correction outside the claim. The
certificate must specify:

```text
kappa_eff,
Lambda_eff,
T_mu nu^shadow,
boundary terms,
normalization of j_s and II_s^H,
whether theta_s is scalar, vector, tensor, or constrained in the regime.
```

This projection is the central proof object. A Gauss identity, a weak-field cancellation,
or a known 4D GR solution is not enough unless it is tied to the full source EL tuple.

### 2.4 Conservation / Source Law

The source law must be branch-specific:

| branch type | admissible source law | conservation burden |
|---|---|---|
| Background/Stueckelberg | `D_A^*F_A = theta` may survive after normalization | Noether identity must account for omitted background variations |
| Branch 2A | `D_A^*F_A = theta` if `D_A Phi = 0` | prove `Phi` and projected conservation |
| Branch 2B | corrected source with `(D_A Phi)^*lambda` | conserve total corrected current |
| Branch 3 | `D_A^*F_A = theta_eff` | conserve total IG current, not bare theta |
| Free beta | collapses to `theta = 0` and `D_A^*F_A = 0` | cannot support nonzero theta shadow |

The certificate must derive, not assume:

```text
nabla^mu T_mu nu^shadow = 0
```

as the 4D image of the full source Noether/Bianchi identities. It is forbidden to rely on
an unproved identity such as a generic `D_A^*D_A^*F_A = 0`, and it is forbidden to move
unexplained residuals to the right-hand side as "matter."

### 2.5 Exact Solution Tests

The exact vacuum tests are:

```text
Schwarzschild(M) on r > 2M
Kerr(M,a) on the exterior domain with |a| < M
```

For each metric, the certificate must provide witness fields:

```text
(s_BH, A_BH, eps_BH, beta_BH or U_BH, lambda_BH if needed, Psi_BH = 0)
```

such that:

```text
s_BH^* g_Y = g_BH              up to diffeomorphism/gauge
T_matter = 0
Lambda = 0                    unless an explicit asymptotic Lambda branch is stated
finite action / finite gauge boundary data
E_s = E_A = E_IG = E_Psi = 0
```

Exact Schwarzschild alone is not enough; Kerr is a separate rotating, non-conformally-flat
test. Passing weak-field Schwarzschild does not pass either exact test.

### 2.6 Weak-Field And Macroscopic Limit

The weak-field gate must be downstream of the exact/source certificate, not a replacement
for it:

```text
g = eta + h,  |h| ~ M/r
R_fail^full = 0 at O(M/r)          canon, bounded scope
PPN/solar-system corrections       derived from the same source branch
```

The macroscopic limit must state how observer GR emerges at large scales:

```text
coarse source state or classical source configuration
  -> stable section s
  -> extracted metric g
  -> suppressed non-GR residual R_shadow
  -> fixed G_N, Lambda_eff, and matter/source coupling
```

Minimum macroscopic requirements:

- `G_N` and `Lambda_eff` are fixed by source geometry and normalization, not fitted after
  the fact.
- Section fluctuations or quantum/source-geometric noise are small enough that `g` is a
  classical observer metric in the regime claimed.
- PPN, gravitational radiation, and cosmological backgrounds are controlled by the same
  branch that passed the exact-solution test.
- Any deviations from GR are named as predictions, not hidden in "shadow" language.

## 3. Current Evidence And Missing Pieces

| certificate stage | current evidence | missing piece | decision |
|---|---|---|---|
| Source field content | typed interface lists `X,Y,g_Y,P,S,A,eps,beta,theta,Psi,s,B_s` | primary-sourced closed `D_GU` and `S_GU` | partial |
| Section extraction | `g=s^*g_Y` is typed; section-pullback language exists | full projection map from EL tuple to 4D tensors | partial |
| 4D EL projection | minimal action spec gives checklist | branch-fixed full EL tuple and projection theorem absent | blocked |
| Conservation/source law | branch matrix distinguishes bare theta, corrected source, total current | derived Noether/Bianchi projection for chosen branch | blocked |
| Exact Schwarzschild/Kerr | weak-field canon bounded; exact gate defines witnesses | exact witness fields satisfying all EL equations | not passed |
| Weak-field limit | `R_fail^full=0` at `O(M/r)` conditionally | PPN and strong-field continuation from same branch | bounded pass only |
| Macroscopic limit | observer metric can be discussed as section shadow | classical/coarse-grained source-to-metric theorem | missing |

The first hard blocker is not Kerr arithmetic. It is a branch-fixed variational object:

```text
write S_GU and IG variation
derive full EL tuple
project it to the observer equation
then test Schwarzschild and Kerr.
```

## 4. Exact Schwarzschild/Kerr Implications

The exact black-hole requirement for a GR shadow is:

```text
Ric[g_BH] = 0 is necessary but not sufficient.
```

Schwarzschild and Kerr are already exact 4D GR vacuum metrics. GU-specific content begins
only when the induced section and source fields solve the full source EL tuple.

Implications by current evidence:

| issue | implication |
|---|---|
| Willmore-only section action | exact Schwarzschild has nonzero section residual; Kerr remains unsafe |
| Weak-field canon | protects only the stated `O(M/r)` compatibility result |
| Missing Branch 2A `Phi` | cannot preserve bare theta source and nonzero theta as a derived branch |
| Branch 2B | exact tests must include multiplier current; source is not bare theta |
| Branch 3 | exact tests must use `theta_eff`; bare-theta canon language must be revised |
| Free beta | theta collapses; it cannot be the nonzero-source branch |

Therefore:

```text
No current branch has a true exact Schwarzschild/Kerr GR-shadow pass.
The correct status is open/blocked, not failed globally and not recovered.
```

The distinction matters. The repo has branch-local failures, but because the full action
and IG branch are not fixed, the global GR-shadow claim is not yet a theorem of failure.
It is an unclosed certificate.

## 5. Branch Robustness Table

| Branch | Source law | True GR shadow status | Weak-field status | Main risk | Decision |
|---|---|---|---|---|---|
| Branch 2A: A-independent constrained IG | `D_A^*F_A = theta` if `D_A Phi = 0` | Not certified; `Phi` missing | Could preserve existing weak-field lane | invented or target-fitted constraint | strongest conservative template, underdefined |
| Branch 2B: A-dependent constrained IG | corrected by `(D_A Phi)^*lambda` | Not certified | must recompute source projection | multiplier current hides residuals | possible branch, not bare theta canon |
| Branch 3: dynamical IG / total current | `D_A^*F_A = theta_eff` | Not certified | must recompute with total current | source language changes; `S_IG-dyn` absent | honest fallback, action unwritten |
| Free-beta / bare norm | `theta = 0`, `D_A^*F_A = 0` | Fails nonzero-theta shadow | cannot support theta lane | auxiliary-field collapse | rejected |
| Background/Stueckelberg | may keep `D_A^*F_A = theta` | Not certified | compatible but thin | omitted variations and Noether cost | viable as spurion branch only |
| Willmore-only | no IG rescue; section EL only | Fails exact Schwarzschild; Kerr unsafe | weak-field residual suppressed | strong-field section residual | exact-GR branch failure |

Robust conclusion:

```text
No positive GR-shadow result is robust across the viable branch set.
The robust negative result is only branch-local:
  free beta kills theta;
  Willmore-only exact black-hole recovery fails.
```

## 6. Claim Certificate Table For GR-SHADOW And ACTION-GR

| Claim | Current status | Proof grade | Dependencies | Forbidden inputs | Closure condition | Exact citation language |
|---|---|---|---|---|---|---|
| `GR-SHADOW` | `specified_open` | `specification` | source fields; section extraction; full EL projection; source conservation; exact Schwarzschild/Kerr witnesses; weak-field/macroscopic limits | weak-field pass as exact recovery; hidden matter relabeling; Willmore-only recovery; branch-engineered cross terms; imported Einstein-Hilbert action as fundamental metric sector | one branch supplies the full certificate and passes exact + macroscopic gates without target fitting | "GR as an observer-facing GU shadow is now a specified certificate, not a proved result; the current repo has weak-field compatibility but no true GR-shadow recovery certificate." |
| `ACTION-GR` | `open` | `specification` | `IG-VARIATION`; written `S_GU`; full `(E_s,E_A,E_IG,E_Psi)`; `II_s^H`; boundary data; fixed source law | weak-field `O(M/r)` promoted to exact GR; relabeling `Q^TF(B_s)` as vacuum matter; unspecified `S_IG-dyn`; free beta with nonzero theta | exact Schwarzschild and Kerr admit smooth vacuum source-field configurations satisfying the full written EL tuple | "Exact GR recovery from the GU action remains open; Schwarzschild/Kerr have not passed the full source-EL test." |

## 7. Forbidden Shortcuts And Rollback Conditions

Forbidden shortcuts:

| shortcut | why it is not a GR shadow |
|---|---|
| Weak-field compatibility | It is a bounded `O(M/r)` check and leaves exact `E_s,E_A,E_IG` unresolved. |
| Willmore-only recovery | Exact Schwarzschild is not Willmore-critical; this is a branch failure, not a recovery. |
| Hidden matter relabeling | Moving `Q^TF(B_s)`, gauge residuals, or multiplier terms to `T_mu nu` fails vacuum GR recovery. |
| Branch-engineered cross terms | Terms chosen after seeing Schwarzschild/Kerr or `xi_eff` targets are target insertion. |
| Bare `R theta^2`, bare `Lambda`, or imported Einstein-Hilbert sector | These may define a different branch, but they do not prove GR is recovered as a source-geometry shadow. |
| Free beta plus nonzero theta | The beta EL equation forces `theta=0`; the branch contradicts itself. |
| Kerr by spherical analogy | Kerr must be checked with angular-momentum boundary data; Schwarzschild symmetry cannot certify it. |

Rollback conditions:

| condition | rollback |
|---|---|
| Primary `D_GU` lacks the typed first-order block needed by upstream gates | demote dependent VZ/action-shadow language to underdefined |
| Actual action varies free `beta` with only `|theta|^2` | reject nonzero-theta source branch |
| Branch 2A `Phi` is absent, A-dependent, or selected from target black-hole/cosmology success | remove bare-source GR-shadow route |
| Branch 3 is chosen but prose still says `D_A^*F_A = theta` | replace with total-current language everywhere |
| Schwarzschild or Kerr fails full vacuum EL tuple | no exact GR-shadow recovery for that branch |
| Exact pass requires nonzero matter stress or relabeled embedding stress | fail vacuum GR-shadow certificate |
| Macroscopic/PPN limit cannot be derived from the same branch | keep exact witness, if any, local only; no broad GR recovery |

## 8. First Exact Missing Proof Object

The first exact missing proof object is:

```text
ELProjectedGRShadowTheorem(branch)
```

Required input:

```text
S_GU[branch]
variation_space[eps,beta or U]
D_GU
section extraction map s^*
j_s and II_s^H normalization
boundary conditions
```

Required output:

```text
1. Full source EL tuple:
   E_s = E_A = E_IG = E_Psi = 0.

2. Branch-specific source law:
   D_A^*F_A = theta,
   or corrected multiplier source,
   or D_A^*F_A = theta_eff.

3. Projection identity:
   Pi_4D(E_s,E_A,E_IG,E_Psi)
     = G[g] + Lambda_eff g - kappa_eff T_shadow - R_shadow.

4. Conservation theorem:
   full Noether/Bianchi identity -> nabla^mu T_mu nu^shadow = 0
   plus any residual conservation law.

5. Vacuum witnesses:
   Schwarzschild and Kerr source-field configurations with R_shadow = 0.

6. Limit theorem:
   weak-field and macroscopic GR emerge from the same branch.
```

Why this object is first:

- Without it, exact Schwarzschild/Kerr cannot be evaluated as GU solutions.
- Without it, source conservation is only branch prose.
- Without it, weak-field compatibility cannot be promoted to recovered GR.
- Without it, "GR is a shadow" is interpretation rather than a certificate.

## 9. Next Meaningful Proof / Computation Step

Do one branch-fixed computation, not another synthesis:

```text
Attempt Branch 2A ELProjectedGRShadowTheorem for Schwarzschild.
```

Minimum next packet:

1. Derive or reject an A-independent, gauge-covariant
   `Phi(eps,beta,s)=0` from source GU/tau-plus/section geometry.
2. Prove `D_A Phi = 0` and compute the projected beta equation.
3. Write the full Branch 2A EL tuple with all `E_s` terms, including `S_W`,
   `S_YM`, `S_theta`, and constraint contributions.
4. Evaluate exact Schwarzschild before Kerr:

   ```text
   E_s = E_A = E_eps = E_beta = E_lambda = E_Psi = 0.
   ```

5. If Branch 2A fails or cannot be sourced, switch explicitly to Branch 3 and rewrite:

   ```text
   D_A^*F_A = theta_eff.
   ```

6. Only after the exact branch is fixed, run the weak-field/PPN/macroscopic projection
   and the FLRW scalar normalization from the same action.

## Machine-Auditable Summary

```json
{
  "version": "2026-06-24",
  "verdict": "CERTIFICATE_SPECIFIED_TRUE_GR_SHADOW_NOT_CERTIFIED",
  "claims": [
    {
      "id": "GR-SHADOW",
      "status": "specified_open",
      "proof_grade": "specification",
      "finality": "not_final",
      "decision": "no_current_true_gr_shadow_certificate",
      "depends_on": [
        "source_field_content",
        "section_metric_extraction",
        "full_4d_EL_projection",
        "conservation_source_law",
        "exact_schwarzschild_kerr_witnesses",
        "weak_field_macroscopic_limit",
        "ACTION-GR",
        "IG-VARIATION"
      ]
    },
    {
      "id": "ACTION-GR",
      "status": "open",
      "proof_grade": "specification",
      "finality": "not_final",
      "decision": "exact_schwarzschild_kerr_not_passed",
      "depends_on": [
        "IG-VARIATION",
        "written_S_GU",
        "full_EL_tuple",
        "II_s_H",
        "black_hole_boundary_data"
      ]
    }
  ],
  "pipeline": [
    {
      "stage": "source_field_content",
      "required": [
        "X",
        "Y_Met_Lor_X",
        "g_Y",
        "P_to_Y",
        "Sp64",
        "D_GU",
        "S_GU",
        "s",
        "A",
        "F_A",
        "eps",
        "beta_or_U",
        "theta",
        "Psi",
        "II_s_H",
        "j_s",
        "branch"
      ],
      "current_status": "partial_typed_action_branch_underdefined"
    },
    {
      "stage": "section_metric_extraction",
      "required": [
        "g_equals_s_star_g_Y",
        "s_star_A",
        "s_star_theta",
        "observer_metric_not_fundamental_quantized_object",
        "normalization_of_j_s_and_II_s_H"
      ],
      "current_status": "typed_but_projection_incomplete"
    },
    {
      "stage": "full_4d_EL_projection",
      "required": [
        "E_s",
        "E_A",
        "E_IG",
        "E_Psi",
        "Pi_4D",
        "R_shadow"
      ],
      "current_status": "blocked_missing_branch_fixed_EL_projection"
    },
    {
      "stage": "conservation_source_law",
      "required": [
        "branch_specific_source_law",
        "Noether_identity",
        "Bianchi_projection",
        "nabla_T_shadow_zero"
      ],
      "current_status": "blocked_source_law_branch_dependent"
    },
    {
      "stage": "exact_solution_tests",
      "required": [
        "Schwarzschild_witness_fields",
        "Kerr_witness_fields",
        "finite_action_boundary_data",
        "vacuum_no_hidden_matter",
        "full_EL_tuple_zero"
      ],
      "current_status": "not_passed"
    },
    {
      "stage": "weak_field_macroscopic_limit",
      "required": [
        "O_M_over_r_weak_field_pass_from_same_branch",
        "PPN_limit",
        "classical_metric_shadow_stability",
        "fixed_G_N_and_Lambda_eff",
        "controlled_GR_residuals"
      ],
      "current_status": "weak_field_bounded_pass_macroscopic_missing"
    }
  ],
  "true_shadow_criteria": [
    "metric_extracted_as_s_star_g_Y_not_fundamental_GR_quantum",
    "full_source_EL_tuple_vanishes_before_projection",
    "4d_projection_equals_Einstein_equation_with_fixed_constants",
    "source_conservation_derived_from_full_Noether_Bianchi_identities",
    "exact_Schwarzschild_and_Kerr_witnesses_pass",
    "weak_field_and_macroscopic_limits_from_same_branch",
    "no_hidden_matter_relabeling_or_target_fitted_terms"
  ],
  "current_evidence": {
    "true_gr_shadow": "not_certified",
    "weak_field_compatibility": "conditional_bounded_pass_O_M_over_r",
    "exact_schwarzschild_kerr": "blocked_open_not_passed",
    "willmore_only": "fails_exact_schwarzschild_kerr_unsafe",
    "ig_variation": "blocked",
    "branch_2a_phi": "missing",
    "theta_xi": "open_no_negative_xi_generated"
  },
  "distinctions": [
    {
      "shortcut": "weak_field_compatibility",
      "classification": "insufficient",
      "reason": "bounded_O_M_over_r_check_not_full_EL_solution"
    },
    {
      "shortcut": "willmore_only_recovery",
      "classification": "branch_failure",
      "reason": "exact_Schwarzschild_not_Willmore_critical_Kerr_unsafe"
    },
    {
      "shortcut": "hidden_matter_relabeling",
      "classification": "forbidden",
      "reason": "vacuum_GR_shadow_cannot_move_unexplained_residuals_to_T_matter"
    },
    {
      "shortcut": "branch_engineered_cross_terms",
      "classification": "forbidden",
      "reason": "cross_terms_must_be_primary_sourced_before_targets"
    }
  ],
  "branches": [
    {
      "key": "branch_2a",
      "label": "Branch 2A A-independent constrained IG",
      "status": "branch_underdefined",
      "source_law": "D_A^*F_A=theta_if_D_A_Phi_zero",
      "true_gr_shadow": "not_certified",
      "rollback_condition": "Phi_missing_A_dependent_or_target_fitted"
    },
    {
      "key": "branch_2b",
      "label": "Branch 2B A-dependent constrained IG",
      "status": "possible_source_corrected",
      "source_law": "corrected_by_multiplier_current",
      "true_gr_shadow": "not_certified",
      "rollback_condition": "bare_theta_source_claimed_despite_D_A_Phi_nonzero"
    },
    {
      "key": "branch_3",
      "label": "Branch 3 dynamical IG total current",
      "status": "honest_fallback_action_unwritten",
      "source_law": "D_A^*F_A=theta_eff",
      "true_gr_shadow": "not_certified",
      "rollback_condition": "S_IG_dyn_unspecified_or_bare_theta_language_retained"
    },
    {
      "key": "free_beta",
      "label": "Free beta bare theta norm",
      "status": "rejected",
      "source_law": "theta=0_and_D_A^*F_A=0",
      "true_gr_shadow": "fails_nonzero_theta_shadow",
      "rollback_condition": "none_branch_already_rejected"
    },
    {
      "key": "background_stueckelberg",
      "label": "Background/Stueckelberg",
      "status": "viable_but_thin",
      "source_law": "D_A^*F_A=theta_possible_after_normalization",
      "true_gr_shadow": "not_certified",
      "rollback_condition": "Noether_cost_or_section_EL_not_closed"
    },
    {
      "key": "willmore_only",
      "label": "Willmore-only section action",
      "status": "fails_exact_strong_field",
      "source_law": "no_IG_source_rescue",
      "true_gr_shadow": "fails_exact_GR_shadow",
      "rollback_condition": "exact_Schwarzschild_or_Kerr_claimed_without_full_coupled_EL"
    }
  ],
  "claim_certificates": [
    {
      "id": "GR-SHADOW",
      "status": "specified_open",
      "proof_grade": "specification",
      "dependencies": [
        "source_field_content",
        "section_metric_extraction",
        "full_4d_EL_projection",
        "conservation_source_law",
        "exact_schwarzschild_kerr_witnesses",
        "weak_field_macroscopic_limit"
      ],
      "forbidden_inputs": [
        "weak_field_pass_as_exact_recovery",
        "hidden_matter_relabeling",
        "Willmore_only_recovery",
        "branch_engineered_cross_terms",
        "imported_Einstein_Hilbert_fundamental_metric_sector"
      ],
      "rollback_condition": "any_required_stage_missing_or_target_fitted",
      "citation_language": "GR as an observer-facing GU shadow is specified but not certified; current evidence gives only bounded weak-field compatibility and open exact action recovery."
    },
    {
      "id": "ACTION-GR",
      "status": "open",
      "proof_grade": "specification",
      "dependencies": [
        "IG-VARIATION",
        "written_S_GU",
        "full_EL_tuple",
        "II_s_H",
        "black_hole_boundary_data"
      ],
      "forbidden_inputs": [
        "weak_field_O_M_over_r_promoted_to_exact_GR",
        "Q_TF_B_s_relabeling_as_vacuum_matter",
        "unspecified_S_IG_dyn",
        "free_beta_with_nonzero_theta"
      ],
      "rollback_condition": "Schwarzschild_or_Kerr_fails_full_vacuum_EL_tuple",
      "citation_language": "Exact GR recovery from the GU action remains open; Schwarzschild/Kerr have not passed the full source-EL test."
    }
  ],
  "forbidden_shortcuts": [
    "weak_field_compatibility_as_exact_GR",
    "Willmore_only_recovery",
    "hidden_matter_relabeling",
    "branch_engineered_cross_terms",
    "bare_Rtheta_or_Lambda_or_Einstein_Hilbert_insertion",
    "free_beta_nonzero_theta",
    "Kerr_by_spherical_analogy"
  ],
  "rollback_conditions": [
    "primary_D_GU_source_mismatch",
    "free_beta_only_theta_norm",
    "branch_2a_Phi_missing_or_target_fitted",
    "branch_3_without_theta_eff_language",
    "Schwarzschild_or_Kerr_full_EL_failure",
    "hidden_matter_required",
    "macroscopic_limit_not_from_same_branch"
  ],
  "first_missing_proof_object": {
    "id": "ELProjectedGRShadowTheorem",
    "requires": [
      "branch_fixed_S_GU",
      "IG_variation_or_S_IG_dyn",
      "full_source_EL_tuple",
      "Pi_4D_projection_identity",
      "conservation_theorem",
      "Schwarzschild_and_Kerr_witness_fields",
      "weak_field_macroscopic_limit"
    ],
    "why_first": "without_this_object_exact_GR_shadow_is_interpretation_not_certificate"
  },
  "next_step": "attempt_Branch_2A_ELProjectedGRShadowTheorem_for_exact_Schwarzschild_then_Kerr_or_switch_to_Branch_3_total_current"
}
```

## Sources Read

- `explorations/primary-gu-interface-contract-2026-06-24.md`
- `explorations/constraint-first-ig-tangent-space-gate-2026-06-24.md`
- `explorations/exact-schwarzschild-kerr-el-gate-2026-06-24.md`
- `explorations/gu-action-4d-physics-gate-2026-06-24.md`
- `explorations/gu-minimal-action-spec-2026-06-24.md`
- `explorations/gu-closed-loop-action-ig-branch-2026-06-24.md`
- `canon/schwarzschild-weak-field-rfail.md`
- `explorations/live-claim-dag-fault-finality-ledger-2026-06-24.md`
