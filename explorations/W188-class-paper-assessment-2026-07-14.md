---
artifact_type: exploration
label: W188
created: 2026-07-14
wave: W188
team: CLASS-PAPER
posture: coherence-first; exploration grade; RUTHLESS novelty honesty; GU-independence is the credibility axis (RESEARCH-POSTURE.md); drafts only, candidate promotion Joe-gated
hypothesis: "Is the open-system / Krein loop-unitarity bistability result (W132/W169/W175/W179/W183/W186) an INCREDIBLY-STRONG stand-alone class-level (GU-free) paper, or a re-dressing of known open-system + PT/Krein results? If strong, begin the candidate; else scaffold an honest-grade draft skeleton."
verdict: "SOLID-INCREMENTAL. A GENUINE new-combination reframe with one clean, correct, useful clarification (a physical-sheet pole of the REDUCED resolvent is not a complex eigenvalue of the TOTAL generator, so closed-system 'physical-sheet pole => non-unitary' inferences fail for an open Krein theory), plus a non-vacuous EXISTENCE result for an operative total-unitary fixed point in a finite model. It is NOT incredibly-strong: every EXACT / theorem-grade ingredient is known machinery re-applied (Lee-Wick/CLOP physical-subspace defect; Feshbach reduced resolvent; Bognar opposite-type collision / exceptional point; Mostafazadeh positive metric; Bender-Mannheim C-operator; Sorkin everpresent fade), and the one genuinely novel assembled claim -- bistable selection of TOTAL unitarity with fade dynamics -- is TOY-MODEL grade and selection-conditional on an unbuilt O(1) coupling ratio. A hep-th/math-ph referee would credit the reframe and reject any claim of PROVING loop unitarity. => scaffold a DRAFT (papers/drafts/open-krein-loop-unitarity-bistability/), do NOT begin a candidate."
depends_on:
  - explorations/W132-graded-optical-theorem-physical-subspace-2026-07-14.md
  - explorations/W169-c-operator-perturbative-construction-2026-07-14.md
  - explorations/W175-build-analytic-fredholm-y14-2026-07-14.md
  - explorations/W179-build-c-operator-allorders-2026-07-14.md
  - explorations/W183-external-input-open-system-reframe-2026-07-14.md
  - explorations/W186-source-content-reservoir-krein-type-2026-07-14.md
  - papers/candidates/keep-and-grade-loop-cost/keep-and-grade-loop-cost-2026-07-11.md
  - RESEARCH-POSTURE.md
scripts:
  - tests/W132_graded_optical_theorem_physical_subspace.py
  - tests/W183_external_input_open_system.py
  - tests/W186_source_content_reservoir_krein_type.py
  - tests/W169_c_operator_perturbative_construction.py
  - tests/W179_c_operator_allorders_qft.py
  - tests/W175_analytic_fredholm_essential_spectrum.py
  - tests/W121_path2_target3_hypothesis_hardening.py
---

# W188 -- is there an incredibly strong GU-free class-level paper in the open-Krein loop-unitarity bistability result?

**Role.** Joe's directive: IF there is an incredibly strong, GU-INDEPENDENT class-level paper in the
open-system / Krein loop-unitarity result, begin the candidate; else scaffold a draft skeleton at honest
grade. This wave runs the RUTHLESS novelty delineation (the decision that determines whether there is a
paper at all), states the class-level theorems GU-free with grades, and produces the hardening ledger.
Five personas inline, one worker, no sub-agents. Every quantitative claim ties to a repo test with
recorded exit status (Section 4). No canon / status / verdict change; drafts only; candidate promotion
and any external action remain Joe-gated.

## The candidate result, stated GU-free (class level)

