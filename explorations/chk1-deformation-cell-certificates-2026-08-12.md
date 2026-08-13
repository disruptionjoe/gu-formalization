---
title: "CHK-1 result: chirality-asymmetric zero-order deformation cells on the frozen K77 bank"
status: draft_result
doc_type: construction_result
created: 2026-08-12
brief_version: "1.2"
brief_note: "v1.1 base brief; rule 14 (five-lens inline pre-flight) ratified mid-run as v1.2"
target_claim: NONE-NOT-A-KILL
head_pin: "c789e75bbe0eb38bcd6342516dc88a39c760852b (2026-08-11 20:51:35 -0500); HEAD advanced to 66144b87 during execution (hourly automation); every consumed fixture verified byte-identical between the two commits"
packet: explorations/decoupling-constructibility-packet-2026-08-12.md (Lens 2, CHK-1)
authored_by: "CHK-1 executing pass; repo READ-ONLY; all outputs live in the session scratchpad"
scripts:
  - scratchpad/chk1/chk1_probe.py (deterministic; 30/30 PASS; exit 0; primes GF(1009), GF(1013))
  - scratchpad/chk1/probe_run3.log (probe output)
  - scratchpad/chk1/frozen_v0174_fixture_run.log (anti-redo baseline: frozen fixture, 37 PASS at pin)
binding: >-
  Binds nothing. This artifact makes no disposition, moves no verdict, changes
  no claim status, row, registry, fence, canon, or posture. The KILL/TRIPWIRE
  evaluation below is stated as certificate plus the packet's own outcome
  grading; every disposition belongs to the executing wave. Certified numbers
  are stated plainly.
canon_verdict_change: none
row_change: none
registry_change: none
---

# CHK-1: the chirality-asymmetric deformation space, computed

## Result, plainly

On the frozen v0.173/v0.174 K77 bank (interface I of the packet), the
pairing-compatible zero-order deformation space is nonzero in the X-odd
(half-coupling) cell for BOTH horns at BOTH layers:

| horn x layer | odd | even-sym | even-asym | even total | single-half-supported |
|---|---:|---:|---:|---:|---:|
| P_sym (1,1,1,1), L1 | **2** | 0 | 2 | 3 | 0 |
| P_skew (1,-1,-1,1), L1 | **2** | 2 | 0 | 3 | 0 |
| P_sym (1,1,1,1), L2 | **28** | 14 | 14 | 28 | 0 |
| P_skew (1,-1,-1,1), L2 | **28** | 14 | 14 | 28 | 0 |
| L0 (control, decides nothing) | 960*959 = 920,640 | — | — | 960^2 = 921,600 | 0 (structural) |
| scrambled horn (1,1,-1,-1), L1 | 2 | 0 | 2 | 3 | 0 |
| scrambled horn (1,1,-1,-1), L2 | 28 | 14 | 14 | 28 | 0 |

- **KILL (packet pre-declared): NOT FIRED.** `dim Z_odd(P,L1) = dim Z_odd(P,L2) = 0`
  for both horns is refuted by explicit integer witnesses. `target_claim:
  NONE-NOT-A-KILL`. (Had it fired, the packet's outcome (b) pre-names
  SC-CHI-01, SC-CHI-03, SC-CHI-04, SC-CHI-50, SC-CHI-51, SC-CHI-53, SC-CHI-54,
  with SC-CHI-02/52 as auxiliary mechanism rows; recorded, not used.)
- **TRIPWIRE: FIRED under the declared swap-labeling; hand-audited below.**
  `dim Z_even-asym(P_sym, L1) = 2 > 0` under the sigma(Q) convention. The hand
  audit (packet outcome (d) prescription) finds the labeling FRAME-SENSITIVE
  and the packet's R4a expectation — explicit asymmetric mass unavailable —
  CONFIRMED by the convention-free certificates, not contradicted.
- All planted controls green; the v0.174 two-horn classification reproduces
  exactly over GF(1009) and GF(1013); every reported dimension is closed by
  explicit integer null vectors verified exactly over Z (integer-certified,
  prime-independent; the two primes steer, the integer witnesses certify).

