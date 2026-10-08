---
title: "K1518--K1522 quadratic-mass localization lower bound"
status: active_research
doc_type: conditional-build-result
classification: SOURCE_NATIVE_ROUTE
direction: observed_to_native
target_claim: SC-META-53
created: "2026-10-08"
updated_at: "2026-10-08"
---

# K1518--K1522 quadratic-mass localization lower bound

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
quadratic-mass Chernoff estimate, entropy localization, nonlinear Hamiltonians
and BRST complex are repository controls, not released GU data.

```gu-typed-objects
result: exponential low-Wick-square probability bound, quadratic many-chaos kinetic-localization boundary, quantitative resolvent collapse and two-sided scalar-recentering corridor
carrier: beta=1 Gaussian reduced Fock space LAYER=toy BRIDGE=positive-state-requirements CHIRALITY=N/A
pairing: Gaussian Q-space pairing ON=repository_owned_control
real_structure: real covariance eigenbasis and coordinatewise complex conjugation
grading: spatial frequency, covariance eigenvalue, Gaussian quadratic mass, relative entropy, free energy, Wick-square energy and cutoff filtration
action_owner: repository-construction -- no released source measure, ground-energy counterterm, renormalized Hamiltonian, BRST charge, physical quotient or observed map
target: SC-META-53 interacting-positive-state boundary MAP-TYPE=restriction
```

## Preflight bookend

K1513--K1517 improve the variational upper side but explicitly leave a
many-chaos lower boundary open. K1474 already gives the needed form-domain
architecture: localizing a normalized state in a rare low-Wick-square event
costs relative entropy, and Gross log-Sobolev converts entropy into free
energy. Its probability input is only Chebyshev, `O(N^-3)`, so the resulting
energy lower bound is merely logarithmic.

The cheapest structural discriminator is Jensen's inequality. A low value of
the integrated square `W_N` forces the Gaussian quadratic mass
`Q_N=int phi_N^2` a fixed fraction above its mean. Unlike the fourth chaos,
`Q_N` diagonalizes exactly as a weighted chi-square sum. Its product moment
generating function gives an exponential tail without a moderate-deviation or
density theorem. The functional-inequality lens composes that event with
K1474; the spectral lens extracts a resolvent rate; the variational lens keeps
the lower boundary distinct from K1516's upper trial. The hostile lens checks
real-mode multiplicities and refuses to call the surviving corridor an
asymptotic.

## K1518 — exponential exclusion of the low Wick-square event

On normalized `T^3`, put

```text
Q_N=int phi_N(x)^2 dx,
W_N=int (phi_N(x)^2-3C_N)^2 dx,
A_N={W_N<=3C_N^2}.
```

Jensen gives

```text
W_N >= (Q_N-3C_N)^2.
```

Hence on `A_N`,

```text
Q_N >= (3-sqrt(3))C_N,
Q_N-C_N >= (2-sqrt(3))C_N.
```

Pass to a real covariance eigenbasis; this avoids double counting conjugate
complex Fourier modes. With independent real standard Gaussians `xi_j`,

```text
Q_N=sum_j lambda_(N,j) xi_j^2,
sum_j lambda_(N,j)=C_N=Theta(N^2),
B_N=sum_j lambda_(N,j)^2=O(N),
lambda_*(N)=max_j lambda_(N,j)=O(1).
```

For `0<t<(2lambda_*)^-1`, the centered moment generating function is exact:

```text
log E exp(t(Q_N-C_N))
 =sum_j[-t lambda_j-(1/2)log(1-2t lambda_j)].
```

For `t<=(4lambda_*)^-1`, the summand is at most `2t^2 lambda_j^2`.
Chernoff optimization therefore gives the weighted-chi-square Bernstein bound

```text
P(Q_N-C_N>=u)
 <=exp[-c min(u^2/B_N,u/lambda_*)].
```

At `u=(2-sqrt(3))C_N`, the two scales are `Omega(N^3)` and
`Omega(N^2)`. The larger covariance eigenvalues set the proved exponent, so

```text
mu(A_N) <= exp(-cN^2).
```

This is an upper small-ball bound, not a matching large-deviation asymptotic.

## K1519 — an `Omega(N^2)` many-chaos lower boundary

Let `psi` be any normalized vector in the nonlinear form domain,
`f=|psi|^2`, and `m_N=int_A_N f dmu`. Binary data processing gives

```text
Ent_mu(f) >= m_N log(1/mu(A_N))-log 2.
```

The cutoff-uniform Gross inequality from K1474 gives

```text
Ent_mu(|psi|^2) <= c_LS q_0[psi].
```

