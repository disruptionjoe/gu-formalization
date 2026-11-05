---
title: "K2555 Global quantitative stability of critical stopping support"
status: active_research
doc_type: exploration
created: "2026-11-05"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: stage-count-uniform stability for finite completed schedules and their initial mixtures; no multiplier interval or arbitrary adaptive rigidity
scripts:
  - tests/channel-swings/k2555_global_stopping_stability_probe.py
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
result: K2555
carrier: original failure-inclusive finite completed stopping schedules at fixed score and their initial mixtures LAYER=toy CHIRALITY=N/A
pairing: prefix survival and actual expected cost; componentwise nonnegative support deficit ON=declared_carrier
real_structure: real probabilities and exact rational derivative and moment certificates
grading: deterministic schedules, initial mixtures, and broader adaptive or limiting implementations remain distinct
action_owner: repository-construction -- supplied fresh fair test/use probability law
target: uniform quantitative stability and exact budget-contact rigidity MAP-TYPE=evaluation
```

# K2555 Near-optimal policies must have one early dominant stage

## Result and scope

K2553 supplies global support at lambda=4/sqrt(3), for every 0<S<=1/2.
This note turns its strict residual into quantitative stability for every
finite completed ordered schedule, with constants independent of stage count,
ratios and positions. Small support deficit forces almost all score into one
early stage and controls deviations of the action parameters from the correct
residual optimizers. At the exact one-stage budget contact it also controls
the dominant action relative to the one-stage optimum. Initial mixtures satisfy
expectation and probability bounds, without assuming their components obey the
mixture's budget separately.

The quantitative statements below are for finite completed schedules and
initial mixtures of those schedules at the SAME score. K2553's qualitative
support for broader adaptive/limiting classes survives; quantitative rigidity
for those implementations requires its own transfer. No whole multiplier
interval, full budget frontier, GU-native probability, empirical or novelty
claim is made. SC-META-53 remains UNCERTAIN; ledger0.263 LT-SM8 retains its
native action/quotient/domain debt. This is independent supplied-law mathematics.

## 1. The original law and an additive deficit certificate

Let b_i>0, 0<=a_i<=b_i, sum b_i=S, s_i=sum_(j>=i)b_j,
t_i=s_i-b_i, P_i=product_(j<=i)(1+a_j)^-1, and

    w(a,b)=log(1+(b-a)^2/[2(a+b)(2-a-b)]),
    p=P_n, C=2sum_i P_i w(a_i,b_i),
    U(s)=max_(0<=a<=s) [1-2lambda w(a,s)]/(1+a), U(0)=1,
    eta=U(S)-p+lambda C >=0.

Zero-score stages can be removed. The residual minimizer alpha(s,b) is the
unique root 2lambda[-w_a(alpha,b)]=U(s). It is NOT generally the one-stage
root; at b=s it equals a_*(s). K2553 gives

    m_s(b)=min_a [(1+a)U(s)+2lambda w(a,b)-U(s-b)]
          >= lambda b(s-b)^2/900.

K2509's original-logarithm bound w_aa>=2/D, D=2(a+b)(2-a-b), and
D<=8b(1-b) for a<=b<=1/2 give

    w_aa>=1/[4b(1-b)].

For clarity the new probe independently certifies the weaker whole-domain
bound w_aa>=1/(4b) by exact rational Bernstein coefficients. The stronger
bound is reused from the displayed K2509 inequality and the monotonicity of
z(2-z) for z=a+b<=2b<=1, not inferred from that weaker certificate.
Taylor's integral remainder at the interior residual optimizer therefore gives

    E_s(a,b)>=lambda b(s-b)^2/900
             +lambda(a-alpha(s,b))²/[4b(1-b)].

The original P_i telescope, not unweighted stage costs, yields

    eta >=lambda sum_i P_i [b_i t_i²/900
                 +(a_i-alpha(s_i,b_i))²/(4b_i(1-b_i))].      (1)

Since log(1+a)<=a and sum a<=S, every P_i>=exp(-S). Put

    E=sum_i b_i t_i²,
    J=sum_i (a_i-alpha(s_i,b_i))²/[b_i(1-b_i)].

Then eta>=lambda exp(-S)(E/900+J/4). These are universal inequalities;
a list of finite exact fixtures is not their proof.

## 2. Score concentration, uniformly over every finite stage count

Let M=max b_i and d=S-M. Expanding each interval integral gives

    S³/3=E+sum_i b_i² t_i+sum_i b_i³/3,
    sum_i b_i t_i=(S²-sum_i b_i²)/2.

Using b_i²t_i<=M b_i t_i and b_i³<=M b_i² gives

    E>=S³/3-MS²/2+(M/6)sum_i b_i²
      >=(S-M)²(2S+M)/6 >= S d²/3.                   (2)

Thus for every schedule, without a small-deficit threshold,

    d² <=2700 exp(S) eta/(lambda S).                (3)

A useful independent proof gives E>=d³/3: on the score interval
[t_i,t_i+b_i], t_i>=max(u-M,0), then integrate and sum. Adjacent exchange
changes E(b,c)-E(c,b) by bc(c-b), so decreasing order minimizes E for a fixed
multiset. Moving a largest stage to the front therefore also proves
E>=M d². These complementary checks do not assume the actual schedule is sorted.

Let L be the total score before a chosen largest stage. Every earlier tail
contains M, hence E>=L M². If M>=S/2, E>=LS²/4. If M<S/2, then d>S/2 and
L<=d; (2) gives E>=Sd²/3>=S²L/6. Therefore globally

    L <=5400 exp(S) eta/(lambda S²).                (4)

A near-optimal schedule has O(sqrt(eta)) total satellite score, but only
O(eta) score BEFORE its largest stage. These constants are conservative and
are not an optimal modulus claim. Equations (1)--(4) also give

    J<=4 exp(S) eta/lambda,
    |a_i-alpha(s_i,b_i)|²
       <=4 exp(S) eta b_i(1-b_i)/lambda.             (5)

The distinction between residual and one-stage optimizers matters in (5).

## 3. Exact contact budget and dominant-action stability

At fixed S let a*=a_*(S), p*=1/(1+a*),
C*=2w(a*,S)/(1+a*). Then U(S)=p*-lambda C*.
For a deterministic finite schedule with C<=C* and p>=p*-epsilon,
0<=epsilon<p*, the global support theorem gives

    p<=p*, 0<=eta<=epsilon, 0<=C*-C<=epsilon/lambda. (6)

Consequently (3)--(5) hold with eta replaced by epsilon. A particularly direct
bound identifies the dominant a_j without confusing the two roots. Write
R=product_(i!=j)(1+a_i); then 1<=R<=exp(d) and 1+a_j=1/(pR).
Using p*-epsilon<=p<=p* gives

    -(1+a*)(1-exp(-d)) <= a_j-a*
                         <=epsilon/[p_star*(p_star-epsilon)],

where p_star is the fixed one-stage optimum p*. Consequently,

    |a_j-a*| <=max((1+a*)d,
                    epsilon/(p_star*(p_star-epsilon))).   (7)

This does not rely on an unproved sensitivity bound for alpha. At eta=0,
(2) forces d=0; strict convexity then forces a_j=a*. The optimizer is exactly
one positive-score stage, up to zero-score idles, within this finite class.
The earlier support theorem gives the contact value; this result adds rigidity
and an explicit stable form of that contact.

## 4. Mixture bounds and the transfer that is NOT allowed

For an arbitrary initial probability mixture of such finite completed schedules
at fixed S, assume expected cost is finite. Linearity gives
eta_mix=U(S)-E[p]+lambda E[C]=E[eta]. Nonnegative inequalities can therefore
be integrated even when stage counts are unbounded across components:

    E[d²]<=2700 exp(S) eta_mix/(lambda S),
    E[L]<=5400 exp(S) eta_mix/(lambda S²),
    E[J]<=4 exp(S) eta_mix/lambda.                    (8)

For delta>0, Markov gives Pr(d>=delta)<=2700 exp(S)eta_mix/(lambda S delta²)
and Pr(L>=delta)<=5400 exp(S)eta_mix/(lambda S² delta), each capped at one.
If eta_mix=0, almost every component has one optimal positive-score stage.
At the contact expected budget E[C]<=C*, E[p]=p* forces E[C]=C* and this
almost-sure form. No claim about how a general adaptive implementation encodes
that law follows.

For E[C]<=C*, E[p]>=p*-epsilon, one has eta_mix<=epsilon and all (8) follows.
However (7) cannot be applied component by component: an initial mixture can
contain an overspending, higher-success component compensated by another.
The probe includes a concrete original-law mixture of a=0 and a=S at S=1/2
whose components lie on opposite sides of the optimal contact cost. Expected
budget is not a per-component constraint. Arbitrary infinite schedules and
adaptive quantitative equality require a separate extension, not a label change.

## 5. Constructive collapse with explicit budget slack

Replace a finite schedule by ONE stage with score S and its largest stage's
action a_j. This is an admissible stage because a_j<=M<=S. Let p_c,C_c be
its original-law success and cost. Since the removed factors multiply to
R in[1,exp(d)],

    0<=p_c-p<=1-exp(-d)<=d.

There is also a uniform cost estimate. Direct differentiation gives w_b>=0;
the new exact degree(4,2) Bernstein certificate proves w_b<=1/2 on the whole
cone. Further, w_a<=0 and log(1+x)<=x give
w(a,b)<=w(0,b)<=b/(4-2b)<=b/3. Let q be the survival prefix before stage j;
q>=exp(-L). Its original contribution is C_j=2q w(a_j,M)/(1+a_j), and

    0<=C_c-C_j<=d+(2S/3)L,
    0<=C-C_j<=2d/3.

The first bound integrates w_b from M to S and uses 1-q<=L; the second
bounds the actual failure-inclusive costs of all satellites. Therefore

    -2d/3<=C_c-C<=d+(2S/3)L,
    |C_c-C|<=d+(2S/3)L.                              (9)

Combining (3),(4) gives an explicit compression guarantee:

    p_c-p<=sqrt(2700 exp(S)eta/(lambda S)),
    C_c<=C+sqrt(2700 exp(S)eta/(lambda S))
             +3600 exp(S)eta/(lambda S).

This is constructive: select a largest stage and reuse its action. It preserves
total score and increases success, with a proved budget SLACK. It does not say
cost decreases or that the compressed stage obeys the original budget exactly.
For initial mixtures collapse each finite component. Cauchy--Schwarz and (8)
give the same bounds on expected success/cost with eta_mix replacing eta;
measurably choose the first largest stage. No single deterministic stage is
claimed to replace the whole mixture.

### Exact-budget repair within the mixture class

Let A=2700 exp(S)/(lambda S) and
Delta=sqrt(A eta_mix)+3600 exp(S)eta_mix/(lambda S). If the original expected
cost is at most K_budget>0, the collapsed mixture costs at most K_budget+Delta.
Mix it with the free single stage a=b=S, using collapsed weight

    theta=K_budget/(K_budget+Delta).

The repaired mixture costs at most K_budget and loses success relative to the
original by at most Delta/(K_budget+Delta), since collapse only increased
success and every success probability lies in[0,1]. Thus near-support schedules
admit an explicitly budget-feasible approximation by mixtures of single stages.
At the contact budget use eta_mix<=epsilon. This is not an exact optimality
claim at other budgets, and K_budget=0 requires separate handling.

## Verification and frontier

The note supplies universal telescoping, moment, ordering, strong-convexity,
budget and mixture arguments. The probe recomputes original derivatives,
whole-domain curvature coefficients with inverse basis reconstruction, exact
moment/exchange identities and deterministic finite countercontrols. Numerical
original-law examples are illustrations only. Independent review checks the
universal reasoning and its exact policy class.

The remaining multiplier interval (4/sqrt(3),8/3) is still open here.
Interpolation between support theorems at the endpoints cannot prove that
intermediate optimized one-stage curves dominate all policies. A new
parameter-dependent residual/optimizer argument is required. For this result,
the next substantive consumer is quantitative transfer to the full adaptive
closure with explicit overshoot/abandonment losses, or a certified parameter
interval theorem; another coefficient of the already proved fixed-multiplier
stability bound is not a new frontier.
