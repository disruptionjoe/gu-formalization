---
artifact_type: exploration
status: exploration (directed firm-up swing; 5-persona inline team; literature check read-only + deterministic test)
created: 2026-07-13
hypothesis: H61 / H61a (the observer-conjecture sectorial closing) -- condition (iii): the two W54/W91-grade facts
conjecture: "the source action IS the observer (CONJECTURE-source-action-is-the-observer-2026-07-11.md)"
branch: "Condition (iii) of the sectorial closing (W94). The sectorial closing uses two W54/W91-grade facts: (a) the firewall grading (metric / C-operator) is NON-LOCAL but EXPONENTIALLY LOCALIZED at the ghost scale ~1/m (W54 Result 3, FREE-CASE theorem + first-order strong-argument); (b) the observer's value-selection half (modular flow + Connes cocycle + section map, W91) is POSITIVITY-FREE. Firm BOTH from free/one-loop to ALL ORDERS / the interacting case, or precisely identify the frontier."
title: "CONDITION (iii) = (b) PARTIALLY. The positivity-free VALUE-SELECTION half (flow + Connes cocycle + section map) is ALL-ORDERS-RIGOROUS: it is an automorphism-level / operator-algebra object (Connes RN cocycle theorem, exact for arbitrary type-III vN algebras; Gottschalk Krein modular flow) that carries NO loop-truncation and does NOT degrade order-by-order -- confirmed by the cocycle identity holding EXACTLY at every coupling. The EXP-LOCALIZATION ~1/m is UPGRADED from W54's first-order strong-argument to a MASS-SCALE (analyticity-strip = mass-gap) argument: every all-orders metric/grading symbol is a rational function of the constituent square roots om_i = sqrt(k^2+m_i^2), whose ONLY singularities are the branch points k=+-i m_i (a sum of positive om's never vanishes), so the nearest singularity to the real axis is at |Im k| = min_i m_i = the mass gap AT EVERY ORDER -- the same mechanism as massive-QFT exponential clustering (rate = mass gap, all-orders / non-perturbative). Along the AF flow the ghost gap stays > 0 at every finite scale, closing ONLY at the free UV endpoint (= the exceptional locus W94 already handles). This STRENGTHENS the first-order argument but is NOT an unconditional all-orders theorem: it is CONDITIONAL on the interacting ghost pole staying REAL-massive (PT-unbroken / definitizable; a complex Lee-Wick pair would move the branch point off the imaginary axis), and the all-orders no-LOCAL-metric (non-entirety) proof proper stays first-order. PRECISE RESIDUAL: the reality of the interacting ghost spectrum = the SAME infinite-rank definitizability residual W91/W94 reduce to -- firming (iii) COLLAPSES onto the already-isolated residual and opens NO new interacting-metric frontier; it additionally inherits the one-loop-truncation grade of the AF ghost-mass running (W53/Result-2)."
grade: "exploration / one all-orders-rigorous result (the positivity-free value-selection half is algebraic / non-perturbative, no truncation limit -- Connes RN cocycle theorem + Gottschalk flow) + one strengthened-but-conditional result (exp-localization mass-scale-protected at every finite scale, conditional on real ghost spectrum) + the identification that firming (iii) reduces to the shared definitizability residual (no new frontier). Encoded in tests/W97_cond_iii_all_orders.py (6/6, numpy-only, exit 0). Literature read-only (2026-07-13): Connes RN cocycle theorem (exact for arbitrary type-III vN algebras); massive-QFT exponential clustering / cluster theorem (rate = mass gap, all-orders / Araki-Hepp-Ruelle, OS reconstruction). No canon, RESEARCH-STATUS, CANON, claim-status, verdict, or public-posture change. The conjecture remains a conjecture; H61/H61a remain OPEN with condition (iii) firmed to all-orders-flow-half + mass-scale-protected-localization, residual localized to the shared definitizability question."
depends_on:
  - explorations/sectorial-relative-j-2026-07-11.md
  - explorations/branch3-algebraic-modular-skeleton-2026-07-11.md
  - explorations/path2-wave2-target3-no-local-positive-metric-2026-07-11.md
  - explorations/path2-branchB-pt-c-operator-2026-07-11.md
  - papers/candidates/keep-and-grade-loop-cost/keep-and-grade-loop-cost-2026-07-11.md
  - GEOMETER-VS-PHYSICS-OBJECTS.md
  - tests/W54_path2_target3_no_local_metric.py
  - tests/W91_algebraic_modular_skeleton.py
  - tests/W94_sectorial_j.py
