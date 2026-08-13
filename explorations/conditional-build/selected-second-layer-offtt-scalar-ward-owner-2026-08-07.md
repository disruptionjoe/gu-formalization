---
artifact_type: conditional_build_result
created: 2026-08-07
status: METRIC_ONLY_OFFTT_BLOCK_NOT_GAUGE_BASIC__FULL_COMOVING_DUPSILON_OWNER_REQUIRED
source_return: SOURCE-CONFIRMS__I2B_NORM_SQUARE__SOURCE-SILENT__I2B_TO_OBSERVER_FULL_II_OWNER
ledger: lab/process/conditional-physics-ledger-v0.42.json
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# Selected second-layer off-TT scalar and Ward owner

## Result in plain English

The direct metric pullback of the selected second-layer quadratic form passes
an important positive control: it reproduces the exact spin-two polynomial
already obtained on plus/cross,

```text
(14356/13689) s (s + 1922/3589).
```

On the spatial trace alone it produces the tempting expression

```text
(14356/13689) s (s + 1157/3589).
```

That is **not** yet a scalar particle pole. The complete ten-component metric
Hessian fails the linear diffeomorphism Ward test with rank four, the spatial
trace couples to the temporal gauge block, and the full Hessian remains rank
ten at `s=-1157/3589`. The number is a diagnostic of a non-basic restriction,
not a characteristic root of the coupled theory.

The construction therefore learned exactly which object is missing: the full
co-moving differential

```text
D Upsilon(delta g, delta varpi, delta section, delta observation).
```

Its connection, section and observation components must complete the metric
block and make the total Hessian descend through the diffeomorphism complex.
Only that quotient may own a scalar characteristic polynomial.

## Layer 0

| phrase | object computed | object kept distinct |
| --- | --- | --- |
| selected `I2B` | stationary norm square `1/2 <Upsilon,G Upsilon>` at `Upsilon=0` | observer/full-II Willmore first variation |
| full `B` coefficient | A12/A14 coefficient family with its own unselected Euler owner | coefficient of the selected residual Hessian |
| scalar restriction | spatial-trace matrix element of a non-basic metric block | scalar characteristic root on a gauge quotient |
| Ward defect | failure of the isolated metric block to annihilate four diffeomorphism directions | failure of the full action |
| full owner | co-moving differential in all action variables | a fitted gauge completion of the metric block |

The source displays the bosonic norm square, but does not identify it with the
older observer/full-II first-variation family. Importing that coefficient would
compare two distinct action owners.

## Exact construction

At the constant graph the metric-to-second-fundamental-form tangent is

```text
delta B_mn = -k_m k_n h - (1/2) delta(algebraic slice)_mn.
```

Pulling back the exact selected coefficients

```text
15376/13689 ||II||^2 - 340/4563 ||tr II||^2
```

and subtracting the *whole* zero-momentum operator yields a symmetric ten by
ten Hessian. It reproduces both plus and cross exactly, so the earlier TT and
massive SO(3) spin-two results survive unchanged.

The same Hessian fails the required descent:

```text
rank(K_metric G_diff) = 4,
<h00, K_metric h_trace> = 6 s (3589 s - 255)/13689,
rank K_metric(-1157/3589) = 10.
```

Two formal symmetric gauge-basic completions can be built that agree on every
spin-two state and disagree on the scalar block. This is an identifiability
control: Ward closure plus TT data do not select the missing scalar coefficient
unless the completion is derived from the action.

## Source return

```text
SOURCE-CONFIRMS:
  the second-layer bosonic residual norm square

SOURCE-SILENT:
  an identification of that norm-square Hessian with the older observer/full-II
  first-variation owner, and the full co-moving D Upsilon differential
```

## Hostile review

- **Differential geometry:** the graph tangent is exact at the stated constant
  background, but the moving connection, section and observation are absent.
- **Representation theory:** the spin-two block remains exact; no scalar irrep
  is promoted from a restricted matrix element.
- **Variational PDE:** a characteristic root requires the full gauge-descended
  principal operator. Rank-four Ward failure blocks that reading.
- **Symplectic geometry:** the isolated metric Hessian does not define the
  action-owned presymplectic reduction, a Green-Lagrangian boundary condition,
  or a BFV phase space.
- **Krein/operator theory:** no closed right-H domain, positive energy, or pole
  prescription follows from the finite matrix calculation.
- **Source criticism:** the source owns the norm-square form but is silent on
  the cross-owner identification and scalar coefficient.

The two-sided process charges both fired. The exciting summary would have
promoted `1157/3589` beyond the artifact, while the previous queue defended a
superseded action owner. Both are repaired in ledger v0.42.

## Progress and next gate

```text
Ledger v0.42 — 82/82 active rows mapped (100%)
32 SAME · 19 DIFFERS · 25 NEEDS · 6 OVER-DETERMINED
Residue — 84 continuous + >=19 function-valued + 9 forks
Quotients ranked — 4 scoped

headline_delta: none
frontier_conditions_closed: 3
  - exact metric pullback reproduces the selected TT polynomial
  - restricted scalar candidate is not a full characteristic root
  - old observer/full-II coefficient is not the selected I2B action owner
frontier_conditions_opened: 1
  - construct and descend the full co-moving D Upsilon differential
remaining_named_conditions: 4
  - full coupled Ward/basicness closure
  - scalar characteristic polynomial on the quotient
  - massless constraint complex
  - coupled nonzero-fermion Hessian and common domain
```

No scalar pole, coefficient, external datum or fifth quotient is added.
P1/P2/P3 remain unused. Curt remains formally separate and no third lane is
promoted.

## Verification

`tests/channel-swings/selected_second_layer_offtt_scalar_ward_owner_probe.py`
passes `30/30`, including planted failures against incomplete subtraction,
restricted-root promotion and TT-implies-Ward reasoning.
