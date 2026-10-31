---
title: "K2370 Potential rates recover the dust state and constrain every seed"
status: active_research
doc_type: exploration
created: "2026-10-31"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematics or numerical evidence; no native GU or hardware certification
scripts:
  - tests/channel-swings/k2370_potential_jet_density_identity_probe.py
---

# K2370 Potential rates recover the dust state and constrain every seed

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
result: K2370
carrier: four-state constrained scalar/dust Fourier mode on the K2364/K2367 sourced fit LAYER=toy CHIRALITY=N/A
pairing: declared real model-field coordinates with positive semidefinite statistical covariance ON=declared_carrier
real_structure: real coefficients and conjugate Fourier reality pairing
grading: density, two potentials and Einstein-time derivatives are distinct readouts
action_owner: repository-construction -- quadratic metric f(R) and conserved Jordan dust
target: all-seed density consistency and snapshot covariance saturation MAP-TYPE=evaluation
```

## Object and reused evidence

Keep the SAME positive-F quadratic metric action, conserved Jordan dust without radiation, fitted interior background and ruler of K2364/K2367. K2308 already owns the constrained scalar/dust system. K2314's compensated density identity still contains unobserved scalar momentum and dust velocity; K2327's projective covariance test explicitly freezes one seed. Here the new construction eliminates those hidden variables by the time derivatives of the two existing potential readouts and characterizes the enlarged arbitrary-four-mode snapshot covariance model. Do not rebuild perturbation equations or claim a new field theory.

Read the mandatory comparator routing before any source inference. SC-COS-50/51/54 ASSERTS retain their source meanings; the source's connection displacement is distinct from this metric action. LT-GR2e v0.263 remains NEEDS. This is a backward demand on a physically completed realization of the fitted history, not source acceptance.

Carrier: the fixed nonzero real Fourier mode with conjugate reality pairing, constrained state X=(Phi,chi,pi,v); pairing: declared normalized real model-field readouts; action owner: supplied quadratic metric f(R) with minimally coupled Jordan dust; time: dimensionless Einstein time t=H_* t_E; b=-1/sqrt6, d>0, Q=kbar^2/a_E^2. No measured tracer, lightcone, selection or derivative estimator is supplied.

## 1. Exact potential-rate state recovery

Define lensing-potential sum L=2Phi and slip Z=2b chi. Their derivatives are with respect to t above, NOT observed redshift or a photon lightcone coordinate. K2308 gives

    Ldot=-H L+u Z/(2b)-d v,
    Zdot=2b pi.

Consequently

    Phi=L/2, chi=Z/(2b), pi=Zdot/(2b),
    v=[-Ldot-H L+u Z/(2b)]/d.

The matrix mapping X to (L,Z,Ldot,Zdot) has determinant 8b^2 d, nonzero whenever b and d are nonzero. Neither H nor u is divided by; scalar turning points and an Einstein-frame H=0 point do not obstruct this algebraic recovery. This is recovery from model fields and their rates, not a demonstration that surveys measure those four quantities.

## 2. Exact all-seed density identity

The Hamiltonian constraint and Jordan-frame density readout give

    d delta_J=-(2Q-u^2)Phi-(3Hu+V'+4bd)chi+3Hd v-u pi.

Substitution of the recovered variables cancels the 3Hu Z term and yields

    2d delta_J+(2Q-u^2+6H^2)L+6H Ldot
              +(V'/b+4d)Z+(u/b)Zdot=0.                 (1)

No quasi-static approximation, primordial spectrum or small scalar-velocity denominator was used. More directly, before imposing the constraint let P=dotPhi and

    C=QPhi+3H(P+HPhi)
      +(u pi-u^2 Phi+V'chi+d(n+bchi))/2.

The left side of (1), with delta_J=n-3bchi, is exactly 4C. Thus it is a constraint consistency relation, not an independent new dynamical equation. Together with potential-rate recovery it is a precise seed-independent check of the fixed model-field realization. It may distinguish supplied models only after fixing their coefficients, field identifications and time convention. It is NOT yet a null statistic for observations.

For any random initial state satisfying the same linear model, every realization satisfies (1), hence the five-readout covariance has this background-dependent null vector. Independent measurement noise or a projected/windowed observation changes that covariance and must be derived explicitly; arbitrary windows do not preserve the local derivative relation automatically.

## 3. Why three simultaneous fields alone do not fix the initial covariance

At a time with H!=0, the three-readout map R: X -> (delta_J,L,Z) has an explicit right inverse E. For arbitrary (delta,L,Z), set

    Phi=L/2, chi=Z/(2b), pi=0,
    v=[d delta+(2Q-u^2)L/2+(3Hu+V'+4bd)Z/(2b)]/(3Hd).

Then R E=I3. The actual K2367 present time satisfies H=1.6125138743...>0. More generally the map has rank3 whenever (H,u)!=(0,0); the displayed right inverse selects the H!=0 chart only. The potential-rate construction above needs neither condition.

Let T be the invertible four-state transfer to that time. For ANY positive semidefinite target covariance Sigma of these three real mode readouts, choose

    D=T^-1 E, C_initial=D Sigma D^T.

This is positive semidefinite and (R T) C_initial (R T)^T=Sigma. Thus an unrestricted covariance of all four initial scalar/dust modes can absorb every three-channel covariance at one fixed mode and time. This is a larger nuisance class than K2327's one-seed power: the old projective-identifiability result remains correct in its smaller class. Real initial amplitudes can also be recovered deterministically. This is a formal linear-model statement: physical linear perturbations require appropriately small amplitudes, and the construction is homogeneous under covariance rescaling. This is a finite-mode existence statement, not a uniform finite-energy spectrum, Gaussianity assumption, source-selected primordial law or arbitrary-covariance repair across multiple times with one frozen initial covariance.

Equation (1) supplies the constructive way forward: common potential rates (or a properly derived multi-time observation) introduce a seed-independent consistency constraint. Another possible route is an independently justified restricted initial covariance; merely choosing one is calibration, not a prediction.

## 4. Actual fitted-history consumer and controls

The companion probe reads K2367's frozen full transfer matrices at k r_d=.1,1,10 and its present background; it does not rerun the ODE or distance fit. At today the recovery determinant is 3.02381051975. Multiplying the five-readout map and null row through all FOUR columns of each stored transfer gives scaled residuals approximately 4.80e-17,6.45e-17,1.59e-16. This checks all initial modes by linearity, rather than only K2367's two illustrated seeds.

An explicit positive 3x3 target covariance is pulled back through each stored transfer and reproduced using 70-digit finite matrix arithmetic. This checks a numerical illustration of the analytic congruence construction; the additional precision does not upgrade the original ODE accuracy or certify a continuum. Floating-point covariance multiplication in the ill-conditioned high-k coordinates initially lost accuracy; retaining factorized covariance and using high precision resolves that numerical seam. No inference is drawn from those failed development checks.

Five changed-equation controls fail the SAME symbolic constraint identity: omit the H^2 term, flip the lensing-rate sign, omit the slip matter coefficient, omit the slip-rate term, or omit dust velocity from the momentum equation. The exact symbolic identities are the proof; the stored matrices and finite arithmetic are the actual-fit consumer.

Next required physical input is a jointly typed observation operator for density, both potentials and their rates (including observer/lightcone/selection, time conversion and noise), or an independently justified initial covariance restriction and shared multi-time likelihood. Do not relabel (1) as an observed null or repeat an unconstrained growth fit. No source, ledger, canon, empirical or stability verdict changes.
