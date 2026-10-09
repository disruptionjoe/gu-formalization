---
title: "Critical-shell all-term balance and fractional singular holonomy"
status: active_research
document_role: exploration
target_claim: INTERNAL_TARGET__CRITICAL_SHELL_FULL_ENERGY_AND_FRACTIONAL_HOLONOMY_SUFFICIENCY
created: "2026-10-09"
updated_at: "2026-10-09"
---

# Critical-shell all-term balance and fractional singular holonomy

> **GU-COMPARATOR-ROUTING:** This artifact studies a repository-owned
> finite-cutoff quartic Hamiltonian and a conditional harmonic spectral model.
> It is not a source-native GU action, physical state space, observed carrier,
> prediction, confirmation, or falsification of a registered source claim.
> Conventional comparator conclusions bind only the models stated here.
>
> **Classification:**
> `INTERNAL_TARGET__CONDITIONAL_MATHEMATICAL_CONTROL__NO_SOURCE_VERDICT`

```yaml
gu-typed-objects:
  carrier: profiled_stationary_gaussian_shell_channels_plus_compact_fractional_sobolev_primitives
  pairing_or_form: optimized_gaussian_dirichlet_wick_form_plus_fourier_sobolev_pairing
  real_structure: real_finite_q_space_and_real_finite_dimensional_spectral_values
  grading: ultraviolet_shell_inflation_plus_fractional_frequency_weight
  action_owner: repository_control_not_source_owned
  target_object: critical_shell_full_energy_balance_and_singular_continuous_holonomy_l1_sufficiency
  observed_intertwiner: UNTYPED
```

## Scope and preflight bookend

K1626 constructs a Gaussian location channel with critical `Theta(N^3)`
information and `Theta(N^4)` missing Fisher information, but K1627 correctly
leaves the full energy balance open. Because that channel's output is itself a
stationary diagonal Gaussian, the cheapest decisive continuation is an exact
all-term comparison with K1572's profiled minimizer.

The independent spectral arc weakens K1628's `H^1` sufficient condition. The
Fourier `L1` conclusion needs only fractional `H^s` regularity with `s>1/2`.
This wider class contains compact continuous BV primitives whose derivatives
are atom-free and purely singular, including an explicit translated Cantor
construction.

SC-ACT-01/02/06 remain assertions and SC-META-53 remains uncertain. The
physics ledger stays 33 SAME / 22 DIFFERS / 31 NEEDS / 2 OVER-DETERMINED.
LT-SM8, LT-GR6b, RA-F1 and AC-F1 do not move. No source, ledger, canon,
paper, prediction, confirmation, or public-posture state moves.

## K1631 — exact full-energy identity for a shell inflation

Use the continuum notation of K1566--K1572 on `Q=[-1,1]^3`. For a positive
stationary diagonal profile `s`, set

```text
A(s)=(1/2) int_Q s(x)/|x| dx,
F(s)=(1/4) int_Q |x|[s+s^(-1)-2] dx.              (1)
```

On the active optimized-mean branch the leading coefficient functional is

```text
J_g(s)=F(s)+6g A(s)[2c_C-A(s)].                    (2)
```

Let `s_*(x)=|x|/sqrt(|x|^2+kappa_g)` be K1572's profiled minimizer,
`A_*=A(s_*)`, and `D_*=c_C-A_*`. The stationarity relation is
`kappa_g=24gD_*`. The scalar identity

```text
u+u^(-1)-v-v^(-1)-(1-v^(-2))(u-v)
  =(u-v)^2/(u v^2)                                  (3)
```

and the exact quadratic remainder of the Wick term give, for every positive
profile `s` that remains on the active branch,

```text
J_g(s)-J_g(s_*)
 =(1/4) int_Q |x| (s-s_*)^2/(s s_*^2) dx
  -6g[A(s)-A_*]^2.                                  (4)
```

No Fisher term is being considered in isolation in (4): it is the complete
leading free-plus-optimized-Wick coefficient difference.

For a symmetric measurable shell patch `E` and fixed `rho>0`, inflate only
that shell:

```text
s_rho=(1+rho)s_* on E,       s_rho=s_* off E.       (5)
```

Writing

```text
W_E=int_E sqrt(|x|^2+kappa_g) dx,
B_E=int_E 1/sqrt(|x|^2+kappa_g) dx,                 (6)
```

equation (4) becomes the exact all-term identity

```text
J_g(s_rho)-J_g(s_*)
 =rho^2[W_E/(4(1+rho))-(3g/2)B_E^2].                (7)
```

## K1632 — critical information can coexist with a positive leading penalty

Choose `0<a<b` and a symmetric positive-measure Jordan-measurable shell patch
`E subset {a<=|x|<=b}` whose boundary has Lebesgue measure zero (for example,
a sufficiently thin symmetric annular patch). Its volume can be made
arbitrarily small while remaining fixed as `N` grows. The elementary bounds

```text
W_E >= sqrt(a^2+kappa_g)|E|,
B_E <= |E|/sqrt(a^2+kappa_g)                         (8)
```

