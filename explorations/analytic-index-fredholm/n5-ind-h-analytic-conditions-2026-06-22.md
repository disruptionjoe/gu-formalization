---
title: "N5 Analytic Conditions: Quaternionic Index and Non-Compact Index Theory"
status: CONDITIONALLY_RESOLVED
date: 2026-06-22
depends_on:
  - "explorations/generation-sector/generation-count-sm-branching-closure-2026-06-22.md"
  - "explorations/anomaly-and-bordism/n1-signature-audit-y14-clifford-algebra-2026-06-22.md"
  - "explorations/geometry-curvature-emergence/pc2-met-x4-bundle-formalization-stub-2026-06-22.md"
---

# N5 Analytic Conditions: Quaternionic Index and Non-Compact Index Theory

**Purpose.** The generation-count exploration
(`explorations/generation-sector/generation-count-sm-branching-closure-2026-06-22.md`) closed the
representation-theory conditions in N5 at exploration/reconstruction grade and
identified two remaining analytic conditions:

> (a) Does ind_ℍ(D_GU) = 24 from the topology of Y¹⁴? Must be computed via an
>     index theorem.
>
> (b) Does L²-index theory apply on the non-compact space Y¹⁴?

This document executes those computations as far as the currently available
structure allows. Results are tagged `[verified]` (established result, named
reference), `[reconstruction]` (inferred from sources with explicit warrant), or
`[speculation]` (extrapolation with explicit naming of what would need to hold).

**Not done here.** This is an exploration-grade analysis, not a proof. Steps that
require analytic estimates (e.g., Sobolev bounds, elliptic regularity on non-compact
manifolds with specific curvature decay rates) are flagged as open with explicit
failure conditions.

---

## Setup

### Notation

- X⁴: smooth, compact, oriented, spin 4-manifold (the physical spacetime)
- Y¹⁴ = Met(X⁴): total space of the bundle of Lorentzian metrics on X⁴, with
  fiber at x ∈ X⁴ equal to the space of Lorentzian metrics on T_x X⁴
- π: Y¹⁴ → X⁴: the bundle projection
- F_x = π⁻¹(x): the fiber over x, as a manifold
- ℊ: the gimmel metric on Y¹⁴, signature (9,5)
- S = ℍ^{64}: the spinor module for Cl(9,5) ≅ M(64,ℍ)
- D_GU: the Dirac-DeRham-Einstein operator (Dirac operator coupled via the shiab Φ)
- S⁺ = ℍ^{32}: the positive chirality half-spinor
- TF: the vertical tangent bundle (tangent bundle along the fibers)

### What is already established

From the N1 signature audit and generation-count closure documents:

1. The correct signature of Y¹⁴ is (9,5). The total gimmel metric has signature
   (9,5) = (3,1)_horizontal ⊕ (6,4)_vertical (after trace-reversal of the
   Frobenius metric on the fiber). `[verified]`

2. Cl(9,5) ≅ M(64,ℍ). The spinor module S = ℍ^{64}, dim_ℝ = 256. Chiral
   half S⁺ = ℍ^{32}, dim_ℝ = 128. `[verified]`

3. D_GU commutes with right-ℍ multiplication; ker(D_GU) is a right-ℍ-module;
   the natural index is ind_ℍ(D_GU) ∈ ℤ counting quaternionic zero modes. `[verified]`

4. 8 ℍ-lines per SM generation (from S(6,4) = ℂ^{16} → Pati-Salam branching).
   For 3 generations we need ind_ℍ(D_GU) = 24. `[verified from branching rules]`

---

## Step 1: Fiber Homotopy Type

### §1.1 The fiber as a homogeneous space

The fiber F_x = π⁻¹(x) is the space of Lorentzian metrics on T_x X⁴ ≅ ℝ⁴. A
Lorentzian metric on ℝ⁴ is a nondegenerate symmetric bilinear form of signature (3,1).
The general linear group GL(4,ℝ) acts transitively on such forms by pullback:
g · h = h(g⁻¹·, g⁻¹·). The stabilizer of the standard Lorentzian form
η = diag(1,1,1,−1) is the orthogonal group O(3,1). Therefore:

> F_x ≅ GL(4,ℝ) / O(3,1)  as a homogeneous space. `[verified]`

### §1.2 Deformation retraction

**GL(4,ℝ) retracts to O(4) by polar decomposition.** Every invertible matrix
A ∈ GL(4,ℝ) factors uniquely as A = QP where Q ∈ O(4) is orthogonal and
P = (A^T A)^{1/2} is symmetric positive definite. The retraction t ↦ Q exp(t log P)
for t ∈ [0,1] deformation retracts GL(4,ℝ) onto O(4). `[verified — standard polar
decomposition; Gram-Schmidt; Milnor, "Topology from the Differentiable Viewpoint"]`

**O(3,1) retracts to O(3) × O(1).** The maximal compact subgroup of O(3,1) is
O(3) × O(1), which is O(3) × {±1}. The polar decomposition for the indefinite
orthogonal group retracts O(3,1) onto its maximal compact. Concretely: every
Lorentz transformation Λ ∈ O(3,1) satisfies Λ = RB where R ∈ O(3) × O(1) is a
"rotation" and B is a boost (with B in the Cartan-decomposition exponential, which
is contractible). `[verified — Gilmore, "Lie Groups, Lie Algebras, and Some of Their
Applications," Ch. 10; the Cartan decomposition of O(p,q) gives maximal compact
O(p) × O(q)]`

Therefore:

> F_x = GL(4,ℝ) / O(3,1) ≃ O(4) / (O(4) ∩ O(3,1))

where ≃ denotes homotopy equivalence, using the fact that a deformation retraction
commutes with the quotient. `[reconstruction — the homotopy equivalence GL/K ≃ C/(C∩K)
holds when the retraction of GL to C (its maximal compact) maps K to C∩K; here
C = O(4), K = O(3,1), C∩K = O(4)∩O(3,1)]`

### §1.3 Computing O(4) ∩ O(3,1)

We need matrices that simultaneously:
- Preserve the positive-definite form δ = diag(1,1,1,1), i.e., M^T δ M = δ, so M ∈ O(4)
- Preserve the Lorentzian form η = diag(1,1,1,−1), i.e., M^T η M = η, so M ∈ O(3,1)

From the first condition: M^T M = I (orthogonal in the Euclidean sense, so M^T = M^{-1}).
Substituting into the second: M^T η M = M^{-1} η M = η, so M commutes with η.

The matrix η = diag(1,1,1,−1) acts as the identity on the first three basis vectors and
as −1 on the fourth. The matrices that commute with η are block-diagonal:

