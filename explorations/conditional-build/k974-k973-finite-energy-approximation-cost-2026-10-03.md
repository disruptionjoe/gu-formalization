---
title: "K974 K973 finite-energy approximation cost"
status: active_research
doc_type: conditional_approximation_cost_result
created: 2026-10-03
claim_ceiling: necessary second-moment lower bound plus one compact-band sufficient construction
manifest: lab/process/k974-k973-finite-energy-approximation-cost.json
probe: tests/channel-swings/k974_k973_finite_energy_approximation_cost_probe.py
target_claim: NONE-NOT-A-KILL
---

# K974 finite-energy approximation cost

Classification: `INTERNAL_CONDITIONAL_MATHEMATICS`.

```gu-typed-objects
result: uniform approximation to the exponential cusp requires diverging spectral second moment
carrier: positive spectral probability states with finite second moment LAYER=observed CHIRALITY=N/A
pairing: positive expectation ON=declared_measure
real_structure: characteristic-function conjugation
grading: degree-zero; no BV or gauge grading
action_owner: UNTYPED -- repository comparison, not a GU-selected energy law
target: strongest finite-energy repair to K971-K973 MAP-TYPE=evaluation
```

Suppose a characteristic function `phi` with second moment `E[omega^2]` obeys

```text
sup_t |phi(t)-exp(-a|t|)| <= eta,   0<eta<1/2.
```

The bound `1-Re phi(t)<=E[omega^2]t^2/2` follows directly from
`1-cos x<=x^2/2`; no centering step is used. Uniform error and
`1-exp(-x)>=x-x^2/2` give, at `t=2 eta/a`,

```text
E[omega^2] >= a^2(1-2 eta)/(2 eta).
```

Thus the spectral second moment must diverge at least as `1/eta` as the uniform error
vanishes. Exact exponential coherence is the singular endpoint.

The normalized Cauchy restriction to `[-Omega,Omega]` supplies a matching-order
finite-energy repair. K967 gives error at most `4a/(pi Omega)`, so
`Omega=4a/(pi eta)` suffices. The repair is symmetric, so its exact second
moment equals its variance:

```text
sigma_Omega^2=a Omega/arctan(Omega/a)-a^2.
```

For `a=1.4`, `eta=0.05`, the necessary lower is `17.64` and the explicit
repair has second moment about `30.6286`. The result proves neither the optimal
constant nor an action-selected cutoff. It quantifies the domain/resolution
budget that K975 must preserve.
