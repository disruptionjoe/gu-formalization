---
artifact_type: exploration
status: exploration
created: 2026-07-11
title: "H9 -- does GU's Bach (Weyl^2 / 4-derivative) gravity sector instantiate the Bateman-Turok ghost-free completion? HONEST OUTCOME: REDUCE (not clear, not fail). The Bateman-Turok clean ghost-parity/O(1,1)/tree-positivity mechanism requires a NON-degenerate MASSIVE ghost (two distinct poles); GU's established (H1) gravity operator is pure Bach = box^2 = the COINCIDENT-POLE degenerate limit, exactly the Pais-Uhlenbeck equal/zero-frequency Jordan-block case where the two-field diagonalization fails and the ghost parity is non-unique (gravity-side image of R1's Jordan-boundary theorem and R3's K-balance). The kinematic Z2 ([P,S_free]=0, P a Krein isometry) genuinely holds, same grade as canon V2. Net: the Bach sector clears via Bateman-Turok ONLY IF GU's gravity is Stelle-type (R+Weyl^2, distinct massive ghost) rather than pure conformal Bach -- the SAME conformal-vs-Einstein / OQ2-A functional datum H1 already isolated. H9's gravity-side ghost frontier COLLAPSES ONTO H1's single named fork."
grade: "exploration / REDUCE (bounded, structural). Confidence moderate-high on the structural claim (partial-fraction degeneracy, PU Jordan block, commutant jump -- all exact sympy, exit 0). Confidence lower on the physics gloss (Mannheim has a contested viability program for the degenerate equal-frequency case; loop-level untested). No forbidden target imported."
depends_on:
  - tests/wave2/H9_ghost_parity_bach_sector.py
  - tests/wave1/H1_bach_flat_exact_vacua.py
  - canon/ghost-parity-krein-synthesis.md
  - explorations/big-swing-2026-07-06/BIG-SWING-CONFORMAL-CLASS-BLOCKED.md
  - explorations/big-swing-2026-07-06/R1-pu-pt-vs-ghost-parity.md
external_ref: "Bateman & Turok, 'Escape from Ostrogradsky via Hidden Ghost Parity', arXiv:2607.00096 (July 2026)"
scripts:
  - tests/wave2/H9_ghost_parity_bach_sector.py
---

# H9 -- Ghost-parity audit of GU's Bach (Weyl^2) gravity sector

## The decidable question

Bateman & Turok (arXiv:2607.00096) make a 4-derivative theory unitary by quantizing
on a Krein space: they **keep** the Ostrogradsky ghost but grade it by a hidden
**ghost parity P**, made explicit via a **two-field O(1,1) embedding** (one healthy
field + one distinct ghost field), and prove that a Krein-space generalized Born rule
gives **positive tree-level transition probabilities** -- provided the ghost parity is
a symmetry of the dynamics (`[P,S]=0`).

Wave 1 (`tests/wave1/H1_bach_flat_exact_vacua.py` + the D-thread) established that
GU's H-class pure-gravity / spin-2 section-EL **is the Bach operator**: on the
transverse-traceless sector `box^2 h = -4 Bach^(1)`. So GU's established gravity
kinetic operator is `box^2`.

H9 asks the sharp cascade-gate: **does that Bach `box^2` sector instantiate the
Bateman-Turok ghost-free completion?** This is the *gravity-side* dual of the
*matter-side* ghost-parity work already in canon; the gravity kinetic operator is
known (Weyl^2), so the free/kinematic structure is fully computable **without** GU's
unbuilt source action.

## What I computed (exact sympy, `tests/wave2/H9_ghost_parity_bach_sector.py`, exit 0)

**PART A -- the O(1,1) split needs a distinct ghost pole; Bach degenerates.**
The Bateman-Turok healthy/ghost O(1,1) structure is exactly the partial-fraction split
of a **massive** quadratic-gravity TT propagator:
`1/(box (box+m^2)) = (1/m^2)[1/box - 1/(box+m^2)]`, a **positive-residue** graviton pole
(`+1/m^2`) plus a **negative-residue** ghost pole (`-1/m^2`) -- the opposite-sign pair
is the O(1,1)/Krein two-field structure. Pure Bach / Weyl^2 = `1/box^2` is a **double
pole** (order 2), the coincident-pole `m -> 0` limit; the split coefficient `1/m^2`
**diverges**. GU's established (H1) operator sits exactly at this singular point.

**PART B -- Pais-Uhlenbeck: clean split <=> distinct frequencies.** The 4-derivative
operator's companion matrix is **diagonalizable** iff the two frequencies are distinct
(`(l^2+1)(l^2+4)`: four distinct eigenvalues `+-i, +-2i`, diagonalizable). The
**equal-frequency** case `(l^2+1)^2` and the **pure-Bach** case `l^4` are **non-
diagonalizable Jordan blocks**. So the two-field embedding degenerates precisely at the
Bach point -- the gravity-side statement of R1's Jordan-boundary nonexistence theorem
and Mannheim's equal-frequency wall.

**PART C -- ghost parity P: kinematic symmetry holds, uniqueness fails at Bach.**
`P = diag(+1,-1)` is a **Krein isometry** (`P^T eta P = eta`, `eta = diag(+1,-1)`) and
**commutes with the free action** (`[P,M_free]=0`): the kinematic `[P,S_free]=0` that
Bateman-Turok positivity needs **does hold at free level** -- but this is trivially true
for *any* O(1,1), and is the same grade as canon V2's Cartan-involution Z2 (residual 0).
At **distinct** masses the commutant of the mass matrix is 2-dimensional (diagonal only),
so P is essentially unique -- the physical/ghost split is canonical. At the **equal**
(Bach-analog) mass the commutant jumps to **4-dimensional** (all of gl(2)): *every* O(1,1)
rotation commutes, so **P is not singled out by the dynamics**. This is the gravity-side
image of R3's spectral sign-blindness: at GU's degenerate spectrum a definitizing
operator exists but is never *determined*.

