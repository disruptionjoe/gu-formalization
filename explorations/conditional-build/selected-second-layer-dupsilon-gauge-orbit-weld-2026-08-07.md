---
artifact_type: conditional_build_result
created: 2026-08-07
status: RANK4_CONNECTION_ORBIT_WELD_FORCED__TRANSVERSE_OWNER_OPEN
source_return: SOURCE-CONFIRMS__METRIC_PLUS_CONNECTION_ORBIT__SOURCE-SILENT__ACTION_DUPSILON_CROSS_BLOCK
ledger: lab/process/conditional-physics-ledger-v0.43.json
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# Selected second-layer D Upsilon gauge-orbit weld

## Result in plain English

The missing co-moving correction is no longer an unspecified enormous object
at its first decisive gate.

The current metric block produces four independent failures of the
diffeomorphism Ward identity. At a residual-zero norm-square point, that
forces the metric part of `D Upsilon` to move in four independent directions
along the four-dimensional diffeomorphism orbit. The source-native connection
one-form orbit also has exactly rank four. It is therefore precisely large
enough to cancel the metric response—no extra field or external datum is
needed for this gauge-orbit burden.

The correction is unique on those four connection-orbit columns. It is not
unique on the other twelve connection directions. An exact diagnostic weld
closes the coupled Ward radical and an exact transverse plant changes the
off-orbit block without changing the weld. Thus the next action calculation is
only four columns:

```text
differentiate selected Upsilon on G_T(k)xi
and compare it with -D_g Upsilon(D_gauge(k)xi).
```

If that comparison fails, the selected action/owner route is wrong or needs
section/observation participation already on the gauge orbit. If it passes,
the remaining transverse connection and section/observation derivatives can
be built afterward.

## Layer 0

| phrase | object proved here | object kept distinct |
| --- | --- | --- |
| residual naturality | `D Upsilon R=0` at an invariant residual-zero point | source redundancy `Xi=D Upsilon` |
| Ward load | `H_gg D` for the selected metric block | the residual response `J_g D` itself |
| rank theorem | `rank(H_gg D)<=rank(J_gD)<=4`, with both bounds equal four | coefficientwise construction of `J_gD` |
| connection orbit | principal diffeomorphism Lie symbol `G_T(k)` of rank four | Lorentz connection gauge or all connection variations |
| diagnostic weld | symmetric completion fixed on `im G_T` | action-derived cross and transverse blocks |
| radical | unreduced gauge directions killed by the Hessian | BV cohomology, BFV phase space or physical quotient |

This also prevents a known homonym: the draft relation `Xi=D Upsilon` is a
redundant Euler equation. It is not the diffeomorphism Ward identity used here.

## Exact rank theorem

At the generic exact rest value used by the predecessor,

```text
rank D_metric = 4,
rank(H_gg D_metric) = 4,
rank G_T = 4,
rank(D_metric,G_T) = 4.
```

For a stationary residual square `H_gg=J_g^! G_res J_g`, rank monotonicity
gives

```text
4 = rank(H_gg D_metric)
  <= rank(J_g D_metric)
  <= rank(D_metric) = 4.
```

Therefore `rank(J_gD)=4`. This inference does not require the residual pairing
to be positive definite; it uses only factorization and rank monotonicity.

Because `G_T` is injective, a cancellation map is uniquely defined on its
image. With any exact left inverse `L G_T=1`, the Hessian-level representative

```text
H_gT = -(H_gg D_metric)L
```

obeys `H_gg D_metric+H_gT G_T=0`. The corresponding symmetric diagnostic
completion kills the full coupled orbit on both sides and preserves the
metric block exactly.

The complement projector `1-G_TL` has rank twelve. Adding any nonzero map
through it leaves the four-column weld unchanged. Ward symmetry therefore
fixes the orbit restriction, not the transverse action.

## Why frame/epsilon transport is not the missing field block

The completed selected-`Cl2` theorem already proves that derivatives of the
moving residual target metric, frame, epsilon and observation transport
multiply `Upsilon(0)` and vanish at stationary quadratic grade. They preserve
naturality but cannot be credited with this nonzero field-variable rank-four
response. The live candidates are the connection, section and observation
arguments of `Upsilon`; the connection orbit is the cheapest exact test
because its rank already matches.

## Source return

```text
SOURCE-CONFIRMS:
  I1B owns both metric and inhomogeneous connection data;
  augmented torsion is an adjoint-valued one-form;
  the second layer is a residual norm square.

SOURCE-SILENT:
  the selected action's four D Upsilon connection-gauge columns,
  the transverse twelve-column derivative, BV quotient and domain.
```

## Specialist and hostile review

- **Differential geometry:** naturality fixes only the gauge-orbit restriction;
  no transverse derivative is invented.
- **Representation theory:** the result uses rank and injectivity, not a
  dimension-only identification.
- **Variational PDE:** residual cancellation and Hessian radicality stay
  separate; the actual four-column Jacobian is the next test.
- **Symplectic geometry:** a four-dimensional radical is not a coisotropic
  reduction, presymplectic quotient or BFV phase space.
- **Krein/operator theory:** the rank inference remains valid for the
  indefinite residual pairing, but says nothing about a closed domain or
  energy sign.
- **Source criticism:** the source types the owner and is silent on the
  coefficientwise weld; `Xi=D Upsilon` is not substituted for Ward.
- **Repo archaeology:** v0.32's coupled-orbit theorem is composed rather than
  recomputed or misattributed to the current second action.

Both hostile charges fired as fences. The summary may not call the diagnostic
weld action-derived, and the lane may no longer defend a full 16-column build
before testing the four already-forced columns.

## Progress and next gate

```text
Ledger v0.43 — 82/82 active rows mapped (100%)
32 SAME · 19 DIFFERS · 25 NEEDS · 6 OVER-DETERMINED
Residue — 84 continuous + >=19 function-valued + 9 forks
Quotients ranked — 4 scoped

headline_delta: none
frontier_conditions_closed: 3
  - forced residual gauge-response rank = 4
  - available connection diffeomorphism orbit rank = 4
  - diagnostic weld exists and is unique on the orbit
frontier_conditions_opened: 0
remaining_named_conditions: 4
  - actual selected-Upsilon four-column comparison
  - twelve transverse connection plus section/observation derivatives
  - scalar and massless constraint quotient
  - coupled fermion Hessian and common domain
```

No scalar pole, coefficient, external datum or fifth quotient is added.
P1/P2/P3 remain unused. Curt remains formally separate and no third lane is
promoted.

## Verification

`tests/channel-swings/selected_second_layer_dupsilon_gauge_orbit_weld_probe.py`
passes `37/37`, including planted failures against connection-orbit deletion,
transverse-block inference, BV promotion and external-datum substitution.
