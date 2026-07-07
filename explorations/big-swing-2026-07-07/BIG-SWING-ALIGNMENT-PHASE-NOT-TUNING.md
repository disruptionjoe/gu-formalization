---
artifact_type: exploration
status: exploration
created: 2026-07-07
title: "Alignment swing: does any GU-native dynamics select the V8 mirror-hiding condensate direction? HONEST OUTCOME: strong bounded-positive. Alignment is a PHASE of the native invariant potentials, not fine-tuning (A1, phase theorem, numerics pending); the orientation Z2 is DISCHARGED as a Krein-labeling redundancy (A3, THEOREM x2); the aligned configuration is a SADDLE under orientation-blind potentials but the exact GLOBAL MINIMUM under one orientation-odd native coupling tr(Q5 Phi^2) with the physical sign (A4, THEOREM x2). V8's three-item invoice (direction + orientation bit + alignment hypothesis) collapses to ONE undetermined SIGN BIT, resolvable only by the still-unbuilt source action. Count stays OPEN."
grade: "exploration / strong bounded-positive. A3, A4 THEOREM grade (both signatures where applicable, powered controls, re-run in the main loop to exit 0). A1 analytic phase theorem at theorem grade but numerical confirmation PENDING (script is heavy; exit-0 receipt not yet landed). A2 (the no-go twin) DID NOT RUN (output-token cap) -- but A1 and A4 exhibit explicit native potentials on which alignment wins, which refutes the strong no-go A2 was to attempt. No forbidden target imported; no dynamics (no S exists); every statement 'the native potential class forces X', never 'GU forces X'. Count stays OPEN."
depends_on:
  - explorations/big-swing-2026-07-07/A1-native-potential-alignment.md
  - explorations/big-swing-2026-07-07/A3-orientation-z2.md
  - explorations/big-swing-2026-07-07/A4-basin-stability.md
  - explorations/big-swing-2026-07-06/VG-V8-t5-map-attempt.md
  - explorations/big-swing-2026-07-06/VG-V2-fourth-seat-gauge-sector.md
  - canon/ghost-parity-krein-synthesis.md
scripts:
  - tests/big-swing/as_a1_native_potential_alignment.py
  - tests/big-swing/as_a3_orientation_z2.py
  - tests/big-swing/as_a4_basin_stability.py
---

# Alignment swing: is the mirror-hiding direction dynamically selected, or another import?

**The swing.** V8 (2026-07-06) constructed the mirror-hiding condensate direction at kinematic grade:
`P_ghost = -(internal spacelike volume)|_W` is Clifford-native, and the channel `phi*Pi_mirror` gaps all
96 mirrors while keeping all 96 generations massless with `[M,P]=0`. Its one unproven hypothesis was
ALIGNMENT: nothing showed any dynamics flows the condensate INTO that direction, and V8 found the gap
closes near misalignment `eps ~ 1`. This swing attacked alignment from four sides: A1 (does any native
invariant potential have its minimum on the mirror-hiding direction?), A2 (no-go twin: prove no native
potential can see it), A3 (is the leftover orientation Z2 fixed by native structure or a genuine
modulus?), A4 (is the aligned configuration a stable basin?).

## Honest outcome: strong bounded-positive, invoice collapses to one sign bit

Alignment is not fine-tuning and it is not an imported direction. It is a **phase** of GU's own native
invariant potentials -- there is an open region of native couplings on which the mirror-hiding
configuration is the exact global minimum -- and the only thing still not determined from inside is a
single coupling SIGN, whose value awaits the unbuilt source action.

## A1 -- the potential scan (CONSISTENT_UNCOMPUTED; phase theorem at theorem grade, numerics pending; verifiers PARTIAL x2)

