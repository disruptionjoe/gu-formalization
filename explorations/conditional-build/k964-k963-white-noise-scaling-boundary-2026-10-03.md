---
title: "K964 K963 white-noise scaling boundary"
status: active_research
doc_type: conditional_white_noise_scaling_boundary_result
created: 2026-10-03
claim_ceiling: exact grid law and asymptotic resource boundary for one collision realization only
manifest: lab/process/k964-k963-white-noise-scaling-boundary.json
probe: tests/channel-swings/k964_k963_white_noise_scaling_boundary_probe.py
target_claim: NONE-NOT-A-KILL
---

# K964 white-noise scaling boundary

```gu-typed-objects
result: grid-exact exponential coherence and singular rapid-refresh continuum scaling
carrier: system qubit tensor a step-indexed fresh-qubit collision family LAYER=observed CHIRALITY=N/A
pairing: imported Hilbert adjoint, ancilla state and partial trace ON=repository_collision_scaling_family
real_structure: computational-basis conjugation with complex unitary phase
grading: degree-zero density operators; no BV or BRST grading
action_owner: repository-construction with imported clock, rate and freshness, not Weinstein source or GU action
target: continuous-time microscopic resource boundary MAP-TYPE=evaluation
```

Let the collision step be `h` and choose
`lambda_h=exp(-2 gamma h)` and
`theta_h=(1/2) arccos(lambda_h)`. At every grid time `t=nh`, K963 then gives
the exact law `lambda_h^n=exp(-2 gamma t)`. The continuum limit is not a
finite-coupling, finite-resource limit:

```text
theta_h ~ sqrt(gamma h),
theta_h/h ~ sqrt(gamma/h),
fresh ancilla rate = 1/h.
```

Thus the exact Markov law is obtainable from this microscopic family only
through a singular weak-collision/rapid-refresh limit. A physical derivation
must own the continuum or thermodynamic reservoir, the state preparation or
reset mechanism, the common domain and the controlled limit. Naming `gamma`
does not supply those structures.
