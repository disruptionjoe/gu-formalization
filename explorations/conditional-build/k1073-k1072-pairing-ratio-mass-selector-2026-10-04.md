---
title: "K1073 pairing-ratio mass selector"
status: active_research
doc_type: conditional_pairing_ratio_selector
created: 2026-10-04
claim_ceiling: exact conditional selector for the supplied modewise K77 candidate family; the required pairing is not source-owned
manifest: lab/process/k1073-k1072-pairing-ratio-mass-selector.json
probe: tests/channel-swings/k1073_k1072_pairing_ratio_mass_selector_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1073 pairing-ratio mass selector

> **GU-COMPARATOR-ROUTING — scope before inference.** This is a conditional
> candidate-action selector, not source-native GU evidence. Read
> `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: `INTERNAL_CONDITIONAL_DECISION_CERTIFICATE`.

```gu-typed-objects
result: a fixed positive quotient pairing selects at most one positive mass coefficient
carrier: one physical K77 quotient mode LAYER=observed CHIRALITY=N/A
pairing: S=c diag(lambda+u,1), c>0 ON=candidate_mode
real_structure: real phase space
grading: known spatial eigenvalue and independently fixed positive pairing
action_owner: repository-construction -- selector is conditional until the functional pairing is source/action owned
target: K1071 positive mass family MAP-TYPE=evaluation
```

K1072's positive solution cone is

```text
S = c diag(lambda+u,1),  c>0.
```

Therefore an independently fixed positive pairing selects

```text
u = S_qq/S_pp - lambda.
```

Overall positive rescaling cancels from the ratio. At a known mode there is at
most one positive coefficient compatible with the fixed pairing. The
qualification is load-bearing: constructing `S` from a previously chosen `u`,
as K1071 does, proves compatibility and not selection. Source/action ownership
must precede the inference.

The producer passes `9/9`; the hostile probe rejects `9/9` cone, formula,
scale, circularity, ownership, scope and promotion mutations.

## Next condition

Test the selector coherently across more than one spatial mode and separate
the kinetic normalization from the mass intercept.
