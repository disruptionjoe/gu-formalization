---
title: "K296 Order-Seven Coalescent-Face Valuation Atlas"
document_role: active_research
operational_state: internal_structural_result
date: "2026-09-22"
claim_ceiling: "Exact one-gap and codimension-two determinant valuations for all 24 K288 occurrences; no fourth-order exterior rule or complete exterior bound."
manifest: lab/process/k296-order-seven-coalescent-face-valuation-atlas.json
producer: tests/channel-swings/k296_order_seven_coalescent_face_valuation_atlas.py
probe: tests/channel-swings/k296_order_seven_coalescent_face_valuation_atlas_probe.py
target_claim: INTERNAL_TARGET:K152_COEFFICIENT_COMPLETE_BASE_ACTION_COLUMN
target_claim_verdict: COMMON_CAUCHY_ZERO_AND_NATIVE_GAP_WEIGHT_RETAINED__COMPANION_ZERO_NOT_UNIFORM
canon_verdict_change: none
---

# K296 Order-Seven Coalescent-Face Valuation Atlas

## GU-COMPARATOR-ROUTING

This is an `INTERNAL_STRUCTURAL_ONLY` result about the repository-supplied
conditional Fock construction. It does not identify a source-selected action
or move a physics-ledger row.

```gu-typed-objects
result: exact simultaneous face valuations of the native gap product, common size-four Cauchy determinant and occurrence-specific size-three companion determinant
carrier: complete K288 order-seven size-four occurrence family on sixteen positive primitive cumulative-time increments LAYER=observed CHIRALITY=S-FULL-DIRAC
pairing: positive Hilbert Gram pairing after normalized specieswise exterior projection PAIRING-TYPE=hilbert
real_structure: CAR adjoint, momentum reflection and real Bessel K1 kernel
grading: conserved incidence charges, impurity seed, bath species, order seven, cumulative-time position and primitive face support
measure: exact K288 native measure in x,y,r,c,u,z coordinates
action_owner: repository-construction from K139, K156 and K179; no source-selected GU action or physical state is supplied
target: determine which coalescent zeros survive before absolute fourth-derivative integration MAP-TYPE=intertwiner
```

## Exact face algebra

For the common odd-position size-four determinant, the left Vandermonde is

```text
r0 r1 r2 (r0+r1) (r1+r2) (r0+r1+r2),
```

and the right factor is the same expression in `c0,c1,c2`. Thus every
one-gap projective face has one exact Cauchy zero. Together with the native
`product(r_i c_i)` density it has order two before any old-kernel derivative
is bounded. An adjacent same-side two-gap face has Cauchy order three; a
nonadjacent or mixed-side two-gap face has order two.

K296 replays all 24 K288 occurrences and evaluates their actual size-three
minors. A companion difference vanishes only when every primitive in its
support is in the scaled face. There is no companion zero on a projective
one-gap face. At codimension-two joins it appears only for minors containing
the forced even-node collision, such as `(2,4)` when `r0=r1=0` or `(4,6)`
when `r1=r2=0`.

The terminal endpoint joins are also nonuniform. When `r2=y=0`, a left
companion has a `(6,8)` zero only if it contains both nodes; the minor for old
position six omits node six and has no such zero. The right join
`c2=1-y=0` has the analogous exception.

## Decision boundary

K296 repairs K295's first loss: the true occurrence carries native-plus-Cauchy
order two at every one-gap face, not merely the native order one used in the
factorwise majorant. It does not yet repair fourth order uniformly because the
companion zero is occurrence-dependent exactly at the old-kernel endpoint
corners. K297 tests those corners. No exterior integral, action-column value,
residual or native K152 interval follows.
