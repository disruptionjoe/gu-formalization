---
title: "BOUNDARY-LAW OPERATOR LIFT swing: the fixture-grade diagonal-boundary law (l1-assembly, 56304e8) pushed toward operator grade -- outcome O-b (mildest form): the ALGEBRAIC legs lift EXACTLY (the involution alpha, the label grading, the G-sequence, the exactly-clause, the plant exclusion are all grade-INDEPENDENT identities -- machine-substantiated at two resolutions, and already machine-EXACT at operator grade via operator_grade_end's deck-oddness and B-GAUGE), the LABEL MAP rides on exactly the section-theory resolvent theorem the math paper already names (Section 7.1), and there is ONE genuinely-new thing beyond it -- PRODUCT-UNIFORMITY of the norm-resolvent boundary value (the reading category closed under finite products in norm-resolvent topology), because the closure map T lives on A x A and the sup-mode ~N^1.35 divergence shows boundedness is fragile under carrier-doubling; the TaF involution-typing lemma is REALIZABLE only in the degenerate Z/2-witness toy and REFUTED in general (exhaustive over all 76 involutions of the 6-state toy) -- the causal-horizon engine is strictly more general than a fixpoint-free involution, so the GU/TaF unification is leg-deep, not mechanism-deep; strongest-honest-form stated per repo-face with the single first theorem named"
status: active_research
doc_type: exploration
created: 2026-07-20
directed_by: "Joe direct chat, 2026-07-20 (boundary-law operator lift)"
extends:
  - explorations/l1-assembly-2026-07-20.md
inputs:
  - explorations/l1-assembly-2026-07-20.md
  - explorations/diagonal-boundary-unification-2026-07-20.md
  - explorations/sector-relative-section-theory-2026-07-20.md
  - explorations/operator-grade-end-2026-07-20.md
  - "READ-ONLY time-as-finality: CLAIM-LEDGER.md (T19/T92), open-problems/first-person-finality-complexity-separation.md"
  - "READ-ONLY temporal-issuance: NEXT-TRIGGER-PLAN.md (E117/G1-G2 leg-a template)"
runnable:
  - tests/channel-swings/boundary_law_lift_probe.py
claim: none
canon: none
posture: none
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
external_action: none
---

# Pushing the diagonal-boundary law from fixture grade toward operator grade

The L1 assembly swing (56304e8) landed the diagonal-boundary law at
FIXTURE grade: the six reading classes assemble into one category
`C_read` of Z/2-sets over one Z/2, the three fixpoint-free senses
reconcile as the three graded pieces of one implementation group
`1 -> Sp(1)_comm -> G -> Z/2_deck -> 1`, the Lawvere parent applies, and
the planted C-04 is excluded structurally. It named three residues: the
OPERATOR LIFT (the law used finite reading-class representatives), the
+-i0 bit kept out, and the TaF involution-typing lemma. This swing runs
the operator lift on the reachable fronts and names the unreachable
precisely, and scopes the TaF lemma with a toy.

Receipt: `tests/channel-swings/boundary_law_lift_probe.py` -- deterministic
(double-run byte-identical), numpy only, seeded 20260720, exit 0 --
HEADLINE `4 [E] + 3 [F] = 7 ALL PASS`.