scripts:
  - tests/W97_cond_iii_all_orders.py
external_refs:
  - "A. Connes, Une classification des facteurs de type III (Ann. Sci. ENS 1973) -- the Radon-Nikodym cocycle (D psi : D phi)_t = Delta_psi^{it} Delta_phi^{-it} is an EXACT unitary cocycle in M for arbitrary type-III von Neumann algebras with faithful normal weights; the cocycle identity u_{s+t}=u_s sigma_s(u_t) is an automorphism-group statement, not a perturbative series."
  - "H. Gottschalk, J. Math. Phys. 43 (2002) 4753 (arXiv:math-ph/0408048) -- Delta^{it}=boost, Bisognano-Wichmann analyticity on Krein spaces; the modular FLOW half is a theorem in the indefinite metric."
  - "H. Araki, K. Hepp, D. Ruelle / the cluster theorem; Osterwalder-Schrader reconstruction -- in a massive QFT with a mass gap, correlations decay exponentially at rate = the mass gap (the minimal mass), an ALL-ORDERS / non-perturbative (axiomatic) statement, NOT a perturbative truncation."
  - "D. Krejcirik & P. Siegl, Phys. Rev. D 86 (2012) 121702 -- bounded metric with UNBOUNDED inverse; the infinite-rank definitizability residual (real vs complex/PT-broken spectrum), shared with W91/W94."
  - "K. S. Stelle (1977); Salvio-Strumia (agravity); W53/W87 -- the ghost mass m_2^2 = (1/2) f_2^2 M_Pl^2 tracks the Weyl coupling; asymptotic freedom drives it to zero ONLY at the free UV fixed point, real and positive at every finite scale."
---

# Condition (iii) of the sectorial closing -- firming the two W54/W91-grade facts to all orders

**Role.** The sectorial closing of the observer conjecture (`W94`) proves that the physical firewall
realization CLOSES sectorially and that the global `J`'s non-existence CONFIRMS observer-relativity.
Its rigor is CAPPED by two supporting facts whose established grade is free-case / one-loop / algebraic-toy:

- **(a)** the firewall grading (the positive metric / C-operator) is **NON-LOCAL but EXPONENTIALLY
  LOCALIZED at ~1/m_ghost** (`W54` Result 3 -- a free-case theorem plus a first-order STRONG-ARGUMENT
  for interacting persistence);
- **(b)** the observer's **value-selection half** (modular flow `Delta^{it}` + Connes cocycle +
  section map, `W91`) is **positivity-free** (algebraic-toy grade).

**Condition (iii)** = firm BOTH from the free/one-loop grade to **all orders / the interacting case**,
or precisely identify the frontier. This swing attacks it and returns the honest grade.

**Answer: (b) PARTIALLY.** The value-selection half is **all-orders-rigorous** (algebraic /
non-perturbative). The exp-localization is **upgraded** from first-order to a **mass-scale
(analyticity-strip = mass-gap) argument** that protects the localization rate at every finite RG
scale, but remains **conditional on the ghost spectrum staying real** -- the **same definitizability
residual** `W91`/`W94` already reduce to. Firming (iii) opens **no new frontier**; it collapses onto
that shared residual.

