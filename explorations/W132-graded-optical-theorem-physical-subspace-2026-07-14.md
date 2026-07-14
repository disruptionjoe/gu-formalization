---
artifact_type: exploration
status: exploration (W132 / H69; 5-persona inline team; one deterministic test; the W48 gate question formalized and computed at toy level)
created: 2026-07-14
hypothesis: H69 (in service of H59)
branch: "Team H69 (W132): the graded optical theorem on the physical subspace -- does the odd-ghost-cut leak violate physical-subspace unitarity?"
title: "W132 VERDICT: VIOLATES-ON-THE-FREE-POSITIVE-SUBSPACE / PRESERVED-IN-THE-C-METRIC-SENSE-ONLY / DECAY-WIDTH-READING-REFUTED-BY-SIGN. The formalization is one exact line: for any Krein-pseudo-unitary S (S^dag eta S = eta, eta = P+ - P-), the physical-subspace S-matrix A = P+ S P+ obeys A^dag A = P+ + B^dag B with B = P- S P+, so S restricted to the positive subspace is an EXPANSION, not a contraction: physical-channel probabilities from a physical in-state sum to 1 + sum_odd |S_fi|^2 >= 1, with equality iff the odd-ghost sector decouples. The leak direction is probability EXCESS into the physical channels, which kills the 'ghost as decay width / probability draining into the graded sector' reading outright (dissipation gives contractions; this is anti-damping). In the W120/W124 toy the elastic partial-wave bound |S_J| <= 1 is SATISFIED on M^2 < s < 2M^2, VIOLATED for every s > 2M^2 (crossover exactly s* = 2M^2, where the doubled mixed cut overtakes the gg cut), maximally violated at the two-ghost threshold s = 4M^2 (deficit -1/4 in units of the gg cut), with a -M^4/s^2 tail; the ghost-free-sector (multichannel) deficit is negative for ALL s > M^2 and tends to -1/2, so the violation is not confined to any window. The ONLY preservation sense available is C-metric unitarity on the FULL Krein space (S^dag eta_+ S = eta_+ with eta_+ = eta C > 0), demonstrated exactly on a constructed S that simultaneously violates naive-subspace unitarity; in QFT that sense is conditional on the interacting C-operator (branch B: exists order by order in QM) and priced non-local by the W54 theorem. Keep-and-grade unitarity is hereby reduced without remainder to the C-operator question: there is no independent physical-subspace optical theorem to hope for. H59 remains OPEN."
grade: "EXACT for the expansion identity A^dag A = P+ + B^dag B and for the Part-2 C-metric coexistence construction (finite-dimensional, machine-verified to 1e-12; the identity is two lines of algebra from S^dag eta S = eta); STRUCTURAL for its application to the QFT S-matrix (fixed-order Fock grading + pseudo-unitarity from the largest-time equation with eta-real couplings, the standard ARGUED step of branch A); TOY-CHECKED for every partial-wave number (split-propagator toy, weights forced by the propagator product, normalization verified in-test by the elastic-cut identity PC0); ARGUED for the Lee-Wick comparison (proof-structure analysis against CLOP 1969 / Lee-Wick 1969, no new computation) and for the tensor-numerator and resonance-window caveats. Test: W132 18/18, exit 0, with positive controls (normal-sign theory satisfies and saturates the standard optical theorem; removal prescription preserves the bound) and negative control (residue flip removes the violation). NO canon / RESEARCH-STATUS / claim-status / verdict / posture change. H59 remains OPEN."
depends_on:
  - explorations/path2-branchA-cutkosky-cut-2026-07-11.md
  - explorations/path2-branchB-pt-c-operator-2026-07-11.md
  - explorations/path2-wave3-target2-graded-clop-and-target3-hardening-2026-07-13.md
  - explorations/path2-wave4-target2-two-loop-overlap-selfenergy-2026-07-13.md
  - explorations/landscape-assessment-post-three-waves-2026-07-14.md
  - papers/candidates/keep-and-grade-loop-cost/keep-and-grade-loop-cost-2026-07-11.md
  - tests/W48_H59_krein_loop_positivity_gate.py
  - tests/W120_path2_target2_keepgrade_vs_clop.py
  - tests/W124_stageA_sunset_graded_vs_LW_CLOP.py
  - tests/W124_stageB_overlap_kite_cuts.py
  - GEOMETER-VS-PHYSICS-OBJECTS.md
