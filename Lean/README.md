# Lean Certificates

This directory contains the repo's first Lean 4 + mathlib robustness layer.

The boundary is deliberately narrow:

- Lean checks finite mathematical kernels.
- Markdown owns interpretation, source provenance, and physics scope.
- Python audits continue to parse repo artifacts and enforce process gates.

Certified files should not contain `sorry` when cited by canon or active-research
documents.

## Current Certificates

| Lean file | Scope | Owner surface |
|---|---|---|
| `GUFormalization/WedgeEinsteinReduction.lean` | Seven finite curvature-identity, moment-sign, coefficient-bound and scalar-growth lemmas; no geometry/measure/PDE realization. | `explorations/conditional-build/wedge-shiab-einstein-reduction-2026-11-27.md` |
| `GUFormalization/NormalSMCharacteristic.lean` | Nine finite Chern-coefficient, twist, divisibility and countercontrol lemmas; topology is written and reviewed. | `explorations/conditional-build/normal-sm-characteristic-constraints-2026-11-27.md` |
| `GUFormalization/PrintedEndpointBranch.lean` | Six finite recurrence, elimination, nonfactorization and rational/sign lemmas. Analytic geometry remains written and reviewed. | `explorations/conditional-build/printed-endpoint-analytic-branch-2026-11-27.md` |
| `GUFormalization/ScalarNormalSchur.lean` | Six finite lemmas for a vanishing moving-frame auxiliary row, frequency-independent compression, signed quadratic-energy dominance, native time-covector arithmetic and real-component sign. Analytic ODE existence, geometry and physical admission are separate reviewed inputs. | `explorations/conditional-build/source-action-scalar-normal-operator-2026-11-27.md` |
| `GUFormalization/CompleteAuxiliaryGraph.lean` | Seven finite lemmas for auxiliary elimination, exact block reduction, formal recurrence, invariant eigenspaces, coefficient count and inverse-free kernel-energy independence. Native inverse certificates and analytic domain exclusions are separate reviewed inputs; no propagation theorem. | `explorations/conditional-build/source-action-full-auxiliary-map-2026-11-26.md` |
| `GUFormalization/Q7Propagation.lean` | Six finite lemmas: Hermitian determinant and two-row injectivity, kernel-independent source pairing, and a null-vector control. Native parity, coupled-sector autonomy and PDE validity remain separate reviewed premises. | `explorations/conditional-build/source-action-q7-propagation-2026-11-26.md` |
| `GUFormalization/Status.lean` | Claim-status order and dependency monotonicity kernel | `lab/methods/claim-status-consistency.md` |
| `GUFormalization/K3IndexArithmetic.lean` | Symbolic K3/RS index arithmetic used by current audits | `lab/active-research/topological-generation-count-families-k3-chi-gate-2026-06-26.md` |
| `GUFormalization/W2Polynomial.lean` | Algebraic `F_2` polynomial identities behind the corrected `w2(Y14)` calculation | `canon/w2-y14-spin-structure.md` |
| `GUFormalization/LocatedNotForcedLegs.lean` | Finite located-not-forced theorem-grade legs: Krein transversality, corrected star-semilinear images with explicit null-image premises and `intersectionDifference = 0`, plus 2-primary identities. This is finite complex Hermitian image-subspace algebra only, not physical-real-form, Fredholm, observed-handedness, or generation-selection content | `canon/core-theorems-symbolic-proof-RESULTS.md`; `explorations/conditional-build/conditional-build-frontier-and-antilinear-null-images-2026-08-22.md` |
| `GUFormalization/LocatedNotForcedFiniteCore.lean` | Finite census encoding and `decide`-checked closure over supplied census data | `papers/candidates/located-not-forced/zenodo-package-v1.0.0/VERIFICATION.md` |
| `GUFormalization/ResidualSelection.lean` | Residual-selection finite logic kernels | `papers/candidates/located-not-forced/zenodo-package-v1.0.0/VERIFICATION.md` |
| `GUFormalization/GroupActionFixedPoints.lean` | Set-level group-action classification: pointwise-invariant valuations are functions into the common fixed-point subtype and have finite cardinality `|Fix(G)|^|A|`; for an arbitrary acted-on domain, equivariant maps are a dependent product of stabilizer-fixed seed values over the domain orbit quotient, giving the exact finite census `|Eqv(A,B)| = product_[omega in A/G] |B^Stab(a_omega)|`. Acting within one orbit gives explicit equivalences between conjugate-representative seed types. Equivariant changes of domain and codomain coordinates preserve the complete map and fixed-seed spaces; domain transport induces an explicit equivalence of orbit quotients, and domain precomposition commutes with codomain postcomposition. Equivariant maps into an arbitrary indexed product of acted-on codomains are exactly indexed families of component equivariant maps; common-fixed and stabilizer-fixed seed spaces, finite counts and existence decompose by the same product. When every point stabilizer imposes one common fixed-value condition, the orbit product reduces to `|B^H|^|A/G|`; free-domain and trivial-codomain actions are the basic specializations. The transitive and regular left-torsor theorems are one-orbit special cases. No physical action or GU verdict is encoded | `VERIFICATION.md` |
| `GUFormalization/GroupActionCoproducts.lean` | Dual set-level structure: equivariant maps out of an arbitrary indexed coproduct with the fiberwise Sigma action are indexed families of component equivariant maps, with exact finite product counts and existence. The action fixes the index and does not model index transport or mixing | `VERIFICATION.md` |
| `GUFormalization/EquivariantInternalHom.lean` | Closed set-level structure: the explicit conjugation action `(g.f)(a) = g.f(g^-1.a)` has equivariant maps as its common fixed points, and diagonal-product equivariant maps satisfy the curry/uncurry exponential law. The action is named rather than globally installed | `VERIFICATION.md` |
| `GUFormalization/GroupActionChangeOfGroups.lean` | Change-of-groups structure for supplied set actions: explicit restriction along `H ->* G`, exact recovery under surjectivity, and a right-translation coinduced action satisfying `Hom_H(Res A,B) ~= Hom_G(A,Coind B)`. All added actions are named rather than globally installed | `VERIFICATION.md` |
| `GUFormalization/GroupActionInduction.lean` | The complementary set-level left adjoint: `Ind_phi B` is the orbit quotient `G ×_H B` with explicit descended left action, and `Hom_G(Ind B,C) ~= Hom_H(B,Res C)`. Equivariant seed maps descend functorially, preserving identities, composition and `G`-equivariance. Quotient orientation and all actions are explicit and non-global | `VERIFICATION.md` |
| `GUFormalization/GroupActionInductionCoherence.lean` | Unit and composition coherence for the balanced-product construction: `Ind_id B ~= B` and `Ind_(psi.comp phi) B ~= Ind_psi (Ind_phi B)` as explicit equivariant equivalences. Both quotient layers and the flattening order are checked | `VERIFICATION.md` |
| `GUFormalization/GroupActionMackey.lean` | Complete set-level Mackey decomposition for subgroup induction: the `K`-orbit quotient of `Res_K^G Ind_H^G(1)` is `K \\ G / H`; each supplied `H`-set summand is `K ×_(K ∩ gHg⁻¹) {}^gB`; intrinsic index fibers form a canonical representative-free `K`-equivariant coproduct decomposition; equivariant seed maps preserve those fibers naturally; representative changes are explicit; and `Hom_K(Res Ind B,C)` is equivalent to the dependent family of transported-intersection seed-map spaces | `VERIFICATION.md` |
| `GUFormalization/GroupActionMackeyLinearization.lean` | Free-module lift of the canonical Mackey carrier equivalence: basis vectors and support cardinality are preserved, and the lift intertwines linearized seed maps and the supplied `K`-actions. This is not an additive Mackey functor on physical representations | `VERIFICATION.md` |
| `GUFormalization/GroupActionMackeyRepresentations.lean` | Bundled permutation-representation strengthening: the free modules carry genuine `K`-representations, canonical assembly is a representation equivalence, and over a commutative semiring it is an `R[K]`-module isomorphism. All actions remain freely generated from supplied sets, not physical representations | `VERIFICATION.md` |
| `GUFormalization/GroupActionMackeyCategory.lean` | Categorical strengthening: the representative-free Mackey construction and restricted induction are functors on supplied actions, canonical assembly is a natural isomorphism, and Mathlib linearization transports it to a natural isomorphism of representations. This does not construct an additive or physical Mackey functor | `VERIFICATION.md` |
| `GUFormalization/GroupActionMackeyAdditivityBoundary.lean` | Exact semantic boundary: the ordinary category of supplied group actions has no point-to-empty morphism and therefore admits neither a preadditive structure nor a zero object. The current Mackey natural isomorphism cannot itself be an additive Mackey functor; an additive span/Burnside-style completion and transfer data remain separate missing structure | `VERIFICATION.md` |
| `GUFormalization/GroupActionAdditiveEnvelope.lean` | Free integer-linear envelope of the supplied-action category: functors and natural isomorphisms lift linearly, so the canonical Mackey natural isomorphism has a preadditive-envelope lift. The point-to-empty hom becomes the singleton formal zero without creating an original action map. This is not a span/Burnside category and supplies no transfer data | `VERIFICATION.md` |
| `GUFormalization/GroupActionBurnside.lean` | Additive Burnside group of finite supplied actions: equivariant equivalence is quotiented, disjoint coproduct is addition, subgroup restriction and induction descend to additive homomorphisms, and the finite transported-intersection coproduct satisfies the Mackey double-coset identity. This is supplied-action algebra, not a physical representation category or source-native action | `VERIFICATION.md` |
| `GUFormalization/GroupActionSpanCategory.lean` | Category of finite supplied-action spans: arbitrary equivariant spans are quotiented by equivariant apex isomorphism, identity is the diagonal span, composition is finite equivariant pullback, explicit unitors/associator prove the category laws, and graph spans embed ordinary equivariant maps while converse graphs supply the transfer direction. No separate categorical universal property is claimed; this is not yet an additive/preadditive Burnside category or a physical/source realization | `VERIFICATION.md` |
| `GUFormalization/GroupActionBurnsideSpanCategory.lean` | Additive completion of the finite supplied-action span category: disjoint coproduct gives homwise commutative monoids, pullback composition distributes in both variables, and homwise Grothendieck completion yields a preadditive category. Graph and converse-graph generators remain explicit. The point-endomorphism Mackey law is supplied separately; no category-valued or physical/source Mackey functor is inferred here | `VERIFICATION.md` |
| `GUFormalization/GroupActionBurnsideSpanMackey.lean` | Identifies the additive Burnside group with the completed endomorphism group of the trivial point action, transports subgroup restriction and induction to those point-endomorphism groups, and proves the Mackey double-coset identity there. This is not a category-valued or physical Mackey functor | `VERIFICATION.md` |
| `GUFormalization/GroupActionBurnsideMackeyFunctor.lean` | Defines the additive point-representable functor `A ↦ Hom(point,A)` on every completed Burnside span object, with named graph transfers, converse-graph restrictions, identity/composition laws, and canonical-pullback Beck-Chevalley. This is one fixed-`G` representable functor, not a classification, subgroup-change theory, or physical/source realization | `VERIFICATION.md` |
| `GUFormalization/GroupActionBurnsideSpanRestriction.lean` | Restricts completed finite-action Burnside span categories along a supplied group homomorphism. The additive functor preserves pullback composition, identities, graph and converse-graph generators, and homwise addition. This is categorical restriction, not categorical induction or a physical/source realization | `VERIFICATION.md` |
| `GUFormalization/GroupActionBurnsideSpanCorrespondence.lean` | Correctly typed additive companion `Hom_H(A, Res B)` for categorical restriction. Precomposition by H-spans and postcomposition by restricted K-spans are additive, commute, and retain graph generators from the set-action induction/restriction adjunction. This is a correspondence, not an induction functor on span categories | `VERIFICATION.md` |
| `GUFormalization/GroupActionBurnsideAdditiveCoend.lean` | Additive-group-valued coend presentation: the free abelian group on all-middle restriction-correspondence pairs is quotiented by left-additivity, right-additivity and arbitrary-middle balance, with existence and uniqueness for every biadditive balanced evaluator. This is not a biset bicategory, ambidexterity theorem, Mackey 2-functor or physical/source realization | `explorations/group-action-burnside-additive-coend-2026-08-31.md` |
| `GUFormalization/GroupActionBurnsideCoYoneda.lean` | Additive co-Yoneda equivalence: composition identifies the all-middle additive coend with the actual iterated restriction-correspondence hom group; the inverse uses the canonical middle object and identity second leg. This is hom-group algebra, not a biset bicategory or Mackey 2-functor | `explorations/group-action-burnside-co-yoneda-2026-08-31.md` |
| `GUFormalization/CandidateCohomologyPairingTransport.lean` | Proves left and right nondegeneracy of supplied descended candidate-cohomology pairings are invariant under an explicit zero- and pairing-preserving equivalence of quotient presentations. The equivalence is supplied algebraic data, not a source-selected physical isometry | `explorations/candidate-cohomology-pairing-transport-2026-08-31.md` |
| `GUFormalization/CandidateCohomologyLinear.lean` | Identifies the representative cycle/gauge quotient with the canonical module quotient `ker d1 / range d0`, and proves every supplied chain map descends linearly compatibly. This is not a source-selected complex or physical state space | `explorations/candidate-cohomology-linear-quotient-2026-08-31.md` |
| `GUFormalization/SourceNativeSpin64Observation.lean` | General linear-algebra certificate: an invertible normal Clifford component lifts every nonzero horizontal trace to the ambient gamma kernel while literal observation pullback retains the nonzero observed trace. No physical quotient or generation sector is constructed | `explorations/source-native-spin64-observation-sector-obstruction-2026-08-30.md` |
| `GUFormalization/SourceNativeObservationDescent.lean` | Split-surjective descent criterion: observation preserves the ambient Clifford kernel exactly when observed contraction factors uniquely through ambient contraction. The factor is explicit, but no source-owned or physical bridge is constructed | `explorations/source-native-spin64-observation-sector-obstruction-2026-08-30.md` |
| `GUFormalization/SourceNativeCorrectedObservation.lean` | For a supplied right inverse to observed Clifford contraction, constructs the canonical trace-subtraction projector, proves the observed carrier is linearly equivalent to gamma kernel times trace carrier, and corrects any observation map into that kernel. The correction is algebraic and is not source-owned or a physical quotient | `explorations/source-native-corrected-observation-projector-2026-08-31.md` |
| `GUFormalization/SourceNativeCorrectedObservationNaturality.lean` | Makes split dependence exact, proves equal projectors iff supplied right inverses agree, and proves projector/corrected-observation naturality under contraction and split intertwiners; no source-selected split or physical quotient is constructed | `explorations/source-native-split-naturality-and-burnside-correspondence-composition-2026-08-31.md` |
| `GUFormalization/GroupActionBurnsideSpanCorrespondenceComposition.lean` | Composes additive restriction correspondences by restricting the second completed span, with bilinearity, outer-action, and graph-generator laws; not categorical induction, a coend classification, or a full Mackey 2-functor | `explorations/source-native-split-naturality-and-burnside-correspondence-composition-2026-08-31.md` |
| `GUFormalization/SourceNativeRealSector.lean` | Abstract real-sector criterion: a supplied linear involution modeling conjugation and anticommuting with chirality gives a linear equivalence between the positive and negative chirality kernels. A scalar-antilinear real structure, Clifford representation and physical interpretation are not constructed | `explorations/source-native-spin64-observation-sector-obstruction-2026-08-30.md` |
| `GUFormalization/SourceNativeAdjointCoupling.lean` | Finite supplied-multiplicity certificate for the adjoint/144 degree ladder: cubic 45 availability, linear PS obstruction, and exact symmetric 54/210 versus alternating 45/945 quadratic owner split. No source coefficient, family selector, or mass is constructed | `explorations/source-native-adjoint-144-coupling-classification-2026-08-31.md` |
| `GUFormalization/SourceNativeFamilyOwnerIdentifiability.lean` | Separates family and quadratic-owner identifiability: exchange invariance forces equal coefficients on equivalent family copies and forbids selecting one copy, while explicit invariant 54-only and 210-only packets prove that family symmetry does not choose the owner axis | `explorations/source-native-family-owner-and-burnside-correspondence-wave-2026-08-31.md` |
| `GUFormalization/SourceCoefficientRank.lean` | Generic homogeneous coefficient-rank discriminator plus the strict frozen-source instantiation: uniqueness is injectivity, any nonzero kernel direction gives a second solution, and the zero strict-source constraint leaves distinct 54-axis and 210-axis packets | `explorations/source-coefficient-packet-rank-certificate-2026-08-31.md` |
| `GUFormalization/SourceNativeActionObservationComplex.lean` | Smallest three-stage gauge→field→equation complex, an actual middle-cycle subtype quotiented by gauge equivalence, cycle-restricted descent for chain maps, exact compatibility laws welding the supplied split-corrected observation into a chain map, and packet-relative nonselection of any injectively parameterized action family | `explorations/source-native-action-observation-complex-2026-08-31.md` |
| `GUFormalization/ExternalInputInterface.lean` | Exact conditional interface theorem: a supplied classifier of admitted external inputs into tagged tiebreaker/free-setting codes has an exact decoder iff it is bijective, with no-missing-port, no-overlap, unique-code, automorphism, planted-third-type and hidden-order controls. No exhaustive GU input carrier or classifier is constructed | `explorations/external-input-interface-equivalence-2026-08-31.md` |
| `GUFormalization/GroupActionBurnsideBisetCoend.lean` | Fixed-middle and all-intermediate-object balance quotients for restriction correspondences, descended composition, three-stage coherence, and set-valued balanced-evaluator factorization/uniqueness. This is not an additive/category-valued coend, biset bicategory, ambidexterity or Mackey 2-functor | `explorations/group-action-burnside-biset-coend-2026-08-31.md`; `explorations/group-action-burnside-all-middle-coend-2026-08-31.md` |
| `GUFormalization/CandidateCohomologyPairing.lean` | Two-sided gauge-basic bilinear descent through the actual middle cycle/gauge quotient, with exact iff criteria between left/right quotient nondegeneracy and the corresponding cycle radical being gauge | `explorations/candidate-cohomology-pairing-criterion-2026-08-31.md` |
| `GUFormalization/GroupActionFixedPointsAxioms.lean` | Default-target `#print axioms` surface for the complete group-action theorem family | `VERIFICATION.md` |
| `GUFormalization/R4TwoArena.lean` | Two-arena weight-parity, CRT, and 2-primary-blindness proof legs | `canon/two-arena-rep-theory-core-RESULTS.md` |
| `GUFormalization/CoflipCore.lean` | Co-flip finite core (CH-REC P1/P2): (1,1) Krein toy rigidity, zero-import diagonal action, split-costs-one, split parity | `explorations/hardening-h2-lean-coflip-2026-07-19.md` |
| `GUFormalization/CoflipAbstract.lean` | Abstract `(eps,mu)` co-flip sign accounting: zero-import diagonal, exact one-bit split price. The `FiniteSignature` field and the `witnessed` Prop are carried but formally inert — no proof uses them (descoped 2026-08-03) | `explorations/hardening-h1-exhaustiveness-2026-07-19.md`; `explorations/hardening-h4-class-generalization-2026-07-19.md` |
| `GUFormalization/CompactImageObstructions.lean` | Extremal-weight annihilation and explicit square-zero-block kernels; carrier faithfulness and compactness remain outside Lean | `papers/candidates/good-stable-compactification-no-go/REPRODUCE.md` |
| `GUFormalization/CompactImageObstructionsAxioms.lean` | Default-target `#print axioms` surface for the compact-image kernels | `papers/candidates/good-stable-compactification-no-go/REPRODUCE.md` |
| `GUFormalization/FiniteResearchKernels.lean` | Finite achirality-trace, mod-3, and rational phase-boundary kernels | `lab/process/lean-verification-lane-LEDGER.md` |
| `GUFormalization/ShiabMultiplicityCertificate.lean` | Finite Schur-overlap deduction from the supplied D7 decomposition rows: chiral selector matrix `[[0,2],[2,0]]`, full-Dirac total `4`, and non-uniqueness of the natural complex block. The module does not construct the decomposition or select a physical Shiab | `canon/shiab-existence-cl95.md`; `explorations/shiab-operator/shiab-codiff-intertwiner-dim-2026-06-26.md` |
| `GUFormalization/VZSchurPrecondition.lean` | Determinant-free block-kernel elimination with the `E`-block left inverse and Schur-complement injectivity explicit in the theorem statement. It does not identify the blocks with GU's actual operator or close FC-VZ-1 | `explorations/cycle-gates-and-audits/cycle1-vz-subprincipal-eblock-proof-gate-2026-06-24.md` |
| `GUFormalization/FiniteResearchKernelsAxioms.lean` | Default-target `#print axioms` surface for the finite research kernels | `lab/process/lean-verification-lane-LEDGER.md` |
| `GUFormalization/PowerMeanReduction.lean` | Finite Cauchy--Schwarz/power-mean kernel, exact 96-cell corollary, and constant-magnitude equality witness; no spectral or physics realization is encoded | `explorations/big-swing-2026-07-07/A1-native-potential-alignment.md`; `explorations/conditional-build/conditional-build-frontier-and-l7-power-mean-2026-08-22.md` |
| `GUFormalization/ChiConjugationTraceParity.lean` | Finite matrix proof that ordinary power traces are even and traces weighted by a conjugation-odd matrix are odd under an involution; no carrier, gauge, vacuum, or physical-orientation realization is encoded | `explorations/big-swing-2026-07-07/A2-native-ring-symmetry-nogo.md`; `explorations/conditional-build/conditional-build-frontier-and-l8-chi-parity-2026-08-22.md` |
| `GUFormalization/InvolutionProjectorKernels.lean` | Abstract inner-involution automorphism and commutator parity, plus complementary linear involution projectors; no carrier, Cartan positivity, maximal-compact, dynamics, spectrum, or physical-sector realization is encoded | `explorations/big-swing-2026-07-06/VG-V2-fourth-seat-gauge-sector.md`; `explorations/big-swing-2026-07-06/VG-V8-t5-map-attempt.md`; `explorations/conditional-build/conditional-build-frontier-and-l9-involution-projectors-2026-08-22.md` |
| `GUFormalization/PacketLocalPositiveCone.lean` | Proves that a sign-invariant pointed subset of an additive carrier is trivial, that a raw linear-map range on a nontrivial carrier cannot itself be both pointed and generating, and that a phase-preserved cone whose phase map squares to negation has the same obstruction. This is a selection boundary for raw linear carriers, not a no-go for quadratic/ray extensions or a GU-native state construction | `explorations/conditional-build/k77-packet-local-positive-state-extension-wave-2026-09-01.md`; `VERIFICATION.md` |
| `GUFormalization/MetricNormalGradingCore.lean` | Conditional pairing/linear-map core: a selfadjoint shape cannot equal a skew connection on a nondegenerate pairing; supplied faithful Clifford residual and nonzero coefficients retain the defect. No geometric connection, domain or physical grade is constructed. | `explorations/conditional-build/metric-normal-family-grading-2026-11-24.md` |
| `GUFormalization/ObservedHiddenPremise.lean` | Integer cancellation from supplied same-grading additivity and total balance, plus the supplied closed-comparison coefficients. Source non-chirality is not proved to supply those analytic premises. | `explorations/conditional-build/zero-total-grading-premise-2026-11-20.md` |
| `GUFormalization/ObservedHiddenSplit.lean` | Finite six-term exact-sequence index additivity and its balanced-total corollary. Exactness, Fredholm realization and physical grading remain supplied obligations. | `explorations/conditional-build/native-descending-grading-classification-2026-11-21.md` |
| `GUFormalization/ProvenanceMixing.lean` | Finite rational six-slot evolution and trace/remainder/scalar mixing checks. No Clifford, PDE, action or physical-family claim. | `explorations/conditional-build/bet-2plus1-provenance-observation-2026-11-11.md` |
| `GUFormalization/SixSpinorGrading.lean` | Conditional finite algebra for receiver uniqueness, quotient oddness and an injective torsion witness, with coefficients, geometric identities and descent supplied. No source-owned physical grading or analytic domain. | `explorations/conditional-build/six-spinor-grading-compatibility-2026-11-24.md` |
| `GUFormalization/SourceClassCore.lean` | Rank lower bound and six-slot minimum from supplied kernel containment and dimensions15s/9s. Spin invariant theory, completeness, source necessity and physical observation domains are outside Lean. | `explorations/conditional-build/source-natural-symbol-class-2026-11-24.md` |
| `GUFormalization/ThreeLocalFloor.lean` | Finite additive/character algebra distinguishing virtual C2 representations from ZMod2 and showing a mod3 character does not factor through forgotten rank. No topology or native datum floor is formalized. | `explorations/conditional-build/x-d1-p3-three-local-floor-2026-11-11.md` |
| `GUFormalization/WeldCoefficientScope.lean` | Phase propagation along a supplied connected relation and an incompatible two-cycle coefficient control. No class-C action, source coefficient or geometric realization. | `explorations/conditional-build/x-p1-p2-class-c-lift-2026-11-11.md` |

