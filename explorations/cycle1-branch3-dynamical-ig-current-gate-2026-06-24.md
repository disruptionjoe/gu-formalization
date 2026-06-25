---
title: "Cycle 1 Branch 3 Dynamical IG Total-Current Source Gate"
date: "2026-06-24"
status: exploration/gate
doc_type: cycle1_branch3_dynamical_ig_current_gate
verdict: "UNDERDEFINED_FIRST_MISSING_OBJECT_IS_SOURCE_FORCED_S_IG_DYN"
owned_path: "explorations/cycle1-branch3-dynamical-ig-current-gate-2026-06-24.md"
optional_audit: "tests/cycle1_branch3_dynamical_ig_current_audit.py"
depends_on:
  - "RESEARCH-POSTURE.md"
  - "process/runbooks/five-lane-frontier-run.md"
  - "explorations/mission-a-lambda-dark-energy-provenance-2026-06-24.md"
  - "explorations/ig-dynamics-nonzero-theta-action-gate-2026-06-24.md"
  - "explorations/dark-energy-assumption3-variational-2026-06-23.md"
  - "explorations/gu-minimal-action-spec-2026-06-24.md"
  - "explorations/gu-closed-loop-action-ig-branch-2026-06-24.md"
---

# Cycle 1 Branch 3 Dynamical IG Total-Current Source Gate

## 1. Verdict

Verdict:

```text
UNDERDEFINED.
```

Branch 3 cannot yet be promoted from `strongest_candidate_open` to a conditional theorem.
The repo contains a coherent theorem schema for a dynamical IG / total-current branch, but
not the first proof object needed to instantiate that schema:

```text
source-forced S_IG_dyn[A, eps, U or beta, optional P_IG, s]
```

The current notes give representative Branch 3 action shapes and the expected source-law
rewrite. They do not identify a primary or geometry-forced dynamic IG action with fixed
normalization, potential, current, boundary terms, section dependence, or reduction data.
Therefore the gate remains underdefined before the source current, `theta_eff`, conservation
identity, `Z_theta`, `C_Rtheta`, or `xi_eff` can be promoted.

Mission A posture applies: assume the GU reconstruction is worth pursuing and build the
missing object if possible, while preserving rollback conditions. This artifact does not
claim that GU derives Lambda, cancels Lambda, solves dark energy, or derives the observed
dark-energy sector.

Status in one line:

```text
Branch 3 is the strongest current dynamic route, but its total-current theorem is only a
contract until S_IG_dyn is written and shown source-forced.
```

## 2. What Was Derived Directly From Repo Sources

The following items are directly supported by the required sources.

1. The minimal theta norm with free independent `beta` fails for nonzero theta:

   ```text
   theta = A - Gamma(eps) - Ad(eps^-1) beta
   delta_beta S_theta = 0  =>  theta = 0
   ```

   This is the load-bearing result from the IG dynamics gate and the closed-loop branch gate.

2. If `eps,beta` are fixed or constrained, a bare source equation can be kept in some branches,
   but that is not Branch 3:

   ```text
   D_A^* F_A = theta
   ```

   Branch 2A is currently the recommended conservative branch because an A-independent
   constraint could preserve this equation. Its first missing object is a real
   `Phi(eps,beta,s)=0`.

3. Branch 3 is the honest dynamical branch because it replaces the algebraic beta collapse
   by a differential IG equation. With

   ```text
   U = Ad(eps^-1) beta
   theta = A - Gamma(eps) - U,
   ```

   the source law is not generically the bare theta law. It becomes a total-current law:

   ```text
   D_A^* F_A = theta_eff,
   theta_eff = g_A^2(c_theta theta - J_IG)
   ```

   up to sign and normalization conventions fixed by the written action.

4. The first-order parent form makes the current obstruction explicit:

   ```text
   S_IG_dyn,parent =
     int_Y <P, D_A U>
     - 1/(2 Z_U) int_Y |P|^2
     - int_Y V(U,eps)
     - c_theta/2 int_Y |theta|^2
   ```

   giving schematically:

   ```text
   E_P:  D_A U - Z_U^-1 P = 0
   E_U: -D_A^* P + V_U + c_theta theta = 0
   E_A:  g_A^-2 D_A^* F_A - c_theta theta + [U,P] = 0
   ```

   so the source contains the canonical IG current `[U,P]`.

