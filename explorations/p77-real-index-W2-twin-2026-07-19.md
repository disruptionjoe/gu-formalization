---
title: "P-77-REAL-INDEX W2 (adversarial twin): the (7,7) real-index generation arithmetic attacked by direct Clifford-module counting -- pre-registration, steering tests, bookkeeping-trap audit, eta skepticism"
status: active_research
doc_type: exploration
created: 2026-07-19
directed_by: "Parent dispatch, probe P-77-REAL-INDEX of CH-SIG-77 (W2 adversarial twin; council-amended mission; independent of W1 by construction -- W1 output not read)"
axiom: lab/process/boundary-adapter-standing-axiom.md
extends: explorations/channel-swing-CH-SIG77-port-2026-07-19.md
inputs:
  - explorations/channel-swing-CH-SIG77-port-2026-07-19.md
  - tests/channel-swings/ch_sig77_port_probe.py
  - explorations/channel-swing-CH-QM-2026-07-19.md
  - canon/no-go-quaternionic-parity-generation-sector.md
  - docs/WHERE-GU-STANDS-AND-THE-MISSING-OBJECT-2026-06-27.md
  - tests/gen_ch2_sx_from_codazzi.py
  - tests/generation-sector/signature_77_rerun.py
  - tests/generation-sector/ghost_parity_krein.py
tests: tests/channel-swings/p77_real_index_twin.py
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# P-77-REAL-INDEX, W2 adversarial twin

Role: independently attack the (7,7) real-index generation arithmetic by a
route DIFFERENT from the KO-of-a-point route -- direct Clifford-module
counting on an explicit, bit-exact, all-REAL integer representation of
Cl(7,7) -- and adversarially steer every convention that could hide a wrong
answer. Signature-pure per K6: every computation is (7,7); (9,5) facts and
standard Clifford-table facts are cited, never recomputed. W1's output
(`explorations/p77-real-index-W1-builder*`) was not read.

## 0. PRE-REGISTRATION (written before any computation was run)

This section was committed to disk before the twin probe script existed or
ran. It binds the verdict rules.

**What would convince me the count is CONVENTION-RIGID.** All three of:

- **R1 (forced divisor).** The real-class module theory yields ONE divisor
  for the count packaging, forced by Schur/bicommutant structure alone
  (i.e. by End of the relevant module), and that divisor is invariant under
  the full declared steering menu below: timelike-set relabeling,
  orientation reversal, BOTH forks of the GRAM-PIN-77 Gram convention,
  per-generation module normalization (complex-Weyl vs real-Majorana vs
  ported-quaternionic), and base/fiber-split carrier typing.
- **R2 (computed numerator).** Some (7,7)-native computation -- connection
  index, carrier arithmetic, or the retyped K3 toy input -- PRODUCES a
  nonzero integer numerator without target-selection (i.e. without choosing
  the number so that the count comes out desired).
- **R3 (steering fails).** Every steering attempt in the declared menu
  either returns the SAME count or fails as a typing error (non-integer /
  demonstrably ill-typed import); no defensible alternative assignment
  yields a different integer count.

**What would convince me the count is CONVENTION-SOFT / FREE-INTEGER.** Any of:

- **S1 (Schur divisor 1).** End of the (7,7) spinor module is R, so the
  algebra forces NO multiplicity quantum, and every candidate per-generation
  divisor is a physical typing CHOICE with at least two defensible values.
- **S2 (steering succeeds both ways).** The declared menu produces count 3
  under one defensible assignment AND a different integer count under
  another defensible assignment.
- **S3 (free numerator).** Nothing (7,7)-native computes the numerator: the
  natural connections give 0 (cited, port probe 1f), and the only computed
  toy input (ch2(S_X)[K3] = -5376) reaches any particular count only via a
  divisor chosen after the fact.

