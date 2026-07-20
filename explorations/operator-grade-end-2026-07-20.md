---
title: "The operator-grade end family, built and answered on one construction (NRES = 64/128/256 refinement ladder, K-self-adjointness exact): Q-A fired A3-by-the-letter -- the uniform-norm boundary value of M_op (q_op + i delta)^{-1/2} DIVERGES at the wall (ceiling ~ N^1.35, the named mode) while the NORM-RESOLVENT mode is delta-Cauchy at every resolution with rate ~ delta^1.0 and deck-oddness is machine-EXACT by pointwise algebra (A2 structurally excluded for this lift; N-uniformity of the resolvent mode left open); Q-B fired B-GAUGE -- J_op and parity transfer lift exactly, the only separator is Im k_op = the J_op-image, the classification stays Z/2; Q-C fired C-BLIND STRENGTHENED TWICE -- the V-crack opens (honest Clifford-even dressing, forced T-odd by the J-real generator census) and blindness survives via the ghost-Kramers conjugation S_VJ = (sigma2 x omega J_quat) o conj, and beyond ALL named symmetries via an exact spectral-pairing identity of graded scattering (V was sufficient, never necessary); no PP4 candidate"
channel: big swing (Joe direct chat, 2026-07-20: summit wave, operator-grade end family)
directed_by: "Joe direct chat, 2026-07-20 (summit wave: operator-grade end family)"
claim: none
canon: none
posture: none
status: COMPLETE. Section 0 (outcome branches) was written to this file
  BEFORE any computation ran and is unedited; results sections were
  appended as stages completed. Probes ALL PASS, exit 0 (9 + 4 + 15
  checks).
probes:
  - tests/channel-swings/operator_grade_end_probe.py   (Q-A, Q-B)
  - tests/channel-swings/operator_grade_face_probe.py  (Q-C, if split is cleaner)
consumes:
  - explorations/sector-relative-section-theory-2026-07-20.md (Section 7 gap spec)
  - explorations/m1-third-reading-2026-07-20.md (universal-null, orientation gauge)
  - explorations/smatrix-sector-face-2026-07-20.md (blindness mechanisms + the crack)
  - explorations/n2-end-family-2026-07-20.md (the faithful end model)
  - tests/rs_bicomplex_spin95_connection_2form.py (honest Clifford-even source)
---

# Operator-grade end family: pre-declared outcome conditions

Written BEFORE computing (Stage 0). Every operator-grade claim below the
line must carry a convergence column (value at each N in {64,128,256} +
extrapolation + rate); a single-N number is not a result. Consistency
bars, standing: the universal-null lemma, the selection rule (only
K_S-linear pairings read the sector), the Kramers no-go -- a violation of
any of these is an error in the build, not a discovery, until proven
otherwise at refinement-ladder grade.

## Section 0. Pre-declared outcome branches

