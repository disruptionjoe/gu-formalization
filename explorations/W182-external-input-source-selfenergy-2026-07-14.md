---
artifact_type: exploration
status: "exploration (W182 / TEAM EXT-SELFENERGY, label W182; coherence-first, exploration grade; five personas inline, one worker, no sub-agents; one deterministic test 11/11 exit 0 with positive controls first + matched negative control)"
created: 2026-07-14
wave: W182
label: W182
posture: coherence-first; exploration grade; honest grading; no manufactured rescue
hypothesis: "The build sprint (W178/W179/W172) computed the ghost pole sheet for the CLOSED theory: the internal ghost self-energy Sigma_internal(s) carries the ANTI-DAMPING sign (W51 Im Sigma(M^2) > 0, W132 probability EXCESS), placing the resummed propagator pole on the PHYSICAL sheet (argument principle: exactly 1 upper-half physical-sheet pole) = spontaneously broken PT = no positive C-metric = NOT-OPERATIVE. But GU is OPEN: an external source (W177 count datum, W180 dark-energy current J, the W158 promotion-gate boundary term on the q=5 frontier) inputs to the source action from OUTSIDE the geometry. Does the external source's contribution Sigma_ext(s) to the ghost propagator D(s) = 1/(s - M^2 - Sigma_internal(s) - Sigma_ext(s)) carry a sign/analytic structure that MOVES the pole off the physical sheet (-> second sheet -> PT unbroken -> OPERATIVE), or reinforce/be negligible (NOT-OPERATIVE stands)?"
verdict: "CONDITIONAL. SOURCE-TERM-DOES-NOT-MOVE-IT at the BUILT (ultralocal) order -- W178's NOT-OPERATIVE lean STANDS; BUT the OPEN-system source supplies a concrete, sign-plausible mechanism by which the NONLOCAL completion CAN move the pole to the second sheet (OPERATIVE), narrowing (not overturning) the inherited H59/W48 object. TWO honestly-separated legs. LEG 1 (built): the W180 promotion-gate source is S_D = Re<Psi, K_S c(A) Psi>, EXACTLY LINEAR in the connection (W180: S_D = A.J); in the induced/Sakharov stance its leading kernel is ALGEBRAIC (theta_induced = kappa M^{-1} J, s-independent, REAL), so its contribution to the ghost self-energy is a REAL CONSTANT Sigma_ext = c_ext: it SHIFTS M^2 -> M^2 + c_ext and adds NO imaginary part -- so at the order W180 actually built the source does NOT move the pole off the sheet (physical-sheet UHP pole count stays 1; E1a). It can only relocate the pole ALONG the real axis, and remove the physical-sheet pole solely by a LARGE (|c_ext| >= M^2 - s_th ~ 0.9), magnitude-gated real shift that pushes the ghost below the two-graviton threshold and CLOSES the decay channel -- a Model-A-style gap-protected OPERATIVE route, not a sheet move (E1b). LEG 2 (the residue's dispersive part): the sheet-moving power lives in the NONLOCAL completion (the full induced-YM kernel D_A* F = W180's UNBUILT eta-from-gimmel-area residue, W151). Modelled as a threshold self-energy, an OPPOSING-sign (normal-damping) external source moves the pole OFF the physical sheet (OPERATIVE) above a critical coupling ratio r* = sqrt(M^2 - s_th)/sqrt(M^2 - s_ext_th) ~ O(1) (E2: physical-sheet UHP pole count flips 1 -> 0 exactly at r*, located to r*=1.000 for equal thresholds and r*=1.500 for s_ext_th=0.60, matching the on-shell width-balance prediction to <0.02/<0.05). The OPPOSING sign is sign-plausible, not manufactured: the promotion gate PROMOTES records from the unconfirmable/ghost (q=5) sector INTO the confirmed C-positive sector H_C+ (W150/W158), so from the ghost sector's viewpoint the boundary flux is a LOSS = an ABSORBING channel = NORMAL-damping (Im Sigma_ext(M^2+i0) < 0, PC3), OPPOSING the internal two-graviton anti-damping; the record channel is C-POSITIVE (W132/W137, positive-Krein-norm intermediate states, the opposite of the negative-norm two-ghost channel that made W132's excess), and it has a DIFFERENT final state (record promotion vs two gravitons), so it is plausibly INDEPENDENT (not the anti-damping leak double-counted). The SIGN decides: a REINFORCING (anti-damping) external source never moves the pole (E3, control), and the machinery does not manufacture poles (NC1). The open-channel/Feshbach regularization direction is real and demonstrated (PC2). So the source term converts W178's 'leans NOT-OPERATIVE' into 'CONDITIONAL on the sign and magnitude of the DISPERSIVE part of the promotion-gate boundary self-energy': the pole moves IFF that part is (i) genuinely dispersive (not the built real ultralocal term), (ii) OPPOSING sign (sign-plausible from the drain direction), (iii) of magnitude kappa_ext/kappa_int > r* ~ O(1) -- the magnitude being the SAME unbuilt eta-from-gimmel-area (W180/W151), not a new object. Effect on bar (b): UNCHANGED verdict; the open-system input NARROWS the inherited H59/W48 residue to the sharper sub-question 'is the dispersive part of the promotion-gate boundary self-energy normal-sign and of magnitude exceeding r* the internal anti-damping?'. H59 remains OPEN."
grade: "RIGOROUS (argument principle, integer, seed-independent) for the pole-sheet counts: PC1 reproduces W178's closed-theory result exactly (internal anti-damping = 1 physical-sheet UHP pole; normal = 0) at four couplings; E2 the physical-sheet UHP count flips 1 -> 0 at r*=1.000 (equal thresholds) with the two-route phase-space check r*=1.500 at s_ext_th=0.60 (both matching sqrt(M^2-s_th)/sqrt(M^2-s_ext_th) to <0.02/<0.05); E3 the reinforcing-sign control never removes the pole; NC1 the opposing source on a normal internal self-energy adds no physical-sheet pole. EXACT for the on-shell signs (PC3: Im Sigma_internal(M^2+i0) = +0.2846 > 0 anti-damping; Im Sigma_ext(opp) = -0.2846 < 0 normal-damping; reinforcing +0.2846). PROVEN-in-control for the open-channel regularization (PC2: a two-channel Feshbach effective Hamiltonian drives the resonance pole into the lower half-plane, Im -> -0.140, monotone in the coupling). STRUCTURAL / MODEL for the lift to GU: Sigma_ext is a sqrt-threshold MODEL self-energy (the same KIND W124/W178 used, not GU's dressed one); the ultralocal-vs-nonlocal split is the W180 built-vs-residue split; the OPPOSING sign is an ARGUED (drain-direction + C-positivity) plausibility, not a derived dressed width; the magnitude r* is the on-shell width balance, and GU's actual kappa_ext/kappa_int is the inherited unbuilt eta-from-gimmel-area (W180/W151). Near threshold the argument-principle count is transitional (pole near the branch point) -- displayed honestly, not asserted on. Test: tests/W182_external_source_selfenergy.py 11/11 exit 0, positive controls first (W178 reproduction; Feshbach open-channel; on-shell signs) + negative control (no spurious poles). NO canon / RESEARCH-STATUS / claim-status / verdict / posture change. H59 remains OPEN."
depends_on:
  - explorations/W178-build-numerical-spectral-model-2026-07-14.md
  - explorations/W179-build-c-operator-allorders-2026-07-14.md
  - explorations/W172-interacting-c-operator-nogo-2026-07-14.md
  - explorations/W180-build-matter-connection-bridge-c3-2026-07-14.md
  - explorations/W158-promotion-gate-boundary-term-C3-2026-07-14.md
  - explorations/W138-issuance-kill-battery-2026-07-14.md
  - tests/W178_build_numerical_spectral_model.py
  - tests/W180_matter_connection_bridge.py
  - GEOMETER-VS-PHYSICS-OBJECTS.md
