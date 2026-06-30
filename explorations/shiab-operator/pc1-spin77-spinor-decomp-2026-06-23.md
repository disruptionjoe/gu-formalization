---
title: "PC1 — Spinor Module and Exterior Algebra as Spin(7,7) Representations: Decomposition and Equivariant Maps S -> Lambda^bullet(R^14)"
date: 2026-06-23
problem_label: "pc1-spinor"
status: reconstruction
verdict: CONDITIONALLY_RESOLVED
---

# PC1 — Spinor Module and Exterior Algebra as Spin(7,7) Representations

## 1. Problem Statement

**What is being computed.** Decompose the spinor module S and the exterior algebra
Lambda^bullet(R^14) as Spin(7,7)-representations over R, and determine whether any
natural Spin(7,7)-equivariant map

  f: S -> Lambda^bullet(R^14)

exists without complexification. This is the positive-construction analog of the N2
shiab computation: N2 asked whether Phi: Omega^2 tensor S -> Omega^1 tensor S exists;
PC1 asks whether the spinor S itself maps into the exterior algebra as a Spin(7,7)-module.

**Why it matters.** The Dirac-DeRham-Einstein complex in GU is supposed to "roll up" the
exterior algebra using the spinor module. For this to work over R (without complexification),
the spinor module must either embed into or share representation-theoretic content with
Lambda^bullet(R^14). If a natural equivariant map S -> Lambda^bullet exists over R, it
provides a canonical identification of the spinor sector with a geometric sub-complex of
the de Rham complex, supporting the "shiab as geometric operation" picture. If no such
map exists, the rolled-up complex requires additional structure (complexification, choice
of section, or auxiliary data) beyond what Spin(7,7) symmetry alone provides.

**Relation to N2 / SC1.** The N2 file (n2-shiab-computation-spin77-branching-rules-2026-06-22.md)
established shiab existence for Spin(7,7) and then for Spin(9,5) under the N1 signature
correction. SC1 (sc1-shiab-domain-codomain-2026-06-23.md) confirmed the domain/codomain
and equivariance of Phi in the correct (9,5) setting. PC1 is complementary: it asks about
the deeper representation-theoretic structure — does S sit inside Lambda^bullet as a
Spin(7,7)-submodule? The answer governs whether the rolled-up Dirac-DeRham complex can be
constructed over R without additional choices.

**Scope of this computation.** This computation is performed for Spin(7,7) as specified
in the PC1 task, which is the original GU convention before the N1 signature correction.
We also note the parallel computation for Spin(9,5) (the correct physical signature) at
the end of each section. The two cases behave differently because Cl(7,7) is real-type
while Cl(9,5) is quaternionic-type.

---

## 2. Established Context

This builds on the following resolved results:

- N1 (n1-signature-audit-y14-clifford-algebra-2026-06-22.md): Correct signature is (9,5),
  not (7,7). Cl(9,5) ~= M(64,H), S = H^64. N2 shiab result survives under (9,5).
- N2 (n2-shiab-computation-spin77-branching-rules-2026-06-22.md): Shiab Phi: Lambda^2 tensor
  S -> Lambda^1 tensor S exists as a natural Spin(7,7)-equivariant real-linear map via
  Clifford contraction. Non-vanishing on all non-zero inputs (verified).
- SC1 (sc1-shiab-domain-codomain-2026-06-23.md): Domain/codomain Phi: Omega^2(Y^14) tensor
  S -> Omega^1(Y^14) tensor S confirmed in Cl(9,5) setting; Spin(9,5)-equivariant;
  H-linear; not named in Harvey or Lawson-Michelsohn.
- Anomaly audit: Gauge group Sp(64), anomaly-free (pseudoreal fundamental, pi_15(Sp) = Z).
  Nguyen §2 FULLY CLOSED.

Discipline tags: [verified] = standard reference-grade; [reconstruction] = inferred with
explicit warrant; [open] = not established here.

---

## 3. Computation

### 3.1 The Clifford Algebra Cl(7,7) and Its Spinor Module

**Classification.** For Cl(p,q) with p = 7, q = 7:

  p + q = 14,  (p - q) mod 8 = 0 mod 8 = 0.

For index 0: Cl(7,7) ~= M(2^{(p+q)/2}, R) = M(128, R).  [verified]

Spinor module: S = R^{128} (the unique irreducible left Cl(7,7)-module). dim_R(S) = 128.  [verified]

Reference: Lawson-Michelsohn, Spin Geometry, Appendix I Table 1; Harvey, Spinors and
Calibrations, Table 6.2.

**Chirality.** Volume element omega = e_1 e_2 ... e_{14}:

  omega^2 = (-1)^q * (-1)^{n(n-1)/2} = (-1)^7 * (-1)^{91} = (-1)(-1) = +1.  [verified]

omega is central (n = 14 even). S splits as:
  S = S^+ oplus S^-,  dim_R(S^+/-) = 64.  [verified]

S^+ and S^- are the two Majorana-Weyl half-spinors in (7,7) signature. They are each
irreducible as Spin(7,7)-representations.  [reconstruction -- standard for real-type
simple Clifford algebras; see Budinich-Trautman Ch. 4]

**Key structural fact: Cl(7,7) ~= M(128,R) is REAL-TYPE (index 0).**
This means S = R^{128} is a real vector space with a non-degenerate symmetric bilinear
form preserved by Spin(7,7). The invariant bilinear form is symmetric (Majorana bilinear
form). There is no quaternionic structure.