For a higher-derivative (Stelle-class) / PT-symmetric / keep-and-grade Krein-quantized field theory
coupled to an EXTERNAL SOURCE (an open system across a boundary), loop-level TOTAL unitarity is a
BISTABLE open-system fixed-point problem: the operative (positive-total-metric, total-unitary) fixed
point EXISTS, is STABLE, and is NON-VACUOUS (a fixed opposite-sign kinematic coupling genuinely spoils
it below a threshold); but a pathological fixed point is EQUALLY self-consistent and stable;
self-consistency does not select; selection reduces to the reservoir's Krein signature / a coupling
ratio vs an O(1) threshold; and a decaying (fade) coupling can dynamically select the operative basin.

## 1. Persona 1 -- PT-QFT / Krein prior-art scholar

**Bender-Mannheim (PT-symmetric QFT; the C-operator; Pais-Uhlenbeck no-ghost theorem).** Bender-Mannheim
established, for the CLOSED fourth-order Pais-Uhlenbeck oscillator and conformal (Weyl) gravity, that the
UNEQUAL-frequency theory has a real spectrum and a positive C-metric (unitary), while the EQUAL-frequency
(conformal, 1/p^4 double-pole) case is a non-diagonalizable Jordan block with NO positive metric. This is
the operative-vs-not dichotomy at the CLOSED, isolated-spectrum level. Assessment: the C-operator, the
positive metric eta_+ = eta C, and the equal-vs-unequal (resonant-vs-generic) dichotomy are KNOWN. The
repo's W169 (Q2 obstruction on a measure-zero commensurate lattice, otherwise C exists through the first
loop order) is a NATIVE re-derivation plus a mild extension of Bender-Mannheim to the specific model:
NEW-COMBINATION at most, mostly KNOWN. Crucially, Bender-Mannheim never couple to an external reservoir,
never get an open sub-system, and never get a bistable selection problem: the OPEN-SYSTEM bistability is
NOT in their work.

**Mostafazadeh (pseudo-Hermitian QM).** The positive metric eta_+ from the eigenvectors, quasi-Hermiticity
requiring a real spectrum, and the order-by-order metric construction are ALL his. KNOWN. The open-system /
bistable structure is not.

**Turok-Bateman (arXiv:2607.00096; the Bateman / ghost-parity clearing).** Tree-level ghost decoupling via
the Bateman transform, a CLOSED, TREE-level statement. The loop-level open-system reframe is beyond its
scope; not scooped, but also does not support the loop claim.

**Anselmi-Piva (fakeon / CLOP) and Grinstein-O'Connell-Wise (Lee-Wick).** These are the two established
loop-level unitarity prescriptions for higher-derivative theories, both in the REMOVAL family (evacuate
the ghost from the asymptotic state space). The candidate result is in the KEEP-and-grade family, so it
does not compete head-on; but the physical-subspace unitarity defect it uses (Theorem 1) is exactly the
Lee-Wick/CLOP physical-subspace object, so the defect identity is KNOWN-in-substance.

## 2. Persona 2 -- open-quantum-systems scholar

**Fano-Anderson / Friedrichs / Feshbach.** The discrete-state-plus-continuum model, the embedded
eigenvalue dissolving into a resonance, the reduced (Feshbach) energy-dependent non-Hermitian effective
Hamiltonian, and the sub-unitary sub-system with a unitary total are ALL textbook (Friedrichs 1948; Fano
1961; Feshbach 1958; Breuer-Petruccione). KNOWN. This is the entire open-system stand-in.

**The honest question: is bistable TOTAL unitarity of an open system known?** Two parts.
(i) In ORDINARY (positive-metric) open systems the total is unitary BY CONSTRUCTION (Hermitian total
Hamiltonian): total unitarity is never in question, so there is no bistable total-unitarity problem. The
novelty axis is that the total here lives on a KREIN (indefinite-metric) space, so total unitarity is NOT
automatic and depends on the reservoir's Krein signature. That is genuinely different from the textbook
open system, and it is the one clean structural point.
(ii) BUT bistability itself is heavily studied in driven-dissipative / non-Hermitian open systems (optical
bistability, dissipative phase transitions, PT-symmetric systems coupled to reservoirs; Longhi and others
on PT open systems and exceptional points in the total generator). So "a bistable open system" and "an
exceptional point in an open non-Hermitian generator" are NOT new. The specific and only novel move is
that the bistable order parameter is the OPERATIVITY OF THE TOTAL METRIC (whether a positive C-metric
exists) rather than a physical observable, with a self-consistent FEEDBACK (the source coupling is large
only when records are physical, i.e. only when the C-metric is operative). That feedback-closing-the-loop
on the metric's own operativity is the piece I cannot match to a known reference. It is a NEW-COMBINATION,
and it is toy-grade.

