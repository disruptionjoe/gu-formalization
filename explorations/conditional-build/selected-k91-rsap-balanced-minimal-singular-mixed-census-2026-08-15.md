---
title: "Selected-K91 RSAP balanced minimal-singular mixed census"
status: active_research
doc_type: exact_minimal_singular_mixed_primary_exhaustion_and_rank_certificate
created: "2026-08-15"
registry: lab/process/selected-k91-rsap-balanced-minimal-singular-mixed-census.json
probe: tests/channel-swings/selected_k91_rsap_balanced_minimal_singular_mixed_census_probe.py
grade: "COMPLETE CENTRALIZER-9 MIXED STRUCTURAL LOCUS IN Ad(G)p; 714 CONFIGURATIONS RANK 90; CENTRALIZER AT LEAST 11 OPEN"
canon_verdict_change: none
---

# Selected-K91 RSAP balanced minimal-singular mixed census

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

Scope: this is a classical real skew-adjoint primary-decomposition and
moment-image result for the balanced symmetric horn. Ordinary Higgs,
family-index and chirality models are not inputs and cannot be successors to
this calculation.

## Result first

K91 closes the first genuinely singular mixed layer of `so(7,7)`: every
signed structural configuration with centralizer dimension `9` has a balanced
representative in the K88 symmetric complement `p`.

There are exactly `714` such mixed configurations after continuous spectral
values and permutations of distinct primary parameters are forgotten:

| source of centralizer excess two | configurations |
|---|---:|
| one real or imaginary nonzero primary with partition `[d,1]` | `590` |
| a minimal-singular zero primary plus regular nonzero complement | `124` |
| **total** | **`714`** |

Every representative has

```text
dim g_X = 9,
rank(pi_X) = 91-9 = 82,
dim(h intersection g_X) = 1,
rank(dJ) = 91-1 = 90.
```

This saturates the sharp `98D` pointwise Poisson bound

```text
rank(dJ) <= (98+82)/2 = 90.
```

Purely semisimple centralizer-nine walls are already contained because every
real semisimple element lies in a real Cartan and K88 places all ten real
Cartan classes in `p`. K91 supplies the previously missing mixed part. The
next uncovered singular mixed strata have centralizer dimension at least
`11`.

## Why this is the complete first mixed stratum

Write the real Jordan decomposition as `X=S+N`, with `[S,N]=0`. Primary
decomposition reduces the centralizer of `X` to the sum of centralizers of the
nilpotent partitions inside the real semisimple primary factors. The complete
real skew-adjoint canonical grammar is the one used in K90 and follows
[Jang--Parker's classification of skew-adjoint operators on pseudoeuclidean
spaces](https://arxiv.org/abs/math/0302030).

For a real or pure-imaginary primary of total multiplicity `n`, a nilpotent
partition `lambda` contributes

```text
sum_j (lambda'_j)^2
```

centralizer dimensions. A single chain `[n]` contributes `n` and is regular.
Exhausting all partitions through `n=7` proves that excess exactly two occurs
only for

```text
lambda = [n-1,1] = [d,1].
```

This includes `[1,1]`: the nilpotent inside that repeated primary is zero, so
the total charge is mixed only when another regular primary carries a
nonzero nilpotent part. K90's regular-nonsemisimple families impose exactly
that condition. Loxodromic centralizers are realifications of complex ones,
so their first nonzero excess is four, not two.

For a zero primary with orthogonal partition `lambda`, the exact centralizer
formula is

```text
c(lambda) = (sum_j (lambda'_j)^2 - number_of_odd_rows)/2.
```

Exhaustion in dimensions `4,6,8,10,12` gives the only excess-two shapes:

```text
dimension 4:       (2,2),
dimension 2m>=6:   (2m-3,3).
```

Dimension `14` would leave no nonzero complement and is pure nilpotent, hence
belongs to K89 rather than the mixed census. The two mechanisms above are
disjoint and exhaust centralizer dimension `7+2=9`.

## Exact counts

The `590` nonzero-primary rows split as follows:

| primary kind | configurations |
|---|---:|
| real | `212` |
| pure imaginary, retaining both sign characteristics | `378` |

By long-chain size `d`, their distribution is
`272,213,71,27,6,1` for `d=1,...,6`.

The `124` singular-zero rows split by zero-primary rank units as

| zero rank units | configurations |
|---:|---:|
| `2` | `34` |
| `3` | `44` |
| `4` | `28` |
| `5` | `14` |
| `6` | `4` |

These are finite signed structural counts, not counts of individual adjoint
orbits: nonzero spectral parameters remain continuous.

## Simultaneous balanced reversal

For a nonzero collision, the probe starts from a K90 balanced configuration
and sets the parameters of one size-`d` chain and one singleton chain equal.
The same exact involution still anticommutes with the full matrix. Exact local
row reduction checks all `48` real/imaginary signed and graded collision
models. In every case the new two-dimensional centralizer contribution splits
as one fixed and one moving direction.

The zero primary contains the only new parity seam. There are `61` signed and
graded local controls. Exactly `31` have the optimal centralizer split and
`30` do not. For two odd chains, the optimal choices give the chains opposite
grading colors; same-color choices put both excess directions on the wrong
side. Crucially, every signed zero-primary row has at least one optimal choice,
and every one of the `124` global configurations can combine such a choice
with its nonzero complement to reach `(3,4)|(4,3)`.

All `714` assembled representatives are then checked exactly for

```text
signature(Q)=(7,7),
R^2=1,
R^T Q R=Q,
RX+XR=0,
X^T Q+QX=0,
signature(Q|R=+1)=(3,4) or (4,3).
```

Primary coprimality makes the global centralizer the direct sum of the local
centralizers. The regular complement contributes seven moving directions;
the singular primary adds one fixed and one moving direction. Hence the exact
global ranks are `82/41/41` for the ambient, fixed and moving adjoint maps,
and `rank(dJ)=49+41=90`.

## Surviving gate

K88--K91 now cover the complete regular locus, the pure nilpotent cone, all
semisimple charges, and the first singular mixed layer. This is not yet a
zero-neighborhood theorem. Centralizer dimensions `11,13,...` arise from
larger partition excess, multiple simultaneous primary collisions and higher-
rank semisimple centralizers with nonregular internal nilpotents. Those
configurations require their own simultaneous-reversal census.

## Claim ceiling

- All `714` centralizer-nine mixed structural configurations meet `Ad(G)p` and
  saturate map rank `90`.
- Combined with K88, the complete centralizer-nine singular layer is covered.
- Singular mixed strata with centralizer dimension at least `11`, a target
  neighborhood of zero, surjectivity and RSAP remain open.
- `H_bal` remains an admissible construction not selected by the source
  action. No physical BFV, positivity, quotient, datum, particle-spectrum or
  source-action conclusion follows.
- The ambient `A3` successor remains `TYPE_MISSING`; `[98,182]` is unchanged.

Reproduce with:

```bash
python3 tests/channel-swings/selected_k91_rsap_balanced_minimal_singular_mixed_census_probe.py
```

The probe uses exact integer matrices and finite-field rank forcing with
matching characteristic-zero centralizer bounds.
