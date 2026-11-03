---
title: "K2526 Geodesic emitters: joint drift-distance repair and velocity-uniform weak test"
status: active_research
doc_type: exploration
created: "2026-11-02"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional radial test-emitter measurement class; no dataset, native GU or empirical verdict
scripts:
  - tests/channel-swings/k2526_geodesic_emitter_drift_repair_probe.py
---

# K2526 A physical moving-emitter nuisance and its consumer

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
result: K2526
carrier: radial timelike geodesic test emitters, comoving observer and photons in the same spatially flat homogeneous FLRW metric LAYER=toy CHIRALITY=N/A
pairing: observer proper-time spectral rates and isotropic source-rest-frame luminosity distance with joint uncertainty ON=declared_carrier
real_structure: real subluminal peculiar velocities and positive expansion histories
grading: instrument calibration, source motion, cosmological redshift and measurement error remain distinct
action_owner: repository-construction -- inherited K2367 sourced metric action; test tracers do not change its dust background
target: exact common-momentum measurement repair and shared-coefficient weak exclusion with uncertain velocities MAP-TYPE=evaluation
```

## Result and scope

[K2524](k2524-anchored-drift-nuisance-quotient-2026-11-02.md) repairs a specified wavelength-calibration class, but leaves physical emitter motion. Here radial freely falling test particles give an explicit physical nuisance: motion changes both drift AND the luminosity-distance anchor, and moves the low-redshift endpoint. We derive the joint exact repair, then consume it in [K2522](k2522-redshift-drift-interface-2026-11-02.md)'s actual weak test. A structural cancellation removes any need to estimate the common momentum precisely for its coasting-shape witness: sufficiently small variation of normalized observed drift rejects the inherited action family uniformly across a declared momentum interval.

These are conditional kinematics and functional bounds. No measured band, feasible sensitivity, source population, clock/ruler calibration or empirical exclusion is supplied. SC-COS-50/51/54 ASSERTS and LT-GR2e/ledger0.263 stay unchanged. The metric comparator has no supplied bridge to native connection-distortion cosmology. The instrument's multiple lines must be from the same moving emitter; they cannot remove its common Doppler shift.

## 1. Exact clocks, motion and distance

Use c_light=1 and spatially flat ds²=dt²-a(t)²(dchi²+chi²dOmega²), a_o=1 at the reference observer epoch. The observer is comoving at the origin. An outward signed radial peculiar velocity v=a_e dchi_e/dt_e obeys |v|<1. A received radial null ray satisfies int_te^to dt/a=chi_e(te), hence

    dt_e/dt_o=1/[y(1+v)], y=a_o/a_e.

Special-relativistic Doppler with the radial source four-velocity gives

    D=gamma(1+v), X=1+z_observed=yD.                  (1)

For a radial timelike geodesic, the conserved comoving momentum is P=a_e gamma v; v_dot_e=-H_e v(1-v²). Since d(log D)/dv=1/(1-v²),

    d(log X)/dt_o=H0-H_e/y,
    G=dX/dt_o=X H0-D H_e.                            (2)

No gravitational field equation entered. This is compatible with the same K2367 metric background only as a test-tracer calculation: the moving tracers do not replace the comoving dust sourcing that background. Nongeodesic forces, nonradial motion, observer acceleration, inhomogeneous potentials, lensing and opacity are not included.

At the reference epoch put p=P/a_o=P. Then

    D_p(y)=sqrt(1+p²y²)+py, X_p(y)=yD_p(y),
    D=sqrt(1+2pX), y=X/D,
    dy/dX=(1+pX)/(1+2pX)^(3/2)>0.                   (3)

The inverse requires 1+2pX>0. The zero-distance background endpoint y=1 is at X0(p)=sqrt(1+p²)+p, not generally X=1. IMPORTANT: along repeated observer times p=P/a_o varies with p_dot_o=-H0 p. Equation(3) is a reference-lightcone relation; differentiating it at fixed p to derive G would be wrong. Equation(2) uses the actual source and observer clocks.

Assume photon reciprocity and isotropic luminosity in the source rest frame. A radial boost leaves the transverse source screen unchanged, so D_A=a_e chi, D_L=X²D_A. Thus, with C(y)=int_1^y du/H(u),

    L(X):=D_L(X)/X=D C(y).                           (4)

This standard source-velocity luminosity correction is consistent with [Davis and Scrimgeour, Eq15](https://arxiv.org/pdf/1405.0105). [Uzan, Bernardeau and Mellier](https://arxiv.org/pdf/0711.1950) provide broader perturbative acceleration context; their cosmology/noise forecast is not imported. Our exact radial derivation supplies the particular nuisance used here. A different candle/beaming model requires its own readout map.

## 2. Known-momentum joint repair

First apply the actual K2524 instrument repair. Allow its remaining common fractional drift bX, and define Q(X)=G_observed(X)/X. For the same p across the supplied tracer curve,

    Q(X_p(y))=H0-H(y)/y+b,
    H_p(y)=y[q-Q(X_p(y))], q=H0+b.                  (5)

At anchor X_a, let D_a=sqrt(1+2pX_a), y_a=X_a/D_a, L_a=D_L(X_a)/X_a. The correct shared-anchor equation is

    integral_1^ya dy/H_p(y)=L_a/D_a.                 (6)

Equivalently, in OBSERVED coordinates,

    integral_X0(p)^Xa (1+pX)/[(1+2pX)(Xq-G_observed(X))] dX
       =L_a/D_a.                                   (7)

Every denominator must be positive, y_a>1, and actual curve coverage is required down to X0(p). The derivative of(6)'s left side with respect to q is -J, J=integral_1^ya y/H_p²dy>0. A root bracket supplies existence and strict monotonicity supplies uniqueness. Positivity of q is not required: it includes the instrumental b, whereas H must be positive. Shifting Q and q by b leaves(5)-(7) invariant. Correcting only drift but retaining the old distance, endpoint or Jacobian changes the reconstructed history.

DeSitter is an exact contrary control. For H=K>0, Q=K(1-1/y), C=(y-1)/K, L=D(y-1)/K. Equations(5)-(6) recover K. If drift is deboosted correctly but the anchor is mistakenly L rather than L/D, the anchor target is too large for p>0. Strict monotonicity forces q<K whenever a positive root exists; the inferred history becomes K+(q-K)y and is not constant. The wrong anchor does not represent a physical new dark-energy observation.

## 3. Finite momentum and joint measurement bands

For smooth Q and a family of positive roots of(6), differentiation at fixed observed X_a,L_a gives

    y'_a=-X_a²/D_a³, C'_p=-L_a X_a/D_a³,
    partial_p X_p(y)=y² D_p(y)/sqrt(1+p²y²),
    q'_p=[y'_a/H_p(y_a)+integral_1^ya y Q'(X_p)partial_p X_p/H_p²dy-C'_p]/J. (8)

This derivative varies the reference-epoch nuisance parameter between trial reconstructions; it is NOT the observer-time derivative warned about in section1. Suppose every trial and true history has m<=H<=M on its whole integration interval; A<=y_a<=B with A>1; |Q'|<=LQ; and define Bx>=sup|partial_p X|, Ba>=sup|y'_a|, Bc>=sup|C'_p|, Jmin=(A²-1)/(2M²). Integrating(8) over |p-p0|<=delta_p gives on a common interval1<=y<=Y<=A

    |H_p-H_p0| <= Y delta_p [2LQ Bx+(Ba/m+Bc)/Jmin].  (9)

For a simultaneous normalized-rate band |delta Q|<=E_Q and anchor |delta L_a|<=E_L, add

    Y[2E_Q+E_L/(D_a,min Jmin)].                       (10)

This uses K2524's exact shared-anchor oscillation identity, composed at fixed p before the momentum comparison. It is a finite bound, not a covariance-only or linearization claim. Positive-root existence and the common envelope across the entire trial family are assumptions to establish independently, not consequences of nominal data. Continuous Q bands need controlled interpolation, redshift assignment, finite baseline, calibration and all correlations. A finite set of noisy samples alone supplies no such band.

## 4. Released structural test avoids precise momentum estimation

The preceding sensitivity estimate can be wasteful. If Q is constant b on the required curve, equation(5) forces H_p(y)=(q-b)y for EVERY admissible p. One distance can leave p and this positive overall scale unidentified, but [K2520](k2520-nonlinear-observation-null-2026-11-02.md) already excludes every such coasting shape for all shared coefficients. Unknown momentum therefore does not save that action family in this observational class.

The stronger finite-band statement follows without a derivative bound or delta_p estimate. Let R=osc Q over the union of all trial observed intervals. Set h0=q-Q(X0(p))=H_p(1). Then

    H_p(y)/h0=y[1-(Q(X_p(y))-Q(X0(p)))/h0].           (11)

The anchor gives a rigorous lower bound on h0. Since H_p(y)<=y(h0+R) and H_p>0,

    h0 >= D_a log(y_a)/L_a-R.                        (12)

This argument does NOT assume h0>R before proving a useful lower bound. For a concrete dimensionless sufficient envelope choose X_a=3/2, p in[0,1/100], 0<L_a<=1, and the SAME K2522 interval1<=y<=Y=36/25. Exact rational inequalities give y_a>29/20>Y, D_a>=1, and log(y_a)>log(29/20)>=9/29. Therefore, if R<9/29,

    h0>=9/29-R>0,
    sup |H_p/h0-y| <= Y R/(9/29-R).                 (13)

The choices here define a mathematical observation envelope in one fixed clock/distance unit system; they are not measured values or a physical Hstar calibration. A general measured Lmax simply changes(12), rather than allowing units to conceal a precision requirement.

Use the exact inherited tolerance eta_star from K2522, approximately3.30264588738e-10. The normalized history hbar=H_p/h0 satisfies its existing half-margin certificate simultaneously for all p if

    R <= (9/29) eta_star/(Y+eta_star).               (14)

Why scaling does not refit the test: its four weak columns scale as h^(-1/2),h^(-5/2),h^(-5/2),h^(3/2). Dividing the equation by h0^(3/2) replaces the SAME shared constants by alpha/h0²,rho/h0⁴,q0/h0⁴. Since the certificate excludes every triple of constants for every allowed normalized history, all positive h0 are covered. This is stronger than testing one fitted coefficient triple, and is not a claim of an empirical/natively owned action exclusion.

A simultaneous band for measured Qhat gives R<=osc Qhat+2E_Q. For the anchor require its full joint positive band satisfy L_a<=1. For each p all values down to X0(p) must be available or rigorously bounded; extrapolation across a missing low-redshift interval is an additional unproved input. A band across the union[1,3/2] is sufficient but is NOT promised by a real moving-source catalogue. This is particularly important because the endpoint moves with p. Same-p geodesic tracers, reciprocity, band coverage, positivity and the reference calibration are all part of the tested class.

## 5. Executed identification follow-through: two anchors and a held-out third

For exact constant Q=b, write f_i(p)=D_i log(X_i/D_i), where D_i=sqrt(1+2pX_i). The reduced anchors satisfy L_i=f_i(p)/h0 with one shared positive coasting scale h0. One anchor admits a continuum of p,h0. Two distinct observed anchors X_a>X_b>1 identify p uniquely if they fit this class. Indeed

    partial_p log f_i=(y_i/D_i)(1-1/log y_i).

For fixed p, put h(y)=y/D_p(y)(1-1/log y) and S=sqrt(1+p²y²). Direct differentiation gives

    h'(y)=[log²y-log y+D_p(y)S]/[D_p(y)² S log²y] >0, y>1,
    D_p(y)S=(D_p(y)²+1)/2.

The numerator is (log y-1/2)²+D_p(y)²/2+1/4, strictly positive. Since y_a>y_b, partial_p log(f_a/f_b)>0. The ratio L_a/L_b therefore has at most one p solution on any connected admissible interval. This is a global monotonicity proof, not a finite parameter scan.

There is an important contrary conclusion. With no sign/magnitude prior on p, the common positive-distance domain is

    -1/(2X_a)<p<(X_b²-1)/(2X_b).

At its lower endpoint D_a log(X_a/D_a) tends to0 while f_b stays positive. At the upper endpoint f_b tends to0 while f_a stays positive. Thus f_a/f_b ranges continuously and strictly increasingly over(0,infinity). EVERY positive pair of anchors fits one p and one h0 in this exact coasting measurement family. Parameter identification by two anchors is therefore not a held-out test. A third anchor requires the nontrivial compatibility condition L_c/L_a=f_c(p)/f_a(p), with p fixed by the first pair. That p must first satisfy 1+2pX_c>0 and y_c>1; otherwise the third anchor rejects the class at its domain boundary. A separately imposed interval such as[0,1/100] restricts the allowed ratio range and can itself reject a pair. Shared multiplicative ruler calibration cancels in ratios but remains necessary to determine the dimensional h0. No real-data accuracy or stability near the degenerate endpoints is claimed.

This identification statement does not undo section4: the inherited metric-action family already excludes all these coasting shapes. It clarifies exactly which observational inputs identify nuisance parameters and which add an independent test of the declared kinematic family.

## 6. Reproduction, contrary cases and next work

The probe derives the clock, geodesic, Doppler and anchor Jacobian identities symbolically; checks exact rational physical velocities, the drifting p normalization, deSitter wrong-anchor control, finite parameter sensitivity, the actual inherited tolerance and scale transformation. It also constructs a nonconstant normalized-rate perturbation that survives instrumental common-mode removal, and an unconstrained between-node bump. Universal bounds follow from(8)-(14) and the cited K2522 certificate, not from counting sampled values.

This replaces an unspecified acceleration error by a concrete exactly repaired physical class and carries it through a velocity-uniform action test. It neither removes arbitrary acceleration nor proves the required error band can be achieved. The next discriminating input is a justified joint curve/anchor band with its low-redshift coverage and an independently supported tracer model; a different accessible configuration or full native coupled action remains a separate alternative. No source, ledger, canon or empirical verdict moves.
