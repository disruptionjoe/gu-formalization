---
title: "K2323 Born lensing and the observer endpoint"
status: active_research
doc_type: exploration
created: "2026-10-30"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematics only; no native physical acceptance
scripts:
  - tests/channel-swings/k2323_born_lensing_observer_domain_probe.py
---

# K2323 Born lensing and the observer endpoint

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
result: K2323
carrier: scalar Born angular count pushforward on the same dust-scalar background with a supplied white-UV longitudinal Gaussian seed LAYER=toy CHIRALITY=N/A
pairing: shared Gaussian spectral covariance and angular integration by parts ON=declared_carrier
real_structure: real sky weights and conjugate Fourier modes
grading: first-order scalar perturbations; angular harmonics
action_owner: repository-construction -- K2311 conditional dust-scalar transfer plus the explicitly supplied Born optical map
target: lensing adjoint, observer-endpoint counterexample and sufficient repairs MAP-TYPE=evaluation
```

## Result and unchanged scientific scope

A smooth positive source-shell window does **not** ensure finite lensing variance for the white-ultraviolet seed used in [K2321](k2321-radial-count-operator-2026-10-30.md). A quadrupolar component has a non-square-integrable 1/k spectral tail from the common observer endpoint. This invalidates extension of that note's local-count H1 theorem to this added optical term by analogy. The local theorem itself survives. We derive the exact adjoint, a positive smooth counterexample and three distinct repairs: a foreground cutoff, angularly constant integrated source moment, or sufficiently decaying ultraviolet covariance. None supplies full observed galaxy counts or physical primordial statistics.

Retain K2311's SAME healthy designer dust-scalar action and real longitudinal seed, with spectral convention Var(Y)=integral P(k)|B(k)|²d³k, P bounded, vanishing below k0>0 and equal to1 at sufficiently large k. Choose the ENTIRE foreground cone 0<=s<=r1 inside one compact smooth background interval strictly after t*. This is stronger than merely requiring source times r0<r<r1 to lie there. The background and exact transfer extend through the observer s=0. With t_s=-a, Jordan potentials satisfy

    W:=Phi_J+Psi_J=2Phi,
    T_W(s,k)=p(s)/k+R(s,k),
    p(s)=-a(s)² d_bg(s) delta(s)/m,  |R(s,k)|<=C/k³.    (1)

These are [K2311](k2311-uniform-constrained-dust-evolution-2026-10-30.md)'s uniform transfer estimates on that compact interval; p is smooth and p(0)!=0 because a,d_bg,delta,m are positive. The scalar conformal perturbation cancels from W. No claim is made at t=t* or beyond the controlled background interval.

Source SC-COS-50/51/54 and SC-ACT-01/GEO-55 retain ASSERTS; SC-META-53 retains UNCERTAIN. The source connection-distortion construction is not this supplied metric cosmology. Ledger0.263 LT-GR2e/GR6b/SM8 remains unchanged; this tests an imported observation/covariance interface, not a source claim.

## Defined angular map and exact shared-seed adjoint

At finite spectral cutoff define the Born angular displacement by the convention

    alpha(r,Omega)= integral_0^r (r-s)/(rs) grad_S W(s,Omega) ds,
    Omega_observed=Omega+alpha,
    Delta_L=-div_S alpha.                                  (2)

This convention defines the sign; changing the map convention reverses the signal but not the variance obstruction. Linear angular number conservation gives (2). Combine it with K2321's fixed-cone radial count at first order, so radial-angular cross terms are second order. This is one specified extension: perturbed radial paths, gravitational/integrated redshift, local observer tetrad terms, magnification selection and complete gauge-invariant counts are not thereby included. [Bonvin and Durrer, What galaxy surveys really measure](https://arxiv.org/abs/1105.5280) treats the fuller observable; we do not attribute this truncated map or the supplied seed to that paper.

For a real compact-annular source weight w, Y_L=integral r²dr dOmega w Delta_L. Swap integrals at finite cutoff and integrate on the sphere:

    f(s,Omega)=integral_max(s,r0)^r1 r²w(r,Omega)(r-s)/(rs) dr,
    Y_L=-integral_0^r1 ds dOmega (Delta_S f)(s,Omega) W(s,Omega),
    B_L(k)=-integral ds dOmega Delta_S f(s,Omega)
                         T_W(s,|k|) exp(i s k.Omega).        (3)

The integral in (3) is angular-first, equivalently with exp(i s k.Omega) replaced by exp(i s k.Omega)-1 since the spherical integral of Delta_S f is zero. At finite cutoff this subtraction makes the observer endpoint integrable before interchanging integrals: the unsubtracted product integrand need not be absolutely integrable. It changes no spectral kernel.

Below the sources,

    f(s,Omega)=M(Omega)/s-L(Omega),
    M=integral r²w dr,  L=integral r w dr.                    (4)

The source taper vanishes near r0 and r1 but (4) extends to the observer. A source-shell gap is not a foreground gap. For the combined count use B_total=B_count+B_L and its squared modulus in the SAME covariance. Independent noise variance addition would drop cross terms and is not justified.

## A sharp explicit failure with a smooth positive window

Let Y20 be a real L2(S2)-normalized harmonic, Delta_S Y20=-6Y20. First take w=F(r)Y20/r² with F smooth compactly supported in (r0,r1), M2=integral F dr nonzero. The angular plane-wave identity gives

    integral Y20(Omega) exp(i ks khat.Omega)dOmega
       =-4pi j2(ks)Y20(khat),
    B_L(k)=-24pi Y20(khat) integral f2(s) T_W(s,k) j2(ks) ds.

Because (j1(u)/u)'=-j2(u)/u and j1(u)/u tends to1/3 at zero and0 at infinity,

    integral_0^infinity j2(u)/u du=1/3,
    B_L(k)=-8pi p(0)M2 Y20(khat)/k+O(log(k)/k²).          (5)

To justify the remainder, p(s)M2/s differs from p(0)M2/s by a bounded function near zero. The other terms of f2p are bounded, piecewise smooth and compactly supported. The elementary bound |j2(u)|<=C min(u²,u^-1) gives their integral O(log(k)/k). The truncated singular integral differs from1/3 by O(1/k); the exact transfer remainder contributes O(k^-3) since integral |j2(ks)|/s ds is uniformly bounded. Multiplication by the outside1/k gives (5). Thus the error term is L2(d³k); the leading term is not. In fact Var with cutoff Lambda divided by Lambda tends to64pi²p(0)²M2² for this normalized harmonic and P=1 at large k. Cross terms in the asymptotic remainder are sublinear, so the limit is meaningful without claiming a bounded variance remainder.

Choose F>=0, integral F=1, and A=(1+epsilon Y20)/(4pi) with 0<|epsilon|<1/||Y20||infinity. Then w=F A/r² is smooth, positive on its source support, normalized and zero-extended H1. Its monopole lensing term vanishes; its nonzero quadrupole has (5) with M2=epsilon/(4pi). K2321's local-count kernel is L2 for this w and cannot cancel a non-L2 lensing kernel. This is an actual counterexample to smooth-window sufficiency for the stated combined truncated observable, not a finite-cutoff numerical failure or a theorem about complete relativistic counts. A monopole/dipole observer subtraction cannot remove this l=2 component.

## Released repair: one angular derivative and the observer moment

A sufficient condition for the principal lens contribution is

    integral_0^r1 ||grad_S f(s,.)||²_L2(S2) ds < infinity.   (6)

Extend the tangential vector field V(x)=p(s)grad_S f(s,Omega)/s by zero off the cone ball. Its distributional divergence is p(s)Delta_S f/s² (the radial component is zero). Equation(3)'s principal kernel is -|k|^-1 Fourier(div V). The Riesz multiplier bound and Plancherel give

    ||B_principal||_L2 <= (2pi)^(3/2)
             [integral p(s)²||grad_S f||² ds]^(1/2).       (7)

No radial derivative of f or H2 angular regularity is required. The boundary at s=0 introduces no radial flux; (6) makes V an L2 field and defines the divergence distributionally.

The exact remainder also exists. Integrate (3) by parts once on S2: the angular derivative of exp(i sk.Omega) contributes sk times the tangential component of khat. Since |R|<=C/k³, its shell multiplier has magnitude bounded by Cs/k². For k>=k0, use the K2319 Coulomb shell bound for k^-1 times an angular Fourier integral, then the remaining factor k^-1<=k0^-1. Minkowski bounds the remainder by a constant times

    integral_0^r1 s^(1/2)||grad_S f(s,.)|| ds.             (8)

The k-dependent radial multiplier can be pulled out of the shell spectral norm by its uniform bound; tangential khat factors are bounded Riesz multipliers. The finite infrared transition band is harmless: the once-integrated formula has s grad f integrable even for f~M/s. This also proves that the exact O(k^-3) remainder cannot repair (5).

For compact-annular w with one L2 angular derivative, (4) shows (6) holds if grad_S M=0. A hard foreground omission s<epsilon0, epsilon0>0, also makes (6) finite. These are sufficient lens-domain statements; no universal converse for arbitrary infinite angular expansions or full counts is claimed. Combine them with K2321's zero-extended H1 source condition to obtain a finite joint count-plus-lens random variable, retaining its cross covariance. A hard angular mask generally violates the supplied derivative hypothesis and earns no sufficiency claim.

A useful nonnegative repair retains anisotropic radial information. Let F1,F2 be distinct nonnegative smooth radial bumps with unit integral, and let Y=Y20. Then

    w=[F1(r)(1+epsilon Y)+F2(r)(1-epsilon Y)]/(8pi r²)    (9)

is positive for the same small epsilon and normalized. M=1/(4pi) is angularly constant, so (6) holds. The quadrupole changes sign between radial weights while the total window stays nonnegative; global signal cancellation is not required. A separated nonnegative F(r)A(Omega) with nonconstant A cannot achieve this moment repair when integral F is nonzero. A physical survey may not cover the full sky, so (9) is a mathematical repair, not an available survey mask.

For the explicit quadrupole and bounded spectral density with P(k) asymptotic to a positive constant times k^-alpha, (5) instead gives finite lens variance iff alpha>1. At alpha=1 it diverges logarithmically; alpha<1 gives power divergence. This changes the covariance premise, not the action or a proven primordial prediction. A foreground cutoff changes the observation model. Moment repair changes the window. Keep these alternatives distinct in later inference.

## Released stability test for additional observation terms

The l=2 divergence survives every finite sum, or L2-convergent sum, of added quadrupole spectral kernels in L2(d³k). If B0=C Y20/k+L2 and G is L2, B0+G is not L2. Its cutoff variance has the same leading linear coefficient: the cross term divided by Lambda tends to zero by Cauchy-Schwarz, since the leading norm grows as sqrt(Lambda) while ||G|| is bounded.

For a concrete sufficient class, consider a scalar line-of-sight term with a ROTATIONALLY INVARIANT transfer a(s)/k+O(k^-2), with remainder uniform over 0<=s<=r1, multiplied after source integration by a bounded radial weight h(s). Its quadrupole kernel contains integral h(s)[a(s)/k+O(k^-2)]j2(ks)ds. Since integral_0^r1 |j2(ks)|ds<=C(1+log k)/k, bounded a,h give an O(log k/k²) principal kernel and O(log k/k³) remainder, both L2 at high frequency. The inherited infrared cutoff controls low frequencies. Observer terms explicitly confined to sky harmonics l=0 or1 have exactly zero l=2 projection at every finite cutoff, even if their unprojected point evaluations lack a white-seed limit. These are sufficient criteria for a cancellation test, not an assertion that the complete physical observed-count formula belongs to this class. Singular endpoint weights and higher-derivative terms are examples of possibilities still to inspect, not an exhaustive classification. The actual shared full operator remains to be derived.

## Verification and remaining construction

The probe checks an exact angular-map Jacobian/count sign, harmonic and kernel/moment identities, tangential scaling, the j2 boundary primitive, positive compensated fixtures, the spectral threshold, and shared-covariance controls; the uniform transfer and continuum conclusions use the written proofs and their inherited hypotheses. Its polynomial radial fixtures have C1 zero extensions and test H1 moment identities; the smooth counterexample uses arbitrary C-infinity bumps. It does not use finite Fourier sampling as a variance certificate. The next complete observable must derive the remaining observer/redshift/ray terms under this same action and inspect their joint endpoint kernel before deciding whether this obstruction survives. A colored physical covariance is an independent input to construct, not permission to silently replace P=1. No source/ledger/canon or GU prediction changes.
