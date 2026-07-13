---
artifact_type: exploration
status: exploration (STEELMAN 3 of the post-W98 rescue routes; first big swing, kill-or-learn; 5-persona inline team; literature read-only + deterministic test)
created: 2026-07-13
hypothesis: H61 / H61a (the observer-conjecture critical path, post-W98) -- steelman 3: the break is the correct phenomenology of being an observer
conjecture: "the source action IS the observer (CONJECTURE-source-action-is-the-observer-2026-07-11.md)"
branch: "STEELMAN 3. The W98 survivor/casualty split is EXACTLY one-sided vs two-sided: what survived (modular flow, algebraic KMS, Connes cocycle / section map, per-region structure) is every operation an INSIDE observer performs; what broke is ONLY J -- the operator mapping M to its COMMUTANT, i.e. (Bisognano-Wichmann) the reflection through the horizon into the causally complementary side. Steelman: the theory retains the COMPLETE set of one-sided physical operations and loses exactly the one two-sided operation no inside observer could perform anyway. THE BAR: prove or refute J-FREENESS OF THE PHYSICAL CONTENT -- every load-bearing one-sided quantity expressible in the flow+cocycle algebra without any J. The circularity trap ('physical' quietly redefined as 'J-free') is the named danger; the enumeration is fixed EX-ANTE."
title: "VERDICT = VIABLE-EARNED (audit-grade, conditions named; NOT yet a one-sidedness theorem). The J-freeness audit passes on every load-bearing one-sided quantity, and the mechanism is sharp: the W98 break is a SUP-LEVEL (uniform-boundedness-over-the-mode-tower) event, while every enumerated physical quantity is a STATE-LEVEL or FUNCTION-LEVEL object that never takes that sup. (i) Expectation values: state+algebra only. (ii) S-matrix construction: Haag-Ruelle/LSZ from local data, no J. (ii-b) CROSSING (danger point): the amplitude-level crossing relation is per-state analytic continuation -- Bros-Epstein-Glaser (1965) prove 2->2 crossing from LSZ+locality+spectral condition with NO operator J; modularly it is the wedge flow continued to Im t = 1/2, and on the W98 interacting Krein tower the per-mode strip factor grows only polynomially (~k^{1/2}, since 1-r_k ~ m2^2/4gk) so any fixed wave packet's continuation is finite and cutoff-convergent while the sup a bounded J needs diverges. (iii) Value-selection: Connes cocycle, flows only, all-orders (W91/W97). (iv) ARAKI RELATIVE ENTROPY (danger point): S(psi||phi) = -<xi_psi, log Delta_{phi|psi} xi_psi> uses ONLY the relative modular OPERATOR's log (the flow's generator); the polar decomposition contains J but the entropy never uses the polar part -- proven constructively on the finite-dim standard form (Araki formula computed with no J in the code path, matches the trace formula to 1e-15). (v) KMS thermality: the same strip continuation, t -> i. (c) Knowing the outside exists: the commutant's EXISTENCE is an algebra-level fact (computed as the kernel of the commutator map, no J); the inside theory needs no operator MAPPING onto it. WHAT GENUINELY NEEDS J: the CPT operator Theta (BW: built from J_W, maps M(W) onto M(W')) and operator Haag duality x -> JxJ -- and these coincide EXACTLY with the ex-ante TWO-SIDED set (operations whose definition references the causal complement). The break removed only the God's-eye operation. CIRCULARITY GUARD: the enumeration was fixed ex-ante from the conjecture's mechanism doc + standard scattering/measurement theory, INCLUDING the adversary's items (crossing, Araki entropy, CPT), and the one-sided/two-sided classifier is BW-geometric, fixed before the audit ran -- DEAD was reachable and was not reached. NAMED CONDITIONS (none a J-need): C1 ghost internal lines inherit path-2's contour/positivity frontier; C2 one-sided asymptotic completeness assumed; C3 the interacting per-state strip continuation is Gottschalk-grade; C4 relative-entropy monotonicity/positivity (Uhlmann) classically uses Hilbert positivity, restriction to the admissible sector unproven. PATH: the ONE-SIDEDNESS THEOREM is scoped; first decisive computation = the per-state/sup-level separation theorem in the interacting continuum (prototyped quantitatively in W105 T3)."
grade: "exploration / one audit-grade result (all load-bearing one-sided quantities J-free; the J-needing set == the ex-ante two-sided set) + one sharp mechanism (the break is sup-level, physical quantities are per-state; per-mode growth polynomial ~k^{1/2} vs divergent sup) + two danger-point computations settled (Araki entropy needs only log Delta_rel, constructive standard-form proof; crossing is function-level analyticity, BEG 1965, no operator J). Encoded in tests/W105_steelman3_j_freeness.py (7/7, numpy-only, exit 0). Literature read-only 2026-07-13: Araki 1976 (relative entropy via the relative modular operator only); Bros-Epstein-Glaser 1965 (crossing without J); Bisognano-Wichmann (J = CRT reflection = the two-sided classifier); Gottschalk 2002 (Krein flow + strip analyticity); Haag-Ruelle/Hepp (S-matrix from local data); Guido-Longo 1995 (spin-statistics from modular covariance, flow-level); Uhlmann 1977 (monotonicity -- the C4 residual). NOT an all-orders one-sidedness theorem; conditions C1-C4 named. No canon, RESEARCH-STATUS, CANON, claim-status, verdict, or public-posture change. The conjecture remains a conjecture; the W98 break STANDS as an operator statement -- this swing reinterprets its SCOPE, earned at audit grade."
depends_on:
  - explorations/break-sectorial-closure-interacting-2026-07-11.md
  - explorations/branch3-algebraic-modular-skeleton-2026-07-11.md
  - explorations/cond-ii-finite-resolution-aqft-2026-07-11.md
  - explorations/cond-iii-w54-all-orders-2026-07-11.md
  - explorations/CONJECTURE-source-action-is-the-observer-2026-07-11.md
  - GEOMETER-VS-PHYSICS-OBJECTS.md
  - tests/W98_break_sectorial_closure.py
  - tests/W91_algebraic_modular_skeleton.py
  - tests/W96_cond_ii_aqft.py
  - tests/W97_cond_iii_all_orders.py
