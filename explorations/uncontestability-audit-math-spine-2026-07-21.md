---
title: "UNCONTESTABILITY audit of the load-bearing math spine — hostile-but-fair (honest expert primed to dismiss unaffiliated work). Inline 3-persona panel (proof-checker / adversarial math-physicist / reproducibility auditor). Kernel-checked what was checkable: ResidualSelection.lean kernel-checks EXIT 0 with NO axioms (8 theorems), reproduce_all.py 31/31 EXIT 0. VERDICT: the spine is honestly graded to a rare degree — often OVER-hedged in the deep files — so almost nothing is graded above its support at the file level; it is NOT yet 'uncontestable' to a primed skeptic, but the contestable joints are FRAMING + VERIFICATION-TIER, not mathematics. The 5 must-fix items are (1) internal-tier ceiling / zero external replication, (2) README charter compresses past its own hedges on three words ('result', 'forces', 'complete modulo'), (3) the one load-bearing falsifiable (DE sign) is conditional + non-distinctive, (4) the σ=w₁ cluster is a 3-link PROPOSAL chain stated as 'exactly two data' in the ledger line, (5) the 'machine-verified' index theorem is Lean-checked only modulo numpy-verified premises. No planted-toy overclaim survives in the current spine (the one prior instance was self-caught and corrected)."
status: active_research
doc_type: exploration
created: 2026-07-21
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
directed_by: "Joe direct chat, 2026-07-21 (hostile-but-fair uncontestability audit of the load-bearing math spine; ONE synchronous pass; inline 3-persona panel; read-only)"
kernel_checks_run:
  - "lake env lean Lean/GUFormalization/ResidualSelection.lean — EXIT 0 (clean elaboration)"
  - "lake env lean Lean/GUFormalization/ResidualSelectionAxioms.lean — EXIT 0; all 8 theorems 'do not depend on any axioms'"
  - "python papers/candidates/located-not-forced/reproduce_all.py — EXIT 0; 31/31 load-bearing numbers reproduce; every check ships a discriminating control; target-import guard on {3,8,24}"
inputs:
  - README.md (esp. 'Purpose (charter, sharpened 2026-07-21)' + 'The irreducible external ledger')
  - VERIFICATION.md
  - RESEARCH-POSTURE.md
  - CANON.md
  - RESEARCH-STATUS.md
  - papers/candidates/located-not-forced/located-not-forced-generation-count-2026-06-29.md
  - papers/candidates/located-not-forced/reproduce_all.py
  - papers/candidates/located-not-forced/REVIEWER.md
  - papers/candidates/six-axis-testability/six-axis-testability-white-paper.md
  - Lean/GUFormalization/ResidualSelection.lean
  - Lean/GUFormalization/LocatedNotForcedLegs.lean
  - Lean/GUFormalization/CoflipCore.lean
  - Lean/GUFormalization/Status.lean
  - tests/generation-sector/net_chiral_index_invariant.py
  - tests/generation-sector/README.md
  - explorations/anomaly-inflow-swing-2026-07-21.md
  - explorations/pin-bordism-cardinality-2026-07-21.md
  - explorations/lp-lc-deficiency-decisive-2026-07-21.md
  - explorations/per-leg-recovery-state-2026-07-21.md
  - explorations/parsimony-unexplained-joints-ledger-2026-07-21.md
  - explorations/blockbuster-p1-de-sign-covariance-2026-07-19.md
---

# Uncontestability audit — the load-bearing math spine

**The test.** Not "is it correct?" but "does it survive an HONEST, good-faith expert who
is nonetheless primed to dismiss unaffiliated work as crank?" That reader trusts nothing
on adjectives, reads the strongest sentence first, and treats every compression as an
attempted overclaim until shown otherwise. The goal is to find every joint such a reader
contests, ranked by damage, each with a concrete hardening fix.

