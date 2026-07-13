---
artifact_type: exploration
status: exploration (HARDENING CLAUSE 2 of the Observer Structure Theorem, one swing, two tasks: (T1) the unrun sheaf-cocycle kill-mode on TRIPLE overlaps + the global-section check; (T2) the U5-derivation attempt -- remove the assumed fixed-mixing-direction leg; deterministic test + honest self-critique)
created: 2026-07-13
hypothesis: H61 / H61a (the observer-conjecture critical path, post-W109) -- clause 2 of the Observer Structure Theorem: proven only PAIRWISE (W107 T7); assumption U5 (fixed mixing direction) ASSUMED and load-bearing
conjecture: "the source action IS the observer (CONJECTURE-source-action-is-the-observer-2026-07-11.md)"
title: "T1 = COCYCLE-HOLDS + GLOBAL-SECTION-EXISTS, T2 = U5-DERIVED (model + skeleton grade, conditional on named inputs).  (T1) Three mutually-overlapping W98 regions (weights 1.0/0.45/0.20, and a radical UV-heavy/IR-heavy CROSSING pair): all three pairs cohere at class level while all three operator disagreements diverge; the comparison data satisfies the cocycle EXACTLY at every layer -- compact witnesses (the trivial layer, named), the relative modular-weight potentials theta_ij(k) = log((1-r^i)/(1-r^j)) (telescope to 1e-12, converge, and are a COBOUNDARY theta_ij -> F_i - F_j with F_i = -log w_i), and the frame aligners (trivial under U5).  The coboundary IS a global section: a weight-independent GLOBAL CLASS (same 2[P], same Krein-null line under two radically different global weights) + a global potential exist, restricting to every region -- while NO global OPERATOR exists (sup-cond diverges at every level, W98 reproduced).  Global class YES / global operator NO: the sharpest form of the clause-2/clause-3 story, earned.  THE DISCRIMINATING CONTROL (adversary answered): the cocycle's genuine failure mode is computed -- three NON-COPLANAR mixing directions give exact pairwise aligners whose loop composition is a NONZERO HOLONOMY (0.403 rad, fixes the null line, moves the transported frame/phase data); coplanar tilts compose abelianly.  HONEST LOADING: in this model class both rotated configurations already break PAIRWISE coherence, so the cocycle can fail only through the same U5 violation pairwise coherence detects -- COCYCLE-HOLDS is genuine but U5-loaded, raising T2's stakes.  (T2) On the W52 exceptional-point family H(a,b,phi) = i a sigma_z + b(cos phi sigma_x + sin phi sigma_y) the positive intertwiner is EXACTLY eta = I + (a/b)(-sin phi sigma_x + cos phi sigma_y): the mixing DIRECTION is a function of the VERTEX PHASE (the interaction's tensor structure) ALONE; (a,b) enter only as the weight r = a/b; the phi=0 member reproduces W98's eta(r_of) exactly.  DERIVED: regional modular weights (positive REAL scalars), coupling profiles g/3g/g*k (RG running of the single real coupling), momentum, and diagonal real field rescalings all leave the direction IMMOBILE to 1e-12 while r spans 0.90 .. 1-1e-10.  So U5 = interaction-universality (one Lagrangian everywhere -- standard QFT) + ONE real grading-odd vertex (W102 skeleton: single |II|^2 vertex, exact Krein-self-adjointness K M_D = M_D^dag K) + positive-real modular weights.  THE ROTATORS NAMED AND COMPUTED (the fork content relocated, not erased): (R1) a second independently-running grading-odd vertex makes the direction run with scale (1.08 rad drift) and rotate region-to-region (persistent 0.26 gap = the W107 T8 break generated from field content); (R2) a complex/CP phase rotates it 1:1.  Both ABSENT at skeleton grade.  NEW: UV SELF-PROTECTION -- bounded NON-scalar modular corrections (nested commutator c_O [H_free, H_int]) rotate by ~ c_O * Dw(k) -> 0: the same UV degeneracy that builds the wall kills every bounded commutator-type rotator at the tail; U5 need only hold asymptotically, and asymptotically it is self-enforced."
grade: "exploration / model-surrogate grade on the W98 Krein-doublet tower + the W52 exceptional-point family (the repo's own objects).  HIGH within the model: every identity is exact/machine-verified (tests/W110_triple_overlap_u5.py, 10/10, numpy-only, exit 0) -- the three-pair coherence, the cocycle exactness and coboundary, the weight-independence of the global class, the holonomy control (0.403 rad), the intertwiner law eta = I + (a/b)rot(phi) with residual < 1e-12 up to a/b = 0.999, the direction-immobility sweep, the 1:1 CP rotation, the two-vertex running drift, the Dw-suppression of nested corrections.  MEDIUM-HIGH: the U5-derivation CHAIN as a physics statement -- each link is computed, but the identification 'vertex phase = field content, fixed by the single |II|^2 vertex on the ker-Gamma carrier' rides on the W102 SKELETON (one vertex, exact Krein-self-adjointness = reality), which is reconstruction-grade, not the finished source action.  MEDIUM: the scalar-or-UV-suppressed form of genuine regional modular corrections -- the leading commutator term is computed suppressed, but the interacting double-cone modular Hamiltonian is unsolved (Casini-Huerta); an UV-non-vanishing grading-odd component would evade.  LOW-MEDIUM: extrapolation beyond the doublet surrogate.  No canon / RESEARCH-STATUS / CANON / claim-status / verdict / posture change; H61/H61a remain OPEN; W98, W100, W103, W107, W109 stand unchanged."
depends_on:
  - explorations/observer-structure-theorem-assembly-2026-07-11.md
  - explorations/krein-ratio-set-tail-coherence-2026-07-11.md
  - explorations/steelman1-adapter-tail-quotient-2026-07-11.md
  - explorations/obj5-minimal-source-action-2026-07-11.md
  - explorations/break-sectorial-closure-interacting-2026-07-11.md
  - GEOMETER-VS-PHYSICS-OBJECTS.md
  - tests/W109_observer_structure_theorem.py
  - tests/W107_krein_ratio_tail_coherence.py
  - tests/W103_steelman1_tail_quotient.py
  - tests/W102_obj5_source_action.py
  - tests/W98_break_sectorial_closure.py
  - tests/W52_path2_E_nogo.py
