---
title: "Joint Lorentz-gauge symmetry and source-current compatibility"
status: exploration
doc_type: structural-result
created: '2026-11-13'
program_target: X-P1-P2
tier: T2
expected_delta: Test complete source-category membership without discarding independent fields or changing observation silently
actual_delta: "Constrained - complete odd-adapter symmetry ranks and held-current stabilizer"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
bears_on: [SC-OP-04, SC-OP-05]
canon_verdict_change: none
---

# Joint Lorentz-gauge symmetry and source-current compatibility

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Its result binds only the
> named model and does not adjudicate Weinstein's source-native mechanism
> without a typed bridge. Read `lab/methods/source-native-comparator-routing.md`
> and follow its source-native pointers. Classification: `INTERNAL_STRUCTURAL_ONLY`.

program_target: X-P1-P2
tier: T2
expected_delta: Joint symmetry, independently fixed current and actual-normal geometry tests
actual_delta: Constrained - complete odd-adapter symmetry ranks and held-current stabilizer

```gu-typed-objects
result: Joint Lorentz-gauge symmetry and source-current compatibility
carrier: full complex Dirac scalar S128 and independent full one-form spinor; no physical family count LAYER=ambient+observed BRIDGE=literal-section-plus-gamma-trace CHIRALITY=S-FULL-DIRAC
pairing: independent nondegenerate density-dual rows and explicitly held versus transported current vertices ON=declared_carrier
real_structure: complex Clifford identities; K77 real and K95 quaternionic structures separately typed; no signature transfer inferred
grading: ambient chirality versus horizontal and normal grades; no physical chirality identification
action_owner: repository-construction -- structural comparison of source-print ingredients; no selected full action
target: joint symmetry and current compatibility MAP-TYPE=intertwiner
```

The symmetry test and fixed-current test answer different questions. On the
full rank128 complex scalar carrier, Lorentz plus full Standard Model symmetry
allows odd adapters only on rank8 sterile support. Color plus electromagnetism
admits full-rank adapters, but those still fail the tested nondegenerate standard spin-action
cross-current in the same literal field coordinates. Exact transport of fields,
bars, density and observations remains a viable comparison category. None of
these conditional exclusions falsifies the source's effective 2+1 mechanism.

## Part I. Full symmetry classification

### 0. Custody, scope, actual delta

Source objects: full complex S of rank128 from eq9.16; independent bars; normal-spinor quantum numbers (SC-FER-07); geometric normal action, not independent internal symmetry (SC-GRP-06); the normal compact Pati–Salam and SM intersection (SC-GRP-03). Parent remains U(64,64) per SC-GRP-02/GEO-51, not an unconditional quaternionic group. This test applies after a fixed Spin reduction and section split, not to all parent transformations with their tensors held fixed. Source current is the literal9.18 alphabet plus its as-yet unspecified typed contractions, not an invented standard current.

Source constraints loaded: the full relevant records in `lab/sources/source-claim-register.yaml`; section9 extraction; full November13 notes; June Pati–Salam exact branching (ONLY its branching, not its obsolete real/complex dimension paragraph); August30 paired-real Spin(6,4) theorem; HE1's explicit no-count and 144/imposter fences; August13 horizontal conjugation result. SC-CHI-04/52 assert effective low-gravity/low-mass behavior, not exact unbroken-SM symmetry of every frozen background. Consequently the full-SM no-invertible result is not a source-effective-chirality kill. Color×EM provides a complete positive successor, not a hypothetical escape.

New delta beyond the weak-only note: every complex-linear odd endomorphism is classified by the exact normal branching. PS rank0; SM maximal rank8/128, not merely no invariant vector; color×EM full-rank family with dimension40 and a simple Clifford-vector witness. Real/antilinear maps, automorphism twists and background transport are separate categories. Thus weak-only positive normal6 selection does not suffice for full observed gauge symmetry, while electroweak reduction repairs the obstruction without breaking horizontal Lorentz or color.

### 1. Category and universal completeness theorem

Fix the connected real horizontal Lorentz spin group L=Spin+(1,3), normal compact subgroup G, and the complex representation

    S = (H_L ⊕ H_R) ⊗ (F ⊕ Fbar),
    dim_C H_L = dim_C H_R = 2, dim_C F = dim_C Fbar =16,
    Ω = χ_H χ_N.

This is the complex Dirac restriction from the 4+10 split. H_L,H_R are inequivalent complex representations of the connected real Lorentz group. F and Fbar are normal chiral modules, with the source's verified table as F. We classify A:S→S with

    A Ω = −Ω A,   A ρ(l,g)=ρ(l,g) A,

for all (l,g), and ask for invertibility. No claim that Ω is an observed physical chirality is used. The operator is a scalar-slot tensor, not a form-degree mixing map or derivative-dependent map. Pure normal Clifford c_N(v) is represented in ambient Cl(H⊕N) with the usual horizontal chirality factor; this does not alter the commutant/rank counts.

Schur's lemma for L gives every complex-linear commuting A as

    A = P_L⊗a_L + P_R⊗a_R.

Since it preserves χ_H, oddness is exactly normal oddness. Therefore

    End^-_{L×G}(S)
      = [Hom_G(F,Fbar) ⊕ Hom_G(Fbar,F)]^{⊕2}.

Write multiplicities m_+(r),m_−(r) for each G-irrep r in F,Fbar. Then

    dim_C End^- = 4 Σ_r m_+(r)m_−(r),
    max rank_C A = 8 Σ_r dim(r) min(m_+(r),m_−(r)).