**Artifacts:** this file + deterministic `tests/W97_cond_iii_all_orders.py` (6/6, numpy-only, exit 0).
**Not committed. Not a claim-status change.** Exploration-grade.

---

## 0. Construction forks (GEOMETER-VS-PHYSICS-OBJECTS.md discipline)

| Object | Construction used | Load-bearing here |
|---|---|---|
| **Ghost clearance** | GU-native **keep-and-grade** (Krein / PT indefinite metric), not positive-Hilbert removal | The two facts are cost-of-the-rescue statements; the whole condition lives on this fork. |
| **The metric / grading** | the **positive intertwiner** `eta` (C-operator), characterized as a symbol built from the constituent `om_i = sqrt(k^2+m_i^2)` (`W54`); its non-locality scale = the analyticity-strip width | The exp-localization RATE is an analytic-structure (mass-gap) property, not a coupling-order property -- this is what makes the mass-scale argument possible. |
| **The value-selection** | the **relative** modular data (reference `phi0` + selected `psi`): flow `Delta^{it}`, algebraic KMS, Connes cocycle `(D psi:D phi0)_t` = the section map (`W91`) | These are **automorphism-level / operator-algebra** objects -- their rigor is set by operator-algebra theorems, NOT by a loop expansion. This is what makes half (b) all-orders. |
| **"Local"** | entire / finite-exponential-type symbol (Paley-Wiener), as in `W54` | The "no LOCAL metric" (non-entirety) statement is exactly as strong as this definition; its all-orders proof is a separate, still-open, item from the ~1/m localization rate. |

**The one fork this swing turns on (named, not defaulted):** *is the exp-localization RATE a
perturbative-order quantity (degrades order-by-order) or a mass-scale/analytic-structure quantity
(protected by the mass gap)?* We identify it as the **latter**, with reason (Section 2): the
localization rate is the width of the analyticity strip, whose only boundary is the constituent branch
points `k=+-i m_i`. This is the geometer-vs-physics-discipline move: the "interactions delocalize the
metric" adversary implicitly reads the rate as a coupling-order quantity; the correct reading is that
it is a mass-gap quantity, and mass gaps are all-orders-protected (exponential clustering).

---

## 1. Five-persona team (inline, sequential, single context)

### Persona 1 -- Krein-QFT / operator specialist (the two computations)

**Half (a), the analytic-structure computation.** The keep-and-grade positive metric symbol is, at
free level, a strictly-signed positive combination of `1/om_i = 1/sqrt(k^2+m_i^2)` (`W54` D1), with
branch points at `k=+-i m_i`; the kernel is `K0(m|x|) ~ e^{-m|x|}` (`W54` D2b). Under interactions the
generator `Q = eps Q1 + eps^2 Q2 + ...` (Branch B) carries **energy denominators**
`1/(om(k_1)+om(k_2)+...)` at each order. **Key structural fact:** every one of these -- at every
order -- is a rational function of the constituent square roots `om_i`. A sum of positive `om`'s is
never zero (no new poles), so the **only** singularities are the branch points of the constituent
`om_i`, i.e. `k=+-i m_i`. Higher orders can introduce more `om_i` factors, hence more branch points,
but **only at their own masses `m_i`** -- never closer to the real axis than the lightest relevant
mass. So the metric/grading symbol is analytic in the strip `|Im k| < min_i m_i` at **every order**,
and its kernel decays at rate `>= min_i m_i = the mass gap`. **The localization rate `~1/m` is a
mass-gap quantity, protected to all orders.** (`W97` T1, T2.)

