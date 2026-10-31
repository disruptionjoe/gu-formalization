---
title: "K2388 Shared-graph tests with exchangeable noise and corrupted calibration"
status: active_research
doc_type: exploration
created: "2026-10-31"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematics; no native GU or measured physical verdict
scripts:
  - tests/channel-swings/k2388_exchangeable_noise_calibration_probe.py
---

# K2388 Shared-graph tests with exchangeable noise and corrupted calibration

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
result: K2388
carrier: one stacked real science error and full-experiment calibration vectors LAYER=toy CHIRALITY=N/A
pairing: supplied or independently trained nonnegative residual score; Euclidean form in exact consumers ON=declared_carrier
real_structure: real exchangeable noise; no moment or nonsingularity requirement
grading: training data, calibration replicates and one science experiment
action_owner: repository-construction -- supplied observation graph after K2376 window bridge
target: finite-sample composite-null rank rejection with adversarial calibration replacements MAP-TYPE=evaluation
```

## A different measurement interface

[K2385](k2385-estimated-noise-calibration-2026-10-31.md) supplies a Gaussian/Wishart pivot when independent full-experiment calibration estimates a common positive covariance. The present alternative replaces that parametric premise by exchangeability of complete error vectors. It needs neither a covariance inverse nor finite moments nor a zero noise mean. It does **not** infer exchangeability from an observed calibration sample. The cost includes discrete significance resolution and a potentially very conservative profile over the shared graph.

The graph remains the conditional metric f(R) observation construction inherited through K2376/K2379, not Weinstein's source-native connection displacement. SC-COS-50/51/54 retain ASSERTS polarity, and LT-GR2e, ledger0.263 and canon remain unchanged. No observed null, survey significance or GU prediction is claimed.

## Exact fixed-parameter rank and composite-null theorem

Write z=s+epsilon in R^D and R_theta=I_n tensor[-G(theta),I_r], with one fixed true theta* in the prespecified Theta. The exact null is R_theta*s=0. Let xi_1,...,xi_m denote clean noise-only calibration vectors for the SAME stacked observation, including its windows, selection and cross-sample errors. Assume (epsilon,xi_1,...,xi_m) is exchangeable, conditional on any training data and on the fixed signal. Independence and identical distribution are sufficient, but exchangeability is the operative premise. The coordinates inside a vector need not be independent. Independent noise replicates must not be replaced by unrelated cosmological skies or latent-field draws.

Before looking at these calibration and science vectors, freeze a score a_theta(v) on residual space. It may be learned from separate training data. For instance a_theta(v)=v^T W_theta v with any fixed positive semidefinite W_theta, including a regularized training estimate, is allowed. No inverse, rank, normality or moments are required. Arbitrary scores can have poor power; validity is not an optimality theorem. Prespecify the graph family, admissible parameter set and score rule as well. Assume the profile rejection event is measurable; the finite polynomial fixtures below are semialgebraic.

Set

    p(theta) = [1 + #{j: a_theta(R_theta xi_j)
                            >= a_theta(R_theta z)}]/(m+1),
    p_profile = sup_(theta in Theta) p(theta).
    Reject iff p_profile <= alpha.                               (1)

At the FIXED theta*, R_theta*z=R_theta*epsilon. Conditional on training, the m+1 scores are exchangeable. For any deterministic list of N=m+1 scores, let r_i be the number of list entries greater than or equal to entry i. At most k indices have r_i<=k: ties can only make the count smaller. Exchangeability gives

    Pr(p(theta*)<=alpha | training) <= floor(N alpha)/N <= alpha.

Integrate over training. Rejection in (1) implies p(theta*)<=alpha, so the composite test has size at most alpha. The fitted supremum is not claimed uniform, and there is no fitted-parameter degrees-of-freedom correction. Ties MUST count with >=; replacing it by > makes all-identical scores falsely reject at every alpha>=1/N. At alpha<1/N this nonrandomized test cannot reject.

This is an application of the standard exchangeable-rank argument, not a claim to have invented conformal inference; see the primary exposition [Kuchibhotla, Exchangeability, Conformal Prediction, and Rank Tests](https://arxiv.org/abs/2005.06095) and [Lei et al., Distribution-Free Predictive Inference for Regression](https://www.stat.berkeley.edu/~ryantibs/papers/conformal-jasa.pdf). The contribution here is the explicit shared-graph profile, error and contamination interface and its certified consumers.

## Contamination, with a precise replacement model

Suppose up to k of the m calibration vectors are replaced arbitrarily AFTER an underlying clean exchangeable sample has been generated. Locations and replacements may depend on the entire clean sample and science error. The training score stays frozen and unaffected. The science vector is not replaced in this model. Let p_obs use the supplied, possibly replaced calibrations. Define

    p_k(theta)=min(1, p_obs(theta)+k/(m+1)).                        (2)

For each theta and every realization, the original clean exceedance count is at most the observed count plus k. Therefore p_k(theta)>=p_clean(theta). Rejecting when sup_theta p_k(theta)<=alpha retains size at most alpha, regardless of the replacement strategy. The proof does not incorrectly condition on an adaptively chosen clean subset. An estimated k has no license from this theorem; k is a supplied deterministic bound.

The correction is sharp against this adversary. Take N distinct exchangeable scores; the clean science upper rank r is uniform on1,...,N. An adversary replaces up to k larger calibration scores by smaller ones, yielding observed upper rank max(1,r-k). Adding k restores corrected numerator max(k+1,r). At any grid threshold alpha=l/N with l>=k+1, rejection has probability exactly alpha. Any smaller additive numerator correction c<k has maximum corrected value (N-k+c)/N<1, so rejecting at that value rejects every rank and violates size. This sharpness statement presumes k<=m; k=m gives only the trivial p=1 rule. The probe enumerates the m3,k1 construction, including its uncorrected size3/4 at nominal1/2.

The smallest possible p_k is (k+1)/(m+1). With contamination that creates large calibration scores the realized numerator can increase again; these are distinct losses. If the science observation is itself corrupted on an event of probability at most beta, coupling to the underlying clean experiment and a union bound give the unconditional size bound alpha+beta, capped at one, provided that clean experiment satisfies the stated premise. No conditional-on-no-corruption rank validity is assumed.

## Graph discrepancy and unknown matched bias

For a prescribed true graph residual h* in H_theta*, define p_k(theta,h) by replacing the science score with a_theta(R_theta z-h), while leaving calibration scores unchanged. Reject only if sup_(theta,h in H_theta) p_k(theta,h)<=alpha. The fixed true pair cancels the graph residual, so the same proof applies. For a Euclidean score and H_theta the raw ball ||h||<=rho, the minimal science score is

    b_theta = max(0, ||R_theta z||-rho)^2.

Using b_theta against all calibration scores gives exactly the worst h at that theta. This is a raw-coordinate allowance, not a variance estimate.

Nonzero bias shared by the complete science-error and calibration law is permitted: no centering is needed. A science-only bias is not. With an exact null signal, calibration noise identically zero and science error a fixed nonzero density offset, the apparent p-value is 1/(m+1) on every experiment. Thus a matching zero covariance, or a large calibration sample, cannot repair a mismatched noise mean. This is a failure of the exchangeability premise, not evidence against the graph or GU.

## Finite global certificate with calibrated sample corruption

Use D4,d2 and one shared scalar theta in[-1,1],

    R_theta=[[-theta,1,0,0],[0,0,-theta,1]],
    z=(1,3,1,-3),   xi_j=(4,0,0,0), j=1,...,59,
    k=1,   alpha=1/20,   a(v)=||v||^2.

These are exact synthetic arithmetic inputs, not measured data or a claim about typical calibration draws. The science score is18+2theta^2 and every displayed calibration score is16theta^2. Their difference

    18-14theta^2 = 4+14(1-theta^2) >= 4

is a global certificate. Thus the displayed data have sup p_k=2/60<1/20. Even if any one displayed calibration is replaced by an arbitrary vector, its score can add at most one exceedance: sup p_k<=3/60=1/20, so rejection survives. This is a deterministic stability statement about that dataset, distinct from the probabilistic size theorem.

The same certificate survives raw graph-error radius rho=1/4: writing u=|theta|<=1,

    18+2u^2-(4u+1/4)^2
      =31/16+14(1-u^2)+2(1-u) >0.

Therefore the smallest corrected science norm remains greater than every unchanged calibration norm. At rho=1/2 and theta=1, sqrt20-1/2<4; all calibration scores exceed the corrected science score, so p_k=1 and the robust test does not reject. Widening Theta to[-2,2] similarly gives theta2 with calibration score64 above science score26, so the uncorrected test does not reject. Calibration radius and error budget matter.

For general scalar affine graphs and polynomial scores, count changes occur only at roots of the finitely many score-difference polynomials. Exact root isolation, sign checks on every cell and endpoint evaluation can certify the maximum count. A local value or a grid produces a LOWER bound on sup p_k; observing small values there cannot certify rejection. The explicit widened-ball fixture has small p at theta0 but p=1 at theta2.

## Nonempty distributional power statement

A supplied bounded law demonstrates that the interface is not vacuous. Let clean errors be xi=(b,0,0,0), |b|<=1, with any common distribution (including a nonzero mean and singular covariance), and let science error be exchangeable with the calibration errors. Supply alternative signal s=(0,4,0,-4), theta in[-1,1], Euclidean score, m59,k1 and alpha1/20. For EVERY realization,

    ||R_theta(s+epsilon)||^2=(4-theta b)^2+16>=25,
    ||R_theta xi_j||^2=theta^2 b_j^2<=1.

Consequently, even after one arbitrary calibration replacement, sup p_k<=3/60 and the test rejects with probability one in this specified alternative model. A raw error allowance rho1/4 preserves the separation because5-1/4>1. This is an analytic conditional power guarantee for supplied bounded support; it is not a survey noise estimate, a claim of generic power or a proof that empirical heavy-tailed data have bounded support.

## Contrary tests and acceptance ceiling

The companion probe exhaustively checks small finite rank lists including ties and arbitrary score replacements, and verifies the exact global polynomial and changed-radius inequalities. It also executes a shared-parameter countercontrol: z=(1,0), noiseless calibrations and Theta={0,1} give p(0)=1 and p(1)=1/(m+1). The null is true at0. Taking inf p rather than sup would falsely reject every time. A score trained to vanish on all calibration points and be positive elsewhere likewise gives p=1/(m+1) almost surely for a continuous new sample: fitting on the rank-calibration set without a valid symmetric conformal construction breaks the proof. The probe checks the finite interpolation analogue; the continuous probability-one assertion is written reasoning, not simulated coverage.

No native source hypothesis, physical ledger row or canon grade changes. Universal coverage and power statements rest on the written proofs; finite algebra and exhaustive finite-list checks are controls. Independent internal review checked the rank proof, profile direction, adaptive replacement sharpness, raw-error consumer and power bounds; a replay-detected raw-radius constant was corrected from63/16 to31/16, preserving its positive margin; no remaining mathematical finding was identified. This is not external-expert or proof-assistant certification. Physical use still requires an actual same-window full-experiment noise calibration protocol, a justified exchangeability/shift account, frozen training and shared gain model, and a justified contamination or discrepancy budget.
