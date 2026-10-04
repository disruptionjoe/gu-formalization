---
title: "K996 K995 integer harmonic circle reconstruction"
status: active_research
doc_type: conditional_phase_reconstruction_result
created: 2026-10-04
claim_ceiling: exact circle-measure uniqueness theorem only
manifest: lab/process/k996-k995-integer-harmonic-circle-reconstruction.json
probe: tests/channel-swings/k996_k995_integer_harmonic_circle_reconstruction_probe.py
target_claim: NONE-NOT-A-KILL
---

# K996 integer-harmonic circle reconstruction

Classification: `INTERNAL_CONDITIONAL_MATHEMATICS`.

```gu-typed-objects
result: uniqueness of a supplied circular phase law from every integer Fourier coefficient
carrier: probability measures on the circle phase quotient LAYER=observed CHIRALITY=N/A
pairing: integration of continuous test functions ON=circle_probability_measure
real_structure: complex conjugation sends harmonic n to harmonic -n
grading: integer Fourier harmonic n
action_owner: UNTYPED -- no GU action owns the circle phase law or integer charge ladder
target: circular phase marginal reconstructed from all integer harmonics MAP-TYPE=evaluation
```

If two probability measures on the circle have the same coefficients
`mu_hat(n)=int exp(-in theta) dmu(theta)` for every integer `n`, they agree on
every trigonometric polynomial. Trigonometric polynomials are uniformly dense
in the continuous functions, so the measures agree. K993's finite-harmonic
counterexample is therefore sharp in the following sense: no finite set
identifies an unrestricted circle law, while the complete integer sequence
does identify the fixed-time circular marginal.

The deterministic control reconstructs an eight-point circular measure from
its complete discrete Fourier table to below `1e-14`. It tests serialization,
not the density theorem itself. The circle quotient, unbounded charge access,
positive state/effect interface and phase law remain imported. This theorem
does not identify a real-valued lift or a process generator from one time.
