---
title: "K1503--K1507 quantitative growing Krylov rate"
status: active_research
doc_type: conditional-build-result
classification: SOURCE_NATIVE_ROUTE
direction: observed_to_native
target_claim: SC-META-53
created: "2026-10-08"
updated_at: "2026-10-08"
---

# K1503--K1507 quantitative growing Krylov rate

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
diagram bounds, Hermite trials and nonlinear Hamiltonians are repository
controls, not released GU data.

```gu-typed-objects
result: logarithmic-over-logarithmic Gaussian moment window, growing Hermite trial, explicit divergent Wick-Krylov variational rate and strengthened scalar-recentering obstruction
carrier: beta=1 Gaussian reduced Fock space LAYER=toy BRIDGE=positive-state-requirements CHIRALITY=N/A
pairing: Gaussian Q-space pairing ON=repository_owned_control
real_structure: Gaussian real field and coordinatewise complex conjugation
grading: spatial frequency, Wiener chaos, complete-pairing diagram, Hermite degree, particle number and cutoff filtration
action_owner: repository-construction -- no released source measure, ground-energy counterterm, renormalized Hamiltonian, BRST charge, physical quotient or observed map
target: SC-META-53 interacting-positive-state boundary MAP-TYPE=restriction
```

## Preflight bookend

K1498--K1502 prove Gaussian convergence at every fixed moment and an
unbounded fixed-degree Ritz coefficient, but give no simultaneous degree and
cutoff rate. The cheapest next discriminator is to retain the combinatorial
cost in the same complete-pairing expansion. A non-Gaussian diagram must
contain a nontrivial fourth-chaos contraction; the number of complete pairings
grows only exponentially in `m log m`. K1498's polynomial contraction decay
therefore beats that cost for `m` of sufficiently small order
`log N/log log N`.

The graph/probability lens counts all diagrams rather than invoking weak
convergence for an unbounded polynomial. The approximation lens works in the
normalized Hermite basis and uses one explicit two-coordinate trial, avoiding
uniform inversion of a growing monomial Hankel matrix. The variational lens
prices the exact chaos ceiling against `H0`. The hostile lens keeps the rate
one-sided and nonoptimal. A many-chaos coercive/localization lower bound remains
the strongest contrary route; the full-PDE and source-selector arcs require
independent inputs not produced here.

## K1503 — a growing Gaussian moment window

Normalize the fourth-chaos kernel by writing

```text
X_N=I_4(g_N),                 E(X_N^2)=1,
delta_N=max_(1<=r<=3)||g_N tensor_r g_N||.
```

K1498 gives

```text
delta_N=O(N^(-3/2)(1+log N)^4).
```

Expand `E(X_N^m)` into complete pairings of the `4m` kernel legs. The Gaussian
moment is exactly the subfamily whose connected components pair two whole
quartic vertices by four edges. Every other diagram contains a first cut with
between one and three legs joining two partially contracted blocks. Repeated
Cauchy--Schwarz at that cut bounds its normalized amplitude by `delta_N`.

The total number of pairings is

```text
(4m-1)!! <= (4m)^(2m).
```

The product-formula multiplicities and the choices of the marked cut are also
bounded by `exp(C m log(m+1))` for one universal `C`. Enlarging `C` once gives

```text
|E(X_N^m)-E(Z^m)|
 <= delta_N exp(C m log(m+1)),       Z~N(0,1).
```

Choose a universal `eta>0` sufficiently small and put

```text
M_N=floor(eta log N/log log N).
```

Since `M_N log(M_N+1)<=eta(1+o(1))log N`, `eta` can be chosen so that the
combinatorial exponent is strictly smaller than `3/2`. Therefore

```text
max_(0<=m<=M_N)|E(X_N^m)-E(Z^m)| -> 0.
```

The value of `eta` is not optimized. The conclusion is an existence theorem
for a nonempty growing window, not a sharp moderate-deviation or total-
variation estimate.

## K1504 — one growing Hermite trial transfers

Let `phi_j=He_j/sqrt(j!)` be the normalized probabilists' Hermite polynomial.
Its monomial coefficient `l1` norm is bounded by

```text
||phi_j||_(coeff,1)<=exp(C_H j log(j+1)).
```

After shrinking `eta` once to absorb this coefficient cost, choose

```text
d_N=floor(M_N/3),
p_N=(phi_(d_N-1)-phi_(d_N))/sqrt(2).
```

The norm of `p_N` uses moments through `2d_N`; its multiplication quotient
uses moments through `2d_N+1`, both inside the K1503 window. Expanding the two
polynomials in monomials and applying K1503 term by term gives

```text
E[p_N(X_N)^2]=1+o(1),
E[X_N p_N(X_N)^2]=-sqrt(d_N)+o(1).
```

