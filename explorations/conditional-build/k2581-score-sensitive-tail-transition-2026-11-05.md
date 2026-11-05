---
title: "K2581 The exact equal-stage resource-tail transition"
status: active_research
doc_type: exploration
created: "2026-11-05"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: sharp full-tail transition for every score up to one-half; no full middle-resource or intermediate optimizer
scripts:
  - tests/channel-swings/k2581_score_sensitive_tail_transition_probe.py
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
result: K2581
carrier: original fair stopping law with finite completed schedules and initial mixtures LAYER=toy CHIRALITY=N/A
pairing: unconditional expected success, leakage and positive-trial functional ON=declared_carrier
real_structure: real controls and multiplier; probability laws and private randomization
grading: stages, expected positive trials and pathwise trial counts kept distinct
action_owner: repository-construction -- stated conditional model
target: score-sensitive global support and exact transition MAP-TYPE=evaluation
```

# Score sensitivity closes the stopping transition

## Result and scope

The former narrow transition bracket is closed exactly. Joint convexity and a score-sensitive action bound prove the equal-stage expected-resource tail globally through its old upper endpoint, including equality. The proof extends to every total score 0<S<=1/2. Beyond that endpoint an actual budget-restored policy defeats the first chord. Released consequences include an exact new budget3 optimum, tangent contact at the critical resource2 corner, and ordered count-specific failure thresholds.

This is independent probability mathematics for the supplied fair stopping law. SC-META-53 remains UNCERTAIN; source/ledger0.263, canon and physical claims do not change. Expected positive trials are not a pathwise cap. No general intermediate-multiplier optimizer, enlarged middle-budget formula, native GU inference or novelty is claimed.

## 1. Exact objects and statement

Fix 0<S<=1/2 and lambda>0. A finite completed schedule has 0<b_i, 0<=a_i<=b_i, sum b_i=S,

    P_i=product_{j<=i}(1+a_j)^(-1),
    p=P_n, C=2 sum P_i w(a_i,b_i), R=2 sum P_i,
    w(a,b)=log(1+(b-a)^2/[2(a+b)(2-a-b)]).

Abort has value0. Q(lambda,k,S) is the supremum of p-lambda C-kR for k>0. F(lambda,M,S) is the constrained original-policy supremum with R<=M. K2569's reduction preserves precisely these original adaptive quantities; K2571 gives a finite optimizing schedule or abort at positive k. Thus the finite optimizer used below is not an assumption excluding adaptive or countable strategies.

Set

    w0(b)=log((4-b)/(4-2b)),
    c(b)=-w_a(0,b)=2(3-2b)/[(2-b)(4-b)],
    H_n=n w0(S/n), Delta_n=H_n-H_(n+1)>0,
    Lambda(S)=1/[2c(S)+4H_1-2H_2].

THEOREM: For every 0<lambda<=Lambda(S) and every M>=2,

    F(lambda,M,S)=1-2lambda[(1-alpha)H_n+alpha H_(n+1)],
    n=floor(M/2), alpha=(M-2n)/2.

Moreover Lambda(S) is the EXACT largest multiplier for which this formula holds simultaneously for all M>=2. Equality belongs to the valid regime. This does not solve the entire constrained frontier for larger multipliers, nor the middle budgets for this enlarged multiplier range.

At S=1/2,

    Lambda=1/[32/21+4log(7/6)-4log(15/14)]
          =0.5363538616895924...,

so the existing K2579 upper bound is sharp.

## 2. Joint convexity on the ACTUAL control triangle

Use t=a+b, d=b-a, N=2t(2-t)+d^2. On 0<=a<=b<=1/2, 0<t<=1 and 0<=d<=t. Here w=log N-log[2t(2-t)]. Exact differentiation gives

    det Hess_(a,b) w = 16 d^2 P / [t^2(2-t)^2 N^3],
    P=2t^2(2-t)^2-d^2(t^2-2t+2).

Since t^2-2t+2>0 and d^2<=t^2,

    P>=t^2(t^2-6t+6)>0  (0<t<=1).

Together with the inherited w_aa>0 this proves Hessian positive definite when a<b, and positive semidefinite at a=b. Therefore w is jointly convex on the triangle away from the origin, and its continuous extension w(0,0)=0 is convex on the closed triangle. Indeed w<=b/2 supplies continuity at the origin. This is a two-dimensional statement, stronger than fixed-b convexity; the latter alone would not justify the following tangent plane.

At every b0>0, the supporting plane is

    w(a,b)>=w0(b0)-c(b0)a+w0'(b0)(b-b0).

It is STRICT when a>0. Along the segment leaving (0,b0) toward (a,b), the Hessian is positive definite on an initial nonempty interval (a<b there); hence the first-order Taylor remainder is positive. The endpoint a=b causes no exception. No differentiability at the origin is used.

The exact probe verifies the determinant identity after rational simplification. This identity and the domain inequality carry joint convexity; a finite sample would not.

## 3. Score-sensitive action exclusion reduces a global optimizer to one positive action

Let k_1=lambda Delta_1, and assume 0<k<=k_1. A single zero-action stage proves

    Q>=J_1=1-2lambda H_1-2k
           >=1-lambda(4H_1-2H_2)
           >=2lambda c(S)>0.

The last inequality is exactly lambda<=Lambda(S). Thus abort cannot optimize. Select a finite maximizing schedule from K2571 and remove zero-score stages (they are not actual positive trials; the canonical finite schedule has b_i>0).

Let V_i denote the priced suffix value starting at stage i. Every V_i>=Q: preceding maps x -> (x-2lambda w-2k)/(1+a) strictly decrease a positive x, while a nonpositive suffix cannot lead to a positive full value. Holding b_i and every other control fixed,

    partial_(a_i) V_i = [-2lambda w_a(a_i,b_i)-V_i]/(1+a_i).

If a_i>0, optimality against a small feasible DECREASE requires this derivative >=0, including the upper boundary a_i=b_i. Strict fixed-b convexity gives -w_a(a_i,b_i)<c(b_i). Hence

    2lambda c(b_i)>V_i>=Q>=2lambda c(S),

so c(b_i)>c(S).

Now c'(b)=4(b^2-3b+1)/[(b-4)^2(b-2)^2]>0 on [0,1/4], and

    c(S)-c(S/2)
      = 2S(2S-1)/[(S-8)(S-4)(S-2)] >=0.

Therefore c(b_i)>c(S) forces b_i>S/2. There can be AT MOST ONE positive action in the entire maximizing schedule, since total score is S. This argument covers Lambda equality because a_i>0 supplied strictness. At S=1/2 it specializes to

    c(b)-16/21=-2(2b-1)(4b-1)/[21(b-4)(b-2)],

so a positive action would need b>1/4.

## 4. Exchange places that sole action FIRST

For stages A,B with c_A=lambda w_A+k and c_B=lambda w_B+k, the adjacent value difference is

    J(AB)-J(BA)=2(a_A c_B-a_B c_A)/[(1+a_A)(1+a_B)]

times their common positive prefix. The downstream suffix cancels. If A has positive a and B has a=0, c_B>=k>0, so A-before-B is strictly better. Thus a maximizing schedule with one positive action puts it first. It is not harmless to put it last: that would change all survival/resource weights.

If its positive action is a, ALL P_i=1/(1+a). Its total value is therefore

    J=[1-2lambda sum_i w(a_i,b_i)-2kn]/(1+a).

Use the convex supporting plane from section2 at b0=S/n for each stage. Summing cancels the b derivatives since sum_i(b_i-S/n)=0 and sum_i a_i=a. Thus

    sum_i w(a_i,b_i)>H_n-c(S/n)a.

Also c(S/n)<=c(S): n=1 is equality; n>=2 follows c increasing on [0,S/2] and c(S/2)<=c(S). Consequently

    J < [J_n+2lambda c(S/n)a]/(1+a)
      <=[J_n+2lambda c(S)a]/(1+a)
      <=Q_0,

where J_n=1-2lambda H_n-2kn and Q_0=max_{r>=1} J_r. The last inequality uses J_n<=Q_0 and 2lambda c(S)<=J_1<=Q_0. Since Q>=Q_0 by feasibility, a global maximizing schedule with a>0 is impossible.

Thus EVERY finite global optimizer has all a_i=0. Strict Jensen then forces equal scores at a fixed count. This proof does not merely find a zero-action optimizer; it excludes all positive-action finite maximizers in this price range.

## 5. Global constrained tail and sharpness

K2577 proves H(t)=t w0(S/t) is strictly decreasing and convex, with Delta_n strictly decreasing to0. Therefore k_n=lambda Delta_n<=k_1. At k=k_n exactly the zero-action equal n and n+1 schedules maximize Q_0. Since the previous proof gives Q=Q_0 for every such k, their mixture at R=M supplies a global support certificate for every original policy, including initial randomization, abandonment and the admissible infinite-policy limits handled by K2569. This proves the displayed F formula.

For lambda>Lambda(S), K2579's first-action perturbation of the one-stage policy has derivative of J-k_1 R at a=0 equal to

    lambda[2c(S)+4H_1-2H_2]-1>0.

For sufficiently small positive epsilon<=S, the perturbed one-stage policy has R=2/(1+epsilon)<2 and strictly exceeds the old support. Mix it with the unchanged two-stage policy, whose R=4, to attain ANY M in [2,4). The exact K2579 repair weight and positive excess multiplier yield a strict feasible improvement over the old chord. Thus no larger lambda can preserve the ENTIRE tail. At equality the previous global proof, not the vanishing derivative, supplies validity.

This proves a sharp FULL-TAIL transition; it does not say every budget loses its old formula simultaneously above the transition.

## 6. Released consumers

### A. Exact budget3 beyond the old lower bound

At S=1/2, lambda=67/125=.536, M=3, choose with equal probability the one-stage a=0,b=1/2 and two-stage a=0,b=1/4 policies. Then

    p=1, R=3, C=log(7/6)+2log(15/14),
    F=1-(67/125)[log(7/6)+2log(15/14)],
    supporting k=(67/125)[log(7/6)-2log(15/14)].

Exact Fraction logarithm enclosures (12 positive series terms and rigorous geometric tail) executed:

    843414877378/10^12 < F < 843414877380/10^12,
    F approx .8434148773785776,
    k approx .008664406153398495,
    67/125<Lambda (certified rational comparison).

Use log r=2 sum_{j=0}^{11}u^(2j+1)/(2j+1)+tail, u=(r-1)/(r+1), 0<tail<=2u^25/[25(1-u^2)]. These values are actual original-law probabilities and failure-inclusive costs, not an unweighted leakage proxy. The exact threshold enclosure can be sharpened to any desired rational width with the same series; no extra precision is scientifically necessary.

A second exact original-law consumer uses S=1/4, lambda=59/100 and M=3: mix equally one stage b=1/4 and two stages b=1/8, all actions zero. The probe certifies lambda<Lambda(1/4), expected trials3, and value1−(59/100)[log(15/14)+2log(31/30)]. This exercises the released general-score theorem.

### B. Critical corner is differentiable at M=2

For general S, the feasible one-stage curve on [2/(1+S),2] is

    G(M)=M/2-lambda M w(2/M-1,S).

It touches F(2)=1-2lambda H_1. Its left derivative at2 is

    G'(2-)=[1-lambda(2c(S)+2H_1)]/2.

At lambda=Lambda(S), this equals k_1=lambda(H_1-H_2), the EXACT right slope of F's first tail chord. Initial randomization makes F concave. Since F>=G with equality at2, its left derivative is at most G'(2-); concavity bounds it below by the right derivative k_1. Hence

    F'(2-)=F'(2+)=k_1  at lambda=Lambda(S).

This proves first-order tangent contact at the critical corner without claiming G=F on the whole middle interval. For lambda<Lambda it only yields k_1<=F'(2-)<=G'(2-), not exact middle optimality. For S=1/2 the full middle formula still retains K2575's independently proved multiplier range.

### C. Ordered count-specific failure thresholds

Define the existing K2579 thresholds

    lambda_n=1/D_n,
    D_n=2c(S/n)+2T_n,
    T_n=(n+1)H_n-nH_(n+1).

Then

    T_n-T_(n+1)=(n+1)[H_n-2H_(n+1)+H_(n+2)]>0.

The c(S/n) sequence is nonincreasing: the n1-to-n2 step follows the exact factor above; later terms strictly decrease because c increases on [0,S/2]. Therefore D_n strictly decreases and lambda_n strictly increases. K2579's limits give

    lambda_1=Lambda(S)<lambda_2<... -> 2/(3+S).

This orders the inexpensive first-action breakdown tests for every count. It does NOT establish that lambda_n is the exact transition at its individual budget/chord; other perturbations could win earlier. At S=1/2 it gives a strictly increasing sequence from .536353... to4/7.


## Controls and remaining frontier

The probe independently differentiates the joint Hessian, checks the score and exchange identities, and evaluates original-law success/leakage/resource with rigorous rational logarithm bounds. A concrete policy at lambda537/1000 uses first action1/10000, repairs its expected budget to3 by mixing with two zero-action stages, and strictly improves the old chord. This lies just above the new threshold. Controls reject the false global bound c(b)<=16/21, reversed exchange, omitted failure-trial cost, infeasible deterministic replacement, and uncorrected equal mixture weights.

The all-policy theorem rests on the optimizer, convexity, exchange and support proof, not the probe count. The entire-tail transition is solved; exact middle budgets in the enlarged multiplier range and globally certified positive-action policies above the transition remain substantial open questions. Individual count thresholds are sufficient failure tests, not separately proved sharp transitions.

[K2579 upper bound and budget repair](k2579-resource-tail-breakdown-2026-11-05.md), [K2577 support and count convexity](k2577-exact-resource-tail-2026-11-05.md), [K2571 positive-price attainment](k2571-stopping-resource-price-2026-11-05.md), [K2569 original-law reduction](k2569-stopping-maximizing-sequences-2026-11-05.md), [K2509 action convexity](k2509-stopping-atom-certificate-2026-11-02.md), [probe](../../tests/channel-swings/k2581_score_sensitive_tail_transition_probe.py), [report](../../lab/process/k2581-score-sensitive-tail-transition.json). General [constrained occupation-measure theory](https://arxiv.org/abs/2307.03158) is background with different process hypotheses, not proof of this supplied-law threshold.
