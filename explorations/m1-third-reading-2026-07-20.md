---
title: "Mannheim third reading at matrix grade: the both-modes/complex-pair construction (PRD 98 045014 + J. Phys. A 51 315302, primaries verified) transposes to the N2 crossing walls with V = K_S and the mode exchange = J_quat -- K-c FIRED: a conserved, deck-compatible indefinite pairing exists across the cone-crossing walls, degenerates to the canonical cut S = K_S e^{alpha w} on the gapped side, covers the wall itself as the Jordan case, and no conserved POSITIVE pairing exists past any wall (universal-null lemma) -- the crossing sector gains defined accounting and W172's unbroken-PT conditional retypes from wall to scheme choice (typed fork-conditional)"
status: active_research
doc_type: exploration
created: 2026-07-20
directed_by: "Joe direct chat, 2026-07-20 (parallel wave: Mannheim third reading)"
axiom: lab/process/boundary-adapter-standing-axiom.md
extends:
  - explorations/n2-end-family-2026-07-20.md
  - explorations/mannheim-pt-intake-d1-method-2026-07-19.md
inputs:
  - explorations/n2-end-family-2026-07-20.md
  - explorations/sig-b5-f2-f5-shadow-2026-07-20.md
  - explorations/f5-signed-fraction-2026-07-20.md
  - explorations/mannheim-pt-intake-d1-method-2026-07-19.md
  - explorations/W172-interacting-c-operator-nogo-2026-07-14.md
  - explorations/W169-c-operator-perturbative-construction-2026-07-14.md
  - lab/sources/claim-mining-toe-mannheim-2026-07-20.md
  - tests/channel-swings/n2_end_family_probe.py
  - tests/generation-sector/gen_sector_bridge.py
  - tests/oq_rk1_cl95_explicit_rep.py
  - GEOMETER-VS-PHYSICS-OBJECTS.md
runnable:
  - tests/channel-swings/m1_third_reading_probe.py
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# The Mannheim third reading, run against the actual N2 walls

The N2 end-family swing named its obstruction precisely: over the
degeneration rays of the faithful Y14-end model, the boundary symbol
family hits cone-crossing walls at finite collar radius -- even-dim
kernel, spectrum leaving the real axis IN COMPLEX-CONJUGATE PAIRS -- and
every off-the-shelf spectral-section theorem refuses that hypothesis. The
Mannheim claim-mining pass surfaced (rows 2.5-2.6) a spoken method for
exactly that situation: his THIRD realization of antilinear symmetry,
where a complex pair E0 +- i Gamma is not a failure of unitarity but a
regime with its own conserved accounting, provided BOTH modes are kept
and combined with a RELATIVE MINUS SIGN. This swing (i) verified the
primaries behind the transcript rows, (ii) formalized the construction at
matrix grade in the repo's Krein setting, and (iii) applied it to the
ACTUAL N2 crossing rays (same machinery, same seed, same stream -- the
same 53 crossing rays out of 200).

Receipt: `tests/channel-swings/m1_third_reading_probe.py` --
deterministic, numpy only, seeded 20260720, exit 0 -- HEADLINE
`12 [E] + 4 [F] = 16 (setup [T] = 3 excluded) ALL PASS`.

**Verdict up front: kill condition K-c fired (success).** The conserved
indefinite pairing exists across the wall, is derivable from K_S/J_quat
alone (K-a did not fire), and is deck-exchange compatible with exactly
the standing Z/2 twist (K-b did not fire). The crossing sector gains a
defined -- indefinite, both-modes -- accounting. W172's unbroken-PT
conditional retypes from wall to scheme choice, as a typed
fork-conditional only: NO claim, canon, scorecard, or posture movement.

## 1. Primary verification (done FIRST, per the mission order)

