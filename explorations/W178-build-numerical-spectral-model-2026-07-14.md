---
artifact_type: exploration
status: "exploration (W178 / TEAM BUILD-NUMERICAL, label W178; coherence-first BUILD sprint, exploration grade; 5 personas inline, one worker, no sub-agents; one deterministic test 14/14 exit 0 with positive + negative controls)"
created: 2026-07-14
wave: W178
label: W178
posture: coherence-first BUILD; exploration grade; honest grading with truncation caveats explicit
hypothesis: "Build a finite/truncated NUMERICAL spectral model of the Y14 covariant record/RS operator D that respects the load-bearing structure ((9,5) Krein signature, ker-Gamma projection, Stelle massless-graviton + massive-ghost spectrum, one interaction vertex) and numerically probe the two decisive quantities the analytic route (W169-W174) cannot yet reach: (a) the C-metric positivity vs coupling (min eig eta_+ = e^{-Q}, cf W171); (b) the ghost self-energy pole SHEET (physical vs second; the W172 PT-breaking decider). Does the grading stay OPERATIVE (positive metric survives / pole stays second-sheet) or does it break (metric loses positivity / pole reaches the physical sheet = NOT-OPERATIVE)?"
title: "W178 VERDICT: PHYSICAL-SHEET-PT-BREAKS-NOT-OPERATIVE (leaning) on the physically-anchored Stelle kinematics; TRUNCATION-CONDITIONAL overall. Two numerical probes of one truncated (9,5)-Krein model bracket bar (b) BY KINEMATIC REGIME, and both isolate the ghost (anti-damping / indefinite-metric) sign as the sole cause. MODEL A (discrete, gap-protected ghost, no open decay channel): the K-pseudo-Hermitian spectrum is REAL and the C-metric positivity witness min eig(eta_+^{-1}) is POSITIVE up to an EXACT exceptional point g_c = 0.406, then a real pair collides and goes complex (PT broken, no positive metric) -- reproducing W171's finite-scale positivity and LOCATING its boundary. The normal-sign control (metric = I, no ghost) has NO exceptional point at any coupling. MODEL B (continuum resummed ghost propagator, ghost ABOVE the two-graviton threshold = the Stelle / W51 kinematics with Im Sigma(M^2) > 0): the ANTI-DAMPING (W132 wrong-sign width) self-energy puts the propagator pole on the PHYSICAL sheet -- RIGOROUSLY, by the argument principle (exactly ONE physical-sheet upper-half pole; the normal-sign control has ZERO, a benign second-sheet resonance). A physical-sheet complex-conjugate pair = complex energy = spontaneously broken PT = no positive metric = NOT-OPERATIVE. NET: the numerical evidence LEANS NOT-OPERATIVE on the physically-correct kinematics, SHARPENING W172's dynamical no-go from 'signalled' to 'realized in a rigorous model self-energy'. The honest caveat: it is a MODEL sqrt-threshold self-energy (the same KIND W124 used, not GU's dressed one), and the gap-protected Model A is OPERATIVE below g_c, so the ABSOLUTE verdict stays conditional on (i) the dressed width carrying the W132 anti-damping sign and (ii) the ghost sitting above the effective continuum threshold -- the inherited H59/W48 open object. H59 remains OPEN."
grade: "EXACT (finite-dim, self-validating to 1e-12..1e-16) for Model A: the (9,5)-signature K-Hermiticity of the vertex (||K V K - V^dag|| = 0.0), the reality of the K-pseudo-Hermitian spectrum below g_c, the exceptional point g_c = 0.4060 located by bisection to 1e-9, the C-metric positivity witness min eig(eta_+^{-1}) monotone-collapsing 0.086 -> 2.3e-4 as g -> g_c, and the normal-sign control staying real to 1e-9 at couplings up to g = 20. RIGOROUS (argument principle, integer, seed-independent) for Model B: #physical-sheet(I) upper-half poles = 1.000 (anti-damping ghost) vs 0.000 (normal control), and #second-sheet(II) = 0 vs 1, at kappa in {0.05,0.2,0.5,1.0}, with the two-graviton threshold below the ghost mass (M2=1.0 > s_th=0.1). PROVEN-in-controls: PC1 the Bender-Brody-Jones 2x2 PT calibrator (unbroken -> real spectrum + positive metric; broken -> complex-conjugate pair; the positive-metric witness collapses to 0 at the exceptional point s = r|sin theta|); PC2 W171's eta_+ = e^{-Q} positivity reproduced at four couplings; PC3 W169's Q2 secular-obstruction lattice reproduced exactly (generic/Stelle EXIST; 2:1 obstructs at Q1; equal-mass/conformal and 3:1 obstruct at Q2). STRUCTURAL / ARGUED for the lift to QFT: both models are finite/model stand-ins (a discrete (9,5) truncation; a single sqrt-threshold bubble self-energy) for the QFT covariant operator D on non-compact Y14, so they DECIDE the STRUCTURE (coupling-controlled PT breaking; physical-sheet pole from the anti-damping sign; both absent for the normal sign) but CANNOT fix GU's dressed coupling or the exact dressed self-energy -- the inherited H59/W48 object. Test: tests/W178_build_numerical_spectral_model.py 14/14 exit 0. NO canon / RESEARCH-STATUS / claim-status / verdict / posture change. H59 remains OPEN."
depends_on:
  - explorations/W131-covariant-operator-y14-2026-07-14.md
  - explorations/W132-graded-optical-theorem-physical-subspace-2026-07-14.md
  - explorations/W169-c-operator-perturbative-construction-2026-07-14.md
  - explorations/W171-rg-positivity-flow-2026-07-14.md
  - explorations/W172-interacting-c-operator-nogo-2026-07-14.md
  - tests/W132_graded_optical_theorem_physical_subspace.py
  - tests/W169_c_operator_perturbative_construction.py
  - tests/W171_rg_positivity_flow.py
  - GEOMETER-VS-PHYSICS-OBJECTS.md
