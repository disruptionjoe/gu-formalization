# A Self-Referential Valuation No-Go and the Forced Symmetry-Breaking of the Residual

**Draft, 2026-07-11.** A short, self-contained structural theorem. It requires no physics and no
prior context: the reader needs only elementary category theory (finite products, the diagonal) and
elementary group theory (a group action and its fixed points). The paper separates six parts
explicitly -- (1) the setting, (2) the assumptions, (3) the theorem, (4) the proof, (5) examples and
counterexamples, (6) the limits of the result -- and adds a dedicated novelty map, which is where the
honest weight of the contribution is assessed. All uses of "--" stand for a dash; there are no
em-dashes.

---

## 0. Informal statement

A self-referential *observer* is modelled as a point of a structure that also carries a two-valued
*admissibility grading* on that same structure. The grading comes with an involution `alpha` that
exchanges the two grades ("admissible" and "inadmissible"). We assume this involution is
**fixpoint-free** (nothing is both admissible and inadmissible). Two elementary facts follow:

- **(I) No self-referential closure, and no symmetric total valuation.** There is no self-referential
  total representation of all admissibility valuations (a Cantor/Lawvere diagonal obstruction); and,
  separately, no total admissibility valuation is `alpha`-invariant. Hence any total valuation the
  observer actually commits to must *break* the grading symmetry.
- **(II) The residual is necessarily a "value," in a non-circular sense.** Define, purely
  group-theoretically, ARENA = a quantity invariant under the acting symmetry, VALUE = a quantity whose
  specification requires breaking that symmetry. This partition is decidable from the group action
  alone, with no reference to what is "forced" or "selected" by any process. Under this definition the
  residual forced by (I) is provably a VALUE.

The synthesis is the load-bearing sentence: *the selection an observer is forced to make is, provably
and non-circularly, a symmetry-breaking one.* We are careful below to state exactly which pieces are
classical and which is the new packaging.

---

## 1. The abstract setting (Part 1)

Work in a category `C` with finite products (the reader may take `C = Set`; nothing below uses more).
Write `1` for the terminal object and call a morphism `x : 1 -> X` a **point** of `X`. In `Set`, points
of `X` are its elements, and we use element notation freely.

**Objects.**

- `A` -- the **arena of observer-states**. Its points are the states the observer can occupy. The
  observer is self-referential in the sense made precise below: a state of `A` can serve both as a
  code (an admissibility rule) and as the argument that rule is applied to.
- `B` -- the **value object**, a two-element object `B = {0, 1}`. Read `0 =` admissible, `1 =`
  inadmissible. `B` is the object in which gradings and valuations take their values.

**The diagonal.** Finite products give the diagonal `Delta : A -> A x A`, `Delta(a) = (a, a)`. This is
the entire formal content of "self-reference": a state applied to itself.

**Valuations.** A **valuation** is a morphism `p : A -> B`; it grades each state as admissible or
inadmissible.

**The grading involution (the firewall).** A morphism `alpha : B -> B` with `alpha . alpha = id_B`.
The intended `alpha` is the **swap** `alpha(0) = 1`, `alpha(1) = 0` -- the map that exchanges
admissible and inadmissible. `alpha` acts on valuations by post-composition: `(alpha . p)(a) =
alpha(p(a))`.

**Self-referential closure.** A morphism `T : A x A -> B` is a candidate *closure*: its "rows"
`T(a0, -) : A -> B` are meant to enumerate valuations, with `a0` the code and the second argument the
input. `T` is **weakly point-surjective** if every valuation is some row: for each `p : A -> B` there
is a point `a0 : 1 -> A` such that `T(a0, x) = p(x)` for all points `x : 1 -> A`. A weakly
point-surjective `T` is exactly a self-referential structure that represents *all* of its own
valuations internally.

That is the whole setting: a self-referential arena `A`, a two-valued grading object `B` with an
involution `alpha`, and the notion of a total internal representation `T` of `A`'s valuations.

---

## 2. The assumptions (Part 2)

- **(A1) Finite products.** `C` has finite products (hence the diagonal `Delta` and the pairing used
  in the proof). Satisfied by any cartesian category, in particular `Set`.
- **(A2) Two-valued grading.** `B` has (at least) the two distinct points `0, 1` that `alpha`
  interchanges; the grading is genuinely two-valued, not collapsed to one point.
