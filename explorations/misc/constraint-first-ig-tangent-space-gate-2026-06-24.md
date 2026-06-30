---
title: "Constraint-First IG Tangent-Space Gate"
date: 2026-06-24
status: exploration
doc_type: research_gate
problem_label: "constraint-first-ig-tangent-space-theorem-or-nogo"
verdict: "NO_BRANCH_2A_DERIVED; CONDITIONAL_TANGENT_THEOREM_ONLY"
owned_path: "explorations/misc/constraint-first-ig-tangent-space-gate-2026-06-24.md"
audit_script: "tests/constraint_first_ig_tangent_gate.py"
depends_on:
  - "explorations/persona-and-dialectic/all-persona-wall-break-steelman-hegelian-2026-06-24.md"
  - "explorations/cycle-gates-and-audits/goal-draft-ig-constraint-derivation-2026-06-24.md"
  - "explorations/misc/gu-closed-loop-action-ig-branch-2026-06-24.md"
  - "explorations/cycle-gates-and-audits/gu-minimal-action-spec-2026-06-24.md"
  - "explorations/misc/ig-dynamics-nonzero-theta-action-gate-2026-06-24.md"
  - "explorations/geometry-curvature-emergence/exact-schwarzschild-kerr-el-gate-2026-06-24.md"
  - "explorations/dark-energy-cosmology/flrw-theta-xi-branch-reduction-2026-06-24.md"
  - "explorations/cycle-gates-and-audits/gu-action-4d-physics-gate-2026-06-24.md"
  - "explorations/cycle-gates-and-audits/live-claim-dag-fault-finality-ledger-2026-06-24.md"
---

# Constraint-First IG Tangent-Space Gate

## 1. Verdict

The current repo does not contain a derived, natural, gauge-covariant
A-independent constraint

```text
Phi(epsilon,beta,s) = 0
```

whose tangent space is proved to remove the free-beta theta collapse while preserving
the bare source equation

```text
D_A^* F_A = theta.
```

What the repo does contain is a sharp conditional theorem:

```text
If Branch 2A supplies a gauge-covariant A-independent Phi whose vertical beta tangent
is a proper subspace of Omega^1(Y,ad P), then nonzero theta may survive as a conormal
component and the A equation is not changed by multiplier currents.
```

But no current source supplies that `Phi`. The natural-looking candidates either:

- leave beta fully free and force `theta = 0`;
- use an A-dependent condition and therefore change the source law;
- are only pullback/Codazzi identities, not IG variation constraints;
- become arbitrary projectors whose success depends on choosing the allowed subspace after
  knowing the desired Schwarzschild/Kerr or FLRW outcome;
- or move to Branch 3, where IG dynamics is honest but the source is a total current
  `theta_eff`, not bare `theta`.

Decision:

```text
Branch 2A: branch-underdefined, not accepted.
Branch 2B: possible but source law corrected.
Branch 3: honest fallback if no natural 2A constraint is found.
Free beta: rejected, theta collapses.

ACTION-GR: remains open; exact Schwarzschild/Kerr not passed.
THETA-XI: remains open; negative xi_eff not generated.
```

This is not a proof that no such `Phi` can exist in mathematics. It is a no-go for the
current repo evidence: the proof object needed for Branch 2A is absent.

## 2. Tangent-Space Theorem / No-Go Statement

Let

```text
B = Omega^1(Y,ad P)
theta = A - Gamma(epsilon) - Ad(epsilon^-1) beta
S_theta = -c_theta/2 int_Y <theta,theta>.
```

Assume a constrained IG branch

```text
C_IG(s) = { (epsilon,beta) : Phi(epsilon,beta,s) = 0 }
```

with multiplier `lambda`, and assume first that `Phi` is independent of the dynamical
connection `A`. At a point `p = (epsilon,beta,s)`, define the pure beta tangent

```text
K_beta(p) = { delta beta in B : D_beta Phi_p(delta beta) = 0 }.
```

This is the part of the tangent space that varies beta while holding `epsilon` and `s`
fixed. The multiplier equation is

