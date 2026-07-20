---
title: "Conditional forcing resolved (outcome C-b, sharpened): the order-3 count IS forced given one explainable external input -- and the minimal input is ONE ORDER-SIX PHASE REFERENCE (Z/6 = the payload bit x one trit anchor); the bit alone is provably insufficient (it is exactly the CUBE of the thing that is enough), the bit + one generic reader operator passes both admission gates yet fails on class stability, and the full quaternionic torsor identification (X2) suffices but is NOT minimal"
doc_type: conditional_forcing_minimal_input
status: exploration tier; ladder complete X0/X1/X1.5/X2 + minimality; probe exit 0
created: 2026-07-20
directed_by: "Joe direct chat, 2026-07-20 (successor line: conditional forcing / minimal input)"
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
target: "Joe's question, verbatim intent: 'Is it FORCED, using the arena of Geometric Unity, if we knew what the input is? What IS that input, that single bit? Could we say forced, with a reasonably explainable input from outside the geometry?' Formalized: characterize the MINIMAL EXTERNAL INPUT X such that (GU frozen inventory) + X passes the reframe pass's two-gate admission test (G1 reach the commutant; G2 nondegenerate on the K_S-confined habitat) and pins the degree condition (deck co-flip admissibility; 3 not | c; k = 64c bookkeeping)."
probe: tests/channel-swings/conditional_forcing_probe.py
related:
  - explorations/verdict-generations-transport-line-closed-2026-07-20.md
  - explorations/k1-reframe-pass-2026-07-20.md
  - explorations/torsor-k-sequence-2026-07-20.md
  - explorations/phase0-torsor-identification-tree-2026-07-20.md
  - explorations/torsion-generation-arena-2026-07-20.md
  - explorations/verify-torsion-arena-2026-07-20.md
  - tests/channel-swings/k1_reframe_probe.py
  - tests/channel-swings/phase0_torsor_checks.py
sources:
  - "P. Olum, 'Mappings of manifolds and the notion of degree' (Ann. of Math. 1953) -- degrees of maps of lens spaces inducing multiplication by r on pi_1 are constrained to r^2 mod n; both generators of the Z/3 give r^2 = 1 mod 3, so the trit anchor needs no orientation choice."
  - "Borsuk-Ulam, two uses: odd maps S^3 -> S^3 have odd degree (deck admissibility pins parity only); no continuous odd map S^3 -> S^1 exists (every weight-blind deck-odd oracle is singular)."
  - "Torsion-arena bookkeeping k = 64c, order(J(k)) in Z/24, sustained twice (b97b798 / 8d000ac)."
---

# Conditional forcing: the minimal external input X

Successor line to the ratified closure of the native-transport question
("located, not forced" within the frozen inventory). Everything here sits on
the framed-reading fork (R0_COND) and the (9,5) H-class conditionality, at
exploration tier, with no claim/canon/posture movement. Probe:
`python tests/channel-swings/conditional_forcing_probe.py` -- ALL PASS,
10 [E] + 2 [F] (setup [T] = 3), exit 0, ~265 s, deterministic; it re-runs the
full closed-line battery (`k1_reframe_probe.py`, which itself re-runs
`phase0_torsor_checks.py`) live inside itself, so every X0 receipt and every
power certificate of the degree counter is refreshed in the same run that
reads the new verdicts.

**Outcome condition fired: C-b, sharpened.** X2 suffices and X1 provably does
not -- and the minimality analysis lands STRICTLY BETWEEN the charter's rungs:
X2 (the full quaternionic torsor identification) is sufficient but not
minimal; the minimal X is one order-six phase reference, of which the payload
bit is exactly the cube.

## 1. The formal statement being certified

Fix the frozen inventory (the (9,5) spine, the record kernel K_S, the
quaternionic commutant Sp(1)_comm = {alpha I + beta J}, the two habitat pins,
the spin-lift family with verified co-flip deck -I). An external input X
FORCES the order-3 count iff inventory + X admits a transport that passes:

- **G1 (reach):** genuinely moves the Sp(1)_comm direction (for kernels:
  non-H-self-adjoint dressing with nonzero commutant columns);
- **G2 (habitat):** stays nondegenerate on the K_S-confined sector;
- **deck admissibility:** exact co-flip q(-v) = -q(v);
- **class stability:** a Psi_0-independent (and oracle-generic) degree c;
- **count:** 3 not | c, whence k = 64c has k mod 24 in {8, 16} and
  order(J(k)) = 3 exactly.

