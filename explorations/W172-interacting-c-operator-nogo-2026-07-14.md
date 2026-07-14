---
artifact_type: exploration
status: exploration (W172 / TEAM NO-GO, label W172; adversarial NEGATIVE attack on the OPERATIVE side; five personas inline, one worker, no sub-agents; one deterministic test 13/13 exit 0 with positive controls)
created: 2026-07-14
wave: W172
label: W172
posture: coherence-first but ADVERSARIAL (attack the OPERATIVE side); exploration grade; honest grading
hypothesis: "Is the Krein grading OPERATIVE = does the interacting C-operator exist? The NEGATIVE attack: try to PROVE the interacting C-operator does NOT exist (NOT-OPERATIVE), by hardening the free no-local-positive-metric theorem (W121/W54) to the interacting case. If it succeeds the tachyon is physical and re-poses bar (b) as the false-vacuum record-accretion ENGINE (W163/W166), it does NOT fail the program."
title: "W172 VERDICT: NARROWED. The free no-local-positive-metric theorem (W121/W54) does NOT extend to forbid the interacting C-operator: it forbids LOCALITY, not EXISTENCE, and the non-locality is BOUNDED (strip-width m, kernel ~e^{-m|x|}), survivable. The interacting C exists ORDER BY ORDER (the positive metric eta_+ = eta C persists under the coupling in the unbroken phase, demonstrated exactly in a finite-dim calibrator). ROUTE 2: CLOP (W124) does NOT force a contradiction -- the GRADED family gives the single unambiguous even-cut value +1; the CLOP band {-1/2,0,+1/2,+1} is a REMOVAL-prescription artifact, so a C-operator commuting with the unambiguous graded S is not obstructed. ROUTE 3: the jointly-unsatisfiable axioms (W133 X1, (A) analyticity vs (P) positivity) PROVE no LOCAL positive metric -- which RE-DERIVES W54's non-locality, NOT a non-existence theorem; GU picks the positivity family consistently AS a non-local object. So the ASSIGNED metric-locality attack returns NO-OBSTRUCTION-FOUND. The ONLY live no-go is DYNAMICAL and INDEPENDENT of that theorem: the ghost self-energy has Im Sigma(M^2) > 0 (W51) with ANTI-DAMPING sign (W132: the leak is probability EXCESS, wrong-sign width), signalling spontaneous PT breaking = a physical-sheet complex-conjugate pole pair = NO positive metric = NO C-operator = NOT-OPERATIVE. But that no-go is CONDITIONAL on the pole reaching the PHYSICAL sheet (exceeding the exceptional point), which W124 established only on a MODEL self-energy and which IS H59's open W48 settling object. NET: the C-operator is OPERATIVE-CONDITIONAL-ON-UNBROKEN-PT, priced non-local (microcausality). Bar (b): NOT cleared, NOT proven-no-go; if the dynamical PT-breaking later closes, NOT-OPERATIVE -> engine reframe (bar (b) RE-POSED as engine, not failed). H59 remains OPEN."
grade: "EXACT for the Krein/CLOP/joint-unsatisfiability weight arithmetic (B2/B3a/B4b), for the W132 expansion identity A^dag A = P+ + B^dag B (PC3, machine-verified on random pseudo-unitary S), and for the Bender-Brody-Jones 2x2 calibrator (C^2=1, [C,H]=0, eta_+>0 in the unbroken phase; the exceptional point s=r|sin theta| where the positive metric ceases to exist). REPRODUCED for the free theorem (W121/W54: even entire grading indefinite; 0/3000 local polynomial fibers grade the ghost; canonical symbol strip-width m to 1e-15). STRUCTURAL for the finite-dim calibrator's role as a stand-in for the QFT C-operator existence question (the actual non-locality is the W54 1/sqrt(k^2+m^2) symbol; the 2x2 model calibrates existence-vs-PT-breaking, it is not the QFT theory). ARGUED for the identification of the anti-damping width with physical-sheet PT breaking (W124's physical-sheet finding is itself a dispersion-consistent MODEL self-energy, not a proof) and for the order-by-order-in-QM -> QFT lift (branch B). Test: tests/W172_interacting_c_operator_nogo.py 13/13 exit 0, positive controls first (calibrator existence; free theorem reproduced; W132 violation reproduced) and negative control (healthy normal-sign theory: C exists at all couplings). NO canon / RESEARCH-STATUS / claim-status / verdict / posture change. H59 remains OPEN."
depends_on:
  - explorations/W132-graded-optical-theorem-physical-subspace-2026-07-14.md
  - explorations/W163-lens-nonperturbative-vacuum-2026-07-14.md
  - explorations/W166-lens-tachyon-is-the-engine-2026-07-14.md
  - tests/W121_path2_target3_hypothesis_hardening.py
  - tests/W124_stageA_sunset_graded_vs_LW_CLOP.py
  - tests/W124_stageB_overlap_kite_cuts.py
  - tests/W132_graded_optical_theorem_physical_subspace.py
  - tests/W133_evencut_discriminator_dispersion.py
  - GEOMETER-VS-PHYSICS-OBJECTS.md
