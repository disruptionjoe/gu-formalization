---
title: "Objective 6 — External Verification Package & Three-Level Legibility Structure"
status: exploration
doc_type: verification-package
created: 2026-07-13
authored_by: obj6-hardening-run (5-persona inline team)
scope: >
  A one-hour-legible external verification package for the program's flagship results.
  NOT committed. Does not change canon, RESEARCH-STATUS, claim-status, or any verdict.
freshness_check: "all cited flagship tests re-run 2026-07-13; exit codes recorded in Appendix A."
---

# Objective 6: Verification Package & Three-Level Legibility

**Purpose.** Let a new expert decide, within an hour, exactly what this program has **proved**,
what it has **computed in a finite model**, what it has **imported** from the literature, and what
remains **conjectural** — and what would **falsify** the leading physical interpretation. The value
of this document is entirely in whether its labels are *true*. Where a label was found to overstate
the evidence, it is flagged as a **CORRECTION** in-line and in §5.

**Honesty boundary (read first).** Everything below is **internal tier**: reproduced and
adversarially re-verified *within this single process*, **not** independently replicated and **not**
peer-reviewed. A green test run (Appendix A) means "the arithmetic and structure re-derive from
scratch on your machine," per `REPRODUCE.md` and `CANON.md` ("Canon means safe to cite as the
current public spine; it does not mean proved physics"). No result here is a physics derivation of
Geometric Unity, and the program's headline physics verdict — the generation count — is **OPEN**.

---

## 0. The three legibility levels (definitions)

Every flagship claim is sorted into exactly one of three levels, and its **imports** and
**open/conjectural** dependencies are listed separately so nothing hides.

| Level | Meaning | What a green test proves about it |
|---|---|---|
| **L1 — PROVEN MATHEMATICS** | Established *exactly* from stated assumptions by a real proof (symbolic / from axioms / from cited theorems used correctly). True regardless of GU or nature. | The finite/symbolic instances re-derive; the *proof* is in the prose, the test is corroboration. |
| **L2 — COMPUTED MODEL RESULTS** | Demonstrated in a *specific finite model, numerical calc, or truncation* (e.g. one-loop, a `ker Γ` projector, a K3 fiber, exhaustive small cases). True *of that model*; generalization is a separate claim. | The model computation reproduces to stated tolerance/exactness. |
| **L3 — PHYSICAL INTERPRETATION** | A claim connecting L1/L2 to GU or to nature ("GU is renormalizable," "the observer is forced to break symmetry," "GU predicts 3 generations"). | A test can only *confirm the math it rests on*, never the interpretation. |

Two cross-cutting tags used throughout:
- **IMPORTED** — a load-bearing fact taken from published literature (cited, not re-derived here).
- **CONJECTURAL / OPEN** — an unclosed bridge; named, not leaned on.

**The single most important legibility fact about this program:** its L1 mathematics is real and
often strong, but **every L3 physical interpretation of a flagship is either OPEN or has a recorded
honest BREAK.** The clearest evidence is Flagship (d): a physical-realization attempt that the
program *retracted* rather than rescued.

---

## 1. Three-level classification of the flagships (the one-hour map)

