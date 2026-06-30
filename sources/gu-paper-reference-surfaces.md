---
title: "GU Paper Reference Surfaces"
status: source
doc_type: reference_surface
source_id: GU-MEDIA-2021-DRAFT-RELEASE
updated_at: "2026-06-19"
---

# GU Paper Reference Surfaces

Extracted from the GU paper (2021 draft release) to support formalization candidates in `docs/paper-formalization-candidates.md`. These tables are reconstructed from the paper text (§12); treat as reconstruction-strength, not verified.

---

## 1. SR/QFT → GU Analogy Table (§12.8, Table 12.11)

The paper's §12.8 draws a structural analogy between the kinematic data of Special Relativity / QFT and the corresponding GU objects. This table is the key cross-map for understanding GU's inhomogeneous-gauge-group construction.

| SR / QFT concept | GU analog | GU object name | Notes |
| --- | --- | --- | --- |
| Minkowski spacetime M^{1,3} | Affine space of connections | A = A(Y, P_H) | Connections on the principal bundle P_H → Y play the role of "spacetime" |
| Flat Minkowski ℝ^{1,3} | Lie algebra / 1-forms | N = Ω¹(Y, ad(P_H)) | Tangent-space analog; the "translation" part of the inhomogeneous group |
| Lorentz group Spin(1,3) | Gauge group | H = Gau(P_H) | Acts on connections as Lorentz acts on frames |
| Poincaré group Spin(1,3) ⋉ ℝ^{1,3} | Inhomogeneous gauge group | G = H ⋉ N | Central construction: G acts on A by (ε, ω) · A = ε · A + ω |
| Inertial frame / gauge choice | Distinguished connection | A₀ (from Zorro construction) | A₀ is GU's "rest frame"; the tilted homomorphism τ_{A₀}: H → G depends on it |
| Lorentz transformations | Gauge transformations in H | H ⊂ G (via τ_{A₀}) | Acts on A preserving A₀ |
| Translations | Connections shifts | N ≅ A (as H-space) | N is both Lie algebra and affine-connection space |
| 4-velocity / position | Connection g = (ε, ω) ∈ G | Element of G = H ⋉ N | One group element maps to two connections via bi-connection map |
| Velocity = derivative of position | Augmented torsion T_g | T_g = ω − ε⁻¹(d_{A₀}ε) | Measures "displacement" between the two connections; gauge-covariant under H_{τ_{A₀}} |

**Formalization candidate.** `docs/paper-formalization-candidates.md` item **8B**. Import this table as a verification target: confirm that G = H ⋉ N with the group law (ε₁,ω₁)·(ε₂,ω₂) = (ε₁ε₂, Ad(ε₂⁻¹)ω₁ + ω₂) recovers the Poincaré group law exactly when H = Spin(1,3) and N = ℝ^{1,3}.

**Strength.** Reconstruction. The analogy is explicit in §12.8 of the paper; the table above is a structured rendering of that text.

---

## 2. GU Construction Location Table (§12 summary)

Where each major GU construction appears in the paper and its role in the overall framework. Useful for mapping formalization candidates to source sections.

| GU construction | Primary section | Brief role |
| --- | --- | --- |
| Observerse (X^n, Y^d, {ι}) — three cases | §2, §3 | Foundation: universe X, metric space Y, observer embeddings |
| Native/invasive field semantic (Hebrew/Greek) | §4 | Notational convention: ג, ℵ for X-native; Greek for Y-native; invasive = ι*(χ) |
| Chimeric bundle C(Y) = V ⊕ H* | §5 | Signature (4,6) for n=4; semi-canonically isomorphic to TY |
| Zorro construction (metric → connection chain) | §6 | ג on X → ℵ on TX → g_ℵ on TY → A₀ on Y; gives distinguished connection |
| Inhomogeneous gauge group G = H ⋉ N | §7 | Group law; tilted homomorphism τ_{A₀}; G acts on A ≅ N |
| Bi-connection map μ_{A₀}: G → A × A | §7 | One group element → two connections; augmented torsion T_g = their difference |
| Shiab operators | §8 | Gauge-covariant contraction operators; Spin(7,7) invariant subspaces {Γᵢ}₀¹⁴ from Def. 8.1 |
| First-order Lagrangian I^B₁ | §8 | ⟨T_ω, ∗(⊢_ω(F_{B_ω}+...))⟩_g; field equation: Swervature = Displasion |
| Second-order Lagrangian I^B₂ | §8 | ‖Υ_ω‖² (Yang-Mills-like) |
| Fermionic sector (four fields) | §9.3 | ψ, ψ̃ ∈ Ω⁰(Y,S/), φ, φ̃ ∈ Ω¹(Y,S/); block Dirac-like operator |
| Deformation complex | §10 | ∂₁: Ω⁰(ad)→Ω¹(ad)⊕Ω⁰(ad), ∂₂: →Ω^{d-1}(ad); ∂₂∘∂₁ = Υ_ω |
| Arrow of time | §12.2 | ℝ¹ uniquely naturally well-ordered; higher dimensions need extra structure |
| GU ↔ SR/QFT analogy | §12.8 | See table above; A↔M^{1,3}, N↔ℝ^{1,3}, H↔Spin(1,3), G↔Poincaré |
| Effective chirality | §12.9 | Globally non-chiral Dirac operator on Y; appears chiral in low-curvature regions via R(y) coupling |

**Formalization candidate.** `docs/paper-formalization-candidates.md` item **7B** (the location table itself as a formalization target for verifying section references and cross-dependencies).

**Strength.** Reconstruction. Section references are from the 2021 draft release; exact theorem/proposition numbers may differ in any published version.

---

## 3. Arrow of Time Claim (§12.2)

The paper's §12.2 contains the following argument:

- ℝ¹ is the unique 1-manifold that is *naturally* well-ordered (i.e., ordered without choosing additional structure).
- Higher-dimensional manifolds (ℝ^n for n ≥ 2) are not naturally well-ordered; imposing an order requires extra structure (a Cauchy foliation, a time function, etc.).
- GU uses this to ground the arrow of time in an algebraic property of ℝ¹ rather than in a physical postulate.

**Relevance to six-axis protocol.** This partially addresses the L4 (causal order) axis: GU's framework has a built-in causal-order argument from the structure of ℝ¹. Six-axis candidates derived from GU constructions should assess whether this ℝ¹ argument determines their L4 class or leaves it open.

**Formalization candidate.** `docs/paper-formalization-candidates.md` item **8A**.

**Strength.** Reconstruction. The claim is in §12.2 of the paper; formal proof of "ℝ¹ is the unique naturally well-ordered 1-manifold" is a theorem in ordered-field theory (ℝ is the unique complete ordered field; ℝ¹ as a manifold has a canonical orientation; the well-ordering claim is about the *canonical* choice being unique) and would require unpacking exactly what "natural" means in this context.
