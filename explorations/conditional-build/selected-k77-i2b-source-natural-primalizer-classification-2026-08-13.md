---
artifact_type: conditional_build_invariant_pairing_result
created: 2026-08-13
run_id: RUN-20260813-024925-gu-i2b-source-natural-primalizer-classification
status: FIXED_SOURCE_NATURAL_QB_UNIQUE_UP_TO_SCALE_ON_LIVE_GRADE_ONE_BRANCH__PAIRING_ONLY_ESCAPE_CLOSED__MOVING_REDUCTION_OR_SOURCE_DERIVED_BV_TANGENT_OPEN
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
ledger_rows: [RA-E1, RA-E3, LT-SM6]
---

# Selected K77 I2B source-natural primalizer classification

## Result in plain English

The missing symbol `Q_B` is not an arbitrary supply of cancellation freedom on
the branch currently being tested.

The source supports two possible symmetry presentations: a full `U(64,64)`
parent, and two complex `C^(32,32)` Weyl halves with their block-preserving
`U(32,32) x U(32,32)` subgroup.  Those are distinct objects.  Nevertheless,
on the actual residual used by the trace-`H_q` construction, both permit only
one fixed natural symmetric pairing, up to an overall nonzero scale.

That is because the live residual is entirely Clifford grade one.  Its
coefficients are traceless and exchange the two Weyl halves:

- for full `U(64,64)`, the central invariant vanishes on this traceless
  sector, leaving only the trace pairing; and
- for the two-half subgroup, the odd residual is the off-diagonal
  bifundamental `Hom_C(S_-,S_+)`, whose invariant Hermitian form is unique up
  to scale.  Its real symmetric part is therefore one-dimensional.

Multiplying the already-computed action by a nonzero scale cannot change its
Euler zero set or erase any transverse cell.  The literal source-natural
fixed-pairing reading therefore retains the fourteen-cell ambient obstruction
of v0.201.  The later conditional observer `Q_u` rivals retain their separate
twelve-cell determinant-80 obstruction and remain fenced as repository
constructions.

This closes a pairing-only escape, not GU.  A moving or field-dependent
fundamental symmetry can create a different primalizer after an action-owned
symmetry reduction, and a source-derived constraint/full BV--Koszul--Tate
tangent can change the admissible variation.  Neither exists yet.

## Exact classification

### Full parent

For the reductive real Lie algebra `u(p,q)`, invariant symmetric bilinear
forms have the standard two-dimensional span

```text
B_1(X,Y) = Re Tr(XY),
B_0(X,Y) = Re Tr(X) Re Tr(Y).
```

Every grade-one Clifford generator in the actual `128 x 128` real K77
representation has trace zero.  Thus `B_0` restricts to zero and all
nondegenerate full-parent fixed pairings restrict to one line.

The executable control solves the complete exact invariance equations for the
faithful `u(1,1)` adjoint prototype.  The full invariant space has dimension
two, while its off-diagonal restriction has dimension one.  This is a firing
control for the center-versus-simple-factor distinction, not a low-rank
substitute for the general reductive-algebra theorem.

### Two halves

Under `U(S_+) x U(S_-)`, the odd coefficient sector is the complex irreducible
bifundamental

```text
W = Hom_C(S_-,S_+).
```

Complex Schur theory leaves one invariant Hermitian line on `W`; its real
symmetric part is the unique fixed quadratic pairing.  The exact
`U(1,1) x U(1,1)` prototype solves all symmetric-form equations on
`M_2(C)_R`: rank `35` in `36` unknowns, hence nullity one.  The unique form is
nondegenerate with inertia `(4,4)`, proving that “unique” does not mean
positive.

This result does not identify the two-half subgroup with full `U(64,64)`, nor
does it turn the two carrier halves into two independently weighted connection
fields.  The same restricted dimension arises by different representation
arguments.

## Composition with the action

V0.201 established that the source-owned residual square, using the natural
Hodge/Clifford-trace comparator, has a conditional radial Mexican-hat shape
but fourteen nonzero ambient connection derivatives.  The residual pieces are
all grade one, so unresolved weights on grades two and five never enter.

For any admissible fixed natural primalizer on this sector,

```text
Q_B = c Q_trace,   c != 0.
```

Hence

```text
E_T[Q_B] = c E_T[Q_trace].
```

All fourteen nonzero cells survive.  Choosing `c=0` is not a repair: it makes
the primalizer degenerate and deletes the action rather than solving it.

The phase-even rank-four pairing from v0.214 remains a useful conditional
counterexample to “the shape cannot fit,” but its exact noncompact `U(1,1)`
plant proves it is not invariant under either source-supported fixed parent.
It becomes admissible only if a moving fundamental symmetry or smaller
action-owned reduction supplies the extra structure.

## Layer 0

| object | result here | not identified with |
| --- | --- | --- |
| source `Q_B` slot | fixed natural pairing classified on grade one | observer `Q_u` |
| full-parent invariant forms | trace plus central product before restriction | the block subgroup |
| two-half invariant form | one line on the odd bifundamental | two independent connection weights |
| overall scale | cannot change an Euler zero set | a selected magnitude |
| phase-even pairing | exact conditional rank-four form | a full-unitary invariant form |
| moving reduction | possible ownership mechanism | a fixed pairing already present in the source |
| BV/KT tangent | possible restriction of admissible variations | a quadratic pairing |

## Adaptive specialist assessment

- **Invariant theory:** the center term and simple-factor trace term were
  separated before restriction.
- **Representation theory:** the two-half residual was typed as an odd
  bifundamental, not as two independently weighted adjoint blocks.
- **Krein geometry:** the unique block form is balanced, so no positivity or
  Hilbert norm is inferred.
- **Variational bicomplex:** a nonzero scalar multiple preserves the Euler
  zero set; it cannot cancel an independent cotangent component.
- **Symplectic/BV:** a primalizer does not construct a constraint, quotient or
  physical tangent.
- **Source criticism:** Weinstein owns the norm-square architecture and group
  arenas, but not the repository's real K77 formula.
- **Contrary path:** field-dependent/moving reductions and source-derived
  BV--KT remain live and are now the only correctly typed escapes in this
  branch.

## Progress meter

```text
Ledger v0.231 — 82/82 target rows mapped (100%)
32 SAME · 19 DIFFERS · 26 NEEDS · 5 OVER-DETERMINED
Residue: 84 continuous + >=19 function-valued + 9 discrete forks
Tightness: T4x1 T3x3 T2x1 · scoped quotients: 5
Headline delta: none
Frontier closed: fixed source-natural Q_B freedom as a cancellation route
Frontier opened: none; moving/action-owned reduction and source-derived BV-KT were already named
```

## Required next gate

Do not search another fixed pairing or assign independent weights to the two
Weyl halves.  V0.192 already showed that the current pointwise action does not
select the compatible moving reduction.  The rank-one successor is therefore
the smallest source-derived constraint/full BV--Koszul--Tate differential on
the full/two-half connection parent.  Compute its tangent image and test
whether it legitimately removes the fourteen source-natural cells and the two
determinant-80 `Q_u` shapes.  A fitted subspace remains inadmissible.

The exact probe passes its predecessor replays, invariant-form classifiers,
actual K77 trace/grade checks, scaling theorem and planted failures.