```text
c_theta Ad(epsilon) theta + (D_beta Phi)^* lambda = 0.
```

Equivalently, for every `eta in K_beta(p)`,

```text
int_Y <Ad(epsilon) theta, eta> = 0.
```

Therefore:

```text
Ad(epsilon) theta in K_beta(p)^perp.
```

Consequences:

| Tangent condition | Consequence |
|---|---|
| `K_beta = B` | `K_beta^perp = 0`, so `theta = 0`. This is the free-beta collapse. |
| `K_beta` proper | Nonzero theta is possible only in conormal directions to the constraint. |
| `K_beta = 0` | Pure beta is fully fixed; beta does not by itself force theta to zero. |
| `D_A Phi = 0` | The connection equation keeps the bare form `D_A^*F_A = theta` after normalization. |
| `D_A Phi != 0` | The connection equation gains `(D_A Phi)^* lambda`; the source law is corrected. |

The theorem is only a tangent-space theorem. It does not prove exact GR and does not
compute a dark-energy curvature coupling. It gives the first admissibility test for a
constraint-first route:

```text
Branch 2A acceptance requires:
  1. Phi is primary-sourced or forced by GU/tau-plus/section geometry.
  2. Phi is gauge-covariant.
  3. D_A Phi = 0 in the variational sense.
  4. K_beta is a proper beta tangent space, not all of Omega^1(Y,ad P).
  5. The conormal directions are not selected using Schwarzschild, Kerr, xi_eff < -0.319,
     xi ~= -0.6, a bare R theta^2 term, or a bare Lambda target.
  6. The same branch supplies enough data for E_s and the FLRW scalar reduction.
```

Current no-go:

```text
No source read in this pass supplies an explicit Phi satisfying all six Branch 2A
requirements.
```

## 3. Candidate Constraint Classes Considered

The candidates below are modeled by their tangent spaces, not by whether they sound
attractive as prose.

### C0. No Constraint / Full IG Translation

```text
C_IG = Epsilon x B.
```

Here `K_beta = B`. The beta equation is the free auxiliary-field equation:

```text
Ad(epsilon) theta = 0.
```

Result: `theta = 0`.

### C1. Background or Fixed Stueckelberg Data

This can be written as a degenerate graph

```text
beta = beta_bg(epsilon,s)
```

or simply as "do not vary `epsilon,beta`." Then `K_beta = 0` if treated as a
constraint, or there is no `E_beta` equation if treated as fixed background data.

This prevents the algebraic collapse and preserves the source equation, but it is not a
derived Branch 2A theorem unless the fixed data or graph is primary-sourced and gauge
covariant. It also weakens the Noether/divergence story because background spurion
variations are omitted.

### C2. A-Independent Geometric Graph

Template:

```text
beta = beta_0(epsilon,s)
Phi = beta - beta_0(epsilon,s).
```

At fixed `epsilon,s`, `K_beta = 0`. More generally, the beta projection of the tangent is

```text
Pi_beta(T C_IG) = im(D_epsilon beta_0, D_s beta_0).
```

This is the cleanest possible Branch 2A shape if `beta_0` is natural and gauge-equivariant.
It preserves

```text
D_A^* F_A = theta
```

because `D_A Phi = 0`.

Current status: desired template only. The repo notes name possible origins, such as
tau-plus, double-coset geometry, section-pullback geometry, or a real Stueckelberg slice,
but they do not supply an explicit A-independent `beta_0` or its tangent projector.

### C3. Tau-Plus / Maurer-Cartan Graph

Natural-looking candidate:

```text
beta = epsilon^-1 d_Gamma epsilon
```

or, using the transcript-style tau-plus map,

```text
beta = epsilon^-1 d_A epsilon.
```

The tau-plus and double-coset notes establish that the construction is group-theoretic and
gauge-equivariant for `G = Sp(64)`. They do not establish that the whole IG variation space
is restricted to the tau-plus image. In those notes, IG remains the semidirect product

```text
G semidirect Omega^1(ad P),
```

so the translation direction is still full unless an extra restriction is imposed.

