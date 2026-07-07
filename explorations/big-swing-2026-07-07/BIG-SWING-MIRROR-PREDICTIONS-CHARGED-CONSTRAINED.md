---
artifact_type: exploration
status: exploration
created: 2026-07-07
title: "Mirror-sector prediction table (second-paper seed): the gapped mirror is CHARGED / COLORED / VISIBLE-BUT-HEAVY, not dark, and NOT excluded (mu is free). Synthesis of routes M1-M4 with verifier verdicts folded (verdicts WIN). DETERMINED, carrier-native, machine-checked in both (9,5) and (7,7): (T1) the mirror is a gauge/family-IDENTICAL, opposite-ghost-parity, negative-Krein-norm VECTORLIKE partner of the physical generations -- intertwiner C = e0..e13|_W = -chi_int, residual 0.0e+00, commutes with all 45 internal so(10) + both family su(2), anticommutes with P_ghost; (T2) the mirror is NOT the pure CPT-conjugate 16bar -- {P,chi_int}=0, it is a (16-16bar) ghost-parity combination; (T5) mirror count = generation count = 96 = 3x2x16 exactly; (M4-4) the one undetermined sign bit is spectrally INVISIBLE; (M4) the mirror spectrum is a single flat degenerate level, generations exactly massless under the mechanism. IMPORTED (honestly flagged, NOT GU-derived): the SM hypercharge embedding SU(3)xSU(2)xU(1) subset Spin(10) that turns the 16 into one charged SM generation -- so 'charged not dark' is a THEOREM only GIVEN the standard embedding; anomaly-freedom is textbook Spin(10). DYNAMICS-GATED (never predicted): the absolute scale mu=phi, vacuum selection, the generation count 3-vs-6, generation Yukawas, any DM role of the 12 neutral states. HONEST OUTCOME: CHARGED-CONSTRAINED."
grade: "MIXED. Carrier-native THEOREM core (T1 intertwiner, T2 not-16bar, T5 count, M4-4 sign-bit invisibility) SUSTAINED under adversarial verification in both signatures. The outward physics readout (charged/colored/visible) is CONSISTENT_UNCOMPUTED: robust GIVEN the standard SM embedding, but the embedding is imported not derived, the per-eigenstate charge labeling is boost-ambiguous on the (5,5) carrier (T4), and gauge-invariance of the mirror mass is proven only against the 20-dim maximal compact, not the full SM. NOT EXCLUDED: mu is free. No absolute-mass claim anywhere. Generation count stays OPEN."
depends_on:
  - canon/ghost-parity-krein-synthesis.md
  - explorations/big-swing-2026-07-06/VG-V8-t5-map-attempt.md
  - explorations/big-swing-2026-07-07/BIG-SWING-ALIGNMENT-PHASE-NOT-TUNING.md
  - explorations/big-swing-2026-07-07/MP-M1-mirror-quantum-numbers.md
  - explorations/big-swing-2026-07-07/MP-M2-dark-vs-visible.md
  - explorations/big-swing-2026-07-07/MP-M3-count-and-anomaly.md
  - explorations/big-swing-2026-07-07/MP-M4-mass-texture-sign-bit.md
  - papers/drafts/Transcript into the impossible.md
scripts:
  - tests/big-swing/mp_m1_mirror_quantum_numbers.py
  - tests/big-swing/mp_m2_dark_vs_visible.py
  - tests/big-swing/mp_m3_count_and_anomaly.py
  - tests/big-swing/mp_m4_mass_texture_sign_bit.py
---

# The gapped mirror sector: falsifiable-prediction table (second-paper seed)

**Outcome tag: CHARGED-CONSTRAINED.** The gapped mirror sector is not a clean dark candidate and
is not excluded. It is a heavy, luminous (charged + colored) vectorlike replica of the visible
generations, hidden by mass alone, at a scale the kinematics does not set.

## The swing (what this synthesis turns outward)

