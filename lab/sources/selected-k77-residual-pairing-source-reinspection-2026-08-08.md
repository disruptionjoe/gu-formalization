---
artifact_type: source_reinspection
created: 2026-08-08
status: SOURCE_CONFIRMS_NORM_SQUARE_AND_ADJOINT_ARENA__SOURCE_SILENT_REAL_K77_PAIRING_SELECTION
---

# Source reinspection: selected K77 residual pairing

## Question

Does Weinstein's released material select the bilinear/Riesz map used when
the first-order residual `Upsilon` is norm-squared, or does it only direct us
to construct such a pairing?

## Primary-source loci

The official Portal/Oxford transcript, stored locally at
`lab/sources/transcripts/portal-special-gu-first-look-2020-04-02.md`, says at
`01:59:12` that the generalized Einstein equation is to be norm-squared. At
`02:00:49` Weinstein identifies the first-order portion as `Upsilon` and says
that taking its norm squared gives a new Lagrangian. At `02:01:28` he says the
resulting operator contains `d_A^*`, described as the adjoint of the Shiab
operator.

The same transcript says at `00:45:00` that indefinite signature of the
Killing form is part of the geometry and explicitly says the physical handling
of that indefiniteness is not known. Thus “norm” cannot be silently upgraded
to a positive Hilbert norm.

The 2021 source packet records `U(64,64)`-type complex notation, while the
repository's real K77 branch uses `Cl(7,7)=M(128,R)` with a real-form
comparator. The primary-source packet explicitly records that the source does
not give the real-form Krein/Riesz map, global domain, or native real-form
translation.

## Disposition

```text
SOURCE-CONFIRMS:
  - Upsilon is the first-order residual to be norm-squared;
  - an adjoint of the Shiab-derived operator is expected downstream;
  - an indefinite invariant-form problem is acknowledged.

SOURCE-SILENT:
  - the exact real K77 residual bilinear/Riesz map;
  - whether full U(64,64) adjoint invariance or only Spin(7,7) covariance
    selects that map after real-form restriction;
  - normalization beyond the already-counted source_norm coordinate;
  - a Krein fundamental symmetry, positive physical subspace, Green identity,
    boundary condition, contour, measure, or closed analytic domain.
```

The Hodge-times-Clifford-trace pairing tested in this wave is therefore a
source-directed construction. It is not a quotation or a source derivation.
Its success may close a conditional local algebraic gate only.

## Layer-0 boundary

- source “norm square” = quadratic-action instruction;
- local `K_loc` = a bundle-fibre bilinear/Riesz candidate;
- formal adjoint = integration-by-parts result after density and connection;
- Krein fundamental symmetry = a further state-space choice;
- analytic domain = boundary/regularity/evolution data.

These five objects are related and none is interchangeable with another.
