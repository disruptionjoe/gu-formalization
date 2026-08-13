---
artifact_type: conditional_build_result
created: 2026-08-07
status: MASSIVE_SPIN2_CLOSURE_EXACT__SPIN0_CHARACTERISTIC_POLYNOMIAL_OPEN
source_return: SOURCE-CONFIRMS__GEOMETRIC_COVARIANCE_AND_FULL_NORM__SOURCE-SILENT__SCALAR_CHARACTERISTIC_COEFFICIENT
ledger: lab/process/conditional-physics-ledger-v0.41.json
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# Selected second-layer massive SO(3) closure and identifiability

## Result in plain English

The massive pair found in the preceding TT calculation cannot remain only two
states in a Lorentz-covariant theory. At a massive rest momentum, ordinary
spatial rotations send the plus/cross pair into three additional
polarizations. Together they form exactly the five-dimensional spin-two
representation.

This closes the predecessor's open massive little-group type:

```text
massive axial weights +/-2
  --SO(3) closure-->
massive spin 2, dimension 5, Casimir -6.
```

The three additional states have axial weights `0,+/-1`. Relative to a chosen
axis they can look “scalar” or “vector,” but they are mandatory members of the
same spin-two particle representation, not optional new fields.

One genuinely separate mode remains: the spatial trace. It is an `SO(3)`
spin-zero representation. Exact commutant algebra proves that the TT result
cannot determine its characteristic polynomial. Two fully rotation-covariant
quadratic operators can agree on all five spin-two states and disagree on
whether the scalar shares the massive pole.

The next honest construction is therefore not a blind scan over five missing
massive states. It is the actual background-subtracted off-TT metric-section
second variation, which must determine the one scalar polynomial, followed by
the separate massless constraint complex.

## Layer 0

| phrase | object proved here | object kept distinct |
| --- | --- | --- |
| axial pair | the plus/cross weight-`+/-2` plane under rotations about one axis | a full massive little-group representation |
| full massive type | the `SO(3)` orbit closure of that plane, dimension five and Casimir `-6` | five positive physical states on a selected global domain |
| scalar | the one-dimensional spatial trace representation | the axial-weight-zero state inside spin two |
| quotient | the finite rest-frame symmetric-tensor complement to the rank-four diffeomorphism image | the full massless constraint/BV quotient |
| identifiability | what covariance plus the TT polynomial fixes | an action-derived off-TT scalar coefficient |

## Exact rest-frame decomposition

For a massive rest covector, the metric diffeomorphism symbol has rank four.
The six complementary coordinates are the spatial symmetric tensors:

```text
Sym2(R3) = Sym2_0(R3) direct-sum R trace
         = spin 2 (dimension 5) direct-sum spin 0 (dimension 1).
```

Starting only with plus and cross, closure under `J12,J23,J31` has rank five.
On that carrier the quadratic Casimir is exactly `-6 I`, the spin-two value.
The trace vector is fixed by all three generators and completes the carrier to
dimension six.

The original `J12` action still squares to `-4 I`, so the predecessor's axial
weight-two result is retained. A planted control verifies that another
rotation sends the two-plane outside itself; calling the pair a full massive
representation would have failed.

## What covariance fixes, and what it cannot fix

The commutant of the exact `SO(3)` action on `Sym2(R3)` has dimension two. Its
two projectors are

```text
P2 = traceless spatial-symmetric projector,
P0 = spatial-trace projector.
```

Thus every invariant quadratic symbol has the form

```text
H(s) = f2(s) P2 + f0(s) P0.
```

The predecessor determines

```text
f2(s) = (14356/13689) s (s + 1922/3589).
```

It says nothing about `f0`. The probe constructs two exact covariant
operators with the same `f2`: one has no scalar pole at `s=-1922/3589`; the
other has a sixth scalar zero there. They agree on plus/cross and on the whole
five-dimensional spin-two closure. This is a planted, exact proof that the
off-TT scalar coefficient cannot be read from TT data.

Consequently, covariance propagates the massive pole across all five spin-two
states, but it does not decide the scalar spectrum.

## Composition with the older native geometry

The repo already knew that the full off-TT higher-codimension variation was
not assembled. In particular, the native constant-background work leaves:

- the coefficient of the full-`B` ambient shear;
- the complete background Euler residual; and
- the background-subtracted metric-section linearization

open. Those are precisely the ingredients that can fix `f0`. The queue now
composes them into the current selected action instead of pretending that a
TT polynomial determines the complete spectrum.

This does not retract the flat/principal TT result. It types its boundary and
turns the former broad “scalar/vector/constraint” task into two ordered gates:

1. compute the single action-owned spin-zero polynomial from the actual
   off-TT section variation;
2. build the distinct massless diffeomorphism/constraint complex.

## Source return

The released material confirms the full connection-difference norm, the
gauge-rotated Levi-Civita connection locus, and the geometric covariance that
motivates the massive little-group test. It does not print the selected
scalar characteristic coefficient, the background-subtracted variation, or
the physical domain.

```text
SOURCE-CONFIRMS:
  geometric connection covariance and the full augmented-torsion norm

SOURCE-SILENT:
  f0(s), the full off-TT section variation, massless constraint descent,
  common Green/Krein domain and BV/BFV reduction
```

## Six-lens hostile review

- **Differential geometry:** the rest-frame carrier is the actual symmetric
  metric tensor. The ambient full-`B` and background-subtracted second
  variation remain mandatory.
- **Representation theory:** orbit rank five and Casimir `-6` establish spin
  two. Dimension alone was not used. The spatial trace is a distinct spin-zero
  irrep.
- **Variational PDE:** covariance forces degeneracy within spin two; it does
  not supply the scalar characteristic polynomial or massless constraints.
- **Symplectic geometry:** no boundary polarization, Green-Lagrangian domain,
  covariant phase space or BFV quotient is selected.
- **Krein/operator theory:** the local opposite pole signs remain finite
  algebra. No common closed right-`H` domain or positive energy follows.
- **Source criticism:** the source owns the geometric directive, not the
  exact spin decomposition or an unprinted scalar coefficient.

The two named hostile charges both fired as repairs. The summary no longer
calls the two-plane a massive representation, and the next lane no longer
defends the superseded idea that every non-TT component is an unidentified
extra representation.

## Progress and next gate

```text
Ledger v0.41 — 82/82 active target rows mapped (100%)
32 SAME · 19 DIFFERS · 25 NEEDS · 6 OVER-DETERMINED
Residue — 84 continuous + >=19 function-valued + 9 forks
Quotients ranked — 4 scoped

headline_delta: none
frontier_conditions_closed: 3
  - massive full SO3 type = spin two
  - three missing axial polarizations = forced spin-two partners
  - TT-to-scalar identifiability boundary
frontier_conditions_opened: 0
remaining_named_conditions: 3
  - action-derived spin-zero characteristic polynomial
  - massless constraint complex
  - coupled nonzero-fermion Hessian and common domain
```

No coefficient, external datum or fifth quotient is added. P1/P2/P3 remain
unused. Curt remains formally separate and no third lane is promoted.

## Verification

`tests/channel-swings/selected_second_layer_massive_so3_closure_probe.py`
passes `31/31`, including two planted failures. An independent Sage/QQ orbit
calculation reproduces closure dimension five and the trace-completed
dimension six.
