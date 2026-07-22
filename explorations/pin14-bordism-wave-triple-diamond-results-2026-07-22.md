---
title: "|Ω^Pin⁺₁₄| — two-method attack results (direct wave + triple-diamond), adjudication, and a §2 correction"
status: exploration
doc_type: results-adjudication
created: 2026-07-22
updates: explorations/sigma-w1-keystone-adversarial-assault-synthesis-2026-07-22.md
lane: "1 (OPERATOR-END-PENCIL)"
grade: exploration-tier; exact ambient group primary-source proved; no GU class asserted; no claim/canon/verdict/freeze movement
---

# |Ω^Pin⁺₁₄| — results of two independent method attacks

> **ADJUDICATION UPDATE (2026-07-22 — primary Smith + ABP + Kirby--Taylor audit).** The cheap route is now
> executed at the exact-sequence level and cross-checked against the direct table.  It gives
> `Omega^{Pin+}_14 ~= Omega^{Pin-}_12 ~= Z/2` exactly.  The earlier wording “reduces to already-known
> ordinary Spin” was incomplete: the reduced `BZ/2` summand is precisely a shifted **Pin-minus** group.  The
> session-scratch “leading ABP term vanishes” statement is not a durable computation of that rank and is
> withdrawn.  See `explorations/pin14-smith-route-audit-2026-07-22.md` and
> `tests/channel-swings/pin14_smith_degree_gate.py`.  This notice governs conflicting text below.

The single bottleneck the σ=w₁ keystone reduces to (leg A) was attacked two ways in parallel: a **direct
4-team wave** (literature / tool / hand-ABP / nonvanishing-probe) and the **triple-diamond challenge
process**. Adjudication weights **anchoring, not agreement** (a value counts only if literature-cited or
tool-reproduced; hand derivations are conjectural).

## Grounded answer (best defensible statement)

- **Exact structure reduction:** `Omega^{Pin+}_14 ~= Omega^{Pin-}_12` — proved from the published Smith
  cofiber sequence, the degree-13/14 Spin zeros, the basepoint splitting, and the reduced Smith equivalence.
- **Nonzero and exponent two:** ABP's Pin exponent theorem in degree 12 gives
  an elementary 2-group.  Larger cyclic 2-power summands are ruled out.
- **Exact value:** Kirby--Taylor define `A(n)` as the number of `Z/2` summands, list `A(14)=1`, and restrict
  other summands to dimensions `0 mod 4`; hence `Omega^{Pin+}_14 ~= Z/2`.
- **Withdrawn:** the session-scratch “leading ABP term vanishes/pure-correction” claim and the conjectural
  `2^6` estimate are not durable evidence and must not be cited.

## §2 correction (to the assault synthesis)

The assault synthesis §2 named the ABP correction summands as **Σ⁸ko⟨2⟩, Σ¹⁰ko, Σ¹²ko⟨2⟩**. Team C flagged,
and it holds: **a free `Σ¹⁰ko` is inconsistent** — it would require a free Z in Ω^Spin₁₀, but Ω^Spin₁₀ is
**pure 2-torsion**. The correct per-degree summand types (ko vs ko⟨2⟩ vs the image-of-J / Brown–Gitler
piece — Team A's literature reads the degree-10 slot as `Σ¹⁰MJ`, not `Σ¹⁰ko`) must be taken from the
**published ABP** (Guo 2018 thesis tables the ko-blocks to ~deg 14; Guo–Putrov–Wang arXiv:1812.11959 §7.1,
noting the clean ko/A(1) identification only holds for s−t < 8). This remains a correction to the historical
engine design, but Kirby--Taylor's direct table supersedes the claim that those three steps are still needed
to obtain the ambient degree-14 group.

## The cheaper route (found by the triple-diamond, now executed)

The assault framed leg A as “commission a bespoke Bruner-`ext` run.”  The triple-diamond's
approach-divergence surfaced the better Smith route, and the present audit completes its degree bookkeeping.
The four-periodic sequence lowers the target to `Omega^{Pin-}_12`; it does not eliminate the reduced
`BZ/2`/Pin-minus term.  Kirby--Taylor's published degree-14 table supplies the missing multiplicity directly,
so no new Adams engine is needed for the ambient group.

## The cheap probe is dead (don't reuse it)

The RP⁴×M¹⁰ nonvanishing probe (assault §2 "lowest-cost partial") **provably VANISHES** for every torsion
M¹⁰ — a false-negative (η²-divisibility of the Spin factor collides with the sporadic zeros at n=5,6,7), NOT
a "group is zero" verdict. Team D, Grade A. Do not read its 0 as anomaly-triviality; do not reuse it at n=14.

## σ's class (leg B) — separable, not a bordism computation

σ = w₁(L_time) is SW-blind (σ⁴=0), so its class lies in ker(→Ω^O₁₄) = the η-detected, Adams-filtration-≥1
interior of the dominant correction summand. Its order needs a **Pin⁺ η-invariant on GU's unbuilt (9,5)
Dirac operator** — gated on constructing the 14-geometry (T2/T3), independent of the group order.

## Lane-1 entry point after closing leg A

Directed Lane-1 run (`OPERATOR-END-PENCIL`), not hourly-eligible (Lane 1 is `WAITING_EXTERNAL`).  For the
pure-topology leg, the ambient group is closed at `Z/2`.  The operator audit shows that GU has not yet constructed the
domain/determinant/Pfaffian line whose class could be paired with it.  Grade: exact ambient group PROVED;
GU class OPEN.