- **(A3) Fixpoint-freeness of the firewall.** `alpha` has **no fixed point**: there is no point
  `b : 1 -> B` with `alpha . b = b`. For the swap on `{0, 1}` this is immediate (`admissible !=
  inadmissible`); it is the single substantive hypothesis, and every conclusion is a strict consequence
  of it.
- **(A4) Nonempty arena** (used only for the invariant-valuation half): `A` has at least one point.

No other assumption is used. In particular no topology, measure, dynamics, order, or physical
structure enters.

---

## 3. The theorem (Part 3)

> **Theorem.** Let `C` be a category with finite products, `A` a nonempty object, `B` a two-valued
> object, and `alpha : B -> B` a fixpoint-free involution (A1-A4). Then:
>
> **(I-a) No closure.** No weakly point-surjective `T : A x A -> B` exists. Concretely, for every
> `T : A x A -> B` the *diagonal valuation* `d = alpha . T . Delta : A -> B` is not a row of `T`; it is
> a valuation that `A` cannot represent from inside.
>
> **(I-b) No invariant valuation.** No valuation `p : A -> B` is `alpha`-invariant: `alpha . p = p` is
> impossible for nonempty `A`. Equivalently, every total valuation the observer commits to satisfies
> `alpha . p != p` -- it breaks the grading symmetry.
>
> **(II) The residual is a value.** Let a group `G` act on `B`, and extend the action to valuations by
> post-composition. Call a valuation *arena-type* if it is `G`-invariant and *value-type* if it is not.
> This dichotomy is decided by the `G`-action alone. Taking `G = <alpha> ~ Z/2`, part (I-b) says every
> total valuation is value-type. Hence the selection an observer is forced into by (I) is necessarily a
> **value** (a symmetry-breaking selection), and this is a group-theoretic fact, not a definitional
> restatement of "forced."

Parts (I-a) and (I-b) are two distinct elementary consequences of A3 (they are not literally the same
statement: (I-a) is about no total *enumeration*, (I-b) about no single *invariant* valuation). Part
(II) supplies the non-circular reading under which the forced residual is a genuine value.

---

## 4. The proof (Part 4)

The proof is purely mathematical and uses no numerical input. (Finite instances have been
machine-checked as confirmation only; see the note at the end of this section. They are not part of
the proof.)

### 4.1 Lawvere's weak fixed-point lemma

**Lemma L (Lawvere 1969; weak form, Yanofsky 2003).** *If there is a weakly point-surjective
`T : A x A -> B`, then every endomorphism `alpha : B -> B` has a fixed point: a point `b : 1 -> B` with
`alpha . b = b`.*

*Proof.* Given `alpha`, form the valuation `f = alpha . T . Delta : A -> B`, i.e. `f(a) =
alpha(T(a, a))`. By weak point-surjectivity there is a point `a0` with `T(a0, x) = f(x)` for all points
`x`. Evaluate at `x = a0`:
```
    T(a0, a0) = f(a0) = alpha(T(a0, a0)).
```
So `b := T(a0, a0)` satisfies `alpha . b = b`. `QED`

**Proof of (I-a).** Contrapositive of Lemma L. By A3, `alpha` has no fixed point; therefore no weakly
point-surjective `T` exists. Moreover the specific valuation exhibited in the proof, `d = alpha . T .
Delta`, cannot be a row of `T`: if `d = T(a0, -)` for some code `a0`, then evaluating at `a0` gives
`T(a0, a0) = d(a0) = alpha(T(a0, a0))`, a fixed point of `alpha`, contradicting A3. So `d` is the
concrete unrepresented (residual) valuation. `QED`

### 4.2 The fixed-point-count corollary

**Lemma C (elementary fixed-point count).** *Let `alpha : B -> B` and `p : A -> B`. If `alpha . p = p`
then `p` factors through the fixed-point subobject `Fix(alpha) = {b : alpha(b) = b}` (the equalizer of
`alpha` and `id_B`). If `Fix(alpha)` is empty and `A` is nonempty, then `alpha . p = p` is impossible.*

*Proof.* `alpha . p = p` says every value `p(a)` satisfies `alpha(p(a)) = p(a)`, i.e. `p(a) in
Fix(alpha)`; so `p` factors through `Fix(alpha)`. If `Fix(alpha) = empty` and `A` has a point `a`,
then `p(a)` would be a point of the empty object, which is impossible. `QED`