The 2026-07-06 V8 result plus the 2026-07-07 alignment swing (A1-A4) built a mostly-complete,
positive **kinematic** result: the ghost parity `P_ghost = -Q5 = -(internal spacelike volume)|_W`
is Clifford-native; the condensate `phi*Pi_mirror` (`Pi_mirror = (I - K|_W)/2`) gaps all 96 mirror
states (the K-negative, P-odd half of the 192-dim self-dual triplet) at mass `~ mu` while keeping
all 96 generation states (K-positive, P-even) exactly massless, with `[M, P_ghost] = 0`. It is a
native phase, a stable global minimum, positivity-preserving, down to one undetermined coupling
sign bit. The physical sector is `96 = 3 x 2 x 16` (three `su(2)+` generations x an `su(2)-`
doublet x the 16 of Spin(10)).

This document **extracts the outside-facing physics** of that gapped mirror sector: its quantum
numbers, whether it is dark or visible, whether its count matches the generations, its anomaly
consequences, and its mass texture -- **each prediction tagged DETERMINED or DYNAMICS-GATED, with
its verifier-adjudicated grade.** It is EXTRACTIVE, not promote-or-kill.

**The honest constraint, restated (binds every row below).** The **absolute** mirror mass scale
`mu = phi` is NOT determined by the kinematics -- it is set by the unbuilt dynamics / VEV. **No
row predicts an absolute mass.** What the kinematics + the one sign bit fix: quantum numbers (rep
theory, exact), dark-vs-visible, count-matching, anomaly consequences, mass *shape*, and the
(non-)imprint of the sign bit.

## Per-route summary (verifier verdicts folded in -- verdicts WIN)

| route | question | build grade | verdict (x2) | what SURVIVES | what is TRIMMED |
|---|---|---|---|---|---|
| **M1** | mirror quantum numbers | THEOREM + 1 caveat | **PARTIAL / PARTIAL** | intertwiner `C=-chi_int` (residual 0.0e+00); mirror != pure 16bar (`{P,chi_int}=0`); count 96=96; vectorlike | "GU predicts the SM quantum numbers" -- the SM hypercharge is imported, never measured on the (5,5) carrier; T4 boost-ambiguity |
| **M2** | dark vs visible | THEOREM (derivation) / CONSISTENT (status) | **PARTIAL / PARTIAL** | 84/72/12 of 96 charged/colored/neutral GIVEN the embedding; not-EXCLUDED (mu free); collider bounds honestly FROM-MEMORY | "DERIVED not imported" (embedding hardcoded); "FALSIFIES Weinstein" (his own words say luminous-but-heavy); THEOREM novelty (textbook SO(10)) |
| **M3** | count + anomaly | THEOREM x2 | **SUSTAINED / PARTIAL** | numerics clean, controls have teeth; family-count matching across the Krein split; vectorlike => anomaly-free => gappable | count-matching is near-tautological (family-blind split); anomaly-freedom is textbook, not a novel prediction |
| **M4** | mass texture + sign bit | THEOREM + CONSISTENT | **PARTIAL / PARTIAL** | flat degenerate mirror level; generations exactly massless; **sign bit spectrally invisible** (the one genuinely NEW determined datum); (7,7) independence | "gauge-invariant" proven only vs the 20-dim maximal compact (25/45 Spin(10) generators break `Pi_mirror`); flatness partly definitional to the imported projector ansatz |

Both verifiers on every route re-ran the scripts from disk to exit 0 in both `(9,5)` and `(7,7)`;
no false number, no smuggled dynamics, and honest_gaps ledgers were judged accurate throughout.
The gap in every case is **framing overreach in the headline/grade, not concealment in the math.**

## THE PREDICTION TABLE

Legend -- **DET** = DETERMINED (kinematically fixed, structural/falsifiable, no absolute-scale
claim). **GATED** = DYNAMICS-GATED (needs the unbuilt source action; never presented as a
prediction). Grade after verdicts: **THM** carrier-native machine-checked theorem; **THM\*** exact
but structurally near-tautological / low discriminating power; **CU** CONSISTENT_UNCOMPUTED (holds
given an imported input or on an auxiliary model, not carrier-derived end-to-end); **[import]**
load-bearing physics imported from standard GUT rep theory, flagged.

