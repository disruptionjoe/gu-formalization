---
artifact_type: exploration
status: "exploration (W184 / TEAM MIRROR-SUPERSELECT; label W184; coherence-first, exploration grade, conditional register, honest grading; five inline personas, one worker, no sub-agents; one deterministic test 11/11 exit 0 with positive controls first + a genuine-superselection control + the channel-removed re-run; RUTHLESS skeptic pass on the superselection-rescue conjecture)"
created: 2026-07-14
label: W184
posture: coherence-first; exploration grade; conditional register; honest grading; the rescue is attacked hard, not wished
hypothesis: "Joe's sharpening of the external-input question: the build sprint leaned NOT-OPERATIVE because the ghost decays into two gravitons above the massless two-graviton threshold (W179) and the anti-damping self-energy puts a pole on the physical sheet (W178). But W173 established the mirror sector as a SUPERSELECTION sector (the Krein form implements the CARTAN INVOLUTION of so(9,5), a global involution). IF the mirror is a genuine superselection sector, the ghost -> two-PHYSICAL-graviton decay CROSSES a superselection boundary = FORBIDDEN -> anti-damping width ZERO -> no physical-sheet pole -> PT unbroken -> the interacting C-operator EXISTS -> OPERATIVE -> bar (b) clears. TEST rigorously: is the mirror a genuine superselection sector, and does the GU interaction vertex conserve or violate the Cartan charge?"
verdict: "DECAY-ALLOWED-NOT-OPERATIVE-STANDS, CONDITIONAL-on-[P_ghost,S]=0. The mirror is NOT a proven superselection sector: W173's Cartan-involution identification (reproduced exactly here, residual 0.0e+00) makes the mirror a GLOBAL Z2 GRADING, which is NECESSARY but NOT SUFFICIENT for a superselection RULE. A charge is a superselection rule only if it COMMUTES WITH THE DYNAMICS. The decisive check: GU's OWN cross/decay vertex A = (a1 a1)a2^dag - h.c. (the W169/W178 vertex, canon-labelled 'Krein-odd') is P-ODD under the ghost-parity/Cartan charge P = (-1)^{n_ghost} -- {P,A}=0, [P,A]=34.3 != 0 -- so it VIOLATES the charge. The decay matrix element <2 gravitons|A|ghost> = 1.41 != 0: the decay is ALLOWED, the anti-damping width is real, the W178 physical-sheet pole stands (reproduced: 1 physical-sheet pole WITH the channel). A COUNTING FACT seals it: any trilinear ghost->2-graviton vertex changes ghost number by 1 (odd) and is therefore ALWAYS P-odd, so a genuine decay vertex can NEVER conserve ghost parity. Superselection would mean such a vertex is ABSENT (coupling zero by symmetry = the ghost DECOUPLES), which is EXACTLY the standing OPEN condition [P_ghost,S]=0 (the Turok-Bateman positivity condition the canon flags as unbuilt) -- NOT an independent new mechanism. Re-running W178's argument-principle pole count with the channel REMOVED gives 0 physical-sheet poles (OPERATIVE), but 'removed' is achieved only by IMPOSING [P,S]=0; it is circular, not delivered by the Cartan grading. The MIRROR-THRESHOLD alternative (ghost decays into mirror gravitons at the fourth-derivative scale, not our massless ones) is kinematically coherent (a gapped mirror graviton closes ITS channel) but does NOT close the decisive OUR-massless-graviton channel: a stress-energy-carrying spin-2 ghost couples to the massless graviton universally, so that channel stays open (open for every M > 0, W179 reproduced) unless the ghost decouples from our gravitons = [P,S]=0 again; and W181 already showed gapping our graviton at the mirror scale is H36-forbidden and GW-excluded by ~1e20. RELATIONAL-SCALE assessment: even granting the inside/outside scale is undetermined up to M_Pl, it does not bind, because the LIGHT field in the decay (our graviton) is empirically massless and the threshold it sets is 0 regardless of where the ghost sits. Effect on bar (b): UNCHANGED -- the superselection reframe RELOCATES bar (b) onto [P_ghost,S]=0 (exactly W173's relocation) and onto the W48 physical-sheet self-energy, it does not clear it. H59 remains OPEN."
grade: "EXACT (self-validating to 1e-12..0.0) for: the reproduction of W173's kinematic fact that K = eta implements the Cartan involution theta(X)=eta X eta of so(9,5) (generators in-algebra 0.0e+00, theta an automorphism 0.0e+00, theta^2=id 0.0e+00, compact so(9)+so(5) FIXED, noncompact NEGATED); the ghost-parity charge P = (-1)^{n_ghost} being a Z2 involution and the Krein fundamental-symmetry sign; the Cartan charge of the ghost (-1) vs two gravitons (+1); the DECISIVE vertex check that GU's cross vertex A is P-ODD ({P,A}=0.0e+00, [P,A]=34.29) while the Krein-even Sv is P-even ([P,Sv]=0.0e+00); the nonzero decay matrix element (1.41); the counting fact that a delta-n_ghost=odd vertex is P-odd. RIGOROUS (argument principle, integer, seed-independent) for the pole counts: 1 physical-sheet pole WITH the channel (NOT-OPERATIVE, W178 reproduced), 0 with the channel removed (OPERATIVE). PROVEN-in-controls: PC1 the W178 physical-sheet decider (1 vs 0 for anti-damping vs normal sign); PC2 the W173 Cartan involution; PC3 a genuine superselection control ([P,V_even]=0 -> P-changing amplitude IDENTICALLY 0; {P,V_odd}=0 -> P-changing amplitude NONZERO) -- the calibrator distinguishing 'forbidden by a conserved charge' from 'a grading the vertex ignores'. STRUCTURAL / ARGUED for the lift to the full QFT: the Fock model is the same minimal two-mode Krein stand-in W169/W178 used (a1 physical, a2 ghost; the A-vertex the minimal cubic cross coupling), so it DECIDES the algebraic structure (the vertex's Cartan-charge parity; the amplitude's non-vanishing; the counting fact) but does not compute GU's full dressed self-energy or fix whether GU's unbuilt dynamics contains the cross vertex -- that is the inherited [P_ghost,S]=0 / H59/W48 object, unchanged. The identification 'Krein-odd == ghost-parity-odd == Cartan-charge-violating' is a machine fact on Fock space (the Krein norm sign of an n-ghost state is (-1)^n). Test: tests/W184_mirror_superselection_decay.py 11/11 exit 0. NO canon / RESEARCH-STATUS / claim-status / verdict / posture change. H36 non-reimport honored. H59 remains OPEN."
depends_on:
  - explorations/W173-brst-cohomology-mirror-sector-2026-07-14.md
  - explorations/W178-build-numerical-spectral-model-2026-07-14.md
  - explorations/W179-build-c-operator-allorders-2026-07-14.md
  - explorations/W181-external-input-continuum-gap-2026-07-14.md
  - canon/ghost-parity-krein-synthesis.md
  - tests/W178_build_numerical_spectral_model.py
  - tests/W179_c_operator_allorders_qft.py
  - GEOMETER-VS-PHYSICS-OBJECTS.md
