# Zenodo release package — version 1.0.0

Primary artifact: `main.pdf`

Title: *A Diagonal No-Go for Self-Valuations and an Invariance Classification*

Author: Joe Hernandez, Independent Researcher

This is a self-contained proposed deposit package. It contains the article PDF and LaTeX source, the exact reproduction and verification receipts, and the narrow Lean/Python source used for the machine-checked and finite-instance claims.

## Contents

- `main.pdf` — article of record
- `main.tex` — release source
- `METADATA.md` and `CITATION.cff` — deposit metadata
- `reproduction.md` — exact commands and formalization scope
- `VERIFICATION.md` — mathematical, Lean, test, bibliography, and PDF receipt
- `Lean/GUFormalization/ResidualSelection.lean` — Lean proof source
- `Lean/GUFormalization/ResidualSelectionAxioms.lean` — explicit axiom receipt
- `tests/W99_theorem_finite_instances.py` — dedicated finite confirmation
- `lakefile.lean` and `lean-toolchain` — minimal Lean project pin
- `LICENSE-DOCS.md` and `LICENSE-CODE.md` — documentation and code licenses
- `MANIFEST.sha256` — integrity manifest

The package intentionally excludes referee reports, persona reviews, internal run plans, broader GU tests, build caches, rendered QA images, and unrelated repository material.

## Reproduce

With Lean/Lake and Python available:

```text
lake -Kjobs=1 build +GUFormalization.ResidualSelection
lake env lean Lean/GUFormalization/ResidualSelectionAxioms.lean
python tests/W99_theorem_finite_instances.py
```

To rebuild the paper:

```text
tectonic main.tex
```

No network upload, Zenodo submission, DOI reservation, Git tag, commit, or push was performed while preparing this staging package.
