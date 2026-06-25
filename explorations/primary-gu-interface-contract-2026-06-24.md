---
title: "Primary GU Interface Contract"
date: "2026-06-24"
status: exploration/interface_contract
doc_type: primary_gu_interface_contract
verdict: "CONTRACT_TYPED_FOR_CITATION_GOVERNANCE; PRIMARY_ACTION_STILL_UNDERDEFINED"
owned_path: "explorations/primary-gu-interface-contract-2026-06-24.md"
audit_script: "tests/primary_gu_interface_contract_audit.py"
depends_on:
  - "explorations/all-persona-wall-break-steelman-hegelian-2026-06-24.md"
  - "process/runbooks/five-lane-frontier-run.md"
  - "explorations/goal-draft-primary-gu-action-operator-spec-2026-06-24.md"
  - "explorations/gu-typed-operator-action-spine-2026-06-24.md"
  - "explorations/gu-minimal-action-spec-2026-06-24.md"
  - "explorations/gu-closed-loop-action-ig-branch-2026-06-24.md"
  - "explorations/gu-action-4d-physics-gate-2026-06-24.md"
  - "explorations/vz-proof-grade-closure-attempt-2026-06-24.md"
  - "explorations/exact-schwarzschild-kerr-el-gate-2026-06-24.md"
  - "explorations/flrw-theta-xi-branch-reduction-2026-06-24.md"
  - "explorations/y14-k3-index-bridge-theorem-or-nogo-2026-06-24.md"
  - "explorations/sm-gauge-higgs-finite-control-extraction-ledger-2026-06-24.md"
  - "explorations/live-claim-dag-fault-finality-ledger-2026-06-24.md"
---

# Primary GU Interface Contract

## 1. Verdict

`I_GU` can be typed as an interface contract now, but not as a proof-grade primary theory.
The contract is strong enough to decide citation language for the live claims:

```text
I_GU =
  (fields, variations, gauge group, D_GU, S_GU,
   section map, source law, boundary conditions, reduction functor).
```

The current repo has one typed operator spine and several action/IG branch variants. It
does not yet have one source-closed primary action/operator object. Therefore:

```text
VZ: typed and conditionally closed only on the operator-spine branch with Phi_d.
exact GR: blocked for every viable branch; Willmore-only and bare-free-beta fail.
theta-xi: no branch generates negative xi_eff; bare free beta kills theta.
Y14/K3 index: conditional bridge shape only; physical RS complex is underdefined.
SM finite control: Pati-Salam branch/host typed; finite selector blocked.
observer/CHSH: formal controls typed; GU-derived rho_AB and observables absent.
```

This is a citation contract, not a glossary. Underdefinition below is a type/interface
error: a claim may cite only the branch that supplies the typed objects it consumes.

## 2. Minimal Typed Interface Fields And Maps

### 2.1 Carrier fields

The minimal carrier is:

```text
X                         smooth oriented 4-manifold
Y = Met_Lor(X)             14D metric bundle over X
g_Y                       fixed gimmel metric, signature (9,5), in baseline
G                         Sp(64)
P -> Y                    principal G-bundle
S = S^+ plus S^-           quaternionic spinor bundle, rank_H(S)=64
Phi_2                     fixed zero-order algebraic shiab map
s: X -> Y                  section, physical metric g = s^*g_Y
A                         Sp(64) connection on P
F_A                       curvature of A
epsilon                   IG/gauge variable
beta                      IG translation field in Omega^1(Y, ad P)
theta                     A - Gamma(epsilon) - Ad(epsilon^-1) beta
Psi                       spinor/form-spinor field
B_s = II_s^H              horizontal-normalized section second fundamental form
j_s                       normal-to-ad(P_s) soldering map with explicit normalization
```

Optional branch fields are:

```text
lambda                    multipliers for constrained IG branches
U = Ad(epsilon^-1) beta    dynamical IG variable in Branch 3
P_IG                      first-order IG momentum in Branch 3
```

