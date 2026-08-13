---
artifact_type: construction_and_composition_result
created: 2026-08-11
ledger_version: "0.174"
result: TWO_EXACT_LOCAL_GRASSMANN_PAIRING_HORNS__ADJOINT_COMPATIBILITY_SELECTS_ZERO_WEIGHT_EQUATIONS__ONE_PRODUCT_INVARIANT_REMAINS
grade: "complete four-scalar Spin-natural local pairing classification over two exact fields and all fourteen directions; anti-linear reality, nonlinear action selection and global domain open"
canon_verdict_change: none
fork_assumed: none
fork_note: "Real K77 is a labelled conditional comparator; no signature or action-parent row is settled."
search_space_dim: "four pairing coefficients decided wholesale; two projective solution lines; two operator weights quotient to one invariant product"
free_object_delta: "zero new fields; no newly booked residue; one already-exposed action-parent coefficient remains"
residue_touched:
  - "RA-D4:T2_DISTANCE_ONLY"
  - "RA-F1:T2_DISTANCE_ONLY"
  - "RA-F2:T2_DISTANCE_ONLY"
  - "RA-G2:T2_DISTANCE_ONLY"
  - "LT-SM3:T2_DISTANCE_ONLY"
  - "AC-F1:T2_DISTANCE_ONLY"
ledger_rows: [RA-D4, RA-F1, RA-F2, RA-G2, LT-SM3, AC-F1]
source_return: SOURCE-CORRECTS
scripts:
  - tests/channel-swings/selected_k77_action_adjoint_weight_classification_probe.py
registry: lab/process/selected-k77-action-adjoint-weight-classification.json
---

# Selected K77 action-adjoint and weight classification

## Plain-English result

The local action is less obstructed—and less selective—than ledger v0.173 said.

The previous check asked only whether the operator was self-adjoint for one symmetric K77 pairing. That is not the physical criterion for a quadratic Grassmann action. What must be alternating is the full coefficient multiplying the two fermion fields. There are two ways for that to happen:

1. a symmetric pairing with an anti-self-adjoint operator; or
2. a skew pairing with a self-adjoint operator.

The complete four-parameter Spin-natural, degree-diagonal pairing family has exactly one projective line of each type. Both are nondegenerate, both work in all fourteen directions, and both work for arbitrary nonzero chiral weights. Thus the local Grassmann action does admit real invariant bilinears, but the adjoint equations select **zero** equations on the weights.

A pairing-preserving chiral field redefinition removes the ratio `w+/w-`. The remaining basis-independent coefficient is

\[
p=w_+w_-.
\]

So the two apparent weights reduce to one genuine local invariant, not zero and not two. The next question is whether the full nonlinear connection/Noether/observation structure fixes `p`; if it does not, `p` is one source-action coefficient already inside the ledger's exposed action-parent range.

## Layer 0

- operator self-adjointness is not operator anti-self-adjointness;
- neither is identical to alternation of the Grassmann quadratic coefficient;
- a local nondegenerate real bilinear is not an anti-linear reality involution or a closed domain;
- a pairing-preserving basis ratio is not the invariant product;
- selected Spin, two `U(32,32)` halves, and full `U(64,64)` remain different parents.

## Complete pairing classification

Write the natural pairing coefficients on the one-form plus/minus and zero-form plus/minus sectors as `(a+,a-,b+,b-)`. Exact coefficientwise classification gives:

| operator parity | pairing line | pairing symmetry | rank |
|---|---|---|---:|
| self-adjoint | `(1,-1,-1,1)` | skew | 1920 |
| anti-self-adjoint | `(1,1,1,1)` | symmetric | 1920 |

For both lines the full coefficient `P D` is alternating. The symmetric pairing plus a self-adjoint-only demand is a planted failure; changing only the relative form-degree sign is neither valid horn.

The result is reproduced over `GF(1009)` and `GF(1013)`. The primary run classifies the four-dimensional pairing space wholesale and both runs test all fourteen axes, unequal weights `(1,2)`, three further weight pairs, nondegeneracy and the chiral field-redefinition identity.

## Selection quotient

For `S=rP_+ + r^{-1}P_-`, applied to both zero- and one-form sectors,

\[
S^T P S=P,
\quad
w_+\mapsto r^2w_+,
\quad
w_-\mapsto r^{-2}w_-,
\quad
p\mapsto p.
\]

The ratio is therefore a basis coordinate within either pairing horn. The product is invariant. Adjoint/Grassmann compatibility has equation rank zero on `(w+,w-)`, so it cannot determine `p`.

## Source return

The 2021 matrix supplies four independent barred/unbarred fields, opposite-half row order, and the minus-star lower-left grammar. That grammar is compatible with the symmetric-pairing/anti-adjoint horn. The source does not identify the actual K77 pairing horn or select `p`.

Return: `SOURCE_CONFIRMS_FOUR_INDEPENDENT_FIELDS_OPPOSITE_HALF_ROW_ORDER_AND_MINUS_STAR_GRAMMAR__SOURCE_CORRECTS_SELF_ADJOINT_ONLY_CRITERION_TO_GRASSMANN_ALTERNATION__SOURCE_SILENT_ON_K77_PAIRING_HORN_AND_INVARIANT_WEIGHT_PRODUCT_SELECTION`.

## Frontier

Closed: complete natural local pairing classification; existence of nondegenerate alternating Grassmann coefficients; removal of the weight ratio as a pairing-preserving basis coordinate.

Opened: one sharper scalar question—does the full nonlinear selected action fix `p`?

Still open: selection of `p`; anti-linear reality and global Green/domain; observation and BV/cohomology; physical chirality, mirror removal, index and count. The weights were already inside the `84..86` parent-dependent residue range, so no booked residue or verdict moves.

## Next gate

`TEST_THE_REMAINING_PRODUCT_P_AGAINST_FULL_NONLINEAR_CONNECTION_COVARIANCE_NOETHER_NORMALIZATION_AND_OBSERVATION__IF_NONE_DEPENDS_ON_P_BOOK_ONE_ACTION_COEFFICIENT_RESIDUE_AND_ADVANCE_GLOBAL_DOMAIN`
