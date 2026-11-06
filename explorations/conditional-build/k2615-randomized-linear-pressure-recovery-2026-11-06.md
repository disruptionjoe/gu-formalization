---
title: "K2615 Randomized linear recovery on the prepared source kernel"
status: active_research
doc_type: exploration
created: "2026-11-06"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: known finite Hilbert ball and scalar linear-query oracle; no physical detector achievability or dimension-uniform radius
scripts:
  - tests/channel-swings/k2615_randomized_linear_pressure_recovery_probe.py
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
result: K2615
carrier: K2611 smooth conserved pressure kernel, finite real Hilbert slices and measurable adaptive scalar linear sensors LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert source error norm ON=declared_carrier
real_structure: real source amplitudes and scalar observations; exact symbolic projection and moment fixtures
grading: source restriction, acquisition class, proof and numerical illustration remain distinct
action_owner: repository-construction -- supplied conditional model
target: exact randomized recovery risk and source-information lower bounds MAP-TYPE=evaluation
```

# Random sensing helps, but does not identify every source

## Result and object boundary

K2613 proved deterministic finite-information ambiguity and expressly left randomized sensing open. The hard pair there could depend on the sensor seed. Here a uniform-sphere argument addresses the actual randomized quantifiers.

Let E be a KNOWN real d-dimensional Hilbert space of K2611 smooth exterior-kernel source perturbations, and let j0+{v in E: ||v||<=R} be an admissible nonnegative-amplitude ball. For a pathwise cap of m<d exact real scalar linear queries, with measurable adaptive selection, arbitrary measurable reconstruction and source-independent randomness, the ideal unrestricted-query minimax risks are

    inf_A sup_(||v||<=R) E ||A(j0+v)-(j0+v)||² = R²(1-m/d),
    inf_A sup_(||v||<=R) E ||A(j0+v)-(j0+v)|| = R c(d,m),
    c(d,m)=Gamma((d-m+1)/2) Gamma(d/2)
                         /[Gamma((d-m)/2) Gamma((d+1)/2)].          (1)

The first quantity is mean SQUARED error, not RMS; RMS is its square root. m=0 gives R² and R directly; m>=d permits exact recovery of this known finite model. These are mathematical oracle results. A restricted physical detector family inherits the lower bounds but need not attain them. The whole infinite-dimensional smooth class inherits a lower bound from each embedded ball; it does not inherit equality or a radius uniform in d.

The source/preparation is the conditional curved-product completion, not source-native GU. SC-ACT-01/02 and SC-GEO-03/55 retain ASSERTS; SC-META-53 remains UNCERTAIN. Ledger0.263 LT-GR1b/6b/10 and LT-SM8 and canon are unchanged. Nonnegative amplitudes and the positive error norm are not physical energy or the action pairing. No randomized nonlinear-sensing, average-query-budget or physical apparatus theorem is claimed.

## 1. The actual source ball and information model

Reuse K2611's infinite-dimensional smooth conserved kernel supported in a fixed interior radial plateau and B exclusion ball. First intersect it with any finitely many desired linear normalization kernels; it remains infinite dimensional. Choose d independent directions and their span E. Fix a positive transverse L2 inner product on source amplitudes with a positive smooth measure. This defines a genuine Hilbert norm on E and an ambient Hilbert source norm for permitted reconstructions. Orthogonal projection back to j0+E cannot increase error to a source in that affine space. One may instead restrict all reconstructions to j0+E from the outset.

K2611's conserved background has both amplitudes equal to one on the perturbation support. Let C_E=max_(||v||=1) max(||deltaP_v||infinity,||deltaA_v||infinity). Choose R C_E<1, and shrink R to accommodate any other strict upper-bound margins. Conservation is linear and the finite normalizations are preserved exactly. This proves the entire closed ball is admissible and all its exterior readings agree with j0. The radius depends on the chosen E and margins. Saturated inequalities and arbitrary nonlinear source equations need not contain this ball.

At each query the algorithm chooses a real linear functional ell_i from its previous real readings and private random seed, and reads ell_i(j0+v). The seed is independent of v. The baseline ell_i(j0) is known and subtracted. Every restriction to finite E is continuous; selection and decoder maps are measurable so the risks exist. Query scaling and unlimited numerical precision do not create extra scalar queries. No vector-valued reading is counted as one. The budget is at most m on every realization, not only in expectation.

## 2. Lower bounds that survive random sensor choice

Put a uniform prior on the radius-R sphere in E. Fix the algorithm's seed. Gram-Schmidt reduces each new query to its component orthogonal to the span already measured. A zero new component supplies no information. Give the algorithm additional orthogonal coordinates until m independent directions are measured if necessary; this can only improve its performance and so is legitimate for a lower bound.

After i independent queries, condition on their transcript. The unknown vector has the form z_i+U_i, where z_i is the known orthogonal projection and U_i is uniform on a sphere of radius rho_i in the (d-i)-dimensional perpendicular space. This follows inductively by rotational invariance and regular conditional distributions. Given the transcript, the next direction is fixed even when its selection is discontinuous. Its normalized coordinate therefore has the ordinary uniform-sphere coordinate law; the adaptive choice cannot select a preferred unknown direction.

Consequently, after m independent queries,

    rho_m²/R² has distribution Beta((d-m)/2,m/2).                   (2)

One derivation multiplies the sequential remaining-radius fractions. Conditional on the past, the next fraction has Beta((d-i-1)/2,1/2) law independent of the past radius. Its moments telescope to Beta((d-m)/2,m/2). Equivalently these are the coordinate-square sums of a normalized d-dimensional standard Gaussian; this is a proof device, not a Gaussian source prior. The endpoints m=0 and m=d are treated separately.

The conditional center z_m minimizes squared error by the conditional-mean identity. It also minimizes expected norm: central symmetry and convexity give E||U-z|| >= E||U|| for every fixed z. Thus the best conditional losses are rho_m² and rho_m. Their expectations from (2) are exactly (1). Randomized decoders cannot improve either conditional minimum.

Integrate over the independent seed, then use worst-case risk >= prior-average risk. This is the correct order of quantifiers: no single source pair is asserted to be invisible for every seed. It proves the bounds against randomized adaptive linear acquisition, including nonlinear decoders and arbitrary computation.

## 3. Achievability and a useful distinction between norms

Choose a Haar-uniform m-dimensional plane in E independently of the source, measure an orthonormal basis and return j0 plus the measured projection. For every fixed v, its residual squared norm divided by ||v||² has exactly (2). The risk is homogeneous in ||v|| and maximal on the boundary, proving both upper bounds in (1).

There is a simpler FINITE algorithm attaining the squared-risk bound: fix any orthonormal basis, choose uniformly one of all m-coordinate subsets, query those coordinates, and zero the rest. Every coordinate is missed with probability (d-m)/d, so its expected squared residual is (1-m/d)||v||². This requires no continuous random rotation. It generally does not attain the expected-NORM optimum. For d=3,m=1 and a vector with equal coordinates, its residual norm is always R sqrt(2/3); the Haar algorithm has mean norm pi R/4, strictly smaller. Confusing mean norm and RMS would give the wrong constant.

These upper bounds assume the arbitrary coordinate queries can actually be performed. They are not a construction of the curved physical receiver matrix or the uncomputed Ore kernel coefficients. Abstract existence of E suffices for the source-class LOWER bound; computable basis and permitted sensors are additional inputs for implementation.

## 4. Released information-complexity and noise consequences

For the known E-ball and unrestricted query model, worst-case RMS error at most epsilon<R is achievable exactly when

    m >= ceil(d [1-epsilon²/R²]), with 0<=m<=d.                    (3)

For example halving RMS on a d=12 ball takes at least nine queries and the random-coordinate scheme achieves it. Finitely many prescribed normalization moments can be imposed before selecting E; they do not count as newly informative queries on that ball. The deterministic worst-case radius remains R for m<d, as K2613 showed. Randomization lowers expected risk but cannot give zero risk on every source in a ball with d>m.

There is also a precise noisy-linear extension. Suppose each noisy reading can be generated from the chosen linear functional's exact scalar value, previous transcript and source-independent auxiliary random variables; subsequent sensors may depend on these noisy readings. An exact linear-query algorithm can simulate this entire experiment with the same pathwise query cap: ask the selected exact query, synthesize its noise, then run the same next-sensor rule and decoder. Therefore the lower bounds (1) still apply to this noisy adaptive linear model. Noise may worsen risk; equality is not asserted. Noise carrying additional source information, nonlinear acquisition, random source-dependent seeds or an expected-only cap fall outside this simulation. This closes the earlier noise-feedback caveat for this specified linear class without pretending the old deterministic hard-pair proof covered it.

No dimension-independent infinite-class error floor follows. For any finite m choose one admissible E of dimension greater than m, obtaining a strictly positive bound with its actual R. Physical restrictions removing these affine balls, a common radial profile, or sufficiently rich interior observations remain different questions.

## Evidence and next condition

The probe checks exact finite random-coordinate risks, adaptive orthogonalization, spherical moments, a normalization-preserving positive-amplitude fixture and the information-complexity consumer. These are finite supporting calculations. The universal adaptive argument and K2611 source embedding are the proofs above, independently reviewed internally; no external certification or novelty claim.

The measurable adaptive-information setting is standard; see [Kunsch, Novak and Wnuk](https://arxiv.org/html/2308.01705). Their norm-embedding problems are context, not the source of the exact constants proved here. The next source question is a real restriction that removes the kernel ball or an actual receiver/domain construction. Randomized scalar linear sensing alone is no longer an untested generic rescue.

[K2611](k2611-fixed-preparation-invisible-pressure-2026-11-06.md), [K2613](k2613-finite-observation-pressure-ambiguity-2026-11-06.md), [probe](../../tests/channel-swings/k2615_randomized_linear_pressure_recovery_probe.py), [report](../../lab/process/k2615-randomized-linear-pressure-recovery.json).