**Half (b), the algebraic computation.** The modular flow `Delta^{it}` (Gottschalk: built from
`log Delta`, real spectrum), the algebraic KMS relation (metric-independent), and the Connes cocycle
`(D psi:D phi0)_t = Delta_psi^{it} Delta_phi0^{-it}` (the section map) are **automorphism-group**
objects. The cocycle identity `u_{s+t} = u_s sigma_s(u_t)` is an operator-algebra identity, exact for
arbitrary type-III von Neumann algebras with faithful weights (Connes RN cocycle theorem). It carries
**no coupling expansion**: it holds exactly at every value of any deformation/coupling parameter of
the weights. So this half does not degrade order-by-order the way a metric-kernel computation would.
(`W97` T5: the cocycle identity is exact -- residual `~3e-16` -- at every coupling.)

### Persona 2 -- math referee (all-orders-vs-truncation, graded honestly)

| Claim | Setting | Grade |
|---|---|---|
| Value-selection half (flow + KMS + cocycle + section map) survives without positivity | algebraic / type-III | **ALL-ORDERS** (Gottschalk theorem; Connes RN cocycle theorem -- exact, non-perturbative) |
| It carries no loop-truncation limit | interacting | **ALL-ORDERS** -- the residual is the standard AQFT existence assumption (interacting region algebra + boost=modular flow), **shared with everything**, NOT a new truncation |
| Exp-localization rate `~1/m` = mass-gap = strip width | all orders | **STRUCTURAL/ALL-ORDERS mechanism** (strip = mass gap, as in massive-QFT exponential clustering) |
| The gap stays `> 0` at every finite RG scale | AF flow | **within the one-loop truncation** (inherits `W53`/Result-2 grade of the `m_2^2` running) |
| Exp-localization is an **unconditional** all-orders theorem | interacting | **NO** -- conditional on the interacting ghost pole staying **real-massive** (PT-unbroken) |
| "No LOCAL (entire-symbol) metric" persists to all orders | interacting | **first-order STRONG-ARGUMENT** (`W54` unchanged) -- the non-entirety proof proper is not all-orders |

**Referee headline.** Half (b) genuinely firms to all orders because its rigor is set by
operator-algebra theorems, not a loop expansion. Half (a) is **strengthened** beyond `W54`'s
first-order argument -- from "the first correction doesn't cancel the cut" to "the localization rate
is a mass-gap quantity, protected at every order and every finite scale" -- but it is **not** upgraded
to an unconditional all-orders theorem: it depends on the reality of the interacting ghost spectrum.
The referee refuses to let "mass-scale protection" be inflated into "all-orders theorem," and refuses
to let the value-selection half's algebraic rigor be understated.

### Persona 3 -- ADVERSARY ("interactions delocalize the metric")

- *Push 1: "Higher-loop corrections resum into a symbol whose kernel is long-range -- the `~1/m`
  localization is a free-theory accident."* **Answered (`W97` T2).** For the kernel to become
  long-range, a singularity of the metric symbol must approach the **real** `k`-axis. But every
  singularity of every order's symbol is a branch point `k=+-i m_i` of a constituent `om_i`; a sum of
  positive `om`'s never vanishes, so no new singularity appears, and none sits closer to the real axis
  than the lightest mass. The strip half-width is **exactly** the mass gap at every order. A long-range
  kernel would require the mass gap to **close** -- which is a spectrum statement, not a loop-counting
  statement.
- *Push 2: "Then the mass gap closes under interactions -- the ghost mass runs to zero."* **Answered
  (`W97` T3).** Along the asymptotically-free flow the ghost mass tracks the Weyl coupling and reaches
  zero **only at the free UV fixed point** (`W53`/`W87`) -- the **same** exceptional locus `W94` T2
  already identifies as the only place definitizability fails, and which no finite-resolution observer
  occupies. At every finite scale the gap is `> 0` and the strip has finite width.
- *Push 3 (the adversary's real point, conceded): "Interactions could drive the ghost pole COMPLEX (a
  Lee-Wick pair / spontaneous PT-breaking) -- then the branch point leaves the imaginary axis and your
  strip argument breaks."* **Conceded, and this is the residual (`W97` T4).** The mass-scale protection
  holds **iff** the interacting ghost pole stays **real-massive** (PT-unbroken), which is exactly the
  branch-point-on-the-imaginary-axis condition = **definitizability**. This is the **same** residual
  `W91`/`W94` reduce to. So the adversary's strongest push does not open a **new** frontier; it lands
  on the **already-isolated** one.

