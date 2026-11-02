---
title: "K2521 Free observer receiver repair and connection-preserving obstruction"
status: active_research
doc_type: exploration
created: "2026-11-02"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematics; no native GU or empirical certification
scripts:
  - tests/channel-swings/k2521_free_observer_receiver_probe.py
---

# K2521 Free observer receiver repair and connection-preserving obstruction

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
result: K2521
carrier: Lorentzian4 graph in K2519 stationary real 7+7 product ambient space with independent metric LAYER=toy CHIRALITY=N/A
pairing: ambient normal metric and trace-reversed DeWitt form on symmetric covariant tensors ON=declared_carrier
real_structure: real local smooth embedding and real pseudo-Riemannian metrics
grading: tangent4, normal10, Clifford degree and metric variation remain distinct
action_owner: repository-construction -- K2519 selected first action and declared moving-conjugation completion
target: rank-ten induced metric receiver and its connection/section compatibility MAP-TYPE=evaluation
```

## Result and boundary

[K2519](k2519-stationary-product-receiver-2026-11-02.md)'s rank-zero obstruction is specific to its totally geodesic observer. A genuine local graph in the SAME stationary ambient product repairs the normal metric receiver to rank10 throughout a neighborhood. At its center the receiver can be an isometry to the native-signature trace-reversed DeWitt form. This does not repair a connection-preserving identification: on every nonzero stationary product branch, an observer initially tangent to the first factor with parallel receiver must have rank at most3. We also test the simplest new section-action owner: a minimal section always loses at least the trace direction.

The ambient independent-metric action remains stationary by inheritance; it has no observer-section equation. No native Met(X) identification, observed matter action, nonzero source/readout or physical Green domain has been constructed. SC-ACT-01/GEO-55 ASSERTS and SC-META-53 UNCERTAIN retain their source meanings. LT-GR10/11 and ledger0.263 remain unchanged. This is not a GU exclusion or a claim that the source requires a parallel receiver.

## 1. A genuine graph, not unconstrained jet data

Choose any K2519 local stationary product seed and a point p. The first factor has signature(4,3), the second(3,4). Choose V subset T_pY in the first factor of signature(1,3), gamma=diag(1,-1,-1,-1). Its normal N has signature(6,4): three positive directions in the first factor and all seven directions in the second. In ambient Riemann normal coordinates use

    s(x)=exp_p(sum_i x^i e_i + sum_A f^A(x)n_A),
    f^A(x)=-sigma_A S_A,ij x^i x^j/4,
    <n_A,n_B>=sigma_A delta_AB.

Einstein summation over both symmetric indices is intended. At zero df=0 and ambient Christoffel symbols vanish. Thus ds has rank4, the induced metric is gamma, and

    II_ij=-(1/2)sum_A sigma_A S_A,ij n_A,
    L(n)_ij=delta_n gamma_ij=-2<n,II_ij>,
    L(n_A)=S_A.                                      (1)

The graph is a smooth embedding on a sufficiently small neighborhood and its induced metric stays Lorentzian. If the ten S_A form a basis, rank L=10 there by continuity. All Gauss/Codazzi/Ricci equations hold for these induced fields because an actual embedding has been constructed; no theorem prescribing an arbitrary metric and II is invoked. There is no prescribed physical background gamma away from zero.

## 2. Explicit DeWitt point isometry and induced geometry

Let G_D(S,T)=tr(gamma^-1 S gamma^-1 T)-(tr_gamma S)(tr_gamma T)/2. Choose positive basis

    diag(1,1,0,0)/sqrt2,
    diag(1,-1,2,0)/sqrt6,
    diag(1,-1,-1,3)/sqrt12,
    (E12+E21)/sqrt2, (E13+E31)/sqrt2, (E23+E32)/sqrt2

and negative basis

    (E01+E10)/sqrt2, (E02+E20)/sqrt2,
    (E03+E30)/sqrt2, gamma/2.

Their Gram matrix is diag(+1 six times,-1 four times). Assign the first three positive basis vectors to first-factor normals and the remaining seven to second-factor normals. Equation(1) makes L an isometry AT p. Rank stays full nearby, but pointwise isometry has not been shown nearby. The completeness identity is

    sum_A sigma_A S_A,ij S_A,kl
      =(gamma_ik gamma_jl+gamma_il gamma_jk-gamma_ij gamma_kl)/2 = Q_ij,kl.

Hence <II_ij,II_kl>=Q_ij,kl/4. With H=tr_gamma II (unnormalized), H=n_trace, <H,H>=-1, and the signed norm ||II||^2=2. In the convention R(X,Y)Z=c(<Y,Z>X-<X,Z>Y), define R_ijkl=<R(e_i,e_j)e_l,e_k>. For c1=lambda1/6, Gauss at p yields

    R^X_ijkl=(c1-1/4)(gamma_ik gamma_jl-gamma_il gamma_jk),
    Scal_X=12c1-3.                                  (2)

This curvature is induced by the graph, not an assumed unchanged K2519 observer curvature. The pulled-back LC connection has mixed II blocks. For distortion T, s*T=a Phi(ds_1)+b Phi(ds_2); it reduces to a Phi_TX only at p or on the radial a=b branch. Reusing the old totally-geodesic connection or pullback throughout the graph would be false.

## 3. Released connection compatibility test

A connection-preserving receiver means nabla L=0 for the induced normal and Levi-Civita Sym² connections. Since both metrics are parallel, (1) makes this equivalent to nabla II=0. This is an ADDITIONAL graft requirement, not a requirement inferred from source silence.

Suppose nabla II=0 on a neighborhood and T_pX lies wholly in the first product factor. Codazzi implies <R^Y(X,Y)Z,n>=0 for every normal n throughout the neighborhood. Differentiate this identity in a tangent W at p, choosing induced tangent/normal frames parallel there, and take n in the second-factor seven-plane. The product ambient curvature is parallel. Terms involving II in the first three slots have zero pairing with this n (mixed product curvature vanishes); the derivative of n contributes -A_n W. Thus, up to the immaterial overall sign,

    c1[gamma(Y,Z)<II(W,X),n>-gamma(X,Z)<II(W,Y),n>]=0. (3)

For c1!=0, contract Y,Z to obtain 3<II(W,X),n>=0. Therefore all seven such normal directions are killed by L and rank L<=3. This contradicts the free graph's rank10. K2519's classification proves lambda1!=0 on every nonzero real stationary branch, so (3) covers all those branches. A tilted initial tangent, changed ambient geometry or nonparallel receiver is outside this obstruction.

There is also an independent point-curvature check for the isometric graph. Write W(X,Y)Z=gamma(Y,Z)X-gamma(X,Z)Y and rho(W)S=-W^T S-SW. Its shape operators are A_n=-gamma^-1 L(n)/2. At p ambient tangent-normal curvature is zero. Ricci gives

    <Rperp(X,Y)n,m>=gamma([A_n,A_m]X,Y),
    L Rperp L^-1=(1/8)rho(W).

A parallel isometric receiver instead requires rho(R^X)=(c1-1/4)rho(W). Thus c1=3/8 is necessary. That isolated equality does NOT rescue the nonzero product branch: (3) still applies. On the zero flat branch c1=0, the Ricci mismatch already prevents this point-isometric graph from extending to a parallel isometric receiver. These are local compatibility statements, not a global normal-bundle classification.

## 4. Released section-action countercontrol and source consequences

For ANY nondegenerate observer embedding, tr_gamma L(n)=-2<H,n>. If H=0, image L is trace-free and rank<=9. Thus adding only a nonzero uncoupled area-tension section action, whose compactly supported normal Euler equation is H=0, cannot retain the full rank-ten receiver. Our graph has H=n_trace!=0 and is not stationary for that added action. Ambient stationarity alone never solved this new equation; adding localized section matter can also change ambient equations.

A coupled/sourced section equation may permit nonzero H, so the area result is a scoped countercontrol. The physical successor needs an actual source-owned section/metric relation and its coupled variations, not a chosen graph plus a claim of complete stationarity. The fixed-source matter/light consumer still requires paired source/readout, contact terms and the common physical domain. Rank restoration eliminates a kinematic barrier, while connection and section stationarity supply sharper independent remaining tests.

Evidence: universal graph and differentiated-Codazzi proofs, exact basis/Gram/Gauss/Ricci algebra, original stationary-seed inheritance and contrary controls. Finite matrix checks support their stated identities, not a proof of all smooth nonlinear physics. Independent review is internal, not external-expert or proof-assistant certification.
