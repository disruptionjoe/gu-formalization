---
title: "DE-as-controller swing (CONSTRUCTION mode): model dark energy as a feedback CONTROLLER, survey the full controller taxonomy (not just PID), and test whether a SIGN-LOCKED controller (respecting GU's w>=-1 rail, no phantom overshoot) can (a) FIT the known DE data and (b) address the Lambda-magnitude fine-tuning via self-tuning. FINDING: the naturally sign-locked class is the PROPORTIONAL / canonical-kinetic controller (= GU's own theta-mode) plus the ONE-SIDED integrators (sliding-mode on the rail as sliding surface, and rectified/anti-windup ratchets = the relaxion class); the OVERSHOOT class (unbounded PI/PID, naive adaptive/LQR) is exactly what the rail forbids, and the control-theoretic overshoot is the field-theoretic kinetic-sign (Krein) flip. On the FIT: only the sign-locked P-controller lands inside the DESI-thawing corridor under w>=-1 (it IS PP1/PP3 re-described); it reproduces the thawing DIRECTION but not the phantom-crossing part of the CPL best fit -- the same live risk. On SELF-TUNING: a one-sided ratchet CAN self-tune AND be sign-locked, but it RELOCATES the ~meV tuning to its setpoint (Weinberg class-relative: evaded, not solved), and the ratchet is NEW physics NOT in GU. NEW falsifiable content: a candidate class discriminator (lift-off vs ride-the-rail vs cross) at PROPOSAL grade. HONEST GRADE: mostly a REFRAME of PP1/PP3 in control vocabulary; the sign-locked fit is FORCED-by-kinetic-sign (real), the self-tuning is FITTED/relocated (new physics, B5-gated). A full construction is NOT warranted now."
status: active_research
doc_type: exploration
created: 2026-07-21
mode: CONSTRUCTION (new hypothesis; posit labeled -- GU supplies only the rail)
directed_by: "Joe direct chat, 2026-07-21 (pre-registered DE-as-controller swing; one synchronous pass, new file + one probe, no commit)"
axiom: lab/process/boundary-adapter-standing-axiom.md
inputs:
  - explorations/comparative-tensions-ledger-cosmo-gravity-2026-07-21.md
  - explorations/parsimony-unexplained-joints-ledger-2026-07-21.md
  - explorations/blockbuster-p1-de-sign-covariance-2026-07-19.md
  - explorations/de-amplitude-audit-2026-07-20.md
  - explorations/prediction-package-pp3-de-curve-family-2026-07-20.md
probe: tests/channel-swings/de_controller_taxonomy_probe.py (foreground, numpy-only, no RNG, EXIT 0, double-run byte-identical, 10 [E] all PASS)
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
external_action: none
---

# DE-as-controller swing (CONSTRUCTION mode)

## 0. MODE, and the posit (binding, stated first)

This is a **CONSTRUCTION-mode** exploration of a **NEW hypothesis** that is
**NOT in GU**. GU supplies exactly one ingredient: the **`w(z) >= -1` sign-lock
rail** (Prediction Packet 1, frozen internal, toy/symbol grade, conditional on
SRC-COH-1 -- the readout identity `(rho_DE + p_DE) = eps * Z * Bdot^2` with
`eps` fixed by the external orientation bit `sigma`; the phantom side has no
surviving GR cancellation). Everything else in this document -- the *controller*
(a dynamical feedback object driving the vacuum energy), and any *self-tuning of
the amplitude* -- is **new physics layered on top of the rail**. The honest
split is enforced throughout and re-stated in Section 5.

