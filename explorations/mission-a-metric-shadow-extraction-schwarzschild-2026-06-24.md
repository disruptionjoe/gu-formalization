---
title: "Mission A Metric Shadow Extraction: Exact Schwarzschild Branch Attempt"
date: "2026-06-24"
status: exploration/branch_attempt
doc_type: metric_shadow_extraction_attempt
problem_label: "metric-shadow-extraction-schwarzschild"
verdict: "BRANCH_2A_NOT_SOURCED; BRANCH_3_TOTAL_CURRENT_OBJECT_REQUIRED; EXACT_SCHWARZSCHILD_PACKET_SPECIFIED_NOT_FILLED"
owned_path: "explorations/mission-a-metric-shadow-extraction-schwarzschild-2026-06-24.md"
audit_script: "tests/mission_a_metric_shadow_extraction_audit.py"
depends_on:
  - "RESEARCH-POSTURE.md"
  - "process/runbooks/five-lane-frontier-run.md"
  - "explorations/metric-marble-prematurity-gate-2026-06-24.md"
  - "explorations/gr-shadow-recovery-certificate-2026-06-24.md"
  - "explorations/exact-schwarzschild-kerr-el-gate-2026-06-24.md"
  - "explorations/constraint-first-ig-tangent-space-gate-2026-06-24.md"
  - "explorations/gu-action-4d-physics-gate-2026-06-24.md"
  - "explorations/gu-minimal-action-spec-2026-06-24.md"
  - "canon/schwarzschild-weak-field-rfail.md"
---

# Mission A Metric Shadow Extraction: Exact Schwarzschild Branch Attempt

## 1. Verdict

This is the first branch-local attempt packet for:

```text
MetricShadowExtractionTheorem(branch, exact Schwarzschild).
```

Decision:

```text
Branch 2A exact Schwarzschild metric-shadow extraction:
  status: conditional_template_only / not executable
  reason: no sourced A-independent Phi(epsilon,beta,s)=0 exists in the current repo

Exact Schwarzschild witness:
  status: packet_specified / not filled
  reason: no branch-fixed full source EL tuple and no source fields solving it

Branch 3 fallback:
  status: required constructive fallback
  minimum object: S_IG_dyn plus total conserved source theta_eff

Exact GR recovery:
  status: not claimed
```

This is not the old "exact GR is blocked" stop sign. Under Mission A, if GU is correct,
there must be a source-geometric object whose observer projection makes Schwarzschild an
exact vacuum metric shadow. The useful result of this pass is that the object can now be
named, its Branch 2A fork can be rejected without pessimism, and the Branch 3 replacement
can be made precise enough for the next computation.

The first live theorem target is:

```text
SchwarzschildMetricShadowExtractionTheorem(branch):
  source fields on Y
  -> admitted section s_M
  -> induced metric g_M = s_M^* g_Y
  -> full source EL tuple E_source = 0
  -> projection Pi_4D(E_source)
  -> G[g_M] - R_shadow = 0
  with R_shadow = 0 in vacuum.
```

Schwarzschild's 4D Ricci-flatness is necessary but carries no GU-specific content by
itself. The GU content begins only when the source fields and source equations select the
Schwarzschild section without importing a metric-first Einstein-Hilbert sector, hidden
matter, or a target-fitted constraint.

## 2. If GU Is Correct, What Metric-Shadow Object Must Exist Here

If the GU hypothesis is substantially correct in the metric-as-shadow sense, exact
Schwarzschild requires a branch-local object with this type:

```text
G_src^Schw(branch) =
  (X_M, Y, g_Y, P, Sp(64), S_GU[branch], D_GU,
   section_space, variation_space, boundary_data,
   s_M, A_M, epsilon_M, beta_M_or_U_M, lambda_M_if_any, Psi_M)
```

where:

```text
X_M = Schwarzschild exterior domain r > 2M
Y = Met_Lor(X_M)
g_M = s_M^* g_Y = g_Schwarzschild(M)       up to diffeomorphism/gauge
Psi_M = 0                                  vacuum spinor sector, if no tadpole exists
T_matter = 0
Lambda_eff = 0                             unless an explicit asymptotic Lambda branch is declared
```