Every "chirality" statement in this artifact is sense (a) of the Layer-0
four-way homonym: the ambient operator-level grading by X = blockdiag(omega)
on the 1,920 carrier. No sense-(b) (observed 4d Weyl) statement is made
anywhere; that bridge is PH-K1-PHYSICAL's open map.

## Layer-0 echo (read first this pass)

`GEOMETER-VS-PHYSICS-OBJECTS.md` (fork rule; rows 21, 24, 30) and
`lab/process/NAMES.md` (all eight collisions) were read before computing.
Persons: Weinstein is the author (they/them); Curt Jaimungal is an expositor,
not formula authority (they/them). Operative rows here: the "chirality"
four-way homonym (sense (a) only, above); "carrier" = the rank-1,920
conditional real-K77 principal carrier, not ker(Gamma) and not W; settled
REAL-CLIFFORD-FORM arena Cl(7,7) = M(128,R); no ambient-signature claim.

## Interface and fixtures (anti-redo)

Interface I per the packet: `(V, X, P_sym, P_skew, D)`, `V = R^1920 =
(Omega^0+Omega^1)(S) = (1+14) x 128` with the fixtures' block order (14
one-form blocks, then the zero-form block); X = blockdiag(omega) splitting
960+960 (each 128 = 64+ + 64-); horns = the two v0.174 pairing lines, both
rank 1,920 at both primes. The operator family was NOT rebuilt: the frozen
fixture `tests/channel-swings/selected_k77_action_adjoint_weight_classification_probe.py`
was executed unmodified at the pin (37 PASS, log attached), and the probe's
integer rebuild of the same Clifford/pairing objects is tied to it by the
regression control (control i), which reproduces its classification lines
`(1,1,1,1)` (anti-self-adjoint) and `(1,-1,-1,1)` (self-adjoint), rank 3 /
kernel 1, 14-axis alternation, the scrambled plant, the chiral-rescaling
identity, and the zero-weight-equations result, at both primes. The v0.173
completion probe (`selected_k77_wedge_shiab_southeast_completion_probe.py`)
supplied the wedge/km/co/southeast cell conventions read directly from its
source.

## Scoped rulings (ambiguities stated, packet-supported readings chosen)

1. **L1 = the Spin-natural ambient cell lattice, read as the equivariant
   zero-order algebra on the four ambient cells** {Omega^1+, Omega^1-,
   Omega^0+, Omega^0-}. The packet's kill quantifies over `dim Z_odd(P, L1)`,
   which is nonvacuous only if L1 carries the cross-degree cells; the
   per-cell dimensions land single-digit as the packet expects. SCOPED.
   Computed completeness: End_so(V) has dimension exactly 10 = 6 even + 4 odd
   (cell dims: 2/2/1/1 on the even diagonal, 1/1/1/1 on the odd cross-degree
   cells, 0 on the other eight lattice cells), certified at both primes by:
   exact S-cell commutants (End(S+-) = 1, Hom(S+,S-) = 0), Sylvester/charpoly
   coprimality for every S<->Psi and Psi+<->Psi- cell, squarefree charpolys
   (nonderogatory restriction) for End(Psi+-) = 1, with an
   associative-generic separating element (attempt 0; Lie-generic elements
   provably do not separate — weights coincide across non-isomorphic irreps —
   so quadratic enveloping words were required and used).
2. **L2 = the sixteen-cell eq (9.16) grammar, zero-order instantiation from
   the s9 extraction**: NW = Shiab-wrapped wedge-VEV cells (14 directions x 2
   chirality routings, X-odd), NE = km-VEV cells (28, X-even), SW = minus-star
   co-VEV cells (28, X-even), SE = displayed zero — the source-admitted
   nonzero rival is unspecified (SOURCE-ADMITS-UNSPECIFIED-RIVAL [SC-OP-05])
   and is excluded, SCOPED. The campaign's own complete sixteen-cell
   lower-order graph/Riccati is OPEN at the pin (v0.183 ledger sentence), so
   this L2 is the artifact's instantiation of the certified grammar, to be
   re-consumed from whatever the campaign later certifies (packet Lens 3
   discipline). The 84 generators are independent (rank 84), disjoint from L1
   (union rank 94), and contain zero equivariant elements (8-generator
   commutant of dimension 24 pruned to 0 by full 91-generator exact
   verification) — a frozen VEV value breaks Spin-naturality, as it should.
