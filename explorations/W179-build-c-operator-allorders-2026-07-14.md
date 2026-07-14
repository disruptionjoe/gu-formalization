---
artifact_type: exploration
status: "exploration (W179 / TEAM BUILD-COP-ALLORDERS; label W179; coherence-first BUILD; five inline personas, one worker, no sub-agents; one deterministic test 23/23 exit 0 with positive + negative controls; EXTENDS W169's QM Q1/Q2 construction to the QFT momentum-space generator Q1(k) with the W54 non-local denominators, and to the all-orders question)"
created: 2026-07-14
label: W179
posture: coherence-first BUILD sprint; exploration grade; honest grading
hypothesis: "Extend the interacting C-operator (W169: C = e^Q P, Q = gQ1 + g^2 Q2 + ..., built through Q2 in QM) toward (i) the QFT/field-theory generator Q1(k) with the correct NON-LOCAL 1/sqrt(k^2+m^2) energy denominators (W54), and (ii) higher / all orders. Does the QFT Q1(k) exist as a bounded (if non-local) similarity to a Hermitian Hamiltonian, and is the all-orders C-operator plausibly convergent for GU's generic spectrum?"
verdict: "PARTIAL / OBSTRUCTS-AT-THRESHOLD. The QFT lift of W169's leading equation [H0,Q1]=-2A is elementwise division by the CONTINUUM energy denominator D(k1,k2) = om2(k1+k2) - om1(k1) - om1(k2) (om_i = sqrt(k^2+m_i^2)); the QFT Q1 kernel is -2g/D. W169's SECULAR/degenerate-block obstruction (a source between E_m=E_n states) lifts to 'D has a real on-shell zero', and that zero exists IFF the ghost can decay into two physical quanta, i.e. IFF m_ghost >= 2 m_phys (the two-body DECAY THRESHOLD). This is W169's discrete 2:1 resonance (w_ghost = 2 w_phys, the Q1 obstruction) lifted to the continuum. RESULT: (SUB-threshold, m_ghost < 2 m_phys) D is strictly one-signed, no on-shell zero -> the QFT Q1 generator EXISTS as a bounded NON-LOCAL kernel whose only singularities are the branch points k=+-i m_i (strip width = the mass gap, position kernel ~ e^{-m|x|}, W54) = a bounded non-local Hermitian partner; and all-orders is CONVERGENT-PLAUSIBLE (W97 strip = gap at EVERY order, geometric majorant with radius set by the gap). (AT/ABOVE threshold, m_ghost >= 2 m_phys) D=0 on a real surface -> the Q1 kernel has an ON-SHELL POLE -> the naive Hermitian generator fails; the resolved pole is the anti-damping width Im Sigma(M^2) > 0 (W51) = spontaneous PT-breaking (W172) = no positive C-metric = NOT-OPERATIVE, and all-orders DIVERGES. THE STELLE SPECTRUM (massless graviton m_phys=0 + massive ghost M): the threshold is 0, so ANY M > 0 is ABOVE threshold (the ghost is embedded in the massless two-graviton continuum) -> the CONTINUUM lift OBSTRUCTS, whereas W169's DISCRETE reading called it OPERATIVE (via 1 != n*0). The QM non-resonance does NOT survive the continuum for a massless lighter field. Effect on bar (b): the QFT lift REPLACES W169's commensurate-ratio sub-bit with the cleaner kinematic sub-bit 'is the ghost below or above the two-physical-particle decay threshold?', and for the physically relevant Stelle spectrum the answer is ABOVE -> the QFT Q1 generator has an on-shell pole -> this COINCIDES exactly with W172's one live dynamical no-go (the ghost decay width, H59's W48 self-energy). The C-operator's QFT existence is CONDITIONAL-ON-SUB-THRESHOLD (PT-unbroken), consistent with W172. H59 remains OPEN."
grade: "EXACT for the QFT energy denominator D = om2(k1+k2)-om1(k1)-om1(k2) and its on-shell-zero <=> decay-threshold discriminant (the rest-frame zero at k^2 = m_ghost^2/4 - m_phys^2, real iff m_ghost > 2 m_phys, machine-symbolic); for the sup-over-splits identity sup_K [sqrt(K^2+m2^2)-sqrt(K^2+4m1^2)] <= 0 iff m2 <= 2 m1; and for the two-body phase-space (Im Sigma) opening exactly at threshold. REPRODUCED for the positive controls: a known non-local C-operator (2x2 Bender-Brody-Jones, C^2=1, [C,H]=0, real spectrum), the W54 kernel bound (K0(m|x|) log-tail slope -m), and W169's discrete Q1/Q2 secular map (generic clean; 2:1 at Q1; equal-mass at Q2). STRUCTURAL for the identification D's real zero = W169's degenerate-block source lifted to the continuum, and for the QFT boundedness reading (no on-shell pole + strip width = gap => bounded non-local partner in the W172 sense). ARGUED / STRONG-ARGUMENT for the all-orders statements: the strip-width-=-gap-at-every-order protection is the W97/W54 mechanism (not a new all-orders theorem); the geometric-majorant convergence is conditional on a bounded renormalized vertex (the standing UV/renormalization structure is inherited, not re-solved here); and the above-threshold DIVERGENCE is the pole-pile-up argument, not a resummation computation. Whether the above-threshold pole reaches the PHYSICAL sheet (a true kill) vs a benign second-sheet resonance is UNDECIDED at this rigor -- it is H59's open W48 self-energy, inherited unchanged. Test: tests/W179_c_operator_allorders_qft.py 23/23 exit 0, positive controls first + negative control (sub-threshold ghost stays bounded, zero width; the pole switches on exactly at ratio 2). NO canon / RESEARCH-STATUS / claim-status / verdict / posture change. H59 remains OPEN."
depends_on:
  - explorations/W169-c-operator-perturbative-construction-2026-07-14.md
  - explorations/W172-interacting-c-operator-nogo-2026-07-14.md
  - explorations/W132-graded-optical-theorem-physical-subspace-2026-07-14.md
  - explorations/cond-iii-w54-all-orders-2026-07-11.md
  - tests/W54_path2_target3_no_local_metric.py
  - tests/W121_path2_target3_hypothesis_hardening.py
  - tests/W132_graded_optical_theorem_physical_subspace.py
  - tests/W169_c_operator_perturbative_construction.py
  - GEOMETER-VS-PHYSICS-OBJECTS.md
