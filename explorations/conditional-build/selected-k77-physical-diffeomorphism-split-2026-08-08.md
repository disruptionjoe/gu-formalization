---
artifact_type: construction_result
created: 2026-08-08
status: PHYSICAL_SPLIT_CLOSES_LOCAL_PACKET__LOCAL_NATURALITY_ONLY
source_return: SOURCE-CONFIRMS
---

# Selected K77 physical diffeomorphism split

## Result in plain English

The fourth physical diffeomorphism direction was not missing and does not need
a gamma-generated repair.  The ordinary metric-bundle lift already contains
it.  Three directions are the familiar rotation-like, metric-skew/Kosmann
part; the longitudinal fourth direction is a symmetric deformation of the
metric itself.

On the finite homogeneous packet this natural lift moves the K77 metric,
density, Hodge operator, tautological forms and observation graph together
exactly.  It uses no fitted coefficient, new field, quotient or external datum.

This is a local kinematic naturality theorem.  It is not yet the nonlinear
selected-action Ward theorem: nonconstant primitive epsilon, ordinary field
Lie transport, the expanded residual coefficients, `K*`, the formal adjoint,
Green current and symplectic/BFV/domain descent remain open.

## Layer 0

The wave kept the following objects separate:

1. a base diffeomorphism Jacobian;
2. its natural lift to the metric bundle;
3. the metric-skew/Kosmann component;
4. the symmetric metric complement;
5. an internal `H`-gauge orbit;
6. movement of the observation graph and its equation dual;
7. primitive epsilon variation;
8. representation transport of a residual already equal to zero;
9. the expanded selected-action Frechet differential.

Only 1-4 and 6-8 at homogeneous background grade are closed here.

## Exact construction

For a fixed covector `q` and base vector `xi`, define

```text
B = xi q^T,
B^dagger = eta B^T eta,
K = (B - B^dagger)/2,
S = (B + B^dagger)/2.
```

The natural covariant symmetric-tensor lift is

```text
V(B): k |-> B^T k + k B.
```

With `G = eta direct-sum G_DeWitt` and
`A = diag(-B,V(B))`, the moving metric `h` obeys

```text
h + A^T G + G A = 0.
```

The exact result is the same for timelike, spacelike and null labels:

| object | exact family rank |
| --- | ---: |
| physical base Jacobian `B` | 4 |
| metric-skew/Kosmann component `K` | 3 |
| symmetric component `S` | 4 |
| functorial `Sym2` lift `V(B)` | 4 |

The kernel of the skew family is exactly the longitudinal `q-sharp` line.
That line has zero skew response and nonzero symmetric response.  Thus

```text
physical rank 4 = Kosmann/skew rank 3 + symmetric longitudinal complement,
```

with no gamma-epsilon direction required for physical diffeomorphism
kinematics.

## Natural objects that close

- The moving metric and frame generator satisfy the exact infinitesimal
  isometry identity above.
- `1/2 tr(G^{-1}h) + tr(A) = 0`, so density and frame Jacobian cancel.
- Degree-one Hodge naturality is coefficientwise exact.
- Degree-two Hodge naturality is exact on three preregistered representative
  two-forms; this is a sampled certificate, not an all-91-column theorem.
- The complete frame derivative of tautological `Phi1` vanishes; `Phi2`
  inherits the naturality.
- For observation graph `L=[I;J]`, with `delta J=VJ-JA_H`, both graph and
  equation-dual naturality are exact.  Freezing `J` produces a live
  no-leakage defect.
- A constant primitive epsilon has zero principal Lie response.  A
  nonconstant epsilon has a live lower-order Lie response in every base
  direction.
- A zero raw residual transports to zero in the degree-thirteen output
  representation.  This is representation-level naturality, not an expanded
  coefficientwise action identity.

## Constraint accounting

The construction selected zero continuous parameters, zero discrete choices,
zero functions and no quotient.  P1/P2/P3 are unchanged and unused.  The
constraint surplus is therefore not reduced by fitting.

The calculation uses the declared-base horn `eta` of signature `(1,3)` and
the trace-reversed fibre metric of signature `(6,4)`, whose direct sum has
exact inertia `(7,7)`.  It does not settle the separate Layer-0 question
whether Weinstein's `(1,3)` declaration is the ambient-relevant base input or
only a `Spin(1,3)` gauge-group statement.

## Source collision

The source confirms the metric-bundle and diffeomorphism-orthogonality target.
It is silent on the exact lift and split.  See
`lab/sources/selected-k77-physical-diffeomorphism-split-source-reinspection-2026-08-08.md`.

## What this corrects

The preceding rank-three result remains valid for the internal bivector and
Kosmann/skew orbit.  It was not the full physical base-diffeomorphism tangent.
The earlier gamma-epsilon rank-four construction remains a conditional
internal or possible future soldering object, but it is not needed to supply
the fourth base-diffeomorphism direction.

## Next gate

Expand the nonhomogeneous selected-action Frechet differential with:

1. nonconstant primitive epsilon;
2. field Lie transport;
3. the actual moving connection/curvature/Shiab/Hodge/density coefficients;
4. the moving observation graph and equation dual.

Test the full coefficientwise Ward identity before deriving `K*`, the formal
adjoint, Green concomitant, symplectic current or BFV/domain claims.

## Executable evidence

- `tests/channel-swings/selected_k77_physical_diffeomorphism_split_probe.py`
- `tests/channel-swings/selected_k77_physical_diffeomorphism_split_independent.sage`
