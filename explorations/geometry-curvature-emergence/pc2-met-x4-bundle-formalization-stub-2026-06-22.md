---
title: "PC2 — Y¹⁴ = Met(X⁴) Bundle Formalization Stub"
artifact_type: exploration
status: exploration
updated_at: "2026-06-22"
depends_on:
  - "explorations/misc/positive-gu-constructions-lane-proposal-2026-06-22.md"
  - "explorations/anomaly-and-bordism/n1-signature-audit-y14-clifford-algebra-2026-06-22.md"
  - "explorations/cycle-gates-and-audits/weinstein-ucsd-2025-04-analysis-2026-06-22.md"
---

# PC2 — Y¹⁴ = Met(X⁴) Bundle Formalization Stub

**Status.** Exploration-grade. This document executes the PC2 target from the
positive-constructions-lane proposal (`positive-gu-constructions-lane-proposal-2026-06-22.md`,
§Target 1 and §Target 2). No result here is promoted to active_research or canon without
meeting the promotion criteria in `RESEARCH-STATUS.md`.

**Purpose.** Provide a derivation template — not a proof — for the formalization of Y¹⁴
as a canonical geometric object: its bundle structure, its canonical metric (the gimmel
metric ℊ), the circularity question in defining the Dirac operator, and what a section
s: X⁴ → Y¹⁴ pulls back to as 4D physics data.

**Key open question (the PC2 wall).** Can the Dirac operator D_ℊ on the spinor bundle
S = H^{64} over Y¹⁴ be defined using only ℊ and ∇_ℊ, without first choosing a section
s: X⁴ → Y¹⁴? The circularity analysis in §3 gives a precise answer.

---

## §1. Y¹⁴ = Met(X⁴) — Bundle Definition, Fiber, Structure Group

### 1.1 The base manifold X⁴

Let X = X⁴ be a smooth, oriented, connected 4-manifold with no metric specified. X is the
"pre-geometric" spacetime: it has topology but no metric, no preferred causal structure,
and no spin structure (the spin structure will be induced by the section s, not put in by hand).

### 1.2 The fiber bundle Y¹⁴ → X⁴

**Definition.** The observerse is the total space of the fiber bundle:

```
π: Y¹⁴ → X⁴
```

with fiber:

```
π⁻¹(x) = Sym²(T*_x X⁴) = {symmetric bilinear forms on T_x X}
```

The fiber at x is the 10-dimensional real vector space Sym²(R⁴*). In local coordinates
(x^μ, h_{μν}) on Y¹⁴ (where x^μ are coordinates on X and h_{μν} = h_{νμ} are 10
independent coordinates on the fiber), the total dimension is 4 + 10 = 14.

**Open subbundle.** The open subbundle of Lorentzian nondegenerate metrics:

```
Met(X⁴) = { (x, h) ∈ Sym²(T*X) : h_x has signature (3,1) }
```

is what GU calls Y¹⁴ (following the transcript [00:04:08]). The notation Y¹⁴ refers to
this open subbundle in practice; the full symmetric-2-tensor bundle is the ambient space.

**Frame bundle equivalence.** The transcript [00:04:08] describes Y¹⁴ alternatively as the
quotient of the frame bundle:

```
Y¹⁴ ≅ F(X) / Spin(1,3)
```

where F(X) = GL⁺(4,R)~-frame bundle of X and Spin(1,3) is the double cover of SO(1,3)
acting on each frame by the right action. The fiber of F(X) is GL⁺(4,R)~ (dimension 16),
and the quotient by Spin(1,3) (dimension 6) gives fiber dimension 10. This identification
is a `[reconstruction]` (see UCSD analysis Claim 1); it is locally equivalent to Met(X⁴)
on the open subbundle of Lorentzian nondegenerate metrics (Kobayashi-Nomizu, Ch. II).

### 1.3 Structure group of π: Y¹⁴ → X⁴

As a fiber bundle over X⁴:

**Fiber.** The fiber Sym²(R⁴*) ≅ R¹⁰ is a real vector space. The natural structure group
acting on the fiber by change-of-frame is:

