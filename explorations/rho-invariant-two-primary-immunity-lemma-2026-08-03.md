---
title: "The rho-invariant 2-primary immunity lemma: for pi_1 = Z/2 the twisted-minus-untwisted APS eta lies in Z[1/2] (register M-M10; audit topo-7)"
status: active_research
doc_type: exploration
lane: "1"
created: 2026-08-03
updated: 2026-08-03
outcome: "LEMMA-STATED-AND-PROVED; STANDARD-RESULT-APPLIED; PERMANENTLY-IMMUNIZES-3-PRIMARY-CLAIMS-AGAINST-2-ADIC-CONVENTION-WORRIES"
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
grade: "standard-result-applied (APS I-III, Donnelly 1978, ABP 1967; the proof below is an assembly of cited theorems plus elementary arithmetic, not new mathematics)"
register_item: M-M10 (lab/process/improvement-register-2026-08-03.md)
depends_on:
  - canon/boundary-einvariant-and-the-tangential-fork.md
  - canon/two-primary-lemma.md
related:
  - explorations/framing-composite-mod3-2026-08-03.md
  - canon/pin14-bordism-derivation-RESULTS.md
---

# The ρ-invariant 2-primary immunity lemma

## Purpose

The boundary-eta program has repeatedly had to argue, case by case, that
2-adic convention subtleties (spin-structure choice ±1/8, the lens factor
1/p = 1/2, e_R-vs-e_C factor 2, the 3/8 gravitational shift) cannot touch
its 3-primary conclusions — see the four-subtlety audit in
`canon/boundary-einvariant-and-the-tangential-fork.md` §2–3 and the germ
recorded there in Verification 2: *"any spectral/gauge invariant on S³/Z₂
lies in Z[1/2]"*. This note upgrades that case-by-case pattern to a single
standard-result-applied lemma that immunizes every present and future
3-primary claim on the RP³ spine — and on the 13-dimensional boundary,
whose relevant π₁ factor is the same Z/2 — against the entire class of
spectral/ρ-invariant convention worries at once.

## The lemma

> **Lemma (ρ-invariant 2-primary immunity).** Let M be a closed
> odd-dimensional spin manifold equipped with a map c: M → BZ/2 (a double
> cover), let D be a Dirac-type operator on M (spin Dirac, signature, or a
> Z/2-equivariant twist thereof), and let α be the nontrivial character of
> Z/2 with associated flat line bundle L_α. Write ξ = (η + dim ker)/2 for
> the APS reduced eta. Then the **relative (twisted minus untwisted) eta**
>
>     ρ_α(M, D) := ξ_α(M, D) − ξ(M, D)   (mod Z)
>
> lies in **Z[1/2]/Z ⊂ Q/Z**: its value is a dyadic rational mod 1. In
> particular its image in any odd-primary summand (e.g. the Z/3 of
> π₃ˢ = Z/24 = Z/8 ⊕ Z/3) is zero, and **no** spin-structure, lens-factor,
> or e_R-vs-e_C convention change — each of which changes the answer by a
> difference of such relative-eta invariants — can perturb any 3-primary
> claim.

**Proof (bordism-exponent route; every ingredient cited).**

1. *ρ_α mod Z is a reduced-spin-bordism invariant of (M, c).* If
   (M, c) = ∂(W, c̃) with W compact spin and the double cover extending,
   then the APS index theorem [APS I] applied to D_W with coefficients in
   L_α and in the trivial bundle gives
   ξ_α(M) − ξ(M) ≡ −(ind_α − ind) − ∫_W Â(W)·(ch(L_α) − 1) (mod Z).
   Since L_α is flat, ch(L_α) = 1 pointwise and the integral term vanishes
   identically; the index difference is an integer. Hence ρ_α ≡ 0 mod Z on
   boundaries, and ρ_α is additive under disjoint union, so ρ_α mod Z is a
   homomorphism on the reduced bordism group Ω̃^Spin_n(BZ/2). (This step
   is the standard flat-coefficient APS argument — [APS II] §§2–4, where ρ
   is introduced for flat unitaries; the local-index-density cancellation
   for the *difference* is exactly why the lemma concerns the relative
   eta, not the twisted eta alone.)
2. *The receiving group is a finite 2-group in every degree.* The
   Atiyah–Hirzebruch spectral sequence for Ω̃^Spin_*(BZ/2) has
   E² = H̃_p(BZ/2; Ω^Spin_q); every reduced homology group of BZ/2 = RP^∞
   with finitely generated coefficients is killed by 2 in positive degree
   (H̃_p(RP^∞; Z) = Z/2 for p odd, 0 for p even; odd-torsion coefficients
   contribute 0). Hence Ω̃^Spin_n(BZ/2) is a finite 2-group for every n —
   the Anderson–Brown–Peterson structure of spin bordism ([ABP 1967];
   "spin-bordism torsion is all 2-primary", the same fact recorded at
   `explorations/global-anomaly-leg-2026-07-20.md:252`).
3. *Exponent finishes.* Let 2^N = exponent of Ω̃^Spin_n(BZ/2). Then
   2^N·(M, c) bounds, so by steps 1–2, 2^N·ρ_α ≡ 0 (mod Z), i.e.
   ρ_α ∈ (1/2^N)Z/Z ⊂ Z[1/2]/Z. An element of Z[1/2]/Z projects to zero
   in every odd-primary summand of any finite quotient (gcd(2^N, odd) = 1,
   CRT). ∎

