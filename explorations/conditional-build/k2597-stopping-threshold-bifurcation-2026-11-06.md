---
title: "K2597 All finite-count local stopping bifurcations and quadratic value gain"
status: active_research
doc_type: exploration
created: "2026-11-06"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: local threshold neighborhood for each fixed n>=2 and score; separate exact half-score consumer, no arbitrary multiplier topology or physical probability
scripts:
  - tests/channel-swings/k2597_stopping_threshold_bifurcation_probe.py
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
result: K2597
carrier: original fair stopping model for each fixed n>=2 and 0<S<=1/2 near its count-n threshold LAYER=toy CHIRALITY=N/A
pairing: unconditional success minus leakage with expected positive-trial budget ON=declared_carrier
real_structure: real controls and private randomization
grading: score, first action, stage count and expected trials distinguished
action_owner: repository-construction -- supplied conditional probability model
target: global local optimizer bifurcation, price and value asymptotics, certified budget-five consumer MAP-TYPE=evaluation
```

# Resolve the sharp count-two threshold

## Result and scope

**General-count extension:** Section6 proves the same local bifurcation for EVERY fixed finite count n>=2, with a neighborhood depending on n and S. It executes exact coefficient consumers for n=3,5,10 at two scores, and identifies a double-critical n=1 half-score corner where this one-critical-direction proof cannot be reused. Sections1–5 retain the count-two derivation and its independently certified finite-offset consumer.

For EACH fixed total score 0<S<=1/2, the exact count-two threshold of K2587 has a locally unique positive-action two/three-stage transition above it. The first action and score asymmetry emerge linearly; the transition price falls below the old chord price quadratically. For any fixed budget4<=M<6, the optimal value is C1 but not C2 in the leakage multiplier at the threshold. This is a local existence theorem with a score-dependent neighborhood, not a claimed explicit uniform radius or complete arbitrary-multiplier phase diagram.

A separate exact consumer at S=1/2, lambda=.54997, M=5 has global support certified by rational inequalities on an explicit rectangle. Its improvement over the old chord is more than4.62e-12, with a value bracket narrower than1e-50. It lies outside K2595's proved strip, and is NOT certified merely by the local asymptotics.

This is GU-independent mathematics in the supplied fair stopping model. SC-META-53 remains UNCERTAIN. No physical probability, native GU positivity, novelty or external-expert certification is claimed. Source, ledger0.263 and canon are unchanged.

## 1. Original law, threshold and effective curvature

Reuse the original adaptive-policy reduction of K2569 and K2587's global sharp support theorem, without recounting them as new verification. Completed schedules have scores b_i>0, 0<=a_i<=b_i, sum b_i=S,

    P_i=product_(j<=i)(1+a_j)^-1, p=P_m,
    C=2 sum P_i w(a_i,b_i), R=2 sum P_i,
    w(a,b)=log[1+(b-a)²/(2(a+b)(2-a-b))].

Put w0(b)=log[(4-b)/(4-2b)], H_m=m w0(S/m), t=S/2,

    Delta2=H2-H3, T2=3H2-2H3,
    c(t)=2(3-2t)/[(2-t)(4-t)],
    lambda0=1/[2(c(t)+T2)], k0=lambda0 Delta2.           (1)

Near a=0 let b(a) uniquely minimize W(a,b)=w(a,b)+w0(S-b), and set g(a)=W(a,b(a)). The score Hessian is positive, so the implicit-function theorem makes b and g analytic locally. The strict positive Hessian of W gives

    b(0)=t, b'(0)=rho=c'(t)/(2w0''(t))>0,
    g(0)=H2, g'(0)=-c(t),
    h=g''(0)=w_aa(0,t)-c'(t)²/[2w0''(t)]>0.            (2)

This is the Schur-complement curvature after score optimization, not the larger fixed-score curvature. For S=1/2 the actual exact derivatives are

    W_aa=15616/2205, W_ab=-64/2205, W_bb=5632/11025,
    rho=5/88, h=171736/24255.                           (3)

The probe derives(3) from the actual log law. Its symbolic general-score expression for h is positive on0<t<=1/4; explicitly, h=2N/[t(t-4)²(t-3)(t-2)²], N=t^5-22t^4+137t³-362t²+431t-192. Its numerator is negative since N<=1/4^5+137/4³+431/4-192<0, and its denominator is negative. Also c'(t)=4(t²-3t+1)/[(2-t)²(4-t)²]>0 on this interval. These local statements do not assume a pre-existing positive first action throughout a larger price window.

## 2. Why the local branch is globally optimal

At(lambda0,k0), K2587 proves that the ONLY maximizing completed schedules are zero-action equal-score counts two and three: all positive actions are strictly below support by the negative quadratic term; strict Jensen excludes unequal scores; the count gap excludes all other counts. The common value Q0=1-2lambda0 T2=2lambda0 c(t) is positive.

This equality classification extends locally without ignoring arbitrarily large stage counts. Since sum a_i<=S, every P_i>=exp(-S)>=1/2, so R>=m and priced value p-lambda C-kR<=1-km. For k>=k0/2>0, all sufficiently large counts are uniformly below positive support. For each of the finitely many remaining counts, extend controls to b_i>=0 with the FORMALLY CHARGED zero-stage resource2 sum P_i. This is a continuous compact simplex; a zero-score stage still costs2P_i there. Removing it gives a valid compressed schedule with strictly higher priced value. Zero-score boundary points therefore cannot be maximizers. Free zero-cost padding is not used in this compactness argument.

Compactness now gives a strict support gap outside small neighborhoods of the two maximizers. At a zero-action equal-m schedule, differentiating the ORIGINAL survival-weighted law gives

    partial_(a_j)J=2lambda c(S/m)-J_m
                  -2(j-1)[lambda w0(S/m)+k].           (4)

At the threshold, every action derivative for count three is strictly negative because c(S/3)<c(S/2). For count two only the FIRST derivative vanishes; the final derivative remains strictly negative. These inequalities persist locally. Consequently the only nearby contenders are the equal-score zero-three policy and the two-stage policy with final action zero and score b(a). The corresponding supporting function2lambda W+Q(1+a)+4k-1 is strictly convex, so its minimizing controls are unique. This proves the global support reduction in a neighborhood for each fixed S, including adaptive mixtures via the reused reduction.

## 3. Exact crossing equation and emerging policy

At the tie of Q2 and J3, stationarity and equality eliminate the price:

    E(a)=1/(2lambda),
    E(a)=3g(a)-(1+3a)g'(a)-2H3,
    E(0)=1/(2lambda0), E'(a)=-(1+3a)g''(a)<0.           (5)

Thus a unique analytic root crosses a=0; it is positive exactly on the lambda>lambda0 side locally. Its score is b(a), and

    kd=[1-2lambda H3+2lambda g'(a)]/6
       =lambda[g(a)-a g'(a)-H3].                       (6)

For delta=lambda-lambda0>0,

    a=delta/(2lambda0²h)+O(delta²),
    b-t=rho delta/(2lambda0²h)+O(delta²),
    kd=lambda Delta2-delta²/(8lambda0³h)+O(delta³),
    R2d=4/(1+a)=4-2delta/(lambda0²h)+O(delta²).          (7)

The second equality in(6) makes the quadratic price shift transparent: g-a g'=H2-h a²/2+O(a³). It is NOT linear. No numerical differentiation or fitted exponent is used.

## 4. Released budget and differentiability consequences

For fixed4<=M<6, mix the ACTUAL two-stage optimizer with zero-three using

    theta=(6-M)/(6-4/(1+a)).                           (8)

Its resource is exactly M, its value equals Q(kd)+kd M, and global support proves optimality for the inequality budget R<=M. Let Fold=1-lambda[(6-M)H2+(M-4)H3]. Then the EXACT identity is

    F-Fold=(6-M)(lambda Delta2-kd)
           =(6-M)delta²/(8lambda0³h)+O(delta³).         (9)

Below and at lambda0, K2587 proves F=Fold. Above, the analytic branch gives(9). The left and right first derivatives agree, but the second derivatives are respectively0 and(6-M)/(4lambda0³h)>0. Thus F is C1 and not C2 at the threshold. At M=6 there is no gain: equal-three remains optimal locally. The mean-resource endpoint and the unequal-score derivative in(7) are part of the result, not frozen at their zero-action values.

## 5. Independently certified consumer outside the old strip

For S=1/2, the probe certifies on lambda in[.5499,.55001] and k in[.00254,.00255]: all counts>=4 are dominated by zero2; count1 is dominated by zero2; two-stage scores outside[.15,.35] are dominated; the last action is zero; and count3's exact maximum is zero3. It uses K2593's universal count majorant and K2595's jointly convex quadratic perspective. Rectangle corner inequalities plus count monotonicity prove the continuum statement, not merely a grid. Positive intercepts are checked explicitly. Hence throughout this rectangle

    Q=max(Q2,J3).                                      (10)

The new rectangle does NOT assert a positive first action everywhere. The threshold and its price lie strictly inside it by exact log intervals.

At lambda=.54997, a high-precision root only proposes rational controls. The saved rational a,b,k are independently certified by interval logs, the convex tangent bound on2lambda W+Q(1+a)+4k-1, and the explicit feasible mixture(8) at M=5. The resulting global upper bound is max(Q2_upper,J3_upper)+5k. The lower bound is the actual original-law mixture value, not a nominal resource-four shortcut. Their difference is below1e-50, and the lower bound exceeds the old chord by more4.62e-12. The report stores exact rational inputs, bounds, and dependency hashes. No explicit Taylor validity radius is inferred from this separate finite consumer.

## 6. Execute the released general-count theorem

Fix an integer n>=2 and0<S<=1/2. Put t=S/n, Delta_n=H_n-H_(n+1), T_n=(n+1)H_n-nH_(n+1), and lambda_n=1/[2(c(t)+T_n)]. K2587 isolates exactly the equal-score zero-action n and n+1 schedules at their threshold price k_n=lambda_n Delta_n. The large-count cutoff and charged-zero compactness in section2 apply with this fixed positive k_n.

Equation(4) holds for EVERY stage j and count m; the new probe derives it directly from the original law with only a_j perturbed. At the threshold, the first action of count n is critical, every suffix action is strictly unfavorable, and every action of count n+1 is strictly unfavorable since c(S/(n+1))<c(S/n) for n>=2. These signs persist nearby. With suffix actions zero, their survival weights coincide, so strict Jensen forces their n-1 scores to equal(S-b)/(n-1). The exact reduced cost is therefore

    g_n(a)=min_b [w(a,b)+(n-1)w0((S-b)/(n-1))].          (11)

Its positive supporting Hessian yields a unique local optimizer. Define

    rho_n=(n-1)c'(t)/(n w0''(t)),
    h_n=w_aa(0,t)-c'(t)²/([n/(n-1)]w0''(t))>0.        (12)

Positivity follows from the positive definite Hessian of W_n: w has positive semidefinite Hessian and positive aa entry, and the strictly convex suffix term adds a positive bb entry. At a=0, b=t, g_n=H_n, g_n'=-c(t), b'=rho_n, and each suffix score has derivative-rho_n/(n-1).

The unique n/n+1 crossing has

    E_n=(n+1)g_n-(1+(n+1)a)g_n'-nH_(n+1)=1/(2lambda),
    E_n'=-(1+(n+1)a)g_n''<0,
    kd=lambda[g_n-a g_n'-H_(n+1)].                    (13)

The all-count reduction and implicit-function proof give a positive action for lambda just above lambda_n. For delta=lambda-lambda_n,

    a=delta/(2lambda_n²h_n)+O(delta²),
    kd=lambda Delta_n-delta²/(8lambda_n³h_n)+O(delta³),
    R_n=2n/(1+a)=2n-n delta/(lambda_n²h_n)+O(delta²).   (14)

For fixed2n<=M<2n+2, mix the optimizing count-n schedule with zero-(n+1), using theta=[2(n+1)-M]/[2(n+1)-2n/(1+a)]. This is an actual original-law policy at exact expected resource M. Its global optimum satisfies the EXACT gain identity

    F-Fold=[2(n+1)-M] * (lambda Delta_n-kd),              (15)
    Fold=1-lambda[(2n+2-M)H_n+(M-2n)H_(n+1)].

It has quadratic right gain[2(n+1)-M]delta²/(8lambda_n³h_n)+O(delta³), zero left gain, and hence is C1 but not C2 at lambda_n. The right second derivative is[2(n+1)-M]/(4lambda_n³h_n)>0; at M=2n+2 the gain is zero. This closes the local transition class without computing each count separately.

### Higher-count consumers and the exact extension boundary

The probe symbolically checks(13), the original stage derivative, exact resource and gain identities for symbolic n, and recovers the n=2 constants. It evaluates exact Schur curvatures and first-score slopes at n=3,5,10 for S=1/2 and1/4; rational log intervals enclose their thresholds, positive action slopes and gain coefficients. These are executed asymptotic-coefficient consumers, NOT finite-offset global optimizer certificates. The separate n=2 consumer in section5 remains the only such new certificate here.

There is a concrete obstruction to blindly extending this single-critical-direction proof to every n>=1: c(1/2)=c(1/4)=16/21. At n=1,S=1/2 and lambda_1, BOTH count-one and count-two first-action derivatives vanish at their common support. Section2's strict inactivity premise for the upper count fails. This does not disprove a bifurcation theorem there; it requires a coupled two-active-branch analysis. The probe verifies this exact equality.

The neighborhood depends on BOTH S and n. As n grows the positive threshold price tends to zero, so the finite-count cutoff used here is not uniform. No interchange of n->infinity with lambda->2/(3+S), uniform Taylor radius or whole-multiplier phase diagram is proved. Those require new estimates, not substitution into(14).

## Verification and next condition

The exact probe computes the true Hessian, score Schur complement, crossing elimination, all-policy rectangle inequalities and original-policy global enclosure. Written compactness/strict-gap and implicit-function arguments carry the score-general local theorem. Contrary controls reject fixed-score curvature, frozen equal scores, reversed price shift, rounded mixture resource and strict improvement at budget6. Independent field-specialist and distinct integrated hostile reviews returned final substantive findings[].

Next compare the n=1 half-score double-critical transition or uniform large-count transition estimates with the response preparation/readout problem. All fixed finite n>=2 local transitions, quadratic gain and value regularity are now covered, together with the separately certified count-two half-score consumer. No claim of a full all-score global frontier is made.

[K2587](k2587-countwise-stopping-support-2026-11-05.md), [K2593](k2593-countwise-convex-stopping-2026-11-06.md), [K2595](k2595-stopping-parameter-stability-2026-11-06.md), [probe](../../tests/channel-swings/k2597_stopping_threshold_bifurcation_probe.py), [report](../../lab/process/k2597-stopping-threshold-bifurcation.json).
