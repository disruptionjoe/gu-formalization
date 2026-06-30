---
title: "Lean + mathlib Robustness Layer Review"
status: active_research
doc_type: roadmap
updated_at: "2026-06-27"
scope: "architectural review"
---

# Lean + mathlib Robustness Layer Review

## Executive Recommendation

This repository should introduce Lean 4 + mathlib as a narrow robustness layer, not as
a parallel rewrite of the GU program.

The highest-confidence return is in small mathematical kernels that the repo repeatedly
uses to decide whether claims may be promoted, blocked, or downgraded:

1. finite-dimensional linear algebra and exact rank/nullity claims;
2. small characteristic-class arithmetic over `F_2`;
3. Clifford/signature/projector identities;
4. representation-theoretic multiplicity certificates;
5. abstract ordered/readout/category lemmas;
6. dependency-status invariants for claim DAGs.

The lowest return is in trying to formalize the full noncompact `Y14` index story,
spin geometry, APS/Dai-Freed/bordism machinery, or the physical GU action layer before
the mathematical objects are fully specified. Those are currently bottlenecks for Lean
and for the repo itself.

The right five-year posture is: make Lean certify the small pieces that keep causing
claim drift, then let prose and ordinary mathematical exposition carry the higher-level
research until those higher-level objects become stable enough to deserve formalization.

## Current Repository Architecture From a Formal-Verification View

The repository is already designed as a guarded reconstruction program, not as an
unqualified proof. The README states that the repo is "not a proof of Geometric Unity"
and emphasizes assumptions, rollback conditions, correction logs, no-go audits, and
proof-grade labels. `RESEARCH-STATUS.md` adds a claim-status consistency rule:
downstream claims cannot outrank their weakest load-bearing dependency. The
claim-status workflow in `lab/process/runbooks/claim-status-consistency-quality-workflow.md`
is explicit about stale wording, source-of-truth ordering, and same-session verdict
inflation.

That is a strong informal architecture. The current weakness is that most "proof"
objects are Python audits or prose contracts. They enforce structure, detect target
leakage, and prevent overclaiming, but they do not provide a small trusted kernel for
mathematical facts. This makes them good governance tests, not proof certificates.

Representative evidence:

- `tests/live_claim_dag_audit.py` checks node IDs, status enums, proof-grade enums,
  and dependency references, but it does not prove any mathematical claim.
- Many tests explicitly state they are "structural audits" or "not a proof"; examples
  include QFT shadow extraction, source-geometry, stress-energy, VZ E-block, K3 bridge,
  and RS symbol/index audits.
- `tests/rs_k3_symbol_index_formula_audit.py` correctly quarantines the physical
  generation count and skips tests whose data are not supplied.
- `tests/oq_rk1_cl95_explicit_rep.py`, `tests/rs_clifford_projector_model.py`,
  `tests/shiab_codiff_intertwiner_dim.py`, and `tests/shiab_family_basis.py` are closer
  to mathematical certificates because they compute explicit finite algebra.

There are no existing Lean files, `lakefile.lean`, or `lean-toolchain` files in the
repo at the time of this review.

## Where Lean Would Have Prevented Past Drift

Lean would not have prevented every correction. Several corrections are due to missing
physical input, not proof sloppiness. But Lean would have materially reduced risk in
four recurring classes.

### 1. Dropped-Term Algebra

The `w2(Y14)` correction is the clearest case. The canon file records that an earlier
unconditional spin claim was false because a `w2(V)` term was dropped in the
`V tensor L` factor. The corrected statement is `w2(Y14) = pi*w2(X4)`, so `Y14` is spin
iff `X4` is spin.

A small Lean file proving the relevant `F_2` polynomial identities would likely have
caught this before promotion:

- `w2(Sym^2 V) = w1(V)^2 + w2(V)` for rank 3;
- `w2(V tensor L) = w2(V) + w1(L)^2` under the oriented-line simplification used here;
- Whitney-product assembly with all degree-2 terms explicit.

This does not require formalizing Stiefel-Whitney classes topologically on day one.
It can begin as an axiomatized graded-commutative `F_2` algebra calculation with named
classes and a later boundary to topology.

### 2. Circular Preconditions

The VZ downgrade records that a Schur complement proof used `E^{-1}` before directly
establishing `E(xi)` invertible. Lean is good at making this kind of precondition
visible: a Schur-complement theorem would require an explicit `[Invertible E]` or
`IsUnit E` hypothesis, so the proof could not silently use the conclusion.

