---
artifact_type: exploration
label: W188
status: "exploration (W188 / boundary-selection non-vacuity audit; conditional register; one deterministic standard-library test; no canon, claim-status, or posture movement)"
created: 2026-07-14
title: "W188 verdict: laws-plus-boundary-selection is a coherent architecture, but today's alleged one boundary datum is not one identifiable bit. The conservative live dependency matrix has exact rank 8."
hypothesis: "Story 3 says universal laws define an admissible family while boundary/history data select the realized world. This is explanatory rather than epicyclic only if the selection data are declared separately from derived bulk invariants, frozen before comparison, reused across sectors, eliminate more freedom than they add, and emit a risky cross-sector prediction. Test that contract on the actual live GU candidates and determine whether the phrase 'one external boundary datum' denotes one identifiable coordinate or several."
grade: "EXACT for the finite dependency bookkeeping, rational matrix ranks, control ranks, group ranks, and non-vacuity score implemented in tests/W188_boundary_selection_nonvacuity.py. STRUCTURAL / RECONSTRUCTION for assigning the cited live GU objects to dependency columns and post-selection outcome contracts. CONDITIONAL for the laws-plus-selection interpretation itself. The audit is conservative: section and source/cure are each represented by only one coordinate although the full spaces may be infinite-dimensional. No physics result, source action, or relation among selectors is derived here."
depends_on:
  - GEOMETER-VS-PHYSICS-OBJECTS.md
  - explorations/W150-substrate-sweep-consensus-crypto-2026-07-14.md
  - explorations/W173-brst-cohomology-mirror-sector-2026-07-14.md
  - explorations/W177-build-connection-curvature-c2-2026-07-14.md
  - explorations/W180-build-matter-connection-bridge-c3-2026-07-14.md
  - explorations/W183-external-input-open-system-reframe-2026-07-14.md
  - explorations/W184-mirror-superselection-decay-2026-07-14.md
  - explorations/W186-source-content-reservoir-krein-type-2026-07-14.md
scripts:
  - tests/W188_boundary_selection_nonvacuity.py
---

# W188: make the laws-plus-boundary-selection story non-vacuous

## Executive result

The architecture is coherent:

> The bulk law defines the admissible worlds. A boundary/history selector chooses one realized world.
> Once chosen, that selector is frozen, and the same choice must produce consequences in several sectors.

But today's GU record does **not** yet justify the stronger sentence "one boundary datum selects the
world." The exact dependency audit gives a conservative rank of **8**, not 1. Three phrases that sound
singular each hide two independent coordinates:

1. "the reservoir datum" = its relative Krein type **and** the source-to-kinematic coupling ratio;
2. "the generation datum" = the source action's K-class/carrier **and** the count selector `1` versus `3`;
3. "the section/source datum" = the observer section `sigma` **and** the source/cure declaration.

The ghost-parity dynamics `[P_ghost,S]=0` and the free scale `mu_DW` add two more coordinates. Thus the
current claim is best read as **one boundary-selection interface carrying at least eight coordinates**, not
one independent bit. A future source action could collapse these to one latent selector, but it must derive
at least seven independent relations among them before comparison with outcomes. Merely giving the bundle
of unresolved choices one name would not do it.

This is a conditional exploration only. It changes no GU status, claim grade, canon, or posture.

## 1. The three-layer contract

Let a candidate theory be a triple

```
T = (D_bulk, B_select, P_post).
```

The layers have different epistemic jobs and may not trade places after looking at data.

### Layer 1: derived bulk invariants `D_bulk`

These are fixed by the chosen construction before any world is selected. In the live GU chain they include:

- the native noncompact real form `Sp(32,32;H)` and its indefinite/Krein structure;
- the `(9,5) = (3,1) + (6,4)` split and the distinction between the base `X4` metric and the
  gimmel/DeWitt metric on `Y14 = Met(X4)`;
- the free-BV result that the mirror is closed-not-exact in the built complex, construction-relative as in
  W173;
- the exact W177 wall that metric-compatible `so(9,5)` curvature is leakage-free and cannot close `C2`;
- the exact W180 minimal-coupling identity `J^a = delta S_D / delta A_a` under its declared induced-source
  construction;
- the `Z/3` torsion arena for the generation question and the impossibility of reaching it with a
  `Z`-valued index;
- the law/shadow distinction: the April 2021 GU law is linear shiab-Einstein, while `|II|^2` is an induced
  geometric self-energy. A scalar pole in the shadow is not automatically a degree of freedom of the law.

