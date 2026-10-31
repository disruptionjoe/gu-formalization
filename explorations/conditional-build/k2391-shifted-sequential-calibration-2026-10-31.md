---
title: "K2391 Shift-robust calibration and anytime shared-graph evidence"
status: active_research
doc_type: exploration
created: "2026-10-31"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematics; no native GU or measured physical verdict
scripts:
  - tests/channel-swings/k2391_shifted_sequential_calibration_probe.py
---

# K2391 Shift-robust calibration and anytime shared-graph evidence

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
result: K2391
carrier: one frozen stacked observation and disjoint paired-exposure calibration batches LAYER=toy CHIRALITY=N/A
pairing: prespecified real residual score with correlated vector errors ON=declared_carrier
real_structure: conditional symmetric exposure noise; observable covariate shift with supplied weights
grading: training, calibration, science and sequential looks
action_owner: repository-construction -- K2376 conditional windowed observation graph
target: exact weighted-rank and sequential composite-null tests MAP-TYPE=evaluation
```

## Scientific result and scope

[K2388](k2388-exchangeable-noise-calibration-2026-10-31.md) gives an exchangeable-noise rank test. Here a concrete **conditional** repeated-exposure model supplies the matching noise law, permits a specified covariate shift, and accumulates evidence across fresh batches while retaining one shared graph parameter. The endpoint includes exact sensitivity to weight uncertainty and a three-look synthetic power guarantee below the one-look significance-resolution floor.

The underlying observation graph remains the conditional metric f(R) construction after the K2376 window bridge. SC-COS-50/51/54 retain ASSERTS; LT-GR2e remains NEEDS and ledger0.263 is unchanged. A test of this supplied graph is not a native GU prediction or a measured cosmological exclusion. No physical calibration data are supplied.

## Observable shift and weighted-index proof

Conditional on separate training and fixed signal s, freeze Theta and residual score a_theta. Calibration pairs (C_j,xi_j), j=1,...,m, are independent from P(dc)K_c(dxi); the independent science pair (C_*,epsilon) has law Q(dc)K_c(depsilon). Q is absolutely continuous relative to P, with supplied likelihood ratio w(c)=dQ/dP. C is an observed environment variable; the ratio does not require knowing epsilon. Arbitrary coordinate correlation and heavy tails are allowed. We assume all profile events below are measurable.

The null says R_theta* s=0 for one fixed theta* in Theta. Science data are z=s+epsilon. At the true theta the science score a_theta(R_theta z) equals a_theta(R_theta epsilon). Conditional on the unordered pool of N=m+1 pairs, the science index has probability pi_i=w(C_i)/sum w(C_j). This follows by factoring each possible assignment's likelihood into the common product of P laws and its one weight. The denominator is positive almost surely because the science weight is positive Q-almost surely. Zero calibration weights are allowed in this exact theorem; the robust boxes below assume positive lower bounds.

For the pooled scores A_i, including the observed science residual score A_*, set

    p_w(theta) = sum_i w(C_i) 1{A_i(theta)>=A_*(theta)} / sum_i w(C_i).

Order score levels from greatest to smallest, merging ties. Their pi masses form consecutive intervals partitioning [0,1]. A level's conservative p-value is its interval's upper endpoint. The total mass of levels with upper endpoint <=alpha is at most alpha. Therefore p_w(theta*) is superuniform. Rejecting only when sup_theta p_w(theta)<=alpha has size at most alpha. This is a worst-case profile, not a fitted-parameter uniform p-value.

For an independent U uniform on [0,1], replacing the upper tail by strict-tail mass plus U times the tied-level mass makes p_w(theta*) exactly uniform. This removes discrete resolution by deliberate randomization; the deterministic rule remains the default here. A shared U across candidate theta still gives pointwise validity at theta*, but adaptive data-selected scores or weights need their own argument.

This applies the weighted-index idea in [Tibshirani et al., Conformal Prediction Under Covariate Shift](https://www.stat.berkeley.edu/~ryantibs/papers/weightedcp.pdf); it does not claim novelty for weighted exchangeability. The graph, exposure and sequential consumers below are explicitly derived.

## Sharp uncertainty in the supplied weights

Suppose positive bounds l_i<=w(C_i)<=u_i hold for every pooled member. With T={i:A_i>=A_*}, the exact maximum over this independent weight box is

    p_plus(theta)=sum_(i in T) u_i /
        [sum_(i in T) u_i + sum_(i notin T) l_i].                 (1)

Increase each tail weight and decrease each outside weight: each change monotonically increases the ratio. Thus (1) is attained at a corner, dominates the true rank, and is the smallest pointwise upper envelope for this box. Shared normalization or parametric constraints may make it conservative; this is not optimality among all tests. Estimated bounds require an external validity guarantee; observing a finite sample does not establish them.

If only max w_i/min w_i<=Gamma is supplied, r=|T| gives

    p_Gamma(r)=Gamma r/(N-r+Gamma r),
    r <= floor[alpha N/(Gamma(1-alpha)+alpha)]                 (2)

as the rejectable-rank condition. The minimum deterministic p is Gamma/(N-1+Gamma), so one-look rejection requires N>=1+Gamma(1-alpha)/alpha. For r<N the largest tolerated ratio is Gamma_max=alpha(N-r)/[(1-alpha)r]. These bounds are sharp over the stated finite weight-range class. Bounds w_i/estimated_w_i in [1/Gamma,Gamma] allow relative distortions Gamma squared; do not confuse those models.

Ignoring weights is unsafe. Conditional on a distinct-score pool with r high-scoring members weighted Gamma and all other members weighted1, that upper-rank event has probability Gamma r/(N-r+Gamma r), exceeding r/N. With no support overlap, calibration can always observe zero noise and science always nonzero noise; ordinary rank rejection may then occur every time.

For a supplied graph discrepancy h in H_theta, replace the science score by a_theta(R_theta z-h) and take the supremum over (theta,h). The true pair restores the proof. A conservative lower bound on the science score gives an upper p-value; in the Euclidean raw ball this bound is max(0,||R_theta z||-rho)^2. Arbitrary replaced calibration vectors from K2388 are a different threat model: (1) does not automatically inherit its k/N correction.

## A same-window conditional calibration instrument

At an observed environment c, collect independent exposures Y_a=s+eta_a with the SAME frozen signal, windows, selection and a centrally symmetric conditional error law H_c. Use one pair for science and disjoint pairs for calibration:

    z=(Y_1+Y_2)/2=s+(eta_1+eta_2)/2,
    xi_j=(Y_(2j+1)-Y_(2j+2))/2.

Symmetry eta=-eta in law and independence make (eta_1+eta_2)/2 and (eta_3-eta_4)/2 identically distributed. This induces the K_c used above. The science pair's environment is drawn from Q and each calibration pair's environment from P. All exposures within a pair share its environment; different pairs have the stated conditional independence. Unrelated skies or latent-field draws are not repeated exposures of the same s.

A common unknown bias cancels from differences but remains in the science average. It must be removed if known, have zero graph residual, or enter a justified discrepancy set. Zero mean alone does not replace symmetry: eta=-1 with probability2/3 and eta=2 with probability1/3 has zero mean. Every calibration half-difference has magnitude at most3/2, while the science mean equals2 with probability1/9. With at least19 calibration vectors the squared-score rank test rejects at nominal1/20 on that event, so its size is at least1/9. Changing windows, signal-dependent errors, drift or shared pair errors likewise require a new matching-law proof.

## Anytime testing while retaining one unknown graph

For each look t, require the entire fresh batch to satisfy the preceding model **conditional on the full past**. Training, sampling rules and beta_t in (0,1) may be predictable. The same fixed theta* must remain in the prespecified Theta. For each theta define

    e_t(theta)=1{p_t_plus(theta)<=beta_t}/beta_t,
    E_t(theta)=product_(j<=t) e_j(theta), E_0=1.

At theta*, conditional expectation of each factor is at most1. Thus E_t(theta*) is a nonnegative supermartingale. For any finite horizon, stop it at its first crossing of1/alpha; the expectation bound and nonnegativity imply crossing probability<=alpha. Increasing horizons gives the infinite-horizon result. Since inf_theta E_t(theta)<=E_t(theta*),

    Pr(exists t: inf_theta E_t(theta)>=1/alpha)<=alpha.        (3)

The profiled infimum is NOT claimed to be a supermartingale. A certified global lower bound is needed to reject; a grid minimum is an upper bound on the infimum and cannot establish rejection. Keep one parameter across looks: inf_theta product e_t(theta) is at least product inf_theta e_t(theta), and can be strictly larger for positive betting functions. For fixed theta, one zero factor is permanent; rejection by the profiled product therefore requires every theta to pass every preceding binary threshold. Other predictable nonnegative p-to-e calibrators with conditional expectation<=1 can replace the binary bet, but are not implemented here.

Reuse control: repeat one uniform p-value U on every look and set e_t=3*1{U<=1/3}. Three looks cross20 with probability1/3, not1/20. Marginally valid p-values do not supply conditional validity. Fresh independent batches suffice; reuse is permitted only with a separate conditional proof, not by this theorem.

If a supplied conditional total-variation discrepancy delta_t bounds the actual batch law from the ideal law, its threshold probability is at most min(1,beta_t+delta_t). Dividing the indicator by that quantity preserves the supermartingale proof. An unconditional TV bound is insufficient for this conditional step.

## Three fresh looks cross a genuine one-look barrier

Use K2388's R_theta=[[-theta,1,0,0],[0,0,-theta,1]], theta in[-1,1], s=(0,4,0,-4), and centrally symmetric exposure errors (b,0,0,0), |b|<=1, conditional on each environment. Both averaged science noise and calibration differences retain |b|<=1. Uniformly in theta,

    ||R_theta z||^2=(4-theta b)^2+16>=25,
    ||R_theta xi||^2<=1.

These exact inequalities include every realization, not a sampled fit. For each fresh batch take m5,N6,Gamma2. The observed science rank is1 and p_plus=2/7 at every theta. No individual batch reaches .05. At beta1/3, every evidence factor is3, so inf_theta E_3=27>20: power is one by look three in this specified alternative, with anytime null size<=.05 under the null model. Raw error rho1/4 preserves separation. For an observed sequence retaining this global separation, the mismatch-corrected evidence crosses by three looks only when (1/3+delta)^3<=1/20; this is an explicit certificate sensitivity bound, not an estimated noise tolerance or sample-optimality theorem. Total-variation proximity alone does not preserve the alternative’s probability-one separation or power.

## Exact exposure-count optimization within the supplied protocol

The preceding36-exposure fixture is not sample-optimal even in its narrow deterministic setting. Under perfect global separation, Gamma2, and a fresh batch with m calibration pairs plus one science pair, the smallest robust p is2/(m+2). Choosing the frozen binary threshold beta equal to that value gives evidence factor(m+2)/2 at cost2(m+1) exposures.

Within this class, the least exposure count guaranteeing the1/20 threshold is26. Use batch calibration sizes(2,2,2,3), hence pair costs(3,3,3,4), and evidence factors(2,2,2,5/2). Their product is20. The exact dynamic program B(0)=1 and

    B(c)=max_(2<=j<=c, c-j feasible) B(c-j)*(j+1)/2

enumerates every partition of integer pair cost c; batches have at least one calibration pair. Exact rational evaluation gives B(13)=20 and B(c)<20 for every c<13. This is a finite exhaustive cost certificate, not a universal optimal-inference or measured-device result. Randomized tests, general betting functions, reused data, exposure allocation with an independent matching-law proof, batch setup costs and other physical resources are outside this optimization. Different thresholds cannot improve the guaranteed product in this binary-bet class: under the perfect-separation premise beta below the minimum p gives zero, and beta above it decreases the factor.

## Evidence and next condition

The companion exact-fraction probe enumerates finite weighted-score pools with ties, checks all interval-weight corners and rational sensitivity endpoints, derives the paired-exposure distributions, verifies counterexamples and the three-look inequalities. Universal inference rests on the written proofs. These are internal mathematical checks and independent read-only review, not external-expert, empirical or proof-assistant certification.

Actual use requires a real fixed-window repeated-exposure protocol, conditional symmetry or another matching-law proof, justified covariate support/weight bounds, fixed-signal validity, and global shared-graph profiling. This construction makes those interfaces explicit but does not supply measured survey data or select a native GU action.
