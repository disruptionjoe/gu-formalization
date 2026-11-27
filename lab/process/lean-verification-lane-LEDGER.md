---
title: "Lean Verification Lane: Ledger and Queue"
status: canon
doc_type: lane-ledger
scope: repo-local
created: 2026-07-07
updated: 2026-11-25
owner_surface: lab/methods/lean-verification.md
---

# Lean verification lane: ledger and queue

## Purpose and boundary

This is the standing Lean queue inside result-hardening research, result hardening and publication readiness. Hourly Progress
uses it only when `lab/process/RESEARCH-AGENDA.json` selects the relevant result-hardening research work item. A finishable
formalization must not displace protected truth-status research merely because Lean has a monotone success condition.

Lean hardens the deduction from explicit premises. It does not establish carrier faithfulness, physical
realization, full-arena transfer, Proposition 1, the W235 record bit, interacting QFT, or external
replication. Those stay in owner prose and machine certificates. Status vocabulary:

- `LEAN-VERIFIED`: default or named target typechecks, with no `sorry` or unreported axioms, and the owner cites it.
- `SOURCE-READY`: complete proof source exists, but the current checkout lacks a green build receipt.
- `LEAN-PARTIAL`: source needs a bounded repair.
- `NUMPY-CERT`: checked in Python only.
- `SYMPY-DERIVED`: symbolic result outside Lean.
- `ARB-CERT`: rigorous interval/ball enclosure via python-flint (FLINT 3 / Arb), with the working
  precision recorded. Strictly stronger than `NUMPY-CERT` for any claim that compares floats or
  asserts a bound; strictly weaker than an exact symbolic identity. Use it for the RB-campaign
  residual, signal/floor, and stability margins currently graded "controlled local numerics."
- `CAS-VERIFIED`: multiplicity, branching, or rank result independently confirmed in a computer
  algebra system (SageMath / Singular / GAP), with the session transcript or script committed.
  Required by the gates listed in `computational-toolchain.md`. Layer-0 applies: a CAS returns a
  decomposition, never a count.
- `PROSE`: written argument only.

## November certificate inventory reconciliation (2026-11-25)

Eight existing finite kernels are now included in the default entrypoint. Their
prior targeted verification is recorded in their linked result and `VERIFICATION.md`;
those receipts do not by themselves certify this newly expanded default target.
The owner closing verification records the exact target, toolchain/manifest and
result of the serialized integration check. No theorem body or scientific scope
changes here, and source/geometry/domain premises remain explicit.

| Lean file | Exact finite scope | Prior targeted evidence |
|---|---|---|
| `Lean/GUFormalization/MetricNormalGradingCore.lean` | Conditional pairing/linear-map core: a selfadjoint shape cannot equal a skew connection on a nondegenerate pairing; supplied faithful Clifford residual and nonzero coefficients retain the defect. No geometric connection, domain or physical grade is constructed. | `explorations/conditional-build/metric-normal-family-grading-2026-11-24.md`; `VERIFICATION.md` |
| `Lean/GUFormalization/ObservedHiddenPremise.lean` | Integer cancellation from supplied same-grading additivity and total balance, plus the supplied closed-comparison coefficients. Source non-chirality is not proved to supply those analytic premises. | `explorations/conditional-build/zero-total-grading-premise-2026-11-20.md`; `VERIFICATION.md` |
| `Lean/GUFormalization/ObservedHiddenSplit.lean` | Finite six-term exact-sequence index additivity and its balanced-total corollary. Exactness, Fredholm realization and physical grading remain supplied obligations. | `explorations/conditional-build/native-descending-grading-classification-2026-11-21.md`; `VERIFICATION.md` |
| `Lean/GUFormalization/ProvenanceMixing.lean` | Finite rational six-slot evolution and trace/remainder/scalar mixing checks. No Clifford, PDE, action or physical-family claim. | `explorations/conditional-build/bet-2plus1-provenance-observation-2026-11-11.md`; `VERIFICATION.md` |
| `Lean/GUFormalization/SixSpinorGrading.lean` | Conditional finite algebra for receiver uniqueness, quotient oddness and an injective torsion witness, with coefficients, geometric identities and descent supplied. No source-owned physical grading or analytic domain. | `explorations/conditional-build/six-spinor-grading-compatibility-2026-11-24.md`; `VERIFICATION.md` |
| `Lean/GUFormalization/SourceClassCore.lean` | Rank lower bound and six-slot minimum from supplied kernel containment and dimensions15s/9s. Spin invariant theory, completeness, source necessity and physical observation domains are outside Lean. | `explorations/conditional-build/source-natural-symbol-class-2026-11-24.md`; `VERIFICATION.md` |
| `Lean/GUFormalization/ThreeLocalFloor.lean` | Finite additive/character algebra distinguishing virtual C2 representations from ZMod2 and showing a mod3 character does not factor through forgotten rank. No topology or native datum floor is formalized. | `explorations/conditional-build/x-d1-p3-three-local-floor-2026-11-11.md`; `VERIFICATION.md` |
| `Lean/GUFormalization/WeldCoefficientScope.lean` | Phase propagation along a supplied connected relation and an incompatible two-cycle coefficient control. No class-C action, source coefficient or geometric realization. | `explorations/conditional-build/x-p1-p2-class-c-lift-2026-11-11.md`; `VERIFICATION.md` |

## Part A: current certificate surface

The toolchain and manifest are pinned.  A fresh serialized macOS build at Lean `4.32.0-rc1` and manifest
mathlib revision `96ec947e9b66a5e6059131fc9c6d13a14cef756e` completed successfully on 2026-07-22
(`lake build`, 8,643 jobs, exit 0; pre-existing linter warnings only).  Receipt scope note (2026-08-03):
that 2026-07-22 build predates the 2026-07-23 edits to `Lean/GUFormalization/LocatedNotForcedFiniteCore.lean`
and `Lean/GUFormalization/LocatedNotForcedLegs.lean`.  The current receipt for those two files is the
located-not-forced v1.0.0 release verification,
`papers/candidates/located-not-forced/zenodo-package-v1.0.0/VERIFICATION.md` (verified 2026-07-23):
targeted `lake -Kjobs=1 build +GUFormalization.LocatedNotForcedFiniteCore` (which builds
`LocatedNotForcedLegs` via its import) plus `lake env lean` single-file checks passed, with only the
standard mathlib axioms `propext`, `Classical.choice`, `Quot.sound` reported.

