# WC-FUNCTION-SPACE-EXT first probe scripts (2026-07-02)

Executable probes for the post-publication function-space extension card in `NEXT-STEPS.md`.

These scripts do not prove the section/Fredholm theorem. They provide a finite-Galerkin
model for the spectral-flow obstruction:

- Krein-compatible paired crossings in a cross-chirality model contribute zero net chiral flow.
- Pure Krein-isometric conjugacy preserves the spectrum, so no new crossing is created.
- A one-sided chiral crossing produces nonzero net flow only in the control that violates the
  modeled Krein-pairing condition.

## Running

From the repo root:

```text
python tests/function-space-ext/krein_spectral_flow_probe.py
```

## Status

Exploration-grade. The actual work card remains open until the unbounded-operator,
domain, APS/end, Fredholm, and spectral-section hypotheses are stated and checked for the
Rarita-Schwinger bundle setting.
