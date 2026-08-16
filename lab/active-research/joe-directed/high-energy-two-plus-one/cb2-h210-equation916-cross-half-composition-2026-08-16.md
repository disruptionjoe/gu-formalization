---
artifact_type: exploration
status: exploration
doc_type: conditional_build_result
created: 2026-08-16
work_item: CB-2
channel: high_energy_two_plus_one_prediction
target_claim: SC-GEN-53
title: "CB-2: the H210 bilinear is cross-effective-half, but its unbarred operator arrows occupy the off-diagonal d0+varpi cells inside each effective half"
grade: "EXACT equation-9.16 cell ledger, source-effective-half bookkeeping, complex D5 duality, and finite conditional rank arithmetic. CONDITIONAL on H210 and a nonzero family covector; CB-1 now supplies the exact injective, ambient-half-flipping rank-16 internal RS map used in the counts. The zero-order varpi summands are placed without relabeling the released source. The full first-order d0+varpi cells retain the known Layer-0 derivative-half collision. No source action, background selection, reality condition, observation quotient, mass, family label, scale, or physical chirality is derived."
disposition: H210_ZERO_ORDER_SUMMAND_HAS_TWO_SOURCE_FAITHFUL_OFFDIAGONAL_CELL_HORNS_AND_TWO_DISPLAYED_REVERSE_PARTNERS__CB1_ODD_PARITY_AND_RANK16_PASS__PP_MM_PORTS_ARE_WRONG_PS_CHANNEL_CONTROLS__FULL_CELL_AND_OBSERVATION_SURVIVAL_TYPE_MISSING
canon_verdict_change: none
steering_effect: "Compose CB-1 only into the zero-order varpi_-+ / varpi_+- summands. Do not use the bare varpi_++ / varpi_-- ports for the 16 x 144 channel, and do not promote the conditional rank-one family kernel through observation before a typed pullback/quotient receipt exists."
canonical_effect: pending_integration
depends_on:
  - lab/methods/source-native-comparator-routing.md
  - lab/active-research/joe-directed/high-energy-two-plus-one/he4-path-reprioritization-2026-08-16.md
  - lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md
  - lab/active-research/joe-directed/carrier/crb-carrier-is-four-corners-not-one-weyl-2026-08-15.md
  - lab/active-research/joe-directed/high-energy-two-plus-one/he3-four-corner-partner-placement-and-family-rank-2026-08-16.md
  - lab/active-research/joe-directed/high-energy-two-plus-one/he4-two-ps-channels-have-distinct-upstairs-owners-2026-08-16.md
  - explorations/conditional-build/selected-k77-four-field-zero-order-port-2026-08-10.md
  - explorations/observation-to-family-b5-campaign-2026-07-20.md
scripts:
  - tests/channel-swings/joe_directed_cb2_h210_equation916_composition_probe.py
---

