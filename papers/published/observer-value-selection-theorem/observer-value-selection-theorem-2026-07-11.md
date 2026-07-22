# A Diagonal No-Go for Self-Valuations and an Invariance Classification

**Joe Hernandez -- Independent Researcher -- July 2026**
Email: joe@disruptionjoe.com

## Abstract

Let `A` and `B` be sets. A valuation is a function `p : A -> B`, and a candidate
self-enumeration is a function `T : A x A -> B` whose rows are intended to exhaust all
valuations. Given a fixed-point-free map `alpha : B -> B`, we prove two elementary facts.
First, no such `T` is weakly point-surjective, and for every `T` the diagonal valuation
`d_T(a) = alpha(T(a,a))` is absent from its rows. Second, if `A` is nonempty, no valuation
is `alpha`-invariant. For `B = {0,1}` and `alpha` the swap, the first fact is the
Cantor-Lawvere diagonal argument and the second is a pointwise fixed-point observation. A
group action on `B` also induces the standard classification of valuations as invariant or
non-invariant; under the swap, every valuation lies in the latter class. This classification
adds no selection theorem. Observer, admissibility, and symmetry-breaking language is offered
only as interpretation. The contribution is a specific synthesis of known pieces, not a new
fixed-point or symmetry theorem. The function-level core and its Boolean corollaries are
machine-checked in Lean 4; the interpretive classification is not formalized.

**MSC 2020:** 03E20 (primary); 18A15, 03A05 (secondary).
**Keywords:** diagonal argument; weak point-surjectivity; valuation no-go; invariance;
self-reference; Lawvere fixed-point theorem.

## 1. Set-level setting

The theorem is stated in `Set`. This choice is deliberate: equality of functions, equality of
rows, and elementwise representation then have their ordinary extensional meanings. No
morphism-level conclusion in an arbitrary category is claimed.

Let `A` be a set of codes or states and let `B` be a set of values. A **valuation** is a
function `p : A -> B`. A function `T : A x A -> B` supplies, for each `a0 in A`, a row

```text
T_a0 : A -> B,    T_a0(x) = T(a0,x).
```

We call `T` **weakly point-surjective** if every valuation is a row:

```text
for every p : A -> B, there is a0 in A such that
T(a0,x) = p(x) for every x in A.
```

This is the uncurried Set-level form of Lawvere's weak point-surjectivity: `T` plays the role
of the transpose of a map `A -> B^A` (Lawvere 1969; Yanofsky 2003).

Let `alpha : B -> B` be a map. It is **fixed-point-free** when

```text
alpha(b) != b for every b in B.
```

The intended two-valued instance is `B = {0,1}` with `alpha(0)=1` and `alpha(1)=0`. The
proofs do not require `B` to have exactly two elements, and the diagonal result does not
require `alpha` to be an involution. Involutivity is used only when `alpha` is read as the
nontrivial element of a `Z/2` action.

## 2. The no-go theorem

> **Theorem (diagonal and invariant-valuation no-go).** Let `A` and `B` be sets and let
> `alpha : B -> B` be fixed-point-free.
>
> 1. For every `T : A x A -> B`, the diagonal valuation
>    `d_T(a) = alpha(T(a,a))` is not a row of `T`. Consequently no weakly
>    point-surjective `T : A x A -> B` exists.
> 2. If `A` is nonempty, then no valuation `p : A -> B` is `alpha`-invariant;
>    equivalently, there is no `p` satisfying `alpha(p(a)) = p(a)` for every `a in A`.

The two conclusions are separate. The first concerns enumeration of all functions `A -> B`;
the second concerns invariance of a single function and uses nonemptiness of `A`.

## 3. Proof

**Lemma (weak Lawvere fixed-point lemma).** If `T : A x A -> B` is weakly
point-surjective, then every map `alpha : B -> B` has a fixed point.

*Proof.* Define `f : A -> B` by `f(a) = alpha(T(a,a))`. Weak point-surjectivity supplies
`a0 in A` such that `T(a0,x) = f(x)` for every `x in A`. Evaluating at `a0` gives

```text
T(a0,a0) = f(a0) = alpha(T(a0,a0)),
```

so `T(a0,a0)` is a fixed point of `alpha`. QED

**Proof of Theorem 2(1).** Fix `T` and a candidate row `a0 in A`. At the row's own index,

