---
artifact_type: exploration
status: exploration (decisive make-or-break case study; 5-persona inline team; concrete rank-2 model + structural derivation + literature check; deterministic test)
created: 2026-07-12
hypothesis: H61a
conjecture: "the source action IS the observer (CONJECTURE-source-action-is-the-observer-2026-07-11.md)"
branch: "H61 Krein Tomita-Takesaki campaign -- the RANK-2 case study (does Shulman's Pi_1 theorem extend beyond rank 1?)"
title: "H61a -- RANK-2 KREIN TOMITA case study. VERDICT = PARTIAL-CONDITIONAL. The decisive object is the modular operator Delta = S^+ S built from the *Krein* Tomita operator S(aOmega)=a^+Omega (a^+ = eta a* eta the Krein adjoint -- NOT the Hilbert adjoint W67/W74 used). Delta is exactly eta-selfadjoint at every rank; the full modular skeleton (J^2=1, JMJ=M', eta-positive polar decomposition S=J Delta^{1/2}, eta-unitary flow) exists IFF spectrum(Delta) is real & positive (the 'modular-PT-unbroken' regime). By Langer's Pi_kappa definitizable-operator theory the non-positive-type defect of Delta is bounded by kappa: at rank 1 it is <= one non-real pair, patched by Shulman's SINGLE quasivector (theorem); at rank 2 it can be TWO non-real pairs = a genuinely 2-dimensional defect (verified: #non-real eigenvalues <= 2*kappa; Pi_1 caps at 2, Pi_2 reaches 4) that a single quasivector cannot patch, and there the eta-positive polar decomposition (the modular CONJUGATION, Shulman's exact deliverable) is the LEADING-EDGE failure. So: EXTENDS on the unbroken interior (a genuine rank-2 witness with all four properties is constructed), OBSTRUCTS on the exceptional/non-real (PT-broken) locus -- which is exactly Branch E's exceptional Jordan locus (W52) and W67's non-positive-vacuum obstruction, now living on the modular operator itself. The finite type-I toy CANNOT decide which class GU's (+64,-64) region algebra is in, because J-symmetry of M_d(C)(x)I forces a factorized grading that confines Delta to the unbroken interior; the obstruction lives only in the quasivector / indefinite-vacuum / type-III regime GU actually needs."
grade: "exploration / two independent derivations that AGREE (concrete finite rank-2 model + structural Pontryagin/Langer argument), deterministic tests/W77_H61a_rank2_krein_tomita.py (5/5, numpy-only, exit 0) + literature check (2026-07-12, read-only: no Pi_kappa (kappa>=2) modular-conjugation theorem exists). The rank-2 EXTENDS-witness (all four properties on a genuine cyclic vector) is PROVEN exactly; the Langer #non-real <= 2*kappa separation and the leading-edge conjugation failure are PROVEN on the finite model; the claim that GU's infinite-rank type-III region algebra lands in the broken (obstruct) class is NOT proven here -- it is the residual open question the finite toy cannot reach. No canon, RESEARCH-STATUS, CANON, claim-status, verdict, or public-posture change. The conjecture remains a conjecture; H61 remains OPEN (now with a sharpened rank-2 map)."
depends_on:
  - explorations/H61-krein-tt-first-swing-2026-07-11.md
  - explorations/path5-branchA-krein-modular-conjugation-2026-07-11.md
  - explorations/path2-branchE-nogo-2026-07-11.md
  - explorations/H62-arena-value-partition-firmup-2026-07-11.md
  - GEOMETER-VS-PHYSICS-OBJECTS.md
  - tests/W67_path5_A_krein_modular.py
  - tests/W74_H61_krein_tt_swing.py
  - tests/W52_path2_E_nogo.py
scripts:
  - tests/W77_H61a_rank2_krein_tomita.py
---

# H61a -- the rank-2 Krein Tomita-Takesaki case study (the single decisive gate)