The transcript rows under verification were mining-report rows 2.5
[01:44:44-01:47:21] (keep both members of E +- i gamma; growing mode =
decay-product population; "the total population remains fixed") and 2.6
[02:10:40-02:12:47] (the resonance propagator
`1/(E-E1-i gamma) - 1/(E-E1+i gamma)` with a relative minus sign; "not a
ghost"; Lee-Wick adjacency).

**[P1] P. D. Mannheim, "Antilinearity rather than Hermiticity as a
guiding principle for quantum theory," J. Phys. A 51 (2018) 315302 =
arXiv:1512.04915 (v5 read in full, 2026-07-20).** This resolves the
mining report's named-verification fork ("likely arXiv:1512.03736 and/or
J. Phys. A 51 (2018) 315302"): the J. Phys. A 2018 paper IS the
construction paper, and its arXiv number is 1512.04915, not 1512.03736
(the latter is the CPT-theorem companion; not needed -- everything the
rows claim is in 1512.04915). The construction, verbatim from the paper:

- For an antilinear-symmetric H, eigenvalues are real or come in
  complex-conjugate pairs E = E_R +- i E_I; there is also the
  Jordan-block (exceptional-point) realization (abstract + Sec. I).
- Introduce V with V H V^-1 = H^dag (pseudo-Hermitian condition; Sec. II
  E: V H - H^dag V = 0 iff ALL V-inner products <R_j(t)|V|R_i(t)> are
  time independent -- eqs (25)-(26); left-eigenvectors <L| = <R|V).
- The complex-pair block, worked exactly (his M(s<1) example, eqs
  (8)-(9)): with sinh(beta) = nu/s, the V-operator and right-eigenvectors
  u+ (growing, E = 1 + i nu) and u- (decaying, E = 1 - i nu) obey

      u+^dag V u+ = 0,   u-^dag V u- = 0      (each member SELF-NULL),
      u-^dag V u+ = +1,  u+^dag V u- = -1     (cross, RELATIVE MINUS),
      u+ u-^dag V - u- u+^dag V = I           (closure).

- The paired propagator (eqs (10) and (13)):

      D(E) = 1/(E-(E0-iGamma)) - 1/(E-(E0+iGamma))
           = -2iGamma/((E-E0)^2 + Gamma^2),

  sign-definite at real E, "the interpretation of D(E) as a probability
  is thus the standard one that is associated with decays"; and the text
  states the both-modes mechanism exactly as the transcript row has it:
  "the only allowed transitions being between the decaying and growing
  states... as the population of state |A> decreases that of |B>
  increases in proportion. Thus despite the presence of the growing
  state <B|, the <B|A> transition matrix element never grows in time."
  The paper itself names the Lee-Wick antecedent ("the Lee-Wick analysis
  of the complex conjugate pair realization of the Lee model") --
  confirming row 2.6's "Leon Wick" as Lee-Wick, as the mining report
  suspected.
- One convention fact the transcript could not show: V in the
  complex-pair regime (eq (8)) is ANTI-Hermitian (machine-checked in the
  probe). With a HERMITIAN fundamental symmetry -- our K_S -- the same
  normal form has cross-pairings +-i r instead of +-1. One factor of i
  of bookkeeping; located, stated, and carried through the probe.

**[P2] P. D. Mannheim, "Unitarity of loop diagrams for the ghostlike
1/(k^2-M1^2)-1/(k^2-M2^2) propagator," Phys. Rev. D 98 (2018) 045014 =
arXiv:1801.03220 (read in full, 2026-07-20).** The mission's "arXiv
~1804.xxxxx" resolves to 1801.03220. Field-grade content verified: the
propagator is the LEFT-RIGHT vacuum object
i<Omega_L|T(phi phi)|Omega_R> = i<Omega_R|V T(phi phi)|Omega_R> (eq (7)),
and the relative minus sign is generated BY the V insertion, "not
through any negative norm properties of the states"; V H - H^dag V = 0
makes the V-norms time independent (eqs (33)-(34)); pseudo-unitarity
U V^-1 U^dag V = I (eq (37)), S V^-1 S^dag V = I (eq (38)); all cut
lines have positive norm (eq (31) region); negative-signatured loop
discontinuities are cancelled by V-dependent TREE-graph contributions
("an effect that is foreign to standard Hermitian theories"). This is
the same paper the D1 build already cited for tree-cancellation; what is
new here is consuming its V-formalism as the field-grade template of the
both-modes accounting.

**Fidelity receipt.** The probe's first [E] reconstructs [P1] eqs
(8)-(13) machine-exactly (V anti-Hermitian; self-null; +-1 cross;
closure = I; the reconstructed H satisfies V H V^-1 = H^dag with
eigenvalues 1 +- i nu; the -2iGamma Lorentzian on an E-grid; time
independence of all pairings while the members grow/decay). The
construction is verified FROM THE PRIMARY, not from the transcript.
Verification status of the transcript rows: 2.5 and 2.6 both
PRIMARY-CONFIRMED (with the two citation corrections above).

## 2. Pre-declared kill conditions (stated before the run)

- **K-a:** the construction requires structure GU's Krein setup cannot
  supply (a preferred positive pairing, or an extra antilinear choice
  not derivable from K_S/J_quat) -> the wall is CONFIRMED SHARPER; W172
  stands.
- **K-b:** the pairing exists but breaks deck-exchange/holonomy
  compatibility -> third reading incompatible with the carrier;
  construction-local no-go.
- **K-c (success):** conserved pairing exists, deck-compatible -> the
  crossing sector gains defined accounting; W172 retypes from wall to
  scheme choice (typed fork-conditional; no claim/canon movement).

**Which fired: K-c.** Clause-by-clause receipts in Section 4.

## 3. The construction (the transposition, object by object)

GEOMETER-VS-PHYSICS-OBJECTS discipline: every identification named, no
silent positivity anywhere (the one positivity-adjacent statement is a
NEGATIVE theorem -- see the universal-null lemma).

| Mannheim object | GU object | Status |
|---|---|---|
| V with V H - H^dag V = 0 | **K_S itself**: the family D(t,s) is K_S-self-adjoint, so K_S D - D^dag K_S = 0 is [P2] eq (34) verbatim with V = K_S | PROGRAM-NATIVE; no new operator introduced |
| antilinear symmetry pairing the modes | **J_quat = C_J o conj**: J^2 = -I, commutes with K_S and with the Clifford action; maps each complex half onto its conjugate half | PROGRAM-NATIVE; the exchange is supplied, not chosen |
| the u+/u- pair | the spectral halves E_{+i g}, E_{-i g} of D past a wall (D^2 = q I, q < 0, g = sqrt(-q)); partner fixed by the SVD of the K_S cross-Gram | derivable from {D, K_S} alone |
| "keep both modes" | keep BOTH halves with the conserved pairing x^dag K_S y; nothing discarded, no positive metric asserted | the only conserved option -- universal-null lemma |
| his +-1 cross-normalization | +-i r cross-residues (r = the uniform pairing weight) | the anti-Hermitian-V vs Hermitian-K_S convention |
| the exceptional point / Jordan block ([P1] eqs (6)-(7)) | the wall point itself: D^2 = 0, Ker D = Range D, 64-dim K_S-null kernel | the wall is [P1]'s Jordan case, exactly |

The evolution used throughout is the symbol-grade U(tau) = exp(-i D tau)
in its closed form U = C(q,tau) I - i S(q,tau) D with C, S ENTIRE in q
-- one formula covering gapped (cos/sin), crossed (cosh/sinh), and wall
(I - i tau D) regimes. "Conserved" means: U^dag K_S U = K_S exactly, on
all three regimes ([P2] eq (37) with V = K_S).

## 4. Results (all on the actual N2 objects; walls at the actual rays)

The test bed: the n2 probe's end-model machinery replicated verbatim,
same seed AND same RNG stream, so the seeded sweep reproduces the n2
catalogue exactly -- 132 gapped / 53 cone-crossing / 0 timelike / 15
undecided ([T] receipt). Deep checks run at the conf-down wall
(s* = 0.0585 at t* = 0.575, q: +3.53 -> -47.75 across it), the boost
wall, and three sweep crossing rays.

**(a) The conserved pairing exists across the wall, K_S-compatibly --
and it is the ONLY kind that can.** V = K_S satisfies Mannheim's
pseudo-Hermitian condition on the whole family; exp(-i D tau) is
K_S-pseudo-unitary on both sides of the wall and at it. New two-line
theorem, machine-checked at the actual crossing (the UNIVERSAL-NULL
LEMMA): if V D = D^dag V and D x = lam x, D y = lam y with lam nonreal,
then (lam - conj(lam)) x^dag V y = 0, so EVERY conserved pairing is
exactly null on each complex half. Consequences: (i) no conserved
positive-definite pairing exists past ANY wall, for any scheme -- W172's
"broken PT => no positive C-metric" is confirmed and UPGRADED from the
C-operator family to all conserved pairings; (ii) every conserved
accounting past the wall is both-modes-shaped (self-null + cross). The
n2 K-nullity little theorem is the V = K_S instance.

**(b) The both-modes normal form holds at the actual walls.** At five
crossing walls: halves exactly K_S-null; cross-Gram nondegenerate with
ALL 64 singular values EQUAL (quaternionic uniformity; r = 0.5810
conf-down, 0.7265 boost, 0.6755/0.6557/0.6779 sweep rays). In the
Mannheim gauge the cross-residues are -+i r: residues conjugate with the
relative minus realized, self-residues zero, and the paired two-point
function w^dag K_S (E-D)^-1 w is REAL on the real axis and exactly the
Lorentzian 2 r Gamma/(E^2 + Gamma^2) of width Gamma = sqrt|q| -- [P1]
eq (13) transposed. Population accounting: the growing member's Dirac
norm inflates as e^{2 Gamma tau} while every K_S pairing is exactly
constant -- the transcript row's "total population remains fixed,"
machine-realized. J_quat maps the growing half onto the decaying half,
and the composite bilinear form B(x,y) = (Jx)^dag K_S y is ANTISYMMETRIC
and nondegenerate -- a symplectic (Kramers) structure on the growing
half; this is why the J-partner itself pairs to zero and the Mannheim
partner is the pairing-canonical (SVD) partner.

**(c) The wall itself is [P1]'s Jordan-block case.** At the exact-null
representative of the actual collision direction: D^2 = 0 with rank
exactly 64, Ker D = Range D, kernel exactly K_S-null AND K_S-orthogonal
to the range (the zero-norm states of the equal-frequency PU case), and
K_S pairs the kernel with a complement ISOMETRICALLY (all 64 singular
values = 1.000000). The Jordan evolution I - i tau D grows states
linearly while every pairing stays constant -- [P1] eqs (6)-(7): "despite
the presence of terms linear in t, their overlap is time independent."

**(d) Continuity in the collar -- and an exceptional-point collapse law
(new finding).** The evolution is entire in q; q(s) passes through the
wall with equal two-sided slopes (63.5/63.7); U is Lipschitz through the
wall. Meanwhile BOTH normalized mode structures collapse AT the wall,
symmetrically: the canonical-cut margin sech(alpha) from the gapped side
(0.661 / 0.209 / 0.066 at delta = 0.2 / 0.02 / 0.002) and the normalized
cross-pairing weight r from the crossed side (0.508 / 0.202 / 0.066 at
the same deltas). The matched values are not a coincidence to leave
lying around: they suggest r and the margin are two costumes of ONE
collapse rate at the exceptional point (a named short computation --
open). So: the conserved accounting (pairing + evolution) crosses the
wall; the MODE NORMALIZATION is singular exactly at it -- which is
[P1]'s own structure: the exceptional point is where the complex-pair
realization hands over to the Jordan realization.

**(e) Deck-exchange compatibility (K-b clause).** U_h is a Hermitian
unitary involution; transporting the pairing around the mixed loop gives
U_h^dag K_S U_h = -K_S EXACTLY: the datum returns to MINUS itself -- the
SAME Z/2 twist as the two-section exchange and the signed-C2 flip (same
U_h, same character), returning to +K_S on the double cover. The seam
identity holds at crossing radii and U_h maps each complex half of
D(0,s) onto the same-eigenvalue half of D(1,s). The same-sign-plane seam
(four K_S factors, even) preserves the pairing exactly -- the trichotomy
transfers. Verdict: not a breakage; the both-modes datum is a
section-like object twisted by the KNOWN character.

**(f) Section-like coverage where the cut has holes.** At a crossing
radius the loop crosses the null cone for an open t-interval (41% of the
loop at s*+0.4 on the conf-down ray): there the canonical cut is
UNDEFINED (the n2 t-holes), yet the conserved-pairing datum is defined
at EVERY t. And on the gapped side the pairing datum is not a rival
structure: sign-diagonalizing K_S on the D-eigenspaces REBUILDS the
canonical cut, machine-equal to the f5 closed form S = K_S e^{alpha w}
at the base point and on the crossing ray's gapped side. One datum,
three regimes: definite blocks (= the canonical cut) on the gapped side,
the Jordan pairing at the wall, null-halves-plus-cross past it.

## 5. What this does to W172, the null-cone findings, and the section
theory

**W172 (the unbroken-PT conditional).** W172's verdict was
OPERATIVE-CONDITIONAL-ON-UNBROKEN-PT: if dynamical PT breaking closes
(physical-sheet complex pair), then no positive C-metric, no C-operator,
NOT-OPERATIVE -> engine reframe. This swing does not touch the
dynamical question (whether the pole reaches the physical sheet -- H59's
open object), and the universal-null lemma CONFIRMS the positive-metric
half at full strength. What retypes is the MEANING of the broken-PT
branch: "no positive C-metric" no longer implies "no conserved
accounting." The fork is now:

- **Scheme P (positive-metric / C-operator):** requires unbroken PT;
  dies at the wall; W172's wall reading is correct FOR THIS SCHEME.
- **Scheme M (both-modes indefinite):** requires only conserved
  NONDEGENERACY; survives the wall with the normal form above; [P2]
  supplies the loop-level implementation in the worked cousin theory.

So "broken PT" retypes from terminal wall to scheme choice -- a TYPED
FORK-CONDITIONAL. Conditions attached: (i) the ontology guard of the
intake doc stands (Mannheim eliminates ghosts by reinterpretation; GU's
mirror half is real and causality-required -- technology import only);
(ii) the transfer is matrix/symbol grade; the field-grade lift of
scheme M for GU is untouched (it is [P2]'s content for HIS theory, not
ours); (iii) the decay-vs-anti-damping ORIENTATION is a gauge at matrix
grade (probe [F] receipt) -- W172's anti-damping sign finding is
operator-grade data and stays exactly as filed. Nothing in W172's text
needs to move; this files alongside it. If the H59 computation later
lands broken-PT, the follow-on question is no longer only "engine
reframe?" but "engine reframe, or scheme-M accounting?" -- both typed,
neither canon.

**The null-cone findings (sig-b5 F2/F5 shadow + n2).** "Outside the
spacelike sector the accounting is UNDEFINED" sharpens to: the CUT-level
accounting is undefined (correct, unchanged -- and now theorem-backed by
the universal-null lemma: no K-definite cut CAN exist there), while a
pairing-level conserved accounting exists and is nondegenerate. The
sector-relative verdict stands; the crossing sector is no longer
structureless. NOT claimed: any extension of the signed functional
k_sigma past the wall (k_sigma consumes the cut Q_sigma; whether a
pairing-level zero-sum analog exists is a named open computation).

**The section theory (N2's one undetermined clause).** The n2 doc left
the sector-relative spectral-section conjecture with exactly one
undetermined clause: "controlled behavior at the cone-crossing walls."
This swing supplies a candidate form for that clause: sections carry the
canonical cut on the gapped sector; at a wall the cut's margin and the
normalized cross-weight collapse at matched rates (the EP law); ACROSS
the wall the section datum continues NOT as a cut but as the conserved
K_S pair-block pairing with the Jordan normal form at the wall and the
both-modes normal form past it, deck-twisted by the standing Z/2. A
Melrose-Piazza-shaped statement would then read: "Krein-compatible
spectral sections relative to the spacelike sub-end, with both-modes
pairing data at the walls." That is a conjecture clause, not a theorem;
but the finite content on both sides AND AT the wall is now computed.

## 6. Council pass (inline, five lenses)

- **PT-quantum theorist (fidelity to Mannheim's actual construction):**
  the import is faithful where it claims to be: eqs (8)-(13) are
  reconstructed digit-exact including the anti-Hermiticity of his V in
  the complex-pair regime, the closure relation, and the propagator
  identity; the transposition correctly maps V -> K_S via eq (34) and
  reproduces self-null/cross/relative-minus/conserved-populations. Two
  deviations, both named: the Hermitian-K_S convention moves his +-1 to
  -+i r; and his +1 normalization of the cross-pairing is absorbed into
  a per-pair gauge that GU's matrix grade cannot fix (his is fixed by
  the dynamics of specific solutions). What the import does NOT bring:
  his C operator (none exists here past the wall -- consistently), his
  vacuum/in-out structure, and his tree-cancellation mechanism (needs
  field grade). Fidelity grade: construction-faithful, scope-honest.
- **Krein analyst (what is derivable from K_S/J_quat alone):**
  everything load-bearing: V = K_S is forced by K_S-self-adjointness of
  the family; the halves and their nullity are spectral facts; the
  partner map is the SVD of the K_S cross-Gram ({D, K_S} only); J_quat
  supplies the antilinear exchange and the symplectic composite; the
  universal-null lemma needs only V D = D^dag V. NOTHING requires a
  positivity posit -- and the lemma proves none is available. The one
  discretionary item is the per-pair phase gauge, which is exactly the
  freedom Mannheim's dynamics fixes and our matrix grade honestly
  cannot. K-a is cleanly discharged.
- **Spectral geometer (does the datum glue -- the section-theory
  consequence):** the datum now glues over MORE of the family than the
  cut ever did: it is defined at every (t,s) sampled including walls and
  crossed t-intervals, transports under the deck with the known
  character, and restricts to the canonical cut on the gapped sector.
  What is NOT established: a global continuity/classification THEOREM
  (the collar samples are finite; the EP collapse law is measured at
  one wall family); and no K-group or index statement anywhere. The
  right next object is the wall-behavior clause written as a normal-form
  condition (Section 5) inside the sector-relative conjecture. Grade:
  existence-side narrowing at truncated-real grade; theorem side
  untouched -- same honest posture as n2.
- **Numerical analyst (collision-neighborhood conditioning):** the
  dangerous zone is the EP, where eigenprojections blow up; the probe
  never diagonalizes near it -- it uses the closed-form projectors
  (D^2 = q I), the entire-in-q evolution (series vs closed forms at
  1e-15), and an exact-null representative (|q| < 1e-14 relative) for
  the wall. Conditioning receipts: cross-Gram singular values equal to
  1e-8 relative; complement pairing sv = 1 to 1e-6; continuity checks
  run on gauge-invariant quantities only, because the replicated n2
  frame machinery carries a per-s cluster gauge with isolated s-spikes
  (found during this build; the n2 probe consumed no s-continuity of
  its gauge, so nothing upstream is contaminated -- but any future
  collar-continuity work should know those spikes exist).
- **Adversarial referee (attack: success by redefinition-by-relabeling
  -- answered in writing):** The charge: "You renamed K_S 'the both-modes
  pairing' and declared victory; K_S-pseudo-unitarity was always true,
  so K-c was unfalsifiable." Answer: (1) K-c was falsifiable and K-a/K-b
  were live: the construction could have needed an antilinear datum
  beyond J_quat (it measurably does not -- J commutes with K_S and the
  Clifford action, neither of which was guaranteed), the cross-Gram
  could have been degenerate or non-uniform (measured nondegenerate,
  exactly uniform), and the deck could have broken the pair blocks
  (measured: maps halves eigenvalue-exactly). (2) The content beyond
  relabeling is the NORMAL FORM PACKAGE at the actual walls: self-null +
  uniform-cross + relative-minus residues + Lorentzian width sqrt|q| +
  Jordan isometric pairing at the EP + the matched margin/r collapse law
  -- none of which is the statement "K_S is conserved." (3) The
  universal-null lemma is a genuine theorem-shaped narrowing: it kills
  every positive-scheme rescue attempt at once, which is a RESULT about
  the wall, not a relabel. (4) Conceded to the attack, in writing: the
  phrase "defined accounting" must not be oversold -- what is defined is
  a conserved nondegenerate pairing with a normal form; no probability
  INTERPRETATION is derived (the orientation gauge [F] check exists
  precisely to keep that honest), and the F5 signed functional is NOT
  extended past the wall. With those concessions the verdict stands:
  K-c, scoped.

## 7. Typed claims

- Universal-null lemma (any conserved pairing is null on each nonreal
  half; no conserved positive pairing past a wall): **NATIVE-DERIVED
  (paper grade, two-line proof, machine-checked on a conserved-V
  family at the actual crossing).**
- Both-modes normal form at the N2 walls (self-null halves, uniform
  nondegenerate cross-Gram, Mannheim-gauge residues -+i r, Lorentzian
  pair propagator, conserved populations): **NATIVE-PROVEN (matrix
  grade, five actual walls).**
- Wall = Jordan case (rank-64 nilpotent, Ker = Range, K-null kernel,
  isometric complement pairing, conserved linear-growth overlaps):
  **NATIVE-PROVEN (matrix grade, exact-null representative of the
  actual collision).**
- Deck compatibility with the standing Z/2 twist; gapped-side
  degeneration to S = K_S e^{alpha w}: **NATIVE-PROVEN (matrix grade;
  f5 closed form reproduced at 1e-15).**
- The EP collapse law (margin and cross-weight -> 0 at matched rates):
  **NATIVE-PROVEN (measured, one wall family); mechanism/closed form
  OPEN (named).**
- W172 retype (wall -> scheme choice) and the section-theory wall
  clause: **typed fork-conditional / conjecture clause respectively --
  R0_COND working grade; no claim movement.**

## 8. Receipts

- Probe (deterministic, numpy only, seeded 20260720, exit 0):
  `tests/channel-swings/m1_third_reading_probe.py` -- HEADLINE
  `12 [E] + 4 [F] = 16 (setup [T] = 3 excluded) ALL PASS`.
- Primaries: arXiv:1512.04915 v5 (= J. Phys. A 51, 315302) and
  arXiv:1801.03220 (= PRD 98, 045014), both read in full 2026-07-20;
  eqs (6)-(13), (25)-(26) of [P1] and eqs (7), (31), (33)-(38) of [P2]
  consumed; [P1] eqs (8)-(13) machine-reconstructed in-probe.
- Test bed: the n2 end-family machinery replicated verbatim (same seed,
  same stream; sweep counts 132/53/0/15 reproduced in-probe); anchors
  xi(0,0) = XI and C2 = 155.3625 reproduced; K_S/J_quat conventions
  identical to the n2/f2/f5 probes.
- Consumed as regression targets, not re-derived: the n2 K-nullity
  little theorem; the f5 canonical-cut closed form S = K_S e^{alpha w}
  (reproduced at 8.9e-16 / 4.4e-15).
- Construction discipline: `GEOMETER-VS-PHYSICS-OBJECTS.md` -- the
  standard positive-Hilbert fork recorded (K-indefinite on its range;
  supplies no conserved positive pairing -- probe [F]); killed list
  honored (no positive-Hilbert default, no index reading, C2 untouched).
- Intake lineage: `explorations/mannheim-pt-intake-d1-method-2026-07-19.md`
  (realizations 1-2 already absorbed there; this swing is realization 3
  ONLY -- no duplication; the intake's ontology guard carried forward).

## 9. Boundary

Exploration tier under the standing axiom, R0_COND working grade (except
the universal-null lemma and the [P1] reconstruction, which are
unconditional algebra). Matrix/symbol grade throughout: no operator on
the end, no L^2/Fredholm theory, no field-grade lift of scheme M, no
in/out states -- the N2 theorem remains the missing object, unchanged in
location. NOT done, named: the decay-vs-anti-damping orientation (gauge
at this grade; operator-grade data); any extension of the F5 signed
functional k_sigma past the wall; the closed form of the EP collapse law;
the sector-relative conjecture's wall clause as a precise statement
(candidate form written, Section 5). Nothing here moves claim status,
canon verdicts, scorecard rows, N-accounting, or public posture; the
bit's VALUE remains externally posited (p2c-owned); W172's text is
untouched (this doc files a typed fork-conditional alongside it); H59
remains OPEN; no cross-owner writes; no external actions. Next rungs in
order of exposure: (i) state the sector-relative conjecture with the
both-modes wall clause; (ii) derive the EP collapse law (margin vs r --
one rate or two); (iii) the pairing-level zero-sum question for F5;
(iv) H59's W48 settling computation, now with the scheme fork typed on
its broken-PT branch.
