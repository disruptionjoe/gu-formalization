---
title: "Mac Lean serialization for proof kernels"
status: complete
doc_type: run-plan-and-receipt
run_id: RUN-20260724-231035-gu-formalization-progress
owner_service_id: RUN-20260724-231035-gu-formalization-owner-service
parent_run_id: RUN-20260724-231035-repository-work-cycle-nbl-hourly
owner_id: gu-formalization
workflow: repo-progress-run
workflow_revision: sha256:09ceebd5cdcb21090c418dd504a529b7bd10a906f5709a709a70f14d9adc918c
mode: execute
lane_id: "3"
starting_revision: e6b441cebaef600b439abb093787236a957fe553
resume_capsule: null
method_refs: []
completed_at: 2026-07-24T23:19:20Z
---

# Extremal-weight nilpotent proof kernel

## Target

Advance Lane 3 `PROOF-STABLE-KERNELS` by adding the next explicitly queued
kernel: a machine-checked finite highest-weight control in which a nonzero
nilpotent raising operator stabilizes the extremal vector.

## Run family

Repo Progress Run, Lane 3, scheduled/non-interactive.

## Formal packet

```yaml
repo: gu-formalization
workflow: repos/private/system-runtime/runtime/workflows/repo-progress-run.md
workflow_revision: sha256:09ceebd5cdcb21090c418dd504a529b7bd10a906f5709a709a70f14d9adc918c
mode: execute
run_id: RUN-20260724-231035-gu-formalization-progress
parent_run_id: RUN-20260724-231035-repository-work-cycle-nbl-hourly
lane_id: "3"
write_boundary:
  - lab/automation/check-lean.sh
  - lab/automation/README.md
  - Lean/GUFormalization/ExtremalWeightNilpotent.lean
  - Lean/GUFormalization.lean
  - Lean/README.md
  - lab/process/lean-verification-lane-LEDGER.md
  - runs/RUN-20260724-231035-gu-formalization-progress.md
method_refs: []
resume_capsule: null
```

## Selection and collision check

- Lane 1 remains the protected North Star, but its strongest operator and B5
  candidates require source-owned operator/domain or middle-differential
  packets. Repeating scalar-mass, ambient-rank, Q1/Q2, or fixed-sampler work is
  explicitly forbidden by current owner truth.
- Lane 2 remains monitor/source gated on current inputs.
- Lane 3 `PROOF-STABLE-KERNELS` is `READY`. Its first three integrity steps
  are already complete, and the owner verification ledger names the W243 /
  GU-002 extremal-weight kernel as the next step.
- The branch began clean and even with its upstream at the starting revision.
  No recent open Run overlaps this boundary, and the resolved writer-claim path
  was absent before this Run acquired it.

## Scope and honesty boundary

The Lean result will formalize one explicit two-dimensional graded
representation: the grading operator, top/bottom weight vectors, raising
operator, grading commutator, nonzero witness, square-zero nilpotency, and
stabilization of the top vector. It will not claim the general
rank-independent W243 theorem, faithfulness to `Sp(32,32;H)`, physical
realization, Proposition 1, W235, interacting dynamics, or compactness of a
physical stabilizer.

## Plan

1. Add a Mac/POSIX Lean wrapper with the required host-local exclusive build
   lock, then establish a fresh default-target baseline.
2. Add the explicitly scoped finite proof kernel and import it from the
   default target.
3. Rebuild through the wrapper and run lightweight certificate, placeholder,
   and diff checks.
4. Update only the Lean navigation/verification ledger, rerank numbered Lanes,
   append the receipt, revalidate authority and collision state, commit, and
   push the current branch.

## Stop conditions

- Stop on another writer claim, overlapping dirt, authority/control drift, a
  live Lean build lock, or a failed pre-change default-target baseline.
- Leave the theorem at finite-control scope if a stronger statement would
  require hiding a representation-faithfulness or physical premise.
- No claim-status, canon, public-posture, Lane-control, portfolio, Runtime,
  mailbox, cross-repository, or non-GitHub external action.

## Lifecycle trace

- `phase_open`: required authority, NBL boundary, owner truth, current Lanes,
  recent Runs, System steward overlay, and the complete numbered-Lane
  alternative set were read before this plan was created.

## Execution notes

- Added `lab/automation/check-lean.sh`, the missing macOS/POSIX counterpart to
  the Windows Lean wrapper. It uses a host-local `shlock` claim, refuses a live
  competing build with exit `75`, supports the existing update/cache
  preparation sequence, and runs the Lake 5 default target without the removed
  `-j1` syntax.
