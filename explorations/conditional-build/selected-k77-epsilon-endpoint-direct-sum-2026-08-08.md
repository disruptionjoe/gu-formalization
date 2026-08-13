---
artifact_type: construction_result
created: 2026-08-08
status: EPSILON_ENDPOINT_TRACE_AND_DIRECT_SUM_40_OF_40_EXACT__ACTION_MOMENTUM_WELD_OPEN
lane: "1"
functional_channels: [BUILD, COMPOSE, SOURCE, VERIFY]
source_return: SOURCE-CONFIRMS__EPSILON_FIELD_AND_PRIMITIVE_CHAIN__SOURCE-SILENT__BFV_IDENTIFICATION__REPO-DERIVES__LOCAL_ENDPOINT_TRACE_AND_DIRECT_SUM_ONLY
ledger_rows: [LT-GR1, LT-GR2b, LT-GR3, LT-GR5, LT-GR6]
scripts:
  - tests/channel-swings/selected_k77_epsilon_endpoint_direct_sum_probe.py
  - tests/channel-swings/selected_k77_epsilon_endpoint_direct_sum_independent.sage
registry: lab/process/selected-k77-epsilon-endpoint-direct-sum.json
---

# Selected K77 epsilon endpoint direct-sum gate

## Result first

Two parts of the v0.73 successor close, and one action-level equality remains.

First, the requested two continuum endpoint evaluations were already present
in the repository.  The v0.25 primitive-epsilon Green identity has independent
left and right traces,

\[
  \eta_3 e_2-\eta_0 e_0,
\]

and the affine collar interpolation
`eta(t)=(1-t)eta0+t eta3` proves that the two trace values are locally
independent.  This is a composition-debt correction: the endpoint map did not
need to be rebuilt.

Second, applying two independent copies of the exact v0.72 group-edge
dressing avoids the single-holonomy loss.  On the exact matrix fixture the
direct-sum map has rank 16 on 24 variables; its oriented pulled-back two-form
has rank 16, and its eight-dimensional kernel is exactly the two independent
endpoint gauge orbits.  At identity its potential is

\[
  p_0\,\delta(x_0-u_0)-p_2\,\delta(x_3-u_3).
\]

Direct sum over the ten already-proved nonzero K77 normal weights gives the
full v0.70 result:

```text
extended dimension: 60
presymplectic rank: 40
endpoint-gauge kernel: 20
local quotient dimension/rank: 40/40
```

The hostile review stopped the initially tempting stronger conclusion.  The
v0.25 boundary coefficient is `i_n(E_B-E_T)`, while v0.69 writes the contact
coefficient as `p=KT`.  Matching the two oriented potentials requires

\[
  e_0=p_0,\qquad e_2=p_2,
\]

with no `p0=p2` restriction, but the current artifacts do not derive this
coefficientwise equality on the selected K77 action.  Equal types and signs
are not an action weld.  Therefore epsilon's boundary restrictions are the
right local edge-coordinate candidate, and the direct-sum geometry is exact,
but epsilon does **not yet own** the v0.70 canonical pair.

## Layer 0

| phrase | exact object | not identified with |
| --- | --- | --- |
| source epsilon | existing bulk group-valued field | a newly introduced BFV edge field |
| epsilon trace | two local collar boundary values | arbitrary global extension through every bundle sector |
| `eta` | logarithmic field-space variation of epsilon | a connection holonomy |
| epsilon Green momentum | `i_n(E_B-E_T)` | contact momentum `p=KT` before the weld |
| direct-sum dressing | two independent endpoint cotangent copies | one source-to-target holonomy |
| local quotient | exact `60/40/20 -> 40/40` collar model | global BFV phase space or common analytic domain |

The load-bearing distinction is the two momenta.  The equality
`i_n(E_B-E_T)=p_KT` is now the entire remaining local ownership gate.

## Source return

Weinstein's sources supply epsilon as a group-valued field and the primitive
two-connection/moving-Shiab chain.  They do not print the BFV boundary
identification or the coefficient weld used here.

```text
SOURCE-CONFIRMS: epsilon field and primitive chain
SOURCE-SILENT:   BFV identification and contact-momentum weld
REPO-DERIVES:    local two-endpoint trace and direct-sum dressing only
```