### 2.2 Variation contract

The baseline variation status is:

| object | type role | variation status |
|---|---|---|
| `X`, `Y`, `g_Y`, `P`, `S`, `Phi_2` | carrier data | fixed in the current baseline |
| `s` | section/4D metric | varied for 4D gates |
| `A` | connection | varied |
| `F_A`, `theta`, `B_s` | derived fields | vary through parents |
| `Psi` | spinor/form-spinor | varied; vacuum may set `Psi=0` only after consistency |
| `epsilon`, `beta` | IG data | branch-dependent; never silently free if nonzero theta is claimed |
| `lambda`, `U`, `P_IG` | branch fields | present only in the corresponding branch |

The binding type rule is:

```text
free beta + only S_theta = -c_theta/2 int |theta|^2
  => E_beta = c_theta Ad(epsilon) theta = 0
  => theta = 0.
```

Any branch that cites nonzero theta, theta dark energy, or the bare source law must either
remove free beta variations, constrain them, or replace the source with a total current.

### 2.3 Gauge group

The gauge group is the vertical principal automorphism group of `P -> Y` with structure
group `Sp(64)`, together with the usual diffeomorphism covariance of the section map. The
contract requires every branch constraint, source law, and reduction map to be equivariant
under the local `Sp(64)` action. A Stueckelberg/background branch may transform
`epsilon,beta` as spurions, but then omitted variations carry a Noether cost.

### 2.4 Operator `D_GU`

The only currently typed candidate for the relevant 0/1 sector is the operator-spine block:

```text
D_lambda^eta:
  Gamma(S^eta plus T^*Y tensor S^-eta)
    -> Gamma(S^-eta plus T^*Y tensor S^eta)

D_lambda(u, psi)
  =
  (d_A^* psi, d_A u + lambda_d Phi_2(d_A psi))
  + Z_A(u, psi).
```

Its principal symbol is:

```text
sigma_1(D_lambda)(xi)(u,psi)
  =
  (i_xi psi, xi tensor u + lambda_d F_xi psi),

F_xi = sigma_1(Phi_2 o d_A)(xi).
```

The coefficient `lambda_d` is load-bearing:

```text
lambda_d = 1       typed-spine proposal; current VZ arithmetic applies.
lambda_d != 1      VZ coefficients must be rederived.
lambda_d = 0       the current VZ route fails for the primary operator.
```

The lower-order ledger `Z_A` must contain all connection coefficients, spin/gimmel terms,
mass terms, gauge-fixing terms, `Phi_F(A)`, curvature insertions, theta/IG terms,
section-pullback terms, and boundary data. None of those terms may be used as the
first-order VZ `F_xi` block.

### 2.5 Action `S_GU`

The minimal action contract is:

```text
S_GU[s,A,epsilon,beta,Psi; branch]
  =
  S_YM[A]
  + S_DD[A,Psi;D_GU]
  + S_theta[A,epsilon,beta]
  + S_W[s]
  + S_IG[branch]
  + S_cross[primary-sourced only]
  + S_boundary.
```

Baseline terms:

```text
S_YM     = -1/(4 g_A^2) int_Y <F_A,F_A>
S_DD     = int_Y <Psi, D_GU(A) Psi>
S_theta  = -c_theta/2 int_Y <theta,theta>
S_W      = alpha_W/2 int_X |II_s^H|^2
```

Excluded from the baseline unless primary-sourced with fixed coefficients:

```text
bare R[g] theta^2
bare Lambda
theta * D_A^*F_A
D_A theta * F_A
torsion/theta invariants with free coefficients
terms introduced because Schwarzschild, Kerr, xi_eff, or n=3 need them
```

The full Euler-Lagrange tuple required for 4D physics is:

```text
(E_s, E_A, E_epsilon, E_beta, E_Psi) = 0
```

plus `E_lambda=0` in constrained branches or `E_U,E_P_IG=0` in dynamical branches.

### 2.6 Section map and reduction functor

The section map is:

```text
s^*: fields on Y -> fields on X
```

with:

```text
g = s^*g_Y
P_s = s^*P
S_s = s^*S
A_s = s^*A
theta_s = s^*theta
B_s = II_s^H
```

The reduction functor is not one map. It is the tuple:

```text
R_GU =
  (R_VZ, R_4D, R_FLRW, R_RS, R_SM, R_OBS).
```

Each component has a typed output:

| component | input it may use | output type |
|---|---|---|
| `R_VZ` | `sigma_1(D_GU)` and Q-sector split | non-null 14D/4D principal-symbol decision |
| `R_4D` | `S_GU`, `s^*`, boundary data | full 4D vacuum EL tuple |
| `R_FLRW` | written branch action and scalar projection | `Z_theta`, `C_Rtheta`, `xi_eff = C_Rtheta/Z_theta` |
| `R_RS` | physical gauge-fixed RS complex from `D_GU` | `H`-linear Fredholm/K3/APS index decision |
| `R_SM` | carrier plus selector/shadow functor | finite-control status: derive/host/import/fail |
| `R_OBS` | zero modes/two-point state plus measurement postulate | `rho_AB`, admissible observables, CHSH value |

### 2.7 Boundary conditions

Boundary data are part of the type:

| gate | required boundary/domain data |
|---|---|
| VZ | local covectors with `q = g_Y(xi,xi) != 0`; no boundary needed for principal symbol |
| exact GR | Schwarzschild/Kerr exterior domains, ADM mass, Kerr angular momentum, finite gauge/action data |
| FLRW | endpoint/cosmological boundary convention and scalar normalization |
| Y14/K3 | weighted noncompact Sobolev domain, tau-discrete projection, or APS boundary operator |
| SM finite control | no target finite algebra, gauge group, Higgs, or `n=3` in the input |
| observer/CHSH | local Alice/Bob split, NAC/local commutativity, trace-one positive finite state |

## 3. Branch Variants And What Each Branch Owns

| branch key | definition | owns | does not own |
|---|---|---|---|
| `operator_spine` | `D_lambda` typed; `lambda_d=1` in proposal; no full action closure | VZ principal-symbol typing; input surface for RS/CHSH state searches | exact GR, theta-xi, source law, physical RS index, SM selector, `rho_AB` |
| `background_stueckelberg` | `delta epsilon = delta beta = 0` | nonzero theta allowed; bare source can survive after normalization | Noether cost, exact GR, generated `xi_eff`, physical selector/state |
| `constrained_ig_a_independent` | `Phi(epsilon,beta,s)=0`, `D_A Phi=0` | strongest conservative source branch: `D_A^*F_A = theta`; nonzero theta if tangent space is not full beta | primary sourcing of `Phi`, full `E_s`, `xi_eff`, exact black holes |
| `constrained_ig_a_dependent` | `Phi(A,epsilon,beta,s)=0` | constrained nonzero theta with multiplier current | bare source law; source is corrected by `(D_A Phi)^*lambda` |
| `dynamical_ig_total_current` | dynamical `U` or first-order `P_IG` | honest dynamical theta/IG route; possible scalar kinetics | bare theta source; source must be `theta_eff` and `S_IG-dyn` is unwritten |
| `bare_free_beta_norm` | free `beta`, only `|theta|^2` IG term | the negative result `theta=0` | nonzero theta, theta dark energy, bare source equation |

## 4. Claim-To-Branch Compatibility Table

Legend: `typed` means the branch supplies the typed object; `conditional` means it
type-checks only under named upstream closure; `branch-local` means it is a local host or
control, not a primary derivation; `blocked` means a required object is missing; `invalid`
means the branch contradicts the claim.

