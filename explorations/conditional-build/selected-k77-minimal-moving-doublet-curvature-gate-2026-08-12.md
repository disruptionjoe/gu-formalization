---
artifact_type: exact_construction_and_composition_result
created: 2026-08-12
run_id: RUN-20260812-070112-gu-minimal-moving-doublet-curvature
status: COMPLETE_CANONICAL_MOVING_DOUBLET_LIFT_EXACT_AND_EQUIVARIANT__FULL_SELF_CURVATURE_ZERO__SOLDERING_KERNEL_CONTROL_NONZERO
target_claim: NONE-NOT-A-KILL
ledger: lab/process/conditional-physics-ledger-v0.198.json
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# Selected K77 minimal moving-doublet curvature gate

## Result

The complete natural lift of the exact four-real weak doublet is

```text
L_q(H) = H (q-flat/q^2),       H in W ~= C^2.
```

It has rank four, satisfies `L_q(H)q=H`, and is exactly equivariant when `H`
and the geometry-owned trace direction `q` move together.  This completes the
connection lift that v0.197 had checked only on its radial member.

The result is also a sharp scoped obstruction.  Every component of `L_q(W)`
shares the same vertical one-form leg `q-flat/q^2`.  Hence its full algebraic
curvature vanishes identically:

```text
(q-flat wedge q-flat) [gamma(H_1),gamma(H_2)] = 0
```

for all four scalar components, despite all six distinct Clifford
commutators being nonzero.  The canonical bank therefore cannot generate a
quartic or select a nonzero vacuum through its own `A wedge A` term.

This is not a no-go for the Higgs route.  Soldering has a 90-dimensional
kernel.  An exact independent-leg perturbation `K` with `Kq=0` preserves the
same observed doublet but creates nonzero exterior and Clifford commutators.
The missing object is thus an **action-owned nondecomposable lift**, or a
different curvature/augmented-torsion term—not another doublet carrier.

## Layer 0 and accounting

The soldered doublet, its connection lift, algebraic curvature, and action
potential remain distinct.  The kernel control demonstrates possibility, not
selection.  Adding an arbitrary kernel coefficient would worsen constraint
surplus; no such parameter is booked.  P1/P2/P3, the 20-dimensional `J`
selection burden, verdicts, residue, quotients, canon, and public posture are
unchanged.

## Checks and boundary

The probe passes 40 exact checks after the complete predecessor chain.  It
includes moving-family equivariance, six noncommuting Clifford controls, the
zero common-leg exterior square, and a nonzero kernel-lift firing control.
It establishes neither a bounded potential nor kinetic positivity,
stationarity, photon survival, doublet-triplet separation, Yukawa texture,
BV closure, or a global domain.

## Next gate

Derive the smallest equivariant nondecomposable lift from the selected action,
moving `J/q` geometry, augmented torsion, or curvature—without fitting a point
in the 90-dimensional kernel.  Then compute its quartic, stationary vacuum,
photon kernel and scalar mass matrix.