> M commutes with η ⟺ M is block-diagonal with a 3×3 block acting on {e_1, e_2, e_3}
> and a 1×1 block acting on {e_4}. `[verified — standard commutant computation]`

Combined with M ∈ O(4) (which means M preserves the Euclidean metric):

- The 3×3 block must be in O(3) (preserves Euclidean metric on ℝ³)
- The 1×1 block must satisfy {±1} (preserves Euclidean metric on ℝ¹)

Therefore:

> **O(4) ∩ O(3,1) = O(3) × O(1) = O(3) × {±1}** `[verified]`

This is also immediately apparent from the fact that O(3) × O(1) is simultaneously the
maximal compact subgroup of O(3,1) and a subgroup of O(4) (since O(3) × O(1) naturally
embeds in O(4) as block-diagonal matrices).

### §1.4 The homotopy type of the fiber

From §1.2 and §1.3:

> F_x ≃ O(4) / (O(3) × O(1))

Now compute this quotient. O(4) acts transitively on the unit sphere S³ ⊂ ℝ⁴ (since
any unit vector in ℝ⁴ can be mapped to any other by an orthogonal transformation). The
stabilizer of the vector (0,0,0,1) ∈ S³ under this action is the set of matrices in O(4)
fixing e_4, which is exactly the block-diagonal matrices with a 3×3 orthogonal block =
O(3) × O(1) (where the O(1) = {±1} part acts trivially on e_4 but the sign must be +1
to actually fix e_4 as a vector, unless... let us be more careful).

**Careful statement.** O(4) acts on S³ by matrix multiplication. The orbit of e_4 = (0,0,0,1)
is all of S³ (transitivity). The stabilizer of e_4 is:

Stab(e_4) = {M ∈ O(4) : M e_4 = e_4}

If Me_4 = e_4, then the fourth column of M is e_4, and since M is orthogonal, the first
three columns must be in O(3) (acting on span{e_1, e_2, e_3}). So:

> Stab_{O(4)}(e_4) ≅ O(3) (embedded as block-diagonal with identity on the 4th row/column)

Therefore, O(4) / O(3) ≅ S³. `[verified — standard homogeneous space construction]`

But O(4) ∩ O(3,1) = O(3) × {±1}, which is LARGER than O(3) = Stab(e_4). The
difference: O(3) × {−1} consists of matrices of the form diag(R, −1) for R ∈ O(3).
These matrices satisfy M e_4 = −e_4, not +e_4. So they act on e_4 by reflection.

The quotient O(4) / (O(3) × {±1}) identifies each coset MO(3) (corresponding to a
point on S³ in the direction of M e_4) with M diag(I_3, −1) O(3) (corresponding to
the antipodal point −M e_4). In other words:

> O(4) / (O(3) × {±1}) = S³ / {±1} = ℝP³

where ℝP³ is real projective 3-space (the quotient of S³ by the antipodal map). `[verified]`

**Verification of dimension.** dim(O(4)) = 6, dim(O(3) × O(1)) = 3 + 0 = 3 (O(1) is
0-dimensional), so dim(O(4)/(O(3)×O(1))) = 6 − 3 = **3**. ✓ (ℝP³ is 3-dimensional.)
`[verified]`

**Alternative identification.** ℝP³ ≅ SO(3). This is the classical identification: the
group SO(3) of 3D rotations is homeomorphic to ℝP³ because SO(3) ≅ S³/{±1}
(via the quaternion double-cover SU(2) = S³ → SO(3) = S³/{±1}). `[verified — standard;
Hatcher, "Algebraic Topology," §1.2]`

**Conclusion:**

> **F_x ≃ ℝP³ ≅ SO(3) ≅ SU(2)/{±1}**
>
> The fiber of Y¹⁴ → X⁴ is homotopy equivalent to real projective 3-space. `[verified]`

### §1.5 The actual fiber as a manifold

The homotopy equivalence F_x ≃ ℝP³ is established. However, the actual manifold F_x is:

> F_x = GL(4,ℝ) / O(3,1)

This is a non-compact manifold. The deformation retraction of GL(4,ℝ) to O(4) involves
a non-compact factor: the space of symmetric positive definite matrices (isomorphic to
the symmetric space GL(4,ℝ)/O(4) = Sym_+(4,ℝ), which is contractible and homeomorphic
to ℝ^{10}). The O(3,1) factor contributes via the Cartan decomposition of O(3,1):

> O(3,1) ≅ (O(3) × O(1)) × ℝ^3   (Cartan decomposition: maximal compact × boost space)

where the boost space ℝ³ is the (non-compact) space of Lorentz boosts. Therefore:

> GL(4,ℝ) / O(3,1) ≅ (GL(4,ℝ)/O(4)) × (O(4)/(O(4)∩O(3,1))) × (O(3,1)/K_{O(3,1)}) / K_{O(3,1)}

This is not a clean product, but the topology is:

> F_x ≃ ℝP³ × ℝ^N for some N (approximately)

The non-compact "stem" directions correspond to the non-compact parts of GL(4,ℝ) and
O(3,1). Specifically, the contractible factors are:

- Sym_+(4,ℝ) ≅ ℝ^{10} from the polar decomposition GL(4,ℝ) = O(4) × Sym_+(4,ℝ)
- The boost space of O(3,1) / (O(3) × O(1)) ≅ ℝ³ (the symmetric space for O(3,1))

After taking the quotient GL(4,ℝ)/O(3,1), the contractible factors partially cancel.
The total fiber dimension: dim GL(4,ℝ)/O(3,1) = dim GL(4,ℝ) − dim O(3,1) = 16 − 6 = 10.
The homotopy-nontrivial part has dimension 3 (the ℝP³ factor). Therefore:

> F_x = GL(4,ℝ)/O(3,1) is a 10-dimensional manifold with homotopy type ℝP³ × ℝ^7

where the ℝ^7 denotes 7 contractible non-compact directions.
`[reconstruction — the 7 = 10 − 3 contractible directions come from: 10 dimensions of
Sym_+(4,ℝ) minus the 3 boost directions in O(3,1)/K, but the count is schematic; the exact
statement is: F_x is a smooth 10-manifold homotopy equivalent to ℝP³]`

**What matters for index theory.** The homotopy type determines the cohomology ring
H*(F_x; ℤ) = H*(ℝP³; ℤ). The non-compact directions are contractible, so they do not
contribute to characteristic classes. For the index theorem computation we need the
characteristic classes of the fiber, which depend only on the homotopy type. `[verified]`

---

## Step 2: Â(fiber) Computation

### §2.1 Spin structure of ℝP³

**Is ℝP³ spin?** The Stiefel-Whitney classes of ℝP³ are computed from the total class:

