---
artifact_type: exploration
status: "exploration (W169 / TEAM C-OP-CONSTRUCT; 5 inline personas; one deterministic test 23/23 exit 0; the interacting C-operator built order by order THROUGH Q2 -- the first genuine loop order -- for the minimal GU keep-and-grade model)"
created: 2026-07-14
label: W169
hypothesis: "Does the perturbative C-operator (C = e^Q P, Q = gQ1 + g^2 Q2 + ...) for GU's interacting keep-and-grade theory EXIST and converge, or does the construction OBSTRUCT at the first loop order Q2? = is the Krein grading physically OPERATIVE?"
verdict: "NARROWED. Q1 EXISTS (reproduces W49). Q2 EXISTS for the minimal single-odd-vertex model (=0 exactly) and for the full vertex at GENERIC/incommensurate physical:ghost mass ratios -- Hermitian, finite, positive metric, and Q2 drives the pseudo-Hermiticity residual from O(g^2) to O(g^3), so C EXISTS-PERTURBATIVELY = OPERATIVE there (this INCLUDES the Stelle massless-graviton + massive-ghost spectrum). The construction OBSTRUCTS-AT-Q2 on a measure-zero lattice of COMMENSURATE (resonant) mass ratios: w_ghost = 2 w_phys obstructs already at Q1, but w_ghost = w_phys (EQUAL mass = the conformal / 1/p^4 double-pole = Bender-Mannheim's PU equal-frequency case) and w_ghost = 3 w_phys obstruct FIRST at Q2 -- invisible to leading order, driven by the physical graviton self-coupling -- with Q2 diverging ~ 1/(w_ghost - w_phys) on approach. bar (b) is thereby REDUCED WITHOUT REMAINDER to one sub-bit: does GU's linearized 4th-order operator sit at the equal-mass/conformal (degenerate, resonant -> NOT-OPERATIVE -> tachyon is the false-vacuum record-accretion engine, W163/W166) locus, or at the mass-split/incommensurate (OPERATIVE -> tachyon spurious, ghost is a physical record, bar (b) clears) locus?"
grade: "EXACT for the order-by-order equations [H0,Q1]=-2A and [H0,Q2]=[Q1,S] (BCH, two lines, machine-checked) and for the secular/degenerate-block obstruction criterion. PROVEN-in-QM (finite dof, self-validating numerics to 1e-9..1e-14) for: Q1/Q2 existence and Hermiticity off resonance, the O(g^2)->O(g^3) residual improvement (log-log slopes 2.01, 3.00), metric positivity, and the Q2-first obstruction at the equal-mass and 3:1 loci (secular_Q1=0, secular_Q2=420, 153). STRUCTURAL for the QFT lift and for the identification of the equal-mass locus with GU's conformal/double-pole member. NOT an all-orders proof; NOT a QFT amplitude. Inherited, NOT re-opened: the QFT non-locality of the generator (W49/W54). Test: tests/W169_c_operator_perturbative_construction.py 23/23 exit 0, with positive controls (2x2 Bender-Brody-Jones exact C-operator; Q1 reproduced) and a negative control (incommensurate/irrational ratio stays obstruction-free). NO canon / RESEARCH-STATUS / claim-status / verdict / posture change. H59 remains OPEN."
depends_on:
  - explorations/path2-branchB-pt-c-operator-2026-07-11.md
  - explorations/W132-graded-optical-theorem-physical-subspace-2026-07-14.md
  - canon/ghost-parity-krein-synthesis.md
  - tests/W49_path2_B_c_operator.py
  - tests/W121_path2_target3_hypothesis_hardening.py
  - tests/W132_graded_optical_theorem_physical_subspace.py
  - GEOMETER-VS-PHYSICS-OBJECTS.md
scripts:
  - tests/W169_c_operator_perturbative_construction.py
external_refs:
  - "Bender, Brody & Jones, Complex extension of quantum mechanics, PRL 89 (2002) 270401; and Ann. Phys. 213 (2004) -- the C = e^Q P construction, Q odd in the coupling for an anti-Hermitian PT interaction"
  - "Mostafazadeh, Pseudo-Hermiticity versus PT symmetry, JMP 43 (2002) 205 & 2814 & 3944 -- the positive metric eta_+ = eta C, order-by-order construction, and the pseudo-Hermiticity equation"
  - "Bender & Mannheim, No-ghost theorem for the fourth-order derivative Pais-Uhlenbeck oscillator model, PRL 100 (2008) 110402 -- real spectrum + positive metric for unequal frequencies; NON-diagonalizable Jordan block (no positive metric) at EQUAL frequency"
  - "Mannheim, Comprehensive solution to the Pais-Uhlenbeck oscillator, and PT-symmetry-based unitarity of conformal (Weyl) gravity -- the 1/p^4 double-pole is the equal-frequency limit"
  - "Stelle, Renormalization of higher-derivative quantum gravity, PRD 16 (1977) 953 -- the 4th-order theory, massless graviton + massive spin-2 ghost"