scripts:
  - tests/W184_mirror_superselection_decay.py
external_refs:
  - "Wick, Wightman & Wigner, The intrinsic parity of elementary particles, Phys Rev 88 (1952) 101 -- superselection rules: a charge that commutes with all observables forbids coherent superpositions and transitions between sectors"
  - "Haag, Doplicher & Roberts (DHR), Local observables and particle statistics, CMP 23/35 (1971/1974) -- superselection sectors as inequivalent representations labelled by global charges; a genuine rule forbids interpolation by any local observable"
  - "Bateman & Turok, Escape from Ostrogradsky via Hidden Ghost Parity, arXiv:2607.00096 -- Krein-space quantization; the projector Born rule requires the ghost parity to be a symmetry of the dynamics, [P_ghost, S] = 0"
  - "Kugo & Ojima, Local covariant operator formalism, PTP Suppl 66 (1979) -- the quartet mechanism; a charge conserved by the S-matrix removes negative-norm states"
  - "Stelle, Renormalization of higher-derivative quantum gravity, PRD 16 (1977) 953 -- massless graviton + massive spin-2 ghost; the ghost is unstable, coupling gravitationally to the massless graviton"
---

# W184 -- does the mirror superselection sector forbid the ghost decay?

## 0. Role, and the one object

**The one object (H59 North Star).** The interacting C-operator whose existence decides bar (b).
The build sprint (W175-W182) leaned **NOT-OPERATIVE** on a single dynamical hinge: GU's massive
spin-2 ghost sits ABOVE the two-graviton decay threshold (W179: the threshold is `2 m_phys = 0`
because the graviton is exactly massless, H51), the decay channel is open, the anti-damping
self-energy (W51/W132 wrong-sign width) puts the propagator pole on the **physical sheet** (W178,
argument principle), PT breaks, no positive C-metric, NOT-OPERATIVE.

