---
title: "K1128 K896 projector commutator audit"
status: active_research
doc_type: corrected_integrability_audit
created: 2026-10-05
claim_ceiling: exact auxiliary first-order principal-symbol classification
manifest: lab/process/k1128-k896-projector-commutator-audit.json
probe: tests/channel-swings/k1128_k896_projector_commutator_audit_probe.py
target_claim: SC-ACT-06
---

# K1128 K896 projector commutator audit

> **GU-COMPARATOR-ROUTING — scope before inference.** This audits an
> auxiliary projector after the K1126 first-order correction. Read
> `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: `AUXILIARY_CONTROL`.

```gu-typed-objects
result: corrected first-order integrability test for T=A(I-P_R)
carrier: frozen radial-slice coefficient space LAYER=toy CHIRALITY=N/A
pairing: frozen Euclidean transpose pairing ON=coefficient-space
real_structure: real skew first-order coefficient
grading: exact auxiliary principal-symbol result
action_owner: repository-construction -- auxiliary projector only
target: SC-ACT-06 MAP-TYPE=evaluation
```

For `T=A(I-P_R)` with `A^T=-A` and `P_R^T=P_R`, first-order formal
self-adjointness requires `T^T=-T`. Its corrected defect is
`T+T^T=P_R A-A P_R`. The defect has exact rank `16382`, so this auxiliary
projector still fails principal integrability. The retired anticommutator test
had rank `130912`.

All first-order completions have `C=-A+Q` with `Q^T=-Q`; radial descent is
`QG=0`. K897's symmetric-`S` classification is therefore withdrawn. The
projector is not source/action owned. The producer passes `15/15`; the hostile
probe rejects `15/15` mutations. No protected status moves.
