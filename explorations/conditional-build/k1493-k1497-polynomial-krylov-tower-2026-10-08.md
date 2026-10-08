---
title: "K1493--K1497 polynomial Wick-Krylov tower"
status: active_research
doc_type: conditional-build-result
classification: SOURCE_NATIVE_ROUTE
direction: observed_to_native
target_claim: SC-META-53
created: "2026-10-08"
updated_at: "2026-10-08"
---

# K1493--K1497 polynomial Wick-Krylov tower

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
polynomial Krylov tower, Jacobi matrices and nonlinear Hamiltonians are
repository controls, not released GU data.

```gu-typed-objects
result: all-fixed-degree top-chaos nondegeneracy, uniformly irreducible Jacobi tower, strict variational and recentering hierarchy, and exact fixed-cutoff multiplication endpoint
carrier: beta=1 Gaussian reduced Fock space LAYER=toy BRIDGE=positive-state-requirements CHIRALITY=N/A
pairing: Gaussian Q-space pairing ON=repository_owned_control
real_structure: Gaussian real field and coordinatewise complex conjugation
grading: spatial frequency, Wiener chaos, polynomial Krylov degree, particle number and cutoff filtration
action_owner: repository-construction -- no released source measure, ground-energy counterterm, renormalized Hamiltonian, BRST charge, physical quotient or observed map
target: SC-META-53 interacting-positive-state boundary MAP-TYPE=restriction
```

## Preflight bookend

K1490 proves a strict gain from one extra polynomial direction, but its fixed
trial does not decide whether the gain is repeatable. The structural question
is whether Gram--Schmidt can ever exhaust the polynomial Krylov tower at a
finite degree. For a fourth-chaos coordinate it cannot: the highest Wiener
chaos in `X_N^j` has degree `4j`, whereas every lower polynomial has degree at
most `4j-4`.

The operator/Wiener-chaos lens therefore selects monic orthogonal polynomials,
not another hand-tuned vector. The probability lens supplies uniform
fixed-degree moment bounds. The spectral lens asks whether strict interlacing
can be made uniform in the cutoff. The variational lens prices the free energy
of a fixed polynomial degree. The moment-problem lens separately asks what the
entire tower reaches when the cutoff is held fixed. The hostile lens forbids
interchanging those two limits. A direct fourth-cumulant or Gaussian-limit
route could prove unbounded coefficient growth, but its contraction estimates
are not yet available and broad moment enumeration is dominated by the exact
top-chaos argument.

## K1493 — no fixed polynomial degree collapses

Write

```text
X_N=I_4(f_N)/sigma_N,                 E(X_N^2)=1.
```

For `j>=0`, let `q_(j,N)` be the monic degree-`j` polynomial orthogonal to
`1,X_N,...,X_N^(j-1)`, and set

```text
h_(j,N)=E[q_(j,N)(X_N)^2].
```

Every lower power has Wiener degree at most `4(j-1)`. Therefore

```text
P_(4j) q_(j,N)(X_N)
 =P_(4j)X_N^j
 =I_(4j)(sym(f_N tensor ... tensor f_N))/sigma_N^j.
```

In the Fourier kernel representation all coefficients of `f_N` are
nonnegative square-root covariance weights subject to momentum conservation.
In the symmetrization norm, the block-preserving permutations alone contribute

```text
(4!)^j ||f_N||^(2j).
```

All remaining coefficient products are nonnegative. Since
`sigma_N^2=4!||f_N||^2`,

```text
||P_(4j)X_N^j||_2^2>=1,
h_(j,N)>=1.
```

Thus no monic residual vanishes. On the other side, the monomial is an
admissible monic competitor and fourth-chaos hypercontractivity gives, for
`j>=1`,

```text
h_(j,N)<=E|X_N|^(2j)
         <=[(2j-1)^2]^(2j)
         =H_j:=(2j-1)^(4j).
```

These are uniform bounds after fixing `j`; they are deliberately not uniform
as `j` tends to infinity.

## K1494 — uniformly irreducible Jacobi compressions

Normalize

```text
phi_(j,N)=q_(j,N)(X_N)/sqrt(h_(j,N)).
```

Multiplication by `X_N` has the three-term recurrence

```text
X_N phi_j=b_(j+1,N)phi_(j+1)+a_(j,N)phi_j+b_(j,N)phi_(j-1),
b_(j+1,N)=sqrt(h_(j+1,N)/h_(j,N)).
```

K1493 implies

```text
H_j^(-1/2)<=b_(j+1,N)<=H_(j+1)^(1/2).
```

Moreover `phi_(j,N)` has Wiener degree at most `4j` and unit `L2` norm. Nelson
hypercontractivity gives

```text
||phi_(j,N)||_4<=3^(2j),
|a_(j,N)|=|E[X_N phi_(j,N)^2]|<=3^(4j).
```

Let `J_(d,N)` be the compression to
`span{phi_(0,N),...,phi_(d,N)}`. It is an irreducible real Jacobi matrix, so
strict Cauchy interlacing gives

```text
lambda_min(J_(d,N))<lambda_min(J_(d-1,N)).
```

For fixed `d`, all relevant diagonal and off-diagonal coefficients lie in a
compact box, and the final off-diagonal is bounded away from zero. The strict
interlacing difference is continuous and positive throughout that compact
set. Hence there is an `epsilon_d>0`, independent of `N`, such that

