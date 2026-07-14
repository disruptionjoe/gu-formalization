---
artifact_type: exploration
status: exploration (5-persona inline team; two deterministic tests; H59 path-2 named next targets)
created: 2026-07-13
hypothesis: H59
branch: "Path-2 wave-3 (Team H59): Target 2 graded side (does keep-and-grade face the CLOP ambiguity?) + Target 3 hardening (hypothesis audit of the no-local-positive-metric theorem)"
title: "TARGET 2 (graded side) VERDICT: EVADES-AT-FIXED-ORDER / RE-FACES-UNDER-RESUMMATION. The CLOP order-of-limits ambiguity attaches to the contour-deformation step of the REMOVAL prescription; keep-and-grade at strict fixed order performs no removal and no deformation, so the ambiguity has no step to attach to. Toy-checked on the 1-loop bubble: the graded ghost cut is -pi(1-M^2/s) (the W48 leak) while the Lee-Wick conjugate-pair contour gives exactly zero for every width; the prescriptions are separated by a non-commuting Gamma->0 limit on the odd-ghost cut support. NEW structural point: graded cut sign = (-1)^{n_ghost}, so W55's CLOP pinch locus s=4M^2 is an EVEN (two-ghost) cut, positive and Cutkosky-unambiguous in the graded theory, while the graded leak locus s=M^2 is empty in Lee-Wick: the two families pay at DISJOINT thresholds. The evasion is bounded by the resonance window |s-M^2| <~ M*Gamma, which is O(M^2) for the broad gravitational ghost: inside it resummation forces complex poles and the contour question returns. TARGET 3 VERDICT: HARDENED-NOT-CLOSED. Hypothesis audit: 4 of 6 hypotheses NECESSARY (one provably TIGHT: the quasi-local escape is realized by the canonical metric itself, so 'no entire-symbol metric' cannot be strengthened to 'no quasi-local metric'); translation invariance weakened -- x-dependent finite-order differential operators are now excluded (pointwise sign-domination, symbolic to degree 6), and equal-energy shell-mixer escapes are power-law non-local (worse than canonical). Remaining escape classes named. H59 remains OPEN."
grade: "STRUCTURAL for the prescription-step attachment claim (the CLOP parameter enters only via the deformation step; ledger-level, consistent with Anselmi-Piva's diagnosis that the ambiguity is a defect of the CLOP formulation); TOY-CHECKED for every contour claim (1-loop bubble, two routes per number, mpmath quadrature vs closed form, 16/16); STRUCTURAL+TOY-CHECKED for the cut-sign parity / disjoint-loci point; ARGUED for the resummation-window guard (fixed-order breakdown scale is standard resonance counting; the O(1) width imports W51's proven Im Sigma(M^2)>0 sign and Gamma/M=O(1) estimate). Target 3: DERIVED (symbolic, degrees 1..6) + swept (4000 draws) for the differential-operator exclusion, with the positivity-to-pointwise-symbol-sign link the named ARGUED step; DERIVED for hypothesis tightness (exact ratio test + kernel slope); ARGUED for the shell-mixer class. Tests: W120 16/16 exit 0, W121 11/11 exit 0, each with positive AND negative controls. No two-loop amplitude computed; W55's removal-side two-loop tensor computation remains open. NO canon / RESEARCH-STATUS / claim-status / verdict / posture changed. H59 remains OPEN."
depends_on:
  - explorations/path2-wave1-synthesis-and-wave2-design-2026-07-11.md
  - explorations/path2-wave2-target2-clop-pinch-gate-2026-07-12.md
  - explorations/path2-wave2-target3-no-local-positive-metric-2026-07-11.md
  - explorations/path2-branchA-cutkosky-cut-2026-07-11.md
  - explorations/path2-branchD-leewick-2026-07-11.md
  - explorations/h59-frg-minimal-truncation-krein-negative-ratio-2026-07-13.md
  - tests/W48_H59_krein_loop_positivity_gate.py
  - tests/W54_path2_target3_no_local_metric.py
  - tests/W55_path2_target2_clop_pinches.py
  - GEOMETER-VS-PHYSICS-OBJECTS.md
scripts:
  - tests/W120_path2_target2_keepgrade_vs_clop.py
  - tests/W121_path2_target3_hypothesis_hardening.py