| `GUFormalization/ChiralWeightTransport.lean` | Conditional density residual, dimension10 obstruction, faithful supplied evaluation and consistent density rows. Clifford/source/domain hypotheses are supplied; no GU theorem. | `explorations/conditional-build/bet-2plus1-chiral-weight-transport-2026-11-25.md` |

## Standalone Lean Certificates

| Lean file | Scope | Owner surface |
|---|---|---|
| `GUFormalization/ResidualSelectionAxioms.lean` | Manual, informational `#print axioms` receipt outside the default target; run with `lake env lean` | `lab/process/lean-verification-lane-LEDGER.md` |
| `tests/big-swing/R4_TwoArena.lean` | Compatibility entrypoint importing the default-target R4 module | `canon/two-arena-rep-theory-core-RESULTS.md` |

## Local Commands

After installing Lean/elan, run from the repository root. Fetch the cache for
the committed dependencies when needed:

```powershell
lake exe cache get
```

The committed `lake-manifest.json` is the dependency lock.  Do not run
`lake update` as a routine reproduction step: the mathlib input tracks
`master`, so an update can advance both the manifest revision and the required
Lean toolchain.  Use it only when intentionally updating and reviewing the pin.

For a single-threaded targeted check with matching compiled imports already
available:

```sh
lake env lean -j1 Lean/GUFormalization.lean
```

