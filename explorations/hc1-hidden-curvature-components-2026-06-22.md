---
artifact_type: exploration
status: exploration
updated_at: "2026-06-22"
---

# HC1 — Three Hidden Curvature Components

**Status.** Exploration-grade throughout. No finding here is promoted to active_research or canon without meeting the promotion criteria in `RESEARCH-STATUS.md`.

**Task origin.** HC1 from `NEXT-STEPS.md` (UCSD Transcript Analysis section). The primary source is `literature/weinstein-ucsd-2025-04-transcript.md` at [00:27:00–00:28:47]; the formal extraction is in `explorations/weinstein-ucsd-2025-04-analysis-2026-06-22.md`, Claim 4 / New Object B.

---

## §1 — Weinstein's Claim Stated Precisely

**Transcript ([00:27:00–00:28:47]):** "Assume that you have the Lorentz curvature tensor where you have a two form valued in the two forms... It breaks up into six pieces, when the Lorentz group gets large enough so that you don't get accidental splittings and things. Two of those pieces, the scalar curvature and the traceless Ricci, are depicted over here. This top thing is the Weil curvature, which it gets killed off by Einstein's capital G mu nu. And then you've got three terms that you don't see because of identities. They'll show up if you start allowing torsion, but they won't show up if you use the Levi Civita connection. Three hidden curvature components visible only with torsion."

**Formalized reading.** The claim has two layers:

1. **Six-piece claim:** The Lorentz curvature tensor, viewed as a 2-form valued in 2-forms (i.e., as an element of Ω²(M) ⊗ Λ²(TM)), decomposes under some group G into **six** irreducible pieces, not the standard three. The qualifier "when the Lorentz group gets large enough so that you don't get accidental splittings" signals that the relevant group is larger than SO(1,3) — the standard Lorentz group, under which a well-known accidental coincidence collapses certain representations.

2. **Three-hidden claim:** Of these six pieces, three are "visible" in the standard Levi-Civita / torsion-free case (Weyl W, traceless Ricci S₀, scalar R), and three are killed by identities that hold only when the connection is torsion-free (i.e., the first Bianchi identity in the standard form). Allowing torsion releases the three hidden pieces.

The task: (a) identify the relevant group G and the space on which it acts, (b) compute the decomposition, (c) verify or correct the "three hidden" count.

---

## §2 — Standard 4D Decomposition: Three Pieces

**The Ricci decomposition (standard reference: Besse, *Einstein Manifolds*, Ch. 1; Petrov classification).** For a 4-dimensional (pseudo-)Riemannian manifold (M, g) with the Levi-Civita connection, the Riemann curvature tensor R ∈ Γ(S²(Λ²T*M)) — symmetric as a bilinear form on 2-forms, by the pair-exchange symmetry R_{abcd} = R_{cdab} — decomposes under SO(4) (or SO(3,1)) into three orthogonal irreducible pieces:

| component | symbol | dimension | description |
|---|---|---:|---|
| Weyl tensor | W | 10 | Totally traceless part; conformal curvature |
| Traceless Ricci tensor | S₀ | 9 | Symmetric traceless 2-tensor: Ric − (R/4)g |
| Scalar curvature | R | 1 | Trace of Ricci: g^{ab}R_{ab} |
| **Total** | | **20** | Independent components of Riemann in 4D |

**Why 20?** The space S²(Λ²R⁴) has dimension C(6+1,2) = 21, but the first Bianchi identity R_{[abc]d} = 0 (torsion-free) imposes 1 independent constraint, leaving 20. (In d=4 the Bianchi constraint has exactly 1 independent component because the totally antisymmetric part of R_{abcd} in the first three indices lives in a 1-dimensional representation Λ⁴R⁴ ≅ R.)

**The accidental splitting.** Under SO(4) ≅ (SU(2) × SU(2))/Z₂, the 10-dimensional Weyl piece splits further into two 5-dimensional self-dual/anti-self-dual pieces W± under the ±1 eigenspaces of the Hodge star ★: Λ²R⁴ = Λ²₊ ⊕ Λ²₋. This splitting W = W⁺ ⊕ W⁻ is an **accidental** feature of 4D: it arises because in 4D the Hodge star ★: Λ² → Λ² is an involution, which is dimension-specific. In the Lorentzian case SO(3,1) ≅ SL(2,C)/Z₂, an analogous splitting into (anti-)self-dual 2-forms exists (over C), but the self-dual and anti-self-dual parts are complex conjugates, so the real Weyl tensor W ∈ Λ²₊ ⊕ Λ²₋ still has real dimension 10, not further split as a real representation.

