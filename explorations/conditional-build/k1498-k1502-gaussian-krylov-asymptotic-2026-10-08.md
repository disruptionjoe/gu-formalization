---
title: "K1498--K1502 Gaussian Krylov asymptotic"
status: active_research
doc_type: conditional-build-result
classification: SOURCE_NATIVE_ROUTE
direction: observed_to_native
target_claim: SC-META-53
created: "2026-10-08"
updated_at: "2026-10-08"
---

# K1498--K1502 Gaussian Krylov asymptotic

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
contraction graphs, Hermite tower and nonlinear Hamiltonians are repository
controls, not released GU data.

```gu-typed-objects
result: ultraviolet Gaussian limit of the normalized quartic Wick coordinate, limiting Hermite Jacobi tower, unbounded fixed-degree variational coefficients and super-sigma scalar-recentering necessity
carrier: beta=1 Gaussian reduced Fock space LAYER=toy BRIDGE=positive-state-requirements CHIRALITY=N/A
pairing: Gaussian Q-space pairing ON=repository_owned_control
real_structure: Gaussian real field and coordinatewise complex conjugation
grading: spatial frequency, Wiener chaos, contraction order, polynomial Krylov degree, particle number and cutoff filtration
action_owner: repository-construction -- no released source measure, ground-energy counterterm, renormalized Hamiltonian, BRST charge, physical quotient or observed map
target: SC-META-53 interacting-positive-state boundary MAP-TYPE=restriction
```

## Preflight bookend

K1493--K1497 prove strict improvement at every fixed polynomial degree but do
not control the improvement as the degree grows. The cheapest discriminator is
not another trial polynomial. It is the fourth-chaos contraction criterion:
if every nontrivial contraction of the normalized kernel vanishes, then the
entire fixed-moment problem converges to the Gaussian one and the limiting
orthogonal polynomials are Hermite polynomials.

The graph lens therefore counts the three contraction topologies before any
moment enumeration. The probability lens applies the fixed-chaos fourth-
moment theorem and uniform integrability. The spectral lens passes fixed Hankel
moment matrices to their Jacobi coefficients. The variational lens uses only a
fixed Hermite degree at a time. The hostile lens forbids selecting a degree
depending on the cutoff or converting one-sided Ritz bounds into a ground-
energy asymptotic.

## K1498 — every nontrivial fourth-chaos contraction vanishes

On normalized `T3`, use

```text
q_N(k)=1_(|k|<=N)/(2 sqrt(m^2+|k|^2)),
V_N=I_4(f_N),
sigma_N^2=4! ||f_N||^2=Theta(N^5),
X_N=V_N/sigma_N.
```

For `r=1,2,3`, the squared contraction norm
`||f_N tensor_r f_N||^2` is the lattice vacuum sum of a connected multigraph
`G_r` on four quartic vertices. Its nonzero edge multiplicities are

```text
m_AB=m_CD=r,             m_AC=m_BD=4-r.
```

Thus every `G_r` has eight covariance edges and cycle rank

```text
L=E-V+1=8-4+1=5.
```

The beta-one covariance contributes one inverse momentum power per edge.
Dyadically order the five independent loop momenta. In every Hepp sector,
successively contracting the highest-scale connected block gives the factor

```text
2^(3L_S-E_S)j
```

for that block. The only two-vertex multiplicities are `1,2,3`, with degrees
`-1,1,3`; every connected three-vertex block has at most four edges and degree
at most two; the full graph has degree seven. Contracting a divergent proper
block and then its quotient preserves the total degree seven. Marginal simple
cycles contribute at most a fixed logarithmic power. Consequently there are
constants `A_r,p_r`, independent of the cutoff, such that

```text
||f_N tensor_r f_N||^2
   <=A_r N^7(1+log N)^p_r,
p_r<=8.
```

Because `||f_N||^4=Theta(N^10)`, all normalized contractions obey

```text
||f_N tensor_r f_N||^2/||f_N||^4
 =O(N^-3(1+log N)^8) -> 0,
r=1,2,3.
```

This is a fixed-chaos ultraviolet statement. It does not estimate polynomial
degree dependence.

## K1499 — Gaussian distribution and every fixed moment

The fourth-moment theorem for a fixed Wiener chaos says that a unit-variance
sequence `I_4(f_N)/sigma_N` converges to a standard normal variable exactly
when all nontrivial contractions vanish. K1498 therefore gives

```text
X_N => Z,                  Z~N(0,1),
E(X_N^4) -> 3.
```

For every fixed `p>=2`, Nelson hypercontractivity gives the cutoff-independent
bound

```text
||X_N||_p <= (p-1)^2.
```

The family `|X_N|^j` is uniformly integrable for each fixed `j`. Distributional
convergence hence upgrades to all fixed moments:

```text
E(X_N^j) -> E(Z^j),        j fixed.
```

In particular the K1483 normalized third moment tends to zero. The result is
not a total-variation estimate, a growing-moment theorem or a uniform statement
for `j=j(N)`.

