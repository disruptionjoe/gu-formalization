# Final release receipt — Located, Not Forced v1.0.0

**Frozen:** 2026-07-23  
**Status:** READY FOR JOSEPH HERNANDEZ'S EXPLICIT ZENODO PUBLISH APPROVAL  
**Source checkpoint:** `020b682d3adf166d2b90017eb18b57be554af83c`

## Deposit files

1. `zenodo-package-v1.0.0/main.pdf` — upload first; keep as the default preview.
2. `located-not-forced-v1.0.0.zip` — upload second as the source and
   reproducibility supplement.

SHA-256:

```text
ad082f47e2c5601946ee5269221ed7bad755383021b47d1ad55e6a49cc2df369  main.pdf
2a675be66eba8c173df45042c2d6cdd3795ba1aee655cca9adc116a02293dff4  located-not-forced-v1.0.0.zip
```

The ZIP contains 64 files total: 63 entries covered by `MANIFEST.sha256`,
plus the manifest itself. It contains no `.DS_Store` or `__MACOSX` payload.

## Final validation

- Canonical v2.15 Markdown, `main.tex`, and `main.pdf` reconciled.
- 18-page US-letter PDF rendered and visually inspected page by page.
- PDF title and author metadata: correct (`Joseph Hernandez`).
- Clean extracted `main.tex` rebuild: byte-identical to deposited `main.pdf`.
- Extracted-package integrity manifest: all entries passed.
- Numerical/symbolic harness: 31/31 passed.
- Physical-signature audit: 53/53 passed.
- Framing sensitivity guard: passed with the declared
  GU-to-natural-tangential-framing premise.
- Evidence inventory/claim-ledger validator: passed.
- Targeted extracted-package Lean build and four Lean entrypoints: passed.
- CFF/YAML, JSON, Python compilation, and repository whitespace checks: passed.

## Zenodo metadata stop check

- Title: final.
- Creator: Joseph Hernandez.
- Affiliation: Independent Researcher.
- Type: Preprint.
- License: CC BY 4.0 for paper/documentation; bundled code remains MIT.
- Repository related identifier:
  `https://github.com/disruptionjoe/gu-formalization`, relation
  `is supplemented by`.
- DOI: intentionally unset until Zenodo assigns one.
- Default preview: `main.pdf`, not the ZIP.

No technical or metadata gate remains. The next irreversible action is Zenodo
**Publish**, which requires Joseph Hernandez's explicit approval.
