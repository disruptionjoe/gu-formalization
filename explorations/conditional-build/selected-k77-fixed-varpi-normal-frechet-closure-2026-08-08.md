---
artifact_type: build_compose_result
created: 2026-08-08
status: LOCAL_FIXED_VARPI_DG_UPSILON_EXACT__COMMON_FIELD_FORMAL_ADJOINT_GREEN_OPEN
source_return: SOURCE_CONFIRMS_TWO_CONNECTION_SOURCE_COORDINATES__SOURCE_SILENT_FIXED_VARPI_NORMAL_FRECHET_CLOSURE
canon_verdict_change: none
---

# Selected K77 fixed-varpi normal Frechet closure

## Result in plain English

The missing metric derivative becomes much smaller when the action's actual
independent variables are respected.

The source coordinates are the metric `g`, an independent connection
`varpi`, and the gauge/frame variable `epsilon`.  Augmented torsion is

```text
T = varpi - B_LC(g,epsilon),
A = B_LC + T = varpi.
```

Therefore a partial metric variation holds `varpi` and `epsilon` fixed:

```text
delta T = -delta B_LC,
delta A = 0,
delta F_A = 0.
```

That last zero is not an assumption.  Expanding

```text
F_A = F_B + d_B T + T wedge T
```

produces three separately nonzero derivatives, but they cancel exactly.  The
tempting alternative—differentiate only the stationary shorthand
`F_A*=T* wedge T*`—gives a false curvature term because that equality is a
selected on-shell relation, not the off-branch definition of curvature.

Together with v0.94, this closes the **local fixed-varpi metric block** of the
raw residual.  Coefficient motion cancels at `Upsilon*=0`, curvature contributes
zero, and the surviving term is the Hodge-primalized
`-delta B_LC` augmented-torsion response.  It has rank six on the timelike,
spacelike and null physical transverse metric subspaces.

## Layer 0

| phrase | exact object | not identified with |
| --- | --- | --- |
| independent connection | `varpi`, an action coordinate | its observed pullback or `T` |
| augmented torsion | `T=varpi-B_LC` | an independently varied torsion tensor |
| total connection | `A=B_LC+T=varpi` | `B_LC` or `T` separately |
| `F_A*=T* wedge T*` | selected stationary identity on the flat branch | off-branch definition of `F_A` |
| `D_g Upsilon` | partial derivative at fixed independent `varpi,epsilon` | full common-field Ward column |
| moving observation | dependent complete-germ receiver | a second metric/action field |
| raw residual zero | `Upsilon*=0` | generally nonzero action Euler covector |

This distinction is load-bearing.  Differentiating an on-shell identity as if
it defined the off-shell field is the exact error the expanded curvature
control catches.

## Exact two-connection theorem

An exact nonabelian polynomial witness uses live `B`, `T` and `delta B=beta`.
Under `delta T=-beta`, all of

```text
delta F_B,
delta(d_B T),
delta(T wedge T)
```

are nonzero, while their sum and the direct `delta F_(B+T)` are zero.
Freezing `T` makes `A` move and produces a nonzero curvature derivative, so
the result is not a vacuous zero family.

## Complete covariant Levi-Civita first jet

In symmetric coframe gauge the full local covariant variation is

```text
delta omega_(mu ab)
  = 1/2 (nabla_b h_(mu a) - nabla_a h_(mu b)).
```

As a map from the forty components of `nabla h` to the twenty-four-component
horizontal Lorentz-connection carrier, it has exact rank `20`.  This corrects
the pre-wave expectation of rank `24`: metric-derived torsion-free
Levi-Civita variations occupy a proper rank-twenty subspace of the unrestricted
connection carrier.

For any fixed nonzero symbol covector, the map has rank `9`; its sole
metric-value kernel is inside the four-dimensional diffeomorphism image.  Its
restriction to the six-dimensional physical transverse complement is
injective in all three causal classes.

Writing the formula with `nabla h` is the complete local lower-order
covariantization.  Background connection coefficients are contained in the
covariant derivative; no free zeroth-order coefficient or extra soldering
field is introduced.  This is a local jet theorem, not a global analytic or
section-existence theorem.

## Observation and soldering