The rank formula uses four independent directed normal maps and horizontal dimension2; it is attained by maximal-rank rectangular maps in every common isotypic block. Invertibility holds iff m_+(r)=m_−(r) for every r, i.e. F|G ≅ Fbar|G. This is necessary AND sufficient and covers arbitrary Clifford tensors: complex Cl14 is End(S), and its odd subspace is exactly the Ω-odd endomorphisms. Higher exterior Clifford degrees cannot evade a theorem about all of End^-(S).

For unequal additional multiplicities the same formula applies after replacing m by actual representation multiplicities. Repeating the same F/Fbar pattern k times does not remove absent charged irreps: the SM maximum becomes8k on128k, although the Hom parameter dimension scales as4k². Those k's are supplied representation multiplicities, never derived physical families. More general changed carrier multiplicities or opposite charge blocks are a changed-carrier repair with an exact matching requirement, not a same-carrier loophole.

### 2. PS → SM → color×EM: full commutants and maximal ranks

All counts below include the full rank128 scalar carrier and the two inequivalent Lorentz chiralities. Global finite center quotients do not change these Lie/representation commutants for the stated honest representations.

| Normal group | dim_C full commuting algebra | dim_C odd subspace | max complex rank | minimum nullity |
|---|---:|---:|---:|---:|
| SU4×SU2_L×SU2_R | 8 | 0 | 0 |128|
| SU3×SU2_L×U1_Y |28|4|8|120|
| SU3×U1_EM |80|40|128|0|

#### Pati–Salam

    F=(4,2,1) ⊕ (4bar,1,2),
    Fbar=(4bar,2,1) ⊕ (4,1,2).

The four summands are mutually inequivalent. There are no common irreps and hence no nonzero odd equivariant endomorphisms. This conclusion uses the complete PS action, not only weakSU2. The full commuting algebra consists of eight scalars (four normal irreps times two Lorentz chiralities), all ambient-even.

#### Standard Model

The exact normal16 table, n=6Y:

    Q=(3,2,1), d^c=(3bar,1,2), u^c=(3bar,1,−4),
    L=(1,2,−3), e^c=(1,1,6), n^c=(1,1,0).

Fbar contains the charge-conjugate table. The ONLY common irrep is (1,1,0), multiplicity one each. Color conjugation, weak type and hypercharge distinguish every other row. The kernel of every odd equivariant A therefore contains

    (H_L⊕H_R)⊗(F_charged15 ⊕ Fbar_charged15),

of complex dimension120. Here 'charged15' means nontrivial under at least one SM factor, including the electrically neutral component of the weak lepton doublet. It does not mean every component has nonzero electric charge. On the sterile normal pair, a_L,a_R each have arbitrary off-diagonal2×2 matrices. Four complex coefficients give maximal total rank8, provided both directions on both Lorentz chiralities are nonzero. Each directed ambient-half map S+→S− and S−→S+ then has rank4. Thus the neutral sterile sector permits an odd intertwiner, but only a rank-limited one; no nondegenerate scalar duality or full scalar coordinate change follows.

Full normal commutant: ten nonsterile irreps with multiplicity1 plus the sterile irrep with multiplicity2, dimension10+4=14. Multiply by two Lorentz irreps for28. Its even part has dimension24 and odd part4.

#### Color×electromagnetism

Restrict using Q_EM=T3_L+Y. Both F and Fbar become the SAME representation

    (3,2/3) ⊕ (3,−1/3) ⊕ (3bar,−2/3) ⊕ (3bar,1/3)
      ⊕ (1,−1) ⊕ (1,+1) ⊕ 2(1,0).

There are six charged irreps, each multiplicity1, and one neutral irrep multiplicity2. Thus Hom(F,Fbar) has dimension6+2²=10 and an invertible locus (C*)^6×GL2(C). The complete odd invertible locus on S is FOUR independent copies of this set: both normal directions at each horizontal chirality. It has complex dimension40 and rank128. Full normal Dirac commutant is six M2(C) blocks and one M4(C) block, dimension6·4+16=40; two Lorentz irreps give80. This is a representation statement, with no identification of masses, generations, particles or antiparticles after physical reduction.

This positive result does not require adding vectorlike matter: the full original normal Dirac scalar already has the matching blocks after restriction. It does require selection of the residual group and the intertwiner within that40-parameter open family. Symmetry alone does not select a unique A or make it a source contraction.

#### The source's possible extra reductive U1 must be named

SC-GRP-03 explicitly retains a possible extra U1 when U(3,2), rather than SU(3,2), is used. Under the usual SO10-compatible SU5×U1_X convention, F=10_1⊕5bar_−3⊕1_5 and Fbar has opposite X charges. These X spectra are disjoint. Therefore preserving X forbids EVERY complex-linear normal-odd intertwiner, even on the sterile pair, regardless of further restricting the other factors. The SM rank8 statement assumes that extra factor is absent/broken, as stated in its group.

If a supplied breaking instead leaves color×EM×U1_(B−L), F and Fbar remain equivalent: the two neutral states split into B−L=±1, so Hom dimension becomes8, odd full dimension32, and maximal rank remains128. Which U1 survives is part of the selected reduction; the names 'extra U1' and 'low energy' alone do not determine it. These are exact conditional controls, not selection claims.

### 3. Higher Clifford tensors and explicit positive/negative controls

