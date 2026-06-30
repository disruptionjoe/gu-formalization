---
title: "C_MPR / 9-tuple / BvN wall: category object, morphism, and proof obligations before theorem status"
date: 2026-06-23
problem_label: "c-mpr-9tuple-object-morphism"
status: exploration
verdict: CONDITIONALLY_RESOLVED
---

# C_MPR / 9-tuple / BvN wall: object, morphism, and proof obligations

## 1. Problem statement

The C_MPR lane (RESEARCH-STATUS row "C_MPR / 9-tuple / BvN wall", publish potential 3) is
flagged with the standing instruction: *state the object, morphism, and proof obligations
before claiming theorem status.* The lane carries three named artifacts asserted by a
"5-way convergence" of agent workers (WRK-388/389/390 v3 + WRK-382/384 v2):

1. **C_MPR** — "the monotone-provenance + readout factorization category", objects
   `M = (E, ≤_E, Cert, G, ≤_G, r, P_O)`.
2. **The Classical-Value-Lattice Wall** — a claimed Birkhoff-von Neumann-1936 generalization
   denying a 1-categorical adjunction `L : C_ClassicalDistribLR ⇄ C_GW : R`.
3. **The 9-tuple** `M_v3 = (T_X, C_X, U, ρ, C_U, ft, ex, rr, arch)` meta-template.

The failure condition for this computation is explicit: **if no well-defined object/morphism
can be written, the lane is a naming exercise, not a theorem — say so explicitly.**

The task is NOT to prove the wall. It is to discharge the prerequisite: write down the category
object, write down the morphism, and check the category axioms (identity, composition,
associativity). Only an object-and-morphism that survives the axiom check earns the word
"category"; only a morphism with a defined domain and codomain earns the word "theorem".

## 2. Established context

- **Signed-readout boundary theorem** (`explorations/signed-calm-jordan/signed-readout-theorem-statement-2026-06-23.md`,
  CONDITIONALLY_RESOLVED, promoted to `lab/active-research/signed-readout/theorem-statement-v1`).
  This supplies the only rigorously-defined pieces of the C_MPR tuple: the evidence monoid
  `E = N_0^{(X)}`, the information order `≤_E` (divisibility), the lattice-ordered codomain
  `(G, ≤_G)`, the weight `w : X → G`, the signed readout `R_w : E → G`, and the PN/Jordan
  provenance split. These are concrete and axiom-checked.
- **Rigor redirect** (`explorations/c-mpr/rigor-redirect-c-mpr-branch.md`, 2026-05-31). Layer 4
  of that document already states the exact category obligations that have NEVER been discharged:
  "Objects: define the tuple fields and their laws. Morphisms: define what structure must be
  preserved. Identities: prove the identity morphism satisfies the laws. Composition: prove
  composed morphisms preserve accumulator, readout, certificate, and approximation/error
  semantics." This file discharges them.
- **Convergence synthesis** (`explorations/c-mpr/historical-c-mpr-convergence-synthesis-2026-05-31.md`).
  Every load-bearing claim in that file carries an explicit `[speculation, candidate canonical
  statement]` tag (§1.1, §2.1, §3). The synthesis itself never proves the category axioms and
  never gives `C_GW` an object-level definition.
- **Standing repo rule** (NEXT-STEPS.md §"What To Avoid"): "Do not treat C_MPR, the 9-tuple,
  PCP-blindness, or the BvN-style wall as settled."

## 3. Computation

### 3.1 The object — what is well-defined and what is decorative

The synthesis tuple is `M = (E, ≤_E, Cert, G, ≤_G, r, P_O)`. Audit each field for whether it
carries a definition with laws (the bar set by the rigor redirect):

