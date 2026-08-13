---
artifact_type: preregistration
status: preregistration
created: 2026-07-29
work_item: B5-INDEPENDENT-RECONSTRUCTION
probe: tests/channel-swings/b5_chirality_orientation_audit_probe.py
follows: explorations/b5-phase-sum-forcing-audit-2026-07-29.md
kill_conditions_declared_before_computation: true
canon_verdict_change: none
---

# Prereg: does anything ORIENT the chirality distinction, or only distinguish it?

## The gap this closes

The phase-sum forcing audit found chirality grading is not blind to six of the
ten special orbits — the `E+/E-` pairs across `S`, `imGamma`, `kerGamma`. It was
careful to claim only that the invariant is **capable of firing**, never that a
forced rule fires it.

That gap is the whole question, and it turns on a distinction the previous run
deliberately did not resolve:

- **Distinguishing** means the two cells of an orbit carry different labels.
  Necessary, but it fixes nothing.
- **Orienting** means something canonically says *which* member takes the `+`
  phase. Only an orientation can fix a sign, and therefore the signed sum.

A label difference with no canonical orientation is a **convention**, not a
datum. If chirality only distinguishes, then the six "addressable" orbits are
addressable exactly by an external `Z/2` chirality orientation — which is the
same type of object `located-not-forced` already says the count needs, and
therefore not a narrowing from committed structure at all.

## The exact test

An orientation exists iff the certified ledger **fails to be invariant** under
global chirality exchange. If relabelling every `E+ <-> E-` throughout leaves the
cell set, the multiplicity function, the slot dimensions, and the orbit structure
identical, then the labels carry no canonical direction and no orientation can be
read off the data.

So the investigation computes the global mirror relabelling and tests invariance of each
certified structure independently.

## Construction fork (per `GEOMETER-VS-PHYSICS-OBJECTS.md`)

Program-native throughout: the observer-symbol matrix, the Krein adjoint, and the
normal-chirality coflip. No positive-Hilbert object is used or substituted.

Relevant settled fork carried into the reading, not assumed as a result:
`W201`/`located-not-forced` type the count's external datum as requiring a
**K-definite, non-chirality re-grading**, because chirality eigenspaces are
`K`-null and every `K`-null re-grading preserves net chiral index zero. If this
run returns `DISTINGUISHED-NOT-ORIENTED`, that is a **second, independent arrival**
at the same typing from the finite symbol ledger rather than from index theory —
and it must be reported as corroboration, not as a new theorem.

## Pre-registered terminal outcomes

- **`ORIENTED`** — some certified structure breaks global chirality-exchange
  invariance and canonically orients all six orbits. Residual drops from eleven
  pairs to five. This is the outcome that would narrow the packet.
- **`PARTIALLY-ORIENTED`** — orientation exists for some but not all six. Report
  exactly which and the resulting residual size.
- **`DISTINGUISHED-NOT-ORIENTED`** — chirality separates the cells, but every
  certified structure is invariant under global exchange, so nothing in the data
  picks a direction. Consequence: the six orbits need an external `Z/2`
  orientation and the earlier "addressable" reading is **withdrawn as a
  narrowing** — they are addressable only by a datum the program does not have.

## Kill conditions, declared before computation

1. If the planted-asymmetry control does **not** detect a deliberately broken
   symmetry, the invariance test cannot fire and the investigation is void.
2. If the global mirror map is not an involution on the certified slot set, the
   input is not the object claimed and the investigation aborts.
3. If the six chirality orbits are not exactly the `E+/E-` pairs found by the
   prior run, the two runs are not talking about the same objects; abort.

## Mandatory controls, positive first

- **P1** the global mirror is an involution and permutes the certified cell set.
- **P2** the six chirality orbits reproduce the prior run's identification.
- **N1** planted dimension asymmetry on one chirality type must be **detected**.
- **N2** planted multiplicity asymmetry must be **detected**.

## What this investigation cannot earn

It cannot freeze a packet field, select a phase or orientation, construct a Green
form or domain, or build an operator. A `DISTINGUISHED-NOT-ORIENTED` result does
not weaken the existing block — it **sharpens** it by showing that six of the ten
signs need the same class of external datum the count already needs, and that
only the four X-sector signs are of an unclassified type.
