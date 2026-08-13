---
artifact_type: conditional_build_action_owner_disposition
created: 2026-08-13
run_id: RUN-20260813-190400-gu-source-natural-second-action-owner
status: SOURCE_FAITHFUL_FIXED_NATURAL_I2B_OWNER_RESOLVED__PRINTED_ENDPOINT_QB_UP_TO_NONZERO_SCALE__EACT_QU_RIVAL_SEPARATE
lane: "1"
functional_channels: [BUILD, COMPOSE, SOURCE, VERIFY]
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
ledger_rows: [RA-E1, RA-E3, LT-SM6]
---

# Source-natural fixed-grade I2B owner disposition

## Bottom line

At the selected local real-K77 grade-one branch, the source-faithful fixed
natural second-action owner is no longer ambiguous:

```text
I2B = 1/2 <Upsilon_print, Q_B Upsilon_print>,
Q_B = c Q_trace/Hodge,   c != 0.
```

The source literally owns the printed-endpoint residual square. The exact
invariant-pairing classification separately proves that both source-supported
parent readings restrict fixed natural `Q_B` to the same one-dimensional
trace/Hodge line on the live grade-one residual. The previously computed
endpoint Hessian therefore represents the source-natural fixed-grade I2B
operator up to an overall nonzero scale.

That scale changes neither Euler zero sets nor ranks. The fixed endpoint
Hessian remains rank `196`, its compatibility family remains rank `56`, and
the already-certified stationary affine/Spencer intersection remains
nonempty. The sixteen-support rational witness and the complete second-
prolongation rank `1904/1960` are preserved.

The repository-composed `E_act/Q_u` norm square remains a separate rival. Its
selected fixed-bank principal map is zero, so endpoint formal-jet results do
not transfer to it. This disposition chooses the source-faithful operator for
the source I2B path; it does not erase the rival or claim the complete moving
GU action has been derived.

## Exact composition

Three prior results are composed without rebuilding the K77 bank:

1. `SC-ACT-04` owns the printed endpoint residual square and distinguishes it
   from the first-action Euler covector.
2. Fixed natural `Q_B` on the actual traceless grade-one residual is unique up
   to nonzero scale under both the full `U(64,64)` and two-half block readings.
3. The printed-endpoint trace/Hodge Hessian and its affine-Spencer system have
   already been computed exactly.

If `H`, `C`, and `g` are the endpoint Hessian, compatibility map, and Euler
covector, replacing the representative trace/Hodge pairing by an admissible
fixed-natural `Q_B` sends them to `cH`, `cC`, and `cg` with `c != 0`. Hence:

```text
rank(cH) = 196,
rank(cC) = 56,
ker(cC) = ker(C),
zero(cg) = zero(g).
```

The source-owned fixed-natural operator is therefore typed and decided at
this grade even though the source does not print the real-K77 normalization.

## What changes

- **Resolved:** the source-faithful fixed-natural I2B owner is the printed
  endpoint square with `Q_B` on the natural trace/Hodge line.
- **Preserved:** endpoint stationary-affine and Spencer results at their exact
  frozen local grade.
- **Preserved as a separate comparator:** the repository `E_act/Q_u` square
  and its zero selected principal owner.
- **Still open:** field-dependent or moving `Q_B`, moving metric/section/Shiab
  coefficients, the full source-unitary carrier, physical tangent/BV/BFV,
  higher nonlinear prolongation, Cartan involutivity, analytic convergence,
  global domain, positivity, spectrum and physical vacuum.

No physics-row verdict, ledger accounting, residue, quotient, canon claim,
P1/P2/P3 datum, or public posture changes.

## Next gate

On the source-faithful endpoint path, stop spending work on fixed-owner
ambiguity. Test the first genuinely moving/nonlinear coefficient prolongation
and Cartan involutivity of the covariantized endpoint system. Keep the
physical-tangent/BV graph as an independent parallel gate and do not use it as
a fitted restriction.

## Receipt

`tests/channel-swings/selected_k77_i2b_source_natural_second_action_owner_probe.py`
replays the exact Q_B and endpoint predecessors and validates the scaling,
operator separation, stationary-affine consequence, and scope fences.
