---
title: "K77 Wave 2: action polarization is channel-blind and the observation Sobolev domain is common"
date: 2026-08-05
lane: 1
status: PARTIAL_WITH_EXACT_NONSELECTION_AND_RESCOPED_DOMAIN
doc_type: construction_result
named_gate: K77_ACTION_DERIVED_POLARIZED_EULER_SHIAB_PRODUCT_SELECTOR_AND_GLOBAL_COUPLED_KREIN_GREEN_OBSERVATION_DOMAIN
gate_before: K77_ACTION_DERIVED_POLARIZED_EULER_SHIAB_PRODUCT_SELECTOR_AND_GLOBAL_COUPLED_KREIN_GREEN_OBSERVATION_DOMAIN
gate_after: K77_FULL_ADJOINT_SHIAB_CHANNEL_RELATION_EXTENSION_BIANCHI_COMPLEX_AND_INDEPENDENT_TWO_CONNECTION_TARGET
route_disposition: PASS_WITH_SELECTOR_NONSELECTION_AND_DOMAIN_RETYPE
source_collision: SOURCE_CONFIRMS_SHIAB_IN_ACTION_AND_MISSING_HISTORICAL_BIANCHI_SELECTOR__SOURCE_CORRECTS_OBSERVATION_AS_GREEN_BOUNDARY__SOURCE_SILENT_ON_GLOBAL_PHYSICAL_DOMAIN
fork_assumed: SIGNATURE-AMBIENT
fork_horn: K77
search_space_dim: "8 discrete source-permitted product labels; their complete grade-one restrictions span 5 linear directions"
free_object_delta: 0
residue_touched:
  - "K77-W2-ACTION-POLARIZATION-DOMAIN:T4"
fork_stack_acknowledged: "This continues the settled K77 carrier and the still-open source-action construction. The result is exact on the complete grade-one coefficient block and conditional at global Sobolev grade; it is not ported to K95 or promoted to a full-adjoint, arbitrary-Y14, or physical-domain theorem."
grade: "Exact complete 91x14 grade-one K77 channel-block span and projective separation; exact frozen action polarization; structural scalar-action Helmholtz theorem; conditional bounded-geometry H10-to-H9 associated-bundle observation scale. Full adjoint coefficient grades, actual arbitrary-Y14 global geometry, closed L2/Krein/hyperbolic/BFV domain, preferred Shiab, observation physics, and all particle rows remain open."
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# K77 Wave 2: action polarization and common observation domain

## Result first

The proposed action/Helmholtz selector has **zero selection rank**. Every one
of the eight displayed commutator/`i`-anticommutator Shiab choices defines a
legitimate scalar-action Euler pair, and all eight polarized Hessians are
exactly symmetric. Variationality therefore certifies the family; it does not
choose a member.

The exact K77 calculation nevertheless finds new structure. On the complete
`91 x 14` grade-one coefficient input block:

- all eight restricted maps are nonzero and pairwise nonproportional;
- their individual ranks remain
  `1190,1190,1190,1190,14,14,374,374`;
- the eight maps span only **five** linear directions; and
- three exact relations account for the rank drop.

Write `C` for commutator and `A` for `i` times anticommutator. On this block,

\[
\begin{aligned}
S_{CCC}-S_{CCA}-S_{ACC}+S_{ACA}&=0,\\
S_{CCC}-S_{CAC}-S_{ACC}+S_{AAC}&=0,\\
S_{CCC}-S_{CAA}-S_{ACC}+S_{AAA}&=0.
\end{aligned}
\]

These are **grade-one restriction identities**, not yet identities on the
full adjoint coefficient carrier. The eight discrete labels also remain eight
candidates: a five-dimensional linear span compresses later target matching
but does not crown one label.

The domain half also resolves cleanly, but at a lower grade than the gate name
suggested. Under explicit bounded-geometry, bounded-coefficient and uniformly
embedded-section hypotheses, all eight first-order Euler families share one
global associated-bundle Sobolev/observation scale

\[
H^{10}(Y,E)\longrightarrow H^9(Y,F).
\]

Field values and first jets restrict to `H5` and `H4` on the codimension-ten
section; Euler values restrict from `H9` to `H4`. This is a common variation
and observation domain, not a common closed `L2` realization or physical
evolution domain.

The important correction is geometric: `s(X4)` is codimension ten. It is not
a Green boundary of `Y14`, whose ordinary boundary would be thirteen
dimensional. A boundary condition on the observation section requires an
explicit defect/current/interface construction. Compact support or Dirichlet
data on an **actual** boundary kills formal flux for every channel and hence
also cannot select one.

## Plain English

We asked whether writing the action correctly or demanding a sensible domain
would tell us which version of Eric's missing Shiab contraction to use. The
answer is no, for a precise reason rather than a failed search.