If `d_A` uses the dynamical `A`, then

```text
D_A Phi != 0,
```

so this is Branch 2B, not Branch 2A. The multiplier current modifies the connection
equation.

If `d_Gamma` uses a fixed reference connection, the candidate could be A-independent and
proper, with tangent image made from covariant exact 1-forms. But the repo has not proved
that this fixed-reference tau-plus graph is the allowed IG variation space rather than a
chosen gauge slice. Current status: natural but underderived.

### C4. Projector or Admissible-Subbundle Constraint

Template:

```text
P_perp(epsilon,s) beta = 0,
beta in Gamma(E_adm(epsilon,s)).
```

Then

```text
K_beta = Gamma(E_adm).
```

This prevents collapse only if `E_adm` is a proper subbundle, and the surviving theta
must lie in the conormal directions:

```text
Ad(epsilon) theta in Gamma(E_adm)^perp.
```

This class can be gauge-covariant only if the projector is natural and equivariant. The
current repo does not supply such a projector. Choosing `E_adm` because its conormal
contains the desired Schwarzschild/Kerr source or the desired FLRW scalar is target
insertion.

### C5. Section-Pullback / Codazzi Constraint

Natural-looking relation:

```text
s^* theta = j_s(II_s^H)
```

or a Codazzi-reduced equation such as

```text
D_a^* F_a + K(A,s) = s^* theta.
```

These are important 4D reduction identities, but they are not currently an A-independent
IG constraint on `(epsilon,beta,s)`. Since

```text
theta = A - Gamma(epsilon) - Ad(epsilon^-1) beta,
```

any constraint written directly on `theta` is A-dependent unless `A` is eliminated by a
separate primary construction. It therefore contributes `(D_A Phi)^* lambda` to `E_A`.

This class is also only a pullback condition. It does not constrain all vertical beta
directions on `Y`; many beta variations can vanish under `s^*` while still being full in
the ambient IG field space.

Current status: natural reduction data, not a Branch 2A variation-space proof.

### C6. Divergence Constraint

Template:

```text
Phi = D_A^* theta = 0.
```

This is gauge-covariant and can make the allowed beta tangent differential rather than
full. But it is explicitly A-dependent. It protects the divergence-free condition by
construction at the price of changing the A equation with derivative multiplier terms.

This is Branch 2B. It cannot be used while still claiming the uncorrected source law
unless the multiplier current is separately proved to vanish.

### C7. FLRW Scalar or Negative-Xi Filter

Examples:

```text
s^* theta = b(t) u_0,
xi_eff < -0.319,
xi ~= -0.6,
```

or any constraint chosen so that the reduced action contains the desired

```text
-1/2 xi R[g] B^2.
```

This is not an admissible `Phi`. It depends on the target cosmology, the scalar ansatz,
or the desired coefficient. It fails the anti-smuggling test even if it prevents the
free-beta collapse.

### C8. Exact Schwarzschild/Kerr Matching Constraint

Example:

```text
Phi chosen so that E_s(s_Schwarzschild) = 0 and E_s(s_Kerr) = 0.
```

This is target engineering. It may be useful as a diagnostic ansatz, but it is not a GU
derivation. It fails anti-smuggling unless the same `Phi` is independently defined before
the black-hole metrics are mentioned.

### C9. Dynamical IG

Branch 3 is not a constraint-first route:

```text
S_IG-dyn = -Z_U/2 int |D_A U|^2 - int V(U,epsilon) - c_theta/2 int |theta|^2
```

or the first-order parent action with momentum `P`.

The tangent space may remain full, but the beta/`U` equation is no longer algebraic, so
nonzero theta can survive. The price is that the source law becomes

```text
D_A^* F_A = theta_eff,
theta_eff = c_theta theta - J_IG.
```

This is the honest fallback if no Branch 2A constraint is derived.

## 4. Candidate-by-Candidate Status