| Lean file | Scope | Current source status |
|---|---|---|
| `Lean/GUFormalization/Status.lean` | Claim-status order and dependency monotonicity | `LEAN-VERIFIED`; 2026-07-22 baseline |
| `Lean/GUFormalization/K3IndexArithmetic.lean` | Symbolic K3 and RS index arithmetic | `LEAN-VERIFIED`; 2026-07-22 baseline |
| `Lean/GUFormalization/W2Polynomial.lean` | `F_2` polynomial identities behind corrected `w2(Y14)` | `LEAN-VERIFIED`; 2026-07-22 baseline |
| `Lean/GUFormalization/LocatedNotForcedLegs.lean` | Krein transversality, corrected finite star-semilinear image typing with explicit null-image premises and zero `intersectionDifference`, and 2-primary identities; no physical-real-form, Fredholm, observed-handedness, function-space, or generation-selection theorem | `LEAN-VERIFIED`; authoritative finite located-not-forced certificate, with T3 correction follow-through verified 2026-08-22; prior release receipt remains the 2026-07-23 zenodo package `VERIFICATION.md` |
| `Lean/GUFormalization/LocatedNotForcedFiniteCore.lean` | Finite census encoding for the LNF paper; exhaustiveness/closure by `decide` over the encoded item list; census numerals are imported data, not derivations | `LEAN-VERIFIED`; 2026-07-23 zenodo receipt (`papers/candidates/located-not-forced/zenodo-package-v1.0.0/VERIFICATION.md`) |
| `Lean/GUFormalization/ResidualSelection.lean` | Residual-selection finite logic kernels | `LEAN-VERIFIED`; 2026-07-22 baseline |
| `Lean/GUFormalization/GroupActionFixedPoints.lean` | Pure set-level valuation-space classification: invariant valuations are equivalent to functions into the common fixed-point subtype and satisfy `|Inv| = |Fix|^|A|`; separately, equivariant maps from an arbitrary acted-on domain form the dependent product of stabilizer-fixed seed values over the orbit quotient and satisfy the exact finite orbit-product census. Seed spaces at representatives in one orbit are explicitly equivalent; equivariant domain and codomain equivalences preserve complete map and fixed-seed spaces; domain transport induces an orbit-quotient equivalence and commutes with codomain transport. Equivariant maps into arbitrary indexed products of acted-on codomains are indexed families of component equivariant maps; common-fixed and stabilizer-fixed seed spaces, finite counts and existence decompose by the same product. A uniform stabilizer-fixed condition reduces the orbit product to `|B^H|^|A/G|`, with free-domain and trivial-codomain results as specializations. The transitive and regular-torsor theorems are one-orbit special cases. No physical group action, observer, dynamics, selection or GU verdict is encoded | `LEAN-VERIFIED`; 2026-08-30 targeted and serialized default-target build; theorem-level receipt exposes product-family choice, quotient-representative and classical-transporter choice and only standard Lean/mathlib axioms; W99 includes indexed heterogeneous codomains, empty-index/factor edges, domain/codomain relabeling, orbit-quotient transport, commuting naturality, uniform and nonuniform stabilizers, representative transport, multiple free orbits, mixed free/fixed, fixed-only, regular-plus-coset and empty-domain hostile controls |
| `Lean/GUFormalization/GroupActionCoproducts.lean` | Pure set-level dual law: equivariant maps out of a heterogeneous indexed Sigma coproduct are indexed families of component equivariant maps. Finite counts multiply and existence is componentwise; the fiberwise action preserves indices and does not model index mixing | `LEAN-VERIFIED`; 2026-08-30 focused packet check plus serialized default-target integration; theorem-level receipt exposes arbitrary-family choice only in the reverse existence law; W99 checks mixed free/fixed fibers, empty index and empty component |
| `Lean/GUFormalization/EquivariantInternalHom.lean` | Pure set-level closed structure: the explicit conjugation action on `A -> B` has exactly the equivariant maps as common fixed points, and equivariant maps on a diagonal product curry to equivariant maps into that internal hom | `LEAN-VERIFIED`; 2026-08-30 focused packet check plus serialized default-target integration; named non-global action avoids the pointwise-action instance; W99 checks C3 inverse placement, fixed points and the complete curry/uncurry map space |
| `Lean/GUFormalization/GroupActionChangeOfGroups.lean` | Pure set-level change of acting groups: actions restrict explicitly along `phi : H ->* G`; surjective `phi` preserves the complete equivariant-map and fixed-point spaces; coinduced functions with right translation satisfy the restriction-coinduction adjunction, with exact finite-cardinality and existence consequences | `LEAN-VERIFIED`; 2026-08-30 focused and serialized default-target integration; all added actions are named non-instances; the theorem-level receipt exposes no new axiom dependency; W99 checks a C4-to-C2 surjection, a non-surjective strictness control, and a nontrivial coinduction census |
| `Lean/GUFormalization/GroupActionInduction.lean` | Pure set-level induction: the explicit `H`-action on `G × B` generates the balanced-product quotient, left `G`-translation descends, induction is left adjoint to restriction, and equivariant seed maps descend functorially with identity, composition and `G`-equivariance laws | `LEAN-VERIFIED`; 2026-08-30 focused and serialized default-target integration; quotient relation, inverse placement and actions are explicit; theorem-level receipt exposes only the established `propext`, `Classical.choice` and `Quot.sound` surface; W99 checks trivial-subgroup and nontrivial identity-homomorphism carriers plus the complete universal-property image/inverse |
| `Lean/GUFormalization/GroupActionInductionCoherence.lean` | Pure set-level coherence: induction along the identity is equivariantly equivalent to the seed action, and induction along a composite is equivariantly equivalent to iterated induction through the explicit flattening `[g,[h,b]] ↦ [g * psi(h),b]` | `LEAN-VERIFIED`; 2026-08-30 focused and serialized default-target integration; inner and outer balanced relations, both inverse laws and `G`-equivariance are explicit; W99 checks identity collapse and a genuinely nested trivial-to-C2-to-C4 composition |
| `Lean/GUFormalization/GroupActionMackey.lean` | Complete pure set-level subgroup Mackey decomposition: `K`-orbits of `Res_K^G Ind_H^G(1)` are `K\\G/H`; actual intrinsic index fibers give a canonical representative-free `K`-equivariant coproduct decomposition; seed maps act naturally; representative changes are explicit; and the Hom-form law identifies `K`-equivariant maps out of `Res Ind B` with the dependent family of transported-intersection seed-map spaces | `LEAN-VERIFIED`; 2026-08-30 focused and serialized default-target integration; the Hom-form equivalence composes domain transport, dependent-coproduct Hom and fiberwise induction-restriction with exact cardinality and existence consequences; theorem receipt exposes only the established `propext`, `Classical.choice` and `Quot.sound` surface; W99 checks the nonnormal `S3` map space has 27 elements on both sides as factors 3 and 9, with a hostile non-equivariant control |
| `Lean/GUFormalization/GroupActionMackeyLinearization.lean` | Free finitely-supported module lift of the canonical Mackey carrier equivalence, with basis/support preservation, seed-map naturality and supplied-`K`-action equivariance | `LEAN-VERIFIED`; 2026-08-31 focused integration; no new choice beyond the inherited quotient carrier, and no physical representation, action coefficient or additive Mackey-functor claim; W99 checks exact coefficients, support, naturality, both `S3` subgroup elements and a noninjective hostile collapse |
| `Lean/GUFormalization/GroupActionMackeyRepresentations.lean` | Bundles the canonical and restricted-induced free modules as `K`-permutation representations, proves canonical assembly is a representation equivalence, and derives the `R[K]`-module isomorphism for commutative semirings | `LEAN-VERIFIED`; 2026-08-31 focused integration; action identity/product and intertwining are theorem fields, with no physical/source representation claim; W99 checks both representation laws, every nonnormal-`S3` basis square and a hostile nonbijective generator |
| `Lean/GUFormalization/GroupActionMackeyCategory.lean` | Packages the representative-free Mackey construction and restricted induction as functors on supplied actions, proves canonical assembly is a natural isomorphism, and transports it through Mathlib linearization to representation functors | `LEAN-VERIFIED`; 2026-08-31 serialized default-target integration; identity, composition and naturality are explicit proof obligations; no additive/physical Mackey-functor claim; W99 checks the complete nonnormal-`S3` functor/naturality control |
| `Lean/GUFormalization/GroupActionMackeyAdditivityBoundary.lean` | Proves the raw category of supplied group actions has no point-to-empty morphism and therefore cannot be preadditive or have a zero object | `LEAN-VERIFIED`; 2026-08-31 focused integration; exact semantic obstruction to promoting the current raw-source natural isomorphism into an additive Mackey functor; no span/Burnside completion, transfer data or physical realization is constructed; W99 checks the empty/singleton finite witness |
| `Lean/GUFormalization/GroupActionAdditiveEnvelope.lean` | Lifts supplied-action functors and natural isomorphisms to Mathlib's free integer-linear categories and applies the construction to canonical Mackey naturality | `LEAN-VERIFIED`; 2026-08-31 focused and serialized default-target integration; the point-to-empty hom becomes exactly formal zero, with no new raw action map, span/Burnside morphism, restriction/transfer data or physical realization; W99 checks coefficientwise additivity and the empty-generator edge |
| `Lean/GUFormalization/GroupActionBurnside.lean` | Constructs the additive Burnside group of finite supplied actions, descends subgroup restriction and induction, and proves the transported-intersection double-coset identity | `LEAN-VERIFIED`; 2026-08-31 focused integration; equivariant equivalence and disjoint-coproduct relations are explicit and the Grothendieck completion supplies inverses; no universal span category, physical representation, source action or GU claim; W99 checks the nonnormal-`S3` 2+4 coproduct, additive class census and a hostile omitted summand |
| `Lean/GUFormalization/GroupActionSpanCategory.lean` | Constructs the category of arbitrary equivariant spans between finite supplied actions, quotiented by equivariant apex isomorphism and composed by finite equivariant pullback; graph spans preserve map composition and converse graphs supply transfer-direction arrows | `LEAN-VERIFIED`; 2026-08-31 focused integration; explicit pullback unitors and associator prove category laws; no separate categorical universal property, homwise coproduct addition, preadditive/group completion, physical/source realization or GU claim; W99 checks identity and associativity through finite multiplicity matrices and rejects hostile entrywise pairing |
| `Lean/GUFormalization/GroupActionBurnsideSpanCategory.lean` | Gives span hom-sets disjoint-coproduct commutative-monoid structure, proves pullback composition distributes in both variables, and Grothendieck-completes every hom to a preadditive Burnside span category | `LEAN-VERIFIED`; 2026-08-31 focused integration; category, bilinearity and graph-generator laws elaborate with only the established `propext`, `Classical.choice`, and `Quot.sound` surface; W99 checks integer multiplicity-matrix addition, formal inverses and both distributivity laws; the point-endomorphism law and all-object point-representable functor are supplied separately, while physical/source realization remains open |
| `Lean/GUFormalization/GroupActionBurnsideSpanMackey.lean` | Identifies the supplied-action Burnside group with the completed point-endomorphism group, transports subgroup restriction and induction, and proves the double-coset law there | `LEAN-VERIFIED`; 2026-08-31 focused integration; quotient and Grothendieck inverses are explicit and the theorem reuses the independently proved finite-action Mackey law; W99 checks the nonnormal-S3 point-apex class and omitted-summand controls; the all-object point-representable functor is supplied separately; no physical/source Mackey functor, source action or GU claim |
| `Lean/GUFormalization/GroupActionBurnsideMackeyFunctor.lean` | Defines the additive point-representable functor `A ↦ Hom(point,A)` on every completed finite supplied-action Burnside span object, with graph transfers, converse-graph restrictions, identity/composition laws, and canonical-pullback Beck-Chevalley | `LEAN-VERIFIED`; 2026-08-31 focused integration; W99 checks the integer-valued finite-set law and rejects a hostile non-pullback relation; this is one fixed-`G` representable functor, not a classification, subgroup-change theory, physical/source realization or GU claim |
| `Lean/GUFormalization/GroupActionBurnsideSpanRestriction.lean` | Restricts completed finite-action Burnside span categories along supplied group homomorphisms, preserving finite pullback composition, identities, addition, graph spans, and converse-graph spans | `LEAN-VERIFIED`; 2026-08-31 focused integration; identity and composite restriction are explicit on actions/maps and W99 rejects mixed acting-group restriction on a pullback; categorical induction, biset/correspondence coherence, physical/source realization and GU claims remain outside the theorem |
| `Lean/GUFormalization/GroupActionBurnsideSpanCorrespondence.lean` | Defines the additive restriction correspondence `Hom_H(A, Res B)`, its commuting left/right span actions, and the graph-generator interface to set-action induction/restriction adjunction | `LEAN-VERIFIED`; 2026-08-31 focused Big Wave integration; correctly typed correspondence only, not an induction functor on spans or a full biset/Mackey 2-functor; no physical/source realization follows |
| `Lean/GUFormalization/GroupActionBurnsideSpanCorrespondenceComposition.lean` | Composes restriction correspondences along two acting-group homomorphisms by restricting the second completed span, with bilinearity, zero, outer-action and graph-generator laws | `LEAN-VERIFIED`; 2026-08-31 focused Progress integration; typed iterated-restriction composition only, not categorical induction, coend classification, ambidexterity or a full Mackey 2-functor; W99 checks the integer-matrix laws and hostile pairing |
| `Lean/GUFormalization/SourceNativeSpin64Observation.lean` | General horizontal/normal gamma-kernel leakage theorem from an explicit normal right inverse | `LEAN-VERIFIED`; 2026-08-31 focused integration; literal pullback obstruction only, with no physical quotient, observed family, mass or action claim |
| `Lean/GUFormalization/SourceNativeObservationDescent.lean` | Exact iff and uniqueness criterion for descent of an ambient Clifford kernel through observation when ambient contraction has a supplied right inverse | `LEAN-VERIFIED`; 2026-08-31 focused integration; explicit algebraic acceptance condition only, with no source-owned factor, physical quotient, family, mass or action claim |
| `Lean/GUFormalization/SourceNativeCorrectedObservation.lean` | Canonical trace-subtraction projector from a supplied observed Clifford right inverse, including idempotence, kernel-times-trace decomposition, and corrected-observation laws | `LEAN-VERIFIED`; 2026-08-31 focused and serialized default-target integration; the split remains supplied and no source/action selection, physical quotient, representation meaning, family, chirality, mass, prediction or GU claim is constructed |
| `Lean/GUFormalization/SourceNativeCorrectedObservationNaturality.lean` | Exact dependence of the corrected projector on its right inverse, equality iff split equality, and naturality across supplied contraction/split intertwiners | `LEAN-VERIFIED`; 2026-08-31 focused Progress integration; `6/6` independent exact controls reject contraction-only naturality; no source/action selection or physical quotient is constructed |
| `Lean/GUFormalization/SourceNativeRealSector.lean` | A supplied linear involution modeling conjugation and anticommuting with chirality linearly exchanges the positive and negative chirality kernels | `LEAN-VERIFIED`; 2026-08-31 focused integration; scalar-antilinearity, the Clifford representation and physical sector identity remain outside Lean |
| `Lean/GUFormalization/SourceNativeAdjointCoupling.lean` | Finite supplied-support certificate for cubic adjoint availability and the symmetric 54/210 versus alternating 45/945 Pati--Salam owner split | `LEAN-VERIFIED`; 2026-08-31 focused integration; decomposition tables remain premises and no source coefficient, family selector or mass is constructed |
| `Lean/GUFormalization/SourceNativeFamilyOwnerIdentifiability.lean` | Proves exchange-invariant equivalent-family coefficients cannot select one copy, while invariant 54-only and 210-only packets keep the quadratic owner axis independent | `LEAN-VERIFIED`; 2026-08-31 focused Big Wave integration; identifiability boundary only, with no source action, family covector, owner coefficient, mass or physical selector |
| `Lean/GUFormalization/SourceCoefficientRank.lean` | Proves homogeneous coefficient uniqueness is injectivity, a nonzero kernel direction forces nonuniqueness, and the strict frozen-source zero constraint leaves distinct 54-axis and 210-axis solutions | `LEAN-VERIFIED`; 2026-08-31 focused Big Wave integration; exact generic linear algebra plus packet-declared source-silence instantiation, with no source action, family covector, normalization, owner ratio, mass or physical selector |
| `Lean/GUFormalization/SourceNativeActionObservationComplex.lean` | Three-stage action complex, actual cycle-subtype quotient by gauge equivalence, cycle-restricted chain-map descent, corrected-observation chain-map weld under two exact compatibility laws, and frozen-packet nonselection for injective action families | `LEAN-VERIFIED`; 2026-08-31 integrity repair and focused Wave 2 integration; `31/31` exact controls plus `8/8` hostile mutations; no source-selected action, split, analytic domain, positive physical Hilbert space or GU verdict |
| `Lean/GUFormalization/ExternalInputInterface.lean` | Exact decoder iff bijective classifier into tagged tiebreaker/free-setting codes, with no-missing-port, no-overlap, unique-code and automorphism/third-type/order controls | `LEAN-VERIFIED`; 2026-08-31 focused computational-interface integration with `13/13` exact and hostile controls; no exhaustive GU external-input carrier, classifier, groupoid equivalence or physical verdict |
| `Lean/GUFormalization/GroupActionBurnsideBisetCoend.lean` | Fixed-middle and all-intermediate-object balance quotients for Burnside restriction correspondences, descended composition, three-stage coherence, and set-valued balanced-evaluator factorization/uniqueness | `LEAN-VERIFIED`; 2026-08-31 focused integration with retained `11/11` nonnormal `S3` controls and `11/11` all-middle universal-property controls; no additive/category-valued coend, bicategory, ambidexterity, Mackey 2-functor or physical/source realization |
| `Lean/GUFormalization/CandidateCohomologyPairing.lean` | Two-sided gauge-basic bilinear descent through the actual middle cycle/gauge quotient and iff criteria between quotient nondegeneracy and the cycle radical being gauge | `LEAN-VERIFIED`; 2026-08-31 focused integration with `12/12` exact GF(2) controls; no action-owned pairing, analytic domain, selected real/Krein form, positivity, conservation, probability or physical-state claim |
| `Lean/GUFormalization/GroupActionFixedPointsAxioms.lean` | Default-target `#print axioms` receipt for the complete group-action theorem family | `LEAN-VERIFIED`; 2026-08-30 serialized default-target build; informational output checked with the proof module |
| `Lean/GUFormalization/ResidualSelectionAxioms.lean` | Manual `#print axioms` receipt; NOT in the default target; informational, non-enforcing — run via `lake env lean` | `LEAN-VERIFIED`; 2026-07-22 baseline toolchain (via `lake env lean`; outside the default `lake build`) |
| `Lean/GUFormalization/R4TwoArena.lean` | R4 weight parity, CRT, and 2-primary blindness | `LEAN-VERIFIED`; default-target integration 2026-07-22 |
| `Lean/GUFormalization/CoflipCore.lean` | Concrete Q×Q coflip accounting, Part A derived | `LEAN-VERIFIED`; 2026-07-22 baseline |
| `Lean/GUFormalization/CoflipAbstract.lean` | Abstract (eps,mu) sign accounting; the `FiniteSignature` field and the `witnessed` Prop are currently formally inert — noted | `LEAN-VERIFIED`; 2026-07-22 baseline |
| `Lean/GUFormalization/CompactImageObstructions.lean` | W243 extremal-weight annihilation algebraic kernel plus compact-image block identities; carrier faithfulness and compactness remain outside Lean | `LEAN-VERIFIED`; integrated by `b895a49c`, receipt in the good-stable paper verification |
| `Lean/GUFormalization/CompactImageObstructionsAxioms.lean` | Default-target `#print axioms` commands for the compact-image theorems | `LEAN-VERIFIED`; default-target integrated by `b895a49c`; informational output checked with the proof module |
| `Lean/GUFormalization/FiniteResearchKernels.lean` | Matrix-trace achirality deduction, section-independent `ZMod 3` arithmetic, and exact rational reduced-potential phase boundary; physical realization remains outside Lean | `LEAN-VERIFIED`; 2026-08-21 targeted serialized build, standard mathlib axioms only |
| `Lean/GUFormalization/ShiabMultiplicityCertificate.lean` | Finite Schur-overlap deduction from the supplied complex D7 decomposition rows: both 91×64 and 14×64 dimension checks, chiral selector matrix `[[0,2],[2,0]]`, full-Dirac total `4`, and non-uniqueness of the natural cross-chiral block | `LEAN-VERIFIED`; 2026-08-30 targeted and serialized default-target integration; the decomposition rows remain supplied certificate data and Lean does not construct D7 representation theory or a physical Shiab |
| `Lean/GUFormalization/VZSchurPrecondition.lean` | General determinant-free block-kernel elimination: a supplied left inverse for `E` plus injectivity of `A-BE⁻¹C` forces the complete block kernel to vanish | `LEAN-VERIFIED`; 2026-08-30 targeted and serialized default-target integration; actual-operator identification, cone invertibility and FC-VZ-1 remain open outside Lean |
| `Lean/GUFormalization/FiniteResearchKernelsAxioms.lean` | Default-target `#print axioms` commands for the finite research kernels | `LEAN-VERIFIED`; 2026-08-21 default-target build; informational output only |
| `Lean/GUFormalization/PowerMeanReduction.lean` | Finite power-mean inequality, exact 96-cell corollary, and constant-magnitude equality witness; spectral realization remains outside Lean | `LEAN-VERIFIED`; 2026-08-22 targeted and default-target serialized build |
| `Lean/GUFormalization/ChiConjugationTraceParity.lean` | Finite ordinary/weighted matrix power-trace parity under involutory conjugation; physical orientation remains outside Lean | `LEAN-VERIFIED`; 2026-08-22 targeted and default-target serialized build |
| `Lean/GUFormalization/InvolutionProjectorKernels.lean` | Inner-involution automorphism and commutator-parity core plus complementary projectors of a linear involution; carrier faithfulness, Cartan positivity, maximal-compact identification, dynamics, spectra and physical interpretation remain outside Lean | `LEAN-VERIFIED`; 2026-08-22 targeted and default-target serialized build |
| `Lean/GUFormalization/PacketLocalPositiveCone.lean` | Sign-invariant pointed subsets are trivial; a raw linear-map range on a nontrivial carrier cannot itself be pointed and generating; and a phase-preserved cone whose phase map squares to negation has the same obstruction. The theorem does not exclude a quadratic, ray, dual-functional or otherwise extended positive carrier | `LEAN-VERIFIED`; 2026-09-01 focused and serialized default-target build; exact rational extension control `15/15`, hostile selftest `13/13`; no GU-native quotient, positive majorant, state, Born rule, action, prediction, confirmation or verdict |
| `tests/big-swing/R4_TwoArena.lean` | Stable R4 compatibility entrypoint | imports the default-target proof-bearing module |

