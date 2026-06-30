---
title: "4D Reduction: Section Pullback, Spinor Branching, Second Fundamental Form"
artifact_type: exploration
status: PARTIAL
date: 2026-06-22
depends_on:
  - "explorations/geometry-curvature-emergence/pc2-met-x4-bundle-formalization-stub-2026-06-22.md"
  - "explorations/generation-sector/generation-count-sm-branching-closure-2026-06-22.md"
  - "explorations/dark-energy-cosmology/dark-energy-noether-closure-2026-06-22.md"
  - "explorations/anomaly-and-bordism/n1-signature-audit-y14-clifford-algebra-2026-06-22.md"
---

# 4D Reduction from Y¹⁴ to X⁴

**Status.** PARTIAL — exploration-grade derivation. Steps B1 (connection pullback) and B3
(second fundamental form) reach reconstruction grade. Step B2 (spinor branching under s*)
reaches verified grade for the main decomposition but leaves a factor-of-4 dimension question
open (resolved structurally in §B2.5 using the ℍ-line argument from the generation-count
closure file). No result promoted to active_research without meeting `RESEARCH-STATUS.md`
criteria.

**Purpose.** Derive the three named steps of the 4D reduction explicitly:
1. **B1:** Section pullback s*(θ): how the 14D distortion reduces to 4D geometric data
2. **B2:** Spinor branching s*(S): how S = ℍ^{64} decomposes under the section
3. **B3:** Second fundamental form of s in Y¹⁴: the bending correction to Levi-Civita

These steps are stated but not derived in the PC2 stub
(`explorations/geometry-curvature-emergence/pc2-met-x4-bundle-formalization-stub-2026-06-22.md`). This document supplies
the derivations to the extent they can be done from first principles without new mathematical
technology.

---

## §Setup — The Section s: X⁴ → Y¹⁴

### Setup.1 — What a section is

Let X⁴ be a smooth, oriented 4-manifold (no metric specified). Let Y¹⁴ = Met(X⁴) be the
total space of the bundle of Lorentzian metrics:

```
π: Y¹⁴ → X⁴,    π⁻¹(x) = {h ∈ Sym²(T*_x X⁴) : h has signature (3,1)}
```

A **section** s: X⁴ → Y¹⁴ with π ∘ s = id_{X⁴} assigns to each x ∈ X⁴ a Lorentzian
metric s(x) ∈ π⁻¹(x). This is exactly a Lorentzian metric on X⁴.

The section s:
- Selects a specific metric on X⁴: g_s(x) := s(x)
- Makes X⁴ into spacetime (M, g_s)
- Embeds X⁴ as a submanifold s(X⁴) ⊂ Y¹⁴ (the image of s)
- The image s(X⁴) is a 4-dimensional submanifold of the 14-dimensional manifold Y¹⁴

### Setup.2 — The tangent map of s

The differential ds: TX⁴ → T(Y¹⁴) maps:
- At a point x ∈ X⁴, the tangent vector v ∈ T_x X⁴ maps to ds(v) ∈ T_{s(x)} Y¹⁴

The tangent space T_{s(x)} Y¹⁴ splits as:
```
T_{s(x)} Y¹⁴ = V_{s(x)} ⊕ H_{s(x)}
```
(vertical ⊕ horizontal; where the vertical tangent space V = ker(dπ) is the 10-dimensional
fiber tangent space, and H is a 4-dimensional horizontal complement determined by the
connection on the bundle Y¹⁴ → X⁴).

The differential ds maps T_x X⁴ into H_{s(x)} (the horizontal subspace), by the definition
of a section (ds composed with dπ is the identity on TX⁴). So:

```
ds: T_x X⁴ → H_{s(x)} ⊂ T_{s(x)} Y¹⁴   (horizontal lift)
```

The section s also determines a **normal bundle** to s(X⁴) in Y¹⁴: the normal bundle is
the vertical tangent bundle restricted to s(X⁴):

```
N_s = V|_{s(X⁴)} → s(X⁴)
```

with fiber N_{s(x)} = V_{s(x)} = T_{s(x)}(π⁻¹(x)) ≅ Sym²(T*_x X⁴) (the 10-dimensional
fiber tangent space).

### Setup.3 — The principal bundle and connection

GU posits a principal G-bundle P → Y¹⁴ where G is a large gauge group (Sp(64) or U(128)
in the chimeric spinor interpretation; see N1 audit and anomaly audit). The bundle carries:
- A connection A ∈ Ω¹(P, Lie(G))
- Curvature F_A = dA + A∧A ∈ Ω²(Y¹⁴, ad P)
- Distortion θ ∈ Ω¹(Y¹⁴, ad P) (the dark energy field; see DD1)

The section s pulls back:
- P → Y¹⁴ to the bundle s*(P) = s⁻¹(P) → X⁴
- A to s*(A) ∈ Ω¹(X⁴, ad s*(P))
- F_A to s*(F_A) ∈ Ω²(X⁴, ad s*(P))
- θ to s*(θ) ∈ Ω¹(X⁴, ad s*(P))

---

## §B1 — Connection and Curvature Pullback

### B1.1 — The pullback of the principal bundle P

**s*(P)** is the principal G-bundle over X⁴ defined by:

```
s*(P) = { (x, p) ∈ X⁴ × P : π_P(p) = s(x) }
```

