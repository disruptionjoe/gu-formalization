---
title: "K1676--K1680 non-orbit cardinal-product descent"
status: active_research
document_role: exploration
claim_verdict: proved_at_finite_cutoff_leading_scale
updated_at: "2026-10-10"
---

# K1676--K1680: a non-orbit cardinal product descends at leading order

## Result and boundary

Fix `g>0` and the K1572 profiled stationary Gaussian covariance `S_(g,N)`.
There are stationary, centered, covariance-matched, positive smooth
finite-Fisher laws `mu_N` and a constant `c_g>0` such that, along all large
cutoffs,

```text
Q_N(mu_N) <= lambda_N^statG - c_g N^4.
```

Consequently

```text
limsup_N E_N/N^4 <= h_g^prof-c_g < h_g^prof.
```

This decides the unrestricted *upper-coefficient* question against the
profiled Gaussian. It does not identify the true coefficient, prove a matching
lower bound, construct a minimizer or continuum state, give an `E_N+O(1)`
recentring, or supply a source-owned physical action or observation.

## K1676: the scalar Fisher price is quartic

For `0<t<1`, let

```text
Y_t=sqrt(t) epsilon+sqrt(1-t) Z,
```

where `epsilon` is symmetric Rademacher and `Z` is standard Gaussian. Its
density is everywhere positive, centered, and has variance one. Relative to
the standard Gaussian its exact score is

```text
s_t(x)=[sqrt(t)tanh(sqrt(t)x/(1-t))-t x]/(1-t).
```

The density ratio has the weighted Hermite expansion

```text
p_t/phi=1-(t^2/12)H_4+O(t^3),
s_t=-(t^2/3)H_3+O(t^3),
```

so, using `E H_3(Z)^2=6`,

```text
j(t):=E s_t(Y_t)^2=(2/3)t^4+O(t^5).
```

In particular there are absolute `t_0,C>0` with `j(t)<=Ct^4` on
`0<t<=t_0`. The fourth cumulant is exact:

```text
kappa_4(Y_t)=E Y_t^4-3=-2t^2.
```

Thus Fisher begins two powers later than the negative cumulant.

## K1677: real cardinal packets carry order-N4 fourth mass

Choose a fixed sufficiently small cube fraction `alpha>0` and an odd integer
`n_N~alpha N`. On the symmetric three-dimensional Fourier cube with
`d_N=n_N^3`, the normalized real cardinal functions are translates of the
product Dirichlet kernel. With normalized Haar measure,

```text
int |D_(j,N)|^4
  = [(2n_N+n_N^(-1))/3]^3.
```

The identity follows from the exact one-dimensional additive-energy count
`sum_s r_n(s)^2=(2n^3+n)/3`, divided by `n^2`, and tensorization.

Apply the K1572 covariance square-root multiplier to these orthonormal
whitened packets, writing the resulting field packets as `psi_(j,N)`. On the
fixed scaled cube the multiplier has size `a_N^2=Theta_g(N^-1)` and relative
oscillation `O_g(alpha^2)`. Hausdorff--Young stability of the finite
trigonometric polynomial therefore gives, after choosing `alpha` small enough,

```text
int |psi_(j,N)|^4 >= c_g N,
L_N:=sum_(j=1)^d_N int |psi_(j,N)|^4 >= c_g N^4.
```

The matching easy bound is `L_N<=C_gN^4`. This is a localized packet estimate,
not an assertion that the K1572 multiplier is constant.

## K1678: product composition and the exact full-gap balance

In K1572-whitened real coordinates put independent copies of `Y_t` on the
cardinal block and standard Gaussians on its orthogonal complement. Push the
law forward by `S_(g,N)^(1/2)`. Its mean and covariance exactly match the
profiled Gaussian, so K1637's covariance Bregman term is `A_N=0`.

Orthogonal score covariance and the chain rule give

```text
R_(Omega,N)/4=(j(t)/4)T_N,
T_N=Tr_E[S_(g,N)^(-1/2) Omega_N S_(g,N)^(-1/2)]
    <=C_gN^4.
```

Cumulant tensorization, which is invariant under the orthogonal cardinal
change of coordinates, gives the exact interaction defect

```text
D_N=-2t^2 L_N.
```

Therefore the K1637 identity reads

```text
Q_N-lambda_N^statG=(j(t)/4)T_N-2g t^2L_N.
```

## K1679: stationarity and strict leading descent

Average the law over spatial translations. The mean and covariance remain
those of K1572, the translation-invariant quartic expectation (hence `D_N`)
is unchanged, and convexity of relative Fisher information can only decrease
`R_(Omega,N)`. Consequently

```text
Q_N-lambda_N^statG
 <= (C C_g/4)t^4N^4-2g c_g t^2N^4.
```

Choose `alpha` first, depending only on fixed `g`, so the packet lower bound
holds. Then choose one fixed `0<t<=t_0`, also depending only on `g`, with
`(C C_g/4)t^2<g c_g`. The right side is at most `-c'_gN^4` for all large `N`.
The construction is genuinely non-orbit: it independently perturbs
`Theta(N^3)` cardinal coordinates and is not a translation/global-phase
mixture of one profile.

## K1680: protected integration and next frontier

The bridge census becomes 395 rows: 316 satisfied, ten conditional, 65
excluded, and four missing. SC-ACT-01/02/06 remain `ASSERTS`; SC-META-53
remains `UNCERTAIN`; the standing ledger remains 33 SAME / 22 DIFFERS / 31
NEEDS / 2 OVER-DETERMINED; and K1145/K1150 remain 0/7. No source, ledger,
canon, paper, prediction, confirmation, or public verdict moves.

The next coefficient work is to optimize/localize this trial and seek a
matching unrestricted lower bound or true coefficient. The independent class
route is unknown-profile/growing-latent entropy with a common Gaussian floor.
Compactness and Mosco questions wait for the true `E_N+O(1)` recentering. The
source-owned action/domain/state/observation tuple remains a separate gate.
