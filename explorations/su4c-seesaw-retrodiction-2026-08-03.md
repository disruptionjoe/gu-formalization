---
artifact_type: exploration
status: exploration
doc_type: posit-retrodiction
created: 2026-08-03
lane: "2"
work_item: M-H3
register: lab/process/improvement-register-2026-08-03.md
panel_refs:
  - "lab/process/mathematician-panel-synthesis-2026-08-03.md (U5/U5b; §2 distinctive-physics list)"
  - "lab/process/eleven-lens-audit-2026-08-03.md (B2, B16)"
title: "M-H3 SU(4)_c seesaw retrodiction: m_D^nu = m_up at the PS scale + type-I seesaw + observed atmospheric scale retrodicts M_R in the band 1.1-6.0 x 10^14 GeV (naive m_t=173: 5.98e14; honest one-loop running: 1.07e14) — squarely inside the canonical GUT-seesaw window, ~5 decades below M_Planck. The Lambda^5/126-analogue channel that would host the Majorana block exists INSIDE the equivariant family (earned, computed); the VEV in that channel is NOT earned. b-tau unification rides the same machinery."
grade: "POSIT / RETRODICTION — standard GUT arithmetic on the verified group-theory chain; NO GU derivation of M_PS, the Λ⁵ VEV, or any Yukawa texture; no claim-status change"
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
construction: "physics-default throughout (SM MS-bar one-loop RGEs, type-I seesaw, measured masses); the only GU-side input is the verified compact group-theory chain — construction declared per GEOMETER-VS-PHYSICS-OBJECTS.md; no geometer-native object is invoked"
depends_on:
  - lab/active-research/pati-salam-chain-verification.md
  - canon/escape-corners-campaign-RESULTS.md
  - canon/shiab-existence-cl95.md
  - tests/chase/MOVE-4/move4_spinor_square_forms.py
  - explorations/yukawa-scoping-2026-07-13.md
  - lab/process/improvement-register-2026-08-03.md
scripts:
  - tests/seesaw/su4c_seesaw_arithmetic.py
outcome: "M_R retrodicted at 1.1e14-6.0e14 GeV (log10 = 14.0-14.8); surplus counted: +1 nominal / -1 hostile; decade-measure 3-of-30 target hit with <= 0.75 decades of declared freedom"
---

# M-H3 — the SU(4)_c seesaw retrodiction (one page)

**What this is.** The one-page posit the 2026-08-03 audit found missing
(physicist-panel item UNABSORBED-4; register row M-H3; panel synthesis U5/U5b).
It is a *retrodiction*: standard, decades-old GUT arithmetic executed on the
group-theory chain this repo has verified — not a GU derivation of anything.
The grade fence in the frontmatter is the claim, in full.

## 1. The posit

The verified chain (`lab/active-research/pati-salam-chain-verification.md`,
19/19 + independent Clifford cross-check) contains Pati-Salam
`SU(4)_c × SU(2)_L × SU(2)_R` with lepton number as the fourth color, and the
16 of Spin(10) containing exactly one generation *including* ν^c. In any
theory realizing that chain as physics, unbroken SU(4)_c forces the
third-generation Dirac neutrino Yukawa to equal the top Yukawa at the scale
where SU(4)_c holds:

```text
m_D^nu(M_PS) = m_t(M_PS)          [SU(4)_c: quark and lepton in one 4]
```

With the type-I seesaw and the observed atmospheric scale
(m_ν₃ ≈ √(2.507×10⁻³ eV²) = 0.0501 eV, normal ordering):

```text
m_nu3 ≈ (m_D^nu)² / M_R    ⇒    M_R = m_t² / m_nu3
```

## 2. The arithmetic, honestly (script: `tests/seesaw/su4c_seesaw_arithmetic.py`, exit 0)

| treatment | m_t input | r_κ (Weinberg-op running) | M_R (GeV) | log₁₀ |
|---|---|---|---|---|
| naive | pole, 173 GeV | 1 (off) | **5.98×10¹⁴** | 14.78 |
| run m_t only | m_t(10¹⁴) = 83.2 GeV (one-loop MS-bar, y_t(10¹⁴)=0.478) | 1 (off) | 1.38×10¹⁴ | 14.14 |
| run m_t and κ | 83.2 GeV | 1.30 | **1.07×10¹⁴** | 14.03 |

Running details: one-loop SM MS-bar RGEs from Buttazzo-et-al. inputs at
μ₀ = 173.34 GeV (g_Y=0.3583, g₂=0.6478, g₃=1.1666, y_t=0.9369, λ=0.1260);
positive control (RK4 vs closed-form g₃ running) passes at 5×10⁻¹⁵; the
evaluation scale μ* = 10¹⁴ is self-consistent with the answer (one fixed-point
iterate moves M_R by 0.001 decades). The κ factor is the flavor-universal
one-loop piece only (y_τ and flavor structure neglected) — it belongs to the
band, not the headline.

**The band, which is the claim:**

```text
M_R ≈ 1.1×10¹⁴ – 6.0×10¹⁴ GeV     (log₁₀ M_R = 14.0 – 14.8)
```

Order of magnitude 10¹⁴: inside the canonical GUT-seesaw / B−L window
[10¹³, 10¹⁶], 4.3–5.1 decades below M_Planck, and M_R/m_D ≈ 10¹² so the
seesaw hierarchy is self-consistent. A non-vacuity control shows the window
test can fail: the same formula applied to the first generation lands at
9.3×10⁴ GeV, nine decades outside.

**b–τ, same machinery.** SU(4)_c likewise forces y_b(M_PS) = y_τ(M_PS) — the
classic b–τ unification, which holds at the ~10–20% level in standard
SO(10)-class fits (threshold- and scenario-dependent; some non-SUSY one-loop
treatments land ~30% off unity). Not recomputed here; cited as the known
performance of the identical mechanism on the charged sector.

