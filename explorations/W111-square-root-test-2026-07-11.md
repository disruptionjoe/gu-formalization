---
artifact_type: exploration
status: exploration (THE SQUARE-ROOT TEST: does the outside view exist at the first-order factorization level? The fusion hypothesis -- "the fourth-order square structure and the outside-view-free Krein doublet are ONE structure, and SQUARING is the operation that COSTS the outside view" -- tested, not assumed; run to a decision)
created: 2026-07-13
hypothesis: "THE FUSION HYPOTHESIS: the UV flagship (|II|^2 -> the Stelle propagator 1/(p^2(p^2-m^2))) and the observer flagship (the W109 wall: no bounded modular conjugation over the Krein doublet tower) are one fact seen twice -- the Krein doublet IS the square's partial-fraction decomposition, and the first-order (square-root, Dirac-type) theory has a BOUNDED definitizable Krein structure over the same tower where the fourth-order conditioning diverges, so that squaring is precisely what costs the outside view."
conjecture: "the source action IS the observer (CONJECTURE-source-action-is-the-observer-2026-07-11.md)" -- adjacent; this swing tests a proposed FUSION of its wall with the UV structure, not the conjecture itself
title: "VERDICT = FUSION-DEAD (as stated), decided by a small exact theorem: SQUARE-ROOT RIGIDITY. Every square root of the interacting fourth-order mode operator commutes with it, hence shares its eigenframe, hence has EXACTLY its optimal metric conditioning: cond_1(k) = cond_4(k) = (1+r_k)/(1-r_k) IDENTICALLY over the full W98/W109 tower (p=0 and p=1; verified exactly, tests/W111, 7/7, exit 0). The first-order factorized theory is exactly as walled as the fourth-order theory -- the wall PRECEDES the square; squaring neither creates nor costs the outside view. WHAT SURVIVES (do not over-cut): (1) the Krein doublet IS the square's partial-fraction decomposition -- 1/(p^2(p^2-m^2)) = (1/m^2)[1/(p^2-m^2) - 1/p^2], opposite-sign residues of magnitude 1/|Dm^2| = the doublet grading, and the residue blow-up as Dm^2 -> 0 is the exceptional-point seed (exact); (2) squaring DOES create the GHOST: at g=0 every first-order branch is Hermitian (positive-definite quantization, NO Krein structure needed at first order) while the assembled fourth-order scalar carries the opposite-residue Krein grading -- at cond 1, ghost WITHOUT wall; (3) the wall is charged by the INTERACTION (non-UV-soft mixing over the degenerating gap Dw(k) -> 0, which is already present in the FIRST-ORDER spectrum), with the same UV-soft survival window X as W100 at every order. THE EARNED REPLACEMENT: 'squaring creates the ghost; interaction creates the wall; the wall is a factorization-level invariant (square-root rigidity).' The two flagships share the doublet SUBSTRATE but are NOT one fact seen twice via squaring. Factorization-dependence (the adversary) answered: the verdict is invariant across every canonical-frame square root (all four sign branches + the 4x4 Dirac-type D4 whose characteristic polynomial IS the fourth-order symbol); the branch bit is METRIC-INERT (one metric family for all branches -- 'the branch-choice information becomes the outside view' is killed by computation); the companion/Ostrogradsky frame is walled even FREE and is a non-canonical frame (named fork, with reason); the scalar symbol underdetermines the wall (diag(w1^2,w2^2) has the same det symbol, min-cond 1). In NO examined factorization is the first order clean while the fourth order is walled: FUSION-REAL is excluded factorization-independently."
grade: "exploration / MODEL-GRADE, two-derivation: D1 = the exact rigidity argument (any X with X^2 = M satisfies XM = X^3 = MX; the commutant of M with distinct eigenvalues is poly(M), 2-dim -- verified via the Sylvester kernel at every probe; so every square root is V-diagonal in M's own eigenframe, and the FULL positive-metric family V^{-dag} diag(p) V^{-1} is shared, with the p-independent Rayleigh lower bound cond >= (1+c)/(1-c), c = |<v1,v2>| = r_k, achieved by eta(r_k)); D2 = direct numeric verification on the W98/W109 tower (same parameters m1=0, m2=0.3, G=0.1, K0*2^22, p in {0,1}; grid minimization over the metric family per branch; tests/W111_square_root_test.py, 7/7, numpy-only, exit 0). D1 and D2 AGREE. NOT a continuum theorem; the model surface is exactly the W98 Krein doublet tower class (symmetric rigor with W98/W109 -- the same surface the wall itself lives on). No canon / RESEARCH-STATUS / CANON / claim-status / verdict / posture change; H61/H61a and the UV-structure candidate stand unchanged; the fusion narrative is CUT at the wall level and retained at the substrate level."
depends_on:
  - explorations/observer-structure-theorem-assembly-2026-07-11.md
  - explorations/break-sectorial-closure-interacting-2026-07-11.md
  - explorations/obj5-minimal-source-action-2026-07-11.md
  - papers/candidates/uv-structure-fourth-order-gravity/uv-structure-fourth-order-gravity-2026-07-11.md
  - papers/candidates/keep-and-grade-loop-cost/keep-and-grade-loop-cost-2026-07-11.md
  - docs/NEXT-FRONTIER-HYPOTHESES.md
  - GEOMETER-VS-PHYSICS-OBJECTS.md
  - tests/W98_break_sectorial_closure.py
  - tests/W109_observer_structure_theorem.py
  - tests/W102_obj5_source_action.py
  - tests/W54_path2_target3_no_local_metric.py