**Proof of (I-b).** By A3, `Fix(alpha) = empty`; by A4, `A` is nonempty. Lemma C gives `alpha . p != p`
for every valuation `p`. `QED`

### 4.3 The non-circular partition and the identification (II)

Let a group `G` act on `B`; extend to valuations `p : A -> B` by `(g . p)(a) = g . (p(a))`. Define a
valuation to be **arena-type** if `g . p = p` for all `g in G` (invariant) and **value-type**
otherwise.

**Non-circularity.** Whether a given `p` is arena-type or value-type is determined entirely by the
`G`-action on `B` and the values of `p` -- a computation in group theory. It makes no reference to
any external notion of a quantity being "forced," "selected," "dynamically determined," or "chosen." In
particular the statement "the arena-type quantities are exactly the forced ones" is *synthetic*: it
relates two independently-defined predicates (invariance on one side, forcing on the other) and could a
priori be false. This is what saves the partition from the tautology "arena := the forced things,
value := the unforced things." (See Example 5.4 for the logical independence made concrete.)

**The identification.** Take `G = <alpha> ~ Z/2`, generated by the fixpoint-free involution. A
valuation is arena-type iff `alpha . p = p`. By (I-b) no total valuation is arena-type; every total
valuation is value-type. Therefore the residual valuation the observer is forced to commit to (its
existence and unrepresentability supplied by (I-a); its non-invariance by (I-b)) is a **value** in the
group-theoretic sense. `QED`

**Machine-checked confirmation (not the proof).** Finite instances of (I-a), the Cantor cross-check,
the fixpoint-free check, and the control cases have been verified exhaustively for `|A| in {1,2,3}` in
the repository tests `W70` and `W73`, and a further finite check accompanies this paper (`W99`). These
runs confirm the elementary lemmas above on small cases; they are evidence, not premises. The proof
stands on Lemmas L and C alone.

---

## 5. Examples and counterexamples (Part 5)

**5.1 The generating instance is Cantor.** Take `A` any set, `B = {0, 1}`, `alpha =` swap. A weakly
point-surjective `T : A x A -> B` is exactly an enumeration of `P(A)` by `A` (a valuation `A -> B` is
the indicator of a subset). (I-a) then reads: no such enumeration exists, and the unrepresented
`d = alpha . T . Delta` is the Cantor diagonal set `{a : a not in T(a)}`. So with two grades and the
swap, Part I *is* Cantor's theorem. This is stated up front because it fixes what is and is not new
(Section 6).

**5.2 Control: a firewall with a fixed point dissolves the theorem.** Drop A3: let `alpha = id_B` (or
any `alpha` with a fixed grade). Then Lemma L has a trivial fixed point, weakly point-surjective `T`
can exist, and constant valuations are `alpha`-invariant (arena-type). No selection is forced. This
shows the conclusion is contributed by fixpoint-freeness specifically, not by "a residual exists" in
general. The hypothesis A3 is load-bearing, not decorative.

**5.3 Counterexample: a genuine third grade breaks the argument.** Let `B = {below, boundary,
above}` and let `alpha` exchange `below` and `above` but fix `boundary`. Now `alpha` has a fixed point,
Lemma L applies with `b = boundary`, and an `alpha`-invariant valuation (constantly `boundary`) exists.
So a genuine neutral middle grade defeats both (I-a) and (I-b). The theorem needs the grading to be
*effectively two-valued with no fixed grade* (A2 + A3); any admissibility scheme with a stable "neutral"
verdict is outside its scope. This is the sharpest limit on the setting.

**5.4 The partition is substantive, not circular.** Consider `G = Z/2` acting on `B = {0, 1}` by swap.
The constant-pair feature "the unordered set `{0, 1}`" is `G`-invariant (arena-type); a specific choice
of element `0` or `1` is not `G`-invariant (value-type). Logical independence from "forcing" is
visible: one can specify an action under which a quantity is invariant while a *separate* dynamics fails
to determine it (an unforced invariant), or is non-invariant while a dynamics does determine it (a
forced value). Because both mismatches are describable, "invariant iff forced" is a claim with content
that could fail -- exactly the mark of a non-vacuous partition. (In the source research program this
was tested against a battery of concrete quantities; here we only need the logical point.)

