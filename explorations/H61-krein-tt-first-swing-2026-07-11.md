---
artifact_type: exploration
status: exploration (first big swing; 5-persona inline team; literature survey + toy extension + deterministic test)
created: 2026-07-12
hypothesis: H61
conjecture: "the source action IS the observer (CONJECTURE-source-action-is-the-observer-2026-07-11.md)"
branch: "H61 Krein Tomita-Takesaki campaign -- the observer conjecture's critical path (fan-out first swing)"
title: "H61 -- FIRST SWING on the Krein-TT campaign. TRIAGE = OPEN-BUT-HARD. The literature is thinner than 'no theorem' and richer than Branch A recorded: the modular FLOW half is a theorem (Gottschalk 2002) AND the modular CONJUGATION half is a theorem AT RANK 1 (Shulman 1997, Pi_1 quasivector Tomita theorem) -- so the conjugation is NOT known-impossible. What is genuinely MISSING: Shulman beyond rank 1 / infinite rank / type III (his quasivector method is rank-1 specific); a POSITIVE KMS state for a genuinely indefinite vacuum -- and a 2026 result (arXiv:2606.13251) sharpens this to a near-no-go: positive KMS <=> quasi-Hermiticity, i.e. the indefiniteness must be similarity-removable, which CONTRADICTS keep-and-grade; and a type-III classification of indefinite local algebras (undeveloped). Toy: J_K=C.PT EXTENDS -- the reflection-symmetry criterion [J_refl,C]=0 is RANK-STABLE (n=1,2,3, full-space rank of indefiniteness 2/8/32) and so is the positivity obstruction. KEY REFRAME: the missing positive state may be a FEATURE not a wall -- 'no distinguished state = the observer's free selection = the value' (couples to H62), so H63 should be re-founded on the algebraic flow+conjugation skeleton, not on a positive state that is provably unavailable."
grade: "exploration / honest literature survey (2026-07-12, read-only) + rank-generalized finite Krein model (tests/W74_H61_krein_tt_swing.py, 9/9, numpy-only, exit 0). The rank-stability of the J_K construction and of the positivity obstruction are PROVEN on finite type-I toys; the rank-1 Shulman theorem is verified concretely on a minimal Pi_1 witness. The type-III / rank>=2 / positive-non-positive-KMS statements are cited or named-missing, NOT proven here. No canon, RESEARCH-STATUS, CANON, claim-status, verdict, or public-posture change. The conjecture remains a conjecture; H61 remains OPEN."
depends_on:
  - explorations/CONJECTURE-source-action-is-the-observer-2026-07-11.md
  - explorations/path5-branchA-krein-modular-conjugation-2026-07-11.md
  - explorations/H62-arena-value-partition-firmup-2026-07-11.md
  - GEOMETER-VS-PHYSICS-OBJECTS.md
  - tests/W67_path5_A_krein_modular.py
scripts:
  - tests/W74_H61_krein_tt_swing.py
---

# H61 -- the Krein Tomita-Takesaki campaign, first swing (KILL-or-LEARN triage)

**Role.** H61 is the observer conjecture's **critical path**: the whole "source action = observer" rigor rests on
developing modular theory with a **non-positive separating functional** on a **type-III Krein/indefinite-metric
region algebra**, so that the Krein grading supplies a modular conjugation `J` (the firewall) and a KMS/modular
structure. Path-5 Branch A (`W67`) established the shape of the problem: the **flow** half of Tomita-Takesaki
survives a Krein space (Gottschalk 2002) but the **conjugation/positivity/KMS** half was recorded as "no theorem",
and the linear `C`-operator is the **fundamental symmetry** while the antilinear `J_K = C.PT` is the conjugation
candidate (verified on a type-I toy IFF the firewall grading is reflection-symmetric).

**This first swing decides: is H61 OPEN-AND-REACHABLE (cite the theorem), OPEN-BUT-HARD (scope the campaign), or
BLOCKED (name the obstruction)?** The honest answer, after an updated literature survey and a rank-generalized
toy, is **OPEN-BUT-HARD** -- and the survey is decisive because it changes Branch A's map in **both** directions
(the conjugation half is better off than "no theorem"; the positivity half is worse off than "no theorem").

**Artifacts:** this file + deterministic `tests/W74_H61_krein_tt_swing.py` (9/9 checks, numpy-only, exit 0). **Not
committed. Not a claim-status change.** Exploration-grade.

---

## 0. Construction forks (GEOMETER-VS-PHYSICS-OBJECTS.md discipline)

