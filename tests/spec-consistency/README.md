# tests/spec-consistency/

Consolidation certificates for specification-level consistency checks. This
family currently maps the H41 source-action requirements spec and verifies that
its arithmetic anchors and class tallies are mutually consistent with already
computed repo artifacts.

These scripts are not a source-action build and not new physics. A green run
means the listed consolidation arithmetic still matches the companion spec at
its stated grade. It does not move claim status, canon, verdicts, public posture,
paper status, or the source-action wall.

## Running This Family

Run the current certificate directly:

```powershell
python tests\spec-consistency\source_action_requirements_consistency.py
```

## Boundary

The public boundary stays:

- This directory maps source-action requirements consistency checks.
- It consolidates already stated arithmetic and table counts; it does not build
  the source action.
- It does not supply a GU-forced generation count, close H41, or resolve H59.
- Do not use these scripts to change canon, claim status, verdicts, public
  posture, paper status, or protected governance surfaces.

## Direct Certificates

| script | role | review note |
|---|---|---|
| `source_action_requirements_consistency.py` | Rechecks the H41 requirements spec's soldering, sector-bookkeeping, residue, cure-uniqueness, flavor-lift, mu_DW-window, and class-tally arithmetic. | Consolidation only; every check reproduces arithmetic already established in cited artifacts, and the source action remains unbuilt. |

## Companion Exploration

`explorations/source-action-requirements-spec-2026-07-13.md`

## Process Gate

`process_gates/spec_consistency_readme_inventory_audit.py` keeps this
README synchronized with tracked direct scripts in this directory and checks
that the consolidation / not-new-physics / no-verdict-change boundary remains
visible.
