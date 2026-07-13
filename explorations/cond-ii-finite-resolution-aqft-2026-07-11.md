---
artifact_type: exploration
status: exploration (firming CONDITION (ii) of the observer conjecture's sectorial closing to rigorous AQFT grade; 5-persona inline team; literature read-only + deterministic test)
created: 2026-07-13
hypothesis: H61 / H61a (the observer-conjecture Krein-TT critical path) -- the SECTORIAL/relative face, condition (ii)
conjecture: "the source action IS the observer (CONJECTURE-source-action-is-the-observer-2026-07-11.md)"
branch: "The sectorial closing (W94) rests on THREE conditions. (ii) is the AQFT one: is 'the observer's firewall / value-selection needs only the PER-REGION (finite-k / sectorial) modular conjugation J, NOT a global observer-independent one' a RIGOROUS AQFT fact, or a physical heuristic? This swing firms it. The Hilbert-case per-region modular theory (Reeh-Schlieder + Tomita-Takesaki, Bisognano-Wichmann wedge-only geometric J, Haag duality) is STANDARD AQFT; the residual is the KREIN transfer (Gottschalk Krein-BW flow half rigorous; conjugation half theorem-grade on finite-rank definitizable sub-sectors only)."
title: "CONDITION (ii) = PARTIALLY (rigorous-Hilbert + strong-argument-Krein). It is a RIGOROUS AQFT FACT in the positive-metric case that physical observables are realized by PER-(region,state) modular structure and NO observable requires a global observer-independent modular conjugation J: the geometric/global J is WEDGE-ONLY (Bisognano-Wichmann), the per-region (Delta_O,J_O) is the STANDARD object (Reeh-Schlieder + Tomita-Takesaki), and the value-selection apparatus (relative entropy, Connes cocycle, relative modular flow) is per-PAIR / region-local. This transfers to the KREIN case in HALF: the FLOW half is RIGOROUS (Gottschalk 2002, Krein Bisognano-Wichmann, Delta^{it}=boost), the CONJUGATION half is THEOREM-GRADE on each finite-rank definitizable Pi_kappa sub-sector (Shulman Pi_1 1997; W77 rank-2 unbroken; W94 T1) but the CONTINUUM / infinite-rank type-III Krein sectorial-conjugation theorem is NOT in the literature. So (ii)'s CLAIM (per-region suffices, not the global limit) is supported by the flow theorem + the finite-rank conjugation theorem; the precise residual is the continuum Krein sectorial-J theorem + the HORN-K/Q definitizability decision (W87). GRADE = PARTIALLY: rigorous-Hilbert (a genuine upgrade from physical heuristic to standard AQFT, not GU-specific) + strong-argument-Krein."
grade: "exploration / one rigorous-AQFT result (Hilbert case: per-region modular theory is standard, geometric global J wedge-only, no observable needs a global J) + one strong-argument transfer (Krein case: flow half a theorem, conjugation half theorem-grade on finite-rank definitizable sub-sectors, continuum theorem open). Encoded in tests/W96_cond_ii_aqft.py (7/7, numpy-only, exit 0). Literature read-only 2026-07-13: Bisognano-Wichmann (J_W = CRT/CPT reflection, geometric, per-wedge); Reeh-Schlieder (vacuum cyclic-separating for every local algebra); Tomita-Takesaki (per-(region,state) (Delta,J)); Haag duality; Gottschalk JMP 43 (2002) 4753 (Krein Bisognano-Wichmann); Shulman 1997 (Pi_1 Krein Tomita); arXiv:2307.11819 (region-dependent, even nonlocal, modular conjugation). No canon, RESEARCH-STATUS, CANON, claim-status, verdict, or public-posture change. The conjecture remains a conjecture; condition (ii) UPGRADED on the Hilbert side to standard-AQFT and remains strong-argument on the Krein side."
depends_on:
  - explorations/sectorial-relative-j-2026-07-11.md
  - explorations/branch3-algebraic-modular-skeleton-2026-07-11.md
  - explorations/H61a-rank2-verdict-and-convergence-2026-07-11.md
  - explorations/CONJECTURE-source-action-is-the-observer-2026-07-11.md
  - GEOMETER-VS-PHYSICS-OBJECTS.md
  - tests/W94_sectorial_j.py
  - tests/W91_algebraic_modular_skeleton.py
  - tests/W77_H61a_rank2_krein_tomita.py
  - tests/W87_horn_k_vs_q.py
scripts:
  - tests/W96_cond_ii_aqft.py
external_refs:
  - "J. J. Bisognano & E. H. Wichmann, J. Math. Phys. 16 (1975) 985; 17 (1976) 303 -- the modular group of a WEDGE algebra + vacuum is the Lorentz boost, and the modular conjugation J_W is the CRT (charge-conjugation x reflection x time-reversal) operator: the geometric/observer-independent meaning of (Delta,J) is proved PER-WEDGE, not globally."
  - "H. Reeh & S. Schlieder, Nuovo Cimento 22 (1961) 1051 -- the vacuum is CYCLIC and SEPARATING for the algebra of every bounded region with nonempty causal complement; hence every local algebra carries a well-defined Tomita-Takesaki modular structure."
  - "M. Tomita / M. Takesaki (Tomita-Takesaki modular theory) -- each von Neumann algebra M with a cyclic-separating vector has its OWN polar decomposition S = J Delta^{1/2}; the pair (Delta,J) is attached to a (algebra, state) PAIR, never to a single global object."
  - "R. Haag, Local Quantum Physics (Springer, 1996) -- Haag duality M(O)' = M(O'); modular theory is intrinsically per-region; the CPT operator Theta is a global antiunitary DERIVED from the per-wedge J_W (PCT theorem), not a modular conjugation of a global algebra."
  - "H. Gottschalk, J. Math. Phys. 43 (2002) 4753 (arXiv:math-ph/0408048) -- Bisognano-Wichmann for quantum fields acting on KREIN spaces: dense analytic vectors for the velocity-transformation generator, Delta^{it}=boost in the indefinite metric. The per-region modular FLOW is a theorem in the Krein case."
  - "V. S. Shulman, 1997 (Pi_1 indefinite-metric Tomita theorem) -- the rank-1 Pontryagin Krein Tomita-Takesaki conjugation theorem; state of the art. No Pi_kappa (kappa>=2) general Krein conjugation theorem exists (H61a)."
  - "H. Casini et al., arXiv:2307.11819 -- modular conjugation for the chiral fermion in multicomponent regions: explicit REGION-DEPENDENT (and, for multicomponent regions, nonlocal) modular conjugation; the modular objects are intrinsically relative to the (region, state)."
  - "H. Langer, spectral functions of definitizable operators in Krein spaces -- Pontryagin Pi_kappa (finite rank) is DEFINITIZABLE (an eta-positive square root / functional calculus exists); general infinite-rank is not."
---

# Condition (ii): is "sectorial / per-region J suffices, no observable needs a global J" a rigorous AQFT fact?

**Role.** The observer conjecture's sectorial closing (`W94`) argues the physical realization of the
observer's firewall requires only a **sectorial / relative** modular conjugation `J` (which exists on
every definitizable sub-sector), **not** the global one (which is walled at `k=inf`). That closing rests
on **three conditions**. This swing firms **condition (ii)** — the AQFT one — to rigorous grade:

> **(ii)** The observer's firewall / value-selection is realized by the **per-(region, state)** modular
> structure of local algebras, and **no observable requires a global observer-independent modular
> conjugation `J`**.

`W94`'s second derivation **D2** already noted (informally) that in **ordinary** QFT the modular
conjugation is intrinsically per-`(region, state)` — the geometric/global `J` is **wedge-only**
(Bisognano-Wichmann) — so a per-region `J` is the **standard** object and a global observer-independent
`J` is the **over-strong** demand. This swing asks whether that is a **theorem** or a **heuristic**, and
whether it **transfers to the Krein case**.

**Answer: condition (ii) = PARTIALLY.** **RIGOROUS in the Hilbert (positive-metric) case** — it is
standard AQFT, not a heuristic and not GU-specific. **STRONG ARGUMENT in the Krein case** — the flow half
is a theorem (Gottschalk), the conjugation half is theorem-grade on each **finite-rank definitizable
sub-sector** (Shulman `Pi_1`; `W77`; `W94` T1), and the **continuum / infinite-rank type-III Krein
sectorial-conjugation theorem** is the residual.

**Artifacts:** this file + deterministic `tests/W96_cond_ii_aqft.py` (7/7, numpy-only, exit 0).
**Not committed. Not a claim-status change.** Exploration-grade.