**Method.** ONE synchronous pass. Three personas reason INLINE in this one worker (never
one agent per persona — Joe's standing rule), then synthesize. Kernel-checked what was
checkable (results in frontmatter; all three EXIT 0). Read-only: no other file edited, no
commit, no push.

**Headline finding up front, stated against my own hostile prior.** I went in expecting to
find claims graded above their support. I mostly found the opposite: the deep files
(`located-not-forced`, the σ-cluster explorations, `per-leg-recovery`, the parsimony
ledger) are graded with a discipline that is *rare* — EXACT / ANALOGY / PROPOSAL / REFUTED
ledgers, kill-conditions declared before computation, planted rigged controls that the
same scorer rejects, and — the strongest single signal — a prior planted-toy overclaim
(the bounded-coefficient collar standing in for true-end asymptotics) that the **program
itself caught and retracted** (`HV-REFUTE`; `lp-lc-deficiency-decisive` §6 reproduces the
toy-vs-true-end divergence on two axes). That is the antithesis of crank behavior. The
formal/computational floor is genuinely strong: the flagship Lean theorems kernel-check
with **no axioms**, and every load-bearing *number* in the lead paper reproduces from first
principles with discriminating controls.

**So the contestable joints are almost entirely FRAMING and VERIFICATION-TIER, not
mathematics.** The spine is not yet "uncontestable" to a primed skeptic — but the reasons
are (a) the irreducible internal-tier ceiling (no external replication; formal verification
covers only finite kernels), (b) a reconstruction gap (the key operators are stand-ins for
an *unbuilt* source action), and (c) charter-level word choices that outrun the repo's own
deep-file hedges. Fixing (b)–(c) is editing; fixing (a) requires an outside human.

---

## The inline panel (independent reasoning, then synthesis)

### Persona (i) — Skeptical referee / proof-checker

*Does every THEOREM-grade claim have a kernel-checked proof or a fully rigorous argument?
Is anything graded above its real support?*

- **Kernel-checked, genuinely (I ran it).** `ResidualSelection.lean` elaborates EXIT 0 and
  its 8 theorems **depend on no axioms** (Lean's own `#print axioms` — not Mathlib's
  standard trio, *zero*). The diagonal/Lawvere no-go, `residual_escapes`, `no_closure`,
  `no_invariant_valuation` are literally kernel-certified and funext-free. Flagship (a) is
  therefore honestly L1. **CLEAN.** The catch the referee immediately makes: the paper
  *itself* concedes this is Cantor–Lawvere 1969, self-graded NOVEL-PACKAGING. Honest.
- **`LocatedNotForcedLegs.lean` / `chi_eq_zero`.** The finite-dimensional core of Theorem 2
  (a K-positive subspace meets a K-isotropic subspace only at 0 ⇒ net chiral index 0) is a
  clean, correct, three-line Mathlib proof. **But** the physically load-bearing premises —
  that GU's chirality eigenspaces *are* K-null (Lagrangian) and a physical subspace *is*
  maximal-K-positive of dim 96 — enter as **hypotheses**, verified only in numpy at 1e-9
  tolerance (`net_chiral_index_invariant.py`; reproduced in `reproduce_all.py`). So "the
  index-conservation theorem is machine-verified" is true for the *implication* and numpy
  for the *premises*. The file's scope boundary says exactly this — but the paper's
  status-table line "theorem (machine-verified)" and VERIFICATION.md do not carry the
  qualifier adjacent. **Slightly-above-support at the adjective level, not the math.**
- **The 2-primary identities (`TwoPrimary` namespace).** `96 = 2^5·3`, spinor-dim not
  div-3, Rokhlin `21σ/8`, adjoint `4k`, lens-η numerator odd — all `norm_num`/`omega`,
  kernel-true, correctly labeled "arithmetic core; the rep-theory fact is a hypothesis."
  **CLEAN.**
- **`CoflipCore.lean`.** A substantial, honest formalization: Part A *derives* the sign
  observables from a finite (1,1) Krein toy rather than stipulating them; Part B proves the
  one-bit accounting over the finite `(Z/2)^4` group. Scope boundary is explicit ("Lean
  checks the finite kernel only… everything physical stays in Markdown/Python"). **CLEAN**,
  correctly scoped.
- **The one honest-map defect I found.** VERIFICATION.md flagship (c) reads "the count is
  forced to {1,3} and 3-primary (a class-wide no-go theorem)." The **current paper proves
  no such thing**: interior net chiral count is even/0 (2-primary), the external count is
  *any* integer (flux number, Aharonov–Casher), multiplicity is natively 3, and the only
  *unconditionally computable* integer is 1. "Forced to {1,3}" is a stale compression that
  the paper's own hedging (v2.1 "removed the necessarily-external overclaim") has since
  outgrown. Because VERIFICATION.md is *billed as the outsider honesty map*, a
  cross-checking referee who trusts it over the paper finds a claim the paper doesn't
  support — the honesty map must be the most conservative surface, not a looser one.
- **Referee verdict.** No THEOREM-grade claim in the deep spine is materially over-graded;
  the mathematics is correct where I could check it and honestly labeled where I could not.
  The defects are (1) VERIFICATION.md flagship (c) staleness and (2) the "machine-verified"
  adjective on Theorem 2 gliding over the numpy premises.

### Persona (ii) — Adversarial mathematical physicist

*Are the computational "tests" genuine or toys? Do the claimed structures hold at the
grade stated (σ=w₁, the reflection-anomaly ID, Pin-bordism cardinality, no-go
class-relativity)? Is any "forced" really only "fits"?*

- **The planted-toy question, head-on.** This session's brief flags a prior planted-toy
  overclaim (bounded-coefficient collar for true-end asymptotics). I checked whether any
  such thing survives in the *current* spine. It does not — and, importantly, the program
  **caught and retracted the prior instance itself**: `lp-lc-deficiency-decisive` §2/§6
  reproduces the collar toy (`P=1+0.2sin`), shows the true flat-geodesic ends have `C_0=√|q|`
  blowing up *exponentially* (not O(1)), and demonstrates the true-end computation differs
  from the toy on **both** axes (the deficiency count *and* the `q<0` crossing the toy never
  sees). Kill-conditions were declared before the computation; controls [b1]–[b4] pass a
  method-power suite *before* GU's case is touched. This is a genuine anti-toy discipline,
  not decoration. **CLEAN — and a credibility asset.**
- **σ = w₁ (orientation/time-reversal Z/2), the reflection-anomaly ID.** Correctly graded
  **MIXED: exact substrate, PROPOSAL 't Hooft anomaly**. The exact parts are real: the
  domain-wall Dirac symbol crossing zero at `{q=0}`, self-adjoint-extension ↔ APS ↔ SPT, and
  the *refutation* that σ is the mod-2 index anomaly (Kramers evenness `det c = q^64`, even —
  machine-corroborated, with an odd-multiplicity `Cl(1,1)` positive control that flips). The
  program uses a banked no-go to *kill* the natural index reading and relocate σ to the
  reflection/Pin family — that is strong, honest work. **But** the promotion "GU carries a
  genuine 't Hooft anomaly" rests entirely on the deck-odd operator action `U N U⁻¹ = −N`,
  which `wave-swing-1` itself tagged ANALOGY/toy (checked in a toy block, not banked at
  operator grade). The doc says this in its own ledger. **Honestly PROPOSAL; the physicist's
  contest is only with any surface that drops the "PROPOSAL."**
- **Pin-bordism cardinality-1 + protection.** Explicitly and correctly **conditional on the
  (proposal-grade) anomaly-inflow ID**, and further gated on an *un-evaluated* exact class
  order in `Ω^{Pin+}_14` (reconstruction-grade — the doc names the single missing number:
  the ABP/Adams SS computation + the Pin η/SW-number value). The controls are genuine
  (standard Pin table `n=0..7` reproduced incl. the `Ω^{Pin-}_2=Z/8`, `Ω^{Pin+}_4=Z/16`
  anchors; the `w1`-blindness non-implication is *exact*, not conditional). The one thing a
  physicist flags: the "cardinality = 1" read-off (τ is a *receptacle label*, not a second
  summand) is a clean argument, but it inherits the proposal grade of the whole chain — so
  the ledger sentence "**Exactly** two data enter from outside" (README) is stating a
  three-link proposal conclusion as if banked. **Honestly graded in the file; contestable in
  the charter line that consumes it.**
- **The reflection-anomaly "excision forbidden ⇒ σ RG-protected" consequences.** Both are
  explicitly PROPOSAL, each labeled "the conditional is exactly 'is the reflection anomaly
  nonzero'." **CLEAN.**
- **No-go class-relativity.** The located-not-forced no-go is scrupulously kept
  class-relative: "complete for the delimited class C," "completeness over the unrestricted /
  function-space theory remains open," "not an impossibility statement over all conceivable
  obstructions." The 2-primary parity backstop (centrality + Schur + even-dimensionality) is
  a genuine table-free argument, not a census gap-filler. **CLEAN.**
- **"Forced" vs "fits" — the physicist's sharpest tool.** `per-leg-recovery` maintains the
  distinction with unusual rigor: given σ,τ *supplied*, every sector is graded Rung-0/Rung-1
  (consistency/hosting), **nothing reaches Rung-2 (native forcing)**, and the summary is one
  line: "most of physics *fits* given the bit, but GU does not yet *force* any of it given
  the bit — and the bit itself is supplied, not derived." This is exactly the honest reading.
  **CLEAN in per-leg; the contest is that the README charter says "forces the dark-energy
  sign," which per-leg (leg 6a) grades as a *conditional* prediction and `blockbuster-p1`
  grades as "DERIVED at toy/symbol grade conditional on SRC-COH-1," not "forced."**
- **The DE sign, adversarially.** `blockbuster-p1` is admirably explicit that (a) the sign is
  derived only at toy grade conditional on an *axiom* (SRC-COH-1, "one Krein form in every
  slot," exhibited in a toy, not derived from the unbuilt `S_IG`) plus three more open links
  (`Z_theta>0`, scalar-block mixing discharge, branch-(a) σ=+1 with "target-read"
  provenance), and (b) `w(z)≥−1` is **not distinctive** — every single-field quintessence
  says it; the distinctive content is only the *rigidity*. A physicist grants the honesty of
  the exploration and contests only the charter compression to "forces."
- **Physicist verdict.** The tests are genuine, not toys; the one prior toy was self-caught.
  Every claimed structure holds at *the grade the deep file states*. No "forced" in the deep
  files is secretly a "fits." The contestable surface is the README charter, which upgrades
  three deep-file grades ("conditional prediction" → "forces", "reconstruction cannot close"
  → "result", "hosts conditionally, gated" → "complete modulo").

### Persona (iii) — Reproducibility / provenance auditor

*Can a stranger reproduce every load-bearing claim from the repo alone? Is source-to-shadow
provenance clean? Are assumptions, rollback conditions, and no-go assumption-audits
explicit?*

- **The lead paper: exemplary.** `reproduce_all.py` recomputes all 31 load-bearing numbers
  from first principles (I ran it: 31/31, EXIT 0, 108 s), **never** hardcodes the target
  integers {3,8,24} (24 = `denom(B₂/4)` via sympy Bernoulli; 8,3 factored from it; 3
  *measured* from the su(2)+ decomposition), and every major check ships a discriminating
  control that must fail on scrambled input (wrong signature → M(128,R); identity Krein
  metric → not (96,96); non-coprime split → not Z/16; K-definite re-grading → |χ|=96). This
  is the gold standard for internal reproduction and is exactly what defuses the
  "verification theater" prior. **CLEAN — an asset.**
- **Assumptions / rollback / no-go audits: explicit and everywhere.** CANON.md carries a live
  correction log (SHIAB-01…05, W2-01, RFAIL-02/03, DARK-ENERGY-01…06 — each a dated
  downgrade or scope-tightening). RESEARCH-POSTURE.md lists the forbidden moves
  ("compatibility-as-derivation," "target data hidden as reconstruction"). The no-go docs
  carry assumption audits and class-relativity caveats. The status-consistency rule
  ("downstream cannot outrank weakest dependency") is even *formalized in Lean*
  (`Status.lean`). **CLEAN — this is a genuine strength a primed skeptic would grudgingly
  credit.**
- **The provenance gap that a stranger actually hits.** The σ-externality result — now the
  README charter's centerpiece — has **no one-command, one-surface reconstruction** the way
  the paper does. Its support "rides on banked structure" spread across ~10 cross-referencing
  exploration files (`wave-swing-1/3`, `prong-0`, `sector-relative-section-theory`,
  `global-anomaly-leg`, `lp-lc-deficiency-decisive`, `anomaly-inflow`, `pin-bordism`). Each
  is individually rigorous with a probe, but there is no single "σ dossier" that linearizes
  the chain end-to-end (operator → `q<0` crossing → `K_S`-null → no self-adjoint realization
  → external Z/2 → = w₁ → Pin receptacle) with the grade and probe at each link and the one
  open number at the end. A stranger *can* reconstruct it, but only by tracing a citation web
  — which, for a primed skeptic, reads as "diffuse, therefore soft." **The paper is one
  command; the charter's centerpiece is a scavenger hunt.**
- **The ceiling: internal-tier, no external replication.** Every result in the spine is, by
  the program's own three-tier vocabulary, "internally established" — reproduced and
  adversarially reviewed *within the same AI-directed process that produced it*. No result
  is externally replicated, peer-reviewed, or signed off by a named specialist. This is
  disclosed relentlessly (caveat (e), VERIFICATION.md "trust the levels not the adjectives,"
  the paper's Verification-status paragraph). Disclosure is honest but does **not** remove
  the vulnerability: for a reader primed to dismiss unaffiliated work, "no outside human has
  ever checked this" is the single highest wall, and it is exactly the wall the crank prior
  is built to see.
- **Auditor verdict.** Provenance is clean and honest *in kind* (correction logs,
  assumption audits, no-go class-relativity, a one-command flagship reproduction). Two gaps:
  (1) the σ-cluster — the charter's load-bearing new result — lacks a consolidated dossier;
  (2) the whole spine is uncrossed at the internal→external tier boundary, and that boundary
  is the credibility ceiling.

---

## SYNTHESIS — the ranked contestability ledger (most-damaging first)

Format per joint: **{claim + grade-as-labeled} · {backing} · {what the hostile-fair expert
contests} · {concrete fix} · {damage}}**.

### 1. The internal-tier ceiling: zero external replication; formal verification covers only finite kernels — **SERIOUS**
- **Claim/grade:** every spine result is "internally established" (disclosed); the Lean layer
  is "a proof-carrying robustness layer for finite kernels."
- **Backing:** GENUINE and honestly disclosed — but structurally load-bearing for
  credibility, not for correctness.
- **Contest:** "The Lean proves Cantor–Lawvere 1969 (conceded), an elementary finite Krein
  lemma, `norm_num` arithmetic, and a finite `(Z/2)^4` action. The *physics* — GU's carrier
  actually having the (+96,−96) form, σ=w₁, the anomaly-inflow ID, the Pin receptacle — is
  kernel-checked **nowhere** and replicated externally **nowhere**. No outside human has ever
  checked this." This is the crank-prior's home turf, and disclosure doesn't disarm it.
- **Fix:** cross the tier boundary on the *smallest* high-value target. Concretely: (a) get
  ONE named specialist to sign off on the located-not-forced core (the ENDORSER-REQUEST
  draft already exists — this is the highest-leverage single action); and/or (b) obtain an
  independent replication of `reproduce_all.py` on a *different toolchain / non-AI* path; and
  (c) port the antilinear index-nullity leg into Lean so the *whole* Theorem-2 conclusion
  (not just the linear leg) is kernel-checked. Until crossed, lead every public surface with
  the internal-tier boundary, not with "result."
- **Damage:** SERIOUS — it is the ceiling on how uncontestable the spine can *be*, not a flaw
  in the math. It cannot be closed from inside the process by construction.

### 2. The README "Purpose/charter" compresses past its own deep-file hedges on three load-bearing words — **SERIOUS**
- **Claim/grade:** charter states σ-externality as "a **result**, not a posture," that the
  program "**forces** the dark-energy sign," and that the construction is "**complete
  modulo** σ, τ."
- **Backing:** each of the three has a deep-file grade that is *weaker* than the charter word.
- **Contest, word by word (the primed skeptic reads the strongest sentence first):**
  - *"result" (σ externality):* `lp-lc-deficiency-decisive` proves LC-SELECTOR about a
    **reconstructed** operator `A~ = −iK_uG d_s + W~` on a reconstructed end geometry; GU's
    actual summit/source action is **BLOCKED / unbuilt** (Weinstein's own "Caveat Emptor,"
    draft eq. 10.10; `per-leg` leg 9 = `BLOCKED_SOURCE_GAP`). The file's own ledger grades the
    σ=w₁ identification "rides on banked structure," not theorem. So "the program's summit
    operator provably does not close" overstates "the reconstruction cannot close, and whether
    GU's unbuilt operator inherits this is reconstruction-grade."
  - *"forces" (DE sign):* `blockbuster-p1` grades it "DERIVED at toy/symbol grade conditional
    on SRC-COH-1" + 3 open links; `per-leg` 6a grades it a *conditional prediction*. "Forces"
    is the repo's own forbidden "compatibility-as-derivation" move applied to itself.
  - *"complete modulo σ,τ":* `per-leg` says given σ,τ physics *fits* at consistency-to-hosting
    grade and "does not yet force any of it," gated on the blocked B5 spine. "Complete modulo"
    reads far stronger than "hosts conditionally, gated on an unbuilt spine."
- **Fix:** sync the three charter words to grades that **already exist verbatim** downstream
  — "the reconstruction cannot close from committed structure (reconstruction-grade for GU's
  unbuilt operator)"; "derives, at toy grade conditional on SRC-COH-1 and an unbuilt action, a
  (non-distinctive) DE sign"; "hosts most of physics at consistency-to-hosting grade,
  conditionally, modulo σ,τ and gated on the blocked source action." The charter's own
  "Honest current standing" paragraph *already* says most of this — the fix is to stop the
  earlier paragraph from outrunning it.
- **Damage:** SERIOUS — the charter is the first thing the primed expert reads, and these are
  exactly the moves RESEARCH-POSTURE.md's guardrails forbid; self-inconsistency here is the
  cheapest possible "gotcha."

### 3. The one load-bearing falsifiable — the DE no-phantom-crossing sign — is conditional on unbuilt structure AND non-distinctive — **SERIOUS**
- **Claim/grade:** "the DE-sign prediction is the load-bearing falsifiable" (README);
  `w(z) ≥ −1` pointwise, PP1 frozen (internal, conditional).
- **Backing:** the co-variance is machine-checked at toy grade (22/22); the *conditionality*
  and *non-distinctiveness* are honestly stated in `blockbuster-p1` §5–7.
- **Contest:** "Your entire falsifiable payload — the one leg the parsimony ledger says
  'carries the entire IBE license' — is (a) a prediction *every* single-field quintessence
  makes, and (b) conditional on an axiom (SRC-COH-1) you assert in a toy, plus `Z_theta>0` and
  a mixing discharge you haven't computed, plus a σ=+1 whose provenance you call 'target-read.'
  Strip those and there is no forced, distinctive prediction left."
- **Fix:** two moves, either raises it out of contest: (i) discharge SRC-COH-1 and `Z_theta>0`
  from the source action so the sign is genuinely *forced* not conditional (same B5 bottleneck
  as everything else — but this is the single highest-leverage physics computation); (ii) in
  *every* public mention, foreground that the distinctive object is the **joint rigidity
  surface** (sign + no-crossing + amplitude-ceiling + one-bit co-flip: one wrong sign kills
  it, no re-fit possible), never the bare sign — `blockbuster-p1` does this; the README does
  not.
- **Damage:** SERIOUS — this is the kill test the program stakes its verdict on; if the one
  falsifiable is contestable as "non-distinctive and conditional," the abduction has no
  observable anchor.

### 4. The σ=w₁ / anomaly-inflow / Pin-bordism cluster is a three-link PROPOSAL chain, but the "irreducible external ledger" states "Exactly two data" as if banked — **SERIOUS (framing) / CLEAN (files)**
- **Claim/grade:** files: MIXED-substrate/PROPOSAL-anomaly, cardinality-1 PROPOSAL conditional
  on the anomaly ID, exact class order reconstruction-grade. README ledger: "**Exactly two**
  data enter from outside: σ … and τ … Both are **provably** unreadable and unmintable."
- **Backing:** the files are impeccably graded (EXACT/ANALOGY/PROPOSAL/REFUTED ledgers, standard
  Pin table reproduced, `w1`-blindness non-implication *exact*). The chain: anomaly-inflow
  't Hooft ID (PROPOSAL, rests on the ANALOGY-tagged deck action `U N U⁻¹=−N`) → Pin
  cardinality-1 + protection (PROPOSAL, conditional on the ID) → exact `Ω^{Pin+}_14` order
  (un-evaluated, reconstruction-grade).
- **Contest:** "'Exactly two' and 'provably' launder a three-link proposal conclusion into a
  banked fact. σ's cardinality-1 is conditional on an anomaly you've tagged PROPOSAL, whose
  load-bearing operator fact you've tagged ANALOGY; τ's Z/3 'locates the three generations' is
  the *open* generation-count question — your own anomaly-inflow doc found the SM mod-3 arena
  **empty**."
- **Fix:** the README already hedges σ's cardinality parenthetically — extend it: in the
  ledger sentence itself write "at most / conjecturally two (σ's and τ's cardinalities are
  proposal-grade; τ's generation role is the open count question)," drop "provably" for τ, and
  name the single closing number (ABP-exact `Ω^{Pin+}_14` order + the operator-grade deck
  action). Consider consolidating the cluster into one σ-dossier (see item 8).
- **Damage:** SERIOUS if the ledger line is read as banked (a primed skeptic will); the cluster
  itself is CLEAN and is some of the best-disciplined work in the repo.

### 5. The "machine-verified index-conservation theorem" is Lean-checked only modulo numpy-verified premises — **SERIOUS (adjective) / CLEAN (math)**
- **Claim/grade:** Theorem 2 status line: "theorem (machine-verified; structure-level symbolic
  proof over abstract cross-chirality Krein space)."
- **Backing:** `chi_eq_zero` is genuinely kernel-checked; the premises (chirality eigenspaces
  K-null; physical subspace maximal-K-positive dim 96) are numpy at 1e-9, disclosed in the Lean
  scope boundary.
- **Contest:** "The Lean proves `K-positive ∩ K-isotropic = {0} ⇒ χ=0` — near-trivial. That
  GU's carrier *satisfies* the hypotheses is an unverified floating-point assertion. You've
  kernel-checked the easy implication and left the load-bearing premise in numpy."
- **Fix:** the repo *already* does exact rep theory over `Cl(9,5)` elsewhere (MOVE-4:
  `dim Hom = 0` with exact 16384=128² checksum, errors 0.00e+00). Do the same for the
  (+96,−96) cross-chirality and K-nullity — produce the signature exactly (sympy/exact
  integers), then feed those exact values into Lean as the discharged hypotheses. Failing that,
  change the status line to "Lean-checked implication; premises computed (numpy, internal
  tier)."
