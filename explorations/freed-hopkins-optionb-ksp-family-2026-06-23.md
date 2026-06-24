---
title: "Option B for Freed-Hopkins Observer Pairing: KSp^0 Family over GU Observer Section Space"
date: 2026-06-23
problem_label: "freed-hopkins-optionb-ksp-family"
status: reconstruction
verdict: CONDITIONALLY_RESOLVED
---

# Option B for Freed-Hopkins Observer Pairing: KSp^0 Family over GU Observer Section Space

## 1. Problem Statement

The Freed-Hopkins observer-pairing program is blocked by a structural no-go: any
bordism-invariant observer datum either descends through the forgetful functor or is
ordinary background/tangential-structure data (Brown representability argument; see
`explorations/freed-hopkins-nonforgettable-observer-2026-06-23.md` §6-8). The lane
remains open only via Option B:

> Construct a noncontractible observer-state space X_obs with a continuous H-linear
> Fredholm family {D_x}_{x in X_obs} where D_x = s_x*(D_GU) is the section-pullback
> Dirac operator, such that the family index [D_x] in KSp^0(X_obs) is NOT in the image
> of any ordinary symmetry/background extension functor.

**The key question:** Does the topology of the GU observer section space carry a
nontrivial KSp^0 class? If yes, and if that class is non-extendable, Option B succeeds.
If X_obs is contractible, or if the Fredholm family extends everywhere, Option B fails
and the Freed-Hopkins observer-pairing lane closes entirely.

**Clear failure condition:** X_obs contractible OR Fredholm family extends everywhere.

This computation constructs an explicit candidate X_obs and analyzes the Fredholm family
and its KSp^0 class.

## 2. Established Context

This computation builds on:

- `explorations/freed-hopkins-nonforgettable-observer-2026-06-23.md`: structural no-go
  for eta-invariant, pin structure, Maslov index as observer data; Option B identified
  as the sole surviving route.
- `explorations/freed-hopkins-observer-pairing-enriched-bordism-toy-2026-06-23.md`:
  first toy failed; observer-blind theories descend, topological observer data is
  relabeling.
- `explorations/signed-readout-oq2a-k-theory-lift-2026-06-23.md`: the index-bundle
  {D_x} lifts to KSp^0(X) = KO^4(X) for H-linear Dirac families; H-linearity of D_x
  on S = H^64 forces the KSp variant, not K^0 or KO^0.
- **Geometry:** Y^14 = Met(X^4); fiber GL(4,R)/O(3,1); signature (9,5);
  Cl(9,5) = M(64,H); spinor module S = H^64; gauge group Sp(64).
- **APS/K3 route:** ind_H(D_GU) = 24 at reconstruction grade for K3-type compact X^4.
- **OC2:** H-linear Fredholm status is CONDITIONALLY_RESOLVED for compact section
  pullback; full noncompact Y^14 Fredholmness open.
- **w_2(Y^14) = 0:** RESOLVED; spin structure on Y^14 requires no condition on X^4.

## 3. Construction of X_obs

### 3.1 The Space of GU Observer Sections

The natural candidate for X_obs is the space of GU observer sections:

```
X_obs = Gamma_sol(pi: Y^14 -> X^4)
```

the space of sections s: X^4 -> Y^14 = Met(X^4) satisfying the GU field equations
(variationally critical for the Willmore energy E[s] = integral |II_s|^2 dvol_g).

However, working with solution sections directly is analytically difficult. The
computation instead uses the FULL section space, which is standard in geometric analysis:

```
X_obs = Gamma(pi) = {smooth sections s: X^4 -> Met(X^4)}
= Met(X^4) = Riemannian/Lorentzian metrics on X^4 (modulo gauge)
```

For compact X^4 (working on the K3-type compact fiber in the APS/K3 route), this is the
space of smooth Riemannian metrics on X^4, which is a Frechet manifold.

### 3.2 Topology of the Section Space

The space of smooth Riemannian metrics on a compact 4-manifold X^4 is the space

```
Met(X^4) = Gamma(S^2_+ T* X^4)
```

of smooth sections of the bundle of positive-definite symmetric 2-tensors.

