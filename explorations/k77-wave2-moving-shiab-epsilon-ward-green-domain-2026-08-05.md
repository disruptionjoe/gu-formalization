---
title: "K77 Wave 2: moving Shiab family, primitive epsilon Ward chain and compact-core Green domain"
date: 2026-08-05
status: PARTIAL_WITH_EXACT_MOVING_FAMILY_PRIMITIVE_CHAIN_AND_FORMAL_GREEN_PAIR
named_gate: K77_MOVING_SHIAB_MIXED_NORMAL_COEFFICIENT_DEPENDENT_EPSILON_WARD_AND_TRACE_CLOSED_GREEN_DOMAIN
gate_before: K77_MOVING_SHIAB_MIXED_NORMAL_COEFFICIENT_DEPENDENT_EPSILON_WARD_AND_TRACE_CLOSED_GREEN_DOMAIN
gate_after: K77_ACTION_DERIVED_POLARIZED_EULER_SHIAB_PRODUCT_SELECTOR_AND_GLOBAL_COUPLED_KREIN_GREEN_OBSERVATION_DOMAIN
route_disposition: PASS_WITH_PRODUCT_SELECTOR_AND_PHYSICAL_DOMAIN_BOUNDARY
source_collision: SOURCE_CONFIRMS_DISPLAYED_MOVING_PHI_FAMILY_TILTED_B_T_AND_FIXED_EPSILON_TRANSLATION__SOURCE_CORRECTS_OVERBUNDLED_EPSILON_CHAIN__SOURCE_SILENT_ON_PRODUCT_SELECTOR_AND_GLOBAL_PHYSICAL_DOMAIN
fork_assumed: SIGNATURE-AMBIENT
fork_horn: K77
search_space_dim: "8 discrete source-permitted low-grade product channels; 0 fitted parameters"
free_object_delta: 0
residue_touched:
  - "K77-W2-MOVING-SHIAB-EPSILON-GREEN: T4"
fork_stack_acknowledged: "The calculation uses the active real Cl(7,7) exterior/Hodge carrier and fixed 4+10 observation split. The older Cl(9,5) moving-Phi result is source archaeology only and is not identified with the K77 coefficient representation."
probe: tests/channel-swings/k77_wave2_moving_shiab_epsilon_ward_green_domain_probe.py
registry: lab/process/k77-wave2-moving-shiab-epsilon-ward-green-domain.json
grade: "Exact exhaustive eight-channel K77 mixed-normal calculation, exact moving-Phi derivative, primitive epsilon chain, off-shell even Ward owner check, and compact-core trace-compatible Green pair. The preferred product selector, global coupled Krein/physical domain, observation descent and physics remain open."
---

# K77 Wave 2 moving Shiab, epsilon Ward and Green domain

## Result in plain English

We built the part Weinstein actually specifies and learned exactly what it can
and cannot do.

His written Shiab is a moving family: `epsilon` conjugates two invariant forms,
and three coefficient-product slots can each use a commutator or `i` times an
anticommutator. That gives eight discrete low-grade channels. We evaluated all
eight exactly on the real `Cl(7,7)` model and the fixed `4+10` observation
split.

Every channel responds to all 85 two-form directions with at least one normal
leg. But response support is not coefficient rank. In channel order the full
grade-one rank vector is exactly `1190,1190,1190,1190,14,14,374,374`:

```text
comm-comm-comm  1190     comm-comm-symi  1190
comm-symi-comm  1190     comm-symi-symi  1190
symi-comm-comm    14     symi-comm-symi    14
symi-symi-comm   374     symi-symi-symi   374
```

Six channels have a rank-85 one-witness-per-exterior-direction slice; the two
`symi-comm-*` channels have all 85 directions live while that selected slice
has rank 10 and the complete 1,190-column grade-one bank has rank 14. This is
the control that prevents “all directions are expressible” from being read as
“all coefficients are independent.”

Moving `epsilon` gives the correct derivative of the Shiab, but it acts by
invertible conjugation. It preserves these ranks. So it supplies covariance
and the missing primitive variation; it does **not** select Eric's preferred
product channel and cannot create the 85-direction annihilator needed by a
zero-jet-only observation.

The primitive `epsilon` equation and off-shell even Ward identity now close at
finite exact grade. A trace-compatible compact-core Green pair also exists:
`D_B:H^10 cap H^1_0 -> H^9` has zero boundary flux for Dirichlet gauge data,
while the unconstrained alternative retains the expected preboundary flux.
This is a closed formal graph on a compact core, not a global physical domain.