external_refs:
  - "Cutkosky, Landshoff, Olive & Polkinghorne, A non-analytic S-matrix, NPB 12 (1969) 281 -- the CLOP prescription and its order-of-limits ambiguity"
  - "Grinstein, O'Connell & Wise, Causality as an emergent macroscopic phenomenon, PRD 79 (2009) 105019, arXiv:0805.2156 -- the GOW Lee-Wick cutting rules"
  - "Anselmi & Piva, A new formulation of Lee-Wick quantum field theory, JHEP 06 (2017) 066, arXiv:1703.04584; Perturbative unitarity of Lee-Wick quantum field theory, PRD 96 (2017) 045009, arXiv:1703.05563 -- the CLOP ambiguity localized at >=2-loop mixed thresholds; ambiguity diagnosed as a defect of the CLOP formulation"
  - "Lee & Wick, Negative metric and the unitarity of the S-matrix, NPB 9 (1969) 209"
  - "Bender & Mannheim, No-ghost theorem for the fourth-order derivative Pais-Uhlenbeck oscillator model, PRL 100 (2008) 110402"
  - "Mostafazadeh, Pseudo-Hermiticity versus PT symmetry, JMP 43 (2002) 205 -- intertwiner family structure"
  - "Bognar, Indefinite Inner Product Spaces, Springer 1974 -- Krein-space gradings and maximal positive subspaces"
---

# Path-2 Wave-3 -- Target 2 (graded side) and Target 3 (theorem hardening)

**Role.** The wave-1 synthesis named two remaining firm-ups after Target 1: TARGET 2 (the two-loop
CLOP question) and TARGET 3 (harden the no-local-positive-metric theorem). W55 already localized the
removal-family pinch candidate (the mixed conjugate threshold `s = 4M^2`) and showed broad
derivative-coupled gravity does not inherit the narrow-scalar theorem. This run executes the two
named next steps that were still missing:

1. **Target 2, graded side:** the trade map prices the GRADING branch (Family 1) in RG-contingency
   and locality. But does keep-and-grade ALSO inherit the CLOP ambiguity, adding a second cost to
   that branch? Nobody had asked the question at the prescription level.
2. **Target 3:** the W54 theorem is flagged independently publishable; its hypotheses had not been
   audited for necessary-vs-convenient, and gap (b) (non-translation-invariant metrics) was raw.

Deterministic tests: `tests/W120_path2_target2_keepgrade_vs_clop.py` (16/16, exit 0) and
`tests/W121_path2_target3_hypothesis_hardening.py` (11/11, exit 0). Five personas run inline,
sequentially; their outputs are folded into the sections below.

## 0. Construction forks (GEOMETER-VS-PHYSICS-OBJECTS.md discipline)

| Object | Constructions in play | Handling |
|---|---|---|
| **The ghost** | (i) keep-and-grade stable Krein-graded real-mass state (GU-native); (ii) Lee-Wick complex-conjugate-pair resonance (Family 2) | **BOTH computed side by side on the same 1-loop bubble** -- the comparison IS the result. Neither defaulted. |
| **Cutting rules** | (i) ordinary real-axis Cutkosky with Krein-sign weights; (ii) GOW/CLOP deformed contour | The ambiguity under test is a property of (ii)'s deformation step; (i) is checked to have no analogous step. |
| **Positivity** | Krein-graded optical theorem (cut weight = product of Krein signs), not pseudo-unitarity, not tree positivity | W48 gate discipline: nothing here counts as loop positivity itself. |
| **"Local" (Target 3)** | entire symbol of finite exponential type (Paley-Wiener), per W54 | Audited rather than assumed: shown NECESSARY AND TIGHT (Section 4). |

## 1. Persona 1 -- PT/Krein specialist: what "facing CLOP" would even mean for the graded theory

The CLOP ambiguity is an order-of-limits ambiguity in HOW a deformed integration contour treats a
pair of complex-conjugate poles when external kinematics pin them against each other (the >=2-loop
mixed threshold). For the graded theory the prior question is: does the graded construction ever
put complex-conjugate poles on the physical sheet with a contour that must be deformed around them?

At **strict fixed order** the answer is structurally no. Keep-and-grade removes nothing: the ghost
propagates with its real mass `M^2` and the ordinary Feynman `i*eps` contour; the absorptive parts
are computed by ordinary Cutkosky cutting; the only modification relative to a healthy theory is the
**weight** each cut carries -- the product of the Krein signs of the cut lines. There is no
resummation step, no complex pole, no deformation, and therefore **no order-of-limits parameter
anywhere in the fixed-order graded amplitude** (test S1, the prescription-step ledger). Positivity
in the graded theory is a statement about the C-operator / sector-wise norms on the state space
(Bognar-style maximal positive subspaces), not about a contour choice: the contour is inherited
unchanged from ordinary QFT. This matches Anselmi-Piva's independent diagnosis from the other side:
the ambiguity is a defect of the CLOP FORMULATION (the deformation-plus-limits procedure), not an
intrinsic property of theories with heavy unstable ghosts.