scripts:
  - tests/W179_c_operator_allorders_qft.py
external_refs:
  - "Bender, Brody & Jones, Complex extension of quantum mechanics, PRL 89 (2002) 270401 -- the C = e^Q P construction and the 2x2 non-local C-operator calibrator"
  - "Mostafazadeh, Pseudo-Hermiticity versus PT symmetry, JMP 43 (2002) 205 -- positive metric eta_+ = eta C; quasi-Hermiticity requires a real spectrum (unbroken PT)"
  - "Stelle, Renormalization of higher-derivative quantum gravity, PRD 16 (1977) 953 -- the 4th-order theory: massless graviton + massive spin-2 ghost; the ghost is UNSTABLE"
  - "Bender & Mannheim, No-ghost theorem for the fourth-order derivative Pais-Uhlenbeck oscillator, PRL 100 (2008) 110402 -- real spectrum + positive metric for UNEQUAL frequencies; the equal-frequency degenerate case has no positive metric"
  - "Araki-Hepp-Ruelle cluster theorem / Osterwalder-Schrader -- exponential clustering at rate = the mass gap (the strip-width = gap mechanism, all-orders / axiomatic)"
---

# W179 -- the QFT C-operator generator Q1(k) and the all-orders question

## 0. Role, and the one object

**The one object.** The INTERACTING C-operator itself. W132 reduced keep-and-grade unitarity
**without remainder** to its existence; W169 built it perturbatively **through Q2 in QM** (finite-dof
Fock): it EXISTS for generic / incommensurate mass ratios (and, in the DISCRETE reading, for the
Stelle massless-graviton + massive-ghost spectrum, because `1 != n*0` for a level spacing) and
OBSTRUCTS on a measure-zero commensurate-resonance lattice. W169 explicitly **flagged, did not
resolve**, two gaps: (a) the QFT generator carries `1/sqrt(k^2+m^2)` energy denominators (W54 -> a
**non-local** Hermitian partner); (b) all-orders convergence is open. W172 sharpened (a): the C exists
non-locally (kernel `~e^{-m|x|}`, strip-width `m`) **unless** dynamical PT-breaking (an on-shell ghost
width, W51). This team **extends the construction** to the QFT generator and the all-orders question.