scripts:
  - tests/W111_square_root_test.py
external_refs:
  - "K. S. Stelle, Phys. Rev. D 16 (1977) 953 -- the fourth-order propagator 1/(p^2(p^2-m^2)) and its partial-fraction ghost."
  - "A. Pais & G. E. Uhlenbeck, Phys. Rev. 79 (1950) 145 -- the fourth-order oscillator; its canonical quantization is the DECOUPLED doublet (the canonical frame used here); the equal-frequency limit is the non-diagonalizable (Jordan) point."
  - "C. M. Bender & P. D. Mannheim, Phys. Rev. Lett. 100 (2008) 110402 -- the unequal-frequency PU oscillator's similarity/Krein structure; the transform degenerates at frequency coincidence (the companion-frame wall named in T5c)."
  - "Z. Bern, J. J. M. Carrasco, H. Johansson -- BCJ color-kinematics double copy (gravity = YM^2 at amplitude level): named ONLY to state the structural DIFFERENCE (Section 5); consistent with the repo's H6 (docs/NEXT-FRONTIER-HYPOTHESES.md): GU's 'square' is the operator square (Dirac^2 = Lichnerowicz type), not BCJ."
---

# W111 -- The square-root test: does the outside view exist at the first-order factorization level?

**Role.** The repo carries two flagships: the **UV structure** (the fourth-order `|II|^2` gravity with the
Stelle propagator `1/(p^2(p^2-m^2))` -- "the square") and the **Observer Structure Theorem** (`W109`: over
the interacting Krein doublet tower no bounded modular conjugation exists at any level -- "the wall").
GU's own framing says the higher-order theory is the SQUARE of a lower-order one ("a square and a square
root, think double copy"; the repo's `H6` reading: the operator square, `Dirac^2 = Lichnerowicz`-type).
**The fusion hypothesis** (narrative-grade before this swing): these are ONE structure -- the Krein doublet
IS the square's partial-fraction decomposition, and **squaring is precisely the operation that costs the
outside view**: the first-order (square-root, Dirac-type) theory would carry a bounded definitizable Krein
structure over the same mode tower where the fourth-order conditioning diverges.

**This swing tests it, with the pre-registered menu:** (i) first-order conditioning bounded where
fourth-order diverges -> FUSION-REAL; (ii) first-order also diverges -> FUSION-DEAD (the wall precedes the
square); (iii) no first-order Krein structure at all (positive-definite) -> FUSION-TRANSFORMED (squaring
creates ghost + wall together).

**Answer: FUSION-DEAD (as stated), by an exact rigidity theorem -- with the honest split.** The interacting
first-order theory is EXACTLY as walled as the fourth-order theory (case (ii)); but the free control lands a
piece of (iii): squaring does create the **ghost** (just not the wall). The earned replacement statement:

> **Squaring creates the ghost; interaction creates the wall; the wall is a factorization-level invariant
> (square-root rigidity).**

**Artifacts:** this file + deterministic `tests/W111_square_root_test.py` (7/7, numpy-only, exit 0).
**Not committed by this run. Not a claim-status change.** Exploration-grade.

---

## 0. Construction forks (GEOMETER-VS-PHYSICS-OBJECTS.md discipline)

