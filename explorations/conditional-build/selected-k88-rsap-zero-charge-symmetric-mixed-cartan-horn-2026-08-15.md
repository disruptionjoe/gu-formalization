---
title: "Selected-K88 RSAP zero-charge balanced symmetric horn"
status: active_research
doc_type: exact_hamiltonian_symmetric_pair_construction_and_regular_cartan_coverage
created: "2026-08-15"
registry: lab/process/selected-k88-rsap-zero-charge-symmetric-mixed-cartan-horn.json
probe: tests/channel-swings/selected_k88_rsap_zero_charge_symmetric_mixed_cartan_horn_probe.py
grade: "98D ZERO-CHARGE RANK-49 HORN; ALL REGULAR SEMISIMPLE REAL CARTAN TYPES RANK-91; SINGULAR COVERAGE OPEN"
canon_verdict_change: none
---

# Selected-K88 RSAP zero-charge balanced symmetric horn

## Result first

K87's real-Cartan obstruction is not universal. A balanced symmetric subgroup
gives a smooth `98D` cotangent horn that contains zero and exact submersive
representatives of all ten real regular-semisimple Cartan spectral classes of
`so(7,7)`, including the action-owned non-loxodromic `(split 5, compact 2)`
class.

Let

```text
G = Spin_0(7,7)
R^(7,7) = U_(3,4) + W_(4,3)
h = so(3,4) + so(4,3).
```

Let `H_bal` be the connected closed symmetric subgroup with Lie algebra `h`.
Globally it is the block-stabilizer image of
`(Spin_0(3,4) x Spin_0(4,3))/diagonal Z2`; writing a plain direct product would
suppress that finite kernel. The quotient changes no Lie-algebra dimension or
differential-rank calculation below.

The involution `S=+1` on `U` and `-1` on `W` gives

```text
so(7,7) = h + p,
h = so(3,4) + so(4,3),  dim h = 42,
p = off-diagonal S-odd part, dim p = 49.
```

Exact matrices verify

```text
[h,h] subset h, [h,p] subset p, [p,p] subset h,
h^perp = p
```

for the trace/Killing pairing. Therefore

```text
M = T*(G/H_bal) = G x_(H_bal) p
dim M = 2(91-42) = 98
J([g,X]) = Ad_g X
image(J) = Ad(G)p.
```

At `[e,0]`, the entire `42D` subgroup stabilizes the point and
`rank(dJ)=49`, saturating `2 rank(dJ)=98+rank(pi_0)`. At `[e,X]`,

```text
dJ(Y,Z) = [Y,X] + Z,  Y,Z in p,
rank(dJ) = 49 + rank(ad_X:p->h)
          = 91 - dim(h intersection g_X).
```

Thus a regular `X` with its seven-dimensional centralizer contained in `p`
has map rank `91` over target rank `84`.

## Ten exact real Cartan controls

A regular real Cartan in the vector representation decomposes into `H`
hyperbolic two-planes, paired positive/negative definite elliptic two-planes
counted by `E`, and `L` neutral loxodromic four-planes. Signature `(7,7)`
forces

```text
H + 2E + 2L = 7,
split rank = H+L,
compact rank = 2E+L.
```