5. The total conserved object is expected to be `theta_eff`, not bare theta:

   ```text
   D_A^* theta_eff = 0
   ```

   This is not yet a theorem in the repo because the full written `S_IG_dyn` and its exact
   gauge Noether identity are absent.

6. The Lambda/dark-energy provenance note already classifies Branch 3 as the strongest
   dynamic route, but blocked before source-generated:

   ```text
   Z_theta, C_Rtheta, xi_eff.
   ```

7. The minimal action spec explicitly marks `S_IG-dyn[eps,beta; A]` as a required open slot.
   It also excludes bare `Lambda` and bare `R theta^2` terms from the baseline unless a
   primary source fixes them.

## 3. Strongest Positive Branch 3 Construction Possible Now

The strongest construction currently available is a conditional theorem schema. It can be
written precisely enough to guide the next proof, but not precisely enough to certify the
physics.

### 3.1 Proof-object contract for `S_IG_dyn`

A Branch 3 action proof object must be a tuple:

```text
DynamicIGActionPacket_B3 =
  (
    field_space,
    S_IG_dyn,
    pairings_and_signs,
    boundary_conditions,
    gauge_action,
    EL_tuple,
    J_IG,
    theta_eff,
    Noether_identity,
    observer_projection,
    FLRW_quadratic_packet,
    provenance_ledger
  )
```

with the following minimum contents.

Field space:

```text
Y = Y^14 = Met(X^4)
G = Sp(64)
P -> Y
A in Conn(P)
eps IG/gauge variable
beta in Omega^1(Y, ad P)
U = Ad(eps^-1) beta
optional P_IG in Omega^k(Y, ad P) with stated degree
s: X -> Y
theta = A - Gamma(eps) - U
Psi optional; Psi = 0 must be consistent in the vacuum branch
```

Action:

```text
S_GU^B3 =
  S_YM[A]
  + S_DD[A,eps,Psi]
  + S_W[s,A,eps,U]
  + S_IG_dyn[A,eps,U,optional P_IG,s]
  + S_boundary
```

The action packet must state whether `S_IG_dyn` is second-order:

```text
S_IG_dyn =
  - c_theta/2 int_Y <theta,theta>
  - Z_U/2 int_Y <D_A U, D_A U>
  - int_Y V(U,eps)
  + optional source-forced lower/cross terms
```

or first-order:

```text
S_IG_dyn,parent =
  int_Y <P_IG, D_A U>
  - 1/(2 Z_U) int_Y <P_IG,P_IG>
  - int_Y V(U,eps)
  - c_theta/2 int_Y <theta,theta>
  + optional source-forced lower/cross terms.
```

These displayed expressions are only admissible templates until a source or geometric
argument fixes the exact term list, coefficient normalizations, signs, and boundary
conditions. `Z_U`, `V`, and any cross term may not be chosen from DESI/Rubin-style target
windows, Schwarzschild/Kerr residuals, or a desired value of `xi_eff`.

Euler-Lagrange tuple:

```text
E_A = delta S_GU^B3 / delta A
E_U = delta S_GU^B3 / delta U
E_eps = delta S_GU^B3 / delta eps
E_s = delta S_GU^B3 / delta s
E_P = delta S_GU^B3 / delta P_IG        if a parent action is used
E_Psi = delta S_GU^B3 / delta Psi       if Psi is included
```

The packet must expose the connection equation in the form:

```text
E_A =
  g_A^-2 D_A^* F_A
  - c_theta theta
  + J_IG
  + J_W
  + J_Psi
  + J_cross
  = 0.
```

Branch 3 is clean only if all non-theta terms in this equation are named and classified.
The source current is then:

```text
theta_eff =
  g_A^2(
    c_theta theta
    - J_IG
    - J_W
    - J_Psi
    - J_cross
  )
```

or the same expression with the signs fixed by the action convention. In vacuum reductions
one may set `Psi = 0` only after proving `E_Psi=0` and `J_Psi=0` are consistent.

### 3.2 Total-current conservation theorem contract

The theorem to prove is:

```text
Theorem_B3_TotalCurrentConservation.

Given:
  a source-forced Branch 3 action packet DynamicIGActionPacket_B3;
  local G gauge invariance of the full action;
  boundary conditions that make the gauge variation boundary term vanish;
  a connection equation E_A = 0 with theta_eff defined from all A-current terms;
  the remaining IG/section/spinor equations imposed where the Noether identity requires them.

Then:
  D_A^* theta_eff = 0
```

