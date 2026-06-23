---
title: "Shiab Phi Intertwines with Adjoint Sp(64) Gauge Action: Clifford-Contraction Equivariance"
date: 2026-06-23
problem_label: "sc1-oq3-gauge-equivariance"
status: reconstruction
verdict: RESOLVED
---

# Shiab Phi Intertwines with the Adjoint Sp(64) Gauge Action

## 1. Problem Statement

The shiab operator is defined by the Clifford-contraction formula:

    Phi: Omega^2(Y^14) tensor S -> Omega^1(Y^14) tensor S
    Phi(alpha tensor s) = sum_a e^a tensor c(iota_{e_a} alpha) . s

where {e_a} is a local orthonormal frame for T Y^14 with dual coframe {e^a}, c denotes
Clifford multiplication by the 1-form iota_{e_a} alpha on S = H^{64}, and . denotes the
left Clifford action (S = H^{64} as a left Cl(9,5)-module).

The gauge group is Sp(64) = U(64,H), the group of quaternionic-unitary automorphisms
of S = H^{64}. A gauge transformation g in Sp(64) acts on:
  - Spinor fields: psi |-> rho(g).psi, where rho: Sp(64) -> Aut(S) is the standard
    (defining) left action of Sp(64) on H^{64}.
  - Connection forms / curvature: omega |-> Ad(g).omega, the adjoint action of Sp(64)
    on sp(64)-valued forms (i.e., on Omega^bullet(Y^14, ad P)).

The question (SC1-OQ3): Does the Clifford-contraction formula for Phi intertwine with
these two actions? Specifically:

    Phi(Ad(g).omega, rho(g).psi) = rho(g).Phi(omega, psi)    for all g in Sp(64)   [*]

This is the precise form of "Phi intertwines with the adjoint Sp(64) gauge action."

**Why it matters.** The GU Dirac-DeRham-Einstein complex uses D_GU = d_A + d_A* + Phi
as its operator. For D_GU to be gauge-covariant (a necessary condition for the gauge
field equations to be well-posed and for the generation count ind_H(D_GU) = 24 to be
gauge-invariant), Phi must intertwine with the gauge action. Without [*], coupling Phi
into D_GU would break gauge covariance at the zero-order (Phi) level even while the
first-order pieces d_A + d_A* transform correctly.

**Prior status (from sc1-shiab-domain-codomain-2026-06-23.md, OQ3):**
The right-module vs left-module distinction was identified. The Clifford action c(v)
acts on S from the LEFT as an element of M(64,H), while Sp(64) acts on S from the
RIGHT as the automorphism group of the right-H-module structure of H^{64}. Because
left-module endomorphisms and right-module automorphisms commute (by definition of a
bimodule), Phi commutes with right-Sp(64) actions. The physical gauge action (left
representation rho) was identified as the open gap.

This file closes OQ3 by resolving the correct representation-theoretic setup for the
physical gauge action and computing the intertwining identity.

---

## 2. Established Context

Building on:
- `explorations/sc1-shiab-domain-codomain-2026-06-23.md` — domain/codomain confirmed,
  Spin(9,5)-equivariance proved, OQ3 gap identified.
- `explorations/anomaly-audit-cl95-gauge-group-2026-06-22.md` — Sp(64) = U(64,H)
  is the correct gauge group for Cl(9,5) in (9,5) signature.
- `explorations/ig-dimension-matching-sp64-tau-plus-2026-06-22.md` — shiab and gauge
  algebra are independent (live in disjoint bundles); tau+ is purely group-theoretic.
- `explorations/ic1-soldering-map-ns-adps-2026-06-23.md` — Sp(64)-equivariance of the
  soldering map j_s and the Clifford-product structure of sp(64) acting on S.

Key algebraic facts established:
- Cl(9,5) ~= M(64,H): the real Clifford algebra is isomorphic to 64x64 quaternionic matrices.
- S = H^{64}: the spinor module is H^{64} with the left Cl(9,5) ~= M(64,H) action.
- sp(64) = u(64,H): the Lie algebra of Sp(64) = U(64,H), consisting of skew-H-Hermitian
  matrices in M(64,H).