---

# W169 -- the perturbative C-operator through Q2 (the first genuine loop order)

## 0. Role, and the one object

The 2026-07-14 landscape and W132 reduced keep-and-grade unitarity **without remainder** to a
single question: does the interacting **C-operator** exist? There is no independent
physical-subspace optical theorem to hope for (W132: the free-grading subspace S-matrix obeys
`A^dag A = P_+ + B^dag B`, an expansion, and the odd cuts are computed nonzero); the only
unitarity resource is the positive C-metric `eta_+ = eta_0 C`. Equivalently: is the Krein grading
physically **OPERATIVE** = does `[P_ghost, S] = 0` survive interactions = does the C-operator exist
at loop level. The keystone chain (W157-W160, W167) reduced the tachyon **sign** to exactly this
one bit: OPERATIVE -> the tachyon is spurious and the ghost is a physical record, bar (b) clears;
NOT-OPERATIVE (the graded positivity is a redundancy, not a record) -> the tachyon is physical and
is the false-vacuum record-accretion engine (W163/W166), bar (b) re-posed.

W49 / branch B built the C-operator's **first** interacting correction `Q1` and stopped there,
explicitly flagging the gap: *"Only the first interacting order of Q was computed ...
convergence/all-orders is not established here."* This team computes the **next** order `Q2` -- the
first genuinely loop/interacting order, where an obstruction can bite -- for the minimal GU
keep-and-grade model, using the standard PT-QFT method (Bender-Brody-Jones / Mostafazadeh
`C = e^Q P`), never before run natively for GU.

Five personas ran inline, sequentially, single context. Deterministic test
`tests/W169_c_operator_perturbative_construction.py`, **23/23, exit 0**.

## 1. Construction forks (GEOMETER-VS-PHYSICS-OBJECTS.md discipline)

| Object | Constructions in play | Handling |
|---|---|---|
| **Physical inner product** | (i) the positive **C-metric** `eta_+ = e^{-Q}` (keep-and-grade: grade the ghost); (ii) a positive-Hilbert-subspace projection (removes the ghost) | We build (i). Projection is the wrong object for this branch and is not used. |
| **The Hamiltonian** | PT/Krein-pseudo-Hermitian `H` (`H != H^dag`) vs its Dirac-Hermitian similarity image `h = e^{-Q/2} H e^{Q/2}` | Both named; the QFT locality of `h` is the inherited W49/W54 crux, not re-opened here. |
| **The vertex** | admissible = Krein-Hermitian `eta_0 V eta_0 = V^dag`, splitting `V = A + S` | `A` Krein-odd + anti-Herm (sources Q1); `S` Krein-even + Herm (sources Q2). THIS SPLIT is the result's engine. |
| **The mass ratio** | generic / incommensurate vs commensurate / resonant `w_ghost : w_phys` | The whole verdict is a fork ON this axis. |

## 2. Persona 1 -- PT-QFT / Bender-Mannheim specialist: the order-by-order equations

For `H = H0 + g V` with `V` admissible (Krein-Hermitian, `eta_0 V eta_0 = V^dag`), decompose `V`
by ghost-number parity into `V = A + S` where `eta_0 A eta_0 = -A = A^dag` (Krein-**odd**,
**anti**-Hermitian) and `eta_0 S eta_0 = +S = S^dag` (Krein-**even**, **Hermitian**). This is
forced: the only genuinely non-Hermitian admissible piece is the Krein-odd one. Writing
`Q = g Q1 + g^2 Q2 + ...` (Hermitian) and expanding the pseudo-Hermiticity condition
`e^{-Q} H e^{Q} = H^dag` by Baker-Campbell-Hausdorff gives, **exactly** (each verified to machine
precision in-test):

>  **order `g^1`:  `[H0, Q1] = -2 A`**
>  **order `g^2`:  `[H0, Q2] =  [Q1, S]`**

Read off three structural facts, before any model:

