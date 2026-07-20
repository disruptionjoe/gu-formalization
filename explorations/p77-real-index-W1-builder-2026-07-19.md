---
title: "P-77-REAL-INDEX (W1 builder): the (7,7) real-index generation arithmetic -- convention rigidity, KO divisor, and the boundary/eta contribution"
status: active_research
doc_type: exploration
created: 2026-07-19
directed_by: "Joe direct chat, 2026-07-19 (CH-SIG-77 channel, probe P-77-REAL-INDEX, W1 builder; council-amended approach binding)"
axiom: lab/process/boundary-adapter-standing-axiom.md
extends:
  - explorations/channel-swing-CH-SIG77-port-2026-07-19.md
  - explorations/channel-swing-CH-QM-2026-07-19.md
inputs:
  - canon/no-go-quaternionic-parity-generation-sector.md
  - docs/WHERE-GU-STANDS-AND-THE-MISSING-OBJECT-2026-06-27.md
  - explorations/channel-swing-CH-SRC-2026-07-19.md
  - tests/channel-swings/ch_sig77_port_probe.py
  - tests/generation-sector/step5_synthesis.py
  - tests/generation-sector/step6_grading_break_decision.py
  - tests/generation-sector/ghost_parity_krein.py
  - tests/generation-sector/signature_77_rerun.py
  - DERIVATION-PROGRESS.md (generation-count-rank3-resolution entry: the ind_H = 24 = 16+8, 24/8 = 3 packaging and its GEN-01/GEN-03 leg-split caveats)
tests: tests/channel-swings/p77_real_index_builder.py
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# P-77-REAL-INDEX (W1 builder): the (7,7) real-index generation arithmetic

Mission: rebuild the (9,5) generation-count packaging
(`ind_H(D_GU) = 8*Ahat(K3) + 8 = 24`, `count = 24/8 = 3`, divisor 8 =
quaternionic rank per generation, all tied to `Cl(9,5) = M(64,H)`) in the
real class `Cl(7,7) = M(128,R)`, with the boundary/eta contribution as the
declared center of gravity. Signature purity (K6): every computation in the
companion script is performed IN (7,7); all (9,5) facts are cited from their
receipts (canon C-01..C-07, step5/step6, the rank3-resolution entry), never
recomputed.

Written in the required order: Section 1 (pre-registered interpretations)
and Section 2 (convention-DOF enumeration) were committed to this file
BEFORE the companion script was written or run. Sections 3+ report what the
computation then returned.

## 1. PRE-REGISTERED INTERPRETATIONS (committed before computing)

Exactly three endings were declared for this probe. What each means:

### Ending FORCED-3

The (7,7) arithmetic yields the generation count 3 as a
**convention-rigid** consequence of module theory plus a computed invariant.
To claim this ending, ALL of the following must hold:

- the same count under BOTH Krein Grams of the GRAM-PIN-77 fork (canonical
  `bS = i*e_s1..e_s7` and chirality-twisted `bT = e_t1..e_t7`), and under
  every sign/orientation/phase convention enumerated in Section 2;
- the divisor (the per-generation unit that turns an index into a count) is
  itself DERIVED from (7,7) module theory, not chosen; and the
  literal-index vs half-index reading fork either collapses (both give 3)
  or one reading is internally forced by a computed structure;
- the value does not depend on which admissible grading-breaker /
  connection is used (the eta/boundary contribution, if it supplies the
  count, must be breaker-independent -- a genuine spectral asymmetry of the
  class, not of one perturbation);
- no free integer input anywhere (no chosen carrier rank, no Candidate-A/B
  style rank pin taken by hand).

**What would NOT count as forced-3** (pre-declared):

- 3 reached by choosing a rank-3 carrier on the constraint surface. That
  is exactly the (9,5) free import (canon C-06 / step10); (7,7) making it
  type-consistent (port probe 1e) does not make it forced.
- 3 reached under one Gram choice, one divisor reading, or one particular
  breaker at one particular coupling t, when another equally legitimate
  convention gives a different number.
