---
title: "Verification: What Is Proved, Computed, and Conjectural"
status: process
doc_type: verification-map
updated_at: "2026-08-31"
---

# VERIFICATION -- what is proved, what is computed, what is conjectural

## Finite-action span category (2026-08-31)

| Claim | Evidence | Honest grade |
| --- | --- | --- |
| Finite supplied `G`-actions and arbitrary equivariant spans, modulo equivariant isomorphism of the apex commuting with both legs, form a category | `Lean/GUFormalization/GroupActionSpanCategory.lean`; default-target axiom receipt | L1 exact category theory on supplied finite actions |
| Identity is the diagonal span and composition is the finite equivariant pullback; explicit left/right unitors and the canonical reassociation of nested pullbacks prove the category laws | Lean `identityCompEquiv`, `compIdentityEquiv`, `assocEquiv`, and `BurnsideSpanObject.category_laws` | L1 exact group-action algebra |
| Equivariant maps embed covariantly as graph spans, graph composition agrees with map composition, and converse graphs supply transfer-direction arrows without assuming an inverse | Lean `graphCompEquiv`, `graph_composition`, and `converseGraph`; finite multiplicity-matrix controls in `tests/W99_theorem_finite_instances.py` | L1 exact categorical consequence |
| A separate categorical universal property, disjoint-coproduct addition on span homs, group completion/preadditivity, a Mackey functor valued in this category, source-native realization, physical representation, selector, prediction, or GU verdict | not constructed by the present span-category theorem | open / explicitly excluded |

## Finite-action Burnside Mackey group (2026-08-31)

| Claim | Evidence | Honest grade |
| --- | --- | --- |
| Finite supplied actions modulo equivariant equivalence form a commutative monoid under disjoint coproduct, whose Grothendieck completion is an additive Burnside group | `Lean/GUFormalization/GroupActionBurnside.lean`; default-target axiom receipt | L1 exact group-action algebra |
| Subgroup restriction and induction preserve equivariant equivalence and disjoint coproduct and therefore descend to additive homomorphisms of Burnside groups | Lean `restriction`, `induction`, `restriction_of`, and `induction_of` | L1 exact categorical algebra for finite supplied actions |
| For finite `G` and subgroups `K,H`, restriction after induction equals the Burnside class of the dependent coproduct over `K \\ G / H` of the transported-intersection induced conjugate seed actions | Lean `restriction_induction_of_eq_mackeyCoproduct`; nonnormal `S3` control in `tests/W99_theorem_finite_instances.py` | L1 additive Mackey double-coset identity |
| Arbitrary-span composition is supplied separately by the finite-action span category above; homwise coproduct addition, group completion/preadditivity, physical representation category, source-native action, coupling, selector or GU verdict | not constructed by this finite-action Burnside group | open / explicitly excluded |

## Free preadditive Mackey envelope (2026-08-31)

| Claim | Evidence | Honest grade |
| --- | --- | --- |
| Every supplied-action functor lifts to the free integer-linear envelopes, preserving each basis morphism with its coefficient | `Lean/GUFormalization/GroupActionAdditiveEnvelope.lean`; default-target axiom receipt | L1 exact category algebra using Mathlib's free linear category |
| The canonical supplied-action Mackey natural isomorphism lifts to a natural isomorphism of the free preadditive envelopes | Lean `canonicalMackeyAdditiveEnvelopeNatIso` | L1 exact functorial consequence |
| The empty raw point-to-empty hom-set becomes exactly the singleton formal zero hom-group, while no original action map is created | Lean `point_to_empty_envelope_eq_zero`; finite control in `tests/W99_theorem_finite_instances.py` | L1 exact boundary; finite control is confirmation only |
| Span morphisms, arbitrary-span composition, Burnside coproduct quotient, restriction/transfer data, double-coset transfer law, physical representation, source-native action or GU claim | not constructed by free hom additivization; the separate finite-action Burnside group below supplies only the stated finite additive Mackey structure | open here / separately narrowed |

## Observation descent and paired real-sector criteria (2026-08-31)

