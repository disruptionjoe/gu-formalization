---
title: "Runbook: publication-status reconciliation (repo ledger vs live venue)"
status: active
doc_type: runbook
owner: gu-formalization
updated: "2026-07-22"
canonical_ledger: papers/published/INDEX.md
---

# Publication-status reconciliation

**Purpose.** Keep `papers/published/INDEX.md` (the canonical posted-status ledger) in sync with reality.
Joe posts artifacts himself, often out-of-band, and no internal surface is automatically told — so the
repo, the Drafting Factory, and project management can silently drift out of agreement about what is
posted. This runbook is the reconciliation that catches it. (It is how the 2026-07-22 OVST / gen-count
DOI mix-up was found.)

## When to run
- After Joe says he posted something.
- When any "post X" work item closes, or posting status is in question.
- On a periodic stewardship cadence (recommend weekly during active publishing).

## Procedure
1. **Enumerate Joe's actual public records.** Zenodo is the primary venue. Query BOTH author-name forms Joe
   uses (the OVST record is under "Hernandez, Joe"; PP3/LNF are slated under "Joseph Hernandez"):
   - `https://zenodo.org/api/records?q=creators.name:"Hernandez, Joe"`
   - `https://zenodo.org/api/records?q=creators.name:"Hernandez, Joseph"`
   - Title search for any expected-but-missing paper, e.g. `q="Located, Not Forced"`.
   - Screen out namesakes (a "Hernandez, Joseph" education paper from Batangas is a different person).
   - Also check arXiv / any other venue Joe used.
2. **Diff the venue result against the ledger** (`papers/published/INDEX.md`):
   - On venue but NOT in the ledger → Joe posted out-of-band. Add it (title, DOI, concept DOI, date,
     author-name-used, source path) and move its source dir `candidates/` → `published/`.
   - In the ledger but NOT on the venue → stale/erroneous; investigate and correct.
   - A DOI attributed to the WRONG paper anywhere → correct against the venue's ACTUAL title. (Verify by
     fetching the record: its title/abstract is ground truth, not any internal note.)
3. **Propagate the corrected truth:**
   - Update `papers/README.md` "Currently" and `papers/candidates/README.md` (folder membership is the
     status signal).
   - Drop a notification to the Drafting Factory mailbox (`system-runtime/mailboxes/drafting-factory/`) and
     to `system-attention` so the factory inventory and Joe's PM reflect the same posted-status.
   - Correct any external PM record that disagrees (e.g. `joe-project-management` work items).
4. **Log** the reconciliation date + result in the ledger's "Reconciliation log".

## Source of truth
`papers/published/INDEX.md` is authoritative for THIS repo's posted-status. Cross-surface consumers (the
Drafting Factory, project management) READ it; they do not maintain a competing posted-status truth.
