---
title: "K2325 Relativistic count and finite-energy covariance"
status: active_research
doc_type: exploration
created: "2026-10-30"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematics only; no native physical acceptance
scripts:
  - tests/channel-swings/k2325_relativistic_count_covariance_probe.py
---

# K2325 Relativistic count and finite-energy covariance

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
result: K2325
carrier: first-order scalar conserved-dust counts on the same Jordan metric with test null photons and a supplied homogeneous Gaussian seed LAYER=toy CHIRALITY=N/A
pairing: conserved-current pullback and common Gaussian spectral covariance ON=declared_carrier
real_structure: real fields and conjugate Fourier modes
grading: linear scalar perturbations; sky harmonics
action_owner: repository-construction -- K2311 designer dust-scalar action plus declared metric photon and count interfaces
target: full linear scalar volume-limited count, quadrupole endpoint and finite-energy seed repairs MAP-TYPE=evaluation
```

## Result and scope

The gravitational redshift, radial ray displacement and observer terms do not cancel [K2323](k2323-born-lensing-observer-domain-2026-10-30.md)'s quadrupole white-ultraviolet divergence for the specified conserved-dust catalog. We construct their common first-order count operator and prove this at the kernel level. We then construct a positive colored seed family: finite expected initial kinetic-energy density already removes this obstruction and makes smooth full counts well defined; stronger decay is required for pointwise evolved density. The action does not choose this covariance. A white-seed failure is not an exclusion of the action or GU.

Keep [K2311](k2311-uniform-constrained-dust-evolution-2026-10-30.md)'s healthy action, longitudinal initial velocity seed, exact constrained transfer, and entire compact foreground interval strictly after t*. Use the R3 extension and spectral normalization Var(Y)=integral P(k)|B(k)|²d³k in [K2319](k2319-lightcone-density-readout-2026-10-30.md). Add test photons following null geodesics of the Jordan metric; count unbiased conserved dust worldlines in a volume-limited catalog, with selection S=1. No flux cut, magnification bias, extinction, tracer creation, vector/tensor perturbations or nonlinear catalog is included. These are explicit observation assumptions, not consequences of the scalar action.

SC-COS-50/51/54 and SC-ACT-01/GEO-55 remain ASSERTS; SC-META-53 remains UNCERTAIN. Ledger0.263 LT-GR2e/GR6b/SM8 stays unchanged. Source connection-distortion and observation are distinct from this conventional metric model. No measured primordial law, empirical confidence, novelty or native GU physics follows.

## Current, null rays and the common observation map

Write

    ds_J²=a_J²[-(1+2Phi_J)deta²+(1-2Psi_J)dx²],
    W=Phi_J+Psi_J=2Phi, Hc=a_J'/a_J>0.

A dot below means partial_eta, n points from observer to source, V_r=n.V, and D_r=partial_r-partial_eta is the derivative on the background past cone. Fix observer coordinate position/time and use its orthonormal tetrad for angles. Start with finite spectral cutoff so every point value exists. Define

    I(r,n)=integral_0^r W(s,n)ds,
    J(r,n)=integral_0^r dot W(s,n)ds,
    Z=Phi_J,o-Phi_J+V_r-n.V_o-J.                         (1)

Z is the log-redshift perturbation at fixed emission time. Fixed observed redshift gives delta_eta=Z/Hc. The radial null equation and tetrad aberration give

    delta_r=-Z/Hc+I,
    delta_theta=-V_o,perp-integral_0^r (r-s)/(rs) grad_S W(s)ds.  (2)

The radial null relation is delta_eta+delta_r=I. The angular displacement here maps observed directions to source coordinates; its inverse has K2323's positive alpha convention.

For the conserved number current Jmu=n_phys u^mu,

    sqrt(-g_J)Jeta=n_com(1+n_J-3Psi_J),
    sqrt(-g_J)Ji=n_com Vi,   n_com=a_J³ nbar_phys=constant.

The lapse cancels between sqrt(-g) and ueta. Pull its three-form back through the perturbed cone; the background cone slope is -n and its flux contributes +V_r. The spatial Jacobian contributes D_r delta_r+2delta_r/r+div_S delta_theta. The result is

    Delta=n_J-3Psi_J+V_r+(D_r+2/r)delta_r+div_S delta_theta. (3)

There is no background n_com time-shift term because it is constant. Derivatives of a perturbation multiplied by a displacement are second order and absent. A variable selection or nonconserved tracer would change (3).

Jordan dust obeys dot V_r+Hc V_r+partial_r Phi_J=0. Differentiating (1) on the cone gives

    D_r Z=partial_r V_r+Hc V_r-dot Psi_J.

Substitute into (3), using D_r Hc=-dot Hc:

    Delta=n_J-partial_r V_r/Hc+dot Psi_J/Hc+Phi_J-2Psi_J
          -A Z+2I/r
          -integral_0^r (r-s)/(rs) Delta_S W(s)ds+2 n.V_o,
    A=dot Hc/Hc²+2/(r Hc).                             (4)

This independently derived current/Jacobian formula agrees with the Newtonian-gauge volume-limited expression in [Bonvin and Durrer, What galaxy surveys really measure, Eqs.6,22,27,31](https://arxiv.org/pdf/1105.5280), after translating photon-direction and potential conventions. Their final expression omits observer monopole/dipole terms; they are retained here. The kinematic derivation uses geodesic dust/null photons, not an Einstein-field-equation substitution for our action.

A fixed-proper-age observing event requires a supplied coordinate lapse delta_eta_o and its initial clock hypersurface. Replace Z by Z+Hc_o delta_eta_o and delta_r by delta_eta_o-(Z+Hc_o delta_eta_o)/Hc+I. The extra term is (D_r+2/r)[(1-Hc_o/Hc)delta_eta_o], a monopole. We do not manufacture this clock datum. The stated coordinate-event model is already definite; the quadrupole conclusion is independent of this optional clock completion.

## Exact comparison and the cancellation test

Let Delta_count denote [K2321](k2321-radial-count-operator-2026-10-30.md)'s current and Doppler map with S=1, and Delta_L the K2323 angular term. Then

    Delta=Delta_count+Delta_L+(D_r+2/r)E+2 n.V_o,
    E=I+(Phi_J+J-Phi_J,o+n.V_o)/Hc.                    (5)

For smooth compact-annular w, integration on the cone gives exactly

    integral r² w (D_r+2/r)E dr dOmega
        =-integral r² (partial_r w) E dr dOmega.        (6)

The derivative of w here is its radial weight derivative; E is restricted to the cone before differentiation. There is no extra 2/r on the right. This avoids unjustified differentiation of asymptotic error terms.

Take w=F(r)Y20(Omega)/r², F smooth supported inside r0<r<r1, M2=integral F nonzero and Y20 real L2-normalized. K2321's paired local count kernel is L2(d³k). Observer scalar and vector terms have only harmonics0 and1 and pair to zero at EACH finite cutoff. No white-noise point evaluation has been assumed to exist.

K2311's exact equations give, uniformly on the entire foreground interval,

    T_W=p(s)/k+O(k^-3), p=-a² d_bg delta/m, p(0)!=0,
    T_dotW=dot p(s)/k+O(k^-2),
    T_PhiJ=O(k^-1).                                    (7)

The time-derivative estimate follows from the exact first equation of K2311: dPhi/dt=(-H+beta u)Phi-d_bg v/(2m)+alpha W_normal. Here W_normal is K2311's scalar normal-form variable, NOT the Weyl potential W; its unnormalized seed transfer is O(k^-2), while Phi,v are k^-1 times their limiting coefficients plus O(k^-3). Thus (7) does not differentiate a big-O claim. Conversion from cosmic to conformal time multiplies by bounded smooth a.

The local-potential quadrupole term from (6) is O(k^-2), using |j2(kr)|<=C/(kr) on the annulus. Swapping I,J with the source integral produces bounded foreground weights even at s=0. Since integral_0^r1 |j2(ks)|ds<=C(1+log k)/k, their kernels are O((1+log k)/k²). These are L2, unlike the lens M2/s endpoint. Therefore

    B_full,2(k)=-8pi p(0)M2 Y20(khat)/k+G(k),  G in L2(d³k). (8)

For UV-white P=1, normalized Y20 and cutoff Lambda,

    Var(Y2,Lambda)/Lambda -> 64pi² p(0)² M2².           (9)

Shared-seed cross terms remain included; the L2 remainder contributes o(Lambda) by Cauchy-Schwarz. Gravitational/integrated redshift and time delay cannot cancel this endpoint in the declared model.

For the positive normalized weight F(1+epsilon Y20)/(4pi r²), harmonic orthogonality under isotropic P gives AT LEAST the quadrupole divergence. The total variance need not have coefficient(9), because observer monopole terms can themselves diverge. Equation(9) is a quadrupole statement, or applies after removing harmonics0 and1. A claim that all observer point measurements have white-seed limits would be false.

## Released repairs: covariance with finite energy and density regularity

For the quadrupole (8), bounded P(k) asymptotic to c k^-alpha, c>0, yields finite variance iff alpha>1. Because P is bounded, the full remainder G in (8) belongs to L2(P d³k). The leading term belongs to that weighted space exactly when alpha>1; adding a member cannot cure nonmembership. This uses no unproved pointwise bound on the entire local-count remainder. K2323's compensated smooth quadrupole with M2=0 also survives (5), including the added terms. Neither statement supplies full nonlinear observations.

A stronger physical regularity discriminator is available without inventing an inflationary history. At t*, the initial longitudinal physical velocity transfer is i khat/a* times the scalar seed. Its expected kinetic energy PER UNIT VOLUME, using positive background mass density rho*, is

    Ekin/V=rho*/(2a*²) integral P(k)d³k.                (10)

Homogeneous fields on R3 do not have finite total energy; (10) is a local expectation. Supply the positive spectral family

    P_q(k)=C 1_{k>=k0}(1+k²/K²)^(-q),
    C>0, K>0, k0>0, q>0.                                  (11)

It defines a real homogeneous isotropic Gaussian spectral measure and satisfies the same constraints mode by mode. At high k, elementary radial power counting gives:

| Requirement for this family | Exact strict threshold |
|---|---|
| Nonzero quadrupole lens/full-count variance | q>1/2 |
| Initial expected local kinetic energy and pointwise velocity variance | q>3/2 |
| Evolved density point variance at a fixed time after t* | q>5/2 |

At equality each diverges logarithmically. The last threshold uses T_n=k delta(t)+O(k^-1), delta(t)>0, not parameter counting. It is compatible with finite velocity energy but rough density for 3/2<q<=5/2. The integrals with a hard infrared gap differ by finite low-frequency terms from familiar whole-line integrals; no zero-mode constraint has been silently filled.

For q>3/2 smooth compact-annular FULL counts are finite, including the observer terms at fixed coordinate event. K2321's source kernel is L2 for white noise and remains so under bounded P_q. The source-potential and bounded foreground terms can also be paired directly with finite-variance point potentials: their transfers are uniformly bounded for k>=k0. Observer velocity/potential transfers are uniformly bounded and integral P_q finite. For the lens, integrate Delta_S onto the smooth weight. Below sources its coefficient is Delta_S M/s plus bounded terms. Its angular mean is zero; replacing exp(i sk.n) by exp(i sk.n)-1 bounds the singular integral by C(1+log k). With T_W=O(1/k) and the exact remainder controlled as in K2323, |B_L(k)|<=C(1+log k)/k, hence bounded for k>=k0. Integral P_q finite then proves lens variance finite without a falsely pointwise differentiated white field. All components use the SAME seed; the finite sum is finite with cross covariance intact.

For q>5/2 the evolved point-density variance is finite uniformly on a fixed compact background interval. Since all variances scale linearly with C, one may choose C small enough to meet any prescribed finite root-mean-square perturbation threshold on that interval. This is an existence/construction statement for a supplied covariance, not a measured normalization, action-selected initial state, almost-sure global positivity, nonlinear dust solution or caustic theorem. Gaussian amplitudes remain unbounded; small RMS is not strict pointwise positivity. Thus the white-seed obstruction rejects a statistical/observation combination, while the SAME action has explicit positive finite-energy statistical repairs.

## Verification and next question

The companion exact probe checks current/lapse cancellation, null displacement, radial Jacobian and adjoint, observer aberration, Euler reduction, same-seed covariance, harmonic orthogonality and strict power thresholds. Mutations change formula coefficients, signs or spectra and must fail clean evaluators. The continuum estimates and transfer of the action use the written proofs and pinned predecessor evidence, not finite sampling. Independent review must challenge the observer boundary, distinct spatial/cone derivatives and the normal-variable/Weyl-variable homonym.

Next obtain a physically justified initial covariance and actual tracer/selection/observer resolution, or compose these kernels with a declared survey likelihood. Finite energy restricts a possible covariance but does not select its shape or amplitude. A flux-selected tracer changes the lens coefficient and must be derived separately. The full native GU action/observation bridge remains open.