**Q-A (the section theorem at operator grade).** Object: N_delta,op =
M_op (q_op + i delta)^{-1/2} on the discretized collar, minimal
configuration first (one gapped ray, one crossing ray containing its
wall), delta-ladder x N-ladder; convergence measured in three modes --
(i) plain operator norm, (ii) norm-resolvent at fixed z off the real
axis, (iii) graph-relative norm ||(N_d - N_d') (D_op - z0)^{-1}||.
- **A1 (converges deck-odd):** some named mode converges N-uniformly as
  delta -> 0 on the wall-containing collar AND the limit is deck-odd
  (defect -> 0 through the ladder). The open theorem is corroborated at
  discretized grade; name the mode and the rate.
- **A2 (converges, deck-oddness fails):** a mode converges but the deck
  defect does not vanish through the ladder. The section theorem's
  candidate definition needs a different deck statement; major structural
  finding.
- **A3 (diverges, named mode):** no mode converges N-uniformly; the
  divergence rate in delta (and its N-scaling) is measured and named.
  The theorem needs modification (e.g., a different regularization or a
  domain excision at the wall); the named rate is the deliverable.
All three are wins if precisely characterized. Expected on the gapped
ray: trivial convergence in every mode (control). The question lives on
the crossing collar.

**Q-B (the orientation bit at operator grade).** The two prescriptions
(q_op + i delta)^{-1/2} vs (q_op - i delta)^{-1/2}.
- **B-GAUGE:** the matrix-grade intertwiners lift: J_op maps the +i0
  family to the -i0 family (defect -> 0 through the ladder), W_OM parity
  transfer survives the collar term, and NO conserved K_S-derivable
  reading of the operator family separates the prescriptions (all
  candidate separators either vanish, are gauge-movable, or fail
  conservation). The bit stays scheme; classification stays Z/2.
- **B-DATA:** a conserved, K_S-derivable, gauge-immovable reading
  separates +i0 from -i0 at refinement-ladder grade (survives the ladder
  with a nonzero extrapolant). The classification doubles to Z/2 x Z/2
  and a dynamical sign enters (W172/H59 anti-damping sign becomes
  physical). Major finding; typed fork-conditional, not canon.
- **B-UNDECIDED:** the candidate separator exists but its ladder
  behavior is inconclusive (no stable extrapolant); named as such.

**Q-C (the V-breaking crack).** Add the honest Clifford-even term
i kappa sigma1 x sigma_c(W) (K_S-self-adjointness preserving; W an
a-priori named connection in the bicomplex fixture's sense -- never read
from xi) to the scattering family and re-run the blindness battery.
- **C-BLIND:** V breaks as predicted (the anticommutation is machine-
  exact) but every traced sector-odd functional remains zero or
  gauge-movable: the surviving mechanisms (parity transfer if it
  survives, current-consumer structure, Kramers) keep the bit blind even
  with curvature. The blindness theorem EXTENDS; the crack closes.
- **C-FACE:** a sector-odd scattering functional appears (nonzero
  through the kappa-ladder and the N/window controls), flips with the
  sector, and is NOT movable by the orientation conjugator W_OM, channel
  gauge, same-sign-plane transport, or frame dressing. The dynamical
  face reopens. Then and only then: check prediction-package admission
  criteria and write explorations/pp4-candidate-operator-face-2026-07-20.md
  as CANDIDATE (unregistered; no self-registration).
- **C-ARTIFACT:** an odd functional appears but fails a control
  (trichotomy, gauge move, or ladder); named as the artifact it is.

Predictions (honest, falsifiable, written now): A1 with mode =
graph-relative and/or norm-resolvent, plain-norm divergence at the wall
at rate delta^{-1/2} (the named non-uniform mode); B-GAUGE (the
intertwiners are pointwise and should commute with the collar term);
Q-C genuinely open -- mechanism 2's parity transfer uses OM, which
COMMUTES with bivectors instead of anticommuting, so BOTH named
mechanisms break and the outcome turns on the current-consumer
structure alone.

RESULTS SECTIONS APPENDED BELOW AS STAGES COMPLETE.

## Section 1. The build (what was actually constructed)

One discretized L^2-grade collar operator, honest by construction:

    G_col = sigma2 x I_128     (collar Clifford element; Hermitian, squares
                                to I, anticommutes with every doubled
                                tangent generator sigma1 x e_a -- exact)
    D_op  = P_N x G_col + blkdiag_j(sigma1 x c(xi(t, s_j)))
    P_N   = -i d/ds            (central difference, Dirichlet; Hermitian)
    K_op  = I_N x I_2 x K_S    (the K_S structure lifted pointwise)

K_op D_op K_op = D_op^dag holds machine-exactly at every resolution (the
discretization does not damage K-self-adjointness). Section objects are
lifted pointwise as multiplication operators -- Ku_op = blkdiag(I_2 x
Ku(s_j)), q_op = blkdiag(q(s_j) I) -- and the candidate section family is
N_delta,op = M_op (q_op + i delta)^{-1/2}, M_op = Ku_op D_op, exactly the
regularization Section 7 of the section-theory doc named for the lift.

Minimal configuration (a named geometric choice, not a tuning): the
conf-down ray crosses first at s* = 0.0585 (t* = 0.575), too close to
the collar base for an interior-wall window; the operator work uses the
loop coordinate whose wall sits nearest 0.6 -- t_op = 0.4100, s*_op =
0.5694, dq/ds|wall = -24.12, window s in [0.1694, 0.9694], q running
8.13 -> -18.10 with a single sign change. Gapped control: the conf-up
ray at the same t_op, s in [0, 1.2], min q = 12.14. Refinement ladder
NRES in {64, 128, 256}; delta-ladder {1, 0.3, 0.1, 0.03, 0.01, 0.003,
0.001}; three convergence modes per (ray, NRES): plain operator norm,
norm-resolvent at z = 2i (block-Thomas LU -- splu's fill on these
dense-block tridiagonals is catastrophic; the structure-honest solver is
part of the numerical-analyst receipt), and graph-relative norm
||(N_d - N_d')(D_op - 2i)^{-1}||. Norms by deterministic power iteration
(~1 percent, sufficient for rate columns; svds stalls on the clustered
spectra -- named numerical decision, cross-checked against svds values
at NRES = 64).

Truncations, named: one loop coordinate per collar (t enters as a
parameter, not a second operator direction); Dirichlet ends; the
Weyl-slice ray family of n2; delta and NRES ladders finite. No claim
depends on a single-N number.

## Section 2. Q-A answered: A3 by the pre-declared letter -- convergence mode identified (norm-resolvent), divergence mode named (sup-mode wall blow-up), deck-oddness exact

Run receipt: operator_grade_end_probe.py -- ALL PASS (9 checks), exit 0,
1547 s. Pre-declared branch fired: **A3** (converges per-resolution in
the resolvent sense; the pre-set N-uniformity bar failed). Both A1 and
A3 were declared wins if precisely characterized; here is the precise
characterization, convergence columns in full.

**Gapped control (trivial regime, as predicted):** delta-Cauchy in plain
AND graph-relative norm at every resolution, fitted rate 1.01 at NRES =
64/128/256, graph-relative N-stable to 3 percent (3.06e-5 / 3.15e-5 /
3.20e-5 at the smallest pair). The boundary value exists off the wall in
every mode.

**Crossing collar (the question), three modes, full ladder:**

- **Plain (sup) mode -- the NAMED DIVERGENCE MODE.** ||N_delta,op||
  saturates to an N-growing ceiling: 204.1 / 505.0 / 1321.0 at NRES =
  64/128/256 (growth ~ N^1.35); successive-delta differences at the
  smallest pair GROW with N (1.29 / 6.33 / 32.8) and the fitted
  delta-slope decays with N (0.70 / 0.54 / 0.35). The uniform-norm
  boundary value does NOT exist at operator grade: the wall's Jordan
  nilpotent normalization is an unbounded sup-mode obstruction. This is
  the operator-grade shadow of the symbol-grade fact that N_delta blows
  up AT the wall point while converging off it.
- **Graph-relative mode (z = 2+2i):** converges at every fixed
  resolution but with the same non-uniform N-shape as the plain mode
  (last-pair 0.84 / 2.65 / 11.3). Relative bounds against D_op do not
  tame the wall.
- **Norm-resolvent mode (z = 2i) -- the SURVIVING CANDIDATE TOPOLOGY.**
  Resolvent differences are delta-Cauchy at EVERY resolution with
  stable fitted rate ~ delta^1.0 (slopes 1.04 / 0.96 / 1.08), matched
  smallest-pair values 0.0066 / 0.0357 / 0.0099 -- bounded, NON-MONOTONE
  in N (the 256 value drops back below the 128 value). The pre-set
  uniformity bar (factor 4 across the ladder) failed at factor 5.4
  through this non-monotone wobble -- which tracks grid-wall alignment
  (min_j |q_j| depends on where the grid lands relative to s*), not a
  divergence trend. Honest statement: the norm-resolvent boundary value
  is the only mode that survives the ladder; its N-uniformity is left
  OPEN at this grade (a finer ladder with wall-aligned grids is the
  named next instrument). The coded verdict A3 stands as printed; the
  structural reading is "A1-shaped, uniformity unproven."

**Deck-oddness at operator grade: EXACT, not asymptotic.** U_h
N_delta,op(t) U_h^{-1} = -N_delta,op(t+1) at 4.8e-13 / 5.7e-13 / 2.7e-12
across the ladder (and on all 6 stage-4 rays). Reason, proved by the
build: deck covariance is pointwise-exact for D and Ku, q is
deck-invariant, and the collar derivative term commutes with the lifted
deck -- so the operator-grade deck statement is inherited by algebra,
not established by a limit. A2 is structurally excluded for THIS lift:
any deck-oddness failure would have to come from a different choice of
operator lift, not from refinement.

**Consequence for the N2 theorem (Section 7 of the section-theory doc,
updated):** the candidate definition should be stated in the
norm-resolvent topology from the start; the sup-mode divergence at rate
~ N^1.35 is the quantitative form of "no off-the-shelf result covers
this"; and the deck clause is a free consequence of pointwise
covariance, needing no analytic work.

## Section 3. Q-B answered: B-GAUGE (the classification stays Z/2)

Pre-declared branch fired: **B-GAUGE**, at machine precision on every
leg, at every resolution:

1. **The intertwiner lifts.** J_op = (I x J_quat) o conj commutes with
   the FULL collar operator (derivative term included; defect 0.0) and
   maps the +i0 family onto the -i0 family exactly (3.7e-17). W172/H59
   tie: the anti-damping orientation remains exchanged by an exact
   antiunitary symmetry of the dynamics at operator grade.
2. **Parity transfer lifts, and the section datum is xi-even.** W = I x
   omega carries D_op(xi) to D_op(-xi) exactly (collar term invariant),
   and M(-xi) = M(xi) pointwise (0.0) -- the orientation flip cannot be
   absorbed into the section datum; the only exchanger of the
   prescriptions among lifted symmetries is the antiunitary J_op.
3. **The separator battery.** The conserved K_S-derivable reading k_op
   (sigma1 x K_S channel against the derived A-density, the operator
   lift of the f5/section reading) has Re k IDENTICAL between
   prescriptions and Im k EXACTLY conjugate-flipped at NRES = 64/128/256
   (defects 0.0) -- the difference between the two prescriptions is
   precisely the J_op-image of the family. The flat I2 x K_S channel is
   trace-blind (0.0), the selection rule's operator-grade echo; a small
   free theorem fell out: the collar derivative term drops out of every
   pointwise-lifted K_S-linear trace reading (its blocks are
   sigma-off-diagonal).

No conserved, K_S-derivable, gauge-immovable reading separates +i0 from
-i0: the orientation bit is SCHEME at operator grade, the classification
stays **Z/2**, and the K-d shadow of the section theory does not fire.
(The doubling caveat stands: B-DATA remains conceivable only through
structures NOT derivable from {D_op, K_op} -- exactly the external-posit
typing the program already carries for the central bit.)

## Section 4. Stage-4 sampled corroboration (~6 rays)

Run receipt: OPGRADE_STAGE4=1 operator_grade_end_probe.py -- ALL PASS
(4 checks), exit 0, headline CORROBORATED. Fresh NAMED seeded stream
(default_rng(20260720), independent draws -- ray-class statistics
corroborate n2's census shape; not the identical 53 rays): 3 crossing
rays with interior walls + 2 gapped rays + the boost ray (gapped class
at its sampled window), 15 draws needed. On EVERY ray at NRES in
{64, 128}: the graph-relative mode (z = 2+2i) converges with fitted
delta-slope 0.96-1.00; gapped rays are N-stable to 0.00-0.01 relative;
crossing rays' graph columns converge at every resolution (N-spread up
to 0.75 at the smallest pair -- the same bounded-but-slower uniformity
the minimal configuration shows); operator-grade deck-oddness is
machine-exact on every ray (worst 5.4e-14). The minimal-configuration
mode structure is generic on the end, not a ray accident.

## Section 5. Q-C answered: C-BLIND, strengthened twice over

Probe: tests/channel-swings/operator_grade_face_probe.py -- ALL PASS,
15 checks, exit 0. Pre-declared branch fired: **C-BLIND** (with two
structural discoveries the branch statement did not anticipate). No PP4
candidate file is written; admission was not reached.

**The crack opens exactly as predicted -- and it does not matter.** The
honest Clifford-even dressing (bicomplex-fixture Sigma_ab carrier, named
a-priori W = 1.0 Sigma_09 + 0.7 Sigma_12, never read from xi) enters the
symbol channel as i kappa B: the i is FORCED by K_S-self-adjointness,
and sigma1 x iB anticommutes with V = sigma2 x omega machine-exactly --
mechanism 1 is broken, as the smatrix doc's one named crack predicted.
The conserved current X1 = sigma2 x K_S survives the dressing exactly.
And yet: every traced (ungraded-prepared) sector-odd functional remains
an exact zero (worst 1.2e-13) at every kappa in {0.05, 0.1, 0.2}, every
segmentation nseg in {24, 48, 96}, and a second scattering energy, while
per-channel graded entries are O(0.5).

**Discovery 1 -- the ghost-Kramers conjugation.** All 91 so(9,5)
generators are J_quat-REAL, so the forced i makes every honest even
symbol dressing J-ODD: opening the V-crack costs explicit T-violation,
and the T-invariant placement of the same connection (covariant
derivative, no i) is exactly the V-COMMUTING one -- the two ways in are
mutually exclusive by algebra. The named surviving symmetry at
connection grade is the product S_VJ = (sigma2 x omega J_quat) o conj:
V and J each flip the even term and the flips cancel; S_VJ is an exact
antiunitary symmetry of EVERY K_S-honest vector+even family (defect 0.0,
universality witnessed on an unrelated symbol), fixes X1 and Gamma, and
exchanges right- with left-movers. Its algebraic boundary is real:
K-honesty forces the i on grade-3 (torsion-type) terms too, which are
V-commuting and J-odd -- a torsion term breaks S_VJ by its full size.
Side finding: the dressing kills the second current (X2 = i I x K_S
omega loses conservation, defect 0.1) -- curvature collapses the
conserved K_S-linear current pair to {X1} alone.

**Discovery 2 -- the deep-blindness identity (the stage's strongest
result).** Escalation: with grade-2 AND grade-3 dressing together, V,
J_quat, and S_VJ are ALL broken -- traced odd functionals still vanish
(5.6e-14). Generic deterministic K-honest family with no end-model
structure: still zero (6.5e-15). Family that breaks X1-CONSERVATION
itself (defect 0.4): still zero (5.2e-14) -- while per-channel readings
stay O(0.5) and non-grading-weighted traces are O(1). The zero is an
exact identity of the graded scattering construction: Q = t^dag E_R t
has an exactly +/- paired spectrum, annihilated by a Hermitian
involution sig (extracted numerically: sig Q sig = -Q at 1e-15,
approximately anticommuting with the incident grading, {sig, E_Lp} ~
6e-3). Consequence for the record: **mechanism 1 (V) was sufficient but
never necessary** -- the smatrix doc's attribution stands as algebra but
is not the load-bearing protection. Identifying sig with a named
channel-algebra element is the sharpest new open object of the blindness
theory. Consistency bars: no violation -- this strengthens the selection
rule's operational content (the sector bit remains dynamically unread).

## Section 6. Council pass (inline, five lenses)

- **Functional analyst (norm-resolvent honesty):** the question was
  posed in the norm-resolvent topology and the answer respects it: the
  sup-mode divergence (~ N^1.35 ceiling) is exactly what an unbounded
  first-order operator times a wall-singular scalar must do, and proves
  nothing against the section theorem; the resolvent-difference columns
  are the honest object, and they are delta-Cauchy with a stable rate
  at every resolution. What is NOT yet earned: an N-uniform bound. The
  non-monotone wobble (0.0066/0.0357/0.0099) is consistent with a
  bounded limit whose constant depends on grid-wall alignment, and
  equally consistent with a slow logarithmic growth sampled at three
  points. The doc says "open" and the probe printed A3; both are
  correct. One more honesty note: z = 2i is a single resolvent point;
  a theorem needs the boundary value on a z-region -- ladder evidence
  at one z is a candidate, not a domain.
- **Spectral geometer:** the deck receipt is the important structural
  one: deck-oddness at operator grade is ALGEBRA (pointwise covariance
  + collar-term deck-invariance), so the Z/2 classifying data of the
  section theory lifts untouched whenever the lift exists at all --
  the analytic and topological halves of the N2 theorem cleanly
  decouple. The A2 branch is thereby structurally empty FOR THIS LIFT,
  which sharpens what a future counterexample would have to attack:
  the lift choice, not the limit.
- **Krein analyst:** Q-B's three machine-zeros are the operator-grade
  completion of the m1 orientation story: the two prescriptions are
  exchanged by an exact antiunitary symmetry of the FULL dynamics
  (derivative included), the section datum is xi-even, and the unique
  K_S-linear separator is the J_op-image. Within everything derivable
  from {D_op, K_op}, the bit is scheme; Z/2 stands. The known caveat is
  unchanged in location: only a structure external to the family could
  ever make it data -- which is the program's standing external-posit
  typing of the central bit, now corroborated one grade higher.
- **Numerical analyst (refinement-scaling discipline, load-bearing):**
  every claim above carries a ladder column; no single-N number is
  load-bearing anywhere. Named numerical decisions, all in the probe
  text: power-iteration norms (~1 percent, cross-checked against svds
  at NRES = 64: 14.6467 vs 14.65), block-Thomas LU replacing splu
  (residuals 1e-12; splu's fill on dense-block tridiagonals was the
  cost wall), the z = 2+2i graph regularizer after the FIRST choice
  z = 2i was caught resonating with the crossed sector's imaginary
  spectrum (dgraph 218 > dplain 61 at NRES = 64 was the tell -- a
  measurement-apparatus artifact found and named, not silently kept),
  Dirichlet ends, and the deep-wall window choice (wall interior,
  dq/ds = -24.1). Known residual: the delta-ladder's smallest rungs at
  NRES = 256 sit below the grid's own wall resolution (q'h ~ 0.075),
  so the sup-mode ceilings are grid-limited by construction -- that is
  the point of reporting them AS the divergence mode.
- **Adversarial referee (every operator-grade claim attacked as a
  discretization artifact; answered in writing):**
  (1) *"The resolvent-mode convergence is just delta-smoothing at fixed
  N."* Answer: at fixed N everything converges trivially once delta <<
  min|q_j|; the receipt is that the fitted rate is stable (~1.0) at all
  three N INCLUDING the regime where delta spans min|q_j|, and the
  matched-pair values do not grow monotonically -- that is not a
  fixed-N triviality, though it is also not yet uniformity; the doc
  claims exactly the middle.
  (2) *"Deck-oddness at 1e-12 is roundoff luck."* Answer: it is an
  algebraic identity of the build (proved in Section 2 of the doc by
  the commutation argument), verified at three resolutions and six
  rays; there is no limit being taken.
  (3) *"The Q-C zeros are your channel construction, not physics."*
  Answer: partially SUSTAINED, and that is Discovery 2: the zeros
  survive breaking every symmetry INCLUDING X1-conservation, so they
  are an identity of the graded scattering construction itself
  (spectral pairing receipt at 1e-15) -- which is why the doc
  reattributes the blindness from mechanism 1 to the unnamed pairing
  identity and marks naming sig as the open object. What the referee
  does NOT get: per-channel entries are O(0.5), non-grading weights
  read O(1), and the even battery is fully alive -- the construction
  is not degenerate; the zero is specific to the graded trace class.
  (4) *"The stage-4 rays are cherry-picked."* Answer: fresh seeded
  stream, seed and draw rule printed, first-found configs accepted by
  pre-stated geometric admission (interior wall), 15 draws, no
  discards beyond the admission rule.

## Section 7. Typed outcomes, receipts, boundary

Outcomes against Section 0 (pre-declared): **Q-A = A3** (probe-printed;
convergence mode = norm-resolvent, rate ~ delta^1.0 per N; divergence
mode = sup-norm, ceiling ~ N^1.35; deck-odd EXACT; resolvent-mode
N-uniformity OPEN). **Q-B = B-GAUGE** (all receipts machine-zero;
Z/2 stands; K-d shadow not fired). **Q-C = C-BLIND** (strengthened:
S_VJ at connection grade; the spectral-pairing identity beyond it; two
structural discoveries -- forced T-parity of honest even dressings, and
current-pair collapse to {X1}). No PP4 candidate file; admission not
reached (no in-principle observable appeared).

Receipts (all deterministic, numpy/scipy only, no new RNG in the end
probe; stage 4's fresh stream named):
- tests/channel-swings/operator_grade_end_probe.py -- ALL PASS, 9
  checks, exit 0 (Q-A + Q-B + adjudication; HEADLINE printed).
- OPGRADE_STAGE4=1 ... operator_grade_end_probe.py -- ALL PASS, 4
  checks, exit 0 (6-ray corroboration; HEADLINE printed).
- tests/channel-swings/operator_grade_face_probe.py -- ALL PASS, 15
  checks, exit 0 (Q-C; HEADLINE printed).

Boundary (what this swing does NOT establish): no N-uniform resolvent
bound (the A1 gate, the one analytic estimate the N2 theorem still
needs); one resolvent point z = 2i, not a domain; one loop coordinate
per collar (t parametric); Dirichlet ends; the pairing involution sig
unnamed; P = 0 stratum untouched; no K-group computed; no claim, canon,
scorecard, or posture movement anywhere in this doc.
