# Process Runbooks

This folder holds repo-local workflow runbooks. They describe when a run type is
appropriate, what it is allowed to change, and what closeout evidence it must leave.

## Live Runbooks

- [`claim-status-consistency-quality-workflow.md`](claim-status-consistency-quality-workflow.md) -
  required sweep before a promotion, downgrade, correction, or other status-changing
  claim edit.
- [`daily-research-portfolio-stewardship.md`](daily-research-portfolio-stewardship.md) -
  daily GU-local reconciliation of research priorities, dependencies, run receipts, and
  high-signal JoeOps routing.
- [`draft-factory-paper-seed-handoff.md`](draft-factory-paper-seed-handoff.md) - cheap
  paper-opportunity seed routing plus capacity-backed source-hardening requests.
- [`five-lane-frontier-run.md`](five-lane-frontier-run.md) - maintainer-directed divergent
  frontier run for ambitious, non-overlapping proof, bridge, no-go, or computation lanes.
- [`meaningful-hourly-progress-swing.md`](meaningful-hourly-progress-swing.md) - default hourly
  GU Progress run for one substantial, decision-grade swing from the steward-maintained portfolio.
- [`lean-verification-run.md`](lean-verification-run.md) - reserve Lean verification lane
  when the portfolio selects an already stable, finite, checkable kernel.
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
