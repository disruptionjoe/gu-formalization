---
title: "The boundary e-invariant of the self-dual twist on RP^3, and the tangential-vs-gauge fork"
status: active
doc_type: result
created: 2026-06-28
grade: "specialist-grade applied index theory + stable homotopy, NOT machine-checked; CONDITIONAL on one named physics fork; favored reading lands the profound result but is not proven"
source: "3 independent routes (APS-Gilkey eta, Chern-Simons/bounding-4-manifold, framed-bordism/J-homomorphism) + 3 adversarial verifications + synthesis (7 agents); the verification corrected our own 1/6 -> 1/12"
depends_on: [explorations/a5-einvariant-specialist-question-and-attempt-2026-06-28.md, canon/firewall-boundary-hypothesis.md]
---

# The Decisive Computation: 3-Primary e-Invariant of the Charge-1 Self-Dual SU(2)+ Twist on RP³ = L(2;1)

## Summary verdict (read this first)

The narrow question -- does the twist's class in π₃ˢ = Z/24 = Z/8 ⊕ Z/3 have a nonzero order-3 component -- **is not settled by index theory alone.** It collapses to a single interpretive fork in how Geometric Unity realizes the SU(2)+ twist:

- **If the twist is a tangential framing modification** (the SU(2)+ = Λ²₊ is the self-dual half of the SO(4) frame bundle, i.e. a tangential structure): the answer is **YES, nonzero order-3**, with corrected value **e = 1/12** (not the 1/6 the original routes published). The conditional profound result lands: the generation count 3 is forced at the boundary by Adams' theorem, in exactly the sector the 2-primary no-go cannot reach.
- **If the twist is a gauge-coefficient bundle in the matter Dirac operator** (integer ch₂ = 4, evaluated as an APS boundary defect on the lens space): the answer is **NO, purely 2-primary**, e = ±3/8, and the kill is complete even at the boundary.

Everything downstream depends on which of these two the GU construction actually instantiates. Index theory cannot pick for us; the physics of the construction must declare it.

---

## 1. The most defensible value of the e-invariant

**Under the tangential-framing reading (the reading the phrase "its class in π₃ˢ" literally demands):**

$$e_R = \tfrac{1}{12} \in \mathbb{Q}/\mathbb{Z}, \qquad \text{class } 2 \in \mathbb{Z}/24 = \mathbb{Z}/8 \oplus \mathbb{Z}/3$$

CRT decomposition: 2 → (2 mod 8, 2 mod 3) = (2, 2).

- **3-primary part: 2 ∈ Z/3  --  NONZERO, order 3.**
- 2-primary part: 2 ∈ Z/8 (order 4). This piece is genuinely convention-sensitive and is the least certain part of the answer.

**Why 1/12 and not the originally published 1/6.** All three adversarial verifications independently converged on the same correction: Routes A and C overcounted the framing multiplier by a factor of 2. The framing degree that the J-homomorphism actually sees is the **stable** class in π₃(SO), which is p₁/2, not the unstable SO(3) Pontryagin number or the Dynkin index.

- Ad: SU(2) → SO(3) is an isomorphism on π₃ (it is the universal cover), but the stabilization SO(3) → SO is **multiplication by 2**.
- p₁/2 : π₃(SO) → Z is an isomorphism; the generator ν has p₁ = 2.
- The adjoint charge-1 bundle has p₁ = 4, so its framing degree is 4/2 = **2**, giving e_R = 2 × (1/24) = **1/12**.

Routes A and C used the twisted-Dirac index ch₂(adjoint) = 2·T(adj)·k = 4 directly as the framing degree, hybridizing the gauge Dynkin index (4) with the gravitational denominator (24). That produced 4/24 = 1/6. The yes/no survives the correction (2 is coprime to 3, still nonzero mod 3), but the published rational 1/6 and the 2-primary part derived from it are wrong by a factor of 2.

**The fundamental twist would give** e = 1/24 (class 1), also nonzero 3-part. **The one multiplier that would kill the 3-part is 3** (the adjoint *dimension*), which is index-theoretically the wrong reading and is correctly rejected by every route: the framing degree is 2 or 4, never 3.