> **THE POSIT (labeled).** *Dark energy is the output of a feedback controller
> whose loop regulates the vacuum-energy sector, and which -- if GU is right --
> is constrained to the sign-locked, no-overshoot (`w >= -1`) class.* GU neither
> contains nor forbids this controller; it only constrains its output sign. The
> payoff is graded against three bars (per the brief): does a sign-locked
> controller (i) FIT the known data under the rail, (ii) self-tune the
> amplitude, (iii) predict a distinctive falsifiable `w(z)` shape. A controller
> that merely re-fits `w(z)` with more knobs is worthless; the only wins that
> count are a controller class that is *naturally* sign-locked and/or
> self-tuning and predicts a specific shape.

Receipt for every dynamical claim below:
`tests/channel-swings/de_controller_taxonomy_probe.py` (foreground, numpy-only,
no RNG, **exit 0**, double-run **byte-identical**, headline `10 [E] = 10 ALL
PASS`). No likelihood is evaluated in this swing; the DESI DR2 / SNe / BAO fit
status is **consumed** from the frozen repo rows (PP1, PP3, the DE-amplitude
audit), never re-fit.

## 1. The control loop, made explicit

To talk about "which controller" we first fix the loop. The dark-energy sector
as a feedback system:

| control object | cosmological realization |
|---|---|
| **plant** | the FLRW background: the field `phi` with **Hubble friction `3H`** as built-in rate damping and the potential curvature `M^2` as the stiffness -- a **second-order** system (`phi'' + 3H phi' + V'(phi) = 0`) |
| **controlled variable** | the deviation of the equation of state from the rail, `w(z) + 1` (equivalently `rho_DE + p_DE`, the source of `Hdot`) |
| **actuator** | the field's kinetic channel: `rho + p = eps * phidot^2`, where **`eps` is the kinetic (Krein) signature** -- `+1` canonical, `-1` phantom/ghost |
| **setpoint** | `w = -1` (zero error = pure vacuum), and, for the amplitude, the target vacuum-energy scale |
| **the GU rail** | `eps = +1` locked by `sigma`: the actuator can only ever *push one way* off the setpoint (`w >= -1`); a controller that "overshoots" the setpoint would require `eps = -1`, which `sigma` forbids |

The single most important structural fact, and the spine of everything below
(probe Part A): **the side of the rail is `eps`, not a gain.** `rho + p = eps *
phidot^2` identically (probe: `max|rho+p - phidot^2| = 3e-16` across the whole
`M^2` band). No proportional/derivative/integral gain acting *through a
fixed-`eps` kinetic term* can move `w` to the other side of `-1`. Crossing the
rail is not a large control effort; it is a **change of the actuator's sign** --
the Krein flip GU's `sigma` locks. This is PP1's readout identity, re-derived in
control-systems language.

## 2. Persona (i) -- Control-systems engineer: the taxonomy, and who overshoots

Independent reasoning. The task is to enumerate the controller taxonomy, map
each to a `w(z)` response, and sort them by **whether they are naturally
one-sided-saturating (a hard rail at `w=-1`, no overshoot) or overshoot into
phantom.** The organizing theorem is elementary and decisive:

> **Overshoot = crossing the setpoint = (here) the kinetic-sign flip.** In a
> regulator, the element that *drives the steady-state error to zero* is
> **integral action**; the element that *causes overshoot and limit cycles* is
> **also** integral action (windup / phase lag). A pure proportional/derivative
> loop on a stable second-order plant **cannot overshoot into instability**;
> adding **unbounded integral** action makes the loop third-order and, above a
> critical gain, sends a pole into the right half-plane (Routh-Hurwitz). The
> cosmological image of that pole crossing is the actuator being asked for a
> configuration the canonical sector cannot supply without flipping `eps` --
> i.e. crossing the rail.

Probe Part B makes this concrete. The field loop `1/(s^2 + 3H s + M^2)` with a
PI controller `k_p + k_I/s` has characteristic polynomial `s^3 + 3H s^2 +
(M^2+k_p) s + k_I`; Routh-Hurwitz gives the critical integral gain **`k_I* =
3H(M^2 + k_p)`** (probe: `k_I* = 24` at `H=1, M^2=8, k_p=0`). Below it the loop
is stable (`max Re(pole) = -0.5`); above it a pole crosses to `Re > 0` (`+0.29`).
Pure P/D action (`k_I = 0`) is unconditionally stable. **A one-sided / rectified
integrator (anti-windup ratchet) cannot wind past the setpoint, so it never
acquires the destabilizing pole** -- it stays in the stable class.

