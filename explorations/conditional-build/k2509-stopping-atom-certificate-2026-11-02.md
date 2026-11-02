---
title: "K2509 A global one-stage stopping certificate at budget one thousandth"
status: active_research
doc_type: exploration
created: "2026-11-02"
classification: CONVENTIONAL_COMPARATOR
target_claim: "NONE-NOT-A-KILL"
claim_ceiling: "conditional supplied-model mathematics; no native GU realization, experimental certification or unrestricted-budget frontier"
---

# K2509 A global one-stage stopping certificate at budget one thousandth

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
result: K2509
carrier: original fresh fair test/use stopping law at 0<S<=1/2; numerical consumer S=1/2 LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert trace or original failure-inclusive probability cost ON=declared_carrier
real_structure: complex adjoint for effects; real probabilities for stopping
grading: original verifier sectors or finite stopping stages
action_owner: repository-construction -- supplied instruments and original probability law
target: global Bellman support, quantitative atom exclusion and exact small-budget frontier MAP-TYPE=evaluation
```

## Result and scope

For the original fresh fair test/use stopping law, every score 0<S<=1/2 and every Lagrange multiplier lambda>=35/4 has an exactly optimal one-stage policy, against all adaptive policies and initial mixtures. A quantitative Bellman inequality strictly excludes every finite schedule with two positive-score stages from the same supporting line. The proof covers all stage sizes, including arbitrarily small satellites.

At S=1/2 and K=1/1000 this closes the previously open frontier:

    F_(1/2)(1/1000)=1/(3/2-d_*),
    2/(3/2-d_*) log(1+d_*^2/[2(1-d_*^2)])=1/1000,
    0<d_*<77/2000.                                         (1)

The unique root gives

    684093908424485444843251472880883/10^33
      < F_(1/2)(1/1000)
      < 684093908424485444843251472880884/10^33.             (2)

The rational endpoints are supported by certified interval logarithms, not floating-point optimization. The theorem is the global inequality below; a narrow numerical bracket alone would not establish optimality.

This is supplied-model, GU-independent probability mathematics. SC-META-53 remains UNCERTAIN; LT-SM8/LT-GR6b and native matter/light/domain obligations remain open. Ledger0.263, source polarities, canon and physical credit are unchanged. No novelty, external-expert or proof-assistant certification is claimed. K2493/K2503/K2507's larger-budget multistage improvements survive: 35/4 is a sufficient multiplier threshold, not the global transition.

## 1. Original law and the one-stage candidate

Reuse K2483/K2485's all-policy least-supersolution and schedule-mixture reductions, with the original failure-inclusive cost. For 0<=a<=b<=s<=1/2,

    w(a,b)=log(1+(b-a)^2/[2(a+b)(2-a-b)]), w(0,0)=0.

A completed finite schedule has sum b_i=S,

    P_i=product_(j<=i)(1+a_j)^(-1), p=P_n,
    C=2 sum_i P_i w(a_i,b_i).                              (3)

This expectation includes failed paths. Stages a>=b are free and may be clipped to a=b; score overshoot may be clipped under the inherited original-law dominance. The cited reduction includes arbitrary adaptive policies, mixtures, abandonment and limiting schedules without an artificial minimum stage size.

For lambda>=35/4, define

    U_lambda(s)=max_(0<=a<=s) [1-2lambda w(a,s)]/(1+a),
    U_lambda(0)=1.                                        (4)

This initially describes only one stage. We now prove it is the full unconstrained Lagrange value. It is between 1/(1+s) and1. Put A=1+a, x=(b-a)^2/[2(a+b)(2-a-b)], and

    M(a,b)=-2A w_a(a,b)+2w(a,b).

### Strict convexity in a and unique maximizing root
Let u=a+b,d=b-a,D=2u(2-u),N=D+d^2. Holding b fixed and differentiating in deficiency d gives D_d=4(u-1), N_d=2a+6b-4. On the stated cone,

    D_d<=N_d<=0, D<=N,
    w_aa=4/D-2/N+D_d^2/D^2-N_d^2/N^2 >=2/D>0.             (5)

Thus M_a=-2A w_aa<0. At a=b, M=0. At a=0, M>=-2w_a>=1, using the elementary derivative bound in section3. The derivative in a of (4)'s objective is (lambda M-1)/A^2. Hence for every s>0 there is a unique interior maximizer a_lambda(s), determined by

    M(a_lambda(s),s)=1/lambda.                             (6)

Let delta=(b-a)/(a+b). The same derivative bound gives M>=delta, so at this root

    a/b >= (lambda-1)/(lambda+1) >=31/39.                  (7)

There is no division by zero at s=0: the cone extension follows by limits. More precisely M(rb,b) extends analytically to b=0, where it is -g'(r), g(r)=(1-r)^2/[2(1+r)], and its r derivative is -g''(r)<0. The implicit function theorem gives a smooth ratio and U through s=0 for each finite lambda in this range.

## 2. Exact uniform curvature certificate for U

Differentiating (6) and using the envelope theorem yields

    U'=-2lambda w_b/A,
    a'=-w_ab/w_aa+w_b/(A w_aa),
    U''=(2lambda/A)[(w_ab-w_b/A)^2/w_aa-w_bb].             (8)

All derivatives here are of the original w; no transformed cost is substituted. Since log(1+x)<=x, define M_up=-2A w_a+2x>=M. The rational function

    F(a,b)=2[(w_ab-w_b/A)^2-w_bb w_aa]
              /[A M_up w_aa]                             (9)

satisfies F>=47/100 throughout a=rb,31/39<=r<=1,0<=b<=1/2 after exact cancellation of removable factors. Positivity also proves its numerator is positive; therefore at (6), where 2lambda=2/M, equation (8) implies

    U_lambda''(s)>=F(a_lambda(s),s)>=47/100.                (10)

This is a full-rectangle polynomial certificate. Substitute r=31/39+(8/39)X,b=Y/2. The exact numerator of F-47/100 has bidegree(11,8). All108 tensor Bernstein coefficients on [0,1]^2 are positive; the minimum is

    260694488634812372/904489565021289.

Its denominator factors consist of a positive factor100, (br+1)^3 and two polynomials of degrees(3,2) and(5,3). Their tensor Bernstein coefficient minima are respectively1,687364/59319 and8. The report records every coefficient; the probe re-derives F from N,D, performs symbolic cancellation and replays coefficient positivity. Bernstein basis functions are nonnegative and sum to1, so this proves the rational inequality everywhere, including the canceled continuous boundary values. A coefficient sign check is used only after exact conversion; sampled values are not the certificate.

## 3. Bound the optimized single-stage curvature from above

Fix total remaining score s and minimize the Bellman residual over its first atom:

    E_s(a,b)=(1+a)U_lambda(s)+2lambda w(a,b)-U_lambda(s-b),
    m_s(b)=min_(0<=a<=b) E_s(a,b).                         (11)

For b>0, E_aa=2lambda w_aa>0. Its a derivative is positive at a=b and negative at a=0, since U<=1 and -w_a(0,b)>=1/2. Therefore the minimizer is unique and interior, with

    k=-w_a=U_lambda(s)/(2lambda)<=1/(2lambda).             (12)

Here is an explicit rational upper bound on its Schur complement. Put u=a+b,delta=(b-a)/u, M0=4-2u,L=M0+delta^2 u. Then w=log(L/M0). Direct differentiation at fixed b gives

    k=(2delta/L)[1+delta(1-u)/(2-u)] >=2delta/L>=delta/2,
    delta<=1/lambda.                                     (13)

At fixed delta, f(u)=log(L/M0) has

    f_uu=4delta^2[2L+(2-delta^2)M0]/(M0^2 L^2)
         <=16delta^2/(M0^2 L).

The radial Hessian direction (r,1), r=a/b, therefore obeys

    (r,1) Hess(w) (r,1)^T
       =(1+r)^2 f_uu
       <=64delta^2/(M0^2 L)
       <=16k^2 L/M0^2
       <=8k^2(1+delta^2/2)
       <=2/lambda^2 [1+1/(2lambda^2)].                    (14)

We used u<=1, M0>=2 and L/M0<=1+delta^2/2. Since w_aa>0, minimizing that quadratic over its first component gives

    w_bb-w_ab^2/w_aa <= (r,1) Hess(w) (r,1)^T.

No positive-definiteness of the full Hessian is assumed. Combining (10),(12)--(14),

    m_s''(b)=2lambda(w_bb-w_ab^2/w_aa)-U''(s-b)
       <=19728/42875-47/100 = -kappa,
    kappa=1693/171500>0.                                 (15)

The minus sign before U'' is essential. The first constant bounds
(4/lambda)[1+1/(2lambda^2)] at lambda=35/4 and decreases thereafter.

## 4. Global Bellman support and quantitative multi-atom exclusion

By continuous cone extension m_s(0)=0. Equation (4) gives m_s(s)=0: (1+a)U(s)+2lambda w(a,s)>=1 with equality at its one-stage maximizer. Subtract kappa b(s-b)/2 from m_s. Equation (15) makes the difference concave with zero endpoints. Hence every original control satisfies

    E_s(a,b)>=m_s(b)>=kappa b(s-b)/2>=0.                   (16)

In particular U satisfies the all-control Bellman supersolution, and the inherited least-supersolution theorem gives

    p-lambda C<=U_lambda(S)                               (17)

for every admissible adaptive policy, including initial mixtures and abandonment. The one-stage root (6) attains equality. This proves global Lagrange optimality; it does not assume that an arbitrary adaptive policy is one deterministic schedule.

For a finite completed schedule, multiply (11) by P_i and telescope using (1+a_i)P_i=P_(i-1). With s_i=sum_(j>=i)b_j,

    U(S)-p+lambda C=sum_i P_i E_(s_i)(a_i,b_i)
       >=(kappa/2)sum_i P_i b_i(s_i-b_i)
       >=kappa p [S^2-sum_i b_i^2]/4.                    (18)

Every schedule with two positive-score stages has strictly positive gap. If its supporting-line gap is at most gamma, then

    S-max_i b_i <=4gamma/(kappa p S).                     (19)

This quantitative score concentration is global and independent of stage count. Initial mixtures obey the average gap inequality. Neither (18) nor (19) asserts unique implementation among all adaptive policies; equivalent repeated-trial implementations and limiting representations need separate typing.

## 5. Exact constrained frontier and the one-thousandth consumer

For fixed S, the one-stage cost C_S(a)=2w(a,S)/(1+a) is strictly decreasing on0<=a<S because w_a<0 and w>0. Along (6), lambda increasing makes a increase to S, and the cost decreases continuously to0. Let K0(S)=C_S(a_(35/4)(S)). For every0<K<=K0(S), there is a unique such one-stage a with cost K. The supporting line (17) then gives F_S(K)<=U_lambda(S)+lambda K=1/(1+a), with equality from the actual one-stage policy. At K=0 the free one-stage baseline is1/(1+S). No statement that K0 is the transition is made.

For S=1/2 write a=1/2-d and A=3/2-d. Then

    x=d^2/[2(1-d^2)],
    C(d)=2log(1+x)/A,
    M(d)=4A d/[(1-d^2)(2-d^2)]+2log(1+x).

Take d0=77/2000. Using x/(1+x)<=log(1+x)<=x, exact rational arithmetic proves

    2x/[A(1+x)]-1/1000=349330467/23366669533000>0,
    4/35-[4A d0/((1-d0^2)(2-d0^2))+2x]
       =5632989533/372503683452145>0.                     (20)

Thus C(d0)>1/1000 and M(d0)<4/35, so lambda(d0)>35/4. The unique root d_* of C(d)=1/1000 is smaller, with still larger multiplier. This proves (1) is inside the global certificate's range using only rational inequalities, without a numerical estimate of the threshold.

For the displayed value (2), the probe uses192-bit Arb logarithms to verify opposite strict cost signs at the rational endpoints

    d_lo=48439958028934968344008499723887/
          1267650600228229401496703205376000,
    d_hi=3027497376808435521500531232743/
          79228162514264337593543950336000.

C is strictly increasing, so these enclose the unique root. Exact rational propagation through1/(3/2-d) gives (2). This replaces K2491's broader certified interval at this one budget, while preserving its general-purpose certificate as valid historical evidence. No new digit or mesh search is needed to prove optimality.

## Verification, contrary controls and remaining frontier

The certificate is finite exact polynomial arithmetic supporting a universal written Bellman proof. The probe recomputes the rational derivatives and all positive numerator/denominator coefficients. It also independently checks original survival-weighted telescoping, exact witness signs, certified root endpoints, and inequalities behind the Schur estimate. These are distinct evidence kinds, not independent theorem counts.

Contrary controls include an overstated curvature constant that fails at a real corner, an altered survival weight that breaks telescoping, original finite multistage gains outside this certified regime retained by K2507, and a false inference from endpoint positivity to a polynomial's interior sign. Boundary controls retain b=0,b=s,r=1 and the full closed rectangle. Independent internal specialists reviewed the proof; no theorem-prover or external expert certification is claimed.

A further attempt to extend this same decoupled-curvature proof to lambda=8 fails an exact corner test: at r=7/9,b=1/2 the rational lower surrogate F is below1/2, whereas the Schur upper constant is129/256>1/2. Thus no uniform constant between these two bounds can close that rectangle. This rejects the present proof template at8, not one-stage optimality there; a sharper coupled estimate could change the conclusion. It prevents treating more Bernstein subdivisions as the missing fix.

The unrestricted frontier beyond K0(S), the actual transition, and the globally optimal finite-atom/distributed-tail structure remain open. The sharp coherent-controller and finite-net coverage results are independent work; no native matter/light or physical GU claim changes. The next global task needs an improved certificate or a concrete competing original policy at a larger budget, not another approximation of the now-solved1/1000 endpoint.

[Exact probe](../../tests/channel-swings/k2509_stopping_atom_certificate_probe.py), [saved report](../../lab/process/k2509-stopping-atom-certificate.json), [K2485 all-policy reduction](k2485-constrained-stopping-frontier-2026-11-01.md), [K2491 prior certificate](k2491-analytic-stopping-certificate-2026-11-02.md), [K2507 retained larger-budget competitors](k2507-stopping-optimal-hybrid-tail-2026-11-02.md).
