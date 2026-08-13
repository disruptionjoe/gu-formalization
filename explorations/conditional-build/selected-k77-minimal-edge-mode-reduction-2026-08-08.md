---
artifact_type: construction_result
created: 2026-08-08
status: MINIMAL_EDGE_EXTENSION_EXACT__SOURCE_SELECTION_OPEN
source_return: SOURCE-SILENT__BOUNDARY_POLARIZATION_AND_EDGE_MODE__REPO-CONSTRUCTS_CONDITIONAL_MINIMAL_EDGE_EXTENSION
ledger_rows: [LT-GR1, LT-GR2b, LT-GR3, LT-GR5, LT-GR6]
scripts:
  - tests/channel-swings/selected_k77_minimal_edge_mode_reduction_probe.py
  - tests/channel-swings/selected_k77_minimal_edge_mode_reduction_independent.sage
registry: lab/process/selected-k77-minimal-edge-mode-reduction.json
---

# Selected K77 minimal edge-mode reduction

## Result first

The v0.69 boundary charge has an exact, coefficient-unique **conditional local
repair**. It is not a source-selected physical boundary theory.

An ordinary scalar boundary counterterm cannot remove the charge. Replacing a
preboundary potential by `theta + delta B` changes its presymplectic form by
`delta^2 B=0`; in coordinates, the Hessian of `B` is symmetric and its
antisymmetrization vanishes. The two unextended alternatives therefore remain
domain choices: boundary-vanishing gauge parameters, or a zero-charge
restriction on the endpoint momenta. Neither is selected by the checked source
or the action assembled so far.

Adding one boundary coordinate per endpoint gives the minimal extension. For
one K77 normal direction, with bulk boundary coordinates
`(g0,g3,p0,p2)` and new edge coordinates `(phi0,phi3)`, define

\[
\Omega_{ext}
=\delta p_0\wedge\delta(g_0-\phi_0)
-\delta p_2\wedge\delta(g_3-\phi_3),
\qquad
\delta_\xi\phi_i=\delta_\xi g_i=\xi_i.
\]

The most general diagonal two-cell edge ansatz fixes its coefficients uniquely
to `(-1,+1)`. Exact arithmetic gives rank four, kernel dimension two, and the
kernel equals the boundary-gauge span. The quotient coordinates
`(g0-phi0,g3-phi3,p0,p2)` carry a nondegenerate rank-four symplectic form.

Tensoring with the ten already-built nonzero K77 normal coefficients gives:

```text
extended boundary dimension: 60
presymplectic rank: 40
characteristic gauge kernel: 20
conditional quotient dimension/rank: 40/40
new bulk fields: 0
new boundary-coordinate dimension: 20
new continuous coefficient freedom: 0
P1/P2/P3 consumed: 0
```

This earns one new **scoped conditional quotient**. It does not construct the
global labelled `Y14` edge bundle, tilted-equivariant cocycle, physical BFV
phase space, polarization, common analytic domain, or charge algebra.

## Layer 0

| phrase | exact object tested | not identified with |
| --- | --- | --- |
| boundary counterterm | scalar functional `B` shifting `theta` by `delta B` | an independent boundary symplectic one-form with edge coordinates |
| boundary condition | restriction on fields or gauge parameters | extension of the boundary field space |
| edge mode | new boundary coordinate transforming with endpoint gauge | a new bulk field, external datum, or source quotation |
| quotient | finite local characteristic quotient of the six-cell exact form | global BFV phase space or analytic operator domain |
| nondegenerate | rank-four reduced symplectic form | positive Krein/Hilbert metric or unitarity |
| physical gauge | diagonal two-connection endpoint action in the local contact model | globally integrated inhomogeneous gauge group on `Y14` |

The first distinction is load-bearing: `delta B` has zero presymplectic curl,
whereas the edge extension changes the field space and contributes a genuine
boundary two-form.

## Source return

Weinstein distinguishes one-time Hamiltonian evolution from multiple-time
ultrahyperbolic boundary problems and explicitly calls the upstairs problem
technical debt. The checked primary-source packets do not choose Dirichlet,
Neumann/zero-charge, edge-mode, BFV, polarization, or common-domain data.

The decisive return is:

```text
SOURCE-SILENT__BOUNDARY_POLARIZATION_AND_EDGE_MODE__
REPO-CONSTRUCTS_CONDITIONAL_MINIMAL_EDGE_EXTENSION
```

Source silence neither endorses nor refutes this conditional completion.

## Why a scalar counterterm cannot solve it

For any boundary scalar `B`,

\[
\theta\longmapsto\theta+\delta B,
\qquad
\Omega=\delta\theta\longmapsto\Omega+\delta^2B=\Omega.
\]

