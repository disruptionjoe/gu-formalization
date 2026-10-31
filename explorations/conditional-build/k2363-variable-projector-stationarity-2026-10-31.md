---
title: "K2363 Variable-projector exclusion through the complete Codazzi equation"
status: active_research
doc_type: exploration
created: "2026-10-31"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematical and numerical results; no native GU or hardware certification
scripts:
  - tests/channel-swings/k2363_variable_projector_stationarity_probe.py
---

# K2363 Variable-projector exclusion through the complete Codazzi equation

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
result: K2363
carrier: real symmetric endomorphisms on the actual fourteen-dimensional metric bundle LAYER=toy CHIRALITY=N/A
pairing: scalar Clifford trace and exterior Hodge ON=declared_carrier
real_structure: real Cl(7,7) and real smooth metric-self-adjoint A
grading: Clifford parity separate from differential form degree and metric splitting
action_owner: repository-construction -- selected comm/symi/symi I1 with fixed metric and epsilon
target: full derivative Euler and smooth variable-projector stationarity MAP-TYPE=evaluation
```

## Result and scope

Allowing arbitrary smooth coefficient functions does not repair [K2360](k2360-anisotropic-native-stationarity-2026-10-31.md)'s excluded horizontal/trace/traceless projector ansatz on the actual K2345 metric. The complete derivative-adjoint equation for symmetric soldering endomorphisms is equivalent to the Codazzi equation in dimension14. Applied to those nonparallel projectors, it forces all three functions equal and constant. The remaining odd Euler rows have the existing nonzero Ricci obstruction. This excludes the entire smooth three-projector family, not general symmetric or mixed-grade fields.

The backward demand is a true stationary receiver background for matter/light response. SC-ACT-01 and SC-GEO-55 ASSERTS retain source status, while selected Shiab, real Cl(7,7), metric and ansatz remain repository constructions. No metric/epsilon stationarity, boundary-domain theorem, source-observation bridge or native GU verdict follows. Ledger0.263 is unchanged.

## 1. Complete derivative Euler, including its adjoint

Let A_ij be a real metric-self-adjoint endomorphism with both indices lowered, T_i=A_i^j gamma_j, and N_kij=∇_k A_ij symmetric in i,j. Work with Levi-Civita total connection and covariantly parallel Clifford/Hodge data, using compactly supported variations. The derivative piece is

    E_D[Z]=1/2 {P(Z,S(DT))-sum_k P(∇_k T,S(e^k wedge Z))}.

After the nondegenerate receiver pairing is identified, its only possible Clifford receiver grade is2. The first Shiab summand sends grade1 to grade2 through the vector commutator. The second sends grade1 to grade3 through the bivector anticommutator, then grade3 to grade2 through the vector anticommutator. For the adjoint, only a grade2 receiver reaches grade1 to pair with ∇T; grade0 first commutator vanishes and grades4 or higher cannot contribute grade1 after the stated bracket parity. Exterior contractions retain the corresponding one-form slot. This accounts for all receiver grades, rather than testing one attractive row.

The metric-natural tensor has one free form index i and antisymmetric pair jk. For N symmetric in its last pair, its only metric contractions are N_jik-N_kij, g_ik ∇_j trA-g_ij ∇_k trA, and g_ik(div A)_j-g_ij(div A)_k. No orientation tensor of rank14 can occur in this rank3, one-derivative expression. Exact selected-backend coefficients give

    Q_j=(div A)_j-∇_j trA,
    E_i;jk=2(∇_j A_ik-∇_k A_ij)+g_ik Q_j-g_ij Q_k.       (1)

The displayed components use the nondegenerate receiver Riesz identification; a particular sorted Clifford blade/pseudo-orthonormal receiver can add a nonzero sign. Contracting i,k gives (n-3)Q_j. Therefore in n14, E=0 forces Q=0 and then ∇_j A_ik=∇_k A_ij. Conversely a symmetric Codazzi tensor has div A=d trA and E=0. This is not parallelness: on flat space a nonconstant Hessian is Codazzi and supplies an explicit countercontrol (the two-variable probe extends by zero in the other twelve directions).

The backend probe fixes the three coefficients by independent diagonal and mixed symmetric jets, checks negative-signature receivers, reproduces the radial -11 coefficient and K2360 connection rows, and checks the contraction symbolically. The invariant contraction classification supplies the universal formula; finite fixtures alone would not prove it.

## 2. The actual projector geometry

Use K2345's G=diag(y,GV) with GV(U,V)=tr(y^-1Uy^-1V)-tr(y^-1U)tr(y^-1V)/2. At the normalized point y=diag(1,-1,-1,-1), let P_H,P_t,P_s be horizontal, vertical trace and vertical traceless projectors. Vertical covariant differentiation preserves this splitting. For diagonal vertical v, y^-1v=diag(r_h),

    ∇_X v=(1/2)y^-1v X

in the horizontal component. The family is A=a P_H+b P_t+d P_s with arbitrary smooth real a,b,d depending on ALL coordinates. Codazzi evaluated on vertical v and horizontal basis h gives

    v(a)=(w_v-a) r_h/2 for every h,                    (2)

where w_v=b for trace v and d for traceless v. Derivatives along h contribute only vertical components in the comparison and cannot cancel this horizontal component.

Take traceless v=y diag(1,1,-1,-1)/2. Comparing h0 and h2 in(2) yields d=a at every point, and v(a)=0. This is an identity of smooth functions, so their derivatives also agree. Next take trace t=y/2 and a nonzero vertical traceless vector w. Since the vertical projectors are parallel, the vertical-vertical Codazzi equation is

    t(d) w = w(b) t.

Their independent subspaces force t(d)=0. Thus t(a)=0. Now(2) for trace t has r_h=1/2, implying b=a. Hence A=aI. Scalar Codazzi in dimension>1 forces da=0, including null gradients; contracting or comparing two independent vectors proves it. K2345 base translations and the GL action are isometries preserving the horizontal, trace and traceless splitting and act transitively on the fixed-signature metric fiber. They transport these normalized-point equations to every chart point; the argument is tensorial and normal-frame-independent. All smooth three-projector candidates collapse to a constant radial field on each connected component.

## 3. Remaining equation and genuine scope escape

Curvature, mass and cubic Euler terms for grade1 T have odd parity and cannot cancel the even derivative rows. With a=b=d constant, K2357's two independent odd equations on this geometry differ by-3, irrespective of a or kappa. Thus there is no full translation-critical field in this smooth three-projector family. No division by a, kappa or a gradient was used; zero and null cases are included.

A general symmetric Codazzi endomorphism is not ruled out. K2360's parallel product witness remains valid on its different geometry; a flat Hessian gives a nonparallel derivative-zero control. Mixed even/odd fields may cancel through different algebraic/derivative channels and are also outside the proof. The next useful actual-metric construction must leave the three-projector family and still meet all transverse, metric/epsilon and common-domain requirements. Repeating variable coefficients within this family is now unnecessary.

Checks deliberately omit the adjoint, freeze the nonparallel projectors, use only one horizontal receiver, or incorrectly generalize Codazzi to parallelness. These changes are detected. No brute-force full-field enumeration, proof-assistant, novelty or physical certification is claimed.