The SM rank8 possibility is not a vector. Use normal exterior spinors Λ*C5, with the usual SU3×SU2 embedding and C5 hypercharges (−1/3,−1/3,−1/3,+1/2,+1/2). One normal chirality is Λeven, the other Λodd. Vacuum and top wedge are both SU5 singlets (hence SM singlets); a product of all five creation operators maps vacuum→top and annihilates every other state. Its reverse is the five-annihilation operator. They are Clifford degree5 and normal odd, each rank1. Their span realizes exactly the two normal Hom directions. With independent horizontal projectors this realizes all four complex odd commuting coefficients, so the rank8 bound is attained by genuine higher Clifford tensors. Five-form sterile exchange is the relevant conventional126-type channel, but nothing here asserts a standard126 VEV or Yukawa mechanism.

Every metric-only vector, every other odd Clifford tensor, and every sum thereof still obeys the fullSM rank bound. An argument merely showing no invariant vector would have missed this nonzero, singular odd sector; an argument declaring no odd invariant at all would be false.

At color×EM the same exterior model supplies a full-rank SIMPLE vector witness. Let a5†,a5 be creation/annihilation in the fifth mode whose Q_EM is0. Then

    V=a5†+a5, V²=I, {V,χ_N}=0,
    [V,SU3]=0, [V,Q_EM]=0,
    [V,Y]≠0, [V,T_weak^+]≠0.

Multiplying by i supplies the negative-norm Clifford generator with square−I in the real normal weak4 convention (this multiplication changes no commutation test). This is the real neutral direction of the electroweak doublet within normal10. Its fixed subgroup inside the usual SM is precisely color×EM, up to finite centers. It preserves full connected horizontal Lorentz. Thus the frozen odd-adapter algebraic repair has a nonempty colorEM, Lorentz-preserving subclass, for which this witness reduces electroweak symmetry by exactly three generators. No elementary Higgs is introduced: this is a geometric tensor in a specified normal representation. A source-owned connection/curvature/section mechanism must select it if it is to describe the source construction.

The probe checks the exact table, dimensions, five-form ranks, chirality, SU5 invariance, neutral-vector square, color/EM invariance and two failing EW generators. It does not establish a source background, real global section, physical positivity or current.

### 4. Real-linear, antilinear, charge-conjugation and parity categories

The preceding table is for COMPLEX-linear intertwiners. For the actual connected Lorentz real group, conjugation exchanges H_L and H_R. For the normal real Spin(6,4) restriction, conjugation exchanges F and Fbar. Therefore ordinary total charge conjugation flips BOTH factors and is AMBIENT-EVEN. It does not supply the required ambient-odd adapter.

A global antilinear Lorentz-equivariant map sends H_L to H_R and vice versa. For it to be ambient-odd it must preserve the normal chirality label. Its normal intertwiner therefore lies in Hom_G(conj(F),F) or Hom_G(conj(Fbar),Fbar), exactly the same overlap spaces as above. PS gives zero; SM gives only the sterile pair; colorEM gives the full-rank family. A putative 'identity on horizontal spinor tensored with normal charge conjugation' is not a well-defined antilinear operator on the complex tensor product: moving a scalar between tensor factors gives contradictory scalar laws. The horizontal semilinearity must be included.

Any real-linear map uniquely splits into complex-linear and antilinear parts. Since the group is complex-linear and Ω is complex-linear, both pieces of an equivariant odd real-linear map remain individually equivariant and odd. In the SM case BOTH images lie in the same sterile subspace of dimension8 complex (16 real). Adding the pieces cannot escape that support. On the complex S regarded as real256, the maximum real rank is16, with real nullity240. The odd real-linear parameter space has dimension16 real (four complex linear and four complex antilinear parameters). ColorEM has maximum real rank256 and odd real-linear dimension160; PS has zero.

K77 and K95 are not the same reality restriction. A K77 real form fixed by its specified ambient charge conjugation has real dimension128; compatible odd maps have maximum real rank8, real nullity120. A K95 quaternionic ambient structure has C²=−1, not a real fixed subspace; its complex128 carrier has underlying real dimension256. If one requires compatibility with that C as well, impose it on the four coefficient blocks; the sterile support remains dimension8 complex/16 real, so no invertible SM map emerges. The existence and coefficients of a selected global reality-compatible A must be checked with that actual C. The rank exclusion does not depend on choosing a K77 reality convention in K95.

Automorphism twists are genuine OTHER categories:

* A complex-linear normal intertwiner with Aρ(g)=ρ(α(g))A, where α conjugates SU3 and reverses Y (or conjugates SU4 at PS), can exchange F,Fbar invertibly. It is not a commuting intertwiner for the held gauge action. The gauge connection, charges, barred action, current generators and receiver identification must all be pulled through α.
* A complex-linear horizontal parity implementer exchanges H_L,H_R while preserving the normal factor and is ambient-odd/invertible. It implements a Lorentz OUTER automorphism, not an element of the connected Lorentz commutant. A spacetime parity transformation also changes the coordinate/covector action; treating its spin matrix as a constant invariant tensor omits that cost.
* Composing an ambient-even charge conjugation with a gauge or parity twist can give odd semilinear alternatives. They remain twisted representation identifications, not ordinary same-action symmetries. General criterion: compare multiplicities after complex conjugation and/or the explicitly stated group automorphism. Do not infer invertibility from the word 'charge conjugation'.

Enlarging connected Lorentz symmetry to a Pin/parity-invariant theory cannot enlarge the ordinary commutant: it imposes additional constraints (typically matching L/R coefficients). Using parity as an intertwining automorphism is different from commuting with parity and the connected group.

### 5. Exact selection costs and native-metric boundary

