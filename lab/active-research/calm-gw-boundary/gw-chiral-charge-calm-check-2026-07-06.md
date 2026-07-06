---
title: "GW Chiral Charge CALM Check"
status: active_research
doc_type: certificate_packet
created: 2026-07-06
validator: tests/calm-gw-boundary/gw_chiral_charge_calm_validator.py
verdict: finite_gate_only
claim_grade: certificate_interface
---

# GW Chiral Charge CALM Check

## Scope

This packet executes the bounded second-pass request from the Nielsen protocol
pilot:

> Check whether the Ginsparg-Wilson modified axial-charge query has the right
> CALM-monotonicity shape.

This is not a theorem about the actual Ginsparg-Wilson operator, not a proof of
the CRDT/lattice-fermion functor, and not a claim-status movement. It is a finite
gate over the order-theoretic interface a future proof would need.

## Gate

The finite model separates three readouts over the same local charge atoms:

| readout | output order | gate result | meaning |
|---|---|---|---|
| Jordan-component charge `(Q_plus, Q_minus)` | product order | monotone | signed charge is coordination-free only while both nonnegative components remain visible |
| scalar net charge `Q_plus - Q_minus` | usual scalar order | non-monotone | adding a negative component can lower the readout |
| rounded integer index readout | usual integer order | non-monotone | the rounding/forgetful step can erase or reverse monotone provenance |

The test therefore supports only this certificate-interface statement:

```text
If a candidate GW axial-charge query is exposed as nonnegative Jordan
components, the component query has CALM shape. Forgetting those components to a
single signed or rounded integer readout is the non-monotone step.
```

## What This Does Not Prove

- It does not identify the actual GW kernel for GU.
- It does not prove that the true global axial charge is coordination-free.
- It does not discharge Nielsen-Ninomiya, anomaly-inflow, signed-readout, or
  non-compact analytic gates.
- It does not promote the CALM/GW analogy to canon.

## Failure Conditions

This gate should be revised or killed if a future check shows any of the
following:

- The actual GW axial-charge observable cannot be factored into nonnegative
  components without importing boundary data.
- The component order needed for monotonicity is not mathematically natural for
  the lattice-fermion algebra.
- The scalar net or rounded integer readout can be shown monotone in the same
  information order without adding a coordination or boundary step.
- The proposed CRDT/lattice-fermion functor cannot preserve the component order.

## Validator

Run from the repository root:

```text
python tests/calm-gw-boundary/gw_chiral_charge_calm_validator.py
```

Expected behavior:

- accepts the Jordan-component query over all subset inclusions in the finite
  atom set;
- rejects the scalar net query with an explicit inclusion witness;
- rejects the rounded integer readout with an explicit inclusion witness;
- confirms that both individual component projections remain monotone.

## Machine-Readable Summary

```json
{
  "packet": "gw_chiral_charge_calm_check_2026_07_06",
  "status": "active_research",
  "verdict": "finite_gate_only",
  "accepted_readout": "jordan_component_charge_product_order",
  "rejected_readouts": [
    "scalar_net_charge_usual_order",
    "rounded_integer_index_usual_order"
  ],
  "does_not_prove": [
    "actual_GW_operator_result",
    "GU_axial_charge_theorem",
    "canon_promotion",
    "claim_status_change"
  ],
  "validator": "tests/calm-gw-boundary/gw_chiral_charge_calm_validator.py"
}
```