scripts:
  - tests/W182_external_source_selfenergy.py
external_refs:
  - "Feshbach, Unified theory of nuclear reactions, Ann. Phys. 5 (1958) 357 / 19 (1962) 287 -- projection onto an open channel; the effective non-Hermitian Hamiltonian and second-sheet (decaying) poles"
  - "Peskin & Schroeder, An Introduction to QFT, ch. 7 -- resummed propagator, self-energy, resonance poles on the second Riemann sheet"
  - "Stelle, Renormalization of higher-derivative quantum gravity, PRD 16 (1977) 953 -- massless graviton + massive spin-2 ghost (the model spectrum)"
  - "Sakharov, Vacuum quantum fluctuations in curved space and the theory of gravitation, Dokl. Akad. Nauk SSSR 177 (1967) 70 -- induced gravity (the no-fundamental-kinetic-term stance = the ultralocal leading kernel)"
  - "Cutkosky, Landshoff, Olive & Polkinghorne, NPB 12 (1969) 281 -- cutting rules / discontinuities across the two-body cut (the sheet structure)"
---

# W182 -- does the external source input move the closed-theory NOT-OPERATIVE ghost pole?

## 0. Role, and the one object

**The one object (H59 North Star).** The interacting ghost propagator of the covariant record/RS
operator `D` on Y14, and the Riemann sheet of its pole -- physical sheet (complex energy, PT broken,
no positive C-metric, **NOT-OPERATIVE**) versus second sheet (benign resonance, PT unbroken,
**OPERATIVE**). W178 computed this for the **CLOSED** theory (internal ghost self-energy only) and
found, by a rigorous argument-principle count, that the **anti-damping** sign (W51 `Im Sigma > 0`,
W132 probability excess) places the pole on the **physical sheet** = NOT-OPERATIVE, leaning. W172
established this is the single live dynamical no-go; W179 lifted it to the QFT decay-threshold
kinematics; W124 supplied the model self-energy KIND.