- **Damage:** SERIOUS for the "machine-verified" adjective (it is the paper's proof-checker
  headline); the mathematics is correct and the disclosure exists in the Lean file.

### 6. VERIFICATION.md — the billed outsider honesty map — is stale/over-precise on flagship (c) — **MEDIUM**
- **Claim/grade:** flagship (c): "the count is forced to {1,3} and 3-primary (a class-wide
  no-go theorem)."
- **Backing:** the current paper proves *interior even/net-0; external = any integer;
  multiplicity natively 3; only computable integer 1* — not "forced to {1,3}."
- **Contest:** "Your own honesty map claims something stronger than your paper proves. Which do
  I trust?" — and the honesty map must be the *most* conservative surface.
- **Fix:** rewrite flagship (c) to "multiplicity natively 3 (a representation dimension); net
  chiral count interior-even / external-by-structure; only unconditionally computable integer
  = 1; three not derived," matching the paper's status table.
- **Damage:** MEDIUM — it is the document explicitly written so outsiders "don't have to trust
  the adjectives," so a loose line there is disproportionately costly.

### 7. The six-axis testability white paper is stale (title) and its central empirical claim is entirely unrun — **MEDIUM**
- **Claim/grade:** "candidate" (staged); a six-axis protocol with H1–H6 hypotheses and
  preregistered rejection conditions.
