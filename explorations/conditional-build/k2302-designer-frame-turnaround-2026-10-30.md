---
title: "K2302 Designer frame turnaround and matter completion"
status: active_research
doc_type: exploration
created: "2026-10-30"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional construction only; no native physical acceptance
scripts:
  - tests/channel-swings/k2302_designer_frame_turnaround_probe.py
---

# K2302 Designer frame turnaround and matter completion

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
result: K2302
carrier: real four-dimensional metric f(R), FLRW scalars and specified matter fields LAYER=toy CHIRALITY=N/A
pairing: Lorentzian metric action and local kinetic forms ON=declared_carrier
real_structure: real coefficients; complex Fourier or Hilbert representation only where stated
grading: stated native Clifford grades or ordinary scalar/number grading; no identification
action_owner: repository-construction -- supplied metric f(R) and explicitly chosen matter
target: regular conformal frame and matter principal propagation MAP-TYPE=evaluation
```

## Exact frame-domain classification

Retain [K2299](k2299-finite-curvature-designer-family-2026-10-30.md): E=Mx³+Nx⁴+L, M>0,N,L>=0, x>=1, F=alpha-A v,0<A<alpha, v(1)=1,v>0,v'<0. Source SC-COS-50/51/54 ASSERTS connection-distortion claims; this supplied metric model does not identify with them. Ledger0.263 and LT-GR2e remain unchanged.

Set s=log x, n=xE'/E>0,w=-v_s>0 and J=v+w/2. The designer ODE gives

    w_s=-(1+n/2)w-nv,
    J_s=-(3/2+n/4)w-nv/2<0.                             (1)

K2299's derivative bound implies w→0, while v→0. Thus J decreases strictly from1+w1/2 to0. Since dot x=-Hx,

    H_E=sqrt(Fref/F) H [alpha-AJ]/[alpha-Av].             (2)

There is a necessary and sufficient classification on the closed half-line:
A<alpha/(1+w1/2) gives H_E>0 everywhere; equality gives H_E(1)=0 only; larger A<alpha gives exactly one finite zero. F and f_RR stay strictly positive there. This is a regular conformal map but a singular chart for variables dividing by H_E. It is not by itself an instability.

For exact dust N=L=0, let p=(5+sqrt73)/4, v=x^-p. The crossing is x*=[A(1+p/2)/alpha]^(1/p). Choose A=2alpha/5. Since3<p<4, this amplitude is above the turnaround threshold but below the positive algebraic trace-mass threshold alpha/(1+p/3). Hence m_alg²=(F/f_RR-R)/3 is positive everywhere despite a unique H_E zero. F*=alpha p/(p+2)>0. [K2291](k2291-rolling-scalar-applicability-2026-10-30.md)'s vacuum H_E-dividing flat-gauge mass cannot be transplanted to this branch.

## A healthy, explicitly supplied matter completion

Use C=H_*=1 for the displayed matter-profile formulas. Choose positive-density pressureless Jordan dust as a smooth single-velocity continuum of positive-mass particles before caustics, represented by -sum m integral ds_J, and radiation P=cX_J²,c>0, X_J=-g_J^{mu nu}partial_mu chi partial_nu chi/2. Its background X_J=sqrt(alpha N/c)x² gives rho_r=3alpha Nx⁴,p_r=alpha Nx⁴ in K2299 scaled units. For general normalization the radiation density is3 C H_*² alpha N x⁴ and X_J=sqrt(C H_*² alpha N/c)x².

With g_E=(F/Fref)g_J,Mpl²=C Fref,phi=sqrt(3/2)Mpl log(F/Fref), the scalar is canonical with

    V_phys=Mpl² Fref H_*²(RF-f)/(2F²), B(phi)=sqrt(Fref/F).

Here R and f are the dimensionless K2299 quantities; equivalently R_phys=H_*²R and f_phys=H_*²f. Dust has mass mB(phi); radiation remains cX_E² because the measure contributes (F/Fref)^-2 while X_J² contributes (F/Fref)^2. B contains no scalar derivatives. In a regular covariant formulation the scalar principal speed is1 and, when N>0, radiation has kinetic coefficient6cX_E, gradient coefficient2cX_E and speed²1/3. For N=0 omit the radiation degree of freedom: cX² at X=0 has degenerate quadratic kinetics, not a healthy extra propagating mode. Dust has positive inertial density and zero pressure sound speed before caustics. These statements do not establish full constrained mass eigenvalues, Jeans growth or finite-time stability.

Einstein-frame Raychaudhuri gives

    dH_E/dt_E=-(phi_dot²+rho_d,E+4rho_r,E/3)/(2Mpl²)<0.

All terms are finite at the zero, so it is a regular expansion-to-contraction turnaround for this completion. A negative potential balances the positive matter/kinetic terms in the zero Friedmann constraint. No ghost or physical singularity follows from the gauge-chart failure.

## Same background does not freeze matter perturbations

For N>0 the radiation profile is monotone and defines smooth Xb(chi) on each finite interval. Change ONLY the radiation action to

    P_epsilon(X,chi)=cX²+epsilon[X-Xb(chi)]².             (3)

On X=Xb, the added value and first derivatives vanish identically along the entire background. Its Euler contribution also vanishes there (the first derivative is the zero function along the solution). The gravitational action, rho,p and full background therefore survive unchanged. But

    K=(6c+4epsilon)Xb, G=2cXb,
    sound_speed²=c/(3c+2epsilon).

At epsilon=-2c the kinetic coefficient is negative and sound_speed²=-1; at epsilon=0 healthy radiation returns. This is an explicit changed-matter-action countercontrol, not an objection to the fully frozen healthy completion. Positivity of background F,f_RR and algebraic mass alone does not specify the missing matter Hessian.

## Verification and next condition

Exact symbolic checks cover ODE monotonicity, conformal sign, dust crossing/sign intervals, kinetic coefficients and identical background first variations. Continuum classification uses the inherited integral proof plus(1), not samples. Faults change actual conformal/flow/Hessian formulas. Internal specialist review is not proof-assistant, novelty or external-expert certification. Standard machinery is contextualized by [De Felice and Tsujikawa](https://arxiv.org/abs/1002.4928).

Next derive coupled dust/radiation/scalar transfer for this frozen healthy completion in variables regular at H_E=0, with selected perturbation data. The action now makes that question concrete; a single-scalar vacuum mass or a background-only fit cannot answer it.