Lean would not automatically prove the E-block invertibility. It would prevent the
determinant identity from being treated as an invertibility proof unless that theorem
had actually been stated and checked.

### 3. Target-Imported Arithmetic

The generation-count lane repeatedly guards against shortcuts such as
`ind_H(D_GU)=chi(K3)=24`, target division by `8/Ahat(K3)`, and deriving rank 4 or 8 from
the desired number. These are partly governance problems, but they also have a natural
formal interface:

- encode the symbolic K3 index expression as a theorem;
- leave `q`, `ch2(F)[K3]`, APS/eta data, and physical RS symbol class as parameters;
- prove that no theorem with the current inputs yields the target rank.

Lean cannot prove absence of all possible routes, but it can make the current route
typed: a theorem requiring `PhysicalRSSymbolClass` cannot be invoked until that object is
constructed.

### 4. Equivariance Does Not Imply Uniqueness

The shiab lane is now corrected: equivariance alone does not pin a unique map. The repo
currently relies on exact Python algorithms and cross-checks. A Lean certificate for the
finite representation-theoretic data would substantially improve long-term confidence,
because this result is load-bearing for the selector-identity boundary.

The highest-value Lean target is not the whole D7 representation theory stack at first.
It is a certificate that the two stated decompositions imply
`dim Hom(Lambda^2 V tensor S+, V tensor S-) = 2`, and hence uniqueness fails. The
decomposition engine can remain external initially if Lean checks the certificate.

## Closest Current Results To Formalization

| Candidate | Current artifact | Why it maps to Lean | Difficulty | Payoff | mathlib status |
|---|---|---:|---:|---:|---|
| K3 arithmetic and forbidden target division | `tests/rs_k3_symbol_index_formula_audit.py`, `tests/cycle1_generation_rs_rank_direct_gate_audit.py` | integer/rational formulas, skipped unknowns, symbolic parameters | Low | High | Available: rings, integers, matrices, finite-dimensional linear algebra |
| Claim-status partial order and dependency monotonicity | `lab/process/runbooks/claim-status-consistency-quality-workflow.md`, `tests/live_claim_dag_audit.py` | finite DAG/status invariant, no stronger downstream claim | Low | Medium | Available: lists/finite types/order relations; graph support enough |
| Signed-readout core | `lab/active-research/signed-readout/` and related status rows | ordered monoids/groups, nonnegative weights, monotonicity theorem | Low-Medium | Medium-High | Available: order algebra, category basics |
| `w2` polynomial identities | `canon/w2-y14-spin-structure.md` | finite `F_2` polynomial identities and Whitney-style algebra | Medium | High | Algebra available; characteristic-class topology mostly missing |
| Explicit Clifford/projector ranks | `tests/oq_rk1_cl95_explicit_rep.py`, `tests/rs_clifford_projector_model.py` | exact finite matrices, projectors, rank/nullity | Medium | High | Matrix/linear algebra/Clifford algebra available; exact matrix certificates need work |
| VZ Schur precondition layer | `RESEARCH-STATUS.md` VZ corrections, `tests/cycle2_vz_actual_operator_e_block_audit.py` | theorem API can force invertibility/domain/cone hypotheses | Medium | High | Matrix algebra available; actual Clifford proof may be hard |
| Shiab Hom multiplicity certificate | `tests/shiab_codiff_intertwiner_dim.py`, `tests/shiab_family_basis.py` | finite Weyl-character/decomposition certificate | High | High | Lie algebra/weights partial; no turnkey D7 multiplicity engine |
| Type II1 finite sign package | `canon/type-ii1-spectral-sm-checklist.md`, related explorations | KO sign tables, finite algebraic real-structure checks | Medium | Medium | Finite algebra available; operator-algebra/semifinite NCG largely missing |
| Category-scope exits and C_SR category | DG audit, C_MPR/category notes | category axioms, functor nondefinition boundaries | Medium | Medium | Category theory strong; physical categories must be defined locally |
| Full noncompact `Y14` index/APS/Fredholm/spin geometry | K3/families route, RS-BRST, Freed-Hopkins lanes | very large analytic and geometric stack | Very High | Low now, High later | Largely missing for this purpose |

## Prioritized Candidate Areas

### Priority 1: Lean "kernel certificates" for arithmetic and dependency gates

**Scope.** Create a small Lean package with:

- a `Status` enum and an order such as `blocked <= open <= conditionally_resolved <= resolved <= verified`;
- finite claim DAG validation for owner-specified claims;
- symbolic RS/K3 index arithmetic with parameters left explicit;
- theorem statements that forbid deriving a generation count unless required data exist.