This checks the entrypoint against the available imports; it does not rebuild
or recheck their source. To verify changed modules, check them sequentially in
dependency order with `lake env lean -j1 -o <module-output.olean> <source.lean>`
before checking the entrypoint, using an isolated build cache. Record the exact
files and retained dependency cache in the receipt. This is a targeted check,
not a fresh full default-target build.

`lake build` remains the full default-target command. The pinned Lake does not
provide the old `lake build -j1` option, and `-Kjobs=1` only sets an unused
package configuration value here; neither limits build concurrency. Lean's
`-j1` above is an actual thread option. Run heavy checks one at a time under the
workspace's local resource convention.

On Windows, the existing wrapper prevents overlapping GU build invocations
(it does not limit the threads or subprocesses inside one build):

```powershell
.\lab\automation\check-lean.ps1 -Cache
```

The `-Update` switch is reserved for an intentional dependency/toolchain upgrade;
it is not a reproduction step.

The process gate `process_gates/lean_certificate_surface_audit.py` derives the
default-target certificate inventory from `GUFormalization.lean`, requires
every library module to be imported or explicitly declared as a manual
non-default certificate, and checks the Lean map, ledger, owner references, and
proof-body placeholder hygiene. It is a routing and governance gate, not a
replacement for `lake build` or targeted standalone Lean checks.

