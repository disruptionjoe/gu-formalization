---
title: "K2319 Light-cone density readout"
status: active_research
doc_type: exploration
created: "2026-10-30"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematics only; no native physical acceptance
scripts:
  - tests/channel-swings/k2319_lightcone_density_readout_probe.py
---

# K2319 Light-cone density readout

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
result: K2319
carrier: supplied continuum Gaussian longitudinal-velocity seed and background null-ray scalar-density readout of the healthy dust-scalar model LAYER=toy CHIRALITY=N/A
pairing: spectral Gaussian isometry with measure d3k and real-space test-function duality ON=declared_carrier
real_structure: conjugate Fourier reality and real radial and angular selection
grading: linear scalar density and independent detector noise
action_owner: repository-construction -- unchanged K2311 equations, supplied continuum spectrum and background optical interpretation
target: sharp light-cone readout domain and detector response cost MAP-TYPE=evaluation
```

## Model, optical assumption and spectral convention

[K2311](k2311-uniform-constrained-dust-evolution-2026-10-30.md), [K2314](k2314-windowed-dust-observables-2026-10-30.md) and [K2317](k2317-spacetime-dust-windows-2026-10-30.md) supply the same healthy scalar/dust linear equations and the uniform transfer

    T(t,k)=k delta(t)+R(t,k), |R(t,k)| <= C/k,
    k=|bold k|, delta(t)>0 for t>t*.                       (1)

Here explicitly replace the torus by spatial R3. The isotropic ODE and its uniform high-frequency proof use real k>0 and k²/a², not integrality, so (1) transfers. Supply a real homogeneous Gaussian longitudinal-velocity seed with spectral density P(k), bounded, zero near k=0 and exactly1 for k>=k0>0. This is a new supplied continuum law, not a measured primordial spectrum or finite-energy realization. Define Gaussian spectral integration by Var(integral b dZ)=integral |b|²P(k)d³k with conjugate reality; no (2pi)^-3 is hidden in this convention.

Grant the background Jordan metric its usual physical optical interpretation. With Einstein-frame coordinates ds_E²=-dt²+a(t)²dx² and ds_J²=B(t)²ds_E², the unparameterized radial null curves agree: dt_J/a_J=dt/a. For observer time t_o define r(t)=integral_t^to ds/a(s), invert on a compact interval I strictly after t*. Fix 0<r0<r1 and select only radii whose emission times lie inside I. This is background null-ray transport with no perturbed ray displacement. Define, first at a spectral cutoff,

    Y_F = integral F(r) [integral_S2 n_J(t(r),r omega) dOmega/(4pi)] dr. (2)

This is a scalar-density functional on background null rays. It is not gauge-invariant observed galaxy counts, a luminosity-distance or lensing estimator, a redshift-bin model, or an empirical likelihood. Those need additional matter, selection and perturbed optical terms. SC-COS-50/51/54 remain ASSERTS, SC-META-53 UNCERTAIN; ledger0.263 LT-GR2e remains NEEDS. No GU prediction, physical initial-law selection or nonlinear dust claim follows.

## Exact radial criterion and a non-canceling repair

Spherical averaging gives sinc(kr)=sin(kr)/(kr). Let F be real L2 with support in[r0,r1], extend by zero, and set

    g(r)=F(r) delta(t(r))/r,
    B_F(k)=integral g(r) sin(kr) dr.

The complete transfer in(2) is B_F(k)+E_F(k), where |E_F(k)|<=C ||F/r||_1/k². Thus E_F belongs to L2(d³k) above k0. The exact Gaussian mean-square existence criterion is consequently

    Y_F exists iff the zero extension of g belongs to H1(R).         (3)

Indeed its leading variance is4pi integral k²|B_F(k)|²dk. Odd extension and Fourier Plancherel show that this integral is finite iff g has an L2 weak derivative and zero traces at both support endpoints. Removing bounded low frequencies does not change that iff; adding the L2 remainder cannot repair a non-L2 leading term. For the UNTRUNCATED leading multiplier with P=1 at all k, the exact identity is

    4pi integral_0^infinity k²|B_F(k)|² dk
      =2pi² integral_0^infinity |g'(r)|² dr.                       (4)

Equation(4) is not the full model variance with its cutoff and remainder. Compact support away zero makes multiplication by delta(t(r))/r a smooth invertible multiplier; equivalently the zero extension of F is H1. A sharp nonzero radial top-hat has endpoint jumps and fails. A single infinitesimal shell is outside the L2 premise and also diverges: its leading coefficient is proportional to sin(kr), whose k²-weighted integral diverges.

A positive repair does not need signed cancellation. Take g=(r-1)(2-r) on[1,2], zero elsewhere (rescale the support into the allowed interval), and F=rg/delta(t(r)). Then F>=0, integral F>0, g is H1 with zero endpoint values, and integral |g'|²=1/3. The uncut leading variance is2pi²/3. Divide F by its integral if a normalized selection is wanted; scale the variance by the square of that factor. This retains a positive response to the positive slow Jeans mode, unlike K2317's signed temporal compensation. It does not assert that tapering preserves every spatial signal or that C-infinity smoothness is necessary.

## Released angular discriminator

Let A in L2(S2) be a real angular weight, normalized by integral A dOmega=1 when an average is wanted, and replace1/(4pi) by A in(2). Define

    h(x)=F(r) delta(t(r)) A(omega)/r², x=r omega.

Its leading transfer is k times the Fourier transform of h with transform integral h exp(i k.x)d³x. The remainder is still L2 in k, including nonsmooth A. To see this, write S_A(r,k)=integral A(omega) exp(i k.r omega)dOmega. The Coulomb Fourier identity gives

    integral |S_A(r,k)|²/|k|² d³k
      = (2pi²/r) integral integral A(omega)conj(A(omega'))/|omega-omega'| dOmega dOmega'
      <= (8pi³/r) ||A||_2².                                      (5)

The last step is Schur's bound: integral_S2 |omega-omega'|^-1 dOmega'=4pi. A regularized Fourier kernel justifies the equality for smooth A; the bounded positive form extends to L2. Minkowski and(1) bound the remainder norm by C sqrt(8pi³)||A||_2 integral |F(r)|/sqrt(r)dr. Infrared removal only helps this bound. Therefore the exact criterion is

    Y_F,A exists iff h belongs to H1(R3).                          (6)

For nonzero radial and angular factors on this annulus, this is equivalent to zero-extended F delta/r² in H1 radially AND A in H1(S2). In spherical coordinates the Dirichlet integral separates as

    integral |grad h|² d³x
      = ||A||² integral r² |q'(r)|²dr
        + ||grad_S A||² integral |q(r)|²dr, q=F delta/r².           (7)

A genuine angular step with a jump across a smooth curve has a surface-measure weak derivative and is not H1. Thus a sharp hemisphere mask fails even with smooth radial taper. Conversely smooth angular taper plus the radial repair gives a finite signal. This is an actual mask boundary, not a finite spherical-harmonic cutoff claim. The all-sky criterion agrees with(3) because the radial identity integral r²|(g/r)'|²=integral|g'|² holds when endpoint traces vanish.

## Detector noise requires finite temporal response

Now separately supply additive spacetime white noise eta with covariance sigma² delta(t-t')delta³(x-x'), explicitly relative to coordinate measure dt d³x. It is independent of the coherently evolved spatial signal. White noise defined instead per FLRW proper volume has scale-factor weights and is a different supplied law.

The ideal readout kernel is F(r)A(omega)delta(t-t(r))/r², which is not L2(dt d³x). No nonzero such ideal readout has finite variance for this noise. This failure applies to zero-thickness spacelike surfaces too; it is not a special pathology of null cones. Smooth spatial taper alone does not repair it.

Supply a compact smooth unit-integral temporal response chi, and chi_tau(s)=tau^-1 chi(s/tau), tau>0. Replace the time delta by chi_tau. The exact noise variance is

    V_noise(tau)=sigma² ||chi||²_2 ||A||²_2 /tau
                   * integral |F(r)|²/r² dr.                     (8)

For full sky ||A||²=1/(4pi). Its 1/tau divergence is independent of the path t(r). The leading signal now uses delta_tau(r)=integral chi_tau(t-t(r))delta(t)dt. For smooth compact F,A, sufficiently small tau with all sampled times inside I, h_tau converges to h in H1. The remainder converges in L2 using (5), uniform |R|<=C/k, pointwise time continuity of the finite-k ODE and dominated convergence. Hence signal readouts converge in mean square as tau->0 while this noise diverges. No rate for the full signal follows from mere time continuity of R.

## Quantitative finite-exposure feasibility

A rate is now available by using more of the SAME constrained evolution. K2308 gives n_J'=qv+3Phi'-3beta pi. K2311 gives qv=s+beta p, pi=p+2beta mPhi', and beta²m=1/6. Therefore exactly

    n_J'=s-2beta p+2Phi'.                                        (9)

For the seeded transfer, its normalized slow estimate gives s=k delta'+O(1/k), while p and Phi' are O(1/k). Thus |partial_t R(t,k)|<=C1/k uniformly on the enlarged compact time interval. For example C1=C_s+2|beta|C_p+2C_P from the respective uniform bounds. Enlarge C1 if needed over the compact spectral transition band above its positive lower cutoff; finite-k ODE continuity supplies this bound. These constants depend on the supplied background and cutoff, not k. This uses the continuity equation, not differentiation of an unsupported big-O asymptotic.

Let m1=integral |u chi(u)|du, Pmax=sup P, D_j=sup_I |delta^(j)|, b(x)=F(r)A(omega)/r², and choose smooth compact F,A. For tau small enough that the entire response remains inside I,

    ||h_tau-h||_Hdot1 <= tau*m1 [D1||grad b||_2
                                  +D2||b t'(r)||_2].

Together with(5) and(9), this bounds the COMPLETE signal difference by

    RMSE(Y_tau-Y_0) <= C_obs tau,
    C_obs=sqrt(Pmax)*m1*{
       (2pi)^(3/2)[D1||grad b||_2+D2||b t'(r)||_2]
       +C1 sqrt(8pi³)||A||_2 integral |F(r)|/sqrt(r)dr}.            (10)

The Fourier Plancherel factor in(10) follows the unnormalized spatial transform used above. Supplied finite constants suffice; no numerical cosmological calibration is claimed. The polynomial response used in the probe is C1 after zero extension, not C-infinity, and still has the required compact L1/L2 moments.

Write D=sigma²||chi||²||A||² integral F²/r², so V_noise=D/tau. For positive supplied signal-RMSE tolerance epsilon, noise budget v_max and C_obs>0, a certified feasible exposure interval is

    D/v_max <= tau <= epsilon/C_obs,
    supp chi_tau around every t(r) contained in I.                (11)

The lower bound is necessary for this noise model; the upper bound is sufficient from(10), not a necessary signal-error limit. If the interval is empty, these certificates do not certify the two tolerances together; they do not prove every detector fails. This explicitly combines radial/angular selection, finite optical exposure and readout noise without canceling the leading Jeans response.

## Normalized taper construction and its precise optimization scope

There is also a useful exact construction at the leading-response level. For full sky, define w(r)=r/delta(t(r))>0 and require normalized F=wg, integral F=1 with g in H1_0(r0,r1). The UNTRUNCATED leading variance(4) is minimized by

    -u''=w, u(r0)=u(r1)=0,
    Z=integral w u=integral |u'|²>0,
    g_*=u/Z, F_*=w u/Z,
    V_lead,min=2pi²/Z.                                          (12)

Proof: the positive Dirichlet Green kernel gives u>0 inside, and integration by parts gives1=integral wg=integral u'g'. Cauchy-Schwarz yields integral|g'|²>=1/Z, with equality only for g=u/Z. Thus the normalized optimizer is positive, unique and signal-preserving at this specified leading-variance objective. It eliminates arbitrary radial-taper tuning for that objective.

For a fixed finite tau, a corresponding leading-plus-noise proxy minimizes

    a integral |g'|² + b0 integral g²/delta²,
    a=2pi², b0=sigma²||chi||²/(4pi tau).

Replace(12)'s operator by -a d²/dr²+b0/delta²; its Dirichlet inverse applied to w, normalized by its w inner product, is the unique positive minimizer, with minimum reciprocal inner product. This is a strictly coercive one-dimensional variational problem. It does NOT optimize the full transfer with R, the infrared-cut spectrum, exposure-induced change delta_tau, angular mask, or a real survey estimator. Those alter the objective. The simple delta=1 control on[1,2] has u=(-r³+7r-6)/6; it checks the variational construction, not the background cosmology.

## Verification and next test

The probe checks shell integration, radial derivative/endpoint identities, spherical energy separation, a genuine angular jump, temporal response scaling and changed-input countercontrols. Universal summability, covariance and domain statements rely on the proofs above, not those finite controls. The standard transform convention is consistent with [NIST DLMF §1.14](https://dlmf.nist.gov/1.14); the normalization in(4) is derived here.

The constructed observation now has explicit background light propagation and radial/angular/temporal requirements. A physically meaningful successor must specify an actual initial covariance and observed number-count/redshift/lensing functional with selection, noise and calibration together. In particular do not transfer(3) to the full gauge-invariant count observable before checking its derivative and boundary terms. Smooth noise coloring or finite angular beams are concrete alternatives to the white/sharp models; positivity of a time average alone remains insufficient for K2317's fixed spatial window.
