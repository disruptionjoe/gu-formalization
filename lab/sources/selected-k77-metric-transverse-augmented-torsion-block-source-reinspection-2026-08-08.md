---
artifact_type: source_reinspection
created: 2026-08-08
status: SOURCE_CONFIRMS_AUGMENTED_TORSION_DIFFERENCE__SOURCE_SILENT_ON_COMPLETE_METRIC_RESIDUAL_OPERATOR
---

# Source reinspection: physical metric and augmented-torsion derivative

## Return

```text
SOURCE-CONFIRMS:
  varpi is the independent connection/one-form variable;
  augmented torsion is the difference between varpi and the
  epsilon-rotated Levi-Civita/reference connection;
  varying g at fixed varpi therefore contributes minus the
  Levi-Civita variation to delta T.

SOURCE-SILENT:
  the complete coefficientwise D_g Upsilon on the selected K77 background;
  the moving Shiab, Hodge, curvature, density and observation packet needed
  to close the remaining four Ward-orbit columns;
  the lower-order transverse block, K-star, adjoint and Green concomitant.
```

Primary checked surfaces are the 2021 draft equations 8.1 and 9.1--9.7 in
`weinstein-gu-primary-source-pack-2026-07-30.md`, the source-variable
reconstruction at
`selected-action-source-variable-hessian-and-diffeomorphism-lift-2026-08-06.md`,
and the gauge-rotated Levi-Civita/augmented-torsion source inspection at
`gu-pullback-augmented-torsion-source-reinspection-2026-08-05.md`.

## Layer-0 consequence

On the identity epsilon frame the principal source-variable relation is

```text
T = varpi - B_LC(g),
delta_g T |_(varpi fixed) = -delta_g B_LC.
```

This determines the direct augmented-torsion input derivative. It does not
determine every way the metric enters `Upsilon`: Shiab, Hodge, the selected
curvature/torsion constituents, density, observation and the action pairing
also move. The source gives the grammar but not the completed K77 coefficient
packet.

The exact six-transverse theorem is therefore source-derived for the direct
principal torsion block and repository-derived for its rank. The remaining
rank-four operator target is a construction burden, not a quotation.