**5.5 Positive existence when hypotheses are met.** For `A` nonempty and `alpha` the swap, (I-a)/(I-b)
both hold, and the concrete unrepresented residual `d = alpha . T . Delta` exists for every candidate
`T`. So the theorem is not vacuously true by absence of models: the setting is inhabited and the
residual is exhibited, not merely asserted.

---

## 6. Novelty map (dedicated assessment)

This section maps the result against the nearest prior art and grades its novelty honestly. The three
possible verdicts are: **(a) GENUINELY NOVEL** (a real synthesis with a new load-bearing statement);
**(b) NOVEL PACKAGING** (correct and clearly stated, but the pieces are known, the value being in the
framing); **(c) SUBSUMED** (already in the literature under another name).

**6.1 Lawvere's fixed-point theorem (Lawvere 1969); Yanofsky (2003).** Part (I-a) *is* Lawvere's weak
fixed-point theorem, in the elementary form popularized by Yanofsky, applied to a two-element `B` with a
fixpoint-free `alpha`. Yanofsky's "universal approach" already unifies Cantor, Russell, Godel, Tarski,
and the halting problem as instances of exactly this scheme. The fixed-point core is therefore **not
new**; with two grades and the swap it is literally Cantor. What is not in Lawvere/Yanofsky is the
*framing*: the two-element `B` read as an admissibility firewall carried by a self-referential observer,
and the identification (via Part II) of the forced residual as a symmetry-breaking selection. That
framing is additive, not a strengthening of the theorem.

**6.2 Kochen-Specker and contextuality (Kochen-Specker 1967; Bell 1966; Abramsky-Brandenburger 2011;
Conway-Kochen 2006).** Kochen-Specker is also a two-valued valuation no-go: for a Hilbert space of
dimension `>= 3` there is no global `{0, 1}`-valuation on the projection lattice compatible with the
functional (FUNC) constraints. Our result is *also* a two-valued valuation no-go with a forced residual,
so the genus is shared. But the *mechanism* differs and they are not the same theorem: Kochen-Specker's
obstruction is geometric/combinatorial (a Gleason-type coloring impossibility forced by the
orthogonality structure of quantum observables in dimension `>= 3`), and its "context" is a maximal
commuting set. Ours is a *self-referential diagonal* obstruction forced by fixpoint-freeness of a
grading involution, with self-application (the diagonal `Delta`) as the essential ingredient;
dimension, orthogonality, and measurement contexts play no role. Abramsky-Brandenburger recast
contextuality sheaf-theoretically (no global section of a presheaf of local valuations); that is closer
in spirit (a global-vs-local obstruction) but again the obstruction is measurement-context gluing, not
self-reference. Conway-Kochen (free will) and Bell add physical (locality/determinism) premises we do
not use. Verdict on this axis: **related but distinct**; ours is not Kochen-Specker in disguise, though
both belong to the family "no consistent global two-valuation."

**6.3 Curie's principle (Curie 1894; Earman 2004).** Part II ("value = requires symmetry-breaking to
specify") is essentially Curie's principle: symmetric causes have symmetric effects, so an asymmetry
requires a broken symmetry. Earman notes that precise formulations of Curie's principle tend toward the
*analytic*. Our contribution here is exactly to avoid that trap in a specific way: we tie the
symmetry-breaking characterization to a *valuation no-go* (Part I) so that the residual is not merely
*allowed* to be symmetry-breaking but is *forced* to be, and we give the arena/value partition a
non-circular group-theoretic definition (Section 4.3, Example 5.4). So the novelty relative to Curie is
the *forcing* of the residual plus the non-circular partition, not the "asymmetry needs broken symmetry"
slogan itself, which is old.

**6.4 The general Lawvere-paradox literature.** Yanofsky (2003) and the broader categorical-diagonal
tradition already subsume the fixed-point machinery and many of its instances. The present result is not
a new theorem *in that tradition*; it is an application of it to a graded/firewall setting joined to a
Curie-style partition.

