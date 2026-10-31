---
title: "K2397 Finite-training shift confidence and shared-environment evidence"
status: active_research
doc_type: exploration
created: "2026-10-31"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematics; no native GU or measured physical verdict
scripts:
  - tests/channel-swings/k2397_finite_training_shift_confidence_probe.py
---

# K2397 Finite-training shift confidence and shared-environment evidence

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
result: K2397
carrier: independent finite binary-environment training and fresh paired-exposure pools LAYER=toy CHIRALITY=N/A
pairing: nonnegative residual scores and conditional probability expectation ON=declared_carrier
real_structure: real errors with K2391 conditional central symmetry and fixed environment laws
grading: independent training, pooled environment groups, one shared graph and fresh looks
action_owner: repository-construction -- K2376 conditional windowed observation graph
target: finite-data nuisance confidence and anytime shared-graph rejection MAP-TYPE=evaluation
```

## Result, Layer 0 and work selection

K2394 assumes a supplied shift budget. This successor learns a confidence set for that budget from finite independent categorical training, proves the complete calibration-plus-testing error bound, and constructs a sharper pool normalizer that preserves equal weights within each environment. Infinite uncertainty about between-environment weights still allows within-environment evidence. A synthetic eight-look continuous-parameter certificate survives the allocated calibration error; it is not measured calibration or a power guarantee.

The operative graph remains the conditional metric f(R) observation graph, not Weinstein's source-native connection displacement. The backwards demand is a reliable same-window observation test with a learnable environmental selection law. A bounded source-to-physics confrontation would also need actual repeated-exposure records, common signal/windows, a matching-law argument and an authenticated native-to-observable map. None is supplied here. We therefore remove one supplied statistical premise without inventing observations. SC-COS-50/51/54, LT-GR2e, the ledger, hypotheses and canon do not change. No substrate candidate or novelty for binomial confidence inversion is claimed.

## Explicit sampling model

There are exactly two **observed** environment labels, 1 and 0. Calibration environments follow P=(p,1-p), science environments Q=(q,1-q), with fixed unknown p,q in (0,1). Before testing, take n_P iid P labels and n_Q iid Q labels, independently of each other and of all future exposures; their numbers of ones are K_P,K_Q. Sample sizes and the confidence construction are fixed before those counts. This training measures environment frequencies only: it neither estimates nor verifies error symmetry, matching signal/windows or instrument stability.

For every future look, conditional on training and the full testing past, one science pair has law Q(dc)K_c(depsilon) and m calibration pairs have law P(dc)K_c(dxi), independently, as in K2391. The exposure construction supplying K_c retains the same fixed signal, windows and conditional central symmetry. The same P,Q govern training and every future look; unmodelled drift is excluded. Batch sizes and score/bet rules may depend on training and past, but not on the current distinguished science label. Keep a prespecified Theta containing one fixed true theta* under the null, and require measurable profiled crossing events. Choosing a different Theta from training needs its own guaranteed inclusion or additional error budget.

## Exact finite-grid confidence construction

Fix delta in (0,1), epsilon=delta/4, and a finite rational grid G containing 0 and 1. For X~Binomial(n,u), write

    Tplus(n,k,u)=Pr_u(X>=k),   Tminus(n,k,u)=Pr_u(X<=k).

For observed k define

    L_n(k)=max({0} union {g in G:Tplus(n,k,g)<=epsilon}),
    U_n(k)=min({1} union {g in G:Tminus(n,k,g)<=epsilon}).       (1)

The endpoints are outward grid roundings of one-sided exact confidence limits; endpoints included in [L,U] make them conservative. No correction by the number of grid points is necessary.

Proof: Tplus(n,k,u) is increasing in u and decreasing in k, while Tminus is decreasing in u and increasing in k. If u<L_n(K), a qualifying g>u gives Tplus(n,K,u)<=epsilon. For fixed u, the latter event is an upper tail {K>=k0} whose probability is its endpoint tail, at most epsilon (or the event is empty). Similarly Pr_u(u>U_n(K))<=epsilon. Thus each interval covers with probability at least 1-2epsilon. The union bound for P and Q gives

    Pr(Good)>=1-delta,
    Good={p in [L_P,U_P] and q in [L_Q,U_Q]}.                (2)

This proof is uniform over the full continuum u in [0,1]; the probe's rational values are controls, not a continuum proof. The intervals are nonempty: if a qualifying lower g exceeded a qualifying upper h, monotonicity at an intermediate u would give Tplus(n,k,u)+Tminus(n,k,u)<=2epsilon<1, contradicting the identity 1+Pr_u(X=k). Fixed-sample inversion does not authorize stopping training when an appealing interval appears.

## Exact shared-environment conditional normalizer

The science-index weights at a null parameter are w_1=q/p and w_0=(1-q)/(1-p). Their only relevant ratio is the **odds ratio**

    r=w_1/w_0=q(1-p)/(p(1-q)).                              (3)

Over the rectangular confidence set intersected with (0,1)^2, r is increasing in q and decreasing in p. Its infimum and supremum are

    r_- = L_Q(1-U_P)/(U_P(1-L_Q)),
    r_+ = U_Q(1-L_P)/(L_P(1-U_Q)),                          (4)

with limits 0 and infinity at the appropriate boundary. In nondegenerate interior intervals these bounds are attained. Boundary statements below use suprema and limits, not claims of an attained zero-probability environment law.

Given an unordered pool, let n_c count members of environment c and S_c=sum_(i:C_i=c)b_i for a nonnegative permutation-equivariant assignment b. The same rule sees the whole unordered pool, residual scores and training, but not which member is the science member. Assuming both n_1,n_0>0, the sharp normalizer over this confidence rectangle is

    C_D(b)=max{ (r_- S_1+S_0)/(r_- n_1+n_0),
                (r_+ S_1+S_0)/(r_+ n_1+n_0) }.             (5)

Indeed, the conditional mean is the displayed linear-fractional function of r, whose derivative has constant sign (S_1 n_0-S_0 n_1)/(r n_1+n_0)^2. Its maximum lies at an endpoint or its limit. The rectangle is connected and r continuous on its interior, so the full interval of ratios is available; (5) is sharp for this stated confidence class. For a pool containing only environment c, use C_D=S_c/n_c. At r=0 or infinity the mixed-pool expression means S_0/n_0 or S_1/n_1, respectively. These are limiting bounds for interior p,q; they do not condition on a zero-probability pool under an added boundary law. The asserted model keeps p,q interior. An extension admitting actual zero environment probabilities must first retain Q<<P, discard null-probability pools and establish its conditional-index law separately.

Set e_i=b_i/C_D when C_D>0, and e_i=0 for all i when b=0. Conditional on a training value in Good and on the unordered pool, the actual index distribution has mean of e at most one. Mixing with a constant gives the safe positive factor

    f_i=(1-lambda)+lambda e_i,       0<=lambda<1.            (6)

Scores may depend on candidate theta; validity is required only at the fixed theta*. Tied maximal scores receive zero bonus in the unique-maximum construction. Training-dependent design is safe because the confidence event and the model hold for the frozen training value; current-label-dependent design is not.

This retains the normalization and equal-environment constraints discarded by K2394's enlarged arbitrary-index ratio polytope. If the training interval allows r in [0,infinity], then C_D=max(S_1/n_1,S_0/n_0). Consequently a unique maximum in a group of n_c members can still receive e=n_c, though no cross-group borrowing is justified. An unbounded shift interval does not prohibit all inference. Without additional assumptions, finite counts cannot establish a finite uniform odds bound with certainty: arbitrarily extreme interior p,q give every finite count pattern positive probability. The learned bounds are confidence statements with an explicit failure budget.

## Full anytime error accounting

For each fixed training value in Good, E_t(theta*)=product_(j<=t) f_j(theta*) is a nonnegative supermartingale starting at one. The stopped first-crossing argument gives conditional probability at most eta of ever crossing 1/eta. Because inf_theta E_t(theta)<=E_t(theta*), the same bound applies to globally certified shared-graph rejection. The infimum need not be a supermartingale. A finite theta grid cannot certify its lower bound.

On bad training, use only the probability bound one. If b=Pr(not Good)<=delta, then

    Pr(ever reject) <= (1-b)eta+b <= (1-delta)eta+delta.      (7)

For desired total alpha>delta choose

    eta=(alpha-delta)/(1-delta),   threshold=1/eta.          (8)

The learned E_t is **not** thereby an unconditional e-process. Equation (7) is the valid event guarantee. For example an abstract procedure with good-training crossing probability eta and bad-training crossing probability one attains eta(1-delta)+delta; the good-event theorem alone cannot omit delta. Likewise taking E=1 on good training and E=1/delta on bad training gives mean 2-delta>1 despite perfect good-event conditional validity. These controls concern the logical inference, not an assertion that the present interval construction attains its coverage upper bound.

A single training confidence event is charged once for this prespecified shared-graph test over all looks. It does not authorize arbitrarily many separately reported graph-family rejections; multiplicity across distinct tests needs its own construction. Fresh batches or another conditional-validity proof remain necessary.

## Finite-training and continuous-graph certificate

Take alpha=1/20, delta=1/100, n_P=n_Q=100, G={j/12:0<=j<=12}, and synthetic counts K_P=K_Q=50. Exact binomial sums give both intervals [1/3,2/3], hence r in [1/4,4]. The total-test threshold is 99/4. This is an example input to the algorithm, not collected training data.

Each testing pool has ordered environments (1,1,0), with the first member designated science only when evaluating its already-symmetric assignment. If a unique maximum is in environment1, its b indicator has normalizer 4/9 and e=9/4. If it is in environment0, its normalizer is 2/3 and e=3/2. The calculation treats each possible science label consistently. At lambda=3/4, the environment1 maximum gets f=31/16 and every member without the maximum gets f=1/4. Using only the enlarged global Gamma4 bound would instead cap that maximum's e at 3/2; learning and retaining the shared environment is strictly more informative.

Use theta in [-1,1], R_theta=(-theta,1), both calibration vectors (0,1/2), science z_1=(1,1), z_2=(1,-1), and z_3=...=z_8=(0,4). Squared residual scores give maximum-bonus failures [1/2,1] at look1 and [-1,-1/2] at look2, including their tie endpoints. They are disjoint; all remaining six looks succeed for every theta. Therefore

    inf_theta E_8(theta)=(1/4)(31/16)^7 > 99/4,              (9)
    product_(j<=8) inf_theta f_j(theta)=(1/4)^2(31/16)^6
                                               < 99/4.

The endpoint values attain the first minimum. Seven looks of this specified pattern give (1/4)(31/16)^6<99/4. Thus eight looks certify rejection for this sequence while separate-look profiling fails. This is not an optimal exposure count or a probability-one alternative-power result. Cost is 48 paired-protocol exposures plus 200 independent environment-label training observations; no equivalence between those two resource units is assumed.

Compatibility: choose p=q=1/2 and, at both environments, the centrally symmetric finite exposure-error support {0,+/-(1,-3),+/-(1,-5),+/-(0,1)}, assigning positive mass to every point. With s=(0,4), equal science errors (1,-3), then (1,-5), then zero produce the stated science vectors; calibration errors (0,1) and zero produce (0,1/2). All training counts and environment arrangements have positive probability under independent sampling. This proves model compatibility and positive support probability only.

## Contrary constructions and remaining physical interface

**Plug-in weights fail even after independent training.** With p=1/2,q=3/4, training of size2 from each law can return one environment1 count each, so plug-in p=q=1/2 assigns r=1. In a (1,1,0) pool with one named environment1 maximum, its actual conditional science-index probability is 3/7, not 1/3. A plug-in normalized indicator has null conditional expectation 9/7>1. Independence permits a confidence argument; it does not turn an estimator into the true law.

**Odds are not probability ratios.** Intervals p,q in [1/3,2/3] allow p=1/3,q=2/3 and r=4. Using r<=2 would set that same indicator normalizer to 2/5 instead of 4/9; its true mean after normalization is 10/9>1.

**No distinguished-label fitting.** In an all-one-environment pool of size3, selecting b_i=1 exactly at the already observed science label and normalizing as if the assignment had been frozen produces e=3 always. The permutation-equivariance and no-current-label premise are essential.

**Unseen environments and drift.** A training count zero gives lower endpoint zero; a count n gives upper endpoint one. Infinite odds endpoints must be retained, rather than silently clipped. Changing future p,q after training can move the true index law outside (4) even when the original intervals covered perfectly. Training counts do not authenticate a stable environment definition, conditional symmetry, identical signal/windows, bias removal or held-out selection. These are distinct physical inputs.

## Specialist checks, evidence and useful successors

Preflight lenses were exact finite-sample statistics, repeated-exposure observational design and adversarial conditional inference. Postflight challenges target grid inversion at endpoints, ratio sharpness with shared labels, calibration-event error mixing, graph tie boundaries and the distinction between synthetic support and measured data. The companion probe exhausts all training counts for several finite sample sizes, checks rational true parameters and monotonic endpoint bounds, replays the exact training example and both continuous-graph cells/endpoints, and constructs the counterexamples above. Universal claims rest on the proofs; finite controls are not a source-mutation harness, external review or proof-assistant certification.

The useful next physical step is a real fixed-window, same-signal repeated-exposure specification with independent environmental training records and a defensible conditional matching law. Useful mathematical successors are a multienvironment confidence region retaining shared normalization, or a separately proved way to reuse calibration under conditional validity. They should be driven by an actual instrument or benchmark; this result supplies neither empirical data nor a native GU prediction.

### Classical reference

The exact binomial-tail inversion is classical: C. J. Clopper and E. S. Pearson, “The Use of Confidence or Fiducial Limits Illustrated in the Case of the Binomial,” *Biometrika* 26 (1934), 404–413, [primary paper](https://www.barestatistics.nl/uploads/1/1/7/9/11797954/clopper__pearson_1934.pdf). Equations (1)–(2) give the full outward-grid and simultaneous-coverage proof used here; the citation is attribution, not a substitute for it.