1. **Only `A` sources `Q1`.** The Hermitian part `S` drops out of leading order entirely.
2. **`S` sources `Q2`, through `[Q1, S]`.** A theory with a purely Krein-odd vertex (`S = 0`) has
   `[Q1, S] = 0`, hence `Q2 = 0` **identically** -- the Bender-Brody-Jones "Q is odd in the
   coupling" result, reproduced. So for a single anti-Hermitian vertex the first genuine correction
   past `Q1` is `Q3`, and there is **no** obstruction at `g^2`.
3. **Solvability = the secular condition.** In the `H0` eigenbasis each equation is
   `X_{mn} = source_{mn} / (E_m - E_n)`, which **exists iff** the source has **no matrix element
   between degenerate states** (`E_m = E_n`). A nonzero degenerate-block source is an
   **obstruction**: there is no Hermitian generator at that order. `Q2` is Hermitian whenever it
   exists (`[Q1,S]` is anti-Hermitian, divided by the antisymmetric `E_m - E_n`).

The obstruction is therefore a **small-denominator / Poincare resonance** phenomenon, living on the
commensurate frequency ratios where the free spectrum is degenerate and the interaction connects
the degenerate states.

## 3. Persona 2 -- Krein / indefinite-metric specialist: positivity and what is graded

The fundamental Krein metric is `eta_0 = (-1)^{N_ghost}` (indefinite: `+1` on even ghost number,
`-1` on odd), and `[H0, eta_0] = 0` -- the free ghost is **graded, not removed** (test PC2d). The
free theory is already `eta_0`-pseudo-Hermitian; the C-operator question is whether a **positive**
metric `eta_+ = eta_0 C` (equivalently `eta_+ = e^{-Q} > 0` with `C = eta_0^{-1} eta_+`,
`C^2 = 1`) also intertwines `H` and `H^dag`. Reusing the W121/W132 meaning of positivity: `C^2 = 1`
is guaranteed to all orders by `Q` Hermitian **and** Krein-odd (`eta_0 Q eta_0 = -Q`), which the
construction delivers (`Q1` verified Krein-odd, test Q1c). Positivity of `eta_+ = e^{-Q}` is then
the surviving content, and it is what fails at a resonance: as the mass gap closes the generator
`Q2 ~ 1/(w_ghost - w_phys)` blows up, `e^{-Q}` leaves the perturbative ball, and there is no order
at which a Hermitian, positive, C-normalizing metric exists. This is exactly the Krein content of
Bender-Mannheim's Pais-Uhlenbeck no-ghost theorem: unequal frequencies -> real spectrum **and**
positive metric; equal frequency -> a non-diagonalizable Jordan block with **no** positive metric.

## 4. Persona 3 -- GU-model specialist: the minimal keep-and-grade model

Two Krein modes -- **physical** graviton mode (1, frequency `w_phys`, norm `+`) and **ghost** mode
(2, frequency `w_ghost`, norm `-`) -- with `H0 = w_phys N1 + w_ghost N2` (Hermitian, bounded below,
**real** spectrum, **indefinite** norm: the keep-and-grade picture of real masses with a graded
ghost). Cubic vertices, all admissible (Krein-Hermitian):

```
A     = (a1)^2 a2^dag - (a1^dag)^2 a2         Krein-odd,  anti-Herm   physical<->ghost (PT part)
Smin  = a1 (a2^dag)^2 + a1^dag (a2)^2         Krein-even, Herm        physical<->ghost (ordinary)
Sgrav = a1^dag a1^dag a1 + a1^dag a1 a1       Krein-even, Herm        PHYSICAL self-coupling
```

`Sgrav` is not optional: every real gravity theory has graviton self-interactions, and it is the
piece that makes `Q2` a **genuine** test, because a Krein-even Hermitian vertex first enters the
C-operator at `O(g^2)`. This is the minimal stand-in for the 4th-order (Stelle) coupled
physical-graviton / ghost sector with the record/RS matter grading carried by `eta_0`.

The resonance structure of this model (net `(Delta n1, Delta n2)` shifts, degenerate when
`w_phys Delta n1 + w_ghost Delta n2 = 0`):

- `A` shifts `(-2, +1)` / `(+2, -1)`: degenerate at **`w_ghost = 2 w_phys`** -> **Q1** obstruction.
- `Sgrav` shifts `(+-1, 0)`; composed with `A` in `[Q1, Sgrav]` gives `(-+1, +-1)` and `(-+3, +-1)`:
  degenerate at **`w_ghost = w_phys`** and **`w_ghost = 3 w_phys`** -> **Q2** obstruction, and
  `w_phys` (leading order) is clean there.