scripts:
  - tests/W110_triple_overlap_u5.py
external_refs:
  - "Cech cocycle / transition-function formalism (standard; e.g. R. Bott & L. W. Tu, Differential Forms in Algebraic Topology) -- the presheaf/gluing frame: pairwise comparison isomorphisms, the 1-cocycle condition on triple overlaps, coboundaries = global sections."
  - "M. V. Berry, Proc. R. Soc. A 392 (1984) 45 -- geodesic-loop holonomy on the Bloch sphere: the computed failure mode of the comparison cocycle (the loop composition of frame aligners is a rotation by the spherical-triangle solid angle)."
  - "H. Araki, Publ. RIMS 11 (1976) 809 -- relative modular theory; the clause-2 invariant whose per-region comparison data this swing composes (via W107)."
  - "A. Connes, Ann. Sci. ENS 6 (1973) 133 -- the cocycle [D psi : D phi]_t; the relative-weight potentials theta_ij are the regularized relative tail data of W103's 'unfixed spinning phase'."
  - "H. Casini & M. Huerta (reviews of entanglement/modular theory in QFT) -- the interacting double-cone modular Hamiltonian is unsolved/non-geometric: the named residual behind the 'scalar-or-UV-suppressed regional corrections' input."
  - "M. Porrati & R. Rahman -- the non-minimal RS completion behind W102's unique causal cure g = 1 (the single-vertex skeleton input to the U5 derivation)."
  - "S. Weinberg, The Quantum Theory of Fields I -- interaction-universality: the Lagrangian density is one global object; regions do not carry region-dependent interaction FORMS, only state/modular data (the standard-QFT leg of the derivation)."
---

# W110: the triple-overlap cocycle and the U5 derivation -- hardening clause 2

