---
artifact_type: construction_result
created: 2026-08-12
source_claims: [SC-ACT-02, SC-ACT-04]
source_return: SOURCE_CONFIRMS_MOVING_CONJUGATED_CLIFFORD_FRAME_GRAMMAR__REPO_CORRECTS_V0204_Q12_TARGET_CLOSURE_BUG_AND_FRAME_ARTIFACT_READING__SOURCE_SILENT_ON_PPLUS_ACTION_OWNERSHIP_SPIN_LIFT_GLOBAL_CONNECTION_AND_EULER_PREBOUNDARY
verdict: POINTWISE_COMPENSATOR_NATURALITY_EXACT__V0204_Q12_EXCLUSION_RETRACTED_BY_APPEND_ONLY_CORRECTION__ACTION_OWNER_OPEN
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
fork_assumed: none
search_space_dim: 99463
free_object_delta: 0
residue_touched:
  - "RA-E1:T2_DISTANCE_ONLY"
  - "RA-E3:T2_DISTANCE_ONLY"
  - "LT-SM6:T2_DISTANCE_ONLY"
---

# Selected K77 I2B compensator naturality

## Outcome

The q13 fixed-output construction from v0.204 is not a frame artifact.  The
orientation-preserving quarter-turn in the equal-sign negative `(12,13)` plane

```text
e12 -> -e13
e13 ->  e12
```

transports the moving field `R3` exactly to `R2`.  It also intertwines every
tested tensorial layer: the K77 metric, all `16,384` exterior Hodge basis
elements, `Phi1`, `Phi2`, all `1,093` admissible source phases, the complete
`99,463`-column selected-Shiab bank, the target `H_q` involution, the rank-170
fixed-output image and the displasion target.  The transported q13 image and
the directly rebuilt q12 image are equal in both directions.

The q12 image contains its own q12 target.  V0.204 reported the opposite
because its `target_independent` helper closed over the q13 `target_vector` and
was reused for the held-out q12 bank.  The new control reproduces that old
failure by deliberately testing the q12 image against q13.  The append-only
correction is therefore exact and localized: this was a target-closure bug.

## Layer 0

These remain distinct:

1. the signed `SO(2)` tensor transport;
2. a chosen lift to the Spin bundle;
3. Weinstein's moving `epsilon`;
4. the repository's `H_q` real involution;
5. the post-composed map `P_+ A`;
6. an action-owned moving connection and its derivatives;
7. the global Euler/preboundary and physical quotient.

This wave establishes pointwise naturality of items 1, 4 and 5 under induced
Clifford transport.  It does not identify that transport with items 2 or 3,
and it does not construct items 6 or 7.

## Exact result and controls

```text
metric defects                         0
Hodge failures over 2^14 masks         0
Phi1 / Phi2 transport failures          0 / 0
source-phase transport failures         0 / 1,093
selected-Shiab failures                 0 / 99,463
target-involution failures              0 / 99,463
rank transported P_+ image              170
transported image = direct q12 image     yes, both inclusions
q13 target transported to q12 target     yes
q12 target in direct q12 image           yes
```

Three controls prevent a vacuous reading:

- q12 and q13 targets are exactly different;
- the old q12 exclusion is reproduced only when the q13 target is incorrectly
  held fixed;
- moving only `q` or fitting an arbitrary compensator is rejected as source
  `epsilon`.

## What changes and what does not

**Corrected:**

- v0.204's q12 target-exclusion result;
- the resulting classification of the q13 witness as frame-specific;
- the priority order: another pointwise coefficient/image search is no longer
  justified before action ownership and derivatives.

**Unchanged:**

- the selected Shiab itself does not intertwine the operative real structures;
- the unmodified selected-Shiab image excludes the target;
- `P_+` is a different post-composed map and is not source-owned;
- the source epsilon, Spin lift, global connection, moving `dH_q`, `dHodge`,
  `dShiab`, Euler/preboundary, vacuum, spectrum, BV and analytic domain remain
  unbuilt;
- P1/P2/P3, verdict counts, residue, canon and public posture do not move.

## Next gate

Locate `P_+` in the actual source action or derive the operative real
projection from the action-owned Spin/source-epsilon lift.  Then differentiate
the complete moving family and compute the global Euler and presymplectic
preboundary classes.  The pointwise naturality theorem is now an input to that
construction, not a substitute for it.
