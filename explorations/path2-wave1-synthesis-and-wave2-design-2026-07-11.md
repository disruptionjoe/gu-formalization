# Path 2 wave 1 -- orchestrator synthesis + wave 2 design

Five blind branches attacked "does the keep-and-grade ghost rescue survive at LOOP level?" from five rival
constructions (A Cutkosky-cut, B PT/C-operator, C fakeon, D Lee-Wick, E adversarial no-go), mutually blind. This
is the synthesis, the cross-test, and the wave-2 target the wave produced. Tests W48-W52 all exit 0.

## 1. The high-level picture: the pre-registered SPLIT landed, and it is coherent

The wave did not prove the rescue works, and did not cleanly kill it. It produced the third pre-registered
outcome -- a precise MAP of which rescue costs what -- and the five blind branches converged on that map with
remarkable agreement. The map has a clean structure: **the rescues fall into two families that pay for loop
unitarity in two different currencies.**

**Family 1 -- GRADING-based (keep the ghost, grade the inner product): A, B.** Give positivity via an indefinite
(Krein / PT) metric with a grading (C-)operator.
- **Grading alone does NOT confine the loop ghost cut (Branch A).** For a *stable* Krein-graded ghost the optical
  theorem leaks a negative contribution on the physical subspace at one loop, located exactly at the
  graviton+ghost threshold `s = m2^2`. Tree positivity (Bender-Mannheim / Pais-Uhlenbeck) is *silent* here
  because 0+1-dim QM has no continuum cut -- which is precisely why tree positivity does not imply loop
  positivity. The ghost decouples only if it is additionally treated as a complex-pole/removed object (Family 2).
- **Where positivity DOES hold, the cost is LOCALITY (Branch B).** The C-operator / positive metric exists order
  by order (proven in QM: free PU exact, first interacting correction unique, `C^2=1`, `eta>0`), but the
  equivalent Dirac-Hermitian Hamiltonian is **non-local** -- its generator carries energy denominators
  `1/sqrt(k^2+m^2)` whose symbol is non-entire (branch points at `k=+-im`). You get manifest positivity
  (non-local `h`) OR manifest locality (PT-Hermitian `H`, whose loop causality is exactly what critics dispute),
  never both manifestly.

**Family 2 -- REMOVAL-based (take the ghost out of the asymptotic spectrum): C, D.** Never let the ghost be an
external state.
- **Fakeon (Branch C):** Q-cut YES *by construction* (the average-continuation prescription cancels the ghost's
  absorptive part exactly -- verified on the one-loop bubble), Q-pos RG-stable in-scheme, but Q-caus micro-
  causality violated within `~1/m2` (Lorentz invariance retained). Bounded/unobservable IF `m2` is heavy;
  **fatal if the ghost is light.**
- **Lee-Wick (Branch D):** Q-cut YES at one loop -- the one-loop self-energy pushes the ghost pole off-axis in
  the **proven-right direction** (`Im Sigma(M^2) > 0`, fixed by the massless-bubble discontinuity and positive
  spin-2 phase space) and the ghost is above threshold *because it is the heaviest mode*; the GOW complex-pole
  cut then carries only positive-norm real states. Q-caus micro-causality violated at `~1/M` (Planckian),
  Lorentz-invariant. One-loop proof-of-concept.

## 2. The unanimous finding (four independent constructions agree)

**At loop level, 4th-order-gravity unitarity is a TRADE against micro-causality / locality -- there is no free
lunch.** A (the saving prescription costs causality), B (positivity costs locality), C (unitarity costs
micro-causality), D (unitarity costs micro-causality) all reach this independently and blind. That is a genuine,
GU-independent structural result about the whole class (Stelle / conformal / agravity): the keep-and-grade rescue
does not remove the ghost problem, it **converts it into a causality problem**, and the conversion is bounded to
the ghost scale `~1/m2` (so plausibly Planckian and controllable, not automatically fatal).

## 3. The cross-test A-D vs E (the payoff the blind architecture bought)

