---
artifact_type: construction_result
created: 2026-08-08
status: TWO_ENDPOINT_COTANGENT_DRESSING_EXACT__SINGLE_HOLONOMY_RETAINS_ONLY_GAUSS_DIAGONAL_HALF__CONTINUUM_ENDPOINT_OWNER_OPEN
source_return: SOURCE-CONFIRMS__K77_P_H_AND_TWO_SIDED_TILTED_ACTION__SOURCE-SILENT__EPSILON_BOUNDARY_BFV_OWNERSHIP
ledger_rows: [LT-GR1, LT-GR2b, LT-GR3, LT-GR5, LT-GR6]
scripts:
  - tests/channel-swings/selected_k77_two_endpoint_edge_dressing_probe.py
  - tests/channel-swings/selected_k77_two_endpoint_edge_dressing_independent.sage
registry: lab/process/selected-k77-two-endpoint-edge-dressing.json
---

# Selected K77 two-endpoint edge dressing

## Result first

The K77 principal group is available, and its natural two-endpoint nonlinear
edge dressing is exactly symplectic. But a **single connection holonomy is too
small** to globalize the full v0.70 boundary phase space.

The current K77 branch already constructs

\[
P_H=P_{\operatorname{Spin}(C)}\times_{\rho_H}U(64,64),
\]

with the real \(\operatorname{Spin}(7,7)\) carrier and its split invariant
spinor form. No K95 quaternionic or right-\(\mathbb H\) machinery is needed.

For a connection holonomy and endpoint frames transforming as

\[
X\mapsto h_s^{-1}Xh_t,\qquad
u_s\mapsto u_sh_s,\qquad u_t\mapsto u_th_t,
\]

the cotangent law and dressed pair are

\[
P\mapsto h_s^TP h_t^{-T},\qquad
q=u_sXu_t^{-1},\qquad
\pi=u_s^{-T}Pu_t^T.
\]

Both \(q\) and \(\pi\) are invariant. On a noncommuting exact rational
fixture, the pulled-back canonical form has rank eight on a sixteen-dimensional
extended space, and its eight-dimensional characteristic kernel is **exactly**
the independent source-and-target gauge orbit. Thus the nonlinear groupoid
reduction is sound and applies functorially to the K77 \(U(64,64)\) extension.

The failure occurs at the action comparison. At identity,

\[
\delta q=\delta u_s+\delta X-\delta u_t.
\]

Writing the connection tangent as
\(\delta X=\delta g_3-\delta g_0\) gives

\[
\delta q=(\delta g_3-\delta\phi_3)
          -(\delta g_0-\delta\phi_0).
\]

So one holonomy sees only the **difference** of the two invariant endpoint
cells. Matching its potential to the v0.70 potential forces
\(p_0=p_2=-P\). The independent endpoint momenta are collapsed to the
Gauss-diagonal subspace:

```text
v0.70 ten-normal quotient:       dimension/rank 40/40
single-holonomy dressed subspace: dimension/rank 20/20
```

The preregistered ending `V070_TWO_ENDPOINT_LINEARIZATION_NOT_RECOVERED`
therefore fires. This is not a failure of the edge idea or of K77. It rules
out a tempting compression. The correct successor must derive two continuum
boundary evaluation maps and their primitive epsilon preboundary momenta from
the selected action, then apply the dressing without replacing the continuum
boundary phase space by one lattice holonomy.

## Layer 0

| phrase | object used here | not identified with |
| --- | --- | --- |
| K77 group owner | chimeric-spin extension `U(64,64)` containing real `Spin(7,7)` | K95 `Sp(32,32;H)` or right-H |
| connection holonomy | group element with source/target gauge action | a pair of independent endpoint field evaluations |
| endpoint frame | `u_s,u_t` with multiplicative gauge law | additive tangent edge cells before exponentiation |
| cotangent dressing | canonical trace pairing on a group holonomy | a positive Hilbert/Krein majorant |
| source epsilon | existing group-valued gauge/nonlinear-sigma field | proven owner of independent BFV edge coordinates |
| Gauss-diagonal subspace | `p_0=p_2` single-holonomy cotangent image | full v0.70 `p_0,p_2` boundary phase space |
| exact quotient | finite algebraic groupoid cotangent reduction | global physical BFV phase space or analytic domain |

The load-bearing distinction is connection holonomy versus continuum boundary
evaluation. A holonomy already integrates the connection between endpoints;
its cotangent carries one momentum. A local field theory has independent
boundary evaluations and their oriented preboundary momenta before any Gauss
reduction. Compressing the latter into the former silently performs half the
reduction.

## Source return

Weinstein explicitly supplies the K77 chimeric-spinor gauge bundle, source
epsilon as a group-valued field, the tilted subgroup and its two-sided action.
Those claims type the nonlinear groupoid construction.

The checked source does not identify the boundary restriction of epsilon with
independent BFV edge fields or print their action-derived primitive
preboundary potential. The correct return is

