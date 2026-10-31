---
title: "K2403 Drift-robust calibration and heterogeneous fresh pools"
status: active_research
doc_type: exploration
created: "2026-10-31"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematics; no measured calibration, hardware or native GU verdict
scripts:
  - tests/channel-swings/k2403_drift_robust_calibration_probe.py
---

# K2403 Drift-robust calibration and heterogeneous fresh pools

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
result: K2403
carrier: adaptively observed binary environment labels and matched residual pools LAYER=toy CHIRALITY=N/A
pairing: declared conditional probability or positive Hilbert channel pairing ON=declared_carrier
real_structure: real probabilities and exact rational or algebraic coefficients
grading: observed records, hidden roles and conditional parameters
action_owner: repository-construction -- K2400 conditional calibration and K2397 matching model
target: time-uniform calibration, heterogeneous pool odds and identification limits MAP-TYPE=evaluation
```

## Result and scope

[K2400](k2400-adaptive-calibration-confidence-2026-10-31.md) used fixed conditional Bernoulli parameters. Here calibration may drift inside a **supplied predictable bound**. The same robust scientific normalizer also works for fresh pools whose calibration members have different environment probabilities, provided conditional independence, hidden-role randomization and a common conditional residual law hold. A sharp identification floor shows which uncertainty more calibration cannot remove.

These are conditional probability results for the existing observation interface. They neither establish measured stability nor identify that interface with the source's connection-displacement cosmology (SC-COS-50/51/54 ASSERTS; LT-GR2e remains open). Bounds on environment frequencies do not establish matching of signals, windows or residuals.

## 1. Anytime anchor and current-law confidence

For sampled labels X_s in[0,1], let p_s=E[X_s|F_(s−1)] and assume |p_s−a|<=d_s for a fixed anchor a and predictable known d_s. The filtration includes all previously available science. Selecting a stream or taking a sample must precede its label. Let dbar_n=sum d_s/n. At n>=1 define

    r_n=sqrt(log(2n(n+1)/epsilon)/(2n)),
    C_n=[Xbar_n−dbar_n−r_n, Xbar_n+dbar_n+r_n] ∩[0,1].       (1)

Use C_0=[0,1]. Conditional Hoeffding's lemma gives E[exp(lambda(X_s−p_s))|past]<=exp(lambda²/8). Iteration, exponential Markov and optimization at lambda=4r give a two-sided tail <=2exp(−2nr²). For completeness, the lemma follows by convexity from a Bernoulli with mean p; the second derivative of its centered log-MGF is the variance of a tilted Bernoulli, at most1/4, and its value/first derivative at zero vanish. Integrating twice yields lambda²/8 for both signs. No independence across times is assumed.

At r_n the failure probability is epsilon/[n(n+1)]; summing over n proves simultaneous anchor coverage >=1−epsilon. Random predictable d_s are allowed if their asserted bounds hold pathwise. Pausing or changing streams preserves the argument on each stream's sampled filtration. Running intersections of the anchor intervals are valid and can improve a poor later average.

For a future science or calibration member with |p_current−a|<=h_j, expand the pre-look anchor interval by h_j and clip. Do this for P and Q anchors with epsilon_P+epsilon_Q=delta. Freeze all current-law intervals before revealing the pool. If drift allowances are only valid with probability1−beta, charge their joint failure separately: the resulting scientific guarantee is generally beta+delta+eta. A fitted drift budget is not a known bound.

## 2. Heterogeneous fresh pools: exact effective odds

Given the pre-pool past, let one science member have environment parameter q and m calibration members have parameters p_1,...,p_m in(0,1), all conditionally independent. Conditional on those labels and the pre-pool past, residuals are independent draws from one common law K_z for each environment z, independently of role; a uniform hidden-role permutation removes member identity. Equivalently this specifies the complete randomization/matching experiment. Scores must be nonnegative and permutation-equivariant functions of the unordered pool and the same graph parameter theta. No observed member identity may leak into a score.

Set o_i=p_i/(1−p_i), and let e_k be their elementary symmetric polynomial. If the complete pool has t ones, 1<=t<=m, each environment-one candidate has relative science-assignment weight r_eff versus an environment-zero candidate, where

    r_eff=odds(q) (m−t+1)/t · e_(t−1)(o)/e_t(o).           (2)

To derive this, conditional on a candidate's role the remaining calibration labels are uniformly permuted. Their particular configuration has probability P(N_cal=k)/binom(m,k); P(N_cal=k)=prod(1−p_i)e_k(o). Divide the environment-one and zero candidate likelihoods, retaining the binomial ratio. The common K_z densities cancel. If every label is the same, all candidate weights are equal within that sole group.

Counting each t-element subset t times gives

    t e_t= sum_|A|=t−1 [prod_i∈A o_i] sum_i∉A o_i.

Hence e_t/e_(t−1) lies between (m−t+1)min(o)/t and (m−t+1)max(o)/t. Thus

    odds(q)/max_i odds(p_i) <= r_eff <= odds(q)/min_i odds(p_i).  (3)

If all p_i lie in a covered common interval[L,U] and q in[l,u], use endpoint odds[odds(l)/odds(U),odds(u)/odds(L)]. Degenerate bounds use monotone limits; actual p_i,q remain interior for this proof. This extends the homogeneous matching result without substituting an average probability. For p=(1/4,3/4),q=1/2, the exact r_eff is3/5 at t=1 and5/3 at t=2. Average p=1/2 incorrectly gives1; the safe interval[1/3,3] covers both.

With environment score sums S_z and counts n_z, set

    C=sup_r (r S_1+S_0)/(r n_1+n_0),
    e(theta)=1−lambda+lambda b_I/C,  0<=lambda<=1.          (4)

The derivative has constant sign, so the supremum is at an endpoint. The exact assignment law and(3) make its conditional expectation <=1 whenever coverage holds. Keep the zero-score and absent-group conventions of K2400. This does not allow reusing previously consumed residuals as fresh evidence or arbitrary dependence between calibration members.

## 3. Shared-graph inference, fallback and costs

Apply K2400's predictable stopped-shadow process at the first pre-look interval failure. The probability that the product at the true fixed theta ever reaches1/eta is <=delta+eta (plus beta when applicable). Rejection by inf_theta product>=1/eta implies crossing at the true theta, without a union penalty over a continuous parameter. Computing that infimum still requires a complete certificate; per-look minima need not compose sharply.

The calibration-free alternative C=max_z S_z/n_z needs only the equal-within-environment assignment property, not between-environment odds. Under that property it gives an unconditional e-process. A predictable convex combination of a valid full-odds factor and a valid calibrated factor is safe only while calibration is covered, retaining delta+eta. It is not a way to remove calibration failure by taking whichever full product looks larger.

A concrete favorable path illustrates the price: at n=4096,k=2048 in each stream, epsilon=1/200, a rational radius1/16 is certified by exp(2n/256)>2n(n+1)/epsilon. With historical drift d=1/32 and deployment allowance h=1/32, each current interval is[3/8,5/8], with odds ratio range[9/25,25/9], contained in[1/4,4]. Deliberately widen these learned odds to[1/4,4] and use that conservative endpoint normalizer. The inherited eight-look continuous shared-graph fixture then remains valid at threshold25. Its complete piecewise cells and endpoints give minimum(1/4)(31/16)^7>25. This uses8192 calibration-label observations plus48 science-pool exposures on that stated path. Their sum8240 is bookkeeping only, not a common measured time, energy or monetary cost. It is neither a deterministic acquisition guarantee nor power on observed data. Every fresh heterogeneous member must fit the current deployment tube; old samples do not gain freshness by relabeling.

## 4. Sharp information limit and failure controls

For constant d choose interior mu with anchors a_±=mu±d. Both admissible models generate the same iid Bernoulli(mu) calibration law. Any interval uniformly covering its anchor with probability1−epsilon contains BOTH anchors with probability>=1−2epsilon under that common law. Thus its width is at least2d on that event. With future deployment allowance h, the same calibration-only experiment can have deployment probabilities mu±(d+h); its corresponding confidence width is at least2(d+h), provided these lie inside[0,1]. This is a sharp irreducible identification floor for the stated information, not an assertion that(1) is finite-sample optimal. Arbitrary varying d_s can favor selected substreams or earlier prefixes.

A block of perfectly copied labels X_1=...=X_m=H has one innovation. Treating it as m independent calibration innovations generally violates the conditional-mean/drift premise after its first reveal. Response-dependent retention similarly invalidates the sampled filtration. Neither control is evidence that correctly specified bounded martingale differences fail.

## Verification

The exact probe checks heterogeneous Poisson-binomial assignment probabilities against direct hidden-role enumeration, endpoint bounds and complete finite score boxes; rational exponential lower bounds for outward confidence radii; finite adaptive crossing by exact dynamic programming; the favorable shared-graph cells; and actual counterexamples to average-law substitution, omitted drift, dependent pooling and evidence reuse. Universal claims rest on the proofs above, not the number of fixtures. Read-only statistical review supports the argument; no external-expert or proof-assistant certification. Actual deployment requires a measured drift/matching model and complete acquisition cost.