**The W182 question (Joe).** GU is **OPEN**: an external source inputs to the source action from
outside the geometry -- W180's built `S_D = Re<Psi, K_S c(A) Psi>` (whose EL current `J` sources the
connection), the W158 promotion-gate boundary term on the `q=5` finality frontier. **Does the
external source contribution `Sigma_ext(s)` to the ghost propagator move the pole off the physical
sheet?** Reuse W178's pole-tracking and W180's `S_D`.

Five personas ran inline, sequentially, one worker, no sub-agents. Deterministic test
`tests/W182_external_source_selfenergy.py`, **11/11, exit 0**, positive controls first.

## 1. Construction forks (GEOMETER-VS-PHYSICS-OBJECTS.md discipline)

| Object | Constructions in play | Handling |
|---|---|---|
| **`Sigma_ext`** | (i) the BUILT ultralocal/Legendre kernel (W180: `theta = kappa M^{-1} J`, algebraic, REAL); (ii) the NONLOCAL completion (`D_A* F`, dispersive) = W180's unbuilt eta-residue | both named; (i) is what W180 built, (ii) carries the sheet-moving power |
| **the source's effect** | a REAL mass shift `M^2 -> M^2 + c_ext` vs a DISPERSIVE width `Im Sigma_ext != 0` | the fork the whole verdict turns on: only a dispersive part can move the sheet |
| **the sign of `Im Sigma_ext`** | OPPOSING (normal-damping, drains the ghost) vs REINFORCING (anti-damping) | argued from the promotion-flux direction + C-positivity; the SIGN decides |
| **the external channel** | independent of the two-graviton channel (different final state) vs the same anti-damping leak double-counted | argued INDEPENDENT (record promotion != two gravitons); the honest risk named |
| **"moves the pole"** | a genuine sheet crossing (E2) vs closing the decay channel by a real shift (E1b) | both are OPERATIVE routes; only the first is a sheet move, and it needs the dispersive opposing part |

**The one fork this turns on (named, not defaulted):** *does the external source contribute a
DISPERSIVE self-energy with the OPPOSING sign and sufficient magnitude, or only the BUILT REAL
ultralocal shift?* The built part does not move the pole; the residue's dispersive part can, under a
sign-plausible condition -- and the magnitude is the inherited unbuilt object.

## 2. Persona 3 (GU-source specialist, led) -- what W180 actually built, and its analytic structure

W180 built the matter->connection bridge in the induced/Sakharov stance: the connection distortion
`theta` has **no fundamental kinetic term**, so its EL equation makes it a functional of the record
field, `theta_induced = kappa M^{-1} J`, with `M` a fixed **algebraic** equivariant Krein kernel
(W180 took `M = Gram`, the ultralocal leading order). The source action `S_D = Re<Psi, K_S c(A) Psi>`
is **exactly linear** in the connection (W180: `S_D = A.J`, residual `4.3e-14`).