3. **The (9.16) plus/minus labels are NOT identified with the ambient
   omega-grading.** The s9 extraction certifies the cell ledger but "does not
   define the plus/minus grading"; L2's X-parities (NW odd, NE/SW even) are
   computed in the fixture carrier's own omega-grading. FRAME-SENSITIVE
   (finding F3 below).
4. **Swap decomposition of Z_even**: sigma(B) = Q B^T Q with Q =
   blockdiag(B_spin), the fixtures' cross-chiral bilinear ("the halves'
   pairing"), horn-independent and weight-free. FRAME-SENSITIVE (finding F1;
   hand audit below).
5. **Control (ii)'s "matched 64+ <-> 64- identity block"** realized as the
   zero-form B_spin block (the canonical matched map; the identity in a
   Bsp-adapted basis). SCOPED.

## Structural certificates (convention-free)

- `{X, P} = 0` exactly for BOTH horns (and the scrambled control): every
  natural pairing in the four-scalar family is purely cross-half — the
  concrete shadow, in this family, of the D7 half-spin duality (S+-^* pairs
  with the opposite half).
- Corollary, certified independently at every horn/layer: the
  single-half-supported admissible even cell is 0 — an X-even admissible B is
  the pairing-transport graph of its (+)-block, never independent on one
  half. A planted single-half mass (B_+ = P_+ on the zero-form sector,
  B_- = 0) is classified swap-asymmetric and REJECTED by the alternation
  test on both horns.
- Form symmetry: P_sym^T = +P_sym, P_skew^T = -P_skew (the v0.174 horn
  symmetries), both rank 1,920 at both primes.

## The odd (half-coupling) witnesses — the candidate VEV-term cells

- **L1 (equivariant layer), dim 2 per horn, with per-horn coefficient
  locks**: for P_sym the admissible combinations are (contraction + insertion)
  on each chirality routing, `C + E` per route; for P_skew they are `E - C`
  per route. These are cross-degree (Omega^1 <-> Omega^0) Clifford
  contraction/insertion pairs — the equivariant zero-order analogue of the km/co
  cell pair the completed operator itself carries; the relative-coefficient
  lock flips with the horn's adjoint parity (PROPOSED reading; the lock
  itself is a certified integer fact).
- **L2, dim 28 per horn = the full NW wedge-VEV cell**: every direction i and
  both chirality routings `wedge(i) o (1 +- omega)` are individually
  admissible on both horns. These are exactly the cells the v0.174 chiral
  weights multiply — the repo-side comparator (iv) of the packet's R1 list;
  the bridge from the source's varpi VEV (SC-CHI-01) to these cells remains
  the SCOPED-OPEN R1 placement question. Adversarial caveat (Lens E): given
  the v0.174 alternation identity for arbitrary nonzero weights, L2-odd >= 28
  was already implied linearly by the frozen bank; it is certified here
  independently, but the discriminating NEW number of this check is L1's
  odd = 2 with its locks — and the planted Dirac-type zero-form mass
  (B_spin block) is X-odd yet NOT admissible on either horn, so the
  admissible coupling space is strictly narrower than "any half-coupling
  mass": it selects the cross-degree locks and the wedge cells.

## KILL evaluation (certificate + packet grading; dispositions wave-owned)

Certificate: `dim Z_odd(P,L1) = 2` and `dim Z_odd(P,L2) = 28` for both horns,
integer-certified. The pre-declared kill condition (zero on both horns at
both layers => no pairing-compatible half-coupling deformation => R1 fails;
outcome (b)) evaluates **NOT FIRED**. This artifact is therefore not a kill
and its `target_claim` is NONE-NOT-A-KILL; no SC row is touched.

Packet outcome grading of the evidence pattern (the wave owns the filing):

