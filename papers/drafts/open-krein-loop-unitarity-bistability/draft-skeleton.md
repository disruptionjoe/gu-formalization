# Open-System Bistability of Total Unitarity in Keep-and-Grade Higher-Derivative Field Theory

**DRAFT skeleton, 2026-07-14 (hardened HQW-KREIN 2026-07-14). GU-INDEPENDENT: the results are about the
class of fourth-order (Stelle-type) gravities and indefinite-metric (Krein / PT-symmetric) keep-and-grade
quantization generally; Geometric Unity is at most one member of the class and is not required anywhere
below. External publication and candidate promotion are Joe-gated. Every quantitative claim ties to a
reproducible test; see `VERIFICATION.md`.**

## Abstract

The one genuinely new and referee-creditable point is a clarification. For a higher-derivative
(Stelle-class) Krein / PT-symmetric keep-and-grade theory coupled to an EXTERNAL SOURCE, i.e. read as an
OPEN system across a boundary, a physical-sheet pole of the REDUCED (Feshbach) ghost resolvent is a
different object from a complex eigenvalue of the TOTAL generator. In a finite Friedrichs / Fano-Anderson
model there is a like-Krein-signed regime with the reduced physical-sheet pole present WHILE the total
spectrum is real at all couplings and a positive total metric exists (total unitary to 1e-15), so the
closed-theory inference "physical-sheet pole implies non-unitary" fails for an open Krein theory. This
reduced-pole-versus-total-eigenvalue separation is the load-bearing contribution.

Around that clarification the draft records three further finite-model results. (i) A physical-subspace
unitarity defect A^dag A = P+ + B^dag B holds exactly for any pseudo-unitary S, with a definite (excess,
anti-damping) sign that refutes a dissipative decay-width reading. (ii) In the opposite-Krein-signed regime
the total generator develops a complex-conjugate pair above an exceptional point and is genuinely
non-unitary, so total operativity is CONDITIONAL on the reservoir Krein signature. (iii) Closing a
self-consistency in which the source coupling is large only when the physical metric is operative yields a
BISTABLE fixed point: an operative fixed point that exists and is stable, is non-vacuous (a fixed
opposite-sign kinematic coupling genuinely spoils it below a critical source coupling), alongside an equally
self-consistent pathological fixed point; self-consistency does not select. Basin selection reduces to the
reservoir Krein signature, equivalently a coupling ratio versus an O(1) threshold.

**Honest limits, stated up front.** The bistable fixed point and its selection are established in a FINITE
TOY MODEL only; whether a generic Stelle-class theory coupled to a physical reservoir realizes this
structure, and which basin it selects, is NOT settled here. Selection is CONDITIONAL on the reservoir Krein
sign, an O(1) coupling ratio that this draft does not compute for any real theory. We state the result at
its honest grade: a reframe plus a non-vacuous existence result, NOT a proof of loop unitarity, and the
draft does not overturn the closed-theory or removal-family results.

## 1. Introduction (skeleton)

- The higher-derivative ghost and the keep-and-grade rescue; tree-level status; the loop question as the
  decider for Stelle gravity, conformal gravity, agravity.
- The move this draft makes: the theory is coupled to an external source, so the physically relevant object
  is an OPEN system, and closed-theory loop-unitarity verdicts (physical-sheet pole implies non-unitary)
  are re-examined in that light.
- Statement of scope: class-level, GU-free; a reframe and an existence result, explicitly not a proof of
  unitarity. Lead the reader with the reduced-pole-versus-total-eigenvalue clarification and flag the
  toy-model and selection-conditional limits before any theorem is stated.

## 2. Setup (class-level, GU-free)

- Krein space H, fundamental symmetry eta = P+ - P- .
- Stelle-class operator D, propagator 1/(p^2(p^2-M^2)) = (1/M^2)(1/p^2 - 1/(p^2-M^2)); the second pole is
  the wrong-sign (ghost) residue; keep-and-grade makes the ghost a real-mass negative-Krein-norm mode
  (Stelle, Phys. Rev. D 16 (1977) 953).
- Coupling to an external source via a source action linear in an external connection/current, making the
  field an open sub-system of H_tot = H_sys (+) H_res with coupling V across a boundary.
- Definitions. "Operative": there exists a positive total metric eta_+ = eta_tot C_tot > 0 under which the
  total generator is pseudo-Hermitian and the total evolution is eta_+-unitary (equivalently the total
  spectrum is real). "Reservoir Krein type": the sign of the reservoir sector the ghost couples into,
  relative to the ghost.

## 3. The theorems, with grades

**Theorem 2 (reduced pole is not the total eigenvalue) -- the load-bearing clarification.** In the finite
Friedrichs / Fano-Anderson model a like-Krein-signed regime exists in which the reduced ghost resolvent
carries an anti-damping physical-sheet pole (argument principle: 1 vs 0 for the normal control) WHILE the
total spectrum is real at every coupling and a positive total metric exists (total unitary to 1e-15). Hence
the closed-theory inference "physical-sheet pole implies non-unitary" fails for an open Krein theory. GRADE:
THEOREM in the finite model; STRUCTURAL for the QFT lift. NOVELTY: KNOWN principle (Feshbach), NEW
application, and the single strongest new point of the draft. (Numbered T2 for continuity with
`VERIFICATION.md`; presented first because it is the load-bearing claim.)

