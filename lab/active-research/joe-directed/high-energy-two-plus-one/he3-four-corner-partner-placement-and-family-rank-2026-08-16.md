---
artifact_type: exploration
status: exploration
doc_type: source-native-bridge-gate
created: 2026-08-16
work_item: HE-3
channel: high_energy_two_plus_one_prediction
target_claim: SC-GEN-53
title: "HE-3: the corrected source-effective carrier puts the 144 partner across the two effective halves at Pati-Salam; two exact PS channels exist, but a 2+1 effect requires their family vectors to align, and that intertwiner is TYPE_MISSING"
grade: "EXACT complex D5 branching arithmetic and exact rational family-rank controls.  The four invariant ladders are 0/2/11, 0/0/3, 0/0/3, and 0/2/11 for 16x144, 16x144bar, 16barx144, and 16barx144bar respectively.  The source-aligned (7,7) effective-half assignment is inherited from the corrected CR-B/escape-corners census, not rederived here.  BRIDGE_OR_SEMANTIC_BOUNDARY: no source-owned family-row intertwiner, effective-half selector, physical operator, background, quotient, scale, threshold, or observable is supplied."
disposition: PARTIAL_CONSTRUCTED__CROSS_HALF_PARTNER_PLACEMENT_EXACT__TWO_PS_CHANNELS_EXACT__FAMILY_VECTOR_ALIGNMENT_TYPE_MISSING__NO_2PLUS1_PHYSICAL_CLAIM
canon_verdict_change: none
steering_effect: "Advance only to the family-vector-alignment/mediator-owner gate; do not repeat a standard family-index or net-chirality calculation."
canonical_effect: pending_integration
depends_on:
  - lab/methods/source-native-comparator-routing.md
  - lab/active-research/joe-directed/high-energy-two-plus-one/he1-imposter-separation-invariant-2026-08-14.md
  - lab/active-research/joe-directed/high-energy-two-plus-one/he2-real-form-does-not-pair-144-with-144bar-2026-08-15.md
  - lab/active-research/joe-directed/carrier/crb-carrier-is-four-corners-not-one-weyl-2026-08-15.md
  - canon/escape-corners-campaign-RESULTS.md
  - tests/escape-corners/referee_legA2_verify.py
  - lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md
  - lab/sources/gu-2021-draft-s11-s12-extraction-2026-08-03.md
  - lab/sources/source-claim-register.yaml
scripts:
  - tests/channel-swings/joe_directed_he3_four_corner_partner_placement_probe.py
---