- 3 assembled by porting the (9,5) "24 = 16+8" packaging with its
  rank_H(S_RS^+) = 4 input carried over by hand: that input is
  physical-count grade in (9,5) (GEN-01: the final halving is unjustified)
  and inherits no new justification from the class change.
- Any "3" whose provenance is the K3 Ahat(K3) = 2 leg times a hand-picked
  rank: same free integer, different clothes.

### Ending FREE-INTEGER

The (7,7) index arithmetic is a plain integer with **no forced
divisibility** and **no forced value**: odd counts including 3 are
reachable (unlike (9,5), where H-linearity forces even), but the actual
value is set by free data -- a chosen carrier rank, a chosen connection /
grading-breaker, or an un-derived per-generation rank. This is parity with
(9,5) on COUNT (the rank/count integer import survives, payload N stays 5)
and an advantage only in TYPE/severity (plain integer under the literal
reading; no foreign non-quaternionic structure needed). This is the port
probe's standing expectation (its Section 6 naive expectation) and claiming
it requires: exhibiting odd reachability, verifying NO forced divisibility
survives (the "/8" and the Kramers factor-2 both die), and verifying no
convention in Section 2 resurrects a parity wall.

### Ending REAL-CLASS-BLOCKS-3

A rebuilt divisibility in the real class forbids the count 3: some computed
structure -- candidates pre-declared as (i) a surviving factor of two in the
real-dimension bookkeeping (the R^128 vs H^64 = 256-real-dim halving
interacting with the per-generation unit), (ii) the ghost/compensator
sector's grading-vs-real-structure interaction forcing even counts under
BOTH Grams with no per-sector escape, (iii) a KO-side 2-divisibility at
p - q = 0 mod 8 that survives every convention -- forces the reachable
counts to be even (or divisible by 4, etc.) in every convention-rigid
reading. This is the fork's remaining cheap kill: the Kramers wall returns
through the arithmetic back door. Claiming it requires the block to be
convention-rigid in the Section-2 sense (a parity that appears under one
Gram but not the other is a convention artifact, not a block).

Adjudication rule (pre-declared): if odd counts are reachable but not
forced, the ending is FREE-INTEGER even if some particular natural
construction happens to output 3. If different Section-2 conventions give
different counts and no internal argument pins the convention, the ending
is FREE-INTEGER (with the convention-dependence named), not FORCED-3.

## 2. Convention degrees of freedom (enumerated FIRST, per council amendment)

The convention space a (7,7) count claim must survive. For each DOF: what
it is, and whether it can change the final count.

| # | DOF | choices | can it move the final count? |
|---|---|---|---|
| D1 | X4 sign convention | mostly-minus (1,3) is what INDUCES (7,7) (port 3f) | No -- fixed by being in this channel; not free inside it |
| D2 | which 7 of 14 directions are timelike | repo T = {4..10} vs any O(7,7) relabeling | No (class-invariant); verified spot-wise in script Part 0 |
| D3 | Krein Gram (GRAM-PIN-77) | canonical bS = i*e_s1..e_s7 (J'-odd) vs chirality-twisted bT = e_t1..e_t7 (J'-even) | Changes sector TYPING (J'-exchanging vs J'-invariant); whether it changes count parity is COMPUTED (Part D). Pre-registered: if parity differs across Grams, no forced claim survives |
| D4 | Gram overall sign / sign of the scalar i | +-bS, +-bT | Relabels the two orientation sectors; cannot move |count| |
| D5 | real-structure phase | J'_theta = e^{i theta} U . conj, all have J'^2 = +1 | No -- rotates the real form R^128 inside C^128, class-rigid; uniqueness up to phase from irreducibility |
| D6 | divisor READING | literal index (count = signature of carrier) vs half-index (count = index/2) | YES: x2 on the final number. In (9,5) the /2 had a Kramers justification; in (7,7) that justification is GONE, so keeping it is an unforced convention. Any forced-3 must show the fork collapses or is pinned |
| D7 | per-generation unit | (9,5) used dim_H = 8 H-lines per generation (16 Weyl = C^16 = H^8). (7,7) analog must be recomputed from module theory: real rank 16 (if the internal 16 carries a real form) or 32 (if it stays complex-class and pairs with its conjugate) | YES if left unpinned: x2. Computed in Part B (not free once module theory is done, but the READING must cite the computation) |
| D8 | orientation of spectral flow / sign of eta | breaker sign, t-direction | Flips the sign; cannot move |count| |
| D9 | inherited rank ambiguity | Candidate A (rank 4 -> 3 gens) vs Candidate B (rank 8 -> 4 gens) from the (9,5) RS leg (GEN-01) | YES: the x(3 vs 4) ambiguity ports verbatim -- the class change does not adjudicate it |

