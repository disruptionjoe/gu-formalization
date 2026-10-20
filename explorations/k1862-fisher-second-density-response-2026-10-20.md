---
title: "K1862: Second Fisher density response and its precise stability class"
status: active_research
doc_type: exploration
created: "2026-10-20"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: second weighted density response for exact optimizers, unweighted response for o(q4)-excess competitors and finite-q excess-to-TV stability; no effective asymptotic error, higher value coefficient or GU physics
---

# Second Fisher density response and its precise stability class

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
result: second optimizer profile, polynomial response, strong near-optimizer stability and an exact-moment tail counterexample
carrier: real probability densities on R with raw second moment1 and fourth moment3-q LAYER=toy CHIRALITY=N/A
pairing: Fisher integral 4 integral |(sqrt p)'| squared ON=real_Sobolev_functions
real_structure: real nonnegative densities; no physical real-form identification
grading: polynomial Hermite degree only
action_owner: repository-construction -- scalar moment-constrained Fisher functional
target: unrestricted real-line density problem MAP-TYPE=evaluation
```

## 1. Result and the independent missing estimate

Let phi be the standard Gaussian density, Hn its probabilists' Hermite
polynomials, and p_q the exact optimizer with raw E X²=1 and E X4=3-q.
Write F(3-q)=I(p_q), psi_q=sqrt(p_q), psi0=sqrt(phi), and

```
u=-H4/48,
v=-1/192-H2/48-H4/64+H6/216+H8/4608,
D2=2v+u²=7H6/432+H8/1152.                              (1)
```

For every fixed nonnegative integer m, as q decreases to0,

```
||(1+|x|^m)[psi_q-psi0(1+q u+q²v)]||_2
 +||(1+|x|^m)[psi_q-psi0(1+q u+q²v)]'||_2 =o(q²),       (2)