## 3. What the repo already owns: the channel, not the VEV

The audit's B2 finding (`lab/process/eleven-lens-audit-2026-08-03.md`),
correcting SHIAB-05's over-broad consequence sentence in
`canon/shiab-existence-cl95.md:84` ("must be supplied by an external
source-action spurion"):

- **Earned (computed, in-repo):** the same-chirality scalar channel is absent
  (dim Hom(S⁺⊗S⁺, Λ⁰) = 0, exact — `tests/chase/MOVE-4/move4_spinor_square_forms.py`),
  but same-chirality channels exist at **every odd k** (MOVE-4's per-k table);
  `canon/escape-corners-campaign-RESULTS.md` has the compact form
  16×16 = 10 + 120 + **126** (singlet-free); and the panel-verified arithmetic
  gives Λ⁵ ⊃ 126 ⊕ 126̄ as a Lorentz singlet (2002 = 252+840+720+180+10,
  252 = 126⊕126̄). So the **channel** in which a ν^c ν^c Majorana block — the
  M_R of §1 — could arise from an odd-form (Λ⁵/126-analogue) VEV lies *inside*
  the Spin-equivariant family. B2's correct statement, kept exactly: there is
  no invariant *scalar* channel; the odd-form VEV is internal to the family.
- **Not earned:** the existence, scale, or alignment of any VEV in that
  channel; M_PS itself; the seesaw as GU dynamics; any Yukawa texture. The
  full PS branching of Λ⁵(V₁₄) (locating the (10,1,3)-type component that
  actually couples to ν^c ν^c) is register item M-H2, still open; its surplus
  audit is M-M19. Prior in-repo state: `explorations/yukawa-scoping-2026-07-13.md`
  (channel inventory complete; all magnitudes source-action-gated).

Signature caveats, on the record: the PS verification file is (7,7)-rooted and
carries no staleness banner (audit B16 / register P-M25); this page uses only
the compact SO(10) ⊃ PS ⊃ SM chain, which is signature-blind. MOVE-4's channel
computation is Spin(9,5).

## 4. Constraint surplus, counted (AGENTS.md discipline)

```text
surplus = (independent constraints satisfied) − (free parameters)
```

**Constraints (2):**
C1 — M_R lands in the canonical GUT-seesaw window [10¹³, 10¹⁶]: 3 decades out
of an a-priori landing space of ~30 (10⁻¹¹ GeV — a ν-scale M_R, no seesaw — up
to 10¹⁹, past M_Planck). C2 — M_R lands below M_Planck with M_R ≫ m_D (the
mechanism is field-theoretic and genuinely seesaw). Independence ranking: C2
is only partially independent of C1 — under a hostile reading C1 subsumes it.

**Free parameters (2):**
F1 — which fermion the relation is applied to. Booked as *forced* on the
nominal reading (SU(4)_c is generation-diagonal; the heaviest ν pairs with the
heaviest up-type quark), but a hostile reading books it as a 3-way discrete
choice worth up to ~10 decades of movement (gen-1 gives 9×10⁴ GeV). F2 — the
running-scheme band (pole vs MS-bar, one-loop truncation, κ on/off): factor
5.6 = 0.75 decades, declared above, consumed into the band.

**Count:** nominal **+1** (C1+C2 − F2, F1 forced); hostile **−1** (C1 only
− F1 − F2). Decade-measure, per "rank it, do not eyeball it": a 3-of-30-decade
target hit with ≤ 0.75 decades of declared freedom (nominal) is informative in
exactly the hypercharge-precedent sense; with F1 booked free the surplus
degrades to weak consistency. Both readings stand as written. What would raise
the surplus to unambiguous: a GU-native M_PS (register M-M22) turning the
window constraint into an equality check, and the M-H2 branching turning the
channel citation into a located coupling.

## 5. Kill conditions (named now, before any future use)

- **K1:** any future GU-native RG determination of M_PS (M-M22) incompatible
  with M_R ≈ 10¹⁴±¹ GeV — in particular M_PS < 10¹³ GeV, since the Majorana
  VEV breaking PS cannot exceed the scale at which PS holds — kills the posit
  as stated.
- **K2:** the M-H2 branching of Λ⁵(V₁₄) → PS fails to contain a
  (10,1,3)-type component coupling to ν^c ν^c — the channel claim of §3 dies.
- **K3:** inverted mass ordering established: m_ν₃ ≈ 0.05 eV is no longer the
  third-generation eigenvalue and the arithmetic as written dies. (A
  quasi-degenerate spectrum near the Σm_ν bound only shifts M_R down by ≲3×
  and survives.)
- **K4:** a GU-native Yukawa computation returning m_D^ν ≠ m_up at M_PS by
  more than O(1) — e.g., large 126-Yukawa contamination of the third-generation
  Dirac mass, a known O(1) effect in SO(10) fits, from the very multiplet
  class supplying M_R.
- **K5:** the same-machinery b–τ relation failing far outside its known
  10–30% SO(10) performance under eventual GU-native thresholds — disfavors
  the SU(4)_c mass machinery wholesale.

## 6. Layer-0 fence

Nothing here counts generations. The relation is applied *within* the third
generation; "three generations" enters only as observed input; no multiplicity
or decomposition result is read as a count (the recurring failure named in
`AGENTS.md`). Every object used is the standard physics-side construction —
SM MS-bar running, type-I seesaw, measured masses — with the single GU-side
input being the verified compact group-theory chain of
`lab/active-research/pati-salam-chain-verification.md`, used only as group
theory.
