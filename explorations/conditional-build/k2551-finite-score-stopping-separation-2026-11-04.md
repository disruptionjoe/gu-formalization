---
title: "K2551 Uniform finite-score satellite onset and local nonattainment"
status: active_research
doc_type: exploration
created: "2026-11-04"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: fixed-score fixed-success local schedule class, arbitrary finite stage count; no unrestricted global phase or GU claim
scripts:
  - tests/channel-swings/k2551_finite_score_stopping_separation_probe.py
---

# K2551 Close the unbounded-stage gap at a fixed score

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
result: K2551
carrier: original stopping schedules at score one half and fixed success, with one dominant stage and arbitrary ordered satellite stages LAYER=toy CHIRALITY=N/A
pairing: original failure-inclusive expected cost with actual prefix survival ON=declared_carrier
real_structure: real probabilities and logarithmic costs
grading: ordered stages, prefix satellites, main stage and suffix satellites
action_owner: repository-construction -- supplied fresh fair test/use probability law
target: stage-uniform local onset, sharp cost infimum, nearoptimal complexity and finite nonattainment MAP-TYPE=evaluation
```

## Result and exact scope

[K2505](k2505-stopping-satellite-hierarchy-2026-11-02.md) left its fixed-score
satellite hierarchy nonuniform in the number, ratios and sizes of satellites.
That gap is closed here. Fix total score S=1/2 and success p(d)=1/(3/2-d).
Let d0 be K2503's unique suffix directional onset in (4/25,17/100). There
exists ONE fixed neighborhood size delta>0, independent of stage count,
such that the following holds for all d sufficiently near d0.

Consider every finite ordered schedule with one distinguished main stage,
any number of prefix and suffix satellites, total satellite score at most
delta, total score S and success exactly p(d). Let C_local(d) be the infimum
of their original expected costs, including the one-stage schedule. Then

    C_local(d)-C_single(d)
       =-alpha²[(d-d0)_+]²/(4 beta)+O(|d-d0|³),       (1)

where alpha>0 is minus the suffix derivative's d-derivative at d0 and
beta=beta_infinity>1/1000 is K2505's diffuse-tail coefficient. For d<=d0
sufficiently close, the local infimum is EXACTLY the one-stage cost, and every
nontrivial finite satellite schedule costs strictly more. For d>d0 close,
no finite schedule attains the local infimum. Finite schedules with
ceil(1/(d-d0)) satellites attain (1) to O((d-d0)^3), and any finite schedule
that is that accurate must have Omega(1/(d-d0)) positive suffix stages.

This is a fixed-score theorem, distinct from K2549's S->0 theorem, and it
covers varying ratios and unbounded stage counts omitted by K2505. It is
LOCAL in satellite mass. Remote competitors, mixtures of different successes,
the unrestricted global transition and exact continuum-hybrid attainment
remain open. K2503/05/07 already supplied finite-score counterexamples and
optimized hybrid tails; none is rediscovered as a new result here.

The original law is supplied positive probability mathematics. SC-META-53
remains UNCERTAIN; ledger0.263 LT-SM8/LT-GR6b retain physical quotient/action/
domain debts. Source, ledger, canon, native GU, empirical and novelty claims
are unchanged.

## 1. Define one common local class before taking limits

For 0<=a_i<=b_i, sum b_i=S, the original law is

    w(a,b)=log(1+(b-a)²/[2(a+b)(2-a-b)]),
    P_i=product_(j<=i)(1+a_j)^(-1),
    p=P_n, C=2 sum_i P_i w(a_i,b_i).

Zero-score stages are identities. Put a=1/2-d, L=1+a=3/2-d. Give satellite
scores u_i before the main stage and t_j after it, ratios s_i,r_j in [0,1],
and define P=sum u_i, Q=sum t_j. The main stage is forced by the same score
and success:

    b_main=S-P-Q,
    a_main=L/[product_i(1+s_i u_i) product_j(1+r_j t_j)]-1. (2)

Choose delta<S/2 sufficiently small and a closed d interval about d0. Since
a is strictly inside (0,S) there, (2) remains strictly inside (0,b_main)
for ALL such satellite lists with P+Q<=delta. The product lies between 1
and exp(P+Q); these bounds prove the uniform feasibility. The main stage is
uniquely the large stage after further reducing delta if necessary. delta
is fixed before d approaches d0; no n-dependent admissibility neighborhood
is used. Arbitrary finite satellite counts and zero scores are allowed.

Inherited [K2503](k2503-stopping-instability-boundary-2026-11-02.md) gives

    g(r)=(1-r)²/[2(1+r)],
    A=-2w_a(a,S), B=2w_b(a,S)/L,
    M=LA+2w(a,S), N=2w_b(a,S),
    phi(M)=min_(0<=r<=1)[g(r)+Mr],
    rd=2/sqrt(1+2M)-1,
    D(d)=[phi(M)-N]/L.

Near d0 the minimizer rd lies strictly inside (2/5,9/20). D(d0)=0 and
D'(d0)=-alpha<0. Every prefix direction has a positive minimum
min_s[g(s)+As-B]>0 on a common closed d neighborhood. These are verified
properties of this exact original cost, not assumptions about global
optimality. K2503's convex H(d) crossing implies the root is simple.

## 2. Uniform expansion for arbitrary suffix ratios

First set P=0. Write Z=product_j(1+r_j t_j), R=sum_j r_j t_j. The exact cost is

    C=(2/L)[ Z w(L/Z-1,S-Q)
        +sum_i w(r_i t_i,t_i) product_(j>i)(1+r_j t_j)]. (3)

The reversed products in this formula retain the actual prefix costs after
using the fixed final success; replacing them by one changes the problem.
For Q<=delta<=1/4, uniformly over every number of stages and ratios in [0,1],

    Z=1+R+(R²-sum r_i²t_i²)/2+O(Q³),
    w(rt,t)=g(r)t/2+c(r)t²+O(t³),
    c(r)=(1-r)²/8-(1-r)^4/[32(1+r)²].

For the product, the absolute degree>=3 tail is at most exp(Q)Q³/6 by
nonnegative elementary symmetric polynomials. The logarithmic remainder is
bounded uniformly on the compact ratio interval: the exact logarithmic
factorization in K2517 gives |remainder|<=t³/2 for t<=1/4. Expanding the
reversed products in (3) and summing uses sum t_i^k<=Q^k, so the total
third-order remainder is bounded by a constant times Q³, independent of n.
The main function f(Z,Q)=Z w(L/Z-1,S-Q) has bounded first three derivatives
on a fixed compact interior neighborhood, uniformly in d. Thus (3) has a
stage-uniform expansion; no fixed-n remainder has been relabeled uniform.

At Z=1,Q=0,

    f_Z=M/2, f_Q=-w_b,
    f_ZZ=L²w_aa, f_ZQ=-w_b+Lw_ab, f_QQ=w_bb.

The linear part of C-C_single is

    D(d)Q+(1/L)sum_i t_i[g(r_i)+M r_i-phi(M)].          (4)

The full quadratic part is

    (1/L)[(M/2+L²w_aa)R²+2(-w_b+Lw_ab)RQ+w_bb Q²
      -(M/2)sum_i r_i²t_i²+2sum_i c(r_i)t_i²
      +sum_(i<j)g(r_i)r_j t_i t_j].                   (5)

In particular this includes unequal ratios and their order dependence.

## 3. Control arbitrary ratio deviations instead of assuming them away

Let E2=sum_i t_i(r_i-rd)² and E1=sum_i t_i|r_i-rd|. The exact identity

    g(r)-g(rd)-g'(rd)(r-rd)
       =2(r-rd)²/[(1+r)(1+rd)²]>=(r-rd)²/4          (6)

and M=-g'(rd) bound the penalty in (4) below by E2/(4L).
Also E1²<=Q E2. All functions and first ratio derivatives in (5) are bounded
on a common compact set. Replacing every r_i by rd changes (5) by at most
C Q E1: diagonal sums use t_i²<=Q t_i, and ordered pairs use their total
partner mass at most Q. Young's inequality then gives

    C Q E1<=E2/(8L)+C'Q³.                            (7)

This prices ratios that vary with d and stage count; it does not assume
uniform pointwise convergence of every satellite ratio.

At the common ratio rd, (5) is exactly

    beta_inf(d)Q²-p(d)J(rd)sum_i t_i²,
    J(r)=(-3+22r²-16r³-3r^4)/[16(1+r)²],
    beta1(d)=(1/L)[L²rd²w_aa+2Lrd w_ab+w_bb
                         -2rd w_b+2c(rd)],
    beta_inf(d)=beta1(d)+p(d)J(rd).                  (8)

K2505 gives J(r0)<0 and beta=beta_inf(d0)>1/1000. The equality in (8)
holds throughout this neighborhood because M=-g'(rd), not merely at the
onset. Smoothness bounds coefficient changes by C|d-d0|. There are positive
j,c,C independent of n such that

    C-C_single >=D(d)Q+beta Q²+j sum_i t_i²+c E2
                         -C[|d-d0|Q²+Q³].           (9)

For a common-ratio cloud the full expansion is an equality with the signed
remainder, rather than only this lower estimate.

## 4. Prefix satellites do not evade the uniform bound

Let Zp,Zs be the prefix and suffix products. Subtract from the full schedule
cost the tail-only cost at the same d and suffix list. The exact difference is

    2sum_prefix w(s_i u_i,u_i)/product_(j<=i)(1+s_j u_j)
    +(2Zs/L)[w(L/(Zp Zs)-1,S-P-Q)-w(L/Zs-1,S-Q)].     (10)

All suffix cost terms cancel because the final success is held fixed.
The linear term is sum_i u_i[g(s_i)+As_i-B], which has a uniform positive
lower bound times P. The same product expansions and bounded derivatives
bound the remainder by C P(P+Q), uniformly in counts and ratios. Decrease
the ONE fixed delta to absorb that error. Combining (9) and (10) yields

    DeltaC>=cP+D(d)Q+beta Q²+j sum_i t_i²+cE2
                              -C[|epsilon|Q²+Q³],   (11)
    epsilon=d-d0.

Constants c can be decreased to a common positive number. This controls
arbitrary ordered prefix/suffix insertion around the single main stage,
not just a terminal equal-ratio family.

## 5. Local phase and sharp uniform coefficient

Choose delta and then |epsilon| small enough that the final error in (11)
is at most beta Q²/2. This is possible with constants independent of n.
For epsilon<=0, K2503 gives D(d)>=0. Hence DeltaC>=0, strictly for every
nonzero satellite list (P>0 or Q>0). The one-stage schedule attains the
local infimum. This is an EXACT local-stability claim, including epsilon=0.

For epsilon>0, D(d)=-alpha epsilon+O(epsilon²). Any possibly improving
schedule obeys from (11)

    Q=O(epsilon), P=O(epsilon²), E2=O(epsilon²).       (12)

This localization is proved BEFORE replacing Q³ by O(epsilon³). Substitution
and square completion give, uniformly in every improving finite schedule,

    DeltaC>=-Gamma epsilon²+beta(Q-z epsilon)²
               +cP+cE2+j sum_i t_i²-O(epsilon³),     (13)
    z=alpha/(2beta), Gamma=alpha²/(4beta).

Schedules with DeltaC>0 trivially satisfy the lower bound on the infimum.
For the upper bound take no prefix, Q=z epsilon, m=ceil(1/epsilon),
t_i=Q/m and r_i=rd, with the main stage from (2). Uniform feasibility holds
for small epsilon, and sum t_i²=Q²/m=O(epsilon³). The equality expansion
in sections2--3 proves DeltaC=-Gamma epsilon²+O(epsilon³), giving (1).
These are finite original schedules with exact fixed score and success,
not an exchanged fixed-m limit or an assumed continuous experiment.

Mixtures of schedules ALL having this SAME success preserve the lower cost
bound by linearity and cannot lower the infimum. Mixtures of different
successes are outside this local fixed-success assertion. No universal
all-policy adaptive optimum is inferred from it.

## 6. Released complexity and exact local finite nonattainment

For a finite local schedule within O(epsilon³) of C_local, (13) and the
matching upper bound imply

    P=O(epsilon³), E2=O(epsilon³),
    |Q-z epsilon|=O(epsilon^(3/2)), sum_i t_i²=O(epsilon³).

Since Q is asymptotic to z epsilon and Q²<=m sum_i t_i², the number of
positive suffix stages satisfies m=Omega(1/epsilon). The construction above
shows this order suffices. The bounds concern individual schedules;
mixtures give expected deficits, not componentwise stability.

Suppose a finite schedule attained C_local for a sufficiently small positive
epsilon. It would meet the preceding nearoptimal bounds. In particular Q>0,
Q<1/100, and E2/Q=O(epsilon²). Since rd stays strictly inside [2/5,9/20],
some positive suffix stage has r_i in that box; otherwise E2 would be at
least a fixed positive multiple of Q. Its score satisfies 0<t_i<=Q<1/100.
K2505's EXACT whole-rectangle fragmentation theorem replaces this stage by
two with the same score and product success and strictly lower original
expected cost. All later prefix weights and the main stage remain fixed.
Total satellite mass, local membership and fixed success are unchanged.
This contradicts attainment. Thus the local infimum is not attained by
ANY finite schedule for epsilon>0 sufficiently small.

This is stronger than a coefficient-level absence of a fixed finite m, but
its locality must remain explicit. It does not exclude a remote globally
optimal finite schedule or prove attainment by the particular continuum
hybrid of K2507. That hybrid is a useful candidate, not an established exact
optimizer of this expanded local class.

## 7. Consuming the result and remaining boundary

The coefficient Gamma previously increased along fixed-n families. Equation
(1) proves its sharp local limiting value even when all ratios, positions and
counts vary. Prefix mass and ratio deviations have explicit nonnegative
costs; finite fragmentation supplies a strict original-law improvement,
not a heuristic preference for diffuse tails. The local counterexample is
below the single-stage mixture frontier at the same fixed success, by
K2493's convex cost theorem. There is also a feasible same-budget success advantage
Gamma L0^4/M0^3*(K-K0)^2+O((K-K0)^3), where K0=C_single(d0).
To avoid assuming smoothness across the changing satellite count, put
h=C_single'(d0)=M0/L0²>0 and k=C_single''(d0)/2. For each budget increment
kappa=K-K0>0, choose m=ceil(1/kappa) FIRST and set

    epsilon=kappa/h-(k-Gamma)kappa²/h³-B kappa³.

The uniform cloud expansion gives cost K0+kappa-hB kappa³+O(kappa³).
One fixed sufficiently large B ensures feasibility. The one-stage inverse
has epsilon_one=kappa/h-k kappa²/h³+O(kappa³). Since p'(d0)=1/L0²,
subtracting success probabilities gives the displayed coefficient. This is
a LOWER construction for the unrestricted frontier, not its expansion.
Remote schedules or cross-success mixtures could do better.

No numerical validity radius is evaluated, and no new finite-budget global
value is claimed. The substantial unresolved question remains a global
Bellman or exchange certificate that excludes remote multiple atoms or a
certified value for that full class. K2515's lambda>=8/3 global theorem
survives; its concavity proof cannot simply be extended by this local result.
The speculative extension to lambda*=4sqrt(3)/3 was not proved here.

## 8. Executed test of a stronger global proof route

A concrete proposed next route was to extend K2515's uniform concavity
argument to lambda_star=4sqrt(3)/3, the sharp possible threshold for a
uniform-in-score one-stage theorem. Test the ACTUAL optimized residual

    m_s(b)=min_a[(1+a)U_lambda(s)+2lambda w(a,b)-U_lambda(s-b)].

At s=1/2,b=99/200, the exact interval probe brackets the one-stage roots at
s and s-b by M=1/lambda, then the distinct residual root by
-w_a=U_lambda(s)/(2lambda). Strict monotonicity from w_aa>0 certifies each
root, without conflating the optimizer equations. Differentiating the
optimized functions gives

    m_s''(b)=2lambda(w_bb-w_ab²/w_aa)-U_lambda''(s-b),
    U_lambda''(t)=(2lambda/(1+a))
       [(w_ab-w_b/(1+a))²/w_aa-w_bb].

Arb encloses m_s''(99/200) in [0.0443395041214579 +/- 6.32e-17], strictly
above 1/100. Thus the old uniform nonpositive-curvature method fails at
this actual interior point. This is a certified method obstruction, NOT a
negative Bellman residual or a policy beating one stage. A direct residual,
exchange or other shape-sensitive global proof remains open. The local
result above does not solve that distinct global question.

## Verification

The exact probe independently expands the original products and main cost,
checks the full unequal-ratio quadratic, Bregman penalty, beta/J identities,
prefix cancellation and original same-success fragmentation fixtures. Arb
brackets the inherited onset and coefficients; these values support typing
and signs but do not replace the uniform proof or establish a radius.
Wrong prefix weights, additive hazard and absent ratio penalties are tested
as contrary constructions. Universal estimates and exact finite controls are
separate evidence kinds. Independent internal review is not external-expert,
proof-assistant or novelty certification.

[Probe](../../tests/channel-swings/k2551_finite_score_stopping_separation_probe.py),
[report](../../lab/process/k2551-finite-score-stopping-separation.json),
[onset](k2503-stopping-instability-boundary-2026-11-02.md),
[fragmentation and missing uniformity](k2505-stopping-satellite-hierarchy-2026-11-02.md),
[optimized hybrid](k2507-stopping-optimal-hybrid-tail-2026-11-02.md),
[small-score uniform theorem](k2549-uniform-nearcritical-stopping-bound-2026-11-04.md).