## 3. Persona 3 -- math-ph theorem-stater: the class-level theorems, GU-free, with grades

**Setup.** H a Krein space, fundamental symmetry eta = P+ - P- . D a Stelle-class field operator whose
propagator 1/(p^2(p^2-M^2)) = (1/M^2)(1/p^2 - 1/(p^2-M^2)) carries a wrong-sign (ghost) residue;
keep-and-grade quantization makes the ghost a real-mass negative-Krein-norm mode. Couple to an external
source via a source action linear in an external connection/current, making the field an OPEN sub-system
of H_tot = H_sys (+) H_res with coupling V across a boundary. "Operative" := there exists a positive total
metric eta_+ = eta_tot C_tot > 0 with the total generator eta_+-pseudo-Hermitian and the total evolution
eta_+-unitary (equivalently, real total spectrum). Reservoir Krein type := sign of the reservoir sector
the ghost couples into, relative to the ghost.

**THEOREM 1 (graded optical theorem / physical-subspace unitarity defect).** For any eta-pseudo-unitary S
(S^dag eta S = eta), with A = P+ S P+ and B = P- S P+,
    A^dag A = P+ + B^dag B,
so physical-channel probabilities from a physical in-state sum to 1 + ||B|i>||^2 >= 1, equality iff
B|i> = 0; the defect is sign-definite (excess / anti-damping), refuting any dissipative decay-width
reading. GRADE: THEOREM (two lines from pseudo-unitarity; machine-checked, W132 tests S1-S2). NOVELTY:
KNOWN-in-substance (Lee-Wick/CLOP physical-subspace unitarity), NEW-form (clean sign-definite operator
identity).

**THEOREM 2 (reduced pole is not the total eigenvalue).** In the finite Friedrichs/Fano-Anderson model
there is a like-Krein-signed regime in which the reduced (Feshbach) ghost resolvent carries an
anti-damping physical-sheet pole (argument principle: exactly 1 vs 0 for the normal control) WHILE the
total spectrum is real at every coupling and a positive total metric exists (total eta_+-unitary to
1e-15). GRADE: THEOREM in the finite model (exact / argument principle); STRUCTURAL for the QFT lift.
NOVELTY: KNOWN principle (Feshbach open-system resonance), NEW-application to the higher-derivative ghost.

**THEOREM 3 (Krein exceptional-point obstruction; opposite-signed reservoir).** In the opposite-Krein-
signed regime, opposite-type eigenvalues collide and the TOTAL generator develops a complex-conjugate
pair above an exceptional point g_c > 0 (located by bisection, g_c = 0.392 in the toy); no positive total
metric; genuinely non-unitary. GRADE: THEOREM in the finite model. NOVELTY: KNOWN (Bognar opposite-type
collision), NEW-application. COROLLARY (T2+T3): total operativity is CONDITIONAL on the reservoir Krein
type -- NEW-COMBINATION as a statement about open higher-derivative theories.

