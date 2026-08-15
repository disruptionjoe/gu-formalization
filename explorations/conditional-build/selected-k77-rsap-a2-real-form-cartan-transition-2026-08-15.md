---
title: "Selected-K77 RSAP split/mixed A2 real-form Cartan transitions"
status: active_research
doc_type: exact_regular_semisimple_transition_construction_and_nonsemisimple_type_gate
created: "2026-08-15"
registry: lab/process/selected-k77-rsap-a2-real-form-cartan-transition.json
probe: tests/channel-swings/selected_k77_rsap_a2_real_form_cartan_transition_probe.py
grade: "SPLIT AND MIXED REGULAR-SEMISIMPLE CARTAN TRANSITIONS CLOSE; REGULAR NONSEMISIMPLE EXTENSION TYPE-MISSING"
canon_verdict_change: none
---

# Selected-K77 RSAP split/mixed `A2` real-form Cartan transitions

## Result first

The compact cotangent-lift mechanism survives every regular-semisimple Cartan
type of the split and mixed real forms. The only change is the rank of the
compact cocharacter lattice and, for the split real Cartan of `SL(3,R)`, a
four-element centralizer component group. Neither requires a new field, a
prequantum twist, or charge integrality.

The conclusion is narrower than full regular globalization. Both principal
factors also contain regular nilpotent values. A nilpotent has no semisimple
Cartan diagonalizer, so these Cartan charts do not cover it even though the
already-proved homogeneous moment map remains rank eight there. Extension
across that locus requires a regular-centralizer group-scheme or real Kostant-
slice transition. That object is not yet written. The result is therefore a
construction on the complete regular-semisimple real-form locus and a
`TYPE-MISSING`, not adverse, verdict at regular nonsemisimple values.

## Layer 0 and the four real Cartan types

The object is a mathematical symplectic/moment atlas for the 20-dimensional
`A2 plus R5_zero` common refinement. It is not an action-selected physical
phase space.

For `SL(3,R)` the regular semisimple locus has two Cartan types:

- three distinct real eigenvalues: split rank two, compact lattice rank zero,
  real Weyl group `S3`; the diagonal centralizer has four sign components,
  `pi_0=(Z/2)^2`;
- one real eigenvalue plus a nonreal conjugate pair: split rank one, compact
  lattice rank one, connected centralizer and real Weyl group `Z/2`.

For `SU(2,1)` it also has two types:

- compact Cartan: compact lattice rank two, connected centralizer, and the
  `Z/2` real Weyl action that exchanges the two positive-sign lines;
- split Cartan: split rank one plus compact rank one, connected centralizer,
  with a `Z/2` split reflection.

The strata are separated by the discriminant. No transition is required
between distinct Cartan types while the value stays regular semisimple;
transitions occur among local sections of the same Cartan-type stratum.

## Exact cotangent transition

Let `Lambda_K` be the compact cocharacter lattice of rank `0`, `1`, or `2`.
On a same-type overlap, the linear Weyl/component action is an integral affine
map `A_ij` and the section logarithm is `phi_ij`. Use

```text
mu_i  = A_ij^{-T} mu_j,
tau_i = A_ij tau_j + phi_ij  mod 2 pi Lambda_K.
```

The orbit part changes by `mu_i^T dphi_ij`. The inverse change of the existing
conjugate coordinate supplies precisely the opposite term in

```text
Theta_i = theta_i^orb - mu_i^T d tau_i + Theta_rest.
```

Hence `Theta_i=Theta_j`, so the symplectic form and all moment components glue.
Triple logarithm defects lie in `2 pi Lambda_K`; when the compact rank is zero
there is no lattice defect, and when it is one or two the defect is identity
on the compact torus. The four split-Cartan sign components act discretely by
cotangent lifts. They change no dimension and preserve the tautological
pairing exactly.

Thus every split/mixed regular-semisimple chart retains the existing
dimension and rank schedule:

```text
dim M = 98,
rank(dJ) = 91.
```

## Why the nilpotent extension does not follow

The size-three Jordan block

```text
N = [[0,1,0],[0,0,1],[0,0,0]]
```

is regular because its centralizer has dimension two, but it is not
semisimple. It occurs in the Lorentz-self-adjoint slice used for both the split
and mixed principal-factor coverage proofs, and the moment differential is
rank eight there. Nevertheless, no eigenline Cartan diagonalizer or compact/
split torus coordinate exists at `N`. The semisimple cotangent atlas therefore
has no typed overlap map to that already-valid local homogeneous chart.

This is not a rank obstruction and not evidence that a 98-dimensional
extension fails. The missing object is a smooth transition using the regular
centralizer family—equivalently a suitably real Kostant/companion slice—and
its two invariant conjugates across the discriminant. It must reproduce the
semisimple torus transitions away from the discriminant and the unipotent
centralizer at `N` without rank loss or primitive defect.

## Claim ceiling

- Split and mixed regular-semisimple `A2` Cartan atlases construct at `98D`.
- Compact lattice ranks `0/1/2` and the split four-component centralizer cause
  no classical cotangent defect.
- The principal factors remain locally valid and rank eight at regular
  nilpotents.
- A full regular real-form atlas is not yet typed across nonsemisimple values.
- `A3` or another higher-root test remains dependency-blocked on that bridge.
- Deeper singular strata, zero charge and the all-strata RSAP remain open;
  the `182D` cotangent parent remains the all-charge fallback.
- No physical, canon, ledger, residue, quotient, datum, or public-posture claim
  changes.

## Next exact gate

Construct the rank-two regular-centralizer/Kostant-slice transition through the
size-three nilpotent for the split and mixed principal factors. Check smooth
primitive and moment pullback, compatibility with all four semisimple Cartan
types, and the `91` map-rank schedule. Only a passing bridge licenses the first
genuinely higher-root subsystem.

Reproduce with:

```bash
python3 tests/channel-swings/selected_k77_rsap_a2_real_form_cartan_transition_probe.py
```

The probe uses exact integer and rational matrices only.