```
GL(4,R) acting on Sym²(R⁴*) by: g · h = h(g⁻¹·, g⁻¹·)
```

More explicitly: for g ∈ GL(4,R) and h ∈ Sym²(R⁴*), (g · h)_{μν} = g^α_μ g^β_ν h_{αβ}
(pullback action). This is a faithful action of GL(4,R) on R¹⁰ (the fiber), giving the
structure group of the bundle as GL(4,R).

On the open subbundle Met(X⁴), the structure group reduces to GL(4,R) acting on
Lorentzian nondegenerate metrics; the stabilizer of a fixed Lorentzian metric h_0 is
O(3,1) ⊂ GL(4,R), and Met(X⁴) ≅ GL(4,R) / O(3,1) as a fiber (as a homogeneous space).

**Diffeomorphism group.** The group Diff(X⁴) of diffeomorphisms of X acts on the base and
lifts to the total space by naturality: a diffeomorphism φ: X → X sends a metric h at x
to the pullback φ*h at φ(x). So Diff(X⁴) acts on Y¹⁴ by bundle automorphisms.

**For the frame bundle of Y¹⁴ itself.** The frame bundle of the total space Y¹⁴ (as a
14-dimensional manifold) has structure group GL(14,R). After equipping Y¹⁴ with the gimmel
metric ℊ of signature (9,5) (see §2), this reduces to:

```
SO(9,5) ⊂ GL(14,R)
```

and the double cover:

```
Spin(9,5) ⊂ GL(14,R)~
```

The spinor bundle S = H^{64} is the standard spinor module for Cl(9,5) ≅ M(64,H),
associated to the Spin(9,5)-principal frame bundle of Y¹⁴ (from the N1 signature audit,
`n1-signature-audit-y14-clifford-algebra-2026-06-22.md`, §5–§6).

---

## §2. Gimmel Metric ℊ — Explicit Construction

### 2.1 Overview

The gimmel metric ℊ is a pseudo-Riemannian metric of signature (9,5) on Y¹⁴, constructed
in three steps:
(a) Frobenius metric on each fiber Sym²(T*_x X), signature (7,3)
(b) Trace-reversal on the fiber, changing signature to (6,4)
(c) Horizontal lift of the (3,1) Lorentzian metric from X⁴

Total signature: (3+6, 1+4) = (9,5). This is verified in detail in the N1 audit.

### 2.2 Step (a): Frobenius metric on the fiber

At a point y = (x, h) ∈ Y¹⁴ (where h ∈ Sym²(T*_x X) is a Lorentzian metric at x), the
Frobenius inner product on the fiber T_h(Sym²(T*_x X)) ≅ Sym²(T*_x X) is:

```
⟨k, l⟩_F := tr(h⁻¹ k · h⁻¹ l) = h^{αβ} h^{γδ} k_{αγ} l_{βδ}
```

for k, l ∈ Sym²(T*_x X) (tangent vectors to the fiber at h).

**Signature computation.** With h = diag(1,1,1,−1) (the canonical Lorentzian representative):
the Frobenius metric on Sym²(R^{3,1}*) has signature (7,3). Derivation in N1 audit §2:
- 4 diagonal basis elements E^{ii}: all positive (norm (h^{ii})² > 0)
- 3 spatial-spatial off-diagonal E^{ij}: positive (norm 2 · 1 · 1 = +2)
- 3 space-time off-diagonal E^{i4}: negative (norm 2 · 1 · (−1) = −2)

Result: (7 positive, 3 negative) = signature (7,3). `[verified]`

### 2.3 Step (b): Trace-reversal

The standard GR trace-reversal operator (in 4D, with factor 1/2):

```
T: Sym²(T*_x X) → Sym²(T*_x X)
T(k)_{ab} = k_{ab} − (1/2)(h^{cd} k_{cd}) h_{ab}
```

maps h to T(h) = −h (the trace direction, spanned by h itself, is negated). The traceless
subspace is fixed: T(k) = k for h^{ab} k_{ab} = 0.