Setup fact (probe [T], exact): order(J(64c)) = 3 iff 3 not | c and = 1 iff
3 | c, for all |c| <= 60; both honest-+- twins (8 and 16 mod 24) are order 3.
So THE ENTIRE COUNT CONDITION IS A MOD-3 STATEMENT ON THE CLASS; deck
oddness is a separate parity (admissibility) demand. These two independent
demands are exactly what the minimal X must supply -- nothing else.

Second setup fact (exact, new here): K_S twisted-commutes with C at 0.0, so
the commutant preserves BOTH confined sectors and its Gram on confined states
is exactly orthonormal. For oracle-type transports (maps into the commutant),
G2 is therefore satisfied BY IDENTITY -- the habitat obstruction that killed
every frozen kernel does not exist on the commutant side of the bridge. The
whole battle is G1 + class stability.

## 2. The ladder

### X0 = nothing -- INSUFFICIENT (cited, not re-litigated)

The ratified closure, re-run live (k1 exit 0 inside this probe): four native
routes dead on pre-declared conditions, self-dual degrees scatter over
{-1, +1, +3, +5} with the fixture, no frozen kernel passes both gates.

### X1 = the payload bit alone -- INSUFFICIENT, as its own theorem (three legs)

The sharpest formal answer to "could the single bit do it?": no, and the
failure is structural, not evidential.

- **Leg A (kernel reading; gates are orientation-invariant).** Add an
  oriented K_S -- both orientations sigma, and both pin-plane dual
  orientations tau. Every dressing constructible from inventory +
  oriented-K_S has IDENTICAL gate verdicts under all four sign decorations:
  grade-1 kernels stay exactly H-self-adjoint (G1 fail); the self-dual
  bridge stays rank EXACTLY 2 on the confined sector of EITHER orientation
  (G2 fail). Flipping the bit only renames which sector is called "+". A
  Z/2 acts on the inventory by relabeling; zero/nonzero and rank conditions
  are Z/2-blind.
- **Leg B (the class is bit-blind).** K_S-orientation flip composes the
  transport with the antipodal map of S^3, which has degree +1: the degree
  is UNCHANGED (witnessed: -1 -> -1). Dual-orientation flip reflects the
  three imaginary commutant coordinates: the degree only negates
  (-1 -> +1). The fixture scatter is untouched. The oriented bit selects
  nothing the un-oriented inventory did not already have.
- **Leg C (map reading; the bit as deck constraint).** Even granting the
  bit its strongest reading -- a constraint on oracle maps (exact co-flip)
  -- the type still contains order-KILLING members: the join map
  (z1^3, z2) is exactly deck-odd with certified degree +3, so k = 192 = 0
  mod 24, order 1. Deck-oddness pins parity only; it cannot see mod 3.

This is the formal content of "the Z/2 shadow is rep-weight-blind": the
phase0 plant passed the shadow while blind, and here the entire Z/2 orbit
of the inventory carries no new forcing power.

### X1.5 = the bit + one generic reader operator -- INSUFFICIENT (and the failure is sharp)

The charter's intermediate candidate: a single non-quaternionic consumer
operator R (the S-matrix consumer-current shape), dressing the frozen record
legs as M_i = K_S e_i R. Finding, in two halves:

- **The reader passes BOTH admission gates** -- strictly further than any
  frozen kernel ever got: non-H-self-adjoint (defect > 0.3), commutant
  columns O(0.1) on confined states (G1), and confined-habitat bridge rank
  4 (G2) -- no parity identity protects the habitat against a generic
  external operator (the K_S-parity collapse was a theorem about the frozen
  pin-duals, not about external dressings).
- **But the class is fixture noise INCLUDING the zero class.** Witnessed
  degrees across readers x pins x draws: {-1, +1, +3}, target-consistent at
  every point, with c = +3 on a FULLY GENERIC Gaussian draw (not a tuned
  state; a 43-run scout sweep across 3 readers, 2 pins, generic/confined/
  sparse states witnessed exactly this set). 3 | 3 gives k = 192, order 1:
  the type straddles order-delivering and order-killing members with no
  Psi_0-independent selection.

A reader can READ the commutant -- both gates -- but cannot SELECT the
transport class. Class stability is the deep obstruction, and it is the
one thing no state-dependent bilinear construction supplies.

### X2 = the bit + the torsor identification -- SUFFICES

The oracle: an Sp(1)-equivariant trivialization of the fiber-core double
cover against the commutant (the demand item from the torsion arena, whose
Z/2 shadow was already verified). Constructed explicitly at fixture grade:

- **Classification.** Equivariance Phi(p v) = p Phi(v) forces RIGHT
  TRANSLATION Phi(v) = v * q0 (quaternion associativity; defect exactly
  0.0 on dyadic samples; a non-translation breaks equivariance at O(1)).
  The oracle's ENTIRE content is one unit quaternion q0 -- one quaternionic
  phase reference, the bit's big brother. The deck co-flip is automatic
  (exactly 0.0): the bit is already inside X2.
- **G1.** The oracle transport genuinely moves the commutant direction:
  J/iJ reach >= 0.90 over the fiber, overlap with J.psi >= 0.80 on confined
  states -- in exact contrast to the closed line's posit-free survivor
  u = I (reach 0, degree 0). The oracle supplies precisely the missing
  point of the coset that K1's conservation rule located but could not
  select.
- **G2.** By identity (setup fact): the commutant preserves both confined
  sectors and acts with exactly orthonormal Gram there. No tuning.
- **The class.** deg(v -> v*q0) = +1 for three generic q0 AND both payload
  orientations +-q0, two regular values each: oracle-choice-independent
  (right translations are all homotopic) and state-free (no Psi_0 appears
  anywhere in the construction). c = 1: odd, 3 not | c, k = 64 = 16 mod
  24, order(J) = 3 exactly; the honest-+- twin (8 mod 24) is also order 3,
  so even the surviving orientation freedom cannot touch the count.

**GU frozen inventory + X2 => the order-3 count is FORCED** (fixture grade,
R0_COND, (9,5) H-class).

## 3. Minimality: X2 is sufficient but NOT minimal

Because the count condition is a mod-3 statement and admissibility is a
parity statement, the natural probe of minimality is the EQUIVARIANCE
LADDER: how small can the matched symmetry group of the phase reference be?
For each finite cyclic Gamma inside the fiber's rotations, matched to the
canonical Gamma of scalar phases in the commutant, the Gamma-equivariant
oracle type has its degrees pinned to r^2 = 1 mod |Gamma| (lens-space degree
theory, Olum; verified at fixture grade on every rung):

- **Z/2 (the bit alone): FAILS.** Degree +3 member witnessed (X1 leg C).
- **Z/3 (the trit WITHOUT the bit): FAILS,** for the other reason: the
  equivariant member (z1^4, z2) has deck parity broken at O(1) --
  inadmissible on the verified double cover -- even though its count side
  is harmless (64*4 = 16 mod 24). The bit is independently necessary for
  ADMISSIBILITY.
- **Z/4 (the bit + one more bit): FAILS.** The deck-odd Z/4-equivariant
  member (z1^9, z2) has certified degree +9; 3 | 9 gives k = 576 = 0 mod
  24, order 1. Two bits cannot see mod 3 (9 = 1 mod 4 but 0 mod 3).
- **Z/6 = Z/2 x Z/3 (the bit + one trit anchor): SUFFICES.** Generic
  members have degree +1; the strictly-Z/6 twisted member (z1^7, z2)
  (Z/6-equivariant at 1e-15, NOT U(1)-equivariant, defect O(1)) has
  certified degree +7: the class MOVES within the type but stays = 1 mod 6,
  so EVERY member is odd with 3 not | c -- order 3 forced across the whole
  type, not just at a chosen member.
- U(1) and Sp(1) (= X2) pin the class to exactly +1 -- MORE than the count
  needs. The count needs only the residue.

**The minimal X, formally:** one Z/6-equivariance datum -- an order-six
rotation axis on the internal fiber, declared to wind in step with the
canonical sixth roots of unity in the commutant scalars. Its CUBE is the
payload bit (deck admissibility); its SQUARE is the trit anchor (mod-3
count). By Olum's r^2 pinning, both generator matchings of the Z/3 give
r^2 = 1 mod 3: the trit anchor needs NO orientation choice -- an unoriented
axis suffices. Nothing below Z/6 works; the subgroup lattice between X1 and
X2 is exhausted (Z/2, Z/3, Z/4 fail; Z/6 is the first sufficient rung).

Connection to N4 (the two frozen Z/3s, 4f5a44c): the commutant-side Z/3
used here is the canonical cube-root-of-unity subgroup of the frozen scalar
phases -- native. The fiber-side Z/3 action and its matching to the scalars
is the external part. Whether N4's identified pair can be read as already
supplying one side of this matching is a natural successor question; it is
NOT asserted here.