scripts:
  - tests/W172_interacting_c_operator_nogo.py
external_refs:
  - "Bender, Brody & Jones, Complex extension of quantum mechanics, PRL 89 (2002) 270401 -- the C-operator construction and the 2x2 PT calibrator (unbroken/broken phases, exceptional point)"
  - "Mostafazadeh, Pseudo-Hermiticity versus PT symmetry, JMP 43 (2002) 205 -- positive metric eta_+ = eta C; quasi-Hermiticity requires real spectrum"
  - "Bognar, Indefinite Inner Product Spaces, Springer 1974 -- Krein decompositions, fundamental symmetry"
  - "Cutkosky, Landshoff, Olive & Polkinghorne, NPB 12 (1969) 281 -- the CLOP order-of-limits ambiguity (removal family)"
  - "Lee & Wick, NPB 9 (1969) 209 -- the removal / complex-pair prescription"
  - "'t Hooft & Veltman, Diagrammar, CERN 73-9 -- largest-time equation, pseudo-unitarity"
---

# W172 -- does the no-local-positive-metric theorem forbid the interacting C-operator?

**Role.** Path-2 (W121) established a machine-checked NO-LOCAL-POSITIVE-METRIC theorem for the
FREE graded theory: no local positive-definite inner product exists; the C-metric is non-local,
W54-priced. W132 found the graded optical theorem VIOLATES on the free positive subspace and is
PRESERVED only in the C-metric sense, reducing keep-and-grade's unitarity WITHOUT REMAINDER to
the interacting C-operator question. This team runs the NEGATIVE attack on the OPERATIVE side:
try to PROVE the interacting C-operator does NOT exist. A clean NOT-OPERATIVE is a real result,
not a defeat -- it would make the tachyon physical and re-pose bar (b) as the record-accretion
ENGINE (W163/W166). Five personas inline; deterministic test
`tests/W172_interacting_c_operator_nogo.py` (13/13, exit 0).

## 0. The one object and the construction forks (GEOMETER-VS-PHYSICS-OBJECTS.md)

**The one object.** The interacting C-operator: an operator with `C^2 = 1`, `[C, S] = 0`, and
`eta_+ = eta C > 0` (positive-definite). Its EXISTENCE is exactly "the Krein grading is
OPERATIVE": if it exists, W132's C-metric unitarity holds on the full space and the ghost is a
bona fide positive-probability out-state; if it does not, physical-subspace unitarity has no
resource (W132) and the grading is NOT-OPERATIVE.

| Object | Constructions in play | Handling |
|---|---|---|
| **The C-operator** | (i) the FREE C (W54: exists, non-local, symbol `1/sqrt(k^2+m^2)`); (ii) the INTERACTING C (branch B: order-by-order in QM; QFT lift open) | both carried; the question is whether (ii) EXISTS |
| **"No positive metric"** | (L) no LOCAL positive metric (W54/W121, proven free); (E) no positive metric AT ALL (the no-go this team hunts) | the attack is precisely: does the interaction upgrade (L) to (E)? |
| **The ghost** | keep-and-grade real-mass Krein state (the branch under test) | the instability escape is the exit INTO Lee-Wick, named as such, not a defense |
| **PT symmetry** | unbroken (real spectrum, C exists) vs spontaneously broken (complex pair, no C) | the dynamical no-go lives at the exceptional point between them |

