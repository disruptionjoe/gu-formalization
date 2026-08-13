---
title: "K77 Wave 2: full-adjoint Shiab span, eddy Bianchi complex and two-connection target"
date: 2026-08-05
status: PARTIAL_WITH_FULL_ADJOINT_EXTENSION_AND_INDEPENDENT_PRE_SHIAB_TARGET
doc_type: construction_result
named_gate: K77_FULL_ADJOINT_SHIAB_CHANNEL_RELATION_EXTENSION_BIANCHI_COMPLEX_AND_INDEPENDENT_TWO_CONNECTION_TARGET
gate_before: K77_FULL_ADJOINT_SHIAB_CHANNEL_RELATION_EXTENSION_BIANCHI_COMPLEX_AND_INDEPENDENT_TWO_CONNECTION_TARGET
gate_after: K77_PRODUCT_SENSITIVE_MOVING_PHI_EPSILON_BIANCHI_CHAIN_MAP_AND_TYPED_TWO_CONNECTION_TO_EULER_COMPARISON_FUNCTOR
route_disposition: PASS_WITH_STRUCTURAL_EXTENSION_AND_TARGET_BUILD__SELECTION_RANK_ZERO_AT_PRE_SHIAB_LAYER
source_collision: SOURCE_CONFIRMS_DISPLAYED_SEPARABLE_SHIAB_AND_EDDY_COMPLETION__SOURCE_CORRECTS_TWO_CONNECTION_TARGET_TO_UNRELEASED_FERMION_CONTEXT__SOURCE_SILENT_ON_PRODUCT_SENSITIVE_CHAIN_MAP_AND_COMPARISON_FUNCTOR
fork_assumed: SIGNATURE-AMBIENT
fork_horn: K77
search_space_dim: "8 displayed product labels spanning exactly 5 full K77 operator directions"
free_object_delta: 0
residue_touched:
  - "K77-W2-BIANCHI-TWO-CONNECTION-TARGET:T4"
fork_stack_acknowledged: "The exact product-incidence theorem applies to the eight displayed K77 formula choices, not every possible Shiab built from other invariant Phi_i, contraction or volume channels. The Bianchi and two-connection results live on the pre-Shiab connection-path carrier; K95/right-H, arbitrary global Y14, observed physics and physical domains remain separate."
grade: "Exact structural full-adjoint span theorem from the displayed formula plus complete grade-one lower bound; exact free-DGA connection-path moment Bianchi syzygy; exact independent Sage reconstruction; source-bounded two-connection target correction. Product-sensitive moving-Phi/epsilon chain map, full comparison functor, preferred Shiab, analytic domain and physics remain open."
canon_verdict_change: none
---

# K77 Wave 2: full-adjoint Shiab/Bianchi/two-connection target

## Result first

The three relations found in the last swing are not a grade-one accident.
They hold on the **entire adjoint coefficient carrier** for the eight displayed
Shiab product choices.

The reason is structural. If `f` is the product used in the first term and
`i,o` are the inner and outer products in the nested term, the displayed
formula separates as

\[
S_{f,i,o}=A_f+B_{i,o}.
\]

There are two possible `A` terms and four possible `B` terms. The eight sums
have a universal incidence rank of five and exactly three rectangular
relations:

\[
\begin{aligned}
S_{CCC}-S_{CCA}-S_{ACC}+S_{ACA}&=0,\\
S_{CCC}-S_{CAC}-S_{ACC}+S_{AAC}&=0,\\
S_{CCC}-S_{CAA}-S_{ACC}+S_{AAA}&=0.
\end{aligned}
\]

This supplies a full-map upper bound of five. The preceding complete
`91 x 14` grade-one calculation already has rank five, so the full eight-map
span has rank **exactly five**. Because the grade-one restrictions are
pairwise nonproportional, all eight full maps remain pairwise
nonproportional. Five operator directions do not mean five selector equations.