The un-typechecked draft duplicate formerly at
`papers/drafts/hardening-pass-2026-07-03/A1-located-not-forced-legs.lean` was retired on 2026-07-22.
`Lean/GUFormalization/LocatedNotForcedLegs.lean` is the sole authoritative certificate.

## Part B: stable theorem-grade queue

| Id | Theorem-grade claim | Source | Current | Feasibility | Load-bearing for |
|---|---|---|---|---|---|
| T1 | No-go is 2-primary; no obstruction is 3-divisible | located-not-forced paper section 4 | `LEAN-VERIFIED` at last receipt | complete | located-not-forced |
| T2 | Krein transversality: positive-definite subspace meets each totally isotropic subspace trivially (`intersectionDifference = 0`) | located-not-forced paper section 6 | `LEAN-VERIFIED` at last receipt (retitled 2026-08-03: `papers/candidates/located-not-forced/HARDENING-QUEUE.md:118` bans the former "net chiral index" phrasing) | complete | located-not-forced |
| T3 | Antilinear null-image transversality | located-not-forced paper section 6 | `LEAN-VERIFIED`; corrected finite complex Hermitian image-subspace theorem only: a supplied star-semilinear map, strict positivity, and explicit total isotropy of both mapped images imply zero `intersectionDifference`; V15-1 forbids physical-handedness, Fredholm, or unchanged Lorentzian-half transfer | complete | located-not-forced |
| A | Achirality: `{K,chi}=0` implies `Re tr(chi Pi_+) = 0` | `canon/ghost-parity-krein-synthesis.md:26` (statement); `explorations/big-swing-2026-07-06/R3-pt-phase-classification-gu-cores.md` | `LEAN-VERIFIED`; explicit finite complex-matrix premises, trace readout only | complete | fences the chiral-generation reading |
| B | V7 mod-3 index arithmetic | `explorations/big-swing-2026-07-06/VG-V7-cp2-equivariant-payoff.md` | `LEAN-VERIFIED`; section-independent `ZMod 3` core only | complete | count-import boundary |
| C | Exact A1 phase boundary `lq = -l4/192` | `explorations/big-swing-2026-07-07/A1-native-potential-alignment.md` | `LEAN-VERIFIED`; rational reduced-family coefficient boundary only | complete | mirror alignment phase |
| D | Power-mean reduction | `explorations/big-swing-2026-07-07/A1-native-potential-alignment.md` §2 and execution-status banner; exact companion `tests/big-swing/as_a1b_reduced_phase_confirm.py` | `LEAN-VERIFIED`; finite inequality, exact 96-cell corollary, and uniform-equality witness only | complete | supports C |
| E | Chi-parity no-go for orientation selection | `explorations/big-swing-2026-07-07/A2-native-ring-symmetry-nogo.md` | `LEAN-VERIFIED`; finite ordinary/weighted matrix power-trace parity only | complete | sign-selection boundary |
| F | Abstract Cartan-involution structural core | `explorations/big-swing-2026-07-06/VG-V2-fourth-seat-gauge-sector.md` | `LEAN-VERIFIED`; abstract inner-involution and commutator-parity core only | complete | quantization seat |
| G | Involution projector algebra for the mirror map | `explorations/big-swing-2026-07-06/VG-V8-t5-map-attempt.md` | `LEAN-VERIFIED`; abstract complementary-projector algebra only | complete | mirror kinematics |
| H | Extremal-weight stabilizer contains an explicit nonzero nilpotent | W243, GU-002, W244 | `LEAN-VERIFIED` for extremal annihilation and explicit square-zero blocks; stabilizer compactness and carrier lift remain structural premises | complete | compactification no-go |
| I | Supplied Shiab decomposition rows imply the complex chiral multiplicity matrix `[[0,2],[2,0]]` | `canon/shiab-existence-cl95.md`; `tests/shiab_codiff_intertwiner_dim.py` | `LEAN-VERIFIED` for the finite dimension and Schur-overlap deduction only; D7 decompositions remain supplied exact data | complete | selector non-uniqueness boundary |
| J | Schur block-kernel elimination requires an explicit inverse for `E` | VZ cycle proof gates | `LEAN-VERIFIED` as an abstract linear-map theorem; actual GU block ownership and cone invertibility remain open | complete | prevents determinant-circular VZ promotion |

