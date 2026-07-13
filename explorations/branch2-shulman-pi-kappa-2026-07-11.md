---
artifact_type: exploration
status: exploration (blind-wave Branch 2; 5-persona inline team; the direct pure-math route -- extend Shulman's Pi_1 quasivector Tomita CONJUGATION theorem to Pi_kappa / infinite rank; concrete rank-2 kappa-quasivector attempt + literature check + deterministic toy)
created: 2026-07-13
hypothesis: H61 / H61a (the observer-conjecture Krein-TT critical path)
conjecture: "the source action IS the observer (CONJECTURE-source-action-is-the-observer-2026-07-11.md)"
branch: "Branch 2 of the TYPE-III KREIN TOMITA-TAKESAKI blind wave -- does Shulman's Pi_1 (rank-1) quasivector construction of the modular conjugation J extend to Pi_kappa / infinite rank via a kappa-quasivector / multi-quasivector device, or is the rank-1 restriction a GENUINE obstruction? (cross-shared with Branch 3's relative/algebraic modular route; both reduce to the infinite-rank definitizability residual)"
title: "Branch 2 -- Shulman Pi_1 -> Pi_kappa. VERDICT = PARTIAL (EXTENDS under definitizability, OBSTRUCTED for GU). A kappa-quasivector construction EXTENDS Shulman's modular conjugation J to every FINITE Pi_kappa -- because on Pi_kappa every eta-selfadjoint operator is DEFINITIZABLE (Langer), the non-positive-type defect of the Krein modular operator Delta=S^+S is a FINITE kappa-dimensional invariant subspace, and #non-real(Delta) <= 2*kappa, so kappa quasivectors patch a kappa-dim defect exactly as one quasivector patches a 1-dim defect; rank 2 is a concrete 2-quasivector witness with all four modular properties (W90 T1). BUT at finite rank the ghost is REMOVABLE (definitizable => quasi-Hermitian), so this is not GU's regime. At INFINITE rank (GU's genuine Delta=S^+S: (+64,-64) per point x infinitely many modes, real-positive spectrum with UNBOUNDED metric inverse) the quasivector route is GENUINELY OBSTRUCTED, not by a failure of one device: a quasivector patches ONE finite defect unit, the count needed = the negative index = infinity, and the kappa=infinity limit assembles into a BOUNDED J (a Krein-antiisometry) IFF the metric inverse is uniformly bounded == definitizable. For GU's non-definitizable Delta the truncated K-quasivector patch norm DIVERGES (Krejcirik-Siegl: bounded metric, unbounded inverse; W52/W53 UV exceptional locus), so no bounded J exists. Thus the quasivector method's REACH IS CO-EXTENSIVE WITH DEFINITIZABILITY; it does NOT independently cross the frontier -- it REDUCES, with no remainder, to the shared infinite-rank definitizability residual, and hands it unchanged to Branch 3 (algebraic) / Branch 5 (no-go). Repo-native indication (W52/W53) places GU on the OBSTRUCTED side. Indication, not proof."
grade: "exploration / two independent derivations that AGREE (D1 the finite-rank quasivector-count = definitizable finite defect, patchable; D2 the infinite-rank assembly norm = metric-inverse norm, bounded iff definitizable). Deterministic tests/W90_shulman_pi_kappa.py (5/5, numpy-only, exit 0) + literature check (2026-07-13, read-only: Shulman 1997 Pi_1 single-quasivector Tomita theorem; Langer definitizable-operator theory on Pi_kappa incl. the kappa-dim non-positive invariant subspace and the finitely-many-critical-points spectral function; Krejcirik-Siegl PRD 86 (2012) 121702 bounded metric with unbounded inverse; arXiv:2606.13251 positive-KMS <=> quasi-Hermiticity). The rank-2 EXTENDS-under-definitizability witness (T1), the finite-defect = kappa criterion (T2), the infinite-rank divergent-assembly obstruction (T3), and the non-real-locus bound on EXTENDS (T4) are PROVEN on the toy; that GU's Delta is on the non-definitizable side is an INDICATION (W52/W53), not proven here. No canon, RESEARCH-STATUS, CANON, claim-status, verdict, or public-posture change. The conjecture remains a conjecture; H61/H61a remain OPEN (the residual sharpened: the pure-math quasivector route does not independently resolve it -- it collapses onto the definitizability residual Branch 3 must confront)."
depends_on:
  - explorations/rankN-krein-tt-for-gu-2026-07-11.md
  - explorations/H61a-rank2-krein-tomita-case-study-2026-07-11.md
  - explorations/H61a-rank2-verdict-and-convergence-2026-07-11.md
  - explorations/H61-krein-tt-first-swing-2026-07-11.md
  - explorations/path2-branchE-nogo-2026-07-11.md
  - explorations/CONJECTURE-source-action-is-the-observer-2026-07-11.md
  - GEOMETER-VS-PHYSICS-OBJECTS.md
  - tests/W77_H61a_rank2_krein_tomita.py
  - tests/W84_rankN_krein_tt.py
  - tests/W74_H61_krein_tt_swing.py
  - tests/W52_path2_E_nogo.py
scripts:
  - tests/W90_shulman_pi_kappa.py
external_refs:
  - "V. S. Shulman, 'Quasivectors and Tomita-Takesaki Theory for Operator Algebras on Pi_1-Spaces', Rev. Math. Phys. 9 (1997) 749-783, doi:10.1142/S0129055X97000270 -- antilinear J-involution + double commutant on a Pontryagin Pi_1 space (rank of indefiniteness 1) via a SINGLE quasivector; the state of the art, no Pi_kappa (kappa>=2) conjugation theorem"
  - "H. Langer, definitizable operators on Krein/Pontryagin spaces -- on Pi_kappa EVERY bounded self-adjoint operator is definitizable, with a spectral function (finitely many critical points), a kappa-dimensional non-positive invariant subspace, and non-real spectrum in <= kappa conjugate pairs of finite algebraic multiplicity; NO such theorem for general self-adjoint operators on infinite-rank Krein spaces"
  - "D. Krejcirik & P. Siegl, 'On the metric operator for the imaginary cubic oscillator', Phys. Rev. D 86 (2012) 121702(R), arXiv:1208.1866 -- real spectrum, complete eigenvectors NOT a Riesz basis => bounded metric with UNBOUNDED inverse => not similar (only quasi-similar) to self-adjoint; the canonical infinite-dim PT-unbroken non-definitizable case"
  - "arXiv:2606.13251, KMS conditions for non-Hermitian systems -- positivity of the biorthogonal thermal state <=> quasi-Hermiticity (the removable-ghost horn)"
---

# Branch 2 -- does Shulman's Pi_1 quasivector Tomita CONJUGATION theorem extend to Pi_kappa / infinite rank?

**Role.** This branch takes the **direct pure-math route** to the frontier that turns the observer conjecture
conditional->theorem: the Krein modular **conjugation** `J` (the firewall antilinear involution `J^2=1`,
`JMJ=M'`, Krein-antiisometry) on GU's genuinely indefinite, **infinite-rank**, type-III region algebra.
Shulman 1997 builds `J` on a Pontryagin `Pi_1` space (rank of indefiniteness **1**) via a **single quasivector**
that patches the `<=1`-dimensional non-positive-type defect of the modular operator. `W84`/rankN showed that at
infinite rank the metric inverse is unbounded (non-definitizable) and left the pure-math question open. **This
branch's question:** is the rank-1 restriction the failure of **one device** (a single quasivector), curable by a
**kappa-quasivector / multi-quasivector** construction that patches a `kappa`-dimensional defect -- or a
**genuine obstruction** no quasivector route can cross?

**Answer: PARTIAL. A kappa-quasivector construction EXTENDS Shulman to every FINITE `Pi_kappa` under
DEFINITIZABILITY, but is GENUINELY OBSTRUCTED at GU's infinite-rank `Delta = S^+ S`. The quasivector method's
reach is CO-EXTENSIVE WITH DEFINITIZABILITY -- it does NOT independently cross the frontier; it reduces, with no
remainder, to the shared infinite-rank definitizability residual.** Cross-shared with Branch 3 (relative/algebraic
modular skeleton): both reduce to *does GU's `Delta` admit a definitizing polynomial / a uniformly bounded metric?*

**Artifacts:** this file + deterministic `tests/W90_shulman_pi_kappa.py` (5/5, numpy-only, exit 0).
**Not committed. Not a claim-status change.** Exploration-grade.

---

## 0. Construction forks (GEOMETER-VS-PHYSICS-OBJECTS.md discipline)

| Object | Construction used | Load-bearing here |
|---|---|---|
| **The algebra** | GU-native indefinite region `*`-algebra on the **Krein space** `[x,y]=<x,eta y>`, `eta` = the C-grading = fundamental symmetry, **infinite** rank of indefiniteness (`(+64,-64)` per point x infinitely many modes). | GU's regime is a **genuine Krein space**, NOT a Pontryagin `Pi_kappa` (finite `kappa`). Langer's finite-rank levers -- and Shulman's quasivector, which is finite-rank machinery -- do NOT transfer for free. |
| **The modular operator** | the **Krein** `Delta = S^+ S`, `S(aOmega)=a^+Omega`, `a^+ = eta a* eta` (the `W77` object, not the Hilbert `Delta` of `W67`/`W74`). | Its *definitizability* -- not merely its spectrum -- decides whether the quasivector route assembles. |
| **The modular conjugation** | the antilinear `J` from the **eta-positive** polar decomposition `S = J Delta^{1/2}` (Shulman's exact deliverable), **not** the linear grading `C`. | This is the object Shulman's single quasivector supplies at rank 1 and the object with no `Pi_kappa (kappa>=2)` theorem. |
| **The "kappa-quasivector"** | encoded via its **essential, construction-independent content**: a quasivector regularizes **one unit** of the non-positive-type defect so an eta-positive polar decomposition exists there; `kappa` quasivectors regularize a `kappa`-dimensional defect. | We do NOT reimplement Shulman's exact functional-analytic device. The facts we test -- defect dimension = negative index, finite & patchable iff definitizable, assembled `J` bounded iff metric inverse bounded -- are properties of `Delta` and the Krein form, independent of the device, so the verdict does not rest on a bespoke construction. |

The one fork this branch sharpens: **"more quasivectors" vs "definitizability."** More quasivectors reach higher
*finite* rank; they never reach `kappa = infinity`, and the `kappa = infinity` limit is exactly where
definitizability -- the property that makes the quasivector patch *bounded* -- fails.

---

## 1. Five-persona team (inline, sequential, single context)

### Persona 1 -- Krein-space operator theorist (states Shulman's Pi_1 construction and WHERE it uses rank 1)

**Shulman's `Pi_1` theorem, precisely (Rev. Math. Phys. 9 (1997) 749).** Let `M` be a weakly-closed
**`J`-symmetric** operator algebra with identity on a **Pontryagin `Pi_1`** space `H` (indefinite inner product
with exactly **one** negative square) possessing a **cyclic and separating** vector `Omega`. Then there is an
**antilinear `J`-involution** `j: H -> H` with `j M j = M'` -- a precise analogue of the Fundamental Tomita
Theorem in the indefinite metric -- together with a **double-commutant theorem** for such algebras. The device is
the **quasivector**: a controlled generalized vector (a functional not implemented by a genuine Hilbert vector)
that substitutes for the **neutral / self-orthogonal** vectors the indefinite form introduces, so that the
Tomita operator `S(aOmega) = a^+Omega` has a well-defined **eta-positive polar decomposition** `S = J Delta^{1/2}`.

**Where rank 1 is used -- two coupled places, both load-bearing.**
1. **The single quasivector patches a `<=1`-dimensional defect.** In `Pi_1` the maximal **non-positive-type**
   (neutral + negative) subspace the modular operator can feel is **1-dimensional** (negative index `kappa = 1`).
   Shulman's *one* quasivector regularizes exactly *one* unit of that defect. If the defect were `2`-dimensional,
   one quasivector could not cover it.
2. **Implicit definitizability.** By Langer, on `Pi_kappa` (finite) **every bounded eta-selfadjoint operator is
   definitizable**: it has a spectral function with **finitely many critical points**, a `kappa`-dimensional
   non-positive invariant subspace, and non-real spectrum in `<= kappa` conjugate pairs of finite multiplicity.
   `Pi_1` is the smallest nontrivial case: definitizability is automatic, so a **spectral function and an
   eta-positive `Delta^{1/2}` exist** away from the single critical point, which the quasivector handles. Shulman
   does not *state* "definitizable" as a hypothesis because on `Pi_1` it is free -- **that is exactly the rank-1
   assumption hiding in plain sight.**

So the rank-1 restriction is **not** an artifact of a lazy proof; it is where **the defect is patchable by one
quasivector** *and* **definitizability is automatic**. Both scale with `kappa`.

### Persona 2 -- math referee (does a kappa-quasivector patch a kappa-dim defect? the Pi_2 ruling)

**Ruling 1 -- at finite rank, YES: a kappa-quasivector construction extends Shulman.** The two rank-1 ingredients
both survive to any *finite* `kappa`:
- The non-positive-type defect of `Delta = S^+ S` on `Pi_kappa` is a genuine **`kappa`-dimensional invariant
  subspace** (Langer/Pontryagin) -- **finite**. `kappa` quasivectors patch a `kappa`-dimensional defect exactly
  as one patches a 1-dimensional one. (`W90` T2: on `Pi_2` the defect is a 2-dim `Delta`-invariant non-positive
  subspace; `#non-real(Delta) <= 2*kappa = 4`.)
- Definitizability is still **automatic** on `Pi_kappa` (Langer), so the spectral function / eta-positive
  `Delta^{1/2}` exists when `spectrum(Delta)` is **real-positive** -- which is **forced** for a genuine
  cyclic-separating vector (`W77` T2: `J`-symmetry forces a factorized grading, hence `[Delta,eta]=0`, hence
  real-positive). **The rank-2 witness (`W90` T1) has a genuinely 2-dimensional negative-type defect and all four
  modular properties hold** (`J^2=1`, `JMJ=M'`, Krein-antiisometry, eta-unitary flow; residuals `< 1e-15`). This
  **is** the 2-quasivector regime, and it **succeeds**.
- **The referee's caveat (decisive for GU).** At finite rank definitizable => the metric is bounded with bounded
  inverse => **quasi-Hermitian** (`W84` T1), so the ghost is **removable** -- the "extension" lives in the
  removable-ghost regime, **not** GU's kept ghost. And it is confined to **real-positive** spectrum: on a
  genuinely non-real (PT-broken) `Delta` there is **no eta-positive square root**, and **no number of
  quasivectors** repairs it -- quasivectors patch a **neutral/negative-type** defect, not **non-real spectrum**
  (`W90` T4). So "EXTENDS" is bounded to the **definitizable + real-positive** regime.

**Ruling 2 -- at infinite rank, NO, and it is genuine.** A quasivector patches **one finite unit**; the count
needed = the **negative index** = **infinity** for GU. The only hope is a `K -> infinity` limit, and that
assembles into a **bounded** `J` (a Krein-antiisometry) **iff** the metric inverse is **uniformly bounded** ==
**definitizable**. General eta-selfadjoint operators on **infinite-rank** Krein spaces are **not** definitizable
(Langer's `Pi_kappa` theorem is finite-rank-specific); there is **no spectral function**, **no eta-positive
`Delta^{1/2}`**, **no `J`**. The referee **refuses "EXTENDS"** for GU.

### Persona 3 -- adversary (both directions)

- *Against OBSTRUCTED ("you're just failing to imagine the right multi-quasivector; the rank-1 restriction is a
  proof artifact").* Pressed honestly: to build a bounded `J` on GU's tower the adversary needs the
  `K -> infinity` quasivector patch to have **bounded norm**, i.e. `sup_k ||metric_k^{-1}|| < infinity`. That is
  **precisely definitizability / quasi-Hermiticity**, and `W52`/R1 (`||C|| -> infinity` at the exceptional locus)
  + `W53` (that locus sits at the free UV FP the AS flow approaches) give a positive indication it **fails** in
  the UV. **Conceded as logically possible only under uniform boundedness -- but that is HORN Q, where the ghost
  is removable** (`W84` T4), so it does not save a *genuine-ghost* extension. The adversary cannot exhibit a
  bounded multi-quasivector `J` for an unbounded-inverse metric because Krejcirik-Siegl proves the metric inverse
  *is* unbounded for the canonical real-spectrum non-Riesz case.
- *Against EXTENDS-at-finite-rank ("your rank-2 success is a type-I artifact").* Answered and conceded in scope:
  the rank-2 witness is the `J`-symmetry-forced factorized/positive-`Delta` class (`W77` T2); it proves the
  quasivector route *works where definitizability holds*, and it is exactly the removable-ghost regime. It does
  **not** claim to reach GU's non-definitizable `Delta`.

The two pushes are mutually defeating: uniform boundedness (needed to extend) removes the ghost; a genuine ghost
(unbounded inverse) blocks the bounded assembly. **Neither delivers a genuine-ghost infinite-rank `J`.**

### Persona 4 -- cross-checker on a rank-2 model (the concrete Pi_2 attempt + literature)

**The rank-2 kappa-quasivector attempt (`W90`, exact, numpy-only).**
- **T1 -- the 2-quasivector regime succeeds.** `Pi_2` (`eta_full = diag(1,-1,-1,1)`, negative index `kappa=2`),
  Krein Tomita operator `S(X)=eta0 C^{-1} X* eta0 C`, `Delta = S^+ S: X -> C^2 X C^{-2}` real-positive. `J`
  built; `J^2=1` (`0`), `JMJ=M'` (`9e-16`), Krein-antiisometry (`5e-16`), polar decomposition `S=J Delta^{1/2}`
  (`4e-16`), eta-unitary flow (`1e-15`). A single (rank-1) quasivector cannot cover this 2-dim defect; the
  `kappa=2` patch does.
- **T2 -- the finite defect = negative index.** On `Pi_2` the non-positive-type defect is a genuine 2-dim
  `Delta`-invariant non-positive subspace (invariance resid `6e-16`, max Krein-Gram eigenvalue `-1.0`), and
  `#non-real(Delta)` maxes at `4 = 2*kappa`. Finite, patchable -- the finite-rank lever with no infinite-rank
  analogue.
- **T3 -- the infinite-rank assembly diverges.** Reusing the repo's exceptional-point mode tower (`W52`/`W84`)
  `H_k=[[i r_k,1],[1,-i r_k]]`, positive metric `eta_k=[[1,-i r_k],[i r_k,1]]`: with `r_k -> 1` (the UV approach
  to the exceptional locus) **every mode is PT-unbroken**, the quasivector count (negative index) diverges
  (`2000 -> 4000` under tower-doubling), **and** the truncated `K`-quasivector patch norm `||metric^{-1}||`
  **doubles** (`2.0e3 -> 4.0e3`) -- **unbounded**, so no bounded `J` in the limit. The **uniform** tower
  (`r_k=0.5`) keeps the patch norm bounded (`2.0 -> 2.0`) -- a bounded `J` assembles, but that is the removable-
  ghost horn.
- **T4 -- EXTENDS is bounded even at rank 2.** A genuinely non-real (PT-broken) `Delta` on `Pi_2` has no
  eta-positive square root (its principal root has `|Im| ~ 2`), so no `J`, and no quasivector repairs it.

**Literature (2026-07-13, read-only).** Shulman 1997 confirmed (`Pi_1`, single quasivector, antilinear
`J`-involution + double commutant; **rank-1 explicit and load-bearing**; no `Pi_kappa` conjugation theorem).
Langer confirmed (on `Pi_kappa` **every** bounded self-adjoint operator is definitizable, spectral function with
finitely many critical points, `kappa`-dim non-positive invariant subspace, `<= kappa` non-real pairs; **no such
theorem at infinite rank**). Krejcirik-Siegl confirmed (bounded metric, **unbounded inverse**, not similar to
self-adjoint). arXiv:2606.13251 (positive-KMS `<=>` quasi-Hermiticity).

Two independent derivations **agree**: **D1** the finite-rank quasivector *count* equals the definitizable finite
defect dimension (patchable); **D2** the infinite-rank assembly *norm* equals the metric-inverse norm (bounded
iff definitizable). Both locate the decision on **definitizability at infinite rank**.

### Persona 5 -- synthesizer (the verdict)

See Sections 2-4.

---

## 2. VERDICT: PARTIAL (EXTENDS under definitizability; OBSTRUCTED for GU)

**A kappa-quasivector construction extends Shulman's modular conjugation `J` to every FINITE `Pi_kappa`
under DEFINITIZABILITY + real-positive spectrum, and is GENUINELY OBSTRUCTED at GU's infinite-rank
`Delta = S^+ S`.**

- **EXTENDS (finite rank, definitizable, real-positive).** On `Pi_kappa` the non-positive-type defect is a
  **finite `kappa`-dimensional** invariant subspace and definitizability is **automatic** (Langer); `kappa`
  quasivectors patch it and, when `spectrum(Delta)` is real-positive (forced for a genuine cyclic-separating
  vector), all four modular properties hold. **Rank 2 is a concrete witness** (`W90` T1). **Caveat:** finite-rank
  definitizable => quasi-Hermitian => the ghost is **removable** -- this is *not* GU's kept-ghost regime, and it
  excludes the non-real (PT-broken) locus (`W90` T4).
- **OBSTRUCTED (infinite rank, GU's genuine `Delta`).** A quasivector patches **one** finite defect unit; the
  count needed = the **negative index = infinity**, so no finite construction reaches GU, and the
  `kappa = infinity` assembly is **bounded iff the metric inverse is uniformly bounded == definitizable**. For
  GU's **real-positive-but-unbounded-inverse** `Delta` (Krejcirik-Siegl; the `W52`/`W53` UV exceptional locus)
  the patch norm **diverges** -- **no bounded `J`**. General Krein-selfadjoint operators at infinite rank are
  **not definitizable** (Langer) -- no spectral function, no eta-positive `Delta^{1/2}`, no `J`. **This is a
  genuine obstruction, not the failure of one device:** *more quasivectors* only means *higher finite rank*, and
  the limit fails exactly where definitizability fails.

**The reach of the quasivector method is CO-EXTENSIVE WITH DEFINITIZABILITY.** It extends precisely as far as
definitizability holds (all finite `kappa`) and fails exactly where it fails (`kappa = infinity`, unbounded metric
inverse). **It is not an independent route around the residual.**

---

## 3. Outcome in terms of the shared infinite-rank definitizability residual (Branch 3 / Branch 5)

**The pure-math quasivector route does NOT independently resolve the frontier. It reduces, with no remainder, to
the shared residual:**

> **RESIDUAL:** does GU's Krein modular operator `Delta = S^+ S` admit a **definitizing polynomial** `p`
> (`p(Delta)` eta-nonnegative) equivalently a **uniformly bounded metric** across the mode tower (bounded metric
> with **bounded inverse**)?
> - **YES (definitizable):** the kappa-quasivector `J` assembles -> the frontier is **resolvable** -- but the
>   ghost is **removable** (quasi-Hermitian; keep-and-grade trivial). This is `W84`'s **HORN Q**.
> - **NO (non-definitizable):** no bounded quasivector `J` exists -> the direct pure-math route is **dead**; hand
>   to **Branch 3's relative/algebraic modular skeleton** (which may bypass the eta-positive square root via a
>   relative modular operator / spatial derivative) or **Branch 5's no-go**. This is `W84`'s **HORN K**.

**Branch 2 does not settle the residual for GU** -- the finite toy cannot reach it, exactly as `W77`/`W84` found.
The repo-native **indication** (`W52`/R1 `||C|| -> infinity` at the exceptional locus; `W53` places that locus at
the free UV FP the AS flow approaches) points to **non-definitizable in the UV**, i.e. GU on the **OBSTRUCTED
(HORN K)** side. **Indication, not proof.**

**What this contributes to the wave.** Branch 2 closes the *direct* pure-math option: the answer to "is the
rank-1 restriction the failure of one device?" is **no** -- a `kappa`-quasivector genuinely extends Shulman, but
**only** across the definitizable (finite-rank / uniformly-bounded-metric) regime, and GU's genuine object sits
outside it (indicated). So the quasivector route cannot, by itself, turn the observer conjecture
conditional->theorem; it **hands the definitizability residual unchanged to Branch 3** (whose relative/algebraic
route is the remaining hope of building `J`-equivalent modular data without an eta-positive square root) and
**sharpens the target for Branch 5** (a definitizability no-go for GU's `Delta` would be the first completed
no-go on this leg).

---

## 4. Two-derivation discipline (they agree) + self-critical pass

**Derivation D1 (finite-rank: quasivector count = definitizable finite defect).** On `Pi_kappa` the
non-positive-type defect of `Delta` is a finite `kappa`-dimensional invariant subspace (Langer/Pontryagin);
`kappa` quasivectors patch it; with real-positive spectrum an eta-positive `Delta^{1/2}` and `J` follow. (`W90`
T1/T2.) The count needed is exactly the negative index.

**Derivation D2 (infinite-rank: assembly norm = metric-inverse norm).** The `K -> infinity` quasivector patch
assembles into a bounded Krein-antiisometry `J` iff the truncated patch norm `||metric_K^{-1}||` stays bounded,
i.e. iff the metric is uniformly bounded == definitizable. For `r_k -> 1` (unbounded inverse) it diverges: no
bounded `J`. (`W90` T3; Krejcirik-Siegl.)

**They agree:** both put the decision on **definitizability at infinite rank** -- D1 is the "how many quasivectors
/ is the defect finite" face, D2 is the "does the assembly stay bounded" face. Two faces of the finite-rank-only
implication *PT-unbroken (real-positive) => definitizable/quasi-Hermitian*, which is **false** at infinite rank.

**Self-critical pass (adversary, both directions).**
- *Against OBSTRUCTED:* "a cleverer multi-quasivector could stay bounded." Answered: bounded assembly `<=>`
  bounded metric inverse `<=>` definitizable; Krejcirik-Siegl exhibits a real-spectrum operator whose metric
  inverse is provably unbounded, and the same fact makes the ghost genuinely kept (HORN K). Uniform boundedness
  (the only escape) is HORN Q, where the ghost is removable -- not a genuine-ghost extension.
- *Against EXTENDS(def):* "the rank-2 success is type-I / positive-`Delta` smuggling." Conceded in scope: it
  proves the route works *where definitizability holds* and is the removable-ghost regime; it does not claim GU.

**The single load-bearing assumption.** That **finite negative index (Pontryagin `Pi_kappa`) definitizability**
-- which makes the defect finite and the quasivector patch bounded -- **persists at infinite rank / type III**.
It is a **finite-rank theorem** (Langer) and is **false** for general self-adjoint operators on infinite-rank
Krein spaces (Langer's non-theorem; Krejcirik-Siegl). GU's region algebra is infinite rank, so it cannot be
assumed -- and that is exactly where the quasivector route stops.

---

## 5. Confidence grade and what would move it

- **kappa-quasivector EXTENDS at finite rank under definitizability + real-positive (rank-2 witness):** **high**
  (exact, `W90` T1/T2; Langer `Pi_kappa` definitizability; Shulman `Pi_1`).
- **Finite-rank extension has a removable ghost:** **high** (`W84` T1; quasi-Hermitian).
- **Infinite-rank quasivector assembly is unbounded when the metric inverse is unbounded (no bounded `J`):**
  **high** -- Krejcirik-Siegl is a published theorem; the `W90` tower is an exact finite surrogate.
- **The quasivector reach is co-extensive with definitizability (route reduces to the shared residual, does not
  independently resolve it):** **high** (D1 + D2 agree; Langer's finite-rank-only theorem).
- **GU sits on the non-definitizable (OBSTRUCTED / HORN K) side:** **medium** -- an *indication* from
  `W52`/R1 + `W53`, not a proof that the infinite-mode metric inverse is unbounded.
- **VERDICT = PARTIAL:** **medium-high.** That the quasivector route extends only across definitizability and
  reduces to the residual is rigorous (theorem-backed); *which* side GU lands on is the residual open.

**What would move it most:** (a) a **definitizability criterion** for GU's region-algebra `Delta = S^+ S` at
infinite rank -- does a definitizing polynomial / uniformly bounded metric exist? (converts the residual into a
decidable test, and settles HORN Q vs HORN K); (b) **Branch 3's** relative/algebraic modular operator giving
`J`-equivalent data **without** an eta-positive square root -- the only route that could cross a *non-definitizable*
residual; (c) a proof that GU's spin-2 modular tower is **non-uniformly** PT-unbroken into the UV (would confirm
non-definitizability and hand the leg to Branch 5's no-go).

---

## 6. What this does NOT do

No GU claim-status, `CANON.md`, `RESEARCH-STATUS.md`, verdict, or public-posture change. No external action; all
citations are read-only literature. The conjecture remains a conjecture; H61/H61a remain **OPEN** (the residual
sharpened: the direct pure-math quasivector route does not independently resolve it -- its reach is co-extensive
with definitizability, and it reduces, unchanged, to the shared infinite-rank definitizability residual that
Branch 3's algebraic route must confront). The deliverable is: Shulman's `Pi_1` construction stated with the two
places rank 1 is used (single-quasivector patch + implicit definitizability); the concrete rank-2 kappa-quasivector
result (EXTENDS in the definitizable/real-positive regime, all four modular properties; obstructs on the non-real
locus); the genuine infinite-rank obstruction (quasivector count + assembly norm both diverge for an unbounded
metric inverse); and the reduction to the shared definitizability residual with the repo-native indication that GU
is on the obstructed side. Reproducible: `tests/W90_shulman_pi_kappa.py` (5/5, exit 0).