**Count of distinct final answers the convention space could produce** from
one and the same underlying index datum: D6 (x2) times D7-if-unpinned (x2)
times D9 (3-vs-4) -- at least **four to eight distinct final counts** are
reachable by convention choices alone (e.g. {3, 6, 4, 8, 3/2...}) unless
each fork is pinned by computation or internal argument. This is the
rigidity bar a FORCED-3 claim has to clear, fixed before computing.

Pre-registered rigidity verdict rule: FORCED-3 requires D3 parity
robustness plus pinned D6 and D7 plus a D9 adjudication plus
breaker-independence in Part C. Anything less lands in FREE-INTEGER (or
BLOCKS-3 if a rigid parity wall appears).

---

*(Everything below this line was written AFTER the companion script
`tests/channel-swings/p77_real_index_builder.py` was run. Sections 1-2
were not edited after computation; the script enforces its own exit-0
check battery.)*

## 3. Class certificate and convention rigidity (script Parts 0 + A)

All exact-arithmetic checks pass with residual literally 0.0 (the matrices
involved have entries in {0, +-1, +-i}, so products and differences are
exact in floating point):

- **Cl(7,7) relations bit-exact**; J' (factors e1 e3 e4 e6 e8 e10 e11 e13)
  commutes with all 14 generators bit-exact, **J'^2 = +1** exact.