```text
d_T(a0) = alpha(T(a0,a0)) != T(a0,a0),
```

because `alpha` is fixed-point-free. Thus `d_T != T_a0`. Since this holds for every `a0`,
`d_T` is not a row. A weakly point-surjective `T` would have to contain `d_T` as a row, so
none exists. This is also the contrapositive engine of the weak Lawvere lemma. QED

**Lemma (pointwise fixed-point observation).** Let `p : A -> B`. If
`alpha(p(a)) = p(a)` for every `a in A`, then every value in the image of `p` is a fixed
point of `alpha`.

*Proof.* For each `a in A`, the displayed equality is exactly the statement that `p(a)` is
fixed by `alpha`. QED

**Proof of Theorem 2(2).** Choose `a in A`. If `p` were `alpha`-invariant, the pointwise
lemma would make `p(a)` a fixed point of `alpha`, contradicting fixed-point-freeness. QED

## 4. Invariance classification

Let a group `G` act on `B`. It acts on valuations by post-composition:

```text
(g . p)(a) = g . p(a).
```

A valuation is **G-invariant** if `g . p = p` for every `g in G`, and **non-invariant**
otherwise. This is a group-action-theoretic criterion depending on the action and on `p`. No
general algorithmic decidability claim is intended.

> **Corollary.** Suppose `A` is nonempty and `alpha : B -> B` is a fixed-point-free
> involution. Under the `Z/2` action generated by `alpha`, every valuation `p : A -> B` is
> non-invariant.

*Proof.* Invariance under the generated action implies `alpha(p(a)) = p(a)` for every `a`.
Theorem 2(2) rules this out. QED

For later interpretation one may label invariant valuations **arena-type** and non-invariant
valuations **value-type**. Those are paper-specific labels for the standard
invariant/non-invariant distinction. The corollary then says that every valuation in the
fixed-point-free two-valued instance is value-type. This sentence is only a classification
consequence. It proves no forcing, choice, commitment, dynamics, canonical residual, or
physical selection mechanism. Because every valuation is already non-invariant, applying the
label to the particular diagonal `d_T` adds no information beyond Theorem 2(2).

## 5. Examples and controls

### 5.1 Cantor's diagonal

Take `B = {0,1}` and let `alpha` swap the two values. A valuation is the characteristic
function of a subset of `A`. If the row `T_a` represents the subset `S_a`, then `d_T` is the
characteristic function of

```text
D = {a in A : a not in S_a}.
```

Theorem 2(1) is Cantor's diagonal theorem in this instance.

### 5.2 A map with fixed points

Let `alpha = id_B`. The fixed-point argument no longer shows that a diagonal is absent: for
example, when `A` is nonempty, a constant `T` represents its own unflipped diagonal as every
row. Invariant valuations also exist, so Theorem 2(2) fails without fixed-point-freeness. This
does **not** make a weakly point-surjective `T` possible when `|B| >= 2`; Cantor's argument
still forbids one in `Set`. If `|B| = 1` and `A` is nonempty, the unique `T` is weakly
point-surjective. Thus the honest control is: this particular fixed-point argument no longer
rules out a row representation, while existence of a complete enumeration depends on `B`.

### 5.3 A third fixed grade

Let

```text
B = {below, boundary, above}
```

and let `alpha` exchange below and above while fixing boundary. The constant-boundary
valuation is `alpha`-invariant, so the invariant-valuation conclusion fails. The same `alpha`
also cannot drive the diagonal contradiction because it has a fixed point. Nevertheless a
weakly point-surjective `T` is still impossible: a three-cycle on `B` is fixed-point-free, so
the weak Lawvere lemma rules out `T`. A neutral fixed grade therefore defeats the
invariant-valuation result and the proof based on this grading involution; it does not defeat
Cantor-Lawvere non-enumerability in `Set`.

### 5.4 Both sides of the classification

Let `A` be nonempty, let `B = {0,1,2}`, and let `Z/2` act on `B` by exchanging `0` and `1`
while fixing `2`. The constant valuation `p_2(a)=2` is invariant. The constant valuations
`p_0(a)=0` and `p_1(a)=1` are exchanged and hence are non-invariant. These are actual
functions `A -> B`, so the example instantiates the definition in Section 4. It also shows
that the classification is specified without any selection or forcing predicate.

### 5.5 Exact machine-checking scope

