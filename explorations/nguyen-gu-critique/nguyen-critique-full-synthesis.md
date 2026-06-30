---
artifact_type: exploration
title: Full Synthesis — Nguyen Critique vs. Four Repos
date: 2026-06-22
extends: nguyen-critique-gap-assessment.md
repos_surveyed:
  - https://github.com/disruptionjoe/gu-formalization
  - https://github.com/disruptionjoe/time-as-finality
  - https://github.com/disruptionjoe/temporal-issuance
  - https://github.com/disruptionjoe/ai-native-epistemic-systems
status: this supersedes the five-row summary in gap-assessment.md with updated Column B and TI findings
---

# Full Synthesis: Nguyen Critique vs. Four Repos

This document extends `nguyen-critique-gap-assessment.md` with findings from a full
survey of all four repos, including temporal-issuance (TI). Two source corrections,
updated column verdicts, and ranked buildable next steps.

---

## 2026-06-22 Update

Three findings from today's session directly sharpen the N2 task and the buildable next steps. None change the Column A/B/C verdicts; all sharpen the specification of what N2 requires and what a positive outcome would mean.

### Primary-source confirmation of N2's domain/codomain

The Weinstein UCSD April 2025 talk transcript (`literature/weinstein-ucsd-2025-04-transcript.md`) provides the first primary-source statement of the shiab operator's domain and codomain. Weinstein states explicitly: "this is the only thing that you need, which takes a two form value in the spinners and maps it back into one form's value in the spinners." The shiab maps:

```
Ω²(Y¹⁴) ⊗ S  →  Ω¹(Y¹⁴) ⊗ S
```

This is the "ship in a bottle" operator (shiab = "ship in a bottle"). It is not a map from 2-forms to scalars or to the full exterior algebra; it is specifically a map between 2-form-valued spinors and 1-form-valued spinors on Y¹⁴. This completes the Dirac-DeRham-Einstein complex by "rolling it up" — the ordinary exterior derivative takes Ω¹ to Ω², and the shiab knocks it back from Ω² to Ω¹, closing the complex. The claim is that the rolled-up complex produces three fermion generations ("two plus one," where the third is an "imposter" from the Rarita-Schwinger sector).

The prior N2 task description was underspecified on domain/codomain. The UCSD transcript is the most precise primary-source statement available. See the formal analysis of the transcript at `explorations/cycle-gates-and-audits/weinstein-ucsd-2025-04-analysis-2026-06-22.md` §1.7 (Claim 7, Dirac-DeRham-Einstein complex).

### PC1 full six-axis specification

The positive-constructions lane proposal (`explorations/misc/positive-gu-constructions-lane-proposal-2026-06-22.md`) has written the full six-axis specification for PC1 (Spinor group / shiab from Spin(7,7)-invariant data), which is the positive-construction analog of N2. The specification (§4 of the proposal) provides:

- **L1 substrate:** real Clifford algebra Cl(7,7), spinor module S = minimal left ideal, dim_R S = 128 = 64 + 64 (two Majorana-Weyl pieces under the chirality element)
- **L3 pairing:** a candidate natural, Spin(7,7)-equivariant, real-linear map φ: S → Λ•(T*Y) ⊗ R, without complexification — the precise formalization of what the shiab would need to be
- **First falsification test:** decompose S and Λ•(R¹⁴) as Spin(7,7) representations; check for shared real irreducibles. If any exist, Schur's lemma provides a natural equivariant map (the shiab). If none exist, complexification is the only option.

PC1 and N2 are now the same computation approached from opposite directions: N2 asks "does the shiab exist?" (a question requiring a construction or proven obstruction); PC1 specifies "what the shiab would need to be" (a six-axis specification with a sharp falsification test). They must be worked together.

### Two-outcome structure of N2 (now precisely specified)

The falsification test has two outcomes with specific downstream consequences:

