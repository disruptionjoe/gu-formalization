---
title: "K2495 Optimal stage ordering and an exactly solved microstage limit"
status: active_research
doc_type: exploration
created: "2026-11-02"
classification: CONVENTIONAL_COMPARATOR
target_claim: "NONE-NOT-A-KILL"
claim_ceiling: "conditional original-law scheduling mathematics; continuum optimum is not the unrestricted optimum"
---

# K2495 Optimal stage ordering and an exactly solved microstage limit

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
result: K2495
carrier: original fresh fair test/use absorbing experiment with failure-inclusive one-sided leakage cost LAYER=toy CHIRALITY=N/A
pairing: positive trace or actual-law expectation on the supplied model ON=declared_carrier
real_structure: complex adjoint for quantum states; real probability for classical histories
grading: target/complement or absorbing test/use histories
action_owner: repository-construction -- supplied conditional mathematical models
target: Stage-order theorem, exact continuum optimizer and finite-schedule approximation boundary MAP-TYPE=evaluation
```

## Result and scope

The original stopping law has an exact optimal ordering for any fixed set of
stages. It strictly improves the K2493 witness. The infinitesimal-stage limit
also admits a unique globally optimal control with a closed parametric cost
and an explicit finite-schedule approximation at unchanged success and score.
An exact counterexample proves that this continuum solution is not the
unrestricted original optimum: finite free stages can do strictly better.

The fresh fair routing, positive probabilities, one-sided leakage cost and
unbounded geometric trial support are supplied assumptions. SC-META-53 remains
UNCERTAIN; ledger0.263 LT-SM8/LT-GR6b keep their native quotient/domain debts.
No source, ledger, canon, physical credit, calibrated implementation or novelty
claim changes. K2485's mixture reduction and K2491's all-policy upper bounds
remain valid and separate from the restricted continuum calculation here.

## 1. Exact exchange and fixed-multiset optimal order

Throughout, 0<S<=1/2; the trivial zero-score case is omitted.

For 0<=a<=b<=S<=1/2, excluding idle a=b=0, write

    w(a,b)=log(1+(b-a)^2/[2(a+b)(2-a-b)]),
    P_i=product_{j<=i}(1+a_j)^(-1),
    C=sum_i 2 P_i w(a_i,b_i),   P=P_n.

Cost includes failed paths. A successful schedule has total b_i=S; these
positive stages reach S only at the end, so permuting them does not change
the target stopping location. For two adjacent stages after survival q,

    C_ij-C_ji=2q(a_j w_i-a_i w_j)/[(1+a_i)(1+a_j)].       (1)

Their product survival and the entire suffix cost are unchanged. Repeated
adjacent exchanges therefore minimize cost over every permutation by sorting
in increasing index w_i/a_i. Give a=0,b>0 index infinity, free a=b>0 index0,
and remove idle stages. Ties give equal cost. This does not select stage
parameters, establish finite attainment, or order arbitrary adaptive controls.

The equal-success merge, when admissible, has

    a_M=a_i+a_j+a_i a_j, b_M=b_i+b_j.

It is allowed only if a_M<=b_M, and improves the displayed order exactly if
w(a_M,b_M)<(1+a_j)w_i+w_j. Equation (1) supplies no universal merge inequality;
K2493 already disproves the global one-stage shortcut.

## 2. A strict finite improvement over K2493

Reverse K2493's two stages:

    (a_1,b_1)=(59/201,49/100), (a_2,b_2)=(1/200,1/100).

Score is still1/2 and success still10/13. Put x=15594601/770157598 and
z=1/2382. The new actual-law cost is

    C_rev=(201/130)log(1+x)+(20/13)log(1+z).

The old tiny prefix has larger index: 200log(1+z)>(201/59)log(1+x).
The bounds z-z^2/2<=log(1+z) and log(1+x)<=x give

    C_old-C_rev >=964434753491869/28545820923554510940
                 >1/30000.

Cubic logarithm upper bounds additionally certify C_rev<633/20000=0.03165.
K2493's single-stage lower cost475/14976 still exceeds this budget. Its same
convexity/tangent argument yields the stronger explicit separation

    F_single-stage-mixtures(633/20000)
       <=10/13 - (5/3)(475/14976-633/20000)
       <10/13 <=F_full(633/20000).

Neither this result nor correct ordering proves that two stages are optimal.

## 3. State the restricted continuum problem separately

Let score t run from0 to S. For infinitesimal stages b=dt,a=r(t)dt, define
R'=r, R(0)=0, R(S)=H, and0<=r<=1. The survival is y=e^(-R), target success
e^(-H), and the limiting cost is

    J=integral_0^S e^(-R(t)) g(r(t)) dt,
    g(r)=(1-r)^2/[2(1+r)].                              (2)

This is a distinct variational problem with0<=H<=S. Finite n-stage schedules
have max log-survival loss n log(1+S/n)<S. No finite-stage equality at H=S
is inferred. The continuum's range must not be confused with the single-stage
bound log(1+S), or with a limit of the full optimization that permits finite
atoms. Section6 explicitly separates those problems.

## 4. Unique global continuum optimizer, including the boundary arc

For0<H<S choose r0 in(0,1), follow

    r'=-(1-r)(1+r)(1+3r)/8,                             (3)

and hold r=0 if it reaches zero before S. Choose r0 so the integral of r is H.
Scalar ODE order preservation and continuity make this integral a strictly
increasing continuous function of r0, from0 to S; hence exactly one r0 works.
At H=0 the only feasible control is r=0, J=S/2; at H=S it is r=1, J=0.

Here is a global proof rather than an Euler-equation guess. In y coordinates,

    J=integral y g(-y'/y) dt,
    y(0)=1, y(S)=e^(-H), -y<=y'<=0.

The feasible set is convex and y>=e^(-H)>0. Because g''=4/(1+r)^3>0,
the integrand is a convex perspective. Equation (3) satisfies the Euler
identity on the interior. On a terminal r=0 arc, y=e^(-H), the first variation
after integration by parts is (1/2)integral delta-y dt>=0: every feasible
decreasing path with the same endpoint lies above e^(-H). Momentum -g'(r)
is continuous at r=0, so no junction boundary term is omitted. Convexity then
gives global optimality against every absolutely continuous feasible y.
Equality in perspective convexity forces identical r almost everywhere;
y(0)=1 then forces identical y. This proves uniqueness. Piecewise smooth
candidate plus bounded gradients justifies the same first-variation inequality
for absolutely continuous competitors; smoothness of the competitor is not
assumed.

Define

    Q(r)=(1-r)(1+3r)/[2(1+r)^2],
    F(r)=-log(1-r)-2log(1+r)+3log(1+3r).

Let rT be the terminal interior ratio, or zero when a terminal zero arc of
length ell is present. Conservation of e^(-R)Q(r) and integration of (3) give

    S=F(r0)-F(rT)+ell,
    H=log[Q(rT)/Q(r0)],   ell>=0,   ell*rT=0,
    J=(8Q(r0)/3)[1/(1+3rT)-1/(1+3r0)]+e^(-H)ell/2.    (4)

For example r0=1/2,rT=2/5,ell=0 gives exactly

    S=log(6125/3993)<1/2, H=log(297/245),
    P=245/297, J=4/99.

The probe certifies the bound on S using a rational cubic upper bound for
log(1+2132/3993), and checks every derivative/conservation identity. A second
fixture at rT=0,ell=1/10 checks the nonempty boundary arc; it is not silently
continued to a negative inadmissible r.

## 5. Exact-success finite approximation and its error budget

For H<S, split into n equal score intervals of length Delta=S/n with
Delta<=min(1/2,1-r0). Let rho_i be the interval mean of the optimizer r and set

    b_i=Delta, a_i=exp(rho_i Delta)-1.

These obey0<=a_i<=b_i, sum b_i=S and product(1+a_i)=exp(H) exactly. For the
upper bound on a_i, log(1+Delta)>=Delta-Delta^2/2>=r0 Delta.
No rounded-control or rationality assumption enters this existence theorem;
implementing a numerical policy requires separately certified integrals and
exponentials or a controlled constraint repair.

A useful uniform elementary bound for0<=q<=1,0<=b<=1/2 is

    0<=2w(qb,b)-b g(q)<=b^2/2.                         (5)

To prove it, set h=g(q)/2, z=(1+q)b/2 and x=bh/(1-z). Since z>=bh,
log(1+x)>=x/(1+x)>=bh. Using log(1+x)<=x, the upper error is at most
b^2 h(1+q)/(1-z)<=b^2/[4(1-b)]<=b^2/2. The b=0 case is by continuity.

Equation (3) has |r'|<=1/2, while |g'|<=3/2 and0<=g<=1/2. Also
|a_i/Delta-rho_i|<=Delta from the exponential remainder at Delta<=1/2.
Thus |a_i/Delta-r(t)|<=3Delta/2 on an interval. Stage survival P_i is exactly
y(t_i); |y(t_i)-y(t)|<=Delta. Applying (5), the cost difference per interval
is at most Delta^2/2+(9/4)Delta^2+Delta^2/2. Therefore

    |C_n-J| <=(13/4)S Delta =13S^2/(4n).               (6)

This is an explicit approximation with the same score and success. It is not
an all-policy upper bound or a proof that the original optimum is attained.

## 6. Why solving the continuum does not solve the original frontier

At H=log(1+S), the original one-stage policy a=b=S costs exactly zero.
For the continuum, R<=H and Jensen give

    J>=e^(-H) S g(H/S)>0,

because0<log(1+S)<S. Thus even the exact continuum optimizer is strictly worse.
More generally, finite all-free schedules attain every H in
[log(1+S),S): on the n-stage score simplex, sum log(1+b_i) varies continuously
from log(1+S) to n log(1+S/n), whose upper endpoint tends to S. Zero stages
are discarded. A continuum-only calculation can therefore miss an entire
free region of the original problem. This settles a possible shortcut and
points to a combined finite-stage and continuum description or an original-law
Bellman certificate; it does not invalidate the exact continuum theorem.

## Evidence and next work

Exact rational and symbolic probes authenticate exchange, finite separation,
Euler/convexity/conservation and parametric identities, boundary fixtures and
uniform approximation inequalities. Finite-control counts are coverage, not
independent theorems; universal proofs are above. Independent probability
review derived and challenged the structural candidates, with separate lead
integration review. No external-expert or proof-assistant certification.

Next: determine how finite stages couple to optimized small-stage intervals,
or construct an original-law Bellman certificate using the ordering constraint.
The exact continuum solution provides a useful restricted optimizer and a
known limitation, not the global answer. Native matter/light, physical quotient
and full ordinary mixed-hook inverse remain distinct open constructions.

[Probe](../../tests/channel-swings/k2495_stopping_order_and_continuum_probe.py),
[report](../../lab/process/k2495-stopping-order-and-continuum.json),
[prior finite separation](k2493-stopping-stage-splitting-2026-11-02.md),
[original constrained frontier](k2485-constrained-stopping-frontier-2026-11-01.md).

Convex-perspective sufficiency is standard; see
[Boyd and Vandenberghe, Convex Optimization](https://stanford.edu/~boyd/cvxbook/).
The present derivation makes no novelty claim for that method.
