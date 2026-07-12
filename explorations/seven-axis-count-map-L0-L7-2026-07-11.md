# The seven-axis count map (L0-L7): H37 discovers the geometry-side axis; the count collapses to one hinge

> **WAVE-14 CORRECTION (2026-07-11, read first).** The headline below ("the count collapses onto the L7
> signature hinge H19") is now **superseded**. Wave 14 (`tests/wave14/H19_seven_seven_branch.py`, exit 0)
> computed the (7,7) branch and found L7 is **live-but-non-deriving**: adopting (7,7) lifts the Kramers
> 2-primary *veto* (odd ranks 1,3,5,7 become admissible) but is **structurally incapable of supplying the
> count**. The signature is a **2-primary** datum (`p-q mod 8 in Z/8`); the count 3 lives in the orthogonal
> **Z/3** arena of `pi_3^s = Z/24`; `|Hom(Z/8,Z/3)| = gcd(8,3) = 1` (the zero map). So a signature move
> *cannot reach* the arena where 3 lives, and the triplet carrier is neutral Krein (net index 0) in **both**
> signatures. The count therefore does **not** collapse onto H19/the signature; (7,7) trades a false
> constraint for *more* freedom and is **not recommended**. The count's real decider is
> **signature-independent** -- the **Z/3-arena chiral selector** (a ghost-parity matter dynamics
> `[P_ghost, S]=0`, the new H38), attacked *without* first settling the signature. Read the map below as the
> route that *led* to this sharper result: L0-L6 locked, L7 identified as the one geometry escape, then L7
> itself shown to lift a veto in the wrong primary arena. See `explorations/wave14/`.
>
> **WAVE-15 UPDATE (2026-07-12).** The signature-independent Z/3 selector was computed
> (`tests/wave15/H38_z3_chiral_selector.py`, exit 0). A **derived Z/3 grading IS present** in the built
> `(9,5)` matter sector (the order-3 subgroup of the self-dual `SU(2)+` on the `192 = 3x64` triplet; the `3`
> is `dim Lambda^2_+(R^4)`, forced by the 4-base, not imported, not ambient triality). But ghost parity
> `[P, S]=0` is **2-primary and index-preserving**, so it permits the vectorlike `3 + 3` and cannot select a
> chiral 3. The count needs a **3-primary AND index-changing** operator -- not a ghost-parity condition but a
> **source-action K-class selection** (SG4, the count's new decider), a property of the *same* unbuilt source
> action the gravity soldering reduces to. See `explorations/wave15/`.
>
> **WAVE-16 UPDATE (2026-07-12).** SG4 computed (`tests/wave16/H39_sourceaction_kclass.py`, exit 0). Carrier
> B (index -38, order-3 `rho=(0,2,1)`) is the **unique index-changing** RS carrier, so any count-selector
> must be B; but which carrier the source action *names* is a **field-space declaration** arithmetic cannot
> force (gamma-trace-constrained -> B; full field space + BRST -> A). So **the count is now a
> conditional-theorem twin of gravity**: located-not-forced modulo one K-class declaration, exactly as gravity
> is Stelle-clear modulo one soldering postulate. Two honest results: the count is narrowed to odd rank in
> `{1,3}` (ceiling `dim Lambda^2_+=3`, not pinned -- a net index 3 has residue 0 = carrier A's); and
> selecting the count via B does **not** break gravity's `[P,S]=0` (arena-orthogonal `gcd(2,3)=1`, and a
> Krein-self-adjoint operator can carry nonzero chiral index). Both faces reduce to ONE forced source-action
> build (the terminal object, H40). See `explorations/wave16/`.
>
> **WAVE-17 UPDATE (2026-07-12), the terminal state.** The forced build was attempted
> (`tests/wave17/H40_terminal_sourceaction.py`, exit 0). The Porrati-Rahman causal window IS a genuine
> structural forcing (the built `C2=155.36` leakage is a real VZ acausality on curved `Y14`, degree-1, so the
> cure is demanded) -- it collapses the 4-corner residual to the 2 **causal** cures `{A,B}`, removing one bit.
> But both are causal, so the final constrain(B)-vs-gauge(A) bit stays a **B-leaning lean**, not forced. The
> **count stays `{1,3}`** (order-3 on `Lambda^2_+` is `SO(3)`: fixed axis + rotated pair; net index 3 =
> residue 0 = carrier A's, so no order-3 datum certifies 3 -- the "forces 3" inference refused). Soldering
> (even) and gamma-trace (odd) are two independent declarations under one geometric-posture meta-choice. The
> program is **one forced build from complete, and the build needs one unbuilt input** -- the source action's
> causal-cure term (a non-minimal RS coupling); GU has the acausality trigger, not the cure. This is the
> honest terminal boundary. See `explorations/wave17/`.

2026-07-11. Joe's move: apply the six-axis escape-hatch framework (`canon/six-axis-escape-hatch-map-RESULTS.md`)
"now seven, with L0" to the generation-count no-go, in light of the Wave-12/13 results (H29, H37). This is a
clean reclassification, and it lands a sharp conclusion: **every axis but one is now proven LOCKED, and the
entire generation-count question collapses onto a single new geometry-side axis -- the signature.**

## Why the original six axes could not see the escape

The six-axis map quantified over **selector-side** moves only -- L1 substrate, L2 observer, L3 pairing,
L4 causal-order, L5 emergence, L6 coordination-loop -- and proved the **hard core**: no selector-side axis can
supply the count (2-primary blindness G2; under-determination G1; the boundary-`eta` test C10). Its one real
escape (C6, Distler-Garibaldi scope-exit) was an *indefinite-signature* move that returned the wrong KIND
(order-2, not the order-3 count). The map's own framing is "selector-side": it was structurally incapable of
including a move that is NOT a selector -- a change of the ambient geometry itself.

H29/H37 found exactly such a move, and it is the ONLY escape.

## The two new levels

- **L0 = the baseline (the built structure itself).** No move: the source action on the `(9,5)`/H-class ambient,
  with its positive-Hessian Koszul-Tate/BV grading and no import. This is the floor the whole map sits on.
- **L7 = the signature / real-form axis (geometry-side).** The choice of the ambient Clifford real form,
  `Cl(9,5)=M(64,H)` (`J^2=-1`, class CII) vs `Cl(7,7)=M(128,R)` (`J^2=+1`). This is orthogonal to all six
  selector-side axes -- it changes the geometry, not the selector -- which is precisely why the six-axis map
  could not contain it.

## The seven-axis verdict on the count (L0 -> L7)

| Axis | Kind | Verdict on the count | Basis |
|---|---|---|---|
| **L0** baseline (built `(9,5)` + positivity + no-import) | geometry (floor) | **LOCKED** -- count provably NOT forced | H37 no-go (`tests/wave13/H37_count_nogo.py`): `{G,H_bd}=0 => eta=0`; Kramers `J^2=-1 =>` mod-2 index 0; positivity forces `V^2=0=>V=0`; the only symmetry escape (antilinear chiralizer) is frame-charge-0 = the forbidden import |
| **L1** substrate | selector | LOCKED | six-axis map (G1: richer substrates return the wrong kind) |
| **L2** observer/consensus | selector | LOCKED | six-axis map (avalanche/metastable stays 2-primary, like BFT) |
| **L3** pairing | selector | LOCKED | six-axis map |
| **L4** causal-order | selector | LOCKED | six-axis map (supplies only a 2-primary orientation bit) |
| **L5** emergence/SOC | selector | LOCKED | six-axis map |
| **L6** coordination-loop | selector | LOCKED | six-axis map (loop attractor selects, does not carry, the order-3) |
| **L7** signature / real-form | **geometry (NEW)** | **THE ONE LIVE ESCAPE** | H37 positive control: on `(7,7)` `J^2=+1` the odd rank-3 projector is ADMISSIBLE (the mod-2/Kramers lock lifts); on `(9,5)` it is forbidden |

**The collapse.** L0 and L1-L6 are all LOCKED (H37 no-go + the six-axis hard core). The generation-count
question therefore reduces to the single new axis **L7 = the signature**: *is GU's Y^14 the `(9,5)`/H-class or
the `(7,7)`/R-class real form?* That is exactly the standing H19 question -- now revealed as **the sole
load-bearing hinge for the entire count.**

## What H37 adds to the six-axis map (the two-leg refinement)

H37 sharpens WHY the lock holds and exactly WHERE it lifts, splitting the count-obstruction into two legs:
- **Z-eta / grading leg** (`{G,O}=0 => eta=0`): **signature-INDEPENDENT** -- it holds on `(7,7)` too. Not the
  hinge.
- **Kramers / mod-2 nullity leg** (`J^2=-1 =>` even multiplicity => no odd nullity): **signature-DEPENDENT** --
  it is THIS leg that lifts under `(7,7)` (`J^2=+1`), admitting the odd rank-3.

So L7 is not a vague "different geometry" -- it is specifically the `J^2` sign that flips the Kramers leg. This
also **retroactively explains C6 (DG scope-exit)**: DG was the indefinite-signature *hint*; L7 is its clean
formalization, and it shows why DG gave order-2 (it moved on the grading leg, which is signature-independent)
rather than the order-3 count (which needs the Kramers leg, i.e. the `J^2` flip).

## Honest limits (do not overclaim)

- **L0's lock is conditional** on two canon legs H37 cites rather than independently re-closes: "positive KT
  Hessian forces the grading" (`C-01`) and "the antilinear chiralizer is the unique GU-native grading-breaker"
  (capstone item-3 uniqueness -- its own flagged softest link). The no-go is a genuine symmetry-class
  exhaustion *given* these; it does not close full operator-space uniqueness.
- **L7 makes the count POSSIBLE-to-force, not automatically 3.** Even on `(7,7)` the RANK stays
  under-determined (SG1 / `C-06`): the odd projector is admissible (odd count no longer forbidden), but which
  odd rank -- 1, 3, 5 -- is not fixed by the signature alone. So `(7,7)` removes the *prohibition*, it does not
  *derive* three.
- No `3 / 24 / 24-8` imported anywhere; `C2 = 155.3625` unchanged (acausal trap avoided); `C2/bare = sqrt(7)`.

## Net

Applying the framework as L0-L7 collapses the generation-count problem from "a diffuse question across ~34
blockers and six axes" to a single, sharply-stated hinge on ONE new geometry-side axis: **the `(9,5)`-vs-`(7,7)`
signature (L7 = H19).** Below that hinge (built `(9,5)`), the count is PROVABLY located-not-forced -- the exact
structural twin of the gravity conditional theorem (H27). This makes H19 the single highest-leverage open
question for the count, and gives it a crisp meaning: L7 is the only axis on which the count is not already
locked.

## Grade

Synthesis / reclassification. The L0 lock is H37-computed (exact, positive-control-verified) modulo the two
cited canon legs; the L1-L6 locks are the six-axis map (its stated grades); L7 as a distinct geometry-side
axis is the contribution here, grounded in the H37 two-leg split. No claim/canon movement; feeds H19 and the
flagship (the count leg is now a proven conditional, signature-contingent). No `3` imported.