| Repair datum/category | What it retains | Exact cost or test |
|---|---|---|
| Fixed PS or SM, same scalar representation | Lorentz and stated normal group | No invertible odd adapter; SM sterile rank8 ceiling |
| Selected v∈positive normal6 | Lorentz and weakSU2_L | Not full color/SM: normal6 has 3+3bar with nonzeroY; stabilizer fixes v, pure color reduces to SU2, pureY is lost (a diagonal U1 can remain) |
| Selected nonnull horizontal v | Normal group | Reduces connected Lorentz to v's little group (timelike Spin3 or spacelike Spin1,2); null v is noninvertible |
| Selected neutral negative-normal weak4 v | Lorentz, color×EM | EW reduction of three generators; actual normal embedding/alignment and nonzero norm required |
| Arbitrary colorEM odd invertible A | Lorentz, color×EM | Four sets of six nonzero complex scalar blocks and one GL2 block; equivalent-representation/gluing data required |
| Normal outer charge twist | Lorentz, transformed normal action | Changes gauge representation/connection/current identification; not same-action invariance |
| Moving spurion A | Covariance of joint fields/background | Transformation law and derivative/connection terms; fixed-background symmetry is stabilizer of A |
| Metric trace datum | Native metric-fibre covariance if actual bridge exists | Need chimeric/actual-normal isometry and its position relative to selected compact/SM reduction; norm−4 alone does not authenticate neutral weak alignment |

Do NOT claim a universal 'metrics cannot supply odd tensors'. In the actual metric fibre Sym²T*X the metric trace is a natural Lorentz scalar and becomes a normal vector only after the required geometric identification. Its earlier norm−4 is relevant and may make c(trace) invertible. On an abstract independently framed H⊕N quadratic split, metric/orientation alone give no selected normal vector; those are different naturality categories. Our complete fullSM commutant says that any supplied invertible odd trace adapter cannot at the same time be a fixed fullSM intertwiner on the stated S. It says nothing against existence of that trace or its covariance under the appropriate diagonal geometric action.

The negative trace failed full weak invariance in the prior fixed compact6+4 reduction. After EW reduction, a negative weak4 vector can indeed be colorEM invariant. Identifying THIS trace with THAT neutral direction requires more than its negative norm: its color6 component must vanish and its weak4 alignment must match the chosen electromagnetic generator. For any nonzero pure weak4 vector, SU2_L×U1_Y acts transitively on its fixed-norm S3; its stabilizer is a conjugate U1_EM and exactly three generators are broken. Thus if the actual normal identification and a compatible compact splitting place the existing trace entirely in weak4, the trace itself supplies the adapter: no second vector need be selected. Selecting that compact splitting and the relative complex/SM embedding is extra embedding data, not extra vector data. A simultaneous change of embedding can supply these conditions but is not already proved source geometry. For an arbitrary negative trace with nonzero positive6 projection, fixed standard color is not retained. A source-owned connection-curvature selection could supply the needed alignment without any conventional scalar potential or any implied vector-boson mass theorem.

### 6. Carry the surviving repair through full operators and weak currents

At a frozen point the prior LDR identities work for every invertible A, not only vectors, provided the scalar/form extension satisfies A1 d=d A0 and the corresponding contraction identity. Taking A1=I_V⊗A0 ensures both exterior identities. The NW and crossed-arrow repairs therefore preserve normalized principal evolution and the six-spinor quotient under the specified scalar coordinate maps. The entire colorEM invertible family is a genuine survivor at that structural level. For general higher A, the prior special identity A²=λI and its scalar-scaled bilinear congruence do NOT automatically hold. Retain exact LDR and independently transport barred factors; do not cite the vector-square simplification for all40 parameters.

If R=diag(I,A^−1) is the scalar coordinate transformation, the transported symmetry is R^−1ρ(t)R. In the scalar block that is Aρ(t)A^−1. Equality with the old held action requires [A,ρ(t)]=0. ColorEM generators pass this representation-covariance test; broken EW generators generically fail. Their transformed vertices must be carried with the appropriate row/column factors. This does NOT mean the held cross-current passes for colorEM: a fixed cross vertex demands rho(t)A=rho(t), not merely [A,rho(t)]=0, and a globally odd invertible A fails that equality on any nonzero graded charged quotient. The independent current.md theorem supplies that sharper result. One cannot transport the equation and then silently hold a printed vertex fixed. The first discriminator is therefore whether the ACTUAL9.18 comparison holds source fields/current fixed or transports their coordinates, after its density/variation ownership is identified. In the transported branch, test a broken weak generator only to decide whether the old held gauge-action identification is retained; it is not an intrinsic obstruction to the transported current, which pulls back exactly.

For a moving background A(x), covariance requires A→ρ(g)Aρ(g)^−1 and

    ∇A=dA+[connection,A].

Frozen commutation with the residual Lie algebra does not imply ∇A=0 for the complete connection. Broken-connection components contribute even for coordinate-constant A. A covariant field redefinition changes the scalar connection and adds A(∇A^−1) (with the precise side determined by field convention). If A is selected as a functional of the source connection/geometry, the source variation also includes δA and variations of its duals/observation. If it is supplied as an independent spurion, the full Ward identity contains its variation; setting the spurion fixed leaves its noninvariant torque term. None can be omitted when comparing the exact source current.

This is not an arbitrary permission to redefine the source current: equality must be checked against a separately authenticated source vertex. Nor does the failure of a fixed unbroken-SM adapter predict wrong-handed weak physics. The source's low-curvature effective statement may use EW-broken backgrounds, full covariant spurions, twisted receiver coordinates, or a physical readout. Those are permitted structural categories with explicit map/cost obligations. Small-curvature suppression needs the previous common-domain/gap-or-time/current hypotheses; this branching calculation supplies none of them.

