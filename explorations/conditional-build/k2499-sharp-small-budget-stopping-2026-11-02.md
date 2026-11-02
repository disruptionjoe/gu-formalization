---
title: "K2499 The sharp original small-budget stopping frontier"
status: active_research
doc_type: exploration
created: "2026-11-02"
classification: CONVENTIONAL_COMPARATOR
target_claim: "NONE-NOT-A-KILL"
claim_ceiling: "conditional supplied-model mathematics; no measured calibration, global finite-budget optimum or native GU realization"
---

# K2499 The sharp original small-budget stopping frontier

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
result: K2499
carrier: original fresh fair test/use absorbing experiment, fixed score S in (0,1/2] LAYER=toy CHIRALITY=N/A
pairing: expectation including failed and abandoned histories ON=declared_carrier
real_structure: real probabilities and controls
grading: finite use schedules, mixtures and arbitrary adaptive trial histories
action_owner: repository-construction -- supplied positive quantum or classical probability model
target: uniform small-budget coefficient and finite-budget envelope MAP-TYPE=evaluation
```

## Result and scope

For every fixed 0<S<=1/2, the full original adaptive success frontier satisfies

    F_S(K)=p0+c_S sqrt(K)+O_S(K),    K down to0,
    p0=1/(1+S), c_S=2 sqrt(S(1-S))/(1+S)^(3/2).          (1)

The coefficient is sharp over all original adaptive policies, not merely a
fixed number of stages. One nearly free stage attains the leading coefficient.
This does not assert exact one-stage optimality for any positive budget, nor
a uniform limit as S changes. K2493's finite-budget strict multistage advantage
and K2495's continuum-versus-atom distinction survive.

The supplied fresh fair test/use law and failure-inclusive one-sided leakage
are those of K2483/K2485. This is independent conditional mathematics.
SC-META-53 remains UNCERTAIN and LT-SM8/LT-GR6b retain their physical-state,
quotient and domain debts. Ledger0.263, canon and physical credit are unchanged.
No hardware, external certification or literature novelty is claimed.

## 1. A uniform finite-schedule estimate

By K2485's exact constrained reduction, it is enough eventually to bound finite
mixtures of finite schedules, including free abandonment. A completed schedule
has controls 0<=a_i<=b_i, sum b_i=S; overshoots can be clipped and a>b dominated
as in K2485. Its success and original expected cost are

    p=product_i(1+a_i)^(-1),
    C=sum_i 2 P_i w(a_i,b_i), P_i=product_{j<=i}(1+a_j)^(-1),
    w=log(1+(b-a)^2/[2(a+b)(2-a-b)]).

Idle stages are removed. Set d_i=b_i-a_i,u_i=a_i+b_i,D=sum d_i,A=S-D,
M=1/p, E=M-1-A. Nonnegative product expansion gives E>=0. When p>p0,

    delta=1+S-M=D-E>0, so 0<=E<D.                        (2)

Write H_i=2u_i(2-u_i)+d_i^2 and T=sum H_i. The logarithm inequality and
weighted Cauchy-Schwarz imply

    C>=2p sum_i d_i^2/H_i >=2p D^2/T.                   (3)

Zero d_i terms cause no problem; H_i>0 for nonidle stages in this domain.
A separate coarse bound, w>=d_i^2/(4u_i), gives

    C>=p D^2/(4S)>=p0 D^2/(4S),
    D<=B(C)=2 sqrt(S C/p0).                             (4)

For the sharp denominator, product expansion yields

    sum_i a_i^2=A^2-2 sum_{i<j}a_i a_j >= A^2-2E >= A^2-2D.

Since sum u_i=2S-D, sum u_i^2>=4 sum a_i^2 and sum d_i^2<=D^2,

    T=4(2S-D)-2 sum u_i^2+sum d_i^2
      <=8S(1-S)+(16S+12)D-7D^2
      <=T0+T1D,
    T0=8S(1-S), T1=16S+12.                             (5)

Finally p-p0=p p0 delta<=p p0 D and p<=1/(1+S-D).
Combining (3)--(5), whenever B(C)<1+S,

    (p-p0)^2/C <= R_S(C),
    R_S(C)=p0^2 [T0+T1 B(C)]/[2(1+S-B(C))].             (6)

This upper bound is uniform over stage number and order. It tends to
T0/[2(1+S)^3]=c_S^2. C=0 is the separate free baseline case. Schedules below
baseline need no estimate on their negative gain.

## 2. A global envelope and the full adaptive frontier

Set

    C0=(1+S)/(16S),
    L=p0[T1+p0 T0]/[2 sqrt(1-S)],
    Lstar=max(L,(1-p0)/C0).

For C<=C0, p0 B(C)<=1/2. Direct subtraction from (6) gives

    R_S(C)-c_S^2
      =p0^3 [T1+p0 T0] B(C)/[2(1-p0 B(C))]
      <=p0^3 [T1+p0 T0] B(C).

Using sqrt(c^2+x)<=c+x/(2c), (6) yields

    p-p0<=c_S sqrt(C)+L C.

For C>C0, p-p0<=1-p0<=Lstar C. Below-baseline schedules and free
abandonment satisfy the upper bound automatically. Thus every finite schedule
has the same global, stage-count-independent envelope

    p<=p0+c_S sqrt(C)+Lstar C.                           (7)

For any finite mixture with expected cost<=K, weighted Cauchy or concavity of
the square root gives

    F_S(K)<=min(1,p0+c_S sqrt(K)+Lstar K).                (8)

K2485 supplies equality of the original frontier and the finite-mixture
supremum with *no budget relaxation*, so (8) covers abandoned and infinite
adaptive trial histories as well. We do not claim every adaptive path itself
has the schedule normal form. In particular, rare high-cost mixture components
cannot change the leading coefficient. They are controlled by the linear tail
term in (7), not silently discarded.

The envelope is constructive but coarse at positive budgets: K2491 can remain
tighter at its specific budget. For a rational convenient coefficient at
S=1/2, c_S<11/20 and Lstar<13, proved by squaring rational quantities. Hence
F_(1/2)(K)<=min(1,2/3+(11/20)sqrt(K)+13K). The exact coefficient in (1),
not this rounded consumer, is the sharp asymptotic.

## 3. Matching original-law witness

Take one stage b=S,a=S-d with 0<d<S. Then

    p(d)=1/(1+S-d),
    C(d)=2/(1+S-d) log(1+d^2/[2(2S-d)(2-2S+d)]),
    p(d)-p0=d/(1+S)^2+O_S(d^2),
    C(d)=d^2/[4S(1-S)(1+S)]+O_S(d^3).                 (9)

Near d=0 the derivative of C(d) is positive, since its leading coefficient
is positive. Thus for every sufficiently small K>0 there is a unique local
d(K)>0 with C(d(K))=K. This is an actual feasible policy, not a relaxed cost.
Equation (9) proves liminf>=c_S and the lower bound
F_S(K)>=p0+c_S sqrt(K)+O_S(K). Together with (8), (1) follows with an absolute O_S(K) remainder. Uniformity as
S tends to0 or beyond the declared interval is not asserted.

At S=1/2, c_S^2=8/27. K2497's analytic upper-bound coefficient squared is
16/27, so its leading constant is larger by sqrt(2). The former bound stays
valid; its apparent leading allowance is not attainable. Numerical refinement
is unnecessary to settle this leading-order question.

## 4. Released concentration consequence

For any sequence of completed finite schedules with C tending to0 and p>p0,
(4) gives D tending to0, while E<D. If a_max=max a_i, then

    a_max A>=sum a_i^2>=A^2-2D,
    A-a_max<=2D/A,  when A>0.                          (10)

Since A tends to S>0, one hazard atom carries all but O_S(sqrt(C)) of total
hazard. The total score outside that same stage is at most 2D/A+D, also
O_S(sqrt(C)). This is uniform even if the number of stages diverges. It
explains why a purely infinitesimal-stage description cannot determine the
sharp zero-budget behavior. It does not exclude small costly satellites,
prove their optimal placement, or constrain every component of every mixture.
The rare expensive mixture components were handled separately in (7).

## 5. Released local test: small satellites in either order

The concentration theorem suggests testing a small second stage directly.
Fix 0<a<S and insert (rt,t), 0<=r<=1, while replacing the main stage by
((a-rt)/(1+rt),S-t). Either order preserves score S and success1/(1+a),
and is feasible for all sufficiently small positive t, uniformly in r.
Let w=w(a,S), A=-2 partial_a w(a,S), B=2 partial_b w(a,S)/(1+a), and

    g(r)=(1-r)^2/[2(1+r)].

The derivative at t=0 of total original expected cost is

    prefix: g(r)+Ar-B,
    suffix: [g(r)+At r-Bt]/(1+a),
    At=(1+a)A+2w, Bt=(1+a)B.                            (11)

This follows by differentiating the exact two-stage cost, including its
survival weights; w(rt,t)=t g(r)/2+O(t^2). Use g(r)>=(1-r)^2/4 and
min over real r of (1-r)^2/4+Ar=A-A^2. Thus prefix derivative is at least
A-B-A^2. Put x=(S-a)^2/[2(S+a)(2-S-a)]. Since x/(1+x)<=w<=x,

    Atlo=(1+a)A+2x/(1+x), Athi=(1+a)A+2x,
    suffix derivative >=[Atlo-Bt-Athi^2]/(1+a).          (12)

Here A,Atlo,Athi are nonnegative in the declared domain. These rational
sufficient certificates are positive for S=1/2 at a=2309/5000 and at
a=499/1000. At the latter both exceed1/2000, uniformly for all r in[0,1].
Continuity on this compact interval gives a common positive t-neighborhood:
no sufficiently small satellite of either order improves those fixed policies
at unchanged success. This closes both insertion directions at these witnesses,
not all finite alternatives.

More generally set a=S-d. The rational lower certificates and evaluation of
(11) at r=1 give, for either order,

    min_r derivative = kappa d+O_S(d^2),
    kappa=1/[2(1-S)(1+S)]>0.

The exact logarithmic cost expressions have a smooth extension at t=0,
uniform in r: the small-stage logarithm is
log(1+(1-r)^2 t/[2(1+r)(2-(1+r)t)]). Taylor expansion therefore gives
min_r excess cost=kappa d t+O_S(t d^2+t^2) on feasible small insertions.
For t=tau d^2 with fixed tau>0, the excess is kappa tau d^3+O_{S,tau}(d^4)>0.
This rules out a natural candidate for changing the order-K frontier term.
It does not control arbitrary t/d^2, finite remote changes, or coordinated
families of many satellites. No exact positive-budget optimum is established.

## 6. Controls, evidence and unresolved question

The exact probe checks denominator identities, product-excess and concentration
inequalities on explicit many-stage schedules, rational lower certificates for
(3), symbolic expansions in (9), the leading constant and a valid finite-budget
use of (7). It tests failed-path cost, omission of the expensive-component tail, wrong leading
constant, and the high-success premise with actual contrary examples.
Universal schedule uniformity, mixture passage and limiting statements rely on
the proofs above and independent review, not a finite numerical grid.

The next substantial target is the subleading role of costly satellites or a
mixed finite-atom/continuum Bellman certificate away from zero. The asymptotic
alone supplies neither exact finite-budget one-stage optimality nor the global
fixed-confidence coefficient. The geometric and native physical alternatives
remain separate open constructions.


[Exact probe](../../tests/channel-swings/k2499_sharp_small_budget_stopping_probe.py)
and [saved report](../../lab/process/k2499-sharp-small-budget-stopping.json).
