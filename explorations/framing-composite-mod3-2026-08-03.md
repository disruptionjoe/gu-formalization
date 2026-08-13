---
title: "Framing composite mod 3: the {0,4} ambiguity decided into a one-bit convention datum (register M-M9; audit HB-02/B6)"
status: active_research
doc_type: exploration
created: 2026-08-03
updated: 2026-08-03
outcome: "COMPOSITE-DECIDED-BY-ONE-RELATIVE-SIGN; H1-SHIFT-LEMMA-PROVED; NO-GU-BRANCH-ASSERTED"
canon_verdict_change: none
grade: "EXACT arithmetic + named-premise fork (the arithmetic is exact and machine-certified; which branch is GU's remains the declared V15-5 premise)"
register_item: M-M9 (lab/process/improvement-register-2026-08-03.md)
audit_findings: [HB-02, B6]
runnable:
  - tests/boundary-eta/framing_composite_mod3.py
depends_on:
  - canon/boundary-einvariant-and-the-tangential-fork.md
  - tests/boundary-eta/v15_framing_convention_sensitivity.py
  - lab/process/eleven-lens-audit-2026-08-03.md
---

# Framing composite mod 3: deciding the {0,4} ambiguity

## Result (read this first)

The eleven-lens audit (B6, downgraded CRITICAL→MAJOR because the V15-5
certificate declares its premise openly) found that the carrier derivation
conflates **two different p₁ = 4's**:

1. **p₁(X₂, φ₊) = 4** — the Kirby–Melvin *relative Pontrjagin number of the
   natural framing* of RP³ = L(2;1) = SO(3), computed against the Euler +2
   disk bundle X₂ over S² (a class-of-a-framed-manifold datum), and
2. **p₁(ad P) = −4c₂ = ∓4** — the Pontrjagin number of the charge-1 adjoint
   clutching bundle, whose role is a *change-of-framing degree* (stable
   degree p₁/2 = ±2 via the ×2 stabilization π₃(SO(3)) → π₃(SO)).

Under the twist-on-top-of-the-natural-framing reading, the honest object is
the **composite** class

    c = n + t = (∓2) + (±2) ∈ Z/24,  i.e.  c ∈ {0, ±4},

which is the audit's {0,4} ambiguity. This note converts that ambiguity into
a **decided statement**:

> **The {0,4} set is not a free ambiguity of the mathematics. It is the two
> fibers of ONE binary convention datum ε = s₁s₂ (the relative sign between
> the natural-framing class and the twist degree). ε = +1 gives c = ±4 with
> 3-part in {1,2} (nonzero); ε = −1 gives c = 0 with 3-part zero. ε is
> invariant under every orientation/generator relabeling, so it is a genuine
> binary about the construction — and the datum that fixes it is named
> below.**

Machine certificate: `tests/boundary-eta/framing_composite_mod3.py`
(38 hard assertions, exact integer/Fraction arithmetic, positive controls
first, exit 0; exits nonzero on any failure).

**What is deliberately NOT asserted:** which branch is GU's. That is the
declared reconstruction-grade premise of the V15-5 certificate
(`tests/boundary-eta/v15_framing_convention_sensitivity.py`: "Lambda^2_+ is
identified with this exact tangential framing", verdict
`PASS_WITH_DECLARED_GU_TANGENTIAL_IDENTIFICATION_PREMISE`) and of
`canon/boundary-einvariant-and-the-tangential-fork.md` (the tangential fork,
resolved tangential at reconstruction grade only). Under the V15-5
*identification* premise the object is the natural framing itself (class
±2, 3-part nonzero for both label signs) and the composite question does not
arise; under the *composite* reading the branch is picked by ε. Index theory
cannot pick; the construction must declare.

## 1. Fixed convention (all sign data named once)