The ten triples `(H,E,L)` with `E+L <= 3` are the ten spectral classes. The
seven split/compact-rank pairs alone are not a complete classification:
`(5,2)`, `(4,3)`, and `(3,4)` occur with more than one loxodromic count.
This is the `O(p,q)` maximal-real-torus block classification specialized to
`p=q=7`; the indecomposable definite, hyperbolic, and neutral `C*` blocks and
conjugacy-by-block-parameters are given in Propositions 2.1--2.4 of
[Dokovic--Thang 1994](https://doi.org/10.4153/CJM-1994-039-5).

### Four non-loxodromic classes

Write the signs of `U` as `+++----` and those of `W` as `++++---`. Pair the
seven `U` lines with `W` using these permutations:

| matching | same-sign pairs | real Cartan type |
|---|---:|---:|
| `(5,6,7,1,2,3,4)` | `0` | `(7,0)` |
| `(1,6,7,5,2,3,4)` | `2` | `(5,2)` |
| `(1,2,7,5,6,3,4)` | `4` | `(3,4)` |
| `(1,2,3,5,6,7,4)` | `6` | `(1,6)` |

Opposite-sign pairs are boost blocks; same-sign pairs are compact rotation
blocks. The seven blocks are disjoint and commute. Distinct positive weights
make every `D7` root value nonzero. Exact row reduction gives ambient adjoint
rank `84`, centralizer dimension `7`, `h`-centralizer dimension `0`, and
moment-map rank `91` for every row.

For the selected `(5,2)` control, weights `(3,1,2,5,4,8,16)` give compact
parameters `3i,5i` and split parameters `1,2,4,8,16`, exactly matching the
K87 excluded spectral type. The whole corresponding Cartan lies in `p`, so
the construction contains a conjugate of every regular element of that type,
not only the printed witness.

### Six loxodromic classes

On a neutral `U_(1,1)+W_(1,1)` four-plane, use the cross-block coefficient
matrix

```text
A = [-3 -3; -3 -2].
```

On one half of that block, `X^2` has trace `5`, determinant `9`, and
discriminant `-11`. It therefore supplies a genuine loxodromic Cartan block,
not a disguised pair of pure real or imaginary blocks. Disjoint copies scaled
by `1,4,16`, plus distinct pure-block weights, give the remaining six classes:

| `H` | `E` | `L` | split/compact rank |
|---:|---:|---:|---:|
| `5` | `0` | `1` | `(6,1)` |
| `3` | `1` | `1` | `(4,3)` |
| `1` | `2` | `1` | `(2,5)` |
| `3` | `0` | `2` | `(5,2)` |
| `1` | `1` | `2` | `(3,4)` |
| `1` | `0` | `3` | `(4,3)` |

Exact row reduction again gives ambient adjoint rank `84`, trivial
`h`-centralizer, `p`-kernel dimension `7`, and moment-map rank `91` in every
class. Together with the four non-loxodromic rows, this exhausts the ten
orthogonal spectral decompositions compatible with signature `(7,7)`.

## Layer 0 and ownership

This is a classical Hamiltonian homogeneous-space construction. It is
canonically obtainable as a right-`H_bal` zero reduction of `T*G`, but neither
the balanced subgroup nor that reduction is selected by the source action. It is
not a physical BFV phase space, boundary condition, quantization, positive
domain, or cohomology result. Ordinary Higgs, family-index, and net-chirality
comparators do not type this question.

## Exact surviving gate

Regular-semisimple coverage is insufficient for a target neighborhood of
zero. The exact remaining membership predicate is:

```text
X belongs to Ad(G)p
iff there is a Q-orthogonal involution R such that
R^2=1, RX+XR=0,
and its eigenspaces have signatures (3,4) and (4,3).
```

The image is conic. Consequently, one missed nonzero orbit and all its
rescalings accumulate at zero outside the image, killing zero-neighborhood
coverage for this horn. The cheapest next order is the signed-Young-diagram
nilpotent census, with the principal `[13,1]` and regular nonsemisimple cases
first, followed only then by mixed Jordan decompositions in singular
semisimple centralizers.

## Claim ceiling

- `T*(Spin_0(7,7)/H_bal)` is a smooth canonical `98D`
  Hamiltonian carrier.
- It achieves map rank `49` at zero and map rank `91` on every real regular-
  semisimple Cartan spectral class.
- It constructs the selected `(5,2)` real-polarization gate and removes K87's
  real-triangular spectral obstruction for this candidate.
- It does not yet prove coverage or submersivity on regular nonsemisimple or
  singular orbits, a target neighborhood of zero, surjectivity, or an RSAP.
- A missed orbit kills only this symmetric horn, not all `98D` Hamiltonian
  models.
- The ambient `A3` successor stays `TYPE_MISSING`; `[98,182]` is not tightened;
  the `182D` cotangent group remains the proved all-charge submersion fallback.
- No canon, ledger, physical-selection, quotient, datum, or public-posture
  change follows.

Reproduce with:

```bash
python3 tests/channel-swings/selected_k88_rsap_zero_charge_symmetric_mixed_cartan_horn_probe.py
```

The certificate uses exact integer and rational arithmetic only.
