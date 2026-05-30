# Persona 14 — Higher / Derived / Homotopy-Coherent Geometer

**Date:** 2026-05-28
**Persona:** Derived algebraic geometry, ∞-categories, factorization algebras, higher gauge theory, BV-BRST in derived setting.
**Question:** Does reinterpreting the metric bundle and observerse projection in a derived or higher-categorical setting evade Witten 1981?

## (a) One-sentence steelman

`[speculation]` Witten 1981 is a theorem about the smooth-section moduli of a 1-categorical KK bundle; if the observerse projection is the smooth shadow of a derived stack or ∞-sheaf whose cotangent complex carries chiral cohomology in negative degree, the chirality forbidden on the smooth quotient can survive as a derived shadow on the 4-manifold.

## (b) Strongest first-principles construction

`[speculation]` Replace Met(X) → X with a derived enhancement RMet(X) → X whose underlying classical stack is Met(X) but whose structure sheaf is a sheaf of cdgas (or simplicial commutative rings) with non-trivial higher homotopy. Concretely: model RMet(X) as the derived mapping stack RMap(X, [pt/GL(4)/O(4)]) in the ∞-topos of derived smooth stacks (Carchedi-Roytenberg, Spivak). The cotangent complex L_{RMet/X} now has both classical part (the smooth fiber Sym²) and a derived part L^{<0} carrying obstruction-theoretic data.

Couple to fermions not as sections of a classical spinor bundle on the 14-dim total space, but as a factorization algebra F on RMet(X) in the Costello-Gwilliam sense. Dimensional reduction is then the pushforward π_* F along the projection π: RMet(X) → X, which lives naturally in the ∞-category of factorization algebras on X. The classical limit of π_* F is what Witten 1981 analyzes; the *derived* π_* F carries additional cohomology classes in H^{<0}.

The key move: chirality in 4D is encoded as a class in the *full* derived factorization homology, not in H^0. The Witten argument computes H^0 of the smooth direct image and finds it non-chiral. A class in H^{-k} for k ≥ 1 would not be visible to Witten's index-theoretic argument because his Dirac operator on the smooth quotient sees only π^cl_*, not Rπ_*.

Mechanism for chirality: interpret the SM fermion content as the homotopy fixed points of an ∞-action of a higher 2-group G on RMet(X), where G is a higher categorical thickening of (a piece of) the SM gauge 2-group in the sense of Schreiber-Sati's higher gauge theory. The transgression τ: H^*(BG; Z) → H^*(X; Z) along the derived projection picks up a chiral piece from the non-trivial homotopy groups π_{≥1}(G) that has no smooth-KK analogue.

## (c) Where it does load-bearing work

The construction does load-bearing work at exactly one place: it replaces the smooth direct image π^cl_* (the object Witten analyzes) with a derived direct image Rπ_*, and then claims chirality lives in degree < 0. The factorization-algebra pushforward is the formal home for "what 14D theory restricts to on 4D." If the derived pushforward carries cohomology the classical pushforward does not, the Witten 1981 obstruction (which is a statement about the classical pushforward's index) does not apply automatically.

The higher 2-group ∞-action is doing the second load-bearing job: it provides a *source* of chirality, namely the homotopy of G, that has no counterpart in 1-categorical KK where the structure group is a Lie group with trivial π_{≥2}.

## (d) What must be true mathematically

For the loophole to be real, four things must hold simultaneously:

1. **Derived enhancement is non-trivial:** RMet(X) must have non-vanishing L^{<0}, i.e., the metric bundle must carry genuine derived structure not captured by Met(X). For a contractible fiber Sym² this is non-obvious; the derived structure must come from the *mapping stack* structure, not the fiber.

2. **Witten's argument genuinely uses smooth-section moduli:** The 1981 obstruction must factor through H^0(π^cl_* F) and not through some intrinsic K-theoretic / cobordism statement that already accounts for derived enhancements. (K-theoretic chirality obstructions in the style of Freed-Hopkins likely *do* extend to the derived setting, which is a danger.)

3. **The higher 2-group action exists and gauges to SM:** There must be a higher 2-group G acting on RMet(X) whose smooth shadow includes SU(3)×SU(2)×U(1) and whose homotopy π_{≥1}(G) provides a chiral class. This is the open construction.

4. **The derived class is detectable physically:** A class in H^{<0} of a factorization algebra must correspond to a real fermion excitation, not a pure-gauge artifact of the BV-BRST resolution. This is the deepest question; in Costello-Gwilliam, negative-degree classes typically encode ghosts and antifields, not physical states.

Condition 4 is the most dangerous: it suggests the chiral "derived shadow" might literally be a ghost rather than a physical fermion.

## (e) Verdict

`[speculation]` The derived / ∞-categorical reinterpretation provides a *formal* loophole around Witten 1981's specific argument (which is genuinely 1-categorical), but the loophole is almost certainly closed by stronger K-theoretic / cobordism-level chirality obstructions (Freed-Hopkins, anomaly-as-invertible-field-theory) that lift to the derived setting. Condition 4 also makes the construction physically suspect: chirality in negative cohomological degree most likely corresponds to BV ghosts, not propagating fermions. The higher 2-group route is the only piece with a plausible physical reading, and it imports SM data by hand at the 2-group level rather than deriving it.

**Verdict: loophole is formally open against Witten 1981 narrowly construed, almost certainly closed against the stronger Freed-Hopkins-class obstructions, and physically suspect because the "derived chiral shadow" is likely a ghost. Not a productive evasion path.**
