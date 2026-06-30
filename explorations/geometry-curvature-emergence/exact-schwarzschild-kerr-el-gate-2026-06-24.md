---
title: "Exact Schwarzschild/Kerr EL Gate"
date: 2026-06-24
status: exploration
doc_type: research_gate
problem_label: "exact-schwarzschild-kerr-el-gate"
verdict: "BLOCKED_ACTION_AND_IG_SOURCE_UNDERDEFINED; WILLMORE_ONLY_BRANCH_FAILS_STRONG_FIELD"
owned_path: "explorations/geometry-curvature-emergence/exact-schwarzschild-kerr-el-gate-2026-06-24.md"
depends_on:
  - "explorations/cycle-gates-and-audits/goal-draft-primary-gu-action-operator-spec-2026-06-24.md"
  - "explorations/cycle-gates-and-audits/goal-draft-ig-constraint-derivation-2026-06-24.md"
  - "explorations/cycle-gates-and-audits/gu-typed-operator-action-spine-2026-06-24.md"
  - "explorations/misc/gu-closed-loop-action-ig-branch-2026-06-24.md"
  - "explorations/cycle-gates-and-audits/gu-action-4d-physics-gate-2026-06-24.md"
  - "canon/schwarzschild-weak-field-rfail.md"
  - "explorations/cycle-gates-and-audits/live-claim-dag-fault-finality-ledger-2026-06-24.md"
---

# Exact Schwarzschild/Kerr EL Gate

## 1. Verdict: blocked

This is not a closed pass. It is not even a conditional pass for exact black holes,
because the full action and the IG variation space are still underdefined.

The correct current verdict is:

```text
blocked:
  exact Schwarzschild/Kerr cannot be evaluated until the full vacuum EL tuple is
  fixed, including the IG source equation and the section variation.

branch failure:
  the Willmore-only / bare-free-beta instantiations already fail as exact
  strong-field vacuum GR branches.
```

The weak-field canon survives inside its stated scope: linearized Schwarzschild has no
leading `O(M/r)` obstruction in the combined `R_fail` bookkeeping. That weak-field
statement does not solve the exact equations below. Exact Schwarzschild and Kerr require
the section, connection, IG, and spinor equations to vanish simultaneously.

## 2. Exact vacuum EL tuple Schwarzschild/Kerr must satisfy

Let `g_BH` be either:

```text
Schwarzschild(M) on r > 2M,
Kerr(M,a) on the exterior domain with |a| < M.
```

The target vacuum configuration must be:

```text
(s_BH, A_BH, epsilon_BH, beta_BH, lambda_BH, Psi_BH = 0)
```

with:

```text
s_BH^* g_Y = g_BH                         up to diffeomorphism/gauge
Ric[g_BH] = 0
Lambda = 0                                unless an explicit asymptotic Lambda branch is stated
T_matter = 0
finite gauge/action boundary data
```

The first branch to test is the Branch 2A constrained-IG branch, because it is the only
current conservative branch that can preserve the bare source equation while avoiding
the free-beta collapse. Its vacuum action schematic is:

```text
S_vac =
  S_YM[A]
  + S_theta[A,epsilon,beta]
  + S_W[s,A,epsilon,beta]
  + integral_Y <lambda, Phi(epsilon,beta,s)>
  + S_cross^vac
  + S_boundary
```

where:

```text
S_YM[A]      = -1/(4 g_A^2) integral_Y <F_A,F_A>
S_theta      = -c_theta/2 integral_Y <theta,theta>
theta        = A - Gamma(epsilon) - Ad(epsilon^-1) beta
B_s          = II_s^H
S_W          = alpha_W/2 integral_X |B_s|^2
Phi          = Phi(epsilon,beta,s), with D_A Phi = 0 for true Branch 2A
```

`S_cross^vac` is zero in the baseline branch unless primary GU data supplies a term and
its coefficient. The spinor action is still part of the operator spine, but the vacuum
gate sets `Psi = 0` only after checking that the spinor equation has no tadpole.

The exact vacuum EL tuple is:

```text
E_A =
  g_A^-2 D_A^* F_A
  - c_theta theta
  + E_A^W
  + E_A^Phi
  + E_A^cross
  + J_Psi
  = 0

E_s =
  alpha_W W_s
  + E_s^YM
  + E_s^theta
  + E_s^Phi
  + E_s^cross
  + T_s^Psi
  = 0

E_beta =
  c_theta Ad(epsilon) theta
  + E_beta^W
  + (D_beta Phi)^* lambda
  + E_beta^cross
  = 0

E_epsilon =
  c_theta L_epsilon^* theta
  + E_epsilon^W
  + (D_epsilon Phi)^* lambda
  + E_epsilon^cross
  + E_epsilon^DD
  = 0

E_lambda =
  Phi(epsilon,beta,s)
  = 0

E_Psi =
  D_GU(A,epsilon) Psi
  + lower-order adjoint/nonlinear spinor terms
  = 0
```

