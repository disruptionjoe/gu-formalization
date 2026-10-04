---
title: "K1009 visibility-noise identifiability boundary"
status: active_research
doc_type: conditional_cross_anchor_identifiability
created: 2026-10-04
claim_ceiling: exact two-parameter visibility and optimized-CHSH relation only
manifest: lab/process/k1009-k1008-visibility-noise-identifiability.json
probe: tests/channel-swings/k1009_k1008_visibility_noise_identifiability_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1009 visibility-noise identifiability boundary

Classification: `INTERNAL_CONDITIONAL_MATHEMATICS`.

```gu-typed-objects
result: visibility-only nonidentifiability and one-additional-calibration reconstruction for K1006
carrier: imported Bell and two-path controls with shared p and lambda LAYER=observed CHIRALITY=N/A
pairing: imported positive state/effect and detector pairings ON=repository_quantum_control
real_structure: complex finite-dimensional Hilbert controls
grading: Bell correlation versus interference visibility readouts
action_owner: UNTYPED -- shared noise parameters are assumed rather than GU derived
target: cross-anchor calibration map MAP-TYPE=evaluation
```

If the same isotropic contrast `p` multiplies K958's phase visibility, then

```text
V=p lambda,
S_max^2/4=p^2(1+lambda^2)=p^2+V^2.
```

K1004's one-parameter relation is the special slice `p=1`. Visibility alone
no longer fixes the Bell value. At the same `V=2/5`:

```text
(p,lambda)=(1,2/5) gives S_max^2/4=29/25>1,
(p,lambda)=(1/2,4/5) gives S_max^2/4=41/100<1.
```

The longitudinal correlation supplies the missing calibration:
`<Z tensor Z>=p`. For `p>0`, the pair `(V,<ZZ>)` reconstructs
`lambda=V/p` and gives `S_max=2sqrt(p^2+V^2)`. Bell violation is then the
quarter-disk complement `p^2+V^2>1` inside `0<=V<=p<=1`.

The shared-parameter hypothesis is itself an imported experimental model. A
GU interface would have to derive or independently calibrate it; K1009 does
not turn it into a source-owned relation.