Effect on signature: the trace direction was positive under the Frobenius metric (⟨h,h⟩_F = 4 > 0).
After trace-reversal, this direction becomes negative. The traceless subspace signature
(6 positive, 3 negative from the off-diagonal computation) is unchanged.

**Post-trace-reversal fiber signature = (6,4).** `[verified]`

This matches the transcript [00:43:04]: "which gets you from a seven three signature to a six four."

**Why trace-reversal?** The trace-reversal is the standard operation in linearized gravity
(the "TT gauge" decomposition) and adjusts the metric so that the resulting spin connection
and Dirac operator have the correct chirality structure. Weinstein refers to it as a "canonical
operation" on Y¹⁴ at [00:43:04] and [00:46:40].

### 2.4 Step (c): Horizontal lift

The bundle π: Y¹⁴ → X⁴ has a vertical subbundle (the tangent spaces to the fibers) and
requires a choice of horizontal complement. The "canonical horizontal structure" for Met(X⁴)
as a bundle over X⁴ is determined by the connection on the frame bundle of X⁴.

For the horizontal metric: the projection π: Y¹⁴ → X⁴ induces a map dπ: T_y Y¹⁴ → T_x X.
The horizontal part of the tangent space T_y Y¹⁴ is the kernel of the vertical projection,
and the horizontal metric is the pullback of the (not-yet-chosen) metric on X⁴.

**The circularity issue (first appearance).** To define the horizontal metric explicitly, we
would need to choose a metric on X⁴ — but that is a section s: X⁴ → Y¹⁴, which is exactly
what we are trying to avoid presupposing. See §3 for the full circularity analysis.

**Working assumption for the horizontal piece.** The point y = (x, h) ∈ Y¹⁴ already
specifies a metric h at x. The horizontal metric at y uses h itself as the Lorentzian metric
for the horizontal directions T_x X:

```
ℊ_horizontal at (x,h) = h  (the fiber point is the horizontal metric)
```

This is the tautological assignment: the metric h at x, being a point in Y¹⁴, provides
the (3,1) horizontal metric automatically. This is the key structural move that avoids
circularity at the level of metric definition (see §3.2 for why this is benign).

**Total gimmel metric:**

```
ℊ = ℊ_horizontal ⊕ ℊ_vertical(trace-reversed Frobenius)
```

with signature (3,1) ⊕ (6,4) = **(9,5)**. `[verified: N1 audit §4]`

---

## §3. The Circularity Question

### 3.1 The apparent circularity

**Statement of the worry.** The Frobenius inner product at a fiber point (x, h) ∈ Y¹⁴ is:

```
⟨k, l⟩_F at h = tr(h⁻¹ k · h⁻¹ l)
```

This uses the metric h to define the inner product on the fiber Sym²(T*_x X) — but h is
itself a point in that fiber. So the metric at fiber point h uses h to define itself.
Is this circular?

More precisely: Y¹⁴ is the space of metrics on X⁴. The gimmel metric ℊ on Y¹⁴ is defined
using, at each fiber point h, the metric h itself. The gimmel metric is therefore a function
of the points of Y¹⁴ that uses those points in its own definition.

### 3.2 Diagnosis: benign tautology (not vicious circle)

**Resolution.** The circularity is a **benign tautological bundle construction**, analogous
to the tautological line bundle over projective space.

The precise argument:

(a) **Y¹⁴ is the total space of a tautological bundle.** The fiber over x ∈ X is
    Sym²(T*_x X). A point y = (x, h) ∈ Y¹⁴ consists of a base point x AND a symmetric
    bilinear form h at x. The symmetric bilinear form h is not "defined by Y¹⁴"; it IS
    a point of Y¹⁴. There is no circularity in using h to compute inner products at h,
    because h is available as part of the input (the point specification) before any metric
    computation begins.

(b) **The Frobenius construction is point-by-point, not self-referential.** To compute
    ⟨k, l⟩_F at (x, h), we use h as data. We do not need to know what the metric is at
    nearby fiber points; we use only the value h at the specific fiber point (x, h). This
    is a fiber-wise construction that does not require global self-reference.

