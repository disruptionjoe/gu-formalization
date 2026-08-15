---
title: "Selected-K94 RSAP centralizer-13 global compatibility census"
status: active_research
doc_type: exact_signed_structural_census_and_balanced_direct_sum_gate
created: "2026-08-15"
registry: lab/process/selected-k94-rsap-centralizer13-global-compatibility-census.json
probe: tests/channel-swings/selected_k94_rsap_centralizer13_global_compatibility_census_probe.py
grade: "CENTRALIZER-13 STRUCTURAL LAYER COMPLETE AND POINTWISE SHARP; HIGHER CENTRALIZERS OPEN"
canon_verdict_change: none
---

# Selected-K94 RSAP centralizer-13 global compatibility census

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

The first global compatibility test of K93's local half-excess law passes.
There are exactly `645` signed structural configurations in the mixed
centralizer-`13` layer of split `so(7,7)`. Every configuration admits one
simultaneous anticommuting orthogonal involution whose two eigenspaces have
signatures `(3,4)` and `(4,3)` and whose fixed centralizer has dimension `3`.

Consequently every row has the sharp schedule

```text
dim(g_X)=13,
rank(target orbit)=91-13=78,
dim(h intersection g_X)=3,
rank(dJ)=91-3=88=(98+78)/2.
```

The `645` rows split into seven exhaustive excess-six mechanisms:

| mechanism | signed structural rows |
|---|---:|
| primitive nonzero excess six | `226` |
| nonzero excess four plus nonzero excess two | `23` |
| three nonzero excess-two primaries | `4` |
| zero-primary excess six | `138` |
| zero excess four plus nonzero excess two | `233` |
| zero excess two plus nonzero excess four | `11` |
| zero excess two plus two nonzero excess-two primaries | `10` |
| **total** | **`645`** |

Another `95` fully semisimple structural rows balance but are not relabeled as
new mixed cases; they route to K88's Cartan argument. Five pure-zero rows also
balance and route to K89's complete nilpotent-orbit census.

## Exact exhaustion method

K94 does not extrapolate from the prior two layers. It reconstructs every K93
local canonical type with excess `0`, `2`, `4` or `6`, retains the full set of
plus-eigenspace signatures among its exact half-excess gradings, and forms all
unordered multisets of distinct spectral primaries subject to:

```text
total rank units = 7,
total form signature = (7,7),
total centralizer excess = 6.
```

The finite dynamic program has `324` nonzero-primary states. Adding zero at
most once is forced because zero is a single spectral primary. The only
positive excess partitions are `6`, `4+2`, and `2+2+2`, which produce the
seven mechanisms above after distinguishing the zero owner.

As a calibration against independent predecessor enumerators, the same
generic program reproduces all `714` K91 excess-two mixed rows and all `673`
K92 excess-four mixed rows exactly. The local matrix certificates from K93
give `Q`-orthogonality, reversal and half-excess centralizer parity on every
factor. Direct sums with distinct primary parameters preserve those
identities and add their form and grading signatures.

## What this changes

K93 left open the possibility that locally optimal gradings could fail to
assemble into the balanced global signature. That possibility does not occur
at centralizer dimension `13`. The uniform law is now globally compatible
through centralizer excess six, not merely locally plausible.

This is evidence for using the multiset signature program rather than
returning to hand-built mechanism censuses at every deeper layer.

## What remains open

This is still one centralizer layer, not the whole Lie algebra. The same exact
program must run over every attainable higher centralizer dimension. The
signed structural inventory is also not automatically a census of connected
`SO_0(7,7)` adjoint orbits; K89 separately closed that refinement for the pure
nilpotent cone.

Therefore K94 does not establish a zero neighborhood, surjectivity or RSAP.
It does not select the balanced subgroup from Weinstein's source or construct
the missing ambient gluing.

## Next exact gate

Extend the K93 optimal-signature multiset program across all remaining mixed
centralizer dimensions `15` through `91`. Route semisimple and pure-zero rows
to K88 and K89, retain the connected-orbit seam explicitly, and stop on the
first balanced-signature failure. Only after all structural layers and their
required connected refinements close may this horn advance to a zero-
neighborhood or surjectivity claim.

## Claim ceiling

- Centralizer-`13` mixed coverage is complete at signed structural grade.
- All `645` new rows saturate the `98D` pointwise rank ceiling at map rank
  `88`.
- Higher centralizers, connected-orbit exhaustion, a zero neighborhood,
  surjectivity, RSAP, source selection and global gluing remain open.
- Ordinary Higgs, family-index and chirality comparators are irrelevant to
  this classical moment-map computation.

Reproduce with:

```bash
python3 tests/channel-swings/selected_k94_rsap_centralizer13_global_compatibility_census_probe.py
```
