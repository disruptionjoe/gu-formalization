---
artifact_type: conditional_build_correction
created: 2026-08-07
status: CONNECTION_CLASS_KILLED_AT_RESIDUAL_ZERO_FIRST_ORDER_PRINCIPAL_GRADE__NORMAL_JET_OR_NONZERO_BACKGROUND_OPEN
source_return: SOURCE-CORRECTS__EPSILON_IS_GAUGE_ORBIT_NOT_DIFFEO_SOLDERING__SOURCE-SILENT__TRANSVERSE117_NORMAL_JET_OR_NONZERO_BACKGROUND_OWNER
ledger: lab/process/conditional-physics-ledger-v0.52.json
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# Selected second-layer transverse-117 residual-zero owner class

## Result in plain English

The queued “move the Levi-Civita/epsilon/soldering connection until it fills
the 117 transverse coefficients” route is unavailable at the current
residual-zero principal grade.

This is structural, not a failed coefficient guess. The principal variation
of the curvature of **any** local connection has the exterior form
`q wedge delta A`. Changing how the connection is assembled from the metric,
source epsilon or soldering data changes `delta A`, but not that exterior
factor. The previous exact split already proves that the 117 transverse
coefficients have zero overlap with every such q-exact coordinate. The
fixed-reference translation curvature therefore exhausts the connection-
curvature principal class here: it owns 28 coefficients, not 145.

Moving the Shiab, frame, Hodge map or target pairing also cannot supply the
missing first-order support at this background. The product rule is

```text
D(S F) = (D S) F_0 + S_0 D F.
```

The selected quadratic branch is evaluated at `F_0=Upsilon_0=0`, so the first
term vanishes. An exact planted nonzero-background control makes it nonzero,
which keeps the conclusion honestly scoped.

The next construction is therefore not another moving-connection search. It
is either the actual ambient normal first jet of raw `Upsilon` on the four
graph columns, a separately source-owned nonconnection two-form/higher-jet
term, or a source-owned nonzero stationary background on which `(D S)F_0`
can operate. This does not kill the full second action.

## Layer 0

| phrase | object proved here | object kept distinct |
| --- | --- | --- |
| moving Levi-Civita | a connection assembled from moving metric data | an ambient observation normal jet |
| source epsilon | a gauge transformation moving `B`, `T` and conjugated Shiab forms | the repo's dynamical diffeomorphism/soldering datum |
| curvature response | principal symbol `q wedge delta A` | lower-order commutators or nonconnection higher jets |
| moving Shiab/frame | `(D S)F_0` in the product rule | `S_0 D F` from a moving source field |
| residual zero | the current stationary quadratic background | a source-owned nonzero stationary solution |
| route kill | zero-background first-order connection/operator class | full nonlinear action, normal-jet route, Euler or physical quotient |

## Exact owner-class theorem

For the non-null representative `q=e^0`, every local connection-curvature
principal response lies in exterior pairs containing `0`. The exact v0.51
packet has:

```text
q-exact support:       7 + 7 + 7 + 7 = 28
transverse support:   51 + 22 + 22 + 22 = 117
support intersection:                         0
```

This is independent of which primitive variables produce `delta A`.
Alternating algebra also gives `q wedge q wedge delta A=0`, so the class is
principal-Bianchi closed. That closure is not total nonlinear naturality.

For a finite exact product-rule fixture, `F_0=0` gives
`D(SF)=S_0 DF`. With `F_0!=0`, the planted control has
`(DS)F_0!=0` and the derivative differs from the frozen-operator derivative.
The second statement is the revival trigger, not a loophole silently used in
the present background.

## Source return

The 2021 source does assign `epsilon` to a gauge orbit and displays
`T=varpi-B(epsilon)`. It does not identify that gauge transformation with the
repo's dynamical soldering field or give the missing four-column ambient
normal jet. The existing source reinspection also corrects the earlier habit
of bundling Hodge, density, metric and observation derivatives into the
epsilon chain.

```text
SOURCE-CORRECTS:
  epsilon is a gauge-orbit variable, not an unbuilt diffeomorphism/soldering
  datum; moving it does not escape the q-exact curvature principal class.

SOURCE-SILENT:
  the transverse-117 normal-jet coefficients, a source-owned nonzero
  stationary background, the nonlinear Euler/Green map and physical domain.
```

## Specialist and hostile review

- **Differential geometry:** the universal curvature symbol, not a preferred
  connection formula, supplies the route kill.
- **Representation theory:** support disjointness is checked coefficientwise;
  equal four-column rank is not used as an identification.
- **Variational PDE / hyperbolic equations:** the theorem is principal and
  background-scoped; lower-order and nonlinear routes remain open.
- **Symplectic geometry:** no Euler, presymplectic, coisotropic, BV or BFV
  conclusion follows from this symbol fence.
- **Krein/operator theory:** no positivity or closed-domain assumption enters.
- **Source criticism:** source epsilon and repo soldering are explicitly
  separated, and source silence is not treated as a refutation.
- **Repo archaeology:** the observation-owner result already named the normal
  first jet; this wave composes it with v0.51 instead of inventing a fifth
  field.

The “summary outruns artifact” hostile charge is answered by the nonzero-
background control. The “lane defends a superseded object” charge fires: the
v0.51 queue overbundled three owner classes under “moving soldering” and is
retyped rather than deepened.

## Progress and next gate

```text
Ledger v0.52 — 82/82 active rows mapped (100%)
32 SAME · 19 DIFFERS · 26 NEEDS · 5 OVER-DETERMINED
Residue — 84 continuous + >=19 function-valued + 9 forks
Quotients ranked — 4 scoped

headline_delta: none
frontier_conditions_closed: 3
  - every moving connection-curvature principal symbol remains q-exact
  - moving Shiab/frame terms vanish at F_0=0
  - source epsilon is fenced from the unbuilt diffeomorphism soldering datum
frontier_conditions_opened: 1
  - choose and construct raw-Upsilon normal jet or source-owned nonzero background
remaining_named_conditions: 5
```

No scalar pole, coefficient, external datum or fifth quotient is added.
P1/P2/P3 remain unused. Curt remains formally separate and no third lane is
promoted.

## Verification

`tests/channel-swings/selected_second_layer_transverse117_residual_zero_owner_class_probe.py`
passes `30/30`, including immutable v0.51 replay and planted nonzero-
background, source-homonym, full-action-overreach and datum controls.