Every candidate can sit inside a scalar action, so every candidate gets the
same basic variational consistency certificate. All candidates can also live
on the same high-regularity function space. Those conditions are common
infrastructure, not a discriminator.

What we did learn is that the eight choices are not eight unrelated objects.
On the full grade-one test block they obey three exact relations, leaving five
independent response directions. That makes the next target comparison
smaller and cheaper. The next selector must be an independent geometric
condition—most plausibly the missing Bianchi/exactness complex or Eric's
two-connection second-layer target—not another self-consistency property that
all scalar actions inherit.

## 0. Layer 0

| phrase | object established here | object kept distinct |
|---|---|---|
| action Euler | derivative of `A_c(T,P)=<T,S_c(P)>`, with both adjoint companion rows | printed unit-weight endpoint |
| Helmholtz | symmetry of the polarized Euler derivative | selection among discrete products |
| map rank | rank or span of the grade-one restriction | coefficient-selection rank or full-adjoint rank |
| global domain | conditional bounded-geometry Sobolev scale | actual arbitrary-`Y14` closed `L2` realization |
| observation trace | codimension-ten interior restriction | codimension-one Green boundary trace |
| Green closure | compact-support or actual-boundary zero flux | self-adjointness, maximal hyperbolicity, BFV, physical evolution |

The ambient Einstein trace and observed Standard Model targets remain held
out. P1/P2/P3 do not choose a channel.

## 1. Source collision

The receipt is
[`gu-action-polarization-domain-source-reinspection-2026-08-05.md`](../lab/sources/gu-action-polarization-domain-source-reinspection-2026-08-05.md).

The source confirms that the displayed Shiab occurs in the action but also
says the preferred historical highest-weight/Bianchi calculation is missing.
It provides no global physical boundary selection. The 2025 TOE discussion
instead distinguishes ordinary one-time initial-value theory from the
multiple-time ultrahyperbolic problem and calls the latter technical debt.

Therefore:

```text
SOURCE-CONFIRMS: displayed action placement and missing selector
SOURCE-CORRECTS: observation section is not already a Green boundary
SOURCE-SILENT: arbitrary-Y14 closed Krein/hyperbolic/BFV domain
```

## 2. Inline specialist preassessment

Ten lightweight lenses were applied before computation:

1. variational bicomplex predicted scalar-action Helmholtz symmetry might be
   channel-blind;
2. Clifford representation theory demanded exact map classes, not rank labels;
3. Krein operator theory separated boundary form from regularity domain;
4. hyperbolic PDE forbade a physical-domain promotion;
5. differential geometry required bounded-geometry and uniform trace
   hypotheses;
6. gauge/BV kept primitive Ward and tangent-differential ownership separate;
7. symplectic geometry kept interior observation and preboundary flux distinct;
8. exact computation required exhaustive enumeration and planted rank errors;
9. source archaeology routed failures back through the missing Bianchi sheet;
10. proof systems assigned both hostile charges: summary overreach and
    superseded-object defense.

The first prediction was confirmed. The hostile pass materially narrowed the
second result from “full K77 maps have rank five” to the correct statement:
the **complete grade-one restrictions** have rank five.

## 3. Exact channel-block classification

The probe evaluates every basis input

\[
e^{ij}\otimes\gamma^k,
\qquad 1\le i<j\le14,\quad 1\le k\le14,
\]

for all eight product triples using exact Gaussian-rational real
`Cl(7,7)` arithmetic. Each restricted operator is flattened with its input
column retained, then exact sparse elimination is applied to the eight whole
operator columns.

The result is

```text
formal product labels:                 8
pairwise projective restriction classes: 8
grade-one restricted operator span:   5
exact restricted relations:            3
```

An independent Sage calculation gives rank eight and determinant `4096` for
the free threefold binary product transform before Clifford/Hodge identities
are imposed. A planted duplicated row has rank seven. Thus the rank-five
collapse comes from the represented K77 grade-one/Hodge block, not from an
accidentally singular formal product encoding.

## 4. Actual action polarization

For a fixed product channel `c`, freeze the moving coefficients long enough to
write the bilinear action block

\[
A_c(T,P)=\langle T,S_cP\rangle.
\]

Its Euler pair is

\[
E_TA_c=S_cP,\qquad E_PA_c=S_c^!T,
\]

and its polarization is

\[
H_c((\dot T,\dot P),(\hat T,\hat P))
=\langle\dot T,S_c\hat P\rangle
+\langle\hat T,S_c\dot P\rangle.
\]

The probe checks direct exact differentiation and the swapped polarization for
all eight grade-one blocks. All pass and remain nonzero.

For the complete moving scalar action, additional derivatives of Hodge,
density, `Phi(epsilon)`, `B`, `T`, and the pseudo-musicals must be included.
They complicate the Euler expression but do not change the structural
Helmholtz fact: the second derivative of one scalar action is symmetric at the
proper graded/formal-adjoint level. This is why the separately printed
unit-weight endpoint cannot be substituted for the action Euler and why the
old fixed-endpoint obstruction does not return as a selector.