Same two load-bearing objects as Branch A; I use the same constructions and say why.
1. **"The algebra"** = the region `*`-algebra `M` represented on the **Krein space** (indefinite `[x,y]=<x,eta y>`,
   `eta` = the C-grading = fundamental symmetry), program-native, **not** a positive-Hilbert-subspace algebra.
   Forced by keep-and-grade: the physics lives in the indefinite metric.
2. **"Modular conjugation"** = the **antilinear** `J_K = C.PT` (the composite), **not** the linear `C` itself
   (that is a type error; `C` is the fundamental symmetry). This swing inherits Branch A's re-typing and does not
   re-litigate it.

The one new fork this swing surfaces: **"positive KMS state" vs "the modular skeleton"**. The standard-physics
default equates the modular structure with an *equilibrium (positive) state*. The program-native reading is that
the *value* (the distinguished state) is exactly what the observer supplies and the *arena* (the flow + the
conjugation) is what is forced. I do not default to either side; Section 5 shows the fork is the crux of the
campaign.

---

## 1. Five-persona team (inline, sequential, single context)

### Persona 1 -- operator-algebra / modular-theory specialist (the survey + the toy)

**The survey, honestly.** I searched for exactly the missing theorem: Tomita-Takesaki for indefinite-metric /
Krein / Pontryagin / PT-symmetric algebras with a non-positive separating functional, plus type-III in the
indefinite metric. What exists:

- **[FLOW] Gottschalk 2002** (`J. Math. Phys.` **43** (2002) 4753-4769; arXiv:math-ph/0408048). Dense analytic
  vectors for the boost generator in indefinite metric => `Delta^{it}` = boost / **Bisognano-Wichmann analyticity
  on Krein spaces**. This is the flow half. **THEOREM.** (Branch A had this.)
- **[CONJ] Shulman 1997** -- **the find that changes the map.** V. S. Shulman, *"Quasivectors and Tomita-Takesaki
  Theory for Operator Algebras on `Pi_1`-Spaces,"* `Reviews in Mathematical Physics` **9** (1997),
  doi:10.1142/S0129055X97000270. For a weakly-closed **J-symmetric** operator algebra with identity on a
  **Pontryagin `Pi_1`** space (**rank of indefiniteness = 1**) with a cyclic & separating vector, there is an
  **antilinear J-involution** `j` -- *a precise analogue of the Fundamental Tomita Theorem in an indefinite
  metric* -- plus a **double-commutant theorem** for such algebras. The technical device is the **quasivector**
  (a controlled substitute for the neutral/self-orthogonal vectors that the indefinite form introduces). **So the
  modular-conjugation half is NOT "no theorem": it is a THEOREM at rank 1.** Branch A's referee row "conjugation
  half has no theorem" was too strong; the honest statement is "**no theorem beyond rank 1**."
- **[KMS] 2026 sharpening** -- arXiv:2606.13251, *"Kubo-Martin-Schwinger conditions for non-Hermitian systems"*
  (2026). The **formal KMS boundary relation** can hold in non-Hermitian/indefinite settings, but **positivity of
  the (biorthogonal) thermal state is EQUIVALENT to quasi-Hermiticity of the Hamiltonian** (finite dimensions).
  I.e. a *positive* KMS state exists **iff** the indefiniteness is a **similarity artifact** (PT-unbroken /
  quasi-Hermitian). A **genuinely kept ghost** (non-quasi-Hermitian -- the whole point of keep-and-grade) admits
  **no positive KMS state**. This is the sharp, cited version of Branch A's toy-level positivity obstruction
  (`W67` T4). It also aligns with the classical passivity/KMS theory (Pusz-Woronowicz; passive <=> KMS requires a
  positive state).