scripts:
  - tests/W132_graded_optical_theorem_physical_subspace.py
external_refs:
  - "Lee & Wick, Negative metric and the unitarity of the S-matrix, NPB 9 (1969) 209 -- unitarity on the physical space via non-asymptotic ghosts"
  - "Cutkosky, Landshoff, Olive & Polkinghorne, A non-analytic S-matrix, NPB 12 (1969) 281 -- the actual physical-subspace unitarity argument for Lee-Wick theories"
  - "Bognar, Indefinite Inner Product Spaces, Springer 1974 -- Krein decompositions, maximal positive subspaces"
  - "Mostafazadeh, Pseudo-Hermiticity versus PT symmetry, JMP 43 (2002) 205 -- positive metric eta_+ = eta C from the C-operator"
  - "Bender, Brody & Jones, Complex extension of quantum mechanics, PRL 89 (2002) 270401 -- the C-operator construction"
  - "'t Hooft & Veltman, Diagrammar, CERN 73-9 -- largest-time equation, pseudo-unitarity diagram by diagram"
---

# W132 -- the graded optical theorem on the physical subspace (H69, the W48 gate)

**Role.** The 2026-07-14 landscape assessment names H69 as the precise form of the open
loop-positivity price: the odd-ghost cut is negative (W48: `-pi(1-M^2/s)` on the one-loop bubble;
W124: `-0.0849` at the kite), and nobody had tested that leak against the optical theorem
restricted to the PHYSICAL subspace, the only unitarity that matters physically. This wave
formalizes the physical-subspace statement, computes the partial-wave unitarity bound in the
W120/W124 toys, and settles the interpretation question (leak as decay width vs leak as
violation). Five personas ran inline, sequentially; deterministic test
`tests/W132_graded_optical_theorem_physical_subspace.py` (18/18, exit 0).

## 0. Construction forks (GEOMETER-VS-PHYSICS-OBJECTS.md discipline)

| Object | Constructions in play | Handling |
|---|---|---|
| **"The physical subspace"** | (i) free-grading positive (even-ghost-number) sector `H_+` of the Krein Fock space; (ii) ghost-free sector (no ghost quanta at all); (iii) the C-positive subspace of the interacting C-metric | ALL THREE computed or characterized; the verdict is stated per construction (this fork IS the result) |
| **The ghost** | keep-and-grade stable Krein-graded real-mass state (the branch under test, per the mandate) | the instability escape is named as the exit INTO the removal family, not a defense of grading |
| **Unitarity** | (K) pseudo-unitarity `S^dag eta S = eta`; (P) physical-subspace probability conservation; (C) `eta_+`-unitarity on the full space | branch A's (K)/(P) split kept sharp; (C) added as the third, previously implicit sense |
| **Cutting rules** | real-axis Cutkosky with Krein weights `(-1)^{n_ghost}` (W120/W124 machinery) | inherited unchanged; weights on the toy forced by the propagator product, not chosen |

## 1. Persona 1 -- Krein/PT specialist: the formalization (question 1)

**The graded optical theorem.** With `eta = P_+ - P_-` (fundamental symmetry; on the Fock space
built from the free grading, `P_+` projects on even ghost number, `P_-` on odd) and `S = 1 + iT`
pseudo-unitary, `S^dag eta S = eta` gives `i(eta T - T^dag eta) = -T^dag eta T`, so for
`|i> in H_+` normalized:

    2 Im T_ii = sum_{f even} |T_fi|^2 - sum_{f odd} |T_fi|^2.

The odd-ghost cuts enter with the minus sign; this is the leak, now stated at operator level.