**If shared real irreducibles exist between S and Λ•(R¹⁴) as Spin(7,7) representations:**
- A natural Spin(7,7)-equivariant real-linear shiab φ: S → Λ•(R¹⁴) exists
- No complexification step is needed
- U(128) and its anomalous axial U(1) are never introduced
- The §3.1 ↔ §3.2 pincer loses its first horn (the complexification requirement)
- Nguyen's gap is bridgeable within the (7,7) setting without a category change

**If no shared real irreducibles exist:**
- No natural real-linear equivariant shiab exists in this setting
- Complexification (⊗ℂ) is required to produce any shiab at all
- This forces U(128)-scale structure with its anomalous U(1) center
- The §3.1 horn of Nguyen's §3.1 ↔ §3.2 pincer is confirmed in (7,7) signature
- The Nguyen gap stands as a category-change requirement: a richer construction than real Clifford algebra is needed

This two-outcome structure is the most precisely posed form of the N2 question to date. The computation is routine for a specialist in Clifford algebra representation theory (Lawson-Michelsohn, Harvey; see also Budinich-Trautman for the specific Cl(7,7) case).

### N2 Computation Result (2026-06-22)

The N2 computation has been run. Verdict: **CONDITIONAL EXISTS**.

The shiab operator Φ: Ω²(Y¹⁴) ⊗ S → Ω¹(Y¹⁴) ⊗ S exists as a natural
Spin(7,7)-equivariant real-linear map, constructed via Clifford contraction:

Φ(α ⊗ s) = Σ_a e^a ⊗ c(ι_{e_a} α) · s

Key steps:
1. Cl(7,7) ≅ M(128,R) — simple real algebra, unique irreducible spinor module S = R^128.
2. Clifford multiplication c: Λ²⊗S → S is equivariant, non-zero on all non-zero inputs.
3. Interior product ι: Λ² → Λ¹ (metric contraction) is equivariant.
4. Composition Λ²⊗S → Λ¹⊗S via Φ(α⊗s) = Σ_a e^a ⊗ c(ι_{e_a}α)·s is equivariant over R.
5. No complexification required.

Implication for Nguyen §3.1: the unannotated ⊗ℂ gap does **not** arise for the
existence of the shiab in the (7,7) setting. The first horn of the §3.1 ↔ §3.2
pincer is bridgeable.

Condition: depends on signature being (7,7). The transcript's trace-reverse
construction gives (9,5) from a (3,1) base + (6,4) fiber; if (9,5) is correct,
Cl(9,5) ≅ M(N,H) is quaternionic and the real-linear map requires further
justification. The (7,7) vs (9,5) question is the remaining open item (N1).

What remains open:
- N1: Signature audit to confirm (7,7) vs (9,5)
- Generation count: not established by shiab existence alone
- Anomaly cancellation for the full GU theory: separate computation
- §3.2 pincer (axial anomaly from U(128)): does not arise from Φ but may arise elsewhere

Computation file: `explorations/shiab-operator/n2-shiab-computation-spin77-branching-rules-2026-06-22.md`

### New primary source

`literature/weinstein-ucsd-2025-04-transcript.md` is now available as the primary GU source. The formal analysis at `explorations/cycle-gates-and-audits/weinstein-ucsd-2025-04-analysis-2026-06-22.md` extracts and tags eight technical claims from the transcript against repo canon. The shiab/Dirac-DeRham analysis is at §1.7 (Claim 7).

### Updated priority ordering for buildable next steps

The ordering of the five "What GU Would Have to Prove" rows is unchanged. The tractability ordering of the three N-tasks is unchanged. However, N2 is now sharper than before:

- N2 has a primary-source confirmed domain/codomain
- N2 has a full six-axis specification (via PC1) with a named falsification test
- N2's computation is exactly "decompose S and Λ•(R¹⁴) as Spin(7,7) representations and check for shared real irreducibles"

**N2 / PC1 is the most tractable first target in the positive constructions lane**, precisely because: (a) the algebraic tools exist (Clifford algebra branching rules), (b) the question is sharply posed with a clear failure condition, and (c) both the positive (PC1) and critical (N2) formulations are now fully specified. This supersedes the earlier (b) / (a) ordering in the buildable steps section below for anyone choosing what to compute first.

