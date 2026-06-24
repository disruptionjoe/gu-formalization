---
title: "Five-Lane Frontier Run"
status: canon
doc_type: runbook
scope: repo-local
updated_at: "2026-06-24"
---

# Five-Lane Frontier Run

This is the standard repo-local run type for advancing the GU formalization frontier with
sub-agents. Use it when the maintainer asks for a "run", "another five", "five tasks", or
similar language in the context of moving the repository forward.

The purpose is not to clear small chores. The purpose is to draft and execute five
ambitious, non-overlapping goals that each move one real proof, no-go, bridge, or
physics-recovery question closer to a decision.

## Core Rule

Each lane must be a meaningful frontier goal, not the smallest available slice.

A good lane should answer at least one of these:

- Can an important claim be promoted, made conditional, blocked, or refuted?
- What exact proof object is missing?
- What branch or assumption fails?
- What computation would unlock the next claim?
- What repo claim should be demoted, guarded, or made more precise?

## Coordinator Workflow

1. Check the branch and worktree first.
2. Draft five ambitious goals from the current frontier.
3. Give each goal a disjoint owned output path.
4. Give each goal an optional owned audit/test path only if a real check is possible.
5. Assign required source files to read first.
6. Spawn five workers in parallel only after the file scopes are non-overlapping.
7. Keep integration work in the main thread.
8. Review returned artifacts for substance, overclaiming, and overlap.
9. Run every added audit or test.
10. Run `git diff --check`.
11. Remove generated cache files such as `tests/__pycache__`.
12. Stage only the intended run files.
13. Commit and push after review passes.
14. Summarize the findings in plain English, including what each result means.

If two strong goals would touch the same files or depend on each other, do not run them in
parallel. Combine them into one lane, run them sequentially, or save one for the next run.

## Goal Quality Bar

Each goal should be written as a decision-grade assignment.

Good goal shape:

```text
Starting from [specific repo objects], derive / rebuild / reduce / test / bridge [specific
claim] far enough to decide [closed / conditional / blocked / fail / no-go]. Identify the
first exact missing proof object or obstruction.
```

Avoid goals that only say:

```text
Summarize this area.
Find next steps.
Review recent files.
Add a small note.
```

Those can be useful support tasks, but they are not frontier-run lanes.

## Worker Contract

Every worker prompt should include this contract:

```text
You are one of five parallel workers in the GU formalization repo.

Coordination rules:
- You are not alone in the codebase.
- Other workers may edit different files in parallel.
- Do not revert or overwrite changes outside your assigned files.
- Do not commit or push.
- Own only the listed output path and optional audit/test path.
- Produce a decision-grade artifact, not a summary-only note.
- Use plain English, but be technically precise.
- Final response must list changed files and verification performed.
```

## Lane Template

Use this structure for each lane:

```text
Goal: [ambitious frontier goal name]

Owned paths:
- explorations/[specific-run-artifact].md
- optional: tests/[specific_audit].py

Read first:
- [source file 1]
- [source file 2]
- [source file 3]

Assignment:
[Concrete proof/reduction/bridge/no-go task.]

Deliverable structure:
1. Verdict: closed / conditional / blocked / fail / no-go / underdefined.
2. What was derived directly from repo sources.
3. The strongest positive result.
4. The first exact obstruction or missing proof object.
5. What this means for the relevant GU claim.
6. Next meaningful proof or computation step.

If you add the optional audit/test, make it a real invariant, contract, or consistency check,
not a placeholder.
```

## Verdict Vocabulary

Use verdicts consistently:

- `closed`: the assigned gate is proved within the stated sources and assumptions.
- `conditional`: the gate closes if a named upstream object or assumption is supplied.
- `blocked`: the repo lacks enough specified structure to evaluate the claim.
- `fail`: a specified branch or model does not satisfy the gate.
- `no-go`: a class of attempted routes is ruled out by a structural obstruction.
- `underdefined`: the mathematical object needed for the claim is not yet specified.
- `host`: the repo has room for the structure, but does not derive or select it.
- `import`: the structure is inserted from outside rather than derived.

Do not let "compatible with" become "derived from". Do not let "hosted by" become
"selected by".

## Integration Acceptance Criteria

A run is acceptable only if:

- All five lanes produce owned artifacts or explicitly report why they could not.
- The artifacts make real decisions or exact deferrals.
- No lane overclaims beyond the sources it read.
- Parallel workers did not edit overlapping paths.
- Added audits/tests pass.
- `git diff --check` passes.
- Generated caches are absent from the final worktree.
- The final commit contains only intended run artifacts.
- The final summary explains the findings in plain English.

## Standard Closeout

After review passes:

```text
git status --short
git add -- [intended run files only]
git diff --cached --stat
git diff --cached --name-status
git commit -m "Run GU frontier gates"
git push
git status --short --branch
```

The final response should include:

- commit hash and message;
- tests/audits run;
- one plain-English finding per lane;
- whether the run produced a new next-frontier target;
- any lane that should be followed sequentially rather than in the next parallel batch.

## Reference Instance

The 2026-06-24 frontier run is the reference instance for this standard:

- VZ proof-grade closure attempt;
- exact Schwarzschild/Kerr Euler-Lagrange gate;
- FLRW theta-xi branch reduction;
- noncompact `Y^14` to K3 index bridge;
- SM gauge/Higgs finite-control extraction ledger.

That run worked because each lane had a distinct owned file, a clear decision target, and
main-thread integration review before commit and push.