| Object | Construction used | Why / load-bearing |
|---|---|---|
| **The mode model** | the repo's own `W98`/`W109` Krein doublet tower (same parameters: `m1=0`, `m2=0.3`, `G=0.1`, `k in [0.1, 0.1*2^22]`, `p in {0,1}`; metric family `eta(r) = I + r sigma_y`) | symmetric rigor: the fusion targets the `W109` wall, so it must be tested on the wall's own surface |
| **The interacting fourth-order mode operator** | `M_k = eta(r_k)^{-1/2} diag(w1^2, w2^2) eta(r_k)^{1/2}` -- quasi-Hermitian with metric exactly `eta(r_k)`; `det(w^2 - M_k) = (w^2-w1^2)(w^2-w2^2)` (the Stelle symbol preserved: the interaction collapses **eigenvectors**, not eigenvalues -- the exceptional-point mechanism `W98` already uses) | faithful to `W98`'s metric family; T2 verifies quasi-Hermiticity, symbol preservation, and that `eta(r_k)` is the **optimal** metric over the FULL family (lower bound `(1+c)/(1-c)`, `c = r_k`, achieved) |
| **The quantization frame** | the **canonical (decoupled-doublet) frame** -- the canonical quantization of the free PU Lagrangian (Pais-Uhlenbeck; Bender-Mannheim) and the frame `W98`/`W109` state the wall in | the companion/Ostrogradsky (position-variable) frame is a **coordinate presentation, not a quantization**: its transform to the canonical frame is UNBOUNDED over the tower and it is walled even FREE (T5c). Comparing first vs fourth order across inequivalent frames would be asymmetric; the fork is **named**, both sides computed |
| **The first-order theory** | standard-field mode-level square root: `D` with `D^2 = M_k` (2x2 branches) and the 4x4 Dirac-type `D4` with `char(D4) = the fourth-order symbol` | the program-native first-order object is `W102`'s `M_D`, which is **natively Krein** (`K M_D = M_D^dag K`, signature `(+64,-64)`) -- noted in Section 4: in GU-as-built the indefiniteness PRECEDES squaring, which cuts against FUSION-REAL from the native side too |

---

## 1. What is TRUE in the fusion: the doublet IS the partial-fraction decomposition (T1)

Exact and verified: `1/(p^2(p^2-m^2)) = (1/m^2)[1/(p^2-m^2) - 1/p^2]`. The two poles carry
**opposite-sign residues** `-+1/m^2` -- the Krein doublet grading `diag(+1,-1)` -- of equal magnitude
`1/|Dm^2|`, which **blows up as the poles degenerate**: the exceptional-point seed is already visible in
the partial fractions. This half of the fusion is real and survives the swing: **the doublet is the
square's partial-fraction structure** (at symbol/residue level).

## 2. The decisive computation: square-root rigidity (T3), and the tower comparison (T4)

**The rigidity theorem (model-grade, exact).** Let `M_k` be the interacting fourth-order mode operator
(diagonalizable, distinct nonzero eigenvalues `w1^2 != w2^2` -- note `w1^2 - w2^2 = m1^2 - m2^2`, a
CONSTANT: the interaction never degenerates the eigenvalues, only the eigenvectors). Then:

1. any `X` with `X^2 = M_k` **commutes** with `M_k` (`XM = X^3 = MX`);
2. the commutant of `M_k` is 2-dimensional (`= poly(M_k)`; verified: the Sylvester kernel has dimension
   exactly 2 at every probe);
3. hence **every square root is diagonal in `M_k`'s own eigenframe** `V`: `D = V diag(+-w1, +-w2) V^{-1}`
   -- exactly four branches, all constructed, all satisfying `D^2 = M_k` to machine precision;
4. hence every square root has the **same full positive-metric family** `V^{-dag} diag(p) V^{-1}` as
   `M_k` itself, with the `p`-independent Rayleigh lower bound `cond >= (1+c)/(1-c)` where
   `c = |<v1, v2>| = r_k` (the unit-eigenvector overlap), achieved by `eta(r_k)`;
5. therefore `min-cond_1(k) = min-cond_4(k) = (1+r_k)/(1-r_k)` **exactly**.

