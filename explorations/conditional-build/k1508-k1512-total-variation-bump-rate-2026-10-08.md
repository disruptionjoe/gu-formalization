---
title: "K1508--K1512 total-variation bump rate"
status: active_research
doc_type: conditional-build-result
classification: SOURCE_NATIVE_ROUTE
direction: observed_to_native
target_claim: SC-META-53
created: "2026-10-08"
updated_at: "2026-10-08"
---

# K1508--K1512 total-variation bump rate

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
Malliavin--Stein estimate, bump trials and nonlinear Hamiltonians are
repository controls, not released GU data.

```gu-typed-objects
result: quantitative fourth-chaos total-variation rate, rare negative bump transfer, square-root-logarithmic Wick variational rate and strengthened scalar-recentering obstruction
carrier: beta=1 Gaussian reduced Fock space LAYER=toy BRIDGE=positive-state-requirements CHIRALITY=N/A
pairing: Gaussian Q-space pairing ON=repository_owned_control
real_structure: Gaussian real field and coordinatewise complex conjugation
grading: spatial frequency, Wiener chaos, Malliavin derivative, rare-event exponent, particle number and cutoff filtration
action_owner: repository-construction -- no released source measure, ground-energy counterterm, renormalized Hamiltonian, BRST charge, physical quotient or observed map
target: SC-META-53 interacting-positive-state boundary MAP-TYPE=restriction
```

## Preflight bookend

K1503--K1507 transfer slowly growing polynomials but pay an
`exp(Cm log m)` coefficient and diagram cost. K1498 contains a stronger
distributional input: all three nontrivial contractions of the normalized
fourth chaos decay at a quantitative polynomial rate. The fixed-chaos
Malliavin--Stein inequality converts those same contractions directly into
total variation, which transfers every bounded measurable test.

The probability lens therefore replaces a growing Hermite polynomial by one
fixed-width smooth bump in the negative Gaussian tail. The form lens uses the
Malliavin chain rule to price the bump's free energy without expanding it into
infinitely many chaoses. The asymptotic lens chooses a rarity exponent below
the contraction threshold `3/2`. The hostile lens keeps the conclusion
one-sided: a localized trial is not a many-chaos lower bound or a ground-state
compactness theorem. K1413 and the source-owned selector tuple remain
independent routes with inputs not produced here.

## K1508 — the contraction estimate gives total variation

Write

```text
X_N=I_4(g_N),                    E(X_N^2)=1.
```

For a normalized variable in the fourth Wiener chaos, the fourth cumulant is
a positive universal linear combination of the three squared nontrivial
contraction norms. The fixed-chaos Malliavin--Stein theorem gives

```text
d_TV(X_N,Z)
 <= C sqrt(E(X_N^4)-3)
 <= C' (sum_(r=1)^3 ||g_N tensor_r g_N||^2)^(1/2),
                                         Z~N(0,1).
```

K1498 bounds each squared normalized contraction by
`O(N^-3(1+log N)^8)`. Hence

```text
epsilon_N:=d_TV(X_N,Z)=O(N^-3/2(1+log N)^4).
```

This rate controls bounded measurable tests. It does not by itself control an
unbounded exponential, polynomial with growing supremum, or derivative-weighted
observable.

## K1509 — a negative bump reaches `sqrt(log N)`

Fix once and for all `b in C_c^1(R)` with

```text
0<=b<=1,       supp(b) subset [-1,0],
b=1 on [-3/4,-1/4].
```

For any fixed `0<alpha<3/2`, set

```text
R_N=sqrt(2 alpha log N),         b_N(x)=b(x+R_N).
```

The Gaussian mass obeys

```text
p_N=E[b_N(Z)^2]
   >=c exp(-(R_N+1)^2/2)
   =N^(-alpha-o(1)).
```

Therefore

```text
epsilon_N/p_N
 =N^(alpha-3/2+o(1))(1+log N)^4 ->0.
```

Total variation transfers the norm. Since the bump is supported where
`x<=-R_N`, it also transfers the bounded numerator:

```text
E[b_N(X_N)^2]                 =p_N(1+o(1)),
E[X_N b_N(X_N)^2]            <=-R_N p_N+O(R_N epsilon_N),
E[X_N b_N(X_N)^2]/E[b_N(X_N)^2]
                              <=-(1-o(1))sqrt(2 alpha log N).
```

