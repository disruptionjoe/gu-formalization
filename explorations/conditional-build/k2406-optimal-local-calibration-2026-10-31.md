---
title: "K2406 Optimal local calibration and a temporal information floor"
status: active_research
doc_type: exploration
created: "2026-10-31"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional statistical mathematics; no measured stability or native GU verdict
scripts:
  - tests/channel-swings/k2406_optimal_local_calibration_probe.py
---

# K2406 Optimal local calibration and a temporal information floor

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
result: K2406
carrier: adaptively observed binary environment labels and matched residual pools LAYER=toy CHIRALITY=N/A
pairing: declared conditional probability or positive Hilbert channel pairing ON=declared_carrier
real_structure: real probabilities and exact rational or algebraic coefficients
grading: observed records, hidden roles and conditional parameters
action_owner: repository-construction -- K2400 conditional calibration and K2397 matching model
target: optimal drift-aware linear smoothing, exact rectangular pool bounds and temporal information limit MAP-TYPE=evaluation
```

## Result and scope

[K2403](k2403-drift-robust-calibration-2026-10-31.md) permits a supplied drift envelope and heterogeneous fresh pools. Here a known temporal Lipschitz bound yields an exactly optimal nonnegative linear smoother **for the stated Hoeffding confidence-radius objective**, sharper individual-member pooling bounds, and a lower bound showing why unlimited old data cannot determine the current probability. The optimum is not a claim of minimax statistical estimation. No observations, measured drift, common-residual matching, native GU bridge or hardware costs are supplied.

## 1. Local confidence and its exact optimizer

At deterministic sample times s_i<t, X_i in[0,1] has predictable conditional mean p_i. Let p_t be the current predeployment conditional mean and assume pathwise |p_i-p_t|<=L(t-s_i), with supplied L>=0. Index i follows reveal order, with all previously revealed science in the filtration. Ages a_i=t-s_i and weights w_i>=0, sum w_i=1, are deterministic. Martingale Hoeffding gives

    P(|sum_i w_i(X_i-p_i)| > c ||w||_2) <= 2 exp(-2c²).

The lemma and filtration proof are in K2403; apply its conditional MGF to lambda*w_i and optimize lambda. Thus with c=sqrt(log(2/epsilon)/2), the clipped interval centered at sum w_i X_i with radius

    R(w)=L sum_i a_i w_i+c ||w||_2                         (1)

covers p_t with probability at least1-epsilon. Random p_t is allowed because the drift bound is pathwise; this is not conditional coverage given the realized data.

For L>0 there is a unique h>min_i a_i solving

    L² sum_i (h-a_i)_+²=c².                               (2)

The left side is continuous and strictly increasing above the minimum. Put d_i=(h-a_i)_+ and D=sum d_i. Then

    w_i*=d_i/D,                 min_w R(w)=Lh.             (3)

Indeed c||w||_2=L||d||_2||w||_2>=L d·w. Hence R(w)>=L sum(a_i+d_i)w_i>=Lh. Equality holds for w=d/D, since its support has a_i<h. This also proves uniqueness: equality in Cauchy requires proportional weights. At L=0, uniform weights minimize the norm and give c/sqrt(n). The active-set breakpoints in(2) yield a quadratic equation, so no numerical optimizer is needed. Clipping to[0,1] may saturate; (3) optimizes the un-clipped certified radius, not all possible confidence procedures.

A predeclared finite or countable bank of deployment times, streams or deterministic weights may allocate epsilon_j with sum epsilon_j<=delta. Simultaneous coverage permits choosing an interval from that bank after observing the data, or intersecting intervals for the SAME target. Intervals for different times require their own drift enlargement. A new hindsight-fitted weight vector is not in the bank merely because it looks favorable. For two independent fair labels, selecting a success whenever one exists makes the selected label's mean3/4 instead of1/2. Likewise optional stream sampling alone does not justify retrospective weighting.

An exact favorable fixture has256 observations at each age1,2,3,4, L=1/32 and c=2. Since exp(8)>400, its failure bound is below1/200. Equation(2) has all four ages active and h=(5+sqrt(11))/2. Its radius is(5+sqrt(11))/64<9/64, the uniform1024-sample radius. Rational batch masses(1/2,1/3,1/6,0) have drift5/96 and noise sqrt(14)/48<5/64, giving radius<25/192. On a half-success-per-batch path this gives[71/192,121/192]. These are1024 actual innovations, not1024 copies of a single label; the favorable path is not a power guarantee. Future use after t requires the additional bound |p_future-p_t|<=L times the delay, and enlarges the interval by that amount.

## 2. Individual intervals improve the actual pooled factor

Retain K2403's complete experiment: one science member q, m independent fresh calibration members p_i, common conditional residual law within each environment, uniform hidden-role randomization and permutation-equivariant scores. For interior parameters and1<=t<=m ones in the pool,

    r=odds(q) (m-t+1)/t e_(t-1)(o)/e_t(o), o_i=odds(p_i). (4)

This r is decreasing in every p_i and increasing in q. To prove the first statement, separate a selected o_i=x. Write e_t/e_(t-1)=(a+xb)/(b+xc), where a=e_t(other), b=e_(t-1)(other), c=e_(t-2)(other), with e_-1=0 and e_0=1. Its derivative is(b²-ac)/(b+xc)²>=0. Elementary symmetric coefficients are log-concave: starting at1, adjoining a factor(1+xz) preserves it because for B_k=A_k+xA_(k-1),

    B_k²-B_(k-1)B_(k+1)
      = A_k²-A_(k-1)A_(k+1)
        +x[A_k A_(k-1)-A_(k-2)A_(k+1)]
        +x²[A_(k-1)²-A_(k-2)A_k] >=0.

The middle term is nonnegative by nonincreasing adjacent ratios on the positive support; endpoint zeros follow by limits. This supplies an elementary proof without assuming independence of polynomial coefficients.

Covered individual intervals p_i∈[l_i,u_i], q∈[l_q,u_q] therefore give

    r in [r(u_vector,l_q), r(l_vector,u_q)].               (5)

These are exact extremes of the RECTANGLE. Shared drift constraints can make its corners jointly infeasible; (5) remains safe but is then not necessarily sharp. Freeze these intervals before pool revelation. Identity/timestamps that reveal the science role may not enter scores. Degenerate boundaries use monotone limits; homogeneous all-zero/all-one pools use the inherited equal-within-group convention.

For p1∈[1/4,1/2], p2∈[1/2,3/4], q=1/2, (5) gives[1/2,3/2] at t=1 and[2/3,2] at t=2. The common-envelope bound would be[1/3,3]. With labels(1,0,0) and bonus scores(1,0,0), the robust normalizer is3/7 rather than3/5, so at unit bet the maximum realized factor is7/3 rather than5/3. This is a precise improvement in the same conditional experiment, not an empirical discovery. For arbitrary scores the fractional-linear normalizer still attains its maximum at one interval endpoint. K2403's stopped-shadow proof transfers unchanged: simultaneous calibration error delta and crossing error eta give delta+eta; a probabilistic drift premise adds its own failure allowance.

## 3. A temporal information floor despite unlimited old data

Consider independent Bernoulli histories, one innovation at each integer age r>=1. For0<a<1/2 and L>0 define

    p^±_(t-r)=1/2 ± (a-Lr)_+,       p^±_t=1/2±a.          (6)

Each path is L-Lipschitz. Histories at ages r>=a/L are identical, so collecting more of that old history cannot distinguish the models. With f_r=(a-Lr)_+, the exact one-label chi-square divergence is16f_r²/(1-4f_r²). Independence gives

    1+chi²(P+ || P-)=product_r [1+16f_r²/(1-4f_r²)].       (7)

The likelihood-ratio identity proves the product formula. Cauchy on total variation gives TV<=sqrt(chi²)/2. If an interval I covers the respective current parameter under EACH model with probability>=1-epsilon, then under P+ it contains both with probability>=1-2epsilon-TV: transfer P- coverage of p^-_t to P+ and intersect with P+ coverage of p^+_t. Its width is then at least2a. This argument also covers randomized intervals with common independent randomness.

For a=1/9,L=1/72, only seven historical labels differ and

    1+chi²=4292603444493/2815640580500 < 2.

Thus TV<1/2. At epsilon=1/20, every uniformly95%-covering interval has width>=2/9 with probability>2/5 under P+, irrespective of how many older labels are observed. This is an information-theoretic lower bound under a KNOWN drift constant, stronger than ignorance about an anchor. It does not prove (1) minimax-optimal or preclude gains from a stronger dynamical model, additional recent innovations, or direct deployment measurement.

## Verification and next condition

The native probe checks exact taper algebra and objective comparisons, polynomial log-concavity identities, finite coordinatewise monotonicity cases and independently enumerated Bernoulli count likelihoods, the actual score normalizer, exact recent-history likelihood product, and changed-assumption controls. Universal martingale, optimizer and lower-bound conclusions use the written proofs; finite pass counts are not independent proofs. The [report](../../lab/process/k2406-optimal-local-calibration.json) pins dependencies. Independent statistical review examined the proof, corrected active-set example, actual probe and generated report before conditional acceptance. Deployment needs a justified drift/matching model, covered times and actual acquisition costs. Unknown drift or outcome-selected new weights remain separate problems.