## Actual-solution observation and natural density (2026-11-25)

`GUFormalization/ObservationSolutionTrace.lean` adds five conditional declarations: Mathlib graph-limit nonclosability, persistence under extension, impossibility of finite bounds for arbitrarily many equal positive masses, the coarea power threshold and the trace scaling order. No `sorry` or axiom is introduced. Actual solution construction/limits, Clifford geometry, measure invariance, source domains and physical necessity remain in the independently reviewed written proofs. This is a verified conditional core, not a complete formalization or source validation. Exact controls:34 reduced Clifford/coarea checks and22 natural-density checks.

## Effective tensor symmetry and finite measures (2026-11-25)

`GUFormalization/LorentzMeasureCore.lean` verifies that the three displayed rational boosts preserve the Lorentz form and that their common fixed symmetric4x4 matrices are exactly its scalar multiples. The first targeted attempt needed the ordinary noncomputable-real definitions and explicit matrix extensionality; the corrected module passes. No proof placeholder or new axiom. This checks the actual finite matrix core, not probability compactness, integration, weak convergence, source necessity or class-C membership. Those remain independently reviewed written arguments. 37 exact controls include gauge compensation, null rotations, scalar-flat curvature and directional limits. [Proof and scope](../explorations/conditional-build/tensor-stabilizer-normalization-2026-11-25.md).

