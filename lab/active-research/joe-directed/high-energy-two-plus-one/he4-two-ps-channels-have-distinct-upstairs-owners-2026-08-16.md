---
artifact_type: exploration
status: exploration
doc_type: source-native-bridge-gate
created: 2026-08-16
work_item: HE-4
channel: high_energy_two_plus_one_prediction
target_claim: SC-GEN-53
title: "HE-4: the two Pati-Salam channels in 16 x 144 have distinct D5 owners, 54 and 210; no single irreducible upstairs channel can align their family rows"
grade: "EXACT complex D5 and Pati-Salam representation arithmetic.  The five multiplicity-one D5 summands have PS-singlet counts 0,1,1,0,0 for 45,54,210,945,1050.  The 945/1050 zeros follow exactly by nonnegative saturation of HE-3's total-two count, not by a large-irrep branching.  BRIDGE_OR_SEMANTIC_BOUNDARY: source ownership, activation, the family covectors, physical operator, quotient, scale, threshold, and observable remain missing."
disposition: EXACT_OWNER_SPLIT__SINGLE_IRREDUCIBLE_ALIGNMENT_ROUTE_EXCLUDED__FAMILY_RANK_UNFORCED__SOURCE_BRIDGE_MISSING
canon_verdict_change: none
steering_effect: "Stop searching for one irreducible D5 summand that owns both channels.  Treat H210, H54, HBOTH, and HNONE as conditional inputs and test their downstream carrier/operator/observation composition; deriving a source action or importing an external selector is outside this path."
canonical_effect: pending_integration
depends_on:
  - lab/methods/source-native-comparator-routing.md
  - lab/active-research/joe-directed/high-energy-two-plus-one/he3-four-corner-partner-placement-and-family-rank-2026-08-16.md
  - tests/generation-sector/q5_spin10_vector_spinor_product.py
  - explorations/resolver-wave-c-rebased-q5-q6-mh7-2026-08-03.md
  - explorations/channel-swing-CH-SM-2026-07-19.md
  - explorations/p54-weld-typing-2026-07-21.md
scripts:
  - tests/channel-swings/joe_directed_he4_distinct_ps_channel_owners_probe.py
---

> [!IMPORTANT]
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

# HE-4 — the two PS channels have distinct upstairs owners

## Outcome first

HE-3 found exactly two Pati-Salam-invariant contractions in the cross-half
complex product `16 x 144`, but could not tell whether their two family rows
were aligned. The exact D5 decomposition banked by Q5 is

```text
16 x 144 = 45 + 54 + 210 + 945 + 1050,
```

with every summand occurring once. The new owner calculation is

| D5 summand | presentation used | `dim Inv_PS` |
|---|---|---:|
| `45` | `Lambda^2(10)` | 0 |
| `54` | `Sym^2_0(10)` | 1 |
| `210` | `Lambda^4(10)` | 1 |
| `945` | saturation remainder | 0 |
| `1050` | saturation remainder | 0 |

The two channels therefore live in **different** multiplicity-one D5
summands: one in the `54` and one in the `210`. No single irreducible D5
summand owns both, so the proposed HE-3 route in which one unique irreducible
upstairs channel fixes their relative Clebsches is excluded.

That does not force the two family rows to be independent. It also does not
force them to be proportional. Under the conditional-build contract, one may
assume that only one owner is active, neither is active, or both are active
with a declared relation after restriction. The exact result is an
owner split and a killed alignment route, not a family-rank result and not a
physical `2+1` prediction.

## 1. The cheap exact proof

Write the Pati-Salam vector restriction as

```text
10 |_PS = A + B = (6,1,1) + (1,2,2).
```

The three small tensor constructions can then be restricted without branching
either large irrep.

### 1.1 The adjoint `45` owns no singlet

Exterior algebra gives

```text
45 = Lambda^2(10)
   -> (15,1,1) + (6,2,2) + (1,3,1) + (1,1,3).
```

There is no `(1,1,1)`, so `dim Inv_PS(45)=0`.

### 1.2 The traceless symmetric `54` owns one singlet

The two summands `A` and `B` each have an invariant quadratic form. Thus
`Sym^2(10)` has two PS-singlet directions. Removing the single D5-invariant
overall trace leaves their relative-trace combination in the `54`:

```text
54 = Sym^2_0(10)
   -> (20',1,1) + (6,2,2) + (1,3,3) + (1,1,1).
```

Hence `dim Inv_PS(54)=1`.

This is only the conventional complex representation label. P-54-WELD already
proved that the source-native distortion is `10`-valued, not directly a `54`;
only an additional quadratic traceless composite could reach this channel.
Nothing here reverses that correction or introduces a conventional scalar VEV.

### 1.3 The four-form `210` owns the other singlet

For `210=Lambda^4(10)`, expand `Lambda^4(A+B)`. The unique singlet is
`Lambda^4(B)`, the orientation line of the four-dimensional `(1,2,2)` block:

```text
210 -> (15,1,1) + (6,2,2)
     + (15,3,1) + (15,1,3)
     + (10,2,2) + (10bar,2,2)
     + (1,1,1).
```

Thus `dim Inv_PS(210)=1`. Calling this a source-owned connection component
would require a separate typed bridge; the representation calculation itself
does not supply one.

### 1.4 Saturation excludes `945` and `1050`

HE-3 independently computes