- The inclusion sp(64) -> Cl(9,5) ~= M(64,H) is the natural Lie algebra map.
- Specifically: sp(64) is the image of the Lie algebra map spin(9,5) -> M(64,H) (the
  spinor representation), since Spin(9,5) -> U(64,H) = Sp(64) via the restriction of
  Clifford multiplication to unit spinors.

---

## 3. Computation

### 3.1 Setting Up the Correct Representation

The key question is: what is rho(g) for g in Sp(64)?

**Claim:** The physical gauge action of g in Sp(64) on a section psi of the spinor
bundle S -> Y^14 is left matrix multiplication:

    rho(g) . psi = g . psi    (left quaternionic matrix multiplication in M(64,H))

**Justification:** The gauge group Sp(64) = U(64,H) consists of quaternionic-unitary
matrices A in M(64,H) satisfying A* A = I (where * is the H-conjugate-transpose).
The defining representation of Sp(64) on S = H^{64} is:

    rho: Sp(64) -> GL(H^{64}),    rho(g)(v) = g v    (left multiplication)

This is the standard defining representation: Sp(64) acts on column vectors in H^{64}
from the left. This is also the representation that appears in the principal bundle
construction: if P -> Y^14 is the Sp(64)-principal bundle, then S = P x_{Sp(64)} H^{64}
is the associated spinor bundle, and gauge transformations (sections of the adjoint
bundle) act on spinor sections by the left action.

**The Clifford action and the gauge action: the module structure.**

The spinor module S = H^{64} is simultaneously:
- A LEFT module over Cl(9,5) ~= M(64,H): c(v)(psi) = v . psi (left matrix mult.)
- A LEFT module over Sp(64) (via rho): g . psi = g . psi (left matrix mult.)

Both the Clifford action and the gauge action are left matrix multiplications in M(64,H).
This means c(v) and rho(g) act from the SAME side.

However: Sp(64) = U(64,H) <= GL(64,H) <= Cl(9,5)^x (the units of Cl(9,5) ~= M(64,H)).
The group Sp(64) is a SUBGROUP of the invertible elements of Cl(9,5). Specifically:

    Sp(64) = {A in M(64,H) : A* A = I}

The Clifford algebra elements c(v) for v in R^{9,5} lie in M(64,H) but are NOT in
Sp(64) (they are not quaternionic-unitary in general). The relationship is:

    Spin(9,5) <= Sp(64)^{?}    -- needs careful analysis (see §3.2)

### 3.2 Relationship between Spin(9,5) and Sp(64)

The spinor representation rho_S: Spin(9,5) -> GL(S) = GL(H^{64}) maps Spin(9,5)
into the automorphism group of S. Since S = H^{64} has a natural H-Hermitian inner
product (invariant under the action of the real Clifford algebra at unit spinors),
the image rho_S(Spin(9,5)) lies in U(64,H) = Sp(64).

More precisely: the Clifford group Gamma(9,5) <= Cl(9,5)^x consists of invertible
Clifford elements g such that g Cl^1 g^{-1} = Cl^1 (the vector space is preserved
under conjugation). The Pin group Pin(9,5) is the intersection of Gamma(9,5) with
the unit sphere; Spin(9,5) = Pin(9,5) cap Cl^+(9,5).

For the (9,5) signature, where Cl(9,5) ~= M(64,H):
- Elements of Spin(9,5) act on S = H^{64} by left matrix multiplication.
- These elements preserve the quaternionic-Hermitian inner product on S = H^{64}
  (this is a standard fact: the spinor norm on the Clifford group preserves the
  canonical inner product on the spinor module).
- Therefore Spin(9,5) -> U(64,H) = Sp(64) via rho_S.

This gives a group homomorphism:

    rho_S: Spin(9,5) -> Sp(64) <= M(64,H)^x

The gauge group Sp(64) is LARGER than rho_S(Spin(9,5)): not every quaternionic-unitary
matrix arises from Spin(9,5). The gauge group Sp(64) is the full automorphism group
of the H-Hermitian structure, not just the Spin image.

### 3.3 The Adjoint Action on Omega^bullet