**Consequence for the ghost self-energy (the load-bearing structural fact).** An **algebraic,
`s`-independent** kernel `M^{-1}` contributes to the ghost self-energy a **REAL constant**
`Sigma_ext = c_ext` (a `kappa <J, M^{-1} J>`-type number): it has **no branch cut and no imaginary
part**. A real, dispersionless self-energy **shifts the mass** `M^2 -> M^2 + c_ext` and adds **no
width**. So at the order W180 actually built, `Sigma_ext` cannot supply an absorptive part, and an
absorptive part is what a sheet crossing requires. The **sheet-moving power lives entirely in the
NONLOCAL completion** (the full induced-YM kernel `D_A* F`, a Green's function), which is exactly
W180's **unbuilt eta-from-gimmel-area residue** (W151). This is the honest built-vs-residue split,
inherited unchanged.

## 3. Persona 2 (self-energy / dispersion specialist) -- E1: the built ultralocal source does not move it

Reusing W178's Model B propagator `D(s) = 1/(s - M^2 - Sigma_internal(s) - Sigma_ext(s))` with
`Sigma_internal = s_sign * kappa * sqrt(s_th - s)` (`s_sign = -1` anti-damping) and adding
`Sigma_ext = c_ext` (real, the built ultralocal term):

- **E1a.** For every shift that keeps `M^2_eff = M^2 + c_ext` comfortably above the two-graviton
  threshold `s_th = 0.10`, the physical-sheet upper-half pole count stays **`1`** (values `+0.30`,
  `0.0`, `-0.20`, `-0.50` all give count `1.00`). **The built ultralocal source does NOT move the
  pole off the physical sheet** -- it only relocates it along the real axis. NOT-OPERATIVE stands at
  this order.
- **E1b.** The physical-sheet count departs from `1` **only** once the real shift drives `M^2_eff`
  into the threshold region (`|c_ext| >= M^2 - s_th ~ 0.9`), i.e. a **large, magnitude-gated** shift
  that closes the decay channel -- a Model-A-style gap-protected OPERATIVE route, **not a sheet
  move**. A small real self-energy leaves the physical-sheet pole in place (it has no width). (Near
  threshold the argument-principle count is transitional, the pole sitting near the branch point;
  displayed honestly, not asserted on.)

**On-shell signs (PC3, exact).** Just above the two-body cut, `Im Sigma_internal(M^2+i0) = +0.2846
> 0` (anti-damping, W51); an OPPOSING external source has `Im Sigma_ext(M^2+i0) = -0.2846 < 0`
(normal-damping, it **subtracts** width); a reinforcing one `+0.2846`. So the question reduces to the
**sign and magnitude of the dispersive part** of `Sigma_ext`.

## 4. Persona 1 (open-quantum-system / Feshbach specialist) -- the source as an open channel; the sign

The source term is a **boundary FLUX** through the `q=5` finality frontier -- a genuine open-system
contribution. Persona 1's two questions:

**(a) Does the open channel regularize the pole?** *Yes, that direction is real (PC2).* A two-channel
Feshbach effective Hamiltonian -- an unstable state coupled to an **absorbing** open channel -- drives
the dressed resonance pole into the **lower half-plane** (`Im -> -0.140`, monotone in the coupling):
a decaying, second-sheet resonance. Integrating out an absorbing external continuum produces a
non-Hermitian `H_eff` whose poles are second-sheet. So an external channel of the **right (absorbing)
sign** *does* move a pole to the second sheet.

**(b) Is GU's boundary flux absorbing (opposing) or emitting (reinforcing)?** *Argued OPPOSING, and
not manufactured.* The promotion gate **PROMOTES** records from the unconfirmable/ghost (`q=5`)
sector **INTO** the confirmed C-positive sector `H_C+` (W150/W158). From the **ghost sector's**
viewpoint that flux is a **LOSS** -- records leave to be promoted -- i.e. an **absorbing** channel =
**normal-damping** sign = **opposes** the internal two-graviton anti-damping. Two structural supports:
(1) the record channel is **C-POSITIVE** (W132/W137), so its intermediate states carry **positive**
Krein norm -- the opposite of the **negative-norm** two-ghost channel that produced W132's probability
**excess** (the anti-damping in the first place); (2) the external channel's **final state** (record
promotion) is **different** from the internal one (two gravitons), so the channels are plausibly
**independent** -- the opposing-sign is not the anti-damping leak double-counted. This is a genuine,
sign-plausible mechanism for `Sigma_ext` to **subtract** width.

## 5. Persona 4 (symbolic/numerical engineer) -- E2: the decisive computation, and the controls

