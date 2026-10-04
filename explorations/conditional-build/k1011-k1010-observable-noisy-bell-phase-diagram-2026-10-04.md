---
title: "K1011 observable noisy-Bell phase diagram"
status: active_research
doc_type: conditional_observable_coordinate_theorem
created: 2026-10-04
claim_ceiling: exact coordinate transformation inside the imported common-contrast two-qubit model only
manifest: lab/process/k1011-k1010-observable-noisy-bell-phase-diagram.json
probe: tests/channel-swings/k1011_k1010_observable_noisy_bell_phase_diagram_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1011 observable noisy-Bell phase diagram

Classification: `INTERNAL_REQUIREMENT_DISPOSITION`.

```gu-typed-objects
result: exact entanglement and optimized-CHSH regions in directly calibrated (p,V) coordinates
carrier: imported two-qubit density matrices rho_(p,lambda) LAYER=observed CHIRALITY=N/A
pairing: imported positive trace/Born pairing ON=repository_quantum_control
real_structure: real calibration wedge 0<=V<=p<=1
grading: entanglement versus optimized-CHSH decision regions
action_owner: UNTYPED -- neither p nor V nor the state family is GU selected
target: observable phase geometry before any empirical score MAP-TYPE=evaluation
```

K1009 gives the common-contrast interface

```text
p=<ZZ>,                    V=p lambda,
0<=lambda<=1,              0<=V<=p<=1.
```

Substituting `lambda=V/p` into K1007 and K1008 (with the `p=0` endpoint
handled directly) gives the exact observable-coordinate regions

```text
entangled             iff  p+2V>1,
optimized CHSH        iff  p^2+V^2>1,
entangled/CHSH-local  iff  p+2V>1 and p^2+V^2<=1.
```

Thus state reconstruction is unnecessary for these two decisions once the
declared two-parameter model and both calibrations are accepted. The exact
K1008 separator becomes `(p,V)=(4/5,8/25)`: its linear entanglement statistic
is `36/25`, while its Bell statistic is `464/625<1`.

This is not a model-free witness. It imports the density family, common
contrast law, positive pairing and observable meanings. GU owns none of those
objects, so no ledger, prediction, confirmation, canon or public verdict
moves.
