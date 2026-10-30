---
title: "K2321 Radial count operator"
status: active_research
doc_type: exploration
created: "2026-10-30"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematics only; no native physical acceptance
scripts:
  - tests/channel-swings/k2321_radial_count_operator_probe.py
---

# K2321 Radial count operator

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
result: K2321
carrier: conserved dust current on a fixed background cone, radial Doppler coordinate map and supplied Gaussian seed LAYER=toy CHIRALITY=N/A
pairing: physical current flux, count pushforward and Gaussian spectral covariance ON=declared_carrier
real_structure: real count contrast with conjugate Fourier modes
grading: first-order scalar perturbations; no native Clifford identification
action_owner: repository-construction -- same K2308/K2311 healthy designer dust-scalar equations and supplied catalog map
target: current-to-count operator, elliptic window domain and displacement-noise cost MAP-TYPE=evaluation
```

## Scope: a physical current with a deliberately restricted optical map

[K2319](k2319-lightcone-density-readout-2026-10-30.md) was a scalar-density readout. Here retain the SAME healthy designer dust/scalar model and its continuum extension, the same real homogeneous Gaussian longitudinal-velocity seed with bounded P(k), zero below a positive infrared cutoff and equal to1 at sufficiently large k. No physical primordial spectrum is inferred. On a compact background time interval strictly after t*, choose an annulus 0<r0<r<r1 whose background-cone times t(r) lie in that interval, with dt/dr=-a(t).

Use conformal Newtonian coordinates in the Jordan frame,

    ds_J²=a_J²[-(1+2Phi_J)deta²+(1-2Psi_J)dx²],
    a_J=B a, Phi_J=Phi+beta chi, Psi_J=Phi-beta chi,
    n_J=n-3beta chi, V=grad(v)/a.

Here n_J is fractional physical number density, not coordinate counts. The Einstein variables and real Fourier convention exp(i k.x) are those of [K2308](k2308-inhomogeneous-constrained-dust-transfer-2026-10-30.md) and [K2311](k2311-uniform-constrained-dust-evolution-2026-10-30.md). Conformal transformation leaves peculiar V unchanged. The conserved Jordan dust current is J^mu=nbar_J(1+n_J)u_J^mu and a_J³ nbar_J=n_com is constant.

We count crossings of the FIXED coordinate surface eta=eta_o-r, keep sky angles fixed, and prescribe only the Doppler radial coordinate map s=r+d, d=V_r/ℋ_J, where ℋ_J=a(H+beta u). This is an explicit mathematical observation model. It omits perturbed photon trajectories, gravitational/integrated redshift, observer terms, lensing, magnification and source bias. It is not the full gauge-invariant observed galaxy-count observable. See [Bonvin and Durrer (2011)](https://arxiv.org/abs/1105.5280) for why that full relativistic observable requires more terms. Success here does not supply them or alter SC-COS-50/51/54, SC-META-53 or ledger0.263 LT-GR2e.

## Conserved-current flux before redshift displacement

The directed coordinate surface element has components proportional to (1,omega_i)r²dr dOmega. To first order,

    sqrt(-g_J)=a_J^4(1+Phi_J-3Psi_J),
    u_J^eta=a_J^-1(1-Phi_J), u_J^i=a_J^-1 V^i.

Thus current flux per coordinate volume r²dr dOmega is

    n_com[1+Delta_c],
    Delta_c=n_J-3Psi_J+V_r = n-3Phi+V_r.             (1)

The lapse cancels. The conformal scalar contribution also cancels between density and volume. Replacing (1) by n_J alone loses a geometric volume term and a crossing-velocity term even on this fixed cone. The surface itself is not varied; (1) therefore must not be advertised as a gauge-invariant catalog prediction.

## Exact radial Jacobian, selection placement and chain rule

First work with a smooth finite spectral cutoff and sufficiently small perturbation so s>0 and 1+D_r d>0. For s=r+d(r,omega), the spatial Jacobian is exactly

    J_map=(s/r)²(1+D_r d),
    D_r=partial_r|t-a partial_t.                              (2)

Angular derivatives of d occupy offdiagonal entries of a triangular radial/angular Jacobian and do not change its determinant. The true-radius selection S(r) is a supplied smooth strictly positive function on the annulus, bounded with its derivatives and inverse. Number conservation gives

    1+Delta_s(s,omega)=S(r)[1+Delta_c(r,omega)]/[S(s)J_map].

Linearizing at the same background coordinate s=r yields

    Delta_s=Delta_c-D_r d-alpha d,
    alpha=2/r+S'/S.                                         (3)

If instead selection is applied after mapping as S(s), it cancels from the normalized contrast and the S'/S term is absent. A sharp or vanishing S cannot be inserted into S'/S: it requires unnormalized distributional count treatment. Angular mask discontinuity is likewise an observation-window issue, not a smooth selection coefficient. Equation (3) uses the derivative of the whole restricted field; replacing D_r by the spatial partial derivative omits time evolution along the cone.

The infinite-cutoff Gaussian result below is a LINEAR functional limit of (3). White-seed samples need not define a pointwise invertible nonlinear map. The finite-cutoff derivation does not establish nonlinear stochastic dust flow or nonlinear catalog existence.

## Exact transfer and the sign of the leading count response

Let T_n,T_Phi,T_v be the exact real seeded transfer functions at t(r),k inherited from K2311. Write mu=omega.khat and

    U=k T_v/a, D=U/ℋ_J.

For the mode exp(i k.r omega), (1)--(3) give the exact scalar transfer

    C(r,mu,k)=T_n-3T_Phi+k mu²D
              +i mu[U-D_r D-alpha D].                       (4)

D_r D here differentiates its background/time coefficient only; the derivative of the Fourier exponential has already produced +k mu²D. There is no sign choice fitted to make the response positive.

For the same designer fixture, let x=1/a_J, F=1-A0*x^(-p)>0, A0=2/5 and p=(5+sqrt73)/4, as in [K2305](k2305-regular-constrained-matter-transfer-2026-10-30.md). This is the healthy designer conformal factor, not the earlier quadratic-action factor. Its existing background formulas give

    h:=H+beta u=x^(3/2)/sqrt(F)>0,
    ℋ_J=a h=sqrt(x)>0.                                      (5)

Thus division uses the Jordan conformal expansion, which stays positive even at the Einstein H=0 turnaround. On this compact post-t* interval K2311 proves delta,delta'>0 and

    T_n=k delta+O(k^-1), T_v=a² delta'/k+O(k^-3),
    T_Phi=-a² d_bg delta/(2m k)+O(k^-3).

Here d_bg is background dust density, distinct from radial displacement d. Set c=delta'/h>0 and L=a delta'-c_r-alpha c. Then

    C=k(delta+c mu²)+i mu L+sum_{j=0}² mu^j O(k^-1),          (6)

uniformly on the annulus. The derivative remainder in (6) is justified by the exact Euler equation, not by differentiating big-O: v'=-(1+2beta²m)Phi-beta u v-beta W with W=O(k^-2) shows the time derivative of the O(k^-3) velocity remainder is O(k^-2). Consequently D_r(D-c)=O(k^-1). K2319 supplies the n_J remainder; T_n=T_nJ+3beta*T_chi and T_chi=O(k^-1) supply the stated n remainder, and smooth bounded background factors preserve these bounds. The transfer functions are smooth on the compact nonzero infrared transition band.

The principal matrix is A=delta I+c omega omega^T, with eigenvalues delta,delta,delta+c, uniformly positive on this annulus. Density and Doppler distortion reinforce each other in this seed/model; a cancellation conclusion would require a different sign, background, seed or observable. Positivity is proved for this fixture, not assumed from ordinary expanding-cosmology intuition.

## Complete white-seed covariance and an exact window criterion

For real zero-extended compact-annular w in L2(R3), define at finite cutoff

    Y_w=integral w(x)Delta_s(x)d³x,
    B_w(k)=integral w(r omega) C(r,omega.khat,k)e^(i k.x)d³x.

With K2319's spectral convention, the exact covariance is

    Cov(Y_w,Y_z)=Re integral P(k) B_w(k)conj(B_z(k))d³k.       (7)

It uses the SAME seed in all density, volume and velocity terms, not independent fitted covariance components. The stochastic integrals exist in mean square exactly when the respective spectral kernels are square integrable. The result is

    Y_w exists iff the zero extension of w belongs to H1(R3). (8)

Here is why lower terms cannot change this iff. The i mu L term is a sum of bounded Riesz multipliers of Fourier transforms of L omega_i w, hence L2 bounded by Plancherel. For a remainder mu^j R_j(r,k) with |R_j|<=C/k, write angular components as products of at most two omega_i and khat_i. K2319's spherical Coulomb/Schur bound gives

    ||k^-1 integral A_r(omega)e^(ik.r omega)dOmega||_L2(d³k)
       <=sqrt(8pi³/r)||A_r||_L2(S2).

Minkowski then bounds the integrated remainder by a constant times
integral r^(3/2)||w(r,.)||_2 dr <= constant ||w||_L2 on the fixed annulus. A bounded r,k coefficient R_j*k may be taken outside this shell norm by its uniform bound. This works for arbitrary L2 angular masks, not only smooth harmonics. The compact infrared band is harmless.

For the leading part define the second-order operator

    Qw=-Delta(delta w)-partial_i partial_j(c omega_i omega_j w).

Its Fourier transform obeys B_lead(k)=|k|^-1 Fourier(Qw). Also

    Qw=-div(A grad w)-div(b w),
    b_i=partial_i delta+partial_j(c omega_i omega_j).

Extend A smoothly and uniformly positively off the annulus, where w=0. Since b is bounded, div(bw) lies in H^-1 for L2 w. Smooth uniformly elliptic distributional regularity gives

    ||w||_H1 <= C(||Qw||_Hminus1+||w||_L2),

and the reverse boundedness holds by the divergence formula. One route to the estimate is the order-minus-two elliptic parametrix: it maps H^-1 to H1, with the smoothing remainder bounded by ||w||L2; localization contains the compact support and introduces only lower-order bounded terms. No boundary regularity is presumed, since w is zero-extended on R3 and its jumps remain distributional derivatives. Equivalently use the shifted coercive divergence operator and its distributional elliptic regularity. Thus Qw in H^-1 iff w in H1. Near k=0, Fourier(Qw)=O(k²) from compact support and its double-divergence form, so division by |k| causes no infrared singularity. Since P=1 at high k, (8) follows. Adding the proved L2 remainder cannot cancel a non-L2 leading part.

For nonzero separated weights w=F(r)A_sky(omega)/r² on the annulus, (8) is equivalent to zero-extended F in H1 in the radial variable and A_sky in H1(S2). A genuine nonzero radial step or angular step fails. Positive radial and angular tapers succeed; no signed compensation of the slow mode is needed. For an explicit positive normalized repair, take G(r)=(r-r0)(r1-r) inside the annulus and zero elsewhere, F=6G/(r1-r0)^3, and nonnegative smooth A_sky with integral1. Then integral F=1, integral|G'|²=(r1-r0)^3/3 and w=F A_sky/r² lies in H1. Positivity alone is insufficient: a square-root edge can be positive while its derivative fails L2.

This preserves K2319's threshold for a NEW elliptic current-count operator, through the proof above rather than a transfer by analogy.

## Released consequence: count and displacement noise have different costs

Supply independent coordinate-spacetime white count noise xi and radial-displacement noise zeta, with covariances sigma_c² delta(t-t')delta³(x-x') and sigma_d² delta(t-t')delta³(x-x') relative to dt d³x, also independent of the seed. Use a finite compact smooth unit-integral response chi_tau(t-t(r)), tau>0, before differentiating the complete restricted displacement. Let nu_sel=S n_com and

    Delta_noise=xi_tau-nu_sel^-1 div(nu_sel omega zeta_tau).

For smooth compact w, integration by parts gives the displacement adjoint weight

    b_w=nu_sel partial_r(w/nu_sel)=partial_r w-(S'/S)w.

Hence the exact noise variance is

    Vnoise=||chi||²/tau [sigma_c²||w||²+sigma_d²||b_w||²].    (9)

The 2/r area term in the forward count map cancels against the volume integration in its adjoint; omitting it before integration gives the wrong noise cost. No separate chi_tau' term survives because the derivative acts on the entire smoothed displacement field before integration by parts. If the primitive noise is in physical velocity instead, replace b_w by b_w/ℋ_J. The formula extends by H1 density. A nonzero ideal zero-thickness readout of either white channel is not defined; finite tau and a radial derivative budget are essential. Correlated errors require cross covariance rather than the independent sum (9).

A supplied deterministic calibration error zeta_cal in L2 gives |delta Y|<=||b_w||2||zeta_cal||2. Thus the same adjoint norm controls white displacement noise and worst-case radial calibration bias. This is a genuine derivative-sensitive requirement absent from density-only detector noise. The finite exposure changes the signal and must be modeled as well; (9) is not a joint signal-error optimum or an automatic extension of K2319's exposure constant to all derivative terms.

## Verification and the next physical boundary

The companion probe checks current-flux/frame cancellation, exact Jacobian and selection placement, the cone chain rule, transfer sign, fixture expansion, elliptic eigenvalues, radial taper energy, displacement adjoint and covariance identities. The polynomial temporal-response fixture is compact L1 intersect L2, not a smooth zero extension; its normalization and noise-scaling checks need only those integrability properties. Exact symbolic fixtures test these identities; the continuum iff and arbitrary-mask lower-order bounds rest on the written argument and independent review, not finite Fourier sampling.

A full observed-count model must now supply perturbed-ray/redshift/observer terms, tracer selection/bias and a physical initial covariance in this SAME action before likelihood or native interpretation. Positive ellipticity is not guaranteed after changing those objects, and this result does not license deleting their terms. No source, ledger, canon, native GU prediction, external-expert certification or empirical likelihood changes.