**What positivity must mean here (and what this file does not touch):** the graded optical theorem
reads `2 Im M = sum_cuts (prod Krein signs) * (positive phase space)`. The open H59 question is
whether the physical-subspace projection kills the negative (odd-ghost) terms; that is W48's gate
and is NOT advanced here.

## 2. Persona 2 -- Lee-Wick/CLOP expert: the precise locus of the ambiguity

From CLOP 1969, GOW 0805.2156, and Anselmi-Piva 1703.04584/1703.05563, the two-loop ambiguity sits
at the **mixed conjugate-pole threshold** `s = (m_+ + m_-)^2 = 4M^2` (exactly W55's pinch locus):
the deformed contour is pinched between `m_+` and `m_-` poles and the result depends on the order in
which the deformation width and the CLOP separation parameter are taken to zero. Attachment
analysis, step by step:

1. Resum the self-energy so the ghost pole splits into a conjugate pair -- introduces complex poles.
2. Remove the ghost from asymptotic states -- makes the real-axis cut through the ghost line empty.
3. Deform the contour around the complex pair (GOW/CLOP) -- **this is the step that carries the
   order-of-limits parameter**, and it only exists because steps 1-2 were performed.

The ambiguity therefore attaches to the **contour step of the removal prescription**, not to the
presence of a wrong-sign residue as such. A construction that never performs steps 1-3 cannot meet
the ambiguity at fixed order. That is the structural core of the graded-side verdict (STRUCTURAL,
ledger-level; test S1).

## 3. Persona 3 -- loop engineer: the toy checks (all numbers two-route)

The 1-loop bubble with one massless line and one massive line, parameter-integral form
`b0(s;a) = -int_0^1 dx log(x a - x(1-x)s - i eps)`, `Im b0 = pi (1 - a/s) theta(s - a)`:

| Check | Result |
|---|---|
| PC1/PC2 positive controls | quadrature Im matches `pi sqrt(1-4m^2/s)` (equal mass) and `pi(1-a/s)` (one massless) to 1e-6 at all sampled `s`; below threshold Im = 0 |
| K1/K2 graded ghost bubble | absorptive part `= -pi(1-M^2/s)` on `s > M^2`, NEGATIVE (the W48 leak), opening exactly at `s = M^2` |
| L1/L2 Lee-Wick pair on the same bubble | sympy identity: the conjugate-pair combination equals the manifestly real Lee-Wick propagator; bubble Im `< 1e-10` for every width `Gamma/M in {0.01, 0.1, 0.5, 1.0}` (Schwarz-reflection cancellation) |
| O1 first difference | the prescriptions differ exactly and only on the odd-ghost cut support, by a **non-commuting limit**: `lim_{Gamma->0} Im(LW) = 0` but `Im(graded, Gamma=0) = -pi(1-M^2/s)` |
| O2 | the REAL parts converge as `Gamma -> 0` (0.288 -> 0.039): the prescriptions differ only in cut assignment, i.e. at the contour step |
| P1-P3 disjoint loci | graded cut sign `= (-1)^{n_ghost}`; the CLOP locus `s = 4M^2` is an even (two-ghost) cut, graded value `+pi sqrt(1-4M^2/s) > 0`, ordinary Cutkosky; the graded leak locus `s = M^2` is empty in LW |
| NC1 negative control | flipping the residue sign to +1 gives a positive cut: the leak genuinely tracks the Krein sign |

**The disjoint-loci point is the new structural output of the toy:** the two rescue families do not
merely pay in different currencies (wave-1 map), they pay at **different kinematic thresholds** --
grading pays at odd-ghost thresholds (first at `s = M^2`), removal risks ambiguity at the even mixed
threshold (`s = 4M^2`), and each family is clean exactly where the other is exposed
(TOY-CHECKED at one loop, STRUCTURAL for the parity rule, which is just multiplicativity of the
Krein signs over cut lines).

## 4. Persona 4 -- mathematical physicist: Target 3 hypothesis audit and hardening

The W54 theorem: in the positive-energy (Bender-Mannheim) quantization of the free 4th-order/PU
field, no positive intertwiner `eta` has an entire (Paley-Wiener local) symbol. Proof skeleton:
(i) commutant characterization of the FULL positive family; (ii) positivity forces the odd-in-energy
sign pattern, whose interpolant carries `1/sqrt(k^2+m_i^2)` for every commutant weight; (iii) the
only entire grading is even-in-energy and yields an indefinite metric; (iv) independent Paley-Wiener
route agrees at `k = +-i m`.

**Audit table (test L1), with the hardening results:**

| Hypothesis | Necessary / convenient | Escape class remaining |
|---|---|---|
| A. Bounded-below (BM) quantization | **NECESSARY** -- in the unbounded-below quantization `eta = 1` is local and positive; drop A and the theorem is false | none (this is the non-vacuity clause) |
| B. Krein signs `(+,-,-,+)` fixed by the local action | **NECESSARY, load-bearing** -- NC1: with all-positive signs the constant local `C = 1` grades; the obstruction is ghost-specific | a local re-signing of the propagator residues would kill the theorem; none known |
| C. Distinct masses `m1 != m2` | **NECESSARY** for the commutant argument | the degenerate case is the exceptional (Jordan) locus where the grading dies anyway (W52/W53); no escape lives there |
| D. Translation invariance of `eta` | **CONVENIENT -- NOW WEAKENED (new)** | see below |
| E. "Local" = entire symbol (Paley-Wiener) | **NECESSARY AND TIGHT (new)** -- the canonical metric ITSELF is quasi-local (strip-analytic of width exactly `m`: exact ratio test; kernel slope `-> -m` after removing the known `(1/2)log r` subleading term). The escape class "quasi-local metrics" is NONEMPTY, so strengthening the theorem to exclude quasi-local metrics is impossible: the hypothesis sits on the true boundary | quasi-locality is not an escape FROM the trade; it IS the priced cost (exponentially localized at the ghost scale) |
| F. Free theory | CONVENIENT at first order (W54 INT1/INT2, strong-argument) | all-orders interacting cancellations, still open |

**The D hardening (the main new result).** The large-`k` sign-domination obstruction is POINTWISE:
a finite-order differential operator with arbitrary `x`-dependent coefficients has, at each fixed
`x`, a polynomial fiber symbol `F(lambda) = sum c_j(x) lambda^j`. Symbolically (degrees 1..6,
generic coefficients): `F(om1) + F(om2) ~ 2 c_d k^d` while `F(om1) - F(om2) ~
(d/2) c_d (m1^2 - m2^2) k^{d-2}` -- the ratio diverges like `k^2` for EVERY polynomial fiber.
Opposite grading signs on the two shells require `|sum| < |diff|`, so **no x-dependent finite-order
differential operator can implement the grading at large k** (T3-1a symbolic + T3-1b 4000-draw
sweep, zero holders). This upgrades W54's gap (b) from ARGUED to **STRONG-ARGUMENT for the
differential-operator class**. The named remaining ARGUED step: the semiclassical link between
operator positivity and pointwise principal-symbol signs.

**The shell-mixer escape (T3-3, ARGUED).** Without translation invariance the commutant of `H`
acquires equal-energy cross-shell mixers (`om1(k1) = om2(k2) = E` for every `E > m2`). But a shell
mixer's position kernel is a delta-shell Fourier transform with power-law envelope `~1/r`, which
dominates the canonical `e^{-m r}` without bound: escaping translation invariance through the
natural commutant extension buys MORE non-locality, not less. The honest remaining escape class for
gap (b): x-dependent local kernels whose fiber symbols are entire but NON-polynomial (finite
exponential type, e.g. oscillatory) -- neither the commutant characterization (translation-invariant
only) nor the pointwise domination argument (polynomial only) covers them. That class is now the
entire content of gap (b).

**Coverage (T3-4).** The theorem does not cover fakeon/Lee-Wick and structurally cannot: they never
seek a positive metric on the ghost-inclusive space (state-space change, priced in causality). The
theorem is exactly a Family-1 cost statement; stating this is a scope clarification, not a weakness.

## 5. Persona 5 -- adversarial skeptic: trying to make keep-and-grade INHERIT the ambiguity

**Attack 1: "the graded ghost is unstable, so fixed order is a fiction."** PARTLY LANDS, and it is
the reason the verdict is NARROWED rather than a clean EVADES. `Im Sigma(M^2) > 0` is
prescription-independent (W51's proven sign): the graded ghost decays into two gravitons whatever
the metric bookkeeping says. Strict fixed order fails in the resonance window
`|s - M^2| <~ M*Gamma`, and for the gravitational ghost `Gamma/M = O(1)` (broad, Planckian), so the
window is `O(M^2)` -- not a small neighborhood (test G1: window fraction 2.0 vs 0.02 for the narrow
reference). Inside the window the graded theory must resum; the dressed pole pair is complex
(forced by reality); and any object built from the RESUMMED graded propagator at the two-loop mixed
threshold faces the same contour question as the removal family. The evasion is real but has a
computable domain of validity, and for gravity that domain excludes an O(1) neighborhood of the
ghost scale.

**Attack 2: "the odd-ghost leak is worse than the ambiguity you evaded."** CORRECT AS PRICING, and
already on the books: the leak (W48, branch A) is Family 1's known cut-level cost, reproduced here
as K1. Nothing new is added to that cost; what is new is the demonstration that CLOP is NOT a
second, additional cost at fixed order, plus the disjoint-loci statement showing the leak and the
ambiguity cannot stack at the same threshold.

**Attack 3: "at two loops a graded overlapping diagram might generate its own order-of-limits
parameter."** FAILS at fixed order: all internal masses are real, all thresholds are real-axis
Cutkosky thresholds of a hermitian local Lagrangian, and two-loop cutting of real-mass diagrams is
unambiguous (standard). The only route to an order-of-limits parameter is through resummation
(attack 1). The two-ghost cut at `s = 4M^2` in the graded theory is positive and ordinary (P3).

**Net skeptic report, at full strength:** the grading branch does NOT gain a second prescription
cost at fixed order; it DOES have its evasion bounded by the O(1) resonance window, inside which the
graded and removal constructions face the SAME unresolved complex-pole contour question. If that
resummed-contour question resolves badly, it hits both families at once.

## 6. Verdicts

**TARGET 2 (graded side): EVADES-AT-FIXED-ORDER / RE-FACES-UNDER-RESUMMATION** (NARROWED-TO: the
resummation window `|s - M^2| <~ M*Gamma`, `O(M^2)` for the broad gravitational ghost).
STRUCTURAL for the attachment claim, TOY-CHECKED for every contour statement. The removal-side
computation W55 named (two-loop tensor discontinuity near `s = 4M^2`) remains Target 2's open half.

**TARGET 3: HARDENED-NOT-CLOSED.** Audit complete (4 NECESSARY, of which E provably TIGHT; 2
CONVENIENT, of which D now weakened). New exclusions: x-dependent finite-order differential
operators (STRONG-ARGUMENT); shell-mixer escapes priced as power-law non-local (ARGUED). Remaining
gap (b) content: x-dependent entire non-polynomial fiber symbols. The theorem remains free-case +
first-order-interacting; its independently-publishable status is strengthened by the tightness
result (the locality hypothesis is on the true boundary, not an artifact of the definition chosen).

## 7. Loop-positivity state (the one-paragraph synthesis, post-W119 + this wave)

Loop positivity for keep-and-grade 4th-order gravity currently stands as follows. The flow side is
as solid as a truncation can make it: the spin-2 grading is RG-stable at all finite scales at one
loop (W53) and in the minimal FRG truncation across three regulator families (W119), with only the
already-named forks (ghost-mass convention, eta_C scheme, spin-0 gauge status) open at the UV
endpoint. The state-space side is priced but not decided: unitarity is a positivity-vs-causality
trade (wave 1); the grading branch's positive metric is provably non-local but exponentially
localized (W54, now hardened: hypotheses audited, differential-operator escapes closed, locality
hypothesis proven tight); the grading branch does NOT additionally inherit the Lee-Wick CLOP
ambiguity at fixed order, because that ambiguity attaches to the removal prescription's contour
step (W120), and the two families' danger loci are disjoint (odd-ghost `s = M^2` vs even-mixed
`s = 4M^2`). What is NOT settled is the sign of the physical-subspace optical theorem itself: the
odd-ghost cut leaks negatively (W48) and whether the graded projection cancels that leak is exactly
the frontier-blocked question. **The single object that would settle the remaining Target-2/family
question:** the two-loop overlapping self-energy at the mixed threshold `s ~ 4M^2`, computed ONCE
with the resummed complex-pair propagator (removal rules) and ONCE in the graded fixed-order theory
with the spin-2 tensor numerator retained, compared for prescription independence and cut sign --
inside the resonance window where the two constructions must converge or visibly split. (For H59
itself the settling object remains W48's minimal source-action loop computation at the negative
ratio; this wave narrows the prescription landscape that computation must navigate.)

## 8. What this does NOT do

No two-loop amplitude computed (W55's named computation still open). No claim that keep-and-grade
loop positivity holds; the W48 leak stands. No all-orders interacting metric theorem. No resolution
of the ghost-mass or eta_C forks. No CANON.md / RESEARCH-STATUS.md / claim-status / verdict /
posture change. **H59 remains OPEN.**

**Artifacts:** this file + `tests/W120_path2_target2_keepgrade_vs_clop.py` (16/16, exit 0) +
`tests/W121_path2_target3_hypothesis_hardening.py` (11/11, exit 0).