integral (1+|x|^m)|p_q-phi[1-q H4/24+q²D2]| dx=o(q²).  (3)
```

Consequently every fixed polynomial observable has a second response.
For arbitrary exact-moment competitors with excess
`I(p)-F(3-q)=o(q⁴)`, the same square-root expansion holds in H1(phi)
after division by psi0, and the density expansion holds in unweighted L1.
It need not hold for their unbounded polynomial observables: section7 gives
an exact-moment family with excess at most9q⁵ but sixth moment tending to
infinity. These are scalar mathematical statements, with no GU or novelty
claim and no claimed effective rate for the little-o terms.
Independently of those asymptotics, the same gap gives the finite-precision
bound `TV(p,p_q)<=sqrt(5[I(p)-F(3-q)]/6)` for `0<q<=1/100`.

[K1843](k1843-unrestricted-fisher-variational-gap-2026-10-20.md) supplies the
positive quartic ground state, its dual, and virial identities;
[K1851](k1851-fisher-parity-stability-2026-10-20.md) supplies unrestricted
uniqueness. [K1859](k1859-fisher-optimizer-tail-response-2026-10-20.md) proves
the quartic value, uniform Gaussian envelope, and second *score-defect*
profile, while explicitly leaving the second density response open.
Its upper trial's polynomial v is a candidate, not an optimizer proof.

Preflight compared three routes: multiplying K1857's H1 convergence by H3,
solving another fitted spectral problem, and using a Gaussian quasimode of
the actual Euler operator. The first lacks a weighted estimate; the second
would not certify an asymptotic profile. The third wins because the existing
fourth-order value controls the multipliers to second order and a uniform
spectral gap turns a small residual into a small state error. Searches for
second density response, weighted response and quasimode found no completed
version in the preceding Fisher chain. No earlier result is being corrected.

## 2. Convex secants give multipliers without differentiating little-o

Set G(q)=F(3-q)-1. K1859 gives

```
G(q)=q²/6+q³/4+11q⁴/108+o(q⁴).
```

The exact quartic multiplier b_q is a subgradient of G. Fix epsilon>0 and
take h=epsilon q². For q sufficiently small both q-h and q+h are in(0,2).
The subgradient inequalities give

```
[G(q)-G(q-h)]/h <=b_q<=[G(q+h)-G(q)]/h.                (4)
```

For each fixed epsilon, the remainder differences divided by h are o(q²).
The polynomial secants equal `q/3+3q²/4 +/- epsilon q²/6+o(q²)`.
First take q->0, then epsilon->0. This proves

```
b_q=q/3+3q²/4+o(q²),
a_q=F-2b_q(3-q)=1-2q-11q²/3+o(q²),
E_q=2F-b_q(3-q)=2-q-19q²/12+o(q²).                    (5)
```

No differentiability of G and no derivative of an unspecified remainder
is assumed. Using h proportional to q instead would not recover the second
coefficient from a third-order value with uncontrolled error.

## 3. A uniform gap for the actual full-line oscillator

The operator and its form domain are

```
H_q=-4d²/dx²+a_q x²+b_q x⁴,
Q(H_q)=H1(R) intersect L2(x4 dx).
```

K1859 proves, for 0<q<=1/100, `a_q>=1/2`, `b_q>0`, `E_q<=3`,
and `p_q<=exp(9/4)exp(-x²/4)`. The harmonic comparison operator
`-4d²+a_q x²` has eigenvalues `2sqrt(a_q)(2n+1)`; these follow by
scaling the Gaussian/Hermite eigenfunctions. Its n=1 level is at least
3sqrt(2). Form ordering and the min-max principle therefore give

```
lambda1(H_q)-E_q >=3sqrt(2)-3>1.                       (6)
```

The comparison is legitimate despite the smaller quartic form domain:
the min-max infimum over its subspaces is no smaller than over the harmonic
form domain. Compact resolvent follows from the confining potential, and
K1843 identifies psi_q as the simple positive ground state. This is a
full-line gap; no parity restriction is imposed. The elementary spectral
estimate used below follows by expanding orthogonally to that ground state.

## 4. Quasimode residual, projection, and normalization

Let z_q=psi0(1+q u+q²v). Conjugating the harmonic operator gives

```
(H_0-2)(psi0 f)=psi0 A f,   A f=-4f''+4x f'.
```

Put W1=x4/3-2x² and W2=3x4/4-11x²/3. Exact polynomial identities are

```
A u+W1+1=0,
A v+(W1+1)u+W2+19/12=0,                               (7)
E_phi u=0,   E_phi(2v+u²)=0.
```

Using(5), equations(7) cancel the orders q and q² in
`r_q=(H_q-E_q)z_q`. The remaining terms are polynomials times psi0
with coefficients o(q²) (or O(q³)). Thus for every fixed integer m>=0,

```
||x^m r_q||_2=o(q²),   ||z_q||²=1+O(q³).               (8)
```

Set c_q=<z_q,psi_q> and e_q=z_q-c_q psi_q. Then e_q is orthogonal
to psi_q and `(H_q-E_q)e_q=r_q`. Equation(6) gives
`||e_q||_2<=||r_q||_2=o(q²)`. The sign c_q>0 for small q follows
from psi_q->psi0 and z_q->psi0 in L2; the former is already K1857,
or follows from K1859's optimizer response. Pythagoras now gives

```
c_q²=||z_q||²-||e_q||²=1+O(q³),
c_q=1+O(q³)=1+o(q²).                                  (9)
```

Normalization is therefore part of the argument; it is not replaced by
declaring the signed polynomial trial to be the positive optimizer.

## 5. Weighted derivative control, including the missing H3 step

Suppress q in the notation. Multiplication of `(H-E)e=r` by x^(2m)e
and integration by parts gives, for m>=1,

```
4||(x^m e)'||²+integral(V-E)x^(2m)e²
 =integral x^(2m)e r+4m²||x^(m-1)e||²,                  (10)
```

where V=a x²+b x4. For m=0 the last term is absent. The identity follows
also by expanding `(x^m e)'`; its coefficient 4m² is essential.

All integrations are justified. The existing uniform Gaussian envelope
and the Euler ODE bound psi_q'' by a polynomial times exp(-x²/8),
uniformly in q<=1/100 (the multipliers are bounded there). Since psi_q'
is L2, its limit at either end is zero once psi_q'' is integrable; integrating
psi_q'' from that end gives a polynomial Gaussian bound on psi_q'. The
same facts hold for z and e. Cutoffs followed by dominated convergence
therefore prove(10), with no imposed boundary condition on a ratio.

