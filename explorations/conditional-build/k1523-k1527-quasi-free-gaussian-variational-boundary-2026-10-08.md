---
title: "K1523--K1527 quasi-free Gaussian variational boundary"
status: active_research
doc_type: conditional-build-result
classification: SOURCE_NATIVE_ROUTE
direction: observed_to_native
target_claim: SC-META-53
created: "2026-10-08"
updated_at: "2026-10-08"
---

# K1523--K1527 quasi-free Gaussian variational boundary

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification is `SOURCE_NATIVE_ROUTE` because the packet tests the positive
Hamiltonian prerequisite bordering SC-META-53. The Gaussian cutoff field,
coherent and quasi-free trial families, nonlinear Hamiltonian and BRST complex
are repository controls, not released GU data.

```gu-typed-objects
result: exact coherent and stationary diagonal quasi-free Rayleigh formulas, ultraviolet shell squeezing cost and a quasi-free N^4 variational boundary
carrier: beta=1 Gaussian reduced Fock space LAYER=toy BRIDGE=positive-state-requirements CHIRALITY=N/A
pairing: Gaussian Q-space pairing ON=repository_owned_control
real_structure: real covariance eigenbasis with pair-degenerate nonzero Fourier covariance factors
grading: spatial frequency, covariance eigenvalue, Gaussian point variance, free energy, Wick-square energy and cutoff filtration
action_owner: repository-construction -- no released source measure, ground-energy counterterm, renormalized Hamiltonian, BRST charge, physical quotient or observed map
target: SC-META-53 interacting-positive-state boundary MAP-TYPE=restriction
```

## Preflight bookend

K1518--K1522 prove the first unrestricted many-chaos lower boundary
`E_N>=c_gN^2` and name an order-`N^2` normalized trial as the cheapest route
toward closing the ground-energy corridor. The immediate candidate is the
Gaussian geometry already native to the fixed Q-space representation. A
coherent shift can move the field toward a minimum of the pointwise square,
and a quasi-free squeeze can reduce fluctuations around it. Both effects have
exact finite-dimensional formulas.

The calculation below tests that entire stationary diagonal quasi-free route
with constant mean,
not only one squeeze parameter. The coherent lens first shows why shifting
without squeezing cannot help. The quasi-free lens then optimizes the mean at
fixed point variance. The ultraviolet-shell lens asks the decisive question:
what does it cost to suppress the point variance by an order-one fraction?
The answer is `Omega(N^4)`, because the top shell carries an order-one fraction
of `C_N` and contains `Theta(N^3)` modes of frequency `Theta(N)`. This kills
the obvious Gaussian `N^2` trial but leaves nonstationary, off-diagonal and
genuinely non-Gaussian routes open.

## K1523 — coherent shifts are exactly vacuum-optimal

Work in the real covariance eigenbasis. Write

```text
phi_N(x)=sum_j sqrt(lambda_j) xi_j e_j(x),
lambda_j=(2 omega_j)^(-1),
C_N=sum_j lambda_j.
```

For a real vector `alpha`, the normalized coherent trial is

```text
psi_alpha(xi)
 =exp[(1/2)sum_j alpha_j xi_j-(1/4)sum_j alpha_j^2].
```

Thus `|psi_alpha|^2 dmu` is the product normal law `N(alpha,I)`. Direct
differentiation in the standard Q-space convention gives

```text
q_0[psi_alpha]=(1/4)sum_j omega_j alpha_j^2.
```

The shifted field has mean

```text
h(x)=sum_j sqrt(lambda_j) alpha_j e_j(x)
```

and still has point variance `C_N`. The pointwise fourth-moment identity yields

```text
E_alpha[(phi_N(x)^2-3C_N)^2]
 =h(x)^4+6C_N^2.
```

On normalized `T^3`, therefore,

```text
q_0[psi_alpha]
 +g int E_alpha[(phi_N^2-3C_N)^2]dx
 =q_0[psi_alpha]+6gC_N^2+g int h^4 dx
 >=6gC_N^2.
```

The vacuum `alpha=0` attains equality. Hence the coherent-sector bottom is
exactly `6gC_N^2=Theta(N^4)`. A large constant displacement toward
`phi^2=3C_N` does not work while the free covariance remains present: the
Gaussian fluctuation terms cancel the tempting quadratic cross term and leave
the vacuum scale plus `int h^4`.

## K1524 — exact stationary diagonal quasi-free formulas

Now let `|psi_(alpha,s)|^2 dmu` be `N(alpha_j,s_j)` in every real coordinate,
with `s_j>0`. Equal sine/cosine factors on each nonzero Fourier pair preserve
translation invariance; take the mean only in the constant zero mode, so the
field mean is the constant `a`. One-coordinate logarithmic differentiation
gives

```text
q_0[psi_(alpha,s)]
 =(1/4)sum_j omega_j[alpha_j^2+(s_j-1)^2/s_j].
```

The centered field has constant point variance

```text
v_N=sum_j lambda_j s_j.
```

The exact Wick-square expectation on normalized `T^3` is

```text
F_C(a,v)
 =a^4+6a^2v+3v^2-6C(a^2+v)+9C^2.
```

At fixed `v`, minimizing over `a^2>=0` gives two branches:

```text
0<=v<=C:
  a^2=3(C-v),
  min_a F_C(a,v)=6v(2C-v);

v>=C:
  a=0,
  min_a F_C(a,v)=3(v-C)^2+6C^2.
```

Thus lowering the `N^4` interaction scale requires `v_N/C_N ->0`; merely
moving the mean is insufficient. The question reduces exactly to the free
cost of suppressing the ultraviolet point variance.

