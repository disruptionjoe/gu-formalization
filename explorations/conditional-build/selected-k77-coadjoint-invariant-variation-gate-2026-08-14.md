---
artifact_type: exact_endpoint_coadjoint_invariant_variation_result
created: 2026-08-14
status: ALL_SEVEN_INVARIANTS_VARY__UNCONSTRAINED_FIXED_ORBIT_GLOBAL_HORN_REJECTED__BOUNDARY_LOCKING_OR_LARGER_CARRIER_OPEN
source_return: SOURCE_CONFIRMS_B_T_AND_MOVING_GAUGE_PARENT__SOURCE_SILENT_INVARIANT_LOCKING_EDGE_FIELD_BOUNDARY_DISPOSITION_AND_DOMAIN
ledger_rows: [RA-G2, LT-SM3, AC-F1, AC-G1a]
registry: lab/process/selected-k77-coadjoint-invariant-variation-gate.json
canon_verdict_change: none
---

# Selected K77 coadjoint-invariant variation gate

## Result first

The minimal 84-dimensional coadjoint orbit constructed at the selected K77
endpoint does **not** extend as one fixed orbit over the unconstrained nearby
action coefficient space.  The endpoint charge was identified exactly with
an element `L` of `so(7,7)` through the vector-representation trace pairing.
The seven type-`D7` invariant generators

```text
tr(L^2), tr(L^4), tr(L^6), tr(L^8), tr(L^10), tr(L^12), Pf(eta L)
```

have independent differentials of rank seven at the regular fixture; their
common tangent kernel is exactly the 84-dimensional coadjoint-orbit tangent.

Along the action-owned finite coefficient-space line

```text
(B,T) -> lambda (B,T),       (delta B,delta T)=(B,T) at lambda=1,
```

the endpoint charge has the exact homogeneity

```text
mu(lambda)=lambda^3 mu_cubic + lambda^2 mu_mass.
```

All seven invariant derivatives are nonzero:

```text
173312
2024711412224/27
9637222290427904/9
518769247691107249979392/2187
30352009699815790466145320960/6561
34267541608565798000339414145302528/59049
5080821530624/3
```

Thus this action-owned direction is transverse to the selected coadjoint
orbit.  A single fixed `O_{-mu}` cannot cancel the endpoint charge over the
full unconstrained nearby coefficient family.

This is a clean kill of the **unconstrained fixed-orbit global horn**, not of
every fixed-orbit boundary theory.  The tested scaling direction is an exact
off-shell tangent in the selected action's `B/T` coefficient space.  An
independently derived boundary/Green stationarity equation could remove that
direction and lock all seven invariants on its admissible boundary locus.  No
such law is presently source-owned or constructed.

## Plain English

The previous packet found the smallest symmetry orbit that cancels the charge
at one endpoint.  This packet asks whether the same orbit still works when the
action fields move.  It does not: every independent label of that orbit
changes under one ordinary exact field variation.  Without an additional
boundary equation that freezes those labels, the edge system must be larger
than one orbit or the charged transformations must be treated as boundary
symmetries rather than removed gauge.

## Exact construction

Let `M_i` be the 91 normalized real bivector generators and let the endpoint
covector have components `mu_i`.  The vector trace form is nondegenerate, so
there is one exact `L in so(7,7)` satisfying

```text
tr(L M_i)=mu_i.
```

With `eta` the exact `(7,7)` metric, `eta L` is skew.  The six even traces and
`Pf(eta L)` form the standard seven invariant-polynomial generators for type
`D7`.  At this fixture their differential matrix has rank seven.  Its kernel
has dimension 84 and agrees with the Kirillov image, providing an independent
control that coadjoint motion preserves every invariant.

The endpoint functional is recomputed from the actual selected action Euler
covectors, not perturbed by hand.  Exact evaluations at `lambda=1,2` separate
the cubic and quadratic contributions and give the analytic first derivative.
The derivative fails the seven-invariant tangent test in all seven rows.

## Route comparison

- **Invariant theory / Lie theory** supplied the decisive coordinate-free
  kill test and was selected.
- **Broad coordinate sampling** was dominated: it could observe change but
  would not prove that the change leaves the orbit.
- **Immediate cotangent/group-carrier construction** was deferred: it is now
  the successor, but building it before proving invariant variation would
  import unnecessary boundary fields.
- **Variational and source lenses** kept the variation inside the selected
  action coefficient fields and refused to call it an on-shell boundary law.
- **BFV and analytic lenses** preserve the algebraic master equation and KT
  result while deferring domains and cohomology.

## Surviving horns and next gate

Three possibilities remain:

1. derive a boundary/Green equation that locks all seven invariant values;
2. construct the smallest equivariant group/cotangent carrier spanning the
   exact transverse invariant variation; or
3. retain the charged transformations as boundary symmetries with charges.

The next structural gate is to compare (1) and (2): derive the boundary
stationarity conditions from the selected action, and in parallel compute the
minimal symplectic enlargement that admits the observed seven-value motion.
Only then should the curved BFV presentation enter an analytic domain.

No ledger verdict, residue, quotient, datum, canon claim, W/mirror selection,
chirality, generation count or public posture changes.  Weinstein's total
theory remains explicitly non-chiral.

## Reproduction

```sh
sage -python \
  tests/channel-swings/selected_k77_coadjoint_invariant_variation_gate_probe.py
```

The probe replays the exact 51-check predecessor, reconstructs the trace dual,
certifies invariant independence and orbit tangency, and tests planted false
orbit-tangent and source/claim controls.
