---
title: "K2571 A positive trial price restores finite attainment"
status: active_research
doc_type: exploration
created: "2026-11-05"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: finite attainment with a positive expected-trial price; exact finite-resource mixture characterization in the certified nonattainment range, not a computed unpriced intermediate optimum
scripts:
  - tests/channel-swings/k2571_stopping_resource_price_probe.py
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
result: K2571
carrier: original predictable fresh fair test/use histories with private randomization and finite-hit success LAYER=toy CHIRALITY=N/A
pairing: unconditional success minus original leakage and expected positive-score trial charges ON=declared_carrier
real_structure: real probabilities and logarithmic costs; compact finite-stage controls
grading: positive trials, positive stages, zero-length padding and initial abort remain distinct
action_owner: repository-construction -- supplied fair stopping probability law
target: trial-price attainment and finite-resource constrained value MAP-TYPE=evaluation
```

# A finite resource ceiling has an attaining policy

## Result and preflight choice

Let J=p-lambda C for the original stopping law, and let R=E N_+ count active trials whose chosen score increment b is positive, including failed and passed tests. Fix 0<S<=1/2 and lambda>0. For EVERY positive price kappa, the maximum of J-kappa R over the original adaptive class is attained by a deterministic finite completed repeated-action schedule or by immediate abort. An explicit stage cap makes this a finite-dimensional optimization. The actual number of experimental trials remains geometrically distributed and need not be bounded pathwise.

There is a further exact constrained result in the certified nonattainment range 0<lambda<=98/51. For EVERY finite resource ceiling M>=0, the maximum of J subject to R<=M is attained by an initial mixture of at most two finite completed schedules, allowing abort as a component. For M>0 the mixture uses exactly M expected positive trials and is selected by a strictly positive supporting resource price. The unrestricted value remains unattained. Thus pricing useful trials or fixing their finite expected budget changes the attainment question without replacing the original leakage law or calling an infinite-score limit a hit.

K2561 already proves a sharp expected-resource order in its high-budget phase. Repeating that argument is not the present contribution. K2569 supplies the resource-preserving reduction and divergence theorem but no finite-resource optimizer. K2485's two-schedule result concerns a LEAKAGE budget and only approximation; it does not establish attainment at a positive-trial budget. The present compactness argument closes that distinct question. Supporting-line and maximum-of-affine-function reasoning are standard convex analysis, applied below with the zero-stage discontinuity checked explicitly; no novelty claim is made.

The useful consumer is an attained finite optimization for a prescribed cost of useful trials, followed by exact interpolation to a resource ceiling. A large uniform hybrid mesh is unnecessary for this existence and stage-bound question. It does not compute the intermediate optimum or select a physical apparatus price. This remains GU-independent mathematics: SC-META-53 remains UNCERTAIN; source polarity, ledger0.263 LT-SM8/LT-GR6b, canon and physical-domain debts are unchanged.

## 1. Original resource accounting and reduction

The original action is a,b in[0,1]. A fresh fair use adds b; a test fails with probability a and otherwise passes. Every active trial pays

    w(a,b)=log(1+(b-a)^2/[2(a+b)(2-a-b)]) for a<b,
    w(a,b)=0 for a>=b.

A repeated positive stage has use probability 1/(1+a), expected positive trials 2/(1+a), and expected leakage 2w/(1+a). For a normalized completed schedule with positive b_i, sum b_i=S and 0<=a_i<=b_i, put

    P_i=product_(j<=i)(1+a_j)^(-1),
    p=P_n, C=2 sum_i P_i w(a_i,b_i), R=2 sum_i P_i.
    J_kappa=P_n-2 sum_i P_i[lambda w(a_i,b_i)+kappa].       (1)

These are original unconditional expectations, including failures. The per-stage affine continuation map is

    x -> [x-2lambda w(a,b)-2kappa]/(1+a), b>0.             (2)

A zero-length padding stage is the identity and incurs NO useful-trial charge. It is omitted from the actual policy. Charging only one kappa in(2), counting 2n unweighted trials, or conditioning leakage on success gives a different objective.

K2569 sections2--3 reduce every original policy with finite R to a mixture of finite normalized completed schedules and initial abort, with J weakly increased and R weakly decreased. That proof preserves nonstationary test-pass actions and post-use continuation labels before clipping and removing incomplete paths. It therefore also increases J-kappa R. A policy with infinite R has penalized value minus infinity when kappa>0; infinite leakage has the same conclusion for lambda>0. The mixture's penalized value is at most its largest component supremum. No deterministic-policy reduction is assumed without this bridge.

## 2. Positive price gives a finite stage cap and an actual maximum

Since sum a_i<=S and log(1+a)<=a,

    P_i>=exp(-S), R>=2 exp(-S)n, J<=1.

Therefore a schedule with n positive stages has

    J_kappa<=1-2kappa exp(-S)n.                           (3)

Abort has value0. All schedules with n>exp(S)/(2kappa) are strictly inferior to abort. Retain n<=floor(exp(S)/(2kappa)), as well as abort; if the cap is zero there is no positive candidate.

For a fixed cap N, use the compact padded simplex sum_(i=1..N)b_i=S, 0<=a_i<=b_i. The extension of w at(0,0) is continuous: its logarithm increment is at most b/[2(2-b)]. Hence J is continuous on this simplex, with zero stages deleted. The RESOURCE IS NOT CONTINUOUS: a positive stage approaching zero still consumes about two conditional trials, whereas an exactly zero stage is omitted. Precisely,

    R=2 sum_i P_i 1_(b_i>0)

is lower semicontinuous because P_i is positive continuous and each indicator of b_i>0 is lower semicontinuous on b_i>=0. Thus J-kappa R is upper semicontinuous and attains a maximum on the compact simplex. Taking also abort proves attainment of

    Q(kappa)=max_original [J-kappa R], kappa>0.            (4)

This compactness is not an assertion that a zero-stage charge is continuous. Deleting a vanishing stage increases the limiting penalized objective, which is the direction needed for upper semicontinuity.

For 0<kappa<1/2, the free full-score stage(a,b)=(S,S) gives

    L_kappa=(1-2kappa)/(1+S)>0.

Comparing(3) with this lower bound improves the cap to

    n<=floor(exp(S)(S+2kappa)/[2kappa(1+S)]).              (5)

This remains only a sufficient search cap, not a formula for the optimal stage count. For S=1/2 and kappa=1/10, exp(1/2)<5/3 implies the right-hand quantity before flooring is less than35/9<4. Hence at most THREE positive stages suffice for EVERY lambda>0 at this price. No numerical optimizer or derivative test is needed for that conclusion.

## 3. The exact small-resource segment and abort price

Each successful policy has at least one positive-score USE. Predictability and the fresh fair bit give E(number of positive-score uses)=R/2 by Tonelli. Consequently

    p<=R/2, J<=R/2, J_kappa<=(1/2-kappa)R.                (6)

For kappa>=1/2, Q(kappa)=0. At kappa>1/2 only policies with R=0 can attain this value; idle conventions do not give a positive-score experiment. At kappa=1/2, both abort and the free full-score stage attain0.

Define F_lambda(M)=sup{J:R<=M}. The free stage has

    R_0=2/(1+S), J_0=1/(1+S), C_0=0.

For 0<=M<=R_0, execute it initially with probability M/R_0 and otherwise abort. Its resource is exactly M and J=M/2. Together with(6),

    F_lambda(M)=M/2, 0<=M<=2/(1+S), for EVERY lambda>0.   (7)

This is an exact original-policy frontier segment. At S=1/2,M=1, an initial3/4 chance of executing(a,b)=(1/2,1/2) gives p=1/2, C=0 and R=1. Its expected resource is not a limit or a rounded budget. M=0 is attained by abort. The statement does not claim that all optimizers in the segment have this representation.

## 4. Finite ceilings remain strictly below the unrestricted value

For the rest of the finite-ceiling theorem assume 0<lambda<=98/51. Write V=V_lambda(S), the unrestricted original dual supremum. K2569 proves compact maxima D_n over schedules with at most n positive stages and strictly positive g_n=D_(n+1)-D_n, with D_0=0. Its resource bridge gives, for every original policy with gap eta=V-J,

    R>=A_n(1-eta/g_n)_+, A_n=2exp(-S)(n+1).               (8)

For any fixed finite M choose n with A_n>M. Whether eta<g_n or eta>=g_n, R<=M and(8) imply

    J<=V-g_n(1-M/A_n)<V.

Thus F_lambda(M)<V for EVERY finite M, uniformly over all policies at that resource ceiling. This is stronger than the nonattainment of V by an individual policy. Initial mixtures cannot evade it. The bound uses a mathematically positive finite-stage gap, not a newly computed numerical gap or a claimed convergence rate.

F is nondecreasing, concave under initial randomization, and finite. Moreover F(0)=0 by(6), and F(M) tends to V as M tends to infinity, because K2569's finite schedules approach V and each has finite R. A finite concave function has a supporting line at each interior M>0; equivalently choose a slope between its right and left derivatives. This is elementary one-dimensional convex analysis, not a compactness assertion about all adaptive policies. Here every supporting slope kappa satisfies

    0<kappa<=1/2.                                       (9)

Nondecreasing F gives kappa>=0; a zero supporting slope would bound F at all larger budgets by F(M), contradicting its limit V>F(M). Concavity and the exact initial slope in(7) give the upper bound. No supporting price at infinity or at the zero-resource endpoint is needed.

## 5. Strong duality without presupposing constrained attainment

Fix M>0 and a supporting kappa from(9). For any finite-resource policy of resource r,

    J<=F(r)<=F(M)+kappa(r-M).

Taking its supremum yields Q(kappa)<=F(M)-kappa M. Conversely every policy with R<=M has J<=Q(kappa)+kappa M. Taking the SUPREMUM, without assuming any feasible maximizer exists, proves

    F(M)=Q(kappa)+kappa M
        =min_(t>=0)[Q(t)+tM], Q(0):=V.                    (10)

The minimum has the strictly positive supporting price above; equality at t=0 is impossible at finite M in this range. This argument is not circular: the budget value is first defined as a supremum, and its attainment is derived next.

## 6. Two finite schedules attain each finite ceiling

Let A_kappa be the set of resource/objective pairs of deterministic finite schedules and abort maximizing Q(kappa). It is nonempty by section2. Its RESOURCE RANGE IS COMPACT, a point that requires more than the padded simplex argument.

To see this, all prices in a neighborhood[kappa/2,3kappa/2] share a finite stage cap from(3). Consider maximizing or near-maximizing schedules at prices tending to kappa; pass to a fixed stage count and a convergent padded control subsequence. If any formerly positive b_i tends to zero, its a_i also tends to zero. Deleting each vanished stage preserves the limiting unpenalized J but removes a resource contribution2P_i>=2exp(-S). The penalized value would increase by at least2kappa exp(-S), contradicting maximality in the limit. The maxima Q(t) themselves converge to Q(kappa), since the common finite cap bounds every retained R by2N and therefore bounds the Lipschitz constant of this supremum of affine functions. Thus no positive stage can disappear in such a near-maximizing sequence. Surviving controls, R and J then converge ordinarily; abort is a separate isolated option. This proves the needed compactness and also controls nearby maximizers.

Write r_min and r_max for the minimum and maximum resources in A_kappa. The elementary envelope slopes of the maximum of the affine functions J-tR are

    Q'_+(kappa)=-r_min, Q'_-(kappa)=-r_max.               (11)

For completeness, a current maximizer supplies one difference-quotient bound. A maximizer at kappa+h supplies the other; the compactness just proved puts every subsequential limit of those optimizers in A_kappa. Let h approach zero from either side to obtain(11). This checks the hypothesis often hidden in a casual use of an envelope theorem.

Since kappa>0 minimizes(10), its left and right derivatives enclose zero, so

    r_min<=M<=r_max.

Choose maximizers with these endpoint resources. If equal, either is sufficient. Otherwise mix the r_min schedule with probability(r_max-M)/(r_max-r_min) and the r_max schedule with probability(M-r_min)/(r_max-r_min). Each component has J=Q(kappa)+kappa r. The mixture therefore has

    R=M, J=Q(kappa)+kappa M=F(M).                         (12)

Both are finite completed original schedules or abort, and both obey the cap for kappa. The maximum is ACTUALLY ATTAINED, not merely approximated by two schedules. The mixing is initial private randomization, already allowed by the original law. It is not two independent leakage constraints or a pathwise bound on trial counts. No assertion that a single schedule suffices is made.

## 7. Execute a positive-price intermediate witness and the vanishing-price limit

The theorem need not force a one-stage answer. At S=1/2,lambda=19/10 take K2565's unchanged rational41-stage policy:

    (a_0,b_0)=(8793/50000,151/500),
    b_(i+1)=99/20000,
    a_(i+1)=b_(i+1)[221/500-(23/500)(2i+1)/80], i=0,...,39.

K2565 certifies J>0.711079567311. The present probe replays its EXACT original prefix resource R=2 sum P_i and verifies R<=82; it reuses the earlier logarithmic certificate instead of recounting it as a new proof. With the actual positive price kappa=1/100000,

    J-kappa R>0.711079567311-82/100000
                 =0.710259567311>0.71+1/5000.            (13)

K2561's certified GLOBAL unpenalized one-stage maximum is below0.71. Penalizing resource only lowers it, and mixtures of one-stage schedules and abort cannot exceed their largest penalized value. Thus at this price the attaining finite optimizer requires more than one positive stage, and the displayed finite witness strictly beats that entire mixture class. This is an executed positive-price consumer, not a computation of the penalized optimizer or its exact stage count. Its stage cap may be conservative.

As kappa decreases to zero, Q(kappa) increases to V: any fixed finite approximate policy provides the lower bound J-kappa R, and Q<=V. If sigma_kappa is any maximizing schedule, then

    Q(kappa)<=J(sigma_kappa)<=V,
    0<=kappa R(sigma_kappa)<=V-Q(kappa) ->0.

In the nonattainment range K2569 now forces R(sigma_kappa) to tend to infinity. The same is true of its positive stage count because R<=2n. Thus finite attainment at every positive price is consistent with resource divergence as the price vanishes. No rate for kappa versus the optimal count is supplied. This price family is a rigorous finite-optimization approximation to the unrestricted problem, not a bounded-resource realization of its unattained supremum.

## 8. Released structural consumer: an exact one-stage priced region

The finite cap need not be searched when an existing theorem already closes the priced problem. Put c=1-2kappa>0. The original-policy inequality R>=2p from(6) gives, for every admissible policy,

    J-kappa R <= c[p-(lambda/c)C].

If lambda/c>=4/sqrt(3), K2559's GLOBAL all-adaptive one-stage theorem applies to the right side. Its one-stage optimizer has R=2p, so it attains equality on the left. Consequently

    Q(kappa)=c U_(lambda/c)(S),
    U_Lambda(S)=max_(0<=a<=S) [1-2Lambda w(a,S)]/(1+a),
    0<kappa<1/2, lambda>=(1-2kappa)4/sqrt(3).       (14)

This is an exact sufficient one-stage region, not a proof that its boundary is sharp at fixed S. At kappa>=1/2 use the separate abort theorem; never divide by c=0. The small-price multistage witness(13) is outside(14), so it remains a genuine contrary case to universal one-stage optimality.

At S=1/2, lambda=19/10, kappa=1/10, the effective multiplier is19/8, whose square361/64 exceeds16/3. Equation(14) therefore eliminates the proposed three-stage search at THIS pair; the three-stage cap remains useful for other multipliers. The optimal a* is the unique root

    M(a)=-2(1+a)w_a(a,1/2)+2w(a,1/2)=8/19.

K2559 supplies M_a=-2(1+a)w_aa<0 and the interior root at these parameters. The new exact rational logarithm enclosure certifies

    383330117/1073741824 < a* < 766660235/2147483648,
    0.5604579098 < Q(1/10) < 0.5604579104,
    1.4738350158 < R*:=2/(1+a*) < 1.4738350164.     (15)

The probe uses the exact logarithmic increment z, sets t=z/(2+z), and encloses log(1+z) between2 sum_(j=0..19)t^(2j+1)/(2j+1) and that sum plus2t^41/[41(1-t^2)]. It checks opposite root signs at the rational endpoints. Since w decreases there, evaluating its endpoint enclosures and the positive denominator bounds certifies Q and R; numerical decimals only display rational proven bounds.

This also executes a NONTRIVIAL finite-budget consumer beyond(7): at the exact budget M=R*, the same one-stage policy attains F_(19/10)(R*)=Q(1/10)+(1/10)R*. No rounding of R* is treated as an exact budget. The whole original adaptive class lies below that supporting line, and the displayed policy lies on it. Thus the positive-price theorem now gives an explicit globally optimal policy bracket and supported budget point, not just existence or a candidate optimizer.

## 9. Execute a whole nonlinear finite-resource segment

The price transformation gives more than the single point(15). Fix0<lambda<4/sqrt(3), and let a_*(S) be K2559's critical one-stage control defined by

    Mfun(a_*,S)=sqrt(3)/4,
    Mfun(a,S)=-2(1+a)w_a(a,S)+2w(a,S).

For every exact resource ceiling m in

    2/(1+S) <= m <= 2/(1+a_*(S)),

take a=2/m-1. For a<S the strictly positive price

    kappa=[1-lambda Mfun(a,S)]/2

has effective multiplier1/Mfun(a,S)>=4/sqrt(3). Its supporting one-stage optimum from(14) has resource exactly m. Therefore the ORIGINAL all-adaptive finite-budget frontier is explicitly

    F_lambda(m)=m/2-lambda m w(2/m-1,S).            (16)

The lower endpoint a=S is the free stage, already covered by(7), and corresponds to kappa=1/2; there is no division by Mfun=0. The upper endpoint has positive price because lambda<4/sqrt(3). No two-schedule optimization is needed on this entire interval. This formula also holds for multipliers between98/51 and4/sqrt(3); its proof uses the positive-price support, not a nonattainment claim in that unclassified interval.

Differentiating the actual cost gives F'_lambda(m)=[1-lambda Mfun(a,S)]/2=kappa and

    F''_lambda(m)=lambda (partial_a Mfun)/m^2<0,

since partial_a Mfun=-2(1+a)w_aa<0. Thus it joins the initial line m/2 with matching derivative1/2 and has strictly decreasing marginal value in its interior. This is an exact new expected-trial frontier segment, not the earlier leakage-budget frontier. Above its upper endpoint the general attainment theorem still applies where stated, but no new closed-form curve or sharp one-stage transition is claimed.

## Postflight, contrary cases and remaining work

The main transfer uses the ORIGINAL fair law and K2569's stronger resource-preserving reduction, not merely the earlier equality of unpriced values. Strongest overclaim: extending strict positive support at every finite M to every lambda. K2559 supplies the contrary regime lambda>=4/sqrt(3), where the unpriced optimum is already an attained one-stage policy and F(M)=V once its finite resource is available; there kappa=0 can support a plateau. The positive-price finite-cap theorem and small-resource segment remain valid for all lambda>0.

Strongest compactness counterconstruction: a two-stage free schedule with first score epsilon tending to zero keeps a limiting extra TWO expected positive trials. At epsilon=0 its omitted padding stage has zero charge. The probe checks this actual law discontinuity and the direction of the penalized jump; claiming continuity would invalidate the proof as written. Strongest reproducibility seam: original resource survival prefixes and the factor2 in(2), both challenged by altered-accounting controls. None of these finite fixtures replaces the universal reduction, upper-semicontinuity, supporting-line or optimizer-limit proofs above.

The exact probe separates rational identities and finite accounting, inherited logarithmic evidence, supporting numerical fixtures, and universal analysis. Independent internal review is required for acceptance; no external-expert, proof-assistant, remote-CI, novelty, physical hardware, native GU or full unpriced intermediate-value certification is asserted. For parameters satisfying(14), reuse the one-stage formula instead of optimizing a multistage family. Outside that sufficient region, the next useful calculation can optimize the bounded finite family at a chosen positive price, or certify its resource bracket and interpolate two supported schedules for a named M. The existence theorem does not establish practical optimizer complexity or choose that operational price for an experiment.

[K2569 resource-preserving bridge](k2569-stopping-maximizing-sequences-2026-11-05.md), [K2567 nonattainment](k2567-stopping-family-structure-2026-11-05.md), [K2565 finite witness](k2565-bellman-supersolution-2026-11-05.md), [K2561 global one-stage bound](k2561-higher-budget-stopping-2026-11-05.md), [K2559 attained regime](k2559-parametric-stopping-concavity-2026-11-05.md), [K2485 distinct leakage-budget theorem](k2485-constrained-stopping-frontier-2026-11-01.md), [standard supporting-line background](https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf), [probe](../../tests/channel-swings/k2571_stopping_resource_price_probe.py), [report](../../lab/process/k2571-stopping-resource-price.json).
