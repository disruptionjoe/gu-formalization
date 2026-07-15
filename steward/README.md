# GU Formalization Steward Context

Status: active repo-local steward context. Adopted 2026-07-01 from the CapacityOS Repo Steward reference architecture; during WI-045 Phase 5, federal steward ownership moved to the System-owned overlay at `../../../system/stewards/gu-formalization.md` from this repo root. Original steward rollout: RUN-20260630-019.

Load this file when a Kernel directive, RCCM workflow, System repo steward overlay, or direct repo-mounted run targets this repository. Do not load `steward/memory-log.md` by default unless doing stewardship or memory work, or this summary appears incomplete.

## North Star

Find what is true about the mathematics and physics in this program's reach, using Geometric Unity as the generative engine, never as a thesis to defend, and report it at honest grade alongside a reliable truth-seeking method.

Change rule: do not change this North Star without very explicit conversation with Joe.

## Long-Term Objectives

- Maintain the research framing in `RESEARCH-PROGRAM.md`.
- Keep current state truthful in `RESEARCH-STATUS.md`.
- Advance contributor roadmap items in `NEXT-STEPS.md`.
- Continue the lead candidate result in `papers/candidates/located-not-forced/`.

Objectives may change when Joe directs that they change.

## Measures And Countermeasures

Measures:

- Claims retain honest grades: `[verified]`, `[reconstruction]`, or `[speculation]`.
- Assumptions, falsification/rollback conditions, dependencies, correction logs, and no-go audits stay explicit.
- Lean, computational tests, and claim mappings remain consistent with the research posture.

Countermeasures / risks:

- Never inflate verdicts.
- Never call compatibility a derivation.
- Never rescue failed arguments.
- Never frame the work as adjudicating GU/Weinstein instead of finding truth.

## What This Repo Owns

This repo owns its research truth: the research program and posture, canon claims, structural-law results, derivation progress, falsifiable-hypothesis tracker, Lean formalization scaffold, computational tests, and explorations lab.

## What This Repo Must Not Absorb

- CapacityOS architecture, Kernel machinery, RCCM methodology, or JoeOps backlog state.
- Third-party source material as editable repo truth.
- Research verdicts or claims from neighboring repos unless explicitly imported and marked.

## Operating Guardrails

- Contributions follow `CONTRIBUTING.md`.
- Claim-status changes run `lab/process/runbooks/claim-status-consistency-quality-workflow.md`.
- Honor the grading discipline in `RESEARCH-POSTURE.md`.
- Public/external consequence, verdict / scientific-status changes, and relicensing pause for Joe.
- Canon promotion is agent-owned: execute it once the `RESEARCH-STATUS.md` Promotion Rule is met, then drop an awareness note in `../../../system/mailboxes/joeops/` from this repo root per `lab/process/templates/canon-promotion-joeops-notice.md`. A claim's *verdict* change is separate and still pauses.
- Cross-repo actions are proposed via the target surface's mailbox (`../../../system/mailboxes/<surface>/` from this repo root) for that steward to decide - not executed directly, and no longer paused for Joe.
- `LICENSE-CODE.md` and `LICENSE-DOCS.md` are protected; never alter casually.
- The GU source PDF is third-party reference material; never modify or relicense.

## Routing

- Research truth stays in this repo.
- CapacityOS architecture questions route to `CapacityOS`.
- JoeOps coordination questions route to `CapacityOS\repos\private\joeops`.
- Durable artifacts belong in `library\repos\public\gu-formalization\`.
- Third-party references belong near the repo under `library\repos\public\gu-formalization\references\external\`.
- Scratch belongs in `_local/`.

## Candidate Decisions

- `papers/candidates/located-not-forced/` is the current lead-result work surface.

## Durable Decisions

- This repo is public; publishing and public/private framing are governed.
- Research truth is repo-owned and changes through the repo's grading discipline.
- The real pause boundary is verdict, claim-status, or external consequence, not reversible internal drafting.

## Principles

- Truth-seeking outranks thesis defense.
- Honest grading is part of the research result.
- Negative results and demotions are progress when they reduce self-deception.

## Memory Log

Chronological memory lives at `steward/memory-log.md`. Append useful memory after sessions where this README is loaded.

Lightweight upward-learning pointer: from this repo root, method/workflow-module learnings go to `../../../system/mailboxes/rccm/`; kernel-primitive learnings go to `../../../system/mailboxes/kernel/`.

## Automation Hooks

Supports CapacityOS-orchestrated and direct repo-mounted runs. Automations are thin triggers; System run-packet/mode resolution plus workflow and this steward context supply the repo-local operation.

### Daily research-portfolio reconciliation

The daily Stewardship run also repairs GU-local coordination drift by reconciling
`lab/process/research-portfolio.json` against completed run receipts, new commits, accepted frozen packets,
dependency changes, falsifiers, survivors, integrity corrections, and official external releases. This is
repo-owned priority maintenance, not CapacityOS or JoeOps ownership of research truth.

Apply `lab/process/runbooks/daily-research-portfolio-stewardship.md`:

- preserve one protected North-Star primary lane and at most one reserve/maintenance lane;
- reprioritize only on a real scientific or dependency signal, never on difficulty, activity, or
  finishability alone;
- keep the primary lane from being displaced by easier Lean or paper-hardening work;
- maintain the portfolio and the top operational block of `NEXT-STEPS.md` as steward-only steering
  surfaces;
- receive hourly priority signals through run receipts and synthesize them once daily;
- route only event-driven, deduplicated high-signal items to JoeOps;
- preserve GU's sovereign native-versus-forced call and require frozen packets at every cross-repo seam.

The current hourly default is `lab/process/runbooks/meaningful-hourly-progress-swing.md`. Lean verification
is an eligible reserve method, not the default research objective.

When older operational-routing prose in `RESEARCH-POSTURE.md`, historical W-series registers, or superseded
`NEXT-STEPS.md` blocks conflicts with the current portfolio, the portfolio controls run selection. This does
not supersede the North Star, alter a scientific claim, or change a verdict.

### Identifier and shared-surface rule

The historical W-series is no longer allocated by hourly or direct Progress runs. Use the namespaced run IDs
in the portfolio and semantic dated research filenames. This removes collisions between direct-chat and
hourly work without requiring a remote lock service.

Routine write ownership:

- daily steward: `lab/process/research-portfolio.json` and the top operational block of `NEXT-STEPS.md`;
- hourly run: its declared research/test/proof paths and ignored `steward/runs/` receipt;
- claim workflow: `CANON.md` and other governed status surfaces.

Every GU Lean/Lake invocation uses `lab/automation/check-lean.ps1`, serialized at `-j1`. Do not overlap a
GU Lean build with another local Lean job.

## Local Source References

- `RESEARCH-PROGRAM.md`
- `RESEARCH-POSTURE.md`
- `RESEARCH-STATUS.md`
- `NEXT-STEPS.md`
- `CONTRIBUTING.md`
- `CANON.md`
- `DERIVATION-PROGRESS.md`
- `lab/process/research-portfolio.json`
- `lab/process/paper-hardening-inventory.md`
- `lab/process/runbooks/daily-research-portfolio-stewardship.md`
- `lab/process/runbooks/meaningful-hourly-progress-swing.md`
- `lab/process/runbooks/claim-status-consistency-quality-workflow.md`