with exact off-shell/on-shell status stated.

The proof must not use the old bare-theta sector-wise Noether argument unless the written
action actually splits into a separately gauge-invariant theta sector whose omitted IG
variations do not contribute. For Branch 3, the expected proof route is the full gauge
Noether identity:

```text
N_A(E_A) + N_U(E_U) + N_eps(E_eps) + N_s(E_s) + N_P(E_P) + N_Psi(E_Psi) = 0.
```

After the relevant non-connection equations are imposed, this must reduce to:

```text
D_A^* E_A = 0.
```

Using:

```text
E_A = g_A^-2 D_A^* F_A - g_A^-2 theta_eff,
```

the theorem must then justify the final step:

```text
D_A^* theta_eff = 0.
```

This final step is not automatic from `D_A^* E_A = 0` unless the action packet also supplies
the needed Yang-Mills integrability identity or equivalent current-conservation identity in
the chosen convention. The dark-energy assumption note already warns that one may not simply
assume `D_A^*D_A^*F_A = 0` in arbitrary Yang-Mills geometry.

Therefore the conservation packet must include one of:

```text
Conservation route A:
  an exact Noether identity whose connection-current part is already
  D_A^* theta_eff = linear combination of non-connection E_i;

Conservation route B:
  a verified branch-specific identity for D_A^*D_A^*F_A that converts
  D_A^*E_A = 0 into D_A^*theta_eff = 0;

Conservation route C:
  an explicitly weaker conservation law, with the observer stress conservation
  proved after projection rather than asserted for theta_eff on Y.
```

The current repo has not selected A, B, or C for Branch 3.

### 3.3 FLRW coefficient packet

Only after the total current theorem is instantiated may Branch 3 enter the theta/dark-energy
coefficient gate. The required packet is:

```text
FLRW_B3_QuadraticPacket =
  (
    s_FLRW,
    observer projection Pi_obs,
    homogeneous mode b_raw(t) u_0,
    representation type of u_0,
    quadratic action S_2[b_raw,g],
    Z_theta,
    C_Rtheta,
    M_eff,
    residual terms,
    xi_eff = C_Rtheta / Z_theta,
    positivity/ghost check
  )
```

with:

```text
S_2[b_raw,g] =
  int_X sqrt(-g) [
    -1/2 Z_theta g^mu nu partial_mu b_raw partial_nu b_raw
    -1/2 (C_M + C_Rtheta R[g]) b_raw^2
    + controlled residuals
  ].
```

No dark-energy promotion is licensed unless:

```text
Z_theta > 0
B = sqrt(Z_theta) b_raw
xi_eff = C_Rtheta / Z_theta
```

are generated before target windows are consulted.

## 4. First Exact Obstruction Or Missing Proof Object

The first exact obstruction is:

```text
missing source-forced S_IG_dyn action term.
```

Ordering of the obstruction:

| object | current status | why it cannot be promoted yet |
|---|---|---|
| `S_IG_dyn` | missing as source-forced action | Existing notes provide representative second-order and first-order templates, not a fixed action from GU source geometry. |
| source current `J_IG` | underdefined | It depends on the exact kinetic/parent/lower/cross terms and boundary conventions. |
| `theta_eff` | contract-only | Its formula changes with every current term in `E_A`; only the schematic `c_theta theta - J_IG` is available. |
| conservation identity | underdefined | The full Noether identity and the exact route to `D_A^* theta_eff = 0` are not written. |
| `Z_theta` | undefined | No Branch 3 quadratic FLRW reduction exists. |
| `C_Rtheta` | undefined | No generated curvature coupling has been computed; a bare insertion is forbidden as provenance. |
| `xi_eff` provenance | undefined | `xi_eff = C_Rtheta/Z_theta` is specified as a gate, but neither coefficient is generated. |

This order matters. The repo does not merely lack a final `xi_eff` number; it lacks the
source-fixed action whose variation would define the current whose conservation would permit
the projection whose quadratic reduction would define `xi_eff`.

## 5. Constructive Next Object That Would Remove Or Test The Obstruction

Build:

```text
Branch3TotalCurrentPacket_V0.
```

Minimum contents:

1. A fixed `S_IG_dyn` or first-order parent action, with signs, pairings, degrees,
   boundary conditions, and all lower/cross terms.