The native invariant structure on the P-even condensate space collapses: because `K|_W = P = -Q5` (V8),
the only parity-sensitive invariants are the Krein supertraces `Str(Phi^n) = tr(sign(K) Phi^n)`, native
at the grade of `K`. For the reduced native family `V = -t2 + l0*t2^2 + lq*Str2^2 + l4*t4` there is an
exact phase theorem over the full 18432-dim P-even space: on the open region `lq < -l4/192` inside the
stable cone the global minima are the mirror-hiding corner (all 96 states of one parity sector uniformly
gapped, the other 96 exactly massless -- V8's `Pi_mirror` payoff realized as a potential MINIMUM); on
`lq > -l4/192` the vacuum is mirror-blind. So alignment no longer needs an imported DIRECTION -- it needs
an imported (or someday derived) SIGN: in the reduced family exactly one bit, `sign(lq + l4/192)`.
**Status:** the analytic phase boundary is theorem-grade; the numerical minimization sweep confirming it
is heavy and had not returned exit 0 at handoff, and did not complete on a main-loop re-run (timeout).
Numerics PENDING; the leg is graded CONSISTENT_UNCOMPUTED until the sweep lands.

## A3 -- the orientation Z2 (THEOREM, kinematic; verifiers SUSTAINED x2; main-loop re-run exit 0)

The leftover "which half is physical" choice is **discharged**: it is a labeling redundancy of the Krein
axioms, not physical data. The lock `P_ghost = K|_W` (3.7e-14) makes the orientation flip and the
Krein-sign flip ONE Z2; a two-line theorem excludes any K-preserving flipper; the flip is implemented by
the GU-native intertwiner `chi` (commutes with all 91 gauge generators, both family actions, `J_quat`;
sends `(K,P,Q5,Pi_mirror) -> (-K,-P,-Q5,Pi_generation)`); the sign of `K` is fixed by no axiom
(`-beta_S` passes the full observable battery at 0.0e+00, and `Ad(-K)=Ad(K)` so V2's Cartan seat `theta`
is sign-blind); no K-invariant observable distinguishes the halves. And `Pi_mirror = (I - K|_W)/2`
identically, so in EVERY orientation the condensate gaps the K-negative (ghost) half and leaves the
K-positive (physical) half massless. **Sharp conclusion:** the theory does not owe "which half" -- the
invariant, orientation-free prediction is "the ghost half gaps." V8's invoice drops from three items to
two; the alignment hypothesis is restated orientation-free as "the condensate couples to the Krein form
itself."

## A4 -- basin and stability (THEOREM, potential-class scope; verifiers PARTIAL x2; main-loop re-run exit 0)

Under every orientation-blind (chi-symmetric) native quartic potential the aligned configuration is an
exact **saddle** (Hessian `{-2m^2 x 9216, +4m^2 x 9216}`; generation masslessness sits at the top of a
double well; global minima are mirror-blind, V1-consistent). But the measured commutant `{I,P,chi,P.chi}`
admits exactly one more P-even K-self-adjoint quadratic weighting -- `Q5` itself -- and the single
orientation-odd native invariant `tr(Q5 Phi^2)` at coupling `h < -m^2` makes the aligned configuration
the **global minimum** (Hessian positive-definite, no zero modes, symmetry-isolated; per-channel proof +
300 random configs). `chi`-conjugation flips `h`, so a chi-symmetric potential provably cannot stabilize
alignment -- consistent with A3 (orientation lives in the same `chi` Z2) and A1 (the sign bit). Krein
positivity `[M,P]=0` is exact across the entire P-even basin at every misalignment amplitude. The Weyl
point (massless generations) is the aligned configuration at scale `2mu`, sitting at the basin bottom with
zero tuning iff the Dirac scale is condensate-born. **Card:** SADDLE (orientation-blind) / ATTRACTOR-
COMPATIBLE (orientation-committed, `h < -m^2`) / MARGINAL (`h = -m^2`).

## A2 -- the no-go twin: DID NOT RUN

The adversarial "prove no native potential can see the alignment datum" route hit the 64k output-token
cap and produced no result. It is not lost science: A1's phase theorem and A4's global-minimum result
both EXHIBIT native potentials on which alignment wins, which directly refutes the strong form of the
no-go A2 was to attempt. The weaker, honest residue A2 might still have found -- that alignment requires
a sign no native invariant fixes -- is exactly what A1/A4 concluded independently.

## What this settles / does not settle

**Settles (at stated scopes):**
1. Alignment is a **phase, not fine-tuning**: an open region of GU-native couplings has the mirror-hiding
   configuration as the exact global minimum (A1 analytic + A4 global-minimum theorem).
2. The orientation Z2 is **not physical data** (A3, theorem): the invariant prediction is "the ghost half
   gaps"; the theory does not and need not say which half.
3. V8's three-item invoice (direction + orientation + alignment) collapses to **one undetermined sign
   bit** -- the sign of the orientation-odd native coupling `tr(Q5 Phi^2)` (equivalently `sign(lq+l4/192)`).
4. Krein positivity holds across the whole basin (A4), so nothing in the breaking endangers consistency.

**Does not settle:**
- **The sign bit itself.** No source action exists, so whether GU's dynamics generates `tr(Q5 Phi^2)`
  with the stabilizing sign is uncomputable, not merely uncomputed. This is now the single load-bearing
  question for the whole mirror sector.
- **A1's numerics** (phase boundary confirmed analytically, sweep pending).
- **The generation count. Stays OPEN.** This swing is about hiding mirrors and stabilizing the vacuum, not
  about deriving 3 -- the physical sector remains achiral `96 = 3x2x16`, and the count import (V7) is
  untouched.

## Where the wall is now

One bit, one object: **does GU's unbuilt source action generate the orientation-odd coupling
`tr(Q5 Phi^2)` with the sign `h < -m^2`?** If yes, the mirror-hiding vacuum is a genuine attractor built
entirely from native structure and V8's alignment hypothesis is discharged; if the sign is opposite or
the coupling is absent, the vacuum is mirror-blind and alignment returns as an import. Everything upstream
(the direction, the orientation, positivity) is now native and settled at kinematic/potential grade.

## Next steps

1. Complete A1's numerical sweep (confirm the analytic phase boundary `lq = -l4/192`); cheap, just slow.
2. Re-run A2 as a bounded no-go: "no chi-symmetric native potential stabilizes alignment" is already
   proven in passing (A4); state it cleanly as the honest half-no-go.
3. The sign bit is a source-action question -- it joins the count as the two things the unbuilt dynamics
   must supply. Both are now single, sharply-typed targets rather than open fogs.

## Governance

Exploration-grade; no canon promotion proposed here. The V8/A-series results together are a candidate
for a canon note ("the mirror-hiding vacuum: native direction, discharged orientation, one open sign"),
flagged for Joe, not applied. Generation-count verdict remains OPEN; any verdict/status flip pauses for
Joe. Verification tier: internal adversarial (A3/A4 sustained by both verifiers and re-run in the main
loop to exit 0; A1 numerics pending; A2 not run).