> [!IMPORTANT]
> **GU-COMPARATOR-ROUTING — scope before inference.** The `16`, `144bar`,
> `144`, and `210` labels below are a typed complex-D5/PS bridge into the
> source's four-field grammar. Ordinary family indices, net-chirality tests,
> scalar-Higgs VEVs, and conventional SO(10) mass models do not adjudicate
> Weinstein's imposter/emergent-chirality proposal without another typed
> bridge. Read `lab/methods/source-native-comparator-routing.md` before reuse.
>
> Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`.

# CB-2 — H210 in the released equation-9.16 grammar

## Outcome first

The load-bearing distinction is between an invariant bilinear and its
unbarred operator arrow. HE-3's Pati--Salam channel is

```text
16 x 144 -> 1_PS.
```

With a self-dual `210` coefficient, that bilinear is equivalently an operator
arrow

```text
16 -> 144* = 144bar.
```

So the bilinear partners lie across the two source-effective halves, while
the raw unbarred operator arrow stays **inside** one effective half. This
duality reverses the tempting cell answer.

Using the released row and column orders without changing a sign label,
the two forward H210 zero-order candidates are

| role | matrix cell | released cell | unbarred operator arrow |
|---|---:|---|---|
| source-effective half A | `(1,2)` | `d0 + varpi_-+` | `nu+ (3 x 16) -> zeta- (144bar)` |
| conjugate half B | `(0,3)` | `d0 + varpi_+-` | `nu- (3 x 16bar) -> zeta+ (144)` |

The displayed reverse-shaped partners are

| role | matrix cell | released cell | unbarred operator arrow |
|---|---:|---|---|
| reverse on B | `(3,0)` | `-d0* - bar(varpi_-+)*` | `zeta+ -> nu-` |
| reverse on A | `(2,1)` | `-d0* - bar(varpi_+-)*` | `zeta- -> nu+` |

Only the **zero-order `varpi` summand** is placed by this result. The complete
`d0+varpi` cells inherit the exact source half-label versus derivative-parity
collision recorded by the section-9 extraction. CB-2 neither relabels the
one-form fields nor claims to repair that collision.

The ordinary bare ports `(0,2)=varpi_++` and `(1,3)=varpi_--` are exact
negative controls for this mechanism. Their raw arrows cross the source
effective halves, but their bilinears have the wrong products
`16 x 144bar` and `16bar x 144`, whose Pati--Salam invariant counts are both
zero. The earlier rank-128 generic zero-form port therefore does not by itself
place H210.

## 1. Contract and source pins

This file declares horn `H210`: assume a compatible nonzero `210` Pati--Salam
channel and no `54`. It does not derive why that coefficient is present or
nonzero. Deriving or varying a source action, solving for a background or
vacuum, importing an external selector, and fitting a family vector are
off-limits.

The interpretation is controlled by `SC-GEN-57/51/53/59/02/04/56/50/52` and
`SC-CHI-50/54/51/53/03` as pinned in the mandatory HE-4 packet. In particular:

- the target is two true-family modules plus one representation-theoretic
  imposter that looks the same after restriction and reunifies differently;
- the parent theory remains non-chiral and both effective halves remain in the
  carrier; and
- no basis choice may turn the coupled family line into a named “third” family.

Equation 9.16 separately fixes four independent barred/unbarred fields and the
exact orders

```text
rows:    (bar-zeta-minus, bar-zeta-plus, bar-nu-minus, bar-nu-plus)
columns: (zeta-plus, zeta-minus, nu-plus, nu-minus).
```

The row reversal is source data. Turning a barred row into the density-dual
slot of an unbarred output uses the repository's inherited opposite-half
density-dual bridge. The source display is consistent with that bridge, but
does not itself supply it, a global Krein adjoint, or a field reality
condition. Every arrow below is conditional on this explicit bridge.

## 2. Why “cross-half bilinear” becomes a within-half arrow

The corrected `(7,7)` census is

```text
A = Omega0(S+) + Omega1(S-) = 3 x 16    + 144bar,
B = Omega0(S-) + Omega1(S+) = 3 x 16bar + 144.
```

For the A-family channel, the invariant's `144` factor is the barred-row
covector dual to the unbarred `144bar` output. Thus

```text
bilinear:       row 144 from B  x  column 16 from A,
operator arrow: column 16 in A  -> output 144bar in A.
```

The conjugate statement exchanges `A/B` and bars. This is why “cross-half” in
HE-3 describes the bilinear representation factors, not a raw arrow from one
unbarred effective package to the other. Confusing those two objects selects
the pp/mm cells and lands in the exact zero-channel products.

The barred fields remain independent. Saying that a row is the density-dual
slot associated to an output invokes the inherited opposite-half
density-dual bridge; it is not a quotation that equation 9.16 constructed
that bridge and does not impose `bar-zeta = zeta*` as a field reality
condition.

## 3. Complete source-faithful horn ledger

| horn | cells switched on | status | exact consequence |
|---|---|---|---|
| `H210-A-UPPER` | zero-order part of `(1,2)` | conditionally compatible | nonzero row on `F x 16 -> 144bar` |
| `H210-B-UPPER` | zero-order part of `(0,3)` | conjugate conditionally compatible | nonzero row on `Fbar x 16bar -> 144` |
| `H210-UPPER-PAIR` | both forward cells | declared conjugate completion | preserves both ambient halves; no reality identification inferred |
| `H210-FOUR-CELL` | forward pair plus `(3,0),(2,1)` | displayed reverse completion | ranks below require all four maps nonzero; source does not prove a common adjoint domain |
| `H210-PPMM` | `(0,2),(1,3)` | incompatible | wrong PS products have invariant count zero |
| `H210-SE` | lower-right quadrant | forbidden by displayed 2021 branch | all four cells are zero; a nonzero-SE rival is source-admitted but unspecified and is not this horn |

The off-diagonal cells also contain `d0`. H210 does not replace, cancel, or
determine that derivative. A statement about the full cell's K77 parity,
global adjoint, closed domain, or spectrum is `TYPE_MISSING`.

## 4. Exact conditional rank packet

Let `F` be the three-dimensional family multiplicity and `r:F->C` a declared
nonzero family covector. CB-1 supplies the exact half-flipping H210 RS map
`T:16->144bar` with `rank(T)=16`. The Kronecker map

```text
M = r tensor T : F tensor 16 -> 144bar
```

has

```text
rank(M) = 16,
dim ker(M) = 48 - 16 = 32 = 2 x 16.
```

This is the basis-free algebraic `2+1` shape: `ker(r)` is a two-dimensional
family subspace. It is not a mass kernel or an observed spectrum.

Exact disjoint-block rank addition gives:

| conditional assembly | domain counted | rank | kernel on counted domain |
|---|---:|---:|---:|
| one forward family arrow | `48` | `16` | `32` |
| two forward conjugate arrows | `96` family inputs | `32` | `64` |
| two forward arrows extended by zero on both `144` inputs | counted `384`-dimensional `16/144` D5 sector | `32` | `352` |
| four nonzero displayed forward/reverse arrows | counted `384`-dimensional `16/144` D5 sector | `64` | `320` |

The `384` here is the reduced internal D5 census
`(3x16+144bar)+(3x16bar+144)`, not the full GU field carrier. The final row
uses a declared four-cell completion: on each `48+144` pair,
the forward and reverse maps land in disjoint output summands, so ranks add.
The source's starred notation does not by itself prove that completion is a
formal adjoint on a common physical domain. Without CB-1 injectivity, replace
each `16` by `rank(T)`; a merely unspecified nonzero abstract map does not
warrant the numerical rank.

## 5. Low/high-energy and observation ceilings

The only source-shaped conditional comparison justified here is

```text
H210 coefficient off:
  no H210 family-to-imposter zero-order summand;

