---
title: "K1117 rank-inertia lower bound"
status: active_research
doc_type: mixed_zero_block_rank_inertia_lower_bound
created: 2026-10-05
claim_ceiling: sharp rank-only finite-symbol inertia bound
manifest: lab/process/k1117-k1116-rank-inertia-lower-bound.json
probe: tests/channel-swings/k1117_k1116_rank_inertia_lower_bound_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1117 rank-inertia lower bound

> **GU-COMPARATOR-ROUTING — scope before inference.** This exact theorem is a
> typed linear-algebra input to the source-native route, not standalone GU
> evidence. Read `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

```gu-typed-objects
result: sharp paired inertia floor controlled by rank A
carrier: finite metric-distortion symbol space LAYER=toy CHIRALITY=N/A
pairing: self-adjoint indefinite quadratic form ON=metric_plus_distortion
real_structure: real or Hermitian finite symbol
grading: metric and distortion blocks
action_owner: repository-construction -- application inherits K128 source ownership
target: K1116 mixed-sign obstruction MAP-TYPE=evaluation
```

For `r=rank(A)`, restrict the quadratic form to the nonzero singular domain
and `ran(A)`. After rescaling by the invertible singular-value matrix, the
resulting `2r`-dimensional compression has form

```text
[[0,I],[I,C_r]] ~ [[0,I],[I,0]].
```

The congruence is the exact shift `x -> x+(1/2)C_r y`, so this compression has
inertia `(r,r,0)`. Inertia interlacing gives

```text
n_+(H) >= rank(A),   n_-(H) >= rank(A).
```

The bound is sharp: with `A=diag(2,3)` and `C=0`, the eigenvalues are
`+/-2,+/-3`, hence inertia `(2,2,0)`. Taking `C=diag(5,-1)` leaves the two
block determinants `-4,-9` and the same inertia. The theorem is finite-symbol
or form-domain structure, not a global spectral or physical-inner-product
claim.

The producer passes `9/9`; the hostile probe rejects `9/9` mutations.
