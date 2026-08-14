---
artifact_type: exact_native_connection_curvature_jet_prerequisite
created: 2026-08-14
status: CURVATURE_ONLY_GATE_REPLACED_BY_LABELLED_CURVATURE_JET_AND_ZORRO_CONNECTION_PREREQUISITE__BOTH_BRANCHES_REMAIN_TYPE_MISSING
source_return: SOURCE_CONFIRMS_ZORRO_CHAIN_AND_DEPENDENT_B_EPSILON_GRAMMAR__SOURCE_SKETCHES_BUT_DOES_NOT_PRINT_THE_INDUCED_Y_CONNECTION_OR_ITS_CURVATURE_JET
lane_id: SRC-RES-COH-01
registry: lab/process/selected-k77-native-connection-curvature-jet-gate.json
canon_verdict_change: none
ledger_row_changes: none
---

# Selected K77 native-connection curvature-jet gate

## Result first

The proposed one-step “curvature-orbit test” is necessary but not sufficient
to decide whether either exact frozen tautological branch is the source-owned
dependent connection `B(epsilon)` on native `Y=Met(X)`.

For

```text
B(epsilon)=epsilon^-1 Gamma_0 epsilon+epsilon^-1 d epsilon,
```

gauge covariance transports not only curvature but its full labelled
covariant jet:

```text
F_B                 = epsilon^-1 F_Gamma0 epsilon,
D_B F_B             = epsilon^-1 D_Gamma0 F_Gamma0 epsilon,
(D_B)^r F_B         = epsilon^-1 (D_Gamma0)^r F_Gamma0 epsilon.
```

A pointwise curvature-orbit match can therefore be only the first necessary
test.  The exact planted control gives two connections with the same curvature
at one point and different first curvature jets.  They cannot be identified
by that pointwise match.

The source-facing Zorro chain is presently a sketch: repository source
inspection confirms the metric-to-Levi-Civita-to-induced-`Y` construction but
also records that the induced `Y` metric and connection are not printed
explicitly.  Consequently there is no current source-owned `F_Gamma0` fixture,
labelled first jet or holonomy data against which either branch can be tested.
This is an exact prerequisite result, not a no-go.

## Frozen tautological branch is already first-jet sensitive

On the frozen ansatz

```text
B_i=b gamma_i,
```

the exact Clifford relations give

```text
F_ij=b^2[gamma_i,gamma_j],
D_i F_ij=4 eta_i b^3 gamma_j,
D_j F_ij=-4 eta_j b^3 gamma_i.
```

The first covariant curvature jet is therefore nonzero for every nonzero
branch scale.  Freezing `Phi1` and its moving frame did not make the jet
irrelevant; it removed precisely the coefficient responses that must be
compared with the native Zorro connection.  A native calculation must move
the labelled `Phi1`, Shiab, Hodge, density and observation packet together.

The two exact branch scales

```text
b_+ = 1/208-sqrt(3)/312,
b_- = 1/208+sqrt(3)/312
```

have distinct `b^2` and distinct nonzero quadratic curvature invariants,
which scale as `b^4`.  Thus one fixed labelled distinguished curvature orbit
at one point of `Y` cannot realize both branches.  Different moving-`Y` points
could still realize different jets, so neither branch is killed by this
separation.

## Layer 0

Keep distinct:

1. an arbitrary frozen full-unitary connection `B=b Phi1`;
2. the dependent gauge transform `B(epsilon)` of a distinguished connection;
3. the Zorro construction of that distinguished connection from metric data;
4. a pointwise curvature orbit;
5. the labelled curvature jet and its holonomy continuation; and
6. fixed-boundary bulk stationarity versus free-edge admission.

The current repository owns item 1 at exact frozen-frame grade, the general
grammar of items 2 and 3, and the gauge-covariant identities linking 4 and 5.
It does not yet own the explicit native connection needed to compare them.

## Route disposition

```text
curvature-only orbit test:                 UNDER-TYPED / RETIRED
full labelled curvature-jet necessity:     EXACT
frozen branch first jet:                   EXACT AND NONZERO
same-point realization of both branches:  KILLED
individual native branch realization:      TYPE-MISSING
global epsilon / native Y background:      NOT CONSTRUCTED
```

The next gate is now executable and unambiguous: construct the explicit Zorro
distinguished connection on the actual `Y` carrier, calculate its labelled
curvature one-jet, compare it separately with each `b_+ Phi1` and `b_- Phi1`
branch, and only then move the rest of the native geometry packet.  If neither
jet matches, the two branches are killed as GU backgrounds.  If one matches,
that branch advances to the common `K_total/L_total` carrier gate.

## Scientific ceiling

This result sharpens `SR-1B`; it does not close it.  The two branches remain
exact fixed-boundary total-residual-zero candidates and remain excluded by the
bare free-edge theorem.  No global connection, action-selected vacuum,
functional domain, SR-2 factorization, physical cohomology, W/mirror choice,
generation count, verdict, residue, quotient, datum, canon or public-posture
change follows.

## Reproduction

```sh
uv run --with sympy==1.14.0 python \
  tests/channel-swings/selected_k77_native_connection_curvature_jet_gate_probe.py
```

The exact certificate passes `36/36`.