---

## 0. Construction forks (GEOMETER-VS-PHYSICS-OBJECTS.md discipline)

| Object | Standard-field construction | Program-native construction | Which side condition (ii) lives on |
|---|---|---|---|
| **The modular conjugation `J`** | Tomita-Takesaki `J` of a local algebra + a cyclic-separating state; geometric only for the wedge (Bisognano-Wichmann) | the antilinear `J = C.PT` (W67), realized **sectorially** per definitizable sub-sector | **The standard-field side is decisive HERE:** condition (ii) is a claim about which modular objects observables need, and that is settled in ordinary positive-metric AQFT (per-region), BEFORE any GU-native input. The Krein-native construction only inherits/sharpens it. |
| **"Global observer-independent `J`"** | never a standard object — even ordinary AQFT builds `(Delta_O, J_O)` per region; the only global antiunitary is CPT `Theta`, **derived** from `J_W` | the walled `k=inf` limit (W90/91/93) | Standard AQFT already declines to build a global `J`; the GU wall is a **sharpening** (nonexistent, not merely nonstandard), not the origin of the per-region structure. |
| **The value-selection** | relative modular data: relative entropy, Connes cocycle `(D psi:D phi)_t`, relative modular flow — all per-**pair**, region-local | the observer's weight selection `psi` vs reference `phi0` (W91, positivity-free) | **Per-pair / region-local on both sides.** The adversary's "value-selection is a global object" fails already in standard AQFT (T3). |

**Why the fork matters and does NOT default silently.** Condition (ii) is one of the rare GU objects
where the answer lives on the **standard-physics side**: "no observable needs a global `J`" is a fact of
ordinary AQFT, independent of GU's Krein primitive. We name this explicitly (per the discipline) rather
than defaulting to the program-native reading — the GU-native Krein `J` only inherits the per-region
structure and adds the definitizability residual.

---

## 1. Five-persona team (inline, sequential, single context)

### Persona 1 — AQFT / local-modular-theory specialist (the Hilbert-case theorem)

The Haag-Kastler axioms assign to each spacetime region `O` a von Neumann algebra `M(O)` on a fixed
Hilbert space with vacuum `Omega`. Three standard theorems make the per-region modular structure the
canonical one:

1. **Reeh-Schlieder (1961).** `Omega` is **cyclic and separating** for every `M(O)` with `O` bounded and
   causal complement nonempty. So every local algebra satisfies the Tomita-Takesaki hypothesis and
   carries its **own** modular pair `(Delta_O, J_O)` from `S_O = J_O Delta_O^{1/2}`.

2. **Bisognano-Wichmann (1975).** For a **wedge** `W`, the modular flow `Delta_W^{it}` is the Lorentz
   **boost** preserving `W`, and the modular conjugation `J_W` is the **CRT operator** (charge-
   conjugation × `x^1`-reflection × time-reversal) — a **geometric, observer-independent** object. This
   is the **only** region for which the modular objects have a proven geometric meaning; and it is
   **per-wedge**, not a single global `J`. (Verified in the literature 2026-07-13:
   "the Bisognano-Wichmann property holds iff `J_W` represents a CPT reflection".)

