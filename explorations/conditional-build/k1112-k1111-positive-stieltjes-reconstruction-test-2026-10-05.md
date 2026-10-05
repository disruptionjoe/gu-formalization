---
title: "K1112 positive Stieltjes reconstruction test"
status: active_research
doc_type: conditional_positive_stieltjes_reconstruction
created: 2026-10-05
claim_ceiling: exact residue reconstruction and positive-class membership test
manifest: lab/process/k1112-k1111-positive-stieltjes-reconstruction-test.json
probe: tests/channel-swings/k1112_k1111_positive_stieltjes_reconstruction_test_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1112 positive Stieltjes reconstruction test

> **GU-COMPARATOR-ROUTING — scope before inference.** This is a conditional
> rational inverse test, not source-native GU evidence. Read
> `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: `INTERNAL_CONDITIONAL_POSITIVE_STIELTJES_RECONSTRUCTION`.

```gu-typed-objects
result: exact recovered residues and bounded-class membership decision
carrier: finite diagonal simple-pole branch LAYER=toy CHIRALITY=N/A
pairing: positive auxiliary Gram form ON=conditional_block_hessian
real_structure: real diagonal simple-pole pencil
grading: physical and auxiliary blocks
action_owner: repository-construction -- no source-selected GU Hessian
target: K1111 shifted-Loewner inverse MAP-TYPE=evaluation
```

After K1111 recovers distinct positive shifts, solve

```text
alpha*x_j+beta-S(x_j)=sum_i w_i/(x_j+d_i)
```

as an exact Cauchy system. For the K1098 fixture, nodes `{0,1}` give matrix
`[[1,1/3],[1/2,1/4]]`, determinant `1/12`, correction values
`(7/3,3/2)` and residues `(1,4)`.

The specified bounded simple-pole positive class passes only when the pencil
has the owned order, every recovered shift and residue is positive, and the
reconstructed branch matches all reserved exact samples. A nonreal,
nonpositive or repeated shift, a nonpositive residue, a singular required
Cauchy system, or a nonzero reserved-sample residual rejects that class. It
does not falsify GU outside the typed bridge.

The producer passes `10/10`; the hostile probe rejects `10/10` mutations.
