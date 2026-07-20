---
title: "S-matrix face of the sector sign: DYNAMICAL BLINDNESS PROVEN at toy grade (K-a for the S-matrix proper + K-b for the graded-current residue) -- the TRANSPARENCY THEOREM (S(E) contains no K_S at all; the sector flip acts as (S, eps) -> (S, -eps)) extends the Araki even/odd selection rule to all of scattering, and the two blindness mechanisms are named: ghost conjugation V = sigma2 x omega (annihilates every ungraded-prepared odd reading identically) and parity transfer T(-D) = W T W^-1 (sector-parity = symbol-orientation-parity for every scattering functional) -- the payload bit's external-posit typing is STRENGTHENED to dynamical grade; the conserved Krein current is K_S-linear, T-odd, and NON-QUATERNIONIC, an orientation consumer that dynamics cannot orient"
status: active_research
doc_type: exploration
created: 2026-07-20
directed_by: "Joe direct chat, 2026-07-20 (big swing: S-matrix face of the sector sign)"
axiom: "lab/process/boundary-adapter-standing-axiom.md for the SECTOR reading of the accounting (R0_COND, as in F2/F5/m1); the transparency, ghost-conjugation, and parity-transfer theorems themselves are unconditional linear algebra on the verified rep"
extends:
  - explorations/m1-third-reading-2026-07-20.md
  - explorations/araki-scale-route-2026-07-20.md
  - explorations/f5-signed-fraction-2026-07-20.md
inputs:
  - explorations/m1-third-reading-2026-07-20.md
  - explorations/araki-scale-route-2026-07-20.md
  - explorations/f5-signed-fraction-2026-07-20.md
  - explorations/n2-end-family-2026-07-20.md
  - explorations/W172-interacting-c-operator-nogo-2026-07-14.md
  - tests/channel-swings/m1_third_reading_probe.py
  - tests/channel-swings/n2_end_family_probe.py
  - GEOMETER-VS-PHYSICS-OBJECTS.md
runnable:
  - tests/channel-swings/smatrix_sector_face_probe.py
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
external_action: none
---

# Does the sector bit have a dynamical face?

The program's central Z/2 payload bit -- the Krein-sector orientation,
K_S -> -K_S under the faithful loop holonomy -- is externally posited
(bar-b, p2c-owned). The Araki swing proved the STATIC selection rule:
every K_S-even functional (every entropy-class, positive-reference
object) is sector-blind; only K_S-LINEAR pairings can read the sector,
and the one reader in hand (k_sigma) is a static functional of the cut.
The open question this swing answers: does any SCATTERING observable --
an S-matrix functional, the dynamical class -- sit in the K_S-linear
reading class? A positive would have been PP4-shaped. The answer is a
theorem-shaped negative, with the mechanism named twice over.

**Verdict up front: K-a fired for the S-matrix proper, K-b for the
residue; K-c did not fire.** The S-matrix of the faithful wall-scattering
toy contains NO K_S anywhere: the sector flip acts on scattering data as
(S, eps) -> (S, -eps), where eps is the channel Krein grading. Every
functional of S alone -- every cross-section analog, width, delay,
eigenphase, relative resonance phase, in/out asymmetry -- is K_S-even
and blind. The K_S-linear scattering class is nonempty (graded-current
functionals, dynamical per channel) but doubly annihilated as a sector
face: a ghost-conjugation symmetry kills every ungraded-prepared odd
reading identically, and a parity-transfer identity makes every
sector-odd scattering functional equally odd under the symbol
orientation convention. A nonzero reading requires an externally fixed
absolute orientation of the conserved current -- which IS the standing
external Z/2 posit. Dynamics consumes the orientation; it cannot
produce it. The external-posit typing of the bit is STRENGTHENED, now
at dynamical grade (toy level). No claim, canon, or posture movement;
no PP4 candidate packet is written (admission criteria not reached --
there is no observable).

Receipt: `tests/channel-swings/smatrix_sector_face_probe.py` --
deterministic (double-run byte-identical), numpy only, no new RNG draws
(all randomness upstream in the m1/n2 seeded stream 20260720), exit 0 --
HEADLINE `12 [E] + 4 [F] = 16 (setup [T] = 3 excluded) ALL PASS`. The m1
probe is executed IN-LOAD as the machinery source (its 16 checks re-run
and pass as a free regression receipt; no existing file edited).

## 1. Pre-declared kill/outcome conditions (in the dispatch before computing)

