---
title: "K1104 finite-sample alias theorem"
status: active_research
doc_type: conditional_finite_sample_alias_theorem
created: 2026-10-05
claim_ceiling: constructive non-identifiability of unbounded positive auxiliary sectors from any finite exact sample set
manifest: lab/process/k1104-k1103-finite-sample-alias-theorem.json
probe: tests/channel-swings/k1104_k1103_finite_sample_alias_theorem_probe.py
target_claim: NONE-NOT-A-KILL
---

# K1104 finite-sample alias theorem

> **GU-COMPARATOR-ROUTING — scope before inference.** This is a conditional
> constructive non-identifiability theorem, not source-native GU evidence.
> Read `lab/methods/source-native-comparator-routing.md` before reuse.

Classification: `INTERNAL_CONDITIONAL_UNBOUNDED_MULTIPLICITY_ALIAS`.

```gu-typed-objects
result: any finite exact mode set admits distinct positive-weight Stieltjes aliases without a multiplicity bound
carrier: one physical plus finitely many diagonal auxiliary real modes LAYER=toy CHIRALITY=N/A
pairing: standard positive Euclidean pairing ON=conditional_block_hessian
real_structure: real symmetric diagonal auxiliary pencils
grading: physical and auxiliary blocks
action_owner: repository-construction -- no source-selected GU Hessian or multiplicity bound
target: K1103 bounded-multiplicity theorem MAP-TYPE=evaluation
```

Let `x_1,...,x_n` be any finite set of distinct nonnegative sample points,
with `n>=2`. Choose `n-1` distinct positive shifts `d_k` and form

```text
F(x)=prod_j(x-x_j)/prod_k(x+d_k).
```

Polynomial division expresses `F` as an affine function plus simple partial
fractions. Split each signed residue between two nonnegative residue lists,
then add the same strictly positive common residue at every pole. Choose two
positive affine slopes with the required difference, and add a sufficiently
large common intercept. The resulting two distinct positive-weight
affine-minus-Stieltjes branches differ by `F`, so they agree at every
prescribed sample point.

For modes `0,1,2,3`, one exact difference is

```text
F=x-12+12/(x+1)-120/(x+2)+180/(x+3).
```

Two positive-weight branches realizing it are

```text
S_L=3x+988-[1/(x+1)+121/(x+2)+1/(x+3)],
S_R=2x+1000-[13/(x+1)+1/(x+2)+181/(x+3)].
```

They agree exactly at the four modes, with common values

```text
5557/6, 11399/12, 57793/60, 58343/60,
```

while remaining distinct rational functions.

The producer passes `12/12`; the hostile probe rejects `13/13` mutations.
Thus no finite exact sample set identifies an unbounded hidden auxiliary
sector. K1103 becomes available only after a finite multiplicity bound is
independently owned. This does not assert that GU has such a sector.
