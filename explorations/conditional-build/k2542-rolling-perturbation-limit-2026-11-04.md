---
title: "K2542 Prepared rolling scalar-dust and tensor Einstein limit"
status: active_research
doc_type: exploration
created: "2026-11-04"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: compact-interval fixed-band prepared linear perturbation convergence; no primordial selection, nonlinear stability, empirical or native GU claim
scripts:
  - tests/channel-swings/k2542_rolling_perturbation_limit_probe.py
---

# K2542 Perturbations do not automatically escape background closure

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
result: K2542
carrier: full constrained scalar-dust and tensor Fourier perturbations of K2540 positive quadratic FLRW family LAYER=toy CHIRALITY=N/A
pairing: real modulated oscillator energy and common finite-band linear readout ON=declared_carrier
real_structure: real backgrounds, complex Fourier modes with conjugate reality pairing, F positive
grading: rolling constrained evolution, frozen static control, scalar preparation and observation are distinct
action_owner: repository-construction -- quadratic metric action with minimally coupled Jordan dust
target: common density lensing slip and tensor Einstein limit MAP-TYPE=evaluation
```

## Result, source boundary and prior work

For each fixed compact redshift interval and Fourier band bounded away from zero and infinity, the K2540 positive family admits common dust initial data and prepared scalar data whose **full rolling** density, lensing, slip and tensor responses converge to the Einstein-dust reference at rate O(1/A). Here A is the large normalized quadratic-action coefficient. This is an actual linear initial-value theorem, not a quasi-static approximation or a statement based only on the frozen scalar mass. Consequently these responses do not supply a uniform positive separation from that same admitted reference on this unbounded prepared family.

[K2367](k2367-sourced-fit-dust-transfer-2026-10-31.md) already owns the normalized rolling matrix, applying [K2308](k2308-inhomogeneous-constrained-dust-transfer-2026-10-30.md). Static scalar/Yukawa tests already exist in K1864/K1866/K2289. The new contribution is a uniform singular-limit argument on [K2540](k2540-prepared-cosmology-source-data-2026-11-04.md)'s repaired background, its common Jordan-data consumer and tensor follow-through. No new perturbation theory, novelty or observational acceptance is asserted.

SC-COS-50 ASSERTS its conditional variable-dark-energy demand, SC-COS-51 ASSERTS its connection-displacement/VEV claim, and SC-COS-54 ASSERTS the two-movable-fields claim. They do not select this metric action, its scalar initial state or dust normalization. LT-GR2e and ledger0.263 remain unchanged. Physical source, primordial covariance, ruler and laboratory coupling selection remain independent inputs.

## 1. Freeze the action, interval and common data

Use units H0=U0=1 and the same action form f(R)=alpha R+R²/2-rho, with alpha=A, rho=B. The physical action normalization remains an independent overall coefficient. In each member use the K2540 source-normalized background with fixed 0<Omega<1,

    s=3log(1+z), x(0)=1, x_s(0)=3Omega/4+delta,
    delta=d1/A+O(A^-2), d1=27(Omega/3+Omega²/8),
    B=6A(1-Omega)-(81/2)Omega²-72(1-3Omega/4)Omega
        +72(Omega-3)delta,
    F=A+R, R=12 x^(1/3)(x-x_s), F0=F(0),
    q=3F0 Omega exp(s).

K2540 supplies actual solutions on every fixed [0,S], positive x,F,B for large A, and x-r=O(A^-1), x_s-r_s=O(A^-1), x_ss-r_ss=O(A^-1), x_sss-r_sss=O(A^-1/2), where r=(1-Omega+Omega exp(s))^(3/4). Coefficient-complete actions and dimensional dust vary across the family; neither is held independently measured.

Fix 0<kmin<=kbar<=kmax<infinity, independent of A. Let beta=-1/sqrt6 (distinct from the running conformal coefficient). The exact Einstein-frame quantities are

    c=F/F0, aE=exp(-s/3)sqrt(c), ell=dtE/ds=-sqrt(c)/(3h),
    h=x^(2/3), br=-3F_s/F,
    H=h(1+br/2)/sqrt(c), u=sqrt(3/2)h br/sqrt(c),
    d=q F0/F²=3Omega exp(s)c^-2,
    V'=F0/sqrt6 [A/F-(A²+2B)/F²],
    V''=F0/3 [-A/F+2(A²+2B)/F²], Q=kbar²/aE².

The d normalization is essential. Omitting F0 changes the limiting matter problem. With Href=sqrt(1-Omega+Omega exp(s)), dref=3Omega exp(s), ellref=-1/(3Href), exact algebra and the stated background bounds give, uniformly on the band,

    c-1,c_s,c_ss=O(A^-1), u,u_s=O(A^-1),
    H-Href, ell-ellref, d-dref, Q-kbar²exp(2s/3)=O(A^-1),
    V'+beta d=O(A^-1), V''=A/3+O(1), (V'')_s=O(1).

For the cancellation use Rref=3Omega exp(s)+12(1-Omega), B/A=6(1-Omega)+O(A^-1). The derivatives needed below are uniformly bounded: R_s,R_ss are bounded by the K2540 estimates, so differentiating the rational expressions introduces no growing coefficient except the constant leading A/3. No fourth background derivative is needed.

## 2. Keep the complete constrained system

Write Y=(Phi,v), chi=delta phi/M, pi=dchi/dtE. K2367's exact reduced system is

    Y_s=ell [Bmat Y+e chi], chi_s=ell pi,
    pi_s=ell[-gamma pi-mu² chi+f], f=bvec Y,
    Bmat=[[-H,-d/2],[-1,-beta u]], e=(u/2,-beta),
    gamma=3H-beta u,
    mu²=Q+V''-2u²-3beta H u-beta V',
    bvec=(-4Hu-2V'-2beta d+beta(2Q-u²),
          -d(2u+3beta H)).

All entries of Bmat,e,bvec and their s derivatives are uniformly bounded on the stated interval/band. For sufficiently large A, c0 A<=mu²<=C0 A and |(mu²)_s|<=C. The system is regular for each finite A; the singular limit is in its fast scalar frequency, not an omitted constraint or an algebraic replacement of the scalar equation.

## 3. A modulated energy for the forced fast mode

First use real modes. For complex modes use |pi|²/2+mu²|chi|²/2-Re(conj(chi)f)+(K/A)||Y||², equivalently the sum of the real and imaginary energies. Choose a sufficiently large constant K independent of A and define

    E=pi²/2+mu² chi²/2-f chi+(K/A)|Y|².

Young's inequality with |f|<=C|Y| and mu²>=c0 A makes E comparable, above and below, to pi²+A chi²+|Y|²/A. Exact differentiation along the FULL system cancels both mu² chi pi and f pi:

    E_s=-ell gamma pi²+(mu²)_s chi²/2-f_s chi
          +(2K/A)Y dot Y_s,
    f_s=(bvec)_s Y+bvec Y_s.

Thus |f_s|<=C(|Y|+|chi|). Each remaining term is bounded by C E using |Y chi|<= (|Y|²/A+A chi²)/2. Hence |E_s|<=C E with C independent of A and kbar in the band. The negative ell is harmless: this two-sided bound proves the estimate in either direction along the finite interval.

At any common initial s_i in [0,S], prescribe bounded Y_i and chi_i=pi_i=0. Then E_i=O(A^-1); Gronwall yields

    Y=O(1), chi=O(A^-1), pi=O(A^-1/2).

The same estimate holds for chi_i=O(A^-1), pi_i=O(A^-1/2). Because ell Bmat differs from the Einstein dust matrix by O(A^-1), while ell e chi=O(A^-1), variation of constants gives Y-Yref=O(A^-1) for common or O(A^-1)-close initial Y. This proves actual finite-interval transfer convergence and rules out an unaccounted growing fast mode for this prepared data class. It is not a nonlinear stability or arbitrary-data theorem.

## 4. Use the same Jordan matter data and observation

The exact constraint and Jordan readouts are

    d n=-(2Q-u²)Phi-(3Hu+V'+beta d)chi+3Hd v-u pi,
    D_J=n-3beta chi, Phi_J=Phi+beta chi,
    Psi_J=Phi-beta chi, lensing=2Phi, slip=2beta chi,
    v_J=c^-1/2 v.

Prescribe the SAME bounded initial Jordan density D and velocity V for all A, with chi_i=pi_i=0. Set v_i=sqrt(c_i)V and

    Phi_i=d_i(3H_i v_i-D)/(2Q_i-u_i²).

Since kmin>0, the denominator is bounded away from zero for large A. These initial Y differ from their Einstein counterparts by O(A^-1). The evolution above then gives D_J-Dref, v_J-vref, both potential differences and lensing difference all O(A^-1), and slip O(A^-1). In the density formula u pi=O(A^-3/2); d has a positive uniform lower bound. This is a shared construction rather than separately fitted readouts. Perturbation amplitudes may be scaled down to stay in the linear regime.

## 5. Execute the independent tensor consumer

For the SAME Jordan background the exact transverse-traceless tensor amplitude satisfies

    hT_ss+(h_s/h-1+F_s/F)hT_s
        +kbar² exp(2s/3)/(9h²) hT=0.

The traceless mixed spatial metric row gives F deltaRic_TT-delta(Hess F)_TT=0: deltaRic_TT=(hT_tt+3h hT_t+kbar²/aJ² hT)/2, delta(Hess F)_TT=-F_t hT_t/2, delta R=0 and dust delta T_i^j|TT=0. Thus no extra tensor mass appears on this sourced background. The time change follows directly from hT_tt+(3h+F_t/F)hT_t+(kbar²/aJ²)hT=0 and dt/ds=-1/(3h); tensor matter anisotropic stress is zero for the admitted dust. All coefficients converge uniformly at O(A^-1) to Einstein's tensor equation on the fixed band. The ordinary first-order system and Gronwall give O(A^-1) convergence of hT and hT_s for common bounded initial tensor data. No fast scalar mode is hidden in this tensor step.

Any fixed bounded linear finite-band readout of these scalar and tensor observables consequently converges. A common finite-dimensional covariance of prepared dust and tensor initial data and finite observation covariance also yield convergent predicted covariance and continuous Gaussian loss where the limiting covariance remains positive definite. This does not select that covariance, primordial spectrum, absolute ruler or matter coupling. Nor does it prove that the reference fits observations. It removes the presumption that merely switching from background distances to these prepared finite-band perturbations must uniformly separate the unbounded family.

## 6. Contrary constructions and precise boundary

- If chi_i=c0!=0 is fixed, the initial slip is exactly 2beta c0 for every A. The prepared-data theorem cannot be extended to arbitrary scalar amplitudes.
- If chi_i=0 but pi_i=p0!=0 is fixed, put tau=sqrt(A)(tE-t_i), chi=A^-1/2 w. The original system has, on bounded tau, w_tau_tau+w/3=O(A^-1/2), w(0)=0, w_tau(0)=p0. The other fields remain bounded there by ordinary continuous dependence; its limiting solution is sqrt3 p0 sin(tau/sqrt3). Therefore the stronger O(A^-1) scalar rate fails. This is a fast-time limit of the actual system, not a claim of nonconvergence.
- As a separately labeled FROZEN static comparison, k²=m²=A/3 leaves scalar relative force correction 1/6 and gamma=5/7. This established Yukawa control illustrates why all-frequency uniformity is a different question; it is not a counterexample to the rolling fixed-band theorem and is not new physical evidence.
- Zero full perturbation data remain zero exactly. The proof neither divides by H nor discards dust/scalar feedback. The initial density chart needs kmin>0; the underlying reduced evolution has a wider chart, but its extension is not inferred here.

## Evidence and next question

The companion exact probe checks the actual matrix/constraint algebra, normalized large-A coefficients, modulated-energy cancellation, common Jordan-data seed, tensor time change and genuine changed-data/normalization controls. The universal uniform estimates and Gronwall argument are the proof; counts are finite controls and reproducibility evidence. No numerical sampling, internal review or exact symbolic fixture is external-expert or proof-assistant certification.

The primary review [De Felice and Tsujikawa, f(R) Theories](https://arxiv.org/abs/1002.4928) places the scalar/matter/tensor framework in its established context; its approximate formulas do not replace the exact IVP argument above. No novelty claim is made. A useful next discriminator needs independently selected scalar/primordial data, finite parameter bounds, nonlinear/local-gravity applicability or a specified changing-frequency experiment. More finite-band prepared growth fits alone do not remove the demonstrated closure.
