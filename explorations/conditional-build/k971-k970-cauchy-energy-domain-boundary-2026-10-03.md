---
title: "K971 K970 Cauchy energy-domain boundary"
status: active_research
doc_type: conditional_energy_domain_result
created: 2026-10-03
claim_ceiling: exact domain statement for the named Cauchy spectral state only
manifest: lab/process/k971-k970-cauchy-energy-domain-boundary.json
probe: tests/channel-swings/k971_k970_cauchy_energy_domain_boundary_probe.py
target_claim: NONE-NOT-A-KILL
---

# K971 Cauchy energy-domain boundary

Classification: `INTERNAL_CONDITIONAL_MATHEMATICS`.

```gu-typed-objects
result: K966's exact exponential state has divergent absolute first and second spectral moments
carrier: K966 environment L2(R,mu_a), a=2 gamma LAYER=observed CHIRALITY=N/A
pairing: positive Hilbert pairing ON=repository_continuum_model
real_structure: spectral complex conjugation
grading: degree-zero state vector; no BV or BRST grading
action_owner: UNTYPED -- repository spectral construction, not a GU action
target: physical energy and form-domain seam left explicit by K966 MAP-TYPE=evaluation
```

The normalized spectral density is

```text
d mu_a/d omega = a/[pi(omega^2+a^2)],  a=2 gamma>0.
```

For the constant unit vector, cutoff moments are exactly

```text
integral_{|omega|<=Omega} |omega| dmu_a
  = (a/pi) log(1+(Omega/a)^2),

integral_{|omega|<=Omega} omega^2 dmu_a
  = (2a/pi)[Omega-a arctan(Omega/a)].
```

Both diverge as `Omega` tends to infinity. Hence the constant vector is not in
`Dom(M_omega)` because its squared graph norm contains the second moment. It is
also not in `Dom(|M_omega|^(1/2))`, the absolute form domain, because that norm
contains the absolute first moment. The bounded spectral unitary
`exp(-itM_omega)` remains defined on the entire Hilbert space, so K966's exact
coherence theorem is unchanged; what fails is a finite-energy/domain upgrade.

This is not yet a general obstruction. It identifies the exact singular seam
of the named Cauchy realization and motivates K972's measure-independent test.
No source claim, physics-ledger row, canon result or public verdict changes.
