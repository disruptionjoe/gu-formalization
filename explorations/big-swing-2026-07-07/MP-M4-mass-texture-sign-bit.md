---
artifact_type: exploration
status: exploration
created: 2026-07-07
title: "Mirror mass texture + the sign bit: the mechanism fixes the SHAPE (flat, gauge-invariant, one degenerate 3x2x16 multiplet, generations exactly massless) but not the POSITION (mu). HONEST OUTCOME: the kinematically-determined mirror spectrum is EXACTLY DEGENERATE with zero texture (THEOREM x2 -- projector spectrum {0,1} plus l4>0 quartic uniformity), symmetry-protected and gauge-invariant; the one undetermined sign bit is spectrally INVISIBLE (orientation, A3) and BINARY (gapped-vs-blind phase), leaving NO imprint on the spectrum. No kinematic mass RATIO beyond the trivial ones (mirror/mirror=1, m_gen/mu=0) is fixed; absolute mu and every mirror/generation ratio are dynamics-gated."
grade: "exploration / THEOREM (determined parts) + CONSISTENT_UNCOMPUTED (gated parts). Runs in the main loop to exit 0 with powered controls, both signatures. No absolute-mass claim. All quantum numbers and counts MEASURED, not imported."
depends_on:
  - explorations/big-swing-2026-07-06/VG-V8-t5-map-attempt.md
  - explorations/big-swing-2026-07-07/BIG-SWING-ALIGNMENT-PHASE-NOT-TUNING.md
  - explorations/big-swing-2026-07-07/A1-native-potential-alignment.md
  - explorations/big-swing-2026-07-07/A3-orientation-z2.md
  - explorations/big-swing-2026-07-07/A4-basin-stability.md
  - canon/ghost-parity-krein-synthesis.md
scripts:
  - tests/big-swing/mp_m4_mass_texture_sign_bit.py
---

# Mirror mass texture and the sign bit: what the kinematics fixes, what the dynamics gates

**The route.** V8 + the alignment swing established a mostly-built positive kinematic result: the
aligned condensate `phi*Pi_mirror` (`Pi_mirror = (I - K|_W)/2 = (I + Q5)/2`) gaps all 96 mirror
states while keeping all 96 generation states massless, `[M,P]=0`, as the exact global minimum of a
native potential on an open region of couplings (A1/A4), down to **one coupling sign bit** (A2). This
route (M4) extracts what that mechanism DETERMINES about the mirror *spectrum* — the pattern of the 96
mirror masses, any fixed ratio, and whether the sign bit is observable — and separates it cleanly from
what needs the unbuilt dynamics.

**The honest constraint (restated).** The **absolute** mirror mass scale `mu` is the condensate VEV
magnitude, set by the unbuilt source action. **No absolute-mass claim is made anywhere.** M4 asks a
strictly *shape* question: given the scale, what is the texture, and does the one sign bit leave a
spectral imprint?

## Honest outcome

The mechanism fixes the **shape** of the mirror spectrum completely and fixes its **position** not at
all — exactly the determined/gated split the swing demands. The determined shape is maximally simple:
a single flat, gauge-invariant, degenerate level.

## What the kinematics DETERMINES (THEOREM)

**(M4-1) Exact degeneracy, zero texture.** The mirror mass matrix `M(phi) = phi*Pi_mirror` has
spectrum **exactly** `{0^96 (generations), phi^96 (mirrors)}`. `Pi_mirror` is a rank-96 orthogonal
projector — its eigenvalues are identically `{0,1}` (verified: idempotent to `9e-15`, spectrum
`{0^96,1^96}`) — so all 96 mirrors sit at **one** mass `mu = phi` with band width `~1e-14`. The
kinematics forces a **flat** mirror spectrum: no family splitting, no isospin splitting, no
generation hierarchy. The mass scales linearly in the condensate amplitude, which is exactly why the
absolute scale is a free multiplier (dynamics-gated).

**(M4-2) The degeneracy is symmetry-protected, and the mirror mass is gauge-invariant.**
`Pi_mirror = (I - P)/2` commutes with the **entire** unbroken group on `W`: both families
`su(2)+ x su(2)-` and the maximal-compact internal `so(5)_s x so(5)_t` (all residuals `~1e-14`, 26
generators checked). It does **not** commute with the internal boosts (the non-compact directions
`Q5` already breaks; `||[Pi_mirror, e4e9]|| = 13.9`). Since any *physical* compact gauge group sits
inside the maximal compact (the internal group is non-compact `SO(5,5)` per the canon A0 correction,
whose maximal compact is `SO(5)xSO(5)` — flagged as a group-theory input, not a numeric import), the
mirror mass is **gauge-invariant**: it does not split within gauge multiplets, and it is a
**vectorlike (Dirac/Majorana-type) mass that needs no electroweak breaking**. The 96 mirrors form one
degenerate multiplet `96 = 3 x 2 x 16`, measured directly on the mirror half `W_-` (su(2)+ weights
`{-2,0,+2}x32`, su(2)- weights `{-1,+1}x48`, uniform `so(5)_s` Casimir — all derived, none imported).

**(M4-3) The quartic actively selects the flat texture** (it is the minimizer, not an ansatz). Among
all mirror-sector mass operators of fixed `tr(M^2)`, the uniform (projector) one **minimizes**
`tr(M^4)` by Cauchy-Schwarz: `tr(Pi^4) = tr(Pi^2)^2/96` exactly, and every split raises `tr(M^4)`
(300 random draws: min excess `+72.7`; an explicit 48/48 two-level split costs `+100%`). So the same
`l4>0` stable-cone quartic that selects the mirror-hiding vacuum in A1 **drives** the spectrum to the
flat texture — a mirror texture would cost potential energy. This ties the degeneracy to A1b's
reduction lemma from the mass side.

