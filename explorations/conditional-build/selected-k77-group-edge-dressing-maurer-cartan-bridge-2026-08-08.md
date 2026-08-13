---
artifact_type: construction_result
created: 2026-08-08
status: GROUP_EDGE_DRESSING_AND_PRESYMPLECTIC_BASICNESS_EXACT__MAURER_CARTAN_TAU_BRIDGE_PURE_GAUGE_ONLY__ACTUAL_K77_H_INSTANTIATION_OPEN
source_return: SOURCE-CONFIRMS__TAU_A0_PURE_GAUGE_MAURER_CARTAN_BRIDGE__SOURCE-SILENT__BOUNDARY_EDGE_DRESSING_AND_PRESYMPLECTIC_COMPLETION
ledger_rows: [LT-GR1, LT-GR2b, LT-GR3, LT-GR5, LT-GR6]
scripts:
  - tests/channel-swings/selected_k77_group_edge_dressing_maurer_cartan_bridge_probe.py
  - tests/channel-swings/selected_k77_group_edge_dressing_maurer_cartan_bridge_independent.sage
registry: lab/process/selected-k77-group-edge-dressing-maurer-cartan-bridge.json
---

# Selected K77 group-edge dressing and Maurer-Cartan bridge

## Result first

The missing universal edge construction exists, and it passes the stronger
symplectic test that v0.71 demanded.

Let a boundary configuration `x` and edge frame `u` transform under a right
gauge action, with cotangent variable `p` transforming contragrediently:

\[
x\mapsto xh,\qquad u\mapsto uh,\qquad p\mapsto p h^{-T}.
\]

Then

\[
q=xu^{-1},\qquad \pi=p u^T
\]

are exactly invariant. Pulling the canonical potential
`Theta=Tr(pi^T delta q)` back to `(x,p,u)` produces a presymplectic form whose
kernel is exactly the simultaneous right gauge orbit on a generic rational
`GL(2)` fixture:

```text
extended dimension: 12
dressed-map rank: 8
pulled-back two-form rank: 8
characteristic-kernel dimension: 4
right gl(2) orbit rank: 4
kernel equals gauge orbit: yes
quotient dimension/rank: 8/8
```

This is not coordinate invariance masquerading as reduction: the complete
kernel equality and nondegenerate quotient are exact. At `x=u=1`,
`delta q=delta x-delta u`, and
`Theta=Tr(p^T(delta x-delta u))`, recovering the v0.70 minus sign.

The bridge to Weinstein's tilted object is differential. The **base**
Maurer-Cartan form

\[
a_u=u^{-1}d u
\]

transforms exactly as

\[
a_u\mapsto h^{-1}a_u h+h^{-1}d h.
\]

It closes on a noncommuting triple overlap. Its curvature is identically zero,
so it realizes only the flat/pure-gauge `A0=0` component of the tilted affine
sector. It is not an arbitrary olive/varpi connection.

## Layer 0

| phrase | exact object | not identified with |
| --- | --- | --- |
| boundary configuration | group-valued `x` | connection one-form |
| edge frame | group-valued right frame `u` | `u^-1 d u` |
| dressed pair | `q=xu^-1`, `pi=p u^T` | raw variables before quotient |
| field-space potential | `Tr(pi^T delta q)` | base exterior derivative |
| differential bridge | base one-form `u^-1 d u` | field-space `delta u` |
| pure-gauge tilted component | flat affine one-form at `A0=0` | arbitrary `varpi` with curvature |
| universal fixture | exact `GL(2,Q)` cotangent theorem | actual K77 `H`-representation/action |

The distinction between base `d` and field-space `delta` is load-bearing. The
first produces the tilted affine component; the second produces the
preboundary two-form.

## Source return

The checked Weinstein surfaces explicitly supply the inhomogeneous gauge
group, tilted homomorphism, second Maurer-Cartan component, and distinguished
Levi-Civita/Zorro reference connection. That confirms the target affine law
and the pure-gauge differential bridge.

They do not supply the boundary edge frame, its cotangent dressing, the
presymplectic completion or BFV reduction.