## 1. Persona 1 -- axiomatic/constructive QFT: the free theorem and the interacting lift

**The free theorem, restated (W121/W54).** In the positive-energy (Bender-Mannheim /
keep-and-grade) quantization of the 4th-order / Pais-Uhlenbeck field, NO positive metric `eta`
has an entire (Paley-Wiener local) symbol; the whole positive-intertwiner family carries the
`1/sqrt(k^2+m_i^2)` branch cuts; the kernel is exponentially localized `~e^{-m|x|}`. The
hypothesis ledger (W121 L1): **A** bounded-below quantization (NECESSARY), **B** Krein signs
`(+,-,-,+)` fixed by the local action (NECESSARY, load-bearing), **C** distinct masses
(NECESSARY), **D** translation invariance (CONVENIENT, now weakened: x-dependent finite-order
differential operators excluded), **E** "local = entire symbol" (NECESSARY AND TIGHT: the
quasi-local escape is realized by the canonical `eta` itself), **F** free theory (CONVENIENT at
first order; all-orders interacting open).

**The crucial reading (test PC2, B1a, B1b).** The theorem forbids **LOCALITY**, not
**EXISTENCE**. The free C-operator EXISTS -- it is the non-local (branch-cut) object whose
sign-type symbol realizes the ghost pattern `(+,-,-,+)` that every local polynomial fiber fails
(PC2: 0/3000 random polynomial graders; B1a: a branch-cut symbol grades it). And the price is
BOUNDED: the canonical symbol `1/sqrt(k^2+m^2)` is analytic in a strip of width exactly `m` (B1b:
Richardson-corrected `k^2`-series ratio `== 1/m^2` to 1e-15), i.e. exponentially localized, NOT
power-law. So in the free case the C-metric is a consistent non-local object with a controlled
(sub-Compton-wavelength) causality violation.

**The interacting lift (test B3b).** Branch B established the interacting C exists ORDER BY ORDER
in QM; the QFT generator `Q(g)` carries `1/sqrt(k^2+m^2)` energy denominators (the same W54
non-locality, now dressed by the vertex). To attack existence one asks: does some order's
equation for `Q_n` have NO solution? The finite-dim calibrator answers the model question
sharply: dressing the grading by a coupling `theta(g) = theta_0 + g` and sweeping `g` across the
unbroken phase, `eta_+ = eta C(g)` stays positive-definite throughout (B3b: min eigenvalue 0.765
> 0). The interaction DRESSES `C`; it does not, of itself, destroy the positive metric. **Route 1
verdict: NO-OBSTRUCTION** -- the no-local-positive-metric theorem does not extend to a
non-existence theorem; hypothesis F's gap (all-orders interacting) is a LOCALITY gap, and
locality is already conceded (and survivable).

## 2. Persona 2 -- Krein/PT specialist: the C-metric closure at loop level (W132/W133)

**What must close.** For the OPERATIVE reading, `S^dag eta_+ S = eta_+` with `eta_+ = eta C > 0`
(W132 Part 2 constructed exactly such an `S` in finite dimension, coexisting with the naive
violation). Closure at loop level means: `C(g)` remains a well-defined involution commuting with
the interacting `S(g)`, with `eta C(g)` positive. The calibrator's exceptional point is the exact
statement of where closure FAILS: `eta_+` is positive-definite precisely while PT is unbroken
(eigenvalues real), and it becomes indefinite the instant the spectrum goes complex (B4a). So
"does the C-metric close at loop level?" is EQUIVALENT to "does the interacting spectrum stay
real (PT unbroken)?" -- a spectral-reality question, not a locality question.

**Why locality alone does not break closure.** A non-local but bounded (strip-width `m`)
similarity transform `rho` with `eta_+ = rho^dag rho` maps the graded theory to a NON-LOCAL
Hermitian theory `H_herm = rho H rho^{-1}`. Non-locality means microcausality is violated within
`~1/m`, but the theory is still self-adjoint with real spectrum and unitary evolution. That is a
survivable object (the free case IS this object). Closure is threatened only if `rho` fails to
exist -- i.e. if the spectrum is complex. This hands the whole no-go to the DYNAMICAL question
(Section 5), not the kinematic locality one.