| field | definition present? | laws stated? | source |
|---|---|---|---|
| `E` (evidence monoid) | YES — `N_0^{(X)}` free commutative monoid | YES (commutative monoid axioms) | signed-readout §3.1 |
| `≤_E` (info order) | YES — componentwise divisibility | YES (directed poset, well-founded, cancellative) | signed-readout §3.1 |
| `G` (codomain) | YES — lattice-ordered abelian group | YES (l-group axioms) | signed-readout §3.2 |
| `≤_G` (semantic order) | YES — l-group order with cone `G_+` | YES (translation-invariant) | signed-readout §3.2 |
| `r` (readout) | YES — unique monoid hom `R_w` extending `w` | YES (additivity) | signed-readout §3.3 |
| `Cert` | NO — "optional proof-carrying provenance layer" | NO laws stated anywhere | synthesis §1.1 only |
| `P_O` | NO — "observer protocol (observation, propagation, merge, ...)" | NO laws; a prose list, not a structure | synthesis §1.1 only |

**Finding (object).** Five of the seven fields ARE well-defined with laws — and they are
exactly the five that the signed-readout theorem independently formalized. Two fields, `Cert`
and `P_O`, are prose placeholders with no algebraic definition and no laws. Crucially, the
five well-defined fields **do not depend on the two decorative ones**: an object of the form
`(E, ≤_E, G, ≤_G, r)` is fully specified without `Cert` or `P_O`.

**Therefore the well-defined object is a 5-tuple, not the advertised 7-tuple.** Define:

> **C_SR (signed-readout category) — objects.** An object is a tuple
> `M = (X, G, w)` where `X` is a set (contribution event types), `G` is a lattice-ordered
> abelian group, and `w : X → G` is a weight function. The derived data `E = N_0^{(X)}`,
> `≤_E`, `R_w : E → G`, and the PN/Jordan split `(w_+, w_-)` are determined by `(X, G, w)`.

This is the honest object. It is a strict reduct of the synthesis 7-tuple. `Cert`/`P_O` can be
re-attached later as extra structure (a comma/slice construction over C_SR), but they are not
needed to have a category and currently carry no laws.

### 3.2 The morphism — written down and axiom-checked

The synthesis (§1.1) proposes: a morphism `f : M → M'` is a monotone provenance map
`f_E : E → E'` plus a readout-compatibility map `f_G : G → G'` with `f_G ∘ r = r' ∘ f_E`.
Make this precise on C_SR objects and check the axioms.

> **C_SR — morphisms.** A morphism `f : (X, G, w) → (X', G', w')` is a pair `f = (φ, ψ)` where:
> - `φ : X → X'` is a function on event types (it induces `φ_* : E → E'`, the unique monoid
>   homomorphism with `φ_*([x]) = [φ(x)]`; `φ_*` is automatically `≤_E`-monotone because
>   `φ_*` preserves `N_0`-sums and `e ≤_E e' ⇒ e' = e + d ⇒ φ_*(e') = φ_*(e) + φ_*(d)`);
> - `ψ : G → G'` is a homomorphism of lattice-ordered abelian groups (preserves `+`, `∨`, `∧`,
>   hence sends `G_+` into `G'_+`, hence is `≤_G`-monotone);
> - **readout-compatibility (the one nontrivial law):** `ψ ∘ w = w' ∘ φ` on `X`.

**Lemma (compatibility lifts from generators to all of E).** If `ψ ∘ w = w' ∘ φ` on `X`, then
`ψ ∘ R_w = R_{w'} ∘ φ_*` on all of `E`. *Proof.* Both sides are monoid homomorphisms `E → G'`
(composites of homomorphisms). They agree on the generators `[x]`:
`ψ(R_w([x])) = ψ(w(x)) = w'(φ(x)) = R_{w'}([φ(x)]) = R_{w'}(φ_*([x]))`. By freeness of `E`
(universal property), two homomorphisms agreeing on generators are equal. ∎

So the generator-level compatibility law `ψ ∘ w = w' ∘ φ` is equivalent to the full square
`ψ ∘ R_w = R_{w'} ∘ φ_*` commuting. This is what makes morphisms checkable on finite data
(`X`) rather than on all of `E`.

