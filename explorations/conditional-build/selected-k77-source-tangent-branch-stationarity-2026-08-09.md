---
artifact_type: construction_and_composition_result
created: 2026-08-09
status: BOTH_ALGEBRAIC_BRANCHES_LOCAL_SELECTED_SOURCE_STATIONARY__AMPLITUDE_AND_COMPLETE_PARENT_TANGENT_OPEN
ledger_rows: [LT-GR1, LT-GR2b, LT-GR2c, LT-GR2d, LT-GR3, LT-GR5, LT-GR6]
canon_verdict_change: none
---

# Selected K77 source-tangent branch stationarity

## Result in plain English

Both nonzero algebraic branches from v0.110 survive the first variation when
the selected action is varied in Weinstein's actual local source variables
`(g,varpi,epsilon)`.

This reverses the apparent failure obtained by varying `B` independently at
fixed `T`. That derivative is nonzero on both branches, but it is not one of
the source's bulk Euler equations. After the correct pullback:

- all 1,470 known low-grade `varpi` directions vanish;
- all 91 selected Spin primitive-epsilon bulk directions vanish after the
  opposite `B/T` motion, moving Shiab term and integration by parts are
  combined;
- the ten metric directions vanish because the Levi-Civita chain is grade two,
  the moving coefficient packet is natural, and the branch action density is
  zero; and
- the complete observation receiver preserves the resulting zero covector.

The nonzero independent-`B` coefficient does not disappear. It becomes the
epsilon endpoint momentum. Compactly supported epsilon transformations are
bulk-degenerate; unrestricted boundary transformations remain charged.

This is a real construction gain, but it is local and conditional. The
algebraic amplitudes remain selected by the homogeneous ansatz, not by GU. The
known count `10+1470+91=1571` is not promoted to a complete full-action tangent,
and the selected Spin-native parent is not identified with either the two
`U(32,32)` halves or full `U(64,64)`.

## Layer 0

The load-bearing pullback is

```text
(g,varpi,epsilon) -> (g,B(epsilon),T=varpi-B(epsilon)).
```

Accordingly:

```text
delta_varpi:     delta B=0,       delta T=delta varpi,
delta_epsilon:  delta B=D_B eta, delta T=-D_B eta,
delta_g|varpi:  delta T=-delta B_LC, delta(varpi)=0.
```

An arbitrary `delta B` at fixed `T` lives on the larger reconstruction space,
not the displayed source domain. It remains a valuable planted control because
it is nonzero on both surviving branches.

## Exact connection Euler polynomials

For `B=b Phi1`, `T=t Phi1`, exact evaluation of every one of the 1,470
low-grade directions at six unisolvent rational points proves

```text
E_B = 312 t(2b+t) Trace_Cl1,
E_T = [312(b+t)^2+t] Trace_Cl1.
```

All 1,274 grade-two directions vanish identically. On both branches,
`E_T=0` while `E_B` is nonzero. Therefore source `varpi` stationarity closes
and the independent-`B` plant fires.

## Primitive epsilon and boundary ownership

The action-owned primitive epsilon equation is not the pointwise demand
`E_B-E_T=0`. Its bulk owner is the covariant adjoint of that coefficient plus
the moving-Shiab term. For every one of the 91 selected Spin generators, six
unisolvent rational backgrounds give exact cancellation of the lower Cartan
and moving-Shiab contribution. On the homogeneous branches the remaining
invariant trace coefficient is covariantly constant, so its bulk divergence
vanishes.

The endpoint term is nevertheless nonzero because `E_B-E_T=E_B`. This matches
the already-proved preboundary theorem: boundary-vanishing transformations are
characteristic, while unrestricted endpoint transformations carry a live
moment map. Calling the endpoint coefficient a failed bulk equation would
erase this symplectic distinction.

## Metric and observation pullback

At fixed source `varpi`, the Levi-Civita field chain obeys
`delta T=-delta B_LC`. Its image is coefficient-grade two and is annihilated by
the grade-one trace covector. The all-ten co-moving `Phi`/Shiab/Hodge/Clifford
packet is already exact and introduces no separate owner. Finally,

```text
L_1 = 7 t [624(b^2+bt+t^2/3)+t]
```

vanishes on both branches, so the direct gimmel-volume trace contributes zero.
The complete observation map transports a zero equation covector to zero.

## Specialist preassessment and hostile review

- **Source/Layer 0:** actual source variables must be pulled back before an
  Euler failure is booked.
- **Symplectic geometry:** the independent-`B` defect is endpoint momentum,
  not a missing bulk equation; unrestricted boundary charge stays live.
- **Variational bicomplex:** derivative epsilon terms are integrated by parts;
  the coefficient of `d eta` is not itself the epsilon Euler density.
- **Gauge/differential geometry:** the result is a local homogeneous
  covariant-divergence statement, not global associated-bundle or domain
  closure.
- **Representation/Clifford:** `1571` is the known selected low-grade bank;
  grade five and expanded group parents prevent a completeness claim.
- **PDE/Krein/analytic:** no propagation, positive domain, determinant,
  contour, reflection positivity or quantum saddle follows.

The hostile verdict is
`CANDIDATE_SURVIVES_WITH_SCOPE_NARROWING__LOCAL_SELECTED_SOURCE_EULER_ONLY`.
It rejects the stronger claims of a complete source tangent, an amplitude
prediction, a full action saddle, or a BV background.

## Progress and next gate

```text
Ledger v0.111 — 82/82 mapped (100%)
32 SAME · 19 DIFFERS · 26 NEEDS · 5 OVER-DETERMINED
Residue 84; conditional action-parent range 84..86
Scoped quotients 5

headline_delta: none
frontier_conditions_closed: 4
frontier_conditions_opened: 1
remaining_named_conditions: 3
```

The next high-information gate is not to rerun the same local stationarity.
It is to determine whether the branch amplitude is a modulus, a boundary
charge/condition, or a global obstruction while independently deciding the
action parent and complete tangent. Only a branch that survives that gate
should receive the full Hessian/BV/common-domain calculation.

P1/P2/P3 remain unused. No verdict, residue, quotient, datum, canon or public
posture changes.

## Evidence

- `tests/channel-swings/selected_k77_source_tangent_branch_stationarity_probe.py`
  — `62/62 PASS`.
- `tests/channel-swings/selected_k77_source_tangent_branch_stationarity_independent.sage`
  — `21/21 PASS`.
- `lab/process/selected-k77-source-tangent-branch-stationarity.json`.
- `lab/process/hostile-reviews/2026-08-09-selected-k77-source-tangent-branch-stationarity-review.md`.