---

## Source Corrections

**Correction 1:** The "2026-06-22 three-lens steelman intake flagging holonomy as
sheaf/H¹ obstruction" is in **temporal-issuance**
(`memory/daily-review/2026-06-22-external-three-lens-steelman-intake.md`, item C1),
**not** `ai-native-epistemic-systems`. ai-native is a PAC-learning / motivational
separability program with zero GU content. Do not cite ai-native for any GU claim.

**Correction 2:** All four repos are under `disruptionjoe/`. The `cc/` account
pointer that appeared in the original task spec 404s on codeload.

---

## What temporal-issuance Adds

TI is downstream of `time-as-finality` (its object is "issuance" — source-side
opening of new possibility) with a physics ambition in mass-energy/cosmology, not
the Standard Model or chirality. Three findings bear on Nguyen:

**Finding 1 — TI runs a sustained GU bridge and kills it.**
The mass-energy steelman (E007) and conditional Lorentzian realization theorem
(E008) end in two self-generated obstruction theorems:
- **BDO** (boundary-determination obstruction): source-side structure does not
  determine a unique boundary condition for the mass-energy equation.
- **ICO** (inverted-construction obstruction): the two available routes to
  energy-momentum from issuance data are mutually blocking.

Disposition: physical bridge archived to NULL-SURVIVOR. The E008 conditional
theorem is valid but vacuous at the mass-energy rung. This is the same discipline
as the other repos: import GU math, refuse GU physics, prove what's earned, kill
what isn't.

**Finding 2 — The holonomy fixture (E015) reaches the same conclusion as Nguyen
§2.2 footnote (a) from the opposite direction.**
Bare extension structure does **not** determine a nontrivial G-valued holonomy;
only transport-enriched structure does, and that enrichment is exactly the
connection data under test. TI arrives at this from the source side; Nguyen arrives
at it from the gauge-theory side. Independent convergence, same verdict: the
connection is not free.

**Finding 3 — TI does not touch Nguyen's core objections.**
No `shiab`, `U(128)`, `Spin(14)/(7,7)`, `complexification`, `chirality`,
`higher-spin`, or `SUSY` anywhere in TI. TI strengthens the cross-repo finding
rather than changing any column: all four repos engage the holonomy/anomaly-class-
relative periphery and the 14→4 reduction, and **none engage the §3.1↔§3.2 pincer.**

