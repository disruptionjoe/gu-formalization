---
title: "K2316 Induced metric coupled pencil"
status: active_research
doc_type: exploration
created: "2026-10-30"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematics only; no native physical acceptance
scripts:
  - tests/channel-swings/k2316_induced_metric_coupled_pencil_probe.py
---

# K2316 Induced metric coupled pencil

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
result: K2316
carrier: ten base symmetric variations with tied DeWitt fibre variation in the flat K77 coefficient model LAYER=ambient CHIRALITY=N/A
pairing: native indefinite Clifford/Hodge pairing and its induced transverse Gram ON=declared_carrier
real_structure: real rational adapted-frame coefficients, complexified for covectors
grading: transverse symmetric odd grade1 and even grade2 coupled block
action_owner: repository-construction -- pullback of frozen K128 I1B coefficient Hessian along the existing metric derivative
target: induced metric characteristic and resonance analysis MAP-TYPE=evaluation
```

## Actual existing map, distinct from its missing lift

[K2313](k2313-full-metric-variation-boundary-2026-10-30.md) contrasts the independent105 ambient metric carrier with the ten-horizontal-slot model. The existing [full normal owner bank](../../tests/channel-swings/selected_k77_full_normal_owner_bank_probe.py) already constructs the ten-direction derivative of the metric-on-metrics. Thus **the algebraic induced metric derivative is available**; it must not be conflated with the still-unowned complete field-bundle first-jet lift or moving normal dynamics.

Use fixed symmetric fibre coordinates E_A, g=diag(1,-1,-1,-1), and

    GV(A,B)=tr(g^-1 E_A g^-1 E_B)
             -1/2 tr(g^-1 E_A)tr(g^-1 E_B),
    P(h)=diag(h,DGV[h]),  D(g^-1)[h]=-g^-1 h g^-1.       (1)

GV has signature(6,4); GY=diag(g,GV) has(7,7). The factor1/2 is fixed. We pull back the **frozen flat T=0 I1B coefficient Hessian** of K2313 along P, with its all-grade distortion carrier and independent distortion coordinate held fixed. This is a new conditional pullback of an existing geometric map. It is not the full source fixed-varpi variation, which includes delta T=-delta B_LC, moving soldering/pairing and field/receiver jets. A frame change can move coefficient derivatives into those jets; it does not erase their obligations. The direct source action's required variational coordinate choice remains separate.

SC-ACT-01/02 and SC-GEO-55 ASSERTS; SC-META-53 UNCERTAIN. Ledger0.263 LT-GR1b/6b/10/11 and LT-SM8 remain unchanged. No source stationarity, physical propagator, quotient or GU verdict follows.

## Ten-dimensional exact reduction

Take q=z dx0, s=z², kappa!=0. Restrict P(h_a) to q-perp; right-raise its transverse index with G_perp^-1 to obtain M_a. Define

    C_ab=tr(M_a M_b), t_a=tr(M_a), tau=t^T C^-1 t.

In the ordered symmetric base slots (00,01,02,03,11,12,13,22,23,33), exact calculation gives

    rank C=10,
    t=(-5,0,0,0,4,0,0,4,0,4), tau=643/91,
    C^-1 t=(-59,0,0,0,29,0,0,29,0,29)/91.             (2)

This uses all ten directions including h00: its vertical variation survives the q-perp restriction. Gauging away h00 as in an unconstrained ambient variation would change the induced carrier. In fact C invertible proves P's transverse image has no kernel.

Reuse K2313's exactly checked native reducing block, with R(M)=M-tr(M)I and B(M)=tr(M)I-2M on transverse dimension13. Write M=sum u_a M_a, odd/even companion matrices o,e. The full companion and ten pulled-back metric rows are

    kappa o+z B(e)+s R(M)=0,
    kappa e+z B(o)=0,
    s tr(R(M_a)o)=0  for all a.                       (3)

All complementary distortion directions decouple by the nondegenerate reducing-block argument, not by a positivity assumption. Away from kappa²=4s and121s,

    o=-kappa s [M_tf/(kappa²-4s)
               -12 tr(M)I/(13(kappa²-121s))],
    e=-(z/kappa)B(o).

The metric pencil is

    H=alpha(C+b tt^T),
    alpha=-kappa s²/(kappa²-4s),
    b=(11kappa²-35s)/(kappa²-121s).                   (4)

The determinant lemma gives a simple nonzero nonresonant root

    s/kappa²=(1+11tau)/(121+35tau)=199/931.            (5)

At that root the kernel is exactly span(C^-1t). Thus h is proportional to diag(-59,29,29,29). R is invertible and M!=0, so the linearized ambient metric curvature is nonzero. This is neither the17/113 horizontal-only root nor the5/29 normal-extended root. It is not an inference from matching dimensions or signatures.

## Released follow-through: exceptional poles and forced response

The companion poles cannot be discarded by dividing through them. At kappa²=4s, the tracefree companion equation requires M_tf=0. But I is not in the induced image: if it were, C u=t and t^T u=13, contradicting tau=643/91. Hence M=0. Pure tracefree distortion may remain, subject to the ten metric constraints.

At kappa²=121s, the trace companion forces tr(M)=0. The remaining rows imply C u is proportional to t. Therefore u is proportional to C^-1t, and t^T u=0 with tau!=0 forces u=0. These two pole calculations exclude additional metric branches there; they do not remove all pure-distortion modes. s=0 and kappa=0 are excluded hypotheses, not resolved cases.

For a supplied induced metric source j and zero companion sources, away from the poles and root,

    u=alpha^-1 [C^-1 j
       - b C^-1t (t^T C^-1j)/(1+b tau)].             (6)

At the simple root, solvability requires (C^-1t)^T j=0. A generic source has a nonzero pole residue along C^-1t; compatible sources retain the homogeneous freedom. This is an algebraic response and compatibility rule, not a global causal Green operator or physical matter coupling. It gives an actual consuming source discriminator rather than another unconnected eigenvalue.

## Horizontal transport and inference limit

The metric construction (1) is equivariant under simultaneous horizontal Lorentz transformations and their symmetric-square action on fibre coordinates. Therefore the induced image is preserved by this subgroup. It transports the temporal mode to horizontal covectors with eta_H^-1(q,q)=199kappa²/931. For a real spatial Fourier vector p with |p|²<199kappa²/931, q=(lambda,i p,0) has lambda=sqrt(199kappa²/931-|p|²)>0. Complex Lorentz transport gives nonzero-curvature growing solutions of the same frozen model; conjugate pairs give real solutions.

A compact smooth Fourier amplitude inside this ball yields horizontal Schwartz wave packets with exponential curvature growth. The coefficients remain constant in normal coordinates, so this is **not** full Y14 localization or finite physical energy. Lorentz covariance here does not permit arbitrary horizontal/normal boosts: those need not preserve P. Nor does frozen coefficient growth decide the complete source moving system.

## Fixed-varpi coordinate follow-through on the same frozen model

A coordinate substitution alone does not supply a new characteristic test. If J(q) is a declared linearized connection map composed with P, set alpha=delta varpi=delta T+J(q)h. On the frozen quadratic action, in covector-valued Euler coordinates,

    (h,T)=S(q)(h,alpha), S(q)=[[I,0],[-J(q),I]],
    H_new(q)=S(-q)^T H_old(q) S(q), det S=1,
    E_new,h=E_old,h-J*E_old,T, E_new,alpha=E_old,T.   (7)

S inverse has +J. Thus the **full mixed-order Fourier pencil** has the same rank, kernel dimension and metric-curvature branches. This does not assert invariance of a naive highest-order principal symbol: differential J changes block orders. For Gram-identified equation vectors, J* is the formal adjoint with the actual pairings, not an ordinary transpose. A nonzero companion source transforms too: j_new=(j_h-J*j_T,j_T); the same metric-source input is retained only when j_T=0. Detector maps must be composed with S as well. Any analytic domain must be transported; a derivative substitution need not preserve an arbitrarily fixed Sobolev space.

Equation(7) is a conditional coordinate theorem and does not claim to have built the source's complete J or normal background. In a nonlinear action away from stationarity, second coordinate derivatives multiply the old Euler covector; those terms cannot be omitted. Here the frozen quadratic model is the explicit setting. The remaining scientific task is the actual curved metric-on-metrics background, moving coefficient/field-jet terms and domain, rather than repeating a triangular coordinate change as if it could by itself eliminate this frozen branch.

## Verification

The probe reconstructs DGV from the existing functions, independently differentiates the rational metric formula, verifies all ten Gram/trace values, and transports the entire induced bank by an explicit rational congruence to native K77 signature. Actual native curvature, odd/even companion and ten metric-dual rows check the root; an independent rank-one determinant/inverse argument checks the result. Mutations change the fibre derivative, trace coupling, root, raised index or companion term and must fail the clean predicates. Finite bank checks support exact coefficient statements; subgroup covariance and Fourier packet claims use the written argument above.

Next: compose this owned induced derivative with the actual fixed-varpi/Levi-Civita and moving field/receiver jets on one stated source background, or construct its source-compatible readout/domain. Do not ask again for the already available algebraic P map; do not promote this frozen branch to a native physical instability.