Since the channel label is a fixed discrete choice rather than a field, there
is no channel Euler row. The earned result is

\[
\operatorname{rank}_{\rm Helmholtz\ selection}=0.
\]

## 5. Common global Sobolev/observation scale

Condition on:

- a bounded-geometry realization of `Y14` and the K77 associated bundles;
- uniformly bounded coefficients and derivatives required by the first-order
  Euler family;
- a uniformly embedded observation section with bounded geometry; and
- the already constructed density/Krein primalizers and transition laws.

Then every channel defines a bounded first-order map from `H10` fields to
`H9` Euler rows. The trace losses are exact:

| object | ambient regularity | section regularity |
|---|---:|---:|
| field value | `H10(Y)` | `H5(X)` |
| field first jet | `H10(Y)` | `H4(X)` |
| Euler value | `H9(Y)` | `H4(X)` |

Channel-dependent principal coefficients can change the Green form while
preserving this common regularity scale. Compact support, or zero trace on an
actual codimension-one boundary, kills the corresponding formal flux for all
eight channels. It supplies no selection equation.

None of this constructs the missing global hypotheses for arbitrary
`Y=Met(X)`, proves an unbounded operator closed on `L2`, selects a
Krein-self-adjoint extension, propagates constraints, or chooses a physical
one-time evolution. The older domain multiplicity probe also warns that
Krein/deck symmetry can leave continuous self-adjoint-domain moduli, but that
finite theorem is not promoted to the actual K77 operator.

## 6. Hostile post-review

The durable review is
[`2026-08-05-k77-wave2-action-polarization-common-observation-domain-review.md`](../lab/process/hostile-reviews/2026-08-05-k77-wave2-action-polarization-common-observation-domain-review.md).

Its accepted repairs were:

- restrict rank five and all three relations to the complete grade-one block;
- distinguish canonical evaluation polarization from a full moving-field
  expansion of the action density;
- call `H10 -> H9` a conditional Sobolev/observation scale, not a closed `L2`
  or physical domain; and
- type `s(X4)` as an interior codimension-ten trace locus, not a Green
  boundary.

## 7. Constraint and construction accounting

| item | result |
|---|---|
| source-permitted discrete labels | 8 |
| grade-one linear response span | 5 |
| action/Helmholtz selection equations | 0 |
| common-domain selection equations | 0 |
| fitted parameters | 0 |
| new fields/projectors/data | 0 |
| P1/P2/P3 used | no |

No physical constraint surplus is claimed. The exact relations reduce the
cost of comparing a future independent target but do not discharge the
selector debt.

## 8. Seven axes plus Layer 0

| level | disposition |
|---|---|
| Layer 0 | endpoint/Euler, rank/selection, interior trace/boundary and Sobolev/physical domain separated |
| L1 | source confirms action placement and missing Bianchi selector; global physical domain silent |
| L2 | eight formal product labels; Sage free-product transform rank eight |
| L3 | exact complete grade-one K77 span five with three relations; full adjoint open |
| L4 | all eight scalar-action polarizations Helmholtz; selection rank zero |
| L5 | even Ward/BV owners inherited; no channel/datum inserted |
| L6 | conditional common `H10 -> H9` observation scale; closed physical domain open |
| L7 | no particle, equation-recovery, mass, anomaly, chirality, count, GR, dark-sector or cosmology row moves |

## 9. Next gate

```text
K77_FULL_ADJOINT_SHIAB_CHANNEL_RELATION_EXTENSION_BIANCHI_COMPLEX_AND_INDEPENDENT_TWO_CONNECTION_TARGET
```

In order:

1. extend or refute the three grade-one relations on every relevant adjoint
   coefficient grade;
2. construct the source-guided Bianchi/exactness complex for the surviving
   full-domain span, including the quadratic eddy term;
3. construct the independent two-connection second-layer target rather than a
   self-derived square; and
4. compare that target to the now compressed channel span before any observed
   physics fit.

If the independent target has projective match rank one, a product channel is
selected. If it has rank zero, the family survives. If it is inconsistent,
revise the Bianchi/path construction rather than killing the K77 carrier.

P1/P2/P3 remain unchanged and unused. Curt remains formally separate guidance
inside the Eric lane. `TG-1 AND TG-2 AND TG-3` remains unpromoted. Wave 3
remains closed.

## Executable receipts

- Main exact probe:
  `uv run --with sympy==1.14.0 python tests/channel-swings/k77_wave2_action_polarization_common_observation_domain_probe.py`
- Independent Sage route:
  `sage tests/channel-swings/k77_wave2_action_polarization_channel_rank_independent.sage`

Main receipt:

```text
7 source + 18 type + 30 exact + 8 planted = 63 PASS
```
