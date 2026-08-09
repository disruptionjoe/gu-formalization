# Source return: moving epsilon in the first-action Hessian

Date: 2026-08-09

## Located argument

The checked 2021-draft source surface defines

```text
B_omega = nabla_0 + epsilon^-1 d_0 epsilon,
T_omega = varpi - epsilon^-1 d_0 epsilon,
Phi_i(epsilon) = Ad(epsilon^-1) Phi_i^0.
```

For the right logarithmic variation `eta=epsilon^-1 delta epsilon`, the
displayed definitions give

```text
delta B = D_B eta,
delta T = -D_B eta,
delta Phi_i = [Phi_i,eta]
```

with the repository's declared commutator convention.  The source-shaped
first action contains the moving Shiab more than once after the `T` Euler
covector is differentiated, so a complete mixed derivative must differentiate
every occurrence.

## Disposition

- `SOURCE-CONFIRMS`: the primitive epsilon connection chain and the conjugated
  moving-`Phi_i`/Shiab grammar.
- `REPO-DERIVES`: the coefficientwise complete epsilon/`E_T` mixed Hessian on
  the selected real K77 carrier and its horizontal/off-slice ranks.
- `SOURCE-SILENT`: whether that finite mixed block selects the 321 tangent,
  the two `U(32,32)` halves or full `U(64,64)`, and any BV, domain or physical
  interpretation.

## Prior-art boundary

`selected-k77-common-first-action-epsilon-hessian` serialized the outer
moving-Shiab cross term and proved that it lands only in grade one.  It did
not include the lower Cartan part of `D_B eta` or the second moving-Shiab term
created when the inner first packet variation is differentiated.  The present
wave composes those missing terms rather than treating the earlier rank as the
complete epsilon Hessian.

Primary evidence locations:

- `lab/sources/gu-moving-shiab-epsilon-green-source-reinspection-2026-08-05.md`
  (draft equations 8.1, 9.2 and 9.3 and their exact source dispositions);
- `lab/sources/selected-k77-source-euler-two-to-one-source-reinspection-2026-08-09.md`
  (source-variable chain); and
- `lab/sources/transcripts/portal-special-gu-first-look-2020-04-02.md:301`
  (the conjugated invariant-form operation).