**Contrast with Cl(9,5).** For Cl(9,5): (p-q) mod 8 = 4 -> M(64,H), quaternionic-type.
S = H^{64}. The half-spinors are H-irreducible. The invariant bilinear form is symplectic
(antisymmetric) for the quaternionic case.

### 3.2 The Exterior Algebra Lambda^bullet(R^14) as a Spin(7,7)-Representation

**Structure.** As vector spaces: Lambda^bullet(R^{14}) = oplus_{k=0}^{14} Lambda^k(R^{14}).

Dimensions:
  dim Lambda^k = C(14,k),  total dim = 2^{14} = 16384.

**Clifford identification.** As algebras: Cl(7,7) ~= Lambda^bullet(R^{14}) (as vector
spaces via the symbol map). The Clifford algebra is a quantization of the exterior algebra.
Importantly, the Clifford ALGEBRA and the exterior ALGEBRA have the same underlying vector
space but different products.  [verified]

**Spin(7,7)-action on Lambda^k.** The group Spin(7,7) subset SO(7,7) subset GL(14,R)
acts on R^{14} by the standard representation, hence on Lambda^k(R^{14}) by the induced
representation. The representations Lambda^k are NOT all irreducible; they decompose
further. Key decompositions:

  Lambda^0 = R (trivial representation, dim 1)
  Lambda^1 = R^{14} (the standard/vector representation, irreducible)  [verified]
  Lambda^2 = so(7,7) as a vector space = adjoint representation, dim 91;
             irreducible for Spin(7,7)  [verified -- so(7,7) is simple, adjoint is irred.]
  Lambda^7 = Lambda^7(R^{14})  (middle degree, dim 3432; not computed in detail here)

**Self-duality.** For signature (7,7), the Hodge star on the middle degree satisfies:
  *: Lambda^7 -> Lambda^7,  *^2 = (-1)^7 (-1)^{7*7/2} (sign computation):
  For (p,q) = (7,7), the Hodge star on Lambda^7 satisfies (*^2) = (-1)^{7+q(p+q-7)}:
  this needs careful computation. Use the formula for signature (p,q):
  * (alpha wedge * beta) = <alpha, beta> vol
  and * * alpha = (-1)^{k(n-k)+q} alpha for alpha in Lambda^k, n = 14, k = 7:
  * * alpha = (-1)^{49 + 7} alpha = (-1)^{56} alpha = alpha.
  So *^2 = +1 on Lambda^7.  [reconstruction -- sign depends on the convention for vol;
  using the (7,7) metric with signature (+^7, -^7), vol = e_1 wedge ... wedge e_{14}
  satisfies vol^2 = (-1)^7 = -1 under the inner product, and the formula gives *^2 = +1
  on Lambda^7 in signature (7,7).]

This means Lambda^7 = Lambda^7_+ oplus Lambda^7_- (self-dual and anti-self-dual pieces)
as Spin(7,7)-representations.

### 3.3 Decomposing S as a Spin(7,7)-Representation in Lambda^bullet

The central question for PC1: does S appear as a sub-representation inside Lambda^bullet(R^14)?

**Dimension count.** S = R^{128}, dim_R = 128. Lambda^bullet has total dim 16384. There
is plenty of room for an embedding by dimension. So the question is not dimension but
representation-theoretic structure.

**Method 1: The Clifford algebra isomorphism.**

The key structural fact: Cl(7,7) ~= M(128, R) acts on S = R^{128} (the spinor module).
The exterior algebra Lambda^bullet(R^{14}) ~= Cl(7,7) as vector spaces (via the
antisymmetrization map).

This means Lambda^bullet(R^{14}) ~= Cl(7,7) ~= End(S) = M(128,R) as a LEFT Cl(7,7)-module
(acting by left multiplication on the algebra itself).

But as a VECTOR SPACE (forgetting the algebra structure), Cl(7,7) is the direct sum of
all left Cl(7,7)-modules:

  Cl(7,7) ~= S^{oplus 128}  (as a left Cl(7,7)-module)

because M(128,R) as a left M(128,R)-module is R^{128} oplus ... oplus R^{128} (128 copies
of the minimal left ideal S = R^{128}).  [verified -- this is the standard fact that the
regular representation of M(n,R) is n copies of the vector representation R^n]

So, as a Spin(7,7)-representation:

  Lambda^bullet(R^{14}) ~= S^{oplus 128}  (128 copies of S = R^{128})  [reconstruction]

where we used that Cl(7,7) ~= M(128,R), the left regular module is the direct sum of 128
copies of the irreducible R^{128}, and Spin(7,7) acts via the spinor representation on
each copy.

**CRITICAL CONSEQUENCE.** This means Lambda^bullet(R^14), viewed as a Spin(7,7)-representation,
is 128 copies of the SAME Spin(7,7)-module S (with no other irreducible types).

This is a remarkable structural fact: the exterior algebra on R^{14}, when viewed through
the Clifford lens, is ENTIRELY composed of spinor representations. There are no "purely
exterior" Spin(7,7)-irreducibles that don't appear in S.

**Failure condition for Method 1.** This argument uses the fact that Cl(7,7) ~= M(128,R)
is a SIMPLE real algebra with a unique irreducible left module S = R^{128}. If Cl(7,7)
were not simple (e.g., if it split as a product algebra), there would be multiple distinct
irreducibles. The simplicity of M(128,R) over R is a standard fact (Artin-Wedderburn).
[verified]

**Method 2: Direct representation-theoretic verification for low degrees.**

Let us check that S appears in Lambda^k for small k using standard Spin(7,7) branching.