**THEOREM 4 (bistable fixed point: existence, stability, non-vacuity) -- the load-bearing novel claim.**
Impose the self-consistency kappa(m) = kappa_max * m, m in {0,1} the operativity order parameter (records
physical only when the C-metric is operative), in the presence of a fixed metric-INDEPENDENT opposite-sign
kinematic coupling g_kin. Then (a) NON-VACUITY: there is a critical kappa*(g_kin) > 0 (bisection, 1.059 in
the toy) below which the total is complex (favorable fixed point spoiled) and above which real, so the
operative fixed point's existence is a real computation that can and does fail; (b) BISTABILITY: for
kappa_max > kappa*, both m=1 and m=0 are self-consistent fixed points; self-consistency does not select;
(c) STABILITY: both fixed points return under perturbation, EP the separatrix; (d) BOOTSTRAP: at m=1 the
total spectrum is real, eta_+ > 0 (min eig 0.448), total eta_+-unitary to 6e-14, while the sub-system
gains. GRADE: TOY-MODEL (finite Friedrichs/Fano-Anderson stand-in; exact/machine-checked WITHIN the toy,
W186 Block D). NOVELTY: NEW-COMBINATION (feedback-driven bistable selection of total unitarity in a Krein
open system); the ingredients KNOWN.

**THEOREM 5 (selection reduces to a coupling ratio vs an O(1) threshold).** Basin selection is set by
kappa_max/g_kin vs r* ~ O(1); self-consistency alone decides nothing. GRADE: TOY / STRUCTURAL. NOVELTY:
NEW framing; this is precisely the honest LIMIT (the selection datum is unbuilt).

**PROP 6 (fade dynamics can dynamically select the operative basin).** If a decaying coupling (everpresent
~ 1/sqrt(N)) also shrinks g_kin as the reservoir accretes, a favorable start stays favorable and even a
pathological start is driven real asymptotically, through a finite-N non-unitary window. GRADE:
PLAUSIBLE-ONLY (ported, debit-carrying; W186 Block E). NOVELTY: NEW-COMBINATION but the weakest leg.

**Supporting machinery (context, not the paper's novelty).** No-local-positive-metric theorem (W121/W54:
KNOWN direction, hardened -- every keep-and-grade positive metric is non-local); perturbative C-operator
existence below the two-body decay threshold (W169/W179: Bender-Mannheim extended natively, CONDITIONAL-
on-sub-threshold / PT-unbroken); the interacting-C essential-spectrum / analytic-Fredholm bound (W175);
the graded CLOP / family map (W124/W133: KNOWN).

**The toy-vs-general gap (Joe's "kill the toy-model dependence").** The novel theorem-grade content (T4,
T5, P6) lives ENTIRELY in a finite Friedrichs/Fano-Anderson stand-in. To be a real class-level result it
needs EITHER a GENERIC-CAPTURE LEMMA (a generic Stelle-class operator coupled to a physically reasonable
external reservoir realizes the bistable-fixed-point structure -- the finite model is representative, not
a rig) OR a real dressed computation (a W187-style calculation showing the operative basin is achieved for
an actual reservoir). Without one, T4/T5/P6 are toy observations, not theorems about the class.

## 4. Persona 4 -- reproducibility / verification engineer: the machine-check map (recorded 2026-07-14)

| Claim | Test | Recorded |
|---|---|---|
| T1 A^dag A = P+ + B^dag B; sign-definite defect | tests/W132_graded_optical_theorem_physical_subspace.py | 18/18, exit 0 |
| T2 reduced physical-sheet pole with real total + positive total metric (like-signed) | tests/W183_external_input_open_system.py | 27/27, exit 0 |
| T3 total exceptional point g_c=0.392, no positive total metric (opposite-signed) | tests/W183_external_input_open_system.py | 27/27, exit 0 |
| T4 bistable fixed point: non-vacuity kappa*=1.059, both fixed points stable, eta_+ min eig 0.448, total unitary 6e-14 | tests/W186_source_content_reservoir_krein_type.py | 36/36, exit 0 |
| C-operator existence through Q2 (off resonance), obstruction on commensurate lattice | tests/W169_c_operator_perturbative_construction.py | exit 0 |
| C-operator all-orders QFT: existence CONDITIONAL-ON-SUB-THRESHOLD | tests/W179_c_operator_allorders_qft.py | exit 0 |
| interacting-C essential spectrum (analytic Fredholm) | tests/W175_analytic_fredholm_essential_spectrum.py | exit 0 (slow, ~3 min) |
| no-local-positive-metric hardening | tests/W121_path2_target3_hypothesis_hardening.py | exit 0 |

