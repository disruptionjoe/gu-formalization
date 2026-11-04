---
title: "K2534 Joint calibrated shape refit and held-out drift repair"
status: active_research
doc_type: exploration
created: "2026-11-04"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional numerical likelihood witnesses and exact nuisance/normalization identities; no family exclusion or native GU prediction
scripts:
  - tests/channel-swings/k2534_calibrated_family_refit_probe.py
---

# K2534 Joint calibrated shape refit and held-out drift repair

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
result: K2534
carrier: supplied four-dimensional flat FLRW quadratic metric action with conserved dust and shared calibrated distance data LAYER=toy CHIRALITY=N/A
pairing: released correlated Cepheid/SN Gaussian covariance and independent BAO covariance ON=declared_carrier
real_structure: positive real expansion and F branch, real positive scale and ruler
grading: exact algebra, numerical trajectory, statistical fit and source prediction remain distinct
action_owner: repository-construction -- quadratic metric cosmology comparator with Omega_d=.3 and Omega_r=0
target: joint shared shape calibration and hypothetical held-out drift MAP-TYPE=evaluation
```

## Decision and scope

The fixed-shape discrepancy in [K2532](k2532-finite-drift-forecast-2026-11-04.md) does not survive as a strong test of this whole comparator family. A third numerical basin gives calibrated SN+BAO loss1461.82011, below the old shape's1470.18323. At its calibrated H0=73.6279, hypothetical ANDES drift loss is3.5500 with zero offset, or0.8000 with a fitted common offset; the old-nearby basin has45.6342/8.3181. These are finite search witnesses, not global minima, empirical drift observations or confidence-level exclusions. The future mean is still supplied flat LCDM with Omega=.3,H0=70; it is not measured truth.

SC-COS-50 ASSERTS the conditional variable-dark-energy demand, SC-COS-51 ASSERTS the displacement/VEV claim, and SC-COS-54 ASSERTS the two-movable-fields claim at the source record's stated scope. None supplies this metric quadratic action, stellar model, photon transport or matter normalization. LT-GR2e and ledger0.263 remain unchanged; all fitting assumptions remain conditional. This does not refute the source or certify its cosmology.

## 1. Shape variables and original equations

Reuse [K2364](k2364-sourced-shared-history-2026-10-31.md)'s sourced equation, s=3log(1+z), U_s=P and

    P_s=P-alpha/(36 U^(1/3))+(rho+2q0 exp(s))/(216 U^(5/3)),
    F=alpha+12 U^(1/3)(U-P), q0=3 F0 U0^(4/3) Omega_d.

Set x=U/U0, y=P/U0, a=alpha/U0^(4/3), b=rho/U0^(8/3). Then

    x_s=y,
    y_s=y-a/(36x^(1/3))+
        [b+6(a+12(1-y0)) Omega_d exp(s)]/(216x^(5/3)),
    E=H/H0=x^(2/3).

This substitution proves U0 is a normalization redundancy for this history; a new independent U0 fit would duplicate shapes. We fix U0=2 and Omega_d=.3, Omega_r=0. Varying Omega or the source/stellar assumptions remains a different comparison, not silently exhausted by three parameters.

The original00 equation is checked on each new witness with Fs obtained from this force, alongside independent integrator comparisons. This checks algebraic original-row consistency; it is not an independent numerical derivative-defect or interval proof.

## 2. One common calibrated fit per shape

The pinned Pantheon+SH0ES release and hashes are reused from K2532. Select zHD>.01 OR IS_CALIBRATOR,1657 rows including77 calibrator rows. Calibrator distance has precedence even when that row passes the redshift threshold. For noncalibrators the model uses the same shape chi and the release's zHEL prefactor. The design columns are1 and the noncalibrator indicator. They profile shared absolute magnitude M and k=-5log10(H0/70) using the complete symmetrized covariance; its original asymmetry is bounded by3.1e-8. The covariance-rounding sensitivity controls in unchanged K2532 are reused, not recounted.

For whitened residual r and design X, theta=(X^T X)^-1 X^T r. The residual projector is idempotent and annihilates exactly those common nuisances. Removing calibrators collapses these two columns to rank1; independent row offsets erase all information. No additional scalar SH0ES prior is added over these rows.

The unchanged13-coordinate BAO release from K2277/K2364 profiles one positive amplitude lambda=(v^T y)/(v^T v). The dimensional ruler is r_d=c U0^(2/3)/(H0 lambda); it is free, not a CMB early-universe prediction. The SN and BAO Gaussian factors are treated as independent supplied likelihoods. Cross-survey covariance, altered stellar physics, luminosity/selection effects and tracer applicability are not derived.

## 3. Search, witnesses and held-out consumer

Three Nelder-Mead starts in log(alpha),log(rho),P0 retain the two old basins and add a large-alpha second-jet seed. The script records starts, safeguard domain, termination and evaluations; finite termination never certifies global optimality. The exact report replays rounded witnesses independently with DOP853 and RK45. Separate SN, BAO, H0, ruler and sampled states are compared, including the z4.5 forecast extension. Positive U,F tests are numerical with event detection, not certified continuum inequalities.

| basin | alpha | rho | P0 | SN+BAO | H0 | r_d Mpc | drift loss: zero/free offset |
|---|---:|---:|---:|---:|---:|---:|---:|
| prior interior |772.398289|8497.5033|.321172005|1470.17153|73.6755|133.250|45.6342 /8.3181|
| near rho boundary |69.6805616|9.37e-10|.892602067|1494.65274|72.4947|135.870|72.8088 /14.4440|
| large-alpha basin |9017.14629|97041.2841|.272158521|1461.82011|73.6279|137.016|3.5500 /.8000|

The drift bins,20-year baseline and uncertainty prescription are the same hypothetical ANDES design as K2532. Drift was excluded from all shape searches. The free-offset score fits that additional future nuisance only; it does not refit the calibrated shape or H0. Conditional discrimination can weaken through a family refit even when a specific low-H0 repair is ruled out by calibration.

## 4. Execute the Einstein-direction control

[K2295](k2295-quadratic-expansion-reconstruction-2026-10-30.md) excludes exact dust LCDM for a nonzero quadratic coefficient, but does not prove uniform separation as the Einstein coefficient grows. A useful exact seed matches two present derivatives:

    y0=3 Omega/4,
    b=6a(1-Omega)-(81/2)Omega²-6(12-9Omega)Omega.

At Omega=.3 these are y0=.225,b=4.2a-20.385 and x_ss(0)=.208125. The probe checks both derivatives against x_LCDM=(Omega exp(s)+1-Omega)^(3/4). It also substitutes the entire proposed LCDM curve into the original00 equation. With t=exp(s), the residual is

    q_required-q=(1-t)[3(12-9Omega)Omega+(81/4)Omega²(1+t)].

This is nonzero away from today at Omega=.3. Matching two jets is not solving the history. A numerical no-refit sequence alpha=10³,10⁴,10⁵ has maximum sampled |E-E_LCDM| over z0..2.33 of.23565,.031851,.00338095, independently replayed. It motivates a singular-limit/oscillatory-mode analysis; these three numbers do not prove a uniform asymptotic theorem.

## Evidence and next question

Exact normalization, common-nuisance projection and original-row residual arguments support the stated algebra. Search and trajectories are numerical evidence, kept separate from source provenance and report consistency. Independent review repaired an invalid initial jet control, separate-observable convergence, extended forecast verification and original-row evidence. No calibration data counts as held-out confirmation.

The fastest new discriminator is a family-level, applicability-qualified held-out growth/slip or drift statistic after proper shape uncertainty, or an analytic Einstein-limit bound excluding a proposed separation test. Repeating the fixed-shape H0 penalty or adding decimal precision does not answer it. A globally exhaustive fit, native action/Met(X) bridge and physical perturbation/readout are open.