- **[III] Type III** -- in the **positive metric**, wedge/local algebras are the unique **hyperfinite type
  `III_1`** factor (Bisognano-Wichmann; **Buchholz-D'Antoni-Fredenhagen**, "The universal structure of local
  algebras," `CMP` **111** (1987) 123; Fredenhagen's scaling-limit argument; "all sufficiently regular local
  algebras of a dilatation-invariant system are type III"). **No indefinite-metric / Krein type classification
  exists.** The type-III question for the region algebra is genuinely undeveloped in the Krein setting.
- **[frame] Indefinite-metric axiomatics** (Morchio-Strocchi Hilbert-space-structure condition; Strocchi's
  *Gauge theories and the physical Hilbert space*; Jakobczyk, `JMP` **25** (1984) 617) -- the natural home for a
  non-positive vacuum, but none of it proves a TT theorem for a type-III indefinite algebra.
- **[PT] pseudo-Hermitian / PT machinery** (Bender-Brody-Jones; Mostafazadeh; Bender-Mannheim Pais-Uhlenbeck) --
  finite-dimensional / QM; the `C`-operator positivity story, but no operator-algebra TT theorem.

**The toy (the extension beyond Branch A).** Branch A's toy was a single `n=1` bipartite model. I push
`J_K = SWAP.conj` (the antilinear CPT-type reflection) across `n = 1, 2, 3` ghost modes per factor, with the
reflection-symmetric Krein metric `eta_full = eta_fac (x) eta_fac`, `eta_fac = G^{(x)n}`, `G = diag(1,-1)`.
Results (all exact, `W74`):
- The **full-space rank of indefiniteness grows as `2^{2n-1}` = 2, 8, 32** -- i.e. the toy climbs *away* from
  Shulman's rank-1 theorem as `n` increases.
- For **every** `n`, `J_K^2 = 1`, `J_K M J_K = M'`, and the **Krein-antiisometry criterion holds IFF the grading
  is reflection-symmetric** (`[SWAP, eta] = 0`; residual `0` for `eta_fac (x) eta_fac`, residual `2.0` for the
  one-sided `eta_fac (x) I`). **The reflection-symmetry criterion `[J_refl, C] = 0` is RANK-STABLE** -- structural,
  not an artifact of the single-mode toy. This is the one+ data point past Branch A.
- The **positivity obstruction is also rank-stable**: at every `n` there is `A in M` with `(A(x)I)Omega` a
  negative Krein-norm vector, so the vacuum is not a positive state (residuals `-0.150, -0.075, -0.038`).
- Separately, a **minimal `Pi_1` (rank-1) witness** (`H = C^2`, `eta = diag(1,-1)`, `M` = diagonal) reproduces
  **Shulman's** conclusion concretely: the antilinear J-involution exists (`J = conj`, `Delta = I`) and is a
  Krein-antiisometry. So the cited rank-1 theorem is verified, and the gap to the toys is exactly **rank >= 2**.

### Persona 2 -- math referee (does the cited work supply what H61 needs, or only adjacent?)

| Piece H61 needs | Cited status | Grade for H61 |
|---|---|---|
| Modular **flow** `Delta^{it}` = boost on Krein | Gottschalk 2002 | **SUPPLIES IT** (theorem) |
| Modular **conjugation** `J` in an indefinite metric | Shulman 1997, **rank 1 only** | **SUPPLIES IT AT RANK 1** -- GU is `(+64,-64)` (infinite rank), a type-III region algebra is infinite rank; **adjacent, not sufficient** |
| Conjugation at **rank >= 2 / infinite rank** | none | **MISSING** (quasivector method is rank-1 specific) |
| **Positive** `Delta` / **positive KMS state** for a non-positive vacuum | arXiv:2606.13251: `<=>` quasi-Hermiticity | **NEAR-NO-GO** -- a positive KMS state requires *removing* the indefiniteness, which keep-and-grade forbids |
| **Type III_1** of the region algebra | BDF/BW in the **positive metric** only | **MISSING in the indefinite metric** (undeveloped) |

**Referee headline.** Two honest corrections to Branch A. (i) **The conjugation half is better than "no theorem":
it is a rank-1 theorem** (Shulman) -- which means the object is *not* known-impossible and the campaign has a real
foothold. (ii) **The positivity half is worse than "no theorem": it is a near-no-go** (positive KMS `<=>`
quasi-Hermiticity, arXiv:2606.13251) -- for a *genuinely* indefinite (kept) vacuum a positive KMS state does not
exist. So the campaign's difficulty is **not** uniform: extend a rank-1 theorem (hard pure math, no known
obstruction) vs. obtain a positive state (obstructed, essentially by definition of keep-and-grade). That
asymmetry is the whole strategic content of the swing.

### Persona 3 -- adversary ("this is genuinely BLOCKED: non-positive KMS does not exist and cannot")

**Attack (the strongest available, now backed by a 2026 theorem).** A modular structure whose physical content
is *thermal/equilibrium* requires a **positive** KMS state. arXiv:2606.13251 makes this sharp: positivity of the
KMS state `<=>` quasi-Hermiticity. Keep-and-grade *insists* the ghost is physical -- i.e. the metric is **not**
quasi-Hermitian-removable (if it were, there would be no ghost and no firewall). **Therefore the very thing that
makes GU's structure interesting (a genuinely kept ghost) is the very thing that forbids a positive modular/KMS
state. The TT-as-equilibrium route is blocked, not merely hard.** The toy confirms the obstruction is rank-stable
(`W74` T2): it does not soften as you approach the continuum.

