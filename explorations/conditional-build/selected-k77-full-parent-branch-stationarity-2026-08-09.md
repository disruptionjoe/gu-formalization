---
artifact_type: construction_and_composition_result
created: 2026-08-09
status: BOTH_BRANCHES_POINTWISE_STATIONARY_FOR_SPIN_BLOCK_AND_FULL_U_PARENTS__PARENT_SELECTION_GLOBAL_TANGENT_AMPLITUDE_OPEN
lane: "1"
functional_channels: [BUILD, COMPOSE, SOURCE, VERIFY]
ledger_rows: [LT-GR1, LT-GR2b, LT-GR2c, LT-GR2d, LT-GR3, LT-GR5, LT-GR6]
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# Selected K77 full-parent branch stationarity

## Result in plain English

The two exact nonzero branches are not artifacts of having tested too small an
internal tangent. Both remain stationary when the source-connection variation
is extended from the selected 1,470 low-grade directions to every one of the
`14 x 16,384 = 229,376` real pointwise `u(64,64)` directions.

This simultaneously covers:

- the selected Spin-native directions;
- the `8,192` block-preserving internal directions associated with the two
  separate `U(32,32)` Weyl halves; and
- the other `8,192` odd directions that exchange the halves and complete the
  full `U(64,64)` comparator.

The complete source-`varpi` Euler covector has only fourteen invariant
grade-one slots, all proportional to

```text
Upsilon = 312(b+t)^2+t.
```

It therefore vanishes on both branches. No grade-five or other omitted
direction survives there, even though grade five is demonstrably live on a
generic background.

Primitive epsilon also closes for the complete pointwise parent. Naturality of
the moving tautological/Shiab packet and cyclicity of scalar Clifford trace
give the infinitesimal identity for all 16,384 generators. The nonzero
`E_B-E_T` coefficient remains endpoint momentum, so unrestricted boundary
transformations are still charged.

## Layer 0

| phrase | object tested | not established |
| --- | --- | --- |
| full parent | complete real pointwise `u(64,64)` coefficient fibre | global adjoint-bundle section or chosen physical symmetry |
| two halves | even/block-preserving `U(32,32) x U(32,32)` directions | a source-selected observed action |
| full stationarity | zero local source-`varpi` covector plus homogeneous epsilon Noether identity | complete functional tangent, Hessian or global vacuum |
| endpoint momentum | nonzero derivative coefficient after bulk integration by parts | failed bulk Euler equation |
| compatibility | the same branch survives each candidate parent tangent | selection or identification of the parents |

The pointwise parent calculation does not turn the known coordinate count into
tangent completeness. Source epsilon is derivative-bearing, global sections
must patch, metric jets remain geometric, and the selected residual is not
closed under either large group without enlargement or reduction.

## Exact result

Six unisolvent rational `(b,t)` samples reconstruct every quadratic component
of the full real-basis Euler covectors. Their polynomial supports are:

```text
E_B:       14 grade-one components
E_T:       14 grade-one components
E_B-E_T:   14 grade-one components
```

Every `E_T` component is zero or divisible by `312(b+t)^2+t`. Evaluation in
`QQ(sqrt(3))` gives zero for all 229,376 `varpi` directions on both branches,
while all fourteen endpoint components remain nonzero.

The independent Sage/FLINT route reconstructs the branch equations, proves the
even/odd `8,192+8,192` split, and verifies the conjugation/trace identity in a
separate exact noncommuting matrix model. Freezing a moving factor fires the
negative control.

## Parent disposition

The result removes one possible selector: stationarity does **not** distinguish
the three parent candidates. It therefore does not settle the action-parent
fork or book the conditional `84..86` residue range. The parent still matters
for invariant pairing coordinates, residual closure, Hessian, BV and domain.

The source return is:

`SOURCE_CONFIRMS_TWO_C32_32_WEYL_HALVES_AND_SEPARATE_U64_64_PRINCIPAL_GROUP__SOURCE_SILENT_OPERATIVE_RESIDUAL_ACTION_PARENT_AND_GLOBAL_TANGENT`.

## Specialist assessment and hostile boundary

- **Representation/Clifford:** the even/odd split is exact; generic grade-five
  support is live, so the expanded test is nonvacuous.
- **Variational bicomplex:** source `varpi` and derivative-bearing epsilon are
  kept separate; the endpoint coefficient is not a pointwise bulk equation.
- **Symplectic geometry:** zero bulk gauge Euler and live endpoint momentum are
  compatible; no boundary quotient is silently imposed.
- **Gauge geometry:** full-parent epsilon closure follows from moving-packet
  naturality and cyclic trace, not from extrapolating 91 tested generators.
- **Krein/PDE/analytic:** no positive state space, characteristic complex,
  contour, determinant, quantum saddle or common closed domain follows.

Hostile verdict:
`CANDIDATE_SURVIVES_WITH_SCOPE_NARROWING__POINTWISE_INTERNAL_PARENT_COMPATIBILITY_ONLY`.

## Progress and next gate

```text
Ledger v0.112 — 82/82 mapped (100%)
32 SAME · 19 DIFFERS · 26 NEEDS · 5 OVER-DETERMINED
Residue 84; conditional action-parent range 84..86
Scoped quotients 5

headline_delta: none
frontier_conditions_closed: 2
frontier_conditions_opened: 0
remaining_named_conditions: 3
```

Next compose the exact nonzero endpoint momentum with the existing charged,
bare-gauge and minimal-edge boundary horns. That decides whether the surviving
amplitude is a modulus, a boundary condition, or killed by the chosen boundary
class. Parent selection and complete global tangent remain separate prerequisites
for the Hessian/BV/common-domain calculation.

P1/P2/P3 remain unused. No verdict, residue, quotient, datum, canon or public
posture changes.

## Evidence

- `tests/channel-swings/selected_k77_full_parent_branch_stationarity_probe.py`
  — `34/34 PASS`.
- `tests/channel-swings/selected_k77_full_parent_branch_stationarity_independent.sage`
  — `20/20 PASS`.
- `lab/process/selected-k77-full-parent-branch-stationarity.json`.
- `lab/process/hostile-reviews/2026-08-09-selected-k77-full-parent-branch-stationarity-review.md`.