## 4. The plain-English deliverable

**What X is.** The universe's geometry, in GU's frozen arena, already
contains the three-ness: an order-3 class sits located in its torsion
bookkeeping, twice verified. What the geometry cannot do from the inside is
line up its internal fiber with that class -- it hands you the dial but no
zero-mark. The minimal external input X is ONE PHASE ANCHOR OF ORDER SIX on
the internal fiber: a single axis of internal rotation, declared to wind in
step with the geometry's own six-fold phase. That anchor's square is a
three-fold reference (which pins the count) and its cube is a single +-
sign (which makes the transport admissible on the double cover). The
"single bit" Joe asked about is real and necessary -- but it is exactly the
cube, the Z/2 shadow, of the thing that is enough. Anything that supplies
the full anchor -- an observer's reference frame, a boundary condition
imposed from outside the geometry, the source action's choice of phase
convention -- makes the count of exactly three unavoidable: every admissible
transport then has degree = 1 mod 6, hence k = 16 mod 24, hence order
exactly 3. And notably, a device that merely READS the geometry (one
external consumer/reader operator, the S-matrix consumer-current shape)
gets through both admission gates and still fails: reading is not anchoring.

**What X being external MEANS (typed honestly).** This is a conditional
statement, not a metaphysical one: "inventory + anchor => three," with the
anchor's necessity proven downward (bit alone: no; bit+bit: no; trit alone:
no) and its sufficiency proven upward (Z/6, U(1), Sp(1): yes). X is typed
as an EXTERNAL REFERENCE DATUM -- not a hidden variable (it carries no
dynamics and no state; any generic anchor of the type gives the same count,
so nothing about its particular value is observable in the count) and not a
boundary condition in the dynamical sense (nothing evolves toward it). It
is the same species of datum as the pairing-family externality already on
the books: a convention-anchor that four independent programs each found
they could not generate internally and each must import exactly once. That
convergence -- independent constructions repeatedly demanding one external
phase-matching of the same small size -- is the observer-convergence theme
in its sharpest form to date: the geometry is one anchor short of forcing
its own generation count, and provably not less than one.

## 5. Five-lens council (answered in writing)

**Representation theorist (the oracle constructions).** The classification
is airtight at its grade: Sp(1)-equivariance against left translation
forces right translation, so X2's moduli is exactly Sp(1) and the homotopy
type is a point -- that is WHY the class is +1 with no further input. The
ladder below it is the right decomposition: each cyclic rung's oracle space
is the space of sections twisted by maps off the lens quotient, and the
witnessed degrees (+1 generic, +7 twisted at Z/6, +9 at Z/4, +3 at Z/2)
realize the predicted cosets 1 + nZ exactly. One caution, recorded: the
fiber-side Z/6 EMBEDDING (the axis) is itself part of X -- do not let the
plain-English statement suggest the axis is native. It does not (it says
"declared").

**Krein analyst (G2 on the confined habitat).** The load-bearing new fact
is exact: K_S twisted-commutes with C, so the commutant restricts to both
confined sectors as a unitary quaternion group with orthonormal Gram --
G2 holds for every oracle in every rung BY IDENTITY, and the entire G2
drama of the kill sequence is revealed as a statement about kernel-side
dressings only. The reader result completes the picture from the other
side: a generic external kernel dressing has NO parity protection (rank 4
confined), so G2 was never the universal wall -- class stability was. I
certify the nondegeneracy claims: nothing in the oracle path divides by a
small singular value anywhere.

**Stable-homotopy / degree specialist (the c bookkeeping under oracle
transport).** Three independent guards on every integer read: two regular
values per degree (all target-consistent), the counter's power certificates
re-run live (+1, +3 known maps), and cross-machinery agreement (join(3,1)
vs quaternion cube, two constructions of degree 3, one verdict; the counter
separates 1/3/7/9 in this very run). The mod-24 arithmetic is exhaustively
checked for |c| <= 60. The lens-space pinning (Olum r^2) is cited, not
re-proven; its fixture-grade content -- every witnessed Gamma-equivariant
degree lies in 1 + |Gamma|Z -- is verified on every rung including the
twisted members. Boundary honestly held: "every member" at Z/6 is
theorem-backed (cited) + witnessed, not enumerated.