Let `O(g)` be the complete observation equation receiver.  Since the raw
residual vanishes at the selected point,

```text
D_g[O(g) Upsilon(g)]
  = (D_g O) Upsilon* + O* D_g Upsilon
  = O* D_g Upsilon.
```

The receiver is invertible at complete-germ grade, so it preserves the
rank-six transverse block.  A planted nonzero residual makes `(D_g O)Upsilon`
live, proving that the term disappears here because `Upsilon*=0`, not because
observation was frozen.

This cancellation does **not** transfer to the action Euler covector used by
the Green construction, which is generally nonzero.  The v0.65 moving-action
receiver therefore survives unchanged.

## What is now closed

On the conditional Spin-native selected K77 parent, the local fixed-varpi
metric partial derivative has the coefficientwise form

```text
D_g Upsilon[h]
  = O* [ *(kappa_1 (-D_g B_LC[h])) ].
```

Here the already-proved v0.94 coefficient packet and the new `delta F_A=0`
identity have been included.  Its physical transverse symbol rank is six for
timelike, spacelike and null covectors.  No coefficient was fitted and no new
normal-jet object was supplied.

The complete common-field Jacobian still includes the independent
`D_varpi Upsilon` and gauge/epsilon directions.  Their Ward graph was built in
predecessors, but the combined action-density formal adjoint has not yet been
assembled with the v0.92 residual pairing.

## Inline specialist assessment

- **Differential geometry:** the two-connection identity and covariant
  Levi-Civita first jet are the right source-native objects; rank `20`, not
  `24`, is the torsion-free image.
- **Symplectic geometry:** closing one partial Frechet block does not produce a
  presymplectic current.  The common-field Green identity and
  antisymmetrization still come next.
- **Variational PDE:** the local first-order operator is complete in covariant
  jet form.  Hyperbolicity, closed domains and global lower-order estimates
  remain open.
- **Real Clifford/Krein:** the exact K77 residual pairing remains usable but
  is indefinite; no positive fundamental symmetry follows.
- **Complex/path-integral:** no complexification, contour, measure, saddle or
  reflection-positivity inference appears.
- **Source criticism:** Weinstein supplies the two-connection/augmented-
  torsion grammar.  The cancellation and rank theorem are repository-derived.
- **Constraint accounting:** zero new fields, parameters, functions, quotients
  or external datum pieces.

## Hostile review and boundary

The hostile verdict is
`SURVIVES_WITH_SCOPE_NARROWING__LOCAL_FIXED_VARPI_RAW_RESIDUAL_BLOCK_ONLY`.
It rejects three stronger readings:

1. `F_A*=T* wedge T*` may not be differentiated as an off-shell definition;
2. rank `20` may not be advertised as the full rank-`24` connection carrier;
3. the raw-residual observation cancellation may not be transferred to the
   nonzero action Euler/Green owner.

No Einstein equation, cosmology, mass, chirality, generation count, quantum
theory, global solution, BV/BFV quotient or positive domain is claimed.

## Frontier delta

Conditions closed: `4`; opened: `0`.

1. fixed-varpi component-normal `delta T`;
2. expanded component-normal `delta F_A` cancellation;
3. complete rank-twenty covariant Levi-Civita first-jet image;
4. dependent moving-observation term at raw residual zero.

Remaining named condition: `1`.

1. Assemble the full common-field operator with the conditional v0.92
   residual pairing, derive its action-density formal adjoint and Green
   concomitant, then test the common analytic/symplectic domain.

P1/P2/P3 remain unused.  Curt remains formally separate.  The third lane is
not promoted.  No verdict, residue, quotient, signature, canon or public
posture moves.

## Evidence

- `tests/channel-swings/selected_k77_fixed_varpi_normal_frechet_closure_probe.py`
  — `58/58 PASS`.
- `tests/channel-swings/selected_k77_fixed_varpi_normal_frechet_closure_independent.sage`
  — `18/18 PASS`.
- `lab/process/selected-k77-fixed-varpi-normal-frechet-closure.json`.
- `lab/process/hostile-reviews/2026-08-08-selected-k77-fixed-varpi-normal-frechet-closure-review.md`.