**Axiom 1 — identity.** `id_M = (id_X, id_G)`. Then `φ_* = id_E`, `ψ = id_G`, and the
compatibility law `id_G ∘ w = w ∘ id_X` holds trivially. The induced readout square is the
identity square. ✓

**Axiom 2 — composition is well-defined.** Given `f = (φ, ψ) : M → M'` and
`g = (φ', ψ') : M' → M''`, set `g ∘ f = (φ' ∘ φ, ψ' ∘ ψ)`. Then `φ' ∘ φ : X → X''` is a
function and `ψ' ∘ ψ : G → G''` is an l-group homomorphism (composite of l-group homs).
Compatibility of the composite:
`(ψ' ∘ ψ) ∘ w = ψ' ∘ (ψ ∘ w) = ψ' ∘ (w' ∘ φ) = (ψ' ∘ w') ∘ φ = (w'' ∘ φ') ∘ φ
= w'' ∘ (φ' ∘ φ)`,
using `f`-compatibility at the second equality and `g`-compatibility at the fourth. So
`g ∘ f` is a morphism. ✓

**Axiom 3 — associativity and unit laws.** Both components compose as ordinary functions
(`φ`) and ordinary group homomorphisms (`ψ`). Function composition and homomorphism
composition are associative and unital, and the pairing is componentwise, so associativity
`(h ∘ g) ∘ f = h ∘ (g ∘ f)` and the unit laws `id ∘ f = f = f ∘ id` follow componentwise. ✓

**Finding (morphism).** A morphism exists, has a defined domain and codomain, satisfies one
nontrivial preservation law (readout compatibility), and the identity/composition/associativity
axioms ALL check. **C_SR is a genuine category.** The five Layer-4 obligations from the rigor
redirect (objects-with-laws, morphisms-with-preservation, identity, composition, associativity)
are discharged for the reduct object. This is the first time in the corpus the axioms are
actually verified rather than asserted.

### 3.3 CALM as a subcategory — checkable now

The synthesis claims `C_CALM ⊂ C_MPR` is the monotone-readout subcategory. On C_SR this is
now a precise, checkable statement:

> **C_CALM := full subcategory of C_SR on objects `(X, G, w)` with `w(x) ∈ G_+` for all `x`.**

By Part (M) of the signed-readout theorem, these are exactly the objects whose readout `R_w`
is `≤_E`→`≤_G` monotone. It is a **full** subcategory: any C_SR morphism between two monotone
objects is admitted (no extra condition), because the morphism law `ψ ∘ w = w' ∘ φ` plus
`ψ(G_+) ⊆ G'_+` is automatically consistent with monotone weights. Inclusion is a faithful
functor. This discharges the "CALM is a subcategory" claim — but **only as a full subcategory**,
NOT as the stronger "reflective subcategory / fibration" claims, which remain OPEN (§5).

### 3.4 The BvN wall morphism — this is where the lane is a naming exercise

The wall (synthesis §2.1) is a statement about a morphism: it denies the existence of an
adjunction
```
L : C_ClassicalDistribLR  ⇄  C_GW  : R.
```
An adjunction is a pair of functors plus a natural iso of hom-sets. To even state the theorem,
both categories and the functors must be defined at object level. Audit:

| ingredient | object-level definition in corpus? |
|---|---|
| `C_ClassicalDistribLR` (LHS) | PARTIAL. The signed-readout objects are concrete; "any category of classical local-rule systems with distributive value lattice" is a description of a class, not a category with specified objects and morphisms. No morphism class is given. |
| `C_GW` (RHS) | **ABSENT.** "the category of Ginsparg-Wilson-modified spectral triples with anomaly-free morphisms" — neither the objects (which spectral triples? what data?) nor "anomaly-free morphisms" are defined anywhere in the corpus. |
| `L`, `R` (the functors) | ABSENT. No object map, no morphism map, no functoriality check. |
| the natural iso `Hom(L–,–) ≅ Hom(–,R–)` | ABSENT. |

