---
title: "K2503 The first infinitesimal satellite instability and a finite stopping advantage"
status: active_research
doc_type: exploration
created: "2026-11-02"
classification: CONVENTIONAL_COMPARATOR
target_claim: "NONE-NOT-A-KILL"
claim_ceiling: "conditional supplied-model mathematics; no native GU realization, measured calibration or global stopping frontier"
---

# K2503 The first infinitesimal satellite instability and a finite stopping advantage

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `CONVENTIONAL_COMPARATOR`.

```gu-typed-objects
result: K2503
carrier: original fresh fair test/use stopping law with score S in (0,1/2] LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert trace or original failure-inclusive expected probability cost ON=declared_carrier
real_structure: complex adjoint for instruments; real probabilities for stopping
grading: original verifier sectors or ordered finite stopping stages
action_owner: repository-construction -- supplied positive instruments and original probability law
target: both insertion orders, exact directional boundary and finite original-law counterpolicy MAP-TYPE=evaluation
```

## Result and scope

The first loss of strict first-order stability against a single infinitesimal
satellite, at S=1/2, occurs through a suffix satellite. Its unique onset in
0<d<=1/5 lies between d=4/25 and d=17/100. Every prefix direction is still
strictly stable through17/100. This is a local directional boundary, not the
first global loss of one-stage optimality: finite competitors and mixtures
can act earlier. A positive second-order certificate also proves uniform
small-satellite stability exactly at the directional boundary.

A separate exact finite witness at budget K=2127/100000 has success3/4,
strictly above every mixture of one-stage policies. It lies below the previous
K2493/K2495 witness budgets. The onset also releases a local optimizing branch with satellite score linear
in d-d_* and a quadratic same-budget advantage above the boundary cost.
The finite witness uses the original failure-inclusive
cost and preserves exact success; it is not a continuous-stage approximation.
K2501's very-small-budget all-policy optimum remains intact.

These are GU-independent supplied-model results. SC-META-53 remains UNCERTAIN;
LT-SM8/LT-GR6b, native matter/light and domain obligations do not move.
Source polarities, ledger0.263, canon and physical credit remain unchanged.
No novelty, external-expert or proof-assistant certification is claimed.

## 1. Original cost and exact directional minimization

Reuse K2485's finite-schedule reduction of the original adaptive experiment:

    0<=a_i<=b_i, sum b_i=S,
    p=product_i (1+a_i)^(-1),
    C=2 sum_i P_i w(a_i,b_i), P_i=product_(j<=i)(1+a_j)^(-1),
    w(a,b)=log(1+(b-a)^2/[2(a+b)(2-a-b)]).

At a fixed one-stage (a,S), 0<a<S, insert (rt,t),0<=r<=1, and change the
main stage to ((a-rt)/(1+rt),S-t). This preserves score and p=1/(1+a),
and is feasible for sufficiently small t>0. The K2499 derivatives are

    prefix: g(r)+Ar-B,
    suffix: [g(r)+Mr-N]/L,
    g(r)=(1-r)^2/[2(1+r)], L=1+a,
    A=-2w_a, B=2w_b/L, M=LA+2w, N=LB.                 (1)

Differentiating g gives g'=1/2-2/(1+r)^2 and g''=4/(1+r)^3>0.
For u>=0 the exact minimum of g(r)+ur over[0,1] is

    phi(u)=2sqrt(1+2u)-u-2, 0<=u<=3/2,
           1/2, u>=3/2,
    r_*(u)=2/sqrt(1+2u)-1 on[0,3/2], and0 above.        (2)

Therefore the minima in (1) are phi(A)-B and [phi(M)-N]/L.
If u+v+2>0 and 0<=u<=3/2, their sign can be tested without a square-root
approximation:

    sign(phi(u)-v)=-sign((u+v)^2+4(v-u)).                (3)

This equivalence follows by squaring two positive quantities. Clipping the
minimizer at r=0 is necessary; blindly continuing its interior formula is wrong.

## 2. A unique suffix boundary at score one half

Set a=1/2-d, L=3/2-d,0<d<=1/5, and

    D=(1-d^2)(2-d^2), q=1-2d^2,
    A=4d/D, B=Aq/L,
    w=log[(2-d^2)/(2(1-d^2))], M=LA+2w, N=Aq,
    Z=M+N, H=Z^2+4(N-M).                               (4)