- **(a)'s CHK-1 leg is satisfied**: `dim Z_odd > 0` for at least one horn (in
  fact both) at L1 and L2, controls green. Full outcome (a) additionally
  requires CHK-2 (anomaly ledger) and CHK-3 (nguyen C4 channel), which this
  check does not execute (CHK-3 dependency registered, not run —
  non-collision).
- **(c)'s datum stands documented**: a coupling-term SPACE exists, and the
  source fixes neither the horn nor the placement — the v0.174 fixture's own
  source return is SOURCE_SILENT_ON_K77_PAIRING_HORN_AND_INVARIANT_WEIGHT_
  PRODUCT_SELECTION; the s9 extraction certifies no global adjoint/domain
  [SC-OP-04] and an unspecified southeast rival [SC-OP-05]; the draft's
  dashed-line diagram carries no operator cells [SC-CHI-01 locus]. The cell
  table above is the register of what any future source display must select
  from: at L1 the two locked cross-degree combos per horn; at L2 the 28-dim
  wedge-VEV cell.
- **(d) was triggered by the labeled tripwire and is resolved by the hand
  audit below**: the re-derivation faulted the check-design's swap-cell
  labeling, not the R4a typing.

## TRIPWIRE evaluation and hand audit (packet outcome (d) prescription)

Raw certificate: under sigma(Q), `dim Z_even-asym(P_sym, L1) = 2` (and 14 at
L2 on both horns) — the tripwire condition as literally written FIRES on
P_sym at L1. Hand audit, both ways, run in-artifact:

1. The sigma(Q)-eigenclass of the even-admissible space FLIPS between horns
   (P_sym: sym 0 / asym 2; P_skew: sym 2 / asym 0; one further even direction
   is not sigma-homogeneous at L1, where even-sym + even-asym = 2 < 3 =
   even). Replacing tau by -tau — an equally natural reading of "identified
   under the halves' pairing" — swaps the labels between horns. The labeled
   cell is therefore FRAME-SENSITIVE (finding F1) and cannot, by itself,
   witness anything physical.
2. The convention-free content of the D7/R4a expectation is certified and
   holds: `{X,P} = 0`, the even-admissible space is a graph (B_- a
   pairing-transport of B_+, never independent), and the single-half-supported
   admissible cell is 0 at every horn and layer, with the planted single-half
   mass rejected. "Explicit asymmetry is expected unavailable" (packet R4a)
   is CONFIRMED in this construction.
3. Resolution: what needed re-derivation was the check design's swap-cell
   definition (the packet's own self-review Charge 1(iii) anticipated that
   its L1 summary would need re-derivation from the fixture); the R4a
   spontaneous-only reading survives. Nothing downstream is filed from the
   labeled firing; the wave consuming CHK-2/CHK-3 should consume the
   convention-free certificates, not the sigma labels.

## Controls (all green; polarity as computed)

| control | expectation | result |
|---|---|---|
| (i) regression, both primes | v0.174 two-horn classification exact | PASS: lines (1,1,1,1) anti / (1,-1,-1,1) self, rank 3, kernel 1; 14-axis alternation both horns; both ranks 1,920; rescaling preserves horns; zero weight equations (extra pairs (1,1),(2,5),(3,7)) |
| (ii) Dirac-type half-coupling plant (zero-form B_spin block) | classified Z_odd; admissibility computed, not assumed | PASS: X-odd; NOT alternating-admissible on either horn (computed) |
| (iii) single-half mass plant (B_+ != 0, B_- = 0) | lands in Z_even swap-asymmetric | PASS: X-even, sigma(B) != B, B_- block zero; rejected by admissibility on both horns |
| (iv) random non-equivariant B | rejected by L1 filter | PASS (exact commutator defect > 0) |
| (v) deliberately symmetrized P*B | rejected by alternation test | PASS |
| (brief) X-commuting plant | even cells only | PASS (zero X-odd component) |
| (brief) scrambled horn (1,1,-1,-1) | dimensions reported | same cell dims as the valid horns (L1 2/3, L2 28/28); it is distinguished not by the deformation cells but by the operator classification — the regression control certifies it is neither valid adjoint horn |
| anti-redo baseline | frozen fixture green at pin | PASS: 37 PASS / 0 FAIL |