A datum is not allowed into this layer merely because it is geometrically natural or repeatedly useful.
It must be derived in the construction being used.

### Layer 2: declared boundary-selection data `B_select`

The conservative live vector is

```
B_select = (
  s_res,          # relative reservoir Krein type
  r_eta,          # source/kinematic coupling ratio relative to r*
  p_dyn,          # whether [P_ghost,S] = 0
  k_gen,          # source-action K-class / carrier A vs B
  n_gen,          # realized admissible count 1 vs 3
  mu_DW,          # overall DeWitt/fourth-order scale
  sigma,          # observer section X4 -> Y14
  c_source        # source/soldering/causal-cure declaration
).
```

This is a **lower bound** on the true selection dimension. `sigma` and `c_source` each stand for a space of
choices, not literally one real parameter. Collapsing them to one coordinate each makes the audit kinder to
the one-datum story.

The entries are not interchangeable:

- `s_res` is a discrete relative Krein type. W183 distinguishes like-signed from opposite-signed reservoirs.
- `r_eta` is a continuous dominance/magnitude variable. W186's favorable fixed point exists only above a
  threshold. A sign does not fix a magnitude.
- `p_dyn` is a dynamical conservation statement. W184 proves that a global Cartan grading alone does not
  imply `[P_ghost,S]=0`.
- `k_gen` chooses the K-class/carrier in which an index-changing selector can live. It does not select the
  observed member of `{1,3}`.
- `n_gen` is the remaining count choice. If set to `3` because the world has three generations, it is a fit,
  not a prediction.
- `mu_DW` is structurally free in a ratio-only DeWitt geometry. It cannot be silently identified with a
  cosmological scale.
- `sigma` determines the observer pullback/compression.
- `c_source` determines the non-metric source/cure/soldering content that the metric-compatible curvature
  cannot supply.

### Layer 3: post-selection predictions `P_post`

Only after the entire `B_select` vector is frozen may the theory be compared with the world. The live outcome
contracts represented in the test include:

- existence of a positive total C-metric;
- the reduced ghost pole sheet and the ghost-to-two-graviton channel;
- the law-to-shadow scalar sign;
- `C2` demotion or survival and the RS causal-cure branch;
- the index-changing carrier and realized generation count;
- the PPN Yukawa range and gravitational-wave dispersion threshold;
- observer pullback, overlap descent, and operator non-gluing;
- matter-to-connection current normalization;
- dark-energy source amplitude;
- reservoir flux type and section/source transduction.

Several are mathematical or model-level risks rather than empirical predictions. That distinction is kept:
the dependency audit says what would move together under a frozen selector, not that GU has already derived
the full functions or passed those tests.

## 2. Construction-fork discipline

Every load-bearing object in the matrix is construction-relative.

| object | construction used here | why it is used | what survives the other construction? |
|---|---|---|---|
| gauge group and sign | native `Sp(32,32;H)` / indefinite Krein form, not compact `Sp(64)` | W183/W186's reservoir sign and C-metric question exist only in the native indefinite construction | In a positive Hilbert/compact construction there is no same sign-flip problem; this audit's Krein columns disappear rather than being solved. |
| ghost treatment | native **KEEP-AND-GRADE**, with `[P,S]=0` and an interacting/total C-operator, not removal | This is the live GU claim tested by W173-W186 | A BRST quotient or positive-Hilbert removal is a different theory. W173's free-complex result leans against removal but does not prove the stabilized theory. |
| generation count | native `Z/3` torsion/K-class arena, not a `Z` Dirac index | `Hom(Z/3,Z)=0`; a `Z` index cannot select the three-primary datum | A `Z`-index no-go does not kill a torsion selector. Conversely, the existence of `Z/3` does not force the count. |
| metric and scale | base `X4` metric and gimmel/DeWitt metric are distinct; `mu_DW` belongs to the latter scale | Prevents importing a base-spacetime normalization into the metric-on-metrics | A single-metric treatment can produce a number only by changing the construction. It does not derive the native scale. |
| gravity law | actual GU law is linear/shiab-Einstein; `|II|^2` is an induced geometric self-energy | Prevents treating a shadow pole or self-energy as the fundamental law | A no-go for fundamental quadratic gravity applies to the induced-shadow branch only if that shadow is what physically propagates. |
| mirror decay vertex | the W184 physicist-side trilinear Fock vertex is used only for the decay/parity test | It directly checks whether a ghost-to-two-graviton vertex is parity odd | The result survives for any trilinear vertex changing ghost number by one. It does not prove the native source action contains that vertex. |
| source/soldering | native equivariant projector/current for the built identities; external symmetric non-metric cure for the live `C2` residue | W177 proves metric-compatible curvature cannot supply the needed leakage; W180 builds the current side | The physicist non-minimal vertex and native projector are not identical. A cure in one construction must be shown to induce the other before the coordinate can be collapsed. |
| observer section | native `sigma: X4 -> Y14`, separate from the source/cure | A pullback selecting an observer shadow is not the same mathematical object as a dynamical source term | A future functorial source action may relate them; no such relation is built today. |

