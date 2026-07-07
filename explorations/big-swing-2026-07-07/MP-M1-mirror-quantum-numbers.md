---
artifact_type: exploration
status: exploration
created: 2026-07-07
title: "MP-M1 (mirror quantum numbers): the gapped mirror sector is a GAUGE-IDENTICAL vectorlike partner of the SM generations, NOT the CPT-conjugate 16bar. THEOREM (both signatures): the full spinor chirality C = e0..e13|_W = -chi_int commutes with all 45 internal so(10) generators, both family su(2), and J_quat, and anticommutes with P_ghost -- so it maps the physical sector bijectively onto the mirror with identical color/isospin/hypercharge/family content, state for state. The ghost-parity Z2 (P) and the Spin(10)-chirality Z2 (chi_int) ANTICOMMUTE ({P,chi_int}=0, ~4e-15 both signatures): each mirror state is a (16 - 16bar) combination, not a pure 16bar -- the naive CPT-conjugate reading is REFUTED. DERIVED (Cl(10) oscillators): the 16 = one SM generation [Q(3,2,1/6)+u^c+d^c+L+e^c+nu^c], charge set {0,+/-1/3,+/-2/3,+/-1}, so the mirror is colored+charged (NOT neutral/dark; consistent with M2). Mirror count = generation count = 96 = 3x2x16 exactly; physical+mirror is vectorlike hence anomaly-free. HONEST CAVEAT (T4): on the (5,5)-signature carrier the SM electric charge does not commute with P (rank-5 so(10) Cartan vs rank-4 compact Cartan = one boost), so the charge CONTENT is invariant/determined but per-eigenstate SM labeling within a ghost sector is exact only up to that one boost rotation. Absolute scale mu = phi is DYNAMICS-GATED and never predicted; the count stays OPEN."
grade: "THEOREM (quantum-number decomposition + intertwiner + count + anomaly) with one CONSISTENT_UNCOMPUTED caveat (per-eigenstate SM charge labeling, T4). All checks pass exit 0 in the main loop, both (9,5) and (7,7) signatures, with a discriminating control (a fake uniform-hypercharge U(1) fails the SM charge set). Target-import guard clean: 128,1664,192,96,32,16 measured; the SM table is DERIVED from the oscillator construction and used only as a CHECK. No absolute-mass claim. Count stays OPEN (the value 3 and the 3-vs-6 extraction are untouched)."
depends_on:
  - canon/ghost-parity-krein-synthesis.md
  - explorations/big-swing-2026-07-06/VG-V8-t5-map-attempt.md
  - explorations/big-swing-2026-07-07/BIG-SWING-ALIGNMENT-PHASE-NOT-TUNING.md
  - explorations/big-swing-2026-07-07/A3-orientation-z2.md
  - papers/drafts/Transcript into the impossible.md
scripts:
  - tests/big-swing/mp_m1_mirror_quantum_numbers.py
---

# MP-M1: what IS the gapped mirror sector? (its quantum numbers)

**The swing's foundational question.** V8 + the A-series built a mostly-complete kinematic result:
the ghost parity `P_ghost = -Q5 = -(internal spacelike volume)|_W` is Clifford-native, and the
condensate `phi*Pi_mirror` gaps all 96 mirror states (the K-negative, P-odd half of the 192-dim
triplet) while keeping all 96 generation states (K-positive, P-even) massless, `[M, P_ghost] = 0`.
The physical sector is `96 = 3 x 2 x 16` (three su(2)+ generations x an su(2)- doublet x the 16 of
Spin(10)). This route extracts the outside-facing prediction: **what ARE the gapped mirror states,
as representations of `SU(3)xSU(2)xU(1)` and `Spin(10)`? Are they the CPT-conjugate / opposite-
chirality partners of the generations (the `16bar`), or something else?**

Script: `tests/big-swing/mp_m1_mirror_quantum_numbers.py` (exit 0; every number below is printed by
it, both signatures where stated). Machinery reused verbatim from the verified carrier recipe
(`ghost_parity_krein.py` / `vg_v8`); the SM decomposition is built independently from a clean Cl(10)
oscillator model and used only as a **check** that the physical half reproduces the SM content.

## Answer (one line)

The gapped mirror sector is a **gauge-identical, opposite-ghost-parity, negative-Krein-norm partner**
of the physical generations -- a *vectorlike* mirror copy carrying the SAME color, isospin, and
hypercharge -- and it is emphatically **NOT** the CPT-conjugate `16bar`.

## 0. Anchors (reproduced before any claim)

`(9,5)` carrier, timelike `{4..8}`: `rank(Gamma) = 128`, `dim ker = 1664`, triplet dim `192`, Krein
signature `(+96, -96, 0)`, `P_ghost = -Q5` (residual `3.7e-14`). The physical 96 decomposes as
`3 (su(2)+ triplet x32) x 2 (su(2)- doublet x48) x 16` with a uniform internal `so(5)_s` spinor
Casimir (the internal factor is one Spin(10) spinor, `4 x 4 = 16`). The `(7,7)` block reproduces its
own anchors (triplet 192, Krein `(+96,-96)`).