**Finding (wall).** The wall denies an adjunction between a category that is only sketched
(`C_ClassicalDistribLR`) and a category that is never defined (`C_GW`), via functors that are
never written. You cannot prove the non-existence of a morphism (here: an adjunction) whose
**codomain category does not have a definition.** A non-existence claim about an undefined
object is not false — it is **not yet a proposition**.

The underlying *mathematical fact* the wall gestures at is real and classical: Birkhoff-von
Neumann 1936 says the projection lattice of a noncommutative von Neumann algebra is
orthomodular but not distributive, so `Proj : C*-alg → OrthomodLat` restricts to distributive
lattices only on the commutative subcategory. That is a true theorem about lattices. But the
**leap** from "distributive ≠ orthomodular at the lattice level" to "no adjunction
`C_ClassicalDistribLR ⇄ C_GW` preserving Dirac content" requires the two categories and the
preservation functor to be defined — and they are not. The leap is precisely the "smuggling
the conclusion through object definitions" failure that the rigor redirect (Layer 5) warned
against.

**Status of the wall: NAMING EXERCISE at the categorical level.** Not because the intuition is
wrong, but because the morphism it is "about" has no defined codomain. It is a theorem-shaped
sentence with an undefined noun.

### 3.5 The 9-tuple — frame, not theorem

`M_v3 = (T_X, C_X, U, ρ, C_U, ft, ex, rr, arch)`. This is a **classification record schema**:
a list of slots an analyst fills when classifying a no-go evasion attempt. Audit against
"is it a theorem / mathematical object":

- It is not an object of a category (no morphisms between 9-tuples are defined).
- It is not a theorem (no proposition is asserted by the tuple itself).
- Its own authors graded it: **"META-FRAME HOLDS — META-THEOREM PARTIAL"** (synthesis §3.4),
  with the universal-completeness conjecture OPEN.
- The `arch = (P_O, E, r)` slot points back at the C_SR data; only `E` and `r` are defined,
  `P_O` is the same undefined prose layer as in §3.1.

**Finding (9-tuple).** It is an internal checklist / record schema. It is correctly NOT
claimed as a theorem by its authors. It earns its keep as documentation, not as mathematics.
No change to its status: it is a frame, and was already honestly labeled as such.

## 4. Result

**Verdict: CONDITIONALLY_RESOLVED.**

The prerequisite the lane demanded — write the object, write the morphism, check the axioms —
is discharged with a split outcome:

1. **C_MPR object: writable, but as a 5-tuple reduct C_SR, not the advertised 7-tuple.** The
   fields `(E, ≤_E, G, ≤_G, r)` are well-defined with laws (inherited from the signed-readout
   theorem). `Cert` and `P_O` are prose placeholders with no laws and are not needed for the
   category.

2. **C_SR morphism: written and axiom-checked. C_SR IS a genuine category.** Identity,
   composition, and associativity all verify; the one nontrivial law (readout compatibility
   `ψ ∘ w = w' ∘ φ`) lifts from generators to all of `E` by freeness. `C_CALM` is a *full*
   subcategory. This is the first axiom-verified (not merely asserted) statement in the lane.

3. **BvN wall: a naming exercise at the categorical level, NOT a theorem.** It denies an
   adjunction whose codomain category `C_GW` is never given an object-level definition and
   whose functors `L, R` are never written. A non-existence claim about an undefined object is
   not a proposition. The classical BvN lattice fact it rests on is true, but the categorical
   wall is not derived from it.

4. **9-tuple: a record schema / frame, correctly not claimed as a theorem by its authors.**

