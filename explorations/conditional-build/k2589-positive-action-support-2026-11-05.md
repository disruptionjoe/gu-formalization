---
title: "K2589 Global positive-action stopping support"
status: active_research
doc_type: exploration
created: "2026-11-05"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: sharp multiplier-uniform one-stage price region and exact supported budget segment; low-price failed chords remain open
scripts:
  - tests/channel-swings/k2589_positive_action_support_probe.py
---

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
result: K2589
carrier: original fair stopping law with finite completed schedules and initial mixtures LAYER=toy CHIRALITY=N/A
pairing: unconditional success, leakage and positive-trial expectation ON=declared_carrier
real_structure: real controls and private randomization
grading: score, positive actions, expected trials and pathwise counts distinguished
action_owner: repository-construction -- supplied conditional model
target: positive-action optimizer and supported resource frontier MAP-TYPE=evaluation
```

# A global positive-action regime beyond the zero-action transition

## Result

For EVERY 0<S<=1/2, lambda>0 and

    k>=lambda Delta1(S), Delta1=H1-H2,
    Hm=m log[(4-S/m)/(4-2S/m)],                  (1)

the global priced original-policy value is

    Q=max(0, max_(0<=a<=S) [1-2lambda w(a,S)-2k]/(1+a)),
    w(a,b)=log[1+(b-a)²/(2(a+b)(2-a-b))].        (2)

An actual one-stage policy or abort attains it. There is NO small-multiplier restriction. Delta1 is the sharp price coefficient that works uniformly for all lambda. This does not say it is the exact transition price at each fixed lambda.

This extends K2583's small-multiplier price theorem and K2571/75's higher-price sufficient regions. In particular positive-action optimizers beyond K2587's zero-action threshold are now explicitly certified. Released consumers solve a new budget segment below2 and two exact rational examples. The failed post2 chords' replacement optimum remains open. The supplied probability model is independent mathematics, not GU probability or physical positivity; SC-META-53, ledger0.263 and canon remain unchanged. No novelty or external certification is asserted.

## 1. A score-scaling inequality with proof

Set A=sum a_i, Wm(A)=m w(A/m,S/m), and q_r(b)=-w_a(rb,b), 0<=r<=1. The key inequality is

    Wm(A)-Hm >= w(A,S)-H1, m>=2,               (3)

strict when A>0. It follows by integrating q_r(S)>=q_r(S/m) over A from0. Here r=A/S varies during the integration; it is not frozen when differentiating Wm in A.

An exact rational formula is

    q_r(b)=2(r-1)(2b(r+1)-r-3) /
            [(r+1)(b(r+1)-2)(b(r²+6r+1)-4(r+1))].

Its b derivative has positive denominator and numerator 4(1-r)P, where

    P=(b²-b)r4+(8b²-10b+3)r3+(14b²-28b+11)r2
       +(8b²-22b+17)r+(b²-3b+1).

On 0<=b<=1/4, absorb the nonpositive r4 coefficient into r3 using r4<=r3. The resulting coefficients of r3,r2,r,1 are bounded below by 13/16,39/8,12,5/16. Thus q_r increases with b when r<1 in this interval.

Also q_r(b)-q_r(b/2) has positive denominator and numerator 2b(1-r)Q, with

    Q=(2b²-3b)r4+(16b²-30b+12)r3
      +(28b²-84b+44)r2+(16b²-66b+68)r
      +(2b²-9b+4).

The same absorption on 0<=b<=1/2 gives nonnegative lower bounds 0,9,39,0. For r>0,b>0,r<1 the r and r2 terms make Q positive. At r=0 it is nonnegative, vanishing only at b=1/2; at r=1 q=0. Therefore q_r(S/m)<=q_r(S/2)<=q_r(S). The integrated inequality is STRICT for A>0 because the interval 0<r<min(A/S,1) has positive measure and strict half-scale inequality. No sample-grid monotonicity is used.

## 2. All schedules, all actions and the essential sign split

Use the inherited completed schedules P_i=product_(j<=i)(1+a_j)^-1, p=P_m, C=2sum P_i w_i, R=2sum P_i. All costs and k are nonnegative and P_i>=p. K2581's joint convexity gives sum w_i>=Wm(A), so

    J=p-lambda C-kR <=p Nm(A),
    Nm(A)=1-2lambda Wm(A)-2km.                 (4)

If Nm<=0, abort dominates. If Nm>0, the product inequality product(1+a_i)>=1+A gives p<=1/(1+A), and J<=Nm/(1+A). This sign split is necessary.

K2577's decreasing convex Hm gives H1-Hm<= (m-1)Delta1. Under(1), the zero-action intercepts obey Jm=1-2lambda Hm-2km<=J1. Equation(3) now yields

    Nm(A)<=N1(A).

Thus every completed schedule is bounded by (2), which an actual one-stage schedule or abort attains. K2569's reduction of arbitrary adaptive policies raises success-minus-leakage and lowers expected resource; integrate this bound over its schedule mixtures. Nonpositive or infinite-priced costs cannot improve it. The result holds for the original policy class, not just deterministic schedules.

For m>=2,A>0 the scaling inequality is strict. Consequently whenever a unique positive one-stage optimum exceeds all zero-action intercepts, no multistage schedule is also optimal. Ties at critical endpoints are retained.

## 3. Solve the supported positive-action branch

Define

    Mfun(a,S)=-2(1+a)w_a(a,S)+2w(a,S).

Fixed-score strict convexity gives Mfun'=-2(1+a)w_aa<0. It decreases from 2c(S)+2H1 to0 at a=S. Differentiating the one-stage priced value gives

    J'(a)=[lambda Mfun(a,S)-(1-2k)]/(1+a)².   (5)

For k>=1/2 every positive-trial schedule has nonpositive priced value, and abort is optimal (at k=1/2 the leakage-free stage a=S ties). For k<1/2, a=S has positive value; the unique optimum is a=0 if lambda Mfun(0,S)<=1-2k, otherwise the unique interior root of equality in(5). This fully computes the global optimizer throughout (1), using a monotone one-dimensional equation with rigorous bisection.

Let Lambda(S)=1/[2c(S)+4H1-2H2]. If

    Lambda(S)<lambda<1/(2Delta1),

then at k*=lambda Delta1 there is a unique a* in(0,S). Its exact root satisfies Mfun(a*,S)=1/lambda-2Delta1; R*=2/(1+a*)<2. For every a in[a*,S), define

    k(a)=[1-lambda Mfun(a,S)]/2.

It lies in[k*,1/2), so the one-stage policy is globally supported at its resource M=2/(1+a). The exact constrained frontier on

    2/(1+S)<=M<=R*

is therefore

    F(lambda,M,S)=M/2-lambda M w(2/M-1,S).      (6)

The support is valid for the inequality constraint R<=M because k(a)>=0. At the lower endpoint a=S, the old general bound p<=R/2 gives F=M/2 and mixing this zero-leakage policy with abort gives the entire lower segment 0<=M<=2/(1+S). Equation(6) adds an above-Lambda nonlinear segment, not the unknown gap R*<M<2 or post2 optimizer. At lambda>=1/(2Delta1), abort is optimal throughout the certified price wedge; at the equality corner k=1/2 the zero-leakage one-stage policy also ties. No strictly positive priced optimum is inferred there.

## 4. Exact original-law consumers and endpoint computation

At S=1/2, lambda=11/20 choose a=1/100, so M=200/101. At S=1/4, lambda=13/20 choose a=1/50, so M=100/51. The probe encloses the logarithms with positive rational atanh series and geometric remainder. It verifies lambda>Lambda(S), k(a)>lambda Delta1, k(a)<1/2, and the original survival p=1/(1+a), failure-inclusive leakage C=2p w, and expected trials R=2p. Thus(6) is the actual optimum at both budgets. Neither a floating optimizer nor an unweighted proxy supplies acceptance.

For the half-score lambda11/20 endpoint the same rational bounds execute monotone bisection for a* at k*. The initial interval[0,S] has opposite derivative signs; at each chosen dyadic point the enclosing sign is decisive. The final bracket width is at most2^-30 S, with corresponding certified brackets for R* and Q. This makes the newly released endpoint computable, while the theorem, not those finite iterations, excludes every multistage competitor.

### Released post2 consumer: certified bounds where the old chord fails

In the regime Lambda(S)<lambda<1/(2Delta1) of section3, the new globally exact support also bounds the unresolved post2 frontier. At k*=lambda Delta1 let V*=Q*+k*R* and let J1=1-2lambda H1-2k*. The zero-action two-stage policy has V2=J1+4k*. Mixing the optimal one-stage policy with that two-stage policy at resource M in[R*,4] yields

    theta=(4-M)/(4-R*),
    lower=theta V*+(1-theta)V2,
    upper=Q*+k*M,
    upper-lower=(1-theta)(Q*-J1).

For 2<=M<4 the feasible lower bound strictly exceeds the former chord by theta(Q*-J1)>0. The upper bound is global over all original policies. This is a certified bracket, not a new exact post2 optimizer. To avoid implementing an irrational action, the probe uses the actual rational action1/125 at S=1/2,lambda11/20, mixes with the zero-action two-stage policy to attain budget3 EXACTLY, and encloses its value from below. The independently certified endpoint Q* supplies the global upper bound. Their width is less than51/1000000, with strict improvement over the old zero-action chord. No numerical-search optimality is inferred.

## 5. The price coefficient is sharp uniformly in lambda

For any 0<=t<Delta1 take k=t lambda and choose lambda>0 sufficiently small that lambda[Mfun(0,S)+2t]<=1 and 1-2lambda(H1+t)>0. Then(5) makes the best one-stage policy a=0, strictly better than abort. The zero-action two-stage policy exceeds it by EXACTLY

    2lambda(Delta1-t)>0.

Therefore no smaller multiplier-uniform coefficient t can replace Delta1 in(1). The probe executes S=1/2, t=Delta1/2 and lambda=1/10 with rigorous interval arithmetic, proving both one-stage optimality within its class and the two-stage counterpolicy. This is an actual policy counterexample to lowering the price condition, not a mutation of a theorem label.

## Verification and remaining work

Exact derivatives and scaling polynomials, interval consumers, monotone endpoint bisection and adverse survival/resource/sign controls support the written all-policy proof. They do not constitute formal proof-assistant or external-expert certification. Positive-action schedules on failed M>=2 chords and the lambda-specific low-price transition remain open; K2587 sharp zero-action thresholds and K2561 unrestricted continuum value are reused, not newly claimed.

[K2587](k2587-countwise-stopping-support-2026-11-05.md), [K2581](k2581-score-sensitive-tail-transition-2026-11-05.md), [K2583](k2583-complete-stopping-resource-frontier-2026-11-05.md), [K2569](k2569-stopping-maximizing-sequences-2026-11-05.md), [probe](../../tests/channel-swings/k2589_positive_action_support_probe.py), [report](../../lab/process/k2589-positive-action-support.json).

Independent read-only field specialists and a distinct integrated hostile reviewer found no remaining substantive defects after endpoint, sign and evidence-wording corrections. K2588 passes23 exact/supporting checks and8 contrary controls; K2589 passes34 and8 including the released post2 bracket. Universal ODE/domain and all-policy proofs remain separate from finite interval, matrix and reporting checks. No external-expert, proof-assistant, remote-CI or physical certification.
