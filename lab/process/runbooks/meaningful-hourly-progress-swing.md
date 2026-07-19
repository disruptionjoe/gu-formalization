---
title: "Meaningful Hourly Progress Swing"
status: active
doc_type: runbook
scope: repo-local
created: 2026-07-15
portfolio: lab/process/research-portfolio.json
---

# Meaningful Hourly Progress Swing

This is the default GU hourly Progress run. It executes one coherent research swing selected from the steward-maintained four-lane portfolio. Lanes 1 through 3 are Progress lanes. Lane A is Stewardship and is never selected by this runbook. This replaces Lean-only hourly selection and tiny bounded-slice behavior.

The target is one meaningful research delta per run, not one file, one lemma, or one commit.

Use one technical lane and one local heavy job at a time. Do not routine-fanout the hourly run. Divergent
multi-lane fanout remains maintainer-directed through `five-lane-frontier-run.md`.

## Selection

1. Load the standard CapacityOS Progress workflow, GU steward context, and local instructions.
2. Create the run plan before research work and inspect recent open run plans for collisions.
3. Read `lab/process/research-portfolio.json`, including the `lane_catalog`, `selection_contract`, and `work_items`.
4. Read the most recent materially relevant `Next-Work Handoff`. Recheck its candidates against current dependencies, collisions, gates, and repo state.
5. Build the eligible set from work items in numbered Lanes 1, 2, and 3. Never select Lane A in Progress mode.
6. Within each numbered lane, identify its strongest eligible work item using the declared score, current evidence, dependencies, kill and switch conditions, and any adaptive internal ranking. If the selected work item defines an `assessment_source`, read it before final selection. If it defines `internal_work_items`, select its highest-ranked unblocked component.
7. Compare the three lane leaders and select the worthiest coherent swing. Lane 1 always retains the protected North-Star purpose, but lane number is not an automatic every-run schedule. Selecting Lane 2 or Lane 3 does not demote Lane 1.
8. Never select `GATED_P2C`, `GATED_NEW_STRUCTURE`, `GATED_FIXED_QUANTITY`, `WAITING_EXTERNAL`, `MONITOR`, `PARKED`, `RESOLVED_NO_GO`, `PAPER_READY`, or `NEEDS_JOE` work as an hourly technical target.
9. Difficulty, activity, finishability, or an easier proof are never sufficient reasons to move work ahead of Lane 1. A non-Lane-1 selection must be justified by current information value, time sensitivity, dependency leverage, collision avoidance, a decision-grade Lane-1 endpoint, or another valid portfolio signal.

When `NO-GO-SCOPE-CHALLENGE` is the selected internal item, also read
`lab/process/recovery-no-go-defense-protocol.md` and
`lab/process/recovery-no-go-defense-register.json`. Select the highest-information pending history audit or
broad swing under that register. The branch-local no-go remains evidence throughout the challenge.

The hourly run does not mutate or authoritatively reprioritize the portfolio. It does re-rank work inside the lane it used and then re-rank all three numbered lanes through the reusable CapacityOS handoff flow. The daily steward in Lane A decides whether that evidence changes durable portfolio state.

## A meaningful swing

Before implementation, state:

- the decision question;
- the exact construction fork and why it is used;
- the load-bearing source objects;
- the first kill or closure condition;
- the expected owned output paths;
- the evidence needed for a decision-grade endpoint.

A swing should normally combine the linked work needed for a real decision. Depending on the lane, that may include derivation, counterexample search, literature or data verification, code, tests, Lean, and a written result. If the first check closes quickly, continue to the next logically linked checkpoint in the same lane when it remains safe and coherent.

Do not pad the run with unrelated work. Do not split one natural proof-and-test packet merely to maximize run counts.

## No-go admission and defense

Before an hourly result is banked as a new `NO_GO`, review prior GU work for the same substantive obstruction.
Search canon, claim and hypothesis ledgers, corrections, explorations, tests, receipts, and superseded steering
history by mechanism as well as label. Record whether the obstruction was previously cleared, the construction
in which it was cleared, and whether that clearance applies to the current frozen construction.

- Same obstruction, same construction, previously cleared: return `INTEGRITY_CONFLICT` in the receipt and
  reconcile the premises before banking the new no-go.
- Same obstruction, different construction: preserve a construction-relative no-go and identify the fork.
- No material prior encounter: record `NO_PRIOR_CLEARANCE_FOUND` plus the bounded search receipt.

The history audit does not count toward the minimum three broad defense swings. For every admitted branch-local
no-go, apply the defense protocol: type and fork the obstruction, attempt a genuinely different construction,
then adversarially adjudicate survivors. Predeclare the construction space. A reframe must explain more rather
than merely survive, and a positive escape never erases the source counterexample.

