---
title: "Selected K77 I2B observer-time Hermitian reduction"
status: exploration
created: 2026-08-12
canon_verdict_change: none
---

# Selected K77 I2B observer-time Hermitian reduction

## Result

The v0.214 phase-even rank-four kinetic candidate has an exact
pseudo-unitary completion, but the geometry-owned vertical trace does **not**
supply it.

On the already-certified four-real principal response, define

```text
H_u = i B gamma(u),
X sharp_u = H_u X dagger H_u,
Q_u(X,Y) = Re Tr((X sharp_u)Y)/128.
```

For an adapted future unit observer `u=e0`, the exact four base blocks are

```text
-8 I4, +8 I4, +8 I4, +8 I4,
```

with every mixed block zero.  Thus `Q_u` has the required Lorentz rank four
and is the negative of the v0.214 phase-even response form.  An exact
`U(1,1)` plant preserves its value `1 -> 1`; the raw coordinate Frobenius
pairing from v0.214 changes `1 -> 1681/81`.  The observer-time form therefore
provides the missing noncompact-unitary-invariant completion of that local
witness.

The canonical vertical trace `q_g=g/2`, represented by the normalized trace
axis in the `(6,4)` normal fibre, gives **zero on all four blocks**.  Its total
live-response rank is zero.  It cannot be used as the rank-four repair merely
because it already owns an `H_q` of inertia `(64,64)` and `(32,32)` on each
ambient Weyl half.

## What the result selects—and what it does not

A time orientation picks the future component of the unit-timelike
hyperboloid.  It does not pick a point of that hyperboloid.  The fibre

```text
SO+(1,3)/SO(3)
```

is three-dimensional and contractible.  Exact common-kernel calculation for
the six Lorentz generators confirms that no nonzero vector is fixed by the
full Lorentz group.  Consequently an observer field `u` costs three
function-valued choices before equations or quotient, unless the observation
map, soldering field or action determines it.

That is a conditional fit, not a failure of the geometry: if an existing
moving observation reduction supplies `u`, the kinetic pairing is available
with no new discrete topological datum.  But the present construction has not
shown that the selected action is independent of `u`.  For the rational boost

```text
u' = (5/3)e0 + (4/3)e7,
```

`gamma(u')^2=1`, while the fixed-frame spatial coefficients become `328/9`
rather than `8`.  This is consistent with an equivariant moving family under
joint transport; it is not proof that changing `u` is gauge or that the action
is basic on the hyperboloid quotient.

## Layer-0 fence

Keep distinct:

| object | established role | not established |
|---|---|---|
| vertical trace `q_g` | geometry-owned negative normal direction | observer time |
| future unit `u` | conditional Lorentzian Hermitian reduction | source-selected field |
| time orientation / P1 | chooses a component and orients a supplied line | manufactures a timelike line or unit vector |
| `H_u` | indefinite Hermitian form and adjoint | positive Hilbert majorant |
| `Q_u` | exact pairing on the finite live response | complete action, Green form or physical spectrum |
| `C^(32,32)+C^(32,32)` | two carrier halves | two independent connections |
| `U(32,32)xU(32,32)` | derived block-preserving subgroup | the full `U(64,64)` parent |

The symplectic review therefore licenses only a fibre/principal pairing
statement.  No Euler equation, presymplectic quotient, closed domain,
stationary vacuum or particle spectrum follows from it.

## Data accounting

No datum is adopted and the ledger residue does not change.  The conditional
cost is recorded, not booked:

```text
future unit observer before equations: 3 function-valued degrees
additional discrete/topological datum: 0 beyond an existing time orientation
```

P1/P2/P3 remain unchanged and unused.  P1 could orient a line after the line
exists; it cannot select `u`.

## Verification

`selected_k77_i2b_observer_time_hermitian_reduction_probe.py` passes
`47 exact + 2 planted = 49`, including the trace rank-zero result, the
observer Lorentz blocks, the rational boost, the noncompact `U(1,1)`
invariance control and the Lorentz fixed-vector calculation.

## Next gate

Derive `u` from the existing observation/soldering field or prove that the
selected action descends to a basic object under changes of `u`.  If neither
holds, decide whether the three-function observer field is an admissible
conditional datum with positive constraint surplus.  Keep the coupled
metric/section/gauge contact parent as an independent route.
