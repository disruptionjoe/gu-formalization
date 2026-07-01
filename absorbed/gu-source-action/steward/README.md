# GU Source Action Steward Context

Status: active. Canonical steward load file adopted 2026-07-01 from the CapacityOS Repo Steward reference architecture. Original steward rollout: RUN-20260630-022.

Load this file when a Kernel directive, RCCM workflow, or direct repo-mounted run targets this repository. Do not load `steward/memory-log.md` or `DERIVATION-PROGRESS.md` by default unless doing stewardship, memory work, or the summary appears incomplete.

## North Star

Construct the one object `gu-formalization` proved is missing: the stabilized RS/IG source action `S_IG`; or honestly prove it cannot be built without import, so every turn either advances a survivable candidate or records a real negative.

Change rule: do not change this North Star without very explicit conversation with Joe.

## Long-Term Objectives

- Construct a valid `S_IG` per `SPEC.md`.
- Preserve the firewall reading if construction fails in the same boundary-shaped way.
- Keep `DERIVATION-PROGRESS.md` and `DEAD-ENDS.md` honest and useful.
- Use `lib/gu_bridge.py` to import verified parent machinery rather than re-derive it here.

## Measures And Countermeasures

Measures:

- Candidate lenses either survive adversarial attack or produce recorded negatives.
- Obstruction facts and bridge constraints remain explicit.
- The repo advances falsification criterion 1 of the Firewall-Boundary Hypothesis.

Countermeasures / risks:

- Never import the answer.
- Treat "it fits beautifully" as a warning, not evidence.
- Do not smuggle the matter-generation target, assumed K3, `24/8`, or fitted structure.
- Do not re-derive parent machinery that should be imported.

## What This Repo Owns

This repo owns its spec, derivation ledger, dead-ends record, candidate lenses, bridge tooling, tests, and falsification-workbench truth.

## What This Repo Must Not Absorb

- Verified parent machinery from `gu-formalization`.
- CapacityOS architecture or JoeOps coordination state.
- Public repo framing until Joe confirms the public/private flip.

## Operating Guardrails

- Compute on the explicit Cl(9,5) representation via `lib/gu_bridge.py`.
- Adversarially attack every candidate.
- Land only what survives.
- Record every honest negative.
- Honor the anti-trap, anti-fixed-solve, anti-vacuous, and anti-import guards.
- Public/private flips, claimed construction successes, hypothesis-status changes, or cross-repo parent changes pause for Joe.

## Routing

- Construction truth stays in this repo.
- Verified parent machinery stays in `gu-formalization`.
- CapacityOS architecture questions route to `C:\Users\joe\JB\CapacityOS`.
- JoeOps coordination questions route to `C:\Users\joe\JB\Github Repos\joeops`.
- Durable artifacts belong in `C:\Users\joe\JB\library\repos\private\gu-source-action\` while pre-public.
- Scratch belongs in `_local/`.

## Candidate Decisions

- Current candidate lenses and negatives live in `DERIVATION-PROGRESS.md` and `DEAD-ENDS.md`.

## Durable Decisions

- This repo is pre-public; public/private flips are governed.
- The verified parent machinery is imported, never re-derived here.
- Importing the target answer is a boundary violation, not a result.

## Principles

- Honest negatives are progress.
- Construction discipline beats aesthetic fit.
- Boundary-shaped failure is evidence when recorded cleanly.

## Memory Log

Chronological memory lives at `steward/memory-log.md`. Append useful memory after sessions where this README is loaded.

Lightweight upward-learning pointer: method/workflow-module learnings go to `CapacityOS/mailboxes/rccm/`; kernel-primitive learnings go to `CapacityOS/mailboxes/kernel/`.

## Automation Hooks

Supports CapacityOS-orchestrated and direct repo-mounted runs. Automations are thin triggers; RCCM workflow plus this steward context supply the repo-local operation.

## Local Source References

- `SPEC.md`
- `Agents Start Here.md`
- `DERIVATION-PROGRESS.md`
- `DEAD-ENDS.md`
- `lib/gu_bridge.py`
- `tests/`