The three pushes are consistent: the exp-localization is mass-scale-protected wherever the ghost
spectrum is real, and the reality of that spectrum is the shared definitizability residual.

### Persona 4 -- cross-checker + literature (read-only, 2026-07-13)

- **Connes RN cocycle theorem** confirmed: `(D psi:D phi)_t` is an exact unitary cocycle in `M` for
  arbitrary type-III von Neumann algebras with faithful normal weights; it intertwines the two modular
  flows (`sigma_t^psi = u_t sigma_t^phi(.) u_t^*`) and obeys the cocycle identity -- an
  **automorphism-group** statement, no coupling expansion. This is the operator-algebra backing for
  half (b) being all-orders. (Connes 1973; multiple modern treatments.)
- **Gottschalk 2002** confirmed: the Krein modular flow `Delta^{it}` = boost is a theorem in the
  indefinite metric (the flow half needs no positive square root).
- **Massive-QFT exponential clustering** confirmed: in a relativistic QFT with a mass gap and unique
  vacuum, correlations decay `~ e^{-M|x|}` at rate `M =` the minimal mass -- the cluster theorem
  (Araki-Hepp-Ruelle), an **all-orders / non-perturbative** (axiomatic) statement, tied to the mass
  gap via the analyticity strip (OS reconstruction). This is the exact analogue of the mass-scale
  protection of half (a): the localization rate is the mass gap, not a perturbative accident.
- **Krejcirik-Siegl** confirmed: the infinite-rank obstruction is the real-vs-complex (definitizable
  vs not) spectrum question -- the shared residual.

**Deterministic toy (`W97`, numpy-only, 6/6).** T1 free strip = `m_ghost` (reproduces `W54`);
T2 every order-channel (subset of the mass tower) is singular at its own lightest mass, all `>=` the
gap, full tower realizing the gap (mass-scale protection); T3 the AF gap `> 0` at every finite scale,
closing only at `t->inf`; T4 real ghost -> branch point on the imaginary axis, complex ghost -> off it
(the residual); T5 the Connes cocycle identity exact at every coupling (`~3e-16`); T6 the grade
booleans. Two faces agree: the localization is mass-gap-protected, the value-selection half is
algebraic/all-orders, the residual is definitizability.

### Persona 5 -- synthesizer

See Sections 2-4.

---

## 2. The mass-scale protection, stated precisely (half a)

**Claim.** For the keep-and-grade positive metric of the interacting 4th-order theory, at every order
in the interaction, the metric/grading symbol is analytic in the strip `|Im k| < m_gap` and its kernel
decays at rate `>= m_gap`, where `m_gap = min_i m_i` is the mass gap of the modes entering the metric.

**Why (the analyticity-strip = mass-gap mechanism).** The free metric symbol and every interacting
correction are rational functions of the constituent one-particle energies `om_i = sqrt(k^2+m_i^2)`
(free: `1/om_i`; order-`n`: sums/products of energy denominators `1/(om_{i_1}+...+om_{i_p})`). Two
facts close it:

1. **No new poles.** A denominator is a sum of **positive** `om`'s; it never vanishes for real masses.
   So the symbol has **no** poles -- its only singularities are the **branch points** of the
   constituent `om_i`, at `k=+-i m_i`.
2. **Higher orders never move the boundary inward.** An order-`n` correction can only introduce more
   `om_i` factors, hence more branch points, but each at its **own** mass `m_i >= m_gap`. No order adds
   a singularity closer to the real axis than `m_gap`.