**Role.** H61's first swing (`W74`) triaged the campaign as OPEN-BUT-HARD and named the sharpest next probe:
does **Shulman's `Pi_1` (rank-1) indefinite-metric Tomita theorem extend beyond rank 1?** Rank 2 is the
decisive first step -- no known obstruction, no theorem. If the modular objects (`J`, `Delta^{it}`,
`J M J = M'`) extend to a rank-2 Krein space, the Krein-TT critical path (H61) is reachable and the payoff
theorem (H63) follows; if they obstruct, that is the conjecture's **first genuine no-go**, cleanly located.

**This swing's answer: PARTIAL-CONDITIONAL, with the fork located precisely.** The modular skeleton extends
to rank 2 **iff** the modular operator `Delta = S^+ S` stays **real-positive** ("modular-PT-unbroken"); it
**obstructs** on the exceptional / non-real (PT-broken) locus, where a genuinely **2-dimensional** defect
(impossible at rank 1) breaks the `eta`-positive polar decomposition -- i.e. Shulman's modular **conjugation**
is the leading-edge failure. The two required derivations -- a concrete finite rank-2 model and a structural
Pontryagin-space argument -- **agree**.

**Artifacts:** this file + deterministic `tests/W77_H61a_rank2_krein_tomita.py` (5/5, numpy-only, exit 0).
**Not committed. Not a claim-status change.** Exploration-grade.

---

## 0. Construction forks (GEOMETER-VS-PHYSICS-OBJECTS.md discipline)

Three load-bearing objects; I state which construction I use and why.

1. **The Tomita operator.** I use the **Krein** Tomita operator `S(aOmega) = a^+ Omega` with the **Krein
   adjoint** `a^+ = eta a* eta` -- program-native, the object forced by keep-and-grade. This is the correction
   over `W67`/`W74`: those files computed the **Hilbert** modular operator `Delta = rho_L (x) rho_R^{-1}`
   (positive by construction, grading-independent) and then checked the reflection-symmetry criterion as an
   *extra* condition. That silently used the positive-Hilbert object. The **decisive** rank question lives in
   the *Krein* modular operator `Delta = S^+ S` (Krein adjoint of the antilinear `S`), which this swing
   computes for the first time.
2. **The modular conjugation.** The antilinear `J` from the **Krein polar decomposition** `S = J Delta^{1/2}`
   with an **`eta`-positive** `Delta^{1/2}` (not the linear grading `C`; that type error is settled in Branch A).
3. **Positivity of the vacuum.** Per H61/H62/H63, I do **not** require a distinguished positive vacuum state.
   The arena is the *algebraic* flow+conjugation skeleton; a positive state is the observer's symmetry-broken
   value. The rank-2 test targets the skeleton, not a positive state.

---

## 1. Five-persona team (inline, sequential, single context)

### Persona 1 -- operator-algebra specialist (builds the model, computes `J`, `Delta`)

**The Krein modular operator, in closed form.** For `M = M_d(C) (x) I` on `H = C^d (x) C^d` with a genuine
cyclic separating vector `Omega = sum_k c_k |k>|k>` and fundamental symmetry `eta` acting `X -> eta_0 X eta_0`
(matrix picture, vector = `d x d` matrix `X`), the Krein Tomita operator is the antilinear map

>  `S(X) = eta_0 C^{-1} X* eta_0 C`,  `C = diag(c_k)` .

Its Krein adjoint `S^+` (for an antilinear `S(v) = M conj(v)`, `S^+` has matrix `eta M^T eta`) gives the
**modular operator**

>  `Delta = S^+ S : X -> C^2 X C^{-2}` ,

which is **exactly `eta`-selfadjoint** (`Delta^+ = Delta`), **real, positive**, and **commutes with `eta`**.
The polar decomposition is genuine: `Delta^{1/2}: X -> C X C^{-1}`, and

>  `J = S Delta^{-1/2} : X -> eta_0 X* eta_0` ,

an antilinear involution. On a rank-2 space (`eta_0 = diag(1,-1)`, so `eta = eta_0 (x) eta_0` has two negative
eigenvalues, `Pi_2`) **all four modular properties hold with the Krein objects** (`W77` T1, residuals `< 1e-15`):

