---
title: "K2539 Full curved tensor constraints and a conserved source construction"
status: active_research
doc_type: exploration
created: "2026-11-04"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: exact covariant tensor equations, scoped profile exclusions and generated conserved-source full local solutions; no fixed-source Green or physical observation claim
scripts:
  - tests/channel-swings/k2539_covariant_tensor_constraints_probe.py
---

# K2539 Curvature is part of source compatibility

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
result: K2539
carrier: independent ambient symmetric metric and End(V) grade-one displacement on the fourteen-dimensional stationary Einstein product LAYER=toy CHIRALITY=N/A
pairing: inherited indefinite symmetric/skew contraction with compact-support differential adjoints ON=declared_carrier
real_structure: real signature (7,7), kappa nonzero, locally symmetric product
grading: symmetric tensor, skew two-form, vector constraint and metric source remain distinct
action_owner: repository-construction -- selected comm/symi/symi I1 completion with moving soldering
target: full covariant conserved-source constraints and explicit generated-source local solutions MAP-TYPE=evaluation
```

## Result and source boundary

The [K2537](k2537-reduced-action-decoupling-2026-11-04.md) action gives an exact second-order vector equation reconstructing the skew field, and a full symmetric-divergence equation retaining the product Weyl tensor. The Weyl term prevents the tempting scalar/vector-only closure. Direct curved fixtures exclude nonconstant pure-trace and one-factor-volume tensor profiles for conserved metric forcing. A coupled two-factor profile repairs that restriction and constructs a nonzero conserved source class. A differential subfamily then supplies both forced sectors and the original metric explicitly. This is a real compatibility construction, not a solution for an arbitrarily prescribed source.

SC-ACT-01 ASSERTS the first-order action; SC-GEO-55 ASSERTS displacement from gauge-rotated Levi-Civita; SC-GEO-03 ASSERTS Met(X), not the independent ambient metric used here; SC-META-53 remains UNCERTAIN about indefinite physical spectra. These source polarities and ledger0.263 GR6b/10/11 are unchanged. Native Met(X), physical quotient, full source/readout boundary realization and observed gravity remain unbuilt. No conditional profile exclusion becomes a source-claim verdict.

## 1. Fix all coefficients and pairings

Reuse K2537, without replaying its native Clifford census:

    a0=-5kappa/2288, lambda=35kappa²/604032,
    m0=-4kappa/11, mS=158kappa/143, mK=148kappa/143,
    mV=503kappa/858, mH=893kappa/858,
    beta=(m0-mS)/14=-15kappa/143.

Let Q=C+K after lowering indices, with C symmetric and K skew, tau=tr C, v=div C-dtau, and w=11v+13div K. Symmetric and skew field pairings are FULL contractions; the three-index hook pairing is (1/2)H_ijk H^ijk. All may be indefinite. Define

    (Jv)_ijk=G_ik v_j-G_ij v_k,
    H_ijk=2(nabla_j C_ik-nabla_k C_ij)+(2/13)(Jv)_ijk,
    S_ik=nabla^j H_(i|j|k),
    V* w=G divw-sym nabla w.

The kinetic terms in the reduced action are |w|²/(26mV)+|H|²/(2mH), with the indicated hook norm. Direct compact-support variation gives the COMPLETE tensor equations for a pure metric source j:

    mK K - (1/(2mV)) d w=0,                         (1)
    F_C := mS C+beta tau G +(11/(13mV))V*w
           -(2/mH)S +(1/(3a0))E C = -j/(6a0).      (2)

Here E is the actual cosmological Einstein linearization from K2537. It includes the product curvature and is divergence-free on this Einstein seed. The skew coefficient 1/2 in (1) comes from the full two-index pairing: integrating w^j nabla^i delta K_ij gives -(1/2)(dw)^ij delta K_ij. The hook coefficient in (2) comes from its two antisymmetric last-index terms and subsequent symmetric projection. These conventions cannot be changed without changing the coefficients.

Equation (1) is stronger than closedness alone:

    K=dw/(2mK mV),
    [I-13/(2mK mV) div d]w=11v.                    (3)

It implies dK=0 and divw=11divv, using divdivK=0. All identities hold distributionally. No inverse of the vector operator in (3) is being assumed, and w is not a new gauge freedom.

## 2. Compute the full curved divergence

Set b=div C, so v=b-dtau. Use the curvature convention

    (Riem C)_ik=R_ipkq C^pq,
    Delta_L C=-Box C+2lambda C-2Riem C.

Direct covariant derivative commutation gives

    S=2Box C-2sym nabla b-2lambda C+2Riem C
       +(2/13)(G divv-sym nabla v).                (4)

On the Einstein product the Ricci tensor is parallel. The local commutator identities needed for divergence are

    div Box C=Box b+lambda b-2div(Riem C),
    div sym nabla b=(Box b+d divb+lambda b)/2,
    Box dtau=d Box tau+lambda dtau,
    div d v=Box v-d divv-lambda v.

Substitution in (4) gives

    div S=(12/13)div d v-(2lambda/13)v-2div(Riem C).

Since Riem C=(lambda/13)(tau G-C)+W C, the two v terms cancel exactly:

    div S=(12/13)div d v-2div(W C).                 (5)

This is local Ricci-commutator algebra, valid with the declared indefinite contraction; it imports no positive spectral theorem. For literature/convention context, the parallel-Ricci Lichnerowicz commutation is recorded in [Bracken, AIMS Mathematics 2 (2017), section 3](https://www.aimspress.com/aimspress-data/math/2017/3/PDF/Math-02-00545.pdf). The explicit formulas and curved fixture here carry the particular application.

For conserved j, divergence of (2) therefore yields

    mS v+kappa dtau
    -[11/(26mV)]div d w-[11lambda/(13mV)]w
    -[24/(13mH)]div d v+[4/mH]div(W C)=0.           (6)

The mass coefficient is mS+beta=kappa. No third derivative has been suppressed by a flat-space replacement. In particular the actual product is not maximally symmetric and W is not zero.

Taking one further divergence gives an exact scalar consumer. With u=divv,

    [mS-121lambda/(13mV)]u+kappa Box tau
       +(4/mH)divdiv(W C)=0,                       (7)
    mS-121lambda/(13mV)=5082101kappa/4603456.

Combine (7) with K2537's full trace equation

    -(5kappa/12)tau+[2820818/(2515kappa)]u
       =[1144/(15kappa)]tr j.                     (8)

Equations (7)--(8) are genuine scalar consequences, but remain coupled to C through divdiv(W C). Solving (8) alone is not solving the field equations.

## 3. A direct curved counterconstruction

Write the seed as a product of two seven-dimensional constant-curvature factors A and B, each with Ric=lambda G. Let phi vary on B only and take C=phi G_A, K=0. Then tau=7phi, b=0, v=-7dphi, w=-77dphi and dv=dw=0. Direct evaluation, without (5), gives

    S=2(Box_B phi)G_A-(14/13)(Box_B phi)G
       +(14/13)Hess_B phi,
    div S=(14lambda/13)dphi.

Meanwhile div(W C)=-(7lambda/13)dphi. Omitting Weyl in (5) would predict zero and fails on this curved field. This tests the curvature sign as well as its presence.

The complete equation has

    div F_C=cA dphi,
    cA=-105kappa/143+847lambda/(13mV)-28lambda/(13mH)
       =-2992502835kappa/4110886208 !=0.

Thus this nonconstant one-factor-volume tensor cannot answer a conserved metric source. For C=phi G, K=0, a separate direct trace control gives

    div F_C=cFull dphi,
    cFull=m0+121lambda/mV=-124533kappa/354112 !=0.

The pure-trace ansatz also fails unless phi is constant. These exclude two specified Q profiles, not the full response or all metric-only matter sources. They explain why replacing the full system by its traced equation is unsafe.

## 4. Execute a coupled repair, including its actual source

The two exclusions suggest the finite repair C=phi(A G_A+B G_B), K=0 with constant A,B and phi on B. Set

    t=7(A+B), q=7A+6B, p=7A+5B.

Now tau=t phi, v=-q dphi, w=-11q dphi, and the skew equation holds exactly. Directly evaluating (2), including E, gives block-diagonal tensors

    (F_C)_A=G_A[M_A phi+R_A Box_B phi],
    (F_C)_B=G_B M_B phi+R_B[G_B Box_B phi-Hess_B phi],
    M_A=mS A+beta t+lambda(t/2-A)/(3a0),
    M_B=mS B+beta t+lambda p/(6a0),
    R_A=-121q/(13mV)-24(A-B)/(13mH)+(A+B)/a0,
    R_B=-121q/(13mV)+28(A-B)/(13mH)+p/(6a0).

Thus div F_C=(M_B-lambda R_B)dphi, with every third derivative canceling by div Hess_B phi=d Box_B phi+lambda dphi. This is a second independent evaluation of (6). Choose

    A=1, B=-cA/(cFull-cA)=332500315/171866582.

Then M_B=lambda R_B, so the B block is exactly R_B[G_B Box_B phi-Hess_B phi+lambda phi G_B], whose divergence is zero. Hence

    j=-6a0 F_C

is an explicit conserved metric-source tensor for which Q=C,K=0 solves the COMPLETE tensor subsystem. It is not merely a conserved vector constraint. The source is nonzero: for a nonzero constant plateau of phi,

    M_A=-308132384957kappa/272236665888,
    M_B=-24749767063kappa/272236665888,

both nonzero. A smooth bump in a B chart supplies such a local example. It is invariant in the A directions; no global compact support in A is asserted.

The construction extends to a distribution phi on B because the operator identities have smooth coefficients. For phi=delta_B it produces Hessian/Box derivatives of delta as well as order-zero terms. It is therefore NOT the prescribed order-zero thin tension or partial-width stress of K2531. This repair proves a nonempty compatible tensor-source class and prevents extrapolating the two ansatz failures to universal source impossibility; it does not repair a fixed source by secretly changing it.

## 5. Follow through to explicit FULL sourced fields

The generated source class contains a subfamily for which the Einstein equation can also be solved without choosing an inverse. Let chi be any smooth scalar on a B chart, put b=332500315/171866582, use the repaired M_A,R_A,R_B above, and set

    phi=(Box_B+2lambda)chi,
    C=phi(G_A+b G_B), K=0,
    z=u G_A+v G_B,
    u=[(6R_B-5R_A)/12]Box_B chi
      +[(7lambda R_B-5M_A)/12]chi,
    v=(R_B phi-7u)/5.                              (9)

Independent variation of the ORIGINAL metric Ricci tensor for z gives

    delta Ric_A=-(Box_B u)G_A/2,
    delta Ric_B=-Hess_B(7u+5v)/2-(Box_B v)G_B/2,
    delta R=-7Box_B u-6Box_B v-7lambda(u+v).

Therefore

    (E z)_A=G_A[3Box_B(u+v)+lambda(5u+7v)/2],
    (E z)_B=(G_B Box_B-Hess_B+lambda G_B)(7u+5v)/2.

Substituting (9) gives E z=F_C/2=-j/(12a0) identically, using M_B=lambda R_B. The remaining fields are

    h=z-C/(6a0), e2=-A2^-1 BQ,

with other reduced grades zero as allowed by K2535. Thus the full linearized reduced system, including the Einstein sector and original readout, has explicit nonzero solutions for these generated sources. This is stronger than a necessary compatibility condition. In particular

    h_A=[404018270kappa²-24838948849Box_B]chi
         /(945266201kappa),
    h_B=-91[571569kappa²+21422093Box_B]chi
         /(85933291kappa).

These coefficients are metric multipliers on their respective factors, not observed coupling constants. The probe independently checks both original Einstein blocks and the original-metric correction. On a constant nonzero chi plateau the source is nonzero; h differs from z. A smooth B-compact bump gives B-compact fields/source. The construction is homogeneous in A; it is not an observer-localized or globally compact source on the product.

All formulas are polynomial differential operators with smooth coefficients, so they also act on distributions chi. For chi=delta_B, h has nonzero Box delta terms, and the generated source generally has fourth derivatives of delta. These are not the order-zero K2531 tension, and its source regularity threshold cannot be copied unchanged. No arbitrary prescribed-source inversion, uniqueness, or boundary choice is claimed.

## 6. Readout and the remaining fixed-source question

For smooth chi this construction has a smooth local original metric, so local restriction to a smooth observation section is mathematically defined. It still supplies neither native Met(X) ownership nor an observed physical response. For chi=delta_B, the explicit nonzero Box delta terms in h cannot be evaluated at B=0 as ordinary functions. A normal smearing or separately defined renormalized observable must be supplied; a failure of a sufficient wavefront test alone would not establish a general obstruction. Here the warning is grounded in the explicit component, not the source's singularity alone.

The prescribed conserved order-zero stress remains different from j=-6a0F_C constructed by choosing chi. Its full common boundary/source/readout realization in signature (7,7) remains open. Neither conservation nor the existence of this generated solution class proves it is in the same operator range. No physical positivity, PPN signature, native Met(X) construction or GU credit is claimed.

## Evidence and next calculation

Universal compact-support variation and Ricci commutators prove (1)--(8). The probe checks full pairing-normalized derivative symbols on nonnull and null covectors, mass coefficients, independent curved factor formulas, exclusions, the repaired generated source and the explicit full Einstein/tensor solution. Finite controls and report consistency remain distinct from the universal proof. Native coefficient banks from K2537 are reused, not recounted.

The next useful question is whether the PRESCRIBED conserved order-zero source lies in a common tensor/Einstein boundary realization with a defined original-metric readout. The constructed source class supplies a positive compatibility control; the failed pure profiles and retained Weyl term constrain that attempt. A new rank census or imposing K=0/C pure trace without its equations would repeat refuted shortcuts.
