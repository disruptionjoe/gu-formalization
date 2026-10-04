---
title: "K1022 pair-source min-entropy boundary"
status: active_research
doc_type: conditional_setting_entropy_boundary
created: 2026-10-04
claim_ceiling: exact CHSH local ceiling implied by a supplied pair-source conditional min-entropy bound
manifest: lab/process/k1022-k1021-setting-min-entropy-boundary.json
probe: tests/channel-swings/k1022_k1021_setting_min_entropy_boundary_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1022 pair-source min-entropy boundary

Classification: `INTERNAL_REQUIREMENT_DISPOSITION`.

```gu-typed-objects
result: exact conversion from pair-source min-entropy to minimum setting-pair mass
carrier: conditional four-symbol setting-pair source LAYER=observed CHIRALITY=N/A
pairing: maximum pair probability against deterministic local CHSH loss placement ON=repository_quantum_control
real_structure: real probability simplex
grading: exact conditional extremal theorem
action_owner: UNTYPED -- no GU randomness source or entropy certificate exists
target: setting-source loophole budget MAP-TYPE=evaluation
```

Suppose, for the feasible four-symbol range `0<=h<=2`, that the pointwise
conditional pair source satisfies `H_infinity(XY|F)>=h`, equivalently
`max_j pi_j<=2^-h`. The other three
coordinates can carry at most `3*2^-h`, hence

```text
min_j pi_j >= max(0,1-3*2^-h),
b_local <= min(1,3*2^-h).
```

Both bounds are sharp. If `2^-h>=1/3`, the distribution
`(0,1/3,1/3,1/3)` is admissible and lets a deterministic local strategy put
its single CHSH loss on the absent pair, attaining win rate one. If
`2^-h<1/3`, the extremizer is
`(1-3*2^-h,2^-h,2^-h,2^-h)`.

Therefore pair-source min-entropy alone forces a nontrivial local ceiling
exactly when `h>log2(3)`. At `h=2` it forces the uniform source. This result
does not infer conditional independence from entropy, replace a device/source
separation argument, or certify any physical randomness implementation.