- **Real-dimension bookkeeping (the mission's declared trap), tracked:**
  the J'-fixed real form inside C^128 has real dimension exactly 128
  (computed as the +1-eigenspace of the real-linear involution
  M = [[Re Cp, Im Cp], [Im Cp, -Re Cp]], M^2 = I exact, trace argument).
  So the (7,7) irreducible module is R^128 = **128 real dimensions**, and
  the complex C^128 used in every probe is its COMPLEXIFICATION. Cited
  contrast: the Cl(9,5) module is H^64 = **256 real dimensions**, whose
  complex RESTRICTION is the same C^128. Same complex rep, half the real
  content -- every factor of two below is stated against this ledger.
- **D2 rigid:** a relabeled timelike set ({0..6}) yields the same class
  (commuting antiunitary, J^2 = +1.000, averaging construction).
- **D4/D5 rigid:** Gram overall signs only relabel sectors; the whole
  J'-phase family squares to +1.
- **D3 (GRAM-PIN-77) fork facts exact:** bS = i*e_s1..e_s7 is Hermitian,
  involutive, and ANTICOMMUTES with J' (J'-odd); bT = e_t1..e_t7 commutes
  (J'-even). Where this does and does not matter for the count: Section 6.
- **Weyl typing (new here):** omega = e_1..e_14 satisfies omega^2 = +1
  exact, is Hermitian, and J' preserves BOTH 64-dim Weyl halves and
  restricts to a real structure on each ((J'|half)^2 = +1, residual 0):
  both halves are REAL, rank_R 64 each (Cl^0(7,7) is of R(+)R type). No
  hidden complex/quaternionic structure survives at the Weyl level.

**Rigidity verdict (per the Section 2 rule):** D1-D5 and D8 are rigid --
no convention there can move a count. The forks that CAN move a final
number remain exactly D6 (literal vs half-index reading, x2), D7 (field
content real-form vs complex-doubled, x2, though the per-generation unit
itself is pinned by module theory in Section 4), and D9 (the inherited
Candidate A/B rank ambiguity, 3-vs-4). Nothing computed tonight pins D6,
D7-reading, or D9; therefore no convention-rigid "3" is available, and by
the pre-registered adjudication rule a FORCED-3 ending is out of reach
unless the boundary computation (Section 5) had pinned a value. It does
not.

## 4. The bulk divisor (script Part B): the /8 dies as forcing, survives as bookkeeping

**Fiber module theory, computed with explicit 32-dim Cl(6,4) gammas** (the
fiber signature (6,4) is convention-invariant, port probe 3f, so this is
the correct fiber in BOTH X4 conventions):

- The commuting conjugation was SOLVED by exhaustive subset search (not
  postulated): P = e0 e2 e4 e7 e9, with **Jf^2 = +1 exact** -- the Cl(6,4)
  Dirac module C^32 is REAL class (p - q = 2 mod 8).
- The internal chirality satisfies **omega_int^2 = -1** exact, so the Weyl
  16s are the +-i eigenspaces and the antiunitary Jf **EXCHANGES** them
  (residual 0): there is NO real form on a single Weyl 16. The minimal
  real block is 16 (+) 16bar = **32 real dimensions**.

**The rebuilt per-generation unit:**

| class | one generation (16 Weyl states) packaged as | unit | real dims |
|---|---|---|---|
| (9,5) cited | C^16 = H^8 (ambient H-structure) | 8 H-lines | 32 |
| (7,7) computed | 16 (+) 16bar real block (no real form on the 16 alone) | 32 R-lines | 32 |

**The same 32 real dimensions per generation in both classes.** The (9,5)
packaging `count = ind_H/8 = ind_C/16 = ind_R/32 = 3` and the (7,7)
packaging `count = ind_R/32` agree in invariant (real) units. So the
naive expectation of the mission brief ("divisor 8 was quaternionic rank,
at p - q = 0 the index is a plain integer with no forced divisibility") is
**verified in its arithmetic half and REFINED in its attribution half**:

- VERIFIED: at p - q = 0 mod 8 (KO side, KO^0(pt) = Z) there is **no
  forced divisibility**. Computed: a rank-1 J'-real Hermitian carrier on
  the constraint surface with signature 1 (odd; J'-defect exactly 0), and
  a J'-real Hermitian block with a 1-dimensional kernel (odd kernel --
  the KO-side Z/2 kernel-parity invariant is LIVE in the real class).
  Reachable-signature divisor = 1. Cited contrast: (9,5) H-linearity
  forces even signature and even kernels (canon C-07, Kramers).
- REFINED: the (9,5) "/8" was never all forcing. Its forced part was only
  the **Kramers factor 2** (H-linearity => even complex index); the
  remaining factor was **unit conversion** (how many lines per
  generation), which is bookkeeping and SURVIVES the port as /32-real.
  What dies in (7,7) is exactly and only the factor 2.

**Bulk divisor result:** count = ind_R / 32, with ind_R a plain free
integer (no forced divisibility). The value 3 is reachable (ind_R = 96,
the same real content as the (9,5) conditional 24) and is NOT forced: no
(7,7) computation supplies ind_R, and the two (9,5) legs that assembled 24
do not port as derivations -- the spin-1/2 leg's Ahat(K3) = 2 is
signature-blind topology and ports, but its companion rank input and the
whole RS leg (rank_H(S_RS^+) = 4, Candidate A) were physical-count grade
in (9,5) already (GEN-01: "the final halving is unjustified") and inherit
no new justification here. The D9 ambiguity (3 vs 4 generations) ports
verbatim.

## 5. THE CENTER OF GRAVITY -- the boundary/eta contribution (script Part C)

The (7,7) D_Sigma = E + E^dag (E = Q M_D Pi, repo xi) on the 1792-dim RS
module:

- **C1 -- the bare eta is computably ZERO in (7,7) too, said plainly.**
  The chiral grading G = Pi - Q anticommutes with D_Sigma ({G,D} ~ 7e-16)
  and mirrors the spectrum: #pos = #neg = 128, eta = 0. This half of the
  (9,5) C-01 mechanism ("any boundary Dirac whose square is the positive
  Koszul-Tate Hessian inherits an anticommuting chiral grading, hence
  eta = 0") is **signature-blind and PORTS**. The port doc's O7 worry
  resolves precisely: the CONCLUSION eta(D_Sigma) = 0 survives by the
  grading route alone; what does not survive is the (9,5) PROOF DECOR and
  -- decisively -- the protection class of the perturbed problem:
- **C2 -- the symmetry class drops CII -> BDI.** Computed: T' = J'_RS has
  T'^2 = +1 with [T', D] = 0 (residual exactly 0), C' = J'_RS . G has
  C'^2 = +1 with {C', D} ~ 1e-15. Cited contrast (step6): (9,5) has
  T^2 = C^2 = -1, class CII, and it was the C-PHS (C^2 = -1) plus Kramers
  that governed the revived flow there. In (7,7) the particle-hole
  symmetry C' still exists but squares to +1: **no Kramers pairing
  anywhere in the class.**
- **C3 -- the revived flow, and THE HEADLINE.** Mirroring step6 with
  (7,7)-admissible breakers (Hermitian, G-diagonal so they genuinely break
  the grading, J'-REAL with defect exactly 0, non-equivariant, anti-trap):

  | breaker | eta(D + t Delta), t = 0 .. 2 (9 points) |
  |---|---|
  | natural diag M_D | 0, 0, 0, 0, 0, 0, 0, 0, 0 |
  | generic J'-real #1 | 0, 0, 0, **2**, 0, 0, 2, 2, 2 |
  | generic J'-real #2 | 0, 0, 0, 0, 0, -2, -2, -2, -2 |
  | generic J'-real #3 | 0, -4, -4, -4, -4, -4, **-6**, -6, -6 |

  Four findings, in order of importance:

  1. **The flow quantum HALVES: 4 -> 2.** Values eta = +-2 and -6 (i.e.
     2 mod 4) occur -- **impossible in (9,5)**, where Kramers doubling
     makes every crossing a pair and the observed flow came in steps of 4
     (step6: values +-4). This is the cleanest computable fingerprint of
     the lost quaternionic protection at the boundary.
  2. **Odd counts become reachable FROM THE BOUNDARY.** Under the D6
     half-index reading (count = eta/2, the reading (9,5) needed for 3),
     the reachable count set now includes ODD values: eta = -6 gives
     count 3, eta = 2 gives count 1. In (9,5) the same reading could only
     ever produce even eta/2 jumps of 2 per crossing-pair... the (7,7)
     boundary can shift the count by ONE unit at a time. This is where
     odd shifts come from, exactly as the council brief posited.
  3. **The value is NOT forced.** Different admissible breakers give
     different eta at the same coupling (breaker #1 vs #2 vs #3 disagree
     at t >= 0.75); the natural M_D-diagonal breaker stays at 0 (special,
     as in (9,5)). The revived index is connection-dependent -- the C-03
     reading ports verbatim. The boundary supplies REACHABILITY of odd
     counts, not the value 3. A count-3 from this route still requires
     the unbuilt Y14 boundary holonomy (SPEC 5(ii)) to select a specific
     connection -- the same missing object as before, now with an odd
     target no longer excluded by type.
  4. Full-space eta remains even at every sampled point -- but that is
     dimension arithmetic (eta = dim - 2k when the kernel is trivial; dim
     = 1792 even), NOT a Kramers survival. The odd-parity invariants live
     one level down: odd kernels (Z/2, Part B3b) and odd per-sector /
     carrier signatures (B3a, D4/D5), all exhibited.

  **Eta/boundary headline: the bare eta is computably zero in (7,7) (the
  grading mechanism is signature-blind and ports); the perturbed boundary
  flow loses its CII/Kramers protection (class BDI), its quantum halves
  from 4 to 2 making odd generation shifts reachable, and its value is
  connection-dependent -- so the boundary is the SOURCE of odd counts but
  does NOT pin 3. FORCED-3 does not materialize here.**

## 6. The ghost/compensator sector (script Part D)

The grading-vs-real-structure interaction, stated precisely and computed
bit-exact where the matrices are integer/i-integer:

- **D1/D2:** the canonical ghost/Krein Gram K = eta_V (x) bS is Hermitian,
  K^2 = I, and **ANTICOMMUTES with J'_RS bit-exact** -- the grading is
  J'-ODD -- while the entire GU-native apparatus (e_a, sigma_ab, Pi, M_D,
  G) is J'-REAL with defect exactly 0 -- the machinery is J'-even. (This
  is the (7,7) face of CH-SRC's observation that the ghost grading
  interacts with the real structure: in (9,5) the whole apparatus
  INCLUDING the Gram was J-even; here the Gram alone goes odd.)
- **D3 (the factor 2 that returns, scoped):** for any J'-real,
  K-commuting Hermitian carrier, J' exchanges the two ghost-parity
  sectors, so the per-sector signatures are EQUAL -- computed: a rank-1
  physical-sector seed plus its forced J'-image gives sig(+) = sig(-) = 1,
  total 2 -- and the TOTAL-space signature is therefore always EVEN. The
  ghost sector's contribution to the count arithmetic is a forced
  mirror-duplication: **under the canonical Gram, whatever the physical
  sector counts, the mirror sector counts identically, and the total is
  even.**
- **D4/D5 (why that is not a wall):** the PHYSICAL count is the
  per-sector count (one ghost-parity sector survives the Turok-Bateman
  projection), and per-sector parity is FREE: a K-commuting rank-3
  carrier supported in the + sector has per-sector signature 3 (canonical
  Gram, D4), and under the chirality-twisted Gram bT (K_T J'-even,
  sectors J'-invariant) a J'-REAL rank-3 carrier with odd signature 3
  lives INSIDE one sector (D5). **Per-sector parity freedom is
  Gram-robust; the total-even fact is Gram-dependent** (under bT no
  total-space evenness is forced at all). By the pre-registered rigidity
  rule, a Gram-dependent parity cannot serve as a REAL-CLASS-BLOCKS-3
  wall -- and the Gram-robust statement is parity FREEDOM, not a block.

## 7. Verdict against the pre-registered endings

**Ending reached: FREE-INTEGER.** Adjudicated strictly against Section 1:

- FORCED-3 fails its bar: the convention space still supports multiple
  final numbers (D6 x D9 unpinned; Section 3); the bulk index has no
  forced divisibility AND no derived value (Section 4); the boundary
  value is connection-dependent (Section 5.C3.3); no computed invariant
  outputs 3 convention-rigidly. Note the discipline point: rank-3 odd
  carriers exist everywhere here (B3a, D4, D5) -- all are the
  pre-declared "would NOT count" free import.
- REAL-CLASS-BLOCKS-3 fails its bar: every candidate block named in the
  prereg was checked and none is convention-rigid. (i) The factor-2
  bookkeeping resolves cleanly: the per-generation unit is the SAME 32
  real dimensions in both classes -- no orphaned factor of two blocks odd
  counts (Section 4). (ii) The ghost-sector evenness is total-space-only
  and Gram-dependent, with per-sector freedom Gram-robust (Section 6).
  (iii) KO^0(pt) = Z carries no 2-divisibility; odd signatures and odd
  kernels are exhibited on the constraint surface (Section 4). The
  fork's remaining cheap-kill window is now CLOSED: the wall does not
  return through the arithmetic back door.
- FREE-INTEGER meets its full claiming burden: odd reachability exhibited
  (bulk: signature-1 and signature-3 carriers; boundary: half-quantum
  flow reaching count-odd values; ghost sector: per-sector odd under both
  Grams); no forced divisibility survives (the Kramers factor 2 dies, and
  nothing replaces it); no Section-2 convention resurrects a parity wall.

Consequences for the channel (proposal-grade, no scorecard edit here):
the port doc's O6/O7/O8 obligations are now COMPUTED for the generation
arithmetic: O7's conclusion (bare eta = 0) survives by the signature-blind
grading route; O6's "/8" is rebuilt as /32-real with only the factor 2
lost; O8's 2-primary shift is exactly the CII -> BDI class drop with flow
quantum 4 -> 2 plus the newly live Z/2 kernel parity. The (9,5)-vs-(7,7)
generation-sector comparison lands as the port probe predicted: **the
fork's advantage is typing and severity (plain free integer, odd shifts
boundary-reachable, no foreign structure needed), NOT count (payload N
stays 5 in both; the rank/count integer import survives in both).** The
comparative verdict remains the integration barrier's business.

## 8. What remains UNCOMPUTED

- **The value of ind_R.** No (7,7) computation supplies the analog of the
  (9,5) conditional 24 (itself physical-count grade on its RS leg). The
  K3 toy-model index that would replace ind_H needs the (7,7) twisted
  Dirac content on K3 with the REAL module -- the Ahat(K3) = 2 input
  ports (topology), but the effective twist rank (Candidate A/B, D9) is
  as underived in (7,7) as it was in (9,5). UNCOMPUTED.
- **The D6 reading pin** (literal vs half-index) in (7,7): with Kramers
  gone, the half-index reading lost its justification, but nothing yet
  positively pins the literal reading. UNCOMPUTED (an argument, not a
  matrix computation).
- **Spin-c in the real class** (O6's possibly-favorable half: whether
  spin-c rescues non-spin X4 once H-linearity is no longer there to
  break). UNCOMPUTED, flagged favorable-if-true.
- **Geometric provenance of a specific breaker/connection**: the flow
  values here are in an auxiliary strength t over admissible breakers,
  not yet a geometric parameter (same standing as (9,5) step6; SPEC
  5(ii) boundary holonomy still unbuilt). UNCOMPUTED.
- **The eta of a GEOMETRIC (7,7) boundary operator on a concrete end**
  (e.g. the S^3 fiber data of oq-rk2 rebuilt in the real class):
  tonight's model is the constraint-surface symbol model, the honest
  finite analog, not the Y14 end. UNCOMPUTED.

## 9. Receipts

- Script: `tests/channel-swings/p77_real_index_builder.py`. Run record
  (2026-07-19 evening): the full battery was executed in two pieces --
  the main run completed Parts 0/A/S/B/C (21 checks, all PASS, including
  the full C3 flow table above) and was manually terminated by the
  operator during Part D setup (termination, not a check failure); a
  synchronous completion run re-executed Parts A + D (8 checks, all
  PASS), with D3 subsequently strengthened to the rank-1-seed variant
  shown above (verified PASS: J'-defect 0.0, [K,A] 8.9e-19,
  sig(+) = sig(-) = 1) and folded into the script. Every check that ever
  ran, passed; no check was weakened after seeing results. 29 distinct
  checks total.
- Bit-exact (residual literally 0.0): Clifford relations, all J'
  commutations, J'^2 = +1, real-form dimension 128, Gram fork facts,
  omega facts, fiber Cl(6,4) relations/conjugation/Weyl-exchange,
  {K, J'_RS} = 0, apparatus J'-reality, Gamma Gamma^dag = 14 I.
- Numeric-tolerance: eta counts (tol 1e-7 relative), flow table, sector
  signatures.
- (9,5) citations (never recomputed): canon
  no-go-quaternionic-parity-generation-sector (C-01..C-07, per-generator
  exact certificate), step5 (eta = 0 mechanism), step6 (CII class,
  flow +-4), step10/11 (odd = import), DERIVATION-PROGRESS
  generation-count-rank3-resolution + GEN-01/GEN-03 (the 24 = 16 + 8
  packaging and its leg-split), port probe (1c-1g, 3f).

## Boundary

Conditional work under the standing axiom; symbol/finite-model grade plus
exact module theory; signature-pure per K6 (every computation (7,7),
(9,5) cited only). The twin worker's output was not read. No claim
status, canon verdict, scorecard row, map cell, GRAM-PIN-77 pin, or
public posture moves; no external action. The (9,5)-vs-(7,7) comparative
verdict stays Joe-gated at the integration barrier.
