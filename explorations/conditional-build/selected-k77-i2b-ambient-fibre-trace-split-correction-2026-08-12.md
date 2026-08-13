---
artifact_type: exact_conditional_variational_correction
created: 2026-08-12
status: V0208_MATRIX_THEOREM_SURVIVES__AMBIENT_ORBIT_RETYPED__FIBRE_NINE_PLUS_RADIAL_ONE__SOLDERING_FOUR_SEPARATE
source_return: SOURCE_CONFIRMS_AUTHORIAL_ONE_THREE_PLUS_SIX_FOUR_CARRIER_SPLIT_AND_C32_32_WEYL_SPLIT__SOURCE_SILENT_ON_PPLUS_SUBFAMILY_RANKS__REPO_CORRECTS_V0208_AMBIENT_FIBRE_TYPING
ledger_rows: [RA-E1, RA-E3, LT-SM6]
canon_verdict_change: none
---

# Selected K77 I2B ambient/fibre trace-split correction

## Result in plain English

V0.208's exact matrix calculation was sound, but its geometric label was not.
It tested all `91` rotations of the complete fourteen-dimensional `(7,7)`
ambient carrier.  It called those the rotations of the ten-dimensional `(6,4)`
metric fibre, whose rotation algebra has only `45` dimensions.

The thirteen motions of the chosen vertical trace vector split exactly into:

```text
9 genuine motions inside the metric fibre
+
4 motions mixing the base with the fibre.
```

The first nine are normalized trace-shape motions.  The four others belong to
the horizontal/vertical soldering or observation split.  A tenth metric-fibre
direction is the radial trace motion excluded by v0.208's fixed-norm orbit.
Thus the actual metric-fibre accounting is `9+1=10`, while the complete
ambient orbit is `9+4=13`.

## Layer 0

| object | exact type | disposition |
| --- | --- | --- |
| `so(7,7)` | ambient bivector algebra, dimension `91` | this is what v0.208 tested |
| `so(6,4)` | vertical metric-fibre algebra, dimension `45` | not the 91-generator family |
| normalized fibre trace orbit | `so(6,4)/so(6,3)`, dimension `9` | exact subfamily survives |
| ambient trace orbit | `so(7,7)/so(7,6)`, dimension `13` | exact v0.208 theorem after retyping |
| four base-fibre motions | generators mixing `TX^(1,3)` with the trace line | soldering/observation-owned |
| radial trace motion | the tenth direction in the ten-dimensional fibre | metric Frechet-owned, not orbit tangent |
| Higgs amplitude `r` | coefficient multiplying the selected connection cell | not the metric trace radius |

The source-level `C^(32,32) + C^(32,32)` carrier split, its derived
block-preserving `U(32,32) x U(32,32)` subgroup, the full `U(64,64)` principal
arena and two independent connection fields remain four distinct objects.

## Exact decomposition

With base indices `0..3`, vertical indices `4..13` and the negative trace axis
`q=13`, exact signature arithmetic gives

```text
ambient:  (7,7), dim so(7,7)=91
base:     (1,3), dim so(1,3)=6
fibre:    (6,4), dim so(6,4)=45
mixed:    4 x 10 = 40
91 = 6 + 45 + 40.
```

The ambient stabilizer/orbit split behind v0.208 is correctly

```text
so(7,7) = so(7,6) + q-perp,
91 = 78 + 13.
```

The vertical-fibre split is instead

```text
so(6,4) = so(6,3) + q-perp_vertical,
45 = 36 + 9.
```

The remaining four ambient orbit generators mix each base axis with `q`.
The full 78-dimensional ambient stabilizer correspondingly decomposes as
`6 + 36 + 36`: base rotations, fibre rotations fixing `q`, and mixed
base-with-fibre-perpendicular generators.

## Exact derivative ranks

Every one of the nine fibre directions and every one of the four soldering
directions retains v0.208's rank-`56` `dot P_+` identity and moving-action
covariance.  Their family ranks are:

```text
nine fibre directions:       rank 280
four soldering directions:   rank 140
all thirteen ambient:        rank 392
intersection:                280 + 140 - 392 = 28.
```

The two families are therefore neither identical nor disjoint.  The rank-28
intersection is a target-image overlap; it is not an identification of their
geometric owners and not a count of modes.

## What v0.208 keeps and loses

Survives unchanged at exact grade:

- all thirteen rank-56 projector derivatives;
- differentiated idempotency, off-diagonal exchange and action adjointness;
- moving-projector/moving-residual covariance;
- the rank-392 joint ambient image;
- zero new datum for ambient Spin-frame transport.

Retracted or retyped:

- `91` is not `dim so(6,4)`;
- `78+13` is not the vertical-fibre stabilizer/orbit split;
- the four base-fibre directions are not metric-fibre trace motions;
- the fixed-norm orbit did not close the tenth radial metric direction.

## Specialist and hostile-preparation synthesis

- **Layer-0/signature arithmetic** caught the mislabeled Lie algebra before it
  became load-bearing.
- **Homogeneous-space geometry** supplies the true nine-dimensional fibre
  orbit.
- **Principal-bundle geometry** assigns the four mixed directions to the
  moving horizontal/vertical split.
- **Variational bicomplex** routes the radial trace direction to the existing
  ten-direction metric Frechet packet rather than `dot P_+`.
- **Symplectic geometry** keeps those four soldering motions distinct until
  observation pullback and the presymplectic current are composed.
- **Analytic review** leaves Green domains, positivity and spectrum open.
- **Contrary review** preserves exact predecessor mathematics while refusing
  its stronger geometric summary.

## Accounting and next gate

No field, parameter, datum, quotient or selector is added.  P1/P2/P3 remain
unchanged and unused.  RA-E1, RA-E3 and LT-SM6 receive append-only correction
edges; headline verdicts, residue, forks, five quotients, canon and public
posture remain unchanged.

Next compose two separately typed packets inside the selected action:

1. the one radial metric-trace Frechet/Hodge/Shiab/connection derivative,
   using the already-certified ten-direction metric machinery; and
2. the four base-fibre soldering/observation derivatives.

Only after that composition may the program claim the complete metric plus
observation Euler and presymplectic preboundary classes.