- **K-a (dynamical blindness theorem):** every S-matrix functional of
  the toy is K_S-even -- the selection rule extends to scattering; the
  external-posit typing is STRENGTHENED.
- **K-b (readable but unrealizable):** K_S-linear scattering functionals
  exist but all require probes with no in-principle physical realization
  independent of an external orientation datum.
- **K-c (the dynamical face):** an in-principle-observable asymmetry
  flips with the sector, survives all trichotomy controls, and its
  non-quaternionic consumer is named; then the PP4 admission criteria
  are checked.

**Which fired: K-a for the S-matrix proper (Sections 4b, 4d), K-b for
the graded-current residue (Sections 4e-4f).** Clause-by-clause receipts
below.

## 2. The toy (constructions named -- GEOMETER-VS-PHYSICS-OBJECTS discipline)

Scattering across the wall region of the faithful Y14-end model, on the
actual N2 objects (same machinery, same seed, same stream as the n2/m1
probes -- the same 53 crossing rays). At a crossing radius s = s* + 0.4
the loop coordinate t crosses the null cone on an open interval (the n2
t-holes); a window [t_lo, t_hi] containing it, with gapped ends, is the
scattering line: gapped asymptotic regions, the crossed (wall) region as
the resonator.

| Object | Construction | Status |
|---|---|---|
| propagation line | the loop coordinate t through the crossed interval; piecewise-constant symbol family D(x) = c(xi(t(x), s)) | the actual N2 family, frozen per segment |
| collar normal | Cl(9,5) at DIM 128 has no 15th generator: the spinor space is DOUBLED, C^2 tensor C^128 -- gamma_a = sigma1 x e_a, Gamma = i sigma2 x I (Gamma^2 = -I, anti-Hermitian, anticommutes with all gamma_a) | the standard boundary-restriction doubling; program-native, NOT a positivity import |
| wave equation | Gamma(d/dx + D~)psi = E psi, D~ = sigma1 x D(x); psi' = A psi, A = -D~ - E Gamma with A^2 = (q(x) - E^2) I EXACTLY | every transfer step has the m1 entire-in-q closed form |
| dispersion | gapped ends propagate for E^2 > q_end (modes +-ik, k = sqrt(E^2 - q)); the crossed region q < 0 is the resonator | the wall supplies the pole structure |
| mode split | KINEMATIC: the +-ik eigenspaces of A (limiting-absorption direction assignment) | consumes NO K_S |
| channel normalization | unit |Krein flux| per channel; the grading operator eps = C^dag X1 C carried separately | |flux| is K_S-EVEN; eps is K_S-ODD |
| conserved structure | the Krein current pair X1 = sigma2 x K_S, X2 = i I x (K_S omega), omega = e_0...e_13 | indefinite; NO positive metric anywhere |

The crossed-region transfer step at E = 0 EQUALS the m1 both-modes
evolution under q -> -q -- the same entire C/S series, machine-checked
at 1.4e-17: the resonator content of the wall IS the both-modes
complex-pair structure, Wick-continued to the collar propagation
coordinate. One construction, not two. The lineshape receipt: the
transmission trace rises from threshold to a resonance peak
(Tr t^dag t/128 = 1.58 at E = 12.4, threshold 9.8) and relaxes toward 1;
PT/Kramers reality J~ T(E) J~^-1 = T(conj E) holds at 1.2e-15, so poles
come in complex-conjugate pairs. On the gapped control ray the same
classification runs with no wall structure to manufacture.

## 3. The conserved current: the only sector-sensitive structure, classified

**(a) Existence and completeness.** X1 = sigma2 x K_S and
X2 = i I x K_S omega are Hermitian and conserved by the actual
wall-window transfer machine-exactly (T^dag X T = X at 3.2e-15);
sigma3 x K_S, I x K_S, and the Dirac identity are NOT conserved
(defects O(1)). Completeness is structural, not enumerative: the D-part
of the conservation condition reads X D~ = -D~^dag X, and
X -> (form-factor) K_S^-1 X bijects conserved currents onto the
ANTICOMMUTANT of the symbol family -- so **every conserved current
carries exactly one factor of K_S and is K_S-LINEAR**, for any span
rank of the window family (the window spans rank 5 of 14; recorded
receipt). There is no K_S-even conserved current to measure with.

