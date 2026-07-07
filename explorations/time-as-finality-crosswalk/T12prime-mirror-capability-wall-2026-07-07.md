---
title: "T12' CONFIRMED: the GU mirror sector is a positivity-forced zero-statistical-trace capability wall (kinematic), so the collective-not-individual reading promotes -- but records-vs-redundancy and the mass connection remain uncomputed"
status: exploration
doc_type: result
created: 2026-07-07
grade: "CONFIRMED (kinematic capability wall), both signatures (9,5) and (7,7). Leg A ~ 9e-16 (individually invisible), Leg B ~ 0.48 (collectively genuine), physical-sector control ~ 0.99 (discriminates). Two honest boundaries: (i) records-vs-redundancy NOT adjudicated (necessary-not-sufficient); (ii) mass/energy connection CONSISTENT_UNCOMPUTED (no dynamics on the carrier). No identity claim; tri-repo guards unchanged."
depends_on:
  - explorations/time-as-finality-crosswalk/mirror-as-collective-capability-boundary-2026-07-07.md
  - canon/ghost-parity-krein-synthesis.md
  - canon/swing-ghost-parity-no-chiral-selection.md
  - explorations/big-swing-2026-07-06/VG-V8-t5-map-attempt.md
scripts:
  - tests/big-swing/t12p_mirror_capability_wall.py
  - tests/generation-sector/ghost_parity_krein.py   # carrier recipe reused
  - tests/big-swing/vg_v8_t5_map_attempt.py          # P_ghost = -Q5 split reused
external_refs:
  - "time-as-finality: T395 (a capability difference can have zero statistical trace on a bounded region); C(R) bounded-region capability object; T392/T393 finality relative to a bounded control region"
---

# T12': is the mirror sector a genuine zero-statistical-trace capability wall?