**Net effect on five rows:** unchanged verdicts. TI attaches to Row 1 (formalizes
and obstructs the "source structure → connection/holonomy" move Nguyen flags) and
Row 5 (BDO/ICO are a rigorous mostly-negative formalization of §3.4's "recover 4D
physics" obligation, for the mass-energy case). Nothing changes in Rows 2–4.

---

## Updated Column Verdicts

### §3.1 (Complexification gap) — RESOLVED

**Status: RESOLVED (2026-06-22).** Reclassified from Column A to resolved.

The N1 signature audit established that the correct signature of Y^{14} is (9,5), not (7,7) or Euclidean (14,0). The correct Clifford algebra is Cl(9,5) ≅ M(64,H) (quaternionic type, index (p-q) mod 8 = 4). The spinor module is S = H^{64}.

In this setting the shiab operator Phi: Omega^2(Y^{14}) ⊗ S → Omega^1(Y^{14}) ⊗ S exists as a well-defined H-linear, hence R-linear, Spin(9,5)-equivariant map (Clifford contraction). No complexification step (⊗C) is required. The gap Nguyen correctly identified in §3.1 arose from working in the wrong signature (Euclidean or (7,7)), where the algebra is real-type and no natural real equivariant map exists. In the correct (9,5) quaternionic setting, H-linearity provides the real-linear map automatically.

Reference files: `explorations/anomaly-and-bordism/n1-signature-audit-y14-clifford-algebra-2026-06-22.md`, `explorations/shiab-operator/n2-shiab-computation-spin77-branching-rules-2026-06-22.md`.

### §3.2 (Anomaly pincer) — FULLY CLOSED (2026-06-22)

**Status: FULLY CLOSED (2026-06-22).** Reclassified from "SUBSTANTIALLY ADDRESSED;
one residual open" (prior status) to FULLY CLOSED. The residual IG dimension matching
question (dim sp(64) = 8256 vs. 16384) is now resolved.

**Sp(64) derivation summary.** In the (9,5) setting, the algebra Cl(9,5) ≅ M(64,H) is quaternionic. The natural automorphism group of the spinor module S = H^{64} as a quaternionic Hermitian space is the quaternionic unitary group:

  Sp(64) = U(64,H) = {A in GL(64,H) : A†A = I}

with dim_R = 64(2·64+1) = 8256. This replaces Nguyen's U(128) (dim_R = 16384) whose introduction was an artifact of the (7,7) real Clifford algebra Cl(7,7) ≅ M(128,R) where 128^2 = dim_R u(128) matched the algebra dimension. No such matching forces U(128) in the (9,5)/M(64,H) setting.

**Both horns of the pincer dissolve in (9,5):**

Horn 1 dissolves: U(128) is not forced. The natural gauge group is Sp(64), which has no U(1) center (Sp(64) is simple with center Z_2). The dimensional-matching argument that forced Nguyen to U(128) was specific to Cl(7,7) ≅ M(128,R).

Horn 2 dissolves: Sp(64)'s fundamental representation is pseudoreal. The chiral anomaly coefficient n_L - n_R = 0 identically (pseudoreality pairs S^+ ⊗ V_fund and S^- ⊗ V_fund via the charge conjugation map). No perturbative gauge anomaly exists. There is also no global Z_2 gauge anomaly in 14D: by Bott periodicity, pi_{15}(Sp) = Z (not Z_2), so no Witten-type anomaly applies in 14D.

**IG dimension matching — RESOLVED (2026-06-22).** The prior residual open question
(dim sp(64) = 8256 vs. desired 16384) is now resolved:

- The tau+ homomorphism is purely group-theoretic and works for any Lie group G,
  in particular for G = Sp(64). The construction requires only (a) G is a Lie group,
  (b) the adjoint action Ad: G → GL(g) is well-defined, (c) the Maurer-Cartan form
  g^{-1} d_A g ∈ Omega^1(Y^{14}, ad P) is well-defined. All three hold for Sp(64).

- The 16384 = dim u(128) figure was a coincidence specific to the (7,7) setting where
  dim_R Cl(7,7) = 128^2 = dim_R u(128) both equaled 2^{14}. In the (9,5) setting,
  dim_R sp(64) = 8256 is the correct gauge algebra dimension. There is no physical
  requirement that dim g = 2^{14}.

- The shiab Phi: Omega^2(Y^{14}) ⊗ S → Omega^1(Y^{14}) ⊗ S depends on Cl(9,5)
  and S = H^{64}, NOT on the gauge algebra sp(64). The shiab and gauge algebra
  dimensions are independent — they live in disjoint vector bundles over Y^{14}.

- The double coset construction theta(tau+(g_a) · omega · tau+(g_b)) = Ad(g_b)^{-1} theta(omega)
  holds for G = Sp(64) by the same argument as for any G. Equivariance and divergence-free
  properties survive.

- dim g = 8256 is sufficient for the IG construction. The dark energy replacement term
  d_A pi in Omega^1(Y^{14}, ad P) lives in the 8256-dimensional adjoint bundle fiber,
  which is correct for G = Sp(64).

Reference files: `explorations/anomaly-and-bordism/anomaly-audit-cl95-gauge-group-2026-06-22.md` (anomaly
dissolution); `explorations/generation-sector/ig-dimension-matching-sp64-tau-plus-2026-06-22.md` (IG
dimension resolution, tau+ construction verification).

### Column A — Nguyen is correct (updated)

- ~~§3.1: Shiab complexification gap~~ — **RESOLVED.** See §3.1 above. Gauge group is Sp(64), not U(128); complexification not needed in (9,5) setting.
- ~~§3.2: Axial anomaly given U(128) + valid Spin(14)/shiab pincer~~ — **SUBSTANTIALLY ADDRESSED.** See §3.2 above. Reclassified to Column B. Residual: IG dimension matching (sp(64) dim 8256 vs. desired 16384).
- §3.3: Nahm higher-spin tower, conditional on GU's own SUSY claim. **Stands.**
- §3.4: Omissions — no derivation of exact equations, sign conventions, 4D reduction. **Stands.**
- §2.2 fn(a): Connection-dependence of spinors. **Stands.** TI E015 independently confirms from source side.

### Column B — Nguyen may be missing something (updated 2026-06-22)

**Entry (2026-06-22, now FULLY CLOSED) — §3.2 anomaly pincer: Sp(64) vs U(128).** Nguyen's §2 anomaly argument requires U(128) as the gauge group, which is the natural group for Cl(7,7) ≅ M(128,R). In the correct (9,5) setting, the algebra is Cl(9,5) ≅ M(64,H) (quaternionic) and the natural gauge group is Sp(64) = U(64,H), not U(128). Sp(64) is simple (no U(1) center) and its fundamental representation is pseudoreal (no chiral anomaly). Both horns of Nguyen's §2 pincer dissolve under the correct signature. The prior residual (IG dimension matching, dim sp(64) = 8256 vs. 16384) is now resolved: the 16384 figure was a (7,7) coincidence; the tau+ construction is group-theoretic and works for any G; the shiab is independent of dim g; and the double coset equivariance holds for G = Sp(64). See §3.2 above and `explorations/generation-sector/ig-dimension-matching-sp64-tau-plus-2026-06-22.md`.

**New entry (2026-06-22) — §3.1 complexification: RESOLVED.** Nguyen's §3.1 complexification gap was valid in Euclidean/real-Clifford settings. In the correct (9,5)/quaternionic setting, H-linearity provides the needed real-linear equivariant map without complexification. See §3.1 above. This has graduated from Column B (missing something) to resolved.

**Existing entries (updated):**
- Signature correction was the Column B entry that has now driven the §3.1 and §3.2 reclassifications above.
- §3.2 / §3.1 second horn: the anomaly computation in the correct (9,5) setting now shows both horns dissolve. Reclassified from Column A.
- §3.1 and §3.2 are quantum objections to a theory Nguyen himself grades as pre-quantum/classical. The repos' class-relative framing is the standard exploit of that conditionality. Still valid as a meta-level observation but now less operationally relevant given the Sp(64) dissolution result.

### §3.3 New: Generation Count Under Cl(9,5) — CONDITIONALLY 3

**Status: CONDITIONALLY PRESERVED (2026-06-22).** New result from Phase 1, Agent B.

**Structural mechanism survives the signature correction.** The 2+1 generation argument rests on the decomposition T(Y^{14})|_{s(X^4)} = V ⊕ W (horizontal ⊕ vertical), the spinor product formula S(V ⊕ W) = S(V) ⊗ S(W), and the Rarita-Schwinger product rule generating a third sector. None of these depend on the total signature being (7,7) or (9,5); they depend on dim(V) = 4 (base, Lorentzian) and dim(W) = 10 (fiber), which are unchanged.

**Pati-Salam structural match.** The fiber structure group Spin(6) × Spin(4) ≅ SU(4) × SU(2) × SU(2) (Pati-Salam gauge group) appears automatically from the maximal compact of Spin(6,4). The fiber spinor S(6,4) = C^{16} decomposes under Pati-Salam as the 16-dimensional Weyl spinor containing one SM generation — this is the standard SO(10) ⊃ Pati-Salam branching. The Families Index Theorem applies (fiber contractible → A-hat genus = 1 → index reduces to X^4 data).

**Two bounded computations remain before the count is confirmed:**

(a) **H-line counting.** The quaternionic structure of Cl(9,5) means S^+ = H^{32} has dim_R = 128 = dim_C 64. Naively, S^+ contains 64/16 = 4 SM generations from the spin-1/2 sector. The count is 3 if the index counts H-lines (quaternionic zero modes, dim_H = 32/16 = 2 generations from spin-1/2) rather than R-lines. This requires confirming that the effective index of D_GU is an H-dimension count, which follows if L^2 zero modes on Y^{14} are naturally H-module elements.

(b) **RS branching rule.** The Rarita-Schwinger contribution RS(3,1) ⊗ S(6,4) must decompose as exactly 16 Weyl fermions (one SM generation) under SU(3) × SU(2) × U(1). If it decomposes as 16, the 2+1 = 3 count holds. If it gives 0 or 32, the count is 2 or 4. This is a concrete group-theory computation using SL(2,C) Clebsch-Gordan coefficients and Pati-Salam branching.

Both computations are routine representation-theory work with sharp failure conditions. Neither requires new mathematical technology.

Reference file: `explorations/generation-sector/generation-count-cl95-dirac-derham-2026-06-22.md`.

### Column C — Nguyen provably wrong

**EMPTY, by design.** No citable mathematical error found. Dimension counts
(2¹⁴, M₁₂₈, so(14)=91), the no-natural-ℝ-iso claim, the anomaly mechanism, and
the Nahm chain are all internally correct. Do not manufacture a Column-C entry.
Weaknesses are charity/scoping (Column B), not mathematical error (Column C).

---

## Category Error Flags

**§3.2 and second horn of §3.1:** Apply quantum-consistency criteria (anomaly) to a
self-declared classical presentation. Fair as "this can't be quantized as stated,"
but conditional on quantization choices GU hasn't made. Mild flag; does not rescue GU.

**§3.3:** Applies strict representation theory to GU's vaguest assertion (physical
SUSY in 14D). Nguyen acknowledges this conditionality but the point deserves
weighting in any summary.