**Under the competing gauge-coefficient reading (Route B):** e = ±3/8 = class ±9 in Z/24. Since 9 ≡ 0 (mod 3), the 3-primary part is identically zero. The published "1/6" is not attained in either internally consistent computation.

---

## 2. Do the three routes agree, and at what confidence?

**They do not agree on the load-bearing yes/no.**

| Route | Method | e-value | 3-primary part | Confidence |
|---|---|---|---|---|
| A | APS–Gilkey η finite sum | 1/6 (flagged 1/12) | nonzero, order 3 | medium |
| B | Chern–Simons / bounding 4-manifold | ±3/8 | **zero** | medium |
| C | Framed bordism / J-homomorphism | 1/6 | nonzero, order 3 | high (on yes/no) |

**Adversarial adjudication of the split:**

- **Verification 1 (index-theory referee):** sides with A/C on the binary (nonzero) but corrects the value to 1/12 (class 2). Identifies Route B's error precisely: B conflates the twisted-Dirac *index* with the framed-bordism *class*, discarding the charge-1 instanton's asymptotic pure-gauge winding g⁻¹dg -- which is exactly the J-homomorphism input -- by replacing it with a flat holonomy-(−1) connection. B answers a different question (flat-boundary ρ-invariant) than the one posed. Verdict: boundary-carries-order-3, confidence medium.
- **Verification 2 (3-primary extraction audit):** verdict **undetermined-needs-specialist**, confidence medium. Confirms the split is an *interpretive value disagreement*, not an extraction slip. Confirms independently that any spectral/gauge invariant on S³/Z₂ lies in Z[1/2] (so Route B is right that no *spectral* denominator-3 exists), but that the tangential framing defect d/24 is a *different operation* not excluded by that fact.
- **Verification 3 (lens-factor handling):** verdict **undetermined-needs-specialist**, confidence medium. Confirms the Z₂ lens factor is a 2-adic red herring for the 3-part (L(3;1) gives −1/3, L(2;1) gives only ±1/8), and that the real question is whether the SU(2)+ twist feeds the gravitational framing channel −p₁/24, where the von Staudt–Clausen 3 inside 24 actually lives.

**Consensus that did emerge across all verifications:**
1. The originally published value **1/6 is wrong**; the correct framing value is **1/12**.
2. The four flagged subtleties (spin structure ±1/8, lens factor 1/2, e_C-vs-e_R factor 2, the 3/8 gravitational shift) are **all strictly 2-adic** and provably cannot touch the Z/3 summand. No arithmetic error in any route on these.
3. The entire disagreement reduces to **one interpretive fork**: tangential framing vs gauge coefficient.

So: routes agree on the *machinery* and on the 2-adic irrelevance of the subtleties, and agree the value is 1/12 once corrected -- but they **split on the binary**, and two of three independent referees call the binary **undetermined** pending a single physics input.

---

## 3. Explicit assumptions the answer depends on

| Assumption | Setting used | Effect on 3-part |
|---|---|---|
| **Spin structure** | RP³ = L(2;1) has two; bare Dirac η = ±1/8 | sign of 2-primary part only; 3-part untouched |
| **Lens factor** | Z₂ quotient enters as 1/p = 1/2, a 2-adic unit inverse | none -- red herring for the 3-part (verified: L(3;1) → −1/3 but L(2;1) → ±1/8) |
| **Normalization** | e_R (KO/real) is the complete order-24 invariant in dim ≡ 3 mod 8, e_R(ν) = 1/24; e_C "sees only half" (order 12, e_C(ν) = 1/12) | factor-of-2, 2-primary; the original "e_C(generator) = 1/24" anchor is imprecise -- it is e_R that pins \|Im J₃\| = 24 |
| **Adjoint vs fundamental** | framing degree = p₁/2 = **2** for the adjoint charge-1 bundle (NOT Dynkin index 4, NOT dimension 3) | sets value 1/12; binary nonzero is stable across fund (1/24) and adjoint (1/12); dies only at multiplier 3 |
| **THE LOAD-BEARING FORK** | tangential framing (Λ²₊ ⊂ SO(4) frame bundle) **vs** gauge coefficient (matter Dirac twisted by adjoint, integer ch₂ = 4) | **tangential → nonzero order 3; gauge-coefficient → zero.** This single choice decides the whole question. |