2. A provenance row for every coefficient:

   ```text
   source_forced | geometry_forced | normalization | imported_control | target_fitted
   ```

3. A full EL tuple:

   ```text
   (E_A, E_U, E_eps, E_s, E_P or none, E_Psi or none)
   ```

4. The exact `J_IG` current and complete `theta_eff`.
5. The exact full-action Noether identity, including whether conservation is off-shell,
   on-shell after IG equations, or only after observer projection.
6. A negative-control check showing that if the kinetic/parent term is removed and `beta`
   is freely varied, the branch returns to `theta = 0`.
7. An FLRW scalar-mode survival check:

   ```text
   s^*theta_eff or s^*U contains b_raw(t) u_0,
   u_0 is homogeneous/isotropic and scalar for the KG reduction.
   ```

8. A quadratic coefficient computation:

   ```text
   Z_theta,
   C_Rtheta,
   xi_eff = C_Rtheta/Z_theta,
   M_eff,
   residual ledger.
   ```

9. A placement ledger:

   ```text
   geometric side | stress side | residual | fail
   ```

10. Rollback/falsification conditions attached to each claim.

Pass condition for this next object:

```text
S_IG_dyn fixed before target data,
theta_eff exactly derived,
D_A^*theta_eff or projected conservation exactly proved,
FLRW coefficient packet emitted with Z_theta and C_Rtheta.
```

Fail or rollback conditions:

```text
S_IG_dyn chosen to fit cosmology target data;
Z_U, V, boundary data, or cross terms tuned to DESI/Rubin windows;
J_IG omitted from the source equation;
bare theta cited as conserved when total current is required;
Noether identity only gives a joint relation and no conservation theorem;
Z_theta <= 0 with no gauge-removal explanation;
C_Rtheta inserted as bare R[g] theta^2;
xi_eff fitted rather than generated;
no scalar FLRW mode survives;
exact-GR residuals hidden inside the dark-energy term.
```

## 6. What This Means For Lambda/Dark Energy And Source-Geometry Claims

Branch 3 currently supports only this careful claim:

```text
The repo has identified a plausible dynamical IG total-current route that could host a
source-derived dark-energy-like term if its action/current/conservation/coefficient packet
is constructed.
```

It does not support:

```text
GU derives Lambda.
GU cancels Lambda.
GU derives dark energy.
GU derives xi_eff < -0.319.
GU derives xi_eff ~= -0.6.
A bare Lambda term is source geometry.
A fitted theta scalar is source-derived.
```

For source-geometry language, Branch 3 is a candidate bridge from source action to observer
stress, not a closed bridge. The source-geometry claim may say:

```text
Branch 3 requires source geometry to appear through a conserved total current theta_eff,
not through bare theta alone.
```

It may not say:

```text
the observed dark-energy source is already generated by GU geometry.
```

If `Branch3TotalCurrentPacket_V0` closes, the result would still be conditional on the
same-branch coefficient packet. A conserved total current alone is not a Lambda/dark-energy
derivation. It is the necessary action-level entry ticket for the later projection and
coefficient gates.

## 7. Next Meaningful Proof Or Computation Step

The next step is not another DESI/Rubin comparison. It is:

```text
derive or falsify Branch3TotalCurrentPacket_V0.
```

Concrete sequence:

1. Choose the smallest source-forced dynamic IG action candidate from GU geometry or a
   primary action source.
2. Derive `E_A` and `E_U` or `E_P` explicitly.
3. Read off `J_IG` and define `theta_eff` with all signs.
4. Prove the full gauge Noether identity and record whether conservation is off-shell,
   on-shell, or projected.
5. Only then run the FLRW quadratic reduction for `Z_theta`, `C_Rtheta`, and `xi_eff`.

The first binary decision is:

```text
Does a source-forced S_IG_dyn exist?
```

If yes, Branch 3 can become a genuine conditional theorem candidate. If no, Branch 3 remains
a physically attractive but underdefined host, and the dark-energy route must either return
to Branch 2A's missing `Phi` or remain phenomenological/control.

## 8. Machine-Readable JSON Summary

