---
title: "K1181 kernel-complement rank identity"
status: active_research
doc_type: exact_kernel_complement_rank_identity
created: "2026-10-05"
claim_ceiling: exact finite-dimensional identity; no source ownership or physical quotient
manifest: lab/process/k1181-kernel-complement-rank-identity.json
probe: tests/channel-swings/k1181_kernel_complement_rank_identity_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1181 kernel-complement rank identity

For linear maps `H:V->E` and `J:V->W`, let `(H,J)` be their stacked map.
Rank-nullity gives the exact identity

```text
rank(J|ker H) = rank(H,J) - rank(H).
```

Indeed, the right side is
`dim ker(H)-dim(ker(H) intersect ker(J))`, which is precisely the rank of
`J` restricted to `ker(H)`. This is the correct complement-rank measure for a
candidate constraint or response: its full target rank receives no credit for
rows already carried by `H`.

Four sharp controls cover zero complement, full complement, zero `H`, and
invertible `H`. The producer passes its declared controls and the hostile probe
rejects `9/9` mutations. No GU object or protected status moves.