Five personas ran inline, sequentially, single context. Deterministic test
`tests/W179_c_operator_allorders_qft.py`, **23/23, exit 0**, positive controls first.

## 1. Construction forks (GEOMETER-VS-PHYSICS-OBJECTS.md discipline)

| Object | Constructions in play | Handling |
|---|---|---|
| **The generator `Q`** | (i) W169's DISCRETE `Q_{mn} = source/(E_m - E_n)` (Fock levels); (ii) the QFT `Q(k)` = momentum-space kernel with CONTINUUM energy denominators | we lift (i) to (ii); the lift IS the result |
| **The energy denominator** | discrete gap `E_m - E_n` vs continuum `D(k1,k2) = om2(k1+k2) - om1(k1) - om1(k2)` | the discrete degeneracy `E_m = E_n` lifts to the on-shell zero `D = 0` |
| **"The generator exists"** | (secular) no source on the degenerate block; (QFT) no on-shell real zero of `D` + bounded non-local kernel | both named; the QFT one is the load-bearing lift |
| **The mass data** | discrete commensurate/incommensurate ratio vs continuum ABOVE/BELOW the two-body decay threshold | the whole verdict is a fork ON this axis, reorganized by the lift |
| **"Bounded"** | naive multiplication-operator boundedness vs W172's bounded-NON-LOCAL (strip-width = gap, `e^{-m|x|}`) | we use the W172 sense: no on-shell pole + strip = gap; the UV growth is the inherited renormalization structure, orthogonal |

**The one fork this build turns on (named, not defaulted):** *does W169's discrete secular
obstruction lift to a commensurate-ratio condition, or to a kinematic decay-threshold condition, in
the continuum?* We show it is the **latter**, and that this **reorganizes** the verdict for the
massless-graviton Stelle spectrum.

## 2. Persona 1 -- PT-QFT / C-operator specialist: the QFT generator Q1(k)

In QFT the cross-vertex `A` (Krein-odd, anti-Hermitian; the QFT face of W169's
`A = (a1)^2 a2^dag - h.c.`, two physical quanta `<->` one ghost quantum, coupling `g`) makes W169's
leading equation `[H0, Q1] = -2A` an **elementwise division by a continuum energy denominator**. A
term `a1(k1) a1(k2) a2^dag(k3)` with momentum conservation `k3 = k1 + k2` shifts the free energy by
`om2(k3) - om1(k1) - om1(k2)`, so

>  **`Q1` kernel:  `q(k1, k2) = -2 g / D(k1, k2)`,  `D(k1, k2) = om2(k1 + k2) - om1(k1) - om1(k2)`,  `om_i(k) = sqrt(k^2 + m_i^2)`.**

This is **exactly** the W54 non-local structure (the `1/sqrt(k^2+m^2)` denominators, now dressed by
the vertex). W169's secular condition -- *no source between DEGENERATE states `E_m = E_n`* -- lifts to:
**`D` has no real on-shell zero**. A real zero of `D` is a continuum degeneracy connected by the
vertex = the QFT obstruction (test Q1-1, Q1-2).

