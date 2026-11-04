---
title: "K2537 Full reduced quadratic action, source shift and skew constraint"
status: active_research
doc_type: exploration
created: "2026-11-04"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: constant-radial full local linear action decomposition and distributional constraint; no Green inverse or observed Einstein claim
scripts:
  - tests/channel-swings/k2537_reduced_action_decoupling_probe.py
---

# K2537 The full source-preserving Einstein/tensor split

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
result: K2537
carrier: independent ambient fourteen-metric and grade-one End(V) displacement on constant radial stationary Einstein product LAYER=toy CHIRALITY=N/A
pairing: inherited indefinite metric Clifford trace and compact-support formal differential adjoint ON=declared_carrier
real_structure: real signature (7,7), nonzero real kappa, no positive-definite replacement
grading: symmetric tensor, skew two-form, Clifford grade, gauge and differential constraint remain distinct
action_owner: repository-construction -- selected comm/symi/symi I1 completion with moving soldering
target: full curvature-dependent quadratic operator and conserved metric-source response MAP-TYPE=evaluation
```

## Result and scope

[K2535](k2535-reduced-response-symbol-2026-11-04.md)'s301-field system can be transformed exactly, including lower-order curvature, into a105-field cosmological Einstein sector and a196-field tensor sector. The change is algebraic and invertible. It also transforms the source: both sectors remain forced, and the original metric readout contains both. No conclusion that observed gravity is Einstein follows.

The tensor algebraic Hessian has three nonzero eigenvalues at the actual radial amplitude. Combining its skew eigenvalue with the previously owned derivative formula gives a new full distributional equation constraint: the skew two-form must be closed for a metric-only source. It need not vanish and is not diffeomorphism gauge. This settles two lower-order issues left open by the frozen symbol, without mistaking them for a Green theorem.

SC-ACT-01 ASSERTS the first-order action; SC-GEO-55 ASSERTS displacement from gauge-rotated Levi-Civita; SC-GEO-03 ASSERTS Met(X), which this independent ambient metric does not construct. SC-META-53 remains UNCERTAIN about physical indefinite-spectrum treatment. Source polarities and ledger0.263 GR6b/10/11 remain unchanged. All statements use the selected completion, not the printed Upsilon equation in place of its true Hessian.

## 1. Reuse the exact nonsymmetric potential

Use the stationary product with Ric= lambda G,

    a0=-5kappa/2288, lambda=35kappa²/604032,
    Lambda=6lambda, kappa!=0.

In moving coordinates T=a0 Phi_G+Q+e2, K2535 proves the complete grade reduction; e2 is reconstructed, not discarded. Lower Q's internal index and identify it with an endomorphism. Let Q=S+K, S*=S and K*=-K for the metric adjoint; C is S with both indices lowered, so C is a symmetric metric perturbation. The tensor pairing is tr(U*V), not a Euclidean norm.

The full cubic invariant and derivative formula are ALREADY proved in [K2369](k2369-nonsymmetric-native-derivative-2026-10-31.md). Its exclusion on a different fixed geometry is not transported here. Reuse only its coefficient identities:

    L3=4e3(S)+(2/3)trS tr(K²)-(4/3)tr(SK²).

Linearize its exact symmetric and skew Euler tensors at S=a0 I,K=0, then add the kappa mass term. The grade-one algebraic Riesz Hessian is

    H1 Q=(kappa-32a0)Q-16a0 Q*+48a0 tr(Q)I.

Thus

| invariant sector | dimension | Riesz eigenvalue |
|---|---:|---:|
|scalar|1|kappa+624a0=-4kappa/11|
|symmetric tracefree|104|kappa-48a0=158kappa/143|
|skew|91|kappa-16a0=148kappa/143|

This derivation uses the full invariant polynomial, valid for indefinite/nonsemisimple endomorphisms; it does not infer a universal operator from three numerical eigenvectors. Actual native Clifford Hessian pairings check scalar, tracefree, symmetric and skew cases of both signature types. All196 algebraic directions are invertible for kappa!=0. That is neither positivity nor invertibility of the differential tensor operator.

## 2. Identify the FULL curved metric and mixed operators

Define the cosmological Einstein linearization at this Einstein seed by

    E h=delta_h(Ein(G)+Lambda G).

It is formally self-adjoint on compactly supported symmetric tensors with the inherited metric pairing. Covariant derivative order remains as in the Levi-Civita variation. In particular

    E h=delta Ric[h]-(G/2)delta R[h]-lambda h,
    delta R= nabla_i nabla_j h^ij - Box(tr h)-lambda tr h.

Here delta Ric is the full linearized Ricci tensor, not its flat principal symbol. Retaining it includes the product's nonzero Weyl curvature; the product is Einstein, not a14-dimensional constant-sectional-curvature space. The action identity below is sufficient without commuting derivatives or importing a maximally symmetric formula.

K2533's exact radial density for ANY metric is12a R+1456a³+7kappa a². At a0,

    1456a0³+7kappa a0²=-24a0 Lambda,

so this density equals12a0(R-2Lambda). Its quadratic metric action at a stationary seed is -6a0<h,E h> in covariant-metric coordinates.

The full linear-in-Q action is also fixed, not guessed: its grade-one Euler at Q=0 is

    -2Ein(G)+(kappa a0+312a0²)G
       =-2(Ein(G)+Lambda G),

since kappa a0+312a0²=-12lambda. It pairs only with C. At the stationary seed the coefficient vanishes, so variations of density, pairing or moving coordinates multiplying that coefficient vanish in the MIXED second variation. The exact mixed term is -2<C,E h>. Antisymmetric Q has none.

K2533 supplies the parallel nondegenerate grade-two even Hessian A2 and actual first-order B; K2535 supplies full grade preservation including curvature. With no even source,

    e2=-A2^-1 BQ,
    T_op=H1-B! A2^-1 B.

The exclamation mark means formal adjoint with this pairing, including the derivative sign. The complete reduced quadratic action with metric source j is therefore

    S2=-6a0<h,E h>-2<C,E h>
       +(1/2)<Q,H1 Q>-(1/2)<BQ,A2^-1 BQ>-<j,h>.       (1)

All integrals are local compact-support pairings (or a boundary convention making the same adjoints valid). No boundary condition or inverse is selected by writing(1).

## 3. Execute the exact field and source change

Let P:Q -> C be symmetrization/lowering, with adjoint P! for the stated pairings, and put

    z=h+C/(6a0), h=z-C/(6a0).

Because a0 is a nonzero constant, this is a smooth derivative-free invertible field change. Completing the action gives

    S2=-6a0<z,E z>+(1/2)<Q,L_Q Q>
       -<j,z>+<j,PQ>/(6a0),
    L_Q=H1-B! A2^-1 B+(1/(3a0))P! E P.              (2)

The two equations and ORIGINAL readout are

    E z=-j/(12a0),
    L_Q Q=-P!j/(6a0),
    h=z-PQ/(6a0), e2=-A2^-1 BQ.                   (3)

Discarding the second source changes the problem. If compatible inverses G_E and G_Q are eventually supplied on common domains, the formal metric response would be

    h= -G_E j/(12a0)+(1/(36a0²))P G_Q P! j,        (4)

plus allowed homogeneous data. Formula(4) is CONDITIONAL on both inverses and their boundary/source/readout domains; it is not a constructed Green response. The tensor term is not known to be small or absent.

The probe independently differentiates K2529's actual four-coordinate action BEFORE imposing seed relations, implements this shift, and verifies mixed-block removal and equality of the original forced response. Its contrary control drops the transformed tensor source and changes the first-factor readout. Thus the source warning has an actual action-level witness, not just an abstract block identity.

## 4. Execute the skew constraint, including distributions

K2369's full derivative Euler has

    (BQ)_i;jk=2(nabla_j S_ik-nabla_k S_ij)
               +G_ik q_j-G_ij q_k,
    q_j=nabla^l Q_lj-nabla_j tr Q.

Use its actual inherited coefficient convention; pairing coordinates may insert their Riesz factors, but never change the following factorization. On skew variations K,

    B K=J div K,

where J is the parallel algebraic metric insertion. No exterior-three-form or traceless-hook derivative receiver survives. This is an existing universal identity; the new probe checks the actual antisymmetrized coefficient on EVERY grade-two receiver of a transverse skew fixture, with a nonzero longitudinal fixture as positive control.

Neither E-mixing nor a pure metric source couples to the skew part. Variation of(2) on K thus gives

    m_K K-(div)! W=0,
    m_K=148kappa/143 !=0,
    W=J! A2^-1 BQ.                                (5)

Depending on whether the two-form pairing includes1/2, (div)! is -d or -d/2; it is always an exterior derivative times the fixed nonzero convention factor. Applying d to(5) therefore proves

    dK=0.                                        (6)

This is exact on the curved product: d²=0 holds independently of curvature. All coefficients are smooth and m_K constant, so the argument applies to distributions. Locally on a contractible coordinate chart K=dW0 for a distributional one-form W0; globally closed need not be exact. This parameterization is not a gauge identification. A nonzero exact two-form is a contrary control to the inference K=0. Equation(6) remains only one necessary constraint; it does not solve the symmetric/tensor system or guarantee an inverse.

## 5. Gauge, symbols and domain consequences

Since Q0=0 is a tensor in moving coordinates, linear diffeomorphisms act by delta Q=Lie_v Q0=0 and delta z=Lie_v G0. All14 known metric diffeomorphism columns are isolated in the Einstein sector. The tensor symbol radicals are not those gauge directions.

Congruence preserves K2535's already computed301-field ranks. Subtracting the Einstein symbol ranks91 nonnull/14 null gives tensor principal ranks117/26, with radicals79/170. These are reused rank consequences of(2), not a new census, physical mode count or characteristic quotient. The nonzero algebraic masses and(6) demonstrate why the principal radical cannot simply be deleted or declared gauge; full constraints remain to be analyzed.

The algebraic field change preserves common local Sobolev classes of(h,Q) and acts on distributions. Reconstructing e2 differentiates Q and may lower its regularity, so common regularity of all ORIGINAL fields needs a separate check. The codimension7 partial-width source and codimension10 thin source from K2531/K2533 retain their exact regularity burdens. Even an Einstein sector inverse in indefinite ambient signature would not specify the tensor inverse, boundary realization or physical four-dimensional pullback. A common source domain, source conservation, allowed homogeneous data and component-specific readout restriction are still required.

## 6. Execute the explicit tensor kinetic and full trace consumer

The remaining inverse A2^-1 can itself be removed from the action. The grade-two carrier V* tensor Lambda²V* splits into the exterior-three-form(364), metric-trace-vector(14), and traceless-hook(896) sectors. The metric-contraction algebra preserves these three inequivalent multiplicity-one orthogonal-group modules. There is no unpaired epsilon at this rank. Thus the parallel O(7,7)-equivariant A2 acts by one scalar on each; indefinite signature does not justify replacing their pairings by Euclidean ones. Direct native Clifford Hessian and mass-pairing fixtures give

    m_V=503kappa/858,
    m_3=394kappa/429,
    m_H=893kappa/858.

The report checks vector, three-form and hook fixtures with native squared pairings -13,-3,-6 and Hessians -503/66,-394/143,-893/143 at kappa=1. These fix the three universal coefficients using the decomposition, rather than claiming all fields were tested independently. The fixture BQ for a pure trace jet also checks the actual formal-adjoint normalization against the native coefficient.

Write tau=tr C, v=div C-d tau, k=div K, and denote the tensor in the derivative formula of section4 by DQ (to distinguish it from the Einstein operator E). Contracting its first and last indices yields

    w=11v+13k,
    (DQ)_V=Jw/13,
    (DQ)_H=DQ-Jw/13.

Total alternation of DQ vanishes, since C is symmetric and J is a metric insertion. Its hook part depends only on C, because subtracting Jw/13 cancels the entire k term. The vector and hook are orthogonal with

    |Jw/13|²=|w|²/13.

Here tensor |D|² means (1/2)D_ijk D^ijk and may be negative; |w|² is also indefinite. The native grade-two Clifford pairing is MINUS this tensor pairing. Consequently the exact eliminated kinetic density in(1)/(2) is

    -(1/2)<BQ,A2^-1 BQ>
       = (429/kappa)[ |w|²/6539+|(DQ)_H|²/893 ].    (7)

This makes L_Q fully explicit in covariant first derivatives, mass terms and the actual cosmological Einstein operator. Curvature is retained when varying and integrating these covariant derivatives; no flat commuting-derivative replacement has occurred. The squared notation supplies no positivity statement.

Now vary the FULL tensor action by delta C=phi G, with all other components unrestricted. It gives delta tau=14phi, delta v=-13dphi, delta w=-143dphi, and delta(DQ)_H=0. The trace of the mass term is m_0 tau. Also

    tr(E C)=-6u+6lambda tau,
    u= nabla_i nabla_j C^ij-Box tau,
    div w=11u,

where div div K=0 exactly by the codifferential-squared identity (equivalently contracted Ricci symmetry). Therefore the trace of ALL tensor Euler equations is

    (m_0+2lambda/a0)tau +(121/m_V-2/a0)u
       =-tr(j)/(6a0),

or at the actual seed,

    -(5kappa/12)tau +[2820818/(2515kappa)]u
       =[1144/(15kappa)]tr(j).                    (8)

This holds distributionally and eliminates K from a genuine full equation. It does NOT restrict C to a pure-trace ansatz or assert that(8) suffices to solve the remaining rows. For a parallel-field control u=0, it gives tau=-4576 tr(j)/(25kappa²). The probe independently reproduces that exact value from the shifted, fully differentiated K2529 homogeneous action with a first-factor source. Its general projection fixtures check alternation, trace and orthogonality; universal completeness follows from the written invariant formulas.

Equations(6)--(8) are useful lower-order and scalar constraints on the full source problem. The remaining symmetric traceless equations and their covariant divergence still determine whether a chosen distributional source admits a compatible response. The source/readout and boundary problem has not been solved by the explicit kinetic coefficients.

## Evidence and next calculation

New evidence is the actual-amplitude irreducible mass evaluation, complete curved action/source split, its original-action forced-response control distributional skew constraint, explicit vector/hook kinetic density and full traced source equation. K2369's invariant potential/derivative, K2533's even inverse and K2535's grade reduction and principal census are reused explicitly. The probe checks exact native coefficients and algebraic identities; the universal variation/adjoint/exterior-derivative argument bears the full claim. No external-expert, proof-assistant, physical positivity or novelty certification is made.

The response question is now a sourced cosmological Einstein equation PLUS one explicit tensor operator L_Q with dK=0. A useful successor must construct its remaining symmetric-divergence constraints and a common distributional boundary realization, or find a concrete source obstruction there. A frozen-rank census or setting Q=0 no longer answers that question. The original metric readout still demands both forced sectors.
