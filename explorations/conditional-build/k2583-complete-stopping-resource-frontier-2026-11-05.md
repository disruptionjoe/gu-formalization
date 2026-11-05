---
title: "K2583 Complete stopping resource frontier and price diagram"
status: active_research
doc_type: exploration
created: "2026-11-05"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: complete finite-resource frontier and all-positive-price optimizer for lambda through Lambda(S); larger multipliers open
scripts:
  - tests/channel-swings/k2583_complete_stopping_resource_frontier_probe.py
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
result: K2583
carrier: original fair stopping law with finite completed schedules and initial mixtures LAYER=toy CHIRALITY=N/A
pairing: unconditional expected success, leakage and positive-trial functional ON=declared_carrier
real_structure: real controls and multiplier; probability laws and private randomization
grading: stages, expected positive trials and pathwise trial counts kept distinct
action_owner: repository-construction -- stated conditional model
target: complete resource frontier and price selection MAP-TYPE=evaluation
```

# Finish every budget, then solve every positive price

## Result and scope

K2581's global support at its first count-change price forces a simpler result at every higher price: all multistage schedules consume more expected trials than the zero-action one-stage schedule. This closes the entire previously missing middle-resource range for every 0<S<=1/2 and 0<lambda<=Lambda(S). It also determines the optimizer for every positive trial price and supplies exact corner slopes, leakage/resource tradeoffs and original-law consumers.

This is independent mathematics for the stated fair stopping law. SC-META-53 remains UNCERTAIN; source, ledger0.263, canon and native GU physical judgments do not change. Expected positive trials are not a pathwise cap. No new multiplier range above Lambda, general intermediate optimizer, novelty or physical apparatus calibration is claimed.

## 1. Objects and complete theorem

Use K2581's completed schedules, 0<b_i, 0<=a_i<=b_i, sum b_i=S<=1/2,

    P_i=product_(j<=i)(1+a_j)^−1,
    p=P_n, C=2 sum_i P_i w(a_i,b_i), R=2 sum_i P_i,
    w(a,b)=log[1+(b−a)²/(2(a+b)(2−a−b))].

Write J=p−lambda C, Q(k)=sup(J−kR), and F(M)=sup_(R<=M)J over original admissible policies. Abort contributes zero. K2569 reduces original adaptive policies and countable strategy limits to initial mixtures of completed schedules and abort by INCREASING J and DECREASING R. Therefore a bound on J−kR for all completed schedules, k>=0, bounds the original policy class. This stronger resource-preserving reduction, not merely an unpriced value identity, is used below.

Define

    w0(b)=log[(4−b)/(4−2b)], c(b)=−w_a(0,b),
    H_n=n w0(S/n), Delta_n=H_n−H_(n+1),
    Lambda(S)=1/[2c(S)+4H_1−2H_2],
    M0=2/(1+S).

For EVERY 0<lambda<=Lambda(S), the complete frontier at finite M>=0 is

    F(M)=M/2,                                      0<=M<=M0;
    F(M)=M/2−lambda M w(2/M−1,S),                   M0<=M<=2;
    F(M)=1−2lambda[(1−theta)H_n+theta H_(n+1)],      M>=2,
           n=floor(M/2), theta=(M−2n)/2.            (1)

All values are ATTAINED by original policies. The first segment mixes abort with the free one-stage action a=b=S. The middle is the single schedule a=2/M−1,b=S. The tail mixes the adjacent n and n+1 zero-action equal-score schedules. The cutoff Lambda is sharp for this COMPLETE formula because K2581 proves the tail fails beyond it. This is NOT a sharpness theorem for the middle segment considered by itself.

## 2. A general price-domination lemma

Suppose at price k* a reference policy with cost R* globally supports J−k*R. Then for every competitor with R>=R*,

    J−kR <= J*−kR*−(k−k*)(R−R*) <= J*−kR*   (k>=k*).  (2)

This is a direct affine-price comparison; it needs no local first-order condition or numerical optimizer. It does not exclude competitors with smaller R.

For a completed schedule, log(1+a)<=a and sum a<=S imply P_i>=exp(−S). Consequently every n>=2 schedule has

    R>=2n exp(−S)>=4 exp(−1/2)>2.                 (3)

For example exp(1/2)<2 proves the strict final inequality. The coarse bound is sufficient; optimizing its constant would not change the endpoint.

K2581 proves the zero-action one-stage reference, J*=1−2lambda H1 and R*=2, is globally optimal at k1=lambda Delta1. Applying(2)–(3) shows that for every k>=k1 EVERY multistage schedule is dominated by this reference. Domination is strict for k>k1, not necessarily at k1, where the equal two-stage schedule ties. Smaller-resource one-stage policies remain candidates. Abort must also be retained.

Thus for k>=k1 the FULL original-policy optimum reduces to one-stage or abort. Mixtures cannot improve a linear priced objective; K2569 supplies the original-policy transfer.

## 3. Execute every middle-budget support

Set

    Mfun(a,S)=−2(1+a)w_a(a,S)+2w(a,S),
    k(a)=[1−lambda Mfun(a,S)]/2.

K2509's exact fixed-b strict convexity gives

    Mfun_a=−2(1+a)w_aa<0, Mfun(S,S)=0,
    Mfun(0,S)=2c(S)+2H1.

Therefore k(a) is strictly increasing from

    k0=[1−lambda(2c(S)+2H1)]/2

to1/2. Crucially

    k0−k1=[1−lambda/Lambda(S)]/2>=0.              (4)

Hence the global one-stage reduction applies at EVERY support k(a). At price k(a), the derivative of the one-stage value f(u)=[1−2k(a)−2lambda w(u,S)]/(1+u) has numerator

    lambda[Mfun(u,S)−Mfun(a,S)].

It is positive for u<a and negative for u>a, so a uniquely maximizes the one-stage value. For a<S its priced value is −2lambda w_a(a,S)>0, since w_a<0 before the diagonal. At a=S it is zero and ties abort. Thus no unaccounted abort optimum invalidates the support.

The chosen policy has R=M=2/(1+a). Its global support proves the middle line of(1) for all original policies with resource<=M. At M0, the free-stage policy has p=1/(1+S)=M0/2 and C=0. For any completed policy p<=R/2, so J<=R/2; the reduction gives the same upper bound for the original class. Abort/free-stage mixing proves the entire first line. The tail is K2581's already-established global theorem, reused rather than rederived.

## 4. Released complete positive-price diagram

Let k_n=lambda Delta_n. K2577/K2581 show these strictly decrease to0. For every k>0:

- If 0<k<k1, maximize J_n(k)=1−2lambda H_n−2kn over positive integers n. The optimal n satisfies k_n<=k<=k_(n−1), with the upper bound absent for n=1. Adjacent counts tie at k=k_n. No positive-action finite optimizer occurs in this region.
- At k=k1, the zero-action counts1 and2 tie; arbitrary mixtures of those policies also optimize.
- If k1<k<=k0, the zero-action single stage is the only completed-schedule optimizer. At the critical multiplier k0=k1 this open-left interval is empty.
- If k0<k<1/2, the unique completed-schedule optimizer is a in(0,S) solving Mfun(a,S)=(1−2k)/lambda, with b=S.
- If k=1/2, abort and the free single stage a=S tie, including their mixtures. If k>1/2, abort is optimal and all positive-stage schedules have negative priced value, since J<=R/2.

The last two branches use a strictly monotone scalar equation with a known bracket [0,S], so bisection with rigorous evaluations provides any prescribed action/value enclosure. This is an executable one-dimensional optimizer in this multiplier range, not the prohibitive multistage grid of K2575. Different implementations with the same original law are not asserted unique.

The threshold equality at k0 has a=0 and is covered by the corresponding endpoint; at lambda=Lambda and k0=k1 the count2 tie remains. These ties matter when converting prices into constrained mixtures.

## 5. Released shape and leakage consequences

The middle curve has

    F'(M)=k(a), F''(M)=lambda Mfun_a(a,S)/M²<0,
    a=2/M−1.

It joins the low-resource line with derivative1/2 at M0. At resource2,

    F'(2−)=k0, F'(2+)=k1,
    F'(2−)−F'(2+)=[1−lambda/Lambda(S)]/2.           (5)

Thus the corner is differentiable exactly at the critical multiplier. This extends K2581's critical-only statement to the entire multiplier range. Later even-budget corners have decreasing positive slopes k_n. No finite-budget plateau occurs: H_n>S/4 and H_n decreases to S/4, so

    F(M)<V=1−lambda S/2, lim_(M→infinity)F(M)=V.

The unrestricted value equals the supremum of finite-resource values: truncate any policy after N actual trials, declaring unresolved outcomes failures. Finite-hit success probabilities converge to p and nonnegative accumulated leakage increases to C; for finite C the objectives converge, while C=infinity cannot improve the finite optimum at lambda>0. Each truncation has expected trials at most N. Thus the displayed limit is the unrestricted V, not only a restricted-family limit.

For the whole tail the optimal policies have p=1. Consequently they also solve the separate problem of minimizing leakage among policies with CERTAIN success and expected resource<=M, M>=2:

    C_min(M)=2[(1−theta)H_n+theta H_(n+1)].        (6)

Indeed choose any lambda in the proved range and apply the global bound to a policy with p=1. The attained value then forces C>=the right side. This yields a lambda-independent exact leakage/resource tradeoff. The same certificate does not say these schedules minimize leakage without the success1 constraint: abort has zero leakage.

## 6. Original-law consumers and rigorous numbers

Use S=1/2, lambda=67/125=.536, M=8/5. This lies in the newly proved range above2/5 and below Lambda. The exact middle optimizer is

    a=1/4,b=1/2, p=4/5, R=8/5,
    w=log(31/30), C=(8/5)log(31/30),
    F=4/5−(536/625)log(31/30).                   (7)

Its supporting price is k(a); exact differentiation gives w_a(1/4,1/2)=−128/465, so Mfun=64/93+2log(31/30). Both k1<k0<k(a)<1/2 and the positive priced optimum are checked with rational logarithm enclosures. An incorrect fair-trial charge or an arbitrary mixture cannot be substituted for the expected resource.

At the same S,lambda, M=1 use the free one-stage policy with probability3/4 and abort otherwise. Then p=1/2, C=0, R=1 and F=1/2. At M=3, mix the zero-action one-stage and equal two-stage schedules equally; its p=1 and C=log(7/6)+2log(15/14) attain both(1) and(6).

A second total score S=1/4, lambda=59/100, M=9/5 gives a=1/9, b=1/4, p=9/10, R=9/5 and

    w=log(1559/1534), F=9/10−(531/500)log(1559/1534).

This checks the general-score extension outside the old half-score theorem. The probe evaluates logarithms by 12 positive atanh-series terms with a rigorous geometric tail, and stores rational lower/upper bounds. It also brackets the scalar price optimizer at the rational price3/10; no floating-point optimizer is used for acceptance.

## Controls and next condition

Controls test strict versus tied count support at k1, changed price direction, omitted failure trials, illegal use of the middle formula above resource2, leakage without the success constraint, and a lambda just above Lambda where the inherited feasible budget-restored policy defeats the old tail. Finite checks support the identities and concrete policies; the universal theorem is the proof in sections2–3 composed with K2581 and K2569.

The complete frontier through Lambda and the corresponding all-positive-price optimizer are now solved. The substantial probability successor is a globally certified positive-action/multistage frontier ABOVE Lambda, where the reference support in(2) is no longer available. K2565's lambda1.9 value bracket survives. No assertion that the middle formula fails immediately above Lambda is made.

[K2581 support and sharp tail](k2581-score-sensitive-tail-transition-2026-11-05.md), [K2575 earlier middle segment](k2575-constructive-priced-optimization-2026-11-05.md), [K2569 original-policy reduction](k2569-stopping-maximizing-sequences-2026-11-05.md), [probe](../../tests/channel-swings/k2583_complete_stopping_resource_frontier_probe.py), [report](../../lab/process/k2583-complete-stopping-resource-frontier.json). General [constrained occupation-measure results](https://arxiv.org/abs/2307.03158) provide background with different hypotheses; the price comparison here is proved directly.

Independent internal acceptance: field specialists cross-reviewed the concrete proofs and controls, then a distinct integrated hostile review returned no substantive findings. Exact producer/replay and native checks passed at the stated scope; no external or proof-assistant certification.
