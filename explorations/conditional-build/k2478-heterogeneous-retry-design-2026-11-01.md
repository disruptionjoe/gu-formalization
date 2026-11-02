---
title: "K2478 Sharp heterogeneous retry risk and resource allocation"
status: active_research
doc_type: exploration
created: "2026-11-01"
classification: CONVENTIONAL_COMPARATOR
target_claim: "NONE-NOT-A-KILL"
claim_ceiling: "sharp abstract conditional interface; continuous allocation only, no measured device or quantum attainability"
---

# K2478 Sharp heterogeneous retry risk and resource allocation

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
result: K2478
carrier: classical terminal attempts supplied by separately justified complete instruments LAYER=toy CHIRALITY=N/A
pairing: actual-law expectation and reached-history conditional probability ON=declared_carrier
real_structure: real probabilities and costs on the stated classical sample spaces
grading: classical trial and reached-attempt histories
action_owner: repository-construction -- supplied conditional mathematical models
target: Unequal retry risk, order and resource design MAP-TYPE=evaluation
```

## Result and premises

K2475's constant-attempt theorem extends to a sharp deterministic unequal
schedule, including one shared calibration event. It yields distinct optimal
risk and cost orders, and an exact convex continuous resource allocation.
Every premise must hold on each reached history under the law conditioned on
the good-calibration event G, P(G^c)<=zeta<1. The attempts need not be independent.
For attempt i require wrong-output probability f_i<=alpha_i, output probability
q_i>=p_i>0, with0<=alpha_i<=1. Each attempt terminates; stop at first output or
finite cap m. Wrong/correct/no-output are exhaustive and have the same meaning
throughout. Caps K_i must include the whole attempt, resets, calibration and
abort; a fixed setup S is paid once.

These are supplied classical probabilities. Abstract extremizers are not
claimed realizable by the original Q/T quantum instruments. SC-META-53 remains
UNCERTAIN; source, ledger0.263, physical GU and canon remain unchanged.

## 1. Exact unequal conditional risk

Define t_i=max(alpha_i,p_i), R_i=product_(j<i)(1-t_j), and

    W=sum_i R_i alpha_i,     C=1-product_i(1-t_i)>0.

Then the exact abstract worst conditional error is

    F=[zeta+(1-zeta)W]/[zeta+(1-zeta)C].                 (1)

To prove it, fix eta in[0,1] and reward wrong output by1-eta, correct output
by-eta, and no terminal output by0. Every suffix optimal value V lies in
[-eta,1-eta]. Its one-step Bellman value is

    max_(p_i<=q<=1) [min(alpha_i,q)-eta q+(1-q)V].        (2)

Below alpha_i the slope is1-eta-V>=0; above it the slope is-eta-V<=0.
Thus t_i is an optimizer regardless of eta or suffix history. Backward
induction gives good-law value W-eta C even against adaptive conditional
choices. Independent laws(alpha_i,t_i-alpha_i,1-t_i) attain it.

Bad calibration can output wrong immediately, value1-eta. At eta=F, the
mixture with bad mass zeta has value0. Smaller bad mass cannot increase it:
1-eta-(W-eta C)>=0. Thus every allowed law has wrong mass<=F times output
mass; positive output follows from the good-law floors. The displayed good
laws and an always-wrong bad law attain F. This proves sharpness of this
single objective, not simultaneous sharpness of risk, delay and cost.

For a fixed known no-output history kernel, (2) uses the conditional mean of
child values; for adversarial child choice it uses their maximum. A finite
signed-payoff tree oracle remains valid. The product formula requires the
same deterministic bounds at every reached history of each index; arbitrary
history-dependent bounds do not inherit one product formula.

## 2. Risk order and cost order can conflict

For a fixed multiset of attempts, C is order independent. Swapping adjacent
A,B changes W_AB-W_BA by their preceding reach probability times
alpha_A t_B-alpha_B t_A. Therefore nondecreasing alpha_i/t_i minimizes(1).

Separately put r_i=product_(j<i)(1-p_j). Under G,
E cost<=S+sum r_i K_i. If caps hold on bad histories too, unconditional cost
satisfies the sharp abstract bound

    E cost<=S+(1-zeta)sum r_i K_i+zeta sum K_i.           (3)

Good law q_i=p_i and bad law never outputting attain the respective cost
bound. They generally differ from the risk extremizer. The adjacent cost
difference is proportional to K_A p_B-K_B p_A, so nondecreasing K_i/p_i
minimizes(3); its bad-event sum is invariant under order.

Example: p_A=p_B=1/2, alpha_A=1/100,alpha_B=1/10,K_A=10,K_B=1.
Risk order AB gives W=3/50 versus BA21/200, both C3/4. Good-law expected
cost is21/2 for AB versus6 for BA. There is no universal order minimizing both.

## 3. Exact continuous allocation for a fixed feasible schedule

Assume0<p_i<1 and choose0<alpha_i<=p_i. Then t_i=p_i, and (1)<=eta iff

    sum r_i alpha_i <= B_eta
      =eta C-(1-eta)zeta/(1-zeta).                      (4)

Strictly positive allocations exist exactly when B_eta>0; B_eta=0 allows
abstract zero error, but not a finite logarithmic certificate. A negative
right side is impossible in this full uncertainty class, not a verdict on a
particular device with a better known bad-event law.

Suppose the independently justified continuous cost is
k_i(alpha)=H_i+a_i log(1/alpha)+b_i/alpha, with a_i>0,b_i>=0.
For positive weights w_i, minimizing sum w_i k_i is a strictly convex decreasing
problem. If all upper caps fit, choose alpha_i=p_i. Otherwise a unique positive
multiplier lambda exhausts(4), with

    alpha_i=min(p_i,
      [w_i a_i+sqrt((w_i a_i)^2+4 lambda r_i w_i b_i)]
       /(2 lambda r_i)).                              (5)

This is the stationarity equation lambda r_i=w_i(a_i/alpha+b_i/alpha^2),
with upper-cap complementary slackness; strict convexity proves global optimality.
The risk sum decreases continuously from sum r_i p_i=C to0 as lambda increases,
so the binding multiplier exists and is unique when0<B_eta<C.
Use w_i=r_i for good-law expected cost, w_i=(1-zeta)r_i+zeta for unconditional
expected cost, and w_i=1 for the pathwise sum cap. The latter is sufficient;
actual pathwise attainability depends on which histories can be reached.
If p_i=1, later attempts are unreachable on G but might still be reached on bad
histories; do not drop their global costs without a structural controller rule.

For m2,p_i1/2,zeta0,eta1/10 and identical log-only costs, pathwise allocation
is alpha_1=3/80, alpha_2=3/40, versus common alpha_i=1/20. Both have exact
conditional error1/10, but the unequal design saves log(9/8) in the continuous
sum. Under good-law expected cost, the same identical laws instead give equal
uncapped alpha: reached probability cancels from the stationarity equation.

## 4. Count consumer and honest rounding guarantee

The K2471 count relaxation has a_i=1/(log2 D_i),
b_i=Csharp K_Bi/(log2 D_i), D_i>0. For a fixed allocation, rounding each
continuous use count upward preserves its sufficient risk inequality and
adds less than one use per attempt; the weighted cost increases by less than
sum w_i u_i for supplied per-use charge u_i. It need not minimize integer
cost. Fixed setup/reset/calibration costs must be counted separately when not
in those coefficients. If p_i or the budget-abort loss changes with count,
(5) is only a conditional relaxation; the same chosen count must be used to
rejustify p_i, calibration, leakage and the whole-attempt cost cap.

The exact signed-payoff oracle, order rule, convex allocation and rounding
bound remove unnecessary constant-allocation conservatism. They do not supply
missing measured completion, quantum memory reset, or reached-history calibration.

## 5. Released integer count optimum for one supplied design

For two attempts with p_1=p_2=1/2, zeta=0, eta=1/10, D_i=1/100 and
K_Bi=1/1000000, minimize the sum of integer certificate uses under the same
sufficient K2471 risk interface. Put beta=Csharp/1000000 and c=log2.
The smallest certifiable error allowance at integer count n is

    a(n)=beta/W(beta exp(n c/100)),

where W is the positive inverse of x -> x exp(x). This follows from the
strictly decreasing equation log(1/a)+beta/a=n c/100. Requiring a<=1/2
forces n>=101. Joint feasibility is exactly a(n1)+a(n2)/2<=3/40 within
this supplied certificate-design class.

The minimum total is **848 uses**, attained by(474,374); the weighted risk
sum lies between0.07484592235 and0.07484592236. Every pair with total847
and both counts>=101 fails: the smallest weighted risk sum lies between
0.07510620745 and0.07510620746 at(474,373). Checking all such847 pairs
excludes every smaller total, since adding uses decreases each a(n).
The equal-count design needs433+433=866 uses, so unequal allocation saves18.
There are multiple848 minimizers; no unique-optimal-count claim is made. The candidate counts also result from rounding the feasible rational allocation in section3; that allocation is the log-only optimizer, not the full continuous optimizer with positive beta.

Arb256 proposes root enclosures using W, then independently checks strict
opposite signs of the original monotone log equation at rational enclosure
endpoints. Those brackets certify the exhaustive847 exclusion and an848
witness. This is optimality of **this sufficient certificate's integer-use
objective** with externally fixed completion and budget inputs, not an
optimal quantum protocol, actual spending optimum or measured apparatus.
All same-count calibration, whole-attempt costs and conditional completion
obligations from section4 remain necessary.

## 6. Verification

Written Bellman slope, event-mixture, exchange and convexity proofs establish
the general claims. Exact rational vertex enumeration independently checks
small unequal schedules, all permutations, shared-calibration ratios and
finite history trees. Exact budget arithmetic plus interval logarithms checks
the unequal allocation and rounding consumer. Contrary controls include
marginal rather than conditional promises, wrong risk/cost order, omitted
shared-failure cost, identical allocation and unpriced rounding. Dependency
hashes authenticate inherited evidence rather than proving new mathematics.
No external-expert, proof-assistant or novelty claim is made.

[Probe](../../tests/channel-swings/k2478_heterogeneous_retry_design_probe.py) and [report](../../lab/process/k2478-heterogeneous-retry-design.json).