Here 0<M<3/2. The suffix derivative is negative exactly when H>0.
Also w'=A/2, so M'=LA', N'=q A'-4dA and

    Z'=(5/2-d-2d^2)A'-4dA,
    Z''=(5/2-d-2d^2)A''-(1+8d)A'-4A.                  (5)

The following rational bounds prove strict convexity on the entire interval,
not only at sampled points:

    2<=A'<=2+10d^2<=12/5,
    18d<=A''<=22d,
    2d<=A<=2d+4d^3<=54/125,
    Z'>=2559/625, Z''>=-2,
    0<=Z<=673/600,
    N''-M''>=-671/125.

For detail, write z=d^2<=1/25. Then D=2-3z+z^2>=47/25,
A'=4(2+3z-3z^2)/D^2 and
A''=8d(18-11z-9z^2+6z^3)/D^3. Clearing positive denominators, the
lower/upper A' bounds reduce respectively to

    36z-38z^2+12z^3-2z^4>=0,
    2z(2-41z+59z^2-29z^3+5z^4)>=0.

The lower A'' bound reduces to
z(560-1260z+1182z^2-594z^3+162z^4-18z^5)>=0.
The upper bound follows from numerator/d<=144 and144/(47/25)^3<22.
The A upper bound reduces to2z(1-5z+2z^2)>=0. Each displayed polynomial
is nonnegative by dropping its positive terms and bounding negative powers
at1/25. These are exact interval bounds.

