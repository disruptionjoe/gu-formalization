---
artifact_type: exploration
status: exploration (Branch 5 of the observer-conjecture frontier wave; ADVERSARIAL no-go / rigidity branch; PRESENT-not-decide; 5-persona inline team; deterministic test)
created: 2026-07-13
hypothesis: H61 / H61a (the observer-conjecture Krein-TT critical path) -- the ADVERSARIAL face
conjecture: "the source action IS the observer (CONJECTURE-source-action-is-the-observer-2026-07-11.md)"
branch: "Branch 5 (adversarial no-go / rigidity) -- try to PROVE that NO type-III Krein Tomita-Takesaki modular conjugation J exists for a NON-DEFINITIZABLE ghost (HORN K); i.e. that Front A (GU's PHYSICAL modular realization of the observer firewall) is IMPOSSIBLE. Blind to the constructive branches (1/2/3). Present the strongest no-go, tagged by strength; the orchestrator weighs it against the constructive branches."
title: "BRANCH 5 ADVERSARIAL NO-GO. VERDICT = STRONG ARGUMENT, NOT a complete theorem. The strongest honest no-go: assembling Mostafazadeh (finite-dim positive-KMS <=> quasi-Hermiticity) + Krejcirik-Siegl (infinite-rank real-positive spectrum => bounded metric, UNBOUNDED inverse => NOT quasi-Hermitian, only quasi-similar) + Langer (Krein-selfadjoint operators are not generally definitizable; a spectral function / eta-positive square root needs definitizability) gives a RIGOROUS no-go for the SPECIFIC positive-Delta / vacuum-polar route: a non-definitizable Delta has no eta-positive Delta^{1/2}, so the vacuum Tomita operator S has no polar decomposition S = J Delta^{1/2} with a BOUNDED Krein-antiisometry J -- concretely J = S Delta^{-1/2} is UNBOUNDED (||Delta^{-1/2}|| -> inf on the r_k->1 tower). CRUX (Task 2): is non-definitizability a GENUINE obstruction to ANY J, or only to that route? Answer: it is genuine for any J tied to the modular flow through a SINGLE GLOBAL metric operator -- the vacuum-polar J (rigorous) AND any relative-to-a-GLOBAL-state J (strong: the transported J_phi = Theta^{-1/2} J_H Theta^{1/2} is unbounded because GNS and Krein reps are only quasi-similar). But it is NOT an obstruction to a BARE-ALGEBRAIC J (W67 built one on a type-I toy WITHOUT a positive Delta), and -- the decisive honest gap -- NOT provably an obstruction to a SECTORIAL relative J: unbounded-inverse is a property of the WHOLE tower (sup over all modes); Branch 3's relative-to-a-state J may localize to a definitizable Pi_kappa SUB-SECTOR where the metric is bounded and a bounded J exists, EVADING the global obstruction. This branch is blind to Branch 3's exact construction and cannot decide whether the firewall needs the whole tower or a sub-sector, so the no-go is INCOMPLETE with that NAMED GAP. CONSEQUENCE (present, not decide): Front A's PHYSICAL modular realization VIA THE VACUUM is walled (rigorous, HORN K); Front A as a WHOLE is NOT provably dead (the algebraic/relative-sector route is open, so the constructive branches LIVE); and the ABSTRACT Lawvere theorem STANDS regardless -- it needs only J^2=1 on the 2-element grading labels (the bare swap), never the flow-tied Delta^{1/2}."
grade: "exploration / one rigorous piece (vacuum-polar no-go: Langer + Krejcirik-Siegl, theorem-grade), one strong piece (global-relative no-go), one honest NAMED GAP (sectorial/definitizable-subsector relative J), all encoded in tests/W93_adversarial_nogo.py (6/6, numpy-only, exit 0) on the repo's W52/W84 exceptional-point tower. The no-go's LOGICAL core (non-definitizable => no vacuum-polar/global-flow-tied J) is theorem-grade; its APPLICATION to GU is conditional on HORN K (W87, truncation-conditional) and on extending arXiv:2606.13251 (positive-KMS <=> quasi-Hermitian) from finite to infinite rank. No canon, RESEARCH-STATUS, CANON, claim-status, verdict, or public-posture change. The conjecture remains a conjecture; H61/H61a remain OPEN."
depends_on:
  - explorations/rankN-krein-tt-for-gu-2026-07-11.md
  - explorations/horn-k-vs-q-gu-ghost-2026-07-11.md
  - explorations/H61-krein-tt-first-swing-2026-07-11.md
  - explorations/path5-branchA-krein-modular-conjugation-2026-07-11.md
  - explorations/path5-branchD-lawvere-no-closure-2026-07-11.md
  - explorations/CONJECTURE-source-action-is-the-observer-2026-07-11.md
  - GEOMETER-VS-PHYSICS-OBJECTS.md
  - tests/W84_rankN_krein_tt.py
  - tests/W87_horn_k_vs_q.py
  - tests/W74_H61_krein_tt_swing.py
  - tests/W67_path5_A_krein_modular.py