## Part C: integrity-first execution order

The first three items are mandatory integrity work, not a retreat from the North Star.

1. `L0 BASELINE` — **DONE 2026-07-22**: exact pinned default target, serialized, exit 0; receipt above.
2. `L1 R4 INTEGRATION` — **DONE 2026-07-22**: proof-bearing source folded into the default target; old path
   retained as a compatibility entrypoint; post-integration build and placeholder audit required by the investigation receipt.
3. `L2 STALE DUPLICATE` — **DONE 2026-07-22**: the un-typechecked A1 draft duplicate was removed;
   `Lean/GUFormalization/LocatedNotForcedLegs.lean` is the sole authoritative certificate.
4. `L3 THEOREM H` — **DONE by `b895a49c`**: `CompactImageObstructions.lean` formalizes extremal
   annihilation and the explicit square-zero blocks. Carrier realization, Proposition 1, W235, and
   compactness remain outside the Lean conclusion; W241's false fixed-`P` implication is not formalized.
5. `L4 THEOREM A` — **DONE 2026-08-21**: finite complex-matrix achirality trace core with
   Hermiticity, anticommutation, and zero trace supplied as explicit premises.
6. `L5 THEOREM B` — **DONE 2026-08-21**: section-independent mod-3 arithmetic over `ZMod 3`,
   including the unit-charge negative control.
7. `L6 THEOREM C` — **DONE 2026-08-21**: exact rational aligned/equality/mirror-blind boundary at
   `lq = -l4/192`.
8. `L7 THEOREM D` — **DONE 2026-08-22**: source-bound finite power-mean inequality,
   exact 96-cell corollary and constant-magnitude equality witness. Spectral
   realization and A1 phase interpretation remain explicit prose/Python premises.
9. `L8 THEOREM E` — **DONE 2026-08-22**: finite matrix power-trace parity
   under involutory conjugation. Carrier faithfulness, gauge nativeness,
   vacuum selection and physical orientation remain explicit prose/Python premises.
10. `L9 THEOREMS F AND G` — **DONE 2026-08-22**: abstract inner-involution
    automorphism and even/odd commutator parity, plus complementary idempotent
    projectors for a linear involution when two is invertible. Representation
    faithfulness, Cartan positivity, maximal-compact identification, physical
    quantization, carrier selection, dynamics and spectra remain prose/Python premises.

**Post-L9 T3 correction follow-through — DONE 2026-08-22.** The prior
symbolic-only antilinear null-image result is now Lean-verified at its corrected
V15-1 ceiling. The map is explicitly star-semilinear; its two image subspaces
are complex `Submodule.map` images; total isotropy is an independent premise;
and the conclusion is only zero finite `intersectionDifference`. A mapped
negative-norm vector is a formal firing control. No physical-real-form,
Fredholm, observed-handedness, function-space, or generation-selection theorem
is claimed.

11. `L10 OLD FILE TRIAGE` — **DONE 2026-08-22 for the live certificate
    surface**: the audit no longer points to the removed runbook or maintains a
    second default-target import list. It derives all 16 imported modules from
    `Lean/GUFormalization.lean`, requires every library module to be imported or
    explicitly exempted, and enforces complete README/ledger coverage. The
    manual `ResidualSelectionAxioms.lean` receipt remains explicitly outside the
    default target and informational. Future old-file triage reopens only on a
    new concrete certificate-confusion defect.

**Post-L10 group-action classification hardening — DONE 2026-08-29.** The
set-level result now identifies the complete invariant-valuation space with
functions into the common fixed-point subtype and proves, for inhabited
domains, that invariant valuations exist exactly when that subtype is
nonempty. A dedicated axiom receipt is part of the default target. This remains
pure mathematics: no physical action, observer, dynamics, selector, carrier,
or GU verdict is constructed.

