---
title: "K2483 Global stopping reduction and a finite lower bound above 2.1522"
status: active_research
doc_type: exploration
created: "2026-11-01"
classification: CONVENTIONAL_COMPARATOR
target_claim: "NONE-NOT-A-KILL"
claim_ceiling: "conditional mathematical result on the stated original or supplied carrier; no native GU or measured implementation claim"
---

# K2483 Global stopping reduction and a finite lower bound above 2.1522

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
result: K2483
carrier: original fresh half-test half-use absorbing experiment with one-sided leakage cost LAYER=toy CHIRALITY=N/A
pairing: positive trace or actual-law expectation as explicitly distinguished below ON=declared_carrier
real_structure: complex adjoint for quantum matrices; real probabilities for classical laws
grading: target and complement or absorbing classical trial histories
action_owner: repository-construction -- supplied conditional mathematical models
target: Least Bellman supersolution, exact zero-budget boundary and lawful strict crossings MAP-TYPE=evaluation
```

## Result and Layer 0

The unrestricted history-dependent Lagrangian problem reduces exactly to the
least nonnegative scalar Bellman supersolution. Finite deterministic repeated
use-stage schedules approximate its value; a history-dependent selector is not
needed to approximate this objective. This is not uniqueness of a Bellman fixed
point or strong duality for the probability-constrained problem.

The exact zero-budget hit probability at score (log2)*s is
2^-floor(s)/(1+fraction(s)). A two-stage original schedule gives
a rigorous finite fixed-confidence coefficient lower bound above2.15223, with
a limiting-family lower bound2.152284 at every dyadic
confidence epsilon=2^(-(m+1)). It strictly improves K2480's1.90645 construction;
the unrestricted optimal coefficient remains open below K2471's uniform upper
bound2.33561. This is conditional probability mathematics, not measured leakage
or a GU prediction. SC-META-53 remains UNCERTAIN; ledger0.263 and canon unchanged.

## 1. Original law, not a changed cost

Each active trial chooses predictable a,b in[0,1], draws a fresh fair test/use
bit, fails and absorbs on test rejection (conditional probability a), stays at
the same score on test pass, and adds c*b on use, c=log2. Every active trial,
including the final failing one, incurs

 w(a,b)=log(1+(b-a)^2/[2(a+b)(2-a-b)]) if a<b,
 w(a,b)=0 if a>=b.

The boundary a=b=0 and a=b=1 has cost0. Stopping/aborting is free in this
mathematical interface. Let tau be first score Z>=L before failure; arbitrary
private randomization and past-dependent actions are allowed, but not advance
knowledge of fresh bits. Set a=b=0 after termination. For lambda>0 define

 V(z)=sup_policy {P_z(tau<infinity)-lambda E_z sum_active w}.

Infinite expected cost has payoff minus infinity. This is original-law
expectation, not cost conditional on eventual success. Actions a>b are
dominated by (b,b): equal use-score, lower failure probability and same zero
cost. We may therefore restrict to0<=a<=b<=1. For finite-horizon values,
aborting gives0 and target boundary gives1, so0<=V_n<=1.

## 2. Trial Bellman equation and minimality

Initialize V_0(z)=1 for z>=L and0 otherwise. Below L,

 V_(n+1)(z)=max(0,sup_ab{-lambda*w+(1-a)V_n(z)/2+V_n(z+c*b)/2}).

V_n is the best payoff with at most n trials. Backward induction proves this:
condition on the first action/outcome; randomization averages candidate payoffs
and cannot exceed their supremum. At a fixed initial score a finite-depth tree
has finitely many reachable nodes, so epsilon-optimal action choices suffice;
no global measurable maximizer or exact attainment is assumed. Markov controls
in score AND remaining horizon achieve the same supremum at that start.

V_n increases and is bounded by1. Let V_* be its pointwise limit. Supremum and
increasing limit commute, and each transition uses only two continuing scores;
thus V_* solves the displayed equation. Any nonnegative supersolution U with
U>=1 at target bounds V_n by induction, hence bounds V_*. For an arbitrary
infinite policy of finite expected cost, trial truncation has hit indicators
increasing to the eventual-hit indicator and costs increasing to total cost;
its payoffs converge. Infinite-cost policies cannot improve0. Therefore V=V_*,
the least nonnegative supersolution. Taking lambda=0 separately drops the cost
term and gives the corresponding reachability value; do not multiply0 by an
infinite expectation.

The idle (0,0) action makes unqualified fixed-point uniqueness false. Nor does
a pointwise greedy selector establish termination or attainment. We use the
minimal construction and finite approximants, not those assertions.

## 3. Exact reduction to repeated use stages

Freeze one pair with b>0 and repeat it until a use or failure. Its success
probability is1/(1+a), mean number of trials is2/(1+a), and expected cost is
2w/(1+a). If U is the value after its use, stage payoff is

 (U-2lambda*w)/(1+a).

Define W_0=1_target and, below target,
W_(n+1)=max(0,sup_(0<=a<=b<=1,b>0)
 [W_n(z+c*b)-2lambda*w]/(1+a)).

These are values for at most n use stages, allowing abort. Each finite schedule
has at most n successful use stages and finite expected trial count<=2n.
Its increasing limit is the least nonnegative stage supersolution by the same
argument. A nonnegative U satisfies the trial supersolution inequalities iff

 (1+a)U(z)>=U(z+c*b)-2lambda*w

for all nonidle actions, which are exactly the stage inequalities. Idle adds
only a tautology. The two least supersolutions coincide: W=V. Consequently
finite deterministic repeated-stage schedules approximate the FULL
history-dependent Lagrangian value. Along a surviving deterministic schedule,
score strictly increases, so it is a score-only policy on its finitely many
live scores. This proves approximation, not a single globally optimal
stationary policy or an equivalence of constrained expected-budget frontiers.

A nonnegative trial/stage supersolution U gives the useful universal dual
bound P(hit)<=U(0)+lambda K for E budget<=K. Randomizing at time zero between
two lawful policies gives convex combinations of their P and K. That is a
primal construction. No strong-duality theorem or necessity of two policies
is asserted here.

## 4. Exact zero-budget boundary

For s<=0 let Q(s)=1. For s=m+r>=0, m=floor(s),0<=r<1, put
Q(s)=2^-m/(1+r). Original zero-cost controls have a>=b; (b,b) dominates them.
For0<=b<=1,

 Q(s-b)/(1+b)<=Q(s).

When b<=r the denominator excess is b(r-b)>=0. When b>r and s-b>=0,
a factor2 carry gives excess (b-r)(1-b)>=0. If s<1 and b>=s,
1/(1+b)<=1/(1+s). These cover all boundaries. Thus Q is a supersolution
for every zero-cost policy, including adaptive randomized and infinite ones.
If E budget=0, nonnegative trial costs vanish almost surely on reached trials,
so the same bound applies. Equality is attained with m unit stages a=b=1,
then a=b=r if r>0. This hits the inclusive threshold exactly and has finite
expected duration. At noninteger s, Q(s)<2^-s, since2^r<1+r. This gives a
strict nondyadic zero-budget boundary, not a positive-budget optimal constant.

## 5. A finite strict original-law improvement

Take target L=c*129/128 and epsilon=1/2. Schedule A consists of seven stages:

- first b=123/128, a=(31/32)b;
- five stages b=1/128, a=(14/32)b;
- final b=1/128, a=(13/32)b.

Schedule B has two stages: a=b=1, then b=1/128,a=(13/32)b.
Both hit exactly L on success. For a finite list (a_i,b_i), compute

 P=product_i 1/(1+a_i),
 K=sum_i [product_(j<i)1/(1+a_j)]*2w_i/(1+a_i).

P is rational, while K is an exact finite sum of logarithms with rational
weights. In particular costs on eventual failure paths are charged. Let
alpha0=(1/2-P_B)/(P_A-P_B) and
alpha=(floor(2^40*alpha0)+1)/2^40. Forty fresh fair routing bits with a=b=0
choose A with probability alpha, otherwise B. These bits add no score or
budget, cannot anticipate later routing, and do have trial/time cost if one
prices physical attempts. Then Pmix>1/2 exactly. Interval arithmetic certifies

 Cfinite=[c/(256)]/Kmix >2.1259.

For any coefficient C<Cfinite, the final-score success event strictly crosses
c+C*Kmix/epsilon and has probability above epsilon. Hence C_(1/2)>=Cfinite.
The explicit finite witness suffices; the exploratory grid used to find it is
not certified globally optimal and is not part of the proof.

Prepending m perfect unit stages multiplies P and K by2^-m and adds mc to
score. For epsilon=2^(-(m+1)), the same ratio and strict margin survive.
Thus every dyadic fixed-confidence coefficient has the same lower bound.
The finite extra fair bits and each stage's geometric pass loop have finite
expected duration; there is no deterministic trial-time cap claim.

## 6. Released two-stage construction and asymptotic bound

The stage reduction releases a simpler construction with a stronger result.
Set r=17/40, t=19/10, A=2rt=323/200 and B=t-1=9/10. For sufficiently small
h>0 use exactly two stages:

 (a1,b1)=(1-Ah,1-Bh),  (a2,b2)=(rt h,t h).

For0<h<min(1/A,1/t), both pairs satisfy0<a<b<=1. The total use score is
c(1+h), the first score is below c, and

 P_h=1/[(2-2rt h)(1+rt h)]=1/[2(1-(rt h)^2)]>1/2.

No initial mixture, external coin or zero-cost prelude is needed at epsilon1/2.
Use the same full-law cost K_h from section5. Since log(1+x)/x->1,

 w1/h -> (A-B)^2/[4(A+B)],
 w2/h -> t(1-r)^2/[4(1+r)]=t*g(r)/2.

The first expected-trial multiplier2/(1+a1) tends to1; the second stage's
reached expected-trial multiplier[1/(1+a1)]*2/(1+a2) also tends to1.
Consequently

 2K_h/h -> D=(A-B)^2/[2(A+B)]+t*g(r)=388781/1207200,
 c*h/(2K_h) -> Ctwo=(1207200/388781)*log2 >2.15228.

Every coefficient below Ctwo is violated by a sufficiently small finite h,
so C_epsilon>=Ctwo at every dyadic epsilon after the same perfect-prelude
transfer. This is a lower bound from one rationally specified family, not an
optimum over r,t or all controls. The actual finite h=1/65536 has exact
P_h-1/2=104329/1374389534511342, and rigorous coefficient ratio
2.15223405865...>2.15223. Its finite strict crossing is checked directly,
independently of the limiting expansion. The earlier mixture remains a valid
intermediate witness, now superseded in strength. Each stage's pass loop has
finite expectation; deterministic trial-time caps and measured resource costs
remain separate.

## 7. Verification, prior art and remaining endpoint

Exact rational checks establish probabilities, stage composition, dominance,
zero-cost boundary cases and fair-bit strictness. Arb intervals enclose the
actual logarithmic budgets and crossing margin. Contrary controls omit failed
path costs, suppress prelude survival, replace output probability by1, or
change the one-sided native cost. A truncated control grid is never treated
as a continuum upper bound; that is an inference boundary, not a probe control. Universal
Bellman and zero-budget arguments are stated separately from finite probes.
Independent internal probability review corrected the cost's one-sided domain
and the stationary-attainment wording before acceptance. No external-expert,
proof-assistant, hardware or novelty certification is claimed.

This is an application of standard total-cost dynamic programming; see
[Bertsekas, noncontractive total-cost problems](https://www.mit.edu/~dimitrib/DP2_Chapter%204_UPDATED.pdf).
The repository-specific contributions are the exact original stage reduction,
zero-budget boundary and the new lawful finite witness. The next useful test
is an analytic supersolution matching improved lower bounds, or a stronger
explicit schedule. A finite grid only proves attainability of its policies;
it cannot bound untested controls or close the global fixed-confidence gap.

[Probe](../../tests/channel-swings/k2483_adaptive_stopping_bellman_probe.py) and [report](../../lab/process/k2483-adaptive-stopping-bellman.json).