3. **Haag duality.** `M(O)' = M(O')`. Together with Tomita's `J_O M(O) J_O = M(O)'`, the modular
   conjugation implements the **geometric complement** relation — again **per region**.

**Specialist finding.** The modular pair is intrinsically attached to a **(region, state)**. A single
global observer-independent modular conjugation is **not** a standard object of AQFT. The only global
antiunitary the theory produces is the **CPT operator `Theta`**, and by the algebraic PCT theorem `Theta`
is **built from the per-wedge `J_W`** (`Theta` = product of the wedge reflection with a rotation), not a
modular conjugation of the global/quasilocal algebra. Indeed the quasilocal algebra does **not** have
`Omega` as cyclic-separating in the modular sense that would yield a nontrivial global `J` with
`J M J = M'`. So condition (ii)'s first half — "no observable needs a global observer-independent `J`" —
is a **rigorous consequence of standard AQFT**.

### Persona 2 — MATH REFEREE (is "no observable needs a global J" a THEOREM or a slogan?)

- **Ruling 1 — per-region is a theorem, not a slogan.** Reeh-Schlieder + Tomita-Takesaki are proved; the
  per-region `(Delta_O, J_O)` is constructed, not posited. Different regions/states give **different**
  modular objects: unitarily related (all faithful normal states on a type-III factor are related by an
  inner unitary, Connes) but **not equal** — `Delta_O` depends on the state, `J_O` on the region.
  arXiv:2307.11819 exhibits an **explicit** region-dependent `J` (nonlocal for multicomponent regions).
  So "the modular conjugation is per-(region,state)" is a computed fact.

- **Ruling 2 — the discriminator that makes it decisive.** The referee's gate on "no observable needs a
  global `J`" is: exhibit the observables and show each is realized by local/relative modular data. The
  physical observables of AQFT are (a) **local** — smeared fields, `M(O)`-elements; (b) the **S-matrix**,
  constructed by **Haag-Ruelle / LSZ collision theory** from local fields and asymptotic **local**
  algebras (no global `J` enters); (c) **relative entropy / relative energy / QNEC** — built from the
  **relative** modular operator `Delta_{phi|psi}` of a **pair** localized to a region (Araki). None of
  these invokes a global modular conjugation. The **geometric** content that IS observer-independent
  (the boost, CPT) is the **wedge** modular data — still per-wedge. **Ruling: rigorous.**

- **Ruling 3 — the honest boundary.** The Hilbert-case statement is standard AQFT. The referee refuses to
  extend the rigor to the **Krein** case for free: the AQFT theorems above assume a **positive-metric**
  Hilbert space, and GU is Krein. The transfer must be argued separately (Personas 4, 5). The referee
  grades the Hilbert half **RIGOROUS** and holds the Krein half for the transfer analysis.

### Persona 3 — ADVERSARY ("the value-selection is a GLOBAL object")

- *Push 1: "the observer's value-selection — choosing which state/history is realized — is a global act;
  it needs a modular object defined on the whole theory, i.e. a global `J`."* **Answered in standard
  AQFT.** The value-selection apparatus is **relative** modular theory: the Connes cocycle
  `(D psi : D phi)_t = Delta_psi^{it} Delta_phi^{-it}` (a Radon-Nikodym derivative of one state against
  a reference), relative entropy `S(psi||phi)`, and the relative modular flow. **All are per-PAIR and
  region-local** — built from the two **flows** (positivity-free, `W91` T2), never from a global
  conjugation. `W96` T3 computes the cocycle on a toy local algebra: it is unitary in `M` and obeys the
  Connes cocycle identity (residual `7e-16`). So the value-selection is **not** a global object; it is a
  per-(region, pair) object. The adversary's premise is false already in ordinary QFT.