The exact probe instantiates an arbitrary symmetric four-by-four Hessian and
checks that its antisymmetrization is zero. A deliberately non-Hessian
one-form has nonzero curl and fires the negative control. Thus an ordinary
boundary functional may change the variational principle, but cannot by
itself cancel the existing presymplectic moment map.

## The unextended horns

The v0.69 contraction is

\[
\iota_{R_\xi}\Omega_{bulk}=-\delta Q_\xi,
\qquad Q_\xi=p_0\xi_0-p_2\xi_3.
\]

- `xi0=xi3=0` gives the compact-support/Dirichlet small-gauge horn.
- Requiring `Q_xi=0` for every endpoint parameter forces `p0=p2=0`; its
  tangent space is isotropic and gives a zero-charge/Neumann-like horn.
- Neither horn is selected by the current source/action.

These are not failures. They are conditional domain choices that must not be
smuggled in as consequences of the bulk action.

## Unique edge coefficients and minimality

For the ansatz

\[
\Omega(c_0,c_3)=\Omega_{bulk}
+c_0\,\delta p_0\wedge\delta\phi_0
+c_3\,\delta p_2\wedge\delta\phi_3,
\]

with simultaneous endpoint motion of `g` and `phi`, exact horizontality solves

\[
(c_0,c_3)=(-1,+1)
\]

uniquely. Omitting the second edge cell or using equal signs leaves a live
contraction and fires planted controls.

There are two independent endpoint gauge parameters. With no extension their
contraction is nonzero; one scalar edge coordinate cannot absorb a rank-two
parameter map. Two edge coordinates saturate the lower bound, and the resulting
kernel is exactly—rather than merely containing—the two gauge generators.

## Exact quotient

The gauge-invariant coordinates are

\[
q_0=g_0-\phi_0,\qquad q_3=g_3-\phi_3,
\]

together with `p0,p2`. On this quotient,

\[
\Omega_{red}=\delta p_0\wedge\delta q_0
-\delta p_2\wedge\delta q_3
\]

has rank four. Direct sum over the ten nonzero K77 weights yields the
`60 -> 40` exact local reduction above. Sage independently reproduces the
coefficient solution, kernel, ranks, quotient and counterterm control over
the rationals.

## What changed

- the scalar-counterterm horn is killed structurally;
- the two unextended polarization horns are typed and remain unselected;
- a minimal edge extension is constructed with zero coefficient freedom;
- its all-ten K77 characteristic quotient is exact and nondegenerate;
- the global edge bundle/source selection/common-domain gate remains open.

Five ledger rows migrate in distance, mapping grade and evidence. The scoped
quotient count moves from four to five. Coverage, verdicts, global continuous
residue, function-valued residue, forks and P1/P2/P3 do not move.

```text
Ledger v0.70 — 82/82 active target rows mapped (100%)
32 SAME · 19 DIFFERS · 26 NEEDS · 5 OVER-DETERMINED
Residue — 84 continuous + >=19 function-valued + 9 forks
Quotients ranked — 5 scoped
headline_delta: SCOPED_QUOTIENT_PLUS_ONE
frontier_conditions_closed: 3
frontier_conditions_opened: 1
remaining_named_conditions: 2
```

## Seven-axis disposition

- **Layer 0:** counterterm/edge mode, restriction/extension, local/global and
  nondegenerate/positive objects are separated.
- **L1 syntactic:** bulk and two endpoint edge coordinates are explicit.
- **L2 type:** endpoint parameters, momenta, edge coordinates and ten K77
  coefficient directions remain distinct.
- **L3 algebraic:** coefficients, kernel, rank and quotient are exact over
  rationals with planted failures and an independent Sage route.
- **L4 geometric:** the flat observed contact germ and K77 coefficient bank
  are used; full labelled-bundle descent is open.
- **L5 variational:** `delta^2B=0`, moment-map cancellation and reduced
  presymplectic form close locally.
- **L6 analytic:** no boundary domain, maximal dissipativity, Green domain or
  polarization is selected.
- **L7 physical:** no global BFV, positivity, unitarity, Einstein, Standard
  Model or cosmology conclusion is claimed.

## Constraint fence

```text
new bulk fields: 0
new boundary-coordinate dimension: 20
new coefficient freedom: 0
new selectors: 0
new scoped conditional quotients: 1
physical boundary condition selected: no
global edge bundle constructed: no
P1/P2/P3 consumed: 0
```

Curt remains formally separate inside the Eric lane. No third lane, canon
verdict, claim status or public posture is promoted.

## Next gate

Lift the two endpoint edge cells to a full labelled `Y14` boundary bundle and
prove tilted-inhomogeneous-gauge equivariance, overlap cocycle closure and the
global moment-map identity—or find a source/action-selected boundary domain.
Only then open the full BFV charge algebra, polarization and common analytic
domain.