**Theorem 1 (physical-subspace unitarity defect).** For eta-pseudo-unitary S, with A = P+ S P+ and
B = P- S P+, A^dag A = P+ + B^dag B; hence physical-channel probability sums to 1 + ||B|i>||^2 >= 1,
equality iff B|i> = 0; the defect is sign-definite (excess / anti-damping). GRADE: THEOREM (two lines;
machine-checked). NOVELTY: KNOWN-in-substance (Lee-Wick / CLOP physical-subspace unitarity), NEW-form.

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

**Supporting (context, not the paper's novelty).** No-local-positive-metric theorem (every keep-and-grade
positive metric is non-local, kernel decaying at the ghost scale); perturbative C-operator existence below
the two-body decay threshold (conditional on PT-unbroken / sub-threshold); the interacting-C essential
spectrum via analytic Fredholm; the graded CLOP / family map.

### Non-locality price of the total metric (H07)

The positive metric bought by keep-and-grade is NON-LOCAL: for the free theory every admissible positive
metric eta_+ = eta C has a kernel that decays at the ghost scale, C(x,y) ~ e^{-m|x-y|}, and no local
positive metric exists (W54 / W121; the non-locality of the metric / C operator in indefinite-inner-product
and PT theories is the general expectation, cf. Bender, Brody & Jones, Phys. Rev. Lett. 89 (2002) 270401;
Mostafazadeh, Int. J. Geom. Meth. Mod. Phys. 7 (2010) 1191). This price does not disappear in the
open-system reading; it RELOCATES to the TOTAL space. The operative fixed point of Theorem 4 buys
total eta_+-unitarity at the cost of a total metric that is itself non-local, with the same ghost-scale
kernel decay inherited on H_tot. Total unitarity is therefore not free of the standard keep-and-grade cost:
the operative fixed point purchases a real total spectrum and a positive total metric, but that metric is
non-local, and the draft states this so total unitarity is not oversold as a local, cost-free property.

### Remark (suggestive, not load-bearing): fade dynamical selection

A decaying coupling (everpresent ~ 1/sqrt(N)) that also shrinks g_kin could dynamically select the
operative basin, passing through a finite-N non-unitary window. This is a SUGGESTIVE / FUTURE remark only.
It is graded PLAUSIBLE-ONLY and debit-carrying: W187 showed the fade discharges only the MAGNITUDE leg of
selection and NOT the sign, and its unconditional form rests on a tie (g_kin proportional to Lambda) that is
not native to the class. It is deliberately NOT a theorem of Section 3, carries no weight in the abstract,
and is recorded here purely as a direction that a future dressed or cosmological computation could pursue.
It is not part of the load-bearing content (which is Theorems 1-3 plus the non-vacuous existence result of
Theorem 4).

## 4. Toy-vs-general hardening (what must be done, and why the honest grade is what it is)

The novel theorem-grade content (Theorems 4, 5) lives ENTIRELY in a finite Friedrichs / Fano-Anderson
stand-in. It decides STRUCTURE (the loop question is a genuine bistable fixed point; the operative fixed
point exists and is stable and non-vacuous) and it CANNOT fix which basin a real theory realizes. To become
a class-level result it needs either:

1. a GENERIC-CAPTURE LEMMA: a generic Stelle-class operator coupled to a physically reasonable external
   reservoir realizes the Theorem 4 structure (the finite model is representative, not a rig); or
2. a real DRESSED COMPUTATION for an actual reservoir, computing the coupling ratio r* and hence the basin.

Until one is in hand, Theorems 4-5 are toy observations, and the paper's defensible claim is the reframe
(Theorems 1-3) plus the non-vacuous existence result.

## 5. Prior-art delineation (full statement in explorations/W188-class-paper-assessment-2026-07-14.md)

**Lee-Wick / CLOP / fakeon delta (H09).** The two established loop-level unitarity prescriptions for
higher-derivative theories, Lee-Wick (Lee & Wick, Nucl. Phys. B9 (1969) 209; Grinstein, O'Connell & Wise,
Phys. Rev. D 77 (2008) 025012) with the CLOP prescription (Cutkosky, Landshoff, Olive & Polkinghorne, Nucl.
Phys. B12 (1969) 281) and the fakeon prescription (Anselmi & Piva, J. High Energy Phys. 06 (2017) 066;
Anselmi, JHEP 02 (2018) 141), are both in the REMOVAL family: they evacuate the ghost from the asymptotic
state space so that the surviving physical subspace is unitary. This draft is in the KEEP-and-grade family
and does NOT compete with those prescriptions. What it adds: Theorem 1 is exactly their physical-subspace
unitarity defect, re-read in the KEEP branch with a definite (excess, anti-damping) sign; and, more
importantly, the strongest single new point is the OPEN clarification that a physical-sheet pole of the
REDUCED resolvent is not a complex eigenvalue of the TOTAL generator, so the closed removal-family
inference "physical-sheet pole implies non-unitary" does not transfer to an open Krein theory. The draft
characterizes the keep branch and clarifies which closed-theory inferences fail once the theory is opened;
it does not claim to improve on the removal prescriptions on their own ground.

