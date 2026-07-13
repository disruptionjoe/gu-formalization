---
artifact_type: exploration
status: exploration
created: 2026-07-12
hypothesis: H59 / H61a (unified UV loop-positivity + observer-conjecture Krein-TT residual)
branch: "W78 -- the decisive shared residual: is GU's spin-0 conformal-factor mode PHYSICAL or a GAUGE ARTIFACT?"
title: "The spin-0 conformal-factor mode of GU's induced |II|^2 action is a genuine PROPAGATING PHYSICAL DOF (the R^2 scalaron), NOT a gauge artifact -- established two independent ways (DOF/constraint count; Weyl-BRST + GHP-scope), with the gauge-escape additionally CLOSED by H49 (GU must break conformal invariance via the induced Einstein term to survive rotation curves, and that same feature makes the conformal mode non-gauge). BUT the physical mode is a positive-norm TACHYON (M_0^2<0), not a ghost -- so the two North Stars SPLIT: GU's loop-POSITIVITY (norm) is NOT threatened by it (positive norm; spin-2 PT-unbroken per W53) and plausibly still closes; the observer conjecture's Krein-TT (real-positive Delta spectrum) IS put PT-broken around flat space by the tachyon and is obstructed there, liftable only by a non-tachyonic true vacuum. VERDICT: PHYSICAL, character = tachyon => CONDITIONAL on GU's vacuum, and the naive 'both close / both no-go' binary is REFINED into a split."
grade: "exploration / gauge-status PROVEN NOT-gauge two independent ways + H49 fork-closure (rigorous within the fourth-order Stelle/agravity truncation that GU's induced action lands in); tachyon-vs-ghost character graded PLAUSIBLE (standard agravity: scalaron positive-norm, ghost only spin-2) with the norm-sign flagged as load-bearing; vacuum-selection residual OPEN. Deterministic test tests/W78_conformal_mode_gauge_status.py, exit 0. No canon / RESEARCH-STATUS / claim-status / verdict / posture changed. H59/H61a remain OPEN."
depends_on:
  - explorations/H61a-rank2-verdict-and-convergence-2026-07-11.md
  - explorations/path2-wave2-target1-af-flow-vs-exceptional-locus-2026-07-11.md
  - explorations/path2-branchE-nogo-2026-07-11.md
  - explorations/path2-branchA-cutkosky-cut-2026-07-11.md
  - explorations/threads/D-structural-conformal-willmore-functor-scoping-and-first-swing-2026-07-11.md
  - papers/candidates/keep-and-grade-loop-cost/keep-and-grade-loop-cost-2026-07-11.md
  - tests/W46_H57_stage2_fixed_point.py
  - GEOMETER-VS-PHYSICS-OBJECTS.md
scripts:
  - tests/W78_conformal_mode_gauge_status.py
---

# W78 -- Is GU's spin-0 conformal-factor mode physical or a gauge artifact?

**Role.** This settles the single shared residual that H61a showed decides BOTH North Stars: is the wrong-sign
spin-0 mode (`f_0^2/f_2^2 < 0`, `M_0^2 < 0`) on GU's asymptotically-free trajectory a PHYSICAL propagating
degree of freedom, or a gauge/unphysical direction (the classic Gibbons-Hawking-Perry conformal-factor problem)?
Everything else on the shared residual is already in hand: W53 proved the spin-2 grading is PT-unbroken across
the entire interacting regime; this is the last shadow.

I ran the 5-persona team inline (specialist / referee / adversary / cross-checker / synthesizer), one context.

## 0. Construction forks (GEOMETER-VS-PHYSICS-OBJECTS.md), stated

Three load-bearing objects have rival constructions; none is defaulted.

