---
title: "K2513 Exact Schur defect extends the global stopping frontier"
status: active_research
doc_type: exploration
created: "2026-11-02"
classification: CONVENTIONAL_COMPARATOR
target_claim: "NONE-NOT-A-KILL"
claim_ceiling: "conditional supplied-model mathematics; no native GU realization or unrestricted-budget frontier"
---

# K2513 Exact Schur defect extends the global stopping frontier

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
result: K2513
carrier: original fresh fair test/use stopping law at 0<S<=1/2 LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert trace or original failure-inclusive probability cost ON=declared_carrier
real_structure: complex adjoint for effects; real probabilities for stopping
grading: original verifier sectors or finite stopping stages
action_owner: repository-construction -- supplied instruments and original probability law
target: all-policy Bellman certificate and exact constrained stopping frontier MAP-TYPE=evaluation
```

## Result and scope

One stage is globally optimal for every original-law score 0<S<=1/2 and multiplier lambda>=4. At S=1/2 every budget 0<=K<=1/200 has the exact one-stage optimum. This extends K2511's sufficient multiplier 5 and guaranteed budget 1/315. The new ingredient is an exact negative correction to the first-stage Schur estimate, combined with a tighter ratio domain. It bypasses K2511's demonstrated limitation of its old proof template at lambda9/2; no more precise inversion of an already solved budget is the result.

This is GU-independent supplied-model probability mathematics. SC-META-53 remains UNCERTAIN; LT-SM8/LT-GR6b and native matter/light/domain obligations remain unchanged. Ledger0.263, source polarities, canon and physical credit do not change. No novelty, external-expert, experimental or proof-assistant certification is claimed. The all-adaptive transfer uses K2483/K2485 and the written argument below; exact fixture counts are not universal theorem counts.

## 1. Law, value and a tighter ratio domain

For 0<=a<=b<=s<=1/2 let

    w(a,b)=log(1+(b-a)^2/[2(a+b)(2-a-b)]), w(0,0)=0,
    U_lambda(s)=max_(0<=a<=s) [1-2lambda w(a,s)]/(1+a).

A finite completed schedule has total score S, P_i=product_(j<=i)(1+a_j)^(-1), success p=P_n and original failure-inclusive cost C=2sum_i P_i w(a_i,b_i). K2483/K2485's schedule-mixture and least-supersolution reductions include adaptive controls, clipping/free stages, abandonment, mixtures and limiting schedules. No continuum tail replaces this law.

Put A=1+a, x=(b-a)^2/[2(a+b)(2-a-b)], k=-w_a and M=2Ak+2w. K2509 proves w_aa>0, M_a=-2A w_aa<0, unique interior maximum M=1/lambda when lambda>1, positivity of U, and the smooth ratio extension through s=0.

The new ratio estimate is

    2k(rb,b)>=-g'(r)=2/(1+r)^2-1/2,
    g(r)=(1-r)^2/[2(1+r)], 5/8<=r<=1, 0<=b<=1/2.  (1)

This is an exact rational certificate: after cancellation and r=5/8+3X/8,b=Y/2, its numerator has degree(5,2) and all Bernstein coefficients are nonnegative; every denominator factor has a fixed nonzero sign whose product is positive. The probe reconstructs the rational function from the original logarithm. The b=0 and r=1 values are continuous limits, not divisions by zero.

Only the r=5/8 boundary of (1) is needed for the domain admission, avoiding circularity. There 2k>=87/338>1/4, with exact gap5/676. Since M>=2k and M decreases strictly with a, the one-stage maximizing root for lambda>=4 lies above a=5s/8. Therefore

    U_lambda(s)<=v(s)=1/(1+5s/8).                       (2)

For fixed s minimize the original Bellman residual

    E_s(a,b)=(1+a)U_lambda(s)+2lambda w(a,b)-U_lambda(s-b),
    m_s(b)=min_(0<=a<=b) E_s(a,b).

Its unique interior a-minimizer satisfies k=U_lambda(s)/(2lambda)<=1/8. At a=5b/8, (1) gives k>=87/676>1/8. Because k decreases strictly with a, this minimizer also has r=a/b>5/8. Both uses cover all b>0; b=0 is handled by the smooth limits. At r=1, k=0 and all relevant canceled identities extend continuously.

## 2. The exact Schur defect and envelope curvature

Define, with continuous canceled extensions,

    Q(r,b)=[w_bb-w_ab^2/w_aa]/w_a^2 at a=rb,
    M_up=-2A w_a+2x >= M,
    F(a,b)=2[(w_ab-w_b/A)^2-w_bb*w_aa]/[A*M_up*w_aa].

Two whole-rectangle certificates on 5/8<=r<=1,0<=b<=1/2 are

    Q(r,b)<=4-14(1-2b)k(rb,b),                         (3)
    F(rb,b)>=7/[10(1+b)^3].                            (4)

For (3), the numerator degree is(14,7); all120 Bernstein coefficients are nonnegative, minimum0. Equality at r=1 is real and a strict whole-rectangle claim would be false. For (4), degree(11,8) gives108 strictly positive coefficients with minimum10543/64. The probe certifies every denominator sign, and reconstructs each polynomial in the Bernstein basis. Coefficient nonnegativity and the partition-of-unity property prove the inequalities everywhere, including the canceled limits.

The key gain is the actual Schur complement, not the former radial upper bound. For example its b=0 limit is

    Q(r,0)=(r+1)^2(3r^2+10r+3)/(r+3)^2,

whereas Q(1,b)=4. This makes the negative hazard-dependent correction in (3) possible.

The unchanged envelope identity is

    U''=(2lambda/A)[(w_ab-w_b/A)^2/w_aa-w_bb].           (5)

At the maximum M=1/lambda. Positivity of (4)'s numerator and M_up>=M imply

    U_lambda''(t)>=7/[10(1+t)^3].                      (6)

For the optimized first atom, (3) gives Schur(w)<=4k^2-14(1-2b)k^3. This polynomial is increasing in k on 0<=k<=1/8, since its derivative is 2k[4-21(1-2b)k]>=2k*(11/8)>=0. Substitution of k<=v(s)/(2lambda) yields

    2lambda Schur(w)<=B_lambda(s,b)
      =2v^2/lambda-(7/2)(1-2b)v^3/lambda^2.             (7)

The negative correction must be retained when substituting k: monotonicity just proved licenses substitution into the whole polynomial. Replacing k separately in a negative term would not be valid.

## 3. Coupled curvature and all-policy certificate

The bound in (7) decreases with lambda>=4: its derivative is

    v^2[-2lambda+7(1-2b)v]/lambda^3 <0.

For R(b)=B_lambda(s,b)(1+s-b)^3,

    R'(b)=v^2(1+s-b)^2/lambda^2
             *[v(35/2+7s-28b)-6lambda] <0,            (8)

because v<=1,s<=1/2,b>=0 and lambda>=4 make the bracket at most21-24. Hence its maximum occurs at b=0. There

    R(0)=(2/lambda)*(1+s)^3/(1+5s/8)^2
                *[1-7/(4lambda(1+5s/8))].

Both positive factors depending on s increase: the logarithmic derivative of the first is (7/4+5s/8)/[(1+s)(1+5s/8)]>0, and the square bracket increases directly. Thus the maximum is s=1/2,lambda4, where v=16/21 and

    R<=32/49<7/10,
    (7/10-32/49)*8/27=92/6615=:kappa.                 (9)

Consequently m_s''(b)=2lambda Schur(w)-U''(s-b)<=-kappa. A second exact check certifies the coupled rational difference 7/[10(1+s-b)^3]-B_4(s,b) on b=XY/2,s=Y/2, with degree(4,4) and all25 numerator coefficients strictly positive after normalizing the denominator sign.

The continuous endpoint values are m_s(0)=m_s(s)=0. Therefore concavity of m_s(b)-kappa*b(s-b)/2 implies

    E_s(a,b)>=kappa*b(s-b)/2>=0.                       (10)

This is the original all-control Bellman supersolution. K2483/K2485's inherited transfer proves p-lambda C<=U_lambda(S) for every admitted adaptive policy. The one-stage maximizer attains it. No positive-definiteness of the full Hessian was assumed; only w_aa>0 and its Schur complement were used.

For a finite completed schedule, multiply (10) by its actual prefix survival P_i and telescope, with s_i=sum_(j>=i)b_j:

    U(S)-p+lambda C >=(kappa/2)sum_i P_i b_i(s_i-b_i)
      >=kappa*p*[S^2-sum_i b_i^2]/4.                  (11)

Thus every finite schedule with two positive-score stages has strict gap; a gap<=gamma forces S-max_i b_i<=4gamma/(kappa*p*S). Initial mixtures inherit average gaps. Unique adaptive implementation and global optimality beyond this regime are not claimed.

## 4. Exact constrained frontier through K=1/200

Let a_lambda(S) be the root M=1/lambda. The original one-stage cost 2w(a,S)/(1+a) decreases strictly with a. Thus for 0<K<=K_*(S)=2w(a_4(S),S)/(1+a_4(S)), the unique a satisfying that cost equal to K has the all-policy optimum F_S(K)=1/(1+a); at K=0 it is1/(1+S). K_* is sufficient, not the true transition.

For S=1/2 write a=1/2-d,A=3/2-d,x=d^2/[2(1-d^2)]. Then

    C(d)=2log(1+x)/A,
    M(d)=4Ad/[(1-d^2)(2-d^2)]+2log(1+x).

Take d0=21/250. The rational bounds x/(1+x)<=log(1+x)<=x give

    2x/[A(1+x)]-1/200=1019/1469796200>0,
    1/4-[4Ad0/((1-d0^2)(2-d0^2))+2x]
      =76284905/30920027924>0.                        (12)

Hence C(d0)>1/200 and lambda(d0)>4. Monotonicity places all K<=1/200 inside the certified region, expanding K2511's guaranteed budget range by315/200=63/40. No numerical maximization or decimal inversion establishes this claim.

## 5. Limitation and next substantive construction

The stronger template is still a sufficient certificate. Its defect estimate (3) cannot simply be extended to the multiplier3 ratio domain: at r=5/9,b=0,

    2k=16/49<1/3,
    4-14k-Q=-19/189<0.                                (13)

The exact limiting one-stage root for lambda3 solves -g'(r)=1/3 and is less than5/9, so this point lies in that larger allowed ratio rectangle. This is a failure of the proposed polynomial bound, not a negative Bellman residual, a competing schedule or a true transition. The old constant-scaled K2511 template at lambda4 is also impossible for its own estimates: its curvature corner49/75 is below required675/676.

K2503's exact suffix instability and K2507's optimized atom-tail constructions remain the closest competing original-law branches. The next substantive question is an actual-U Bellman residual or a multiple-atom/optimized-tail policy near that boundary, with exact original prefix weights. Refining rational endpoints within K<=1/200 is already covered by the inverse and is not a new frontier result. No claim here excludes remote finite competitors or mixtures outside the supported regime.

## Verification and limitations

The exact probe reconstructs rational derivatives from the original logarithmic law, certifies whole-domain numerator and denominator signs, and checks calculus, original prefix-weight telescoping and rational budget consequences. Genuine contrary controls reject corrupted polynomials, finite endpoint sampling, strict free-boundary Schur claims, unweighted costs and invalid template extensions. Finite counts describe evidence coverage, not universal theorem counts. Independent internal review examines the proofs and actual probes; no external or proof-assistant certification is claimed.

[Exact probe](../../tests/channel-swings/k2513_exact_schur_stopping_probe.py), [saved report](../../lab/process/k2513-exact-schur-stopping.json), [K2511 predecessor](k2511-coupled-stopping-certificate-2026-11-02.md), [K2503 suffix instability](k2503-stopping-instability-boundary-2026-11-02.md), [K2507 optimal hybrid tail](k2507-stopping-optimal-hybrid-tail-2026-11-02.md).
