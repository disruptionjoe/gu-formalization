---
title: "Omega^{Pin+}_14 = Z/2: the full ABP + Smith derivation (promoted from recitation-from-tables to derivation grade); coprimality of the 14-dim Pin wall (Z/2) with the 13-dim framed receptacle (Z/3); class realization explicitly open"
status: canon
doc_type: results
created: 2026-08-03
canon_promoted_at: 2026-08-03
tier: internal
gu_independent: true
register_item: M-M11 (lab/process/improvement-register-2026-08-03.md; audit topo-10/HB-06)
verdict: "Omega^{Pin+}_14 = Z/2 at DERIVATION grade (was: exact-but-recited multiplicity). GU CLASS REALIZATION stays OPEN — no verdict on any GU claim moves."
certificate: "tests/channel-swings/pin14_smith_degree_gate.py (degree-shift bookkeeping/type gate ONLY, per its own receipt; a derivation-grade literal-derivation gate is P-H10's open campaign item)"
source_explorations:
  - explorations/pin14-smith-route-audit-2026-07-22.md
  - explorations/pin14-anomaly-number-2026-07-21.md
  - lab/process/eleven-lens-audit-2026-08-03.md
depends_on:
  - canon/two-primary-lemma.md
---

# Ω^{Pin+}₁₄ ≅ Z/2: the derivation

**Canon means: safe to cite as the current public spine of the project. It does not mean proved
physics.** This is a GU-independent bordism computation (internal tier — reproduced within this
process, not externally replicated). It moves **no verdict**: the generation count stays OPEN, and
whether GU's proposed 14-dimensional datum maps to the nonzero class stays OPEN (see "The open gap"
below).

## What is being promoted, and from what

The exact value Ω^{Pin+}₁₄ ≅ Z/2 has been in-repo since 2026-07-22
(`explorations/pin14-smith-route-audit-2026-07-22.md`), but its multiplicity step was **recited**
from Kirby–Taylor's published table (A(14) = 1), and the exploration's own receipt is explicit
about its runnable: *"It is a bookkeeping/type gate, not a replacement for the cited theorems or
table"* — a status the eleven-lens audit sharpened (the gate's seven checks restate literals
assigned ten lines above; findings P-H10/HB-06). The repo's own anti-recitation discipline is
binding here: the 2026-07-21 banking session had already ruled that *"reciting a published
|Ω^{Pin+}₁₄| ... would be exactly the planted-toy over-claim"*
(`explorations/pin14-anomaly-number-2026-07-21.md:186`), and the portfolio's T1 line holds the same
gate: *"published tables list it nonzero but reciting that is a planted-toy over-claim — genuinely
reconstruct or report BLOCKED"* (`lab/process/RESEARCH-AGENDA.json`, PIN14 entry).

**This promotion satisfies that gate:** the chain below computes the group — including the
multiplicity — from general structural theorems (Smith cofiber sequence, the ABP splitting, the
ko-homology of RP^∞, one Postnikov/Steenrod step that reduces to a binomial coefficient), with the
Kirby–Taylor table demoted to an independent **cross-check**. No step recites Ω^{Pin+}₁₄ itself.

## The derivation (five steps)

**Step 1 — Smith reduction.** The Pin⁺ member of the four-periodic Smith family
(Spin×Z/2 → Pin⁻ → Spin×_{±1}Z/4 → Pin⁺; Debray–Devalapurkar–Krulewski–Liu–Pacheco-Tallaj–
Thorngren, arXiv:2405.04649) has cofiber sequence

    MTSpin → MTPin⁺ → Σ MTSpin ∧ (BZ/2)₊ .

Taking π₁₄ and using the ABP coefficient table values Ω^Spin₁₃ = Ω^Spin₁₄ = 0:

    0 = Ω^Spin₁₄ → Ω^{Pin+}₁₄ → Ω^Spin₁₃((BZ/2)₊) → Ω^Spin₁₃ = 0
    ⟹  Ω^{Pin+}₁₄ ≅ Ω̃^Spin₁₃(BZ/2)

(the disjoint basepoint splits off an Ω^Spin₁₃ = 0 summand). Degree bookkeeping: the suspension in
the third term is what turns π₁₄ into a degree-13 group.

**Step 2 — ABP splitting through degree 15, calibrated.** Anderson–Brown–Peterson (Ann. of Math.
86 (1967)): 2-locally

    MSpin ≃ ko ∨ Σ⁸ko ∨ Σ⁸ko⟨2⟩ ∨ (summands of connectivity ≥ 16, plus HZ/2 wedge
    summands whose first appearance is in degree 20)

where ko⟨2⟩ is the 1-connected cover (π₂ = Z/2 bottom). Working 2-locally suffices for Step 3's
target because Ω̃^Spin_*(BZ/2) is a finite 2-group in every degree: in the Atiyah–Hirzebruch
spectral sequence every E²-entry H̃_p(BZ/2; Ω^Spin_q) is killed by 2 (reduced homology of RP^∞;
odd-torsion coefficients contribute zero). **Calibration** of the truncation against the known
coefficients (the check that no summand relevant below degree 16 is missing):