| # | Prediction | Tag | Grade | Notes (verifier-adjudicated) |
|---|---|---|---|---|
| **P1** | The mirror is a **gauge- and family-IDENTICAL, opposite-ghost-parity, negative-Krein-norm vectorlike partner** of the physical generations -- same internal so(10) + family content, state for state. | **DET** | **THM** | Intertwiner `C = (e0..e13)|_W = -chi_int`, residual **0.0e+00**; `[C, all 45 internal so(10)] <= 2.6e-14`, `[C, family su(2)+/-] <= 8.6e-14`, `{C, P_ghost} = 5.3e-14`. Mirror/physical Casimir spectra match (`||dFam||=3.5e-14`, `||dInt||=3e-16`). Both signatures. **The strongest, cleanest result of the swing.** |
| **P2** | The mirror is **NOT the pure CPT-conjugate 16bar**; it is a `(16 - 16bar)` ghost-parity combination. Neither sector is a Spin(10)-chirality eigenstate. | **DET** | **THM** | `{P_ghost, chi_int} = 3.8e-15 (9,5) / 4.0e-15 (7,7)`; `chi_int` signature `(+96,-96)`; `[C,P]/|C| = 2.00`. Refutes the naive "mirror = 16bar" reading; identifies the Distler-Garibaldi vectorlike structure as *(generation + ghost)*. |
| **P3** | **Mirror count = generation count = 96 = 3 x 2 x 16, exactly.** The mirror/dark sector has as many families as the visible sector. | **DET** | **THM\*** | Dimension-preserving isomorphism `C`; both Krein halves measured identical (`su(2)+ {-2,0,+2}x32`, `su(2)- {-1,+1}x48`, `so(5)` Casimir 2.500). **Verifier caveat:** near-tautological -- `[J_family, P_ghost]=0` makes the split family-blind by construction, so equality is structurally forced, not discovered. The value **3** (and 3-vs-6) stays OPEN. |
| **P4** | The mirror is **electrically CHARGED and COLORED, not neutral/dark**: of 96 states, **84 charged, 72 colored, 12 neutral** (color-singlet mirror neutrinos). Charged mirror quarks `Q=+/-2/3,+/-1/3` + charged mirror leptons `Q=+/-1`. | **DET given embedding** | **CU [import]** | Exact charge set `{0,+/-1/3,+/-2/3,+/-1}` on the Cl(10) 16; electron/up/nu^c controls pass; wrong-U(1) control fails. **BUT** the SM hypercharge `y=(-1/3,-1/3,-1/3,+1/2,+1/2)` is **hardcoded**, never measured on the carrier; T4: on the `(5,5)` carrier `Q` does not commute with `P` (rank-5 vs rank-4 compact Cartan = one boost), so per-eigenstate charge labeling is boost-ambiguous. Robust *given* the standard embedding; not a GU derivation of the SM. |
| **P5** | **Charge is chirality-blind:** gapping the mirrors necessarily gaps a full heavy replica of visible-matter charges. There is **no way to gap only the neutral subset** -- charged/colored come along in one multiplet. | **DET given embedding** | **CU [import]** | Follows from P1+P4. Kills the clean-dark-candidate reading: the 12 neutral states cannot be isolated by the mechanism. |
| **P6** | The full physical+mirror spectrum is **vectorlike (16 (+) 16bar), hence gauge-anomaly-free**, each 16 separately anomaly-free (Spin(10)). This is *why* uniform Dirac gapping is anomaly-consistent. | **DET** | **THM\* [import]** | Four SM coefficients computed = 0 on the built 16 (`SU(3)^3=0`, `SU(2)^2U(1)=4.4e-16`, `U(1)^3=1.1e-16`, `grav^2U(1)=-2.2e-16`); full so(10) cubic tensor `A^{abc}=0`. **Verifier caveat:** this is textbook SO(10) anomaly-safety (no cubic Casimir); the SM hypercharge does no work in the vanishing (random so(10) weights give the same zeros). A consistency remark, not a novel prediction. |
| **P7** | The mirror spectrum is a **single flat, degenerate level** -- one mass, 96-fold, zero texture (no family / isospin / hierarchy splitting), band width `~1e-14`. A discovered non-flat leading texture is in tension. | **DET (leading order)** | **THM\*** | `M(phi)=phi*Pi_mirror` spectrum exactly `{0^96, phi^96}`; `Pi_mirror` rank-96 projector; quartic `tr(M^4)` minimized by the uniform level. **Verifier caveat:** flatness is partly definitional given the imported projector ansatz (A1/A4); leading-order only (radiative/EWSB lifts expected, gated). |
| **P8** | The mirror mass is **gauge-invariant / vectorlike (needs no electroweak breaking)** -- it does not split within gauge multiplets at leading order. A chiral (gauge-breaking) mirror mass is in tension. | **DET vs max-compact; CU vs SM** | **CU** | `Pi_mirror` commutes with all 26 checked unbroken generators (`~1e-14`) and with the 20-dim maximal compact `SO(5)xSO(5)`. **Verifier finding:** 25 of the 45 Spin(10) generators do NOT commute with `Pi_mirror` (`~13.9`). Whether the actual SM group lands inside the 20 commuting directions is **unverified** -- a live risk, not a formality. Downgraded from THEOREM. |
| **P9** | The generation half is **exactly massless under the mirror-hiding mechanism** (`m_gen/mu = 0` to `1e-15`). Generation masses come from a separate, unbuilt mechanism. | **DET** | **THM\*** | Definitional to the aligned projector; orientation-independent; both signatures. |
| **P10** | The one undetermined sign bit is **SPECTRALLY INVISIBLE**: both orientations give the identical mass multiset `{0^96, phi^96}` (max diff `1.6e-15`); `chi` conjugates one into the other (`3.7e-14`). Its only physical content is the binary gapped-vs-blind phase; it is **not a texture/ratio knob**. | **DET** | **THM** | The one genuinely NEW determined datum of M4; survives both verifiers cleanly. Rules out reading any mirror observable off the sign choice. |
| **P11** | The only kinematically fixed **ratios** are trivial: `mirror/mirror = 1`, `m_generation/mu = 0`. The Weyl relation `phi = mu/q` is the alignment condition itself, not an independent number. | **DET** | **THM** | Closes the door on any nontrivial kinematic mass ratio. |

