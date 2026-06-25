---
title: "Three-Cycle Fifteen-Hole Run"
status: canon
doc_type: runbook
scope: repo-local
updated_at: "2026-06-25"
---

# Three-Cycle Fifteen-Hole Run

This is the repo-local workflow for doing three standard five-lane frontier runs in a
row. Use it when the maintainer asks for "three runs", "fifteen holes", "15 quality
holes", or a similar batch.

The unit of work is still `five-lane-frontier-run.md`. This runbook only adds the
sequential wrapper that lets later cycles learn from earlier cycles instead of repeating
or diluting them.

## Purpose

The goal is to produce fifteen quality holes overall:

- five decision-grade holes in cycle 1;
- five decision-grade holes in cycle 2;
- five decision-grade holes in cycle 3.

A quality hole is not a small chore or a vague next step. It is a named missing proof
object, obstruction, branch decision, bridge, invariant, computation, or falsification
gate whose resolution would materially change the GU reconstruction map.

The workflow must optimize for Mission A from `RESEARCH-POSTURE.md`: if GU is
substantially correct, what structures must exist, and can the repo construct, constrain,
or falsify them?

## Non-Negotiable Rule

Do not pad the batch.

If fewer than fifteen quality holes can be drafted without overlap, report the shortage
plainly and run only the quality lanes. A weak lane should not be included just to reach
the number fifteen.

## Preflight

Before cycle 1:

1. Verify the branch and worktree are clean or explicitly account for existing changes.
2. Read `RESEARCH-POSTURE.md`.
3. Read `process/runbooks/five-lane-frontier-run.md`.
4. Review the newest Mission A artifacts and audits.
5. Build a candidate hole bank with at least eighteen candidates when possible.
6. Mark dependencies between candidates.
7. Split candidates into parallel-safe sets.

The candidate bank should distinguish:

- immediate parallel lanes;
- sequential lanes that depend on earlier results;
- lanes that touch the same files and must not run together;
- lower-quality backup lanes that should only run if upgraded into real holes.

## Cycle Workflow

Run each cycle as a complete five-lane frontier run:

1. Select five ambitious, non-overlapping lanes from the current bank.
2. Assign each lane a disjoint owned artifact path and optional audit path.
3. Spawn five workers in parallel only after write scopes are disjoint.
4. Keep coordination, review, and integration in the main thread.
5. Review every returned artifact for substance, overclaiming, and duplicate work.
6. Run every new audit and relevant existing audit.
7. Run `git diff --check`.
8. Remove generated caches such as `tests/__pycache__`.
9. Commit and push the cycle before starting the next cycle.
10. Close the workers for that cycle.

After each cycle, update the hole bank:

- promote newly discovered exact blockers into candidate holes;
- remove duplicate or resolved holes;
- move dependent holes into the next cycle only if their prerequisites are now clear;
- demote weak or summary-only ideas;
- preserve sequential dependencies.

## Quality Hole Acceptance Bar

Each of the fifteen lanes must record:

- a specific GU claim, bridge, or proof object under test;
- the owned output path;
- the sources read first;
- the strongest positive construction attempt;
- the first exact obstruction or missing object;
- a verdict using the vocabulary from `five-lane-frontier-run.md`;
- what would change if the hole closed;
- what would falsify or demote the route;
- the next meaningful computation or proof step;
- an audit/test when a real machine-checkable invariant is available.

At least one of these must be true for every lane:

- it could promote a claim if successful;
- it could demote a claim if it fails;
- it identifies a missing mathematical object that blocks a major reconstruction route;
- it separates two currently conflated branches;
- it turns a vague obstacle into a precise theorem, counterexample, or computation.

## Anti-Overlap Rules

Do not run two lanes in the same cycle if they:

- edit the same artifact or audit;
- need incompatible rewrites of the same claim ledger;
- depend on each other's result;
- ask the same mathematical question in different words;
- both need the same unresolved source extraction.

If overlap is unavoidable, combine the work into one lane or sequence it into the next
cycle.

## Three-Cycle Closeout

At the end of cycle 3, add a plain-English synthesis in the final response. If the run
created a natural repo artifact for synthesis, write it as an additional owned file;
otherwise summarize without inventing a file.

The closeout should answer:

- Which holes were closed, conditional, blocked, failed, or turned into no-go results?
- Which new proof objects became the next frontier?
- Which lanes should be sequential rather than parallel in the next batch?
- Did the three-cycle wrapper improve quality compared with isolated five-lane runs?
- Did any result materially change the next five goals?

## Machine-Readable Workflow

```json
{
  "artifact": "THREE_CYCLE_FIFTEEN_HOLE_RUNBOOK",
  "unit_runbook": "process/runbooks/five-lane-frontier-run.md",
  "cycles": 3,
  "lanes_per_cycle": 5,
  "target_quality_holes": 15,
  "padding_forbidden": true,
  "primary_optimization_target": "Mission_A_information_gain_about_GU_reconstruction",
  "cycle_commit_required": true,
  "cycle_push_required": true,
  "parallelism_rule": "parallel_within_cycle_only_after_write_scopes_are_disjoint",
  "sequential_learning_rule": "update_hole_bank_after_each_cycle_before_selecting_next_lanes",
  "quality_hole_required_fields": [
    "specific_claim_or_bridge",
    "owned_output_path",
    "sources_read_first",
    "strongest_positive_construction_attempt",
    "first_exact_obstruction_or_missing_object",
    "verdict",
    "impact_if_closed",
    "rollback_or_falsification_condition",
    "next_meaningful_computation_or_proof_step"
  ],
  "forbidden_modes": [
    "padding_weak_lanes",
    "summary_only_lanes",
    "overlapping_parallel_write_scopes",
    "duplicate_mathematical_questions",
    "starting_cycle_n_plus_1_before_cycle_n_commit_push"
  ]
}
```