| Object | Construction used | Why |
|---|---|---|
| **Gravity functional** | GU-native **induced `|II|^2`** via Gauss `|II|^2 = |H|^2 - R^X`, which lands in the 4th-order Stelle/agravity class `f_2^2 C^2 + f_0^2 R^2 + (induced Einstein) + (Lambda)` (H49, H57-stage1). NOT a freely chosen `R^2` Lagrangian, and NOT the pure conformal `|H|^2` Willmore. | The gauge-status answer differs between "pure conformally-invariant Willmore" (conformal mode gauge) and "conformal-invariance-broken induced action" (conformal mode physical). We must identify which GU is. |
| **The conformal / spin-0 mode** | the `R^2`-induced spin-0 excitation of the fourth-order propagator (the "scalaron"), NOT the second-order Einstein-Hilbert conformal factor | The gauge/GHP argument attaches to the *second-order* conformal factor; the physical-DOF argument attaches to the *fourth-order* scalaron. Conflating them is the load-bearing trap. |
| **The positivity object / `Delta`** | the PHYSICAL-subspace Krein modular operator `Delta = S^+ S` (H61a), whose PT-(un)brokenness = real-positive spectrum decides both North Stars | The question is whether the spin-0 mode enters this physical `Delta` or is projected out with the gauge modes. |

## 1. Persona 1 -- QG / higher-derivative specialist: DOF/constraint analysis and the gauge determination

### 1.1 What the spin-0 mode is, precisely, in GU

GU's gravity functional is the induced `|II|^2` (fork table, H49), which by the Gauss identity is
`|II|^2 = |H|^2 - R^X`: a conformal-Willmore / Bach-class spin-2 piece (`|H|^2`, fourth-order) **minus the induced
Einstein-Hilbert term `R^X`** (second-order). H49 is decisive on one point: **pure conformal `|H|^2` DIES on the
rotation-curve refutation; GU survives only because the induced action keeps the Einstein term `-R^X`.** In the
fourth-order truncation this reads `f_2^2 C^2 + f_0^2 R^2 + (induced EH) + Lambda` (H57-stage1), and the induced
`f_0^2` is **nonzero with its own beta function** (`beta_{f_0^2} != 0`, marginally relevant, a genuine independent
running coupling; W46 Q4/Q5). The spin-0 mode is the `R^2`-scalaron of this action.

### 1.2 DOF / constraint count (derivation i)

Fourth-order (Stelle) gravity has **8 propagating DOF** = 2 (massless graviton) + 5 (massive spin-2 ghost, from
`C^2`) + **1 (massive spin-0 scalaron, from `R^2`)**. The scalaron is present and propagating **iff the `R^2`
coefficient is nonzero.** Diffeomorphism invariance removes 4+4 of the metric's 10 components; it does **not**
touch the scalaron -- the scalaron survives the full diffeomorphism constraint analysis as a physical DOF (this is
exactly the Starobinsky inflaton for `f_0^2 > 0`).

Contrast the two regimes cleanly:
- **Second-order GR** (`f_0^2 = f_2^2 = 0`): 2 DOF; the conformal factor (trace of `g`) is **non-dynamical**,
  fixed by the Hamiltonian constraint -- constrained/gauge. THIS is the regime where the GHP conformal-factor
  problem lives, and there the wrong-sign direction is genuinely a gauge/contour artifact.
- **Fourth-order with `f_0^2 != 0`** (GU's regime): the `R^2` term **promotes the conformal factor to a
  propagating physical DOF** (the scalaron). This is standard and not in dispute: `R^2` gravity propagates a
  physical scalar.

**GU has `f_0^2 != 0` (computed, with independent running). Therefore the DOF count gives +1 PHYSICAL scalar.**
The mode is NOT constrained like GR's conformal factor.

### 1.3 Gauge determination (derivation ii): Weyl-BRST + the scope of GHP

The only candidate gauge symmetry that could remove a conformal/spin-0 mode is **local Weyl (conformal)
invariance**. Two facts close it:

- **`R^2` is NOT Weyl-invariant in 4D.** Under a local conformal rescaling only `C^2` (Weyl-squared) and the
  Gauss-Bonnet/Euler density are invariant; `R^2` and the Einstein term `-R^X` are not. GU's action contains BOTH
  a nonzero `R^2` AND the induced Einstein term -- so **GU has no exact Weyl gauge symmetry in the spin-0
  sector.** A mode is removable only if it is BRST-exact for an actual gauge symmetry; there is no Weyl BRST
  operator here for the conformal mode to be exact under. **The mode is therefore NOT gauge / NOT s-exact.**
- **GHP contour rotation is out of scope for this mode.** Gibbons-Hawking-Perry rotate the wrong-sign
  *Euclidean kinetic* term of the *second-order* conformal factor -- a choice of integration contour for a
  *non-propagating* direction. GU's pathology is `M_0^2 < 0`: a *tachyonic mass* (a Lorentzian **pole location**
  of a *propagating fourth-order* scalar), not a Euclidean kinetic-sign choice. GHP does not, and cannot, rotate
  away a physical tachyonic pole. So the GHP escape does not apply.