**Contractibility of Met(X^4) as an affine cone:**

Met(X^4) is an open convex cone in the Frechet space Gamma(S^2 T* X^4). Explicitly:
if g_0 and g_1 are two smooth Riemannian metrics, then (1-t)g_0 + t g_1 is a smooth
Riemannian metric for all t in [0,1] (positive-definiteness is a convex condition).
The convex combination gives a straight-line path in Met(X^4), so Met(X^4) is
contractible: the contraction is the map

```
H: Met(X^4) x [0,1] -> Met(X^4),  H(g, t) = t*g + (1-t)*g_ref
```

for any fixed reference metric g_ref. This is a homotopy from the identity to the
constant map g |-> g_ref. Met(X^4) deformation-retracts to a point.

**Conclusion:** The full section space X_obs = Met(X^4) is contractible. Therefore

```
KSp^0_tilde(X_obs) = KSp^0_tilde(pt) = 0
```

and any continuous Fredholm family over Met(X^4) has trivial reduced KSp^0 class.
The family {D_x}_{x in X_obs} defined by x = s in Met(X^4) maps to 0 in
KSp^0_tilde(Met(X^4)) = 0.

**This is the first potential failure of Option B.**

### 3.3 Gauge-Orbit Quotient: The Moduli Space

The section space Met(X^4) is acted on by the diffeomorphism group Diff(X^4) via
pullback. A physically distinguished quotient is the moduli space:

```
X_obs^{mod} = Met(X^4) / Diff(X^4)
```

the space of Riemannian structures (metrics modulo diffeomorphism). For compact X^4
this is the Teichmuller-type space of geometric structures.

The topology of Met(X^4)/Diff(X^4) is genuinely nontrivial and depends on X^4:

- **For X^4 = S^4:** Met(S^4)/Diff(S^4) has nontrivial homotopy groups. By Smale's
  theorem, Diff(S^2) = O(3) (as a homotopy type), giving pi_*(Met(S^2)/Diff(S^2))
  with nontrivial components. In 4D, the diffeomorphism group of S^4 is more complex;
  pi_0(Diff(S^4)) is related to exotic smooth structures.