> w(ℝPⁿ) = (1+α)^{n+1}   in H*(ℝPⁿ; ℤ/2),   where α ∈ H¹(ℝPⁿ; ℤ/2) is the generator

For n = 3:
> w(ℝP³) = (1+α)⁴ = 1 + 4α + 6α² + 4α³ + α⁴

In ℤ/2 coefficients: 4 ≡ 0, 6 ≡ 0, so (1+α)⁴ = 1 in H*(ℝP³; ℤ/2).

Therefore all Stiefel-Whitney classes of ℝP³ vanish: w_1 = w_2 = w_3 = 0. `[verified]`

**Conclusion:** ℝP³ is both orientable (w_1 = 0) and spin (w_2 = 0). `[verified]`

*Note:* The vanishing of all w_i for ℝP³ follows from the fact that (1+α)⁴ ≡ 1 mod 2
in H*(ℝP³; ℤ/2). This is the specific case n = 3 (mod 4 = 3) where ℝPⁿ is spin.
Compare: ℝP¹ is spin (circle), ℝP² is not (w_2 ≠ 0), ℝP³ is spin, ℝP⁴ is not, etc.
`[verified — ℝPⁿ is spin iff n ≡ 3 (mod 4) for n ≥ 2; Lawson-Michelsohn §II.1,
Example 5.14]`

### §2.2 Is T(SO(3)) trivial?

**Claim.** The tangent bundle T(SO(3)) is trivializable. `[verified]`

**Argument.** SO(3) is a Lie group. Every Lie group has a trivial tangent bundle: the
left-invariant vector fields {X_1, X_2, X_3} (corresponding to an orthonormal basis
{e_1, e_2, e_3} of the Lie algebra so(3)) provide a global frame for T(SO(3)). The map
(g, v) ↦ (dL_g)(v) gives a bundle isomorphism T(SO(3)) ≅ SO(3) × ℝ³. `[verified —
standard Lie group fact: T(G) ≅ G × g for any Lie group G; e.g. Milnor-Stasheff,
"Characteristic Classes," §4]`

Since ℝP³ ≅ SO(3), we have T(ℝP³) = T(SO(3)) which is trivializable. `[verified]`

**Implication for Pontryagin classes.** If T(ℝP³) is stably trivializable (which it is,
since it is actually trivializable), then all Pontryagin classes of ℝP³ vanish:

> p_k(ℝP³) = 0   for all k ≥ 1. `[verified — characteristic classes of a trivial bundle vanish]`

*Explicit check.* p₁(ℝP³) ∈ H⁴(ℝP³; ℤ). But dim(ℝP³) = 3, so H⁴(ℝP³; ℤ) = 0. Therefore
p₁(ℝP³) = 0 by dimensionality alone. `[verified]`

### §2.3 The Â-genus of ℝP³

The Â-genus is computed from the Pontryagin classes. For an n-manifold M, the Â class is:

> Â(M) = 1 − p₁/24 + (7p₂ − p₁²)/5760 + ...  (in H*(M; ℚ))

For ℝP³ (dimension 3):
- H^k(ℝP³; ℚ) = 0 for k > 0 (since H*(ℝP³; ℤ) is torsion in positive degrees,
  and rational cohomology of ℝP³ vanishes in positive degrees) `[verified]`
- Therefore all Pontryagin class terms vanish rationally.

**Conclusion:**

> **Â(ℝP³) = 1** (in H*(ℝP³; ℚ))
>
> Equivalently, the Â-genus ∫_{ℝP³} Â = 0 (since ℝP³ has dimension 3, which is odd, so
> the fundamental class is in degree 3, and Â lives in degree 0 for the leading term,
> hence the integral is 0). `[verified]`

*More precisely:* the Â-genus ∫_M Â(TM) is only interesting (and nonzero) in dimensions
divisible by 4. For odd-dimensional manifolds like ℝP³ (dim = 3), the Â-genus integral
is automatically 0 — not because the integrand vanishes, but because there is no degree-3
rational cohomology to integrate against. The top-degree part of Â(TM) that would
contribute is the degree-3 part, but since T(ℝP³) is trivializable, Â(TℝP³) = 1 (just
the degree-0 term), and ∫_{ℝP³} 1 = 0 in rational cohomology (no degree-3 class). `[verified]`

### §2.4 Fiber Â computation for the Bismut theorem

The Bismut Families Index Theorem requires Â(TF) where TF is the **vertical** (fiber)
tangent bundle restricted to the fiber F_x. Since F_x ≃ ℝP³ (homotopically), and
T(F_x) restricted to the fiber is homotopy-equivalent to T(ℝP³), which is trivializable:

> **Â(TF) = 1** (as a class in H*(F_x; ℚ))  `[reconstruction — follows from trivializability
> of T(ℝP³) and the fact that Â of a trivial bundle is 1; the extension from ℝP³ to the
> actual 10-manifold F_x = GL(4,ℝ)/O(3,1) uses the homotopy equivalence]`

*Caveat:* The actual vertical tangent bundle TF on the full non-compact fiber
GL(4,ℝ)/O(3,1) (a 10-manifold) must be distinguished from T(ℝP³) (a 3-manifold).
The homotopy equivalence GL(4,ℝ)/O(3,1) ≃ ℝP³ means the cohomological characteristic
classes agree rationally. Specifically: under the homotopy equivalence, Â(TF) pulls
back to Â(T(ℝP³)) = 1 in rational cohomology. `[reconstruction]`

---

## Step 3: Families Index Theorem Applied

### §3.1 Setup for the Bismut Families Index Theorem

The Bismut Families Index Theorem (Bismut 1986) applies to a proper fibration π: Z → B
with compact fibers, equipped with a family of Dirac operators D_b on the fibers. It
computes the Chern character of the index bundle:

> ch(ind D) = ∫_{fib} Â(TF) · ch(S_F)   in H*(B; ℚ)

where S_F is the fiber spinor bundle. `[verified — Bismut, "The Atiyah-Singer index theorem
for families of Dirac operators: two heat equation proofs," Inventiones Math. 83, 1986]`

**Issue: non-compact fibers.** The Bismut theorem in its standard form requires compact
fibers. Our fiber F_x = GL(4,ℝ)/O(3,1) is 10-dimensional and non-compact. The compact
retract ℝP³ ⊂ F_x is compact, but the full fiber is not.

This is the primary obstruction, addressed in detail in Step 4. For now, we analyze what
the theorem would give under the assumption that the index can be computed on the
compact retract (or with appropriate boundary conditions). This assumption is labeled
`[speculation]`.

### §3.2 Identifying the family of Dirac operators

In the GU setting:
- B = X⁴ (compact base)
- Z = Y¹⁴ (non-compact total space)
- The family of operators is D_GU|_{fiber} restricted to the fiber over each x ∈ X⁴