Use the current six-axis specification discipline during this work: Layer 0 semantic alignment plus L1-L7.
Compare historical clearances by their signatures, and do not admit a Swing-2 escape until its axis deltas,
literature anchors, target bridge, and first falsification test are explicit. Vague axes return `UNDERDEFINED`.

When the history audit closes without an integrity conflict and run capacity remains, continue into Swing 1 in
the same run. Do not emit a history-only receipt just to increase the count. After every current target completes
Swing 1, follow the register's conditional-unitarity interleave, then resume Swing 2 and Swing 3.

## Required result vocabulary

Every technical swing ends with one operational result:

```text
CLOSED
CONDITIONAL
BLOCKED
FAIL
NO_GO
UNDERDEFINED
INTEGRITY_CONFLICT
```

State what changed, what did not change, the first residual, and whether a valid daily-steward signal occurred.

## Identifier and collision policy

The W-series is historical. Neither hourly nor direct Progress allocates a new W number.

Use:

```text
hourly run:  GUH-YYYYMMDDTHHMMSSZ-<slug>
direct run:  GUD-YYYYMMDDTHHMMSSZ-<slug>
daily steward: GUS-YYYYMMDD-<slug>
research file: <topic>-<subtopic>-YYYY-MM-DD.md
```

Before writing:

1. Fetch and inspect `origin/main`.
2. Check open run plans from roughly the last hour.
3. Check the intended paths locally and on the fetched branch.
4. Declare disjoint owned paths.
5. Stop or choose a non-overlapping swing if another run owns the lane or files.

Before committing:

1. Fetch and rebase on current `origin/main`.
2. Review the diff and validation output.
3. Stage only explicit paths. Never use `git add -A`.
4. Push the coherent commit and leave the tree clean.

## Steering-surface firewall

Hourly runs do not edit:

- `lab/process/research-portfolio.json`;
- the top operational block in `NEXT-STEPS.md`;
- `CANON.md`;
- historical W-series steering registers.

Put the proposed priority effect in the ignored run receipt. The daily steward integrates it.

## Lean guard

Lean is a reserve method, not the default objective. Use it only for a stable finite kernel that prevents a known error and can state every modeling premise explicitly.

On this Windows host, every GU Lean or Lake invocation must use `lab/automation/check-lean.ps1`, which acquires a host-local exclusive lock and runs `lake build`; Lake 5 no longer accepts the historical `lake build -j1` form. The file handle does not serialize another computer or a cloud runner and cannot stop a contributor from bypassing the wrapper. Other hosts must use their runner-native single-build lock and any supported low-parallelism control, and no two hosts may write the same checkout. Do not encode interacting physics, carrier faithfulness, or native realization as an unmarked axiom.

## Prediction discipline

- Freeze a native relation before opening target data.
- Separate native, imported, fitted, and free quantities.
- Compatibility is not prediction.
- A structural feature without a physical observable is not prediction.
- A standard EFT mimic with equal freedom defeats distinctiveness.
- F1 is a falsification tripwire, not a positive prediction.
- DE-AMP is a normalization audit, not decisive prediction extraction.

## Adaptive lane reranking

After execution and validation, but before the receipt, run the standard CapacityOS `rerank-next-work` flow and append its `Next-Work Handoff` to the run plan.

1. Classify the current work item, and any selected adaptive component, with the flow's disposition vocabulary.
2. Re-rank eligible work inside the lane just worked. When a work item has `internal_work_items`, rank those components first, then compare that workstream with the lane's other eligible work items.
3. Record at most three within-lane candidates, explain why the first now deserves attention, and name the evidence that preserved or changed the order.
4. Identify the strongest eligible work item in each of Lanes 1, 2, and 3. Re-rank those three lane leaders and record at most three cross-lane candidates.
5. State explicitly whether the recommended next run stays in the current lane or switches lanes. A scheduling switch does not change Lane 1's protected purpose.
6. Exclude Lane A from the scientific ranking. Route `steward reconciliation needed` to Lane A without treating it as Progress output.
7. Leave durable portfolio edits to the daily steward.

A maintainer-directed run or separately scoped automation may add effort to one work item, but it must not silently create another lane, bypass a gate, or overwrite the hourly handoff.

## Closeout

The receipt must name:

- result vocabulary outcome;
- files changed;
- validation run;
- scientific grade and unchanged statuses;
- dependency changes;
- `priority_signal: none` or one valid signal;
- `joe_signal: none` or the exact trigger;
- `paper_seed_proposal: none` or the complete Drafting Factory seed payload discovered during the swing;
- current lane, work-item disposition, and adaptive component disposition when applicable;
- ranked next work inside the lane just worked;
- ranked Lane 1, Lane 2, and Lane 3 leaders plus the recommended next lane from the `Next-Work Handoff`;
- commit and push status.

A blocked run is useful only when it identifies the exact missing object and a lawful next test. Repeatedly reporting the same wall is not progress.