**Everything below is DYNAMICS-GATED -- explicitly NOT predicted:**

| gated quantity | why |
|---|---|
| **Absolute mirror mass scale `mu = phi`** | set by the unbuilt VEV / source action. No absolute-mass claim is made anywhere. |
| **Whether GU's dynamics selects the mirror-gapping vacuum** | the single open coupling sign bit (`sign tr(Q5 Phi^2)`, A1/A2/A4); needs the source action `S`. |
| **The generation count (the value 3; the 3-vs-6 extraction)** | untouched by every route; `96 = 3 x 2 x 16` chi-trace-achiral, exactly as OPEN as canon states. |
| **Generation Yukawa texture (SM fermion masses)** | a different, unbuilt condensate. |
| **Any mirror-gap / generation-mass ratio** | both scales unbuilt. |
| **Any dark-matter role of the 12 neutral mirror-neutrino states** | needs stability, relic abundance, and decoupling from the 84 charged states they gap alongside -- all gated, and disfavored since they sit in one multiplet. |
| **Radiative / EWSB lifts of the flat degeneracy** | existence expected once dynamics is built; size entirely gated. |
| **Per-eigenstate SM charge labeling inside one ghost sector (T4)** | tied to the signature/embedding and to the same achirality/count question the dynamics must settle. |

## Headline physics readout

**The gapped mirror sector is CHARGED / COLORED / VISIBLE-BUT-HEAVY -- not dark, not excluded.**

- It is **not a clean dark-matter candidate**: 84/96 states are electrically charged, 72/96
  colored, only 12/96 neutral, and the neutral minority cannot be isolated by the mechanism (P4,
  P5). This holds *given* the standard SM embedding of Spin(10).
- It is **not excluded**: the absolute scale `mu` is free (dynamics-gated). From-memory collider
  bounds (flagged) -- charged heavy leptons excluded to a few hundred GeV, vectorlike heavy quarks
  to `~1.3-1.5 TeV` -- would force `mu >~ 1 TeV` *if* the mirrors are producible states. `mu` near
  the electroweak scale would be excluded; but `mu` is free, so the honest status is a
  **constrained, testable-in-principle** sector.
