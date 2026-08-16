---
artifact_type: exploration
status: exploration
doc_type: conditional_build_exact_finite_naturality_result
created: 2026-08-16
work_item: CB-4A
channel: high_energy_two_plus_one_prediction
target_claim: SC-GEN-53
title: "CB-4A: the finite co-moving H210 contraction square commutes, so rank descends on the graph bundle while components remain gauge dependent"
grade: "EXACT scoped two-field K77/Clifford certificate. CONDITIONAL on H210; source-shaped imposter-to-partner wording separately requires H210-ALIGN. The result is formal associated-bundle covariance, not a selected observation section, quotient, mass, scale, threshold, or observable."
disposition: H210_FINITE_NATURALITY_SQUARE_PASSES__RANK_AND_KERNEL_DIMENSION_DESCEND__COMPONENTS_LOCAL_FRAME_STABILIZER_AND_SPIN_SIGN_DEPENDENT__PHYSICAL_OBSERVATION_NOT_PROMOTED
canon_verdict_change: none
steering_effect: "Do not search for a preferred finite O(7,7) or Spin(7,7) lift. Carry the H210 contraction as an associated-bundle morphism and use rank/kernel dimension as the intrinsic finite datum. Keep H210-ALIGN, physical reduction, and all action-owned dependencies separate."
depends_on:
  - lab/active-research/joe-directed/high-energy-two-plus-one/he4-path-reprioritization-2026-08-16.md
  - lab/active-research/joe-directed/high-energy-two-plus-one/cb1-h210-k77-rs-intertwiner-2026-08-16.md
  - lab/active-research/joe-directed/high-energy-two-plus-one/cb3-h210-literal-pullback-rank-2026-08-16.md
  - lab/active-research/joe-directed/high-energy-two-plus-one/cb3-wave-h210-observation-reprioritization-2026-08-16.md
  - lab/process/hostile-reviews/2026-08-16-joe-directed-cb3-h210-observation-review.md
  - explorations/conditional-build/selected-k77-canonical-section-jet-cartan-spin-prolongation-2026-08-12.md
  - explorations/conditional-build/selected-k77-finite-section-projector-atlas-descent-2026-08-12.md
scripts:
  - tests/channel-swings/joe_directed_cb4_h210_comoving_naturality_probe.py
---