**Finite group-action census hardening — DONE 2026-08-29.** For finite domains
and codomains, the same equivalence now yields the exact cardinality
`|Inv(A,B)| = |Fix_G(B)|^|A|`. The inhabited-domain zero criterion and the
empty-domain singleton exception are separate Lean theorems, and W99 checks
swap, identity, boundary-fixed and fixed-point-free actions through domain
size zero. No physical interpretation is added.

**Regular-domain equivariance boundary — DONE 2026-08-30.** The acted-on-domain
case is now separated formally from pointwise invariance. For the regular left
`G`-torsor, evaluation at the identity is a Lean equivalence between
equivariant maps `G → B` and all values of `B`; every identity value seeds a
unique map, and finite codomains give `|Eqv(G,B)| = |B|`. W99 checks C2 swap,
C2 identity and C3 cycle controls, including the hostile fixed-point-free case
where regular equivariant maps exist despite an empty common fixed set. This is
pure set-level mathematics and supplies no physical action or physical domain action,
observer, selector, carrier or GU verdict.

**Transitive orbit–stabilizer equivariance census — DONE 2026-08-30.** For any
transitive `G`-set `A` and chosen basepoint `a₀`, Lean now identifies the
complete equivariant-map space `A → B` with values fixed by `Stab(a₀)`.
A classical transporter constructs the inverse, and a separate lemma proves
that its value is independent of the representative. Finite types satisfy
`|Eqv(A,B)| = |B^Stab(a₀)|`, and an equivariant map exists exactly when the
stabilizer-fixed subtype is inhabited. W99 tests non-free actions where the
stabilizer leaves one value, all values, or no values; the earlier regular
torsor theorem is recovered as the trivial-stabilizer case. The arbitrary-orbit
product below closes the remaining multi-orbit limitation. This theorem alone
supplies no physical action, observer, dynamics, selector, carrier or GU verdict.

**Arbitrary-orbit equivariance product — DONE 2026-08-30.** For any `G`-set
`A`, Lean now identifies the complete equivariant-map space `A → B` with the
dependent product, over `A/G`, of values fixed by the stabilizer of a chosen
orbit representative. Quotient representatives and classical transport are
explicit, and transported values are representative-independent. Finite types
satisfy the exact product census
`|Eqv(A,B)| = product_[omega in A/G] |B^Stab(a_omega)|`; existence is
equivalent to every orbit factor being inhabited. W99 tests a mixed free/fixed
action, two fixed orbits with no seed, a regular-plus-coset action with one
empty factor, and the empty-domain empty product. The earlier transitive and
regular-torsor theorems are recovered as one-orbit cases. This remains pure
set-level mathematics and supplies no physical action, observer, dynamics,
selector, carrier or GU verdict.

**Orbit-representative and quotient closed forms — DONE 2026-08-30.** Lean now
constructs the action-induced equivalence between the stabilizer-fixed seed
types at `a` and `g • a`, making representative-independent factor cardinality
explicit. For free domain actions and, separately, trivial codomain actions,
the complete equivariant-map space is equivalent to the ordinary function
space `A/G -> B`; finite types satisfy `|Eqv(A,B)| = |B|^|A/G|`, and on an
inhabited domain maps exist exactly when `B` is inhabited. W99 checks transport
on free and fixed orbits, two free-orbit families, mixed and nonfree domains,
and the empty quotient with empty codomain. The axiom receipt adds no dependency
beyond the existing standard `propext`, `Classical.choice` and `Quot.sound`
surface. This remains pure set-level mathematics and supplies no physical
action, observer, dynamics, selector, carrier or GU verdict.

**Equivariant bifunctoriality and orbit naturality — DONE 2026-08-30.** Lean
now constructs the postcomposition equivalence on complete equivariant-map
spaces induced by an equivariant codomain equivalence, together with explicit
transport of common-fixed and point-stabilizer-fixed seed subtypes. An
equivariant domain equivalence induces an explicit equivalence `A/G ~= C/G`
without choosing orbit representatives, preserves finite orbit count, and its
precomposition map commutes with codomain postcomposition. W99 tests a
nontrivial codomain relabeling, all seed factors on a mixed free/fixed action,
the transported orbit partition and the commuting square. The axiom receipt
adds no dependency beyond the existing standard `propext`,
`Classical.choice` and `Quot.sound` surface; the new orbit transport selects no
orbit representatives. This remains pure set-level mathematics and supplies no physical
action, observer, dynamics, selector, carrier or GU verdict.

**Indexed-codomain product preservation — DONE 2026-08-30.** Lean now proves
that equivariant maps into an arbitrary dependent product of acted-on
codomains are exactly indexed families of equivariant component maps. The
common-fixed and every point-stabilizer-fixed seed subtype decompose through
the same product; finite indexes have exact multiplicative cardinalities and
existence is coordinatewise, with classical choice explicit for arbitrary
index families. W99 checks a heterogeneous two-component action, free and
fixed stabilizers, the unique empty-index map and annihilation by an empty
component factor. The axiom receipt adds nothing beyond the established
`propext`, `Classical.choice` and `Quot.sound` surface. This remains pure
set-level mathematics and supplies no physical action, observer, dynamics,
selector, carrier or GU verdict.

**Global subgroup Mackey decomposition — DONE 2026-08-30.** For subgroups
`H K <= G`, Lean defines the explicit left-right action
`(k,h).g = k*g*h^-1` and proves that the `K`-orbit quotient of the restricted
induced point carrier `Res_K^G Ind_H^G(1)` is equivalent to the single
double-coset quotient `K\\G/H`. The stabilizer of `[g,star]` is exactly the
transported intersection subgroup defined by the witness equation
`k*g = g*h`; quotient equality is unpacked to an actual `h : H`, not inferred
from a count. For every supplied `H`-set `B` and representative `g`, Lean then
defines the transported action through `g^-1*k*g : H`, induces it from
`K ∩ gHg^-1` to `K`, and proves `[k,b] |-> [k*g,b]` is an injective,
`K`-equivariant equivalence onto exactly the classes admitting a representative
`[k*g,b]`. W99 checks the nonnormal `S3` example with a nontrivial two-point
seed: the full- and trivial-intersection representatives give disjoint two- and
four-class summands. Lean now chooses one representative of every explicit
double-coset class, forms the dependent coproduct of all such summands, and
proves `[q,[k,b]] |-> [k*g_q,b]` is a `K`-equivariant equivalence with the
complete restricted induction. The proof exposes the classical choice,
double-coset index and actual `K × H` quotient witnesses. W99 checks that its
chosen nonnormal `S3` representatives assemble bijectively and equivariantly
onto all six classes. Lean also proves the stronger canonical partition: the
actual fibers of the intrinsic double-coset index are `K`-stable, and their
dependent coproduct is explicitly and `K`-equivariantly equivalent to the
complete restricted induction without calling the representative selector.
The comparison back to transported-intersection summands retains the declared
classical choice. W99 checks the intrinsic fibers partition and remain stable
before representatives are chosen. This remains pure supplied-action mathematics and
constructs no physical action, carrier, observer, dynamics, selector or GU
verdict.

**Free-module Mackey linearization — DONE 2026-08-31.** Lean applies the free
finitely-supported `R`-module functor to the canonical representative-free
Mackey carrier equivalence. The resulting linear equivalence maps each basis
vector to its assembled restricted-induced class, preserves exact support
cardinality, and intertwines both linearized equivariant seed maps and the
explicit supplied `K`-actions. W99 checks these laws on the nonnormal `S3`
control and rejects a noninjective hostile basis collapse. This is a genuine
linear-algebra strengthening of the carrier theorem, but it is not an additive
Mackey functor on physical representations and supplies no source action,
coupling, coefficient, selector or GU verdict.

**Mackey permutation-representation equivalence — DONE 2026-08-31.** Lean now
bundles the free modules on the canonical coproduct and restricted-induced
carrier as genuine `K`-representations and proves canonical assembly is an
equivalence of those representations. Over every commutative semiring the
intertwiner is equivalently an isomorphism of modules over `R[K]`. W99 checks
the identity and multiplication laws, every basis intertwining square in the
nonnormal `S3` control and a hostile nonbijective generator that fails the C2
law. This is the structured-representation strengthening expressly required
to reopen the theorem family; it remains free permutation algebra on supplied
set actions, not an additive Mackey functor on physical representations, and
supplies no source action, coupling, coefficient, selector or GU verdict.

**Categorical Mackey natural isomorphism — DONE 2026-08-31.** Lean packages
the representative-free coproduct and restricted induction as functors from
supplied `H`-actions to supplied `K`-actions and proves canonical assembly is
a natural isomorphism. Mathlib's standard free-linearization functor transports
that isomorphism to the corresponding representation functors over any
commutative ring. W99 checks identity, composition and the full nonnormal-`S3`
naturality square. This is the stronger categorical reopening condition; it is
not an additive Mackey functor on physical representations and supplies no
source action, coupling, coefficient, selector or GU verdict.