```json
{
  "artifact": "CYCLE1_BRANCH3_DYNAMICAL_IG_CURRENT_GATE",
  "version": "2026-06-24",
  "mission_posture": "Mission_A_constructive_obstruction",
  "verdict": "underdefined",
  "promotion_decision": {
    "from": "strongest_candidate_open",
    "to": "conditional_theorem",
    "promoted": false,
    "reason": "source_forced_S_IG_dyn_is_missing"
  },
  "explicit_non_claims": {
    "GU_derives_Lambda": false,
    "GU_cancels_Lambda": false,
    "GU_derives_dark_energy": false,
    "GU_derives_xi_eff_window": false,
    "bare_Lambda_source_derived": false
  },
  "derived_from_repo_sources": [
    "free_beta_with_only_theta_norm_forces_theta_zero",
    "Branch_3_allows_nonzero_theta_by_making_IG_dynamical",
    "Branch_3_generically_rewrites_source_law_to_total_current",
    "theta_eff_not_bare_theta_is_the_conserved_candidate",
    "Z_theta_C_Rtheta_xi_eff_are_required_but_undefined"
  ],
  "strongest_positive_construction": {
    "status": "conditional_theorem_schema_not_instantiated",
    "source_law_contract": "D_A^*F_A=theta_eff",
    "theta_eff_contract": "theta_eff_equals_g_A^2(c_theta_theta_minus_all_A_currents)",
    "representative_parent_action": "int<P_IG,D_A U>-1/(2Z_U)int|P_IG|^2-int V(U,eps)-c_theta/2 int|theta|^2",
    "required_theorem": "Theorem_B3_TotalCurrentConservation",
    "required_conservation_output": "D_A^*theta_eff=0_or_precise_projected_conservation"
  },
  "first_missing_object": "source_forced_S_IG_dyn_action_term",
  "missing_objects_ordered": [
    "S_IG_dyn",
    "source_current_J_IG",
    "theta_eff",
    "conservation_identity",
    "Z_theta",
    "C_Rtheta",
    "xi_eff_provenance"
  ],
  "proof_object_contract": {
    "dynamic_action_packet": [
      "field_space",
      "S_IG_dyn",
      "pairings_and_signs",
      "boundary_conditions",
      "gauge_action",
      "EL_tuple",
      "J_IG",
      "theta_eff",
      "Noether_identity",
      "observer_projection",
      "FLRW_quadratic_packet",
      "provenance_ledger"
    ],
    "total_current_theorem_requires": [
      "local_G_gauge_invariance",
      "boundary_term_vanishes",
      "complete_E_A_current_decomposition",
      "non_connection_EL_terms_accounted_for",
      "route_to_D_A_star_theta_eff_conservation"
    ],
    "flrw_packet_requires": [
      "b_raw_u0_mode",
      "u0_representation_type",
      "Z_theta",
      "C_Rtheta",
      "xi_eff_equals_C_Rtheta_over_Z_theta",
      "positivity_check",
      "residual_ledger"
    ]
  },
  "constructive_next_object": "Branch3TotalCurrentPacket_V0",
  "rollback_falsification_conditions": [
    "S_IG_dyn_absent",
    "S_IG_dyn_not_source_forced",
    "Z_U_or_V_target_fitted",
    "J_IG_omitted_from_source_law",
    "bare_theta_claimed_conserved_in_Branch_3",
    "Noether_identity_does_not_imply_total_current_conservation",
    "no_FLRW_scalar_mode",
    "Z_theta_nonpositive_without_gauge_removal",
    "C_Rtheta_inserted_by_hand",
    "xi_eff_fitted_not_generated",
    "DESI_Rubin_window_used_upstream",
    "exact_GR_residual_hidden_as_dark_energy"
  ],
  "lambda_dark_energy_implication": {
    "current_claim_allowed": "Branch_3_can_host_a_possible_source_derived_dynamic_theta_IG_term_after_total_current_packet_closes",
    "current_claim_forbidden": "GU_has_derived_or_cancelled_Lambda_or_dark_energy",
    "next_gate_before_cosmology": "derive_or_falsify_Branch3TotalCurrentPacket_V0"
  }
}
```

## Sources Read

- `RESEARCH-POSTURE.md`
- `process/runbooks/five-lane-frontier-run.md`
- `explorations/mission-a-lambda-dark-energy-provenance-2026-06-24.md`
- `explorations/ig-dynamics-nonzero-theta-action-gate-2026-06-24.md`
- `explorations/dark-energy-assumption3-variational-2026-06-23.md`
- `explorations/gu-minimal-action-spec-2026-06-24.md`
- `explorations/gu-closed-loop-action-ig-branch-2026-06-24.md`
