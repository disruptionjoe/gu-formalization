---
title: "Selected-K87 RSAP zero-charge maximal-unipotent horn"
status: active_research
doc_type: exact_hamiltonian_cotangent_construction_and_target_coverage_obstruction
created: "2026-08-15"
registry: lab/process/selected-k87-rsap-zero-charge-maximal-unipotent-horn.json
probe: tests/channel-swings/selected_k87_rsap_zero_charge_maximal_unipotent_horn_probe.py
grade: "98D ZERO-CHARGE RANK-49 HORN CONSTRUCTED; SPLIT-REGULAR SUBMERSION; FULL ZERO-NEIGHBORHOOD COVERAGE FAILS"
canon_verdict_change: none
---

# Selected-K87 RSAP zero-charge maximal-unipotent horn

## Result first

The zero-charge rank ceiling is nonlinearly attainable on a smooth
`98`-dimensional Hamiltonian carrier.

Let

```text
G = Spin_0(7,7)
N = a maximal split unipotent subgroup of G.
```

The `D7` root system has `42` positive roots, so

```text
dim G       = 91
dim N       = 42
dim G/N     = 49
dim T*(G/N) = 98.
```

The cotangent lift of the left `G` action has its canonical equivariant moment
map

```text
J(q,p)(xi) = p(xi_G/N(q)).
```

At the zero covector over `eN`, the entire `42D` group `N` stabilizes the
point. Consequently

```text
rank(dJ) = dim G - dim N = 49,
J = 0,
rank(pi_0) = 0.
```

Thus the exact pointwise inequality `2 rank(dJ) <= 98+rank(pi)` is saturated,
not merely approached. At a regular split-Cartan covector, the infinitesimal
`N` stabilizer is zero, so the same moment map has rank `91` over target
Poisson rank `84`. This is a genuine smooth symplectic construction joining a
split-regular submersive locus to zero.

It is not an RSAP zero-neighborhood chart. Its image misses every regular
mixed/elliptic Cartan type, including the action-owned `(split 5, compact 2)`
endpoint and arbitrarily small rescalings of it.

## Exact matrix model

Use the isotropic metric

```text
eta = [[0,I7],[I7,0]].
```

Then every element of `so(7,7)` has the form

```text
X = [[A,B],[C,-A^T]],   B^T=-B, C^T=-C.
```

The `91` coordinates divide as `49+21+21`. Choose the standard positive
`D7` roots:

- `e_i-e_j`, represented by strictly upper-triangular `A` entries;
- `e_i+e_j`, represented by the `21` skew `B` entries.

Their span is the `42D` nilradical `n`. Exact bracket checks close both `n`
and

```text
b = a+n = {A upper triangular, B skew, C=0}.
```

The Killing form is a nonzero multiple of `tr(XY)`. Its pairing has rank `42`
on `n`, and the `49D` space `b` is orthogonal to every element of `n`.
Therefore

```text
n^perp = b.
```

The cotangent fibre over `eN` is `n^ann`, identified with `b`; equivariance
then gives the complete moment image

```text
image(J) = Ad(G)b.
```

## Why zero-neighborhood coverage fails

Every matrix in `b` is block upper triangular. Its vector-representation
eigenvalues are the real diagonal entries of `A` and their negatives.
Conjugation does not change eigenvalues, so every charge in `Ad(G)b` is real-
triangularizable.

By contrast, an exact regular `(5,2)` Cartan witness has five boost parameters

```text
1, 2, 4, 8, 16
```

and two compact rotation parameters

```text
3i, 5i.
```

No `D7` root `+-z_i+-z_j` vanishes, so the witness is regular. Its four
nonreal vector eigenvalues exclude it from `Ad(G)b`. Every nonzero scalar
multiple is still excluded and converges to zero as the scalar tends to zero.
Hence the image contains no full target neighborhood of zero.

This is stronger than merely saying the map is not globally onto: the natural
maximal-unipotent horn fails the local coverage condition needed to glue all
regular Cartan chambers through zero.

## Layer 0 and comparator routing

This is a classical Hamiltonian homogeneous-space construction. It is not a
boundary condition selecting the physical zero-charge horn and is not a
source-owned phase space. The ordinary Higgs model, ordinary family index,
and net-chirality target do not type its stabilizer or moment image and remain
irrelevant.

## Claim ceiling and next gate

- `T*(Spin_0(7,7)/N)` is a smooth symplectic `98D` carrier with a canonical
  Poisson moment map.
- It achieves rank exactly `49` at zero and rank `91` over a split-regular
  locus. The pointwise zero ceiling is therefore nonlinearly sharp.
- Its image is exactly `Ad(G)b`, not all of `so(7,7)*`.
- It excludes the action-owned `(5,2)` Cartan type and has no full target
  neighborhood of zero. This candidate is killed as an RSAP zero chart.
- No general obstruction to another `98D` zero-neighborhood construction is
  proved. Nonhomogeneous models and cotangent horns with other `42D`
  stabilizers remain open.
- The ambient `A3` successor and cross-real-form incidence are not used or
  reopened. Global all-strata RSAP remains open, with the `182D` cotangent
  group as fallback.
- No canon, ledger, residue, quotient datum, physical interpretation or public
  posture changes.

Next classify alternative `42D` stabilizer cotangent horns—or construct a
nonhomogeneous `98D` model—and require its moment image to meet the action-
owned `(5,2)` mixed Cartan type before any gluing work.

Reproduce with:

```bash
python3 tests/channel-swings/selected_k87_rsap_zero_charge_maximal_unipotent_horn_probe.py
```

The certificate uses exact integer and rational arithmetic only.