- Established a fresh pre-change default-target baseline through that wrapper:
  `lake build` completed successfully (`8645` jobs). Existing Coflip linter
  warnings were unchanged.
- Implemented and compiled the planned explicit two-weight theorem-H control
  as a concrete attempt. The post-change default target completed successfully
  (`8646` jobs), proving the nonzero, square-zero, degree-`+2` raising witness
  that stabilizes the top-weight vector at its declared finite scope.
- The scheduled-run protected-surface audit then correctly rejected the
  intended `Lean/` footprint. That gate is a review boundary, not a theorem
  failure. All theorem source, default-target import, Lean navigation, and
  verification-ledger edits were fully reverted before close. No protected
  surface remains in the diff.
- Documented the retained wrapper in `lab/automation/README.md`. This closes
  the concrete Mac serialization gap and makes future authorized proof-kernel
  work executable without bypassing local resource safety.

## Next-Work Handoff

- current work: Mac/POSIX Lean serialization prerequisite for Lane 3
  `PROOF-STABLE-KERNELS`
- current disposition: `ENDPOINT_POSITIVE`
- durable priority owner: GU Lane A stewardship
- recommendation status: advisory

| rank | lane / work | current disposition | exact gate or next action |
|---:|---|---|---|
| 1 | Lane 1 `OPERATOR-END-PENCIL` / B5 | protected North Star, not executable | frozen source-owned operator/domain or middle-differential packet |
| 2 | Lane 3 `PROOF-STABLE-KERNELS` theorem H | mathematically ready; scheduled protected-surface gate | run in an explicitly reviewed/manual protected-surface context, reusing the compiled finite witness design |
| 3 | Lane 2 prediction work | monitor/source gated | official data release or frozen native bridge/structure |

- strongest runnable next under this same unattended boundary: none beyond the
  completed wrapper capability; do not manufacture a theorem outside `Lean/`
  to evade the protection gate.
- switch signal: explicit protected-surface review authority for theorem H, a
  new Lane 1 source packet, official prediction data, or another
  owner-authoritative numbered-Lane signal.

## Validation

- Pre-change `lab/automation/check-lean.sh`: default target passed, `8645`
  jobs.
- Concrete theorem-H attempt: default target passed, `8646` jobs, before the
  protected-surface review gate caused full reversion.
- Wrapper live-lock negative control: exit `75` with the expected competing
  lock message; temporary control lock removed.
- `sh -n lab/automation/check-lean.sh`: passed.
- `python3 process_gates/protected_surface_diff_audit.py`: `3/3` passed after
  protected edits were reverted.
- `python3 process_gates/lean_certificate_surface_audit.py`: `6/6` passed.
- `git diff --check`: passed.
- Effect-boundary revalidation: owner authority SHA-256
  `1007e5871c0311e3ea9deead63fdeee1513d2058acdea44ad7c11dd3482057d8`;
  `LANES.yaml` SHA-256
  `5c535ae8674718dc2f2bfedf21bfe4c04ac9cceafe62bbfe1428e3814da9f083`;
  `LANE-STATE.yaml` SHA-256
  `66b34f71b79da5082761bf3c4dffa87c7ff69d84dbf342bb65575b3b4e343e2f`;
  writer claim still owned by this Run; host Lean lock released.

## Receipt

- Phase result: `progressed`.
- Lane: `3`, supporting result hardening and future Lane 1 truth testing.
- Planned boundary included the theorem-H protected surfaces. Actual durable
  footprint is only:
  `lab/automation/check-lean.sh`, `lab/automation/README.md`, and this Run
  record. The protected attempt was fully reverted and produced no owner-truth
  or claim effect.
- Owner effect: a reusable, collision-safe Mac/POSIX Lean execution capability
  plus an exact evidenced handoff for the next proof kernel.
- Required flows attested:
  `standard-run-safety-check`, `select-lane`, `create-run-plan`,
  `revalidate-lane-selection`, and `append-run-receipt`.
- Conditional flow invoked: `rerank-next-work`. No Lane-state refresh,
  artifact-disposition flow, rubric evaluation, canon/claim workflow, or
  cross-owner flow was invoked.
- Required graph attested: `true`; exceptions: none.
- Method refs/effect: `[]` / `null`.
- No claim, canon, verdict, public posture, Lane/control, portfolio, Runtime,
  mailbox, cross-repository, or non-GitHub external action changed.
- Exact wake: explicit protected-surface review authority for theorem H, or a
  new owner-authoritative numbered-Lane switch signal.
- `phase_close`: this receipt closes the only formal phase; no further owner
  content effect may be added under this packet.