## 3. Persona 3 -- CLOP/Lee-Wick specialist: does W124's ambiguity force a contradiction?

**The CLOP band is a REMOVAL artifact (test B2).** W124 computed the two-loop mixed-threshold
ambiguity band `Im S_LW in {-1/2, 0, +1/2, +1} x Im S_graded`. But the ambiguity attaches to the
REMOVAL prescription's contour-deformation step (which order the pair width `M*Gamma` and the
residual `eps` are removed). The GRADED family -- real mass, ordinary Feynman contour, ordinary
Cutkosky cuts with Krein weight `(-1)^{n_ghost}` -- gives a SINGLE value: at the even (two-ghost)
cut `(-1)^2 = +1`, one point, no order-of-limits freedom (B2). The graded `S` is
CLOP-UNAMBIGUOUS. A C-operator is required to commute with THAT `S`; since `S` is unambiguous,
CLOP does not present it with an inconsistent object to commute with. **Route 2 verdict:
NO-OBSTRUCTION** -- CLOP does not force a contradiction in the interacting C-operator; it
constrains the removal family's uniqueness, a different branch. (This is the honest reading: the
adversary WANTED CLOP to inject an inconsistency into the graded C, and it does not.)

## 4. Persona 1 + 5 -- the jointly-unsatisfiable axioms (W133): a no-go, or a re-derivation?

**The joint-unsatisfiability (test B3a, W133 X1, exact).** The Lagrangian fixes the ghost residue
sign `eps = -1`. In ANY real-axis-cut quantization the cut weights are products of Krein signs:
even cuts carry `eps^2 = +1`, odd cuts carry `eps = -1`. Spectral positivity of ALL real-axis
cuts requires `eps = +1`. Contradiction: **(A)** real-axis analyticity and **(P)** spectral
positivity are JOINTLY UNSATISFIABLE for this Lagrangian class. The two quantization families
each keep exactly one axis: graded keeps (A) and grades the state space; Lee-Wick keeps (P) and
relocates absorptive content off-axis (its microcausality price).

**Does this PROVE no single C-operator? NO (the decisive adversarial move, honestly made).** The
joint-unsatisfiability is about (A)+(P) WITH A LOCAL STRUCTURE (real-axis cuts, local inner
product). The C-operator's entire function is to restore (P) by redefining the inner product to
the NON-LOCAL `eta_+ = eta C`. Under `eta_+` the ghost states have positive norm -- (P) is
restored -- at the cost of LOCALITY, i.e. exactly the escape the joint-unsatisfiability leaves
open. So W133's structure RE-DERIVES W54's non-locality (you cannot have both axioms locally),
it does NOT prove non-existence. **GU's structure picks the positivity family consistently, as a
non-local object.** Asking "does the jointly-unsatisfiable structure pick positivity
consistently?" -- yes, provided the non-local `eta_+` exists, which is the spectral-reality
question again. **Route 3 verdict: NO-OBSTRUCTION** as a non-existence proof.

## 5. Persona 5 -- adversarial skeptic RUTHLESS: steelman NO-OBSTRUCTION, then find the real handle

**Steelman NO-OBSTRUCTION at full strength.** Every kinematic route the mandate named fails to
produce non-existence: (1) no-local-positive-metric forbids LOCALITY (bounded, strip-width `m`,
survivable), the interacting C exists order-by-order; (2) CLOP is a removal artifact, the graded
`S` is unambiguous; (3) joint-unsatisfiability re-derives non-locality, not non-existence. Do NOT
manufacture a no-go that is not there: the assigned attack HONESTLY returns NO-OBSTRUCTION-FOUND.
The C-metric survives as a consistent non-local object at the level the free theorem controls.