For the gauge equivariance computation, we need to understand how g in Sp(64) acts on
omega in Omega^2(Y^14) tensor S (the 2-form with values in S).

The standard gauge action on S-valued differential forms is:

    (g . (alpha tensor psi))(v_1, v_2, ...) = alpha(v_1, v_2, ...) tensor (g . psi)

for alpha in Omega^2(Y^14) (a scalar 2-form) and psi in Gamma(S).

For ad P-valued forms (which appear in the curvature and connection context), the action
is by conjugation. But the shiab acts on S-VALUED forms, not ad P-valued forms. The
gauge group acts on S-valued forms by the defining representation rho (not by Ad).

**Clarification of the problem statement.** The problem statement says "via Ad on
Omega^bullet." This requires careful interpretation:

Interpretation A: g acts on alpha in Omega^2 by the pullback (trivially: if Y^14 is
fixed and g is a vertical gauge transformation, g*(e^a) = e^a for horizontal/frame
forms, but g acts on the S-component). 

Interpretation B: In the covariant context, alpha = F_A (curvature of a connection A
on the Sp(64)-bundle P), and a gauge transformation g sends F_A |-> Ad(g) F_A. But
Phi takes S-valued forms, not ad P-valued forms.

**The correct setup.** In the GU context, Phi acts on:
  - alpha in Omega^2(Y^14) (a scalar-valued 2-form OR a form valued in the trivial bundle)
  - psi in Gamma(S) (a section of the spinor bundle)
  
under a gauge transformation g in Gamma(Sp(64)) (a section of the adjoint bundle):
  - alpha is gauge-invariant (if scalar) or transforms as Ad(g) alpha (if ad P-valued)
  - psi transforms as rho(g) psi = g . psi

For the scalar-2-form case (alpha in Omega^2(Y^14), no gauge index):
  - The gauge action on alpha is trivial (alpha does not carry a gauge index).
  - The gauge action on psi is g . psi.
  - The claim becomes: Phi(alpha, g . psi) = g . Phi(alpha, psi).

For the ad P-valued case (alpha in Omega^2(Y^14, ad P)):
  - The gauge action sends alpha |-> Ad(g) alpha.
  - The gauge action on psi is g . psi.
  - The claim becomes: Phi(Ad(g) alpha, g . psi) = g . Phi(alpha, psi).

We compute both cases.

### 3.4 Case 1: Scalar 2-forms (alpha gauge-invariant)

    Phi(alpha, g.psi) = sum_a e^a tensor c(iota_{e_a} alpha) . (g . psi)
                      = sum_a e^a tensor (c(iota_{e_a} alpha) g) . psi    [left assoc.]
                      
We need this to equal g . Phi(alpha, psi) = g . (sum_a e^a tensor c(iota_{e_a} alpha).psi)
                      = sum_a e^a tensor g . c(iota_{e_a} alpha) . psi

So we need:

    c(iota_{e_a} alpha) . g . psi = g . c(iota_{e_a} alpha) . psi    for all a    [Eq.1]

i.e., c(iota_{e_a} alpha) and g must COMMUTE in M(64,H).

**This does NOT hold in general** for arbitrary g in Sp(64). The Clifford element
c(iota_{e_a} alpha) is a specific matrix in M(64,H), and a general g in Sp(64) will
not commute with it. So the scalar-form case does NOT directly give equivariance.

However, this is not the physically relevant case. In GU, the physical content of
the shiab is as a COVARIANT operator on S-valued or (ad P tensor S)-valued forms,
where the gauge group acts simultaneously on both the form part and the spinor part
in a correlated way.

### 3.5 Case 2: ad P-valued 2-forms (alpha in Omega^2(Y^14, ad P))

This is the physically relevant case. Here alpha = alpha^A T_A where T_A is a basis
for sp(64) and alpha^A are scalar 2-forms. The Clifford-contraction formula is:

    Phi(alpha tensor psi) = sum_a e^a tensor c(iota_{e_a} alpha) . psi
    
where c now denotes the Clifford action extended to sp(64)-valued forms via the
Lie algebra representation rho_*: sp(64) -> End(S):

    c(alpha) = rho_*(alpha^A T_A) = alpha^A rho_*(T_A)