scripts:
  - tests/W93_adversarial_nogo.py
external_refs:
  - "D. Krejcirik & P. Siegl, On the metric operator for the imaginary cubic oscillator, Phys. Rev. D 86 (2012) 121702(R), arXiv:1208.1866 -- bounded metric with UNBOUNDED inverse; eigenvectors complete but not a Riesz basis; NOT similar to self-adjoint, only quasi-similar"
  - "H. Langer, Spectral functions of definitizable operators in Krein spaces -- spectral function (hence eta-positive square root / functional calculus) under DEFINITIZABILITY; Pontryagin Pi_kappa definitizable; no such theorem for general self-adjoint operators on infinite-rank Krein spaces"
  - "A. Mostafazadeh, pseudo-Hermitian QM -- finite-dim: diagonalizable + real spectrum <=> quasi-Hermitian (a positive-definite, in finite dim automatically bounded-invertible, metric exists)"
  - "arXiv:2606.13251, KMS conditions for non-Hermitian systems -- positivity of the biorthogonal thermal state <=> quasi-Hermiticity (finite-dim)"
  - "V. S. Shulman, Rev. Math. Phys. 9 (1997) 749 -- the rank-1 (Pi_1) quasivector Tomita theorem; no Pi_kappa (kappa>=2) conjugation theorem exists"
---

# Branch 5 -- the adversarial no-go / rigidity swing (present, do not decide)

**Role.** Branch 5 is the ADVERSARIAL face of the observer-conjecture frontier. Blind to the
constructive branches (1/2/3), it tries to **PROVE Front A is IMPOSSIBLE**: that NO type-III Krein
Tomita-Takesaki modular conjugation `J` exists for a **non-definitizable** ghost (the HORN K
regime, W84/W87). If the no-go is genuine and complete, GU's *physical* modular realization of the
observer firewall is walled forever (a real, clean result -- though the abstract Lawvere theorem,
which needs only `J^2=1` on grading labels, would stand regardless). If the algebraic/relative route
evades it, the no-go has a named gap and the constructive branches live. **This branch PRESENTS the
strongest no-go it can, tagged by strength, and does NOT decide** -- the orchestrator weighs it.

**A modular conjugation** here means an antilinear `J` with: (1) `J^2 = 1`; (2) `J M J = M'`; (3) `J`
a **Krein-antiisometry** (`[Jx,Jy] = conj([x,y])`, `[x,y] = <x, eta y>`); (4) **modular covariance**
`S = J Delta^{1/2}`, `J Delta J = Delta^{-1}`, where `Delta = S^+ S` is the Krein modular operator
(`S(aOmega) = a^+ Omega`, `a^+ = eta a* eta`).

**Artifacts:** this file + deterministic `tests/W93_adversarial_nogo.py` (6/6, numpy-only, exit 0).
**Not committed. Not a claim-status change.** Exploration-grade.

---

## 0. Construction forks (GEOMETER-VS-PHYSICS-OBJECTS.md discipline)