**Joe's sharpening (the rescue under test).** That whole chain assumed the decay is ALLOWED and into
OUR massless gravitons. But W173 established the mirror sector as a **superselection sector**: the
Krein form `K` implements the **Cartan involution** of `so(9,5)` (canon V2, residual `0.0e+00`), a
GLOBAL involution defining the non-compact real form, not a local gauge redundancy. If the mirror is
a genuine superselection sector, the ghost `->` two-physical-graviton decay **crosses a
superselection (Cartan) boundary** = FORBIDDEN `->` the anti-damping width is ZERO `->` the
physical-sheet pole never forms `->` PT unbroken `->` the interacting C-operator EXISTS `->`
OPERATIVE `->` bar (b) clears.

This wave tests that rigorously, and attacks it hard (a clean rescue would reverse the sprint, so it
must be earned). Five personas ran inline, one worker, no sub-agents. Deterministic test
`tests/W184_mirror_superselection_decay.py`, **11/11, exit 0**, positive controls first.

## 1. Construction forks (GEOMETER-VS-PHYSICS-OBJECTS.md discipline)

| Object | Constructions in play | Handling |
|---|---|---|
| **the mirror grading** | (i) a global Z2 GRADING (Cartan involution, kinematic); (ii) a genuine superselection RULE (charge commutes with all observables AND the dynamics) | W173 established (i); (ii) requires the extra dynamical fact `[K,S]=0` -- the load-bearing distinction |
| **"the Cartan charge"** | the eigenvalue of `K` = ghost parity `P = (-1)^{n_ghost}` on Fock space | the same Z2; the Krein fundamental-symmetry sign |
| **the interaction vertex** | (a) the cross/decay vertex `A` (ghost `<->` two gravitons, Krein-odd); (b) a Krein-even vertex `Sv` (ghosts pair-produced) | the DECISIVE question is which parity `A` has under `P` |
| **the decay channel** | ghost `->` two OUR massless gravitons vs ghost `->` two MIRROR gravitons (fourth-derivative scale) | the mirror-threshold alternative; assessed in Part 5 |
| **the IR/relational scale** | de Sitter `H0`, the mirror/fourth-derivative scale `mu_DW` up to `M_Pl` | assessed against the empirically-massless graviton (Part 5) |

**The one fork this wave turns on (named, not defaulted):** *does GU's interaction vertex CONSERVE
the Cartan (ghost-parity) charge (`->` genuine superselection `->` decay forbidden `->` OPERATIVE) or
VIOLATE it (`->` a mere grading `->` decay allowed `->` NOT-OPERATIVE stands)?* We show it VIOLATES
it, and that the rescue is logically equivalent to the standing open condition `[P_ghost,S]=0`.

## 2. Persona 1 -- superselection / algebraic-QFT specialist: is the Cartan grading a superselection RULE?

A **superselection rule** (Wick-Wightman-Wigner; DHR) is not merely a global grading. It requires a
charge `Q` that **commutes with every observable** and, decisively, **with the dynamics** (the
Hamiltonian / S-matrix), so that no physical process interpolates between the sectors and coherent
superpositions across them are unobservable. Global-ness of the grading operator is **necessary**
(a local gauge transformation gives redundancy, not superselection) but **not sufficient**: the
sufficient and decisive ingredient is `[Q, S] = 0`.