**The taxonomy, mapped.**

| controller | DE realization | `w(z)` response | rail behavior |
|---|---|---|---|
| **bang-bang / relay** | first-order-transition / stepped potential | sharp switching features, chatter | **overshoots** (chattering = limit cycle across setpoint) |
| **P (proportional)** | **mass term `V=1/2 M^2 phi^2`** (gain `M^2`, setpoint = VEV) -- **the GU theta-mode** | **thawing**: frozen at `-1` by `3H`, lifts as `H` drops below `M`, then oscillatory/matter-like | **naturally one-sided** (`eps=+1` canonical -> `w>=-1` pointwise) |
| **PD** | mass term + explicit rate coupling (Hubble friction is already D) | damped thawing, faster settle | **naturally one-sided** (still canonical) |
| **PI / PID (unbounded I)** | integral of the vacuum-energy error driving the field | drives error toward 0 but **overshoots** | **CROSSES** the rail above `k_I*` (Krein flip) -- FORBIDDEN by `sigma` |
| **integral-only** | pure accumulator | marginal / drift | overshoots unless rectified |
| **lead-lag** | non-minimal / derivative (Horndeski `G3,G4`) shaping | frequency-shaped lift | side depends on sign; not naturally locked |
| **LQR / optimal** | quadratic-cost linear state feedback | tunable damped response | **fitted**: can be made non-overshooting, nothing *forces* it |
| **MPC (constrained)** | receding-horizon with hard constraint `w>=-1` | any admissible shape, rail enforced by constraint | rail-respecting **by design** (a stand-in for a constrained variational principle) -- fitted, not forced |
| **gain-scheduled** | field-dependent mass `M^2(phi)` | thawing/freezing quintessence | one-sided iff kinetic stays canonical |
| **adaptive (MRAC / self-tuning regulator)** | parameters track to cancel vacuum energy (**sequestering / Fab-Four**) | self-tuning transient | **overshoot-prone** (adaptive bursting) unless one-sided |
| **sliding-mode (SMC)** | sliding surface `s = (w+1) >= 0`, reaching law | **reach then RIDE the rail** (`w -> -1` and stays) | **naturally one-sided-saturating** -- the rail *is* the sliding surface |
| **feedback-linearization** | design `V(phi)` for a target `w(z)` | arbitrary | pure fit; worthless as "forced" |
| **H-infinity** | robust DE sector vs matter perturbations | robust damped | design choice; not naturally locked |

**Engineer's verdict.** Three archetypes are **naturally one-sided-saturating**:
(1) the **proportional / canonical-kinetic controller** (rail respected because
`eps=+1`, i.e. the actuator has no wrong-sign mode); (2) **sliding-mode with the
rail as the sliding surface** (the surface `w=-1` is an invariant the reaching
law approaches from above and never crosses); (3) the **rectified / anti-windup
integrator (ratchet)** -- the relaxion class -- which zeroes error from *one
side* and cannot overshoot. The whole **overshoot family (unbounded PI/PID,
naive LQR, adaptive-with-bursting, bang-bang)** is precisely what the rail
forbids, and it forbids them *for the same reason in every case*: overshoot
demands the Krein flip.

## 3. Persona (ii) -- Dark-energy phenomenologist: does a sign-locked controller FIT?