**PART D -- adversarial: GU's Krein form is not literally Bateman-Turok's O(1,1).**
GU's matter Krein form is **O(96,96)** (the 192-dim self-dual triplet, so(9,5) Cartan
involution). Bateman-Turok's per-mode gravity ghost space is **O(1,1)** (one healthy +
one ghost spin-2 polarization). `96 != 1`: these are **different Krein spaces**. What is
shared is only the **Z2 grading of a balanced/neutral Krein form** -- an analogy at
kinematic grade, not an equality of spaces. The canon's V2 statement ("K equals the
ghost parity on the triplet") is about the *matter* O(96,96), and does **not** transport
to the *gravity* O(1,1) as an identity.

## Verdict: REDUCE (not CLEAR, not FAIL). Confidence moderate-high (structural).

- **Not cleared.** Bateman-Turok's clean ghost-parity / O(1,1) / tree-positivity
  mechanism requires a **non-degenerate massive** ghost (two distinct poles). GU's
  established gravity sector is pure Bach = `box^2` = the coincident-pole **degenerate**
  limit, exactly where the diagonalization fails (PART B) and the ghost parity is
  non-canonical (PART C). So the Bach sector does **not** simply "clear the ghost
  objection via Bateman-Turok."
- **Not newly failed.** The kinematic Z2 genuinely holds: P is a Krein isometry and
  commutes with the free action. The obstruction is **degeneracy + missing dynamics**,
  the same open condition canon already fences (R3 sustained x2) -- not a fresh
  contradiction that would sink the conformal/Bach reading.
- **The fork.** The Bach sector clears via Bateman-Turok **only if** GU's gravity is
  actually **Stelle-type** (`R + Weyl^2`, a *distinct massive* ghost), **not** pure
  conformal Bach. Adding an Einstein-Hilbert `box` term is exactly what turns `box^2`
  (double pole, degenerate) into `box(box+m^2)` (two simple poles, non-degenerate,
  Bateman-Turok-ready). Whether GU's action carries that term is the **conformal-vs-
  Einstein / OQ2-A functional** datum that H1 already isolated. **So H9's gravity-side
  ghost frontier collapses onto H1's single named fork.** The gravity ghost question,
  the matter generation-count question, and the OQ2-A functional choice are one fork
  seen three ways.

## Honest boundary (what I did NOT do)

- **Interacting `[P,S]=0` is untested.** GU supplies no built source action; only the
  free-level Z2 is checkable. This is the standing missing-source-action gap.
- **Loop-level positivity is untested** -- by me and (for GU) by anyone. Bateman-Turok
  prove **tree** level only; higher-derivative ghost theories historically fail at loops
  (complex ghost masses, optical-theorem violation). Even granting GU a massive Stelle
  ghost, tree positivity would not settle loop unitarity.
- **The Mannheim steelman.** Mannheim argues the equal-frequency / pure-conformal PU
  case is *still* viable via a specific limiting/PT construction. I did not refute that;
  I recorded that this program is exactly the R3-blocked one (the definitizing operator
  exists but is not dynamics-derived on GU's carrier), which is why the verdict is
  REDUCE and not CLEAR, and also why it is not FAIL.
- **Fiber/gauge terms** (`E_s^YM`, `E_s^theta`, ...) need the unbuilt full action; a
  pure-gravity vacuum plausibly zeroes them but this file does not close them.
- **The OQ2-A functional choice** (pure Bach vs `R + Weyl^2`) -- the decisive fork -- is
  named, not resolved.

## Re-ranking signal for the council

This result **raises the priority of the conformal-vs-Einstein fork** and should re-weight
the sibling hypotheses:

- **H8 (is-GU-just-Bach?) and H4 (conformal functional): PROMOTE to decisive.** H9 shows
  the entire gravity ghost question reduces to whether GU's gravity operator is pure Bach
  `box^2` (degenerate, Bateman-Turok fails, ghost parity non-unique) or `R + Weyl^2`
  Stelle (non-degenerate, Bateman-Turok applies cleanly). This is now the single highest-
  leverage gravity-sector fork: it simultaneously decides the ghost objection, feeds the
  OQ2-A functional datum from H1, and gates whether the matter-side V2 Cartan-involution
  story has a gravity-side partner at all.
- **H1 (Bach exact vacua): CONFIRMED-adjacent, no change.** H9 is consistent with and
  builds on H1; it inherits H1's "reduces to the OQ2-A functional" verdict and shows the
  *ghost* axis reduces to the same datum. The two now share one fork.
- **H2 (signature): mild coupling.** The O(1,1) vs O(96,96) distinction (PART D) is a
  signature/dimension statement; H9 supplies a clean reason the matter-sector Krein result
  does not automatically transport to gravity. Worth a note in H2, not a re-rank.
- **H5 (entropic): unaffected** by this gravity-kinetic-operator analysis.

**Suggested next council reflection focus:** the conformal-vs-Einstein fork as a *single*
decidable object. Concretely -- is there anything in GU's forced geometry (the shiab
operator, the Rarita-Schwinger source, the fiber Yang-Mills sector) that forces an
Einstein-Hilbert `box` term (hence a distinct massive Stelle ghost, Bateman-Turok-ready)
versus leaving the gravity sector purely conformal `box^2` (degenerate, ghost parity
non-derived)? Resolving that one fork would flip H9 from REDUCE to CLEAR or to FAIL and
would simultaneously settle H1's OQ2-A datum. Until then, both H1 and H9 stand at the same
honest boundary: kinematics exact, one named functional datum open, dynamics unbuilt.
