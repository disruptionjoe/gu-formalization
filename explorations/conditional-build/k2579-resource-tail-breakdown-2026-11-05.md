---
title: "K2579 A certified transition for equal-stage resource tails"
status: active_research
doc_type: exploration
created: "2026-11-05"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: expanded exact post2 frontier and certified transition bracket; no middle-resource extension or full intermediate optimum
scripts:
  - tests/channel-swings/k2579_resource_tail_breakdown_probe.py
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
result: K2579
carrier: original fair stopping law with finite completed schedules and initial mixtures LAYER=toy CHIRALITY=N/A
pairing: unconditional expected success, leakage and positive-trial functional ON=declared_carrier
real_structure: real controls and multiplier; probability laws and private randomization
grading: stages, expected positive trials and pathwise trial counts kept distinct
action_owner: repository-construction -- stated conditional model
target: action perturbation and exact resource-preserving contrary policies MAP-TYPE=evaluation
```

# A resource-preserving counterexample to the continued tail

## Result and boundary

K2577 completely solves the expected-trial frontier for 0<lambda<=2/5 at S=1/2. It does not justify the same equal-stage answer for larger multipliers. Here a sharper optimizer exclusion extends the exact post2 tail to lambda_safe≈0.535190, while an action perturbation bounds the true full-tail transition above by≈0.536354. A rational two-schedule mixture strictly improves the old budget3 answer at lambda3/5. The proof supplies feasible improvements at every point of every failed chord; it does not mistake failure of a particular dual support for a global constrained counterexample.

This is GU-independent conditional probability mathematics. SC-META-53 remains UNCERTAIN, source polarities, ledger0.263 and canon unchanged. Expected trials are distinct from pathwise caps. No global intermediate optimizer, sharp global phase transition, physical resource calibration or novelty claim is asserted.

## 0. Execute an enlarged exact tail before testing its failure

For S=1/2, direct maximization of c(b)=−w_a(0,b) on0<=b<=1/2 gives

    cmax=3−sqrt5 at b*=(3−sqrt5)/2.

The exact factorization (cmax−c(b))(2−b)(4−b)=cmax(b−b*)² proves this is the GLOBAL maximum. Let H_n=n w0(S/n) and

    lambda_safe=1/[2(3−sqrt5)+4log(7/6)−4log(15/14)]
               in(535190/10^6,535191/10^6).

For0<lambda<=lambda_safe and any0<k<=k_1=lambda(H_1−H_2), the one-stage zero-action candidate supplies

    Q_k>=1−2lambda H_1−2k
        >=1−lambda(4H_1−2H_2)>=2lambda cmax>0.

By K2571 a finite positive optimizer exists. Every suffix V_i is at least Q_k: preceding affine maps (x−2lambda w−2k)/(1+a) decrease positive values; any nonpositive suffix would make the total nonpositive. If any a_i>0, inherited strict w_aa>0 gives −w_a(a_i,b_i)<c(b_i)<=cmax. The action derivative of that suffix is (−2lambda w_a−V_i)/(1+a_i)<0; its whole-schedule derivative has only an extra positive prefix. Decreasing a_i therefore improves the optimizer, a contradiction. The equality case lambda=lambda_safe is valid because a_i>0 supplies strictness. All optimal actions are zero.

Strict Jensen minimization then forces equal scores at fixed stage count. K2577's convex perspective H(t)=t w0(S/t) and decreasing adjacent differences show that at every k_n the n/n+1 schedules give the global priced optimum. Their mixture at expected budget M=2(n+alpha) therefore attains the global support inequality. For EVERY M>=2,

    F_lambda(M)=1−2lambda[(1−alpha)H_n+alpha H_(n+1)],
    0<lambda<=lambda_safe, n=floor(M/2), alpha=(M−2n)/2.      (0)

This enlarges only the POST2 formula. The middle4/3<M<2 formula retains K2575's proven multiplier range; no extension is inferred. As a new exact consumer, atlambda8/15 andM3 the optimal original law mixes one and two zero-action stages equally, with value1−(8/15)[log(7/6)+2log(15/14)]. The rational certificate verifies8/15<lambda_safe, so this example lies beyond the former2/5 guarantee.

## 1. Perturb an actual schedule

For the supplied original law, P_i=product_(j<=i)(1+a_j)^(-1), p=P_n, C=2 sum P_i w(a_i,b_i), R=2 sum P_i, with

    w(a,b)=log(1+(b−a)²/[2(a+b)(2−a−b)]),
    J=p−lambda C, 0<=a_i<=b_i, sum b_i=S<=1/2.

Set b=S/n,w0(b)=w(0,b),H_n=n w0(S/n),

    c(b)=−w_a(0,b)=2(3−2b)/[(2−b)(4−b)],
    k_n=lambda(H_n−H_(n+1))>0.

The old n and n+1 equal-stage candidates have J_n=1−2lambda H_n,R_n=2n and equal priced value J_n−2nk_n. Keep every b_i=b, take ONLY a_1=epsilon in(0,b], and leave later actions zero. This is a valid original policy with

    R_epsilon=2n/(1+epsilon),
    J_epsilon=[1−2lambda(w(epsilon,b)+(n−1)w0(b))]/(1+epsilon).

Differentiating the priced excess at zero gives

    d/d epsilon [J_epsilon−k_n R_epsilon]_(0)=lambda D_n−1,
    D_n=2c(S/n)+2H_n+2n(H_n−H_(n+1)).                  (1)

Thus lambda>lambda_n:=1/D_n yields a strictly positive excess for sufficiently small positive epsilon. This is a one-sided derivative with a positive admissible interval, hence an existence proof of an actual finite-policy improvement. At equality the first derivative is zero and this argument makes NO verdict. Other perturbations might fail earlier; lambda_n is not claimed to be a sharp global transition.

## 2. Execute the exact budget repair

For ANY M in[2n,2n+2), mix the perturbed n-stage schedule with the unchanged equal(n+1) schedule. Put

    theta=(M−R_epsilon)/(2n+2−R_epsilon)

on the n+1 schedule. Since R_epsilon<2n<=M<2n+2, 0<theta<1 and expected resource is exactly M. If L_n(M) is the old straight chord between the two equal-stage candidates, the improvement is exactly

    J_mix−L_n(M)=(2n+2−M)/(2n+2−R_epsilon)
                  *[J_epsilon−k_n R_epsilon−(J_n−2nk_n)].    (2)

Every factor is positive under(1). This turns a dual direction into a concrete feasible violation of the entire half-open chord. At its far endpoint the factor vanishes; use the next chord's condition if needed. No conclusion about the full optimum's exact value or support size is obtained beyond this lower bound.

## 3. Execute all count thresholds and their limiting boundary

For0<b<=1/2,

    c(b)−3/4=b(2−3b)/[4(2−b)(4−b)]>0.

Moreover H_n>S/4 by the positive power series of w0, and H_n−H_(n+1)>0 by strict convexity, as proved in K2577. Therefore

    D_n>(3+S)/2, lambda_n<2/(3+S).

Since c(S/n)->3/4, H_n->S/4 and n(H_n−H_(n+1))->0, the thresholds converge to2/(3+S). The last limit follows directly from H_n=S/4+3S²/(32n)+O(n^-2). At S=1/2 the limit is4/7. Consequently EVERY finite chord fails already at lambda=4/7, even though its limiting derivative margin tends to zero. No single epsilon uniform in n is claimed. For lambda>4/7 the conclusion also holds. This identifies a necessary boundary for any unchanged full equal-stage tail and leaves the gap above lambda_safe unresolved.

At n=1,S=1/2,

    lambda_1=1/[32/21+4log(7/6)−4log(15/14)]
             in(536353/10^6,536354/10^6).

Thus the first chord fails well before4/7. This does not contradict K2577's2/5 theorem or establish monotonicity of the sequence lambda_n.

### A genuine transition, without claiming an exact endpoint

For a fixed M>=2, let B_lambda(M) denote the feasible equal-stage chord. F_lambda(M)−B_lambda(M) is nonnegative and convex in lambda: F is the supremum of affine policy values, while B is affine. It is finite, and continuous forlambda>0; indeed0<=C<=S for all completed schedules by w<=b/2, hence the same Lipschitz bound survives mixtures and the original-law reduction. Atlambda0 success1 is feasible for M>=2, so the difference is zero. Each zero set is an interval. Intersecting over ALLM>=2 gives a closed initial interval with a true full-tail transition lambda_tail. The positive theorem and first-chord violation establish

    lambda_safe<=lambda_tail<=lambda_1,
    lambda_1−lambda_safe<1164/10^6.

Neither endpoint is proved sharp; a different multistage perturbation may fail sooner than lambda_1. This brackets where the ENTIRE post2 tail remains exact, not the optimizer at every multiplier or the transition at a single budget.

## 4. Rational original-policy consumer at budget3

Take S=1/2,lambda=3/5,M=3. Schedule A has (a,b)=(1/100,1/2); B has two stages a=0,b=1/4. Their actual quantities are

    R_A=200/101, J_A=100/101−(120/101)log(17599/15198),
    R_B=4, J_B=1−(12/5)log(15/14).

Mix A with probability101/204 and B with103/204. The expected resource is exactly3 and

    J_mix=203/204−(10/17)log(17599/15198)−(103/85)log(15/14).

The old equal-stage chord gives

    J_old=1−(3/5)log(7/6)−(6/5)log(15/14).

The exact difference obeys

    49/100000 < J_mix−J_old < 1/2000.                 (3)

Numerically J_mix≈0.8252135937665094 and J_old≈0.8247181463193033; these decimals only report the rational enclosures. The certificate uses log r=2 sum_(j>=0)u^(2j+1)/(2j+1), u=(r−1)/(r+1), truncated at j=7 with positive tail<=2u^17/[17(1−u²)]. It computes all success, leakage and resource weights from the original law. Neither schedule alone has expected resource3. Using equal mixture weights would underspend and would not execute the exact equality in this example.

## 5. Consequences for resource and price calculations

Equation(2) supplies a strict lower bound on the true constrained frontier F_lambda(M), invalidating the old chord wherever(1) holds. At the same k_n it also shows the global priced value exceeds the two equal-stage candidates. This does NOT show that either candidate is never optimal at another price, or that one positive action is sufficient for the new optimum. The multistage witness atlambda1.9 in K2575 and unpriced K2565 bracket are retained unchanged.

The next constructive route is to optimize a positive-action prefix plus a zero-action tail, with global support or contrary controls against additional actions. The exact derivative formula gives a cheap count-specific switch condition before expensive search. A larger equal-stage table would miss the new direction; a local optimum cannot certify the all-policy value. General constrained randomized stopping frameworks concern different processes and do not provide this supplied-law calculation.

Universal differentiation, feasible mixing and series limits carry the stated claims. The exact probe independently evaluates schedules, log tails, mixture resource and contrary sign/control substitutions; finite checks are not a proof of a global optimizer. [K2577 valid small-multiplier theorem](k2577-exact-resource-tail-2026-11-05.md), [K2575 prior contrary schedules](k2575-constructive-priced-optimization-2026-11-05.md), [probe](../../tests/channel-swings/k2579_resource_tail_breakdown_probe.py), [report](../../lab/process/k2579-resource-tail-breakdown.json).
