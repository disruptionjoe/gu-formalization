---
title: "K1041 mass/scale nonidentifiability"
status: active_research
doc_type: conditional_dispersion_scale_nonidentifiability_theorem
created: 2026-10-04
claim_ceiling: exact scale symmetry for the K77 two-mode candidate dispersion; no GU action no-go or empirical score
manifest: lab/process/k1041-k1040-mass-scale-nonidentifiability.json
probe: tests/channel-swings/k1041_k1040_mass_scale_nonidentifiability_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1041 mass/scale nonidentifiability

Classification: `INTERNAL_CONDITIONAL_NONSELECTION`.

```gu-typed-objects
result: two-mode dispersion identifies only spatial-scale-squared divided by mass-squared, not the absolute mass coefficient
carrier: K77 positive quotient Fourier modes LAYER=observed CHIRALITY=N/A
pairing: positive K77 quotient energy ON=repository_owned_candidate_action
real_structure: real stationary wave phase space
grading: two spatial modes with eigenvalues s^2 and 4s^2
action_owner: repository-construction -- neither mass nor ruler source-selected
target: absolute mass-horn identifiability MAP-TYPE=not-a-map
```

For `omega_n^2=n^2 s^2+m^2`, the two-mode squared-frequency ratio is

```text
Q(m^2,s^2) = (4s^2+m^2)/(s^2+m^2).
```

It obeys `Q(c m^2,c s^2)=Q(m^2,s^2)` for every positive `c`. In
particular, `(m^2,s^2)=(1,1)` and `(4,4)` both give `Q=5/2`. Thus a
dimensionless dispersion ratio cannot identify the absolute mass horn while
the spatial ruler is free. This is a route-changing obstruction: freeze one
common independently owned scale before using dispersion as a discriminator.

The deterministic producer passes `12/12`; the hostile probe rejects `12/12`
formula, symmetry, ownership and promotion mutations.

## Next condition

Freeze one common scale without fitting it to either horn and preregister
nonzero modes not used in K1037's zero-mode controls.