- *Push 2: "the S-matrix is global — it relates the whole in- and out-Hilbert spaces."* **Answered.** The
  S-matrix is **global as a unitary** but is **constructed** from **local** data (Haag-Ruelle scattering
  builds asymptotic fields from local ones; LSZ from time-ordered local correlators). The one genuinely
  global antiunitary — CPT `Theta` — is **derived** from the per-wedge `J_W` (PCT theorem), not a
  primitive. So "global as an object" does not mean "requires a primitive global `J`": the global
  observables **factor through** per-region / per-pair modular structure.

- *Push 3 (the fallback): "fine in Hilbert; but GU is Krein — maybe the Krein value-selection is
  irreducibly global."* **This is the real residual, and it is honestly the Krein-transfer question, not
  the Hilbert one.** Per `W91`, the Krein value-selection (flow / KMS / Connes cocycle / section map) is
  **positivity-free** and therefore **survives** the indefinite metric at the **flow** level. What does
  not transfer for free is the **conjugation** (the firewall's `J^2=1`), and that is exactly where the
  residual sits (Persona 4). The adversary's strongest form reduces to "is the infinite-rank Krein region
  algebra definitizable?" — the shared HORN-K/Q open (`W87`), **not** a claim that the value-selection is
  global.

### Persona 4 — CROSS-CHECKER (the Krein transfer + literature)

**The Krein transfer splits exactly along the flow/conjugation seam (matching Branch 3, `W91`).**

- **FLOW half — RIGOROUS.** **Gottschalk (JMP 43 (2002) 4753, math-ph/0408048)** proves Bisognano-
  Wichmann for local relativistic quantum fields on **Krein spaces**: a dense set of analytic vectors for
  the velocity-transformation generator exists, so `Delta^{it}` = boost is defined in the indefinite
  metric. Verified 2026-07-13. So the **per-region modular flow** — the object that carries the value-
  selection — survives the Krein case **as a theorem**. `W96` T4 reproduces the toy fact (`W91` T1): the
  flow stays `eta`-unitary (residual `2e-15`) across the entire exceptional-locus approach `r: 0.30 ->
  0.99`, independent of metric conditioning.

- **CONJUGATION half — THEOREM-GRADE ON FINITE-RANK DEFINITIZABLE SUB-SECTORS ONLY.** The per-region
  Krein `J` needs an `eta`-positive `Delta^{1/2}` (polar decomposition), i.e. **definitizability**
  (Langer). On a **Pontryagin `Pi_kappa`** (finite-rank) sub-sector the metric **is** definitizable, so
  the per-region/sectorial Krein `J` **exists** with all four axioms — **theorem-grade** (Shulman's
  `Pi_1` Krein Tomita theorem, 1997; `W77` rank-2 in the modular-PT-unbroken regime; `W94` T1). But the
  **continuum / infinite-rank / type-III** Krein per-region conjugation theorem is **not in the
  literature**: Shulman `Pi_1` is the state of the art, and there is **no `Pi_kappa` (`kappa >= 2`)
  general Krein Tomita-conjugation theorem** (`H61a`). `W96` T5 encodes both faces: the sub-sector `J`
  has finite norm `||J_sector|| = 2.51`; over the non-definitizable tower `sup ||J_kappa|| -> inf`
  (`1000`), so there is no continuum lift.

- **Literature agrees on the two load-bearing facts.** (i) **Bisognano-Wichmann**: `J_W` = CRT/CPT
  reflection, geometric, **per-wedge** — the global geometric `J` is wedge-only. (ii) **Langer**:
  `Pi_kappa` (finite rank) is definitizable (`eta`-positive `Delta^{1/2}` exists), general infinite-rank
  is not — the sub-sector escape and the tower obstruction are two faces of the same dichotomy.

**Cross-check verdict.** The per-region **structure** survives the Krein case; the per-region **flow**
survives with **full rigor**; the per-region **conjugation** survives **on each finite-rank definitizable
sub-sector** (theorem) but the **continuum** conjugation theorem is the open residual. This is exactly
what condition (ii) needs — the observer occupies a finite sub-sector — and exactly where it is not yet a
continuum theorem.

### Persona 5 — SYNTHESIZER (the grade)

See Sections 2-4.

---

## 2. VERDICT: condition (ii) = PARTIALLY (rigorous-Hilbert + strong-argument-Krein)

| Question | Answer | Grade | Evidence |
|---|---|---|---|
| Is "physical observables are realized by per-(region,state) modular structure" a theorem? | **YES** — Reeh-Schlieder + Tomita-Takesaki | **RIGOROUS (Hilbert)** | W96 T1 |
| Is the geometric / observer-independent `J` wedge-only? | **YES** — Bisognano-Wichmann; CPT `Theta` derived from `J_W` | **RIGOROUS (Hilbert)** | W96 T2 |
| Does any observable require a global observer-independent `J`? | **NO** — S-matrix from local fields; value-selection per-pair (Connes cocycle) | **RIGOROUS (Hilbert)** | W96 T3 |
| Does the per-region FLOW survive the Krein case? | **YES** — Gottschalk Krein Bisognano-Wichmann | **RIGOROUS (Krein flow)** | W96 T4 |
| Does the per-region CONJUGATION `J` survive the Krein case? | **On each finite-rank definitizable sub-sector** (Shulman `Pi_1`, `W77`, `W94` T1); continuum theorem OPEN | **STRONG ARGUMENT (Krein)** | W96 T5 |
| Does condition (ii)'s CLAIM (per-region suffices, not global) hold? | **YES** — supported by the flow theorem + the finite-rank conjugation theorem | **PARTIALLY** | W96 T6 |

**The precise statement.**
> **Hilbert case (rigorous, standard AQFT, NOT GU-specific):** modular theory is intrinsically
> per-`(region, state)`; the observer-independent geometric modular conjugation is **wedge-only**
> (Bisognano-Wichmann); and **no observable requires a global observer-independent `J`** — the value-
> selection apparatus is per-pair / region-local, and the global observables (S-matrix, CPT) factor
> through local / per-wedge modular data. A demand for a global `J` is over-strong even in ordinary QFT.
>
> **Krein case (strong argument, where the residual is):** the per-region modular **flow** transfers with
> **full rigor** (Gottschalk); the per-region modular **conjugation** transfers **theorem-grade on each
> finite-rank definitizable sub-sector** (Shulman `Pi_1`; `W77`; `W94` T1) — which is exactly the
> sectorial `J` condition (ii) claims suffices — but the **continuum / infinite-rank type-III Krein
> sectorial-conjugation theorem** is not established, and it is coupled to the **HORN-K/Q definitizability
> decision** (`W87`).

**This is a genuine upgrade.** `W94`'s D2 was stated as an informal second derivation ("AQFT modular
theory is per-region"). Condition (ii) is now firmed: the Hilbert half is **standard-AQFT rigorous** (a
move from "physical heuristic" to "theorem"), and the Krein half is **precisely localized** to the one
missing continuum theorem — the same residual Branch 3 (`W91`) and `H61a` reach from independent
directions. **The demand for a global observer-independent `J` was never a standard object of QFT; the
sectorial/per-region `J` is the standard one.**

