---
title: "K962 K961 exponential semigroup finite-parent no-go"
status: active_research
doc_type: conditional_exponential_semigroup_no_go_result
created: 2026-10-03
claim_ceiling: exact no-go for the declared finite closed controlled-dephasing parent only
manifest: lab/process/k962-k961-exponential-semigroup-no-go.json
probe: tests/channel-swings/k962_k961_exponential_semigroup_no_go_probe.py
target_claim: NONE-NOT-A-KILL
---

# K962 exponential semigroup finite-parent no-go

```gu-typed-objects
result: finite closed controlled-dephasing parent cannot equal strict positive-rate exponential decay for all nonnegative time
carrier: finite system qubit tensor finite environment Hilbert space LAYER=observed CHIRALITY=N/A
pairing: imported Hilbert adjoint and environment trace pairing ON=repository_finite_dilation
real_structure: complex conjugation in chosen finite bases
grading: degree-zero density operators; no BV or BRST grading
action_owner: repository-construction, not Weinstein source or GU action
target: exact exponential coherence law under five declared premises MAP-TYPE=not-a-map
```

For `gamma>0`, K960's candidate coherence law `lambda(t)=exp(-2 gamma t)`
tends to zero. K961's finite closed coherence factor returns arbitrarily close
to one at arbitrarily late times. The two statements are incompatible.
Therefore no fixed finite-dimensional environment, fixed environment state,
time-independent controlled-dephasing Hamiltonian and positive rate can
realize the exact exponential law for every `t>=0`.

The conclusion is premise-local. It does not exclude an infinite/continuum
environment, a fresh-ancilla tape or reset law, time-dependent driving,
non-Hamiltonian dynamics or a finite-window approximation. It also does not
falsify GU: current GU custody supplies none of the physical quotient,
environment, state/effect semantics or coupling assumed by the question.