**Role.** The Observer Structure Theorem (`W109`) has three clauses; clause 2 (interface coherence) was
proven only **pairwise** (`W107` T7) and rests on **U5** -- the fixed-mixing-direction assumption --
which was **ASSUMED** (W103 CM1 / W107 assumption 1) and is load-bearing. This swing runs the two
hardening moves in one: **(T1)** the unrun kill-mode -- does the pairwise class-comparison data satisfy
the **cocycle condition on triple overlaps** (a genuine presheaf/net), and does a **global class** (a
global section) exist even though no global operator does? **(T2)** the **U5-derivation attempt** --
is the mixing direction fixed by the **field content** (the interaction's tensor structure, the same
Lagrangian in every region), with only the scalar weight varying?

**Answer: T1 = COCYCLE-HOLDS + GLOBAL-SECTION-EXISTS (with the U5-loading named honestly);
T2 = U5-DERIVED at model + skeleton grade (conditional on named inputs; the rotators computed and
named).** **Artifacts:** this file + `tests/W110_triple_overlap_u5.py` (10/10, numpy-only, exit 0).
**Not committed by this run. Not a claim-status change.**

---

## 0. Construction forks (GEOMETER-VS-PHYSICS-OBJECTS.md discipline)

| Object | Construction used | Load-bearing here |
|---|---|---|
| **The regions / triple overlap** | `W98` T6's own setup extended: three mode-weight profiles on the shared tower (scalar 1.0/0.45/0.20; plus radical UV-heavy/IR-heavy **crossing** profiles). | T1 is computed on the exact configuration class of the pairwise result -- no substitution. |
| **The comparison data** | **standard-math** (Cech transition data): compact witnesses; relative modular-weight potentials `theta_ij(k) = log((1-r^i_k)/(1-r^j_k))` (the regularized form of W103's unfixed tail phase); canonical geodesic frame aligners `u_ij` on the Bloch sphere. | The decisive honesty fork of T1: the witness layer is **trivially exact** (telescoping) -- named, not counted. The potential and frame layers are where content and the failure mode live. |
| **The intertwiner family** | the repo's own `W52` exceptional-point family `H(a,b,phi)`, extended by the vertex phase `phi`; the `phi = 0` member reproduces `W98`'s `eta(r_of(g,k))` **exactly** (verified). | T2 is a statement about the very metric family the break/theorem live on. |
| **The field-content input** | the `W102` source-action **skeleton**: ONE `|II|^2`-derived vertex on the ker-Gamma carrier; exact Krein-self-adjointness `K M_D = M_D^dag K` (residual 0) = real coupling; unique causal cure `g = 1`. | The skeleton is reconstruction-grade, **not** the finished source action -- this is exactly where the T2 verdict's "conditional" lives (Section 4). |

---

## 1. T1: the triple-overlap cocycle (`W110` T1-T5)

**Setup.** Three mutually-overlapping regions = three modular-weight profiles on the shared W98 tower.
Precondition first: **all three pairs cohere** at class level (metric differences `|r^i_k - r^j_k| -> 0`,
compact; same `2P`; same Krein-null line) while **all three operator disagreements diverge** -- the
W107 two-region result extends to the full triple (T1).

**The cocycle, layer by layer (T2):**

1. **Compact witnesses** `K_ij = C_i - C_j`: the cyclic sum vanishes **exactly** by telescoping. This is
   the trivial layer the adversary predicted; it is named and **not counted as content**.
2. **Relative modular-weight potentials** `theta_ij(k) = log((1-r^i_k)/(1-r^j_k))` -- the regularized
   relative form of the tail's unfixed spinning phase (`W103`). Each is computed as one independent log,
   so the cocycle identity `theta_12 + theta_23 + theta_31 = 0` is a genuine float check: it holds to
   `< 1e-12` at every `k` in `1e2..1e6`. The potentials **converge** (`theta_12 -> log(w_2/w_1)`, error
   `2.7e-3 -> 2.7e-7`) and -- the decisive structure -- they are a **coboundary**:
   `theta_ij -> F_i - F_j` with the per-region potential `F_i = -log w_i`.
3. **Frame aligners** `u_ij`: under U5 all mixing directions coincide, so `u_ij = 1` and the holonomy
   defect is zero exactly.

**Radical weights (T3).** An UV-heavy region (`w: 0.4 -> 2.5`) and an IR-heavy region (`w: 2.5 -> 0.4`)
that **cross** at `k ~ 1e3` still cohere pairwise with the constant region, the cocycle stays exact,
and the potentials converge to the log-ratio of the **UV limits**. Coherence is a property of
"weights bounded below + fixed direction", not of nearly-equal constant weights.

**The global section (T4) -- the prize, earned.** A coboundary is precisely a global section of the
potential data. And the **class** itself glues: assigning to the union the tail class computed with
*any* bounded-below global weight gives the **same** class data (same `2P` to `< 5e-3`, same null line
to `1 - 1e-9`, under two radically different global weight choices -- the `W103` rate-independence doing
real work), and this assignment restricts to every region's class. Meanwhile **no global operator
exists**: the union's sup-conditioning grows without bound under UV doubling (`1779 -> 3557 -> 7112`),
and so does every region's own (`W98`/`W109` clause 3 reproduced on the same arrays).

> **A GLOBAL CLASS EXISTS; A GLOBAL OPERATOR DOES NOT.** The interface data (`2[P]`, the null line, the
> weight potential `F = -log w`) is a genuine presheaf **with a global section**; the God's-eye
> conjugation operator is absent at every level, including globally. Clause 2 strengthens from
> "pairwise coherence" to "presheaf with a global section"; clause 3 is untouched. This is the sharpest
> form of the one-sided story the program has produced.

**The discriminating control (T5) -- the adversary answered.** "Your cocycle holds trivially because
the classes are equal by construction." Response: the cocycle has a **computed, genuine failure mode**.
Give the three regions **non-coplanar** mixing directions (`e_y`; tilted 0.9 toward `e_x`; tilted 0.8
toward `e_z`). Every pairwise aligner is exact (`u (n_j.sigma) u^dag = n_i.sigma` to `1e-12`) -- the
data is pairwise-comparable -- but the loop composition `u_12 u_23 u_31` is a **nonzero holonomy**:
a rotation by **0.403 rad** about `n_1` (the spherical-triangle solid angle) that fixes region 1's null
*line* but acts nontrivially on the transported transverse frame -- exactly the phase data `W103`
identified as the tail's unfixed datum. Coplanar tilts (W107 T8's own control family) compose
**abelianly** (defect `< 1e-12`). So triple-consistency is a real property with a real failure mode,
not a tautology.