## Five-lens pre-flight (brief v1.2 rule 14; run INLINE, retrospectively
against the finished computation, before the kill/tripwire evaluation was
written; declared bases and confidences)

- **Lens 1 — variational/operator theory** (basis: PRINCIPLE, plus DIRECT for
  the rescaling identity via control (i); confidence 0.8). A zero-order
  deformation B enters D + B below the first-order symbol; linearized
  conjugation of the family produces first-order objects, so the cells are
  not inflated by [Lambda, D]-type gauge directions. Pairing-preserving
  chiral isometries act WITHIN cells and preserve their dimensions (the
  v0.174 ratio-removal transport, reproduced exactly); the dims are raw
  admissible-cell dimensions, not moduli after that action — stated, graded.
- **Lens 2 — Grassmann/superalgebra typing** (basis: DIRECT; confidence 0.9).
  The admissibility used is exactly the v0.174-corrected criterion
  (alternation of the full quadratic coefficient (PB)^T = -PB, not operator
  self-adjointness), regression-tied to the frozen fixture at both primes;
  the odd-cell coefficient locks flip with the horn's adjoint parity, the
  signature of a genuinely Grassmann-graded pairing compatibility.
- **Lens 3 — source criticism: which VEV object would the cells host**
  (basis: DIRECT on register rows verified at the pin; confidence 0.85).
  SC-CHI-01's operative clause (sub-fields of varpi above zero, p.52) would
  populate exactly the L2 varpi-grammar cells computed here; SC-CHI-51's
  "field of VEV in a Dirac-like operator" is an operator-level zero-order
  term — hosted by these cells in sense (a) only; SC-CHI-52's
  curvature-coaxing (auxiliary) is dynamical and has no finite check here
  (R4d; "carried as an unpaid debt" per its adherence note). The source
  selects neither horn nor placement — outcome (c)'s datum, verbatim source
  returns cited above.
- **Lens 4 — Layer-0 semantics** (basis: DIRECT; confidence 0.9). X-odd/even
  is chirality sense (a); ker(Gamma)'s 832+- never enters; the (9.16) +-
  labels are display labels, not omega-grading (F3). THIS LENS CHANGED THE
  ARTIFACT: an earlier draft of the L2 grammar routed cells through
  omega-projected +- labels as if source-owned; the extraction's abstention
  forced the F3 marking and the "instantiation, not identification" wording.
- **Lens 5 — adversarial refutation: when is a nonzero cell NOT a VEV lever**
  (basis: PRINCIPLE; confidence 0.75). (i) Gauge-trivial inflation: the
  equivariance filter selects, it does not quotient; no quotient by carrier
  automorphisms is taken anywhere — dims are upper-level counts of admissible
  directions, and any moduli statement is future work; (ii) necessity
  caveat: L2-odd >= 28 follows linearly from the frozen bank's own
  alternation identity, so at L2 the kill could not have fired while v0.174
  stands — the informative new numbers are L1's odd = 2 locks and the
  admissibility REJECTION of the naive Dirac block; (iii) nonzero cells with
  no source selection support outcome (c), not a construction. THIS LENS
  CHANGED THE ARTIFACT: the outcome-grading sentence now carries the
  L2-necessity caveat and the "strictly narrower than any half-coupling
  mass" sharpening.

Declaration: the lenses were run inline (no subagents), retrospectively;
Lenses 4 and 5 changed typing sentences as marked; no lens changed any
certified number or the kill/tripwire certificates. Lens outputs are planning
evidence.

## FRAME-SENSITIVE findings (rule 13)

- **F1** — the even-sym/even-asym labeling under sigma(Q) flips between horns
  under tau -> -tau; any statement routing SC-CHI-01's or SC-CHI-53's "two
  chiral halves coupled by a VEV" through the swap-cell labels is
  frame-sensitive; the convention-free invariants (graph-tied halves,
  single-half cell = 0) are not.
- **F2** — "X-odd hosts the VEV coupling term" is a sense-(a) statement
  (ambient operator grading); reading it in sense (b) (observed Weyl) for
  SC-CHI-50/SC-CHI-51 crosses the PH-K1-PHYSICAL open bridge and is
  frame-sensitive until that map exists.