---

## 3. The precise residual (do not overclaim)

The residual is **NOT** on the Hilbert side and **NOT** in condition (ii)'s claim. It is a single missing
**continuum Krein theorem**, coupled to a decidable computation:

1. **A continuum / infinite-rank type-III Krein per-region (relative) modular conjugation theorem on a
   definitizable sub-sector** — satisfying `J M J = M'`, Krein-antiisometry, and the covariance
   `S = J Delta^{1/2}`. The finite-rank case is a theorem (Shulman `Pi_1`; extended to the PT-unbroken
   rank-2 interior in `W77`); the continuum lift is open. (No `Pi_kappa`, `kappa >= 2`, general theorem
   exists — `H61a`.)

2. **The HORN-K/Q definitizability decision (`W87`)** — is GU's actual infinite-rank region algebra
   definitizable (a positive reference weight exists, HORN Q) or not (HORN K)? This decides whether the
   sectorial structure is the **whole** story (each observer's sub-sector definitizable, sectorial `J`
   exists) with **no** bounded global limit — which is precisely the observer-relativity `W94` argues
   for. Note the self-consistency: at HORN K the global `J` is **absent by theorem**, which `W94` reads
   as observer-relativity confirming itself; condition (ii) only needs the **sectorial** `J`, which
   exists at every finite rank regardless.

