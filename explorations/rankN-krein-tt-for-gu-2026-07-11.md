---
artifact_type: exploration
status: exploration (directed swing; 5-persona inline team; the composition-closure test W77 x W83; literature check + deterministic toy)
created: 2026-07-12
hypothesis: H61 / H61a (the observer-conjecture Krein-TT critical path)
conjecture: "the source action IS the observer (CONJECTURE-source-action-is-the-observer-2026-07-11.md)"
branch: "rankN -- does PT-unbrokenness (W83) SUFFICE to extend the Krein modular conjugation to GU's genuinely-indefinite, infinite-rank, type-III region algebra (W77's IFF), or is there a RESIDUAL type-III obstruction BEYOND PT-unbrokenness?"
title: "rankN Krein-TT for GU. VERDICT = RESIDUAL TYPE-III OBSTRUCTION (with the SUBTLE removable-ghost horn named). The naive composition -- W77 (rank>1 Krein-TT extends IFF Delta=S^+S is modular-PT-unbroken) x W83 (the AS branch IS PT-unbroken on the physical sector) -- does NOT close. PT-unbrokenness is the claim that Delta has real-positive spectrum; 'standard Tomita-Takesaki then applies' would require the indefinite algebra to be QUASI-HERMITIAN, i.e. to admit a metric operator that is BOUNDED WITH BOUNDED INVERSE (a bounded similarity to a positive-metric/self-adjoint algebra). The decisive fact: PT-unbroken => quasi-Hermitian holds at FINITE rank (every bounded operator on a Pontryagin Pi_kappa space is DEFINITIZABLE, Langer; a diagonalizable real-spectrum operator is boundedly similar to a self-adjoint one, Mostafazadeh) -- and there the ghost is REMOVABLE, so keep-and-grade is trivial. At INFINITE rank / type III (GU's actual region algebra) the implication FAILS: real-positive spectrum (complete eigenvectors, not a Riesz basis) admits only a bounded metric with UNBOUNDED INVERSE (Krejcirik-Siegl 2012, the imaginary cubic oscillator: NOT similar to self-adjoint, only QUASI-similar), and general self-adjoint operators on infinite-rank Krein spaces are NOT definitizable, so there is NO spectral function, NO eta-positive square root of Delta, and hence NO modular conjugation J from real-positive spectrum alone. So PT-unbrokenness is NECESSARY but NOT SUFFICIENT at type III. The residual condition -- UNIFORM boundedness of the metric across the mode tower / definitizability -- is INDEPENDENT of AS-selection, so the two named conditions do NOT collapse to one ('only Reuter-FP-genuine remains' is FALSE). The removability dichotomy (arXiv:2606.13251, positive-KMS <=> quasi-Hermiticity, which contradicts keep-and-grade) is reconciled as a genuine XOR: HORN Q (quasi-Hermitian => standard TT closes BUT the ghost is removable, keep-and-grade trivial -- a DIFFERENT important conclusion) vs HORN K (genuine kept ghost => keep-and-grade nontrivial BUT standard TT does NOT apply, the infinite-rank Krein conjugation theorem is genuinely needed and does not exist). A repo-native indication places GU on HORN K: W52/R1 give ||C|| -> infinity approaching the exceptional (Jordan) locus, and W53 places that locus (m2^2 -> 0) at the free UV fixed point the AS trajectory approaches, so the metric conditioning plausibly DEGRADES in the UV -> inverse metric plausibly unbounded -> genuine ghost, obstruction stands, NOT removable. Indication, not proof."
grade: "exploration / two independent derivations that AGREE (D1 functional-analytic: definitizability/spectral-function for eta-selfadjoint operators is a finite-rank/Pontryagin phenomenon, so real-positive spectrum at infinite rank does not yield an eta-positive square root -> no J; D2 quasi-Hermiticity dichotomy: positive-KMS <=> bounded-invertible metric, which either removes the ghost or fails to exist). Deterministic tests/W84_rankN_krein_tt.py (5/5, numpy-only, exit 0) + literature check (2026-07-12, read-only: Krejcirik-Siegl PRD 86 (2012) 121702 [bounded metric, unbounded inverse]; Langer definitizable-operator theory [Pi_kappa definitizable, general Krein-selfadjoint not]; arXiv:2606.13251 [positive-KMS <=> quasi-Hermiticity]; Shulman Pi_1). The finite-rank collapse (T1), the infinite-rank failure of the implication (T2, Krejcirik-Siegl surrogate), the independence of the closure condition from PT-unbrokenness (T3), and the removability XOR (T4) are PROVEN on the toy; the claim that GU's region algebra sits on HORN K is an INDICATION (W52/R1 + W53), not proven. No canon, RESEARCH-STATUS, CANON, claim-status, verdict, or public-posture change. The conjecture remains a conjecture; H61/H61a remain OPEN (now with the residual sharpened: PT-unbroken is necessary but not sufficient; the residual is uniform-metric/definitizability)."
depends_on:
  - explorations/H61a-rank2-krein-tomita-case-study-2026-07-11.md
  - explorations/H61a-rank2-verdict-and-convergence-2026-07-11.md
  - explorations/H61-krein-tt-first-swing-2026-07-11.md
  - explorations/frg-fr-weyl-af-as-fork-2026-07-11.md
  - explorations/path2-branchB-pt-c-operator-2026-07-11.md
  - explorations/path2-branchE-nogo-2026-07-11.md
  - explorations/CONJECTURE-source-action-is-the-observer-2026-07-11.md
  - GEOMETER-VS-PHYSICS-OBJECTS.md
  - tests/W77_H61a_rank2_krein_tomita.py
  - tests/W83_frg_fr_weyl_af_as.py
  - tests/W74_H61_krein_tt_swing.py
  - tests/W52_path2_E_nogo.py
