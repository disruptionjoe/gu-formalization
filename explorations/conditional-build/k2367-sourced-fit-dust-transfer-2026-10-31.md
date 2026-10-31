---
title: "K2367 The fitted material history has a coupled dust response"
status: active_research
doc_type: exploration
created: "2026-10-31"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematics or numerical evidence; no native GU or hardware certification
scripts:
  - tests/channel-swings/k2367_sourced_fit_dust_transfer_probe.py
---

# K2367 The fitted material history has a coupled dust response

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
result: K2367
carrier: constrained scalar and conserved dust perturbations of the fixed K2364 metric history LAYER=toy CHIRALITY=N/A
pairing: positive Einstein scalar kinetic form and declared finite coordinate readout ON=declared_carrier
real_structure: real background and complex Fourier amplitudes with reality pairing
grading: background, perturbations and observation are separate
action_owner: repository-construction -- quadratic metric f(R), minimally coupled Jordan dust, radiation absent
target: actual same-coefficient perturbation transfer and ruler-labelled Jordan response MAP-TYPE=evaluation
```

## Question, scope and reuse

[K2364](k2364-sourced-shared-history-2026-10-31.md) already fits conserved dust at chosen Omega=.3. [K2308](k2308-inhomogeneous-constrained-dust-transfer-2026-10-30.md) already derives the full constrained scalar-dust equations. The new calculation composes that existing operator with the actual interior fitted history; it does not derive a new perturbation theory or repeat the fit. Coefficients, initial background, dust fraction and fitted ruler stay fixed. No quasi-static or frozen-dust replacement is made.

SC-COS-50/51/54 ASSERTS keep their source meanings; LT-GR2e remains NEEDS and ledger0.263 unchanged. This conditional metric comparator is not the source connection displacement. The backward demand is that one distance-fit realization also supply its coupled material response. The response is not a calibrated growth likelihood, physical stability verdict, primordial mode selection or native prediction.

## 1. Normalize the same action and density

Use K2364's dimensionless alpha=775.88047141, rho=8540.41820373, U0=2, p0=.3175541986, Omega=.3, and fitted lambda=48.4745294. Let s=3log(1+z), h=U^(2/3), F=alpha+12U^(1/3)(U-p), q=q0 exp(s), q0=3F0 h0² Omega. Integrate the original U,p equations through z=2.33. Put c=F/F0, beta_run=-3F_s/F and

    a=e^(-s/3)sqrt(c), dt/ds=-sqrt(c)/(3h),
    H=h(1+beta_run/2)/sqrt(c),
    u=sqrt(3/2)h beta_run/sqrt(c), d=q F0/F²,
    V=F0/4 [1-2alpha/F+(alpha²+2rho)/F²],
    V'=F0/sqrt6 [alpha/F-(alpha²+2rho)/F²],
    V''=F0/3 [-alpha/F+2(alpha²+2rho)/F²].

Here t=H_* t_E, phi/M=sqrt(3/2)log(c), chi=delta phi/M, pi=dchi/dt and v=H_*v_E. H,u,d,V are normalized by H_*, M H_*, M²H_*², M²H_*² respectively; primes differentiate phi/M. If the physical action is C f/2, M²=C H_*²F0. Normalized units do not determine C,H_* or M. In particular d is q F0/F², not q/F². Today d0=3h0²Omega.

The scalar's constant dust coupling b=-1/sqrt6 is distinct from beta_run. The probe checks the Einstein equations 3H²=u²/2+V+d, dot H=-(u²+d)/2, dot u=-3Hu-V'-bd and dot d=(-3H+bu)d against independently differentiated background formulas. A normalized density error fails these checks.

## 2. Constrained system and fixed ruler labels

For Q=kbar²/a², use X=(Phi,chi,pi,v). K2308's four-dimensional reduced matrix is

    J[0]=(-H,u/2,0,-d/2),
    J[1]=(0,0,1,0),
    J[2]=(-4Hu-2V'-2bd+b(2Q-u²),
           -Q-V''+2u²+3bHu+bV',-3H+bu,-d(2u+3bH)),
    J[3]=(-1,-b,0,-bu).

Reconstruct the eliminated number perturbation using

    dn=-(2Q-u²)Phi-(3Hu+V'+bd)chi+3Hd v-u pi.

This chart divides by positive d, not by H or 2Q-u². Integrate dT/ds=(dt/ds)JT backwards from z=2.33 to today. Liouville's identity gives det T=a(initial)^4, since tr J=-4H and a(today)=1. The exact finite-k theorem comes from K2308; numerical transfer magnitudes here are basis-dependent evidence, not an invariant stability test or uniform-in-k estimate.

The distance fit supplies lambda=(H_* r_d)^-1 in c_light=1 units. Label modes by kappa=k r_d and set kbar=lambda kappa. Thus a free H_* rescaling cannot alter this dimensionless mode family. kappa=.1,1,10 are declared probes, not an inferred observed spectrum or a derivation of r_d.

## 3. Actual density and velocity consumers

The Jordan readouts are delta_J=n-3bchi, Phi_J=Phi+bchi, Psi_J=Phi-bchi, lensing sum=2Phi and slip=2bchi. At the initial redshift set chi=pi=0 and choose the two independent basis seeds (delta_J,v)=(1,0) and (0,1/sqrt(Q)). The constraint fixes Phi=d(3Hv-delta_J)/(2Q-u²); the probe verifies that this seed chart denominator is nonzero at each chosen mode. These unit columns are coefficients to be multiplied by a small perturbation amplitude, not claims that order-one perturbations are linear. This seed chart is optional and does not restrict the regular evolution theorem.

The report gives the full transfer, its singular values in the stated X coordinates, and today's density/lensing/slip for both seeds. It also evolves a changed equation omitting the beta²d scalar force: that is a rejected inconsistent implementation, not a second valid model. The altered scalar force fails the same Hamiltonian propagation test by the nonzero residual u b² d chi/2; merely obtaining a different transfer would not be a valid fault detector. Direct full-system identities and independent DOP853/RK45 replay distinguish this computation from fitting a desired growth curve.

The evaluated density outputs are:

| k r_d | Unit density seed: delta_J(today) | Unit velocity seed: delta_J(today) |
|---|---:|---:|
| .1 | 1.894719 | 1.577647 |
| 1 | 1.837301 | 29.474553 |
| 10 | 1.841443 | 296.425260 |

These are conditional responses in the specified basis. In particular the background does not select a unique growth factor. At k r_d=1, add -0.06233516696 times the velocity seed to the density seed: initial density remains one, today's density cancels, but lensing is approximately -1.24318e-6 and slip -1.51465e-4. The script constructs and checks this combination using the actual transfer. The linear ambiguity is exact; its displayed coefficients are numerical. All amplitudes may be scaled down together to stay linear. A source-selected velocity/covariance condition is needed to remove it; distances alone do not do so.

Two combinations are fixed by this same fitted realization: the trace-scalar scale m_trace r_d=sqrt(alpha/3)/lambda, and (rho_J0/M²)r_d²=3Omega(h0/lambda)². The first is not the full rolling constrained mass; the second is action-normalized matter, not a measurement of laboratory Newton's constant. Separate H_*,r_d,M and a primordial covariance remain unselected.

## Evidence and remaining condition

The companion checks exact symbolic reduction/constraint propagation, numerical independent background equations, both original and reduced perturbation equations, the determinant, independent integration, physical readouts and altered equations/normalizations. Positive sampled F is numerical evidence, not a continuum interval certificate. K2364's released distance likelihood is reused by hash; it is not rerun or counted as new evidence.

Supply a physical common initial covariance, ruler and selection model before comparing these responses with data. The finite response calculation closes the earlier missing application of the coupled dust system to this actual fit. It does not complete physical calibration, source ownership or nonlinear/continuum stability.
