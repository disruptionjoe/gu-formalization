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
| `GUFormalization/SourceNativeSpin64Observation.lean` | General linear-algebra certificate: an invertible normal Clifford component lifts every nonzero horizontal trace to the ambient gamma kernel while literal observation pullback retains the nonzero observed trace. No physical quotient or generation sector is constructed | `explorations/source-native-spin64-observation-sector-obstruction-2026-08-30.md` |
| `GUFormalization/SourceNativeObservationDescent.lean` | Split-surjective descent criterion: observation preserves the ambient Clifford kernel exactly when observed contraction factors uniquely through ambient contraction. The factor is explicit, but no source-owned or physical bridge is constructed | `explorations/source-native-spin64-observation-sector-obstruction-2026-08-30.md` |
| `GUFormalization/SourceNativeRealSector.lean` | Abstract real-sector criterion: a supplied linear involution modeling conjugation and anticommuting with chirality gives a linear equivalence between the positive and negative chirality kernels. A scalar-antilinear real structure, Clifford representation and physical interpretation are not constructed | `explorations/source-native-spin64-observation-sector-obstruction-2026-08-30.md` |
| `GUFormalization/SourceNativeAdjointCoupling.lean` | Finite supplied-multiplicity certificate for the adjoint/144 degree ladder: cubic 45 availability, linear PS obstruction, and exact symmetric 54/210 versus alternating 45/945 quadratic owner split. No source coefficient, family selector, or mass is constructed | `explorations/source-native-adjoint-144-coupling-classification-2026-08-31.md` |
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

## Standalone Lean Certificates

| Lean file | Scope | Owner surface |
|---|---|---|
| `GUFormalization/ResidualSelectionAxioms.lean` | Manual, informational `#print axioms` receipt outside the default target; run with `lake env lean` | `lab/process/lean-verification-lane-LEDGER.md` |
| `tests/big-swing/R4_TwoArena.lean` | Compatibility entrypoint importing the default-target R4 module | `canon/two-arena-rep-theory-core-RESULTS.md` |

## Local Commands

After installing Lean/elan:

```powershell
lake exe cache get
lake build
```

The committed `lake-manifest.json` is the dependency lock.  Do not run
`lake update` as a routine reproduction step: the mathlib input tracks
`master`, so an update can advance both the manifest revision and the required
Lean toolchain.  Use it only when intentionally updating and reviewing the pin.

Or use:

```powershell
.\lab\automation\check-lean.ps1 -Update -Cache
```

The process gate `process_gates/lean_certificate_surface_audit.py` derives the
default-target certificate inventory from `GUFormalization.lean`, requires
every library module to be imported or explicitly declared as a manual
non-default certificate, and checks the Lean map, ledger, owner references, and
proof-body placeholder hygiene. It is a routing and governance gate, not a
replacement for `lake build` or targeted standalone Lean checks.
