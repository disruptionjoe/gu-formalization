---
title: "K1074 multimode affine stiffness law"
status: active_research
doc_type: conditional_multimode_stiffness_theorem
created: 2026-10-04
claim_ceiling: exact multimode compatibility and recovery theorem for the supplied quadratic wave family; no source-owned Hessian
manifest: lab/process/k1074-k1073-multimode-affine-stiffness-law.json
probe: tests/channel-swings/k1074_k1073_multimode_affine_stiffness_law_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1074 multimode affine stiffness law

> **GU-COMPARATOR-ROUTING — scope before inference.** This is a conditional
> action-Hessian requirement, not source-native GU evidence. Read
> `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: `INTERNAL_CONDITIONAL_DECISION_CERTIFICATE`.

```gu-typed-objects
result: common kinetic normalization forces an affine stiffness law whose intercept-to-slope ratio is the mass coefficient
carrier: multiple spatial modes of the K77 positive quotient LAYER=observed CHIRALITY=N/A
pairing: S_qq(lambda)=c(lambda+u), S_pp(lambda)=c with common c>0 ON=candidate_action
real_structure: real modal phase space
grading: common-normalization family across known spatial eigenvalues
action_owner: repository-construction -- no source functional Hessian supplies slope or intercept
target: K1073 conditional selector MAP-TYPE=evaluation
```

With a common kinetic normalization `c>0`, K1073 becomes

```text
S_qq(lambda)=c(lambda+u),  S_pp(lambda)=c.
```

The stiffness is affine in `lambda`, with slope `c` and intercept `cu`.
For two distinct known modes,

```text
c = (A_2-A_1)/(lambda_2-lambda_1),
u = A_1/c-lambda_1.
```

Exact rational controls recover three supplied `(c,u)` pairs. If every mode
instead receives an unrelated kinetic scale `c_lambda`, invariance alone gives
only separate ratios and does not identify one common `u`. Common
normalization is therefore an action/Hessian requirement, not free algebra.

The producer passes `8/8`; the hostile probe rejects `8/8` affine-law,
recovery, normalization, ownership, scope and promotion mutations.

## Next condition

Supply a source/action-owned functional pairing or Hessian, verify the common
normalization and affine law, then read the intercept before apparatus scoring.