- **F3** — the (9.16) sixteen-cell +- labels vs the ambient omega-grading
  (SC-OP-04's certified grammar does not define the grading); L2's X-parities
  are computed in the fixture carrier's omega-grading.

## Three-charge self-review (same-pass)

**Charge 1 — where the summary outruns the artifact.** (i) "Candidate
VEV-term cells" is the packet's vocabulary; nothing here shows a VEV
dynamically populates the odd cells — the R1 bridge (source varpi placement
-> these cells) is SCOPED-OPEN and SC-CHI-52's dynamical half has no finite
check; the return states "candidate". (ii) "TRIPWIRE FIRED" as a headline
would outrun: it fired under a frame-sensitive labeling and the hand audit
resolves it; both facts are stated wherever either is. (iii) The L1
completeness equality is a mod-p upper bound meeting integer lower witnesses
at both primes; the Lie-theoretic multiplicity narrative is exposition, not
the certificate. List otherwise empty.

**Charge 2 — where rigor defends a superseded or mistyped object.** The
layers quantify over the v0.173/v0.174 completed family per the packet's
interface clause; a future campaign correction of the ALTERNATION criterion
itself would invalidate the admissibility condition (the packet's own
Charge-2 warning) — the executing wave re-verifies the criterion against the
then-current ledger. The L2 instantiation stands in for the campaign's open
v0.183 sixteen-cell lower-order object and must be re-consumed when that
lands. The s9 +- labels were not identified with the omega-grading (F3). No
(9,5)-horn machinery is premised anywhere. List otherwise empty.

**Charge 3 — what else must change if the result stands.** PH-K1-PHYSICAL,
the Witten-1983 exit, and the Rung 1 multiplicity fence — **survive**
(nothing here bridges to sense (b) or uses the 384 chirally). SC-CHI-51 and
SC-CHI-52 adherence notes — **needs-recheck** (outcome (a)-leg: the
deformation-space table now exists for their PARTIAL/ADHERED context to
cite). The packet's CHK-1 swap-cell specification — **needs-recheck** (F1:
the executing wave should pin the tau convention or consume the
convention-free certificates). The nguyen C4 channel — **untouched**
(dependency registered, not executed). Dissolved rows — **none** (stated
explicitly). Empty lists are stated as empty.

## Verify status manifest

- The cell-dimension table (all seven rows); the odd witnesses and their
  per-horn locks; {X,P} = 0; horn form symmetries and ranks 1,920; the
  single-half zeros; the L1 basis equivariance (91 generators, exact
  integers); L1 completeness = 10 (both primes, associative-generic attempt
  0); L2 independence (84), union rank 94, equivariant content 0 (pruned
  exactly); L0 arithmetic 1,842,240 / 2x960^2; all eight controls; the frozen
  fixture's 37 PASS at the pin; fixture byte-identity c789e75b -> 66144b87:
  **CONFIRMED** (exact integer certificates; two primes GF(1009), GF(1013)
  reported throughout).
- The L1 lattice reading; the L2 instantiation pending the campaign's
  sixteen-cell object (v0.183 OPEN); the SE-cell exclusion; the
  B_spin realization of control (ii); the sigma(Q) convention (F1); the R1
  varpi-placement bridge; the (9.16) label non-identification (F3):
  **SCOPED**.
- The km/co-grammar reading of the L1 odd locks; the outcome typing
  suggestion ((a)'s CHK-1 leg + (c)'s datum, (d) resolved): **PROPOSED**
  (the wave certifies or refutes; dispositions wave-owned).

## What this artifact does not do

No registry, ledger, fence, canon, verdict, residue, adherence, or posture
change; no wave bound; no queue priority claimed; no kill made or implied
(target_claim: NONE-NOT-A-KILL); no repo file edited (repo READ-ONLY; all
outputs in the session scratchpad); no CHK-2/CHK-3 execution (dependencies
registered); no dark-typing chosen; no fork horn adjudicated; no sense-(b)
chirality statement made; the hostile review an executing wave owes is not
satisfied by the self-review above.
