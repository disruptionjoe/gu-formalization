---
title: "Negative Wick-defect tangent and evolving-holonomy radius budget"
status: active_research
document_role: exploration
target_claim: INTERNAL_TARGET__NEGATIVE_WICK_DEFECT_AND_HARMONIC_HOLONOMY_CONTROL
created: "2026-10-09"
updated_at: "2026-10-09"
---

# Negative Wick-defect tangent and evolving-holonomy radius budget

> **GU-COMPARATOR-ROUTING:** This artifact studies a repository-owned
> finite-cutoff quartic variational problem and a periodic gauge-PDE control.
> It is not a source-native GU action, physical state space, observed carrier,
> prediction, confirmation, or falsification of a registered source claim.
> Conventional comparator conclusions bind only the models stated here.
>
> **Classification:**
> `INTERNAL_TARGET__CONDITIONAL_MATHEMATICAL_CONTROL__NO_SOURCE_VERDICT`

```yaml
gu-typed-objects:
  carrier: finite_cutoff_translation_invariant_wavefunctions_plus_periodic_charged_fields
  pairing_or_form: quartic_schrodinger_form_fixed_moment_fisher_form_and_harmonic_adapted_energy
  real_structure: real_finite_q_space_with_complex_u1_charged_pde_field
  grading: gaussian_tangent_normal_split_and_charge_powers_Q_n
  action_owner: repository_control_not_source_owned
  target_object: negative_wick_defect_compensation_and_K1573_harmonic_radius_budget
  observed_intertwiner: UNTYPED
```

## Scope and preflight bookend

The quantum arc keeps the finite cube cutoff, positive mass and positive
coupling of K1433--K1577. It asks a local structural question before attempting
another global coefficient estimate: is the profiled Gaussian stationary in
the unrestricted finite-dimensional form problem, and can negative Wick
defect be linearly dominated by the excess Fisher cost near that Gaussian?

The PDE arc keeps the periodic temporal/Coulomb-gauge convention of
K1568--K1579. It writes the spatial connection as its harmonic mean plus a
mean-zero part and differentiates the energy adapted to the moving harmonic
operator. The result is conditional control, not a completed nonlinear flow.

SC-ACT-01/02/06 remain assertions and SC-META-53 remains uncertain. The
physics ledger stays 33 SAME / 22 DIFFERS / 31 NEEDS / 2 OVER-DETERMINED. No
source, ledger, canon, paper, prediction, confirmation or public-posture state
moves.

## K1581 — every profiled Gaussian has a strict unrestricted residual descent

Fix a finite cutoff and let `H_N=H_(0,N)+gW_N`, `g>0`, on the finite
real Q-space. Let `G_N` be any normalized, nondegenerate real Gaussian,
including K1572's unique larger stationary diagonal Gaussian minimizer, and
write

```text
lambda_G=<G_N,H_N G_N>,
r_N=(H_N-lambda_G)G_N.                              (1)
```

The quotient `(H_(0,N)G_N)/G_N` is a polynomial of degree at most two in the
Q-coordinates. The Wick interaction `W_N` is a nonconstant polynomial with a
nonzero quartic homogeneous part. Hence `r_N` cannot vanish almost everywhere:
no nonzero Gaussian is an eigenfunction of the positive-coupling quartic
Hamiltonian.

Put `sigma_N=||r_N||>0` and `u_N=r_N/sigma_N`. The exact compression to
`span{G_N,u_N}` is

```text
[ lambda_G   sigma_N ]
[ sigma_N    mu_N    ],    mu_N=<u_N,H_Nu_N>.       (2)
```

Its lower eigenvalue is strictly below `lambda_G`. Since translations commute
with `H_N` and K1572's Gaussian is translation invariant, `r_N` and the Ritz
vector are translation invariant too. Therefore K1572's finite-cutoff
Gaussian value is not the unrestricted translation-invariant infimum.

This is a strict finite-cutoff statement only. Equation (2) gives no uniform
lower bound on the gap without cutoff estimates for `sigma_N` and `mu_N`.
It does not change the K1577 class coefficient, prove a different unrestricted
coefficient, or exclude bounded-error recentering.

## K1582 — linear negative defect beats quadratic Fisher excess locally

At K1572's interior Gaussian minimizer, split the real form tangent into the
Gaussian moment tangent (normalization, mean and covariance variations) and
its orthogonal complement. Optimization over the Gaussian parameters makes
`r_N` orthogonal to the moment tangent. Thus `-r_N` is a nonzero fixed-moment
first-order descent direction.

Equivalently, use a bounded smooth approximation to `-r_N/G_N`, project away
the constant, linear and quadratic Gaussian statistics, and use the local
Gaussian exponential family to correct normalization, mean and covariance
exactly. This produces positive smooth finite-Fisher densities `rho_epsilon`
with the same moments as `G_N` and