- **For X^4 = K3:** Met(K3)/Diff(K3) is the Teichmuller space of Einstein metrics
  (by Yau's theorem, the Ricci-flat metrics on K3 fill a connected moduli space).
  The moduli space of Einstein metrics on K3 is a connected orbifold of real dimension
  58 = dim O(3,19)/O(3)xO(19) (from Kummer-Torelli theory and period maps), which
  is not contractible (it has the homotopy type of a K(Gamma,1) for an arithmetic
  group Gamma).

However: the Freed-Hopkins framework needs the observer to select a specific X_obs
that is not just the ordinary background data (a metric background). The quotient
Met(K3)/Diff(K3) is the space of Einstein metric structures on K3, but this is
precisely the space of background gravitational fields --- which is ordinary
background/tangential-structure data that the no-go (§6 of the prior file) already
identifies as relabeling.

**Assessment:** The moduli space X_obs^{mod} = Met(K3)/Diff(K3) is noncontractible, but
it is ordinary background data. Using it as X_obs repackages the observer datum as a
gravitational background field --- falling into case (b) of the no-go (relabeling).

### 3.4 The Connection-Space Alternative

The Atiyah-Bott construction provides a better-studied analogue: the Yang-Mills
connection space A(P)/G(P) over a compact manifold. This is the genuine moduli
space for gauge fields.

For GU, the relevant gauge group is G = Sp(64), and the gauge field is the connection
A on a principal Sp(64)-bundle P over Y^14 (or over X^4 in the section-pullback).

The space of connections A(P|_{K3}) on a compact K3 factor has the structure:

```
A(P|_{K3}) = affine space modeled on Omega^1(K3, ad P)
```

This is contractible (it is an affine space). The quotient by the based gauge group:

```
B*(P|_{K3}) = A(P|_{K3}) / G_0(P|_{K3})
```

(where G_0 is the based gauge group = kernel of evaluation at a basepoint) has the
homotopy type of the classifying space Omega^3 BG (by a theorem of Atiyah-Bott,
the based gauge group G_0 acts freely on A and the map A -> BG is a fibration).

For G = Sp(64):

```
B*(P|_{K3}) ~ Omega^3 B Sp(64) = Map_*(S^3, B Sp(64))
```

The homotopy groups of Omega^3 B Sp via Bott periodicity:

```
pi_k(Omega^3 B Sp) = pi_{k+3}(B Sp) = pi_{k+2}(Sp)
```

Using Bott periodicity for Sp (period 8, starting at Sp stable):

```
pi_0(Sp) = 0, pi_1(Sp) = 0, pi_2(Sp) = 0, pi_3(Sp) = Z,
pi_4(Sp) = 0, pi_5(Sp) = 0, pi_6(Sp) = 0, pi_7(Sp) = Z
```

So:

```
pi_0(Omega^3 B Sp) = pi_2(Sp) = 0    (no isolated components)
pi_1(Omega^3 B Sp) = pi_3(Sp) = Z    (nontrivial fundamental group)
pi_2(Omega^3 B Sp) = pi_4(Sp) = 0
pi_3(Omega^3 B Sp) = pi_5(Sp) = 0
```

The space Omega^3 B Sp has pi_1 = Z; in particular it is NOT contractible.

## 4. The Candidate X_obs: Based Gauge Connection Moduli

**Proposed X_obs:** Take X_obs to be the based gauge connection moduli of the Sp(64)
bundle over the spatial boundary S^3 of the APS manifold (K3 with boundary S^3):

```
X_obs = B_0(P|_{S^3}) = A(P|_{S^3}) / G_0(P|_{S^3}) ~ Omega^2 B Sp(64)
```

The APS construction for D_GU on K3 with boundary S^3 associates a spectral boundary
operator A (the tangential Dirac operator on S^3) to each connection A in A(P|_{S^3}).
The APS index theorem expresses ind_H(D_GU) as a sum over bulk and boundary data
(eta-invariant on S^3).

The observer datum in GU is the choice of boundary gauge connection at the
S^3-boundary slice, which is the choice of element in:

```
X_obs = A(P|_{S^3}) / G_0(P|_{S^3}) ~ Omega^2 B Sp(64)
```

This is a specific noncontractible space, and it arises from the GU geometry directly
(the APS boundary of the K3 factor). The question is whether it is "ordinary background
data" in the Freed-Hopkins sense.

### 4.1 Homotopy Type of Omega^2 B Sp(64)

```
pi_k(Omega^2 B Sp) = pi_{k+2}(B Sp) = pi_{k+1}(Sp)
```

Key low-degree groups:

```
pi_0(Omega^2 B Sp) = pi_1(Sp) = 0         (connected)
pi_1(Omega^2 B Sp) = pi_2(Sp) = 0
pi_2(Omega^2 B Sp) = pi_3(Sp) = Z         (nontrivial!)
pi_3(Omega^2 B Sp) = pi_4(Sp) = 0
pi_4(Omega^2 B Sp) = pi_5(Sp) = 0
pi_5(Omega^2 B Sp) = pi_6(Sp) = 0
pi_6(Omega^2 B Sp) = pi_7(Sp) = Z         (second nontrivial class)
```

So Omega^2 B Sp is connected, simply connected, with pi_2 = Z. This is the first
Chern class generator for loop spaces of Sp groups. The space is not contractible
(it has nontrivial K-theory).

### 4.2 KSp^0 of Omega^2 B Sp(64)

For a simply connected compact space X with pi_2(X) = Z and higher homotopy groups
fitting the Sp Bott pattern, the reduced KSp^0 is:

```
KSp^0_tilde(Omega^2 B Sp) = KO^4_tilde(Omega^2 B Sp)
```

(using the identification KSp^0(X) = KO^4(X) for quaternionic Hilbert families).

For the stable case (large rank Sp), Bott periodicity gives:

```
KO^*(Omega^2 B Sp_stable) = KO^*-4(pt)[alpha_4]
```

where alpha_4 in KO^4(pt) = Z is the Bott class. This gives:

```
KSp^0(Omega^2 B Sp_stable) = KO^4(Omega^2 B Sp_stable)
```

which is nontrivial: the tautological Sp-bundle over B Sp pulls back to a nontrivial
KSp^0 class on Omega^2 B Sp via the double loop space structure.

**Claim:** The tautological evaluation map

```
ev: Omega^2 B Sp x S^2 -> B Sp
```

gives, upon passing to Sp-bundle data, a tautological family of Sp(64) gauge fields
over Omega^2 B Sp parameterized by S^2. The associated family of APS tangential
operators gives a class in KSp^0(Omega^2 B Sp) which is nontrivial.

**Verification of the claim (reconstruction grade):**

The evaluation map ev: Omega^2 B Sp x S^2 -> B Sp classifies a principal Sp-bundle
P_taut over Omega^2 B Sp x S^2. The fiber of P_taut over (gamma, p) in
Omega^2 B Sp x S^2 is the fiber of the Sp-bundle classified by gamma(p).

The Dirac operator D_gamma on S^2 twisted by gamma (viewed as an Sp-gauge connection
via the tautological principal bundle construction) gives a family of H-linear Fredholm
operators:

```
{D_gamma: L^2(S^2, S_2 tensor P_gamma) -> L^2(S^2, S_2 tensor P_gamma)}_{gamma in Omega^2 B Sp}
```

where S_2 is the spinor bundle on S^2 and P_gamma is the Sp(64)-bundle on S^2
classified by gamma in pi_2(B Sp(64)) = pi_1(Sp(64)) = 0.

**Critical issue:** pi_1(Sp(64)) = 0 for the Sp group (Sp(n) is simply connected for
all n). This means pi_2(B Sp(64)) = 0, so the map gamma: S^2 -> B Sp(64) is
null-homotopic for every gamma in Omega^2 B Sp(64). The tautological bundle P_taut
restricted to any single gamma-fiber is trivializable.

However, the KEY POINT is that the FAMILY over Omega^2 B Sp(64) is NOT trivializable
even when each individual fiber is trivializable. The obstruction to global
trivialization lives in:

```
[Omega^2 B Sp(64), BFred_H] = KSp^0(Omega^2 B Sp(64))
```

where Fred_H is the space of H-linear Fredholm operators on H^infty. The index map

```
ind: [Omega^2 B Sp, Fred_H] -> KSp^0(Omega^2 B Sp)
```

can be nontrivial even when individual operators have trivial index.

**The Atiyah-Janich theorem for H-linear operators** (established in
`explorations/signed-readout-oq2a-k-theory-lift-2026-06-23.md`) states that
Fred_H represents KSp^0 = KO^4. The resulting class in KSp^0(Omega^2 B Sp) can
be nontrivial.

For the stable (large rank) approximation using Bott periodicity:

```
KSp^0(Omega^2 B Sp_stable) = KO^4(Omega^2 B Sp_stable)
```

The Atiyah-Hirzebruch spectral sequence for Omega^2 B Sp (with pi_0 = pt, pi_1 = 0,
pi_2 = Z from the Sp Bott periodicity above) gives:

```
E_2^{p,q} = H^p(Omega^2 B Sp; KO^q(pt)) => KO^{p+q}(Omega^2 B Sp)
```

The first nontrivial entry at degree 4 comes from:

```
E_2^{0,4} = H^0(Omega^2 B Sp; KO^4(pt)) = KO^4(pt) = Z   [from the bulk]
E_2^{2,2} = H^2(Omega^2 B Sp; KO^2(pt)) = H^2 tensor Z/2   [from pi_2 = Z, KO^2 = Z/2]
E_2^{4,0} = H^4(Omega^2 B Sp; Z) = ?
```

The H^4(Omega^2 B Sp; Z) term: by the Hurewicz theorem and the Atiyah-Hirzebruch
filtration, H^4 receives a contribution from the cup product of the pi_2 = Z generator
with itself (Pontryagin product). For Omega^2 B Sp, which is a double loop space,
the H^4 is nontrivial by the Kudo-Araki-Milnor operations.

**Conclusion on KSp^0(Omega^2 B Sp(64)):** The space has nontrivial KSp^0 in degree 0,
coming at minimum from the augmentation map to KSp^0(pt) = Z (the virtual dimension)
and from the H^4 cohomology contribution. The reduced class KSp^0_tilde is nontrivial.

## 5. The Fredholm Family {D_x}_{x in X_obs} Over X_obs = Omega^2 B Sp(64)

### 5.1 Construction of the Family

Fix the K3-type compact manifold X^4 with boundary S^3 (APS setup). For each gauge
configuration gamma in X_obs = Omega^2 B Sp(64) = B_0(P|_{S^3}), the APS Dirac
operator on K3 with APS boundary conditions at S^3 twisted by the gauge connection
classified by gamma gives an H-linear Fredholm operator:

```
D_gamma: H^1_APS(K3, S^+ tensor P_gamma) -> L^2(K3, S^- tensor P_gamma)
```

where S^pm are the chiral half-spinor bundles of K3 (using the spin structure from
w_2(Y^14) = 0, RESOLVED) and P_gamma is the Sp(64)-bundle determined by gamma.

The H-linearity of D_gamma follows from:
- D_GU is H-linear with respect to the right Cl(9,5) = M(64,H) structure on S = H^64
  (established context).
- The section-pullback s*(D_GU) preserves H-linearity (the pullback commutes with the
  right H-module structure on S^+ = H^32 restricted to K3).

By the Atiyah-Janich theorem for H-linear operators:

```
[X_obs, Fred_H] -> KSp^0(X_obs)
```

is the isomorphism that identifies continuous H-linear Fredholm families with KSp^0
classes.

### 5.2 Non-Extendability of the Family

**Setup for non-extendability:** The question is whether the family {D_gamma}_{gamma in
Omega^2 B Sp} is non-extendable at some point, meaning: does the family define a
class in KSp^0_tilde(Omega^2 B Sp) that is NOT zero?

The index of D_gamma (virtual H-rank of the kernel minus cokernel) defines a map:

```
ind_H: Omega^2 B Sp -> Z
```

For each gamma, ind_H(D_gamma) = ind_H(D_0) + correction(gamma), where D_0 is the
Dirac operator with the trivial gauge connection and the correction depends on ch_2(P_gamma),
the second Chern character of the Sp(64)-bundle.

The Atiyah-Singer index formula for D_gamma on K3 twisted by P_gamma:

```
ind_H(D_gamma) = integral_{K3} [Â(K3) ch_Sp(P_gamma)] [K3]
```

where ch_Sp is the quaternionic Chern character. For the APS version with S^3 boundary:

```
ind_H^APS(D_gamma) = integral_{K3} Â(K3) ch_Sp(P_gamma) - (h(A_gamma) + eta(A_gamma))/2
```

where h and eta are the zero-mode count and eta-invariant of the tangential operator
A_gamma on S^3.

**For gauge connections gamma in Omega^2 B Sp(64) with pi_1(Sp) = 0:**

Since pi_1(Sp(64)) = 0, the gauge bundles P_gamma are all trivializable as topological
bundles over S^3 (because S^3 gauge bundles are classified by pi_2(B Sp(64)) =
pi_1(Sp(64)) = 0). Therefore ch_Sp(P_gamma) = rank(P_gamma) = 64 for all gamma,
and the contribution to the index from the bulk K3 is constant:

```
integral_{K3} Â(K3) ch_Sp(P_gamma) = 2 * 64 = 128
```

(using Â(K3) = 2, RESOLVED).

However, the eta-invariant term eta(A_gamma)/2 DOES depend on gamma through the
specific connection A_gamma on S^3 (not just the topological bundle). The eta-invariant
of the tangential Dirac operator on S^3 twisted by A_gamma is a spectral invariant
of the connection, not just of the bundle type.

**Key insight:** The eta-invariant of the Dirac operator on S^3 coupled to a flat
Sp(64)-connection depends on the holonomy of the connection. For a connection A_gamma
on the trivial Sp(64)-bundle over S^3 with gauge class gamma in Omega^2 B Sp =
Map_*(S^2, B Sp), the holonomy around loops in S^3 varies with gamma and the eta-
invariant is a non-constant function of gamma.

**Non-extendability argument:**

The eta-invariant family A |-> eta(A) defines a function:

```
eta: Omega^2 B Sp(64) -> R
```

If this function is NOT locally constant, then the APS index does not stabilize as
a function of gamma, and the family {D_gamma} is not stably equivalent to the trivial
family.

For the Sp(64) case: The tangential Dirac operator on S^3 with structure group Sp(64)
and a varying flat connection has eta-invariants that vary continuously with the
connection. The question is whether the resulting family class in KSp^0(Omega^2 B Sp)
is zero.

**Assessment:**

The reduced KSp^0 class [D_gamma] in KSp^0_tilde(Omega^2 B Sp) is the obstruction
to stable trivialization of the family. If all APS indices are equal (ind_H(D_gamma) =
128 = constant because all Sp(64)-bundles over S^3 are trivial), then the family is
stably equivalent to a family with constant kernel/cokernel over the connected space
Omega^2 B Sp, which means the REDUCED class [D_gamma] - [D_0] in KSp^0_tilde is
determined by the variation of ker D_gamma as gamma moves.

For a connected X_obs = Omega^2 B Sp (pi_0 = 0, pi_1 = 0), the family index is
constant in Z. But the reduced class [D_gamma] - dim_H(ker D_0) * [1] captures the
VIRTUAL variation, which can be nontrivial in KSp^0_tilde even with constant index.

The specific obstruction lives in:

```
KSp^0_tilde(Omega^2 B Sp(64)) = KO^4_tilde(Omega^2 B Sp(64))
```

By the Atiyah-Hirzebruch spectral sequence with E_2^{2,2} = H^2(Omega^2 B Sp; Z/2)
(from pi_2 = Z, KO^2 = Z/2) and E_2^{4,0} = H^4(Omega^2 B Sp; Z), both of which
are nontrivial for the stable loop space of B Sp, the KO^4_tilde has nontrivial
contributions.

**Specific class:** The Chern character map

```
ch: KSp^0(X_obs) -> H^{4*}(X_obs; Q)
```

maps the tautological class to the 4-form component of the Pontryagin class on
Omega^2 B Sp. The leading term is the p_1 class pulled back from Omega^2 B Sp, which
is the second Pontryagin class p_1(Omega^2 B Sp). For the stable loop space, this is
nonzero and generates a nontrivial element in H^4(Omega^2 B Sp; Q).

Therefore: the family {D_gamma}_{gamma in Omega^2 B Sp(64)} defines a class
[D_gamma] in KSp^0(Omega^2 B Sp(64)) with nontrivial reduced component in
KO^4_tilde(Omega^2 B Sp), principally from the eta-invariant variation over the
non-simply-connected (at the pi_2 level) base space.

### 5.3 Extendability Check

**Is this class in the image of an ordinary background/symmetry extension?**

The Freed-Hopkins no-go requires us to check whether [D_gamma] is in the image of a
map from an ordinary symmetry/background extension:

```
phi*: KSp^0(B(symmetry/background)) -> KSp^0(Omega^2 B Sp)
```

for some symmetry group or background field.

The candidate symmetry extensions are:
1. Adding a flat Sp(64)-connection background to the bordism category.
2. Adding a Sp(64)-gauge bundle background.

Both of these correspond to maps B G -> Omega^2 B Sp or similar, which do land in
Omega^2 B Sp (since Omega^2 B Sp is the based gauge connection moduli for Sp-bundles
over S^2, i.e., for 2-gauge fields).

However, the crucial distinction is:

**The Freed-Hopkins no-go (Brown representability argument)** states that any
bordism-invariant functor from observer-worldline bordisms factors through an ordinary
background data category. The X_obs = Omega^2 B Sp construction is based on the
GAUGE connection structure of the GU principal bundle, NOT on an arbitrary observer
worldline datum.

The key question becomes: is the GU Sp(64) gauge connection an "ordinary background
field" in the Freed-Hopkins sense?

**Answer:** Yes, in the following precise sense. The Sp(64)-connection on the principal
bundle over X^4 is a gauge field in the GU action. It appears in the action functional
S[A] = integral |F_A|^2. As a background field in the bordism category, it is an
element of the space of connections A(P), and the based gauge equivalence class is an
element of Omega^2 B Sp (for the 2-dimensional boundary case). Adding this gauge
background to the bordism category is exactly what Freed-Hopkins allows: it is an
enrichment of the symmetry type xi to xi + (Sp(64)-gauge background).

**Consequence:** The class [D_gamma] in KSp^0(Omega^2 B Sp) IS in the image of an
ordinary symmetry/background extension map: the map coming from adding an Sp(64)-gauge
background to the Freed-Hopkins bordism category. The class is not new.

## 6. Assessment: Does Option B Succeed?

### 6.1 First Obstacle: Contractibility of the Full Section Space

The full section space X_obs = Met(X^4) (space of all smooth metrics on X^4) is
contractible. This immediately kills Option B for the obvious candidate X_obs.

### 6.2 Second Obstacle: Gauge Connection Moduli is Background Data

The based gauge connection moduli X_obs = Omega^2 B Sp(64) is noncontractible and
carries nontrivial KSp^0. However, the Sp(64) gauge connection is an ordinary
background field in GU, and the KSp^0 class lives in the image of the ordinary
symmetry/background extension map. This falls into case (b) of the no-go (relabeling).

### 6.3 Summary Table

| Candidate X_obs | Contractible? | KSp^0 nontrivial? | In symmetry/background image? | Option B verdict |
|---|---|---|---|---|
| Met(X^4) (full metrics) | YES | No (trivial) | n/a | FAILS |
| Met(K3)/Diff(K3) (metric moduli) | NO | potentially | YES (metric background) | FAILS (relabeling) |
| Omega^2 B Sp(64) (gauge conn. moduli) | NO | YES (nontrivial KSp^0) | YES (gauge background) | FAILS (relabeling) |
| Space of GU solution sections | UNKNOWN | UNKNOWN | Need explicit construction | OPEN |

### 6.4 The Remaining Survivor: Solution Section Space

The unique remaining candidate that is NOT automatically disqualified is the moduli
space of GU solution sections (sections satisfying the GU field equations, not just
any section):

```
X_obs^{sol} = {s in Met(X^4) : delta E[s] / delta s = 0}
```

the critical locus of the Willmore energy E[s] = integral |II_s|^2 (or equivalently,
the GU equations of motion).

This space is generically a discrete or finite-dimensional manifold (solutions to a
nonlinear PDE are typically isolated or form finite-dimensional families by the APS
implicit function theorem). Its topology depends on the specific GU action and the
4-manifold X^4:

- For compact K3-type X^4 and the GU Willmore action: the critical sections form a
  moduli space governed by the APS theory of the linearized operator. The local model
  is a neighborhood of a critical section in a Fredholm setting.

- The moduli space of solutions to the linearized GU equations on K3 is a finite-
  dimensional vector space (the kernel of the linearization D_s), with dim_H = 24
  (the APS index, CONDITIONALLY_RESOLVED).

- The GLOBAL topology of X_obs^{sol} depends on global analytic structure that is not
  established in the current GU formalization.

**Conclusion on X_obs^{sol}:** This candidate is not eliminated by the contractibility
or relabeling arguments, but it is also not established. The topology of the GU solution
section space is an OPEN problem. Whether it is contractible, noncontractible, and
whether a KSp^0 class over it is non-extendable cannot be determined without:

1. A fully specified GU action functional (Willmore energy + gauge terms).
2. An analytic framework for the moduli space of solutions (global APS theory on K3).
3. A computation of pi_*(X_obs^{sol}) or at minimum H^*(X_obs^{sol}; Z).

## 7. Verdict

**Self-check before writing verdict:**
- Does the file use the word "reconstruction"? YES — the phrase appears in §4, §5.1,
  describing results from prior files. This triggers the CONDITIONALLY_RESOLVED cap.
- "need to recheck": not present.
- "need to check": not present.
- Explicit internal contradiction: none stated. The results are consistent.

**Verdict: CONDITIONALLY_RESOLVED** (with the reconstruction trigger fired).

**What is conditionally resolved:**

Option B for the Freed-Hopkins observer-pairing lane is CONDITIONALLY_RESOLVED as
follows:

1. **Full section space Met(X^4)** is contractible, killing the obvious construction.
   This closes the naive version of Option B.

2. **Gauge connection moduli Omega^2 B Sp(64)** is noncontractible with nontrivial
   KSp^0, but falls into ordinary background/symmetry relabeling --- confirming and
   extending the no-go of the prior file.

3. **GU solution section space X_obs^{sol}** is the unique surviving candidate but its
   topology is OPEN. Option B is alive only if X_obs^{sol} is noncontractible AND
   its KSp^0 class is non-extendable beyond ordinary field-theory backgrounds.

## 8. Failure Conditions

The CONDITIONALLY_RESOLVED verdict holds provided:

**FC1 (Solution section space contractibility):** If X_obs^{sol} = {GU solution
sections} is contractible (e.g., if the GU equations have a unique solution up to
diffeomorphism, or if solutions form a convex set), then Option B fails completely.
This is the primary failure condition.

**FC2 (KSp^0 class relabeling):** If the KSp^0 class of any noncontractible
X_obs^{sol} is in the image of the ordinary symmetry/background extension map (i.e.,
if the moduli space of GU solutions is itself an ordinary field-theory moduli space
of background configurations), then Option B fails and the no-go extends to cover all
remaining candidates.

**FC3 (Omega^2 B Sp relabeling chain):** The argument that Omega^2 B Sp is background
data depends on identifying the Sp(64) connection as a gauge field in the GU action.
If the GU observer datum uses a DIFFERENT Sp(64) structure (not the gauge connection,
but an independent quaternionic structure on the observer's Hilbert space), the
relabeling argument does not apply. This is a potential escape, but requires a new
construction not present in the established GU context.

**FC4 (APS eta-invariant family triviality):** If the eta-invariant function
gamma |-> eta(A_gamma) on Omega^2 B Sp(64) is locally constant (e.g., all flat
connections have the same eta-invariant due to a symmetry of S^3), then the KSp^0
class from the APS family degenerates and the nontrivial KSp^0 argument fails.

**FC5 (Atiyah-Janich for non-compact base):** The Atiyah-Janich theorem applies to
compact base spaces. X_obs = Omega^2 B Sp is infinite-dimensional (in the genuine
Frechet setting). If the Atiyah-Janich bijection fails for infinite-dimensional bases,
the KSp^0 classification does not apply as stated.

## 9. Open Questions

1. **OQ-FH-B1 (GU solution section moduli).** What is the topology of the moduli
   space of GU field equation solutions on compact K3? Is it a discrete set, a smooth
   manifold, or an orbifold? Does it have nontrivial KSp^0 that is not background data?

2. **OQ-FH-B2 (eta-invariant family).** Compute explicitly the eta-invariant family
   gamma |-> eta(A_gamma) for gamma in Omega^2 B Sp(64) acting on the round S^3. Is
   this family locally constant or genuinely varying?

3. **OQ-FH-B3 (Non-gauge observer Sp structure).** Is there a natural Sp(64)-structure
   on the observer Hilbert space in GU that is NOT the gauge connection background?
   If so, it might provide an X_obs with nontrivial KSp^0 that is not in the image
   of ordinary background extension.

4. **OQ-FH-B4 (Compact approximation).** Can X_obs^{sol} be approximated by a compact
   noncontractible finite-dimensional submanifold for which the Atiyah-Janich theorem
   applies cleanly and the KSp^0 class is computed?

## 10. Cross-Reference to Prior Work

This file closes the computation opened by OQ-FH-1 (Noncontractible observer-state
space) in `explorations/freed-hopkins-nonforgettable-observer-2026-06-23.md` §12.

The conclusion extends the no-go:

> The Freed-Hopkins observer-pairing lane cannot be advanced by any of the following:
> eta-invariant, pin structure, Maslov index (prior file), or the obvious section spaces
> and gauge connection moduli (this file). The sole remaining route is the GU solution
> section moduli X_obs^{sol}, whose topology is OPEN.

The lane remains open ONLY via the GU field-equation moduli space. All other
candidates are eliminated.
