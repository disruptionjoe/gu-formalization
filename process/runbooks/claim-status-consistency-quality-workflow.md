---
title: "Claim-Status Consistency Quality Workflow"
status: canon
doc_type: runbook
scope: repo-local
updated_at: "2026-06-25"
---

# Claim-Status Consistency Quality Workflow

Use this workflow whenever a result promotes, downgrades, corrects, or substantially
re-scopes a research claim. Its job is to stop path-dependent status drift: future agents
should not have to rediscover that an older "resolved" phrase was later narrowed.

## Trigger

Run this workflow before committing if any changed artifact:

- changes a verdict, status label, or canon/not-canon boundary;
- weakens a load-bearing assumption;
- keeps historical prose that could be read as the current claim;
- promotes an exploration, paper draft, or roadmap item into a stronger public surface.

## Source Of Truth Order

When surfaces disagree, prefer the newest explicit correction on the claim's owner
artifact, then canon/status ledgers, then roadmaps and papers, then historical
explorations.

Owner surfaces to check:

1. the source artifact or exploration being corrected;
2. `RESEARCH-STATUS.md`;
3. `CANON.md`;
4. affected files under `canon/`;
5. `DERIVATION-PROGRESS.md`;
6. `NEXT-STEPS.md`;
7. current paper drafts;
8. tests or audits that encode the old claim.

## Consistency Rules

- A downstream claim cannot have a stronger status than its weakest load-bearing
  dependency.
- Same-session resolution of a named contradiction cannot immediately become canon-grade
  without an independent later pass.
- If old prose remains for provenance, add a nearby "historical" or "superseded" marker
  and point to the current owner surface.
- Do not rewrite every historical file mechanically; do guard any file likely to be read
  as a current roadmap, canon entry, or live draft.
- Prefer exact claim IDs in correction notes, such as `SHIAB-01`, `ANOMALY-01`, or
  `GEN-OPEN-01`.

## Formal Certificate Boundary

```yaml
formal_certificate:
  lean_module: GUFormalization.Status
  lean_file: Lean/GUFormalization/Status.lean
  certified_definitions:
    - ClaimStatus
    - AllowedByDeps
  certified_theorems:
    - claim_le_first_dependency
    - verified_not_allowed_over_open
    - resolved_not_allowed_over_open
  scope: finite_status_order_and_dependency_monotonicity_kernel_only
  does_not_claim:
    - markdown_parsing
    - owner_surface_discovery
    - historical_prose_classification
    - mathematical_correctness_of_any_GU_claim
```

## Required Sweep

1. Name the claim, prior status, proposed status, and load-bearing dependencies.
2. Search for stale stronger wording in owner surfaces and live drafts.
3. Patch every owner surface so it either carries the current status or explicitly says
   the stale text is historical.
4. Record the downgrade/promotion in `RESEARCH-STATUS.md`.
5. Run `git diff --check`.

Useful searches:

```text
rg -n "FULLY CLOSED|VERIFIED|EVADED|CONDITIONALLY 3|CONDITIONALLY_3|ANOMALY_CANCELS|ind_H\\(D_GU\\)=24" RESEARCH-STATUS.md CANON.md DERIVATION-PROGRESS.md NEXT-STEPS.md canon papers
rg -n "Noether|D_A\\*theta|D_A\\*theta|Sp\\(64\\)|U\\(128\\)|injectiv|kernel|rank" RESEARCH-STATUS.md CANON.md DERIVATION-PROGRESS.md NEXT-STEPS.md canon papers
```

## Status-Change Table

Use this table shape in the integration note or status ledger:

| claim | prior status | current status | weakest dependency | stale wording searched | files updated |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

## Acceptance Criteria

A status-changing patch is acceptable only if:

- no current owner surface asserts a stronger status than the corrected claim;
- old stronger wording is either removed or explicitly marked superseded;
- affected roadmaps and paper drafts cannot mislead a future agent about the current
  claim boundary;
- `git diff --check` passes;
- any machine audit that tracks the claim is updated or deliberately left as historical.

## Machine-Readable Workflow

```json
{
  "artifact": "CLAIM_STATUS_CONSISTENCY_QUALITY_WORKFLOW",
  "trigger": "before_commit_for_status_changing_claims",
  "required_owner_surfaces": [
    "source_artifact",
    "RESEARCH-STATUS.md",
    "CANON.md",
    "canon/",
    "DERIVATION-PROGRESS.md",
    "NEXT-STEPS.md",
    "current_paper_drafts",
    "tests_or_audits"
  ],
  "stronger_downstream_status_forbidden": true,
  "historical_prose_requires_supersession_marker": true,
  "same_session_contradiction_resolution_blocks_canon_promotion": true,
  "verification": [
    "targeted_rg_sweep",
    "git_diff_check"
  ]
}
```