**The physical-subspace statement (the exact core of this wave).** Let `A = P_+ S P_+` (the
physical-subspace S-matrix) and `B = P_- S P_+` (the ghost-production block). Sandwiching
pseudo-unitarity with `P_+` and using `P_+ eta = P_+`, `P_- eta = -P_-`:

    A^dag A = P_+ + B^dag B.

Two lines of algebra, EXACT, all orders, no toy input (machine-verified on random pseudo-unitary
S, test S1-S2). Consequences:

1. **Probability conservation on the physical subspace reads:** for physical `|i>`,
   `sum_{f phys} |S_fi|^2 = 1 + sum_{f odd} |S_fi|^2 >= 1`, with equality iff `B|i> = 0`.
   The physical-subspace S-matrix is unitary iff the odd-ghost sector DECOUPLES. W120/W124
   computed the odd-cut amplitudes and they are nonzero; `B != 0` in keep-and-grade.
2. **The violation direction is EXCESS, not loss.** `A` is an expansion (`||A psi|| >= ||psi||`),
   never a contraction. Probability is not draining out of the physical world into a hidden
   graded sector; the physical channels RECEIVE more probability than the in-state carried.
3. **What `2 Im T_phys` equals:** strictly less than the physical-channel sum,
   `2 Im T_ii = sum_phys |T_fi|^2 - sum_odd |T_fi|^2 < sum_phys |T_fi|^2` whenever any odd
   channel is open. The forward absorption undercounts the observable production; that IS the
   optical-theorem failure, localized in one inequality.

**Bognar note.** `H_+` above is the maximal positive subspace of the free grading. Choosing a
different maximal positive subspace rotates `P_+` but cannot change the conclusion: the identity
holds for every fundamental decomposition, and `B = 0` for some decomposition iff `S` commutes
with the corresponding grading, which is exactly the C-operator condition of Section 3.

## 2. Persona 2 + 3 -- unitarity analyst and loop engineer: the partial-wave bound (question 2)

**The toy.** `chi chi -> chi chi` (massless matter) through the dressed fourth-order propagator
`D(s) = (1/M^2)[1/s - 1/(s - M^2)]`, graviton-sector one-loop bubble from the split propagator
squared. The propagator product FORCES the cut weights: `D x D` has coefficients `(+1, -2, +1)`
on the `(gg, g+ghost, ghost+ghost)` bubbles, which with identical-particle phase-space factors
gives channel weights `(1/2, -1, 1/2)`. The mixed (odd) channel is DOUBLED relative to branch A's
single-counting table; this factor of 2 is combinatorics of the split, not a choice, and it moves
the crossover. Normalization is verified in-test, not assumed: the elastic chi-chi cut equals
`|a_tree|^2` exactly (PC0, two routes, dev 4e-22), so the partial-wave bound is internally
calibrated.

**The elastic bound.** `|S_J|^2 = |1 + 2ia|^2 = 1 - 4(Im a - |a|^2)`; at leading order the
elastic cut cancels `|a_tree|^2` and the deficit shape is the graviton-sector signed cut sum

    F(s) = (1/2) rho_00 - rho_0M + (1/2) rho_MM,   rho_ab = sqrt(lambda(s,a,b))/s.

| `s/M^2` | `F(s)` | `|S_J|^2 - 1` (g = lam = 5) | bound |
|---|---|---|---|
| 1.5 | +0.16667 | -1.466e-01 | HOLDS |
| 2.0 | 0 (exact) | 0 | boundary |
| 2.5 | -0.10000 | +3.518e-03 | **VIOLATED** |
| 3.0 | -0.16667 | +2.290e-03 | **VIOLATED** |
| 4.0 | -0.25000 | +8.589e-04 | **VIOLATED (maximal)** |
| 5.0 | -0.07639 | +9.449e-05 | **VIOLATED** |
| 8.0 | -0.02145 | +3.383e-06 | **VIOLATED** |
| 20.0 | -0.00279 | +9.547e-09 | **VIOLATED** |