## 1. Why this moves the gate

The predecessor left four related tasks: compute the actual 85-column family
block, compose the dependent `epsilon` chain, check the complete even Ward
owners, and close a trace-compatible Green domain. This wave completes all
four at the source-family/compact-core grade.

It also removes one false obligation. Hodge, density, metric and section
motion are separate primitive variations; they are not automatically part of
the fixed-metric `epsilon` chain. The source-defined chain moves `B`, `T`, and
the conjugated `Phi_i` inside the Shiab.

The remaining bottleneck is narrower: derive a product channel from the action
or another source-owned invariant condition, and extend the formal Green pair
to the global coupled Krein/observation domain. Wave 3 is not admitted yet.

## 2. Inline divergent specialist preassessment

| lens | binding instruction |
| --- | --- |
| variational bicomplex | differentiate primitive `epsilon`, not independent `B` and `T` alone |
| gauge geometry | derive the Maurer--Cartan chain and keep tilted-left versus adjoint-right actions distinct |
| representation theory | exhaust all eight products and report exterior support separately from coefficient rank |
| differential geometry | keep moving `Phi`, Hodge, density, metric and section owners separately typed |
| hyperbolic/operator theory | build a closed graph and Green form without calling it physical evolution |
| symplectic/BFV | retain nonzero boundary flux as preboundary data rather than killing it by assertion |
| exact computation | use rational Gaussian arithmetic and an independent dual-number derivative |
| source archaeology | collide every apparent failure with draft equations (8.1), (9.2)--(9.7) |
| statistics/ML engineering | do not learn a selector over eight enumerable candidates; enumerate exactly |
| science council/proof systems | charge both summary-over-artifact and defense-of-superseded-object failures |

Pre-registered kills were a fitted selector, support reported as rank, a claim
that conjugation changes rank, use of the epsilon equation to repair the
fixed-epsilon translation row, omission of a Ward owner, and promotion of a
compact Dirichlet graph to a physical domain. All are planted in the probe.

## 3. Layer 0 and source collision

The full receipt is
[`gu-moving-shiab-epsilon-green-source-reinspection-2026-08-05.md`](../lab/sources/gu-moving-shiab-epsilon-green-source-reinspection-2026-08-05.md).

| phrase | object built here | kept distinct |
| --- | --- | --- |
| moving Shiab | the eight source-permitted maps with `Phi_i(epsilon)=Ad_(epsilon^-1)Phi_i^0` | the missing preferred historical selector |
| live exterior direction | existence of at least one nonzero coefficient witness | rank of the complete coefficient bank |
| primitive epsilon equation | chain rule through `B`, `T` and moving `Phi_i` | independent fixed-`epsilon` translation equation |
| even Ward | off-shell infinitesimal homogeneous covariance of all owners | an odd super-IG BV differential |
| formal Green domain | compact-core closed graph with stated boundary condition | global coupled Krein self-adjoint or hyperbolic physical domain |
| epsilon | source gauge transformation/observer field | soldering, orientation datum or observation section |

The source confirms the family, movement and two-connection definitions. It
corrects the overbundled owner ledger. It is silent on product selection and
global analytic boundary data.

## 4. Exhaustive K77 product-family calculation

For the displayed two-term Shiab write schematically

\[
 \mathscr S_\epsilon(F)=
 \Phi_1(\epsilon)\diamond_1 *F
 -\frac12 *\bigl(\Phi_1(\epsilon)\diamond_3
   *(\Phi_2(\epsilon)\diamond_2 *F)\bigr), \tag{1}
\]

where each `diamond_i` is either the commutator or the symmetric product
`i(ab+ba)`. The search space is the full `2^3=8` family and has zero fitted
continuous parameters.

For the fixed tangent four-plane `H` and normal ten-plane `N`, the relevant
block is

\[
 (H^*\wedge N^*)\oplus\Lambda^2N^*,\qquad 40+45=85. \tag{2}
\]

The exact exterior/Hodge implementation tests every element of (2) against
all fourteen grade-one Clifford coefficients. Its complete result is:

| channel | live exterior directions | selected 85-column rank | full 1,190-column rank |
| --- | ---: | ---: | ---: |
| `comm,comm,comm` | 85 | 85 | 1190 |
| `comm,comm,symi` | 85 | 85 | 1190 |
| `comm,symi,comm` | 85 | 85 | 1190 |
| `comm,symi,symi` | 85 | 85 | 1190 |
| `symi,comm,comm` | 85 | 10 | 14 |
| `symi,comm,symi` | 85 | 10 | 14 |
| `symi,symi,comm` | 85 | 85 | 374 |
| `symi,symi,symi` | 85 | 85 | 374 |