| # | datum | value fixed here | flip effect |
|---|---|---|---|
| C1 | orientation of the spine | RP³ = ∂X₂, X₂ = Euler +2 disk bundle over S², boundary orientation (per the canon fork file / V15-5) | flips n AND t → ε invariant |
| C2 | generator labels | e_R(ν) = +1/24 (Adams), class(ν) = +1 ∈ Z/24 | relabels the group → flips n and t together → ε invariant |
| C3 | natural framing | Kirby–Melvin right-handed Lie framing φ₊ on SO(3): h(φ₊) = 3 − m = **+1** at m = 2, hence p₁(X₂, φ₊) = h + 3σ(X₂) = **+4** | selecting the left framing φ₋ flips n alone → flips ε |
| C4 | twist duality | charge-1 adjoint clutching **self-dual vs anti-self-dual w.r.t. C1**; p₁(ad P) = −4c₂, stable degree ±2 | flips t alone → flips ε |
| C5 | action convention | composite = class(natural) + degree(twist), framing acted on the right | inverse convention flips t; must be co-declared with C4 |

Literature anchors (Kirby–Melvin, *Canonical framings for 3-manifolds*,
Turkish J. Math. 23 (1999), arXiv:math/9903056): the Hirzebruch defect is
h(ψ) = p₁(W, ψ) − 3σ(W) for any compact oriented W bounding M; the total
defects of the Lie framings are H(S³, φ±) = (0, ±2) and H(SO₃, φ±) =
(0, ±1); the quotient framing on L(m;1) has h(φ₊) = 3 − m; and the
π₃(SO(3))-generator α acts by p₁ ↦ p₁ + 4 (their Lemma 2.3a) — which **is**
the ×2 stabilization in p₁/2 form. The homogeneous-space value h = 1 and
the bounding-manifold value p₁(X₂, φ₊) = 4 = h + 3σ are two KM data that
cohere on the same convention; the certificate checks the coherence.

**The e-invariant formula and its hypothesis (audit B7/P-H26).** The class
is read off via e_R[M, ψ] = s·p₁(W, ψ)/48 for W a compact **spin** filling
with ψ spin-compatible (the canon cites Randal-Williams for this formula;
the missing bibliography entry and the unstated W-spin hypothesis are
tracked for the Zenodo v1.0.1 batch under P-H26 — this note *states* the
hypothesis and *checks* it). The spin hypothesis is load-bearing and
machine-visible: a closed spin 4-manifold has p₁ = 3σ ∈ 48Z (Rokhlin), so
the formula is filling-independent across spin fillings; the non-spin
Euler +1 filling of S³ (CP² minus a ball, rel p₁ = 3) yields 3/48 = 1/16,
which is not even a Z/24 class (24·(1/16) ∉ Z) — the certificate
demonstrates the failure. X₂ itself is spin (w₂ = Euler number mod 2 = 0).

## 2. The computation

All in Z/24 = Z/8 ⊕ Z/3 (CRT), certificate Parts 1–2, 4:

- **Natural-framing class of RP³:** n = s₁·(p₁/2) = s₁·2, i.e. **∓2 ∈
  Z/24** with e_R = ∓1/12; 3-part = 2 or 1 — nonzero for both label signs.
- **Change-of-framing degree of the charge-1 adjoint twist:** t = s₂·2,
  i.e. **±2**, from |p₁(ad P)| = 4 and the ×2 stabilization (never the
  Dynkin index 4, never the dimension 3).
- **Both relative signs' composites:**

  | s₁ | s₂ | ε = s₁s₂ | c = n + t ∈ Z/24 | c mod 3 |
  |---|---|---|---|---|
  | +1 | +1 | +1 | 4 | 1 (nonzero) |
  | +1 | −1 | −1 | 0 | 0 |
  | −1 | +1 | −1 | 0 | 0 |
  | −1 | −1 | +1 | 20 (= −4) | 2 (nonzero) |

  Reduced mod 3: **{0} for ε = −1 vs {1,2} for ε = +1.** The global
  relabelings (C1, C2) flip s₁ and s₂ together, so ε and the
  zero/nonzero-3-part decision are invariant — certified exhaustively.
- **V15-5 cross-check:** in V15-5's coordinates (base object = the twist,
  d = 2) the composite reading enters as a framing shift k = n; the
  composite vanishes exactly when k = −2 ≡ 1 (mod 3), matching V15-5's own
  erasure rule "P3 vanishes iff k ≡ 1 mod 3".

