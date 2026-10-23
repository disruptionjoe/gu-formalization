---
title: "K1962: Finite tails improve the thermal rooted polygon"
status: active_research
doc_type: exploration
created: "2026-10-22"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: exact rooted-family improvement and priced optimizer; no global all-spectrum optimum
scripts:
  - tests/channel-swings/k1962_finite_tail_thermal_improvement.py
  - tests/channel-swings/k1962_finite_tail_thermal_improvement_probe.py
---

# K1962: Discarding the finite right arm loses useful protocols

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

```gu-typed-objects
result: strict finite-tail improvements for every limiting rooted chord and finite priced-family optimization
carrier: fixed extreme four-state channel, t=1/2 bath, finite nondegenerate catalyst LAYER=toy CHIRALITY=N/A
pairing: worst-input marginal half trace distance and initial mean energy ON=independent_initial_registers
real_structure: complex conserving shell unitaries with exact real populations
grading: additive energy shells, not source chirality
action_owner: repository-construction -- fixed conditional quantum channel
target: rooted physical family inside the all-spectrum energy-return frontier MAP-TYPE=intertwiner
```

## 1. What is new and what is reused

[K1960](k1960-thermal-frontier-convexification-2026-10-22.md) proves a global
convex frontier and constructs an upper polygon U from limiting right-infinite
rooted families. It explicitly does not claim U is optimal. Every vertex of
that polygon with root index n>=1 has finite physical right-tail truncations
lying strictly below its preceding chord. This supplies an all-n reason that
U is not the global frontier, rather than another finite-cutoff conjecture.

The elementary witness(E,R)=(19/8,9/32) is already known in K1950/K1952; it
is reused, not counted as a new optimum. New content is the universal
truncation identity, an exact finite search for the priced optimum over ALL
rooted families, and its small-price tail-length consequence. None optimizes
over all finite spectra or proves a global asymptotic amplitude.

## 2. Exact truncation identity and every-chord improvement

Use q=2/3, p=1/9, W=25/8 and K1960's finite occupied energies
1,3,...,2(n+m)+1, with unnormalized weights q^(n-i) for i<=n and p^(i-n)
for i>n. These are actual finite physical shell protocols. Put

    Z= W-2 q^n, h=p^m/8, B=2n+2m+13/4,
    R_n=1/(2Z), E_n=2n-11/4+(4n+9/2)q^n/Z.

The omitted right tail has total weight h and conditional mean energy B:
its first omitted index is m+1 and the geometric excess mean is p/(1-p)=1/8.
Consequently the finite protocol has exactly

    R_nm-R_n = h/[2Z(Z-h)],
    E_n-E_nm = h(B-E_n)/(Z-h).                         (1)

For n>=1 let s=s_(n-1)<0 be K1960's preceding polygon slope. Whenever
E_(n-1)<=E_nm<E_n, formula(1) gives

    U(E_nm)-R_nm
      = h/(Z-h) [(-s)(B-E_n)-1/(2Z)].                  (2)

As m grows, E_nm increases to E_n and B grows without bound. Thus chord
membership holds eventually and the bracket becomes strictly positive.
Every n>=1 therefore has finite protocols strictly improving U. There is
also a nonempty open interval of budgets with R_star(E)<U(E), by continuity
and the one physical strict witness. No infinite catalyst is used.

Examples from exact physical populations:

|n|m|Mean energy|Return|Improvement below U|
|---|---|---|---|---|
|1|1|19/8|9/32|23/7200|
|2|1|37/10|9/40|3/61000|
|3|4|86073/16615|6561/33230|37/235102250|
|4|8|791265823/117514891|43046721/235029782|1/167684709850|

The last two are independently checked using full complex conserving shell
unitaries including unused inputs and incomplete edge shells. The all-n result
is the proof above; a finite table cannot establish it. K1960's upper bound
and its asymptotic bound remain valid. K1954's rejection of the proposed third
secant also remains valid.

## 3. Exact priced right-arm optimizer

For lambda>0 define f_nm=R_nm+lambda E_nm. Appending the next rightmost
weight w=p^(m+1) at e_new=2n+2m+3 gives

    f_(n,m+1)-f_nm = w/(Z_nm+w) [lambda e_new-f_nm].    (3)

This identity has a single-crossing consequence. While lambda e_new<f_nm,
appending lowers the cost. At the first nonnegative difference the new cost
is a weighted average of f_nm and lambda e_new, hence no larger than
lambda e_new; the NEXT added energy is larger by2, so every later difference
is strictly positive. Equality gives two adjacent tied minimizers only.
A crossing occurs at finite m because f_nm converges while e_new diverges.
Thus the first m satisfying lambda(2n+2m+3)>=f_nm is a global minimizer over
ALL right-arm lengths for this n, not just a scanned cutoff.

