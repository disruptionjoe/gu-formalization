---
artifact_type: source_return
created: 2026-08-12
status: SOURCE_CONFIRMS_U3_2_PATI_SALAM_INTERSECTION_AND_VARPI_HIGGS_CUSTODY__SOURCE_SILENT_ON_TRACE_Q_RADIAL_IDENTIFICATION_AND_ACTION_SELECTION
---

# Source return: moving Hq, U(3,2), SM and Higgs direction

## Return

- `SOURCE-CONFIRMS` (`SC-GRP-03`): the Standard Model is claimed in the
  intersection of the Pati-Salam maximal compact and the complex `U(3,2)`
  reduction of `Spin(6,4)`, with the special/full-unitary `U(1)` caveat.
- `SOURCE-CONFIRMS` (`SC-GRP-01`, `SC-GRP-02`): the principal connection
  parent is full `U(64,64)`, not the normal `U(3,2)` subgroup and not
  automatically two independent `U(32,32)` connections.
- `SOURCE-ASSERTS` (`SC-FER-03`, `SC-META-57`) and `SOURCE-DISAVOWS`
  (`SC-GEO-58`): gauge, Higgs-like, CKM and Yukawa functions are components of
  the ad-valued one-form `varpi`; there is no separate fundamental Higgs.
- `SOURCE-CONFIRMS` (`SC-SIG-52`): the trace sign is chosen so that the normal
  maximal compact is Pati-Salam.

The checked source does not identify the trace vector q with the weak-doublet
direction selected by a particular orthogonal `J`; does not identify a radial
coefficient in `varpi`; and does not derive a kinetic term, quartic potential,
Yukawa map or nonzero stationary amplitude for that composition.

## Disposition

```text
SOURCE-CONFIRMS:
  the U(3,2)/Pati-Salam intersection target;
  the full U(64,64) parent;
  varpi custody of Higgs-like functions.

REPO-DERIVES:
  exact 12-dimensional S(U(3)xU(2)) intersection;
  exact 16-state chiral-spin hypercharge weights;
  fixed q leaves SU(3)xU(1), dimension nine;
  q orbit plus one radial coefficient has four real doublet components.

SOURCE-SILENT:
  selection of one J from its 20-dimensional family;
  identification of the radial coefficient with a varpi cell;
  action selection, kinetic/potential/Yukawa and physical Higgs spectrum.
```

Return code:
`SOURCE_CONFIRMS_U3_2_PATI_SALAM_INTERSECTION_AND_VARPI_HIGGS_CUSTODY__SOURCE_SILENT_ON_TRACE_Q_RADIAL_IDENTIFICATION_AND_ACTION_SELECTION`.