**(b) The current is T-odd and NON-QUATERNIONIC.** J~ = I x J_quat
commutes with the whole dynamics and maps right-movers onto left-movers
(residual 1.5e-14): J~ IS the time reversal of the scattering problem.
Both currents ANTI-commute with J~ (defect 0.0): currents are T-odd,
exactly as physical currents must be. This is the Kramers-guard
consistency the mission demanded, discharged in the strongest form: the
canon no-go (every J-commuting Hermitian probe is sector-blind) is not
merely respected -- the only sector-sensitive structures in the entire
scattering apparatus are exactly the non-quaternionic (J-anticommuting)
objects the no-go permits. The named non-quaternionic consumer exists:
it is the conserved Krein current itself. But it is an orientation
CONSUMER, not producer -- Sections 4e-4f.

**(c) Channel structure.** The flux Gram on the kinematic right-movers
has signature (64,64) with ALL |eigenvalues| equal (quaternionic
uniformity, as at the m1 walls) and is exactly X1-orthogonal to the
left-movers: 64 positive-flux and 64 negative-flux (ghost) channels per
direction. Graded flux conservation holds at S level machine-exactly
(E_in = t^dag E_trans t - r^dag E_refl r, both incidences, cross-identity
closing the full graded S-unitarity, defects 2.5e-15): conservation is
INDEFINITE, both-modes-shaped, exactly as the universal-null lemma
demands -- no positive conservation law exists to import, and none was.

## 4. Results (the classification)

**(a) The even class receipts.** Battery: Tr t^dag t, Tr r^dag r,
singular values of t, the double-graded trace Tr(t^dag E t E). All
channel-gauge invariant; all EQUAL under the sector flip to 4.9e-16.
(Phases of det t are channel-gauge data, not observables -- consistent
with the [F] channel-gauge control.)

**(b) THE TRANSPARENCY THEOREM (central result).** Under K_S -> -K_S the
ENTIRE S-matrix -- all four blocks, both incidences -- is IDENTICAL to
machine zero (3.0e-15) while the channel grading flips exactly. The
sector flip acts on scattering data as **(S, eps) -> (S, -eps)**.
Mechanism: the dynamics (A = -D~ - E Gamma), the kinematic mode split,
and the |flux| normalization consume no K_S-sign anywhere. Consequence:
every functional of S alone -- |S_ab|^2 elements, total cross-section
analogs, line widths, Wigner delays, eigenphases, relative phases
between the paired resonance legs, in/out asymmetries -- is K_S-EVEN
and sector-blind. **The Araki even/odd selection rule extends to the
whole S-matrix.** (Mission question 1, answered: ALL of them.)

**(c) The flip realized as deck transport.** Conjugating the whole
window family by the faithful holonomy U_h with K_S held fixed acts on
the functional battery exactly as K_S -> -K_S (even class invariant at
1e-15-grade, graded class flips at 1.9e-14): the form-side and
transport-side realizations of the sector flip agree on all scattering
data, as m1 deck-compatibility requires.

**(d) The K_S-linear class is NONEMPTY and dynamical.** Single-grading
functionals (graded transmission/reflection) flip exactly under the
sector flip, and per-channel graded transmissions are nonzero (0.25 on
the main ray; 0.25-0.60 across the sampled rays). The blindness below is
a theorem about what can CONSUME the odd class, not an empty class.
(Mission question 2, first half: yes, K_S-linear scattering functionals
exist.)

**(e) BLINDNESS MECHANISM 1 -- GHOST CONJUGATION.** V = sigma2 x omega
is a Hermitian unitary involution that COMMUTES with the entire dynamics
(Gamma, every window symbol, the full transfer; defects 0.0) and
ANTI-commutes with BOTH conserved currents (0.0). Machine consequence:
every fully-traced (V-symmetric, i.e. ungraded-prepared) K_S-odd
functional vanishes IDENTICALLY -- graded transmission and reflection
traces are exact zeros (6.6e-15) while their per-channel entries are
O(0.1). The dynamics pairs every ghost channel with a non-ghost partner
of equal dynamics and opposite grading. A nonzero sector-odd reading
therefore requires a GRADED PREPARATION -- an input state that already
encodes the current's orientation. The dynamics cannot break the
V-degeneracy for you.