**Where the adversary is forced to stop (does not veto).** The block is only a block **for the positive-state
reading**. The adversary cannot block the **flow** (Gottschalk, a theorem) nor the **conjugation** (Shulman gives
it at rank 1; nothing forbids higher rank -- the adversary has **no** no-go for rank `>= 2`, only the absence of
a theorem). And the adversary cannot show the conjecture *needs* a positive state: the conjecture's own logic
(H62; the "framework, not theory" clause) is that **there is no distinguished state -- that absence is the
observer's free selection**. So the adversary's strongest point, honestly pressed, **relocates** the obstruction:
it kills "modular structure = a positive equilibrium state," which the conjecture was **already not claiming**.
The adversary lands one durable mark -- **do not smuggle a positive KMS state into H63** -- and concedes the flow
+ conjugation skeleton is not blocked.

### Persona 4 -- cross-checker (verifies the toy + the key citations)

- **Toy (`W74`, exact, no truncation):** re-ran the `n=1,2,3` family and the `Pi_1` witness. All nine checks pass,
  exit 0. Independently sanity-checked: `[SWAP, eta_fac (x) eta_fac] = 0` for all `n` (SWAP intertwines the two
  identical factor gradings); `[SWAP, eta_fac (x) I] != 0` (residual `2.0`) -- so the criterion genuinely
  discriminates and is not vacuously true. Rank-of-indefiniteness count `2^{2n-1}` verified by eigenvalue sign
  count, not asserted.
- **Citations:** Gottschalk 2002 confirmed (JMP 43, 4753; arXiv:math-ph/0408048 -- BW on Krein via complex
  velocity transformations). Shulman 1997 confirmed (Rev. Math. Phys. 9; `Pi_1`; antilinear J-involution + double
  commutant; quasivectors; the **rank-1** restriction is explicit and load-bearing in the abstract). BDF type
  `III_1` confirmed (CMP 111 (1987) 123, universal structure). The 2026 KMS result confirmed as a finite-dim
  *positivity `<=>` quasi-Hermiticity* statement (formal KMS can hold without positivity). **Honest caveat on the
  2026 paper:** it is finite-dimensional and recent; I use it as a *sharpening/indicator* of the positivity
  obstruction, not as a proven type-III no-go. That distinction is preserved in the grade.
- **One correction to my own prior:** the `Pi_1` witness has `Delta = I` because `M` is abelian-maximal; it is a
  valid but *degenerate* modular structure. It confirms *existence* of the antilinear J in an indefinite metric,
  **not** a nontrivial modular flow. I do not overstate it.

### Persona 5 -- synthesizer (triage verdict)

See Sections 2-5.

---

## 2. TRIAGE VERDICT: **OPEN-BUT-HARD** (with a sharpened, asymmetric campaign scope)

Not **OPEN-AND-REACHABLE**: no citable theorem covers the conjugation beyond rank 1, the type-III classification
of indefinite local algebras, or a positive modular structure for a non-positive vacuum. You cannot "cite the
theorem."

Not **BLOCKED**: the modular **flow** is a theorem (Gottschalk), the modular **conjugation** is a theorem **at
rank 1** (Shulman) -- so the load-bearing object is **not known-impossible** -- and the one genuine near-no-go
(positive KMS `<=>` quasi-Hermiticity) bites only the **positive-state** reading, which the conjecture does not
require (it may even be a *feature*; Section 5).

**OPEN-BUT-HARD**, and the campaign is now scoped along a **fault line Branch A did not see**: the two missing
pieces have **different characters**.

---

## 3. What the literature SUPPLIES vs what is MISSING (the campaign scope)

**Supplied now (citable / constructible):**
1. Modular **flow** `Delta^{it}` = boost, BW analyticity on Krein -- **Gottschalk 2002**.
2. Modular **conjugation** (antilinear J-involution) in an indefinite metric **at rank of indefiniteness 1** --
   **Shulman 1997** (`Pi_1`, quasivectors, + double commutant). Verified concretely (`W74` T3).
3. `C` = fundamental symmetry `eta`; the antilinear `J_K = C.PT` on a **type-I** toy satisfies all three algebraic
   axioms **IFF `[J_refl, C] = 0`** (reflection-symmetric firewall grading) -- and this criterion is now
   **rank-stable** (`W74` T1).