The file `Lean/GUFormalization/ResidualSelection.lean` formalizes the function-level
statements over Lean types: the weak Lawvere lemma, diagonal escape, the shared no-closure
theorem, and the pointwise no-invariant-valuation theorem. It also proves their
`B = Bool` corollaries for Boolean negation. These are the Set-level statements used in this
paper. Lean does not formalize Section 4, the interpretive labels, the literature map, or any
physical reading. The separate Python script `tests/W99_theorem_finite_instances.py`
exhaustively checks small finite instances; it is executable confirmation, not proof. Exact
commands and theorem names appear in `submission/reproduction.md`. The repository hosts a
broader research program; only the files named there are relied on here.

## 6. Interpretation and prior-art map

### 6.1 What the formal theorem says

The mathematical theorem says only that a fixed-point-free map prevents a complete
row-enumeration and, on a nonempty domain, prevents invariant valuations. An observer reading
is possible: `A` may be described as an arena of states that can encode and evaluate
valuations, the diagonal as self-application, `B = {0,1}` as an admissibility grading, and
`alpha` as the grade swap. Under that reading, the result says that complete internal
enumeration fails and every total valuation is non-invariant. The words "observer,"
"admissibility," "arena," "value," and "symmetry-breaking" belong to this interpretation.
The words "forced," "commit," and "selection" are not formal predicates and are not
conclusions of the theorem.

### 6.2 Lawvere, Yanofsky, and Cantor

Theorem 2(1) is classical. It is the weak Lawvere/Yanofsky diagonal scheme; for the Boolean
swap it is Cantor's theorem. No fixed-point theorem is claimed as new.

### 6.3 Valuation no-gos and contextuality

Kochen-Specker gives a finite noncolorability construction for quantum observables constrained
by orthogonality; Bell's 1966 hidden-variable analysis gives a related Gleason-based route and
emphasizes the role of contextuality assumptions. Abramsky and Brandenburger express
contextuality as an obstruction to global sections over measurement contexts, while
Conway-Kochen adds quantum and relativistic assumptions absent here. These works share the
broad genre of valuation impossibility, but their engines are quantum-observable constraints
or contextual gluing, not the self-diagonal `a |-> T(a,a)` used here.

### 6.4 Observer and interactive self-reference

Observer/self-reference motivation is also not new. Breuer studies limits on accurate
self-measurement; Szangolies applies Lawvere's theorem to epistemic horizons in quantum
foundations; Abramsky and Zvesper reduce an interactive epistemic paradox to a relational
Lawvere argument. Frauchiger-Renner and Brukner provide distinct observer no-go results in
quantum foundations. A recent preprint by Lawrence uses Lawvere-style diagonalization in a
selection-motivated information-theoretic setting. None of these comparisons makes the
present theorem physically instantiated, and no novelty is claimed for observer language by
itself.

### 6.5 Invariance and Curie's principle

The invariant/non-invariant partition in Section 4 is standard symmetry language, not new
mathematics and not Curie's causal principle. Curie's historical principle concerns symmetries
of causes and effects. Earman analyzes a precise formulation and its near-vacuity in quantum
field theory while emphasizing spontaneous symmetry breaking; Norton treats the principle as
a truism whose application depends on how causal terms are mapped into a science. The present
paper uses neither causal principle. It uses only the elementary group action on functions.

### 6.6 Novelty grade

The defensible grade is **novel packaging**. The diagonal theorem is classical; the
invariant/non-invariant distinction is standard; and the observer/self-reference motivation
has close precedents. The contribution is the explicit, self-contained packaging of a
two-valued admissibility reading, the diagonal no-go, the separate invariant-valuation
observation, the classification caveat, and a reproducible Lean anchor. We do not claim that
this packaging is a new fixed-point theorem, symmetry theorem, physical theory, or forcing
principle. Nor do we claim that a literature search proves uniqueness of the packaging.

## 7. What the theorem does not establish

- **No arbitrary-category result.** The theorem is stated and proved in `Set`. It makes no
  morphism-level claim in an arbitrary category with finite products.
- **No physical or operator-algebra realization.** No physical system, observable algebra, or
  operator-algebra construction is shown to instantiate the hypotheses.
- **No physical selection mechanism.** The theorem supplies no dynamics, probability law,
  forcing modality, choice rule, or mechanism by which an observer selects a valuation.