Equation (5) now gives Z''>=-2+21d-28d^2-132d^3>=-2;
Z' >=(111/50)*2-4*(1/5)*(54/125)=2559/625.
Since w<=d^2/[2(1-d^2)]<=1/48, Z<=27/25+1/24.
Finally q-L=d-1/2-2d^2>=-1/2 and1-8d>=-3/5 give
N''-M''=(q-L)A''+(1-8d)A'-4A>=-671/125.
It follows that

    H''=2(Z')^2+2ZZ''+4(N''-M'')
       >=2(2559/625)^2-4(673/600)-2684/125 >7.           (6)

At0, H=0 and H'=-4. Exact logarithm bounds give H(4/25)<0 and H(17/100)>0:
use x=d^2/[2(1-d^2)], x-x^2/2<=w<=x. H decreases as M increases since
partial_M H=2Z-4<0. Thus the lower w bound certifies the first upper sign,
and the upper w bound certifies the second lower sign. Strict convexity,
H'(0)<0 and these signs imply exactly one positive root d_* in(4/25,17/100),
with H<0 before it and H>0 after it throughout(0,1/5].

This is an exact implicit characterization of the first suffix directional
instability. At d=d_* the minimum first derivative is zero; this argument
alone makes no second-order claim; section 3a closes that local equality case.

## 3. Prefix directions do not cause that onset

In the same interval A<3/2. The sign of (A+B)^2+4(B-A) is the sign of

    R(d)=-6+41d-43d^2-44d^3+61d^4-16d^6+8d^7.

For0<=d<=17/100 the cubic/quartic and sixth/seventh pairs are nonpositive.
The remaining quadratic is increasing and at17/100 equals-2727/10000.
Thus R<0 and every prefix direction has a strictly positive first derivative
for0<d<=17/100. Combined with section2, suffix is the first strictly negative
single-satellite direction among both orders on this interval. No statement
about coordinated satellite collections or the global optimizer is implied.

At a=1/3,d=1/6 one can see the difference exactly:
A=864/2485,B=612/2485 and the prefix sign polynomial is
-326304/6175225. But the suffix choice r=3/7 gives

    g(r)+Mr-N=-268/17395+(6/7)log(71/70)
             <-11/3479,
    suffix derivative <-33/13916.                      (7)

A prefix-only stability test would miss this genuine improvement direction.

## 3a. Equality at the boundary is locally stable

Write u=a+b, v=b-a and W(u,v)=log[(2u(2-u)+v^2)/(2u(2-u))].
At the one-stage point u=1-d,v=d put D2=2(1-d^2), N2=2-d^2.
For a suffix of score t and ratio r, set k=rL. Direct differentiation of

    C(t)=2/L [(1+rt)w((a-rt)/(1+rt),1/2-t)+w(rt,t)]

gives the coefficient of t^2 as B2/L, where

    B2=(1+k)^2 W_uu+2(1-k^2)W_uv+(1-k)^2 W_vv
       -2r w_b+(1-r)^2/4-(1-r)^4/[16(1+r)^2],
    W_uu=4d^2/(N2 D2)+16d^2(1/D2^2-1/N2^2),
    W_uv=-8d^2/N2^2, W_vv=2/N2-4d^2/N2^2,
    w_b=2d(1-2d^2)/[(1-d^2)(2-d^2)].

The chain-rule w_a contributions cancel. On the entire rational box
4/25<=d<=17/100,2/5<=r<=9/20, we have

    1/2<k<61/100, W_uu>=d^2>=16/625,
    |W_uv|<3/50, W_vv>97/100, 0<w_b<9/50,
    (1-r)^2/4-(1-r)^4/[16(1+r)^2]
       >=121/1600-81/19600>7/100.

These follow from 0<D2<N2<=2 and the interval endpoints; in particular
W_vv>=1-4(17/100)^2/[2-(17/100)^2]^2>97/100.
It follows, with the signs of each summand respected, that

    B2>(9/4)(16/625)-(3/2)(3/50)+(39/100)^2(97/100)
        -2(9/20)(9/50)+7/100
      =23137/1000000>1/50,
    B2/L>1/67.                                         (7a)

The unique zero-derivative ratio r_*(M(d_*)) is strictly inside this box:
A>=2d and 2w>=d^2 give M>=3d-d^2>=284/625>759/1682;
A<9/25, L<27/20 and 2w<3/100 give M<129/250<51/98.
Substitution into (2) yields 2/5<r_*<9/20. The logarithm lower bound
2w>=d^2 also follows by integrating w'=A/2>=d from zero.

At d=d_*, all suffix first derivatives are nonnegative with exactly this
one zero. On a closed neighborhood of r_* within the box, (7a) and the
uniform Taylor remainder imply positive cost change for sufficiently small
t>0. On the complementary compact ratio set the first derivative has a
strictly positive minimum, which controls the uniform remainder there.
The smooth extension of w(rt,t) at t=0 is uniform for r in[0,1]. Prefix
first derivatives have a positive compact minimum by section3. Hence there
exists one t0>0 such that every feasible single prefix or suffix with
0<t<t0 strictly increases cost, uniformly over all r in[0,1], at d=d_*.
The same argument gives a uniform small-satellite stability neighborhood
on the pre-onset side. It does not exclude remote finite satellites,
coordinated collections, or global competitors, and gives no explicit t0.

## 3b. The improving branch and its quadratic advantage after onset

The equality certificate also determines a useful local policy, not merely
a sign. Write d0=d_*, r0=r_*(M(d0)), L0=L(d0), M0=M(d0), and

    Delta(d,t,r)=C_suffix(d,t,r)-C_single(d),
    D1(d,r)=[g(r)+M(d)r-N(d)]/L(d), beta(d,r)=B2(d,r)/L(d).

The smooth extension at t=0 gives, uniformly nearby,
Delta=t D1+t^2 beta+O(t^3). At(d0,r0), D1=partial_r D1=0,

    gamma=partial_rr D1=g''(r0)/L0>0, beta0=beta(d0,r0)>1/67,
    partial_d D1=-alpha,
    alpha=H'(d0)/[4L0 sqrt(1+2M0)]>0.                 (7b)

To see the last identity, rationalize the minimized first derivative as
-H/[L(2sqrt(1+2M)+M+N+2)]; its denominator at the root is
4L0 sqrt(1+2M0). Strict convexity of H and its two roots imply H'(d0)>0.
The optimizer's ratio derivative contributes zero by stationarity.

The stationary equations (partial_t Delta,partial_r Delta/t) extend smoothly
at t=0. Their Jacobian in(t,r) at(d0,0,r0) is

    [[2 beta0, 0], [partial_r beta(d0,r0), gamma]],

which is invertible. The implicit function theorem gives a unique local
stationary branch. For delta=d-d0>0 small it satisfies

    t_opt=alpha delta/(2 beta0)+O(delta^2)>0,
    r_opt=r0+O(delta),
    Delta_opt=-Gamma delta^2+O(delta^3),
    Gamma=alpha^2/(4 beta0)>0.                         (7c)

Its Hessian has tt entry tending to2 beta0 and rr entry gamma t_opt+O(t_opt^2),
while the cross entry is O(t_opt). Hence it is a strict local minimum among
nearby suffix policies at the same exact success p(d)=1/L(d). Feasibility is
strict for small delta. This is not a global two-stage optimizer. Alternatively,
fixing r=r0 and taking t=alpha delta/(2 beta0) already realizes the same leading
improvement, without needing to optimize the ratio.

This yields a same-budget comparison with all one-stage mixtures. Put
K0=C_single(d0), kappa=K-K0>0. Since

    C_single(d)=2w(d)/L(d), C_single'(d)=M(d)/L(d)^2>0,
    p'(d)=1/L(d)^2,

the improving branch's cost can be locally inverted to hit K exactly. If
f_one(K) is the original one-stage-mixture optimum, K2493's convexity gives
the inverse single-stage curve in this interior neighborhood. The branch's
actual success obeys

    P_branch(K)-f_one(K)
      =[Gamma L0^4/M0^3] kappa^2+O(kappa^3)>0.         (7d)

Indeed the cost gain Gamma delta^2 permits an extra d of
Gamma delta^2/C_single'(d0), and delta=kappa/C_single'(d0)+O(kappa^2).
Thus F_all(K)>=P_branch(K) gives a quantitative quadratic lower separation
immediately above K0. This is a constructed-policy expansion, not an expansion
of F_all, a global transition theorem, or a result at K=1/1000.

## 4. Released finite policy and all-one-stage-mixture gap

Take in this order

    main: (a,b)=(691/2109,49/100),
    suffix: (a,b)=(3/700,1/100).                         (8)

Their total score is1/2 and exact success is3/4. For x>=0,
log(1+x)<=x-x^2/2+x^3/3; the integral remainder has the correct sign.
Applying this upper bound to both original logarithmic stages and their exact
survival weights gives

    C_policy <2127/100000=:K.

The one-stage policy of the same success has

    C_single=(3/2)log(71/70)
            >=417/19600=K+27/4900000.                 (9)

The probe performs these comparisons entirely with rational arithmetic.
K2493 proves the original one-stage cost as a function of success is convex
above p0=2/3. Extend it by0 on[0,p0]; the extension stays convex. Jensen
therefore bounds every mixture of one-stage policies and free abandonment
by this same cost-success curve. No rare costly mixture can evade (9).

Its derivative at p=3/4 is

    C_single'(3/4)=2log(71/70)+1152/2485 <1/2.

Since the derivative is increasing, for p<=3/4 the cost increment from p to
3/4 is at most(3/4-p)/2. Monotonicity excludes p>=3/4 at budget K.
Consequently

    F_one-stage-mixtures(K)<=3/4-27/2450000
       <3/4<=F_all-original-policies(K).               (10)

For p below baseline the same success bound is automatic. This is an explicit
strict separation at the stated budget, not a sharp global value or optimum
for two stages. In particular it says nothing new about K=1/1000.

## 5. Verification and remaining question

Exact derivatives, rational interval bounds on H'', logarithm-root brackets,
the exact second-order chain identity and uniform boundary stability,
original two-stage costs and survival products support the written universal
proof. Contrary controls include wrong insertion order, unclipped minimizer,
omitted survival weights and extrapolation from first-order stability to
finite/global optimality. Finite fixture counts are coverage, not theorem counts.
K2485 finite-mixture/adaptive reduction, K2493 convexity and K2501 local optimum
are reused at their original scope, not rerun as new evidence.

Next: certify the first global loss of one-stage optimality, including finite
satellites, mixtures and all-stage competitors. Equality at the local boundary
is now stable against uniformly small single satellites. The directional root is an upper obstruction
for any claimed one-stage regime, not a proof of its lower endpoint.


[Exact probe](../../tests/channel-swings/k2503_stopping_instability_boundary_probe.py) and [saved report](../../lab/process/k2503-stopping-instability-boundary.json).
