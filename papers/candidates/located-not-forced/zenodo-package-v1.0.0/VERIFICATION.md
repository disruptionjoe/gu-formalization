# Release verification — version 1.0.0

**Verified:** 2026-07-23  
**Immutable source checkpoint:** `020b682d3adf166d2b90017eb18b57be554af83c`

This receipt records validation of the package after extraction from the
Zenodo ZIP into a clean temporary directory. It is an internal release receipt,
not a claim of independent peer review.

## Package and paper

- `MANIFEST.sha256`: all 63 non-manifest package files matched.
- `SOURCE-COMMIT.txt`: matched the immutable source checkpoint above.
- `main.pdf`: 18 US-letter pages; title and author metadata matched.
- `main.pdf` SHA-256:
  `ad082f47e2c5601946ee5269221ed7bad755383021b47d1ad55e6a49cc2df369`
- A clean Tectonic 0.16.9 rebuild of the extracted `main.tex`, with the
  deposited reproducible-build timestamp, was byte-identical to `main.pdf`.
- Every page of the final PDF was rendered and visually inspected. No clipping
  or overlap was found. The TeX log has no overfull box; one benign underfull
  paragraph warning remains.

## Executable evidence

- Numerical and symbolic reproduction: **31/31 passed**.
- Release-evidence inventory and claim-ledger validator: **passed**.
- Physical Lorentzian signature discriminator: **53/53 passed**, including
  exact machine-receipt matching.
- Framing convention and sensitivity discriminator:
  `PASS_WITH_DECLARED_GU_TANGENTIAL_IDENTIFICATION_PREMISE`.
- Package integrity manifest: **passed**.

Tested Python environment: Python 3.14.6, NumPy 2.5.1, SymPy 1.14.0.

## Formal evidence

The extracted package passed:

```text
lake -Kjobs=1 build +GUFormalization.LocatedNotForcedFiniteCore
lake env lean tests/located-not-forced/H2_FiniteCore.lean
lake env lean tests/located-not-forced/V15_CodomainSeparatedFiniteCore.lean
lake env lean tests/located-not-forced/V15_KreinTransversality.lean
lake env lean Lean/GUFormalization/R4TwoArena.lean
```

The reported dependencies were the standard Mathlib axioms `propext`,
`Classical.choice`, and `Quot.sound`; no custom axiom was introduced.

## Release boundary

These checks establish internal reproducibility of the deposited, scoped
claims. They do not derive three generations, prove unrestricted `C_inv`,
close the true-`Y14` source-action residual, establish external replication, or
replace peer review.
