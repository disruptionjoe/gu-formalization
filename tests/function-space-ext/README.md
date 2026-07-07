# WC-FUNCTION-SPACE-EXT probes (2026-07-02)

Executable probes for the post-publication function-space extension card in
`NEXT-STEPS.md`.

This is a function-space extension script map only. It does not change claim status,
verdicts, public posture, canon, or the paper-cited generation-sector
scripts. The local boundary is: the closed/interior spectral-gapped model gives
a conditional theorem inside the cross-chirality Krein class, while the
noncompact-end, APS eta, UII, and family-index residuals remain open unless a
separate target operator or external topological datum is supplied.

## Direct certificates

- `krein_spectral_flow_probe.py` is the first finite-Galerkin model: paired
  Krein-compatible crossings contribute zero net chiral flow, while a one-sided
  control leaves the modeled class.
- `dirac_spectral_flow_section.py` is the computed conditional
  section-setting theorem for the closed/interior 1D Krein-Dirac model.
- `aps_eta_boundary_control.py` is an exploration-grade finite
  boundary-spectrum control for the APS/noncompact-end residual; it does not
  compute the Rarita-Schwinger eta invariant.
- `aps_end_eta_class_symmetry.py` upgrades the hand-picked boundary-control
  model to a class-generic symmetry check: inside the sector class, chirality
  odd plus Krein-self-adjoint end operators have symmetric spectra and zero eta.
- `gap_wellposedness_end.py` checks the noncompact-end gap-vs-well-posedness
  dichotomy for physical spectral projections inside the cross-chirality Krein
  class.
- `family_index_bundle.py` checks that a parameter-space family-index bundle
  term cancels inside the modeled interior class rather than supplying an
  internal odd count.
- `flux_index_2d.py` shows how an external magnetic-flux/topological datum can
  carry an odd chiral count, outside the interior Krein-self-adjoint model.
- `external_chiral_background_odd_count.py` pins where an external chiral
  background can supply odd count and where the closed interior class cannot.
- `uii_gap_certificate_validator.py` is the signed-readout OC1/OC2 Uniform
  Invertibility at Infinity certificate-shape validator: it accepts a uniformly
  gapped H-linear asymptotic family and rejects zero-gap and J-breaking controls.

## Independent checks

- `verify/dirac_spectral_flow_indep_check.py` independently re-checks the
  section theorem with a Fourier momentum substrate and non-degenerate spectrum.
- `verify/aps_end_eta_class_symmetry_indep_check.py` independently re-checks the
  end-eta spectral symmetry using odd moments rather than eigenvalue sorting.
- `verify/gap_wellposedness_indep_check.py` independently re-checks the
  gap/well-posedness dichotomy on seeded random Hermitian substrates.
- `verify/family_index_bundle_indep_check.py` independently re-checks the
  family-index cancellation with a different parameter and projector-completeness
  witness.
- `verify/flux_index_2d_indep_check.py` independently re-checks that the
  flux-index count tracks magnetic flux across different lattice sizes and odd
  flux values.
- `verify/uii_gap_certificate_indep_check.py` independently re-checks the UII
  certificate shape on rotated positive H-linear bases, with separate zero-gap
  and J-breaking controls.

## Running

From the repo root:

```text
python tests/function-space-ext/krein_spectral_flow_probe.py
python tests/function-space-ext/dirac_spectral_flow_section.py
python tests/function-space-ext/verify/dirac_spectral_flow_indep_check.py
python tests/function-space-ext/aps_eta_boundary_control.py
python tests/function-space-ext/aps_end_eta_class_symmetry.py
python tests/function-space-ext/verify/aps_end_eta_class_symmetry_indep_check.py
python tests/function-space-ext/gap_wellposedness_end.py
python tests/function-space-ext/verify/gap_wellposedness_indep_check.py
python tests/function-space-ext/family_index_bundle.py
python tests/function-space-ext/verify/family_index_bundle_indep_check.py
python tests/function-space-ext/flux_index_2d.py
python tests/function-space-ext/verify/flux_index_2d_indep_check.py
python tests/function-space-ext/external_chiral_background_odd_count.py
python tests/function-space-ext/uii_gap_certificate_validator.py
python tests/function-space-ext/verify/uii_gap_certificate_indep_check.py
```

For a manifest-only sweep, use:

```text
python scripts/reproduce_all.py --quick --tracked-only --list -k tests/function-space-ext
```

## Status

The closed/interior, spectral-gapped section model is a computed and
independently re-verified conditional theorem. The signed-readout OC1/OC2
noncompact extension now has a UII certificate shape, but the actual target
asymptotic operator and lower-bound proof remain open. The APS/noncompact-end
eta correction, family-index / higher-topology terms, external-background
imports, and full Rarita-Schwinger bundle analytic hypotheses remain open.