**Difficulty.** Low.

**Payoff.** High for claim drift, medium for mathematics.

**mathlib.** Already available.

**Boundary.** Python can still parse Markdown and JSON; Lean checks the finite theorem
kernel. Do not make Lean parse the whole repo.

### Priority 2: Characteristic-class arithmetic shim

**Scope.** Formalize the algebraic part of the `w2(Y14)` correction:

- degree-1 roots over `F_2`;
- total Stiefel-Whitney class as a formal polynomial;
- `Sym^2` and tensor-with-line degree-2 computations;
- Whitney assembly producing `w2(Y14)=pi*w2(X4)` under the stated assumptions.

**Difficulty.** Medium if kept algebraic; high if full topology is attempted.

**Payoff.** High. This exact class of error already caused a canon correction.

**mathlib.** Polynomial/ring/algebra support is available. Full characteristic classes
do not appear to be a mature mathlib surface, so use an axiomatized boundary first.

**Boundary.** The Lean theorem should certify the formal algebraic calculation. The prose
file should still carry the topological interpretation and hypotheses.

### Priority 3: Exact Clifford/projector certificates

**Scope.** Replace or augment numerical `numpy` checks with exact Lean certificates for:

- Clifford relations for the chosen gamma matrices;
- chirality projectors and rank;
- gamma-trace kernel dimension in the finite Cl(4,0) toy;
- selected Cl(9,5) finite identities that are small enough to prove exactly;
- Schur complement theorem requiring explicit invertibility.

**Difficulty.** Medium for small matrices; medium-high for full Cl(9,5) rank unless
certificate-based.

**Payoff.** High. This guards VZ, RS rank, and shiab-family work.

**mathlib.** Matrices, finite-dimensional linear algebra, quadratic forms, tensor products,
and `CliffordAlgebra` exist. Out-of-the-box spinor-representation classification is not
the right dependency; prefer explicit matrices or finite certificates.

**Boundary.** Keep large numerical searches in Python/Sage when useful, but export small
rank/equivalence witnesses that Lean checks.

### Priority 4: Shiab multiplicity certificate

**Scope.** Formalize the conclusion:

`dim Hom(Lambda^2 V tensor S+, V tensor S-) = 2`, with the analogous block table.

**Implementation strategy.**

1. Phase A: Lean checks a finite certificate: two decompositions plus Schur's lemma
   imply the Hom dimension.
2. Phase B: Lean checks a Weyl-character/Racah-Speiser certificate for D7.
3. Phase C: only if needed, build reusable Dn highest-weight infrastructure.

**Difficulty.** High if built from first principles; medium-high with certificates.

**Payoff.** High. It locks a major correction: equivariance alone does not select the
GU operator.

**mathlib.** Partially available. mathlib has Lie algebras, root systems, weights, and
basic representation theory, but the specific D7 decomposition workflow would likely
need new project-local formalization.

**Boundary.** Do not formalize all representation theory. Formalize exactly enough to
make "dim > 1" robust.

### Priority 5: Signed-readout and finite observer/category kernels

**Scope.** Formalize the small abstract Mission B results:

- monotonicity iff all weights lie in the positive cone;
- PN/Jordan-style decomposition at the algebraic level;
- C_SR category object/morphism laws;
- record-graph finality predicates for finite DAGs.

**Difficulty.** Low-Medium.

**Payoff.** Medium-High. These tools are reused and conceptually clean.

**mathlib.** Already strong for ordered algebra and category theory.

**Boundary.** Formalize the reusable theorem core, not the GU physical interpretation.

### Priority 6: Type II1 finite-control sign package

**Scope.** Formalize finite sign tables and real-structure compatibility statements:

- `J^2` sign calculations;
- chirality commutation/anticommutation sign table;
- finite Connes-control comparison gates that do not require semifinite von Neumann
  algebra theory.

**Difficulty.** Medium.

**Payoff.** Medium. Valuable, but not as directly claim-drift-critical as w2, RS/K3, or
shiab selector multiplicity.

**mathlib.** Finite algebra is available. Semifinite spectral triples, modular
Tomita-Takesaki machinery, and Type II1 operator algebra infrastructure would be
substantial new formalization.

### Priority 7: Full analytic/index-theoretic stack

**Scope.** Noncompact `Y14` Fredholmness, APS eta corrections, KSp/KO families index,
Dai-Freed/global anomaly, spin geometry, and physical RS-BRST complexes.

