---
artifact_type: source_reinspection
created: 2026-08-08
status: SOURCE_CONFIRMS_CARRIERS__SOURCE_SILENT_ON_PHYSICAL_SOLDERING_IDENTITY
---

# Source reinspection: gamma-soldered source-epsilon orbit

## Return

```text
SOURCE-CONFIRMS:
  epsilon is an H-valued field in the inhomogeneous gauge data;
  T_omega=varpi-epsilon^-1 d0 epsilon;
  Phi_i(epsilon)=Ad(epsilon^-1)Phi_i^0;
  P_H is the chimeric-spinor unitary/Krein frame extension.

SOURCE-SILENT:
  the identification eta=gamma_epsilon(xi-flat) as the physical
  diffeomorphism-to-epsilon soldering law;
  the six transverse D_g Upsilon columns, complete D_epsilon Upsilon,
  residual pairing, formal adjoint, Green concomitant and physical quotient.
```

Primary checked surfaces are the 2021 draft equations 8.1 and 9.1--9.7 in
`weinstein-gu-primary-source-pack-2026-07-30.md`, plus Portal
`01:21:48--01:22:54` and `01:33:22--01:37:34` as recorded in the global K77
chimeric-spin construction.

## Layer-0 correction

Three adjacent objects must remain separate:

1. source `epsilon`, an H-valued gauge/nonlinear-sigma field;
2. `gamma_epsilon=Ad(epsilon^-1) gamma_0`, the dependent labelled Clifford
   map from the chimeric bundle into `ad(P_H)`; and
3. the new conditional tangent rule
   `eta=gamma_epsilon(xi-flat)`, which uses that map to solder a spacetime
   diffeomorphism parameter into an epsilon variation.

The source supplies the first two objects. It does not state the third
identity. The third is therefore a zero-coefficient construction hypothesis,
not a quotation or derivation from Weinstein.

Likewise, differentiating H-equivariance at `Upsilon*=0` supplies the epsilon
response on an internal gauge orbit. That derivative is not the printed
exterior-covariant prolongation `Xi=D_omega Upsilon`.

## Why this source check changes the construction

The ordinary spin/Kosmann compensator is grade two and has the same
longitudinal kernel as the spin Levi-Civita connection lift. It cannot supply
the fourth response. The source-owned chimeric frame has an additional exact
property: grade-one Clifford multiplication is B-skew and lands in
`ad(P_H)`. Thus the candidate `gamma_epsilon(xi-flat)` is admissible by type
and can be tested without adding a field or coefficient.

Source evidence licenses that test but does not establish its physical
interpretation. A pass is compatibility plus positive constraint surplus,
not recovery of Einstein gravity or a physical phase space.