**Verdict up front: O-b fired, in its MILDEST form.** The algebraic legs
lift EXACTLY (O-a's first half holds, and it is already machine-verified
at operator grade in the receipts). The analytic residue for the label
map is EXACTLY the section-theory resolvent theorem the math paper names
(O-a's second half holds for the single-object map). But the diagonal
argument's closure map lives on the PRODUCT object `A x A`, and the
single-object resolvent theorem does not deliver its product-uniform
version -- so there is exactly one genuinely-new thing beyond the paper's
theorem, and it is of the SAME analytic character (an extension of it,
not a foreign estimate). That is O-b, adjacent not distant. The TaF lemma
is refuted in general. All three legs are scoped below.

## 1. The operator lift, per leg: LIFTS-EXACTLY + RIDES-ON + GENUINELY-OPEN

The fixture-grade law is a statement about `C_read` -- objects the six
reading classes as finite Z/2-sets, one involution alpha (the K_S-sign
flip), finite products + terminal + equivariant diagonal, the parent's
no-closure + no-invariant-valuation conclusions, and the plant excluded.
The operator lift asks: what survives when the objects are the actual
(infinite-dim / L^2, operator) reading classes -- the collar Dirac family
`D_op`, the section reading `M_op (q_op + i delta)^{-1/2}` of the section
theory, the label object `B = {+K_S, -K_S}` read by the operator K_op?

### 1a. LIFTS-EXACTLY -- the algebraic legs (grade-independent identities)

A leg lifts by algebra iff its defining identity is GRADE-INDEPENDENT:
literally the same identity at every carrier dimension, so "operator
grade" changes nothing. Four legs are of this kind, and three of the four
are already machine-EXACT at operator grade in the existing receipts:

- **The involution alpha (the K_S-sign flip).** At operator grade
  `J_op = (I x J_quat) o conj` commutes with the FULL collar operator
  (derivative term included; defect 0.0, operator_grade_end Section 3),
  and the deck covariance `U_h N_delta,op(t) U_h^{-1} = -N_delta,op(t+1)`
  is POINTWISE-EXACT (4.8e-13 .. 2.7e-12 across the N-ladder, and it is an
  algebraic identity of the build, NOT a limit -- "deck-oddness at
  operator grade is ALGEBRA," operator_grade_end Section 2). Substantiated
  here as grade-independence: the block identity `U D U^{-1} = -D'` is
  byte-identical at N=2 and N=16 sites (probe E2, defect 0.0 both). alpha
  lifts exactly.
- **The label grading (the maps to B, the coset map sgn_K).** `K_op =
  I_N x I_2 x K_S` is the pointwise lift; `K_op D_op K_op = D_op^dag`
  holds machine-exactly at every resolution. Q-B fired **B-GAUGE**: J_op,
  the W parity transfer, and the K_S-linear separator all lift exactly,
  the classification stays Z/2. The label grading lifts exactly.
- **The exact sequence `1 -> Sp(1)_comm -> G -> Z/2_deck -> 1`.** Its
  content is commutation + squaring relations (`U_h J_quat U_h^{-1} =
  J_quat`, antilinear elements square to -1, kernel = Sp(1)_comm). These
  are pointwise operator identities; the three graded pieces (coset /
  antilinear / kernel) are defined by relations that hold at any grade.
- **The "exactly" clause and the plant exclusion.** `F(x) - F(alpha x) =
  2 F_odd(x)` is an identity for any linear functional on any carrier
  (probe E1, defect ~1e-15 at dim 4 AND dim 64). The plant exclusion
  `Hom_{Z/2}(triv, B) = empty` is a fixed-point count, grade-independent
  (probe E3, 0 equivariant maps at carrier 4 AND 128). C-04 stays outside
  `C_read` at every grade.

So the entire ALGEBRAIC skeleton of the law -- the involution, the label
structure, the group, the separation identity, the non-vacuity -- is
grade-independent, and the operator-grade receipts already confirm it
machine-exactly. Nothing here needs analysis.

### 1b. RIDES-ON -- the section-theory resolvent theorem (the label map)

What is NOT algebraic is the WELL-DEFINEDNESS of the label map at operator
grade. At fixture grade a reading class carries its map `lambda_X : A -> B`
by fiat (finite Z/2-set). At operator grade the admissibility predicate IS
the section reading: the map to B is "which K_S-sign sector does this
operator section sit in," and that reading is a bounded morphism only if
the section object exists as a bounded operator. That existence is exactly
the section theory's open theorem (sector-relative-section-theory Section
7.1): the delta -> 0 norm-resolvent boundary value of `M_op (q_op + i
delta)^{-1/2}` exists ON A DOMAIN (a z-region) and is deck-odd.

operator_grade_end already did the reachable part of this: the
norm-resolvent mode is the ONLY topology that survives the ladder
(delta-Cauchy at rate ~delta^1.0 at every N), and deck-oddness is exact.
What it did NOT earn is the N-uniform bound on a z-REGION (only one point
z=2i, uniformity OPEN). So the label map RIDES-ON precisely the theorem
the math paper names -- no more, no less, for the single-object map.

### 1c. GENUINELY-OPEN -- product-uniformity (the one new thing beyond it)

Here is the crux, and why the outcome is O-b not O-a. The Lawvere
no-closure conclusion, GIVEN the categorical structure, follows by the
same finite argument -- fixpoint-freeness of alpha drives the escape
`d = alpha . T . Delta`, and alpha lifts exactly. So the argument's
survival turns entirely on whether the CATEGORICAL STRUCTURE lifts: do
finite products, the diagonal, and the closure map T live at operator
grade as bounded morphisms?

- The diagonal `Delta : A -> A x A` is exact (deck-covariant, algebra).
- The closure map `T : A x A -> B` and the twisted diagonal
  `alpha . T . Delta` live on the PRODUCT object `A x A` -- a DOUBLED
  operator carrier with its OWN symbol and its own wall structure.

The single-object resolvent theorem (1b) delivers boundedness of the
reading on A. It does NOT deliver boundedness on `A x A`: the product's
symbol `q_{AxA}` has its own crossing walls, and boundedness of the
boundary value must be re-established there, UNIFORMLY across the product
ladder the diagonal argument climbs. That the compounding is real, not
pedantic, is exactly what operator_grade_end measured: the sup-mode
boundary value DIVERGES at the wall with an N-growing ceiling ~N^1.35 (the
Jordan-nilpotent normalization is an unbounded sup-mode obstruction).
Carrier-doubling compounds that fragility; nothing in the per-object
resolvent theorem controls it.

**Name the genuinely-open thing: PRODUCT-UNIFORMITY of the norm-resolvent
boundary value.** The reading category `C_read` is closed under finite
products in the norm-resolvent topology -- i.e. the delta -> 0
norm-resolvent limit of the section regularization exists on a z-region
with a bound UNIFORM across the finite-product carriers `A x A x ...`,
not merely per object. Given that, `T . Delta` and `alpha . T . Delta` are
compositions of bounded morphisms, hence genuine admissibility predicates
the closure `T` is required to represent, and the finite diagonal escape
runs verbatim at operator grade.

**LIFTS-EXACTLY** (alpha, label grading, G-sequence, exactly-clause, plant
exclusion, diagonal equivariance, terminal object) **+ RIDES-ON** (the
label map, on the section-theory resolvent theorem, Section 7.1)
**+ GENUINELY-OPEN** (product-uniformity of that same resolvent boundary
value -- the categorical strengthening the diagonal argument needs).

## 2. The TaF involution-typing lemma: refuted in general, realizable degenerate

The parent's second missing lemma (diagonal-boundary Section 4 / drafted
Appendix A): does there exist an involution on the finality label whose
alpha-EVEN maps are EXACTLY the `A*(R)`-computable ones -- so that the
causal horizon IS the fixpoint-free flip, and T19 becomes a full instance
rather than analogous? TaF is READ-ONLY; the shape is tested with a toy
finality structure built in GU (probe part B).