Thus either

```text
q_0[psi] >= log(1/mu(A_N))/(4c_LS)=Omega(N^2),
```

or `m_N<=1/2`, in which case

```text
int W_N |psi|^2 dmu >= (3/2)C_N^2=Theta(N^4).
```

For every fixed `g>0`, the finite-cutoff Hamiltonian therefore satisfies

```text
E_N=inf spec(H_N)
   >=c_g N^2
```

for some `c_g>0` and all sufficiently large `N`. Unlike the polynomial
Krylov and exponential-tilt upper trials, this lower estimate applies to every
normalized form-domain state and hence is genuinely many-chaos. It remains
nonsharp and supplies no ground-state profile.

## K1520 — quantitative resolvent collapse and low-shift exclusion

For every fixed `lambda>0`, positivity and the spectral theorem give

```text
||(H_N+lambda)^(-1)||=(E_N+lambda)^(-1)=O(N^-2).
```

More generally, if

```text
a_N <= c_g N^2-r_N,       r_N -> infinity,
```

then the bottom of `H_N-a_N` is at least `r_N` and its resolvent converges to
zero in norm. In particular every `a_N=o(N^2)` remains too small: it cannot
produce a finite nontrivial self-adjoint strong-resolvent limit. The bound is
one-sided; no matching `N^-2` resolvent asymptotic follows.

## K1521 — a two-sided but nonmatching recentering corridor

Combining K1519 with K1516 gives

```text
c_g N^2
 <= E_N
 <= 6gC_N^2-(1-o(1))g sigma_N R_N,

R_N=N^(1/14)/(1+log N).
```

The two ends use different mechanisms. Shifts below the lower boundary drive
the spectrum to `+infinity`. Shifts whose descent below `6gC_N^2` is smaller
than the K1516 correction drive the spectrum to `-infinity` along normalized
tilt trials. A nontrivial uniformly semibounded continuum candidate can only
be sought inside the large remaining corridor. This does not identify
`E_N+O(1)`, match exponents, prove compactness or supply Mosco recovery.

For

```text
mathbb H_N=H_N tensor 1+1 tensor Delta_BRST,
```

K1471 gives `inf spec(mathbb H_N)=E_N`, and harmonic compression is the
matter resolvent tensored with `P_harm`. The low-side collapse and high-side
instability transfer exactly at finite cutoff. No continuum interacting BRST
operator or GU physical Hilbert space is thereby constructed.

## K1522 — admission replay

The bridge census is now 228 rows: 149 satisfied, ten conditional, 65 excluded
and four missing. SC-ACT-01/02/06 remain `ASSERTS`, SC-META-53 remains
`UNCERTAIN`, the physics ledger stays 33 SAME / 22 DIFFERS / 31 NEEDS /
2 OVER-DETERMINED, K1145/K1150 stay `0/7`, and no source, canon, paper,
prediction, confirmation or public status moves.

## Postflight hostile review

The strongest overclaim would call the quadratic lower boundary a true
ground-energy scale. It is not: the current upper bound remains near the
`N^4` Wick-square vacuum scale and no order-`N^2` trial has been constructed.
The large corridor is a localization theorem plus a variational theorem, not
an asymptotic.

The most delicate internal seam is the quadratic coordinate normalization.
The proof diagonalizes the finite real covariance operator, so the variables
are independent and every complex Fourier conjugacy is already encoded in the
real eigenvalue multiplicities. Only the orders `sum lambda_j=Theta(N^2)`,
`sum lambda_j^2=O(N)` and `max lambda_j=O(1)` enter. Jensen has the correct
direction: low `W_N` implies large `Q_N`; it does not assert the converse.

The strongest contrary route is now an order-`N^2` upper construction or a
stronger low-event geometry that raises the lower scale. The fixed Gaussian
representation remains load-bearing; a singular dressing or changed measure
can alter the problem. Within these ceilings, the result replaces the
logarithmic lower boundary by a quadratic one and quantitatively narrows the
class of scalar recentring candidates.

## Exact next input

Construct a normalized trial with energy comparable to `N^2`, or strengthen
the low-Wick-square small-ball geometry beyond the quadratic-mass consequence,
to begin closing the surviving ground-energy corridor. Only after identifying
`E_N` to bounded error should compactness and Mosco liminf/recovery be tested
on one common nonlinear domain. Independently, K1413 still requires a
genuinely gauge/Maxwell-dependent spacetime, secondary-null or
derivative/nonlocal estimate, and source admission still requires one
action-owned primitive circle, kinetic normalization, physical carrier and
faithful observed intertwiner.
