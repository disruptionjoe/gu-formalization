---
title: "K2357 Curved radial-distortion stationarity and Einstein obstruction"
status: active_research
doc_type: exploration
created: "2026-10-31"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional selected-action mathematics; no native GU or empirical certification
scripts:
  - tests/channel-swings/k2357_curved_native_stationarity_probe.py
---

# K2357 Curved radial-distortion stationarity and Einstein obstruction

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
result: K2357
carrier: real Cl(7,7) one-form distortion on a14-dimensional Levi-Civita chart LAYER=toy CHIRALITY=N/A
pairing: scalar Clifford trace and pseudo-Riemannian exterior Hodge ON=declared_carrier
real_structure: real Cl(7,7) fields and real amplitudes
grading: internal Clifford parity separate from form degree
action_owner: repository-construction -- selected comm/symi/symi first I1 action, fixed metric and epsilon
target: all-translation radial consistency with variable amplitude MAP-TYPE=evaluation
```

## Result and exact scope

For the declared selected I1 convention, a smooth radial distortion T=a(p)Phi1 is stationary under ALL compactly supported translation variations on a connected Levi-Civita chart if and only if a is constant, the geometry is Einstein Ric=lambda g, and

    312a²+kappa a+12lambda=0.                              (1)

This closes the radial-repair gap left by [K2345](k2345-curved-bundle-ricci-obstruction-2026-10-30.md): that metric's two distinct Einstein eigenvalues cannot be canceled by a common scalar amplitude, including a variable one. It also classifies the conditional radial roots on an Einstein geometry, keeping the merged-root case. It does not exclude nonradial or mixed-grade distortions and does not assert metric/epsilon stationarity, a physical solution or a global boundary domain.

SC-ACT-01 ASSERTS the first action and SC-GEO-55 ASSERTS displacement from gauge-rotated Levi-Civita. The selected Clifford metric, product tuple, radial ansatz and coefficients remain repository constructions. Source/ledger0.263 GR6b/SM8, physical quotient and canon remain unchanged. The flat root a=-kappa/312 is old evidence in [the curvature-graph result](selected-action-curvature-graph-six-versus-four-2026-08-06.md); this note's new object is the curved, variable-amplitude all-receiver condition, not that root or a new source action. An older odd B=bPhi1 model is not a Levi-Civita spin connection and cannot substitute for this proof.

## Convention and full first variation

Let Phi1 be the tautological Clifford-valued soldering one-form and Phi2=Phi1 wedge Phi1/2. Work in the associated real Clifford bundle with the total connection induced by Levi-Civita, so Phi1, Phi2, Hodge and scalar trace are parallel. A local normal orthonormal frame can compute coefficients at a point; it does not make curvature or derivatives of a vanish. Spin gauge rotation changes both reference and field, preserving the equation. Freeze geometry and epsilon while varying translation T. Kappa is a real constant.

Use the selected action density

    L(T)=P(T,S(F_B)) + 1/2 P(T,S(D_B T))
           + 1/3 P(T,S(T wedge T)) + kappa/2 P(T,*T),

where P is the top-form scalar Clifford trace pairing and S is the same comm/symi/symi Shiab backend as K2354. Compactly supported tests justify covariant integration by parts. The full derivative term's Euler coefficient is the skew part of its coefficient pairing, not coefficient transpose without integration by parts.

At T=aPhi1, curvature, mass and cubic Euler covectors have odd internal parity. The derivative Euler covector has even parity and is J(da), with

    J(v)[Z]=1/2{P(Z,S(v wedge Phi1))-P(Phi1,S(v wedge Z))}.

The second minus sign comes from integration by parts; all coefficient derivatives vanish covariantly, not by freezing a nonparallel coordinate frame. Different parity covectors cannot cancel under the nondegenerate parity-respecting trace/Hodge pairing.

## Variable amplitudes cannot supply the missing repair

J is a real Spin(7,7)-equivariant linear map from the standard covector module into the even translation dual. Exact backend evaluation with v=dx0 and Z=dx1 gamma01 gives pairings2 and24, hence J(v)[Z]=-11. Therefore J is nonzero. The real standard representation of the connected Spin(7,7) group is irreducible: an invariant subspace is invariant under the generators of so(7,7), which connect every coordinate direction. Its invariant kernel is consequently zero. This proof includes null covectors; no positive norm or transitivity between timelike and null orbits is assumed. Thus the full even Euler equation J(da)=0 forces da=0 pointwise. On a connected chart a is constant.

The probe independently computes all14 input columns and a diagonal14-by14 receiver minor. These finite coefficients confirm injectivity directly and guard the representation argument's convention; the universal proof is algebraic. Suppressing the adjoint half changes the operator and is not an allowed reduction.

## All odd receivers and curved roots

For a genuine algebraic Riemann curvature, the prior selected-curvature theorem proves that S(F_B), Riesz-identified through the fixed trace/Hodge pairing, is -2 Einstein14. Reuse this theorem only for the Levi-Civita/Riemann convention; an arbitrary connection curvature is not granted Riemann pair symmetry.

The mass covector at aPhi1 is kappa a Phi1. The cubic covector at Phi1 is invariant under simultaneous spin/frame action. Each Shiab term adds at most three Clifford generators; differentiating the cubic expression therefore yields internal grade at most5. An invariant map from the standard vector to exterior powers in14 dimensions has only the degree1 identity and the degree13 Hodge-dual possibility. The grade bound excludes13, so the cubic covector is a scalar multiple of Phi1 against every receiver, including receivers outside low grades. The actual native evaluation at Z=dx0 gamma0 gives cubic contributions312 and624; division by3 gives312. Its mass coefficient is1. Thus the FULL odd Euler equation is

    -2 Einstein14 + (kappa a+312a²) I =0.                 (2)

This is a support/equivariance proof of all-receiver closure, not a finite scan mislabeled complete. For Ric=lambda g, scalar curvature is14lambda and Einstein=-6lambda I; equation(2) gives(1). Conversely(2) implies Ric is scalar, and the contracted Bianchi identity in dimension14 makes lambda constant; also a was already constant. The roots are

    a=[-kappa +/- sqrt(kappa²-14976lambda)]/624.

There are two, one or no real roots according as the discriminant is positive, zero or negative. At lambda0, a0 and -kappa/312 reproduce prior flat results. Nonzero Weyl curvature is permitted on an Einstein chart because the reused Shiab Riemann identity contracts it out; this does not dispose of independent metric equations. With F=qPhi2, the backend gives S(F)=156q Phi1, consistent with lambda=13q in this normalization and the quadratic discriminant kappa²-194688q. These are conditional fixed-geometry translation-critical fields, not selected physical vacua.

## Application and follow-through

K2345's constructed metric bundle has raised Ricci eigenvalues1/4 (multiplicity5) and -5/4 (multiplicity9), scalar curvature-10. Hence Einstein eigenvalues21/4 and15/4. Subtracting the two required scalar equations in(2) gives -3=0. No real or complex scalar a can cancel this anisotropy; allowing a(p) does not help because J(da)=0 independently forces constancy. K2345 only excluded T0 on this geometry and deliberately left nonzero radial repair open; the present full equation closes that branch. K2354's separate four-component flat ansatz exclusion is retained, not reused as this theorem.

The surviving next construction must be nonradial or change geometry. Natural horizontal4/vertical trace1/vertical traceless9 projector components on K2345 supply a concrete larger candidate, but those projectors need not be parallel. Their actual covariant derivatives generate even Euler terms; merely assigning three independent constants and ignoring derivatives repeats the wrong truncation. Build the derivative-complete mixed tangent and all transverse equations before seeking a stationary receiver background. Common boundary/domain and metric/epsilon variations remain independent requirements.

## Evidence and countercontrols

The exact probe reconstructs the derivative coefficient/minor, mass/cubic coefficients and constant-curvature normalization from the pinned backend, verifies root/threshold/anisotropy algebra, and alters the adjoint, curvature isotropy, discriminant and scope assumptions. Universal tensor statements rely on the derivation, all-receiver support and the cited Riemann theorem. No large full-field brute-force enumeration, physical positivity, spectrum, empirical test, proof-assistant or external-expert certification is claimed.