4. Positive-metric local algebras are hyperfinite **type `III_1`** -- BW + **Buchholz-D'Antoni-Fredenhagen** --
   the *target* type, established on the positive side.

**Missing (needs new mathematics; named precisely):**
1. **Shulman beyond rank 1.** Extend the `Pi_1` quasivector Tomita theorem to **`Pi_kappa` (rank `kappa >= 2`),
   infinite rank, and type III**. GU's `(+64,-64)` metric and a type-III region algebra are **infinite rank**, so
   rank-1 is not enough. **No known obstruction** -- this is hard pure operator theory, the *primary* campaign
   target. (The toy shows the *construction* survives to any finite rank in the type-I case; the missing content
   is the *theorem* at infinite rank + type III, and the quasivector control of neutral vectors when there are
   infinitely many.)
2. **A positive modular structure for a non-positive vacuum -- near-no-go.** arXiv:2606.13251: positive KMS `<=>`
   quasi-Hermiticity. For a genuinely kept ghost this **does not exist**. **Campaign decision (Section 5): do not
   try to build a positive state; re-found the payoff on the algebraic flow+conjugation skeleton.**
3. **Type `III_1` of the indefinite-metric region algebra.** BW/firewall needs it; no finite model decides it
   (`W67` T6); the Krein-space type classification is undeveloped. Open.

---

## 4. Type III status (Task 3 -- honest, partial)

- **Positive metric:** local/wedge algebras are the unique hyperfinite **`III_1`** factor -- Bisognano-Wichmann
  (modular flow = boost forces `III_1`), Buchholz-D'Antoni-Fredenhagen (universal structure), Fredenhagen
  (nontrivial scaling limit `=>` `III_1`), and the general "dilatation-invariant local systems are type III". So
  the **target** type is exactly right and well-established -- **on the positive side**.
- **Indefinite metric:** **no type classification exists.** A finite toy is type I (`W67` T6: it has a trace and
  minimal projections), so no finite computation decides it. The obstruction to answering in one swing is
  structural: type `III_1`-ness is a **continuum** property (it comes from the scaling limit / the absence of a
  trace), and the very device that proves it in the positive metric (the modular flow's spectrum, KMS at the
  Reeh-Schlieder vacuum) is **exactly the positive-state apparatus that fails in the indefinite metric**. So the
  type-III question is **entangled with missing-piece 2**: to run the BDF/Fredenhagen argument in the Krein
  setting you would first need the modular/KMS structure that arXiv:2606.13251 says has no positive-state form.
  **Status: OPEN; the obstruction is that the standard type-III proofs are built on the positive KMS structure the
  indefinite metric lacks.** A plausible route (unverified): argue type III from the *algebraic* modular flow +
  Gottschalk analyticity + a Krein Reeh-Schlieder, bypassing the positive state -- same reframe as Section 5.

---

## 5. The key reframe (couples H61 to H62) -- the positivity wall may be a FEATURE

The one genuine near-no-go is: **no positive KMS/equilibrium state for a genuinely indefinite vacuum**. Branch A
filed this as *the* load-bearing gap. This swing's central *learning* is that it may not be a gap at all:

- **H62 (firmed, `W73`) says:** ARENA = symmetry-**invariant** (forced); VALUE = requires symmetry-**breaking**
  (the observer's selection). The **modular conjugation `J_K` and the modular flow are symmetry data** (fixed by
  `eta`, by the reflection `SWAP`, by the boost generator) -- **arena**. A **distinguished positive state** is
  precisely a choice of vacuum/frame -- **symmetry-breaking = value**. And arXiv:2606.13251 says a positive KMS
  state exists **iff** you *break* the genuine indefiniteness (quasi-Hermiticity) -- i.e. the positive state is
  *literally* the symmetry-broken datum.
- **Therefore the absence of a distinguished positive state is not a failure of the modular skeleton; it IS the
  observer's free selection -- the value.** This is exactly the conjecture's "framework, not theory becomes a
  necessity" clause (CONJECTURE Sec 3) and H62's arena/value split, now meeting the operator-algebra facts.
