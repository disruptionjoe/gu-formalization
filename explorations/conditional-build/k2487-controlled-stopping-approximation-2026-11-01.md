---
title: "K2487 Controlled finite approximation of the original stopping frontier"
status: active_research
doc_type: exploration
created: "2026-11-01"
classification: CONVENTIONAL_COMPARATOR
target_claim: "NONE-NOT-A-KILL"
claim_ceiling: "conditional mathematical result on the stated original or supplied carrier; no native GU or measured implementation claim"
---

# K2487 Controlled finite approximation of the original stopping frontier

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
result: K2487
carrier: original fresh half-test half-use absorbing experiment with one-sided leakage cost LAYER=toy CHIRALITY=N/A
pairing: positive trace or actual-law expectation as explicitly distinguished below ON=declared_carrier
real_structure: complex adjoint for quantum matrices; real probabilities for classical laws
grading: target and complement or absorbing classical trial histories
action_owner: repository-construction -- supplied conditional mathematical models
target: Uniform schedule compression, action-grid and budget-preserving approximation MAP-TYPE=evaluation
```

## Result and Layer 0

A finite library of original-law schedules now bounds the unrestricted constrained stopping frontier from both sides with an explicit error. Tiny stages are merged with a proved cost surcharge; directed rounding preserves hitting. The same-budget approximation uses free-abort mixing, and a finite Bellman calculation supplies a global certificate with the stated error. This is a conditional mathematical theorem, not a numerical solution of the sharp fixed-confidence problem.

The law and allowed information are exactly K2483/K2485: fresh fair test/use routing, private initial randomization and expected leakage including failing paths. All positive probability structure is supplied mathematics. SC-META-53 remains UNCERTAIN; ledger0.263 LT-SM8/LT-GR6b retain native physical state and domain debts. Source polarities, ledger, canon and physical credit are unchanged. No novelty or external certification claim.

Let s>0 be target in log2 units. Original controls 0<=a<=b<=1 after dominance; one-stage survival p=1/(1+a), one-stage expected cost c(a,b)=2 w(a,b)/(1+a), w=log(1+(b-a)^2/[2(a+b)(2-a-b)]), extended by zero at both diagonal corners. A deterministic complete schedule can be clipped to total sum b=s (K2485); incomplete schedules have zero probability and are dominated by free abort. Stage costs always include failure paths.

## Elementary uniform estimates
Put u=a+b,d=b-a and x=d^2/[2u(2-u)]. On the triangle d<=u(2-u), since u(2-u)-d=a(3-a-2b)+b(1-b)>=0. Thus 0<=x<=d/2<=b/2 and 0<=c<=b. At the other corner also d<=1-a, giving continuous extension x->0 as (a,b)->(1,1).

Interior derivatives satisfy
x_a=-d/[u(2-u)]-d^2(1-u)/[u^2(2-u)^2],
x_b= d/[u(2-u)]-d^2(1-u)/[u^2(2-u)^2].
Hence |x_a|,|x_b|<=2, |w_a|,|w_b|<=2. Since w<=1/2, |c_a|<=5 and |c_b|<=4. Along segments in the triangle, continuity extends this to
|c(a,b)-c(a',b')|<=5|a-a'|+4|b-b'|.

Define f(a,b)=d^2/[2u], f(0,0)=0. This is convex and positively homogeneous (quadratic-over-linear), hence subadditive f(sum pairs)<=sum f(pairs). If b<=1/2 then
|c(a,b)-f(a,b)|<=b^2.
Proof: u<=1, f<=b/2, x=f/(2-u). Upper: c<=2x=f/(1-u/2)<=f(1+u)<=f+b^2. Lower: log(1+x)>=x-x^2/2 gives c>=2x/(1+a)-x^2/(1+a)>=f/(1+a)-x^2>=f-fa-x^2>=f-3b^2/4.

## Compress tiny stages, WITHOUT truncating their total mass
Choose 0<delta<=1/4. Keep all stages b>delta individually. Within each intervening run of b<=delta, greedily group until cumulative B>=delta, then start a new group; leave at most one residual group at each run end. Each small group has B<=2delta<=1/2. Replace its list by the single pair (A,B)=(sum a,sum b). This stays in 0<=A<=B<=1. Score remains exactly s.

Every retained large stage and every completed small group has score at least delta; the number of such pieces is <=s/delta. Residual groups number at most (#large+1)<=s/delta+1. Thus compressed length <=N=ceil(2s/delta)+1.

For one grouped block, old survival p=product(1+a_i)^(-1), new survival q=(1+A)^(-1). Then q>=p and
q-p<=A-log(1+A)<=A^2/2<=B^2/2.
For rigor: H=log(q/p)=sum log(1+a_i)-log(1+A) lies in [0,A-log(1+A)]; q-p=q(1-exp(-H))<=H. The block old expected cost C=sum_i product_(j<i)(1+a_j)^(-1)c_i. Since c_i<=b_i and 1-prefix_survival<=sum_prior a_j<=B,
sum c_i-C<=B^2.
Convexity/subadditivity and local cost estimates give
c(A,B)<=f(A,B)+B^2<=sum f_i+B^2<=sum c_i+2B^2<=C+3B^2.

Let S2=sum_over_small_blocks B^2<=2delta*s. At any block boundary the increased survival prefix is <=S2/2 (telescoping products bounded by one). Original unweighted block costs total <=s. Therefore globally
P_compressed>=P_original,
K_compressed<=K_original+3S2+(S2/2)*s
 <=K_original+delta*s*(6+s).
This explicitly prices the increased chance of reaching later expensive stages.

## A finite action grid with no missed-hit discontinuity
Choose integer M>=1, mesh eta=1/M. For every compressed pair round a DOWN to floor(Ma)/M and b UP to ceil(Mb)/M. Rounded controls remain in the triangle with 0<b<=1. Follow the rounded schedule but terminate on its first hit. Rounding b upward guarantees reaching s no later than completion of the full rounded sequence; rounding a downward gives weakly higher full-sequence survival. Thus hit probability weakly increases. Early termination only reduces expected cost.

For the full rounded sequence each c changes by <=9eta. At any prefix the survival increase is <=Neta, because 1/(1+a) is 1-Lipschitz. Original compressed unweighted costs sum<=s. Thus
P_grid>=P_original,
K_grid<=K_original+E,
E=delta*s*(6+s)+N*(9+s)/M.

The library consists of free abort plus all original-law schedules of length<=N over the finite grid 0<=a<=b<=1,b>0, terminating at first score >=s. The target is J=ceil(Ms), so for rational s (or a supplied certified integer J=ceil(Ms)) this is fully finite and concrete; arbitrary computable-real input alone does not uniformly decide that ceiling. Grid probabilities are rational; grid costs are finite rational-weighted logarithms of rationals, so interval-certified arithmetic applies. No deterministic trial-time cap: each use stage still repeats through pass loops with finite expected trial count <=2N.

## Rigorous two-sided frontier and Bellman certificates
Let G=finite-library mixture frontier and F=unrestricted original frontier at fixed s. K2485's two-schedule approximation plus the map above proves
G(K)<=F(K)<=G(K+E) for every K>=0.
For K>0, mix any mapped policy (cost<=K+E) with free abort at weight K/(K+E). Therefore
G(K)>=K/(K+E)*F(K),
0<=F(K)-G(K)<=E/(K+E).
(The bound is crude but explicit and tends to zero as delta->0 and N/M->0.) At K=0 use K2483 exact Q(s), not division by zero. Can adjoin its exact schedule to the finite library to get G(0)=F(0), without affecting upper bounds. When this nongrid schedule is adjoined, evaluate its payoff Q(s) separately and take the maximum with the grid Bellman value.

The finite mixture LP has a maximizing mixture of at most two schedules. For lambda>=0, let V^grid_lambda=max_library(P-lambda*K). Then
V^grid_lambda<=V_lambda<=V^grid_lambda+lambda*E.
For any lambda>=0, the certified continuum bound is
F(K)<=min(1,V^grid_lambda+lambda*(K+E)).
Finite Bellman recursion defines Vgrid exactly. For rational lambda and rational s its value is computable to certified error by interval arithmetic (no exact comparison of logarithmic expressions is assumed): target state j>=J has value1, n=0 below target has0; for n>=1,
W_n(j)=max(0,max_(a=l/M,b=k/M,0<=l<=k<=M,k>0)
[W_(n-1)(j+k)-2lambda*w(a,b)]/(1+a)).
Start j=0,n=N. Costs require interval certificates for numerical release. This is a computability/error theorem, not a practical complexity claim or sharp fixed-confidence number.

Explicit tolerance selection: for K>0 and desired additive error e in(0,1), it suffices E<=e*K/(1-e). Pick delta<=min(1/4,e*K/[2(1-e)*s*(6+s)]), N=ceil(2s/delta)+1, then M>=2(1-e)*N*(9+s)/(e*K). This may be computationally huge; say so without treating size as mathematical failure.

## Literature and scope
Primary sources verified via web: Bertsekas, Dynamic Programming and Optimal Control II, Chapter4, Noncontractive Total Cost Problems (updated October2024), https://www.mit.edu/~dimitrib/DP2_Chapter%204_UPDATED.pdf . Relevant general approximation literature: Naci Saldi, Finite-State Approximations to Discounted and Average Cost Constrained Markov Decision Processes, https://arxiv.org/abs/1807.02994 ; Saldi/Yuksel/Linder, Asymptotic Optimality of Finite Approximations to Markov Decision Processes with Borel Spaces, https://arxiv.org/abs/1503.02244 . Those papers cover different discounted/average criteria; do not import them as proofs for this undiscounted absorbing law. The original-law compression derivation above supplies the needed uniform control. No novelty claim.


## Reproducibility, review and next condition

Independent probability and adversarial review checked the uniform inequalities and all-policy transfer. The lead independently checked the derivative bounds, compression and survival-cost proof. Review restricted the effective threshold claim to rational s or a supplied certified ceiling; a generic computable-real name does not decide equality to a grid boundary. Exact symbolic identities, rational contrary cases, Arb interval costs and a separate exhaustive tiny-library comparison support the implementation. The universal result is the written argument, not the count of finite fixtures. Inherited K2483/K2485 policy reduction is authenticated, not reproved by the probe.

This makes each fixed rational-target, positive-budget frontier effectively approximable, without claiming efficient complexity, an optimal hardware law, or a sharp constant uniform over all targets/budgets. The next question is a sharper compression/error bound or analytic certificate that makes the finite interface useful computationally. Whole fixed-confidence optimization still requires uniform control over target and small-budget limits.

[Probe](../../tests/channel-swings/k2487_controlled_stopping_approximation_probe.py) and [report](../../lab/process/k2487-controlled-stopping-approximation.json).