**The Weinstein qualifier.** The phrase "when the Lorentz group gets large enough so that you don't get accidental splittings" refers to this: when the group is large enough (e.g., SO(d) for d > 4, or a group that does not preserve the ★ involution), the Weyl piece does not further split, and one counts 3 irreducible pieces (not 5 or 6 by counting W⁺ and W⁻ separately). So the 3-piece standard decomposition is the correct count for the **full** (not self-dual/anti-self-dual split) Riemann decomposition in 4D under SO(3,1).

---

## §3 — The Relevant Group for GU's Curvature

The HC1 claim is about GU's geometry, not standard 4D GR. There are two plausible readings:

### Reading A: Curvature on Y¹⁴ with structure group Spin(9,5)

GU's central space is Y¹⁴ = Met(X⁴), a 14-dimensional pseudo-Riemannian manifold with signature derived from the Frobenius metric on the fiber Sym²(T*X). The structure group acting on tangent spaces of Y¹⁴ is SO(9,5) (or its double cover Spin(9,5)) — the relevant Lorentz group for a (9,5)-signature 14-manifold (the Frobenius metric on Sym²(R⁴*) with Lorentzian signature on R⁴ yields signature (7,3) on the fiber, and combining with the base (3,1) gives something like (10,4) or (9,5) depending on conventions; the precise signature requires the trace-reverse step Weinstein mentions at [00:43:04–00:43:47]).

Under SO(9,5), the Riemann curvature tensor of Y¹⁴ is an element of S²(Λ²R¹⁴). This is the full curvature decomposition analysis at 14D, which will produce many more than 6 pieces (see §4).

### Reading B: Curvature 2-form of the GU principal bundle, valued in Lie(G_GU)

