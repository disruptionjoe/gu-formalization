---
title: "K2331 Certified full-count windows and a one-sky sign test"
status: active_research
doc_type: exploration
created: "2026-10-30"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematics; no empirical, hardware or native GU acceptance
scripts:
  - tests/channel-swings/k2331_certified_count_window_covariance_probe.py
---

# K2331 Certified full-count windows and a one-sky sign test

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
result: K2331
carrier: two real harmonic count windows of the frozen healthy designer dust action LAYER=toy CHIRALITY=N/A
pairing: positive Gaussian covariance or complex Hilbert norm as explicitly stated ON=declared_carrier
real_structure: real field with conjugate Fourier modes or complex adjoint
grading: linear scalar quadrupole and five real harmonic components
action_owner: repository-construction -- K2305/2308 background and constrained dynamics plus K2325 observation and supplied compact-band seed
target: validated covariance and exact finite-replication sign discrimination MAP-TYPE=evaluation
```

## Result and fixed statistical model

This is an actual interval evaluation of [K2329](k2329-robust-count-covariance-test-2026-10-30.md)'s full-count kernels, including foreground lensing, time delay and integrated redshift. For two declared positive radial windows and the band1<=k<=2, it certifies strictly negative response kernels and strictly positive shared-seed cross covariance. The sign also holds for every nonzero nonnegative window on the same two supports and every positive-integral nonnegative integrable spectrum on this band. A released exact sign test uses the five real full-sky quadrupole modes, without inventing independent skies or a large-sample approximation.

Keep the SAME [K2305](k2305-regular-constrained-matter-transfer-2026-10-30.md) background, [K2308](k2308-inhomogeneous-constrained-dust-transfer-2026-10-30.md) constrained evolution, and [K2325](k2325-relativistic-count-covariance-2026-10-30.md) conserved unbiased volume-limited dust count with coordinate-event observer and test null photons. Set C=Fref=alpha=M_J=H*=Mpl=1, A_d=2/5, p=(5+sqrt73)/4. Radiation is absent. Initial time is the Einstein turnaround x*=[A_d(1+p/2)]^(1/p), observer x=1; r=2(1-x^-1/2), r*=0.02184241375... . At x*, (Phi,chi,pi,v)=(0,0,0,1/k), and the reconstructed number perturbation is exactly zero. All emitting times used below are strictly after the turnaround.

Supply P(k)=1 on[1,2], zero elsewhere, with the unchanged normalization Var(Y)=integral P|B|²d³k. This is an explicitly band-limited positive Gaussian law, NOT the earlier P4 law or a measured primordial spectrum. Compact support makes sharp radial windows admissible here; it does not repair a white ultraviolet law. Define s=r/r*. The normalized radial windows F1=4/r* on s∈[1/4,1/2], F2=4/r* on s∈[5/8,7/8], zero elsewhere. Each count weight is F_i(r)Y_2m/r², with real L2-normalized harmonics. Gaussian probabilities, seed, optical interpretation and catalog remain supplied conventional physics. SC-ACT-01/GEO-55/COS-50/51/54 ASSERTS, SC-META-53 UNCERTAIN and ledger0.263 LT-GR2e/GR6b/SM8 are unchanged. No empirical rejection, source mechanism test, novelty or GU prediction is claimed.

## Actual coefficients and full observation

Let beta=-1/sqrt6, y=(Phi,chi,pi,v), q=k²/a². Use F=1-A_d x^-p and the exact H,u,d,V',V'' in K2305(6)-(7). Eliminating number by K2308's constraint gives y_t=J y with

    J=[[-H, u/2, 0, -d/2],
       [0, 0, 1, 0],
       [-4uH-2V'-2beta d+beta(2q-u²),
        -q-V''+2u²+3beta Hu+beta V', -3H+beta u, -2ud-3beta Hd],
       [-1, -beta, 0, -beta u]].

Use z=1-s increasing from the seed to the observer. Write r=r* s; then x=(1-r/2)^-2 and y_z=r* a J y. Conformal Hc=sqrt(x), partial_eta Hc=-x/2, and A=-1/2+2/(r sqrt(x)). Define P_t=-H Phi+(u chi-dv)/2. Reconstruct

    n=[-(2q-u²)Phi-(3Hu+V'+beta d)chi+3Hd v-u pi]/d,
    nJ=n-3beta chi, PhiJ=Phi+beta chi, PsiJ=Phi-beta chi,
    dotPsiJ=a(P_t-beta pi), W=2Phi, dotW=2a P_t.

Dots are conformal partial-time derivatives, never derivatives along the cone. Compute

    Q0(r)=integral_0^r W j2(ks) ds,
    Q1(r)=integral_0^r W j2(ks)/s ds,
    Qd(r)=integral_0^r dotW j2(ks) ds.

The actual source integrand in b_i=integral F_i g dr is

    g=[nJ+dotPsiJ/Hc+(1+A)PhiJ-2PsiJ]j2(kr)
      -k²v/(a Hc)j2''(kr)-Akv/a j2'(kr)
      +A Qd-4Q0/r+6Q1.                                  (1)

The last line is K2329's complete foreground term at L=2. Source windows exclude r=0; foreground integrals include it. Observer monopole/dipole terms vanish at this finite spectral support after quadrupole projection. No omitted observer point limit is used.

## Why the enclosures certify entire cells

Arb ball arithmetic at128-bit midpoint precision encloses every elementary operation, including algebraic x*, logarithmic real powers, and their rounding. Split z into512 equal cells and k into32 equal cells. For each cell I and parameter interval K evaluate A_I=r*aJ. Given starting enclosure Y, construct a box Z and check strict inclusion

    Y+[0,h] A_I Z is contained in the interior of Z,
    h ||A_I||infinity <1.                                (2)

A first-exit argument and uniqueness of the bounded linear IVP place the whole solution in Z; its endpoint lies in Y+h A_I Z. Thus initial/spectral uncertainty, local truncation and arithmetic rounding are all enclosed. Failure to find a tube aborts; it is never treated as a successful sample. Stored tubes are reversed into increasing radial order. In each foreground cell, old Q+[0,dr] times its interval integrand encloses EVERY partial integral, and old Q+dr times the range encloses its endpoint. Window boundaries align with cells; their exact normalized masses are4/512. The band sum covers all of[1,2]. The exterior spectral contribution is exactly zero for this supplied law.

Use the entire power series

    j2(t)=sum_(m>=0) (-1)^m t^(2+2m)/(2^m m! (2m+5)!!).

Terms m=0..6 are evaluated by interval arithmetic, with twice the absolute m=7 term bounding the tail, also after one/two derivatives; on |t|<1 each subsequent term ratio is less than1/2. In Q1 evaluate j2(kr)/r as the polynomial series k^(2+2m)r^(1+2m) BEFORE division. Its remainder uses the same geometric bound and is finite at r=0. No rounded sine cancellation, numerical derivative, unchecked mesh-convergence argument or omitted first cell supplies a proof. Interval Picard enclosure is an established validated-ODE method; see [Nedialkov, Jackson and Corliss](https://www.sciencedirect.com/science/article/pii/S0096300398100838). The application here is this actual full-count operator.

## Certified covariance and its useful consequence

The complete source-cell enclosures are strictly negative on BOTH annuli for EVERY k in[1,2]. Consequently the selected b_i are negative. Integrating with the actual spherical normalization gives

    Mij=16pi² integral_1^2 k² b_i(k)b_j(k) dk.

The companion report records tighter Arb endpoints; safe outward rational bounds are

    228 < M11 < 273,
    230 < M12=M21 < 273,
    231 < M22 < 273.                                    (3)

These are full covariance bounds in the declared dimensionless seed convention, not relative-precision claims or realistic survey forecasts. M is positive semidefinite by its exact Gram definition. These enclosures do NOT prove det M>0 or positive definiteness. Independent readout noise N0=I2, if supplied, makes the total covariance strictly positive definite. Strict negativity of g proves more than this single top-hat fixture: every positive-integral nonnegative integrable F_i on the corresponding annuli yields b_i<0 and every positive-integral nonnegative integrable spectrum supported on[1,2] gives M12>0. Arbitrary tracer changes, extra spectral support, sign-changing windows, source correlations or correlated noise are outside that conclusion.

A genuine changed-window control negates F2 only. It preserves M11,M22 and reverses M12. This is a normalization/sign control, not a competing physical theory or empirical exclusion. Negating the entire seed would preserve the covariance and cannot test this seam.

## Follow-through: finite one-sky sign calibration

Under the stated isotropic Gaussian seed, rotationally invariant dynamics and the SAME radial windows, the five real L=2 harmonic coefficient pairs y_m are independent centered bivariate Gaussians with common covariance. Supply centered isotropic Gaussian noise independent between the two channels and independent of the seed; its cross covariance is zero and its five modes are independent. Unknown nonnegative seed amplitude and unknown diagonal noise variances preserve correlation rho>=0 (take total marginal variances positive). The fixed-band sign theorem therefore supplies a nuisance-uniform consequence that does not need10000 hypothetical skies.

For a centered nonsingular bivariate Gaussian, rotational symmetry of a pair of independent standard normals gives

    Pr(sign y1 != sign y2)=arccos(rho)/pi <=1/2.           (4)

The boundary degenerate cases follow by limits. One proof writes y1=X and y2=rho X+sqrt(1-rho²)Z; angular sectors where the signs disagree have total angle2 arccos(rho). Therefore the predeclared test that rejects ONLY when all five pairs have opposite signs has false-rejection probability at most(1/2)^5=1/32. It uses one full sky and one predeclared L, window pair and orientation. It is a conservative exact sign test, not an optimal likelihood. At an explicitly supplied negative-correlation alternative rho=-sqrt3/2 its power is(5/6)^5; this illustrates scope, not observed evidence. If selecting among J predeclared tests, union bound gives J/32, so arbitrary searching is not a5% test.

For the specific unit-amplitude M in(3) plus I2, rho>230/274>0.83 is certified; the null is strongly aligned, though no data have been supplied. For an explicit changed-noise countercontrol, add the positive semidefinite covariance1000[[1,-1],[-1,1]] to(3): its cross covariance is negative despite the unchanged signal/action. This demonstrates why independent channel noise is load bearing. Cut skies, anisotropic noise, correlated channel noise, unknown means and fitted windows invalidate the independent-mode or nonnegative-correlation premise unless separately handled. Repeated detector reads of one mode do not give new seed realizations. A negative observed sample cross covariance alone is not a population rejection: (4) is the actual finite-data rule.

## Evidence and next construction

The interval report is a computer-assisted enclosure for this complete finite-band model. Independent analytic reviews inspect the coefficient, endpoint and integration proofs; changed-input tests inspect the actual evaluator. This is neither a Lean certificate nor an external-expert/empirical validation. Next replace the supplied narrow spectrum/windows/noise by a physically justified family and certify its signs or covariance cone; spectral support outside[1,2] requires new computation and tails. The full-count fixture now exists and need not be replaced again by arbitrary covariance matrices. Native curved stationary fields, receiver jets and common analytic domain remain separate missing constructions.
