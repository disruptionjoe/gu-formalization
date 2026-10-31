---
title: "K2366 Curvature forces scalar Codazzi fields on the actual metric"
status: active_research
doc_type: exploration
created: "2026-10-31"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematical or numerical result; no native GU or hardware certification
scripts:
  - tests/channel-swings/k2366_curvature_codazzi_rigidity_probe.py
---

# K2366 Curvature forces scalar Codazzi fields on the actual metric

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
result: K2366
carrier: real symmetric endomorphisms on the fourteen-dimensional metric bundle LAYER=toy CHIRALITY=N/A
pairing: nondegenerate metric and selected scalar Clifford trace ON=declared_carrier
real_structure: real metric-self-adjoint A with signature(7,7)
grading: Clifford grade, horizontal and vertical metric tensors are distinct
action_owner: repository-construction -- selected comm/symi/symi I1 with fixed geometry and epsilon
target: general symmetric Codazzi rigidity and translation stationarity MAP-TYPE=evaluation
```

## Result and scope

On the actual K2345 metric, every smooth metric-self-adjoint Codazzi endomorphism is a constant scalar on each connected component. This removes K2363's projector restriction: no diagonalizability, positivity or projector ansatz is assumed. Composed with K2357's unequal odd Euler rows, it excludes every grade-one translation field T_i=A_i^j gamma_j with symmetric A for this selected fixed-geometry action. It does not exclude antisymmetric A, mixed Clifford grades, changed geometry, full metric/epsilon solutions or GU itself.

SC-ACT-01 and SC-GEO-55 ASSERTS remain source facts. The exact metric, selected Shiab and real Cl(7,7) remain repository constructions; ledger0.263 does not change. The backward demand is a stationary receiver for matter/light response. The proof is an algebraic compatibility reduction before a nonlinear PDE search.

## 1. Codazzi curvature compatibility

Regard A as a tangent-valued one-form. Codazzi is d_nabla A=0, so d_nabla² A=R wedge A gives

    R(X,Y)AZ+R(Y,Z)AX+R(Z,X)AY=0.                 (1)

Contract the output of (1) with its first input; symmetry gives tr(R(Y,Z)A)=0, and the other two terms give [A,Ric#]=0. This identity uses only a nondegenerate metric and applies in indefinite signature; it does not use a Riemannian eigenbasis theorem. K2345 gives two distinct Ricci eigenvalues:1/4 on W=H4 plus vertical trace, and-5/4 on vertical traceless S9. Consequently A preserves W and S.

At y=diag(1,-1,-1,-1), put t=y/2, whose norm is-1. Write

    AX=B X+ell(X)t, At=b t+v, AU=C U (U traceless).

B is g-self-adjoint and self-adjointness gives ell(X)=-g(v,X). No restriction on the9x9 self-adjoint C has yet been imposed.

## 2. Actual curvature identities

For vertical symmetric U,V, let S=y^-1 U,T=y^-1 V. The metric is G=diag(y,GV),

    GV(U,V)=tr(y^-1 U y^-1 V)-tr(y^-1 U)tr(y^-1 V)/2.

The exact point jets of K2345 give

    R(U,t)=0 on the whole tangent space,
    R(X,U)t=-S X/8,
    R(t,X)V=+T X/8,
    R(U,V)X=-[S,T]X/4,
    R(X,U)V=-T S X/4.                            (2)

The companion reuses K2345’s metric two-jet backend to construct the full curvature matrices, independently contracts their Ricci tensor, and checks these identities on spanning horizontal/vertical bases, including the indefinite signs. The sign convention is the same as K2345; reversing all R signs leaves compatibility and rigidity unchanged. Retaining mixed connection and its derivatives is essential.

## 3. Eliminate every nonscalar block

Use (1) on (X,U,t), U traceless. Its horizontal part is

    -b S X/8+(y^-1 C(U))X/8=0,

so C(U)=bU for all U. Its vertical part is R(X,U)v=0. Pair it with t and use skew-adjointness of curvature:

    0=G(R(X,U)v,t)=-G(v,R(X,U)t)=g(v,SX)/8.

Choose invertible traceless S=diag(1,1,-1,-1). Since X is arbitrary and g is nondegenerate, v=0 and ell=0.

Now use (1) on (X,U,V), both traceless. Equations(2) reduce it to

    [S,T](bI-B)X=0.

Traceless g-self-adjoint S,T have commutators with zero common kernel. Explicitly take S0=diag(3,1,-1,-3) and T0j=E0j-Ej0 for j=1,2,3. Their commutators are nonzero multiples of Lorentz boosts E0j+Ej0; their common kernel is zero. Hence B=bI and A=bI pointwise. Finally scalar Codazzi forces db=0 in dimension>1, including null gradients. Base translations and the GL action transport this normalized-point argument throughout the fixed-signature metric fiber, as in K2363. Therefore the theorem is global on each connected chart component, with no boundary/domain assertion.

## 4. Stationarity consumer and scope controls

K2363's selected complete derivative Euler is E=2curl(A)+g wedge(divA-dtrA), whose contraction11Q makes E=0 equivalent to Codazzi. Curvature, mass and cubic terms are odd in Clifford parity and cannot cancel this even derivative equation for a pure grade-one field. Rigidity therefore forces constant radial T=bPhi1. K2357's remaining odd equations on this geometry differ by-3, independent of b and kappa. No such symmetric grade-one field is translation critical.

The result eliminates all105 symmetric coefficient functions as a route on THIS geometry, not all field configurations. A nonconstant flat Hessian is Codazzi; K2360's different parallel-product geometry has a nonscalar parallel stationary witness. These genuine escapes reject an invalid universal-Codazzi-implies-scalar extrapolation. Antisymmetric endomorphisms and mixed grades change the derivative/algebraic problem and remain live. Independent metric/epsilon variations, a common closed domain and source observation/matter maps are still required even after a translation solution is supplied.

The universal statement rests on the written curvature-compatibility proof; finite rational identities check its actual-metric hypotheses. No proof-assistant, external-expert, novelty or native-GU acceptance is claimed.
