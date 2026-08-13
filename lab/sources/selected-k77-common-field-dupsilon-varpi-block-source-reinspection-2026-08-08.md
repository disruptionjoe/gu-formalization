---
artifact_type: source_reinspection
created: 2026-08-08
status: SOURCE_CONFIRMS_VARPI_DIRECTION_AND_EPSILON_FIELD__SOURCE_SILENT_PHYSICAL_BLOCKS
---

# Source reinspection: the common-field D-Upsilon variables

## Return

```text
SOURCE-CONFIRMS:
  I1B is defined on inhomogeneous gauge data together with MET(X);
  T_omega=varpi-epsilon^-1 d0 epsilon;
  the displayed translation-direction variation varpi -> varpi+s alpha has
  residual Upsilon^B=odot_omega F_Aomega + * kappa_1 T_omega;
  Xi_omega=D_omega Upsilon_omega is printed as a redundant equation.

SOURCE-SILENT:
  the complete Frechet blocks D_g Upsilon and D_epsilon Upsilon;
  the active K77 residual pairing K*, formal adjoint and Green concomitant;
  coefficientwise equality with the repo's selected metric/full-II diagnostic.
```

Primary checked surface:
`lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md`, construction rows
`WGS-01`, `WGS-04`, and `WGS-06`. The existing scoped collision receipt is
`PW2F-SRC-10-VARIATION-AND-PAIRING-OWNERSHIP` in
`lab/process/pw2f-primary-source-collision-manifest.json`.

## Layer-0 correction

The letter `D` appears in two different roles that must not be collapsed:

- `D_omega Upsilon` in the printed `Xi` equation is an exterior covariant
  derivative/prolongation of the residual;
- `D_epsilon Upsilon` is a Fréchet derivative of that residual with respect to
  the group-valued source field `epsilon`.

The source explicitly prints the first and does not print the second. The
first therefore cannot be copied into the missing source-epsilon column of the
common-field Jacobian.

Likewise, the displayed `varpi+s alpha` variation owns the `varpi` direction
of the residual. It does not publish the K77 physical metric derivative of
Shiab/Hodge, the dependent observation normal jet, or the active
Krein/Riesz pairing used to form a stationary Gram Hessian.

## Construction consequence

The exact repo response can be restricted to the source-owned horizontal
`varpi` carrier now. If its diffeomorphism response has rank three while the
older metric diagnostic has rank-four Ward load, the honest alternatives are:

1. on a fixed-`epsilon` `(g,varpi)` horn, do not import that metric diagnostic
   as the common-field Gram block; or
2. construct the missing `epsilon` and physical metric blocks and show their
   complete source/action-owned cancellation.

Source language licenses the second horn as a question because `epsilon` is in
the action domain. It does not answer it.