Here:

```text
W_s = Delta^perp H + normal-curvature terms + shape terms
```

is the horizontal-normalized Willmore section residual for `B_s = II_s^H`.
`L_epsilon^*` is the adjoint of the linearized map

```text
delta epsilon |-> delta_epsilon Gamma
                 + delta_epsilon(Ad(epsilon^-1) beta).
```

For a strict A-independent Branch 2A constraint:

```text
E_A^Phi = 0.
```

If `B_s` is treated as a pure section object, then:

```text
E_A^W = E_beta^W = E_epsilon^W = 0.
```

If instead the horizontal-normalized section curvature is represented through
`theta` at the action level, these terms are not optional. They are part of the exact
tuple and may be the only available internal cancellation channel for the black-hole
section residual.

The normalized source equation:

```text
D_A^* F_A = theta
```

appears only after all of the following are true:

```text
g_A^2 c_theta = 1
Psi = 0 and J_Psi = 0
E_A^W = 0 or absorbed into the chosen source law
E_A^Phi = 0
E_A^cross = 0
```

If Branch 3 is selected instead, introduce `U = Ad(epsilon^-1) beta` or a first-order
momentum `P`. Then the connection equation becomes a total-current law:

```text
E_A =
  g_A^-2 D_A^*F_A
  - c_theta theta
  + J_IG
  + E_A^W
  + E_A^cross
  = 0

D_A^*F_A = theta_eff,
theta_eff = g_A^2(c_theta theta - J_IG + ...)
```

and the conserved source is `theta_eff`, not bare `theta`. That is a different exact
black-hole gate.

If `beta` is free and the only IG term is the bare theta norm, the tuple collapses:

```text
E_beta = c_theta Ad(epsilon) theta = 0
theta = 0
E_A = g_A^-2 D_A^*F_A = 0
```

That branch cannot support the advertised nonzero theta source.

## 3. Residual terms and what would have to make them vanish

For each black-hole metric, the residual ledger is:

| Residual | Current status | What must vanish or cancel |
|---|---|---|
| `R_GR = G[g_BH]` | Vanishes exactly for Schwarzschild and Kerr in 4D GR. | No GU content by itself. This only says the induced metric is Ricci-flat. |
| `R_W = alpha_W W_s(s_BH)` | Nonzero in the Willmore-only Schwarzschild analysis; Kerr is expected to fail for the same non-conformally-flat reason. | Must be canceled by `E_s^YM + E_s^theta + E_s^Phi + E_s^cross`, or the section action must be different. |
| `R_A = g_A^-2 D_A^*F_A - c_theta theta + ...` | Underdefined until the branch fixes `E_A^W`, `E_A^Phi`, and cross terms. | Need a smooth finite-action `A_BH` solving the exact source equation, with the correct boundary data and no hidden matter current. |
| `R_IG = (E_beta,E_epsilon,E_lambda)` | Blocked by missing Branch 2A constraint. Free beta kills theta. | Need a primary/geometric `Phi(epsilon,beta,s)=0` whose tangent space does not span all beta variations, or switch to Branch 3 and rewrite the source. |
| `R_Psi = E_Psi` | Usually harmless if the Dirac-DeRham action is bilinear and has no vacuum tadpole. | Need `Psi=0` to imply `J_Psi=T_s^Psi=0` for the black-hole background. |
| `R_cross` | Absent in the baseline, but could be supplied by a primary action. | Any cancellation from cross terms must use fixed coefficients, not terms introduced because Schwarzschild/Kerr need them. |
| Boundary residuals | Not computed. | ADM mass, angular momentum, gauge flux, and section boundary terms must be compatible with the variational principle. |

The exact obstruction is therefore not the 4D Einstein tensor. The obstruction is:

```text
alpha_W W_s(s_BH)
  + E_s^YM(A_BH,s_BH)
  + E_s^theta(A_BH,epsilon_BH,beta_BH,s_BH)
  + E_s^Phi(lambda_BH,epsilon_BH,beta_BH,s_BH)
  + E_s^cross
  = 0
```

together with the simultaneous connection and IG equations. The known Willmore-only
branch has:

```text
W_s(s_Schwarzschild) != 0
```

schematically through:

```text
H_Schw ~ M/r^2,
Delta^perp H_Schw ~ M/r^4,
hat B_Schw != 0,
Q^TF(B_s) ~ M^2/r^4.
```

Kerr has the same structural danger plus rotation-dependent residuals. Since Kerr is
Ricci-flat but not conformally flat, a Schwarzschild-only cancellation would not be
enough for the exact vacuum GR gate.

## 4. Weak-field compatibility check

The canon weak-field result is compatible with the exact tuple, but it does not solve it.

