---
artifact_type: exploration
status: exploration
created: 2026-07-29
lane: "1"
work_item: B5-INDEPENDENT-RECONSTRUCTION
title: "B5 PHASE-SUM FORCING AUDIT: the blocked packet's ten-phase residual is ONE INTEGER, not ten bits -- the eleven real parity-dimension pairs are a pure function of the SIGNED SUM of the ten special-orbit phases (even = 68 + sum, sum in {-10,...,+10} step 2), verified by exhaustive enumeration of all 1024 assignments with direct cell counting agreeing with the sum formula. FORCING SPLIT: chirality grading is NOT blind to 6 of the 10 special orbits (the E+/E- pairs in S, imGamma, kerGamma); provenance sector, slot dimensions, and cell multiplicity are blind to ALL ten. The four X-sector orbits (X1T, X23, X2T, X32) are blind to every invariant available in the certified data. Verdict SUM-REDUCTION + STRUCTURAL-FORCING."
grade: "EXACT for the finite enumeration, the sum-reduction, and the blindness/non-blindness classification (tests/channel-swings/b5_phase_sum_forcing_audit_probe.py, all controls pass incl. one that FIRED and caught a sign-convention error before it became a claim). CONDITIONAL and NOT established: that any FORCED GU result actually assigns the six chirality-addressable signs -- the probe shows only that the invariant is capable of firing, never that a forced rule fires it. No packet field frozen, no phase/coflip/Green-form/domain selected, no operator built."
prereg: explorations/prereg-b5-phase-sum-forcing-audit-2026-07-29.md
probe: tests/channel-swings/b5_phase_sum_forcing_audit_probe.py
construction: "program-native throughout per GEOMETER-VS-PHYSICS-OBJECTS.md -- the observer-symbol matrix, formal Krein adjoint, and normal-chirality coflip are GU-native. No positive-Hilbert adjoint, Green form, or domain used or substituted."
depends_on:
  - lab/process/runs/GUH-20260729T131135Z-b5-native-packet-source-audit/run-plan.md
  - tests/shiab_b5_observer_symbol_multiplicity_matrix.py
  - tests/shiab_b5_krein_mirror_orbit_reduction.py
  - GEOMETER-VS-PHYSICS-OBJECTS.md
kill_conditions_declared_before_computation: true
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
outcome: "SUM-REDUCTION + STRUCTURAL-FORCING"
---

# B5 phase-sum forcing audit

## What this run is not

`GUH-20260729T131135Z-b5-native-packet-source-audit` asked whether the repository
can **freeze** the five native packet fields and returned `BLOCKED` — no
repo-owned construction fixes any of them. **That verdict is accepted here and is
not re-litigated.** Nothing below freezes a field, selects a phase or coflip
type, constructs a Green form or domain, or builds an operator.

This run asks the different question the block leaves open: *what shape is the
residual, and can anything already available narrow it?* Narrowing a candidate
set with an independently available invariant is not the act the blocked run
refused, which was selecting phases from support multiplicities.

## Result 1 — the residual is one integer, not ten bits

Exhaustive enumeration of all `2^10 = 1024` antilinear phase assignments, with
the even/breaking split computed by **direct cell counting** and independently by
a sum formula, agreeing on every assignment:

```text
even = 68 + sum(signs),      sum(signs) in {-10, -8, ..., +8, +10}
```

The baseline `68` is the certified linear-coflip even count, recovered here from
the four-cell orbits plus the symmetric half of the special orbits rather than
assumed. Because flipping one sign changes the sum by two, the eleven values run
`58, 60, ..., 78` in steps of two — reproducing the certified reduction exactly.

**The consequence is the point.** The ten phase invariants span a `2^10` space but
have only an **eleven-valued effect** on the real coefficient dimension, and that
effect depends *only on the signed sum, never on which phases carry which sign*.
So the packet's real-dimension residual is **one integer in `[-10, +10]`**.