scripts:
  - tests/W105_steelman3_j_freeness.py
external_refs:
  - "H. Araki, Publ. RIMS 11 (1976) 809 -- relative entropy of states of von Neumann algebras: S(psi||phi) = -(xi_psi, log Delta_{phi|psi} xi_psi). Only the relative modular OPERATOR enters; the polar J-part never does. (Modern exposition: E. Witten, Rev. Mod. Phys. 90 (2018) 045003.)"
  - "J. Bros, H. Epstein, V. Glaser, Comm. Math. Phys. 1 (1965) 240 -- crossing for two-particle amplitudes proved from LSZ + locality + the spectral condition by analytic continuation in the invariants: a FUNCTION-level theorem; no operator J appears in the proof."
  - "J. J. Bisognano & E. H. Wichmann, J. Math. Phys. 16 (1975) 985; 17 (1976) 303 -- J_W is the CRT reflection through the wedge edge onto the causal complement: the geometric fact that J IS the two-sided swap (used here as the EX-ANTE one-sided/two-sided classifier, independent of the audit's outcome)."
  - "H. Gottschalk, J. Math. Phys. 43 (2002) 4753 -- Krein Bisognano-Wichmann: the modular flow and its strip analyticity (dense analytic vectors) survive the indefinite metric; the per-state continuation input for crossing/KMS at HORN K."
  - "R. Haag / D. Ruelle / K. Hepp -- Haag-Ruelle scattering theory: the S-matrix is constructed from LOCAL fields, asymptotic limits, the mass gap, and the spectrum condition; no modular conjugation enters the construction."
  - "D. Guido & R. Longo, Comm. Math. Phys. 172 (1995) 517 -- spin and statistics from modular COVARIANCE (the flow); the PCT operator is a DERIVED packaging, not an input to the statistics phase."
  - "A. Uhlmann, Comm. Math. Phys. 54 (1977) 21 -- monotonicity of relative entropy under completely positive maps; the proof uses Hilbert-space positivity (interpolation), the source of named condition C4."