| Candidate | Naturality | Gauge covariance | Tangent-space size | Source-law effect | Anti-smuggling status |
|---|---|---|---|---|---|
| C0 no constraint / full IG | Natural as the full semidirect product | Yes | `K_beta = B` full | `theta = 0`; source collapses to `D_A^*F_A=0` | Not smuggled, but fails |
| C1 fixed/background data | Possible only if primary-sourced | Spurion-covariant if transformed | No beta EL, or `K_beta = 0` | Bare source preserved | Must not be target-fitted; not a dynamical IG theorem |
| C2 A-independent graph `beta_0(epsilon,s)` | Strong template, not instantiated | Would pass if `beta_0` equivariant | `K_beta = 0`; projection proper only if proved | Bare source preserved | Passes only if `beta_0` is derived before physics targets |
| C3 tau-plus graph | Natural group-theoretically | Yes | Proper only if tau-plus image is imposed as variation space | Branch 2A only with fixed reference; Branch 2B if `d_A` uses dynamical `A` | Underderived; no target insertion by itself |
| C4 projector/subbundle | Natural only if canonical projector exists | Only if equivariant | Proper if nontrivial `E_adm` is proved | Bare source preserved if A-independent | Fails if projector chosen around target theta |
| C5 section/Codazzi relation | Natural reduction identity | Type-checks after soldering `j_s` | Pullback restriction, not ambient beta tangent proof | A-dependent if written on `theta`; source corrected | Fails if used to impose exact-GR cancellation |
| C6 `D_A^*theta=0` | Natural as conservation/gauge condition | Yes | Differentially proper | A-dependent multiplier changes `E_A` | Smuggles conservation if imposed instead of derived |
| C7 FLRW scalar/xi filter | Low | Only after ansatz | Engineered | Depends on chosen term | Fails: uses `xi_eff < -0.319` or `xi ~= -0.6` as input |
| C8 exact-GR matching | Low | Depends on construction | Engineered | Usually changes section/source equations | Fails: uses Schwarzschild/Kerr success as input |
| C9 dynamical IG | Natural action route if written | Yes if action is invariant | Constraint theorem not applicable | Source becomes `theta_eff` | Honest fallback; still no exact GR or xi coefficient |

## 5. Claim Certificate Table for ACTION-GR and THETA-XI

| Claim node | Current certificate | What this tangent gate changes | Forbidden success inputs | Closure condition |
|---|---|---|---|---|
| `ACTION-GR` | `open`, proof grade `specification`, finality `not_final` | No upgrade. Branch 2A is not derived, 2B changes the source, Branch 3 changes the source, and free beta fails. | Weak-field `O(M/r)` pass as exact recovery; Willmore-only cancellation; relabeling `Q^TF(B_s)` as vacuum matter; unspecified IG dynamics or cross terms; a `Phi` chosen because Schwarzschild/Kerr need it. | A written branch with full `(E_s,E_A,E_epsilon,E_beta,E_Psi)` and smooth vacuum Schwarzschild and Kerr solutions, with no hidden matter source. |
| `THETA-XI` | `open`, proof grade `conditional_reconstruction`, finality `not_final` for GU provenance | No upgrade. No current branch computes `Z_theta`, `C_Rtheta`, or `xi_eff = C_Rtheta/Z_theta`; free beta removes the scalar. | Bare `R theta^2`; inserted `xi ~= -0.6`; treating `xi_eff < -0.319` as input; assuming scalar `s^*theta` after the constraint removes or changes it; using unspecified `S_IG-dyn`. | Written branch reduces to a canonical homogeneous scalar with generated `xi_eff < -0.319`, preferably near `-0.6`, after normalization. |

## 6. Branch Robustness Table

