---
title: "K2342 Contact lift and second-jet cost of the induced metric mode"
status: active_research
doc_type: exploration
created: "2026-10-30"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematics; no native GU, empirical or whole-instrument acceptance
scripts:
  - tests/channel-swings/k2342_holonomic_metric_lift_probe.py
---

# K2342 Contact lift and second-jet cost of the induced metric mode

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
result: K2342
carrier: Lorentz metric bundle with ten symmetric fibre coordinates and first jets of sections LAYER=toy CHIRALITY=N/A
pairing: DeWitt form and literal section pullback ON=declared_carrier
real_structure: real symmetric tensors and real section jets
grading: base4 plus symmetric-metric fibre10
action_owner: repository-construction -- explicit local block metric continuation and K2316 frozen induced coefficient mode
target: holonomic lift, moving metric terms and curvature boundary MAP-TYPE=evaluation
```

## Result and prior evidence

Normal dependence by itself is not a holonomicity obstruction. The coefficient fields of [K2339](k2339-induced-normal-localization-2026-10-30.md) admit a local contact prolongation and a smooth independent metric-family realization. However neither construction identifies the frozen coefficient h=P0u with the complete metric change under a vertical diffeomorphism. Its missing mixed/vertical Jacobian terms are explicit. On the actual K2316 temporal kernel, the moving section also has a nonzero observed second derivative, and the natural local block continuation is already curved.

The block-metric Christoffels and literal graph pullback are prior evidence in [the June23 coordinate note](../geometry-curvature-emergence/ii-s-coordinate-formula-2026-06-23.md); they are consumed here, not claimed new. The contribution is the exact lift and second-jet comparison for K2339/K2316, with the strongest integrability counterargument rejected. [H24](../wave6/H24-RY-normalization-2026-07-11.md) is related curvature context with its own dimensions and conventions, not automatically the four-dimensional calculation below.

SC-ACT-01/02 and SC-GEO-55 ASSERTS, SC-META-53 UNCERTAIN, and ledger0.263 remain unchanged. These geometric constructions do not prove source action stationarity, a native instability or a physical energy/domain. We explicitly choose a local coordinate horizontal splitting; no unique source-selected metric or connection is inferred from its existence.

## Exact contact prolongation: a constructive positive result

Use base x^mu, symmetric Lorentz metric coordinates y^A and first jets p_mu^A. Contact forms are theta^A=dy^A-p_mu^A dx^mu. For ANY smooth symmetric coefficient field u^A(x,y), the vertical field V=u^A partial_yA prolongs to

    pr1 V=u^A partial_yA+(partial_mu u^A+p_mu^B partial_B u^A) partial_pmuA.

Cartan's identity gives, coefficientwise,

    L_(pr1 V) theta^A=(partial_B u^A) theta^B.        (1)

Thus its local flow preserves the contact ideal and sends holonomic sections to holonomic sections. Explicitly s_epsilon=F_epsilon composed with s, where F is the vertical local flow. Normal-dependent u is allowed; after composition with a section it becomes a base field. The full Y-dependent solution is not thereby identified with a source Euler variation or a normal-L2 field on the section.

Independently, for bounded smooth h=P0u on a local chart, G_epsilon=G0+epsilon h is a nondegenerate metric for sufficiently small epsilon on compact sets. This realizes the algebraic tangent as a metric family. It need not belong to the nonlinear natural metric-on-metrics construction, and does not preserve its functional dependence automatically. Therefore neither a blanket integrability exclusion nor automatic native admission follows.

## Exact moving-metric distinction

Fix the explicit block metric

    G(y)=diag(y,GV(y)),
    GV(A,B)=tr(y^-1 A y^-1 B)-1/2 tr(y^-1 A)tr(y^-1 B).

For vertical V, its actual tensor Lie derivative is

    L_V G=P_y(u)+G DV+(DV)^T G,                     (2)

where P_y(u)=partial_y G[u] includes the fibre derivative. In coordinates

    (L_VG)_mu,nu=u_mu,nu,
    (L_VG)_mu,A=GV_AB partial_mu u^B,
    (L_VG)_A,B=DGV[u]_AB+GV_CB partial_Au^C+GV_AC partial_Bu^C. (3)

At y=g0, the value-only P0u has zero mixed block. Since GV is nondegenerate, equality with(2) forces partial_mu u=0. Hence the time-growing K2316/K2339 coefficient does NOT realize a pure vertical-diffeomorphism metric variation by P0u alone. This is an exact obstruction to that particular identification; it is not an obstruction to(1) or to independent metric variations. A vertical diffeomorphism also moves the receiver/section, so its upstairs tensor cannot be silently inserted into the frozen action with a fixed receiver.

## Executed second-jet consumer on the actual mode

For literal section s_epsilon(x)=(x,g0+epsilon H(x)), the prior graph formula gives

    gamma_mu,nu(epsilon)=(g0+epsilon H)_mu,nu
         +epsilon² GV_AB(g0+epsilon H) partial_mu H^A partial_nu H^B.

Consequently gamma'(0)=H, but

    gamma''_mu,nu(0)=2 GV_AB(g0) partial_mu H^A partial_nu H^B. (4)

This is an exact local family, not a proposed ambient-field equation. Let g0=diag(1,-1,-1,-1), and use the actual temporal induced kernel

    H=diag(-59,29,29,29) exp(lambda t)/91,
    lambda²=199 kappa²/931.

Then direct trace contraction yields GV(Hamp,Hamp)=-4654/8281 and

    gamma''_00(0)=-9308 lambda² exp(2lambda t)/8281, (5)

with the other components zero. The mixed block missing from P0u is also nonzero because partial_0u=lambda u. These concrete corrections survive even though the first observed derivative is exactly H. They invalidate a first-derivative-only transfer to an arbitrary second variation.

For an action S composed with a lift Phi, the chain rule is

    D²(S composed Phi)[u,u]=D²S[D Phi u,D Phi u]+DS[D²Phi(u,u)]. (6)

At a background stationary on the entire second-jet direction, the second term vanishes. If stationarity is missing or only restricted, it cannot be deleted. Thus(5) is NOT by itself a proof that the stationary Hessian changes, and a claimed change requires its actual Euler covector. This gives the exact conditional repair and the remaining consumer input.

## Curvature of the declared continuation, not a flat-background inference

Choose R^i_jkl=partial_k Gamma^i_lj-partial_l Gamma^i_kj+Gamma^i_km Gamma^m_lj-Gamma^i_lm Gamma^m_kj. For the declared block metric, Gamma^A_ij=-GV^{AB}E_Bij/2 and Gamma^i_jA=y^{ik}E_Akj/2. The inverse DeWitt identity in dimension4 is

    sum_AB GV^{AB} E_Aij E_Bkl
      =1/2(g_ik g_jl+g_il g_jk)-1/2 g_ij g_kl.

It gives every horizontal curvature component

    R_ijkl=1/4(g_ik g_jl-g_il g_jk),
    R_0101=-1/4, R_1212=1/4.                       (7)

The probe checks all256 components against direct Christoffel contraction using the actual symmetric-coordinate basis. A coordinate change can remove Christoffel values at a point, but not(7). This continuation cannot have the flat full Levi-Civita background silently assumed by a frozen-flat calculation. It does not refute K2339, which declares its frozen scope. It does not prove that the actual source field equations fail: other connection/field and receiver contributions still have to be constructed.

Earlier dimension3 faithful models and opposite Riemann conventions have different coefficients/signs; no old curvature result is overwritten or declared erroneous by matching labels alone. The same source-geometer versus conventional-physics object distinction applies here.

## Verification and next construction

The probe checks contact-ideal preservation with genuinely normal-dependent polynomial fields, full moving mixed/vertical terms, the actual kernel trace and graph second jet, the action-chain-rule control and all4D horizontal curvature components. Faults omit total derivatives, mixed terms, fibre derivatives, graph quadratic terms or change the DeWitt contraction before the checks. Universal existence and chain-rule statements are established by the formulas above, not inferred from finite controls.

Next instantiate the complete source field/receiver variation and stationary Euler covector on ONE curved background, then apply(6) to its real action Hessian and analytic domain. The contact lift is now available and should not be requested again as if normal dependence forbade it. The actual curved operator, second-jet action contraction and source stationarity remain separate constructions.
