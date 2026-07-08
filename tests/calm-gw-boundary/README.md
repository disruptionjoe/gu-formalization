# CALM / GW Boundary Validators

Finite gates for the CALM/Ginsparg-Wilson boundary program.

These scripts test certificate shape only. They do not prove the actual
Ginsparg-Wilson operator, discharge Nielsen-Ninomiya, or change research status.
They also do not move claim status, verdicts, or public posture.

## Running

From the repo root:

```text
python tests/calm-gw-boundary/gw_chiral_charge_calm_validator.py
```

## Current Gate

- `gw_chiral_charge_calm_validator.py` checks that a Jordan-component signed
  charge readout is monotone in product order while the scalar net charge and
  rounded integer readout are not monotone in the same finite information order.

## Boundary

This lane is a finite certificate-shape guard for the CALM/Ginsparg-Wilson
boundary program. It keeps the nonnegative Jordan components visible and marks
the scalar/rounded readouts as forgetful failures. It is not a proof of the
actual GW operator and does not change claim status, research status, verdicts,
or public posture.
