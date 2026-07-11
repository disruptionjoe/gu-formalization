---
title: "H18 — The Forcing Computation: does GU's action norm the full II_s or only its trace?"
artifact_type: exploration
status: exploration
updated_at: "2026-07-11"
wave: 4
condorcet_rank: 1
depends_on:
  - "tests/wave4/H18_forcing_II_vs_H.py"
  - "tests/wave3/H15_gravity_fork_R_term.py"
  - "explorations/geometry-curvature-emergence/dd1-distortion-tensor-literature-check-2026-06-22.md"
  - "explorations/geometry-curvature-emergence/ii-s-coordinate-formula-2026-06-23.md"
  - "canon/shiab-existence-cl95.md"
  - "explorations/shiab-operator/sc1-shiab-domain-codomain-2026-06-23.md"
  - "papers/drafts/Transcript into the impossible.md"
verdict: "A (II-class) strongly favored at STRUCTURAL grade; residual gate = unbuilt source action"
---

# H18 — The Forcing Computation

**Discipline.** Exploration-grade. Compute → adversarially verify → honest grade. No result
promoted to active_research/canon without the `RESEARCH-STATUS.md` criteria. The reproducible
check is `tests/wave4/H18_forcing_II_vs_H.py` (exit 0, 12/12 PASS).

---

## The question H18 settles

H15 (`tests/wave3/H15_gravity_fork_R_term.py`) reduced the whole gravity+ghost fork to **one
binary** — GU's forced section-shape action:

- **|II_s|² (II-class, FULL second fundamental form).** By the 4D Gauss identity
  `|II|² = |H|² − R^X`, this carries a *dynamical* Einstein-Hilbert `R^X` term (R is not
  topological in 4D) → gravity = **Stelle R + Weyl²** → a *distinct* massive ghost →
  Bateman-Turok Krein parity **CLEARS** it → gravity + ghost clear, DeWitt Λ for free.
- **|H_s|² (H-class, mean-curvature trace).** Pure conformal **Bach □²** → coincident double
  pole → degenerate → Bateman-Turok split singular → **ghost open** → gravity at-risk.

H15 computed *both consequences* exactly and returned **verdict C** (under-determined at the
built action, with a structural lean to A). H18's job: settle **which** GU's actual forced
structure gives — from GU's own structure, not by fiat.

## What H18 computed (test: `tests/wave4/H18_forcing_II_vs_H.py`)

**Part 1 (exact sympy). Full-norm vs trace is a real, decidable fork.** For a generic
symmetric section SFF `II_{μν}` (the object `B^V_{μν,ab}` of `ii-s-coordinate-formula` §4, a
symmetric 2-tensor with **both** spacetime indices free): `|II|²` and `|H|² = (tr II)²` differ
by exactly `−R^X` and are distinct observables — the full-norm quadratic form has **rank 10**
on `Sym²(ℝ⁴)` (sees every component, including the 9-dim traceless graviton data `|II₀|²`), the
trace-square has **rank 1**. So "does the action norm the full II or only its trace" is exactly
H15's fork, not a cosmetic relabel.

**Part 2 (exact sympy). A Yang-Mills norm-square is a FULL norm, not a trace.** The YM inner
product `⟨F,F⟩` on `Λ²(ℝ⁴)` is the full metric Gram form: **rank 6 = dim Λ²** (keeps all
curvature components); any trace-first scalar functional of `F` has a 5-dim kernel (loses 5 of
6). Weinstein is explicit that the action is this full norm-square: *"a wedge a in the
perturbative expansion of a curvature tensor … take its norm square, you get a quartic"*
([00:43:04]); the theory is *"Yang Mills plus Dirac plus Higgs"* first-order with the
second-order theory *"its square … think double copy"* ([00:05:43]). With `θ = II_s` (DD1),
the YM norm is the **full** `|II_s|²` → II-class.

**Part 3 (structural bookkeeping). The adversarial counter is refuted on the bosonic leg.**
The steelman H-class argument: Weinstein celebrates *Einstein's contraction* — the Riemann
curvature is a "2-form-valued 2-form" and Einstein *"contract[s] one index on either side of a
tensor product to get a symmetric 2-tensor"* ([00:13:44]); GU's generalization is the **shiab**
`Φ: Ω²(Y¹⁴)⊗S → Ω¹(Y¹⁴)⊗S`. A contraction is trace-like — does the action trace before norming?

H18 shows the contraction lives on the **source/fermion side, not inside the bosonic action
norm**, by two independent separations:

- **(3a) Type/degree.** The shiab is degree-**lowering** (2-form → 1-form, Δdeg = −1), the map
  that *"knock[s] it back from two forms to one forms … gives your rolled-up complex"*
  ([00:36:13]) — i.e. it builds the Dirac-DeRham-Einstein complex (the **generation/fermion**
  sector, three families). The bosonic action norm is a full `deg2 ⊗ deg2 → deg0` inner product
  (a double full contraction that **retains the whole quadratic form**, Part 2). Different maps,
  different type.
