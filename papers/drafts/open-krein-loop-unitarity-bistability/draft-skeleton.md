# Open-System Bistability of Total Unitarity in Keep-and-Grade Higher-Derivative Field Theory

**DRAFT skeleton, 2026-07-14. GU-INDEPENDENT: the results are about the class of fourth-order (Stelle-type)
gravities and indefinite-metric (Krein / PT-symmetric) keep-and-grade quantization generally; Geometric
Unity is at most one member of the class and is not required anywhere below. External publication and
candidate promotion are Joe-gated. Every quantitative claim ties to a reproducible test; see
`VERIFICATION.md`.**

## Abstract

Fourth-order (Stelle) gravity is renormalizable and asymptotically free but propagates a massive spin-2
ghost. The keep-and-grade program keeps the ghost and grades the state space with an indefinite (Krein)
metric so that a positive physical inner product and a unitary S-matrix are recovered; it is established at
tree level and its loop-level fate decides an entire class of theories. We study the loop question for the
theory coupled to an EXTERNAL SOURCE, i.e. as an OPEN system across a boundary, and report the following.
(1) A physical-subspace unitarity defect A^dag A = P+ + B^dag B holds exactly for any pseudo-unitary S,
with a definite (excess, anti-damping) sign that refutes a dissipative decay-width reading. (2) Once the
theory is open, a physical-sheet pole of the REDUCED (Feshbach) ghost resolvent is a different object from
a complex eigenvalue of the TOTAL generator: in a finite Friedrichs / Fano-Anderson model there is a
like-Krein-signed regime with the reduced physical-sheet pole present WHILE the total spectrum is real at
all couplings and a positive total metric exists (total unitary), so the closed-theory inference
"physical-sheet pole implies non-unitary" fails for an open Krein theory. (3) In the opposite-Krein-signed
regime the total generator develops a complex-conjugate pair above an exceptional point, and is genuinely
non-unitary. (4) Closing a self-consistency in which the source coupling is large only when the physical
metric is operative yields a BISTABLE fixed point: an operative fixed point that exists and is stable, is
non-vacuous (a fixed opposite-sign kinematic coupling genuinely spoils it below a critical source
coupling), alongside an equally self-consistent pathological fixed point; self-consistency does not select.
Basin selection reduces to the reservoir Krein signature, equivalently a coupling ratio versus an O(1)
threshold. **The bistable fixed point and its selection are established in a finite model only; whether a
generic Stelle-class theory coupled to a physical reservoir realizes this structure, and which basin it
selects, is not settled here.** We state the result at its honest grade: a reframe plus a non-vacuous
existence result, not a proof of loop unitarity.

## 1. Introduction (skeleton)

- The higher-derivative ghost and the keep-and-grade rescue; tree-level status; the loop question as the
  decider for Stelle gravity, conformal gravity, agravity.
- The move this draft makes: the theory is coupled to an external source, so the physically relevant object
  is an OPEN system, and closed-theory loop-unitarity verdicts (physical-sheet pole implies non-unitary)
  are re-examined in that light.
- Statement of scope: class-level, GU-free; a reframe and an existence result, explicitly not a proof of
  unitarity.

## 2. Setup (class-level, GU-free)

- Krein space H, fundamental symmetry eta = P+ - P- .
- Stelle-class operator D, propagator 1/(p^2(p^2-M^2)) = (1/M^2)(1/p^2 - 1/(p^2-M^2)); the second pole is
  the wrong-sign (ghost) residue; keep-and-grade makes the ghost a real-mass negative-Krein-norm mode.
- Coupling to an external source via a source action linear in an external connection/current, making the
  field an open sub-system of H_tot = H_sys (+) H_res with coupling V across a boundary.
- Definitions. "Operative": there exists a positive total metric eta_+ = eta_tot C_tot > 0 under which the
  total generator is pseudo-Hermitian and the total evolution is eta_+-unitary (equivalently the total
  spectrum is real). "Reservoir Krein type": the sign of the reservoir sector the ghost couples into,
  relative to the ghost.

## 3. The theorems, with grades

**Theorem 1 (physical-subspace unitarity defect).** For eta-pseudo-unitary S, with A = P+ S P+ and
B = P- S P+, A^dag A = P+ + B^dag B; hence physical-channel probability sums to 1 + ||B|i>||^2 >= 1,
equality iff B|i> = 0; the defect is sign-definite (excess / anti-damping). GRADE: THEOREM (two lines;
machine-checked). NOVELTY: KNOWN-in-substance (Lee-Wick / CLOP physical-subspace unitarity), NEW-form.

**Theorem 2 (reduced pole is not the total eigenvalue).** In the finite Friedrichs / Fano-Anderson model a
like-Krein-signed regime exists in which the reduced ghost resolvent carries an anti-damping physical-sheet
pole (argument principle: 1 vs 0 for the normal control) WHILE the total spectrum is real at every coupling
and a positive total metric exists (total unitary to 1e-15). GRADE: THEOREM in the finite model; STRUCTURAL
for the QFT lift. NOVELTY: KNOWN principle (Feshbach), NEW-application.

**Theorem 3 (Krein exceptional-point obstruction).** In the opposite-Krein-signed regime, opposite-type
eigenvalues collide and the total generator develops a complex-conjugate pair above an exceptional point
g_c > 0 (bisection); no positive total metric; genuinely non-unitary. GRADE: THEOREM in the finite model.
NOVELTY: KNOWN (Bognar), NEW-application. COROLLARY (2+3): total operativity is conditional on the
reservoir Krein type.

