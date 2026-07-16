---
title: "Five-Lane Frontier Run"
status: canon
doc_type: runbook
scope: repo-local
updated_at: "2026-07-07"
---

# Five-Lane Frontier Run

> **ROUTING (updated 2026-07-15, maintainer-directed).** This is the multi-lane divergent Progress run and
> remains session-directed. Automated hourly Progress uses `meaningful-hourly-progress-swing.md`, which takes
> one substantial, decision-grade swing from the steward-maintained portfolio. Lean verification is the
> Lane 3 method, not the default objective. See `daily-research-portfolio-stewardship.md` for selection.
>
> **REGISTRY CONSUMPTION (prototype, 2026-07-07).** A divergent-progress lane that faces a genuine wall
> should now draw its move from a source, in this order of provenness:
> 1. **flow-directed** — a proven flow (`CapacityOS/system/runtime/flows`), if one matches the wall;
> 2. **registry-borrowed** — a tested-but-unproven move from the ai-epistemology wall-breaking registry
>    (`ai-epistemology/field-guide/branch-5-evolvability/wall-breaking-move-registry.md`): classify the wall
>    against its taxonomy, select a move whose trigger matches, run it against its **pre-registered success
>    criterion**;
> 3. **workflow-deemed** — the workflow decides ad hoc (least proven; use when neither above matches).
> After running a registry-borrowed move, **log the outcome** (program, wall type, move, pre-registered
> criterion, GO/NO-GO) as a short markdown message in `CapacityOS/system/mailboxes/ai-epistemology/` so the
> registry maintainer can ingest it into the deployment log. This is what turns the registry's n=3 priors
> into measured reliability. Tier-C (unifier) moves MUST be followed by MDM-A1 (adversarial twin) before
> banking any positive. Divergent INPUTS (MDM-H1 curiosity import, MDM-H2 dismissal override) remain
> maintainer-supplied — an automated divergent run PROPOSES the wall classification + candidate moves; the
> maintainer picks.

This is the standard repo-local run type for advancing the GU formalization frontier with
sub-agents. Use it when the maintainer asks for a "run", "another five", "five tasks", or
similar language in the context of moving the repository forward.

## STOP RULE — no-progress halt (check BEFORE every run)

Before starting, check the last 3 syntheses (`ls explorations/*synthesis* | tail -3`) and
`git log --oneline -15`. **HALT and escalate to the maintainer instead of running** if
either holds: (1) the live frontier is gated on lawful-local custody of source bytes the
agent cannot obtain (re-deriving "the source is still absent" and renaming the missing
object is not progress); or (2) the last 3 runs all report `claim_status_change: false`,
`claim_promotions: 0`, `source_admissions_count: 0`. When halting, append a dated `## HALT`
note to `lab/process/loop-adversarial-log.md` with the reason and the human action needed, and
do NOT create new artifacts or commit. See `three-cycle-fifteen-hole-run.md` for the full rule.

For three sequential five-lane cycles, use `three-cycle-fifteen-hole-run.md` as the
wrapper and this file as the unit run.

The purpose is not to clear small chores. The purpose is to draft and execute five
ambitious, non-overlapping goals that each move one real proof, no-go, bridge, or
physics-recovery question closer to a decision.

The default optimization target is the truth-seeking posture in `RESEARCH-POSTURE.md`: determine what
structure GU and the observerse geometry genuinely locate, derive, block, or make cheaper than competing
accounts. Do not reduce frontier runs to the single question "does bare GU force three generations"; a lane may
advance the larger unifying-fit question, a concrete GU reconstruction object, or a GU-independent result that
survives at honest grade.

## Core Rule

Each lane must be a meaningful frontier goal, not the smallest available slice.

Each lane should optimize for information gain about the central GU reconstruction
hypothesis, not merely for conservative appearance or local mathematical neatness.

A good lane should answer at least one of these:

- If GU is substantially correct, what mathematical object, invariant, category,
  reduction, or analytic theorem must exist here?
- Can we construct it far enough to test it?
- Can an important claim be promoted, made conditional, blocked, or refuted?
- What exact proof object is missing?
- What branch or assumption fails?
- What computation would unlock the next claim?
- What repo claim should be demoted, guarded, or made more precise?

## Coordinator Workflow

1. Check the branch and worktree first.
2. Review `explorations/cycle-gates-and-audits/remaining-math-topography-ledger-v0-2026-06-26.md` when
   building the candidate hole bank, so each lane starts with a terrain hypothesis and
   forbidden shortcut. If a row routes to spectral, code, noncommutative, descent, or
   provenance terrain, also check the ledger's certificate carry-forward section for
   useful witness schemas from the quantum/chaos/crypto lens pass.
3. Draft five ambitious goals from the current frontier.
4. Give each goal a disjoint owned output path.
5. Give each goal an optional owned audit/test path only if a real check is possible.
6. Assign required source files to read first.
7. Spawn five workers in parallel only after the file scopes are non-overlapping.
8. Keep integration work in the main thread.
9. Review returned artifacts for substance, overclaiming, and overlap.
10. If any lane changes a claim status, run
   `lab/process/runbooks/claim-status-consistency-quality-workflow.md`.
11. Run every added audit or test.
12. Run `git diff --check`.
13. Remove generated cache files such as `tests/__pycache__`.
14. Stage only the intended run files.
15. Commit and push after review passes.
16. Summarize the findings in plain English, including what each result means.

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
5. The constructive next object that would remove or test the obstruction.
6. What this means for the relevant GU claim.
7. Next meaningful proof or computation step.
8. Terrain classification: suspected terrain, forbidden shortcut, first invariant to
   test, and kill condition.
9. If applicable, certificate/witness shape: public inputs, witness, verifier predicate,
   semantic lift, and anti-smuggling guard.

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
- Mission A lanes explain what would have to exist if GU is correct, then either construct
  toward it or identify the first exact obstruction.
- Mission B lanes are explicitly labeled as secondary independent mathematics.
- No lane overclaims beyond the sources it read.
- Any status-changing lane passes the claim-status consistency workflow before commit.
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