---

## 4. The verdict

**The boundary class is undetermined by index theory; it is fixed by one physics declaration.**

- **Tangential reading (favored, not proven):** The self-dual SU(2)+ = Λ²₊ is literally the self-dual half of the SO(4) tangent-frame group, hence a *tangential* structure. Under this reading the twist feeds the gravitational Â-genus framing channel −p₁/24, which carries the von Staudt–Clausen 3 inside 24. The class is **2 ∈ Z/24**, e = **1/12**, 3-primary part **= 2 ∈ Z/3, nonzero order 3.** → **The conditional profound result lands:** GU's matter-generation count reduces to one boundary class, and the canonical charge gives a nonzero order-3 element, forcing generation count 3 by Adams' theorem in precisely the sector the 2-primary bulk no-go is structurally blind to.

- **Gauge-coefficient reading (Route B, live alternative):** If the twist is genuinely a gauge coefficient in the matter Dirac operator with integer ch₂ = 4, then on the 2-primary lens boundary the only surviving fractional term is the 2-adic gravitational defect −(3/8)σ(X). The class is **±9 ∈ Z/24**, 3-primary part **= 0.** → **The kill is complete even at the boundary**; the 3-primary summand is unreachable from the lens boundary just as it is from the bulk.

This is **not** a closed kill and **not** a closed profound result. It is a result conditioned on one sub-question.

**The single sub-question that settles it:**

> Does the GU construction realize the self-dual SU(2)+ = Λ²₊ twist as a **tangential framing modification** of RP³ (which injects the 3-divisible J-homomorphism generator 1/24 through the gravitational −p₁/24 channel, even though RP³ is a 2-primary manifold), or as a **gauge-coefficient bundle** in the matter Dirac operator (integer-quantized ch₂ = 4, whose only boundary residue on L(2;1) is the 2-adic gravitational η)?

Tangential → **YES, order-3, generation count 3 forced at the boundary.**
Gauge-coefficient → **NO, purely 2-primary, kill complete.**

The phrase "its class in π₃ˢ" grammatically favors the framing/framed-bordism reading, and the identity SU(2)+ = Λ²₊ ⊂ SO(4) is a genuinely tangential structure, both of which tilt toward YES. But neither is decisive, and Route B's reading is internally consistent and cannot be excluded by index theory.

---

## 5. Honest grade and what a human specialist must still confirm

**Grade:** Specialist-grade *applied* index theory / stable homotopy. **Not machine-checked.** The standard anchors are verified or standard:

- π₃ˢ = Z/24 = Im J₃; e_R(ν) = 1/24 = denom(B₂/4) (von Staudt–Clausen: 3 | 6 because (3−1) | 2). Solid.
- Bare RP³ = L(2;1) Dirac reduced η = ±1/8 (numerically exact: single-term csc² sum at k = 2), signature η = 0, flat-adjoint Chern–Simons ≡ 0 (Ad(−1) = id). Solid and confirmed.
- The four flagged subtleties are provably 2-adic. Solid.
- The factor-of-2 correction 1/6 → 1/12 (framing degree p₁/2 = 2, from SO(3) → SO being ×2). Solid, agreed by all three referees.

**What is reconstruction-grade / unconfirmed:**

1. **The interpretive fork itself** (tangential vs gauge-coefficient). This is the entire ballgame and is a statement about the GU construction, not about index theory. A human must read off from the GU matter-sector definition whether Λ²₊ enters as a tangential framing or a gauge coefficient. No literature source was found computing the exact RP³ charge-1 SU(2)-adjoint twisted η in either reading (the 1-form-symmetry paper 2509.22788 and the lens-space Dirac-spectrum papers do not; the "e-Invariant of Twisted Dirac Operators of S³/Γ" paper was inaccessible, HTTP 403).
2. **Whether, under the tangential reading, the framing defect is honestly d/24 with d = p₁/2 = 2.** The referees reconstructed this by hand (Ad iso on π₃, ×2 stabilization, p₁/2 iso); it should be checked against an explicit Sp(1)×Sp(1) = Spin(4) decomposition / equivariant-instanton-at-fixed-point computation on the A₁ = D⁴/Z₂ orbifold.
3. **The exact 2-primary part** (2, vs the candidates 4, 9, 5, ... depending on spin structure and whether the 3/8 gravitational shift is folded in). This does not affect the 3-primary conclusion but is not pinned.