**The discriminant is the two-body decay threshold (the headline).** `D(k1,k2) = 0` with
`k1 + k2 = K` means `om2(K) = om1(k1) + om1(k2)`: the ghost energy equals two physical energies at the
same total momentum = **the ghost can decay into two physical quanta**. The maximum of `D` over the
split at fixed `K` is at `k1 = k2 = K/2`, giving `sup D(K) = sqrt(K^2 + m2^2) - sqrt(K^2 + 4 m1^2)`,
which is `<= 0` for all `K` **iff** `m2 <= 2 m1` (test Q1-3, exact). Symbolically, in the ghost rest
frame `D(k, -k) = 0` at `k^2 = m_ghost^2/4 - m_phys^2`, a real momentum **iff `m_ghost > 2 m_phys`**
(test Q1-4). So:

>  **On-shell zero of `D`  `<=>`  `m_ghost >= 2 m_phys`  (the two-body decay threshold).**

This is **W169's discrete `2:1` resonance** (`w_ghost = 2 w_phys`, the Q1 obstruction) **lifted to the
continuum**. The discrete Poincare resonance becomes a kinematic decay threshold.

## 3. Persona 2 -- functional-analysis specialist: boundedness of the sub-threshold non-local kernel

**Sub-threshold (`m_ghost < 2 m_phys`): the generator EXISTS as a bounded non-local operator.** `D` is
strictly one-signed (test Q1-1: `max D < 0`), so `1/D` has **no on-shell pole**; on any compact
momentum region `|D|` is bounded below (test Q2-1). The non-locality is exactly W54's: continue `D` to
complex `k` and the nearest singularity is the branch point of `1/om_i` at `k = +-i m_i` -- the
**strip width is the mass gap** (test Q2-2: the `k^2`-series radius `= m^2`), so the position-space
kernel decays `~e^{-m|x|}` (test Q2-3: an explicit FT of the reduced symbol has a negative log-tail
slope). This is precisely W172's **bounded, strip-width-`m`, survivable** non-locality: a similarity
`rho` with `eta_+ = rho^dag rho` maps the graded theory to a **non-local but self-adjoint** Hermitian
Hamiltonian with real spectrum. So the honest QFT sense of *"the non-local Hermitian partner exists
and is bounded"* is met **sub-threshold**. (The large-`|k|` smallness of `D`, giving the kernel a UV
growth, is the standard renormalization structure of any QFT generator; it is orthogonal to the IR
resonance/existence question, which is the on-shell-zero test, and is inherited, not re-solved.)

**At/above threshold (`m_ghost >= 2 m_phys`): the naive Hermitian generator does NOT exist.** `D = 0`
on a real codimension-1 surface (test Q1-2: sign change), so `1/D` has an on-shell pole. There is no
bounded Hermitian generator; resolving the pole (`i epsilon` / resummation) is exactly the dynamical
question of Section 5.

## 4. Persona 3 -- resummation specialist: the all-orders question

**Sub-threshold: CONVERGENT-PLAUSIBLE.** Every order-`n` generator symbol is a rational function of
the constituent one-particle energies `om_i(k_j)` (W54/W97): the denominators are **sums of the same
positive energies** minus at most one ghost energy, and their **only** singularities are the branch
points `k = +-i m_i`. No order introduces a singularity closer to the real axis than the gap, so the
**analyticity strip = the mass gap at EVERY order** -- the W97 mass-scale-protection mechanism, the
same one that makes exponential clustering (rate = mass gap) an all-orders fact in a massive QFT (test
Q5-1: the sub-threshold `n`-body denominators stay clear of zero by the margin `2 m1 - m2 > 0`). With
the denominators bounded below by a positive `D0` and a **bounded renormalized vertex** `g`, the
order-`n` generator is majorized by `~(g/D0)^n`, a geometric series with **finite radius `g < D0`
set by the gap** (test Q5-2). So the all-orders C-operator is **convergent-plausible** for a
sub-threshold (mass-split, both massive) spectrum -- an asymptotic-vs-convergent upgrade of W169's
"exists through Q2", conditional on the inherited UV/renormalization control.

