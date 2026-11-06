---
title: "K2603 Critical metric divergence rates and multiscale conserved observations"
status: active_research
doc_type: exploration
created: "2026-11-06"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: necessary logarithmic norm growth for the full selected metric; no matching upper estimate or physical apparatus
scripts:
  - tests/channel-swings/k2603_critical_metric_divergence_rates_probe.py
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
result: K2603
carrier: full metric distributions of the selected stationary Einstein product with compact conserved radial A pressure and localized B source LAYER=toy CHIRALITY=N/A
pairing: invariant tensor distribution/test pairing and explicitly auxiliary positive dual norms ON=declared_carrier
real_structure: real nonzero kappa, product signature7+7, local smooth charts
grading: full tensor including TT, compact source-contact observations, mathematical norms and physical gauge remain distinct
action_owner: repository-construction -- selected comm/symi/symi first-action completion
target: quantitative critical norms and aggregate detector conditioning MAP-TYPE=evaluation
```

# Critical divergence has a quantitative rate

## Result and source boundary

K2600 proved qualitative divergence of critical fixed-patch norms for the full metric. The new step is to combine ACTUAL curved compact conserved detectors at different scales. For every full response h_epsilon to the fixed nonzero compact conserved A-pressure times a B-source mu_epsilon of mass one, uniformly bounded total variation and support within C epsilon of an interior point,

    ||chi h_epsilon||L^(7/5) >= c [log(r0/epsilon)]^(5/7),
    ||chi h_epsilon||H^(-3/2) >= c [log(r0/epsilon)]^(1/2).       (1)

The Sobolev bound also holds in L2_A H^(-3/2)_B. The fixed cutoff chi equals one on a product patch containing the detectors below. Constants depend on the fixed source/patch/coefficient data and total-variation bound, not on epsilon or homogeneous preparation. The statement is for sufficiently small epsilon; infinite norms already satisfy it. No existence, matching upper bound, exact asymptotic coefficient, pointwise metric or sufficient regularity is asserted.

These are seven-dimensional B concentration estimates for the FULL selected metric, including all TT additions. SC-GEO-03 ASSERTS Met(X), SC-GEO-55 ASSERTS displacement from gauge-rotated Levi-Civita, and SC-ACT-01 ASSERTS the source first action. The present independently selected curved-product completion is not identified with those objects. SC-META-53 remains UNCERTAIN about indefinite spectra. Ledger0.263 LT-GR1b/6b/10 and LT-SM8, source and canon remain unchanged. No novelty or physical/GU certification.

## 1. Same nonzero contact signal at every admissible scale

Reuse K2548/K2600's identity for EVERY full selected-system solution,

    <h,D_phi>=-<t_A mu,F(X,Y)phi>,
    D_phi=E(G_A d(X,Y)phi), F=d/(12a0)-b_f/(36a0²),
    degree_Y d=degree_Y F=5,
    F_5/L_d=-424853/(149354 kappa)!=0.                    (2)

Both leading coefficients are constant in X. E is the full linearized Einstein map, not a scalar reconstruction. The test is compact and conserved. Homogeneous full-system responses and formal metric-gradient variations pair to zero. None of this selects a physical gauge or boundary condition.

Fix eta(A) with c_eta=<t_A,eta>!=0; K2600 proves such a test exists for any nonzero compact radial A-pressure. Choose a B-covector xi with q_b0(xi)!=0 for the wave principal form. Choose compact smooth phi equal to (xi dot z)^10/10! on a neighborhood of zero. Put

    T_r=r^10 D_[eta(A)phi(z/r)].                       (3)

For C'epsilon<=r<=r0, the source support lies in the polynomial core. Acting on that polynomial, the principal B term is constant; coefficients at z differ from their values at0 by O(epsilon), and lower derivative terms have factors r^(10-j), j<=9. After integration against the uniformly TV-bounded source,

    <h_epsilon,T_r>=-F_5 c_eta q_b0(xi)^5+O(r+epsilon). (4)

This is uniform in r and epsilon in the stated range, even for signed mass-one sources. Choose a fixed sign of the tests and sufficiently small r0; all these signals are at least c0>0. Centering or positivity of a mollifier is not required. A source of zero total mass has no such leading signal, so the theorem does not apply to a difference of two regularizations.

## 2. Preserve the curved operator in the scaling argument

Identify test tensor covectors using the invariant density and a fixed auxiliary positive norm dual to the field norm. The B differential order of D is at most12. A derivatives act on fixed eta, and all coefficient/density functions are smooth on a fixed compact chart. Thus

    T_r(A,z)=r^-2 Psi_r(A,z/r),                        (5)

where Psi_r has fixed compact support in A and the rescaled B variable and uniformly bounded derivatives of EVERY fixed order for0<r<=r0. A term of B order j<=12 has additional factor r^(12-j); differentiating its rescaled smooth coefficient preserves uniformity. This includes tensor frame changes and invariant density, rather than treating the indefinite metric contraction as positive. No flat operator replaces the curved detector.

Take r_j=r0*2^-j, j=0,...,N-1, ending while r_j>=C'epsilon. Then N is of order log(r0/epsilon). The finite sum S_N=sum T_rj is compact and conserved and, by(4),

    <h_epsilon,S_N> >= c0 N.                         (6)

## 3. Lebesgue endpoint by nested support

Equation(5) and nested supports give, up to fixed support constants,

    |S_N(A,z)| <= C max(|z|,r_(N-1))^-2

on the largest fixed B ball, and zero outside. In B dimension7 the inner ball contributes a bounded amount to the7/2-power integral; the rest has radial integral integral rho^6 rho^-7 d rho. Each dyadic shell contributes at most a constant. Fixed A support only changes that constant. Therefore

    ||S_N||L^(7/2) <= C N^(2/7).                     (7)

Duality between7/2 and7/5, with chi=1 on test support, proves the first bound in(1). This uses an upper bound for the norm of the test SUM; it does not presume disjoint supports or an annular lower bound on the metric.

## 4. Sobolev endpoint by an explicit cross-scale estimate

Joint Euclidean Fourier transformation on the compact coordinate patch gives

    hat T_r(alpha,zeta)=r^5 hat Psi_r(alpha,r zeta).

Uniform smooth compact profiles have uniform Schwartz bounds. For r<=R<=1 substitute zeta=w/R in the H^(3/2) inner product. The prefactor is r^5 R^5 R^-7; the weight obeys

    (1+|alpha|²+|w/R|²)^(3/2)
       <= R^-3 (1+|alpha|²+|w|²)^(3/2).

Bound hat Psi_r(alpha,(r/R)w) uniformly with rapid alpha decay, and hat Psi_R(alpha,w) with rapid joint decay. The remaining integral is bounded independently of r,R. Consequently

    |<T_r,T_R>H^(3/2)| <= C(r/R)^5.                  (8)

The identical proof with weight(1+|zeta|²)^(3/2) proves the L2_A H^(3/2)_B bound. This is why smooth varying coefficients do not invalidate the estimate. Summing the geometric series,

    ||S_N||H^(3/2)^2 <= C sum_ij 2^(-5|i-j|)
                       <=(33C/31)N.                 (9)

The anisotropic norm satisfies the same estimate. Equations(6) and(9) prove both negative-Sobolev assertions of(1). Local equivalent auxiliary norms only change constants. Repeating the SAME scale N times instead would give a Gram norm of order N² and no gain; almost orthogonality is a proved part of the argument, not a label.

## 5. Executed consequences: aggregate observations and resolution limits

Normalize the actual sum S_N by its dual norm. Its H^(3/2)-unit conserved observation has signal at least c sqrt N, whereas K2600's INDIVIDUAL critical Sobolev-unit tests had order-one signal. Its L^(7/2)-unit observation has signal at least c N^(5/7). The finite sum retains homogeneous-response annihilation and formal metric-gradient invariance from(2). All observations remain contact-supported; source-disjoint compact-adjoint tests have zero signal.

For an error tensor e with ||chi e||H^(-3/2)<=delta, the normalized Sobolev observation changes by at most delta; the analogous Lebesgue statement uses L^(7/5). Thus these are deterministic conditioning estimates in specified auxiliary norms. They do not assume a noise distribution or a physical sensor.

Conversely, a family constrained by an a priori critical norm budget B cannot resolve arbitrarily small mass-one sources in this selected system. Rearranging(1) gives necessary bounds of the form

    epsilon >= r0 exp[-C_H B²]        (Sobolev budget),
    epsilon >= r0 exp[-C_L B^(7/5)]   (Lebesgue budget),        (10)

with fixed constants and in the small-epsilon range of the theorem. A fixed additive constant inside the logarithm may be absorbed into r0. These are necessary resolution bounds, not sufficient reconstruction guarantees; the constants are not calibrated physical numbers. This is an actual consumer of the rate, beyond repeating qualitative divergence.

## Evidence and limitations

The bump-scaling and almost-orthogonality method is standard harmonic analysis; [Tao's harmonic-analysis appendix](https://www.math.ucla.edu/~tao/preprints/chapter.pdf) supplies methodological context, not the selected-system theorem. Here(5)--(9) prove the needed estimate directly.

The probe pins and checks the actual K2600 contact coefficient, tests the shell integral and geometric Gram sum, and uses a Gaussian Fourier-profile fixture with exact cross-scale integrals. The Gaussian fixture is NOT compact and is NOT the curved conserved detector; it tests the algebraic scaling against an independent computable model. The uniform-profile proof above supplies the actual theorem. A flat seven-dimensional Newton kernel |z|^-5 has the same critical logarithmic exponents, but this does not prove a matching full-system upper bound.

Controls reject identical-scale amplification, zero-mass signal transfer, characteristic covectors, zero A-trace, a14D scaling substitution and a putative uniform bounded critical field. Next seek matching sufficient local response regularity or an independently specified physical/source-disjoint readout; neither follows from these necessary bounds.

[K2600](k2600-full-metric-contact-regularity-2026-11-06.md), [K2548](k2548-compact-coupled-metric-detectors-2026-11-04.md), [probe](../../tests/channel-swings/k2603_critical_metric_divergence_rates_probe.py), [report](../../lab/process/k2603-critical-metric-divergence-rates.json).