**Both derivations agree: the spin-0 mode is a PROPAGATING PHYSICAL DOF, not gauge.**

### 1.4 The fork-closure by H49 (the decisive, non-obvious point)

The GEOMETER-side hope for a gauge verdict is: "GU's `|II|^2` is the conformally-invariant Willmore energy, so the
conformal mode is Weyl-gauge (Bach annihilates the conformal mode)." **H49 has already closed this escape.** A
conformally-invariant functional (needed to make the conformal mode gauge) is exactly the pure-`|H|^2`/pure-`C^2`
theory that H49 showed **dies on the rotation-curve refutation.** GU survives *only* by keeping the induced
Einstein term `-R^X`, which **breaks** conformal invariance. So:

> GU cannot gauge away the conformal mode without restoring the exact conformal invariance that H49 proved GU must
> break to be viable. "Conformal mode is gauge" and "GU survives rotation curves" are mutually exclusive; H49
> already chose the second. Hence the conformal mode is physical -- and this holds on BOTH fork sides (the
> geometer's induced `|II|^2` and the physics Stelle truncation agree), so it is not a defaulting artifact.

## 2. Persona 2 -- math-physics referee: is "physical" established, or asserted?

- **Rigorous.** (i) DOF count: `R^2 != 0` => +1 propagating scalar is a textbook constraint-analysis result;
  GU's `f_0^2 != 0` is computed (W46). (ii) Weyl non-invariance of `R^2` + induced-EH is elementary and exact.
  (iii) GHP scope (second-order Euclidean kinetic vs fourth-order Lorentzian tachyonic mass) is a clean category
  distinction. (iv) H49 fork-closure is a proven repo result used correctly (viability requires conformal-symmetry
  breaking; symmetry breaking forbids the gauge status). These four independently deliver **NOT gauge**.
- **What is NOT proven / graded down.** The *character* of the physical mode -- positive-norm **tachyon** vs
  **ghost** -- rests on the standard agravity fact that the scalaron is a healthy (positive-norm) scalar and the
  ghost lives only in the spin-2 sector. That is the generic result but is *convention/sign-sensitive* for the
  wrong-sign `f_0^2 < 0`; I grade it PLAUSIBLE and flag the scalaron norm-sign as load-bearing (see 5).
- **Circularity check.** The determination does not assume the conclusion: it grants the strongest gauge case
  (conformal-Willmore / GHP) and defeats it on independent grounds (DOF count, Weyl algebra, H49), rather than
  asserting "physical." Clean.
- **Grade issued.** Gauge status: **NOT gauge -- rigorous** (two derivations + H49). Character (tachyon vs
  ghost): **PLAUSIBLE**. Vacuum resolution: **OPEN**.

## 3. Persona 3 -- adversary (presses the verdict BOTH ways)

**Against "physical" (i.e. for gauge):**
1. *"It's the conformal factor; ordinary GR constrains it away."* -- Defeated by 1.2: that is the *second-order*
   conformal factor. `R^2 != 0` promotes it to a propagating scalaron; the constraint that kills it in GR is
   absent once `f_0^2 != 0`.
2. *"GHP contour rotation handles the wrong sign -- it's not a genuine instability."* -- Defeated by 1.3: GHP
   addresses a Euclidean *kinetic* sign of a *non-propagating* mode; `M_0^2 < 0` is a *mass* sign of a
   *propagating* mode. Different object. The adversary is exactly conflating the two constructions the fork rule
   warns against.
3. *"GU's `|II|^2` is conformally invariant (Willmore/Bach), so the mode is Weyl-gauge."* -- Defeated by 1.4
   (H49): conformal invariance is precisely what GU must break to survive.

**Against "gauge" (i.e. for physical) -- the adversary's strongest, and it LANDS:** *"The fourth-order `R^2` mode
IS a physical propagating scalar unlike GR's constrained conformal factor -- you cannot gauge it away."* Correct.
This is the specialist's own conclusion. The adversary's pressure here is *sustained*, not defeated: the mode is
physical.

**But the adversary over-reaches when it says "physical => fatal PT-broken no-go, done."** A physical *tachyon* is
not a physical *ghost*. `M_0^2 < 0` with **positive norm** signals an unstable *vacuum* (the scalaron rolls), not
a negative-norm state. Tachyonic instabilities are standardly resolved by expanding around the true vacuum
(Higgs/Coleman-Weinberg/tachyon-condensation), where `M_0^2 > 0` and the spectrum is real. So "physical" forces a
*conditional*, not an automatic kill -- the residual moves to vacuum selection.

## 4. Persona 4 -- cross-checker: second derivation + GHP/agravity literature

- **Independent DOF cross-check (Ostrogradsky/Stelle spectrum).** The fourth-order propagator
  `1/(p^2(p^2 - m_2^2))` (spin-2) plus the `R^2`-induced `1/(p^2 - M_0^2)` (spin-0) each carry a genuine pole.
  A pole = a propagating asymptotic state. The spin-0 pole exists iff `f_0^2 != 0`. This reproduces 1.2 from the
  propagator side rather than the constraint side -- two derivations, same conclusion (the discipline that caught
  the `M^2/r^2` bug). **Agree: physical.**
- **Literature (read-only, from stored knowledge; no external write).** (a) GHP 1978: the conformal-factor
  wrong-sign is the *second-order* Euclidean action; the standard resolution is contour rotation of a
  *gauge/unphysical* direction -- explicitly a second-order statement. (b) Agravity (Salvio-Strumia 2014): the
  `R^2` scalaron is a *physical* scalar (a candidate inflaton), and its non-tachyonic requirement is `f_0^2 > 0`;
  the ghost is *only* the spin-2 mode. So `f_0^2 < 0` => tachyonic *scalaron*, positive-norm -- exactly this
  work's reading. (c) Starobinsky `R^2` inflation: the scalaron is uncontroversially a physical propagating DOF.
  The literature is unanimous that the *fourth-order `R^2`* mode is physical (unlike the *second-order* conformal
  factor). The contested part in the literature is causality/locality of the *ghost*, not the reality of the
  scalaron. **This confirms: the "it's just the gauge conformal-factor problem" defense is a category error.**

## 5. Persona 5 -- synthesizer: verdict, the split, the load-bearing assumption

**VERDICT: PHYSICAL (not gauge) -- and because the physical mode is a positive-norm TACHYON rather than a ghost,
the naive "both North Stars close / both no-go" binary is REFINED into a SPLIT, leaving a CONDITIONAL that turns
on GU's vacuum, not on gauge status.**

**Gauge status (settled).** The spin-0 mode is a genuine propagating physical DOF (the `R^2` scalaron). Both
independent derivations agree it is NOT gauge: (i) DOF/constraint count -- `f_0^2 != 0` gives +1 propagating
scalar, not GR's constrained conformal factor; (ii) Weyl-BRST + GHP-scope -- no exact Weyl symmetry (so not
s-exact), and GHP contour rotation addresses only the second-order Euclidean kinetic conformal factor, not a
fourth-order tachyonic pole. The gauge escape is additionally **closed by H49**: conformal invariance (which
alone could make the mode gauge) is exactly what GU must break to survive rotation curves. Two derivations agree;
the fork does not rescue "gauge."