---

# Steelman 3 -- the J-freeness audit: is the break the correct phenomenology of being an observer?

**Role.** `W98` broke the sectorial closure: for a genuine interacting type-III_1 region there is **no
bounded modular conjugation `J`**, global or regional. This swing tests the third rescue route -- the
steelman that the survivor/casualty split is **exactly one-sided vs two-sided**. Survived (`W91`/`W96`/
`W97`): the modular flow, the algebraic KMS relation, the Connes cocycle / section map (the
value-selection), per-region modular structure -- every operation an **inside** observer performs on its
**own** algebra. Broke (`W90`-`W93`, `W98`): exactly one object, `J` -- the antilinear map of the algebra
onto its **commutant**, which Bisognano-Wichmann identify geometrically as the **reflection through the
horizon into the causally complementary side**. If the steelman is right, the theory retains the complete
set of one-sided physical operations and loses only the one two-sided operation no inside observer could
perform anyway (compare black-hole complementarity: the interior<->exterior map is not an operator of
either observer's algebra), and the break is the conjecture's **phenomenology**, not a wall.

**The bar (set by the task, W94-style sloppiness forbidden):** prove or refute **J-freeness of the
physical content** -- every load-bearing **one-sided** quantity expressible in the
`{one-sided algebra, flow, cocycle}` skeleton without any `J`. The named danger is the **circularity
trap**: "physical = J-free" would be vacuous. Section 1 fixes the enumeration **ex-ante**, before any
J-analysis.

**Answer: VIABLE-EARNED (audit-grade; NOT yet a one-sidedness theorem).** All seven load-bearing
one-sided quantities audit J-free -- including the two danger points, Araki relative entropy and crossing
symmetry -- and the set that genuinely needs `J` coincides **exactly** with the ex-ante two-sided set
(the CPT operator `Theta` and operator Haag duality `x -> JxJ`, i.e. the swap itself). The sharp
mechanism: the `W98` break is a **sup-level** (uniform-boundedness-over-the-mode-tower) event, and every
enumerated physical quantity is a **per-state / function-level** object that never takes that sup.

**Artifacts:** this file + deterministic `tests/W105_steelman3_j_freeness.py` (7/7, numpy-only, exit 0).
**Not committed. Not a claim-status change.** Exploration-grade.

---

## 0. Construction forks (GEOMETER-VS-PHYSICS-OBJECTS.md discipline)

| Object | Construction used | Load-bearing here |
|---|---|---|
| **The physical-operation enumeration** | **standard-physics side**: measurement theory (expectation values, distinguishability) + scattering theory (S-matrix, crossing, unitarity) + the conjecture's own mechanism doc (value-selection, KMS/mu_DW, grading). | The enumeration must be fixed on grounds INDEPENDENT of the audit's outcome; both sources are external to the J-question. Named, not defaulted: the answer to "what must a physics deliver" lives on the standard side; "what the mechanism itself performs" on the program-native side. Both are included. |
| **The one-sided/two-sided classifier** | **standard-physics (BW geometry)**: an operation is two-sided iff its DEFINITION references the causal complement `M'`. | This is the circularity firewall: the classifier is a geometric fact (Bisognano-Wichmann: `J` = reflection into the complement), computable before and independent of any J-freeness result. |
| **Ghost clearance** | GU-native **keep-and-grade** (Krein), as everywhere on this path. | The break and the audit both live on this fork; the sup-level divergence is the kept ghost's UV degeneracy (`W98`). |
| **The modular objects** | the antilinear `J = S Delta^{-1/2}` (broken, `W98`) vs the flow `Delta^{it}` / `log Delta` (surviving, Gottschalk). | The audit's whole content is WHICH of the two each physical quantity consumes. |

**The one fork this swing turns on (named):** *is a physical quantity an OPERATOR-level object (needs a
uniformly bounded map on the whole space) or a STATE/FUNCTION-level object (evaluated on fixed vectors /
as boundary values of analytic functions)?* The `W98` break killed an operator-level object (`J` must be
bounded: `J^2 = 1` + anti-isometry force uniform control over the whole mode tower). The audit finds every
enumerated physical quantity on the state/function level. This is not a redefinition -- it is the same
distinction `W97` already used (per-quantity finite vs sup unbounded), now applied systematically.

---

## 1. The enumeration, fixed ex-ante (the circularity guard)

The list of physical operations is fixed from two sources **before** any J-analysis, and deliberately
**includes** the adversary's strongest items:

**(E1) The conjecture's own mechanism** (`CONJECTURE-source-action-is-the-observer`, Secs 2-6): the
value-selection (choosing `psi` against a reference `phi0` -- the Connes cocycle / section map); the
KMS/thermality of the observer's horizon (the mu_DW / modular-temperature identification); the
admissibility grading. These are the operations the mechanism itself performs.

**(E2) Standard scattering and measurement theory** (what ANY physics must deliver): expectation values
of observables in physical states; an S-matrix, **with crossing symmetry and unitarity** (crossing is not
optional for a relativistic S-matrix -- the adversary is right about that, so it is IN the list);
distinguishability of states (Araki relative entropy -- the standard quantity most entangled with modular
theory); and, from the audit brief's danger point (c), whether the inside theory needs to *know there is
an outside*.

**The classifier** (fixed ex-ante, geometric): an operation is **two-sided** iff its **definition**
references the causal complement `M'`. By Bisognano-Wichmann, `J_W` is the CRT reflection through the
wedge edge **onto the complement** -- so the CPT operator `Theta` (built from `J_W`) and the operator
implementation of Haag duality (`x -> JxJ in M'`) are two-sided **by definition**, before any audit runs.
Everything in (E1)+(E2) above is one-sided by the same criterion: both crossing channels are amplitudes
among the observer's **own** asymptotic states; relative entropy compares two of the observer's **own**
states; the cocycle lives **in `M`**.

**Why this is not circular (the trap, answered up front).** Three independent facts: (1) the enumeration
sources (mechanism doc; textbook scattering/measurement) predate and do not mention `J`; (2) the
classifier is BW geometry, not J-freeness -- it was applied before the audit and its output (7 one-sided,
2 two-sided) is recorded as data in `W105` T1 with all audit fields empty at declaration; (3) **DEAD was
reachable**: crossing and Araki entropy are one-sided by the classifier yet classically credited to `J`
in the literature -- had either genuinely consumed a bounded `J`, the verdict would have been DEAD. One
item did audit J-needing (`Theta`); it is excluded from "load-bearing one-sided" by the **prior**
geometric criterion, not by its audit outcome.

---

## 2. Five-persona team (inline, sequential, single context)

### Persona 1 -- modular/operator specialist (danger point (a): Araki relative entropy)

**The exact dependency.** Araki's relative entropy is
`S(psi||phi) = -<xi_psi, log Delta_{phi|psi} xi_psi>`. The relative modular operator
`Delta_{phi|psi} = S_{phi,psi}^+ S_{phi,psi}` is built from the closable antilinear
`S_{phi,psi}(a xi_phi) = a^* xi_psi` and its **adjoint** -- not its polar decomposition. The polar
decomposition `S = J Delta^{1/2}` **contains** `J`, which is why the danger point is real -- but the
**entropy formula consumes only `log Delta_{phi|psi}`**, the generator of the **relative flow**, which is
exactly the half that survived (`W91`: the relative flow and cocycle are flow-level; Gottschalk:
`log Delta` exists whenever the spectrum is real, which holds at every finite scale per `W97`).

**Constructive proof (`W105` T2).** On the genuine finite-dimensional standard form (`M = Mat_2` by left
multiplication on `HS(C^2)`, `Delta_{phi|psi}: X -> rho_phi X rho_psi^{-1}`, `xi_psi = rho_psi^{1/2}`),
the Araki formula is **computed with no `J` and no square root in the code path** and matches the
independent trace formula `tr rho_psi (log rho_psi - log rho_phi)` to `1.8e-15`, for generic
non-commuting densities. This is a constructive proof that the formula's only modular input is
`log Delta_rel`. On the Krein face: the per-state entropy form stays finite across the whole
exceptional-locus approach `r: 0.3 -> 0.99` while `J`'s prerequisite (the eta-positivity margin of
`Delta^{1/2}`) degrades and the J-cost `1/sqrt(1-r)` blows up. **Araki relative entropy is J-free.**