The audit therefore does **not** claim a construction-independent no-go. Its conclusion is narrower and
harder to evade: in the actual set of constructions used by today's live results, the selectors have
different dependency signatures. Any proposed unification must build the maps that identify them.

## 3. Exact dependency and identifiability result

The test constructs a 16 by 8 binary matrix `M`. Row `i` is a post-selection outcome contract; column `j`
is one boundary coordinate; `M_ij = 1` when that outcome changes under that coordinate in the cited live
construction. Exact Gaussian elimination over the rationals gives

```
rank_Q(M) = 8.
```

All eight columns pivot. The grouped ranks are:

| phrase / candidate family | exact rank | meaning |
|---|---:|---|
| reservoir Krein type + eta/coupling ratio | 2 | sign and magnitude are not identified |
| ghost-parity dynamics | 1 | a grading is not the S-matrix conservation law |
| generation K-class + count selector | 2 | carrier admissibility does not select `3` |
| `mu_DW` scale | 1 | ratio-only geometry leaves one continuous scale |
| observer section + source/cure | 2 | pullback and dynamics are not the same object |
| **total** | **8** | one interface, at least eight current coordinates |

This is an identifiability result about the present formalization, not a metaphysical statement that nature
must contain eight arbitrary constants. A future source action could impose relations. But to reach one
latent coordinate from rank 8, it must derive **seven independent relations** among these columns. Those
relations must be obtained before using the observed generation count, DESI, PPN, GW, or pole outcome.

## 4. Strong non-epicycle rule

A boundary datum `b` is admissible only if all four conditions hold.

### N1. Freeze before comparison

The value and construction of `b` must be recorded before looking at the outcome used to test it. A lean,
candidate family, or consistency basin is not a freeze. Changing from like-signed to opposite-signed after
seeing the pole, choosing carrier B because it can host three, or setting `mu_DW` from the observed scale
fails N1.

### N2. Reuse across sectors

The identical datum, with the identical value and no translation knob, must enter at least two sectors. A
new copy per sector is several data with the same name. Current promising reuse paths include:

- `p_dyn`: loop/decay unitarity and the effective law-to-shadow sign;
- `k_gen`: the matter carrier and RS causal cure;
- `mu_DW`: PPN and GW/continuum thresholds;
- `sigma` / `c_source`: observer pullback, matter connection, and `C2` closure;
- reservoir sign/ratio: reduced pole, total metric, and source flux.

The count selector `n_gen` currently fails this test: it selects the observed matter multiplicity and has no
independent cross-sector consequence in the live chain.

### N3. Eliminate more freedom than it adds

For a package with `m` independently stated outcome contracts and boundary-Jacobian rank `r`, define

```
relations = m - r
strict_selection_surplus = relations - r = m - 2r.
```

The selector is compressive only when `strict_selection_surplus > 0`: the relations it forces among outputs
outnumber the independent choices it adds. This is deliberately stronger than ordinary parameter counting.

For today's conservative ledger, `m = 16` and `r = 8`, so

```
relations = 8
strict_selection_surplus = 0.
```

The package is at best break-even before grading how many rows are genuine predictions. A true one-latent
selector controlling the same 16 outputs has rank 1 and surplus 14, which the positive control reproduces.
Eight unrelated one-output knobs have negative surplus, which the epicycle control reproduces.

### N4. Emit a risky cross-sector prediction

At least one consequence must span sectors and be capable of failing with the selector held fixed. Merely
reproducing the datum used to select the world does not count. Candidate risks include:

- use one frozen `mu_DW` to predict both PPN range and GW dispersion;
- use one frozen source/cure to choose the RS carrier and then predict a matter or gravity coupling not used
  in that choice;
- use one frozen signed reservoir coupling to predict both the total C-metric regime and the reduced pole
  sheet;
- use one frozen observer section/source map to predict both overlap descent and the current normalization.

The generation count alone fails N4 today. "Choose the world with three generations; predict three
generations" is not risky.

## 5. Controls