**Raw-action additivity obstruction — DONE 2026-08-31.** Lean proves that
the ordinary category of supplied group actions has no morphism from the
nonempty one-point trivial action to the empty trivial action. Since a
preadditive category supplies a zero morphism between every pair of objects,
the raw action category cannot be preadditive; a zero object is excluded by
the same witness. Thus the existing Mackey natural isomorphism is not itself
an additive Mackey functor. A genuine successor must separately own an
additive span/Burnside-style completion, restriction and transfer data, and
their double-coset compatibility. This is a constructive categorical boundary,
not a no-go for such completions and not a physical claim.

**Free preadditive Mackey envelope — DONE 2026-08-31.** Lean now uses
Mathlib's free integer-linear category to add formal sums to every supplied-
action hom-set, lifts arbitrary functors and natural isomorphisms, and applies
that lift to the canonical representative-free Mackey natural isomorphism.
The raw point-to-empty hom-set becomes exactly the singleton formal zero, but
no original action map is manufactured. W99 checks coefficientwise additivity
and this empty-generator edge. This is a free hom additivization, not a
span/Burnside category: it supplies no new span morphisms, coproduct-as-sum
relations, restriction or transfer maps, double-coset transfer law, physical
representation, source-native action or GU verdict.

**All-object point-representable Burnside Mackey functor — DONE 2026-08-31.**
Lean applies the additive covariant representable functor `Hom(point,-)` to
the completed finite supplied-action Burnside span category. Graph spans give
named transfers and converse graphs give named restrictions; their identity
and composition laws are explicit. For the canonical equivariant pullback of
two action maps, Lean identifies the two composite spans and obtains the
Beck-Chevalley restriction-transfer equality. W99 checks the corresponding
integer-valued finite-set calculation and a hostile non-pullback relation.
This is one representable fixed-`G` functor, not a classification, a
nonrepresentable target-category functor, subgroup-change coherence, a
physical/source realization, or a GU verdict.

**Additive Burnside span categorical restriction — DONE 2026-08-31.** Lean
now restricts finite supplied-action spans along arbitrary group
homomorphisms, proves restriction preserves the finite pullback apex,
disjoint-coproduct addition and completed bilinear composition, and packages
the result as an additive functor between completed Burnside span categories.
Graph and converse-graph generators are preserved; identity and iterated
restriction are coherent on supplied actions and equivariant maps. W99 checks
the finite pullback carrier and diagonal restricted action and rejects a mixed
homomorphism mutation. This is categorical restriction only: ordinary
induction is not promoted because it does not generally preserve pullbacks,
and no biset/correspondence Mackey 2-functor, physical/source realization or GU
verdict is constructed.

**Source-native observation and adjoint-coupling kernels — DONE 2026-08-31.**
Lean proves the general horizontal/normal gamma-kernel leakage theorem from an
explicit normal right inverse, and separately checks the supplied finite
adjoint/144 support and PS-singlet tables. The latter yields cubic `45`, no
linear PS owner, symmetric `54/210` owners and no alternating PS owner. These
certificates harden the two banked representation results without deriving
their decomposition inputs or constructing an observation quotient, action
coefficient, family selector, mass, prediction or GU verdict.

**Observation descent and paired real-sector criteria — DONE 2026-08-31.**
Lean proves the exact split-surjective factorization criterion for preserving
the ambient Clifford kernel, including uniqueness of the factor, and proves
that a supplied linear involution modeling conjugation and anticommuting with
chirality gives a linear equivalence of the two chirality kernels. These
theorems expose every premise and do not construct the source-owned factor,
physical quotient, scalar-antilinear real structure, Clifford representation,
observed family, action or mass.

**Corrected observed gamma-kernel projector — DONE 2026-08-31.** Lean now
constructs `P = 1 - j Gamma` from a supplied observed Clifford right inverse,
proves that its fixed space and image are exactly `ker Gamma`, proves
idempotence, and packages the complete carrier decomposition as a linear
equivalence with `ker Gamma × trace`. Composing it with any observation map
removes exactly its observed trace and changes nothing on already
gamma-traceless outputs. The exact finite Clifford control passes `23/23` and
rejects identity and wrong-sign hostile maps. The split remains supplied: Lean
does not prove source/action ownership, a physical quotient, representation
meaning, observed family, chirality, mass, prediction or GU verdict.

## Part D: lock and progress contract

On Windows, every invocation uses `lab/automation/check-lean.ps1`. Its exclusive file handle is host-local.
It does not serialize another computer or cloud runner, and it cannot technically stop a direct command from
bypassing policy. Other hosts require a runner-native single-build lock and `-j1`. No two hosts may write the
same checkout.

A run makes progress only by producing a current green baseline, integrating an existing certificate,
retiring a misleading certificate lookalike, adding a newly `LEAN-VERIFIED` kernel, repairing a
`LEAN-PARTIAL` kernel, or recording an exact faithfulness/mathlib obstruction that prevents a false theorem
from entering Lean. Do not manufacture a trivial theorem to appear busy.
**Additive coend and pairing transport — DONE 2026-08-31.**
`Lean/GUFormalization/GroupActionBurnsideAdditiveCoend.lean` presents the
all-middle restriction-correspondence coend as the free abelian group modulo
left-additivity, right-additivity and balance, and proves unique factorization
for every biadditive balanced evaluator.
`Lean/GUFormalization/CandidateCohomologyPairingTransport.lean` separately
proves left/right nondegeneracy of the descended candidate pairing is invariant
under an explicit pairing-preserving quotient equivalence. Exact controls pass
10/10 and 10/10. No source action, analytic/positive physical completion,
bicategory, ambidexterity or Mackey 2-functor is inferred.

**Additive co-Yoneda and linear candidate cohomology — DONE 2026-08-31.**
`Lean/GUFormalization/GroupActionBurnsideCoYoneda.lean` proves composition is
an additive equivalence from the all-middle coend to the actual iterated-
restriction hom group, with a canonical identity-leg inverse.
`Lean/GUFormalization/CandidateCohomologyLinear.lean` proves the existing
cycle/gauge quotient has the canonical `ker d1 / range d0` module presentation
and functorial linear chain-map descent. Exact controls pass 10/10 and 10/10.
No source action, physical state space, analytic/positive completion,
bicategory, ambidexterity or Mackey 2-functor is inferred.

## Independent chiral transport core (2026-11-25)

`Lean/GUFormalization/ChiralWeightTransport.lean` is in the default root. Its five conditional theorems verify the density residual, dimension10 arithmetic obstruction and equality, conversion through a supplied faithful evaluation, and abstract consistent rows. The universal Clifford, Hermitian-adjoint, source and domain premises live in [the written result](../../explorations/conditional-build/bet-2plus1-chiral-weight-transport-2026-11-25.md). Pinned single-thread targeted check passed; this is not a formalization of the full geometric theorem.

## Actual-solution observation and natural density (2026-11-25)

`Lean/GUFormalization/ObservationSolutionTrace.lean` adds five conditional declarations: Mathlib graph-limit nonclosability, persistence under extension, impossibility of finite bounds for arbitrarily many equal positive masses, the coarea power threshold and the trace scaling order. No `sorry` or axiom is introduced. Actual solution construction/limits, Clifford geometry, measure invariance, source domains and physical necessity remain in the independently reviewed written proofs. This is a verified conditional core, not a complete formalization or source validation. Exact controls:34 reduced Clifford/coarea checks and22 natural-density checks.

## Effective tensor symmetry and finite measures (2026-11-25)

`Lean/GUFormalization/LorentzMeasureCore.lean` verifies that the three displayed rational boosts preserve the Lorentz form and that their common fixed symmetric4x4 matrices are exactly its scalar multiples. The first targeted attempt needed the ordinary noncomputable-real definitions and explicit matrix extensionality; the corrected module passes. No proof placeholder or new axiom. This checks the actual finite matrix core, not probability compactness, integration, weak convergence, source necessity or class-C membership. Those remain independently reviewed written arguments. 37 exact controls include gauge compensation, null rotations, scalar-flat curvature and directional limits. [Proof and scope](../../explorations/conditional-build/tensor-stabilizer-normalization-2026-11-25.md).

## Slice-completion finite algebra (2026-11-25)

`Lean/GUFormalization/SliceCompletion.lean` verifies five finite matrix-algebra consequences for shifted-square intertwiners and invertible right factors. The actual varying-cone exclusion also uses written analytic/free-jet, determinant and continuity arguments; those are not formalized here. Two independent mathematical reviews and a hostile source-scope review accepted the stated internal class result. No source, physical, class-C or ledger verdict changes. The exact principal-algebra probe passed 236 controls. [Proof and scope](../../explorations/conditional-build/source-action-slice-completion-2026-11-25.md).

## Predictive-realization finite core (2026-11-25)

`Lean/GUFormalization/PredictiveRealization.lean` checks nine lemmas: finite-minor injectivity, strict norm and approximate-left-inverse injectivity, and complex involution projector identities. No proof placeholders. The Clifford classification, actual450 coefficient assembly, rational root-ball certificates, pseudodifferential induction and PDE estimates remain separately reviewed written/computational evidence. The actual contour replay passes6300 principal controls and both full450 rank certificates; this is not a physical/source verdict. [Result](../../explorations/conditional-build/source-action-predictive-realization-2026-11-25.md).

## Actual-variable completion finite core (2026-11-25)

`Lean/GUFormalization/VariableCompletion.lean`: **LEAN-VERIFIED**, eight finite matrix/complex-algebra lemmas for left Gram normalization and the actual real-action phase/charge/energy/symplectic signs. Parameterized CK, Parseval, native analytic coefficients and physical/source scope are written/reviewed hypotheses. Targeted `lake env lean` passed; no default whole-project build claim. Evidence: `explorations/conditional-build/source-action-variable-completion-2026-11-25.md`.