## 5. Persona 4 -- symbolic engineer: the computation (tests/W169..., 23/23, exit 0)

Deterministic, numpy only, 64-dim two-mode Fock space. **Positive controls first**: the exact 2x2
Bender-Brody-Jones C-operator reproduced (`C^2 = 1`, `[C,H] = 0`, real spectrum, PC1); the leading
GU equation `[H0, Q1] = -2A` solved to `7e-14` with `Q1` Hermitian and Krein-odd (Q1a-c,
reproducing W49). Then:

**`Q2` = 0 for the pure-odd vertex.** With `S = 0`, source `[Q1, S] = 0` exactly -> `Q2 = 0`
(Q2a). No `g^2` obstruction for a single anti-Hermitian vertex.

**`Q2` EXISTS at generic masses** (`w_phys = 1.0, w_ghost = 1.3`, full vertex): degenerate-block
source `= 0` (Q2b1), `Q2` solves its equation to `1e-12` (Q2b2) and is Hermitian (Q2b3). It does
its job: the pseudo-Hermiticity residual `||eta_+ H - H^dag eta_+||` has log-log slope **2.01**
with `Q1` alone (`O(g^2)`) and **3.00** once `Q2` is included (`O(g^3)`) -- `Q2` cancels the
`O(g^2)` non-Hermiticity (Q2b4-5) -- and the positive metric `eta_+ = e^{-(gQ1 + g^2 Q2)}` is
positive-definite (Q2b6).

**The obstruction map** (Q2c), degenerate-block sources `secular_Q1`, `secular_Q2`:

| `w_phys` | `w_ghost` | `secular_Q1` | `secular_Q2` | status |
|---|---|---|---|---|
| 1.0 | 1.3 | 0 | 0 | **EXISTS through Q2** (generic) |
| 1.0 | sqrt 2 | 0 | 0 | **EXISTS through Q2** (irrational; negative control) |
| **0.0** | **1.0** | 0 | 0 | **EXISTS through Q2** (Stelle: massless graviton + massive ghost) |
| 1.0 | 2.0 | 34.3 | 0 | OBSTRUCTS **at Q1** (A-vertex 2:1 resonance) |
| 1.0 | **1.0** | 0 | **420** | **OBSTRUCTS at Q2** (equal mass = conformal / double-pole) |
| 1.0 | 3.0 | 0 | **153** | **OBSTRUCTS at Q2** (3:1 resonance) |

and the approach: `max|Q2|` grows `141 -> 1732` as the gap `w_ghost - w_phys` closes `+0.40 ->
+0.02`, i.e. `Q2 ~ 1/(w_ghost - w_phys)` diverges into the equal-mass obstruction (Q2c6). The
equal-mass and 3:1 rows are the headline: `secular_Q1 = 0` (leading order is clean) while
`secular_Q2 != 0` -- a genuine **loop-order** obstruction, invisible to `Q1`, driven by the
physical self-coupling `Sgrav`.

## 6. Persona 5 -- adversarial skeptic: steelman OBSTRUCTS-AT-Q2, then bound it