**The honest loading (not hidden).** In this model class, **both** rotated configurations already break
*pairwise* coherence (metric difference `> 0.5`, non-compact -- `W107` T8 reproduced). So the cocycle
can only fail through the same U5 violation that pairwise coherence already detects: COCYCLE-HOLDS is
genuine but **U5-loaded** -- it does not add an independent survival beyond pairwise + U5; it **raises
the stakes of U5**. That is what makes T2 the other half of this swing rather than a separate errand.

---

## 2. T2: the U5 derivation (`W110` T6-T9)

**The intertwiner law (T6).** On the W52 minimal exceptional-point family
`H(a,b,phi) = i a sigma_z + b(cos phi sigma_x + sin phi sigma_y)`, the positive intertwiner is exactly

> `eta = I + (a/b)(-sin phi sigma_x + cos phi sigma_y)`

(residual `< 1e-12` up to `a/b = 0.999`; positive). The mixing **direction** is the vertex phase rotated
by `pi/2` -- **a function of the interaction's tensor structure alone**; the magnitudes `(a, b)` enter
only through the weight `r = a/b`. Under the identification `a = g`, `b = g + Dw(k)/2` the `phi = 0`
member reproduces `W98`'s `eta(r_of(g,k))` **exactly** -- this is the metric family of the break, the
coherence result, and the theorem, not a stand-in.

**The derivation chain (T7), each link computed:**

1. **Regional weights cannot rotate.** Modular/KMS weights are **positive real scalars**; a positive
   real multiplying the coupling changes `r`, not `phi`. Verified: direction identical to `1e-12`
   across `w in {1.0, 0.45, 0.20}` while `r` spans `0.90 .. 1 - 1e-10`.