**Above threshold: DIVERGES / OBSTRUCTS.** The on-shell denominator vanishes already at Q1 and every
higher order re-uses the **same** vanishing decay denominator (the ghost sits on the two-particle
surface at every order). The majorant's `D0 -> 0`, the radius `-> 0`, the series does not resum into a
positive C-metric (test Q5-3). The pole goes complex = PT broken.

## 5. Persona 4 -- symbolic/numerical engineer + Persona 5 adversary: the Stelle case, the first loop, and the honest bound

**The Stelle spectrum is the reorganization (tests Q3-1..3).** W169's discrete reading called the
Stelle spectrum (`w_phys = 0`, `w_ghost = 1`) OPERATIVE because `1 != n * 0` (a massive ghost is not
an integer multiple of a zero level spacing) -- reproduced exactly here (Q3-1: discrete
`secular_Q1 = secular_Q2 = 0`). **But the continuum lift OBSTRUCTS.** With `m_phys = 0` the
two-graviton continuum runs from `0` to `inf`, so a ghost of **any** mass `M > 0` is **above** the
(zero) threshold -- embedded in the massless two-graviton continuum -- and `D` develops a real on-shell
zero for every `M` (Q3-2: sign change for `M in {0.3, 1, 3, 10}`). The **same** Stelle spectrum is
OPERATIVE discretely and OBSTRUCTS in the continuum (Q3-3). **The QM non-resonance is a discrete
accident that does not survive the continuum for a massless lighter field.** Physically this is the
well-known instability of the Stelle ghost: a massive spin-2 ghost above a massless graviton always
has an open two-graviton channel.

**The first loop confirms it dynamically (tests Q4-1..3).** The `g^2` correction (the ghost
self-energy, the `[Q1, S]`-type loop) acquires an **imaginary part** exactly when the decay channel
opens: a toy two-body phase space `integral dk delta(M - 2 om1(k))` is **zero below threshold** (Q4-1)
and **positive above** (Q4-2), and positive for the massless-graviton Stelle case (Q4-3). This is the
**W51 anti-damping width** / **W172 PT-breaking handle**, now located at the first loop order as the
`Im` part of the `Q2` generator's source. Sub-threshold there is no width and the loop-order
obstruction is absent.

**Adversary, at full strength, then bounded.** *Steelman OBSTRUCTS:* the physically relevant GU
spectrum is Stelle -- massless graviton + massive ghost -- and it is **above threshold**, so the QFT
Q1 generator has an on-shell pole, the ghost has a width, PT breaks, no positive C-metric exists, and
the all-orders C-operator does not converge. The discrete "mass-split => OPERATIVE" reading of W169 was
a level-spacing accident; in the continuum the ghost is embedded, not gapped. This is a real,
sign-definite, loop-order kill of the graded-positivity reading **for the massless-graviton case**.
*Bounding it (honestly):* (1) the obstruction is **not** generic to all keep-and-grade spectra -- a
**sub-threshold** (both-massive, `m_ghost < 2 m_phys`) spectrum has no on-shell zero, a bounded
non-local generator, and a convergent-plausible series (negative control NEG1: deep sub-threshold stays
bounded, zero width; NEG2: the pole switches on **exactly** at ratio `2`). (2) Whether the
above-threshold pole reaches the **physical sheet** (a true kill) versus a benign **second-sheet
resonance** is **UNDECIDED at this rigor** -- it is H59's open W48 self-energy, inherited unchanged.
"Width nonzero" (channel open) is what Part 4 shows; "physical-sheet complex pair" is the standing open
computation. So this is **OBSTRUCTS-AT-THRESHOLD as an on-shell-pole / existence-of-the-naive-generator
statement**, coinciding with W172's dynamical handle -- not a proven physical-sheet no-go.