All eight ran to exit 0 on 2026-07-14 (Python, numpy). W175 is slow (about three minutes). The
theorem-grade novelty (T4) is machine-checked ONLY within the finite toy; no test exercises a real
Stelle/GU dressed reservoir (that is the hardening gap).

## 5. Persona 5 -- hostile referee (full strength)

**Attack on novelty.** "You have assembled known pieces -- the Lee-Wick/CLOP physical-subspace defect, the
Feshbach reduced resolvent, the Bognar opposite-type exceptional point, the Mostafazadeh positive metric,
the Bender-Mannheim C-operator, the Sorkin everpresent fade -- into a finite model and called the assembly
a set of theorems. Every EXACT statement (T1, T2, T3) is a known object re-applied to the higher-derivative
ghost. The only thing that is not off-the-shelf, the feedback-driven bistable selection (T4), is a
TOY with a hand-chosen kappa(m); a driven-dissipative-systems referee has seen bistability and exceptional
points in open non-Hermitian systems for two decades. Where is the theorem about the CLASS?"

**Attack on the toy-vs-general gap.** "The physically-anchored coupling in a real Stelle theory is the
opposite-sign kinematic one (the ghost above the two-graviton threshold decaying into positive-norm
gravitons). By your own Theorem 3 that is the pathological basin. Your operative basin exists only above an
unbuilt O(1) coupling ratio you never compute for any real theory. So you have PROVEN nothing about whether
any higher-derivative theory is actually loop-unitary this way. The paper's honest content is: 'IF an
external source dominates the kinematic channel by an unbuilt O(1) factor, THEN a toy model is total-
unitary.' That is a conditional observation, not a unitarity theorem."

**Would a hep-th / math-ph referee accept this as NEW?** As a THEOREM paper claiming loop unitarity: NO
(rejected on the toy-vs-general gap and the selection-conditionality). As a math-ph FRAMEWORK / LETTER
making one clean, correct, useful point -- that for an open indefinite-metric (Krein) higher-derivative
theory a physical-sheet pole of the REDUCED resolvent does NOT imply a non-unitary TOTAL, so closed-system
'physical-sheet pole => non-unitary' inferences are invalid, and total operativity is a genuine bistable
fixed-point selection set by the reservoir Krein type -- with the toy-vs-general gap flagged honestly:
PLAUSIBLY, at a good-but-not-flagship venue, AND only after the generic-capture lemma or a real dressed
computation is in hand. The reduced-pole-vs-total-eigenvalue clarification is the strongest single
contribution and is correct.

**Honest verdict:** OVERCLAIMED if sold as incredibly-strong; SOLID-INCREMENTAL and genuinely useful if
sold as an honest reframe. Not INCREDIBLY-STRONG.

## 6. Synthesis -- verdict, per-element delineation, decision

**VERDICT: SOLID-INCREMENTAL.** A genuine new-combination reframe with one clean correct clarification and
a non-vacuous existence result in a toy; NOT incredibly-strong, because the theorem-grade content is known
machinery and the novel assembled claim is toy-model and selection-conditional.

| Element | KNOWN / NEW |
|---|---|
| A^dag A = P+ + B^dag B (defect operator, sign-definite) | KNOWN-in-substance (Lee-Wick/CLOP), NEW-form |
| Reduced pole =/= total eigenvalue for the ghost | KNOWN principle (Feshbach/Fano), NEW-application |
| Krein exceptional-point obstruction (opposite-signed reservoir) | KNOWN (Bognar), NEW-application |
| Positive total metric / total eta_+-unitarity (like-signed) | KNOWN (Mostafazadeh), NEW-application to the total |
| Total operativity CONDITIONAL on reservoir Krein type | NEW-COMBINATION |
| Bistable fixed point with feedback, non-vacuous | NEW-COMBINATION, TOY |
| Selection = coupling ratio vs O(1) | NEW framing (= the honest limit) |
| Fade dynamical selection | NEW-COMBINATION, PLAUSIBLE-only |
| C-operator perturbative existence below threshold | KNOWN (Bender-Mannheim), NEW native model |
| No-local-positive-metric | KNOWN direction (W54/W121), hardened |

