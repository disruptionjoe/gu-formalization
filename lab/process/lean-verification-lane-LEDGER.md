---
title: "Lean Verification Lane: Ledger and Queue"
status: canon
doc_type: lane-ledger
scope: repo-local
created: 2026-07-07
updated: 2026-08-31
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

## Part D: lock and progress contract

On Windows, every invocation uses `lab/automation/check-lean.ps1`. Its exclusive file handle is host-local.
It does not serialize another computer or cloud runner, and it cannot technically stop a direct command from
bypassing policy. Other hosts require a runner-native single-build lock and `-j1`. No two hosts may write the
same checkout.

A run makes progress only by producing a current green baseline, integrating an existing certificate,
retiring a misleading certificate lookalike, adding a newly `LEAN-VERIFIED` kernel, repairing a
`LEAN-PARTIAL` kernel, or recording an exact faithfulness/mathlib obstruction that prevents a false theorem
from entering Lean. Do not manufacture a trivial theorem to appear busy.
