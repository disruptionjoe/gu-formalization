---
title: "Goal Draft: Derive the IG Constraint / Variation Space"
date: 2026-06-24
status: exploration
doc_type: research_goal_draft
problem_label: "ig-constraint-variation-space-derivation"
verdict: "DRAFT_GOAL_BRANCH_2A_FIRST_BRANCH_3_FALLBACK"
owned_path: "explorations/cycle-gates-and-audits/goal-draft-ig-constraint-derivation-2026-06-24.md"
depends_on:
  - "explorations/misc/ig-dynamics-nonzero-theta-action-gate-2026-06-24.md"
  - "explorations/misc/gu-closed-loop-action-ig-branch-2026-06-24.md"
  - "explorations/cycle-gates-and-audits/gu-minimal-action-spec-2026-06-24.md"
  - "explorations/cycle-gates-and-audits/gu-typed-operator-action-spine-2026-06-24.md"
  - "tests/gu_action_branch_gate.py"
  - "canon/theta-field-flrw-dark-energy-eos.md"
  - "explorations/cycle-gates-and-audits/live-claim-dag-fault-finality-ledger-2026-06-24.md"
---

# Goal Draft: Derive the IG Constraint / Variation Space

## Goal Statement

Derive the allowed IG variation space for `(eps,beta)` from GU structure, instead of
choosing a constraint because it prevents the bare theta norm from forcing
`theta = 0`.

The target is to determine, with explicit equations, whether the IG variables live on an
A-independent constrained Stueckelberg/geometric subspace

```text
Phi(eps,beta,s) = 0,
D_A Phi = 0,
```

or whether no such subspace is forced and the theory must move to dynamical IG variables
with a total-current source law. In the successful Branch 2A case, the derivation should
explain why the allowed beta variations do not span all of `Omega^1(Y,ad P)`, compute the
projected `E_beta` equation, and preserve the vacuum source equation

```text
D_A^* F_A = theta
```

after the existing normalization. In the fallback Branch 3 case, the derivation should say
plainly that the bare theta-source equation is not the right canon object and replace it with

```text
D_A^* F_A = theta_eff,
theta_eff = c_theta theta - J_IG,
D_A^* theta_eff = 0.
```

This is a goal for removing an ambiguity in the variational principle, not a goal for making
`theta` nonzero by stipulation.

## Why This Matters

The action/IG lane currently has one load-bearing blocker: with only

```text
S_theta = -c_theta/2 int_Y |theta|^2,
theta = A - Gamma(eps) - Ad(eps^-1) beta,
```

and freely varied `beta`, the beta equation forces

```text
theta = 0.
```

That kills the intended nonzero theta source and the theta dark-energy mode. The branch notes
already identify Branch 2A as the strongest conservative route, but Branch 2A is only legitimate
if the constrained variation space is derived from a written GU action, tau-plus / IG geometry,
double-coset structure, section-pullback geometry, or a real Stueckelberg slice. A constraint
invented only to avoid `theta=0` is not evidence.

Solving this goal would turn the live node `IG-VARIATION` from "blocked" into a precise fork:
either Branch 2A becomes a real action branch, or Branch 3 becomes the honest replacement. In
both outcomes the project gets sharper. The exact Schwarzschild/Kerr gate and the FLRW
`xi_eff` gate are not solved by this goal, but they become well-posed instead of depending on
an unstated variation rule.

## Current Branch Decision

The current branch decision remains:

```text
Try Branch 2A first:
  A-independent constrained IG / Stueckelberg geometry.
```

Branch 2A is worth trying because it is the only live branch that can simultaneously allow
nonzero `theta` and preserve

```text
D_A^* F_A = theta.
```

But this goal tightens the decision:

```text
Branch 2A is not accepted until Phi(eps,beta,s)=0 and its allowed tangent variations
are derived from GU geometry or a written GU action.
```

If the derivation fails, do not weaken the standard. The fallback is:

```text
Switch to Branch 3:
  eps,beta are dynamical IG fields;
  the connection equation is a total-current law;
  canon language must stop identifying bare theta as the exact conserved source.
```

Branch 2B, where `Phi` depends on `A`, is not the main target. It can be recorded if forced
by primary structure, but it changes the source equation through a multiplier current and
therefore does not close the conservative Branch 2A goal. Branch 4, the bare free-beta norm,
is rejected unless `theta=0` is accepted as intended physics.

## Exact Deliverables

1. A variation-space derivation note that states the actual status of `(eps,beta)`:
   background/Stueckelberg, A-independent constrained, A-dependent constrained, or dynamical.