### 7. Scope and fastest discriminators

1. Authenticate the action of the source's relevant connection/epsilon on the normal scalar, form and dual slots (geometric G or moving M, not failed spin-only F).
2. Establish the actual residual background group: fullSM, colorEM, or one with a surviving additional U1. This single answer separates maximal ranks0/8/128 without searching action coefficients.
3. If colorEM, test the source-native trace/other supplied tensor's exact normal position and nonzero norm. A neutral weak4 tensor is an explicit algebraic survivor; a generic negative trace need not have that position.
4. Identify held versus transported source current and scalar receiver FIRST. Held nonzero standard cross-current rejects global odd congruences already under unbroken charged generators; transported fields/bars give an exact pullback with the complete density, epsilon and geometry/connection chain terms. Only then use a broken weak generator to test whether the old gauge-action identification, rather than its conjugate, is being retained. ColorEM intertwiners pass the representation-covariance test by construction, not the held-current test.

The result excludes only the fixed same-action invertible adapter category at PS/fullSM, and exhibits its precise singular residue and nonempty EW-broken successor. It does not require every possible source resolution to use an odd adapter: relative-label/sign, changed-arrow, nonlocal/domain/readout and source-admitted operator rivals remain distinct. No source kill, family count, chirality prediction, action construction, class-C restriction or matrix status change follows.

### 8. Object-first collision / prior-art note

A final mechanism search found K2165 (`explorations/conditional-build/k2165-even-clifford-adapter-descent-2026-10-27.md`) already classifies the FULL even-horizontal-Clifford centralizer as Cl(N)+ω_H Cl(N), dimension2048 real in its Cl77 category. The complex horizontal-Lorentz Schur step above is the same underlying centralizer fact, not new mathematics. K2165's intertwining target is a normalized fixed-splitting five-spinor principal adapter, with ten such slots and a different simple-contraction operator; its seven-form exclusion is not imported here. What is new in this front is intersecting the scalar chirality-odd portion with the actual normal PS→SM→colorEM actions, obtaining exact support/ranks and explicit higher-tensor/vector witnesses, and following the SAME scalar adapter through the current/reduction costs.

CB7 (`lab/active-research/joe-directed/high-energy-two-plus-one/cb7-homogeneous-cell-parity-classifier-2026-08-16.md`) and the earlier source-sign/primalizer records already classify minimum odd-adapter grammar and warn that a parity bit does not construct a module-coherent map. Their H210/144 and W+mirror graph objects differ from this fullDirac scalar. No old source-sign obstruction, family claim or retired graph kill is reopened. Standard Schur branching and exterior-spinor algebra have no novelty claim; only this scoped structural comparison is new.

## Part II. Independently fixed currents

### Scope and source custody

SC-OP-04 ASSERTS the candidate-strength four-independent-field operator at draft eq9.16; SC-OP-05 UNCERTAIN admits an unspecified nonzero-SE rival. The primary extraction `lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md` records eq9.18's connection Euler component as the outer-starred sum of barν ζ, barζ ν and odot(barζ,ζ), and eq9.20 joins bosonic and fermionic Euler residuals. It does not select a density lift, odot coefficient, or global variational domain. Bars remain independent throughout. No isolated NW Ward identity is imposed and no unique Shiab contraction is inferred.

SC-GRP-02 and SC-GEO-51 ASSERT the U(64,64) parent; SC-GRP-03 ASSERTS the normal-bundle reductions/intersection; SC-GRP-06 ASSERTS no internal symmetry group; SC-FER-07 ASSERTS normal-spinor quantum numbers. The representations below are restrictions of that geometric spin carrier, not an inserted internal factor. The known complex branching is used with its own scope, not as a real-form, physical-family or chirality derivation. SC-META-56 DISAVOWS demanding an action for the odd graded structure as a prerequisite. The Noether analysis below concerns ordinary gauge covariance of whatever variational family is actually supplied.

GU-COMPARATOR-ROUTING: these are source-shaped structural constraints. No ordinary net-family count, scalar Higgs/VEV model, physical symmetry-breaking verdict, or source falsification follows. Classification INTERNAL_STRUCTURAL_ONLY.

### 1. Exact change-of-variable current, including density

Avoid using A for both the connection and the odd adapter. Write the varied connection as a, the odd adapter as C=c(v), and all geometric/epsilon/Clifford/density data as b. Let a supplied density-valued bilinear be

    I[a,Ψ,barΨ;b] = integral barΨ K_a[b] Ψ,
    Ψ=(ζ,ν), with independent barΨ.

This is notation for the variational grammar, not a proposed selected action. Fix a reference density if desired and absorb its nondegenerate density-identification matrix into K. For invertible local field/row changes

    Ψ = R[a,b] ψ,
    barΨ = barψ L[a,b],

its exact pullback has differential coefficient K'=L K R. In K(Rψ), differentiation acts on R as well as on ψ. Let V_a[α]=δ_a K[α]. Before any integration by parts,

    δ_a I' = integral barψ { (δL) K(Rψ)
                          + L V_a[α](Rψ)
                          + L K((δR)ψ) }.

Every dependence of epsilon, Hodge, Clifford embedding and density in K is included in V_a. A multiplicative density change f[a,b] adds (δf)barψ L K Rψ and multiplies the three terms by f; equivalently absorb f into L. This formula remains exact for x-dependent changes. If R/L depend on connection jets, their variations are differential operators in α; integrate them by parts with compact support to obtain the Euler covector.