## 6. Verdict

**PARTIAL / OBSTRUCTS-AT-THRESHOLD.**

- **QFT `Q1(k)`:** kernel `-2g/D`, `D = om2(k1+k2) - om1(k1) - om1(k2)`; on-shell zero
  `<=> m_ghost >= 2 m_phys` (W169's discrete `2:1` resonance lifted to the two-particle **decay
  threshold**).
- **Sub-threshold (`m_ghost < 2 m_phys`): EXISTS.** Bounded non-local kernel, strip width = the mass
  gap, position kernel `~e^{-m|x|}` (W54) -- a bounded non-local Hermitian partner (the W172 sense).
  All-orders **CONVERGENT-PLAUSIBLE** (strip = gap at every order, geometric majorant, radius set by
  the gap), conditional on the inherited UV/renormalization control.
- **At/above threshold (`m_ghost >= 2 m_phys`): OBSTRUCTS.** Real on-shell pole = anti-damping width
  `Im Sigma > 0` (W51) = spontaneous PT-breaking (W172) = no positive C-metric; all-orders diverges.
- **Stelle spectrum (massless graviton + massive ghost): ABOVE threshold for every `M > 0`** (embedded
  in the massless two-graviton continuum) -> the continuum lift **OBSTRUCTS**, **sharpening** W169's
  discrete "mass-split => OPERATIVE" reading.

**Effect on bar (b).** The QFT lift **replaces** W169's commensurate-ratio sub-bit with the cleaner
kinematic sub-bit: **is the ghost BELOW or ABOVE the two-physical-particle decay threshold?**
- **Below threshold (both massive, `m_ghost < 2 m_phys`) ->** the QFT C-operator exists as a bounded
  non-local object, all-orders convergent-plausible, **bar (b) clears** (perturbatively, priced
  non-local).
- **Above threshold (incl. the massless-graviton Stelle spectrum) ->** the QFT `Q1` generator has an
  on-shell pole; this **coincides exactly with W172's one live dynamical no-go** (the ghost decay width
  = H59's W48 self-energy). The C-operator's QFT existence is **CONDITIONAL-ON-SUB-THRESHOLD**
  (PT-unbroken), consistent with W172; whether the Stelle pole is physical-sheet (kill) or second-sheet
  (survivable resonance) is the **inherited open** H59 object.

W179's contribution is to carry W169's construction from QM to the QFT generator and to **relocate the
obstruction**: not a measure-zero commensurate-ratio lattice, but a codimension-one **decay threshold**
that the physically relevant massless-graviton spectrum sits **above**, converging the C-operator
question onto the **same** dynamical PT-stability bit reached from the gravity side (W51), the matter
side (W132), and W172.

**H59 remains OPEN.** No canon / RESEARCH-STATUS / claim-status / verdict / posture change. Status
changes only via the runbook.

## 7. What this does NOT do

- No all-orders **proof**: the strip-protection (W97) + geometric-majorant convergence is a
  STRONG-ARGUMENT conditional on a bounded renormalized vertex; the UV/renormalization structure is
  inherited, not re-solved.
- No resolution of the **physical-sheet vs second-sheet** fate of the above-threshold ghost pole --
  that is H59's open W48 self-energy; W179 shows the channel is open (nonzero width), which is
  necessary but not sufficient for a physical-sheet kill.
- No full spin-2 tensor numerators (W134 owns those); the `A`-vertex model is the minimal cubic stand-in.
- No claim that keep-and-grade is dead: a sub-threshold (both-massive) spectrum is on the EXISTS side;
  the reduction is that GU's **Stelle** spectrum is above threshold and inherits the W172 dynamical no-go.

**Artifacts:** this file + `tests/W179_c_operator_allorders_qft.py` (23/23, exit 0).
