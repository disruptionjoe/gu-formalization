---
title: "K2477 Randomized score preludes strengthen fixed-confidence bounds"
status: active_research
doc_type: exploration
created: "2026-11-01"
classification: CONVENTIONAL_COMPARATOR
target_claim: "NONE-NOT-A-KILL"
claim_ceiling: "explicit finite-law lower bounds only; global fixed-confidence optimum remains open"
---

# K2477 Randomized score preludes strengthen fixed-confidence bounds

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
result: K2477
carrier: original fresh half-test half-use absorbing experiment with predictable risks LAYER=toy CHIRALITY=N/A
pairing: actual-law expectation and reached-history conditional probability ON=declared_carrier
real_structure: real probabilities and costs on the stated classical sample spaces
grading: classical trial and reached-attempt histories
action_owner: repository-construction -- supplied conditional mathematical models
target: Fixed-confidence stopping coefficient MAP-TYPE=evaluation
```

## Result

At every dyadic confidence epsilon=2^(-(m+1)), m>=0, the fixed-confidence
coefficient of K2474 obeys the stronger necessary lower bound

    C_epsilon >= Lmix
      = log(2)/[r1 (k(r1)+H(r0))] > 1.8736,
    r0=47/100, r1=1/3,
    k(r)=(1-r)^2/[2r(1+r)],
    H(r)=k(r)(1-exp(-r))/(exp(-r)-1/2).                 (1)

This improves the prior dyadic lower bound Csharp log2, approximately1.6189,
while the inherited universal upper bound remains
Csharp=(1+log2)^2/[4(1-log2)], approximately2.3356. Neither(1) nor its two-rate
parameters are claimed optimal. The improvement uses a lawful mixture of
actual score-generating preludes, with zero initial score. It does not repair
the independently activated one-use shortcut rejected in K2474.

Probability and risk are supplied classical interfaces; SC-META-53 remains
UNCERTAIN. No physical GU, ledger0.263, source-polarity or canon change follows.

## 1. Exact finite construction on the original law

Put c=log2, rho=2^-m, epsilon=rho/2. Choose integer M sufficiently large.
An initial finite sequence of fresh a=b=0 routing trials generates a random
branch bit: these trials have no failures, score or original budget. On branch0
run m perfect prelude trials a=b=1; on branch1 run m+1. Surviving means every
prelude choice was use, giving respective probabilities rho and rho/2 and
scores m c and(m+1)c, at zero budget.

On the surviving branch j use the original repeated-use law, stopping at first
test failure or at N_j uses, with

    b=1/M, a_j=r_j/M, N_0=M+1, N_1=1,
    p_0=(1+r0/M)^(-(M+1)), p_1=(1+r1/M)^(-1),
    w_j=log(1+(b-a_j)^2/[2(a_j+b)(2-a_j-b)]).

Both successful branches have the **same actual final score**
L=(m+1)c+c/M. For branch probability alpha,

    P=rho [alpha p_0+(1-alpha)p_1/2],
    K=rho [alpha (2w_0/a_0)(1-p_0)
            +(1-alpha)(w_1/a_1)(1-p_1)].               (2)

K is the full-law expected original budget, not a conditional survivor cost.
The exact repeated-stage law is inherited from K2474; failed paths' costs are
included. Earlier crossing can only increase the crossing event, so P is a
sufficient lower bound, not a claim that every crossing ends at this score.

Take the rational ideal weight

    alpha*=[1/2+1/M^2-p_1/2]/[p_0-p_1/2].              (3)

Since exp(-r0)>1/2, this lies in(0,1) for all sufficiently large M and makes
P=epsilon+rho/M^2. To avoid assuming an arbitrary external coin, choose J with
2^J>=4M^3 and set alpha=floor(2^J alpha*)/2^J. J zero-risk fair routing bits
implement this dyadic weight exactly. It lowers P by less than rho/2^J, so
P>epsilon still holds. The rounding changes alpha by O(M^-3), below its
O(M^-1) leading term. After termination set a=b=0; all stopping laws are valid
with initially zero score and finite expected budget. The use targets and parameters are finite; pass-trial counts are geometrically unbounded. Termination is almost sure, not a deterministic trial-time cap.

## 2. Limit proves a necessary coefficient

For a=r b as b approaches0,
2w/a approaches k(r). Also

    p_0 -> exp(-r0),       1-p_1 ~ r1/M,
    M alpha -> r1/[2(exp(-r0)-1/2)].

Substitution in(2) gives

    M K/rho -> (r1/2)[k(r1)+H(r0)].

Since epsilon(L-log(1/epsilon))=rho c/(2M), the exact finite-law violation
threshold epsilon(L-log(1/epsilon))/K converges to(1). For every lambda<Lmix,
a sufficiently late finite M gives score strictly above
log(1/epsilon)+lambda K/epsilon and success probability strictly above epsilon.
This proves the lower bound; equality or infinite-time attainability is not
required. Arb enclosures certify the stated rational-parameter value and actual
finite witnesses; the analytic limit supplies the all-confidence theorem.

## 3. General construction envelope, not a global optimizer

For a common score c ell, choose finite prelude depths j<=floor(ell), weights
alpha_j, rates0<r_j<1, and integer N_j with b_j=(ell-j)/N_j<=1. Then

    q_j=2^-j (1+r_j b_j)^(-N_j),
    d_j=2^-j (2w_j/(r_j b_j))[1-(1+r_j b_j)^(-N_j)],
    P=sum alpha_j q_j,            K=sum alpha_j d_j.    (4)

A zero-length tail at ell=j has q_j=2^-j,d_j=0. For a fixed finite candidate
bank, finding the cheapest mixture with a prescribed P is a two-equality
linear program: its extreme optimum uses at most two branch types (normalization
and success mass). For rational candidate parameters, exact rational probabilities and real costs allow direct
pair comparison. This reduces search inside this family; it does not prove
that every adaptive experiment is such a mixture. An optimizer at P=epsilon
alone is not a violation: a feasible strict perturbation must be exhibited.
The dyadic construction above supplies that perturbation explicitly. For other
confidence levels the K2474 bound survives; no universal improvement at every
epsilon is asserted.

## 4. Verification and inference limits

Finite checks use exact rational p_j, rounded coin weights and margins, with
Arb256 log/exponential enclosures. They certify actual finite laws for multiple
M and dyadic confidences, direct stage-recursion costs, and the limit value.
Controls omit survivor weights or score-generating preludes, use an endpoint
success probability, or remove failed-stage costs. These altered laws fail the
same mathematical requirements. Finite checks, exact identities, asymptotic
proof and reused evidence are reported separately.

The gap to Csharp remains. The next discriminator is a larger adaptive stopping
variational law or an upper bound exploiting fixed confidence. No numeric search
here proves global optimality, physical calibration, novelty or external
certification. Random routing is independent and budget-free only because its
a=b=0 choices are explicitly part of the original experiment.

[Probe](../../tests/channel-swings/k2477_randomized_score_preludes_probe.py) and [report](../../lab/process/k2477-randomized-score-preludes.json).
