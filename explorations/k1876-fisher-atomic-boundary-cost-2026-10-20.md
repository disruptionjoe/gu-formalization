---
title: "K1876: Sharp Fisher cost at the atomic sixth-moment boundary"
status: active_research
doc_type: exploration
created: "2026-10-20"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: sharp scalar endpoint and explicit value bounds; no computed sextic coefficients or spectral gap, GU physics or novelty claim
---

# The tight tail cap costs (k+1)² divided by its slack

For the K1874 problem, raw second moment1, fourth moment k>3 and sixth
moment at most M, write delta=M-k². Then

```
lim_(delta->0+) delta V(k,k²+delta) = (k+1)².           (1)
```

This is the OTHER endpoint from K1874's large-M law. Its score projection
had coefficient (k-3)² near the atomic boundary; that lower bound remains
correct but is not sharp there. A sign-adjusted score and an exactly
moment-matched, unequal-variance Gaussian mixture close the gap.
The proof also yields a finite-slack lower bound and a rigorous narrow
value bracket at k=4, M=16+10^-12. No numerical sextic eigenproblem is needed.

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

```gu-typed-objects
result: sharp atomic-boundary Fisher cost, finite-slack bound and optimal Gaussian width allocation
carrier: real probability densities on R, raw second1 fourth k>3 sixth<=M LAYER=toy CHIRALITY=N/A
pairing: Fisher energy4 integral |u'| squared with u=sqrt(p) ON=real_H1_functions
real_structure: nonnegative real densities and real polynomial moments
grading: moment degree and small positive cap slack
action_owner: repository-construction -- constrained scalar Fisher functional
target: sharp minimum value as M approaches k squared MAP-TYPE=evaluation
```

## 1. Scope and prerequisite

[K1874](k1874-fisher-sixth-moment-cap-2026-10-20.md) supplies feasibility
M>k², attainment, a unique positive even optimizer, and convergence to atoms
at0 and +/-sqrt(k). We reuse those results without rerunning their proofs.
The current argument works directly on all feasible densities; it does not
assume a numerical optimizer or use evenness in the lower bound. The upper
trial is even. This is independent probability mathematics, with no source,
physics-ledger, canon or novelty claim.

