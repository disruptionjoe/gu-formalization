---
artifact_type: construction_result
created: 2026-08-13
status: FROZEN_PROJECTED_ADJOINT_PROLONGATION_NOT_A_COMPLETE_STATIONARY_GAUGE_DIFFERENTIAL__RANK25_WARD_COMPLETION_OPEN
channels: [Build, Compose, Source, Verify]
source_return: SOURCE-CONFIRMS_AND_SILENT
ledger_rows: [RA-E1, RA-E3, LT-SM6]
scripts:
  - tests/channel-swings/selected_k77_i2b_projected_adjoint_jet_prolongation_probe.py
target_claim: SC-ACT-04
canon_verdict_change: none
fork_assumed: none
search_space_dim: "ten symmetric observed jet blocks times the exact rank-25 projected Cl2 adjoint image; prolonged rank 250"
free_object_delta: 0
residue_touched: [RA-E1:T2_DISTANCE_ONLY, RA-E3:T2_DISTANCE_ONLY, LT-SM6:T2_DISTANCE_ONLY]
---

# Selected K77 I2B projected-adjoint jet prolongation

## Result first

The field-level rank-25 projected `Cl2` adjoint image is **not yet** the full
gauge/BV differential that may be quotiented from the local stationary
two-jet fibre.

Its exact frozen tensor-product prolongation over the ten symmetric observed
second-jet blocks has rank `250`. Only a rank-`225` subspace lies in the
homogeneous stationary Euler-symbol kernel. The remaining rank `25` is one
Lorentz-trace response:

```text
block ranks: 00:25 01:0 02:0 03:0 11:25 12:0 13:0 22:25 23:0 33:25
B11 G = B22 G = B33 G = - B00 G
rank [B_mn G] = 25
```

Thus all six mixed copies are stationary tangents, while the four diagonal
copies obey one rank-25 trace condition rather than supplying four independent
defects.

## Exact quotient bookkeeping

The complete ten-block holonomic Euler symbol is onto the 196-dimensional
field cotangent. Its homogeneous kernel therefore has dimension

```text
10*196 - 196 = 1764.
```

The projected-adjoint prolongation contributes `250` directions, but only

```text
250 - rank(M restricted to G_prolonged) = 250 - 25 = 225
```

are tangent to that kernel. The only currently licensed frozen-symbol quotient
is consequently

```text
1764 - 225 = 1539.
```

On the predecessor's `(00)+(01)` slice, the same calculation reads
`196 - 25 = 171`: the mixed rank-25 copy is tangent and the diagonal copy is
not.

These numbers are symbol dimensions, not physical modes, particle counts,
theory residue, or a reduced phase space.

## Why the tempting quotient fails

V0.229 built the exact **field-level projected adjoint image** of the selected
distortion cell. This wave intentionally tests the naive prolongation obtained
by placing one independent copy in each symmetric second-jet block. A genuine
jet prolongation of the source gauge action must also contain the product-rule
terms involving gauge-parameter jets, the nonzero stationary connection jet,
and the moving `Q_B`, `H_q`, Shiab and observation data. At connection level,
the affine `d eta`/Maurer-Cartan contribution must be typed before identifying
the distortion-only adjoint action with the complete BV generator.

A genuine gauge orbit through a full stationary configuration must be tangent
to the complete linearized Euler equation. The nonzero rank-25 response is
therefore a **Ward-completion diagnostic**. It does not prove a gauge anomaly,
and it does not make those 25 directions physical.

## Structure fingerprint and variational altitude

- **Carrier:** selected real-K77, 196-real `Omega1(Cl1)` distortion bank.
- **Field map:** the exact `196 x 91` projected `Cl2` adjoint map, rank `25`;
  its 66-parameter reducibility is removed by choosing 25 pivot fields.
- **Jet carrier:** `Sym^2(R^4)^* tensor im(G)`, real rank `250`.
- **Pairing/action:** frozen selected `SC-ACT-04` residual-square principal
  Euler symbol with the inherited trace-`H_q` fixture.
- **Altitude:** stationary principal-symbol tangent/intersection only.
- **Globalization:** one local frozen frame; no atlas, associated-bundle,
  observation, or global domain descent.
- **Commuting square tested:** frozen prolonged projected-adjoint image into
  the stationary Euler symbol. Status: `FAILED` by exact rank `25`.

## Hostile fences

- **Layer 0:** projected adjoint, full inhomogeneous connection gauge action,
  and complete BV differential remain distinct.
- **Spencer/PDE:** this is the first symbol intersection, not formal
  integrability, involutivity, constraint propagation, or a solution germ.
- **Variational/BV:** only tangent gauge directions may be quotiented. The
  non-tangent complement is a missing-completion burden.
- **Symplectic:** `1539` is not a presymplectic or BFV quotient dimension.
- **Krein/analytic:** no positivity, hyperbolicity, domain, spectrum, mass, or
  stability follows from these ranks.
- **Source:** Weinstein supplies the inhomogeneous/titled connection grammar,
  but not this selected K77 prolongation or its rank pattern.
- **Accounting:** no ledger row, residue, scoped quotient, P1/P2/P3, canon
  verdict, or public posture moves.

## Validation

- Exact probe: `49/49 PASS` under pinned SymPy `1.14.0` and NumPy `2.5.1`.
- The local stationary/Bianchi predecessor replays inside the probe.
- Exact real-K77 phase and Clifford-grade checks pass.
- Invalid all-250 quotient and four-independent-diagonal readings fire planted
  failures.

## Next gate

Construct the **actual stationary-jet gauge/BV differential**: prolong the
source action through the nonzero connection two-jet with all product-rule
terms, moving `Q_B`, `H_q`, Shiab and observation coefficients, and the
inhomogeneous connection contribution where the connection rather than its
homogeneous difference is varied. Require its image to lie in the complete
linearized Euler kernel. Then run the first Spencer compatibility/involutivity
test and only afterward form a physical-carrier quotient.