The deterministic test uses matched controls.

- **Positive rank control:** the 8 by 8 identity has exact rank 8.
- **Positive coherent-source control:** sixteen outcomes depending on one latent selector have rank 1 and
  strict surplus 14.
- **Negative epicycle control:** eight independent one-output knobs have rank 8 and negative surplus.
- **Relabel control:** duplicating a column under another name does not increase rank.
- **Live matrix:** exact rank 8; every column pivots; the three umbrella pairs each have rank 2.

These controls prevent two opposite mistakes: counting synonyms as new physics and counting distinct
dependency signatures as one datum because they share a narrative role.

## 6. Verdict

### What survives

Story 3 survives as a serious architecture:

> Laws can define an admissible class without selecting one realized member. Boundary/history data can do
> the selecting. The scientific content then lies in the invariant relations forced after that selection.

This is compatible with the strongest structural findings today: the `Z/3` arena cannot be reached by the
integer index; metric-compatible curvature cannot close `C2`; scale-covariant geometry does not fix
`mu_DW`; the reduced open subsystem need not itself be unitary; and an observer section need not be the
dynamical source.

### What fails today

The stronger claim that all residues have collapsed to **one independent external bit** fails the present
identifiability audit. The exact conservative rank is 8. No value in the live vector was frozen source-first,
the full package has zero strict compression surplus, and the count selector fails reuse, compression, and
risky cross-sector prediction.

The honest wording is therefore:

> Today's GU work localizes the unresolved physics to one boundary-selection **interface**, carrying at least
> eight currently independent coordinates. It has not yet shown that this interface is governed by one datum.

That is still potentially valuable. Localization is not derivation, but it is more precise than an
unstructured list of free parameters.

## 7. What would upgrade the story

A source-action construction upgrades the story only if it does all of the following in order:

1. declares the native/physicist construction map for every fork above;
2. derives at least seven independent relations reducing the rank from 8 to 1, or openly reports the
   residual rank it actually reaches;
3. freezes the remaining selector before comparison with the count, pole, PPN, GW, or cosmology;
4. reuses that same selector without sector-specific retuning;
5. predicts at least one cross-sector outcome not used in the freeze;
6. survives the test with the adverse control construction as well, or states exactly why it does not
   transfer.

The more modest and immediately feasible target is rank reduction from 8 to a smaller number. Even a proved
rank-3 source action would be real compression. The audit should be rerun after each built relation rather
than declaring victory only at rank 1.

## 8. Explicit falsifiers

The boundary-selection story, in its strong explanatory form, is falsified or demoted by any of these:

1. **Rank persistence:** the completed source action leaves two or more independent selector coordinates
   after all native relations are imposed.
2. **Post-hoc motion:** a selector must be changed after seeing the generation count, pole sheet, DESI/DE,
   PPN, or GW result.
3. **Sector splitting:** the "same" datum takes different values in matter, gravity, quantum, observer, or
   cosmology sectors without a derived translation law.
4. **No risky surplus:** after excluding calibration rows and definitional identities, the strict selection
   surplus is non-positive.
5. **Count tautology:** the count selector yields no consequence beyond selecting the observed count.
6. **Construction failure:** a claimed no-go or relation exists only for the physicist vertex or only for the
   native projector/current, while the actual source action uses the other and no transfer theorem is built.
7. **Metric conflation:** the same scale or sign is assigned to the base `X4` metric and the gimmel/DeWitt
   metric without a derived map.
8. **Law/shadow conflation:** an induced `|II|^2` pole is treated as a fundamental-law degree of freedom
   despite the linear shiab-Einstein law, or dismissed solely because the parent law is linear despite the
   shadow being what propagates.
9. **Positive-Hilbert escape by relabeling:** KEEP-AND-GRADE fails and the repair silently removes the ghost;
   that may define a viable different theory, but it falsifies this boundary-selection construction.

## 9. What this does not do

- It does not prove GU, a source action, a C-operator, or a boundary ontology.
- It does not move H59, the count, bar (b), canon, `RESEARCH-STATUS`, or publication posture.
- It does not assert that the eight-coordinate lower bound is fundamental. It is the rank of today's live
  construction ledger.
- It does not treat WI-068 coordination prose as repo truth. The cited explorations provide the object-level
  dependencies; WI-068 supplied only the phrase "one external datum" being audited.
- It does not use the standard-physics and native-geometer constructions interchangeably. Each transfer gap
  is named above.

**Artifacts:** this file and `tests/W188_boundary_selection_nonvacuity.py`.