- **Consequence for the campaign / H63.** Do **not** attempt to construct a positive KMS state (provably
  unavailable for a kept ghost, and *wanted* to be unavailable). **Re-found H63 on the algebraic modular skeleton**
  -- the flow (Gottschalk), the conjugation (Shulman-type, extended), and the *algebraic* KMS relation (metric-
  independent, `W67` T5) -- with the **missing positive state as the residual free selection the Lawvere no-closure
  argument already needs**. The firewall's `J_K^2 = 1` flip (H63's lemma L2) lives in the conjugation skeleton, not
  in a state. If H63 can be stated this way, the positivity near-no-go stops being an obstruction and becomes the
  *mechanism*.

**H62 confirmation (Task 4).** The arena/value split is non-circular via the **symmetry** characterization, and
Krein-TT targets genuinely symmetry-invariant structure (`J_K`, the flow), **not** a tautology. Verified as a
structural assertion (`W74` T4): the arena is `{J_K, flow, algebraic KMS}` (all symmetry-fixed), the value is
`{the positive state}` (symmetry-broken, and provably so via quasi-Hermiticity). **The framing holds.**

---

## 6. Campaign scope if reachable (concrete next swings, ranked)

1. **Extend Shulman `Pi_1` -> `Pi_kappa` / infinite rank.** The primary pure-math target. Sub-goal: identify
   whether the quasivector construction has a rank-`kappa` analogue, or a genuine rank obstruction at `kappa = 2`.
   The searches suggest rank `>= 2` is *open* (no theorem either way), so a rank-2 case study is the sharpest next
   probe -- either it extends (campaign reachable) or it hits a first real obstruction (campaign narrows to a
   no-go). *A finite rank-2 non-abelian Krein toy with nontrivial `Delta` is the natural next test file.*
2. **Re-found H63 on the algebraic skeleton (no positive state).** State the Lawvere no-closure lemma using only
   the flow + conjugation + algebraic KMS, with the positive state as the residual selection. This is the
   highest-value swing: it converts the positivity near-no-go from wall to mechanism and is *independent* of the
   pure-math extension (1). If it works, H61's "load-bearing gap" downgrades to "the value, by design."
3. **Type III via the algebraic route.** Attempt BDF/Fredenhagen-style type-`III_1` for the indefinite region
   algebra using the *algebraic* modular flow + Gottschalk analyticity + a Krein Reeh-Schlieder, bypassing the
   positive KMS state. Hardest; depends on (1).

---

## 7. Confidence grade and what would move it

- **Rank-stability of the `J_K` construction and the reflection-symmetry criterion** (`W74` T1): **high** (exact,
  `n=1,2,3`).
- **Rank-stability of the positivity obstruction** (`W74` T2): **high** (exact).
- **Shulman rank-1 theorem supplies the conjugation** (T3 + citation): **high** for rank 1; the rank-1 witness is
  degenerate (`Delta=I`) so it confirms *existence*, not a nontrivial flow.
- **Positive KMS `<=>` quasi-Hermiticity as the positivity obstruction** (arXiv:2606.13251): **medium-high** --
  cited, finite-dimensional, recent; used as a sharpening/indicator, not a proven type-III no-go.
- **Triage = OPEN-BUT-HARD:** **medium-high.** The upgrade over Branch A (conjugation is a rank-1 theorem, not
  "no theorem"; positivity is a near-no-go, not "no theorem") rests on two specific citations that a specialist
  should read in full (Shulman's rank-1 restriction; the 2026 KMS paper's scope).
- **The key reframe (positivity wall = the value)**: **medium** -- it is a *plausible and well-motivated*
  re-founding (it matches H62 and the conjecture's own logic), but H63-on-the-algebraic-skeleton is **not yet
  written**; until it is, "feature not wall" is a strong hypothesis, not a result.

**What would move it most:** (a) a **rank-2** Krein modular-conjugation case study (extends Shulman => reachable;
obstructs => a first real no-go); (b) an **algebraic-skeleton statement of H63** that never invokes a positive
state (would convert the near-no-go into the mechanism); (c) a specialist reading of Shulman confirming the
quasivector method's exact rank dependence.

---

## 8. What this does NOT do

No GU claim-status, `CANON.md`, `RESEARCH-STATUS.md`, verdict, or public-posture change. No external action; all
citations are read-only literature. The conjecture remains a conjecture; H61 remains **OPEN** (now graded
OPEN-BUT-HARD with a scoped campaign). The deliverable is a corrected literature map (conjugation = rank-1
theorem; positivity = near-no-go, not silence), one+ toy data point past Branch A (rank-stability of both the
`J_K` construction and the obstruction), an honest type-III status, and a strategic reframe coupling the
positivity wall to H62's arena/value split. Reproducible: `tests/W74_H61_krein_tt_swing.py` (9/9, exit 0).