| Branch | Tangent-space result | Source-law robustness | Exact GR consequence | Theta-xi consequence | Decision |
|---|---|---|---|---|---|
| Branch 2A: A-independent constrained IG | Required `K_beta proper`; not proved by current repo | Robust only if `D_A Phi = 0` and no hidden A dependence | Open; full section equation still uncomputed | Open; scalar mode and coefficients undefined | Strongest conservative template, branch-underdefined |
| Branch 2B: A-dependent constrained IG | Can prevent collapse | Not robust: `(D_A Phi)^* lambda` corrects `E_A` | Open; multiplier current must be solved | Open; multiplier branch affects coefficients | Possible branch, but not bare theta-source canon |
| Branch 3: dynamical IG / total current | Constraint theorem not applicable; full variations allowed with dynamics | Robust only after rewriting source as `theta_eff` | Open; possible cancellation route but no solution | Open; best shape for scalar dynamics but no coefficient | Honest fallback if 2A fails |
| Free beta / bare norm | `K_beta = B` full | Fails: `theta = 0` | Fails or reduces to Willmore/YM vacuum | Fails: theta scalar absent | Rejected |

Robustness conclusion:

```text
No positive target is robust across Branch 2A, 2B, 3, and free beta.
The only robust result is the negative one: free beta plus only |theta|^2 kills theta.
```

## 7. First Exact Obstruction or Missing Proof Object

The first missing proof object is not a Schwarzschild computation and not a cosmology
scan. It is the Branch 2A tangent certificate:

```text
Object:
  a gauge-covariant A-independent Phi(epsilon,beta,s)=0

Required data:
  D_beta Phi
  K_beta = ker(D_beta Phi)
  proof that K_beta is a proper beta tangent space
  conormal image im(D_beta Phi)^*
  projected beta equation
  proof that D_A Phi = 0 in the variational sense
  proof that Phi was not selected using Schwarzschild, Kerr, xi_eff < -0.319, xi ~= -0.6,
  a bare R theta^2 term, or a bare Lambda target.
```

Why the current natural candidates do not supply it:

- The full IG semidirect product is natural and gauge-covariant, but its translation tangent
  is full and beta collapses theta.
- Tau-plus is natural and gauge-covariant, but the repo uses it to establish equivariance
  and the IG construction, not to restrict all IG variations to the tau-plus graph. If it
  uses dynamic `A`, it is Branch 2B.
- Section-pullback and Codazzi identities are important reduction data, but constraints
  written on `theta` are A-dependent and do not define the ambient beta variation space.
- Divergence constraints are A-dependent and change `E_A`.
- Projectors and scalar filters have no canonical source in the repo and are vulnerable to
  target insertion.

Therefore the first obstruction is:

```text
No derived D_beta Phi, hence no tangent projector, hence no legitimate Branch 2A beta
projection equation.
```

Downstream consequences:

- Without `Phi`, exact Schwarzschild/Kerr cannot be tested as solutions of a fixed EL tuple.
- Without `Phi` or `S_IG-dyn`, the FLRW scalar direction `u_0`, `Z_theta`, and `C_Rtheta`
  are undefined.
- Without `D_A Phi = 0`, the bare source equation cannot be preserved.

## 8. Next Meaningful Proof / Computation Step

Do a tau-plus slice audit before any more GR or FLRW work:

```text
Input:
  tau-plus / double-coset construction
  reference connection choice Gamma versus dynamical A
  current definitions of epsilon, beta, and IG

Output:
  one of:
    TAU_SLICE_2A_DERIVED:
      beta = beta_0(epsilon,s) or epsilon^-1 d_Gamma epsilon,
      D_A Phi = 0,
      K_beta proper,
      gauge covariance proved.

    TAU_SLICE_2B_ONLY:
      beta = epsilon^-1 d_A epsilon or equivalent A-dependent slice,
      source law corrected by multiplier current.

    TAU_NOT_A_VARIATION_CONSTRAINT:
      tau-plus gives equivariance only; IG translation remains full.

    NO_NATURAL_SLICE_USE_BRANCH_3:
      write S_IG-dyn and replace theta by theta_eff in the source law.
```

If `TAU_SLICE_2A_DERIVED` is not obtained, stop calling Branch 2A the active action
branch. Move to Branch 3 or keep the action gate open. Only after the tangent certificate
exists should the next worker compute:

```text
E_s for exact Schwarzschild first,
then Kerr,
then the FLRW scalar projection and xi_eff = C_Rtheta / Z_theta.
```

## Machine-Auditable Summary