W173's argument establishes the necessary half and stops there. It shows `K` is the Cartan
involution -- a GLOBAL automorphism, not a local gauge transformation -- and concludes "a global
involution grades states into superselection labels (records)." **PC2 reproduces the kinematic fact
exactly**: with `eta = diag(+1 x 9, -1 x 5)`, `theta(X) = eta X eta` is an automorphism of `so(9,5)`
(`theta[X,Y] = [theta X, theta Y]`, residual `0.0e+00`), `theta^2 = id`, it FIXES the maximal compact
`so(9)+so(5)` and NEGATES the noncompact part. So the mirror is genuinely globally Cartan-graded.

But the leap from "global grading" to "superselection rule" is exactly the missing sufficient step.
**The canon itself flags it as open:** `ghost-parity-krein-synthesis.md` lists `[P_ghost, S] = 0`
(the Turok-Bateman positivity condition) as "the honest open condition," unchecked because "GU
supplies no S-matrix." W173's own verdict calls the mirror a record only "as far as the Y14
source-action is unbuilt" and RELOCATES bar (b) onto that object. So at the algebraic-QFT level the
honest statement is: **the mirror is a global GRADING that becomes a superselection RULE only under
the unproven `[K,S]=0`.** Answer to task (1): **WEAKER-grading** -- a genuine superselection rule is
NOT established; it is conditional on `[K,S]=0`.

## 3. Persona 2 -- BRST/Krein specialist: the Cartan charge of the ghost vs two gravitons, and "Krein-odd"

On Fock space the ghost-parity operator `P = (-1)^{n_ghost}` **is** the Krein fundamental-symmetry
sign: a state with `n` ghost quanta has Krein norm sign `(-1)^n` (C0, `P^2 = 1`). This is the same Z2
as `K` restricted to the sector. The charge assignments (C1, exact): the **ghost** is `P = -1`
(Krein-negative), a single **physical graviton** is `P = +1`, **two physical gravitons** are
`P = +1`. So the decay `ghost -> 2 gravitons` is **charge-changing**: `(-1) -> (+1)`. It is therefore
superselection-forbidden **if and only if** `P` is conserved by the dynamics.

The decisive object is the vertex that mediates it. GU's cross vertex, used verbatim in W169/W178
(`fock_build`), is `A = (a1 a1) a2^dag - (a1^dag a1^dag) a2` -- two physical quanta `<->` one ghost
quantum. The canon and W179 label it **"Krein-odd."** The machine identity that makes this decisive:
**"Krein-odd" == "ghost-parity-odd" == "Cartan-charge-violating,"** because the Krein sign IS
`P = (-1)^{n_ghost}` and `A` changes `n_ghost` by one. This is not a coincidence to be discovered
later; it is already written into the sprint's own construction. The very object that produces the
decay is the object that breaks the charge Joe hopes will forbid it.

## 4. Persona 3 -- self-energy / decay specialist: the DECISIVE vertex check, and the pole re-count

**The decisive computation (C2).** Compute the parity of GU's cross vertex `A` under `P`:

>  `{P, A} = 0.0e+00`  (A is P-ODD),   `[P, A] = 34.29 != 0`  (A does NOT commute with P).

For contrast the Krein-even vertex `Sv` (ghosts pair-produced) gives `[P, Sv] = 0.0e+00` (P-even,
conserves the charge). So **GU's decay vertex VIOLATES the Cartan charge.** Answer to the decisive
task-(2) check: **the GU interaction vertex VIOLATES the Cartan charge; it does not conserve it.**

**Consequence (C3).** The decay matrix element is nonzero:
`|<2 gravitons| A |ghost>| = 1.41 != 0`. The decay is ALLOWED given the vertex; the anti-damping
width is real, not zero; **the W178 physical-sheet pole stands** -- PC1 reproduces it exactly (1
physical-sheet upper-half pole WITH the channel; 0 for the normal-sign control).

