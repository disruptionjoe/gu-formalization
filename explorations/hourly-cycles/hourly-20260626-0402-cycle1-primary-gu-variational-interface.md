---
title: "Primary GU Variational Interface V0 Gate"
date: "2026-06-26"
status: exploration
doc_type: frontier_run_lane_artifact
run_id: "hourly-20260626-0402"
cycle: 1
lane: "PrimaryGUVariationalInterface"
artifact_id: "PrimaryGUVariationalInterface_V0"
verdict: "UNDERDEFINED_BLOCKED_BRANCH_FIXED_IG_VARIATION_PACKET_MISSING"
owned_path: "explorations/hourly-20260626-0402-cycle1-primary-gu-variational-interface.md"
---

# Primary GU Variational Interface V0 Gate

## 1. Verdict

`PrimaryGUVariationalInterface_V0` is not present in the repo as a closed typed
variation tuple.

The repo does have:

```text
I_GU =
  (fields, variations, gauge group, D_GU, S_GU,
   section map, source law, boundary conditions, reduction functor)
```

as a typed interface contract, plus schematic Euler-Lagrange slots for the main
branches. It does not yet have a branch-fixed, source-derived tuple

```text
(S_GU[branch], Var[branch], E_s, E_A, E_IG, E_Psi,
 SourceLaw[branch], Pi_4D, R_shadow)
```

that produces

```text
Pi_4D(E_s,E_A,E_IG,E_Psi)
  =
  G_mu_nu[g = s^*g_Y]
  + Lambda_eff g_mu_nu
  - kappa_eff T_mu_nu^shadow
  - R_mu_nu^shadow
```

with a controlled residual and a derived source law, without inserting
Schwarzschild, Kerr, a target stress tensor, a target `xi_eff`, or a bare
Einstein-Hilbert sector upstream.

Decision:

```text
verdict_class = underdefined / blocked
exact GR recovery = not admitted
schematic EL tuple = present
full derived EL tuple = absent
branch source law = taxonomy present, derivation absent
```

The first exact missing variational object is:

```text
BranchFixedIGVariationPacket_V0
```

This is more precise than "write the full action." The first unresolved choice is the
IG variation object that determines whether the action is Branch 2A, Branch 2B,
Branch 3, background/Stueckelberg, or rejected free beta. Until that packet exists,
`S_GU/S_IG` has no single source law and no evaluable exact-GR Euler-Lagrange tuple.

## 2. Sources Read First

Required process and posture sources:

- `RESEARCH-POSTURE.md`
- `process/runbooks/five-lane-frontier-run.md`
- `explorations/remaining-math-topography-ledger-v0-2026-06-26.md`

Exact-GR, action, IG, source-law, and anti-smuggling artifacts located by `rg` and read:

- `explorations/primary-gu-interface-contract-2026-06-24.md`
- `explorations/gu-action-4d-physics-gate-2026-06-24.md`
- `explorations/gu-minimal-action-spec-2026-06-24.md`
- `explorations/exact-schwarzschild-kerr-el-gate-2026-06-24.md`
- `explorations/gr-shadow-recovery-certificate-2026-06-24.md`
- `explorations/gu-typed-operator-action-spine-2026-06-24.md`
- `explorations/gu-closed-loop-action-ig-branch-2026-06-24.md`
- `explorations/ig-dynamics-nonzero-theta-action-gate-2026-06-24.md`
- `explorations/constraint-first-ig-tangent-space-gate-2026-06-24.md`
- `explorations/cycle1-branch3-dynamical-ig-current-gate-2026-06-24.md`
- `explorations/stress-energy-shadow-emergence-certificate-2026-06-24.md`
- `explorations/source-geometry-not-quantized-gravity-contract-2026-06-24.md`
- `explorations/live-claim-dag-fault-finality-ledger-2026-06-24.md`
- `canon/schwarzschild-weak-field-rfail.md`
- `explorations/rfail-non-umbilic-schwarzschild-2026-06-23.md`

Relevant structural audit files read:

- `tests/primary_gu_interface_contract_audit.py`
- `tests/gr_shadow_recovery_certificate_audit.py`
- `tests/constraint_first_ig_tangent_gate.py`
- `tests/cycle1_branch3_dynamical_ig_current_audit.py`
- `tests/stress_energy_shadow_emergence_audit.py`

