---
artifact_type: preregistration
status: preregistration
created: 2026-07-29
work_item: B5-INDEPENDENT-RECONSTRUCTION
probe: tests/channel-swings/rung2_dynamical_wall_selectability_probe.py
implements: lab/active-research/conditional-source-action-toy-construction-program-2026-07-26.md
follows:
  - explorations/imposed-wall-triplet-comparator-2026-07-26.md
  - explorations/rung1-finite-coefficient-enumeration-2026-07-29.md
kill_conditions_declared_before_computation: true
canon_verdict_change: none
---

# Prereg: Rung 2 version 2 (dynamical wall) + a reusable selectability test

## Two things in one run, and why they belong together

**Part A — the instrument.** Three times in one day the answer to "can GU select
this from inside?" has been no, and each time the mechanism was identical: an
**exact symmetry of the structure exchanges the two candidates**. That is
mechanical and therefore testable in advance. This investigation builds it as a reusable
instrument:

> Given candidate options and the exact symmetries of the structure, is there a
> symmetry carrying one candidate to another while preserving every declared
> invariant? If yes, the choice is **unselectable from inside** and requires
> external input. If no, it is at least potentially selectable.

**Part B — Rung 2 version 2.** The imposed-wall control
(`imposed-wall-triplet-comparator-2026-07-26`) states the handoff exactly: the
dynamical branch must supply a target-blind source field and topological sector
that **select a wall and its orientation**. This investigation derives the wall from the
field equations rather than imposing it, then asks whether location and
orientation are selected.

They belong together because Part A predicts Part B's answer, so Part B is a
live test of the instrument rather than a demonstration of it.

## Construction fork (per `GEOMETER-VS-PHYSICS-OBJECTS.md`)

**Standard-field**, explicitly. `SRC-TOY-01` permits the first physical
comparator to be a positive-Hilbert domain-wall construction. This is not
transferred to the `(9,5)` Krein / gimmel / `ker Gamma` carrier; a later
transport must prove the real action, physical quotient, operator, and domain.
The triplet is **supplied**, inherited from Rung 1, and no result here derives
three.

## Declared inputs, frozen before computation

Double-well potential `V(phi) = lambda (phi^2 - v^2)^2`; boundary sector
`phi(-L) = -v`, `phi(+L) = +v`; Yukawa coupling `y`; wall matrix = the chirality
grading; supplied triplet `dim T = 3`; finite interval `[-L, L]` on a fixed grid.

The wall is **derived** by minimising the energy functional under those boundary
conditions. Imposing a `tanh` profile would be the failure mode this version
exists to avoid.

## Pre-registered prediction (stated so it can fail)

`SECTOR-SUPPLIED`. Location is expected unselected because translation
invariance makes the wall position a flat direction; orientation is expected
unselected because `phi -> -phi` is an exact symmetry of the potential, so kink
and antikink are exactly degenerate. If either turns out selected, the
prediction is wrong and that is the more interesting outcome.

## Pre-registered terminal outcomes

- **`ACTION-SELECTS`** — the derived dynamics fixes wall location and/or
  orientation without an external input. Report which, and the mechanism.
- **`SECTOR-SUPPLIED`** — the sector and orientation are inputs; the action
  determines only the profile. Report the exact degeneracies.
- **`INSTRUMENT-VOID`** — the selectability test fails its own validation case
  and nothing in Part A or B may be read.

## Kill conditions, declared before computation

1. The instrument **must** reproduce the known answer on its validation case
   (B5 chirality orbits, established unselectable this morning). Failure voids
   the whole run.
2. A **planted symmetry-breaking potential** (adding a cubic term) must make
   orientation register as selectable. If the instrument cannot detect selection
   where it genuinely exists, it is useless and the investigation is void.
3. A **planted translation-breaking term** must make location register as
   selectable.
4. The derived wall must reproduce the imposed-wall control's accessible rank
   for the supplied multiplicity. If it does not, the derivation disagrees with
   the established comparator and Part B is void.

## Controls, positive first

- **P1** derived kink profile satisfies the field equation to stated tolerance.
- **P2** zero-mode count on the derived background matches the imposed-wall table.
- **N1** cubic-term potential makes orientation selectable.
- **N2** linear-gradient term makes location selectable.
- **N3** instrument reproduces the B5 chirality result.

## What this investigation cannot earn

Not anomaly inflow — the Pin/Smith class is `NOT-DEFINED`, so `S_inflow` can
only be standard-field and that gap is declared, not closed. Not GU-native
operator status, not a derivation of three, not a packet field. At most: an
exact statement about what a dynamical source can and cannot select at this
rung, and a validated instrument.

## Preregistered null hypothesis (added 2026-08-03, register M-H16)

The null hypothesis for any dynamical-selection result at this rung is
**|winding| = 1**: generic single-defect energetics select a unit wall, so the
accessible count reduces entirely to the SUPPLIED multiplicity `N` and the run
has demonstrated hosting, not selection (the Jackiw-Rebbi standard; see
`explorations/imposed-wall-triplet-comparator-2026-07-26.md` and the
literature-lens confirmation that the index is representation content in every
published wall construction). A selection claim requires beating this null:
the dynamics must pick `|winding| != 1` or an otherwise non-generic sector,
target-blind. Reading a hosting result as selection is the Layer-0 failure
this line preregisters against.