```text
F(rho_epsilon)-F(G_N)=O(epsilon^2),
E_(rho_epsilon)W_N-E_(G_N)W_N=-c_N epsilon+O(epsilon^2),
c_N>0.                                               (3)
```

By K1534 the second line is precisely the integrated Wick defect at fixed
moments. It is negative for sufficiently small positive `epsilon`. Therefore
there is no local inequality of the form

```text
F(rho)-F(G_N) >= c [-D(rho)]_+                      (4)
```

with any fixed positive `c` on a neighborhood of the Gaussian fixed-moment
manifold. The proposed linear Fisher payment for negative defect is false even
at one cutoff. A quadratic or cutoff-dependent compensation, or a global
nonperturbative lower bound, remains possible and is exactly what a leading
coefficient theorem would need.

The same construction explains K1581 without claiming an asymptotic gap: the
Fisher penalty starts at second order while the quartic interaction sees the
normal residual at first order.

## K1583 — moving holonomy costs total variation, not amplitude

Let `a(t)` be a prescribed continuously differentiable harmonic connection on
the torus and consider

```text
partial_t^2 phi+L_(a(t))phi=0,
L_a=-(grad-i e a)^2+m^2,    m>0.                   (5)
```

With

```text
H_a=(1/2)(||partial_t phi||_2^2+<phi,L_a phi>),     (6)
```

the equation cancels the state derivatives and gives

```text
dH_a/dt=(1/2)<phi,(partial_t L_a)phi>
       =-e dot(a) dot sum_k (k-ea)|phi_k|^2.        (7)
```

Since `2m|p|<=|p|^2+m^2`,

```text
|dH_a/dt| <= (|e|/m)|dot(a)| H_a,
H_a(t)<=H_a(0) exp((|e|/m) TV_[0,t](a)).           (8)
```

The global charge generator commutes with every `L_(a(t))`, so (7)--(8) hold
at each charge tier and after summing any positive charge-analytic hierarchy.
Static flat holonomy has zero cost, exactly recovering K1579. For Maxwell in
temporal gauge, `dot(a)=-mean(E)`: the new coefficient is the harmonic electric
field, not the gauge-potential amplitude. A continuous holonomy lift is used;
fixed large-gauge lattice shifts do not change its variation.

## K1584 — harmonic/oscillatory split and conditional positive radius

In Coulomb gauge decompose

```text
A(t,x)=a(t)+A_perp(t,x),
mean(A_perp)=0,    div(A_perp)=0.                   (9)
```

Use `D_(a(t))` in the principal energy. On the mean-zero part, torus Hodge and
Poincare estimates give, for the relevant integer `s`,

```text
||A_perp||_(H^(s+1)) <= C_s ||curl A||_(H^s),
||partial_t A_perp||_(H^s) <= ||E_perp||_(H^s).    (10)
```

Thus the raw harmonic term `|e|||a||` can be removed from K1573's radius
coefficient. The background-adapted hierarchy instead has the schematic
remainder budget

```text
R_s(t)=C_s[(|e|/m)|dot(a)|
           +|e| ||curl A||_(H^s)
           +|e| ||E_perp||_(H^s)
           +controlled nonlinear current/radial terms].                (11)
```

Consequently, on every interval where the adapted coercive hierarchy closes,

```text
rho(t)>=rho(0)-C_s int_0^t R_s(tau)dtau.            (12)
```

Finite holonomy variation and an integrable oscillatory/nonlinear remainder
therefore preserve a positive limiting radius when the right side of (12)
stays positive. This is the correct structural successor to the false raw
`int|a|` requirement.

No estimate here proves that the coupled nonlinear Maxwell-current dynamics
makes (11) integrable. Evolving holonomy, the mean electric mode, the current
feedback, radial term, coercivity and global continuation remain the live
debts.

## K1585 — protected integration and hostile bookend

The bridge census is now 300 rows: 221 satisfied, ten conditional, 65 excluded
and four missing. K1581--K1582 prove a strict finite-cutoff negative-defect
opening, not an unrestricted leading coefficient or bounded-error theorem.
K1583--K1584 replace the spurious flat-holonomy amplitude cost by a conditional
total-variation plus curvature/remainder budget, not a nonlinear global flow.

The hostile quantum check rejects three overclaims: strict Ritz descent has no
uniform gap yet; the first-order construction defeats only linear Fisher
compensation; and K1577's class theorem remains correct. The hostile PDE check
requires positive mass in (8), a continuous holonomy lift, Coulomb/mean-zero
Hodge control, and an independently proved `L1_t` remainder before any global
radius claim.

The next quantum wake is a quantitative cutoff estimate for the residual Ritz
matrix or a global nonlinear Fisher/defect inequality strong enough to decide
the unrestricted coefficient. The next PDE wake is an actual coupled estimate
making harmonic electric variation and the oscillatory/current remainder
integrable. The source-owned action/measure/Hamiltonian tuple remains a
separate admission gate.