The theorem must produce, not assume:

```text
E_source(branch; s_M,A_M,epsilon_M,beta_M_or_U_M,lambda_M,Psi_M) = 0

Pi_4D(E_source) =
  G_mu nu[g_M]
  + Lambda_eff g_mu nu
  - kappa_eff T_mu nu^shadow
  - R_mu nu^shadow
  = 0

vacuum Schwarzschild specialization:
  G_mu nu[g_M] = 0
  Lambda_eff = 0
  T_mu nu^shadow = 0
  R_mu nu^shadow = 0
```

The metric-shadow object therefore has three logically separate layers:

| layer | required object | current status |
|---|---|---|
| extraction | `g_M = s_M^* g_Y`, induced metric variations from source variations | typed but not proved as an exact solution branch |
| source equation | full `E_s,E_A,E_IG,E_Psi,E_lambda` for one branch | not fixed for Branch 2A or Branch 3 |
| projection | `Pi_4D(E_source)` giving Einstein form with controlled residual | missing theorem |

Mission A reconstruction label:

```text
This is a reconstruction target, not a proof.
```

Proof would require the exact fields, exact action/operator branch, and exact projection
identity. Speculation begins only when proposing candidate origins for `Phi` or
`S_IG_dyn`; those proposals are labeled below.

## 3. Branch 2A Construction Attempt

Branch 2A is the conservative branch because it preserves the bare source equation after
normalization:

```text
D_A^* F_A = theta
theta = A - Gamma(epsilon) - Ad(epsilon^-1) beta.
```

It can do that only if the IG constraint is A-independent:

```text
Phi(epsilon,beta,s) = 0,
D_A Phi = 0.
```

The Branch 2A exact Schwarzschild packet would use:

```text
S_vac^2A =
  S_YM[A]
  + S_theta[A,epsilon,beta]
  + S_W[s,A,epsilon,beta]
  + int_Y <lambda, Phi(epsilon,beta,s)>
  + S_DD[A,epsilon,Psi]
  + S_cross^vac
  + S_boundary
```

with the baseline rule:

```text
S_cross^vac = 0
```

unless a primary source fixes a cross term and coefficient before Schwarzschild is tested.

### 3.1 Candidate Phi Requirements

For Branch 2A to be usable here, `Phi` must satisfy all of the following:

| requirement | exact role in the Schwarzschild packet |
|---|---|
| primary or geometric origin | `Phi` must come from GU/tau-plus/double-coset/section geometry before black-hole targets are named. |
| A-independence | `D_A Phi = 0`, so the connection equation is not corrected by multiplier current. |
| gauge covariance | the constraint surface is preserved by local `Sp(64)` gauge transformations. |
| proper beta tangent | `K_beta = ker D_beta Phi` is a proper subspace of `Omega^1(Y,ad P)`. |
| conormal theta survival | `Ad(epsilon) theta in K_beta^perp` may be nonzero without choosing the conormal from Schwarzschild success. |
| section compatibility | `D_s Phi` is defined and contributes honestly to `E_s`, rather than hiding section residuals. |
| anti-smuggling | no use of exact Schwarzschild, Kerr, weak-field success, desired `xi_eff`, bare `Lambda`, or bare `R theta^2` to choose the constraint. |

The tangent theorem from the constraint-first gate says:

```text
E_beta:
  c_theta Ad(epsilon) theta + (D_beta Phi)^* lambda = 0

for eta in K_beta:
  <Ad(epsilon) theta, eta> = 0

therefore:
  Ad(epsilon) theta in K_beta^perp.
```

If `K_beta` is full, then `theta = 0`. If `K_beta` is proper and sourced, nonzero theta may
survive. That is the whole Branch 2A opportunity.

### 3.2 Available Sources And Candidate Status

The required sources do not currently supply a usable `Phi`:

| candidate source | status for Branch 2A | reason |
|---|---|---|
| no constraint / full IG translation | fails | beta variations are full, so `theta = 0`. |
| A-independent graph `beta = beta_0(epsilon,s)` | strong template only | no natural `beta_0` is supplied by the repo sources. |
| fixed-reference tau-plus graph | speculative source | could be A-independent if it uses fixed `Gamma`, but no theorem says IG variations are restricted to this graph. |
| dynamic tau-plus graph using `d_A` | Branch 2B, not 2A | A-dependent, so multiplier current modifies `E_A`. |
| section-pullback/Codazzi relation | reduction identity, not IG tangent certificate | constraints on `s^*theta` do not control all ambient beta variations on `Y`. |
| divergence condition `D_A^* theta = 0` | Branch 2B | A-dependent and imposes conservation instead of deriving it. |
| projector/admissible subbundle | underived | no canonical equivariant projector appears in the required sources. |
| exact Schwarzschild matching filter | forbidden | target-fitted constraint. |

Survival status:

```text
Branch 2A survives as a conditional theorem template.
Branch 2A does not currently supply an executable exact Schwarzschild witness.
```

The branch cannot currently be used because the exact EL tuple depends on data that do not
exist:

```text
D_beta Phi,
K_beta,
(D_beta Phi)^* lambda,
D_s Phi,
proof D_A Phi = 0,
anti-smuggling proof for Phi.
```

Without those data, the symbols `E_beta`, `E_lambda`, and `E_s^Phi` are placeholders. A
placeholder cannot certify an exact Schwarzschild metric shadow.

### 3.3 Branch 2A Equations If Phi Were Supplied

If a sourced `Phi` is later found, the exact Schwarzschild equations to solve are:

```text
E_A =
  g_A^-2 D_A^* F_A
  - c_theta theta
  + E_A^W
  + J_Psi
  + E_A^cross
  = 0

E_s =
  alpha_W W_s
  + E_s^YM
  + E_s^theta
  + (D_s Phi)^* lambda
  + E_s^cross
  + T_s^Psi
  = 0

E_beta =
  c_theta Ad(epsilon) theta
  + (D_beta Phi)^* lambda
  + E_beta^W
  + E_beta^cross
  = 0

E_epsilon =
  c_theta L_epsilon^* theta
  + (D_epsilon Phi)^* lambda
  + E_epsilon^W
  + E_epsilon^DD
  + E_epsilon^cross
  = 0

E_lambda = Phi(epsilon,beta,s) = 0

E_Psi =
  D_GU(A,epsilon) Psi
  + lower-order spinor terms
  = 0.
```

For strict Branch 2A:

```text
E_A^Phi = 0.
```

That condition is load-bearing. If `E_A^Phi` is nonzero, the source equation is corrected
and the branch is no longer 2A.

## 4. Branch 3 Fallback Construction

Because Branch 2A cannot currently be sourced, the minimal honest fallback is Branch 3:
dynamical IG variables and a total current. This is not a downgrade to vagueness. It is a
different object with a different source law.

Minimum Branch 3 object:

```text
S_GU^3 =
  S_YM[A]
  + S_theta[A,epsilon,U]
  + S_IG_dyn[A,epsilon,U,P_IG;s]
  + S_W[s,A,epsilon,U]
  + S_DD[A,epsilon,Psi]
  + S_boundary
```

where either:

```text
U = Ad(epsilon^-1) beta
```

or a first-order parent pair is used:

```text
(U, P_IG).
```

A minimal schematic action shape is:

```text
S_IG_dyn =
  - Z_U/2 int_Y <D_A U, D_A U>
  - int_Y V(U,epsilon)
  + first_order_terms(P_IG, D_A U)
  + possible source-fixed section couplings.
```

This schematic is not yet a GU action. It is the smallest object that would let the
Schwarzschild attempt proceed without pretending bare theta is conserved.

The Branch 3 connection equation must be:

```text
E_A =
  g_A^-2 D_A^*F_A
  - c_theta theta
  + J_IG
  + E_A^W
  + J_Psi
  + E_A^cross
  = 0.
```

Equivalently:

```text
D_A^*F_A = theta_eff

theta_eff =
  g_A^2(c_theta theta - J_IG - E_A^W - J_Psi - E_A^cross)
```

or, in the cleaner vacuum normalization when `E_A^W`, `J_Psi`, and cross terms are absent
from the connection source:

```text
theta_eff = g_A^2(c_theta theta - J_IG).
```

