---
title: "K1186 joint gauge-admissibility theorem"
status: active_research
doc_type: exact_joint_gauge_admissibility_theorem
created: "2026-10-05"
claim_ceiling: exact finite-dimensional necessity; no source-owned enlarged gauge image
manifest: lab/process/k1186-joint-gauge-admissibility-theorem.json
probe: tests/channel-swings/k1186_joint_gauge_admissibility_theorem_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1186 joint gauge-admissibility theorem

> **GU-COMPARATOR-ROUTING — scope before inference.** This is a general
> finite-dimensional gate for a supplied packet. Read
> `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: `CONDITIONAL_RESULT`.

```gu-typed-objects
result: joint Hessian/response gauge-admissibility gate
carrier: supplied finite-dimensional field tangent V LAYER=toy BRIDGE=exact_linear_algebra CHIRALITY=N/A
pairing: symmetric Hessian H plus candidate response J ON=V
real_structure: real finite-dimensional controls
grading: gauge parameters --d--> fields --(H,J)--> equations+responses
action_owner: N/A -- theorem applies only after a source-owned d is supplied
target: SC-ACT-06 necessary admission gate MAP-TYPE=evaluation
```

For a current-parent packet with Hessian `H`, response or constraint `J`, and
proposed gauge differential `d`, descent requires both `Hd=0` and `Jd=0`.
Equivalently,

```text
im d subset ker H intersection ker J = ker(H,J).
```

Thus response annihilation alone cannot authenticate a gauge image. The exact
dimension ceiling is `rank d <= dim ker(H,J)`, and it is sharp: inclusion of
the full joint kernel attains equality. Four coordinate controls separately
exercise full admission, response-only failure, Hessian-only failure, and a
trivial joint kernel. The producer passes `16/16`; the hostile probe rejects
`12/12` mutations. No GU object or protected status moves.
