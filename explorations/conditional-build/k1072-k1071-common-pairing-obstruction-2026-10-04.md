---
title: "K1072 common-pairing obstruction"
status: active_research
doc_type: conditional_common_pairing_obstruction
created: 2026-10-04
claim_ceiling: exact two-generator linear-algebra obstruction inside the supplied K77 mode family; no global action no-go
manifest: lab/process/k1072-k1071-common-pairing-obstruction.json
probe: tests/channel-swings/k1072_k1071_common_pairing_obstruction_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1072 common-pairing obstruction

> **GU-COMPARATOR-ROUTING — scope before inference.** This is a conditional
> action-pairing theorem, not source-native GU evidence. Read
> `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: `INTERNAL_CONDITIONAL_NONSELECTION`.

```gu-typed-objects
result: one nonzero positive pairing cannot symmetrize two distinct massive-wave generators at a fixed spatial mode
carrier: one physical K77 quotient mode LAYER=observed CHIRALITY=N/A
pairing: arbitrary real symmetric S=[[a,b],[b,c]] ON=candidate_mode
real_structure: real two-dimensional phase space
grading: fixed spatial mode; two distinct positive frequency-squared parameters
action_owner: repository-construction -- no source-owned common pairing is supplied
target: coefficient-independent pairing across K1071 family MAP-TYPE=not-a-map
```

For `K_w=[[0,1],[-w,0]]`, `w=lambda+u>0`, and the full real symmetric
pairing `S=[[a,b],[b,c]]`,

```text
K_w^T S + S K_w = [[-2wb,a-wc],[a-wc,2b]].
```

Thus one generator is symmetrized exactly when `b=0` and `a=wc`. If the same
`S` symmetrizes distinct `w_1,w_2`, then `(w_1-w_2)c=0`, so `c=0`, and hence
`a=b=0`. No nonzero positive-semidefinite coefficient-independent pairing can
therefore serve two distinct masses at one fixed spatial mode.

This is not an obstruction to a pairing for one chosen coefficient; K1071
supplies one. It identifies the missing selection datum. The producer passes
`10/10`; the hostile probe rejects `10/10` formula, solution, scope and
promotion mutations.

## Next condition

Classify the positive one-generator solution cone and read the coefficient
selected by an independently fixed pairing.