**(M4-4) The sign bit leaves no spectral imprint.** The one undetermined coupling sign
`sign(lq + l4/192) = sign of tr(Q5 Phi^2)` selects the **orientation** (which K-half gaps). The
opposite orientation is `phi*Pi_generation = phi*(I + P)/2`, and `chi` conjugates one into the other
(`||chi Pi_mir chi - Pi_gen|| = 3.7e-14`, A3 at the operator level). The two sign choices give the
**identical** mass multiset `{0^96, phi^96}` (max difference `1.6e-15`) — only the *label* (which half
is called physical) swaps. So the orientation content of the sign bit is spectrally **invisible**. Its
only physical content is **binary**: the gapped-mirror phase vs the mirror-blind phase (whether the
vacuum gaps at all, A4). Within the gapped phase it produces no texture, no ratio, no observable. **It
is not a spectral knob.**

**(M4-5) The generation half is exactly massless** under the mechanism (`m_gen/mu = 0` to `1e-15`) —
a structural consequence of the aligned projector, orientation-independent.

## What stays DYNAMICS-GATED (CONSISTENT_UNCOMPUTED — never predicted)

- **The absolute scale `mu`** (the condensate VEV magnitude, a free linear multiplier).
- **The generation Yukawa texture** (the Standard-Model fermion masses): a *different*, unbuilt
  condensate. The generation half is massless under the *mirror-hiding* mechanism; whatever gives the
  three generations their masses is a separate object.
- **Therefore any mirror-gap / generation-mass RATIO** — both scales are unbuilt.
- **Whether GU's source action supplies the gapping sign** (the load-bearing A2 sign bit).
- **Radiative / EWSB lifts of the flat degeneracy.** Once dynamics exists, the flat mirror level will
  generically be split by loop corrections and by whatever couples the mirror sector to the electroweak
  scale; that splitting is *expected to exist* but its size is entirely gated. The determined statement
  is the *leading-order* flatness protected by the maximal-compact symmetry.

## The ratios, precisely

| quantity | value | status |
|---|---|---|
| mirror / mirror mass ratio | `1` exactly (flat) | **DETERMINED** |
| `m_generation / mu` (aligned limit) | `0` exactly | **DETERMINED** |
| mirror band width / `mu` | `0` (no texture) | **DETERMINED** |
| Weyl-point relation `phi = mu/q` | the alignment condition itself, not an independent number | **DETERMINED** (definitional) |
| absolute `mu` | — | **GATED** |
| mirror-gap / generation-mass | — | **GATED** (different condensate) |
| degeneracy-lift size (loops, EWSB) | — | **GATED** |

The misaligned generic toy `M = mu*I + phi*q*Q5` (with `Q5 = -1` on generations, `+1` on mirrors)
gives `m_gen = |mu - q phi|`, `m_mir = |mu + q phi|`; the Weyl point `phi = mu/q` (generations
massless, mirrors at `2mu`) is exactly the equal-weight alignment condition, not a free prediction. In
the aligned projector limit the generation branch is massless at *all* `phi`, so there is no
independent ratio to read off.

## Controls (discriminating power)

A generic chi-anticommuting (pure `E-`) condensate **splits** the mirror band (band width `~3.8` at
unit norm — a texture, not flat); a generic mixed P-even condensate splits **both** bands. So the
zero-width mirror band is **special** to the aligned projector direction the mechanism selects, not an
artifact that any mirror-gapping operator would produce. The flatness checks have power.

## Signature independence

The full result reproduces in the `(7,7)` signature (`i*(e11e12e13) = -P` to `7e-14`; flat 96-fold
mirror degeneracy with exactly massless generations to `1e-14`): the flat texture is not a `(9,5)`
artifact.

## The honest boundary (the deliverable)

The mechanism **determines the shape** of the mirror spectrum and **does not determine its position**:

- **Determined (falsifiable/structural):** the mirror sector is a *single degenerate level* — one
  mass, 96-fold, a `3 x 2 x 16` multiplet — that is **gauge-invariant** (vectorlike, no EWSB), with the
  generations exactly massless alongside it. This is a *prediction about the shape of the spectrum*:
  a discovered mirror sector with a non-flat leading texture, or one whose mass breaks the SM gauge
  symmetry (chiral mirror masses at leading order), or a mirror count not matching `3 x 2 x 16`, would
  be in tension with the mechanism. The sign bit adds nothing here — it is spectrally invisible.
- **Gated:** where that level sits (`mu`), and how it relates to any other scale. No number.

This is the correct M4 result: the swing asked what the kinematics + the one sign bit fix about the
texture, and the answer is *everything about the shape, nothing about the scale* — with the sign bit
demoted from a potential texture knob to a spectrally-silent binary phase switch.

## Governance

Exploration-grade; no canon promotion proposed. The generation-count verdict stays **OPEN** (untouched
— this route is about the mirror spectrum's shape, not the count). From-memory / structural inputs are
flagged in-script (the `SO(5,5)` maximal compact `SO(5)xSO(5)`; "a compact gauge group sits in the
maximal compact"). No absolute mass is claimed. Verification tier: internal, main-loop, exit 0, both
signatures, controls with discriminating power.