## Coupled constraint energy finite core (2026-11-25)

`Lean/GUFormalization/CoupledGhost.lean`: **LEAN-VERIFIED**, eight finite lemmas for signed auxiliary elimination, canonical quadratic energy, leading-sign domination and count arithmetic. Clifford blocks, moving projectors, analytic stationary branch and physical domains remain written/reviewed mathematics. Targeted `lake env lean` passed without proof placeholders; no full project rebuild claim. Evidence: `explorations/conditional-build/source-action-coupled-ghost-2026-11-25.md`.

## Finite-coupling constraint core (2026-11-25)

`Lean/GUFormalization/KappaOneConstraints.lean`: **LEAN-VERIFIED**, three finite lemmas for symmetric/skew contraction, constraint-count arithmetic and the intermediate-value sign obstruction. Targeted `lake env lean` passed without placeholders. The actual symbol/projector proof, exact root matrices, real-form transfer and PDE/physical interpretation remain separately checked written mathematics. No full project rebuild claim. Evidence: `explorations/conditional-build/source-action-kappa1-constraints-2026-11-25.md`.

## Reduced evolution finite core (2026-11-26)

`Lean/GUFormalization/ReducedEvolution.lean`: **LEAN-VERIFIED**, four finite lemmas for the noncommutative square-zero sandwich, unbounded affine rays and universal derivative jets. Targeted `lake env lean -j1` passed without placeholders. Exact native matrices, canonical-energy reduction and variable-coefficient localized-packet estimates remain reviewed written mathematics; no full PDE formalization or project rebuild claim. Evidence: `explorations/conditional-build/source-action-reduced-evolution-2026-11-26.md`.

## Actual first-graph and charged-matter finite core (2026-11-26)

`Lean/GUFormalization/GraphDomain.lean`: **LEAN-VERIFIED**, seven lemmas for graph annihilation/factored kernels, negative-energy approximation, central-current phase sign and positive-charge obstruction, and affine-tail growth. Targeted `lake env lean -j1` passed without placeholders. The actual-coefficient packet proof, null eikonal construction, native matrices and selected matter-domain theorem remain independently reviewed written mathematics. No full PDE formalization or whole-project build claim. Evidence: `explorations/conditional-build/source-action-graph-domain-2026-11-26.md`.

## Steelman and external-datum finite core (2026-11-26)

`Lean/GUFormalization/SteelmanDatum.lean`: **LEAN-VERIFIED**, four lemmas for finite coefficient descent, negative interval excluding flatness, equivalent-norm bound and vanishing boundary-term sign. Targeted compilation passed without placeholders. Native SO3 projections, root curvature, operator domains, BRST interpretation and Chern transgression remain independently reviewed mathematics; no full PDE or whole-project-build claim. Evidence: `explorations/conditional-build/source-action-steelman-datum-2026-11-26.md`.

## Current receiver finite core (2026-11-26)

`Lean/GUFormalization/CurrentReceiver.lean`: **LEAN-VERIFIED**, six finite lemmas for conjugate-charge signs, the positive-graph contradiction, norm-margin arithmetic, a work/energy counterexample and bounded difference frequency. Targeted compilation passed without placeholders. Native current coefficients, cross-Gram robustness, CK/PT domain covariance and physical propagation remain separately reviewed mathematics; no full PDE or whole-project-build certification is claimed. [Result](../../explorations/conditional-build/source-action-current-receiver-2026-11-26.md).

## Receiver strategy finite core (2026-11-26)

`Lean/GUFormalization/ReceiverStrategy.lean`: **LEAN-VERIFIED**, six finite lemmas for boost-defect arithmetic and the two owned witness failures, adjoint/kernel scalar identities and a nonzero massless-null transfer. Targeted compilation passed; analytic support, full Lorentz-domain covariance, native normal-energy/Clifford certificates and physical propagation remain separate reviewed obligations. [Result](../../explorations/conditional-build/source-action-receiver-strategy-2026-11-26.md).

## Paired response finite core (2026-11-26)

`Lean/GUFormalization/PairedResponse.lean`: **LEAN-VERIFIED**, seven finite lemmas on affine-jet subtraction, rational boost/norm arithmetic, Gram cancellation and the spin5 Casimir denominator. Targeted compilation passed; native coefficient certificates, CK covariance proof, weak PDE response and source validity are distinct obligations. [Result](../../explorations/conditional-build/source-action-paired-response-2026-11-26.md).

## Rotation rigidity finite core (2026-11-26)

`Lean/GUFormalization/RotationRigidity.lean`: **LEAN-VERIFIED**, nine finite lemmas for trace-scale cancellation, coordinate separation, injectivity, rotation transversality, conormal normalization and null unmasking. Targeted compilation passed. Analytic orbit saturation, CK existence and native naturality remain written proofs, not full Lean PDE certification. [Result](../../explorations/conditional-build/source-action-rotation-rigidity-2026-11-26.md).

## Covariant finite-jet ambiguity finite core (2026-11-26)

`Lean/GUFormalization/CovariantJetAmbiguity.lean`: **LEAN-VERIFIED**, affine measurement-kernel characterization of right inverses, arbitrary hidden parameter families, chosen-image injectivity, finite even-polynomial coefficient isolation and cutoff vanishing. Targeted compilation passed without sorry. Analytic CK filtration/existence and Lorentz covariance remain written reviewed proofs; no physical-state formalization. [Result](../../explorations/conditional-build/source-action-covariant-jet-ambiguity-2026-11-26.md).

## Petrov probability finite core (2026-11-26)

`Lean/GUFormalization/PetrovProbability.lean`: **LEAN-VERIFIED**, nine lemmas for weighted overlap double-counting, quarter/half bounds, variation discrepancy and exact quartic stabilizer substitutions. Targeted compilation passed without sorry. Properness, tightness, Petrov classification and the probability-limit theorem remain independently reviewed written mathematics. No source necessity or worldwide novelty is formalized. [Proof](../../explorations/conditional-build/petrov-probability-selection-2026-11-26.md).

## Normal tensor finite core (2026-11-26)

- Certificate: `Lean/GUFormalization/NormalTensorClass.lean`.
- Status: LEAN-VERIFIED; ten finite lemmas, targeted `lake env lean` PASS with no placeholders.
- Validated statement boundary: coefficient reality versus sharp-skew incompatibility, injective factor10 contraction and arithmetic only. Actual Clifford/representation completeness, local analytic proof and source necessity are not formalized. Two independent normal-class mathematical reviewers and hostile source review; separate independent auxiliary review.
- Owner: `explorations/conditional-build/source-normal-tensor-class-2026-11-26.md`; reproducibility: `tests/program-focus/source_normal_tensor_class_probe.py`. No physical-ledger verdict or entire-project build claim.

## Q7 propagation finite core (2026-11-26)

`Lean/GUFormalization/Q7Propagation.lean`: **LEAN-VERIFIED**, six finite lemmas for Hermitian nondegeneracy, two-row injectivity and kernel-independent source tests, with an indefinite null-vector countercontrol. Targeted compilation passed without proof placeholders; default import registered. Native parity, source binding, root boxes, quadratic autonomy and PDE/representation reasoning are separately validated, not formalized by this module. [Result](../../explorations/conditional-build/source-action-q7-propagation-2026-11-26.md).

## Complete auxiliary graph finite core (2026-11-26)

`Lean/GUFormalization/CompleteAuxiliaryGraph.lean`: **LEAN-VERIFIED**, seven finite lemmas for unique auxiliary elimination, exact two-block equivalence, formal recurrence uniqueness, commuting-map eigenspaces, the25082 remaining coefficient count and inverse-free reciprocity/kernel-energy independence. Targeted `lake env lean -j1` passed without warnings or placeholders; default import registered. Statement validation retains arbitrary supplied invertible A/M and linear B/E/D: native identification, complete root-box inverses, differential domains and obstruction estimates are separately reviewed inputs. No convergent formal series, actual PDE solution or physical quotient is formalized. [Result](../../explorations/conditional-build/source-action-full-auxiliary-map-2026-11-26.md).


## 2026-11-27 — Scalar-normal reduction finite core

`Lean/GUFormalization/ScalarNormalSchur.lean`: **LEAN-VERIFIED**, six lemmas for the moving-frame auxiliary-row cancellation, frequency-independent compression, positive/negative quadratic dominance, native du norm arithmetic and real-component sign. Targeted single-thread `lake env lean -j1` passed without warnings or placeholders; default import registered. Statement validation: the compression hypotheses, root coefficients and O(k) patch-boundary remainder are supplied and checked outside Lean. Exact triangular geometry, local analytic ODE solutions, global/physical admissibility and the full PDE are not formalized. [Result](../../explorations/conditional-build/source-action-scalar-normal-operator-2026-11-27.md).

## 2026-11-27 — On-shell dynamics finite core

`Lean/GUFormalization/OnshellDynamics.lean`: **LEAN-VERIFIED**, five lemmas for left-shear blocks, reflection preservation, positive-real entry from a trace-zero positive moment, scalar moment bounds and conservative rate arithmetic. Targeted single-thread compilation passed without warnings or placeholders; default import registered. Statement validation: supplying the native matrix/eigenvalue list, the root certificates and the actual microlocal/packet theorem remains separately reviewed mathematics. No full-PDE formalization or whole-project build claim. [Result](../../explorations/conditional-build/source-action-onshell-dynamics-2026-11-27.md).

