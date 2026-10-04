---
title: "K998 K997 invisible winding lift nonidentifiability"
status: active_research
doc_type: conditional_lift_nonidentifiability_result
created: 2026-10-04
claim_ceiling: exact invisible lattice-jump lift counterexample only
manifest: lab/process/k998-k997-invisible-winding-lift-nonidentifiability.json
probe: tests/channel-swings/k998_k997_invisible_winding_lift_nonidentifiability_probe.py
target_claim: NONE-NOT-A-KILL
---

# K998 invisible winding-lift nonidentifiability

Classification: `INTERNAL_CONDITIONAL_MATHEMATICS`.

```gu-typed-objects
result: distinct real Levy lifts with one identical circular phase process
carrier: real-valued Levy paths projected modulo 2 pi LAYER=observed CHIRALITY=N/A
pairing: characteristic-function expectation ON=repository_stochastic_model
real_structure: real phase paths with conjugate characteristic functions
grading: integer versus noninteger frequency and winding-jump count
action_owner: UNTYPED -- no GU action owns either real lift or the winding record
target: real-lift identifiability through integer-charge observations MAP-TYPE=quotient
```

Let `X_t` be any real Levy phase and let `N_t` be an independent Poisson
process. For every rate `lambda>=0`,

```text
X'_t = X_t + 2 pi N_t
```

has the same circle-valued path as `X_t`. Its exponent differs by
`lambda(exp(-i 2 pi u)-1)`, which vanishes at every integer `u`. Therefore all
integer harmonics at all times and every integer-charge system process are
identical. Yet positive rates produce distinct unwrapped terminal laws, jump
counts and quadratic variation. At `u=1/2` the exponent changes by
`-2 lambda`, so a noninteger probe would also separate the lifts if such a
probe were physically owned.

K997's circular identification result remains exact. What fails is the
stronger inference from the circular quotient to a real microscopic lift.
The family is a counterexample, not an exhaustive classification of all lifts.
