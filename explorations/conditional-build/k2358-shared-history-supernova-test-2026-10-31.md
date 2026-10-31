---
title: "K2358 Shared expansion history against two released likelihoods"
status: active_research
doc_type: exploration
created: "2026-10-31"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematics or numerical released-likelihood evidence; no native GU certification
scripts:
  - tests/channel-swings/k2358_shared_history_supernova_test_probe.py
---

# K2358 Shared expansion history against two released likelihoods

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
result: K2358
carrier: real flat vacuum expansion histories and two released correlated data vectors LAYER=toy CHIRALITY=N/A
pairing: Gaussian covariance with profiled intercept and ruler ON=declared_carrier
real_structure: real positive expansion histories, real coefficients and released magnitude/distance data
grading: correlated observation rows versus shared shape coordinates and calibration nuisances
action_owner: repository-construction -- shared conditional vacuum metric f(R) coefficients
target: joint numerical data compatibility MAP-TYPE=evaluation
```

## Result and scope

One shared rolling vacuum history now has a numerical fixed-release witness against both the1590 selected Pantheon+ lightcurve rows and all13 DESI coordinates. The shape coefficients and initial derivative are shared; only the supernova magnitude intercept and one positive BAO ruler are profiled independently because they represent different calibration scales. This is a numerical compatibility witness under fixed published corrections/covariances and assumed zero inter-survey covariance. It is not a native GU prediction, a global optimum, a p-value, or a calibration-free physical test.

[K2355](k2355-released-supernova-shape-2026-10-31.md) supplied the actual supernova consumer. [K2283](k2283-global-quadratic-cosmology-2026-10-30.md) supplied the prior DESI witness and global positive-history theorem. Their composition is new here. K2265 already excludes a nonconstant constant-R regular vacuum branch and exact LCDM-shaped vacuum; those results are reused as typing constraints, not new findings. SC-COS-50/51/54 ASSERTS and ledger0.263 LT-GR2e retain their source/observation and matter debts. The supplied metric f(R) family is distinct from the source connection-distortion construction and does not repair its failed local screening.

## One history, full constraint, two consumers

Set b=-1, a=alpha/(b H_*²)=-A<0, r=rho/(b H_*⁴)=-B<0, t=(1+z)^3, U(1)=2, U_t(1)=V1, M(1)=0. Reuse the exact full00 reduction:

    U_tt=-A/(36t² U^(1/3))+B/(216t² U^(5/3)),
    M_t=1/[3(tU)^(2/3)], H/H_*=U^(2/3).

These equations enforce the full vacuum constraint; trace alone is not fitted. U1 fixes a scale convention, not a measured H0. K2283's coercive energy proves U>0 at every finite past redshift for A,B>0. Its integrating factor proves that dimensionless endpoint F/H_*²=12U^(1/3)(U-tU_t)+A>0 implies positivity throughout the preceding interval. All reported F values mean F_phys/H_*² in these b=-1 units. Our endpoint values are floating-point observations, not rigorous interval enclosures. Numerical convergence is separately checked with tighter DOP853 tolerances and RK45. No continuum numerical certification is claimed.

For supernovae use f_i=5log10[(1+zHEL_i)M(zHD_i)], the pinned K2355 corrected magnitudes, zHD>.01 and full selected covariance. Profile the single additive intercept by covariance whitening. The BAO vector uses the same M and U in DM, DH and DV, with one positive amplitude lambda=(H_*r_d)^(-1). All13 means and covariance are read from the hash-checked source text already stored in K2277, with no new dataset substitution. The sum Q_SN+Q_BAO assumes block-diagonal joint covariance; lack of a supplied cross-survey covariance is an explicit limitation. Distinct nuisance scales do not mean independent shape coefficients or coordinate-specific rulers.

## Concrete consequence and joint follow-through

The old DESI SHAPE (A,B,V1)=(33.8,1,.9303) is evaluated on the previously unused supernova consumer before any shape refit. Its BAO ruler is analytically reprofiled (50.03961479 versus the earlier fixed50.04185); Q_SN=1442.50368274 and Q_BAO=5.88076664. The committed report records its actual two discrepancies. Then the SN-only search and joint search use the same three-parameter family. The frozen joint witness is

    A=55.85236076, B=929.86045772, V1=.4885325972.

It gives approximately Q_SN=1402.46615 and Q_BAO=7.00625, sum1409.47240, with lambda47.69122 and endpointF143.74231. A SN-only witness near(57.47501734,940.15711289,.4923669240) gives Q_SN1402.35800 but Q_BAO13.81022. Thus optimizing each dataset separately is not a joint witness; the retained joint coefficients explicitly pay the tradeoff. This does not establish statistically significant tension. The prior DESI criterion Q13<6 is not met by the joint witness, and no global statement excluding simultaneous Q13<6 and another SN threshold follows. No threshold was independently specified for this joint comparison.

All three SN starts and two joint starts converge near the stated witnesses. A third joint start terminates at a very poor local result (sum about14523), despite reporting numerical success. The report preserves that outcome. Nelder-Mead operates on logA,logB,V1, with max450 iterations and declared tolerances; no finite bounded parameter box or global-minimum claim follows. An earlier least-squares attempt entered a nonpositive-F penalty region and produced no usable witness; it is not scientific exclusion. Deterministic report replay uses the exact rounded witnesses, not optimizer success.

## Controls, limitations and reuse

The exact domain and F identities are already proved in K2271/K2283. Here the new evidence is numerical: input hashes, full covariance, both surveys, profile invariance, independent ODE method and tighter tolerances. Altered redshift prefactor, diagonal covariance and independently adjustable BAO coordinate rulers change the actual calculation. A fully free luminosity-evolution vector can still mimic every finite-row mean; the probe constructs that mimic. Do not apply K2355's two-fixed-shape Gaussian classification theorem to data-fitted shapes.

The remaining useful question is whether a physically justified common matter/radiation and perturbation/ruler model, or actual population/selection variants, preserve the witness. Vacuum optics transported through published survey products is not that model. A new tighter optimizer tolerance alone does not supply the missing physical premise. No novelty or external-expert certification is claimed. Background metric equations are reviewed by [De Felice and Tsujikawa](https://arxiv.org/abs/1002.4928); released input locators and covariance semantics are pinned by K2355 and K2277.

Reproduce with NumPy/SciPy, one BLAS thread, and K2355's hash-verified scratch inputs:

    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python tests/channel-swings/k2358_shared_history_supernova_test_probe.py --data-dir /absolute/scratch/path

`--scout` optionally reruns the documented numerical search. The default is the reproducible frozen-witness calculation.
