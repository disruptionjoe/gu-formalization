---
title: "K2474 Fixed-confidence lower bounds and activation entropy loss"
status: active_research
doc_type: exploration
created: "2026-11-01"
classification: CONVENTIONAL_COMPARATOR
target_claim: "NONE-NOT-A-KILL"
claim_ceiling: "conditional lower bounds and rejected shortcut; exact fixed-confidence optimum remains open"
---

# K2474 Fixed-confidence lower bounds and activation entropy loss

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
result: K2474
carrier: original half-test half-use predictable binary absorbing-failure experiment LAYER=toy CHIRALITY=N/A
pairing: actual-law expectation and entropy ON=declared_carrier
real_structure: real coefficients and probabilities in the stated conditional models
grading: homogeneous degrees or classical reached-attempt histories as stated
action_owner: repository-construction -- supplied conditional mathematical models
target: Fixed-confidence expected-budget coefficient bounds MAP-TYPE=evaluation
```

## Result

K2471 gives the sharp coefficient C=(1+log2)^2/[4(1-log2)] uniformly over
confidence levels. At a fixed epsilon, a dyadic zero-budget prelude followed
by a repeated-use law proves the necessary lower bound

    C_epsilon >= C eta log(1/eta)/(1-eta),
    eta=2^m epsilon, m=max{integer m>=0: 2^(-m)>epsilon}.   (1)

Here 1/2<=eta<1. Thus every fixed confidence requires at least C log2,
while K2471 supplies C_epsilon<=C. The staircase lower bound is not asserted
to be exact or continuous. At an exactly dyadic epsilon, eta is 1/2, not1.
A naive independently activated one-use experiment cannot establish fixed-
confidence sharpness: activation supplies no initial score and incurs an
exact entropy deficit. These are conditional mathematical results on the
original classical law; SC-META-53 remains UNCERTAIN, ledger0.263 unchanged.

## 1. Original experiment and exact finite laws

Use K2468's predictable test-failure a, actual-use risk b, fresh half routing,
absorbing test failure and Z=c sum(use*b), c=log2, initially Z=0. For a<b,

    w=log(1+(b-a)^2/[2(a+b)(2-a-b)]),
    B=sum w; for a>=b set w=0.

C_epsilon is the infimum of coefficients lambda>=0 making crossing of
log(1/epsilon)+lambda K/epsilon have probability<=epsilon for every such
experiment and every justified bound E B<=K. No budget is estimated from
passing data.

With fixed a>0,b and stopping at Nth use or first failure,

    p=(1+a)^(-N), Zhit=N c b, E B=(2w/a)(1-p).           (2)

One successful use-stage has probability1/(1+a), expected length2/(1+a),
and expected budget2w/(1+a). Sum the N geometrically reached stages to
obtain (2). After termination set both risks zero. At any threshold<=Zhit,
the N-use event is a subset of crossing. Earlier crossings can only help
a lower-bound counterexample; (2) need not be the entire crossing law.

## 2. Dyadic prelude and the limiting lower bound

Run m steps with a=b=1, requiring each to be use. Tests fail immediately;
survival probability rho=2^(-m), survivor score m c=-log rho, and budget0.
Then use (2) with a=r b, 0<r<c. Fix rho>epsilon and eta=epsilon/rho.
Choose p_N>eta tending down to eta and

    b_N=(p_N^(-1/N)-1)/r.

For sufficiently large integer N, 0<a<b<=1. Full success has probability
rho p_N>epsilon. Exact expected budget is rho*(2w/a)(1-p_N), not a
conditional-on-survival budget. Taylor expansion at b=0, with a=r b, gives

    w/b -> (1-r)^2/[4(1+r)],
    Zhit -> (c/r)log(1/eta),
    E B_chain -> (1-r)^2(1-eta)/[2r(1+r)].

Consequently epsilon*(m c+Zhit-log(1/epsilon))/E B_total tends to

    R0(r) eta log(1/eta)/(1-eta),
    R0(r)=2(c-r)(1+r)/(1-r)^2.

Every smaller coefficient fails for a sufficiently late FINITE law with
strict success probability above epsilon. The inherited maximizer
r=(3c-1)/(3-c) gives R0(r)=C. The function
eta log(1/eta)/(1-eta) is increasing on(0,1), since its derivative has
numerator -log eta-1+eta>0. Choose the largest strictly allowed m to prove
(1) and its C log2 floor. If rho=epsilon, no p_N>eta=1 exists; taking a
continuity limit there would be invalid.

## 3. Why random activation alone does not transfer sharpness

Activate a first-use-or-failure experiment independently with probability
alpha; otherwise never add score. Its hit probability p=alpha/(1+a), score
c b, and K=2pw. Let s=1/(1+a). The initial conditional success probability
is s on activation and0 otherwise, so

    E[q0 log q0]-p log p=-p log alpha,
    p(c b+log p)=E J+p log alpha,

where E J=2p psi and psi=[c b-log(1+a)]_+/2 on the positive-score branch.
The displayed equality uses c b>log(1+a); otherwise replace E J by the
signed expression p(c b-log(1+a)) before taking its positive part.
For near-extremal b->0 and alpha near epsilon, the lost entropy approaches
epsilon log(1/epsilon), whereas E J tends to zero. Initializing score at
-log alpha would change the original experiment.

For epsilon<1/2 the one-use score<=c cannot cross any nonnegative-coefficient
threshold. At epsilon=1/2 any positive coefficient precludes crossing for
nontrivial positive budget; lambda0,b1 has a separate endpoint exception.
For epsilon>1/2, put h=log(1/epsilon), A=1/epsilon-1. Any positive-coefficient
violation needs b>h/c, a<A and p>epsilon, hence

    lambda <= epsilon*(c b-h)/(2p w)
           < (c b-h)/(2w) <= psi/w < C.

Since h/c>A, this region is compactly separated from b0 and a=b after
closure. K2471's continuous strict finite-pair inequality gives a strict
supremum gap below C for this whole activated one-use family. This does not
settle the optimum among all adaptive experiments.

Universal evidence is the exact stopped law, limiting construction, entropy
calculation and compactness argument. Exact rational/Arb256 finite laws certify
actual counterexamples and endpoint handling; grid checks are not optimization
proofs. Fixed confidence remains bracketed, not solved. No physical apparatus,
inferred leakage, novelty, external-expert or proof-assistant certification.

[Probe](../../tests/channel-swings/k2474_fixed_confidence_stopping_probe.py) and
[report](../../lab/process/k2474-fixed-confidence-stopping.json).