**Second framing (G-index route, the parent citation of the register
item).** For the free involution τ on the double cover M̃ (quotient M),
ρ_α is the τ-weighted equivariant eta of M̃ up to sign
(ξ_τ(M̃) = ξ(M) − ξ_α(M) by the transfer/character decomposition), and
Donnelly's G-eta theorem [Donnelly 1978] together with the G-index theorem
of [APS III] computes it on any bounding G-manifold as a sum of defect
terms with denominators dividing |G|·(character-ring denominators). For
G = Z/2 the character group is 2-primary and all character values lie in
{±1} ⊂ Z, so every denominator is a power of 2 — the same conclusion, from
the equivariant side. (For the signature operator [APS II §4] proves
ρ_α ∈ Q directly; the 2-power denominator statement for G = Z/2 follows as
above.)

## Quantitative check (the lemma reproduces the known denominators)

For n = 3: the only contributing ABP summand below degree 8 is ko, and
k̃o₃(BZ/2) = Z/8, so Ω̃^Spin_3(BZ/2) ≅ Z/8, exponent 2³. The lemma then
says ρ ∈ (1/8)Z mod Z on RP³ — exactly the hardening-audit closed form
η̄(charge-q Dirac on L(2;1)) = (2q² − 4q + 1)/8, 2-primary for every q
(`canon/boundary-einvariant-and-the-tangential-fork.md` §7), and exactly
the gauge-adjoint value 3/8. The lemma is the structural reason those
denominators had to be powers of 2.

For n = 13 (the actual boundary dimension): Ω̃^Spin₁₃(BZ/2) ≅ Z/2 — this
is the very group computed in the Pin⁺ degree-14 derivation
(`canon/pin14-bordism-derivation-RESULTS.md`, via Ω^{Pin+}₁₄ ≅
Ω̃^Spin₁₃(BZ/2)), so the exponent is 2 and the lemma holds on the 13-dim
boundary with N = 1.

## Consequences (what is now immune, permanently)

1. **The four flagged convention subtleties** of the boundary-e-invariant
   computation (spin structure ±1/8; lens factor 1/2; e_R vs e_C factor 2;
   the 3/8 gravitational shift) are differences of π₁ = Z/2 relative-eta
   data, hence lie in Z[1/2]: they *provably cannot* reach the Z/3 summand.
   The canon's case-by-case verification ("all strictly 2-adic",
   Verification 1–3) is now a one-line corollary.
2. **On the RP³ spine:** any spectral/gauge invariant built from
   Z/2-twisted eta data on S³/Z₂ lies in Z[1/2] (the Verification-2 germ,
   now with a proof and citations). The entire 3-primary burden of the
   program therefore sits where the canon already put it: in the
   tangential framing channel −p₁/24 (a framed-bordism datum, not a
   spectral one), whose mod-3 arithmetic is governed by the framing-shift
   lemma of `explorations/framing-composite-mod3-2026-08-03.md`.
3. **On the 13-dimensional boundary:** the link is an S⁶-bundle over the
   RP³ spine (13-dim total; `canon/boundary-einvariant-and-the-tangential-fork.md`
   §7); its relevant fundamental-group factor is the same Z/2 (S⁶ and the
   6-sphere fibers are simply connected), so every character-twisted
   relative eta pulled back through the Z/2 classifying map obeys the
   lemma verbatim, with exponent 2 in degree 13. No lens-factor or
   spin-structure bookkeeping on the actual boundary can move a 3-primary
   claim either.
4. **Scope fence (what the lemma does NOT say).** It does not say the
   boundary carries a nonzero 3-part (that is the tangential-fork premise,
   V15-5), and it does not constrain framed-bordism/J-homomorphism data —
   the framing channel is *not* a π₁ = Z/2 relative-eta invariant, which
   is precisely why the order-3 carrier can live there while every
   spectral route is 2-adically frozen. It also complements
   `canon/two-primary-lemma.md` from the opposite side: that lemma says
   the program's obstructions cannot *force* an odd count; this one says
   convention noise cannot *fake or destroy* one.

## Citations

- M. F. Atiyah, V. K. Patodi, I. M. Singer, *Spectral asymmetry and
  Riemannian geometry* I, II, III, Math. Proc. Camb. Phil. Soc. 77 (1975)
  43–69; 78 (1975) 405–432 (ρ_α for flat unitaries, §§2–4); 79 (1976)
  71–99 (the G-index / rationality side).
- H. Donnelly, *Eta invariants for G-spaces*, Indiana Univ. Math. J. 27
  (1978) 889–918 (equivariant eta and its index-theorem evaluation).
- D. W. Anderson, E. H. Brown, F. P. Peterson, *The structure of the Spin
  cobordism ring*, Ann. of Math. 86 (1967) 271–298 (spin bordism torsion
  is 2-primary; the coefficient inputs).
- In-repo germ: `canon/boundary-einvariant-and-the-tangential-fork.md`
  §2 Verification 2 ("any spectral/gauge invariant on S³/Z₂ lies in
  Z[1/2]") and §7 (the (2q² − 4q + 1)/8 closed form).

Per the repo's oq3b forensic standard, the three external citations above
were confirmed at statement level against the standard literature during
the 2026-08-03 audit cycle; page-level re-verification against primary
texts should accompany any *publication* use (the same caveat the
mathematician-panel synthesis §6 applies to its own external
attributions).

## Grade

standard-result-applied; claim_status_change: none. No verdict moves; no
new mathematics is claimed. The value added is structural: one cited lemma
retires an entire recurring class of 2-adic convention objections against
the program's 3-primary claims, on the spine and on the honest boundary.