**Difficulty.** Very high.

**Payoff.** Low now, because the repository itself records missing GU data in several
places: physical RS action/BRST data, gauge fixing, same-operator bridge, `ch2(F)`, APS
boundary data, and KSp/KO pushforward objects.

**mathlib.** Largely missing for this exact purpose. Manifolds and vector bundles exist,
but not enough of spin geometry, topological K-theory, characteristic classes, APS index
theory, or Dai-Freed anomaly machinery to make this efficient.

**Boundary.** Do not attempt this until the informal research has stabilized the object
being formalized.

## mathlib Coverage Assessment

This assessment uses public mathlib documentation and project pages checked on
2026-06-27.

| Domain | Status for this repo | Notes |
|---|---|---|
| finite-dimensional linear algebra | Already available | mathlib has modules, linear maps, bases, finite dimensionality, matrices, determinants, rank-related infrastructure, bilinear/quadratic forms |
| tensor/exterior/Clifford algebra | Partially to strongly available | `TensorAlgebra`, `ExteriorAlgebra`, and `CliffordAlgebra` are listed; explicit finite Clifford certificates are realistic |
| matrices/projectors/rank | Already available | Best near-term target for exact replacement of numerical projector checks |
| category theory | Already available | Categories, functors, adjunctions, limits/colimits, over categories, homological algebra, triangulated-category infrastructure exist |
| homological algebra | Already available/partial | Chain complexes, homology, exact sequences, spectral sequences are represented; useful for formal skeletons, not full physics BRST by itself |
| representation theory | Partially available | `Representation`, `FDRep`, characters, Lie weights/root systems exist; D7 highest-weight decomposition machinery likely needs project-local work |
| Lie algebras | Partially available | Lie algebra basics, Cartan, root systems, Serre construction, semisimple files exist; Lie groups and analytic representation theory are much thinner |
| manifolds/differential geometry | Partially available | Smooth manifolds, manifold derivative, tangent bundles, vector bundles, pullbacks, Riemannian vector bundles exist; advanced spin/Dirac/index theory is not ready enough |
| topology | Broad basics available | General topology, compact/Hausdorff categories, CW complexes exist; specialized KSp/KO/index stack not available as needed |
| Clifford/spin geometry | Clifford available, spin geometry largely missing | Algebraic Clifford layer is realistic; spinor bundles, spin structures, Dirac operators, APS theory would be new work |
| characteristic classes | Largely missing for current need | Use algebraic shims first for `w2` polynomial identities |
| K-theory / KO / KSp | Largely missing for current need | Do not base near-term roadmap on full KSp families index formalization |
| operator algebras / Type II1 | Largely missing for current need | Finite sign/algebra checks are realistic; semifinite spectral triples are not a quick win |
| differential equations / GR / physical action | Bottleneck | Lean can help with tensor identities eventually, but the repo lacks stable source-level objects in key places |
| anomaly/bordism/Dai-Freed | Bottleneck | High research value but currently poor confidence per unit effort |

Useful external references:

- mathlib overview: https://leanprover-community.github.io/mathlib-overview.html
- mathlib full index: https://leanprover-community.github.io/mathlib4_docs/Mathlib
- mathlib overview source listing algebra, Clifford, representation theory, and linear
  algebra: https://github.com/leanprover-community/mathlib4/blob/master/docs/overview.yaml
- manifold derivative docs:
  https://leanprover-community.github.io/mathlib4_docs/Mathlib/Geometry/Manifold/MFDeriv/Defs.html
- vector bundle docs:
  https://leanprover-community.github.io/mathlib4_docs/Mathlib/Geometry/Manifold/VectorBundle/Basic.html
- tangent bundle docs:
  https://leanprover-community.github.io/mathlib4_docs/Mathlib/Geometry/Manifold/VectorBundle/Tangent.html
- pullback vector bundle docs:
  https://leanprover-community.github.io/mathlib4_docs/Mathlib/Geometry/Manifold/VectorBundle/Pullback.html
- Riemannian vector bundle docs:
  https://leanprover-community.github.io/mathlib4_docs/Mathlib/Geometry/Manifold/VectorBundle/Riemannian.html
- category adjunction docs:
  https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/Adjunction/Basic.html
- homological complex docs:
  https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Homology/HomologicalComplex.html

## Where Lean Would Become a Bottleneck

Lean becomes a bottleneck when the formalization target is not a stable mathematical
object yet, or when the required library stack is much larger than the claim being
checked.

Avoid near-term Lean work on:

