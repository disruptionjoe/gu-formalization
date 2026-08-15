---
title: "Selected-K77 RSAP compact-A2 integral-affine atlas closure"
status: active_research
doc_type: exact_global_symplectic_moment_atlas_construction
created: "2026-08-15"
registry: lab/process/selected-k77-rsap-a2-integral-affine-atlas.json
probe: tests/channel-swings/selected_k77_rsap_a2_integral_affine_atlas_probe.py
grade: "COMPACT A2 REGULAR 98D SYMPLECTIC/MOMENT ATLAS CLOSES WITH THE EXISTING CARTAN TORUS; SINGLE-CHART RELATIVE PRIMITIVE REMAINS OBSTRUCTED"
canon_verdict_change: none
---

# Selected-K77 RSAP compact-A2 integral-affine atlas closure

## Result first

The compact adjacent-`A2` continuation closes as a classical multi-chart
symplectic and moment atlas at dimension `98`. No prequantum line, new degree
of freedom, or charge-integrality condition is needed.

The preceding unit-Hopf obstruction is genuine on every fixed regular
simple-root orbit. What it omitted, deliberately, is the variation of the two
`A2` charges and their two conjugate Cartan angles in the full 20-dimensional
common refinement. Once those already-owned variables are restored, the
section transition is an ordinary cotangent lift.

Write

```text
mu_1=lambda_1-lambda_2,
mu_2=lambda_2-lambda_3,
phi_ij=(phi_ij^1,phi_ij^2),
tau_i in t/(2 pi Lambda_coroot).
```

On an overlap, the orbit primitive changes by

```text
theta_i^orb-theta_j^orb = mu^T d phi_ij.
```

The inverse Cartan-angle coordinate changes by

```text
tau_i=tau_j+phi_ij  mod 2 pi Lambda_coroot.
```

Therefore the full local primitive

```text
Theta_i=theta_i^orb-mu^T d tau_i+Theta_rest
```

glues strictly: `Theta_i=Theta_j`. Equivalently, in the local polarization
used by the predecessor's universal model, the two missing terms combine as

```text
mu^T dphi_ij + phi_ij^T dmu = d(mu^T phi_ij).
```

The nonzero fixed-charge period has not been gauged away; it is cancelled by
the transition of an existing Cartan angle in the full source. This is a
classical atlas construction, not prequantization.

## Two-root Cech--de Rham object

The compact `A2` torus bundle has Chern lattice `Z alpha_1^vee plus Z
alpha_2^vee`. Local logarithms obey

```text
phi_ij+phi_jk+phi_ki = 2 pi n_ijk,
n_ijk in Z^2.
```

The same integer is identity on the Cartan torus, so the `tau` transition
closes on every triple. Both simple-root restrictions reproduce the unit Hopf
class. The third positive root has

```text
mu_12=mu_1+mu_2,
n_12=n_1+n_2,
```

so it introduces no third independent obstruction. The Cech two-class is not
zero; it is absorbed by the inverse transition of the already-present torus
coordinate. This distinction is the global content of the construction.

The simple reflections act on the charge column by

```text
s_1 = [[-1,0],[1,1]],
s_2 = [[1,1],[0,-1]],
```

and on conjugate angles by inverse transpose. They square to identity, obey
the `A2` braid relation, and preserve `mu^T d tau`. Thus the Weyl changes of
regular chamber coordinates introduce neither a symplectic nor moment-map
defect.

## Why the dimension stays 98

The two angles are not imported repair fields. Locally they are the two
conjugates already counted in the universal minimal realization of
`sl(3)^* x R5_zero`; globally they are the corresponding root-Cartan
directions already present in the `Spin_0(7,7) x C` regular carrier. The
remaining 78-dimensional leaf and five centre pairs are unchanged. Hence the
composition remains

```text
78 + 20 = 98,
rank(dJ)_regular = 91,
rank(dJ)_A2-origin = 88.
```

All 13 common-refinement moment components remain section-independent. The
full `so(7,7)^*` moment map therefore glues with the previously proved rank
schedule.

## First collapse compatibility

At the first wall `mu_1=0`, the term `mu_1 d tau_1` vanishes and the
`alpha_1` circle may collapse while the primitive lattice vector
`alpha_2^vee` remains. This exactly matches the compact rank-one
`T*(SU(2)/U(1))` attachment and the already-proved `91 -> 90` map-rank drop.
The same statement holds with roots exchanged. At the adjacent `A2` point,
both simple-root circles are handled by the principal
`T*(SU(3)/SO(3))` factor and the existing `91 -> 88` schedule.

This proves the lattice, primitive and rank compatibility needed by the
compact `A1/A2` wall atlas. It does not classify the global split or mixed
real-form transitions, an `A3` or other higher root subsystem, the full
singular stratification, or the zero-charge `rank(dJ)<=49` endpoint.

## Claim ceiling and hostile scope

- The one-global-diagonalizer route remains killed.
- The fixed-charge relative primitive still has period `2 pi mu_alpha`.
- The complete compact regular multi-chart symplectic/moment atlas closes.
- Its full primitive closes only after the existing Cartan-angle transition
  is included; a bare orbit chart does not acquire an exact primitive.
- No charge quantization follows. Prequantum integrality remains a separate
  question because this cancellation uses classical cotangent coordinates.
- No physical phase space, stationary background, cohomology, spectrum or
  Standard Model claim follows.

No ledger, canon, residue, quotient datum, public posture or external system
changes.

## Next exact gate

Globalize the split and mixed principal-`A2` factors with their actual
noncompact/compact Cartan lattices and component groups. Test whether the same
cotangent-lift cancellation closes every real-form overlap. If it does, pass
to the first `A3` (three adjacent roots) or other genuinely higher singular
root subsystem; if it fails, retain the exact real-form obstruction rather
than importing a twist. Zero charge and the all-strata minimum remain open.

Reproduce with:

```bash
python3 tests/channel-swings/selected_k77_rsap_a2_integral_affine_atlas_probe.py
```

The probe uses exact integer and rational lattice arithmetic.