**Honesty guard.** The exact 2-primary part of the RP³ natural-framing
class is *not* pinned (canon fork file §5 item 3); every load-bearing
statement above about RP³ classes is therefore either a formula-output
labeled with its hypothesis or a mod-3 statement. The mod-3 statements are
immune to every 2-primary correction by the lemma below plus the
ρ-invariant immunity lemma
(`explorations/rho-invariant-two-primary-immunity-lemma-2026-08-03.md`).

## 3. The H¹(RP³;Z/2) framing-shift lemma (proved)

Sixteen of the twenty-four classes of Z/24 have nonzero 3-part, so "the
3-part is nonzero" is generic, not automatic — an uncontrolled framing
shift could in principle land anywhere. RP³ has |H¹(RP³;Z/2)| = 2 spin
structures and correspondingly a non-degree direction in its framing set
(Kirby–Melvin: F ≅ H¹(M;Z/2) × Z × Z non-canonically). The lemma closes
that door:

> **Lemma.** Let M be a closed oriented 3-manifold with stable framing f,
> and let g: M → SO be any framing change with top-cell degree d(g) ∈ Z.
> Then
>
>   [M, f·g] − [M, f] = d(g)·ν + τ  in π₃ˢ = Z/24,  with 2τ = 0.
>
> Since the 2-torsion of Z/24 is {0, 12} and both elements have zero
> Z/3-coordinate, the 3-part of ANY framing change equals d(g) mod 3. In
> particular the H¹(M;Z/2)-indexed shifts (spin-structure flips, d = 0
> component) are **strictly 2-primary**: they cannot create or erase a
> 3-part.

**Proof.** By Pontryagin–Thom, the framed class [M, f] is the composite of
the framed collapse u_f: S³ → Σ^∞M₊ with the projection Σ^∞M₊ → S⁰, and a
framing change g twists this by the stable "unit" J(g): the difference
[M, f·g] − [M, f] is the composite of u_f with the reduced class
J(g) − 1 ∈ [Σ^∞M₊, S⁰], which is filtered by the skeleta of M. (i) The
top-cell (3-cell) contribution is d(g)·J(generator of π₃SO) = d(g)·ν, by
definition of the J-homomorphism and of d(g). (ii) Since π₂(SO) = 0, the
only sub-top-cell contribution comes from the 1-skeleton, i.e. from the
composition of g's H¹(M; π₁SO) = H¹(M;Z/2) component with
J(π₁SO) = η ∈ π₁ˢ. Every such contribution is a stable composite with η on
one side; composition in the stable category is bilinear and 2η = 0, so
each such term τ satisfies 2τ = 2(x∘η) = x∘(2η) = 0. (iii) The 2-torsion
subgroup of Z/24 is {0, 12} = {0, η³} (η³ = 12ν; 2-locally 4ν, CRT (4,0)),
and an element of order dividing 2 in Z/8 ⊕ Z/3 has zero Z/3-coordinate
(Z/3 has no 2-torsion). Hence 3-part([M,f·g] − [M,f]) = d(g) mod 3. (iv)
Well-definedness of d(g) for M = RP³: a g trivial on the 1-skeleton is,
since π₂SO = 0, homotopic to one trivial on the 2-skeleton and factors
through M/M⁽²⁾ ≃ S³; the indeterminacy of the factorization lies in the
image of [ΣRP², SO] → [S³, SO] = Z, which is the image of a finite group
in Z, hence 0. ∎

Arithmetic side certified exhaustively in Part 3 of the runnable (η³ = 12ν
CRT (4,0); 3-part(d·ν + τ) = d mod 3 for all d ∈ [−24, 24], τ ∈ {0, 12}).

**Consistency instance.** The known KM data even exhibit the lemma: the
right- and left-handed Lie framings of SO(3) (the canonical framings of
its two spin structures) differ by a π₁-nontrivial framing change whose
lift to S³ has stable degree −2 (so d = −1 on SO₃), and their classes'
3-parts differ by exactly −1 ≡ 2 (mod 3) — degree mod 3, with any residual
discrepancy confined to the unpinned 2-part, as the lemma requires.