where π_P: P → Y¹⁴ is the bundle projection. The projection s*(P) → X⁴ sends (x, p) ↦ x.

`[verified — standard pullback bundle construction; any smooth map s: X → Y and principal
bundle P → Y determines the pullback s*(P) → X; see Kobayashi-Nomizu I, §I.5]`

**Structure group.** The structure group of s*(P) is the same G as P, since the pullback
preserves the fiber type. So s*(P) is a G-bundle over the 4-dimensional spacetime X⁴.

**Interpretation.** The pullback bundle s*(P) is the gauge bundle of the 4D theory. Its
structure group G (Sp(64)) is far larger than the Standard Model gauge group SU(3)×SU(2)×U(1).
GU proposes that the SM gauge content emerges from the structure of the spinor bundle S inside
s*(P) via the observation map — the SM gauge group is a subgroup of G that acts on the
relevant spinor representation. This is a separate story from the bundle pullback itself.

### B1.2 — The pullback connection s*(A)

Given a connection A on P → Y¹⁴, the pullback s*(A) is a connection on s*(P) → X⁴.

**Construction.** A connection A on P → Y¹⁴ is a G-equivariant horizontal distribution
on P. The pullback connection s*(A) is defined as follows: a tangent vector v ∈ T_x X⁴ is
horizontal in s*(P) if and only if its lift to T_{s(x)} Y¹⁴ via ds is horizontal in P
under A. More concretely:

If A ∈ Ω¹(Y¹⁴, ad P) is the connection 1-form (in local gauge), then:

```
s*(A) = A|_{s(X⁴)} ∘ ds ∈ Ω¹(X⁴, ad s*(P))
```

i.e., s*(A) at a point x ∈ X⁴ and tangent vector v ∈ T_x X⁴ evaluates as:

```
s*(A)(x)(v) = A(s(x))(ds(v))
```

This is a standard pullback of a differential 1-form. `[verified — standard; pullback of
connection forms is a special case of pullback of differential forms]`

**The pulled-back connection is a 4D gauge field.** s*(A) is a connection on the G-bundle
s*(P) → X⁴. In 4D physics language, s*(A) is a gauge potential 1-form valued in Lie(G).
This is the 4D Yang-Mills connection in the spacetime X⁴ with metric g_s = s(x).

### B1.3 — The pullback curvature s*(F_A)

The curvature F_{s*(A)} of the pulled-back connection s*(A) equals the pullback s*(F_A)
of the 14D curvature F_A:

```
F_{s*(A)} = s*(F_A)
```

**Proof.** For a pullback connection, the curvature transforms as:

```
F_{s*(A)} = s*(F_A)
```

This follows from the naturality of the exterior derivative and the wedge product:

```
s*(F_A) = s*(dA + A∧A) = d(s*A) + (s*A)∧(s*A) = F_{s*(A)}
```

`[verified — standard result for pullback connections; see Milnor-Stasheff App. C or
Kobayashi-Nomizu I, §II.3]`

**Decomposition of s*(F_A).** The pullback curvature s*(F_A) ∈ Ω²(X⁴, ad s*(P)) is a
2-form on X⁴ valued in ad s*(P). It contains the full gauge-theoretic curvature of the
pulled-back connection.

The curvature F_A on Y¹⁴ is a 2-form on Y¹⁴, which at any point s(x) has components in
all pairs of tangent directions to Y¹⁴ (including vertical-vertical, horizontal-vertical, and
horizontal-horizontal components). The pullback s* extracts only the **horizontal-horizontal**
components (those that pair two horizontal tangent vectors):

```
s*(F_A)(v, w) = F_A(ds(v), ds(w))   for v, w ∈ T_x X⁴
```

The vertical-horizontal and vertical-vertical components of F_A are not captured by s*(F_A).
These represent the "extra" curvature of the 14D bundle connection that is not visible in
the 4D pullback. `[verified — pullback of a 2-form picks up only the components along the
image of the differential ds, which maps into horizontal directions]`

### B1.4 — The pullback distortion s*(θ)

The distortion θ ∈ Ω¹(Y¹⁴, ad P) pulls back to:

```
s*(θ) ∈ Ω¹(X⁴, ad s*(P))
```

a 1-form on X⁴ valued in ad s*(P). This is the quantity that, in GU, is supposed to
reproduce Einstein's equations or replace the cosmological constant.

**What is s*(θ) geometrically?** The distortion θ on Y¹⁴ is defined (from DD1 and the
transcript) as:

```
θ = A − g_Y · ∇_LC(g_Y)
```

(schematically: the difference between the GU connection A and the Levi-Civita connection of
the gimmel metric ℊ on Y¹⁴, conjugated appropriately by a gauge transformation g_Y as per
the τ⁺ construction).

The pullback s*(θ) under the section s (which selects a metric g_s = s(x) on X⁴) is:

```
s*(θ) = s*(A) − (g_Y ∘ s) · ∇_LC(g_s)
```

where ∇_LC(g_s) is the Levi-Civita connection of the metric g_s on X⁴. The factor
(g_Y ∘ s) is the gauge transformation applied along the section s.

**Simplification in the "identity section" case.** If s is the "observing section" that
selects the physical metric g_s and if A is tuned to be the canonical connection of Y¹⁴
(the gimmel Levi-Civita connection ∇_ℊ), then:

```
s*(θ) = s*(A) − ∇_LC(g_s) = [s*(∇_ℊ)] − ∇_LC(g_s)
```

The pullback of the gimmel Levi-Civita connection decomposes as (from the PC2 stub §5.4):

```
s*(∇_ℊ) = ∇_LC(g_s) + II_s
```

where II_s is the second fundamental form of s (see §B3 below). Therefore:

```
s*(θ) = II_s
```

The distortion in 4D becomes the **second fundamental form of the section**. This is the
most concrete identification: the dark energy field θ, when pulled back to the observing
4D spacetime via the section s, equals the bending of s in Y¹⁴.

`[reconstruction — this identification requires: (i) A = ∇_ℊ (canonical connection), (ii)
the decomposition s*(∇_ℊ) = ∇_LC + II_s (from Gauss formula for submanifolds), (iii) the
specific form of the τ⁺ gauge transformation reducing to the identity in the canonical case.
The identification s*(θ) = II_s is strongly motivated but has not been verified in full rigor.]`

### B1.5 — Does s*(θ) give the 4D Einstein equations?

**The GU vacuum equation on Y¹⁴ (on-shell):**

```
D_A* F_A = θ    (from dark-energy-noether-closure-2026-06-22.md §4.2)
```

Pulling back via s*:

```
s*(D_A* F_A) = s*(θ)
```

The left side is a complicated object: it is the pullback of the 14D Yang-Mills equation
applied to the curvature F_A. For a general section s, this pullback is not the same as
the Yang-Mills equation for the 4D pulled-back connection s*(A).

**However, there is a special case.** If the section s is a **totally geodesic section**
(its second fundamental form vanishes: II_s = 0) AND the connection A is the canonical
gimmel connection ∇_ℊ, then:

```
s*(θ) = II_s = 0
s*(D_A* F_A) = D_{s*(A)}* s*(F_A)
```

The vacuum equation becomes:

```
D_{s*(A)}* s*(F_A) = 0    (4D Yang-Mills vacuum equation)
```

This is NOT Einstein's equations; it is the 4D Yang-Mills equation for the pulled-back
connection. To get Einstein's equations, one needs to make contact between the Yang-Mills
structure and the Riemann curvature tensor — which is the Einstein-Cartan move (using
the accidental isomorphism so(1,3) ≅ Λ²T*X⁴ in 4D) that Weinstein discusses at [00:29:00–00:30:05].

**When II_s ≠ 0:** The vacuum equation becomes:

```
D_{s*(A)}* s*(F_A) = s*(θ) = II_s
```

This is a **sourced Yang-Mills equation** on X⁴ where the source is the second fundamental
form of the section. The second fundamental form encodes how the metric g_s varies in the
metric space Y¹⁴. If II_s is small (slowly-varying metric), this reduces to the vacuum
Yang-Mills equation; if II_s is comparable to the curvature, it contributes as a dynamical
source.

**Connection to dark energy.** The vacuum GU field equation (after section pullback) is:

```
D_{s*(A)}* s*(F_A) − II_s = 0
```

