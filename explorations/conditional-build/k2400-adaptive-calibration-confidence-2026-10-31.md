---
title: "K2400 Adaptive calibration and anytime shared-graph inference"
status: active_research
doc_type: exploration
created: "2026-10-31"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional probability theorem; no measured calibration or native GU verdict
scripts:
  - tests/channel-swings/k2400_adaptive_calibration_confidence_probe.py
---

# K2400 Adaptive calibration and anytime shared-graph inference

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
result: K2400
carrier: fresh binary-environment labels and paired residual pools with one shared observation parameter LAYER=toy CHIRALITY=N/A
pairing: conditional probability expectation and nonnegative evidence products ON=declared_carrier
real_structure: real Bernoulli laws with fixed p,q and conditional matching law
grading: past information, current hidden assignment, and future label reuse
action_owner: repository-construction -- K2376 conditional observation graph and K2397 paired exposure law
target: adaptive calibration confidence, optional stopping and shared-graph rejection MAP-TYPE=evaluation
```

## Result and scope

Fixed independent training in [K2397](k2397-finite-training-shift-confidence-2026-10-31.md) can be replaced by a confidence sequence: calibration may stop, resume or allocate observations using past results. Each completed science pool may contribute its **environment labels once** to later calibration, provided those labels have the fixed conditional Bernoulli laws assumed below. This permits useful learning without a separate label-only pilot. Its residuals cannot be reused as fresh science evidence.

The price of unrestricted predictable adaptation is an additive error guarantee `delta+eta`, proved with a stopped shadow process. Conditioning on the future all-time calibration-coverage event is invalid in general. The stronger K2397 independent-training formula remains valid in its original scope; it does not transfer automatically.

This is conditional mathematics for the supplied metric f(R) observation graph. SC-COS-50/51/54 ASSERTS retain their source meanings; no bridge to their native displacement action, held-out cosmology, measured matching stability or LT-GR2e recovery is supplied. Exact synthetic paths below establish feasibility of the mathematical interface, not statistical power or a measured dataset.

## 1. Two confidence sequences under predictable sampling

Let each revealed calibration label in stream P or Q be Bernoulli with fixed conditional probability p or q given **the entire prior history**, including past science. Stream choice and whether to sample are predictable. This is stronger than marginal stationarity, and excludes response-dependent retention and drift. The streams need not be mutually independent if each next conditional law is as stated.

For n labels in one stream and k successes, use the uniform-prior likelihood mixture

    M_n(u) = B(k+1,n-k+1) / [u^k (1-u)^(n-k)]
           = 1 / [(n+1) binom(n,k) u^k (1-u)^(n-k)].       (1)

For fixed true u in(0,1), integrate likelihood-ratio martingales over v∈[0,1]; M_n(u) is a nonnegative martingale starting at1. Holding it constant when the other stream is sampled preserves this property in calendar time. At u=0 or1, define by the corresponding likelihood ratio on its support; paths impossible under u may give infinity, and the on-support mixture is a supermartingale (mass can be lost), which suffices.

Set C_n={u∈[0,1]:M_n(u)<=1/epsilon}. Ville's inequality bounds the probability of ever losing true u by epsilon. Allocate epsilon_P+epsilon_Q=delta; a union bound gives simultaneous all-time coverage at least1-delta. Optional stopping and restarting data collection do not require a new delta allocation while the original products and counts continue. Resetting the product and repeatedly claiming a fresh epsilon is a different procedure.

For exact outward rounding on a rational grid, M_n is decreasing up to k/n and increasing afterwards. A lower endpoint may move to a grid point g<=k/n only when M_n(g)>=1/epsilon; the upper moves to g>=k/n by the same test. Include 0 or1 when not excluded. The resulting closed interval contains C_n; n=0 returns[0,1]. This is rounding outward, not taking only accepted grid points. Taking running intersections is also safe but is not used by the finite fixture.

## 2. Predictable robust factors and the stopped proof

Before science look j, freeze the confidence rectangles from completed labels and past history. Map them to the extended odds interval

    r = q(1-p)/(p(1-q)),

using monotonic endpoints, retaining 0 and infinity. Use interior p,q for the pooling proof; degenerate supports require separate support handling. For a pool's environment values z_i∈{0,1}, nonnegative permutation-equivariant scores b_i, n_z counts and S_z sums, define

    C_j = sup_r (r S_1+S_0)/(r n_1+n_0),
    e_j(theta) = 1-lambda_j + lambda_j b_I/C_j,            (2)

where0<=lambda_j<=1 is predictable, I is the distinguished science item and theta is the same graph parameter at every look. The score vector may use the current unordered pool symmetrically but cannot privilege its revealed science assignment. If C_j=0, define b_I/C_j=0; under a covered conditional law this event carries zero probability of a positive distinguished score. For absent environment groups use their actual limiting group, not an undefined0/0.

The ratio in (2) has constant-sign derivative in r, so its supremum is at an endpoint; infinite odds give the within-environment mean. Under K2397's conditional matching law, assignment weights are proportional to r^z_i. Thus E[e_j(theta0)|past]<=1 whenever the frozen set contains the true p,q, also after averaging the pool. Neither training nor environment labels establish the matching law or common signal/windows.

Let tau be the first look whose **pre-look** confidence set misses true p or q. Though unobservable, tau is predictable in the proof. Define e'_j=e_j before tau and e'_j=1 from tau onward. Its product is a nonnegative supermartingale because every active factor has conditional expectation<=1. Hence

    P(ever E_j(theta0)>=1/eta) <= eta + delta.             (3)

Indeed the actual and shadow products agree unless calibration ever fails, an event of probability<=delta. This avoids conditioning on a future event. Assume a fixed parameter set Theta containing theta0 and measurable profiled crossing events. A global shared-graph rejection requires inf_theta E_j(theta)>=1/eta, which implies crossing by the true fixed theta0 if that graph is true; there is no union penalty over theta. Computing the infimum still requires a complete parameter certificate, not a grid heuristic.

For alpha=1/20 and delta=1/100, use eta=1/25 and threshold25. Using K2397's independent-training threshold99/4 would justify only delta+4/99=499/9900>1/20 by this adaptive proof. This does not prove the threshold always fails; it proves that its old error calculation is unavailable under the enlarged assumptions.

## 3. Legal and illegal reuse

After a look's test factor is fixed, reveal/record its known-role P and Q environment labels and update counts for **future** looks. The required conditional Bernoulli assumption must hold in the filtration including already revealed information; if revealing residuals predicts labels, order the joint reveal as one fresh block and use the block's conditional label likelihood given the prior history, not a falsely sequential conditional law. A block of multiple labels needs its stipulated joint product law, or a correctly constructed joint likelihood ratio. Merely having Bernoulli marginals is insufficient.

No separate independent pilot is required by the theorem, but exposures still cost acquisition, matching, measurement and reset. Reusing a fair event H as evidence twice gives factors2·1_H and product4·1_H with expectation2; fresh-factor validity has been lost. Choosing a bonus at the observed distinguished assignment yields e equal to pool size under uniform assignment; permutation-equivariance is essential. Defining a set using the current assignment and treating it as pre-look is equally invalid.

## 4. Exact synthetic continuation and resource boundary

The probe uses epsilon=1/200 per stream and grid multiples of1/12. At n100,k50 the outward interval is[1/4,3/4]. On an alternating0,1 label path the first sample count with interval width<=1/3 is n128,k64, yielding[1/3,2/3]. Two streams following that path use256 labels; this is a path-specific stopping time, not a guaranteed cost or power claim. The inherited shared-graph fixture then has odds[1/4,4], worst-case eight-look product(1/4)(31/16)^7>25 over every theta∈[-1,1]. The two nonconstant residuals are(1-theta)^2 and(1+theta)^2 versus calibration residual1/4; the remaining six have residual16. The first score fails to exceed1/4 exactly on[1/2,1], the second exactly on[-1,-1/2]; thus the factors are piecewise constant with breakpoints±1/2. These breakpoints and endpoints are evaluated, with each open cell represented separately. Multiplying separate per-look minima incorrectly loses shared-parameter evidence.

There is **no uniform deterministic exposure guarantee** for learning bounded odds without bounded p,q. For any finite T, the path with all Q labels1 and all P labels0 has positive probability when0<p,q<1. The intervals retain q=1 and p=0, so their robust odds upper endpoint remains infinity. When science is the sole env1 item, any nonnegative factor conditionally safe for this pool under every allowed odds value on that assignment is<=1. Earlier26/28-exposure optima assumed supplied finite odds and do not transfer.

A useful fallback requires no calibration: take C=max(S_0/n_0,S_1/n_1) over present groups, valid for all odds. This gives an unconditional e-process without delta spending and still learns within a repeated environment. It sacrifices between-environment borrowing. Choosing between a calibrated test and this fallback after seeing which wins requires a valid mixture or preallocated testing budget; two separate level-alpha tests cannot both be called one level-alpha test. A fixed convex mixture of nonnegative supermartingales is valid for the same null; calibrated processes have only their stopped/coverage guarantee unless their construction is made unconditional.

## Verification and next meaningful input

The accompanying rational probe checks likelihood-mixture recursion, finite optional-crossing probabilities, outward intervals and the exact stopping path, normalized pool bounds, complete shared-parameter cells and counterexamples. These are finite exact checks; the universal claims rest on the written martingale and stopping proofs. They are not external-expert or proof-assistant certification.

Preflight statistical and observational lenses target predictable selection and conditional matching; postflight challenges future-event conditioning, label/residual reuse, support endpoints and deterministic cost. Actual implementation requires a measured stability/matching argument and priced acquisition protocol. A larger mathematical successor is robust confidence under a specified drift model or dependence-safe block calibration; arbitrary drift is not addressed by renaming the current labels stable.

Classical method attribution: beta-mixture confidence sequences are established methodology; see [Howard et al., Time-uniform, nonparametric, nonasymptotic confidence sequences](https://arxiv.org/abs/1810.08240). No novelty is claimed for that method.