- **Backing:** honest as a *methods proposal* ("The next step is to run the benchmark");
  drafting note concedes it is now "seven axes + Layer-0," title/body unreconciled; H1–H6 are
  prospective with zero data.
- **Contest:** "This is a preregistration sitting in `candidates/` next to your flagship as if
  it were a result. And it advertises six axes while your own note says seven."
- **Fix:** retitle/refold to "Seven-Axis + Layer-0" (per the drafting note), and label it
  explicitly as a *protocol preregistration (methods; benchmark unrun)*, not a candidate
  result. No physics claim needs to move — just the tier/title.
- **Damage:** MEDIUM — adjacency to the flagship in `candidates/` lends it borrowed weight it
  hasn't earned yet.

### 8. The σ-cluster (the charter's centerpiece) has no consolidated, one-surface reconstruction — **COSMETIC→MEDIUM**
- **Claim/grade:** the σ-externality chain is spread across ~10 cross-referencing explorations,
  each rigorous with a probe.
- **Backing:** traceable, but only by following a citation web.
- **Contest:** "Your flagship reproduces in one command; the result your charter now leads with
  is a scavenger hunt across a dozen files. Diffuse reads as soft."
- **Fix:** write ONE σ-dossier that linearizes the chain (operator → `q<0` crossing →
  `K_S`-null → no self-adjoint realization → external Z/2 → =w₁ → Pin receptacle → protection),
  each link with its grade and its probe, ending on the single open number (ABP-exact
  `Ω^{Pin+}_14` order + operator-grade deck action). Mirror the `reproduce_all.py` pattern with
  a single `sigma_dossier_reproduce.py`.