In functional notation the same statement is

    E'_a = pullback(E_a) + (D_a Ψ)^* E_Ψ + (D_a barΨ)^* E_barΨ,

with any other dependent data contributing the analogous term. Stars here denote dual differential operators in the variation pairing, NOT guessed Krein conjugations. This supplies the missing connection-dependent terms explicitly. On the full transformed matter-shell they vanish, but an off-shell identity may not drop them. Boundaries contribute the correspondingly transported preboundary form and require the actual common domain.

For a-independent R,L and a fixed density, the exact frozen vertex is

    V'[α] = L V[α] R.

Hence current equality at TRANSPORTED field values is an identity of the pulled-back action. Equality in the HELD source fields is instead the substantive condition

    L V[α] R = V[α]  for every admitted α.

These are different comparisons. The fully general frozen classification is the two-sided stabilizer of the actual vertex family {V[α]}; because odot is not supplied, no numerical full stabilizer is claimed. An overall scale f multiplies the left side. A gauge transformation can also transport α by its adjoint action; equality after this gauge-index transport is weaker than equality for every held α.

Observation must follow the same distinction: O'(ψ)=O(Rψ), barO'(barψ)=barO(barψ L). Literal O unchanged requires OR=O; the prior scalar odd changes do not satisfy this on the independent scalar slot. Current equality on a physical readout only tests the relevant sandwiched vertex or solution space, not all independent off-shell rows and columns.

### 2. Charged-support theorem for an independently held cross-current

Assume an actual NE vertex has been fixed as

    V_NE(ξ,T)ν = B1(ξ tensor ρ(T)ν),

where B1 is the specified nondegenerate density-dual map and T ranges over the admitted connection Lie algebra h. Fix the same exterior arrow, fields and variation map. Define

    W_h = sum_T im ρ(T),       Z_h = intersection_T ker ρ(T).

