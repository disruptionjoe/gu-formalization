---
title: "K2569 Resource-preserving reduction and necessary trial growth"
status: active_research
doc_type: exploration
created: "2026-11-05"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: original-law maximizing-sequence structure and expected positive-trial divergence; no matching lower resource rate or exact intermediate value
scripts:
  - tests/channel-swings/k2569_stopping_maximizing_sequences_probe.py
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
result: K2569
carrier: original predictable fresh fair test/use histories and normalized completed schedules LAYER=toy CHIRALITY=N/A
pairing: unconditional success minus original leakage cost and expected positive-score trial count ON=declared_carrier
real_structure: real probabilities, finite logarithmic costs and compact finite-dimensional controls
grading: trials, use stages, private randomization, abort and finite-hit success remain distinct
action_owner: repository-construction -- supplied fair stopping law
target: resource-preserving schedule reduction and maximizing-sequence complexity MAP-TYPE=evaluation
```

# Approaching the unattained value requires unbounded expected useful trials

## Result and what is new

Fix 0<S<=1/2 and 0<lambda<=98/51. K2567 proves that the original adaptive dual supremum V_lambda(S) is not attained. Nonattainment alone does not prove that approaching it consumes increasing resources. This note proves that every sequence of original policies whose dual values approach V has expected positive-score trial counts tending to infinity. Arbitrary predictable choices, private randomization, aborts and possibly unbounded trial counts remain allowed. Idle trials are not counted as productive work.

The decisive new bridge is a resource-preserving reduction from the original adaptive law to mixtures of finite completed repeated-action schedules. K2483 previously identified their common supremum using Bellman supersolutions; that value identity by itself did not control resources of arbitrary policies. Compact finite-stage maxima and their strict increase now give a noncircular gap modulus. The executed quantitative consumer uses the existing S=1/2, lambda=19/10 certificate to bound the fraction of compressed schedules with at most one stage. An additional executed consumer gives an O(1/eta) sufficient original-policy resource bound by converting compact hybrid approximants; no matching necessary rate, new exact intermediate value, or physical controller cost is claimed.

This is GU-independent mathematics of the supplied law. SC-META-53 remains UNCERTAIN, LT-SM8/LT-GR6b keep their physical-state/domain obligations, and source polarities, ledger0.263 and canon are unchanged.

## 1. Original law and the resource being priced

Use K2483's exact law. A trial chooses predictable a,b in[0,1]. A fresh fair use adds b to accumulated normalized score; a test rejects with conditional probability a and absorbs in failure, otherwise stays. Every trial incurs

    w(a,b)=log(1+(b-a)^2/[2(a+b)(2-a-b)]) if a<b,
    w(a,b)=0 if a>=b.

Success is a FINITE hit of S. Let J=p-lambda C and N_+ count active trials with b>0, including final failures. Private randomness is available as in the original policy class. Infinite expected cost cannot improve a positive V. Policies with E N_+=infinity already satisfy any finite lower bound below. We therefore establish the reduction for finite E N_+.

For a repeated positive-score stage (a,b), geometric summation gives use probability 1/(1+a), expected trials 2/(1+a), and expected cost 2w/(1+a). The cost is unconditional; failure-path costs cannot be discarded.

## 2. Compress an adaptive score epoch without losing its resource account

Pre-sample private randomness, so conditional on it the action chosen after each test pass is deterministic. Until the first use, failure or abort, the all-test-pass branch is a single chain. Write its kth action as (a_k,b_k), with continuation program C_k after a use, and

    r_0=1, r_k=product_(j<k)(1-a_j)/2,
    nu_k=r_k(1+a_k)/2=r_k-r_(k+1).                (1)

At entry, randomly choose label (a_k,b_k,C_k) with probability nu_k, and use the leftover mass for immediate free abort. If a label is chosen, repeat that action until use/failure, then invoke its SAME post-use continuation. Because r_k<=2^-k, the infinite chain has no leftover nontermination mass; a finite chain's leftover is its abort mass. The label retains the entire conditional continuation, not just its score.

For each k,

    compressed use weight =nu_k/(1+a_k)=r_k/2,
    compressed cost       =2nu_k w_k/(1+a_k)=r_k w_k,
    positive-trial count  =2nu_k 1_(b_k>0)/(1+a_k)
                           =r_k 1_(b_k>0).        (2)

These are exactly the original epoch's weights. The original failure weight r_k a_k/2 is preserved too. Iterating conditionally at each continuation preserves total success, cost and positive-trial expectation by nonnegative sums. This includes changing actions after test passes; it does not assume the original policy was stationary at a given score.

If b=0, this stage makes no score and has w=0 for every a. Replace it by a private random choice of its continuation with probability 1/(1+a), otherwise abort. This preserves success/cost, counts zero positive trials, and removes the zero-score stage. Infinite chains of these choices that never progress are non-successful and can be sent to free abort. The original class allows private randomization, so no experimental trial is needed to implement these choices.

## 3. Normalize the surviving schedules and remove incomplete paths

If a>b, w=0. Replace its stage by (b,b), executed with probability (1+b)/(1+a), otherwise abort. Its use weight and positive-trial expectation stay respectively 1/(1+a) and 2/(1+a). If a positive stage overshoots remaining score s, replace b by s and a by a'=min(a,s), with execute probability (1+a')/(1+a). Again use probability and positive-trial expectation are unchanged, while its cost is 2w(a',s)/(1+a)<=2w(a,b)/(1+a) by the original clipping inequality. Stop when the normalized score reaches S.

Pre-sample all stage labels and these abort choices along the hypothetical all-use path. This yields a probability distribution over deterministic normalized schedules, with 0<=a_i<=b_i, b_i>0, and total score at most S, terminating either at a finite hit, at abort, or after infinitely many stages without a finite hit. Failure probabilities still arise from each scheduled geometric stage; the sampled schedule is not conditioned on actual survival.

An incomplete schedule has zero success and nonnegative cost. Replace it by initial free abort; J weakly increases and resources weakly decrease. For an infinite normalized positive-stage schedule,

    P_i=product_(j<=i)(1+a_j)^-1
       >=exp(-sum_(j<=i)a_j)>=exp(-S),             (3)

so its expected positive trials 2 sum_i P_i are infinite. Finite original E N_+ therefore gives such schedules zero mixture mass (Tonelli). After removing finite incomplete schedules, the result is a mixture of finite completed schedules and free abort, with

    J_mix>=J_original, E N_+(mix)<=E N_+(original). (4)

This is a domination result for this objective AND resource, not a bijection of policies or a theorem about every constrained resource frontier. All operations are private randomization and lawful original repeated stages. There is no success assigned to a path that only approaches S at infinity.

## 4. Compact finite-stage maxima have strict successive gaps

Let D_n be the maximum original dual over completed schedules with at most n positive stages, D_0=0. For n>=1 represent them using the compact padded set

    sum_i b_i=S, 0<=a_i<=b_i, i=1,...,n,
    J=product_i(1+a_i)^-1
       -2lambda sum_i w(a_i,b_i)product_(j<=i)(1+a_j)^-1. (5)

Zero b forces zero a; its padded map is the identity and costs zero. It is not executed as a two-trial stage. On the triangle b<=1/2 the logarithm extends continuously at (0,0): its argument increment is at most b/[2(2-b)], hence w=O(b) uniformly. Thus J is continuous on this compact set and D_n is attained. The free a=b=S stage makes D_n>0.

K2567 proves every finite completed schedule can be strictly improved by splitting its last positive stage (or first optimizing that stage, then splitting it). An optimizer for D_n must consequently have exactly n positive stages: otherwise its improvement remains in the n-stage set. Splitting this optimizer gives

    g_n:=D_(n+1)-D_n>0, n>=1; g_0:=D_1>0.        (6)

Every D_n<V, and K2483's least-supersolution theorem supplies D_n increasing to V. This relies on its finite-stage approximation result at the same law and lambda, not on a uniform numerical grid. The g_n are finite-dimensional mathematical quantities, not previously computed constants or an asserted rate.

## 5. Execute the all-adaptive resource and mixture-concentration consumer

For a policy let eta=V-J>=0, and let N denote the number of positive stages in the dominating mixture of (4), with N=0 for abort. Every component with N<=n has J<=D_n and every other component has J<=V. Hence

    (V-D_n)P(N<=n)<=V-J_mix<=eta,
    P(N<=n)<=min(1,eta/g_n).                     (7)

For a completed schedule, E N_+=2 sum_i P_i>=2e^-S N by (3). Therefore, for every finite m,

    E N_+(original)
      >=2e^-S sum_(n=0)^m (1-eta/g_n)_+.         (8)

In particular it is at least 2e^-S(n+1)(1-eta/g_n)_+ for any one n. Both inequalities refer to the original policy's expected resource, even though N describes its compressed mixture. As eta tends to zero, every fixed finite sum in (8) tends to m+1. Letting m be arbitrarily large proves

    J_k -> V  implies E N_+(policy_k) -> infinity. (9)

This is convergence to infinity, not only unboundedness of a subsequence. A policy with infinite resource causes no exception. Free idles do not drive this conclusion: the counted trials make positive score on use. Finite expectation for each approximating policy remains possible; K2483 gives such approximants. Rates such as 1/eta or log(1/eta) are NOT proved, because the gaps g_n have no uniform lower estimate here.

A mere statement that the final hit has a tiny residual would not prove (9): a large preceding stage can leave an arbitrarily small last stage. The compact optimization and resource-preserving bridge address that missing step.

## 6. Executed numerical-certificate consumer, without recomputing old banks

At S=1/2 and lambda=19/10, K2561's certified global one-stage bound gives D_1<0.71. K2565's lawful 41-stage witness gives V>0.711079567311. Therefore the rigorous rational number

    delta_1=1079/1000000

is a lower bound for V-D_1; it is not asserted to bound g_1=D_2-D_1. Equation(7) now gives P(N<=1)<=eta/delta_1. For example, a policy with dual error at most delta_1/10 has at least90% weight on schedules of at least two positive stages in its dominating mixture, hence

    E N_+>= (18/5)e^(-1/2)>2.18.                 (10)

This modest explicit bound is a real original-policy resource statement; it does not price wall time or hardware. For stronger numerical bounds one may certify D_M-D_n>0 for finite M>n, or combine a certified V lower bound with a D_n upper bound. Every such number may replace g_n in (7)--(8) if it is a valid lower bound for V-D_n. Computing it is a separate finite-dimensional optimization task.

## 7. Execute the matching direction: an explicit finite-policy upper resource bound

The divergence theorem leaves the rate open, but K2563's hybrid hierarchy can now be converted into an explicit ORIGINAL-policy stage count. This upper approximation holds for every lambda>0, not only the nonattainment interval. Write g(r)=(1-r)^2/[2(1+r)] and reuse the optimized continuum semigroup C_b(x), with

    C'=-lambda q(C/lambda),
    q(u)=min_(0<=r<=1)[ru+g(r)], 0<=q<=1/2,
    0<=q'<=1 where differentiable.

For nonnegative continuation x<=1, the scalar Euler value E=x-lambda b q(x/lambda) obeys K2563's rigorous bound

    0<=C_b(x)-E<=lambda b^2/4.                    (12)

Choose a minimizing r at x/lambda and a=rb. The original logarithm satisfies 2w(rb,b)=b g(r)+e, 0<=e<=b^2/2 (K2495, reused in K2563). Exact rearrangement gives

    [x-lambda b g(r)-lambda e]/(1+rb)-E
      =[r^2 b^2 x+lambda r b^2 g(r)-lambda e]/(1+rb)
      >=-lambda b^2/2.

Thus the optimized original atom map A_b(x) satisfies

    A_b(x)>=C_b(x)-3lambda b^2/4.                 (13)

A and C are monotone and 1-Lipschitz in continuation value; A is nonnegative because a=b is admissible. Consequently errors add when continuum pieces are replaced backwards through any prefix, including original atoms.

Take a maximizing K2563 hybrid with at most N atoms and N+1 continuum blocks, whose value is at least V-lambda S^2/(4N). Split each positive continuum block into pieces of length at most S/N. Their total number is at most 2N+1: the sum of the ceilings is at most N plus the number of positive blocks. Their squared lengths sum to at most S^2/N. Replace each by its optimized original atom using (13). Retain the original N atom lengths, but reoptimize their a-controls backwards at the new continuation values using A_b. This weakly improves each retained map relative to its former choice, preserves score and atom count, and keeps every intermediate suffix nonnegative as required in (12)--(13). The resulting completed original schedule has at most3N+1 positive stages and dual loss at most

    lambda S^2/(4N)+3lambda S^2/(4N)=lambda S^2/N.

Therefore

    D_(3N+1)>=V-lambda S^2/N,
    some such policy has E N_+<=6N+2.            (14)

Zero pieces are omitted; no continuum endpoint is declared to be a finite hit. This is a finite-policy existence/conversion result given a maximizing hybrid and the scalar atom optimizers. It is not an efficient algorithm to compute that hybrid, and it does not solve the global intermediate value. Choosing N>=lambda S^2/eta gives an O(1/eta) sufficient expected-resource bound, while (9) supplies divergence with no matching rate.

For S=1/2, lambda=19/10 and eta=1/10000, N=4750 suffices: at most14251 original stages and expected positive trials at most28502. These conservative numbers describe a guaranteed approximation class, not a constructed numerical optimizer. The existing41-stage witness has its separately certified error; it does not establish this finer tolerance. The new bound makes a quantitative original-policy search target available without repeating the enormous uniform hybrid grid.

## Verification and strongest contrary cases

The exact probe checks a nonstationary two-attempt epoch, continuation-use weights, expected trials and original logarithmic cost coefficients, preabort normalization, overshoot clipping, actual prefix-weighted stage resources and the rational gap consumer. It changes the actual probability/cost accounting in contrary controls. These finite checks support the formulas; the universal measure, compactness and nonattainment transfer is the proof above and receives independent internal review.

K2559's lambda>=4/sqrt(3) region has an attained one-stage optimizer with finite expected trials. Thus (9) cannot be extended to all multipliers. A never-finitely-hitting infinite schedule is not an optimizer, even if it approaches S. No external-expert, proof-assistant, remote-CI, novelty or GU certificate is asserted.

Next obtain useful certified D_n gaps or prove a global structure for the maximizing relaxed hybrids. The intermediate transition and exact value remain open; this theorem removes any bounded-expected-positive-trial maximizing sequence as a proposed answer in the certified nonattainment interval. Preparation, empirical common-carrier and native physical-state debts remain separate.

[K2563 hybrid and Euler bounds](k2563-global-hybrid-reduction-2026-11-05.md), [K2483 original law](k2483-adaptive-stopping-bellman-2026-11-01.md), [K2567 nonattainment](k2567-stopping-family-structure-2026-11-05.md), [K2561 one-stage bound](k2561-higher-budget-stopping-2026-11-05.md), [K2565 witness](k2565-bellman-supersolution-2026-11-05.md), [K2559 contrary regime](k2559-parametric-stopping-concavity-2026-11-05.md), [probe](../../tests/channel-swings/k2569_stopping_maximizing_sequences_probe.py), [report](../../lab/process/k2569-stopping-maximizing-sequences.json).