| claim | `operator_spine` | `background_stueckelberg` | `constrained_ig_a_independent` | `constrained_ig_a_dependent` | `dynamical_ig_total_current` | `bare_free_beta_norm` |
|---|---|---|---|---|---|---|
| VZ principal symbol | typed: closes for `lambda_d != 0`; GU still conditional | conditional on same `D_GU` | conditional on same `D_GU` | conditional on same `D_GU` | conditional on same `D_GU` | conditional on same `D_GU`, though source branch fails |
| exact Schwarzschild/Kerr | blocked: no full action | blocked: full `E_s` not solved | blocked: recommended branch, `Phi` missing | blocked: multiplier/source branch missing | blocked: `S_IG-dyn` and total-current solution missing | invalid/fail: theta killed and Willmore residual remains |
| FLRW theta-xi | blocked: no action/reduction | blocked: no `Z_theta` or `C_Rtheta` | blocked: scalar direction and coefficients undefined | blocked: multiplier coefficients undefined | blocked: strongest route, but `S_IG-dyn` absent | invalid: theta scalar absent |
| Y14/K3 index | conditional typed input for physical RS symbol | blocked: physical RS complex and bridge missing | blocked: physical RS complex and bridge missing | blocked: physical RS complex and bridge missing | blocked: physical RS complex and bridge missing | blocked: physical RS complex and bridge missing |
| SM finite control | branch-local: Pati-Salam packet/host only | branch-local host; selector absent | branch-local host; selector absent | branch-local host; selector absent | branch-local host; selector absent | branch-local host; selector absent |
| observer/CHSH | blocked: representation spaces only; no `rho_AB` | blocked: no state/measurement channel | blocked: no state/measurement channel | blocked: no state/measurement channel | blocked: possible future state source, underdefined | blocked: Bell ansatz still not GU-derived |

## 5. Claim Certificate Table

| claim | proof grade | dependencies | forbidden inputs | rollback condition | exact citation language |
|---|---|---|---|---|---|
| VZ 14D principal-symbol gate | conditional_reconstruction | `D_GU` contains `Phi_d = Phi_2 o d_A` with `lambda_d != 0`; Q-sector split; non-null `q`; coefficient convention | zero-order `Phi_F` as `F_xi`; untyped `D_GU`; coefficient drift; determinant-only E-block proof | primary operator lacks `Phi_d`, has `lambda_d=0`, or changes coefficient without rederivation | "Relative to the typed-spine operator with nonzero `Phi_d` (lambda_d=1 in the proposal), the 14D non-null principal-symbol Schur gate closes; the primary GU VZ claim remains conditional until `D_GU` is source-closed." |
| exact Schwarzschild/Kerr recovery | specification/open | written `S_GU`; IG variation branch; full EL tuple; `II_s^H`; boundary data | weak-field `O(M/r)` as exact recovery; hidden matter relabeling; unspecified cross terms; free beta with nonzero theta | either Schwarzschild or Kerr fails the full vacuum EL tuple, or the branch needs unspecified terms | "Exact Schwarzschild/Kerr recovery is open and blocked by the full action/IG variation; the weak-field Schwarzschild result remains bounded to its stated reconstruction scope." |
| FLRW theta `xi_eff` | conditional_reconstruction | written branch action; scalar `s^*theta`; `Z_theta`; `C_Rtheta`; canonical `xi_eff`; generated coefficient | hand-inserted `xi ~= -0.6`; bare `R theta^2` without primary source; applying scalar KG if the mode is not scalar; free-beta branch | `xi_eff >= -0.319`, no scalar mode, no `R B^2` term, or coefficient depends on unspecified `S_IG-dyn` | "The DESI-sign theta mechanism requires `xi_eff < -0.319`; no current GU branch has generated that coefficient." |
| Y14/K3 physical RS index | contract_only/conditional_theorem | physical GU RS complex; nonempty bounded tau-discrete projection; weighted Fredholm package; K3/APS bridge; right-H family; `ch_2(F)` | raw K3 RS index as physical index; target `ind_H=8`; total index `24`; three_generations; complex index halved without H certificate | missing bridge condition, background-dependent `k`, non-Fredholm sector, wrong APS operator, or other computed index | "The K3 RS calculation is a compact control until the physical GU RS complex and Y14-to-K3 bridge are proved; generation count remains open." |
| SM finite-control package | reconstruction/negative_filter | fixed selector/shadow functor; Pati-Salam-to-SM selection; finite algebra/gauge quotient; Higgs projection; anomaly shadow | importing `A_F`; importing `G_SM`; choosing `n=3`; `C_n` cardinality transport; ambient Higgs slot as physical Higgs | selector imports rather than derives, replacement test works for `n != 3`, or extra observer modes remain anomalous | "The typed GU carrier derives a Pati-Salam one-generation representation branch and hosts Higgs quantum numbers; it does not derive the full SM finite-control package." |
| observer/CHSH physical forcing | executable_control | GU-derived `rho_AB`; finite reduction map; GU-admissible +/-1 observables; NAC/local commutativity | copying Bell control into GU slot; Pati-Salam labels as a state; generic vacuum entanglement as finite density matrix; Pauli settings without measurement postulate | derived state is separable, all admissible settings have `CHSH <= 2`, or violation comes only from ansatz/control state | "The Pati-Salam CHSH fixture has strong controls and ansatz states, but GU physical forcing is open until GU supplies `rho_AB` and admissible observables." |