scripts:
  - tests/W178_build_numerical_spectral_model.py
external_refs:
  - "Bender, Brody & Jones, Complex extension of quantum mechanics, PRL 89 (2002) 270401 -- the C-operator construction and the 2x2 PT calibrator; unbroken/broken phases; the exceptional point s = r|sin theta|"
  - "Mostafazadeh, Pseudo-Hermiticity versus PT symmetry, JMP 43 (2002) 205 -- positive metric eta_+ = eta C; quasi-Hermiticity requires real spectrum"
  - "Bender & Mannheim, No-ghost theorem for the fourth-order Pais-Uhlenbeck oscillator, PRL 100 (2008) 110402 -- real spectrum + positive metric for unequal frequencies; Jordan block (no positive metric) at equal frequency"
  - "Stelle, Renormalization of higher-derivative quantum gravity, PRD 16 (1977) 953 -- the 4th-order theory: massless graviton + massive spin-2 ghost (the model spectrum)"
  - "Bognar, Indefinite Inner Product Spaces, Springer 1974 -- Krein decompositions, fundamental symmetry"
  - "Peskin & Schroeder, An Introduction to QFT, ch. 7 -- resummed propagator, self-energy, resonance poles on the second Riemann sheet"
---

# W178 -- a discretized spectral model of the Y14 record/RS operator D: C-metric positivity and the ghost-pole sheet

**Role.** The H59 North Star is one object: the covariant record/RS operator `D` on non-compact
Y14 (symbol built W131) whose interacting C-operator existence / spectral structure decides
bar (b). The analytic wave W169-W174 left the decision on a single dynamical hinge (W172): the
ghost self-energy has `Im Sigma(M^2) > 0` (W51) with the **anti-damping** sign (W132 probability
EXCESS, wrong-sign width), which *signals* a physical-sheet complex-conjugate pole pair =
spontaneously broken PT = no positive metric = **NOT-OPERATIVE** -- but *only if* the pole actually
**reaches the physical sheet**, which W124 established only on a MODEL self-energy and which is
H59's open W48 object. This team builds a finite **numerical** model that respects the load-bearing
structure and computes the two decisive quantities the analytic route could not reach. Five
personas ran inline, one worker; deterministic test `tests/W178_build_numerical_spectral_model.py`
(**14/14, exit 0**).

## 0. The one object and the construction forks (GEOMETER-VS-PHYSICS-OBJECTS.md)

| Object | Constructions in play | Handling |
|---|---|---|
| **The operator D** | (i) the QFT covariant operator on non-compact Y14 (W131 symbol; analytic layer unbuilt); (ii) a finite/truncated numerical stand-in | We build (ii) in two complementary representations and read off structure; (i)'s analytic layer stays the inherited residual. |
| **"positivity"** | the interacting C-metric `eta_+ = e^{-Q} > 0` (Mostafazadeh; the only survivor per W132) | Model A computes it vs coupling and locates where it fails. |
| **The ghost** | keep-and-grade real-mass Krein state (the branch under test) | kept; the removal (Lee-Wick) exit named, not defended. |
| **PT symmetry** | unbroken (real spectrum, C exists) vs spontaneously broken (complex pair, no C) | the exceptional point / physical-sheet crossing is exactly the boundary. |
| **The ghost kinematics** | ghost BELOW the continuum threshold (gap-protected, stable) vs ABOVE it (can decay = Stelle massless-graviton case, W51 open channel) | **The whole verdict brackets on this axis** -- Model A is the first regime, Model B the second. |