Changing only B1 to B1' preserves this cross-current iff

    (B1'-B1)|_(V* tensor W_h) = 0.

Proof: independent bars detect every density-covector component, independent ν give every representation image, and independent ξ span V*. This is equality of bilinear tensors, not a trace or charge-sum test. Thus all possible density changes are

    B1' = B1 + M π,

where π is the quotient onto (V* tensor S)/(V* tensor W_h), subject to nondegeneracy and any separately required reality/equivariance constraints. For a compact/reductive unitary representation, S=W_h direct-sum Z_h, and π can be the invariant sterile projection. If only tangent connection covectors are varied, replace V* by H*: the conclusion fixes only horizontal form support. The obstruction below already holds on that nonzero support.

The analogous SW statement fixes B0 on W_h whenever its actual connection response contains the corresponding spin-action contraction. In the geometric form-plus-spin category this conclusion can be tested on horizontal one-form inputs and horizontal normal-gauge variations, where the normal vector action on H is zero. Do not silently assume a spin-only normal-form response for the whole SW vertex. NE alone already suffices for the main obstruction.

For the usual normal Weyl branching recorded in `lab/active-research/pati-salam-chain-verification.md`, the six complex summands have dimensions 6,3,3,2,1,1 and charges n=6Y equal to 1,2,-4,-3,6,0. Therefore:

| Admitted connection variations | W within one normal16 | Z within one normal16 | Full complex Dirac14 W/Z (horizontal multiplicity4, normal16+16bar) |
| --- | ---: | ---: | ---: |
| SU(2)_L only | 8 | 8 | 64 / 64 |
| SU(3)c x SU(2)_L x U(1)Y | 15 | 1 | 120 / 8 |
| SU(3)c x U(1)EM | 14 | 2 | 112 / 16 |
| full parent U(64,64) on S | all | 0 | 128 / 0 |

For full SM the only invisible normal state is the neutral singlet, not all weak singlets. Hypercharge already acts invertibly on every other displayed summand; its zero trace does not cancel entrywise current polarization. For color+EM both neutral states per16 are invisible. For the parent, the central iI acts invertibly. These are complex carrier/support dimensions, not independent real field counts or physical family numbers. Compact branching is used only as the existing representation restriction, not a claimed compactification. For other reductions compute W and Z rather than reusing this table.

Gauge symmetry breaking does not by itself remove broken-generator connection variations from the full action. Restricting to an effective unbroken current requires an explicit restriction/integration-out/current matching; a vacuum stabilizer is not that map.

#### Consequence for same-half density repair

The natural opposite-half density B detects a nonzero u in W_h of ambient chirality s against some barred vector of chirality -s. A same-half B' annihilates that same pairing. Thus B' cannot both have the new same-half support and agree with B on a nonzero graded charged W_h. All admitted normal gauge generators are ambient-even, so W_h and Z_h are chirality-stable. Full SM fixes the incompatible density on 120/128 spinor support; weak alone already fixes a nonzero half and excludes a uniform same-half replacement there. Sterile freedom remains real, but modifying only it cannot repair all printed derivative cells, which also test charged independent fields.

This strengthens the prior November13 §6 image-spanning control: one does not need all of S to be spanned to obstruct a global parity-changing density. It does NOT authenticate B as the source-selected density. It is a conditional statement once an independent fixed current/density is actually supplied.

### 3. Exact scalar-coordinate congruence classification

The previous two tensor repairs reduce to a scaled scalar-coordinate congruence. In density-row coordinates write

    K = [[K11,K10],[K01,0]],
    K' = f diag(I,U) K diag(I,V).

Here U acts on the scalar equation-output/density-row coordinate and V on the independent scalar field; C or C^-1 are the previous choices. This is a general frozen scalar-only family, not a guessed action. The cross-current blocks become

    V'10(α)=f V10(α)V,
    V'01(α)=f U V01(α),
    V'11(α)=f V11(α).

For independently held standard cross vertices, exact same-current conditions are

    ρ(T)(f V-I)=0  for every T,
    (f U-I)ρ(T)=0  for every T,

after the actual fixed nondegenerate density identifications. The second formula presumes the typed SW spin-response just stated; use its actual response otherwise. Equivalently,

    im(fV-I) subset Z_h,       (fU-I)|_W_h=0.

Thus V must induce f^-1 times identity on the charged quotient S/Z_h; U must restrict to f^-1 times identity on W_h. In W⊕Z coordinates, the complete cross-only solution is

    V = [[f^-1 I_W,0],[P,Q]],
    U = [[f^-1 I_W,R],[0,T]],

with Q,T invertible for invertible U,V. If h-equivariance is also required, maps between nontrivial W and trivial Z vanish: P=R=0, leaving arbitrary invertible sterile blocks Q,T. If a nonzero NW current is independently fixed, its unchanged block also forces f=1. No f=1 conclusion is taken from an unspecified or vanishing NW coefficient. The common congruence U=V imposes both sets of conditions and removes P,R even without separately imposing equivariance.

#### Odd scalar adapters fail this fixed-current test, even if equivariant

For any nonzero W_h, a chirality-odd invertible V cannot induce the nonzero scalar f^-1 I on S/Z_h: the quotient grading is well-defined, the induced V anticommutes with it, while the identity commutes. Equivalently, on a nonzero charged chiral vector the old cross vertex is in one ambient half and the odd-adapted cross vertex is in the other. This uses independent field polarization, not an approximate dimension comparison. The same argument applies to U where the SW response is as above.

Therefore an adapter can COMMUTE with the unbroken color+EM representation, even have full rank, and still fail the held cross-current identity. A commutator tests representation equivariance; rho(T)V=rho(T) tests current preservation with the scalar field name held fixed. These are not interchangeable. The weakness of the source physical-current identification prevents promoting this conditional failure to a GU obstruction.

If odd changes are confined to Z while identity is retained on W, current-preserving sterile modifications exist (when the graded sterile dimensions allow them). Such a block operator is not globally chirality-odd and cannot perform the prior uniform parity repair. The same point applies to the full-SM odd-commutant space (complex dimension4, maximal complex rank8 in the stated full carrier): sterile invertibility does not give a global invertible odd repair.

For the NW tensor repair the prior paired identity is K'_NW=λ B R_- D R_- with R_-=diag(I,C^-1), λ=C² and K=BD. Thus in density-row coordinates it is λ (B R_- B^-1) K R_-. For the cross-arrow repair K'_cross=B R_+ D R_+=(B R_+ B^-1) K R_+, with R_+=diag(I,C). Do not commute B through C or mistake a barred density row for an unbarred spinor. After the actual B0 identification the scalar left factor is C^±1; in the held grammar the former cross blocks carry λ C^-1=C, and the latter carry C. Both therefore face exactly the same charged-support obstruction. Absorbing λ into density or independently renormalizing bars is another coordinate change; if it is allowed, repeat the displayed f,U,V conditions. A nonzero scalar normalization cannot turn an odd charged-quotient map into identity.

By contrast, at transported old fields and bars each congruence has exactly the original current pulled back, with the transformed scalar observation, density and grading. That is an authentic equivalence of a supplied bilinear. It cannot simultaneously be described as unchanged literal scalar provenance/current grammar. This viable transported branch is not excluded.

### 4. Connection-dependent repairs: useful exact separation

The frozen equations remain the necessary direct-vertex test when C, density and epsilon are independent parameters during connection variation. If C=C[a], the extra chain terms in §1 can cancel a direct current difference off shell only if their complete local differential expression does so; they are not automatically zero. A useful independent-jet diagnostic compares their derivative orders. For an algebraic C[a], δC is algebraic in α but K((δC)ψ) contains derivatives of α and of ψ. The Euler covector after integration by parts contains the associated matter Euler derivative. Equality only after setting matter equations to zero is on-shell equality, not the held off-shell source eq9.18 identity.

There is no general impossibility theorem for engineered a-dependent maps: exact pullbacks, gauge-related coordinates, constrained variations, or additional compensating vertices can exist. Their admissibility still depends on locality, differential order, real structure and domain. An a-independent moving tensor C(x) contributes derivatives ∂C to the differential operator but no δ_a C term. These two meanings of 'moving' must be separated.

Even when δ_a C=0 for an external C(x), its covariant derivative varies as δ_a(∇C)=[ρ(α),C] in a fixed spin frame. The compensated cross arrow d_a composed with C has vertex ρ(α)C; its rewritten form C d_a+(∇C) has the same vertex because Cρ(α)+[ρ(α),C]=ρ(α)C. Omitting the compensator instead gives Cρ(α). Thus the §3 condition uses the full compensated composition and does not confuse a connection-independent tensor with a connection-independent covariant derivative. The matching form-leg/geometric variation remains included.

A changed independent background connection can also make a principal block insensitive to the connection being tested. That changes which connection current is measured and must be named. It does not change the symbol repair by a zero-order cancellation alone.

### 5. Moving geometric tensors, epsilon and full Noether identity

Let b denote any additional geometric tensor, background section, epsilon wrapper or chimeric identification. Suppose a supplied family is gauge-covariant when b transforms. With infinitesimal gauge parameter η, write schematically

    δa=-D_a η,   δΨ=ρ(η)Ψ,   δbarΨ=-barΨρ(η),   δb=R_b(η).

The integrated Noether identity is the adjoint of this ENTIRE variation generator:

    (-D_a)^* E_a + R_Ψ^*E_Ψ + R_barΨ^*E_barΨ + R_b^*E_b = 0.

No isolated NW divergence identity follows. This is compatible with the source total-Euler architecture at eq9.20, and does not demand an unasserted odd action symmetry.

Three distinct branches survive:

1. **External parameter transported across backgrounds.** b is not varied dynamically but transforms as a spurion to relate different backgrounds. The family is covariant. On a fixed background only its stabilizer is a symmetry, unless the omitted term R_b^*E_b vanishes for a separate reason. On the dynamical field shell the residual Noether balance still contains this background force term; claiming full conservation by dropping it is invalid. Class C explicitly admits typed external background/boundary data, so this cost does not exclude hosting.
2. **Independent dynamical b.** Include E_b=0 and all its contributions. Then the full identity reduces on the full shell. Added equations, DOFs and constraint/domain effects must be supplied; no unique completion is selected here.
3. **Composite b=F[a,g,epsilon,...].** Pull back the action with the full chain rule. The connection Euler covector contains (D_aF)^*E_b, and the other owners receive their corresponding terms. Gauge-fixing or choosing an adapted moving frame cannot erase these terms from an off-shell comparison; it changes coordinates/constraints and the gauge generator together.

In particular full-parent conjugation transports c, chirality, C, density and epsilon simultaneously. It preserves relative parity and the rank/support of the cross-current; it does not create an odd fixed-current repair in each chart. A noninvariant negative-normal trace vector may define a covariant family across backgrounds, despite failing fixed weak invariance. Additional positive normal direction or horizontal clock choices face their respective geometric/representation costs but are not excluded as typed external data. A global chimeric-to-normal bridge and a domain preserving these transports remain separate questions.

### 6. Shortest useful next discriminator

Do not demand an entire selected action or invent coefficients. Fix only the source-owned connection-variation prescription for the cross terms:

    α -> δ(d_a), δ(d_a^*), δepsilon, δB0, δB1,

with explicit statement of what is held: independent source fields, section, chimeric/Clifford map and background tensor. This is enough to decide whether the standard cross vertex above is the operative one. Then:

- if literal source fields and nondegenerate standard cross vertices are held, the previous globally odd scalar congruences cannot preserve that off-shell current even under only weak variations; full SM leaves merely the sterile quotient invisible;
- if scalar/row/observable coordinates are transported, retain the exact equivalent branch and test the actual physical readout and its common domain;
- if epsilon or geometric tensor is connection-dependent, retain the complete chain current and gauge generator, and distinguish on-shell from off-shell matching;
- if an effective current projects away directions, record that projection/solution space before applying a support theorem.

This discriminates surviving structural categories without manufacturing odot, selecting a specific action, treating an isolated Ward test as law, or requiring exact physical-sector invariance that the source only claims effectively.

### Novelty and verification limits

Object-first search found:

- November12 `source-current-grading-membership`: independent-bar SE theorem, hidden coordinate shifts, basic a-dependent chain-rule caveat.
- November13 `source-degree-duality-compatibility` §6: image-span density theorem and central-iI full-parent control.
- June24 `misc/constraint-first-ig-tangent-space-gate` and `misc/gu-closed-loop-action-ig-branch`: background/spurion Noether cost, without this scalar-congruence/current classification.
- August05 `lab/sources/gu-defect-localization-ward-bv-source-reinspection`: moving-current/density chain rules in a different support-motion object.

New delta is the exact weak/SM/EM charged-versus-sterile support, the full scalar-only current-stabilizer equations and their parity obstruction even when the adapter is representation-equivariant, plus the explicit connection/density chain rule and its parameter/dynamical/composite routing for THESE repairs. General spurion caveats and generic field-redefinition equivalence are inherited facts, not novelty claims. Universal results rest on written polarization and quotient-grading proofs; the retained replay supplies exact supporting and contrary current controls, reviewed against these proofs. All statuses and class C remain unchanged.

## Evidence and acceptance

- Primary source claims: `lab/sources/source-claim-register.yaml`; fields/current: `lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md`; source labels: `lab/sources/gu-2021-draft-s11-s12-extraction-2026-08-03.md`.
- Prior full-carrier results: `explorations/conditional-build/source-symbol-quotient-membership-2026-11-12.md` and `explorations/conditional-build/source-current-grading-membership-2026-11-12.md`.
- Earlier joint tests: `explorations/conditional-build/source-weak-action-transport-2026-11-13.md` and `explorations/conditional-build/source-degree-duality-compatibility-2026-11-13.md`.
- Companion: `explorations/conditional-build/source-moving-repair-2026-11-13.md`.
- Replay: `tests/program-focus/source_current_geometry_probe.py`; exact retained evidence and dependency hashes: `lab/process/source-current-geometry.json`.

Independent specialist cross-review and exact supporting/contrary controls
support conditional T2 acceptance. Written universal proofs carry the claims;
finite controls and assertion counts are not independent discoveries. No Lean,
external-expert certification, selected source action, physical prediction,
source/canon verdict or class-C decision is claimed. Matrix18/18 remains
constrained and its joint realization remains open.