```text
lambda_min(J_(d,N))
 <=lambda_min(J_(d-1,N))-epsilon_d.
```

This compactness argument proves a gap at every fixed degree. It does not give
a useful all-degree asymptotic for the gaps.

## K1495 — strict fixed-degree variational hierarchy

Define

```text
c_1=1,
c_d=1+sum_(r=2)^d epsilon_r.
```

K1484 gives `lambda_min(J_(1,N))=-1+o(1)`, and K1494 gives, for every fixed
`d`,

```text
lambda_min(J_(d,N))<=-c_d+o(1),
c_d>c_(d-1).
```

The degree-`d` polynomial space lies in Wiener degree at most `4d`. With
cutoff frequency at most `N`, its normalized free form cost is at most

```text
4d omega_max(N)=O_d(N).
```

Consequently, for every fixed `d` and `g>0`,

```text
E_N<=6gC_N^2-c_d g sigma_N+O_d(N).
```

Uniform semiboundedness of `H_N-a_N` therefore requires

```text
a_N<=6gC_N^2-c_d g sigma_N+O_d(N)
```

for every fixed `d`. More explicitly, if `delta>0` and eventually

```text
a_N>=6gC_N^2-g(c_d-delta)sigma_N,
```

then

```text
inf spec(H_N-a_N)<=-g delta sigma_N+O_d(N)->-infinity.
```

This proves that no finite polynomial degree supplies a terminal coefficient.
It does not prove that `sup_d c_d` is infinite, and the present packet does not
construct the weakly convergent trials needed for a new Mosco statement.

## K1496 — the full fixed-cutoff tower and the noncommuting limits

At fixed cutoff,

```text
W_N=V_N+6C_N^2
   =integral (phi_N(x)^2-3C_N)^2 dx>=0.
```

Thus `X_N=V_N/sigma_N` is bounded below by

```text
-L_N,              L_N=6C_N^2/sigma_N.
```

The cutoff field has finitely many Gaussian Fourier coordinates with full
support. The constant configurations
`phi_N(x)=plus-or-minus sqrt(3C_N)` are in that support and make `W_N=0`.
Every neighborhood of either configuration has positive Gaussian measure, so

```text
ess inf X_N=-L_N.
```

Put `Z_N=X_N+L_N=W_N/sigma_N>=0`. Finite-dimensional norm equivalence bounds
`sqrt(Z_N)` by `A_N(1+||G_N||^2)` for the Gaussian coordinate vector `G_N`.
For some cutoff-dependent `c_N>0`,

```text
E exp(c_N sqrt(Z_N))<infinity.
```

Hardy's criterion makes the Stieltjes moment problem determinate. Equivalently,
the Jacobi operator determined by these moments is essentially self-adjoint,
and its spectral measure is the law of `X_N`. The nested finite Jacobi bottoms
therefore satisfy

```text
lambda_min(J_(d,N)) decreases to ess inf X_N
                         =-6C_N^2/sigma_N
```

as `d` tends to infinity with `N` fixed. Since `C_N=Theta(N^2)` and
`sigma_N=Theta(N^(5/2))`, the endpoint magnitude is `Theta(N^(3/2))`.

This does not commute the limits. The Hardy constant, localization degree and
free-energy cost depend on `N`; a degree `d(N)` may cost much more than the
fixed-degree `O_d(N)` estimate. The fixed-cutoff multiplication endpoint is
not a uniform ultraviolet ground-energy asymptotic.

## K1497 — admission replay

The bridge census is now 187 rows: 117 satisfied, ten conditional, 56 excluded
and four missing. SC-ACT-01/02/06 remain `ASSERTS`, SC-META-53 remains
`UNCERTAIN`, the physics ledger stays 33 SAME / 22 DIFFERS / 31 NEEDS /
2 OVER-DETERMINED, K1145/K1150 stay `0/7`, and no source, canon, paper,
prediction, confirmation or public status moves.

## Postflight hostile review

The strongest overclaim would infer `sup_d c_d=infinity` from strict increase.
The compact interlacing gaps may decay summably; a Gaussian moment limit,
recurrence asymptotic or another uniform-in-degree argument is still required.
The strongest contrary route is a many-chaos coercive lower/localization
estimate for the actual Hamiltonian, which could bracket the ground energy
without following polynomial multiplication compressions.

The weakest transfer seam is the order of limits. K1496 is exact only after
fixing `N`; its polynomial degree, Hardy constant and kinetic cost are not
uniform. The result nevertheless closes a real ambiguity: K1490 is not an
isolated accident, no finite fixed degree is variationally terminal, and the
full finite-cutoff multiplication tower is understood exactly.

## Exact next input

For the quantum arc, prove either that the fixed-degree coefficients `c_d` are
unbounded—most directly through a fixed-order moment/recurrence limit with
controlled contractions—or a many-chaos coercive/localization lower bound that
brackets `E_N`. Only then choose a degree depending on the cutoff or test
compactness and Mosco liminf/recovery for `a_N=E_N+O(1)`. Independently, K1413
still requires a genuinely gauge/Maxwell-dependent spacetime, secondary-null
or derivative/nonlocal estimate controlling both leakages.
