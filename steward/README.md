# GU Formalization Steward Context

Status: active. Canonical steward load file adopted 2026-07-01 from the CapacityOS Repo Steward reference architecture. Original steward rollout: RUN-20260630-019.

Load this file when a Kernel directive, RCCM workflow, or direct repo-mounted run targets this repository. Do not load `steward/memory-log.md` by default unless doing stewardship or memory work, or this summary appears incomplete.

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
- Public/external consequence, claim-status changes, verdict changes, relicensing, or cross-repo action pause for Joe.
- `LICENSE-CODE.md` and `LICENSE-DOCS.md` are protected; never alter casually.
- The GU source PDF is third-party reference material; never modify or relicense.

## Routing

- Research truth stays in this repo.
- CapacityOS architecture questions route to `C:\Users\joe\JB\CapacityOS`.
- JoeOps coordination questions route to `C:\Users\joe\JB\Github Repos\joeops`.
- Durable artifacts belong in `C:\Users\joe\JB\library\repos\public\gu-formalization\`.
- Third-party references belong near the repo under `C:\Users\joe\JB\library\repos\public\gu-formalization\references\external\`.
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

Lightweight upward-learning pointer: method/workflow-module learnings go to `CapacityOS/mailboxes/rccm/`; kernel-primitive learnings go to `CapacityOS/mailboxes/kernel/`.

## Automation Hooks

Supports CapacityOS-orchestrated and direct repo-mounted runs. Automations are thin triggers; RCCM workflow plus this steward context supply the repo-local operation.

## Local Source References

- `RESEARCH-PROGRAM.md`
- `RESEARCH-POSTURE.md`
- `RESEARCH-STATUS.md`
- `NEXT-STEPS.md`
- `CONTRIBUTING.md`
- `CANON.md`
- `DERIVATION-PROGRESS.md`
- `lab/process/runbooks/claim-status-consistency-quality-workflow.md`