**Theorem 4 (bistable fixed point).** With kappa(m) = kappa_max * m (m the operativity order parameter) and
a fixed metric-independent opposite-sign kinematic coupling g_kin: (a) NON-VACUITY, a critical
kappa*(g_kin) > 0 below which the total is complex and above which real; (b) BISTABILITY, both m=1 and m=0
are self-consistent fixed points; (c) STABILITY, both return under perturbation; (d) BOOTSTRAP, at m=1 the
total spectrum is real, a positive total metric exists, the total is unitary while the sub-system gains.
GRADE: TOY-MODEL (finite stand-in; exact within the toy). NOVELTY: NEW-COMBINATION (feedback-driven
bistable selection of total unitarity in a Krein open system); ingredients KNOWN.

**Theorem 5 (selection reduces to a coupling ratio).** Basin selection is set by kappa_max/g_kin versus
r* ~ O(1); self-consistency alone decides nothing. GRADE: TOY / STRUCTURAL.

**Proposition 6 (fade dynamical selection).** A decaying coupling (everpresent ~ 1/sqrt(N)) that also
shrinks g_kin can dynamically select the operative basin, through a finite-N non-unitary window. GRADE:
PLAUSIBLE-ONLY (ported, debit-carrying).

**Supporting (context, not the paper's novelty).** No-local-positive-metric theorem (every keep-and-grade
positive metric is non-local, kernel decaying at the ghost scale); perturbative C-operator existence below
the two-body decay threshold (conditional on PT-unbroken / sub-threshold); the interacting-C essential
spectrum via analytic Fredholm; the graded CLOP / family map.

## 4. Toy-vs-general hardening (what must be done, and why the honest grade is what it is)

The novel theorem-grade content (Theorems 4, 5, Proposition 6) lives ENTIRELY in a finite Friedrichs /
Fano-Anderson stand-in. It decides STRUCTURE (the loop question is a genuine bistable fixed point; the
operative fixed point exists and is stable and non-vacuous) and it CANNOT fix which basin a real theory
realizes. To become a class-level result it needs either:

1. a GENERIC-CAPTURE LEMMA: a generic Stelle-class operator coupled to a physically reasonable external
   reservoir realizes the Theorem 4 structure (the finite model is representative, not a rig); or
2. a real DRESSED COMPUTATION for an actual reservoir, computing the coupling ratio r* and hence the basin.

Until one is in hand, Theorems 4-5 and Proposition 6 are toy observations, and the paper's defensible claim
is the reframe (Theorems 1-3) plus the non-vacuous existence result.

## 5. Prior-art delineation (full statement in explorations/W188-class-paper-assessment-2026-07-14.md)

- **Lee-Wick (Grinstein-O'Connell-Wise) / CLOP / fakeon (Anselmi-Piva).** The removal family; Theorem 1 is
  their physical-subspace unitarity defect re-read with a definite sign in the KEEP branch. The draft
  characterizes the keep branch and does not compete with the removal prescriptions.
- **Bender-Mannheim (PT-symmetric QFT, C-operator, Pais-Uhlenbeck no-ghost theorem).** The closed
  operative-vs-not dichotomy (unequal-frequency operative, equal-frequency Jordan block) is theirs;
  Theorems 4-5 are its OPEN-system extension, with the reservoir Krein type as the new selection axis.
- **Mostafazadeh (pseudo-Hermitian QM).** The positive metric eta_+ and quasi-Hermiticity machinery are
  his; applied here to the TOTAL space.
- **Bognar (Krein spaces).** The opposite-type collision producing complex pairs (Theorem 3) is standard
  Krein-space spectral theory.
- **Fano-Anderson / Friedrichs / Feshbach open-system machinery.** The discrete-plus-continuum model and
  the reduced non-Hermitian effective Hamiltonian are textbook; the NEW move is that the total lives on a
  Krein space, so total unitarity is not automatic and is bistable.
- **Driven-dissipative / non-Hermitian open-system bistability and exceptional points.** Bistability and
  exceptional points in open non-Hermitian systems are established; the delta here is that the bistable
  order parameter is the OPERATIVITY OF THE TOTAL METRIC with a self-consistent feedback, not a physical
  observable. This delta must be stated explicitly and the closest analogues cited.
- **Turok-Bateman (ghost-parity clearing).** Tree-level; not in competition with the loop question.

## 6. Honest open items (lead with these)

- No proof that any real Stelle-class theory coupled to a physical reservoir realizes the bistable
  structure or selects the operative basin: the pieces are the generic-capture lemma / dressed computation
  of Section 4.
- The physically-anchored kinematic coupling (ghost above the two-body threshold, opposite sign) is the
  DEFAULT and gives the pathological basin; the operative basin requires the source coupling to dominate by
  an unbuilt O(1) factor.
- The operative TOTAL metric is non-local (inherits the no-local-positive-metric price relocated to the
  total space); total unitarity carries that cost and must not be oversold.
- Proposition 6 (fade) is plausible-only and passes through a finite-N non-unitary window; it must not
  carry weight in the abstract or the theorems.
- The QFT lift of Theorems 2-3 is structural; a genuine field-theoretic model would raise it.

## 7. What this draft does NOT claim

- It does not prove loop unitarity of any higher-derivative theory.
- It does not overturn the closed-theory / removal-family results; it characterizes the open keep-and-grade
  branch and clarifies which closed-theory inferences fail once the theory is opened.
- It asserts no GU-specific content; GU is at most one member of the class and is not required.

*Draft skeleton filed 2026-07-14. Honest grade SOLID-INCREMENTAL. Drafts only; candidate promotion and
external publication Joe-gated.*
</content>