## 6. Branch Robustness Table

| claim/object | primary | branch-local-natural | branch-local-engineered | absent | underdefined |
|---|---|---|---|---|---|
| `D_lambda` VZ principal block | no: proposal only | yes, if primary `D_GU` contains `Phi_d` | yes if coefficient chosen only to preserve old arithmetic | yes if `lambda_d=0` | coefficient/source provenance |
| Branch 2A IG source law | no | yes if `Phi(epsilon,beta,s)` is forced by GU geometry | yes if constraint is invented to save theta | no constraint means no branch | `Phi` and tangent space |
| Branch 3 total current | no | yes if `S_IG-dyn` is written naturally | yes if potential/couplings are fitted to targets | absent in current action | `S_IG-dyn`, `J_IG`, source law |
| exact Schwarzschild/Kerr | no | possible only after full EL solution | engineered if cross terms are fitted to black holes | Willmore-only/free-beta branches fail | full `E_s,E_A,E_IG` |
| FLRW negative `xi_eff` | no | possible in Branch 3 or sourced Branch 2A after reduction | engineered if `xi` is inserted or tuned | absent in Branch 4 | `Z_theta`, `C_Rtheta`, scalar mode |
| Y14/K3 index bridge | no | natural theorem shape with physical RS complex and bridge | engineered if ghost/APS data are chosen for index target | raw K3 is not physical index | physical symbol, projection, bridge |
| SM finite control | no | Pati-Salam branch and Higgs-slot host | `C_n`, fixed CC import, chosen `n=3` | positive selector absent | fixed-data selector/shadow |
| observer/CHSH | no | finite Pati-Salam control fixture | Bell state copied into GU slot | GU-derived state absent | zero modes/two-point map and measurement postulate |

## 7. First Exact Obstruction Or Type Error

The first exact type error is the free-beta branch:

```text
S_theta = -c_theta/2 int_Y <theta,theta>
theta = A - Gamma(epsilon) - Ad(epsilon^-1) beta
delta_beta arbitrary
```

implies:

```text
E_beta = c_theta Ad(epsilon) theta = 0,
theta = 0.
```

Therefore a branch cannot simultaneously have:

```text
beta freely varied,
only the bare theta norm as IG action,
nonzero theta,
D_A^*F_A = theta,
theta-FLRW dark energy.
```

That obstruction propagates into the interface:

```text
source_law(I_GU) is not a single field equation until variation_space(epsilon,beta)
and S_IG are fixed.
```

The second obstruction is operator provenance:

```text
VZ may cite only a `D_GU` whose first-order 0/1 block contains Phi_d.
```

If the primary operator contains only `Phi_F(A)`, the current VZ `F_xi` block is not the
primary operator's block.