## Slice-completion finite algebra (2026-11-25)

`GUFormalization/SliceCompletion.lean` verifies five finite matrix-algebra consequences for shifted-square intertwiners and invertible right factors. The actual varying-cone exclusion also uses written analytic/free-jet, determinant and continuity arguments; those are not formalized here. Two independent mathematical reviews and a hostile source-scope review accepted the stated internal class result. No source, physical, class-C or ledger verdict changes. The exact principal-algebra probe passed 236 controls. [Proof and scope](../explorations/conditional-build/source-action-slice-completion-2026-11-25.md).

## Predictive-realization finite core (2026-11-25)

`GUFormalization/PredictiveRealization.lean` checks nine lemmas: finite-minor injectivity, strict norm and approximate-left-inverse injectivity, and complex involution projector identities. No proof placeholders. The Clifford classification, actual450 coefficient assembly, rational root-ball certificates, pseudodifferential induction and PDE estimates remain separately reviewed written/computational evidence. The actual contour replay passes6300 principal controls and both full450 rank certificates; this is not a physical/source verdict. [Result](../explorations/conditional-build/source-action-predictive-realization-2026-11-25.md).

## Actual-variable completion finite core (2026-11-25)

`GUFormalization/VariableCompletion.lean`: **LEAN-VERIFIED**, eight finite matrix/complex-algebra lemmas for left Gram normalization and the actual real-action phase/charge/energy/symplectic signs. Parameterized CK, Parseval, native analytic coefficients and physical/source scope are written/reviewed hypotheses. Targeted `lake env lean` passed; no default whole-project build claim. Evidence: `explorations/conditional-build/source-action-variable-completion-2026-11-25.md`.

## Coupled constraint energy finite core (2026-11-25)

`GUFormalization/CoupledGhost.lean`: **LEAN-VERIFIED**, eight finite lemmas for signed auxiliary elimination, canonical quadratic energy, leading-sign domination and count arithmetic. Clifford blocks, moving projectors, analytic stationary branch and physical domains remain written/reviewed mathematics. Targeted `lake env lean` passed without proof placeholders; no full project rebuild claim. Evidence: `explorations/conditional-build/source-action-coupled-ghost-2026-11-25.md`.

## Finite-coupling constraint core (2026-11-25)

`GUFormalization/KappaOneConstraints.lean`: **LEAN-VERIFIED**, three finite lemmas for symmetric/skew contraction, constraint-count arithmetic and the intermediate-value sign obstruction. Targeted `lake env lean` passed without placeholders. The actual symbol/projector proof, exact root matrices, real-form transfer and PDE/physical interpretation remain separately checked written mathematics. No full project rebuild claim. Evidence: `explorations/conditional-build/source-action-kappa1-constraints-2026-11-25.md`.

## Reduced evolution finite core (2026-11-26)

`GUFormalization/ReducedEvolution.lean`: **LEAN-VERIFIED**, four finite lemmas for the noncommutative square-zero sandwich, unbounded affine rays and universal derivative jets. Targeted `lake env lean -j1` passed without placeholders. Exact native matrices, canonical-energy reduction and variable-coefficient localized-packet estimates remain reviewed written mathematics; no full PDE formalization or project rebuild claim. Evidence: `explorations/conditional-build/source-action-reduced-evolution-2026-11-26.md`.

## Actual first-graph and charged-matter finite core (2026-11-26)

`GUFormalization/GraphDomain.lean`: **LEAN-VERIFIED**, seven lemmas for graph annihilation/factored kernels, negative-energy approximation, central-current phase sign and positive-charge obstruction, and affine-tail growth. Targeted `lake env lean -j1` passed without placeholders. The actual-coefficient packet proof, null eikonal construction, native matrices and selected matter-domain theorem remain independently reviewed written mathematics. No full PDE formalization or whole-project build claim. Evidence: `explorations/conditional-build/source-action-graph-domain-2026-11-26.md`.

## Steelman and external-datum finite core (2026-11-26)