- **No canonical residual.** The diagonal `d_T` depends on the chosen candidate `T`. The
  theorem does not choose a distinguished `T` or a distinguished valuation.
- **No physical prediction or support for a physical theory.** The result has no empirical
  content by itself and provides no confirmation of Geometric Unity or any other theory.
- **No particular value, constant, or count.** It computes no number and does not derive three
  generations or any generation count.
- **No full-paper formalization.** Lean checks the function-level core and Boolean corollaries
  only. The group-action classification, interpretation, prior-art assessment, and physical
  disclaimers are not formalized.
- **No theorem-level novelty for the components.** The mathematical components are classical
  or elementary; the claimed contribution is only their carefully delimited synthesis.

## Use of generative AI tools

Generative AI tools were used substantially in drafting, formalization support, literature
discovery, and adversarial review. The author takes full responsibility for the content. The
Lean proofs and finite-instance checks provide independently executable checks of the narrow
mathematical claims; they do not transfer authorship or responsibility to the tools.

## References

- F. W. Lawvere, "Diagonal arguments and cartesian closed categories," in *Category Theory,
  Homology Theory and Their Applications II*, Lecture Notes in Mathematics 92, Springer,
  1969, 134-145. DOI: 10.1007/BFb0080769.
- N. S. Yanofsky, "A universal approach to self-referential paradoxes, incompleteness and
  fixed points," *Bulletin of Symbolic Logic* 9(3), 2003, 362-386. DOI:
  10.2178/bsl/1058448677.
- G. Cantor, "Uber eine elementare Frage der Mannigfaltigkeitslehre," *Jahresbericht der
  Deutschen Mathematiker-Vereinigung* 1, 1891, 75-78.
- S. Kochen and E. P. Specker, "The problem of hidden variables in quantum mechanics,"
  *Journal of Mathematics and Mechanics* 17, 1967, 59-87. DOI:
  10.1512/iumj.1968.17.17004.
- J. S. Bell, "On the problem of hidden variables in quantum mechanics," *Reviews of Modern
  Physics* 38(3), 1966, 447-452. DOI: 10.1103/RevModPhys.38.447.
- S. Abramsky and A. Brandenburger, "The sheaf-theoretic structure of non-locality and
  contextuality," *New Journal of Physics* 13, 2011, 113036. DOI:
  10.1088/1367-2630/13/11/113036.
- J. H. Conway and S. Kochen, "The free will theorem," *Foundations of Physics* 36(10),
  2006, 1441-1473. DOI: 10.1007/s10701-006-9068-6.
- P. Curie, "Sur la symetrie dans les phenomenes physiques, symetrie d'un champ electrique
  et d'un champ magnetique," *Journal de Physique Theorique et Appliquee*, 3e serie, 3,
  1894, 393-415. DOI: 10.1051/jphystap:018940030039300.
- J. Earman, "Curie's Principle and spontaneous symmetry breaking," *International Studies
  in the Philosophy of Science* 18(2-3), 2004, 173-198. DOI:
  10.1080/0269859042000311299.
- J. D. Norton, "Curie's Truism," *Philosophy of Science* 83(5), 2016, 1014-1026. DOI:
  10.1086/687934.
- T. Breuer, "The impossibility of accurate state self-measurements," *Philosophy of
  Science* 62(2), 1995, 197-214. DOI: 10.1086/289852.
- J. Szangolies, "Epistemic horizons and the foundations of quantum mechanics,"
  *Foundations of Physics* 48(12), 2018, 1669-1697. DOI:
  10.1007/s10701-018-0221-9.
- N. D. Lawrence, "The no barber principle: towards formalised selection in the inaccessible
  game," arXiv:2604.21945, 2026.
- S. Abramsky and J. Zvesper, "From Lawvere to Brandenburger-Keisler: interactive forms of
  diagonalization and self-reference," *Journal of Computer and System Sciences* 81(5),
  2015, 799-812. DOI: 10.1016/j.jcss.2014.12.001.
- D. Frauchiger and R. Renner, "Quantum theory cannot consistently describe the use of
  itself," *Nature Communications* 9, 2018, 3711. DOI:
  10.1038/s41467-018-05739-8.
- C. Brukner, "A no-go theorem for observer-independent facts," *Entropy* 20(5), 2018, 350.
  DOI: 10.3390/e20050350.