**Consequence for the physical Krein `Delta = S^+ S`.** Because the mode is physical, it **enters** the
physical-subspace `Delta` (it is not projected out with the gauge modes). Its contribution is:
- **norm:** positive (scalaron is a healthy scalar; ghost is only spin-2) -> does **NOT** make the inner product
  indefinite;
- **spectrum:** `M_0^2 < 0` -> imaginary frequencies for soft modes -> **non-real** -> **PT-broken** in the
  spin-0 sector, around the flat (`R = 0`) vacuum.

**The split (contra the H61a binary, and more honest than it).** "PT-unbroken" bundles two requirements that the
tachyon separates:
- **GU's UV loop-POSITIVITY North Star** needs a **positive inner product** (norm). The spin-0 tachyon is
  positive-norm, so it does **not** obstruct it; the spin-2 sector is PT-unbroken across the interacting regime
  (W53). => **Loop-positivity plausibly CLOSES on the physical sector** (conditional only on the scalaron being
  genuinely positive-norm, not a ghost-tachyon).
- **The observer conjecture's Krein-TT North Star** needs **real-positive `Delta` spectrum** (stability). The
  physical tachyon gives imaginary modular spectrum => **PT-broken around flat space** => Krein-TT **obstructed
  there**. The obstruction lifts **iff** GU's true vacuum is non-tachyonic (`M_0^2 > 0`), an **uncomputed
  vacuum-selection** question (GU's flow carries a free relevant `Lambda`; a constant-curvature/de Sitter true
  vacuum could restore `M_0^2 > 0`).

