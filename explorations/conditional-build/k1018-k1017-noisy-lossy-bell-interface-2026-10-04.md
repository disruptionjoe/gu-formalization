---
title: "K1018 noisy-lossy Bell interface"
status: active_research
doc_type: conditional_noisy_lossy_composition
created: 2026-10-04
claim_ceiling: composition inside imported noisy-state and independent-loss models
manifest: lab/process/k1018-k1017-noisy-lossy-bell-interface.json
probe: tests/channel-swings/k1018_k1017_noisy_lossy_bell_interface_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1018 noisy-lossy Bell interface

Classification: `INTERNAL_REQUIREMENT_DISPOSITION`.

```gu-typed-objects
result: exact noisy-state and detector-efficiency CHSH composition
carrier: K1011 common-contrast two-qubit state plus K1017 local loss flags LAYER=observed CHIRALITY=N/A
pairing: density-matrix correlators composed with a classical detector mixture ON=repository_quantum_control
real_structure: real calibration coordinates p,V,eta_A,eta_B
grading: conditional exact composition with no GU ownership or empirical score
action_owner: UNTYPED -- state, preparation, loss and measurement maps are imported
target: noisy-lossy Bell decision surface MAP-TYPE=evaluation
```

K1011 gives ideal optimized CHSH value `2sqrt(p^2+V^2)` and zero local
marginals. Composing K1017 yields

```text
S_loss = 2[eta_A eta_B sqrt(p^2+V^2)
             + (1-eta_A)(1-eta_B)].
```

At the frozen `p=1,V=2/5` point, equal efficiency violates only when

```text
eta > 10/(5+sqrt(29)) = 0.9629120178...
```

The much higher threshold than K1016 reflects the small ideal Bell margin,
not a new quantum effect. The formula is exact only after supplying the noisy
state, zero marginals, fixed assignment and independent setting-independent
loss. It supplies no detector calibration, locality theorem or GU quotient.