**Decision.** SOLID-INCREMENTAL does not meet Joe's "incredibly strong" trigger to begin a CANDIDATE.
Per the directive and RESEARCH-POSTURE, I scaffold a DRAFT skeleton at honest grade in
papers/drafts/open-krein-loop-unitarity-bistability/ (README, draft-skeleton, VERIFICATION). No candidate
promotion; no external action. The draft leads with what is proven (T1-T3 in the finite model; T4 non-
vacuity in the toy) versus what is conditional (basin selection; the QFT lift), and the abstract states the
toy-model and selection-conditionality honestly.

## 7. Hardening ledger to submission (ranked)

1. **GENERIC-CAPTURE LEMMA (decisive; without it there is no class-level theorem).** Prove that a generic
   Stelle-class operator coupled to a physically reasonable external reservoir realizes the T4 bistable-
   fixed-point structure -- i.e. the finite Friedrichs/Fano-Anderson model is representative, not a rig.
   This is the single gate between "toy observation" and "class-level result." Alternative discharge: the
   W187-style DRESSED COMPUTATION showing the operative basin is achieved (or not) for an actual reservoir
   and computing the coupling ratio r*.
2. **PRIOR-ART DELTA against driven-dissipative / non-Hermitian open-system bistability.** A referee will
   have seen bistability and exceptional points in open non-Hermitian systems. State precisely the delta:
   the bistable order parameter here is the OPERATIVITY OF THE TOTAL METRIC with a self-consistent
   feedback, not a physical observable. Sweep Longhi and the PT-open-systems / dissipative-phase-transition
   literature and cite the closest analogues explicitly.
3. **PRIOR-ART DELTA against Bender-Mannheim.** State that T4/T5 are the OPEN-system extension of the
   Bender-Mannheim closed operative-vs-not dichotomy; the equal-vs-unequal frequency result is theirs, the
   reservoir-Krein-type selection is the new axis. Cite the PU no-ghost theorem and the conformal-gravity
   unitarity papers.
4. **PRIOR-ART DELTA against Lee-Wick / CLOP / fakeon.** State that T1 is the physical-subspace unitarity
   defect of the removal family, re-read with a definite sign in the keep-and-grade family; the paper does
   not compete with the removal prescriptions, it characterizes the keep branch.
5. **REMOVE the everpresent-fade leg from the load-bearing claims (or grade it PLAUSIBLE loudly).** P6 is
   ported, debit-carrying, and passes through a finite-N non-unitary window; it must not carry weight in
   the abstract. Either demote to a clearly-flagged remark or supply a native normalization.
6. **QFT-LIFT of T2/T3 beyond the finite model.** The reduced-pole-vs-total-eigenvalue separation is
   currently exact only in the finite Friedrichs stand-in; a genuine field-theoretic statement (even a
   1+1 or mini-superspace model) would raise T2/T3 from STRUCTURAL to THEOREM in QFT.
7. **Non-locality accounting of the TOTAL C-operator.** The total metric inherits the W54/W121 non-locality
   debt relocated to the total space; the draft must state the price honestly (the operative metric is
   non-local, kernel decaying at the ghost scale) so total unitarity is not oversold.

*Filed 2026-07-14 by TEAM CLASS-PAPER (W188). Coherence-first; exploration grade; RUTHLESS novelty
honesty. Five personas inline (PT-QFT/Krein prior-art scholar; open-quantum-systems scholar; math-ph
theorem-stater; reproducibility engineer; hostile referee); no sub-agents. Verdict SOLID-INCREMENTAL;
draft scaffolded, candidate NOT begun. No canon / status / verdict / posture change; drafts only; external
action and candidate promotion Joe-gated.*
</content>