This is the falsifiable leg of the bridge hypothesis
`mirror-as-collective-capability-boundary-2026-07-07.md` ("the GU mirror sector = collective-not-
individual records"). The hypothesis earns its keep ONLY if the mirror sector is a real capability
difference that is invisible to an individual observer yet genuine (collectively distinguishable) --
the TaF **T395** signature. If the mirror were individually distinguishable, the reading is a rename
and dies; if nothing distinguishes the two states at all, there is no wall, just nothing.

**Verdict: CAPABILITY WALL CONFIRMED (kinematic), both signatures.** With two honest boundaries stated
below. The T12' leg PROMOTES: the collective-not-individual reading is anchored to a specific formal
property, not a metaphor. It is not an identity claim and moves no ledger.

## The test (on the verified 192-dim triplet carrier)

Carrier reused verbatim from `tests/generation-sector/ghost_parity_krein.py` and
`tests/big-swing/vg_v8_t5_map_attempt.py`. Anchors reproduced first, both signatures:

- `rank(Gamma)=128`, `ker(Gamma)=1664`, triplet `dim=192`; `su(2)+` Casimir top eig `=8`.
- triplet Krein signature `(+96, -96, 0)`; `|K|`-eigs all exactly `1` (`K|_W` is an involution).
- `P_ghost = sign(K) = K|_W`; and in `(9,5)`, `P_ghost = -Q5` (compressed internal spatial volume) at
  `3.7e-14`.
- **PHYSICAL** sector `W+` = K-positive eigenspace (96-dim, positive Krein norm); on `W+` the Krein form
  equals `+I_96` (positive-definite physical inner product). **MIRROR/ghost** sector `W-` = K-negative
  eigenspace (96-dim); on `W-` the Krein form equals `-I_96`. They are K-orthogonal.

**Capabilities.** An INDIVIDUAL observer's operations are the `W+`-preserving Krein-unitaries; a
positivity-preserving K-unitary that preserves `W+` also preserves `W- = W+^{\perp_K}`, so it is
**block-diagonal** `U = U_+ \oplus U_-`, `U_\pm \in U(96)`. Individual measurement is the Turok-Bateman
**projector Born rule**: read only `P_+ psi`. COLLECTIVE operations are the FULL Krein-unitary group
`U(96,96)` on all of `W` (K-unitary but not block-diagonal), which can rotate mirror amplitude into the
physical sector.

**States.** Two states that AGREE on `W+` and differ only on `W-`:
`psi = psi_+ + a*phi_-`, `psi' = psi_+ + b*phi_-`, same `psi_+`, same mirror direction `phi_-`,
`a=0.8 != b=0.4`. Both are positive-Krein-norm physical states (`+0.36`, `+0.84`). The mirror difference
is genuinely present: `||psi - psi'|| = 0.40`, K-norm difference `= 0.48`.

## Results (both (9,5) and (7,7); script exit 0)

| quantity | (9,5) | (7,7) | reading |
|---|---|---|---|
| **Leg A** key residual (individual) | `9.1e-16` | `8.9e-16` | mirror difference INVISIBLE to every individual-accessible op |
| **Leg B** key residual (collective) | `0.4800` | `0.4800` | difference is GENUINE, collectively distinguishable |
| **Control C1** (physical-sector pair) | `0.9890` | `0.9971` | physical difference IS individually visible -> Leg A has power |
| Control C2 (mirror present) | `0.40 / 0.48` | `0.40 / 0.48` | not DEGENERATE |

**Leg A (individual invisibility), measured as linear residuals (see numerics note):**
- projector-Born statistics over 400 physical observables: max residual `1.2e-16`.
- after each of 60 individual-accessible (block-diagonal K-unitary) operations, `||P_+ U psi - P_+ U psi'||`
  max `9.1e-16`, Born-stat residual max `1.6e-16`. The accessible operations provably cannot move mirror
  content into the physical sector: `P_+ U psi = U_+ psi_+` is identical for both states.

**Leg B (collective visibility):**
- K-norm difference `0.48`; Krein pairing `<psi|psi'>_K = 0.68` (distinct from each self-norm).
- mirror-number observable `N_- = P_-`: **collective** (raw-Krein) expectation `-0.64` vs `-0.16`
  (diff `0.48`); **individual** (projector-Born) expectation `~1e-17` for both (ghost removed).
- explicit full Krein-unitary boost `V` (K-unitary residual `1.2e-13`, `||P_+ V P_-|| = 10.7 != 0`):
  after `V`, physical components differ, `||P_+ V psi - P_+ V psi'|| = 0.44` -- a collective operation
  makes the mirror difference individually measurable.

**Numerics note.** The trace distance `sqrt(1-|<u,v>|^2)` sqrt-amplifies the ~`1e-16` rounding of the
overlap to a ~`1e-8` floor when the two states are identical. Leg A's pass/fail therefore uses the LINEAR,
un-amplified residuals (`~1e-15`); the trace distance is printed as an annotated auxiliary. For Leg B and
C1 the true value is O(1), so the floor is irrelevant.

## Why this is not the tautology "the projector removes the ghost"

Two distinct anti-tautology arguments, both verified in-script:

1. **Not a hand-inserted pre-projection.** The SAME observable `P_-` that reads the mirror separates the
   two states in its raw Krein expectation (diff `0.48`, the collective reading) while its individual
   projector-Born expectation is `~0`. Leg A's zero is the CLOSURE of the block-diagonal accessible
   operation algebra (verified over 60 random accessible ops) checked against a physical-sector control
   that DOES distinguish (C1 `~0.99`) -- not a definitional pre-projection of the ghost.

2. **Not the generic-subspace fact (the harder objection).** "A difference in ANY subspace is invisible to
   operations preserving it plus a readout of its complement" is generic to any orthogonal decomposition
   and would be content-free. What lifts THIS case above the generic fact: the split is not hand-picked.
   BOTH the projector-Born readout (read only `W+`) AND the block-diagonal operation restriction are FORCED
   by Krein **positivity** (Turok-Bateman) -- `W-` is the unique sector positivity must project out, and a
   positivity-preserving K-unitary must preserve `W+`. So the mirror sector is the **positivity-forced
   blind spot**, not an arbitrary chosen block. That forcing is the Krein/ghost-specific content, and it is
   what ties the abstract capability wall to GU's actual ghost sector rather than to a random subspace.

## Honest boundaries (what CONFIRMED does and does not mean)

- **Kinematic only.** The wall is a statement about state distinguishability on the 192-dim triplet. There
  is no dynamics / S-matrix / Hamiltonian on the carrier, so whether the mass gap `mu` is the ENERGY PRICE
  of crossing the individual<->collective boundary is **CONSISTENT_UNCOMPUTED** -- it requires the unbuilt
  GU source action. The hypothesis' central physical payoff (`mu` = the individual<->collective threshold
  made physical) is NOT reached by this test; it remains a conjecture the test does not touch.
