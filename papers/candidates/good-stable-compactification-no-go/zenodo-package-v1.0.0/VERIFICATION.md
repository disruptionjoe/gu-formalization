---
release_version: "1.0.0"
scientific_gate_verdict: "pass"
actionable_hardening_remaining: 0
pdf_visual_qa_verdict: "pass"
pdf_default_preview_required: true
verified_pdf: "compact-image-obstructions-sp32-32-v1.0.0.pdf"
verified_pages: 13
source_archive_clean_room_verdict: "pass"
source_commit: "507cd21bb2edf72db96d55ba3cef3f9f7e23ff26"
---

# Release verification - v1.0.0

## Scientific identity and hostile gate

- The package is bound to reviewed source commit
  `507cd21bb2edf72db96d55ba3cef3f9f7e23ff26`.
- The editable Markdown SHA-256 is
  `406bbf731ab1f58c6de097f25b59695ee59c2217b1919745738d52c22a6e39be`.
- The version-bound specialist and publication/reproducibility hostile passes
  report `fatal=0`, `major=0`, `minor_actionable=0`, and
  `actionable_hardening_remaining=0`.
- Remaining criticisms are declared successor scopes: non-extremal
  classification, infinite-dimensional analysis, a physical application
  dictionary, or independent external review.
- Generative AI use and author responsibility are disclosed in the paper.

## Paper-specific scientific checks

### Exact SageMath certificate

Result: **PASS**

```text
PASS exact SageMath certificate: 2721 checks
decomposition: 8256 = 2080 + 4096 + 2080
arithmetic: rational quaternions; no floating point or tolerances
```

### Independent exact property certificate

Result: **PASS**

```text
PASS exact property certificate: 400 generated examples plus deterministic controls
arithmetic: integer quaternions; no floating point or tolerances
planted mutants rejected: wrong X_+ sign; noncommuting-is-not-purely-odd
```

### Lean 4 kernel and axiom receipt

Result: **PASS**

The seven paper declarations compile under the pinned Lean/mathlib project.
The clean-room axiom receipt reports only `propext` and, for the two
weight-shift declarations, `Quot.sound`. It reports no project-specific axiom
or admitted declaration.

## TeX, PDF, and visual QA

- The standalone TeX compiles successfully with Tectonic.
- Tectonic reports no overfull box, underfull box, missing-character, or
  compilation error. Its two `unicode-math` notices describe standard command
  selection and do not identify a rendered defect.
- The PDF is 13 US-letter pages with title, subject, keywords, author, page
  count, and page-size metadata present and correct.
- All 13 pages were rendered at 140 dpi and inspected visually.
- Mathematics, quaternionic blocks, the four-row obstruction table, lists,
  links, references, page numbers, margins, and the final evidence appendix are
  legible with no clipping, overlap, raw Markdown, or raw TeX.
- After the final source cleanup, a second 13-page render was pixel-identical
  to the inspected render on every page.
- A PDF text-layer scan found nonempty text on all pages and no raw `$$`, code
  fence, or `\\operatorname` source tokens.

## Standalone source archive

Result: **PASS**

The final ZIP contains 29 entries and excludes `.venv`, `.lake`,
`__pycache__`, `.DS_Store`, and build artifacts. After extraction into a clean
directory:

- `SOURCE-MANIFEST.sha256` validated every archived file;
- the exact property certificate passed;
- the exact SageMath certificate passed;
- Mathlib's pinned cache was obtained and both paper-specific Lean modules
  compiled, followed by the expected axiom receipt; and
- Tectonic rebuilt a 13-page US-letter PDF with the correct title and author.

## Metadata and integrity controls

- `CITATION.cff` parses as YAML 1.2 metadata and names Joseph Hernandez,
  Independent Researcher.
- `METADATA.md` includes copy-ready title, description, keywords, creator,
  affiliation, license, repository URL, and exact source-revision URL.
- The package-level `MANIFEST.sha256` freezes every upload payload except the
  manifest itself.

## Frozen principal hashes

```text
406bbf731ab1f58c6de097f25b59695ee59c2217b1919745738d52c22a6e39be  compact-image-obstructions-sp32-32-v1.0.0.md
215f3e66278fef15c18dc1c56b26be3220884140a472d92d8c0a5a1d395843ac  compact-image-obstructions-sp32-32-v1.0.0.tex
1bd6e71ee4a4f5a53b6fef4548fc55aea5334f708d7d003bae7fac99d64582e4  compact-image-obstructions-sp32-32-v1.0.0.pdf
e5511db2167df2381a9819971210956c917e674e5214348e19fbba38f83d9b19  compact-image-obstructions-sp32-32-source-v1.0.0.zip
```

## Deposit rule

`compact-image-obstructions-sp32-32-v1.0.0.pdf` is the version of record and
must be the Zenodo default preview. The Markdown, TeX, and ZIP are public
source. This package has been prepared and validated but not posted; the final
Zenodo Publish action requires separate explicit approval.
