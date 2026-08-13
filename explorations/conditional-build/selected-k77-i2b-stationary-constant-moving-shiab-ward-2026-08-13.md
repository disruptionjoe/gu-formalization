---
artifact_type: construction_result
created: 2026-08-13
status: CONSTANT_PARAMETER_WARD_EXACT__FIRST_AND_SECOND_PARAMETER_JETS_OPEN
run_id: RUN-20260813-141118-gu-i2b-stationary-constant-moving-shiab-ward
lane: "1"
functional_channels: [BUILD, COMPOSE, SOURCE, VERIFY]
channels: [Build, Compose, Source, Verify]
ledger_rows: [RA-E1, RA-E3, LT-SM6]
target_claim: SC-ACT-04
source_return: SOURCE_CONFIRMS_AND_SILENT
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
fork_assumed: none
search_space_dim: "91 constant Cl2 generators on one exact 196-cell stationary two-jet"
free_object_delta: 0
residue_touched: [RA-E1:T2_DISTANCE_ONLY, RA-E3:T2_DISTANCE_ONLY, LT-SM6:T2_DISTANCE_ONLY]
scripts:
  - tests/channel-swings/selected_k77_i2b_stationary_constant_moving_shiab_ward_probe.py
---

# Selected K77 I2B stationary constant moving-Shiab Ward completion

## Result

The predecessor's frozen rank-90 constant-parameter Ward response is **not an
obstruction**. The source-owned moving-`Phi1/Phi2` Shiab derivative has rank
`90`, but by itself leaves an exact rank-`24` remainder. That remainder is not
an arbitrary missing field. It is exactly cancelled by the rank-`24` motion of
the curvature-source input at the stationary branch `rho=-1/3`.

For all 91 `Cl2` generators, the complete constant-order identity is

```text
frozen field/jet response
+ moving Phi/Shiab response
+ moving rho=-1/3 curvature-source input
= 0                                                  coefficientwise.
```

The last owner is independently identified before the Euler cancellation:

```text
delta_source R
  = [eta,R] - D_A R([eta,A])
  = -(1/3) Shiab([eta,A] wedge A + A wedge [eta,A]).
```

Thus the earlier rewriting of the branch residual as only `H_q=*T_q` was
value-correct but derivative-incomplete: it erased the co-motion of the two
eddy/source terms whose values cancel at `rho=-1/3`.

## Exact receipt

```text
rank(frozen constant response)                      = 90
rank(moving-Phi/Shiab Euler response)               = 90
rank(frozen + moving-Phi/Shiab)                     = 24
rank(moving curvature-source response)              = 24
rank(complete constant-parameter Ward response)     = 0
kernel of each rank-90 component                    = span{e12 e13}
rank(independent second-parameter-jet trace)         = 25
```

The moving-Shiab implementation was checked directly on all `273` stationary
source packets (`3` packets times `91` generators). Reversing its sign fails
on every live packet and leaves a nonzero Ward response. The `e12e13` column
remains zero in every response component.

## Interpretation

This closes the **constant-parameter** even Ward gate without a new datum or
field. It also corrects the owner list: moving Shiab is necessary but not
sufficient; the already-present curvature-source term must move with the
branch. Neither `Q_B` nor a separately chosen `H_q` is used to fit the answer.

The result does not touch the independent rank-25 second-parameter-jet
Lorentz trace. First parameter jets, the affine connection term where
applicable, observation/section contact, and the full BV differential remain
unassembled.

## Structure fingerprint and altitude

- carrier: selected `196`-real `Cl1` connection bank;
- gauge carrier: all `91` real-K77 `Cl2` generators;
- pairing: symmetric real part of the grade-one Hodge/Clifford scalar pairing;
- real structure: trace-`H_q` phase bank;
- selected Shiab: `(comm,symi,symi)`;
- ambient horn: conditional real `(7,7)` K77 fixture;
- altitude: exact local stationary Euler-jet covariance at constant parameter;
- globalization: base-point/local only.

The commuting square “move the inputs then apply Shiab” versus “apply Shiab
then move the output” is `PROVED` on every load-bearing stationary source
packet. The constant Euler-Ward square is also `PROVED`. First-/second-jet,
Spencer, global descent and physical reduction squares remain `OPEN`.

## Scope fences

- Ward closure is not anomaly cancellation and not a physical-mode count.
- The rank-24 source response is field/background co-motion, not 24 new
  parameters.
- No `Q_B` construction, `H_q` selection, source action completion, BV
  quotient, presymplectic reduction, domain, spectrum or stability follows.
- No ledger, residue, quotient count, datum, canon verdict or public posture
  changes.

## Next gate

Assemble first-parameter-jet and symmetric second-parameter-jet responses,
including the affine connection, observation/section and any genuinely live
`Q_B/H_q` coefficient terms. Require cancellation of the surviving rank-25
trace, retain `e12e13` as a control, and then run Spencer compatibility.
