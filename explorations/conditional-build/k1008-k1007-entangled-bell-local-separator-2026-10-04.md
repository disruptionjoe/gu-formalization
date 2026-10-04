---
title: "K1008 entangled versus CHSH-local separator"
status: active_research
doc_type: conditional_entanglement_nonlocality_separator
created: 2026-10-04
claim_ceiling: exact PPT versus optimized-CHSH separation inside K1006 only
manifest: lab/process/k1008-k1007-entangled-bell-local-separator.json
probe: tests/channel-swings/k1008_k1007_entangled_bell_local_separator_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1008 entangled versus CHSH-local separator

Classification: `INTERNAL_CONDITIONAL_MATHEMATICS`.

```gu-typed-objects
result: exact separation between K1007 entanglement and optimized CHSH violation
carrier: K1006 two-qubit density family LAYER=observed CHIRALITY=N/A
pairing: imported positive trace state/effect pairing ON=repository_quantum_control
real_structure: complex two-qubit Hilbert space with Hermitian observables
grading: Alice versus Bob local algebras
action_owner: UNTYPED -- state preparation and setting optimization are imported
target: entanglement versus Bell-nonlocality thresholds MAP-TYPE=evaluation
```

K1006 has correlation tensor `p diag(lambda,-lambda,1)`. The two largest
eigenvalues of `T^T T` give

```text
S_max=2p sqrt(1+lambda^2),
CHSH violation iff p^2(1+lambda^2)>1.
```

For every `lambda>0`, the entanglement threshold
`p_E=1/(1+2lambda)` is strictly below the CHSH threshold
`p_B=1/sqrt(1+lambda^2)`, because

```text
(1+2lambda)^2-(1+lambda^2)=lambda(4+3lambda)>0.
```

The exact point `p=4/5`, `lambda=2/5` is entangled but does not violate
CHSH even after optimization:

```text
p(1+2lambda)=36/25>1,
S_max^2=1856/625<4.
```

Its K957 frozen-setting witness is also classical, with square `1568/625`.
Thus the ideal K1001 equivalence between nonzero coherence and CHSH violation
is not robust to independent isotropic contrast loss. This does not prove the
state admits a local hidden-variable model for all measurements; the result is
only the named optimized-CHSH classification.