**The tower comparison (the task's decisive computation):** `cond_1(k)/cond_4(k) = 1` **identically**
across the full tower, at `p=0` and at `p=1`; both diverge together (sup doubling per octave, the
`W98`/`W109` wall reproduced). **Pre-registered case (ii): the wall precedes the square.** The genuine
first-order 4x4 Dirac-type operator `D4` (spectrum `{+-w1, +-w2}`) has characteristic polynomial equal to
the fourth-order symbol `(w^2-w1^2)(w^2-w2^2)` -- it IS the PU first-order form, the honest "square root of
the square" -- and its metric `eta (+) eta` has the identical conditioning.

**The free control (the piece of (iii) that survives):** at `g = 0` every first-order branch is
**Hermitian** -- the free first-order theory admits a positive-definite Hilbert quantization, cond 1,
**no Krein structure needed at first order** -- while the assembled fourth-order scalar already carries
the opposite-residue Krein grading of Section 1, at cond 1: **ghost without wall**. So the squaring
(assembly of the doublet into ONE higher-derivative scalar) genuinely creates the **indefiniteness**; it
just does not create (or cost) the **wall**. The wall needs the interaction, and the interaction walls the
first-order theory identically (rigidity).

## 3. Factorization-dependence: the adversary answered (T5, T6)

The adversary: *"your first-order D is a chosen factorization -- a different square root changes the
answer."* Checked four ways:

- **(a) Branch invariance.** All four sign branches + `D4` share ONE metric family (rigidity). The branch
  bit is **metric-inert**: it costs nothing on any state and can store nothing. The sub-narrative "the
  two square-root branches collapse under squaring and the branch-choice information becomes the
  inaccessible outside view" is **killed by computation** -- the branch bit has no metric content to lose.
- **(b) Frame covariance.** Conjugating `D` and `M` by the same bounded frame preserves the equality
  `min-cond_1 = min-cond_4` (same transformed family). The rigidity is not an artifact of the frame.
- **(c) The companion/Ostrogradsky frame (the one real fork, named).** The balanced position-variable
  first-order form (Vandermonde eigenframe over nodes `{+-w1, +-w2}/wbar`) is walled **even free**: its
  eigenvector overlap `-> 1` as `Dw -> 0` regardless of interaction. It is NOT a canonical quantization
  (its transform to the canonical doublet frame is unbounded over the tower; the canonical quantization
  of the free PU Lagrangian is the decoupled doublet -- Pais-Uhlenbeck, Bender-Mannheim). Named, not
  defaulted. Note the direction of this fork: if one insisted on the position frame, the wall would
  precede even the **interaction** -- still not FUSION-REAL.
- **(d) Symbol underdetermination.** `diag(w1^2, w2^2)` has the same fourth-order det symbol as `M_k`
  with min-cond 1: the scalar **symbol** does not carry the wall. The wall is data of the
  **(operator, inner product) pair** -- and that pair is exactly what square-rooting cannot change.

**Conclusion, invariance in the direction that matters:** in NO examined factorization is the first-order
theory clean while the fourth-order theory is walled. FUSION-REAL is excluded
**factorization-independently**; the verdict does not flip across natural square roots, so no UNDECIDED
fork remains.

**Order-independence of the wall condition (T6).** The first-order spectrum `{+-w1, +-w2}` contains the
SAME degenerating gap `Dw(k) -> 0` (between the `+w1` and `+w2` branches) that drives the fourth-order
wall -- so any non-UV-soft **first-order** mixing walls the first-order theory directly, no pullback from
fourth order needed; and the UV-soft window `g = o(1/k)` is the same survival boundary `X` as `W100`, at
every order. **Fake-escape guard:** the eigenvalue gap of `M_k` is the CONSTANT `|Dm^2|` (squaring "opens"
the gap from `Dw -> 0` to a constant), yet the conditioning diverges anyway -- the wall lives in the
**eigenvector collapse**, not in an eigenvalue gap. "Squaring cures the degeneracy" is a fake escape,
tested and closed.

## 4. Contact with the repo's other structures (honest, no overreach)

- **`W54` (the no-local-positive-metric theorem, fourth order).** No first-order analogue exists at free
  level, and that is itself informative: the free first-order multiplet is positive-definite with the
  trivial (local) metric `I` -- there is nothing non-local to prove. `W54`'s non-locality cost, like the
  ghost sign, is created by the scalar **assembly** (the metric that positivizes the assembled scalar
  must mix the `1/w_i` symbols and inherit their branch cuts). Squaring's costs are the ghost and the
  metric non-locality; the wall is not among them.
- **`W102` (GU's native first-order structure).** GU-as-built does not match even the "squaring creates
  the ghost" half cleanly: `M_D` is **natively Krein-self-adjoint** (`K M_D = M_D^dag K`, `beta_S`
  signature `(+64,-64)`) -- in GU the indefiniteness is present BEFORE any squaring. Both readings
  (standard-field positive free multiplet; GU-native indefinite `M_D`) agree on the verdict direction:
  neither gives a bounded first-order `J` over a walled fourth-order tower.
- **`W109` untouched.** The Observer Structure Theorem gains a small strengthening in kind, not a change:
  its clause-3 absence is now known to be **invariant under factorization level** on the model class --
  one cannot evade the wall by passing to the square root. Nothing in `W109`'s statement, grade, or named
  lifts moves.

## 5. The double-copy paragraph (one, honest)

The "square" here is **operator composition**, not the BCJ double copy -- consistent with the repo's `H6`.
BCJ color-kinematics squares **numerators** over the SAME set of propagator poles (gravity amplitudes =
gauge-squared kinematic factors / the same `1/p^2` poles), and its extra states (dilaton, B-field) are
positive-norm tensor-product states, not ghosts. The Stelle square multiplies **pole structures**
(`1/p^2 * 1/(p^2-m^2)`), and its extra state is the opposite-residue partial-fraction ghost -- a different
squaring operation with a different cost. The GU slogan's honest reading (`Dirac^2 = Lichnerowicz`-type
operator square) is the one this swing tested, and at that reading the square-root level buys nothing
against the wall (rigidity). Superficially similar, structurally different; no BCJ import is made, and no
BCJ escape from the wall is available (an amplitude-level double copy would not alter the mode-level
metric family either -- it is a statement about numerators, not about the inner product).

