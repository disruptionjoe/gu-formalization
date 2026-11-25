---
status: exploration
doc_type: structural-result
created: '2026-11-25'
program_target: LB-LADDER
tier: T1
expected_delta: Classify tensor-supported finite normalization and its symmetry-restoration limit without
  constructing an action.
premises:
- SC-GEO-03 supplies the metric-fibre arena, not a probability measure
- SC-CHI-51/52 assert VEV/curvature decoupling, not full tensor disappearance
- SC-GEO-55 concerns gauge-rotated-LC displacement; applying this theorem requires its effective joint stabilizer
- Finite invariant background probability and a common regular limit are additional hypotheses
source_bridge:
  status: conditional
  reason: 'Source necessity is ABSENT: no cited source claim requires finite invariant background probability,
    full tensor restoration or a common regular probability limit.'
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
internal_target_verdict: scoped internal class exclusion; no source claim killed
bears_on:
- SC-GEO-03
- SC-GEO-55
- SC-CHI-51
- SC-CHI-52
- SC-META-53
canon_verdict_change: none
title: 'Restoring Lorentz symmetry: singular limits and the observation burden'
class_covered: Lorentz-equivariant probability families on the full fixed-signature metric fibre, with
  a common weak probability limit at a fully Lorentz-fixed parameter; no claim from scalar-curvature decrease
  alone.
actual_delta: Every invariant finite probability is supported on the positive conformal ray; a common
  restored limit cannot be a regular full-dimensional density. Scalar-flat tensor strata and direction-dependent
  or singular limits survive.
internal_target: INTERNAL-REGULAR-RESTORED-FIBRE-PROBABILITY
kill_condition: A common weak probability limit at full Lorentz restoration is confined to the conformal
  ray, excluding a smooth full-dimensional probability limit.
---

# Restoring Lorentz symmetry: singular limits and the observation burden

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`

```yaml
program_target: LB-LADDER
tier: T1
expected_delta: Classify tensor-supported finite normalization and its symmetry-restoration limit without
  constructing an action.
actual_delta: Every invariant finite probability is supported on the positive conformal ray; a common
  restored limit cannot be a regular full-dimensional density. Scalar-flat tensor strata and direction-dependent
  or singular limits survive.
