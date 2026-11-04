---
title: "K2532 Finite drift forecast exposes the fitted history scale freedom"
status: active_research
doc_type: exploration
created: "2026-11-04"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional numerical forecast and exact nuisance algebra; no empirical exclusion or native GU prediction
scripts:
  - tests/channel-swings/k2532_finite_drift_forecast_probe.py
---

# K2532 Finite drift forecast exposes the fitted history scale freedom

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
result: K2532
carrier: K2364 fixed sourced quadratic metric FLRW history and five comoving forecast bins LAYER=toy CHIRALITY=N/A
pairing: declared diagonal forecast covariance and common scale/velocity offset ON=declared_carrier
real_structure: real positive-U positive-F numerical history and real observational parameters
grading: in-sample distance fit, forecast discrepancy, dimensional calibration and empirical evidence remain distinct
action_owner: repository-construction -- metric f(R), not native connection displacement
target: one fixed realization under joint nuisance profiling MAP-TYPE=evaluation
```

## Result and backward demand

[K2364](k2364-sourced-shared-history-2026-10-31.md) supplied a sourced quadratic metric history fitting the declared supernova/BAO distances. [K2528](k2528-observation-forecast-feasibility-2026-11-04.md) found that an actual drift forecast does not supply the continuous information required by K2526's sufficient certificate. [K2530](k2530-finite-drift-envelope-2026-11-04.md) built conditional finite-information envelopes, still requiring an independent regularity input.

A different, cheaper test is now executed: the action itself predicts a finite drift vector. The chosen forecast's comoving-absorber premise replaces neither source motion in general nor observed continuous bands. It defines a narrower supplied comparison in which no interpolation premise is needed. The existing distance fit does not select a dimensional Hubble scale. Holding that scale equal to the reference gives a large forecast discrepancy; freeing it almost erases the discrepancy. The released calculation identifies the corresponding ruler and quantifies the missing external scale information.

SC-COS-50/51/54 ASSERTS retain their exact source meanings. The tested scalar metric action remains a comparator, not native connection displacement. LT-GR2e remains NEEDS and ledger0.263 is unchanged. No measured exclusion, family rejection, confidence level, GU prediction or novelty is claimed.

## 1. Fixed dimensionless action-forward extension

Do not refit the DIMENSIONLESS alpha, rho, present curvature or dust fraction. Reuse the rounded interior K2364 witness:

    alpha=775.88047141, rho=8540.41820373,
    U0=2, P0=.3175541986, Omega_d=.3, Omega_r=0.

In s=3log(1+z), h=U^(2/3),

    U_s=P,
    P_s=P-alpha/(36U^(1/3))+(rho+2q0 exp(s))/(216U^(5/3)),
    F=alpha+12U^(1/3)(U-P), q0=3F0 h0² Omega_d,
    E(z)=h(z)/h0.                                      (1)

The action is f(R)=alpha R+R²/2-rho. Varying H0 below varies H*=H0/h0 and hence the dimensional action coefficients and densities corresponding to these fixed dimensionless values. This is the still-uncalibrated scaling family, not one independently calibrated dimensional action. Its original00 identity is

    3Fh²-q-(F-alpha)²/4-rho/2-9h²F_s=0.                (2)

The exact algebra in the probe verifies (2) from (1). Omitting dust force leaves residual -q in the original equation. The new extension reaches z=4.5, beyond the previous z=2.33. Tight DOP853 and independent RK45 agree to4.82e-11 in U,P,chi on2001 sample nodes. Minimum sampled U=2 and F=797.2474671; F(4.5)=974.9754431. The scaled original00 residual is2.20e-15. This residual uses the same RHS and chain rule: it checks original-row algebra at sampled states, not the dense trajectory interpolation defect. Independent-solver agreement is the trajectory convergence evidence. These are converged numerical observations, not interval domain or continuum error certificates. No null/kill conclusion is certified by floating-point sampling.

## 2. Actual forecast inputs and conditional vectors

Use [Marques, Martins and Alves2023, section2, equations1--3](https://arxiv.org/pdf/2305.01446): 20 years, S/N3000, six quasars per bin at z=(2,2.5,3,3.5,4.5). The source assumes absorbers follow cosmological expansion. Its marginal statistical uncertainty formula is

    sigma_v=1.35(3000/2370)^(-1)(6/30)^(-1/2)
            ((1+z)/5)^(-lambda) cm/s,
    lambda=1.7 for z<=4, .9 above4.

The resulting sigmas are (5.683145,4.372997,3.484921,2.852552,2.188731) cm/s. We ADOPT independent-bin statistical covariance diag(sigma²) as the forecast approximation; these marginal errors do not certify the full instrument/tracer covariance. The reference is flat LCDM with Omega_m=.3 and supplied H0=70 km/s/Mpc. No realized instrument precision is inferred. A Julian year=31557600 seconds is used.

For d_i=1-E(z_i)/(1+z_i), A=c H0 T, the supplied signal is v=A d. This is the source forecast's first-order expansion in the observing baseline, not exact finite20-year evolution. With the same H0=70:

| z | Fixed witness cm/s | Reference cm/s |
|---|---:|---:|
|2|-.868277366|.479614999|
|2.5|-5.092893352|-2.241010486|
|3|-9.685816282|-4.946386845|
|3.5|-14.46750469|-7.583702317|
|4.5|-24.36416034|-12.59822217|

This calculation uses a fixed model and a specified reference mean, not a new dataset. It does not reuse the same-momentum moving-candle construction as if it described absorption tracers.

## 3. Execute the missing-scale and common-calibration repair

Let y be the reference vector and W=diag(sigma^-2). Compare y with A d+b1, retaining ONE scale A>0 and ONE common velocity offset b. Set X=[d,1]. When X has full column rank, the unconstrained optimum is

    theta_hat=(X^T W X)^(-1)X^T W y,
    Q=I-X(X^T W X)^(-1)X^T W,
    loss=y^T W Q y.                                   (3)

Q²=Q, QX=0 and Q^T W=WQ follow by multiplication. Thus y=X theta_hat+Qy is W-orthogonal and (3) is the global minimum. If A_hat<=0, project to the A>=0 boundary, optimize b there, and report only an infimum if A is strictly positive. Both actual fits below have A_hat>0.

| Nuisances | H0 km/s/Mpc | b cm/s | Quadratic forecast loss |
|---|---:|---:|---:|
|Same supplied scale, no offset|70|0|37.05271561|
|Fixed70, free common offset|70|profiled|6.726928217|
|Free scale, no offset|36.19735582|0|.03636582820|
|Free scale and common offset|37.68877761|.4251793616|.01853692600|

These losses are squared covariance distances between specified forecast means. They are not empirical chi-square significance or a likelihood-ratio test of the entire quadratic family. Holding H0=70 would conceal a degree of freedom left by the previous distance fit. Freeing it is a legitimate repair of THIS comparison; whether that scale is physically admissible requires independent information.

## 4. Released ruler and scale-information consequences

The same fitted BAO parameter lambda=48.4745294 obeys lambda=c/(H_* r_d) and H0=H_*h0. Consequently

    H0 r_d/c=h0/lambda.                               (4)

The three rows imply r_d=(140.2476927,271.2170065,260.4843965) Mpc respectively. This is not a sound-horizon calculation: the supplied dust-only late history has no early-universe ruler construction. Changing H0 together with this free ruler leaves its dimensionless BAO and intercept-profiled supernova predictions unchanged. We reuse that algebraic scaling and the pinned prior likelihood; no large distance covariance replay or new fit is counted in this section; section5 below executes the new calibrated consumer.

For a useful quantitative wake, remove the weighted constant mean: d_c=d-1(1^T Wd)/(1^T W1), and similarly y_c. Let K=(cT)^2 d_c^T Wd_c in consistent H0 units. The fixed-shape loss after profiling b is exactly

    L(H)=L_min+K(H-H_hat)^2.                           (5)

A separately SUPPLIED Gaussian calibration centered on70 with standard deviation sigma_H gives

    H_joint=(K H_hat+70/sigma_H²)/(K+1/sigma_H²),
    L_joint=L_min+K(70-H_hat)^2/(1+K sigma_H²).          (6)

The report evaluates sigma_H=1,5,10,20 as sensitivity scenarios, not measured priors. It does not assume that a standard-model-dependent external H0/r_d inference transports unchanged into this action. A physical calibration must name its model dependence and covariance before (6) becomes an observation test.

The residual r=Qy gives a designed contrast c=W r with c^T d=c^T1=0 and (c^T y)^2/(c^T diag(sigma²)c)=L_min. This is a model/reference-designed forecast statistic, not a held-out statistic chosen independently of those predictions. Adding common-mode covariance tau²11^T does not change the loss after a free common offset: minimizing over that offset removes the sole affected direction. An explicit tau=10cm/s replay checks this case. Arbitrary cross-bin errors are not thereby harmless. Allowing an independent offset in every bin makes X full row rank and annihilates all drift information; the exact contrary fixture demonstrates that loss of identifiability.

## 5. Executed calibration: the released Cepheid rows break the scale repair

The missing dimensional information is present in a part of the already pinned release that K2355/K2364 did not use. We now consume it, rather than leave an abstract prior as the next task. Follow the [pinned primary Pantheon+SH0ES likelihood](https://raw.githubusercontent.com/PantheonPlusSH0ES/DataRelease/c447f0fea703fcd0fff57de5000947b5ca81286b/Pantheon%2B_Data/5_COSMOLOGY/cosmosis_likelihoods/Pantheon%2BSH0ES_cosmosis_likelihood.py) and [column/covariance definitions](https://raw.githubusercontent.com/PantheonPlusSH0ES/DataRelease/c447f0fea703fcd0fff57de5000947b5ca81286b/Pantheon%2B_Data/4_DISTANCES_AND_COVAR/README): select zHD>.01 OR IS_CALIBRATOR. Calibrator rows use CEPH_DIST as a distance modulus; all other rows use the model distance. One absolute magnitude M is shared. Preserve repeated rows and the full selected covariance; Cepheid uncertainty is already included.

The two exact input SHA256 values are unchanged from K2355 and recorded in the report. There are1657 selected lightcurve rows:77 calibrator rows representing43 literal CID strings, and1580 noncalibrator rows. These are correlated observations, not an iid count. Ten previously selected zHD>.01 rows are calibrators and now take the calibrator branch; the primary likelihood's precedence matters.

Let H_ref=70 and let chi=int dz/h from(1). Define t_i=CEPH_DIST for calibrators and

    t_i=5log10[(c/H_ref)(1+zHEL_i)h0 chi(zHD_i)]+25

otherwise. For n_i=1 only on noncalibrators, r=m_b_corr-t has model

    r=M1+k n, k=-5log10(H0/H_ref), B=[1,n].             (7)

Fit theta=(M,k) by the same full-covariance GLS formula as(3); now Cov(theta)=(B^T C^-1 B)^-1. With calibrators removed, n=1 and the design has rank1: the old shape-only degeneracy is recovered as a real contrary control. With the actual rows, rank is2. Profiling M gives the exact fixed-shape relation

    Delta chi_SN²(H0)=[k(H0)-k_hat]²/Cov(theta)_kk.      (8)

The raw calibrated submatrix has an absolute rounding asymmetry up to3e-8; the previous noncalibrator subset was symmetric. We explicitly use (C+C^T)/2, and rerun the fit using each triangular symmetric completion. Each changes M or k by less than3.92e-8 and chi_SN² by2.54e-6. No input bytes are altered and no covariance error is hidden by Cholesky's triangle convention.

At the fixed dimensionless sourced shape:

- H0=73.68059845 km/s/Mpc; M=-19.24055087.
- The conditional profile-Delta1 interval is[72.67814259,74.69688126]; local linear sigma_H=1.00933776.
- Joint released SN/Cepheid quadratic loss1459.58361287; the same BAO scale implies r_d=133.24183972Mpc.
- The drift-only repair H0=37.68877761 raises this joint SN loss by2394.813178 at the fixed shape, even after profiling M.
- A fixed LCDM shape Omega_m=.33157578 gives H0=73.53461875, M=-19.24407911 and loss1452.01612164 as a separate release-convention check. It is not a new optimized cosmological fit or model-selection claim.

This is a RELEASED-LIKELIHOOD DIAGNOSTIC conditional on the fixed shape and transport of Cepheid/stellar calibration, SN luminosity standardization, peculiar velocities, bias/selection corrections and covariance into the comparator. The mean-product uncertainties include assumptions inherited from the release. The fixed-shape parameters were chosen with the earlier SN/BAO sample, so these numbers are not independent held-out evidence for that shape. The calibration row selection is new to this calculation; no native gravity-dependent stellar calibration is derived.

Equation(8) replaces the uncalibrated supernova likelihood. We do NOT add a separate SH0ES scalar prior on top of the same supernova data. The BAO shape/ruler evidence is reused, not replayed as an independent new dataset.

## 6. Execute the joint future-forecast consumer

Under the explicit hypothetical assumption that the five future drift bins have the reference mean y and independent forecast errors from section2, add their loss to(8), then optimize H0. The existing SN covariance is used once; there is no extra scalar H0 prior. At the calibrated SN optimum the drift loss is45.55262385 without an offset and8.34229111 after profiling one offset. Joint optimization yields:

| Future calibration assumption | Joint H0 | SN loss increase | Future drift loss | Added total loss |
|---|---:|---:|---:|---:|
|No velocity offset|72.51054334|1.36547043|42.75535691|44.12082735|
|One free common offset|73.44762562|.05344567|8.23488157|8.28832724|

These totals use actual current calibration data plus HYPOTHETICAL future drift means, not a realized empirical rejection. They quantify why the scale-only forecast repair no longer works within the released calibrated fixed-shape likelihood, and why velocity-offset calibration remains consequential even after scale calibration. For fixed shape the scalar objective is A log²(H/H_SN)+K(H-H_d)²+C with A,K>0 and, in both branches, 0<H_d<H_SN. Its derivative is negative below H_d and positive above H_SN; on that bracket its second derivative is 2A[1-log(H/H_SN)]/H²+2K>0. Hence there is exactly one global minimum for H>0. A bracketed root solver locates it numerically and checks its derivative. This certifies the scalar optimization structure, not a global cosmological-family fit or confidence-calibrated exclusion. Independent per-bin offsets would still erase the drift information.

## Acceptance and frontier

Exact projection/original00 algebra, numerical trajectories/GLS/profile evaluations and contrary controls are separate evidence kinds. The calibrated release replays with independent trajectories; original00 residual is algebraic consistency, not an interval certificate. No external-expert, proof-assistant, empirical GU or novelty certification.

Reproduce using NumPy/SciPy/SymPy with one BLAS thread and the two pinned K2355 files, named data.dat and covariance.cov:

    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python tests/channel-swings/k2532_finite_drift_forecast_probe.py --data-dir /absolute/scratch/directory

The strongest observation successor is a joint dimensionless-parameter refit under this calibrated likelihood plus the same BAO consumer, then its held-out drift/growth test with explicit instrument nuisance model. A family verdict also requires calibration/selection transport robustness; repeatedly retesting only this frozen shape or inventing independent calibration would not supply it. On the native side, mixed-source response remains independent. Neither result changes source or ledger status.
