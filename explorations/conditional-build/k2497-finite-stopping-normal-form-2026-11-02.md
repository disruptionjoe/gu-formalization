---
title: "K2497 Finite free-stage normal form and an all-policy cost bound"
status: active_research
doc_type: exploration
created: "2026-11-02"
classification: CONVENTIONAL_COMPARATOR
target_claim: "NONE-NOT-A-KILL"
claim_ceiling: "conditional original-law stopping mathematics; no sharp global optimum or physical implementation"
---

# K2497 Finite free-stage normal form and an all-policy cost bound

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
result: K2497
carrier: original fresh fair test/use absorbing experiment with failure-inclusive one-sided leakage cost LAYER=toy CHIRALITY=N/A
pairing: expectation under the actual probability law ON=declared_carrier
real_structure: real probability and real stage controls
grading: successful, failed and abandoned histories
action_owner: repository-construction -- supplied conditional stopping experiment
target: finite-stage dominance, all-policy analytic frontier bound and exact cost witness MAP-TYPE=evaluation
```

## Result, assumptions and relation to earlier work

For 0<S<=1/2, every finite successful schedule with success greater than the
zero-cost baseline 1/(1+S) is weakly improved by a schedule with at most one
free stage, placed first. The improvement is strict if there were two positive
free stages. Every positive zero-hazard stage can also be strictly improved by
splitting it. Separately, a closed-form lower bound on expected cost holds for
all adaptive policies, including abandoned and infinite histories. It improves
the elementary K2485 square-root bound but does not replace K2491's tighter
certified small-budget example or solve the global optimum.

The supplied positive probability model, fresh fair routing, trial cost,
geometric retry support and ability to randomize initially are assumptions.
SC-META-53 remains UNCERTAIN; LT-SM8/LT-GR6b retain native state/quotient/domain
debts. No source, physics ledger0.263, canon, physical recovery, hardware or
novelty claim changes. This is independent conditional mathematics.
K2495 owns adjacent exchange and its continuum variational problem. K2485
owns reduction of the full adaptive supremum to mixtures of finite schedules.
The finite reductions below preserve exact success and score; the global bound
has a separate actual-law proof and does not assume that reduction.

## 1. The finite normal form

Use 0<=a_i<=b_i and sum b_i=S. Put

    w(a,b)=log(1+(b-a)^2/[2(a+b)(2-a-b)]),
    P_i=product_{j<=i}(1+a_j)^(-1), p=P_n,
    C=sum_i 2 P_i w(a_i,b_i).

Idle (0,0) is removed. A free stage has a=b>0; a costly stage has b>a.
K2495's adjacent exchange places all free stages first at no greater cost.
Let their total score be T, and write their product as product(1+b_i)=1+B.
Let A=sum of the remaining a_i, and M=1/p. Nonnegative product expansion gives

    M-1 >= B+A.

In the high-success region p>1/(1+S), M-1<S, so B+A<S.
The costly score slack is S-T-A; the increment required to replace the free
prefix by its single equal-product stage (B,B) is Delta=B-T>=0, and

    S-T-A > B-T=Delta.

Therefore choose 0<=delta_i<=b_i-a_i on the costly stages with
sum delta_i=Delta. Replace the free prefix by (B,B) and each costly stage by
(a_i,b_i-delta_i). All controls remain admissible, B<S, total score is exactly
S and total success is exactly p. Every paid-stage survival weight P_i is
unchanged. At fixed a, w is strictly increasing for b>a, since

    d/db [(b-a)^2/(2(a+b)(2-a-b))]
      =(b-a)(3a+b-2a^2-2ab)/[(a+b)^2(2-a-b)^2] >0.

The final positivity holds on 0<=a<b<=S<=1/2. Thus C cannot increase,
and it strictly decreases when Delta>0 (two or more positive free stages).
Reducing a paid b to a may create new free stages. Repeat the same operation
after sorting: any such new free stage either survives as the sole free stage
or merges in a subsequent step; every coalescence reduces the stage count.
The process terminates with at most one positive free prefix and no greater
cost. It does not bound the number of positive-cost stages or prove finite
optimal-policy attainment.

For an initial mixture, any component with p<=p0=1/(1+S) and positive cost
can be replaced by probability p/p0 of the one free stage (S,S), otherwise
immediate abandonment. This keeps component success p at zero cost. Therefore
K2485's near-optimal finite-mixture representation may be chosen with low-success
components of zero cost, and high-success components in the stated normal form.
No assertion about every optimizer or pathwise adaptive normal form follows.

## 2. Exact finite improvement and the zero-hazard boundary

The three-stage schedule

    (1/10,1/10), (1/10,1/10), (1/20,3/10)

becomes

    (21/100,21/100), (1/20,29/100).

Both have S=1/2 and p=2000/2541. Their cost difference is

    (4000/2541) log(687157/685146) > 1/250.

The probe checks the rational logarithm argument and proves the last inequality
using log(1+x)>=x/(1+x). This is a strict improvement of that actual schedule,
not a comparison with the unknown optimum.

For a=0 the stage function is

    f(b)=w(0,b)=log((4-b)/(4-2b)), f(0)=0,
    f''(b)=1/(2-b)^2-1/(4-b)^2 >0.

Consequently f(b1)+f(b2)<f(b1+b2) for b1,b2>0 with total<=S.
Replacing a positive zero-hazard stage by two such stages preserves all
survival weights and success, and strictly lowers cost. No finite minimizing
schedule can contain one; an optimizing sequence may have infinitely many
small stages, and K2495's zero-ratio continuum suffix remains possible.
This gives a reason not to infer finite attainment from finite normal forms.

## 3. A universal actual-law lower bound

Allow the original adaptive trial controls 0<=a,b<=1 and early abandonment.
Each reached trial chooses controls before a fresh fair test/use coin. The
test branch fails with conditional probability a; the use branch adds b to
score. A failed or completed history stops. Define success probability p and
expected cost K=E sum w, including failed paths; for a>b the one-sided cost
is zero. Overshooting final score is harmless to the proof below.

For d=(b-a)_+ and u=a+b, with the zero case interpreted continuously,

    w(a,b) >= d^2/(4u).

For b>a this follows from log(1+x)>=x/(1+x) and

    4(a+b)-[2(a+b)(2-a-b)+(b-a)^2]=a^2+6ab+b^2>=0.

The inequality is strict whenever d>0. For a>=b both sides are zero.
Let A=E sum a, B=E sum b, D=E sum d, over all reached trials. Nonnegative
Tonelli summation and the fresh coin give

    A=2 P(failure)<=2(1-p),
    B=2 E(total use score)>=2Sp,
    B<=2(S+1).

The last bound uses that score before hitting is below S and the last
increment is at most one; it also covers nonhitting infinite histories.
No finite expected trial duration is assumed. A is finite from its exact
failure identity; hence Cauchy-Schwarz on the expected trial-count measure gives

    K >= D^2/[4(A+B)] >= (B-A)_+^2/[4(A+B)].

The zero denominator case is separate and trivial. For B>A the last expression
increases with B and decreases with A. In the high-success region p>p0,
substituting the preceding bounds yields

    K >= L_S(p) = ((1+S)p-1)^2 / [2(1+(S-1)p)].         (1)

Set L_S(p)=0 below p0. In fact K>L_S(p) for every actual high-success policy:
D>=B-A>0 implies positive expected measure of trials with d>0, where the
stage inequality is strict. This does not imply a uniform positive gap for
a sequence of policies. The bound therefore applies non-strictly to a supremum.
At p=1 it recovers nonattainment of K=S/2, already established by K2485.

For 0<=K<=S/2, solving the quadratic gives the explicit upper bound

    F_S(K) <= [1+S-(1-S)K
                +sqrt(4S(1+S)K+(1-S)^2 K^2)]/(1+S)^2.  (2)

For larger budgets cap the bound at one. At K=0 it equals p0. Its small-K
leading increment is 2 sqrt(S K)/(1+S)^(3/2), sharper than K2485's
2 sqrt(S K). At S=1/2,K=1/1000, (2) is below 691/1000. K2491's upper bound
684885741753/10^12 is tighter at that point; the new formula's value is its
closed all-S/all-budget proof, not a new best numerical certificate.

## Verification, scope and next question

The probe checks rational schedule identities and strict cost improvement,
symbolic derivative/convexity/quadratic identities, finite illustrative
occupancy cases and genuine wrong-cost/order/constraint controls. Universal
termination, Tonelli and Cauchy arguments are above and receive independent
internal review. Finite coverage is not a count of independent theorems.

The remaining original-law problem is the number and placement of costly
finite atoms and small-stage intervals. A normal form, strict improvement or
nonattainment does not supply a global all-control Bellman equality. The
current results remove redundant free-prefix search and give a closed analytic
constraint; they leave sharp positive-budget attainment and the optimal mixed
atomic/continuous policy unresolved.

[Probe](../../tests/channel-swings/k2497_finite_stopping_normal_form_probe.py),
[report](../../lab/process/k2497-finite-stopping-normal-form.json),
[ordering and continuum](k2495-stopping-order-and-continuum-2026-11-02.md),
[adaptive frontier](k2485-constrained-stopping-frontier-2026-11-01.md).
The quadratic-over-linear convexity method is standard; see
[Boyd and Vandenberghe](https://stanford.edu/~boyd/cvxbook/). No novelty claim.