```

```gu-typed-objects
result: Restoring Lorentz symmetry: singular limits and the observation burden
carrier: fixed-signature Lorentz metric fibre in Sym2(Vstar) LAYER=ambient CHIRALITY=N/A
pairing: positive absolute density ON=metric_fibre; not physical Krein positivity
real_structure: real downstairs Lorentz (3,1); no identification of K95 and K77
grading: N/A
action_owner: repository-construction
target: invariant measure and symmetry MAP-TYPE=not-a-map
```

## 1. Result and exact hypotheses

**Target:** X-P1-P2-P3; P1/P3 domain-boundary, P2 symmetry; LB-LADDER.
**Tier:** T1 internal structural exclusion; no source, physics-ledger or class-C verdict changes.
**Source-necessary claim tested:** no. **Weakest source link:** the source does not require a finite invariant background probability or a common regular limit. Separately, scalar-curvature decay does not imply full Lorentz restoration. **Class-C representativeness:** unresolved.

Use V,g,G,E,M and the left action from the [effective-stabilizer theorem](tensor-stabilizer-normalization-2026-11-25.md). This note classifies the singular alternatives the prior smooth-density theorem deliberately left open. It does not equate an invariant probability with an arbitrary normalized quantum state.

**Theorem B1.** Every G-invariant Borel probability on M is supported on

    {c g : c>0}.

Conversely every probability supported on this ray is G-invariant. In particular δ_g is a counterexample to any claim that *all* finite invariant measures are impossible. The ray leaves the distribution of scale c completely open; it does not select c=1, the observing section, a section quotient or a physical normalization.

**Theorem B2.** Suppose a G-invariant punctured parameter domain approaches a G-fixed parameter z0, μ_z are G-equivariant probability measures on M, and they have a **common, path-independent weak probability limit** μ0 as z→z0. Then μ0 is supported on the same ray. Therefore it cannot be a smooth full-dimensional probability density. If z0 is already included in an equivariant family, invariance at z0 alone gives B1; continuity is only needed for the extension assertion.

One-path convergence or tightness alone does not imply invariance. Tight families can have singular or distinct cluster limits. A common probability limit plus local uniform absolute continuity of densities would be contradictory; a fixed first jet or diagonal value alone is not that uniform regularity condition.

## 2. Proof of the support theorem

Let W=span(supp μ)⊂E. It is invariant. The invariant-probability lemma in the companion note gives compact induced G action on W. A coordinate Lorentz boost is diagonalizable over the reals with positive eigenvalues in E. Its restriction to any invariant W remains diagonalizable. Boundedness of all positive and negative powers forces every eigenvalue on W to be1. Thus each of the three coordinate boosts acts identically on W.

The simultaneous fixed subspace of those three boosts on Sym²(V*) is exactly Rg. This follows by elementary matrix algebra, checked both with exact rational boosts cosh=5/4, sinh=3/4 and in Lean. Hence W⊂Rg. Fixed signature(-+++) excludes c≤0, establishing support on c>0. The converse is immediate since G fixes every cg.

The proof concerns the actual downstairs Lorentz representation on metric forms. It does not use an elliptic/Krein spectral transfer, a native Fredholm grading, or any source differential equation.

## 3. Proof and limits of the restoration statement

For fixed A∈G, continuity gives Az→z0. Since the limit is common, μ_Az→μ0. Equivariance gives μ_Az=A_*μ_z→A_*μ0 by continuity of pushforward under the fixed linear homeomorphism of M. Uniqueness of weak limits implies A_*μ0=μ0; now apply B1.

A restoring family can therefore concentrate onto the conformal ray, fail to have a common limit (including direction-dependent limits), or lose tightness in M. Escape toward degenerate metrics is loss of tightness in M even if the same sequence remains bounded in ambient E. These are exits from the stated regular common-limit requirements; they are not disproofs of every singular or state-dependent construction.

### Exact directional control

For a future timelike v=εu, where g(u,u)=−1 and ε>0, let

    h_u=g+2u_flat⊗u_flat,
    μ_v=Z_τ^{-1} exp(f0−τQ_(h_u)) μ_K

with fixed τ. This is a covariant family on the timelike cone, independent of ε for a fixed direction u. All unit clocks are Lorentz-related, so Z_τ is independent of u. Distinct clocks give distinct measures. To see this exactly, choose a null covector ℓ separating u and u', and take y=g+sℓ⊗ℓ. The determinant lemma and Sherman–Morrison formula give det y=det g and

    Q_(h_u)(g,y)=8s²[ℓ(u)]⁴.

Different future unit clocks can be separated by such a null ℓ. Thus the limits along εu and εu' differ. This particular family has no common limit at v=0. It does not exclude other families with singular common limits.

### Singular path limits really remain possible

Fix u and put μ_ε=Z_ε^{-1} exp(f0−Q_(h_u)/ε²) μ_K. Then μ_ε⇒δ_g as ε↓0. A small coordinate ball of radius ε about g has mass bounded below by c ε^10 before normalization, since Q has a positive quadratic minimum and the base density is smooth positive there. Outside any fixed neighborhood of g, properness and the unique zero give Q≥δ>0. For ε small,

    unnormalized outside mass ≤ C exp(−δ/(2ε²)),
    μ_ε(outside) ≤ C' ε^(-10) exp(−δ/(2ε²)) →0.

The finite constant follows by domination with one fixed integrable Gaussian. This proves concentration. It is a **fixed-direction path** control, not a proof of a common all-direction covariant limit. The diagonal logjet remains the specified one; division by Z_ε changes the diagonal value. Do not infer concentration is impossible from the first jet.

## 4. What SC-CHI-52 actually licenses

SC-CHI-51/52 assert VEV/curvature-related effective chiral decoupling in the source Dirac/RS discussion. Scalar-curvature reduction does not imply that every curvature tensor, displacement field, state or order parameter vanishes. The scalar-flat Ricci stratum in the companion theorem retains compact isotropy and a canonical positive h. Adding εg changes scalar curvature while preserving that h. Thus a regular finite density can persist as scalar curvature approaches0; the proposed inference from scalar0 to full restored symmetry **dies**.

If all such tensor data actually tend to a G-fixed value, B2 applies only after the source also selects the finite-probability and common-limit hypotheses. A direction retained as data or a state-selected noninvariant probability is a different surviving category. SC-META-53's internal maximal-compact statement supplies none of these bridges.

## 5. Joint follow-through: normalization does not repair literal observation

For each **fixed** smooth strictly positive density, its ratio to an ordinary smooth positive local reference density is bounded above and below on a compact tube around the observation section. Therefore the prior [exact-solution local-L2 nonclosability](solution-observation-trace-2026-11-25.md) persists for the **same operator and same admitted solution core**: its null-slab sequence still tends to0 while literal contraction has a fixed nonzero observed limit. The same applies to the graph norm when the sequence solves that same operator exactly.

This reuses the earlier theorem and earns no second exclusion credit. Global finite mass does not change this local argument. A density-dependent formal adjoint, conjugated operator, lower-order coupling or changed domain requires a separate check that the witness remains admitted and solves the new equation. Constants need not remain uniform as z varies; a singular limit changes the space/category.

Consequently a proposal using a compact-stabilizer density still needs an independent observation-domain repair, such as stronger regularity, a different admitted solution class, a quotient or a nonliteral readout with a source bridge. None is constructed here. The source contraction, 2+1 structure, total nonchirality, actual U versus optional Sp, and separate K95/K77 geometries are preserved.

## 6. What moved, what died, what survives

- **Class exclusion:** no full-dimensional finite positive invariant measure for noncompact effective isotropy; no regular full-dimensional common probability limit at full Lorentz restoration.
- **Rejected inference:** scalar-curvature0 alone restores full Lorentz isotropy. Explicit curvature strata and geometry disprove it.
- **Survivors:** compact effective isotropy (including scalar-flat Ricci), singular conformal-ray measures, direction-dependent families, noninvariant normalized states, alternative domains/readouts. These are mathematical categories, not certified GU realizations.
- **Not excluded:** GU, class C, SC-CHI-51/52, ordinary normalized L2 fermions, or the source's non-LC displacement. No count, chirality, parity, dark-energy or phenomenological prediction credit follows.

The next source-facing discriminator is the **effective joint stabilizer and observation-domain effect of the already-described non-LC displacement/tensor data**, if the source fixes enough representation information. The prior bounded source-law corpus audit is complete; repeating it is not the next test. Reopening needs newly authenticated representation/field-law data. Do not build the missing source operator or reopen tensor-free finite-density constructions. If source data do not determine the joint action, record that precise missing datum and continue the strongest eligible source-relevant class test.

## 7. Verification boundary

`tensor_normalization_probe.py` checks exact finite-dimensional controls and contrary examples. `LorentzMeasureCore.lean` proves actual three-boost fixed matrices are conformal; the analytic compactness, integrability and weak-limit arguments remain written proofs with independent measure/representation specialists and a hostile physics review. See the joint review and machine evidence linked in the companion note. This is verified algebra plus reviewed analysis, not a fully formalized probability theorem or a validated source realization.