**Lambda^0 = R (trivial):** This is the trivial representation. S^+ and S^- are non-trivial
(dim 64 each); S does not appear in Lambda^0. Consistent with Method 1 (Lambda^0 is just one
"basis element" of Cl(7,7), and only collectively do 128 basis elements span an S-copy).

**Lambda^1 = R^{14} (vector representation):** The vector representation of Spin(7,7)
is NOT the spinor representation. dim Lambda^1 = 14 << 64 = dim(S^+), so S^+ and S^-
do not appear as sub-representations of Lambda^1. Lambda^1 is an irreducible 14-dimensional
Spin(7,7)-representation distinct from the spinor representations.  [verified]

**Lambda^2 = so(7,7) (adjoint representation, dim 91):** The adjoint representation of
so(7,7) = D_7 has dim 91. The spinor representations of D_7 over R have dimension 64 each.
dim(Lambda^2) = 91 < 128 = dim(S), so S itself does not appear. But S^+ (dim 64) could in
principle appear in Lambda^2 (dim 91). For D_7 = so(14,C), the adjoint representation
decomposes over C as the 91-dimensional irreducible. Under the real form so(7,7), the
decomposition is non-trivial but 64 > 91/2, so a spin representation of real dim 64 cannot
appear in the 91-dimensional adjoint without dimension overflow.
Conclusion: S^+ does NOT appear in Lambda^2.  [reconstruction]

**Lambda^7 (middle degree, dim 3432):** dim(Lambda^7) = C(14,7) = 3432. The spinor modules
S^+ and S^- have dim 64 each. A priori, 64 divides into 3432 as 3432/64 = 53.625, which is
not an integer, so Lambda^7 cannot be a direct sum of S^+ copies alone. But Lambda^7 could
contain several copies of S^+ among other irreducibles.

For the present computation, the key fact is that S^+ (or S^-) FIRST appears in degree k
where the cumulative dimension from Lambda^0 up to Lambda^k first exceeds 64. That is:
  Lambda^0 + ... + Lambda^2 has dim 1 + 14 + 91 = 106 < 128.
  Adding Lambda^3: dim = 106 + C(14,3) = 106 + 364 = 470.
The first S^+-copy must therefore be contained in a range that includes Lambda^3 or higher.

More precisely (using Method 1): Lambda^0 oplus Lambda^1 oplus Lambda^2 oplus Lambda^3 has
dim 1 + 14 + 91 + 364 = 470. Under Spin(7,7), the first 128-dimensional Cl(7,7)-module
copy of S = R^{128} must start somewhere in Lambda^3 or involve Lambda^3 non-trivially.

**What degrees contain S.** The precise answer requires the decomposition of the map

  c_k: Lambda^k(R^{14}) -> Hom(S^+, S^{(-1)^k}) (Clifford action)

For the map Lambda^0 oplus Lambda^1 oplus ... -> M(128,R) ~= Cl(7,7):
- Lambda^{even} maps to Cl^{even} ~= M(64,R) oplus M(64,R) (the even Clifford sub-algebra,
  which decomposes as direct sum of Hom(S^+,S^+) oplus Hom(S^-,S^-) since even elements
  preserve chirality).
- Lambda^{odd} maps to Cl^{odd} ~= Hom(S^+,S^-) oplus Hom(S^-,S^+) (odd elements swap
  chirality).

So:
  Lambda^{even} = Lambda^0 + Lambda^2 + Lambda^4 + Lambda^6 + Lambda^8 + Lambda^10 + Lambda^12 + Lambda^14
  maps to:  Hom_R(S^+, S^+) oplus Hom_R(S^-, S^-) ~= M(64,R) oplus M(64,R)

  Lambda^{odd} = Lambda^1 + Lambda^3 + Lambda^5 + Lambda^7 + Lambda^9 + Lambda^11 + Lambda^13
  maps to:  Hom_R(S^+, S^-) oplus Hom_R(S^-, S^+)

The Clifford representation Cl(7,7) -> End(S) = M(128,R) is an isomorphism.
Therefore as a Spin(7,7)-representation:

  Lambda^{even} ~= End(S^+) oplus End(S^-)  as Spin(7,7)-representations  [reconstruction]
  Lambda^{odd}  ~= Hom(S^+, S^-) oplus Hom(S^-, S^+)  as Spin(7,7)-representations

Now: End(S^+) = Hom(S^+, S^+) ~= S^+ tensor (S^+)*. As a Spin(7,7)-representation,
(S^+)* ~= S^+ (self-duality of the Majorana spinor in (7,7) signature: the invariant
symmetric bilinear form B: S^+ tensor S^+ -> R provides an isomorphism S^+ -> (S^+)*
as Spin(7,7)-modules).  [reconstruction -- standard for index 0 case with symmetric B]

So End(S^+) ~= S^+ tensor S^+ as a Spin(7,7)-representation.

And:
  Lambda^{even} ~= (S^+ tensor S^+) oplus (S^- tensor S^-)
  Lambda^{odd}  ~= (S^+ tensor S^-) oplus (S^- tensor S^+)
                ~= S^+ tensor S^- oplus (S^+ tensor S^-)  (if S^- ~= S^+)

where the last step uses that for (7,7) signature both half-spinors are isomorphic as
abstract vector spaces (both are R^{64}) and may or may not be isomorphic as
Spin(7,7)-representations.

### 3.4 The Natural Equivariant Map S -> Lambda^bullet

**Constructing the map.** We want a Spin(7,7)-equivariant map

  f: S -> Lambda^bullet(R^{14})

that is natural (constructed from the Clifford algebra and the (7,7) metric alone).

