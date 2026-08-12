---
title: "Selected K77 I2B observer-associated basicness"
status: exploration
created: 2026-08-12
run_id: RUN-20260812-174351-gu-i2b-observer-associated-basicness
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# Selected K77 I2B observer-associated basicness

## Result

The observer-Hermitian rank-four response from v0.215 is **not** a frame
artifact.  It is an exact associated family under simultaneous Spin transport
of the observer, fields and Hermitian form.  But it is **not basic after the
observer is forgotten**, and the presently built coarse observation projector
does not select the observer's timelike line.

This removes one false horn and sharply separates the live ones:

| proposed owner of `u` | result at current grade |
|---|---|
| diagonal Spin/frame transport | `EXACT` |
| coarse rank-four observation projector alone | `REFUTED` |
| quotient obtained by forgetting `u` | `REFUTED_ON_LIVE_RESPONSE` |
| complete moving `epsilon_IG` / richer observation flag | `OPEN` |
| selected source-action equation for `u` | `OPEN` |
| external datum | fallback only; not adopted |

No external datum, parameter or new field is booked.

## Exact associated-family theorem

In the plus-first K77 frame, take the adapted Lorentz plane on axes
`(0,7,8,9)` and the exact boost

```text
L e0 = (5/3)e0 + (4/3)e7,
S = (2 + gamma7 gamma0)/sqrt(3).
```

The probe verifies exactly

```text
L^T eta L = eta,
S gamma0 S^-1 = (5/3)gamma0 + (4/3)gamma7,
S^T B S = B,
H_(Lu) = S^-T H_u S^-1.
```

The load-bearing adjoint is

```text
A sharp_u = H_u^-1 A^dagger H_u.
```

The inverse is essential.  Although the adapted `H_e0` happens to be an
involution, a noncompact change of frame acts on a Hermitian form by
congruence, not similarity.  Replacing `H_(Lu)^-1` by `H_(Lu)` after the boost
manufactures a covariance failure.

With the correct inverse, `sharp` intertwines on all eight Clifford blades
that occur in the live response.  Cyclicity of trace then transports the
entire `16 x 16` response Gram matrix, covering all 256 pairings.  The
normalized rotor passes; its unnormalized `2 + gamma7 gamma0` control scales
`B` by `3` and rejects.

The Spin lift is even and preserves the two ambient Weyl halves.  This proves
no independent-connection statement: source `C^(32,32)+C^(32,32)`, a derived
block-preserving `U(32,32)xU(32,32)` subgroup, the full `U(64,64)` parent and
two independently varied connections remain four distinct claims.

## Why covariance does not remove the observer

V0.215's fixed-field control remains live.  Holding the response fields fixed
while moving `u` changes a spatial coefficient from `8` to `328/9`.  Therefore
the form is natural on the associated observer family, but it does not descend
to an observer-free object merely by declaring `u` gauge.

The earlier finite observation atlas owns a Lorentzian rank-four plane and a
local adapted representative only modulo its block stabilizer.  In an adapted
frame its projector is preserved by every embedded Lorentz generator.  Their
common fixed tangent-vector space is zero.  The explicit boost above preserves
the same rank-four projector while moving `e0`.  Thus the coarse section data
selects the plane, not a future-unit vector inside it.

This does not kill the full observation route.  The repo has not yet built the
complete moving `epsilon_IG` flag or shown whether it reduces the Lorentz
stabilizer to an `SO(3)` stabilizer.  That richer composite is a different
object from the coarse projector and stays open.

## Layer-0 and symplectic fence

Keep distinct:

- simultaneous frame covariance versus vertical basicness after forgetting
  the observer;
- the coarse observation plane versus a complete moving observation flag;
- an observer-dependent indefinite Hermitian adjoint versus a positive
  Hilbert majorant;
- a finite principal pairing versus an action density, Euler operator,
  presymplectic potential or Green/domain construction;
- source carrier halves versus unitary subgroups versus connection fields.

The symplectic lens licenses only the associated-family pairing theorem.  No
variation with respect to `u` has been added to the selected action, so there
is no `u` Euler equation, Ward identity, moment map or BV quotient yet.

## Data accounting

The conditional cost remains recorded but unbooked:

```text
future-unit observer before equations: 3 function-valued degrees
coarse observation projector's reduction of that cost: 0
new discrete/topological datum adopted: 0
```

P1/P2/P3, the residue, the five scoped quotients and all ledger verdict counts
remain unchanged.

## Verification

`selected_k77_i2b_observer_associated_basicness_probe.py` passes
`40 exact + 2 planted = 42`.  It checks the exact Spin lift and Hermitian-form
law, every live Clifford blade, the trace-cyclicity theorem covering all 256
live pairings, the fixed-field nonbasicness control, and the Lorentz-stabilizer
nonselection theorem for the observation projector.

## Next gate

Construct the smallest richer observation flag that could reduce the coarse
Lorentz stabilizer to `SO(3)` and test whether its selected action is basic.
In parallel, write the constrained `u` variation of the current selected
action: if its Euler/Ward equation determines `u`, the dynamic horn survives;
if not, price the three-function observer field by constraint surplus.  Keep
the coupled metric/section/gauge contact parent as an independent comparator.