| Object | Construction used | Load-bearing here |
|---|---|---|
| **The algebra** | GU-native indefinite region `*`-algebra on the **Krein space** (`[x,y]=<x,eta y>`, `eta` = C-grading = fundamental symmetry), **infinite** rank of indefiniteness (`(+64,-64)` per point, a QFT region algebra). NOT a positive-Hilbert-subspace algebra. | The no-go is a **genuine-Krein / infinite-rank** statement; it deliberately does NOT assume away the ghost (that would be HORN Q, the removable case). |
| **The modular operator** | the **Krein** `Delta = S^+ S`; its **definitizability** is the hinge. Under the adversarial hypothesis `Delta` is **non-definitizable** (the Krejcirik-Siegl class: bounded metric, unbounded inverse). | This is the HORN K regime the sibling swings (W84/W87) argue GU sits on (truncation-conditional). The no-go is what HORN K *costs* Front A. |
| **The conjugation `J`** | the **antilinear** modular conjugation, distinguished into three constructions (Section 2): **(i) vacuum-polar** (covariance-tied), **(ii) global-relative** (relative to a positive state tied to the whole tower by one metric), **(iii) bare-algebraic / sectorial-relative**. | Naming these three is the whole result: the no-go bites (i) rigorously and (ii) strongly, but NOT (iii). Defaulting to "one J" would either overstate (kill all) or understate (kill none). |

**The one fork this swing turns on: "the modular conjugation" is not a single object.** The physics
default treats `J` as *the* Tomita conjugation (route i). But the observer conjecture's *algebraic*
re-founding (H61 §5; Branch A/W67) admits a **bare** `J` with no positive-`Delta` tie, and Branch 3
proposes a `J` **relative to a selected state**. We do NOT default to the vacuum-polar reading; the
no-go's completeness depends entirely on which construction the firewall actually needs.

---

## 1. Five-persona team (inline, sequential, single context)

### Persona 1 -- no-go / rigidity theorist (assemble the strongest no-go)

**The assembly (Task 1).** Three imported facts chain into a clean no-go for the positive-`Delta`
route:

- **[M] Mostafazadeh (finite dim).** Diagonalizable + real-positive spectrum `<=>` quasi-Hermitian:
  a positive-definite metric `Theta` exists (bounded-invertible automatically in finite dim), and
  positive-KMS `<=>` quasi-Hermiticity. *In finite dim, PT-unbroken gives you everything.*
- **[KS] Krejcirik-Siegl (PRD 86 (2012) 121702).** At **infinite rank**, real-positive spectrum
  (eigenvectors **complete but not a Riesz basis**) admits only a bounded metric with **UNBOUNDED
  INVERSE** -- so the operator is **not similar** to a self-adjoint one, only **quasi-similar**;
  **not quasi-Hermitian.** *The finite-dim equivalence [M] FAILS at infinite rank.*
- **[L] Langer.** A spectral function -- hence a functional calculus, hence an **eta-positive square
  root** `Delta^{1/2}` -- exists for an eta-selfadjoint `Delta` **under definitizability**; automatic
  on Pontryagin `Pi_kappa` (finite rank), **absent** for general self-adjoint operators on
  infinite-rank Krein spaces.

**Assembled -- THEOREM (vacuum-polar route).** *Let `Delta = S^+ S` be the Krein modular operator on
an infinite-rank Krein space, with real-positive spectrum but **non-definitizable** (KS class:
bounded metric, unbounded inverse). Then: (a) `Delta` has no eta-positive square root `Delta^{1/2}`
(Langer -- no spectral function); (b) hence the vacuum `S` admits no polar decomposition
`S = J Delta^{1/2}` with `J` a **bounded** Krein-antiisometry; (c) hence there is no modular
conjugation built from the vacuum, and no positive KMS state ([M] denied at the level it can reach).*
Concretely (`W93` T2): on the `r_k -> 1` tower, `J = S Delta^{-1/2}` has `||J|| = 1/sqrt(1-r_k) ->
inf`. **A modular conjugation must be a bounded (anti)isometry; an unbounded `J` is not one.** So the
vacuum-polar `J` **does not exist**. This piece is **rigorous** (theorem-grade), modulo the two
imported conditionals flagged by the referee.

