---
title: "K1019 loss calibration rectangle"
status: active_research
doc_type: conditional_calibration_propagation
created: 2026-10-04
claim_ceiling: exact propagation of one supplied simultaneous confidence box
manifest: lab/process/k1019-k1018-loss-calibration-rectangle.json
probe: tests/channel-swings/k1019_k1018_loss_calibration_rectangle_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1019 loss calibration rectangle

Classification: `INTERNAL_REQUIREMENT_DISPOSITION`.

```gu-typed-objects
result: exact corner propagation for noisy-state and detector confidence rectangles
carrier: simultaneous box in p,V,eta_A,eta_B LAYER=observed CHIRALITY=N/A
pairing: K1018 half-CHSH decision function ON=repository_quantum_control
real_structure: compact real four-dimensional calibration rectangle
grading: conditional confidence-event propagation; no confidence event constructed
action_owner: UNTYPED -- calibration apparatus and joint coverage are not GU owned
target: noisy-lossy certification geometry MAP-TYPE=evaluation
```

Write

```text
F(p,V,eta_A,eta_B)
 = eta_A eta_B sqrt(p^2+V^2)+(1-eta_A)(1-eta_B).
```

It is monotone in `p,V`, but it is bilinear rather than globally monotone in
the two efficiencies. Therefore a simultaneous rectangle is propagated
exactly as follows:

- at `(p_L,V_L)`, take the minimum over the four efficiency corners; certify
  CHSH only if that minimum exceeds one;
- at `(p_U,V_U)`, take the maximum over the four efficiency corners; exclude
  CHSH only if that maximum is at most one;
- otherwise report inconclusive.

This corner rule prevents a false lower-corner monotonicity argument. Exact
controls include a certifying box around `p=1,V=0.4,eta_A=eta_B=0.98` and an
excluding box around the K1012 entangled-but-CHSH-local region. The supplied
box must already have valid joint coverage and systematic allowances.
