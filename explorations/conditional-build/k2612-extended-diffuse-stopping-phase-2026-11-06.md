---
title: "K2612 A larger certified diffuse stopping phase"
status: active_research
doc_type: exploration
created: "2026-11-06"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: supplied stopping law and sufficient phase boundary; no sharp boundary or transfer of higher resource correctors
scripts:
  - tests/channel-swings/k2612_extended_diffuse_stopping_phase_probe.py
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
result: K2612
carrier: original adaptive randomized fair stopping policies, original leakage and finite hit event LAYER=toy CHIRALITY=N/A
pairing: unconditional success minus original failure-inclusive leakage ON=declared_carrier
real_structure: real positive score and multiplier with exact rational and interval certificates
grading: continuum supremum, finite policy, expected trials and leakage budget remain distinct
action_owner: repository-construction -- supplied fair stopping law
target: sufficient diffuse phase and exact constrained-budget consumer MAP-TYPE=evaluation
```

# Enlarge the phase by checking the actual output root

## Result

Put v0=16119/17381 and let H_s be the flow y'=q(y), where

    q(v)=2sqrt(1+2v)-2-v for v0<=v<=3/2,
         1/2 for v>=3/2.

For every 0<S<=1/2 and 0<lambda<=lambda0(S)=1/H_S(v0), the original adaptive stopping supremum is

    V_lambda(S)=lambda H_S^(-1)(1/lambda).

This strictly enlarges K2561's uniform lambda<=4/5 region. At S=1/2 the new sufficient multiplier endpoint is approximately0.8604375545379493. Its corresponding constrained leakage-budget endpoint is approximately0.1566899850577046 with success approximately0.9327848347161163. The probe supplies rigorous rational brackets for these illustrations. This is NOT the sharp phase boundary.

All-policy nonattainment, finite approximation and inverse-error complexity continue to hold. We also derive the enlarged exact constrained segment and an explicit inverse-budget interpretation. No K2602--K2608 second/third resource correction or uniform constant is extended automatically. This remains independent mathematics of the supplied fair law, not physical probability or native GU; SC-META-53, ledger0.263 LT-SM8/LT-GR6b and canon remain unchanged.

## 1. A new root barrier using the existing certified rectangle

Reuse K2561's original

    w(a,b)=log(1+(b-a)^2/[2(a+b)(2-a-b)]),
    F_b(u)=min_(0<=a<=b) [(1+a)u+2w(a,b)],
    M(a,b)=-2(1+a)w_a+2w,
    G_b(v)=partial_b F_b(F_b^(-1)(v)).

Its exact Bernstein certificate proves partial_b G_b(v)>=gamma=78360951/2744000000 whenever the interior OUTPUT root M(a,b)=v lies in 0<=a/b<=2/5,0<=b<=1/2. The same boundary branch a=0 has derivative at least3/8>gamma. The certificate concerns output roots, not input u.

At a=2b/5, use log(1+x)<x for x>0 to obtain M(2b/5,b)<U(b), with

    U(b)=1-2(3421b²-6095b+2350)/[7(7b-10)(89b-140)],
    U'(b)=30(173339b²-443380b+275900)
                   /[7(7b-10)²(89b-140)²].

The derivative numerator on b=y/2 has degree-two Bernstein coefficients

    275900, 165055, 390179/4,

all strictly positive. Denominators are nonzero throughout the interval. Hence U is increasing and U(b)<=U(1/2)=v0. Since M_a=-2(1+a)w_aa<0, every interior output root with v>=v0 has a/b<2/5. At b=0 the limiting minimizer r(v)=2/sqrt(1+2v)-1 is also less than2/5 at v0; above3/2 the optimizer clips to zero.

The unchanged certificate thus gives

    G_b(v)>=q(v)+gamma b, v>=v0.

The a=0 crossing is continuous and occurs at most once as in K2561; the widened v interval does not change the boundary-threshold monotonicity. This is a whole-domain proof. A numerical grid is neither used nor needed. q is positive and nondecreasing on this domain.

## 2. Use the exact trajectory condition

Scalar comparison yields

    F_b(u)>=H_b(u)+gamma b²/2, u>=v0.

Set theta=1/lambda and u(s)=H_s^(-1)(theta). The exact condition theta>=H_S(v0) is equivalent to u(S)>=v0, so all0<=s<=S remain inside the certified domain. The semigroup identity H_b(u(s))=u(s-b) proves

    (1+a)V(s)+2lambda w(a,b)-V(s-b)>=lambda gamma b²/2.

K2561's monotone clipping handles overshoots and a>b using the original cost law and nonnegative extra residual terms; its finite-horizon original conditional-expectation telescope gives V(S)>=p-lambda C for every original adaptive randomized policy. Abort and nonabsorption contribute nonnegative terminal terms; approaching zero score without a finite hit is not an attained success.

For n finite equal-score steps, choose the exact F_(S/n) minimizing actions in forward affine composition. Uniform first-order expansion on this fixed compact trajectory and discrete Gronwall give O(1/n) error, with original survival weights retained. Alternatively take a_i=(S/n)r(H_((i-1)S/n)(u(S))); the same uniform local expansion supplies a feasible matching sequence. Thus the upper bound is sharp. This proof uses the previous generator certificate on a newly verified domain, not a new assumption that every fluid candidate is optimal.

Since q(v)<1/2 below3/2 and v0<1, H_(1/2)(v0)<v0+1/4<5/4. Therefore lambda0(S)>=lambda0(1/2)>4/5 for every allowed S. The old theorem is retained as a subset.

## 3. Enlarged exact constrained segment

For theta between theta0(S)=H_S(v0) and theta_sat=(3+S)/2 put

    u=H_S^(-1)(theta), p=q(u)/q(theta), B=theta p-u.

Then dp/dtheta=p[q'(u)-q'(theta)]/q(theta)>0, and dB/dtheta=theta dp/dtheta>0 below saturation. Thus dp/dB=1/theta and d²p/dB²=-1/[theta³ dp/dtheta]<0. At theta_sat, p=1 and B=S/2. At the new lower endpoint,

    B0(S)=H_S(v0) q(v0)/q(H_S(v0))-v0 >0.

Positivity follows also from the finite-policy limiting integral of the positive leakage density along a positive-length path. Hence the exact supremal success is p(theta) throughout B in[B0(S),S/2], strictly concave below saturation. If a finite approximant has cost C_n>B, mix it with free abort with probability B/C_n; otherwise keep it. This enforces the exact original budget and preserves convergence. No relaxed-budget limit is used.

For any success target p_target in[p0(S),1), there is a unique theta in[theta0,theta_sat) with p(theta)=p_target. The infimum feasible leakage budget is B(theta), and it is not attained at that success target. To see that the infimum can still be approached with success at least p_target, use contacts with success strictly above p_target and budgets decreasing to B(theta); their finite approximants eventually exceed p_target. The supporting dual bound excludes any smaller budget. This is an inverse-budget consequence, not an assertion that the limit policy is admissible. At p_target=1 the existing infimum S/2 is likewise not attained.

## 4. Nonattainment and adaptive complexity survive

A policy with positive hit probability has a reached positive clipped-score trial with positive probability. The strict Bellman slack excludes equality in the dual bound; zero-hit policies have value<=0<V. Thus no original policy attains V or any constrained contact in the new interval.

For deterministic completed n-stage schedules,

    V-(p-lambda C)>=lambda gamma exp(-S) S²/(2n).

For arbitrary original adaptive policies let N+ count reached positive-score trials, including failures. Predictability and the fresh fair use/test rule give E sum b'=2E sum_use b'>=2S p. Cauchy--Schwarz on the occupation measure and the per-trial slack imply

    eta=V-p+lambda C >=lambda gamma S² p²/E N+.

At a constrained contact C<=B, eta<=p_star-p. Therefore expected positive trials diverge at least inversely with success error. The finite approximants and budget repair have O(1/error) expected positive trials, giving the sharp order at every fixed new contact. No assertion about pathwise total-cost caps, hidden idles or a uniform S->0 constant is made.

## 5. Certified consumers and rejected extrapolations

The exact clock is tau(v)=log(sqrt(1+2v)-1)-3log(3-sqrt(1+2v)) below3/2, and2v-3 above. It has tau'=1/q and matched values at3/2. The probe brackets theta0 at S=1/2 and1/4 using rational endpoints whose clock residuals have certified opposite signs, then propagates interval arithmetic into lambda0,p0,B0. It executes rational finite schedules at lambda=17/20,S=1/2 inside the newly certified region, retaining actual success, leakage and expected trials. These finite consumers illustrate convergence; the universal bound comes from sections1--2.

K2561's rational hybrid at lambda19/10 and its exact intermediate-output generator failure remain valid. They show why this sufficient extension cannot be extrapolated to all positive multipliers. Later corrector theorems remain on their stated domains pending separate bounds. The new lower endpoint v0 is a convenient rational barrier from log(1+x)<x, not the maximally possible output floor. A further sharper barrier or direct Bellman comparison may enlarge the phase, but needs its own proof.

Next compare an actual sharper fluid/atomic junction with positive-action count rounding or the fourth-order terminal tie. The full intermediate phase diagram remains open; the old4/5 frontier is no longer the best available sufficient phase.

[K2561](k2561-higher-budget-stopping-2026-11-05.md), [K2559](k2559-parametric-stopping-concavity-2026-11-05.md), [K2557](k2557-parametric-stopping-support-2026-11-05.md), [probe](../../tests/channel-swings/k2612_extended_diffuse_stopping_phase_probe.py), [report](../../lab/process/k2612-extended-diffuse-stopping-phase.json).
