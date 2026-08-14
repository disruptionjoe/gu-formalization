---
artifact_type: exact_jet_order_determinacy_gate
created: 2026-08-14
status: NONZERO_T_ACTION_BIANCHI_ONE_JET_ADMITTED__EPSILON_AND_TOTAL_METRIC_UNDERDETERMINED_AT_THIS_ORDER
probe: tests/channel-swings/selected_k77_nonzero_t_epsilon_jet_order_gate_probe.py
registry: lab/process/selected-k77-nonzero-t-epsilon-jet-order-gate.json
canon_verdict_change: none
---

# Selected-K77 nonzero-T epsilon jet-order gate

## Result first

The exact canonical-Zorro nonzero-`T` action/Bianchi witness is a field
**one-jet**. That data does not determine either the primitive-epsilon Euler
row or the total fixed-`varpi` metric/observation row.

The primitive identity is

```text
E_epsilon = D_B^!(E_B-E_T) + (D_epsilon S)^! K_S.
```

Even after `E_B-E_T` is evaluated, its formal adjoint contains the first
derivative of that Euler covector. Since the Euler covector already depends on
the field one-jet, this requires a compatible field two-jet. Two exact local
extensions can share the complete admitted field one-jet and give different
`D_B^!(E_B-E_T)` values. Therefore primitive-epsilon stationarity is not a
function of the presently owned witness.

The metric conclusion is independent. The direct density partial
`-t(27+728t^2)` is coprime to the branch polynomial and nonzero on both roots,
but the total fixed-`varpi` row also contains the metric derivatives of
dependent `B_Z`, moving Shiab, Hodge, frame, volume and observation. Two graph
returns on the same field one-jet can respectively preserve or exactly cancel
the direct partial. Those derivatives are not serialized in the admitted
packet, so the direct partial cannot decide total metric stationarity.

## Disposition

This is an order/type result, not a branch obstruction. Both algebraic
amplitudes remain `NOT-YET-FALSIFIED` at action/Bianchi one-jet grade. `SR-1`
remains `BACKGROUND-MISSING`; `SR-2` remains blocked.

Next construct a compatible field two-jet and the selected K77 moving
Shiab/Hodge/frame/volume/observation derivative bank. Then compute `E_B`, the
primitive-epsilon row and the total fixed-`varpi` metric row on the same
witness. Do not call missing higher-order data a zero and do not promote the
one-jet to a stationary background.

Reproduce with:

```bash
python3 tests/channel-swings/selected_k77_nonzero_t_epsilon_jet_order_gate_probe.py
```