`GUFormalization/SteelmanDatum.lean`: **LEAN-VERIFIED**, four lemmas for finite coefficient descent, negative interval excluding flatness, equivalent-norm bound and vanishing boundary-term sign. Targeted compilation passed without placeholders. Native SO3 projections, root curvature, operator domains, BRST interpretation and Chern transgression remain independently reviewed mathematics; no full PDE or whole-project-build claim. Evidence: `explorations/conditional-build/source-action-steelman-datum-2026-11-26.md`.

## Current receiver finite core (2026-11-26)

`GUFormalization/CurrentReceiver.lean`: **LEAN-VERIFIED**, six finite lemmas for conjugate-charge signs, the positive-graph contradiction, norm-margin arithmetic, a work/energy counterexample and bounded difference frequency. Targeted compilation passed without placeholders. Native current coefficients, cross-Gram robustness, CK/PT domain covariance and physical propagation remain separately reviewed mathematics; no full PDE or whole-project-build certification is claimed. [Result](../explorations/conditional-build/source-action-current-receiver-2026-11-26.md).

## Receiver strategy finite core (2026-11-26)

`GUFormalization/ReceiverStrategy.lean`: **LEAN-VERIFIED**, six finite lemmas for boost-defect arithmetic and the two owned witness failures, adjoint/kernel scalar identities and a nonzero massless-null transfer. Targeted compilation passed; analytic support, full Lorentz-domain covariance, native normal-energy/Clifford certificates and physical propagation remain separate reviewed obligations. [Result](../explorations/conditional-build/source-action-receiver-strategy-2026-11-26.md).

## Paired response finite core (2026-11-26)

`GUFormalization/PairedResponse.lean`: **LEAN-VERIFIED**, seven finite lemmas on affine-jet subtraction, rational boost/norm arithmetic, Gram cancellation and the spin5 Casimir denominator. Targeted compilation passed; native coefficient certificates, CK covariance proof, weak PDE response and source validity are distinct obligations. [Result](../explorations/conditional-build/source-action-paired-response-2026-11-26.md).

## Rotation rigidity finite core (2026-11-26)

`GUFormalization/RotationRigidity.lean`: **LEAN-VERIFIED**, nine finite lemmas for trace-scale cancellation, coordinate separation, injectivity, rotation transversality, conormal normalization and null unmasking. Targeted compilation passed. Analytic orbit saturation, CK existence and native naturality remain written proofs, not full Lean PDE certification. [Result](../explorations/conditional-build/source-action-rotation-rigidity-2026-11-26.md).

## Covariant finite-jet ambiguity finite core (2026-11-26)

`GUFormalization/CovariantJetAmbiguity.lean`: **LEAN-VERIFIED**, affine measurement-kernel characterization of right inverses, arbitrary hidden parameter families, chosen-image injectivity, finite even-polynomial coefficient isolation and cutoff vanishing. Targeted compilation passed without sorry. Analytic CK filtration/existence and Lorentz covariance remain written reviewed proofs; no physical-state formalization. [Result](../explorations/conditional-build/source-action-covariant-jet-ambiguity-2026-11-26.md).

## Petrov probability finite core (2026-11-26)

`GUFormalization/PetrovProbability.lean`: **LEAN-VERIFIED**, nine lemmas for weighted overlap double-counting, quarter/half bounds, variation discrepancy and exact quartic stabilizer substitutions. Targeted compilation passed without sorry. Properness, tightness, Petrov classification and the probability-limit theorem remain independently reviewed written mathematics. No source necessity or worldwide novelty is formalized. [Proof](../explorations/conditional-build/petrov-probability-selection-2026-11-26.md).

## Normal tensor finite core (2026-11-26)

`GUFormalization/NormalTensorClass.lean`: **LEAN-VERIFIED**, ten lemmas for incompatible coefficient conjugation laws, the injective factor10 contraction, ambient-pair zero and dimension arithmetic. Targeted compilation passed with no placeholders. Clifford completeness, Lie generation, fixed-versus-moving source scope and local constrained-response analysis remain independently reviewed written mathematics; no whole-project rebuild or physical certification. [Result](../explorations/conditional-build/source-normal-tensor-class-2026-11-26.md).

## 2026-11-27 — On-shell dynamics finite core

`GUFormalization/OnshellDynamics.lean`: **LEAN-VERIFIED**, five lemmas for left-shear blocks, reflection preservation, positive-real entry from a trace-zero positive moment, scalar moment bounds and conservative rate arithmetic. Targeted single-thread compilation passed without warnings or placeholders; default import registered. Statement validation: supplying the native matrix/eigenvalue list, the root certificates and the actual microlocal/packet theorem remains separately reviewed mathematics. No full-PDE formalization or whole-project build claim. [Result](../explorations/conditional-build/source-action-onshell-dynamics-2026-11-27.md).

## 2026-11-27 — Finite-loss completion core

`GUFormalization/FiniteLossCompletion.lean`: **LEAN-VERIFIED**, six lemmas: formal transport residual order, universal exponent schedule, logarithmic-power decay, shrinking observation time, vanishing-error contradiction and Sobolev-sandwich transfer. Targeted single-thread compilation passed without warnings/placeholders; default import registered. Classical PDO Taylor/tail estimates, maximal-spectrum transport, native identification and physical/source scope remain independently reviewed written inputs. No full-PDE or whole-project build claim. [Result](../explorations/conditional-build/source-action-finite-loss-completions-2026-11-27.md).

## 2026-11-27 — Coupled support core

`GUFormalization/CoupledSupport.lean`: **LEAN-VERIFIED**, seven lemmas: rational K95 pair arithmetic, longitudinal cancellation, transverse nonzero scalar product, closure contains differences, an open ball yields local differences, an open positive cone has full difference set, and full differences force full source support. Targeted single-thread compilation passed without warnings/placeholders. Native null-kernel/vertex identification, convolution and actual physical/curved admission remain separately reviewed; no whole-project build claim. [Result](../explorations/conditional-build/source-action-coupled-support-2026-11-27.md).

## 2026-11-27 — Matched selected-current core

`GUFormalization/SelectedJet.lean`: **LEAN-VERIFIED**, five lemmas: noncommutative Clifford right cancellation, two-frequency affine separation, affine constant cancellation, raw/skew control, and scalar Gram-perturbation threshold. Targeted single-thread compilation passed without placeholders. Native graph/CK identification, Lorentz band proof and physical normalization remain separately reviewed; no whole-project build claim. [Result](../explorations/conditional-build/source-action-selected-jet-2026-11-27.md).

## 2026-11-27 — Packet phase arithmetic core

`GUFormalization/PacketPhase.lean`: **LEAN-VERIFIED**, four lemmas: derivative budget, inverse phase-charge cost, incompatibility of a uniform polynomial lower bound with rapid decay, and nonzero real quadrature. Targeted single-thread compilation passed without placeholders. Native CK bounds, graph composition, plateau transfer and nonstationary-phase theorem remain separately reviewed written proofs; no whole-project or full-PDE verification claim. [Result](../explorations/conditional-build/source-action-packet-phase-2026-11-27.md).