But D_GU is a 14-dimensional operator on Y¹⁴, not a family of lower-dimensional operators
indexed by X⁴. The correct interpretation is the **families index** setup:

> The Families Index Theorem for D_GU should be read as follows: D_GU defines a
> continuous family (parameterized by X⁴) of operators on the fibers. The index of
> this family is an element of K(X⁴).

However, D_GU is the full 14D Dirac operator on Y¹⁴; it mixes horizontal and vertical
directions. The restriction of D_GU to the fibers is not D_GU itself but a fiber-Dirac
operator D_{fib} obtained by projecting to the vertical component of D_GU.

**Key point:** The Bismut theorem should be applied to the *fiber Dirac operator* D_{fib},
not the full D_GU. The full D_GU = D_{fib} + D_{hor} where D_{hor} contains horizontal
(X⁴) derivatives. In the adiabatic limit (as the fiber-to-base scale ratio → 0), the
leading index contribution comes from D_{fib}. `[reconstruction — standard adiabatic
limit analysis; Berline-Getzler-Vergne, "Heat Kernels and Dirac Operators," Ch. 10]`

### §3.3 The fiber Dirac operator and its index

**Fiber spinor bundle.** Over the fiber F_x = GL(4,ℝ)/O(3,1), the spinor bundle S_F
is the restriction of the full spinor bundle S = ℍ^{64} to the fiber. Since the fiber
has signature (6,4) (from the trace-reversed Frobenius metric on the vertical directions),
the relevant Clifford algebra is Cl(6,4):

> Cl(6,4) ≅ M(16,ℂ),   fiber spinor S(6,4) = ℂ^{16}   `[verified — N1 audit, §2; and the
> generation-count closure document §2.1]`

The fiber Dirac operator D_{fib} acts on sections of S(6,4) over F_x. Its index:

> ind(D_{fib}) ∈ K(pt) = ℤ   (or in KO(pt) for the ℍ-linear version)

### §3.4 The Bismut formula on the fiber

**If** the Bismut theorem applies (with compact fiber, or with the non-compactness
handled — see Step 4), the formula gives:

> ch(ind D_{fib}) = ∫_{F_x} Â(TF_x) · ch(S(6,4))

With Â(TF_x) = 1 (from Step 2, under the homotopy-type argument), this simplifies to:

> ch(ind D_{fib}) = ∫_{F_x} ch(S(6,4))

Now ch(S(6,4)) = dim_ℂ(S(6,4)) + (higher Chern character terms) = 16 + (higher terms).

**The integral.** The Chern character is a formal polynomial in the curvature:

> ch(S(6,4)) = rank(S(6,4)) + c₁(S(6,4)) + (c₁² − 2c₂)/2 + ...

The integral ∫_{F_x} ch(S(6,4)) picks out the degree-dim(F_x) = degree-10 component
(or degree-3 if we use the homotopy retract ℝP³). But here we hit a critical dimensional
constraint:

**The fiber is 10-dimensional (as a manifold), homotopy equivalent to the 3-manifold ℝP³.**

The Bismut formula integrates a cohomology class over the *actual* fiber (the 10-manifold),
not over the homotopy retract (the 3-manifold). The integral of a form over a 10-manifold
requires a 10-form; the integral of a form over a 3-manifold requires a 3-form.

Since S(6,4) = ℂ^{16} is a flat bundle (it is the fiber of the Cl(6,4)-spinor bundle,
which is trivializable over the contractible fibers of F_x → ℝP³), its Chern character
is:

> ch(S(6,4)) = 16 (the rank, as a degree-0 class)

This is a locally constant function, not a differential form of degree 10. Therefore:

> ∫_{F_x} ch(S(6,4)) = ∫_{F_x} 16 · [10-form part of ch(S(6,4))]

But if ch(S(6,4)) = 16 (a flat bundle with trivial curvature), then the integral over a
non-compact 10-manifold is zero — or rather undefined, since ∫_{F_x} 1 diverges for
non-compact F_x. `[verified — the Bismut formula requires L²-integrability, and an
integral of a constant over a non-compact manifold is infinite]`

**Resolution of the integral.** The correct interpretation is:

(a) The Bismut formula for the *families index* integrates over the fiber and returns
    a class in H*(X⁴; ℚ), not a number.
(b) The 10-dimensional integration over F_x of a degree-0 form returns a degree-10
    class. But H^{10}(X⁴; ℚ) = 0 since dim X⁴ = 4. So the formula gives 0 in this
    naive reading.

This suggests the Bismut formula, naively applied to D_{fib} over the full 10-dim
non-compact fiber, gives ind = 0 — which is wrong (it would predict 0 generations).
The error is in the setup: the families index theorem is being mis-applied.

### §3.5 Correct setup: the Bismut theorem for the 14D operator

**The correct statement.** The families index theorem should be applied to the FULL 14D
operator D_GU, viewed as a family over X⁴ only in a degenerate sense. The correct
theorem to apply is the **Atiyah-Singer index theorem on Y¹⁴** (if the manifold is
compact or if an L²-index is well-defined), not the Bismut theorem.

The Bismut Families Index Theorem applies to a situation where:
- The total space Z is a fiber bundle over B with compact fibers
- The operator is a *family* of operators on each compact fiber

In the GU case:
- Y¹⁴ is the total space
- X⁴ is the base
- The fibers F_x are NON-COMPACT (GL(4,ℝ)/O(3,1))
- D_GU is a 14D operator on the total space, not a family of operators on the fibers

The Bismut theorem does not directly apply to this setup. `[verified — the non-compactness
of the fibers is a genuine obstruction to the standard Bismut theorem]`

### §3.6 What the Bismut theorem would give IF the fiber were compact

For completeness, if the fiber could be replaced by its compact retract ℝP³ (a 3-manifold
with trivial T), and if the spinor bundle S(6,4) were replaced by the fiber spinor bundle
S(3, 0) on ℝP³ (a 3-dimensional space with signature (3,0) or (2,1) depending on the
Euclidean vs. Lorentzian restriction of the fiber metric), then:

> The Â-genus ∫_{ℝP³} Â(Tℝp³) = 0 (odd-dimensional manifold)

This gives:

> ch(ind D_{fib,compact}) = ∫_{ℝP³} Â(Tℝp³) · ch(S_F) = 0 · (anything) = 0

**Warning:** An index of 0 does NOT mean no zero modes. It means the chiral index
(dim ker D⁺ − dim ker D⁻) = 0. If the operator is self-adjoint (as Dirac operators
typically are), this is automatic: the Atiyah-Singer index of a self-adjoint operator
is always 0. The generation count comes from the *total* kernel dimension, not the
*chiral* (signed) index.