The conserved object is:

```text
D_A^* theta_eff = 0
```

as the branch's Noether/Bianchi consequence. Conservation is not a statement about bare
`theta` unless the action proves `J_IG = 0` and the other source corrections vanish.

Branch 3 exact Schwarzschild must supply:

```text
(s_M, A_M, epsilon_M, U_M, P_IG,M, Psi_M = 0)
```

such that:

```text
E_s^3 = 0
E_A^3 = 0
E_U^3 = 0
E_P_IG^3 = 0       if first-order parent is used
E_epsilon^3 = 0
E_Psi^3 = 0
```

and:

```text
Pi_4D(E_source^3) =
  G[g_M] - R_shadow^3 = 0,
R_shadow^3 = 0.
```

The constructive opportunity in Branch 3 is real: `S_IG_dyn` may produce section-variation
terms and source currents capable of canceling the known Willmore-only Schwarzschild
residual. The cost is also real: all source-current language must be rewritten around
`theta_eff`.

## 5. Exact Schwarzschild Witness Packet

This section is the packet that a future proof or computation must fill.

### 5.1 Domain And Boundary Data

Required data:

```text
X_M = {r > 2M} with asymptotically flat Schwarzschild exterior structure
M > 0 fixed by ADM mass at infinity
inner boundary: horizon-excision limit r -> 2M^+ or regular horizon extension stated
outer boundary: r -> infinity with fixed ADM mass and finite source action
Lambda_eff = 0 unless a separate asymptotic Lambda branch is declared
T_matter = 0
```

Gauge/IG boundary data:

```text
A_M has finite Yang-Mills action/energy on the exterior domain
allowed gauge transformations approach the declared asymptotic class
epsilon_M, beta_M_or_U_M obey finite source norm and boundary variations
lambda_M obeys the multiplier boundary condition in Branch 2A, if used
section variations fix ADM mass and preserve the declared exterior domain
```

### 5.2 Required Fields

| field | required value or property | can currently be filled? |
|---|---|---|
| `s_M` | section with `s_M^* g_Y = g_Schwarzschild(M)` | only as target extraction data; not source-selected |
| `g_M` | exact Schwarzschild exterior metric | yes, as external GR target |
| `B_M = II_s^H` | horizontal-normalized section second fundamental form | typed; exact source value not computed here |
| `A_M` | Sp(64) connection solving the branch source equation | no |
| `F_A,M` | curvature of `A_M` with finite boundary data | no |
| `epsilon_M` | IG/gauge variable compatible with `Gamma(epsilon)` | no |
| `beta_M` | Branch 2A translation field satisfying `Phi=0` | no, because `Phi` is absent |
| `lambda_M` | Branch 2A multiplier | no, because `D_beta Phi` is absent |
| `U_M,P_IG,M` | Branch 3 dynamical IG fields | no, because `S_IG_dyn` is absent |
| `Psi_M` | zero vacuum spinor with no tadpole | conditionally fillable; must still be checked against `D_GU` |
| constants | `g_A,c_theta,alpha_W,kappa_eff,j_s` normalization | partially typed; not fully reduced |

### 5.3 Required Equations

Metric extraction:

```text
s_M^* g_Y = g_Schwarzschild(M).
```

Exact 4D GR target identity:

```text
Ric[g_Schwarzschild] = 0,
G[g_Schwarzschild] = 0.
```

Source equations, Branch 2A:

```text
E_A^2A = 0
E_s^2A = 0
E_beta^2A = 0
E_epsilon^2A = 0
E_lambda^2A = Phi = 0
E_Psi^2A = 0.
```

Source equations, Branch 3:

```text
E_A^3 = 0
E_s^3 = 0
E_U^3 = 0
E_P_IG^3 = 0       if first-order parent is used
E_epsilon^3 = 0
E_Psi^3 = 0.
```

Projection and vacuum residual:

```text
Pi_4D(E_source) =
  G_mu nu[g_M]
  + Lambda_eff g_mu nu
  - kappa_eff T_mu nu^shadow
  - R_mu nu^shadow
  = 0

exact vacuum Schwarzschild requires:
  Lambda_eff = 0
  T_mu nu^shadow = 0
  R_mu nu^shadow = 0.
```

