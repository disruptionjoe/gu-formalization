---
title: "K1033 quotient-local no-signalling interface"
status: active_research
doc_type: conditional_quotient_local_nosignalling
created: 2026-10-04
claim_ceiling: exact finite-dimensional positive local-effect theorem on a supplied physical quotient
manifest: lab/process/k1033-k1032-quotient-local-nosignalling.json
probe: tests/channel-swings/k1033_k1032_quotient_local_nosignalling_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1033 quotient-local no-signalling interface

Classification: `INTERNAL_REQUIREMENT_DISPOSITION`.

```gu-typed-objects
result: normalized positive joint probabilities and nonselective remote-marginal invariance
carrier: supplied positive bipartite physical quotient H_A tensor H_B LAYER=toy CHIRALITY=N/A
pairing: trace pairing of a positive normalized state with complete local effects ON=repository_quantum_control
real_structure: complex Hilbert quotient with Hermitian effects
grading: exact finite-dimensional theorem with Bell-state normalization control
action_owner: UNTYPED -- state, tensor/local algebra and effects are not GU selected
target: local observable export interface MAP-TYPE=evaluation
```

On a supplied positive quotient, let `rho>=0`, `Tr(rho)=1`, and let
`{E_a^x}` and `{F_b^y}` be complete local POVMs. Then

```text
p(a,b|x,y) = Tr[rho (E_a^x tensor F_b^y)]
```

is nonnegative and normalized. Summing Alice's outcomes gives

```text
sum_a p(a,b|x,y) = Tr[rho (I tensor F_b^y)],
```

which is independent of Alice's setting. The exact Bell-state control in the
computational basis has joint table `diag(1/2,1/2)` and both marginals
`(1/2,1/2)`.

This is the algebraic remote-marginal theorem K960 required. It does not
supply spacelike locality, settings, a physical state, a tensor-factor or
commuting-algebra identification, or measured records. Those remain separate
owners under K1021--K1030.
