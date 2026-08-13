---
artifact_type: exact_conditional_bundle_variational_result
created: 2026-08-12
status: PPLUS_DESCENDS_WITHOUT_CHOSEN_GLOBAL_SPIN_FRAME__MOVING_DPPLUS_EXACT__ARBITRARY_FIELD_EULER_PREBOUNDARY_OPEN
lane: "1"
functional_channels: [BUILD, COMPOSE, SOURCE, VERIFY]
source_return: SOURCE_CONFIRMS_MOVING_EPSILON_CONJUGATION_GRAMMAR__SOURCE_SILENT_ON_HQ_AND_PPLUS__REPO_DERIVES_SIGN_INSENSITIVE_ASSOCIATED_PPLUS_DESCENT_AND_MOVING_DPPLUS__UNITARY_PARENT_AND_FULL_EULER_PREBOUNDARY_OPEN
ledger_rows: [RA-E1, RA-E3, LT-SM6]
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# Selected K77 I2B global primalizer descent

## Result in plain English

The projector derived in v0.206 does not require a globally chosen Spin
frame.  The already-supplied Spin structure, the global tautological trace
direction and the associated-bundle transition law are enough: the two signs
of every local Spin lift act identically by conjugation, so

```text
P_+ = (1+tau_q)/2
```

glues as a global endomorphism of the selected residual bundle.

The wave also computes the missing term when that reduction moves.  Along the
tested normal-plane Cartan generator `L`,

```text
dot tau = [L,tau],             dot P_+ = (1/2)[L,tau].
```

`dot P_+` has exact rank `56` on the `392`-real-dimensional target.  It is not
optional: freezing the projector fails on exactly `56` carrier basis
directions.  Including it restores the differentiated naturality and the
moving first-variation identity.

This closes the associated-bundle and pure-frame derivative subproblems.  It
does not identify the transition with Weinstein's `epsilon`, select the full
`U(64,64)` connection or the two-`U(32,32)` reduction, or compute arbitrary
metric/field variations and the complete Euler/preboundary classes.

## Layer 0

| object | meaning here | not established |
| --- | --- | --- |
| underlying Spin bundle | supplied global structure used to form associated bundles | a global Spin frame/section |
| local Spin lift `S` or `-S` | two representatives of one orthogonal transition | a physical datum or source `epsilon` |
| residual bundle | associated target bundle carrying the selected Shiab output | source-full unitary connection parent |
| `tau_q` | moving `H_q` real involution on that bundle | a source-published reality condition |
| `P_+` | action-owned Euler primalizer on the fixed-real stratum | nonlinear replacement `A -> P_+A` |
| `dot P_+` | derivative induced by moving the reduction | complete field-space derivative of the action |
| pure-frame covariance | simultaneous transition of tensors, residual and primalizer | physical stationarity or gauge reduction |
| full `U(64,64)` | source-sized parent unitary connection | two independent `U(32,32)` connections |
| two `U(32,32)` halves | block-preserving reduction inside the full parent | automatically selected action parent |

The first row is the key correction to the predecessor's next-gate wording.
A global frame is not required to globalize an associated endomorphism.  The
underlying Spin structure is still required and remains part of GU's supplied
starting data.

## Exact associated-bundle theorem

If local target transitions are `rho(g_ab)` and

```text
tau_b = rho(g_ab) tau_a rho(g_ab)^-1,
```

then polynomial functoriality gives

```text
P_b = rho(g_ab) P_a rho(g_ab)^-1.
```

The exact certificate tests this on three patches with adjacent negative-plane
quarter turns.  The two transition generators do not commute.  Direct and
sequential transport agree on every one of the `392` real target-coordinate
basis vectors; the involution and projector intertwine on all three overlaps.
The fibrewise projector has real rank `196`.

No global Spin section is chosen.  Replacing a local lift `S` by `-S` leaves
adjoint transport unchanged:

```text
(-S) X (-S)^-1 = S X S^-1.
```

Therefore the centre-sign ambiguity cannot obstruct this projector's descent.
This does not eliminate other topology: it uses the already-admitted Spin
principal bundle and global trace-`q` section rather than proving their
existence for an arbitrary bare four-manifold.

