---
artifact_type: exact_lie_closure_and_boundary_polarization_ownership_result
created: 2026-08-14
status: RANK8_NOT_CLOSED__ACTIVE25_GENERATES_FULL_SO77__COVARIANT_POLARIZATION_ORBIT_DIM40__SOURCE_OWNER_ABSENT
source_return: SOURCE_OWNS_FULL_GAUGE_PARENT_AND_NONCHIRAL_TOTAL__SOURCE_SILENT_SPLIT_REDUCTION_W_MIRROR_POLARIZATION_FIELD_BFV_AND_ANALYTIC_DOMAIN
ledger_rows: [RA-G2, LT-SM3, AC-F1, AC-G1a]
canon_verdict_change: none
---

# Selected K77 boundary-edge Lie-closure gate

## Result first

The rank-eight mixed obstruction found at the W/mirror base-boundary pair is
not an eight-dimensional gauge algebra and cannot honestly be repaired by
adding eight independent BFV edge coordinates.

The exact selected coefficient bank activates 25 `so(7,7)` bivectors:

```text
17 split-preserving + 8 mixed.
```

The eight mixed generators are precisely the four base axes crossed with
normal axes `12` and `13`. They are not bracket closed. Their smallest Lie
closure has dimension 15: the eight mixed directions plus seven split
directions. More decisively, the active `17+8` representatives bracket-generate
all 91 directions of `so(7,7)`. The 66 directions with zero tangent image at
the selected coefficient bank are not an ideal, so rank 25 is not the
dimension of an effective quotient gauge algebra.

The smallest full-gauge covariant owner of the W relation is instead the
homogeneous polarization family

```text
Spin(7,7) x_H W,   H = split stabilizer,
dim Spin(7,7) = 91, dim H = 51, dim Spin(7,7)/H = 40.
```

Equivalently, a moving projector `P` obeying `delta P=[X,P]` makes the
constraint `(1-P) psi=0` covariant because

```text
delta((1-P)psi) = X(1-P)psi.
```

This constructs the algebraic shape of a possible edge/polarization
completion, but not its source/action owner. The selected tangent sees only
eight of the forty orbit directions; installing only those eight would be a
background-fitted truncation. The source owns neither a reduction to `H` nor
a 40-coordinate polarization field. The conjugate mirror family is equally
available, so the real action still selects neither member.

## Layer 0

| phrase | exact object | kept distinct from |
| --- | --- | --- |
| rank eight | tangent rank at one selected coefficient bank | Lie-algebra dimension |
| active 25 | nonzero infinitesimal representatives at that bank | quotient gauge algebra |
| split stabilizer `H` | 51-dimensional subgroup preserving W and mirror | selected source gauge group |
| mixed complement | 40-dimensional tangent of `G/H` | bracket-closed subalgebra |
| moving polarization | associated family `G x_H W` | chosen physical W half |
| covariant boundary relation | algebraic constraint bundle | BFV master complex or closed analytic domain |

The carrier is the primal W/mirror one-form sector. It is not either ambient
`C^(32,32)` carrier half, and a gauge-covariant family is not physical
cohomology.

## Broad route-changing lens census

- **Lie theory — selected:** bracket closure decides the edge-carrier size
  before a field is introduced.
- **Representation theory — decisive:** W has the 51-dimensional base/normal
  split stabilizer, so its full orbit has dimension 40.
- **BRST/BFV — adverse:** the ghost bracket forbids an eight-only complex; the
  zero tangent directions cannot be quotiented because their kernel is not an
  ideal.
- **Homogeneous geometry — constructive:** `G x_H W` is the minimal covariant
  polarization family and supplies the exact moving-projector law.
- **Variational/Green — inherited:** the predecessor's base maximal isotropy
  survives pointwise along the covariant orbit; no Green rank is rerun.
- **Symplectic geometry — ceiling:** covariance alone supplies no edge
  symplectic form, moment map, charge or classical master equation.
- **Analytic/PDE — deferred:** a codimension-one interface, closedness,
  Calderon/Lopatinski control and propagation wait for an owned polarization.
- **Source criticism — high:** full gauge ownership does not imply ownership
  of a split reduction or a new coset-valued boundary field.
- **Philosophy of science — anti-fitting:** the observed rank eight is local
  evidence about one background, not permission to install eight adjustable
  compensators.

The selected structural route dominated direct BFV construction because it
decides the minimal carrier and exposes the undercount before functional
analysis. The fallback full group-valued edge frame is unnecessary at this
stage: the 40-dimensional coset is the smaller covariant polarization owner,
while the full 91-dimensional group remains the ghost algebra.

## Exact proof

Write the four base axes as `B={0,7,8,9}` and retain normal axes `12,13` from
the selected coefficient bank. The active mixed set is

```text
{M_b,12, M_b,13 : b in B}.
```

Its brackets produce the six base-base generators and `M_12,13`, yielding a
15-dimensional closure. The active split set contains every normal-normal
generator incident to `12` or `13`. Bracketing these with the active mixed
set generates every base-normal direction; further brackets generate the
remaining split directions. The closure is therefore all 91 bivectors.

An exact reconstruction of the K77 coefficient-bank action independently
reproduces rank `25=17+8` and the generator labels. A planted fixed-projector
control has nonzero mixed variation, whereas allowing `delta P=[X,P]` cancels
it into the covariant constraint identity.

## Hostile boundary

The strongest overclaim is that a 40-dimensional edge field has now been
derived. It has not. The result derives the minimal local homogeneous orbit
needed for full-gauge covariance if this W/mirror boundary route is pursued.
No source term, action equation, preboundary symplectic potential or boundary
condition selects or dynamics this field.

The strongest contrary route is a genuine action-owned reduction of the gauge
group to the split stabilizer. That would avoid the coset edge owner, but no
current source/action law supplies it. The strongest positive control is the
moving-projector covariance identity; the strongest negative control is the
nonzero fixed-projector mixed variation.

Global topology can also obstruct a global coset section even when the local
dimension count is exact. No analytic closedness, well-posedness, positivity,
physical cohomology or member selection follows.

## Progress and next gate

```text
Ledger v0.251 — 82/82 target rows mapped (100%)
32 SAME · 19 DIFFERS · 26 NEEDS · 5 OVER-DETERMINED
Residue: 84 continuous + >=19 function-valued + 9 discrete forks
Tightness: T4x1 T3x3 T2x1 · scoped quotients: 5
Headline delta: none
```

The next gate is ownership, not another finite rank calculation: derive either
the split-stabilizer reduction or the `Spin(7,7)/H` polarization field from the
source action and its preboundary variation. Only then construct the coupled
BFV charge/master equation and a codimension-one analytic domain. Do not add
eight fitted edge fields, choose W or mirror, or call the coset family physical
cohomology.

No verdict, residue, datum, quotient, generation count, canon claim or public
posture changes.

## Reproduction

```sh
sage -python tests/channel-swings/selected_k77_boundary_edge_lie_closure_gate_probe.py
```

The exact probe passes all declared checks.
