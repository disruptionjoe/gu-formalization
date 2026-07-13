---
artifact_type: exploration
status: exploration (blind-wave Branch 3; 5-persona inline team; literature check read-only + deterministic toy)
created: 2026-07-13
hypothesis: H61 / H63 (the observer-conjecture Krein-TT critical path; the algebraic re-founding)
conjecture: "the source action IS the observer (CONJECTURE-source-action-is-the-observer-2026-07-11.md)"
branch: "Branch 3 (blind wave) -- TYPE-III KREIN TOMITA-TAKESAKI via an ALGEBRAIC / RELATIVE modular skeleton that BYPASSES the positive KMS state: can the modular conjugation J (the firewall) be built from the surviving Krein structure (Gottschalk flow + Connes cocycle + half-sided modular inclusion) WITHOUT a positive Delta? Cross-shared with Branch 2 (Shulman quasivector route) on the infinite-rank definitizability residual."
title: "Branch 3 algebraic/relative modular skeleton. VERDICT = REDUCES-TO-DEFINITIZABILITY. The algebraic/relative route SPLITS cleanly. (A) The FLOW half -- the modular flow Delta^{it} (Gottschalk 2002), the algebraic KMS relation, and the Connes cocycle (D psi:D phi0)_t = the RELATIVE flow -- IS constructible WITHOUT the positive state: all three are built from flows / automorphisms, never from a positive square root, and this half realizes the observer's VALUE-SELECTION (choosing psi against a reference phi0) and IS the observer-record<->section map (path5-branchB). A genuine advance: the value-selection has a positivity-free algebraic realization. (B) The CONJUGATION half -- the firewall's antilinear J^2=1, J=S Delta^{-1/2} -- still needs an eta-POSITIVE square root via polar decomposition, which 'eta-selfadjoint + real-positive spectrum' does NOT supply (a separate definitizability condition). The RELATIVE move does NOT rescue it: relative modular theory replaces one positive state by a PAIR, genuinely breaking the symmetry, but the relative Delta_{phi,psi} is STILL eta-positive and its square root STILL needs a POSITIVE reference weight -- so a relative J exists IFF a positive reference weight exists IFF Delta is definitizable. At HORN K (GU's genuinely-indefinite, non-definitizable vacuum, W87) even the reference has no positive representative, so the relative J fails EXACTLY where the absolute one does. Half-sided modular inclusions (Wiesbrock/Borchers) relocate positivity to the spectrum condition (a positive-generator translation), which the indefinite metric breaks (ghosts = no positive energy) -- the same residual, re-coordinatized. So NO genuine relative J bypasses positivity (not CONSTRUCTIBLE); the flow/section half survives and the residual is a decidable shared condition (not OBSTRUCTED). Branch 3 and Branch 2 reduce to the SAME open question: is the region algebra's modular Delta DEFINITIZABLE at infinite rank (equivalently, does a positive reference weight exist)?"
grade: "exploration / literature check (2026-07-13, read-only: Gottschalk 2002 JMP 43 4753; Wiesbrock CMP 157 (1993) 83 + Borchers CMP 143 (1992) 315 on half-sided modular inclusions [positive-generator translation]; Araki/Connes relative modular theory [relative Delta positive, cocycle from flows]; Langer definitizability + Krejcirik-Siegl PRD 86 (2012) 121702 [infinite-rank residual]; arXiv:2606.13251 KMS<=>quasi-Hermiticity) + deterministic tests/W91_algebraic_modular_skeleton.py (5/5, numpy-only, exit 0). PROVEN on the toy: the flow Delta^{it} stays eta-unitary across the exceptional-locus approach while the eta-positivity of Delta^{1/2} degrades (T1); the Connes cocycle is built from flows only, obeys the cocycle identity, and is rate-invariant (T2); the relative J's eta-positivity margin degrades in lockstep with the absolute one (T3); the HSMI generator is real but sign-indefinite (spectrum condition broken) in the indefinite metric (T4). The claim that GU sits on the non-definitizable horn (HORN K) is INHERITED from W87 (repo-native indication, not proven here). No canon, RESEARCH-STATUS, CANON, claim-status, verdict, or public-posture change. The conjecture remains a conjecture; H61/H63 remain OPEN with the residual sharpened and LOCALIZED to the conjugation half."
depends_on:
  - explorations/rankN-krein-tt-for-gu-2026-07-11.md
  - explorations/H61-krein-tt-first-swing-2026-07-11.md
  - explorations/H61a-rank2-verdict-and-convergence-2026-07-11.md
  - explorations/path5-branchB-filtration-section-map-2026-07-11.md
  - explorations/CONJECTURE-source-action-is-the-observer-2026-07-11.md
  - GEOMETER-VS-PHYSICS-OBJECTS.md
  - tests/W84_rankN_krein_tt.py
  - tests/W74_H61_krein_tt_swing.py