2. **RG running of the single real coupling cannot rotate.** Profiles `g`, `3g`, `g*k` (the W109 X1
   check extended): direction immobile at every momentum.
3. **Field rescalings cannot rotate.** Diagonal real rescalings `D = diag(d1, d2)` (wavefunction
   renormalization): `eta' = D^{-1} eta D^{-1}` intertwines `H' = D H D^{-1}` (verified) and the phase
   of the grading-odd entry -- the direction datum -- is exactly invariant.
4. **Interaction-universality supplies the rest.** The vertex phase is set by the interaction
   Lagrangian's tensor structure in the doublet basis (the PU embedding of the one physical field).
   The Lagrangian is **one global object** -- regions do not carry region-dependent interaction *forms*,
   only state/modular data (standard QFT). In the W102 skeleton the interaction is **one** `|II|^2`-derived
   vertex on the ker-Gamma carrier with **exact Krein-self-adjointness** (`K M_D = M_D^dag K`, residual
   0 -- reality), so the phase is one fixed number.

> **U5-DERIVED (model + skeleton grade):** fixed direction = interaction-universality + a single real
> grading-odd vertex + positive-real modular weights. The assumption leaves the free-assumption column;
> what remains is a set of **named** inputs, each standard or skeleton-verified.

**The rotators, named and computed (T8) -- the fork content relocated, not erased.** What *would*
rotate the direction:

- **(R1) a second independently-running grading-odd vertex.** With `b_x = const` and
  `b_y ~ k^{0.3}`, the effective vertex phase **runs** (drift `1.08` rad over `1e2..1e6` -- the
  "interaction-universality fails under RG" adversary made concrete), and weighting the two vertices
  differently region-to-region produces a **persistent** direction gap (`0.26` rad, non-compact) --
  the W107 T8 rotated-frame break, now *generated from field content* rather than posited.
- **(R2) a running complex/CP phase.** A phase `delta` on the coupling rotates the direction by
  exactly `|delta|` (1:1, verified to `1e-9`).

Both are **absent at W102 skeleton grade** (one vertex; exact Krein-self-adjointness = real coupling;
the unique causal cure `g = 1` leaves no second grading-odd gravity-ghost vertex). Neither is excluded
at full-continuum grade -- that is the honest residual (Section 4).

**UV self-protection (T9) -- new, and the answer to the state-dependence adversary.** The genuine
regional modular Hamiltonian is not exactly "scalar weight x Lagrangian"; its corrections carry
commutator terms. The leading non-scalar term in the doublet model,
`c_O [H_free, H_int] = c_O * Dw(k) * g * (rotated component)`, tilts the direction by
`~ c_O * Dw(k)` -- and `Dw(k) -> 0` is the **same UV degeneracy that builds the wall**. Verified:
region-dependent `c_O in {+0.8, -0.5}` rotate the direction at low `k` (`3.6e-4` rad at `k = 1e2`) but
the deviation falls `~ 1/k` to `3.6e-7` at `k = 1e5`, and the two regions' tail classes **still cohere**
(compact difference, same null line). So **U5 need only hold asymptotically, and asymptotically it is
self-enforced against every bounded commutator-type correction** -- only an UV-non-vanishing second
grading-odd structure (R1) can rotate the tail.

---

## 3. What this does to the Observer Structure Theorem

- **Clause 2 STRENGTHENS: pairwise -> presheaf with a global section.** The interface classes on
  overlaps satisfy the triple-overlap cocycle exactly, survive radical weight profiles, and **glue to a
  global class** (weight-independent `2[P]` + null line + global potential `F = -log w`) -- while no
  global operator exists at any level. The theorem's sharpest available form -- *the observers share
  one global interface class but no God's-eye operator* -- is now computed, not conjectured.