2. If Branch 2A succeeds, an explicit candidate constraint or intrinsic description:

   ```text
   C_IG(s) = {(eps,beta) : Phi(eps,beta,s)=0}
   ```

   together with the tangent space `T C_IG`, the allowed variations
   `(delta eps, delta beta)`, and the conormal/multiplier directions that absorb the
   `S_theta` beta variation.

3. A proof that the Branch 2A constraint is A-independent:

   ```text
   D_A Phi = 0
   ```

   in the sense needed by the action variation, so that the connection equation is not
   silently corrected by `(D_A Phi)^* lambda`.

4. The projected IG Euler-Lagrange equations:

   ```text
   E_A:
     g_A^-2 D_A^*F_A - c_theta theta = 0

   E_beta:
     c_theta Ad(eps) theta + (D_beta Phi)^* lambda = 0

   E_eps:
     c_theta L_eps^* theta + (D_eps Phi)^* lambda = 0

   E_lambda:
     Phi(eps,beta,s) = 0
   ```

   or the corrected Branch 3 equations with `J_IG` if Branch 2A fails.

5. A gauge/Noether compatibility statement: say whether `D_A^* theta = 0` is an on-shell
   consequence of the source equation, a sector identity, a constraint, or false for bare
   `theta` and true only for `theta_eff`.

6. A branch-gate update proposal for the logical matrix encoded by
   `tests/gu_action_branch_gate.py`. This need not be a code change in this goal draft, but
   the result must be precise enough that the checker could be updated without interpretation.

7. A downstream handoff contract for the exact GR and FLRW gates: state exactly what data the
   next worker must use to compute `E_s`, exact Schwarzschild/Kerr viability, `Z_theta`,
   `C_Rtheta`, and

   ```text
   xi_eff = C_Rtheta / Z_theta.
   ```

## Acceptance Criteria

This goal is accepted only if one of the following two outcomes is reached cleanly.

### Acceptance A: Branch 2A Derived

Branch 2A is accepted if all of the following are true:

- The constraint or variation space is forced by a primary GU source, tau-plus / IG geometry,
  double-coset geometry, section-pullback geometry, or a legitimate Stueckelberg slice.
- The allowed beta variations are explicitly smaller than all of `Omega^1(Y,ad P)` in the
  branch being varied.
- The beta equation becomes a projected/conormal equation and no longer implies `theta=0`.
- `Phi` is independent of `A` in the variational sense needed to preserve
  `D_A^*F_A = theta`.
- Gauge covariance of `theta` and the status of `D_A^*theta = 0` are stated without relying
  on a hidden free variation.
- No bare `R theta^2`, bare `Lambda`, or tuned `xi` is inserted to make the FLRW gate pass.
- The result gives enough structure to run the full EL tuple and the FLRW scalar reduction.

### Acceptance B: Branch 3 Fallback Executed

Branch 3 is accepted as the fallback if Branch 2A cannot be derived and the note does all of
the following:

- States that no A-independent GU-derived constraint has been found.
- Writes the dynamical IG action slot or minimal current structure needed to replace the
  algebraic beta equation.
- Replaces the source law everywhere with a total-current equation:

  ```text
  D_A^*F_A = theta_eff.
  ```

- States that conservation applies to `theta_eff`, not generally to bare `theta`.
- Marks the old bare-theta source language as superseded for this branch.
- Leaves `xi_eff` open until computed from the written `S_IG-dyn`, not fitted.

## Failure / Demotion Criteria

Demote the goal or the branch if any of these conditions fire:

- The proposed Branch 2A constraint is chosen only because it removes the free-beta
  `theta=0` equation.
- The constraint depends on `A` but the branch still claims the uncorrected source equation
  `D_A^*F_A = theta`.
- The allowed beta variations secretly span the full beta-field space, so `E_beta` again
  forces `theta=0`.
- Gauge covariance is obtained by treating `(eps,beta)` as fixed spurions while also varying
  them in the EL tuple.
- A negative `xi_eff` is inserted as a free phenomenological parameter rather than generated
  by reduction.
- The scalar FLRW mode is assumed after the constraint makes `s^*theta` non-scalar,
  constrained away, or pure gauge.
- Exact Schwarzschild/Kerr language is upgraded from weak-field or open status without the
  full EL tuple.
- The result conflicts with the live claim DAG by upgrading `IG-VARIATION`, `ACTION-GR`, or
  `THETA-XI` without meeting the relevant closure condition.
- The actual written GU action has free `(eps,beta)` and only the bare theta norm. In that
  case the nonzero-theta branch fails in that action, and the honest status is:

  ```text
  theta = 0,
  D_A^*F_A = 0
  ```

  for the bare branch.

## Dependencies

Minimum dependency set:

- `explorations/misc/ig-dynamics-nonzero-theta-action-gate-2026-06-24.md` for the free-beta
  obstruction and the Branch 1/2/3 split.
