---
title: "Selected-K93 RSAP uniform local centralizer-parity qualification"
status: active_research
doc_type: exact_local_primary_exhaustion_and_global_theorem_qualification
created: "2026-08-15"
registry: lab/process/selected-k93-rsap-uniform-local-centralizer-parity-qualification.json
probe: tests/channel-swings/selected_k93_rsap_uniform_local_centralizer_parity_qualification_probe.py
grade: "LOCAL PARITY LAW EXHAUSTIVELY QUALIFIED; GLOBAL BALANCED DIRECT-SUM THEOREM OPEN"
canon_verdict_change: none
---

# Selected-K93 RSAP uniform local centralizer-parity qualification

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

The rank pattern observed in K89--K92 is not an accident of their first two
singular layers. Every local canonical primary type available inside real
dimension fourteen admits a reversing grading satisfying

```text
dim(fixed centralizer)
  = (dim(primary centralizer) - primary rank units)/2.
```

The exact finite census is:

| local primary species | signed types |
|---|---:|
| zero, rank units `1,...,6` | `459` |
| real | `44` |
| pure imaginary, with sign characteristics | `248` |
| loxodromic | `6` |
| **total** | **`757`** |

There are zero failures. Rank-units-seven pure zero primaries have no mixed
complement and were already covered globally by K89.

## What was proved

For each zero-primary orthogonal partition, the probe enumerates every real
signed row and searches its odd-chain grading colors. For each real and
loxodromic primary it exhausts ordinary partitions and chain colors. For each
pure-imaginary primary it additionally exhausts the sign characteristic on
every repeated chain size. Exact finite-field row reduction computes the
fixed centralizer for each candidate grading; characteristic-zero partition
formulas fix the total centralizer dimension.

Thus every individual primary factor has at least one grading whose fixed
centralizer is exactly half its excess above the regular rank contribution.
If compatible choices can be assembled globally, an element with total
centralizer dimension `c` would obey

```text
dim(h intersection g_X)=(c-7)/2,
rank(dJ)=91-(c-7)/2=(189-c)/2,
```

which is precisely the sharp `98D` pointwise Poisson bound.

## Why this is not yet the global theorem

Local optimality does not guarantee that the same choices sum to the required
global grading signature `(3,4)|(4,3)`. The local options carry both a
centralizer parity and a restricted form signature; optimizing the first can
remove choices needed for the second. K91 and K92 checked this compatibility
on centralizer dimensions `9` and `11`, but higher primary sums remain open.

Nor does a signed structural census automatically settle every possible
connected `SO_0(7,7)` orbit refinement. K89 closed that seam for pure
nilpotents; K93 does not silently generalize it.

## Next exact gate

Use only the locally optimal signature-option sets to enumerate the complete
centralizer-`13` mixed layer. A missing balanced sum is an exact counterexample
to the uniform global law and kills this horn's zero-neighborhood claim. If
all rows pass, repeat the finite dynamic program across every attainable total
centralizer dimension before stating surjectivity or RSAP.

## Claim ceiling

- The half-excess fixed-centralizer rule is exhaustive and exact locally for
  all `757` relevant signed primary types.
- No global balanced-direct-sum theorem, centralizer-`13` coverage, connected-
  orbit exhaustion, zero neighborhood, surjectivity or RSAP is claimed.
- No particle-physics, source-action, BFV, positivity, quotient or physical
  conclusion follows.

Reproduce with:

```bash
python3 tests/channel-swings/selected_k93_rsap_uniform_local_centralizer_parity_qualification_probe.py
```