A datum that fixes that sum fixes the coefficient dimension **without selecting
any individual phase**. That is a materially cheaper reopener than "freeze ten
phases," and it is a different kind of object.

## Result 2 — the forcing split: six addressable, four blind

For each invariant expressible on the certified finite cell data, does it take
different values on the two cells of a special orbit? An invariant blind to the
swap cannot fix that sign.

| invariant | distinguishes |
|---|---|
| chirality grading | **6 of 10** |
| provenance sector | blind to all 10 |
| slot dimensions | blind to all 10 |
| cell multiplicity | blind to all 10 |

The six are exactly the `E+ <-> E-` pairs across the three provenances — `S`,
`imGamma`, `kerGamma`, each with an `L16` and an `R16` orbit. The four blind ones
are exactly the **X-sector** orbits: `X1Tm/X1Tp`, `X23m/X23p`, `X2Tm/X2Tp`,
`X32m/X32p`.

**What this does and does not earn.** It establishes that chirality grading is
*capable* of breaking six of the ten ties, and that **nothing available in the
certified data can break the remaining four**. It does **not** establish that any
FORCED GU result actually assigns those six signs — that is a separate question
this run did not ask and cannot answer.

If such a rule exists, the residual narrows from eleven pairs to **five** (four
free signs give sums `c-4, c-2, c, c+2, c+4`). If it does not, the eleven stand.

## The honest reading

The block is **structural in its X-sector half**. Four of the ten phases are not
narrowable from committed finite data at all — not because nobody looked, but
because every invariant the certified ledger carries is blind to them. That is
worth knowing before more search is spent there.

The other half is **potentially addressable** and was not previously separated
out. The chirality-addressable six are where a forced rule could bite.

## Controls, including one that fired

All controls pass. Recorded because it matters: the control **"pairs run 58..78
in steps of two" FAILED on first execution** and caught a sign-convention error
— the first model contributed `0/+1` per orbit where the certified structure
contributes `-1/+1`, yielding eleven values in steps of one. The kill condition
voided the run rather than letting a wrong dimension formula become a finding.
The corrected model derives its baseline from the ledger instead of asserting it.

- `P1` certified counts reproduced: 136 cells, 68 adjoint edges, 29 four-cell and
  10 special two-cell joint orbits.
- `P1b` every special orbit is a mirror-involution pair.
- `P2/P3` exhaustive 1024-assignment enumeration; direct counting agrees with the
  sum formula on every assignment.
- `N1` a planted position-dependent (non-sum) rule gives 56 distinct values, not
  eleven — so the sum-reduction is not an artifact of the counting code.
- `N2` a planted orbit-breaking invariant is detected, proving the forcing test
  can fire.

## Scope limits, binding

Only constraints expressible on the certified finite cell data were tested.
**`SA-U4`'s forced RS mass, the `g=1` causal cure coefficient, positivity bounds,
and `mu_DW` live outside this data and are reported UNTESTED — never as
unforcing.** Any of them could still fix the sum, and claiming otherwise from
this probe would be the silent-default failure mode
`GEOMETER-VS-PHYSICS-OBJECTS.md` warns about.

The single-carrier O-b reduction is not touched here, and the 2026-07-22
operator/domain correction stands unaffected.

## Reopeners, in cost order

1. **Cheapest and new:** is there a FORCED GU result that assigns the chirality
   sign on the six `E+/E-` special orbits? If yes, the residual drops to five
   pairs from committed structure alone.
2. **The named remainder:** what class of datum could fix the four X-sector
   signs? By this run, nothing in the certified ledger can.
3. **Outside this data:** do `SA-U4`, the `g=1` cure, positivity, or `mu_DW`
   constrain the signed sum? Untested here and each is a separate computation.

## What moved

Nothing. No claim, canon, verdict, count, priority, posture, or packet field.
`B5-INDEPENDENT-RECONSTRUCTION` remains blocked and `SRC-COH-1` remains open. The
contribution is a sharper description of the residual the block leaves behind,
and a split of it into an addressable half and a provably-unaddressable-here half.