## Exact moving-primalizer theorem

Differentiate the transported family

```text
tau(t) = R(t) tau(0) R(t)^-1,
P(t)   = R(t) P(0) R(t)^-1.
```

For the exact generator taking `q_13` toward `q_12`, the certificate proves on
the complete target carrier:

```text
dot P P + P dot P = dot P,
P dot P P = 0,
(1-P) dot P (1-P) = 0,
dot P U + P dot U = d/dt(P(t)U(t)).
```

Thus `dot P` exchanges the fixed and anti-fixed sectors rather than adding a
new diagonal selector.  Its exact rank is `56`.  Freezing `P` makes the last
identity fail on `56` basis vectors, so the derivative is a genuine required
owner term rather than bookkeeping.

The transport generator is skew for the selected real action pairing and
`dot P` is self-adjoint at first order.  With the moving fixed residual `y(t)`,

```text
dot P y + P dot y = dot y,
d/dt B_R(P(t)U(t),y(t)) = 0.
```

The latter identity passes on every carrier basis direction and includes two
nontrivial cancellations between the moving projected residual and moving
target terms.

## What was closed and what remains

Closed at exact conditional grade:

- `P_+` descends as a sign-insensitive associated-bundle endomorphism;
- no chosen global Spin frame or additional datum is needed for that descent;
- the pure-frame moving term is `dot P_+=[L,tau]/2`;
- differentiated idempotency, off-diagonal exchange, action adjointness and
  moving first-variation covariance hold exactly.

Still open:

- whether the operative source connection is full `U(64,64)`, its
  block-preserving two-`U(32,32)` reduction, or another compatible parent;
- identification of the associated transition with source `epsilon`;
- arbitrary moving `q`, metric, DeWitt, Hodge, Shiab, connection, observation
  and field variations rather than a pure frame orbit;
- formal adjoint/Green return, the Euler operator and presymplectic
  preboundary current;
- physical vacuum, kinetic normalization, spectrum, Yukawa placement,
  BV/domain, index and generation count.

The v0.206 nonlinear fence is unchanged.  Away from an `H_q`-fixed residual,
the anti-fixed action sector remains nonzero, so `A -> P_+A` is not a derived
nonlinear field equation.

## Source return and accounting

The source confirms an `epsilon`-conjugated moving Clifford frame and the
residual norm-square/adjoint grammar.  It does not print the repository
`H_q`, `P_+`, the associated-endomorphism proof or `dot P_+`.  Those are
repository-derived consequences inside the selected conditional K77 action.

No field, parameter, datum, function-valued slot, quotient or selector is
added.  P1/P2/P3 remain unchanged and unused.  Three ledger rows migrate only
in distance and evidence; headline verdicts, residue, forks, five quotients,
canon and public posture do not move.

## Adaptive specialist review

- **Principal-bundle geometry:** removed the false requirement for a chosen
  global frame and required a genuine overlap/cocycle test.
- **Clifford/Krein geometry:** kept the centre-sign cancellation, involution
  transport and indefinite action adjoints exact.
- **Category/functoriality:** required direct and sequential descent on a
  noncommuting triple overlap.
- **Variational bicomplex:** forced `dot P_+` to appear with the moving
  residual instead of being priced as a new datum.
- **Symplectic geometry:** refused to identify this fibrewise derivative with
  the presymplectic potential or a BFV quotient.
- **Analytic review:** retained the formal adjoint, Green domain, spectrum and
  positivity as open.
- **Source criticism:** kept source `epsilon` and the full/two-half unitary
  parent separate from the repository construction.
- **Contrary path:** the frozen-projector plant fired on all `56` moving
  directions while the non-fixed residual control from v0.206 remains live.

## Next gate

Assemble the arbitrary-field derivative packet

```text
dot P_+ + dot Hodge + dot Shiab + dot connection + dot observation + dot fields
```

inside the selected residual-square action, including the gauge-rotated
Levi-Civita/soldering owner and the composite variation of trace `q_g=g/2`.
Then derive the complete Euler and presymplectic preboundary classes.  Run the
full-`U(64,64)` and block-two-half parents as separate comparators; do not
collapse them by notation or identify their connection with the K77 vector
connection without the missing compatibility map.
