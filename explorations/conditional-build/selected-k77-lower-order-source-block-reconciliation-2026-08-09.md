---
artifact_type: construction_and_composition_result
created: 2026-08-09
status: BOTH_BRANCHES_LOWER_EPSILON_RANK91__FIXED_VARPI_METRIC_PORTED__COMPLETE_PARENT_OPERATOR_OPEN
ledger_rows: [LT-GR1, LT-GR2b, LT-GR2c, LT-GR3, LT-GR5, LT-GR6]
canon_verdict_change: none
---

# Selected K77 lower-order source-block reconciliation

## Result in plain English

The two exact K77 backgrounds now carry the previously missing selected
lower-order primitive-epsilon block of the raw residual.  It is not zero: all
91 Spin directions remain independent on each branch.  The earlier
fixed-`varpi` metric theorem also ports to both branches once its
raw-residual-zero premise is checked explicitly.

The wave caught two tempting but false routes before arriving there.  It first
treated the transgression packet as the raw residual, and then tried to turn
the residual-zero condition into a zero Jacobian.  The correct objects are:

```text
Upsilon = T + * Shiab(F_A),       A=B+T=varpi,
D_epsilon Upsilon|lower
  = delta T + * (D_epsilon Shiab)(F_A).
```

At fixed `varpi`, `delta A=delta F_A=0`; the split term and Shiab coefficients
still move.  A zero residual therefore need not have a zero derivative.

## Exact epsilon block

On the invariant family `B=b Phi1`, `T=t Phi1`, six rational unisolvent
samples prove the coefficientwise quadratic identity

```text
Upsilon = [312(b+t)^2+t] Phi1,
D_epsilon Upsilon|lower
  = [-b+360(b+t)^2] [Phi1,eta].
```

The two source-stationary branches satisfy `Upsilon=0`, but their lower-order
coefficients are the positive nonzero conjugates

```text
(51-19 sqrt(3))/8112,
(51+19 sqrt(3))/8112.
```

The 91 commutator columns have exact rank 91, so both branch maps have rank
91.  Omitting moving Shiab and freezing `delta T` each fire as planted
failures.  This is lower order only; the already-built principal `-q eta`
bank remains live and distinct.

## Metric composition debt closed

The metric block was not missing mathematics.  v0.95 had already proved, at
fixed `varpi,epsilon`,

```text
delta T=-delta B_LC,
delta A=delta F_A=0,
rank(D_g Upsilon|physical transverse)=6
```

for timelike, spacelike and null symbols.  Its moving coefficient and
observation terms vanish specifically at `Upsilon*=0`.  Both algebraic
branches meet that premise, so the result ports.  The full Levi-Civita
first-jet source map remains rank 20 before the physical transverse quotient.

## What this does not establish

- The raw residual derivative is not the integrated first-action epsilon
  Euler density and is not its endpoint momentum.
- Lower-order rank 91 plus principal rank 91 is not a complete first-action or
  residual-square Hessian.
- The selected Spin tangent is not either `U(32,32)` half and not full
  `U(64,64)`.
- No action parent, branch, gauge fixing, ghost complex, positive Riesz map,
  closed domain, Green inverse, BV-BFV phase space or quantum measure follows.

## Reviews and progress

The symplectic lens keeps the live first-action endpoint charge separate from
this raw residual Jacobian.  The variational lens rejects residual-zero as a
claim of zero linearization.  The source lens returns `SOURCE-CONFIRMS` for
the grammar and `SOURCE-SILENT` for the exact K77 block.  The representation,
Krein, microlocal and analytic lenses preserve all parent, domain and quantum
fences.

```text
Ledger v0.120 — 82/82 mapped (100%)
32 SAME · 19 DIFFERS · 26 NEEDS · 5 OVER-DETERMINED
Residue 84; conditional action-parent range 84..86
Scoped quotients 5

headline_delta: none
frontier_conditions_closed: 2
frontier_conditions_opened: 0
remaining_named_conditions: 2
```

Next construct the complete first-action Hessian and expanded-parent
pairings, keeping the first and residual-square actions distinct.  Only then
admit gauge/ghost/domain work.  P1/P2/P3 remain unchanged and unused.

## Evidence

- `tests/channel-swings/selected_k77_lower_order_source_block_reconciliation_probe.py`
  — `36/36 PASS`.
- `tests/channel-swings/selected_k77_lower_order_source_block_reconciliation_independent.sage`
  — new result `22/22 PASS`, after independent predecessor replays.
- `lab/process/selected-k77-lower-order-source-block-reconciliation.json`.

The fail-closed wave audit and v0.119 predecessor audit pass. Three unrelated
baseline process debts remain unchanged: the process-gate inventory omits
`import_ban_audit.py`, the tests-root inventory has eleven unclassified root
scripts, and the functional-channel scope audit expects the pre-existing
`ACTION_OWNED_DEGREE14_GREEN_PRIMARY` directive. They are recorded, not
silently repaired by this scientific wave.