**The honest residual (named as C4, not hidden):** the **definition** is J-free, but the
information-theoretic **properties** -- positivity, and especially monotonicity under channels (Uhlmann
1977) -- are classically proved with Hilbert-space positivity (operator interpolation). If the observer's
distinguishability calculus needs monotonicity, the admissible (eta-positive) sector must supply the
positivity input. Plausible (the admissible sector IS positive-metric), unproven here.

### Persona 2 -- scattering theorist (danger point (b): crossing and CPT)

**What the S-matrix construction needs.** Haag-Ruelle (and LSZ) build the S-matrix from **local** fields,
the mass gap (`W97`: gap protected at every finite scale), asymptotic limits, and the spectrum condition.
**No modular conjugation enters the construction.** (Condition C2: one-sided asymptotic completeness is
assumed at standard-scattering grade -- the same assumption ordinary QFT makes.)

**Crossing -- the adversary's strongest card, taken at full strength.** Crossing is NOT optional; and
Bisognano-Wichmann DO tie `J_W` to CRT. The resolution is that the literature contains **two distinct
objects** under the one word:

1. **Crossing as an analytic identity among amplitudes** (the thing an S-matrix needs): proved by
   **Bros-Epstein-Glaser (1965)** for 2->2 from LSZ + locality + the spectral condition, by analytic
   continuation in the Mandelstam invariants. **No operator `J` appears anywhere in the proof.** It is a
   FUNCTION-level theorem: an equality of boundary values of one analytic function. Modularly, the same
   continuation is the wedge flow taken to `Im t = 1/2` **evaluated in fixed states**.