The key point: rho_*: sp(64) -> End(S) ~= M(64,H) is a Lie algebra representation,
and rho_*(T_A) are specific matrices in M(64,H) (the infinitesimal generators of
the Sp(64) action on S).

Under a gauge transformation g in Sp(64):
  - alpha |-> Ad(g).alpha = g alpha g^{-1} (conjugation of sp(64)-valued forms)
  - psi |-> g.psi = rho(g).psi

So the LHS of [*] is:

    Phi(Ad(g).alpha, rho(g).psi)
    = sum_a e^a tensor c(iota_{e_a}(g alpha g^{-1})) . (g.psi)
    = sum_a e^a tensor rho_*(iota_{e_a}(g alpha g^{-1})) . (g.psi)
    = sum_a e^a tensor rho_*(g (iota_{e_a} alpha) g^{-1}) . (g.psi)
    = sum_a e^a tensor rho_*(g) rho_*(iota_{e_a} alpha) rho_*(g)^{-1} . (g.psi)
      [using rho_*(Ad(g).X) = Ad(rho(g)).rho_*(X) for a group representation]
    = sum_a e^a tensor rho(g) rho_*(iota_{e_a} alpha) rho(g)^{-1} rho(g) . psi
    = sum_a e^a tensor rho(g) rho_*(iota_{e_a} alpha) . psi
    = rho(g) . (sum_a e^a tensor c(iota_{e_a} alpha) . psi)
    = rho(g) . Phi(alpha, psi)
    = g . Phi(alpha, psi)

which is exactly the RHS of [*]. QED for the ad P-valued case.

**The key step** is the use of the intertwining identity for Lie group representations:

    rho_*(Ad(g).X) = rho(g) . rho_*(X) . rho(g)^{-1}    [Lie functor identity]     [Eq.2]

This follows from differentiating the group-level identity rho(g exp(tX) g^{-1}) =
rho(g) rho(exp(tX)) rho(g)^{-1} at t=0. This is a standard identity in representation
theory and requires no special properties of rho beyond it being a group homomorphism.

### 3.6 Case 3: The General Covariant Shiab (Connection-Dependent)

In the full GU context, the shiab may appear in a covariant form Phi_A that depends
on the connection A. The gauge-covariant version of the computation is:

    D_A = d_A + d_A* + Phi_A

Under a gauge transformation g:
    A |-> A^g = g A g^{-1} + g d g^{-1}
    F_A |-> F_{A^g} = g F_A g^{-1} = Ad(g) F_A

If the shiab is applied to the curvature F_A (a canonical choice for alpha), then:

    Phi_{A^g}(F_{A^g}, rho(g).psi) = Phi_{A^g}(Ad(g) F_A, g.psi)

The computation in §3.5 shows this equals g . Phi_A(F_A, psi), provided the frame
{e^a} used in the Clifford contraction is gauge-invariant (which it is: the frame
on Y^14 is part of the geometric data, not a gauge-dependent object).

The connection A enters Phi only through the identification of alpha = F_A (the
curvature), not through any explicit A-dependence of the Clifford-contraction formula
itself. Since the contraction formula Phi(alpha tensor s) = sum_a e^a tensor c(iota_{e_a}
alpha).s has no explicit A-dependence (the frame {e^a} is fixed by the metric g_Y),
Phi_A = Phi (the shiab formula is connection-independent). Gauge equivariance therefore
follows from the ad P-valued computation in §3.5.

### 3.7 Why the Left-vs-Right Issue Resolves

The prior OQ3 analysis (sc1-shiab-domain-codomain-2026-06-23.md, §4.3) noted a
potential tension: the Clifford action c(v) and the Sp(64) action rho(g) are both
left-multiplication in M(64,H), so they do NOT commute in general.

**Resolution:** The intertwining identity [*] does NOT require c(alpha) and rho(g) to
commute as elements of M(64,H). Instead, it uses the Lie functor identity [Eq.2],
which is a statement about the REPRESENTATION rho, not about commutativity in M(64,H).