| Claim | Evidence | Honest grade |
| --- | --- | --- |
| With a supplied right inverse for ambient Clifford contraction, observation preserves its kernel iff observed contraction factors through ambient contraction | `Lean/GUFormalization/SourceNativeObservationDescent.lean`; default-target axiom receipt | L1 exact linear algebra from explicit premises |
| The factor is explicitly `gammaB ∘ observe ∘ rightInv` and is unique | Lean `descentFactor_unique` | L1 exact split-surjection consequence |
| A supplied linear involution modeling conjugation and anticommuting with chirality exchanges the positive and negative chirality kernels by a linear equivalence | `Lean/GUFormalization/SourceNativeRealSector.lean`; default-target axiom receipt | L1 exact algebra from explicit premises; no scalar-antilinear structure is constructed |
| The actual source-owned observation factor/quotient, Clifford representation, physical real sector, observed family, action, mass or GU verdict | not constructed by these criteria | open / explicitly excluded |

## Raw-action additivity obstruction (2026-08-31)

| Claim | Evidence | Honest grade |
| --- | --- | --- |
| For any supplied group, there is no action morphism from its nonempty one-point trivial action to its empty trivial action | `Lean/GUFormalization/GroupActionMackeyAdditivityBoundary.lean`; default-target axiom receipt | L1 exact categorical obstruction |
| The ordinary category of supplied actions admits no preadditive structure and no zero object | Lean `action_preadditive_false` and `action_has_no_zero_object` | L1 exact consequence of the empty point-to-empty hom-set |
| The existing canonical Mackey natural isomorphism is not by itself an additive Mackey functor | the source category lacks the hom-set zero required by preadditivity; W99 checks the empty/singleton finite witness | exact scope boundary on the current construction |
| Additive span/Burnside completion, restriction/transfer data, double-coset compatibility on that completion, or physical realization | not constructed by this obstruction theorem | open / explicitly excluded |

## Categorical Mackey natural isomorphism (2026-08-31)

| Claim | Evidence | Honest grade |
| --- | --- | --- |
| The representative-free Mackey construction and restricted induction are functors from supplied `H`-actions to supplied `K`-actions, and canonical assembly is a natural isomorphism between them | `Lean/GUFormalization/GroupActionMackeyCategory.lean`; default-target axiom receipt | L1 exact categorical algebra from supplied actions |
| Applying Mathlib's standard free-linearization functor gives a natural isomorphism of `K`-representation functors over any commutative ring | Lean `canonicalMackeyRepresentationNatIso` | L1 exact functorial consequence |
| Identity, composition and the complete naturality square hold in the nonnormal `S3` control | `tests/W99_theorem_finite_instances.py` | finite confirmation only |
| Additive Mackey functor, physical representation, source-native action, coupling or selector | not constructed by this functor packaging | open / explicitly excluded |

## Mackey permutation-representation equivalence (2026-08-31)

| Claim | Evidence | Honest grade |
| --- | --- | --- |
| The free modules on the canonical Mackey coproduct and restricted-induced carrier carry genuine `K`-permutation representations, and canonical assembly is an equivalence of those representations | `Lean/GUFormalization/GroupActionMackeyRepresentations.lean`; default-target axiom receipt | L1 exact representation algebra from supplied set actions |
| Over any commutative semiring, the equivalence induces an isomorphism of modules over the group algebra `R[K]` | Lean `canonicalMackeyGroupAlgebraLinearEquiv` | L1 exact algebraic consequence |
| Identity, multiplication and complete basis intertwining laws hold in the nonnormal `S3` control; a nonbijective hostile generator fails the group law | `tests/W99_theorem_finite_instances.py` | finite confirmation only |
| Additive Mackey functor on physical representations, source-native action, coupling or selector | not constructed by permutation-representation packaging | open / explicitly excluded |

## Free-module Mackey linearization (2026-08-31)

| Claim | Evidence | Honest grade |
| --- | --- | --- |
| The canonical representative-free Mackey carrier equivalence lifts to an `R`-linear equivalence of free finitely-supported modules | `Lean/GUFormalization/GroupActionMackeyLinearization.lean`; default-target axiom receipt | L1 exact algebra from the supplied set actions |
| The lift preserves basis vectors and support cardinality and intertwines linearized seed maps and the supplied `K`-actions | Lean naturality/equivariance/support theorems; nonnormal `S3` controls in `tests/W99_theorem_finite_instances.py` | L1 exact algebra; finite controls are confirmation only |
| Additive Mackey functor on physical representations, source-native action, coupling or selector | not constructed by free linearization | open / explicitly excluded |

## Source-native adjoint/144 coupling degree ladder (2026-08-31)