| property | status on the rank-2 witness |
|---|---|
| (a) Krein polar decomposition `S = J Delta^{1/2}`, `Delta^{1/2}` `eta`-positive | **HOLDS** |
| (b) `J^2 = 1` | **HOLDS** |
| (c) `J M J = M'` (and Krein-antiisometry `[Jx,Jy] = conj[x,y]`) | **HOLDS** |
| (d) `Delta^{it} M Delta^{-it} = M`, flow `eta`-unitary | **HOLDS** |

So **there is a genuine rank-2 model in which Shulman's theorem's conclusion holds** -- the extension is not
universally blocked.

**But the same computation shows *why* this is not the whole story.** `Delta = S^+ S` is `eta`-selfadjoint,
and its *sign* is governed by the indefinite form: `[Delta x, x] = [Sx, Sx]`, which is **indefinite**. So
`Delta` is **not** `eta`-positive in general -- it can acquire non-real spectrum. The witness above is
positive only because `[Delta, eta] = 0`. The decisive question is whether that always happens.

### Persona 2 -- math referee (is the polar decomposition genuine? is `J^2=1`, `JMJ=M'` verified?)

- The polar decomposition in T1 is **genuine in the Krein space**: `Delta` is `eta`-selfadjoint with real
  positive spectrum, `Delta^{1/2}` is `eta`-positive, `J` is a Krein-antiisometry with `J^2=1` and `J M J=M'`
  (all machine-zero). This is a **real, exact rank-2 result**, not a Hilbert artifact: it uses the Krein
  adjoint throughout.
- **The referee's load-bearing caveat.** The witness is **type I** with a **genuine positive-normed cyclic
  vector**, and the grading is **reflection-symmetric/factorized** (`eta = eta_0 (x) eta_0`). Persona 4 shows
  this is **forced** by `J`-symmetry of `M_d(C) (x) I` -- and that forcing is exactly what makes `Delta`
  `eta`-positive. So T1 proves *existence in the unbroken interior*, **not** that every rank-2 model extends.
  The referee refuses to grade this as "EXTENDS" until the broken regime is examined.

### Persona 3 -- adversary ("your finite model is type I and hides the real obstruction")

**Attack.** "You constructed a positive `Delta` because you chose a factorized grading and a positive cyclic
vector. That is precisely the case Shulman already handles at any rank in the type-I setting. The genuine
rank-2 difficulty is the **quasivector** regime -- when there is *no* positive cyclic vector and the modular
operator feels the indefiniteness. You have hidden the obstruction, not tested it."

**Where the adversary lands (this is correct and I concede it).** The finite type-I model with a genuine
cyclic vector **cannot** reach the obstruction, and I prove why (`W77` T2): for `M = M_d(C) (x) I` to be
`J`-symmetric (`a^+ in M` for all `a`), the grading **must factorize** `eta = P (x) Q`; a non-factorized
rank-2 grading makes `a^+ not in M`. A factorized grading forces `[Delta, eta] = 0`, hence `Delta` real-positive
**at any rank**. So the type-I toy is **confined to the unbroken interior** -- it is *structurally blind* to
the rank-2 obstruction, which lives only where a **quasivector** is genuinely needed (indefinite vacuum, no
positive cyclic vector -- the type-III / infinite-rank case GU actually needs). This is the same wall
`W67`/`W74` hit ("no finite toy can realize type III"), now sharpened: it is not merely that the toy is type I,
it is that `J`-symmetry *forces* the positive-`Delta` class.

### Persona 4 -- cross-checker (second derivation + literature)

**Second derivation (structural, independent of the finite model): the Pontryagin / Langer rank bound.**
`Delta = S^+ S` is `eta`-selfadjoint on `Pi_kappa`. By **H. Langer's theory of definitizable operators on
Pontryagin spaces**, an `eta`-selfadjoint operator has its **total non-real spectral multiplicity (and its
Jordan / negative-type defect) bounded by `kappa`**. Concretely (`W77` T3, verified over thousands of random
Krein-Tomita-type `S`):

