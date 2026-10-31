---
title: "K2339 Induced metric normal dispersion and localized frozen solutions"
status: active_research
doc_type: exploration
created: "2026-10-30"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematics; no native GU, survey or hardware acceptance
scripts:
  - tests/channel-swings/k2339_induced_normal_localization_probe.py
---

# K2339 Induced metric normal dispersion and localized frozen solutions

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
result: K2339
carrier: ten induced metric coefficients allowed to depend on all fourteen coordinates with full distortion companions LAYER=toy CHIRALITY=N/A
pairing: native indefinite Clifford/Hodge pairing and transverse induced Gram ON=declared_carrier
real_structure: real K77 coefficients, complex-bilinear transpose and conjugate-symmetric Fourier fields
grading: metric derivative P with odd grade1 and even grade2 reducing companions
action_owner: repository-construction -- unchanged K2316 frozen flat coefficient Hessian, with explicitly enlarged coefficient-function class
target: direction-dependent characteristic and real full-normal Fourier packets MAP-TYPE=evaluation
```

## Outcome and functional-class boundary

[K2316](k2316-induced-metric-coupled-pencil-2026-10-30.md) owns the induced metric derivative P and its temporal199/931 characteristic. Here its normal-direction characteristic changes nontrivially, but the simple root continues to a thirteen-momentum neighborhood. This yields growing real Schwartz packets in ALL thirteen non-time coordinates of the frozen model, if its ten coefficient functions are allowed to depend on normal coordinates.

This enlargement is explicit: h=sum u_a(x,y)P_a. A strict base variation u_a(x) does NOT gain normal dependence from Fourier analysis. On a flat noncompact normal R10 fibre a nonzero base-only coefficient is not L2 in the normal variables. An arbitrary localization factor changes the equations; the coupled solution below constructs allowed normal variation in the enlarged coefficient model. Neither functional class is silently identified with the complete source tangent.

Retain g=diag(1,-1,-1,-1), GV(A,B)=tr(g^-1 E_A g^-1 E_B)-tr(g^-1 E_A)tr(g^-1 E_B)/2, G=diag(g,GV), and P_a=diag(E_a,DGV[E_a]) from K2316, in the same fixed coordinates. No normal-dependent recomputation of G or P is implied. SC-ACT-01/02 and SC-GEO-55 ASSERTS; META53 UNCERTAIN. Ledger0.263 and native verdicts remain unchanged. Full moving metric/field/receiver jets, source stationarity and physical domains remain unconstructed.

## Coordinate-invariant transverse reduction with a fixed induced image

For complex nonnull q set

    s=q^T G^-1 q, Pi=I-G^-1 q q^T/s,
    M_a=Pi G^-1 P_a Pi,
    C_ab=tr(M_a M_b), t_a=tr M_a, tau=t^T C^-1 t.    (1)

Pi is G-self-adjoint and projects along q-sharp. Every M_a annihilates q-sharp, so full14 traces are precisely transverse13 traces. Formula(1) recomputes the induced image at EACH q; it does not assume that arbitrary horizontal/normal Lorentz transformations preserve P. K2313's unrestricted frozen coefficient formula can be applied to these particular transverse images. Locally choose an analytic orthonormal transverse frame and z=sqrt(s); then K2316 companion elimination gives

    H_ind=alpha(C+b t t^T),
    alpha=-kappa s²/(kappa²-4s),
    b=(11kappa²-35s)/(kappa²-121s),
    F(q)=kappa²(1+11tau)-s(121+35tau)=0.             (2)

Only the nonnull nonresonant neighborhood with C invertible is asserted. No finite rank alone supplies a global Green operator. Complementary distortion directions remain decoupled by the same nondegenerate reducing-block argument; metric components along q do not enter frozen curvature.

## Exact normal direction, not an ambient cone shortcut

In original fibre coordinate order (00,01,02,03,11,12,13,22,23,33), e4 is the fibre00 covector. Direct rational matrix evaluation at q=e0+v e4 yields

    s=1+v²/2,
    tau=4(46v^6+107v^4+356v²+643)
                  /(37v^6+62v^4+176v²+364)
       =643/91+(4104/8281)v²+O(v^4).                (3)

At v=i/2: s=7/8, tau=1448/209,

    det C=-5124528732635136/5764801,
    t=(-38/7,0,0,0,4,0,0,4,0,4),
    C^-1t=(-112,0,0,0,70,0,0,70,0,70)/209,
    (1+11tau)/(121+35tau)=1793/8441.                (4)

This q is an exact direction control; to put it on shell choose kappa²=s/(1793/8441), or rescale q for a fixed nonzero kappa. It is not the temporal ratio199/931. Reusing a constant tau under arbitrary ambient boosts would give the wrong branch.

## Universal continuation and constructed packets

Fix real kappa!=0. At q0=(lambda0,0), lambda0=|kappa|sqrt(199/931), C is invertible, both companion denominators and s are nonzero, and

    partial_lambda F(q0)=-2lambda0(121+35*643/91)!=0.

Tau is homogeneous degree zero in q. Rational analyticity of(1) and the analytic implicit-function theorem therefore give a unique local branch lambda(p) with q=(lambda(p),i p), p in R13 near0. Shrink the neighborhood so all prior denominators stay nonzero, the induced metric pencil kernel remains one-dimensional, and Re lambda>lambda0/2. Real coefficients and uniqueness imply lambda(-p)=conjugate(lambda(p)). This is a local existence statement, not a numerical radius of validity.

Choose u(q)=C(q)^-1t(q), reconstruct metric and odd/even companions through the analytic versions of K2316's formulas, and choose a real-analytic transverse frame near real q0 and holomorphically extend it. All amplitudes are analytic and satisfy every pulled-back metric and companion row. Curvature is nonzero at0; continuity keeps its Euclidean coordinate norm bounded below on smaller compact support. Choose nonzero smooth compactly supported Fourier amplitude a(p) with a(-p)=conjugate a(p), and integrate

    h(t,X)=integral a(p) sum_a u_a(q(p))P_a
                          exp(lambda(p)t+i p·X) dp. (5)

The companions use the same integral. Compact support permits differentiation under the integral, so these are exact solutions of the frozen constant-coefficient system. For each finite t they are Schwartz in all13 coordinates; conjugate symmetry makes them real. Plancherel and the curvature lower bound give an exponentially growing POSITIVE COORDINATE L2 curvature norm for t>=0, at least a constant times exp(lambda0 t/2). That norm is a mathematical diagnostic, not the indefinite action energy or a physical instability verdict.

For kappa=1 and momentum p only along fibre00, expanding(2)-(3) gives the nontrivial dispersion check

    lambda(p)²=199/931+(177061/370538)p²+O(p^4).     (6)

The constant-tau shortcut would produce coefficient1/2. The old horizontal-only root17/113 and K2310's different enlarged-image5/29 root remain separate. Analytic continuation of the induced image cannot be inferred from matching dimensions.

## Acceptance and remaining construction

The probe reconstructs the fixed P from the owned geometric formulas without running legacy import side effects, verifies projection/trace data and exact changed-direction values, tests the rational identity at multiple directions, the simple-root and dispersion coefficients, and the full reduced companion/metric equations at the rescaled normal control. Faults reuse the temporal root at the normal direction, omit the even companion, omit projector normalization or the fibre derivative, or freeze tau in normal dispersion before applying the checks. Finite algebra supports the rational formulas; the all13 local continuation and Fourier packet statements use the written analytic proof. No Lean or interval certificate is claimed.

This resolves localization only in the explicitly enlarged frozen coefficient-function class. A genuine source conclusion still needs a background stationary under the actual field variations, moving coefficient and receiver terms, source/observation map and a common analytic domain. Repeating a triangular coordinate change or simply multiplying a base solution by a normal bump cannot supply that lift.