**(f) BLINDNESS MECHANISM 2 -- PARITY TRANSFER (the orientation
equivalence).** Conjugation by W = I x omega maps the symbol-orientation
flip (D -> -D, K_S fixed) EXACTLY onto the sector flip (D fixed,
K_S -> -K_S): T(-D) = W T W^-1 at machine zero, and W carries both
currents to minus themselves. Verified on the battery: under D -> -D
every even functional is invariant and every graded functional flips --
IDENTICALLY to the sector flip. So for EVERY scattering functional,
**sector-parity = symbol-orientation-parity**: any K_S-odd scattering
reading moves under the kappa-type orientation convention (xi -> -xi)
and is a gauge artifact AS A SECTOR FACE unless an absolute symbol
orientation is externally fixed -- which is the same single Z/2 posit
the bit already was. Contrast, and this is the sharp point: the static
reader k_sigma is xi-EVEN (it consumes the cut, quadratic in xi --
S = K_S e^{alpha w} with w bilinear), which is exactly why it can read
the sector without touching the orientation. No scattering functional
has that option: the dynamics couples through c(xi), linearly. The
dynamical route does not merely fail to read the bit -- it CONVERTS the
bit into an orientation convention it cannot fix.

**(g) Sampled corroboration.** Boost wall, three seeded n2 sweep
crossing rays, and the gapped conformal control ray: transparency,
ghost conjugation (with exact-zero traced odds), and parity transfer
hold at machine zero at every sampled configuration; per-channel graded
content is nonzero on every crossing ray. Family-wide mechanisms, not
one-ray accidents.

**Trichotomy controls (all mandatory, all run):** same-sign-plane
transport (U_ss): the entire battery, even AND graded, exactly
invariant. Covariant pseudo-unitary frame dressing (non-unitary boost
included, M^dag K_S M = K_S at 6.6e-18): all functionals exactly
invariant; re-deriving bases independently exposes only the residual
grading-pseudo-unitary channel gauge, itself K_S-even. Channel-gauge
moves (grading-commuting unitaries; the m1 per-pair phase gauge lives
here): invariant. SRC-REJ-1 guard: C2 obeys its closed-form law at the
window points untouched; the toy makes no source-side claim.

## 5. What this does and does not move

- **The bit's typing.** The value of bar-b was externally posited on
  static grounds; this swing adds: it is dynamically unreadable at toy
  grade -- the S-matrix is transparent to it, and the only dynamical
  structures that touch it (the currents) consume an orientation rather
  than produce one. The 5-method static reduction and this dynamical
  extension now say the same thing from independent directions. Typing
  STRENGTHENED; no claim movement (R0_COND working grade for the sector
  reading; the three theorems are unconditional algebra).
- **The twist vs the value (do not conflate).** The Z/2 TWIST (the
  holonomy character, U_h^dag K_S U_h = -K_S) is native, proven, and
  HAS dynamical shadows -- it is exactly why the graded functionals
  flip under deck transport. What has no dynamical face is the VALUE
  (which sector is positive). Interference-style experiments read
  relative signs (the twist's existence); they cannot mint the absolute
  orientation. The payload is the orientation.
- **Relation to the Araki selection rule.** The selection rule said:
  even channel blind, K_S-linear channel reads. Scattering refines it:
  the S-matrix sits ENTIRELY in the even channel (transparency); the
  K_S-linear channel exists dynamically but factors as
  (static grading) o (blind S) and is orientation-hungry. No new reader
  was created; the static reader k_sigma remains the only one, and it
  is not a scattering observable.
- **Relation to the universal-null lemma and W172.** Consistent and
  consumed: the S-level conservation law is indefinite (both-modes-
  shaped), as the lemma requires; no positive channel metric exists or
  was imported; W172's text and the m1 fork-conditional are untouched.
- **Kramers no-go.** Fully consistent (Section 3b): no J-commuting
  Hermitian probe appears anywhere in the odd class; the named
  non-quaternionic object is the conserved current, and naming it is
  what exposed the orientation-consumer structure.

## 6. Council pass (inline, five lenses)

- **Scattering theorist (unitarity/Breit-Wigner honesty in the Krein
  setting):** the toy is a legitimate scattering problem: well-posed
  transfer, kinematic in/out split with a limiting-absorption direction
  assignment, exact graded flux conservation at S level, threshold
  behavior and a resonance peak over the wall, PT-reality forcing
  conjugate pole pairs. What it is NOT: a positive-unitarity S-matrix
  -- and that is the point; the conservation law available is the
  indefinite graded one, and the probe verifies it is EXACT. Honesty
  flags: the lineshape receipt is shape-grade (peak + relaxation), not
  a fitted Breit-Wigner; pole positions were not hunted in the complex
  plane (PT-reality receipt instead); the Wigner-delay claim rides on
  transparency (S identical => delays identical), not on a separate
  delay computation. None of these gaps can move the verdict: they are
  all functionals of S alone, and S is identical under the flip.
- **PT/Krein theorist (fidelity to the both-modes construction):** the
  toy consumes m1 faithfully: V = K_S pseudo-Hermiticity becomes
  T^dag X T = X with X = sigma2 x K_S (the [P2] eq (37)/(38) shape at
  transfer grade); the crossed-region step is the both-modes evolution
  Wick-continued (same entire series, 1.4e-17); the channel space is
  irreducibly indefinite (64+64 with uniform |flux|). The doubling is
  the standard boundary-restriction move and adds exactly two Pauli
  slots; the one discretionary convention (Gamma = i sigma2 x I) is
  named, and the currents' existence does not depend on it (any
  doubling admitting a conserved current yields X = one-K_S-factor
  currents, by the bijection argument). Nothing positive-metric was
  smuggled: the only place positivity appears is |flux| normalization,
  which is K_S-even by construction.
