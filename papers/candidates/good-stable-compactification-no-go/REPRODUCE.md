# Reproducing the paper-specific checks

Run all commands from the `gu-formalization` repository root. The written
manuscript is the proof; these commands independently check its narrow formal
kernel and exact concrete specialization.

## 1. Exact property-based certificate

Requirements: Python 3.11–3.14 and `uv`.

```bash
UV_CACHE_DIR="${UV_CACHE_DIR:-/tmp/compact-image-uv-cache}" \
  uv lock --check \
  --project papers/candidates/good-stable-compactification-no-go/evidence

UV_CACHE_DIR="${UV_CACHE_DIR:-/tmp/compact-image-uv-cache}" \
  uv run --locked \
  --project papers/candidates/good-stable-compactification-no-go/evidence \
  python papers/candidates/good-stable-compactification-no-go/evidence/compact_image_obstructions_properties.py
```

Expected headline:

```text
PASS exact property certificate: 400 generated examples plus deterministic controls
```

The calculation uses a separate integer-quaternion implementation and no
floating point. Hypothesis is configured with `derandomize=True`.

## 2. Exact SageMath certificate

Requirement: SageMath 10.9 or a compatible later release.

```bash
DOT_SAGE="${DOT_SAGE:-/tmp/compact-image-sage}" \
  sage -python papers/candidates/good-stable-compactification-no-go/evidence/compact_image_obstructions_exact.py
```

On the Mac used for the recorded run, `sage` was:

```text
/Applications/SageMath-10-9.app/Contents/Frameworks/Sage.framework/Versions/Current/venv/bin/sage
```

Expected headlines:

```text
PASS exact SageMath certificate: 2721 checks
decomposition: 8256 = 2080 + 4096 + 2080
```

All matrices use the rational quaternion algebra $(-1,-1)_{\mathbb Q}$. The
certificate also checks the exact unnormalized isotropic basis change
$T=\sqrt2S$, its inverse, and the upper/diagonal/lower transformed blocks.

## 3. Lean kernel and axiom receipt

The repository pins Lean and mathlib in `lean-toolchain` and
`lake-manifest.json`. The paper-specific wrapper acquires the repository's
exclusive Lean build lock before invoking Lake:

```bash
sh papers/candidates/good-stable-compactification-no-go/evidence/check_lean_receipt.sh
```

It compiles:

- `Lean/GUFormalization/CompactImageObstructions.lean`
- `Lean/GUFormalization/CompactImageObstructionsAxioms.lean`

and prints the axiom dependencies of all seven paper-facing declarations. The
expected dependencies are only Lean's standard `propext` and, for the two
weight-shift declarations, `Quot.sound`. No project-specific axiom is used.

## Scope of machine checking

Lean checks the involutory-conjugation lemma, a pointwise weight-shift lemma,
its explicit no-higher-weight consequence, and mutually square-zero block maps
over a possibly noncommutative ring. Sage and Python check the exact
quaternionic specialization. None of these tools formalizes Haar averaging,
the complete real-reductive group theorem, or any physical interpretation.

## 4. Frozen-file checksums

```bash
shasum -a 256 -c \
  papers/candidates/good-stable-compactification-no-go/evidence/checksums.sha256
```

The checksum manifest covers the manuscript, reproduction and verification
notes, both exact certificates, the locked Python environment, the Lean
wrapper, and both Lean modules. It intentionally does not hash itself.