Independent reasoning. Map controller outputs to `w(z)` and check the
data-allowed region under the rail. The relevant data landscape (consumed, not
re-fit): **DESI DR2** prefers a CPL point in the `(w0 > -1, wa < 0)` thawing
quadrant whose central curve formally crosses to `w < -1` at moderate `z`; **SNe
(Pantheon+)** and **BAO** are consistent with that corridor; the repo's frozen
adjudication (DE-amplitude audit) puts GU's own sector as an **LCDM mimic**,
`f0 < 0.027` (canonical), `|w0+1| < 0.04`, with the split an upper limit, not a
detection.

**Which controllers land inside the data-allowed region under `w>=-1`?**

- The **P-controller (mass term = GU theta-mode)** produces exactly a **thawing
  curve in the DESI quadrant**: `w0+1 > 0`, `wa < 0`, on the frozen PP3 slope
  `R = wa/(w0+1) ~ -1.0 to -1.3`, pointwise `w >= -1` (probe Part A: `w0 = -0.89`
  for the demo displacement, `min(w+1) = 0` at the rail, monotone thawing lift).
  This is the **one class that fits** -- and it fits because it *is* PP1/PP3.
- The **sliding-mode / saturating** controller fits the *null* corner (rides the
  rail, `w ~ -1`), indistinguishable from LCDM unless it leaves the rail.
- The **overshoot (PI/PID) class** would fit the phantom-crossing part of the
  DESI CPL central curve -- **but that is the forbidden side.** So the
  phenomenology splits cleanly: the *thawing* part of the DESI hint is
  reproducible by a sign-locked controller; the *phantom-crossing* part is
  reproducible only by the overshoot class the rail excludes.

**Is the DESI thawing hint reproducible by a sign-locked controller? YES for the
direction, NO for the crossing.** A sign-locked P-controller reproduces `w0 > -1,
wa < 0` (thawing) and sits on the PP3 locus; it **cannot** reproduce a robust
pointwise `w < -1` at any `z`. This is precisely the repo's live-risk posture:
the current DESI-CPL preferred region *implies* crossing at moderate `z`, and if
that consolidates into a robust >=3-sigma pointwise `w<-1` (KILL-P1-B), the entire
sign-locked-controller hypothesis dies with PP1. **Honest fit status: the
sign-locked P-controller fits the surviving LCDM-mimic / thawing band and is
exposed to the crossing, exactly as PP1/PP3 already are. The controller framing
adds no new fit -- it re-describes the existing one.**

## 4. Persona (iii) -- Self-tuning / dynamical-systems theorist: the amplitude

Independent reasoning. Which controllers are self-tuning *attractors* that could
address the `~10^-120` / `~meV` amplitude fine-tuning, and does the setpoint
merely relocate the tuning?

**A feedback controller driving an error to zero IS a self-tuning attractor** --
the same object as Fab-Four self-tuning, vacuum sequestering, or cosmological
relaxation, viewed through control theory. Probe Part C exhibits the mechanism
honestly on a toy:

- **Self-tuning is real (attractor is IC-independent).** A rectified-integral
  (ratchet) controller drives an effective `Lambda` from initial conditions
  **spanning 120 decades** (`1` to `1e120`, i.e. a Planck-scale vacuum energy) to
  **one common attractor** (probe: spread `0` about the setpoint `1e-3`). This is
  the genuine appeal -- the mechanism does not care where `Lambda` starts.
- **But the attractor value = the setpoint, and the setpoint is a FREE INPUT.**
  Move the setpoint, the attractor moves 1:1 (probe: `attractor(setpoint) =
  1e-4, 1e-3, 1e-2, 3e-2`). So the mechanism converts *"why is `Lambda ~
  10^-120`"* into *"why is the controller's setpoint at `~meV` rather than
  exactly zero."* This is a genuine, respectable **reframing -- not an
  elimination.** (Matches the comparative-tensions ledger 5.4 verdict exactly:
  "legitimate member of the self-tuning class; not a solution, a relocation.")
- **Weinberg no-go is class-relative -- and evaded, not solved.** Probe Part C's
  Weinberg check: a *static, constant-field* equilibrium with *zero total vacuum
  energy* over-determines the single field value (`V'(phi*)=0` AND `V(phi*)=0`:
  two conditions, one unknown), so only a **tuned parameter** (`Lam_bare = 0`)
  gives a zero-energy static point (probe: generic residual `0.700`; only the
  tuned value gives `0`). The **never-static ratchet evades the LETTER** by never
  sitting at such a point -- exactly how Fab-Four (gives up static),
  sequestering (gives up local/finite), and relaxation (dynamical scan) evade
  Weinberg's assumptions. Evasion is real and licensed (the repo's standing
  "no-go may be class-relative" posture); it is **not** a solution of the CC
  problem -- the residual setpoint tuning remains.

