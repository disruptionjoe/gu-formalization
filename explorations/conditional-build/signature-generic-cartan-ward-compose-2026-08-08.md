---
artifact_type: build_compose_result
created: 2026-08-08
status: SIGNATURE_GENERIC_CARTAN_AND_PRIMITIVE_EPSILON_COMPOSED__K77_K95_LOCAL_HODGE_EXACT__SELECTED_ACTION_FRECHET_OPEN
source_return: SOURCE-CONFIRMS
canon_verdict_change: none
---

# Signature-generic Cartan/Ward composition

## Plain-English result

One item in the current Build queue was stale. The primitive `epsilon` Euler
row was already constructed exactly in ledger v0.25. What had not been done
was to connect it cleanly to ordinary spacetime motion without confusing an
internal gauge transformation with a diffeomorphism.

That connection now closes. Ordinary Lie transport of a connection splits
exactly into two pieces:

```text
L_xi A = i_xi F_A + D_A(i_xi A).
```

The first is a curvature contraction; the second is an internal gauge
direction. Neither piece works alone. For the source's flat pure-gauge second
connection `B`, the curvature piece vanishes and

```text
L_xi B = D_B(i_xi B).
```

Thus the `B` contribution to the Lie derivative of `T=A-B` is precisely a
field-dependent instance of the already-built primitive-epsilon chain, with
`eta=i_xi B`. This composes the two objects without declaring that every
epsilon variation is a spacetime diffeomorphism.

The real-form control also succeeds. K77 and K95 have different Hodge
operators and inertias `(7,7)` and `(9,5)`, but their metric, density, sampled
degree-one/degree-two Hodge and moving-observation naturality packets both pass
independently. The common part is genuinely tensor-natural; the operators are
not being silently ported.

## What this removes from the queue

Do not ask another agent to “construct nonconstant primitive epsilon.” The
source-owned row, Euler chain and compact Green owner already existed. This
wave adds the missing field-dependent Cartan composition.

The remaining burden is narrower:

1. assemble the selected-action Frechet coefficient bank on K77, including
   every actual coefficient;
2. use K95 as a separate real-form control wherever Hodge, Clifford, Krein,
   formal-adjoint or domain data enter;
3. prove coefficientwise `J R=0`; and only then
4. construct `K*`, the formal adjoint, Green/symplectic current and physical
   quotient/domain.

## Exact construction

For a nonabelian connection `A` and adjoint-valued one-form `T`, exact
polynomial matrix witnesses verify

```text
L_xi A = i_xi F_A + D_A(i_xi A),
L_xi T = (i_xi D_A T + D_A i_xi T) + [T,i_xi A].
```

Negative controls show that deleting the curvature contraction, the gauge
derivative or the internal one-form orbit makes the identities fail.

For a live nonconstant vector field and a commuting flat second connection,
`F_B=0` and `D_B(i_xi B)` is nonzero. This prevents the composition from being
a constant-background tautology.

## Branch-native controls

The K77 and K95 packets were recomputed rather than identified:

| object | K77 | K95 |
| --- | ---: | ---: |
| total inertia | `(7,7)` | `(9,5)` |
| Hodge operator | branch-native | different branch-native operator |
| metric/density naturality | exact | exact |
| degree-one Hodge naturality | exact | exact |
| sampled degree-two Hodge naturality | exact | exact |
| moving observation graph | exact | exact |

There are 168 exact branch checks. The explicit plant verifies that the two
Hodge matrices are not equal.

## Constraint accounting

```text
new fields: 0
new coefficients: 0
new functions: 0
new quotients: 0
external datum consumed: 0
P1/P2/P3: unchanged and unused
```

The fit surplus is not diluted: every object was already source-owned or
previously constructed.

## Seven-axis disposition

- **Layer 0:** ordinary Lie, gauge-covariant Lie, internal gauge, primitive
  epsilon, branch Hodge and selected-action Frechet objects remain distinct.
- **L1:** the exact formulas and both signature branches are explicit.
- **L2:** the same connection/distortion field types used by v0.25 are reused.
- **L3:** nonabelian Cartan, flat-pure-gauge and 168 branch checks are exact.
- **L4:** local K77/K95 metric/Hodge/observation geometry closes.
- **L5:** the primitive epsilon row composes, but the full selected-action
  Frechet bank and coefficientwise `J R=0` remain open.
- **L6:** no common Krein fundamental symmetry, adjoint, Green or evolution
  domain is inferred.
- **L7:** no Standard Model, Einstein, cosmology, chirality, mass, anomaly or
  generation verdict changes.

## Evidence

- `tests/channel-swings/signature_generic_cartan_ward_compose_probe.py`
- `lab/process/signature-generic-cartan-ward-compose.json`
- `lab/sources/signature-generic-cartan-ward-source-reinspection-2026-08-08.md`

The production probe passes 204/204.