scripts:
  - tests/W91_algebraic_modular_skeleton.py
external_refs:
  - "W. Gottschalk, J. Math. Phys. 43 (2002) 4753 (arXiv:math-ph/0408048) -- Delta^{it}=boost, Bisognano-Wichmann analyticity on Krein spaces; the modular FLOW half is a theorem in the indefinite metric."
  - "H.-W. Wiesbrock, Comm. Math. Phys. 157 (1993) 83 -- half-sided modular inclusions: a +HSMI is characterized by a one-parameter unitary group with POSITIVE Hermitian generator (the spectrum condition)."
  - "H.-J. Borchers, Comm. Math. Phys. 143 (1992) 315 -- the commutation relations of Delta^{it} and J with a translation U(a) of POSITIVE generator; the structure theorem behind HSMI reconstruction of J."
  - "H. Araki (relative modular operator) / A. Connes (Radon-Nikodym cocycle, 1973) -- the relative modular operator Delta_{phi|psi} is POSITIVE self-adjoint; the cocycle (D psi:D phi)_t = Delta_psi^{it} Delta_phi^{-it} is built from the modular flows and lies in M."
  - "H. Langer, spectral functions of definitizable operators in Krein spaces; D. Krejcirik & P. Siegl, Phys. Rev. D 86 (2012) 121702 -- the infinite-rank definitizability residual (bounded metric, unbounded inverse), shared with Branch 2."
  - "arXiv:2606.13251, KMS conditions for non-Hermitian systems -- positive (biorthogonal) KMS state <=> quasi-Hermiticity (HORN Q/HORN K)."
---

# Branch 3 -- the algebraic / relative modular skeleton: can J be built without the positive state?

**Role.** This blind-wave branch attacks the frontier the prior wave (`W84`/`W87`) left standing: at
type III / infinite rank, GU's indefinite vacuum is a **genuine, non-definitizable ghost** (HORN K), so the
standard Tomita-Takesaki positivity engine -- the `eta`-positive polar decomposition `S = J Delta^{1/2}` with
a **positive** `Delta` -- has **no positive state to run on**. Branch 3 asks the strongest possible question:
**can the modular conjugation `J` (the firewall, antilinear `J^2=1`, `JMJ=M'`) be built ALGEBRAICALLY /
RELATIVELY, bypassing the positive state**, from the structure that DOES survive the indefinite metric --
the Gottschalk modular **flow** `Delta^{it}`, the Connes **cocycle** of relative modular theory, a
**half-sided modular inclusion** ported to Krein?

**The answer: the algebraic/relative route SPLITS.** Its flow half is constructible without the positive
state (a genuine advance); its conjugation half **reduces to the shared infinite-rank definitizability
residual**. **VERDICT = REDUCES-TO-DEFINITIZABILITY** -- the same residual Branch 2 (Shulman quasivector)
reduces to.

**Artifacts:** this file + deterministic `tests/W91_algebraic_modular_skeleton.py` (5/5, numpy-only, exit 0).
**Not committed. Not a claim-status change.** Exploration-grade.

---

## 0. Construction forks (GEOMETER-VS-PHYSICS-OBJECTS.md discipline)