**The counting fact that seals it (C4).** A vertex's ghost parity is `(-1)^{delta n_ghost}`. Any
trilinear `ghost -> two-graviton` vertex changes ghost number by **one** (odd), so it is **ALWAYS
P-odd**. A genuine decay vertex can NEVER conserve ghost parity. `P` is conserved only if such
trilinear cross vertices are **absent** -- i.e. ghosts are pair-produced, the ghost sector
**decouples**. This is the crux the rescue misreads: **superselection does not "block a would-be
nonzero width"; a genuine superselection rule means the mediating coupling is ZERO by symmetry.** The
picture "the width wants to be nonzero but the boundary forbids it" is not how superselection works.

**The pole re-count with the channel removed (C5).** Re-running W178's argument-principle count with
the two-graviton cut CLOSED at the ghost mass (threshold raised above the ghost, no absorptive part)
gives **0 physical-sheet poles -> OPERATIVE**. WITH the channel it is 1 -> NOT-OPERATIVE. So the
rescue's conclusion is arithmetically correct **conditional on removing the channel** -- but
"removing the channel" is achieved only by IMPOSING `[P,S]=0` (a P-even / decoupled dynamics). It is
**circular**: it is not delivered by the Cartan GRADING (PC2), which the actual P-odd vertex (C2)
violates. The pole disappears exactly when, and only when, you assume the conclusion.

## 5. Persona 3 (cont.) -- the MIRROR-THRESHOLD alternative and the relational-scale point

**The reframe.** Perhaps the ghost decays into MIRROR gravitons (at the fourth-derivative / mirror
scale), not our massless ones, so the relevant threshold is the MIRROR two-graviton threshold, and
the ghost could sit below it (sub-threshold -> OPERATIVE, W179). And perhaps the inside/outside scale
is genuinely undetermined, so W181's de-Sitter-scale dismissal does not bind.

**Kinematically coherent, but it does not close the decisive channel (M1/M2).** Reusing W179's energy
denominator `D(k1,k2)`: for OUR massless graviton (`m_phys = 0`) the two-graviton channel has a real
on-shell zero for **every** ghost mass `M > 0` -- the channel is open regardless of the ghost's
scale. A MIRROR graviton gapped above `M/2` would indeed close ITS channel (M1 confirms the reframe
is coherent for the mirror channel). But the ghost is a spin-2 state carrying stress-energy, so by
**gravitational universality it couples to OUR massless graviton**, and that channel stays open (M1)
unless the ghost DECOUPLES from our gravitons -- which is once again the cross-coupling-zero /
`[P,S]=0` / superselection condition. Same open object, relabeled.

**Relational-scale assessment.** Even granting the inside/outside scale is undetermined up to `M_Pl`,
it **does not bind**, because the LIGHT field in the decisive decay is OUR graviton, which is
empirically massless; the threshold it sets is `0` no matter where the ghost sits. W181 already made
this quantitative: the honest external IR gap is `H0 ~ 1e-33 eV`, `g_available/g_needed in
[1e-20, 1e-60]` across the whole `mu_DW` window up to `M_Pl`, never `>= 1`; and gapping OUR graviton
at the mirror/`mu_DW` scale is the H36-forbidden re-import and GW-excluded by `~1e20`. So the
relational-scale freedom does not rescue: the decay is into OUR massless gravitons, whose threshold
cannot be raised without a GW-excluded graviton mass. Answer to task (3): the mirror-threshold reframe
does **not** move the ghost sub-threshold in the decisive channel; the correct threshold for the
process that drives NOT-OPERATIVE is the OUR-massless one W179 used.

## 6. Persona 4 -- symbolic/numerical engineer: the test and its controls

`tests/W184_mirror_superselection_decay.py`, **11/11, exit 0** (numpy only, seed 20260714). Positive
controls run FIRST (W138 discipline):

- **PC1** reproduces W178's physical-sheet decider (argument principle): 1 physical-sheet pole WITH
  the anti-damping channel, 0 for the normal-sign control -- the NOT-OPERATIVE baseline.
