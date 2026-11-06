---
title: "K2613 Finite nonlinear and adaptive information does not identify prepared pressure sources"
status: active_research
doc_type: exploration
created: "2026-11-06"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional smooth pressure class and source-norm recovery only; no physical energy or randomized sensing theorem
scripts:
  - tests/channel-swings/k2613_finite_observation_pressure_ambiguity_probe.py
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
result: K2613
carrier: K2611 smooth conserved correlated pressures on the selected curved product LAYER=toy CHIRALITY=N/A
pairing: complete exterior metric readings plus finite real source calibrations ON=declared_carrier
real_structure: real compact kernel perturbations about a nonnegative conserved background
grading: source reconstruction, calibrated data and physical admissibility are distinct
action_owner: repository-construction -- K2611 fixed reciprocal preparation
target: finite-information injectivity and source recovery error MAP-TYPE=evaluation
```

# Finite information cannot remove the smooth source ambiguity

## Result and scope

K2611 supplies an infinite-dimensional space of smooth conserved source perturbations whose fixed-preparation full metric vanishes outside one B ball. We show that adding finitely many continuous nonlinear measurements still fails to identify every source in a sufficiently small nonnegative-amplitude neighborhood. Deterministic adaptive linear measurements fail even on the transcript of an explicitly chosen background. An imported adaptive-continuous theorem extends the conclusion to nonlinear probes selected by arbitrary deterministic rules. The resulting source-reconstruction error has a quantitative lower bound on each chosen finite-dimensional ball.

These statements concern K2611's correlated smooth pressure class and specified mathematical preparation. They do not give a native GU verdict, positive physical energy, fixed-profile counterexample, randomized-sensing theorem or a universal error floor independent of the chosen subspace. SC-ACT-01/02 and SC-GEO-03/55 retain ASSERTS; SC-META-53 remains UNCERTAIN. Ledger0.263 LT-GR1b/6b/10 and LT-SM8 and canon are unchanged.

## 1. A real admissible ball, not a formal dimension count

Use K2611's actual conserved background j0, with pressure amplitudes P0=A0=1 on a compact plateau and both amplitudes nonnegative everywhere. Choose d independent smooth kernel perturbations v1,...,vd supported strictly inside that plateau. Each obeys deltaA=deltaP+deltaP'/(4alpha), with support away from the radial center. Let E be their real span and choose a genuine norm ||.||_* on E, for example the transverse L2 norm of both amplitudes with a fixed positive smooth measure. It is an auxiliary source norm, not the indefinite action pairing or physical energy.

The injection E into smooth source amplitudes is continuous on this finite-dimensional space. Set

    C_E=max_(||v||_*=1) max(||deltaP_v||infinity,||deltaA_v||infinity).

Compactness gives C_E finite and positive. Choose r>0 with r C_E<1. Every source j0+v with ||v||_*<=r has positive amplitudes on the perturbation support and unchanged nonnegative amplitudes elsewhere. Its complete exterior observations equal those of j0. All these sources satisfy the original conservation equation and the same fixed preparation. No source is inserted by extension across an endpoint.

A finite collection of strict upper seminorm bounds can be included by reducing r within their actual margins at j0. Exact finite linear normalizations can be imposed FIRST: intersect the infinite-dimensional kernel with the kernels of those functionals, then choose d independent directions in the intersection. All sources then have the realized background normalizations, without rescaling them. A bound saturated at j0 or an arbitrary nonlinear admissibility equation need not contain any such ball; no conclusion is made for it.

## 2. Fixed continuous nonlinear calibrations

Let F1,...,Fm be any real-valued measurements continuous on every finite-dimensional affine slice under consideration. Smooth-source topology on fixed compact support is sufficient; no global Banach completion or differentiability is needed. Take d=m+1 above. On the radius-r sphere, the map v -> (F_i(j0+v)) is continuous. The classical Borsuk-Ulam theorem provides v with

    ||v||_*=r, F_i(j0+v)=F_i(j0-v) for all i.

The two sources are distinct, nonnegative-amplitude, conserved, and share all exterior data. The calibration functionals can be nonlinear, and can represent finitely many interior metric observations whenever these are continuous functions of the prepared source. The conclusion remains a source-space result; an observation constant on E is not a source reconstruction.

The common nonlinear readings need not be those of j0. For example on this affine family F(j0+v)=||v||_*² has F=0 only at j0 while every antipodal pair on the sphere shares F=r². Thus a specified nonlinear constraint can identify one data fiber even though the map is not injective on the neighborhood. Generic noninjectivity is not ambiguity at every prescribed measurement vector.

## 3. Adaptive information and the importance of its type

For at most m deterministic adaptive LINEAR measurements, d=m+1 suffices and no continuity of sensor selection is needed. Run the algorithm on j0 and freeze the selected functionals ell1,...,ellm along that transcript. Their restrictions to E have a common nonzero kernel. Normalize v in that intersection to ||v||_*=r. At the first stage j0 and j0+/-v have equal readings; induction gives the same next sensor and the same next reading at every stage. Early stopping can be padded with zero readings. Hence the pair shares the entire BASELINE transcript, as well as all original exterior data. This argument permits the sensor rule to depend on the already known common exterior data.

For arbitrary deterministic adaptive CONTINUOUS nonlinear measurements, a stronger imported theorem is required: Ullrich, Theorem1, states that m such measurements on a sphere in dimension d>=2^m have an antipodal collision, even with discontinuous selection rules. Apply it to F(v)=j0+v on E. K2611 supplies any finite d, so the same source ambiguity follows. This extension relies on the cited preprint, not on the classical m+1 argument; no novelty is claimed. [Ullrich, arXiv:2610.33781v1](https://arxiv.org/html/2610.33781v1).

If the complete adaptive transcript is itself continuous, the classical d=m+1 proof already applies. Continuity of each selected nonlinear functional alone does not imply that aggregate continuity. Discontinuous source encodings, infinitely many exact readings, random measurement selection, and a physical restriction removing the affine ball are outside these claims.

## 4. Released quantitative recovery consequence

Let an algorithm return a reconstructed source from the entire available transcript. For the indistinguishable pair j+=j0+v and j-=j0-v, its output is the same z. In any ambient source norm extending ||.||_* on E, the triangle inequality gives

    max(||z-j+||_*,||z-j-||_*) >= ||j+-j-||_*/2 = r.

If the norm was defined only on E, constrain reconstruction to the affine source family, or specify an ambient extension before using this formula. Therefore the worst-case source recovery error on this ball is at least r. The constant reconstruction j0 has worst-case error r on the ball, so the minimax error over the specified deterministic measurement class is exactly r whenever the matching dimension threshold holds. This statement permits unlimited computation and arbitrary decoders; it concerns information, not computational difficulty.

Randomizing only the decoder does not improve the worst-case expected norm error: apply the triangle inequality to the same output law and average. Adding source-independent noise AFTER the completed noiseless transcript, with law depending only on that transcript, also preserves indistinguishability. Noise fed back into adaptive sensor choice is a different acquisition law and is not covered. These arguments do not apply to randomized measurement selection: the hard pair could depend on the sensor seed. No uniform error floor as d or m increases follows, because admissible r depends on the chosen E, its source norm and background margins.

For fixed m, the construction may first preserve any finite prescribed linear moments at their background values and then choose the required dimension for the nonlinear/adaptive measurements. Thus combining finite normalization with finite calibration does not rescue whole-neighborhood recovery on this class. A meaningful successful repair must remove the relevant affine kernel ball, provide sufficiently rich infinite information, or change the source/preparation model. A pointwise physical restriction may do so; it has to be tested rather than replaced by a count of calibrations.

## 5. Exact controls and remaining question

The probe constructs a nonzero exact null vector for a sequentially chosen two-sensor linear example, verifies equal baseline transcripts and preserved moments, tests antipodal nonlinear readings that differ from baseline, verifies positive amplitude margins and norm separation, and exhibits injectivity once the class is reduced to a measured line. It also tests the triangle/expected-risk identities and the different dimension thresholds. These are finite algebraic fixtures, not a numerical proof of Borsuk-Ulam or a computation of the unknown curved kernel coefficients.

The existence and compactness of the real curved kernel and background are reused from K2611; the universal observation conclusions are the proofs above. The adaptive nonlinear extension is an explicit theorem import with its stronger dimension cost. Independent review is internal, not external-expert certification.

Next test an actual source restriction eliminating this affine freedom (for example a common radial-profile condition or physically derived nonlinear source relation), or an infinite-dimensional interior observation with its full domain. The actual synchronized Ore coefficients/order remain uncomputed. Finite nonlinear calibration and deterministic adaptive calibration alone are now resolved at their stated scopes.

[K2611](k2611-fixed-preparation-invisible-pressure-2026-11-06.md), [probe](../../tests/channel-swings/k2613_finite_observation_pressure_ambiguity_probe.py), [report](../../lab/process/k2613-finite-observation-pressure-ambiguity.json).