## 2026-11-27 — Theta divergence finite cores

`GUFormalization/ThetaDivergence.lean`: **LEAN-VERIFIED**, five lemmas: symmetric self-commutator contraction, affine-connection cancellation, separated component, conditional stationary kernel, and separated leading power. Targeted single-thread compilation passed without placeholders. Native geometry, exact root certificates, analytic branch and source dictionary are separately checked/reviewed; no full-PDE formalization. [Result](../explorations/conditional-build/source-action-theta-divergence-2026-11-27.md).

## 2026-11-27 — Endpoint on-shell finite cores

`GUFormalization/EndpointOnshell.lean`: five targeted single-thread checked lemmas, no placeholders/warnings. Covers on-shell elimination, zero-preserving transfer obstruction, quadratic shift, injective raising and inverse-square order-gap cost. Native geometry, root intervals, finite-jet applicability and source bridge are separately verified/reviewed; no whole-project build claimed.

## 2026-11-27 — Ratio-free Riemann-response finite cores

`GUFormalization/RiemannSilence.lean`: four targeted single-thread checked lemmas, no placeholders/warnings. Covers cubic kernel pairing, four-row coefficient elimination, restriction vanishing and zero-preserving postcomposition. Complete native representation classification, Clifford witnesses and source identification are separately proved/reviewed; no whole-project build claimed.

## 2026-11-27 — Stationary torus finite cores

`GUFormalization/StationaryTorus.lean`: **LEAN-VERIFIED**, four lemmas: antisymmetric norm count, two-component independence, positive orthogonal-gauge exclusion and impossibility of a strictly positive gap with a nonpositive witness. Targeted single-thread compilation passed without warnings or placeholders. Global bundle flow, stationary PDE, integration by parts, elliptic domain and inherited flat-PS completeness remain independently reviewed written dependencies. No full-project build or PDE formalization. [Result](../explorations/conditional-build/bet-mass-gap-stationary-torus-2026-11-27.md).

## 2026-11-27 — Real-form transfer finite cores

`GUFormalization/RiemannRealForm.lean`: **LEAN-VERIFIED**, five finite lemmas: real-pair kernel inclusion, complex four-row elimination with arbitrary nonzero scales, joint-reference tangent radical, fixed-connection metric block and its nonzero control. Targeted single-thread compilation passed without warnings/placeholders; default import registered. Real-form/Clifford/Spin identifications, polynomial/naturality transport and the functional critical-family theorem remain separately reviewed written inputs. No full native replay, PDE formalization or full-project build. [Result](../explorations/conditional-build/riemann-realform-transfer-2026-11-27.md).

### 2026-11-27 — Endpoint cubic finite cores

`GUFormalization/EndpointCubic.lean`: exact183/8 arithmetic, zero-linear-row polynomial extraction, symmetric mixed expansion and two leading-term positivity/nonzero cores. Analyticity, native geometry and full coupled stationarity remain written/inherited dependencies; no numerical radius.

## 2026-11-27 — Conservation descent finite cores

`GUFormalization/ConservationDescent.lean`: **LEAN-VERIFIED**, four finite lemmas: normal-jet compensation, surjective consequence equivalence, vanishing free-jet coefficient row and flat superpotential divergence. Targeted single-thread compilation passed with one style linter warning about unnecessary tactic sequencing and no placeholders. Smooth Gaussian/ODE extension, bundle geometry and source/physical applicability remain separately reviewed written mathematics; no full-PDE or whole-project verification claim. [Result](../explorations/conditional-build/bet-cosmology-conservation-descent-2026-11-27.md).

## 2026-11-27 — Full Shiab consistency finite cores

`GUFormalization/FullShiabConsistency.lean`: **LEAN-VERIFIED**, five finite lemmas: three cyclic maps collapse, odd scalar parity, central-matrix tests, mixed quadratic factor and central/traceless spanning. Targeted single-thread compilation passed without output or placeholders. Universal matrix-unit classification, compact variational argument, Spin/real-form and source identification remain separately reviewed written inputs; no full-project or source formalization claim. [Result](../explorations/conditional-build/full-shiab-variational-consistency-2026-11-27.md).

## Printed endpoint Hessian separation (2026-11-27)

`GUFormalization/EndpointHessianSeparation.lean`: **LEAN-VERIFIED**, targeted single-thread compilation passed. It checks affine pairing cancellation at arbitrary backgrounds and rank-gap arithmetic from explicit premises; it does not formalize the smooth variational theorem or source custody. Targeted receipt is in `lab/process/printed-shiab-endpoint-audit.json`.

## Compact excitation charge finite cores (2026-11-27)

`GUFormalization/CompactCharge.lean` checks the abstract boundary-balance cancellation and nonnegative finite-sum implication. Smooth lifts, cutoff extensions, Stokes and physical/source applicability remain written and reviewed. See [result](../explorations/conditional-build/compact-excitation-charge-2026-11-27.md).

## Unitary dual closure finite cores (2026-11-27)

`GUFormalization/UnitaryDualClosure.lean` proves insertion-factor projection cancellation and invertible postcomposition zero equivalence. Clifford identities, source/jet/paired-domain applicability and native rank512 remain written and reviewed premises. See [result](../explorations/conditional-build/bet-2plus1-unitary-dual-closure-2026-11-27.md).

## Shiab derivation finite cores (2026-11-27)

`GUFormalization/ShiabDerivation.lean` proves coefficient-commutator Leibniz and two-map annihilation. Full graded/Spin classification, Riemann geometry, real-form transfer, source applicability and global group bundle proofs remain written and reviewed. See [result](../explorations/conditional-build/shiab-graded-derivation-class-2026-11-27.md).

## Shiab companion finite cores (2026-11-27)

`GUFormalization/ShiabCompanion.lean` proves zero-preserving nonfactorization and bilinear polarization. Exterior classification, Clifford/Riemann identity, real forms, actual jets and source relevance remain written and reviewed. [Result](../explorations/conditional-build/shiab-bianchi-companion-class-2026-11-27.md).

## Null-symbol trace finite cores (2026-11-27)

`GUFormalization/NullSymbolTrace.lean` checks trace/order arithmetic only. The exact-chain trace and source applicability remain written/reviewed. Result: `explorations/conditional-build/null-boost-symbol-trace-2026-11-27.md`.

## Finite normal-jet recurrence (2026-11-27)

`GUFormalization/NormalJetRecursion.lean` checks two finite causal recurrence lemmas. Smooth ODE existence, jet realization, support and Stokes remain written/reviewed; existing CompactCharge cores are reused. Result: `explorations/conditional-build/bet-cosmology-normal-jets-2026-11-27.md`.