Structure (all closed-form, test P2): `F > 0` on `M^2 < s < 2M^2` (the gg cut still covers the
leak there); crossover at EXACTLY `s* = 2M^2`, where the doubled mixed cut `2(1 - M^2/s)`
overtakes `rho_00 = 1`; `F < 0` for every `s > 2M^2`; the two-ghost cut opening at `4M^2` only
softens the violation (maximum `|F| = 1/4` exactly at threshold); tail `F -> -M^4/s^2` (fitted
slope -2.004, coefficient 1.001). So the answer to the question "is total Im (physical + Krein
ghost cuts) still >= the unitarity bound?": NO for all `s > 2M^2`, and the total never recovers.

**The stronger multichannel statement.** Against the ghost-free physical sector (every matched
physical cut cancelled by its own `|a_if|^2`), the deficit is `G(s) = -rho_0M + (1/2) rho_MM`,
which is negative for ALL `s > M^2` and tends to `-1/2` as `s -> infinity` (test P4). The
elastic bound's `s < 2M^2` grace window is an artifact of letting the gg channel's surplus
mask the leak; row-level probability conservation fails from the first odd threshold on, and
the failure does NOT die at large s. The violation is therefore not confined to the resonance
window `|s - M^2| <~ M Gamma` and cannot be waved off as a fixed-order breakdown artifact.

**Controls.** Normal-sign theory (all weights positive): bound satisfied and standard optical
theorem saturated at every sampled s (P1, PC0). Removal/Lee-Wick prescription (ghost cuts
identically zero, the W120 L2 / W124 result): deficit `= +1/2 > 0` everywhere, physical-subspace
unitarity preserved, reproducing the Cutkosky et al. structure (P6). Residue flip: violation
disappears (N1); the effect tracks the Krein sign and nothing else.

## 3. Persona 1 + 4 -- the structural question (question 3): is there a preserved weaker sense?

**The decay-width / interference reading is REFUTED, by sign.** The proposed reading was: the
ghost is a Krein resonance that removes probability from the physical channel; negative cut =
probability flowing INTO the graded sector; physical unitarity survives in an open-system sense.
The exact identity kills this: an open (dissipative) system has a CONTRACTIVE physical S-matrix
(`S^dag S <= 1`, Lindblad-compatible), whereas `A^dag A = P_+ + B^dag B >= P_+` is EXPANSIVE.
The odd-ghost leak pumps probability INTO the observable channels; it is anti-damping, the
S-matrix face of branch A's anti-resonance (wrong-sign width) observation. No open-system or
"probability hides in the ghost sector" reading exists, because the sign is the wrong way.

**The one surviving sense: C-metric unitarity on the FULL space.** If an interacting C-operator
exists (`C^2 = 1`, `[S, C] = 0`, `eta_+ = eta C > 0`), then `S^dag eta_+ S = eta_+`: the theory
is exactly unitary on the WHOLE Krein space with the positive inner product `<.|eta_+|.>`, all
probabilities positive, total probability 1. Part 2 of the test constructs such an `S`
explicitly (`S = e^{Q/2} e^{ih} e^{-Q/2}` with `[h, eta] = 0`, `Q` Hermitian and eta-odd): the
SAME matrix violates naive-subspace unitarity (physical row sum 97.12) while conserving
C-probability to 1e-12 (C1-C4). This is the exact-toy demonstration that the two statements
coexist without contradiction: the violation is real on the free positive subspace AND the
theory can be unitary, if and only if the physical inner product is the C-metric one. In that
reading the ghost is a bona fide positive-probability out-state (in the C inner product) and
the "leak" becomes ordinary inelasticity into ghost channels, with books balanced.

**Connection to W121/branch B, made load-bearing.** The C-metric sense is not free: branch B
showed the interacting C exists order by order in QM but its QFT generator carries
`1/sqrt(k^2+m^2)` energy denominators, and W54 (hardened by the W121-test audit) proves no local
positive metric exists for the free fourth-order field, with the differential-operator escapes
closed. So the preservation sense that survives is exactly as strong as the C-operator program
and pays exactly the W54 non-locality price. After this wave the reduction is without remainder:
**keep-and-grade has no unitarity resource other than the C-operator.** There is no independent
"physical-subspace optical theorem" for it to satisfy; the free-grading subspace fails
exactly, and the C-subspace succeeds trivially when C exists.