```text
dim Inv_PS(16 x 144) = 2.
```

Invariant dimension is additive on direct sums and is a nonnegative integer.
The `54` and `210` already contribute `1+1=2`, while the `45` contributes zero.
Therefore

```text
dim Inv_PS(945) + dim Inv_PS(1050) = 0,
```

which forces both terms to vanish individually. The probe also subtracts the
small exact characters from the `2304`-dimensional product, checks that the
remainder has dimension `1995=945+1050`, and directly obtains zero PS
invariants on that remainder. Full large-irrep branching would add cost but no
information.

The conjugate cross-half product has the same total-two result and the same
self-dual `54`/`210` owners. The same-effective-half product still has zero PS
channels; HE-4 does not move the HE-3 placement boundary.

## 2. What multiplicity one does and does not fix

Let `F` be the three-dimensional family-copy space supplied by the corrected
source census. The owner result refines the HE-3 coupling space to

```text
Hom_PS(F x 16 x 144, 1)
    = F*_(54)  +  F*_(210).
```

Because the `54` and `210` each occur once in `16 x 144`, the D5-equivariant
projection into each owner is unique up to scale. But they are inequivalent D5
irreps, and `Hom_D5(54,210)=0`. Thus D5 symmetry alone supplies no linear
intertwiner or forced relation between their independent scales or their two
family covectors. An ambient or nonlinear relation is not excluded.

The precise possibilities remain:

| assumed conditional horn | possible family-map rank | warranted conclusion |
|---|---:|---|
| neither owner activated | 0 | no separation |
| one owner activated with a nonzero family covector | 1 | conditional two-dimensional kernel |
| both activated with proportional nonzero covectors | 1 | conditional two-dimensional kernel |
| both activated with independent covectors | 2 | only one-dimensional kernel |

Distinct owners therefore do **not** imply rank two. Conversely, their rows
could be proportional only through an additional source/action relation,
accident, or symmetry visible after restriction; D5 representation theory does
not force it. A single reducible source object or nonlinear composite could
also carry both owner components. HE-4 excludes only the **single irreducible
D5 owner** route, not every possible common source object.

Even a later rank-one result would establish only a structural coupling kernel.
It would not name a family, construct an effective-half selector, place a term
in the physical Hessian, prove a nonzero stationary background, or show that a
state becomes massive or observable.

## 3. Prior-art and novelty boundary

Already owned and cited here:

- Q5's five-summand D5 decomposition and multiplicity-one statement;
- HE-3's total-two PS count, cross-half placement, and generic family-rank gate;
- CH-SM's conventional identification of `54` and `210` PS-breaking directions;
- P-54-WELD's correction that no direct native-distortion-to-`54` map exists.

New in HE-4:

1. the exact intersection of the five D5 summands with the two HE-3 PS
   invariant lines;
2. the saturation proof that both large summands own zero singlets;
3. the conclusion that the two channels have distinct irreducible owners and
   that no single irreducible D5 projection can align their family rows.

This is mostly a high-value composition of prior exact results. It is not a new
derivation of an ordinary generation count, net chirality, or standard-Higgs
mass mechanism.

## 4. Source-native bridge ledger and next gate

| required object | status after HE-4 | consequence |
|---|---|---|
| exact D5 owner of first PS line | `54`, exact comparator fact | direct native owner not supplied |
| exact D5 owner of second PS line | `210`, exact comparator fact | source placement/selection still required |
| one irreducible owner of both lines | excluded | stop this HE-3 alignment route |
| source selection between owners | `TYPE_MISSING` | zero/one/two active channels remain possible |
| relation between family covectors | `TYPE_MISSING` | rank remains unforced |
| effective-half selector and operator placement | `TYPE_MISSING` | no physical mass inference |
| background, quotient, scale, threshold, observable | source-silent | no prediction packet |

The efficient next gate is not a full `945`/`1050` branching, another
family-index calculation, or a program to derive the missing source action.
This lane is a **conditional build**. Declare one of four inputs:

```text
H210:  a compatible nonzero 210 channel is present and 54 is absent;
H54:   a compatible nonzero quadratic 54 channel is present and 210 is absent;
HBOTH: both are present, with proportional and independent rows kept separate;
HNONE: neither is present.
```

Then test how that assumed horn composes with the current `(7,7)` carrier, the
equation-9.16 cross-half cell grammar, the observation/quotient maps, and the
algebraic family kernel. Missing action selection stays in the dependency
ledger as a fence; constructing it or importing an external selector is
off-limits in this path.

## 5. Reproduction

From the repository root:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 tests/channel-swings/joe_directed_he4_distinct_ps_channel_owners_probe.py
```

The executable reruns HE-1 and Q5 as exact dependencies, constructs the small
tensor characters, verifies their irreducibility and complete PS dimension
closures, performs the nonnegative saturation, checks the conjugate and
wrong-half controls, and preserves the missing family-row relation explicitly.

## Verdict

`HE-4 = EXACT_OWNER_SPLIT / BRIDGE_OR_SEMANTIC_BOUNDARY.`

The strongest warranted sentence is:

> The two Pati-Salam invariant lines in the cross-half `16 x 144` product are
> owned separately by the multiplicity-one D5 summands `54` and `210`; `45`,
> `945`, and `1050` own none. Hence no single irreducible D5 channel fixes the
> two family rows, while their rank remains conditional-horn and downstream-
> composition dependent.