`tests/W182_external_source_selfenergy.py`, **11/11, exit 0** (numpy only; seed 20260714).
Positive controls first: **PC1** reproduces W178's closed-theory result exactly (internal
anti-damping `= 1` physical-sheet pole at `kappa in {0.05,0.2,0.5,1.0}`; normal `= 0`); **PC2** the
Feshbach open-channel regularization; **PC3** the on-shell signs.

**E2 -- the decider (argument principle, integer).** Add the **nonlocal opposing-sign** external
source `Sigma_ext(s) = +kappa_ext sqrt(s_ext_th - s)` (the residue's dispersive part) and sweep the
ratio `r = kappa_ext / kappa_int`:

| `r = kappa_ext/kappa_int` | # phys-sheet UHP poles | verdict |
|---:|---:|---|
| 0.00 | +1.00 | NOT-OPERATIVE (physical-sheet pole) |
| 0.50 | +1.00 | NOT-OPERATIVE |
| 0.90 | +1.00 | NOT-OPERATIVE |
| 0.99 | +0.75 | transition |
| 1.01 | +0.24 | transition |
| 1.10 | -0.00 | **OPERATIVE (pole moved off the physical sheet)** |
| 1.50 | -0.00 | OPERATIVE |
| 2.00 | -0.00 | OPERATIVE |

**The physical-sheet pole count flips `1 -> 0` at a sharp critical ratio.** The external source
**moves the pole off the physical sheet** (to the second sheet) once its opposing on-shell width
exceeds the internal anti-damping width. The critical ratio is **located and matches the phase-space
prediction** `r* = sqrt(M^2 - s_th)/sqrt(M^2 - s_ext_th)`: `r*(numeric) = 1.000 = r*(predicted)` for
equal thresholds (E2c), and a **second route** at `s_ext_th = 0.60` gives `r*(numeric) = 1.500 =
r*(predicted)` (E2d) -- confirming the crossing is the on-shell **width balance**
`kappa_ext sqrt(M^2 - s_ext_th) = kappa_int sqrt(M^2 - s_th)`, not an artifact (W138 two-route
discipline).

**The sign decides (E3, control).** A **reinforcing** (anti-damping, `s_sign_ext = -1`) external
source **never** removes the physical-sheet pole (count stays `>= 1` for all `r`). So the E2 move is
due to the **opposing sign**, not merely to adding a channel. **NC1 (negative control):** the
opposing external source on a **normal** internal self-energy adds **no** spurious physical-sheet pole
(count stays `0`) -- the argument-principle machinery does not manufacture poles; E2 is a genuine
sheet move of the ghost pole.

## 6. Persona 5 (adversarial skeptic) -- steelman the rescue, then bound it honestly

**Steelman OPERATIVE (the rescue at full strength).** The open-system source is exactly the kind of
absorbing boundary channel that regularizes a resonance (PC2, Feshbach). The promotion gate drains
the C-positive record content out of the ghost sector -- a loss, normal-damping, opposing the
anti-damping (PC3, Section 4). Above a coupling ratio `r* ~ 1` the pole moves to the second sheet and
the grading is OPERATIVE (E2). This is a concrete mechanism, from the *open* structure the closed-
theory sprint (W178/W179/W172) by construction never included.

**Now bound it (each conceded, no manufactured rescue).**
1. *The BUILT part does not do it.* W180's actual construction is **ultralocal/algebraic**, hence a
   **real** self-energy: it shifts `M^2`, adds no width, does **not** move the pole (E1a). The sheet-
   moving power is entirely in the **unbuilt** nonlocal completion (the eta-from-gimmel-area residue).
   So at the currently-built order **NOT-OPERATIVE STANDS**.
2. *The SIGN is argued, not derived.* The opposing sign rests on the drain-direction + C-positivity
   argument (Section 4); it is **plausible and structurally supported**, but it is not a computed
   dressed width. If the dispersive part turned out reinforcing, E3 shows the pole never moves.
3. *The MAGNITUDE is the inherited unbuilt object.* Even with the opposing sign, the pole moves only
   for `r > r* ~ O(1)`, and GU's actual `kappa_ext/kappa_int` is the **eta-from-gimmel-area**
   (W180/W151), whose magnitude is exactly what those waves left unbuilt (only the sign forced).
4. *The channel-independence risk.* The opposing-sign argument needs the promotion channel to be
   **independent** of the two-graviton anti-damping channel. Argued independent (different final
   state), but at model rigor it is not proven orthogonal -- if they were the same leak, no
   subtraction.

**Skeptic's residue (honest).** The source term does **not** move the pole at the built order (real
ultralocal shift; E1). It **can** move it in the nonlocal opposing-sign regime above `r*` (E2), by a
genuine open-channel/Feshbach mechanism (PC2) with a sign-plausible drain direction (Section 4). So
the honest reading is **CONDITIONAL**, and the condition is a **sharpening** of the inherited
H59/W48 object, not a new one.

