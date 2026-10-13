---
title: "K1796--K1800 Full-Fisher Retained-Box Closure Wave"
status: active_research
doc_type: exploration
updated_at: "2026-10-13"
---

# K1796--K1800 full-Fisher retained-box closure wave

## Daily frontier review

The prior wave left one exact actionable frontier: 25 rational boxes from the
degree-nine full-Fisher lower cover, split as eight boxes in slab two and
seventeen in slab three. Slab one was already closed. The other major program
frontiers were not equally ready:

- quantitative Haar saving still lacks a cutoff-uniform posterior
  concentration inequality;
- the correlated-tensor route still lacks a realizable positive
  covariance-matched seed;
- a source-owned physical quotient, action and observation remain absent.

The retained-box route therefore remained the strongest ambitious safe swing.
It has exact inputs, an existing upper threshold, local whole-line Krawczyk
certificates and a clear fail-closed admission boundary.

## Resource failure repaired

K1795 reported that a raw symbolic degree-eleven Gram inversion exceeded the
measured resource budget. The obstruction was representational rather than
mathematical: the computation carried `q` as a free symbol even though this
frontier is explicitly fixed at `q=1/1024`.

Specializing `q=1/1024` before inversion reduces the odd Hermite Gram problem
to a five-dimensional exact rational matrix. Fraction-free inversion then
completes. The cross-multiplied degree-eleven threshold polynomial has 1,258
terms and canonical coefficient digest
`21310c7437582e7526b81c8fb56fdd5753812f95956bf1d648fbf5e9b1ebb21e`.

The original exact Bernstein implementation was also unnecessarily expensive
for this polynomial. A separable transform now performs:

1. exact affine substitution in `t`;
2. exact affine substitution in `z`;
3. power-to-Bernstein conversion in `t`;
4. power-to-Bernstein conversion in `z`.

All coefficients remain rational. No floating sign decision enters pruning.

## Exact degree-eleven contraction

On the 25 K1791 boxes, deterministic `t,z,t,z` subdivision gives 155 terminal
leaves. Seventy have a strictly positive Bernstein lower coefficient and 85
remain. Leaf count is not the useful measure because subdivision increases
the number of boxes. Exact area is:

- retained fraction of the K1791 frontier: `17/80`;
- newly excluded fraction of that frontier: `63/80`;
- retained fraction of the original K1771 input cover: `85/15104`;
- total excluded fraction of the original input cover: `15019/15104`.

Slab two contracts from eight input boxes to seven terminal leaves occupying
`7/128` of its K1791 frontier area, or `7/15104` of the original input-cover
area. Slab three contracts from seventeen input boxes to 78 terminal leaves
occupying `39/136` of its K1791 frontier area, or `78/15104` of the original
input-cover area.

The exact partition digest is
`0b327f8e6a74d5df3e1b24261d5bccdc24229162043494ad82aaaa7922c1d9c0`.

## Degree thirteen does not select the next method

The same fixed-cutoff repair also completed exact degree-thirteen inversion.
Its threshold polynomial has 2,385 terms. At the same split depth it retained
the same exact `17/80` area, with 85 residual leaves. That experiment is useful
method evidence but is not promoted into the admitted certificate bank:
degree escalation alone does not sharpen the geometric target at this scale.

## Admission boundary

The wave does not prove complete slab-two exclusion, complete slab-three
stationary uniqueness or a global optimizer. K1788 still isolates one local
slab-two boundary KKT point, and K1787 still isolates one local slab-three
stationary point, but 85 residual leaves remain outside those local claims.

For omission control, K1799 counts four face and four corner incidences per
retained box: 340 face incidences and 340 corner incidences. These are
conservative box-local obligations, not 340 unique geometric boundaries.
Shared internal boundaries should be deduplicated by the next local-model
engine, but every resulting geometric face and corner still needs a directed
gradient, interval-Newton or value certificate.

The next method should therefore be cancellation-aware and local, beginning
with slab two's seven leaves. Repeating coarse entrywise Hessian intervals or
increasing Hermite degree without a new local representation is not the
selected continuation.

Protected source, standing-ledger, canon, paper, prediction, confirmation and
public postures do not move. No scalar trial law becomes a source-owned
physical state or an unrestricted infimum.
