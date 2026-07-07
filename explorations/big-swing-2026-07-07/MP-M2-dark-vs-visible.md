---
artifact_type: exploration
status: exploration
created: 2026-07-07
title: "MP-M2 dark vs visible: the gapped mirror sector is NOT dark. DERIVED (Spin(10) -> SU(3)xSU(2)xU(1), electron control Q=-1): 84 of 96 mirror states are electrically CHARGED and 72 are COLORED (mirror quarks Q=+/-2/3,+/-1/3 + mirror charged leptons Q=+/-1); only 12 are neutral, all color-singlet mirror neutrinos. Verdict = (ii) a CHARGED/COLORED, VISIBLE, CONSTRAINED sector -- Weinstein's 'everything below the line is dark' is FALSIFIED as a quantum-number statement; the sector is luminous and can only be hidden by MASS (large mu). Falsifiable payoff: the mechanism predicts a full heavy vectorlike mirror generation at the single scale mu; collider data (mirror quarks excluded to ~1.3-1.5 TeV, from-memory) forces mu >~ 1 TeV, and mu near electroweak would be EXCLUDED. The absolute scale mu = phi stays DYNAMICS-GATED (never predicted)."
grade: "CONSISTENT_UNCOMPUTED for the physics status of the sector (a viable charged/visible sector requires dynamics-gated mu >~ 1 TeV); the quantum-number DERIVATION itself is THEOREM grade (exact charges from the Clifford/Spin(10) construction, electron control Q=-1, up Q=+2/3, nu^c Q=0, wrong-embedding control has power, both chirality halves computed). Not EXCLUDED because mu is free; would be EXCLUDED only under the dynamics-gated assumption mu ~ electroweak. Collider bounds flagged FROM-MEMORY."
depends_on:
  - explorations/big-swing-2026-07-06/VG-V8-t5-map-attempt.md
  - explorations/big-swing-2026-07-07/BIG-SWING-ALIGNMENT-PHASE-NOT-TUNING.md
  - canon/ghost-parity-krein-synthesis.md
  - papers/drafts/Transcript into the impossible.md
scripts:
  - tests/big-swing/mp_m2_dark_vs_visible.py
---

# MP-M2 -- Dark vs visible: what ARE the gapped mirror states electrically?

**The swing.** V8 + the A-series established, at kinematic grade, that the condensate
`phi*Pi_mirror` (`Pi_mirror = (I - K|_W)/2`) gaps all 96 mirror states at mass `~ mu` while
keeping all 96 generation states massless, `[M, P_ghost] = 0`, on the physical sector
`96 = 3 x 2 x 16`. That is an internal-consistency result. This route makes it face outward:
**compute the electric charge `Q = T3 + Y` of every gapped mirror state and decide whether the
sector is a dark-matter candidate (neutral, hidden) or a charged/colored sector that colliders
and cosmology would already constrain.** Weinstein asserts "everything below the line is dark"
[`Transcript into the impossible`, line 128]. We TEST that by DERIVING the charges from the
Spin(10) / Standard-Model structure -- we do not import his claim.

Script: `tests/big-swing/mp_m2_dark_vs_visible.py` (exit 0; every number below is printed by it).
Machinery reused verbatim from the verified carrier recipe (`vg_v8_t5_map_attempt.py` /
`ghost_parity_krein.py`).

## Result in one line

The gapped mirror sector is **not dark**. It is a full heavy replica of the visible matter
charges: **84 of its 96 states are electrically charged and 72 are colored**; only 12 are
neutral, all of them color-singlet mirror neutrinos. Verdict = **(ii) a charged/colored,
visible, constrained sector** -- testable, and already forcing `mu >~ 1 TeV`.

## Anchors (reproduced before any charge claim)

`(9,5)` carrier, timelike `{4..8}`: `rank(Gamma) = 128`, `dim ker = 1664`, triplet dim `192`,
Krein signature `(+96, -96, 0)`, `P_ghost = -Q5` on `W` (residual `3.7e-14`). The physical 96
decomposes as `3 x 2 x 16`: su(2)+ family weights `{-2,0,+2} x32` (the generation triplet),
su(2)- weights `{-1,+1} x48` (the doublet), and a uniform internal `so(5)_s` spinor Casimir
`2.500` (the internal factor is one 4-dim spinor; `4 x 4 = 16` = the Spin(10) spinor). The
gapped **mirror sector is the K-negative 96**, carrying the identical `3 x 2 x 16` structure.

## The derivation (no imported charges)