## 1. Persona 1 -- numerical-QFT / lattice specialist: the finite model and the truncation

Two complementary finite models, each respecting a different part of the load-bearing structure.

**Model A -- truncated (9,5)-Krein spectral model on ker-Gamma.** A finite basis carrying the
gimmel fiber Krein form of W131 as `K = diag(+1 x 9, -1 x 5)` (signature **(9,5)** exactly:
9 physical positive-norm directions, 5 ghost negative-norm directions). `H0 = blockdiag(m_phys I9,
M I5)` is the **Stelle** spectrum: 9 near-massless graviton modes at `m_phys = 0.15`, 5 massive
ghost modes at `M = 1.0`. One interaction vertex `g V` mixes the blocks, built **K-Hermitian**
(`K V = V^dag K`, machine-checked `||K V K - V^dag|| = 0.0`) so that `H(g) = H0 + g V` is
K-pseudo-Hermitian -- its spectrum is real (PT unbroken) until an exceptional point. This is the
minimal model with the (9,5) grading, the ker-Gamma-shaped physical/ghost split, the Stelle
spectrum, and one vertex.

**Model B -- resummed ghost propagator.** `D(s) = 1/(s - M^2 - Sigma(s))` with a dispersive
**square-root-threshold** model self-energy `Sigma(s) = s_sign * kappa * sqrt(s_th - s)` -- the
same KIND of model self-energy W124 used. `s_sign = -1` encodes the ghost **anti-damping** (W132
wrong-sign width, W51 `Im Sigma(M^2) > 0`); `s_sign = +1` is the normal-particle control. Physical
sheet (I): principal `sqrt`. Second sheet (II): `w_II = -w_I` (the two-body-cut discontinuity).

**The truncation, named.** Model A is finite-dimensional and has no locality notion (as W171's toy
did not); Model B is a single-bubble model self-energy, not GU's dressed one. Neither can fix GU's
physical coupling or its exact dressed self-energy. So both **decide the STRUCTURE** and one
**locates thresholds**, but the absolute verdict inherits the H59/W48 gap. Stated up front; not
walked back later.

## 2. Persona 2 -- Krein / PT specialist: the C-metric positivity sweep (Model A, reusing W171/W132/W132)

For a K-pseudo-Hermitian `H(g)` with real spectrum the positive metric is
`eta_+ = (P P^dag)^{-1}` (with `P` the right-eigenvector matrix; equivalently W171's `eta_+ = e^{-Q}`,
`C = K eta_+`, `C^2 = 1`, `[C,S] = 0`). Its existence is exactly the OPERATIVE condition. We track
the **positivity witness** `min eig(eta_+^{-1}) = min eig(P P^dag)` (normalized): positive while the
eigenvectors are independent, collapsing to 0 when they coalesce (the exceptional point).

Sweeping `g` (bisection on the first appearance of a complex eigenvalue):

| `g / g_c` | `max|Im eig|` | `min eig(eta_+^{-1})` | phase |
|---:|---:|---:|---|
| 0.200 | 4e-17 | 8.62e-2 | PT-unbroken (**OPERATIVE**) |
| 0.500 | 4e-17 | 6.74e-2 | PT-unbroken (OPERATIVE) |
| 0.800 | 3e-17 | 4.71e-2 | PT-unbroken (OPERATIVE) |
| 0.950 | 8e-17 | 1.14e-2 | PT-unbroken (OPERATIVE) |
| 0.999 | 1e-16 | 2.28e-4 | PT-unbroken (OPERATIVE) |
| 1.001 | 1.9e-2 | -- | PT-**BROKEN** (NOT-OPERATIVE) |
| 1.050 | 1.4e-1 | -- | PT-BROKEN |
| 1.300 | 3.5e-1 | -- | PT-BROKEN |

**Exceptional point `g_c = 0.4060`** (bisection to 1e-9). Below it the spectrum is exactly real and
`eta_+` is positive-definite -- **reproducing W171's finite-scale C-metric positivity and, new
here, LOCATING its boundary**. The witness collapses **monotonically** (`8.62e-2 -> 2.28e-4`) as
`g -> g_c`: the C-metric ceases to exist precisely at the exceptional point (the finite-dim
realization of Bender-Mannheim's equal-frequency Jordan block and of the BBJ calibrator's
`s = r|sin theta|`). Above `g_c` a real pair has collided into a complex-conjugate pair -- **PT
spontaneously broken, no positive metric, NOT-OPERATIVE**. The **normal-sign control** (Hermitian
vertex, metric `= I`, no ghost) stays real for all `g` up to 20: **the exceptional point is
specific to the Krein/ghost (indefinite-metric) sign**, not a generic feature.