### 5.4 What Can And Cannot Currently Be Filled

Can be filled now:

- `X_M = {r > 2M}` and the external Schwarzschild metric target.
- The statement `Ric[g_M]=0` and `G[g_M]=0`.
- The extraction form `g_M = s_M^* g_Y` as a typed requirement.
- Vacuum target values `T_matter=0`, `Lambda_eff=0`.
- The weak-field bounded compatibility citation from the canon, only inside `O(M/r)`
  scope.

Cannot be filled now:

- A source-selected `s_M` satisfying the full branch EL tuple.
- A Branch 2A `Phi`, tangent projector, multiplier, and conormal current.
- A Branch 3 `S_IG_dyn`, `J_IG`, and `theta_eff` solution.
- A finite-action `A_M` solving the connection equation.
- The exact cancellation:

  ```text
  alpha_W W_s(s_M)
    + E_s^YM
    + E_s^theta
    + E_s^Phi_or_IG_dyn
    + E_s^cross
    = 0.
  ```

- The projection identity with `R_shadow = 0`.
- The Noether/Bianchi projection that gives observer conservation.

Therefore the witness packet is specified but not filled.

## 6. First Exact Obstruction Or Missing Proof Object

The first exact missing proof object is:

```text
SchwarzschildMetricShadowExtractionTheorem(branch)
```

as the exact-Schwarzschild specialization of:

```text
MetricShadowExtractionTheorem(branch).
```

Its first child blocker is:

```text
ELProjectedGRShadowTheorem(branch, Schwarzschild).
```

The obstruction is branch-dependent:

| branch | first obstruction | why it comes first |
|---|---|---|
| Branch 2A | no sourced `Phi(epsilon,beta,s)=0` | without `Phi`, the beta tangent, multiplier equation, and unchanged source law are undefined |
| Branch 3 | no written `S_IG_dyn` and no `theta_eff` current | without the total-current action, nonzero theta has no honest source law |
| Willmore-only | `W_s(s_Schwarzschild) != 0` | exact Schwarzschild is not Willmore-critical in the current reading |
| free beta with only `|theta|^2` | `theta = 0` | the algebraic beta equation kills the advertised source |

The first exact obstruction for this assignment is not:

```text
Ric[g_Schwarzschild] != 0.
```

That is false; Schwarzschild is Ricci-flat. The obstruction is:

```text
No current branch supplies source fields satisfying the full source EL tuple whose
projection has R_shadow = 0.
```

Equivalently:

```text
Metric extraction is typed.
Metric-shadow selection is not proved.
```

Rollback language:

- If a future note claims Branch 2A but still lacks `Phi`, roll back to
  `conditional_template_only`.
- If `Phi` uses dynamic `A`, roll back Branch 2A to Branch 2B/source-corrected language.
- If Branch 3 is chosen but prose still cites `D_A^*F_A = theta`, roll back to total-current
  language with `theta_eff`.
- If exact Schwarzschild requires hidden matter, bare `Lambda`, or relabeled `Q^TF(B_s)`,
  the vacuum metric-shadow claim fails for that branch.
- If only the weak-field canon is used, keep the claim bounded to `O(M/r)` compatibility.

## 7. Constructive Next Object

The next object should not be another summary. It should be a fork-resolving construction:

```text
TauSliceOrBranch3SchwarzschildSourcePacket.
```

It has two allowed exits.

### Exit A: Prove A Fixed-Reference Branch 2A Slice

Construct:

```text
Phi_tau(epsilon,beta,s) =
  beta - beta_0(epsilon,s) = 0
```

where `beta_0` is built from fixed source geometry, for example a fixed-reference
tau-plus/Maurer-Cartan object using `Gamma(epsilon,s)` rather than the dynamical `A`.

Required proof fields:

```text
D_A Phi_tau = 0
D_beta Phi_tau = identity on the constrained graph normal
K_beta proper
gauge covariance of C_IG = {Phi_tau = 0}
anti-smuggling proof: no Schwarzschild/Kerr/FLRW target input
D_s Phi_tau contribution to E_s
```