The wave also builds the source-guided quadratic-eddy Bianchi object. For the
connection path `B_t=B+tT`, let

\[
\bar F=\int_0^1F_{B_t}\,dt
=F_B+\frac12D_BT+\frac13T\wedge T
\]

and

\[
M_1=\int_0^1tF_{B_t}\,dt
=\frac12F_B+\frac13D_BT+\frac14T\wedge T.
\]

Integrating `D_{B_t}F_{B_t}=0` gives the exact first-moment syzygy

\[
D_B\bar F+[T,M_1]=0.
\]

An independent two-connection reconstruction reaches the same object. The
shifted square supplies

\[
\Delta F=F_{B+T}-F_B=D_BT+T\wedge T,
\qquad T=A-B.
\]

Therefore

\[
\boxed{\bar F=F_B+\frac12\Delta F-\frac16T\wedge T.}
\]

This target is constructed before applying any Shiab, and Sage independently
verifies it in a free associative algebra. The mixed northeast square defect
`-T wedge F_B` remains nonzero; ordinary Bianchi cannot be misused to delete
it.

The decisive boundary is that these new constraints still have **product
selection rank zero**. They constrain the connection-path input before a
Shiab is chosen. The missing discriminator is now precise: construct the
product-sensitive moving chain-map defect

\[
\mathfrak B_c
=D_{\rm out}\circ S_c-S_c\circ D_{\rm in},
\]

including `Phi(epsilon)`, Hodge, density, both connections and the active
gauge/observer owners, then compare it to an independently typed codomain
target. Separately, a chain functor must connect the unreleased
two-connection fermion complex to the bosonic Euler complex before their full
squares can be compared.

## Plain English

We learned two useful things and refused one tempting overclaim.

First, the eight candidate contraction formulas really contain only five
independent operator directions. That is true on the whole Clifford algebra,
not just on the slice we tested last time. It makes every later comparison
substantially cheaper.

Second, Eric's quadratic “eddy” correction now has an exact geometric role.
It is the average curvature along the path between two connections, and it
satisfies an integrated Bianchi identity. The later two-connection square
independently reconstructs precisely that average from its curvature and
torsion blocks.

But neither result chooses the missing Shiab. Both live before the contraction
is applied. The next swing has to test how each candidate intertwines the
actual moving differentials. That is where the product order can matter.

## 0. Layer 0

| phrase | object built here | object kept distinct |
|---|---|---|
| full-adjoint relation | identity among the eight displayed operator formulas on every coefficient input | relation inside only one grade, or all possible Shiab constructions |
| differential Bianchi | `D_B barF+[T,M1]=0` in the connection-path DGA | algebraic first Bianchi or variational exactness |
| variational exactness | Euler derivative of one scalar action | the Bianchi syzygy or `Xi=D Upsilon` |
| two-connection target | `(F_B,Delta F,T)` reconstructing `barF` before Shiab | a published bosonic operator or full Euler-complex comparison |
| selection rank | equations on the five-dimensional Shiab span | map rank, path-coefficient uniqueness, or nonzero response |
| physics target | held out | ambient `Y14` path curvature |

P1/P2/P3 do not enter any object in this table.

## 1. Source collision

The source receipt is
[`gu-shiab-bianchi-two-connection-target-source-reinspection-2026-08-05.md`](../lab/sources/gu-shiab-bianchi-two-connection-target-source-reinspection-2026-08-05.md).

It produces three material dispositions:

- `SOURCE-CONFIRMS`: the displayed separable product formula, the missing
  historical Bianchi sheet and the `1/2,1/3` quadratic-eddy completion;
- `SOURCE-CORRECTS`: the unreleased two-connection square appears in the
  immediate fermion-roll context, not as a ready bosonic target; and
- `SOURCE-SILENT`: the moving product-sensitive chain-map law and the typed
  comparison functor.

The reconstruction is therefore graded as source-guided exact mathematics,
not attributed as Weinstein's unpublished selector.

## 2. Inline specialist preassessment