**What would move the grade to FIRMABLE-NOW:** a proof of (1) — a continuum Krein type-III sectorial-
conjugation theorem under definitizability. That would make the Krein transfer of condition (ii)
theorem-grade, matching the Hilbert case, and close (ii) to fully rigorous.

**What would NOT move it (honesty):** more finite-rank toys (already theorem-grade); the flow half
(already rigorous, Gottschalk); or the Hilbert case (already rigorous). Do not mistake the abundant
finite-rank evidence for the missing continuum theorem.

---

## 4. Confidence grade and scope

- **Hilbert: modular theory per-(region,state):** **HIGH** (Reeh-Schlieder + Tomita-Takesaki, standard).
- **Hilbert: geometric/global `J` is wedge-only:** **HIGH** (Bisognano-Wichmann; CPT `Theta` derived).
- **Hilbert: no observable needs a global `J`:** **HIGH** (S-matrix from local fields; value-selection
  per-pair; the global antiunitary is derived, not primitive).
- **Krein: flow half rigorous:** **HIGH** (Gottschalk 2002, cited theorem; `W96` T4 exact toy).
- **Krein: conjugation half theorem-grade on finite-rank definitizable sub-sectors:** **HIGH within the
  finite rank** (Shulman `Pi_1`; `W77` rank-2 unbroken; `W94` T1); **the continuum lift is OPEN**.
- **Condition (ii) = PARTIALLY (rigorous-Hilbert + strong-argument-Krein):** the grade this swing
  delivers. **Not FIRMABLE-NOW** (the continuum Krein conjugation theorem is missing); **not FRONTIER**
  (the Hilbert case is rigorous standard AQFT and the Krein flow half is a theorem).

**Honest register.** This firms **one** of the three conditions of `W94`'s sectorial closing. It does not
close conditions (i) or (iii), and it does not change the conjecture's status. It does establish that the
AQFT content of the sectorial reading — "the observer needs only the per-region `J`, no observable needs
a global one" — is **standard AQFT in the Hilbert case** and **strong-argument in the Krein case**, with
the residual precisely named.

---

## 5. What this does NOT do

No GU claim-status, `CANON.md`, `RESEARCH-STATUS.md`, verdict, or public-posture change. No external
action; all citations are read-only literature. The conjecture remains a conjecture; condition (ii) of
`W94`'s sectorial closing is **UPGRADED** on the Hilbert side from physical heuristic to **standard
AQFT**, and remains **strong-argument** on the Krein side with the residual localized to a single
continuum theorem. This branch **presents, does not decide** — it hands the orchestrator: the Hilbert-
case rigor (per-region modular theory, wedge-only geometric `J`, no observable needs a global `J`), the
Krein-flow-half theorem (Gottschalk), the Krein-conjugation-half finite-rank theorem (Shulman `Pi_1` /
`W77` / `W94` T1), the precise residual (continuum Krein sectorial-conjugation theorem + HORN-K/Q, `W87`),
and the honest grade: **condition (ii) = PARTIALLY (rigorous-Hilbert + strong-argument-Krein)**.
Reproducible: `tests/W96_cond_ii_aqft.py` (7/7, exit 0).
