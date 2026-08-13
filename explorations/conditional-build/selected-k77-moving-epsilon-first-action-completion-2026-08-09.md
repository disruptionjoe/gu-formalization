# Selected K77 moving-epsilon first-action completion

Date: 2026-08-09
Disposition: `SELECTED_SPIN_321_EPSILON_CLOSURE_KILLED__EXPANDED_TANGENT_OR_SOURCE_DERIVED_EQUATION_QUOTIENT_REQUIRED`

## Result in plain English

The earlier fixed-operator calculation found that the 91 primitive epsilon
directions leak into 88 off-slice grade-two equations.  The possible repair
was that the omitted epsilon-dependent geometry might cancel that leakage.

It does not.  This wave adds both missing pieces:

1. the lower Cartan term `[B,eta]` in `D_B eta`; and
2. the derivative of every occurrence of the moving `Phi(epsilon)`/Shiab map
   in the first-action `E_T` covector.

On the actual real K77 exterior/Clifford carrier, every one of those correction
terms is exactly zero against all 1,274 grade-two equation covectors, for all
91 epsilon generators.  Therefore the complete selected-Spin primitive
epsilon block is coefficientwise identical to the fixed principal block:

| block | full rank | horizontal rank | off-slice rank |
|---|---:|---:|---:|
| fixed `q eta` | 91 | 6 | 88 |
| lower Cartan correction | 0 | 0 | 0 |
| all moving-Shiab corrections | 0 | 0 | 0 |
| total epsilon block | 91 | 6 | 88 |

This holds on both exact `QQ(sqrt(3))` branches and timelike, spacelike and
null representatives.  Timelike and spacelike totals have `403` nonzero
entries (`385` off-slice); null has `806` (`770` off-slice).

The 321-field selected-Spin truncation is therefore not Hessian-closed.  The
ten metric columns cannot cancel a response attached to 91 distinct epsilon
input columns.  The next physical construction must either expand the tangent
or derive an action/source-owned quotient of the off-slice equations.  This
does **not** automatically promote all 1,571 low-grade coordinates.

## Layer 0

| phrase | object decided here | object kept distinct |
|---|---|---|
| primitive epsilon | independent source variation at fixed `varpi`: `delta B=D_B eta`, `delta T=-D_B eta` | diagonal gauge characteristic and boundary charge |
| moving epsilon geometry | lower Cartan plus every differentiated epsilon-dependent Shiab occurrence | ten metric/density/Hodge motions |
| grade-two closure | image in the complete `1,274=24+1,250` equation dual | a BV quotient or analytic domain |
| selected parent | grade-preserving real `Spin(7,7)` carrier | two `U(32,32)` halves and full `U(64,64)` |
| first action | source-shaped transgression Hessian | raw residual and residual-square Hessian |

The selected Spin action preserves Clifford grade.  On these stationary
branches its grade-two first variation is zero, so co-moving frame or
observation receiver transport acts on the zero covector and cannot supply a
hidden epsilon correction.  A full-unitary parent may mix the Weyl/grade
blocks and is not covered by this theorem.

## Prior-art composition

The apparent breadth of the old moving-geometry work hid four different
objects:

- v0.66 was a finite noncyclic toy mixed Hessian;
- v0.67 built the ten metric geometry bank but not this action Hessian;
- v0.94/v0.97 established raw-residual naturality, not the first-action
  Hessian; and
- v0.106 serialized only the outer moving-Shiab first-action term.  It was
  rank 91 on grade one and zero on grade two.

The new calculation differentiates the inner Shiab occurrence and adds the
lower Cartan term.  Both also vanish on grade two.  Thus v0.106 was incomplete
as a formula but its grade-two zero was not an artifact.

## Exact construction

For `B=b Phi1`, `T=t Phi1`, factor the branch scalars before entering the
carrier.  Writing `X(a,v)=a wedge v + v wedge a`, the source derivative has

```text
delta B = q eta + b[Phi1,eta],
delta T = -delta B,
delta Phi_i = [Phi_i,eta].
```

The probe factors the full mixed derivative into fixed-principal, lower-Cartan
and moving-Shiab rational tensors, then evaluates the two algebraic branches
only at sparse-column assembly.  This keeps the carrier operations over exact
`Fraction` arithmetic and the final ranks over `QQ(sqrt(3))`.

The independent Sage route does not read the primary columns.  It rebuilds
the v0.106 carrier and verifies six separate rational identities for every
generator/receiver pair:

```text
91 * 1274 = 115,934 checks per identity,
6 identities = 695,604 exact scalar checks.
```

All pass.  The grade-one v0.106 rank-91 block is the nonvacuity control: the
moving-Shiab operator is live, but its grade-two pairing is forbidden on this
selected carrier.

## Source return

- `SOURCE-CONFIRMS`: `T_omega=varpi-epsilon^-1 d_0 epsilon`, the primitive
  `D_B eta` chain and conjugated moving `Phi_i(epsilon)`/Shiab grammar.
- `REPO-DERIVES`: the complete selected-Spin epsilon/grade-two first-action
  mixed block and its exact causal/branch ranks.
- `SOURCE-SILENT`: the 321 truncation, an equation quotient, expanded action
  parent and physical interpretation.

## Hostile and specialist disposition

- **Layer-0/source:** the result kills a selected-parent truncation, not GU.
- **Representation:** the zero correction is grade-sensitive; it is not
  automatically portable to two `U(32,32)` halves or full `U(64,64)`.
- **Variational bicomplex:** every explicit epsilon owner in `D_epsilon E_T`
  is included; first-action and residual-square Hessians remain separate.
- **Symplectic geometry:** primitive epsilon source motion is not silently
  quotiented as gauge, and unrestricted boundary charge remains live.
- **Analytic/Krein:** finite exact ranks imply no positive energy, contour,
  hyperbolicity, closed domain or unitarity.
- **Accounting:** no field, coefficient, quotient or datum was added;
  P1/P2/P3 remain unused.

## Process finding and mandatory successor

The first implementation recursively rebuilt the entire v0.122 bank before
recomputing it.  It was stopped.  The repaired implementation imports the
v0.106 carrier and factors shared tensors once, cutting the exact path from an
unbounded duplicate replay to minutes.

Before another heavy Hessian wave, the next Run must create a durable,
versioned exact coefficient-bank artifact/API with source-revision and
construction hashes, stale-cache rejection and a bounded equivalence replay.
An unverified matrix dump does not satisfy this gate.

## Progress and next gate

```text
Ledger v0.123 — 82/82 active target rows mapped (100%)
32 SAME · 19 DIFFERS · 26 NEEDS · 5 OVER-DETERMINED
Residue — 84 continuous; conditional parent range 84..86
Scoped quotients — 5

headline_delta: none
conditions_closed: 3
  - lower Cartan epsilon/grade-two contribution decided: zero
  - every moving-Shiab epsilon/grade-two contribution decided: zero
  - selected-Spin 321 epsilon closure decided: killed
conditions_opened: 0
remaining_named_conditions: 2
  - build the durable exact coefficient-bank API
  - then complete the ten metric source Hessian and choose expanded tangent
    versus a source/action-owned equation quotient
```

Primary probe: `399/399 PASS`.  Independent Sage: `6/6` structural identities
and `695,604` exact scalar checks pass.
