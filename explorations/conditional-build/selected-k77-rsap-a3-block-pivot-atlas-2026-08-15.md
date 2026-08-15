---
title: "Selected-K77 RSAP complete split-A3 block-pivot atlas"
status: active_research
doc_type: exact_global_regular_symplectic_moment_atlas_construction
created: "2026-08-15"
registry: lab/process/selected-k77-rsap-a3-block-pivot-atlas.json
probe: tests/channel-swings/selected_k77_rsap_a3_block_pivot_atlas_probe.py
grade: "FULL SPLIT-A3 REGULAR ATLAS CONSTRUCTED; SIGNED BLOCK-PIVOT MOMENT AND PRIMITIVE COCYCLES CLOSE; FIRST SINGULAR CENTRALIZER JUMP OPEN"
canon_verdict_change: none
---

# Selected-K77 RSAP complete split-`A3` block-pivot atlas

## Result first

The remaining split-`A3` regular atlas closes. The correct completion is not
an inference from the one contractible Gauss cell. It is a finite symmetric
block-pivot atlas on

```text
B22 = {Q=Q^T : det(Q)=1, inertia(Q)=(2,2)}
    = SL(4,R)/SO(2,2).
```

The predecessor used the scalar `1+1+1+1` `LDL^T` sector with one fixed
inertia sign word and one ordered invariant chamber. Scalar pivots alone miss
regular points whose required leading diagonal pivot vanishes. Symmetric
elimination supplies the missing charts by allowing nonsingular `2 x 2`
pivots. There are five ordered block shapes, `66` pivot skeletons and `306`
inertia-labelled chart sectors in a redundant finite cover. The old scalar
sector contributes `144` of those labels; `162` use at least one `2 x 2`
pivot.

Every overlap is an ordinary base-coordinate change on `B22`. Its cotangent
lift preserves the tautological primitive strictly, hence preserves the
symplectic form. The cotangent moment map is the same geometric map in every
chart, so all local moment components intertwine. Triple maps compose to the
identity before taking cotangent lifts. Unlike the predecessor, this argument
does not need each chart component to be contractible: the tautological
one-form exists globally on every cotangent chart and pulls back naturally.

Therefore `X18(A3)=T*B22`, its `T*R4` centre completion, and the existing
`A2/A3` universal `26D` normalization form a complete split-regular atlas.
With the common `72D` leaf, the carrier remains `98D` and the regular map rank
remains `91`. Compact and mixed `A3` forms, the first singular centralizer
jump, deeper strata, zero charge and all-strata RSAP remain open.

## Layer 0 and the symmetric-space carrier

This is a classical symplectic/moment atlas. It is not an action-selected
physical phase space, a quantization or a particle-physics comparator.

Fix `H22=diag(1,1,-1,-1)`. The congruence map

```text
g SO(2,2) -> Q=g H22 g^T
```

identifies `SL(4,R)/SO(2,2)` with determinant-one real symmetric forms of
inertia `(2,2)`. The base has dimension `15-6=9`; its cotangent bundle has
dimension `18`. This makes the omitted “sign and Bruhat components” a concrete
matrix-atlas problem rather than an undefined collection of components.

## Complete block-pivot census

On one chart choose a symmetric permutation `P` and factor

```text
P Q P^T = L D L^T,
```

where `L` is block-unit lower triangular and `D` is symmetric block diagonal
with nonsingular blocks of size one or two. The possible ordered block
compositions and their census are:

| block shape | ordered pivot skeletons | inertia labels per skeleton | labelled sectors |
|---|---:|---:|---:|
| `1+1+1+1` | 24 | 6 | 144 |
| `2+1+1` | 12 | 4 | 48 |
| `1+2+1` | 12 | 4 | 48 |
| `1+1+2` | 12 | 4 | 48 |
| `2+2` | 6 | 3 | 18 |
| **total** | **66** |  | **306** |

The skeleton count is `4!/(b1! ... bk!)`. An inertia label assigns each block
its number of negative directions and requires the total to be two. Thus the
scalar sector has the six sign words with two plus and two minus pivots. A
shape with one `2 x 2` block has four allowed inertia allocations; `2+2` has
three.