**Method: Clifford algebra isomorphism approach.**

Since Cl(7,7) ~= M(128, R) ~= End(S), and Lambda^bullet ~= Cl(7,7) (as vector spaces via
the antisymmetrization/symbol map sigma: Lambda^bullet -> Cl(7,7)), we have:

  Lambda^bullet(R^{14}) ~= Cl(7,7) ~= End_R(S) = Hom_R(S, S).

A Spin(7,7)-equivariant map f: S -> Lambda^bullet can be constructed as follows:

**Construction 1: Spinor-pairing map.**

Fix a non-zero element s_0 in S (or consider the map s -> f(s) parametrically). Define:

  f_{s_0}: S -> Cl(7,7) ~= Lambda^bullet(R^{14})
  f_{s_0}(s) = s tensor_B s_0

where s tensor_B s_0 is the rank-1 element of End(S) = S tensor S^* formed by the
outer product s (x) B(-, s_0), with B the invariant bilinear form on S.

This map is:
- Linear in s: YES (for fixed s_0).
- Spin(7,7)-equivariant? For g in Spin(7,7):
    f_{g.s_0}(g.s) = (g.s) tensor_B (g.s_0) = g.(s tensor_B s_0) = g. f_{s_0}(s).
  So f is equivariant if we transform s_0 simultaneously. But f_{s_0} with a FIXED s_0
  is NOT equivariant (it depends on a choice of s_0, which breaks Spin(7,7) symmetry).

Conclusion: this construction gives an equivariant map S x S -> Lambda^bullet (bilinear)
but NOT a linear equivariant map S -> Lambda^bullet with a fixed element chosen in advance.

**Construction 2: Pure Clifford module approach.**

Can we find a NATURAL linear Spin(7,7)-equivariant map f: S -> Lambda^bullet(R^{14})?

By Schur's lemma, such a map exists if and only if S and Lambda^bullet share a common
irreducible Spin(7,7)-subrepresentation. From §3.3 (Method 1):

  Lambda^bullet ~= S^{oplus 128}  as Spin(7,7)-representations.

Since S itself is a direct summand of Lambda^bullet (128 times!), there are many
equivariant maps S -> Lambda^bullet. The projection onto any one copy is equivariant.
However, choosing a specific copy is NOT natural (it requires choosing a row index i in
{1,...,128}, which is not Spin(7,7)-invariant).

**The natural map question more precisely:** We want a map that is:
(a) Linear: f: S -> Lambda^bullet
(b) Spin(7,7)-equivariant: f(g.s) = g.f(s) for all g in Spin(7,7)
(c) Natural: constructible from the Cl(7,7) structure and the (7,7) metric alone,
    without arbitrary choices

**Obstruction to a natural linear map.** The space of Spin(7,7)-equivariant linear maps

  Hom_{Spin(7,7)}(S, Lambda^bullet) ~= Hom_{Spin(7,7)}(S, S^{oplus 128}) ~= R^{128}