**The one clean win at the intersection.** The controller that is **both**
sign-locked **and** self-tuning is the **one-sided / rectified integrator
(ratchet, relaxion class)**: it zeroes from one side (no overshoot -> rail-safe)
*and* it is an IC-independent attractor. Unbounded PI/PID is self-tuning but
overshoots (rail-violating); the pure P-controller is rail-safe but **not**
self-tuning (it has a fixed setpoint = the imported VEV). **So the sign-lock and
the self-tuning are compatible only in the one-sided-integrator corner -- and
that corner still relocates the tuning to its stopping scale.**

## 5. Persona (iv) -- GU-constraint keeper: the honest in-GU vs new-physics split

Independent reasoning. Enforce the split and grade.

| ingredient | in GU? | grade |
|---|---|---|
| the sign-lock rail `w(z) >= -1`, no phantom overshoot | **IN GU** | PP1 frozen (toy/symbol, cond. SRC-COH-1). The rail = `eps=+1` = canonical kinetic = "the actuator has no wrong-sign mode." |
| GU's own DE controller | **IN GU** = a **pure P-controller** (the theta-mode: mass term `M^2` in the root band, setpoint = the VEV) | reconstruction/toy grade (PP3 locus). **Not self-tuning** -- setpoint imported. |
| the DE **amplitude** / `~meV` setpoint being *solved* | **NOT in GU** | `PRED-NORM-RANK = RESOLVED_NO_GO`; the amplitude is a pure import into the blocked **B5** source-action slot ("as brute as `Lambda`"). |
| a **self-tuning** (integral / ratchet / adaptive) controller existing | **NOT in GU** | GU has **no built source action** (B5 blocked) -> no dynamical relaxation mechanism at all. GU neither proposes nor forbids it; it only constrains its output sign. |

**Keeper's ruling.** "GU's `sigma` closes the `Lambda` fine-tuning via a
self-tuning attractor" is **false / an inflation** -- GU's native DE controller
is a *pure proportional* controller with an *imported* setpoint; it does no
self-tuning. What GU genuinely contributes is the **no-overshoot rail**: a hard,
falsifiable, one-sided constraint on the *entire controller class* -- any
GU-compatible DE controller must be sign-locked (P / canonical-kinetic /
sliding-on-the-rail / rectified-integral), never an unbounded PI/PID that
overshoots into phantom. That is a real, narrow contribution, and nothing more.

## 6. Synthesis (four inline personas reconciled)

**The three-bar scorecard (per the brief).**

1. **FIT under the rail.** Only the **sign-locked P-controller** (= GU
   theta-mode) lands inside the DESI thawing corridor while respecting `w>=-1`;
   it reproduces the thawing *direction* but not the phantom-*crossing* part of
   the CPL best fit. **This is PP1/PP3 re-described -- no new fit, same live risk
   (KILL-P1-B).**
2. **SELF-TUNE the amplitude.** A **one-sided ratchet** (relaxion class) is the
   unique controller that is *both* sign-locked *and* self-tuning; it drives
   `Lambda` to an IC-independent attractor -- **but relocates the `~meV` tuning
   to its setpoint** (Weinberg class-relative: evaded, not solved), and it is
   **new physics not in GU** (B5-gated). GU's own controller does **not**
   self-tune.