**Bridge.** Electric charge `Q` is a Spin(10) Cartan element (a gamma bilinear) acting purely on
the internal `16`. The `16` is one irreducible rep, so its `Q`-spectrum is identical whether read
on the carrier or on a clean `Cl(10)` Fock model. The su(2)+ (family) and su(2)- factors are
separate tensor factors from the `16`; `SU(3) x SU(2) x U(1)` sits inside Spin(10) and acts only
on the `16`, so those factors are gauge-neutral spectators. So the whole charge question lives in
the `16`, and the 96 mirror states are `6 = 3 x 2` copies of it.

**Build the `16`.** Five Clifford (fermionic) oscillators `c_k` give `Cl(10)` (residual `0`); the
ten gammas `Gamma_{2k} = c_k + c_k^dag`, `Gamma_{2k+1} = i(c_k^dag - c_k)` satisfy
`{Gamma_a, Gamma_b} = 2 delta_ab` (residual `0`); the chirality `Gamma_11` splits the 32-dim
spinor into `16 + 16bar`. This is the standard Spin(10) spinor -- nothing assumed.

**The SM embedding (defined, then `Q` is an output).** Color `SU(3)` rotates oscillators
`{1,2,3}`, weak `SU(2)_L` rotates `{4,5}`, `T3 = (n_4 - n_5)/2`, and hypercharge is the unique
traceless Cartan combination commuting with `SU(3) x SU(2)` that makes `Q` integer/third-integer:
`Y = sum y_k (n_k - 1/2)`, `y = (-1/3,-1/3,-1/3,+1/2,+1/2)`. Then

> **`Q = T3 + Y = sum_k q_k (n_k - 1/2)`, with `q = (-1/3, -1/3, -1/3, +1, 0)`.**

Verified: `Q` commutes with all `SU(3)_c` generators (color-blind, residual `0`) and with `T3`,
but NOT with the full `SU(2)_L` (`[Q, SU(2)_raise] = 2.83`) -- correct, since `Q = T3 + Y` is
exactly the generator that breaks `SU(2)_L` to `U(1)_em`. And `H_k = (i/2) Gamma_{2k} Gamma_{2k+1}
= n_k - 1/2`, so `Q` is a genuine Spin(10) Cartan / gamma bilinear (residual `0`).

**The charge spectrum on the `16` (one Standard-Model generation):**

| Q | multiplicity | content | colored? |
|---|---|---|---|
| `-1` | 1 | `e` | no |
| `-2/3` | 3 | `u^c` | yes (3bar) |
| `-1/3` | 3 | `d` | yes (3) |
| `0` | 2 | `nu`, `nu^c` | no |
| `+1/3` | 3 | `d^c` | yes (3bar) |
| `+2/3` | 3 | `u` | yes (3) |
| `+1` | 1 | `e^c` | no |

**14 of 16 charged; 12 of 16 colored; exactly 2 neutral (both color singlets).**

**Controls (the derivation has discriminating power).** The electron-like state (color singlet,
charged) reads `Q = -1` exactly; the up-type states (colored, `Q = +2/3`) form a color triplet
(3 states); the only neutral states are the two color-singlet neutrinos (`Q = 0`). A WRONG
embedding (uniform `q_k`, a fake `U(1)` that is not hypercharge) fails to reproduce the SM charge
set `{0, +/-1/3, +/-2/3, +/-1}`.

## The gapped mirror sector

The mirror is the opposite-chirality partner (`16bar`); its charges are the conjugates `-Q`, the
**same set of magnitudes** `{0, 1/3, 2/3, 1}`. Electric charge is chirality-blind, so gapping the
mirrors necessarily gaps charged and colored states. Per `16bar`: 14 charged, 12 colored, 2
neutral color-singlet -- identical magnitudes to the generation. This makes gen `16` + mirror
`16bar` a **vectorlike (Dirac) pair**: net chiral asymmetry 0, so the mirrors are Dirac-massable
at any `mu` with **no gauge anomaly** -- which is exactly why they CAN be uniformly gapped, and
confirms "mirror" = vectorlike partner.

Scaled to the full sector `96 = 6 x 16`:

> **Of the 96 gapped mirror states: 84 CHARGED, 72 COLORED, 12 NEUTRAL (all color singlets).**

Crucially, the condensate gaps all 96 uniformly at one mass -- **there is no way to gap only the
neutral part**; the charged and colored mirror states come along in the same multiplet.

## Verdict: determined vs dynamics-gated

**DETERMINED (kinematics + the SM embedding, exact -- no absolute-scale claim):**
- The gapped mirror sector is **not electrically neutral**: mirror up/down quarks
  (`Q = +/-2/3, +/-1/3`, color `3/3bar`) and mirror charged leptons (`Q = +/-1`). Only 12 of 96
  neutral (color-singlet mirror neutrinos).