## K1525 — the ultraviolet shell costs `Omega(N^4)`

For the standard three-dimensional torus cutoff, choose the real-mode shell

```text
S_N={j:N/2<=|k_j|_infinity<=N}.
```

It contains `Theta(N^3)` real modes. On it,

```text
omega_j=Theta(N),
lambda_j=Theta(N^-1),
C_(S,N)=sum_(j in S_N)lambda_j>=kappa C_N
```

for some cutoff-independent `kappa>0` and all large `N`. The last fact is the
ordinary three-dimensional lattice-shell comparison: both `C_(S,N)` and
`C_N` are order `N^2`, and the fixed-ratio outer shell carries a positive
fraction of the radial integral.

Suppose first that

```text
v_N<=(kappa/2)C_N.
```

Then `v_(S,N)<=v_N` and the shell deficit satisfies

```text
delta_(S,N)
 =sum_(j in S_N)lambda_j(1-s_j)
 =C_(S,N)-v_(S,N)
 >=(kappa/2)C_N
 =Theta(N^2).
```

Weighted Cauchy gives

```text
delta_(S,N)^2
 <=[sum_(S_N)omega_j(1-s_j)^2/s_j]
   [sum_(S_N)lambda_j^2 s_j/omega_j].
```

On the shell, `lambda_j/omega_j=O(N^-2)`, so

```text
sum_(S_N)lambda_j^2 s_j/omega_j
 <=O(N^-2)sum_(S_N)lambda_j s_j
 =O(N^-2)v_(S,N)
 =O(1).
```

Consequently the squeeze part of `q_0` is `Omega(N^4)`.

If instead `v_N>(kappa/2)C_N`, the optimized K1524 potential is already
`Omega(C_N^2)=Omega(N^4)`: for `v_N<=C_N`, use
`6v_N(2C_N-v_N)>=3kappa C_N^2`; for `v_N>=C_N`, use the lower bound
`6C_N^2`. The two branches therefore cover the entire stationary diagonal
quasi-free class.

## K1526 — the classified quasi-free bottom is `Theta(N^4)`

Let `E_N^qf` be the infimum over the normalized stationary,
translation-invariant diagonal quasi-free trials with constant mean above. For every fixed
`g>0`, K1525 gives

```text
E_N^qf>=c_gN^4.
```

The vacuum belongs to the class and has energy `6gC_N^2=O(N^4)`, hence

```text
E_N^qf=Theta_g(N^4).
```

This is a route decision, not the true ground-energy asymptotic. K1519 still
proves only `E_N>=c_gN^2` on the full nonlinear form domain, and K1516 still
provides the strongest current unrestricted upper descent from the vacuum
scale. The missing order-`N^2` trial cannot be a coherent state or one of the
stationary diagonal quasi-free squeezes classified here. A successful trial
must use structure outside this class—genuinely non-Gaussian correlations,
nonstationary/off-diagonal Gaussian covariance, or another nonlinear
form-domain construction. None is supplied here.

Every subquartic scalar shift leaves all Rayleigh quotients in the classified
quasi-free class divergent to `+infinity`. This is not a spectral or resolvent
statement for `H_N`, because a lower bound on a restricted trial class is not
a lower bound on the full form domain. Tensoring one of these matter trials
with a harmonic BRST vector preserves the same Rayleigh quotient, so the
restriction transfers only as a trial-class statement; it constructs no
continuum interacting BRST charge or physical GU Hilbert space.

## K1527 — admission replay

The bridge census is now 234 rows: 155 satisfied, ten conditional, 65 excluded
and four missing. SC-ACT-01/02/06 remain `ASSERTS`, SC-META-53 remains
`UNCERTAIN`, the physics ledger stays 33 SAME / 22 DIFFERS / 31 NEEDS /
2 OVER-DETERMINED, K1145/K1150 stay `0/7`, and no source, canon, paper,
prediction, confirmation or public status moves.

## Postflight hostile review

The strongest overclaim would promote the quasi-free `Theta(N^4)` result to
the unrestricted ground energy. That is invalid: the class fixes stationary
translation-invariant diagonal covariance and a constant mean. Nonstationary,
off-diagonal and non-Gaussian states remain outside it, and K1519's unrestricted
lower boundary remains only `Omega(N^2)`.

The most delicate normalization seam is the real-mode shell. Sine and cosine
coordinates are counted once as real covariance eigenvectors; equal factors on
each pair ensure stationarity. The shell proof uses only fixed-ratio lattice
counting, `omega=Theta(N)`, `lambda=Theta(N^-1)`, positive `s_j`, and the exact
Q-space free form. Complex-mode double counting is neither needed nor allowed.

The strongest contrary route is a genuinely nonlinear likelihood depending on
the full field, or a nonstationary/off-diagonal Gaussian covariance whose local
variance profile evades the stationary shell dichotomy. The present theorem
does not say those routes work; it says the coherent and stationary diagonal
quasi-free shortcuts do not. The fixed Gaussian representation remains
load-bearing, and a singular dressing or changed measure can alter the
question.

## Exact next input

Construct or exclude a genuinely non-Gaussian normalized trial with energy
comparable to `N^2`, or extend the shell argument to a materially broader
Gaussian/nonlinear class without assuming stationarity and diagonal covariance.
Only after identifying `E_N` to bounded error should compactness and Mosco
liminf/recovery be tested on one common nonlinear domain. Independently,
K1413 still requires a genuinely gauge/Maxwell-dependent spacetime,
secondary-null or derivative/nonlocal estimate, and source admission still
requires one action-owned primitive circle, kinetic normalization, physical
carrier and faithful observed intertwiner.