So the shared residual does **not** collapse to a single clean "both close" or "both no-go." It **splits**: the
positivity leg is in good shape; the stability/Krein-TT leg is obstructed at the flat vacuum and conditional on a
non-tachyonic true vacuum.

**Load-bearing assumptions (named).**
1. **The `R^2` scalaron is positive-norm (a tachyon, not a ghost).** Standard agravity: the ghost is the spin-2
   mode; the scalaron is a healthy scalar whose `f_0^2 < 0` makes it *tachyonic* (mass), not *ghostly* (norm). If
   instead GU's `|II|^2` sign structure makes the spin-0 mode a **ghost-tachyon** (negative norm AND `M^2 < 0`),
   then it breaks loop-positivity too and BOTH North Stars go no-go together. This norm-sign is the single fact
   that decides whether the two legs split or fall together.
2. **The truncation.** GU's induced `|II|^2` is treated in the fourth-order Stelle/agravity class it lands in
   (H49, H57-stage1); the ported one-loop betas (W45-47) fix `f_0^2 < 0` on the AF trajectory.

**Confidence.** Gauge status NOT-gauge: **rigorous** within the truncation (two derivations + H49 fork-closure;
literature-unanimous that the fourth-order `R^2` mode is physical). Tachyon-not-ghost character: **PLAUSIBLE**
(standard agravity; norm-sign load-bearing). Vacuum resolution of the Krein-TT leg: **OPEN**.

## 6. What this does and does not do

**Does:** settles the physical-vs-gauge status of the decisive shared residual -- **PHYSICAL, not gauge**, two
independent ways, with the gauge escape closed by H49; and shows the mode is a positive-norm **tachyon**, which
**splits** the two North Stars (positivity leg plausibly closes; Krein-TT leg conditional on GU's vacuum) rather
than deciding both identically.

**Does NOT:** compute a GU/Stelle loop amplitude; compute GU's true vacuum (the open residual); prove the
scalaron's norm-sign from the `|II|^2` sign structure (assumed standard, flagged load-bearing); change `CANON.md`,
`RESEARCH-STATUS.md`, `claim-status`, verdicts, or public posture. H59/H61a remain **OPEN**.

## 7. Next valid swing

1. **Decide the norm-sign of the `R^2` scalaron directly from GU's `|II|^2` sign structure** (`|II|^2 = |H|^2 -
   R^X`, Gauss). This is the single fact that decides whether the two North Stars split (tachyon: positivity
   survives) or fall together (ghost-tachyon: both no-go).
2. **Compute GU's true vacuum.** Does the free relevant `Lambda` + the scalaron potential admit a stable
   constant-curvature vacuum on which `M_0^2 > 0`? If yes, the Krein-TT leg's flat-space obstruction lifts and
   BOTH North Stars close on the physical sector around the true vacuum. If no stable vacuum exists, it is the
   program's first genuine no-go, cleanly located at the scalaron potential.
</content>
</invoke>