| Claim | Evidence | Honest grade |
| --- | --- | --- |
| The paired-real family/144 system has one cubic adjoint-`45` invariant vertex, obtained by pairing the multiplicity-one `45` lines in the two conjugate same-label complex products | `tests/channel-swings/source_native_adjoint_144_coupling_probe.py` composed with the exact Q5 dictionary | exact representation-grade availability |
| No nonzero Pati-Salam-preserving linear adjoint background exists; the first symmetric-quadratic owners are `54` and `210`, each with one PS singlet, while the alternating `45` and `945` owners have none | exact weight-character derivation of `Sym^2(45)=1+54+210+770` and `Lambda^2(45)=45+945`, plus the held HE-4 PS counts; 23/23 controls including hostile mutations | exact representation-grade obstruction and feasibility classification |
| Source action placement, form-leg contraction, family covector, coefficient, physical operator, mass, observed sector, scale, threshold or prediction | not established by this gate | open / explicitly excluded |

## Source-native Spin(6,4) observation sectors (2026-08-30)

| Claim | Evidence | Honest grade |
| --- | --- | --- |
| The real `Cl(6,4)` structure exchanges complex `16+ / 16-` half-spinors and `144+ / 144-` gamma kernels while preserving each paired total | `tests/channel-swings/source_native_spin64_observation_sector_probe.py` (real integer 32x32 Clifford construction, volume/chirality and split-surjectivity controls) | exact representation-grade |
| Literal section pullback does not preserve the ambient gamma kernel | general Clifford witness in `explorations/source-native-spin64-observation-sector-obstruction-2026-08-30.md`; finite exact hostile control in the probe | theorem-grade algebraic obstruction to the naive bridge |
| Observed generations, physical chirality, masses, action, quotient and source claim | not established by this gate | open / explicitly excluded |

Outsider entry point. This program uses internal labels ("theorem-grade", "closed", "confirmed"); this file
exists so you do NOT have to trust them. It classifies the flagship results into three honesty levels, gives each
a compact verification package, and states plainly what would falsify the leading interpretations. Companion to
`REPRODUCE.md` (how to run the tests) and the long-form audit in
`explorations/obj6-verification-package-2026-07-11.md`.

## The three levels

- **L1 PROVEN MATHEMATICS** -- established exactly from stated assumptions; the proof does not depend on any
  numerical run.
- **L2 COMPUTED MODEL RESULT** -- demonstrated in a specific finite model / numerical calculation / RG
  truncation; regulator/scheme/truncation caveats apply.
- **L3 PHYSICAL INTERPRETATION** -- connects an L1/L2 result to Geometric Unity or to nature; the most
  conjectural level.

## Flagship results