3. **DISTINCTIVE `w(z)` signature.** See Section 7 -- one candidate, PROPOSAL
   grade.

**The deep unifying statement the controller lens buys (this is the genuine
intellectual yield):** *the GU sign-lock is exactly the control-theoretic
statement that the DE regulator has no unbounded integral action -- because
"zeroing the steady-state vacuum-energy error" (the job of integral action) and
"overshooting the setpoint into phantom" (the failure mode of integral action)
are the same element, and `sigma` forbids the overshoot.* Therefore, if GU is
right, the DE controller is confined to `{P, PD, sliding-on-the-rail,
rectified-one-sided-integral}` and excluded from `{unbounded PI/PID, naive
adaptive, bang-bang}`. And the field-theoretic name of the excluded pole (the
Routh-Hurwitz RHP crossing) is the **Krein-sign flip** -- the same bit `sigma`.

## 7. Distinctive falsifiable signature (candidate new prediction, PROPOSAL grade)

Beyond the bare no-crossing bound (PP1) and the PP3 thawing locus, the
controller taxonomy suggests one **candidate new discriminator** (probe Part D):
the **class of the controller is readable from the late-time shape of
`w(z)+1`**:

- **P-controller (GU-native):** `w+1` **lifts off** the rail monotonically
  (thawing away from `-1`), then goes oscillatory/matter-like -- it does *not*
  regulate back to `-1` (probe: `w+1: 0 -> 0.11`, a lift).
- **Sliding-mode / saturating controller:** `w+1` **returns to the rail** --
  a genuine regulator with setpoint `w=-1` drives the error back down; `w(z)`
  turns over and heads back toward `-1` at late times (probe: the sliding
  trajectory rides down to `0^+`). **A non-monotone `w(z)` that peaks and
  returns to the rail is the fingerprint of an actual regulating controller** --
  distinct from monotone thawing quintessence, which only leaves the rail.
- **Overshoot / phantom class:** `w+1` **crosses** below `0` (probe: phantom
  `min(w+1) = -0.67`) -- the forbidden side; a robust detection kills the whole
  sign-locked hypothesis.

**Grade of this signature: PROPOSAL, and honestly NOT GU-native.** GU's own
controller is the P-controller, which *lifts off* and does **not** return to the
rail. So a detected **"return-to-rail" (non-monotone `w(z)`)** would be evidence
for a **sliding/ratchet controller that is NOT in GU** -- it would support the
*new-physics* layer, not GU itself. The signature is a genuine, computable,
pre-registerable discriminator among sign-locked controllers, but it does not
rise to a *forced* GU prediction. It is a candidate refinement for the
source-action campaign, not a near-term kill test. (The near-term kill remains
KILL-P1-A/B: any robust pointwise `w<-1`.)

## 8. The honest forced-vs-new grade, and whether a construction is warranted

**Forced vs fitted, line-itemed.**

| element | forced or fitted? | why |
|---|---|---|
| the rail `w>=-1` (sign-lock) | **FORCED** (by the kinetic/Krein sign = `sigma`) | `rho+p = eps*phidot^2` identically; no gain crosses it (probe Part A). Real, and already GU (PP1). |
| the sign-locked class being `{P, sliding, one-sided-I}` | **FORCED** given the rail | overshoot = Krein flip = forbidden; this is a theorem, not a fit (probe Part B). Genuine *reframe* content. |
| the DESI thawing fit | **RE-FIT, not new** | it *is* PP3; the controller lens re-describes it, adds no knob and no new fit. |
| self-tuning the amplitude | **FITTED / RELOCATED** | a ratchet self-tunes but the setpoint is free (probe Part C); Weinberg evaded not solved; and the ratchet is **new physics, not in GU**. |
| the return-to-rail signature | **new, PROPOSAL grade, non-GU-native** | a real discriminator, but its positive detection supports the *added* controller, not GU. |

