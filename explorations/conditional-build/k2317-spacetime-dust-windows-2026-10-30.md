---
title: "K2317 Spacetime dust windows"
status: active_research
doc_type: exploration
created: "2026-10-30"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematics only; no native physical acceptance
scripts:
  - tests/channel-swings/k2317_spacetime_dust_windows_probe.py
---

# K2317 Spacetime dust windows

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
result: K2317
carrier: supplied Gaussian velocity seeds and spacetime test functions for the same healthy4D dust-scalar linearization LAYER=toy CHIRALITY=N/A
pairing: Gaussian covariance and spacetime window duality ON=declared_carrier
real_structure: conjugate Fourier modes on the three-torus and real time weights
grading: scalar density and potential readouts of constrained linear evolution
action_owner: repository-construction -- unchanged K2308/K2311 designer action and K2314 supplied statistics
target: time-filter and moving-window variance criteria MAP-TYPE=evaluation
```

## Frozen model and actual observation

Keep [K2314](k2314-windowed-dust-observables-2026-10-30.md)'s exact healthy scalar/dust action, smooth compact background interval after turnaround t*, positive dust, no radiation, supplied independent half-lattice circular Gaussian velocities with P_k=1 and conjugate reality. The Jordan density transfer obeys uniformly

    T_nJ(t,k)=N delta(t)+r(t,k), |r(t,k)|<=C/N,
    N=|k|, delta(t)>0, delta'(t)>0 for t>t*.         (1)

The positive derivative follows from the integrating factor in K2311's attractive Jeans equation and positive initial derivative. These are supplied white longitudinal velocities, not an inferred physical primordial law. Fields may be distributions, not nonlinear positive dust.

For a spacetime window K(t,x), define the observation first at finite Fourier cutoff. Its mean-square limit exists exactly when

    sum_k | integral conjugate(Khat(t,k)) T_nJ(t,k) dt |² < infinity. (2)

This follows from the same Gaussian isometry as K2314. The time covariance is coherent for each mode: the same random V_k evolves at every time. Replacing the square of the time integral by an integral of squared transfers silently introduces independent temporal noise and computes a different model. Real readouts use the conjugate half-lattice form; factors of two follow K2314.

SC-COS-50/51/54 ASSERTS, ledger0.263 LT-GR2e NEEDS, unchanged. These are model spacetime windows, not measured redshift/lightcone optical observables.

## Positive time averaging retains the rough response

Let K=f(t)W(x), fixed real f in L1 on the compact interval, and set A_f=integral f delta. Equation(1) yields

    T_f(k)=N A_f+O(||f||_1/N).                      (3)

When A_f!=0, T_f is comparable to N for large N, so white-seed variance is finite iff W is in H1. Any nonzero nonnegative weight supported after t* has A_f>0. Ordinary finite-duration averaging therefore does not remove the ultraviolet problem: it averages a slowly growing mode, not a rapidly oscillating wave. A fixed f is required; changing f with N defines a different observation.

If A_f=0, W in H^-1 is sufficient, hence every L2 window including a spatial top-hat works. No converse or nonzero residual coefficient is asserted. This cancellation removes the leading Jeans response as well as its large variance; it is not signal-preserving recovery of the density.

## Released construction: normalized temporal compensation and its cost

Choose two smooth nonnegative unit-mass bumps b1,b2 with strictly ordered disjoint compact supports after t*. Put D_i=integral b_i delta. Then 0<D1<D2, and

    f=(D2 b1-D1 b2)/(D2-D1),
    integral f=1, integral f delta=0,
    ||f||_1=(D1+D2)/(D2-D1).                       (4)

Thus constant temporal signals are preserved while this particular leading growth response is canceled. The amplification diverges when the two response averages approach each other; the construction prices rather than hides calibration sensitivity. Exact background integrals D_i are part of the supplied design, not calculated by the finite symbolic check.

For true response delta_true and calibrated delta_cal used in(4), leakage A=integral f(delta_true-delta_cal) obeys

    |A|<=||f||_1 ||delta_true-delta_cal||_infinity.  (5)

Any actual nonzero A restores the H1 requirement. Not every nonzero calibration error does so: an error orthogonal to f has A=0. A fixed small upper bound on A alone is insufficient to preserve the continuum cancellation. Explicitly supplied independent temporal white readout noise with covariance sigma² delta(t-t') adds sigma²||f||_2² times the spatial noise spectrum; it is not the coherent signal covariance(2). For disjoint bumps, ||f||_2²=(D2²||b1||_2²+D1²||b2||_2²)/(D2-D1)². Close response values amplify that noise too.

## Moving observer: directional smoothing, not universal smoothing

Now observe integral f(t)nJ(t,x+vt) against W(x), W in L2. Set

    B_k=integral f(t)delta(t) exp(i k.v t) dt.

The transfer is N B_k+R_k with |R_k|<=C||f||_1/N. Since (w_k R_k) is square summable, the exact necessary and sufficient white-seed criterion is

    sum_k N² |w_k|² |B_k|² < infinity.             (6)

This uses the vector-space property of l2, not a false pointwise lower bound when B_k is small. If f is smooth with compact interior support, repeated integration by parts gives arbitrarily fast decay in |k.v|. That is directional decay, not uniform decay in N.

A paired exact control makes the distinction decisive. Let W(x) be the indicator of 0<=x1<=pi, independent of x2,x3 on the2pi torus, with nonnegative nonzero smooth f. Only k=(n,0,0) occurs and w_n=(1-(-1)^n)/(2pi i n) up to conjugation. For v=e2, k.v=0 and B_k=A_f>0: every odd n contributes the same positive leading amount to(6), so variance diverges. For v=e1, B_k is the Fourier transform of smooth compact f delta at n, giving rapid decay and finite variance. Smooth motion can repair this particular slab window only when it samples across the rough direction. Neither example is a physical lightcone or a general survey prescription.

## Verification and next construction

Exact symbolic controls test normalized cancellation, leakage, coherent cross-time covariance, noise amplification and phase direction. Finite rational-weight Fourier controls test the slab support and transverse/longitudinal motion. Infinite summability and decay claims rely on Gaussian isometry and integration by parts above, not a finite cutoff count.

The next physical test needs specified initial covariance, source/detector geometry and noise together. A true lightcone window must be composed with the observer's metric and optical transport; an arbitrary moving Euclidean window is not that bridge. The current theorem supplies a falsifiable variance/calibration requirement for such a construction.