The key source pattern is consistent: current files enforce interfaces and
anti-overclaim guards, but they do not supply a branch-fixed variational theorem.

## 3. Specific GU Claim / Bridge Under Test

The bridge under test is:

```text
PrimaryGUVariationalInterface_V0:

Given source data
  X, Y = Met_Lor(X), g_Y, P -> Y, Sp(64), S, Phi_2,
  s, A, epsilon, beta or U, theta, Psi, II_s^H, j_s,

and a branch-fixed action
  S_GU[branch] = S_YM + S_DD + S_theta + S_W + S_IG[branch]
                 + source-forced cross/boundary terms,

derive the full Euler-Lagrange tuple
  E_s = 0,
  E_A = 0,
  E_IG = 0,
  E_Psi = 0,

derive the branch source law
  D_A^*F_A = theta,
  or D_A^*F_A = theta plus multiplier correction,
  or D_A^*F_A = theta_eff,

and project to an observer-facing 4D equation
  G[g = s^*g_Y] + controlled residual/source terms = 0.
```

The test asks whether this is already in the repo without target-metric insertion.

Answer: no. The current repo has a typed contract for what the interface must
contain, and has branch-local obstruction theorems. It does not yet have the
source-derived variational object that makes the tuple unique.

## 4. Terrain Classification And Forbidden Shortcut

Terrain:

```text
primary terrain = smooth-variational
guard terrain   = provenance-verifier
```

This is a smooth-variational wall because the decisive object is an action,
variation space, Euler-Lagrange tuple, source law, and projection identity. It also
needs a provenance-verifier guard because many fake closures can be manufactured by
choosing constraints or cross terms after seeing the target metrics.

Forbidden shortcut:

```text
Do not use Schwarzschild/Kerr success, weak-field success, a desired xi_eff,
or hidden stress-energy relabeling to choose S_IG, Phi, cross terms, source law,
or residual absorption.
```

Concrete forbidden moves rejected in this lane:

- Treating the canon weak-field `O(M/r)` Schwarzschild pass as exact nonlinear GR.
- Treating `Ric[g_BH] = 0` as GU-specific recovery before the source EL tuple is solved.
- Choosing `Phi(epsilon,beta,s)` so that Schwarzschild/Kerr residuals cancel.
- Choosing `S_IG_dyn`, `Z_U`, `V`, or cross terms from a target `xi_eff` window.
- Preserving old bare-theta source language after moving to Branch 3.
- Moving Willmore, gauge, multiplier, or section residuals into `T_mu_nu^shadow`
  without a variational provenance ledger.

## 5. Strongest Positive Construction Attempt

The strongest positive construction currently available is a conditional interface
template:

```text
PrimaryGUVariationalInterface_Template =
  (
    field_space,
    branch_key,
    S_GU[branch],
    Var[branch],
    EL_tuple,
    source_law[branch],
    Pi_4D,
    residual_control,
    anti_target_provenance
  )
```

Use the current minimal action skeleton:

```text
S_GU =
  S_YM[A]
  + S_DD[A,Psi]
  + S_theta[A,epsilon,beta]
  + S_W[s,A,epsilon,beta]
  + S_IG[branch]
  + S_cross[source-forced only]
  + S_boundary.
```

The full variation should produce:

```text
E_A =
  g_A^-2 D_A^*F_A
  - c_theta theta
  + J_Psi
  + E_A^W
  + E_A^IG
  + E_A^cross
  = 0

E_s =
  delta_s S_W
  + delta_s S_YM
  + delta_s S_theta
  + delta_s S_IG
  + delta_s S_DD
  + boundary terms
  = 0

E_IG =
  E_epsilon, E_beta
  or E_epsilon, E_U, E_P
  or E_lambda

E_Psi = 0.
```

Then a 4D projection theorem would identify:

```text
Pi_4D(E_s,E_A,E_IG,E_Psi)
  =
  G_mu_nu[g]
  + Lambda_eff g_mu_nu
  - kappa_eff T_mu_nu^shadow
  - R_mu_nu^shadow.
```

The best conservative route is still Branch 2A:

```text
Phi(epsilon,beta,s) = 0,
D_A Phi = 0,
K_beta = ker(D_beta Phi) proper,
D_A^*F_A = theta after normalization.
```