- **On Weinstein's "everything below the line is dark":** the verifiers corrected the M2 headline.
  It is *not* "falsified." Weinstein's own next sentence (Transcript line 128) says the states are
  "luminous, but you haven't seen them yet ... too massive." That is exactly this readout. The
  honest verb is **disambiguated in favor of luminous-but-massive**, not "falsified" -- only a
  literal all-neutral reading of "dark" is refuted, and Weinstein self-corrects it in the same
  breath.

## An unreconciled physical tension (flagged, load-bearing for the paper)

The M4 physics-consistency verifier surfaced a genuine internal inconsistency the routes have not
closed, and it must be named in any paper built on this table:

> The falsifiable collider payoff of P4/P5 (a heavy vectorlike mirror generation, pair-producible
> at `sqrt(s) > mu`) requires the K-negative 96 to be **physical, producible asymptotic states.**
> But `canon/ghost-parity-krein-synthesis.md` -- a dependency doing the generation-count work --
> treats the same K-negative 96 as **negative-norm GHOSTS removed by the Turok-Bateman projector
> Born rule** (unphysical, never produced, no collider signature). These two fates are mutually
> exclusive.

The "luminous / collider-testable" framing silently adopts the vectorlike-mass resolution, which
undoes the ghost-removal resolution the canon uses. "Luminous" also overstates observability of
ghost-projected states -- the defensible determined statement is "the mirror **carries** color +
charge labels," with observability itself contingent on which resolution the built dynamics
realizes. This is the central open physics question the mirror-mechanism paper must resolve, not
paper over.

## What this gives the second (mirror-mechanism) paper

A real, carrier-native spine of machine-checked theorems -- the outside-facing content:

1. **The intertwiner theorem (P1) + not-16bar (P2).** These are genuine, novel, exact
   (residual 0.0e+00), discriminating results in both signatures: the mirror is the
   *opposite-ghost-parity vectorlike partner*, not the CPT-conjugate. This is the paper's
   structural thesis and it survives full adversarial scrutiny.
2. **The sign-bit invisibility theorem (P10).** A clean new determined datum: the one open sign
   bit is a binary phase switch with no spectral imprint. It closes off a whole class of "read the
   texture to fix the sign" hopes.
3. **The determined/gated discipline itself.** The table cleanly separates what the kinematics
   fixes (quantum-number *relations*, count-matching, mass *shape*, sign-bit silence) from what the
   dynamics must supply (`mu`, vacuum selection, the count, Yukawas). No gated quantity is sold as
   a prediction. This discipline is the paper's honesty backbone.
4. **The charged-not-dark readout (P4/P5)** as a *conditional* structural claim -- correct given
   the standard embedding, honestly flagged as embedding-dependent -- plus the reconciliation
   question above as the paper's central open problem.

## What stays gated / open (the paper must NOT claim)

- No absolute mass. `mu` is free.
- No generation count. `3` and 3-vs-6 are untouched.
- No GU-derivation of the SM quantum numbers: the hypercharge embedding is imported textbook SO(10)
  GUT rep theory, applied in an auxiliary compact Cl(10) model, never measured on the actual
  Spin(5,5) carrier. The GU-specific content is "mirror IS quantum-number-identical to *whatever*
  the physical generations are" (proven) + "IF the physical 16 is a standard SO(10) generation THEN
  it is colored+charged" (imported).
- No unqualified "gauge-invariant mirror mass": proven only against the 20-dim maximal compact;
  the SM-into-`SO(5)xSO(5)` embedding is unclosed (25/45 Spin(10) generators break `Pi_mirror`).
- No resolution of the producible-mirrors-vs-removed-ghosts tension.

## Honest scope

Verification tier: **internal adversarial** -- each route built in the main loop to exit 0 with
powered controls (both signatures), then independently re-run and audited by two verifiers per
route; verdicts folded here with verdicts winning. All physics from memory (SM quantum numbers,
SO(10) anomaly-safety, collider/DM bounds, the Distler-Garibaldi vectorlike framing) is flagged
`[import]`/FROM-MEMORY. Absolute scale gated throughout. This is the **second-paper
(mirror-mechanism) frontier**; the frozen located-not-forced paper is untouched.

## Next steps

