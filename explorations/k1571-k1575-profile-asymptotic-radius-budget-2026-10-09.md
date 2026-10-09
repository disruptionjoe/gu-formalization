---
title: "Profiled coefficient asymptotics and analytic-radius budget"
status: active_research
document_role: exploration
target_claim: INTERNAL_TARGET__K1569_FACTORIAL_SAME_RADIUS_REWEIGHTING
created: "2026-10-09"
updated_at: "2026-10-09"
---

# Profiled coefficient asymptotics and analytic-radius budget

> **GU-COMPARATOR-ROUTING:** This artifact studies a repository-owned
> finite-cutoff scalar-field and gauge-PDE control. It is not a source-native
> GU action, physical state space, observed carrier, prediction, confirmation,
> or falsification of a registered source claim. Conventional comparator
> conclusions bind only the model stated here and do not transfer to
> Weinstein's source-native mechanism without an explicit typed bridge.
>
> **Classification:**
> `INTERNAL_TARGET__CONDITIONAL_MATHEMATICAL_CONTROL__NO_SOURCE_VERDICT`

```yaml
gu-typed-objects:
  carrier: finite_cutoff_real_scalar_q_space_plus_smooth_lifted_charge_fields
  pairing_or_form: stationary_gaussian_dirichlet_form_and_charge_analytic_graph_energy
  real_structure: real_fourier_coordinates_with_complex_charge_pairing_in_pde_arc
  grading: cube_cutoff_modes_and_charge_powers_Q_n
  action_owner: repository_control_not_source_owned
  target_object: stationary_diagonal_gaussian_coefficient_and_K1568_adjacent_charge_shift
  observed_intertwiner: UNTYPED
```

## Scope and preflight bookend

The quantum arc keeps K1566--K1567's normalized three-torus, cube Fourier
cutoff, positive mass and coupling, and stationary translation-invariant
diagonal Gaussian trial class. Its question is whether the profiled continuum
recovery is the actual coefficient limit inside that class and what its
coupling asymptotics say. The unrestricted non-Gaussian ground energy remains
a different problem.

The PDE arc keeps K1568's smooth periodic temporal-gauge core and K1450's
charge-analytic weights. K1569 already proves that a fixed factorial radius
cannot bound the adjacent shift. The live alternatives are to spend analytic
radius dynamically, strengthen the charge tail, or find a genuine
gauge/spacetime cancellation.

The route-changing checks are structural. Convex duality and the exact
finite-cutoff Euler equation dominate another Gaussian trial search. A general
weighted-shift criterion dominates trying isolated weight formulas. The source
claims SC-ACT-01/02/06 remain assertions and SC-META-53 remains uncertain;
none supplies the action, measure, Hamiltonian, physical quotient or observed
map used by these repository controls.

## K1571 — weak- and strong-coupling coefficient asymptotics

Retain K1566's notation

```text
A(kappa)=(1/2) int_Q (r^2+kappa)^(-1/2) dx,
D(kappa)=c_C-A(kappa),
kappa_g=24gD(kappa_g).
```

Differentiation gives

```text
D'(kappa)=(1/4) int_Q (r^2+kappa)^(-3/2) dx.       (1)
```

Only the interior cube origin contributes to the logarithmic divergence. A
ball contained in the cube supplies the full solid angle, while its complement
is uniformly integrable. Therefore

```text
D(kappa) ~ (pi/2) kappa log(1/kappa).              (2)
```

Substitution into the self-consistency equation yields

```text
g log(1/kappa_g) -> 1/(12pi),    g -> 0.           (3)
```

The coefficient gain has a sharper exact identity. Since
`dF_*/dD=kappa/2`, integration by parts and
`g=kappa_g/[24D(kappa_g)]` give

```text
6gc_C^2-h_g^prof
 = (1/2) int_0^(kappa_g) D(u)du
   -kappa_gD(kappa_g)/4.                            (4)
```

Equation (2) makes the logarithmic pieces cancel in (4), leaving

```text
(6gc_C^2-h_g^prof)/kappa_g^2 -> pi/16,
g log(1/(6gc_C^2-h_g^prof)) -> 1/(6pi).            (5)
```

Thus the every-positive-coupling improvement is real but beyond every power
of `g` near zero.

At strong coupling, cube moments give

```text
A(kappa)=4kappa^(-1/2)-2kappa^(-3/2)+O(kappa^(-5/2)),
F_*(A(kappa))=2sqrt(kappa)-c_Omega/2
              +3kappa^(-1/2)+O(kappa^(-3/2)).      (6)
```

Solving the self-consistency equation and inserting (6) gives

```text
sqrt(kappa_g)=sqrt(24c_C g)-2/c_C+o(1),
h_g^prof=4sqrt(24c_C g)-4/c_C-c_Omega/2+o(1).      (7)
```

These are class-specific coefficient asymptotics, not an unrestricted lower
coefficient or a bounded-error ground-energy expansion.

## K1572 — exact finite-cutoff Gaussian minimizer

For fixed cutoff point variance `V`, minimize

```text
sum_k omega_k(s_k+s_k^(-1)-2)/4
subject to V=sum_k s_k/(2omega_k).                 (8)
```

Strict convexity gives the unique constrained profile

```text
s_(N,k)=omega_k/sqrt(omega_k^2+kappa).             (9)
```

Set

```text
A_N(kappa)=(1/2)sum_k(omega_k^2+kappa)^(-1/2),
D_N(kappa)=C_N-A_N(kappa).                         (10)
```