```text
SOURCE-CONFIRMS__K77_P_H_AND_TWO_SIDED_TILTED_ACTION__
SOURCE-SILENT__EPSILON_BOUNDARY_BFV_OWNERSHIP
```

Source epsilon is a well-typed candidate owner. It is not yet the constructed
owner.

## Exact symplectic calculation

For generic rational two-by-two matrices, the map

\[
(X,P,u_s,u_t)\longmapsto(q,\pi)
\]

has rank eight. Pulling back
\(\Omega_{can}=\operatorname{Tr}(\delta\pi^T\wedge\delta q)\)
gives rank eight and kernel dimension eight. The infinitesimal action is

\[
\begin{aligned}
\delta X&=-\xi_sX+X\xi_t,\\
\delta P&=\xi_s^TP-P\xi_t^T,\\
\delta u_s&=u_s\xi_s,\\
\delta u_t&=u_t\xi_t.
\end{aligned}
\]

All eight generators lie in the kernel, their rank is eight, and adjoining an
independent kernel basis does not increase rank. A frozen-cotangent plant and
reversed source/target law both fail. An independent Sage/QQ route reproduces
the complete result.

Because the proof is a matrix identity using only the cotangent trace pairing,
it specializes to the matrix group \(U(64,64)\) and its real
\(\operatorname{Spin}(7,7)\) subgroup. The two-by-two fixture is a compact
exact witness, not a replacement gauge group.

## Why the v0.70 recovery fails

The v0.70 reduced endpoint cells are

\[
q_0=g_0-\phi_0,\qquad q_3=g_3-\phi_3,
\]

with potential

\[
\Theta_{70}=p_0\,\delta q_0-p_2\,\delta q_3.
\]

The holonomy linearization gives

\[
\Theta_{hol}=P(\delta q_3-\delta q_0).
\]

Coefficient comparison forces \(p_0=p_2=-P\). Per normal direction, the
full endpoint quotient has dimension/rank `4/4`; the holonomy image has
`2/2`. Direct sum over ten nonzero K77 normals yields `40/40` versus `20/20`.

This negative result is useful: it prevents a mathematically elegant
groupoid shortcut from deleting the common endpoint mode and momentum
difference before the selected action says they are gauge or constrained.

## What changed

- the K77 `P_H` group owner is explicitly reconciled with the edge problem;
- exact two-sided nonlinear cotangent dressing and kernel equality are built;
- the single-holonomy candidate is killed as a globalization of the **full**
  v0.70 phase space;
- the missing owner is narrowed to the selected action's two continuum
  boundary evaluations and primitive epsilon preboundary pair;
- no quotient, residue, verdict, datum or public-posture count moves.

```text
Ledger v0.73 — 82/82 active target rows mapped (100%)
32 SAME · 19 DIFFERS · 26 NEEDS · 5 OVER-DETERMINED
Residue — 84 continuous + >=19 function-valued + 9 forks
Quotients ranked — 5 scoped
headline_delta: NONE
frontier_conditions_closed: 2
frontier_conditions_opened: 1
remaining_named_conditions: 2
```

## Seven-axis disposition

- **Layer 0:** K77/K95, holonomy/endpoint evaluation, epsilon/edge field,
  group/cotangent and local/global objects are separated.
- **L1 syntactic:** source/target actions, cotangent law, dressed variables and
  endpoint linearization are explicit.
- **L2 type:** the source-owned `U(64,64)` matrix category is used; the exact
  `GL(2,Q)` fixture is only a universal witness.
- **L3 algebraic:** finite invariance, Jacobian rank, kernel equality, quotient
  rank and the `40 -> 20` comparison pass exactly with planted failures.
- **L4 geometric:** a connection groupoid edge is constructed; the continuum
  boundary evaluation bundle and full `tau_A0` action remain open.
- **L5 variational:** the canonical groupoid form is basic, but it is only the
  Gauss-diagonal subspace of the action-owned v0.70 preboundary class.
- **L6 analytic:** polarization, global BFV, charge algebra and common
  Green/Krein domain remain open.
- **L7 physical:** no positivity, unitarity, Einstein, Standard Model or
  cosmology conclusion is claimed.

## Constraint fence

```text
new bulk fields: 0
new boundary fields selected: 0
new coefficient freedom: 0
new scoped quotients: 0
K77 group owner: constructed
single-holonomy full-v0.70 bridge: killed
P1/P2/P3 consumed: 0
```

Curt remains formally separate inside the Eric lane. No third lane, canon
verdict, claim status or public posture is promoted.

## Next gate

Derive the two continuum endpoint evaluation maps and the primitive epsilon
preboundary momenta from the selected action. Then apply the direct-sum K77
edge dressing to both endpoint copies and prove its global overlap and moment
map descent **without** compressing them to a single holonomy. Only after that
should full `tau_A0`, BFV charge algebra, polarization and common-domain work
open.