| # | Claim | Level | Confidence | Reproduce | Strongest objection (conceded) |
|---|---|---|---|---|---|
| a | **Diagonal self-valuation theorem:** if a set `B` admits a fixed-point-free endomap, no map `T : A × A -> B` is weakly point-surjective; for inhabited `A`, no valuation `p : A -> B` is invariant under that endomap. More generally, pointwise invariance under a group action is equivalent to the image of `p` lying in the common fixed-point set; for finite `A` and `B`, the exact number of pointwise-invariant valuations is `|Fix_G(B)|^|A|`, so the empty-domain case has one valuation even when the fixed set is empty. This does not count acted-on-domain equivariant maps: for an arbitrary `G`-set, equivariant maps are a dependent product of values in `B` fixed by one chosen representative's stabilizer for every orbit, giving `|Eqv(A,B)| = product_[omega in A/G] |B^Stab(a_omega)|` for finite types. Seed types at representatives in one orbit are explicitly equivalent. Equivariant changes of domain and codomain coordinates preserve the complete map and fixed-seed spaces; domain transport induces an explicit equivalence of orbit quotients, and the two coordinate transports commute. Equivariant maps into arbitrary indexed products of acted-on codomains and out of arbitrary indexed coproducts of acted-on domains decompose into their component map families, with exact finite counts and existence laws. The conjugation action on `A -> B` has exactly the equivariant maps as common fixed points, and diagonal-product maps satisfy the equivariant curry/uncurry exponential law. Acting groups may be changed explicitly: restriction along `phi : H ->* G` preserves the complete map and fixed-point spaces when `phi` is surjective, while arbitrary restriction has both a checked left adjoint `Ind`, realized by the balanced-product orbit quotient with `Hom_G(Ind B,C) ~= Hom_H(B,Res C)`, and a checked right adjoint `Coind` with `Hom_H(Res A,B) ~= Hom_G(A,Coind B)`. Induction is coherent: `Ind_id B ~= B` and `Ind_(psi.comp phi) B ~= Ind_psi (Ind_phi B)` as explicit equivariant equivalences. For subgroups `H,K <= G`, the Mackey interface identifies the `K`-orbit quotient of `Res_K^G Ind_H^G(1)` with `K\\G/H` and proves the stabilizer of `[g,star]` is the transported intersection condition `k*g = g*h`; for an arbitrary supplied `H`-set `B`, the transported action through `g⁻¹kg : H` makes `K ×_(K ∩ gHg⁻¹) {}^gB` explicitly `K`-equivalent to the concrete `[kg,b]` summand, and choosing one representative of every double coset yields a dependent-coproduct `K`-equivalence with all of `Res_K^G Ind_H^G(B)`. If every point stabilizer imposes one common fixed-value condition, then `Eqv(A,B)` is exactly `(A/G -> B^H)` and has finite count `|B^H|^|A/G|`. Free-domain and trivial-codomain actions are specializations; the transitive and regular left-torsor results are the one-orbit cases. | **L1** (math) / L3 (optional observer reading) | math HIGH; observer reading LOW | `Lean/GUFormalization/ResidualSelection.lean` proves the diagonal / no-closure / no-invariant-valuation core; `Lean/GUFormalization/GroupActionFixedPoints.lean` proves the pointwise fixed-set classification, finite cardinality and edge cases, arbitrary-domain orbit-product equivalence, representative, domain/codomain and orbit-quotient transport, commuting naturality, indexed-codomain product preservation, uniform-stabilizer, free-domain and trivial-codomain quotient classifications, existence criteria and finite censuses; `Lean/GUFormalization/GroupActionCoproducts.lean`, `Lean/GUFormalization/EquivariantInternalHom.lean`, `Lean/GUFormalization/GroupActionChangeOfGroups.lean`, `Lean/GUFormalization/GroupActionInduction.lean`, `Lean/GUFormalization/GroupActionInductionCoherence.lean`, and `Lean/GUFormalization/GroupActionMackey.lean` prove the coproduct, closed-structure, two-sided change-of-acting-groups, induction-coherence, and complete subgroup Mackey decomposition laws; the default-target axiom receipt reports the exact theorem dependencies; `tests/W99_theorem_finite_instances.py` is confirmation only; paper `papers/published/observer-value-selection-theorem/` | "This is Cantor-Lawvere plus elementary group-action facts." CONCEDED -- self-graded NOVEL-PACKAGING (b); novelty is the explicit synthesis and controls, not a new fixed-point or equivariance theorem. |
| b | **UV structure:** GU/4th-order+ker-Gamma-RS is renormalizable + asymptotically free/safe; unitary at tree/algebraic grade (+ a machine-checked no-local-positive-metric theorem); loop positivity OPEN; the ghost is genuinely kept (HORN K). | **L2** (truncation-conditional) | MEDIUM-HIGH (model); UV completion OPEN | `tests/W44,W45-47,W48-54,W81,W83,W87,W88,W95-97` | "No complete two-loop RGE fixes sign(eta_C)." CONCEDED -- the horn is scheme-conditional (CONTROLLED-EXCEPT-ETAC); loop unitarity is an open positivity-vs-causality trade. |
| c | **Generation count:** located-not-forced -- multiplicity is natively 3 (a representation dimension); the net chiral count is interior-even / net-0 (2-primary, a class-wide no-go) and external-by-structure (the external count is any integer -- flux number / Aharonov-Casher); the only unconditionally computable integer is 1; "3" over "1" is NOT derived (requires an observer/symmetry-breaking selection). | **L1** cores (one Lean-verified); "3" is L3 OPEN | cores HIGH; "3" OPEN | `tests/W55-W60` | "Hom(Z/3,Z)=0 means you surrender the count; only the honest integer is 1." CONCEDED -- it is a no-go that LOCATES, not a derivation of 3. |
| d | **Sectorial-closure BREAK (retraction):** the "physical modular realization closes sectorially" claim was FALSE -- a genuine finite spacetime region is type III_1 / infinite-rank, so under a physical interaction no coherent net of bounded modular conjugations exists (an IFF-no-go with an explicit falsification boundary, condition X = UV-soft coupling). | L2 (reconstruction) | MEDIUM-HIGH | `tests/W98,W100_obj2` | "A region is not a cutoff." This IS the program's own break -- included as the credibility anchor: the program retracts honestly. |
| e | **Observer Structure Theorem (model grade):** under one unified assumption set, on the W98 Krein tower class: (1) an observer's complete one-sided physics (incl. the value-selection cocycle) is finite per-state on a sharp state class, needing NO modular conjugation; (2) the interface obstruction is a grading-relative invariant whose classes form a presheaf WITH a global section (cocycle holds on triple overlaps) -- a global CLASS exists while no global OPERATOR does; (3) no bounded conjugation exists at any level, located ([C]=2[P]) and typed, and the absence is FACTORIZATION-INVARIANT (square-root rigidity). The mixing-direction assumption is DERIVED-conditional (interaction-universality). All mathematical clauses are horn-independent class-statements. | **L2** (model-grade theorem; NOT continuum) | MEDIUM-HIGH; lifts named (Weinberg transfer, skeleton-grade vertex uniqueness, HORN K for membership) | `tests/W109` (composed) + `W105-W108, W110-W112` | "A conjunction of separately-tuned toys" -- answered by the single-instance joint verification + 18/18 sweep; "second reframe of a retracted claim" -- conceded and distinguished: every clause survived pre-registered kill-modes, and the theorem asserts the ABSENCE of the conjugation (W94 negated, not repaired). Prior-art framing per W112: the new content is the exact identification of the wall-carrying grading-sensitive object, inside an existing graded-invariants field. |

