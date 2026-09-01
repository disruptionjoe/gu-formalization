---
title: "K80 I1B matrix-density half-density wave"
status: active_research
doc_type: reverse_scaffold_i1b_matrix_density_half_density_result
date: 2026-09-01
target_claim: NONE-NOT-A-KILL
claim_ceiling: exact principal compatibility, complete positive two-by-two matrix-weight classification and matrix half-density transport for one repository-owned control; no source cross-null operator, physical density, rank-jump boundary law or coefficient selector
manifest: lab/process/k80-i1b-matrix-density-half-density-wave.json
probe: tests/channel-swings/k80_i1b_matrix_density_half_density_probe.py
---

# K80 I1B matrix-density half-density wave

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`

```gu-typed-objects
result: complete formal-symmetry classification of positive Hermitian two-by-two matrix densities for the frozen principal matrix J, plus exact matrix half-density transport
carrier: complex two-component sections on 0<u<1 with repository-owned C1 positive Hermitian density W(u) LAYER=conditional CHIRALITY=N/A
pairing: positive L2(W du) pairing transported by the canonical matrix half-density U=W^(1/2)
real_structure: componentwise conjugation with real principal matrix J; nonscalar admissible W is complex Hermitian and diagonal in the complex J-eigenbasis
grading: the two J eigenchannels with positive weights w_plus and w_minus; no gauge, BRST, BV or physical grading
action_owner: repository owns the matrix-density countercontrol only; no filed source action owns its operator, density, lower-order potential, domain or boundary relation
target: whether a non-power-law matrix-valued physical-density surrogate can leave an invariant beyond scalar half-density transport MAP-TYPE=classification
```

## Result first

For the frozen two-component principal matrix

```text
J=[[0,-1],[1,0]],          J^dagger=-J,       J^2=-I,        (1)
```

formal symmetry does not permit an arbitrary positive matrix density. The
principal term forces the density to commute with `J`. Every allowed positive
Hermitian `2 x 2` density is therefore diagonal in the two complex
`J`-eigenchannels. Its complete connection correction is removed by the
matrix half-density `U=W^(1/2)`. Weight transport alone again selects neither
`log(2)` nor `log(3)`.

This extends the scalar power-law result to the entire positive matrix-weight
class compatible with the frozen principal symbol. It does not derive the
actual I1B cross-null operator, physical density, matching law or spectrum.

## Formal-symmetry equations

Freeze

```text
D=J d/du+A(u),
<f,g>_W=integral f^dagger W(u)g du,                           (2)
```

where `W=W^dagger>0` is `C1`. Integration by parts gives

```text
<f,Dg>_W-<Df,g>_W
=[f^dagger WJg]
 +integral f^dagger[-W'J+WA-A^dagger W]g du,                (3)
```

provided the derivative coefficients agree. The full pointwise conditions are

```text
WJ=JW,                    WA-A^dagger W=W'J.                 (4)
```

The first equation is not optional: if `W` does not commute with `J`, the
coefficients of `f'` differ before any lower-order correction can act.

## Complete positive matrix-weight classification

Write a general Hermitian matrix as

```text
W=[[x,z],[conjugate(z),y]].                                  (5)
```

Solving `[W,J]=0` gives `x=y` and `z` purely imaginary. Hence

```text
W=aI-beta iJ=[[a,i beta],[-i beta,a]],                       (6)
```

with eigenweights

```text
w_plus=a+beta,             w_minus=a-beta.                   (7)
```

Positivity is exactly `a>|beta|`, or equivalently `w_plus,w_minus>0`.
Thus the admissible matrix-valued extension is real and substantial but still
commutative: it consists of two independently weighted complex `J`
eigenchannels. A genuinely noncommuting positive density cannot make the
fixed `J d/du` principal part formally symmetric.

## Canonical matrix half-density

Because all matrices in (6) commute pointwise and across `u`, define

```text
A_W=(1/2)W^(-1)W'J.                                         (8)
```

Then `A_W^dagger=-A_W` and

```text
WA_W-A_W^dagger W=W'J.                                      (9)
```

Every solution of the lower-order equation is

```text
A=A_W+V,                  WV=V^dagger W.                    (10)
```

Let `U=W^(1/2)`. Since `U` commutes with `J` and
`U'U^(-1)=(1/2)W^(-1)W'`, direct conjugation gives

```text
U(J d/du+A_W)U^(-1)=J d/du,                                 (11)
U D U^(-1)=J d/du+U V U^(-1).                               (12)
```

The transported potential `UVU^(-1)` is Hermitian. The Green form transports
exactly:

```text
f^dagger WJg=(Uf)^dagger J(Ug).                              (13)
```

Therefore minimal/maximal domains and extension data are again weight
coordinates, while an independently owned lower-order potential or boundary
relation can remain as genuine operator data.

## Exact nonscalar control

Choose the two positive eigenweights

```text
w_plus=(1+u)^2,             w_minus=(2+u)^2.                 (14)
```

Then (6) is genuinely nonscalar, while `U` has eigenweights `1+u` and
`2+u`. The exact identities (8)--(13) remove the full matrix connection. This
control is stronger than repeating the scalar power-law case: the two
principal eigenchannels carry different non-power-law weights, yet no weight
invariant survives canonical transport.

What can survive is now sharply localized: an independently source-owned
`W`-self-adjoint `V`, a singular residue not absorbed into (8), a rank-jump
matching relation, a spectral datum, or a boundary law. The density by itself
does not distinguish the candidate tangential coefficients.

## Hostile review and claim ceiling

The strongest overclaim would say every positive matrix density is removable.
The theorem first requires principal compatibility with this exact fixed `J`;
noncommuting weights are excluded, not conjugated. The strongest contrary
route is an independently owned lower-order or boundary invariant, preserved
as `UVU^(-1)` or transported domain data rather than erased. The weakest
reproducibility seam is the matrix square root; the probe uses the explicit
positive eigenweights (14), whose square roots are rational affine functions.

No native I1B source packet currently owns `J`, `W`, `A`, `V`, a physical
pairing, the cross-null normal operator, the rank-jump matching law or its
spectrum. No prediction, confirmation, held-out score or GU verdict follows.

## Next condition

Derive the source-owned cross-null principal matrix, physical density,
lower-order potential and rank-jump boundary or spectral law together. Then
perform the same half-density transport and test the surviving Hermitian
potential, residue, matching and spectral invariants against `log(2)` and
`log(3)`.

Reproduce with:

```bash
python3 tests/channel-swings/k80_i1b_matrix_density_half_density_probe.py
python3 tests/channel-swings/k80_i1b_matrix_density_half_density_probe.py --selftest
```