show that the right side of (7) is strictly positive whenever

```text
0<|E|<(a^2+kappa_g)^(3/2)/[6g(1+rho)].              (9)
```

Shrink `E` further if needed so that
`(rho/2)B_E<D_*`; then the inflated profile remains on the active branch.
The corresponding symmetric lattice shell has `d_N=Theta(N^3)` modes.
K1626's channel formulas still give

```text
I(M_N;X_N)=(d_N/2)log(1+rho)=Theta(N^3),
Delta_N=[rho/(1+rho)]sum_(k in E_N)omega_k/s_(N,k)
       =Theta(N^4).                                  (10)
```

Boundary-null Jordan measurability makes the lattice Riemann sums converge, so
applying them to (7) gives

```text
Q_N(Law(X_N))-lambda_N^prof
 =c_(g,rho,E)N^4+o(N^4),     c_(g,rho,E)>0.         (11)
```

Thus the exact K1626 critical channel does not lower the profiled coefficient;
for the admitted thin fixed-ratio shell it pays a positive leading penalty.
This resolves the witness's full variational balance without weakening K1627's
method-sharpness result. It does not control genuinely non-Gaussian or
nonstationary laws.

## K1633 — fractional `H^s`, `s>1/2`, suffices for holonomy `L1`

Use the Fourier convention
`widehat G(t)=int exp(-it omega)G(omega)d omega` and define

```text
||G||_(H^s)^2=(1/(2pi))int_R (1+t^2)^s|widehat G(t)|^2 dt.  (12)
```

For scalar or finite-dimensional vector-valued `G in H^s(R)` with `s>1/2`,
weighted Cauchy--Schwarz gives

```text
||widehat G||_1
 <=[int_R(1+t^2)^(-s)dt]^(1/2)
    [int_R(1+t^2)^s|widehat G(t)|^2dt]^(1/2)
 =C_s||G||_(H^s),                                    (13)

C_s=[2pi sqrt(pi) Gamma(s-1/2)/Gamma(s)]^(1/2).      (14)
```

The threshold in this argument is exact: the weight integral is finite
precisely for `s>1/2`. K1628 is the special stronger case `s=1` obtained from
an `L2` derivative. The fractional theorem needs neither absolute continuity
nor an `L2` derivative.

## K1634 — an explicit singular-continuous positive class

Let `mu_C` be the standard middle-thirds Cantor probability measure on
`[0,1]`, let

```text
F_C(x)=mu_C((-∞,x]),
G_a(x)=F_C(x)-F_C(x-a),       a>1.                  (15)
```

Then `G_a` is compactly supported in `[0,1+a]`, continuous and of bounded
variation, with

```text
DG_a=mu_C-tau_a mu_C.                               (16)
```

The derivative measure is atom-free and purely singular. The Cantor
distribution is Hölder with exponent
`alpha=log(2)/log(3)`, so the same is true of `G_a`. Monotonicity gives an
`L1` increment bound of order `|h|`; combining it with the Hölder `L-infinity`
increment bound makes the squared `L2` increment order `|h|^(1+alpha)`.
The difference-quotient characterization therefore gives

```text
G_a in H^s(R) for every s<(1+alpha)/2.              (17)
```

Choose any `1/2<s<(1+log(2)/log(3))/2`, for example `s=3/4`. K1633 then gives
`widehat G_a in L1`. This supplies an explicit compact primitive with an
atom-free singular-continuous derivative inside the positive holonomy class.
It does not prove that every atom-free singular measure is sufficient.

## K1635 — protected integration and hostile bookend

The bridge census is now 350 rows: 271 satisfied, ten conditional, 65
excluded, and four missing. K1631--K1632 close K1626's own full all-term
balance with a positive leading penalty while preserving the open unrestricted
non-Gaussian/nonstationary coefficient problem. K1633--K1634 enlarge the
positive spectral class from `H^1` to fractional `H^s`, `s>1/2`, and include
an explicit singular-continuous derivative measure.

Hostile review rejects promoting the shell result to all critical-capacity
channels, all Gaussian heterogeneity, or the unrestricted coefficient. It
also rejects treating `s=1/2` as sufficient, treating atom-freedom alone as
sufficient, or transferring the Fourier-amplitude budget to electric-field
`L1`, nonlinear remainders, or a source-owned flow.

The next quantum wake is a genuinely non-Gaussian/nonstationary all-term
competitor or a global Fisher/defect coercivity theorem. The next PDE wake is
deriving fractional primitive regularity and integrable
curvature/current/radial remainders from one source-owned nonlinear action and
domain. The source-owned action/measure/Hamiltonian tuple remains separate.

## Postflight bookend

The quantum result now distinguishes method sharpness from variational effect:
critical information can carry a leading missing-Fisher term while the exact
full energy rises at leading order. The spectral result shows that absolute
continuity is not necessary for the positive holonomy class; fractional
regularity can admit compact singular-continuous derivatives. Protected source,
ledger, canon, paper, prediction, confirmation, and public-posture states are
unchanged.