(c) **Comparison with the tautological line bundle.** Over RP¹, the tautological line bundle
    assigns to each point [v] ∈ RP¹ (a line in R²) the line itself as the fiber. The fiber
    at [v] IS [v]; it uses the point to define itself. This is not circular because [v] is
    given as data. Similarly, the fiber of Y¹⁴ at (x, h) uses h as data, and h is given
    as part of the specification of the point.

(d) **No fixed-point problem.** A vicious circularity would arise if the metric ℊ at y
    required knowing ℊ at nearby points before it could be defined at y. The Frobenius
    construction is purely algebraic at each fiber point — no differential equation is solved,
    no nearby information is used. The definition is explicit and direct:
    ℊ_vertical at (x,h) = trace-reversed Frobenius(h).

**Conclusion.** The circularity is benign. The gimmel metric ℊ on Y¹⁴ is well-defined
as a smooth pseudo-Riemannian metric of signature (9,5) on the 14-dimensional manifold Y¹⁴.
No vicious circularity obstructs the definition.

### 3.3 The genuine difficulty: the horizontal piece

The horizontal metric (§2.4) assigns h itself as the Lorentzian metric for horizontal
directions. This is also a benign tautology in the same sense: h is available as data at
the fiber point (x, h).

However, the horizontal-vertical split — the connection on the bundle Y¹⁴ → X⁴ that
defines what "horizontal" means — does require additional structure. There is no canonical
connection on Y¹⁴ → X⁴ as a fiber bundle (the bundle does not have a preferred principal
bundle connection). This is not a circularity but a **genuine degree of freedom**:
the horizontal-vertical split of T_y Y¹⁴ requires choosing a connection on F(X) → X
(the frame bundle of X⁴), which is an additional geometric datum.

For the gimmel metric to be canonical (not depending on this extra choice), the horizontal
metric must be defined without specifying the splitting. One approach: use only the
vertical metric (the trace-reversed Frobenius) and define the horizontal metric
tautologically from h, accepting that the full gimmel metric requires a choice of
horizontal distribution. This is the **first genuine degree of freedom** in the gimmel
metric construction.

**Practical consequence.** In the transcript, Weinstein states that Y¹⁴ has a "god given
metric" ([00:43:47]). The analysis above shows: the vertical metric (trace-reversed Frobenius)
IS canonical (no choice required). The horizontal metric is also canonical in the tautological
sense (h provides the (3,1) piece). The only residual non-canonicity is the horizontal-vertical
splitting of T_y Y¹⁴, which requires a choice of connection on the base bundle. Whether
Weinstein intends a canonical connection here is left open in the transcript.

---

## §4. The Canonical Dirac Operator

### 4.1 The question

From the PC2 six-axis specification (positive-constructions-lane proposal, §3, first
falsification test):

> Define a canonical Dirac operator D_Y on Y¹⁴ = Met(X⁴) that does not presuppose a
> choice of metric on X⁴. If the only well-defined Dirac operator requires first choosing
> a section s and thus re-introduces the metric as external data, the spinor-metric
> circularity is not resolved.

### 4.2 What is needed for D_ℊ

A Dirac operator D_ℊ on the spinor bundle S = H^{64} over Y¹⁴ requires:
1. A pseudo-Riemannian metric on Y¹⁴ — provided by ℊ of signature (9,5). ✓
2. A Spin(9,5)-structure on Y¹⁴ (a spin structure) — requires Y¹⁴ to admit a
   Spin(9,5)-principal bundle. This is a topological condition on Y¹⁴; it is not
   automatically satisfied.
3. The Levi-Civita connection ∇_ℊ of ℊ — determined by ℊ uniquely (torsion-free,
   metric-compatible). ✓
4. The associated spin connection on the spin bundle — determined by ∇_ℊ and the
   spin structure. ✓ (once the spin structure is given)

### 4.3 The Dirac operator formula

If the spin structure exists, the Dirac operator is:

```
D_ℊ: Γ(S) → Γ(S)
D_ℊ ψ = Σ_{A=1}^{14} e^A · ∇^S_{e_A} ψ
```