## 2026-11-27 — Smooth local complement finite core

`GUFormalization/LocalComplement.lean` checks seven finite character-sign, exceptional-product, receiver-rank and native-rank contradiction statements. The all-character completeness proof, smooth graph equation, native Clifford geometry and complex metric-flip transfer remain written/reviewed premises; no physical interpretation follows. Result: `explorations/conditional-build/bet-2plus1-local-complement-2026-11-27.md`.

## 2026-11-27 — Reference holonomy finite cores

`GUFormalization/ReferenceHolonomy.lean`: targeted single-thread Lean compilation passed without placeholders. Four lemmas check the nonzero real curvature eigenvalue/positive-norm contradiction, its inner-product form, and a real-part margin. Native connection geometry, compact holonomy, Ricci-flat product rigidity and spectral continuity remain written, internally reviewed proofs. No physical positivity, quantum gap or whole-project formalization follows. Result: `explorations/conditional-build/bet-mass-gap-reference-holonomy-2026-11-27.md`.

## 2026-11-27 — Printed differential finite cores

`GUFormalization/PrintedDifferential.lean` checks the abstract two-channel mode lift, quadratic quotient, determinant arithmetic and scalar perturbation margin. Targeted single-thread compilation passed without placeholders. Native symbol, geometry, scalar fundamental solutions, curved analytic CK and Sobolev growth remain written reviewed proofs. Result: `explorations/conditional-build/printed-differential-solvability-2026-11-27.md`.

## 2026-11-27 — Printed nonlinear finite cores

`GUFormalization/PrintedNonlinear.lean` checks the two-channel hook mode, zero-self-interaction consequence, cokernel correction obstruction and dispersion arithmetic. Targeted single-thread compilation passed without placeholders. Native Clifford identities, analytic branch coefficients, h-series and PDE/domain conclusions remain written reviewed proofs. Result: `explorations/conditional-build/printed-nonlinear-transfer-2026-11-27.md`.

## 2026-11-27 — Printed state-completion finite cores

`GUFormalization/PrintedStateCompletion.lean` checks left-cokernel obstruction, its persistence when the reduced base contributes zero to the receiver, and the nonzero scaling arithmetic. Targeted single-thread compilation passed without placeholders. Native Clifford amplitudes, C² graph differentiation, analytic poles and secular PDE responses remain written reviewed proofs. Result: `explorations/conditional-build/printed-state-completion-2026-11-27.md`.

## 2026-11-27 — Evolution-complement finite cores

`GUFormalization/EvolutionComplement.lean` checks a differentiated graph identity, factorization-kernel implication and the finite dimension inequalities. Targeted -j1 compilation passed. The native minor, geometry and graph differentiation remain written/exactly computed results, not fully Lean formalized.

## 2026-11-27 — Full-system CW finite cores

`GUFormalization/CWFullSystem.lean` checks excluded-support receiver logic, scalar linear-growth unboundedness and the exact support/secular arithmetic. Targeted single-thread compilation passed. Native descriptor, packet/moment, temporal Jordan and covariance proofs remain separately written/reviewed; no physical Hilbert norm or quantum theory is formalized.

## 2026-11-27 — Nonlinear CW finite cores

`GUFormalization/CWNonlinearCompletion.lean` checks the boosted stable margin, nonzero residue, uniqueness with a left inverse, actual self-particular arithmetic and threshold positivity. Five theorems compiled with targeted single-thread Lean. Kernel/coarea and representation proofs remain written/reviewed, not fully formalized.

## 2026-11-27 — Local-current finite cores

`GUFormalization/LocalCurrent.lean` checks nonnegative anti-isometry, observed-retention contradiction, normal aggregate/restore arithmetic and restricted-density positivity. Five targeted single-thread Lean theorems pass. Native symbol, spectral quotient, current-jet identity and source/physical-domain interpretation remain written reviewed arguments.

## 2026-11-28 — CW symmetry/domain finite cores

`GUFormalization/CWSymmetryDomain.lean` checks reversal-closure logic, mass positivity and margin, residue lower-bound arithmetic and rational core fixtures (five theorems). Targeted single-thread compilation; no sorry. Full orbit/coarea/complete-history, source identification and physical quantum claims are not formalized by these finite cores.

## CW global coefficient norm (2026-11-28)

`GUFormalization/CWGlobalNorm.lean` checks six finite cores: boost and amplification arithmetic, the growth lower bound, kernel domination, companion decay and degree/shell counts. Targeted single-thread compilation passed without proof placeholders. The full scalarizer, thirteen-dimensional packet argument, bilinear estimates and physical/source bridges are written mathematics, not formalized by these lemmas. See `../explorations/conditional-build/cw-edge-decay-and-global-norm-2026-11-28.md`.

## 2026-11-28 — CW global quadratic boundary finite cores

`GUFormalization/CWQuadraticBoundary.lean` checks six finite cores: shell/receiver arithmetic, intrinsic forced identity and derivative accounting. Targeted single-thread compilation passed without proof placeholders. Integration, global packets, residue identities and physical/source applicability remain written/reviewed mathematics. No full-project build or canon promotion is claimed. Result: `explorations/conditional-build/cw-global-quadratic-boundary-2026-11-28.md`.

## 2026-11-28 — Nonlinear cosmology finite cores

`GUFormalization/CosmologyRoll.lean` checks six finite lemmas: strict moment discriminant, potential identity, damping/crossing bounds and rate/kinematic arithmetic. Targeted single-thread compilation passed; no proof placeholders. Global ODE continuation, cone and asymptotic arguments remain reviewed written mathematics. No full-project build or canon promotion. Result: `explorations/conditional-build/bet-cosmology-nonlinear-roll-2026-11-28.md`.

## 2026-11-28 — Positive quotient finite cores

`GUFormalization/PTPositiveQuotient.lean` checks seven finite contraction, readout, PSD, weight and exact-arithmetic cores. Targeted single-thread compilation passed. Packet/form-domain/coarea and source-applicability arguments remain written and reviewed, not Lean-formalized. Result: `explorations/conditional-build/pt-positive-quotient-observation-2026-11-28.md`.

## 2026-11-28 — Observer horizon finite cores

`GUFormalization/ObserverHorizon.lean` checks seven pointedness, quotient, factorial and arithmetic cores. Analytic cone/measure/jet/geometry arguments remain written and independently reviewed. Result: `explorations/conditional-build/observer-horizon-compatibility-2026-11-28.md`.

## 2026-11-28 — Unimodular Lambda finite cores

`GUFormalization/UnimodularLambda.lean` checks seven background uniqueness, sign, factorization, growth and shift cores. Differential geometry/Noether/PDE proofs remain written and independently reviewed. Result: `explorations/conditional-build/unimodular-lambda-and-scalar-2026-11-28.md`.
