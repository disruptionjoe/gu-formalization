# Zenodo Release Checklist -- post it publicly today, no endorsement

**Prepared:** 2026-07-09; research draft hardened 2026-07-23. **Status:** PUBLICATION RECONCILE DEFERRED.
**Purpose:** get *Located, Not Forced* public, citable, and open for review
**immediately**, with zero gatekeeping -- in parallel with the slower arXiv endorsement path.

Zenodo is CERN-operated, mints a permanent citable **DOI**, requires no endorsement, and carries none of the
crank reputation of no-gate physics dumps (viXra etc.). Posting here does **not** block arXiv or journal
submission later -- the arXiv nonexclusive license is preserved and most journals accept preprints.

All steps are Joe's. Agents do not create the account, upload, or publish.

## One prerequisite

- **Final compiled PDF.** The Markdown is currently canonical and has changed since the preliminary TeX/PDF
  pass. Reconcile, compile, render, and inspect the final PDF before using this checklist.
- **ORCID iD** (optional but do it -- 5 min, free, at orcid.org). It strengthens the Zenodo record *and* the
  endorser ask, and ties the work to a persistent scholarly identity.

## Checklist

1. **Account:** log in at zenodo.org with your ORCID or GitHub (either works; ORCID preferred for author
   linkage).
2. **New upload → files:** after the deferred release package is regenerated and verified, upload `main.pdf`
   first and keep it as the default preview. Upload the supplementary ZIP as the reproducibility/source
   bundle. The PDF is the human-facing paper; the ZIP is not the default preview.
3. **Resource type:** `Preprint`.
4. **Metadata:**
   - **Title:** Located, Not Forced: Two-Primary Obstructions Cannot Force the Fermion Generation Count in a
     Clifford Rarita–Schwinger Sector
   - **Authors:** Joseph Hernandez; affiliation: Independent Researcher (attach ORCID if available)
   - **Description:** paste the shortened abstract from the runbook (Step 3) -- it's already plain-text and
     self-contained.
   - **Keywords:** generation count, chirality, Clifford algebra, Rarita–Schwinger, stable homotopy, bordism,
     anomaly, Krein, hep-th, math-ph
   - **Related identifiers:** `https://github.com/disruptionjoe/gu-formalization`, relation
     *is supplemented by*. Confirm this field is visibly populated before publishing.
   - **License:** CC BY 4.0 for the paper and documentation. The supplementary bundle identifies code
     separately under the repository's code license.
5. **Publish only after the final-reconcile receipt is green.** The DOI is permanent and Zenodo is versioned,
   but the current scaffold is not the publication artifact.
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
