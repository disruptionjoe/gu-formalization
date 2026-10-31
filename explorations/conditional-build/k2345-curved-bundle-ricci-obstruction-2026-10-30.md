---
title: "K2345 Full metric-bundle Ricci and stationary-background boundary"
status: active_research
doc_type: exploration
created: "2026-10-30"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematics; no native GU or empirical certification
scripts:
  - tests/channel-swings/k2345_curved_bundle_ricci_obstruction_probe.py
---

# K2345 Full metric-bundle Ricci and stationary-background boundary

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
result: K2345
carrier: declared local metric G=diag(y,GV(y)) on base4 and symmetric-metric fibre10 LAYER=toy CHIRALITY=N/A
pairing: pseudo-Riemannian DeWitt bilinear form ON=declared_carrier
real_structure: real coefficients or complex adjoint as explicitly stated
grading: horizontal4, vertical trace1 and traceless9
action_owner: repository-construction -- K2342 coordinate-horizontal block continuation; selected action contraction only conditionally
target: full Ricci, Einstein anisotropy and receiver distinction MAP-TYPE=evaluation
```

## Result and inference boundary

[K2342](k2342-holonomic-metric-lift-2026-10-30.md) computes horizontal curvature, but horizontal curvature alone does not determine the full Ricci tensor or an action equation. Here the complete14-dimensional coordinate Christoffels and their derivatives are contracted on the same declared metric. With S=y^-1 A and T=y^-1 B,

    Ric_HH=y/4, Ric_HV=0,
    Ric_VV(A,B)=−5 tr(ST)/4+tr(S)tr(T)/4,
    Scal_G=−10.                                             (1)

The raised Ricci eigenvalues are1/4 on horizontal4 plus vertical trace1, and−5/4 on vertical traceless9. No constant cosmological shift makes this metric Einstein. It is not a stationary vacuum of the Einstein-Hilbert-plus-cosmological-term action on this full metric carrier. This exact failure concerns this coordinate-horizontal continuation only, not all natural metrics on the metric bundle, all source connections, or GU.

Source SC-ACT-01 and SC-GEO-55 ASSERTS their action and gauge-rotated Levi-Civita displacement; neither asserts that this particular G at T=0 is its stationary solution. SC-META-53 remains UNCERTAIN. Ledger0.263 and native source verdicts stay unchanged. This continuation has the actual signature computed below; it must not inherit K77 Clifford/action conventions by name alone.

## Full calculation and analytic extension

Fix symmetric coordinate matrices E_A with off-diagonal entries1 in both positions and

    GV(A,B)=tr(y^-1 A y^-1 B)−tr(y^-1 A)tr(y^-1 B)/2.

All matrices and derivatives in the probe are literal derivatives of this metric, with no fitted connection. At y=g0=diag(1,−1,−1,−1), inverse derivatives are

    d_A(y^-1)=−g0 E_A g0,
    d_A d_B(y^-1)=g0 E_A g0 E_B g0+g0 E_B g0 E_A g0.

Differentiating the displayed GV supplies every first and second metric derivative. The code builds Γ^a_bc=G^ad(∂bGdc+∂cGdb−∂dGbc)/2, differentiates both inverse and metric derivatives, and forms Ric_bd=R^a_bad in the convention of K2342. It checks all196 entries against(1), the vanishing mixed block, raised trace/traceless actions and scalar. Omitting vertical derivative contributions or mixed Christoffels is detected.

For an independent structural derivation, the fibre connection on constant symmetric A,B is ∇^V_A B=−(Ay^-1B+By^-1A)/2, with fibre Ricci −tr(ST)+tr(S)tr(T)/4. The horizontal metric contributes another−tr(ST)/4. For horizontal Ricci, the fibre Laplacian and matrix-gradient-square terms cancel; grad_V log|det y|=−y leaves y/4. The general linear transformations (x,y)→(Lx,L^-T y L^-1) preserve both blocks and are transitive on each fixed-signature fibre. Base translations preserve G. Thus the exact point calculation and tensor covariance prove(1) throughout this chart/signature component, not merely at one sampled metric. The curvature convention also reproduces K2342's R0101=−1/4 and R1212=1/4.

The vertical form has inertia(6,4); the horizontal g0 has(1,3), so total inertia is(7,7). This is an actual calculation for the explicitly chosen g0 sign convention. Reversing the base metric without changing the vertical form changes that total signature; neither is a universal source-signature verdict.

## Stationarity consumer, with explicit selected-contraction premise

Einstein_14=Ric−Scal G/2 has raised eigenvalues21/4 and15/4. Adding Lambda G cannot annul both; their difference is3/2. A nonzero local Euler covector yields a compactly supported variation of matching sign, so this is a stationarity obstruction, not just nonzero curvature.

The repository's [selected curvature contraction](selected-action-curvature-graph-six-versus-four-2026-08-06.md) supplies S_sel(R)=−2 Einstein_14 and <Phi1,S_sel(R)>=12 Scal14 on its K77 algebraic Riemann carrier. In a local orthonormal frame of the actual(7,7) metric above, IF this same selected Shiab/pairing and tautological Phi1 are the adopted first-action conventions, at T=0 the independent translation variation is exactly S_sel(F_LC); terms quadratic/cubic in T contribute no first variation. Its radial pairing is−120. The selected T=0 first-action background therefore fails stationarity. This is a conditional reuse of the named selected contraction, not a new source-selected Shiab theorem or an assertion that every GU action equals Einstein-Hilbert. Additional action terms, different contraction conventions, nonzero distortion or a different continuation require their own Euler test. We do not assert that a constant radial distortion cannot repair the complete graded equation without computing that equation.

## Executed receiver consequence

For K2316's H=diag(−59,29,29,29)e^(lambda t)/91, the literal fixed-ambient moving-graph receiver has gamma'(0)=H. On its flat observed base,

    delta R_X=∂mu∂nu H^munu−Box tr_g0 H
             =(87/91)lambda² e^(lambda t),                  (2)

which is nonzero. It cannot be a base-coordinate gauge perturbation of the flat observed metric: the scalar curvature derivative of a diffeomorphism of a flat metric is zero. This does not prove physical instability or gauge-invariant spectrum of the full source theory.

In contrast, simultaneous ambient transport G_e=F_e^*G and s_e=F_e^-1 composed s satisfies s_e^*G_e=s^*G exactly. Both first and second receiver jets cancel by composition. The probe verifies this with a finite nonlinear vertical flow and full graph derivatives in a two-coordinate control. This control illustrates the universal pullback identity; it does not replace the14-dimensional Ricci calculation. The fixed-ambient graph motion in(2), the value-only coefficient P0u and simultaneous transported receiver are different variations.

## What this settles and what remains

The actual continuation is curved and non-Einstein, and the conditional selected-contraction T=0 first-action translation Euler is nonzero. Therefore a frozen-flat stationary Hessian cannot be imported on this background by assuming its lower terms vanish. This is a concrete negative test of the simplest background; it removes that shortcut. A repaired nonzero-distortion stationary field/receiver packet, complete action and common analytic domain remain to be constructed. Neither normal holonomicity nor physical gauge classification is settled by the Ricci result. Universal claims use covariance and the written tensor derivation; exact finite controls verify the implementation. No canon, ledger or source verdict moves.