> [!IMPORTANT]
> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact uses
> conventional complex `Spin(10)` representation theory only as a comparator
> inside a source-native carrier question. Its result does not adjudicate
> Weinstein's mechanism without a typed carrier/map/action/quotient/observable
> bridge. Read `lab/methods/source-native-comparator-routing.md` and follow its
> source-native pointers. Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`.

# HE-3 — four-corner partner placement and the family-rank gate

> [!NOTE]
> **Later steering (HE-4, 2026-08-16).** Section 6's original proposal to
> derive a source-owned mediator has been superseded by
> `he4-path-reprioritization-2026-08-16.md`. This channel is a conditional
> build: declare `H210`, `H54`, `HBOTH`, or `HNONE`, then test downstream
> geometric composition. Deriving a source action or importing an external
> selector is off-limits here.

## Outcome first

The corrected carrier census changes what the earlier isolated `16 x 144`
calculation means.

On the repository's **source-aligned `(7,7)` carrier horn**, the source-stated
effective half

```text
Omega^0(S14+) + Omega^1(S14-)
```

contains three spin-1/2 family units in the same complex internal `16` and a
gamma-traceless dark slot in `144bar`. Its conjugate effective half contains
three `16bar` family units and a dark `144`. This is the corrected census owned
by `tests/escape-corners/referee_legA2_verify.py` and
`canon/escape-corners-campaign-RESULTS.md`; it is a premise here, not a new
derivation.

Re-running the exact HE-1 engine on all four pairings gives:

| placement | tensor product | `Spin(10)` | Pati-Salam | SM |
|---|---:|---:|---:|---:|
| cross-half | `16 x 144` | 0 | 2 | 11 |
| same effective half | `16 x 144bar` | 0 | 0 | 3 |
| conjugate same effective half | `16bar x 144` | 0 | 0 | 3 |
| conjugate cross-half | `16bar x 144bar` | 0 | 2 | 11 |

Thus the family-shaped part of the `144` is not a partner for the families in
its own source-effective half at Pati-Salam. It is a candidate partner for the
families in the **opposite** half. The conjugate statement holds in reverse.
This is the new bounded result.

It does **not** yet force a physical 2+1 spectrum. The two Pati-Salam singlets
are two distinct contraction channels, hence two a priori distinct rows in the
three-dimensional family space. A one-family deviation requires their rows to
be proportional, so that the combined family coupling has rank one. The exact
probe demonstrates all three admissible logical outcomes:

| source-owned two-row family matrix | rank | untouched family subspace | result |
|---|---:|---:|---|
| two proportional nonzero rows | 1 | 2 | conditional 2+1 pattern |
| two independent rows | 2 | 1 | not a 2+1 pattern |
| two zero rows | 0 | 3 | no separation |

The source does not supply those family rows or an upstairs intertwiner fixing
their relative Clebsches. Therefore the correct verdict is
`TYPE_MISSING(family-vector alignment)`, not “2+1 forced.”

## 1. What is exact, and what depends on the carrier horn

### 1.1 Horn-robust facts

The four ladders are facts about complex D5 modules and their restrictions to
the complexified Pati-Salam and Standard-Model subalgebras. The probe uses
doubled integer weights and rational charges; it contains no floating-point
step. Complex conjugation exchanges the first ladder with the fourth and the
second with the third. Each tensor product closes on dimension `2304`.

These complex branching statements survive the repository's real-form/carrier
horns. They do not by themselves choose a real bilinear, a physical half, or a
mass operator.

### 1.2 Source-aligned `(7,7)` assignment

The interpretation “same effective half” versus “cross-half” uses the
source-aligned `(7,7)` census:

```text
source-stated effective half:      3 x 16     + 144bar
conjugate effective half:          3 x 16bar  + 144
```

This is exactly where the HE-1 isolated pairing needed correction. In the
source-stated half, `16 x 144bar` has no Pati-Salam singlet. The Pati-Salam
channels counted by HE-1's `16 x 144` ladder live across the two halves.

### 1.3 CR-B caveat

CR-B established that the declared ambient fermion is a four-corner/full-Dirac
object, not one Weyl corner. It also kept separate the later source statement
that a low-`varpi` regime behaves as two effective opposite-half theories. The
source does not construct the projection or decoupling operator that makes
either effective half physical.

Accordingly, “cross-half” here is an exact placement in the corrected ambient
module bookkeeping. It is **not** proof that the channel appears in the
observed action, survives the quotient, is massive, or decouples. Conversely,
the same-half Pati-Salam zero is not a no-go for the full four-corner theory,
because the conjugate corner is present in the declared carrier.

## 2. Exact calculation

The executable imports HE-1's already positive-controlled Weyl/Racah engine and
forms all four products. For a product `A x B`, it computes

```text
(dim Inv_Spin(10)(A x B), dim Inv_PS(A x B), dim Inv_SM(A x B)).
```

The exact result is

```text
16     x 144       -> (0, 2, 11)
16     x 144bar    -> (0, 0,  3)
16bar  x 144       -> (0, 0,  3)
16bar  x 144bar    -> (0, 2, 11)
```

The branching-content control explains the Pati-Salam rung. The `144` contains
each of the two `16bar` Pati-Salam blocks once and contains neither `16` block.
The `144bar` contains each `16` block once and contains neither `16bar` block.
Hence only the cross-half orientations can contract at Pati-Salam.

The three same-half SM singlets are a lower-symmetry fact. They do not repair
the missing Pati-Salam partner and must not be promoted into a high-energy GU
mechanism without a source-owned breaking background and action placement.

## 3. Why two Pati-Salam channels do not yet mean one different family

Write the two Pati-Salam contractions as rows `r_L` and `r_R` acting on the
three source-census family copies. Their combined family map is

```text
M_F = [ r_L ]
      [ r_R ].