If this closes, the next computation is the exact Branch 2A Schwarzschild source tuple:

```text
(E_A^2A,E_s^2A,E_beta^2A,E_epsilon^2A,E_lambda^2A,E_Psi^2A) = 0.
```

### Exit B: Write The Branch 3 Total-Current Action

If Exit A fails, stop trying to preserve the bare source law and write:

```text
S_IG_dyn[A,epsilon,U,P_IG;s]
```

with fixed coefficients and boundary terms. Then derive:

```text
J_IG = delta_A S_IG_dyn
theta_eff = g_A^2(c_theta theta - J_IG + branch-fixed corrections)
D_A^*F_A = theta_eff
D_A^*theta_eff = 0.
```

The first actual Schwarzschild computation in Branch 3 should reduce the source equations
under the static spherically symmetric exterior ansatz to a coupled ODE/PDE system for:

```text
A_M(r), U_M(r), P_IG,M(r), epsilon_M(r)
```

with:

```text
s_M^*g_Y = g_Schwarzschild(M)
finite action at infinity
regular exterior/horizon boundary behavior
E_s^3 = E_A^3 = E_U^3 = E_P_IG^3 = E_epsilon^3 = 0.
```

This is constructive because it creates a falsifiable object:

```text
Either the total current can cancel the exact Schwarzschild section residual with no hidden
matter, or Branch 3 fails exact Schwarzschild for the written action.
```

Kerr should wait. A rotating test is mandatory later, but Schwarzschild must first decide
whether any branch can fill one exact metric-shadow witness at all.

## 8. Claim Certificate Table And Machine-Readable Summary

| claim | status | proof grade | dependencies | closure condition | rollback condition | exact citation language |
|---|---|---|---|---|---|---|
| `SCHWARZSCHILD-METRIC-SHADOW-EXTRACTION` | `specified_not_filled` | reconstruction packet | `MetricShadowExtractionTheorem`, exact witness fields, full source EL tuple, projection identity | one branch supplies source fields with `s_M^*g_Y=g_Schw` and `R_shadow=0` | source fields absent, hidden matter needed, or only weak-field evidence supplied | "The exact Schwarzschild metric-shadow witness packet is specified but not yet filled." |
| `BRANCH-2A-SCHWARZSCHILD` | `conditional_template_only` | tangent theorem conditional | sourced A-independent `Phi`, proper `K_beta`, no target fitting | `Phi` is derived and exact Branch 2A EL tuple is solved | `Phi` missing, A-dependent, non-covariant, or engineered around Schwarzschild | "Branch 2A remains the conservative template, but it is not executable without a sourced `Phi`." |
| `BRANCH-3-TOTAL-CURRENT` | `required_fallback` | constructive specification | written `S_IG_dyn`, `J_IG`, `theta_eff`, conservation theorem | total-current action solves exact Schwarzschild source tuple | `S_IG_dyn` absent or bare-theta source language retained | "If Branch 2A cannot be sourced, exact Schwarzschild must be attempted in Branch 3 with `theta_eff`." |
| `WEAK-FIELD-SCHWARZSCHILD` | `bounded_compatibility` | canon scoped result | `canon/schwarzschild-weak-field-rfail.md` | no upgrade here; remains weak-field support | cited as exact nonlinear recovery | "Weak-field Schwarzschild compatibility remains bounded to the canon's `O(M/r)` scope." |
| `EXACT-GR-RECOVERY` | `not_claimed` | no promotion | Schwarzschild and Kerr witnesses from same branch, macroscopic limit | both exact witnesses and projection theorem close without imports | Schwarzschild packet unfilled, Kerr absent, hidden matter/imports used | "This artifact does not claim exact GR recovery." |