The infinite-tail limit f_n,infinity=R_n+lambda E_n is never the minimum for
lambda>0. Formula(1) gives

    f_n,infinity-f_nm
       = h/(Z-h)[lambda B-f_n,infinity],              (4)

which is positive for sufficiently large finite m. This is a priced strict
improvement, not a global supporting-line certificate.

## 4. A finite exact algorithm for all rooted families

The left arm's mean distance below its root is at most
q/(1-q)=2. Its mean energy is therefore at least2n-3; adding right-arm
populations raises that mean. Also R_nm>4/25. The n=m=0 family provides cost
1/2+lambda. Hence an index n with

    4/25+lambda(2n-3)>1/2+lambda,
    equivalently n>2+17/(100lambda),                 (5)

cannot win. Enumerate n only up to a safe integer bound from(5), and use the
first-crossing rule(3) at each n. This returns the exact priced minimum over
the entire infinite discrete rooted family. All arithmetic can be rational
for rational lambda, including ties.

|lambda|Minimizing(n,m)|Mean energy|Return|
|---|---|---|---|
|1/4|(0,0)|1|1/2|
|1/10|(1,1)|19/8|9/32|
|1/25|(2,2)|675/181|81/362|
|1/50|(2,4)|54787/14671|6561/29342|
|1/100|(3,8)|564739097/109011835|43046721/218023670|

This offers candidates for the global dual from K1960, but its minimum is an
UPPER bound on b(lambda), because rooted families are a subset of protocols.
It is not an all-spectrum lower certificate. Mixtures cannot reduce a linear
priced objective below the best component, so the same infimum holds for
mixtures of rooted protocols with arbitrarily small nondegeneracy shifts.
This does not make the restricted family complete for the global problem.

## 5. Small-price boundary-layer consequence

Fix n. Let m_lambda be the first crossing in(3), and let f_inf=R_n+lambda E_n.
The crossing inequality, after using(4), is exactly

    Z[lambda(2n+2m+3)-f_inf]+lambda h/4 >=0.           (6)

The preceding m fails it. Together they imply

    m_lambda=R_n/(2lambda)+(E_n-2n-3)/2+O(1),
    lambda log(f_inf-min_m f_nm) -> -(R_n/2)log9.      (7)

For completeness, m_lambda tends to infinity as lambda decreases. At the
first crossing, lambda B-f_inf is between lambda/4-o(lambda) and
9lambda/4+o(lambda), using failure at m-1 and h_(m-1)=9h_m.
Equation(4) then bounds the positive improvement between positive constant
multiples of lambda*9^(-m_lambda). Taking lambda times its logarithm proves(7).
This is a fixed-root, small-price statement. It neither interchanges a growing
n with the limit nor proves that the global E-asymptotic coefficient changes.
Tiny finite improvements alone cannot establish or refute global modulation.

## 6. Verification and scope

The producer checks1272 exact identities/price comparisons and1590 physical
shell controls. The separate probe reconstructs populations by recurrence,
rebuilds incoming deficits using bath labels, checks283 exact comparisons,
and independently checks two symbolic tail identities. Four mathematical
input faults are detected after a green baseline: right-tail ratio, energy
origin, return normalization and omitted tail normalization. A first draft
of the independent checker mistakenly used half the gap-two bath weights;
its clean baseline failed, the coefficients were corrected to H=1/5,L=4/5,
and the full independent replay then passed. No crash is counted as detection.

Strongest overclaim: treating the restricted priced minimum as a global dual
lower bound. Strongest contrary construction: a different support motif can
beat this entire family. Weakest transfer seam: actual physical shell
realization; exact complex controls accompany the previously proved family
construction. Universal claims rely on(1)-(7), not finite sample counts.
Internal review found no residual issue within this scope; no external expert,
formal certification or novelty claim is made.

[Ng et al., Limits to catalysis in quantum thermodynamics](https://arxiv.org/abs/1405.3039)
is context for mean-energy restrictions, not the source of this channel-specific
optimizer; its abstract was rechecked. SC-META-53 remains UNCERTAIN and
LT-SM8/LT-GR6b/AC-F1 remain NEEDS. No GU source/action/quotient claim moves.
The useful next test is an all-spectrum priced lower bound or a physical
non-rooted motif beating the exact restricted optimum, not more truncation
examples or extrapolation from a finite hull.
