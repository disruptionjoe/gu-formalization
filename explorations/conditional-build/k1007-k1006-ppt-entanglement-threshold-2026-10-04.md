---
title: "K1007 PPT entanglement threshold"
status: active_research
doc_type: conditional_entanglement_threshold
created: 2026-10-04
claim_ceiling: exact two-qubit PPT negativity and concurrence boundary inside K1006 only
manifest: lab/process/k1007-k1006-ppt-entanglement-threshold.json
probe: tests/channel-swings/k1007_k1006_ppt_entanglement_threshold_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1007 PPT entanglement threshold

Classification: `INTERNAL_CONDITIONAL_MATHEMATICS`.

```gu-typed-objects
result: PPT entanglement threshold negativity and concurrence for K1006
carrier: K1006 two-qubit density family LAYER=observed CHIRALITY=N/A
pairing: imported positive trace state/effect pairing ON=repository_quantum_control
real_structure: complex two-qubit Hilbert space with partial transpose on Bob
grading: Alice versus Bob tensor factors
action_owner: UNTYPED -- the noisy state remains repository selected
target: entanglement boundary MAP-TYPE=evaluation
```

The Bob partial transpose of `rho_(p,lambda)` has spectrum

```text
(1+p)/4, (1+p)/4,
(1-p+2p lambda)/4,
(1-p-2p lambda)/4.
```

For this two-qubit family, PPT is equivalent to separability. Hence

```text
entangled  iff  p(1+2 lambda)>1,
N=max(0,[p(1+2 lambda)-1]/4),
C=max(0,[p(1+2 lambda)-1]/2)=2N.
```

At `lambda=2/5`, the entanglement threshold is `p_E=5/9`. The rational
control `p=4/5` has partial-transpose minimum `-11/100`, negativity
`11/100` and concurrence `11/50`.

This supplies an exact internal state-classification boundary, not a GU-owned
physical state, Born derivation, preparation protocol or empirical score.
