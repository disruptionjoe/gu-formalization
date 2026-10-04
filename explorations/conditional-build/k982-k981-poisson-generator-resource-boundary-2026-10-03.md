---
title: "K982 K981 Poisson generator resource boundary"
status: active_research
doc_type: conditional_poisson_generator_resource_result
created: 2026-10-03
claim_ceiling: exact generator and resource accounting for one supplied stochastic process
manifest: lab/process/k982-k981-poisson-generator-resource-boundary.json
probe: tests/channel-swings/k982_k981_poisson_generator_resource_boundary_probe.py
target_claim: NONE-NOT-A-KILL
---

# K982 Poisson generator and resource boundary

Classification: `INTERNAL_CONDITIONAL_MATHEMATICS`.

```gu-typed-objects
result: exact dephasing generator at finite event rate with imported stochastic-clock and point-jump resources
carrier: K981 system qubit and Poisson counting path LAYER=observed CHIRALITY=N/A
pairing: imported positive Hilbert pairing plus classical expectation ON=repository_stochastic_model
real_structure: computational-basis conjugation
grading: degree-zero density operators; no BV or BRST grading
action_owner: repository-construction of an imported random-unitary jump law, not a deterministic closed Hamiltonian or GU action
target: resource classification of the stochastic assumption-fork horn MAP-TYPE=evaluation
```

Over `dt`, zero or one jump occurs with probabilities `1-gamma dt+o(dt)`
and `gamma dt+o(dt)`. Hence

```text
D_dt(rho)=rho+gamma dt (Z rho Z-rho)+o(dt),
L(rho)=gamma(Z rho Z-rho).
```

The event rate is finite: on `[0,T]`, both the mean and variance of the jump
count are `gamma T`. There is no deterministic collision step `h` and no
`h^{-1/2}` coupling in this horn. K978's divergence is therefore a real cost
of its named grid construction, not a universal cost theorem for every exact
Markov realization.

The repair changes assumptions rather than removing resource debt. Exact
point jumps, the Poisson clock, ensemble probability semantics and unbounded
count support over an unbounded horizon remain imported. No finite closed
Hamiltonian parent or stochastic action is supplied.