Hence the analyticity strip has half-width `= m_gap` at **every order**, and the kernel decays at rate
`= m_gap` -- the **same mechanism** that makes exponential clustering (rate = mass gap) an all-orders
fact in a massive QFT. **This is the mass-scale argument: the localization rate is a mass-gap quantity,
not a coupling-order quantity, so it is protected under interactions.** (`W97` T2.)

**RG protection.** The relevant gap is the ghost mass `m_2`. Along the AF flow `m_2^2 = (1/2)f_2^2
M_Pl^2` tracks the Weyl coupling and closes **only at the free UV endpoint** (`W53`/`W87`) -- the
exceptional locus `W94` already handles. At every finite scale the strip has finite width. (`W97` T3;
inherits the `W53`/Result-2 one-loop-truncation grade of the running.)

**Honest limits of the mass-scale argument (the residual).**
- It protects the **localization rate**, not the **non-entirety** ("no LOCAL metric") itself. The
  all-orders proof that no positive metric with an **entire** symbol emerges from resummation is a
  separate item; `W54`'s non-entirety persistence remains **first-order STRONG-ARGUMENT**.
- It is **conditional on the ghost pole staying real-massive**. If interactions drove the ghost to a
  **complex-conjugate (Lee-Wick) pair** -- spontaneous PT-breaking -- the branch point would leave the
  imaginary axis and the "strip = mass gap" picture would change. Reality of the interacting ghost
  spectrum **is** the definitizability condition (branch point on the imaginary axis = PT-unbroken =
  definitizable). This is the **same** residual `W91`/`W94` reduce to. (`W97` T4.)

---

## 3. The value-selection half is all-orders-rigorous (half b)

