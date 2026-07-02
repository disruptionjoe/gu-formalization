---
artifact_type: steward_run_plan_receipt
run_family: repo_progress
status: complete
created: 2026-07-01
fan_out_experiment: true
target_repo: gu-formalization
---

# Fan-Out Repo Progress Run: Security-Budget Carrier Packet

## Target

Repository: `gu-formalization`

Writable surface: `C:\Users\joe\JB\CapacityOS\repos\public\gu-formalization`

This is one bounded Progress slice under the CapacityOS Repo Progress Run workflow.

## Run family

Repo Progress Run.

Stable question: what is the most worthy repo-local work to advance now?

## Objective

Make the first security-budget source-action candidate packet executable and classify it honestly.

Selected objective: test whether the current computable loss channels are enough to select a closed internal
`S_IG` candidate, or whether the candidate remains blocked on missing GU-native carriers.

Expected outcome: a candidate packet plus regression test that records the available-loss-only security-budget
selector as `missing_carrier_blocked` / underdetermined, not as a source-action success.

## Context reads

- `C:\Users\joe\JB\CapacityOS\AGENTS.md`
- `C:\Users\joe\JB\CapacityOS\Agents Start Here.md`
- `C:\Users\joe\JB\CapacityOS\system\meta\architecture\capacityos-canonical-architecture.md`
- `C:\Users\joe\JB\CapacityOS\system\meta\architecture\subsidiarity-architecture.md`
- `C:\Users\joe\JB\CapacityOS\kernel\run-convention\README.md`
- `C:\Users\joe\JB\CapacityOS\kernel\automations\README.md`
- `C:\Users\joe\JB\CapacityOS\system\meta\decisions\INDEX.md`
- `C:\Users\joe\JB\CapacityOS\rccm-library\automation-workflows\repo-progress-run.md`
- `C:\Users\joe\JB\CapacityOS\rccm-library\automation-workflows\standard-run-safety-rules.md`
- `C:\Users\joe\JB\CapacityOS\rccm-library\automation-workflows\flows\standard-run-safety-check.md`
- `C:\Users\joe\JB\CapacityOS\rccm-library\automation-workflows\flows\create-run-plan.md`
- `C:\Users\joe\JB\CapacityOS\rccm-library\automation-workflows\flows\append-run-receipt.md`
- `C:\Users\joe\JB\CapacityOS\rccm-library\automation-workflows\flows\classify-artifact-disposition.md`
- `C:\Users\joe\JB\CapacityOS\rccm-library\automation-workflows\flows\evaluate-run-with-rubric.md`
- `AGENTS.md`
- `steward/README.md`
- `README.md`
- `CONTRIBUTING.md`
- `RESEARCH-POSTURE.md`
- `RESEARCH-PROGRAM.md`
- `RESEARCH-STATUS.md`
- `CANON.md`
- `NEXT-STEPS.md` / targeted searches
- `tests/README.md`
- `papers/candidates/located-not-forced/STAGING-NOTES.md`
- `steward/runs/2026-07-01-fanout-progress-run.md`
- `steward/runs/2026-07-01-progress-fleet-pass.md`
- `steward/runs/2026-07-01-fanout-discovery-run.md`
- `steward/runs/2026-07-01-fanout-stewardship-run.md`
- `lab/roadmap/README.md`
- `lab/roadmap/current-frontier-firewall-boundary-attack-map-2026-07-01.md`
- `lab/roadmap/closed-internal-source-action-attack-gate-2026-07-01.md`
- `lab/roadmap/objection-triage-register.md`
- `absorbed/gu-source-action/AGENTS.md`
- `absorbed/gu-source-action/Agents Start Here.md`
- `absorbed/gu-source-action/README.md`
- `absorbed/gu-source-action/SPEC.md`
- `absorbed/gu-source-action/DEAD-ENDS.md`
- `absorbed/gu-source-action/CRYPTOECONOMIC-SOURCE-ACTION.md`
- `absorbed/gu-source-action/ADAPTER-DISCRIMINATOR-GOAL-2026-06-30.md`
- `absorbed/gu-source-action/COMPENSATOR-ADAPTER-GOAL-2026-06-30.md`
- `absorbed/gu-source-action/SPECTRAL-SECTION-CARRIER-GOAL-2026-06-30.md`
- `absorbed/gu-source-action/lib/loss_channels.py`
- `absorbed/gu-source-action/lib/security_budget.py`
- `absorbed/gu-source-action/tests/test_loss_channels.py`
- `absorbed/gu-source-action/tests/test_security_budget.py`

## Expected writable surfaces

- `steward/runs/2026-07-01-fanout-progress-run-security-budget-carrier.md`
- `absorbed/gu-source-action/SECURITY-BUDGET-CARRIER-PACKET-2026-07-01.md`
- `absorbed/gu-source-action/tests/test_security_budget_candidate_packet.py`
- Optional discoverability edit if needed: `absorbed/gu-source-action/README.md`