### Persona 2 -- math referee (grade the no-go's strength)

**Ruling 1 -- the vacuum-polar no-go is theorem-grade, but not unconditional.** The logic
(non-definitizable `=>` no eta-positive `Delta^{1/2}` `=>` no bounded vacuum-polar `J`) is a genuine
theorem: Langer's non-theorem for general Krein-selfadjoint operators plus Krejcirik-Siegl's
published example are exactly what it needs. **But** it inherits two conditionals: (i) that GU's
`Delta` really is **non-definitizable** (HORN K) -- which W87 grades HIGH within the operative
truncation but MEDIUM unconditionally (a full FRG lifting `f_2^2* > 0` would flip to HORN Q, where
the no-go evaporates and the ghost is removable); (ii) that arXiv:2606.13251's positive-KMS `<=>`
quasi-Hermitian, used to deny a positive KMS state, **extends from finite to infinite rank** (it is
proved finite-dim). So: **theorem on the abstract route; conditional in its application to GU.**
Grade: **STRONG ARGUMENT, theorem-grade on the vacuum-polar route.**

**Ruling 2 -- the no-go is NOT a blanket "no J ever."** The referee refuses to let Persona 1 inflate
this to "no modular conjugation exists." Two escapes are on the table (Personas 3-4): a
**bare-algebraic** `J` that never invokes `Delta^{1/2}` (W67 built one), and a **relative** `J` tied
to a selected state. The vacuum-polar theorem says nothing about the bare one and only *conditionally*
about the relative one. **The referee requires the no-go be presented as bounding the FLOW-TIED
routes, not all `J`.**

**Ruling 3 -- the honest gate.** Whether non-definitizability genuinely walls Front A reduces to:
**does the firewall's `J` have to be tied to the modular flow through a single global metric?** If
yes (routes i, ii), the no-go bites. If a sectorial/relative `J` suffices (route iii), it does not.
That is a question about the *physics requirement*, which this branch cannot settle. **The no-go is
therefore INCOMPLETE with a named gap; grade the completeness MEDIUM.**

### Persona 3 -- steelman-of-construction (try the algebraic/relative route against the no-go)

I now genuinely try to **build a `J` that evades** the no-go -- Branch 3's idea, honestly pressed.

- **Attempt A -- bare-algebraic `J` (no covariance tie).** Drop axiom (4). W67/H61 built a `J` on a
  type-I toy satisfying `J^2=1`, `JMJ=M'`, Krein-antiisometry **IFF the grading is
  reflection-symmetric** (`[J_refl, eta]=0`) -- **with no positive `Delta` anywhere**. So the bare
  axioms **do not require definitizability**. **Verdict: the bare route EVADES the no-go** -- but it
  also drops the modular *flow* (Bisognano-Wichmann `Delta^{it}` = boost), so it is not yet the full
  firewall the conjecture wants. It shows definitizability is a constraint on the *flow tie*, not on
  the conjugation *per se*.

- **Attempt B -- relative-to-a-GLOBAL-state `J`.** Select a positive faithful state `phi`, do GNS,
  take the standard (bounded) conjugation `J_H`, transport back: `J_phi = Theta^{-1/2} J_H
  Theta^{1/2}`, where `Theta` is the metric operator relating the GNS and Krein representations. If
  `Theta` were bounded-invertible the two reps would be **similar** (quasi-Hermitian) -- but that is
  exactly HORN Q / definitizable, contradiction. Under non-definitizability `Theta` has **unbounded
  inverse** (KS), the reps are only **quasi-similar**, and `||J_phi|| = sqrt(cond Theta) -> inf`
  (`W93` T3). **Verdict: the GLOBAL relative route is ALSO obstructed** -- the transported `J_phi` is
  unbounded, not a genuine Krein-antiisometry. This is the strong extension of the no-go: it kills
  not just the vacuum but *any* positive state tied to the whole tower.

