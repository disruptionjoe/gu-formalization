---
artifact_type: construction_result
created: 2026-08-08
status: SOURCE_NATIVE_PHYSICAL_WARD_CLOSED__ACTION_EULER_OPEN
canon_verdict_change: none
---

# Selected K77 source-native physical-diffeomorphism Ward closure

## Result

The exact physical four-dimensional Ward graph closes in the timelike,
spacelike and null causal classes without the conditional grade-one gamma
insertion.

The correct graph is

```text
metric / Levi-Civita:  delta_g T = -q eta,
Cartan connection:     delta varpi = q eta + [T,eta],
moving Shiab:          delta_epsilon Phi_i = [Phi_i,eta].
```

On the selected stationary branch these pieces give

```text
delta T = [T,eta],
delta F = [F,eta],
delta Upsilon = 0  when Upsilon*=0.
```

The final main exact calculation passes `52/52`; the independent Sage Clifford and
exterior-calculus route passes `19/19`.  Every complete Ward column has empty
support.

## What changed from v0.97

The rank-four defect in v0.97 combined two objects that were not the physical
graph:

1. a response operator frozen at the timelike covector `q0` was reused under
   spacelike and null labels; and
2. the dependent grade-one `gamma_epsilon` orbit was substituted for the
   source-native bivector/Kosmann compensator.

Recomputing the operator at the actual covector makes the distinction visible:

| causal class | physical Jacobian | spin/Cartan image | complete defect | frozen-`q0` defect |
|---|---:|---:|---:|---:|
| timelike | 4 | 3 | 0 | 0 |
| spacelike | 4 | 3 | 0 | 3 |
| null | 4 | 3 | 0 | 3 |

The fourth spacetime direction is not missing.  It is the symmetric
longitudinal metric direction already constructed by the physical lift.  Its
spin-connection/raw-residual image is zero, so it does not need a gamma field
to make the Ward response rank four.

## Controls with real force

- Omitting the moving-Shiab coefficient response leaves rank `3`.
- Omitting the lower Cartan commutator `[T,eta]` leaves rank `3`.
- Freezing the timelike response under spacelike or null labels leaves rank
  `3`.
- The grade-one gamma orbit is never used.

Thus the result is not a cancellation fitted after inspecting the answer.  It
uses the source coefficients and zero adjustable parameters.

## Layer 0 and scope

This closes the **dependent physical four-column diffeomorphism orbit**.  It
does not construct the arbitrary primitive field derivative
`D_epsilon Upsilon[eta]` on every epsilon variation.  That larger bank should
now be built only if the action Euler/BV calculation actually demands it.

Likewise, raw-residual `J R=0` is not yet an action-level Noether identity,
presymplectic basicness, BFV reduction, a global Green operator, an Einstein
equation, or quantum theory.

The calculation remains conditional on the Spin-native K77 parent.  The two
`U(32,32)` Weyl halves and full `U(64,64)` comparator remain distinct action
parents; this wave does not collapse them.  P1/P2/P3 remain unused.

## Source return

`SOURCE-CONFIRMS_MOVING_PHI_TWO_CONNECTION_AND_PRIMITIVE_EPSILON_GRAMMAR__SOURCE_SILENT_PHYSICAL_CARTAN_COMPOSITION`.

Weinstein supplies the moving-`Phi_i`, augmented-torsion and primitive-epsilon
grammar.  The exact physical Cartan composition above is a repository
construction, not a quotation.

## Next gate

Extend the already-built `K_loc` equation dual, formal adjoint and Green
concomitant to this physical metric--`varpi`--epsilon graph.  Then derive the
action Euler/Noether identity and presymplectic class.  Keep operator-valued
adjoints covector-valued unless a geometric field-space Riesz map is built.

## Evidence

- `tests/channel-swings/selected_k77_source_native_diffeomorphism_ward_closure_probe.py`
- `tests/channel-swings/selected_k77_source_native_diffeomorphism_ward_closure_independent.sage`
- `lab/process/selected-k77-source-native-diffeomorphism-ward-closure.json`
- `lab/process/hostile-reviews/2026-08-08-selected-k77-source-native-diffeomorphism-ward-closure-review.md`