## What is proved / computed / imported / conjectural

- **PROVED (L1):** flagship (a) as pure set-level math; several (c) cores (incl. a Lean-checked CRT
  split); the no-local-positive-metric theorem (free case); functoriality of
  set-level subgroup induction in equivariant seed maps, naturality of the
  representative-free Mackey fiber decomposition, equivariant
  representative-independence of transported-intersection Mackey summands,
  the Hom-form Mackey equivalence from restricted-induced maps to the
  dependent family of transported-intersection seed-map spaces, and the
  free-module lift of the canonical carrier equivalence with basis/support,
  seed-map naturality and supplied-action equivariance laws; its bundled
  equivalence of `K`-permutation representations and resulting group-algebra
  module isomorphism over commutative semirings;
  and two finite
  certificate deductions: the supplied Shiab decomposition rows give complex
  chiral multiplicities `[[0,2],[2,0]]`, while an explicit left inverse for an
  eliminated block plus Schur-complement injectivity forces the abstract block
  kernel to vanish. The first does not construct the D7 decompositions or a
  physical selector; the second does not identify GU's actual operator or
  close FC-VZ-1.
- **COMPUTED (L2):** all FRG/UV results (one-loop + ker-Gamma projector + partly ported agravity betas); the
  sectorial IFF-no-go; the source-action skeleton (O5).
- **IMPORTED (cited, not re-derived):** standard higher-derivative-gravity betas (Fradkin-Tseytlin/
  Avramidi-Barvinsky/agravity); the Reuter fixed point + matter bounds (Reuter-Saueressig/Dona-Eichhorn-Percacci);
  Tomita-Takesaki / Bisognano-Wichmann / Shulman / Gottschalk; Lawvere/Yanofsky; DESI DR2 numbers.
- **CONJECTURAL (L3):** "the source action IS the observer" as a physical statement (the modular-conjugation
  realization is WALLED, see (d)); GU housing the Standard Model beyond gauge-group grade; the value of the
  generation count; that GU is on HORN K unconditionally (truncation-conditional).

## What would falsify the leading interpretations

- Flagship (a) physical reading: already broken at the modular-realization level (d). The ABSTRACT theorem is not
  falsifiable by physics (it is math); its physical relevance is.
- Flagship (b) HORN K: a complete two-loop-with-graviton EH x Weyl RGE giving eta_C > 0 in the physical
  (Weyl-adapted) scheme would flip to HORN Q (removable ghost) -- see `explorations/obj4-uv-scheme-stability`.
  Under HORN Q, flagship (e)'s mathematics survives unchanged (class-statements); only GU's MEMBERSHIP in the
  wall class narrows.