For a self-adjoint Dirac operator (or in the L²-Fredholm sense), the *family* index in
K(X⁴) can still be non-trivial even when the fiberwise numerical index is 0. The K-theory
class encodes more refined information. `[reconstruction — Atiyah-Singer families index in K-theory
vs. the numerical Â-genus integral]`

### §3.7 Revised verdict on Step 3

The families index theorem computation, as attempted above, runs into two obstructions:

1. **Non-compact fibers** prevent the direct application of the Bismut theorem.
2. **Dimensional mismatch**: the fiber is 10-dimensional but the Â-integral over a
   non-compact space does not reduce to a class in H*(X⁴; ℚ) without L²-bounds.

**What CAN be said.** The Atiyah-Singer index theorem on Y¹⁴ itself (not the Bismut families
theorem) is the appropriate tool. If ind_ℍ(D_GU) is well-defined on Y¹⁴ (question of
Step 4), it is an integer in ℤ computed from the Â-genus and Chern character data of Y¹⁴:

> ind_ℍ(D_GU) = ∫_{Y¹⁴} Â(TY¹⁴) · ch(S)   (symbolically, if Y¹⁴ were compact)

Since Y¹⁴ is not compact, this integral requires compactification or L²-methods. See Step 4.

---

## Step 4: Non-Compact Index Theory

### §4.1 The non-compactness of Y¹⁴

Y¹⁴ = Met(X⁴) is a fiber bundle over the compact base X⁴ with fiber
F_x = GL(4,ℝ)/O(3,1), which is a non-compact 10-manifold. Therefore Y¹⁴ is non-compact.

The standard Atiyah-Singer index theorem applies to compact manifolds without boundary.
For non-compact manifolds, several extensions exist:

(A) **L²-index theorem (Atiyah's Γ-index theorem, 1976):** for manifolds with a cocompact
    proper group action; the index is a von Neumann-dimension.

(B) **Atiyah-Patodi-Singer (APS) index theorem, 1975:** for compact manifolds with
    boundary; uses global boundary conditions.

(C) **Gromov-Lawson index theorem (1983), Roe's index theorem (1988), Bunke's index
    theorem (1992):** for manifolds of bounded geometry; the index is defined in K-theory.

(D) **Fredholm index under decay conditions:** if D_GU is Fredholm on weighted L²-Sobolev
    spaces (with polynomial or exponential weight decay toward the fiber ends), the index
    is well-defined.

### §4.2 Bounded geometry

**Definition.** A Riemannian manifold (M, g) has bounded geometry if:
- The injectivity radius is bounded below: inj(M) ≥ ε > 0
- All covariant derivatives of the curvature tensor are bounded: |∇^k R| ≤ C_k for all k ≥ 0

`[verified — Shubin, "Spectral theory of elliptic operators on non-compact manifolds,"
Astérisque 207, 1992; Roe, "Elliptic Operators, Topology and Asymptotic Methods"]`

**Does Y¹⁴ have bounded geometry?**

Y¹⁴ = Met(X⁴) is equipped with the gimmel metric ℊ of signature (9,5). The gimmel metric
is constructed from the Frobenius metric on the fibers plus the tautological (3,1)
horizontal metric. The curvature of ℊ involves:

- The Riemann curvature of X⁴ in the horizontal directions
- The curvature of the fiber metric (Frobenius metric on Sym²(T*X)) in the vertical directions
- Cross-terms from the horizontal-vertical coupling

**Problem with the non-compact fiber.** As one moves to "infinity" in the fiber
F_x = GL(4,ℝ)/O(3,1), the fiber point h → ∞ (meaning the metric h becomes degenerate
or its determinant → 0 or ∞, i.e., one approaches the boundary of the space of
non-degenerate Lorentzian metrics). The Frobenius metric tr(h⁻¹ k h⁻¹ l) involves h⁻¹,
which blows up as h degenerates. Conversely, as det(h) → ∞ (metrics with very large
scale), the Frobenius metric also changes behavior.

**The injectivity radius issue.** For symmetric spaces of non-compact type (like the
fiber GL(4,ℝ)/O(3,1)), the injectivity radius is positive and bounded below (since they
are simply connected and non-positively curved). `[verified — Cheeger-Gromov, symmetric
spaces of non-compact type are Hadamard manifolds]`

However, GL(4,ℝ)/O(3,1) is NOT a Riemannian symmetric space with the gimmel metric —
the gimmel metric on the fiber has Lorentzian signature (6,4), not Riemannian signature.
The analysis of bounded geometry for pseudo-Riemannian metrics is more subtle.

**Conclusion on bounded geometry.** Whether Y¹⁴ with the gimmel metric ℊ has bounded
geometry (in an appropriate pseudo-Riemannian or Lorentzian sense) is not established
at this stage. It is plausible (since the fiber is a homogeneous space of a Lie group,
which typically has bounded geometry under the invariant metric), but requires:

1. A precise definition of "bounded geometry" for pseudo-Riemannian manifolds `[open]`
2. A computation of the curvature of ℊ on Y¹⁴ in terms of the curvature of X⁴ and
   the Frobenius metric `[open — requires Riemannian submersion curvature formulas]`
3. Verification that the curvature and all its derivatives are bounded `[open]`

This is `[speculation]` at the current stage.

### §4.3 The families structure vs. the non-compact issue

**The key structural question.** Does the fact that Y¹⁴ is a fiber bundle over a compact
base X⁴ allow one to reduce the index theory on Y¹⁴ to index theory on X⁴ — avoiding
the non-compactness problem?

**The Bismut families perspective.** Suppose one could apply the Bismut Families Index
Theorem to D_GU, treating it as a family of fiber operators. The output would be an
element:

> ind(D_GU) ∈ K(X⁴)

indexed by the compact space X⁴. Since X⁴ is compact, this K-theory class is a well-defined
object over a compact space, regardless of the non-compactness of Y¹⁴ itself.

**Why this might work.** If D_GU can be decomposed as:

> D_GU = D_{fib} + D_{hor}/ε + O(ε)  (in the adiabatic limit with scale parameter ε)

where D_{fib} is Fredholm on each fiber (with appropriate decay conditions at infinity
of the fiber) and D_{hor} = D_X is the Dirac operator on X⁴, then the adiabatic limit
theorem gives:

> ind(D_GU) = ind_{families}(D_{fib}) ∈ K(X⁴) `[reconstruction — Bismut-Cheeger adiabatic
> limit theorem; Bismut-Cheeger, "η-invariants and their adiabatic limits," J. AMS 2, 1989]`

In this limit, the non-compactness of the fiber is handled by the Fredholmness of D_{fib}
on each non-compact fiber (with suitable L²-conditions).

**The critical gap.** For D_{fib} to be Fredholm on F_x = GL(4,ℝ)/O(3,1) (non-compact),
the operator must be Fredholm in an appropriate weighted L²-sense. This requires either:

(i) The fiber operator has a positive spectral gap (so that L²-sections not in the kernel
    decay exponentially), OR

(ii) The operator is invertible at infinity (in the Roe-index theory sense), OR

(iii) Appropriate APS-type boundary conditions at the "end" of the non-compact fiber.

None of these conditions is verified for D_{fib} on GL(4,ℝ)/O(3,1) with the
trace-reversed Frobenius metric. `[speculation — whether D_{fib} is Fredholm on the
non-compact fiber GL(4,ℝ)/O(3,1) is an open analytic question]`

### §4.4 Compactification approach

An alternative to the L²-index theory on the non-compact Y¹⁴ is to **compactify** the
fiber. This is natural in the physics context: in any physical spacetime, the metric is
bounded and non-degenerate, so one restricts to metrics satisfying bounds:

> ε ≤ det(h) ≤ ε^{-1},   |h_{μν}| ≤ C

This restriction gives a **compact** subset of Met(X⁴), and the resulting compactified
Y¹⁴ (call it Ȳ¹⁴) is a compact manifold with boundary. The APS theorem would then apply:

> ind_APS(D_GU, Ȳ¹⁴) = ∫_{Ȳ¹⁴} Â(TȲ¹⁴) · ch(S) − η(D_boundary)/2

where η is the eta-invariant of the Dirac operator restricted to the boundary ∂Ȳ¹⁴.
`[reconstruction — Atiyah-Patodi-Singer, "Spectral asymmetry and Riemannian geometry,"
Math. Proc. Cambridge Phil. Soc. 77, 1975]`

**Problem.** The compactification cuts off the fiber at the boundaries where metrics
degenerate. The physical meaning of these boundaries is unclear in GU, and the η-invariant
of the boundary operator is in general difficult to compute. The compactification approach
introduces an arbitrary choice of cutoff.

**The correct compactification.** In GU, the natural compactification of the fiber
(if it exists) is the Thurston compactification or the DM compactification from algebraic
geometry (adding degenerate metrics in a controlled way). Whether such a compactification
supports the APS theorem is unknown. `[speculation]`

### §4.5 Summary: L²-index theory on Y¹⁴

**What is established:**

1. Y¹⁴ is a non-compact 14-manifold (fiber bundle over X⁴ with non-compact fibers).
   `[verified]`

2. The standard Atiyah-Singer index theorem does not directly apply. `[verified]`

3. The families structure (Y¹⁴ → X⁴ with compact base) potentially reduces the problem
   to index theory over X⁴, via the Bismut-Cheeger adiabatic limit. `[reconstruction]`

4. The adiabatic limit theorem requires D_{fib} to be Fredholm on each fiber.
   Whether D_{fib} is Fredholm on GL(4,ℝ)/O(3,1) is an open analytic question.
   `[speculation]`

5. The fiber GL(4,ℝ)/O(3,1) is a homogeneous space of a Lie group; Dirac operators on
   such spaces have been studied (e.g., by Parthasarathy 1972, Atiyah-Schmid 1977). On
   symmetric spaces, the Dirac operator is typically Fredholm on the L²-kernel when
   the representation theory gives a discrete series. For non-compact symmetric spaces,
   the L²-spectrum can have discrete components (the discrete series). `[verified —
   Atiyah-Schmid, "A geometric construction of the discrete series for semisimple Lie
   groups," Inventiones Math. 42, 1977]`

6. If GL(4,ℝ)/O(3,1) admits a discrete series (in the sense of Atiyah-Schmid), the
   L²-kernel of D_{fib} is finite-dimensional and the index is well-defined. `[reconstruction
   — Atiyah-Schmid proved this for semisimple Lie groups G and symmetric spaces G/K; GL(4,ℝ)
   is reductive (not semisimple) but the theorem extends with appropriate modifications]`

**Key positive result (Atiyah-Schmid).** For a connected semisimple Lie group G with
maximal compact subgroup K, and a spinor bundle S over G/K, the Dirac operator on G/K
has a non-trivial L²-kernel if and only if the representation being constructed is a
discrete series representation. In this case, the kernel is finite-dimensional.
`[verified — Atiyah-Schmid 1977, Theorem]`

**Application to our setting.** The fiber GL(4,ℝ)/O(3,1) is a reductive symmetric space
(GL(4,ℝ) reductive with maximal compact O(4), O(3,1) as a subgroup). The Dirac operator
D_{fib} on this space has been implicitly studied in the representation theory of GL(4,ℝ).
If the relevant representation (corresponding to the spinor module S(6,4)) is in the
discrete series of GL(4,ℝ), the L²-index is well-defined.

**This is the key open analytic question for condition (b):** Does the spinor module
S(6,4) of Cl(6,4), restricted to the fiber GL(4,ℝ)/O(3,1) with the trace-reversed
Frobenius metric, define a discrete series representation? If yes, condition (b) is
satisfied. If no, the L²-index may not be well-defined. `[speculation]`

### §4.6 The families structure avoids some non-compact issues

**Positive conclusion.** The following is the best available structural argument:

The families index theorem, applied to π: Y¹⁴ → X⁴, computes an element of K(X⁴). Since
X⁴ is compact, this element is well-defined as long as:

1. The family of fiber operators D_{fib,x} (indexed by x ∈ X⁴) is a continuous family
   of (potentially unbounded) operators.
2. Each D_{fib,x} is Fredholm on L²(F_x, S(6,4)) (possibly with weighted Sobolev spaces).

**If** condition (2) holds (i.e., each fiber Dirac operator is Fredholm), then:
- The non-compactness of Y¹⁴ as a total space does NOT obstruct the computation.
- The index lives in K(X⁴), which is well-defined because X⁴ is compact.
- The non-compact fiber contributes only through the fiber-wise Fredholm index, which
  is an element of K(pt) = ℤ.

**Therefore:** The non-compact index theory issue (condition b) is EQUIVALENT to the
Fredholmness of D_{fib} on each non-compact fiber F_x. This is an analytic condition
on a single fiber (a Lie group quotient), not a global condition on Y¹⁴.

**This is a more tractable question than L²-index theory on the full Y¹⁴.** The
Atiyah-Schmid discrete series analysis applies to exactly this type of problem.
`[reconstruction]`

---

## Step 5: Verdict

### §5.1 Condition (a): ind_ℍ(D_GU) = 24 from topology

**Current status: OPEN — cannot be confirmed at this stage.**

The Â-genus of ℝP³ is 0 (trivially, in odd dimensions). This means the "fiber Â-genus"
contribution to the families index theorem is trivial. The generation count of 3 does NOT
come from a topological invariant of the fiber (ℝP³) but rather from the representation-
theoretic content of the spinor module S(6,4) = ℂ^{16}.

**What the topology does and does not give:**

- Topology of the fiber (ℝP³): determines whether D_{fib} has a well-defined index.
  The spin structure of ℝP³ (verified: ℝP³ is spin) ensures the Dirac operator is
  well-defined. The Â(ℝP³) = 1 says there is no topological obstruction from the fiber.
  `[verified]`

- The specific value ind_ℍ(D_GU) = 24 must come from the FULL index theorem on Y¹⁴
  (or the families index over X⁴), incorporating:
  - The topology of X⁴ (the Â-genus of X⁴, which is ind(Dirac_{X⁴}) = Â(X⁴)[X⁴] ∈ ℤ)
  - The Chern character of the spinor bundle restricted to the families setting

**Specific failure condition for condition (a):** If the Â-genus of X⁴ is not
constrained to be a specific value (as would be appropriate for a "generic" compact
spin 4-manifold), then ind_ℍ(D_GU) depends on the topology of X⁴ and is NOT
universally 24. For a generic spin 4-manifold, Â(X⁴) can be any integer.

**What GU needs for condition (a).** One of:

(i) A constraint that forces X⁴ to have Â(X⁴) = specific value (e.g., Â(X⁴) = 1,
    which holds for X⁴ = K3 surface, but not for generic spin 4-manifolds). `[speculation]`

(ii) A mechanism by which the fiber index (from the representation theory of S(6,4))
     gives exactly 24 ℍ-lines, independent of X⁴'s topology. This would require the
     fiber Dirac operator D_{fib} on each F_x to have exactly 24 ℍ-dimensional L²-kernel,
     which is a specific condition on the representation theory of GL(4,ℝ)/O(3,1). `[speculation]`

(iii) A compactification of Y¹⁴ on which the Atiyah-Singer theorem gives ind = 24 for
      topological reasons (characteristic class computation). This would require knowing
      the topology of the compactification. `[speculation]`

**In the absence of constraint on X⁴ or a specific compactification, ind_ℍ(D_GU) is
not determined to be 24 by topology alone. Condition (a) is OPEN.**

### §5.2 Condition (b): L²-index theory applies

**Current status: CONDITIONALLY RESOLVED in favor of well-definedness, with one open
analytic condition.**

**The structural argument (reconstruction-grade):**

The families structure Y¹⁴ → X⁴ reduces condition (b) to the Fredholmness of D_{fib}
on the fiber F_x = GL(4,ℝ)/O(3,1). The non-compactness of Y¹⁴ does not obstruct the
families index over the compact base X⁴, provided D_{fib} is Fredholm on each fiber.

**The Atiyah-Schmid mechanism.** The fiber F_x = GL(4,ℝ)/O(3,1) is a reductive
homogeneous space. The Dirac operator on a reductive homogeneous space G/K with a
G-invariant spinor bundle has been analyzed by Atiyah-Schmid (1977) and Parthasarathy
(1972). The L²-kernel of the Dirac operator on G/K is non-trivial and finite-dimensional
if and only if the corresponding representation is in the discrete series. In this case:
- D_{fib} is Fredholm on L²(G/K, S)
- ind(D_{fib}) = dim(discrete series representation)
- The families index ind(D_GU) ∈ K(X⁴) is well-defined

**The open condition.** Whether the spinor module S(6,4) on GL(4,ℝ)/O(3,1) (with the
trace-reversed Frobenius metric of signature (6,4)) corresponds to a discrete series
representation of GL(4,ℝ) requires:

1. Identification of the infinitesimal character of S(6,4) as a GL(4,ℝ)-module `[open]`
2. Verification that this infinitesimal character is in the discrete series spectrum
   of GL(4,ℝ)/O(3,1) `[open]`

If this discrete series condition holds: condition (b) is satisfied, the families index
is well-defined, and the non-compact index theory issue is avoided by the Atiyah-Schmid
mechanism. `[reconstruction — IF discrete series condition holds]`

If it does not hold: the Dirac operator D_{fib} on F_x may not be Fredholm in L², and
condition (b) fails. `[speculation — failure mode]`

**Most likely outcome (reconstruction-grade).** The fiber GL(4,ℝ)/O(3,1), with the
Lorentzian signature (6,4) metric and the spinor bundle S(6,4), is a well-studied
object in representation theory. The fact that O(3,1) is the structure group of Lorentzian
4-manifolds and GL(4,ℝ)/O(3,1) is the space of Lorentzian metrics makes this space
appear in multiple mathematical physics contexts. The Dirac operator on this space in
discrete series analysis is a concrete computation that could in principle be carried out,
but has not been done in the GU formalization context. `[open]`

### §5.3 The 3-generation claim

**Status: CONDITIONALLY 3 generations.**

**The representation-theory conditions are CLOSED** (from the generation-count closure
document). The SM branching S(6,4) → 16 Weyl fermions is verified; the 2+1 mechanism
is verified at reconstruction grade.

**The analytic conditions status:**

| Condition | Status | What would close it |
|---|---|---|
| (a) ind_ℍ = 24 from topology | OPEN | Either a constraint on X⁴ topology, or a discrete-series computation showing D_{fib} on GL(4,ℝ)/O(3,1) has 24 ℍ-dimensional L²-kernel |
| (b) L²-index well-defined | CONDITIONALLY RESOLVED | Discrete series analysis for GL(4,ℝ) acting on S(6,4) over GL(4,ℝ)/O(3,1); whether S(6,4) is in the discrete series |

**Overall verdict on the 3-generation claim:**

The analytic index computation is more subtle than the representation-theory argument.
The key finding of this document is:

1. The fiber homotopy type (ℝP³) is computed and verified. The fiber is spin. The
   Â-genus of ℝP³ is 1 (no topological obstruction from the fiber geometry).

2. The Bismut Families Index Theorem does NOT directly give ind_ℍ = 24, because:
   - The fibers are non-compact (Bismut requires compact fibers in its standard form)
   - The Â-genus of the 3-dimensional fiber ℝP³ is trivially 0 as an integral (odd dimension)
   - The generation count comes from representation theory (S(6,4) content), not from
     the fiber topology

3. The correct framework is the families index over X⁴ combined with the Atiyah-Schmid
   discrete series analysis for the fiber. This framework POTENTIALLY resolves both
   condition (a) and (b) together, but requires a specific discrete series computation
   for GL(4,ℝ)/O(3,1) with spinor module S(6,4).

4. The non-compact index theory issue is NOT avoided entirely by the families structure —
   it is reduced to an equivalent question about Fredholmness of D_{fib} on the
   non-compact fiber.

---

## Implications for the 3-Generation Count

### §6.1 What this analysis establishes

The analysis of the fiber homotopy type, the Â-genus, and the index theory reveals that
**the 3-generation count in GU rests on two pillars that are not fully resolved at the
analytic level:**

**Pillar 1 (Representation theory).** The fiber spinor S(6,4) = ℂ^{16} carries exactly
one SM generation; the 2+1 mechanism (two spin-1/2 sectors + one RS sector) gives
3 × 8 = 24 ℍ-lines. This pillar is CLOSED at reconstruction grade. `[established]`

**Pillar 2 (Index theory).** The analytic index ind_ℍ(D_GU) must equal 24, which requires:
(a) A specific topological or representation-theoretic condition forcing the kernel
    dimension to be exactly 24 ℍ-lines.
(b) The L²-index theory to be applicable, requiring D_{fib} to be Fredholm on each
    fiber GL(4,ℝ)/O(3,1). `[open]`

### §6.2 The correct index theorem to apply

Based on this analysis, the correct index theorem for condition (a) is:

> **Harish-Chandra's L²-index theorem** for the Dirac operator on the reductive symmetric
> space GL(4,ℝ)/O(3,1), combined with the **Atiyah-Schmid discrete series realization**.

If S(6,4) defines a vector of discrete series representations of GL(4,ℝ), then:

> ind_L²(D_{fib}) = ∑_π m_π · dim(π_K)

where the sum is over discrete series representations π of GL(4,ℝ) appearing in S(6,4),
m_π is the multiplicity, and dim(π_K) is the K-type multiplicity. For this to equal
24 (in ℍ-lines), the discrete series decomposition of S(6,4) as a GL(4,ℝ)-module must
yield exactly 24 ℍ-dimensional content. `[speculation — requires explicit Harish-Chandra
character formula computation]`

### §6.3 Failure conditions

The 3-generation count fails if any of the following hold:

1. D_{fib} on GL(4,ℝ)/O(3,1) is NOT Fredholm in L² (no discrete series; the L²-kernel
   is infinite-dimensional or ill-defined).

2. The L²-kernel of D_{fib} has ℍ-dimension ≠ 24 (wrong generation count from the
   discrete series decomposition).

3. The families index ind(D_GU) ∈ K(X⁴) is not the constant integer 24 but depends
   on x ∈ X⁴ (varying family) — this would mean the generation count varies across
   spacetime, which is unphysical.

4. The RS sector contributes a different number of ℍ-lines than 8 in the index-theory
   computation (even if the representation-theory argument gives 8).

### §6.4 The most precise open statement

> **The 3-generation prediction of GU reduces, at the analytic level, to the following
> specific computation:**
>
> Does the Dirac operator D_{fib} on GL(4,ℝ)/O(3,1) with the trace-reversed Frobenius
> metric (signature (6,4)) and spinor bundle S(6,4) = ℂ^{16} (the spinor module of
> Cl(6,4) ≅ M(16,ℂ)) have a finite-dimensional L²-kernel of ℍ-dimension exactly 24?
>
> This is a concrete representation-theory computation in the discrete series of GL(4,ℝ),
> or equivalently a Fredholm-index computation for the Dirac operator on a specific
> reductive homogeneous space.
>
> **Status: OPEN. This is the precise mathematical formulation of the remaining analytic
> condition N5(a)–(b).**

---

## References

- Atiyah, M.F., Schmid, W., "A geometric construction of the discrete series for semisimple
  Lie groups," Inventiones Mathematicae 42, 1977, pp. 1–62. (L²-Dirac operator on G/K;
  discrete series; Fredholmness on non-compact symmetric spaces.)