If that object existed and was source-derived, it would preserve the bare source law
without free-beta collapse. The repo proves the conditional tangent-space theorem, but
does not provide the required `Phi`.

The honest dynamic fallback is Branch 3:

```text
S_IG_dyn[A,epsilon,U or beta, optional P_IG,s]
D_A^*F_A = theta_eff
theta_eff = g_A^2(c_theta theta - J_IG + ...)
```

The repo has a coherent Branch 3 theorem schema and representative parent action
forms. It does not have a source-forced `S_IG_dyn`, so `J_IG`, `theta_eff`,
conservation, and FLRW coefficients are only contract-level.

Therefore the strongest positive construction attempt remains conditional and cannot
be promoted to a present typed variation tuple.

## 6. First Exact Obstruction Or Missing Proof Object

The first exact missing variational object is:

```text
BranchFixedIGVariationPacket_V0
```

Required contents:

```text
BranchFixedIGVariationPacket_V0 =
  (
    branch_key,
    IG_field_space,
    IG_variation_space,
    S_IG_or_constraint,
    coefficient_and_boundary_provenance,
    beta_or_U_equation,
    connection_current_decomposition,
    source_law,
    Noether_or_projected_conservation_identity,
    anti_target_smuggling_certificate
  )
```

It must close exactly one of these routes.

Route 2A, bare-source constrained IG:

```text
DerivedAIndependentIGConstraintPacket_2A =
  (
    Phi(epsilon,beta,s)=0,
    D_beta Phi,
    K_beta = ker(D_beta Phi),
    proof K_beta is proper,
    conormal image im(D_beta Phi)^*,
    projected beta equation,
    proof D_A Phi = 0,
    proof Phi is not target-selected
  )
```

Current status: absent.

Route 3, dynamical total current:

```text
SourceForcedSIGDynPacket_3 =
  (
    S_IG_dyn or first-order parent action,
    signs, pairings, degrees, boundary terms,
    E_A, E_U/E_P, E_epsilon, E_s,
    exact J_IG,
    theta_eff,
    full-action Noether identity,
    proof theta_eff conservation or projected conservation,
    proof coefficients are not target-fitted
  )
```

Current status: absent.

Why this is first:

- Without it, the source law is not a single typed field equation.
- Without it, `E_beta` either collapses theta or is not defined as an admissible
  projected equation.
- Without it, the section equation cannot be paired with the correct connection and IG
  equations.
- Without it, the 4D Einstein tensor can be written as a target-side object, but the
  GU-specific projection identity and residual control are not derived.
- Without it, Schwarzschild/Kerr are only target tests, not source-field solutions.

The Willmore-only Schwarzschild obstruction remains important, but it is not the first
missing variational object for this lane. It is a branch-local failure that becomes
decisive only after a branch-fixed full tuple is available or after the branch is
declared Willmore-only/free-beta.

## 7. What Would Change If The Hole Closed

If `BranchFixedIGVariationPacket_V0` closed, the repo would gain a real input for the
exact-GR gate:

```text
S_GU[branch] and Var[branch] fixed
=> full EL tuple derivable
=> source law stated exactly
=> Pi_4D projection theorem becomes checkable
=> Schwarzschild can be tested before Kerr
```

For Branch 2A, a valid packet would permit a bare-source exact-GR attempt:

```text
D_A^*F_A = theta
```

with nonzero theta allowed only in the conormal directions of a source-derived
constraint. Exact Schwarzschild would then be a well-posed question:

```text
Find (s_Schw,A_Schw,epsilon_Schw,beta_Schw,lambda_Schw,Psi=0)
such that E_s = E_A = E_epsilon = E_beta = E_lambda = E_Psi = 0.
```

For Branch 3, a valid packet would revise the source language:

```text
D_A^*F_A = theta_eff
```

and the exact-GR and FLRW lanes would have to use the total current, not bare theta.
Only then could the repo compute `Z_theta`, `C_Rtheta`, and `xi_eff = C_Rtheta/Z_theta`
from the same branch.

If the hole closed and exact Schwarzschild plus Kerr passed with no hidden matter,
`ACTION-GR` could move from open specification toward conditional recovery. If it
closed and either black-hole vacuum failed, the failure would be branch-specific and
decision-grade rather than an underdefinition.

