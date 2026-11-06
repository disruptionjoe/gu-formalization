---
title: "K2591 Exact mixed positive-action stopping frontier near budget three"
status: active_research
doc_type: exploration
created: "2026-11-06"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: exact implicit optimizer on one mixed resource segment at fixed score and multiplier; not all positive-action budgets
scripts:
  - tests/channel-swings/k2591_multistage_stopping_support_probe.py
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
result: K2591
carrier: original fair stopping schedules and adaptive-policy mixtures at S=1/2 lambda=11/20 LAYER=toy CHIRALITY=N/A
pairing: unconditional success minus leakage with expected positive-trial budget ON=declared_carrier
real_structure: real controls and private randomization
grading: score, first action, stage count and expected trials distinguished
action_owner: repository-construction -- supplied conditional probability model
target: exact implicit mixed one/two-stage resource optimizer MAP-TYPE=evaluation
```

# Replace the failed chord by its actual positive-action optimizer

## Result and prior credit

At S=1/2 and lambda=11/20 there is a UNIQUE price kc in [11/1250,89/10000] at which the optimal one-stage and optimal two-stage policies tie. Every larger stage count is strictly inferior throughout this price window. The two-stage optimizer has a positive FIRST action, zero last action and unequal scores. At kc their resources satisfy R1<2<3<7/2<R2<4. Mixing these two policies is the EXACT original-policy optimum for every resource M in [R1,R2]. In particular the previously unresolved budget3 value is now characterized exactly by a finite convex problem and a unique scalar crossing, with a rigorous rational enclosure of width less than 10^-24:

    kc approximately .00886209863199932675637,
    F(3) approximately .83939516168723973943494.

The decimals are displays of certified enclosures, not floating-search acceptance. The probe reports rational bounds. K2589 previously bounded F(3) in a width51e-6 interval; K2587 already owns sharp zero-action chord thresholds, and K2561 the unrestricted value. Neither is new here. This is independent mathematics, not native GU probability or physical positivity. SC-META-53 remains UNCERTAIN; source, ledger0.263 and canon do not change. No novelty or external certification is claimed.

## 1. Original law and a uniform exclusion of all counts m>=3

Reuse K2569 completed schedules with b_i>0, 0<=a_i<=b_i, sum b_i=S,

    P_i=product_(j<=i)(1+a_j)^-1, p=P_m,
    C=2 sum P_i w(a_i,b_i), R=2 sum P_i,
    w(a,b)=log[1+(b-a)^2/(2(a+b)(2-a-b))].

K2581 proves joint convexity of w on this triangle, and K2587 proves

    sum w >= H_m-c(S/m)A+A^2/(8S), A=sum a_i,
    H_m=m w(0,S/m), c(b)=2(3-2b)/[(2-b)(4-b)].

Since P_i>=p, for N=1-2lambda sum w-2km we have J=p-lambda C-kR<=p N. If N<=0 abort dominates; only if N>0 use p<=1/(1+A). This necessary sign split is retained.

For k in I=[.0088,.0089], convexity of H_m and k_min>lambda(H3-H4) give J_m=1-2lambda H_m-2km<=J3(k_min) for ALL m>=3. Also c(S/m)<=c(1/4)=16/21. Put B=2lambda*16/21 and D=lambda/(4S)=11/40. Then

    J <= max(0, [J3+B A-D A^2]/(1+A))
      <= J3+(B-J3)_+^2/(4D) < .802.             (1)

For the second inequality rewrite the fraction as J3+[(B-J3)A-DA^2]/(1+A). If the added numerator is negative it is <=J3; otherwise remove its denominator and maximize the parabola. The probe bounds J3 and logs by rational intervals. An actual one-stage candidate is >.8127 throughout I (it suffices to check k_max). Thus every m>=3 is uniformly excluded, without a finite-count truncation assumption. K2569's adaptive reduction and mixing lift every support inequality to the original policy class, including integrable randomized mixtures. Infinite nonintegrable costs cannot improve a positive priced value.

## 2. Exclude extreme score splits, then eliminate the last action

For two stages write b=b1 and b2=S-b. The exact global bound c(b)<191/250 follows from

    191(2-b)(4-b)-500(3-2b)=191b^2-146b+28>0;

its discriminant is -76. The quadratic bound above, without equal-score Jensen, gives

    sum w >= w(0,b)+w(0,S-b)-(191/250)A+A^2/(8S).

Outside b in [3/20,7/20], convexity and symmetry of w(0,b)+w(0,S-b) bound its minimum by the value at3/20. Use k_min and the same parabola estimate as(1): J<.812. The zero-action two-stage policy itself exceeds .8126 at k_max and hence throughout I. These splits therefore cannot maximize even within the two-stage class anywhere in I.

Inside this interval, b2<=7/20. For a suffix of score b2 the one-stage derivative at a2=0 is nonpositive if

    lambda[2c(b2)+2w(0,b2)] <= 1-2k.

The stronger bound lambda[2(191/250)+2w(0,7/20)]<1-2k_max holds strictly. Fixed-score strict convexity makes its derivative numerator strictly decreasing with a2. Consequently its unique optimal last action is a2=0. This is conditional optimization of the exact suffix inside the survival-weighted objective; it is NOT an assumption that general schedules have only one action. The remaining first action is denoted a.

## 3. Exact finite-dimensional price value

For EVERY k in I the global value is therefore

    Q(k)=max(Q1(k),Q2(k)),
    Q1=max_(0<=a<=S) [1-2lambda w(a,S)-2k]/(1+a),
    Q2=max_(3/20<=b<=7/20,0<=a<=b)
                  [1-2lambda(w(a,b)+w(0,S-b))-4k]/(1+a).   (2)

Abort lies strictly below. Both maxima are attained on compact domains. They are unique: at a positive optimum Q the equivalent supporting function

    Phi1=2lambda w(a,S)+Q(1+a)+2k-1,
    Phi2=2lambda(w(a,b)+w(0,S-b))+Q(1+a)+4k-1

is strictly convex. Joint convexity of w, strict fixed-b action convexity and strict convexity of w(0,S-b) suffice for the second statement, including the boundary. Hence the optimum is equivalently the unique zero minimum of Phi. Interior stationary equations are

    2lambda w_a(a1,S)+Q1=0,
    2lambda w_a(a2,b)+Q2=0,
    w_b(a2,b)-w_0'(S-b)=0.                       (3)

One may use (2) as the exact definition without presuming interior solutions; the derivative signs below establish interiority at the crossing.

Every maximizing two-stage first action is <1/3. Indeed the uniform equal-score quadratic majorant with c<=191/250 is decreasing for A>=1/3 and is <.80 at1/3, while the two-stage class has its own feasible floor >.8126. The stronger released check at A=1/7 gives the same decreasing majorant <.812<.8126, so in fact every optimizer has a2<1/7. Therefore R2=4/(1+a2)>7/2, whereas R1=2/(1+a1)<=2. Globally on the compact two-stage domain R2>=80/27, so comparing the affine-in-k policy values at any two prices shows Q1-Q2 is strictly increasing with slope at least26/27 in the difference-quotient sense. No differentiability or finite-policy assumption is needed for this envelope argument.

Rational tangent certificates prove Q2>Q1 at k_min and Q1>Q2 at k_max. There is exactly one crossing kc by continuity. At kc the one-stage derivative at0 is positive, and the two-stage derivative at a=0,b=S/2 is positive; the probe certifies both throughout the narrow kc bracket. Thus both first actions are positive. The score boundaries are excluded by the strict <.812 bound. At a=b the action derivative of Phi2 is Q>0, so moving inward decreases it. At a=0 the unique score minimizer is b=S/2 and its action derivative is Q-2lambda c(S/2)<0. Thus the two-stage optimizer is interior. The displayed score is an approximation, not a rational exact maximizer.

The unequal-score assertion has an exact discriminator, not just a numerical witness. At b=S/2=1/4,

    w_b(a,1/4)-w0'(1/4)
      =-64a(128a^3-2192a^2+2824a+5)
        /[105(4a-7)(4a+1)(16a^2-40a-15)] <0

for 0<a<=1/4. The denominator is positive and the cubic is at least (2824-548)a+5>0. Thus the true positive-action interior optimum cannot have equal scores. The probe transfers its positivity upper bound to the entire crossing interval by Qc<=Qupper+4*radius; reduced-policy resources are at most4.

At kc, mixing the two optimizers with theta=(R2-M)/(R2-R1) gives resource EXACTLY M and success-minus-leakage Qc+kc M. The global support(2) proves equality with the constrained optimum for ALL M in [R1,R2], including M=3. Positive kc validates an inequality budget R<=M. This closes a failed post2 interval, not all budgets or multipliers.

## 4. Rational support certificates and an actual feasible consumer

No numerical maximizer supplies an upper bound. At a rational candidate x, let J_hi enclose its priced value from above. For Phi at Q=J_hi, compute the exact rational derivative(s), g. Set

    epsilon=2 sum |g_i|+10^-40, Qbar=J_hi+epsilon.

Every coordinate displacement in the domain has absolute value<=1/2. Raising Q adds epsilon to the a derivative and increases Phi(x) by epsilon(1+a). Convexity therefore gives Phi>=epsilon(1+a)-[sum|g_i|+epsilon]/2>0 everywhere. Thus Qbar is a GLOBAL upper bound. The candidate itself supplies the lower bound. Logarithms use positive rational atanh series with a proved geometric tail. These are explicit convex supporting planes, not sample-grid evidence.

At the rational price .008862098631999326756366633770 use the rational actions and score recorded in the probe (30 decimal places). Apply the certificate independently to Q1 and Q2. Uniform exclusions(1) and section2 make max of these upper bounds global. A mixture of the actual rational one-stage and two-stage policies has exact resource3; it gives a lower bound. The resulting width is <10^-24. This proves the displayed F value independently of irrational optimizer evaluation. The interval for Q1-Q2 and its slope26/27 also gives a rigorous kc enclosure. The zero-action-two-stage shortcut fails an explicit positive first-action derivative control; the optimized two-stage score is not silently forced equal.

## 5. Released consumers, scope and next work

The same rational one/two-stage mixture construction is executed at budgets5/2 and7/2. The released action cutoff a2<1/7 proves R2>7/2, while R1<2. Thus both lie in the EXACT optimal segment, and the same support/feasible pair encloses their values to width<10^-24. This uses the new resource-separation proof; numerical near equality alone would not establish segment membership.

General multipliers, further low-price transitions and all remaining failed chords are open. Carry the proved count reduction and convex support method into those questions rather than requeueing this budget3 optimum. Existing K2589 high-price and K2587 sharp zero-action regions remain unchanged.

[K2589](k2589-positive-action-support-2026-11-05.md), [K2587](k2587-countwise-stopping-support-2026-11-05.md), [K2581](k2581-score-sensitive-tail-transition-2026-11-05.md), [K2569](k2569-stopping-maximizing-sequences-2026-11-05.md), [probe](../../tests/channel-swings/k2591_multistage_stopping_support_probe.py), [report](../../lab/process/k2591-multistage-stopping-support.json).

Independent read-only field specialists and a distinct integrated hostile reviewer found no remaining substantive defects after proof and control repairs. K2590 passes27 exact supporting checks and12 contrary controls; K2591 passes34 and7. Universal domain/adjoint and all-policy arguments remain distinct from symbolic identities, rational support certificates and finite consumers. No external-expert, proof-assistant, remote-CI or physical certification.
