---
title: "Selected-K77 RSAP split-A3 two-wall census and first origin attachment"
status: active_research
doc_type: exact_singular_atlas_census_and_attachment
created: "2026-08-15"
registry: lab/process/selected-k77-rsap-a3-two-wall-census-origin-attachment.json
probe: tests/channel-swings/selected_k77_rsap_a3_two_wall_census_origin_attachment_probe.py
grade: "FULL SPLIT-A3 TWO-WALL TARGET CENSUS CLOSED; SAME-SIGN LOCAL FACE EXCLUDED AS RSAP; FIRST ALTERNATING THREE-WALL ORIGIN ATTACHED AT 98D/MAP RANK 85"
canon_verdict_change: none
---

# Selected-K77 RSAP split-`A3` two-wall census and first origin attachment

## Result first

The split-`A3` two-wall target census closes, and the first genuinely
three-wall intersection attaches.

Among the six `A3` roots there are `15` unordered pairs. Twelve share one
coordinate and span `A2`; three are disjoint and span `A1 x A1`. These are
the only target subsystem types. Relative to a fixed `(2,2)` signature, their
source presentations subdivide into

```text
A2:       4 split/split presentations, 8 same-sign/opposite-sign presentations,
A1 x A1: 2 split/split presentations, 1 same-sign/same-sign presentation.
```

The apparent extra `A2` type does not require a new target factor. Its naive
same-sign rank-one restriction is `T*(SL(2,R)/SO(2))`. That moment map sees
only zero and the hyperbolic semisimple cone in `sl2*`; it misses elliptic and
nonzero nilpotent controls and is not locally surjective at zero. It is
therefore a partial source sheet, not an RSAP wall chart.

Every `A2` target pair nevertheless has another preimage inside the same
`T*(SL(3,R)/SO(2,1))` factor whose three-coordinate signs alternate
`(+,-,+)` or `(-,+,-)`. Both roots are then the already constructed
`sl2/so(1,1)` wall type. Likewise every ordered `A3` chain has exactly two
alternating `(2,2)` allocations. Choose `(+,-,+,-)`: all three simple-root
faces are split, both adjacent two-wall faces are the banked principal
`sl3/so(2,1)` model, and the orthogonal face is the banked split `A1 x A1`
model. No new field is introduced; the construction selects the surjective
sheet already present in the homogeneous cotangent carrier.

At the three-wall intersection the `sl4` covector is zero. The smooth source
is still

```text
S72 x T*(SL(4,R)/SO(2,2)) x T*R4,
```

of dimension `98`. The principal factor map rank is `9` at zero, so the full
map rank is `72+9+4=85` while the target Poisson rank is `72`. This saturates
the pointwise RSAP bound `s <= (98+72)/2=85`. The complete schedules through
the regular, one-wall, orthogonal-two-wall, adjacent-`A2`, and origin strata
are respectively

```text
target rank: 84, 82, 80, 78, 72,
map rank:    91, 90, 89, 88, 85.
```

All face-to-origin transitions are cotangent lifts through the common
principal factor. Every triangle in the first four-chart nerve closes by
normalization, so the geometric moment and tautological primitive Cech defects
are zero. Other `A3` real forms, the remaining nonsemisimple singular Jordan
transition census, deeper `so(7,7)` strata, zero charge and global all-strata
RSAP remain open.

## Layer 0

This is a classical symplectic/Poisson atlas construction. It is not an
action-selected physical phase space, a quantization, a spectrum or a
particle-physics comparator.

## Exact two-wall census

Identify an `A3` root with an edge of the complete graph on four eigenvalue
labels. Two edges either share a vertex or are disjoint:

| root-pair relation | count | subsystem |
|---|---:|---|
| share one vertex | `12` | `A2` |
| disjoint | `3` | `A1 x A1` |

The Weyl group `S4` is transitive on each row. Now fix two positive and two
negative signs. A root is split when its endpoints have opposite signs and
same-sign otherwise. Direct enumeration gives:

- `A2`: four pairs of two split roots and eight pairs with one same-sign and
  one split root; two same-sign roots are impossible on a three-coordinate
  block of signature `(2,1)` or `(1,2)`;
- `A1 x A1`: two split/split perfect matchings and one same/same matching;
  a same/split perfect matching is impossible with two signs of each kind.

The orthogonal cases were all banked by the rank-82 wall-family packet. The
already attached `(+,-,+)` principal `A2` chart handles the split/split row.
Only the same/split presentation needs a scope decision.

## Why the naive same-sign face is not a wall chart

Use the standard `sl2` basis

```text
H = [[1,0],[0,-1]],
X = E+F,
K = E-F.
```

For the same-sign involution, the fixed line is `so(2)=R K` and its
annihilator is `span(H,X)`. Every covector there has the form

```text
aH+bX = [[a,b],[b,-a]],       det=-(a^2+b^2).
```

Conjugation preserves determinant. Hence the coadjoint saturation contains
only hyperbolic semisimple elements and zero. It excludes the elliptic control
`K`, whose determinant is `+1`, and the nonzero nilpotent `H+K`, whose
determinant is zero while the displayed plane has determinant zero only at
the origin. Thus `T*(SL2/SO2)` is not locally onto `sl2*` at the wall.