## 2026-11-27 — Finite-loss completion core

`Lean/GUFormalization/FiniteLossCompletion.lean`: **LEAN-VERIFIED**, six lemmas: formal transport residual order, universal exponent schedule, logarithmic-power decay, shrinking observation time, vanishing-error contradiction and Sobolev-sandwich transfer. Targeted single-thread compilation passed without warnings/placeholders; default import registered. Classical PDO Taylor/tail estimates, maximal-spectrum transport, native identification and physical/source scope remain independently reviewed written inputs. No full-PDE or whole-project build claim. [Result](../../explorations/conditional-build/source-action-finite-loss-completions-2026-11-27.md).

## 2026-11-27 — Coupled support core

`Lean/GUFormalization/CoupledSupport.lean`: **LEAN-VERIFIED**, seven lemmas: rational K95 pair arithmetic, longitudinal cancellation, transverse nonzero scalar product, closure contains differences, an open ball yields local differences, an open positive cone has full difference set, and full differences force full source support. Targeted single-thread compilation passed without warnings/placeholders. Native null-kernel/vertex identification, convolution and actual physical/curved admission remain separately reviewed; no whole-project build claim. [Result](../../explorations/conditional-build/source-action-coupled-support-2026-11-27.md).

## 2026-11-27 — Matched selected-current core

`Lean/GUFormalization/SelectedJet.lean`: **LEAN-VERIFIED**, five lemmas: noncommutative Clifford right cancellation, two-frequency affine separation, affine constant cancellation, raw/skew control, and scalar Gram-perturbation threshold. Targeted single-thread compilation passed without placeholders. Native graph/CK identification, Lorentz band proof and physical normalization remain separately reviewed; no whole-project build claim. [Result](../../explorations/conditional-build/source-action-selected-jet-2026-11-27.md).

## 2026-11-27 — Packet phase arithmetic core

`Lean/GUFormalization/PacketPhase.lean`: **LEAN-VERIFIED**, four lemmas: derivative budget, inverse phase-charge cost, incompatibility of a uniform polynomial lower bound with rapid decay, and nonzero real quadrature. Targeted single-thread compilation passed without placeholders. Native CK bounds, graph composition, plateau transfer and nonstationary-phase theorem remain separately reviewed written proofs; no whole-project or full-PDE verification claim. [Result](../../explorations/conditional-build/source-action-packet-phase-2026-11-27.md).

## 2026-11-27 — Theta divergence finite cores

`Lean/GUFormalization/ThetaDivergence.lean`: **LEAN-VERIFIED**, five lemmas: symmetric self-commutator contraction, affine-connection cancellation, separated component, conditional stationary kernel, and separated leading power. Targeted single-thread compilation passed without placeholders. Native geometry, exact root certificates, analytic branch and source dictionary are separately checked/reviewed; no full-PDE formalization. [Result](../../explorations/conditional-build/source-action-theta-divergence-2026-11-27.md).

## 2026-11-27 — Endpoint on-shell finite cores

`Lean/GUFormalization/EndpointOnshell.lean`: **LEAN-VERIFIED**, five targeted single-thread checked lemmas, no placeholders/warnings. Covers on-shell elimination, zero-preserving transfer obstruction, quadratic shift, injective raising and inverse-square order-gap cost. Native geometry, root intervals, finite-jet applicability and source bridge are separately verified/reviewed; no whole-project build claimed.

## 2026-11-27 — Ratio-free Riemann-response finite cores

`Lean/GUFormalization/RiemannSilence.lean`: four targeted single-thread checked lemmas, no placeholders/warnings. Covers cubic kernel pairing, four-row coefficient elimination, restriction vanishing and zero-preserving postcomposition. Complete native representation classification, Clifford witnesses and source identification are separately proved/reviewed; no whole-project build claimed.

## 2026-11-27 — Stationary torus finite cores

`Lean/GUFormalization/StationaryTorus.lean`: **LEAN-VERIFIED**, four lemmas: antisymmetric norm count, two-component independence, positive orthogonal-gauge exclusion and impossibility of a strictly positive gap with a nonpositive witness. Targeted single-thread compilation passed without warnings or placeholders. Global bundle flow, stationary PDE, integration by parts, elliptic domain and inherited flat-PS completeness remain independently reviewed written dependencies. No full-project build or PDE formalization. [Result](../../explorations/conditional-build/bet-mass-gap-stationary-torus-2026-11-27.md).

## 2026-11-27 — Real-form transfer finite cores

`Lean/GUFormalization/RiemannRealForm.lean`: **LEAN-VERIFIED**, five finite lemmas: real-pair kernel inclusion, complex four-row elimination with arbitrary nonzero scales, joint-reference tangent radical, fixed-connection metric block and its nonzero control. Targeted single-thread compilation passed without warnings/placeholders; default import registered. Real-form/Clifford/Spin identifications, polynomial/naturality transport and the functional critical-family theorem remain separately reviewed written inputs. No full native replay, PDE formalization or full-project build. [Result](../../explorations/conditional-build/riemann-realform-transfer-2026-11-27.md).

## 2026-11-27 — Endpoint cubic finite cores

`Lean/GUFormalization/EndpointCubic.lean` registers five finite cores for the analytic-branch endpoint result: exact coefficient, extraction, polarization and conditional positivity/nonzero. Targeted check recorded in `lab/process/source-action-endpoint-cubic.json`; no full PDE/source formalization.

## 2026-11-27 — Conservation descent finite cores

`Lean/GUFormalization/ConservationDescent.lean`: **LEAN-VERIFIED**, four finite lemmas: normal-jet compensation, surjective consequence equivalence, vanishing free-jet coefficient row and flat superpotential divergence. Targeted single-thread compilation passed with one style linter warning about unnecessary tactic sequencing and no placeholders. Smooth Gaussian/ODE extension, bundle geometry and source/physical applicability remain separately reviewed written mathematics; no full-PDE or whole-project verification claim. [Result](../../explorations/conditional-build/bet-cosmology-conservation-descent-2026-11-27.md).

## 2026-11-27 — Full Shiab consistency finite cores

`Lean/GUFormalization/FullShiabConsistency.lean`: **LEAN-VERIFIED**, five finite lemmas: three cyclic maps collapse, odd scalar parity, central-matrix tests, mixed quadratic factor and central/traceless spanning. Targeted single-thread compilation passed without output or placeholders. Universal matrix-unit classification, compact variational argument, Spin/real-form and source identification remain separately reviewed written inputs; no full-project or source formalization claim. [Result](../../explorations/conditional-build/full-shiab-variational-consistency-2026-11-27.md).

## Printed endpoint separation (2026-11-27)

`Lean/GUFormalization/EndpointHessianSeparation.lean`: **LEAN-VERIFIED**, targeted single-thread check passed with no output. Finite nonzero-coefficient cancellation and rank-gap arithmetic only; irreducibility, inherited universal proof and source bridge remain written/reviewed. Evidence: `lab/process/printed-shiab-endpoint-audit.json`.

## Compact excitation charge finite cores (2026-11-27)

`Lean/GUFormalization/CompactCharge.lean` checks the abstract boundary-balance cancellation and nonnegative finite-sum implication. Smooth lifts, cutoff extensions, Stokes and physical/source applicability remain written and reviewed. See [result](../../explorations/conditional-build/compact-excitation-charge-2026-11-27.md).

## Unitary dual closure finite cores (2026-11-27)

`Lean/GUFormalization/UnitaryDualClosure.lean` proves insertion-factor projection cancellation and invertible postcomposition zero equivalence. Clifford identities, source/jet/paired-domain applicability and native rank512 remain written and reviewed premises. See [result](../../explorations/conditional-build/bet-2plus1-unitary-dual-closure-2026-11-27.md).

## Shiab derivation finite cores (2026-11-27)

`Lean/GUFormalization/ShiabDerivation.lean` proves coefficient-commutator Leibniz and two-map annihilation. Full graded/Spin classification, Riemann geometry, real-form transfer, source applicability and global group bundle proofs remain written and reviewed. See [result](../../explorations/conditional-build/shiab-graded-derivation-class-2026-11-27.md).

## Shiab companion finite cores (2026-11-27)

`Lean/GUFormalization/ShiabCompanion.lean` proves zero-preserving nonfactorization and bilinear polarization. Exterior classification, Clifford/Riemann identity, real forms, actual jets and source relevance remain written and reviewed. [Result](../../explorations/conditional-build/shiab-bianchi-companion-class-2026-11-27.md).

## Null-symbol trace finite cores (2026-11-27)

`Lean/GUFormalization/NullSymbolTrace.lean` checks trace/order arithmetic only. The exact-chain trace and source applicability remain written/reviewed. Result: `explorations/conditional-build/null-boost-symbol-trace-2026-11-27.md`.

## Finite normal-jet recurrence (2026-11-27)

`Lean/GUFormalization/NormalJetRecursion.lean` checks two finite causal recurrence lemmas. Smooth ODE existence, jet realization, support and Stokes remain written/reviewed; existing CompactCharge cores are reused. Result: `explorations/conditional-build/bet-cosmology-normal-jets-2026-11-27.md`.