**Philosopher of physics (the typing of X).** The result deserves its
careful typing. X is a reference convention with a nonzero minimum size:
that is neither a hidden variable (no ontic surplus; generic anchors are
count-equivalent) nor an empirical parameter (no measurement distinguishes
anchors within the type) nor nothing (the downward proofs show the count
is NOT convention-free). The honest name is a STRUCTURE CONSTANT OF
DESCRIPTION: the geometry underdetermines its own generation count by
exactly one Z/6 phase-matching, no more, no less. The conditional is
stated; whether an observer, a boundary, or a source action supplies the
anchor is left as the disjunction it really is. No metaphysical assertion
is made, and section 4's wording keeps the modality explicit.

**Adversarial referee (attacking every "suffices" as oracle-smuggling).**
My standard: an oracle must be GENERIC of its declared type; a tuned
witness proves nothing. Attacks run: (1) X2's q0 -- three draws plus both
orientations, all degree +1; the type has no tunable freedom left after
the classification theorem, which itself was checked with an exact 0.0
defect and a non-example at O(1). Not smuggled. (2) The Z/6 rung -- the
dangerous one, since a lazy advocate would test only v*q0 members. The
probe includes a strictly-Z/6 member that is provably NOT U(1)-equivariant
(defect 1.03) with degree +7: the class demonstrably moves within the
type, and the sufficiency claim survives BECAUSE the residue, not the
value, carries the count. That is the opposite of tuning. (3) The planted
control -- I demanded a weight-blind oracle that passes the Z/2 shadow, and
it FAILS G1 exactly (reach 0.0, rejected), reproducing the phase0 plant's
signature; bonus: Borsuk-Ulam makes every such oracle singular, witnessed
by a 2.0 jump across a 2e-9 gap. (4) The X1.5 near-miss -- I pressed for
more draws before accepting the kill; the 43-run scout sweep plus the
probe's decisive subset witnessed the 3-divisible member on a fully
generic draw. The kill stands on class instability, not on gate failure --
recorded, because it is the honest and STRONGER statement. Verdict: no
suffices-claim in this document rests on a tuned object.

## 6. Boundary (what this pass cannot see)

- Everything is fixture grade on the frozen (9,5) spine, R0_COND, both
  habitat pins; "every member of the Z/6 type" is theorem-cited (Olum) and
  multiply witnessed, not exhaustively enumerated.
- The identification of the fiber-side Z/3 with either of N4's two frozen
  Z/3s is NOT established; if it ever is, the external input shrinks
  further (toward the matching alone). Named as the natural successor.
- X1.5's kill is a genericity statement (three readers, many draws, scatter
  witnessed); a SPECIAL reader with a stable class would be a new N-item
  with its own import price, exactly as the tree prices such things.
- Whether physics-side occupants (GEOMETER-VS-PHYSICS fork) supply the
  anchor natively is untouched, as throughout the program.
- No Lean/lake; no claim, canon, or posture movement; the line's verdict
  vocabulary ("forced given X") is conditional by construction.

## Receipts

- Probe: tests/channel-swings/conditional_forcing_probe.py -- ALL PASS,
  10 [E] + 2 [F] = 12 (setup [T] = 3 excluded), exit 0, ~265 s,
  deterministic; k1_reframe_probe re-runs clean inside it (exit 0, its own
  15 checks all pass, phase0 battery live).
- HEADLINE (verbatim from the run): CONDITIONAL FORCING RESOLVED -- outcome
  C-b, sharpened. X1 provably insufficient (orientation-invariant gates;
  bit-blind class; deck-odd degree-3 order-killer). X1.5 passes BOTH gates
  and fails on class scatter {-1, +1, +3} including the zero class on a
  generic draw. X2 SUFFICES (c = +1 oracle-independent and state-free,
  k = 64 = 16 mod 24, order 3 FORCED). X2 NOT minimal: the minimal X is ONE
  ORDER-SIX PHASE REFERENCE (Z/6 = bit x trit; witnessed degrees 1 and 7,
  all = 1 mod 6; Z/4, Z/3, Z/2 all fail). The single bit is exactly the
  CUBE of the thing that is enough. Planted weight-blind oracle rejected by
  G1 while passing the Z/2 shadow.
- Key exact identities new in this run: K_S C - C conj(K_S) = 0.0;
  commutant Gram on confined states orthonormal to 3.3e-16; equivariance-
  forces-right-translation at defect exactly 0.0 (dyadic samples).
- Witnessed degree table: X1.5 readers {-1, +1, +3}; X2 all +1 (3 q0 x +-);
  Z/6 type {+1, +1, +7}; Z/4 witness +9; Z/2 witness +3; Z/3 witness
  deck-inadmissible (defect 1.50).