Therefore no source-permitted channel satisfies the fixed-section
mixed-normal annihilator required for zero-only localization. This kills that
candidate mechanism, not the action family. The retained ambient normal first
jet from the preceding wave remains necessary.

## 5. Moving-Phi derivative and selection boundary

For `chi=epsilon^-1 delta epsilon`,

\[
 \delta\Phi_i=[\Phi_i,\chi]. \tag{3}
\]

Differentiating both occurrences in (1) gives the exact moving-Shiab response.
The probe independently verifies (3) and the resulting `delta S` by dual
numbers. Because simultaneous conjugation is invertible on domain and
codomain, it preserves support and rank. Thus the epsilon orbit provides the
correct equivariant family motion but no discriminator among the eight rows.

## 6. Primitive epsilon Euler row and Ward identity

With

\[
 B=\nabla_0+\epsilon^{-1}d_0\epsilon,
 \qquad T=\varpi-\epsilon^{-1}d_0\epsilon, \tag{4}
\]

and fixed `varpi`, the right-logarithmic variation gives

\[
 \delta B=D_B\eta,\qquad \delta T=-D_B\eta. \tag{5}
\]

If `K_S` denotes the action derivative with respect to the Shiab map, the
primitive row is

\[
 \boxed{E_\epsilon=D_B^!(E_B-E_T)
 +(D_\epsilon\mathscr S_\epsilon)^!K_{\mathscr S}.} \tag{6}
\]

An exact matrix fixture verifies the direct chain rule and keeps the
moving-Shiab contribution independently nonzero. The complete infinitesimal
homogeneous even Ward contraction vanishes off shell. Omitting either the
moving-Shiab owner or the inhomogeneous connection direction makes a planted
fixture fail. Equation (6) does not alter the fixed-`epsilon` translation
Euler row and is not an odd BV construction.

## 7. Green pair and analytic boundary

On a compact smooth core with the fixed observation section and the preceding
trace thresholds, choose

\[
 \eta\in H^{10}\cap H^1_0,qquad
 E_B-E_T\in H^9. \tag{7}
\]

Then `D_B eta` lies in `H9`, the graph is closed, and integration by parts has
zero boundary flux. Without the Dirichlet condition the same identity retains

\[
 \int_{\partial Y}\langle\eta,\iota_n(E_B-E_T)\rangle, \tag{8}
\]

which is the preboundary alternative. `H9` still traces values and first jets
to `H4(X)` and `H3(X)` respectively. Nothing here proves a global noncompact
`Y14` domain, coupled Krein self-adjointness, maximal dissipativity,
constraint propagation, hyperbolicity or a physical BFV phase space.

## 8. Seven-axis disposition

| layer | result |
| --- | --- |
| Layer 0 | all six object separations above pass; K77/K95 fork preserved |
| L1 | source equations and prior moving-Phi derivation located |
| L2 | all eight K77 product channels and 85 mixed-normal directions computed exactly |
| L3 | moving-Phi derivative and primitive chain independently verified |
| L4 | fixed-metric primitive epsilon Euler row exact; metric/section rows kept separate |
| L5 | complete homogeneous even Ward owner fixture exact; odd BV remains open |
| L6 | compact-core H10-to-H9 Green graph exact; global physical domain open |
| L7 | no preferred selector, datum use, physics row, claim or public-posture movement |

## 9. Accounting and next gate

| item | disposition |
| --- | --- |
| source candidates | all 8 enumerated |
| fitted parameters | 0 |
| new fields/projectors/data | 0 |
| `free_object_delta` | 0 |
| P1/P2/P3 | unchanged and unused |
| Curt | formally separated guidance inside the Eric lane |
| `TG-1 AND TG-2 AND TG-3` | not promoted |
| Wave 3 | closed |
| physics rows | none moved |

Next named gate:

`K77_ACTION_DERIVED_POLARIZED_EULER_SHIAB_PRODUCT_SELECTOR_AND_GLOBAL_COUPLED_KREIN_GREEN_OBSERVATION_DOMAIN`

Exit condition: derive or kill a product-channel discriminator from the
polarized action-derived Euler/Helmholtz structure, then construct one global
coupled Krein Green/observation domain on which that same choice descends.
Failure must name the action coefficient, representation block, boundary
condition or observation map. It may not return to “need a source action or
external datum,” fit a selector, use P1/P2/P3 as a projector, or infer physical
recovery from carrier support.