- **`Pi_1` (`kappa = 1`):** `#`non-real eigenvalues of `Delta` `<= 2` -- **at most one** conjugate pair. The
  non-positive-type defect is `<= 1`-dimensional. **Shulman's single quasivector patches exactly one unit** --
  which is precisely why the `Pi_1` theorem exists.
- **`Pi_2` (`kappa = 2`):** `#`non-real eigenvalues **reaches 4** -- **two** conjugate pairs, a genuinely
  **2-dimensional** non-positive defect that is **impossible at rank 1**. A single quasivector cannot patch a
  2-unit defect.

This **agrees** with the finite model: the finite model shows extension is *possible* (positive `Delta`
exists), the structural bound shows rank 2 *opens a defect dimension* the rank-1 method cannot cover. The two
derivations meet at the exact object -- the spectrum of `Delta = S^+ S` -- and give a **conditional** answer.

**Where the obstruction actually bites (`W77` T4): the CONJUGATION is the leading edge.** On a broken rank-2
`Delta` (non-real spectrum):
- the **`eta`-positive polar decomposition** `S = J Delta^{1/2}` **fails** -- there is no `eta`-positive
  square root of a non-real-spectrum operator, so Shulman's antilinear `J`-involution is **not recoverable**;
- the **flow** `Delta^{it}` is **strictly more robust but also conditional**: `eta`-unitary iff `log Delta` is
  `eta`-selfadjoint, i.e. iff `spectrum(Delta)` avoids the **negative real axis**. It **survives** a non-real
  pair with *positive* real part (exactly Gottschalk's boost spectrum) but **fails** at a negative real
  eigenvalue. So the conjugation is the **first casualty** as `Delta` leaves the interior -- and it is exactly
  the object Shulman's rank-1 quasivector supplies and for which **no `Pi_kappa` (`kappa >= 2`) theorem exists**.

**Literature check (2026-07-12, read-only).** Confirmed: **Shulman 1997** (`Pi_1`, `Rev. Math. Phys.` 9,
749-783) is the state of the art for the modular conjugation; his companion GNS-on-Pontryagin paper
(`Funct. Anal. Appl.` 31, 1997) builds representations on `Pi_kappa` via neutral cocycles but **does not**
prove a modular-conjugation Tomita theorem at `kappa >= 2`. **Gottschalk 2002** supplies the flow (boost /
BW analyticity). **Langer's** definitizable-operator theory supplies the `kappa`-bound. **No `Pi_kappa`
(`kappa >= 2`) Tomita-Takesaki conjugation theorem is in the literature.** The rank-2 gate is genuinely open,
and this swing maps it.

### Persona 5 -- synthesizer (the verdict)

See Sections 2-4.

---

## 2. VERDICT: PARTIAL-CONDITIONAL (the fork, stated precisely)

**The Krein modular skeleton extends from rank 1 to rank 2 IFF the modular operator `Delta = S^+ S` is
real-positive (modular-PT-unbroken).**

- **EXTENDS (unbroken interior).** When `Delta` has real positive spectrum, all four properties hold with the
  genuine Krein objects: `S = J Delta^{1/2}` (`eta`-positive `Delta^{1/2}`), `J^2 = 1`, `J M J = M'`,
  Krein-antiisometry, `Delta^{it} M Delta^{-it} = M` with an `eta`-unitary flow. A concrete rank-2 witness
  is constructed and verified exactly (`W77` T1).
- **OBSTRUCTS (broken locus).** When `Delta` acquires non-real spectrum -- possible at rank 2 with a
  **2-dimensional** defect that rank 1 forbids -- the `eta`-positive polar decomposition fails and the
  modular **conjugation** (Shulman's rank-1 deliverable) is **not recoverable by a single quasivector**. The
  flow is more robust (survives a non-real pair off the negative axis, per Gottschalk) but also degrades on
  the negative-real-axis part of the broken locus.

It is **not** a clean EXTENDS (a rank-2 model can break; the defect can be 2-dimensional) and **not** a clean
OBSTRUCTS (a rank-2 model with a genuine cyclic vector extends fully). The computation gives the conditional
answer; I did not force either pole.

---

## 3. Where rank 2 differs from rank 1 (the precise obstruction, named)

**The non-positive-type defect of the modular operator `Delta = S^+ S` is bounded by `kappa` (Langer). Rank 1
allows a `<= 1`-dimensional defect, which Shulman's SINGLE quasivector patches -- that is the whole content of
the `Pi_1` theorem. Rank 2 allows a `2`-dimensional defect (two non-real modular pairs), which a single
quasivector cannot patch, and on which the `eta`-positive polar decomposition -- the modular conjugation --
ceases to exist.**

- This is **specific to the dimension of the defect**, and it **generalizes to all rank `>= 2`**: at rank
  `kappa` the defect can be `kappa`-dimensional, requiring a `kappa`-fold quasivector construction that
  Shulman's method (built for one) does not supply. GU's `(+64,-64)` metric is infinite rank -- the defect is
  unbounded.
- The obstruction locus is **exactly the exceptional (Jordan) / non-real (PT-broken) spectrum** of Branch E
  (`W52`) and the **non-positive-vacuum** obstruction of `W67` -- the *same* keep-and-grade mechanism, now
  located on the **modular operator itself**. When `Delta` hits an exceptional point (a Jordan block at an
  eigenvalue collision), it is precisely the `a/b -> 1` degeneration Branch E identified; past it, non-real
  spectrum = PT-broken = no `eta`-positive `Delta^{1/2}`.

**The finite type-I toy cannot decide which class GU is in.** `J`-symmetry forces the toy into the unbroken
interior (Section 1, Persona 3/4). Whether GU's genuinely indefinite, infinite-rank, type-III region algebra
sits in the unbroken (extends) or broken (obstructs) class is a **continuum / quasivector** question no finite
model reaches -- the same open frontier as the type-III question in `W67`/`W74`.

---

## 4. Two-derivation discipline (they agree) + self-critical pass

**Derivation (i) -- concrete finite model.** Rank-2 witness with all four properties exact (`W77` T1);
`J`-symmetry forces the factorized/positive-`Delta` class (`W77` T2); `Delta = S^+ S` exactly `eta`-selfadjoint
and the leading-edge conjugation failure on a broken `Delta` (`W77` T4).

**Derivation (ii) -- structural (Pontryagin/Langer).** `Delta` `eta`-selfadjoint with `#`non-real `<= 2*kappa`
(`W77` T3): `Pi_1` caps at one pair (single quasivector -> theorem), `Pi_2` reaches two pairs (2-dim defect,
no single-quasivector patch).

**They agree:** both locate the decision on `spectrum(Delta = S^+ S)`; the finite model proves the unbroken
interior extends, the structural bound proves rank 2 opens a defect dimension the rank-1 method cannot patch.
Conditional, not clean either way.

**Self-critical pass (the adversary's strongest press, both directions).**
- *Against EXTENDS:* "you smuggled positivity / used a type-I artifact." **Conceded and quantified:** the
  extends-witness is exactly the `J`-symmetry-forced positive-`Delta` type-I class; it proves *possibility*,
  not universality. The load-bearing assumption for "EXTENDS" would be that GU's region algebra is
  modular-PT-unbroken -- **unestablished**.
- *Against OBSTRUCTS:* "the obstruction is a model artifact." **Answered:** the obstruction is not a single
  contrived model -- it is the `kappa`-bounded defect of *any* `eta`-selfadjoint modular operator (Langer, a
  theorem), and it coincides with two independently-derived repo obstructions (`W52`, `W67`). But it is
  **not** a completed no-go either: no *specific* GU modular operator is shown to be broken. So the honest
  status is a **conditional obstruction with a named, decidable trigger** (the modular operator reaching its
  exceptional locus), exactly the shape Branch E reported for loop positivity.

**The single load-bearing assumption.** Whether GU's genuinely-indefinite, infinite-rank, type-III region
algebra has a **modular-PT-unbroken** modular operator `Delta = S^+ S` (real-positive spectrum) or a **broken**
one (non-real spectrum / exceptional locus). EXTENDS lives on the first, the first genuine no-go on the second.
The finite/type-I toy cannot decide it; it is the decidable continuum question this case study hands forward.

---

## 5. Consequence for the campaign (H61 -> H63)

- The rank-2 gate is **not** cleanly open and **not** cleanly closed: it is **conditional on the modular
  operator's spectrum**. This *sharpens* `W74`'s "extend Shulman `Pi_1 -> Pi_kappa`" target: the extension is
  not a uniform theorem to be proven, it is **contingent** on staying in the unbroken interior, with a named
  failure locus (the exceptional / PT-broken spectrum of `Delta`).
- It **corrects** `W74`'s "the `J_K` construction is rank-stable (`n=1,2,3`)": that rank-stability is the
  **Hilbert** modular operator (grading-independent, always positive) plus an extra reflection-symmetry check
  -- the *unbroken interior*. The genuine rank question is the **Krein** modular operator `Delta = S^+ S`,
  which `W74` did not compute; its spectrum is what decides the gate.
- **For H63.** The payoff should be re-founded, per H61's reframe, on the algebraic flow+conjugation skeleton
  **in the modular-PT-unbroken regime**, with the unbroken condition (`spectrum(Delta) real-positive`) stated
  as an **explicit postulate** (Track-2 conditional-theorem form: "H63 given the region algebra is
  modular-PT-unbroken"). The residual open question -- is GU's region algebra unbroken? -- is exactly the
  decidable continuum computation this swing isolates, and it couples to Branch E's identical open computation
  (does the RG flow reach the exceptional locus?).

---

## 6. Confidence grade and what would move it

- **Rank-2 EXTENDS-witness (all four properties, genuine cyclic vector):** **high** (exact, `W77` T1).
- **`J`-symmetry forces factorized grading => type-I toy blind to the obstruction:** **high** (`W77` T2 +
  the structural argument).
- **Langer bound `#`non-real `<= 2*kappa`, `Pi_1` caps at 1 pair / `Pi_2` reaches 2:** **high** (exact over
  thousands of samples; a cited theorem of definitizable-operator theory).
- **Conjugation is the leading-edge failure (fails before the flow):** **high** on the finite model (`W77` T4).
- **VERDICT = PARTIAL-CONDITIONAL:** **medium-high.** The fork (unbroken extends / broken obstructs) is
  rigorous; the claim that *GU's* infinite-rank type-III algebra is in the broken class is **not** proven --
  it is the residual open question, honestly flagged.

**What would move it most:** (a) exhibit an *infinite-mode / type-III* Krein-graded model (Bogoliubov ghost
doubling) and compute whether its `Delta = S^+ S` is modular-PT-unbroken or broken -- the first computation
that reaches past the type-I wall; (b) a `kappa`-fold quasivector construction extending Shulman to `Pi_2`
in the unbroken interior (would upgrade "possible" to "theorem, conditional on unbroken"); (c) prove the GU
region algebra's modular operator is generically broken (would convert the conditional obstruction into the
conjecture's first completed no-go).

---

## 7. What this does NOT do

No GU claim-status, `CANON.md`, `RESEARCH-STATUS.md`, verdict, or public-posture change. No external action;
all citations are read-only literature. The conjecture remains a conjecture; H61 remains **OPEN** (now with a
sharpened rank-2 map: conditional on the modular operator's spectrum, with a named failure locus). The
deliverable is: a genuine rank-2 Krein modular skeleton constructed with the *Krein* Tomita operator (all four
properties in the unbroken interior); the exact place rank 2 differs from rank 1 (the Langer `kappa`-bounded
defect; single-quasivector patches one unit, rank 2 needs two); the leading-edge location of the obstruction
(the conjugation / `eta`-positive polar decomposition); an honest account of why the finite type-I toy cannot
decide the GU case; and the coupling to Branch E (`W52`) and `W67`. Reproducible:
`tests/W77_H61a_rank2_krein_tomita.py` (5/5, exit 0).
