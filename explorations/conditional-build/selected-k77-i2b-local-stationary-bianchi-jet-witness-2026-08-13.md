---
artifact_type: construction_result
created: 2026-08-13
status: LOCAL_STATIONARY_CONNECTION_TWO_JET_CONSTRUCTED__BIANCHI_COMPATIBLE__AFFINE_FIBRE196__FORMAL_INTEGRABILITY_AND_PHYSICAL_QUOTIENT_OPEN
channels: [Build, Compose, Source, Verify]
ledger_rows: [RA-E1, RA-E3, LT-SM6]
target_claim: SC-ACT-04
source_return: SOURCE_CONFIRMS_I2B_CONNECTION_GRAMMAR__SOURCE_SILENT_LOCAL_STATIONARY_TWO_JET_SELECTION_AND_GLOBALIZATION__REPOSITORY_DERIVES_EXPLICIT_LOCAL_WITNESS
canon_verdict_change: none
fork_assumed: none
search_space_dim: "392 rational symmetric 00/01 connection-two-jet coordinates; rank 196; affine solution fibre dimension 196; decided wholesale at one base point"
free_object_delta: 0
residue_touched: [RA-E1:T2_DISTANCE_ONLY, RA-E3:T2_DISTANCE_ONLY, LT-SM6:T2_DISTANCE_ONLY]
---

# Selected K77 I2B local stationary Bianchi-jet witness

## Result in plain English

The previous wave showed that a genuine connection second derivative *could*
reach the selected I2B Euler equation. This wave constructs one explicitly.

An exact sparse rational solve produces a symmetric connection two-jet with
fourteen nonzero coefficients: thirteen in the `(0,0)` block and one in the
mixed `(0,1)` block, with denominators only `3` and `4`. Inserting that jet
into the selected residual-square Euler map cancels all `196` real connection
equation cells exactly. The jet is realized by the local polynomial

\[
\delta A_a^I(x)
=\tfrac12 C_{00,a}^{I}(x^0)^2+C_{01,a}^{I}x^0x^1,
\]

so its value and first derivative vanish at the base point while its symmetric
second derivative supplies the required Euler contribution. All `5,096`
componentwise linear Bianchi checks vanish there. This is therefore an actual
local connection-jet witness, not an arbitrary curvature value.

The result is real progress but not a physical solution. The map has `392`
jet variables, rank `196`, and hence a `196`-dimensional affine solution
fibre. The action has selected an equation, not a unique solution. That fibre
must now be interpreted through formal integrability, source gauge/BV
prolongation, boundary/initial data, observation and global descent; it must
not be booked as `196` new theory parameters or mistaken for an external
datum.

## Layer 0

This wave keeps four altitudes separate:

1. **Euler-image membership:** v0.236 proved the target belongs to the local
   principal image.
2. **Local Euler-stationary jet:** this wave exhibits a rational preimage and
   verifies exact cancellation at the base point.
3. **Local solution germ:** still open; it requires prolongation/formal
   integrability and the moving lower-order geometry.
4. **Physical/global solution:** still open; it additionally requires the
   actual source gauge/BV quotient, observation, boundary/domain data and
   atlas descent.

The `196`-dimensional affine fibre is solution-jet freedom at altitude 2.
It is neither a canonical choice nor automatically theory residue. Asking the
source action to choose a unique member was too strong: differential field
equations normally define solution spaces. The correct next question is which
part of this fibre survives prolongation and physical quotient.

## Exact certificate

```text
rank(B_00):                         182
rank(B_00 + symmetric B_01):        196
holonomic variables:                392
affine solution-fibre dimension:    196
witness support:                     14
  support in B_00:                   13
  support in B_01:                    1
witness denominators:               {3,4}
Euler cells after substitution:     196/196 exactly zero
linear Bianchi components:        5,096/5,096 exactly zero
```

The zero jet and a one-coefficient perturbation both fail stationarity. A
deliberately non-holonomic `(0,1)`/`(1,0)` mismatch fires the Bianchi check.

Because the polynomial is an ordinary local connection perturbation,
`F=dA+A wedge A` satisfies the connection Bianchi identity algebraically.
The certificate checks the only new second-jet content at the base point; it
does not claim that the selected Euler equation vanishes away from that point.

## Constraint accounting

Surjectivity provides existence with zero selection surplus:

\[
392\ \text{jet coordinates}-196\ \text{independent equations}
=196\ \text{affine directions}.
\]

That count is not the dimension of a physical phase space. The rank-`25`
`Cl2` source gauge distribution lives on the field carrier, not yet on this
two-jet fibre, and cannot be subtracted without constructing its jet
prolongation and the relevant BV/KT quotient. Boundary or initial conditions
may own further directions. No continuous coordinate is added to the
canonicity ledger.

## Source return

`SC-ACT-04` confirms the residual-square connection equation that owns this
test. Weinstein does not print this selected real-K77 rational jet, its affine
fibre, its formal prolongation, or its global/physical quotient.

`SOURCE-CONFIRMS` the action grammar; `SOURCE-SILENT` on the repository's
representative and the downstream realization.

## Hostile review disposition

The three-charge review returns
`SCOPED_CONSTRUCTION_SURVIVES__LOCAL_STATIONARY_BIANCHI_JET_ONLY`. It rejects:

- upgrading one stationary base-point jet to a local or global solution;
- asking the source action to canonically choose one physical history;
- treating the affine fibre as external data or a reduced phase space;
- subtracting the unprolonged rank-`25` field-level gauge image;
- inferring positivity, spectrum, mass, stability or Einstein `2/2`.

## Progress and next gate

```text
Ledger v0.236 — 82/82 mapped (100%)
32 SAME · 19 DIFFERS · 26 NEEDS · 5 OVER-DETERMINED
Residue: 84 continuous + >=19 function-valued + 9 discrete forks
Headline delta: none
Frontier: 2 named conditions closed · 1 retyped · 3 remain
```

Next prolong the actual rank-`25` `Cl2` source gauge/BV distribution to the
symmetric two-jet equation, compute its intersection and quotient with this
affine stationary fibre, and run the first Spencer/formal-integrability gate
including moving `Q_B`, `H_q` and observation jets. Only after a compatible
solution germ exists should the program attempt global descent, preboundary
data and the physical-carrier Einstein `2/2` comparison.
