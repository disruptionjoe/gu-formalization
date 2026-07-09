# Process Runbooks

This folder holds repo-local workflow runbooks. They describe when a run type is
appropriate, what it is allowed to change, and what closeout evidence it must leave.

## Live Runbooks

- [`claim-status-consistency-quality-workflow.md`](claim-status-consistency-quality-workflow.md) -
  required sweep before a promotion, downgrade, correction, or other status-changing
  claim edit.
- [`five-lane-frontier-run.md`](five-lane-frontier-run.md) - maintainer-directed divergent
  frontier run for ambitious, non-overlapping proof, bridge, no-go, or computation lanes.
- [`lean-verification-run.md`](lean-verification-run.md) - convergent Lean verification lane
  for automated or hourly progress when the selected item is already finite and checkable.
- [`three-cycle-fifteen-hole-run.md`](three-cycle-fifteen-hole-run.md) - sequential wrapper for
  three five-lane frontier cycles with integration, validation, commit, and push after each
  cycle.

## Boundary

- This map is navigation and process knowledge only. It does not change claim status, canon
  verdicts, public posture, proof status, or research verdicts.
- The Lean verification runbook explains when Lean work is appropriate, but this README does
  not run Lean, typecheck proofs, or validate any research claim.
- The parent process overview remains [`../README.md`](../README.md); status-changing claim
  edits still use the claim-status consistency workflow above.
