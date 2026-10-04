---
title: "K1002 fixed versus adaptive Bell witness"
status: active_research
doc_type: conditional_bell_measurement_protocol_separator
created: 2026-10-04
claim_ceiling: exact witness-choice separator on the imported K956 family
manifest: lab/process/k1002-k1001-fixed-versus-adaptive-bell-witness.json
probe: tests/channel-swings/k1002_k1001_fixed_versus_adaptive_bell_witness_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1002 fixed versus adaptive Bell witness

Classification: `INTERNAL_CONDITIONAL_MATHEMATICS`.

```gu-typed-objects
result: exact state at which the frozen K957 witness is local while the optimized witness still violates CHSH
carrier: K1001 imported two-qubit Bell-diagonal family at lambda=2/5 LAYER=observed CHIRALITY=N/A
pairing: imported trace expectation ON=repository_quantum_control
real_structure: complex two-qubit Hilbert space
grading: fixed versus state-adaptive measurement protocol
action_owner: UNTYPED -- no GU owner for either protocol
target: witness-death versus optimized-Bell-death distinction MAP-TYPE=evaluation
```

At the exact control `lambda=2/5`, K957's frozen settings give

```text
S_fixed^2=2(1+2/5)^2=98/25<4,
```

so that witness does not violate CHSH. K1001's adaptive settings give

```text
S_max^2=4(1+(2/5)^2)=116/25>4.
```

The state parameter and remote marginal are identical; only the chosen
measurement settings differ. This one rational point is therefore a complete
counterexample to the inference “the K957 witness stopped violating, hence the
damped state admits no Bell violation.” It does not say an apparatus can tune
those settings without cost, calibration or prior knowledge of `lambda`.