At m=0, `V>=x²/2`, `E<=3` and(8)-(9) yield

```
4||e'||²+(1/2)||x e||²
 <=3||e||²+||e|| ||r||=o(q⁴).                          (11)
```

Inductively assume `||x^m e||` and `||x^(m-1)e||` are o(q²).
The mixed term in(10) is at most
`||x^(m+1)e|| ||x^(m-1)r||`. Young's inequality absorbs one quarter
of `||x^(m+1)e||²` into the positive potential term, leaving
`||x^(m-1)r||²=o(q⁴)`. This proves both
`||x^(m+1)e||=o(q²)` and `||(x^m e)'||=o(q²)`.
Subtract `m x^(m-1)e` to obtain `||x^m e'||=o(q²)`.
This induction establishes every fixed polynomial weight.

The Gaussian envelope and ODE also bound the corresponding weighted norms
of psi_q and psi_q' uniformly. Equation(9) then permits replacing c_q psi_q
by psi_q in(2). In particular the previously missing multiplication of
the first response by H3 is now legitimate. Equivalently,

```
(sqrt(p_q/phi)-1-q u)/q² -> v in every polynomial-weight H1(phi),
```

because division by psi0 sends a derivative to `e'+x e/2` in L2(dx).
Cauchy-Schwarz applied to the difference of squares, with the same weighted
bounds, proves(3); the q³ and q⁴ polynomial trial terms are o(q²).

## 6. Executed observable and near-optimizer consequences

For every fixed polynomial f, equation(3) gives

```
E_(p_q) f=E_phi f-(q/24)E_phi(f H4)+q² E_phi(f D2)+o(q²).
E X6=15-15q+(35/3)q²+o(q²),
E X8=105-210q+(1085/3)q²+o(q²).                        (12)
```

The density formula is uniform over measurable `|f(x)|<=1+|x|^m`
for each fixed m. This includes bounded-observable and CDF second response.
Normalization, raw second moment and raw fourth moment have zero second
correction because D2 contains only H6 and H8. Odd moments vanish exactly
for the optimizer. No numerical onset or uniformity as m->infinity is claimed.

Now let p be any feasible, possibly asymmetric, density and f=sqrt(p).
The equal raw moments imply the exact quadratic-form identity

```
D=I(p)-F(3-q)=<f,(H_q-E_q)f>.
```

Decompose f=c psi_q+e with e orthogonal to psi_q. Positivity gives c>=0,
and(6) gives `||e||²<=D`. Also
`4||e'||²+(1/2)||x e||²<=D+3||e||²<=4D`.
Normalization gives `c=sqrt(1-||e||²)`; for D->0,
`|1-c|<=||e||²<=D`. Hence when D=o(q⁴),
`f-psi_q`, its derivative, and x times it are o(q²) in L2.
Combining with(2) proves the second H1(phi) square-root profile and the
unweighted L1 density profile for the entire stated near-optimal class.
This does not supply higher weighted norms for e: its Euler residual is
uncontrolled. Section7 makes that distinction necessary, not optional.

### Finite-precision consumer of the same gap

The gap is already uniform on `0<q<=1/100`; the following consequence
requires no limit and no asymptotic error estimate. Put
`g_star=3sqrt(2)-3`. The same spectral decomposition gives
`D>=g_star(1-c²)`. Cauchy-Schwarz on the difference of squares gives

```
TV(p,p_q)=(1/2) integral |f-psi_q|(f+psi_q)
 <=(1/2)||f-psi_q||_2 ||f+psi_q||_2
 =sqrt(1-c²) <= min(1,sqrt(D/g_star)).                  (12a)
```

This is a certificate for any feasible density with finite Fisher, including
asymmetric ones. Since `sqrt(2)>7/5`, one has `g_star>6/5`, and hence the
fully rational weaker bound and its precision budget are

```
TV(p,p_q)<=min(1,sqrt(5D/6)),
D<=(6/5)epsilon²  implies TV(p,p_q)<=epsilon.           (12b)
```