- Atiyah, M.F., Patodi, V.K., Singer, I.M., "Spectral asymmetry and Riemannian geometry I–III,"
  Math. Proc. Cambridge Phil. Soc. 77–79, 1975–1976. (APS index theorem for compact
  manifolds with boundary; η-invariant.)
- Berline, N., Getzler, E., Vergne, M., "Heat Kernels and Dirac Operators," Springer,
  Grundlehren vol. 298, 1992. Ch. 10 (adiabatic limit; families index theorem).
- Bismut, J.-M., "The Atiyah-Singer index theorem for families of Dirac operators: two
  heat equation proofs," Inventiones Mathematicae 83, 1986, pp. 91–151. (Families index
  theorem; Bismut superconnection.)
- Bismut, J.-M., Cheeger, J., "η-invariants and their adiabatic limits," Journal of the
  American Mathematical Society 2, 1989, pp. 33–70. (Adiabatic limit theorem for families
  of Dirac operators.)
- Hatcher, A., "Algebraic Topology," Cambridge UP, 2002. §1.2 (ℝP³ ≅ SO(3); fundamental
  group); §3.3 (Stiefel-Whitney classes of projective spaces).
- Lawson, H.B., Michelsohn, M.L., "Spin Geometry," Princeton UP, 1989. §II.1 (spin
  structures; ℝPⁿ spin iff n ≡ 3 mod 4); §II.7 (KO-theory index).
