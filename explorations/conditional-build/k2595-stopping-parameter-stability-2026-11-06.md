---
title: "K2595 Uniform stopping topology and multiplier sensitivity"
status: active_research
doc_type: exploration
created: "2026-11-06"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: complete frontier at S=1/2 and lambda in [0.54999,0.55001] only; no arbitrary score or physical probability claim
scripts:
  - tests/channel-swings/k2595_stopping_parameter_stability_probe.py
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
result: K2595
carrier: original fair stopping policies at S=1/2 and a fixed multiplier interval LAYER=toy CHIRALITY=N/A
pairing: unconditional success minus leakage with expected positive-trial budget ON=declared_carrier
real_structure: real controls and private randomization
grading: score, first action, stage count and expected trials distinguished
action_owner: repository-construction -- supplied conditional probability model
target: uniform all-budget frontier, crossing sensitivity and budget consumers MAP-TYPE=evaluation
```

# A complete frontier stable under a multiplier interval

## Result and scope

K2593's complete finite expected-resource frontier persists for EVERY lambda in [54999/100000,55001/100000], with S=1/2 fixed. Its abort, pure-one, mixed-one/two, pure-two, mixed-two/three and zero-action tail pieces remain valid, with unique smoothly varying transition prices kc(lambda) and kd(lambda). This is a continuum theorem, not a parameter grid. No statement is made for every multiplier or a varying score.

The useful follow-through is quantitative: crossing sensitivities, the optimal leakage response, a uniform exact-budget399/100 consumer whose value is AFFINE in lambda, and an actual budget5 policy transferred across the interval. This is independent mathematics in the supplied fair stopping model. SC-META-53 remains UNCERTAIN; source register, ledger0.263, physical probability, canon and native GU credit are unchanged. Prior fixed-parameter results and the adaptive-policy reduction retain their explicit credit.

## 1. Uniform support reduction by a convex perspective

Use K2593's original law, w(a,b), H_m=m w(0,S/m), c(b), resource R, leakage C and success p. For completed schedules, 0<=C<=S=1/2: w decreases in a, w(0,0)=0 and w0'(b)<=1/2 on [0,1/2], so 2 sum P_i w<=sum b_i. This also holds for the adaptive mixtures of K2569. Thus for lambda'>lambda, each class value Qi satisfies

    -S(lambda'-lambda) <= Qi(lambda',k)-Qi(lambda,k) <= 0. (1)

Differences of two such class values change by at most S|delta lambda|, not twice that bound.

Keep I=[.00254,.0089], middle price.003, and two-stage score interval[.15,.35]. The majorant is

    U(J,B,lambda)=J+(B-J)_+²/(2lambda),
    J_m=1-2lambda H_m-2km.

The squared positive part is convex; its perspective x_+²/(2lambda), lambda>0, is jointly convex. On x>0 its Hessian is positive semidefinite with determinant zero; at x=0 the first derivative joins continuously to zero. J and B are affine in(lambda,k). Therefore U-J2 is jointly convex. A convex function on a rectangle is bounded above by a convex combination of its four corner values. This is the standard perspective operation, as described in Boyd and Vandenberghe, [Convex Optimization, section3.2.6](https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf); the Hessian and join are independently checked here.

The exact probe checks all four corners of the multiplier/price rectangles for K2593's m>=4, extreme-score and upper-price count3 exclusions. It separately checks positive intercepts, count monotonicity, zero3 at prices up to.003, zero suffix action, positive first action, sharp tail, and high/low price overlaps at both multiplier endpoints. These inequalities are affine or have monotonic endpoint reductions as specified in K2593. Smallest representative margins include >.00265 for m>=4 exclusion, >.00196 for extreme scores and >.0000215 for positive first action. Every strict margin is certified with rational logarithm bounds.

Consequently, throughout the rectangle the actual all-policy support remains

    Q(lambda,k)=max(Q1(lambda,k),Q2(lambda,k),J3(lambda,k)),
    Q2=max_(.15<=b<=.35,0<=a<=b)
       [1-2lambda(w(a,b)+w0(S-b))-4k]/(1+a).              (2)

The final action is zero as a proved optimizer property, not a restriction imposed on competing policies. All stage counts are bounded by the universal count majorants; an unexamined large count is not discarded.

## 2. Crossings, full budget topology, and sensitivity

Recompute rational support certificates for the kd endpoint candidates at.00254 and.00255. The center signed margins exceed respectively.00001350 and.000006499. Equation(1) spends at most.000005 across the whole half-width, preserving their signs. K2591's unchanged exact kc endpoint supports at.0088 and.0089 are reused by hash; their margins likewise exceed.000005.

The resource separations hold uniformly:

    R2-R1 >= 26/27,    R3-R2 >=2.

They make Q1-Q2 and Q2-J3 strictly increasing in price, giving unique crossings kd in(.00254,.00255) and kc in(.0088,.0089). Tail support at k3=lambda(H3-H4), the new kd support, affine comparison in price and K2587's sharp tail cover lower prices. K2589's high-price theorem overlaps I and covers higher prices. The same original-policy construction and attainment proof as K2593 therefore applies to EVERY finite budget: replace lambda,kc,kd and their optimizing resources in its six-row table. There is no missing price interval. The sharp count-three tail persists; the count-two sharp threshold is below the entire strip.

The active one/two optimizers at the transitions are interior. For one stage, the probe checks J1(.0088,lambda)<2lambda c(S), so the derivative of its original priced objective at a=0 is positive throughout the crossing bracket; at a=S the original objective derivative is negative because w_a=0 and its value is positive. The two-stage interiority checks are inherited uniformly from section1. Strict positive Hessians of their supporting functions give smooth optimizer dependence by the implicit-function theorem. For Q2, W=w(a,b)+w0(S-b) is strictly convex; the denominator is handled by its positive supporting function, not called convex. Differentiate Qi_lambda=-Ci and Qi_k=-Ri. At a crossing of left class i and right class j,

    k'(lambda)=(Ci-Cj)/(Rj-Ri),
    |kc'|<=27/52,   |kd'|<=1/4.                           (3)

The formulas apply throughout this strip; smoothness fails to be asserted at a topology change outside it. At a mixed budget, envelope differentiation gives F_lambda=-[theta Ci+(1-theta)Cj], where theta is its actual resource-restoring mixture weight. Thus the frontier's sensitivity is the attained leakage. No finite difference is used as certification.

## 3. Exact affine consumer at budget399/100

Set M=399/100 and a=4/M-1=1/399. The minimizing score b* for

    g(a)=min_b [w(a,b)+w0(S-b)]

is independent of lambda. Let b0 be K2593's explicit rational approximation. Its exact rational derivative residual r=W_b(a,b0) satisfies |r|<2e-57. Since W_bb>=w0''>=3/16 on the admitted interval,

    |b*-b0| <=16|r|/3,
    W(a,b0)-8r²/3 <=g(a)<=W(a,b0).                       (4)

The interval encloses the unique score minimizer. The explicit numerator representation

    w=log N-log2-log(a+b)-log(2-a-b),
    N=4a+4b-a²-6ab-b²

gives |w_ab|<300 at a=1/399, b in[.15,.35]: N>.5, |N_a|,|N_b|<=4, |N_ab|=6, a+b>=.15 and2-a-b>1.5. Hence g'(a) is bounded by w_a(a,b0) +/-1600|r|. The supporting price

    k(lambda)=[1-2lambda(g-(1+a)g')]/4

stays strictly between.00255 and.0088 at both endpoints and therefore throughout the strip. This proves the consumer stays on the pure-two branch; affine value is not assumed before proving branch membership.

    F(399/100,lambda)=M/4-(lambda M/2)g,
    dF/dlambda=-(M/2)g approximately -.271515972355975.     (5)

Exact rational log intervals and (4) enclose (5) uniformly to width below10^-40. The report executes both interval endpoints and the center, with exact resource399/100; their affine bounds cover the continuum.

## 4. Released actual mixed-budget consumer

Retain K2593's rational two-stage policy and equal-three policy near the center kd. Keep theta=(6-5)/(6-R2); its mixture has EXACT resource5 for every lambda because the probability law does not depend on the leakage multiplier. Its value is the same center value minus delta lambda times its explicitly computed leakage, approximately.271333261667768. This supplies an affine feasible lower bound throughout the strip.

A matching conservative global upper bound is F_center_upper+S max(0,lambda_center-lambda), by(1). The two actual endpoint brackets have width below10^-5; they are genuine robust bounds, not new10^-40 mixed optimizers. The sharper pure-budget enclosure in section3 and the weaker transferred mixed consumer are intentionally distinguished. Reoptimizing the mixed policies can tighten these bounds, but is not needed to prove topology or quantitative robustness.

## 5. Execute the neighboring topology boundary

K2587 already gives the sharp count-two threshold

    lambda2=1/[2(c(S/2)+3H2-2H3)].

New exact interval evaluation isolates it in(.54996339,.54996340), strictly BELOW the uniform strip. At lambda=.5499, budget5 is attained by an equal mixture of the actual equal-score zero-action counts two and three, with exact value

    F(5,.5499)=1-.5499(H2+H3).

The probe encloses this value below10^-40 width and checks exact budget5. Global optimality follows from the reused sharp threshold theorem, not from this single finite policy check. Thus the positive-action two/three structure cannot be continued unchanged across lambda2. This identifies and consumes a real topology boundary; it does not solve the near-boundary asymptotic expansion or other score values. It is stronger than reporting that a chosen parameter rectangle ended.

## Verification and next condition

The probe checks62 rational/symbolic supporting facts and8 contrary controls. The universal perspective, all-count, uniqueness, attainment and sensitivity arguments are written above and reuse explicitly identified predecessor proofs. K2591 endpoint supports are reused evidence with pinned hashes, not newly executed tests. No external-expert, proof-assistant or physical certification is claimed.

Next derive the near-boundary positive-action expansion across the now isolated sharp count-two threshold, or construct a score-varying region with uniform bounds. Do not requeue this strip's full topology, crossing sensitivity or pure-budget affine response as absent. The physical response/readout arc remains independent.

[K2593](k2593-countwise-convex-stopping-2026-11-06.md), [K2591](k2591-multistage-stopping-support-2026-11-06.md), [K2587](k2587-countwise-stopping-support-2026-11-05.md), [probe](../../tests/channel-swings/k2595_stopping_parameter_stability_probe.py), [report](../../lab/process/k2595-stopping-parameter-stability.json).

Independent read-only field specialists and a distinct integrated hostile reviewer inspected the mathematical transfers and final candidates. K2594 passes38 supporting checks and7 contrary controls; K2595 passes62 and8. Exact polynomial/jump/interval calculations, reused predecessor certificates and exponent bookkeeping are distinguished from the written continuum kernel, synthesis, convexity and sensitivity proofs. No external-expert, proof-assistant or physical certification is claimed. Final substantive findings: [].