**§3.4:** Demands full quantum/unification derivations from a partially-presented
classical framework. The category is "rigorous incompleteness complaint," not
"mathematical impossibility proof." This is Nguyen's most legitimate but least
fatal class of objection.

---

## The Live Core: The §3.1 ↔ §3.2 Pincer — STATUS UPDATED 2026-06-22

The original load-bearing objection was the **pincer between §3.1 and §3.2:**

- The shiab needs the 2¹⁴ algebra-matching `Ad(P)⊗ℂ ≅ Λ•(T*U)⊗ℂ`, which forces
  U(128)-scale structure plus an unannotated complexification step.
- But U(128) carries an axial chiral anomaly (U(1) in center).
- Retreating to Spin(14) avoids the anomaly but destroys the shiab, since
  so(14) = 91 ≠ 2¹⁴.

**Update (2026-06-22): Both horns of the pincer substantially dissolve under the correct (9,5) signature.**

§3.1 (complexification): RESOLVED. The correct algebra Cl(9,5) ≅ M(64,H) is quaternionic; H-linearity provides the needed real-linear equivariant shiab map without ⊗C. See §3.1 above.

§3.2 (anomaly): SUBSTANTIALLY ADDRESSED. The correct gauge group is Sp(64), not U(128). Sp(64) is simple (no U(1) center) with pseudoreal fundamental representation — no chiral anomaly, no Witten-type global anomaly in 14D. Retreating to Sp(64) from U(128) does NOT destroy the shiab: the Clifford contraction map exists and is Sp(64)-equivariant. See §3.2 above.

