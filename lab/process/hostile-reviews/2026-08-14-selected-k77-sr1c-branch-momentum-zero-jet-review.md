---
artifact_type: hostile_review
created: 2026-08-14
target: explorations/conditional-build/selected-k77-sr1c-branch-momentum-zero-jet-2026-08-14.md
verdict: SURVIVES_WITH_SCOPE_NARROWING__ZERO_JET_MOMENTUM_NOT_J1P
---

# Hostile review: SR-1C branch momentum zero-jet

## Verdict

`SURVIVES_WITH_SCOPE_NARROWING__ZERO_JET_MOMENTUM_NOT_J1P`.

The result correctly serializes a live fourteen-cell point momentum on both
algebraic roots and an exact zero moving-Shiab primitive return. It does not
construct the spatial first jet of the momentum or the total primitive
epsilon and metric rows.

## Strongest attacks

### `E_B` may have been inferred from `E_T`

Rejected. The calculation uses the independent-`B` variation of the same
source action. Its derivative companion has the action-owned factor one,
twice the `E_T` half-companion, and its nonzero-`T` algebraic term is evaluated
directly against every dual row.

### The symmetric `DT` correction may have been omitted

Rejected. The exact thirteen-cell correction is inserted through the same
196-row companion map used by the action/Bianchi predecessor. Deleting it
changes the momentum and fires a planted control.

### The covector could be nonzero only on one numerical root

Rejected. Every coefficient is reduced symbolically in the irreducible
quadratic quotient and remains a nonzero affine polynomial. No floating
embedding is selected, and a nonzero rational affine polynomial cannot share
a root with the irreducible quadratic.

### The moving-Shiab zero may be vacuous

Rejected. Before pairing with `T`, both the `F_BZ` and invariant-curvature
moving-Shiab families have rank 91. The paired zero is therefore a selection-
and-pairing result, not frozen coefficient motion.

### A live point momentum may already obstruct primitive epsilon

Rejected. Primitive epsilon contains `D_B^!p`, not `p` itself. Distinct field
jets can share the same point momentum and have different divergence. The
spatial first jet remains the next required owner.

### Normal coordinates may erase needed lower data

Accepted as a scope fence. This is the repository's local covariantly normal
formal-jet chart. Connection coefficients are contained in covariant
derivatives; the result is not a fixed-coordinate global formula or a bundle
descent theorem.

## Required successor

Differentiate the fourteen serialized coefficients on the admitted branch
first jet, including motion of the symmetric correction and exact root
relation. Construct `D_B^!p`, compose the already-zero moving-Shiab return,
and only then decide primitive epsilon stationarity. The moving
Hodge/frame/density/lowerer metric returns remain a separate required packet.