## 6. The verdict and the theorem-shape

**VERDICT: FUSION-DEAD (as stated).** "Squaring costs the outside view" is false: the first-order
factorized theory of the interacting fourth-order operator is exactly as walled, by rigidity, invariantly
across factorizations, at `p=0` and `p=1`, over the same tower where `W109`'s conditioning diverges.

**The earned replacement (model-grade, two derivations agreeing):**

> **Square-root rigidity.** On the `W98` Krein doublet tower class: every square root of the interacting
> fourth-order mode operator shares its eigenframe and hence exactly its optimal metric conditioning
> (`min-cond_1 = min-cond_4 = (1+r_k)/(1-r_k)` identically); the `W109` outside-view absence is therefore
> a **factorization-level invariant** -- squaring neither creates nor costs it. What squaring does create
> is the **ghost** (the opposite-residue Krein grading of the assembled scalar, from a positive-definite
> free first-order multiplet) -- bounded, wall-free. The wall is charged by the interaction (non-UV-soft
> mixing over the degenerating gap `Dw(k) -> 0`, already present in the first-order spectrum), with the
> same survival window `X` at every order.

The two flagships are **not** one fact seen twice via squaring. They share the doublet **substrate** (the
partial-fraction structure, Section 1 -- true and kept), and they are connected by the rigidity statement
(the wall cannot be factored away) -- a weaker, but real and now theorem-shaped, bridge.

## 7. Honest limits

1. **Model-grade only.** The rigidity argument is exact linear algebra per mode on the `W98` tower class;
   it is NOT a continuum operator-algebra statement. Its application to GU inherits every named condition
   of `W98`/`W109` (non-UV-soft coupling, HORN K, the Krein doublet reading).
2. **"Every square root" means every square root of the SAME interacting operator.** If GU's physical
   first-order theory is not required to square to the interacting fourth-order operator (i.e., if the
   interaction genuinely lives only at fourth order and the first-order theory is free), the free control
   applies -- but then the fourth-order theory at that level is also unwalled (ghost without wall), and
   the fusion still fails: there is no regime with a walled square over a clean square root.
3. **The companion-frame fork is named, not adjudicated beyond the canonical-quantization argument.**
   Both frames were computed; neither yields FUSION-REAL.
4. **No canon / RESEARCH-STATUS / CANON / claim-status / verdict / posture change.** H61/H61a remain OPEN;
   the `W109` theorem and the UV-structure paper candidate stand unchanged; the fusion narrative is cut at
   the wall level and retained at the substrate level. This branch presents, does not decide.

*Filed 2026-07-13 (W111 swing; task-named path retains the 2026-07-11 series stamp). Reproducible:
`python -u tests/W111_square_root_test.py` (exit 0, 7/7 PASS). Not committed by this run.*