2. **CRT as a bounded operator** (`Theta`, `J_W`): the operator that packages the endpoint of that
   continuation **together with the reflection onto the complement**. This is the two-sided object, and
   it is the `W98` casualty.

**The quantitative separation (`W105` T3, the heart of the swing).** On the `W98` interacting Krein tower
(`1 - r_k ~ m2^2 / 4gk` in the UV): the per-mode strip factor `<e, eta_+(r_k)^{-1/2} e>` grows only
**polynomially** (`~ k^{1/2}`; measured factor 3.94 over a 16x momentum span), so any fixed Schwartz wave
packet's crossing/KMS continuation is **finite and cutoff-convergent** (kmax 1e3 -> 4e3 changes it below
`1e-10`); while the **uniform** bound a `J` requires (`sup_k ||eta_+(r_k)^{-1/2}||`) **diverges** under UV
doubling -- the `W98` break, reproduced inside this test. **The break is carried entirely by the
uniformity; no fixed amplitude loses its crossing continuation.** The same strip continued to `t -> i` is
the algebraic KMS relation -- so horizon thermality is the same J-free object (`W91`).

**The honest residual (C1, named):** crossing needs the spectrum condition. The FULL Krein doublet
generator is sign-indefinite (`W105` T6: spec `{+3.0, -3.015}` at the probe momentum) -- the adversary is
right that this input is not free. But external physical amplitudes use the **admissible** (eta-positive)
sector, where the generator IS positive; ghost **internal** lines inherit the **path-2 contour frontier**
(Cutkosky/fakeon/Lee-Wick) -- a positivity/contour question, already open and owned by path 2, **not a
J-need**. If path 2 kills admissible-sector crossing, the theory dies for a different reason; the
steelman's claim is only that `J` is not what crossing consumes.

**Spin-statistics and antiparticles** (what CPT delivers observably, inside): the statistics phase is
derivable from modular **covariance** of the flow (Guido-Longo 1995) and classically from
Wightman-function analyticity (Jost) -- both function/flow-level; antiparticle (conjugate-sector)
existence is DHR theory on the field algebra, one-sided. The Krein transfer of Guido-Longo is
strong-argument only (Hilbert theorem as stated) -- part of C3's grade, flagged.

### Persona 3 -- ADVERSARY (the two named pushes, answered)

