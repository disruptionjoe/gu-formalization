# Zenodo Release Checklist -- post it publicly today, no endorsement

**Prepared:** 2026-07-09; release verified 2026-07-23. **Status:** READY FOR JOSEPH HERNANDEZ'S EXPLICIT PUBLISH APPROVAL.
**Purpose:** get *Located, Not Forced* public, citable, and open for review
**immediately**, with zero gatekeeping -- in parallel with the slower arXiv endorsement path.

Zenodo is CERN-operated, mints a permanent citable **DOI**, requires no endorsement, and carries none of the
crank reputation of no-gate physics dumps (viXra etc.). Posting here does **not** block arXiv or journal
submission later -- the arXiv nonexclusive license is preserved and most journals accept preprints.

Preparation and draft-field completion may be assisted. The irreversible
Zenodo publish action requires Joseph Hernandez's explicit approval.

## One prerequisite

- **Final compiled PDF: complete.** The canonical Markdown, release TeX, and
  18-page PDF are reconciled, reproducible, and visually inspected.
- **ORCID iD** (optional but do it -- 5 min, free, at orcid.org). It strengthens the Zenodo record *and* the
  endorser ask, and ties the work to a persistent scholarly identity.

## Checklist

1. **Account:** log in at zenodo.org with your ORCID or GitHub (either works; ORCID preferred for author
   linkage).
2. **New upload → files:** upload
   `zenodo-package-v1.0.0/main.pdf` first and keep it as the default preview.
   Upload `located-not-forced-v1.0.0.zip` as the reproducibility/source bundle.
   The PDF is the human-facing paper; the ZIP is not the default preview.
3. **Resource type:** `Preprint`.
4. **Metadata:**
   - **Title:** Located, Not Forced: A Scoped Two-Primary Audit of a Clifford Rarita–Schwinger Generation
     Carrier
   - **Authors:** Joseph Hernandez; affiliation: Independent Researcher (attach ORCID if available)
   - **Description:** paste the shortened abstract from the runbook (Step 3) -- it's already plain-text and
     self-contained.
   - **Keywords:** generation count, chirality, Clifford algebra, Rarita–Schwinger, stable homotopy, bordism,
     anomaly, Krein, hep-th, math-ph
   - **Related identifiers:** `https://github.com/disruptionjoe/gu-formalization`, relation
     *is supplemented by*. Confirm this field is visibly populated before publishing.
   - **License:** CC BY 4.0 for the paper and documentation. The supplementary bundle identifies code
     separately under the repository's code license.
5. **Final-reconcile receipt: green.** The extracted ZIP passed its integrity
   manifest, 31/31 reproduction, 53/53 physical-signature audit, framing
   sensitivity guard, evidence validator, targeted Lean checks, and a
   byte-identical PDF rebuild. Stop for Joseph Hernandez's explicit approval
   before selecting **Publish**.
6. **Wire it back:** add the DOI badge/link to the GitHub repo README and to disruptionjoe.com, and use the DOI
   in the endorser note and anywhere you invite review.

## Alternative: GitHub-release route

Zenodo can auto-archive a GitHub release and DOI the whole repo snapshot. Skip it for now -- it DOIs the entire
`gu-formalization` repo, not the paper, which is noisier than a clean single-paper preprint record. Use the
direct PDF upload above; revisit repo-archival later if you want a citable code snapshot too.

## What this does and doesn't buy you

- **Does:** public, permanent, citable, reviewable **today**; a DOI for the endorser note and your surfaces;
  proof-of-priority timestamp.
- **Doesn't:** land in hep-th where physicists actually browse. That reach still needs the one arXiv
  endorsement. Run both; they don't conflict.
