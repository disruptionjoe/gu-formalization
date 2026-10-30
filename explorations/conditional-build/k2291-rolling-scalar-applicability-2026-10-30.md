---
title: "K2291 Constrained rolling scalar on the fixed history"
status: active_research
doc_type: exploration
created: "2026-10-30"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional supplied models only; no native GU, empirical or hardware acceptance
scripts:
  - tests/channel-swings/k2291_rolling_scalar_applicability_probe.py
---

# K2291 Constrained rolling scalar on the fixed history

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or borders a conventional particle-physics comparator. Any result about a standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126` Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-mass route binds only that named model. It is not evidence for or against Weinstein's source-native mechanism without an explicit typed bridge. Read `lab/methods/source-native-comparator-routing.md` and follow its source-native pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

```gu-typed-objects
result: K2291 Constrained rolling scalar on the fixed history
carrier: real scalar perturbations of the same positive-F vacuum metric history LAYER=toy CHIRALITY=N/A
pairing: declared real metric scalar pairing ON=declared_carrier
real_structure: real metric histories and perturbations
grading: no native Clifford or chirality transfer
action_owner: repository-construction -- supplied conditional model
target: regular constrained scalar mass MAP-TYPE=evaluation
```

## Result and scope

On the SAME full13-compatible [K2283](k2283-global-quadratic-cosmology-2026-10-30.md) history, the correctly constrained scalar perturbation has positive canonical kinetic and gradient terms. At the present endpoint its flat-gauge effective mass obeys

    -8.532 < mu_Q²/H_E² < -8.531,

although the trace coefficient alpha/3 is positive and V_phi_phi/H_E² is between4.604 and4.605. These are different masses. Thus positivity of either elementary coefficient does not establish the rolling perturbation's positive effective mass. A negative instantaneous mass is NOT by itself a growing-mode theorem, finite-time amplification bound or empirical exclusion. No GU, ledger, source or canon verdict changes.

## 1. Regular Einstein-frame problem on the full path

With the K2286 normalization, set F=f_R>0, Fref>0 constant, g_E=(F/Fref)g, M²=C Fref, phi=sqrt(3/2)M log(F/Fref). The scalar potential is

    V=M² Fref/4 [1-2alpha/F+D/F²], D=alpha²+2rho_v.

Here D is a constant in this note, unrelated to the diagonal pump operator in K2290. This is the standard metric-f(R) scalar-tensor transformation, not a replacement for source-native GU dynamics. It is valid on the already proved positive-F domain. In Einstein proper time,

    H_E=sqrt(Fref/F)(H+dot F/(2F)),
    dot phi_E=sqrt(3/2)M sqrt(Fref/F) dot F/F,
    3M²H_E²=dot phi_E²/2+V,
    dot H_E=-dot phi_E²/(2M²).

The Jordan vacuum constraint gives exactly

    (H+dot F/(2F))²=(dot F/(2F))²+(FR-f)/(6F).

For alpha>0,rho_v>0, FR-f=R²/2+rho_v>0. The initial factor H+dot F/(2F) is positive by K2286 alpha_M0≈-.82558, hence it stays positive and never crosses zero on the certified path. Smooth positive U,F on its compact redshift interval make all coefficients finite. Turning points dot phi=0 are allowed. No gauge dividing by dot phi is needed; use the spatially flat gauge variable Q=delta phi+(dot phi/H_E)psi, with psi the scalar spatial curvature perturbation in the convention giving this invariant combination.

## 2. Retain the lapse and shift constraints

For nonzero comoving wave number, integrate out lapse/shift in the single minimally coupled canonical scalar problem. The resulting quadratic action is

    S_Q=1/2 integral dt_E d³x a_E³
                  [dot Q²-a_E^-2(partial Q)²-mu_Q² Q²],
    mu_Q²=V_phi_phi-(1/(M² a_E³)) d/dt_E[a_E³ dot phi²/H_E].

Expanding with ddot phi=-3H_E dot phi-V_phi and dot H_E=-dot phi²/(2M²) yields

    mu_Q²=V_phi_phi+3dot phi²/M²
           +2dot phi V_phi/(M²H_E)-dot phi^4/(2M^4H_E²).

The kinetic and gradient signs are positive, so this is not a ghost or wrong-characteristic-sign result. Positive H_E makes the mass regular even when dot phi vanishes. The k->0 adiabatic solution is used as a consistency check below; global gauge zero modes need their own boundary convention.

## 3. Same coefficients, independent algebraic checks

Write b=dot F/(HF)=alpha_M, h=H/H_*=U^(2/3), and use dimensionless F,alpha,rho_v in H_* units. Set

    x=dot phi/(M H_E)=sqrt(6)b/(b+2),
    y=V_phi/(M H_E²)=(alpha-D/F)/[sqrt(6)h²(1+b/2)²],
    w=V_phi_phi/H_E²=(-alpha+2D/F)/[3h²(1+b/2)²].

Then mu_Q²/H_E²=w+2xy+3x²-x^4/2. The ratio is independent of overall action normalization and Fref, with no free BAO ruler. Freeze alpha=33.8,rho_v=1,U=2,p=.9303 at z=0 and retain the K2283 flow, s=3log(1+z):

    U_s=p, p_s=p-alpha/(36U^(1/3))+rho_v/(216U^(5/3)),
    F=12U^(1/3)(U-p)+alpha, b=-3F_s/F.

Outward Arb arithmetic gives the stated negative mass and positive w. The potential alone switches concavity at Fcrit=2D/alpha≈67.7183, lying strictly between the present F≈49.973 and the past endpoint F>123. This sign crossing follows continuity, but neither side's potential curvature alone decides the rolling dynamics.

A second route checks the mass using the exact long-wavelength adiabatic solution Q proportional to dot phi/H_E. Let j=b/(b+2), l=ds/d(log a_E)=-6/(b+2), and prime_s mean the displayed flow derivative. From dot H_E/H_E²=-3j², its equation implies

    mu_Q²/H_E²=-[l² j_ss+(l l_s-3j²l+3l)j_s]/j.

At the present point j!=0 this agrees independently with the direct potential/constraint formula. This identity is a consistency check, not a separate matter mode or empirical confirmation. The probe differentiates the actual flow and evaluates both expressions, instead of comparing copied decimal answers.

A different constant-curvature vacuum is a positive-mass countercontrol: F=D/alpha, dot phi=0 and mu_Q²=V_phi_phi=Fref alpha²/(3D)>0. There Q=delta phi remains regular even though a curvature variable dividing by dot phi is unavailable. Thus the present rolling result is not an action-wide negative-mass theorem.

## 4. Useful consequence and remaining gate

K2286's tensor sector can be healthy while a rolling scalar has a negative instantaneous effective mass. One cannot append 'scalar stable' to the distance/tensor witness using alpha/3 or F>0 alone. Conversely this result does not falsify the history: cosmological friction, wave number, duration and physical initial data determine amplification. The next calculation needs the actual constrained evolution/transfer on the common interval or a justified matter-background solution; a frozen-source Yukawa calculation cannot replace it. [K2289](k2289-quadratic-source-matching-2026-10-30.md) explicitly marks its different local approximation.

Standard scalar-tensor and perturbation machinery is reviewed by [De Felice and Tsujikawa](https://arxiv.org/abs/1002.4928). Here its hypotheses, regular gauge and exact same-history mass are checked. Symbolic differentiation and outward intervals are distinct from universal action/regularity arguments and inherited full-path evidence. No nonlinear stability, empirical, Lean, novelty or external-expert certification is asserted.
