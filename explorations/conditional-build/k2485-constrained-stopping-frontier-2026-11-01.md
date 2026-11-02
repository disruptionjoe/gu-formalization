---
title: "K2485 Global Bellman certificate and the constrained two-schedule frontier"
status: active_research
doc_type: exploration
created: "2026-11-01"
classification: CONVENTIONAL_COMPARATOR
target_claim: "NONE-NOT-A-KILL"
claim_ceiling: "conditional mathematical result on the stated original or supplied carrier; no native GU or measured implementation claim"
---

# K2485 Global Bellman certificate and the constrained two-schedule frontier

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
result: K2485
carrier: original fresh half-test half-use absorbing experiment with one-sided leakage cost LAYER=toy CHIRALITY=N/A
pairing: positive trace or actual-law expectation as explicitly distinguished below ON=declared_carrier
real_structure: complex adjoint for quantum matrices; real probabilities for classical laws
grading: target and complement or absorbing classical trial histories
action_owner: repository-construction -- supplied conditional mathematical models
target: Global supersolution, constrained duality and two-schedule approximation MAP-TYPE=evaluation
```

## Result and Layer 0

For every original expected budget K, the unrestricted adaptive hit-probability
supremum equals the supremum over finite mixtures of finite repeated-use-stage
schedules. At most two schedules approximate that supremum arbitrarily well
while preserving expected cost <=K. A new global Bellman supersolution proves
quantitative continuity at the exact zero-budget boundary and closes the
endpoint needed for constrained strong duality. The exact saturation threshold is K=s/2: success supremum reaches one there,
but no policy attains one at that critical budget. A sharp optimum within the
two-stage tangent family and a strict finite witness are also obtained. This
does not supply a globally optimal fixed-confidence numerical constant.

The operative law, its one-sided trial cost and fresh-routing assumptions are
exactly [K2483](k2483-adaptive-stopping-bellman-2026-11-01.md). Cost is expected
under the actual law on successful and failed paths. Arbitrary private initial
randomization is allowed; advance knowledge of fresh routing is not. Positive
probabilities and this control model are supplied mathematics. SC-META-53
remains UNCERTAIN; native GU domain/quotient debts, ledger0.263 and canon remain
unchanged. No measured calibration, physical recovery or novelty is claimed.

## 1. Explicit global supersolution

Measure remaining target in units c=log2, so s=(L-z)/c. Write
Q(s)=1 for s<=0, and Q(m+r)=2^(-m)/(1+r) for m>=0, 0<=r<1.
K2483 proves Q(s-b)<=(1+b)Q(s) for s>0, 0<=b<=1.
For lambda>0 define

 U_lambda(s)=min(1,Q(s)+s/lambda), s>0; U_lambda(s)=1, s<=0.

This is a GLOBAL trial/stage supersolution for the original cost. Proof follows on all controls, not a grid. Dominance permits 0<=a<=b<=1. Put d=b-a, D=2(a+b)(2-a-b). For d>0, D>0 and

 w=log(1+d^2/D)>=d^2/(D+d^2)>=d^2/(8b),
 8b-(D+d^2)=4(b-a)+a^2+6ab+b^2>=0.

For d=0, the same final inequality reads 0>=0; idle b=0 is separate tautology. Overshooting controls can be clipped: set b'=min(b,s), a'=min(a,b'). The use branch still hits the target, failure is no greater, and cost is no larger. If a>=b', new cost is0. If a<b', fixed-a cost is nondecreasing with b, because for x=(b-a)^2/[2(a+b)(2-a-b)],

 dx/db=(b-a)*(3a+b-2a^2-2ab)/[(a+b)^2*(2-a-b)^2]>=0,
 3a+b-2a^2-2ab=a(1-a)+(a+b)(1-a)+a(1-b)>=0.

Thus it suffices to check b<=min(1,s). For Ubar(s)=Q(s)+s/lambda on s>=0, target Ubar(0)=1, and

 Ubar(s-b)-(1+a)Ubar(s)
 <=d Q(s)-[b+a*s]/lambda
 <=d-b/lambda
 <=lambda*d^2/(4b)
 <=2lambda*w.

The penultimate step is exactly (lambda*d-2b)^2/(4b*lambda)>=0. Thus Ubar is a supersolution on clipped actions; original overshooting actions have the same next target value, a no-smaller (1+a) multiplier, and no-smaller cost, so their inequalities follow too. The constant1 is also a supersolution. Their minimum is a supersolution: at a state select its minimizing component, and bound the next-state minimum by that component. On target define it to equal1. This proves U_lambda including overshooting actions and idle. For a>b, replacing a by b decreases failure at unchanged use-score and zero cost, so the full original action square is covered.

Consequently, for any finite-budget original policy,

 P(hit)<=min(1,Q(s)+lambda*K+s/lambda).

Optimizing lambda gives P(hit)<=min(1,Q(s)+2 sqrt(sK)). For K=0 take lambda to infinity. This bound is crude away from zero, and does not close the dyadic coefficient gap. Its new purpose is a global explicit certificate and a quantitative right-continuity estimate at the exact nondyadic zero-budget boundary. No finite lambda attainment is claimed at K=0.

## 2. Exact constrained frontier, without asserting optimal-policy attainment

Fix finite s>0. Let F(K) be the supremal original hit probability among policies with expected original leakage <=K. Let G(K) be the same supremum restricted to FINITE mixtures of deterministic finite repeated-use-stage schedules (including free abort). Individual schedules have finitely many successful use stages, but their geometric pass loops have unbounded trial-time support and finite expected duration. Mixture weights use allowed time-zero private randomization.

Both frontiers are nondecreasing, concave and bounded in[0,1], since randomizing initially combines cost and probability linearly. For K>0 both are continuous (finite concave functions on the interior). Their constrained sets are nonempty. G(0)=F(0)=Q(s), attained by floor(s) perfect unit stages and one residual perfect stage when needed. For sufficiently large K, G(K)=F(K)=1: choose a=0 with finitely many b=1 stages (or residual last step); each use stage eventually succeeds surely and has finite original cost. The supersolution above implies right continuity at0 for both frontiers.

K2483 proves for every lambda>0 that

 V_lambda=sup_original[P-lambda K]=sup_finite_schedule[p-lambda k].

The lambda=0 support is1, because the just-described finite sure-hit schedule exists. Passing to finite mixtures does not change any affine supremum.

For a fixed K>0 choose any supporting slope mu>=0 of the concave G at K; such a finite slope exists at an interior point, and nondecreasing G allows a nonnegative slope. For every finite schedule (k,p),

 p<=G(k)<=G(K)+mu(k-K).

Conversely, mixtures approaching G(K) with costs<=K imply
sup_mix[p-mu*k]>=G(K)-mu*K. Thus the common support value is exactly G(K)-mu*K, also when mu=0. For ANY original policy with cost k<=K, support equality gives
p<=V_mu+mu*k<=G(K). Taking suprema yields F(K)<=G(K); the opposite inequality is immediate. Therefore F(K)=G(K) for every K>=0 and

 F(K)=inf_{lambda>=0}[V_lambda+lambda*K],

where V_0=1. For K>0 a finite supporting multiplier attains the dual infimum. At K=0 the global supersolution gives V_lambda<=Q(s)+s/lambda and the exact zero-cost policy gives V_lambda>=Q(s), proving the same dual identity by a limit. This is strong duality for the budget-constrained SUPREMUM, not an assertion that an original optimal policy or finite schedule attains F(K).

## 3. Two finite schedules suffice to approximate the constrained supremum

Fix K>0 and eta>0. By definition of G there is a finite mixture with cost<=K and hit probability>F(K)-eta. Optimize its finitely many weights subject to sum weights=1, weights>=0, and the single cost inequality. This finite linear program has an optimum at an extreme point with at most two positive weights (one if the cost constraint is slack). Reweighting its existing schedules therefore preserves cost<=K and weakly improves probability. This proves that a mixture of at most TWO deterministic finite schedules achieves probability>F(K)-eta with cost <=K (no budget relaxation). It does not prove exact attainment or bound schedule lengths. For K=0 the exact Q schedule suffices. For large budgets the finite sure-hit schedule suffices. A finite prescribed action grid still cannot upper-bound the continuum frontier; the theorem concerns all original controls.

## 4. Exact sure-hit saturation budget and a genuine nonattainment example

For every original action, w(a,b)>=(b-3a)/4, strictly if b>0. If b<3a the right side is negative and the claim is immediate; if b=3a>0 the native cost is positive. For b>3a, log(1+x)>x/(1+x) and the exact identity

 4(b-a)^2-(b-3a)[2(a+b)(2-a-b)+(b-a)^2]
 =16a^2+(b-3a)(a^2+6ab+b^2)>=0

prove the claim, including all positive-cost endpoint cases. At a=b=0 equality holds.

For any original policy terminated on first hit/failure/abort, Tonelli and fresh fair routing give E sum a=2P(fail) and E sum b=2E sum_use b>=2s P(hit). There is no infinity subtraction: before first hit pathwise sum_use b<=s+1, so E sum b<=2(s+1), and P(fail)<=1. Therefore

 K>= [s P(hit)-3P(fail)]/2 >= [(s+3)P(hit)-3]/2,
 F(K)<=min(1,(2K+3)/(s+3)).

In particular F(K)<1 for K<s/2. Conversely choose n>=ceil(s) equal stages a=0,b=s/n. Every stage eventually uses almost surely and the total score equals s, so P(hit)=1 and

 K_n=2n log[(4-s/n)/(4-2s/n)]>s/2,
 lim_(n to infinity) K_n=s/2.

For K>s/2 a sufficiently large finite n is feasible, giving attained probability1. At K=s/2, mix the nth sure-hit schedule with free abort, with schedule probability alpha_n=(s/2)/K_n. This spends exactly s/2, and alpha_n tends to1. Thus F(s/2)=1 as a supremum.

No policy attains that endpoint: P(hit)=1 forces P(fail)=0, hence a=0 almost surely on every reached trial. Since s>0, at least one positive-b trial occurs with positive probability. The strict inequality w(0,b)>b/4 on b>0 then implies E sum w>E sum b/4>=s/2. Countability of the trials makes the strict expected gap valid: a positive random summand occurs with positive probability. Infinite-cost policies cannot attain the finite budget either. This is an exact, original-law example where duality holds and the constrained supremum equals1 but no primal policy attains it. It justifies the approximation-only language in the two-schedule theorem. The stated n-stage policies retain finite expected trial count2n and unbounded trial-time support.

## 5. Released exact tangent-family optimum

K2483's two-stage limiting denominator in x=rt,y=t is
D(x,y)=(2x-y+1)^2/[2(2x+y-1)]+(y-x)^2/[2(y+x)], on the convex admissible domain y>=1, 0<x<y, 2x>=y-1, with both denominators positive. It is convex as a sum of quadratic-over-linear functions on positive denominators. At a stationary point put k=(2x-y+1)/(2x+y-1), l=(y-x)/(y+x). Derivatives vanish exactly when
2k-k^2-l-l^2/2=0 and -k-k^2/2+l-l^2/2=0.
They give l=3k/2-k^2/4 and k^3-12k^2+60k-16=0. The cubic derivative3[(k-4)^2+4]>0, so it has exactly one root in(0,1). The resulting admissible interior r=(1-l)/(1+l), t=(1+k)/[(1+k)-2r(1-k)] gives global minimum WITHIN this family D*=k+k^2/2. Its limiting lower bound is log2/D*=2.15232055114655..., a small improvement. Feasibility is exact: the cubic root lies in(7/25,29/100), so l=3k/2-k^2/4 lies in(1/3,1), hence 0<r<1/2. The denominator defining t is positive (greater than2k), t>1, x=rt lies between0 and y=t, and (2x-y+1)=k(2x+y-1)>0. Stationarity and Euler identity D-x D_x-y D_y=k+k^2/2 prove the optimal value algebraically; convexity gives a global family minimum, including boundary limits. This is not a global stopping optimum.

A finite rational release uses r=42509/100000, t=47703/25000, h=1/268435456, A=2rt and B=t-1. Use the original two-stage controls (1-Ah,1-Bh), (rt h,t h). Exact success is 1/[2(1-(rt h)^2)]>1/2; use score is1+h. The original unconditional expected cost is K=2w1/(1+a1)+2w2/[(1+a1)(1+a2)]. Arb256 certifies log2*h/(2K)>2.15232 in the saved report. Perfect unit preludes transfer the same strict finite ratio to every dyadic confidence. This is a predeclared witness and native interval test, not an optimization-grid inference.

## 6. Evidence and remaining question

Universal inequalities, the clipping argument, supporting-line proof and
finite-simplex extreme-point argument above establish the all-policy claims.
The probe separately checks exact derivative/denominator/square identities,
finite rational stage inequalities including overshoots, interval original
costs and an actual finite-library mixture that beats its feasible individual
members. That library is a control, not the global optimum. Repeated grid cases
are regression coverage, not separate theorems. Failure-path charging and
naive extension controls test the load-bearing seams. Independent probability
and integration review check the written universal proof, not only probe counts.

The least-supersolution framework is standard noncontractive total-cost dynamic
programming; see [Bertsekas, Chapter4](https://www.mit.edu/~dimitrib/DP2_Chapter%204_UPDATED.pdf).
The present specialization uses the original leakage law to supply a global
certificate and establish the exact constrained reduction. It does not assert
external-expert or proof-assistant certification. The next substantial endpoint
is a sharp continuum Bellman certificate or an equally rigorous finite
approximation error bound; an unverified action grid and the two-stage tangent
optimum cannot close the full fixed-confidence constant gap.

[Probe](../../tests/channel-swings/k2485_constrained_stopping_frontier_probe.py)
and [report](../../lab/process/k2485-constrained-stopping-frontier.json).
