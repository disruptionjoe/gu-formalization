---
title: "K2346 Positive count-response discrimination with Cox brightness"
status: active_research
doc_type: exploration
created: "2026-10-30"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematics; no native GU or empirical certification
scripts:
  - tests/channel-swings/k2346_positive_count_response_discrimination_probe.py
---

# K2346 Positive count-response discrimination with Cox brightness

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
result: K2346
carrier: two disjoint sphere photon bins and a fixed bounded quadrupole shape family LAYER=toy CHIRALITY=N/A
pairing: ordinary probability and likelihood ON=declared_carrier
real_structure: real coefficients; complex Hilbert adjoint where stated
grading: Poisson total and angular marks
action_owner: repository-construction -- positive heat-response Poisson/Cox model
target: finite conditional discrimination and its exact nuisance boundary MAP-TYPE=evaluation
```

## Result and prior boundary

[K2343](k2343-conditional-count-exchangeability-2026-10-30.md) constructs an equality-null test, not a discriminator of distinct response laws. [K2327](k2327-constrained-seed-likelihood-2026-10-30.md) already owns Gaussian projective-response identifiability. Here a positive point-process realization admits exact elimination of arbitrary common Cox brightness and a finite-count test uniform over a bounded shape nuisance. The two heat responses and shape interval are supplied; they are not two derived cosmologies or the K2331 Gaussian count experiment. SC-COS-50/51/54 ASSERTS remains unchanged, as do ledger0.263 and all native physical verdicts.

## Positive likelihood and nuisance elimination

On the unit sphere fix a known axis v and f(n)=A[1+q P2(v.n)], A>0 and q in[1/2,3/4]. P2(x)=(3x²−1)/2, so f>=5A/8>0. A may be deterministic or randomly mixed with ANY distribution, including lognormal; this is a common scalar amplitude, not an arbitrary spatial lognormal field. q may also be random in the stated interval and correlated with A; the uniform conditional bounds below survive its changed posterior.

For h=0,1 supply R_h=exp(t_h Delta_sphere), t0=log2/6,t1=log2/2. Their quadrupole factors are b0=1/2,b1=1/8. Heat preserves positivity and total flux. Count each photon once in the disjoint polar region |v.n|>=1/2 and its equatorial complement. Each has area2pi, and its mean P2 is respectively3/8 and−3/8. Conditional independent Poisson bin means are

    mu_plus=2pi E A(1+3q b_h/8),
    mu_minus=2pi E A(1−3q b_h/8).

Their joint likelihood factors EXACTLY into Pois(N;4pi EA) times Bin(K;N,p_h(q)), where N is the total and

    p_h(q)=1/2+3q b_h/16.                            (1)

Consequently conditioning on N eliminates A, even after Cox mixing. With deterministic A and N>0, its profile maximum is N/(4pi E); the profiled q is clip_[1/2,3/4]{16(K/N−1/2)/(3b_h)}. N=0 carries no directional information. Integrating a fixed common mixing law gives the same count-total factor under both hypotheses. With random q the conditional law is a mixture of these binomials, so no point-estimate formula is asserted for an arbitrary joint prior.

For general fixed positive bin means EA r_hj the same calculation yields Multinomial(N,p_h), p_h=r_h/sum r_h. Equal normalized vectors are exactly absorbed by free amplitude. Unequal fixed vectors are identifiable with growing photon count; composite response models require separation of their whole normalized sets. This criterion does not identify an operator from one unknown arbitrary input.

## Finite composite test and exact calibration

Under H0, p belongs to[35/64,73/128]; under H1 it belongs to[131/256,265/512]. The gap is15/512. Decide H1 when K/N<=545/1024, and H0 otherwise. Each error is at most

    exp(−225 N/524288).                              (2)

Proof: for a Bernoulli variable the second derivative of its centered log moment generating function is the variance of a tilted Bernoulli, at most1/4. Its value and first derivative vanish at zero, so the log-MGF is at most t²/8. Independence, exponential Markov and optimization give Pr(|one-sided sample error|>=a)<=exp(−2Na²). The threshold is distance15/1024 from either nearest endpoint. Binomial stochastic monotonicity places the worst errors at the nearest endpoints. Mixtures cannot increase their supremum. At N>=8192 the exponent is at least225/64>3 and exp3>20; both errors are below5%. The probe also sums the actual N=8192 binomial tails exactly as integers, rather than confusing the concentration bound with an exact attained risk.

The test conditions on the observed count; N>=8192 is a data condition, not a promise that finite exposure attains it. A fixed photon-number stopping experiment also gives independent identically distributed angular marks with this law conditional on the latent values A,q, which must remain constant throughout acquisition. Unknown time-varying shapes require a separate model.

## Executed robustness and brightness consumers

If calibrated actual normalized polar probability differs from its admitted value by at most eta=1/512, the SAME threshold has remaining margin13/1024. At N>=12288 the error bound is exp(−507/128)<1/20. This accommodates, for example, an independent contaminating mark fraction at most eta, since mixture contamination shifts any bin probability by at most that fraction. Arbitrary correlated photons, count duplication or uncontrolled spatial Cox fluctuations do not obey the binomial theorem. An unrestricted foreground can erase the separation.

For a finite-exposure promise supply Pr(mu<2n)<=beta for mu=4pi EA and n=12288. The Poisson Chernoff bound gives Pr(N<n | mu>=2n)<=exp(−n/4), so

    Pr(insufficient photons)<=beta+exp(−n/4).

Proof uses log E exp(−tN)=mu(exp(−t)−1) and t=log2; its exponent at n<=mu/2 is at most−mu/8. Thus the experiment can return INSUFFICIENT_COUNTS below n; an unconditional wrong-or-inconclusive bound is beta+exp(−n/4)+exp(−507/128). A known lower intensity is the beta=0 case. Lognormal A has no positive lower support; its specified quantile, not merely its name, must supply beta.

Without any intensity floor, no test has uniform finite-exposure power. Both experiments have the same empty-count atom of mass exp(−mu); their total variation is at most1−exp(−mu). A size-alpha test has power at most alpha+1−exp(−mu), tending to alpha as mu tends to zero. This is a rigorous counterweight to the positive conditional bound.

## Exact nonidentifiability and what remains

For unrestricted positive source shapes, let B_t denote heat and choose any positive g. Sources f0=B_t1 g and f1=B_t0 g give B_t0 f0=B_t1 f1 by semigroup commutation: the entire Poisson laws coincide. In the quadrupole family, admitting q0=1/8 and q1=1/2 makes q0 b0=q1 b1=1/16. Independent arbitrary bin amplitudes can likewise absorb any positive response vector. These changed-input counterexamples preserve positivity and show why the shape interval, known axis and response calibration are substantive assumptions.

A physical application must supply competing cosmological/tracer predictions for one positive intensity family, its admitted shape nuisance and response, and a photon sampling law. Neither this supplied heat example nor another arbitrary fitted family can authenticate that bridge. The new conditional count likelihood and exact calibration can then be reused. No novelty, empirical, Lean, external-expert or native GU certification is claimed.