```text
SOURCE-CONFIRMS__TAU_A0_PURE_GAUGE_MAURER_CARTAN_BRIDGE__
SOURCE-SILENT__BOUNDARY_EDGE_DRESSING_AND_PRESYMPLECTIC_COMPLETION
```

## Exact construction

The primary probe uses independent rational matrices `x,p,u,h`, forms the
dressed map symbolically, evaluates its exact Jacobian at the preregistered
generic fixture, and pulls back the canonical eight-dimensional symplectic
matrix. Four independent `gl(2)` infinitesimal generators are built as

\[
(\delta x,\delta p,\delta u)=(xE,-pE^T,uE).
\]

All four lie in the kernel, and their rank equals the kernel nullity. A planted
transformation that leaves `p` inert is not characteristic.

For the differential bridge, the probe uses `d(uh)=du h+u dh` and verifies the
affine law and noncommuting triple-overlap product rule exactly. Wrong-side,
reversed-order and omitted-product-rule plants fail. An independent Sage/QQ
route reproduces the invariant dressing, rank/kernel theorem, affine law,
triple overlap and zero Maurer-Cartan curvature.

## Symplectic interpretation

The edge frame does not add physical boundary degrees of freedom in this
universal model: four new group coordinates arrive with four new gauge
directions. The quotient recovers the canonical dressed cotangent phase space.
That is the right formal shape for a BFV edge completion, but it is not yet the
physical K77 BFV phase space. The actual action's invariant trace, endpoint
orientation, field representation, moment map and analytic domain still own
that claim.

## What changed

- a universal group-valued edge dressing is constructed;
- its pulled-back symplectic form is basic with exactly the gauge kernel;
- identity linearization recovers the v0.70 preboundary minus sign;
- `u^-1 d u` supplies an exact differential bridge to the flat tilted component;
- arbitrary `varpi`, nonzero `A0` and actual K77 action ownership remain open;
- no new quotient, residue, verdict, datum or public-posture movement occurs.

```text
Ledger v0.72 — 82/82 active target rows mapped (100%)
32 SAME · 19 DIFFERS · 26 NEEDS · 5 OVER-DETERMINED
Residue — 84 continuous + >=19 function-valued + 9 forks
Quotients ranked — 5 scoped
headline_delta: NONE
frontier_conditions_closed: 3
frontier_conditions_opened: 1
remaining_named_conditions: 2
```

## Seven-axis disposition

- **Layer 0:** group frame, base Maurer-Cartan one-form, field-space variation,
  pure-gauge component and arbitrary connection remain distinct.
- **L1 syntactic:** right action, dressed coordinates, canonical potential,
  gauge generators and affine bridge are explicit.
- **L2 type:** base `d` and field-space `delta`, configurations and cotangents,
  universal `GL(2)` fixture and actual K77 representation are separated.
- **L3 algebraic:** exact rational rank/kernel calculations, noncommuting
  overlaps, planted failures and independent Sage replay pass.
- **L4 geometric:** the universal finite bundle/dressing law passes; the actual
  labelled K77 `H`-bundle and full `tau_A0` geometry remain open.
- **L5 variational:** the pulled-back two-form is basic and its quotient is
  nondegenerate in the fixture; the action-owned physical preboundary form is open.
- **L6 analytic:** polarization, global Green/Krein common domain and BFV
  completion remain open.
- **L7 physical:** no positivity, unitarity, Einstein, Standard Model or
  cosmological conclusion is claimed.

## Constraint fence

```text
new bulk fields: 0
new boundary-coordinate dimensions: 0
new coefficient freedom: 0
new scoped quotients: 0
pure-gauge differential bridge: exact
arbitrary varpi bridge: not claimed
P1/P2/P3 consumed: 0
```

Curt remains formally separate inside the Eric lane. No third lane, canon
verdict, claim status or public posture is promoted.

## Next gate

Instantiate the universal dressing on the actual K77 `H`-representation and
action-owned preboundary potential with its invariant trace. Extend the bridge
from `A0=0` to the full `tau_A0` law and prove the global `H`-bundle moment map
and characteristic-kernel descent before opening BFV/common-domain work.