- **Kramers guard (attack any positive -- here, attack the residue):**
  there is no K-c positive to attack; the guard instead certifies the
  two consistency obligations. (i) The mission's warning stands
  answered: no J-commuting Hermitian probe reads the sector anywhere in
  this swing; the K_S-linear class is carried entirely by
  J-ANTI-commuting currents, which is the non-quaternionic structure
  the no-go demands -- so had K-c fired, the consumer was already
  named. (ii) The V-symmetry is itself a Kramers-type degeneracy
  statement: V commutes with the dynamics and anticommutes with the
  grading, so odd readings come in cancelling pairs exactly as Kramers
  partners do -- the scattering extension REPRODUCES the no-go's
  structure at channel level rather than evading it. Verdict:
  consistent, and mutually reinforcing.
- **Experimental phenomenologist (is anything here measurable; zero
  overclaim):** what an experimenter could measure in the toy's world:
  transmission/reflection probabilities, lineshapes, delays -- all
  K_S-even, all sector-blind (transparency). What would read the
  sector: the SIGN of the conserved Krein current carried by a channel
  (is this channel a ghost or not, absolutely). Both mechanisms say the
  same operational thing: any detector calibration that could fix that
  sign is itself the external orientation datum -- calibrating against
  the dynamics is impossible (V-degeneracy), and calibrating against
  the symbol orientation is circular (parity transfer). So the honest
  experimental statement is: RELATIVE sector data (twist effects,
  interference minus signs) are measurable in principle; the ABSOLUTE
  bit is not, at this grade. No overclaim: this is a toy -- one window
  geometry, piecewise-constant symbols, matrix grade; "unmeasurable" is
  proven only for this class of models.
- **Adversarial referee (attack every asymmetry as a gauge artifact --
  and attack the negative too; answered in writing):** (i) Charge: the
  transparency theorem is trivial -- you built S without K_S, so of
  course it doesn't depend on K_S. Answer: what is nontrivial is that a
  K_S-free construction EXISTS that is complete scattering data (modes,
  channels, conservation, resonances) -- in the static theory the
  analogous statement is FALSE (the cut, and hence k_sigma, cannot be
  built K_S-free). The theorem's content is a difference between the
  static and dynamical categories, and the probe exhibits it, not
  assumes it. (ii) Charge: the choice of kinematic (rather than flux)
  in/out splitting smuggled the conclusion. Answer: the flux splitting
  is not available as an alternative -- flux signature is (64,64) on
  each kinematic mover space, so "in = positive flux" does not define a
  splitting at all; kinematic is the only construction, and it is
  K_S-free as a fact, not a choice. (iii) Charge: the V-symmetry is an
  artifact of the doubling convention. Answer: partially conceded and
  quantified -- V is exact because the family is Clifford-VECTOR
  (D = c(xi)); a Clifford-EVEN term (bivector/curvature-type, e.g. a
  connection term) ANTI-commutes with V (machine receipt) and would
  break Mechanism 1. This is the named operator-grade residue. But
  Mechanism 2 (parity transfer) does not use V and survives any family
  that stays odd-linear in the symbol; and the completeness bijection
  (every conserved current is K_S-linear) is convention-free. The
  negative rests on three legs; the referee breaks at most one, at a
  grade this swing does not reach. (iv) Charge: the per-channel graded
  transmissions (0.25-0.60) ARE the observable you claim doesn't exist.
  Answer: they flip under the orientation control (kappa-type xi sign
  move) with defect 3.4e-14 -- by the mission's own trichotomy rule,
  an asymmetry that moves under a control is a gauge artifact. This is
  precisely the pre-declared discipline doing its job on the most
  tempting candidate.

