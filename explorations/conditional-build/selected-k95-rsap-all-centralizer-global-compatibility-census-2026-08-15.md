---
title: "Selected-K95 RSAP all-centralizer global compatibility census"
status: active_research
doc_type: exact_complete_signed_structural_census_and_connected_orbit_qualification
created: "2026-08-15"
registry: lab/process/selected-k95-rsap-all-centralizer-global-compatibility-census.json
probe: tests/channel-swings/selected_k95_rsap_all_centralizer_global_compatibility_census_probe.py
grade: "ALL SIGNED STRUCTURAL LAYERS COMPLETE AND POINTWISE SHARP; CONNECTED-ORBIT REFINEMENT OPEN"
canon_verdict_change: none
---

# Selected-K95 RSAP all-centralizer global compatibility census

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

## Result first

The K93 half-excess law is globally compatible on every signed structural
configuration in split `so(7,7)`. The exact full census contains:

| routed class | rows | result |
|---|---:|---|
| non-pure-zero nonsemisimple | `3,691` | every row balances |
| fully semisimple | `558` | every row balances; route to K88 |
| pure zero | `99` | K89 connected-orbit census |
| **all structural rows** | **`4,348`** | **zero balance failures** |

The `3,691` mixed/regular-nonsemisimple rows occupy exactly these centralizer
layers:

| `dim(g_X)` | rows | map rank `(189-dim(g_X))/2` |
|---:|---:|---:|
| `7` | `545` | `91` |
| `9` | `714` | `90` |
| `11` | `673` | `89` |
| `13` | `645` | `88` |
| `15` | `331` | `87` |
| `17` | `135` | `86` |
| `19` | `243` | `85` |
| `21` | `163` | `84` |
| `23` | `70` | `83` |
| `25` | `35` | `82` |
| `27` | `32` | `81` |
| `29` | `4` | `80` |
| `31` | `42` | `79` |
| `33` | `32` | `78` |
| `35` | `10` | `77` |
| `37` | `2` | `76` |
| `39` | `3` | `75` |
| `47` | `9` | `71` |
| `49` | `3` | `70` |
| **total** | **`3,691`** | |

The missing odd centralizer dimensions are unattainable for a non-pure-zero
nonsemisimple primary sum; they are not skipped layers.

## Exact exhaustion

The probe reconstructs the complete K93 catalog of `757` signed local primary
types: `459` zero, `44` real, `248` signed pure-imaginary and `6`
loxodromic. It retains every exact half-excess grading signature needed for
global assembly, then forms unordered multisets subject to total rank units
seven and form signature `(7,7)`. It scans every even centralizer excess from
`0` through `84`, not merely the previously observed layers.

For high-excess zero primaries, equal Jordan chains are reduced by permutation
class and sign-characteristic independence of the fixed-centralizer
dimension. This is not assumed from convenience: the reduced calculation
exactly reproduces every independently computed K94 low-excess option set
before it is used higher up. Only `459` exact zero permutation-class ranks are
then required. The nonzero catalog needs `207` higher signature-class checks,
and the final nonzero multiset program has `405` states.

The generic enumerator independently returns K90's `547` rows when its two
pure-zero regular rows are restored, plus K91's `714`, K92's `673`, and K94's
`645`. Those calibrations fix the structural equivalence and routing convention
before the new deeper-layer counts are read.

## Uniform rank law

For every mixed row with centralizer dimension `c`, one simultaneous balanced
orthogonal involution has

```text
dim(h intersection g_X) = (c-7)/2,
rank(target orbit)       = 91-c,
rank(dJ)                 = 91-(c-7)/2 = (189-c)/2.
```

Thus every structural row saturates its `98D` pointwise Poisson bound.

## What is now closed

- No higher signed structural layer remains to enumerate.
- There is no structural counterexample to balanced global assembly.
- K93's local law is globally compatible on every structural row, not only
  through centralizer `13`.
- Hand-building another excess mechanism census is no longer the right next
  move.

## The remaining orbit seam

The finite rows suppress continuous spectral parameters and classify signed
canonical structures, not automatically every connected `SO_0(7,7)` adjoint
orbit. K89 separately proved that all `99` pure-zero signed diagrams are stable
and therefore exactly the connected nilpotent orbit classes. K95 does not
silently extend that stability statement to nonnilpotent primary sums.

The next gate is therefore precise: classify when each nonnilpotent
`O(7,7)` canonical class splits under `SO_0(7,7)`, then prove that every split
component—not merely one structural representative—meets the balanced
complement. A missed connected component would still block the all-charge
claim.

## Claim ceiling

- Complete signed structural coverage is proved for the classical balanced
  moment-map horn.
- Connected nonnilpotent orbit coverage, a zero neighborhood, surjectivity,
  RSAP, source selection and global gluing remain open.
- No physical phase-space, quantum, BFV, positivity or particle-physics claim
  follows.
- Ordinary Higgs, family-index and chirality comparators are irrelevant to
  this classical moment-map computation.

Reproduce with:

```bash
python3 tests/channel-swings/selected_k95_rsap_all_centralizer_global_compatibility_census_probe.py
```