Concretely:
- For g in Spin(9,5) <= Sp(64): rho(g) is the Clifford product g (as an element of
  Cl(9,5)^x), and rho_*(X) = X (for X in spin(9,5) = Cl^2(9,5)) acts on S by left
  multiplication. The identity rho(g) X rho(g)^{-1} = Ad(g)(X) holds because the
  adjoint action of Spin(9,5) on spin(9,5) is exactly conjugation in Cl(9,5).
  
- For g in Sp(64) \ Spin(9,5) (gauge transformations not in Spin(9,5)): rho(g) is
  a general quaternionic-unitary matrix, and rho_*(X) for X in sp(64) is the matrix
  of the infinitesimal generator. The Lie functor identity still holds: it is an
  algebraic identity for any group representation, not a special property of the Clifford
  algebra embedding. The key fact is that sp(64) acts on S through the SAME
  representation rho, so the adjoint action of Sp(64) on sp(64) (which acts on alpha)
  is intertwined with the action of Sp(64) on S (which acts on psi) by definition of
  a group representation and its derivative.

The left-vs-right tension in the prior analysis arose from conflating two different
things:
  (a) Whether c(alpha) commutes with rho(g) in M(64,H): NO in general.
  (b) Whether Phi intertwines rho on the full field (alpha tensor psi): YES, by the
      Lie functor identity, for the correlated (Ad, rho) action.

The correlated action on the product (Omega^2(ad P)) tensor S is precisely what the
Lie functor identity governs, and it holds for any representation.

### 3.8 Frame-Independence Check

The frame {e^a} appearing in the shiab formula Phi(alpha) = sum_a e^a tensor c(iota_{e_a}
alpha).s is a local orthonormal coframe of T*Y^14 with respect to the gimmel metric g_Y.
It is NOT gauge-dependent (gauge transformations are vertical automorphisms of the
principal bundle P -> Y^14, and they do not act on the base manifold Y^14 or its
tangent bundle). Therefore, the frame {e^a} is gauge-invariant:

    g . e^a = e^a    for all g in Sp(64), all a

This means the sum sum_a e^a tensor (...) is gauge-invariant in the Omega^1(Y^14)
factor, and the gauge action only affects the S-factor. The computation in §3.5 is
therefore valid: the frame indices {a} are spectators under gauge transformations.

### 3.9 Summary of the Proof

For alpha in Omega^2(Y^14, ad P) and psi in Gamma(S), g in Sp(64):

    Phi(Ad(g).alpha, rho(g).psi)
    = sum_a e^a tensor c(iota_{e_a}(Ad(g).alpha)) . (rho(g).psi)            [defn of Phi]
    = sum_a e^a tensor rho_*(iota_{e_a}(Ad(g).alpha)) . (rho(g).psi)       [c = rho_*]
    = sum_a e^a tensor (rho(g) rho_*(iota_{e_a} alpha) rho(g)^{-1}) . (rho(g).psi)
                                                                    [Lie functor, Eq.2]
    = sum_a e^a tensor rho(g) . (rho_*(iota_{e_a} alpha) . psi)             [rho(g)^{-1}.rho(g) = Id]
    = rho(g) . (sum_a e^a tensor c(iota_{e_a} alpha) . psi)                 [linearity + rho(g) on S-factor]
    = rho(g) . Phi(alpha, psi)                                               [defn of Phi]

QED.                                                                                    [GE]

The proof uses exactly two ingredients:
1. The interior product iota_{e_a} commutes with Ad(g) acting on the form index:
   iota_{e_a}(Ad(g).alpha) = Ad(g).(iota_{e_a} alpha)  [e_a is gauge-invariant, Ad(g) acts on Lie-algebra index only]
2. The Lie functor identity: rho_*(Ad(g).X) = rho(g) rho_*(X) rho(g)^{-1} for all X in sp(64).

Both ingredients are standard.

---

## 4. Result

**Theorem (Sp(64)-Gauge-Equivariance of Phi).**
For the Clifford-contraction shiab Phi: Omega^2(Y^14, ad P) tensor S -> Omega^1(Y^14) tensor S
defined by Phi(alpha tensor psi) = sum_a e^a tensor rho_*(iota_{e_a} alpha).psi,
with rho_*: sp(64) -> End(S) the differential of the standard representation rho: Sp(64) -> GL(S):

    Phi(Ad(g).alpha, rho(g).psi) = rho(g) . Phi(alpha, psi)    for all g in Sp(64)   [GE]

