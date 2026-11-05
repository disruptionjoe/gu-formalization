---
title: "K2573 Every finite expected-trial budget has a finite attaining mixture"
status: active_research
doc_type: exploration
created: "2026-11-05"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: all positive leakage multipliers and joint leakage-resource budgets; no computed intermediate optimizer or sharp unpriced transition
scripts:
  - tests/channel-swings/k2573_universal_resource_attainment_probe.py
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
result: K2573
carrier: original adaptive fresh fair test/use stopping histories and resource-preserving finite completed schedules LAYER=toy CHIRALITY=N/A
pairing: unconditional success, original leakage, and expected positive-score trials ON=declared_carrier
real_structure: real coefficients and positive auxiliary norms
grading: source-selected physics and supplied mathematical preparations remain distinct
action_owner: repository-construction -- stated conditional model
target: finite resource compactness and attained multi-budget tradeoffs MAP-TYPE=evaluation
```

# Resource compactness removes the multiplier restriction

## Result and scope

For every lambda>0, 0<S<=1/2 and finite expected-positive-trial ceiling M>=0, the original adaptive stopping value

    F_lambda(M)=sup{p-lambda C : R<=M}

is attained by an initial mixture of at most TWO finite completed repeated-action schedules, allowing abort. K2571 proved this in 0<lambda<=98/51 by first establishing a strictly positive supporting price. The present result removes that multiplier restriction by proving constrained compactness first. It does not settle whether the unrestricted supremum is attained in the intermediate multiplier range.

Released follow-through also proves that the maximum success probability under BOTH C<=B and R<=M, for finite B,M>=0, is attained by at most THREE such schedules. An explicit uniform finite-stage truncation error supplies a convergent finite optimization. Expected trials are counted under the original law, including failures; a finite schedule still has an unbounded geometric number of test passes. No pathwise trial cap or physical apparatus is inferred.

This is GU-independent probability/optimization. The current source polarities, ledger0.263, canon, physical quotient and native action/observation debts do not change. In particular SC-META-53 remains UNCERTAIN. Positive-price attainment, K2571's exact one-stage region and nonlinear budget segment, and K2565's unpriced value bracket remain reusable results, not repeated calculations or new claims here.

## 1. The exact finite schedules and the bridge being used

For n positive stages, sum b_i=S and 0<=a_i<=b_i, put

    P_i=product_(j<=i)(1+a_j)^(-1),
    p=P_n, C=2 sum P_i w(a_i,b_i), R=2 sum P_i,
    w(a,b)=log(1+(b-a)^2/[2(a+b)(2-a-b)]).

The continuous extension at a=b=0 is0. Zero-score padding is omitted from actual execution and incurs zero resource. Abort has (p,C,R)=(0,0,0). From K2569's original-policy reduction, any policy with finite R is dominated by an initial mixture of finite normalized completed schedules and abort: p weakly increases, C and R weakly decrease. The reduction retains nonstationary test-pass actions and post-use labels before clipping. The stronger three-coordinate dominance, rather than only equality of the unpriced supremum, is required for the joint-budget result below.

On the compact padded simplex D_n, p and C are continuous, while

    R=2 sum P_i 1_(b_i>0)

is lower semicontinuous. A vanishing positive stage leaves a nonzero limiting resource charge; its zero limit is deleted. K2571 already checked this direction. Also

    P_i>=e^-S, R>=2e^-S n                         (1)

for exactly n POSITIVE stages, and 0<=p<=1. Since a+b<=1 and (b-a)^2<=b(a+b), w<=b/2, so 0<=C<=sum P_i b_i<=S. This coarse uniform bound suffices here; it is not a best leakage estimate.

## 2. Tightness and attainment without a positive price

Take a sequence of feasible schedule mixtures whose J=p-lambda C tends to F_lambda(M). Represent each component with its ACTUAL positive stage count n before padding. Let its mixture measure on D_n have mass pi_n and include an isolated abort component n=0. Equation(1) gives uniformly

    sum_(n>N) pi_n <= M e^S/[2(N+1)].             (2)

For each fixed n, D_n is compact; sequential compactness of finite measures gives a weakly convergent subsequence. A diagonal subsequence works for every integer n and for abort. The uniform tag-tail bound (2) makes the limiting masses sum to1; no probability disappears at an infinite stage count. This is tightness of a distribution of finite schedules, not compactness of a single infinite control path.

Within D_n, continuity preserves integrals of p,C. Their uniform bounds and (2) control the remaining tag tail, so the total integrals of p,C converge to those of the limiting mixture. Lower semicontinuity of the nonnegative R gives for each finite tag head, and then by increasing the head,

    integral R dmu <= liminf integral R dmu_j <= M.

Zero stages are deleted in each limiting component; they preserve p,C and can only lower R. Thus the limit is an admissible initial randomization over finite original schedules, has R<=M, and attains F_lambda(M). M=0 gives abort by p<=R/2; the same proof also works for lambda=0, though later strict-price statements need their stated assumptions.

The key contrary construction is a mixture with a tiny chance of a very long schedule. No fixed deterministic stage cap contains every such feasible policy. Bound(2), rather than a false pointwise cap, is what controls its probability. Likewise lower semicontinuity, not continuity of R, is essential. There is no appeal to unproved finite dimensionality of the original adaptive class.

## 3. Why two finite schedules suffice, including a zero-price plateau

F is finite, nondecreasing and concave under initial randomization, with F(0)=0 and initial segment M/2 from K2571. For M>0 choose a supporting slope kappa>=0. If kappa>0, K2571's price-attainment and compact-resource-range proof applies for EVERY lambda>0. The constrained optimizer must maximize J-kappa R and use R=M. The endpoint-resource mixture of at most two price maximizers therefore attains F(M), with finite stage caps as in K2571. Its strict-price machinery did not itself require lambda<=98/51; that restriction was used only to establish positive support at every finite M.

If a supporting slope is0, monotonicity and concavity imply F(M)=V:=sup_original J. The attaining measure from section2 has J=V for mu-almost every component, since J<=V and the nonnegative gap V-J has integral zero. In particular at least one finite schedule attains V. Among all such finite schedules a minimum resource R_* exists: choose any one with resource R0, minimize over those with R<=R0, and use (1) to bound their positive stage count. On the finite union of compact padded D_n, J=V is closed and R is lower semicontinuous. Deleting a zero stage preserves J and lowers R. Thus the minimum is attained by a finite schedule. Every V-attaining mixture has resource at least R_*, so R_*<=M; this single schedule solves the constrained problem.

Consequently a finite-budget plateau occurs iff an unpriced finite optimizer exists; its exact onset is R_*. Before such an onset every supporting slope is positive and the budget is exhausted by the two-schedule construction. If no finite unpriced optimizer exists, F(M)<V at every finite M and every support is positive. This extends the structural dichotomy to the unclassified lambda interval WITHOUT declaring which side of it occurs there. K2567/K2569 settle nonattainment for 0<lambda<=98/51; K2559 supplies an attained one-stage regime at lambda>=4/sqrt3.

## 4. Execute simultaneous leakage and useful-trial budgets

For finite B,M>=0 define

    G(B,M)=sup{p:C<=B, R<=M}.

The same tightness proof uses (2); p,C continuity makes C<=B survive the limit, while R lower semicontinuity keeps its constraint. Thus G is attained by a measure on finite schedules and abort. This is the original leakage C, not a Lagrange-multiplier surrogate, and the two budgets concern the SAME policy.

We now reduce the attaining measure to finite support without assuming a positive price. Its moment vector (C,R,p) is integrable and is a barycenter of a full-measure set of actual finite-schedule moment values. Here support means that set, not only its topological closure. An elementary finite-dimensional barycenter lemma puts this vector in the CONVEX HULL of that support, not merely its closure. To see the distinction, take the affine hull of the support. If the mean is not in the relative interior of its closed convex hull, a supporting linear functional is nonnegative about the mean and has expectation0, hence vanishes almost surely; restrict to that hyperplane and induct on dimension. In the remaining affine space the mean lies in the relative interior, which is contained in the convex hull itself. Caratheodory then represents the same (C,R,p) by at most four finite schedules/abort.

For these at most four fixed components solve the finite linear program in their initial probabilities: maximize p with normalization, C<=B and R<=M. It has an optimal vertex with at most three positive weights (normalization plus at most two active budget equations). It cannot improve beyond the original optimum G, so this vertex still attains G. Therefore at most THREE finite schedules suffice. Neither both budgets being active nor positive supporting prices are required. This argument also covers B=0 or M=0 and redundant constraints. It does not supply the component controls numerically or turn two independent fitted policies into one jointly feasible policy.

The same finite-support proof gives a second route to the two-schedule F result: preserve (R,J), use at most three components, and optimize their weights under one inequality. Section3 retains the price/plateau interpretation, which the support-count argument alone does not identify.

## 5. Execute a finite-stage approximation certificate

Let F_N and G_N restrict all mixture components to at most N positive stages. The finite collection of padded simplexes is compact; the preceding arguments imply their optima are attained by at most two or three components, respectively. Replace all n>N components of an optimal unrestricted-budget mixture by abort. Both C and R decrease. The loss of p is at most its discarded mass; the loss of J is also at most that mass because J<=1 (discarding negative J improves it). Thus for N>=1,

    0<=F_lambda(M)-F_N(M)<=M e^S/[2(N+1)],
    0<=G(B,M)-G_N(B,M)<=M e^S/[2(N+1)].           (3)

These bounds hold for every lambda>0 and finite B,M. They are sufficient uniform errors, not sharp asymptotic rates, a fine control-grid certificate, or practical optimizer-complexity claims. Unlike a cap derived from a positive supporting price, (3) is available directly from the specified resource budget even when the needed price is unknown or zero. Finite dimensional global optimization of the retained controls is still needed; an arbitrary numerical local optimum is not F_N or G_N.

For S=1/2, use the rational upper bound e^(1/2)<5/3. At M=2 and error1/1000, N=1666 suffices because M(5/3)/(2(N+1))=5/5001<1/1000. The probe proves the exponential inequality by a Taylor sum plus a geometric tail, and verifies this exact rational consumer. This is an executed choice of a sufficient optimization size, not a computation of the optimum and not a recommendation to brute-force1666 stages.

## 6. Execute an exact joint-budget point and preserve limits

Take S=1/2 and arbitrary B>=0. For 0<=M<=4/3, K2571's free full-score stage (a,b)=(1/2,1/2) has p=2/3,C=0,R=4/3. Initially execute it with probability3M/4 and otherwise abort. It yields p=M/2,C=0,R=M. Every original policy has p<=R/2 by the fair-use identity, so

    G(B,M)=M/2, 0<=M<=4/3, B>=0.                (4)

At B=0 the entire remaining frontier is also explicit. A zero expected leakage policy has a>=b almost surely on every active action; the resource-preserving bridge leaves only zero-leakage stages a_i=b_i. For a completed schedule product(1+b_i)>=1+sum b_i=1+S, so p<=1/(1+S). Equality is attained by the one-stage free schedule. Therefore for ALL finite M and B=0,

    G(0,M)=min(M/2,1/(1+S)).                      (5)

The same formula follows for arbitrary S in(0,1/2]; its threshold is2/(1+S). The minimum combines the independent universal bounds p<=R/2 and zero-leakage success<=1/(1+S), and a single free schedule/abort mixture achieves each segment. This is a nontrivial exactly solved joint-budget boundary; it does not solve B>0 above that resource threshold or the unpriced intermediate transition. The probe checks actual law accounting for two free stages to reject the false assertion that zero leakage removes all survival loss.

## Evidence and next condition

Universal compactness and finite-support arguments are written proofs requiring independent review. Exact finite schedule calculations, lower-semicontinuity counterexamples, tail-bound arithmetic and original-law joint consumers provide supporting evidence; saved reports/hashes are provenance, not theorem proofs. No numerical sampling is called a continuum certificate. The strongest remaining numerical question is a supported optimum outside K2571's sufficient one-stage price region. A useful follow-up can certify a low-dimensional global optimizer or exploit schedule structure to make (3) computationally useful. The existence and support theorems do not supply such structure, a sharp transition, or a resource-error lower rate.

[K2569 resource-preserving original-law bridge](k2569-stopping-maximizing-sequences-2026-11-05.md), [K2571 price and budget theorem](k2571-stopping-resource-price-2026-11-05.md), [probe](../../tests/channel-swings/k2573_universal_resource_attainment_probe.py), [report](../../lab/process/k2573-universal-resource-attainment.json).
