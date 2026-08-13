---
artifact_type: construction_and_scope_result
created: 2026-08-10
status: HARD_REDUCTION_NOT_ACTION_EQUATION__ZERO_BRANCH_COMPLEMENT_DYNAMICAL__NONZERO_BRANCH_NORMAL_HESSIAN_OPEN
ledger_rows: [LT-GR1, LT-GR2b, LT-GR3, RA-D2, RA-F1, RA-F2, RA-G2, LT-SM3, AC-F1]
canon_verdict_change: none
---

# Selected K77 bosonic parent action ownership

## Result in plain English

The written source action does **not** make the moving rank-`8128`
`B`-adjoint-skew connection space the physical field space by equation of
motion. It norms the full connection displacement, and its quadratic term has
a nonzero Hessian on the rank-`8256` complementary sector at the zero branch.
Those directions are therefore dynamical there; they are not a radical,
Lagrange constraint or BV quotient.

This closes the rank-one question only at the zero branch. The exact
nonzero-branch normal Hessian has not been assembled. The next Build must
linearize the full selected action about `T*=-(kappa_1/312) Phi1` and resolve
the Hessian simultaneously by:

1. `B`-adjoint parity: `8128 + 8256`; and
2. moving Weyl block/coset: `8192 + 8192`.

Only after that gate should the program build the induced K77 Dirac/Rarita--
Schwinger operator on the source-full carrier and compare it with the declared
moving-Spin truncation.

## Layer 0: four nearby objects

| object | exact role | not equivalent to |
|---|---|---|
| `P_epsilon` | moving projector onto the `B`-adjoint-skew connection sector | an Euler constraint or fermion projector |
| `Q_epsilon=1-P_epsilon` | rank-`8256` connection complement | a gauge radical or BV-exact sector |
| `D_varpi chi_epsilon=0` | compatibility with two moving Weyl halves | `P_epsilon varpi=varpi` |
| gauge-rotated Levi-Civita connection | reference connection in `T=varpi-B_ref` | the variable connection `varpi` |

The parity and Weyl decompositions cross rather than coincide. Their exact
four cells are

```text
P/block = 4096    P/coset = 4032
Q/block = 4096    Q/coset = 4160.
```

Consequently, `D_varpi chi_epsilon=0` cannot stand in for the moving
`B`-adjoint projector. It removes all `8192` coset directions, including
directions in both `P` and `Q`.

## Exact composition

The source says the first action contains the unprojected quadratic term
`(kappa_1/2)<T,*T>` for the full adjoint-valued one-form
`T=varpi-B_ref`. The grade-saturated receipt says the Hodge/Krein lift in that
term is the identity on all `16384` internal connection directions. Hence, at
`T=0` and nonzero `kappa_1`, its linearized Euler map is nonzero on both the
rank-`8128` and rank-`8256` sectors.

This is stronger than the earlier consistent-truncation result but narrower
than full parent selection. The source-residual first-order graph preserves
both sectors and gives every complementary grade a live target. That graph is
not itself the full selected-action Hessian at the nonzero branch.

The known nonzero invariant branch also exposes a distinct cost of imposing
Weyl compatibility. The gauge-rotated Levi-Civita reference is block
compatible, but `Phi1` is odd and lies in the block-exchanging coset. Thus on
the invariant line and for nonzero `kappa_1`,

```text
T*=-(kappa_1/312) Phi1
```

is excluded by `D_varpi chi_epsilon=0`. This does not prove that every
nonzero compatible configuration is absent; it proves only that this already
constructed nonzero branch would be discarded.

## Efficient specialist preassessment

- **Layer-0 semantics — ACTUAL MATH, very high.** `P/Q`, block/coset,
  reference/field and constraint/equation are four different typings. The
  cross-cell dimensions make the first two distinctions exact.
- **Prior-art archaeology — ACTUAL MATH, very high.** The expensive
  `229376`-direction calculations already provide the ranks, transition graph,
  full Hodge lift and stationary branch. Composition is higher-yield than
  rebuilding them.
- **Variational bicomplex — ACTUAL MATH, very high.** A nondegenerate quadratic
  Hessian gives an equation for the complement; it does not generate
  `Q varpi=0`. The actual nonzero-branch Hessian remains the decisive missing
  object.
- **Principal-bundle geometry — ACTUAL MATH, high.** A connection preserving a
  moving Weyl reduction is a legitimate reduced-connection condition, but it
  is not the `B`-adjoint real-form reduction.
- **Representation/Clifford theory — ACTUAL MATH, high.** Odd `Phi1` exchanges
  Weyl halves, explaining exactly why the constructed nonzero invariant branch
  conflicts with block compatibility.
- **Symplectic/BV — ACTUAL MATH, high.** A nonzero bulk Hessian direction is
  not a presymplectic radical. No characteristic quotient or BV differential
  removes the complement in the current construction.
- **Operator/PDE/Krein — ACTUAL MATH, high.** This finite zero-jet result says
  nothing yet about a closed domain, positivity, propagation, contour or
  low-energy integration of the complementary modes.
- **Effective-field-theory — ACTUAL MATH, medium.** Heavy complementary modes
  might be integrated out after the nonzero Hessian and couplings are known;
  that would be an effective reduction, not a fundamental hard restriction.
- **Path-integral/analytic — ACTUAL MATH, medium.** A contour could suppress or
  select modes only after a real action and integration cycle are specified.
  It cannot be inferred from finite nondegeneracy alone.
- **Source/constraint audit — ACTUAL MATH, high.** Primary-source packets
  confirm the full displacement norm and the gauge-rotated Levi-Civita
  reference, while remaining silent on a hard `B`-adjoint constraint.

## Hostile-review correction

The strongest initial summary said that the action gives both sectors
nonzero dynamics. That is exact only for the quadratic Hessian at `T=0`.
The source-residual graph is first order and sector preserving, but it is not a
substitute for the selected-action Hessian at `T*`. The surviving disposition
is therefore:

```text
HARD_REDUCTION_NOT_ACTION_EQUATION
ZERO_BRANCH_COMPLEMENT_DYNAMICAL
NONZERO_BRANCH_NORMAL_HESSIAN_OPEN
```

The moving Spin bundle survives as a conditional local consistent truncation
or real-form posit. The full-`U(64,64)` versus two-`U(32,32)`-half parent,
global domain, BV quotient and physical low-energy parent remain open.

## Accounting and next gate

No verdict, residue, quotient, datum, coefficient, P1/P2/P3 or public posture
moves.

```text
headline_delta: none
conditions_closed: 3
  - hard P restriction is not generated by the written action at the zero branch
  - the complementary sector is dynamical rather than a radical there
  - D_varpi chi=0 is a distinct block/coset constraint and excludes the known nonzero invariant branch
conditions_opened: 1
  - compute the complete nonzero-branch normal Hessian in both decompositions
remaining_named_conditions: 2
  - nonzero-branch normal Hessian and effective/constraint disposition
  - induced K77 Dirac/RS operator and five-way physical-carrier comparison
```

Evidence: `38/38 PASS`, including a planted `P`-only action, a compatible
block-even displacement and the incompatible odd branch.
