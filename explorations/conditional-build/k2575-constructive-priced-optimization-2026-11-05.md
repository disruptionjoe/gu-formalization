---
title: "K2575 Constructive priced stopping optimization"
status: active_research
doc_type: exploration
created: "2026-11-05"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: stage margin, new global merge wedge and finite approximation certificate; no general intermediate optimizer or efficient grid claim
scripts:
  - tests/channel-swings/k2575_constructive_priced_optimization_probe.py
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
result: K2575
carrier: original adaptive fair stopping law reduced to finite completed schedules LAYER=toy CHIRALITY=N/A
pairing: unconditional success minus original leakage and expected positive-trial price ON=declared_carrier
real_structure: real coefficients and positive auxiliary norms; complexification only where explicit
grading: positive stages, geometric trials and charged zero padding remain distinct
action_owner: repository-construction -- stated conditional model
target: constructive finite optimization and a supported resource consumer MAP-TYPE=evaluation
```

# Quantitative merging makes a new optimizer explicit

## Result and prior boundaries

K2571 already proves finite attainment and a stage cap at every positive trial price. K2573 already proves two-schedule finite-budget attainment for every positive leakage multiplier. The new results here are a quantitative minimum stage size, a GLOBAL one-stage merge region outside K2571's high-effective-multiplier region, an exact supported resource point, and a finite rational approximation certificate. A cheap numerical scout is used only to find a short contrary witness outside the new region. No guessed numerical maximum becomes a theorem.

All statements concern the original supplied probability law, independently of GU. SC-META-53 remains UNCERTAIN; source polarities, ledger0.263, canon, physical preparation and native action/observation debts remain unchanged. These are not novelty claims or physical resource calibrations.

## 1. Exact law and derivative estimates

For sum b_i=S, 0<=a_i<=b_i, 0<S<=1/2, define

    P_i=product_(j<=i)(1+a_j)^(-1),
    w(a,b)=log(1+(b−a)^2/[2(a+b)(2−a−b)]),
    J_k=P_n−2 sum_i P_i[lambda w(a_i,b_i)+k],
    R=2 sum_i P_i, k>0, lambda>0.

Delete zero b stages; abort has value0. K2569's resource-preserving original-policy reduction makes the maximum over these schedules and abort equal to the full adaptive value Q. Each positive stage maps a continuation x to (x−2lambda w−2k)/(1+a). Every suffix of a positive-valued schedule is positive, since a nonpositive suffix stays negative under the preceding affine maps.

Write t=a+b, dlt=b−a and z=dlt²/[2t(2−t)]. For t>0,

    z_b=dlt/[t(2−t)]−dlt²(1−t)/[t²(2−t)²],
    −z_a=dlt/[t(2−t)]+dlt²(1−t)/[t²(2−t)²].

Thus 0<=w_b<=2/3 and |w_a|<=1. To prove the first bound, z_b>=0 follows dlt<=t and (2−t)−(1−t)=1. The upper bound is g(a)=(b−a)/[(a+b)(2−a−b)]. At fixed b<=1/2, its logarithmic derivative is −1/(b−a)−1/(a+b)+1/(2−a−b)<0, so g(a)<=g(0)=1/(2−b)<=2/3. For the second bound use dlt<=t to obtain (3−2t)/(2−t)²<=1. Division by 1+z only improves both bounds. At a=b>0 the limiting derivatives are0; the continuous origin and integration along line segments supply the same Lipschitz estimate on the closed triangle. Also w<=b/2. These are universal inequalities, not sampled derivative tests.

## 2. Quantitative adjacent merging

Take a positive-valued schedule with at least two positive stages. Delete stage i of score delta=b_i and keep the other controls. Let P_i denote its original prefix probability. Its suffix value x is positive. Deletion changes the local value by

    x−(x−2lambda w_i−2k)/(1+a_i)
       =(a_i x+2lambda w_i+2k)/(1+a_i),

so gains at least2k P_i in the whole schedule. Add delta to an ADJACENT remaining stage j, keeping a_j fixed. The total score is restored, admissibility survives, and all new b are still<=S. The only new cost is leakage, at most2lambda Lw delta P_j^(deleted), with Lw=2/3. Survival and every resource weight are unchanged by this score addition. For either neighbor,

    P_i/P_j^(deleted)>=1/(1+a_i)>=1/(1+delta).

Therefore the operation strictly improves value whenever

    delta(1+delta)<k/(lambda Lw).                 (1)

Every positive global optimizer with at least two stages must consequently have EACH stage

    b_i>=delta_min=(sqrt(1+4k/(lambda Lw))−1)/2.

This is a quantitative exclusion of disappearing positive stages, not K2571's already-known qualitative compactness argument. For multistage optimizers it bounds n by floor(S/delta_min); a cap covering ALL optimizers is max(1,floor(S/delta_min)), to combine with existing caps; it need not be the tightest cap. The strict gain condition and the positive-suffix premise are essential. It is not a statement about arbitrary negative-valued schedules or unpriced k=0 optimization.

## 3. Execute a new global one-stage wedge and budget point

Every multistage schedule has a smallest delta<=S/2. Hence if

    k>lambda Lw S(2+S)/4, Lw=2/3,               (2)

every positive multistage schedule can be strictly improved by one adjacent merge. Repeating terminates at one stage, preserving positivity. Thus Q equals the maximum of abort and the ONE-STAGE problem under(2), without any numerical search or cap enumeration. Equality is not covered by this strict theorem.

Choose S=1/2, lambda=1/10, k=1/20. The threshold in(2) is1/48<1/20. This lies far outside K2571's earlier sufficient region: lambda/(1−2k)=1/9<4/sqrt(3). Put c0=1−2k=9/10. The one-stage objective is f(a)=[c0−2lambda w(a,S)]/(1+a). Its derivative numerator is

    −2lambda(1+a)w_a−c0+2lambda w
       <=2lambda(1+S)+lambda S−c0=−11/20<0.

Thus the UNIQUE positive deterministic optimal schedule is a=0,b=1/2. The optimal value and actual unconditional resource are

    Q=9/10−(1/5)log(7/6),
    p=1, C=2log(7/6), R=2.

Initial mixtures cannot improve it; this is the original adaptive supremum by the reduction, although distinct implementations of the same law need not be unique. Since the price support inequality J−kR<=Q holds for EVERY policy, this same schedule solves the constrained problem at R<=2:

    F_(1/10)(2)=1−(1/5)log(7/6).

This executes a supported nonlinear-resource point outside the previously certified one-stage region. R=2 is expected positive trials; repeated fair tests still allow arbitrarily many actual trials. A pathwise cap of2 is false.

## 4. Extend ordering, but do not relabel old work

K2495 already establishes the unpriced adjacent exchange rule. With c_i=lambda w_i+k, two successive stages give

    J(AB)−J(BA)=2[a_A c_B−a_B c_A]/[(1+a_A)(1+a_B)]

before the positive prefix multiplier; the common suffix cancels. Thus a_i/c_i can be sorted nonincreasingly without decreasing value. Since k>0 every c_i>0, including a_i=0. This is a priced extension of the prior theorem, not a new unpriced ordering discovery. It removes redundant permutations for a fixed multiset; it does not solve the continuous control problem or show every optimum has one atom.

## 5. Execute a finite rational approximation certificate

Let N be any valid positive-stage cap from K2571 (or max(1,floor(S/delta_min)) from the margin above). For 0<k<1/2 one available cap is floor(exp(S)(S+2k)/[2k(1+S)]). On each padded n<=N simplex use the CONTINUOUS charged extension

    tilde J=P_n−2 sum_(i=1..n) P_i(lambda w_i+k),

even if b_i=0. This is NOT actual resource accounting at zero: deleting such a stage raises value by its positive prefix charge. It is a conservative device for rounding an optimizer with positive stages to the grid.

For two points in the same n simplex, telescoping the survival products gives |Delta P_i|<=||Delta a||_1. From the derivative estimates and sum w_i<=S/2,

    |Delta tilde J| <= (1+2lambda+lambda S+2kn)||Delta a||_1
                      +2lambda||Delta b||_1.            (3)

For rational S, let h=S/m. Round b by largest remainders to nonnegative grid values summing exactly S; each error is<h. Put a_i'=min(b_i',h floor(a_i/h)); its error is<h too. Delete zero stages in the rounded actual schedule. The deletion only improves tilde J. If G_h is the maximum ACTUAL value over all these rational schedules for n<=N, plus abort, then

    0<=Q−G_h<=N h(1+4lambda+lambda S+2kN).              (4)

This is a finite computability theorem with explicit error, not an efficient algorithm or a computed G_h. For rational inputs logs are enclosed rationally: if r>=1 is the argument, u=(r−1)/(r+1), then log r=2 sum_(j>=0)u^(2j+1)/(2j+1). Truncate after j=K; the remaining positive tail is at most 2u^(2K+3)/[(2K+3)(1−u²)]. Finite enumeration and these intervals supply an arbitrarily small certified bracket; no floating-point local optimizer is needed in the theorem.

At lambda=19/10,k=1/20,S=1/2, exp(1/2)<5/3 proves N=6 suffices. The coefficient in(4) is609/10 times h. Taking m=30451 gives h=1/60902 and rounding error609/609020<1/1000. This is an executed error/size choice, NOT enumeration of that prohibitively large grid. Order restrictions can prune it. The error theorem here uses the unpruned grid; directly imposing b>=delta_min after rounding is not justified because rounding can lower a positive stage. No complexity improvement is proved.

## 6. Released contrary consumer: short multistage schedules still matter

A four-start SLSQP scout (n=1,2,3,4,6 at prices .05,.01,.001,.0001) found no improvement over its one-stage candidate at the first three prices, and found useful two- and three-stage candidates at .0001. These are nonexhaustive numerical observations only. The six-stage near-zero padded local optima illustrate why a naive continuous resource objective is delicate; do not treat them as global certificates.

At lambda=19/10,k=1/10000,S=1/2 take the exact rational TWO-STAGE schedule

    (a1,b1)=(232032/10^6,383085/10^6),
    (a2,b2)=(52201/10^6,116915/10^6).

Rational logarithm enclosures prove J_k>71029/100000>.71. K2561's independently certified global unpriced one-stage bound is <.71, and positive pricing only lowers it. Therefore this short schedule beats ALL one-stage schedules and their initial mixtures at the stated positive price. This is a strict multistage witness, not the global two-stage or adaptive optimizer. The new merge wedge does not apply there.

An executed rational THREE-STAGE follow-up uses

    b=(353164,80582,66254)/10^6,
    a=(210796,35947,28097)/10^6.

The same exact log enclosure proves J_k>71032/100000 and exceeds the two-stage witness by more than1/40000. It does not exclude every two-stage competitor. Its actual p,C,R are retained in the report so a reader can use its one-policy supported/budget LOWER bound without refitting or confusing expected with pathwise trials.

## 7. Execute the entire low-multiplier nonlinear resource segment

The merge theorem releases more than a single budget point. Reuse K2559/K2571's actual one-stage derivative quantity

    Mfun(a,S)=−2(1+a)w_a(a,S)+2w(a,S),
    partial_a Mfun=−2(1+a)w_aa<0, Mfun(S,S)=0.

Here strict convexity w_aa>0 on the one-stage interval is inherited from [K2509 section1](k2509-stopping-atom-certificate-2026-11-02.md), propagated through K2559/K2571, not inferred from the new finite fixtures. At S=1/2,

    Mfun(0,1/2)=32/21+2log(7/6)<13/7.

For EVERY 0<lambda<=2/5 and every a in[0,1/2), set

    k(a)=[1−lambda Mfun(a,1/2)]/2.

The uniform inequality lambda[Mfun(0,1/2)+5/12]<191/210<1 implies k(a)>lambda Lw S(2+S)/4. Thus the NEW global merge theorem applies to every such support price. The one-stage derivative numerator is lambda[Mfun(u,S)−Mfun(a,S)], positive for u<a and negative for u>a. It globally maximizes at the desired a; a=0 uses the endpoint version. At a=S use the already proved free-stage price k=1/2 separately.

The corresponding expected resource is m=2/(1+a), which covers the ENTIRE interval[4/3,2]. The support inequality J−kR<=Q then proves, for all original adaptive policies,

    F_lambda(m)=m/2−lambda m w(2/m−1,1/2),
    0<lambda<=2/5, 4/3<=m<=2.

This extends K2571's shorter sufficient-region segment to its full one-stage resource range for a rational interval of multipliers. Its derivative is k(a)>0 and its second derivative lambda(partial_a Mfun)/m²<0; it joins the existing F=m/2 line at4/3 with derivative1/2. At m=2 its left derivative remains positive. There is NO plateau assertion for m>2: K2567/K2569 nonattainment and K2573 imply F_lambda(M)<V for every finite M in this multiplier family. What happens after resource2 requires multistage support, not extending the one-stage formula past a=0.

## Evidence and next condition

The derivative, merge and grid derivations carry universal claims. Exact probes verify the algebra, adverse substitutions, rational log tails and actual original-law consumers. Numerical scouts remain separate from certification. The unpriced multiplier transition and useful global optimization outside both one-stage regions are open. A next solver can combine the proved cap, stage margin and ordering with adaptive certified bounds; a larger uniform grid or a local optimum alone is not that solver.

[K2571 attainment and prior sufficient region](k2571-stopping-resource-price-2026-11-05.md), [K2573 constrained frontier](k2573-universal-resource-attainment-2026-11-05.md), [K2569 inherited one-stage bound](k2569-stopping-maximizing-sequences-2026-11-05.md), [probe](../../tests/channel-swings/k2575_constructive_priced_optimization_probe.py), [report](../../lab/process/k2575-constructive-priced-optimization.json).
