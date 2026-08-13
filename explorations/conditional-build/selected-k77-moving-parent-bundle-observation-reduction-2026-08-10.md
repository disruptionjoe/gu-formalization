---
artifact_type: exact_construction_result
created: 2026-08-10
status: MOVING_SPIN113893_AND_FULL_U229477_GLOBAL__TWO_HALF_REDUCTION_INSIDE_FULL_P_H__ACTION_PROJECTOR_OWNERSHIP_OPEN
canon_verdict_change: none
---

# Selected K77 moving-parent bundle and observation reduction

## Result

The fixed-frame conclusion from v0.129 was too broad. A fixed rank-`8,128`
Spin-skew subspace is not invariant under the exhibited full-unitary escape,
but the already source-owned moving Clifford frame transports its projector:

```text
P_epsilon = Ad(epsilon^-1) P_0 Ad(epsilon).
```

On two exact noncommuting rational Clifford transitions, the transported
projector accepts all `8,128` transported skew directions, rejects all `8,256`
complement directions, is idempotent, and obeys direct/sequential cocycle
descent on all `16,384` coefficient directions. Recomputing `Phi_1`, `Phi_2`,
Hodge and the first-order Euler operator in the moving frame gives exact
equivariance and sector closure wholesale. Freezing those objects is a planted
failure.

Therefore both associated-bundle candidates globalize at this finite gate:

```text
moving Spin-skew: connection 113792 + metric/epsilon 101 = 113893
full U(64,64):    connection 229376 + metric/epsilon 101 = 229477
```

This does not select which tangent the action owns.

## What the two `C^(32,32)` halves mean

The moving chirality involution

```text
chi_epsilon = Ad(epsilon^-1) chi_0 Ad(epsilon)
```

splits the full `u(64,64)` coefficient space into `8,192` block directions and
`8,192` off-diagonal directions. The former are the tangent of a connection
compatible with the two-half reduction; the latter are bifundamental/coset
associated one-form data. The Spin-skew Euler carrier crosses both pieces:
`4,096` skew-block plus `4,032` skew-coset directions.

Thus the source's two Weyl spaces are not, by notation alone, two independent
principal `U(32,32)` connection groups. The source parent remains full
`P_H` with `U(64,64)` structure, and the two halves define a moving reduction
inside it. A genuine reduced connection still requires a compatibility law
such as `D_varpi chi_epsilon = 0`, or an action/BV mechanism that enforces it.

## Observation pullback

Ordinary value pullback changes the fourteen one-form slots to four but does
not choose an internal parent:

```text
moving Spin-skew observed value total = 4*8128 + 101 = 32613
full-U observed value total           = 4*16384 + 101 = 65637
```

Pulling back `P_H` retains its structure group unless a reduction section is
also constructed. These are value counts, not a first-jet tangent, spectrum,
quotient, or particle count.

## Source return and Layer 0

The 2021-draft source packets confirm the full `U(64,64)` `P_H`, the two
`C^(32,32)` Weyl halves and the epsilon-moved frame. They do not state that the
physical action tangent is the Spin-skew subbundle or that observation selects
the reduction:

```text
SOURCE_CONFIRMS_FULL_U6464_P_H_TWO_C32_32_WEYL_HALVES_AND_EPSILON_MOVED_FRAME__SOURCE_SILENT_SPIN_SKEW_TANGENT_CONSTRAINT_AND_PHYSICAL_REDUCTION
```

The distinctions carried forward are fixed subspace versus moving subbundle;
two Weyl vector bundles versus two principal groups; full-U parent versus a
moving block reduction; affine connection value versus adjoint-valued tangent;
pullback versus structure-group reduction; and Euler covariance versus action
parent selection.

## Accounting and boundary

No coefficient, quotient, external datum, P1/P2/P3, canon verdict or public
posture changes. This finite exact result supplies no positive Krein majorant,
closed Green domain, BV quotient, quantum measure, Standard Model spectrum,
generation count, or cosmological prediction.

The next decisive gate is to derive whether the selected source action owns
`P_epsilon u=u` and/or `D_varpi chi_epsilon=0`, including the variation of the
moving projector and the complement Euler equation. Only then should the
campaign resume gauge, domain and physical reduction work.

## Validation

- exhaustive Python certificate: `39/39 PASS`;
- independent Sage exact implementation: `15/15 PASS`;
- planted failures: fixed projector under unitary escape, frozen moving Euler
  data, observation-as-selector, and commuting-transition assumptions.