**Declared steering menu** (committed now; each attempt will be documented
with its outcome, including failures): (i) timelike-set relabeling /
orientation; (ii) canonical Gram bS vs chirality-twisted Gram bT
(GRAM-PIN-77 both forks); (iii) divisor readings {8, 16, 32} crossed with
numerator retypes {24, 48, 96}; (iv) divisor readings of the honest K3
number -5376 over the repo's own natural dimensions; (v) base-Clifford-
linearity ("spacetime-scalar carrier") typing.

**Decision rule (binding, per council amendment).** If both "3" and
"not-3" are achievable by defensible convention assignments, the verdict is
FREE-INTEGER / CONVENTION-SOFT regardless of what any single computation
outputs.

**Pre-declared expectations** (falsifiable by the runs below): from the
ground documents alone I expect S1 and S3 to hold (End = R for M(128,R);
numerator uncomputed everywhere). I pre-register the specific predictions:
(a) End_{Cl(7,7)}(R^128) has real dimension 1; (b) the commutant of a
(1,3) base tetrad inside M(128,R) has real dimension 1024 with quaternionic
type; (c) base-linear Hermitian carriers have eigenvalue multiplicities
divisible by 8. If any of these comes out otherwise, that is reported as a
surprise and the verdict logic re-examined from scratch.

---

*(Results below this line were written after the pre-registration, from the
machine-checked runs of `tests/channel-swings/p77_real_index_twin.py` --
exit 0, 27/27 checks. One check assertion was corrected between the first
and second run: I had miscounted the number of non-integer cells in the 3x3
count matrix as 4; it is 3. No mathematical content changed. All three
pre-registered predictions (a), (b), (c) came out as predicted.)*

## Verdict up front

**FREE-INTEGER / CONVENTION-SOFT**, by the pre-registered decision rule:
the steering menu produces count 3 under defensible assignments AND
produces 6, 12, 42, 24, 3/2 (and a typing under which literal 3 is
outright impossible) under other defensible assignments. S1, S2, and S3
all hold; R1, R2, R3 all fail. The evidence supports the port probe's
ending (ii): **3 is reachable-with-free-integer, not forced and not
excluded** -- parity with (9,5), the fork's generation advantage stays
typing-only. The remaining cheap-kill window (ending (iii),
"real-class divisibility makes 3 unreachable") is CLOSED: the Schur
divisor of the (7,7) class is 1 and odd carriers exist on the exact
constraint surface. But the twin also found a wall the port probe did not
look at: **the Kramers wall did not vanish in (7,7) -- it moved to the
spacetime factor** (Section 3, trap T4), and any construction that types
the generation carrier as spacetime-scalar (base-Clifford-linear) faces a
signature-in-8Z quantization there.

## 1. The independent functor path: direct real-module counting

Route: an explicit all-REAL integer representation of Cl(7,7) --
7 symmetric gammas squaring to +I, 7 antisymmetric squaring to -I, entries
in {0, +1, -1} (signed permutations), Clifford relations INTEGER-EXACT.
This is a different functor from both the KO-of-a-point route and the port
probe's complex Jordan-Wigner route: here the real form is EXHIBITED rather
than certified via J'^2 = +1, so the two probes corroborate each other from
opposite sides (a J'-real-structure certificate = "a real form exists"; the
twin constructs it).

- **Algebra identified bit-exactly.** All 16383 nonscalar Clifford
  monomials have exact integer trace 0 (Gray-code sweep via signed-
  permutation composition); every monomial is orthogonal (m^T = m^{-1}),
  so the trace form is diagonal and nonzero on the 16384 monomials => they
  are linearly independent => the real algebra has dimension 16384 =
  dim_R M(128,R) => **Cl(7,7) = M(128,R) and End_{Cl(7,7)}(R^128) = R.**