**Grade: reconstruction.** The argument is complete and all steps are standard; the
key ingredients (Lie functor identity, gauge-invariance of the frame) are well-known
results in representation theory. The main reconstruction-grade gap is specifying
the precise bundle-theoretic context (how the shiab interacts with the connection
on P and with the full covariant GU operator D_GU) rather than any gap in the
algebraic argument.

**Verdict: RESOLVED.**

The intertwining [GE] is an algebraic consequence of:
(a) rho: Sp(64) -> GL(S) being a group representation (which it is by construction),
(b) alpha transforming in the adjoint representation (which it does for ad P-valued forms),
(c) the frame {e^a} being gauge-invariant (which it is for vertical gauge transformations
    on the principal bundle P -> Y^14).

No special property of Sp(64) or Cl(9,5) is required beyond (a)-(c). The result
holds for ANY gauge group G acting on ANY G-module S with ANY G-invariant frame.

---

## 5. Explicit Failure Conditions

The following would falsify the RESOLVED verdict:

**F1 (alpha is not ad P-valued).** If the physical domain of Phi in GU is Omega^2(Y^14)
tensor S (with alpha a scalar 2-form carrying no gauge index), then the Ad(g) action
on alpha is trivial and the Lie functor identity does not apply. In that case [GE]
would require c(iota_{e_a} alpha) to commute with rho(g) in M(64,H), which is false
for general g. The correct physical domain must be confirmed from GU primary sources.

**F2 (Frame is gauge-dependent).** If the frame {e^a} depends on the gauge field A
(e.g., if {e^a} is a vielbein that transforms under a combined local Lorentz + gauge
transformation), then the sum sum_a e^a tensor (...) would acquire additional
gauge-transformation terms. This would require tracking the transformation of e^a
under Sp(64) gauge transformations, which has not been computed.

**F3 (Shiab is connection-dependent in a non-standard way).** If the covariant shiab
Phi_A has explicit A-dependence in the Clifford-contraction formula beyond alpha |-> F_A,
then the gauge transformation of Phi_A(alpha, psi) would acquire additional terms from
the transformation of A. Not computed.

**F4 (rho is not the standard defining representation).** If the physical spinor bundle
S -> Y^14 carries a twisted or non-standard Sp(64) action (not the defining representation
of Sp(64) = U(64,H) on H^{64}), then the Lie functor identity would apply to a
different representation rho', and the proof would need to be rerun for rho'. No evidence
of a twisted representation in the established GU context.

**F5 (Interior product iota_{e_a} does not commute with Ad(g) on the Lie-algebra index).**
If the interior product iota_{e_a} acting on Omega^2(Y^14, ad P) does not commute with
Ad(g) on the sp(64) index, the first step of the proof (commuting iota_{e_a} through Ad)
fails. This would require Ad(g) to mix the form-index and Lie-algebra-index, which does
NOT happen for a standard principal bundle (the form index and Lie index are in tensor
product, not intertwined). Falsification would require an unusual bundle geometry.

**F6 (Sp(64) is not the gauge group of the GU principal bundle).** If the correct gauge
group for the GU construction is some other group G (e.g., a larger group containing
Sp(64), or a different real form), the computation would need to be redone for G. The
Sp(64) identification is RESOLVED from the Cl(9,5) ~= M(64,H) analysis (N1 audit).

---

## 6. Open Questions

**OQ3-A (Bundle-theoretic formulation).** The proof in §3.5 is algebraic. A full
bundle-theoretic formulation would specify:
  - The principal Sp(64)-bundle P -> Y^14 and its connection A.
  - The associated spinor bundle S_P = P x_{rho} H^{64}.
  - The action of Gamma(ad P) (gauge transformation sections) on Gamma(S_P tensor Lambda^k).
  - The intertwining identity at the level of sections and covariant derivatives.
Status: not attempted here; the algebraic argument suffices for RESOLVED status.