| n | ko_n | (Σ⁸ko)_n = ko_{n−8} | (Σ⁸ko⟨2⟩)_n = ko⟨2⟩_{n−8} | sum | known Ω^Spin_n |
|---|---|---|---|---|---|
| 8 | Z | Z | 0 | Z² | Z² ✓ |
| 9 | Z/2 | Z/2 | 0 | (Z/2)² | (Z/2)² ✓ |
| 10 | Z/2 | Z/2 | Z/2 | (Z/2)³ | (Z/2)³ ✓ |
| 11 | 0 | 0 | 0 | 0 | 0 ✓ |
| 12 | Z | Z | Z | Z³ | Z³ ✓ |
| 13 | 0 | 0 | 0 | 0 | 0 ✓ |
| 14 | 0 | 0 | 0 | 0 | 0 ✓ |

The n = 13, 14 rows reproduce the two vanishing inputs of Step 1 from the summand homotopy —
self-consistency of the truncation, with ABP's table as the single source.

**Step 3 — evaluate on BZ/2.** Smashing the truncated splitting with BZ/2:

    Ω̃^Spin₁₃(BZ/2) ≅ k̃o₁₃(BZ/2) ⊕ k̃o₅(BZ/2) ⊕ k̃o⟨2⟩₅(BZ/2).

The connective real K-homology of RP^∞ (computed in full in Bruner–Greenlees, *The connective real
K-theory of finite groups*; the classical source is the bo-resolution literature) vanishes in
degrees ≡ 4, 5, 6 mod 8:

    k̃o₁₃(BZ/2) = 0   (13 ≡ 5 mod 8),      k̃o₅(BZ/2) = 0   (5 ≡ 5 mod 8).

(Corroboration of the same table one degree down: k̃o₃(BZ/2) = Z/8 is exactly the exponent behind
the lens-space eta denominators (2q² − 4q + 1)/8 on L(2;1) — see
`explorations/rho-invariant-two-primary-immunity-lemma-2026-08-03.md`.)

For the third summand, the cofiber sequence of the cover, ko⟨2⟩ → ko → τ_{≤1}ko, gives in
BZ/2-homology (using k̃o₅(BZ/2) = k̃o₆(BZ/2) = 0, degrees 5 and 6 both in the vanishing range):

    k̃o⟨2⟩₅(BZ/2) ≅ (τ̃_{≤1}ko)₆(BZ/2).

The truncation τ_{≤1}ko is the two-stage Postnikov system ΣHZ/2 → τ_{≤1}ko → HZ with k-invariant
Sq² (composed with mod-2 reduction). Its BZ/2-homology in degree 6 sits in the exact sequence

    H̃₇(BZ/2; Z) --(Sq²-induced)--> H̃₅(BZ/2; Z/2) → (τ̃_{≤1}ko)₆(BZ/2) → H̃₆(BZ/2; Z) = 0 ,

and the connecting map is dual to Sq²: H⁵(BZ/2; Z/2) → H⁷(BZ/2; Z/2), which on the generator is

    Sq²(x⁵) = C(5,2)·x⁷ = 10·x⁷ ≡ 0 (mod 2).

Hence the connecting map is zero and

    k̃o⟨2⟩₅(BZ/2) ≅ H̃₅(BZ/2; Z/2) = Z/2.

**Step 4 — assemble.**

    Ω^{Pin+}₁₄ ≅ Ω̃^Spin₁₃(BZ/2) ≅ 0 ⊕ 0 ⊕ Z/2 = **Z/2**,

with the generator detected in the ko⟨2⟩ / H̃₅-filtration piece.

**Step 5 — independent cross-check (the July route, now demoted to corroboration).** The reduced
Smith equivalence MTSpin ∧ BZ/2 ≃ Σ MTPin⁻ identifies Ω̃^Spin₁₃(BZ/2) ≅ Ω^{Pin−}₁₂; ABP's Pin
exponent theorem (CMH 44 (1969), Thm 5.1/Cor 2.1) gives exponent 2 in degree 12 ≡ 4 mod 8, and
Kirby–Taylor's direct Pin⁺ table (CMH 65 (1990), p. 446: A(14) = 1, higher-order summands only in
degrees ≡ 0 mod 4, and 14 ≢ 0 mod 4) gives the same multiplicity. Both legs return Z/2. **The
Kirby–Taylor A-number is used only here**, as a cross-check of a quantity Steps 2–3 already
computed.

## Coprimality: the Pin flavor cannot contaminate the count

The 14-dimensional Pin wall is valued in Z/2 (above). The 13-dimensional framed receptacle of the
count program is purely 3-primary: π₁₃ˢ has 3-torsion Z/3 as its relevant summand for the boundary
class, with Im J₁₃ = 0 (the dim-13 restatement, register M-H7/U3; and CRT as in
`canon/two-primary-lemma.md`). Since gcd(2, 3) = 1, Hom(Z/2, Z/3) = Hom(Z/3, Z/2) = 0: **no choice
of Pin flavor (Pin⁺ vs Pin⁻), and no 2-primary re-typing of the 14-dimensional wall, can leak into
the 3-primary count arithmetic in either direction.** The Pin-wall question (does GU's 14d content
carry the nontrivial Z/2 class — the anomaly/firewall-home question, register M-M12) and the count
question (the Z/3 boundary class) are CRT-disjoint channels. This is the same disjointness spine as
the two-primary lemma, applied one dimension up.