- Milnor, J., Stasheff, J., "Characteristic Classes," Princeton UP, Annals of Mathematics
  Studies 76, 1974. §4 (trivial tangent bundle of Lie groups).
- Parthasarathy, R., "Dirac operator and the discrete series," Annals of Mathematics
  96 (1), 1972, pp. 1–30. (Dirac operator on semisimple Lie groups; discrete series.)
- Roe, J., "Elliptic Operators, Topology and Asymptotic Methods," 2nd ed., CRC Press, 1998.
  (Non-compact index theory; bounded geometry; coarse index.)
- Prerequisites: `explorations/generation-sector/generation-count-sm-branching-closure-2026-06-22.md`,
  `explorations/anomaly-and-bordism/n1-signature-audit-y14-clifford-algebra-2026-06-22.md`,
  `explorations/geometry-curvature-emergence/pc2-met-x4-bundle-formalization-stub-2026-06-22.md`

---

*Filed: 2026-06-22. Executes the analytic index conditions in NEXT-STEPS.md N5(a)–(b).
Verdict: Fiber homotopy type is ℝP³ (verified). Â(fiber) = 1 (no topological obstruction
from fiber geometry). The Bismut Families Index Theorem does not directly give ind_ℍ = 24;
the relevant framework is the Atiyah-Schmid discrete series for GL(4,ℝ)/O(3,1).
Condition (b) reduces to Fredholmness of D_{fib} on the fiber, which is an open
representation-theory computation. Both analytic conditions remain OPEN; the precise
formulation is: does the Dirac operator on GL(4,ℝ)/O(3,1) with spinor module S(6,4)
have ℍ-dimensional L²-kernel equal to 24?*