- Dark energy (in the one-residual flagship): the current honest register after the W113 joint-profile
  correction -- the shape AND the canonical f_0 = 0.125 are both viable on the DESI DR2 BAO likelihood (the old
  "f_0 tension" was a fixed-amplitude-slice artifact); the sector's residual lives entirely in the
  amplitude-calibration direction, with two referents kept DISTINCT: under amplitude MARGINALIZATION the data
  prefer an amplitude +1.81% above Planck (A* = 30.8059) and the shape -- canonical f_0 included -- is viable
  inside delta-chi^2 <= 1; under the packet's OWN-theta_star calibration GU's amplitude is pinned at +5.66%
  above Planck (A_GU = 31.9715), overshooting the BAO-preferred amplitude for this shape (A* = 31.4709) by
  +5.74 sigma (dAIC +35.79) -- the decisively-disfavored leg the PP3 packet quotes. A future BAO amplitude
  calibration confirming the Planck value at sub-percent precision would exclude the family; the CPL-level
  falsification (H43/H44) stands regardless.
- The observer conjecture's "wall becomes prediction" move: the pre-registered fork
  (`explorations/obj3-adversarial-fork-preregistered`) landed on Outcome B (wall remains); the exact evidence that
  would reverse it to A/C/D is listed there.

## Honesty boundary
The program's leading PHYSICAL story (source action = observer) is NOT established: its rigorous modular
realization broke (d), and its status is mechanism-genuine + abstract-theorem-proven + value-selection-realized-
algebraically, with the full firewall-as-modular-conjugation WALLED. The durable, externally-attackable results
are (a) the abstract theorem, (b) the UV structural map (truncation-conditional), (c) the interior-even /
external-by-structure count no-go, and (d) the honest break. Trust the levels, not the adjectives.

## Probe and mutation-harness discipline (adopted 2026-08-17)

Every exact probe in this repository certifies a claim only as far as its own
failure path is real. The following are the minimum standard, each learned
from a dated incident in which a green instrument certified nothing:

1. **A selftest verifies its clean baseline BEFORE running any mutation**, and
   aborts red rather than banking a false "all mutations caught." A red
   baseline makes every mutation exit nonzero for the pre-existing reason.
   (Three archaeology probes shipped 2026-08-15 could accept a red baseline;
   caught in independent review IV-20260815.)
2. **A mutation corrupts machinery or a reference — never the check itself.**
   Loosening a check's predicate (`== 4` → `>= 0`, a pin → a length test, a
   gate → constant True) can only make the probe greener and is undetectable
   by any runner: unfalsifiable by construction. (Six of fifteen mutations in
   one probe were this class, masked by incident 3 below; repaired
   2026-08-17.)
3. **A catch counts only via a genuine failing check** — a `[FAIL]` line or
   equivalent — and a nonzero exit without one is CRASH-NOT-DETECTION and
   fails the selftest. A crash also exits nonzero, so exit codes alone cannot
   distinguish a working harness from a broken one. (A path bug ran every
   mutant one directory deep; all fifteen "catches" were crashes;
   found by FX-3, 2026-08-17.)
4. **An absence check on a clean corpus needs a planted-positive control**:
   corrupting the detector cannot flip an absence result, so the detector's
   power must be demonstrated on a synthetic positive it is required to flag.
5. **Selftests exit 0 on success.** A harness that inverts the convention
   reads as broken when healthy and healthy when crashed. (Normalised
   2026-08-15.)
6. **Tolerances and baselines must not absorb planted controls.** A scope
   baseline wide enough to swallow the selftest's own planted reds silently
   voids the selftest; pin the selftest's baseline independently of the
   live one. (The kill-target gate's selftest failed invisibly for a day
   this way; repaired 2026-08-15.)
7. **Verification of a harness reads what the catches actually were**, not the
   summary line — a PASS built on crash-catches prints the same PASS.

These rules bind new probes and repairs of old ones; they are not a mandate to
retrofit every historical probe. Where an old probe is touched for another
reason, bring its harness to this standard in the same change.

## 2026-08-31 — Source-native representation kernels Lean-checked

`Lean/GUFormalization/SourceNativeSpin64Observation.lean` proves the general
linear-algebra obstruction behind the exact finite probe: if normal Clifford
multiplication has a right inverse, a nonzero horizontal trace has an ambient
gamma-traceless lift whose literal pullback retains that nonzero trace.
`Lean/GUFormalization/SourceNativeAdjointCoupling.lean` checks the supplied
finite representation supports and Pati--Salam multiplicities, yielding the
exact cubic/linear/quadratic owner split. The theorem statements do not derive
the representation tables or construct physical/source-owned data. Axiom
output is recorded by the default group-action receipt module; W99 carries
independent positive and negative finite controls.