## 4. Persona 4 -- mathematical physicist: the Lee-Wick comparison

Cutkosky-Landshoff-Olive-Polkinghorne's actual physical-unitarity argument has three steps:
(i) the ghost's self-energy moves its pole off the real axis into a complex-conjugate pair, so
the ghost is NOT an asymptotic state; (ii) asymptotic completeness is postulated on the stable,
positive-norm states only, so the unitarity equation's saturation runs over physical states
alone; (iii) the largest-time/cutting equations are made consistent with (ii) by deforming the
contour so ghost cuts cancel pairwise (Schwarz reflection; W120's L1/L2 verified exactly this
zero on the bubble, W124 on the sunset), at the price of the CLOP order-of-limits ambiguity at
mixed two-ghost thresholds and of micro-causality. Their `S^dag S = 1` on the physical space is
GENUINE unitarity, bought by evacuating the ghost from the state space.

The graded theory negates step (i) by mandate: the ghost is KEPT with real mass as an
asymptotic Krein state. Then step (ii) is unavailable (the odd sector is part of asymptotic
completeness) and step (iii) is unnecessary (no deformation; W120). What replaces the Lee-Wick
theorem is exactly the pair of statements of Section 1: pseudo-unitarity (exact, their equation
projected with eta instead of 1) and the expansion identity (their unitarity defect, now with a
definite SIGN and a definite operator, `B^dag B`). The two families' unitarity statements are
thus formally dual: removal deletes `B` by fiat of the state space and pays in
causality/ambiguity; grading keeps `B != 0` and pays either the violation (free subspace) or
the C-metric non-locality (full space). This is the state-space half of the W120 disjoint-loci
map, and it closes the same way: there is no third option in which the graded `B` survives AND
the free positive subspace conserves probability.

## 5. Persona 5 -- adversarial skeptic: steelmanning VIOLATES, then attacking the violation

**The steelman, at full strength.** The violation is not a toy artifact and not perturbatively
small in any structural sense: (a) the operator identity is exact and coupling-independent;
(b) the elastic partial-wave bound fails at leading nonvanishing order for every `s > 2M^2`,
i.e. `|S_J| > 1` for arbitrarily weak coupling on an infinite s-range, with the crossover
`s* = 2M^2` and maximum at `s = 4M^2` computable and now computed; (c) the multichannel deficit
tends to a CONSTANT (`-1/2` in gg-cut units), so the violation persists at `s >> M^2`, far
outside the resonance window where fixed-order keep-and-grade is trusted; (d) the doubled mixed
cut means branch A's single-counting table UNDERSTATED the leak by a factor of 2. If
keep-and-grade's physical content is "the free positive subspace is the physical world," that
content is dead at accessible s: probability excess from `s = M^2` on, elastic bound gone from
`2M^2` on. A harder kill of that specific reading is not available.

**Attacks on the violation (each answered):**
1. *"The free grading is the wrong physical subspace in the interacting theory."* CORRECT, and
   it is the only exit; but it is not free. It renames the physical world into the C-positive
   subspace, whose existence in QFT is unproven (branch B: QM only) and whose metric is
   provably non-local (W54). The attack does not restore unitarity on any LOCALLY definable
   physical subspace; W54's hardened audit closed the local escapes.
2. *"The odd amplitudes might vanish by a symmetry, B = 0."* Refuted by computation: the odd
   cuts are nonzero at one loop (W48/W120), at the sunset and at the genuinely overlapping kite
   (W124, `-0.0849`); and W134 (landed during this wave) COMPUTED the Stage-C expectation: the
   on-shell spin-2 cut numerator is positive semidefinite for every vertex, the `(-1)^{n_ghost}`
   parity lifts intact to spin-2, and the odd-cut leak is confirmed, not cured, at tensor level.
3. *"The ghost is unstable (Gamma/M = O(1)), so odd-ghost asymptotic states do not exist and the
   whole question is moot."* That is the LEE-WICK exit, not a defense of grading: taking it
   abandons keep-and-grade for the removal family and buys the CLOP/causality ledger (W120/W124).
   Within the graded mandate (real mass, kept), the violation stands; and by (c) above it cannot
   be quarantined inside the resonance window.
