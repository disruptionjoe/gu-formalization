---
title: "Selected-K77 CBRS-1V field-admissible Spin-connection obstruction"
status: active_research
doc_type: exact_formal_local_connection_obstruction
created: "2026-08-22"
registry: lab/process/selected-k77-cbrs1v-spin-connection-orbit-obstruction.json
probe: tests/channel-swings/selected_k77_cbrs1v_spin_connection_orbit_obstruction_probe.py
grade: "EXACT RECONSTRUCTION-GRADE FORMAL LOCAL OBSTRUCTION TO THE COMPLETE METRIC-COMPATIBLE SPIN-CONNECTION CLASS NEAR THE UNIT BASE-J4 COFRAME BODY"
target_claim: NONE-NOT-A-KILL
source_return: SOURCE_CONFIRMS_ACTION_PRIMITIVE_EPSILON_AND_METX_GRAMMAR__REPOSITORY_DERIVES_THE_FIELD_ADMISSIBLE_SPIN_CONNECTION_OBSTRUCTION__SOURCE_SILENT_ON_THE_COFRAME_CLASS_AND_OBSTRUCTION
canon_verdict_change: none
---

# Selected-K77 CBRS-1V field-admissible Spin-connection obstruction

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`

```gu-typed-objects
result: CBRS-1V exact field-admissible Spin-connection obstruction for the radial base-J4 coframe lift
carrier: complete selected-first-action T plus independent Spin-grade-two connection plus four real Grassmann-even base scalars near the unit base-J4 body LAYER=toy CHIRALITY=N/A
pairing: selected K77 Clifford scalar-density pairing and fixed internal Lorentz scalar pairing ON=complete_zero_covector_field_tangent_and_primitive_divergence_receiver
real_structure: real base-J4 radical pair in the selected B-skew Cl(7,7) bank
grading: unrestricted Clifford grades one and three for momentum with metric-compatible Spin-grade-two connection generators
action_owner: repository-construction
target: simultaneous T connection primitive-epsilon scalar and intrinsic MET(X) local Euler completion MAP-TYPE=evaluation
```

## Result first

Allowing all `1,274` components of the existing independent Spin connection
does **not** rescue the CBRS-1U coframe lift once every field owner is imposed.

There is a tempting false positive. At the unit-spacelike scalar orbit, form
the complete contracted connection map

```text
(A_0,...,A_13) -> sum_i eta_i [M_i,A_i],
A_i in spin(7,7),
```

where `M0=E_B-E_T` is the exact 18-cell grade-one/grade-three momentum. Its
reached receiver has dimension `78`, and the map has rank `78`. The radial
return lies in that image: the augmented rank is also `78`. Thus an arbitrary
connection plant can cancel the primitive divergence algebraically.

That plant is not a simultaneous Euler solution. The complete pointwise
`T`-plus-connection Hessian at each base-J4 branch has nullity `40`, and the
complete coframe-enlarged zero-covector Hessian still has nullity `40`. In both
cases the kernel is exactly the broken diagonal-Spin gauge orbit. There is no
non-gauge connection modulus in which to realize the unrestricted rank-78
plant while retaining the `T`, independent-connection and scalar owners.

The radial primitive residual cannot disappear along the remaining gauge
orbit. Its active unit-spacelike two-cell contraction has exact norm

```text
q_rad = (35647003639 + 449808155 sqrt(4177)) / 15753835008 > 0.
```

For every one of the 91 Spin bivectors `a`, cyclic invariance gives

```text
q([M_rad,a],M_rad) + q(M_rad,[M_rad,a]) = 0.
```

The exact probe verifies all 91 identities. A gauge orbit can rotate the
nonzero residual but cannot turn it into zero. The CBRS-1U obstruction
therefore survives every smooth field-admissible metric-compatible Spin
connection completion near the licensed unit body.

## Why unrestricted surjectivity is a control, not a rescue

The primitive equation contains a contracted covariant derivative, not the
stronger equation `D_B M=0`. That distinction matters. A first pass based only
on covariant constancy would overstate the obstruction. The full contracted
map deliberately permits all 14 independent connection one-form components
and finds:

| block | reached rows | rank | augmented rank |
| --- | ---: | ---: | ---: |
| grade one | 14 | 14 | 14 |
| grade three | 64 | 64 | 64 |
| combined | 78 | 78 | 78 |

So the connection equation is not rejected because Spin lacks enough
algebraic incidence. It is rejected because those cancelling directions do
not survive the simultaneous field equations. Dropping those equations
repeats the wrong-owner shortcut that CBRS-1H and CBRS-1U already exposed.

## Formal-local scope

The exact complete Hessian is nondegenerate transverse to the diagonal gauge
orbit. The implicit-function consequence is local: near the unit body, the
smooth zero set of the point-field owners has no additional connection branch
beyond the radial particular solution and gauge transport. The primitive
residual is gauge covariant and has nonzero invariant norm on that branch.

This closes the existing metric-compatible Spin-connection class locally. It
does not exclude a disconnected remote branch, a nonmetric Weyl geometry, or
a new action-owned primitive field. Those are materially different classes.

## Hostile return and ceiling

- **Strongest contrary construction:** the unrestricted contracted connection
  map really is surjective. Any summary that says the connection algebra
  cannot cancel the return is false.
- **Strongest dropped-owner failure:** the rank-78 cancellation ignores the
  complete `T` and independent-connection equations, whose common kernel has
  no non-gauge connection modulus.
- **Strongest equation-strength failure:** `D_B^!M=0` is a divergence equation,
  not full covariant constancy. The probe computes the divergence receiver.
- **Strongest extension overclaim:** a Weyl/dilation line is not a
  metric-compatible Clifford-derivation connection. A new compensator or
  Lagrange multiplier is a new action owner and must carry its own coefficient,
  scale and Euler equation.
- **Strongest global overclaim:** the implicit-function statement is local near
  the unit base-J4 body. It is not a global solution-space classification.

No stabilizer, spectrum, ledger verdict, canon, source ownership, residue,
particle assignment, prediction, confirmation or public posture changes.

## Reverse-scaffold consequence

Continue with `CBRS-1W`: freeze the smallest target-blind **action-owned**
primitive-momentum class with an independent non-gauge grade-one/grade-three
return. Require its coefficient, scale and field equation before solving it.
A naked Weyl line, fitted Lagrange multiplier, branch-selected frame or
postselected cancellation is inadmissible. Do not compute a spectrum or
advance to CBRS-2 before an actual local solution passes every Euler owner.

Reproduce with:

```bash
sage -python \
  tests/channel-swings/selected_k77_cbrs1v_spin_connection_orbit_obstruction_probe.py
```

The exact probe passes `31/31` after native propagation.