- **(3b) Clifford parity.** The shiab is **Clifford-ODD** (Clifford mult by a 1-form swaps
  chirality `Σ⁺ → Σ⁻`; `sc1-shiab-domain-codomain` §3.2/§3.6). The actual EL operator of the
  full-norm `|F|²` action is `d_A*`, which is **Clifford-EVEN**. Canon `shiab-existence-cl95.md`
  SHIAB-A: *"GU's shiab is NOT the metric codifferential d_A* — the shiab is Clifford-odd, d_A*
  is Clifford-even, so they cannot be proportional."* So Einstein's contraction (the shiab) is
  **not** the operator that varies the graviton action; it does not sit inside the action norm.

Therefore the trace-before-norm counter is **FALSE** for the bosonic/graviton sector. This is
the new result beyond H15: it removes the specific mechanism by which H-class could have been
*forced*.

**Part 4 (propositional forcing, with grades).**
`P1` (θ = full `II_s`) `∧` `P2` (action = YM full `|θ|²`) `∧` `¬C` (no trace-before-norm) `⟹`
**Branch A** (full II-class). Adversarial self-test in the test: the forcing is *conditional* —
flipping `P1`, `P2`, or establishing `C` each breaks Branch A — so H18 **settles the sign**, it
is not an unconditional proof.

**Part 5.** Re-verifies (self-contained, all dims) `|II|² = |H|² − R^X`, tying Branch A to
H15's `R^X`-carrying Stelle/ghost-clears branch.

## VERDICT: (A) II-class FORCED / STRONGLY FAVORED — at STRUCTURAL grade

| Leg | Finding | Grade |
|---|---|---|
| θ = **full** `II_s` (both indices free, not a trace) | `s*(θ) = II_s`, `II_s` a full symmetric 2-tensor | **reconstruction** — DD1 `PARTIALLY_NAMED`; `ii-s` §7 calls `s*(θ)=II_s` a *"reconstruction claim"*; literal-graph vs horizontal-normalized convention still open |
| action = YM **full** norm-square `|θ|²` (not a trace) | transcript + double-copy | **transcript** — action *type* is stated; the exact section functional is unbuilt |
| Einstein-contraction ≠ action norm (counter refuted) | shiab is Clifford-odd source/fermion map, ≠ `d_A*` | **structural** (canon SHIAB-A + degree/type) |

**Net:** H18 **upgrades** H15's "verdict C with a lean to A" to **"A strongly favored /
structurally forced modulo two reconstruction-grade premises, both of which lean A."** The one
adversarial reason to fear H-class (GU's special contraction) is defeated for the bosonic leg.

### Honest caveats — what stays gated on the unbuilt action

- **Not proof grade.** Two premises are reconstruction/transcript, not proven: **(P1)** the
  off-shell identity `s*(θ) = II_s` (full, convention-fixed), and **(P2)** that the section
  functional *literally equals* the YM `|θ|²` rather than a distinct "Willmore-type" energy that
  could re-introduce a trace. The **single missing piece is GU's source action**, which would
  upgrade P1/P2 to proofs (or falsify one).
- The "**Willmore-type energy**" naming in H15 is loose — conformal Willmore = `∫|H|²` is
  *H-class*. What pins it to the full `|II_s|²` is the YM/double-copy structure, i.e. P2; the
  pinning shares P2's grade.
- **Ghost clearance** itself (Bateman-Turok Krein parity, `m² = +1/2 > 0`) is H15 Part C/E, not
  re-derived here. **Sp(64)/Cl(9,5) rep theory**, shiab parity, and `d_A*` even/odd are taken
  from canon, not re-proved.
- **Adversarial residual on 3b:** the shiab being Clifford-odd rests on the (9,5) signature
  (`sc1` F1/SHIAB-04). Under a (7,7) alternative the chirality/parity cut changes; the
  full-norm-vs-trace argument (Parts 1–2) is signature-independent, but the specific parity
  refutation of the counter inherits the (9,5) assumption.

## RE-RANK signal

**Branch A ⟹ the GRAVITY LEG CLEARS** at the same grade as P1/P2 (structural; ghost via
H15 + Bateman-Turok). Consequences for the council ranking:

- **H16 (Stelle viability) is promoted to the natural #1.** Given A, the load-bearing check is
  now: is the induced Einstein `R^X` term the **right sign** and the ghost mass sensible **once
  the ambient DeWitt `R^Y` is included** (H15 Part E flagged this as the reconstruction-grade
  gate)?
- **The entropic / H5 route does NOT rise.** It would only rise on Branch B (H-class), which
  H18 argues against.
- **Highest-leverage next step:** turn **P1** (`s*(θ) = II_s`, off-shell, convention-fixed)
  from reconstruction into proof — the single move that converts H18's *structural* A into a
  *hard* A. This is the section-pullback / Codazzi computation `ii-s` §6.3 sets up.

**Next council reflection should focus on:** (i) H16 — close the ambient-`R^Y` sign/magnitude of
the induced Einstein term; (ii) proving P1 (the section-pullback identity `s*(θ) = II_s`).

---

*Filed 2026-07-11. Wave 4, Condorcet #1. Reproducible: `python tests/wave4/H18_forcing_II_vs_H.py`
(exit 0). Exploration-grade; not promoted to canon.*