## 4. The decision structure and the sign-audit checklist

**Decision structure.**

- **Premise A (V15-5 identification reading, the declared premise):** the
  GU twist *is* the natural tangential framing. Object class = s₁·2; 3-part
  nonzero for both signs. No composite arises. (This is what the V15-5
  certificate certifies, under its openly declared premise.)
- **Premise B (composite reading, the audit-B6 alternative):** the twist
  acts on top of the natural framing. Object class = c = 2(s₁ + s₂);
  branch decided by ε = s₁s₂:
  - **ε = +1:** c = ±4, 3-part nonzero ({1,2}).
  - **ε = −1:** c = 0, 3-part zero (the erasing branch; = V15-5's
    "shift k ≡ 1 mod 3" row).

**Sign-audit checklist — exactly which convention datum picks the branch.**

1. Fix C1 (orientation: boundary of the Euler +2 filling) and C2 (label:
   e_R(ν) = +1/24). These are pure labels: flipping either flips s₁ and s₂
   together and cannot move ε. ✔ certified.
2. Name the natural-framing datum in that orientation: KM right-handed
   φ₊ with h = +1, p₁(X₂, φ₊) = +4 (C3). This fixes s₁.
3. Name the twist's duality **in the same orientation**: is the charge-1
   adjoint clutching self-dual or anti-self-dual with respect to C1
   (equivalently: the sign of c₂(P), equivalently the ± in Λ²±)? This
   fixes s₂ — *jointly with* the declared composition convention C5.
4. **The branch-picking datum is therefore: the relative orientation
   between (a) the orientation of the spine for which the KM natural
   framing is the right-handed one and (b) the orientation of the base
   with respect to which GU's SU(2)₊ = Λ²₊ summand is the SELF-dual half.**
   That is a statement about the GU construction (which orientation the
   observerse machinery induces on the RP³ spine vs which duality the
   su(2)₊ summand carries) — the same epistemic class as the V15-5
   premise, and it is **not asserted here**.
5. Anything else (spin-structure choice, lens factor, e_R vs e_C, the 3/8
   shift, H¹ framing shifts) is strictly 2-primary and cannot move the
   mod-3 decision: the lemma of §3 plus the ρ-invariant immunity lemma.

## 5. What this changes and what it defers

- **Changes:** the {0,4} ambiguity is retired as an *ambiguity*; it is now
  a decided two-branch structure with a named one-bit selector. The
  conflation of the two p₁ = 4's is explicitly separated (a framed-class
  datum vs a change-of-framing degree).
- **claim_status_change: none.** No verdict moves. The located-not-forced
  headline is untouched (audit B6: "does not touch the headline"). The
  tangential-vs-gauge fork and the V15-5 identification premise stay
  exactly where the canon puts them.
- **Deferred (tracked elsewhere, per register):** (i) the HB-01
  "independent derivation matching" language in
  `canon/final-verdict-generation-count-and-the-open-bridge.md:51-57` — a
  CS-marked canon wording fix that should route through the claim-status
  workflow: the two p₁ = 4's are *coherent inputs on one convention chain*,
  not independent derivations of the same number; (ii) the Randal-Williams
  bibliography entry + the W-spin hypothesis statement in the published
  deposit — the P-H26 Zenodo v1.0.1 correction batch. Neither is executed
  in this note.

## 6. Grade

EXACT arithmetic + named-premise fork. The arithmetic (Z/24 CRT, the
composite table, the shift lemma's arithmetic side, the well-definedness
controls) is exact and machine-certified. The KM inputs (h = 3 − m,
p₁(X₂, φ₊) = 4, the α-action) are cited primary-source values whose
internal coherence is checked. The lemma's proof is written above
(standard stable-homotopy facts: Pontryagin–Thom, π₂SO = 0, J(π₁SO) = η,
2η = 0, η³ = 12ν). The branch selection is a named physics datum, declared
NOT decided — the same fork the canon already owns.