| Object | Construction used | Load-bearing here |
|---|---|---|
| **The algebra** | GU-native indefinite region `*`-algebra on the **Krein space** (`[x,y]=<x,eta y>`, `eta`=the C-grading), **infinite** rank of indefiniteness, genuinely-indefinite (HORN K, `W87`) | The absence of a positive state is program-native (KEEP-AND-GRADE), not a defect -- and it IS the observer's value-selection (CONJECTURE Sec 3). |
| **The modular conjugation** | the **antilinear** `J = C.PT`, obtained from the polar decomposition `S=J Delta^{1/2}`, **not** the linear `C` (that is the fundamental symmetry) | Its construction needs an `eta`-positive `Delta^{1/2}`; this branch tests whether an ALGEBRAIC/RELATIVE route builds it without a positive `Delta`. |
| **The state / weight** | a **reference** faithful weight `phi0` + the observer's **selected** weight `psi` (relative modular theory), **not** a single distinguished positive KMS state | The relative move is program-native: "no distinguished state = the observer's free selection" (H62 arena/value). The question is whether "relative" also removes the POSITIVITY requirement, or only the uniqueness one. |

The one new fork this branch surfaces: **"absolute modular conjugation (one positive state)" vs "relative
modular conjugation (a reference + a selected weight)."** The conjecture's mechanism lives on the relative
side; this branch determines that the relative side genuinely helps the **flow/section** half but **not** the
**conjugation** half.

---

## 1. Five-persona team (inline, sequential, single context)

### Persona 1 -- von Neumann / Tomita-Takesaki algebraist (the exact positivity dependency)

The deliverable of Tomita-Takesaki is the pair `(Delta^{it}, J)` from the closed antilinear `S(aOmega)=a^+Omega`,
`Delta = S^+ S`, and the polar decomposition `S = J Delta^{1/2}`. **Isolate where positivity enters:**

- **The FLOW `Delta^{it}`** is a one-parameter `eta`-unitary group. Gottschalk (2002) builds it on a Krein
  space directly from the **boost generator's analyticity** (Bisognano-Wichmann), i.e. from `log Delta`
  (which exists whenever `Delta` has real spectrum), **NOT** from a positive square root. **So the flow half
  does not need positivity.** (`W91` T1: the flow stays `eta`-unitary to `1e-14` across the entire
  exceptional-locus approach `r: 0.3 -> 0.99`.)