Branch E's obstruction: the positivity-defining grading is **dynamical** (coupling-dependent, not kinematic),
exists only on an open PT-unbroken domain, and **degenerates to zero on a codim-1 exceptional (Jordan) locus** ->
loop positivity is **RG-contingent, not structural**; tree positivity only certifies the free point. Class-wide
(via the repo's R1 equivalence: positive grading <=> Krein-diagonalizable real-spectrum action), and it
pre-empts the obvious repair ("the grading is the kinematic Cartan involution, so it can't run" -- R1 says the
kinematic form is indefinite, not positivity-defining). Crucially E does **not** touch pseudo-unitarity
(`S^dag eta S = eta`, Bateman-Turok, all-orders, undisputed).

Cross-testing E against the four constructions resolves the whole picture:
- **E lands on Family 1 (A, B).** Their positivity is exactly the dynamical grading E shows is RG-contingent. So
  Family 1's loop positivity is not structural -- it survives only if the RG flow stays in the PT-unbroken
  domain.
- **E is EVADED by Family 2 (C, D).** Fakeon and Lee-Wick do not rely on a positive grading at all (they remove
  the ghost from asymptotic states), so "the grading degenerates" does not apply to them -- but they pay E's
  cost in the *causality* currency instead.

So the wave reveals a conservation-like law: **you pay for loop unitarity either in positivity-robustness
(Family 1, RG-contingent -- can fail on an exceptional locus) or in causality (Family 2, bounded ~1/m2).** No
branch found a construction that pays neither.

## 4. Where this sits against the blockbuster bar

- NOT a clean proof the rescue works (grading-alone fails; Family 1 positivity is RG-contingent).
- NOT a clean class-wide kill (E is a rigorous *burden-flip*, not a completed no-go; Family 2 evades it).
- IT IS a precise, rigorous-able MAP that decides the *character* of the whole class: loop-level 4th-order-gravity
  unitarity is a positivity-vs-causality trade with two rescue families paying in different currencies. Made
  rigorous, "the loop-level cost structure of keep-and-grade 4th-order gravity" is a genuine GU-independent
  contribution -- referee-grade as a *structural* result, short of the full theorem.

And the wave handed a razor-sharp, and possibly DECISIVE, wave-2 target (below), because E's burden-flip connects
directly to machinery we already built (the asymptotic-freedom flow, W45-W47).

## 5. Wave 2 design (the wave produced its own next target)

**Target 1 -- THE DECISIVE ONE (a SWING, uses machinery we already have).** E reduced Family-1 loop positivity to
a single question: **does the 4th-order + RS RG flow reach the PT-breaking / exceptional (Jordan) locus, or does
it stay in the PT-unbroken domain?** We already have the flow -- the asymptotic-freedom beta functions (H57/H60,
tests W45-W47), whose trajectory sits at a negative conformal-mode ratio `f_0^2/f_2^2 < 0`. So the swing is:
map E's exceptional-locus criterion onto the AF trajectory and check whether the flow crosses it.
  - If the AF flow stays PT-unbroken all the way to the UV fixed point -> **Family-1 positivity is RG-stable for
    this theory** -> keep-and-grade WORKS for asymptotically-free 4th-order gravity (proof-of-concept, the
    strongest available outcome, and it closes GU's UV North Star as a conditional YES).
  - If the flow crosses the exceptional locus -> Family-1 positivity fails, and Family 2 (the bounded causality
    trade) is the only surviving route -> a sharp, honest narrowing.
  This is decisive either way and reuses `BetaSystem` from W45. Cross-share for this swing (allowed -- it is not
  a blind branch): E's Jordan-locus / exceptional-point criterion + A/D's complex-pole (pole-collision) picture +
  the W45-W47 beta system, handed to one worker.

**Target 2 -- Family-2 firm-up (a SWING).** D's one killing obstruction: a `>=2`-loop CLOP-contour pinch for the
*broad*, derivative-coupled gravitational Lee-Wick resonance (proven-safe only for narrow scalar/gauge Lee-Wick).
A two-loop CLOP-stability check decides whether Family 2's one-loop unitarity is all-orders-robust.

**Target 3 -- B's burden-to-theorem (a SWING, GU-independent, publishable).** Prove (or refute) that NO local
positive metric exists for the interacting 4th-order QFT. A "no local positive metric" theorem upgrades B's
Q-caus FAIL from a symbol-level argument to a theorem and would make Family 1's locality cost rigorous and
class-wide.

**Recommendation:** run **Target 1 as the next swing** -- it is decisive, it reuses the AF machinery, and it is
the direct continuation of E's burden-flip; it can turn "keep-and-grade positivity is RG-contingent" into a
concrete YES or NO for the specific asymptotically-free theory. Targets 2 and 3 are the follow-on firm-ups
(and Target 3 is independently publishable). A full second blind wave is NOT warranted yet -- wave 1 already
converged the map; wave 2 is a focused decisive swing, not a re-fan-out.

## 6. Honest register
This is one-loop / QM-order / symbol-level work across the board (each branch graded its own confidence: A/D
one-loop indication, B interacting-order QM + structural QFT argument, C by-construction, E rigorous mechanism +
plausibility for the completed kill). The MAP is solid; the individual verdicts are indications, not proofs. No
canon / RESEARCH-STATUS / claim-status / verdict / posture changed; H59 remains OPEN.