- the full noncompact `Y14` analytic index;
- APS/b/scattering calculus;
- Dai-Freed/global anomaly classification;
- full Freed-Hopkins bordism machinery;
- Type II1 spectral triples beyond finite sign/package checks;
- exact GR or dark-energy field-equation derivations unless the action and variation
  spaces are fully specified;
- full D7 representation theory from first principles unless the project commits to
  maintaining it as a reusable library.

In these areas, Lean can still help later by enforcing definitions and dependencies, but
using it now would mostly create maintenance cost and delay the research.

## Recommended Formalization Boundaries

The right interface is a proof-carrying kernel, not proof-carrying everything.

### Boundary A: Prose owns interpretation; Lean owns finite kernels

Example: `canon/w2-y14-spin-structure.md` should keep the geometric discussion, source
interpretation, and Milnor-Stasheff citation. Lean should own the formal `F_2`
polynomial calculation that makes dropped terms impossible.

### Boundary B: Python/Sage may discover; Lean verifies certificates

The current Python scripts are valuable exploration tools. Keep them for search,
matrix generation, and heavy computation. Add exportable certificates:

- decomposition tables;
- explicit basis/rank witnesses;
- kernel/projector witnesses;
- invertibility witnesses;
- finite DAG/status tables.

Lean should check the witness, not repeat every search algorithm.

### Boundary C: Markdown claim pages cite Lean theorem IDs

For any Lean-certified result, add a small block to the owning Markdown artifact:

```text
formal_certificate:
  lean_file: Lean/GUFormalization/W2.lean
  theorem: GU.W2.y14_spin_iff_base_spin
  scope: algebraic_SW_class_calculation_only
  does_not_claim: full_noncompact_index
```

This mirrors the repo's current machine-readable JSON blocks without forcing all prose
into Lean.

### Boundary D: Lean theorem dependencies mirror claim dependencies

If a claim depends on `PhysicalRSSymbolClass`, `GaugeFixingSlice`, or
`Ch2Background`, those should be parameters or typeclasses in the Lean statement. This
prevents a proof from silently importing the target.

### Boundary E: No `sorry` in CI certificates

Exploratory Lean files may contain `sorry`, but certified files referenced by canon,
active research, or roadmap gates should build with `set_option autoImplicit false` and
no `sorry`.

## Comparison With Current Research Practice

The repository should borrow practices from successful Lean projects without copying
their scale.

### FLT and large theorem projects

The Fermat's Last Theorem formalization uses blueprint software: a human-readable proof
map linked to Lean objects. The key lesson is not "formalize everything"; it is "make the
dependency graph explicit and modular so contributors can work locally." This repo
already has a claim DAG and correction system. A lightweight blueprint for Lean kernels
would fit naturally.

Source: https://lean-lang.org/use-cases/flt/

### Equational Theories Project

The Equational Theories Project separates conjectured from Lean-verified implications,
uses dashboards, and combines humans, automation, finite counterexamples, and Lean. This
is directly relevant: the GU repo already distinguishes `OPEN`, `CONDITIONALLY_RESOLVED`,
and `verified/reconstruction/speculation`. The practice to import is a visible dashboard
of "Lean-certified", "Python-audited", "prose-only", and "blocked-missing-object" claims.

Source: https://teorth.github.io/equational_theories/

### Physlib / PhysLean

Physlib shows that physics formalization in Lean is real but still infrastructure-heavy.
The practice to import is API-building around stable physics concepts, not premature
formalization of a whole physical theory. For this repo, the stable APIs are likely
finite spinor/Clifford/projector objects, not the full GU action.

Source: https://github.com/leanprover-community/physlib

### AI-assisted Lean projects

LeanDojo-v2 and related AI theorem-proving tools use repository tracing, theorem
information extraction, proof-state data, retrieval, and proof search. This points to a
longer-term opportunity: once the repo has a Lean kernel, it can expose high-quality
formal theorem nodes for AI-assisted maintenance. But AI should assist the kernel, not
replace the requirement that the Lean files build.

Source: https://leandojo.org/leandojo.html

### Mathlib Initiative practice

The Mathlib Initiative roadmap emphasizes review cycles, ecosystem support, and tooling
for AI training data extraction. For this repo, that argues for a small, well-maintained
Lean package with stable imports rather than a pile of experimental files that bit-rot.

Source: https://mathlib-initiative.org/roadmap/

## Roadmap

### Implementation status

Initial scaffold started 2026-06-27:

- `lean-toolchain` and `lakefile.lean` added for a Lean 4 + mathlib package.
- First certificate modules added under `Lean/GUFormalization/`:
  `Status.lean`, `K3IndexArithmetic.lean`, and `W2Polynomial.lean`.
- Owner-surface certificate blocks added for the claim-status workflow, the K3
  generation-count gate, and the corrected `w2(Y14)` algebra.
- `tests/lean_certificate_surface_audit.py` checks the integration surface without
  requiring Lean to be installed.
- `.github/workflows/lean.yml` runs the Lean build in CI via `leanprover/lean-action`.

### Quick wins: weeks

1. Add a minimal Lean package:
   - `lean-toolchain`;
   - `lakefile.lean`;
   - `GUFormalization/Status.lean`;
   - `GUFormalization/K3IndexArithmetic.lean`;
   - `GUFormalization/W2Polynomial.lean`;
   - CI or local script to run `lake build`.

2. Formalize the status-order invariant:
   - define statuses and proof grades;
   - prove a finite dependency checker theorem for sample DAGs;
   - keep Markdown parsing in Python.

3. Formalize K3 arithmetic:
   - encode `Ahat(K3)=2`, `chi(K3)=24`, `sigma(K3)=-16`, `p1=-48` as assumptions/data;
   - prove the index formula currently used by the audit;
   - prove that the formula still depends on missing parameters and does not by itself
     imply the generation count.

4. Formalize the `w2` polynomial shim:
   - prove the corrected degree-2 identities over `F_2`;
   - cite the Lean theorem from `canon/w2-y14-spin-structure.md`.

5. Add a "formal certificate" block format to one or two Markdown owners.

### Medium-term investments: months

1. Exact matrix certificates for Clifford/projector facts:
   - start with Cl(4,0) toy projectors;
   - then add small exact witnesses for selected Cl(9,5) facts;
   - use certificate-style proofs for large ranks.

2. Shiab multiplicity certificate:
   - Lean-check the decomposition-to-Hom-dimension implication;
   - import a finite decomposition table as data;
   - only later formalize Racah-Speiser/Klimyk if reuse justifies it.

3. VZ Schur-precondition API:
   - prove a general matrix theorem whose statement forces invertibility of the E-block;
   - refactor VZ prose to cite the theorem as a guardrail, not as a full evasion proof.

4. Signed-readout theorem kernel:
   - formalize monotonicity and finite record-graph lemmas;
   - keep GU interpretation separate.

5. Build a small "Lean certificate dashboard":
   - certified by Lean;
   - audited by Python;
   - prose/reconstruction only;
   - blocked on missing source object.

### Long-term infrastructure: years

1. Project-local finite representation theory library:
   - Dn roots and weights;
   - Weyl group finite certificates;
   - highest-weight decomposition certificates;
   - enough to support all recurring Spin(9,5)/D7 bookkeeping.

2. A reusable Clifford/spinor certificate layer:
   - explicit gamma models;
   - chirality, real/quaternionic structures;
   - finite Clifford-module maps;
   - rank/H-rank conversion theorems with exact hypotheses.

3. Formal source-to-index scaffolding, only after source objects exist:
   - typed placeholders for physical RS-BRST data;
   - symbol-class boundary;
   - K3/APS/eta slots as explicit assumptions;
   - no attempt at full proof until those slots are mathematically populated.

4. Selective upstream contributions to mathlib:
   - small characteristic-class algebra APIs;
   - Clifford matrix certificate utilities;
   - representation-theory certificate helpers;
   - only upstream material that has general value beyond GU.

5. AI-native theorem maintenance:
   - use LeanDojo-style tracing or equivalent tooling on the project-local Lean package;
   - mine theorem dependencies for claim-drift alerts;
   - let agents propose Lean patches, but keep CI as the arbiter.

## Final Recommendation

If this repository is going to become one of the strongest AI-native mathematical
research programs over the next five years, Lean should be introduced as a small trusted
spine under the highest-risk mathematical gates.

Do not ask "Should GU be formalized in Lean?" Ask:

> Which small theorem, if machine-checked, prevents the next false promotion, hidden
> target import, or repeated algebraic mistake?

The first Lean targets should be `w2` arithmetic, K3/index arithmetic, claim-dependency
invariants, and finite Clifford/projector facts. The second wave should add
representation-theoretic certificates and signed-readout/category kernels. The full
noncompact index, spin geometry, anomaly, and physical action layers should remain prose
and traditional mathematics until their objects are stable enough that Lean would verify
them rather than define the research problem.
