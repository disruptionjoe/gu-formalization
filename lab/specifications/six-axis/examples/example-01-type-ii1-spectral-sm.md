---
title: "Example 01 — Type II_1 / Non-Embeddable Spectral Standard Model"
status: canon
doc_type: specification
updated_at: "2026-05-31"
---

# Example 01 — Type II_1 / Non-Embeddable Spectral Standard Model

| candidate | L1 substrate | L2 observer | L3 pairing | L4 causal order | L5 emergence | L6 coordination loop | first falsification test |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Type II_1 spectral SM | Type II_1 spectral triple w/ Jones-subfactor extension | Finite Turing (BPP/BQP) | Cartesian / smooth (Connes-channel) | Total-order Lorentzian | Specific-object | No loop | Connes finite-control checklist (KO-dim 6, order-one, gauge extraction, anomaly) must extend coherently to the Type II_1 regime; failure on any item kills the candidate. |

## Leg 1 — Substrate class

- **Class label:** (c) Type II_1 spectral triple with Jones-subfactor extension; non-embeddable regime allowed.
- **Specification:** Replace the finite-dimensional internal algebra `A_F = C ⊕ H ⊕ M_3(C)` of Chamseddine-Connes with a Type II_1 factor `M` carrying a faithful normal tracial state, equipped with a Jones-subfactor inclusion `N ⊂ M` of finite index whose principal graph encodes the generation structure. Allow the regime where `M` is non-embeddable into the ultrapower of the hyperfinite II_1 factor (MIP*=RE class). The internal spectral data `(A_F, H_F, D_F, J_F, γ_F)` is replaced by a Type II_1 spectral triple in the sense extending Chamseddine-Connes to non-type-I internal algebras.
- **Literature anchor:** Chamseddine-Connes spectral action (2007); Jones, Index for subfactors (Invent. Math. 1983); Ji-Natarajan-Vidick-Wright-Yuen, MIP*=RE (2020); Connes Embedding Problem and the recent negative resolution.
- **Class-assumption signature broken:** Distler-Garibaldi assumes specific finite-dimensional embedding into a compact Lie group; spectral-SM substrate sidesteps that frame entirely. No-go theorems built on finite-dimensional internal algebras (implicit in Witten-style KK reductions) do not apply to Type II_1.

## Leg 2 — Observer class

- **Class label:** (a) Finite Turing observer (BPP / BQP).
- **Specification:** The observer is a standard finite-resource quantum or classical computational agent that can compute trace values, indices, and KO-dimension invariants of finite-dimensional approximations. It cannot access the full non-embeddable structure of `M`; it sees only finite-dimensional approximants. This is the 00d-default observer; the candidate's heterodoxy is in L1, not L2.
- **Literature anchor:** Standard complexity classes BPP, BQP. The observer's failure to see non-embeddable structure is exactly the MIP*=RE separation result.
- **Class-assumption signature broken:** Preserves all four no-go theorems' observer assumptions. The candidate's strategy is to keep observer class standard so the obstruction lives entirely in substrate.

## Leg 3 — Pairing

- **Class label:** (a) Cartesian / smooth (Connes-channel).
- **Specification:** The observer-substrate coupling is the standard spectral-action channel: the observer measures spectral invariants of `(A, H, D, J, γ)` via heat-kernel / Dixmier-trace functionals. No modification to the Connes-Chamseddine extraction procedure.
- **Literature anchor:** Connes-Chamseddine spectral action principle (CMP 1997).
- **Class-assumption signature broken:** Preserves Freed-Hopkins anomaly-pairing structure; the candidate does not rely on observer-pairing enrichment.

## Leg 4 — Causal-order class

