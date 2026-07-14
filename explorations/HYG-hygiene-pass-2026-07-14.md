---
title: "HYG hygiene pass"
status: exploration
doc_type: lab-note
updated_at: "2026-07-14"
---

# HYG hygiene pass (2026-07-14)

Lab record, not canon. This note describes a repo-hygiene pass only. It moves no
verdict, canon, RESEARCH-STATUS, claim status, or public posture, and asserts no
research result. Do not cite as a result.

Scope: bring the two RED process gates from the W189 hardening register to GREEN
and scrub em dashes from submission-facing support docs. No science touched.

## H01 -- explorations README surface map

`explorations/wave46/` existed on disk but was undeclared in
`explorations/README.md`, so `process_gates/explorations_readme_surface_map_audit.py`
was RED (live directories did not match linked directories). Fix: added the
`wave46` link to the "Hypothesis-wave runs" wave list. Gate now GREEN.

## H02 -- explorations top-level file boundary

`process_gates/explorations_top_level_file_boundary_audit.py` asserted a stale
4-entry allow-list for top-level `explorations/*.md`, but ~200 dated arc notes
(the W-wave / dated-exploration lab record, named `<slug>-YYYY-MM-DD.md`) now
legitimately sit at the top level. This was a stale convention, not a real
boundary breach: every top-level note matches either the curated allow-list or
the dated-arc naming convention.

Fix: rescoped the gate (not the files). Top-level Markdown is now accepted if it
is a curated boundary-labeled stub OR a dated arc note. The boundary intent is
preserved: any undated, non-allow-listed loose file still fails, the curated
stubs still must carry their explicit boundary phrases, and the README-level
"research lab, not the project canon" language is still required. No files moved.
Foldering the dated notes into topical subdirectories remains a separate,
optional FILL-IN item; it is not required for the boundary to hold.

## H03 -- em-dash scrub (submission-facing support docs)

Replaced every em dash (U+2014) with ` -- ` in the submission-facing support
docs that contained them:

- `papers/candidates/located-not-forced/ENDORSER-REQUEST-DRAFT.md` (11)
- `papers/candidates/located-not-forced/REVIEWER.md` (12)
- `papers/candidates/located-not-forced/SUBMISSION-RUNBOOK.md` (17)
- `papers/candidates/located-not-forced/ZENODO-RELEASE-CHECKLIST.md` (8)
- `papers/candidates/observer-value-selection-theorem/submission/VERIFICATION.md` (1)
- `papers/candidates/observer-value-selection-theorem/submission/reproduction.md` (1)

En dashes (U+2013) were left as-is: all occurrences are compound-name connectors
(Rarita-Schwinger, Kochen-Specker, Cantor-Lawvere, and similar) or numeric ranges
(`~1-2 weeks`), none functioning as em dashes. The submission papers themselves
(`main.tex`, `COMPILE.md`) already contained zero em dashes and were verified,
not edited. Changes are dash-only; no wording changed.

## Gate results

Both target gates GREEN after the pass. The full `process_gates/` suite has one
unrelated RED (`tests_root_readme_inventory_audit`: `tests/README.md` says 149
W-series packets, actual 150) caused by the separately committed W192 test, not
by this pass; flagged for the owning team.
