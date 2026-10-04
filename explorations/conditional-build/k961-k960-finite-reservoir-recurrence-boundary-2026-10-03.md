---
title: "K961 K960 finite-reservoir recurrence boundary"
status: active_research
doc_type: conditional_finite_reservoir_recurrence_result
created: 2026-10-03
claim_ceiling: finite-dimensional autonomous controlled-dephasing recurrence theorem only; no general open-system or GU no-go
manifest: lab/process/k961-k960-finite-reservoir-recurrence-boundary.json
probe: tests/channel-swings/k961_k960_finite_reservoir_recurrence_boundary_probe.py
target_claim: NONE-NOT-A-KILL
---

# K961 finite-reservoir recurrence boundary

Classification: `INTERNAL_CONDITIONAL_MATHEMATICS`.

```gu-typed-objects
result: finite autonomous controlled-dephasing coherence is a recurrent trigonometric polynomial
carrier: finite system qubit tensor finite environment Hilbert space LAYER=observed CHIRALITY=N/A
pairing: imported Hilbert adjoint and environment trace pairing ON=repository_finite_dilation
real_structure: complex conjugation in chosen finite bases
grading: degree-zero density operators; no BV or BRST grading
action_owner: repository-construction, not Weinstein source or GU action
target: microscopic owner of the K960 exponential candidate MAP-TYPE=evaluation
```

K960 imports the exponential coherence law rather than deriving its microscopic
owner. K961 asks the cheapest action-level question: can one fixed finite
environment with a time-independent Hamiltonian produce strict irreversible
dephasing for all time?

For the general finite controlled-dephasing Hamiltonian

```text
H=|0><0| tensor H0 + |1><1| tensor H1,
```

the system coherence is multiplied by

```text
f(t)=Tr(rho_E exp(i H1 t) exp(-i H0 t)).
```

Diagonalizing `H0` and `H1` separately writes `f` as a finite sum of phases
`sum_k c_k exp(-i omega_k t)`, with `sum_k c_k=f(0)=1`. Simultaneous
Diophantine approximation of the finite frequency set gives arbitrarily late
times when all phases are arbitrarily close to one. Hence `f(t)` returns
arbitrarily close to its initial value. Commutation of `H0` and `H1` is not
required.

This is a recurrence theorem for the declared finite closed parent. It does
not address infinite reservoirs, repeated fresh ancillas, reset operations,
time-dependent driving, non-Hamiltonian primitives or finite-time
approximations. Hilbert space, the trace state and the controlled interaction
remain repository-supplied rather than GU-owned.