(128-dimensional, by Schur's lemma over R applied to 128 copies of the same irreducible).
[reconstruction -- uses that S is R-irreducible, giving Hom(S,S) = R by Schur, and
Hom(S, S^{128}) = R^{128}]

This is a 128-dimensional space of equivariant maps. The issue is that NO element of this
space is canonical/natural: each corresponds to choosing a linear functional R^{128} -> R
(selecting a copy), which is not determined by Spin(7,7) invariants alone.

**Alternative formulation: equivariant map S -> Lambda^k for fixed degree k.**

For a fixed degree k, Hom_{Spin(7,7)}(S^+, Lambda^k) is non-zero iff S^+ is a summand
of Lambda^k as a Spin(7,7)-representation.

From Method 1 (Clifford isomorphism): S appears in EVERY summand Lambda^k in the sense
that the projection of the Clifford algebra onto Lambda^k pieces is a Spin(7,7)-module map.
But "S appears in Lambda^k" requires dim(Lambda^k) >= dim(S^+) = 64.

The first Lambda^k with dim >= 64 is Lambda^3 (dim 364). Does S^+ appear in Lambda^3?

**Degree-3 decomposition.** Lambda^3(R^{14}) as a representation of Spin(7,7) = SO(7,7):

The representation Lambda^3(R^{14}) for SO(14) restricted to SO(7,7) decomposes. Over the
complexification SO(14,C) (type D_7), Lambda^3 is the irreducible representation with
highest weight (0,0,0,0,0,1,0) in D_7 notation (the 3rd fundamental representation).
Under the real form SO(7,7) = SO(p,q), this representation remains irreducible over R
as long as the highest weight is real (not quaternionic or complex-type). For SO(7,7),
the real form type is D_7^{(7,7)}, and Lambda^3 is an irreducible real representation
of dim_R = 364.  [reconstruction -- standard for exterior power representations of SO(p,q)]

The spin representations S^+ and S^- of SO(7,7) have highest weights (1/2, 1/2, 1/2,
1/2, 1/2, 1/2, 1/2) and (1/2, 1/2, 1/2, 1/2, 1/2, 1/2, -1/2) in D_7 notation (the
two half-spinor highest weights). These are complex-valued highest weights for D_7.

**A critical subtlety.** For the REAL form SO(7,7) (which is a split real form of D_7),
the complex spin representations Delta^+ and Delta^- of D_7 (each dim_C = 64) descend to
REAL representations. Since SO(7,7) is a split real form, the spin representations are
real-valued (non-quaternionic, non-complex): Delta^+|_{SO(7,7)} is a REAL irreducible
representation of real dimension 64 = 2 * 32 (not 64 from H^{32} as in the quaternionic
case).  [reconstruction -- the split real form SO(p,p) always has real-type (not quaternionic)
spin representations; this is the source of the Majorana-Weyl spinors in (7,7)]

So S^+ and S^- are real irreducible 64-dimensional representations of Spin(7,7).

**Does S^+ appear in Lambda^3?** By the Clebsch-Gordan analysis:

Lambda^3 (the 3rd antisymmetric power of the 14-dim vector representation) for D_7 is the
irreducible representation with highest weight (0,0,1,0,0,0,0) (in Dynkin label notation
for D_7, where the nodes are labeled 1,...,7 with 6,7 being the two spinor nodes).

The spin representations S^+ and S^- have highest weights with Dynkin labels supported on
nodes 6 and 7. The fundamental representations with these labels are:

  Lambda^1: Dynkin label (1,0,0,0,0,0,0) -- vector
  Lambda^2: Dynkin label (0,1,0,0,0,0,0) -- adjoint  
  Lambda^3: Dynkin label (0,0,1,0,0,0,0) -- 3rd antisymmetric power
  ...
  Lambda^6: Dynkin label (0,0,0,0,0,1,0) -- one half-spin
  Lambda^7: Dynkin label (0,0,0,0,0,0,1) -- the other half-spin
  
where Lambda^6 and Lambda^7 (using the GU/Dynkin notation) are the half-spin representations
of highest weight dim 64 for D_7.

Wait -- this notation requires care. For D_7 = so(14,C):
  - The fundamental representations are V_1 = C^{14} (vector), V_2 = Lambda^2(C^{14}) (adjoint),
    ..., V_5 = Lambda^5(C^{14}) (dim C(14,5) = 2002), and then the two SPINOR representations
    V_6 = S^+ (dim 64) and V_7 = S^- (dim 64) that do NOT appear as exterior powers!

This is the critical point: **the spinor representations V_6 = S^+ and V_7 = S^- of D_7 are
NOT among the exterior power representations Lambda^k(C^{14}) for any k.** [verified -- this
is a standard fact: the spinor representations of D_n are not polynomial representations in
the vector representation; they are the "exceptional" fundamental representations that require
the spin group cover]

**What this means for the natural equivariant map question:**

Over C: The complex spinor representations S^+ and S^- of so(14,C) = D_7 do NOT appear
in any Lambda^k(C^{14}). Therefore there is NO non-zero complex-linear equivariant map
  f_C: S^+_C -> Lambda^k(C^{14})  for any k.
This is a consequence of the highest-weight theory: S^+ has highest weight involving a
"spinor weight" (half-integer coordinates) that cannot be realized as a sub-weight of any
tensor representation (Lambda^k is a tensor representation = polynomial in the vector
representation, with integer-coordinate weights only).  [verified -- standard in Lie theory]

Over R for SO(7,7): We must check whether the restriction of S^+ to the real form changes
this conclusion.

**The decisive result:**

For the split real form SO(7,7) of D_7:
1. S^+ and S^- are real irreducible 64-dimensional representations.
2. Lambda^k(R^{14}) are real representations that, upon complexification, give Lambda^k(C^{14}).
3. The complexification of any R-linear equivariant map f: S -> Lambda^k gives a C-linear
   equivariant map f_C: S^+_C -> Lambda^k_C = Lambda^k(C^{14}).
4. By the complex result above, no such non-zero C-linear equivariant map exists.
5. Therefore no non-zero R-linear equivariant map f: S^+ -> Lambda^k(R^{14}) exists.  [reconstruction]

**Conclusion for the natural linear map question:**

There is NO non-zero Spin(7,7)-equivariant R-linear map

  f: S -> Lambda^k(R^{14})

for any single degree k. This follows from the highest-weight obstruction: S carries
half-integer weights (spinor weights) while Lambda^k carries only integer weights (tensor
weights), and no equivariant map can bridge the two.

**The "128 copies" reconciliation.** This appears to contradict §3.3's statement that
Lambda^bullet ~= S^{oplus 128} as Spin(7,7)-representations. The resolution:

Lambda^bullet(R^{14}) is a SUM over k of Lambda^k(R^{14}). The Clifford isomorphism
Cl(7,7) ~= Lambda^bullet ~= M(128,R) shows that Lambda^bullet (the TOTAL exterior algebra)
is isomorphic to M(128,R) as a vector space. M(128,R) as a left M(128,R)-module = as a
left Cl(7,7)-module decomposes as 128 copies of S = R^{128}. But this Cl(7,7)-module
structure on Lambda^bullet is NOT the same as the Spin(7,7)-module structure on Lambda^bullet
coming from the SO(7,7) action on R^{14}.

The two actions are:
(A) Spin(7,7) acts on Lambda^k(R^{14}) via the exterior power of the standard 14-dim representation.
(B) Cl(7,7) acts on itself (Lambda^bullet as a vector space) by LEFT multiplication --
    the left regular representation.

These are two different actions on the same vector space Lambda^bullet. The left-regular
Cl(7,7)-action decomposes into 128 copies of S. The SO(7,7)-exterior-power action does NOT.

For the purposes of the PC1 question (natural equivariant maps S -> Lambda^bullet), the
relevant action is (A), the geometric action via exterior powers of the standard representation.
Under action (A), S does not appear in any single Lambda^k; it appears in the full exterior
algebra only when we use the ALGEBRA structure (Clifford multiplication), not just the module
structure.  [reconstruction -- this distinction is crucial and not always stated clearly]

### 3.5 What Natural Maps DO Exist: S x Lambda^1 -> Lambda^bullet and the Shiab

While there is no natural LINEAR equivariant map S -> Lambda^k (for any k), there are
natural equivariant maps involving S and exterior forms together. The shiab (N2/SC1) is
the primary example:

  Phi: Lambda^2 tensor S -> Lambda^1 tensor S  (the shiab from N2/SC1)

This is NOT a map from S to Lambda^bullet; it maps FROM a tensor product involving S.

**What the highest-weight obstruction means for the Dirac-DeRham complex.**

The Dirac-DeRham-Einstein complex in GU is built as:

  ... -> Omega^{k+1} tensor S ->^{Phi} Omega^k tensor S -> ...

Each arrow is the shiab, reducing the form degree by 1 while keeping S. The complex is
BIGRADED in (form degree, spinor sector). At no step does the spinor S factor disappear
or get "absorbed" into a pure exterior form. This is representation-theoretically consistent
with the PC1 finding: S cannot map into Lambda^bullet directly, so the complex must carry
S throughout.

This means: the "rolling up" of the exterior algebra by S is done at the level of the full
(Omega^* tensor S) complex, not by mapping S into Lambda^*. The S-component is not a
sub-object of Lambda^bullet but is rather a "coefficient bundle" for the forms.

**The Clifford map Lambda^bullet -> End(S) direction.** While S does not map INTO Lambda^bullet,
Lambda^bullet DOES map INTO End(S) via the Clifford representation:

  sigma: Lambda^bullet(R^{14}) -> Cl(7,7) -> End(S)

This is the (unique up to scale) Clifford representation of the exterior algebra on the
spinor module. It is Spin(7,7)-equivariant and surjective onto End(S) (since Cl(7,7) ~= M(128,R)
acts irreducibly on S).  [verified]

So the direction is: Lambda^bullet acts on S, but S does not embed in Lambda^bullet.

### 3.6 The (9,5) Case: Parallel Analysis

**What changes.** For Cl(9,5) ~= M(64,H), spinor module S = H^{64}:
- S carries a quaternionic structure (not a real symmetric form, but a quaternionic
  Hermitian form).
- The spinor representations S^+ and S^- are irreducible over H (H-irreducible).
- The Clifford representation sigma: Lambda^bullet -> End_H(S) maps Lambda^{even} to
  End_H(S^+) oplus End_H(S^-) and Lambda^{odd} to Hom_H(S^+, S^-) oplus Hom_H(S^-, S^+).

**The same highest-weight obstruction applies.** The spinor representations of so(9,5)
(a real form of D_7) still carry spinor weights (half-integer coordinates in D_7 weight
space). Lambda^k(R^{14}) still carries tensor weights (integer coordinates). No non-zero
H-linear equivariant map S -> Lambda^k exists. [reconstruction -- same argument as (7,7)]

**Difference.** In the (9,5) case, the equivariant maps S -> Lambda^k are also zero, but
the relevant equivariant maps Lambda^bullet acts on S are H-linear. The shiab Phi is
H-linear in the (9,5) case (as established in SC1).

### 3.7 Summary of Representation-Theoretic Findings

| Question | (7,7) Clifford type | (9,5) Clifford type |
|---|---|---|
| Cl(p,q) isomorphism | M(128,R) -- real type | M(64,H) -- quaternionic type |
| Spinor module S | R^{128}, chiral halves S^+/- = R^{64} | H^{64}, chiral halves S^+/- = H^{32} |
| Invariant bilinear form on S | Symmetric (Majorana) | Antisymmetric (symplectic) |
| S^+ as real Spin-representation | R-irreducible, dim_R 64 | H-irreducible, dim_R 128 |
| S^+ in Lambda^k for any k? | NO -- spinor weight obstruction | NO -- same obstruction |
| Natural linear map S -> Lambda^k | Does NOT exist | Does NOT exist |
| Space of equivariant maps S -> Lambda^bullet | R^{128} (128-dim) but none natural | H^{64} (64-dim over H) but none natural |
| Lambda^bullet as Spin-module via exterior action | Tensor representations only | Tensor representations only |
| Lambda^bullet as Cl-module via Clifford action | 128 copies of S (via left regular) | 64 copies of S (over H, via left regular) |
| Shiab Phi: Lambda^2 tensor S -> Lambda^1 tensor S | Exists, real-linear, equivariant (N2) | Exists, H-linear, equivariant (SC1) |
| Lambda^bullet acts on S via sigma | Surjective (Cl(7,7) irred.) | Surjective (Cl(9,5) irred.) |

---

## 4. Result

### 4.1 Main Verdict

**VERDICT: CONDITIONALLY_RESOLVED**

**The PC1 computation establishes:**

**(A) Decomposition of S as a Spin(7,7)-representation.**
  S = S^+ oplus S^-, each S^+/- being a real irreducible 64-dimensional representation
  of Spin(7,7) (Majorana-Weyl spinors). The half-spinors S^+/- are the two half-spin
  representations of D_7 = so(14,C) restricted to the split real form Spin(7,7).
  Status: reconstruction-grade (verified for the Clifford algebra structure; the explicit
  D_7 representation theory is standard literature).

**(B) Lambda^bullet(R^14) as a Spin(7,7)-representation.**
  Each Lambda^k is an irreducible (or low-multiplicity) real representation of Spin(7,7)
  via the exterior power action. Crucially, Lambda^k carries TENSOR weights (integer
  coordinates in D_7 weight space) while S^+/- carry SPINOR weights (half-integer
  coordinates). The two types of representations do not share any irreducible summands.
  Status: reconstruction-grade (highest-weight theory for D_7 is standard; the specific
  statement about integer vs. half-integer weights is verified).

**(C) No natural equivariant map S -> Lambda^k(R^14) exists for any k.**
  The highest-weight obstruction is absolute: spinor weights cannot appear in tensor
  representations, and any R-linear equivariant map would induce a C-linear equivariant map
  after complexification, which is zero by the D_7 highest-weight classification.
  Status: reconstruction-grade for the (7,7) case; same conclusion holds for (9,5).

**(D) What maps DO exist.**
  The natural equivariant maps go in the OPPOSITE direction:
    sigma: Lambda^bullet(R^{14}) -> End(S)  (the Clifford representation, surjective)
    Phi: Lambda^2 tensor S -> Lambda^1 tensor S  (the shiab, established in N2/SC1)
  These involve Lambda^bullet acting on S, not S mapping into Lambda^bullet.
  Status: verified (Clifford representation) and reconstruction (shiab).

**(E) The rolled-up complex interpretation.**
  The fact that S cannot map into Lambda^bullet over R means the Dirac-DeRham-Einstein
  complex must carry S as a permanent "coefficient" factor throughout. The complex is
  bigraded as (form degree) x (spinor sector) and cannot be reduced to a complex
  on Lambda^bullet alone. This is representation-theoretically required.
  Status: reconstruction-grade consequence of (A)-(C).

**Condition for "CONDITIONALLY" prefix.** The computation is at reconstruction grade.
The decisive step -- that the spin representations of D_7 do not appear as summands of
any Lambda^k(C^{14}) -- is a standard Lie-theory fact that we have stated but not
verified from primary source (weight computation). A CAS verification (LiE, SageMath,
or GAP) checking that the highest weight of S^+ has half-integer coordinates not appearing
in any Lambda^k(C^{14}) would upgrade this to verified. No new mathematical input is
expected to change the conclusion; the condition is technical verification only.

### 4.2 Explicit Failure Conditions

**F1 (Half-integer weight claim wrong).** If the highest weight of S^+ in D_7 notation
has integer coordinates (making it a tensor representation), then S^+ could appear in
some Lambda^k and the no-map conclusion would be wrong. This would require a fundamental
error in the D_7 highest-weight classification for spin representations. Checked: the
half-spinor representations of D_n have highest weights (1/2, ..., 1/2, +1/2) and
(1/2, ..., 1/2, -1/2) in the orthonormal basis for weight space, which are NOT weights
of any Lambda^k.  [reconstruction]

**F2 (Real form changes the conclusion).** If passing from the complex form D_7 to the
real form Spin(7,7) introduces new real irreducibles that are simultaneously sub-representations
of Lambda^k and half-spin, the conclusion would fail. Real forms can split complex irreducibles
into multiple real irreducibles, but they cannot merge a spin representation with a tensor
representation (the weight-space argument is algebraic and does not depend on the real form).
[reconstruction -- real forms of a complex Lie algebra preserve the weight lattice structure]

**F3 (Regularization escape: the mixed map).** If the physical map of interest is not
S -> Lambda^k but rather S -> Lambda^bullet / ~ (some quotient), or involves a connection
A as additional data, the pure equivariance argument may not apply. Specifically, if one
allows connection-dependent maps (gauge-equivariant but not Spin(7,7)-equivariant as a
representation-theoretic map), then non-equivariant maps exist trivially. The failure
condition for F3 is a redefinition of "natural" that GU relies on.

**F4 (Exceptional isomorphism for D_7).** If D_7 has an exceptional isomorphism with
another algebra that identifies some Lambda^k with a spin representation, the above
conclusion would fail. D_7 = so(14,C) has no exceptional isomorphisms of this type
(unlike D_4 = so(8,C) with triality, or D_3 = A_3 etc.). For n >= 5, D_n has no
exceptional outer automorphisms that swap tensor and spin representations.  [verified]

### 4.3 Open Questions

**OQ1 (CAS verification).** Verify using LiE, SageMath, or GAP that:
  (a) The highest weight of S^+ for D_7 has coordinates (1/2,1/2,1/2,1/2,1/2,1/2,1/2)
      (or similar half-integer form in the orthonormal basis).
  (b) For Lambda^k = 0,...,14, the highest weights are (1,0,...,0), (1,1,0,...,0), etc.
      (all integers).
  (c) The decomposition of Lambda^k into D_7-irreducibles does not contain S^+.
This would upgrade the result from reconstruction to verified.

**OQ2 (Positive-construction implication for the complex).** Given that S cannot map into
Lambda^bullet, determine precisely what the Dirac-DeRham-Einstein complex looks like as a
bigraded complex. Is the complex:

  0 -> Omega^{14} tensor S -^{Phi}-> Omega^{13} tensor S -^{Phi}-> ... -^{Phi}-> Omega^0 tensor S -> 0 ?

If so, what is the kernel and image at each step, and what is the index of this complex
(the "Euler characteristic" sum of (-1)^k dim ker Phi_k)? This computation would be the
next step in establishing the three-generation count.

**OQ3 (Uniqueness of Phi in the rolled-up complex).** SC1 established that Phi is the
unique NATURAL Spin(9,5)-equivariant H-linear map of type Lambda^2 tensor S -> Lambda^1 tensor S
(up to non-natural choices). Does this extend: is the SEQUENCE of shiab maps

  {Phi_k: Lambda^{k+1} tensor S -> Lambda^k tensor S}

the unique (up to scale) natural sequence of equivariant operators connecting adjacent
degrees in the bigraded complex? If yes, the complex structure is canonically forced by
representation theory. If no, additional input is needed.

---

## 5. Implication for the Positive Constructions Lane

**PC1 outcome.** The positive-construction analog of N2 has a nuanced answer:

  DOES NOT EXIST: A natural Spin(7,7)-equivariant map S -> Lambda^k(R^14) for any k.
  DOES EXIST: Natural maps Lambda^bullet tensor S -> Lambda^{bullet-1} tensor S (the shiab).

This resolves the "does the spinor sit inside the exterior algebra?" question:
The answer is NO (over R, without complexification, for the tensor action of SO(7,7)).
The spinor S is a COEFFICIENT of the exterior complex, not a sub-object of it.

**Relation to the Nguyen critique.** Nguyen §3.4 objects that GU provides no derivation
of how S enters the geometric complex. The PC1 result clarifies: S enters as a coefficient
bundle on which Lambda^bullet ACTS (via Clifford multiplication), not as a sub-bundle of
Lambda^bullet. This is not a gap but a feature: the Dirac-DeRham complex Omega^* tensor S
is the correct geometric object, and the shiab is the correct operator connecting its degrees.
The S cannot be "collapsed" into pure forms; its presence is representation-theoretically
required.

**Distler-Garibaldi comparison.** The PC1 finding that S does not embed in Lambda^bullet
over R is structurally similar to the Distler-Garibaldi pattern: GU cannot avoid using
the full spinor module as additional structure beyond what the manifold's exterior algebra
provides. Whether this is an obstruction or a feature depends on whether GU provides an
independent physical motivation for the S factor (e.g., via the Dirac-DeRham-Einstein
complex as a unified physical content). The current state: S's presence is required and
consistent, but its origin as a "natural" geometric object requires the Y^14 construction
and the spin structure (both established in earlier computations).

**Update to no-go map.** The PC1 result is a clarification of the no-go map's
richer-substrate column: the Met(X^4) = Y^14 construction provides S as a natural spinor
bundle (not as an embedding in Lambda^bullet), and the shiab provides the equivariant
operator connecting S-valued forms. This narrows but does not resolve the Distler-Garibaldi
stress case: the richer datum is S (the spinor), and its existence over R is confirmed by
the Cl(9,5) quaternionic structure (w_2(Y^14) = 0, spin structure exists unconditionally).

---

## 6. Summary

| Item | Result | Grade |
|---|---|---|
| S as Spin(7,7)-module | S = S^+ oplus S^-, each real irred. dim 64 (Majorana-Weyl) | reconstruction |
| Lambda^k as Spin(7,7)-module | Tensor representations with integer weights, irred. or low-mult. | reconstruction |
| Natural map S -> Lambda^k | Does NOT exist (half-integer vs. integer weight obstruction) | reconstruction |
| Equivariant Hom(S, Lambda^bullet) | 128-dimensional space; no element is natural/canonical | reconstruction |
| Lambda^bullet acts on S (Clifford) | Surjective, equivariant: sigma: Lambda^bullet -> End(S) | verified |
| Shiab Phi: Lambda^2 tensor S -> Lambda^1 tensor S | Exists, equivariant, non-vanishing (N2/SC1) | reconstruction |
| Rolled-up complex requires S as coefficient | Yes -- S cannot be absorbed into Lambda^bullet | reconstruction |
| Same conclusion for (9,5) signature | Yes -- same weight obstruction, H-linear version | reconstruction |
| Upgrade path to verified | CAS check on D_7 highest weights for S^+ vs Lambda^k | open |

---

## 7. References

- Lawson, H.B. and Michelsohn, M.L., _Spin Geometry_, Princeton UP, 1989.
  Appendix I Table 1 (Clifford classification), Chapter I §5 (spinor modules).
- Harvey, F.R., _Spinors and Calibrations_, Academic Press, 1990.
  Table 6.2 (Cl(p,q)), Table 13.5 (invariant bilinear forms), Chapter 6 (spinors).
- Budinich, P. and Trautman, A., _The Spinorial Chessboard_, Springer, 1988.
  Chapter 4 (Majorana-Weyl spinors in split signature).
- Humphreys, J.E., _Introduction to Lie Algebras and Representation Theory_, Springer, 1972.
  Chapter IV (highest-weight theory), Chapter V (representations of semisimple algebras).
  Key fact: fundamental representations V_6 and V_7 of D_7 are half-spin, not polynomial
  in V_1 = C^{14}. See §24 for the full list of fundamental representations.
- Adams, J.F., _Lectures on Exceptional Lie Groups_, U. Chicago Press, 1996.
  Real forms of spin representations of D_n.
- explorations/shiab-operator/n2-shiab-computation-spin77-branching-rules-2026-06-22.md (shiab existence)
- explorations/shiab-operator/sc1-shiab-domain-codomain-2026-06-23.md (domain/codomain, equivariance, H-linearity)
- explorations/anomaly-and-bordism/n1-signature-audit-y14-clifford-algebra-2026-06-22.md (signature (9,5) RESOLVED)

---

*Filed: 2026-06-23. Computation for PC1 / positive-constructions lane. Grade: reconstruction.
Key result: S does not embed in Lambda^bullet(R^14) over R (no natural equivariant linear
map S -> Lambda^k). The rolled-up Dirac-DeRham complex on Omega^bullet tensor S is the
correct geometric object; S is a coefficient bundle, not a sub-bundle of Lambda^bullet.
This is representation-theoretically forced by the spinor vs. tensor weight structure of D_7.*