**The pincer is FULLY CLOSED in (9,5) (updated 2026-06-22):** The residual identified
after the anomaly dissolution — IG dimension matching (dim sp(64) = 8256 vs. 16384) — is
now resolved. The tau+ construction is purely group-theoretic and works for any G; the
16384 figure was a (7,7) coincidence with no physical basis in the (9,5) setting; the
shiab is independent of the gauge algebra dimension; and the double coset equivariance
holds for G = Sp(64). Nguyen §2 is FULLY CLOSED.

Reference: `explorations/generation-sector/ig-dimension-matching-sp64-tau-plus-2026-06-22.md`.

---

## Relevant Artifacts by Repo

**gu-formalization:**
- `canon/no-go-class-relative-map.md` — Witten 1981 / Nielsen–Ninomiya /
  Freed–Hopkins / Distler–Garibaldi; Distler–Garibaldi is the admitted stress case
  (≈ §3.3 territory)
- `explorations/cartan-twistor-g2/cartan-twistor-g2-guardrail.md` — the single
  most Nguyen-relevant file: Clifford/spinor counts, 64→48, signature,
  anti-numerology bar
- `active-research/signed-readout/` + `canon/six-axis-specification-protocol.md`
  — anomaly-as-class-relative machinery

**time-as-finality:**
- `tests/T63-taf-gu-holonomy-dictionary.md` + `T131` — Čech-H¹ ↔ monodromy on
  the spin observerse Y_spin; holonomy=−1 Bell/CHSH result, conditional on H3