The strict inequality `alpha<3/2` is load-bearing. At the endpoint, K1508's
present bound no longer proves that the transferred mass dominates the error.

## K1510 — the free cost is lower order

The Malliavin chain rule gives

```text
D b_N(X_N)=b_N'(X_N)D X_N,       E||D X_N||^2=4.
```

For `H0=dGamma(omega)` and cutoff frequency ceiling
`omega_max(N)=O(N)`, the unnormalized free form satisfies

```text
q0[b_N(X_N)]
 <=omega_max(N)||b'||_infinity^2 E||D X_N||^2
 =O(N).
```

After normalization by the cutoff bump mass,

```text
q0[b_N(X_N)]/E[b_N(X_N)^2] <=N^(1+alpha+o(1)).
```

Meanwhile `sigma_N=Theta(N^(5/2))`, so

```text
N^(1+alpha+o(1))/(sigma_N R_N)
 =N^(alpha-3/2+o(1))/sqrt(log N) ->0.
```

For every fixed `g>0` and `alpha<3/2`, the normalized trial therefore gives

```text
E_N
 <=6gC_N^2
   -(sqrt(2 alpha)-o(1))g sigma_N sqrt(log N).
```

Equivalently, for every `c<sqrt(3)`,

```text
E_N<=6gC_N^2-cg sigma_N sqrt(log N)
```

eventually, and

```text
liminf_N (6gC_N^2-E_N)/(g sigma_N sqrt(log N))>=sqrt(3).
```

The number `sqrt(3)` is the boundary obtained from K1498's current
total-variation exponent. It is not claimed to be the true energy coefficient
or an optimal localization constant.

## K1511 — recentering and harmonic-BRST boundary

If `H_N-a_N` is uniformly bounded below, then `a_N<=E_N+O(1)`. K1510 forces

```text
liminf_N (6gC_N^2-a_N)/(g sigma_N sqrt(log N))>=sqrt(3).
```

Every scalar family with limsup strictly below `sqrt(3)` has spectral bottoms
tending to minus infinity. The normalized bump trials lie in the unit ball of
the fixed Gaussian Hilbert space, so each sequence has a weakly convergent
subsequence. Its weak limit may be zero; Mosco weak liminf still applies.
Along the excluded recentering window the form values tend to minus infinity,
contradicting every finite semibounded candidate form.

Tensoring the trials with K1471's normalized degree-zero harmonic BRST vacuum
preserves their form values and weak convergence. The same exclusion therefore
holds for the full matter--BRST forms and harmonic compression. No
ground-energy-recentered limit, recovery sequence, compactness, continuum
interacting BRST charge or changed-representation conclusion follows.

## K1512 — admission replay

The bridge census is now 212 rows: 135 satisfied, ten conditional, 63 excluded
and four missing. SC-ACT-01/02/06 remain `ASSERTS`, SC-META-53 remains
`UNCERTAIN`, the physics ledger stays 33 SAME / 22 DIFFERS / 31 NEEDS /
2 OVER-DETERMINED, K1145/K1150 stay `0/7`, and no source, canon, paper,
prediction, confirmation or public status moves.

## Postflight hostile review

The strongest overclaim would identify `sqrt(3)` with the true ground-energy
coefficient. The argument supplies only an upper trial, and `sqrt(3)` comes
from the present contraction exponent rather than a matching lower bound. The
strongest contrary route is a many-chaos coercive or small-ball localization
lower estimate; it could put the true correction on a larger scale. The
weakest analytic seam is the weighted Malliavin form comparison, which uses
only the cutoff frequency ceiling and therefore gives a deliberately crude
normalized kinetic bound.

The transfer itself is restricted to bounded compactly supported observables.
The numerator is safe only because `x b_N(x)^2` has supremum `O(R_N)`. No
unbounded tail observable is smuggled through total variation. The fixed
Gaussian representation remains load-bearing; a singular dressing or changed
measure can alter the compactness and recentering problem.

## Exact next input

For the quantum arc, prove a many-chaos kinetic-localization lower boundary or
a matching small-ball/coercive estimate for the true `E_N`; only then test
ground-energy recentering, compactness and Mosco recovery on one common
nonlinear domain. Independently, advance K1413 through a genuinely
gauge/Maxwell-dependent spacetime, secondary-null or derivative/nonlocal
estimate controlling both leakages. Source admission still requires one
action-owned primitive circle, kinetic normalization, physical carrier and
faithful observed intertwiner.