- **U5 MOVES COLUMNS: from ASSUMED (open fork) to DERIVED-conditional.** In the `W109` assumption table,
  U5's grade line should read: *derived from interaction-universality + single real grading-odd vertex
  (W102 skeleton, exact Krein-self-adjointness) + positive-real modular weights; UV-self-protected
  against bounded non-scalar modular corrections; residual fork NAMED = (R1) a second independently-
  running grading-odd vertex / (R2) a running CP phase, both absent at skeleton grade.* The assumption
  does not vanish outright at continuum grade -- the single-vertex/reality input is skeleton-verified,
  not continuum-proven, and the interacting double-cone modular Hamiltonian remains unsolved -- but the
  fork is now a **specific physics question about field content**, not a free structural assumption.
- **The dependency structure is now honest in both directions:** T1 showed the cocycle is U5-loaded;
  T2 showed U5 is derivable from named inputs. Net: clause 2's whole coherence story (pairwise + triple
  + global section) rests on *interaction-universality plus the skeleton's single real vertex* -- a far
  better foundation than "assumed."
- Nothing else moves: clauses 1 and 3, the `W98` break, the `W100` IFF, the `W94` retraction, `W103`,
  `W107`, `W109` all stand unchanged.

## 4. Honest residuals (named, not hidden)

1. **The cocycle's non-independence.** Within the model class, triple-failure is reachable only through
   pairwise-failure (U5 violation). A model where pairwise coherence holds but the triple cocycle fails
   was not found -- and in the 2x2 doublet surrogate it plausibly cannot exist (pairwise class agreement
   forces the same null line, making the aligners trivial). Whether a higher-dimensional carrier admits
   "pairwise-coherent but holonomy-obstructed" configurations is open; the holonomy computation shows
   exactly what such an obstruction would look like (a gerbe-type defect on the tail's phase data).
2. **The skeleton-grade condition on T2.** The single-vertex and reality inputs are W102 skeleton facts
   (reconstruction-tier). The finished source action could in principle generate (R1) or (R2) at loop
   level; T9 shows any such rotator must be UV-non-vanishing to matter -- a sharp target, not a vague worry.
3. **The scalar-weight surrogate.** The genuinely interacting double-cone modular Hamiltonian is
   unsolved (Casini-Huerta); T9 covers bounded commutator-type corrections only. An UV-non-vanishing
   grading-odd modular component would evade both the derivation and the coherence -- it is the same
   named object as (R1) seen from the state side.
4. **Doublet-surrogate extrapolation** to the genuine III_1 region algebra: unchanged from W107
   (LOW-MEDIUM), inherited here.

## 5. Verdicts and confidence

**T1 VERDICT: COCYCLE-HOLDS + GLOBAL-SECTION-EXISTS.** Exact at every layer, radical-weight-robust,
with the failure mode computed (nonzero non-coplanar holonomy) and the U5-loading named. Confidence:
**HIGH in-model** (exact + machine-verified); **MEDIUM** as a statement about GU regions (inherits U5's
grade -- which T2 improves).

**T2 VERDICT: U5-DERIVED (model + skeleton grade, conditional on named inputs).** The direction is a
computed function of the vertex tensor structure alone; weights, running, and rescalings are proven
inert; bounded non-scalar corrections are UV-suppressed; the residual fork is two named physics
questions (second running grading-odd vertex; running CP phase), both absent in the W102 skeleton.
Confidence: **HIGH** for the model-level chain (exact); **MEDIUM-HIGH** for the skeleton-conditional
physics reading; the continuum residual is named, not graded away.

## 6. What this does NOT do

No GU claim-status, `CANON.md`, `RESEARCH-STATUS.md`, verdict, or public-posture change; no external
action; literature read-only. H61/H61a remain **OPEN**; the `W98` break, the `W100` IFF, the `W109`
theorem's stated grade all stand. This branch **presents, does not decide** -- it hands the
orchestrator: the triple-overlap cocycle result with its three layers and the trivial layer named, the
radical-weight robustness, the global-class-exists / global-operator-does-not contrast, the holonomy
failure mode and the honest U5-loading, the U5-derivation chain with each link computed, the two named
rotators with the RG adversary made concrete, the UV self-protection result, and the proposed U5 grade
line for the `W109` assumption table. Reproducible: `tests/W110_triple_overlap_u5.py` (10/10, exit 0).