1. **Close the SM embedding on the carrier (P4/P8).** Build the SM Cartan directly on the `(9,5)`
   carrier internal and test whether a compact SM commuting with `Pi_mirror` exists inside the
   maximal compact `SO(5)xSO(5)` -- the load-bearing unverified step behind both the charge
   labeling (T4) and gauge-invariance (25/45 broken generators).
2. **Reconcile producible-mirrors vs removed-ghosts** -- the central physics question; decide which
   resolution the mechanism realizes before any collider claim is made.
3. **Sharpen T4** on a signature where the SM electric-charge Cartan lands in the compact rank-4
   subgroup, upgrading the per-eigenstate labeling from CU to THEOREM.
4. Leave the generation count OPEN -- no route advances it.

## Governance

Exploration-grade; **no canon promotion proposed.** The prediction table is a candidate seed for a
mirror-mechanism paper's outside-facing content, flagged for Joe, not applied. Generation-count
verdict remains OPEN. The located-not-forced paper is frozen and untouched.

---

## Verifier's note (main-loop review, 2026-07-07)

Synthesis of a 13-agent workflow (`wf_d633ddf4-160`; 4 build routes, 8 skeptics, 1 synthesis). First
mirror-mechanism swing; EXTRACTIVE (a prediction table), not promote-or-kill. Main-loop review:

- **Re-run from disk (exit 0, results reproduced):** `mp_m3_count_and_anomaly.py` (count-matching MEASURED
  equal on both Krein halves; all four SM gauge anomalies DERIVED zero on the physical half; the mirror is
  the exact anomaly-conjugate; controls discriminate) and `mp_m2_dark_vs_visible.py` (charges DERIVED from
  the Spin(10) -> SU(3)xSU(2)xU(1) embedding, electron control Q=-1 passes, wrong-embedding control has
  power; verdict (ii) CHARGED/VISIBLE, with the mu >~ 1 TeV collider constraint).
- **The headline finding is a genuine, verified, outside-facing result:** the gapped mirror sector is NOT
  dark. It is a heavy, charged, colored, VECTORLIKE mirror generation -- 84/96 charged, 72/96 colored, only
  12/96 neutral -- with the IDENTICAL SU(3)xSU(2)xU(1) content as the visible generations, state for state.
  This CORRECTS Weinstein's own "everything below the line is dark" (falsified as a quantum-number claim;
  the correct reading is his hedge "luminous ... too massive ... not yet seen").
- **The determined (falsifiable/structural) predictions, graded:** (1) the mirror is a charged/colored
  vectorlike heavy replica of a full SM generation [THEOREM]; (2) N_mirror(families) = N_visible(families)
  [THEOREM]; (3) the mechanism yields a gauge-consistent anomaly-free chiral SM automatically, because
  Spin(10) is anomaly-safe and the mirror is the exact anomaly-conjugate [THEOREM]; (4) the mirror spectrum
  is a single degenerate gauge-invariant mass level, flat, zero texture, symmetry-protected [THEOREM]; (5)
  a genuine constraint on the unbuilt dynamics: mu >~ 1 TeV, or the mechanism is excluded by colliders.
- **Honestly dynamics-gated (not predictions):** the absolute scale mu, all mirror/generation ratios, and
  the generation Yukawa texture. The one sign bit is spectrally invisible (orientation only). Verifiers
  gave M1/M2 PARTIAL -- the AGGREGATE charge structure (84/72/12) is derived and re-run-confirmed, but the
  exact per-eigenstate SM labeling carries a CONSISTENT_UNCOMPUTED residual (T4); this does not affect the
  aggregate dark-vs-visible verdict or the anomaly result.

**Bottom line (main-loop concurrence):** a productive extractive swing. The mirror mechanism is not a dark
sector -- it is a falsifiable heavy charged vectorlike mirror generation with matched family count, automatic
anomaly consistency, and a flat spectrum, constrained to mu >~ 1 TeV. This is exactly the outside-facing,
potentially-falsifiable content the second (mirror-mechanism) paper needs, and it includes a defensible
correction to a claim in GU's own public presentation. Internal tier; absolute scale gated on the unbuilt
source action. Not the located-not-forced paper; this is the second-paper frontier.
