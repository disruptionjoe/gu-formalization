---
title: "K2355 A real released supernova distance-shape diagnostic"
status: active_research
doc_type: exploration
created: "2026-10-31"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional construction or released-likelihood diagnostic; no GU certification
scripts:
  - tests/channel-swings/k2355_released_supernova_shape_probe.py
---

# K2355 A real released supernova distance-shape diagnostic

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
result: K2355
carrier: Pantheon+ selected corrected-magnitude rows with joint covariance LAYER=toy CHIRALITY=N/A
pairing: Gaussian release likelihood with profiled magnitude intercept ON=declared_carrier
real_structure: real Gaussian magnitude data and real distance-shape parameters
grading: correlated lightcurve rows versus physical objects
action_owner: repository-construction -- fixed released corrections and conventional flat FLRW optics
target: reproducible distance-shape comparison and calibration sensitivity MAP-TYPE=evaluation
```

## Result and scope

[K2352](k2352-calibrated-flrw-identifiability-2026-10-31.md) establishes abstract nuisance-class boundaries. Here the calculation uses an actual public observation product: Pantheon+ corrected supernova magnitudes and its full statistical-plus-systematic covariance. It profiles a free magnitude intercept, approximately reproduces the released flat-LambdaCDM matter-density fit as a positive control, evaluates the two conventional extreme shapes used in K2349, and computes the exact sensitivity of that fixed-shape contrast to an additional bounded magnitude drift. Machine-readable numerical results are in `lab/process/k2355-released-supernova-shape.json`.

This is a diagnostic of a FIXED RELEASED LIKELIHOOD. It is not a reanalysis of lightcurves, selection simulations or all possible population evolution. In particular, extreme de Sitter and Einstein-de Sitter shapes are evaluated against corrections/covariance made with the release's assumptions; this does not establish that those corrections remain calibrated under those extremes. A fixed likelihood contrast is useful reproducible evidence, but it is neither a native GU forecast nor universal physical exclusion. SC-COS-50/51/54 ASSERTS and LT-GR2e NEEDS retain their original scope; no source, ledger0.263, canon or residue changes.

## Pinned public inputs and observation convention

DataRelease revision `c447f0fea703fcd0fff57de5000947b5ca81286b`:

- [Corrected-magnitude table](https://raw.githubusercontent.com/PantheonPlusSH0ES/DataRelease/c447f0fea703fcd0fff57de5000947b5ca81286b/Pantheon%2B_Data/4_DISTANCES_AND_COVAR/Pantheon%2BSH0ES.dat), SHA256 `1cb0fc379ef066afdc2ffd1857681cc478024570d8a3eba284fb645775198cf8`.
- [Full covariance](https://raw.githubusercontent.com/PantheonPlusSH0ES/DataRelease/c447f0fea703fcd0fff57de5000947b5ca81286b/Pantheon%2B_Data/4_DISTANCES_AND_COVAR/Pantheon%2BSH0ES_STAT%2BSYS.cov), SHA256 `abf806d966485e64afdb359c87bffc0ecc00d05eff0a31ced66f247385df0fdc`.
- [Statistical covariance](https://raw.githubusercontent.com/PantheonPlusSH0ES/DataRelease/c447f0fea703fcd0fff57de5000947b5ca81286b/Pantheon%2B_Data/4_DISTANCES_AND_COVAR/Pantheon%2BSH0ES_STATONLY.cov), SHA256 `9f177129a332735d3637affd20054080d5260815f3ca0809120c05b2c902297f`.
- [Release column and covariance definitions](https://github.com/PantheonPlusSH0ES/DataRelease/blob/c447f0fea703fcd0fff57de5000947b5ca81286b/Pantheon%2B_Data/4_DISTANCES_AND_COVAR/README).
- [Pantheon+ analysis paper](https://arxiv.org/abs/2202.04077) supplies the reference fit; [CosmoSIS likelihood implementation](https://github.com/joezuntz/cosmosis-standard-library/blob/main/likelihood/pantheon_plus/pantheon_plus_shoes.py) supplies a separate convention cross-check.

Use `zHD>0.01`, `m_b_corr`, and the corresponding principal submatrix of the 1701-by-1701 covariance, preserving row order. The matrix file's first scalar is its dimension, followed by row-major entries. Keep repeated lightcurve measurements and their off-diagonal covariance. The probe reports row count and literal distinct CID count separately; CID aliases are not resolved, and neither count is an iid sample-size claim. Do not use SH0ES-calibrated distance moduli or their plotted diagonal errors. A free intercept absorbs absolute luminosity and H0 scale; neither is estimated here.

For flat geometry use

    f_i = 5 log10[(1+zHEL_i) chi(zHD_i)],
    chi_dS=z, chi_EdS=2[1-(1+z)^(-1/2)],
    chi_LCDM(z;Omega)=integral_0^z du/sqrt[Omega(1+u)^3+1-Omega].

The luminosity prefactor and radial integral use different redshift columns. Peculiar-velocity corrections, lensing, population/selection and intrinsic scatter already contribute through the published product; they are not independently certified by our Cholesky test. In particular the release documents a fiducial-LCDM redshift-to-magnitude uncertainty and simulation-based brightness bias corrections. This is no complete raw marked-Poisson or Cox calibration.

## Exact profiling and a fixed-pair discrimination theorem

Let C be fixed positive definite, y the corrected magnitudes, and 1 the constant vector. Define

    P=C^-1-C^-1 1 (1^T C^-1 1)^-1 1^T C^-1,
    b_i=[1^T C^-1(y-f_i)]/[1^T C^-1 1],
    chi_i^2=(y-f_i)^T P(y-f_i).

These follow by differentiating the quadratic in the one intercept. P1=0 and PCP=P. With TWO FIXED shapes, v=f1-f0,

    D²=v^T P v, T=v^T P[y-(f0+f1)/2], chi0²-chi1²=2T.

Under y=b1+f_i+Normal(0,C), T has mean minus/plus D²/2 and variance D². If D>0, threshold zero has error Phi(-D/2) under either shape; D=0 means the shapes differ only by an intercept and are indistinguishable. This theorem remains true with correlated or repeated measurements when their stated joint C is the actual covariance. It does NOT apply unchanged after choosing f from the same data. The optimized LCDM curve is therefore a reproducibility/goodness-of-fit control, not one of the fixed-pair Gaussian power hypotheses. Its profile Delta-chi²=1 interval is reported under the fixed likelihood, not a calibration-free confidence interval. Nominal degrees of freedom assume the stated Gaussian model; chi-square values alone are not universally calibrated p-values.

## Follow-through: exact unknown-drift sensitivity

Put w=Pv. If an unmodeled fixed magnitude drift delta has max|delta_i|<=beta, then

    |w^T delta| <= beta ||w||_1,

with equality at delta_i=plus/minus beta sign(w_i). Thus a fixed-pair conditional error bound is Phi[-D/2+beta||w||_1/D]; it loses a positive separation guarantee at beta=D²/(2||w||_1). The measured sign of T cannot reverse under that box when beta<|T|/||w||_1. These are computed requirements on an additional calibration envelope, not measured bounds on it.

For a completely unrestricted evolution vector, delta=v-c1 exactly maps one mean to the other. The minimum one-sided max norm is osc(v)/2, achieved by centering at the midpoint of max/min v. If each model may vary independently within the same symmetric box, the two finite mean classes overlap iff osc(v)<=4beta. This is the finite released-row consumer of K2352, retaining covariance and actual redshifts. No amount of precision in this release removes unconstrained evolution. The probe constructs the exact mean-mimic and extremal box direction, rather than merely warning about nuisance.

## Numerical result and interpretation

There are1590 selected lightcurve rows and1473 distinct literal CID strings. The fit gives Omega_m=0.33157578 with profile Delta-chi²=1 interval[0.31360802,0.34999852], chi²=1402.91913 for nominal1588 degrees of freedom. This approximately reproduces the published reference rather than claiming bitwise agreement with the original sampling pipeline. Fixed dS and EdS give chi²=2059.86945 and2101.14554; both are substantially worse than the fitted control. Their difference is-41.27609, while a worst-case additional magnitude drift of about0.00219311 can reverse their observed ranking. The conditional pair-separation radius is0.14157274; these different radii answer different questions. The tiny Gaussian classification error assumes one extreme endpoint generated the data and is NOT confidence that dS describes the observed data. The report stores its logarithm to avoid rounding a very small nonzero probability to zero.

## Released covariance-variant follow-through

The actual published STATONLY matrix retains off-diagonal intrinsic-scatter covariance between repeat observations; it is not the deliberately incorrect diagonal-only control. Repeating the same profiled fit with that matrix gives Omega_m=0.34783709, chi²=1484.10550, and extreme-pair Delta-chi²=-31.61012. The main full-covariance values are0.33157578,1402.91913 and-41.27609. This is a concrete sensitivity to the release's treatment of systematic uncertainty. The corrected mean magnitudes and bias model remain unchanged; dropping systematic covariance is not a more accurate analysis or a calibration-free fit. Chi-square values across different covariance choices are not likelihood rankings, since their normalization/log determinants differ. Full statistical-plus-systematic covariance remains the operative result. Both variants leave the unrestricted-evolution ambiguity intact.

## Reproduction and controls

Save the three pinned inputs under any scratch directory as `data.dat`, `covariance.cov` and `statonly.cov`; no external dataset is vendored. Run with Python, NumPy and SciPy:

    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python tests/channel-swings/k2355_released_supernova_shape_probe.py --data-dir /absolute/scratch/path

The committed report records package versions, hashes, selected counts, optimum/interval, all fit values and drift radii. Controls test endpoint quadratures, 32/64/128-node convergence, a separately factorized row permutation, intercept shifts, Delta-chi² identity and a broad published-fit reproduction window. Altered diagonal covariance and incorrect redshift use produce different answers; this is explicit sensitivity, not new science from deliberately wrong inputs. Standard double precision and quadrature convergence are numerical evidence, not interval-certified cosmology. The next substantive step is a population/selection robustness analysis with actual simulation variations or a source-derived model family using the same observation interface, not another arbitrary narrow-scatter fixture.