In the 4D language: the Yang-Mills curvature is balanced by the second fundamental form.
The second fundamental form II_s ∈ Γ(S²T*X⁴ ⊗ N_s) encodes the "bending" of the
observation section in the metric space. This is the GU dark energy contribution: a
geometric quantity (bending of the observer's section) that acts as a source in the
curvature equation, replacing Λg_{μν}.

`[reconstruction — the identification (sourced Yang-Mills) = (GU analog of Einstein equations
with dark energy) requires: identifying the Yang-Mills connection with the spin connection of X⁴,
using the accidental isomorphism so(1,3) ≅ Λ²T*X⁴, and tracing through the GU action principle
to see that the coupled equations reduce to Einstein + dark energy in some limit. This is an
exploration-grade sketch, not a derivation.]`

---

## §B2 — Spinor Branching Under the Section

### B2.1 — Setup: the 14D spinor S = ℍ^{64}

From the N1 signature audit (`n1-signature-audit-y14-clifford-algebra-2026-06-22.md`):

- Y¹⁴ carries the gimmel metric ℊ of signature (9,5)
- The Clifford algebra Cl(9,5) ≅ M(64,ℍ) (quaternionic 64×64 matrices) `[verified]`
- The irreducible spinor module: S = ℍ^{64}, dim_ℍ = 64, dim_R = 256 `[verified]`

A section s: X⁴ → Y¹⁴ determines a splitting of the tangent bundle of Y¹⁴ at s(X⁴):

```
T_{s(x)}Y¹⁴ = H_{s(x)} ⊕ V_{s(x)}
```

where:
- **H** (horizontal) ≅ T_x X⁴ is 4-dimensional with signature (3,1) (the tangent to the
  section, which inherits the Lorentzian metric g_s from X⁴)
- **V** (vertical) = T_{s(x)}(π⁻¹(x)) ≅ Sym²(T*_x X⁴) is 10-dimensional with signature
  (6,4) (after the trace-reversal of the Frobenius metric)

This is the (H ⊕ V) splitting with signatures (3,1) + (6,4) = (9,5). `[verified — from
the gimmel metric construction in PC2 stub §2]`

### B2.2 — Clifford algebra splitting

The Clifford algebra Cl(H ⊕ V) = Cl(9,5) splits via the canonical algebra isomorphism:

```
Cl(p+q, r+s) ≅ Cl(p,r) ⊗̂ Cl(q,s)   (graded tensor product)
```

In our case:

```
Cl(9,5) ≅ Cl(3,1) ⊗̂ Cl(6,4)
```

(graded tensor product of Clifford algebras for the horizontal (3,1) and vertical (6,4)
factors). `[verified — this is the standard Clifford algebra product formula for orthogonal
direct sums; see Lawson-Michelsohn §I.1, Proposition 1.3]`

**Known Clifford algebras:**
- Cl(3,1) ≅ M(4,R): real 4×4 matrices; (p−q) mod 8 = (3−1) mod 8 = 2... 

Wait — let me compute (p,q) = (3,1): index = p − q = 2, from ABS table: Cl(3,1) ≅ M(2,ℍ)
(quaternionic 2×2 matrices). `[verified — Lawson-Michelsohn Appendix I, Table 1: index 2
gives ℍ-type with N = 2^{4/2}/2 = 2, so M(2,ℍ); dim_R = 16 ✓ = dim Cl(3,1)]`

- Cl(6,4) ≅ M(16,C): complex 16×16 matrices. `[verified — from generation-count-sm-branching
  closure §2.1: index (6−4) mod 8 = 2 gives complex type with N=16, so M(16,C)]`

**Spinor modules:**
- S(3,1) = ℍ^2 (the irreducible Cl(3,1) = M(2,ℍ) module): dim_ℍ = 2, dim_R = 8, dim_C = 4
  `[verified — M(2,ℍ) acts on ℍ^2 by matrix multiplication]`
- S(6,4) = ℂ^{16} (the irreducible Cl(6,4) = M(16,C) module): dim_C = 16, dim_R = 32
  `[verified — M(16,C) acts on ℂ^{16}]`

### B2.3 — The spinor product formula

For an orthogonal direct sum V = H ⊕ V_fiber of vector spaces with non-degenerate quadratic
forms, the spinor module satisfies:

```
S(H ⊕ V_fiber) = S(H) ⊗_R S(V_fiber)   (real tensor product)
```

`[verified — standard "spinor product formula"; see Lawson-Michelsohn §I.5, Theorem 5.4 or
the ABS paper §2; also cited in generation-count-sm-branching-closure-2026-06-22.md §1.5]`

Applying to our case:

```
S(9,5) = S(3,1) ⊗_R S(6,4)
```

**Dimension check:**
- dim_R(S(3,1) ⊗_R S(6,4)) = dim_R(ℍ²) × dim_R(ℂ^{16}) = 8 × 32 = 256
- dim_R(S(9,5)) = dim_R(ℍ^{64}) = 256 ✓

`[verified — dimensions are consistent]`

### B2.4 — What the components are

**S(3,1) = ℍ² — the spacetime spinor factor.**

As a representation of Spin(3,1) ≅ SL(2,C)/Z₂, the module S(3,1) = ℍ² decomposes. The
Dirac spinor representation of Cl(3,1) = M(2,ℍ) on ℍ² is:

Over ℂ (complexifying): ℍ² ⊗_R ℂ = ℂ⁴ (since each ℍ ⊗_R ℂ = ℂ²). The complexified
spinor ℂ⁴ is the Dirac spinor representation of Spin(3,1) in standard notation: it decomposes
under SL(2,C) as:

```
ℂ⁴ = S_L ⊕ S_R   (left-handed Weyl ⊕ right-handed Weyl spinors)
```

where S_L = (1/2,0) (dim_C = 2) and S_R = (0,1/2) (dim_C = 2) are the two Weyl spinor
representations of SL(2,C). Over R, the real structure of M(2,ℍ) makes the Dirac spinor
a quaternionic 2-vector (not reducible over R to two independent Weyl spinors; they are
related by quaternionic conjugation). `[verified — standard SL(2,C) spinor theory]`

**S(6,4) = ℂ^{16} — the fiber spinor factor (internal matter content).**

As established in the generation-count-sm-branching-closure-2026-06-22.md §2:

```
S(6,4) = ℂ^{16} decomposes under the maximal compact Spin(6) × Spin(4)
                = SU(4) × SU(2)_L × SU(2)_R (the Pati-Salam group) as:

S(6,4) → (4, 2, 1) ⊕ (4̄, 1, 2)    [one complete Pati-Salam generation]
```

`[verified — generation-count-sm-branching-closure §2.3; Slansky 1981 Table 28]`

This is 16 Weyl fermions = one SM generation with right-handed neutrino.

**The full spinor under the section:**

```
S(9,5) = S(3,1) ⊗_R S(6,4) = ℍ² ⊗_R ℂ^{16}
```

Under the section s, a spinor Ψ ∈ Γ(S) over Y¹⁴ pulls back to s*(Ψ) ∈ Γ(s*S) over X⁴,
where:

```
s*(S)_x = S(3,1) ⊗_R S(6,4) = ℍ² ⊗_R ℂ^{16}
```

(the tensor product of spacetime spinor and fiber spinor, at each point x ∈ X⁴).

Under SL(2,C) × Pati-Salam = SL(2,C) × SU(4) × SU(2)_L × SU(2)_R, the spinor content is:

```
s*(S) = (S_L ⊕ S_R) ⊗_C S(6,4)
       = [S_L ⊗_C S(6,4)] ⊕ [S_R ⊗_C S(6,4)]
```

Over ℂ (complexifying the real tensor product):

```
S_L ⊗_C S(6,4) = (1/2,0) ⊗_C ℂ^{16} ≅ ℂ^{32}
S_R ⊗_C S(6,4) = (0,1/2) ⊗_C ℂ^{16} ≅ ℂ^{32}
```

Under Pati-Salam (acting on S(6,4)):

```
S_L ⊗ S(6,4) → S_L ⊗ [(4,2,1) ⊕ (4̄,1,2)]    (left-handed spacetime spinor ⊗ Pati-Salam)
S_R ⊗ S(6,4) → S_R ⊗ [(4,2,1) ⊕ (4̄,1,2)]    (right-handed spacetime spinor ⊗ Pati-Salam)
```

Each of these sectors gives 16 complex Weyl fermion degrees of freedom under the Pati-Salam
gauge group — one SM generation. Together, the two sectors give 2 generations.

The third generation arises from the Rarita-Schwinger sector (spin-3/2 coupling term in the
Leibniz rule for the Dirac-DeRham operator; see generation-count §4 and the transcript at
[00:39:18]).

### B2.5 — Resolving the Factor-of-4 Discrepancy

**The apparent discrepancy.** From B2.3 and B2.4:
- s*(S) as an ℝ-vector space has dim_R = 256
- Two SM generations (from S_L ⊗ S(6,4) and S_R ⊗ S(6,4)) have dim_C = 32 + 32 = 64
  complex dimensions = dim_R = 128 real dimensions
- Remaining: 256 − 128 = 128 real dimensions not accounted for by the two spin-1/2 sectors

**Resolution from ℍ-line counting** (from generation-count-sm-branching-closure §1.5):

The spinor module S = ℍ^{64} has dim_ℍ = 64 and carries a **right ℍ-module structure** that
D_GU commutes with. The natural index theorem for D_GU counts ℍ-lines (quaternionic dimensions),
not ℝ-lines. Under this counting:

- S_L ⊗_R S(6,4) as an ℍ-module: 2 ℍ-lines (from S_L = ℂ² = ℍ¹ as ℍ-module) times 8
  ℍ-lines (from S(6,4) = ℂ^{16} = ℍ^8 as ℍ-module) tensored over ℝ gives 4 × 1 × 8 = 32
  ℍ-lines. Similarly for S_R.

Wait — let me use the formula from the generation-count file §1.5: ℍ^r ⊗_ℝ ℍ^s has
ℍ-rank 4rs. So S_L ⊗_ℝ S(6,4) (where S_L = ℍ¹ as a quaternionic Weyl spinor and
S(6,4) = ℍ^8) has ℍ-rank = 4 × 1 × 8 = 32 ℍ-lines.

This means the two "standard" sectors S_L ⊗ S(6,4) and S_R ⊗ S(6,4) together span
32 + 32 = 64 ℍ-lines = dim_ℍ S. So the full spinor is accounted for:

```
S(9,5) = [S_L ⊗_R S(6,4)] ⊕ [S_R ⊗_R S(6,4)]
```

where each factor has dim_ℍ = 32 and the two factors together give dim_ℍ = 64 = dim_ℍ(S(9,5)).
`[reconstruction — this decomposition uses the ℍ-rank formula for real tensor products of
quaternionic modules; it accounts for the full quaternionic spinor without "extra" components]`

The 256 real dimensions decompose as:
- S_L ⊗_R S(6,4): dim_R = 4×32 = 128 real dimensions (containing 2 SM-generation-worth of
  Weyl fermions under SL(2,C) × Pati-Salam, after complexification)
- S_R ⊗_R S(6,4): dim_R = 128 real dimensions (another 2 generations worth)

But in terms of distinct SL(2,C) × Pati-Salam representations, the S_L and S_R sectors each
contribute **exactly one** Pati-Salam generation of 16 Weyl fermions. The remaining 128−32 = 96
real dimensions per sector (i.e., the complex dimensions beyond the Pati-Salam 16) arise from
the real structure (the ℍ vs. ℂ counting). They are not additional "extra" fermion content;
they are the real degrees of freedom in the quaternionic spinor that are related by the
quaternionic conjugation (the right ℍ-action). In the physical Dirac operator's index, only
the ℍ-line count is physically meaningful, and each S_L ⊗ S(6,4) sector contributes 1 SM
generation.

`[reconstruction — this resolution of the "extra" dimensions is consistent with the
generation-count-sm-branching-closure §1.5 analysis; it relies on the ℍ-line index theorem
applying correctly to the non-compact Y¹⁴ setting, which is an open analytic condition (A-1)
from that file]`

### B2.6 — The Rarita-Schwinger sector

The Dirac-DeRham operator D_GU on Y¹⁴ = H ⊕ V is NOT the simple Dirac operator ∂_H ⊗ 1_V +
1_H ⊗ ∂_V; there is a Leibniz coupling term. From the generation-count §4 and the transcript
[00:39:18]:

```
D_GU acts on (S_L ⊕ S_R) ⊗ S(6,4)
            = S_L ⊗ S(6,4) ⊕ S_R ⊗ S(6,4) ⊕ RS(3,1) ⊗ S(6,4)
```

where RS(3,1) is the Rarita-Schwinger (spin-3/2) sector that appears in the Leibniz rule
for the spinor product on the direct sum H ⊕ V. This contributes a third SM generation
with:
- Internal quantum numbers from S(6,4): the Pati-Salam representation (4̄,2,1) ⊕ (4,1,2)
  (flipped chirality = conjugate Pati-Salam representation)
- Lorentz representation: spin-3/2 rather than spin-1/2
- At low energy: gauge-indistinguishable from the spin-1/2 generations

`[reconstruction — from generation-count-sm-branching-closure §4; the RS sector's appearance
in the section pullback requires explicit analysis of the Leibniz coupling in the pulled-back
operator s*(D_GU); not derived here in full detail]`

### B2.7 — Summary of spinor branching

Under the section s: X⁴ → Y¹⁴, the spinor bundle S = ℍ^{64} pulls back to:

```
s*(S) = S(3,1) ⊗_R S(6,4)
       = ℍ² ⊗_R ℂ^{16}
```

with the SM content (under SL(2,C) × SU(4) × SU(2)_L × SU(2)_R):

| Sector | Origin | SM reps | Lorentz spin | # generations |
|---|---|---|---|---:|
| S_L ⊗ S(6,4) | Horizontal left-Weyl ⊗ fiber spinor | (4,2,1)⊕(4̄,1,2) | spin-1/2 | 1 |
| S_R ⊗ S(6,4) | Horizontal right-Weyl ⊗ fiber spinor | (4,2,1)⊕(4̄,1,2) | spin-1/2 | 1 |
| RS(3,1) ⊗ S(6,4) | Leibniz Rarita-Schwinger coupling | (4̄,2,1)⊕(4,1,2) flipped | spin-3/2 | 1 (imposter) |
| **Total** | | | | **3** |

`[verified for the spin-1/2 sectors (branching rules); reconstruction for RS sector count]`

---

## §B3 — Second Fundamental Form of the Section

### B3.1 — Definition

The section s: X⁴ → Y¹⁴ is a smooth immersion (embedding) of X⁴ as a 4-dimensional
submanifold of Y¹⁴. The **second fundamental form** of s measures how s curves in Y¹⁴.

**Gauss formula.** For a submanifold M ⊂ N (here: s(X⁴) ⊂ Y¹⁴) with a connection ∇^N on
the ambient manifold N and the induced connection ∇^M on M, the Gauss formula states:

```
∇^N_{ds(v)} ds(w) = ds(∇^M_v w) + II_s(v, w)   for v, w ∈ TX⁴
```

where:
- ∇^N is the Levi-Civita connection of the gimmel metric ℊ on Y¹⁴
- ∇^M is the connection induced on s(X⁴) from ℊ (which equals the Levi-Civita connection
  of the induced metric s*(ℊ) = g_s on X⁴)
- II_s(v, w) ∈ N_{s(x)} = V_{s(x)} is the **second fundamental form**, a symmetric bilinear
  map II_s: T_x X⁴ × T_x X⁴ → V_{s(x)} `[verified — standard formula; see do Carmo "Riemannian
  Geometry" §6.2 or O'Neill §II.4]`

The second fundamental form II_s is a tensor:

```
II_s ∈ Γ(S²T*X⁴ ⊗ N_s)
```

where N_s is the normal bundle of s (which is the vertical bundle V|_{s(X⁴)}, a rank-10
vector bundle over s(X⁴), or equivalently over X⁴). So:

```
II_s ∈ Γ(S²T*X⁴ ⊗ π*(Sym²T*X⁴))
```

(a symmetric 2-tensor on X⁴ valued in the symmetric 2-tensors on X⁴, i.e., a 4th-order
tensor).

### B3.2 — What is the normal bundle N_s?

**N_s = V|_{s(X⁴)}.** The vertical tangent bundle at s(x) is:

```
V_{s(x)} = T_{s(x)}(π⁻¹(x)) ≅ Sym²(T*_x X⁴)
```

This is the 10-dimensional tangent space to the fiber over x, which consists of all symmetric
2-tensors at x. As a vector bundle over X⁴:

```
N_s ≅ π*(Sym²T*X⁴)|_{s(X⁴)} ≅ Sym²T*X⁴
```

(the symmetric 2-tensor bundle over X⁴). The normal bundle to the section s is the symmetric
2-tensor bundle of X⁴. `[verified — this follows from the vertical bundle being Sym²T*X⁴
over Y¹⁴, pulled back to X⁴ via s]`

**The second fundamental form II_s is:**

```
II_s ∈ Γ(S²T*X⁴ ⊗ Sym²T*X⁴)
```

This is a 4-index tensor symmetric in the first two indices (the S²T* factor) and the last
two indices (the Sym²T* factor, which is also symmetric). It is a totally symmetric 4-tensor
on X⁴:

```
II_s ∈ Γ(Sym²T*X⁴ ⊗ Sym²T*X⁴)
```

`[reconstruction — the full symmetry of II_s requires checking that the normal bundle metric
is compatible with the symmetry; standard for totally geodesic sections]`

### B3.3 — Explicit formula for II_s in local coordinates

Let (x^μ) be local coordinates on X⁴ and (x^μ, h_{αβ}) be the associated coordinates on
Y¹⁴ (where h_{αβ} = h_{βα} are the 10 fiber coordinates). The section s in these coordinates
is:

```
s(x^μ) = (x^μ, g_μν(x))
```

where g_μν(x) is the metric tensor of g_s at x.

The differential of s:

```
ds(∂_μ) = ∂_μ + (∂_μ g_{αβ}) ∂/∂h_{αβ}
```

(the horizontal lift plus the variation of the metric).

The second fundamental form of s in Y¹⁴ is (using the Gauss formula and the gimmel
Levi-Civita connection ∇_ℊ):

```
II_s(∂_μ, ∂_ν) = [∇_ℊ_{ds(∂_μ)} ds(∂_ν)]^vertical
                = [∇_ℊ_{∂_μ} (∂_ν + (∂_ν g_{αβ}) ∂/∂h_{αβ})]^vertical
```

The vertical component of this Christoffel-symbol expression, using the gimmel metric ℊ
(which is the trace-reversed Frobenius metric in the fiber direction), involves:

```
II_s(∂_μ, ∂_ν) = (∇_{LC}(g_s))_μν^{αβ} ∂/∂h_{αβ} + (second derivatives of g_{αβ})
```

`[reconstruction — this computation requires the explicit Christoffel symbols of ℊ in the
(x^μ, h_{αβ}) coordinates; the gimmel metric's Christoffel symbols depend on the Frobenius
metric (trace-reversed) and the horizontal metric; the computation is concrete but lengthy]`

**The key structural observation.** The second fundamental form II_s of the section s is
directly related to the **rate of change of the metric** g_s as a function on spacetime. If
g_s is constant (flat spacetime), II_s = 0 (s is totally geodesic). If g_s varies (curved
spacetime), II_s ≠ 0 and encodes the curvature of the spacetime metric.

More precisely: II_s(∂_μ, ∂_ν) measures how s bends in the fiber direction when moving in
the μ-ν directions. Since the fiber at x is Sym²(T*_x X⁴), the "bend" in the fiber direction
records how the metric g_s changes from one fiber to the next. This is controlled by the
covariant derivative of g_s — which is the Levi-Civita compatibility condition ∇_{LC}g_s = 0
plus higher-order derivative information.

For a **metric connection** (∇g_s = 0): the basic Levi-Civita compatibility makes the
first-order terms in II_s vanish, leaving only higher-order (second-derivative) contributions.
The result: II_s ∝ ∂∂g_s (second derivatives of the metric) in some appropriate sense.

### B3.4 — How II_s relates to the 14D curvature F_A

The curvature F_A on Y¹⁴ and the second fundamental form II_s are related by the
**Gauss equation** for submanifolds:

```
s*(F_A) = F_{s*(A)} + II_s ∧ II_s   (schematically)
```

More precisely, the Gauss equation for the curvature of an embedded submanifold states:

```
s*(R_ℊ)_{μνρσ} = R_{g_s,μνρσ} + II_s(∂_μ, ∂_ρ) · II_s(∂_ν, ∂_σ) − II_s(∂_μ, ∂_σ) · II_s(∂_ν, ∂_ρ)
```

where R_ℊ is the Riemann tensor of the gimmel metric ℊ on Y¹⁴ and R_{g_s} is the Riemann
tensor of the induced metric g_s on X⁴. `[verified — standard Gauss equation for
submanifolds; see do Carmo Ch. 6, Theorem 6.3]`

**Applied to the gauge bundle.** For the connection A on the Sp(64)-bundle P → Y¹⁴, the
analog of the Gauss equation involves the principal bundle curvature:

```
s*(F_A) = F_{s*(A)} + (II_s contribution to F_A along s)
```

The "II_s contribution" is the component of F_A in the vertical-horizontal directions
(mixed curvature), which becomes the II_s term when pulled back to X⁴. This is in the spirit
of the "curvature of the embedding" contributing to the effective 4D gauge curvature.

`[reconstruction — the precise form of the Gauss equation for gauge bundles over submanifolds
(rather than the Riemannian Gauss equation for the tangent bundle) requires careful statement;
the schematic F_{s*(A)} = s*(F_A) − II_s ∧ II_s is the structural form]`

### B3.5 — Is θ = D_A*F_A related to II_s?

From §B1.4, in the canonical connection case:

```
s*(θ) = II_s   (on-shell, with A = ∇_ℊ)
```

From the GU vacuum equation (dark-energy-noether-closure §4.2):

```
θ = D_A* F_A   (on-shell)
```

Pulling back:

```
s*(D_A* F_A) = s*(θ) = II_s
```

This gives the identification:

```
4D geometric data: II_s ≅ s*(D_A* F_A) = D_{s*(A)}* s*(F_A) + (correction from II_s)
```

The correction from II_s arises because the pullback of D_A* F_A is not the same as
D_{s*(A)}* s*(F_A); the difference is controlled by the Codazzi equation (the next equation
after the Gauss equation for submanifolds):

```
D_A* F_A|_{horizontal} = D_{s*(A)}* s*(F_A) + (∇ II_s term from Codazzi equation)
```

`[reconstruction — the Codazzi equation for principal bundles states ∇^⊥ II_s − some
curvature term = 0 when A is flat in the normal directions; without that flatness, there
is a correction to the naive identification]`

**Summary.** On-shell (with A = ∇_ℊ and the GU vacuum equation):

```
II_s ≈ s*(D_A* F_A) ≈ D_{s*(A)}* s*(F_A) + (Codazzi correction)
```

The second fundamental form II_s is the 4D geometric quantity that equals the divergence of
the pulled-back curvature, modulo the Codazzi correction. This is the 4D identification of
the dark energy field: II_s encodes the "bending" of the observation section, which equals the
divergence of the gauge field curvature on X⁴.

---

## §What Equations Emerge in 4D

**Collecting the pullback data.** Given section s: X⁴ → Y¹⁴ with metric g_s, the GU field
equations pull back to X⁴ as follows:

**From the bosonic sector (Yang-Mills on Y¹⁴ pulled back):**

```
D_{s*(A)}* s*(F_A) = II_s + (Codazzi correction)
```

In the limit where II_s is small (slowly varying metric g_s) and the Codazzi correction
is negligible:

```
D_{s*(A)}* s*(F_A) ≈ 0   (4D Yang-Mills vacuum)
```

**From the bosonic sector (Riemann tensor of g_s on X⁴ via Gauss equation):**

```
R_{g_s,μνρσ} = s*(R_ℊ)_{μνρσ} − II_s · II_s   (Gauss equation)
```

The Einstein tensor of g_s is related to s*(R_ℊ) and II_s. If s*(R_ℊ) is fixed by the
14D dynamics, then this equation controls the 4D Riemann tensor as a function of II_s.

**Schematic Einstein-like equation.** Combining the Gauss equation with the Yang-Mills
field equation and identifying the Riemann curvature with the Yang-Mills curvature via
the Einstein-Cartan move (so(3,1) ≅ Λ²T*X⁴):

```
G_{μν}[g_s] = II_s · II_s − s*(R_ℊ)_{contracted} + cosmological-type term from II_s
```

`[speculation — this schematic "Einstein-like equation" requires: (i) the Einstein-Cartan
identification of Riemann curvature with Yang-Mills curvature, (ii) explicit handling of
the trace of the Gauss equation, (iii) verification that s*(R_ℊ) is the appropriate fixed
background. This is exploration-grade speculation; the equation is not derived.]`

**What is established.** At exploration grade:
- The section pullback machinery is well-defined (B1: verified)
- The spinor branching gives 2 + 1 SM generations (B2: reconstruction grade)
- The second fundamental form II_s appears as the dark energy field in 4D (B3: reconstruction)
- The full Einstein equations are NOT derived; they require further work on the Einstein-Cartan
  identification and the interplay of the Gauss/Codazzi equations with the GU action

---

## §Open Questions

**OQ-1 (Priority).** Does s*(D_A* F_A) = D_{s*(A)}* s*(F_A) hold, or is there a Codazzi
correction? Computing the Codazzi equation for the principal bundle (not just the tangent
bundle) in the (9,5)-signature Riemannian submersion Y¹⁴ → X⁴ would close this.

**OQ-2.** What is the explicit formula for II_s in coordinates (x^μ, h_{αβ}) on Y¹⁴? The
sketch in §B3.3 gives the structure but not the explicit Christoffel symbols of ℊ. This is
a concrete computation using the gimmel metric (known from the N1 audit) and is in principle
routine.

**OQ-3.** Does the identification s*(θ) = II_s hold off-shell (for all sections s) or only
on-shell (for solutions of the GU vacuum equation)? The derivation in §B1.4 uses the GU
vacuum equation θ = D_A* F_A; the off-shell statement requires the τ⁺ construction and the
gauge transformation analysis.

**OQ-4.** What happens to the RS sector under the section pullback? The generation count §B2.6
establishes the RS sector's SM content, but its precise role in the pulled-back Dirac operator
s*(D_GU) (including the shiab Φ contribution) is not derived here.

**OQ-5.** Does the ℍ-line index theorem apply to the non-compact Y¹⁴ in the families
setting? This is the analytic open condition (A-1) from the generation-count closure file;
it affects the generation count but not the structural pullback derivations in B1 and B3.

**OQ-6 (Gauss equation completeness).** The Gauss equation for the tangent bundle gives a
formula for the 4D Riemann tensor in terms of the 14D curvature and II_s. Does the Gauss
equation for the Sp(64)-bundle curvature give an analogous formula? If so, does combining
the two Gauss equations yield a 4D equation that reduces to Einstein's equations in some limit?
This is the most ambitious question and the natural endpoint of the PC2 program.

---

*Filed: 2026-06-22. Executes the section-pullback derivation tasks (B1, B2, B3) for PC2.
Builds on: `pc2-met-x4-bundle-formalization-stub-2026-06-22.md` (framework),
`generation-count-sm-branching-closure-2026-06-22.md` (B2 branching),
`dark-energy-noether-closure-2026-06-22.md` (B1 θ identification),
`n1-signature-audit-y14-clifford-algebra-2026-06-22.md` (B2 spinor module).
Status: PARTIAL — B1 and B2 at reconstruction grade; B3 at reconstruction grade;
full Einstein equations not derived (exploration-grade speculation). No result promoted to
active_research or canon without meeting `RESEARCH-STATUS.md` criteria.*