## The open gap (explicitly NOT closed): class realization

A nonzero ambient group is not a proof that any particular class is nonzero. Whether GU supplies a
Pin⁺ 14-manifold/operator family at all, and whether its proposed σ-datum maps to the nonzero
element of Z/2, are both **OPEN** — the operator/domain/line-bundle map is unbuilt (the July
exploration's own "Not settled" items stand verbatim, and
`tests/channel-swings/pin_smith_class_realization_gate.py` currently contains a==a-class asserts,
flagged P-H10). This promotion closes the *ambient group's derivation status* and nothing else.

## Honest input ledger (what is computed vs what is cited)

- **Computed here:** the long-exact-sequence bookkeeping (Step 1); the calibration table (Step 2);
  the two exact sequences and the binomial coefficient C(5,2) ≡ 0 mod 2 (Step 3); the assembly and
  the CRT/coprimality arithmetic.
- **Cited structural theorems (not answer-recitations):** the Smith cofiber sequence
  (arXiv:2405.04649); the ABP splitting and Spin coefficient table (Ann. Math. 86 (1967)); the
  ko-homology of RP^∞ vanishing pattern (Bruner–Greenlees); the ABP Pin exponent theorem
  (CMH 44 (1969)); Sq² on H*(RP^∞) (Wu formula/binomial — elementary).
- **Cited table value, cross-check only:** Kirby–Taylor A(14) = 1 (CMH 65 (1990) p. 446).

Per the repo's oq3b forensic standard, the external sources were live-checked at statement level
in the July audit and the 2026-08-03 audit cycle; page-level re-verification should accompany any
publication use.

## Promotion-Rule criteria (all six addressed)

1. **Clear scope statement.** The claim is the ambient bordism group Ω^{Pin+}₁₄ ≅ Z/2 at
   derivation grade, plus the Z/2 ⊥ Z/3 coprimality remark. No GU class, no count, no verdict.
2. **Proof or falsification target.** Proof: Steps 1–4 with Step 5 as an independent cross-check.
   Falsification targets: exhibit a summand of MSpin of connectivity < 16 missed by the Step-2
   calibration; a nonzero k̃o₁₃ or k̃o₅ of BZ/2; an error in the Sq²/k-invariant identification; or
   a Smith-sequence degree-bookkeeping error.
3. **Explicit assumptions.** The cited structural theorems in the input ledger; 2-locality
   justified by the AHSS 2-primarity of Ω̃^Spin_*(BZ/2); ko⟨2⟩ = 1-connected cover convention with
   the τ_{≤1}ko k-invariant = Sq².
4. **Known failure modes.** (i) Truncation-completeness of the ABP wedge below degree 16 —
   mitigated by the seven-row calibration reproducing Ω^Spin₈..₁₄; (ii) the k-invariant convention
   — mitigated because H̃₆(BZ/2;Z) = 0 makes the answer depend only on the Sq²-induced map, which
   is computed, and by the Step-5 cross-check; (iii) integral-vs-2-local mismatch — closed by the
   AHSS argument.
5. **No dependency on internal work artifacts.** The next actions (class realization; the
   M-M12/Freed–Teleman probe) are specified by named open items in this file and the register; no
   internal work-artifact system is required to act on it.
6. **No stale stronger status after the sweep.** No owner surface claims more than this file: the
   July exploration carries a same-day pointer note (promotion executed; its "recitation closes the
   multiplicity" step superseded); the gate's docstring status ("bookkeeping/type gate") is quoted
   here rather than upgraded; the portfolio's T1 "genuinely reconstruct or report BLOCKED" line is
   *weaker* than this result and is left to the P-H27 portfolio-reconciliation pass to refresh
   (stale-weaker, not stale-stronger). `CANON.md` gains the corresponding row this same day.

## Support (machine)

Internal tier; no Lean content. `tests/channel-swings/pin14_smith_degree_gate.py` (exit 0) checks
the three degree shifts of Step 1/Step 5 and pins the wording against "ordinary Spin alone"
regressions — per its own receipt it is a bookkeeping/type gate, NOT a certificate of this
derivation; upgrading it to a literal-derivation gate (deriving the calibration table and the
binomial step rather than restating constants) is part of the P-H10 campaign and is deliberately
not claimed here.

## Reversal

Revert this file and the `CANON.md` row added 2026-08-03; strike the promotion pointer note at the
end of `explorations/pin14-smith-route-audit-2026-07-22.md`; the July exploration then again holds
the result at exact-but-recited grade. No downstream migration required: no other canon file, paper
draft, or verdict consumes the *derivation grade* (as opposed to the value) of this group.