The second identity is exact in the Gaussian law because multiplication by
`x` couples `phi_(d-1)` and `phi_d` with coefficient `sqrt(d)`. Hence the
normalized cutoff trial has multiplication Rayleigh quotient at most
`-sqrt(d_N)/2` eventually.

This transfers one explicit trial. It does not prove operator-norm convergence
of a growing Jacobi matrix, uniform orthogonal-polynomial asymptotics or the
largest admissible degree window.

## K1505 — an explicit divergent variational rate

The polynomial `p_N(X_N)` lies in Wiener chaos at most `4d_N`. With
`omega_max(N)=O(N)`, its normalized free-form cost obeys

```text
<p_N,H0 p_N>/||p_N||^2 <=4d_N omega_max(N)=O(Nd_N).
```

K1482's normalization of the finite-cutoff Hamiltonian gives the competing
interaction gain

```text
-(g sigma_N/2)sqrt(d_N),       sigma_N=Theta(N^(5/2)).
```

Because

```text
Nd_N/(sigma_N sqrt(d_N))
 =O(sqrt(d_N)/N^(3/2)) -> 0,
```

there is a universal `c>0` such that, for every fixed `g>0`,

```text
E_N
 <=6gC_N^2
   -c g sigma_N sqrt(log N/log log N)
```

for all sufficiently large `N`. Equivalently,

```text
(6gC_N^2-E_N)/(g sigma_N)
 >=c sqrt(log N/log log N).
```

This is the first quantitative simultaneous cutoff-degree rate in the current
Krylov route. It is not asserted sharp and remains only a variational upper
bound on `E_N`.

## K1506 — strengthened recentering and BRST boundary

If `H_N-a_N` is uniformly bounded below, then `a_N<=E_N+O(1)`. K1505 therefore
forces

```text
6gC_N^2-a_N
 >=c g sigma_N sqrt(log N/log log N)+O(1)
```

after possibly decreasing `c`. In particular every scalar shift with

```text
6gC_N^2-a_N
 =o(g sigma_N sqrt(log N/log log N))
```

fails uniform semiboundedness.

The normalized trial has no fixed vacuum coefficient at growing degree, so the
K1501 vacuum-component shortcut is unavailable. Instead use the unit ball's
weak compactness: every normalized trial sequence has a weakly convergent
subsequence. If a finite semibounded limiting form had Mosco weak liminf, the
recentered values along that subsequence could not tend to minus infinity.
They do throughout every window bounded above by `(c-epsilon)g sigma_N` times
the displayed square-root rate. Thus fixed-Gaussian Mosco weak liminf fails in
that window. Tensoring with K1471's normalized degree-zero harmonic BRST vacuum
transfers the same obstruction to the full forms and harmonic compression.

The weak limit may be zero; Mosco weak liminf still applies to it. No compactness,
nonzero weak-limit theorem, recovery sequence, true-ground-energy recentering,
interacting continuum BRST operator or changed-representation result follows.

## K1507 — admission replay

The bridge census is now 204 rows: 129 satisfied, ten conditional, 61 excluded
and four missing. SC-ACT-01/02/06 remain `ASSERTS`, SC-META-53 remains
`UNCERTAIN`, the physics ledger stays 33 SAME / 22 DIFFERS / 31 NEEDS /
2 OVER-DETERMINED, K1145/K1150 stay `0/7`, and no source, canon, paper,
prediction, confirmation or public status moves.

## Postflight hostile review

The strongest overclaim would call the logarithmic-over-logarithmic window
optimal or treat its Ritz rate as the ground-energy asymptotic. Neither follows:
the complete-pairing count and Hermite coefficient bound are deliberately
crude, while the argument supplies no many-chaos lower bound. The strongest
contrary route is still kinetic localization/coercivity for the actual ground
state; it could put the energy on another scale. The weakest transfer seam is
the fixed Gaussian representation. A singular dressing or non-Gaussian measure
can change compactness and the appropriate recentering problem.

The most delicate internal seam is the diagram cut: the bound uses that every
non-Gaussian complete pairing contains a nontrivial contraction of the
normalized fourth-chaos kernel. Whole-vertex four-edge pairings are removed as
the Gaussian subfamily before the first-cut argument. Under that exact
partition, K1498's contraction defect controls every residual diagram.

## Exact next input

For the quantum arc, sharpen the diagram constants or prove a matching
many-chaos kinetic-localization lower boundary for the true `E_N`; only then
test true-ground-energy recentering, compactness and Mosco recovery on one
common nonlinear domain. Independently, advance K1413 through a genuinely
gauge/Maxwell-dependent spacetime, secondary-null or derivative/nonlocal
estimate controlling both leakages. Source admission still requires an
action-owned primitive circle, kinetic normalization, physical carrier and
faithful observed intertwiner.