- **Damage:** COSMETIC→MEDIUM — a findability/uncontestability gap, not a correctness gap, but
  it is the charter's load-bearing new result.

### 9. Novelty framing of the located-not-forced "inverse reading" — **COSMETIC**
- **Claim/grade:** novelty claimed only for "obstructions/selectors live in Z/8, so the
  2-primary no-go is blind to a Z/3 count"; bare `24 = 8×3` and `π₃ˢ=Z/24` conceded to Wang
  2023 / Wan-Wang-Yau 2026.
- **Backing:** best-effort literature search, negative result, narrow claim — honest.
- **Contest:** "The 'inverse reading' may be a repackaging of a known factorization."
- **Fix:** none required beyond what exists; optionally have a homotopy theorist confirm the
  inverse reading is non-obvious (folds into item 1's external sign-off).
- **Damage:** COSMETIC.

---

## Verdict — how close is the math spine to "uncontestable to a good-faith expert"?

**On mathematics and honest grading: very close — closer than almost any unaffiliated
program I would expect.** The flagship theorems kernel-check with no axioms; the lead paper's
31 load-bearing numbers reproduce from first principles with discriminating controls and a
target-import guard; the deep files carry EXACT/PROPOSAL/REFUTED ledgers, correction logs,
no-go class-relativity, kill-conditions-before-computation, and even a Lean-formalized
status-monotonicity invariant. The one prior planted-toy overclaim was **self-caught and
retracted**. At the file/grade level, essentially nothing is graded above its support — the
deep spine is, if anything, *over-hedged*.

**On surviving a reader primed to dismiss unaffiliated work: not yet — but the gap is
framing and verification-tier, not mathematics.** Three structural facts keep it contestable:
(a) the whole spine is internal-tier with **no external human check** (irreducible from
inside the process); (b) the σ-externality result and the index theorem's premises are proven
about **reconstructions / numpy stand-ins** for an **unbuilt** source action; (c) the README
charter **upgrades three deep-file grades** ("conditional prediction" → "forces,"
"reconstruction cannot close" → "result," "hosts conditionally" → "complete modulo") — the
precise "compatibility-as-derivation" moves the program's own guardrails forbid, sitting in
the first paragraph a skeptic reads.

**The 3–5 must-fix items (in priority order):**

1. **Cross the internal→external tier boundary on the smallest high-value target** — one
   named-specialist sign-off on the located-not-forced core (the ENDORSER-REQUEST draft
   exists) and/or an independent non-AI replication of `reproduce_all.py`. This is the only
   fix that raises the *ceiling*; it cannot be done from inside the process. **(Item 1.)**
2. **Sync the README charter's three words to their existing downstream grades** — "result"→
   "reconstruction cannot close (reconstruction-grade for GU's unbuilt operator)"; "forces the
   DE sign"→"derives at toy grade conditional on SRC-COH-1 + unbuilt action, non-distinctive";
   "complete modulo σ,τ"→"hosts conditionally, gated on the blocked source action." Pure
   editing; removes the cheapest self-inconsistency gotcha. **(Item 2.)**
3. **Reframe the one falsifiable as the joint rigidity surface, not the bare DE sign, in every
   public mention, and state its conditionality + non-distinctiveness inline** (as
   `blockbuster-p1` already does but the README does not). **(Item 3.)**
4. **De-bank the "exactly two external data" ledger line** — mark σ's and τ's cardinalities
   proposal-grade *in the sentence*, drop "provably" for τ, and name the single closing number
   (ABP-exact `Ω^{Pin+}_14` order + operator-grade deck action). **(Item 4.)**
5. **Fix the two honesty-surface defects** — rewrite VERIFICATION.md flagship (c) to match the
   paper ("multiplicity 3 / external count / computable integer 1," not "forced to {1,3}"), and
   change Theorem 2's "machine-verified" line to "Lean-checked implication; premises computed
   (numpy)" — or discharge the premises with the exact rep theory the repo already runs
   elsewhere. **(Items 5–6.)**

Do these five and the spine is contestable only on the one wall no editing can remove — that
no outside human has checked it yet — which is precisely the wall item 1 is built to breach.

## Boundary

Read-only audit, exploration tier. Only ONE new file was written — this document. Three
kernel/reproduction checks were *run* read-only against the existing repo (results in
frontmatter; all EXIT 0); no source, test, canon, paper, README, VERIFICATION, LANE-STATE,
or any other file was edited. No commit, no push. No claim-status, canon-verdict, paper-status,
or public-posture change; the grades and verdicts of the audited files are *consumed and
assessed*, not moved. This audit is not itself a physics result and asserts none; it is a
contestability assessment of surfaces the program already produced. Every "fix" above is a
proposal for the owner, applied to nothing.