- **Necessary, not sufficient, for "records."** The T395 zero-trace signature is NECESSARY for the "mirror
  = collective RECORDS" reading, but it does NOT by itself distinguish "collective records" from the
  standard ghost reading "unphysical redundancy to be discarded." Both have identical zero individual
  trace. Adjudicating records-vs-redundancy needs the dynamics / boundary-adapter (unbuilt). This test
  shows the mirror sits behind the positivity-forced capability wall; it does not show what is behind the
  wall is a record rather than a gauge artifact.
- **No chirality, no count, no dynamics** are claimed or touched (consistent with
  `swing-ghost-parity-no-chiral-selection.md`: the ghost parity gives consistency, not chirality).

## Connection to the hypothesis and the standing guards

The bridge note said T12' passes iff "no observable / statistic supported on the physical positive-norm
sector can distinguish states that differ only in the mirror sector," with a discriminating control. That
is exactly what is measured: Leg A `~1e-15` with control C1 `~0.99`. So **the reading is anchored, not a
rename** -- a specific formal property (positivity-forced zero-trace ghost) meeting a specific measured TaF
result (T395), with a runnable controlled test, rather than two vague shapes matching.

Standing guards (from the bridge note) are unchanged and load-bearing: NO identity claim (the boundary
adapter is unbuilt; even the "=" is a conjecture); analogy-grade until the adapter is built; cross-repo
material is stress-test input, never support; single-process convergence is weak evidence. This result
moves the GU ledger not at all: it is a kinematic property of the existing carrier, reported honestly.

## Reproduce

```
python tests/big-swing/t12p_mirror_capability_wall.py      # exit 0; prints every cited number, both signatures
```

---

## Verifier's note (main-loop review, 2026-07-07)

Re-run from disk in the main loop: `tests/big-swing/t12p_mirror_capability_wall.py` exits 0, both
signatures (9,5) and (7,7), with Leg A ~ 9e-16 (individual invisibility), Leg B = 0.48 (collective
visibility), and BOTH controls firing (C1 physical-sector pair individually visible at ~0.99 -> Leg A
has power; C2 mirror genuinely present at 0.40 -> not degenerate). Anchors reproduced (Krein (+96,-96,0),
P_ghost = -Q5 at 3.7e-14, W+/W- = 96/96).

- **The anti-tautology argument is the load-bearing part and it holds.** The result is NOT the generic
  "a difference in any subspace is invisible to operations preserving it." What lifts it above that: the
  split is not hand-picked -- Krein positivity (Turok-Bateman) FORCES both the Born-rule readout (read only
  W+) and the block-diagonal restriction of individual-accessible operations. The mirror is the
  positivity-forced blind spot, which is the ghost-specific content. That is a real, verified statement.
- **The verdict is honestly bounded, and I concur with the bounds:** (i) KINEMATIC only -- no dynamics on
  the carrier, so whether the mass gap mu is the energy price of the individual<->collective boundary is
  uncomputed (a conjecture this test does not touch); (ii) zero-trace is NECESSARY BUT NOT SUFFICIENT for
  "collective records" -- it does not distinguish records from the standard ghost reading "discardable
  redundancy," since both have identical zero individual trace.
- **Net for the bridge hypothesis:** the T12' leg PROMOTES -- "mirror = collective-not-individual" survives
  its first real test and is anchored, not a rename. It is NOT proven: the records-vs-redundancy question
  and the mu<->boundary identification are the next tests, both gated on the unbuilt dynamics / adapter.
  No identity claim; tri-repo guards unchanged; no ledger moved.

**Bottom line (main-loop concurrence):** the first falsifiable leg of the mirror-capability bridge came
back positive at kinematic grade, on a positivity-forced (not arbitrary) blind spot, with powered
controls. The interpretation is anchored; the "collective records" reading specifically, and the energy
connection, remain open behind the dynamics.