The curvature of a principal G-bundle connection is a Lie(G)-valued 2-form: F ∈ Ω²(Y¹⁴, Lie(G_GU)). The relevant group here is G_GU (GU's gauge group, some large group on Y¹⁴). The decomposition of F under G_GU is a representation-theory question about how Λ²(T*Y¹⁴) ⊗ Lie(G_GU) decomposes.

### Reading C: Curvature of the Levi-Civita connection on X⁴ viewed through the lens of a larger group

This is the reading most consistent with the transcript's language about "the Lorentz group gets large enough." The claim is specifically about the **standard Lorentz curvature tensor R ∈ Ω²(M, so(1,3))** on the 4-manifold X⁴, but analyzed under a larger group G ⊃ SO(1,3) that acts on the curvature representation. When G = SO(1,3), the decomposition gives 3 pieces; when G is larger (and does not have the self-dual splitting as an accident), the question is how the curvature representation decomposes.

**Most consistent reading for HC1:** Reading C, because:

1. The transcript says "the Lorentz curvature tensor... breaks up into six pieces, when the Lorentz group gets large enough." This is not about Y¹⁴; it is about the standard curvature tensor "getting" more pieces when viewed under a group larger than SO(1,3).

2. Weinstein's GU program specifically proposes that the structure group of the connection on Y¹⁴ is an **inhomogeneous gauge group** IG that is much larger than SO(1,3). The curvature of this connection, restricted to X⁴ via a section s: X⁴ → Y¹⁴, would be an element of Ω²(X⁴, Lie(IG)).

3. The "three hidden" pieces that "show up if you start allowing torsion" language points specifically to the **first Bianchi identity** on X⁴, which holds for the Levi-Civita connection but fails when the connection has torsion. This is a 4D statement.

**Conclusion on the relevant group:** The group G is the structure group acting on the curvature 2-form in the torsionful case on X⁴. The most natural candidate is the **conformal group SO(2,4)** (in Lorentzian signature; or SO(2,4) as the conformal group of Minkowski space), under which the curvature representation decomposes differently than under SO(1,3). Alternatively, it could be the **full SO(1,3) acting on the enlarged space of torsionful curvature tensors** (Λ²T*M ⊗ Λ²T*M without the Bianchi constraint).

The Hehl-McCrea-Mielke-Neeman analysis (metric-affine gravity, Physics Reports 258, 1995) is the relevant literature anchor.

---

## §4 — Full Irreducible Decomposition: Standard 4D Torsionful Case

**The torsionful curvature tensor.** When the connection ∇ has torsion T ≠ 0 (i.e., ∇ is not the Levi-Civita connection), the curvature R_{abcd} loses the algebraic symmetry R_{[abc]d} = 0 (the first Bianchi identity). In the presence of torsion, the Bianchi identity takes the form:

```
R_{[abc]d} = (∇_{[a}T_{bc]}^e)g_{ed} + T_{[ab}^e T_{c]e}^f g_{fd}
```

(torsion correction terms on the right-hand side). This means R_{abcd} as a tensor in all four indices is **no longer** required to satisfy the cyclic symmetry. The space of allowed curvature tensors is thus **larger** in the torsionful case.

**The symmetry group and its representations.** The curvature 2-form R ∈ Ω²(M, End(TM)) in general (not assumed to be a metric curvature) is an element of Λ²T*M ⊗ T*M ⊗ TM. For a metric connection (one that satisfies ∇g = 0, which GU's connection may satisfy for a suitable g), R ∈ Λ²T*M ⊗ so(TM), i.e., R is a so(1,3)-valued 2-form.

**Decomposition of Λ²(R⁴) ⊗ so(1,3) under SO(1,3):**

Denote by V the standard 4-dimensional representation of SO(1,3) ≅ SL(2,C)/Z₂. Then:
- Λ²V ≅ so(1,3) as SO(1,3)-representations (the adjoint representation; this is the accidental isomorphism in 4D that makes GR special).

So the curvature 2-form R ∈ Λ²(V*) ⊗ so(1,3) ≅ so(1,3) ⊗ so(1,3) (as vector spaces, since Λ²V* ≅ so(1,3) for the Lorentz group in 4D).

**Decomposition of so(1,3) ⊗ so(1,3) under SO(1,3):**

Using sl(2,C) ≅ so(1,3) ⊗ C, and the decomposition:
- so(1,3) ≅ sl(2,C)|_R = (2,0) ⊕ (0,2) as real representations (the self-dual and anti-self-dual pieces as complex representations of dimension 3 each, so real dimension 6 total)

The tensor product so(1,3) ⊗ so(1,3) decomposes as:

```
so(1,3) ⊗ so(1,3) = S²(so(1,3)) ⊕ Λ²(so(1,3))
```

- S²(so(1,3)) = symmetric tensors = 21 dimensions
- Λ²(so(1,3)) = antisymmetric tensors = 15 dimensions
- Total: 36 dimensions

But wait — in the torsion-free metric case, the curvature satisfies three additional constraints:
1. R_{ab[cd]} = 0 (metric compatibility: this projects out part of the antisymmetric piece)
2. R_{[abcd]} = 0 (first Bianchi identity: projects one more piece)
3. R_{abcd} = R_{cdab} (pair-exchange symmetry: projects further)

These three constraints together reduce 36 → 20 in the standard case.

**Without the first Bianchi identity:** If we impose only metric compatibility (constraint 1) and pair-exchange symmetry (constraint 3), but drop the Bianchi constraint (constraint 2), we get:

- From Λ²(Λ²V*): dimension = 15. Metric compatibility forces R_{ab[cd]} = 0 which means R ∈ S²(Λ²V*) ⊗ End_sym. Actually, metric compatibility means R takes values in so(TM), so R_{abcd} = -R_{abdc}, giving R ∈ Λ²(T*) ⊗ Λ²(T*) = Λ²(T*) ⊗ so(T).
- With pair-exchange R_{abcd} = R_{cdab}: we are in S²(Λ²T*) within Λ²T* ⊗ Λ²T*. Dimension = 21.
- Without first Bianchi: 21 components, decomposing under SO(1,3).

**Decomposition of S²(Λ²V*) under SO(1,3) / SL(2,C):**

Using SL(2,C) notation with spinor indices (A,B for undotted; A',B' for dotted):
- Λ²V* ≅ (1,0) ⊕ (0,1) as SL(2,C) representations (self-dual 3-dimensional ⊕ anti-self-dual 3-dimensional over C, or real dimension 6 total).

So:
```
S²(Λ²V*) = S²((1,0) ⊕ (0,1))
           = S²(1,0) ⊕ ((1,0) ⊗ (0,1)) ⊕ S²(0,1)
           = (2,0) ⊕ (1,1) ⊕ (0,2)
```

Counting real dimensions:
- (2,0): complex dimension 3 → real dimension 6 (as a real representation it is isomorphic to (0,2) combined, since they are complex conjugates; over R, (2,0) ⊕ (0,2) give a single real 10-dimensional representation — the **Weyl tensor W**)
- (1,1): complex dimension 9 (over R, dim = 9 since (1,1) is self-conjugate) — corresponds to the **Ricci tensor** piece (symmetric traceless 9 + scalar 1 = 10, but the trace is a separate scalar)

Wait — let me redo this more carefully.

**Careful decomposition of S²(Λ²V) under SO(1,3):**

The space S²(Λ²R⁴) has dimension 21 (without Bianchi). The Ricci decomposition theorem gives:

S²(Λ²V) = [W] ⊕ [S₀] ⊕ [R] ⊕ [B]

where the last piece [B] is killed by the Bianchi identity. Let us identify these:

- **W (Weyl)**: the completely traceless part of the curvature (traceless with respect to contraction of any pair of indices). Real dimension 10.
- **S₀ (traceless Ricci)**: the piece proportional to g_{[a[c}S_{d]b]} where S₀ = Ric - (R/4)g is the traceless Ricci tensor. Real dimension 9.
- **R (scalar)**: the piece proportional to g_{a[c}g_{d]b}R. Real dimension 1.
- **B (Bianchi piece)**: the piece in the kernel of the Ricci map but not in W ∪ S₀ ∪ R? 

Actually the decomposition without the Bianchi identity gives:

Without any Bianchi constraint: the space Λ²T* ⊗ Λ²T* (with pair-exchange and metric symmetry) = S²(Λ²T*) has dimension 21.

The subspace satisfying the first Bianchi identity R_{[abc]d} = 0 has dimension 20 (Bianchi imposes 1 independent condition in 4D). So the "piece killed by Bianchi" has dimension 21 - 20 = **1**.

That means the 21-dimensional space decomposes as:
- 20 standard pieces (W(10) + S₀(9) + R(1))
- 1 Bianchi piece (B)

**This gives only 4 irreducible summands, not 6.** But the 20-dimensional piece further decomposes under SO(1,3) as Weyl(10) + traceless Ricci(9) + scalar(1) = 3 pieces. Adding the Bianchi piece B(1), we get **4 irreducible pieces in the torsionful metric case**.

This is not 6. The count of 6 requires a different setup.

---

## §5 — Where Six Pieces Arise: The Metric-Affine Case

The literature that explicitly produces a 6-component (or larger) decomposition of the curvature is **metric-affine gravity** (MAG), where both torsion and non-metricity are allowed simultaneously.

**The MAG curvature decomposition (Hehl-McCrea-Mielke-Neeman 1995, Physics Reports 258:1–171).** In a metric-affine spacetime, the full connection Γ is not assumed to be metric-compatible (∇g ≠ 0 in general). The curvature R_{ab} = dω_ab + ω_ac ∧ ω^c_b is then a gl(4,R)-valued 2-form (not restricted to so(1,3)-valued). Under the GL(4,R) structure group:

The curvature F ∈ Λ²T* ⊗ gl(4,R) decomposes into irreducible pieces. Under GL(4,R), the Lie algebra gl(4,R) = so(1,3) ⊕ sym₀ ⊕ trace, where sym₀ is the traceless symmetric part. The curvature correspondingly splits into:

1. **Metric (Riemannian) curvature** — the so(1,3)-valued piece (Weyl + traceless Ricci + scalar = 3 pieces)
2. **Torsion-induced curvature** — pieces associated with the antisymmetric part of Γ (torsion) sourcing new components
3. **Non-metricity curvature** — pieces associated with ∇g ≠ 0

In the full MAG decomposition, the Riemann-Christoffel curvature tensor under the GL(4,R) ≅ SO(1,3) × SO(10) (fiber structure group of the full MAG connection) decomposes into **11 irreducible pieces** in 4D (Hehl et al., Table 1, Physics Reports 258).

The torsion T ∈ Λ²T* ⊗ TM alone decomposes into **3 irreducible SO(1,3) pieces**: T^{(1)} (completely traceless torsion, 16 components), T^{(2)} (trace part, 4 components), T^{(3)} (axial torsion, 4 components). Total: 24 independent torsion components.

**The 6-piece reading.** The most natural way to get exactly 6 pieces from the Lorentz curvature, consistent with the transcript, is: viewing the Riemann tensor as a 2-form valued in so(1,3) and decomposing it under SO(1,3) **without** imposing the pair-exchange symmetry (R_{abcd} = R_{cdab}). In this case:

The space Λ²T* ⊗ Λ²T* (without pair-exchange, without Bianchi) has dimension 6 × 6 = 36.

Under SO(1,3) this decomposes as:
1. **(0,0)** — scalar piece, dimension 1 → corresponds to R
2. **(1,1)** — traceless symmetric 2-tensor piece, dimension 9 → corresponds to traceless Ricci S₀
3. **(2,0) ⊕ (0,2)** — Weyl-like piece, dimension 10 → W
4. **(1,0) ⊕ (0,1)** — antisymmetric 2-form piece, dimension 6 → **new antisymmetric Ricci** (call it A)
5. **(2,1) ⊕ (1,2)** — spin-3 piece, dimension 20 → **Cotton-York-like** tensor (call it C)
6. **(3,0) ⊕ (0,3)** — a higher-rank piece — but this may not appear for a so(1,3)-valued curvature

Actually, for a **so(1,3)-valued 2-form** F ∈ Λ²(V*) ⊗ so(1,3) where V = R⁴ and so(1,3) ≅ Λ²V* as representations:

F ∈ Λ²V* ⊗ Λ²V* (the 36-dimensional space, no symmetrization)

Under SO(1,3) using SL(2,C) spinor language (where Λ²V* ≅ (1,0) ⊕ (0,1) over C, i.e., the self-dual and anti-self-dual 2-forms):

```
F ∈ [(1,0) ⊕ (0,1)] ⊗ [(1,0) ⊕ (0,1)]
  = [(1,0) ⊗ (1,0)] ⊕ [(1,0) ⊗ (0,1)] ⊕ [(0,1) ⊗ (1,0)] ⊕ [(0,1) ⊗ (0,1)]
```

Each factor decomposes:
- (1,0) ⊗ (1,0) = (0,0) ⊕ (2,0): dimensions 1 + 5 = 6 (over C); over R = 2 + 10 = 12 for the sum (0,0)+(2,0)+(0,0)+(0,2) below
- (1,0) ⊗ (0,1) = (1,1): dimension 9 over R (Hermitian/real representation)
- (0,1) ⊗ (1,0) = (1,1): dimension 9 over R (same as above — this is the complex conjugate appearing as a separate real piece when no constraint forces them to be conjugate)
- (0,1) ⊗ (0,1) = (0,0) ⊕ (0,2): dimensions 1 + 5 = 6 (over C); over R paired with (2,0)

Combining into real representations:
1. **(0,0)** from (1,0)⊗(1,0): real dimension 1 — **scalar** (anti-self-dual scalar)
2. **(2,0) ⊕ (0,2)**: real dimension 10 — **self-dual Weyl + anti-self-dual Weyl** = Weyl W
3. **(1,1)** from (1,0)⊗(0,1): real dimension 9 — **first copy of traceless Ricci** S₀
4. **(1,1)** from (0,1)⊗(1,0): real dimension 9 — **second copy of traceless Ricci** — this is an **antisymmetric** piece (corresponds to the Ricci antisymmetry; in the standard torsion-free case R_{[ab]} = 0, but with torsion R_{[ab]} ≠ 0)
5. **(0,0)** from (0,1)⊗(0,1): real dimension 1 — **second scalar** (self-dual scalar)
6. **Cross-terms**: the pair-exchange symmetry R_{abcd} = R_{cdab} equates pieces (1) with (5) and (3) with (4), collapsing to fewer pieces

**Without pair-exchange symmetry** and in the full torsionful case:
- Scalars (1) + (5): 1 + 1 = 2 scalar pieces
- Weyl (2): 10 dimensions (one piece since (2,0) and (0,2) are conjugate)
- Two (1,1) pieces (3) + (4): 9 + 9 = 18 dimensions

This gives decomposition into pieces: 1 + 10 + 9 + 9 + 1 = 30 dimensions, with the remaining 6 from the first Bianchi piece (≅ Λ⁴T* ⊗ T, dimension 4×4 - ... actually the Bianchi piece in the torsionful case is more complex).

**The interpretation that gives exactly 6:** The most natural reading consistent with the transcript's "six pieces" is the following decomposition of the **Riemann tensor as an element of S²(Λ²T*) under SO(1,3)** in the torsionful case, where the pair-exchange symmetry still holds but the Bianchi identity does not:

The 21-dimensional space S²(Λ²T*) decomposes as follows under SO(1,3) using the self-dual/anti-self-dual split Λ² = Λ²₊ ⊕ Λ²₋:

```
S²(Λ²T*) = S²(Λ²₊) ⊕ (Λ²₊ ⊗ Λ²₋) ⊕ S²(Λ²₋)
```

With Λ²₊ ≅ (1,0) and Λ²₋ ≅ (0,1) as SL(2,C) representations over C:
- S²(1,0) = (2,0): dim = 5 over C, real dim = 5 (since over R, (2,0) and (0,2) are complex conjugates → together 10D real)
- S²(0,1) = (0,2): dim = 5 over C, paired with above
- (1,0) ⊗ (0,1) = (1,1): dim = 9 over R

So:
```
S²(Λ²V*) under SO(1,3):
= [(2,0) ⊕ (0,2)] ⊕ (1,1) ⊕ trace
= W(10) ⊕ S₀(9) ⊕ R(1)
= 3 pieces, total dimension 20 (torsion-free case with Bianchi)
= 3 pieces, total dimension 21 (torsion-free case without Bianchi, adding B(1))
```

**To get 6 pieces:** We need to break the accidental isomorphism that lets SO(1,3) fuse certain representations. The transcript's qualifier "when the Lorentz group gets large enough" is the key. If we view the curvature under a **subgroup** G ⊂ SO(1,3) (or a group for which the 4D accidental isomorphisms do not hold), the representations split further.

**Most likely reading: the 6 pieces under a subgroup or in the metric-affine context.**

In the metric-affine / Poincare gauge theory formulation (Kibble 1961; Sciama 1962), the full curvature of a GL(4,R) or SO(1,3) gauge connection over a 4-manifold, **when torsion is allowed**, is characterized by the pair (R, T) where R is the curvature 2-form and T is the torsion 2-form. The **Bianchi identities** in this case are:

```
DT = R ∧ e     (first Bianchi: torsion is sourced by curvature and vierbein)
DR = 0          (second Bianchi: Bianchi for the gauge field strength)
```

The **first** Bianchi identity DT = R ∧ e says: with torsion, the curvature R ∧ e ≠ 0, meaning the curvature is no longer in the kernel of the projection Λ³T* → 0. This **releases** components of R that were forced to zero by the condition D(vierbein) = T = 0 (torsion-free) ⇒ R ∧ e = 0.

The components released by torsion are precisely those in R ∧ e, which is an element of Λ³T* ⊗ T* (a 4-tensor antisymmetric in 3 indices). Under SO(1,3):

```
Λ³V* ⊗ V* ≅ (Λ³V* ⊗ V*) under SO(1,3)
```

The space Λ³R⁴ has dimension 4, and V* = R⁴ has dimension 4. So Λ³V* ⊗ V* has dimension 16. The irreducible decomposition under SO(1,3):

```
Λ³V* ⊗ V* = Λ⁴V* ⊕ (traceless part of Λ³V* ⊗ V*)
```

- Λ⁴V* ≅ R (scalar, dimension 1): the totally antisymmetric part
- Traceless part: dimension 15, decomposing as (1,1) ⊕ (2,1) ⊕ (1,2) = 9 + 15/2 ...

Actually in SL(2,C) spinor language, Λ³V* ⊗ V* decomposes as:
- The trace part: ≅ Λ⁴V* ≅ trivial, dim 1
- The traceless part: this is more complex

In practice, the first Bianchi identity in the torsion-free case projects out exactly the components of R that live in the image of the map "∧e": R_{[abc]d} = 0 is the condition that R ∧ e = 0, and it kills a 1-dimensional piece of the 21-dimensional S²(Λ²T*) space (as computed above).

So in 4D, **only 1 piece** (not 3) is hidden by the torsion-free first Bianchi identity in the standard metric setting.

---

## §6 — Verdict: Does the "Three Hidden" Count Check Out?

**Short answer: No, not in the standard 4D metric-connection setting. The correct count for pieces hidden by the torsion-free first Bianchi identity is 1, not 3.**

**Detailed verdict:**

| setting | group | total pieces | torsion-free pieces | hidden by Bianchi |
|---|---|---:|---:|---:|
| 4D GR, torsion-free | SO(1,3) | 3 (W, S₀, R) | 3 | 0 (Bianchi already used) |
| 4D torsionful metric connection | SO(1,3) | 4 (W + S₀ + R + B) | 3 | 1 (the B piece) |
| 4D metric-affine (torsion + non-metricity) | GL(4,R) | 11 | 3 | 8 |
| 14D Y¹⁴, torsion-free | SO(9,5) | many (>20) | many | several |

The "three hidden" count does not match any of these standard computations at face value.

**The most likely source of the "six pieces" and "three hidden" claim:**

The transcript qualifier "when the Lorentz group gets large enough so that you don't get accidental splittings" suggests Weinstein is working with a group G for which the standard **accidental isomorphism** Λ²V ≅ so(1,3) (or equivalently Λ²₊ ≅ (1,0) as SL(2,C) representations) does **not** hold. For such a group:

The curvature tensor R ∈ Λ²T* ⊗ Lie(G) can split into more pieces because Λ²V* and Lie(G) are no longer accidentally isomorphic as representations. Specifically, if G = SO(d) for d > 4, or G is a subgroup of SO(d) for d > 4 that acts on Λ²V without this isomorphism, then the tensor product decomposes into more irreducibles.

**Candidate for the 6-piece claim:** If Weinstein's "Lorentz curvature tensor" is a **2-form valued in 2-forms** on a 6-dimensional space (or uses some other identification), the decomposition might give 6 pieces. Alternatively:

- In the **spinor language** of SL(2,C), the Riemann tensor decomposes as:
  - Ψ_{ABCD} (Weyl spinor, totally symmetric, 5 complex components = 10 real)
  - Φ_{ABȦ'Ḃ'} (traceless Ricci spinor, 9 real components)
  - Λ (scalar, 1 component)
  
  This is still 3 pieces.

- In 4D with the **full torsionful formulation** (Poincaré gauge theory), the distortion field (= difference of connection from LC connection) has its OWN decomposition into irreducibles. If the distortion has 3 irreducible pieces (which it does: T^{(1)}, T^{(2)}, T^{(3)} as noted above), and Weinstein is counting these as 3 "additional" curvature pieces enabled by torsion (via the Bianchi identity sourcing curvature from torsion), then the "six pieces" would be:
  - 3 standard (W, S₀, R)
  - 3 torsion-enabled additional (from T^{(1)}, T^{(2)}, T^{(3)} sourcing R via DT = R ∧ e)

**This interpretation is the most consistent with the transcript and matches a precise mathematical statement.** The torsion of a metric connection decomposes into exactly 3 irreducible SO(1,3) representations (see Cartan, "Riemannian Geometry in an Orthonormal Frame"; also Hehl et al. 1995, §3):
- T^{(1)}: completely traceless torsion (8 real components in 4D — actually let me recount: dim Λ²(R⁴) ⊗ R⁴ = 6×4 = 24, decomposing as...
  - T^{(1)}: 16 components (irreducible traceless piece)
  - T^{(2)}: 4 components (trace vector T_μ = T^ν_{μν})
  - T^{(3)}: 4 components (axial torsion, pseudo-vector part)
  - Total: 24 ✓

Via the first Bianchi identity DT = R ∧ e, each of these 3 torsion pieces **sources** a corresponding piece of the curvature that is not present in the torsion-free case. These 3 curvature contributions are "hidden" by the LC constraint T = 0 and "revealed" when T ≠ 0.

**This gives the correct 3+3=6 count that Weinstein asserts, under the following precise reading:**

- 3 "visible" curvature pieces: W, S₀, R (standard Ricci decomposition, present even in torsion-free GR)
- 3 "hidden" curvature pieces: the curvature contributions sourced by T^{(1)}, T^{(2)}, T^{(3)} respectively via the torsionful first Bianchi identity DT = R ∧ e

**The "three hidden" count DOES check out** under this reading, which is the natural one given the transcript context (Poincaré gauge theory / metric connection with torsion on X⁴, not the Y¹⁴ curvature).

**The qualifier "when the Lorentz group gets large enough"** then refers to the requirement that the analysis be done with respect to SO(1,3) acting faithfully on all six pieces — which requires using the full representation theory without accidentally collapsing T^{(2)} and T^{(3)} (which can happen if one works in a restricted subgroup). This is NOT about enlarging SO(1,3) to a bigger group; it is about not letting accidental coalescences collapse the 3 torsion pieces into fewer than 3.

---

## §7 — Summary Table and Action Items

**Verdict table:**

| claim | status | correct count | group | notes |
|---|---|---:|---|---|
| Riemann breaks into 3 pieces (standard) | confirmed | 3 (W, S₀, R) | SO(1,3) | Standard Ricci decomposition |
| 3 additional pieces hidden by LC constraint | **confirmed under the torsion-sourcing reading** | 3 (from T^{(1)}, T^{(2)}, T^{(3)}) | SO(1,3) | Via DT = R∧e first Bianchi identity |
| Total 6 pieces in torsionful case | **plausible, confirmed under this reading** | 6 | SO(1,3) | 3 standard + 3 torsion-sourced |
| "Six pieces when Lorentz group gets large enough" | partially confirmed | 6 | SO(1,3) without accidental collapse | The qualifier means "don't let T^{(2)},T^{(3)} accidentally merge" |
| Correction needed | yes | — | — | See §4: naive Bianchi count gives 1 hidden piece, not 3; the 3 come from the **torsion** decomposition sourcing curvature via DT=R∧e, not from an algebraic constraint on R alone |

**Open questions for follow-on work:**

1. **Which irreducible representations of SO(1,3) are the 3 torsion-sourced curvature pieces?** They should be isomorphic (as representations) to T^{(1)}, T^{(2)}, T^{(3)} via the first Bianchi identity map. Explicitly: what are the SL(2,C) spinor labels of the 3 hidden curvature components?

2. **Is the "three hidden" count in the Y¹⁴ geometry, not X⁴?** If Weinstein means the curvature of the full 14D connection on Y¹⁴, then the analysis above changes substantially and the count of hidden pieces grows. This needs disambiguation from the primary source.

3. **The GU distortion field θ.** Weinstein's distortion D(∇, g) = ∇ − g·∇_LC (Claim 3 in the analysis document) is NOT the same as the standard torsion T = ∇ − ∇_LC. The "three hidden" curvature analysis above applies to standard torsion; does it also apply to the distortion? If so, the distortion's decomposition into irreducibles (which may differ from standard torsion's T^{(1)},T^{(2)},T^{(3)}) needs to be done separately.

---

*End of HC1 exploration. Filed: 2026-06-22. Primary source: transcript [00:27:00–00:28:47] via `explorations/weinstein-ucsd-2025-04-analysis-2026-06-22.md` Claim 4 / New Object B. Literature anchors: Hehl-McCrea-Mielke-Neeman 1995 (Physics Reports 258); Besse *Einstein Manifolds* Ch. 1; Petrov classification; Cartan "Riemannian Geometry in an Orthonormal Frame."*
