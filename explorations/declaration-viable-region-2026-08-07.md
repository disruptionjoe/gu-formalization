---
artifact_type: exploration_result
created: 2026-08-07
status: GENESIS_SET_IS_NOT_SELF_CONSTRAINING__ZERO_INTERNAL_EXCLUSIONS__ALL_REDUCTION_IS_TARGET_IMPOSED
run_id: GUH-20260808T024447Z-source-action-parameter-structure
grade: "CLASSIFICATION OVER FILED TEXT. Every option set and every constraint is
  read from explorations/source-action-requirements-spec-2026-07-13.md and
  classified. The option COUNTS involve reading judgment and are reported as
  illustrative. The central result -- that no member of the constraint set
  excludes any genesis option -- does not depend on the counts and is checkable
  line by line against the five tensions."
ledger: lab/process/conditional-physics-ledger-v0.39.json
ledger_staleness_note: "Analysed against v0.39. The ledger reached v0.68 the same day; re-verify counts before citing. The verdict split moved 32/19/25/6 -> 32/19/26/5 as AC-G1 was superseded by AC-G1a."
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
priority_change: none
row_change: none
residue_touched: []
ledger_rows_declared_before_work: "none. This is a classification of the
  requirements spec, not a Build on a ledger row. No meter movement is claimed
  and none occurred; stated explicitly per the functional channel operating
  contract's no-change reason requirement."
deposit: "PRE-DEPOSIT. Not citable until hostile-reviewed under the standing
  2026-08-03 rule."
follows:
  - explorations/source-action-lens-sweep-viability-2026-08-07.md
---

# The DECLARATION viable region: the genesis set does not constrain itself

## Outcome

The nine `DECLARATION` rows were treated as genesis parameters and the five named
tensions as the constraints coupling them. The question was the size of the
viable region `V`.

**Result: no member of the constraint set excludes any genesis option. Every
reduction in `V` comes from imposing target physics, not from the theory.**

```text
genesis options excluded by internal consistency (I + R) : 0
|V| internal-consistency only                            : 1536   (10.58 bits)
|V| with all target impositions applied                  :   96   ( 6.58 bits)

reduction attributable to the theory                     : 0.00 bits
reduction attributable to the target                     : 4.00 bits
```

## Option sets, as read

| row | options | basis |
|---|---|---|
| SA-Y2 | 2 | texture fork: charges-add / transpose-bilinear `C` (1+2 block) vs charges-subtract / Krein sesquilinear (diagonal). The `Lambda^k` choice is **not** counted as free: the row states `k = 0` *for mass generation*, which is a target imposition |
| SA-Y5 | 2 | hierarchy mechanized vs fitted, stated as an exclusive-or with `SA-Y4`. The space of flavor symmetries strictly larger than `Z/3` is **unbounded as written** and is counted as one branch — see fragility below |
| SA-Y6 | 6 | sector-to-flavor assignment: bijections of three `Z/3` sectors onto three generations |
| SA-Y8 | 2 | Majorana spurion supplied or not |
| SA-G1 | 2 | soldering forced by a new mechanism vs carried as a declaration |
| SA-C1 | 2 | carrier B (`ker Gamma`, index `-38`, can count-select) vs carrier A (full + BRST, index `-42`, permits only) |
| SA-C3 | 2 | realized chiral rank in `{1, 3}` |
| SA-U2 | 2 | agravity vs GU-native fixed-scale |
| SA-U5 | 2 | exhibit a guardian vs accept Rahman-cutoff finite-EFT status |

## Every constraint, classified

