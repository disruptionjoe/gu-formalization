---
title: "K2580 One fixed radial and angular TT source domain"
status: active_research
doc_type: exploration
created: "2026-11-05"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: fixed common radial-amplitude Dirichlet and annular impedance TT source domain; scalar complement and physical preparation open
scripts:
  - tests/channel-swings/k2580_radial_angular_source_domain_probe.py
---

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
result: K2580
carrier: radial-dependent TT source module of the selected curved seven-plus-seven system LAYER=toy CHIRALITY=N/A
pairing: indefinite tensor-test duality and auxiliary positive Sobolev norms ON=declared_carrier
real_structure: real data; complex impedance explicitly represents two real quadratures
grading: scalar amplitudes, TT tensor, shifted and original metric, auxiliary grade2 kept distinct
action_owner: repository-construction -- stated conditional model
target: fixed-domain paired response and original metric observation MAP-TYPE=evaluation
```

# One fixed common radial and angular source domain

## Result and scope

The regular-center radial Dirichlet realization supplies a spectral gap large enough to make BOTH actual annular potentials monotone for every radial and angular mode. This produces a fixed common TT preparation, a uniform polynomial inverse with explicit moderate constants, and a nonconstant radial-source/conserved-observation consumer. The radial boundary condition is on the scalar amplitude; it is not full tensor Dirichlet data.

K2562 and K2564 already construct full compact-source responses using parameter-selected radial conditions and a different global B completion. This note does not rediscover or supersede that existence result. It extends K2578's fixed-annulus R(1) sector to general radial TT amplitudes under ONE fixed radial boundary realization, with compatibility conditions stated below. The scalar cofactor complement and physically selected preparation remain open.

SC-ACT-01 ASSERTS its first-order action, SC-GEO-03 ASSERTS Met(X), SC-GEO-55 ASSERTS gauge-rotated-Levi-Civita displacement, and SC-META-53 remains UNCERTAIN about indefinite spectra. This product and action completion are repository constructions. Ledger0.263 LT-GR6b/10/11 and LT-SM8, source polarities and canon remain unchanged. The auxiliary five-dimensional radial norm is a calculation device, not physical normal dimension or positive physical energy. No native GU recovery, causal evolution or novelty claim.

## 1. Fixed radial realization and quantitative gap

Use K2552 notation, κ ≠ 0:

    K = 35 κ² / 3624192, R = 1/|κ|,
    S(r) = sin(√K r)/√K, C(r) = cos(√K r),
    α = C'/C, β = S'/S,
    D5 = ∂r² + (6α+4β)∂r,
    w5 = C^6 S^4.

Let A5 = −D5 on L²((0,R), w5 dr), with the regular center and scalar Dirichlet value f(R)=0. Precisely, use the closed nonnegative form ∫ w5 |f'|², initially on smooth even radial functions with zero outer value. The center is the regular/Friedrichs endpoint. K2562 §1 already proves its compact resolvent through conjugation to −∂r²+2/r²+bounded potential. Thus there is a real orthonormal basis φ_j with A5 φ_j=σ_j φ_j and φ_j regular even at zero. The scalar amplitude condition does NOT say the reconstructed tensor R(f) vanishes at R: its other components involve f'.

For x=√K r, the elementary bounds sin x/x ≥ 1−x²/6 and cos²x ≥ 1−x² imply

    1 ≥ w5/r^4 = (sin x/x)^4 cos^6x
      ≥ (1−2x²/3)(1−3x²)
      ≥ 1−11x²/3
      ≥ 988381/988416 > 1/2.

For f(R)=0, weighted Cauchy–Schwarz gives

    |f(r)|² ≤ (r^(−3)−R^(−3))/3 · ∫_r^R s^4 |f'(s)|² ds.

The integral of r^4(r^(−3)−R^(−3))/3 from 0 to R equals R²/10. Integrating the estimate and bounding the inner factor by this full integral yields

    ∫ r^4 |f|² ≤ (R²/10) ∫ r^4 |f'|².

Comparison with w5 therefore gives

    ∫ w5 |f|² ≤ (R²/5) ∫ w5 |f'|²,
    σ_j ≥ 5/R² = 5κ².                                      (1)

Density extends the inequality to the closed form. No numerical eigenvalue calculation is used.

## 2. All radial and angular modes are monotone

Retain K2578's fixed B annulus, t0=asinh 1, t1=asinh 2,

    ζ = sinh²t ∈ [1,4],
    x = log[tanh(t/2)/tanh(t0/2)] ∈ [0,d],
    d = log[((√5−1)/2)/(√2−1)],
    J = sinh t cosh(t)^(3/2),
    L = ℓ(ℓ+2), n=m+1 ≥ 1.

Both compact angular factors are the existing S³ factors with ALL harmonic multiplicities. Set

    c = 970112/(13395κ),
    μ = 611557655 κ² / 39953092608,
    rE = 1/(6a0), a0 = −5κ/2288.

For a source j=R(b), allowing b=b(r,x,θ,ω), the TT scalar equations are exactly

    (D5+Y+μ−21K)u = −rE b/c,
    (D5+Y−16K)v = rE b.                                  (2)

On a radial eigenmode D5=−σ and an angular mode, the K2578 Liouville identity gives y_Q=Ju and y_E=Jv:

    y_Q'' − P_Q y_Q = f_Q = (rE/(cK)) Jζ b,
    y_E'' − P_E y_E = f_E = −(rE/K) Jζ b = −c f_Q,

    P_Q = n² + (A−σ/K)ζ − (L+3/4)ζ/(1+ζ),
    A = μ/K−49/4 = 121366223/77168,
    P_E = n² − (29/4+σ/K)ζ − (L+3/4)ζ/(1+ζ).             (3)

The radial spectral gap proves

    A−σ/K ≤ A−5κ²/K = −39831726385/77168 < 0.

Consequently ∂ζP_Q and ∂ζP_E are strictly negative for EVERY radial/angular mode. In particular there is no finite double-turning exception in this Dirichlet-radial family. The fixed R(1) mode is not a member of A5's Dirichlet spectrum and its old exception is not contradicted.

Choose the COMMON normalization

    ν² = 1+n²+L+σ/K,
    k² = 1+n²+L+4σ/K+30.                                (4)

Since σ/K>A, direct bounds give

    |P_Q| ≤ n²+4σ/K+(4/5)L+3/5,
    |P_E| ≤ n²+4σ/K+(4/5)L+148/5,

so |P_Q|,|P_E|≤k². Also ν²≤k²≤31ν² (a deliberately loose fixed comparison). No angular cutoff or omitted radial degree occurs.

## 3. A common fixed preparation and a uniform forced inverse

For BOTH channels use

    y'(0)+iky(0)=k g0,
    y'(d)−iky(d)=k gd.                                  (5)

The four boundary data, two per channel, are supplied independently. The forcing is linked by (3), not freely specified independently. The same radial basis, k and endpoint rules define a common domain. This is a nonlocal spectral boundary preparation; complex impedance means two coupled real quadratures, not a real scalar Robin law or a self-adjoint full-system boundary problem.

K2576 §§2–3 applies with its ACTUAL hypotheses now proved for every index: P is real, nonincreasing, and |P|≤k². For clarity, its essential estimates are as follows. The homogeneous flux identity gives

    ||(y,y'/k)(0)||² + ||(y,y'/k)(d)||²
       = |g0|²+|gd|².

On a nonpositive suffix, F=|y'|²+(1−P)|y|² obeys F'≥−F; propagate backward. On a positive prefix, |y|² is convex and (|y'|²−P|y|²)'=−P'|y|²≥0 controls the derivative from the turn. If there is no turn, use the whole nonpositive or whole nonnegative estimate. Thus

    sup_x ||(y,y'/k)|| ≤ C_H k ||(g0,gd)||,
    C_H=max(√6 exp(d/2),2+d).                            (6)

Zero data imply a zero endpoint jet and uniqueness. For forcing, let U(0)=1,U'(0)=−ik and V(d)=1,V'(d)=ik. Their nonzero constant Wronskian W gives

    G(x,τ)=U(min(x,τ))V(max(x,τ))/W.

The derivative jump is one and both impedances in x are zero. The homogeneous boundary responses imply |U/W|,|V/W|≤C_H. Backward energy bounds V on the nonpositive suffix; on the positive prefix use nonnegative Dirichlet interpolation plus the one-dimensional maximum-principle bound for its Dirichlet Green kernel. This yields

    sup |G| ≤ C_G k,
    C_G=C_H(1+√3 exp(d/2))+d/4.                           (7)

There is no exceptional factor exp(Kstar d). Integrating Gf proves sup|y|≤C_G k||f||L1. The integrated Taylor estimate on an available one-sided interval of length min(d/2,1/k) gives

    |y'(x)| ≤ (4/d+5k/2)sup|y| + ||f||L1.                (8)

These are a common uniform polynomial bound for both coupled scalar channels, with constants depending on the fixed B annulus and displayed selected-model coefficient multipliers. They are not a sharp regularity loss or a physical condition-number calibration.

## 4. Synthesis, center regularity and honest boundary compatibility

Define the auxiliary joint Hilbert scale by

    ||a||Hs² = Σ_(j,ℓ,m,all multiplicities) ν^(2s)|a_(jℓm)|².

It is the spectral scale of the positive radial Dirichlet realization plus the two compact angular Laplacians. It is NOT by definition a physical tensor norm. Equations (6)–(8), k comparable to ν, Minkowski and finite-sum density give

    (g0,gd,f) ∈ H^(s+1) × H^(s+1) × L1_x H^(s+1)
      → y ∈ C_x H^s, y_x ∈ C_x H^(s−1).                 (9)

The equations hold in the corresponding spectral/distribution sense. The coefficient representation supplies uniqueness in this class. Strong continuity follows from finite sums and the uniform bounds, not merely per-mode nonresonance.

For a full smooth physical reconstruction, make the data assumption explicit: boundary data lie in the intersection of ALL joint spectral powers; forcing is smooth in x with values in that intersection, with every needed seminorm locally bounded. This is a sufficient compatible spectral-smooth class. Elliptic regularity of A5, regarded as the auxiliary smooth radial five-ball operator, gives smooth even radial amplitudes; compact angular ellipticity gives smooth angular dependence; repeated use of (3) gives smooth x dependence. Smooth even radial amplitudes reconstruct smooth invariant tensors at the ACTUAL three-dimensional normal center through K2552's formula R; in particular b−a_b=O(r²).

Do NOT identify this spectral-smooth class with arbitrary C∞ functions up to r=R. Dirichlet powers impose outer compatibility. Finite eigenfunction sums and smooth functions flat at the outer endpoint are valid examples. For finite s the theorem first states an auxiliary coefficient-space estimate; tensor reconstruction is a finite-order differential map on interior subintervals r>0 with the corresponding local regularity loss. No unproved extension from arbitrary negative spectral order to a regular physical tensor at the center is asserted.

For smooth compatible data set

    Q=R(u), z=R(v), h=z−rE Q,
    e2=−A2^−1 B_aux Q,

with all other selected auxiliary grades zero. The exact K2552 intertwiner Box_A R(f)=R(D5 f−14Kf) and (2) verify the Schur and Einstein source rows. Trace and divergence vanish, so the skew, mixed and BB rows vanish; auxiliary elimination verifies its own row. Thus EVERY selected linear row holds for this radial TT source class, including nonconstant radial sources. This is not an inverse for the scalar complement, arbitrary tensor sources, or all coupled homogeneous sectors.

## 5. Released original-metric observation

Put δ=μ−5K. Since the second operator in (2) equals the first minus δ, the same algebra now on the general radial module yields

    E h = −(rE/2)(1+rE/c) R(b) − (rE δ/2) R(u).         (10)

For any smooth compact tensor Wtest, set F=E Wtest. The Einstein Bianchi identity gives conservation of F; formal self-adjointness and compact support imply

    <F,h> = <Wtest,E h>.

This readout is continuous in the appropriate supplied data seminorms for the smooth reconstruction, or interior Sobolev spaces of adequate order. It includes the direct source term. The E-channel homogeneous preparation drops out at fixed source, but only for this compact Einstein-image detector class. This is not gauge equivalence or invisibility to every conserved detector. No independently calibrated physical Wtest is supplied.

## 6. Executed nonconstant radial source consumer

A manufactured exact solution checks all signs and the extra radial dependence without relying on numerical eigenvalues. Put q=S(r)² and a=S(R)². Direct differentiation gives

    D5 F(q)=4q(1−Kq)F''(q)+(10−24Kq)F'(q),
    D5 q=10−24Kq.

Take W0(q)=(q−a)^5, constant on B, and use the radial operators

    D_E=D5−16K, D_Q=D5+μ−21K.

Define

    u*=D_E W0,
    v*=−c D_Q W0,
    b*=−(c/rE) D_Q D_E W0.                              (11)

Commutation of these two polynomial differential operators gives D_Q u*=−rE b*/c and D_E v*=rE b*. Both amplitudes vanish at r=R. Since two second-order operators lower the order of vanishing by at most four, b* also vanishes there. Hence b* is in the radial Dirichlet H1 form domain, so with constant angular data it is an actual s=0 consumer of (9). All functions are smooth even at zero. This finite polynomial is not asserted to lie in EVERY Dirichlet spectral power; its smoothness is independently explicit.

Use actual B endpoint data computed from y_Q=J u*,y_E=J v* and (5). In spectral notation these are g0=k^−1 y'(0)+i y(0) and gd=k^−1 y'(d)−i y(d), mode by mode; k here includes the radial eigenvalue, so it is the positive spectral operator (4), not a single constant for the polynomial. The source and boundary data are legitimate in the s=0 sufficient classes: u*,v* vanish at R and are smooth, their derivatives in x only multiply them by bounded scalar functions, and k^−1 improves the spectral order. The uniform inverse therefore reproduces (11) by uniqueness. These endpoint data generally do not vanish.

The leading q5 coefficients are

    [u*]q5 = −216K,
    [b*]q5 = −216K c(221K−μ)/rE.

At κ=1, 221K−μ=−58476335/4439232512 ≠ 0, so the source is nonzero and genuinely nonconstant. The q5 coefficient of the radial amplitude in E h* from (10) is

    −477595265/411382839296 ≠ 0.

Thus E h* is not identically zero. Choose an interior point where it is nonzero and a compact test Wtest with a matching dual component supported in a sufficiently small neighborhood. The nondegenerate tensor pairing and continuity make <Wtest,E h*> nonzero; F=E Wtest is an actual compact conserved detector with nonzero readout. This is an existence construction of the detector, not a numerical calibrated integral.

The exact probe recomputes the source residuals, outer traces, TT identities, observation polynomial and gap constants. These checks support the formulas; the universal spectral and domain theorem is proved above.


## Verification and remaining frontier

Contrary controls change the radial eigenvalue sign, substitute the fixed-R(1) potential, omit the Einstein response or direct source term, confuse the shifted and original metric, and falsely infer spectral compatibility or full tensor Dirichlet data from scalar smoothness. Each is checked against an actual residual, coefficient, trace or readout. Universal proofs are separate from finite symbolic checks.

The next substantive question is whether the scalar cofactor complement can share this SAME fixed preparation, with compatible overlap and original-metric observation. The existing full-source construction under parameter-switched domains remains valid evidence. Independent physical boundary/control selection, sharper losses and arbitrary-annulus uniformity remain open.

[General impedance literature](https://arxiv.org/abs/1504.01037) treats different Helmholtz hypotheses and is background only. The present result follows from the actual weighted gap, shifted potentials and [K2576 estimates](k2576-polynomial-impedance-control-2026-11-05.md), with [K2552 all-row intertwiner](k2552-localized-source-domain-2026-11-04.md). See [K2562 prior source construction](k2562-parameter-dependent-response-2026-11-05.md), [K2564 distributional source response](k2564-localized-spectral-response-2026-11-05.md), [probe](../../tests/channel-swings/k2580_radial_angular_source_domain_probe.py) and [report](../../lab/process/k2580-radial-angular-source-domain.json).