## 1. T1 -- the intertwiner theorem (the workhorse): mirror = gauge-identical to physical

The full spinor chirality `C = (e0 e1 ... e13)|_W` **equals `-chi_int`** (the internal Spin(10)
chirality `e4..e13`) on `W` identically (residual `0.0e+00`), because the base volume degenerates on
`W` (`chi_base|_W = -I`, V8). Machine-checked:

- `C` is an involution (`C^2 = I`) and **anticommutes with `P_ghost`** (`{C,P} = 5e-14`): so `C`
  maps the physical sector bijectively onto the mirror sector.
- `C` **commutes with all 45 internal `so(10)` bivectors** (max residual `2.6e-14`), with **both
  family `su(2)+/-` actions** (`8.6e-14`), and with `J_quat`.

Since `C` is gauge- and family-trivial and swaps the ghost parity, the mirror sector
`= C(physical)` carries the **identical internal-gauge + family representation** as the physical
sector, state for state. Confirmed directly: the family and internal Casimir spectra on the mirror
96 match the physical 96 exactly (`||dFam|| = 3.5e-14`, `||dInt|| = 3e-16`).

> **Determined.** Whatever SM quantum numbers the physical generations carry, the mirror carries
> them identically -- same color, isospin, hypercharge, and family multiplicity. The mirror is a
> *vectorlike (same-charge) partner*, not an opposite-charge conjugate.

## 2. T2 -- the mirror is NOT the `16bar`

The ghost-parity `Z2` (`P`) and the Spin(10)-chirality `Z2` (`chi_int`, the `16` vs `16bar`
grading) **anticommute**: `{P, chi_int} = 0` (residual `3.8e-15` in `(9,5)`, `4.0e-15` in `(7,7)`),
with `chi_int` itself of signature `(+96, -96)` on `W`. So the physical/mirror basis is a
**45-degree rotation** of the `16 / 16bar` basis (`C` is the chirality *grading*, `P` is the
*swap*; `[C,P]/|C| = 2.00`):

- each **physical** state is a maximally-entangled `(16 + 16bar)` combination;
- each **mirror** state is the orthogonal `(16 - 16bar)` combination.

> **Refutation (determined).** The naive reading "the gapped mirrors are the CPT-conjugate `16bar`
> partners" is FALSE as a literal statement: neither the physical nor the mirror sector is a
> Spin(10)-chirality eigenstate. This is V8's "no `16`-vs-`16bar` decomposition of the physical
> sector," now read as the positive characterization of the mirror: it is the opposite-*ghost-parity*
> partner (T1), gauge-identical to the physical sector -- the Distler-Garibaldi vectorlike structure,
> identified as *(generation + ghost)* rather than *(generation + physical mirror)*.

## 3. T3 -- the derived `16` = one SM generation (so the mirror content is one SM generation)

Built as the `+`-chirality spinor of `Cl(10)` from 5 fermionic Clifford oscillators (standard
Spin(10) construction; `{c_i, c_j^dag} = delta_ij` and `{Gamma_a, Gamma_b} = 2 delta_ab` at machine
zero), with the SM embedding color `= {osc 1,2,3}`, weak `= {osc 4,5}`, `Y = sum y_k (n_k - 1/2)`,
`y = (-1/3,-1/3,-1/3,1/2,1/2)`. Electric charge `Q = T3 + Y` is a pure **output** and commutes with
`SU(3)_c` and `T3` (a legitimate SM charge). The `16` decomposes EXACTLY:

| field | SU(3) | SU(2) | \|Y\| | states |
|---|---|---|---|---|
| `Q` quark doublet | 3 | 2 | 1/6 | 6 |
| `u^c` quark singlet | 3bar | 1 | 2/3 | 3 |
| `d^c` quark singlet | 3bar | 1 | 1/3 | 3 |
| `L` lepton doublet | 1 | 2 | 1/2 | 2 |
| `e^c` lepton singlet | 1 | 1 | 1 | 1 |
| `nu^c` lepton singlet | 1 | 1 | 0 | 1 |

charge set `{0, +/-1/3, +/-2/3, +/-1}`; **14 of 16 charged, 12 colored, 2 neutral (color-singlet
neutrinos)**. (Overall `Y`-sign and `3<->3bar` are pure convention -- which chirality is called the
`16`, sign of hypercharge -- and change no physics; charge magnitudes are physical and match the SM.)
A discriminating control confirms the derivation has power: a **fake uniform-hypercharge `U(1)`**
(not the SM `Y`) fails to reproduce the SM charge set. This `16` **is** the carrier's internal factor
(same irrep -> same Cartan spectrum), so it is the physical half's content; by T1 the mirror carries
it identically.

