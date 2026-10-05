---
title: "K1107 Loewner order lower bound"
status: active_research
doc_type: conditional_loewner_order_lower_bound
created: 2026-10-05
claim_ceiling: exact auxiliary-order lower bound from finite confluent Loewner data
manifest: lab/process/k1107-k1106-loewner-order-lower-bound.json
probe: tests/channel-swings/k1107_k1106_loewner_order_lower_bound_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1107 Loewner order lower bound

> **GU-COMPARATOR-ROUTING — scope before inference.** This is a conditional
> scalar rational-function theorem, not source-native GU evidence. Read
> `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: `INTERNAL_CONDITIONAL_LOEWNER_ORDER_LOWER_BOUND`.

```gu-typed-objects
result: exact minimum auxiliary order from a positive confluent Loewner minor
carrier: one physical plus finitely many diagonal auxiliary real modes LAYER=toy CHIRALITY=N/A
pairing: standard positive Euclidean pairing ON=conditional_block_hessian
real_structure: real symmetric diagonal auxiliary pencil
grading: physical and auxiliary blocks
action_owner: repository-construction -- no source-selected GU Hessian
target: K1106 symmetric Loewner kernel MAP-TYPE=evaluation
```

K1106 turns values and first derivatives at distinct regular nodes into a
positive Gram matrix. If an `r x r` principal minor is positive, the matrix
has rank at least `r`. Because a positive-slope branch with `m` distinct poles
has rank at most `m+1`, every representation matching the same confluent data
must have

```text
m >= r-1.
```

The implication is a lower bound. It becomes an exact order statement only
when an independent owner supplies `m<=r-1`. In the K1098 fixture, the
three-node determinant is `2/2025>0`, so no zero- or one-pole positive-slope
branch can match both the values and first derivatives at all three nodes.

This does not contradict K1104. K1104 concerns value-only finite samples;
confluent derivative data are additional observations. Nor does a positive
minor cap hidden order: without an independently owned multiplicity bound,
higher-order aliases remain possible.

The producer passes `11/11`; the hostile probe rejects `11/11` mutations.