On the active mean branch, `y_N=3D_N-m^2/(4g)`, and the exact reduced Euler
equation is

```text
kappa+3m^2=24gD_N(kappa).                          (11)
```

Finite mass reveals a feature absent from the leading continuum equation.
Because `D_N` is increasing and strictly concave,

```text
f_N(kappa)=kappa+3m^2-24gD_N(kappa)
```

is strictly convex. For every fixed `g>0` and all sufficiently large `N`, its
minimum is negative, while `f_N(0)>0` and `f_N(kappa)->infinity`. Hence (11)
has exactly two roots. The smaller root is a local maximum separating the
vacuum from the active branch. The larger root is the unique active local
minimum; K1567's strict coefficient gain makes it the global
stationary-diagonal minimum. The inactive branch is at least the vacuum
because its interaction increment is `3gD_N^2`, and the high-variance branch
has nonnegative free cost without an interaction gain.

Riemann-sum convergence then gives

```text
kappa_(g,N)^+/N^2 -> kappa_g,
kappa_(g,N)^-/N^2 -> 0,
E_N^(stationary diagonal Gaussian)/N^4 -> h_g^prof. (12)
```

K1567's recovery is therefore asymptotically exact in the complete stationary
diagonal Gaussian class. Equation (12) does not extend to non-Gaussian states.

## K1573 — moving-radius absorption

Let `X_n=a_n(rho)H_n`, with `a_n(rho)=rho^(2n)/n!`. Then

```text
G_rho=sum_n X_n,
partial_rho G_rho=(2/rho)sum_n nX_n.               (13)
```

K1568's adjacent shift can be rewritten as

```text
S_rho=(1/rho)sum_n sqrt(n+1)sqrt(X_nX_(n+1)).      (14)
```

For every `epsilon>0`, weighted Young gives

```text
S_rho <= (epsilon/4)partial_rho G_rho
       +(epsilon+epsilon^(-1))G_rho/(2rho).         (15)
```

Suppose the smooth-core hierarchy has the form

```text
dG_rho/dt <= L(t)G_rho+C_mB_A(t)S_rho.             (16)
```

Along a decreasing radius, the chain rule adds
`rho' partial_rho G`. Choosing

```text
epsilon=-4rho'/(C_mB_A)
```

absorbs the derivative term in (15). The remaining scalar coefficient is

```text
L-2rho'/rho+C_m^2B_A^2/[8rho(-rho')].              (17)
```

The transparent choice `-rho'=C_mB_A/4` sets `epsilon=1` and leaves
`L+C_mB_A/rho`. In particular, the radius stays positive on every interval
satisfying

```text
(C_m/4) int B_A < rho(0).                          (18)
```

This is a one-moving-radius formulation of the current normal form. It makes
the price explicit; it does not prove that the global `B_A` budget is finite.

## K1574 — general weight-ratio boundary

For arbitrary positive weights `w_n`, define

```text
G_w=sum_n w_nH_n,
S_w=sum_n w_n sqrt(H_nH_(n+1)).                    (19)
```

Writing `X_n=w_nH_n` shows that

```text
S_w=sum_n q_n sqrt(X_nX_(n+1)),
q_n=sqrt(w_n/w_(n+1)).                             (20)
```

Therefore `S_w<=CG_w` for every nonnegative sequence if and only if
`q=sup q_n<infinity`. Weighted Cauchy gives `C<=q`; a two-tier concentration
gives `C>=q/2` and proves necessity.

For K1450's weights,

```text
w_n=rho^(2n)/n!  =>  q_n=sqrt(n+1)/rho,            (21)
```

so same-radius control fails. Geometric weights have `q_n=1/rho` and control
the shift, but impose a strictly stronger charge tail. Exact
exponential-generating Leibniz normalization uses square-root weights
proportional to `rho^n/n!`, for which `q_n=(n+1)/rho`; it is even less
compatible with a bounded adjacent shift.

The internal target
`INTERNAL_TARGET__K1569_FACTORIAL_SAME_RADIUS_REWEIGHTING` is therefore
excluded: changing notation inside the same factorial hierarchy cannot remove
the shift. Stronger regularity, radius expenditure or a structural
gauge/spacetime cancellation remain live.

## K1575 — protected integration

The bridge census is now 290 rows: 211 satisfied, ten conditional, 65
excluded and four missing. SC-ACT-01/02/06 remain `ASSERTS`; SC-META-53
remains `UNCERTAIN`; the physics ledger remains 33 SAME / 22 DIFFERS / 31
NEEDS / 2 OVER-DETERMINED; K1145/K1150 remain `0/7`. No source, ledger,
canon, paper, prediction, confirmation or public-posture state moves.

## Postflight hostile bookend

The finite-cutoff hostile pass rejected the tempting one-root transcription of
the continuum equation. The mass term creates two positive critical roots:
the smaller is a barrier and only the larger minimizes. The weight-theorem
pass also rejected the over-tight proposed upper constant `(1+q)/2`; the
general bound is `q`, while the two-tier lower witness is `q/2`.

The remaining quantum debt is genuinely unrestricted: a non-Gaussian matching
lower coefficient or bounded-error recentering. The remaining PDE debt is a
global coefficient estimate strong enough to keep (18) positive, or a
gauge/spacetime mechanism that removes the radius expenditure. The
source-owned action/measure/Hamiltonian tuple remains a separate admission
gate.