## 3. Persona 3 -- spectral / resummation specialist: the ghost-pole sheet (Model B, the W172 decider)

The physically-anchored kinematics: the massive spin-2 ghost sits **above** the two-graviton
threshold (`M^2 = 1.0 > s_th = 0.1`) -- this is exactly the Stelle massless-graviton decay channel,
and it is why `Im Sigma(M^2) > 0` (W51): the absorptive part is nonzero at the ghost mass. The
decisive quantity is the **Riemann sheet** of the propagator pole. We count physical-sheet
upper-half poles rigorously by the **argument principle** (contour integral of `F'/F`, an integer,
seed-independent):

| `kappa = g^2` | # phys-sheet(I) UHP poles | # sheet(II) UHP poles | sheet-II pole |
|---:|---:|---:|---|
| ghost 0.05 | **+1.000** | 0.000 | +0.999 +0.047i |
| ghost 0.20 | **+1.001** | -0.001 | +0.981 +0.185i |
| ghost 0.50 | **+1.002** | -0.002 | +0.901 +0.410i |
| ghost 1.00 | **+1.004** | -0.004 | +0.744 +0.629i |
| normal 0.05 | 0.000 | +1.000 | +0.999 -0.047i |
| normal 0.20 | -0.001 | +1.001 | +0.980 -0.189i |
| normal 0.50 | -0.002 | +1.002 | +0.875 -0.458i |
| normal 1.00 | -0.004 | +1.004 | +0.500 -0.806i |

**The decider (B2).** For the ghost with the anti-damping sign, the pole is on the **PHYSICAL
sheet** -- exactly ONE upper-half sheet-I pole, and NONE on sheet II, at every sampled coupling. A
physical-sheet complex pole (with its lower-half conjugate) is a complex energy = spectrum not real
= **spontaneously broken PT = no positive metric = NOT-OPERATIVE**. **The negative control (B3)
settles the convention**: the normal particle has ZERO physical-sheet poles and ONE on the second
sheet -- the textbook-correct statement that resonances live on sheet II and the physical sheet is
pole-free. Because the convention reproduces the normal case correctly, the ghost result is a
genuine, correctly-computed departure. And the sheet-II tracker (B1) shows the anti-damping
resonance in the **opposite half-plane** to the normal one (median `Im`: `+0.30` vs `-0.32`) -- the
W132 wrong-sign width / W51 `Im Sigma > 0` realized numerically.

So on the physically-anchored kinematics the ghost pole **does** reach the physical sheet: the
W172 no-go's *signal* is *realized* in a rigorous (argument-principle) model computation.

## 4. Persona 4 -- symbolic / numerical engineer: the test and its controls

`tests/W178_build_numerical_spectral_model.py`, **14/14, exit 0** (numpy only; seed 20260714 pins
the single fixed random vertex block). **Positive controls run FIRST**: **PC1** the
Bender-Brody-Jones 2x2 PT calibrator -- unbroken phase real spectrum, broken phase a
complex-conjugate pair, and the positive-metric witness collapsing to 0 at the exceptional point
`s = r|sin theta|`; **PC2** W171's `eta_+ = e^{-Q}` positive-definite at four couplings (0.1 -> 3.0);
**PC3** W169's Q2 secular-obstruction lattice reproduced exactly (generic + Stelle mass-split
EXIST `secular = 0`; `2:1` obstructs at Q1 `secular_Q1 = 34.3`; equal-mass/conformal and `3:1`
obstruct at Q2 `secular_Q2 = 420, 153`). **Negative controls**: A4/NC1 normal-sign spectrum real
to 1e-9 at `g` up to 20 (no exceptional point without a ghost); B3/NC1 normal-sign pole on the
second sheet (0 physical-sheet poles). Every load-bearing number has two routes or a matched
control (W138 discipline). Exactness where it matters: Model A's K-Hermiticity residual is `0.0`;
the argument-principle counts are integers to 3-4 digits.

## 5. Persona 5 -- adversarial skeptic: do not over-read a finite model

