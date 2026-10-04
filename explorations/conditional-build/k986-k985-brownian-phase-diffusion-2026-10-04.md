---
title: "K986 K985 Brownian phase diffusion"
status: active_research
doc_type: conditional_stochastic_unravelling_result
created: 2026-10-04
claim_ceiling: exact imported Brownian unraveling only
manifest: lab/process/k986-k985-brownian-phase-diffusion.json
probe: tests/channel-swings/k986_k985_brownian_phase_diffusion_probe.py
target_claim: NONE-NOT-A-KILL
---

# K986 Brownian phase diffusion

Classification: `INTERNAL_CONDITIONAL_MATHEMATICS`.

```gu-typed-objects
result: exact continuous-path random-unitary realization of the K956 dephasing semigroup
carrier: supplied qubit plus classical Brownian sample space LAYER=observed CHIRALITY=N/A
pairing: imported positive qubit trace pairing and Gaussian expectation ON=repository_stochastic_model
real_structure: computational-basis conjugation plus real Brownian phase
grading: degree-zero ensemble channel
action_owner: UNTYPED -- no GU action owns the Brownian clock or white-noise limit
target: non-jump microscopic horn for the K956 reduced law MAP-TYPE=evaluation
```

Let `W_t` be standard Brownian motion and set

```text
X_t = sqrt(gamma) W_t,
U_t = exp(-i X_t Z).
```

The off-diagonal multiplier is

```text
E exp(-2 i X_t) = exp[-(1/2)(2 sqrt(gamma))^2 t]
                 = exp(-2 gamma t).
```

Thus the ensemble channel is exactly K956's dephasing semigroup. Brownian
increments are stationary and independent, paths are continuous almost surely,
and local nonselective evolution preserves every remote marginal.

This is not a GU action or a derived white-noise limit. The Brownian clock,
Gaussian probability law, positive pairing and record interpretation are all
supplied. The construction exists to test microscopic identifiability, not to
claim physical ownership.