```

Representation multiplicity determines that there are two rows. It does not
determine their entries or make them proportional.

The basis-invariant discriminator is `rank(M_F)`:

```text
rank 0: all three family directions lie in ker(M_F)
rank 1: two directions lie in ker(M_F)       [conditional 2+1]
rank 2: only one direction lies in ker(M_F)  [not 2+1]
```

The executable uses exact rational planted controls and verifies that an
invertible family-basis change preserves the distinction. It also verifies
that the **same two-channel multiplicity** permits both rank one and rank two.
Therefore multiplicity alone cannot settle the claimed partition.

No family is labelled by this test. A rank-one result, if later derived, would
select an unlabelled one-dimensional image in family space. Nothing here names
that direction “third,” derives the number three from an index, or establishes
a generation-parity/chirality theorem.

## 4. Source-native bridge ledger

| required object | current status | consequence |
|---|---|---|
| corrected four-corner carrier | supplied by CR-B/corrected census | enough to place the complex modules |
| four complex branching ladders | exact here | cross-half Pati-Salam placement established |
| two PS contraction spaces | exact here | two possible family rows, not their alignment |
| source-owned family-row intertwiner | `TYPE_MISSING` | rank one is not derived |
| effective-half selector/decoupling map | `TYPE_MISSING` | “luminous half” is not yet a physical projection |
| operator/sign placement in source eq. 9.16 | `TYPE_MISSING` | no mass/Hessian conclusion |
| nonzero source-owned background | source-silent | no channel activation conclusion |
| physical quotient/domain and exotic decoupling | source-silent | no observed spectrum conclusion |
| numerical scale, threshold, observable | source-silent | no prediction or exclusion channel |

The `varpi`-sector must remain correctly typed: it is a connection/distortion
sector, represented source-side by an `ad(P)`-valued one-form and its induced
operator insertion. It is **not a scalar VEV**. A future background question
must ask for a nonzero stationary source-owned connection/distortion component,
its contraction, and its survival through observation—not silently substitute
a conventional Higgs scalar.

The fermionic-operator extraction adds a live warning: the source half signs,
form-degree duality, and displayed equation (9.16) are not yet simultaneously
reconciled in the repository. HE-3 therefore reports a missing operator type
rather than inventing a cross-half entry in the physical Hessian.

## 5. Prior-art boundary and novelty

Already owned and only composed here:

- HE-1's exact `16 x 144` ladder and Pati-Salam branching;
- HE-2's result that the relevant complex modules do not become self-dual merely
  by choosing the real form;
- CR-B's four-corner carrier correction and bare same-class protection;
- the corrected source-effective-half census `3 x 16 + 144bar` and its
  conjugate;
- the generic fact that cross-half couplings are constructible in comparator
  models while their source placement remains open.

New here:

1. the exact **four-ladder** table rather than the isolated HE-1 ladder;
2. its composition with the corrected source-effective-half census, locating
   the Pati-Salam `144` partner across the halves;
3. the family-rank discriminator proving that two Pati-Salam channels do not
   by themselves force a rank-one/2+1 effect.

This does not reopen the ordinary family-index, net-chirality, or standard-Higgs
routes. Those are comparators and are not the source-native question.

## 6. Strongest next bounded calculation

The next swing should ask whether a **single source-owned upstairs mediator**
fixes the relative Pati-Salam Clebsches and therefore forces the two family rows
to be proportional.

The exact D5 decomposition already banked for `16 x 144` is

```text
45 + 54 + 210 + 945 + 1050,
```

with multiplicity one for each complex summand. The promising finite gate is:

1. branch those five mediator summands to Pati-Salam and identify which owns
   the two singlets;
2. intersect that owner with the correctly typed source-native
   connection/distortion grades, keeping metric-distortion and Clifford-form
   owners separate;
3. compute the restriction of the surviving unique upstairs intertwiner to
   both Pati-Salam family blocks;
4. return `rank 1`, `rank 2`, `zero`, or `TYPE_MISSING` without fitting family
   coefficients.

The `210` is a concrete candidate because its four-form presentation has a
Pati-Salam singlet, while native connection-placement work also finds a
signature-dependent grade-six `210` route. That is a target for calculation,
not a conclusion: grade, real structure, source ownership, and observation
placement must be verified before calling it the mediator. In particular, no
line in HE-3 calls it a VEV or a mass.

## 7. Reproduction

From the repository root:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 tests/channel-swings/joe_directed_he3_four_corner_partner_placement_probe.py
```

The probe reruns HE-1's `62/62` dependency internally, checks all four
dimension-`2304` products, computes the four ladders, verifies the conjugation
and wrong-half controls, and runs exact rational rank/basis-change controls.

## Verdict

`HE-3 = PARTIAL_CONSTRUCTED / BRIDGE_OR_SEMANTIC_BOUNDARY.`

The strongest warranted sentence is:

> In the corrected source-aligned `(7,7)` four-corner bookkeeping, the complex
> `144` family-shaped Pati-Salam partner lies across the two source-effective
> halves, and exactly two cross-half Pati-Salam contraction channels exist.
> A one-family-versus-two effect follows only if their family-space rows have
> rank one. The source-owned intertwiner, selector, and physical operator that
> could establish that rank are not supplied.

No generation count, generation index, chirality/parity inference, mass,
scale, threshold, exotic-decoupling claim, or observable follows.
