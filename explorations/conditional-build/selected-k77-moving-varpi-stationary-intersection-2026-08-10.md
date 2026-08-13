---
artifact_type: construction_result
created: 2026-08-10
status: exact_conditional_result
canon_verdict_change: none
---

# Selected K77 moving-`varpi` stationary intersection

## Result

The fixed-fixture conclusion from v0.156 does not extend to the actual
source-stationary connection.  Both canonical displayed-southeast-zero
trace-`q`/Pin candidates have exact rank/nullity

```text
rank 1792, nullity 128
```

on **both** nonzero bosonic stationary branches.  The kernel is an explicit
graph between `Omega0(S)` and the gamma-trace image in `Omega1(S)`.  Its
one-form component is annihilated by the Rarita--Schwinger projector, by the
proposed `W` projector and by the mirror projector.  It is therefore not the
previously proposed `W`/mirror carrier.

This is the first exact composition in the repository of all three of these
ingredients:

1. the componentwise draft-9.16 four-field operator grammar;
2. the actual tautological source family `varpi=(b+t) Phi1`;
3. the already-certified nonzero bosonic stationary amplitudes.

It establishes an algebraic stationary intersection.  It does **not** yet
establish a differential solution, BV cohomology, a closed-domain zero mode,
chirality, an index, three generations or mirror removal.

## Layer 0

The v0.156 fixture was decomposable:

```text
varpi_i = a_i P.
```

The bosonic source branches instead use the tautological one-form

```text
Phi1 = sum_i e^i gamma_i,
varpi_i = s gamma_i,
s = b+t.
```

The fourteen coefficients are different Clifford matrices.  Treating the
second object as the first asks a different question.  The componentwise
extension used here is not a fitted replacement: decomposable one-forms span
`T* tensor End(S)`, and the extension is the unique bilinear map that reduces
to the accepted v0.156 formula on every decomposable control.

Five distinctions remain load-bearing:

- fixed decomposable fixture versus tautological source connection;
- zero-order algebraic block versus the full differential operator;
- finite kernel versus BV cohomology and a closed analytic domain;
- a branch that is stationary versus a source mechanism selecting its
  amplitude;
- the displayed southeast-zero block versus the source-admitted nonzero
  southeast rival.

The selected real-Spin parent, Curt's two `U(32,32)` Weyl-half presentation and
the later full `U(64,64)` principal group also remain separate.  The present
tautological connection is source-owned in the selected construction; the
calculation does not identify the three action parents or port the branch to
the block-preserving two-half domain.

## Componentwise operator

For connection components `V_i in End(S)`, the unique linear extension of the
accepted decomposable upper-left map is

```text
R_rc(V) = delta_rc sum_k gamma_k V_k - gamma_c V_r.
```

The upper-right port stacks the components `V_r`.  With spinor pairing `B`
and ambient signs `eta_r`, the action-tied lower row is

```text
L_r(V) = -eta_r B V_r^T B.
```

The two surviving source-faithful candidates place the Pin intertwiner on the
column or row side.  Exact controls recover all three v0.156 decomposable
parent witnesses coefficient-for-coefficient; a nondecomposable planted test
fails that collapse.

## Exact rank and graph theorem

At unit tautological scale, both candidates have

```text
upper-left rank 1792
port rank        128
lower-row rank   128
full rank       1792
full nullity     128.
```

Every displayed-zero block is linear in `varpi`, so the rank and nullity are
identical for every nonzero scalar `s`.

The result is characteristic-zero exact.  Let

```text
I_i = (eta_i/12) gamma_i.
```

The two 128-column kernel graphs have lower component the identity and upper
components obtained from `I_i` by the respective column-Pin or row-Pin rule.
They are annihilated over `QQ(i)`, proving nullity at least 128.  The
1792-square upper-left block is invertible modulo the good prime `1000033`, so
its characteristic-zero determinant is nonzero and the full nullity is at
most 128.  Hence the nullity is exactly 128.

The one-form graph satisfies

```text
Pi_RS graph_1 = 0,
W graph_1     = 0,
Mirror graph_1 = 0.
```

Thus it is entirely gamma-trace.  It pairs an `Omega0(S)` field with its
gamma-trace image in `Omega1(S)`.  This resembles the first two
family-shaped sectors in the public generation narrative, but resemblance is
not a generation count or an observed-family derivation.

## Intersection with the bosonic branches

The two exact source-stationary amplitudes are

```text
s_plus  = (-3 + sqrt(3))/624,
s_minus = (-3 - sqrt(3))/624.
```

Both are nonzero because their numerator norm is `9-3=6`.  By linearity, both
therefore lie on the same exact rank-1792/nullity-128 locus.  The preregistered
horn `BRANCH_INTERSECTION_NONEMPTY` fires for both branches.

The external-tiebreak preregistration does not fire.  These modes project to
zero in both `W` and mirror, so they supply neither symmetric nonzero
`W`/mirror nullities nor an action-owned asymmetry between those carriers.

## What changed

- The inference “the canonical source-faithful operator has no stationary
  modes” is narrowed to v0.156's fixed decomposable fixture.
- The moving-`varpi` rank-loss intersection is closed positively on the
  certified tautological line.
- The physical burden is better typed: couple this exact graph to the
  action-derived fermion current and to the differential BV/Green/domain
  problem.
- `W`, mirror and the southeast-nonzero operator remain separate comparators.

No ledger verdict, residue coordinate, quotient, external datum, P1/P2/P3
assignment, canon result or public posture changes.

## Next gate

Construct the coupled nonzero-fermion Euler system on this exact
`Omega0`--gamma-trace graph, including the action-derived fermion current and
the differential principal/lower-order operator.  Then compute the BV/Green
domain and determine whether any of the 128 algebraic modes survives as
physical cohomology.  Keep `W`, mirror and the source-admitted southeast-
nonzero map as distinct comparators.  Make no count inference before a closed
Fredholm problem exists.

## Evidence

- `tests/channel-swings/selected_k77_moving_varpi_stationary_intersection_probe.py`;
- `lab/process/selected-k77-moving-varpi-stationary-intersection.json`;
- `lab/process/hostile-reviews/2026-08-10-selected-k77-moving-varpi-stationary-intersection-review.md`;
- `lab/sources/selected-k77-moving-varpi-stationary-intersection-source-return-2026-08-10.md`.