## 8. What Would Falsify Or Demote The Route

This route is falsified or demoted if any of the following occurs:

- The actual branch varies free `beta` with only `S_theta = -c_theta/2 int |theta|^2`;
  then `E_beta` forces `theta = 0`.
- Branch 2A cannot supply a source-derived, gauge-covariant, A-independent
  `Phi(epsilon,beta,s)=0` with proper beta tangent.
- The only available `Phi` is A-dependent; then the source law is corrected and the
  bare `D_A^*F_A = theta` route must be abandoned.
- The only available `Phi` is selected by Schwarzschild/Kerr success, a target FLRW
  scalar, a target `xi_eff`, a bare `R theta^2`, or a bare `Lambda`.
- Branch 3 is chosen but no source-forced `S_IG_dyn` exists.
- Branch 3 is chosen but old prose still treats bare theta as the conserved current.
- Exact Schwarzschild or Kerr requires nonzero hidden matter stress in a branch
  advertised as vacuum.
- The 4D Einstein-Hilbert metric action or target stress tensor is inserted as an
  independent sector rather than recovered as a projection of source variation.
- `R_shadow` is uncontrolled or is absorbed into `T_mu_nu^shadow` after the target
  test is known.

Any of these results would keep `ACTION-GR` open or demote the relevant branch to fail,
import, ansatz, or modified-gravity scope.

## 9. Next Meaningful Computation Or Proof Step

Build one object, not another global synthesis:

```text
BranchFixedIGVariationPacket_V0.
```

Recommended sequence:

1. Attempt Branch 2A first:

   ```text
   derive Phi(epsilon,beta,s)=0
   from tau-plus / IG / section geometry,
   prove gauge covariance,
   prove D_A Phi = 0,
   compute D_beta Phi and K_beta,
   prove K_beta proper,
   prove the conormal directions were not target-selected.
   ```

2. If Branch 2A is not derived, stop calling the bare source route active and switch to
   Branch 3:

   ```text
   write S_IG_dyn or a first-order parent action,
   derive E_A and E_U/E_P,
   read off J_IG and theta_eff,
   prove the total-current Noether identity.
   ```

3. Only after one of those packets exists, compute:

   ```text
   E_s for exact Schwarzschild first,
   E_A plus E_IG on the same witness fields,
   then Kerr with angular momentum boundary data.
   ```

4. Only after the exact-GR branch is fixed, reduce the same action to FLRW and compute:

   ```text
   scalar survival,
   Z_theta,
   C_Rtheta,
   xi_eff = C_Rtheta / Z_theta.
   ```

## 10. Claim-Status Consistency Result

No claim ledgers were changed by this lane. No promotion or demotion was made, so the
claim-status consistency workflow was not triggered.

The result is consistent with the current status surface:

```text
IG-VARIATION: blocked
ACTION-GR: open
GR-SHADOW: specified_open / not certified
weak-field Schwarzschild: bounded canon pass at O(M/r)
exact Schwarzschild/Kerr: not passed
```

This artifact sharpens the blocker rather than changing a claim status:

```text
from:
  "full action / IG variation missing"

to:
  "BranchFixedIGVariationPacket_V0 missing; it must supply either
   DerivedAIndependentIGConstraintPacket_2A or SourceForcedSIGDynPacket_3
   before a full exact-GR variation tuple can exist."
```

## 11. JSON Summary

```json
{
  "artifact_id": "PrimaryGUVariationalInterface_V0",
  "run_id": "hourly-20260626-0402",
  "cycle": 1,
  "lane": "PrimaryGUVariationalInterface",
  "artifact_path": "explorations/hourly-20260626-0402-cycle1-primary-gu-variational-interface.md",
  "verdict_class": "underdefined_blocked",
  "target_import_used": false,
  "claim_status_consistency_triggered": false,
  "exact_gr_recovery_admitted": false,
  "full_el_tuple_present": false,
  "source_law_present": false,
  "first_missing_object": "BranchFixedIGVariationPacket_V0: either DerivedAIndependentIGConstraintPacket_2A or SourceForcedSIGDynPacket_3",
  "forbidden_shortcut_rejected": true,
  "next_frontier_object": "BranchFixedIGVariationPacket_V0"
}
```
