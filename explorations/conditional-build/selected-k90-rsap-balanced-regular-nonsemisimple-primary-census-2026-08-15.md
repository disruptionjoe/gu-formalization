---
title: "Selected-K90 RSAP balanced regular-nonsemisimple primary census"
status: active_research
doc_type: exact_regular_skewadjoint_primary_exhaustion_and_rank_certificate
created: "2026-08-15"
registry: lab/process/selected-k90-rsap-balanced-regular-nonsemisimple-primary-census.json
probe: tests/channel-swings/selected_k90_rsap_balanced_regular_nonsemisimple_primary_census_probe.py
grade: "COMPLETE REGULAR NONSEMISIMPLE LOCUS IN Ad(G)p; 547 SIGNED PRIMARY CONFIGURATIONS RANK 91; SINGULAR MIXED JORDAN OPEN"
canon_verdict_change: none
---

# Selected-K90 RSAP balanced regular-nonsemisimple primary census

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.
>
> Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`.

Scope: this is a classical skew-adjoint primary-decomposition and moment-image
result for the K88 balanced symmetric horn. It is not a particle-physics
comparator, source-selected phase space, boundary law, BFV quotient,
quantization or positivity theorem.

## Result first

The complete regular nonsemisimple locus of `so(7,7)` meets the balanced
symmetric complement `p`. The real skew-adjoint primary grammar has four
orthogonal species:

```text
Z_m       zero primary, regular partition [2m-1,1], dimension 2m;
R_d       real eigenvalue pair +/-a, dimension 2d;
I_d^eps   pure-imaginary pair +/-ib with sign characteristic eps, dimension 2d;
L_d       loxodromic quartet +/-a+/-ib, dimension 4d.
```

Regularity is the rank-unit equation

```text
m + sum d(R_d) + sum d(I_d^eps) + 2 sum d(L_d) = 7,
```

with distinct nonzero primary parameters and one Jordan chain on each complex
eigenspace. Nonsemisimplicity means `m>1` or at least one nonzero primary has
`d>1`.

After imposing total form signature `(7,7)`, retaining both imaginary sign
characteristics, quotienting the equal singleton rows at `m=1`, and treating
nonzero spectral parameters as distinct but unordered, the exact finite
structural census contains `547` signed primary configurations. Every one
admits a `Q`-orthogonal involution `R` with

```text
R^2=1,  RX+XR=0,
signature(Q|R=+1)=(3,4) or (4,3).
```

Exact matrices then give the same rank row in all `547` configurations:

```text
dim h = 42, dim p = 49,
rank(ad_X on so(Q)) = 84,
rank(ad_X:h->p) = 42,
rank(ad_X:p->h) = 42,
rank(dJ) = 49+42 = 91.
```

Thus every regular nonsemisimple charge is in the moment image and the map is
submersive there. Together K88, K89 and K90 now cover the complete regular
locus and the complete pure nilpotent cone. The only remaining classical
moment-image gate is the singular mixed-Jordan locus.

## Why this primary grammar is exhaustive

For a real skew-adjoint operator, the minimal polynomial splits into mutually
orthogonal nondegenerate primary subspaces for:

1. a loxodromic conjugate quartet;
2. a pure-imaginary conjugate pair;
3. a nonzero real pair; and
4. the zero primary.

The paired real and loxodromic generalized eigenspaces are complementary null
spaces. Pure-imaginary primary blocks carry a real sign characteristic, and
the zero primary carries the orthogonal signed-partition data used in K89.
This is the canonical decomposition developed in Sections 2--6 of
[Jang--Parker, *Skewadjoint operators on pseudoeuclidean spaces*](https://arxiv.org/abs/math/0302030).
The probe specializes that grammar to real dimension `14`, signature `(7,7)`
and ambient rank `7`.

The number `547` is not a count of individual adjoint orbits. Eigenvalues vary
continuously. It counts signed primary configurations after forgetting the
continuous values and quotienting permutations of distinct primary factors
of the same structural type. The zero-primary distribution is:

| zero rank units `m` | configurations |
|---:|---:|
| `0` | `124` |
| `1` | `167` |
| `2` | `136` |
| `3` | `72` |
| `4` | `28` |
| `5` | `14` |
| `6` | `4` |
| `7` | `2` |

The last row is the two principal `[13,1]` nilpotent forms replayed from K89.
The `m=0` rows prove that the result is not being obtained by hiding every
mixed case inside a zero-primary grading choice.

## Exact blockwise reversing involutions

For a real pair, write `A=J_d(a)` and use

```text
X = diag(A,-A^T),
Q = [0 I; I 0],
R = [0 cH; cH 0],
```

where `H` is the reversal matrix and `c=+/-1`. Then `AH=HA^T`, so `R`
anticommutes with `X` and is `Q`-orthogonal. Changing `c` exchanges the two
possible signature contributions.

For a pure-imaginary pair, let `K_b` be the real rotation matrix, `N_d` the
nilpotent Jordan shift, `D_d=diag(1,-1,...)`, and `C=diag(1,-1)`. With the
alternating reversal `H_d^eps`, use

```text
X = I_d tensor K_b + N_d tensor I_2,
R = D_d tensor C,
Q = H_d^eps tensor I_2       when d is odd,
Q = H_d^eps tensor J_2       when d is even.
```

Both signs `eps` are retained even when the even-`d` form is neutral, because
they are sign-characteristic data rather than a coarse signature count.

For a loxodromic quartet, realify `J_d(a+ib)` and pair it with its negative
transpose using the same hyperbolic `Q`. The reversing graph uses
`H_d tensor C` and contributes `(d,d)` to each grading eigenspace.

The zero primary uses the K89 odd chain plus singleton construction. At
`m=1` the two rows both have size one, so `(+,−)` and `(−,+)` are the same
signed partition; failing to quotient that permutation creates a planted
overcount. The extra zero-primary centralizer direction joins the singleton
to the long-chain endpoints. Its `R`-parity is the product of their grading
colors, so the colors must be opposite. The census imposes that condition
before testing the balanced total signature.

Orthogonal direct sums preserve every identity. The finite search over the
blockwise grading signs finds at least one total `(3,4)|(4,3)` grading for all
`547` signed primary configurations.

## Exact regular rank

The probe checks all `547` assembled representatives against the exact
`Q`-skew, orthogonality, anticommutation and balanced-signature identities.
For rank, it avoids treating repeated occurrences of the same primary block
as independent evidence. Instead it certifies all `88` canonical signed and
graded primary-block variants. Because `R` need not be diagonal in the
canonical primary basis, it projects the complete local orthogonal basis by

```text
Y_h = Y + RYR,
Y_p = Y - RYR
```

and row-reduces the full and fixed adjoint maps. Every block has centralizer
dimension equal to its rank-unit contribution, and every fixed restriction is
injective. Thus each regular primary centralizer lies entirely in the moving
space. Distinct nonzero primary parameters make the primary polynomials
coprime, so the centralizer of an assembled family is the direct sum of these
certified block centralizers. The rank-unit equation makes its dimension
exactly seven in every one of the `547` families.

The local row reductions are over a finite field and supply lower bounds for
characteristic-zero rank. Their matching regular-centralizer and fixed-domain
upper bounds force the same exact rational ranks. Primary direct sum then
gives ambient/fixed/moving ranks `84/42/42` throughout. In particular,
`h intersection g_X=0` on the complete regular nonsemisimple locus. A separate
whole-matrix mutation repeats a real primary parameter and correctly drops
the ambient rank below `84`.

## Surviving gate

K90 closes every regular primary shape, including nontrivial Jordan blocks on
real, imaginary, loxodromic and zero primaries. It does not settle singular
mixed elements. At a singular semisimple value, repeated primary factors
enlarge a real reductive centralizer; the nilpotent part can occupy several
Jordan blocks and can mix multiplicity spaces. One involution must
anticommute with the semisimple and nilpotent parts simultaneously while
retaining the balanced global signature.

The next exact census must therefore be indexed by singular semisimple
centralizer type and nilpotent orbit inside that centralizer. Repeating a
nonzero primary parameter is the cheapest mutation: the probe confirms that
it immediately enlarges the centralizer and exits the regular table.

## Claim ceiling

- The complete regular semisimple locus is covered by K88.
- The complete pure nilpotent cone is covered by K89.
- The complete regular nonsemisimple locus is covered and submersive by K90.
- Singular mixed-Jordan coverage, a target neighborhood of zero,
  surjectivity and RSAP remain open.
- The subgroup `H_bal` remains an admissible construction not selected by the
  source action. No physical BFV, positivity, cohomology, quotient, datum or
  particle-spectrum conclusion follows.
- The ambient `A3` successor remains `TYPE_MISSING`; `[98,182]` is unchanged.

Reproduce with:

```bash
python3 tests/channel-swings/selected_k90_rsap_balanced_regular_nonsemisimple_primary_census_probe.py
```

The probe uses exact integer construction, all-family identity checks and
blockwise rank forcing as described above.