For an opposite-sign root the fixed line is `so(1,1)=R X` and the
annihilator is `span(H,K)`. There

```text
det(aH+bK)=b^2-a^2,
```

and explicit hyperbolic, elliptic and nonzero nilpotent representatives are
`H`, `K`, and `H+K`. This is the source-native wall sheet already proved
surjective. The same-sign result is therefore a scoped partial-image result,
not an obstruction to the principal `A2` factor.

## Opposite-sign sheet routing

At an `A2` intersection the repeated three-dimensional eigenspace has
signature `(2,1)` or `(1,2)`. Its zero cotangent fibre contains every base
form of that signature. For any chosen adjacent target roots, assign the
minority sign to their shared vertex and the majority sign to the two outer
vertices. Both root restrictions are then opposite-sign. The fourth
coordinate receives the remaining sign needed for total signature `(2,2)`.

This is not a claim that the partial same-sign source point is locally
surjective. It says the same smooth homogeneous cotangent factor has a second
preimage of the target intersection that is surjective in all required wall
directions. The completed block-pivot atlas contains both base regions, while
the RSAP attachment uses the opposite-sign one.

For a full ordered `A3` chain, the only assignments making all three adjacent
roots opposite-sign are

```text
(+,-,+,-),       (-,+,-,+).
```

Both have total signature `(2,2)`. This alternating sheet reduces every
rank-one and two-wall face to a previously constructed model.

## All real Jordan types have a `(2,2)` symmetrizer

The origin attachment must cover a neighborhood containing more than real
diagonal controls. The exact block census supplies the required statement.
For a real Jordan block of size `n`, the reverse identity `R_n` satisfies

```text
J_n^T R_n = R_n J_n.
```

Its inertia is `(1,0)`, `(1,1)`, `(2,1)`, `(2,2)` for `n=1,2,3,4`, up to
overall sign. A real complex-pair block is self-adjoint for a `(1,1)` form;
a size-two complex Jordan block is self-adjoint for the tensor product of that
form with `R_2`, of inertia `(2,2)`. Taking block sums and choosing signs gives
inertia `(2,2)` for all nine real dimension-four Jordan configurations:

```text
4; 3+1; 2+2; 2+1+1; 1+1+1+1;
complex+2; complex+1+1; complex+complex; complex-Jordan-size-2.
```

The probe verifies every block identity and inertia exactly. Consequently
every real `sl4` covector is conjugate to the annihilator of some `so(2,2)`
base point. Every such form has positive determinant and can be multiplied by
a positive scalar to normalize its determinant to one without changing the
self-adjointness identity or inertia. The split principal cotangent moment map
is therefore onto every real Jordan type. This is a dimension-four signature
refinement of the general
symmetric-symmetrizer result of
[Taussky--Zassenhaus](https://doi.org/10.2140/pjm.1959.9.893).

## Origin rank and cocycle

For `m=ann(so(2,2))`, the cotangent moment differential at `[e,lambda]` is

```text
dJ(X,delta lambda)=[X,lambda]+delta lambda,
X,delta lambda in m.
```

The moving-space centralizer dimensions at the regular, one-wall,
`A1 x A1`, `A2`, and origin controls are `3,4,5,6,9`. Since `dim(m)=9`, the
factor map ranks are `15,14,13,12,9`. Adding the common `72D` leaf and the
four external zero-coordinate projections gives the stated full schedule.

Normalize the two principal-`A2` face charts, the orthogonal `A1 x A1` chart,
and the `A3` origin chart through the same cotangent factor. Each transition
is an actual base diffeomorphism with inverse-transpose covector change.
Therefore the tautological primitive and symplectic form agree strictly, and
the geometric moment map is unchanged. Every triangular product in the
four-chart nerve telescopes to identity. No contractibility, logarithm,
prequantum twist or integrality assumption is used.

## Claim ceiling and next gate

- Every split-`A3` two-wall target type is classified and covered.
- The naive same-sign `SL2/SO2` face is excluded only as an RSAP wall chart;
  it remains a legitimate partial source sheet.
- One alternating three-wall `A3` origin attachment constructs at `98D`, map
  rank `85`, target Poisson rank `72`.
- The result proves surjectivity of the split principal factor onto every real
  `sl4` Jordan type, but does not yet compute every nonsemisimple singular
  transition and Cech overlap inside the full `so(7,7)` atlas.
- Other `A3` real forms, deeper ambient strata, zero charge and all-strata
  RSAP remain open.
- No canon, ledger, residue, quotient datum, physical interpretation or public
  posture changes.

Next classify and glue the remaining split-`A3` nonsemisimple singular Jordan
transitions. Only after their rank and primitive cocycles close should another
`A3` real form or a higher-root subsystem be entered.

Reproduce with:

```bash
python3 tests/channel-swings/selected_k77_rsap_a3_two_wall_census_origin_attachment_probe.py
```

The certificate uses exact integer and rational arithmetic only.