The weak-field Schwarzschild check uses the small parameter `epsilon_N = M/r` and keeps
only the leading reconstruction-grade bookkeeping:

```text
G[g_Schw] = 0                                  exactly
Q(B_s) is quadratic in B_s                     no leading linear contribution
E^Psi = 0 or O(epsilon_N^2)                    if Psi=0 is consistent
R_fail^full = 0 at O(M/r)                      in the canon's non-standard combined convention
```

The exact tuple asks a stronger question:

```text
W_s + section variations from A, theta, IG, and cross terms = 0
E_A = 0
E_beta = 0
E_epsilon = 0
E_Psi = 0
```

The weak-field result only says the leading Ricci/Gauss/Q/Psi bookkeeping does not
contradict solar-system-scale linearized Schwarzschild. It leaves these exact questions
unanswered:

```text
Does the linearized Yang-Mills equation solve D_A^*F_A = theta for the Schwarzschild section?
Does the full section equation cancel Delta^perp H_Schw?
Does the IG equation allow the needed nonzero theta?
Do the same cancellations survive near r ~ 2M?
Do they survive the Kerr angular-momentum terms?
```

So the weak-field pass is not falsified by this gate. It is bounded: it cannot be
promoted to exact nonlinear black-hole recovery.

## 5. Obstruction classification

The obstruction type is:

```text
primary classification:
  blocked by action-underdefinition and IG-source underdefinition.

branch-local classification:
  genuine strong-field failure for the Willmore-only / bare-free-beta branches.
```

Why not a global "genuine strong-field failure" yet?

The full GU action/operator spine deliberately keeps open terms that can affect the exact
section equation:

```text
E_s^YM,
E_s^theta,
E_s^Phi,
E_s^cross,
and possibly E_A^W/E_beta^W if II_s^H is represented through theta.
```

Until those are fixed by a primary action and an IG variation rule, the exact black-hole
gate is not computable. However, the already specified weaker branches do fail:

```text
Willmore-only:
  W_s(s_Schwarzschild) != 0, Kerr expected nonzero.

bare free beta plus only |theta|^2:
  E_beta forces theta = 0, removing the advertised source.
```

Thus a precise status statement is:

```text
GU exact black-hole recovery: blocked/open.
Current Willmore-only exact black-hole recovery: fail.
Current bare-free-beta theta-source branch: fail.
Weak-field Schwarzschild canon: still conditionally resolved inside its scope.
```

## 6. Next meaningful proof/computation step

Do not start with Kerr. The next useful step is a Schwarzschild Branch 2A computation:

1. Derive or reject the A-independent IG constraint

   ```text
   Phi(epsilon,beta,s)=0
   ```

   from primary GU structure, tau-plus / double-coset geometry, or a real
   Stueckelberg slice. If this cannot be done, switch the gate to Branch 3 and use
   `theta_eff`.

2. With that branch fixed, compute the exact Schwarzschild section equation:

   ```text
   alpha_W W_s(s_Schw)
     + E_s^YM
     + E_s^theta
     + E_s^Phi
     + E_s^cross
     = 0
   ```

   in the horizontal-normalized `II_s^H` convention and with the `j_s` normalization
   carried explicitly.

3. Separately solve the connection equation:

   ```text
   g_A^-2 D_A^*F_A - c_theta theta + ... = 0
   ```

   for a finite-action `A_Schw` with the same asymptotic mass data.

4. Only after Schwarzschild closes or fails exactly, run Kerr with angular momentum
   boundary data. A spherical cancellation does not imply a rotating one.

I did not add `tests/gu_blackhole_el_gate.py` in this pass. A real executable audit should
check the normal Willmore residual, the projected IG beta equation, or a branch-fixed
symbolic invariant of the exact tuple. A test that only rechecks `Ric[g_Schw]=0` would be
true but would not audit the GU obstruction.

## Sources Read

- `explorations/cycle-gates-and-audits/goal-draft-primary-gu-action-operator-spec-2026-06-24.md`
- `explorations/cycle-gates-and-audits/goal-draft-ig-constraint-derivation-2026-06-24.md`
- `explorations/cycle-gates-and-audits/gu-typed-operator-action-spine-2026-06-24.md`
- `explorations/misc/gu-closed-loop-action-ig-branch-2026-06-24.md`
- `explorations/cycle-gates-and-audits/gu-action-4d-physics-gate-2026-06-24.md`
- `canon/schwarzschild-weak-field-rfail.md`
- `explorations/cycle-gates-and-audits/live-claim-dag-fault-finality-ledger-2026-06-24.md`
- `explorations/cycle-gates-and-audits/gu-minimal-action-spec-2026-06-24.md`
- `explorations/misc/ig-dynamics-nonzero-theta-action-gate-2026-06-24.md`
- `explorations/geometry-curvature-emergence/rfail-non-umbilic-schwarzschild-2026-06-23.md`