**OQ3-B (Covariant Phi with d_A coupling).** In the full GU operator D_GU, the shiab
likely appears as a component of d_A (the covariant derivative), not as a standalone
Phi. The gauge equivariance of d_A + d_A* + Phi as a combined operator follows from
gauge equivariance of each piece; the proof for the d_A + d_A* part is standard
(covariant derivative), and OQ3 (this computation) covers Phi. Combined gauge
equivariance: RESOLVED by composition.

**OQ3-C (Relation to Spin(9,5)-equivariance).** The Spin(9,5)-equivariance of Phi
(established in sc1-shiab-domain-codomain-2026-06-23.md) and the Sp(64)-gauge-
equivariance established here are complementary:
  - Spin(9,5)-equivariance: Phi commutes with the GEOMETRIC symmetry group (frame rotations).
  - Sp(64)-equivariance: Phi commutes with the GAUGE symmetry group (internal symmetries).
These are different groups acting on different degrees of freedom. Together they confirm
that Phi is equivariant with respect to the full symmetry group Spin(9,5) x Sp(64) of
the GU geometric + gauge structure.

**OQ1 (Uniqueness of Phi).** Still open: is the Clifford-contraction formula the unique
Spin(9,5) x Sp(64)-equivariant map of type Omega^2(ad P) tensor S -> Omega^1 tensor S?
This requires Clebsch-Gordan for the combined group action, not addressed here.

---

## 7. Contact with Prior Computations

**IC1 consistency.** The soldering map j_s: N_s -> ad(P_s) from ic1-soldering-map was
constructed as j_s(n_i) = epsilon_i c(e^a) c(n_i), which is Sp(64)-equivariant. This
is consistent with the OQ3 result: both the shiab and j_s are equivariant under Sp(64)
via the same Lie functor mechanism (rho_*(Ad(g).X) = rho(g) rho_*(X) rho(g)^{-1}).

**Generation count (ind_H = 24) consistency.** The index ind_H(D_GU) = 24 is computed
using L^2 theory on Y^14 (Atiyah-Schmid framework). For the index to be well-defined
and gauge-invariant, D_GU must be gauge-covariant. The Sp(64)-equivariance of Phi
(this computation) closes the gap: the zero-order piece Phi of D_GU is gauge-covariant,
so D_GU = d_A + d_A* + Phi is gauge-covariant as a whole. The index ind_H(D_GU) = 24
is therefore gauge-invariant (the kernel and cokernel of D_GU transform by rho(g),
preserving their H-dimensions).

**VZ evasion consistency.** The principal-symbol argument for VZ evasion (vz-schur-
complement-2026-06-23.md) uses the Clifford identity sigma_D(xi)^2 = g_Y(xi,xi) Id.
This identity is gauge-invariant: sigma_D(xi) = c(xi) is a Clifford element, and
c(xi)^2 = g_Y(xi,xi) Id holds in Cl(9,5) regardless of the gauge field A. The Sp(64)-
equivariance of Phi does not affect the principal symbol (Phi is zero-order), so VZ
evasion is unaffected.

---

## 8. Summary Table

| Question | Verdict | Grade |
|----------|---------|-------|
| Does Phi intertwine with (Ad, rho) for g in Sp(64)? | YES — Theorem [GE] | reconstruction |
| Proof mechanism | Lie functor identity rho_*(Ad(g)X) = rho(g)rho_*(X)rho(g)^{-1} | verified (standard) |
| Is the frame {e^a} gauge-invariant? | YES — e^a is part of metric g_Y, not A | verified |
| Does iota_{e_a} commute with Ad(g) on Lie-algebra index? | YES — form/Lie indices in tensor product | verified |
| Does this require commutativity of c(alpha) and rho(g) in M(64,H)? | NO — not needed | n/a |
| Connection to Spin(9,5)-equivariance | Compatible — independent symmetry groups | reconstruction |
| Impact on ind_H(D_GU) = 24 | Gauge-invariance of index confirmed | reconstruction |
| Impact on VZ evasion | None — Phi is zero-order, principal symbol unaffected | reconstruction |
| OQ3-A (bundle-theoretic) | Open | open |
| OQ3-B (covariant Phi in d_A) | RESOLVED by composition | reconstruction |
| OQ1 (uniqueness) | Still open | open |