## Exact endpoint and symplectic calculation

The collar trace Jacobian with respect to `(eta0,eta3)` is the identity.  A
constant-collar plant has rank one and therefore catches the forbidden
diagonal-only endpoint assumption.

For each endpoint, with right action

\[
  x_i\mapsto x_i h_i,\quad u_i\mapsto u_i h_i,
  \quad p_i\mapsto p_i h_i^{-T},
\]

the dressed variables are `q_i=x_i u_i^{-1}` and
`pi_i=p_i u_i^T`.  Each copy has pulled-back rank eight and gauge kernel four.
Their oriented direct sum has rank 16 and kernel eight.  A planted inert
right cotangent motion is not characteristic.

The scalar identity tangent has variables `(x0,x3,p0,p2,u0,u3)` and form

\[
  \delta p_0\wedge\delta(x_0-u_0)
  -\delta p_2\wedge\delta(x_3-u_3).
\]

It has rank four and exactly the two endpoint-shift directions as kernel.
Ten nonzero scalar multiples therefore have rank 40 and kernel 20.  The v0.73
single-holonomy `20/20` theorem remains true as a compression no-go; it is not
retracted.

## The remaining action weld

The exact sign comparison gives the necessary and sufficient local condition

```text
epsilon Green:   eta3 e2 - eta0 e0
edge potential:  eta3 p2 - eta0 p0
weld:            e0=p0 and e2=p2
```

No relation between `p0` and `p2` is required.  What is missing is not another
endpoint field or another symplectic construction.  It is the coefficientwise
normal evaluation of the actual selected action's `E_B-E_T`, compared with
the already-built `KT` contact momentum under the same invariant trace,
orientation and observation receiver.

## What changed

- the two continuum endpoint evaluations close at local collar grade;
- direct-sum nonlinear dressing recovers the full `40/40` quotient;
- the single-holonomy `40 -> 20` negative result is preserved;
- the missing local owner is narrowed to one explicit action-momentum weld;
- v0.70's boundary-coordinate cost is not retyped away before that weld;
- no verdict, residue, quotient, datum or public posture moves.

```text
Ledger v0.74 — 82/82 active target rows mapped (100%)
32 SAME · 19 DIFFERS · 26 NEEDS · 5 OVER-DETERMINED
Residue — 84 continuous + >=19 function-valued + 9 forks
Quotients ranked — 5 scoped
headline_delta: NONE
frontier_conditions_closed: 2
frontier_conditions_opened: 1
remaining_named_conditions: 2
```

## Seven-axis disposition

- **Layer 0:** field/trace/variation, Green/contact momentum and
  endpoint/holonomy objects are separated.
- **L1 syntactic:** both predecessor potentials and their exact coefficient
  match condition are explicit.
- **L2 type:** group coordinates, cotangents, action Euler traces and K77
  normal weights remain distinct.
- **L3 algebraic:** collar trace rank, direct-sum rank/kernel, `40/40` recovery,
  signs and planted failures pass exactly over rationals and independently in
  Sage.
- **L4 geometric:** local collar and identity-component endpoint restrictions;
  global `tau_A0` overlap and bundle extension remain open.
- **L5 variational:** the exact weld condition is located but not yet proved
  coefficientwise on the selected action.
- **L6 analytic:** no polarization, charge algebra, common Green/Krein domain
  or global BFV construction is inferred.
- **L7 physical:** no positivity, unitarity, Einstein, Standard Model or
  cosmology conclusion is claimed.

## Constraint fence

```text
new bulk fields: 0
new external datum: 0
new coefficients or selectors: 0
v0.70 boundary coordinates retyped as existing epsilon traces: not yet
new scoped quotients: 0
P1/P2/P3 consumed: 0
```

Curt remains formally separate inside the Eric lane.  No third lane, claim
status, canon verdict or public posture is promoted.

## Next gate

Compute `i_n(E_B-E_T)` and `p=KT` coefficientwise on the same selected K77
normal/contact bank, with the invariant trace, endpoint orientation and
observation receiver fixed.  If the two endpoint equalities pass, epsilon owns
the existing v0.70 edge coordinates locally and the next gate is full
`tau_A0` overlap/global BFV descent.  If they fail, retain the direct-sum
geometry but keep the boundary edge field independent.
