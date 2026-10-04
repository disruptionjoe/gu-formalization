---
title: "K993 K992 finite harmonic nonidentifiability"
status: active_research
doc_type: conditional_phase_law_nonidentifiability_result
created: 2026-10-04
claim_ceiling: exact finite-harmonic counterexample family only
manifest: lab/process/k993-k992-finite-harmonic-nonidentifiability.json
probe: tests/channel-swings/k993_k992_finite_harmonic_nonidentifiability_probe.py
target_claim: NONE-NOT-A-KILL
---

# K993 finite-harmonic nonidentifiability

Classification: `INTERNAL_CONDITIONAL_MATHEMATICS`.

```gu-typed-objects
result: distinct compound-Poisson phase laws identical on any prescribed finite harmonic set
carrier: arbitrary supplied finite integer charge spectrum LAYER=observed CHIRALITY=N/A
pairing: imported positive trace pairing and classical compound-Poisson expectation ON=repository_stochastic_model
real_structure: symmetric real phase-jump distributions
grading: finite observed charge-gap set S
action_owner: UNTYPED -- no GU action owns the jump measures or charge spectrum
target: general finite-probe phase-law identifiability MAP-TYPE=evaluation
```

Let `S` be any finite set of nonzero integer harmonics. Choose distinct
integers `N,M>max|S|`. Define `nu_N` as the uniform measure on the shifted
roots

```text
theta_k = 2 pi (k+1/2)/N,  k=0,...,N-1,
```

and similarly for `nu_M`. The supports contain no zero angle and are symmetric
under sign. Their Fourier moments are

```text
hat(nu_N)(r)=exp(i pi r/N) if N divides r, and 0 otherwise.
```

Hence both moments vanish for every `r` in `S`. Compound-Poisson processes
with the same total rate have identical characteristic exponents `-lambda` on
all observed harmonics, although their jump laws and microscopic records are
different.

K992's qutrit therefore gives a genuine separator for the named Brownian and
K987 pair, but no finite-dimensional charge spectrum identifies an arbitrary
microscopic phase law. This is a counterexample to full finite-probe
identification, not an exhaustive classification of all Levy processes.