- **Verdict = (ii) a CHARGED / COLORED, VISIBLE, CONSTRAINED sector**, not a clean dark candidate.
- Weinstein's "everything below the line is dark" is **falsified as a quantum-number statement**:
  the sector is luminous (charged/colored). It can be hidden only by being **heavy** (large `mu`)
  -- which is Weinstein's own hedge in the same breath, "these two things here are luminous ...
  too massive ... you haven't seen it yet" [Transcript, line 128]. "Dark" is the wrong word;
  "heavy and not-yet-produced" is the right one.

**DYNAMICS-GATED (NOT predicted):**
- The absolute mirror mass scale `mu = phi`. Set by the unbuilt VEV/source action. **No absolute
  mass is claimed.**
- Whether GU's dynamics even selects the mirror-gapping vacuum (the A2 sign bit).
- Any dark-matter role for the 12 neutral mirror-neutrino states -- needs stability, relic
  abundance, and a way to decouple them from the 84 charged states they are gapped alongside; all
  dynamics-gated and disfavored, since they gap in one multiplet with charged colored states.

**FALSIFIABLE CONTENT (the swing's outside-facing payoff):**
- The mechanism **predicts a full heavy vectorlike mirror generation** (mirror quarks + charged
  mirror leptons) at the single scale `mu` -- pair-producible at a collider with `sqrt(s) > mu`.
- **Lower bound on `mu` [FROM-MEMORY, flagged].** Heavy charged leptons are excluded by LEP to
  `~100 GeV` and by the LHC to a few hundred GeV; sequential / vectorlike heavy quarks are
  excluded by the LHC to `~1.3-1.5 TeV`. So `mu` must be **above `~ 1 TeV`** or the mirror quarks
  would already have been produced. If `mu` were near the electroweak scale the mechanism would be
  **EXCLUDED (case iii)**; since `mu` is a free dynamics-gated scale, the honest status is **(ii)**:
  the charged mirror sector pushes `mu >~ 1 TeV` and is testable, not yet excluded.
- This is a genuine kinematic constraint on the still-unbuilt dynamics: **any source action that
  generates the mirror-gapping condensate at `mu <~ 1 TeV` is already ruled out by collider data.**

## Honest gaps

1. **Kinematic only.** No source action, no `S`, no dynamics. `mu` is uncomputable, so the
   collider constraint is a bound on the dynamics, not a prediction of a mass.
2. **The SM embedding is a choice.** `SU(3) x SU(2) x U(1) ⊂ Spin(10)` is fixed by the standard
   (anomaly-free, integer-charge) requirement and validated by the electron control; a different
   `U(1)_Y` normalization is excluded by that control, but the embedding is an input, not derived
   from GU dynamics (GU supplies the `16`, not the choice of which Cartan is electromagnetism).
3. **Carrier bridge is by irrep identity, not by building `Q` on the (9,5) carrier directly.** The
   internal factor is verified to be the 16 (`so(5) x so(5)` spinor `4 x 4`); the charge spectrum
   is then computed on the clean `Cl(10)` model, valid because the 16 is one irrep. A direct build
   of the SM Cartan on the `so(5,5)` carrier internal is not done (the SM group is not aligned with
   `so(5)_s x so(5)_t`); it would be a stronger but redundant check.
4. **Collider bounds are from-memory**, not re-derived. Order-of-magnitude only; the qualitative
   conclusion (charged colored mirror fermions near electroweak are excluded) is robust, the exact
   TeV number is not load-bearing.
5. **The dark-matter door is not fully shut, only pushed.** A neutral mirror-neutrino subsector
   COULD in principle carry a dark component, but not as a clean prediction of this mechanism: the
   neutral states are a `12/96` minority gapped together with the charged/colored majority, and
   any separation is dynamics-gated.
6. **Count untouched.** This route says nothing about the generation count 3; the physical sector
   stays `96 = 3 x 2 x 16`. Dark-vs-visible is orthogonal to the count question.

## Governance

Exploration-grade; no canon promotion proposed. The determined content (mirror sector is
charged/colored/visible, forcing `mu >~ 1 TeV`) is a candidate line for a mirror-mechanism paper's
prediction table, flagged for Joe, not applied. This is the second-paper (mirror-mechanism)
frontier; the frozen located-not-forced paper is untouched. Verification tier: internal
adversarial (single main-loop build, exit 0, powered controls including a wrong-embedding
control; from-memory collider bounds flagged).
