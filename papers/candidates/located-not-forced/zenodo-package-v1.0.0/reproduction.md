# Reproduction guide

Repository: <https://github.com/disruptionjoe/gu-formalization>

## 1. Python evidence

The tested environment uses Python 3.14.6, NumPy 2.5.1, and SymPy 1.14.0.

```text
python -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python reproduce_all.py
.venv/bin/python validate_release_evidence.py --repo-root .
```

`reproduce_all.py` deterministically recomputes 31 load-bearing numerical and symbolic checks and executes
discriminating controls. Exit 0 means all declared values matched. `validate_release_evidence.py` checks the
machine-readable evidence inventory, coverage arithmetic, file references, and source anchors; it does not
replace execution of the numerical harness.

## 2. Lean evidence

The toolchain is pinned in `lean-toolchain`; dependency revisions are pinned in `lake-manifest.json`.

```text
lake -Kjobs=1 build +GUFormalization.LocatedNotForcedFiniteCore
lake env lean tests/located-not-forced/H2_FiniteCore.lean
lake env lean tests/located-not-forced/V15_CodomainSeparatedFiniteCore.lean
lake env lean tests/located-not-forced/V15_KreinTransversality.lean
lake env lean Lean/GUFormalization/R4TwoArena.lean
```

The finite-core module machine-checks the encoded two-block matching packet, exhaustive finite generator
type, exact power-of-two modulus packet, arbitrary product/gcd/lcm 2-primary closure, and the typed vanishing
of additive maps `ZMod 3 →+ Z`. The physical 192-dimensional carrier census is supplied as computed input;
the module does not reconstruct that carrier end to end.

## 3. Rebuild the paper

With Tectonic 0.16.9:

```text
tectonic -X compile main.tex --outdir build
```

The deposited `main.pdf` is the source-of-record build from `main.tex`. After rebuilding, inspect every page;
successful compilation alone is not visual verification.

## Scope boundary

Passing every packaged check is internal-tier reproduction. It does not establish external peer review,
identify a torsion class with an integer count, replace the indefinite Krein structure with Hilbert
positivity, prove completeness outside class C, or close the true-`Y14` source-action residual.
