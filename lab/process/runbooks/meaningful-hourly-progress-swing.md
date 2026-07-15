---
title: "Meaningful Hourly Progress Swing"
status: active
doc_type: runbook
scope: repo-local
created: 2026-07-15
portfolio: lab/process/research-portfolio.json
---

# Meaningful Hourly Progress Swing

This is the default GU hourly Progress run. It executes one coherent research swing selected from the steward-maintained portfolio. It replaces Lean-only hourly selection and tiny bounded-slice behavior.

The target is one meaningful research delta per run, not one file, one lemma, or one commit.

Use one technical lane and one local heavy job at a time. Do not routine-fanout the hourly run. Divergent
multi-lane fanout remains maintainer-directed through `five-lane-frontier-run.md`.

## Selection

1. Load the standard CapacityOS Progress workflow, GU steward context, and local instructions.
2. Create the run plan before research work and inspect recent open run plans for collisions.
3. Read `lab/process/research-portfolio.json`.
4. Select the protected primary lane if it is `ACTIVE` or `READY` and its dependencies permit work.
5. Use the reserve lane only when the primary is genuinely blocked, waiting on external state, or has just reached a decision-grade endpoint. Record the exact reason.
6. Never select `GATED_P2C`, `WAITING_EXTERNAL`, `MONITOR`, `PARKED`, `RESOLVED_NO_GO`, `PAPER_READY`, or `NEEDS_JOE` work as an hourly technical target.

The hourly run does not reprioritize the portfolio. It reports evidence and a suggested priority signal in its receipt. The daily steward decides whether the signal changes the queue.

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

## Required result vocabulary

Every technical swing ends with one operational result:

```text
CLOSED
CONDITIONAL
BLOCKED
FAIL
NO_GO
UNDERDEFINED
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

On this Windows host, every GU Lean or Lake invocation must use `lab/automation/check-lean.ps1`, which acquires a host-local exclusive lock and runs `lake build -j1`. The file handle does not serialize another computer or a cloud runner and cannot stop a contributor from bypassing the wrapper. Other hosts must use their runner-native single-build lock and `-j1`, and no two hosts may write the same checkout. Do not encode interacting physics, carrier faithfulness, or native realization as an unmarked axiom.

## Prediction discipline

- Freeze a native relation before opening target data.
- Separate native, imported, fitted, and free quantities.
- Compatibility is not prediction.
- A structural feature without a physical observable is not prediction.
- A standard EFT mimic with equal freedom defeats distinctiveness.
- F1 is a falsification tripwire, not a positive prediction.
- DE-AMP is a normalization audit, not decisive prediction extraction.

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
- commit and push status.

A blocked run is useful only when it identifies the exact missing object and a lawful next test. Repeatedly reporting the same wall is not progress.