**Steelman (at full strength).** Do not declare existence from `Q1`: `Q1` sees only the
anti-Hermitian cross-vertex `A`, and `A`'s single resonance (2:1) is a leading-order artifact. The
loop order is where the physical graviton self-coupling first enters the metric, and it obstructs
at `w_ghost = w_phys` -- **the equal-mass locus is exactly GU's conformal / pure-Weyl / `1/p^4`
double-pole member** (the "conformal member of the quadratic class" the ghost-parity synthesis
already flags, and Bender-Mannheim's equal-frequency Pais-Uhlenbeck non-unitary case). A 4th-order
kinetic term built from `Weyl^2` alone has a **double** pole at `p^2 = 0` = equal frequency =
degenerate = ON the obstruction. If GU's linearized operator is conformal-type, the C-operator does
not exist even perturbatively at the first loop order -> **NOT-OPERATIVE** -> the tachyon is the
false-vacuum record-accretion engine, bar (b) re-posed. This is a real, sign-definite,
loop-order kill of the graded-positivity reading, not a toy artifact.

**Bounding it (each answered by the computation).**
1. *"The obstruction is generic."* NO -- it is measure-zero. Off the commensurate lattice
   (`w_ghost / w_phys` irrational or non-integer-ratio) `secular_Q1 = secular_Q2 = 0` and `Q2`
   exists (two negative controls). The resonant set is a lattice of rational ratios.
2. *"Stelle gravity is on the bad locus."* NO -- generic Stelle is **massless graviton
   (`w_phys -> 0`) + massive ghost (`w_ghost = M`)**, which is non-resonant (`M != n * 0`); the
   `w_phys = 0, w_ghost = 1` row EXISTS through `Q2`. The mass-split spectrum is OPERATIVE-perturbatively.
3. *"Existence is proven."* NO -- it is QM and perturbative only, and the inherited W49/W54 result
   still applies in the EXISTS case: the QFT generator carries `1/sqrt(k^2 + m^2)` energy
   denominators, so the Dirac-Hermitian partner is **non-local**. OPERATIVE here means
   "perturbatively unitary at the price of a non-local Hermitian image," not "healthy and local."

**Skeptic's residue (honest).** Which locus GU actually occupies is not settled by this method; the
equal-mass/conformal double-pole is a live possibility and would flip the verdict to NOT-OPERATIVE.
The crossover VALUES (2:1 at Q1, 1:1 and 3:1 at Q2) are specific to the minimal vertex set; a
richer vertex moves the lattice but not the existence of the two regimes or the sign of the secular
obstruction.

## 7. Verdict

**NARROWED.**

- **`Q1`: EXISTS** (reproduces W49). Hermitian, Krein-odd, `C^2 = 1`.
- **`Q2`: EXISTS-PERTURBATIVELY = OPERATIVE** for the pure-odd vertex (`= 0` exactly) and for the
  full vertex at **generic / incommensurate** mass ratios, **including the Stelle massless-graviton
  + massive-ghost spectrum**. Hermitian, finite, positive metric, and it drives the
  pseudo-Hermiticity residual from `O(g^2)` to `O(g^3)`.
- **`Q2`: OBSTRUCTS-AT-Q2 = NOT-OPERATIVE** on the measure-zero **commensurate-resonance** lattice.
  `w_ghost = 2 w_phys` obstructs already at `Q1`; **`w_ghost = w_phys` (equal mass = conformal /
  `1/p^4` double-pole = Bender-Mannheim PU)** and `w_ghost = 3 w_phys` obstruct **first at `Q2`**,
  invisible to leading order, driven by the physical self-coupling, with `Q2` diverging on approach.

**Effect on bar (b).** The interacting-C-operator question is reduced **without remainder** to one
sub-bit: **is GU's linearized 4th-order operator the equal-mass / conformal (degenerate, resonant)
case or the mass-split / incommensurate case?**
- **Mass-split / incommensurate -> OPERATIVE-perturbatively ->** the tachyon is spurious, the ghost
  is a physical record, **bar (b) clears** (perturbatively, and modulo the inherited QFT
  non-locality of the Hermitian partner).
- **Equal-mass / conformal double-pole -> OBSTRUCTS-AT-Q2 -> NOT-OPERATIVE ->** the graded
  positivity is a redundancy, not a record; the tachyon is physical and is the false-vacuum
  record-accretion engine (W163/W166), **bar (b) re-posed**.

This is the identical bit reached from the gravity side (quadratic-gravity dynamics realizing
`[P_ghost, S] = 0`, the ghost-parity synthesis open condition), the matter side (W132: the only
unitarity resource is the C-operator), and the time-as-finality "records vs redundancy" reading.
W169's contribution is to locate it precisely: **not** a generic feature of the interacting theory,
but a resonance condition on the physical:ghost mass ratio, with the conformal double-pole as the
one distinguished obstructing point that first bites at the loop order `Q2`.

**H59 remains OPEN.** No canon / RESEARCH-STATUS / claim-status / verdict / posture change. Status
changes only via the runbook.

## 8. What this does NOT do

- No all-orders proof: only `Q1` and `Q2` are computed; `Q3+` and convergence (asymptotic vs
  convergent) are not established.
- No QFT amplitude and no resolution of the inherited **non-locality** of the Hermitian partner
  (W49/W54); the EXISTS verdict is "perturbatively unitary in QM," not "local and healthy."
- No determination of which locus GU actually occupies -- that is the reduced sub-bit, and it lives
  in GU's linearized 4th-order operator (the W165/W167 alpha+beta sign object), not in this method.
- No change to the keystone chain's tachyon sign, only a sharper statement of the pivot it turns on.

**Artifacts:** this file + `tests/W169_c_operator_perturbative_construction.py` (23/23, exit 0).
