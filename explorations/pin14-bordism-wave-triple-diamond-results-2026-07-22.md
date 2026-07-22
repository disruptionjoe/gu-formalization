---
title: "|Ω^Pin⁺₁₄| — two-method attack results (direct wave + triple-diamond), adjudication, and a §2 correction"
status: exploration
doc_type: results-adjudication
created: 2026-07-22
updates: explorations/sigma-w1-keystone-adversarial-assault-synthesis-2026-07-22.md
lane: "1 (OPERATOR-END-PENCIL)"
grade: exploration-tier; NO value asserted; no claim/canon/verdict/freeze movement
---

# |Ω^Pin⁺₁₄| — results of two independent method attacks

The single bottleneck the σ=w₁ keystone reduces to (leg A) was attacked two ways in parallel: a **direct
4-team wave** (literature / tool / hand-ABP / nonvanishing-probe) and the **triple-diamond challenge
process**. Adjudication weights **anchoring, not agreement** (a value counts only if literature-cited or
tool-reproduced; hand derivations are conjectural).

## Grounded answer (best defensible statement)

- **|Ω^Pin⁺₁₄| is a finite 2-group, order ≥ 2** — PROVED (2-local; Σ⁻¹MTPin⁺ = MSpin ∧ MTO₁).
- **Almost certainly nonzero and *moderate*** (a few Z/2's plus one η-type cyclic summand), not trivial and
  not astronomical — STRONGLY-DISFAVORED-zero (mod-4 pattern: d=14 ≡ 2 puts the large cyclic summands
  elsewhere). *Not proved.*
- **The leading ABP term VANISHES at n=14** (stem 13 = 0) ⇒ Ω^Pin⁺₁₄ is a **pure-correction group** —
  Grade A (Team C's from-scratch A(1)-resolution engine, validated by reproducing Ω^Pin⁺_n for n=0–7
  exactly, incl. the Z/16 at n=4).
- **Exact value: OPEN and genuinely unpublished.** Literature frontier is **k ≤ 12** (Giambalvo 1973;
  García-Etxebarria–Montero Table B.1 gives the d≤12 orders); n=14 is two degrees past every accessible
  table. **No exact value is asserted; none is fabricated.**
- **Team C's conjectural estimate (2⁶ = 64; honest range 8–2048) is NOT settled** and must not be cited —
  it hinges entirely on the ABP correction-summand identities (see the §2 correction below).

## §2 correction (to the assault synthesis)

The assault synthesis §2 named the ABP correction summands as **Σ⁸ko⟨2⟩, Σ¹⁰ko, Σ¹²ko⟨2⟩**. Team C flagged,
and it holds: **a free `Σ¹⁰ko` is inconsistent** — it would require a free Z in Ω^Spin₁₀, but Ω^Spin₁₀ is
**pure 2-torsion**. The correct per-degree summand types (ko vs ko⟨2⟩ vs the image-of-J / Brown–Gitler
piece — Team A's literature reads the degree-10 slot as `Σ¹⁰MJ`, not `Σ¹⁰ko`) must be taken from the
**published ABP** (Guo 2018 thesis tables the ko-blocks to ~deg 14; Guo–Putrov–Wang arXiv:1812.11959 §7.1,
noting the clean ko/A(1) identification only holds for s−t < 8). **This identity is the crux step** and the
entire source of the 8–2048 width. §2's "power of 2 / needs the three ABP steps" conclusion stands; only the
summand *labels* were imprecise.

## The cheaper route (found by the triple-diamond, missed by the assault)

The assault framed leg A as "commission a bespoke Bruner-`ext` run." The triple-diamond's approach-divergence
surfaced a better path: the **Smith fiber sequence** (Debray–Devalapurkar–Krulewski–Liu–Pacheco-Tallaj–
Thorngren, *The Smith Fiber Sequence and Invertible Field Theories*, arXiv:2405.04649, CMP 2025) — a
4-periodic LES reducing Ω^Pin⁺₁₄ to **already-known Ω^Spin_\*** (known well past deg 14). This **downgrades
the difficulty from "bespoke computation" to "apply a published LES."** Recommended primary route.

## The cheap probe is dead (don't reuse it)

The RP⁴×M¹⁰ nonvanishing probe (assault §2 "lowest-cost partial") **provably VANISHES** for every torsion
M¹⁰ — a false-negative (η²-divisibility of the Spin factor collides with the sporadic zeros at n=5,6,7), NOT
a "group is zero" verdict. Team D, Grade A. Do not read its 0 as anomaly-triviality; do not reuse it at n=14.

## σ's class (leg B) — separable, not a bordism computation

σ = w₁(L_time) is SW-blind (σ⁴=0), so its class lies in ker(→Ω^O₁₄) = the η-detected, Adams-filtration-≥1
interior of the dominant correction summand. Its order needs a **Pin⁺ η-invariant on GU's unbuilt (9,5)
Dirac operator** — gated on constructing the 14-geometry (T2/T3), independent of the group order.

## Lane-1 entry point (to actually close leg A)

Directed Lane-1 run (`OPERATOR-END-PENCIL`), not hourly-eligible (Lane 1 is `waiting_external`). Two routes,
in priority: (1) the **Smith LES** (arXiv:2405.04649) → known Spin data; (2) a completed **Adams-SS/`ext`**
run with the **correct published ABP module list** (Guo/GPW). Team C's validated resolution engine is a
reusable starting tool (it lives in session scratch — would need re-creating and committing into
`tests/` to become durable). Even a completed exact order only closes leg A; leg B (σ's η-class) stays
GU-gated. Grade: value OPEN, structural bound PROVED.
