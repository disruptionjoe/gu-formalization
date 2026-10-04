---
title: "K981 K980 Poisson phase-flip unraveling"
status: active_research
doc_type: conditional_poisson_phase_flip_result
created: 2026-10-03
claim_ceiling: exact random-unitary unraveling of the imported qubit semigroup only
manifest: lab/process/k981-k980-poisson-phase-flip-unravelling.json
probe: tests/channel-swings/k981_k980_poisson_phase_flip_unravelling_probe.py
target_claim: NONE-NOT-A-KILL
---

# K981 Poisson phase-flip unraveling

Classification: `INTERNAL_CONDITIONAL_MATHEMATICS`.

```gu-typed-objects
result: exact finite-rate Poisson phase-flip unraveling of the K956 dephasing semigroup
carrier: one imported system qubit plus a classical Poisson counting path LAYER=observed CHIRALITY=N/A
pairing: imported positive Hilbert state/effect pairing and ensemble expectation ON=repository_stochastic_model
real_structure: computational-basis conjugation
grading: degree-zero density operators; no BV or BRST grading
action_owner: repository-construction with supplied stochastic clock and jumps, not Weinstein source or GU action
target: strongest time-dependent stochastic horn left open by K979 MAP-TYPE=evaluation
```

Let `N_t` be a Poisson process of rate `gamma` and evolve each sample path by

```text
U_t=Z^{N_t}.
```

Even counts act by the identity and odd counts act by `Z`. Therefore

```text
D_t(rho)=P(N_t even) rho + P(N_t odd) Z rho Z,
P(even)=(1+exp(-2 gamma t))/2,
P(odd) =(1-exp(-2 gamma t))/2.
```

The coherence factor is exactly the Poisson characteristic function
`E[(-1)^{N_t}]=exp(-2 gamma t)`. Independent increments give the semigroup
law, convex mixing gives complete positivity and trace preservation, and a
local nonselective channel preserves every remote marginal.

This is not a bounded autonomous Hamiltonian dilation. The classical random
clock, probability law and ideal point-jump rule are supplied. The result
therefore opens an explicitly typed stochastic/time-dependent horn without
constructing a GU physical quotient or action.
