---
artifact_type: construction_result
created: 2026-08-13
status: FROZEN_STATIONARY_PRODUCT_RULE_WARD_RESIDUAL_RANK115__MOVING_COMPLETION_OPEN
channels: [Build, Compose, Source, Verify]
ledger_rows: [RA-E1, RA-E3, LT-SM6]
target_claim: SC-ACT-04
source_return: SOURCE_CONFIRMS_AND_SILENT
canon_verdict_change: none
fork_assumed: none
search_space_dim: "three exact 196x91 maps: constant-parameter product rule, owned lower-order response, and effective rank-25 second-parameter-jet trace"
free_object_delta: 0
residue_touched: [RA-E1:T2_DISTANCE_ONLY, RA-E3:T2_DISTANCE_ONLY, LT-SM6:T2_DISTANCE_ONLY]
scripts:
  - tests/channel-swings/selected_k77_i2b_stationary_product_rule_ward_probe.py
---

# Selected K77 I2B stationary product-rule Ward response

## Result

Differentiating the adjoint action through the **nonzero stationary two-jet**
changes the Ward calculation substantially.

For a constant `Cl2` gauge parameter `eta`, the product-rule term

```text
delta(T_mn) = [eta, C_mn]
```

has exact Euler-response rank `91`. The complete owned lower-order I2B Hessian
on `delta T=[eta,T]` has rank `25`. Their columnwise sum—the complete frozen
constant-parameter response presently assembled—has rank `90`, with exactly
one kernel generator:

```text
eta = e12 e13.
```

The effective second-parameter-jet Lorentz-trace response from the predecessor
has rank `25` and is independent of that rank-90 image. The combined frozen
Ward-completion burden therefore has rank `115`.

## Interpretation

This is progress because the previously vague “moving Ward terms” are now
split by parameter-jet order:

- constant parameter: `91` possible generators, exactly one tangent in the
  frozen packet, leaving rank `90` for moving completion;
- symmetric second parameter jet: one independent rank-`25` Lorentz-trace
  response;
- first parameter jets: not yet assembled and remain open.

The rank `115` is not an anomaly and not a count of physical modes. A complete
gauge transformation also moves the Shiab, `Q_B`, `H_q`, observation/frame
data and, where a connection rather than its homogeneous difference is used,
the affine derivative term. Those missing responses must be added before
gauge tangency is judged.

## Exact identities

```text
rank(product-rule response)                  = 91
rank(owned lower-order response)             = 25
rank([product | lower])                      = 115
rank(product + lower)                        = 90
ker(product + lower)                         = span{e12 e13}
rank(second-parameter-jet trace)             = 25
rank([product+lower | second-jet trace])      = 115
```

The fact that `rank([product|lower])=115` while their sum has rank `90` is a
columnwise Ward cancellation statement, not image containment.

## Scope fences

- **Layer 0:** constant, first-jet and second-jet gauge parameters remain
  distinct.
- **Principal-bundle:** the distortion's homogeneous adjoint action and a
  connection's affine action remain distinct.
- **Variational/BV:** the calculation includes the stationary product rule and
  owned lower-order Hessian, but not all moving action coefficients.
- **Spencer/PDE:** no first-jet symbol, compatibility character, involutivity or
  solution germ is established.
- **Symplectic/Krein/analytic:** no phase-space quotient, positivity, domain,
  propagator, spectrum or stability follows.
- **Source:** the source confirms the connection/distortion grammar but is
  silent on these selected K77 ranks.
- **Accounting:** no ledger, residue, quotient count, datum, canon verdict or
  public posture changes.

## Next gate

Assemble the moving Shiab/`Q_B`/`H_q`/observation response separately for
constant, first-jet and second-jet gauge parameters. Require exact cancellation
of the rank-90 and rank-25 frozen residuals, retain `e12e13` as a control, and
only then compute the Spencer symbol/cohomology of the completed differential.
