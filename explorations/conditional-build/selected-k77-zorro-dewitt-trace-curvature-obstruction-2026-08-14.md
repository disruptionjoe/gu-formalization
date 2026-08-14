---
artifact_type: exact_reconstruction_scoped_native_background_obstruction
created: 2026-08-14
status: BOTH_NONZERO_TAUTOLOGICAL_BRANCHES_KILLED_FOR_CANONICAL_ZORRO_DEWITT_CONNECTION_METRIC__SOURCE_GLOBAL_BACKGROUND_OPEN
source_return: SOURCE_CONFIRMS_ABSTRACT_METRIC_TO_LC_TO_INDUCED_Y_CHAIN__SOURCE_SILENT_ON_COORDINATE_FORMULA_AND_UNIQUENESS__REPOSITORY_DERIVES_CANONICAL_RECONSTRUCTION_OBSTRUCTION
lane_id: SRC-RES-COH-01
registry: lab/process/selected-k77-zorro-dewitt-trace-curvature-obstruction.json
canon_verdict_change: none
ledger_row_changes: none
---

# K77 Zorro/DeWitt trace-curvature obstruction

## Result first

The repository already had more Zorro geometry than the preceding native
curvature-jet gate credited.  The B2C15P reconstruction builds the standard
Levi-Civita-horizontal connection metric

```text
G_Y = h_ij dx^i dx^j + D_h(theta,theta),
theta = dh-C(Gamma^h)dx,
```

with the trace-reversed DeWitt fibre form.  Porting its pure-vertical geometry
from the old `(9,5)` convention to the authorial
`(1,3)+(6,4)=(7,7)` horn gives a decisive exact mismatch:

- the normalized metric-trace line is a flat factor of the DeWitt fibre;
- all nine labelled trace--traceless vertical curvature planes vanish;
- for either nonzero frozen branch `B=b Phi1`, the same nine curvatures are
  `2 b^2 gamma_trace gamma_a` and are nonzero.

Gauge conjugation preserves zero.  Therefore neither exact `b_plus` nor
`b_minus` branch can be a gauge transform of the distinguished connection in
this canonical reconstruction.  The mismatch occurs at point-curvature grade,
so a labelled first-jet calculation is unnecessary for these two candidates.

This is a reconstruction-scoped kill, not a source-global no-go.  The 2021
draft states the metric-to-Levi-Civita-to-induced-`Y` chain but does not print
the induced metric, connection formula or a uniqueness theorem.  A different
completion of that sketch remains logically open.

## Why the trace planes vanish

Write a fibre metric as

```text
h = exp(2s) h_hat,       det(h_hat) fixed,
```

and decompose a metric variation by

```text
h^-1 delta h = 2 delta(s) I + h_hat^-1 delta h_hat,
tr(h_hat^-1 delta h_hat)=0.
```

For the four-dimensional trace-reversed form

```text
D_h(A,B)=tr(AB)-1/2 tr(A)tr(B),
```

the scale/traceless cross term vanishes and the scale coefficient is constant.
The fibre is therefore locally a metric product of its scale line and the
unimodular metric space.  Its mixed curvature is identically zero.  In the
exact DeWitt frame, column six is the sign-equivalent half-metric line, has
norm `-1`, is orthogonal to the other nine directions, and all nine mixed
curvature matrices vanish.

The exact coordinate calculation independently verifies:

```text
D_{-g}=D_g;
inertia(D)=(6,4);
24/45 coordinate vertical planes are curved;
each nonzero intrinsic fibre-curvature endomorphism has rank 6;
9/9 trace--traceless frame planes have curvature zero.
```

An independent replay of the older complete fourteen-dimensional connection-
metric jet contracts its full ambient Riemann tensor with the trace direction
and returns no nonzero mixed leg (`[]`).  This controls the passage from the
intrinsic fibre calculation to the reconstructed `Y` connection at the
observation-section normal jet.

Thus the result is not the tautology that the reconstructed connection is
flat.  Its traceless sector is curved; only the canonical scale factor is flat.

## Why both frozen branches fail

On the frozen tautological connection,

```text
B_u=b gamma_u,
F_B(u,v)=b^2[gamma_u,gamma_v].
```

For an orthogonal trace direction `q` and any of the nine orthogonal fibre
directions `e_a`, Clifford anticommutation gives

```text
F_B(q,e_a)=2 b^2 gamma_q gamma_a != 0
```

whenever `b != 0`.  Both exact scales

```text
b_plus  = 1/208-sqrt(3)/312,
b_minus = 1/208+sqrt(3)/312
```

are nonzero.  An internal gauge transformation conjugates the value of the
curvature but does not relabel its tangent two-plane arguments, and the zero
endomorphism cannot be conjugated to a nonzero one.  The two candidates hence
fail the necessary curvature-orbit identity independently.

## Source and reconstruction boundary

Draft equations `(3.16)`--`(3.17)` say that the observed metric on `X` induces
its Levi-Civita connection and, through the Zorro chain, a metric and
connection on `Y`.  The draft also says each observation induces that upstairs
pair.  It does not provide the coordinate formula used here or prove it is the
only natural construction.

Accordingly:

```text
canonical connection-metric reconstruction:  BOTH BRANCHES KILLED
old B2C15P (9,5) versus K77 sign port:          VERTICAL RESULT INVARIANT
source-global Zorro completion:                OPEN
current constructed native background bank:   EMPTY
all possible action-stationary backgrounds:    OPEN
```

Any rival completion that is meant to rescue one of these same branches must
now do something precise: produce nonzero mixed curvature between the natural
metric-trace line and all nine complementary vertical directions, or explain
why the distinguished connection is not the Levi-Civita connection of the
standard Zorro connection metric.

## Correct successor

The result changes the construction target.  Do not keep fitting an arbitrary
`B=b Phi1` to the source-dependent connection.  Instead either:

1. hold the canonical Zorro connection `B_Z` fixed and solve the source Euler
   residual nonhomogeneously for `T=varpi-B_Z` and `varpi`; or
2. derive a different Zorro completion from explicit axioms and test whether
   it has the nonzero mixed trace curvature demanded by either old branch.

The first route has higher immediate physics value because `B` is dependent
while `varpi` is the source-native independent connection.  It asks the action
to find a vacuum rather than asking the geometric base connection to imitate a
homogeneous Clifford ansatz.

## Scientific ceiling

No global source uniqueness, action-stationary vacuum, first-jet equality,
functional domain, positivity, SR-2 factorization, physical cohomology,
W/mirror choice, generation count, external datum, canon verdict, residue,
quotient or public-posture change follows.

## Reproduction

```sh
sage -python \
  tests/channel-swings/selected_k77_zorro_dewitt_trace_curvature_obstruction_probe.py
```

The exact certificate passes `35/35`.