> **Determined (cross-ref MP-M2).** The mirror sector is colored and electrically charged -- a full
> heavy vectorlike replica of the visible matter (`84/96` charged, `72/96` colored, `12/96` neutral
> color-singlets). It is **not a neutral dark sector**; Weinstein's "everything below the line is
> dark" is corrected to "luminous but hidden" (by ghost projection + mass gap, not by neutrality).

## 4. T4 -- the rank obstruction (the honest caveat behind the per-state labeling)

The ghost-parity-commuting compact subgroup is `Spin(5) x Spin(5)` (rank 4); its Cartan is spanned by
the **within-block** bivectors, all verified to commute with `P` (`e4e5, e6e7, e9e10, e11e12`,
`[.,P]/|.| ~ 4e-15`). But `so(10)` has **rank 5**, and the fifth Cartan direction necessarily pairs
the leftover timelike and spacelike gammas into a **boost** that anticommutes with `P` (`e8e13, e8e9`,
`{.,P}/|.| ~ 4e-15`). The SM electric-charge Cartan `Q` has nonzero weight on this fifth direction,
so **`Q` does not commute with `P` on this `(5,5)`-signature carrier**.

> **Consequence (CONSISTENT_UNCOMPUTED).** The charge **content** (which reps appear; colored /
> charged) is a ghost-parity-invariant, determined quantity. The clean **per-eigenstate** SM charge
> labeling within a single ghost sector is exact only up to the one boost rotation between the two
> sectors -- the same `16+16bar` vectorlike-mixture caveat as T2. (This is exactly why the invariant
> statement is at the `Spin(5)x Spin(5) = (4,4)` level and the vectorlike level, not at the level of
> a clean chiral `16` inside one ghost sector -- and it is the kinematic root of the achirality fence
> and the open count.)

## 5. T5 -- count and anomaly

- **Mirror count = generation count = `96 = 3 x 2 x 16`, exactly** (`C` is a dimension-preserving
  isomorphism). The value `3` and the `3`-vs-`6` extraction remain **OPEN** (unchanged by this route).
- **Anomaly.** The physical + mirror content is a full vectorlike `16 (+) 16bar`, hence
  gauge-anomaly-free; each `16` is separately anomaly-free (`Spin(10)`). This is precisely why the
  mirrors *can* be Dirac-gapped uniformly, and it reproduces the Distler-Garibaldi vectorlike
  obstruction with the mirrors now identified as the negative-norm ghosts.

## 6. Determined vs dynamics-gated (the honest ledger)

**Determined (kinematics + Clifford + the SM embedding; exact, no absolute-scale claim):**
1. The mirror is a gauge-identical, opposite-ghost-parity, negative-Krein-norm vectorlike partner of
   the generations (T1) -- same color/isospin/hypercharge/family, state for state.
2. The mirror is NOT the CPT-conjugate `16bar` (T2): `{P, chi_int} = 0`.
3. The content is one full SM generation of quantum numbers (T3): colored quarks, charged leptons,
   neutral neutrinos -- hence colored + charged, not a neutral dark sector.
4. Mirror count = generation count = `96 = 3 x 2 x 16` (T5).
5. The full spectrum is vectorlike, hence anomaly-free.

**Dynamics-gated (NEVER predicted here):**
- The **absolute mirror mass scale `mu = phi`** -- set by the unbuilt VEV / source action. No
  absolute-mass claim is made.
- The **orientation "which half is physical" bit** -- discharged by A3 as a Krein-labeling
  redundancy; the invariant statement is "the ghost half gaps."
- Whether GU's dynamics **selects** the mirror-gapping vacuum -- the one open sign bit (A1/A2/A4).
- The **generation count** stays OPEN.

## 7. Honest gaps

1. **Kinematic only.** No source action, no `S`, no dynamics: everything is representation theory on
   the frozen carrier. The absolute scale, and whether the mirrors are gapped at all, are the unbuilt
   dynamics' job.
2. **The T4 caveat is a genuine `(5,5)`-signature limitation.** On a carrier whose internal signature
   split the SM electric-charge Cartan into the compact rank-4 subgroup, `Q` would commute with `P`
   and the per-eigenstate labeling would sharpen from CONSISTENT_UNCOMPUTED to THEOREM. Testing that
   is a natural next probe; the invariant content-level statements already hold in both signatures run.
3. **The `16bar` shorthand in sibling routes.** MP-M2 (dark/visible) labels the mirror "the
   opposite-chirality `16bar`" as a working shorthand; T2 refines this -- the charge *magnitudes*
   coincide either way (charge is chirality-blind), so M2's charged/colored verdict is unaffected, but
   the precise object is the ghost-parity partner, a `(16 - 16bar)` combination.
4. **The count is not advanced.** `96 = 3 x 2 x 16`, chi-trace-achiral; extracting `3` (not `6`, not
   `48`) is exactly as open as canon states.