scripts:
  - tests/W84_rankN_krein_tt.py
external_refs:
  - "D. Krejcirik & P. Siegl, On the metric operator for the imaginary cubic oscillator, Phys. Rev. D 86 (2012) 121702(R), arXiv:1208.1866 -- bounded metric with UNBOUNDED INVERSE; eigenvectors complete but not a Riesz basis; NOT similar to self-adjoint, only quasi-similar"
  - "J.-P. Antoine & C. Trapani; F. Bagarello et al., Non-Selfadjoint Operators in Quantum Physics (Wiley 2015) -- quasi-Hermiticity requires a bounded boundedly-invertible metric; else 'similarity' weakens to 'quasi-similarity'"
  - "H. Langer, Spectral functions of definitizable operators in Krein spaces -- spectral theorem under definitizability; in Pontryagin Pi_kappa every bounded operator is definitizable; no such theorem for general self-adjoint operators on infinite-rank Krein spaces"
  - "A. Mostafazadeh, pseudo-Hermitian QM -- finite-dim: diagonalizable + real spectrum <=> quasi-Hermitian (a positive-definite metric exists)"
  - "arXiv:2606.13251, KMS conditions for non-Hermitian systems -- positivity of the biorthogonal thermal state <=> quasi-Hermiticity"
  - "V. S. Shulman, Rev. Math. Phys. 9 (1997) 749 -- the rank-1 quasivector Tomita theorem; no Pi_kappa (kappa>=2) conjugation theorem exists"
---

# rankN -- does PT-unbrokenness close the rank>1 Krein Tomita-Takesaki for GU?

**Role.** This swing tests the single composition the observer conjecture's critical path now hangs on.
`W77`/H61a proved a fork: the Krein modular skeleton (`J^2=1`, `JMJ=M'`, the `eta`-positive polar
decomposition `S = J Delta^{1/2}`, the `eta`-unitary flow) extends past Shulman's rank-1 theorem **iff**
the Krein modular operator `Delta = S^+ S` is **modular-PT-unbroken** (real-positive spectrum). `W83`
argued that on GU's selected **asymptotic-safety** branch the modular/grading spectrum **is PT-unbroken**
on the physical (spin-2) sector. The naive composition reads:

> PT-unbroken (`W83`) `=>` rank>1 Krein-TT closes (`W77`) `=>` the observer conjecture's two named
> conditions collapse to one (only "the Reuter FP is genuine" remains).

**This swing's answer: the composition does NOT close. VERDICT = RESIDUAL TYPE-III OBSTRUCTION.**
PT-unbrokenness is **necessary but not sufficient** at infinite rank / type III, because *PT-unbroken does
not imply quasi-Hermitian there* -- and quasi-Hermiticity (a bounded, boundedly-invertible metric) is
exactly what "standard Tomita-Takesaki then applies" requires. The residual condition is an **independent**
one (uniform-metric/definitizability), so the two named conditions do **not** collapse. The subtle
alternative -- that PT-unbroken *does* give quasi-Hermiticity and hence a **removable** ghost -- is named
as HORN Q and is a different, still-important conclusion; a repo-native indication places GU on the
genuine-ghost HORN K instead.

**Artifacts:** this file + deterministic `tests/W84_rankN_krein_tt.py` (5/5, numpy-only, exit 0).
**Not committed. Not a claim-status change.** Exploration-grade.

---

## 0. Construction forks (GEOMETER-VS-PHYSICS-OBJECTS.md discipline)

| Object | Construction used | Load-bearing here |
|---|---|---|
| **The algebra** | GU-native indefinite region `*`-algebra on the **Krein space** `[x,y]=<x,eta y>`, `eta` = the C-grading = fundamental symmetry, **infinite** rank of indefiniteness (GU is `(+64,-64)` per point, a QFT region algebra has infinitely many modes) | GU's regime is a **genuine Krein space**, NOT a Pontryagin `Pi_kappa` (finite `kappa`). Langer's finite-rank levers do NOT transfer. |
| **The modular operator** | the **Krein** `Delta = S^+ S`, `S(aOmega)=a^+Omega`, `a^+=eta a* eta` -- the object `W77` isolated, not the Hilbert `Delta` of `W67`/`W74` | Its *spectrum* decides `W77`'s fork; its *definitizability* decides this swing's. |
| **The reduction claim** | "**standard TT applies**" = the algebra is **quasi-Hermitian**: a metric `Theta` **bounded with bounded inverse**, `h = Theta^{1/2} H Theta^{-1/2}` self-adjoint | This is the precise content of "PT-unbroken => quasi-Hermitian => standard TT". The whole swing turns on whether real-positive spectrum delivers a *bounded-invertible* `Theta` at infinite rank. |

The one new fork surfaced: **"PT-unbroken" vs "quasi-Hermitian."** In finite dimensions these coincide;
at infinite rank they come apart, and that gap is the swing's result.

---

## 1. Five-persona team (inline, sequential, single context)

### Persona 1 -- operator-algebra / modular-theory specialist (what closure actually requires)

`W77`'s IFF is stated on the **spectrum** of `Delta` (real & positive). But the deliverable of Tomita-Takesaki
is the **modular conjugation** `J`, obtained from the **`eta`-positive square root** `Delta^{1/2}` in the
polar decomposition `S = J Delta^{1/2}`. Building `Delta^{1/2}` needs a **functional calculus** for the
`eta`-selfadjoint `Delta` -- a **spectral function**. Two ways to have it:

1. **The definitizable / Pontryagin route (Langer).** If `Delta` is *definitizable* -- in particular on a
   Pontryagin `Pi_kappa` space (finite rank), where **every bounded operator is definitizable** -- Langer's
   spectral theorem supplies a spectral function, hence an `eta`-positive `Delta^{1/2}`, hence `J`. This is
   exactly why the rank-1 theorem exists (Shulman's single quasivector patches the `<=1`-dimensional defect)
   and why `W77` got a clean rank-2 witness in the unbroken interior.
2. **The quasi-Hermitian route (Dieudonne / Scholtz-Geyer-Hahne).** If the algebra is *quasi-Hermitian* -- a
   metric `Theta` **bounded with bounded inverse** intertwines `H` and `H^dag` -- then `h=Theta^{1/2}H Theta^{-1/2}`
   is a genuine self-adjoint operator on a positive Hilbert space, **standard Tomita-Takesaki holds at any
   type (including III_1)**, and one transports `J`, `Delta` back by the bounded similarity. This is the
   clean way "standard TT applies once PT-unbroken" *could* be true.

**The specialist's finding:** at **finite rank** both routes are available from PT-unbrokenness, and they
**agree** -- a diagonalizable real-spectrum operator in finite dimensions is quasi-Hermitian (a
positive-definite metric exists, Mostafazadeh) and every `Pi_kappa` operator is definitizable. **So finite
reasoning genuinely suggests the composition closes.** (Verified exactly, `W84` T1: a PT-unbroken mode is
quasi-Hermitian, `h` is exactly Hermitian, standard TT applies -- and the ghost is thereby *removable*.)

**But at infinite rank / type III both routes fail from real-positive spectrum alone**, and that is GU's
regime.

### Persona 2 -- MATH REFEREE (does PT-unbroken give quasi-Hermitian at type III? is the ghost removable or not?)

**Ruling 1 -- PT-unbroken does NOT imply quasi-Hermitian at infinite rank.** The counterexample is a
theorem, not a worry: **Krejcirik-Siegl (PRD 86 (2012) 121702)** show the PT-symmetric **imaginary cubic
oscillator** has a *real spectrum* and a *complete* set of eigenvectors that is **not a Riesz basis**;
consequently its metric operator `Theta` is **bounded but has an UNBOUNDED INVERSE**. Such an `H` is **not
similar to a self-adjoint operator** -- only **quasi-similar** -- so it is **not quasi-Hermitian** in the
sense that makes standard TT apply. Real-positive spectrum (PT-unbroken) is therefore *strictly weaker* than
quasi-Hermitian in infinite dimensions.

**Ruling 2 -- and there is no spectral-function fallback.** By **Langer**, a spectral function for an
`eta`-selfadjoint operator on a Krein space exists **under definitizability**; **on `Pi_kappa` (finite rank)
every bounded operator is definitizable**, but for **general self-adjoint operators on infinite-rank Krein
spaces there is no such theorem**. So at GU's infinite rank, real-positive spectrum yields **neither** a
bounded-invertible metric **nor** an `eta`-positive `Delta^{1/2}`: the modular conjugation `J` is **not
constructible from PT-unbrokenness alone**. Langer's `Pi_kappa` machinery -- the exact lever behind Shulman
rank-1 and `W77` -- is **finite-rank-specific** and does not extend to infinite `kappa`.

**Ruling 3 -- is the ghost removable?** This is a genuine XOR, resolved by *which* metric obtains
(Ruling 1's two cases), and it is the reconciliation of arXiv:2606.13251:
- **HORN Q (metric bounded with bounded inverse = quasi-Hermitian):** standard TT closes, but the bounded
  similarity `Theta^{1/2}` maps the indefinite algebra to a **positive-metric** one -- the ghost is
  **removable**, and **keep-and-grade is trivial** (the "ghost" was a bounded-similarity artifact). This is
  arXiv:2606.13251's "positive-KMS `<=>` quasi-Hermiticity" and its "contradicts keep-and-grade."
- **HORN K (metric bounded, inverse UNBOUNDED = genuinely indefinite):** the ghost is **not removable**
  (only quasi-similar), keep-and-grade is **nontrivial** -- **but** the theory is not quasi-Hermitian,
  standard TT does **not** apply, and one is thrown back on the **non-existent** infinite-rank Krein
  conjugation theorem.

**Referee headline.** Neither horn yields "PT-unbroken `=>` a *genuine kept-ghost* rank>1 Krein-TT closes."
Either the ghost is removable (and the interesting structure evaporates) or the obstruction survives. The
referee refuses "RANK>1 CLOSES."

### Persona 3 -- ADVERSARY (both directions)

- *Against RESIDUAL OBSTRUCTION ("PT-unbroken is enough; you are importing an infinite-dim pathology GU
  need not have").* Pressed honestly: the adversary must claim GU's tower is **uniformly** PT-unbroken (a
  spectral gap bounded away from the exceptional locus across all modes), which upgrades PT-unbrokenness to
  quasi-Hermiticity. **Conceded as logically possible -- and named HORN Q.** But then the adversary has
  *removed the ghost*: keep-and-grade is trivial and the AS-branch theory is secretly positive-metric. So
  this attack does not save "RANK>1 CLOSES with a genuine ghost"; it converts the outcome to
  SUBTLE-removable-ghost. And it is **unestablished**: uniform boundedness across the UV tower is exactly
  what `W52`/R1 (`||C|| -> infinity` near the exceptional locus) and `W53` (the locus sits at the free UV FP
  the AS flow approaches) give a **positive indication against**.
- *Against SUBTLE-removable ("keep-and-grade would be trivial, so the ghost must be removable, so TT
  closes").* Answered: removability requires the *uniform* / bounded-inverse metric, which the same
  `W52`/`W53` indication argues **fails** in the UV. A bounded metric with unbounded inverse (Krejcirik-Siegl)
  keeps the ghost genuinely (only quasi-similar) -- keep-and-grade stays nontrivial -- **and** blocks
  standard TT. So the generic type-III expectation is HORN K, not HORN Q.

The adversary's two pushes are mutually defeating: one removes the ghost, the other keeps it but keeps the
obstruction. Neither delivers a clean collapse.

### Persona 4 -- CROSS-CHECKER (the quasi-Hermiticity literature + a toy)

**Literature (2026-07-12, read-only).**
- **Krejcirik-Siegl (PRD 86 (2012) 121702, arXiv:1208.1866):** confirmed -- bounded metric, **unbounded
  inverse**, eigenvectors complete but **not a Riesz basis**, `H` **not similar** (only quasi-similar) to a
  self-adjoint operator. The canonical infinite-dim PT-unbroken-but-not-quasi-Hermitian example.
- **Antoine-Trapani / Bagarello et al. (Non-Selfadjoint Operators in Quantum Physics, Wiley 2015):**
  confirmed -- quasi-Hermiticity is defined by a **bounded boundedly-invertible** metric; when the inverse is
  unbounded, "similarity" must be weakened to "quasi-similarity" and the self-adjoint equivalence is lost.
- **Langer:** confirmed -- spectral function under **definitizability**; **`Pi_kappa` (finite) definitizable**;
  no spectral theorem for **general** self-adjoint operators on infinite-rank Krein spaces.
- **arXiv:2606.13251:** positive (biorthogonal) thermal state `<=>` quasi-Hermiticity -- the HORN Q/HORN K
  dichotomy in physics form.

**Toy (`W84`, exact, numpy-only).** Reuse the repo's own exceptional-point model (`W52`) **mode by mode**:
`H_k = [[i a_k, b_k],[b_k, -i a_k]]`, ratio `r_k=a_k/b_k`, **PT-unbroken iff `r_k<1`**, positive metric
`eta_k=[[1,-i r_k],[i r_k,1]]` with eigenvalues `1 -+ r_k` and condition number `(1+r_k)/(1-r_k)`.
- **T1 -- the finite-rank collapse is REAL:** a PT-unbroken mode is quasi-Hermitian; `eta_k` is
  bounded-invertible (cond `3.0` at `r=0.5`); `h=eta^{1/2}Heta^{-1/2}` is exactly Hermitian (resid `1e-16`)
  -> standard TT via bounded similarity -> **ghost removable**.
- **T2 -- the implication FAILS at infinite rank:** a mode **tower** with `r_k -> 1` (the UV approach to the
  exceptional locus, `W53`: `m2^2 -> 0` at the free UV FP) has **every mode PT-unbroken** yet drives
  `min eig(metric) -> 0`, `sup cond -> infinity`, and `||Theta^{-1}||` **grows without bound** (doubles when
  the tower doubles). So real-positive spectrum does **not** give a bounded-invertible metric -- the finite
  surrogate of Krejcirik-Siegl's Riesz-basis failure.
- **T3 -- the two conditions do NOT collapse:** two towers, **both** mode-wise PT-unbroken -- a **uniform**
  one (`r_k=0.5`, sup cond bounded, TT closes) and a **non-uniform** one (`r_k->1`, sup cond unbounded, TT
  does not close). PT-unbrokenness alone does not decide between them; closure is controlled by **uniform
  boundedness / definitizability**, an **independent** condition. (Bounded-vs-unbounded detected by growth
  under tower-doubling, not an arbitrary threshold.)
- **T4 -- removability XOR:** HORN Q (uniform) Hermitizes every mode by a bounded similarity -> ghost
  removable; HORN K (non-uniform) has Hermitizing norm growing without bound -> ghost **not** removable but
  standard TT does not apply. Never both.

Two independent derivations (**D1** definitizability/functional-analytic; **D2** quasi-Hermiticity
dichotomy) **agree**: PT-unbroken alone does not close rank>1 Krein-TT at type III, and the residual is the
uniform-metric/definitizability condition.

### Persona 5 -- SYNTHESIZER (the verdict)

See Sections 2-4.

---

## 2. VERDICT: RESIDUAL TYPE-III OBSTRUCTION (the composition does not close)

**PT-unbrokenness (real-positive `Delta`) is NECESSARY but NOT SUFFICIENT for rank>1 Krein-TT on GU's
genuinely-indefinite, infinite-rank, type-III region algebra.**

- At **finite rank** the composition genuinely appears to close: PT-unbroken `=>` quasi-Hermitian `=>`
  standard TT (via a bounded similarity), because every `Pi_kappa` operator is definitizable and a
  real-spectrum diagonalizable operator is quasi-Hermitian. **But at finite rank the ghost is *removable*,
  so this "closure" trivializes keep-and-grade.**
- At **infinite rank / type III** the implication **fails**: real-positive spectrum admits only a bounded
  metric with **unbounded inverse** (Krejcirik-Siegl), i.e. **quasi-similar, not similar**, to a self-adjoint
  algebra; and general Krein-selfadjoint operators are **not definitizable** (Langer), so there is **no
  `eta`-positive `Delta^{1/2}`** and **no `J`** from PT-unbrokenness alone. Langer's `Pi_kappa` method (behind
  Shulman rank-1 and `W77`) is finite-rank-specific.

**The residual, named:** **uniform boundedness of the metric operator across the mode tower / definitizability
of `Delta` at infinite rank.** This is a *different* condition from mode-wise PT-unbrokenness, and it is **not
supplied by AS-selection**. It is exactly the infinite-rank Krein Tomita conjugation theorem that does not
exist -- "type III_1 is a further step," made precise as the failure of the finite-rank
PT-unbroken `=>` quasi-Hermitian implication.

---

## 3. The two questions the orchestrator asked, answered

**(a) Does PT-unbroken imply quasi-Hermitian at type III?** **No.** True in finite dimensions (Mostafazadeh;
`Pi_kappa` definitizable, Langer). **False at infinite rank** -- Krejcirik-Siegl exhibit a PT-unbroken
(real-spectrum) operator whose metric has an unbounded inverse, hence not similar (only quasi-similar) to a
self-adjoint operator. GU's region algebra is infinite rank, so the finite-dim equivalence cannot be assumed.

**(b) Do the two named conditions collapse to one (only Reuter-FP-genuine)?** **No.** Closure requires the
**independent** uniform-metric/definitizability condition on top of PT-unbrokenness (`W84` T3: two mode-wise
PT-unbroken towers, one closes and one does not). The AS-selection that closes the scalaron (W83 condition ii)
does **not** thereby close the Krein-TT leg. Both the Reuter-FP-genuine condition **and** the
infinite-rank/definitizability condition remain.

**(c) If quasi-Hermitian, is the AS-branch ghost removable (changing the picture)?** **Yes -- that is HORN Q,
and it *would* change the picture** (the AS-branch "ghost" would be secretly positive-metric, keep-and-grade
unnecessary). But the repo-native evidence points to **HORN K** (genuine, non-removable ghost): `W52`/R1 give
`||C|| -> infinity` approaching the exceptional (Jordan) locus, and `W53` places that locus (`m2^2 -> 0`) at
the free UV fixed point the AS trajectory approaches -- so the metric conditioning plausibly **degrades in the
UV**, the inverse metric is plausibly unbounded, the ghost is genuinely kept, and standard TT does not apply.
**Indication, not proof.**

**A structural note (the beautiful tension).** The very fact that keeps keep-and-grade nontrivial -- a
genuine, non-removable ghost (metric inverse unbounded) -- is the *same* fact that prevents PT-unbrokenness
from closing the Krein-TT (no bounded similarity, no quasi-Hermitian reduction, definitizability genuinely
needed). Conversely, the only way PT-unbrokenness closes TT (HORN Q, uniform metric) is the way that removes
the ghost. This is arXiv:2606.13251's "quasi-Hermiticity contradicts keep-and-grade," now located precisely
on the modular conjugation: **you cannot have both a genuine kept ghost and a free standard-TT closure from
PT-unbrokenness.**

---

## 4. Two-derivation discipline (they agree) + self-critical pass

**Derivation D1 (functional-analytic / definitizability).** `J` needs an `eta`-positive `Delta^{1/2}` from a
spectral function for the `eta`-selfadjoint `Delta`. Spectral functions exist under **definitizability**:
automatic on `Pi_kappa` (finite rank), **absent** for general self-adjoint operators on infinite-rank Krein
spaces (Langer). So real-positive spectrum at infinite rank does **not** yield `J`. (`W84` narrative; the
finite-rank success is T1.)

**Derivation D2 (quasi-Hermiticity dichotomy).** "Standard TT applies" `<=>` quasi-Hermitian `<=>` bounded
boundedly-invertible metric. In infinite dim, PT-unbroken admits only a bounded metric with unbounded inverse
(Krejcirik-Siegl), i.e. quasi-similar, not similar. Either the metric is uniformly bounded (HORN Q -> ghost
removable) or it is not (HORN K -> TT open). (`W84` T2-T4.)

**They agree:** both locate the residual on the **uniform-metric/definitizability** condition and both deny a
genuine-ghost closure from PT-unbrokenness alone. D1 is the "no square root / no `J`" face; D2 is the "no
bounded similarity / removability XOR" face -- two faces of the finite-rank-only implication
PT-unbroken `=>` quasi-Hermitian.

**Self-critical pass (adversary, both directions).**
- *Against RESIDUAL:* "GU's tower could be uniformly PT-unbroken." Conceded as HORN Q -- **but that removes
  the ghost** (SUBTLE), and `W52`/`W53` indicate against uniformity in the UV. Not a genuine-ghost closure.
- *Against SUBTLE:* "keep-and-grade must be nontrivial, so the ghost is not removable" -- **agreed, and that
  is precisely HORN K, where TT does not close.** The nontriviality of keep-and-grade is *evidence for the
  obstruction*, not against it.

**The single load-bearing assumption.** That **mode-wise PT-unbrokenness (real-positive `Delta`) equals
quasi-Hermiticity / definitizability (a uniformly bounded, boundedly-invertible metric with a functional
calculus).** This equivalence is a **finite-rank theorem** (Mostafazadeh; Langer's `Pi_kappa`
definitizability) and is **false at infinite rank / type III** (Krejcirik-Siegl; Langer's non-theorem for
general Krein-selfadjoint operators). GU's region algebra is infinite rank, so the equivalence cannot be
assumed -- and that is exactly the gap that makes the composition **not** close.

---

## 5. Consequence for the campaign (H61 -> H63) and for the conjecture

- The observer conjecture is **not** tightened to "only Reuter-FP-genuine remains." It retains **two**
  independent open legs: (i) the Reuter FP genuine (W83), and (ii) the **infinite-rank Krein-TT conjugation /
  definitizability** leg -- which PT-unbrokenness does *not* discharge. `W77`'s "conditional on
  spectrum(`Delta`) real-positive" is **necessary but not the whole condition**; add "and the metric is
  uniformly bounded / `Delta` is definitizable at infinite rank."
- **For H63.** The re-founding on the algebraic flow+conjugation skeleton should state the postulate as
  *both* "modular-PT-unbroken" **and** "the region algebra's modular operator is definitizable (uniform
  metric)" -- the second is the genuine type-III content and is currently unproven. The `J^2=1` firewall flip
  (H63's lemma L2) needs the `eta`-positive `Delta^{1/2}` that only definitizability supplies.
- **The honest fork for GU.** HORN Q (quasi-Hermitian, ghost removable) would be a *different, still
  important* conclusion: the AS-branch theory is secretly positive-metric and unitarity is standard -- but
  keep-and-grade / the Krein firewall would then be a redundant description, weakening the observer
  identification's reliance on a genuine indefinite modular conjugation. HORN K (genuine ghost) preserves the
  firewall picture **but** leaves the infinite-rank conjugation theorem genuinely open. The `W52`/`W53`
  indication favors HORN K.

---

## 6. Confidence grade and what would move it

- **Finite-rank collapse is real (PT-unbroken => quasi-Hermitian => TT closes, ghost removable):** **high**
  (exact, `W84` T1; Mostafazadeh; Langer `Pi_kappa`).
- **Implication fails at infinite rank (real spectrum admits only unbounded-inverse metric):** **high** --
  Krejcirik-Siegl is a published theorem with a canonical example; the `W84` tower is an exact finite
  surrogate.
- **Closure needs an independent uniform-metric/definitizability condition (no collapse):** **high** (`W84`
  T3; Langer's non-theorem for general Krein-selfadjoint operators).
- **Removability XOR (quasi-Hermitian <=> removable ghost):** **high** (`W84` T4; arXiv:2606.13251,
  medium-high on the paper's finite-dim scope).
- **GU sits on HORN K (genuine ghost, obstruction stands):** **medium** -- an *indication* from `W52`/R1
  (`||C|| -> infinity`) + `W53` (UV approach to the exceptional locus), not a proof that the infinite-mode
  metric inverse is unbounded.
- **VERDICT = RESIDUAL TYPE-III OBSTRUCTION:** **medium-high.** That PT-unbrokenness is necessary-not-sufficient
  and the conditions do not collapse is rigorous (theorem-backed); *which* horn GU lands on is the residual
  open, honestly flagged.

**What would move it most:** (a) compute whether GU's spin-2 modular tower is **uniformly** PT-unbroken (a
uniform spectral gap along the AS trajectory into the UV) -- uniform => HORN Q (removable ghost, a different
conclusion), non-uniform => HORN K (obstruction confirmed); this is the same UV RG computation `W53`/Branch E
already share. (b) A definitizability criterion for the region algebra's `Delta` at infinite rank (would
convert the residual into a decidable test). (c) An infinite-rank / type-III Krein conjugation theorem under
uniform boundedness (would close HORN Q's TT leg conditionally).

---

## 7. What this does NOT do

No GU claim-status, `CANON.md`, `RESEARCH-STATUS.md`, verdict, or public-posture change. No external action;
all citations are read-only literature. The conjecture remains a conjecture; H61/H61a remain **OPEN** (now
with the residual sharpened: PT-unbrokenness is necessary but not sufficient at type III; the residual is
uniform-metric/definitizability, independent of AS-selection; the two named conditions do not collapse). The
deliverable is: the precise reason the `W77 x W83` composition does not close (finite-rank
PT-unbroken `=>` quasi-Hermitian fails at infinite rank, Krejcirik-Siegl + Langer); the removability
dichotomy reconciling arXiv:2606.13251 (HORN Q removable-ghost vs HORN K genuine-ghost-with-obstruction); the
repo-native indication that GU is on HORN K; and the single load-bearing assumption (finite-rank equivalence
of PT-unbroken and quasi-Hermitian). Reproducible: `tests/W84_rankN_krein_tt.py` (5/5, exit 0).
