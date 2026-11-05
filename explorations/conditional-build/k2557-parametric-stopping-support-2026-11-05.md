---
title: "K2557 Adaptive stopping rigidity and parametric certificate boundary"
status: active_research
doc_type: exploration
created: "2026-11-05"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: quantitative adaptive stability at the critical multiplier; remaining multiplier interval open
scripts:
  - tests/channel-swings/k2557_parametric_stopping_support_probe.py
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
result: K2557
carrier: original fresh fair test/use histories with predictable controls, absorption and finite expected total cost LAYER=toy CHIRALITY=N/A
pairing: unconditional original-law expectation including failing trials and terminal potentials ON=declared_carrier
real_structure: real probabilities and logarithmic costs with exact rational supporting identities
grading: active trials, successful use increments, failure, abort and nonabsorption remain distinct
action_owner: repository-construction -- supplied stopping probability law
target: adaptive quantitative stability, exact optimizer classification and parametric scope test MAP-TYPE=evaluation
```

# K2557 Account for the whole adaptive history

## Result and boundary

At lambda=4/sqrt(3), K2553 proves the one-stage global support bound for every
0<S<=1/2. K2555 quantifies finite schedules and initial mixtures. This result
extends quantitative control to arbitrary predictable, randomized adaptive
policies with finite expected cost, including unbounded duration, overshoot,
abandonment and nonabsorption. It uses the actual trial law, without assuming
that an adaptive policy is a mixture of fixed schedules.

The exact support optimizers are repeated one-stage optimal actions separated
by arbitrary predictable cost-free idles, provided absorption occurs almost
surely. Their expected physical duration need not be finite. Near-optimal
policies have small abandonment/nonabsorption probability and controlled
score fragmentation on successful paths. This does not establish the remaining
multiplier interval, other-budget frontier, GU-native probability, measured
implementation or novelty. SC-META-53 remains UNCERTAIN and ledger0.263
LT-SM8 retains the action, quotient and domain debt.

## 1. The attempted parameter extension and its honest outcome

Parameterize the zero-score optimizer by r0. The root equation gives

    lambda(r0)=2(1+r0)^2/[(1-r0)(3+r0)],
    2sqrt(3)-3 <= r0 <= 4/sqrt(7)-1.

This maps the proposed interval onto [4/sqrt(3),8/3]. An exact expansion of
the original one-stage root M=1/lambda, not the residual root, gives

    a_one(b)/b = r0+c(r0)b+d(r0)b²+O(b³),
    c(r)=-(r-1)(3r+5)(r²+6r+1)/32,
    d(r)=(r-1)(45r^7+597r^6+2609r^5+4905r^4+3175r³
          -1217r²-1669r-253)/[2048(r+1)].

These coefficients do not certify root bounds on finite scores. In fact at
r_max=4/sqrt(7)-1, d=761/686-29647sqrt(7)/76832<9/100.
For A0=34963/34300 and B0=29647/76832,
7B0²-A0²=1700087313/527067520000>0 proves that strict sign. Thus
reusing the old lower quadratic coefficient9/100 puts its curve ABOVE the
actual root for sufficiently small positive scores at lambda=8/3. Reusing K2553's old residual upper ribbon is
invalid: at lambda=8/3, b=0, r=3/5 its limiting hazard 2lambda k is3/4,
which exceeds the required2/3. This is an exact failure of that domain
certificate, not a counterexample to support. No three-variable global sign
certificate is claimed. The stronger ready consequence of existing support
is the adaptive theorem below; interpolation is not used to fill the gap.

## 2. Exact trial slack, including clipping losses

Write s for the remaining score in units of log2. The original active trial
chooses predictable a,b in[0,1]. A fresh fair bit selects test or use; test
rejects with probability a, test pass leaves s unchanged, use reduces s by b
and hits if b>=s. Failure, hit and voluntary abort are absorbing. Every
active trial, including a failing trial, incurs the ORIGINAL cost

    w(a,b)=log(1+(b-a)²/[2(a+b)(2-a-b)]) if a<b,
    w(a,b)=0 if a>=b.

Let U(s)=max_(0<=a<=s)(1-2lambda w(a,s))/(1+a), U(0)=1. K2553 supplies
2/3<=U(s)<=1 on[0,S]. For a reached trial put b'=min(b,s),
a'=min(a,b'), and define

    E'=(1+a')U(s)+2lambda w(a',b')-U(s-b'),
    delta=U(s)-[(1-a)U(s)+U(s-b')]/2+lambda w(a,b)
         =E'/2+U(s)(a-a')/2+lambda[w(a,b)-w(a',b')].       (1)

All three summands are nonnegative. If a>b', the clipped cost is0. Otherwise
a'=a and increasing b above a increases w; this follows directly by
differentiating the original logarithm, also checked in K2555. Thus clipping
is an accounting identity for the original policy, not a substitution of a
more favorable policy.

For b'>0 let alpha(s,b') be the residual optimizer solving
2lambda[-w_a(alpha,b')]=U(s), and t=s-b'. K2553's Hermite gap and K2555's
strong-convexity bound give

    delta >=lambda b't²/1800
             +lambda(a'-alpha(s,b'))²/[8b'(1-b')]
             +U(s)(a-a')/2+lambda(w-w').                 (2)

At b'=0 use0 for both gap terms. If b=0 and a>0 the rejection loss remains
in(1); such an action is not an idle. The only zero-cost zero-score idle
with zero slack is a=b=0.

## 3. Tail potential is indispensable

Let T be absorption time into hit/fail/abort, possibly infinity. Before
absorption, s_n decreases and has a limit s_infinity. Let p_n be the
probability of hit by horizon n and C_n the expected original cost of trials
before horizon n or absorption. Iterated conditional expectation gives

    U(S)-p_n+lambda C_n
      =E sum_(active trials before n) delta
       +E[1_(still live at n) U(s_n)]
       +E[1_(abort by n) U(s_abort)].                    (3)

Hit has potential1, failure0; abort is paid as the last displayed loss.
For finite expected cost, monotone convergence applies to costs and
nonnegative slacks; bounded convergence applies to the live potential.
Therefore with eta=U(S)-p+lambda C,

    eta=E sum_active delta
        +E[1_(T=infinity)U(s_infinity)]
        +E[1_abort U(s_abort)].                         (4)

In particular

    Pr(nonabsorption or abort)<=3eta/2,
    E sum_active(a-a')<=3eta,
    E sum_active(w-w')<=eta/lambda.                     (5)

Probabilities may of course be capped at1. If infinitely many use increments
approach S but never reach it in a finite trial, the trajectory has NOT hit.
Then s_infinity=0 and its tail potential is U(0)=1, not0. Endless idling also
has zero local slack yet retains U(S). Dropping either terminal term would
falsify the optimizer classification. Infinite expected cost is excluded
from the quantitative theorem and cannot improve the support optimum.

## 4. Successful paths concentrate, without a fixed-schedule representation

Predictability and the independent fair use bit imply, for any nonnegative
predictable F at a reached trial,

    E sum_use F = (1/2) E sum_active F.                 (6)

This includes the last hitting use. It holds by Tonelli even with unbounded
trial counts. Combining(2),(4),(6),

    E sum_use b'(s-b')² <=900eta/lambda,
    E sum_use (a'-alpha(s,b'))²/[b'(1-b')] <=4eta/lambda. (7)

On a HIT path there are finitely many trials, hence finitely many positive
clipped use increments summing exactly S. Define M as their largest increment,
d=S-M, L as the score before the first largest increment, and
J=sum_use (a'-alpha(s,b'))²/[b'(1-b')]. Define d=L=J=0 off HIT when using
these variables under expectation. K2555's deterministic moment inequalities
apply to each hit-path partition; no policy-law equivalence is needed:

    E[1_hit d²]<=2700eta/(lambda S),
    E[1_hit L]<=5400eta/(lambda S²),
    E[1_hit J]<=4eta/lambda.                            (8)

These bounds have no exp(S) factor because they use actual trial occupation
rather than a lower bound on deterministic survival prefixes. Conditional-on-
hit bounds divide by p>0. Markov yields, for x>0,
Pr(hit and d>=x)<=2700eta/(lambda S x²), and an analogous L bound with x.
This does not assert all failure paths have completed score partitions.

A useful operational consequence also holds on ALL paths: the expected number
of active trials with b'>=u and s-b'>=v, for positive u,v, is at most
1800eta/(lambda u v²). The expected number of such use trials is at most
900eta/(lambda u v²). These count inefficient partial actions even if the
experiment later fails; near-optimality constrains more than successful runs.

## 5. Exact equality and constrained-contact consequence

If eta=0, equation(4) rules out abort and nonabsorption with positive
probability. At every reached trial, up to a null set, delta=0. If b'>0,
(2) forces b'=s and a'=alpha(s,s)=a_one(s); clipping loss forces a=a'.
The root is strictly interior, so strict increase of w(a,b) for b>a excludes
b>s. Thus the nonidle action is exactly (a_one(s),s). No partial use has
occurred before absorption, so s=S. If b'=0, zero slack forces a=0 and then
b=0. Conversely arbitrary predictable idles interspersed with the fixed
optimal action give equality when absorption occurs almost surely.

Let a*=a_one(S). The expected number of nonidle trials is2/(1+a*), by summing
the per-active-trial absorption probability(1+a*)/2. Fresh bits give
p*=1/(1+a*) and C*=2w(a*,S)/(1+a*). Waiting times between these trials can
have infinite expectation without changing p,C; physical waiting is not
priced by this mathematical cost. This is uniqueness of the reached nonidle
action, not uniqueness of the policy or of its duration.

For ANY adaptive policy with C<=C* and p>=p*-epsilon,

    p<=p*, 0<=eta<=epsilon,
    0<=C*-C<=epsilon/lambda.                           (9)

Consequently every bound(5),(7),(8) and the action-count bound holds with
eta replaced by epsilon. At exact contact equality the policy classification
above is complete. Initial randomization is already included in predictability;
no componentwise budget premise is inserted.

## Verification and remaining question

The probe independently checks the original trial/slack decomposition, a
branching finite adaptive tree telescope, occupation factors, exact root
expansion and failed parameter-ribbon endpoint, moment constants and meaningful
contrary controls. These finite algebraic checks support but do not replace
the universal expectation/limit/equality proofs. Independent review checks
those arguments and their quantifiers. Existing whole-domain K2553/K2555
certificates are reused at their unchanged scope, not recounted as new tests.

Remaining work is the actual parameter-dependent root and sign certificate,
or a global constrained-frontier construction beyond the certified contact.
A physical time/controller cost would define a different optimization problem.
No unproved Geometric Unity probability mechanism is inferred.

[Original trial law](k2483-adaptive-stopping-bellman-2026-11-01.md),
[global certificate](k2553-global-stopping-certificate-2026-11-04.md),
[finite-schedule inequalities](k2555-global-stopping-stability-2026-11-05.md),
[probe](../../tests/channel-swings/k2557_parametric_stopping_support_probe.py).
