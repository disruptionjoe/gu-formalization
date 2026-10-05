---
title: "K1131 mixed-block solvability constraint map"
status: active_research
doc_type: exact_mixed_hessian_solvability_constraint_theorem
created: 2026-10-05
claim_ceiling: exact finite-dimensional solvability theorem; no propagation or physical quotient
manifest: lab/process/k1131-mixed-block-solvability-constraint-map.json
probe: tests/channel-swings/k1131_mixed_block_solvability_constraint_map_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1131 mixed-block solvability constraint map

> **GU-COMPARATOR-ROUTING — scope before inference.** This theorem is applied
> to the source-native I1B mixed Hessian, but it does not manufacture a source
> constraint or a physical quotient. Read
> `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: `SOURCE_NATIVE_ROUTE`.

```gu-typed-objects
result: exact solvability constraint for a mixed metric-distortion Hessian
carrier: finite metric h plus distortion t symbol carrier LAYER=source-print CHIRALITY=N/A
pairing: real adjoint pairing defining C-star ON=distortion-equation-space
real_structure: finite real linear maps
grading: metric fields, distortion fields and distortion Euler rows
action_owner: source-action -- conditional theorem applied to the I1B block
target: K128 mixed Hessian MAP-TYPE=restriction
```

For a mixed Hessian

```text
H = [[0,A*],[A,C]],
```

the distortion Euler equation is `C t + A h = 0`. Let the columns of `L`
span `ker(C*)`. The finite-dimensional Fredholm alternative gives the exact
field constraint

```text
Q h = 0,                 Q = L* A.                    (1)
```

Equation (1) is necessary and sufficient for `-A h` to lie in `im(C)`.
Consequently `rank(Q) <= rank(A)`. If `C` is invertible, `L` has no columns,
`Q` has rank zero, and the distortion equation eliminates `t` without
constraining `h`. If `C` is singular, its nullity alone still says nothing
about `rank(Q)`: an exact compatible control has `Q=0`, while an equally small
singular control has `rank(Q)=1` and forces `h_2=0`.

This separates four objects that cannot be interchanged: distortion
elimination, a field constraint, a left equation identity, and a gauge
generator. Turning (1) into a field-theoretic constraint additionally requires
a smooth left-null bundle, tangential/lower-order propagation, action ownership
and one common closed domain. The producer passes `13/13`; the hostile probe
rejects `10/10` mutations.
