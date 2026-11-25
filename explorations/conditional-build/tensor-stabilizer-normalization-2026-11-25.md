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
title: 'Tensor-supported metric-fibre normalization: the effective stabilizer criterion'
class_covered: All finite-dimensional tensor-orbit inputs with commuting Lorentz/internal-gauge actions,
  gauge trivial on the metric fibre, and a smooth strictly positive finite measure on the full fixed-signature
  metric fibre.
actual_delta: A finite positive invariant density exists on a fixed tensor orbit iff its effective Lorentz
  stabilizer is compact; scalar-flat Ricci is a constructive survivor and gauge compensation can remove
  an apparent clock.
internal_target: INTERNAL-TENSOR-NORMALIZATION-NONCOMPACT-ISOTROPY
kill_condition: A noncompact effective stabilizer excludes every finite smooth strictly positive invariant
  measure in this category.
---

# Tensor-supported metric-fibre normalization: the effective stabilizer criterion

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
actual_delta: A finite positive invariant density exists on a fixed tensor orbit iff its effective Lorentz
  stabilizer is compact; scalar-flat Ricci is a constructive survivor and gauge compensation can remove
  an apparent clock.
```

```gu-typed-objects
result: Tensor-supported metric-fibre normalization: the effective stabilizer criterion
carrier: fixed-signature Lorentz metric fibre in Sym2(Vstar) LAYER=ambient CHIRALITY=N/A
pairing: positive absolute density ON=metric_fibre; not physical Krein positivity
real_structure: real downstairs Lorentz (3,1); no identification of K95 and K77
grading: N/A
action_owner: repository-construction
target: invariant measure and symmetry MAP-TYPE=not-a-map
```

## 1. Result, scope and novelty

**Target:** X-P1-P2-P3; P1/P3 domain-boundary, P2 symmetry; LB-LADDER.
**Tier:** T1 internal class exclusion. No physics-ledger, source-register, canon or class-C verdict changes.
**Source-necessary claim tested:** no. **Weakest unproved source link:** finite invariant background probability is necessary for the source mechanism. **Class-C representativeness:** unresolved; this is a measure category, not an action class.

The prior [metric-only theorem](natural-density-fibre-volume-2026-11-25.md) rules out finite positive natural measures with only (g,y) input. Its clock-assisted density is already owned. The new result classifies which additional tensor-orbit inputs can permit that escape, including internal gauge compensation. The invariant-probability lemma is known mathematics; the application and source-relevance audit are the repository delta.

Let V be real four-dimensional, g have signature (-+++), G=SO^+(g), E=Sym²(V*), and M the open subset of metrics of the same signature. Use the **left** action A·y=A^{-T}yA^{-1}; replacing A by A^{-1} gives the congruence convention in the prior note. The group preserves g. Extra tensor data z have a finite-dimensional continuous G×K action, with K acting trivially on M. Set

    H_eff = closure of projection to G of Stab_(G×K)(z).

This is the closure of the stabilizer of the gauge orbit, allowing limiting compensated transformations; the projected stabilizer need not itself be closed. A gauge-invariant G-equivariant assignment μ_z must be H_eff-invariant. If the actions do not commute, they must at least define the stated semidirect action and an action on gauge orbits; otherwise the quotient question is not yet typed. If K acts nontrivially on M, use the actual induced image instead: the present formula is not a transfer theorem.

**Theorem A.** For a closed subgroup H of G, there exists an H-invariant smooth strictly positive finite density on all M **iff H is compact**. Consequently the same criterion decides existence of a covariant density assignment on one tensor orbit, with H=H_eff. It does not assert a canonical selection or smooth extension across orbit strata.

## 2. Proof of necessity: invariant probability forces compact linear action

**Lemma.** A linear group preserving a Borel probability μ on a finite-dimensional real W whose support spans W is relatively compact in GL(W).

The span of support is invariant. Suppose h_n is unbounded. After dividing by operator norm and passing to a subsequence, h_n/||h_n|| tends to a nonzero T. For every v outside ker T, ||h_n v|| tends to infinity. For every R>0, Fatou and invariance imply

    μ(W \ ker T) ≤ liminf μ{v: ||h_n v||>R} = μ{v: ||v||>R}.

Let R tend to infinity. The support is contained in ker T, contradicting spanning. The group is uniformly bounded; so are its inverses, which belong to the same group. Its closure is therefore compact in GL(W).

This is a self-contained version of the known invariant-probability compact-action fact; see Baues–Globke–Zeghib, *Rigidity of pseudo-Hermitian homogeneous spaces of finite volume*, [Proposition 3.6(3)](https://perso.ens-lyon.fr/zeghib/Pseudo_Hermitian_Homogeneous.pdf), pp10–11; also Meerschaert–Veeh, [*Symmetry groups in d-space*](https://www.stt.msu.edu/users/mcubed/GROUPS.pdf), p2. No novelty claim is attached to the lemma.

A strictly positive smooth density on the open M has support spanning E. The induced congruence action is bounded by the lemma. For Euclidean Frobenius norms its operator norm on symmetric matrices is ||A||² (the lower bound is attained on rank-one xxᵀ, and the upper bound is immediate). For our inverse convention use A^{-1}; a group contains its inverses. Thus H is bounded in the defining representation. Since H is closed in the closed Lorentz group and Lorentz limits remain invertible, H is compact. Normalizing a finite positive mass to probability loses no hypothesis.

## 3. Sufficiency, including the retained diagonal jet

Average any positive Euclidean metric over compact H to get an H-invariant positive metric h. The canonical absolute vertical volume is, up to a fixed positive constant,

    dμ_K(y)=C |det y|^(-5/2) dy.

For fixed g,h put

    f0(g,y)=−(1/2) log|det(g^{-1}y)|,
    Q_h(g,y)=||y−g||_h² + ||y^{-1}−g^{-1}||_(h^{-1})²,
    ρ_τ(g,y)=exp(f0(g,y)−τ Q_h(g,y)),     τ>0.

The first norm is on covariant forms and uses h^{-1}; the second on contravariant forms uses h. Both are positive Euclidean tensor norms. Q is proper on M, has unique zero g and zero differential there. These formulas are H-invariant. The inverse Gaussian absorbs every inverse-determinant power near det y=0; the first Gaussian controls infinity. More explicitly, |det y|^{-3} ≤ ||y^{-1}||^{12}, and polynomial growth is absorbed by exp(−τ||y^{-1}−g^{-1}||²); the remaining Gaussian is integrable over E. Hence ∫ρ_τ dμ_K is finite.

The previously required supplied jet survives:

    ρ_τ(g,g)=1,
    d_y logρ_τ|_g(v)=−(1/2) tr(g^{-1}v).

For the separate K_λ geometry with λ=1/2 this is the prior b=H jet. It does not establish that this adjoint condition is source-necessary or sufficient for any unbuilt operator.

There is **no normalization-versus-jet obstruction**. For fixed reference volume define Z(τ)=∫ρ_τ dμ_K. It is continuous on τ>0 by dominated convergence on compact τ intervals, strictly decreasing because Q>0 almost everywhere, tends to0 as τ→∞, and tends to∞ as τ↓0 by monotone convergence and the prior metric-only infinite-mass theorem. Thus a unique τ gives Z(τ)=1, while preserving both ρ(g,g)=1 and its logjet. Alternatively division by Z normalizes any τ while preserving only the logjet. Choice of reference volume and unit mass is explicit, not physical selection.

Transport from one orbit representative produces a well-defined equivariant density on its homogeneous orbit because the density is invariant under the joint stabilizer. No global section across orbit strata is promised.

## 4. What counts as enough additional structure

A closed H⊂SO^+(1,3) is compact iff it fixes some future timelike vector. For the forward direction average a future timelike vector over H; convexity of the future timelike cone gives a nonzero timelike invariant vector. For the reverse direction H is a closed subgroup of its SO(3) stabilizer. This is **existence of a clock direction**, not a unique, source-selected or observable clock.

| Fixed extra datum | Residual symmetry | Finite positive invariant density? |
|---|---|---|
| Scalars, scalar curvature, multiples of g | Full G | No |
| A future timelike vector | SO(3) | Yes |
| A nonzero spacelike vector | SO^+(1,2) | No |
| An exact nonzero null vector | Euclidean group E(2), with null rotations | No |
| A null ray alone | Includes boosts | No |
| Two ordered independent future null vectors | SO(2); their sum is timelike | Yes |
| Ricci-type tensor with separated timelike eigenline | Subgroup of SO(3) | Yes on that spectral stratum |

Equal stabilizer dimensions do not imply equal answers: the timelike, spacelike and null-vector stabilizers all have dimension3; only the first is compact. Two null **lines** are not the ordered-vector control because a compensating boost remains.

### Gauge compensation is indispensable

Let e:V→W be a coframe, let internal K=SO^+(W,g) act on the left, and external G on the right: (A,k)·e=k e A^{-1}. At e=Id the pure external stabilizer is trivial, but the joint stabilizer is the diagonal {(A,A)}. Its projected H_eff is all G. Therefore this datum does **not** provide a finite gauge-invariant positive fibre density, despite its trivial bare stabilizer.

This countercontrol is not an identification of the source displacement field. SC-GEO-55 concerns a displacement from gauge-rotated Levi-Civita data, with internal representation and compensation still to be supplied. Components cannot be treated as an ordinary physical torsion vector without that bridge. SC-META-53's internal maximal-compact shielding likewise does not select a downstairs Lorentz clock. Full U(64,64) is not silently replaced by optional Sp(32,32).

## 5. Scalar-flat curvature is a real contrary category

Take g=diag(−1,1,1,1), S=diag(3,1,1,1). Then tr(g^{-1}S)=0, but g^{-1}S has distinct timelike eigenvalue−3 and spatial eigenvalue1, with compact SO(3) stabilizer. The algebraic curvature tensor

    R_abcd=(g_ac S_bd+g_bd S_ac−g_ad S_bc−g_bc S_ad)/2

has curvature symmetries and Bianchi identity, g^{ac}R_abcd=S_bd and scalar0. This is an admissible local pseudo-Riemannian curvature model, independent of equations of motion; local realization is standard, e.g. Gilkey–Park–Sekigawa, [Theorem1.1](https://arxiv.org/pdf/1111.1380).

On this two-eigenvalue spectral stratum the positive metric can be obtained without choosing an eigenvector sign:

    A=g^{-1}S,  P_t=(A−λ_s I)/(λ_t−λ_s),
    h(v,w)=g(v,w)−2g(P_t v,w).

For this S, h=I. Replacing S by S+εg changes scalar curvature to4ε while preserving P_t and h exactly. Hence scalar curvature→0 can retain a perfectly regular finite density. This is a structural stratum, not only a single arbitrarily chosen clock.

There is also an explicit geometric realization with scalar curvature identically0:

    g=−dt²+t(dx²+dy²+dz²),    t>0.

Its orthonormal Ricci tensor is (3,1,1,1)/(4t²). This is an off-shell geometric control, **not a GU solution or source action**. It shows why SC-CHI-52's scalar-curvature decrease cannot be substituted for disappearance of all symmetry-breaking tensors.

## 6. Source consequence and remaining burden

No source claim dies. A proposed finite **invariant background** probability on M must supply extra data whose effective stabilizer is compact, or change the measure/support/category. This is a conditional necessary-and-sufficient fixed-orbit constraint. It does not require all ordinary normalized states to be invariant: an infinite invariant background measure can support many noninvariant normalized L2 wavefunctions transforming covariantly. Normalizable fermions do not by themselves imply finite background volume.

K95 and K77 remain separately typed. The argument uses the downstairs Lorentz action, not an identification of normal signatures or a positive Krein pairing. Observation remains source contraction; no 2+1, chirality or family-count inference follows. Symmetry-restoration and the actual-solution trace consequence are treated in the [companion result](symmetry-restoration-measure-limit-2026-11-25.md).

## 7. Verification and review

The exact probe `tests/program-focus/tensor_normalization_probe.py` checks stabilizers, gauge compensation, curvature and null-rank-one controls. `Lean/GUFormalization/LorentzMeasureCore.lean` checks the three actual rational-boost fixed-matrix equations, not probability compactness, integration or weak convergence. Independent reviews and their explicit coverage are recorded in `lab/process/hostile-reviews/2026-11-25-tensor-normalization-review.md`; machine evidence is in `lab/process/tensor-normalization-wave.json`.