```json
{
  "artifact": "MISSION_A_METRIC_SHADOW_EXTRACTION_SCHWARZSCHILD",
  "version": "2026-06-24",
  "verdict": "BRANCH_2A_NOT_SOURCED_BRANCH_3_TOTAL_CURRENT_REQUIRED_EXACT_SCHWARZSCHILD_PACKET_SPECIFIED_NOT_FILLED",
  "mission": "Mission_A_GU_reconstruction",
  "theorem_target": "MetricShadowExtractionTheorem",
  "exact_target": "exact_Schwarzschild",
  "exact_gr_recovered": false,
  "metric_shadow_extraction_proved": false,
  "branch_2a": {
    "status": "conditional_template_only",
    "source_law_if_closed": "D_A^*F_A=theta",
    "required_phi": "Phi(epsilon,beta,s)=0",
    "requirements": [
      "primary_or_geometric_origin",
      "A_independent_D_A_Phi_zero",
      "gauge_covariant",
      "proper_beta_tangent_K_beta",
      "conormal_theta_survival_without_target_fitting",
      "D_s_Phi_contribution_accounted",
      "anti_smuggling"
    ],
    "available_sources": [
      {
        "candidate": "no_constraint_full_ig",
        "status": "fails_theta_collapse"
      },
      {
        "candidate": "a_independent_graph_beta_0",
        "status": "template_not_instantiated"
      },
      {
        "candidate": "fixed_reference_tau_plus",
        "status": "speculative_not_derived"
      },
      {
        "candidate": "dynamic_tau_plus_d_A",
        "status": "branch_2b_not_2a"
      },
      {
        "candidate": "section_pullback_codazzi",
        "status": "reduction_identity_not_ambient_beta_constraint"
      },
      {
        "candidate": "divergence_constraint",
        "status": "branch_2b_source_corrected"
      },
      {
        "candidate": "projector_subbundle",
        "status": "no_canonical_projector_in_sources"
      },
      {
        "candidate": "exact_schwarzschild_matching_filter",
        "status": "forbidden_target_fitting"
      }
    ],
    "current_failure": "no_D_beta_Phi_no_K_beta_no_lambda_no_E_s_Phi",
    "can_be_used_now": false
  },
  "branch_3": {
    "status": "required_constructive_fallback",
    "required_object": "S_IG_dyn_total_current",
    "source_law": "D_A^*F_A=theta_eff",
    "theta_eff": "g_A^2(c_theta_theta_minus_J_IG_plus_branch_fixed_corrections)",
    "conservation_target": "D_A^*theta_eff=0",
    "minimum_fields": [
      "U_or_beta",
      "P_IG_if_first_order",
      "A",
      "epsilon",
      "s",
      "Psi"
    ],
    "closure_condition": "derive_total_current_and_solve_exact_Schwarzschild_full_source_tuple",
    "rollback_condition": "S_IG_dyn_absent_or_bare_theta_source_language_retained"
  },
  "schwarzschild_witness_packet": {
    "status": "specified_not_filled",
    "domain": "r_greater_than_2M_exterior",
    "boundary_data": [
      "ADM_mass_M",
      "asymptotic_flatness",
      "finite_gauge_action",
      "section_variations_preserve_mass",
      "horizon_excision_or_regular_extension",
      "Lambda_eff_zero_unless_declared"
    ],
    "required_fields": [
      "s_M",
      "A_M",
      "F_A_M",
      "epsilon_M",
      "beta_M_or_U_M",
      "lambda_M_if_Branch_2A",
      "P_IG_M_if_Branch_3_first_order",
      "Psi_M_equals_0",
      "B_M_equals_II_s_H",
      "j_s_normalization"
    ],
    "required_equations": [
      "s_M_star_g_Y_equals_g_Schwarzschild",
      "E_A_equals_0",
      "E_s_equals_0",
      "E_IG_equals_0",
      "E_Psi_equals_0",
      "E_lambda_equals_0_if_constrained",
      "Pi_4D_E_source_equals_G_plus_Lambda_minus_kappa_T_minus_R_shadow",
      "R_shadow_equals_0"
    ],
    "currently_fillable": [
      "external_GR_metric_target",
      "Ricci_flat_identity",
      "vacuum_target_T_matter_zero",
      "Lambda_eff_zero_as_target",
      "weak_field_bounded_citation"
    ],
    "currently_missing": [
      "source_selected_section",
      "Branch_2A_Phi",
      "Branch_3_S_IG_dyn",
      "finite_action_A_M_solution",
      "section_residual_cancellation",
      "projection_identity",
      "Noether_Bianchi_projection"
    ]
  },
  "first_missing_proof_object": {
    "id": "SchwarzschildMetricShadowExtractionTheorem",
    "parent": "MetricShadowExtractionTheorem",
    "child_blocker": "ELProjectedGRShadowTheorem_Schwarzschild",
    "branch_2a_blocker": "Phi_not_sourced",
    "branch_3_blocker": "S_IG_dyn_total_current_not_written"
  },
  "constructive_next_object": {
    "id": "TauSliceOrBranch3SchwarzschildSourcePacket",
    "exit_A": "derive_fixed_reference_tau_slice_Phi_tau_for_Branch_2A",
    "exit_B": "write_Branch_3_S_IG_dyn_and_total_current_then_solve_static_spherical_source_tuple",
    "kerr_deferred": true
  },
  "claim_certificates": [
    {
      "id": "SCHWARZSCHILD-METRIC-SHADOW-EXTRACTION",
      "status": "specified_not_filled",
      "proof_grade": "reconstruction_packet",
      "closure_condition": "branch_source_fields_solve_full_EL_and_project_with_R_shadow_zero",
      "rollback_condition": "source_fields_absent_hidden_matter_needed_or_only_weak_field_evidence"
    },
    {
      "id": "BRANCH-2A-SCHWARZSCHILD",
      "status": "conditional_template_only",
      "proof_grade": "conditional_tangent_theorem",
      "closure_condition": "sourced_Phi_and_exact_Branch_2A_EL_solution",
      "rollback_condition": "Phi_missing_A_dependent_non_covariant_or_target_fitted"
    },
    {
      "id": "BRANCH-3-TOTAL-CURRENT",
      "status": "required_fallback",
      "proof_grade": "constructive_specification",
      "closure_condition": "S_IG_dyn_total_current_solves_exact_Schwarzschild",
      "rollback_condition": "S_IG_dyn_absent_or_theta_eff_not_used"
    },
    {
      "id": "WEAK-FIELD-SCHWARZSCHILD",
      "status": "bounded_compatibility",
      "proof_grade": "canon_scoped_result",
      "closure_condition": "no_exact_upgrade_in_this_artifact",
      "rollback_condition": "used_as_exact_nonlinear_recovery"
    },
    {
      "id": "EXACT-GR-RECOVERY",
      "status": "not_claimed",
      "proof_grade": "no_promotion",
      "closure_condition": "Schwarzschild_and_Kerr_witnesses_close_from_same_branch",
      "rollback_condition": "any_exact_recovery_claim_made_from_this_packet"
    }
  ],
  "rollback_conditions": [
    "Branch_2A_without_Phi",
    "Phi_A_dependent_so_Branch_2B",
    "Phi_target_fitted_to_Schwarzschild_or_Kerr",
    "Branch_3_without_theta_eff",
    "S_IG_dyn_absent",
    "hidden_matter_or_Q_TF_relabeling_required",
    "bare_Lambda_or_Einstein_Hilbert_rescue_inserted",
    "weak_field_promoted_to_exact",
    "projection_identity_missing",
    "R_shadow_nonzero_in_vacuum"
  ],
  "forbidden_claims": [
    "exact_GR_recovered",
    "exact_Schwarzschild_metric_shadow_proved",
    "Branch_2A_accepted_without_Phi",
    "bare_theta_conserved_in_Branch_3",
    "weak_field_pass_is_exact_black_hole_recovery"
  ],
  "next_step": "build_TauSliceOrBranch3SchwarzschildSourcePacket_before_Kerr"
}
```

## Sources Read

- `RESEARCH-POSTURE.md`
- `process/runbooks/five-lane-frontier-run.md`
- `explorations/metric-marble-prematurity-gate-2026-06-24.md`
- `explorations/gr-shadow-recovery-certificate-2026-06-24.md`
- `explorations/exact-schwarzschild-kerr-el-gate-2026-06-24.md`
- `explorations/constraint-first-ig-tangent-space-gate-2026-06-24.md`
- `explorations/gu-action-4d-physics-gate-2026-06-24.md`
- `explorations/gu-minimal-action-spec-2026-06-24.md`
- `canon/schwarzschild-weak-field-rfail.md`