## 8. Next Meaningful Proof/Computation Step

The next step is not another global summary. It is a branch-closing proof packet:

1. Try Branch 2A first:

   ```text
   derive Phi(epsilon,beta,s)=0,
   prove D_A Phi = 0,
   prove T C_IG does not contain all beta variations,
   derive the multiplier equations.
   ```

   If this fails, switch explicitly to Branch 3.

2. If Branch 3 is needed, write `S_IG-dyn` and replace the source language everywhere:

   ```text
   D_A^*F_A = theta_eff,
   theta_eff = g_A^2(c_theta theta - J_IG + ...).
   ```

3. With one branch fixed, compute the full EL tuple and run Schwarzschild before Kerr:

   ```text
   E_s = E_A = E_IG = E_Psi = 0
   ```

   in the `II_s^H` and `j_s` normalization.

4. On the same branch, reduce FLRW to the quadratic scalar action and compute:

   ```text
   Z_theta,
   C_Rtheta,
   xi_eff = C_Rtheta / Z_theta.
   ```

5. In parallel only after `D_GU` is primary-sourced, derive the physical RS complex for
   `R_RS`, and only then attempt the Y14/K3 bridge.

6. For observer/CHSH, do not reuse the Bell control. Define the GU measurement channel:

   ```text
   zero modes / two-point function -> rho_AB -> admissible +/-1 observables.
   ```

   Then run the existing CHSH fixture.

## Machine-Readable Contract

