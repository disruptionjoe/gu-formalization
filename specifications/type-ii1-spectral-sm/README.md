---
title: "Type II_1 / Non-Embeddable Spectral Standard Model — Control Checklist + Extension Requirements"
status: canon
doc_type: overview
updated_at: "2026-05-31"
---

# Type II_1 / Non-Embeddable Spectral Standard Model — Control Checklist + Extension Requirements

This folder is the WRK-377 single-pass artifact for `pathway A` of `roadmap/15-persona-pathway-ranking.md` — the lead Tier-1 high-upside construction path in the gu-formalization repo. It is the **first falsification test** referenced by `wrk-375-gu-six-axis/examples/example-01-type-ii1-spectral-sm.md`.

## What this artifact does

It does **not** construct a Type II_1 / non-embeddable spectral Standard Model. It produces the requirements a Type II_1 candidate must meet, by:

1. Pinning down what the finite Connes-Chamseddine spectral Standard Model already proves in the published literature (the **control case**), one checklist item at a time, with literature anchors.
2. For each control-case item, naming what a Type II_1 extension must preserve, redefine, or coherently replace, and what is currently unknown.
3. Distinguishing **established control-case facts** from **speculative extension requirements** at every item.
4. Closing with a short list of contributor questions for operator-algebra / NCG specialists.

The goal is a clean obstruction checklist. A clean "this extension fails at item X" is a valuable result; so is "this extension is open at item X and here is the precise open question."

## Files

- `connes-finite-control-checklist.md` — what the finite Connes-Chamseddine spectral Standard Model proves and what a Type II_1 extension must preserve.
- `type-ii1-extension-requirements.md` — what additional structure the Type II_1 / non-embeddable regime needs to provide that the finite case does not require, and what is currently open in the published record.

## How to read

Read `connes-finite-control-checklist.md` first. It gives the eight control-case items (KO-dimension 6, real even structure, order-zero / order-one conditions, chirality operator, finite spectral triple data, inner fluctuations, gauge-group recovery, fermion representation content, anomaly compatibility) plus a brief "what must be preserved" note per item.

Then read `type-ii1-extension-requirements.md`. It walks the same items from the Type II_1 side and adds the structural questions specific to the non-embeddable regime (Murray-von Neumann trace, Breuer-Fredholm index, semifinite spectral triples, Jones-subfactor inclusions, MIP*=RE separation).

## What this is NOT

- It is **not** a construction. No Type II_1 spectral Standard Model is built here.
- It is **not** a no-go theorem. The published record shows the bridge has not been attempted in full; it does not show the bridge cannot be built.
- It is **not** a claim that any Type II_1 extension reproduces the Standard Model. It is a list of conditions any such candidate must meet.
- It is **not** specialist review. The artifact is structured so a Connes-school operator-algebra specialist can do the actual specialist work; the artifact is the agent-grade scoping document that names what they would be checking.

## Provenance and citations

The control-case checklist items are drawn from:

- Connes (2006), *Noncommutative Geometry and the Standard Model with neutrino mixing*.
- Chamseddine-Connes-Marcolli (2006), *Gravity and the Standard Model with neutrino mixing*.
- Chamseddine-Connes (2007), *Why the Standard Model*.
- Chamseddine-Connes (2007), *Conceptual Explanation for the Algebra in the Noncommutative Approach to the Standard Model*.
- Chamseddine-Connes-van Suijlekom (2013), *Beyond the Spectral Standard Model: Emergence of Pati-Salam Unification*.

The Type II_1 / non-embeddable extension requirements draw on:

- Connes-Moscovici (2006), *Type III and Spectral Triples* (twisted spectral triples).
- Benameur-Fack (2006), *Type II non-commutative geometry I* (Dixmier trace in von Neumann algebras).
- Carey-Phillips-Rennie-Sukochev (2006), *The Chern Character of Semifinite Spectral Triples*.
- Gabriel-Grensing (2013), *Ergodic Actions and Spectral Triples* (first-order condition beyond finite-dimensional case).
- Chattopadhyay-Pradhan-Skripka (2023), *Approximation of the Spectral Action Functional in the Case of τ-Compact Resolvents*.
- Junge-Navascués-Palazuelos-Pérez-García-Scholz-Werner (2010), *Connes' embedding problem and Tsirelson's problem*.
- Ji-Natarajan-Vidick-Wright-Yuen (2020), *MIP* = RE*.
- Goldbring (2021), *Non-embeddable II_1 factors resembling the hyperfinite II_1 factor*.
- Evans-Kawahigashi (2023), *Subfactors and Mathematical Physics*.

All of these are summarized in `literature/01-non-embeddable-type-ii-1-spectral-standard-model.md`, which is the immediate parent document of this checklist work.

## Relationship to related GU research artifacts

- **WRK-375 / six-axis specification protocol** (`wrk-375-gu-six-axis/`). WRK-375 produced `example-01-type-ii1-spectral-sm.md`, which names the Type II_1 spectral Standard Model as a single-axis-heterodox sextuple (L1 = Type II_1 spectral triple; L2-L6 inherit defaults). The first falsification test for that sextuple is exactly **this checklist**. WRK-377 supplies the artifact that the WRK-375 example points to.
- **WRK-376 / no-go forgetful-image map** (`wrk-376-gu-no-go-map/`). Complete as of 2026-05-30. Its analysis predicts that **Freed-Hopkins compatibility for the Type II_1 candidate comes from the Connes-channel pairing forgetting L1 substrate enrichment** — i.e., the standard spectral-action observer/pairing automatically lands the candidate inside the Freed-Hopkins anomaly classification image, where ordinary SM anomaly cancellation is the operating constraint. This recommendation is absorbed into **Item 9** of `connes-finite-control-checklist.md` as the explicit Freed-Hopkins compatibility sub-item. WRK-376 also identifies Distler-Garibaldi as the visible stress case (every successful evasion changes the category, not the shadow); this is consistent with the Type II_1 frame, which sidesteps Distler-Garibaldi by replacing the finite-dimensional internal algebra rather than living inside the same Lie-group embedding category.
- Other related artifacts (Nielsen-Ninomiya analogy, observer-pairing anomaly enrichment, stochastic parity-breaking, Cartan-twistor guardrail, Sorkin causal-set axis, RG-universality axis) are mostly orthogonal: they vary axes other than L1 in the six-axis frame, so they do not directly load on the Type II_1 control-case checklist.

## Public location

The public summary is `canon/type-ii1-spectral-sm-checklist.md`. The detailed checklist and extension requirements live in this folder so contributors can work against finite, reviewable controls.

## Status

Public draft artifact.