**Is this worth a real construction (routed through the source action / B5)?
NO -- not now.** Two reasons, both structural:

1. The **sign-locked controller that FITS is already built** -- it is the GU
   theta-mode / PP1 / PP3. A "construction" of it would duplicate frozen work.
2. The **only genuinely new payoff (a self-tuning, sign-locked controller that
   fixes the amplitude) is B5-gated new physics.** To be GU-native, the ratchet
   / one-sided-integral element would have to be *emitted by the source action*
   (B5), which is **blocked** -- the same bottleneck that gates every native DE
   result. Building the controller before B5 exists would be positing the
   mechanism, not deriving it; and even if built, it relocates rather than
   eliminates the tuning (Weinberg class-relative).

**Routing recommendation (proposal only; nothing executed).** Record this
document as the **control-systems reframe** of the DE sign-lock -- valuable
vocabulary that (a) sharpens *why* the rail is one-sided (no unbounded integral
= no overshoot = no Krein flip) and (b) cleanly separates GU's contribution
(the rail) from the self-tuning new physics (the ratchet). Flag the
**"return-to-rail" discriminator** as a candidate refinement for the
**source-action / B5 campaign** (if B5 ever emits a dynamical DE sector, ask
whether it is a P-controller (lifts off) or a regulator (returns) -- the shape
reads the mechanism). **Do not open a new construction lane.** The one wire that
matters remains the DESI/Euclid no-phantom-crossing test.

## 9. Receipts

- Probe: `tests/channel-swings/de_controller_taxonomy_probe.py`, run
  2026-07-21, **exit 0**, double-run **byte-identical**, headline `10 [E] = 10
  ALL PASS`, numpy-only, no RNG. Parts: A (rail = kinetic sign, gain-independent,
  `rho+p=eps*phidot^2` to `3e-16`, `w>=-1` across the `M^2` band `{3,7,8}`); B
  (Routh-Hurwitz `k_I* = 3H(M^2+kp) = 24`; pole crosses to `Re=+0.29` above it;
  one-sided integrator stays stable); C (self-tuning attractor IC-independent
  over 120 decades; setpoint free = relocation; Weinberg static overdetermination
  = tuning); D (three-class `w(z)` discriminator: lift / ride / cross).
- Consumed frozen rows (not re-derived): PP1 readout identity and rail
  (`blockbuster-p1-de-sign-covariance-2026-07-19.md`); PP3 thawing locus and
  slope (`prediction-package-pp3-de-curve-family-2026-07-20.md`); amplitude =
  import, `PRED-NORM-RANK NO_GO`, `f0 < 0.027` (`de-amplitude-audit-2026-07-20.md`);
  Weinberg class-relativity and the PID-is-a-relocation verdict
  (`comparative-tensions-ledger-cosmo-gravity-2026-07-21.md`); the amplitude as
  GU's open/brute joint (`parsimony-unexplained-joints-ledger-2026-07-21.md`).

## 10. Boundary

Exploration tier under the standing axiom, `R0_COND` working grade,
**CONSTRUCTION mode** with the posit labeled (Section 0). Two NEW files written
-- this document and the probe -- no existing file edited. **No claim-status, no
canon-verdict, no scorecard, no register, no paper-status, no public-posture
movement**; nothing committed, nothing pushed, nothing external (Joe alone ever
takes anything outside). PP1/PP3/audit rows and the `sigma`/`tau` externality
are consumed, not moved. No likelihood was evaluated; the controller framing
re-describes the frozen fit rather than re-fitting data. The self-tuning result
is a **relocation, not a solution**, and the self-tuning controller is **new
physics not in GU**; the rail is the only in-GU ingredient. The
"return-to-rail" discriminator is **PROPOSAL grade** and, if detected, supports
the added controller, not GU. Order-of-grade bookkeeping only; no physical
probabilities. Research-only: no shipping, publishing, or process advice.
