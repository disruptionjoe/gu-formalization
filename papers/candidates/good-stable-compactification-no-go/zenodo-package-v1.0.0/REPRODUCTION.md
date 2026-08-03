# Reproducing the paper-specific checks

Repository: <https://github.com/disruptionjoe/gu-formalization>

Source revision:
`507cd21bb2edf72db96d55ba3cef3f9f7e23ff26`

The source ZIP contains the editable paper, standalone TeX, exact certificate
sources, locked Python environment, narrow Lean project, and verification
records. The written manuscript is the proof; these commands independently
check the disclosed formal kernel and concrete quaternionic specialization.

Run the commands below from the extracted source archive root.

## 1. Exact property-based certificate

Requirements: Python 3.11-3.14 and `uv`.

```sh
UV_CACHE_DIR="${UV_CACHE_DIR:-/tmp/compact-image-uv-cache}" uv lock --check --project evidence
UV_CACHE_DIR="${UV_CACHE_DIR:-/tmp/compact-image-uv-cache}" uv run --locked --project evidence python evidence/compact_image_obstructions_properties.py
```

Expected headline:

```text
PASS exact property certificate: 400 generated examples plus deterministic controls
```

The implementation uses exact integer quaternions, deterministic Hypothesis
generation, and planted wrong-sign and mixed-parity mutants.

## 2. Exact SageMath certificate

Requirement: SageMath 10.9 or a compatible later release.

```sh
DOT_SAGE="${DOT_SAGE:-/tmp/compact-image-sage}" sage -python evidence/compact_image_obstructions_exact.py
```

Expected headlines:

```text
PASS exact SageMath certificate: 2721 checks
decomposition: 8256 = 2080 + 4096 + 2080
```

The certificate uses the rational quaternion algebra; no floating point or
tolerance is used.

## 3. Lean 4 kernel and axiom receipt

The archive pins Lean and mathlib in `lean-toolchain` and
`lake-manifest.json`.

```sh
ELAN_NO_UPDATE_CHECK=1 lake exe cache get
ELAN_NO_UPDATE_CHECK=1 lake build +GUFormalization.CompactImageObstructions +GUFormalization.CompactImageObstructionsAxioms
ELAN_NO_UPDATE_CHECK=1 lake env lean Lean/GUFormalization/CompactImageObstructionsAxioms.lean
```

The cache command is recommended for a clean extraction; it retrieves the
pinned Mathlib build cache rather than recompiling the full imported dependency
graph. It does not replace either paper-specific Lean command.

The expected axiom receipt names only Lean's standard `propext` and, for the
two weight-shift declarations, `Quot.sound`. No project-specific axiom or
`sorry` is used.

## 4. Rebuild the paper

With Tectonic installed:

```sh
tectonic compact-image-obstructions-sp32-32-v1.0.0.tex
```

## Scope

Lean checks seven narrow algebraic declarations. SageMath and Python check the
explicit quaternionic specialization. None of these tools formalizes compact
Haar averaging, the full real-reductive theorem, or any physical
interpretation. Exact checked outputs and environment versions are recorded in
`VERIFICATION.md`.