H210 coefficient on, before observation:
  one unlabelled family covector couples to the opposite-origin imposter
  through each conjugate effective package; ker(r) has dimension two.
```

This matches the representation-origin grammar of the `2+1` claim better than
an ordinary family index or scalar mass story. It does not establish the
source's claimed energy regime. The source supplies no scale, threshold, or
cell-specific nonzero background.

Literal observation is pullback/contraction, not a guarantee of injectivity.
The released observation work finds the `3E+ + 3E-` branching but no physical
quotient removing mirrors or the 1536-mode complement. Consequently

```text
rank after pullback <= rank before pullback,
```

and equality, nonzero survival, quotient rank, a luminous selector, and a
physical family spectrum are all `TYPE_MISSING`. CB-2 does not call a
pre-observation kernel a measured two-family sector.

## 6. Multi-lens assessment and falsifiers

1. **Equation-9.16 grammar:** exact row reversal selects off-diagonal cells.
2. **Barred/unbarred duality:** density-dual row typing is used; a field reality
   condition is not.
3. **Four-corner bookkeeping:** both A and B are retained; no half is deleted.
4. **Operator versus bilinear:** the cross-half object is the bilinear partner;
   the operator arrow stays within A or B.
5. **Source chirality:** ambient sign, form degree, effective package, and 4D
   chirality remain separate types.
6. **Family symmetry:** only `ker(r)` is invariantly named.
7. **Observation:** all displayed ranks are pre-pullback ceilings.
8. **Low/high limit:** zero/nonzero H210 is a declared conditional comparison,
   not a derived energy threshold.
9. **Novelty archaeology:** the sixteen-cell matrix and generic rank-128
   zero-form port were banked; new here is their exact composition with the
   HE-3/HE-4 cross-half owner result and the pp/mm negative control.
10. **Hostile falsifier:** CB-1 now passes the `-+`/`+-` zero-order parity and
    rank-16 Clebsch gate. H210 is killed downstream on this route if the
    inherited density-dual bridge fails, a required real-form horn rejects the
    block, or every allowed block is annihilated by pullback/quotient.

## 7. Killed hypotheses and remaining types

Killed here:

- “cross-half bilinear means a raw unbarred cross-half arrow”;
- “the H210 channel belongs in the bare `varpi_++/varpi_--` ports”;
- “the existing generic rank-128 port proves H210 placement”; and
- “the released southeast-zero block can host this family/imposter arrow.”

Still `TYPE_MISSING`:

- fixed-trace-`Hq` simultaneous PS-equivariant unitary realization (an
  adverse construction horn, not a source-level kill);
- source ownership of the inherited opposite-half density-dual bridge;
- a source-selected nonzero H210 coefficient and family covector;
- a source-supplied reality/adjoint condition joining forward and reverse
  cells;
- reconciliation of the full derivative cells with source ambient-half
  labels;
- observation/quotient/domain survival; and
- family identity, mass, scale, threshold, observable, or prediction.

## 8. Reproduction and next conditional gate

From the repository root:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 tests/channel-swings/joe_directed_cb2_h210_equation916_composition_probe.py
PYTHONDONTWRITEBYTECODE=1 python3 tests/channel-swings/joe_directed_cb2_h210_equation916_composition_probe.py --selftest
```

The probe locks the sixteen-cell ledger, row reversal, two forward and two
reverse candidates, pp/mm adverse controls, and exact rank-nullity packet.

CB-1 has now passed the strict parity/rank composition gate: its exact K77
intertwiner is odd and has the ambient-half flip required by
`varpi_-+ / varpi_+-`. The next gate is therefore to carry only these
zero-order summands through a typed observation pullback while retaining the
fixed-trace-`Hq` branch as an explicit adverse subhorn. Do not repair the full
`d0+varpi` collision by relabeling the source or inventing an action.

## Verdict

`CB-2 = CONDITIONAL CELL PLACEMENT PASS / FULL-CELL AND OBSERVATION TYPE_MISSING.`

The strongest warranted sentence is:

> Under H210, the `16 x 144` invariant is cross-effective-half as a bilinear
> but acts as `16 -> 144bar` inside one unbarred effective package. The released
> equation-9.16 grammar places its zero-order summands in the off-diagonal
> `d0+varpi_-+` and `d0+varpi_+-` cells, with two displayed reverse partners.
> An injective rank-16 intertwiner and one nonzero family row leave an exact
> two-dimensional family kernel before observation; the full derivative cell,
> adjoint completion, and physical survival remain unconstructed.
