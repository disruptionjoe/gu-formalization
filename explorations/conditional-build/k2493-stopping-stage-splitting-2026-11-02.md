---
title: "K2493 Two stages beat every initial mixture of single-stage policies"
status: active_research
doc_type: exploration
created: "2026-11-02"
classification: CONVENTIONAL_COMPARATOR
target_claim: "NONE-NOT-A-KILL"
claim_ceiling: "conditional mathematics on the declared supplied model; no native GU or measured implementation claim"
---

# K2493 Two stages beat every initial mixture of single-stage policies

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
result: K2493
carrier: original fresh fair test/use absorbing experiment with failure-inclusive one-sided leakage cost LAYER=toy CHIRALITY=N/A
pairing: positive trace or actual-law expectation on the supplied model ON=declared_carrier
real_structure: complex adjoint for quantum states; real probability for classical histories
grading: target/complement or absorbing test/use histories
action_owner: repository-construction -- supplied conditional mathematical models
target: Convex single-stage cost frontier, exact equal-success splitting discriminator and certified separation MAP-TYPE=evaluation
```

## Result and Layer 0

At target S=1/2 and expected budget K=317/10000, an explicit two-stage policy
attains success10/13. Every initial mixture of single-stage policies has success
at most10/13-163/5616000. This is a strict structural separation in the
original law, not a grid comparison or an exact unrestricted optimum.

Here one stage means a fixed pair (a,b) repeated until one successful use or
failure, then stopping. Continuing the same pair through several uses is a
multistage policy. The exclusion includes arbitrary initial randomization of
single stages and abstention, not arbitrary policies with multiple uses.

The supplied model imports fair routing and ordinary positive probabilities.
SC-META-53 remains UNCERTAIN; ledger0.263 LT-SM8/LT-GR6b retain their native
positive-quotient/domain debts. No source, ledger, canon, physical-credit,
novelty or hardware conclusion changes.

## 1. Keep the original law and failed paths

For a<b, write

    w(a,b)=log(1+(b-a)^2/[2(a+b)(2-a-b)]),

and w=0 for a>=b. A stage's survival is1/(1+a), expected cost2w/(1+a),
and successful score increment b. Two stages have

    P=1/[(1+a1)(1+a2)],
    C=2w(a1,b1)/(1+a1)+2w(a2,b2)/[(1+a1)(1+a2)].

These expectations charge failed paths. K2485 clipping permits b<=S and0<=a<=b
for optimal successful stages. A successful single stage can use b=S; overshoot
only increases its cost at fixed a. For lower success than the free baseline
p0=1/(1+S), randomize a free stage with abstention.

## 2. The entire single-stage mixture frontier is convex

For 0<S<=1/2 and p0<=p<=1, put a=1/p-1 and

    C_S(p)=2p*w(a,S).

Extend C_S(p)=0 on0<=p<=p0. This is strictly convex above p0. To prove it,
write u=a+S and

    R=2(1-S)+2sqrt((1-S)^2+S^2),
    T=-2(1-S)+2sqrt((1-S)^2+S^2).

The numerator inside the logarithm is (R-u)(u+T), while its denominator is
2u(2-u). Here R>=2, T>0 and0<u<2; direct differentiation gives

    w_aa=1/u^2+1/(2-u)^2-1/(R-u)^2-1/(u+T)^2 >0.
    C_S''(p)=2*w_aa/p^3 >0.

Each paired difference is nonnegative, the T difference strictly positive.
At p0, w=w_a=0, so the zero extension is convex with matching derivative.
For p>p0, w>0 and w_a<0, hence C_S is strictly increasing. Jensen therefore
bounds the cost of any initial mixture below by C_S of its average success.
Abstention and nonoptimal one-stage controls do not evade it. This argument
covers arbitrary probability mixtures by boundedness/continuity, not just
finite lists. No analogous convexity of the unrestricted adaptive frontier is
being assumed.

## 3. Exact infinitesimal prefix-splitting criterion

Start with interior0<a<S. Insert a tiny prefix, retaining the same total
score and success:

    (a1,b1)=(r*t,t),
    (a2,b2)=((a-r*t)/(1+r*t),S-t), 0<=r<=1.

For each fixed r all constraints hold for sufficiently small positive t.
Let g(r)=(1-r)^2/[2(1+r)], A=-2w_a(a,S), B=2w_b(a,S)/(1+a). The actual
failure-inclusive cost has derivative at t0

    C'(0)=g(r)+A*r-B.

The first stage contributes g; the second contributes A*r-B. Since
 g'(r)=1/2-2/(1+r)^2, A>=0, the minimizing ratio is
max(0,2/sqrt(1+2A)-1). The minimum is

    2sqrt(1+2A)-A-2-B, if A<=3/2;
    1/2-B,             if A>=3/2.

In the first case it is negative exactly when
(A+B)^2+4(B-A)>0, by squaring positive sides. This provides a rational local
split discriminator at rational a,S. Equality is only a first-order boundary;
it does not settle higher order or finite splits.

At S=1/2,a=3/10, A=125/294, B=575/1911. The rational choice r=1/2 gives
C'(0)=-19/3822. The next section supplies an actual finite witness, so the
result does not rest on an unpriced infinitesimal argument.

## 4. Finite separation with rational logarithm bounds

Take

    (a1,b1)=(1/200,1/100),
    (a2,b2)=(59/201,49/100).

Their total score is1/2 and (1+a1)(1+a2)=13/10, so P=10/13 exactly. Cost is

    (400/201)log(2383/2382)
      +(20/13)log(1+15594601/770157598).

For0<=x<=1, x-x^2/2 <=log(1+x)<=x-x^2/2+x^3/3. These bounds follow by
integrating the geometric expansion of1/(1+x), with its signed remainder.
Applying the upper bound to both terms gives exactly

    C <=23953698080207568695086312488346395340/
         756214107135085584280098236052573693831
      <317/10000.

The single stage with the same success uses a=3/10,b=1/2 and costs
(20/13)log(49/48). Its rational lower bound is475/14976, exceeding K by
163/9360000. Convexity already separates every single-stage mixture from the
two-stage witness at success10/13.

For an explicit probability gap, the derivative at p*=10/13 is

    C_S'(p*)=2log(49/48)+325/588 <1/24+325/588 <3/5.

For p<=p*, convexity and the tangent give
C_S(p)>=475/14976+(3/5)(p-p*). For p>p* monotonicity already exceeds the
budget. Therefore

    F_single-stage-mixtures(317/10000)
        <=10/13-163/5616000
        <10/13<=F_full(317/10000).

Geometric pass loops have finite expectation but unbounded trial support;
there is no fixed trial cap claim. A randomized mixture cannot be rejected
by comparing only pure policies; the convexity theorem is essential here.

## 5. What this says about the previous tiny-budget certificate

K2491's actual witness a=2309/5000,S=1/2 has strictly positive minimum prefix
insertion derivative. The probe proves this without floating point using
4(1+2A)>(A+B+2)^2 and0<A<3/2. Thus this particular counterexample mechanism
does not immediately improve that witness. This is only infinitesimal prefix
stability, not a proof that one stage is optimal at K=1/1000.

A tiny suffix has different coefficients:
A_tail=(1+a)A+2w, B_tail=(1+a)B, and derivative
[g(r)+A_tail*r-B_tail]/(1+a). Finite interior splits and initial randomization
of multistage policies remain separate. The new larger-budget separation
invalidates a global one-stage merge conjecture; it does not invalidate
K2491's all-policy upper certificate or determine its exact optimum.

## Evidence and next question

Independent probability review supplied the candidate convexity and splitting
argument; root independently checked the symbolic identities, exact finite
law, logarithm brackets, gap and local small-budget sign. An initial probe
sign error in the derivative identity failed and was corrected before any
result was accepted. Contrary controls change failure combination, prefix
survival charges, budget or admissible control domains. Finite controls do
not replace the universal Jensen proof. No external-expert or proof-assistant
certification is claimed.

Next: solve the genuinely multistage frontier using a structural Bellman
certificate or characterize the region where every stage split can be
merged. A locally positive derivative alone cannot prove that region. The
native positive quotient, matter/light source/readout and ordinary mixed-hook
inverse remain independent unresolved constructions.

[Probe](../../tests/channel-swings/k2493_stopping_stage_splitting_probe.py),
[report](../../lab/process/k2493-stopping-stage-splitting.json),
[all-policy certificate](k2491-analytic-stopping-certificate-2026-11-02.md),
[original constrained frontier](k2485-constrained-stopping-frontier-2026-11-01.md).