So the lane is **part theorem-bearing (the C_SR category), part naming exercise (the wall)**.
The honest status replacing "5-way convergence on a canonical category and wall" is: there is
ONE rigorous category (C_SR, = the signed-readout objects organized categorically) and ONE
suggestive-but-undefined wall.

### Explicit failure conditions

A failure condition here = a specific mathematical statement that would falsify a claim made
in §4. At least three:

- **FC1 (object not a category).** If a C_SR morphism `(φ, ψ)` could satisfy the
  generator-level law `ψ ∘ w = w' ∘ φ` yet FAIL the full square `ψ ∘ R_w = R_{w'} ∘ φ_*`, then
  composition would not be well-defined and C_SR would not be a category. This is falsified
  only if `E` is not free on `X` (a relation among generators) — exactly failure mode F1 of
  the signed-readout theorem. Under H1 (free `E`), the §3.2 Lemma forecloses it.
- **FC2 (CALM not full).** If there existed monotone objects `M, M'` (all weights in `G_+`)
  and a structure-preserving map between their readouts that is NOT of the form `(φ, ψ)` with
  `ψ` an l-group homomorphism, then `C_CALM` would be a non-full subcategory and the §3.3
  claim fails. This fires if "monotone-readout morphism" is defined more liberally than l-group
  homomorphism (e.g. allowing monotone-but-nonadditive readout maps).
- **FC3 (wall is actually a theorem).** If someone supplies an object-level definition of
  `C_GW` (objects = specified spectral-triple data; morphisms = specified anomaly-free maps)
  AND functors `L, R` with a functoriality proof, then the wall ceases to be a naming exercise
  and §3.4's verdict is overturned. The §3.4 finding is conditional on `C_GW` remaining
  undefined; it is falsified the moment a definition is written.
- **FC4 (Cert/P_O carry hidden laws).** If `Cert` or `P_O` were given algebraic definitions
  with laws that the 5-tuple reduct violates, then C_SR would be the wrong reduct and the
  honest object would be larger than claimed in §3.1. Currently no such laws exist in the
  corpus, but their later supply would revise the object.

## 5. Open questions

- **Reflectivity / fibration (OPEN, unchanged).** Is `C_CALM` *reflective* in `C_SR` (left
  adjoint to inclusion)? Is `C_SR` a fibration over the category of evidence monoids with
  readout fibers? These are the synthesis §1.3 OPEN items; this file proves the full-subcategory
  claim but leaves reflectivity/fibration untouched. They are now well-posed because C_SR is a
  defined category.
- **Defining `C_GW` (the real blocker for the wall).** To upgrade the wall from naming exercise
  to theorem requires: (a) objects of `C_GW` = a specified tuple of spectral-triple data
  (algebra, Hilbert space, Dirac, real structure, GW relation); (b) morphisms = "anomaly-free
  maps" given an actual definition; (c) the functors `L, R`; (d) the preservation requirement
  ("non-trivial Dirac content") stated as a functor property. Only then can non-existence of
  the adjunction be a proposition. This is the single highest-leverage missing piece in the
  entire lane.
- **Re-attaching Cert/P_O.** If `P_O` (observer protocol) is to be real structure rather than
  prose, the natural home is a comma category or a Grothendieck construction over C_SR indexed
  by record-graphs `G_R` (the record-graph formalization in
  `explorations/signed-calm-jordan/signed-readout-oq1-record-graph-2026-06-23.md` is the candidate index data).
  Whether that yields laws compatible with the C_SR morphisms is open.
- **Does the wall's classical BvN core have ANY categorical bite without `C_GW`?** Possibly the
  honest residue is a much smaller true statement: "the functor `Proj : C*-alg → OrthomodLat`
  does not factor through `DistribLat ↪ OrthomodLat` off the commutative subcategory." That IS
  a theorem (it is essentially BvN 1936). It says nothing about adjunctions to a GW category.
  Whether the lane should retreat to exactly this defensible statement is a Joe-decision.