For example excess `D<=3/25000` certifies `TV<=1/100`, uniformly throughout
this near-Gaussian window. An available rigorous upper bound on D may be
substituted; this result does not itself compute F at a supplied q. This is
distance to the true optimizer, not to its polynomial approximation.
It does not produce a finite-q error bound for the second-response expansion,
nor a bound on arbitrary high moments. The tail family below preserves that
distinction even when the TV distance is exceptionally small.

## 7. Executed contrary family: excess o(q4) still permits divergent moments

For 0<q<=1/200 set

```
epsilon=q20, w=q^(-8), v=(1-q12)/(1-q20),
k0=(3-q-3q4)(1-q20)/(1-q12)²,   q0=3-k0.
```

Let r_k0 be the exact optimizer with raw second moment1 and fourth k0,
and r_v its dilation to variance v. Define
`p=(1-epsilon)r_v+epsilon N(0,w)`. Direct algebra gives
`E X²=1` and `E X4=3-q`, exactly. On this full interval,

```
0<q0-q<4q4, q0<2q<=1/100,
1<(1-epsilon)/v<1+2q12.                               (13)
```

For clarity these are whole-interval inequalities, not conclusions from a
grid. The numerator of q0-q is
`3q4-2(3-q)q12+(3-q)q24+(3-q-3q4)q20`; its leading term dominates
the remaining terms on q<=1/200, while `(1-q12)²` is positive and near1.
After division by q4, coefficientwise interval bounds verify both signs.
Likewise the numerator of `(1-epsilon)/v-1` is
`q12-2q20+q40`; division by q12 gives the two bounds in(13).

K1859's b_s<s for s<=1/100 and the subgradient inequality at q0 imply
`F(k0)-F(3-q)<=q0(q0-q)<=8q5`. Fisher convexity and dilation give

```
0<=I(p)-F(3-q)
 <=[F(k0)-F(3-q)]+[((1-epsilon)/v)-1]F(k0)+epsilon/w
 <=8q5+4q12+q28<9q5=o(q4).                            (14)
```

Here F(k0)<2 by the same certified window. But the Gaussian component gives
`E X6>=15 epsilon w³=15q^(-4)->infinity`.
Thus even this strong near-optimal class has the universal *unweighted*
second profile while failing polynomial moment response. No heavy tail is
attributed to the exact optimizer. This also checks that an energy-gap
estimate is not silently being used as an all-weight resolvent estimate.

## 8. Verification, hostile review, and remaining scope

Run `python3 tests/channel-swings/k1862_fisher_second_density_response.py`
and `python3 tests/channel-swings/k1862_fisher_second_density_response_probe.py`.
The producer uses sparse rational polynomials; the independent probe uses
dense rational coefficients and separately reconstructed Hermites. They
check both oscillator perturbation equations, normalization, all reported
moment coefficients, harmonic-gap inequalities, and exact mixture moments
and interval bounds. They also check the rational finite-q gap, TV conversion
and its example precision budget. Input/reference mutations must fail explicit assertions
after a clean baseline; reporting faults are counted separately. Neither
implementation imports the other. Dependency digests preserve the inherited
analytic premises. These arithmetic controls do not prove min-max,
asymptotic secants, spectral projection or the weighted integration argument.

Hostile analytic review checked the order of secant limits, the smaller
quartic form domain, full-line versus even spectral gap, sign and size of
the projection coefficient, every boundary term in weighted integration,
raw versus centered moments, and the exact-versus-near-optimizer scope.
The quasimode may have zeros or signs; only its residual and positive
overlap are used. The true optimizer is never identified with the trial.
All continuum conclusions remain analytic derivations with exact controls,
not formal proof-assistant certification or external peer acceptance.

This closes the second density response left open by K1859 and its bounded
observable and moment consumers. The known fourth-order value is an input,
not a new result here. Effective finite-q second-response error needs an
effective remainder in the multiplier/value input. A fifth value coefficient
would require a new controlled lower-bound calculation; polynomial trial
serialization alone is insufficient. The generic near-optimizer polynomial
extension is explicitly refuted, so it is not a proposed successor.
