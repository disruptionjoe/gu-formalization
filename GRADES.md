---
title: "Grade and Status Crosswalk"
status: process
doc_type: reference
updated_at: "2026-08-26"
---

# Grade and Status Crosswalk

This repository uses several vocabularies that answer different questions.
They are orthogonal: no label on one axis automatically promotes, resolves, or
converts a label on another.

| axis | question answered | representative labels | what it does not mean |
| --- | --- | --- | --- |
| document status | What role does this file play? | `canon`, `active_research`, `exploration`, `process`, `archive`, `source`, `draft` | A file role is not a scientific verdict or evidence grade. |
| evidence / verification grade | How strongly is this result established, and by what method? | L1/L2/L3 where an artifact defines that ladder; `EXACT`, proof-grade, computed, independently re-verified, reconstruction, proposal, toy | Strong computation does not by itself make a physical interpretation canon or resolved. |
| claim or canon verdict | What is the current disposition of the exact scoped claim? | `RESOLVED`, `CONDITIONALLY_RESOLVED`, `OPEN`, plus explicitly scoped corrections and no-go dispositions | `RESOLVED` is never inferred from a file's location, an executable's green exit, or a hosting grade. |
| construction / hosting level | How much of the intended physical structure has been built? | proposal, toy, consistency, hosting, forcing | Hosting shows fit under supplied inputs; it does not mean the inputs or observed physics were forced. |

## Reading rule

Read all applicable axes. A `canon` file may contain an `OPEN` claim at
reconstruction grade; an exact toy computation may remain an `exploration`;
and a hosting-grade construction may still depend on supplied external data.
The weakest load-bearing dependency and the artifact's stated claim ceiling
control what may be cited.

When an artifact uses L1/L2/L3, use the definition local to that artifact or
method. Those tokens are not globally substituted for proof, computation, or
reconstruction labels unless the owning surface explicitly defines that map.

## Status-field boundary

`RESEARCH-STATUS.md` declares the seven document-role values above for
Markdown research documents. Historical and operational artifacts also use a
frontmatter key named `status` for verdicts, run phases, review outcomes, and
append-only ledger states. Those values are not silently added to the seven-
value document-role vocabulary and are not normalized by this crosswalk.

The complete tracked population is frozen in
`lab/process/frontmatter-status-population.yaml`: 2,831 status-bearing files,
including 1,452 legacy untyped uses. Those historical values remain local to
their artifacts and protected by a content-addressed ratchet; they are not a
global vocabulary and are never rewritten by string substitution.

New Markdown documents, and intentional changes to a legacy non-role value,
use the axis-specific keys selected by that contract: `status` for the seven
document roles, `claim_verdict` for scientific disposition, and
`operational_state` for run, review, workflow or append-only ledger state.
Changing the frozen mapping requires an explicit manifest update and semantic
review rather than silent normalization.

## Change discipline

- Changing a document role does not change a claim verdict.
- Changing an evidence grade or claim verdict follows
  `lab/methods/claim-status-consistency.md`.
- New evidence never promotes itself to canon.
- A green certificate proves only its declared claim and controls.
- Public wording must preserve the construction level and exact claim ceiling.
