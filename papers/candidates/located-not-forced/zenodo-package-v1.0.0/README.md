# Zenodo release package — version 1.0.0

> **Preparation scaffold, not a release artifact.** The Markdown manuscript is still being hardened.
> Reconcile the final TeX/PDF, regenerate the integrity manifest, and complete `VERIFICATION.md` before upload.

Primary artifact: `main.pdf`

Title: *Located, Not Forced: Two-Primary Obstructions Cannot Force the Fermion Generation Count in a Clifford Rarita-Schwinger Sector*

Author: Joseph Hernandez, Independent Researcher

This package contains the article PDF and source, the readable v2.13 manuscript, a one-command
symbolic/numerical reproduction harness, a machine-readable evidence manifest, and the bounded Lean proof
surface. It is intentionally scoped to the paper rather than the wider research repository.

## Contents

- `main.pdf` — article of record and intended Zenodo default preview
- `main.tex` — release LaTeX source
- `manuscript-v2.13.md` — readable source copy
- `METADATA.md` and `CITATION.cff` — copy-ready deposit metadata
- `reproduction.md` — exact commands and dependency boundaries
- `VERIFICATION.md` — release validation receipt
- `REVIEWER.md` — clone-to-evidence reviewer route
- `PRIOR-ART-DELTA.md` — scoped literature-positioning table
- `LOAD-BEARING-NUMBERS.json` and `validate_release_evidence.py` — evidence inventory and validator
- `reproduce_all.py` — deterministic 31-check reproduction harness
- `Lean/GUFormalization/LocatedNotForcedLegs.lean` — existing finite theorem legs
- `Lean/GUFormalization/LocatedNotForcedFiniteCore.lean` — bounded class-C finite-core formalization
- `Lean/GUFormalization/R4TwoArena.lean` — typed two-arena arithmetic boundary
- `tests/located-not-forced/H2_FiniteCore.lean` — targeted Lean certificate
- `lakefile.lean`, `lake-manifest.json`, and `lean-toolchain` — pinned Lean project
- `requirements.txt` — tested Python package versions
- `LICENSE-DOCS.md` and `LICENSE-CODE.md` — documentation and code licenses
- `MANIFEST.sha256` — package integrity manifest

The package excludes internal persona reports, private run plans, unrelated repository tests, build caches,
and exploratory material that is not part of the release evidence.

## Fast reproduction

```text
python reproduce_all.py
python validate_release_evidence.py --repo-root .
lake -Kjobs=1 build +GUFormalization.LocatedNotForcedFiniteCore
lake env lean tests/located-not-forced/H2_FiniteCore.lean
```

Passing these commands is internal-tier reproduction. It does not replace external peer review and does not
derive three generations. Non-equivariant constructions and the true-`Y14` fiber
pushforward/source action remain open.