- **Class label:** (a) Total-order Lorentzian (smooth Cauchy slicing).
- **Specification:** Standard smooth Lorentzian manifold `M^4` as the external geometry; Connes-style product spectral triple `(M^4 × F)` where `F` is the Type II_1 internal triple.
- **Literature anchor:** Connes-Chamseddine almost-commutative geometry.
- **Class-assumption signature broken:** Preserves Witten 1981 causal-order assumption.
- **GU paper §12.2 note:** The GU paper §12.2 addresses L4 within GU's own framework, arguing that ℝ¹ is the unique naturally well-ordered 1-manifold and grounding the arrow of time in that algebraic fact. This candidate does not derive from the GU observerse construction and so §12.2 does not directly constrain its L4 choice. However, GU-derived candidates (those that use the Observerse triple (X, Y, {ι}) or the chimeric bundle C(Y)) should assess their L4 class against §12.2 before defaulting to Total-order Lorentzian. See `lab/sources/gu-paper-reference-surfaces.md` §3.

## Leg 5 — Emergence class

- **Class label:** (a) Specific-object substrate.
- **Specification:** `M` and `N ⊂ M` are specific Type II_1 factors / inclusions chosen to reproduce SM fermion content; they are not universality-class representatives. The candidate's bet is that a specific Type II_1 inclusion can carry chirality / 3-generation data via principal-graph data that is invisible to type-I-only no-go theorems.
- **Literature anchor:** Jones index theory; Popa's classification of subfactors.
- **Class-assumption signature broken:** Preserves emergence-class assumption.

## Leg 6 — Coordination-loop class

- **Class label:** (a) No loop.
- **Specification:** Standard fixed-substrate / read-off-observer model. No backreaction of the observer's measurement on `M`.
- **Literature anchor:** Standard spectral-action procedure.
- **Class-assumption signature broken:** Preserves coordination-loop assumption.

## Chirality bridge claim

The substrate-level invariant carrying chirality / 3-generation / gauge-group content is the **principal graph and standard invariant of the Jones-subfactor inclusion `N ⊂ M`** in the Type II_1 regime, together with the KO-dimension grading on the extended spectral triple. The forgetful operation that reduces this to the smooth-bundle shadow is the truncation to the finite-dimensional approximant chain `A_F^(n) → A_F` followed by the Connes-Chamseddine spectral-action extraction. The Distler-Garibaldi no-go computes a representation-theoretic obstruction in the finite-dimensional Lie-group frame that the truncation lands in; the obstruction is real at that frame but does not constrain the Type II_1 standard-invariant data, because non-embeddable subfactors carry indices and principal graphs with no finite-dimensional Lie-group analog. Witten 1981 / Freed-Hopkins / Nielsen-Ninomiya act on the smooth-Lorentzian × finite-internal sector and similarly compute the truncation image.

## One first falsification test

**Test:** Run the Connes finite-control checklist on a candidate Type II_1 extension. Specifically:

1. Specify a concrete Jones-subfactor inclusion `N ⊂ M` (index, principal graph) intended to encode 3-generation structure.
2. Construct the extended spectral triple `(A, H, D, J, γ)` with `A` of Type II_1.
3. Check that the extension preserves: KO-dimension 6 (mod 8); the order-one condition on `D`; the first-order differential calculus; gauge-group extraction yielding SU(3) × SU(2) × U(1); anomaly cancellation per generation.

**Failure modes that kill the candidate:**

- KO-dimension is undefined or wrong in the Type II_1 regime.
- Order-one condition cannot be satisfied with a self-adjoint `D` of compact resolvent (or its Type II_1 analog).
- Gauge extraction does not yield the SM group.
- Anomaly cancellation does not survive the extension.

**Runner:** Operator-algebra / NCG specialist (Connes-school). An agent pass can produce the checklist artifact (which items must be checked, in what order, with what acceptance criterion); the actual extension construction is specialist work.

**Why this test is load-bearing:** The Type II_1 path is only interesting if it preserves what the finite Connes-Chamseddine control case already does. If the checklist fails at any item, the candidate is not "almost right" — it fails at the level the control case already passes, and the candidate is dead.

## Notes

- This is the lead Tier-1 candidate per `syntheses/08`.
- The candidate is deliberately single-axis-heterodox (only L1 differs from 00d defaults). This keeps the surface for specialist disagreement small.
- Sibling candidates that vary L4 (Sorkin) or L5 (RG / universality) explore the orthogonal axis-drops.