**6.5 Honest verdict: (b) NOVEL PACKAGING.** The load-bearing mathematical facts (Lemmas L and C) are
classical; with two grades Part I is Cantor and in general it is Lawvere/Yanofsky, and Part II is a
sharpened Curie's principle. What is genuinely contributed, and is not simply any one of those pieces,
is the *synthesis*: (i) reading the two-element grading as an admissibility firewall on a
self-referential observer, so that the classical diagonal fires on "the observer's own admissibility
valuation"; (ii) proving the forced residual is not merely unforced but *symmetry-breaking*, via the
fixpoint-count corollary; and (iii) supplying a non-circular, group-theoretic arena/value partition that
makes "the residual is a value" a substantive rather than definitional claim, and that ties Curie's
principle to a valuation no-go. This is a correct, clearly-stated, well-mapped synthesis whose parts are
known -- the respectable and common (b) outcome. The closest single prior result is **Yanofsky (2003)**
for Part I and **Earman's analysis of Curie's principle (2004)** for Part II. We do *not* claim (a): no
individual step is a new theorem, and inflating the synthesis to "genuinely novel" would not survive a
specialist who recognizes the Cantor/Lawvere core. We also do not accept (c): no prior source states the
combined "forced residual is provably a symmetry-breaking value, under a non-circular partition" as a
single result, so it is not strictly subsumed.

---

## 7. What the theorem does NOT establish (Part 6)

- **No physical or operator-algebra realization.** The theorem is purely structural. A separate attempt
  to realize `A` as the observable algebra of a spacetime region and `alpha` as a grading of a modular
  conjugation -- so that the abstract firewall would become a physical one -- **did not go through**: in
  the interacting continuum the required per-region construction fails to exist and to cohere across
  overlaps (recorded in the repository as the `W98` break). Nothing in this paper depends on that
  realization, and none of it is claimed here. The abstract theorem stands; the physical instantiation
  does not.
- **No dependence on, or support for, any physical theory.** The setting uses no physics. The theorem
  neither assumes nor provides evidence for any specific unified theory, field content, or model. Any
  physical theory can at most be *one instance* of the abstract setting, and being an instance confers
  no confirmation on the theory.
- **No specific value, constant, or count.** The theorem says the forced residual *is a
  symmetry-breaking selection*; it does not compute which selection, nor any number, ratio, dimension,
  or count. It is an existence-and-character result, not a quantitative one.
- **Not a physical prediction.** It is a logical/structural theorem about self-referential valuations.
  It makes no empirically testable claim on its own.
- **Genericity, not uniqueness.** Because Part II is a form of Curie's principle, the arena/value
  partition it uses is *generic* to symmetry-based structures, not a signature of any particular system.
  Genericity is not vacuity (the partition is still non-circular and falsifiable), but it means the
  theorem cannot be used to argue that any specific framework is distinguished.
- **Novelty caveats (from Section 6).** Part I is classical (Cantor / Lawvere / Yanofsky) and Part II
  sharpens a classical principle (Curie). The honest novelty grade is (b) novel packaging; the value is
  in correctness, self-containment, and the mapped synthesis, not in a new fixed-point core.
- **Scope of the grading.** The theorem requires an effectively two-valued grading with a fixpoint-free
  involution (A2, A3). It says nothing about admissibility schemes with a stable neutral verdict; a
  genuine third fixed grade dissolves it (Example 5.3).

---

## References (for the novelty map)

- F. W. Lawvere, *Diagonal arguments and cartesian closed categories* (1969).
- N. S. Yanofsky, *A universal approach to self-referential paradoxes, incompleteness and fixed
  points*, Bull. Symbolic Logic 9(3):362-386 (2003).
- S. Kochen and E. P. Specker, *The problem of hidden variables in quantum mechanics*, J. Math. Mech.
  17:59-87 (1967); J. S. Bell, *On the problem of hidden variables in quantum mechanics*, Rev. Mod.
  Phys. 38:447 (1966).
- S. Abramsky and A. Brandenburger, *The sheaf-theoretic structure of non-locality and contextuality*,
  New J. Phys. 13:113036 (2011); J. Conway and S. Kochen, *The free will theorem*, Found. Phys. 36:1441
  (2006).
- P. Curie (1894); J. Earman, *Curie's principle and spontaneous symmetry breaking*, Int. Stud. Phil.
  Sci. 18:173-198 (2004).

*Repository confirmation (not part of the proof): tests `W70`, `W73`, and `W99` verify finite instances
of the lemmas exhaustively for small arenas. External publication is gated pending review.*
