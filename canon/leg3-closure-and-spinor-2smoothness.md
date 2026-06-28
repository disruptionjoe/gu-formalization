---
title: "Leg 3 closure (H3) and the spinor 2-smoothness lemma (M3)"
status: active
doc_type: result
created: 2026-06-28
depends_on: [canon/multiplicity-theorem.md, canon/ghost-parity-krein-synthesis.md]
tests: [tests/generation-sector/leg3_family_embedding_enumeration.py, tests/generation-sector/h1_selfdual_family_kill.py]
---

# Leg 3 closure and the spinor 2-smoothness lemma

Two results that together upgrade the multiplicity finding from "we searched and found a 3" to "the 3 is
the canonical and essentially unique odd-multiplicity route, and we know exactly why."

## M3 -- the spinor 2-smoothness lemma (the positive backbone)

**Lemma.** Let a family / internal symmetry `SO(m)` act on the matter module so that the
generation-multiplicity space is a representation of `SO(m)`. If that multiplicity space is a (sum of)
**spinor** representation(s) of `SO(m)`, its dimension is a power of two, hence not divisible by 3. An odd
generation multiplicity therefore can only come from a **non-spinor** family representation -- a vector,
an adjoint, or a self-dual / principal-`su(2)` representation, whose dimension may be odd.

**Proof.** The Dirac spinor of `SO(m)` has dimension `2^floor(m/2)`; the irreducible half-spinors of
`SO(2k)` have dimension `2^(k-1)`. All are powers of two, and a power of two is never divisible by the odd
prime 3. The vector (`dim m`), the adjoint (`dim m(m-1)/2`), and symmetric / self-dual tensors are not
constrained to powers of two: in particular the self-dual two-form bundle `Lambda^2_+` of a 4-manifold has
dimension 3. Hence any factor of 3 in a generation multiplicity must enter through a non-spinor family
representation. QED.

**Why it matters.** It converts the open-ended search "is there any GU-native odd multiplicity?" into a
sharp dichotomy: the spinor route is provably 3-free, so the only candidate for an odd generation count is
a non-spinor family index. That is exactly the self-dual structure H1 found, and it tells a referee where
the single load-bearing mechanism lives instead of asking them to trust an exhaustive search.

**Instantiation (machine-checked, `h1_selfdual_family_kill.py`).** The self-dual `SU(2)+` decomposition of
the gamma-traceless module is `640` singlets `+ 416` doublets `+ 64` triplets. The `416` doublets (dim 2,
a power of two) are the spinor-route content -- the base Weyl spinor `(2,1)` tensored through. The `64`
triplets (dim 3, odd) are the non-spinor route: they arise from the **vector** base index, via
`(4,1) (x) (2,1) = (2,2) (x) (2,1) = (3+1, 2)`, where the `2 (x) 2 = 3 + 1` that produces the odd 3 comes
from the vector `4 = (2,2)`, i.e. from the self-dual two-form `Lambda^2_+`, not from any spinor. The lemma
predicts this exactly: the 3 is non-spinor or it does not exist.

## H3 -- leg 3 closure (the canonical, unique odd route)

The earlier multiplicity note left a leg open: only maximal-rank `D5` splits had been searched; non-regular
/ principal `su(2)` family embeddings had not. H3 closes this for the family symmetry that commutes with
the full unification group.

**Setup.** `Spin(14) ⊃ Spin(10) x Spin(4)`, so the commutant of the gauge group `Spin(10)` is
`so(4) = su(2)+ (+) su(2)-`. Up to conjugacy `so(4)` has exactly three `su(2)` subalgebras: self-dual
`su(2)+`, anti-self-dual `su(2)-`, and the diagonal / vector `su(2)` (the `so(3)` rotating three base
axes). `su(3)` cannot embed: `dim su(3) = 8 > 6 = dim so(4)`.

**Result (machine-checked, `leg3_family_embedding_enumeration.py`).** The 16-dimensional generation
multiplicity space decomposes under each embedding as:

| family su(2) | multiplicity-space content | odd piece |
| --- | --- | --- |
| self-dual `su(2)+` | `2*(j=0) + 4*(j=1/2) + 2*(j=1)` | TRIPLET `j=1` (dim 3) |
| anti-self-dual `su(2)-` | same (parity image) | TRIPLET `j=1` (dim 3) |
| diagonal / vector `su(2)` | `4*(j=1/2) + 2*(j=3/2)` | NONE (all even / 2-smooth) |

So the only `su(2)` family embeddings producing an odd generation multiplicity are the self-dual and
anti-self-dual `su(2)` (equivalent up to orientation / parity), and the odd multiplicity is always the
**triplet, `j=1`, dimension 3** -- never a quintet (`j=2`, dim 5) or anything higher. No `su(3)` family
symmetry commutes with `Spin(10)`. The self-dual `SU(2)+` is therefore the canonical and essentially
unique odd-multiplicity route, and the count it forces is robustly 3.

## Honest residual

H3 closes leg 3 for family symmetries commuting with the **full** unification group `Spin(10)`. A family
symmetry commuting only with the Standard-Model subgroup `G_SM ⊂ Spin(10)` has a larger commutant in which
a horizontal `su(3)` could in principle live; that case is not covered here and is the remaining scope of
leg 3. It is a bounded next computation (the commutant of `G_SM` in `so(14)` and its `su(3)` content), not
an open-ended search. M3 already constrains it: any odd multiplicity it could produce must again come
through a non-spinor family index, not a spinor one.