**Bender-Mannheim (PT-symmetric QFT, C-operator, Pais-Uhlenbeck no-ghost theorem) delta (H08).**
Bender & Mannheim (Phys. Rev. Lett. 100 (2008) 110402; Phys. Rev. D 78 (2008) 025022; with the Dirac
quantization of Mannheim & Davidson, Phys. Rev. A 71 (2005) 042110) established, for the CLOSED fourth-order
Pais-Uhlenbeck oscillator (Pais & Uhlenbeck, Phys. Rev. 79 (1950) 145) and conformal (Weyl) gravity, the
operative-vs-not dichotomy: the UNEQUAL-frequency theory has a real spectrum and a positive C-metric
(unitary), while the EQUAL-frequency (conformal, double-pole) case is a non-diagonalizable Jordan block with
NO positive metric. The C-operator, the positive metric eta_+ = eta C (Mostafazadeh, J. Math. Phys. 43
(2002) 205), and the equal-vs-unequal dichotomy are theirs and are KNOWN. What this draft adds: Theorems 4-5
are the OPEN-system EXTENSION of that closed dichotomy. Bender-Mannheim never couple to an external
reservoir, never obtain an open sub-system, and never obtain a selection problem; here the reservoir Krein
type is the NEW selection axis, and total operativity becomes a bistable fixed-point question rather than a
fixed property of the isolated spectrum. The closed operative-vs-not result is a boundary case (empty
reservoir) of the open bistable structure.

- **Mostafazadeh (pseudo-Hermitian QM).** The positive metric eta_+ and quasi-Hermiticity machinery are his
  (J. Math. Phys. 43 (2002) 205; review Int. J. Geom. Meth. Mod. Phys. 7 (2010) 1191); applied here to the
  TOTAL space.
- **Bognar (Krein spaces).** The opposite-type collision producing complex pairs (Theorem 3) is standard
  Krein-space spectral theory (Bognar, Indefinite Inner Product Spaces, Springer 1974).
- **Fano-Anderson / Friedrichs / Feshbach open-system machinery.** The discrete-plus-continuum model and the
  reduced non-Hermitian effective Hamiltonian are textbook (Friedrichs, Commun. Pure Appl. Math. 1 (1948)
  361; Fano, Phys. Rev. 124 (1961) 1866; Feshbach, Ann. Phys. 5 (1958) 357); the NEW move is that the total
  lives on a Krein space, so total unitarity is not automatic and is bistable.
- **Driven-dissipative / non-Hermitian open-system bistability and exceptional points.** Bistability and
  exceptional points in open non-Hermitian systems are established (reviews: El-Ganainy et al., Nat. Phys.
  14 (2018) 11; Ashida, Gong & Ueda, Adv. Phys. 69 (2020) 249); the delta here is that the bistable order
  parameter is the OPERATIVITY OF THE TOTAL METRIC under a self-consistent feedback, not a physical
  observable. This delta is stated explicitly and the closest analogues cited.
- **Turok-Bateman (ghost-parity clearing).** Tree-level; not in competition with the loop question.

## 6. Honest open items (lead with these)

- No proof that any real Stelle-class theory coupled to a physical reservoir realizes the bistable
  structure or selects the operative basin: the pieces are the generic-capture lemma / dressed computation
  of Section 4.
- The physically-anchored kinematic coupling (ghost above the two-body threshold, opposite sign) is the
  DEFAULT and gives the pathological basin; the operative basin requires the source coupling to dominate by
  an unbuilt O(1) factor.
- The operative TOTAL metric is non-local (inherits the no-local-positive-metric price relocated to the
  total space, Section 3 H07); total unitarity carries that cost and must not be oversold.
- The fade selection remark is suggestive / future only (Section 3); it is plausible-only, passes through a
  finite-N non-unitary window, discharges the magnitude leg but not the sign, and carries NO weight in the
  abstract or the theorems.
- The QFT lift of Theorems 2-3 is structural; a genuine field-theoretic model would raise it.

## 7. What this draft does NOT claim

- It does not prove loop unitarity of any higher-derivative theory.
- It does not overturn the closed-theory / removal-family results; it characterizes the open keep-and-grade
  branch and clarifies which closed-theory inferences fail once the theory is opened.
- It asserts no GU-specific content; GU is at most one member of the class and is not required.

*Draft skeleton filed 2026-07-14; hardened 2026-07-14 (HQW-KREIN: fade demoted to a suggestive remark, the
abstract now leads with the reduced-pole-versus-total-eigenvalue clarification and states the toy and
selection-conditional limits up front, the total-metric non-locality price is stated, and the
Bender-Mannheim and Lee-Wick/CLOP prior-art deltas are written and cited). Honest grade SOLID-INCREMENTAL.
Drafts only; candidate promotion and external publication Joe-gated.*
</content>
