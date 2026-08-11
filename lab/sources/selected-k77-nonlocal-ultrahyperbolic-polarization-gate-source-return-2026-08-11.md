---
artifact_type: source_return
created: 2026-08-11
status: SOURCE_CONFIRMS_SCALAR_NONLOCAL_REMEDY__SOURCE_SILENT_ON_GU_MATRIX_POLARIZATION
---

# Source return: K77 nonlocal ultrahyperbolic polarization gate

## Primary literature

Walter Craig and Steven Weinstein, *On determinism and well-posedness in
multiple time dimensions*, arXiv:0812.0210, prove for the scalar
ultrahyperbolic equation that generic Sobolev Cauchy data are ill-posed, while
explicit nonlocal constraints yield well-posed codimension-one evolution.
Their Fourier construction distinguishes center, center-stable and
center-unstable data. Two-sided global center data have Fourier support in the
strict cone `|eta'|<|xi|`.

Disposition: `SOURCE-CONFIRMS` the scalar donor theorem. It does not state a
theorem for the GU matrix operator.

## Eric Weinstein source

The GU source names the multiple-time upstairs problem and the need for an
ultrahyperbolic boundary treatment as technical debt. It does not write a
selected analytic domain, a matrix polarization, a Green-compatible boundary
condition, or a BV reduction for the current real-K77 source-shaped operator.

Disposition: `SOURCE-SILENT` on
`N(k)=E(k)^2-rho(k)^2 I`, its kernel, its action/Green/BFV compatibility, and
its curved or nonlinear completion.

## Combined return

`SOURCE_CONFIRMS_ULTRAHYPERBOLIC_BOUNDARY_TECHNICAL_DEBT_AND_SCALAR_CRAIG_WEINSTEIN_NONLOCAL_REMEDY__SOURCE_CORRECTS_NONE__SOURCE_SILENT_ON_GU_MATRIX_POLARIZATION_SELECTED_ACTION_DOMAIN_GREEN_BFV_AND_NONLINEAR_PROPAGATION`