- **Attempt C -- relative-to-a-state `J` on a definitizable SUB-SECTOR (the one that evades).**
  Here is the honest hole in my own no-go. Unbounded-inverse is a property of the **whole tower**
  (`sup` over *all* modes, `r_k -> 1`). A selected state's GNS representation need not see the whole
  tower -- it can be supported on a **`Pi_kappa` (finite-rank) sub-sector**, where the metric is
  **bounded** and a **bounded `J` exists** (`W93` T4: the first `kappa` modes give `sup
  ||Delta^{-1/2}|| < inf`). If the observer firewall only needs to grade a sub-sector -- or if
  Branch 3's relative construction localizes to one -- then **the global obstruction does not fire,
  and route C EVADES the no-go.** I cannot rule this out: I am blind to Branch 3's exact construction,
  and nothing in the vacuum-polar or global-relative arguments forces the firewall to be global.
  **Verdict: route C is a GENUINE named gap. My no-go is NOT complete.**

**Steelman's honest report:** the no-go survives the bare route (evades but loses the flow) and the
global-relative route (obstructed) -- **but it does NOT survive the sectorial/definitizable-subsector
relative route.** That route is the named gap, and it keeps the constructive branches alive.

### Persona 4 -- cross-checker (independent recomputation + literature)

- **Recomputed the three routes on the W52/W84 tower** (`W93`, exact, numpy-only). (i) vacuum-polar
  `||J|| = 1/sqrt(1-r)` grows `63 -> 89` under tower doubling; (ii) global-relative `||J_phi|| =
  sqrt(cond Theta)` grows `89 -> 126`; (iii) `Pi_200` sub-sector stays bounded (`sup ||Delta^{-1/2}||
  = 14.2`, finite). The bounded-vs-unbounded split is detected by growth under doubling, not an
  arbitrary threshold -- same discipline as W84 T3. **All three confirmed.**
- **The finite-rank control (T1):** at `r=0.5` a bounded `J` exists (`||J|| = 1.41`), the ghost is
  removable. So the no-go is **specifically infinite-rank / non-definitizable**, not a blanket claim
  -- an important honesty check the adversary must not skip.
- **Literature (read-only, 2026-07-13).** Krejcirik-Siegl (unbounded metric inverse, quasi-similar
  not similar): the load-bearing fact for routes (i)/(ii). Langer (definitizability needed for a
  spectral function; `Pi_kappa` automatic, general infinite-rank not): the "no `Delta^{1/2}`" step
  AND the sub-sector escape (T4) both trace to the *same* Langer dichotomy -- `Pi_kappa` is
  definitizable, the full tower is not. Mostafazadeh / arXiv:2606.13251 (positive-KMS `<=>`
  quasi-Hermitian, **finite-dim**): supports "no positive KMS state" but only conditionally at
  infinite rank -- the referee's flagged conditional. Shulman `Pi_1`: a rank-1 conjugation theorem
  exists, consistent with route C's sub-sector escape being real at finite `kappa`.
- **One correction to the adversary's own prior:** the global-relative no-go (route ii) is *stronger*
  than the vacuum-polar one -- it kills *any* global positive state, not just the vacuum -- but it is
  *strong argument*, not theorem, because it assumes the relative `J` is transported through a single
  global metric. The sub-sector escape (route C) is exactly the failure of that assumption. **The
  no-go and its gap are two faces of the Langer `Pi_kappa`-vs-infinite-rank dichotomy.**

### Persona 5 -- synthesizer (the verdict)

See Sections 2-4.

---

## 2. VERDICT: STRONG ARGUMENT, NOT a complete theorem (present, do not decide)

**Three constructions of `J`, three fates:**

| Route | What it is | Fate under non-definitizability | Strength |
|---|---|---|---|
| **(i) vacuum-polar** | `S = J Delta^{1/2}`, covariance-tied | `J = S Delta^{-1/2}` **UNBOUNDED** -- no eta-positive `Delta^{1/2}` (Langer) | **RIGOROUS no-go** |
| **(ii) global-relative** | `J_phi = Theta^{-1/2} J_H Theta^{1/2}`, one global metric | `||J_phi|| = sqrt(cond Theta) -> inf` -- reps only quasi-similar (KS) | **STRONG no-go** |
| **(iii) bare / sectorial-relative** | `J^2=1, JMJ=M'`, Krein-antiisometry, no global flow tie | bare: EXISTS (W67, no `Delta`); sectorial: bounded on a `Pi_kappa` sub-sector | **EVADES -- named gap** |