## K1500 — the fixed Jacobi tower converges to Hermite

Fix `d`. The Gram matrix of `1,x,...,x^d` depends only on moments through
order `2d`. K1499 makes it converge to the positive-definite Gaussian Hankel
matrix. Cholesky/Gram--Schmidt coefficients are continuous on the positive-
definite cone, so the orthonormal polynomials and the multiplication
compression satisfy

```text
J_(d,N) -> J_d^G.
```

For the normalized probabilists' Hermite basis,

```text
x phi_j^G=sqrt(j+1) phi_(j+1)^G+sqrt(j) phi_(j-1)^G.
```

Thus `J_d^G` has zero diagonal and off-diagonal entries
`1,sqrt(2),...,sqrt(d)`. Put

```text
c_d^G=-lambda_min(J_d^G).
```

The final two-coordinate principal compression is

```text
[ 0       sqrt(d) ]
[ sqrt(d) 0       ],
```

so Rayleigh--Ritz gives

```text
c_d^G>=sqrt(d),
lambda_min(J_(d,N)) -> -c_d^G.
```

The fixed-degree coefficients are therefore unbounded. This statement takes
`N` to infinity before increasing `d`; it neither supplies a simultaneous
rate nor contradicts K1496's different fixed-cutoff tower limit.

## K1501 — super-`sigma_N` variational descent

Let `A>0`. Choose one fixed degree `d` with `sqrt(d)>A+2`. By K1500, for all
large cutoffs the normalized polynomial Ritz vector has multiplication
Rayleigh quotient below `-(A+1)`. It lies in Wiener degree at most `4d`, so
its free form cost is at most

```text
4d omega_max(N)=O_d(N)=o(sigma_N).
```

For every fixed `g>0`, eventually

```text
E_N<=6gC_N^2-A g sigma_N.
```

Since `A` was arbitrary,

```text
(6gC_N^2-E_N)/(g sigma_N) -> +infinity.
```

This is an unbounded one-sided correction, not a rate. The proof selects a
fixed degree after `A` and only then lets `N` grow; it does not construct
`d(N)`.

There is an immediate scalar-recentering boundary. If `H_N-a_N` is uniformly
bounded below, then necessarily

```text
(6gC_N^2-a_N)/(g sigma_N) -> +infinity.
```

Indeed, failure supplies a subsequence on which that ratio is bounded by some
`K`; choose fixed `A>K+1` above and the corresponding normalized Ritz values
tend to minus infinity. Hence every shift with

```text
6gC_N^2-a_N=O(sigma_N)
```

fails uniform semiboundedness. The normalized fixed-degree trials have weakly
convergent subsequences in the fixed Gaussian Hilbert space, while their form
values tend to minus infinity, so no finite semibounded limiting form can
satisfy Mosco weak liminf for such a shift. Tensoring with K1471's normalized
degree-zero harmonic BRST vacuum transfers the same boundary to the full forms
and harmonic compression.

The true-ground-energy shift `a_N=E_N+O(1)` is not excluded. No matching lower
bound, ground-state localization, compactness, Mosco recovery or interacting
continuum BRST operator has been constructed.

## K1502 — admission replay

The bridge census is now 196 rows: 123 satisfied, ten conditional, 59 excluded
and four missing. SC-ACT-01/02/06 remain `ASSERTS`, SC-META-53 remains
`UNCERTAIN`, the physics ledger stays 33 SAME / 22 DIFFERS / 31 NEEDS /
2 OVER-DETERMINED, K1145/K1150 stay `0/7`, and no source, canon, paper,
prediction, confirmation or public status moves.

## Postflight hostile review

The strongest overclaim would read the limit above as a quantitative
ground-energy asymptotic. It is not. For each requested coefficient the proof
chooses a different but fixed polynomial degree; neither the contraction
constants nor the moment matrices are controlled uniformly as that degree
grows. A cutoff-dependent choice could make the free-energy cost comparable to
the gain and requires new estimates.

The strongest contrary route is still a many-chaos coercive/localization lower
bound for the actual Hamiltonian. Such a theorem could identify the true scale
without following the polynomial tower. The weakest transfer seam remains the
fixed Gaussian representation: singular dressing or a changed measure may
alter the compactness problem. Within those ceilings, the result decides the
question left by K1497: the fixed-degree coefficients are unbounded, and no
scalar recentering only `O(sigma_N)` below the Wick square's vacuum level can
support a uniformly semibounded fixed-Gaussian continuum route.

## Exact next input

For the quantum arc, prove a quantitative growing-degree contraction/moment
bound together with its `H0` cost, or construct a many-chaos coercive and
kinetic-localization lower bound for the actual ground energy. Only then test
compactness plus Mosco liminf/recovery for `a_N=E_N+O(1)`. Independently,
K1413 still requires a genuinely gauge/Maxwell-dependent spacetime,
secondary-null or derivative/nonlocal estimate controlling both leakages, and
source admission still requires the action-owned primitive circle, kinetic
normalization, physical carrier and faithful observed intertwiner.
