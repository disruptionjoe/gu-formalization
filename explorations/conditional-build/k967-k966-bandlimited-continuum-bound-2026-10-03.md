---
title: "K967 K966 bandlimited continuum bound"
status: active_research
doc_type: conditional_bandlimited_continuum_result
created: 2026-10-03
claim_ceiling: uniform truncation bound for the named Cauchy spectral model only
manifest: lab/process/k967-k966-bandlimited-continuum-bound.json
probe: tests/channel-swings/k967_k966_bandlimited_continuum_bound_probe.py
target_claim: NONE-NOT-A-KILL
---

# K967 bandlimited continuum bound

```gu-typed-objects
result: uniform error bound for normalized finite-band Cauchy spectrum
carrier: system qubit tensor L2([-Omega,Omega],mu_gamma normalized) LAYER=observed CHIRALITY=N/A
pairing: positive restricted Hilbert pairing ON=repository_bandlimited_model
real_structure: complex conjugation in the spectral representation
grading: degree-zero density operators; no BV or BRST grading
action_owner: repository-construction with imported cutoff, not Weinstein source or GU action
target: finite-band approximation to K966 MAP-TYPE=evaluation
```

Restrict `mu_gamma` to `[-Omega,Omega]` and normalize. Its discarded mass is

```text
q_Omega = (2/pi) arctan(2 gamma/Omega)
        <= 4 gamma/(pi Omega).
```

Writing the full characteristic function as the convex combination of the
normalized inside and outside characteristic functions gives

```text
sup_t |f_Omega(t)-exp(-2 gamma |t|)|
  <= 2 q_Omega
  <= 8 gamma/(pi Omega).
```

The bound is uniform for all real time and includes the normalization penalty.
It proves that finite spectral bandwidth is not itself a discriminator at a
fixed tolerance. The cutoff is not source-owned, not an ultraviolet law and
not evidence for a GU reservoir.
