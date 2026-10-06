---
title: "K1187 radial joint-nullspace audit"
status: active_research
doc_type: corrected_auxiliary_radial_joint_nullspace_audit
created: "2026-10-05"
claim_ceiling: exact nonnull auxiliary-slice arithmetic; no native gauge ownership
manifest: lab/process/k1187-radial-joint-nullspace-audit.json
probe: tests/channel-swings/k1187_radial_joint_nullspace_audit_probe.py
target_claim: SC-ACT-06
---

# K1187 radial joint-nullspace audit

> **GU-COMPARATOR-ROUTING — scope before inference.** This composes an exact
> historical calculation only after applying K1127's ownership correction.
> Read `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: `CORRECTION_PROPAGATION`.

```gu-typed-objects
result: nonnull joint nullspace on the corrected auxiliary radial slice
carrier: K887 frozen q-lambda radial connection-only slice LAYER=source-print+toy BRIDGE=dependency_audit CHIRALITY=N/A
pairing: K887 selected Hessian restriction and raw Upsilon response restriction ON=radial_slice
real_structure: real K77 nonnull base covector
grading: auxiliary radial parameters --G--> connection tangent --(H,J)--> frozen targets
action_owner: source-action -- only the separate rank-four metric diffeomorphism image is owned at T=0
target: SC-ACT-06 MAP-TYPE=evaluation
```

K887's exact auxiliary radial carrier has dimension `16384`. On it, the raw
Upsilon response has rank zero and the selected Hessian has rank `8191`.
Therefore the stacked restriction has rank `8191`, and rank-nullity gives

```text
dim ker((H,J)|R) = 16384 - 8191 = 8193.
```

Only those `8193` directions are even eligible under K1186. The other `8191`
directions fail Hessian annihilation despite raw-response annihilation. K1127
and K1129 remain controlling: neither the full radial carrier nor its joint
nullspace is a native T=0 action-owned gauge image. The calculation is
nonnull-only and supplies no null-stratum rank. The producer passes `17/17`;
the hostile probe rejects `13/13` mutations. No protected status moves.
