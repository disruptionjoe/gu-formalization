---
artifact_type: conditional_build_result
created: 2026-08-07
status: FULL_II_PLUS_TRACE__SELECTED_CL2_COMPLETE__TOTAL_RESIDUAL_OTHER_GRADES_OPEN
source_return: SOURCE-CONFIRMS_NORM_SQUARE__SOURCE_SILENT_ON_OWNER_MAP
canon_verdict_change: none
---

# Selected second-layer full-Cl2 residual pullback

## Result in plain English

The complete selected Clifford-grade-two response of the second action is now
known, not sampled.  The 1,274-by-100 map contains only 640 nonzero entries,
has full rank 100, and changes the earlier projected trace coefficient by a
fixed amount.  It still does **not** equal a pure observer full-`II` norm:

```text
I2B_Cl2(II) = kappa_1^2 [
  (15376/13689) ||II||^2
  -(340/4563) ||tr II||^2
].
```

The trace and traceless relative eigenvalues are respectively
`11296/13689` and `15376/13689`.  Both are positive, so completing the
selected `Cl2` target preserves the native inertia `(54,46)` rather than
turning the form into positive physical energy.

This is a real construction advance.  It closes the selected-`Cl2` leakage
question, while leaving the total residual and other Clifford grades open.

## Layer 0

| phrase | object proved here | object kept distinct |
| --- | --- | --- |
| full residual | complete selected bosonic `Cl2` residual response to the 100 Gauss variables | the source's total bosonic-plus-fermionic residual and any other Clifford grade |
| norm square | stationary quadratic pullback of the native indefinite target pairing | a positive Hilbert energy or physical probability norm |
| co-moving | exact frame/epsilon/observation transport at a stationary quadratic point | cubic, Euler, preboundary or covariant-phase-space equivalence |
| full `II` | the observer rank-100 second-fundamental-form quadratic invariant | a helicity-two graviton carrier or Einstein recovery |

The source confirms the two-layer norm-square architecture and is silent on
the map from this selected K77 residual to observer full-`II`.  Source return:
`SOURCE-CONFIRMS_NORM_SQUARE__SOURCE_SILENT_ON_OWNER_MAP`.

## Representation-blocked construction

Splitting the residual by horizontal/normal form index and by `HH/HN/NN`
bivector type leaves only two support cells:

```text
H_HN: 280 nonzero coefficients
N_NN: 360 nonzero coefficients
total: 640
```

Sixty off-diagonal `II_(mu nu)^a` columns contain two nonzero entries.  Forty
diagonal columns contain thirteen: four `H_HN` entries and the nine oriented
`N_NN` directions transverse to normal `a`.  The resulting sparse formula
has rank 100.  An exhaustive exact check then compares every one of the
`1,274 x 100` coefficients to the selected-action Hessian.

The earlier rank-100 Gauss projection had trace coefficient `-448/4563`.
The orthogonal completion adds exactly `4/169`, producing `-340/4563`.
Thus the original `2/39` leakage witness was genuine but local: its complete
effect is a trace-sector correction, not loss of rank or a new quotient.

## Stationary co-moving composition

For

```text
I2(s) = 1/2 <U(s), G(s) U(s)>,    U(0)=0,
```

the second variation is `<DU,G(0)DU>`.  Derivatives of the moving target
metric, frame, epsilon and observation transport multiply `U(0)` and vanish
at this grade.  This composes the previously exact naturality and observation
theorems without freezing them as physical data.

The cancellation is strictly stationary and quadratic.  It supplies no
cubic, Euler, preboundary, symplectic-current, helicity, BV, BFV or global
domain theorem.

## Disposition

- Fired ending: `FULL_II_PLUS_TRACE`.
- Selected `Cl2` completeness: closed.
- Total-residual/other-grade support: open.
- Helicity two: untested.
- Coefficient selection, residue reduction and a fifth quotient: not booked.
- P1/P2/P3: unused.
- Curt track: formally separate; no third lane is promoted.

The next highest-information gate is to type the total residual by Clifford
grade, prove zero blocks without reusing the killed full-Spin shortcut, and
compute any surviving other-grade support.  Only the resulting complete
quadratic carrier may advance to cubic/Euler/preboundary and helicity tests.
Common-domain and odd BV/BFV work remains conditional on exact helicity two.

## Verification

`tests/channel-swings/selected_second_layer_full_cl2_residual_pullback_probe.py`
derives the sparse formula, exhaustively checks all coefficients, computes
the exact Gram pullback, verifies stationary co-moving cancellation, and runs
planted scope failures.  Result: `32/32 PASS`.

The six-lens hostile review is filed at
`lab/process/hostile-reviews/2026-08-07-selected-second-layer-full-cl2-residual-pullback-review.md`.