## 7. Typed claims

- Transparency theorem (S(E) identical under K_S -> -K_S; sector flip
  acts as (S, eps) -> (S, -eps)): **NATIVE-PROVEN (matrix grade, machine
  zero, five rays + gapped control).**
- Conserved-current completeness (every conserved current of the
  collar-Dirac transfer is K_S-linear; X -> K_S^-1 X bijection onto the
  family anticommutant): **NATIVE-DERIVED (paper grade, two-line proof;
  existence and non-conservation controls machine-checked).**
- Currents T-odd and non-quaternionic (J~-anticommuting):
  **NATIVE-PROVEN (machine-exact).**
- Ghost-conjugation mechanism (V = sigma2 x omega commutes with the
  dynamics, anticommutes with the currents; traced odd functionals
  vanish identically): **NATIVE-PROVEN (machine-exact, all sampled
  rays); scope limited to Clifford-vector families (named).**
- Parity transfer (T(-D) = W T W^-1; sector-parity =
  orientation-parity for all scattering functionals): **NATIVE-PROVEN
  (machine zero, all sampled rays).**
- "The payload bit is dynamically unreadable" as a program statement:
  **R0_COND working grade, toy scope** -- the theorems are unconditional
  on the toy; the extension to operator grade is the named open front.

## 8. Receipts

- Probe: `tests/channel-swings/smatrix_sector_face_probe.py` -- HEADLINE
  `12 [E] + 4 [F] = 16 (setup [T] = 3 excluded) ALL PASS`, exit 0,
  deterministic, numpy only, no new RNG draws.
- Machinery source: the m1 probe executed in-load (its 16 checks re-run,
  ALL PASS -- n2 sweep 132/53/0/15, both-modes normal form, walls s* =
  0.0585 / t* = 0.575 inherited); no existing file edited or re-run
  destructively.
- Anchors: window [0.295, 0.965] at s* + 0.4 on the conf-down ray, q
  ends 96.3/79.2, q_min -47.8; threshold 9.81, peak 1.582 at E = 12.41;
  flux |ev| 0.6486 uniform at 5.2e-15; per-channel graded content
  0.25-0.60 across rays.
- Construction discipline: GEOMETER-VS-PHYSICS-OBJECTS -- every object's
  construction named (Section 2 table); the one standard-physics fork
  (positive channel metric / flux-based in-out splitting) is
  UNAVAILABLE here, and its unavailability is itself a receipt
  (signature (64,64) on each mover space); killed items stay killed;
  C2 untouched (SRC-REJ-1 guard [F]).

## 9. Boundary

Exploration tier under the standing axiom; the three theorems are
unconditional algebra on the verified rep; the SECTOR reading of the
grading inherits R0_COND. Toy grade throughout: one window per ray,
piecewise-constant symbol family, matrix grade -- no operator on the
end, no L^2, no field-grade lift, no in/out Fock structure. NOT done,
named: (i) the operator-grade escape hatch -- Clifford-EVEN family
terms (connection/curvature-type) break the V-symmetry; whether a
faithful operator-grade collar family contains such terms, and whether
parity transfer alone then still closes the odd class, is the one place
a dynamical face could still hide; (ii) pole positions in the complex
plane were not hunted (PT-reality receipt only); (iii) the window
family spans rank 5 of 14 -- the completeness argument is span-free,
but a fuller-span window would tighten the anticommutant receipt;
(iv) wave-packet/two-arm interference protocols (twist-reading, not
value-reading -- Section 5) were argued, not simulated. Nothing here
moves claim status, canon verdicts, scorecard rows, N-accounting, or
public posture; the bit's VALUE remains externally posited (p2c-owned);
W172 and the m1 fork-conditional are untouched; no PP4 candidate packet
exists or is registered (K-c did not fire); no external actions; no
commits. Next rungs in order of exposure: (i) the operator-grade
V-breaking question (does the faithful collar connection add even-degree
terms, and what survives); (ii) state the "dynamical selection rule"
(transparency + parity transfer) as a single lemma alongside the Araki
selection rule; (iii) the two-arm twist interferometer as a named
computation (reads the character, not the value -- keep the distinction
honest in any future PP shaping).