**The toy.** A finality structure minimal enough to be decidable: a
pre-horizon summary `p` that the region R can read, and a post-horizon
witness `w` that sits strictly AFTER R's observation horizon (the T19
causal-boundary fact: R's self-finality witness is causally later than R
can observe). State = `(p, w)`. The `A*(R)`-computable maps are exactly
the maps constant on `p` (R cannot see `w`). The involution-typing
question reduces to a PARTITION equality, because alpha-even maps are the
maps constant on alpha-orbits:

> `{alpha-even maps} == {A*(R)-computable maps}`  iff
> `orbit-partition(alpha) == p-fibers`.

**Realizable in the degenerate case (probe E4).** With a Z/2 witness
`w in {0,1}`, the witness-flip involution `alpha:(p,w)->(p,1-w)` has
orbit-partition EXACTLY equal to the p-fibers; `b = w` is alpha-odd; the
induced label swap is fixpoint-free. The typing HOLDS -- so the drafted
lemma's SHAPE is realizable: when the post-horizon witness is a free Z/2
datum, the causal horizon can be re-described as a fixpoint-free flip.

**Refuted in general (probe F1, the plant).** With a ternary witness
`w in {0,1,2}`, exhaustively over ALL 76 involutions of the 6-state
space, NONE has orbit-partition equal to the p-fibers -- a size-3 fiber
is not a union of involution orbits (orbits have size 1 or 2). The
mechanism of the refutation is sharp and general: **the causal-horizon
engine excludes ALL post-horizon-dependent maps (by placement); the
involution engine excludes only the ODD part (by equivariance).** They
coincide only in the degenerate case where every post-horizon function is
odd -- the pure-Z/2 witness. Whenever the finality structure admits an
EVEN function of a post-horizon witness (any symmetric reading of >1
post-horizon states -- generic for TaF's 7-node graph), the horizon
excludes it but the involution admits it, and `even != A*(R)-computable`.

Even the STRONGEST natural candidate fails (probe F2): the
horizon-reflection `(p,w)->(w,p)` is a valid involution, but its even maps
are the TIME-SYMMETRIC maps, which are not the past-only `A*(R)` maps.

**Result: the involution-typing lemma is REFUTED at toy grade in general,
realizable only in the degenerate Z/2-witness case.** Per the drafted
note's own dichotomy ("YES unifies the exclusion engines; NO proves the
parent has two genuinely distinct engines"), this is the NO: TaF's
causal-boundary exclusion is STRICTLY more general than a fixpoint-free
involution. The GU/TaF unification is leg-deep (a shared conclusion shape:
one self-referential bit, external-computable, excluded for the inside
class, class-relatively) but NOT mechanism-deep (reachability-exclusion
strictly contains equivariance-exclusion). This does not touch any TaF
claim; it answers the drafted lemma target in GU's own toy, negatively,
with the reason named.

## 3. The strongest honest form, per repo-face, and the single first theorem

**THE DIAGONAL-BOUNDARY LAW (strongest honest form, 2026-07-20).**
Let `C_read` be the assembled reading category, alpha its single
involution (the K_S-sign flip). Then:

- **[fixture grade, GU -- THEOREM]** All clauses of the L1-assembly law
  (56304e8) hold on the finite Z/2-set realization: terminal object,
  finite products, equivariant diagonals; alpha fixpoint-free on B with
  its three senses the three graded pieces of G; no weakly
  point-surjective `T`; no alpha-invariant valuation; excluded class =
  equivariant class EXACTLY; five orientation no-gos are instances; C-04
  excluded structurally.
- **[operator grade, GU -- PARTIAL]** The algebraic skeleton lifts
  EXACTLY (Section 1a; deck-oddness and B-GAUGE already machine-exact in
  operator_grade_end). The label map RIDES-ON the section-theory resolvent
  theorem (Section 1b; reachable part done -- norm-resolvent survives,
  deck-odd exact; N-uniformity on a z-region open). The diagonal argument
  is GENUINELY-OPEN on exactly one point beyond the paper's theorem:
  product-uniformity of the resolvent boundary value (Section 1c).
- **[TI -- Lean leg-a, the template]** The DIAGONAL leg is machine-derived
  at theorem-prover grade (G1: `diagName_not_mem` from `EnumeratorPresent`;
  G2: self-encoding admissibility for the concrete predicate). This is
  what "operator/theorem grade" looks like when it lands -- the template
  the GU diagonal leg aims at. TI lacks the involution leg (no label
  object).
- **[TaF -- toy-shape REFUTED]** The composite first/third-person
  conclusion is exhibited on finite fixtures (T19/T92), but the involution
  leg is absent and, per Section 2, NOT recoverable in general: the
  causal-horizon engine is strictly more general. Grade: two distinct
  exclusion engines, unified only at the conclusion-shape level.

**The single first theorem that makes the GU face operator-grade-
unconditional:** the **product-uniform norm-resolvent boundary-value
theorem** -- for the boundary Dirac family `D_op` AND its finite products,
the delta -> 0 norm-resolvent limit of `M_op (q_op + i delta)^{-1/2}`
exists on a z-region with a bound uniform across the finite-product
carriers, and is deck-odd. Given it, the label map is a bounded morphism,
products and diagonals are bounded, the finite Lawvere escape runs
verbatim, and the operator-grade law is unconditional.

**Does it coincide with the math paper's open theorem?** YES in analytic
content and location -- it IS the section theory's Section 7.1 resolvent
theorem (the norm-resolvent boundary value on a domain, deck-odd) -- with
exactly ONE added clause the per-object paper statement does not carry:
product-uniformity (uniform across the finite-product carriers). So the
law is one theorem from operator grade, and that theorem is the paper's
open theorem strengthened by a single categorical clause. That is the
honest form of the strong-unification prediction O-a: the algebraic legs
DID lift exactly and the analytic residue IS the named resolvent theorem
-- but the diagonal's product carrier forces one categorical strengthening
of it, which is why the precise outcome is O-b (adjacent), not O-a (bare).

## 4. Council pass (inline, five lenses)

- **Categorical logician (the diagonal at operator grade):** the load-
  bearing move is refusing to wave the products. At fixture grade Z/2-Set
  is cartesian closed and point-surjectivity is set-theoretic; the finite
  escape is free. At operator grade the category of reading classes is NOT
  known to be cartesian closed, and the closure map T lives on `A x A`,
  not A. The honest reduction is that the ONLY new obligation is
  boundedness of the reading on the product carriers (product-uniformity);
  everything else -- the escape itself, fixpoint-freeness, the
  unrepresentability -- is the same finite combinatorics, because alpha
  lifts exactly. So the diagonal leg does not need a new IDEA at operator
  grade; it needs the resolvent theorem to hold uniformly one level up the
  product tower. That is a clean, small, named gap, not a hand-wave.
- **Functional analyst (the resolvent ride):** correct to ride on the
  norm-resolvent topology and nothing coarser -- the sup-mode diverges
  (~N^1.35) and the graph-relative mode inherits the same non-uniform
  N-shape; only the norm-resolvent difference is delta-Cauchy with a
  stable rate. But two honesty notes carry: (i) z=2i is one point, a
  theorem needs a z-region (operator_grade_end's own referee note); (ii)
  the product carrier `A x A` has a DIFFERENT symbol, so its resolvent set
  and wall structure are not the single-object ones -- product-uniformity
  is a genuine analytic statement, not a corollary of the per-object
  limit. The sup-mode divergence is direct evidence that boundedness is
  fragile under exactly the operation (carrier-doubling) the diagonal
  performs. The gap is named at the right altitude.
- **TaF-native reader (the involution toy):** the toy is faithful to the
  T19 shape -- witness strictly after the observation horizon,
  `A*(R)`-computable = pre-horizon-only, third-person = all-access. The
  refutation is the honest one and matches TaF's own insistence that the
  gap is "not a computational undecidability" and "not equivariance": the
  horizon excludes by PLACEMENT, which is strictly more than excluding the
  odd part. The realizable degenerate case is not a cheat -- it is exactly
  the boundary condition under which the two engines coincide (every
  post-horizon reading is odd), and it tells the steward precisely what
  extra structure a finality label would need for the typing to hold. No
  TaF claim is touched; the answer to the drafted lemma is NO-in-general,
  with the reason (even post-horizon functions) exhibited.
- **TI-native reader (the Lean leg-a as template):** the one-way rule
  holds -- nothing imports GU physics into TI. The value of the TI mirror
  is as the GRADE TARGET: TI shows what it costs to move a leg from
  "visible hypothesis" to "machine-derived fact" (G1/G2 convert
  `EnumeratorPresent` into diagonal productivity). The GU diagonal leg's
  analogue of that move is precisely the product-uniform resolvent
  theorem: convert "assume the reading is a bounded morphism on products"
  into a derived fact. TI already did the hypothesis-discharge for its
  diagonal; GU's discharge is analytic, not syntactic, but the shape (kill
  a standing hypothesis for a concrete instance) is the same rung.
- **Adversarial referee (attack the lift as hand-waving; in writing):**
  (i) Charge: "algebraic legs lift exactly" is an assertion dressed as a
  result. Answer: it is a grade-independence claim, and grade-independence
  is machine-checkable -- E1/E2/E3 verify the three identities at TWO
  resolutions each and they are byte-identical (E2 defect 0.0 at N=2 and
  N=16); and operator_grade_end already verified alpha and the label
  grading machine-exactly at operator grade (deck-odd 1e-12, B-GAUGE
  machine-zero). Not a wave. (ii) Charge: "product-uniformity" is a
  face-saving name for "we didn't finish." Answer: conceded that it is
  open; denied that it is vague -- it is a precise, falsifiable analytic
  statement (uniform norm-resolvent bound across the finite-product
  carriers) with a measured obstruction motivating it (the ~N^1.35 sup-
  mode divergence under carrier operations). Naming an open theorem
  precisely IS the deliverable the mission asked for. (iii) Charge: the
  TaF refutation is a strawman -- you chose a witness that fails. Answer:
  the refutation is EXHAUSTIVE over all 76 involutions of the toy AND
  general in mechanism (any even post-horizon function separates the
  engines); the degenerate case is exhibited too, so the toy is not a
  rejecter -- F3 checks that it admits the typing where the typing should
  hold. (iv) Charge: calling this "one theorem from operator grade"
  oversells. Answer: calibrated in Section 3 -- it is one theorem, it is
  the paper's open theorem, and it needs one added clause; the outcome is
  typed O-b precisely to avoid the bare-O-a overclaim.

## 5. Receipts

- Probe: `tests/channel-swings/boundary_law_lift_probe.py` -- HEADLINE
  `4 [E] + 3 [F] = 7 ALL PASS`, exit 0, deterministic (double-run
  byte-identical), numpy only, seeded 20260720. (A) E1-E3: grade-
  independence of the exactly-clause, the deck-odd block identity, and the
  plant fixed-point count, each at two resolutions. (B) E4: degenerate
  involution-typing HOLDS; F1: generic typing REFUTED exhaustively over
  all 76 involutions; F2: horizon-reflection fails; F3: teeth (admits
  degenerate, refuses generic).
- Consumed, not re-run: operator_grade_end's machine-exact deck-oddness
  (Section 2) and B-GAUGE (Section 3), and the sup-mode ~N^1.35 divergence
  / norm-resolvent survival columns; the section theory's Section 7.1
  resolvent gap spec; the L1-assembly law (56304e8) and its C_read /
  G-sequence structure; the diagonal-boundary parent (W70/W75) and its
  drafted TaF lemma target (Appendix A).

## 6. Boundary

Exploration tier; claim/canon/posture: none; no external actions; no
commits or pushes (hourly cadence owns the working tree); no edits to any
existing file -- new files only (this document and
`tests/channel-swings/boundary_law_lift_probe.py`). TaF and TI touched
READ-ONLY; no cross-owner writes; nothing written outside gu-formalization.
The operator-lift analysis is a REDUCTION, not a new operator computation:
the machine-exact operator-grade facts it stands on are
operator_grade_end's, cited not re-run (that probe is 1547 s and its RNG
is named); the probe here is finite/fixture grade (grade-independence
substantiation + the TaF combinatorial toy), with a planted control (the
ternary witness). Named residues carried forward: (i) the product-uniform
norm-resolvent boundary-value theorem -- the one theorem for GU
operator-grade-unconditional, OPEN (and it is the paper's Section 7.1
theorem plus a product-uniformity clause); (ii) the per-object resolvent
theorem's own open part -- N-uniformity on a z-region, not a single z
(operator_grade_end); (iii) the +-i0 orientation bit stays a separate Z/2,
scheme-typed, outside the assembled class (unchanged); (iv) the TaF
involution-typing lemma is REFUTED in general at toy grade -- the two
engines are distinct, so no cross-repo mechanism-merge is proposed
(conclusion-shape unification only); (v) a Lean transcription of the
finite skeleton remains a possible rung, not started. Nothing here moves
bar-b, H59, W172, N-accounting, scorecard rows, or public posture; the
bit's VALUE remains externally posited (p2c-owned).