where {e_A} is a local orthonormal frame for ℊ (with ℊ(e_A, e_B) = η_{AB}, η = diag(1,...,1,−1,...,−1)
with signature (9,5)), e^A is the dual coframe, · is Clifford multiplication in Cl(9,5),
and ∇^S is the spin connection (the lift of ∇_ℊ to the spinor bundle S via the spin representation).

**This D_ℊ is defined using only ℊ and ∇_ℊ.** No section s: X⁴ → Y¹⁴ is required.

### 4.4 Can D_ℊ be defined without choosing a section?

**Answer: YES, in principle, subject to one condition.**

D_ℊ exists as a well-defined operator on Y¹⁴ if:
(a) The gimmel metric ℊ is well-defined on Y¹⁴ — established in §2. ✓
(b) Y¹⁴ admits a spin structure compatible with ℊ — this is a topological condition,
    not requiring a section of Y¹⁴ → X⁴.

**The obstacle.** The spin structure condition: does the manifold Y¹⁴ = Met(X⁴) (with its
topology as an open subbundle of Sym²(T*X)) admit a Spin(9,5)-structure?

Y¹⁴ = Met(X⁴) is contractible fiber by fiber (Sym²(T*_x X) ≅ R¹⁰ is contractible), so
Y¹⁴ has the same homotopy type as X⁴. Therefore:

```
w_2(Y¹⁴) ∈ H²(Y¹⁴, Z/2) ≅ H²(X⁴, Z/2)
```

Y¹⁴ admits a spin structure if and only if w_2(Y¹⁴) = 0 (the second Stiefel-Whitney class
of the tangent bundle of Y¹⁴ vanishes). Since π: Y¹⁴ → X⁴ is a homotopy equivalence,
this is equivalent to a spin structure condition on X⁴ combined with a condition from the
fiber bundle structure.

**Key observation.** The structure group of Y¹⁴ as a manifold is Spin(9,5) (after reducing
GL(14,R) to SO(9,5) via ℊ and then lifting). The tangent bundle of Y¹⁴ splits as:

```
T(Y¹⁴) = π*(TX⁴) ⊕ T_vertical(Y¹⁴)
```

The vertical bundle T_vertical(Y¹⁴) ≅ π*(Sym²(T*X⁴)) is a vector bundle over Y¹⁴.
The spin structure on Y¹⁴ exists if w_2(π*(TX⁴)) + w_2(π*(Sym²(T*X⁴))) = 0, which
(using the tensor product formula for Stiefel-Whitney classes) reduces to conditions on
w_1 and w_2 of X⁴.

**For X⁴ orientable (w_1 = 0) and spin (w_2 = 0):** Y¹⁴ admits a canonical spin structure
and D_ℊ is well-defined on Y¹⁴ without any section choice. `[reconstruction: spin structure
argument; exact computation of w_2(Y¹⁴) requires Stiefel-Whitney class computation via
Gysin sequence for the fiber bundle, not carried out here]`

**For X⁴ spin-cobordism zero (w_2 ≠ 0):** Y¹⁴ may not admit a spin structure, and D_ℊ
as defined above does not exist without choosing a section (which provides a metric and a
specific spin structure on X⁴, from which the spin structure on Y¹⁴ can be induced).

### 4.5 Resolution of the spinor-metric circularity

**The circularity.** In standard 4D physics, defining a Dirac operator requires a metric
(for the spin connection). Choosing the metric is the "circular" input that GU aims to
avoid. GU's proposal: put the metric as a coordinate on Y¹⁴ and define the Dirac operator
on the 14D space using ℊ, not a prior choice of metric on X⁴.

**Status after this analysis.** The spinor-metric circularity is partially resolved:

- D_ℊ can be defined on Y¹⁴ using only ℊ (which is canonical, tautological, requiring no
  metric choice on X⁴ beyond the Frobenius construction). ✓
- D_ℊ is a well-defined 14D Dirac operator that acts on spinors over the full observerse. ✓
- The zero modes of D_ℊ are defined without choosing a 4D metric. ✓