Ten lightweight lenses shaped the calculation:

1. Clifford representation theory asked for a structural grade-independent
   proof before any `2^14` enumeration;
2. invariant theory proposed an incidence upper bound plus a complete-block
   lower bound;
3. differential geometry derived path moments from `B+tT`;
4. the variational bicomplex kept Bianchi and action exactness separate;
5. homological algebra typed the shifted square before comparison;
6. Krein/operator theory retained density-dual/primal distinctions;
7. gauge/BV kept moving `epsilon`, both connections and Ward owners live;
8. exact-computation engineering used a free DGA and independent Sage route;
9. source archaeology corrected the target's fermionic context; and
10. proof-systems review assigned summary-overreach and stale-object charges.

This avoided the projected `91 x 16384 x 8` brute-force census. The structural
proof is both stronger and cheaper.

## 3. Exact full-adjoint span theorem

Write the displayed map as

\[
S_{f,i,o}(\Xi)
=A_f(\Xi)+B_{i,o}(\Xi),
\]

where `A_f` is the first `Phi_1 wedge *Xi` term and `B_i,o` is the nested
`Phi_1`, `Phi_2`, Hodge term. This equality is an identity of formulas for
every adjoint-valued two-form `Xi`; it does not depend on its Clifford grade.

The exact `8 x 6` incidence matrix has rank five and a three-dimensional left
kernel generated by the displayed relations. Hence the span of the eight full
maps has dimension at most five. The complete grade-one restriction from the
predecessor has rank five, so restriction cannot increase dimension and the
full-map dimension is exactly five.

One exact coefficient blade in each grade `0,...,14` was also evaluated as a
corroborating plant. Every relation passed, but those representatives are not
used as the proof.

Scope fence: this theorem covers the eight product substitutions in equation
9.3's displayed low-degree architecture. It does not enumerate other
source-natural Shiabs using different invariant `Phi_i`, contraction,
Clifford-volume or projection channels.

## 4. Eddy-completed Bianchi complex

The main probe works in the free differential graded algebra on degree-one
generators `B,T` and degree-two generators `dB,dT`. Thus a commuting or scalar
fixture cannot accidentally erase `T wedge T`.

It verifies exactly:

\[
F_B=dB+B^2,
\quad D_BT=dT+BT+TB,
\quad D_BF_B=0,
\]

the connection-path moments `barF,M1`, and

\[
D_B\bar F+[T,M_1]=0.
\]

Solving a general ansatz `F_B+aD_BT+bT^2` against the path integral uniquely
returns `a=1/2,b=1/3`. This is uniqueness with two constraints on two
coefficients—surplus zero—not a phenomenological prediction.

The identity is a pre-Shiab differential syzygy. It is not yet the actual
bundle-global moving-`Phi(epsilon)` complex and does not prove `Xi=D Upsilon`,
Noether closure, BV closure, conservation after observation, or an analytic
domain.

## 5. Independent two-connection reconstruction

The exact shifted-square predecessor gives the independent blocks

\[
(D^2)_{11}=\Delta F,
\qquad (D^2)_{21}=T,
\qquad (D^2)_{12}=-T\wedge F_B.
\]

Using the named background curvature `F_B`, the first two blocks reconstruct
the source path average:

\[
F_B+\frac12(D^2)_{11}-\frac16((D^2)_{21})^2=\bar F.
\]

This is independent of all eight product labels. It is stronger than a target
defined by squaring one candidate Shiab, and it corrects the earlier
mixed-Bianchi shortcut by retaining the live northeast defect.

The scope is equally important: the primary-source ordering types the
unreleased shifted operator as a fermion-complex completion or rival. The
formula above constructs a shared **connection-path curvature target**, not a
published identification of the full fermionic square with the bosonic Euler
complex.

## 6. Why selection rank remains zero

