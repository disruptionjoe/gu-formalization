---
title: "K1386--K1390 diagonal covariant hierarchy"
status: active_research
doc_type: conditional-build-result
classification: SOURCE_NATIVE_ROUTE
direction: observed_to_native
target_claim: SC-META-53
created: "2026-10-07"
updated_at: "2026-10-07"
---

# K1386--K1390 diagonal covariant hierarchy

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `SOURCE_NATIVE_ROUTE` only because this packet tests the
maximal-compact analytic route left uncertain by SC-META-53. The compact
circle, unbounded generator, charge regularizer, scalar-electrodynamics
action, Lorenz gauge and every high-regularity norm below are repository
constructions. They do not identify a source-selected action, observed charge
assignment, physical gauge quotient or source observation map.

Scope: an exact covariant commutator filtration, a finite triangular
charge--spatial hierarchy, closure of the differentiated Maxwell source, and
a closed local high-regularity a priori inequality. No smooth-solution
construction, global large-data propagation, nonlinear KT range, proper
BV-BFV quotient, quantization or GU physical cohomology is constructed.

```gu-typed-objects
result: covariant derivative-charge filtration, finite triangular high-regularity hierarchy, differentiated Maxwell-source closure and local continuation bound
carrier: Lorenz-gauge scalar-electrodynamics data on R x T3 with the unbounded self-adjoint integer generator Q on the K-finite common core LAYER=toy BRIDGE=maximal-compact-charge-reduction CHIRALITY=N/A
pairing: positive gauge-fixed Sobolev control norm plus triangular charge-regularized matter energy ON=repository_owned_control
real_structure: real Abelian connection and complex principal-series Hilbert matter carrier
grading: covariant derivative order, integer compact charge and BRST ghost degree
action_owner: repository-construction -- K1359/K1366, not a released source action
target: SC-META-53 conditional nonlinear propagation boundary MAP-TYPE=restriction
```

## Preflight bookend

K1381--K1385 prove that a finite rectangular charge--Sobolev hierarchy cannot
close the finite-`p` bare Hölder estimate: its top corner asks simultaneously
for another charge and `3/p` more spatial derivatives. That statement leaves
open a diagonal hierarchy in which spatial and charge order are not
independent ceilings.

The route-changing identity is already forced by the admitted gauge action:
the curvature of `D=partial+iAQ` is `FQ`. The cheapest constructive question is
therefore whether each covariant commutator exchanges derivative position for
one `Q` while preserving combined order. If so, the differentiated Maxwell
source must be checked on the same tier and the resulting norm must pay its
own coefficient bounds. A source/action-owned observed-carrier selector is the
strongest independent alternative, but the released corpus still supplies no
generator normalization, observed intertwiner or domain-preserving selector.

## K1386 — the covariant commutator is triangular

On the smooth spacetime/K-finite common core,

```text
D_mu=partial_mu+i A_mu Q,
[Q,D_mu]=0,
[D_mu,D_nu]=i F_mu_nu Q.
```

The first commutator with the covariant wave operator is

```text
[D_a,D^mu D_mu]u
 =i(partial^mu F_(a mu))Q u+2i F_a^mu Q D_mu u.
```

Inducting on an ordered multiindex `alpha` gives only terms of the form

```text
(partial^beta F) D^gamma Q^(n+1) phi,
|beta|+|gamma|<=|alpha|,
```

when the equation for `D^alpha Q^n phi` is commuted. The matter factor has

```text
|gamma|+(n+1)<=|alpha|+n+1.
```

Thus a commutator can move one unit from covariant-derivative position to
charge position, but it creates no new combined-order tier. This is an exact
curvature identity, not a null-form cancellation.

## K1387 — a finite triangular hierarchy closes the matter commutators

For an integer `R>=3`, define

```text
T_R={(alpha,n): |alpha|+n<=R}.
```

Sum over `T_R` the energies of `D^alpha Q^n phi`:

```text
||D_t D^alpha Q^n phi||_2^2
+||D_x D^alpha Q^n phi||_2^2
+m^2||D^alpha Q^n phi||_2^2
+mu||Q D^alpha Q^n phi||_2^2.
```

Each index controls one additional covariant derivative and one additional
charge in the alternative principal terms. K1386 therefore places every
commutator factor on the already controlled tier of combined order at most
`R+1`. Unlike a rectangle, the triangle does not demand the simultaneous new
corner `(S+3/p,N+1)`.