**But do NOT shy from the genuine handle either -- and there is one, INDEPENDENT of the
metric-locality theorem (test B4a-B4d).** The C-operator exists iff PT is unbroken (the spectrum
is real); this is Mostafazadeh's quasi-Hermiticity condition, exhibited exactly by the calibrator
(B4a: past the exceptional point `s < r|sin theta|` the eigenvalues go complex and NO positive
metric exists). Now the dynamics: the interacting ghost self-energy has `Im Sigma(M^2) > 0`
(W51's proven sign) AND the associated leak is probability EXCESS -- W132's exact identity
`A^dag A - P_+ = B^dag B >= 0`, the S-matrix face of the ANTI-resonance (wrong-sign width) (B4b).
A wrong-sign width is a pole in the WRONG half-plane = a growing mode = precisely the
physical-sheet complex-conjugate pair that SPONTANEOUSLY BREAKS PT. Broken PT ⟹ no positive
metric ⟹ no C-operator ⟹ NOT-OPERATIVE. **This handle is DYNAMICAL and is NOT supplied by the
no-local-positive-metric theorem** -- it is a separate spectral fact.

**Why it is NARROWED, not NO-GO-PROVEN (B4c).** Whether the pole actually REACHES the physical
sheet (exceeds the exceptional point) versus stays a benign SECOND-sheet resonance is UNDECIDED
at the available rigor. W124 asserted "physical sheet" on a dispersion-consistent MODEL
self-energy, not a proof; the settling computation is exactly H59's W48 minimal source-action
loop, still OPEN. The negative control (B4d) confirms the no-go is SPECIFIC to the ghost's
anti-damping sign: a healthy normal-sign theory stays unbroken for all couplings and the
C-operator exists everywhere -- the calibrator does not manufacture the no-go.

## 6. Synthesis and verdict (question 4)

**Does the no-local-positive-metric theorem extend to the interacting case? NO** -- it forbids
LOCALITY, not EXISTENCE, and the non-locality is bounded and survivable; the interacting C exists
order-by-order; the C-metric survives as a consistent non-local object (routes 1-3 all
NO-OBSTRUCTION).

**The jointly-unsatisfiable-axioms result (question 3).** (A) analyticity and (P) positivity are
jointly unsatisfiable WITH A LOCAL STRUCTURE (W133 X1, exact). This PROVES no LOCAL positive
metric -- a re-derivation of W54's non-locality -- NOT that no single C-operator exists. GU's
structure picks the positivity family consistently as a NON-LOCAL object.

**The one live no-go (question 2).** DYNAMICAL PT breaking: the anti-damping width (W51 sign x
W132 excess) signals a physical-sheet complex pole pair = broken PT = no C-operator =
NOT-OPERATIVE. This is INDEPENDENT of the metric-locality theorem and CONDITIONAL on the pole
reaching the physical sheet (= H59's open object).

**VERDICT: NARROWED.** The assigned metric-locality attack returns NO-OBSTRUCTION-FOUND; the
no-go survives only as the dynamical PT-stability question, NARROWED-TO the physical-sheet-vs-
second-sheet fate of the interacting ghost pole (H59's W48 settling computation). The interacting
C-operator is **OPERATIVE-CONDITIONAL-ON-UNBROKEN-PT**, priced non-local (microcausality).

**Effect on bar (b): NEITHER cleared NOR proven-no-go -- SHARPENED.** Bar (b) carries the
C-operator as operative-conditional-on-unbroken-PT with a standing non-locality (microcausality)
cost. If the dynamical PT-breaking later CLOSES (the pole is shown physical-sheet by the H59 W48
computation), the grading is NOT-OPERATIVE, the tachyon is physical, and bar (b) is RE-POSED as
the false-vacuum record-accretion ENGINE (W163/W166) -- a re-posing, NOT a program failure. If PT
is shown UNBROKEN (pole stays second-sheet), the C-operator exists and the OPERATIVE reading is
consistent, bar (b) carrying the non-locality cost. The no-local-positive-metric theorem alone
settles NEITHER direction.

## 7. What this does NOT do

No claim that the C-operator does or does not exist in QFT -- the finite-dim calibrator settles
the EXISTENCE-VS-PT-BREAKING logic (existence iff unbroken PT), not the QFT spectrum. No proof
that the ghost pole is physical-sheet (that is W124's model finding and H59's open computation).
No spin-2 tensor numerators (W134 owns those). No canon / RESEARCH-STATUS / claim-status /
verdict / posture change; **H59 remains OPEN** (the settling object is unchanged: the W48 minimal
source-action loop, now equipped with the sharpened criterion -- compute whether the graded
ghost's dressed pole crosses to the physical sheet, i.e. whether interacting PT is spontaneously
broken).

**Artifacts:** this file + `tests/W172_interacting_c_operator_nogo.py` (13/13, exit 0).