4. *"|S_J| > 1 at order g^4 might be cured at higher orders."* No: unitarity deficits cannot be
   cancelled between orders at weak coupling (the leading term dominates as g -> 0), and the
   exact identity shows the all-orders sign is fixed: `A^dag A - P_+ = B^dag B >= 0` at EVERY
   order pattern; the deficit can only grow with more open odd channels.

**Skeptic's residue (honest):** the toy is scalar with the vertex structure of a single split
propagator; a genuinely graded spin-2 theory could in principle move `s* = 2M^2` (the crossover
depends on relative residues and multiplicities), though it cannot remove the row-level excess
(exact) or the sign of `G(s)` (every odd cut is negative, every matched physical cut cancels).
The crossover VALUE is toy-grade; the existence and direction of the violation are not.

## 6. Verdict (question 4)

**VIOLATES on the free positive (physical) subspace -- exact and computed.** Exact: `A^dag A =
P_+ + B^dag B`, so physical-channel probability sums exceed 1 for every s above the first
odd-ghost threshold (`s > M^2`); the deficit operator is `B^dag B`, nonzero by the computed odd
cuts. Toy-checked: the elastic partial-wave bound `|S_J| <= 1` fails for all `s > 2M^2`,
maximally at `s = 4M^2`, tail `-M^4/s^2`; the ghost-free multichannel deficit is negative for
all `s > M^2` with limit `-1/2`.

**PRESERVED-IN: the C-metric sense only** -- full-Krein-space unitarity `S^dag eta_+ S = eta_+`
under the positive inner product `eta_+ = eta C`, demonstrated exactly in the toy to coexist
with the naive violation; in QFT conditional on the interacting C-operator (open, branch B) and
priced non-local (W54, hardened). Equivalently NARROWED-TO: physical-subspace unitarity for
keep-and-grade holds iff the physical inner product is redefined to the non-local C-metric;
on any locally-defined positive subspace it is violated at all `s > 2M^2` (elastic) and
`s > M^2` (row level).

**The interference/decay-width reading: REFUTED by sign.** The leak is probability EXCESS into
physical channels (anti-damping), not drainage into the graded sector; no open-system weaker
sense exists.

**Impact on the trade map.** The wave-1 two-currency map (grading pays positivity, removal pays
causality) is sharpened into a single mandatory purchase: the grading branch's positivity cost
is now EXACTLY the C-operator's non-locality cost, because the free-subspace reading is dead as
a matter of exact algebra plus computed nonzero odd cuts, and the C-metric reading is the unique
survivor. Branch A's one-loop "case (c) leak" is upgraded from a one-loop indication to an
exact, all-orders, sign-definite operator statement with its partial-wave footprint mapped.
The W48 gate question ("does the graded projection cancel the leak?") is ANSWERED: no
projection onto a positive subspace of the free grading can, and the only cancellation is the
C-metric's re-normalization of the ghost channel to positive probability.

## 7. What this does NOT do

No claim that keep-and-grade is dead as a THEORY: the C-metric route remains open exactly to
the extent branch B's QFT C-operator question is open; what is dead is physical-subspace
unitarity on the free grading. No spin-2 tensor numerators computed HERE; W134 (landed during
this wave) supplies the tensor-level sign lift, but the crossover VALUE `s* = 2M^2` remains
toy-grade (it depends on relative residues and multiplicities, which W134 does not fix). No resummation inside the resonance window. No statement about the
removal family beyond reproducing its preserved bound as a control. No canon / RESEARCH-STATUS
/ claim-status / verdict / posture change; **H59 remains OPEN** (status changes only via the
runbook; the settling object for H59 remains the W48 minimal source-action loop computation,
which this wave equips with its unitarity criterion: compute `B` and the C-metric, not a
subspace projection).

**Artifacts:** this file + `tests/W132_graded_optical_theorem_physical_subspace.py`
(18/18, exit 0).
