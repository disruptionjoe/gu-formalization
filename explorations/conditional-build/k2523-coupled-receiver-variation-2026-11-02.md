---
title: "K2523 Coupled receiver variation and bending obstruction"
status: active_research
doc_type: exploration
created: "2026-11-02"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematics; no native GU or empirical certification
scripts:
  - tests/channel-swings/k2523_coupled_receiver_variation_probe.py
---

# K2523 Coupled receiver variation and bending obstruction

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
result: K2523
carrier: Lorentzian4 observer with rank-ten normal metric receiver in independent pseudo-Riemannian ambient14 LAYER=toy CHIRALITY=N/A
pairing: full ambient and intrinsic variational duals and signed normal contraction ON=declared_carrier
real_structure: real nondegenerate tangent and normal metrics
grading: ambient metric, independent connection displacement, observer section and matter variations remain distinct
action_owner: repository-construction -- declared intrinsic or quadratic bending additions to stationary ambient seed
target: coupled Euler equations, normal-jet defect coefficient and source-conjugate linear response MAP-TYPE=evaluation
```

## Result and scope

[K2521](k2521-free-observer-receiver-2026-11-02.md) repairs the metric receiver kinematically. We now compute two independent action tests. An intrinsic action on a free observer imposes its full metric Euler equation and, under stated domain assumptions, carries its own intrinsic response into the ambient/section system. An uncancelled quadratic bending defect instead produces a normal-derivative ambient metric source: rank ten excludes every nonzero coefficient pair in that class. The intrinsic Einstein action is an explicit contrary route because its ambient Gauss-curvature term cancels that derivative source.

These are conditional graft statements. SC-ACT-01/GEO-55 ASSERTS do not source-select either addition; SC-META-53 remains UNCERTAIN. Native Met(X) variation is not independent ambient G variation. LT-GR10/11 and ledger0.263 do not move. No physical source/readout/Green domain, stationary Einstein free embedding in K2519's curved ambient, or native motion/light ratio is established.

## 1. Complete first variation, not a rank-only inference

Let gamma=s*G, R h=s*h and L n=-2<II,n>. An independent metric variation h and section variation v+n give

    delta gamma=R h+Lie_v gamma+L n.                 (1)

For any supplied intrinsic S_X(gamma,psi), retain its FULL Euler covector E_gamma, including density, pairing, coframe, connection-chain and matter contributions. Under compactly supported variations the normal section equation is L*E_gamma=0. If L:N->Sym²T*X is an isomorphism everywhere on the patch, this is equivalent to E_gamma=0. Tangential equations retain their diffeomorphism/matter Noether identity. No positive inner product is needed: stars denote actual variational duals, not coefficient transposes for differential operators.

For intrinsic EH plus matter this is the known free-embedding Einstein mechanism; see [Bustamante, Debbasch and Brachet](https://arxiv.org/abs/gr-qc/0509090) and [Willison](https://arxiv.org/abs/1311.6203). Those results do not supply a solution in the particular curved (7,7) K2519 ambient. K2521 is Einstein at its central point only; rank10 nearby does not prove intrinsic equations nearby.

If the independent ambient seed is stationary and S_X has no other ambient dependence, ambient metric variation adds R*E_gamma. Thus a simultaneous E_gamma=0 solution leaves that ambient first variation zero. A nonzero pure uncoupled tension has E_gamma proportional to gamma^-1 and is excluded by full rank, reproducing K2521's trace obstruction. Zero bilinear matter at psi=0 gives E_gamma=0 but no nonzero section-sector response by itself; this does not exclude a geometric intrinsic action.

## 2. Released full Hessian and imported response

Assume the action has the additive form I_bulk(b)+S_X(gamma,psi), with b=(G,T,epsilon,...) and intrinsic-only fields psi: the two parts share gamma through G and s but have no additional shared arguments or direct cross-action terms. At a simultaneous stationary bulk/intrinsic solution, in a tangent-coordinate gauge with normal section n, put k=Rh+Ln. Retain all bulk-internal and intrinsic-internal mixed blocks. With their variations suppressed in the displayed notation only, the quadratic form is

    Q(h,n)=H_bulk[h,h]+H_X[Rh+Ln,Rh+Ln].             (2)

This is the full Hessian chain rule. The term E_gamma[D²gamma] vanishes only because the intrinsic Euler covector vanishes. Connection displacement T and epsilon remain in the bulk block and psi in the intrinsic block. If S_X also depends on T, epsilon, shared matter or other bulk fields, the cross terms generally prevent this diagonalization: the full unreduced Hessian is required and equations(2)-(3) do not establish decoupling. The bulk is section independent in the additive conditional class.

Invertible L gives the linear change n=L^-1(k-Rh). General source covectors transform as

    j_k=L^{-*}j_n,    j_bulk'=j_bulk-R*L^{-*}j_n.     (3)

An induced-metric source (R*j,L*j) becomes (0,j); the same transformation applies to a fixed induced-metric readout. If compatible domains and inverses exist, its response is exactly r G_X j. This imports the supplied intrinsic dynamics; it does not derive that dynamics from I1. A general source/readout need not decouple, and dropping the second term in (3) changes the response. The existing [complete matter/light formula](../../lab/active-research/joe-directed/prediction-kickoff/matter-light-reciprocity-2026-10-27.md) still governs Schur reduction, contact terms and singular blocks.

Equations(2)-(3) are formal smooth/local identities. Ambient restriction is a trace operator; the chosen function spaces must admit its trace, L inverse, transformed domains and dual sources. No global inverse, nonlinear Nash coordinate chart, positivity or physical causal propagator follows from the finite control. A singular intrinsic Hessian requires constraints/gauge/domain treatment; invertible L does not remove its gauge kernel.

## 3. Full ambient normal jets constrain bending actions

Take the localized addition

    S_b=(1/2)int_X [alpha||II||²+beta||H||²] mu_gamma,
    H=tr_gamma II.                                 (4)

The coefficients are real constants, norms are signed, and II is Levi-Civita second fundamental form of the independent ambient metric. This is NOT augmented torsion T. No other defect term carrying ambient normal metric derivatives is included in this class.

At fixed s choose smooth compactly supported ambient variations h whose full tensor value vanishes along X. Their symmetric tangential normal derivatives J_Aij=(nabla_nA h)_ij are arbitrary. Such variations exist in tubular coordinates with a cutoff. Tangential derivatives of the zero restriction vanish. The connection variation formula gives

    delta gamma=delta mu=0,
    delta II^A_ij=-(1/2)G_N^{AB}J_Bij,
    delta S_b=-(1/2)int_X M^{ijA}J_Aij mu_gamma,
    M^{ijA}=alpha II^{ijA}+beta gamma^{ij}H^A.        (5)

Neither induced inverse metric nor normal metric varies on X for these test variations. Requiring stationarity for all normal jets forces M=0. Trace gives (alpha+4beta)H=0 and the exhaustive coefficient cases are:

| Coefficients | Necessary condition | Receiver rank |
|---|---|---|
| alpha nonzero, alpha+4beta nonzero | II=0 | 0 |
| alpha nonzero, alpha+4beta=0 | II=gamma H/4 | at most1 |
| alpha=0, beta nonzero | H=0 | at most9 |
| alpha=beta=0 | no restriction from this test | at most10 |

Consequently rank10 requires alpha=beta=0 in the UNCANCELLED class(4). The proof uses all independent jets, not a potentially zero indefinite norm. The probe evaluates the complete jet-to-variation coefficient on K2521's explicit basis and the trace/traceless coefficient cases.

Generic defect localization and normal derivatives of delta distributions were already established in [the full-source moving-section analysis](../k77-wave2-full-source-action-defect-localization-moving-section-ward-bv-2026-08-05.md). Here the new consumer is the explicit quadratic bending moment and its receiver-rank obstruction. An intrinsic addition vanishes on these test variations and cannot cancel it. Nor can a smooth bulk Euler density cancel a nonzero normal delta derivative: the distributions have distinct support/order. Replacing the previously stationary bulk by another smooth nonstationary bulk alone is therefore not a repair. Matching normal-jet defect terms, a nonsmooth/interface or smeared completion, or restricted variation spaces are different candidates requiring their own full variation.

## 4. Essential counterconstruction: retain ambient curvature

The signed Gauss identity is

    R_gamma=R_tan+||H||²-||II||².                    (6)

For the variations in(5), intrinsic gamma is unchanged everywhere on X, so delta R_gamma=0. Therefore delta R_tan=delta||II||²-delta||H||². Written in ambient/extrinsic terms, the intrinsic EH action includes precisely the curvature contribution that cancels the apparent bending moment. Dropping R_tan falsely extends the obstruction to intrinsic gravity. The graph has a nonzero II and H, so this is a nonvacuous cancellation, not a zero-geometry exception.

This counterroute narrows the result and releases the response calculation in section2. It still requires an actual stationary intrinsic geometry and native attribution if GU credit is sought. The next source-facing construction is the true coupled normal-jet coefficient from the selected native action/observation, including the native G(g,s) relation rather than independent G, and its cancellation/field equations. An independent conditional alternative is a genuine Einstein/free embedding plus common-domain response. A chosen graph, ordinary torsion substitution or standalone reciprocal matrix is insufficient.
