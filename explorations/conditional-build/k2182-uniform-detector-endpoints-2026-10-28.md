---
title: "K2182 Endpoint cusp and uniform detector certification"
status: active_research
doc_type: exploration
created: "2026-10-28"
classification: BRIDGE_OR_SEMANTIC_BOUNDARY
target_claim: NONE-NOT-A-KILL
claim_ceiling: supplied positive free-field binary diagonal instrument, arbitrary feasible signed contrast and threshold, vacuum output field energy only
scripts:
  - tests/channel-swings/k2182_uniform_detector_endpoints_probe.py
---

# K2182 Endpoint cusp and uniform detector certification

> **GU-COMPARATOR-ROUTING: scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`.

```gu-typed-objects
result: K2182 endpoint cusp, local threshold saturation and uniform approximation
carrier: fixed positive scalar Fock vacuum and photon-added signal with binary diagonal local occupation effects LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert form and free vacuum output energy ON=declared_carrier
real_structure: positive square-root diagonal Kraus followed by one real squeeze per reported outcome
grading: occupation number, not source ambient chirality
action_owner: repository-construction: supplied free Hamiltonian and instrument class
target: finite-budget lower energy envelope and inverse contrast bound MAP-TYPE=intertwiner
```

## Result and scope

For the supplied binary diagonal instrument, the optimized field-energy frontier
has an explicit square-root cusp at maximal contrast. The threshold is attained
exactly, and the exact-contrast frontier is strictly increasing, in the proved
neighborhood [3/4-1/1024,3/4]. The leading defect allocation is determined.
Combining this quantitative endpoint theorem with K2180 removes the vanishing
margin gap in its theoretical finite approximation interface.

This is GU-independent mathematics of the fixed positive free scalar Fock model.
The cost excludes apparatus, clock, preparation, switching and reset. Source
SC-META-53 remains UNCERTAIN. No source, ledger0.263, LT-SM8/LT-GR6b, canon,
physical quotient, arbitrary-channel, novelty or external-expert verdict changes.
Global monotonicity, global threshold saturation and optimizer uniqueness are
not asserted. K2176's half-contrast numerical bracket remains unchanged.

## Definitions and reused endpoint

Use [K2180](k2180-detector-contrast-frontier-2026-10-28.md)'s definitions:
p_n=(3/4)4^-n, q_n=3n-1, 0<=x_n<=p_n, y=p-x,
R(x)=sum(n+1/2)x_n, T(x)=sum(n+1)sqrt(x_n x_(n+1)), C=40/3,
A(s)=41s²/6+3/(2s²), and

    E(x;s1,s0)=R(x)A(s1)+R(y)A(s0)-C[s1 T(x)+s0 T(y)]+35/18.

A representative minimizer has s=(s1,s0) in S², S=[2/3,113/100].
F(d) minimizes E at exact contrast d=sum q_n x_n; For 0<=d<=3/4, V(d) minimizes it for
contrast at least d. Outcome swap gives F(-d)=F(d) and the same threshold
value for absolute contrast. Compactness and uniformly summable moment and
coherence bounds give attainment and continuity, as in K2178/K2180.

The unique maximal-contrast profile r+ is x0=0, xn=pn for n>=1. Its moments
are R1=11/24,R0=3/8,T1=7/24,T0=0. Write a=s1*, b=s0* for its unique
minimizing squeezes, where

    451a^4-280a^3-99=0,    b=(9/41)^(1/4).

Let Emax=E(r+;a,b). This endpoint was already certified in K2160/K2162;
the new statement concerns its neighborhood, not a new endpoint value.
Set delta=3/4-d. The exact nonnegative defect identity is

    delta=x0+sum_(n>=1)(3n-1)y_n.                       (1)

## Uniform boundary-edge expansion

For 0<=delta<=3/8 and every s in S²,

    E(x;s)=E(r+;s)-C[s1 sqrt(p1 x0)+s0 sqrt(p0 y1)]+Remainder,
    |Remainder| <= M delta,     M=369/10.              (2)

Here are bounds on the actual infinite sums. Moment displacement is
|R(x)-11/24|<=3delta/4, since (n+1/2)/(3n-1)<=3/4 for n>=1.
The range of A on S has width less than4, so the moment-energy error is
at most3delta.

For click coherence, remove edge0. Its bulk loss relative to r+ is nonnegative.
The elementary inequality 1-sqrt((1-u)(1-v))<=u+v on [0,1] and p_(n+1)=p_n/4
bound this loss by sum_(n>=1)c_n y_n, with c1=1 and
c_n=(5n+1)/2 for n>=2. Since c_n/(3n-1)<=11/10, the loss is
at most (11/10)sum q_n y_n. Edge0 differs from sqrt(p1 x0) by at most
sqrt(x0 y1)<=delta/(2sqrt2). Thus the total click remainder is at most
(3/2)delta, because 11/10+1/(2sqrt2)<3/2.

For no-click coherence, its edge0 differs from sqrt(p0 y1) by at most
sqrt(x0 y1). Its bulk is bounded by
sum_(n>=1)(n+1)(y_n+y_(n+1))/2. The coefficient of y1 is1 and of yn for
n>=2 is n+1/2, hence bulk<=3delta/4. Both quantities are nonnegative;
the remainder is their difference, so its absolute value is at most the
larger bound, namely3delta/4. Therefore the energy remainder is at most
[3+C(113/100)(3/2+3/4)]delta=(369/10)delta. This is a uniform bound,
not a truncated-sum numerical assertion.

## Sharp leading cusp

Define

    kappa(s)=10/sqrt(3) sqrt(s1²+2s0²),
    kappa=kappa(a,b),    mu=41/8,    L=M+800/123.

Cauchy-Schwarz and (1) give
C[s1 sqrt(p1 x0)+s0 sqrt(p0 y1)]<=kappa(s)sqrt(delta).
Equality is achieved by the cap-feasible two-coordinate profile

    x0=delta s1²/(s1²+2s0²),
    y1=delta s0²/(s1²+2s0²),  y_(n>=2)=0.             (3)

Indeed x0<=delta<=3/8<p0 and y1<=delta/2<=3/16=p1.
The endpoint energy has Hessian diag((11/24)A''(s1),(3/8)A''(s0))>=mu I,
since A''(s)=41/3+9/s^4. Also kappa is Lipschitz with constant
ell=sqrt(200/3). For z=||s-(a,b)||,

    E(x;s)>=Emax-kappa sqrt(delta)+mu z²/2-ell sqrt(delta) z-M delta.

Completing the square costs ell²/(2mu)=800/123. Using (3) at (a,b) for
the upper bound proves, for 0<=delta<=3/8,

    Emax-kappa sqrt(delta)-L delta
       <= F(3/4-delta)
       <= Emax-kappa sqrt(delta)+M delta.             (4)

Since kappa>0 this is a genuine cusp: differentiability with finite one-sided
slope at maximal contrast is impossible. It supplies no derivative formula at
interior contrasts. The witness (3) need not be the exact optimizer.

## Released local threshold theorem

On [3/4-1/1024,3/4], V(d)=F(d), and F is strictly increasing.
At a profile of defect epsilon in (0,1/1024], keep its squeezes fixed and use
(3) at defect4epsilon. Its energy minus the original is at most

    -kappa(s)sqrt(epsilon)+5M epsilon
    <=-(20/3)sqrt(epsilon)+5M epsilon <0.             (5)

The uniform lower bound kappa(s)>=20/3 follows from s1,s0>=2/3, and
20/3-5M/32=173/192>0. The new profile is capped because4epsilon<=3/8.
If a threshold minimizer has actual contrast c>d, a sufficiently small positive
convex mixture with this lower-energy profile still has contrast>=d. Energy
is convex in x at fixed squeezes, so it strictly decreases: contradiction.
The epsilon=0 case uses any sufficiently small positive defect in (3), whose
square-root decrease dominates its linear remainder. At d=3/4 there is only
r+. This proves saturation including the endpoint.

For d1<d2 in the neighborhood, start at an optimizer for d2. The same decrease
and a sufficiently small mixture produce contrast>=d1 with energy<F(d2).
Thus V(d1)<F(d2), and saturation proves F(d1)<F(d2). This argument does not
assume convexity of F after squeeze minimization. It does not extend the local
interval to all contrasts.

## Optimizer localization

Uniformly over all minimizing profiles as delta decreases to zero,

    ||s-(a,b)||=O(sqrt(delta)),
    sum_(n>=2)q_n y_n=O(delta^(3/2)),
    x0/delta -> a²/(a²+2b²),
    y1/delta -> b²/(a²+2b²).                          (6)

To see this, combine the upper witness in (4) with the lower coercive bound
before completing the square. For z=||s-(a,b)|| this gives
(mu/2)z²-ell sqrt(delta)z<=2Mdelta, hence z=O(sqrt(delta)).
Write G=C[s1 sqrt(p1 x0)+s0 sqrt(p0 y1)]. Equation (2), the upper witness,
and E(r+;s)>=Emax then give kappa(s)sqrt(delta)-G=O(delta).
If tdelta=delta-x0-2y1, Cauchy gives G<=kappa(s)sqrt(delta-tdelta).
Since sqrt(delta)-sqrt(delta-tdelta)>=tdelta/(2sqrt(delta)) and
kappa(s)>=20/3, tdelta=O(delta^(3/2)). After division by sqrt(delta),
the Cauchy inequality becomes asymptotically equality. Its unique nonnegative
unit maximizing direction, together with s->(a,b), yields the two ratios.
This localizes every sequence of optimizers without proving uniqueness.

## Released uniform finite-head repair

The endpoint theorem gives the explicit modulus

    |F(3/4-delta)-Emax|<=12sqrt(delta)+44delta,          (7)

because kappa<=113/10 and M+800/123<44. The same envelope holds for V near
the endpoint: every feasible actual contrast has smaller defect, and r+ is
feasible. A stronger direct repair removes the endpoint gap for the finite
program without a split into endpoint and interior regions.

Reuse K2180's relaxed finite-head minimum m_K(d), half tail and quantities
B_K=3(K+1)4^(-K-1), tau_K. Any relaxed full profile v has contrast c with
|c-d|<=B_K/2. Mix it toward the appropriate extremal profile r+ or r- to
reach d exactly. If already equal, do nothing. Explicitly alpha=|d-c|/|d(r)-c| when c differs from d. This absolute denominator
is positive even at the endpoint, and alpha<=1. Put w=(1-alpha)v+alpha r,
u_n=|w_n-v_n|, h=|d(w)-d(v)|. Extremal direction aligns every coordinate
with the sign of q_n, so

    sum |q_n|u_n=h,  |R(w)-R(v)|<=3h/4,
    sum_(n>=0)(n+1)u_n<=h,  sum_(n>=1)n u_n<=h/2.     (8)

For either branch (x or p-x), use
|sqrt(ab)-sqrt(cd)|<=sqrt(b)sqrt(|a-c|)+sqrt(c)sqrt(|b-d|)
and Cauchy-Schwarz in each weighted edge sum. Since
sum(n+1)p_(n+1)=1/3 and sum(n+1)p_n=4/3,

    |T(w)-T(v)| <= (1+sqrt(2))sqrt(h/3).

These bounds hold for the complement branch too. The moment-energy change
is at most3h, and C(s1+s0)<=452/15. Therefore fixed squeezes obey

    |E(w;s)-E(v;s)|
      <=3h+(452/15)(1+sqrt(2))sqrt(h/3).

With h<=B_K/2, define

    rho_uniform(K)=3B_K/2+30sqrt(B_K).                 (9)

The constant30 is conservative: sqrt(2)<10/7 and
452²(3+20/7)<450²*6 imply (452/15)(1+sqrt(2))/sqrt(6)<30.
Thus, for EVERY d in the closed range [-3/4,3/4],

    m_K(d)-tau_K <= F(d) <= m_K(d)+rho_uniform(K).     (10)

The lower side is K2180's unchanged tail replacement proof. A true extremal
profile has a feasible relaxed head, so no domain disappears at endpoints.
For thresholds use the threshold head set; leave already feasible v unchanged
and repair upward only when c<d. Then h<=B_K/2 and (10) holds with the
threshold minimum and V for all d in [0,3/4]. Absolute thresholds use swap.
The result does not assume saturation outside the proved local interval.

This is an endpoint-uniform O(sqrt(K)2^-K) error bound. Away from endpoints,
retain the better K2180 repair min(rho_uniform,WB_K/(2eta)), W=602/45,
eta=3/4-|d|>0. A fully rational conservative version replaces sqrt(B_K) by
3(K+1)/2^(K+1), using sqrt(3(K+1))<=3(K+1). Increasing K until the combined
tail, repair and finite-solver tolerance is below any rational epsilon is
therefore terminating, uniformly in contrast, including endpoints. Exact
algebraic endpoint evaluation remains a cheaper option exactly at maximal
contrast. The finite semialgebraic optimization itself is still unimplemented;
this is a proved error interface, not a new numerical optimum or complexity bound.

## Verification and remaining work

The exact probe checks the defect equation, edge-coefficient bounds, cusp
allocation and caps, strong-convexity constants, threshold descent margin and
rational uniform cutoff, with genuine changed-equation/data faults after a
green baseline. Full-tail rational interval evaluations test representative
profiles against (2); they supplement the written infinite-sum proof.
Independent internal review checks that proof and its optimized transfer.

General threshold saturation, interior squeeze structure, a practical certified
finite optimizer and physical autonomous controller remain distinct tasks.
No proof-assistant or external-expert certification is claimed.