> [!IMPORTANT]
> **GU-COMPARATOR-ROUTING — source-native conditional build.** This result
> tests the downstream geometry of Weinstein's F/Q/Z, `2+1`, imposter,
> Pati--Salam recombination, and emergent-chirality proposal. Ordinary family
> indices, net-chirality arguments, scalar-Higgs VEVs, and conventional
> `SO(10)` mass mechanisms are controls only and do not adjudicate this path.
> Read `lab/methods/source-native-comparator-routing.md` before reuse.
>
> Horn `H210` is assumed. `H210-ALIGN` remains a separate provenance horn.
> Deriving or varying an action, selecting a background or section, fitting a
> family row, importing an external datum, constructing a physical quotient,
> or inferring a mass, scale, threshold, phenomenology, or observable is
> outside this result.
>
> Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`.

# CB-4A — finite co-moving H210 naturality square

## Verdict first

The finite square passes exactly. For every admitted graph chart and every
tested K77 transition, the literal contraction of the co-moving H210 tensor
obeys

```text
L_(J')^T T' = A^-T S(g)(L_J^T T),

J' = (c+dJ)(a+bJ)^-1,
A  = a+bJ,
T' = g^-T S(g)T.
```

Consequently, the pointwise **rank and kernel dimension** of the contraction
descend on the nondegenerate graph/projector bundle. The component tensor does not
descend as a preferred matrix: it is a section of an associated bundle and
changes under the horizontal coframe, the block stabilizer, and the sign of a
local Spin lift.

This closes CB-3's finite co-moving naturality falsifier in favor of `H210` at
formal tensor grade. It does not close `H210-ALIGN`, choose an observation
section, or turn raw pullback into a physical observation.

## Conditional-build preflight

Seven lenses controlled the construction.

| lens | load-bearing question | answer used here |
|---|---|---|
| tensor/functor naturality | how do the three legs move? | ambient covectors use `g^-T`, spinor values use `S(g)`, horizontal covectors use `A^-T` |
| exact finite K77/Clifford | is the lift really orthogonal and Clifford covariant? | test finite Cayley transformations and explicit 128-spinor rotors over two exact fields |
| graph atlas | what is the correct overlap law? | retain the fractional denominator `A^-1`; `c+dJ` alone is false |
| principal bundle | what is canonical? | the graph/projector is canonical; O/Spin representatives are local modulo the block stabilizer and Spin sign |
| family/chirality | what survives the move? | rank and basis-free family kernel; both conjugate ambient halves are retained |
| adverse controls | which shortcuts could fake the result? | freeze `T`, omit `A^-1`, use `g` on the covector leg, or freeze the Clifford frame |
| claim inflation | is covariance already observation? | no; it is only an associated-bundle morphism before physical reduction |

The source packet fixes the F-shaped `128` as the imposter referent and the
Z/internal-`144` as the distinct predicted partner. `H210` supplies the
conditional family-to-partner port; identifying its quotient family line with
F provenance still requires `H210-ALIGN`.

## The exact square

Write the finite K77 transformation in blocks relative to `H+V`:

```text
g = ((a,b),(c,d)),
L_J = (I,J)^T : H -> H+V.
```

On the overlap where `A=a+bJ` is invertible,

```text
g L_J = L_(J') A,
J' = (c+dJ)A^-1.
```

An ambient covector-spinor transforms as

```text
T' = (g^-T tensor S(g))T.
```

Therefore

```text
L_(J')^T T'
 = L_(J')^T g^-T S(g)T
 = A^-T L_J^T S(g)T
 = A^-T S(g)(L_J^T T).
```

The first equality types the ambient covector and spinor legs separately. The
second is the transpose of `L_(J')=gL_JA^-1`. The last uses that graph
contraction acts only on the covector leg.

The displayed formula treats `T` as a covector-spinor, equivalently column by
column in the CB-1 operator. If the domain spinor frame is co-moved as well,
the full intertwiner formula has the same `S_in(g)^-1` factor on the right of
both sides. That extra invertible factor does not alter the square, rank, or
kernel dimension.

## Exact H210 composition

The probe reuses the current K77 split

```text
H signature = (1,3),
V signature = (6,4)
```

and the scaled CB-1 pure-normal tensor

```text
T_mu = 0,
T_a  = -2 Gamma_a phi4  on A6,
T_a  = +3 Gamma_a phi4  on B4.
```

The common factor of five relative to `-2/5,+3/5` changes no rank. Three
mixed Cayley transitions, each mixing four disjoint horizontal/vertical
planes, are tested over `GF(1009)` and `GF(1013)`. Their explicit finite Spin
rotors satisfy

```text
S(g) Gamma_i S(g)^-1 = sum_j g_(ji) Gamma_j
```

on all fourteen Clifford generators.

Each transition is composed with three graph strata:

| graph input | rank on each real ambient K77 Weyl half | internal-complex rank | finite result |
|---|---:|---:|---|
| flat `J=0` | `0` | `0` | remains zero after a co-moving mixed transition |
| weighted totally isotropic two-plane | `48` | `12` | rank survives exactly |
| banked receiver jet | `64` | `16` | full rank survives exactly |

The flat case is decisive against a misleading coordinate reading. A frozen
pure-normal tensor appears to acquire a nonzero contraction when the graph is
moved. Once the tensor and Clifford frame move with the graph, its zero rank
remains zero. Conversely, the banked receiver's full rank is not destroyed by
changing graph chart.

For the banked receiver and a declared nonzero family covector `r in M_3*`,
the internal rank remains `16` and the basis-free family-input kernel remains

```text
ker(r) tensor 16,    dim_C = 32.
```

The same result holds on the conjugate ambient half. Neither half is deleted
or promoted to the physical luminous sector.

## Atlas, stabilizer, and Spin-sign descent

The graph/projector prior art already established

```text
P_(J') = g P_J g^-1.
```

CB-4A adds the associated covector-spinor morphism over that base. A
nontrivial block-stabilizer element `k=diag(-I_H,-I_V)` gives two local lifts `g`
and `gk` with

```text
g P_0 g^-1 = (gk) P_0 (gk)^-1.
```

Their Spin lifts differ by the volume element, and either Spin lift may also
be multiplied by the double-cover sign. These changes alter local component
representatives. They cannot alter rank because all relevant coframe and Spin
factors are invertible.

Thus the precise descent statement is:

| object | descent status |
|---|---|
| graph plane / projector `P_J` | canonical on the admitted finite graph bundle |
| contraction as associated-bundle morphism | gauge covariant and well-defined through transition functions |
| pointwise rank and kernel dimension | intrinsic, chart/stabilizer/Spin-sign independent; rank may still vary between geometric strata |
| component matrix `L_J^T T` | local-frame dependent; not a canonical scalar or matrix |
| normalized `O(7,7)` representative | local and block-stabilizer dependent |
| Spin representative | local, stabilizer dependent, and sign ambiguous |
| physical observation or quotient | not constructed |

No preferred finite O/Spin lift is missing from this result. Asking for one
would mistake gauge representative data for geometry. A genuinely global
associated bundle still requires the ordinary orientation/Spin structure and
its transition cocycle; this probe verifies the local algebra and the tested
overlaps, not a new global topology theorem.

## Adverse controls

All four wrong transports fail on every nonflat case in both exact fields:

1. hold `T` fixed while moving the graph;
2. replace `J'=(c+dJ)(a+bJ)^-1` by `c+dJ`;
3. transform the covector index by `g` rather than `g^-T`; and
4. move the one-form index while freezing the Clifford/Spin frame.

The controls show that commutation is not a dimension coincidence. Every
factor in the square is load bearing.

## What has and has not moved

The finite naturality objection from CB-3 is discharged: raw rank variation
under a frozen splitting is coordinate variation, while co-moving rank is an
intrinsic associated-bundle datum. This is a real strengthening of the H210
conditional chain.

Nothing in the calculation establishes:

- the source action or its variation;
- a selected vacuum, background, graph, section, or external datum;
- `H210-ALIGN` or a named third-family direction;
- a physical quotient removing mirrors or B5 extras;
- a mass, energy scale, threshold, chirality selector, or observable; or
- preservation of a free Z/internal-`144` index after literal contraction.

The codomain remains a four-dimensional covector-spinor associated bundle.
The exact result concerns the rank of that contraction, not survival of an
uncontracted `144` representation.

## Certificate

Run:

```text
sage -python \
  tests/channel-swings/joe_directed_cb4_h210_comoving_naturality_probe.py
```

All `39` checks pass. The certificate includes the columnwise covector-spinor
square and its full-intertwiner/right-domain transport, three mixed transitions times
three graph strata over each of two exact fields, all fourteen finite gamma
covariance identities per transition, both ambient Weyl halves, the block-
stabilizer lift ambiguity, the Spin sign, and all four firing wrong-transform
classes.

## Route consequence

`H210` should not be demoted for coordinate-dependent pullback rank: the
co-moving square proves that rank and kernel dimension descend. The efficient
next question is not construction of a preferred lift. Downstream work should
carry this as an associated-bundle morphism and confront whichever remaining
conditional gate the integrated hostile review ranks highest. `H210-ALIGN`
and physical reduction remain explicit separate dependencies rather than
tasks to derive an action, select a section, or fit a family datum.
