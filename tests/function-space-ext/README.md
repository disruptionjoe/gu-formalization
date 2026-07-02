# WC-FUNCTION-SPACE-EXT probes (2026-07-02)

Executable probes for the post-publication function-space extension card in `NEXT-STEPS.md`.

These scripts separate three layers of the function-space question:

- `krein_spectral_flow_probe.py` is the first finite-Galerkin model: paired Krein-compatible
  crossings contribute zero net chiral flow, while a one-sided control leaves the modeled class.
- `dirac_spectral_flow_section.py` is the computed conditional section-setting theorem for the
  closed/interior 1D Krein-Dirac model.
- `verify/dirac_spectral_flow_indep_check.py` independently re-checks the section theorem with a
  Fourier momentum substrate and non-degenerate spectrum.
- `aps_eta_boundary_control.py` is an exploration-grade finite boundary-spectrum control for the
  APS/noncompact-end residual; it does not compute the Rarita-Schwinger eta invariant.

## Running

From the repo root:

```text
python tests/function-space-ext/krein_spectral_flow_probe.py
python tests/function-space-ext/dirac_spectral_flow_section.py
python tests/function-space-ext/verify/dirac_spectral_flow_indep_check.py
python tests/function-space-ext/aps_eta_boundary_control.py
```

## Status

The closed/interior, spectral-gapped section model is a computed + independently re-verified
conditional theorem. The APS/noncompact-end eta correction, family-index / higher-topology
terms, and full Rarita-Schwinger bundle analytic hypotheses remain open.