- **THE DIVISIBILITY RESULT (the probe's central question): the Schur
  divisor is 1.** End = R means the (7,7) class forces NO multiplicity
  quantum on any Hermitian carrier. On the EXACT constraint surface
  (Gamma Gamma^T = 14 I integer-exact, so A = 14 Pi is an integer matrix
  with Gamma A = 0 and A^2 = 14 A bit-exact, ker dim 1664 exact), rank-3
  and rank-2 real symmetric carriers give signatures 3 and 2: **every
  integer is a reachable carrier index; real-class divisibility constrains
  NOTHING at the native-typing level.** (Independent re-derivation of port
  probe 1e/1f by the real-form route.) Consequence for the trichotomy:
  ending (iii) -- "real arithmetic forces an even or /4 count, the wall
  returns through the arithmetic back door" -- is dead **at native
  typing**; see T4 for the non-native typing where a wall does return.
- **Submodule structure that the count packaging must respect:** the fiber
  Cl(6,4) = M(32,R) (1023/1023 traceless, integer-exact) has fiber
  chirality omega(6,4)^2 = -I EXACTLY: omega is a COMPLEX STRUCTURE on
  R^32, so there is **no real Weyl module** -- the "one generation = one
  Weyl-16" unit exists only complexly; the unique irreducible REAL fiber
  module is the 32-dim Majorana-Dirac one. Any real-class divisor
  therefore has TWO defensible values (16 complex-Weyl, 32 real-Majorana)
  before any physics is spoken: pre-registered S1 confirmed.

## 2. The steering test (documented attempts, each with outcome)

Menu item (i), orientation/timelike relabeling: global sign flip and the
T = {4..10} relabeling leave every class certificate invariant
(16383/16383 traceless both ways). **Steering outcome: no effect. The
CLASS is convention-rigid** -- softness lives in the count packaging, not
the algebra.

Menu item (ii), GRAM-PIN-77 both forks: chirality-twisted bT (timelike
7-product) is REAL symmetric, bT^2 = I, trace 0 exact -> real 64/64
sectors; canonical bS = i * (spacelike 7-product) -- the bare real product
is antisymmetric with square -I exact, so the scalar i is forced and
J'-odd (real-form re-derivation of probe 1c) -> complexified 64/64
sectors. Rank-3 (odd) AND rank-2 (even) carriers exist INSIDE the +sector
under BOTH forks. **Steering outcome: neither fork pins parity; the fork
changes sector reality-typing only.** Cannot make 3 forced, cannot make 3
forbidden, via the Gram.

Menu item (iii), the retype matrix (numerators {24 H-units blind, 48
C-units, 96 R-units} x divisors {8 rank_H blind, 16 rank_C Weyl, 32
rank_R Majorana}), exact fractions:

    24/8 = 3    24/16 = 3/2   24/32 = 3/4
    48/8 = 6    48/16 = 3     48/32 = 3/2
    96/8 = 12   96/16 = 6     96/32 = 3

**CAN I MAKE 3? Yes** -- the whole type-consistent diagonal gives 3 (the
count is invariant under HONEST retyping, as it must be: same complexified
data, ind_C = 2 ind_H in the H-class vs ind_R = ind_C in the R-class, and
the divisor doubles in step). **CAN I MAKE NOT-3? Yes** -- any port that
retypes the numerator but not the divisor (or vice versa) gives 6, 12,
3/2, or 3/4, and each such cell is exactly the kind of half-retyped
arithmetic a port would naturally produce (T1-T3 below). By the
pre-registered decision rule this alone settles CONVENTION-SOFT --
**with the sharpening that softness here is TYPING-DISCIPLINE softness:
the honest diagonal is count-preserving; the off-diagonal cells are
errors waiting to be made, not defensible physics.** The genuinely free
part is the NUMERATOR: the "24" is an open target never computed in
either class (cited: canon/no-go-class-relative-map.md GU-Chir block;
nothing (7,7)-native computes any numerator -- connections give 0, port
probe 1f). S3 confirmed.

Menu item (iv), the honest K3 number: -5376 recomputed exactly from its
own stated formula ((128/8) * 7 * 3 * sigma(K3)); factorization
**-5376 = -(2^8 * 3 * 7)**. Divisor-steering over repo-natural dimensions:

    /128 (spinor dim_C) = -42     /1792 (RS space) = -3
    /224 (14 x Weyl-16) = -24     /896 (half RS)   = -6
    /64  (H-lines)      = -84     /448 (14 x 32)   = -12

**CAN I MAKE 3? Yes**: divisor 1792 (= dim of the RS space 14 x 128, as
natural-looking a normalization as any) gives exactly -3. **CAN I MAKE
NOT-3? Yes**: -42, -24, -6, -12, -84, -2 all with equally natural
divisors -- including resurrecting the magic "24" itself via divisor 224
= 14 x 16. The decisive forensic point: **the "3" extractable from -5376
is Hirzebruch's coefficient (p1 = 3 sigma), and the "7" is the 1+6
tangent+Sym^2 multiplier -- neither is generation content.** Any future
claim that "-5376 secretly contains the 3" must be met with this
factorization.

Menu item (v), base-linearity typing: see T4. **Steering outcome: a
defensible typing exists under which literal 3 is IMPOSSIBLE** (signature
forced into 8Z), and a renormalized reading (count = sig/8) under which
it is free again -- the same literal-vs-renormalized fork the (9,5) class
already had. This is the strongest not-3 steering result: not just a
different number, but a wall, from a typing choice the transcript does
not pin.

## 3. Bookkeeping traps found (the factor-of-two hunt)

- **T1 (the 256-vs-128 halving).** (9,5): irreducible = H^64 = real dim
  256. (7,7): irreducible = R^128 = real dim 128. SAME complexification
  C^128. Any "per real dimension" bookkeeping ported across silently
  gains or loses a factor 2; any per-H-line bookkeeping (the codazzi
  test's own hline_norm divides by 64) has no (7,7) referent at all.
- **T2 (the ungraded-tensor trap -- the nastiest one).** The naive
  Kronecker port base (x) fiber makes base and fiber gammas COMMUTE (it
  is not a Cl(7,7) module), and its commutant contains exact quaternion
  units: End = H (dim 4, exact) on a 256-dim real module. **The lazy
  factorized port of (7,7) lands exactly on quaternionic-class module
  data -- it silently resurrects the Kramers wall and destroys the fork's
  entire advantage** (M(2,H) (x) M(32,R) = M(64,H); only the GRADED
  tensor gives M(128,R)). Worse, the error has opposite sign in the two
  classes: (9,5) naive Kronecker gives 4 x 32 = 128 = half the true 256;
  (7,7) naive gives 8 x 32 = 256 = double the true 128. A formula keyed
  to "dim(base) x dim(fiber)" is off by a RELATIVE factor 4 between the
  classes.
- **T3 (divisor/numerator half-retype).** The B1 matrix above: honest
  retyping doubles numerator AND divisor together (24/8 -> 48/16 ->
  96/32, all = 3); retyping one without the other is the natural porting
  mistake and yields 6, 12, 3/2, 3/4.
- **T4 (THE MOVED WALL -- new, not in the port probe).** In the
  (7,7)-inducing mostly-minus X4 convention the BASE algebra is
  quaternionic: **Cl(1,3) = M(2,H)**, certified integer-exact (explicit
  quaternion units R_i, R_j in the commutant, squares -I, anticommuting,
  commuting with all four gammas bit-exactly; commutant dim = 4 exact).
  Inside M(128,R) the commutant of a base tetrad is M(16,H) (exact
  dimension 1024 = 128^2/16 by averaging-projector trace; R^128 = 16
  copies of the unique irreducible H^2), and a generic base-Clifford-
  linear symmetric carrier has ALL eigenvalue multiplicities divisible by
  8 (observed: sixteen 8-blocks) => **spacetime-scalar carriers have
  signature in 8Z; literal index 3 is unreachable under that typing.**
  Contrast (cited, standard table + probe 3f convention discussion,
  comparison-grade): the (9,5)-inducing convention has Cl(3,1) = M(4,R)
  -- base-real, base-multiplicity quantum 4. So the signature swap does
  not delete the quaternionic structure; it RELOCATES it from the total
  algebra to the spacetime factor (and the (9,5) class symmetrically has
  it on the total but not the base). The CH-SIG-77 weld must therefore
  PIN the carrier's base-typing (spacetime-scalar vs not) as an explicit
  convention datum, or the wall re-enters unannounced.
- **T5 (the K3 input retyping).** The number -5376 PORTS: the spin-trace
  identity ch2(S) = (dim_S/8) p1(V) is complexified-Lie-algebra data,
  blind to the real form, and the fiber content (6,4) is convention-
  invariant (probe 3f). But its TYPE changes: in the real class the
  invariant it shadows is a Pontryagin-type/KO characteristic number
  (for a complexified real bundle, ch2 = p1-shadow), and the KO
  refinement carries mod-2 data (KO^{-1}, KO^{-2} = Z/2) that ch2 cannot
  see at all: **the toy input UNDERDETERMINES the real-class index; it
  does not need discarding, it needs a declared retype plus the missing
  mod-2 components.** Meanwhile the Ahat(K3) = 2 "doubling role" does NOT
  evaporate: K3's own Dirac operator is quaternionic (KO^{-4}) regardless
  of the ambient signature -- and the finite shadow of the KO product
  alpha^2 = 4 beta is certified exactly (H (x)_R H = M(4,R), Gram = 4 I):
  any factorized bookkeeping that multiplies the K3 H-type Dirac against
  another H-typed factor hides a x4 when repackaged real.

## 4. The eta/boundary question, skeptically

The (9,5) eta = 0 proof used C = J_quat . G (AZ class CII); J_quat is
gone in (7,7). Findings:

- **The conclusion has a J-free route.** With the EXACT grading
  G = Pi - Q (G^2 = I from the exact rational Pi = A/14), any
  KT-shaped off-diagonal D = Pi H Q + Q H Pi anticommutes with G, so the
  spectrum is exactly symmetric and the finite-shadow eta vanishes WITH
  NO ANTIUNITARY INPUT (checked: anticommutator 2e-13, spectral asymmetry
  1e-13, eta_finite = 0). The C-01 mechanism ("any boundary Dirac whose
  square is the positive KT Hessian inherits the anticommuting chiral
  grading") is grading-driven and signature-blind; the CII/J_quat proof
  was sufficient, not necessary.
- **What it would take to FORCE a nonzero eta:** (i) the true noncompact
  boundary operator (uncomputed in BOTH classes -- only round-S^3 APS
  eta = 0 exists, cited from the codazzi test's own caveats); (ii) a
  G-breaking term FORCED by (7,7)-specific structure -- none identified;
  in (9,5) grading-breaking was optional and connection-dependent (cited
  C-02/C-03); or (iii) an AZ argument -- the class genuinely changes
  (CII -> BDI-type, since J'^2 = +1), so the CII-specific protection
  proof DIES and its stability under perturbations must be re-derived,
  but the unperturbed conclusion stands on the grading.
- **Honest scale limit, symmetric in both directions:** at toy scale a
  nonzero eta is structurally invisible (finite symmetric spectra give
  eta = 0 identically), so the toy can neither exhibit a (7,7) boundary
  contribution nor certify its absence -- and the same limit applies to
  the (9,5) toy-grade eta = 0. Absence of the CII proof is NOT presence
  of a nonzero eta; equally, nothing here bounds the true eta away from
  contributing. O7 stays NEEDS-RECOMPUTE, with the sharpened statement:
  what needs recomputing is the PERTURBATION STABILITY of eta = 0 in the
  new AZ class, not the unperturbed vanishing.

## 5. Verdict against the pre-registration

- **R1 fails:** no forced divisor -- Schur divisor is 1, and the
  per-generation divisor has two defensible values (16/32) because no
  real Weyl module exists (omega^2 = -I).
- **R2 fails:** no (7,7)-native computation produces a numerator
  (connections 0, cited; K3 toy reaches specific counts only via
  after-the-fact divisors; the 24 target is open in both classes).
- **R3 fails / S2 holds:** 3 achievable (type-consistent diagonal; K3
  divisor 1792), not-3 achievable (6, 12, 42, 24, 3/2; base-linear
  typing forbids literal 3 outright).
- **S1, S3 hold.** Pre-registered predictions (a) End = R dim 1,
  (b) base-tetrad commutant dim 1024 quaternionic, (c) base-linear
  multiplicities divisible by 8: ALL CONFIRMED.

**VERDICT: FREE-INTEGER / CONVENTION-SOFT.** The trichotomy resolves to
ending (ii): the count-3 target is reachable-with-free-integer in the
real class, exactly as in (9,5); the fork's generation advantage is
typing/severity only, and the port probe's "N stays 5" stands. The
cheap-kill window (iii) is closed at native typing. The actionable
residue for the weld: pin THREE convention data or the softness bites --
the Gram fork (GRAM-PIN-77), the per-generation module normalization
(Weyl-16 complex vs Majorana-32 real), and (new) the carrier's
base-typing (T4), plus a declared KO retype of any K3 toy input (T5).

## Raw data for the parent

1. **Independent-path divisibility:** End_{Cl(7,7)}(R^128) = R
   (bit-exact; 16383/16383 traceless monomials) => Schur divisor 1, no
   algebra-forced quantum; odd (3) and even (2) carriers on the EXACT
   integer constraint surface (Gamma Gamma^T = 14 I, A^2 = 14 A,
   ker dim 1664 exact). Real-class divisibility does NOT make 3
   unreachable: ending (iii) dead at native typing. Fiber Cl(6,4) =
   M(32,R) with omega^2 = -I (no real Weyl => divisor fork 16 vs 32).
2. **Steering outcomes:** made 3: YES (retype diagonal 24/8 = 48/16 =
   96/32; K3 number /1792). Made not-3: YES (6, 12, 3/2, 3/4 by
   half-retype; -42/-24/-6/-12/-84/-2 from the K3 number; literal 3
   IMPOSSIBLE under base-linear typing). Orientation and both Gram forks:
   no effect on parity (class rigid, count packaging soft). By the
   pre-registered rule: FREE-INTEGER/CONVENTION-SOFT.
3. **Traps:** T1 real-dim halving 256->128; T2 ungraded Kronecker port
   resurrects End = H on dim 256 (the (9,5) wall back, silently; errors
   have OPPOSITE sign in the two classes, relative factor 4); T3
   numerator/divisor half-retype (x2/x4 count shifts); T4 THE MOVED WALL:
   Cl(1,3) = M(2,H) integer-exact, base-linear carriers signature in 8Z
   (new; weld must pin carrier base-typing); T5 K3 input: -5376 ports but
   retypes (ch2 -> p1/KO shadow; mod-2 KO data invisible to ch2;
   Ahat(K3) = 2 quaternionic doubling intrinsic to K3, survives;
   H (x) H = M(4,R) exact = the alpha^2 = 4 beta x4 shadow); -5376 =
   -(2^8 * 3 * 7) and its extractable "3" is Hirzebruch's p1 = 3 sigma.
4. **Eta:** conclusion eta = 0 has a J-free chiral-grading route
   (machine-checked shadow, no antiunitary input); what died with J_quat
   is the CII stability argument, not the vanishing; nothing identified
   forces a nonzero eta; toy scale cannot see one in either class. O7 =
   "recompute perturbation stability in the new AZ class."
5. **Verdict:** CONVENTION-SOFT / FREE-INTEGER; supports port-probe
   ending (ii) (parity with (9,5), advantage typing-only); convention
   data to pin at the weld: Gram fork, module normalization (16/32),
   carrier base-typing, K3-input KO retype.

## Boundary

All conditional under the standing axiom; toy- and symbol-grade
computations plus exact module theory; W1's output not read (independence
preserved for the parent's comparison). Signature-pure per K6: all
computations (7,7) or its subalgebras; (9,5) and standard-table facts
cited, never recomputed; the base-algebra comparison is comparison-grade
convention-location data in the sense of port-probe Part 3. No claim
status, canon verdict, scorecard row, map cell, or public posture moves;
no external action; the (9,5)-vs-(7,7) comparative verdict stays the
integration barrier's business.