These `306` labels are not asserted to be disjoint connected components.
They are a deliberately redundant finite atlas: different pivot skeletons
overlap, and a single point can have several valid factorizations. The split
diagonal centralizer separately has `2^3=8` components. On symmetric forms,
the sign representatives `epsilon` and `-epsilon` induce the same congruence,
leaving four effective form actions. The Weyl group is `S4`; it permutes the
six scalar inertia words transitively. All of these discrete changes are base
diffeomorphisms and therefore have canonical cotangent lifts.

For every block shape, the free entries of `L` plus the symmetric entries of
`D` total ten, the dimension of `Sym_4`. The equation `det(Q)=det(D)=1`
removes one coordinate, leaving the required nine-dimensional base chart.

## Why the cover is complete

The coverage proof is an exact elimination induction. At any Schur stage:

1. if some diagonal entry is nonzero, symmetrically permute it into the first
   position and take a nonsingular `1 x 1` pivot;
2. if every diagonal entry vanishes, nonsingularity forces some off-diagonal
   entry `b` to be nonzero; the corresponding principal block is
   `[[0,b],[b,0]]`, with determinant `-b^2`, so it is a nonsingular `2 x 2`
   pivot; and
3. the Schur complement stays nonsingular because the determinant factors as
   the pivot determinant times the Schur-complement determinant.

The induction terminates in one of the five displayed block shapes. Sylvester
inertia is additive across the block factorization, so restricting the block
labels to total inertia `(2,2)` gives exactly `B22`. The exact probe also
exhausts all `4 x 4` symmetric matrices with entries in `{-1,0,1}` and
determinant one as a finite planted control, including the all-zero-diagonal
anti-diagonal form that no scalar first pivot can enter.

This is the standard real symmetric-indefinite block factorization used by
the Bunch--Kaufman method; the external algorithmic control is the
[LAPACK `DSYTRF` specification](https://www.netlib.org/lapack/explore-html/d8/d0e/group__hetrf_ga431b081d6c9c48af82ec003a7d3070ff.html).
The coverage argument above is the exact algebraic statement used here; no
floating-point stability claim is imported.

## Transition, primitive and moment cocycles

Let `kappa_i` be the block-`LDL^T` coordinate map of chart `i`. On every
nonempty overlap the base transition is

```text
f_ji = kappa_j^-1 composed with kappa_i.
```

Its cotangent lift is

```text
x_j  = f_ji(x_i),
xi_j = (Df_ji)^(-T) xi_i.
```

Therefore

```text
xi_j^T dx_j = xi_i^T dx_i
```

identically, including on nonlinear scalar/block-pivot overlaps. The probe
checks one such rational overlap exactly. Exterior differentiation gives the
symplectic identity. The natural moment map

```text
J([g,xi]) = Ad_g^* xi
```

does not depend on the chosen coordinates for `[g,xi]`; the four central
coordinates are carried identically. Consequently the complete local target
map is the same `19`-component `sl4* x R4_zero` map in every normalization.

On a triple overlap,

```text
f_ki = f_kj composed with f_ji
```

by chart composition. The chain rule gives the same identity for the
cotangent lifts, so both the moment and primitive Cech defects vanish strictly.
Any nontrivial topology inside a block domain is harmless here: strict
tautological naturality, not exactness inferred from contractibility, kills
the primitive monodromy.

## Claim ceiling and next gate

- The complete split-`A3` regular atlas and its `A2/A3` regular transitions
  construct at `98D`, map rank `91`.
- The old identity Gauss component remains a valid subchart; its result is
  strengthened, not replaced.
- The `306` labels are overlapping atlas sectors, not orbit or connected-
  component counts.
- No compact or mixed `A3` factor, singular attachment, zero-charge chart or
  all-strata RSAP is constructed.
- No canon, ledger, residue, quotient datum, physical claim or public posture
  changes.

The next exact gate is the first split-`A3` singular centralizer jump. It must
attach the codimension-one subregular target to this completed regular atlas,
preserve the Poisson and primitive overlaps and realize the already-required
full-carrier map-rank change `91 -> 90`. Only then should deeper singular
types be entered.

Reproduce with:

```bash
python3 tests/channel-swings/selected_k77_rsap_a3_block_pivot_atlas_probe.py
```

The probe uses exact integer and rational arithmetic only.
