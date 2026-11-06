---
title: "K2593 Complete fixed-multiplier stopping frontier"
status: active_research
doc_type: exploration
created: "2026-11-06"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: exact all-budget frontier only at S=1/2 lambda=11/20; no parameter-uniform or physical result
scripts:
  - tests/channel-swings/k2593_countwise_convex_stopping_probe.py
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
result: K2593
carrier: original fair stopping schedules and adaptive-policy mixtures at S=1/2 lambda=11/20 LAYER=toy CHIRALITY=N/A
pairing: unconditional success minus leakage with expected positive-trial budget ON=declared_carrier
real_structure: real controls and private randomization
grading: score, first action, stage count and expected trials distinguished
action_owner: repository-construction -- supplied conditional probability model
target: complete fixed-parameter resource frontier MAP-TYPE=evaluation
```

# Complete the fixed-multiplier frontier, including the second transition

## Result and scope

For the ORIGINAL fair stopping law at S=1/2 and lambda=11/20, the finite expected-resource frontier is now characterized exactly for EVERY budget M>=0. It consists of an abort mixture, a pure one-stage curve, the K2591 mixed one/two segment, a pure two-stage curve with unequal scores, a NEW mixed two/three segment, and K2587's existing zero-action tail. The two-stage branch and second transition close the remaining gaps. The new crossing is

    kd approximately .00254675025157832772072144165383758231.

Actual policies at budgets4,5,11/2 have rigorous upper/lower enclosures of width below10^-40; at budget5 the value is approximately .8507624332646700090982740. A pure two-stage interior consumer is also enclosed. These decimals display rational certificates, not optimizer acceptance.

This is independent mathematics in a supplied probability model. SC-META-53 remains UNCERTAIN; source, ledger0.263 and canon do not change. No physical probability, GU positivity, new external evidence or novelty is asserted. K2591 owns the first mixed transition, K2589 the high-price one-stage region, K2587 the sharp tail, and K2569 the original-adaptive-policy reduction. Their unchanged proofs are reused, not counted as new tests.

## 1. Original law and all-count majorant

Completed schedules have b_i>0, 0<=a_i<=b_i, sum b_i=S,

    P_i=product_(j<=i)(1+a_j)^-1, p=P_m,
    C=2 sum P_i w(a_i,b_i), R=2 sum P_i,
    w(a,b)=log[1+(b-a)^2/(2(a+b)(2-a-b))].

Write w0(b)=log[(4-b)/(4-2b)] for 0<=b<=S, including w0(0)=0 by continuity. Let H_m=m w(0,S/m), c(b)=2(3-2b)/[(2-b)(4-b)],
J_m(k)=1-2lambda H_m-2km, A=sum a_i and D=lambda/(4S)=11/40.
K2587's universal estimate is

    p-lambda C-kR <= max(0,N_m(A)/(1+A)),
    N_m=J_m+2lambda c(S/m)A-D A^2.             (1)

The max shorthand retains the essential sign split: only when the preceding numerator is positive may product(1+a_i)>=1+A be used to upper-bound p. It does not upper-bound a negative numerator in that way. For J>0 and B>=0,

    (J+B A-D A^2)/(1+A)
       <= U(J,B):=J+(B-J)_+^2/(4D).           (2)

Write the quotient as J+[(B-J)A-DA²]/(1+A); if the added numerator is negative it is at most J, otherwise discard its denominator and maximize the parabola. The inequalities below have positive J floors, so the abort branch also lies below them.

## 2. A broad price reduction, not a finite count truncation

Use I=[127/50000,89/10000]=[.00254,.0089]. The following finite endpoint certificates have UNIVERSAL consequences.

**All m>=4.** Convexity of H_m and k_min>lambda(H4-H5) imply J_m<=J4 for every m>=4. Also c(S/m)<=c(1/8), by monotonicity on[0,1/4]. Bounding the numerator in(1) directly by J4+B4 A-DA², B4=2lambda c(1/8), gives U(J4,B4). The difference U(J4(k),B4)-J2(k) is convex in k: the linear terms are affine and the squared positive part of an affine function is convex. It is strictly negative at BOTH endpoints of I, as the rational probe proves. A convex function is bounded above by its endpoint chord, so every count m>=4 is inferior to the feasible zero-action two-stage policy throughout I. No unexamined large count remains.

**Two-stage extreme scores.** Put b=b1 and b2=S-b. Outside[3/20,7/20], strict convexity and symmetry of w0(b)+w0(S-b) bound its minimum by Hout=w0(3/20)+w0(7/20). The exact inequality c(b)<191/250 on[0,1/2] follows from the positive quadratic191b²-146b+28, whose discriminant is-76. The general fixed-score curvature bound gives sum w>=Hout-(191/250)A+A²/(8S). The same convex endpoint argument proves U(1-2lambda Hout-4k,2lambda191/250)<J2 throughout I. Hence every two-stage optimizer has b strictly inside[3/20,7/20].

In that interval the exact suffix derivative satisfies

    2lambda[191/250+w0(7/20)]<1-2k_max.

Fixed-score strict convexity makes its derivative numerator strictly decreasing with the suffix action. Therefore the unique final action is ZERO for every maximizing two-stage policy throughout I. This is a consequence of the actual survival-weighted suffix problem; it is not an assumed restriction on all policies.

**Count three.** On[k_min,.003], J3(.003)>2lambda c(1/6), so (1) makes the zero-action equal-three policy exactly optimal within its count. On[.003,k_max], U(J3,2lambda c(1/6))-J2 is convex and negative at both endpoints, hence ALL three-stage policies are inferior to zero2 there. Thus throughout I the global original-policy price value is exactly

    Q(k)=max(Q1(k),Q2(k),J3(k)),               (3)
    Q1=max_(0<=a<=S) [1-2lambda w(a,S)-2k]/(1+a),
    Q2=max_(3/20<=b<=7/20,0<=a<=b)
           [1-2lambda(w(a,b)+w0(S-b))-4k]/(1+a).

Even when J3 is dominated it is feasible, so its inclusion in(3) is harmless. Abort is strictly below J2 on I. K2569's completed-schedule reduction and integration extend these supports to the original adaptive and randomized policy class, not just a chosen finite family. Infinite nonintegrable cost cannot beat a positive-price finite policy.

## 3. Two unique crossings and no missing price interval

Both Q1 and Q2 have unique optimizers by the convex supporting-function argument of K2591. For Q2, the cost W(a,b)=w(a,b)+w0(S-b) is strictly convex: fixed-score w is strictly convex in a and w0 is strictly convex in its score; its positive semidefinite Hessian plus this second contribution is positive definite in the interior. The denominator has been handled by the positive optimum's supporting function, not by declaring a quotient convex.

For every two-stage reduced policy, R2=4/(1+a)>=80/27>2>=R1; thus Q1-Q2 is strictly increasing with difference-quotient slope at least26/27. K2591's certified crossing kc in[.0088,.0089] is therefore the only such crossing throughout I.

Also R2<=4<6=R3, so Q2-J3 is strictly increasing with difference-quotient slope at least2. New rational tangent certificates give Q2<J3 at.00254 and Q2>J3 at.00255. Hence there is exactly one kd between them. The exact root is defined by Q2(kd)=J3(kd); no rounded number defines the theorem. Since kd<kc, Q1<Q2 at kd. Thus the active branches on I are zero3, pure2, pure1, with only the two specified ties.

The intervals outside I are covered, too. k*=lambda(H1-H2) lies STRICTLY inside I near.008890715. K2589 therefore covers all higher prices with one-stage-or-abort support. At k3=lambda(H3-H4)<k_min, K2587 proves zero3 globally supported, since lambda<lambda3(S). The same fixed zero3 policy is globally supported at kd. Every competing policy's value difference is affine in price, so endpoint comparison supports zero3 throughout[k3,kd]. K2587 supplies every lower-price count interval and the tail. For k>=1/2 abort is optimal; at k=1/2 the zero-leakage one-stage policy also ties. These overlaps leave no uncovered positive price.

## 4. Exact frontier for every finite budget

Let ai_c and b_c denote the unique optimizing actions/scores at kc; let a2_d,b_d denote those at kd. Define R1c=2/(1+a1_c), R2c=4/(1+a2_c), R2d=4/(1+a2_d), Qc=Q(kc), Qd=Q(kd). Then

| Budget M | Exact optimum F(M) |
|---|---|
| 0<=M<=4/3 | M/2 |
| 4/3<=M<=R1c | M/2-lambda M w(2/M-1,S) |
| R1c<=M<=R2c | Qc+kc M |
| R2c<=M<=R2d | M/4-(lambda M/2) min_b [w(4/M-1,b)+w0(S-b)] |
| R2d<=M<=6 | Qd+kd M |
| 2n<=M<=2n+2, n>=3 | 1-2lambda[(1-theta)H_n+theta H_(n+1)], theta=(M-2n)/2 |

The minimum in the pure2 row is over a<=b<=S (equivalently the proved interior interval for this branch), and it has a unique minimizer. Adjacent rows agree at their endpoints.

Here is why the table gives attained original-policy optima, not just a concave upper envelope. On[kd,kc] the Q2 optimizer is interior. At a=0 the unique b minimizer is1/4 and the action derivative of its supporting function is J2(k)-2lambda c(1/4)<0; the probe's endpoint inequality at k_min implies this throughout the interval. At a=b the action derivative is Q2>0, and the score endpoints are excluded above. Uniqueness and compactness make a(k),b(k) continuous. The optimal resource is nonincreasing in price by comparing the two optimal affine supports. It is STRICTLY decreasing: if two prices had the same a, strict score minimization would give the same b, whereas the interior equation

    4k=1-2lambda W+2lambda(1+a)w_a(a,b)       (4)

forces the prices equal. Hence R2(k) continuously covers[R2c,R2d] and each pure2 row is supported at a positive price. The same one-stage argument covers[4/3,R1c]. At a tie, mix its two actual optimizing policies with theta=(Rright-M)/(Rright-Rleft), so the expected resource is exactly M and support equality holds. The first row mixes abort with a=S zero-leakage one-stage. The tail uses the already-proved equal-count mixtures. Positive supporting prices prove optimality also for the inequality budget R<=M.

This is a COMPLETE fixed-parameter frontier, not a theorem for every multiplier. It is not a claim that every admissible adaptive policy itself has at most three stages: the support reduction bounds all of them and exhibits attaining policies; the tail uses arbitrarily large finite counts as M grows.

## 5. Exact certificates and released consumers

Logarithms use rational atanh series with an explicit geometric remainder, outward rounded to65 decimal places. At a rational candidate for Q2, set a convex supporting function Phi=2lambda W+Q(1+a)+4k-1. Its exact rational gradient plus the interval upper bound on candidate value supplies a global tangent upper bound, exactly as in K2591. Small gradients are not treated as optimality without this convex bound. The slope>=2 for Q2-J3 converts interval disagreement into the kd enclosure of width below10^-40.

Mix the rational two-stage policy at the displayed kd approximation with the ACTUAL equal-score zero-action three-stage policy. At M=4,5,11/2 the rational mixing weight gives exact budget, and the global support gives a value bracket below10^-40 width. Each improves the old failed zero2/zero3 chord STRICTLY. The two-stage resource is approximately3.9999658168713063935365; using4 in the mixture formula would lose the exact budget. The previous chord's tiny failure is real, not floating noise.

At the EXACT budget399/100, choose a=1/399 and the rational score b approximately .25033758242444017891390. The supporting rational price is approximately .00734521535627247415550, strictly between the certified crossing brackets. The actual two-stage policy has resource399/100 identically; its global-support/actual-value bracket has width below10^-40, near .8481662152042137414778246. Thus the new branch was consumed beyond the second tie itself, with no floating-budget substitution.

## Verification and next research

The probe verifies the endpoint inequalities that drive the universal convex/count arguments, original-law mixtures and interval values. Contrary controls retain failures from zero-action/equal-score shortcuts, wrong survival or stage costs, wrong mixture weights and a reversed negative-numerator inequality. Finite controls are separate from the written all-policy and attainment proofs. The fixed-(S,lambda) gaps are closed; do not requeue them as absent. The remaining question is parameter stability and changing count topology outside this fixed pair, compared with the source-response boundary problem. Neither mathematical result chooses a physical model.

[K2591](k2591-multistage-stopping-support-2026-11-06.md), [K2589](k2589-positive-action-support-2026-11-05.md), [K2587](k2587-countwise-stopping-support-2026-11-05.md), [K2569](k2569-stopping-maximizing-sequences-2026-11-05.md), [probe](../../tests/channel-swings/k2593_countwise_convex_stopping_probe.py), [report](../../lab/process/k2593-countwise-convex-stopping.json).

Independent read-only field specialists and a distinct integrated hostile reviewer found no remaining substantive findings after scope and probe repairs. K2592 passes50 exact supporting checks and9 contrary controls; K2593 passes41 and6. Universal boundary, spectral-synthesis, convexity and all-policy proofs remain separate from algebraic fixtures, interval certificates and actual finite consumers. No external-expert, proof-assistant, remote-CI or physical certification.