The relation theorem reduces the displayed family to a five-dimensional map
span. The averaged Bianchi and two-connection equations contain only
`B,T,F_B,Delta F` and path moments. They do not contain a coordinate on that
five-dimensional span. Their coefficient matrix on the Shiab basis is
therefore the exact `0 x 5` matrix:

\[
\operatorname{rank}_{\rm product\ selection}=0.
\]

This does **not** prove that every historical Bianchi criterion is
channel-blind. It proves that the now-constructed pre-Shiab criterion is. A
product-sensitive selector must act after the product order becomes visible,
through the moving chain-map defect `D_out S_c-S_c D_in` or another
independently sourced codomain relation.

## 7. Constraint and construction accounting

| item | result |
|---|---:|
| displayed product labels | 8 |
| full operator-span dimension | 5 |
| universal relations | 3 |
| path-average coefficients | 2 |
| path-integral constraints | 2 |
| transgression surplus | 0 |
| Bianchi/two-connection product-selection rank | 0 |
| new fields/projectors/data | 0 |
| P1/P2/P3 used | no |

No physical constraint surplus is claimed.

## 8. Seven axes plus Layer 0

| level | disposition |
|---|---|
| Layer 0 | full/restricted, five meanings of exactness, and fermion/boson target types separated |
| L1 | source confirms formula and eddy; corrects two-connection context; chain map silent |
| L2 | full displayed map span exactly five; independent Sage certificate |
| L3 | free-DGA path curvature moments and two-connection reconstruction exact |
| L4 | transgression coefficients exact; scalar-action variationality inherited and distinct |
| L5 | pre-Shiab averaged Bianchi built; moving product-sensitive chain map open |
| L6 | no closed Krein/Green/hyperbolic/BFV domain claimed |
| L7 | no particle, equation recovery, mass, anomaly, chirality, count, GR or dark-sector row moves |

## 9. Hostile post-review

The review is
[`2026-08-05-k77-wave2-full-adjoint-bianchi-target-review.md`](../lab/process/hostile-reviews/2026-08-05-k77-wave2-full-adjoint-bianchi-target-review.md).

Its material repairs are reflected above:

- “all Shiabs” was narrowed to the eight displayed equation-9.3 products;
- “Bianchi complex” was narrowed to the exact pre-Shiab path-moment syzygy;
- “independent two-connection target” was narrowed to the reconstructed
  connection-path curvature input, not a full cross-complex identification;
- selection rank zero was limited to the constructed pre-Shiab constraints;
  the missing historical product-sensitive criterion remains open.

## 10. Next gate

```text
K77_PRODUCT_SENSITIVE_MOVING_PHI_EPSILON_BIANCHI_CHAIN_MAP_AND_TYPED_TWO_CONNECTION_TO_EULER_COMPARISON_FUNCTOR
```

In order:

1. construct the incoming and outgoing covariant differentials for the actual
   `epsilon`-conjugated `Phi_1,Phi_2`, Hodge, density and adjoint bundles;
2. compute `D_out S_c-S_c D_in` on the five-dimensional full-map basis;
3. derive the codomain target from the full action/Ward architecture rather
   than fitting it from a candidate;
4. construct or refute a typed chain functor from the unreleased shifted
   two-connection fermion complex to the bosonic Euler complex; and
5. promote a product only if an independent target has projective match rank
   one under hostile review.

P1/P2/P3 remain unchanged and unused. Curt remains formally separate guidance
inside the Eric lane. `TG-1 AND TG-2 AND TG-3` remains unpromoted. Wave 3 and
all physics rows remain closed.

## Executable receipts

- Main exact probe:
  `UV_CACHE_DIR=/tmp/gu-uv-cache uv run --with sympy python tests/channel-swings/k77_wave2_full_adjoint_shiab_bianchi_two_connection_target_probe.py`
- Independent Sage:
  `sage tests/channel-swings/k77_wave2_bianchi_two_connection_target_independent.sage`

Main receipt:

```text
6 source + 25 type + 21 exact + 9 planted = 61 PASS
```
