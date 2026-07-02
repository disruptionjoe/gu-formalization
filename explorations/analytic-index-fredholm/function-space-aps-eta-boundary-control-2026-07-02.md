---
title: "WC-FUNCTION-SPACE-EXT APS Eta Boundary-Control Probe"
date: 2026-07-02
status: exploration
doc_type: exploration_note
work_card: WC-FUNCTION-SPACE-EXT
---

# WC-FUNCTION-SPACE-EXT APS Eta Boundary-Control Probe

## Question

The conditional section-setting theorem now covers the closed/interior, spectral-gapped
Krein-Dirac model: under the stated self-adjoint, chirality-odd, Krein-self-adjoint, and
Fredholm hypotheses, net chiral spectral flow is zero.

The remaining analytic residual includes APS/noncompact-end eta terms. This note makes
that residual concrete with a finite boundary-spectrum control.

## Executable Probe

Script:

```text
tests/function-space-ext/aps_eta_boundary_control.py
```

The model does not compute the Rarita-Schwinger eta invariant. It only checks the
minimal boundary mechanism:

- paired or symmetric boundary spectra have finite `eta_0 = #positive - #negative = 0`,
  kernel count `h = 0`, and APS half-term `(eta + h)/2 = 0`;
- paired deformations remain eta-neutral;
- one external unpaired positive boundary mode gives `eta_0 = +1` and half-term `+1/2`;
- one external unpaired negative boundary mode gives `eta_0 = -1` and half-term `-1/2`.

## Interpretation

This separates two facts that the work card must keep distinct:

```text
interior Krein-paired spectral flow = 0
boundary/end eta contribution = not decided by the interior theorem
```

So the v2.8 conditional theorem does not automatically close the APS/noncompact-end
residual. To close it, a later pass must prove one of the actual Rarita-Schwinger
boundary/end alternatives:

- the relevant boundary/end spectrum has a symmetry forcing the eta term to vanish,
- the eta/end term is nonzero and supplies external boundary data,
- or the APS/noncompact-end setup is not the correct analytic completion for the
  operator family being tested.

## Status

Exploration-grade boundary control only. No paper edit, no `CANON.md` promotion, and no
claim-status or verdict change. The conditional interior theorem stands; the APS/end and
family-index residual remains open.
