---
title: "K1681--K1685 localized cardinal upper coefficient"
status: active_research
document_role: exploration
claim_verdict: proved_at_fixed_shape_leading_scale
updated_at: "2026-10-10"
---

# K1681--K1685: localizing the non-orbit upper coefficient

## Result and boundary

K1679's unspecified strict decrement can be replaced by an explicit continuum
variational upper envelope. For every fixed `g>0`, define

```text
h_g^card-up
 = h_g^prof
   + inf_(C,0<t<1) [(j_R(t)/4) tau_g(C)-2g t^2 ell_g(C)],
```

where `C` is a fixed conjugation-symmetric rectangular scaled Fourier block, `j_R` is the
exact Rademacher--Gaussian relative Fisher information, and `tau_g,ell_g` are
the continuum trace and packet-fourth-mass functionals below. Then

```text
limsup_N E_N/N^4 <= h_g^card-up < h_g^prof.
```

This makes the upper target explicit. It does not identify the true
unrestricted coefficient or prove a matching lower bound.

## K1681: the universal symmetric weak-channel law

Let `X` be bounded, symmetric, centered and unit variance and put

```text
Y_t=sqrt(t)X+sqrt(1-t)Z.
```

Mehler's identity gives, relative to the standard Gaussian `phi`,

```text
p_t/phi
 = 1 + sum_(n>=3) t^(n/2) E[H_n(X)] H_n/n!.
```

Symmetry removes odd `n`, variance matching removes `n=2`, and
`E H_4(X)=kappa_4(X)`. Differentiating the logarithm in Gaussian-weighted
spaces gives

```text
grad log(p_t/phi)=(kappa_4(X)/6)t^2H_3+O_X(t^3),
j_X(t)=(kappa_4(X)^2/6)t^4+O_X(t^5).
```

Independence and cumulant homogeneity separately give the exact identity

```text
kappa_4(Y_t)=t^2 kappa_4(X).
```

## K1682: the sharp negative-kurtosis boundary

For every centered unit-variance seed,

```text
E X^4 >= (E X^2)^2=1,
kappa_4(X)>=-2.
```

Equality holds exactly when `X^2=1` almost surely; centering then forces the
symmetric Rademacher law. Thus Rademacher uniquely maximizes the negative
fourth-cumulant magnitude available at fixed small `t`.

Writing `u=-kappa_4(X)` and using limiting block weights `tau,ell`, K1681
gives the local gap

```text
(u^2 tau/24)t^4-g u ell t^2+O_X(t^5).
```

In the effective coordinate `q=u t^2`, the quadratic surrogate is

```text
(tau/24)q^2-g ell q,
```

with formal optimizer `q_*=12g ell/tau` and value
`-6g^2ell^2/tau` when that point lies in the controlled weak regime. This is
not a finite-`t` global optimality theorem: higher Hermite terms remain.

## K1683: continuum localization of both terms

Let `kappa_(g,N)^+/N^2 -> kappa_g` be the K1572 profile parameter and set

```text
b_g(xi)=sqrt(|xi|^2+kappa_g),
a_g(xi)=[2b_g(xi)]^(-1/2).
```

The two functions have different roles. `b_g` is the whitened relative-score
trace density because `omega_k/s_(N,k)=sqrt(omega_k^2+kappa_(g,N)^+)`.
`a_g` is the physical field covariance square-root multiplier because
`sqrt(s_(N,k)/(2omega_k))=[2sqrt(omega_k^2+kappa_(g,N)^+)]^(-1/2)`.

For a conjugation-symmetric axis-aligned rectangular box `C` of positive side
lengths, odd lattice side counts and product real cardinal coordinates, the
block on modes `k/N in C` obeys

```text
T_N/N^4 -> tau_g(C)=int_C b_g(xi) dxi,

L_N/N^4 -> ell_g(C)
 = |C|^(-1) int_(C^3)
     a_g(x)a_g(y)a_g(z)a_g(x+y-z) 1_C(x+y-z)
     dx dy dz.
```

The first limit is a direct Riemann sum. The second is the weighted additive
energy of the block: expand one packet's fourth power, impose
`k_1+k_2=k_3+k_4`, and multiply by the number of cardinal translates. The
bounded positive profile makes `tau_g(C),ell_g(C)` finite and strictly
positive. When `C` is a cube of side `alpha` and the multipliers are constant
`a_g=A,b_g=B`, these formulas reduce to

```text
tau=B alpha^3,
ell=(8/27)A^4 alpha^6,
```

recovering K1677's three-dimensional additive-energy constant.

## K1684: the explicit upper functional

For fixed `C,t`, the K1678 covariance-matched product law has finite-cutoff
gap

```text
(j_R(t)/4)T_N-2g t^2L_N.
```

Translation-Haar averaging preserves covariance and quartic defect and cannot
increase Fisher. K1683 therefore yields

```text
limsup_N (Q_N-lambda_N^statG)/N^4
 <= (j_R(t)/4)tau_g(C)-2g t^2ell_g(C).
```

Taking the infimum gives `h_g^card-up`. For every fixed admissible `C`, the
bracket is `-2g ell_g(C)t^2+O(t^4)`, hence is negative for all sufficiently
small positive `t`. The upper envelope is therefore strictly below
`h_g^prof`.

Haar averaging may lower Fisher further, and allowing general or `N`-dependent shapes,
non-product cumulant tensors or other scalar seeds may lower the upper bound.
The functional is consequently an explicit trial-side envelope, not the true
coefficient.

## K1685: protected integration and next frontier

The bridge census becomes 400 rows: 321 satisfied, ten conditional, 65
excluded and four missing. SC-ACT-01/02/06 remain `ASSERTS`; SC-META-53
remains `UNCERTAIN`; the standing ledger remains 33 SAME / 22 DIFFERS / 31
NEEDS / 2 OVER-DETERMINED; and K1145/K1150 remain 0/7. No source, ledger,
canon, paper, prediction, confirmation or public verdict moves.

The primary next gate is an unrestricted lower bound against the now-explicit
`h_g^card-up`, or a proof that a wider packet/cumulant class lowers it. The
unknown-profile/growing-latent entropy theorem remains a separate class result.
Compactness, Mosco convergence and `E_N+O(1)` recentering still wait for the
true coefficient and shift. The source-owned action/domain/state/observation
tuple remains separate.
