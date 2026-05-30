# Problem Shape — Nondeterminism / Orbit-Equivalence / Type II$_1$ / Free Probability (Heterodox)

**Date:** 2026-05-28
**Baseline accepted:** Computation is substrate. Geometry is observer-frame artifact. The bundle is emergent. No-go theorems constrain observer-frames, not substrate. (00c)
**Persona:** Operator-algebraist with strong heterodox lean — Voiculescu free probability, Jones subfactors / planar algebras, Connes embedding and MIP* = RE, Bost-Connes, descriptive set theory of Borel equivalence relations, Connes' noncommutative geometry past the smooth spectral triple.

## (a) Thesis (mainstream-in-domain)

Textbook operator-algebra reading of the substrate-first frame: model the substrate by a separable Hilbert space $H$, observables by $\mathcal{B}(H)$ (Type I), and the observer-frame projection by orthogonal projection onto an invariant subspace under some group action. Independence is tensor; states are normal; spectral theory is Lebesgue. The "observerse" projection becomes a conditional expectation onto a Type I subfactor. Chirality is encoded as a representation of a CAR algebra on $H$. Standard, smooth, decidable, and inherits Witten / Freed-Hopkins through the type-I commutant structure exactly as the smooth-bundle thesis did. The substrate-bundle inversion buys nothing because the von Neumann algebra is already isomorphic to a bounded-section algebra.

## (b) Heterodox antithesis

Five moves break the Type I mainstream:

1. **Type II$_1$ as the natural substrate algebra.** Murray-von Neumann's continuous dimension function $\dim : \mathrm{Proj}(M) \to [0,1]$ is exactly the kind of non-integer, observer-frame-rescalable quantity a substrate-first reading wants. Bundle reductions produce integer dimensions; substrate projections produce continuous trace. The "amount of observerse" projected at a point is a real number in $[0,1]$, not a fiber dimension.

2. **Voiculescu free independence replaces tensor independence.** The substrate noise is **free**, not classical, not even quantum-tensor. Free CLT yields the semicircle law instead of the Gaussian. The observer extracts a tensor-independent marginal only after frame-fixing. Pre-frame, the substrate's correlation structure is free-probabilistic. [speculation] The smooth-bundle thesis silently assumes tensor independence on the fiber; this is where it imports classical-noise structure into a substrate that may not have it.

3. **Jones subfactor inclusions as the geometric primitive.** An inclusion $N \subset M$ of II$_1$ factors carries a Jones index $[M:N] \in \{4\cos^2(\pi/n) : n \ge 3\} \cup [4, \infty]$, a Jones tower, and a planar algebra $\mathcal{P}_\bullet(N \subset M)$ that is a 2-dim TQFT-class invariant. The "observerse projection" becomes the conditional expectation $E_N : M \to N$. The "fiber" is the standard invariant, a planar algebra, not a vector space. Witten 1981 has no purchase here because the reduction is conditional expectation, not Levi-Civita pullback.

4. **MIP* = RE (Ji-Natarajan-Vidick-Wright-Yuen 2020) and Connes' embedding failure.** Some quantum correlations are not in the closure of finite-dimensional ones. The substrate may live in the non-embeddable regime. If so, no approximation by Type I$_n$ or matrix limits can reproduce it; this is a genuine substrate-class boundary that no smooth or even tensor-network approximation crosses. [speculation] Chirality could be a non-embeddable correlation: a $\mathbb{Z}/2$-asymmetry visible only in correlations that no finite-dimensional, hence no smooth-bundle, observer-frame can sample. This would make Witten 1981 not just non-applicable but **structurally blind** at the bundle level.

5. **Bost-Connes and Borel-equivalence complexity.** Bost-Connes systems realize KMS-state phase transitions as Galois-symmetry breaking on an arithmetic algebra; the reduction $14 \to 4$ becomes a low-temperature phase. Descriptive set theory (Hjorth, Kechris, Adams) classifies Borel equivalence relations past smooth into a rich hierarchy ($E_0$, treeable, anti-treeable, F$_2$-superrigid). The orbit-equivalence quotient class P3 named at 00b is generically **anti-classifiable**: in many cases there is no Borel-measurable invariant separating orbits.

## (c) Aufhebung as a problem-shape question

Thesis says the substrate sits inside $\mathcal{B}(H)$ and its inclusions are tensor; antithesis says the substrate is a II$_1$ factor and its inclusions are subfactor-with-planar-algebra. The Aufhebung within the domain:

> **The observerse is a subfactor inclusion $N \subset M$ of II$_1$ factors; the projection is conditional expectation $E_N$; the Standard Model is a planar-algebra invariant of the inclusion; chirality lives in the non-embeddable / Connes-non-Cep regime where finite-dim approximation fails.**

This yields the problem-shape:

> **What subfactor inclusion $N \subset M$ of II$_1$ factors has planar-algebra standard invariant $\mathcal{P}_\bullet(N \subset M)$ whose low-temperature KMS-phase content recovers the SM gauge data, and is the inclusion Connes-embeddable or does it live in the MIP*-witnessed non-embeddable regime?**

## (d) What WRK-326 should ask next from this lens

Stop asking "does the bundle reduction deliver chiral SM." Start asking: **name the subfactor inclusion and read its planar algebra.** Concretely:

- Specify candidate II$_1$ inclusions: hyperfinite $R \subset R^G$ for a discrete group $G$ acting outerly; group-subgroup subfactors with $G = \mathrm{SU}(3) \times \mathrm{SU}(2) \times \mathrm{U}(1)$; depth-2 inclusions with quantum-group symmetry; Bisch-Haagerup subfactors with the SM as their principal graph asymptote.
- For each, compute the Jones index and check whether it sits in the discrete tower or the continuous spectrum $[4, \infty)$, and whether the principal graph is finite (amenable) or infinite (non-amenable).
- Check Connes-embeddability of the inclusion. If non-embeddable, the inclusion encodes correlations no smooth-bundle frame can reproduce; chirality may live there.
- Frame the GR limit as the KMS-state low-temperature symmetry-breaking on a Bost-Connes-class arithmetic algebra over the inclusion.

## (e) Falsifiable mathematical sub-question

> **Does there exist a II$_1$ subfactor inclusion $N \subset M$ of finite Jones index whose standard invariant (planar algebra) admits a fusion-category quotient equivalent to $\mathrm{Rep}(\mathrm{SU}(3) \times \mathrm{SU}(2) \times \mathrm{U}(1))$, and is this inclusion Connes-embeddable?**

A negative answer to the existence half (Popa-class rigidity or Bisch-Jones planar-graph classification rules out such an inclusion at any finite index) closes the heterodox subfactor route at the planar-algebra layer. A positive answer with Connes-embeddable inclusion hands WRK-326 a concrete planar-algebraic SM derivation that competes with the Connes spectral-triple program named at 00b Finding B. A positive answer with **non-embeddable** inclusion is the most interesting outcome: it would witness chirality as an MIP*-class correlation invisible to every smooth or tensor-approximated observer-frame, which would explain at the substrate level **why** Witten 1981 / Freed-Hopkins always close at the bundle level without being violated by anything observable.