```json
{
  "version": "2026-06-24",
  "interface": {
    "name": "I_GU",
    "required_slots": [
      "fields",
      "variations",
      "gauge_group",
      "operator_D_GU",
      "action_S_GU",
      "section_map",
      "source_law",
      "boundary_conditions",
      "reduction_functor"
    ],
    "required_fields": [
      "X",
      "Y",
      "g_Y",
      "P",
      "S",
      "Phi_2",
      "s",
      "A",
      "F_A",
      "epsilon",
      "beta",
      "theta",
      "Psi",
      "II_s_H"
    ]
  },
  "status_enum": [
    "typed",
    "conditional",
    "branch-local",
    "blocked",
    "invalid",
    "underdefined"
  ],
  "branch_keys": [
    "operator_spine",
    "background_stueckelberg",
    "constrained_ig_a_independent",
    "constrained_ig_a_dependent",
    "dynamical_ig_total_current",
    "bare_free_beta_norm"
  ],
  "branches": [
    {
      "key": "operator_spine",
      "variation_rule": "action_not_closed",
      "source_law": "none",
      "current_status": "typed_operator_proposal",
      "owns": ["VZ_principal_symbol_typing"]
    },
    {
      "key": "background_stueckelberg",
      "variation_rule": "delta_epsilon_delta_beta_zero",
      "source_law": "D_A_star_F_A_equals_theta_after_normalization",
      "current_status": "viable_but_thin",
      "owns": ["nonzero_theta_allowed", "bare_source_possible"]
    },
    {
      "key": "constrained_ig_a_independent",
      "variation_rule": "Phi_epsilon_beta_s_equals_zero_D_A_Phi_zero",
      "source_law": "D_A_star_F_A_equals_theta",
      "current_status": "recommended_but_Phi_missing",
      "owns": ["nonzero_theta_if_constraint_real", "bare_source_conservative_branch"]
    },
    {
      "key": "constrained_ig_a_dependent",
      "variation_rule": "Phi_A_epsilon_beta_s_equals_zero",
      "source_law": "corrected_by_multiplier_current",
      "current_status": "possible_but_source_rewritten",
      "owns": ["constrained_nonzero_theta"]
    },
    {
      "key": "dynamical_ig_total_current",
      "variation_rule": "epsilon_beta_or_U_dynamical_with_S_IG_dyn",
      "source_law": "D_A_star_F_A_equals_theta_eff",
      "current_status": "honest_fallback_but_S_IG_dyn_missing",
      "owns": ["possible_dynamic_scalar", "total_current_language"]
    },
    {
      "key": "bare_free_beta_norm",
      "variation_rule": "free_beta_with_only_theta_norm",
      "source_law": "D_A_star_F_A_equals_zero",
      "current_status": "invalid_for_nonzero_theta",
      "owns": ["theta_zero_no_nonzero_source"]
    }
  ],
  "claim_keys": [
    "VZ",
    "EXACT_GR",
    "THETA_XI",
    "Y14_K3_INDEX",
    "SM_FINITE_CONTROL",
    "OBSERVER_CHSH"
  ],
  "compatibility": {
    "operator_spine": {
      "VZ": "typed",
      "EXACT_GR": "blocked",
      "THETA_XI": "blocked",
      "Y14_K3_INDEX": "conditional",
      "SM_FINITE_CONTROL": "branch-local",
      "OBSERVER_CHSH": "blocked"
    },
    "background_stueckelberg": {
      "VZ": "conditional",
      "EXACT_GR": "blocked",
      "THETA_XI": "underdefined",
      "Y14_K3_INDEX": "underdefined",
      "SM_FINITE_CONTROL": "branch-local",
      "OBSERVER_CHSH": "blocked"
    },
    "constrained_ig_a_independent": {
      "VZ": "conditional",
      "EXACT_GR": "blocked",
      "THETA_XI": "underdefined",
      "Y14_K3_INDEX": "underdefined",
      "SM_FINITE_CONTROL": "branch-local",
      "OBSERVER_CHSH": "blocked"
    },
    "constrained_ig_a_dependent": {
      "VZ": "conditional",
      "EXACT_GR": "blocked",
      "THETA_XI": "underdefined",
      "Y14_K3_INDEX": "underdefined",
      "SM_FINITE_CONTROL": "branch-local",
      "OBSERVER_CHSH": "blocked"
    },
    "dynamical_ig_total_current": {
      "VZ": "conditional",
      "EXACT_GR": "blocked",
      "THETA_XI": "underdefined",
      "Y14_K3_INDEX": "underdefined",
      "SM_FINITE_CONTROL": "branch-local",
      "OBSERVER_CHSH": "blocked"
    },
    "bare_free_beta_norm": {
      "VZ": "conditional",
      "EXACT_GR": "invalid",
      "THETA_XI": "invalid",
      "Y14_K3_INDEX": "underdefined",
      "SM_FINITE_CONTROL": "branch-local",
      "OBSERVER_CHSH": "blocked"
    }
  },
  "certificates": [
    {
      "claim": "VZ",
      "proof_grade": "conditional_reconstruction",
      "dependencies": ["D_GU_has_Phi_d", "lambda_d_nonzero", "Q_sector_split", "non_null_q"],
      "forbidden_inputs": ["Phi_F_as_F_xi", "untyped_D_GU", "coefficient_drift", "determinant_only_E_block"],
      "rollback_condition": "primary_D_GU_lacks_Phi_d_or_lambda_d_zero_or_changed_without_rederivation",
      "citation_language": "Relative to the typed-spine operator with nonzero Phi_d, the 14D non-null Schur gate closes; primary GU VZ remains conditional."
    },
    {
      "claim": "EXACT_GR",
      "proof_grade": "specification_open",
      "dependencies": ["written_S_GU", "IG_variation_branch", "full_EL_tuple", "II_s_H", "black_hole_boundary_data"],
      "forbidden_inputs": ["weak_field_as_exact", "hidden_matter_relabeling", "unspecified_cross_terms", "free_beta_nonzero_theta"],
      "rollback_condition": "Schwarzschild_or_Kerr_fails_full_vacuum_EL_tuple",
      "citation_language": "Exact Schwarzschild/Kerr recovery is open; weak-field Schwarzschild remains bounded to its stated reconstruction scope."
    },
    {
      "claim": "THETA_XI",
      "proof_grade": "conditional_reconstruction",
      "dependencies": ["written_branch_action", "scalar_theta_mode", "Z_theta", "C_Rtheta", "xi_eff_canonical"],
      "forbidden_inputs": ["xi_minus_0_6_inserted", "bare_Rtheta_without_primary_source", "non_scalar_mode", "free_beta_branch"],
      "rollback_condition": "xi_eff_ge_minus_0_319_or_no_scalar_mode_or_no_generated_RB2_term",
      "citation_language": "No current GU branch has generated the negative xi_eff required by the DESI-sign theta mechanism."
    },
    {
      "claim": "Y14_K3_INDEX",
      "proof_grade": "contract_only_conditional_theorem",
      "dependencies": ["physical_RS_complex", "P_disc", "weighted_Fredholm", "K3_or_APS_bridge", "right_H_family", "ch2_F"],
      "forbidden_inputs": ["raw_K3_as_physical", "ind_H_8_target", "total_index_24", "three_generations", "complex_index_halved_without_H"],
      "rollback_condition": "missing_bridge_or_nonFredholm_or_background_dependent_or_wrong_APS_or_other_index",
      "citation_language": "K3 is a compact control until the physical GU RS complex and Y14-to-K3 bridge are proved; generation count remains open."
    },
    {
      "claim": "SM_FINITE_CONTROL",
      "proof_grade": "reconstruction_negative_filter",
      "dependencies": ["fixed_selector_shadow", "Pati_Salam_selection", "finite_algebra_or_gauge_quotient", "Higgs_projection", "anomaly_shadow"],
      "forbidden_inputs": ["A_F_import", "G_SM_import", "n_equals_3_choice", "C_n_cardinality_transport", "ambient_Higgs_slot_as_physical"],
      "rollback_condition": "selector_imports_target_or_replacement_test_passes_for_other_n_or_extra_modes_anomalous",
      "citation_language": "The typed GU carrier derives a Pati-Salam one-generation representation branch and hosts Higgs quantum numbers; full SM finite control is not derived."
    },
    {
      "claim": "OBSERVER_CHSH",
      "proof_grade": "executable_control",
      "dependencies": ["GU_derived_rho_AB", "finite_reduction_map", "GU_admissible_observables", "NAC_local_commutativity"],
      "forbidden_inputs": ["Bell_control_copied_into_GU", "Pati_Salam_labels_as_state", "generic_vacuum_entanglement_as_finite_density_matrix", "Pauli_settings_without_measurement_postulate"],
      "rollback_condition": "derived_state_separable_or_all_admissible_settings_CHSH_le_2_or_violation_only_ansatz",
      "citation_language": "Pati-Salam CHSH controls are strong, but GU physical forcing is open until GU supplies rho_AB and admissible observables."
    }
  ]
}
```

## Sources Read

- `explorations/all-persona-wall-break-steelman-hegelian-2026-06-24.md`
- `process/runbooks/five-lane-frontier-run.md`
- `explorations/goal-draft-primary-gu-action-operator-spec-2026-06-24.md`
- `explorations/gu-typed-operator-action-spine-2026-06-24.md`
- `explorations/gu-minimal-action-spec-2026-06-24.md`
- `explorations/gu-closed-loop-action-ig-branch-2026-06-24.md`
- `explorations/gu-action-4d-physics-gate-2026-06-24.md`
- `explorations/vz-proof-grade-closure-attempt-2026-06-24.md`
- `explorations/exact-schwarzschild-kerr-el-gate-2026-06-24.md`
- `explorations/flrw-theta-xi-branch-reduction-2026-06-24.md`
- `explorations/y14-k3-index-bridge-theorem-or-nogo-2026-06-24.md`
- `explorations/sm-gauge-higgs-finite-control-extraction-ledger-2026-06-24.md`
- `explorations/live-claim-dag-fault-finality-ledger-2026-06-24.md`
- `explorations/observer-finality-physical-forcing-gate-2026-06-24.md`
- `explorations/observer-finality-gu-derived-chsh-state-attempt-2026-06-24.md`