The radial term causes no internal-charge loss because `Q` commutes with its
real scalar multiplier. Spatial commutations of the cubic radial term close
by the ordinary `H^R(T3)` tame product estimate. This is a finite
high-regularity repair of the algebraic staircase, not yet a bound on the
coupled coefficients.

## K1388 — the Maxwell source uses the same tier

The source is

```text
j_nu=e Im<Qphi,D_nu phi>.
```

It is gauge invariant, so ordinary derivatives of the pairing can be expanded
covariantly. Every term in `partial^alpha j` pairs factors of the schematic
form

```text
D^beta Qphi,       D^gamma Dphi,
|beta|+|gamma|<=|alpha|,
```

plus lower curvature commutators. For `|alpha|<=R`, either high factor has
combined order at most `R+1`, which is exactly K1387's principal tier. The
three-dimensional algebra and tame estimates for `R>=3` yield

```text
||j||_(H^R)<=C_R Y_R^2.
```

In Lorenz gauge, the component wave equations for `A` therefore satisfy the
matching high-order Maxwell energy estimate. The same smooth Noether identity
used in K1374 propagates the differentiated Lorenz/Gauss constraint. This is a
gauge-fixed analytic closure; it is not closed KT range or a physical BFV
quotient.

## K1389 — the hierarchy pays its local coefficient norm

Let `Y_R^2` be the positive componentwise Lorenz-gauge
`H^(R+1) x H^R` wave norm of `A` plus the K1387 matter energy. For smooth
K-finite solutions define the low coefficient

```text
B_R=1+||A||_(W^(1,infinity))+||F||_(W^(1,infinity))
      +||phi||_infinity^2+||Dphi||_infinity+||Qphi||_infinity.
```

The K1386 commutators, K1388 current bound and cubic tame estimate give

```text
dY_R/dt<=C_R B_R Y_R.
```

Because `R>=3`, Sobolev embedding on `T3` and the same finite triangular norm
give

```text
B_R<=C_R(1+Y_R)^2,
dY_R/dt<=C_R(1+Y_R)^2Y_R.
```

If `Y_R(0)=Y_0`, a bootstrap Gronwall argument gives the explicit local bound

```text
Y_R(t)<=2Y_0
for 0<=t<=log(2)/(C_R(1+2Y_0)^2).
```

More generally, the high norm continues across every finite interval on which
`integral B_R dt` is finite. This closes the local a priori hierarchy on one
finite triangular topology. It does not construct the smooth solution to
which the estimate applies. It also does not close globally: K1379 already
shows that base energy plus Gauss does not control the necessary endpoint
coefficient norms, and no dispersive decay or coercive spacetime monotonicity
is supplied here.

## K1390 — admission replay

The bridge census now has 61 rows: 40 satisfied, six conditional, eleven
excluded and four missing. Four new satisfied rows record the commutator
filtration, finite triangular matter closure, differentiated Maxwell-source
closure and closed local a priori inequality. The finite-`p` rectangular
nonclosure remains true at its stated method scope; the diagonal repair does
not reverse it.

The same four source/physical rows remain missing: source-owned selection and
normalization; identification with one source action; a closed fully coupled
global nonlinear BV-BFV quotient with positive physical Hilbert cohomology;
and a source-owned observed-state/export map. K1145/K1150 remain `0/7`.

## Postflight hostile review

The strongest overclaim is that a closed local high-regularity inequality is a
global well-posedness or physical-quotient theorem. It is neither. The
strongest contrary construction remains K1379's fixed-base-energy
concentration family, which prevents the local coefficient from being bounded
by the conserved base energy. The weakest reproducibility seam is the
gauge-fixed tame estimate: it applies to smooth Lorenz-gauge common-core
solutions and does not itself build a completed gauge-independent flow.

The repair is structural and useful: it proves that the top-corner loss is an
artifact of independent rectangular ceilings, not an unavoidable feature of
the covariant equation. It is nevertheless repository-owned. No source,
ledger, canon, paper, prediction, confirmation or public posture moves.

## Exact next input

Construct smooth local evolution on the completed finite triangular graph
domain and prove gauge-independent continuation, then seek a global estimate
for `integral B_R dt` through a genuine dispersive, Morawetz, null-form or
small-data mechanism. Only after global coupled propagation should closed
nonlinear KT range, BV-BFV properness and positive physical cohomology be
attempted. Independently, a source/action-owned observed-carrier selector must
fix `Q` and its normalization while preserving the triangular domain.