## 7. Verdict

**CONDITIONAL. SOURCE-TERM-DOES-NOT-MOVE-IT at the built ultralocal order (W178 NOT-OPERATIVE
STANDS); CAN move it (OPERATIVE) in the nonlocal opposing-sign regime above `r* ~ O(1)`.**

- **`Sigma_ext`'s contribution + sign.** BUILT (ultralocal, W180): a **REAL constant** (mass shift,
  **no width**) -- does not move the pole (E1a); removes the physical-sheet pole only by a large,
  magnitude-gated real shift that closes the decay channel (E1b). NONLOCAL completion (the unbuilt
  eta-residue): **dispersive**, with the sign set by the promotion-flux direction -- the gate
  **drains** the C-positive record content **out of** the ghost `q=5` sector = **loss** =
  **normal-damping** = `Im Sigma_ext(M^2+i0) < 0` = **OPPOSES** the internal anti-damping (PC3,
  Section 4).
- **Pole-sheet verdict with the source included (numbers).** At the built order **unchanged**: `1`
  physical-sheet UHP pole (NOT-OPERATIVE). With the dispersive opposing part: the physical-sheet UHP
  pole count flips **`1 -> 0`** (OPERATIVE) at `r* = 1.000` (equal thresholds; two-route check
  `r* = 1.500` at `s_ext_th = 0.60`), matching the on-shell width balance to `<0.02`/`<0.05`. The
  SIGN decides (E3: reinforcing never moves it); no spurious poles (NC1).
- **Open-channel/Feshbach assessment.** The boundary flux IS a genuine open channel (PC2: an
  absorbing channel drives the pole to the second sheet); it regularizes the pole in the
  **opposing-sign, sufficient-magnitude** regime, and only there.
- **Effect on bar (b): UNCHANGED verdict.** The open-system input **NARROWS** the inherited H59/W48
  residue to the sharper sub-question: *is the DISPERSIVE part of the promotion-gate boundary
  self-energy normal-sign (opposing) and of magnitude exceeding `r*` the internal anti-damping?* The
  magnitude is the SAME unbuilt eta-from-gimmel-area (W180/W151); the sign is sign-plausible from the
  drain direction. This is a refinement of the standing object, not a new one, and not a manufactured
  rescue.

**H59 remains OPEN.** No canon / RESEARCH-STATUS / claim-status / verdict / posture change.

## 8. What this does NOT do

- No claim that the pole IS on the second sheet: the built ultralocal source leaves it on the
  physical sheet (E1); the move (E2) is conditional on the **unbuilt** dispersive opposing-sign part.
- No derivation of the dressed `Sigma_ext`: it is a sqrt-threshold **model** self-energy (the KIND
  W124/W178 used), and the sign is **argued** (drain direction + C-positivity), not a computed width.
- No fixing of GU's `kappa_ext/kappa_int` relative to `r*`: that magnitude is the inherited
  eta-from-gimmel-area (W180/W151), only the sign forced.
- No proof of channel independence: argued (different final state), not shown orthogonal at model
  rigor -- the honest risk in the opposing-sign subtraction.
- No canon movement; no external action; the exploration is the computation, not a status change.
  W138 discipline: every load-bearing number has two routes or a matched control.

**Artifacts:** this file + `tests/W182_external_source_selfenergy.py` (11/11, exit 0).

*Filed 2026-07-14 by Team EXT-SELFENERGY (W182). Five personas inline in one worker
(open-quantum-system/Feshbach specialist, self-energy/dispersion specialist, GU-source specialist,
symbolic/numerical engineer, adversarial skeptic); no sub-agents. Reproducible:
`python -u tests/W182_external_source_selfenergy.py` (11/11, exit 0; positive controls first).
Exploration grade; coherence-first; no canon movement; H59 remains OPEN.*
