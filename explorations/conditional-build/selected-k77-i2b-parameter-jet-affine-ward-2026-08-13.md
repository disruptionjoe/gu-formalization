---
artifact_type: construction_result
created: 2026-08-13
status: LOCAL_AFFINE_PARAMETER_JET_SUBCHAIN_COVARIANTIZED__OBSERVATION_BV_SPENCER_OPEN
channels: [Build, Compose, Source, Verify]
ledger_rows: [RA-E1, RA-E3, LT-SM6]
target_claim: SC-ACT-04
source_return: SOURCE_CONFIRMS_AND_SILENT
canon_verdict_change: none
fork_assumed: none
search_space_dim: "universal free-associative second covariant jet plus ten exact 196x25 selected K77 action blocks"
free_object_delta: 0
residue_touched: [RA-E1:T2_DISTANCE_ONLY, RA-E3:T2_DISTANCE_ONLY, LT-SM6:T2_DISTANCE_ONLY]
scripts:
  - tests/channel-swings/selected_k77_i2b_parameter_jet_affine_ward_probe.py
---

# Selected K77 I2B parameter-jet affine Ward completion

## Result

The predecessor's independent rank-`25` second-gauge-parameter-jet trace is
not a geometric obstruction. It is the exact defect obtained by differentiating
the distortion field with **raw** second jets while omitting the affine
connection terms required to form covariant jets.

For an adjoint-valued field `T`, connection `B`, and gauge parameter `eta`, the
ordered second covariant derivative was expanded in the free associative
algebra. The connection laws

```text
delta T = [eta,T]
delta B_mu = partial_mu eta + [eta,B_mu]
```

give exact homogeneous transformation of `D_mu D_nu T`. In particular, the
pure `partial_mu partial_nu eta` contributions are

```text
raw second field jet:       +[partial_mu partial_nu eta, T]
affine connection owner:    -[partial_mu partial_nu eta, T]
complete covariant jet:      0.
```

This sign is fixed before the action response is inspected. Porting it through
all ten exact selected K77 Hessian blocks gives

```text
rank(raw second-parameter-jet response)       = 25
rank(affine connection response)              = 25
rank(complete covariant response)             = 0.
```

All six mixed blocks remain zero. The four diagonal raw blocks retain the
single Lorentz-trace relation and cancel coefficientwise against the affine
owner. Freezing or reversing the affine owner leaves rank `25`.

## What this closes

Together with the constant-order predecessor, the local **affine connection-
jet subchain** now closes at constant and pure second-parameter-jet order:

- constant order: moving Shiab plus the co-moving curvature-source term;
- first parameter connection-jet terms: the universal covariant first/second
  derivative identity;
- pure second parameter jets: the source-owned affine connection correction.

No new field, coefficient, or external datum is introduced. This does **not**
close every first-parameter-jet term in the selected action: observation/
section contact and any independently moving coefficient owners still require
the full adapter.

## Layer-0 boundary

The affine owner belongs to the **full source connection**. Its effective
action on the 196-real distortion bank is the commutator used by the selected
K77 block, but that does not identify the two carriers. The calculation proves
a local formal covariantization theorem, not a full source-connection-to-K77
adapter, associated-bundle descent, or observation-section theorem.

## Structure fingerprint and altitude

- carrier: selected 196-real `Omega1(Cl1)` distortion bank;
- gauge image: exact rank-25 effective projected-adjoint image;
- parameter jets: one universal free-associative connection law and ten
  symmetric observed second-jet blocks;
- pairing/action: the same selected SC-ACT-04 Hessian blocks;
- real structure: trace-`H_q` selected real-K77 fixture;
- altitude: local formal Ward covariantization at a stationary two-jet;
- globalization: base-point/local only.

The commuting square “form covariant jets then transform” versus “transform
then form covariant jets” is `PROVED` universally at first and ordered second
jet. Its exact selected K77 Hessian port is `PROVED`. Full carrier descent,
nonlinear BV, Spencer involutivity, observation, symplectic and analytic
squares remain `OPEN`.

## Hostile fences

- The rank-25 disappearance is not 25 physical modes being removed.
- Formal Ward covariance is not a BV differential, cohomology, or physical
  quotient.
- No anomaly cancellation, chirality, generation, spectrum, positivity,
  hyperbolicity, boundary condition, or stability follows.
- The prior live preboundary moment map is not erased by a bulk local identity.
- No ledger, residue, quotient count, datum, canon verdict, or public posture
  changes.

## Next gate

Complete the source-connection-to-effective-distortion adapter together with
the observation/section contact response and any genuinely live coefficient
owners. Then run the first Spencer compatibility/involutivity test on that
complete covariantized stationary symbol and its local quadratic connection
witness. Only a formally compatible descended image may enter the BV and
presymplectic quotient.