- `explorations/misc/gu-closed-loop-action-ig-branch-2026-06-24.md` for the current branch matrix,
  exact GR gate, FLRW `xi_eff` gate, and Branch 2A recommendation.
- `explorations/cycle-gates-and-audits/gu-minimal-action-spec-2026-06-24.md` for the action inventory, EL tuple,
  sign conventions, normalization, and failure conditions.
- `explorations/cycle-gates-and-audits/gu-typed-operator-action-spine-2026-06-24.md` for the typed carrier,
  variation-status ledger, and the requirement that `epsilon,beta` not be free with only
  `|theta|^2`.
- `tests/gu_action_branch_gate.py` for the executable branch-status summary.
- `canon/theta-field-flrw-dark-energy-eos.md` for the current theta FLRW canon surface,
  including scalar-mode assumptions and the corrected, IC-sensitive EOS status.
- `explorations/cycle-gates-and-audits/live-claim-dag-fault-finality-ledger-2026-06-24.md` for the live statuses:
  `IG-VARIATION` blocked, `ACTION-GR` open, and `THETA-XI` open for GU provenance.

Likely additional dependencies for the actual derivation:

- The primary written GU action, if available.
- Tau-plus / double-coset IG construction notes.
- Section-pullback and Codazzi notes relating `s^*theta`, `II_s^H`, and normal-bundle data.
- Any BRST/gauge-slice source that justifies treating the constraint as a Stueckelberg slice.

## First 3 Concrete Work Packets

### Work Packet 1: Variation-Space Archaeology

Inventory every place the repo or primary source defines `IG`, `eps`, `beta`, `tau^+`,
double-coset data, Stueckelberg status, or section-pullback relation. Produce a table with
four columns:

```text
source claim,
mathematical object,
implied allowed variations,
does it support Branch 2A, Branch 2B, Branch 3, Branch 1, or Branch 4?
```

The output should identify whether any source already forces

```text
beta = beta_0(eps,s),
beta in im(tau^+_eps),
P_perp(beta,eps,s)=0,
```

or an equivalent A-independent slice.

### Work Packet 2: Candidate Constraint Derivation Or No-Go

For each serious Branch 2A candidate, write the constraint as an intrinsic subspace
`C_IG(s)` and compute its linearization. The essential test is:

```text
delta_beta theta = -Ad(eps^-1) delta beta
```

paired against only the allowed `delta beta` directions. Show either:

```text
projection_allowed(Ad(eps) theta) = 0
```

with nonzero conormal directions still available for `theta`, or prove that the allowed
variations are full and the candidate collapses to `theta=0`.

### Work Packet 3: Branch Decision And Handoff Contract

Write the branch decision in machine-checkable terms:

```text
BRANCH_2A_DERIVED
BRANCH_2A_NOT_DERIVED_USE_BRANCH_3
BRANCH_2B_ONLY_SOURCE_REVISED
BRANCH_4_REJECTED_THETA_ZERO
```

Then state the exact equations the next action worker must use. If Branch 2A is derived,
hand off `Phi`, `T C_IG`, multiplier equations, and the unchanged `E_A`. If Branch 3 is
selected, hand off `S_IG-dyn` or the minimal current form, `J_IG`, `theta_eff`, and the revised
Noether/conservation statement.

## What This Would Lead To

If Branch 2A succeeds, the project gets a conservative action branch with a nonzero theta
source that does not smuggle in a constraint. The next workers can then run the real physics
gates:

```text
1. derive the full EL tuple;
2. test exact Schwarzschild and Kerr as vacuum configurations;
3. reduce the same branch on FLRW;
4. compute Z_theta, C_Rtheta, and xi_eff;
5. decide whether xi_eff < -0.319 is generated or not.
```

If Branch 2A fails, the project still gains a clean result: stop trying to preserve the bare
theta-source equation. Branch 3 becomes the honest route, with dynamical IG variables and a
total-current conservation law. That would likely be the stronger dark-energy branch, but it
requires canon surgery:

```text
old language:
  theta is the source and D_A^*theta = 0

new Branch 3 language:
  theta_eff is the source and D_A^*theta_eff = 0
```

Either outcome is worth doing. A derived Branch 2A would preserve the existing reconstruction
with real geometric backing. A Branch 3 demotion would prevent the project from building
dark-energy and exact-GR claims on an auxiliary-field contradiction.

## Bottom Line

The goal is not "find a way to keep `theta != 0`." The goal is:

```text
Derive the IG variation space.
```

Branch 2A is the first target because it keeps the most existing structure. Branch 3 is the
fallback because it is the honest dynamical alternative. Anything weaker leaves the
`IG-VARIATION` node blocked and keeps both `ACTION-GR` and `THETA-XI` open.