- *Push 1: "crossing symmetry and CPT are not optional -- any relativistic S-matrix needs them, and they
  are theorems ABOUT `J`."* **Half right, and the half matters.** Crossing is not optional -- it is IN
  the enumeration and the audit had to pass it, not dodge it. But "crossing is a theorem about `J`" is
  historically backwards: BEG proved crossing in 1965 **without** `J`; Bisognano-Wichmann in 1975 showed
  the analytic data can additionally be **packaged** into a bounded operator in the positive-metric case.
  At HORN K the packaging fails while the analytic data survives (Gottschalk flow + per-state
  continuation; `W105` T3 quantifies the separation). What IS a theorem about `J` is the CPT **operator**
  `Theta` -- and `Theta` maps `M(W)` onto `M(W')`: it is the swap, classified two-sided ex-ante. An
  inside observer uses crossing relations among its own amplitudes; it never applies `Theta`.
- *Push 2 (the circularity trap): "you are quietly redefining 'physical' to mean 'J-free'."* **Answered
  structurally, not rhetorically** (Section 1 + `W105` T1): the enumeration comes from the mechanism doc
  and textbook scattering/measurement theory, fixed with the classifier before the audit; the adversary's
  own items are in the list; the audit fields were empty at declaration; DEAD was reachable (a genuine
  J-need in crossing or Araki entropy would have returned it). And one item DID audit J-needing
  (`Theta`) -- it is excluded from the one-sided set by the prior BW-geometric criterion, not by its
  outcome. The non-vacuousness witness is crossing itself: one-sided by the classifier, classically
  credited to `J`, and the audit had to (and did) find its J-independence by an argument (BEG +
  per-state analyticity), not by fiat.
- *Push 3 (the residual push): "then the steelman is unfalsifiable -- anything that breaks will be
  declared two-sided."* No: the classifier is fixed. If a future computation shows a **one-sided**
  quantity (e.g. admissible-sector crossing at two loops, or entropy monotonicity) genuinely requires a
  bounded `J`, the steelman dies -- the fork stays sharp and is written into the test's booleans
  (`verdict_DEAD_...` is a live, checkable flag, currently `False`).

### Persona 4 -- CROSS-CHECKER (the audit table + the literature)

The per-quantity audit (the deliverable; = `W105` output):

| # | Physical operation (source) | Ex-ante side | What it consumes | Needs `J`? | Evidence |
|---|---|---|---|---|---|
| i | Expectation values of own observables (measurement) | one-sided | state + algebra | **NO** | trivial; W105 T4 |
| ii | S-matrix construction (Haag-Ruelle/LSZ) | one-sided | local fields, gap, asymptotics | **NO** (C1, C2) | [HR]; W105 T4 |
| ii-b | **Crossing symmetry** (scattering; danger point) | one-sided | per-state strip continuation of the flow + admissible-sector spectrum condition | **NO** | BEG 1965; W105 T3 |
| iii | Value-selection (cocycle / section map; mechanism doc) | one-sided | the two flows only | **NO** (all-orders) | W91/W97; W105 T4 |
| iv | **Araki relative entropy** (distinguishability; danger point) | one-sided | `log Delta_{phi|psi}` only | **NO** (C4 on monotonicity) | Araki 1976; W105 T2 constructive |
| v | KMS thermality of the horizon (mechanism doc) | one-sided | the same strip, `t -> i` | **NO** | W91; W105 T3 |
| c | Knowing the outside exists (audit brief (c)) | one-sided | nontriviality of `M'` = algebra-level | **NO** | W105 T4 (commutant found with no `J`) |
| -- | CPT operator `Theta` | **two-sided** | `J_W` (BW) | **YES** | BW; dies with W98 |
| -- | Operator Haag duality `x -> JxJ` | **two-sided** | `J` | **YES** | Tomita; dies with W98 |

**The discriminator (`W105` T5): `{needs J} == {two-sided ex-ante}`, exactly.** Computed as a set
equality, not asserted.

