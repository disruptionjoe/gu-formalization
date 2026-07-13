---
title: "path5 Branch E -- the self-dual-square / color-kinematics / Willmore FALSIFIER (does the ARENA force a VALUE?)"
status: exploration
doc_type: research_note
branch: "path5-E (falsifier, PRESENT-not-DECIDE, run BLIND to branches A-D)"
role: "adversary against the conjecture 'values unforceable in principle'; try to force a genuine VALUE from the arena"
updated_at: "2026-07-11"
verdict: "NO falsification survives. Every arena-forcing on the board reduces to a dimensionless RATIO / a direction-up-to-scale / a UV-asymptotic limit / a discrete ARENA -- never a genuine dimensionful VALUE and never the 3-over-1 selection. Overall: STRONG CORROBORATION of in-principle-unforceability. Honest caveat: the arena/value split is partly self-sealing (see Persona 3), so the corroboration is genuine but its robustness is partly definitional. I PRESENT; I do not render the verdict."
test: "tests/W71_path5_E_falsifier.py (deterministic, exit 0)"
depends_on:
  - "explorations/wave27/H48-self-dual-square-forcing-2026-07-11.md"
  - "explorations/H57-flow-stage2-fixed-point-critical-surface-2026-07-11.md"
  - "explorations/H60-firm-asymptotic-freedom-2026-07-11.md"
  - "explorations/CONJECTURE-source-action-is-the-observer-2026-07-11.md (falsifier description only, sec 7)"
  - "GEOMETER-VS-PHYSICS-OBJECTS.md (fork rule; mu_DW ratio-only row)"
---

# path5 Branch E -- the self-dual-square / color-kinematics / Willmore FALSIFIER

## The charge

The conjecture (`CONJECTURE-source-action-is-the-observer`) claims physical VALUES are
**unforceable in principle**: the source action is the observer, so forcing a value = forcing the
observer = a category error. The geometry forces the **ARENA** (the admissibility structure -- Krein
UV, 3-primary count arena, 4th-order graviton, forced dimensionless ratios), **never the VALUE** (the
scale mu_DW, the 3-over-1 count selection, DE magnitude). The conjecture names its own kill switch:
the **self-dual-square / color-kinematics / Willmore forcing** -- if the arena forces the count/norm
onto a specific value with no observer/selection input, in-principle-unforceability is FALSE.

**My job (Branch E): prosecute HARD that the ARENA DOES FORCE A VALUE.** I present the strongest case
per candidate, tagged DECISIVE / STRONG / WEAK, with the honest steelman rebuttal. I do NOT render the
final verdict -- the orchestrator weighs this against the constructive legs.

**The dividing line I hold myself to** (the only line that makes the test non-trivial): a genuine
**VALUE** is (a) a **dimensionful / scale-carrying** quantity requiring a ruler to state, OR (b) a
**discrete selection WITHIN a forced discrete arena** (e.g. 3 out of the forced set {1,3}). An
**ARENA / RATIO** is a forced **dimensionless** number, a **direction/shape up to scale**, an operator
identity, a **UV-asymptotic limit**, or the **discrete set itself** (not the pick inside it). The
conjecture explicitly concedes that dimensionless ratios are forced (mu_DW row, H24: "geometry fixes
only dimensionless ratios, overall scale structurally free") -- so a forced ratio is NOT a
counterexample; it IS the arena. To falsify I must force a **dimensionful value** or a **discrete
selection**.

Construction fork used throughout (GEOMETER-VS-PHYSICS-OBJECTS): the gravity functional is the
program-native induced `|II|^2` (not a freely chosen `R^2`); `mu_DW` is the program-native ratio-only
free scale (not a mass to measure). I attack the CLAIM (values unforceable), staying on the native
side where the conjecture actually lives.

---

## PERSONA 1 -- the FORCING specialist (builds the strongest case the arena forces a value)

### Candidate A -- self-dual color-kinematics forces the COUNT onto carrier B
Requiring gravity = (self-dual gauge)^2 imposes the kinematic-Jacobi (color-kinematics) constraint.
If that constraint closes ONLY on carrier B's gamma-trace-constrained field space (index-changing,
the count-carrier), the arena would force the count-carrier -- a discrete value -- in one stroke.
**Strongest framing:** the self-dual `su(2)_+` algebra on `Lambda^2_+` closes with Jacobiator exactly
zero AND preserves `ker Gamma` (carrier B): `||Gamma J_i Pi_RS|| = 8e-15` on the verified Cl(9,5) rep.
So the kinematic algebra "picks B."