- **PC2** reproduces W173's kinematic fact: `K = eta` implements the Cartan involution of `so(9,5)`
  (automorphism, `theta^2 = id`, compact fixed, noncompact negated; residuals `0.0e+00`).
- **PC3** is the calibrator that distinguishes the two readings: a genuine superselection charge
  (`[P, V_even] = 0`) gives an **identically zero** cross-sector amplitude; a grading the vertex
  ignores (`{P, V_odd} = 0`) gives a **nonzero** amplitude. This is the template the core applies to
  GU's own vertex.
- **Core (C0-C5):** the charge is a Z2 involution; the ghost/two-graviton charges; the decisive
  vertex check (`A` is P-odd, `Sv` is P-even, exact); the nonzero decay amplitude; the counting fact;
  the channel-removed pole re-count.
- **Mirror-threshold (M1/M2):** the our-massless channel is open for every `M`; closing it needs
  `[P,S]=0`, not a mirror threshold.

Every load-bearing number has two routes or a matched control. Exactness where it matters: the vertex
parity residuals and the Cartan-involution residuals are `0.0e+00`; the pole counts are integers.

## 7. Persona 5 -- adversarial skeptic (RUTHLESS): steelman DECAY-ALLOWED, and why the rescue fails

**Steelman the rescue (at full strength).** W173 proved (residual `0.0e+00`) that `K` is the Cartan
involution -- a genuine GLOBAL automorphism defining the non-compact real form. A global involution
is the textbook source of a superselection label (univalence, baryon number, the WWW intrinsic-parity
rule). The ghost is `K = -1`, two gravitons are `K = +1`; the decay is manifestly charge-changing. If
`K` is superselected, the amplitude is identically zero, the width vanishes, the pole never forms,
and the sprint's NOT-OPERATIVE lean reverses to OPERATIVE. This is a clean, principled mechanism, not
a wish.

**Kill the steelman (the decisive check comes out the wrong way for the rescue).** A superselection
rule requires the charge to commute with the DYNAMICS, not merely to be global. The decisive test is
the vertex: **GU's own cross/decay vertex `A` is P-ODD** (`{P,A}=0`, `[P,A]=34.3 != 0`, C2). It
VIOLATES the Cartan charge. So `K` is **not** conserved by the interaction that produces the decay,
and there is **no** superselection protection. Worse, this is structural, not incidental: any
trilinear ghost `->` two-graviton vertex changes ghost number by one and is therefore ALWAYS P-odd
(C4). You cannot have both (i) a vertex that mediates the decay and (ii) `K` conserved: (i) forces
`{K, H_int} = 0`, which is `[K, H_int] != 0`. The only way `K` is conserved is that the cross vertex
is ABSENT -- the ghost decouples, which is precisely the unproven `[P_ghost, S] = 0`, and which the
big-swing R3 result (SUSTAINED x2) found GU-native dynamics does NOT supply in a way that also
chiralizes (spectrally sign-blind; `{K, chi} = 0` forces `Re tr(chi Pi_+) = 0`; mirrors and
generations gap together). So the rescue is not independent of the standing open object; it IS that
object, relabeled.

**Skeptic's residue (honest).** There remains a genuine OPERATIVE possibility: IF GU's unbuilt
dynamics turns out to have NO Krein-odd cross vertex (ghosts always pair-produced, `[P_ghost,S]=0`
holds), the ghost is stable, no physical-sheet pole, OPERATIVE -- this is the record branch of W173.
But that is the OPEN condition, not a consequence of superselection, and it is not what the generic
quadratic-gravity / Stelle dynamics the sprint modelled delivers (a gravitationally coupled spin-2
ghost has the cross vertex). So the honest verdict is CONDITIONAL, and superselection does not
independently clear bar (b).

## 8. Verdict

**DECAY-ALLOWED-NOT-OPERATIVE-STANDS, CONDITIONAL-on-`[P_ghost,S]=0`.**