**Bottom line.** The robust, defensible facts are: (a) the corrected value is **1/12, not 1/6**; (b) every flagged convention subtlety is 2-adic and cannot reach Z/3; (c) the binary answer is controlled entirely by **one interpretive choice**, with two of three independent referees calling it **undetermined-needs-specialist** and one calling it nonzero. Under the most defensible reading (tangential Λ²₊ framing) the answer is **YES, nonzero order-3, and the conditional profound result holds**; under Route B's gauge-coefficient reading it is **NO and the kill is complete.** Do not report this as a closed result either way. Report it as: *one well-posed sub-question away from decisive, with the tangential reading favored but not proven.*

---

## 6. Addendum: independent first-principles resolution -- the fork resolves TANGENTIAL (2026-06-28)

An independent agent, given only the self-contained fork question (no access to this computation), worked
part (a) from first principles and resolved it the same way: **TANGENTIAL**. The reasoning, which is a
genuinely independent second derivation:

- The April 2021 draft reduces the observerse structure group via
  `Spin(7,7) -> Spin(6,4) -> Spin(6) x Spin(4)`. The `Spin(4) = SU(2)+ x SU(2)-` factor is explicitly tied
  to the local frame rotations of the 4-base `TX^4`, and the self-dual summand `su(2)+` is generated by the
  self-dual 2-forms `Lambda^2_+` of that base.
- The Rarita-Schwinger field is a 1-form-valued spinor whose vector index lives in the full 14D tangent
  space, decomposing as `TY ~ TX^4 (+) N^10` (base frame + internal normal). The matter Dirac/RS operator's
  covariant derivative therefore couples `Lambda^2_+` through the **Levi-Civita spin connection** on the
  base frame directions, NOT through a separate internal gauge potential `omega`. The draft explicitly
  separates the metric-induced Levi-Civita spin connection (carrying the base frame, including its self-dual
  part) from the additional gauge potentials `omega` that handle the internal Pati-Salam factors; `su(2)+`
  is on the frame side. So `Lambda^2_+` enters as a tangential framing.
- The attack ("in a unified theory everything is gauge / Spin(7,7) treats all connections symmetrically")
  fails because the draft distinguishes the Levi-Civita spin connection from `omega`, and the self-dual
  `su(2)+` is not among the internal gauge fields from the normal-bundle reduction.
- It independently confirmed the index theory: `p_1(ad P) = +/- 4` for the charge-1 self-dual bundle, the
  stabilization `SO(3) -> SO` multiplies by 2, the framing degree is `p_1/2 = 2`, so `e_R = 2/24 = 1/12`;
  and the gravitational framing channel `-p_1/24` carries the von Staudt-Clausen 3, giving the nonzero
  3-primary part. The gauge reading is disfavored by the construction.

**Updated verdict.** With two independent first-principles analyses agreeing on the tangential reading, the
fork is **resolved tangential at reconstruction grade**: GU's matter sector, read through its own
`4+10 / Spin(4)-frame` structure, places `Lambda^2_+` as a tangential framing, so the boundary e-invariant
carries a nonzero 3-primary part (`e_R = 1/12`, class 2 in `Z/24`), and Adams' theorem forces generation
count 3 in exactly the sector the 2-primary bulk no-go is blind to. This remains **reconstruction-grade**
(it is an inference from the 4+10 split, the frame identification of `Spin(4)`, and the RS vector-index
structure -- NOT a theorem of the published draft, whose explicit matter operator / source action is
unbuilt). It is robust within the available data and the gauge alternative is positively disfavored, but a
final theorem awaits GU's explicit matter Dirac/RS operator. Further deep-research input is incoming and may
sharpen or qualify this.