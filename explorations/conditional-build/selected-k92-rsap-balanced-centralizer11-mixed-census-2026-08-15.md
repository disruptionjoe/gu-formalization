---
title: "Selected-K92 RSAP balanced centralizer-11 mixed census"
status: active_research
doc_type: exact_higher_singular_mixed_primary_exhaustion_and_rank_certificate
created: "2026-08-15"
registry: lab/process/selected-k92-rsap-balanced-centralizer11-mixed-census.json
probe: tests/channel-swings/selected_k92_rsap_balanced_centralizer11_mixed_census_probe.py
grade: "COMPLETE CENTRALIZER-11 MIXED STRUCTURAL LOCUS IN Ad(G)p; 673 CONFIGURATIONS RANK 89; CENTRALIZER AT LEAST 13 OPEN"
canon_verdict_change: none
---

# Selected-K92 RSAP balanced centralizer-11 mixed census

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
moment-image result for the K88 balanced symmetric horn. It is not a
source-selected phase space, action, boundary law, BFV quotient, quantization,
positivity theorem or particle-physics comparator.

## Result first

K92 closes the next higher-singular mixed layer of `so(7,7)`: every signed
structural configuration with centralizer dimension `11` has a balanced
representative in the K88 symmetric complement `p`.

The finite census has exactly `673` configurations after continuous spectral
values and permutations of distinct primary parameters are forgotten:

| source of total centralizer excess four | configurations |
|---|---:|
| one real, imaginary or loxodromic excess-four primary | `137` |
| two distinct nonzero excess-two primaries | `169` |
| one zero primary of excess four plus regular complement | `283` |
| one zero-primary and one nonzero-primary excess-two collision | `84` |
| **total** | **`673`** |

Every representative has

```text
dim g_X = 11,
rank(pi_X) = 91-11 = 80,
dim(h intersection g_X) = 2,
rank(dJ) = 91-2 = 89.
```

Thus the complete layer saturates the sharp `98D` pointwise Poisson bound

```text
rank(dJ) <= (98+80)/2 = 89.
```

Together K88--K92 cover every semisimple charge, the complete regular locus,
the pure nilpotent cone, and the first two singular mixed layers. The next
uncovered mixed strata have centralizer dimension at least `13`.

## Why the excess-four grammar is exhaustive

For a real or pure-imaginary primary whose nilpotent multiplicity partition is
`lambda`, the centralizer contribution is

```text
sum_j (lambda'_j)^2.
```

Exhausting partitions through multiplicity seven proves that the only
primitive excess-four partition is `[n-2,2]`, including `[2,2]`. Loxodromic
primaries are realifications of complex primaries, so their first singular
partition `[n-1,1]` doubles complex excess two to real excess four. The
remaining nonzero mechanism is the direct sum of two excess-two `[d,1]`
collisions at distinct primary parameters.

For an orthogonal zero primary,

```text
c(lambda) = (sum_j (lambda'_j)^2 - number_of_odd_rows)/2.
```

The excess-four partitions in dimensions four through twelve are

```text
4:   [1,1,1,1]
6:   [3,1,1,1]
8:   [4,4], [5,1,1,1]
10:  [5,5], [7,1,1,1]
12:  [7,5], [9,1,1,1].
```

The four-dimensional all-singleton zero primary is semisimple. The census
therefore retains it only when its regular nonzero complement already has a
nonzero nilpotent part; the `24` fully semisimple rows are excluded as K88
coverage rather than mislabeled mixed configurations. The last mechanism
combines one K91 excess-two zero primary with one K91 real or imaginary
excess-two collision. These primitive and additive possibilities exhaust
total excess four.

## Exact structural counts

The `137` primitive nonzero rows split into

| primary kind | configurations |
|---|---:|
| real `[n-2,2]` | `35` |
| pure imaginary `[n-2,2]`, retaining all chain signs | `87` |
| loxodromic realification of `[n-1,1]` | `15` |

The `169` double-collision rows split into `30` real/real, `63`
real/imaginary, and `76` imaginary/imaginary pairs. Collision pairs are
unordered, but their two primary parameters remain distinct.

The zero-primary census tests `621` signed grading allocations. Exactly `237`
put two centralizer dimensions in `h`; every signed row has at least one such
optimal allocation. Combining those rows with their regular complements gives
`283` mixed configurations. Adding the `84` zero-excess-two plus
nonzero-excess-two rows completes the count.

## Simultaneous balanced reversal and exact rank

Each nonzero primary is assembled from the K90 canonical blocks with the
appropriate Jordan chains assigned the same spectral parameter. The existing
blockwise reversing involutions still satisfy `RX+XR=0`; parameter equality
does not change that identity. Exact local row reduction checks `40` new
signed and graded primitive controls:

- real and imaginary `[d,2]` for `d=2,...,5`; and
- loxodromic `[d,1]` for `d=1,2`.

Every control has centralizer excess four split as two fixed and two moving
dimensions. The double-collision mechanisms compose two independently
certified K91 excess-two blocks. The zero-primary construction enumerates all
odd-chain grading colors and the paired-even-chain reversal, retaining the
`384` nonoptimal allocations as adverse controls rather than suppressing
them.

Every one of the `673` assembled `14x14` representatives is checked exactly
for

```text
signature(Q)=(7,7),
R^2=1,
R^T Q R=Q,
RX+XR=0,
X^T Q+QX=0,
signature(Q|R=+1)=(3,4) or (4,3).
```

Coprime primary decomposition makes the centralizer a direct sum across
distinct primary parameters. The local certificates give total centralizer
dimension `11`, split as `2` fixed plus `9` moving dimensions. Since
`dim h=42` and `dim p=49`, the ambient/fixed/moving adjoint ranks are
`80/40/40`, and the cotangent moment differential has rank `49+40=89`.
Finite-field row reduction supplies exact lower bounds; the matching
characteristic-zero centralizer formulas supply the upper bounds.

## Surviving gate

Centralizer dimensions `13,15,...` arise from the next primitive partition
excesses and larger additive combinations. K89--K92 support the sharp law on
the complete pure nilpotent cone and the first two mixed singular layers:

```text
dim(h intersection g_X) = (dim g_X - 7)/2,
```

but two layers do not prove it uniformly. The next route should classify
centralizer dimension `13` and simultaneously test whether a structural
centralizer-parity theorem can replace layer-by-layer enumeration. A single
counterexample to balanced membership still kills this horn's zero-
neighborhood claim.

## Claim ceiling

- All `673` centralizer-eleven mixed structural configurations meet `Ad(G)p`
  and saturate map rank `89`.
- Singular mixed strata with centralizer dimension at least `13`, a target
  neighborhood of zero, surjectivity and RSAP remain open.
- `H_bal` remains an admissible construction not selected by the source
  action. No physical BFV, positivity, quotient, datum, particle-spectrum or
  source-action conclusion follows.
- The ambient `A3` successor remains `TYPE_MISSING`; `[98,182]` is unchanged.

Reproduce with:

```bash
python3 tests/channel-swings/selected_k92_rsap_balanced_centralizer11_mixed_census_probe.py
```

The probe uses exact integer matrices, exhaustive structural enumeration and
finite-field rank forcing with matching characteristic-zero centralizer bounds.