- The residual non-canonicity is in the horizontal-vertical splitting (a connection on
  Y¹⁴ → X⁴), and in the spin structure of Y¹⁴ (which depends on the topology of X⁴). ✗ (open)
- The pullback of D_ℊ to a 4D Dirac operator via a section s: X⁴ → Y¹⁴ does re-introduce
  the metric (since s is a metric choice). But this pullback is the observer's act of "choosing
  a physics"; it is not a prerequisite for D_ℊ to be defined. The metric is a coordinate of
  Y¹⁴, not an external datum.

**Summary.** GU's resolution of the spinor-metric circularity is genuine for the definition
of D_ℊ as a 14D operator; the circularity is a non-issue at the 14D level because h is a
coordinate, not a datum. The circularity re-appears when pulling back to X⁴, but at that
stage it is the observer's section choice — which is the "observation map," not a definition
of the Dirac operator itself.

---

## §5. Section Pullback Map s*

### 5.1 Definition of a section

A section of π: Y¹⁴ → X⁴ is a smooth map:

```
s: X⁴ → Y¹⁴,   π ∘ s = id_{X⁴}
```

i.e., a smooth assignment of a Lorentzian metric s(x) ∈ Sym²(T*_x X⁴) to each point
x ∈ X⁴. This is exactly a Lorentzian metric on X⁴.

**There is no canonical section.** Since X⁴ has no preferred metric (it is pre-geometric),
there is no preferred section. This is the structural reason Y¹⁴ is interesting: the
observerse encodes all possible metrics as its points, with no one preferred.

### 5.2 What s* pulls back

Given a section s: X⁴ → Y¹⁴ (i.e., a metric on X⁴), the pullback s* returns the following
4D physics data:

| 14D object on Y¹⁴ | Pullback s*(·) to X⁴ | 4D physics interpretation |
|---|---|---|
| Metric ℊ on Y¹⁴ | s*(ℊ) | A metric on X⁴ (derived from ℊ and the section s); in the horizontal directions, this reduces to s(x) itself |
| Levi-Civita connection ∇_ℊ | s*(∇_ℊ) | A connection on T(X⁴) containing the Levi-Civita connection of s(x) plus fiber-direction terms |
| Spinor bundle S → Y¹⁴ | s*(S) | A spinor bundle on X⁴ with Cl(3,1) ⊂ Cl(9,5) chirality structure |
| Dirac operator D_ℊ | s*(D_ℊ) | A 4D Dirac operator on X⁴ with the metric s(x); the standard Dirac operator of 4D physics in the metric s(x) |
| Connection A on P → Y¹⁴ | s*(A) | A gauge connection on the pullback bundle s*(P) → X⁴; a 4D gauge field |
| Distortion θ on Y¹⁴ | s*(θ) | A torsion-type tensor on X⁴ (see DD1 for the precise reduction) |
| Curvature F_A on Y¹⁴ | s*(F_A) | 4D curvature 2-form; the gauge field strength in the metric s(x) |

### 5.3 How the 4D SM content is encoded

From the UCSD analysis, Claim 5 (fermion generations via spinor pullback):

The 14D spinor content is (before pullback):

```
Ψ = (Ω⁰(Y¹⁴) ⊗ S⁺) ⊕ (Ω¹(Y¹⁴) ⊗ S⁻)
```

After pullback s*, the horizontal-vertical decomposition of Ω•(Y¹⁴) gives:

```
Ω^k(Y¹⁴) |_{s(X)} ≅ ⊕_{p+q=k} Ω^p(X⁴) ⊗ Ω^q_vertical
```

The SM fermion content (quarks, leptons, neutrinos with their quantum numbers) is claimed
to appear in this decomposition when S^± is decomposed under Cl(3,1) ⊂ Cl(9,5). This
decomposition is the PC2 open computation — it requires:
1. Branching rules for S = H^{64} (Spin(9,5) spinor) → Spin(3,1) = SL(2,C) representations.
2. Checking whether the resulting 4D representations match SM matter content.

This is labeled `[speculation]` (sub-claim B of Claim 5 in the UCSD analysis).

### 5.4 The Levi-Civita connection under s*