```json
{
  "version": "2026-06-24",
  "verdict": "NO_BRANCH_2A_DERIVED",
  "tangent_theorem": {
    "beta_space": "Omega^1(Y,ad P)",
    "collapse_condition": "K_beta = Omega^1(Y,ad P)",
    "survival_condition": "Ad(epsilon) theta in K_beta^perp with K_beta proper",
    "branch_2a_requires": [
      "gauge_covariant_Phi",
      "D_A_Phi_equals_0",
      "proper_beta_tangent",
      "primary_or_geometric_origin",
      "no_target_success_inputs"
    ],
    "current_repo_has_natural_branch_2a_phi": false
  },
  "forbidden_target_success_inputs": [
    "Schwarzschild/Kerr exact solution",
    "weak-field O(M/r) as exact GR",
    "Q^TF(B_s) relabeled as vacuum matter",
    "xi_eff < -0.319",
    "xi ~= -0.6",
    "bare R theta^2",
    "bare Lambda",
    "unspecified S_IG-dyn"
  ],
  "candidates": [
    {
      "key": "no_constraint_full_ig",
      "status": "fail_theta_collapse",
      "natural": true,
      "gauge_covariant": true,
      "tangent": "K_beta_full",
      "source_law": "D_A^*F_A=0_after_theta_zero",
      "anti_smuggling": "not_smuggled_but_fails"
    },
    {
      "key": "background_or_fixed_stueckelberg",
      "status": "not_branch_2a_derivation",
      "natural": "only_if_primary_sourced",
      "gauge_covariant": "spurion_covariant_if_transformed",
      "tangent": "no_E_beta_or_K_beta_zero",
      "source_law": "bare_theta_source_preserved",
      "anti_smuggling": "must_not_be_target_fitted"
    },
    {
      "key": "a_independent_geometric_graph",
      "status": "template_not_instantiated",
      "natural": "possible",
      "gauge_covariant": "requires_equivariant_beta_0",
      "tangent": "K_beta_zero_projection_undefined",
      "source_law": "bare_theta_source_preserved_if_D_A_Phi_zero",
      "anti_smuggling": "passes_only_if_derived_before_targets"
    },
    {
      "key": "tau_plus_graph",
      "status": "underdetermined_or_2b",
      "natural": true,
      "gauge_covariant": true,
      "tangent": "proper_only_if_tau_image_is_imposed",
      "source_law": "bare_if_fixed_reference_corrected_if_dynamic_A",
      "anti_smuggling": "not_target_driven_but_not_derived_as_constraint"
    },
    {
      "key": "projector_admissible_subbundle",
      "status": "not_found_in_repo",
      "natural": "requires_canonical_projector",
      "gauge_covariant": "requires_equivariant_projector",
      "tangent": "K_beta_equals_admissible_subbundle",
      "source_law": "bare_if_A_independent",
      "anti_smuggling": "fails_if_chosen_to_keep_target_theta"
    },
    {
      "key": "section_pullback_codazzi",
      "status": "reduction_identity_not_branch_2a_constraint",
      "natural": true,
      "gauge_covariant": "after_soldering_map",
      "tangent": "pullback_restriction_not_ambient_beta_certificate",
      "source_law": "corrected_if_written_on_theta",
      "anti_smuggling": "fails_if_used_to_force_exact_GR_cancellation"
    },
    {
      "key": "divergence_constraint",
      "status": "branch_2b_source_corrected",
      "natural": true,
      "gauge_covariant": true,
      "tangent": "differentially_proper",
      "source_law": "corrected_by_multiplier_current",
      "anti_smuggling": "smuggles_conservation_if_imposed_not_derived"
    },
    {
      "key": "flrw_scalar_xi_filter",
      "status": "anti_smuggling_fail",
      "natural": false,
      "gauge_covariant": "ansatz_dependent",
      "tangent": "engineered",
      "source_law": "target_dependent",
      "anti_smuggling": "uses_negative_xi_target"
    },
    {
      "key": "exact_gr_matching_constraint",
      "status": "anti_smuggling_fail",
      "natural": false,
      "gauge_covariant": "construction_dependent",
      "tangent": "engineered",
      "source_law": "target_dependent",
      "anti_smuggling": "uses_black_hole_success_target"
    },
    {
      "key": "dynamical_ig_total_current",
      "status": "honest_fallback_not_constraint_theorem",
      "natural": "possible_if_action_written",
      "gauge_covariant": "requires_invariant_S_IG_dyn",
      "tangent": "constraint_not_applicable",
      "source_law": "D_A^*F_A=theta_eff",
      "anti_smuggling": "acceptable_if_coefficients_fixed_before_targets"
    }
  ],
  "branches": [
    {
      "key": "constrained_ig_a_independent",
      "status": "branch_underdefined",
      "nonzero_theta": "conditional_on_derived_proper_tangent",
      "source_law": "D_A^*F_A=theta_only_if_D_A_Phi_zero",
      "exact_gr": "not_passed",
      "theta_xi": "not_generated"
    },
    {
      "key": "constrained_ig_a_dependent",
      "status": "source_corrected",
      "nonzero_theta": "possible",
      "source_law": "corrected_by_multiplier_current",
      "exact_gr": "not_passed",
      "theta_xi": "not_generated"
    },
    {
      "key": "dynamical_ig_total_current",
      "status": "honest_fallback",
      "nonzero_theta": "possible_with_written_dynamics",
      "source_law": "D_A^*F_A=theta_eff",
      "exact_gr": "not_passed",
      "theta_xi": "not_generated"
    },
    {
      "key": "bare_free_beta_norm",
      "status": "rejected",
      "nonzero_theta": "fails_theta_equals_zero",
      "source_law": "D_A^*F_A=0",
      "exact_gr": "not_passed",
      "theta_xi": "theta_scalar_absent"
    }
  ],
  "claim_certificates": [
    {
      "id": "ACTION-GR",
      "status": "open",
      "proof_grade": "specification",
      "finality": "not_final",
      "decision": "no_exact_GR_pass",
      "depends_on": ["IG-VARIATION", "written_S_GU", "full_EL_tuple"]
    },
    {
      "id": "THETA-XI",
      "status": "open",
      "proof_grade": "conditional_reconstruction",
      "finality": "not_final",
      "decision": "no_generated_negative_xi",
      "depends_on": ["IG-VARIATION", "ACTION-GR", "canonical_scalar_reduction"]
    }
  ],
  "next_step": "tau_plus_slice_audit_before_exact_GR_or_FLRW"
}
```