**Is non-definitizability a GENUINE obstruction to ANY `J`, or only to the positive-Delta route?**
**Genuine for any `J` tied to the modular flow through a SINGLE GLOBAL metric operator** (routes i and
ii) -- this is more than "the specific positive-Delta route": it kills the vacuum polar decomposition
*and* every global positive-state relative construction, because both need a bounded-invertible metric
that non-definitizability denies (KS: only quasi-similar). **But NOT genuine for a bare-algebraic `J`
(exists without a positive `Delta`) and NOT provably genuine for a SECTORIAL/definitizable-subsector
relative `J`.** The obstruction is exactly the Langer `Pi_kappa`-vs-infinite-rank dichotomy: it fires
on the *whole tower*, not on a definitizable sub-sector.

**Is the no-go COMPLETE?** **No.** Named gap = **the algebraic/relative-to-a-state `J` on a
definitizable (`Pi_kappa`) sub-sector** (Persona 3, route C). Unbounded-inverse is a `sup`-over-all-
modes property; a firewall `J` that needs only boundedly-many modes escapes it. This branch is blind
to Branch 3's exact construction and cannot decide whether the firewall needs the whole infinite tower
or a sub-sector, so it **presents the gap and does not close it.**

---

## 3. The two consequences (present, do not decide)

**If the no-go were complete and genuine (it is not, but stating the clean outcome):** Front A would
be **dead** -- GU's *physical* modular realization of the observer firewall walled forever at
type-III definitizability, a real and clean result. **The abstract Lawvere theorem (Branch D/W70)
would STAND regardless:** it needs only `J^2=1` on the 2-element grading **labels** (the bare swap,
fixpoint-free), which needs no eta-positive `Delta^{1/2}`, no definitizability, no bounded metric
(`W93` T5). The "value unforceable in principle" engine is untouched even by a complete physical
no-go -- the observer *mechanism* survives; only its *physical modular realization* is walled.

**What actually holds (the honest landing):** the no-go is **STRONG but INCOMPLETE.**
- Front A's realization **via the vacuum** (route i) is **walled -- rigorously** (Langer +
  Krejcirik-Siegl), conditional on HORN K (W87).
- Front A's realization **via any global positive state** (route ii) is **walled -- strongly.**
- Front A's realization **via a sectorial/relative `J`** (route iii) is **OPEN** -- the named gap.
  **So Front A as a WHOLE is NOT provably dead, and the constructive branches (which this branch is
  blind to) LIVE through this gap.**

