---
title: "K987 K986 symmetric compound Poisson family"
status: active_research
doc_type: conditional_stochastic_family_result
created: 2026-10-04
claim_ceiling: exact imported finite-activity family only
manifest: lab/process/k987-k986-symmetric-compound-poisson-family.json
probe: tests/channel-swings/k987_k986_symmetric_compound_poisson_family_probe.py
target_claim: NONE-NOT-A-KILL
---

# K987 symmetric compound-Poisson phase family

Classification: `INTERNAL_CONDITIONAL_MATHEMATICS`.

```gu-typed-objects
result: continuum of exact finite-activity random-unitary realizations of K956
carrier: supplied qubit plus a signed compound-Poisson record LAYER=observed CHIRALITY=N/A
pairing: imported positive qubit trace pairing and classical expectation ON=repository_stochastic_model
real_structure: real signed phase increments
grading: degree-zero ensemble channel
action_owner: UNTYPED -- no GU action selects jump angle, rate or record
target: finite-activity microscopic horn family MAP-TYPE=evaluation
```

Fix `0<theta<pi` modulo the trivial zeros of `sin(theta)`. Let events arrive
with total rate

```text
lambda = gamma / sin(theta)^2
```

and give each event an independent sign `epsilon=+1` or `-1` with equal
probability. For `X_t=theta sum epsilon_j`,

```text
E exp(-2 i X_t)
  = exp(lambda t [cos(2 theta)-1])
  = exp(-2 gamma t).
```

Every angle therefore yields the same reduced semigroup. At `theta=pi/2`,
the two signed unitaries differ only by global phase and recover K981 with
`lambda=gamma`. As `theta` tends to zero, the rate diverges as
`gamma/theta^2`; this records the diffusion scaling but does not itself prove
a physical diffusion limit.

K981 is therefore one member of a continuum, not a selected stochastic horn.
The angle, rate law, clock and signed record remain imported.
