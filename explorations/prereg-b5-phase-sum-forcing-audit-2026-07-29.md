---
artifact_type: preregistration
status: preregistration
created: 2026-07-29
work_item: B5-INDEPENDENT-RECONSTRUCTION
probe: tests/channel-swings/b5_phase_sum_forcing_audit_probe.py
kill_conditions_declared_before_computation: true
canon_verdict_change: none
---

# Prereg: is the B5 phase residual a single integer, and does anything forced fix it?

## Why this investigation and not the one just done

`archived private execution record/` asked
whether the repository can **freeze** the five native packet fields and returned
`BLOCKED` — no repo-owned construction fixes any of them. That verdict is
accepted here and is **not** re-litigated. Re-running it would be waste.

This investigation asks the strictly different question the block leaves open. The blocked
audit reports a residual of **ten unselected antilinear phase invariants** and
**eleven possible real parity-dimension pairs** (`even` from 58 to 78 in steps of
two, summing to 136). Two things about that residual are not yet established:

1. **What is the actual map** from the `2^10 = 1024` phase assignments onto the
   eleven pairs? If it is a pure function of a *signed sum*, the residual is not
   ten bits — it is **one integer** in an eleven-element set.
2. **Is that integer touched by anything already FORCED?** Eliminating candidates
   using an independently forced result is not the same act as *selecting* phases
   from support multiplicities, which the blocked run correctly refused.

## Construction fork (stated, per `GEOMETER-VS-PHYSICS-OBJECTS.md`)

**Program-native throughout.** The observer-symbol matrix, the formal Krein
adjoint, and the normal-chirality coflip are GU-native objects taken from the
certified ledger. No standard positive-Hilbert adjoint, Green form, or domain is
used, constructed, or substituted — that alternative remains an explicit hostile
control in the blocked run, not a fallback here.

**Explicit scope limit on "forced".** Only constraints *expressible on the
certified finite cell data* can be tested here — chirality grading, provenance
sector, the mirror involution, and the adjoint involution. Constraints that live
outside this finite data (`SA-U4` RS mass, the `g=1` causal cure coefficient,
positivity bounds, `mu_DW`) **cannot** be evaluated by this probe and will be
reported as untested rather than as unforcing. Claiming otherwise would be the
silent-default failure mode.

## Pre-registered terminal outcomes

Exactly one governs:

- **`SUM-REDUCTION + NO-STRUCTURAL-FORCING`** — the eleven pairs are a pure
  function of the signed sum of the ten special-orbit phases, and no structural
  invariant available in the certified data distinguishes the two cells of any
  special orbit. Consequence: the block is **structural, not incidental**, and
  the lawful reopener sharpens to *supply one datum that fixes a signed integer*.
- **`SUM-REDUCTION + STRUCTURAL-FORCING`** — the map is a signed sum **and** some
  available invariant does distinguish within at least one special orbit.
  Consequence: the residual narrows below eleven; report by how much.
- **`NOT-A-SUM`** — the map onto the eleven pairs is finer than a signed sum.
  Consequence: the "ten invariants, eleven pairs" summary is incomplete and must
  be restated before any packet work continues.

## Kill conditions, declared before computation

1. If the `1024 -> 11` map is **not** a pure function of the signed sum, the run
   returns `NOT-A-SUM` and every downstream claim in it is void.
2. If the certified matrix does not reproduce **136 ordered cells, 68 adjoint
   edges, 29 four-cell joint orbits and 10 special two-cell joint orbits**, the
   run aborts — the input is not the object the blocked audit reported on.
3. If a **planted asymmetric phase rule** (a rule that is deliberately not a
   function of the sum) still yields exactly eleven pairs, the sum-reduction is an
   artifact of the counting code and the investigation returns `NOT-A-SUM`.
4. If the ten special orbits are **not** all mirror-involution pairs, the sector
   classification is wrong and that section is void.

## Mandatory controls, positive first

- **P1** reproduce the certified counts (136 / 68 / 29 / 10) from the ledger.
- **P2** exhaustive enumeration of all 1024 assignments, not a sample.
- **P3** independent recomputation of each dimension pair by direct cell counting
  rather than by the sum formula, and agreement of the two methods.
- **N1** planted asymmetric rule must give a different pair count (kill 3).
- **N2** a planted invariant that *does* distinguish within a special orbit must
  be detected by the forcing test, proving the test can fire.

## What this investigation cannot earn

No packet field is frozen. No phase, coflip type, Green form, or domain is
selected. No operator is constructed. No claim, canon, verdict, count, priority,
or posture moves. A `NO-STRUCTURAL-FORCING` result **certifies the existing block
as structural**; it does not weaken or discharge it, and it is not evidence that
the packet is unbuildable — only that it is not narrowable from committed finite
data.
