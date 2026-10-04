---
title: "K1037 stationary wave generator"
status: active_research
doc_type: conditional_stationary_quotient_generator_result
created: 2026-10-04
claim_ceiling: exact modewise generator compatibility for the existing constant-coefficient K77 candidate; no nonlinear BV master equation, GU-selected generator or dissipative resource
manifest: lab/process/k1037-k1036-stationary-wave-generator.json
probe: tests/channel-swings/k1037_k1036_stationary_wave_generator_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1037 stationary wave generator

Classification: `INTERNAL_CONDITIONAL_COMPOSITION`.

```gu-typed-objects
result: the mass-one and mass-four K77 wave actions have radical-preserving energy-skew first-order generators
carrier: quotient mode coordinates (q,p) plus the ambient gauge radical LAYER=observed CHIRALITY=N/A
pairing: M_m=diag(m^2,1,0) ON=repository_owned_candidate_action
real_structure: real phase-space modes
grading: physical quotient plus null gauge representative direction
action_owner: repository-construction -- K77 quadratic candidate, not source-selected GU
target: K1034 closed-generator criterion MAP-TYPE=homomorphism
```

The zero field `Phi=0` is stationary for both K77 quadratic actions on the
ultrastatic slab. For a spatial Fourier mode with Laplacian eigenvalue
`lambda`, put `omega_m^2=lambda+m^2` and write the first-order flow as

```text
K_m = [[0,1,0],[-omega_m^2,0,0],[0,0,0]],
M_m = diag(omega_m^2,1,0).
```

The exact finite controls use the spatial zero mode for `m^2=1` and `m^2=4`.
For every nonnegative `lambda`, the gauge radical is invariant and direct
multiplication gives

```text
K_m^T M_m + M_m K_m = 0.
```

Thus the flow descends and conserves the positive quotient energy. This is
the exact K1034 compatibility identity on the existing constant-coefficient
candidate, not a source-selected GU generator. It also supplies no dissipative
CPTP dynamics, nonlinear BV master equation or interacting common domain.

The deterministic producer passes `15/15`; the hostile probe rejects `14/14`
stationarity, radical, defect, energy, scope and ownership mutations.

## Next condition

Compose the same quotient with the K77 two-copy effect interface and test
normalization plus nonselective remote-marginal invariance.
