---
title: "K2533 Mixed top symbol and radial localized-source obstruction"
status: active_research
doc_type: exploration
created: "2026-11-04"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: selected-action ordinary top symbol and radial-only response theorem; no full Green inverse or native GU exclusion
scripts:
  - tests/channel-swings/k2533_mixed_source_response_probe.py
---

# K2533 Mixed top symbol and radial localized-source obstruction

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
result: K2533
carrier: radial K2519 stationary independent ambient fourteen-metric and full real Cl(7,7) displacement one-form LAYER=toy CHIRALITY=N/A
pairing: scalar Clifford trace Hodge and compact covariant-metric test pairing ON=declared_carrier
real_structure: real signature (7,7), nonzero real kappa, real distributional linear perturbations
grading: Clifford grade, ordinary differential order, mixed-order characteristic and physical quotient are distinct
action_owner: repository-construction -- selected comm/symi/symi I1 completion with moving soldering
target: actual order-two metric-displacement coupling and localized metric source compatibility MAP-TYPE=evaluation
```

## Result and scope

[K2529](k2529-native-displacement-response-2026-11-04.md) gives an invertible four-coordinate homogeneous Hessian, and [K2531](k2531-partial-thickness-source-2026-11-04.md) gives a conserved codimension7 partial-width source. Neither supplies a full field response. This note constructs the ACTUAL highest ordinary order-two symbol at the radial stationary product, then tests a necessary sourced subproblem. Its nonnull/null ranks are182/28. The radial-only response class cannot answer either the thin or partial-width metric source when the independent translation source is zero. Anisotropic/mixed-grade responses remain open.

SC-ACT-01 ASSERTS the first-order action and SC-GEO-55 ASSERTS displacement from gauge-rotated Levi-Civita. SC-GEO-03 ASSERTS Met(X); this independent-ambient completion is not that identification. SC-META-53 remains UNCERTAIN. Selected Shiab, Clifford convention and independent metric are repository choices. Ledger0.263 GR6b/10/11 and source/canon status are unchanged. Ordinary top-symbol degeneracy is not a physical ghost, a complete characteristic variety or a GU falsification.

## 1. Actual independent-coordinate order

Use K2519's selected local functional, with compactly supported variations,

    I1=int[P(T,S(F_B))+(1/2)P(T,S(D_B T))
             +(1/3)P(T,S(T wedge T))+(kappa/2)P(T,*T)]. (1)

B is the genuine Levi-Civita spin connection of independent G; the soldering, S, Hodge and volume move with G. Use a local algebraic identification of Clifford bundles under metric changes. Gauge-rotated descriptions transform simultaneously; no independently varying source-varpi/epsilon jet is silently identified with T. The completion's conjugation equation is retained through its natural symmetry/translation relation, as in K2519; no physical gauge quotient is constructed here.

In these coordinates F_B is affine in second metric derivatives, with coefficients algebraic in G. The curvature term is linear in T. Integrating its second-G-derivative terms once transfers a derivative to an algebraic function of G,T and leaves a first-jet density. D_B T contains first T and first G derivatives; its term is linear in those derivatives, while the other terms are algebraic. Therefore the full Euler linearization has ordinary order at most2; the TT block has order at most1. All potential and moving-pairing terms remain at lower order. Boundary equivalence uses compact support and is not a boundary-condition theorem.

This is sharper in DIFFERENT coordinates than the older [source-coordinate bulk audit](selected-k77-bulk-operator-admission-2026-08-09.md), which retained safe4/3/2 bounds after derivative-dependent B(g,epsilon) substitution. No contradiction or universal coordinate-invariant order claim follows.

## 2. The complete ordinary order-two block at the radial seed

At a0=-5kappa/2288, write the grade-one endomorphism in the moving soldered frame as A=a0 I+C. Let C_sym denote its G-selfadjoint part, expressed as a covariant symmetric tensor using background G. The Riemann/Clifford identity reused from K2357/K2519 gives the exact curvature density

    (tr A)R-2tr(A Ric)=12a0 R-2<C,Einstein>.             (2)

Only symmetric grade-one T couples to Riemann curvature: S(F_B) is grade1 and selfadjoint, so other Clifford grades and antisymmetric C pair to zero for every G. This statement includes derivatives under moving identification, not just a frozen coefficient evaluation. The derivative term in (1) contributes at most ordinary order1 to the linearized Euler equations; the potential contributes order0.

With covariant metric variation h, suppressing lower-order curvature terms, define E(xi) as the linearized Einstein tensor with formal derivatives replaced by the real covector xi (no Fourier i). If v_j=xi^i h_ij, q=xi^i xi_i, t=tr_G h, then

    E(xi)h_ij=(xi_i v_j+xi_j v_i-q h_ij-xi_i xi_j t
                   -G_ij(xi^k v_k-q t))/2.            (3)

Metric variation of the Einstein-Hilbert density with respect to covariant G has coefficient -Einstein. Thus on (h,C_sym) the order-two Hessian operator is

    L2(xi)=[[-12a0 E(xi), -2E(xi)],
             [ -2E(xi),       0   ]].                 (4)

Indices/pairing on C are raised with background G. The scalar2x2 coefficient matrix has determinant-4. Remaining field coordinates have zero order-two rows/columns. The finite probe checks self-adjointness with the symmetric-tensor pairing weights G^ii G^jj times2 off diagonal, not ordinary coordinate transpose.

This is the full HIGHEST ORDINARY order-two symbol of the declared completion. It is NOT the full mixed-order symbol: its zero TT order-two block can have essential first-order equations. Treating those zero rows as physical gauge or discarded fields would change the system.

## 3. Universal rank and the actual null conormal

For q!=0, h=xi tensor w+w tensor xi is a14-dimensional gauge kernel. Choose an orthogonal splitting along xi. On the13-dimensional transverse space, E is a nonzero scalar times trace reversal h_perp-G_perp tr(h_perp). Its trace eigenvalue1-13 is nonzero. Hence rank E=dim Sym²(R13)=91 and its kernel is exactly the gauge image.

For xi nonzero and q=0, (3) depends only on (v,t). The map h ->(v,t) is surjective onto a15-dimensional space: in a null basis, the row contracted by xi supplies arbitrary v, while one transverse diagonal entry independently adjusts t. Its kernel after applying E is exactly v=c xi, t=2c. Indeed the transverse-transverse equations first force xi dot v=0; a complementary null vector and transverse directions then force v proportional to xi; the remaining xi-xi equation fixes t. Thus rank E=15-1=14. This holds for every nonzero null covector, not only one representative. The exact probe checks all105 symmetric basis columns for positive, negative and null representatives and independently tests Bianchi/gauge identities. It also rejects the Ricci-only altered symbol by a nonzero original Bianchi contraction.

Since the2x2 factor in(4) is invertible, ranks L2 are182 nonnull and28 null. In K2531's second-factor normal space W of signature(3,4), nonzero null conormals actually exist. A positive Euclidean covector norm cannot replace this geometry to justify an elliptic inverse. The rank calculation alone does NOT prove those covectors characteristic for a completed mixed-order gauge-fixed system; first-order constraints may change that question. It rules out importing a uniformly elliptic inverse from(4).

## 4. Execute the radial sourced subproblem before a full inverse

The source has j_T=0 in these independent coordinates. Restrict the RESPONSE, not just the source, to radial soldering T=a Phi for arbitrary metric. The exact restricted density is

    L_rad=12a R+1456a³+7kappa a².                      (5)

Its derivative term vanishes by Clifford parity. But varying only (5) would miss transverse T equations. Reuse [K2357](k2357-curved-native-stationarity-2026-10-31.md)'s FULL even translation equation J(da)=0 with injective algebraic J, and full odd equation

    -2Einstein+(kappa a+312a²)G=0.                     (6)

On a connected chart the former forces a constant. The covariant-metric Euler tensor of(5), including derivative-of-a terms before imposing constancy, becomes

    -12a Einstein+(1456a³+7kappa a²)G/2
       =c(a)G on(6),
    c(a)=-a²(5kappa/2+1144a).                         (7)

Along E_T=0, the extra moving-soldering chain term E_T[delta T] is zero. Thus (7) is the independent fixed-T metric equation on this solution set, not a falsely frozen soldering variation.

Linearize at the radial joint seed, with delta T=a0 delta Phi+alpha Phi. The zero translation source gives d alpha=0. The derivative of J times da0 vanishes, so the conclusion extends to distributions: a smooth algebraic left inverse of J forces the distributional derivative of alpha to vanish. Distributional constants on a connected chart are ordinary constants. Since c(a0)=0,

    j_G=c'(a0)alpha G0, c'(a0)=-25kappa²/4576.          (8)

The metric-covector normalization is the one in delta I=int <E_G,h>; changing the source convention rescales both sides and does not change support. Equation(8) is smooth with full support unless zero. K2529's nonzero thin covector and K2531's nonzero partial-width stress are supported on positive-codimension sets and cannot equal it. Testing away from the support first forces alpha=0; testing a nonzero tangent source then gives a contradiction.

This excludes radial-only linear responses to these specified j_T=0 sources. It does not exclude arbitrary anisotropic/mixed-grade responses or source actions that also couple to T. The homogeneous four-coordinate Hessian permits nonradial displacement responses, so its invertibility and (8) are compatible. Conservation is necessary but insufficient for a radial response.

## 5. Released domain and readout demands

For K2531's fixed-width j=f(u)delta(v), v in R7, its proven H^(-s) threshold is s>7/2. Since the present COMPLETE independent-coordinate system has ordinary order at most2 with smooth coefficients, a solution with EVERY component in common H^r_loc must satisfy

    r < -3/2; the original codimension10 thin source requires r < -3. (9)

This follows from L:H^r_loc -> H^(r-2)_loc and the source threshold. It is a necessary common-component bound, not existence, elliptic gain or the maximal regularity of h alone. For example a two-component system can place a singularity entirely in one component while the observed component is zero; (9) cannot assign that singularity to the readout.

The generic codimension10 isotropic Sobolev trace on X requires r>5. That sufficient route cannot be obtained merely from a common regularity class satisfying(9). More specific component regularity or a microlocal restriction can still exist. The standard distributional pullback criterion requires the actual response's wavefront to avoid the observer conormal; see [the pullback discussion in the primary conormal-distribution analysis, section4.6](https://doi.org/10.1007/s11868-024-00617-y). Failure to verify a sufficient criterion is not proof that a particular pullback is impossible. Source wavefront is not automatically response wavefront, nor does a symbol rank decide it.

## 6. Execute the available first-order port

The first-order TT coefficient is NOT missing. [K132's all-grade analysis](selected-k132-native-i1b-t0-all-grade-noether-complex-2026-08-16.md) already computes it in the same real Cl(7,7), selected comm/symi/symi convention. Its first-order density is quadratic in T, so the TT principal coefficient is independent of background T and curvature. In a covariantly normal moving frame it transports pointwise to the current stationary product; derivatives of frame/coefficients contribute lower-order terms. The actual Euler coefficient is the antisymmetrized raw pairing, C1(xi)=(raw(xi)-raw(xi)^T)/2, including the integration-by-parts sign.

The reused full229376-carrier ranks are130912 for either nonnull causal type and122746 for nonzero null xi, with grade chains

    0--3--4--7--8--11--12,
    1--2--5--6--9--10--13--14.

These are K132's TT ranks only. Its coupled ten-metric ranks, zero-background Noether images and functional boundary realization are not transported into this105-metric stationary-product problem. No rank is newly recomputed for that huge bank. A cheap direct native-backend check gives the two radial pairings2 and24 and Euler coefficient(2-24)/2=-11, matching K2357. Omitting the formal adjoint gives1 and fails the normalization. The port is justified by the derivative coefficient's background independence, not by matching ranks alone.

## 7. Execute the actual even auxiliary test at the NEW amplitude

The first-order term changes internal parity. Write T=O+E for odd/even internal Clifford parity. At O0=a0 Phi and E0=0 the even-even block has no derivative term. Its algebraic Hessian A0 comes from the mass and cubic potential; curvature is linear in T. The old [full-parent Hessian](selected-k77-nonzero-branch-parent-hessian-2026-08-10.md) used a_old=-kappa/312. Our amplitude is a0/a_old=15/22, so

    H_new=(7/22)kappa M+(15/22)H_old.                  (10)

Old full rank does not imply new full rank because M is indefinite. We actually evaluate the new even blocks, using the inherited complete invariant-label proof and its exact coefficient functions, not its old pass total.

For a basis e^i tensor gamma_J, the algebraic mass/cubic Hessian preserves Clifford grade and the label J xor{i}. The cubic coefficient support property is independent of its scalar amplitude, so its previous proof applies unchanged; the mass is diagonal. For the third cubic polarization, P(Phi,S(U2)) is a Spin-invariant scalar functional on exterior-two forms tensored with Clifford forms. Its grade bound excludes the Hodge-complement grade12 channel, leaving the grade2 contraction. A grade2 component of the Clifford commutator [gamma_J,gamma_K] requires equal input grades: the possible grade-difference2 product commutes and cancels. The contracted two-form indices i,j require J xor K={i,j}, hence J xor{i}=K xor{j}. This proves grade/label preservation for that third term; the q-image support covers the other two terms. Off-label finite samples alone would not prove completeness. A fixed grade g and label size g-1 or g+1 has at most14 basis states. Signed permutations within the seven positive and seven negative axes reduce every label to its size and positive count. The multiplicity is binomial(7,p)binomial(7,size-p). The new probe constructs every even-grade signature representative at a0=-5/2288, kappa=1, checks the q-image support and symmetric entries, and computes each exact rational rank and determinant. Multiplicity-weighted dimensions exhaust the carrier:

| Even grade | Dimension | New rank |
|---|---:|---:|
|0|14|14|
|2|1274|1274|
|4|14014|14014|
|6|42042|42042|
|8|42042|42042|
|10|14014|14014|
|12|1274|1274|
|14|14|14|
|Total|114688|114688|

Thus A0 is pointwise invertible for every kappa!=0, since the normalized matrix scales by kappa. This is a new amplitude-specific exact census, not a sample, inference from old rank or positive-energy assertion. The report stores every orbit, multiplicity and determinant; the old full-bank runner is not recursively executed. Reused code functions and coefficient backend are pinned by hash.

## 8. Released moving-geometry Schur reduction

Use the local algebraic moving coordinates O=a0 Phi_G+Q. For Q=0, the even Euler forcing vanishes for EVERY G: a0 is constant, D_B Phi_G=0, the derivative forcing J(da0) is zero, and the algebraic/curvature parity contributes only odd Euler components. Its derivative with respect to G is therefore zero, rather than an omitted mixed term.

At the stationary seed the complete linearized even equation is

    A0 e+B Q=j_even,

where B is the actual covariant first-order odd-to-even operator, with its coefficient supplied by section6. For our metric-only source j_even=0, e=-A0^-1 BQ. Substitution in the quadratic action gives the reduced odd contribution

    -(1/2)<BQ,A0^-1 BQ>,
    L_odd,eff=L_odd,algebraic-B! A0^-1 B.              (11)

Here B! is the formal adjoint with the actual indefinite trace/Hodge pairing and compact-support integration. A0 and its inverse are covariantly parallel at the radial seed. This is exact local linearized elimination of all even auxiliary fields; it does not drop them or infer positive energy. The metric--odd curvature block(4), pure metric Einstein block and odd algebraic potential remain. If an even source is introduced, its effective source and quadratic contact term must be retained; the present source has none.

This materially improves the next response problem: the first-order coefficient and algebraic even inverse are now owned, and the remaining local operator is a second-order system on105 metric plus114688 odd coordinates. It is not legitimate to replace B!A0^-1B with a positive Gram form, equate its rank with rank B, or restrict to grades1/2 merely because curvature couples to grade1. The existing grade chains expose the omitted paths. A separate domain/covector analysis must combine this complete reduced symbol and lower-order terms with diffeomorphism constraints, source, boundary conditions and observed pullback. We do not report a full Green solution from the Schur identity or infer all characteristic cones from the earlier ordinary top block.

## Evidence and frontier

Exact finite symbol matrices, radial algebra, new complete even-amplitude census and contrary controls accompany the universal order/rank/source-support and local Schur arguments. The old injectivity, stationary seed and source regularity are reused with explicit pointers; their earlier checks are not recounted as new results. No source claim, physical quotient, full Green inverse, native Met(X) bridge, external-expert review or novelty is established. The ordinary symbol, radial source theorem, transported first-order coefficient and actual even inverse now make the remaining odd-metric/source-readout construction more precise, while K2532 independently tests a physical observation configuration.
