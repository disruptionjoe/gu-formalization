---
title: "K2585 Eventual exact stopping tail above the complete-frontier transition"
status: active_research
doc_type: exploration
created: "2026-11-05"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: sufficient eventual exact tail above Lambda(S), with explicit onset bounds; low budgets and larger multipliers remain open
scripts:
  - tests/channel-swings/k2585_eventual_stopping_tail_probe.py
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
result: K2585
carrier: original fair stopping law with finite completed schedules and initial mixtures LAYER=toy CHIRALITY=N/A
pairing: unconditional expected success, leakage and positive-trial functional ON=declared_carrier
real_structure: real controls and multiplier; probability laws and private randomization
grading: stages, expected positive trials and pathwise trial counts kept distinct
action_owner: repository-construction -- stated conditional model
target: above-transition eventual resource frontier and certificate onset MAP-TYPE=evaluation
```

# A broken first chord does not destroy every later chord

## Result and scope

For the original fair stopping law, the exact zero-action optimal tail returns at sufficiently large finite expected budgets for a nonempty interval ABOVE the sharp all-budget transition of K2581/K2583. We give a global support certificate, an explicit finite onset bound, its asymptotic cost, and two policies at the SAME multiplier: a low-budget counterpolicy and a rigorously optimal high-budget mixture. This is a new partial frontier above the complete-frontier range, not a complete positive-action optimizer.

The result is independent mathematics. SC-META-53 remains UNCERTAIN. No native GU probability, apparatus calibration, physical positivity, novelty or pathwise-trial theorem follows. Source claims, ledger0.263 and canon are unchanged.

## 1. Objects and a stronger global support criterion

Retain the original schedules and adaptive-policy reduction of K2569:

    0<b_i, 0<=a_i<=b_i, sum b_i=S<=1/2,
    P_i=product_(j<=i)(1+a_j)^(-1), p=P_n,
    C=2 sum_i P_i w(a_i,b_i), R=2 sum_i P_i,
    w(a,b)=log[1+(b-a)^2/(2(a+b)(2-a-b))].

Abort has value zero. Put Q=sup(p-lambda C-kR) at lambda,k>0 and

    w0(b)=log[(4-b)/(4-2b)],
    c(b)=-w_a(0,b)=2(3-2b)/[(2-b)(4-b)],
    H_n=n w0(S/n), Delta_n=H_n-H_(n+1),
    J_n(k)=1-2lambda H_n-2kn, Q0(k)=max_(n>=1)J_n(k).

**Global criterion:** if Q0(k)>=2lambda c(S), then Q=Q0 and every finite maximizing completed schedule has zero actions and equal scores at its count. The criterion is sufficient; its failure is not a counterexample.

Proof. K2571 gives a finite maximizing schedule or abort at positive k, and the hypothesis forces Q>=Q0>0. In a maximizing schedule, each priced suffix value V_i is positive and V_i>=Q: every preceding map x -> (x-2lambda w-2k)/(1+a) strictly decreases positive x, while a nonpositive suffix cannot yield a positive full value. A positive a_i permits a small feasible decrease, including when a_i=b_i. Its first-order condition and strict fixed-b convexity give

    0<=partial_(a_i)V_i=[-2lambda w_a(a_i,b_i)-V_i]/(1+a_i),
    V_i < 2lambda c(b_i).

Thus c(b_i)>c(S). K2581 proves c increasing on [0,S/2] and c(S/2)<=c(S) for S<=1/2. Therefore b_i>S/2 and at most one action is positive. The exact adjacent exchange identity, with c_A=lambda w_A+k,

    J(AB)-J(BA)=2(a_A c_B-a_B c_A)/[(1+a_A)(1+a_B)]

up to its positive common prefix, puts that sole positive action first. All survival factors then equal1/(1+a). K2581's JOINT convex supporting plane at b0=S/m is strict for a>0 and gives

    sum_i w(a_i,b_i)>H_m-c(S/m)a.

Here c(S/m)<=c(S), including m=1. Hence

    J < [J_m(k)+2lambda c(S/m)a]/(1+a)
      <= [Q0+Q0 a]/(1+a)=Q0,

contradicting maximality. All actions vanish; strict Jensen makes scores equal. Equality in the hypothesis causes no exception because a>0 supplied strictness. K2569's reduction INCREASES unpriced value and DECREASES expected resource; therefore this bounds the entire original adaptive and countable class, not merely deterministic schedules. The positive-price finite-attainment result supplies the finite optimizer used in the argument.

## 2. Execute the eventual frontier

Define

    T_n=(n+1)H_n-nH_(n+1),
    B_n(S)=1/[2(c(S)+T_n)],
    L(S)=1/[2c(S)+S/2].

Strict convexity of H(t)=t w0(S/t) implies Delta_n decreases strictly to zero. At k_n=lambda Delta_n, precisely the zero-action counts n,n+1 tie at Q0=1-2lambda T_n. If lambda<=B_n, section1 makes this a GLOBAL support. Their mixture therefore attains

    F(lambda,M,S)=1-2lambda[(1-theta)H_n+theta H_(n+1)],
    n=floor(M/2), theta=(M-2n)/2.                  (1)

for M in[2n,2n+2]. Moreover

    T_n-T_(n+1)=(n+1)(H_n-2H_(n+1)+H_(n+2))>0,
    T_n -> S/4.

So B_n strictly increases to L, and lambda<=B_N proves(1) for EVERY M>=2N. B1=Lambda(S), the old sharp ENTIRE-tail threshold. For Lambda<lambda<L an N exists: this is a nonempty new regime. At equality lambda=B_N, the first supported chord and all later chords are included. At lambda=L no finite N satisfies this certificate, but no failure of the optimal formula is inferred.

The certificate also solves every sufficiently small positive price: since Q0(k) is nonincreasing in k, lambda<=B_N implies Q=Q0 for all 0<k<=k_N. Optimal counts are selected by k_n<=k<=k_(n-1), with adjacent-count ties at k=k_n. This gives a practical integer optimizer in this price region. It says nothing universal about higher prices or lower budgets above Lambda.

## 3. Released explicit onset and asymptotic cost

The positive convergent series

    H_n=sum_(m>=1) S^m(2^(-m)-4^(-m))/(m n^(m-1))

shows, using 1-(n/(n+1))^(m-1)<=(m-1)/(n+1),

    0<T_n-S/4
      <= S^2/(16n)[4/(1-S/(2n))-1/(1-S/(4n))]
      <= 2S^2/(7n).                              (2)

Indeed the bracket equals(3-2x)/[(1-2x)(1-x)] for x=S/(4n)<=1/8; numerator<=3 and denominator>=21/32, giving(2). The m=1 term is exact and the geometric-series sum treats every higher term, not a finite Taylor sample.

Thus for any 0<lambda<L,

    Nsafe=max(1,ceil[4lambda S^2/(7(1-lambda/L))])  (3)

suffices, including when the expression is an integer. Exact B_n evaluation often lowers this conservative bound.

For the minimal CERTIFICATE count Ncert(lambda)=min{n:lambda<=B_n}, write A=3S^2/32 and B=7S^3/192. The convergent series yields

    H_n=S/4+A/n+B/n^2+O(n^-3),
    T_n=S/4+2A/n+(-A+3B)/n^2+O(n^-3),
    L-B_n=3L^2 S^2/(8n)+O(n^-2).

For fixed S>0 as lambda increases to L from below,

    Ncert(lambda) ~ 3L^2 S^2/[8(L-lambda)].        (4)

Monotonicity of B_n and sandwiching its positive leading1/n term prove the inverse asymptotic despite integer rounding. This is the cost of this sufficient certificate, not a necessary resource divergence of true optimizers. The old K2577 value-gap asymptotic applies to the now-certified eventual tail as well:

    V-F(M)=3lambda S^2/(8M)+7lambda S^3/(24M^2)+O(M^-3)

at even M; at non-even M, interpolation can change the order M^-3 term but preserves the displayed first two terms. Here V=1-lambda S/2 follows by finite-trial truncation and the eventual exact tail as in K2583. This extends that unrestricted value identity to this regime without solving lower budgets.

## 4. Same multiplier, two different budget regimes

Take S=1/2 and lambda=11/20=.55. Then

    L=84/149=.563758389...,
    B2=.549963396..., B3=.554417128...,
    B2<11/20<B3; Ncert=3, Nsafe=4.

All M>=6 therefore have the EXACT frontier(1). At M=7 mix equally zero-action equal3 and equal4 schedules. These original policies have p=1, R=7 and

    C=3log(23/22)+4log(31/30),
    F=1-(11/20)[3log(23/22)+4log(31/30)]
      =.85451698155... .                          (5)

The global support is k3=(11/20)[3log(23/22)-4log(31/30)]>0.

At the SAME lambda, the old resource3 chord is NOT optimal. Take the one-stage policy a=1/1000,b=1/2, for which w=log(1750999/1501998), and mix it with the zero-action equal2 schedule using weights1001/2004 and1003/2004. Their original expected resource is exactly3. The gain over the old chord is

    (11/20)log(7/6)-(275/501)log(1750999/1501998)
      -(11/10020)log(15/14)-1/2004
      >1/100000.                                 (6)

This is a constructive low-budget counterpolicy, not a claim it is optimal. It directly rules out extending the whole old tail unchanged while demonstrating rigorous recovery of later chords. All logarithmic inequalities and values here use rational atanh-series bounds with positive remainder; the probe never uses floating optimizer output for certification.

## 5. Execute the full criterion price window

Define q_m=[1-2lambda(H_m+c(S))]/(2m). The global criterion of section1 is exactly 0<k<=kcert, where kcert=max_m q_m, whenever lambda<L. Write A=1-lambda/L>0. Since H_m>S/4, q_m<A/(2m), while q_m becomes positive for sufficiently large m. A certified positive incumbent q_j>=qlo>0 therefore reduces the maximum to a FINITE integer search: indices m>A/(2qlo) cannot improve it. For rational or certifiably represented inputs, use rational logarithm bounds on the remaining indices to enclose the finite maximum to any requested accuracy. The finite max expression defines the threshold exactly; general exact ties need not be decidable by interval refinement. This encloses the threshold of the sufficient criterion, not the largest true zero-action price window.

For S=1/2,lambda11/20, exact interval comparisons over m=1,...,5 with the proved tail exclusion give the unique maximizing count3 and

    .002535657570 < kcert < .002535657571.

Every price up to this certified window uses the zero-action integer optimizer; it extends beyond the first certified chord price k3. The count2 change price is larger than kcert and is not licensed by this criterion. At lambda>=L all q_m<0, so this certificate supplies no positive price window; the true optimizer question remains separate.

For a second total score, S=1/4,lambda3/5 lies above Lambda(S) and below L(S). Exact support at N=2 proves every budget M>=4 has formula(1). This checks the variable-score extension rather than extrapolating the half-score example.

## 6. Scope, controls and next question

B_n is NOT claimed sharp for each individual chord. The known first-action failure threshold uses c(S/n), giving 1/[2c(S/n)+2T_n]; for n>=3 it differs from B_n. No necessity is proved by the sufficient onset bound or its divergence. Above-L, intermediate positive-action multistage policies, the unproved interval of budgets below the certified tail, and pathwise trial caps remain open. K2565's lambda1.9 bracket survives.

Controls alter survival/failure-trial accounting, mixing weights, the support inequality, count range, and asymptotic constants, and test the genuine positive-action budget3 gain. Finite exact checks certify these identities and consumers; the continuum/global conclusions are sections1–3 with their named prerequisites. The next consequential test is a score-dependent global support that either closes the gap between B_n and the known failure threshold or supplies the true finite-budget positive-action optimizer.

[K2581 joint convexity and action exclusion](k2581-score-sensitive-tail-transition-2026-11-05.md), [K2583 complete low-multiplier frontier](k2583-complete-stopping-resource-frontier-2026-11-05.md), [K2569 original-policy reduction](k2569-stopping-maximizing-sequences-2026-11-05.md), [K2571 positive-price attainment](k2571-stopping-resource-price-2026-11-05.md), [probe](../../tests/channel-swings/k2585_eventual_stopping_tail_probe.py), [report](../../lab/process/k2585-eventual-stopping-tail.json).

Independent internal acceptance: field specialists cross-reviewed both constructions and a distinct integrated hostile review returned no remaining findings. Exact producer/replay and affected native checks passed. This is internal review, not external or proof-assistant certification.