## Sources Read

Required sources:

- `explorations/persona-and-dialectic/all-persona-wall-break-steelman-hegelian-2026-06-24.md`
- `explorations/cycle-gates-and-audits/goal-draft-ig-constraint-derivation-2026-06-24.md`
- `explorations/misc/gu-closed-loop-action-ig-branch-2026-06-24.md`
- `explorations/cycle-gates-and-audits/gu-minimal-action-spec-2026-06-24.md`
- `explorations/misc/ig-dynamics-nonzero-theta-action-gate-2026-06-24.md`
- `explorations/geometry-curvature-emergence/exact-schwarzschild-kerr-el-gate-2026-06-24.md`
- `explorations/dark-energy-cosmology/flrw-theta-xi-branch-reduction-2026-06-24.md`
- `explorations/cycle-gates-and-audits/gu-action-4d-physics-gate-2026-06-24.md`
- `explorations/cycle-gates-and-audits/live-claim-dag-fault-finality-ledger-2026-06-24.md`

Additional context used:

- `explorations/cycle-gates-and-audits/gu-typed-operator-action-spine-2026-06-24.md`
- `explorations/generation-sector/ig-dimension-matching-sp64-tau-plus-2026-06-22.md`
- `explorations/geometry-curvature-emergence/4d-reduction-section-pullback-2026-06-22.md`
- `explorations/geometry-curvature-emergence/codazzi-sp64-bundle-2026-06-23.md`
- `tests/gu_action_branch_gate.py`
- `tests/flrw_theta_xi_branch_gate.py`
- `tests/live_claim_dag_audit.py`