**Steelman the kill (Model B).** On the physically-correct Stelle kinematics -- massive ghost above
the two-graviton threshold, `Im Sigma(M^2) > 0` established (W51), width sign anti-damping
(W132) -- the resummed pole is on the PHYSICAL sheet by a rigorous integer count, at every
coupling, with the normal-sign control cleanly on the second sheet. That is a physical-sheet
complex-conjugate pair = broken PT = no C-operator = **NOT-OPERATIVE**. This is the numerical
realization the W172 no-go was missing; the tachyon is then physical and bar (b) is **re-posed** as
the false-vacuum record-accretion **engine** (W163/W166) -- a re-posing, not a program failure.

**Now bound it honestly (each conceded).**
1. *"It is a MODEL self-energy."* TRUE -- a single sqrt-threshold bubble, the same KIND W124 used,
   not GU's dressed self-energy. The **sign** (anti-damping) is inherited (W51/W132), not
   re-derived; if the dressed width were normal-sign the control (B3) shows the pole stays
   second-sheet and the grading is OPERATIVE.
2. *"The other regime is OPERATIVE."* TRUE -- Model A (a **gap-protected** discrete ghost, no open
   decay channel) is OPERATIVE with a positive C-metric all the way up to `g_c = 0.406`. Whether GU's
   ghost is above or below the effective continuum threshold is the physical fork, and the Stelle
   answer (massless gravitons, threshold at 0) puts it **above** -- Model B's regime -- but a
   confining / gapped dressing would move it.
3. *"A finite model cannot upgrade plausible to proven."* TRUE -- neither model fixes GU's coupling
   or its exact dressed self-energy; that is the inherited H59/W48 loop.

**Skeptic's residue (honest).** The two models **bracket** the answer by kinematic regime, and
**both isolate the ghost (anti-damping / indefinite-metric) sign** as the sole cause -- the
normal-sign controls show neither an exceptional point (A4) nor a physical-sheet pole (B3). The
numerical evidence therefore **leans NOT-OPERATIVE** on the physically-anchored kinematics, but the
absolute verdict is truncation-conditional on the two inherited facts above.

## 6. Synthesis and verdict

**PHYSICAL-SHEET-PT-BREAKS-NOT-OPERATIVE (leaning) on the physically-anchored Stelle kinematics;
TRUNCATION-CONDITIONAL overall.**

- **(a) C-metric positivity vs coupling.** `min eig(eta_+^{-1}) > 0` for `g < g_c = 0.406`
  (**OPERATIVE**; W171 finite-scale positivity reproduced, its boundary now located), collapsing
  monotonically to 0 at `g_c`; complex spectrum (NOT-OPERATIVE) above. Gap-protected regime.
- **(b) ghost self-energy pole sheet.** For the ghost above the two-graviton threshold (Stelle /
  W51 kinematics), the anti-damping self-energy puts the pole on the **PHYSICAL sheet** (argument
  principle: exactly 1 physical-sheet upper-half pole; normal-sign control: 0, benign second-sheet
  resonance). **PT broken, no positive metric, NOT-OPERATIVE.**
- **What it decides about bar (b).** The numerical evidence **LEANS NOT-OPERATIVE**: the
  physically-anchored Model B realizes the physical-sheet pole that W172 could only signal, so if it
  holds for GU's dressed self-energy the grading is a redundancy (not a record), the tachyon is
  physical, and bar (b) is **re-posed as the record-accretion engine** (W163/W166). This SHARPENS
  W172 -- from "signalled" to "realized in a rigorous model" -- without overturning it: the verdict
  stays conditional on (i) the dressed width carrying the W132 anti-damping sign and (ii) the ghost
  sitting above the effective continuum threshold, which is the **inherited H59/W48 open object**.
  Model A shows the alternative (gap-protected) regime is OPERATIVE below `g_c`, so the two regimes
  bracket the physical answer and the fork is a decidable dynamical question, not a mush.

**H59 remains OPEN.** No canon / RESEARCH-STATUS / claim-status / verdict / posture change.

## 7. What this does NOT do

- No QFT amplitude and no construction of the QFT C-operator: both models are finite/model stand-ins
  for `D` on non-compact Y14; the analytic layer (the Y14 propagator, W131's named residual) is
  untouched.
- No proof that GU's dressed self-energy is the anti-damping-sign, ghost-above-threshold case -- that
  sign and kinematics are inherited (W51/W132/Stelle), and the model self-energy is a single bubble
  (as W124's was), not GU's.
- No determination of GU's physical coupling relative to Model A's `g_c` -- the inherited H59/W48
  loop.
- No canon movement; no external action; the exploration is the computation, not a status change.

**Artifacts:** this file + `tests/W178_build_numerical_spectral_model.py` (14/14, exit 0).
