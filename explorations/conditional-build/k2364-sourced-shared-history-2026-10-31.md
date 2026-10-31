---
title: "K2364 Sourced continuation of the shared cosmology witness"
status: active_research
doc_type: exploration
created: "2026-10-31"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematical or numerical result; no native GU or hardware certification
scripts:
  - tests/channel-swings/k2364_sourced_shared_history_probe.py
---

# K2364 Sourced continuation of the shared cosmology witness

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
result: K2364
carrier: positive-F quadratic metric FLRW histories LAYER=toy CHIRALITY=N/A
pairing: canonical metric action and comoving distance ON=declared_carrier
real_structure: real coefficients and real conserved-fluid histories
grading: background, scalar velocity and density response are distinct
action_owner: repository-construction -- quadratic metric f(R), not native connection distortion
target: actual material background and distance sensitivity MAP-TYPE=evaluation
```

## Scope and reused evidence

The question is whether the actual K2358 joint distance witness survives adding a declared conserved material load at fixed coefficients and present H,R. K2292 already supplies its sourced flow; K2295 already excludes exact dust-bearing LCDM for this quadratic class and constructs designer alternatives; K2361 already excludes unchanged-history retuning. None is rederived as a new result here. We compute the previously unevaluated sourced trajectories of the actual witness and derive a local distance discriminator and source tangent for their consumer.

SC-COS-50/51/54 ASSERTS retain their source meaning, LT-GR2e remains NEEDS, and ledger0.263 is unchanged. This scalar metric action is a conditional comparator, not the source's connection displacement. Supplied matter fractions are not inferred measurements. No GU prediction, empirical exclusion or perturbative stability follows. Section 6 adds a conditional in-sample refit.

## 1. Same present geometry, changed scalar velocity

Use s=3log(1+z), h=H/H_*=U^(2/3), f=alpha R+R²/2-rho. Keep K2358's rounded (alpha,rho,U0,p0)=(55.85236076,929.86045772,2,.4885325972). In the same dimensionless convention,

    U_s=p,
    p_s=p-alpha/(36U^(1/3))+(rho+2q)/(216U^(5/3)),
    q=q_d0 exp(s)+q_r0 exp(4s/3),
    F=12U^(1/3)(U-p)+alpha,
    chi_s=exp(s/3)/(3U^(2/3)), chi(0)=0.

Set q_i0=3F0 h0² Omega_i using the original present values once. Omega is an action-normalized chosen input, not a measured density estimate in a different gravity model. Fixing U0,p0 fixes h0,R0,F0 but does not fix dotF. The full00 constraint forces

    Delta p_s(0)=q0/(108U0^(5/3)),
    Delta F_s(0)=-q0/(9U0^(4/3)),
    Delta beta0=Omega_d+Omega_r, beta=-3F_s/F.

Thus a chosen dust fraction .3 changes the near-zero vacuum beta0 by exactly .3. The implementation checks full00 directly, not just this derived identity. Radiation contributes to full00 despite its zero trace.

## 2. An exact local shape consequence

Since h and its first z derivative match at today, the first nonzero change is

    Delta h_zz(0)=q0/(18U0²),
    Delta chi(z)=-q0 z³/(108U0^(10/3))+O(z^4)
               =-F0 Omega_total z³/(36U0²)+O(z^4).

This follows by differentiating h=U^(2/3) twice, using ds/dz=3/(1+z), and integrating the difference of 1/h. It proves local shape change for nonzero q0. A constant distance scale cannot remove it on an interval once the common leading z/h0 term fixes that scale. It is not a whole-interval sign theorem or exclusion at finitely many distances. Arbitrary evolution/selection functions remain outside this frozen comparison.

## 3. Actual finite-interval continuation and tangent

The companion evaluates vacuum, Omega_d=.01,.1,.3 and (.3,.0001) dust/radiation through z=2.33 without refitting. It reports h, chi, F and original-row residuals at declared redshifts. Tight DOP853/RK45 comparison supplies numerical convergence evidence. Floating-point positive F values are not interval certificates. K2292's integrating-factor theorem can turn a certified positive endpoint into a whole-path statement, but no endpoint enclosure is claimed here.

For q=lambda qbar, the independent source tangent (u,v,c)=partial_lambda(U,p,chi) starts at zero and obeys

    u_s=v,
    v_s=v+[alpha/(108U^(4/3))-5(rho+2lambda qbar)/(648U^(8/3))]u
          +qbar/(108U^(5/3)),
    c_s=-2exp(s/3)u/(9U^(5/3)),
    partial_lambda F=4(4U-p)U^(-2/3)u-12U^(1/3)v.

Centered finite differences around lambda=1 independently test this system with nonnegative source amplitudes. The tangent coefficient can change sign, so a global monotonicity claim is not inferred. Two altered-source solves omit matter force or tracefree radiation. Two separate algebraic scope controls exhibit the nonzero tangent and scalar-velocity shift that would be lost by freezing them; these are not executions of mutated tangent solvers.

## 4. Consumer and limits

The finite-interval outputs quantify precisely why the old vacuum distance likelihood cannot simply be reused after adding matter. The local cubic result is exact, the evaluated trajectories are numerical, and supplied densities have no observational certification. Section 6 supplies a jointly refitted sourced example; fluid perturbation/ruler/selection construction remains required. K2361's vacuum single-scalar transfer is not the material perturbation system: additional fluid density, velocity and entropy modes matter. Keeping a numerical F domain does not establish stability or source ownership.

Background equations: [De Felice and Tsujikawa](https://arxiv.org/abs/1002.4928). No novelty claim.

## 5. Released likelihood follow-through

The new material curves are passed through the SAME K2358 Pantheon+1590-row full covariance and DESI13-coordinate likelihood operators. Only the original supernova intercept and shared BAO ruler scale are profiled; alpha,rho,U0,p0 and the stated densities are fixed. Inter-survey covariance is still assumed zero. The raw release hashes and DESI embedded source hashes are checked; K2358’s vacuum result is reproduced before comparing material curves.

| Chosen Omega_d | Chosen Omega_r | SN chi-square | BAO chi-square | BAO ruler scale |
|---|---|---|---|---|
|0|0|1402.4661463|7.0062535|47.6912244|
|.01|0|1402.9464116|15.8900302|48.1478116|
|.1|0|1421.0395344|500.1700051|51.4184911|
|.3|0|1515.2808975|1945.9335561|56.2906439|
|.3|.0001|1515.3495473|1946.8540503|56.2930782|

For Omega_d=.3, chi(2.33) falls from .8165867703 to .6462986782 (relative change−.2085364328), h(2.33) rises from5.517594540 to9.693744879, and F endpoint is110.8467763. No F crossing is detected numerically. The largest independent-integrator state/tangent difference at the declared redshift nodes is3.28e-10; likelihood convergence is checked separately. Local cubic coefficient is−.1639673248, and the smallest checked z=.002 gives a finite-difference ratio .99905 to that asymptote.

This is a substantial failure of the unchanged-parameter continuation to retain the old BAO fit, not a confidence-calibrated rejection of the entire sourced quadratic family. Coefficients and present curvature may be refitted, and physical density/ruler/selection assumptions remain to be justified. The numerical chi-square values do not establish those assumptions or a native GU prediction.

Reproduce with `python tests/channel-swings/k2364_sourced_shared_history_probe.py --data-dir <pinned-release-directory>`; `--write` refreshes the report. Obtain the exact release files and hashes through [K2355](k2355-released-supernova-shape-2026-10-31.md). This new probe requires NumPy, SciPy and SymPy and uses no optimizer; the report binds all local dependencies and raw file hashes.


## 6. Same-launch repair: a fitted sourced existence witness

Refitting the same quadratic sourced family at the chosen Omega_d=.3, Omega_r=0 restores much of the distance fit. Minimize SN chi-square + BAO chi-square using Nelder-Mead in (log(alpha),log(rho),p0), with U0=2. Positivity of alpha,rho is imposed by exponentials; p0 is unrestricted. Reject F0<=0 before setting q_d0=3F0 h0²(.3), and reject failed integration or nonpositive endpoint F. The source normalization uses today's F0 once for each candidate. Changing alpha,p0 therefore changes physical q_d0: this fixes the supplied fraction, not physical dust density.

Both searches use the same released likelihood, DOP853 rtol2e-9, maxiter3000, xatol1e-8 and fatol1e-7, and terminate successfully. Two starts reveal different basins:

| Start (alpha,rho,p0) | Rounded witness (alpha,rho,p0) | Evaluations | SN chi-square | BAO chi-square |
|---|---|---|---|---|
|(55.85236076,929.86045772,.4885325972)|(69.86241292,2.175269709e-9,.895216134)|567|1416.5679760|28.5431085|
|(200,2000,.7)|(775.88047141,8540.41820373,.3175541986)|332|1409.2981487|10.5996204|

The first approaches the positive-rho boundary and is not an interior-optimum claim. The second is a finite interior existence witness with F0 about801.31746, endpoint F about851.02284 and profiled ruler about48.47453. The companion replays both rounded witnesses with tight DOP853 and independent RK45, compares likelihoods, checks full00 directly on1001 nodes, and checks positive U,F on that grid plus absence of detected F crossings. These support the numerical domain; they are not interval enclosures or a global optimum certificate. The script reproduces the witnesses and their likelihoods; search provenance is recorded, while optimization is not rerun by the ordinary probe.

The poor unchanged-parameter material curve is therefore repairable inside this chosen family. Neither basin is a held-out prediction, calibrated model selection, perturbative stability result, or native GU evidence. The next useful consumer must justify physical density and ruler/selection assumptions and include the coupled fluid perturbation system. Repeating the already completed joint refit is no longer the next frontier.
