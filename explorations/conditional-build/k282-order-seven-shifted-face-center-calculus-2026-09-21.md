---
title: "K282 order-seven shifted face-center calculus"
status: internal_structural_result
date: 2026-09-21
claim_ceiling: exact shifted Hermite--Genocchi operator through size four, local outward neighborhoods for all 63 size-four masks and domain-preserving binding of all 98 order-seven patterns and 996 nontrivial occurrences; no arbitrary-gap coverage, mixed-Duffy/Jacobi error, action-column value, residual, exterior gap, native K152 interval, physical state, source claim, ledger row, canon, paper or public posture is changed
manifest: lab/process/k282-order-seven-shifted-face-center-calculus.json
producer: tests/channel-swings/k282_order_seven_shifted_face_center_calculus.py
probe: tests/channel-swings/k282_order_seven_shifted_face_center_calculus_probe.py
target_claim: INTERNAL_TARGET:K152_COEFFICIENT_COMPLETE_BASE_ACTION_COLUMN
target_claim_verdict: ALL_SIZE_FOUR_FACE_CENTERS_HAVE_LOCAL_OUTWARD_CHARTS__ARBITRARY_GAP_ATLAS_OPEN
canon_verdict_change: none
---

# K282 order-seven shifted face-center calculus

> **GU-COMPARATOR-ROUTING:** This artifact tests a repository-supplied
> conditional Fock construction. Read
> `lab/methods/source-native-comparator-routing.md` and the current source and
> physics ledgers before transferring it to a GU-native physical state.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

```gu-typed-objects
result: the shifted Hermite--Genocchi divided-difference operator extends through size four, and every one of the 63 size-four gap faces has a certified local outward neighborhood on 31/256<=x<=1/8; the complete order-seven family is bound to its size-specific operator without extending those local domains
carrier: hard-core C3 impurity tensor positive particle/hole antisymmetric Fock space over L2(R;C4), restricted to the K162 zero-bath seed orbits LAYER=observed CHIRALITY=S-FULL-DIRAC
pairing: positive Hilbert Gram pairing after complete normalized specieswise exterior projection PAIRING-TYPE=hilbert
real_structure: CAR adjoint, momentum reflection, Hermitian matched finite-cutoff normal ordering, real Bessel K1 kernel and confluent mixed Newton divided differences
grading: conserved incidence charges, impurity seed, bath species, order seven, K179 contraction identity, cumulative-time position, primitive face support and six size-four row/column gaps
action_owner: repository-construction -- K139 fixes C and G, K156 fixes W, and K179 fixes the coefficient family; no source/GU action selects a physical extension, state, domain, polarization or scalar center
target: provide local outward size-four face charts before transverse gap coverage and determinant-preserving Jacobi composition MAP-TYPE=intertwiner
```

## Preflight bookend

K281 proves the size-four coalescent normal form and all 63 face masks, but its
zero-centered order-16 perturbation certifies no finite-gap cell. The failure
is caused by taking absolute residual/cofactor bounds around the Cauchy
determinant. Repeating radial subdivision, evaluating raw nearly singular
determinants or expanding all Leibniz terms would not repair that lost shared
correlation.

K193 already supplies the correct shifted entry operator for size two and
three. K282 extends that construction to size four and binds the combined
operator to K280's complete order-seven census. Source and physics posture are
unchanged: `SC-META-53` is `UNCERTAIN`; `LT-SM8`, `LT-GR6b`, `RA-F1` and
`AC-F1` remain `NEEDS`.

## Exact shifted operator

For `F_x(y)=x K1(x(1+y))`, `G(y)=(1+y)^-1` and one entrywise
Hermite--Genocchi center `a`, K282 uses

```text
[r_0,...,r_i][c_0,...,c_j](F_x-G)
 = sum_n (F_x^(n)(a)-G^(n)(a))/n!
         [r_0,...,r_i][c_0,...,c_j](w+r+c-a)^n.
```

The mixed divided difference of each monomial is generated directly as a
nonnegative multinomial sum of complete homogeneous polynomials. It has no
explicit gap denominator and therefore remains exact on confluent faces. An
independent rational shift-and-restore replay checks all 272 size-four matrix
entries through order 16.

The first shifted implementation still expanded the determinant as absolute
residual terms around the Cauchy matrix. Its radius remained near nine even as
the chart width tended to zero. K282 therefore evaluates each exact confluent
Cauchy entry by the same-sign divided-difference Leibniz formula, adds every
shifted residual in one shared chart, and preconditions the complete matrix at
the face center:

```text
det(A) = det(A_0) det(I + A_0^-1 (A-A_0)).
```

This is the correlation-preserving step. It is not a positivity assumption;
the center inverse and both determinants are directed Arb intervals.

## Complete local face bank and family binding

Every one of K281's 63 nonempty masks certifies on the complete radial cell
`31/256 <= x <= 1/8`. The selected charts use coordinate half-width
`1/16384` and 64 contiguous radial subcells. Across the complete bank, the
outward normalized regularizer range has lower bound greater than
`0.2721697335` and upper bound less than `1.4052779900`. The fully active
face-center value independently recomputed at 280 decimal digits is about
`0.8322764562914433` and lies inside its directed interval.

K280 contains 72 size-two patterns with 720 occurrences, 25 size-three
patterns with 252 occurrences, and one size-four pattern with 24 occurrences.
K282 binds all 98 patterns and all 996 nontrivial occurrences to the matching
shifted operator. This does not enlarge any domain: size two and three retain
only the K193 charts, while size four receives only the 63 declared K282
charts. All 408 signed Gram entries and 16 coherent groups remain in scope.

## Postflight bookend

K282 closes the shifted face-center operator through size four and proves a
strict local outward neighborhood for every named size-four face. It releases
the fully active chart for a correlated projective-scale follow-through.

Strongest overclaim: these 63 local outward charts cover arbitrary gap ratios.
They do not. Strongest contrary case: the failed absolute cofactor radius
means the shifted operator fails. It does not; complete determinant
preconditioning converts the same exact entries into positive directed
enclosures. Weakest reproducibility seam: transverse shape variables must be
introduced in one common chart before mixed differentiation; independently
ranging them would discard the correlation just recovered.

There is no arbitrary-gap coverage, mixed-Duffy derivative or Jacobi cubature
error, no action-column value, no residual, exterior gap or native K152
interval, and no source, ledger, physical, canon, paper or public-posture move.
