---
title: "K2394 Robust nonbinary evidence, recovery and sharp paired-exposure limits"
status: active_research
doc_type: exploration
created: "2026-10-31"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematics; no native GU or measured physical verdict
scripts:
  - tests/channel-swings/k2394_robust_pool_sequential_evidence_probe.py
---

# K2394 Robust nonbinary evidence, recovery and sharp paired-exposure limits

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
result: K2394
carrier: finite conditional noise pools and sequential paired-exposure experiments LAYER=toy CHIRALITY=N/A
pairing: nonnegative residual scores and conditional probability expectation ON=declared_carrier
real_structure: real errors with K2391 conditional central symmetry and observable shift
grading: unordered pool, possible science index, fixed shared graph and fresh looks
action_owner: repository-construction -- K2376 conditional windowed observation graph
target: robust e-factor construction, shared-parameter recovery and protocol resource limits MAP-TYPE=evaluation
```

## Scientific result and scope

K2391's binary factors permanently lose all evidence at a failed look. This successor characterizes all nonnegative factors that are safe conditional on each unordered noise pool under its bounded weight-ratio model. It constructs positive factors that recover from failed looks, derives the log-optimal factor for a supplied conditional alternative, and broadens the 26-exposure lower bound beyond binary bets within the explicitly enlarged finite ambiguity class. Strictly positive factors cost at least 28 exposures for guaranteed separated-path rejection in this same protocol. The nine-look continuous-parameter fixture certifies rejection where binary factors and separately profiling each look fail.

Layer 0: the observation graph is the conditional metric f(R) graph, not a derivation of Weinstein's connection displacement. These are conditional statistics, not a new native GU mechanism, measured exclusion or physical noise estimate. SC-COS-50/51/54 retain ASSERTS; no ledger, hypothesis, canon or LT-GR2e grade changes. No seven-axis substrate candidate is claimed.

## Exact conditional-pool evidence cone

Retain K2391's model conditional on full past and any independent training: one science error has law Q(dc)K_c(depsilon), N-1 independent calibration errors have P(dc)K_c(dxi), Q<<P, and w=dQ/dP has supplied pooled max/min ratio at most Gamma>=1. Require positive weights. At the fixed true graph theta*, the science residual equals the science-error residual. Conditional on the unordered pooled pairs, the science index I has probability p_i=w_i/sum_j w_j. Therefore p belongs to the convex compact polytope

    P_Gamma={p: sum_i p_i=1, p_i>=0, p_i<=Gamma p_j for every i,j}.

All its coordinates are positive. We deliberately require robustness to EVERY p in this finite polytope. This is an enlarged ambiguity class: a known weight function, repeated environments requiring equal weights, or additional normalization/parametric information may restrict the physically admissible p further. Necessity and resource optimality below are for the enlarged class, not all tests valid under every such more informative model. A factor assignment e=(e_1,...,e_N)>=0 is safe for this enlarged conditional-index class exactly when

    sup_(p in P_Gamma) sum_i p_i e_i <= 1.                 (1)

The assignment may use the entire unordered pool but MUST be permutation-equivariant and must not use which member is the science member. It can rank pooled scores, use environments and independent prelabel randomness; fitting a rule that singles out the observed science label violates the theorem. At candidate theta, form all residual scores and apply the same symmetric rule. The proof only needs the fixed theta* to have the null pool law. Ties must be handled symmetrically; the unique-maximum rule below sets its indicator to zero for every member of a tied maximum.

For b_i>=0, sort b_(1)>=...>=b_(N). Define

    C_Gamma(b)=max_(0<=k<=N)
        [Gamma sum_(i<=k)b_(i)+sum_(i>k)b_(i)]/[Gamma k+N-k]. (2)

If C>0, e_i=b_i/C satisfies (1), with equality for a permitted p. If b is zero take e=0. To prove (2), write p=w/sum w with 1<=w_i<=Gamma. A linear-fractional function of any single weight is monotone or constant, so its maximum occurs at a box corner. Among corners with k large weights, putting them on the k largest b maximizes the numerator without changing the denominator. Conversely every such corner is permitted in the enlarged finite ambiguity class. Equation (2) is a sharp normalizer for a given assignment, not an optimality claim about every measurement design.

A particularly transparent positive factor is

    e_i=(1-lambda)+lambda*(N-1+Gamma)/Gamma
                        *1{i is the unique largest score}, 0<=lambda<1. (3)

At most one member receives the bonus, and its conditional probability is at most Gamma/(N-1+Gamma), so (3) is safe. It is strictly positive and can recover from a nonextreme look. At lambda=1 it reduces to the separated-rank binary factor.

## Log-optimality for a supplied conditional alternative

Suppose a strictly positive conditional alternative index distribution q is supplied in the same pool coordinates, independently of the actual science label. It is a design assumption, not estimated evidence for a physical noise law. Let p* minimize KL(q||p)=sum_i q_i log(q_i/p_i) over P_Gamma. Existence follows from compactness and positivity. Then

    e*_i=q_i/p*_i,  max_(e satisfying (1)) sum_i q_i log e_i
                                  = min_(p in P_Gamma) KL(q||p). (4)

Indeed, the first derivative of KL at p* toward any p gives sum_i p_i q_i/p*_i<=1, so e* is feasible. For any other feasible e, Jensen gives

    sum_i q_i log(e_i/e*_i) <= log(sum_i p*_i e_i) <= 0.

This proves (4), including zero candidate factors by the extended log convention. It is the elementary finite convex case of the known reverse-information-projection/e-variable relationship; see Larsson, Ramdas and Ruf, [The numeraire e-variable and reverse information projection](https://arxiv.org/abs/2402.18810). No novelty for that general relationship is claimed.

For N3,Gamma2,q=(3/4,1/8,1/8), p*=(1/2,1/4,1/4) and e*=(3/2,1/2,1/2). Feasibility follows from p_1<=1/2 and p·e*=1/2+p_1<=1; the displayed identity q_i=p*_i e*_i and Jensen certify exact optimality. If q is itself in P_Gamma, the optimum is zero and e*=1: this supplies a contrary case to any claim that positive betting always creates information.

## Sequential validity and continuous shared-graph recovery

Require every fresh batch to satisfy the model conditional on full past. Keep the fixed true parameter theta* in the prespecified Theta and assume the profiled crossing events are measurable. For a fixed theta*, conditional expected factor is at most1; E_t(theta*)=product_(j<=t)e_j(theta*) is a nonnegative supermartingale. The first-crossing argument gives

    Pr(exists t: inf_theta E_t(theta)>=1/alpha)<=alpha.     (5)

As in K2391, the infimum itself need not be a supermartingale. It must be globally certified, and theta must denote the same fixed graph across looks. A grid minimum gives the wrong bound for certification. Adaptive bets and batch sizes may use the past; marginal validity or naive reuse of calibration data does not provide the conditional premise.

Exact observed-data fixture: theta in[-1,1], R_theta=(-theta,1), N3,Gamma2,lambda3/4,alpha1/20. Both calibration vectors at every look equal (0,1/2). The science vectors are z_1=(1,1), z_2=(1,-1) and z_3=...=z_9=(0,4). Each look costs three exposure pairs, so the displayed nine-look certificate uses54 exposures. Use squared residual scores. At look1 the unique-high-score failure set is [1/2,1]; at look2 it is [-1,-1/2]. These disjoint closed sets include ties. The remaining seven looks succeed for every theta. Consequently each theta has at most one factor1/4 and otherwise factors7/4, with equality at either endpoint:

    inf_theta E_9(theta)=(1/4)(7/4)^8
                       =5764801/262144 >20.                (6)

The binary choice lambda1 instead has inf_theta E_9=0, because theta1 fails look1 permanently. Profiling each look before multiplication yields only (1/4)^2(7/4)^7=823543/262144<20. Thus retaining one shared graph and allowing positive factors each matter.

This displayed sequence can occur with one fixed signal s=(0,4), P=Q, and an identical finite centrally symmetric exposure law supported on 0, +/-(1,-3), +/-(1,-5), +/-(0,1). Give every point positive mass. Science pairs with both errors (1,-3), both (1,-5), and both0 give the three displayed science-vector types. Calibration pairs with errors (0,1) and0 give (0,1/2). Independence makes the finite sequence have positive probability. The actual ratio is1 and lies within the conservative Gamma2 bound. This verifies compatibility of the observed fixture with the matching instrument; it does NOT establish probability-one power, typical behavior, measured support or a nine-look optimality claim.

## Sharp exposure limits beyond binary bets

Fix K2391's protocol: a fresh batch uses m>=1 calibration pairs and one science pair, costing 2(m+1) exposures, and Gamma2. Restrict to products of factors satisfying (1) conditional on each pool, including arbitrary nonnegative rank/score assignments and predictable choices, but requiring the full enlarged P_Gamma ambiguity set even if observed environments might justify a smaller set. On a globally separated outcome, feasibility evaluated at the index distribution admitted by that enlarged class with science weight Gamma and every other weight1 forces

    e_science <= (m+Gamma)/Gamma.                          (7)

All other terms are nonnegative. Equality requires every other assignment to be zero. This is a pointwise bound independent of bet shape; it covers predictable random choice of conditionally valid assignments. It does not cover arbitrary randomized payouts constrained only after averaging their randomness, arbitrary sequential tests, data reuse, different exposure matching, or stronger known weight information.

Write j=m+1 for pair cost. Under perfect separation the maximal product at total pair cost c obeys B(0)=1, B(1)=0 and

    B(c)=max_(2<=j<=c) B(c-j)*(j+1)/2.

The recurrence exhausts every partition; adaptive choices still produce one such realized partition. Exact rational computation shows max_(c<13)B(c)<20 and B(13)=20, attained at costs(3,3,3,4). Thus 26 exposures remain necessary and sufficient for guaranteed separated-path rejection across this expanded conditional-pool e-factor class.

If every assignment is strictly positive, (7) is strict. Every partition with cost<=13 therefore gives product<20, so at least28 exposures are needed. At costs(3,3,4,4), use (3) with lambda19/20; its separated factors are39/20,39/20,97/40,97/40. Their product14311089/640000>20, proving28 attainable. This is the exact price of strict positivity for guaranteed separation in this protocol, not a universal sample-complexity result. It does not say28 is needed on arbitrary nonseparated observations or under exact known equal weights.

## Conditional mismatch and hostile controls

If the actual full-batch law is within supplied conditional TV distance delta of the ideal law, and a factor lies in[a,b], then its conditional expectation is at most1+delta(b-a). Divide by this quantity to preserve (5). The bound uses the oscillation, not merely the upper bound, and is sharp for a saturated two-event ideal law when delta probability moves from the lower to upper value. For (3) with N3,Gamma2,lambda3/4 the range is[1/4,7/4], hence denominator1+3delta/2. At delta1/200 the observed certificate (6) survives nine corrections; at delta1/100 it does not. These are exact observed-sequence sensitivity controls, not alternative power guarantees.

Unsafe label selection: after seeing science index I, assign b_I=N and all other b zero. Normalizing as though b were a frozen symmetric assignment yields e_I=(N-1+Gamma)/Gamma>1 always, invalidating expectation. Unsafe nominal normalization: b=(3,1,1),N3,Gamma2 has nominal average5/3 but worst mean2; dividing by5/3 gives null mean6/5. Unsafe reuse: repeat one Bernoulli(1/2) success and the factor7/4 on success,1/4 otherwise; by six looks the path crosses20 with probability1/2, exceeding1/20. Fresh conditional validity was essential.

## Claim ceiling and verification

The companion exact-rational probe checks sorted normalizers against all small box corners, feasibility and sharpness fixtures, the continuous graph cells and endpoints, all finite pair-cost partitions through14 via the dynamic program, positive-bet resource controls, TV sensitivity and hostile controls. Universal statements rest on the proofs above; finite enumeration is an implementation/counterexample check. The recovery fixture is an observed synthetic sequence with positive support probability, not measured data or a uniform alternative-power theorem. The five finite counterexample/assumption controls are not a source-mutation harness. Internal review is not external-expert or proof-assistant certification.
