# CALM / GW Boundary Validators

Finite gates for the CALM/Ginsparg-Wilson boundary program.

These scripts test certificate shape only. They do not prove the actual
Ginsparg-Wilson operator, discharge Nielsen-Ninomiya, or change research status.

## Running

From the repo root:

```text
python tests/calm-gw-boundary/gw_chiral_charge_calm_validator.py
```

## Current Gate

- `gw_chiral_charge_calm_validator.py` checks that a Jordan-component signed
  charge readout is monotone in product order while the scalar net charge and
  rounded integer readout are not monotone in the same finite information order.