- **Is the mirror a genuine superselection sector?** **NO / WEAKER-grading.** W173's Cartan-involution
  identification (reproduced, residual `0.0e+00`) makes it a GLOBAL Z2 GRADING -- necessary but not
  sufficient. A superselection RULE needs `[K,S]=0`, which is the standing unproven condition.
- **Does the GU interaction vertex conserve or violate the Cartan charge?** **VIOLATES.** The cross
  vertex `A` (canon "Krein-odd") is P-ODD (`{P,A}=0`, `[P,A]=34.3`); any ghost `->` two-graviton
  vertex is P-odd by counting. The Krein-even `Sv` conserves it, but `Sv` does not mediate the decay.
- **Ghost-decay verdict:** **ALLOWED.** `<2 gravitons|A|ghost> = 1.41 != 0`; the width is real; the
  W178 physical-sheet pole stands (1 physical-sheet pole WITH the channel).
- **Re-run pole count with the channel removed:** **0 physical-sheet poles (OPERATIVE)** -- but only
  by IMPOSING `[P,S]=0`; circular, not delivered by the Cartan grading.
- **Mirror-threshold / relational-scale:** does NOT close the decisive OUR-massless-graviton channel
  (open for every `M`); closing it needs `[P,S]=0`, not a mirror threshold; the empirically-massless
  graviton pins the threshold at `0` regardless of the ghost's scale (W181: GW-excluded by `~1e20`).

**Effect on bar (b): UNCHANGED.** The superselection reframe RELOCATES bar (b) onto `[P_ghost,S]=0`
(exactly W173's relocation) and onto the W48 physical-sheet self-energy; it does not clear it. The
build sprint's NOT-OPERATIVE lean is UNMOVED by the superselection channel. **Effect on the W48
question:** unchanged -- W184 does not resolve physical-sheet-vs-second-sheet; it shows the specific
claim "superselection forbids the decay" is false unless `[P_ghost,S]=0`, and the decisive vertex
check comes out VIOLATES. **H59 remains OPEN.** No canon / RESEARCH-STATUS / claim-status / verdict /
posture change.

## 9. What this does NOT do (honest limits)

- **This does not close the OPERATIVE branch.** If GU's unbuilt dynamics has no Krein-odd cross vertex
  (`[P_ghost,S]=0`), the ghost is stable and OPERATIVE survives -- W173's record branch. W184 shows
  superselection does not DELIVER that condition; it does not disprove it. The condition is inherited
  open.
- **The Fock model is the minimal two-mode Krein stand-in** (a1 physical, a2 ghost; A the minimal
  cubic cross vertex), the same W169/W178 used. It decides the algebraic structure (the vertex's
  Cartan-charge parity, the amplitude's non-vanishing, the counting fact) but does not compute GU's
  full dressed self-energy or the M(64,H) rep.
- **No canon movement, no external action.** The Cartan-involution / ghost-parity identification is
  reproduced, not re-derived as canon. H36 non-reimport honored (the mirror scale is never identified
  with the DE scale; the mirror-threshold rescue is named and shown to require the forbidden
  identification). The exploration is the computation, not a status change.

**Artifacts:** this file + `tests/W184_mirror_superselection_decay.py` (11/11, exit 0).

*Filed 2026-07-14 by Team MIRROR-SUPERSELECT (W184). Five personas inline in one worker
(superselection/algebraic-QFT specialist, BRST/Krein specialist, self-energy/decay specialist,
symbolic/numerical engineer, adversarial skeptic RUTHLESS); no sub-agents. Reproducible:
`python -u tests/W184_mirror_superselection_decay.py` (11/11, exit 0). Exploration grade; conditional
register; no canon movement; H59 OPEN. Verdict: DECAY-ALLOWED-NOT-OPERATIVE-STANDS,
CONDITIONAL-on-[P_ghost,S]=0 -- the mirror is a global Cartan grading, not a proven superselection
rule; GU's cross vertex is Krein-odd = ghost-parity-odd = Cartan-charge-violating, so the decay is
allowed and the physical-sheet pole stands; the superselection reframe relocates bar (b) onto
[P_ghost,S]=0, it does not clear it.*