| constraint | what it does | excludes a genesis option? |
|---|---|---|
| T1 written-shiab vs causality (`SA-C2`) | acts on the shiab formula | **no** |
| T2 guardian-free UV boundedness (`SA-U5`) | *labels* the guardian-free branch as at best a finite-`Lambda` EFT; both branches stay internally consistent | **no** |
| T3 H45-vs-H48 (`SA-G5`) | acts inside the FIT space | **no** |
| T4 anti-gauge-fixing vs BRST (`SA-C1` side A) | side A *requires* a GU-native local fermionic invariance — a requirement, not an impossibility proof | **no** |
| T5 swampland (`SA-U5`/`SA-G2`) | explicitly speculative tier, carried unresolved | **no** |
| `SA-C1` in-row | "B is FORCED CONDITIONALLY: **if** the source action is to count-select at all" | conditional on target |
| `SA-Y8` in-row | "**ONLY IF** same-chirality masses are wanted" | conditional on target |
| `SA-Y2` in-row | "`k = 0` **for mass generation**" | conditional on target |
| `SA-C3` in-row | must fix the rank in `{1,3}`; nothing internal prefers either | conditional on target |
| `SA-Y5` in-row | exclusive-or with `SA-Y4`: partitions the hierarchy supply route | **no** |

## What this means

**The genesis set is not self-constraining.** The steelmanned reading expected
the tensions to play the role `f < n/3` plays in a consensus protocol — coupling
the genesis constants so that choosing some forecloses others. They do not. Each
of the five is either about a different object (`T1`, `T3`), a label on a branch
that remains consistent (`T2`), a requirement on one branch (`T4`), or explicitly
speculative (`T5`).

**The four bits of reduction come from outside the theory.** They are bought by
imposing count-selection, three generations, same-chirality masses, and UV
completeness. Those are statements about what we are asking GU to reproduce, not
statements GU makes.

**Therefore the external datum is larger than the program accounts for. It
includes the target.** `P1/P2/P3` count datum slots for things GU must import as
*facts*. Nothing counts the target physics that is doing the actual constraining.
That is why "P1/P2/P3 remain unused" has appeared in dozens of artifacts without
meaning anything: the slots were never where the imported content sat.

**This generalizes a trap the repository already names at one row.** `SA-Y6`
carries the W60 warning that identifying sector 0 with the top quark is the
"answer-as-premise trap." This classification says the same hazard is structural
across the genesis set, not local to that row. Every target imposition above is
an answer entering as a premise; the difference is that four of them are load-
bearing for the count and none is booked as an import.

**Ninety-six configurations survive full target imposition.** Even after asking
GU to reproduce everything, roughly `6.6` bits of specification freedom remain,
concentrated in `SA-Y6` (6), `SA-Y2`, `SA-Y5`, `SA-G1` and `SA-U2`. That is a
measure of how far the current specification is from rigid.

## Fragility, stated plainly

- **The counts are judgment.** `SA-Y6 = 6` assumes the assignment is a free
  bijection. `SA-Y5 = 2` collapses an unbounded symmetry space to one branch. If
  either is wrong the bit counts move. **The zero-exclusion result does not
  depend on any count** and can be checked line by line.
- **`R` is what was found, not what exists.** Five tensions are the consolidated
  set as of 2026-07-13. An unfound constraint could exclude genesis options and
  would change the central result. `1536` is an upper bound.
- **"Internal consistency" is the spec's own certification**, which already
  reports no outright contradiction. This artifact adds no consistency proof; it
  only classifies what the recorded tensions do.
- **This is not a claim that target imposition is illegitimate.** Every physics
  program imposes its target. The claim is only that here it is doing the
  constraining while being booked nowhere.

## What would change the result

- A tension shown to exclude a genesis option outright, rather than condition on
  a target, would falsify the central finding directly.
- A bound on `SA-Y5`'s symmetry space would replace the largest judgment call.
- A sixth constraint found among the genesis rows would reduce `1536` and is the
  cheapest way to make the region genuinely internal.

## Fences

No verdict, row, distance, revival trigger, residue count, quotient, fork, canon
entry, lane, priority or queue rank moves. Test B of the run plan (ranking the
quotients) was **not** executed and remains open.