| Flagship | L1 PROVEN (math, from assumptions) | L2 COMPUTED (finite model / truncation) | L3 PHYSICAL INTERPRETATION (status) | Net confidence |
|---|---|---|---|---|
| **(a) Observer / value-selection THEOREM** | The self-referential valuation no-go: **(I-a)** no weakly point-surjective `T:A×A→B`; **(I-b)** no `α`-invariant valuation; **(II)** the forced valuation is symmetry-breaking. Real proof from A1–A4 (Lawvere/Yanofsky contrapositive + Curie partition). | Exhaustive finite-instance confirmation (`W99`, `W70` over \|A\|∈{1,2,3}, `W73`). | "The observer/source is forced into a symmetry-breaking **value**; the source action *is* the observer; firewall." **UNPROVEN.** Its one physical-realization attempt is the **W98 BREAK** (Flagship d). | Math **HIGH**; physical reading **LOW/OPEN** |
| **(b) UV result (renorm + AF/AS + unitary-on-physical-sector), HORN K** | Little at flagship grade. Closest-to-proved pieces: `no-local-positive-metric` (machine-checked), the exact `f₂²*=0` Gaussian-root algebra (S1), homogeneous-quadratic no-interacting-FP (structural). | **All four results are L2:** one-loop truncation + `ker Γ` finite spin-3/2 projector + ported agravity β-functions + keep-and-grade Krein. Renormalizability, asymptotic freedom, unitarity-*trade*, tachyonic price. **HORN K** (`f₂²*=0` selected) = the interacting-ghost horn, repo-native answer on its own W83 data. | "**GU** is renormalizable, asymptotically free, and unitary." **Truncation-conditional; loop-positivity OPEN; the modular/firewall closure BREAKS (W98).** | Model-level **MEDIUM-HIGH**; physical UV completion **OPEN** (horn K vs Q undecided) |
| **(c) Generation count located-not-forced, {1,3} no-go** | **Theorem-grade cores:** 2-primary lemma `Hom(Z/3,2-group)=0`, CRT split `Z/24=Z/8⊕Z/3` (**Lean-verified**, no `sorry`), finite-dim Krein index conservation (Thm 2), Schur, oddness ⇒ count ∈ {1,3}, ceiling `3 = dim Λ²₊(R⁴)`. From standard citable math. | `W55–W60`: deterministic index / anomaly-inflow / cobordism / homotopy-torsion / no-go / SU(2)₊ checks. | "**GU predicts / forces 3 generations.**" **NOT forced** — 3-vs-sterile-1 needs input C1 (spin=flavor); framing presupposes the torsion-count reading; only honest computable integer is **1**. Count **OPEN** in `RESEARCH-STATUS.md`. | Math cores **HIGH**; the "3" **OPEN** |
| **(d) Sectorial-closure BREAK (W98)** | — (this is a *retraction*, not a new result) | `W98`: in a genuine interacting type-III₁ continuum region, the three closure properties **cannot** hold simultaneously (`P1 XOR P3`); W94 closure demoted to a finite-mode toy artifact. | Removes the physical modular realization of the observer conjecture (a) and of the horn-K firewall (b). **Honest falsification.** | Break **MEDIUM-HIGH** (symmetric with W94's original grade) |

**Reading the table in one sentence:** the program has genuine **proven mathematics** (a-L1, c-L1),
solid **computed-model** UV results (b-L2), a real **honest retraction** (d) — and **no flagship's
physical interpretation is closed**; every L3 arrow is OPEN or broken, which is exactly what the
program says.

---

## 2. Per-flagship verification packages

Each package has the requested nine fields. All file paths absolute under
`C:\Users\joe\JB\CapacityOS\repos\public\gu-formalization\`.

### (a) Observer / value-selection THEOREM — **L1 PROVEN (math) + L3 OPEN (physics)**

- **Paper:** `papers\candidates\observer-value-selection-theorem\observer-value-selection-theorem-2026-07-11.md`
  ("A Self-Referential Valuation No-Go and the Forced Symmetry-Breaking of the Residual").
- **Formal claim (verbatim, §3).** For a category with finite products, nonempty `A`, two-valued
  `B`, and fixpoint-free involution `α:B→B` (A1–A4): **(I-a)** no weakly point-surjective
  `T:A×A→B` exists; **(I-b)** no valuation `p:A→B` is `α`-invariant; **(II)** taking `G=⟨α⟩≅Z/2`,
  every total valuation is *value-type* (symmetry-breaking), so "the selection an observer is forced
  to make is, provably and non-circularly, a symmetry-breaking one."
- **Exact assumptions (§2).** A1 finite products; A2 two-valued grading; A3 **fixpoint-freeness of
  the firewall** ("the single substantive hypothesis"); A4 nonempty arena. Explicitly: "No topology,
  measure, dynamics, order, or physical structure enters."
- **Dependency graph.** (I-a) ← Lawvere 1969 / Yanofsky 2003 weak fixed-point lemma, used
  contrapositively (with B=2 this *is* Cantor). (I-b) ← elementary `Fix(α)` equalizer count. (II) ←
  Z/2 action + Curie/Earman arena-vs-value partition. No dependence on other in-repo results.
- **Proof/derivation pointer.** Complete elementary proof in the paper **§4** (4.1–4.3). Real and
  valid at the stated level.
- **Executable reproduction.** `python tests\W99_theorem_finite_instances.py`;
  `python tests\W70_path5_D_lawvere.py`; `python tests\W73_H62_arena_value_partition.py` (stdlib,
  deterministic; each prints `[PASS]`, exits 0). Or `python scripts\reproduce_all.py -k W99`.
  Each test's docstring states "CONFIRMATION, NOT PROOF."
- **Known failure modes (§5, §7).** With `α=id_B` (A3 removed) **no selection is forced** — A3 is
  load-bearing. A genuine **third grade** `{below, boundary, above}` with `α` fixing `boundary`
  **defeats both (I-a) and (I-b)** (any admissibility scheme with a stable neutral verdict is out of
  scope). **No physical/operator-algebra realization exists** — the modular-conjugation attempt
  "did not go through … recorded as the `W98` break."
- **Strongest adversarial objection.** "This is just Cantor/Lawvere/Curie in physics costume; the
  'observer is forced to a *value*' is a semantic bridge the skeleton does not force." (W70 itself
  records: "'the residual IS the value' is NOT forced by the skeleton.")
- **Answer.** The paper concedes it — self-labels **"(b) NOVEL PACKAGING,"** credits
  Lawvere/Yanofsky/Cantor + Curie/Earman, and claims only synthesis. The *math* stands; the physical
  reading is disclaimed in §7.
- **Confidence grade.** Math: **HIGH** (elementary, exhaustively finite-checked). Physical reading:
  **LOW / OPEN** (no realization; W98 break). Publication Joe-gated.
- **HONESTY AUDIT.** Label **HONEST with one required separation.** The object is a *genuine theorem*
  correctly proved (not a strong argument dressed as a theorem), but its **core is IMPORTED**
  (Lawvere/Yanofsky/Cantor/Curie) and its **physical interpretation (L3) is unproven** with a
  recorded break. **CORRECTION for the newcomer:** do not read "observer/value-selection theorem" as
  a proven physics statement about GU. Proven = the set-theoretic no-go. Unproven = every word that
  makes it *about observers, sources, or firewalls*.

### (b) UV result — renormalizable + asymptotically free/safe + unitary-on-physical-sector, HORN K — **L2 COMPUTED (truncation-conditional)**

- **Paper:** `papers\candidates\uv-structure-fourth-order-gravity\uv-structure-fourth-order-gravity-2026-07-11.md`
  ("Renormalizable, Asymptotically Free, and Unitary Fourth-Order Gravity — and the Tachyonic Price
  of Asymptotic Freedom").
- **Formal claims (abstract, verbatim keys).** (1) **Renormalizability:** power-counting
  renormalizable; the `ker Γ` transverse spin-3/2 projector has momentum-degree zero and removes the
  Velo-Zwanziger non-renormalizable modes. (2) **Asymptotic freedom:** unique Gaussian UV fixed
  point, made structural by the homogeneous-quadratic one-loop system (`b₂=133/10>0`; Weyl coupling
  predicted). (3) **Unitarity:** on the physical subspace the inner product is positive (massive
  spin-2 Krein-graded, PT-unbroken; scalaron positive-norm); "loop unitarity is a
  positivity-vs-causality trade." (4) **Tachyonic price:** the same AF *forces* the
  conformal-scalaron mass-squared negative (background-independent instability). Fork: AF-with-tachyon
  **or** asymptotic-safety-with-(possible)-stability.
- **What HORN K is / the truncation.** In `β_{f₂²} = −κ f₂⁴(b₂ᵍʳᵃᵛ+b₂ᴿˢ) + η_C f₂²`, **HORN K** =
  `f₂²*=0` (the interacting/genuine-ghost fixed point, `η_C=0` Weyl-adapted scheme). Repo-native
  answer on the repo's **own W83 data** (Reuter FP at `g*=0.674, λ*=0.151, f₂²*=0`), per
  `W87_horn_k_vs_q`. The whole flagship is conditional on: **one loop**; the **`ker Γ` finite
  projector**; **ported agravity β-functions**; **keep-and-grade Krein**; `c_RS_weyl` a *band*
  [1.02,1.82] (not heat-kernel-computed); `η_C` **scheme-conditional**.
- **Assumptions.** GU's induced `|II|²` action sits in the Stelle/agravity 4th-order class (so ported
  betas apply); `ker Γ` projector exact/background-independent/degree-0; `c_RS_weyl > −13.3`
  (AF-survival); homogeneous-quadratic one-loop system; **HORN K selection = Weyl-adapted scheme**
  (argued, not proven); Krein grading with real (PT-unbroken) ghost spectrum.
- **Dependency graph.** `H58 (W44)` renorm → `H57s1 (W45)` → `H57s2 (W46)` → `H60 (W47)` AF-firm →
  {`H59 (W48)` loop-positivity **OPEN**, `E2 (W81)` AS fork}. The observer/firewall sectorial closing
  `W94` rests on Condition-(i)=**HORN K** (`W95`), Condition-(ii)=AQFT-per-region-J (`W96`),
  Condition-(iii)=all-orders value-selection (`W97`) — all three collapse onto the shared
  **infinite-rank Krein definitizability** residual (= the horn-K/Q deciding computation).
- **Proof/derivation pointer.** `H58` power-counting = **COMPUTED** (explicit 4×4 projector,
  residuals ~1e-16; not a BRST all-orders proof). AF = **DERIVED-on-PORTED** (agravity betas ported;
  FP structure derived; no GU loop integral run). No-interacting-FP = **STRUCTURAL**. No-local-metric
  = **machine-checked**. Connes RN-cocycle value-selection = **IMPORTED theorem**. No flagship-level
  closed theorem.
- **Executable reproduction.** `python tests\W44_H58_rs_power_counting.py`,
  `W45_/W46_/W47_` (AF), `W48_H59_krein_loop_positivity_gate.py`, `W81_E2_asymptotic_safety.py`,
  `W87_horn_k_vs_q.py`, `W95_cond_i_horn_k.py`, `W96_cond_ii_aqft.py`, `W97_cond_iii_all_orders.py`.
  Numpy-only; each exits 0. Or `python scripts\reproduce_all.py --quick`.
- **Known failure modes.** Complete 2-loop Weyl RGE not available → `η_C` sign (hence HORN K vs Q)
  **undecided**; `η_C` **scheme-conditional** (EH-adapted scheme → HORN Q, removable ghost); loop
  positivity (`H59`) **OPEN** (`READY_FOR_LOOP_POSITIVITY_COMPUTE`, not done); infinite-rank type-III
  Krein modular-conjugation theorem **missing** (Shulman only rank-1); tachyon **forced** on the AF
  route; Reuter FP **truncation-dependent**; **no built source action** to run BRST/loop-positivity on.
- **Strongest adversarial objection (cond-i, conceded in-doc).** "Complete two-loop HD-gravity RGEs
  would settle `sign(η_C)` and they don't exist, so you cannot claim HORN K."
- **Answer.** "Agreed, and it is the honest core of the grade." It blocks *firmable-now* but the
  adversary equally cannot exhibit a computed lift → verdict **FRONTIER (firmable-leaning)**, not a
  theorem. Not defeated; graded.
- **Confidence grade.** Model-level results **MEDIUM-HIGH** and reproducible; HORN K selection
  **FRONTIER**; UV completion (AF-vs-AS) **OPEN**. Target hep-th, Joe-gated.
- **HONESTY AUDIT.** The **COMPUTED-MODEL / truncation-conditional label is HONEST and applied
  conscientiously** (every quantitative claim carries a KNOWN/PORTED/COMPUTED/DERIVED grade; the
  one-loop truncation, scheme-conditionality, banded `c_RS_weyl`, and open loop-positivity are stated
  prominently; the title itself foregrounds the *tachyonic price*). **CORRECTION (register slip):**
  the paper **abstract's** flat headline "the theory is renormalizable, asymptotically free, **and
  unitary**" is **stronger than the body supports** — §5/§8 make loop-positivity **OPEN** and
  "unitary on the physical sector" is a *tree/algebraic + no-local-metric result + a
  positivity-vs-causality trade*, not a performed loop-positivity computation. For an outsider,
  read it as: **"unitary at tree/algebraic level with a machine-checked no-local-metric theorem;
  loop unitarity is an open positivity-vs-causality trade."**

### (c) Generation count located-not-forced, {1,3} no-go — **L1 PROVEN cores + L3 OPEN ("3")**

- **Papers:** flagship restatement
  `papers\candidates\generation-number-located-not-forced\generation-number-located-not-forced-2026-07-11.md`
  ("Class-Wide No-Go and the SU(2)+ Reduction", tied to W55–W60); fuller formal paper (Theorems 1 & 2,
  all caveats, internal v2.12 + arXiv `.tex`)
  `papers\candidates\located-not-forced\located-not-forced-generation-count-2026-06-29.md`; companion
  `papers\candidates\generation-number-boundary-odd-primary\generation-number-boundary-odd-primary-2026-07-11.md`
  (primary-partition Lemma verbatim). Canon spine: `canon\two-primary-lemma.md`,
  `canon\two-arena-rep-theory-core-RESULTS.md`, `canon\single-decider-integer-index-RESULTS.md`,
  `canon\ko-degree-obstruction-ladder-RESULTS.md`, `canon\order3-equivariant-rho-RESULTS.md`.
- **Formal claim.** Across five blind constructions (A index, B anomaly-inflow, C cobordism, D
  homotopy-torsion, E adversarial no-go): the generation number is **not forced** by first-principles
  topological/representation selectors; it is a mod-3 torsion datum **forced into {1,3} and
  3-primary** (2, 4, … excluded by the self-dual 2-form structure; ceiling `3 = dim Λ²₊(R⁴)`), but
  **3-over-1 is not forced** (the sterile 1-generation solution is anomaly-free and admissible).
  Forcing 3 is **provably equivalent to identifying the family bundle with the self-dual frame
  adjoint** (spin = flavor, "input C1"), which first principles do not supply.
- **Assumptions.** Count selected by a topological/rep-theoretic invariant on an oriented 4-base;
  `π₃ˢ=Z/24=Z/8⊕Z/3`; the constructions are the standard index/inflow/cobordism/homotopy ones.
- **Dependency graph.** two-primary/`Hom(Z/3,Z)=0` obstruction → four blind constructions converge
  (Result 1 no-go) → forced content {1,3}, 3-primary (Result 2) → SU(2)₊ reduction closes the escape
  as a first-principles route (Result 3) → single open input **C1**. GU appears only as the source of
  one **unclosed** graded/"guardian" escape (examined, found *not* a spacetime symmetry → long shot).
- **Proof/derivation pointer & level split (paper §6, §8).**
  - **L1 PROVEN (theorem-grade, §8):** the mathematical cores — the 2-primary/primary-partition
    Lemma (`Hom(Z/3, 2-group)=0`, `gcd(3,2^k)=1`), the CRT two-arena split `Z/24=Z/8⊕Z/3`
    (**Lean-verified**: `tests\big-swing\R4_TwoArena.lean`, exit 0, no `sorry`/axiom), Theorem 2
    (finite-dim Krein index conservation ⇒ no net chirality without a boundary — the finite shadow
    of Nielsen-Ninomiya), Schur, oddness ⇒ {1,3}, ceiling `dim Λ²₊=3`. "checked by deterministic
    computation against standard, citable mathematics."
  - **L2 COMPUTED:** `W55–W60` (index, anomaly-inflow, cobordism, homotopy-torsion, no-go, SU(2)₊).
  - **IMPORTED:** 3-primary location — Garcia-Etxebarria-Montero (1808.00009), Wan-Wang-Yau; inflow —
    Nielsen-Ninomiya / Callan-Harvey / Kaplan; cobordism homomorphism — Freed-Hopkins.
  - **CONJECTURAL / OPEN:** the value **3** (needs C1 closed or an anomaly forbidding the sterile
    axis); the GU graded-guardian route.
- **Executable reproduction.** `python tests\W55_path3_A_index.py` … `W60_path3_wave2_su2plus.py`
  (all exit 0). Or `python scripts\reproduce_all.py -k W5` / `-k W60`.
- **Known failure modes.** The whole thing is a **no-go, not a derivation of 3** — if C1 is later
  supplied by a specific theory, 3 is forced (the no-go then does not apply to that theory); the
  rank-1 sterile axis is admissible in every construction; the mod-3 Dai-Freed arena for the SM is
  empty (`Ω^Spin_5(BG_SM)⊗Z_(3)=0`), i.e. the anomaly is generation-blind.
- **Strongest adversarial objection (the category-error / integer-index attack — the sharpest one to
  press).** "A nonzero class in `Z/3` detects information mod 3; it is not the integer 3, and
  `Hom(Z/3,Z)=0` means there is no class-to-count map at all. Worse: the entire positive framing
  rests on the **torsion-count reading** (caveat a) — under a literal *integer-index* reading, the
  same net-index-0 result would *forbid* an odd count outright. So 'located, not forced' surrenders
  the count and is a restatement that the tools cannot see it. And the only honest computable integer
  on the real geometry is **1** (GU's own Pati-Salam `Spin(7,7)` → exactly one anomaly-free
  generation) — evidence tilts toward one, not three." (Secondary steelman, §5: gauging SU(2)₊ makes
  Λ²₊ irreducible, so any matter forces rank 3.)
- **Answer.** The count objection is **conceded, not rebutted** — the paper front-loads it as caveats
  (a)-(b), states "This paper does NOT claim three generations," and reframes the deliverable as a
  *no-go that LOCATES*: the theorem-grade cores survive the objection intact even though the count
  claim is surrendered by it. On the SU(2)₊ steelman: gauging a group never forces its matter into the
  adjoint (`Rep(SU(2))` has every dimension; singlet rank-1 survives, anomaly-free); Schur forces 3
  *only given* C1; decisively the frame SU(2)₊ acts on **spin**, the generation label is a Lorentz
  **scalar (flavor)** — promoting Z/3→SU(2)₊ *relocates* the sterile axis, does not forbid it.
- **Confidence grade.** Math cores **HIGH** (theorem-grade, computation-checked); framework-facing
  legs **reconstruction grade**; the value 3 **OPEN**. `RESEARCH-STATUS.md`/`CANON.md`: generation
  count **OPEN**; nothing derives three. Target hep-th/math-ph, Joe-gated.
- **HONESTY AUDIT.** **Labels HONEST — and unusually self-critical** (the docs record their own
  in-line downgrades: "EMPIRICAL → PARTIALLY STRUCTURAL"; a corrected `e_R=1/12` order-label error;
  Theorem 1 regraded "as a finite adversarial hunt rather than a closed proof"; deciders assert
  `integer_is_3=False` and the `+8` RS leg was "explicitly refused rather than fabricated"). The
  genuinely referee-proof core is real and machine-checked (CRT split Lean-verified, no `sorry`;
  finite-dim Krein Theorem 2). Two disclosures a reader must carry: **(i)** "complete for class C"
  (Theorem 1) is COMPUTED (enumeration + engine sweep), *not* a closed impossibility proof over all
  operators — the paper says exactly this and bounds where C breaks; **(ii) the sharpest contingency
  — the positive "located, not forced" framing presupposes the *torsion-count reading*; under an
  integer-index reading the same math forbids an odd count.** This is disclosed (caveat a), not
  hidden, so no label is *dishonest* — but an outsider should read "located, not forced" as
  *contingent on the torsion reading*, and should note the only honest computable integer is **1**,
  so the evidence tilts toward one, not three. Matches the standing verdict: "GU **locates** the
  count, does **not force** it."

### (d) Sectorial-closure BREAK (W98) — **HONEST FALSIFICATION / RETRACTION**

- **Writeup:** `explorations\break-sectorial-closure-interacting-2026-07-11.md`.
  **Test:** `tests\W98_break_sectorial_closure.py` (7/7 checks, numpy-only, `SystemExit(0)`).
- **What was held (W94).** `explorations\sectorial-relative-j-2026-07-11.md` /
  `tests\W94_sectorial_j.py` asserted, on a **finite-mode / mode-diagonal (free, one-loop) toy**,
  that the observer conjecture's physical firewall modular conjugation `J=C·PT` **closes sectorially**
  (per definitizable Pontryagin `Π_κ` sub-sector) even though no global `J` exists — and that the
  global `J`'s non-existence *is* the observer-relativity. This underwrote the conjecture "the source
  action **is** the observer" and the horn-K firewall reading.
- **What BROKE.** Verbatim verdict: **"BREAKS-AT-1. The sectorial closure does NOT survive the
  relaxation to a genuine interacting continuum region: it was a FINITE-MODE / mode-DIAGONAL TOY
  ARTIFACT."** Closure needs three properties simultaneously — (P1) every finite region has a bounded
  `J_O`; (P2) regional `J`'s cohere on overlaps; (P3) no global bounded `J`. In a *genuine* finite
  spacetime region (type III₁ by Reeh-Schlieder → contains the whole UV momentum tower), the Krein
  healthy/ghost frequencies degenerate in the UV `Δω(k)=|m₁²−m₂²|/(ω₁+ω₂)→0` **independent of the
  mass gap**; any non-UV-soft interaction drives the exceptional-point parameter `r_k→1`, so
  `‖J_O‖→∞`: **P1 fails**, **P2 fails**, and **P1 XOR P3** (a region already contains all UV modes,
  so `sup_region = sup_global`). W94's decisive error: it read the observer's region as a finite-
  **resolution UV cutoff** (finite rank, definitizable) rather than a genuine finite **spacetime
  region** (type III₁, infinite rank) — "a region is not a cutoff."
- **Genuine retraction?** **Yes.** The program explicitly **demotes** W94 from "sectorially closed"
  to "finite-mode toy artifact that BREAKS-AT-1 in the interacting continuum," steelmans survival
  first, and names the single load-bearing survival window (an interaction UV-soft faster than `1/k`,
  e.g. `g(k)~1/k²`) — which the physical derivative-coupled Weyl² ghost does **not** satisfy, so on
  the physical reading the break is generic. The MATH-REFEREE persona rules the obstruction "genuine …
  not a numerical fudge."
- **Relation to the UV flagship (b).** The break bites **exactly where the free theory worked**:
  free/mode-diagonal closure succeeded because the ghost was a clean removable grading; interaction
  (the physical Weyl² ghost) is what breaks P1/P2. It **does not threaten** the renormalizability /
  AF results — it removes the *observer/firewall sectorial-closure* reading that was to ride on top of
  a genuine interacting horn-K region. Either W87 horn outcome is consistent with the break: HORN K
  (`f₂²*=0`) → break stands; HORN Q → closure is vacuous anyway.
- **Executable reproduction / exit.** `python tests\W98_break_sectorial_closure.py` → asserts all 7
  break-checks (T2 conditioning grows 8890→17779→35557 under UV doubling; T5 P1-XOR-P3; T6 overlap
  disagreement 0.32→10.97→34.70 vs free=0), then `SystemExit(0)`. **Exit 0 means "the break is
  confirmed,"** not "closure holds."
- **Confidence grade.** **MEDIUM-HIGH** (symmetric with W94's original grade; it removes W94's
  survival). Not committed; touches no canon/status/posture file.
- **Why it belongs in a verification package.** It is the cleanest evidence the program **retracts
  honestly**: a previously-claimed sectorial closure, adversarially re-tested in a more physical
  model, was withdrawn and demoted rather than defended — and the withdrawal is itself a runnable,
  reproducible certificate.

---

## 3. Recommended location & format

**Recommendation: promote a hardened version of this file to a repo-root `VERIFICATION.md`,** the
outsider's entry point, and keep the working long-form here in `explorations/`.

Rationale:
- The repo already has `REPRODUCE.md` (how to *run* the certs) and `RESEARCH-STATUS.md` /
  `CANON.md` (the *internal* ledger). What is missing is a **one-hour outsider map** that a new
  expert hits first: "here are the ~3 flagships, here is proven/computed/imported/conjectural for
  each, here is the one command to reproduce, here is what would falsify the leading reading."
  `VERIFICATION.md` at root, linked from `README.md`, fills exactly that gap and sits beside
  `REPRODUCE.md` as its claims-side companion.
- **Format:** keep §1 (the three-level table) and §2 (the nine-field packages) verbatim; each
  flagship links its paper, its `tests/W…` certs, and one `python scripts\reproduce_all.py -k …`
  line. Lead with the **honesty boundary** (internal tier) and the **BREAK (d)** as a first-class
  entry, not a footnote — the break is the credibility of the whole document.
- **Do not** put this in `canon/`: it is a navigational/verification aid, not a scientific verdict.
  Promotion to `VERIFICATION.md` is a docs move (agent-ownable per the Promotion Rule); it changes
  no verdict and should run the claim-status-consistency sweep so no stronger wording leaks in.

Until that promotion, **this exploration file is the deliverable.**

---

## 4. Five-persona inline review

**P1 — Skeptical newcomer-expert (must navigate it in an hour).** "The three-level table is the
thing I needed: I can see in one screen that (a) is real math with a costume, (b) is one-loop
model-conditional, (c) proves a no-go not a prediction, and (d) is a retraction. My only risk is
over-trusting words like 'theorem' and 'unitary' — flag both up front." → Addressed: §1 net-sentence
+ the two register-slip CORRECTIONS in (a) and (b).

**P2 — Claims auditor.** "Check the labels against the primary text. (a): paper self-labels 'NOVEL
PACKAGING' and disclaims physical realization — matches L1-math/L3-open. (b): abstract says 'unitary'
flatly but §5/§8 make loop-positivity OPEN — **overstated in the abstract**, must be corrected. (c):
§8 explicitly says 'not a derivation of three generations' and splits grades — accurate. (d):
verbatim 'BREAKS-AT-1' and explicit demotion — accurate." → All findings folded in; the only label
correction that survives audit is (b)-abstract and the (a) proven-vs-physical separation.

**P3 — Adversary (are the labels honest, or is failure being hidden?).** "Two attack surfaces. (i)
Is 'located, not forced' a euphemism for 'we failed to derive 3'? No — the paper *proves* the
non-forcing and names the exact missing input C1; that is a stronger, more falsifiable statement than
a failed derivation, and it is labeled OPEN in the status ledger. (ii) Is the UV 'unitary' hiding the
open loop-positivity? Partly, in the abstract only — the body is honest and the title advertises the
*tachyonic price*. Net: no hidden failure; one abstract-level over-read, now corrected. And (d) is an
adversary's dream — the program itself killed a prior claim." → No dishonest label survived except the
(b)-abstract slip, corrected.

**P4 — Cross-checker (do the tests actually run?).** Re-ran every cited flagship cert 2026-07-13; all
exit 0 (Appendix A), including `W98` which exits 0 *by asserting the break*. Confirmed the canonical
harness `python scripts\reproduce_all.py` discovers all `W44–W99` certs. Confirmed the certs are
numeric/symbolic (numpy/stdlib), not prose-asserts. **One caveat recorded:** exit-0 is *internal
reproduction*, not external replication or a physics claim — stated in the honesty boundary and by
`REPRODUCE.md` itself.

**P5 — Synthesizer.** The program's real shape: **strong L1 mathematics (a, c), a disciplined L2 UV
model (b), and an honest L3 vacancy everywhere** — no physical interpretation of a flagship is closed,
and the one that was attempted (sectorial closure) was retracted (d). The verification package is
trustworthy precisely because its labels survive an adversarial pass with only one correction (the
UV abstract's "unitary"), and because it foregrounds its own retraction. Recommended home:
`VERIFICATION.md` at root. Falsifiers are explicit per flagship (below).

**What would falsify the leading physical interpretation (per flagship):**
- (a) A physical/operator-algebra realization of the valuation no-go that closes (would revive the
  observer reading) — *or* confirmation it cannot (W98 direction). Currently: no realization.
- (b) A complete 2-loop Weyl RGE fixing `sign(η_C)`: `η_C>0` ⇒ **HORN Q** ⇒ ghost removable ⇒ the
  "genuine firewall / AF-unitary" reading deflates. A performed loop-positivity computation failing
  positivity would falsify "unitary." A scheme-independent statement that the tachyon cannot be
  escaped would kill the AF route.
- (c) Any first-principles theory supplying **C1** (spin=flavor / an anomaly forbidding the sterile
  axis) would *force 3* and end "located, not forced" for that theory; conversely a demonstrated
  admissible sterile-1 world confirms it.
- (d) A UV-soft interaction (`g(k)` decaying faster than `1/k`) in the physical GU ghost sector would
  save sectorial closure — currently believed absent, hence the break stands.

---

## Appendix A — Freshness check (re-run 2026-07-13, exit codes)

Command form: `python tests\<file>.py` (per-file), cross-checked via `python scripts\reproduce_all.py`.
All exit codes **0** (for `W98`, exit 0 = the break is confirmed).

| Flagship | Tests re-run | Exit codes |
|---|---|---|
| (a) Observer theorem | W99, W70, W73 | 0, 0, 0 |
| (b) UV / horn K | W44, W45, W46, W47, W48(H59), W81, W83, W87, W88, W95, W96, W97 | all 0 |
| (b) extras | W73(arena), W75, W76, W63, W70 | all 0 |
| (c) Generation {1,3} | W55, W56, W57, W58, W59, W60 | all 0 |
| (d) Sectorial BREAK | W98 (+ W99 finite-instances) | 0, 0 |
| Structural spine (cross-check) | big-swing/R4_crt_two_arena, big-swing/R3_signed_readout_certificate | 0, 0 |

Harness sanity: `python scripts\reproduce_all.py --quick` over the selected slice → **VERDICT: GREEN**.
Environment: Python 3.14.3, numpy/scipy/sympy per `requirements.txt` (exact-fact certs, not
tolerance-sensitive).

---

## Appendix B — Label corrections found by this audit (summary)

1. **Flagship (a):** the proven object is the **set-theoretic** valuation no-go (IMPORTED core:
   Lawvere/Yanofsky/Cantor + Curie). The **physical** "observer/source/firewall value-selection"
   reading is **L3 UNPROVEN** with a recorded break (W98). Separated explicitly; paper is honest
   (self-labels "NOVEL PACKAGING").
2. **Flagship (b):** the paper **abstract's** "renormalizable, asymptotically free, **and unitary**"
   over-reads the body — loop-positivity is **OPEN** (`H59`), so "unitary" should read "unitary at
   tree/algebraic grade + machine-checked no-local-metric theorem; loop unitarity an open
   positivity-vs-causality trade." Body and all exploration files are honest; only the abstract
   headline slips.
3. **Flagship (c):** no correction needed — labels honest; §8 already splits theorem-grade cores from
   reconstruction-grade legs and denies deriving 3.
4. **Flagship (d):** no correction needed — an honest, reproducible retraction, correctly graded.