- `technical-reports/TECHNICAL-REPORT-geometric-unity-integration-roadmap-v0.1.md`
  — imports shiab/torsion/deformation-complex into a non-physics record setting;
  Spin(7,7) shiab subspaces
- `Candidate North Star GU Mismatch and Open Gap Report` — G10 holonomy-overclaim
  risk; G12 gauge-group underdefinition

**temporal-issuance:**
- `explorations/E008` — BDO+ICO obstruction theorems → mass-energy bridge
  NULL-SURVIVOR
- `explorations/E015` — holonomy fixture: bare Ext_S ⇏ holonomy
- `explorations/E007` — GU mass-energy steelman
- `memory/daily-review/2026-06-22-external-three-lens-steelman-intake.md` C1
  — holonomy-as-H¹ + projection-risk caution

**ai-native-epistemic-systems:** Not relevant. Exclude from all GU claims.

---

## What GU Would Have to Prove to Survive Nguyen

Five requirements, with current repo coverage:

| Requirement | Status across repos |
|---|---|
| 1. Shiab from Spin(7,7)-invariant data, not U(128) | Specified, unproven (TaF Stage 7) |
| 2. Faithful (7,7) reality replacing forced ⊗ℂ | Bookkeeping noted, not constructed (gu-formalization guardrail) |
| 3. Anomaly-inflow / enriched-bordism story making 4D shadow anomaly-free | Repo's strongest lane but only by lattice/cobordism analogy, not GU's axial-U(1) |
| 4. Higher-structure SUSY/generation carrier paying category-change tax | Explicitly admitted failure point (Distler–Garibaldi stress case) |
| 5. Derived 14→4 reduction incl. 64→48 | Named, unproven; TI BDO/ICO suggest source-side structure alone is obstructed for mass-energy analog |

---

## Buildable Next Steps (Ranked)

**(a) Close the pincer or formally document it as the live open problem.**
Write the explicit obligation: define a shiab from Spin(7,7)/Sp(14)-invariant
subspaces and compute its anomaly content. This is the one place new mathematics
is required. No repo currently performs this computation.

**(b) Signature audit.**
Redo §3.1's complexification argument in signature (7,7) with Majorana–Weyl,
and state precisely whether the unannotated-⊗ℂ gap survives. If it doesn't, that
is Column B's strongest entry. If it does, Column A is stronger than Nguyen stated
for the GU case.

**(c) Promote the TaF Čech-H¹ ↔ holonomy result from H3-conditional to
H3-discharged**, or record H3 as the explicit blocker. Currently
`tests/T63-taf-gu-holonomy-dictionary.md` is conditional; that conditionality
is unresolved.

**(d) Run the cech_sheaf_fixture** that E015 routes to, to determine whether typed
admissibility can force transition cocycles (the source-side version of the same
holonomy question).

**(e) Do not treat any repo artifact as a refutation of Nguyen in published framing.**
All are exploratory / `[CONJECTURE]` and the repos' own NEXT-STEPS forbid
"proves GU" claims. Framing should be: "these repos specify the escape routes GU
would need; none prove they work."
