---
artifact_type: construction_and_composition_result
created: 2026-08-09
status: BOTH_BRANCHES_GRADE1_HESSIAN_NONDEGENERATE__GRADE1_GRADE2_CROSS_ZERO__MINIMAL321_SURVIVES_CONNECTION_GATE_ONLY
ledger_rows: [LT-GR1, LT-GR2b, LT-GR2c, LT-GR3, LT-GR5, LT-GR6]
canon_verdict_change: none
---

# Selected K77 first-action tangent closure

## Result in plain English

The feared connection-to-off-slice leakage does not occur in the first
transgression action.  On both exact K77 backgrounds, every one of the `196`
grade-one connection directions has zero second-variation pairing with all
`1,274` grade-two covectors.  That includes the `24` horizontal grade-two
directions and the `1,250` off-slice directions.

The connection sector itself is not empty or degenerate.  Its complete
`196 x 196` Hessian has rank `196` and exact inertia `(97,99,0)` on both
branches.  The two matrices are unequal but Galois conjugate.

Consequently the smallest already-known selected completion,
`321 = 125+196`, survives this connection-block closure gate.  It is not
thereby selected and it is not a complete field tangent.  Metric/epsilon,
epsilon/epsilon, derivative-jet and expanded-parent blocks remain open.

## Layer 0

This Run computes the Hessian of the first transgression action.  It does not
compute the raw-residual Jacobian or the Hessian of the residual-norm-square
action.  A vanishing cross block is a statement about one block of one action;
it is not a BV quotient, a closed domain or a physical spectrum.

The compared tangent candidates also remain distinct:

- `321` is the minimum-known selected completion `125+196`;
- `1,571` is the known low-grade coordinate bank `10+1470+91`, not a theorem
  of functional completeness;
- `16,382` is the already-computed two-`U(32,32)`-half invariant closure;
- `16,383` is the already-computed full-`U(64,64)` parent closure.

The last two dimensions and their invariant pairing multiplicities were
already established by v0.93.  They were not recomputed or claimed as new.

## Exact certificate

For both stationary branches

```text
(b,t) = (1/208-sqrt(3)/312, (-2+sqrt(3))/208)
(b,t) = (1/208+sqrt(3)/312, (-2-sqrt(3))/208),
```

the grade-one/grade-two Hessian has shape `1274 x 196` and zero constant,
`b`, and `t` components coefficientwise.  Therefore its full, horizontal and
off-slice ranks are all zero on both branches.

The grade-one self blocks have:

```text
rank:     196, 196
inertia:  (97,99,0), (97,99,0)
nnz:      560, 560
relation: unequal Galois conjugates
```

The primary probe reports `27/27 PASS`.  An independent route central-
differences exact Euler covectors at three rational fixtures, checks three
widely separated grade-one inputs against every grade-two output, and uses
Sage/FLINT over `QQ(sqrt(3))` for wholesale self-block rank and Galois
conjugacy; it reports `18/18 PASS`.

## Fired control and durable trap

The first provisional calculation appeared to find rank-`177` off-slice
leakage.  The planted independent route killed it.  The `1,470` low-grade
basis is interleaved by form slot: its positional first `196` entries contain
only `28` grade-one and `168` grade-two elements.  Slicing by position tested
the wrong object.  Filtering by the recorded Clifford grade makes the entire
mixed block vanish.

This is the same class of failure Layer 0 is meant to prevent: a controlled
calculation can still answer the wrong typed question.  Future bank selection
must be label-based and independently checked by direct Euler variation.

## Source return

The source confirms the full adjoint-valued one-form, the two-connection
difference `T=varpi-epsilon^-1 d epsilon`, and the first-action grammar.  It is
silent on `321` versus `1,571`, the exact branch Hessian and the operative
action parent.  The source does not select the tangent from this result.

## Specialist pre-assessment and hostile post-review

- Differential geometry: test the entire off-slice grade-two carrier, not
  only the observed horizontal `24`.
- Representation theory: select banks by Clifford-grade labels and keep the
  two `U(32,32)` halves distinct from full `U(64,64)`.
- Variational bicomplex: compute the action Hessian, not a residual Jacobian.
- Symplectic geometry: a zero bulk cross block does not construct a
  presymplectic reduction or BFV quotient.
- Krein/operator theory: inertia `(97,99)` is nondegeneracy, not positivity or
  a physical mass spectrum.
- Source criticism: source silence about the tangent is not a selection rule.

The hostile review accepted the exact block theorem only after narrowing the
disposition from “tangent closed” to “survives this connection-block gate.”

## Progress and next gate

```text
Ledger v0.121 — 82/82 mapped (100%)
32 SAME · 19 DIFFERS · 26 NEEDS · 5 OVER-DETERMINED
Residue: 84 continuous; conditional parent range 84..86
Conditions closed: 2 · opened: 0 · remaining named: 2
```

Next complete the minimal-`321` metric/epsilon and epsilon/epsilon Hessian
blocks and test the remaining off-slice low-grade leakage.  Then build the
expanded-parent Hessians before gauge fixing, ghosts, `Dmax/Dmin`, Krein and
coupled BV--BFV work.  P1/P2/P3 remain unused.