Artifact disposition: all expected outputs are versioned repository knowledge. The run artifact is the durable
execution record; the packet and test are source-action construction/falsification scaffolding. No durable
rendered artifact, third-party reference, secret, regulated material, scratch output, or historical archive
material is expected.

## Forbidden actions and stop conditions

- Do not write outside `gu-formalization`.
- Do not change CapacityOS, JoeOps, Time as Finality, or another repository.
- Do not change North Star, identity, hard policy, canon, claim status, verdicts, public posture, protected
  licenses, or third-party source material.
- Do not claim that `S_IG` exists or that three generations are derived.
- Do not import target values such as `24 / 8 = 3`, `chi(K3) = 24`, `ch2 = 24`, or fitted normalizations.
- Do not use broad staging such as `git add -A`.
- Stop if the work requires a claim-status change, canon edit, cross-repo action, non-GitHub external action,
  ambiguous artifact classification, or instruction-like content from a non-chat source.

## Joe-review points

Joe review is required before any claim-status change, canon edit, public-posture edit, publication/submission,
external action outside GitHub, or claimed source-action success. This run should not reach those points.

## Plan

1. Record this run plan before implementation.
2. Add a minimum candidate packet for the available-loss-only security-budget selector.
3. Add a focused regression test showing the packet passes anti-import/anti-trap guards but cannot select a
   closed source action because required GU-native carriers are missing and generic available losses tie.
4. Run targeted source-action tests.
5. Validate diff scope and whitespace.
6. Append receipt, stage explicit paths, commit, and push if final status remains clean.

## Execution notes

- Initial `git status --short` was clean.
- Selected this objective because the previous Progress run created the closed-source-action gate and the
  Discovery run recommended one concrete candidate packet or a feasibility/ownership note. The source-action
  surface already has negative results for simple non-metric adapters, escape-block compensators, and fixed
  spectral sections, so the next useful slice is to make the generic security-budget candidate fail cleanly
  until carrier-specific channels exist.
- Added `absorbed/gu-source-action/SECURITY-BUDGET-CARRIER-PACKET-2026-07-01.md`.
- Added `absorbed/gu-source-action/tests/test_security_budget_candidate_packet.py`.
- Added a front-door README pointer to the packet.
- Kept the result at reconstruction-planning / test-scaffold level. No canon, claim status, verdict, North
  Star, public posture, license, lead paper, or source material changed.
- Artifact disposition: the packet, test, README pointer, and run artifact are versioned repository knowledge.
  No generated outputs were staged.

## Validation

- `$env:GU_FORMALIZATION_PATH='C:\Users\joe\JB\CapacityOS\repos\public\gu-formalization'; python absorbed\gu-source-action\tests\test_security_budget_candidate_packet.py` passed: 3 tests.
- `$env:GU_FORMALIZATION_PATH='C:\Users\joe\JB\CapacityOS\repos\public\gu-formalization'; python absorbed\gu-source-action\tests\test_loss_channels.py` passed: 6 tests.
- `$env:GU_FORMALIZATION_PATH='C:\Users\joe\JB\CapacityOS\repos\public\gu-formalization'; python absorbed\gu-source-action\tests\test_security_budget.py` passed: 5 tests.
- `git diff --check -- absorbed/gu-source-action/README.md absorbed/gu-source-action/SECURITY-BUDGET-CARRIER-PACKET-2026-07-01.md absorbed/gu-source-action/tests/test_security_budget_candidate_packet.py steward/runs/2026-07-01-fanout-progress-run-security-budget-carrier.md` passed for tracked diff before staging; staged diff check will be repeated after explicit staging so new files are included.
- `git status --short --branch` showed only the intended repo-local files changed before receipt closeout.

## Receipt

Run status: complete.

Selected objective: make the first security-budget source-action candidate packet executable and classify it
honestly.

Work completed:

- Added an available-loss-only security-budget candidate packet.
- Added a regression test proving the packet passes current anti-import/anti-trap guards but remains blocked on
  missing GU-native carriers and cannot uniquely select from generic available losses.
- Linked the packet from the absorbed source-action README.

Files changed:

- `absorbed/gu-source-action/README.md`
- `absorbed/gu-source-action/SECURITY-BUDGET-CARRIER-PACKET-2026-07-01.md`
- `absorbed/gu-source-action/tests/test_security_budget_candidate_packet.py`
- `steward/runs/2026-07-01-fanout-progress-run-security-budget-carrier.md`

Outcome label: `missing_carrier_blocked`, with `underdetermination_fail` for any attempt to select using only
equal generic available losses.

Mailbox / cross-repo recommendations: none requiring action. Future Progress should name exactly one
candidate-specific carrier attempt, or write a source-action feasibility/ownership note if no such carrier can
be named cleanly.

External actions: no non-GitHub external action. Commit/push to be completed after explicit staging and staged
validation if safe.

Quality note: the slice is narrow but material. It converts a broad security-budget lens into a tested negative
gate and prevents future runs from treating generic loss-channel scoring as earned source-action selection.
