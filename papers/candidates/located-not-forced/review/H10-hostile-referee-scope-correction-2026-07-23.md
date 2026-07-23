# H10 hostile-referee scope correction

**Date:** 2026-07-23  
**Target:** `located-not-forced-generation-count-2026-06-29.md`  
**Disposition:** release-blocking objections corrected in the canonical Markdown draft. Final TeX/PDF/package
reconciliation is deferred until publication preparation resumes.

## Blocking objections and disposition

1. **Mixed codomains.** Earlier prose moved `Z`-valued equality/index constraints into a `Z/8` “arena.”
   The revision keeps finite torsion rows, integer-valued parity/divisibility rows, and the standard
   `Z/24 = Z/8 + Z/3` decomposition separate. CRT conclusions now require an explicit torsion-valued map.

2. **Krein diagnostic promoted to physical chirality.** The finite theorem is now stated as
   `chi_cap(P) = dim(P ∩ W_+) - dim(P ∩ W_-) = 0`. Numerical projection-image rank balance is labeled a
   separate diagnostic. Neither is described as a physical handedness count, graded trace, spectral flow,
   or Fredholm index.

3. **Overbroad operator no-go.** Claims that no interior operator can force an odd count, that antilinearity is
   the unique escape, and that the count is necessarily external were removed. The surviving audit is complete
   only for encoded finite class C and listed controls. Non-equivariant, K-definite, function-space, and
   true-`Y14` source-action constructions remain open.

4. **Wrong torsion order.** The framed class `2 in Z/24` and `e_R=1/12 in Q/Z` have additive order 12.
   Only the projected nonzero `Z/3` component has order 3.

5. **Prior-art overreach.** Wang already uses `Z/24` and `24/8=3`; Wan–Wang–Yau v2 explicitly separates
   2/3-primary data and uses CRT. The remaining novelty language is a search-bounded carrier-specific inverse
   assembly, not proof of publication novelty.

6. **Evidence semantics.** The disputed `256` is labeled a projector trace, not a physical index. The
   machine-readable manifest distinguishes 23 full independent derivations, one independent value-only
   check, six same-code-path checks, and one result with no second executable/formal path.

## Verification

- `validate_release_evidence.py --repo-root .`: PASS.
- `reproduce_all.py`: 31/31 enumerated checks PASS.
- `lake build`: PASS, 8,645 jobs; existing linter warnings only.
- `lake env lean tests/located-not-forced/H2_FiniteCore.lean`: PASS.
- Lean finite core remains bounded to the supplied class-C packet and does not claim carrier faithfulness or
  the true-`Y14` source-action result.

## Remaining publication gate

The Markdown is canonical for the current hardening campaign. Before publication, reconcile the TeX from the
Markdown, compile and render the final PDF, regenerate the package and SHA-256 manifest, run a fresh-checkout
reproduction, and inspect the final Zenodo metadata. The current package directory is explicitly a scaffold.
