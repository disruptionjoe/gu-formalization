---
title: "K2577 The exact small-multiplier resource tail"
status: active_research
doc_type: exploration
created: "2026-11-05"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: exact supplied-law finite-resource frontier for 0<lambda<=2/5; no native GU or general multiplier solution
scripts:
  - tests/channel-swings/k2577_exact_resource_tail_probe.py
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
result: K2577
carrier: original adaptive fair stopping law reduced to finite completed schedules LAYER=toy CHIRALITY=N/A
pairing: unconditional success minus original leakage and expected positive-trial price ON=declared_carrier
real_structure: real coefficients and positive auxiliary norms; complexification only where explicit
grading: positive stages, expected trials and pathwise counts remain distinct
action_owner: repository-construction -- stated conditional model
target: the complete small-multiplier finite-resource frontier MAP-TYPE=evaluation
```

# The complete small-multiplier resource frontier

## Result and scope

For the original supplied fair stopping law, define F_lambda(M)=sup(p−lambda C) over policies with expected positive-score trials R<=M. For EVERY 0<lambda<=2/5, at S=1/2, this note completes the entire finite-resource frontier. The previous K2575 nonlinear segment ends at M=2. The new tail is piecewise linear, with vertices realized by n equal positive stages having a=0, success probability1 and expected trials2n. Between vertices, randomize once between the neighboring schedules. This is global over original adaptive policies, including abandonment and private randomization, by K2569's resource-preserving reduction and K2571's positive-price finite attainment.

This is GU-independent conditional probability mathematics. SC-META-53 remains UNCERTAIN. Ledger0.263, source polarities, native action/observation/quotient debts, canon and physical claims are unchanged. No novelty or experimental resource calibration is asserted. Expected trials are not a pathwise trial cap.

## 1. Uniform action exclusion at small positive prices

For a finite completed schedule with positive b_i summing to S<=1/2 and 0<=a_i<=b_i, use

    P_i=product_(j<=i)(1+a_j)^(-1),
    w(a,b)=log(1+(b−a)^2/[2(a+b)(2−a−b)]),
    J_k=P_n−2 sum_i P_i[lambda w(a_i,b_i)+k],
    R=2 sum_i P_i.

K2571 proves that every k>0 has an optimal finite schedule or abort. Its actual original-law scope is essential. K2509 section1 proves w_aa>0 for fixed b>0. Therefore

    0<=−w_a(a,b)<=−w_a(0,b)=2(3−2b)/[(2−b)(4−b)]<4/5.

The strict upper bound follows since (4/5)(2−b)(4−b)−2(3−2b)=(4b²−4b+2)/5>0. The origin is handled by one-sided cone limits; only positive b are used for differentiation.

For 0<lambda<=2/5 and 0<k<=1/16, a single a=0 stage gives

    Q_k>=1−lambda S−2k>=27/40>(8/5)lambda.

Here w(0,S)<=S/2 is K2575's proven bound. In any positive finite maximizer, every suffix value V_i is at least Q_k: each preceding affine map (x−2lambda w−2k)/(1+a) reduces a positive x. A nonpositive suffix cannot yield a positive total. Holding b_i and all other controls fixed,

    partial_(a_i) V_i=[−2lambda w_a(a_i,b_i)−V_i]/(1+a_i)<0.

Its whole-schedule derivative has an additional positive prefix factor. Thus any a_i>0 admits a strict improvement by decreasing it slightly. EVERY finite maximizing schedule in this price range has all a_i=0. This argument uses an attained global optimizer, not a claim that the derivative has this sign for every arbitrary bad schedule.

## 2. Equal stages and exact price thresholds

Put

    w0(b)=w(0,b)=log((4−b)/(4−2b)),
    H(t)=t w0(S/t), t>=1.

The derivatives satisfy w0''(b)=1/(2−b)^2−1/(4−b)^2>0. Hence Jensen's inequality shows that at fixed n, the unique minimizing positive score vector is b_i=S/n. Since a=0, p=1,R=2n, and

    Q_k=max_(n>=1)[1−2lambda H(n)−2kn]

in the stated price range; abort is strictly dominated. Write x=S/t. Then H'=w0(x)−xw0'(x)<0 and H''=x²w0''(x)/t>0. Thus H(n) decreases strictly to S/4 and its successive drops decrease strictly to0. Define

    k_n=lambda[H(n)−H(n+1)]>0.

All k_n lie inside the proved exclusion range. Indeed w0''<=4/9 on[0,1/2], and

    H(1)−H(2)=w0(S)−2w0(S/2)<=S²/9,
    k_n<=k_1<=1/90<1/16.

The first inequality follows by integrating w0'(u+S/2)−w0'(u) over0<=u<=S/2. At k=k_n exactly the n and n+1 stage candidates tie and dominate every other count by strict convexity of H. For n>=2, k_n<k<k_(n−1) selects exactly n stages; ties select its two neighbors. For k_1<k<=1/16 the optimizer is one stage. This is an efficient exact count selection via monotone thresholds, without enumerating a high-dimensional control grid.

## 3. Execute the entire post-two tail

For M>=2, set n=floor(M/2) and alpha=(M−2n)/2 in[0,1). At k=k_n the global support inequality J−kR<=Q_k holds for EVERY original policy. The mixture with probabilities1−alpha and alpha of the n and n+1 equal-stage policies has R=M and attains that support. Therefore, for every0<S<=1/2,

    F_lambda(M)=1−2lambda[(1−alpha)H(n)+alpha H(n+1)],
    0<lambda<=2/5, M>=2.                              (1)

No mass at abort or infinite schedule is needed for this optimizer. The result establishes an optimal law, not uniqueness of every internal implementation. It is strictly increasing, with slope k_n on each open segment, and has a downward slope jump at every even M>=4. Noninteger M is an expected resource budget and is realized by initial randomization, not a fractional number of stages on one path.

At S=1/2, combine(1) with K2571/K2575 to obtain ALL budgets:

    F_lambda(M)=M/2,                         0<=M<=4/3;
    F_lambda(M)=M/2−lambda M w(2/M−1,1/2),   4/3<=M<=2;
    F_lambda(M)=the expression in(1),        M>=2.

The first segment uses the free one-stage schedule plus abort; the middle is the previously proved one-stage resource range. The tail is the new result. At M=2 the left derivative is [1−lambda(32/21+2log(7/6))]/2, whereas the right derivative is k_1=lambda[log(7/6)−2log(15/14)]. The corner is genuine: using log(7/6)<1/6, the left derivative exceeds9/70 forlambda<=2/5, while k_1<=1/90. The frontier is not globally smooth and the one-stage formula cannot be extended through negative a.

## 4. Concrete original-law consumer

At S=1/2, lambda=1/10 and M=3, choose with probability1/2 either one stage b=1/2 or two stages b=1/4 each, all a=0. Then

    p=1, R=3,
    C=log(7/6)+2log(15/14),
    F_(1/10)(3)=1−[log(7/6)+2log(15/14)]/10.

The saved report gives rational logarithm enclosures for this exact optimum and its supporting price k_1. A deterministic two-stage policy uses expected4 and violates the budget3; a single stage is feasible but strictly suboptimal. The construction explicitly executes the mixture, original failure-inclusive leakage, price support and expected resource calculation.

## 5. Released sharp asymptotic resource and price consumers

For |b|<2,

    w0(b)=sum_(j>=1)(2^(−j)−4^(−j))b^j/j
          =b/4+3b²/32+7b³/192+O(b^4).

Uniformly in alpha in[0,1], with M=2(n+alpha), substitution into(1) gives

    V_lambda=1−lambda S/2 (reuse K2561),
    V_lambda−F_lambda(M)=3lambda S²/(8M)+7lambda S³/(24M²)+O(M^(−3)).       (2)

The interpolation error first enters at order M^(−3): expanding the two weighted terms around n+alpha cancels the linear deviation. A useful sharpened bound, from 0<w0'''<=16/27, is 3lambda S²/(8M)<=V−F(M)<=3lambda S²/(16n)+16lambda S³/(81n²). Every finite budget has a strict gap. Thus the minimum expected resource for error epsilon below the unpriced supremum satisfies M_epsilon~3lambda S²/(8epsilon), for fixed positive lambda,S in range. This is sharp for the FULL original policy class, not merely an upper bound for one construction or a pathwise complexity assertion.

A nonasymptotic sufficient consumer follows from w0''<=4/9:

    0<H(n)−S/4<=2S²/(9n),
    0<V_lambda−F_lambda(M)<=4lambda S²/(9 floor(M/2)).   (3)

At S=1/2,lambda=1/10,error1/1000, n=12 (expected24 trials) suffices by(3); the exact optimal gap is also enclosed in the report. This is a constructive resource choice, while(2) gives the limiting best constant.

The thresholds and priced optimum have sharp small-price laws:

    k_n~3lambda S²/(32n²),
    n(k)~S sqrt(3lambda/(32k)),
    R(k)~S sqrt(3lambda/(8k)),
    V_lambda−Q_k~S sqrt(3lambda k/2),    k down to0.

At ties either adjacent n or their mixtures has the same asymptotic. These follow from the displayed convergent series and minimization of 3lambda S²/(16n)+2kn; discrete rounding contributes a lower-order error. The square-root price loss and reciprocal budget loss are compatible dual descriptions, not competing resource conventions.

## Evidence, counterexamples and remaining scope

The universal result is carried by the optimizer-exclusion, strict convexity and support proofs. Exact probes check derivative algebra, the uniform rational margins, series coefficients, actual finite laws, rigorous log enclosures, boundary slopes and contrary constructions. Finite checks do not prove the all-policy theorem. The strongest overclaim is extrapolation beyondlambda2/5: K2575'slambda1.9 small-price witnesses already have nonzero a and show the different regime needs its own argument. The new proof does not resolve that intermediate frontier or the sharp multiplier transition. K2565's bracket remains unchanged.

[K2575 earlier nonlinear segment](k2575-constructive-priced-optimization-2026-11-05.md), [K2571 positive-price attainment](k2571-stopping-resource-price-2026-11-05.md), [K2569 resource-preserving reduction](k2569-stopping-maximizing-sequences-2026-11-05.md), [K2509 strict convexity](k2509-stopping-atom-certificate-2026-11-02.md), [probe](../../tests/channel-swings/k2577_exact_resource_tail_probe.py), [report](../../lab/process/k2577-exact-resource-tail.json).
