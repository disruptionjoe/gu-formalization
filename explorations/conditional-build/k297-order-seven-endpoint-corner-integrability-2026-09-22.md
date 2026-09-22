---
title: "K297 Order-Seven Endpoint-Corner Integrability"
document_role: active_research
operational_state: internal_structural_result
date: "2026-09-22"
claim_ceiling: "Exact occurrencewise endpoint-corner integrability through derivative order four; no divergence theorem for the complete coherent sum or true integrand."
manifest: lab/process/k297-order-seven-endpoint-corner-integrability.json
producer: tests/channel-swings/k297_order_seven_endpoint_corner_integrability.py
probe: tests/channel-swings/k297_order_seven_endpoint_corner_integrability_probe.py
target_claim: INTERNAL_TARGET:K152_COEFFICIENT_COMPLETE_BASE_ACTION_COLUMN
target_claim_verdict: OCCURRENCEWISE_FOURTH_ORDER_RULE_FAILS_ONLY_AT_TERMINAL_OLD_POSITION__ORDERED_COHERENT_SUM_REQUIRED
canon_verdict_change: none
---

# K297 Order-Seven Endpoint-Corner Integrability

## GU-COMPARATOR-ROUTING

This is an `INTERNAL_STRUCTURAL_ONLY` result about the repository-supplied
conditional Fock construction. It does not identify a source-selected action
or move a physics-ledger row.

```gu-typed-objects
result: exact endpoint-corner homogeneity and absolute-integrability classification for each old position through shape-derivative order four
carrier: all 24 K288 size-four occurrences with the K296 determinant valuations retained LAYER=observed CHIRALITY=S-FULL-DIRAC
pairing: positive Hilbert Gram pairing before coherent signed group composition PAIRING-TYPE=hilbert
real_structure: CAR adjoint, momentum reflection and real Bessel K1 kernel
grading: conserved incidence charges, impurity seed, bath species, order seven, old position and endpoint-corner support
measure: native projective gap weight with y or 1-y paired to its old-position Bessel kernel
action_owner: repository-construction from K139, K156 and K179; no source-selected GU action or physical state is supplied
target: decide whether occurrencewise fourth-order bounds can be integrated over the K294 angular exterior MAP-TYPE=intertwiner
```

## Corner calculation

For old positions two, four and six, the minimal left endpoint corners scale
`(r0,r1,r2,y)`, `(r1,r2,y)` and `(r2,y)` respectively. The right corners use
`c` and `w=1-y`. After pairing the endpoint weight to the old kernel, its
order-`m` derivative has homogeneous degree `-m`. Adding the native gap
weight, common Cauchy Vandermonde and companion Vandermonde gives:

| old position | native gap degree | Cauchy degree | companion degree | corner variables | fourth-order verdict |
| ---: | ---: | ---: | ---: | ---: | --- |
| 2 | 3 | 6 | 3 | 4 | integrable |
| 4 | 2 | 3 | 1 | 3 | integrable |
| 6 | 1 | 1 | 0 | 2 | logarithmically nonintegrable |

The terminal exception is exact. Its leading rational model is

```text
g^2 y/(y+a g),
d_g^4[g^2 y/(y+a g)] = 24 a^2 y^3/(y+a g)^5.
```

The last expression has degree `-2` in the two variables `(g,y)`, producing
a logarithmic absolute divergence on any interior split subcone. This is not
the K290 `g^-4` artifact: the native gap and Cauchy zero have already been
retained.

## Decision boundary

The result rejects occurrence-by-occurrence fourth-order global composition.
It does not prove divergence of a complete coherent group. K288 stores the
upper triangle with symmetry multiplicities, which is valid after the real
Gram integral but does not expose every ordered left/right old-position term
needed for pointwise corner cancellation. The next legal packet must restore
the ordered `3 x 3` coherent old-position sum, extract its terminal-corner
leading coefficient and test cancellation in all four groups before taking
absolute values. K294's radial gamma strata cannot repair an angular logarithm
at fixed positive `x`.
