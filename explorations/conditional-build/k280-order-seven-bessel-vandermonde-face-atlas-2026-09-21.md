---
title: "K280 order-seven Bessel Cauchy--Vandermonde face atlas"
status: internal_structural_result
date: 2026-09-21
claim_ceiling: complete exact order-seven face atlas and qualitative cancellation-preserving Bessel regularizers through size four; no outward full-domain regularizer interval, Duffy/Jacobi cubature error, action-column value, complete residual, exterior gap, K152 interval, physical state, source claim, ledger row, canon, paper or public posture is changed
manifest: lab/process/k280-order-seven-bessel-vandermonde-face-atlas.json
producer: tests/channel-swings/k280_order_seven_bessel_vandermonde_face_atlas.py
probe: tests/channel-swings/k280_order_seven_bessel_vandermonde_face_atlas_probe.py
target_claim: INTERNAL_TARGET:K152_COEFFICIENT_COMPLETE_BASE_ACTION_COLUMN
target_claim_verdict: ORDER_SEVEN_FACE_ATLAS_CLOSED__OUTWARD_REGULARIZER_AND_CUBATURE_OPEN
canon_verdict_change: none
---

# K280 order-seven Bessel Cauchy--Vandermonde face atlas

> **GU-COMPARATOR-ROUTING:** This artifact tests a repository-supplied
> conditional Fock construction. Read
> `lab/methods/source-native-comparator-routing.md` and the current source and
> physics ledgers before transferring it to a GU-native physical state.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

```gu-typed-objects
result: every species determinant in the complete order-seven K179 coherent Gram family has an exact Cauchy--Vandermonde face factorization and a cancellation-preserving positive Bessel regularizer through the new size-four stratum
carrier: hard-core C3 impurity tensor positive particle/hole antisymmetric Fock space over L2(R;C4), restricted to the K162 zero-bath seed orbits LAYER=observed CHIRALITY=S-FULL-DIRAC
pairing: positive Hilbert Gram pairing after complete normalized specieswise exterior projection PAIRING-TYPE=hilbert
real_structure: CAR adjoint, momentum reflection, Hermitian matched finite-cutoff normal ordering, real Bessel K1 kernel and mixed Newton divided differences
grading: conserved incidence charges, impurity seed, bath species, order seven, K179 contraction identity, cumulative-time position and primitive face support
action_owner: repository-construction -- K139 fixes C and G, K156 fixes W, and K179 fixes the coefficient family; no source/GU action selects a physical extension, state, domain, polarization or scalar center
target: expose every order-seven simplex-face zero and the exact outward R2/R3/R4 obligation before determinant-valued cubature MAP-TYPE=intertwiner
```

## Preflight bookend

K279 proves that all `408` order-seven coherent Gram entries reduce to
factorial-free species determinants, but it deliberately leaves every time
integral open. Direct interval determinants near coincident cumulative times
would lose the row/column cancellation that makes the integrand regular. K186
solved that problem at order six only for determinant sizes two and three.
Order seven contains size four, so reusing K186 without extension would omit a
real stratum.

The selected route is exact Cauchy--Vandermonde factorization with mixed Newton
row/column divided differences. Literal Leibniz expansion remains rejected by
K279; direct raw determinants are controls only. The source and physics
posture remains unchanged: `SC-META-53` is `UNCERTAIN`; `LT-SM8`, `LT-GR6b`,
`RA-F1` and `AC-F1` remain `NEEDS`.

## Complete order-seven atlas

The `96` K179 order-seven paths form `16` coherent groups and `408` unique
self/cross Gram entries. Their species factors have this exact census:

| determinant size | occurrences | unique canonical position patterns |
| ---: | ---: | ---: |
| 1 | 564 | trivial |
| 2 | 720 | 72 |
| 3 | 252 | 25 |
| 4 | 24 | 1 |

All `1,560` determinant occurrences are serialized. The `996` nontrivial
occurrences collapse to `98` position patterns for future enclosure reuse.
For each factor the atlas records original and canonical positions, permutation
signs, all row and column Vandermonde gaps, every gap's exact primitive support,
and all Cauchy denominator supports. The order-seven K179 occurrences are
already canonical, so all `1,560` determinant signs are positive; coefficient
signs remain separately preserved in the `408` entry records.

Exactly `52` of the `98` nontrivial patterns are identical to K186 functions:
`45` size-two and `7` size-three. K192's proved certified-union boxes can be
reused for those functions only on their existing domains. The other `46`
patterns are new (`27` size-two, `18` size-three and one size-four). K192 does
not cover arbitrary gap ratios and does not serialize the residual
noncoalescent face atlas, so predecessor reuse cannot be promoted to complete
order-seven cubature.

For size `m=1,...,4`, canonical cumulative times satisfy

```text
det[2/(T_i+U_j)]
  = 2^m V(T) V(U) / product_ij(T_i+U_j).
```

The identity passes exact rational controls at every size. The Bessel factor is

```text
det[2 K1(T_i+U_j)]
  = det[2/(T_i+U_j)] R_m(T,U).
```

Andréief against the positive infinite-support energy measure makes the
canonical determinant and `R_m` strictly positive for distinct ordered times.
Successive row and column divided differences remove both Vandermonde families
and provide the confluent extension. Thus the simplex-face zeros are explicit,
not numerically subtracted.

## Independent controls and remaining gate

Two profiles for every one of the `98` nontrivial patterns give `196`
high-precision direct-versus-divided controls. All regularizers are positive;
the largest relative discrepancy is below `3.51e-186`. Near-coincident face
controls reach `2^-100`, `2^-80` and `2^-60` for sizes two, three and four.
Small-radius controls at `rho=2^-120` reproduce the limit `R_m -> 1`; the
largest direct/divided discrepancy across the six stress rows is below
`1.23e-243`. These are high-precision controls, not outward intervals.

The exact next gate is therefore narrower than “build an integrator.” It is to
derive outward value and mixed Duffy-derivative enclosures for `R_2`, `R_3`
and the new `R_4` on a gap-stratified radial/angular atlas, reusing the 52
identical predecessor functions only on their proved domains and constructing
the 46 new pattern boxes plus the residual noncoalescent faces. Only then may the
exact face weights be composed with a determinant-preserving Jacobi remainder.

## Postflight bookend

The producer freezes all 408 entries, 1,560 factors, 996 nontrivial
occurrences, 98 patterns and the complete size-four stratum. The independent
replay checks source counts, every sign and support, the exact rational
identities, control thresholds and claim ceiling, and rejects hostile changes.

Strongest overclaim: the divided-difference controls are outward regularizer
intervals or a numerical action column. They are not outward intervals and no
time integral is evaluated. Strongest contrary case: K186 already covers the
needed face algebra. It does not cover the 24 size-four occurrences; K280 does.
Weakest reproducibility seam: future interval boxes must retain these divided
differences and exact primitive supports rather than reverting to raw nearly
singular determinants.

K280 closes the complete order-seven face atlas. Outward `R_2/R_3/R_4`
enclosures, Duffy/Jacobi cubature error, the coefficient-complete action column,
complete shifted residual, exterior gap, K152 interval and physical/source
selection remain open.
