---
title: "K2517 Sharp small-score stopping transition and a finite policy separation"
status: active_research
doc_type: exploration
created: "2026-11-02"
classification: CONVENTIONAL_COMPARATOR
target_claim: "NONE-NOT-A-KILL"
claim_ceiling: "conditional original-law probability theorem; asymptotic transition, not a fixed-score global phase boundary or GU result"
---

# K2517 Sharp small-score stopping transition and a finite policy separation

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
result: K2517
carrier: original finite/adaptive fresh fair test-use schedules with total score S LAYER=toy CHIRALITY=N/A
pairing: original failure-inclusive probability cost ON=declared_carrier
real_structure: real probabilities and logarithmic cost
grading: ordered finite stages, initial mixtures and admitted limits
action_owner: repository-construction -- supplied original stochastic law
target: uniform second-order value asymptotic and exact finite two-stage superiority MAP-TYPE=evaluation
```

## Result and scope

The original stopping law has a sharp **second-order small-score aggregation/diffusion transition** at lambda_star=4sqrt(3)/3. Below it, finite two-stage policies beat the actual best one-stage policy for all sufficiently small positive scores. A fully rational schedule at lambda=128/57 and S=1/100000 proves this with an explicit positive gap. Above it, one stage attains the optimal second-order coefficient; this does not prove its exact optimality at finite score. At equality, every fixed nondegenerate two-stage split loses to the optimized one-stage policy at cubic order, while degenerating splits and general multistage equality remain open.

This replaces a proof-domain obstruction with an actual original-law policy separation and an all-policy asymptotic theorem. K2515's uniform lambda>=8/3 certificate and S=1/2 budget<=1/90 theorem remain valid. No new exact S=1/2 transition or budget frontier is claimed. SC-META-53 remains UNCERTAIN; source polarities, ledger0.263, canon and native physical-state/domain debts remain unchanged. The result is GU-independent supplied-model probability mathematics, without novelty, hardware, external-expert or proof-assistant certification.

## 1. Original model and scope of the supremum

For 0<=a<=b let

    w(a,b)=log(1+(b-a)^2/[2(a+b)(2-a-b)]), w(0,0)=0.

For a finite completed schedule, b_i>=0, sum b_i=S, 0<=a_i<=b_i,

    P_i=product_(j<=i)(1+a_j)^(-1), p=P_n,
    C=2sum_i P_i w(a_i,b_i), G_lambda=p-lambda C.

Write V_lambda(S)=sup G_lambda over the original policies. The exact finite-completed-schedule, initial-mixture and limiting-schedule reduction of K2483/K2485 is reused: adaptive decisions, free stages, clipping and abandonment do not add a value beyond that reduction. The theorem below is first proved uniformly for every finite completed schedule, without a stage-count cap. Linear mixtures and the admitted limits preserve its upper bound. It makes no claim for a modified cost law or unmodeled feedback.

For lambda>1 define

    r=2/sqrt(1+2/lambda)-1 in(0,1),
    A=(3r+1)/(r+3),
    H=(3r+1)(r²+6r-3)/[8(r+3)],
    B_star=rA/2+max(H,0).                              (1)

Then, uniformly over the policy supremum,

    V_lambda(S)=1-A S+B_star S²+O_lambda(S³).           (2)

The following proof supplies explicit constants for 0<S<=1/4, so the notation does not hide a nonuniform stage or policy limit.

## 2. Uniform original-law expansion

Set a_i=r_i b_i, r_i in[0,1], and define

    alpha(r)=(1-r)^2/[4(1+r)], beta(r)=(1+r)/2,
    g=2alpha, q=alpha beta-alpha²/2, f=r+lambda g,
    A_i=sum_(j<=i) r_j b_j.

The letter A_i is a cumulative action; A in(1) is the scalar f(r). They are distinct. For b<=1/4,

    w(rb,b)=alpha b+q b²+R_w, |R_w|<=b³/2.            (3)

Indeed x=alpha b/(1-beta b), with alpha<=1/4,beta<=1 and x<=b/3. The geometric-series remainder in x is <=b³/3. The replacement of x²/2 by alpha²b²/2 costs <=b³/9. The logarithm remainder |log(1+x)-x+x²/2|<=x³/3<=b³/81. Their sum is37b³/81<b³/2. Also 0<=q<=1/8.

Taylor-expand product_j(1+t a_j)^(-1) at t=0. Its third derivative has absolute value at most6 A_i³ for t>=0: each complete homogeneous coefficient of degree3 is bounded by A_i³, and all denominators only reduce it. Similarly the second derivative is bounded by2 A_i². Thus

    P_i=1-A_i+(A_i²+sum_(j<=i)a_j²)/2+R_i,
    |R_i|<=A_i³,
    |P_i-1+A_i|<=A_i², |P_i-1|<=A_i.

Multiplying these expansions in the original **prefix-weighted** cost gives

    G_lambda=1-sum_i b_i f(r_i)+Q+R,
    Q=A_n²/2+sum_i a_i²/2
       +lambda sum_i g(r_i)b_i A_i-2lambda sum_i q(r_i)b_i²,
    |R|<=R0 S³, R0=1+7lambda/4.                       (4)

For the cost remainder, the three contributions are bounded by
sum_i[(1/2)b_i A_i²+(1/4)b_i² A_i+b_i³]<=7S³/4, using g<=1/2, q<=1/8, P_i<=1 and (3). The success remainder is <=S³. This remains uniform with arbitrarily many stages or zero-score stages.

## 3. Optimize without assuming a common stage ratio

Direct differentiation gives g''(u)=4/(1+u)^3>=1/2 on[0,1]. The unique minimizer of f is r from(1), with f'(r)=0 and f(r)=A. Therefore

    sum_i b_i[f(r_i)-A] >=lambda E2/4,
    E1=sum_i b_i|r_i-r|, E2=sum_i b_i(r_i-r)^2,
    E1²<=S E2.                                        (5)

Let Q_common denote Q with all r_i replaced by r. Bounds |g'|<=3/2, |q'|<=17/16 yield

    |Q-Q_common|<=L S E1, L=2+33lambda/8.               (6)

The first two success terms cost at most2S E1. The g term costs at most2lambda S E1: varying g costs(3/2)S E1 and varying A_i costs(1/2)S E1. The q term costs at most(17/8)lambda S E1, since sum b_i²|r_i-r|<=S E1. The derivative bound on q follows from |alpha'|<=3/4, alpha<=1/4, beta<=1 and beta'=1/2.

Complete the square in E2, using(5):

    L S E1-lambda E2/4<=L² S³/lambda.                 (7)

For common r, exact algebra reduces the entire ordered quadratic term to

    Q_common=rA S²/2+H sum_i b_i².                     (8)

Since 0<=sum b_i²<=S², equations(4)--(8) give the all-policy upper bound

    V_lambda(S)<=1-A S+B_star S²+(R0+L²/lambda)S³.      (9)

If H>=0, the one-stage policy a=rS attains the coefficient B_star with error at mostR0 S³. If H<0, equal n-stage policies a_i=rS/n,b_i=S/n have sum b_i²=S²/n. Taking their supremum as n tends to infinity gives the same lower coefficient with error at mostR0 S³. No infinite policy is falsely claimed to attain that supremum. Thus

    1-A S+B_star S²-R0 S³ <=V_lambda(S)<=right side(9).

This proves(2) for arbitrary mixtures and allowed limits through the inherited reduction. The proof is analytic and uniform; finite numerical optimizer searches are not used.

## 4. The sharp asymptotic transition and finite two-stage consequence

The sign of H is the sign of r²+6r-3, which vanishes at r_star=2sqrt(3)-3. Since lambda=2(1+r)²/[(1-r)(r+3)] increases with r, its multiplier is lambda_star=4sqrt(3)/3.

For a single stage the same proof, with sum b_i²=S², yields

    U_lambda(S)=1-A S+B_one S²+O_lambda(S³),
    B_one=rA/2+H=(3r+1)(r²+10r-3)/[8(r+3)].            (10)

Two equal stages at fixed ratio r have coefficient B_two=rA/2+H/2. Hence for every 1<lambda<lambda_star,

    D=B_two-B_one=-H/2>0,
    G_two-U_lambda(S)>=D S²-(2R0+L²/lambda)S³.          (11)

Every 0<S<min(1/4,D/(2R0+L²/lambda)) therefore has a finite two-stage policy strictly above the **optimized** one-stage value. Initial mixtures of one-stage policies cannot evade the comparison, because each component has dual value at most U. This is an actual obstruction to a uniform-in-score one-stage theorem below lambda_star, rather than K2515's intercept1/2 proof-template limitation at18/7.

### Exact rational witness

Choose lambda=128/57,r=5/11,S=1/100000, with two identical stages

    (a_i,b_i)=(1/440000,1/200000).

Then

    A=13/19, H=-13/2299, D=13/4598,
    R0=281/57, L=214/19,
    2R0+L²/lambda=121025/1824,
    G_two-U_lambda(S)>=1910239/8828160000000000000>0.   (12)

All inputs and the guaranteed gap are rational. The remainder proof controls the exact logarithmic law, so this is not a floating-point comparison or a comparison against an unoptimized proxy. It proves a dual separation, not a newly solved constrained budget frontier at S=1/2.

For lambda>lambda_star, H>0 favors aggregation at second order; it does not rule out higher-order gains or finite-score competing policies. Equation(2) is a sharp second-order asymptotic transition, not the exact global phase diagram.

## 5. Released equality test: optimize a fixed two-stage split

At lambda_star and r_star, H=0, so the preceding quadratic test is silent. Fix theta in(0,1), write x=theta,y=1-theta and b1=xS,b2=yS, and optimize both ratios. This is a fixed split, not optimization over theta depending on S.

For reference define

    t=alpha beta²-alpha² beta+alpha³/3,
    F2=f''(r_star)=3/2+5sqrt(3)/6,
    Bprime=[d/du (u²+lambda g(u)u-2lambda q(u))]_(u=r_star)
          =1/4+7sqrt(3)/12.

Here lambda is held fixed when differentiating. The fixed-common-r cubic coefficients are

    C1=-r³-2lambda(t-rq+r²alpha),
    C2=-r³(1-2xy)-2lambda[t(1-3xy)-rq(x³+y²)
                                      +alpha r²(1-2xy)].

The ratio gradients of Q at the leading optimum are x(x Bprime+y A) and y² Bprime. Optimization adds

    [x(x Bprime+y A)²+y³ Bprime²]/(2 F2)

to C2, and Bprime²/(2F2) to C1. For every fixed split, the leading strictly convex f localizes all optimizers at(r_star,r_star). Its negative weighted Hessian in the maximization problem is nonsingular; the implicit-function theorem gives the stated optimized expansion and an O_theta(S^4) remainder.

Exact simplification yields the optimized two-stage minus one-stage cubic gap

    theta(1-theta)[c0(1-theta)+c1 theta],
    c0=(13185-7619sqrt(3))/48<0,
    c1=(2841-1643sqrt(3))/48<0.                         (13)

The signs are exact: 3*7619²-13185²=303258>0 and 3*1643²-2841²=27066>0. Thus every fixed nondegenerate split is worse for sufficiently small S at equality. No uniform conclusion as theta tends to0 or1 is licensed, and arbitrary many-stage equality remains open. This resolves the natural fixed-split successor without pretending it settles the global transition.

## Evidence and next question

The exact probe reconstructs original logarithmic coefficients, f/g/q derivatives, the common-r quadratic and ordered cubic terms, minimizer/threshold identities, all rational witness constants and algebraic signs. It checks finite prefix expansions and genuine wrong-cost, wrong-ratio, boundary and sample-only countercontrols. Universal and uniform statements rely on sections2–3; exact finite identities do not replace their proofs. Independent internal review examines both the written estimates and probes. No external or proof-assistant certification is claimed.

The next substantive problem is a finite-score all-policy certificate approaching lambda_star, or an actual S=1/2 competing policy. At equality, degenerating stage splits and arbitrary multistage cubic behavior require new estimates. Repeating same-intercept slopes, solved budgets or decimal inverses is not that construction.

[Exact probe](../../tests/channel-swings/k2517_small_score_stopping_transition_probe.py), [saved report](../../lab/process/k2517-small-score-stopping-transition.json), [K2515](k2515-stopping-transition-certificate-2026-11-02.md), [original reduction K2485](k2485-constrained-stopping-frontier-2026-11-01.md), [K2483](k2483-adaptive-stopping-bellman-2026-11-01.md).