**Literature check (2026-07-13, read-only).** Araki 1976: the relative entropy formula consumes only the
relative modular operator -- confirmed (Witten's RMP review states the formula in exactly this form).
BEG 1965: crossing from LSZ + locality + spectrum, function-level -- confirmed. BW: `J_W` = CRT
reflection onto the complement -- confirmed (this is the classifier). Gottschalk 2002: Krein flow +
dense analytic vectors -- confirmed (`W91`/`W96`). Guido-Longo: statistics from modular covariance --
confirmed at Hilbert grade; Krein transfer is strong-argument. Uhlmann 1977: monotonicity via
positivity -- confirmed, hence C4.

### Persona 5 -- SYNTHESIZER

See Sections 3-5.

---

## 3. VERDICT: VIABLE-EARNED (audit-grade), and what "earned" means here

**The steelman's claim was falsifiable and survived its audit.** Every load-bearing one-sided quantity is
expressible in `{one-sided algebra, flow Delta^{it}, Connes cocycle, per-state strip continuation}` with
no bounded `J`; the two J-consumers are exactly the two operations whose definitions reference the causal
complement -- the swap across the firewall. The `W98` break therefore removes **only** the God's-eye
operation, and the steelman's reading stands at this grade: **the break is the phenomenology of being an
observer, not a wall through the physics.** (Complementarity analogy, support not proof: in black-hole
complementarity the interior-exterior map is likewise not an operator available to either observer.)

**The sharp mechanism (the transferable content):** the `W98` break is a **sup-level** event -- what
diverges is `sup_k ||eta_+(r_k)^{-1/2}||`, the uniform bound a bounded antilinear involution requires.
Every enumerated physical quantity is **per-state or function-level**: evaluated on fixed (Schwartz-
packet) states or as boundary values of analytic functions, where the per-mode cost grows only
polynomially (`~ k^{1/2}`) and is integrable against any physical wave packet. **No fixed physical
quantity takes the sup.** This is the same per-quantity-vs-sup structure `W97` found for localization,
now shown to cover the full physical enumeration.

**What VIABLE-EARNED does NOT mean (do not overclaim):**
- It is **not** an all-orders one-sidedness theorem. The audit is exact on the toy/tower and
  literature-backed at the named grades; the continuum interacting statement is scoped (Section 4).
- It does **not** repair `W94`: the sectorial closure (a bounded regional `J`) stays broken exactly as
  `W98` left it. The firewall-as-bounded-modular-conjugation identification stays **retracted**; what
  this swing establishes is that nothing the observer's physics needs was living on that identification.
- It does not resolve C1-C4. In particular C1 (ghost internal lines / path-2 contour) and C4 (entropy
  monotonicity at HORN K) are live ways the THEORY could still die -- for reasons that are not J.

---

## 4. The scoped path: the ONE-SIDEDNESS THEOREM

**Statement to prove.** *In the interacting Krein theory at HORN K, every element of the fixed
enumeration E is expressible in the positivity-free skeleton `{M(O), Delta^{it}, Connes cocycle,
per-state strip continuation on a dense set of analytic vectors}`; each is finite on fixed physical
(admissible, Schwartz-packet) states at every finite scale; and no step consumes a bounded `J` or
`Theta`.* The break is then localized, as a theorem, to the two-sided operator packaging.

**What it requires (in dependency order):**
1. **The per-state/sup-level separation theorem in the interacting continuum** -- the first decisive
   computation (see below). Prototyped quantitatively in `W105` T3 on the W98 tower.
2. **Interacting Krein strip analyticity** (upgrades C3): extend Gottschalk's dense-analytic-vector
   Bisognano-Wichmann from free Krein fields to the interacting Krein doublet at every finite scale --
   the input for crossing/KMS per-state continuation. Plausible route: `W97`'s all-orders
   analyticity-strip (= mass gap) argument already controls the relevant branch points.
3. **Krein Araki entropy with properties** (upgrades C4): definition via `log Delta_rel` (done, J-free);
   prove positivity + monotonicity restricted to the admissible sector (where the metric is positive) --
   likely an Uhlmann-interpolation argument run inside the eta-positive subspace.
4. **Admissible-sector crossing with ghost internal lines** (C1): shared with / owned by path 2
   (Cutkosky-fakeon contour). Not duplicated here; the one-sidedness theorem takes it as an interface.
5. **Krein Guido-Longo** (spin-statistics from the flow) -- or accept the function-level Jost route on
   the admissible sector; needed only for the "complete physical content" adjective, not the core.

**The first decisive next computation (one swing, sharp, kill-capable):** prove on the `W98` interacting
continuum model that for EVERY admissible finite-energy wave packet the `Im t in [0, 1/2]` strip
continuation and the relative-entropy form are finite and cutoff-convergent **with bounds uniform on
compact coupling/scale sets** (not uniform over the tower -- that is the break), i.e. the divergence is
carried entirely by the uniformity and never by a fixed matrix element. The `~ k^{1/2}` per-mode growth
vs Schwartz decay computed in `W105` T3 says this should go through; the kill-mode is a physical packet
class or a loop order where the per-state growth becomes non-integrable -- if found, the steelman dies
honestly (a one-sided quantity would need the sup after all).

---

## 5. Confidence grade and what would move it

- **Araki relative entropy J-free (definition):** **HIGH** -- constructive standard-form proof (`W105`
  T2, 1e-15) + Araki's formula as stated in the literature.
- **Crossing is function-level / per-state, not bounded-`J`:** **HIGH on the Hilbert side** (BEG 1965 is
  a theorem with no `J`); **MEDIUM-HIGH on the Krein side** (per-state continuation exact on the tower;
  interacting continuum is C3, Gottschalk-grade).
- **The break is sup-level; physical quantities per-state (the separation):** **HIGH on the model**
  (`W105` T3, quantitative: polynomial per-mode vs divergent sup); **MEDIUM-HIGH as a continuum claim**
  (the scoped theorem, step 1).
- **The J-needing set == the two-sided set (the discriminator):** **HIGH** given the enumeration --
  computed set equality; the classifier is BW geometry.
- **The enumeration is complete (nothing physical omitted):** **MEDIUM-HIGH** -- it covers the mechanism
  doc + standard scattering/measurement; the named residual risk is a physical quantity outside both
  sources (e.g. a genuinely global charge structure). Any candidate addition can be run through the same
  audit; the fork stays live.
- **VERDICT = VIABLE-EARNED (audit-grade):** **MEDIUM-HIGH** -- earned by a falsifiable audit that
  included the adversary's items and could have returned DEAD; capped below HIGH by C1-C4 and by the
  missing continuum theorem.

**What would move it most:** (a) the first decisive computation above (per-state/sup separation with
uniform-on-compacts bounds) -- promotes to a conditional theorem or kills; (b) an Uhlmann-type
monotonicity proof restricted to the admissible sector (C4) -- removes the entropy residual; (c) a path-2
resolution of the ghost-line contour (C1) -- external to this steelman but load-bearing for the theory;
(d) adversarially: any exhibited one-sided quantity whose per-state cost is non-integrable against
physical packets -- kills the steelman cleanly.

---

## 6. What this does NOT do

No GU claim-status, `CANON.md`, `RESEARCH-STATUS.md`, verdict, or public-posture change. No external
action; all citations are read-only literature. The conjecture remains a conjecture; the `W98` break
STANDS as an operator statement (no bounded `J`, global or regional, for a physical interacting region)
and the `W94` retraction is untouched. What this swing adds is the **scope** of the break, at audit
grade: the killed object is exactly the two-sided swap across the firewall, and the complete enumerated
one-sided physical content -- expectation values, S-matrix construction, crossing, value-selection,
Araki relative entropy, KMS thermality, outside-existence -- is expressible in the surviving
flow/cocycle/per-state skeleton with no `J`. This branch **presents, does not decide** -- it hands the
orchestrator: the ex-ante enumeration and BW-geometric classifier (the circularity answer), the
per-quantity audit table, the two danger-point computations (Araki entropy constructive; crossing
per-state vs sup-level, quantitative), the discriminator (needs-J set == two-sided set), the named
conditions C1-C4, the scoped one-sidedness theorem, and the honest verdict -- **VIABLE-EARNED
(audit-grade)**. Reproducible: `tests/W105_steelman3_j_freeness.py` (7/7, exit 0).