- **The CONJUGATION `J = S Delta^{-1/2}`** needs `Delta^{1/2}` to be **`eta`-positive**, so that `J` is a
  Krein anti-isometry (`[Jx,Jy] = conj[x,y]`). And here is the exact subtlety: **`Delta` `eta`-selfadjoint
  with real-positive spectrum does NOT make `Delta^{1/2}` `eta`-positive.** `eta`-positivity of `Delta^{1/2}`
  is the condition that the Hermitian form `eta * Delta^{1/2}` is `>= 0` -- a **separate** condition, exactly
  **definitizability** (a spectral function / `eta`-positive functional calculus). (`W91` T1: the
  `eta`-positivity margin of `Delta^{1/2}` degrades `1.284 -> 0.158` as `cond(eta) -> inf`, while the flow is
  untouched.) **This is the one piece that needs the positive state, and it is precisely the firewall's
  `J^2=1` flip (H63's lemma L2).**

**Specialist finding.** Positivity is needed at **exactly one place**: the `eta`-positive square root in the
polar decomposition. Everything else -- the flow, the algebraic KMS relation, the commutant relation once `J`
is given -- is positivity-free. So the whole question is whether the **square root** can be obtained
algebraically/relatively.

### Persona 2 -- math referee (does the relative move remove the positivity, or only the uniqueness?)

The relative apparatus and what each piece requires, graded:

| Piece | What it needs | Survives without a positive state? |
|---|---|---|
| Modular **flow** `Delta^{it}` = boost on Krein | `log Delta` (real spectrum) | **YES** -- Gottschalk 2002 (theorem). |
| Algebraic **KMS** relation | metric-independent boundary condition | **YES** -- formal KMS holds without positivity (arXiv:2606.13251). |
| **Connes cocycle** `(D psi : D phi0)_t = Delta_psi^{it} Delta_phi0^{-it}` | the two **flows** only | **YES** -- built from flows, no square root; lands in `M` (`W91` T2). |
| **Relative modular operator** `Delta_{phi,psi}` | `Delta_{phi,psi} = S_{phi,psi}^+ S_{phi,psi}` is **POSITIVE** | **NO** -- it is `eta`-positive, and its polar `Delta_{phi,psi}^{1/2}` needs a **positive reference weight** `phi0`. |
| **Relative conjugation** `J_{phi,psi}` | the `eta`-positive `Delta_{phi,psi}^{1/2}` | **NO** -- reduces to definitizability (`W91` T3). |

**Referee headline.** The relative move removes the **uniqueness** requirement (one distinguished state) but
**not** the **positivity** requirement. Relative modular theory is built on a **pair** of faithful (positive)
weights; the relative modular operator is itself **positive self-adjoint** (Araki), so its square root -- the
only thing `J_{phi,psi}` needs beyond the flow -- **still** requires a positive anchor. The referee's ruling:
**a relative `J` exists IFF a positive reference weight exists IFF `Delta` is definitizable.** The relative
route does not bypass positivity for the conjugation; it relocates the positivity from "the state" to "the
reference weight," which at HORN K is equally unavailable.

### Persona 3 -- ADVERSARY (both directions)

- *Against REDUCES ("the cocycle is positivity-free, so the whole relative structure is; you are smuggling
  the positive reference back in").* Pressed: the **cocycle** is positivity-free because it is a **flow-level**
  object (a ratio of two `Delta^{it}`'s) -- and that is genuinely a win, it gives the observer-record<->section
  map without a positive state. But the **conjugation** is a **square-root-level** object, and no amount of
  flow data yields an `eta`-positive square root when the metric inverse is unbounded. The adversary must
  either (a) supply a positive reference weight -- which is HORN Q, the removable-ghost horn `W87` closed for
  GU -- or (b) concede the square root is unavailable. **Conceded: the flow/section half survives; the
  conjugation half does not.**
- *Against CONSTRUCTIBLE ("half-sided modular inclusion reconstructs `J` from geometry, bypassing the
  state").* Answered: Borchers/Wiesbrock reconstruct `J` from an inclusion `N subset M` **plus a translation
  `U(t)` with a POSITIVE generator** (the spectrum condition). In the indefinite metric an `eta`-selfadjoint
  generator has **real but sign-indefinite** spectrum -- the ghost IS the failure of the spectrum condition
  (`W91` T4: real spectrum `[-0.866, +0.866]`, not one-sided). So HSMI needs a **positive-generator** the
  Krein flow does not supply: it **relocates** positivity to the spectrum condition, the same residual.
- *Against OBSTRUCTED ("if the square root is unavailable, the route is a no-go").* Answered: it is **not** a
  no-go, because (i) the flow/cocycle/section half **genuinely survives**, and (ii) the residual
  (definitizability = a positive reference weight exists) is a **decidable shared condition**, not a proven
  impossibility -- the same open question Branch 2 reaches. And the **abstract** Lawvere firewall needs only
  the `Z/2` **label-involution** on `{admissible, inadmissible}` (no `Delta` at all), so the residual bites
  only the **physical** type-III modular realization (`W84`/`W87`).

The three pushes are mutually consistent: the route is neither a positivity-bypass nor a no-go -- it **splits**.

### Persona 4 -- CROSS-CHECKER (the literature + the toy)

**Literature (2026-07-13, read-only).**
- **Gottschalk 2002** confirmed -- `Delta^{it}` = boost, BW analyticity on Krein; the flow half is a theorem.
- **Wiesbrock 1993 / Borchers 1992** confirmed -- half-sided modular inclusions are characterized by a
  one-parameter unitary group with **positive Hermitian generator**; Borchers' commutation relations use a
  translation of **positive generator**. The positivity is the spectrum condition, not removable in general.
- **Araki / Connes relative modular theory** confirmed -- the relative modular operator `Delta_{phi|psi}` is
  **positive, non-singular, self-adjoint**; the cocycle `(D psi : D phi)_t = Delta_psi^{it} Delta_phi^{-it}`
  is built from the flows and lies in `M`. So the cocycle is flow-level (survives) but the relative modular
  operator is positive (its square root needs a positive anchor).
- **Langer / Krejcirik-Siegl** confirmed -- the infinite-rank definitizability residual (bounded metric,
  unbounded inverse), the SAME residual Branch 2 reduces to.
- **arXiv:2606.13251** -- positive KMS `<=>` quasi-Hermiticity (HORN Q/K), the physics form of "a positive
  reference weight exists `<=>` definitizable."

**Toy (`W91`, exact, numpy-only).** Reuse the repo's exceptional-point model (`W52`) as the definitizability
proxy (`r -> 1` = the UV approach to the exceptional locus, `W53`).
- **T1 -- flow survives, `J` needs positivity:** `Delta^{it}` is `eta`-unitary to `2.4e-14` for all `r`; the
  `eta`-positivity margin of `Delta^{1/2}` degrades `1.284 -> 0.158`. The two are cleanly separated.
- **T2 -- relative flow/cocycle survives:** the Connes cocycle obeys the cocycle identity to `1.7e-16`, is
  unitary in `M` to `2.2e-16`, is built from flows only, and its rate-invariant content is stable under
  `tau -> 3 tau` to `4.8e-5` (matching the branchB rate-independence discipline).
- **T3 -- relative `J` still needs a positive anchor:** the relative modular operator's `eta`-positivity
  margin degrades `1.075 -> 0.168`, **tracking** the absolute case `1.284 -> 0.158` -- the relative and
  absolute conjugations fail together.
- **T4 -- HSMI relocates positivity:** the `eta`-selfadjoint generator has real spectrum `[-0.866, +0.866]`
  but is **sign-indefinite** (spectrum condition broken) -- HSMI's positive generator is not supplied.

Two independent faces agree: the **flow/cocycle/section** structure is positivity-free; the **conjugation**
structure reduces to definitizability.

### Persona 5 -- SYNTHESIZER (the verdict)

See Sections 2-4.

---

## 2. VERDICT: REDUCES-TO-DEFINITIZABILITY (the algebraic/relative route SPLITS)

**The route splits into two halves with different characters:**

- **(A) The FLOW half -- CONSTRUCTIBLE without the positive state.** The modular flow `Delta^{it}`
  (Gottschalk), the algebraic KMS relation, and the Connes cocycle `(D psi : D phi0)_t` (the **relative
  flow**) are all built from flows / automorphisms, **never** from a positive square root. This half
  **realizes the observer's VALUE-SELECTION** -- choosing the selected weight `psi` against a reference `phi0`,
  which genuinely breaks the symmetry -- and it **IS the observer-record<->section map** (`path5-branchB`,
  now positivity-free at the flow level). **A genuine advance:** the conjecture's first-theorem object (the
  section map) has an algebraic realization that does not need the unavailable positive state.

- **(B) The CONJUGATION half -- REDUCES to the shared definitizability residual.** The firewall's antilinear
  `J = S Delta^{-1/2}` needs an `eta`-positive square root. Neither the absolute nor the relative construction
  supplies it without a **positive anchor**: the relative modular operator `Delta_{phi,psi}` is `eta`-positive
  and its square root still requires a positive reference weight `phi0`. Half-sided modular inclusions
  relocate the same positivity to the spectrum condition, which the indefinite metric breaks. So:
  **a relative `J` exists IFF a positive reference weight exists IFF `Delta` is definitizable at infinite
  rank** -- the SAME residual Branch 2 reaches.

**Neither CONSTRUCTIBLE nor OBSTRUCTED.** Not CONSTRUCTIBLE: no genuine relative `J` bypasses positivity for
the conjugation. Not OBSTRUCTED: the flow/section half genuinely survives, and the residual is a **decidable
shared condition**, not a no-go.

---

## 3. The four tasks, answered

**(1) Which piece of TT needs the positive state, which survive (per Gottschalk)?** The **only** piece that
needs positivity is the `eta`-positive **square root** `Delta^{1/2}` in the polar decomposition `S = J
Delta^{1/2}` -- hence the **conjugation `J`**. What survives without it: the **flow** `Delta^{it}` (Gottschalk,
built from `log Delta`), the **algebraic KMS** relation (metric-independent), and the **Connes cocycle**
(built from the two flows). `eta`-selfadjoint + real-positive spectrum is **not** enough for the square root:
`eta`-positivity of `Delta^{1/2}` is a **separate definitizability** condition (`W91` T1).

**(2) Can `J = C.PT` be built from the Krein flow + a half-sided modular inclusion, without a positive
`Delta`?** **No.** HSMI (Wiesbrock/Borchers) reconstructs `J` from an inclusion + a translation with a
**positive generator** (the spectrum condition). In the indefinite metric the `eta`-selfadjoint generator has
**real but sign-indefinite** spectrum (`W91` T4) -- the ghost is exactly the failure of the spectrum
condition. HSMI therefore **relocates** positivity from "positive KMS state" to "positive-spectrum generator,"
which the Krein flow does not supply -- the same definitizability residual in a different coordinate.

**(3) The KEY CONCEPTUAL MOVE -- does a relative/observer-indexed `J` exist where the absolute one does
not?** The relative move is **exactly right for the mechanism**: the absence of a distinguished state IS the
observer's value-selection, and relative modular theory (a reference `phi0` + the selected `psi`) is the
symmetry-breaking that realizes it. **And for the FLOW / the section map, it delivers** -- positivity-free
(`W91` T2). **But for the CONJUGATION it does not**: relative modular theory replaces one positive state by a
**pair**, removing the **uniqueness** requirement but **not** the **positivity** requirement -- the relative
modular operator is still `eta`-positive and its square root still needs a positive **reference** weight. At
HORN K (GU's genuinely-indefinite, non-definitizable vacuum, `W87`) **no** positive weight exists at all, so
even the reference has no positive representative and the relative `J` fails **exactly where** the absolute
one does (`W91` T3, the two margins degrade in lockstep). **So a relative `J` does NOT exist where the
absolute one does not.** The relative idea is a genuine advance for the value-selection and the section map;
it is **not** a positivity bypass for the firewall.

**(4) VERDICT.** **REDUCES-TO-DEFINITIZABILITY.** Stated in the shared-residual coordinate: **Branch 3
(algebraic/relative) and Branch 2 (Shulman quasivector) reduce to the SAME open question** -- *is the region
algebra's modular `Delta` DEFINITIZABLE at infinite rank (equivalently, does a positive reference weight
exist)?* `W84`/`W87`'s repo-native indication (`||C|| -> inf` at the UV exceptional locus, the Reuter/AS FP at
`f_2^2*=0`) places GU on **HORN K** (non-definitizable) -- so the **physical** relative `J` is walled, but the
**flow/section** half and the **abstract** `Z/2`-label firewall (Lawvere no-closure) **stand**.

---

## 4. Consequence for the campaign (H61 -> H63) and for the conjecture

- **The residual is now LOCALIZED.** After this branch, the observer conjecture's Krein-TT leg is not a
  monolithic "build type-III Krein Tomita-Takesaki." It splits: the **flow / cocycle / observer-record<->
  section** half is **discharged on the algebraic skeleton without a positive state** (a genuine reduction of
  the open surface), and the **only** remaining obstruction is the **conjugation** half -- the `eta`-positive
  square root = definitizability = a positive reference weight. `path5-branchB`'s "Gap A (Krein modular
  theory)" is thereby sharpened: its **cocycle/weight** content is positivity-free (constructible now); only
  its **conjugation** content carries the residual.
- **For H63.** Re-found the payoff theorem on the algebraic skeleton exactly as `W74`/`W84` recommended:
  state the flow (Gottschalk), the algebraic KMS relation, and the **relative** cocycle (the section map) as
  the positivity-free arena, and state the single postulate as **"the modular `Delta` is definitizable at
  infinite rank (a positive reference weight exists)"** -- the residual the firewall's `J^2=1` flip (L2)
  needs. The **abstract** Lawvere no-closure (the GU-independent credibility headline) needs only the `Z/2`
  label-involution and is **independent** of this postulate.
- **The honest strongest outcome this branch could have produced** was a genuine relative `J` bypassing
  positivity (CONSTRUCTIBLE -> frontier resolvable). **It did not.** What it produced instead is (i) a **real
  positive result** -- the flow/section half is positivity-free, realizing the value-selection algebraically
  -- and (ii) a **precise reduction** of the remaining obstruction to the shared definitizability residual,
  confirming Branch 2's target from an independent (relative-modular) direction. Do not overclaim a
  construction: the conjugation is walled at the shared frontier, not built.

---

## 5. Confidence grade and what would move it

- **Flow `Delta^{it}` survives without positivity:** **high** (Gottschalk theorem; `W91` T1 exact).
- **Connes cocycle / relative flow / section map survives without positivity:** **high** (built from flows;
  `W91` T2 exact; matches `path5-branchB` at the selection level).
- **Relative `J` still needs a positive anchor (no positivity bypass for the conjugation):** **high** -- the
  relative modular operator is positive (Araki), its square root needs a positive reference; `W91` T3 shows
  the relative and absolute margins degrade together.
- **HSMI relocates positivity to the spectrum condition:** **medium-high** -- Borchers/Wiesbrock use a
  positive generator; `W91` T4 shows the Krein generator is sign-indefinite; the general Krein-HSMI theory is
  not fully developed in the literature, so "relocates, not removes" is a strong argument rather than a cited
  theorem.
- **GU sits on HORN K (non-definitizable):** **medium** -- inherited from `W87` (repo-native indication, not
  proven here).
- **VERDICT = REDUCES-TO-DEFINITIZABILITY:** **medium-high** -- the split is rigorous (flow survives /
  conjugation needs positivity are both theorem-backed); which horn GU lands on is the residual open, and it
  is the SAME residual Branch 2 reaches (cross-confirmed).

**What would move it most:** (a) an infinite-rank / type-III Krein conjugation theorem **under
definitizability / a positive reference weight** (would close HORN Q's conjugation leg conditionally, matching
the flow half); (b) a proof that GU's region-algebra `Delta` is **non-definitizable** at infinite rank (would
harden HORN K from indication to theorem -- the shared computation with Branch 2 and `W53`); (c) a Krein
half-sided modular inclusion theorem that reconstructs `J` from a **definitizable** flow without an explicit
positive generator (would convert the relocation of T4 into a decidable criterion).

---

## 6. What this does NOT do

No GU claim-status, `CANON.md`, `RESEARCH-STATUS.md`, verdict, or public-posture change. No external action;
all citations are read-only literature. The conjecture remains a conjecture; H61/H63 remain **OPEN** with the
residual **localized to the conjugation half** and the flow/section half discharged positivity-free. The
deliverable is: the precise positivity dependency (only the `eta`-positive square root / `J` needs it); the
positivity-free algebraic realization of the flow, the algebraic KMS relation, and the relative cocycle (the
section map = the observer's value-selection); the demonstration that the relative move removes uniqueness but
not positivity (relative `J` exists IFF a positive reference weight exists IFF definitizability); the HSMI
relocation of positivity to the spectrum condition; and the statement of the outcome in the shared-residual
coordinate (Branch 2 and Branch 3 reduce to the same infinite-rank definitizability question). Reproducible:
`tests/W91_algebraic_modular_skeleton.py` (5/5, exit 0).