### Candidate B -- Willmore/conformal uniqueness forces the NORM to a unique value
The IG-invariant quadratic functionals of the soldering distortion are exactly two (`|II|^2`, `|H|^2`);
conformal-weight covariance imposes one linear constraint (`beta = -1/4 alpha`); admissible dimension
`= 2 - 1 = 1`. **The functional is UNIQUE** -- the same universal property that forces Bach as the
unique conformal 4-derivative curvature functional. **Strongest framing:** the arena (conformal
geometry of the `X^4 -> Y^14` embedding) forces the action to the pure-Bach `|II_0|^2` norm -- a
specific norm = a specific value the geometry hands you with no observer input.

### Candidate C -- asymptotic freedom PREDICTS f_2 (the strongest determination on the board)
H57/H60: the induced 4th-order graviton has `beta_{f_2^2} = -kappa x^2 b_2` with
`b_2 = 133/10 + c_RS_weyl > 0` across the entire tightened band `[1.02,1.82]`. So `f_2^2` is
**asymptotically free -> fixed to 0 in the UV -> marginally irrelevant -> PREDICTED**, removing it as a
free parameter: the critical surface drops from `{M_Pl, Lambda, f_0^2, f_2^2}` to `{M_Pl, Lambda,
f_0^2}`. **Strongest framing:** the arena (the graviton's own beta function, no observer) forces the
coupling `f_2` onto the specific value `0`. That is the arena forcing a value = falsification.

### Candidate D -- forced dimensionless constants (the operator-identity route)
`box^2 = -4 Bach` (H1, machine-checked) forces the specific number `-4`; the conformal weight is forced
to `4`; the Willmore constraint forces `-1/4`. **Strongest framing:** these are specific numbers the
arena forces with no observer -- values.

---

## PERSONA 2 -- the MATH REFEREE (grades each; checks it is a genuine VALUE, not an arena/ratio)

- **Candidate A (count -> B): WEAK as a forcing, and it forces NOTHING discriminating.** H48 Q2 is a
  clean H20-style negative: the self-dual algebra closes on **BOTH** A and B because `Gamma` is an
  `so(9,5)`-EQUIVARIANT intertwiner (`Gamma J_i = sigma_i Gamma`) and `ker Gamma` is an
  `so(9,5)`-subrep -- but so is the full field space, so `J_i` preserves it too. The kinematic algebra
  is **carrier-BLIND**; the A/B bit is the downstream INDEX (`-42` vs `-38`), which kinematic-Jacobi
  does not see. So it does not force even the *arena's* A/B bit, let alone a value. **Not a value
  forcing.**
- **Candidate B (norm): STRONG as a forcing, but the forced object is a RATIO/DIRECTION, not a value.**
  The 1-dimensionality is real (genuine universal property). But "forced up to scale" = a forced
  **direction** in the 2-dim functional space = the forced dimensionless **ratio** `beta/alpha = -1/4`.
  The overall **scale is free** (mu_DW, the observer's ruler). And it is **conditional** on granting
  conformal invariance (proven only linearized on the spin-2 sector) and forces `|II_0|^2`, not GU's
  `|II|^2`. What the arena forces here is a dimensionless ratio + a shape -- **arena, by the
  conjecture's own taxonomy. Not a value forcing.**
- **Candidate C (f_2): STRONG as a determination, but f_2 is DIMENSIONLESS and the forced content is a
  UV limit + a fixed ratio.** `f_2` is a dimensionless coupling; "`f_2 -> 0`" is a **UV-asymptotic**
  statement, not a value at any physical scale. The genuine physical invariant is the **fixed ratio**
  `r* = f_0^2/f_2^2` (negative); the dimensionful predictions still need `mu_DW = M_Pl` (observer-set).
  "`f_2` predicted" = "one fewer free parameter / the coupling is irrelevant" = a **predictivity/arena**
  statement. **Not a dimensionful value forcing.**
- **Candidate D (constants -1/4, -4, 4): these are dimensionless operator-identity/shape numbers =
  arena by definition.** `-4` is a fixed coefficient of an operator identity; `4` is fixed by
  dimensional analysis; `-1/4` is Candidate B's ratio. None is a scale-carrying value or a discrete
  selection. **Not value forcings.**

**Referee tally:** the strongest *forcing* is Candidate B (STRONG) and the strongest *determination* is
Candidate C (STRONG); Candidate A is WEAK (forces nothing), D is arena-by-definition. **None forces a
genuine VALUE** on the dividing line above.

---

## PERSONA 3 -- the STEELMAN-OF-THE-CONJECTURE (argues each apparent forcing is arena/ratio, value free)

- **On B:** "Forced up to scale" is the tell. The geometry forces the **ratio** `-1/4` and the
  **direction** `|II_0|^2`; the scale -- the one thing you would measure -- is exactly `mu_DW`, which
  H24 proves is structurally free. This is the arena/value split made explicit: shape forced, scale
  free. Not a counterexample; a confirmation.
- **On C:** `f_2` is a **dimensionless running coupling**. AF says it flows to zero in the UV and the
  physical UV variable is the **ratio** `r*` -- both dimensionless, both arena. The observer still sets
  `mu_DW`; where on the trajectory "you" sit (hence the finite-scale value of `f_2`) is observer-fixed.
  "Predicted" means "not an independent knob," which is a statement about the **arena's dimension**, not
  a measured value. Confirmation.
- **On A:** the arena does not even force the discrete A/B bit; the count selection 3-over-1 remains
  exactly the free value path 3 left. Strong confirmation.
- **On D:** dimensionless structural constants are the definition of the arena.

- **BUT the steelman must also keep ME honest about the conjecture's weakness:** the arena/value split
  is at some risk of being **self-sealing**. It classifies *forced* things as "arena" and *unforced*
  things as "value," so any forcing can be reabsorbed as "arena." The split is only non-trivial because
  it names, in advance, two concrete events that WOULD break it: (i) the arena forcing a **dimensionful**
  quantity, or (ii) the arena forcing the **3-over-1 selection**. Those events are what Branch E hunts.
  They demonstrably do not occur in A-D -- so the corroboration is **genuine**, but part of its
  robustness is definitional, and the orchestrator should weight it as such.

---

## PERSONA 4 -- the CROSS-CHECKER (verifies against the actual prior results)

- **B against H48:** matches. H48 Q1: coeff count 2, constraint count 1, dim admissible 1, forces the
  traceless conformal `|II_0|^2` "up to scale," conditional on the conformal grant; the two honest
  caveats (a) target-revising, (b) conditional are quoted verbatim. Cross-check PASSES.
- **A against H48:** matches. H48 Q2: `||Jacobiator|| = 0`, `dim Lambda^2_+ = 3`,
  `||Gamma J_i Pi_RS|| ~ 8e-15`, `rank Pi_RS = 1664`, closes on BOTH A and B, "removes 0 of the K-class
  A/B bit," RELABELS. Cross-check PASSES.
- **C against H57/H60:** matches. H57 Stage 2: `f_2^2` marginally irrelevant, "no (predicted)", the UV
  variable is the ratio `r = f_0^2/f_2^2`, both fixed ratios negative. H60: `b_2 = 133/10 + c_RS_weyl`,
  band `[1.02,1.82]`, homogeneous-quadratic -> the physical objects are fixed **ratios** (rays), "never
  an isolated interacting fixed point," and `M_Pl(=mu_DW)` is "the ratio-only free scale." The
  homogeneity lever is itself the statement that only **ratios** are pinned. Cross-check PASSES and, if
  anything, STRENGTHENS the steelman (H60 says explicitly the forced objects are ratios/rays).
- **Taxonomy against GEOMETER table:** the mu_DW row ("scale-covariant geometry fixes only DIMENSIONLESS
  RATIOS, overall scale STRUCTURALLY free") is exactly the arena/value dividing line. Consistent.

No prior result contradicts the referee/steelman reading. No result on the board forces a dimensionful
value or the 3-over-1 selection.

---

## PERSONA 5 -- the SYNTHESIZER (per candidate: strongest case + honest strength + value or arena?)

| Candidate | Strongest forcing case | Prosecution strength | Steelman rebuttal | Genuine VALUE forced? |
|---|---|---|---|---|
| **A. color-kinematics -> carrier B (count)** | self-dual `su(2)_+` closes (Jacobiator 0) AND preserves `ker Gamma` (carrier B) | **WEAK** | `so(9,5)`-equivariant => closes on BOTH A and B; carrier-blind; A/B bit is downstream index | **NO** -- forces nothing, not even the arena's A/B bit |
| **B. Willmore/conformal uniqueness -> norm** | unique 1-dim functional `|II_0|^2` (universal property, like Bach) | **STRONG** (as a forcing) | forced only **up to scale** = the dimensionless ratio `-1/4` + a direction; scale (mu_DW) free; conditional on conformal grant; forces `|II_0|^2` not `|II|^2` | **NO** -- forces a RATIO/direction (arena), scale free |
| **C. AF -> f_2 predicted** | beta forces `f_2 -> 0`, removes a free parameter | **STRONG** (as a determination) | `f_2` dimensionless; `->0` is a UV-asymptotic limit; physical invariant is the fixed **ratio** `r*`; scale mu_DW observer-set; "predicted" = arena-dimension statement | **NO** -- arena/ratio, scale observer-set |
| **D. forced constants (-1/4, -4, 4)** | specific numbers forced with no observer | **arena-by-def** | dimensionless operator-identity / shape / dimensional-analysis numbers | **NO** -- arena by definition |

**No row forces a genuine VALUE.** The two events that would falsify -- (i) the arena forcing a
dimensionful quantity, (ii) the arena forcing the 3-over-1 selection -- do not occur. Everything forced
is a dimensionless ratio, a direction-up-to-scale, a UV-asymptotic limit, an operator-identity constant,
or a discrete ARENA (never the selection inside it). The scale `mu_DW` and the 3-over-1 pick -- the two
genuine "values" -- stay unforced.

---

## OVERALL ASSESSMENT (Branch E presents; does not decide)

**No arena-forcing of a genuine VALUE survives.** The prosecution's two strongest cases (B: Willmore
uniqueness; C: f_2 predicted) are real *forcings/determinations* but both land on the **ratio/arena**
side of the conjecture's own dividing line: B forces a dimensionless ratio + a shape up to a free scale;
C forces a dimensionless coupling's UV limit + a fixed ratio, scale still observer-set. Candidate A
forces nothing discriminating (the named kill switch RELABELS -- closes on both carriers). Candidate D
is arena by definition.

**Therefore this is STRONG CORROBORATION of in-principle-unforceability**, not a falsification. The
pattern is uniform and matches the conjecture's prediction exactly: the arena is richly forced (ratios,
directions, UV limits, discrete arenas), the VALUE (scale, discrete selection) is never forced.

**The one honest deduction I flag for the orchestrator (Persona 3):** the corroboration is genuine
because the two pre-named falsifying events demonstrably do not occur -- but the arena/value split is
partly **self-sealing** (it reclassifies forced things as arena), so the *robustness* of the
corroboration is partly definitional rather than empirical. A future genuine kill would need the arena
to force a **dimensionful** value or the **3-over-1 selection**; nothing on the current board does.

**Strength tag on the falsification attempt: it FAILS. Best forcing (B) is STRONG but forces an
arena/ratio, not a value. I present this; the verdict is the orchestrator's.**

*Reproducible: `python tests/W71_path5_E_falsifier.py` (deterministic, exit 0). Exploration-grade; not
promoted; no canon/verdict/claim-status file touched; no git commit (orchestrator verifies).*
