---
title: "Selected K77 common connection branch and moving-epsilon Hessian"
status: conditional_build
doc_type: exploration
created: "2026-08-08"
lane: "1"
channels: [BUILD, COMPOSE, SOURCE, VERIFY]
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# Selected K77 common connection branch and moving-epsilon Hessian

## Result

The old shared background was not a critical point of the complete selected
first action. It was only critical after restricting away the grade-one
connection directions.

The v0.105 point was

\[
 B_*=0,\qquad T_*=-\frac1{312}\Phi_1.
\]

It solves the raw residual and every `T` Euler equation. But exact
differentiation of the same source-shaped first action on the full admitted
`Cl1+Cl2` one-form tangent gives a nonzero `B` Euler covector: fourteen
diagonal grade-one support entries, each `1/312`. Together they are the single
invariant trace covector. Every grade-two direction vanishes, which explains
why the 125-field bivector slice looked stationary.

The useful result is constructive rather than merely negative. On the
invariant ansatz

\[
 B=b\Phi_1,\qquad T=t\Phi_1,
\]

the exact first action is

\[
 I_1(b,t)=7t(624b^2+624bt+208t^2+t).
\]

Besides the trivial zero, its unique nontrivial `B/T` critical point is

\[
 B_*=\frac1{156}\Phi_1,
 \qquad T_*=-\frac1{78}\Phi_1,
 \qquad A_*=B_*+T_*=-\frac1{156}\Phi_1.
\]

This point solves **all 1,470** low-grade `B` and `T` Euler directions and,
independently, the raw source residual

\[
 \mathscr S(F_{A_*})+*T_*=0.
\]

It is therefore the first explicit nontrivial background shared by the
connection equations of the selected first action and the residual used by
the second action. The direct metric Euler equation—movement of Hodge,
`Phi`, density and observation at fixed connection variables—has not yet been
computed. So this is a **common connection-critical branch**, not yet a full
stationary action background.

## Moving primitive epsilon

The lower-order response requested by v0.105 is now serialized. At the new
branch the 91 bivector generators give 91 independent moving-Shiab columns,
each with support two. Their pairing with `T_*` vanishes, so primitive epsilon
has zero first variation at the branch. But the mixed first-action Hessian is
not zero:

```text
moving-Shiab epsilon columns:       91
column rank:                         91
mixed receiver matrix:         1470 x 91
mixed rank:                          91
nonzero entries:                    182
nonzero receiver rows:              182
receiver grade:             Cl1 exclusively
```

Thus the lower-order epsilon block lands entirely in the grade-one sector
omitted from the 125-field metric/varpi/epsilon slice. Restricting the Hessian
to 125 fields would delete this full-rank block while all first variations
still vanish. That is precisely the kind of silent truncation a BV
construction cannot tolerate.

## Layer 0

| phrase | exact object | disposition |
|---|---|---|
| old residual-zero point | `B=0`, `T=-Phi1/312`; raw Upsilon and `E_T` zero | not full `E_B/E_T` criticality |
| repaired branch | `B=Phi1/156`, `T=-Phi1/78`; all 1470 connection equations and raw Upsilon zero | exact, direct metric Euler open |
| 125-field bank | metric ten + horizontal varpi 24 + primitive epsilon 91, all coefficient-grade two | constrained physical slice |
| known grade-one sector | complete `V* tensor V`, dimension/rank 196 | live first-action receiver sector |
| full low-grade source tangent | `Omega1 x (Cl1+Cl2)`, dimension 1470 | source-faithful connection candidate |
| epsilon first variation | pairing of `T_*` with moving Shiab plus connection chain | zero on repaired branch |
| epsilon Hessian cross | derivative paired with all low-grade connection directions | rank 91, grade-one only |
| action BV differential | tangent differential plus complete stationary Hessian and Noether complex | not constructed |

The minimum already-proved completion of the current slice is `125+196=321`
directions. A full low-grade source-faithful candidate would replace the
horizontal 24 by all 1,470 connection directions, giving
`10+1470+91=1571`. Selecting between these is an action-parent/truncation
question, not arithmetic. No new field is proposed by this count: both
candidate sectors already exist in the repository.

## Source return

```text
SOURCE-CONFIRMS:
  nonlinear first action; T=varpi-epsilon^-1 d epsilon; moving-Shiab grammar
SOURCE-SILENT:
  repaired common branch; direct metric Euler closure; 321 versus 1571 tangent
REPO-DERIVES:
  old trace-covector defect; repaired connection branch; rank-91 epsilon cross
```

This also composes prior art rather than pretending it was absent. The repo
already knew that the path-average curvature in the first action differs from
`F_A`, and it already owned the nondegenerate 196-dimensional grade-one
Hessian. Nobody had applied both facts to the v0.105 stationary fixture.

## Specialist and hostile return

- **Variational bicomplex:** raw-residual zero and first-action criticality are
  different equations. The corrected branch closes the connection equations;
  direct metric variation remains mandatory.
- **Symplectic geometry:** a constrained Hessian that deletes a live mixed
  block cannot own the BV differential or the presymplectic reduction.
- **Krein/operator:** exact finite ranks do not choose a field Riesz, positive
  structure, contour or maximal domain.
- **Microlocal PDE:** the epsilon term is lower order, so it need not change
  principal characteristics; it can still change the kernel and BV complex.
- **Real Clifford:** the receiver-grade result is exact over real K77. No
  complexification decides it.
- **Representation theory:** the rank-91 block is the full bivector module
  coupled to the grade-one receiver. The two `U(32,32)` halves and full
  `U(64,64)` remain separate parent comparators.
- **Source criticism:** Weinstein supplies the grammar, not this branch or
  truncation selection.
- **Constraint accounting:** no coefficient, selector, field, quotient or
  external datum is added. P1/P2/P3 remain unused.

The hostile review narrows “common stationary branch” to “common
connection-critical branch,” keeps the direct metric Euler open, and refuses
to promote either 321 or 1,571 fields before the action-parent gate is
decided.

## Progress and next gate

Ledger v0.106 remains `82/82`, with verdict counts `32/19/26/5`, residue
`84..86`, nine forks and five booked scoped quotients.

Five conditions close: the old-background first-action defect, exact
invariant action polynomial, nontrivial connection-critical branch, its raw
residual compatibility, and the complete moving-epsilon cross block. Two
conditions open explicitly: direct metric Euler closure on the repaired
branch, and source-faithful field-tangent selection.

Next compute the direct ten metric Euler components on the repaired branch.
If they vanish or can be closed without new freedom, choose and justify the
321 versus 1,571 field tangent, assemble the full first-action Hessian
including the rank-91 epsilon/Cl1 cross, and recompute the second-action
lower-order blocks on that same background. Only then derive the action BV
differential, trace soldering, maximal domain and odd BFV/BRST/CME.

## Receipts

- Primary exact route:
  `tests/channel-swings/selected_k77_common_first_action_epsilon_hessian_probe.py`
  — `61/61 PASS` after hostile-scope additions.
- Independent Sage/QQ route:
  `tests/channel-swings/selected_k77_common_first_action_epsilon_hessian_independent.sage`
  — `29/29 PASS` plus immutable predecessor replay.
- Hostile review:
  `lab/process/hostile-reviews/2026-08-08-selected-k77-common-first-action-epsilon-hessian-review.md`.