The modular flow `Delta^{it}`, the algebraic KMS relation, and the Connes cocycle
`(D psi:D phi0)_t` (= the section map = the observer's value-selection, `W91`/path5-branchB) are
**automorphism-level / operator-algebra** objects:

- **They are positivity-free** (`W91`): built from flows / automorphisms, never from a positive square
  root. (The positive square root is needed only for the **conjugation** `J`, which is the sectorial /
  definitizability half -- not condition (iii)'s subject.)
- **They carry no loop-truncation limit.** The Connes Radon-Nikodym cocycle theorem is exact for
  arbitrary type-III von Neumann algebras with faithful normal weights; the cocycle identity is an
  automorphism-group statement, not a perturbative series. `W97` T5 confirms it holds **exactly**
  (residual `~3e-16`) at every value of an arbitrary coupling/order deformation of the weights, with
  the section (the rate-invariant relative content) recovered independent of the modular rate.
- **The residual is the standard AQFT existence assumption**, not a truncation: that the interacting
  region von Neumann algebra exists and that the boost is the modular flow (Bisognano-Wichmann). This
  is shared with the free/algebraic-toy grade -- going to the interacting case introduces **no new
  truncation** for this half.

So half (b) **firms to all orders**: the observer's value-selection is realized by an algebraic /
non-perturbative structure that does not degrade with interaction order.

---

## 4. The grade of condition (iii): (b) PARTIALLY -- and the residual is not new

**GRADE = (b) PARTIALLY.**

- **Positivity-free value-selection half:** **ALL-ORDERS-RIGOROUS** (algebraic / non-perturbative;
  Connes RN cocycle theorem + Gottschalk flow; no truncation limit). **FIRM.**
- **Exp-localization `~1/m`:** **STRENGTHENED** from `W54`'s first-order strong-argument to a
  **mass-scale (analyticity-strip = mass-gap) argument** protecting the localization rate at every
  finite RG scale (degrading only at the free UV endpoint = the exceptional locus `W94` handles), but
  **NOT** an unconditional all-orders theorem: **conditional on the interacting ghost pole staying
  real-massive** (PT-unbroken / definitizable), and inheriting the one-loop-truncation grade of the
  ghost-mass running. The all-orders **no-LOCAL-metric** (non-entirety) proof proper stays first-order.

**PRECISE RESIDUAL.** The all-orders persistence of half (a) reduces to the **single** condition that
the interacting ghost pole stays **real-massive** (branch point on the imaginary axis = PT-unbroken =
definitizable), versus migrating to a complex Lee-Wick pair. This is the **same** infinite-rank
**definitizability** residual `W91`/`W94` reduce to. **Firming condition (iii) therefore opens NO new
interacting-metric frontier -- it collapses onto the already-isolated definitizability residual.** The
only additional grade it carries is the one-loop-truncation grade of the AF ghost-mass running
(`W53`/Result-2).

**Consequence for the sectorial closing (`W94`).** Condition (iii) does not independently cap the
sectorial closing's rigor beyond what `W91`/`W94` already isolate. The value-selection half that the
closing needs is all-orders-rigorous; the firewall grading it needs is mass-scale-localized at every
finite scale; and the one residual -- reality/definitizability of the interacting ghost spectrum -- is
the **same** deciding computation the whole arc already points at (the full-FRG `beta_{f_2^2}`:
`f_2^2* = 0` firms HORN K / genuine firewall, `f_2^2* > 0` flips to HORN Q / removable ghost). So
condition (iii) is firmed to **all-orders-flow-half + mass-scale-protected-localization**, with the
residual **not new** but shared.

---

## 5. Confidence grade and what would move it

- **Value-selection half is all-orders-rigorous (algebraic, no truncation):** **HIGH** (Connes RN
  cocycle theorem + Gottschalk; `W97` T5 exact at every coupling).
- **Exp-localization rate = mass gap at every order (mass-scale mechanism):** **HIGH** (the
  analyticity-strip = mass-gap structure is exact; same mechanism as massive-QFT clustering; `W97` T2).
- **The AF gap stays > 0 at every finite scale:** **HIGH within the one-loop truncation** (`W53`/`W87`;
  `W97` T3).
- **Exp-localization is NOT an unconditional all-orders theorem (conditional on real ghost spectrum):**
  **HIGH** -- the residual is honestly the reality/definitizability condition (`W97` T4).
- **Firming (iii) opens no new frontier (residual = shared definitizability):** **MEDIUM-HIGH** -- the
  reduction is clean; the one open is whether the interacting ghost genuinely stays real (the same
  `W87` deciding computation).
- **GRADE = (b) PARTIALLY:** **HIGH** -- both halves graded at their true strength; the residual named
  and shown to coincide with the already-isolated one.

**What would move it most.** (a) The full-FRG `beta_{f_2^2}` computation (`W87`): a real-massive
interacting ghost at the fixed point firms the mass-scale protection to an unconditional all-orders
statement (real branch point at every scale); a complex/Lee-Wick fixed point would move the residual.
(b) An all-orders proof of **non-entirety** (no entire-symbol positive metric emerges from
resummation), upgrading `W54`'s first-order persistence -- distinct from the localization-rate
argument firmed here. (c) A rigorous construction of the interacting region von Neumann algebra with
boost = modular flow, discharging the standard AQFT existence assumption for half (b).

---

## 6. What this does NOT do

No GU claim-status, `CANON.md`, `RESEARCH-STATUS.md`, verdict, or public-posture change. No external
action; all citations are read-only literature. The conjecture remains a conjecture; H61/H61a remain
**OPEN** with condition (iii) firmed to **all-orders value-selection half + mass-scale-protected
exp-localization**, the residual **localized to the shared definitizability question** (not a new
frontier). The deliverable is: the mass-scale (analyticity-strip = mass-gap) argument for the
localization rate (`W97` T1-T3); the honest residual (reality of the interacting ghost spectrum =
definitizability, `W97` T4); the all-orders-rigorous (algebraic / non-perturbative) status of the
value-selection half (`W97` T5); and the grade -- **(b) PARTIALLY** -- with the precise residual
(`W97` T6). Reproducible: `tests/W97_cond_iii_all_orders.py` (6/6, exit 0).
