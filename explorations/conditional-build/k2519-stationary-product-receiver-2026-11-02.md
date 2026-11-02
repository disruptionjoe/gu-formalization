---
title: "K2519 Full stationary product seeds and a native receiver obstruction"
status: active_research
doc_type: exploration
created: "2026-11-02"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematics and numerical evidence; no native GU or empirical certification
scripts:
  - tests/channel-swings/k2519_stationary_product_receiver_probe.py
---

# K2519 Full stationary product seeds and a native receiver obstruction

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
result: K2519
carrier: real Cl(7,7) fields over two seven-dimensional space forms with independent ambient metric LAYER=toy CHIRALITY=N/A
pairing: scalar Clifford trace, pseudo-Riemannian Hodge and moving ambient volume ON=declared_carrier
real_structure: real fields and real parameters
grading: Clifford grade, form degree, ambient metric and observer displacement remain distinct
action_owner: repository-construction -- selected comm/symi/symi I1 with an explicit moving-conjugation epsilon completion
target: full stationary local seed and concrete observation receiver compatibility MAP-TYPE=evaluation
```

## Result and exact boundary

The parallel7+7 product of [K2360](k2360-anisotropic-native-stationarity-2026-10-31.md) can be solved for metric AND all-translation stationarity. Its old translation-only witness fails the metric equations. We classify all real branches in this ansatz, close epsilon stationarity in an explicit gauge-conjugation completion, and construct a Lorentzian4 observer embedding. That embedding fails a specific native metric-fiber receiver test: normal displacements induce zero first-order metric change, whereas the tautological metric-bundle receiver has rank10.

These are full local stationary seeds of the DECLARED independent-ambient-metric first action, not native GU stationary solutions. The metric of Met(X), observed matter action, source/readout and physical Green domain have not been identified. SC-ACT-01/GEO-55 ASSERTS and SC-META-53 UNCERTAIN preserve their meanings. LT-GR10/11 and ledger0.263 stay unchanged. A scoped failure of this graft is not an exclusion of native GU, mixed-grade solutions or other embeddings.

## 1. Selected variational owner

Reuse [K2357](k2357-curved-native-stationarity-2026-10-31.md)'s real Clifford convention:

    I=int [P(T,S(F_B)) + (1/2)P(T,S(D_B T))
           +(1/3)P(T,S(T wedge T)) +(kappa/2)P(T,*T)].

B is the genuine Levi-Civita spin connection, Phi the parallel Clifford soldering one-form, S the selected comm/symi/symi Shiab map, P scalar trace/top-form pairing. A=B+T remains a full connection, not a claim that A is Levi-Civita or ordinary torsion. The metric G is an independent ambient14-dimensional variable in this completion. All variations have compact support; no global boundary/domain is claimed.

Let G be a local product of7-dimensional space forms of signatures(4,3),(3,4), Ricci eigenvalues lambda1,lambda2, sectional curvatures lambda_i/6. Set T=Phi composed A0, A0=aI7 direct-sum bI7. Both projectors are parallel. Write u=a+b,v=a-b,l=lambda1+lambda2,m=lambda1-lambda2.

K2360 proves the FULL-receiver translation equation for parallel selfadjoint diagonalizable A0:

    -2Ric+Scal I+kappa A0+4[A0²-tr(A0)A0+e2(A0)I]=0.

Its even derivative covector vanishes by parallelism; simultaneous sign-flip invariance and grade<=5 exclude untested odd receivers, as proved there. We reuse this exact support theorem, not a new finite scan. In the two blocks the equation is equivalent to

    l=-kappa u/12-13u²+v²,
    m=v(kappa-24u)/2.                                  (1)

## 2. The missing metric equations, with full variation

The exact density restricted to the parallel family is L=C+V, with

    C=Scal tr(A0)-2tr(A0 Ric)=42ul-7vm,
    V=4e3(A0)+(kappa/2)tr(A0²)
     =182u³-42uv²+(7kappa/4)(u²+v²).

The derivative term is zero along this family. Rescale the ith factor by exp(2t_i), keeping a,b fixed in the moving soldered frame. The volume has derivative7, and lambda_i derivative-2lambda_i, so the two metric rows are

    E1=7L-14lambda1(6u-v),
    E2=7L-14lambda2(6u+v).                              (2)

Why restricted scale derivatives suffice here: on E_T=0 the chain terms from changing Phi and A0 coordinates are E_T[delta T]=0. Thus the restricted derivative equals the independent fixed-T metric derivative. The full action is natural under simultaneous frame/spin transformations, so its Euler symmetric tensor at this locally homogeneous product is invariant under connected SO(4,3) times SO(3,4). Each standard factor has only its metric as invariant symmetric bilinear form; neither has an invariant covector and hence no cross-block invariant tensor exists. The Euler tensor therefore has exactly two scalar coefficients. Its pairing with the two independent factor metrics determines both. Equivalently localize the scale variations with compact support; after integration by parts derivative terms have covariantly parallel coefficients on this homogeneous seed and vanish. Global noncompact rescaling alone is not the justification. This covers arbitrary compactly supported inhomogeneous metric variations, not just homogeneous trial variations. Moving density, Hodge, Clifford identification and LC terms are included by the restricted action plus this tensor argument. It would fail without full E_T=0 or the local isotropy/naturality hypotheses.

On (1), E1=E2=0 reduce to

    6u m-v l=0,
    5kappa(u²+v²)+1144u³-264uv²=0.                      (3)

## 3. Complete real classification within the ansatz

For any real kappa, a=b=lambda1=lambda2=0 is a solution. If v=0 and u is nonzero, (3) gives the radial branch

    a=b=-5kappa/2288,
    lambda1=lambda2=35kappa²/604032, kappa!=0.           (4)

In particular K2357's old nonzero flat translation root is not jointly stationary.

For v!=0, (1),(3) imply

    v²=(37/12)kappa u-59u²,
    u[(185/12)kappa²-1104kappa u+16720u²]=0.

The u=0 case would force v=0. When kappa=0, v²=-59u² also forces zero; no divided-out real branch is lost. Otherwise let

    t_plus/minus=(828 +/- sqrt(105609))/25080,
    w=t(37/12-59t), u=kappa t, v=sigma kappa sqrt(w), sigma=+/-1,
    a=(u+v)/2, b=(u-v)/2,
    lambda1,2=kappa²(1-24t)[3t/2 +/- sigma sqrt(w)/4].   (5)

The defining polynomial is200640t²-13248t+185=0. Exact bounds324<sqrt105609<325 show both t>0 and t<37/720, so w>t²>0 and a,b have opposite signs. For t_minus, t<37/1140<1/24, the Ricci eigenvalues have opposite signs. For t_plus, t>1/24 and t>37/1140, both are negative. Neither is zero. Each sign permits a real local product space-form realization; no global completeness, stability or positive physical Hilbert metric is implied.

A decisive control is K2360's (a,b,kappa,lambda1,lambda2)=(1,-1,2,3,1). It obeys all translation rows but L=-14 and (E1,E2)=(-14,-126). Using it as a Hessian background for a stationary full theory would be invalid.

## 4. Epsilon and other primitive owners

Declare the moving-conjugation completion explicitly:

    B_e=e^-1 B0 e+e^-1 de,
    S_e=Ad_(e^-1) S0 Ad_e.

Trace invariance, covariant curvature and D_B covariance give the finite identity I(G,T,e)=I(G,Ad_e T,1). Hence all epsilon variations pair with the already zero full translation Euler covector. At fixed varpi the additional delta T=-D_B eta likewise contributes zero. This is a property of this completion, not proof that the source selected it or that a separately printed four-field residual has the same variational owner. Orthogonal coframe/spin changes are gauge, while G retains its independent variations above.

Zero barred/unbarred fermions solve a specified bilinear9.16-type completion and give zero current. This observation does not supply its missing density-dual matter action or a nonzero source/readout. The ambient I1 has no independent observer-section argument, so no nontrivial section equation follows until a localization/observation action is added. We do not call its absence a solved physical equation.

## 5. Actual pullback input and its failed graft

Inside the first factor choose a totally geodesic Lorentzian4 submanifold X of signature(1,3), with the second factor fixed. Such local space-form submanifolds exist for these signatures. Its second fundamental form II=0 and

    K_X=lambda1/6, Ric_X=(lambda1/2)gamma, Scal_X=2lambda1.

The normal rank is10, signature(6,4); the first-factor normal connection is flat along X because R(X,Y)n=0 for tangent X,Y and normal n, and product cross curvature vanishes. The pulled-back B splits into tangent spin LC and retained flat normal spin connection. The distortion is s*T=a Phi_TX, still a Clifford-valued ONE-FORM. Keep the restricted ambient spinor carrier and normal Clifford directions.

A14-form pulls back to zero on X4. Substituting a4-dimensional Hodge operator for the ambient14-dimensional one is not a derived observed action. A fiber/localization prescription with its density would be another construction.

For ambient metric variation H and displacement ds(v)+n, the induced metric obeys

    delta gamma=s*H+Lie_v gamma-2<II,n>.

At fixed ambient G, every pure normal displacement of this seed therefore has zero metric receiver. By contrast, [K2345](k2345-curved-bundle-ricci-obstruction-2026-10-30.md)'s tautological metric-bundle graph has vertical displacement h_ab with delta gamma_ab=h_ab: rank10. No invertible first-jet receiver-preserving identification maps the zero normal receiver to that native identity receiver. The fact that ranks and signatures of the bundles match is insufficient. This rules out the stated fixed-ambient, pure-normal graft, not coupled ambient metric variation, tangential mixing or a different embedding with nonzero II.

A second, conditional compatibility check: the flat normal connection cannot be identified connection-preservingly with the LC-induced S²T*X connection for any nonzero branch. Its curvature on a spacelike two-plane sends a diagonal symmetric tensor to a nonzero off-diagonal tensor proportional to K_X; a traceless choice gives the same obstruction. All nonzero branches have lambda1!=0. This concerns that explicitly chosen LC-induced vertical connection, not every possible native vertical connection.

Normal displacement does not disappear from all readouts. In a compatible gauge/trivialization,

    delta(s*A)=s*(delta A+i_xi F_A)+D_(s*A)(s*i_xi A).

Curvature and normal Clifford coupling remain. The constructed metric/connection/distortion and these receiver maps are concrete inputs, but they do not determine `(r_light-c r_motion) G_full |S`. Eliminating T still transforms source and readout and retains contact terms; singular blocks require the full coupled operator.

## Evidence and released next question

The exact probe checks density, full translation reductions, both metric rows, complete algebraic branches and sign intervals, predecessor failure, induced curvature and a symmetric-tensor curvature receiver. These are exact symbolic/finite controls. Universal all-receiver, local-isotropy and pullback claims use the written arguments and pinned predecessor theorems; the probe does not certify all infinite-dimensional variations by enumeration. Independent specialist and integrated hostile review examine those arguments. No proof-assistant, external-expert, empirical or novelty certification.

A non-totally-geodesic native observer construction must restore the rank10 receiver while preserving the full coupled stationary equations, or the actual [K2366](k2366-curvature-codazzi-rigidity-2026-10-31.md) geometry needs a mixed-grade solution outside its fixed Codazzi exclusion. The new stationary seeds remove the translation-only shortcut and show precisely why this natural transplant still fails. They do not settle the actual Met(X) action, matter/light response, physical quotient or boundary inverse.