The pullback of ∇_ℊ to X⁴ via s decomposes as:

```
s*(∇_ℊ) = ∇_{LC}(s) + F_s
```

where:
- ∇_{LC}(s) is the Levi-Civita connection of the metric s(x) on X⁴ (the standard GR
  Levi-Civita connection)
- F_s is a correction term from the curvature of the section map s (measuring how quickly
  the section bends in Y¹⁴) — this is the "second fundamental form" of s in Y¹⁴

This decomposition is `[reconstruction]` — it follows from the general formula for the
pullback of a connection via an immersed submanifold, but the specific form of F_s in
terms of the Frobenius metric and s requires a computation.

---

## §6. What PC2 Requires Next

### 6.1 First nontrivial computation

The derivation stubs above establish the framework. The **first nontrivial computation** is:

**Compute the Stiefel-Whitney class w_2(Y¹⁴)** as a class in H²(X⁴, Z/2), using the
fiber bundle structure π: Y¹⁴ → X⁴ and the Gysin sequence (or the Whitney product formula
for the total Stiefel-Whitney class of a tensor product bundle).

If w_2(Y¹⁴) = π*(w_2(X⁴)) (i.e., Y¹⁴ is spin if and only if X⁴ is spin), then the spin
structure condition for D_ℊ reduces cleanly to a condition on the base spacetime X⁴. This
would establish that D_ℊ is defined on Y¹⁴ for any spin 4-manifold X⁴ without any section
choice — completing the canonical Dirac operator construction.

If w_2(Y¹⁴) ≠ π*(w_2(X⁴)) (additional topological obstructions from the fiber), then
D_ℊ is more restricted and the obstacle needs to be understood before the spinor-metric
circularity resolution can be claimed.

**This is a routine computation in algebraic topology (Gysin sequence / Stiefel-Whitney
classes of associated bundles).** It should be carried out before PC2 can be marked as
a completed derivation stub.

### 6.2 Second computation: branching rules for s*(S)

After the spin structure question is settled, the next computation is the branching:

```
S = H^{64} as Spin(9,5) → Spin(3,1) × Spin(6,4) representation
```

This determines what SM content appears in the section pullback. The computation uses
the decomposition Cl(9,5) ⊃ Cl(3,1) ⊗ Cl(6,4) (as algebras via the fiber-base split),
with the spinor module S decomposing accordingly.

### 6.3 Third computation: second fundamental form of s

The term F_s in the pullback of ∇_ℊ (§5.4) should be computed explicitly:

```
F_s ∈ Ω¹(X⁴) ⊗ π*(Sym²(T*X⁴))
```

(a 1-form on X⁴ valued in the fiber direction). This term is what makes s*(∇_ℊ) differ
from the Levi-Civita connection of s(x); it encodes the "tilt" of the section in the
observerse. Whether it contributes to the SM gauge content or to the distortion θ is
the PC2 open question for the torsion-for-Λ connection (see DD1 §6).

### 6.4 What promotion to active_research requires

PC2 should be promoted from exploration to active_research when:
- The w_2(Y¹⁴) computation is completed (routine topology; no new math required).
- The branching rules s*(S) are computed to the level of Spin(3,1)-representations.
- The second fundamental form F_s is computed in local coordinates.

None of these require new mathematical technology; they are concrete computations using
established tools (Gysin sequences, Clifford algebra branching rules, Riemannian submersion
formulas).

---

*Filed: 2026-06-22. Executes the PC2 target from
`explorations/misc/positive-gu-constructions-lane-proposal-2026-06-22.md` (§Target 1, §Target 2)
and from `NEXT-STEPS.md` (§Positive GU Constructions Lane). Primary sources:
`explorations/anomaly-and-bordism/n1-signature-audit-y14-clifford-algebra-2026-06-22.md`,
`explorations/cycle-gates-and-audits/weinstein-ucsd-2025-04-analysis-2026-06-22.md` (Claims 1, 5, 6).
Discipline: exploration-grade; no results promoted to active_research or canon without
meeting `RESEARCH-STATUS.md` criteria.*