**The tension, stated plainly (the same one W84/W87 found, from the adversary's side).** The only way
non-definitizability could be *dodged* wholesale is HORN Q (quasi-Hermitian) -- but that removes the
ghost and deflates the firewall to a trivial grading. Under HORN K (genuine ghost, the interesting
case) the vacuum and global-relative routes are genuinely walled. **The adversary's strongest honest
result is: "the flow-tied physical `J` is walled under HORN K; escape requires either a bare/sectorial
`J` (the gap) or HORN Q (ghost removable)."** The no-go does not kill the conjecture; it **sharpens
the constructive burden** onto the sectorial/relative route.

---

## 4. Two-piece discipline (rigorous + strong) + self-critical pass

**Piece R1 (rigorous, theorem-grade) -- vacuum-polar.** Non-definitizable `Delta` has no eta-positive
`Delta^{1/2}` (Langer); so `J = S Delta^{-1/2}` is unbounded (`W93` T2, `||J|| = 1/sqrt(1-r) -> inf`);
so no bounded vacuum-polar Krein-antiisometry. Modulo HORN K (W87) and the KS-class identification.

**Piece R2 (strong argument) -- global-relative.** Any positive state tied to the whole tower by one
metric `Theta` has `Theta` with unbounded inverse (KS); the transported `J_phi = Theta^{-1/2} J_H
Theta^{1/2}` is unbounded (`W93` T3). Modulo the assumption that the relative `J` is *global* -- whose
failure is exactly the gap.

**They agree** on the flow-tied routes and both trace to the KS/Langer infinite-rank pathology. R1 is
the "no square root" face; R2 is the "quasi-similar, not similar" face.

**Self-critical pass (steelman-against-self, honestly).**
- *Against the no-go:* "a bare or sectorial `J` evades you." **Conceded** -- the bare `J` exists
  (W67, no `Delta`), and a `Pi_kappa` sub-sector admits a bounded `J` (`W93` T4). The no-go bounds
  the *global flow-tied* routes only. **This is the named gap; I do not paper over it.**
- *Against the evasion:* "a bare `J` drops the modular flow (Bisognano-Wichmann), so it is not the
  full firewall." **True** -- the bare route buys evasion at the cost of the flow, so it is not a free
  win for the constructive side either. The sectorial-relative route (C) is the one that might get
  *both* flow and evasion; whether it does is the open question this branch cannot close.
- *The single load-bearing assumption:* that **the firewall's `J` must be tied to the modular flow
  through a single global metric operator.** If TRUE, the no-go is complete (Front A dead under HORN
  K). If FALSE (a sectorial/relative `J` suffices), the gap is real. **This branch presents both and
  does not decide** -- deciding needs Branch 3's construction, which it is blind to.

---

## 5. Confidence grade and what would move it

- **Vacuum-polar no-go (route i): non-definitizable => unbounded `J`:** **HIGH** (exact, `W93` T2;
  Langer + Krejcirik-Siegl) -- theorem-grade on the abstract route.
- **Global-relative no-go (route ii): transported `J_phi` unbounded:** **MEDIUM-HIGH** (exact on the
  tower, `W93` T3; assumes a single global metric).
- **Non-definitizability is a GENUINE obstruction to global-flow-tied `J`:** **MEDIUM-HIGH.**
- **The named gap is real (sectorial/subsector `J` evades):** **HIGH** (exact, `W93` T4; the Langer
  `Pi_kappa` escape).
- **The no-go is INCOMPLETE:** **HIGH** -- follows directly from the gap being real.
- **Abstract Lawvere theorem stands regardless:** **HIGH** (`W93` T5; label swap needs no `Delta^{1/2}`).
- **Application to GU (HORN K):** **MEDIUM** -- inherits W87's truncation-conditionality.

**What would move it most (names what would COMPLETE or KILL the no-go):** (a) a proof that the
observer firewall's `J` **must** be global / flow-tied (would CLOSE the gap -> Front A dead under HORN
K -- a complete no-go); (b) Branch 3's explicit **sectorial/relative construction** of a bounded `J`
on a definitizable sub-sector satisfying `JMJ=M'` + Krein-antiisometry + the flow (would REALIZE the
gap -> the no-go is defeated, Front A lives); (c) an infinite-rank extension of arXiv:2606.13251
(would firm the "no positive KMS state" conditional); (d) the W87 deciding computation (full FRG
`beta_{f_2^2}` with graviton loops -- `f_2^2* = 0` firms HORN K and the no-go's premise; `f_2^2* > 0`
flips to HORN Q where the whole no-go evaporates and the ghost is removable).

---

## 6. What this does NOT do

No GU claim-status, `CANON.md`, `RESEARCH-STATUS.md`, verdict, or public-posture change. No external
action; all citations are read-only literature. The conjecture remains a conjecture; H61/H61a remain
**OPEN**. This branch **presents, does not decide.** The deliverable is: the strongest honest
adversarial no-go (RIGOROUS for the vacuum-polar route, STRONG for the global-relative route), the
determination that non-definitizability is a **genuine** obstruction to any **global-flow-tied** `J`
but **not** to a bare or **sectorial/definitizable-subsector relative** `J`, the honest verdict that
the no-go is **INCOMPLETE** with that **named gap** (so Front A is not provably dead and the
constructive branches live), and the note that the **abstract Lawvere theorem stands regardless.**
Reproducible: `tests/W93_adversarial_nogo.py` (6/6, exit 0).
