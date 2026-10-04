---
title: "K966 K965 Cauchy continuum reservoir"
status: active_research
doc_type: conditional_continuum_reservoir_result
created: 2026-10-03
claim_ceiling: exact repository-owned continuum controlled-dephasing dilation only; no GU action or prediction
manifest: lab/process/k966-k965-cauchy-continuum-reservoir.json
probe: tests/channel-swings/k966_k965_cauchy_continuum_reservoir_probe.py
target_claim: NONE-NOT-A-KILL
---

# K966 Cauchy continuum reservoir

Classification: `INTERNAL_CONDITIONAL_MATHEMATICS`.

```gu-typed-objects
result: exact autonomous continuum dilation of exponential coherence
carrier: system qubit tensor L2(R,mu_gamma) LAYER=observed CHIRALITY=N/A
pairing: positive Hilbert pairing and system partial trace ON=repository_continuum_model
real_structure: complex conjugation on the Cauchy spectral representation
grading: degree-zero density operators; no BV or BRST grading
action_owner: repository-construction, not Weinstein source or GU action
target: continuum escape left open by K962 and demanded by K965 MAP-TYPE=evaluation
```

For `gamma>0`, let `mu_gamma` be the probability measure on `R` with

```text
d mu_gamma/d omega = (2 gamma)/(pi(omega^2+(2 gamma)^2)).
```

On `H_E=L^2(R,mu_gamma)`, the constant function `1` is a unit vector and the
multiplication operator `M_omega` is self-adjoint on its standard domain. The
controlled Hamiltonian

```text
H=|0><0| tensor 0 + |1><1| tensor M_omega
```

generates an autonomous unitary group. Tracing the environment in the vector
state `1` multiplies system coherence by the characteristic function

```text
f(t)=integral_R exp(i omega t) d mu_gamma(omega)=exp(-2 gamma |t|).
```

The constant vector need not lie in the unbounded generator's operator domain;
the spectral unitary `exp(-it M_omega)` is bounded and defined on the whole
Hilbert space. No finite-energy claim is made for that vector.

Thus an infinite positive-pairing reservoir realizes the exact exponential
law without a fresh collision tape. A local trace-preserving reduced channel
also leaves every remote marginal invariant.

This closes the mathematical continuum escape, not the GU ownership demand.
The system/environment split, Cauchy measure, rate, initial vector, trace/Born
semantics and observable interpretation are repository inputs. No source
claim chooses them.