The primary publisher abstract of [Minimum Fisher information of
moment-constrained distributions with application to robust blind identification
(1998)](https://www.sciencedirect.com/science/article/abs/pii/S0165168497002259)
describes higher-moment Fisher minimization and Gaussian-mixture approximations.
It establishes relevant prior work, not the specific endpoint formula here.
The proof below is supplied explicitly; no inaccessible theorem is imported.

## 2. A finite-slack lower bound that sees all three wells

For a>0 define g=x³-kx, h=(x²-a)/(x²+a), and psi=h g. Then
psi²<=g² and E g²=E X6-k²<=delta. For finite Fisher, score integration
by parts gives E[rho psi]=-E psi'. Smooth cutoffs justify it: psi grows
cubically, psi' quadratically, and finite sixth moment controls the score
product by Cauchy-Schwarz. Infinite Fisher satisfies the lower bound trivially.
Consequently

```
I(p) delta >= (E psi')².
```

The exact algebraic identity

```
psi'=k+(k-3a)x²/(k+a) + x g R_a(x²),
R_a(s)=2[a(5a+3k)+(3a+k)s]/[(a+k)(a+s)²]
```

gives a uniform remainder estimate. For s>=0,

```
0<=R_a(s)<=2(5a+3k)/[(a+k)(a+s)],
sqrt(s)/(a+s)<=1/(2sqrt(a)).
```

Using E X²=1 and Cauchy-Schwarz, therefore,

```
E psi' >= k+1 - 4a/(k+a)
                  - (5a+3k)/(k+a) sqrt(delta/a).
V(k,k²+delta) >= [k+1-4a/(k+a)
                  -(5a+3k)/(k+a)sqrt(delta/a)]_+²/delta.       (2)
```

The positive part is essential: squaring a possibly negative lower bound
would be invalid. This is a finite-budget bound, not only an asymptotic.
Choosing a=delta^(1/3) yields the simpler explicit estimate

```
delta V >= [k+1-(5+4/k)delta^(1/3)]_+².                       (3)
```

Thus liminf delta V >=(k+1)². No weak-limit transfer is needed for this
step. Intuitively, h reverses the score test near the central well, so the
contributions add rather than cancel. At the limiting atoms their weighted
absolute derivatives are (1-1/k)k+(1/k)2k=k+1, whereas the unadjusted
signed derivative gives3-k. This explains the two different coefficients.

## 3. Exactly feasible unequal-width trial

Let t>0 be small, y(t) the root near k of

```
F(t,y)=(1-t)y²+(3t-k)y+kt/2-9t²/4+3t³/4=0,
w(t)=(1-t)/(y(t)-t/2),
p_t=(1-w)N(0,t)+(w/2)N(+sqrt(y),t/2)+(w/2)N(-sqrt(y),t/2).
```

F(0,k)=0 and F_y(0,k)=k>0. The implicit function theorem gives a real
analytic root for all sufficiently small positive t, with y>0,0<w<1.
Explicitly it is the larger quadratic root; its discriminant is
`k²-8kt+(2k+18)t²-12t³+3t4`, positive near0.
The Gaussian moments give E X²=1 exactly and
`(E X4-k)(y-t/2)=F(t,y)=0`. There is no approximate moment matching.

The sixth moment is

```
M(t)=15(1-w)t³+w[y³+(15/2)y²t+(45/4)yt²+(15/8)t³].
y'(0)=k-7/2,   w(0)=1/k,
M(0)=k²,      M'(0)=k(k+1)>0.
```

Hence M(t) is locally strictly increasing and every sufficiently small
positive delta has an exactly feasible t(delta), with
`t(delta)=delta/[k(k+1)]+O(delta²)`. Convexity of Fisher under mixing gives

```
I(p_t) <= (1-w)/t + w/(t/2) = (1+w)/t.
limsup delta V <= k(k+1)(1+1/k)=(k+1)².
```

The mixture bound is not an equality for its Fisher information. The lower
bound applies to the trial too, so it also proves the trial is asymptotically
optimal in Fisher value. This proves (1), not a Gaussian shape theorem for
the exact optimizer at its individual wells.

## 4. Executed allocation and scaling consumers

For trial central variance c0*t and outer variance c1*t, the limiting masses
are p0=1-1/k,p1=1/k. The leading cost times slack is

```
(p0/c0+p1/c1)(p0 k² c0+p1 4k² c1)
 = (k+1)²+(k-1)(c0-2c1)²/(c0 c1).                         (4)
```

Thus c0=2c1 is the unique optimal positive ratio in this Gaussian-mixture
allocation problem. Equal widths cost k(k+3), larger by k-1. This explains
why repeating K1874's equal-width trial cannot attain the tight-cap constant.
It is a statement about leading trial allocation, not an unproved local
central-limit theorem for all minimizing densities.

For raw second moment s>0, fourth q>3s² and sixth cap R>q²/s, scaling
X=sqrt(s)Y gives I(X)=I(Y)/s. Therefore the sharp divergence is

```
V(s,q,R) ~ (q+s²)²/[s(sR-q²)] as R decreases to q²/s.
```

Both boundary regimes now have different useful constants: the large-cap
cost excess is (k-3)²/M, and the tight-cap total cost is (k+1)²/(M-k²).
They concern the same moment problem but cannot be interchanged.
For any large allowed Fisher budget L, the minimum feasible cap slack has
leading (k+1)²/L. This is an asymptotic budget law; use (2) and the exact
trial, not the asymptotic alone, for a finite certificate.

## 5. A finite certified value bracket

At k=4, delta=10^-12, choose a=1/10000 in (2). Exact rational arithmetic
bounds its square-root expression below by9999/2000. For the upper bound
choose `t=1/20001000000000`. The larger root lies in

```
4+t/2-10t² < y(t) < 4+t/2+10t².
```

The polynomial has opposite signs at these endpoints and positive derivative
throughout the interval. Positive-term interval substitution in the Gaussian
sixth moment proves M(t)<16+10^-12. Substitution in (1+w)/t proves

```
24.99500025 < 10^-12 V(4,16+10^-12) < 25.002.                (5)
```

These are rational, rigorously directed bounds on the actual minimum,
not floating quadrature or a guessed leading coefficient. Their total width
is below0.028 percent of25. The trial's mean separation, weight and widths
are defined algebraically. Sextic coefficients, a spectral gap and optimizer
TV/entropy error are not supplied by this value bracket.

## 6. Evidence, hostile review and remaining boundary

The [producer](../tests/channel-swings/k1876_fisher_atomic_boundary_cost.py)
checks19 symbolic/rational groups and2 upstream pins. The
[independent probe](../tests/channel-swings/k1876_fisher_atomic_boundary_cost_probe.py)
uses157 rational controls,6 reporting/pin checks,6 mathematical coefficient
faults and4 reporting faults, with a clean baseline first. The symbolic
identities, positive rational brackets and analytic proof above carry the
claim. Rational sampling is an additional control, not proof of a continuum
inequality. No proof-assistant or external expert verification is claimed.

Hostile review addressed non-even densities, score cutoff tails, a negative
bound before squaring, exact versus approximate moments, inequality rather
than equality cap, IFT positivity and monotonicity, the mixture upper bound,
and the difference between trial-width optimality and actual optimizer shape.
The all-positive interval sixth-moment upper expression intentionally discards
a negative term; the certified inequality still holds. No open scientific
finding from these checks is suppressed.

A second-order sharp endpoint expansion, actual well-profile convergence and
sextic coefficient/gap enclosures require new proof. The finite estimate and
allocation/scaling/budget consequences above are completed; they do not imply
any GU physical prediction or change any source or physics-ledger verdict.
