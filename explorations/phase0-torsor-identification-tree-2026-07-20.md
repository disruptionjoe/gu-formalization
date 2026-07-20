---
title: "Phase-0 decision tree for ID-1: the native Sp(1)-torsor identification with carrier rep-weight -- minimal sufficiency, candidate ledger, negative control, kill-ordered branches"
doc_type: scoping_decision_tree
status: phase0_scoping (no Phase-1 node executed; small computations only, exit 0)
created: 2026-07-20
directed_by: "Joe direct chat, 2026-07-20 (Phase 0 scout A, ten-persona-amended)"
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
target: "ID-1 of explorations/torsion-generation-arena-2026-07-20.md (as re-specified by verify-torsion-arena-2026-07-20.md Sections B/E): the rep-weight half of the torsor demand -- the framing transforming in the carrier representation. Only the Z/2 co-flip shadow is verified, and it is rep-weight-blind."
probe: tests/channel-swings/phase0_torsor_checks.py
related:
  - explorations/torsion-generation-arena-2026-07-20.md
  - explorations/verify-torsion-arena-2026-07-20.md
  - explorations/sig-b5-habitat-verification-2026-07-20.md
  - explorations/source-packet-coflip-holonomy-freeze-2026-07-20.md
  - explorations/blockbuster-p5-instance-dossier-2026-07-19.md
  - explorations/d1-coperator-build-2026-07-19.md
  - explorations/operator-grade-end-2026-07-20.md
  - explorations/m1-third-reading-2026-07-20.md
  - explorations/W203-branch3-source-action-fixed-coefficients-2026-07-14.md
  - explorations/channel-swing-CH-REC-2026-07-19.md
  - explorations/global-anomaly-leg-2026-07-20.md
  - tests/channel-swings/sig_b5_habitat_probe.py
sources:
  - "Steenrod, The Topology of Fibre Bundles: principal G-bundle classification via [M, BG]; BSU(2) is 3-connected, so every principal Sp(1)-bundle over a 3-complex (S^3, RP^3) is trivial."
  - "Adams, J.F., On the groups J(X) IV, Topology 5 (1966): im J = Z/24 in pi_3^s; the framed class of S^3 with its Lie-group (left-invariant) framing generates im J (= nu up to sign)."
  - "Milnor, On manifolds homeomorphic to the 7-sphere (1956): p_1 = +-2(h-j) for the f_{h,j} clutchings -- the adjoint-type control arithmetic."
  - "Bott (1959): c : pi_3(O) -> pi_3(U) is x2; Dynkin-index additivity for pi_3(SU(2)) -> pi_3(U(N))."
---

# Phase-0 decision tree: the torsor identification ID-1

This is a SCOPING artifact. It produces no result on ID-1 itself; it fixes the
minimal target, the candidate ledger with validated kill tests, and the order
of Phase-1 swings. Everything sits on the framed-reading fork (R0_COND,
explorations/global-anomaly-leg-2026-07-20.md) and inherits the (9,5)
H-class conditionality of the frozen spine.

## 1. Minimal sufficiency (the target, shrunk)

**What the headline needs.** order(J(k)) = 3 iff gcd(k,24) = 8 iff
(v2(k) >= 3 AND 3 not | k). The full-carrier transport delivers k = 64; but
64 is sufficient, not necessary.

**Structural fact that shrinks the target (this is the load-bearing Phase-0
observation).** Any candidate identification for ID-1 is, by the demand's own
wording, a transport VALUED IN THE COMMUTANT ("whose induced twist is the
commutant action"). On a native carrier H^(64m), the commutant is M(m,H)
(unit group Sp(m)); every algebra-invariant sub-carrier has H-multiplicity
64j. The complexification of the realified carrier assigns the framing twist
winding 128c for a family of pi_3(Sp(m))-class c, hence (Bott c = x2):

    k = 64c,   c = the pi_3-class (degree) of the transport in the commutant.

So v2(k) >= 6 >= 3 is AUTOMATIC for any nonzero natural (= commutant-valued)
transport -- it is the verifier's M1 fact (frozen irrep H-dimension 64 = 2^6)
doing the work, with NO rep-weight hypothesis beyond naturality. Probe check
[M]: k = 64c lands in {0, 8nu, 16nu} for every integer c, order 3 iff
3 not | c.

**The minimal sufficient statement (MS).**

> MS: There exists a native transport of stable framings around the S^3
> double cover of the fiber core that (a) is equivariant for the frozen
> Cl(9,5) algebra action (equivalently: commutant-valued at every point),
> (b) restricts on the deck Z/2 to the machine-verified co-flip (-1 acts as
> -I: center-faithful), and (c) has pi_3-degree c in the commutant with
> c != 0 mod 3.

For a torsor-type identification, c = +-1 always, so (c) is automatic and MS
collapses to: SOME algebra-equivariant identification exists at all. The
"full carrier rep" formulation is the special case c = +-1, m-block-diagonal;
it is NOT needed. Answering the prompt's sub-questions: a quaternionic-
dimension-8 subrepresentation "transforming correctly" is NOT actually
available as a weaker option -- algebra-invariant sub-carriers come only in
H-multiplicity 64j, so the naturality requirement itself forces v2 >= 6; the
weakening that IS real is the degree c (any c with 3 not | c works) and the
sub-carrier count j (3 not | jc for a proper sub-carrier transport).

**What changes if only MS is ever proven.** Nothing that is currently
delivered. Probe check [M]: the orientation-unpinned class SET {8nu, 16nu}
is IDENTICAL for every k with 8|k, 3 not | k. The full-carrier value 64
already leaves the residue (8 vs 16, e-invariant 1/3 vs 2/3) unpinned
because the orientation sign is honest +-. So the exact class {8nu vs 16nu}
is not currently distinguished by ANY branch; only the ORDER (and the
subgroup, hence the index reading = 8) is delivered either way. The exact
class matters downstream ONLY if Scout B's dictionary turns out to read the
mod-3 residue / e-invariant -- see Section 5.

## 2. The candidate ledger

Shared naturality specification (category obligation). A candidate is a map
Phi : S^3-cover (basepointed at v0) -> Sp(m)_commutant such that
(i) DOMAIN: the S^3 double cover of the fiber-core RP^3 (machine-verified
retraction, sig_b5_habitat_probe.py); (ii) CODOMAIN: the unit group of the
commutant of the frozen Cl(9,5) action on the native carrier;
(iii) NATURALITY: the induced framing twist commutes with every carrier map
in the frozen ledger -- concretely, pointwise commutant-valuedness against
all 14 algebra generators (linear part: [X, e_a] = 0; antilinear part:
e_a C = C conj(e_a)) AND deck-restriction = the verified co-flip.

Validated kill tests (power demonstrated in tests/channel-swings/
phase0_torsor_checks.py, exit 0, 0.4 s):

- **Test N (naturality / commutant-valuedness).** One commutator battery
  (14 generators) on fixtures. POWER: kills R2 (the known rep-weight-blind
  metric/spin transport; residual 2.00) and the plant (Section 3); passes R1
  (the known k = 64 commutant family) bit-exact (0.0 linear and antilinear).
  A test that passed R2 would be broken; this one does not.
- **Test Z (center-faithfulness).** The verified deck monodromy -I already
  excludes every transport whose Sp(1)-weight content is even-only (adjoint,
  V_3, V_5, ...): adjoint(-1) = identity rotation (probe [Z], exact). This
  extracts NEW power from the existing Z/2 receipt: the shadow is
  rep-weight-blind only AMONG center-faithful reps.
- **Test W (degree mod 3).** For survivors of N: the pi_3-degree c of the
  transport in the commutant; kill if c = 0 mod 3 (class dies), else order 3.
  Structural (weight decomposition), no quadrature needed.

| Candidate | Precise object (domain -> codomain) | Frozen source | Test N (naturality) | Cheapest decisive kill + demonstrated power | Import price | Features (source / equivariance / grade) |
|---|---|---|---|---|---|---|
| **K1 record-current transport** | v |-> the commutant unitary that conserves/intertwines the current J^a = Re<Psi, K_S e_a Psi> along the core family; S^3-cover -> Sp(1)_comm | W203 Sect. "promotion-gate record current"; ch_rec_coflip_probe.py; CH-REC identity | open: is the current-defined transport commutant-valued? one battery on fixtures | Test N (power: killed R2/plant, passed R1); then Test W | 0 if the conservation rule is canonical; +1 posit if a gauge choice enters | record sector / bilinear-equivariant / grade-1 (vector) |
| **K2 C-operator weld** | v |-> C(v) C(v0)^(-1) where C(v) is the D1-built C-operator at anchor v; S^3-cover -> Sp(1)_comm, IF the admissible-C set at each anchor is an Sp(1)_comm-torsor | d1-coperator-build-2026-07-19.md (headline: C-determination FAILS at degenerate anchors by NON-UNIQUENESS, an admissible continuum); d1_coperator_build_probe.py | open: the continuum's shape IS the question | shape-of-ambiguity check: compute the admissible-C set at one frozen degenerate anchor; kill if it is NOT a free commutant orbit (then no canonical map without a choice); power: the same fixture already separated Jordan-form vs continuum failure shapes | 0 if the continuum is exactly a commutant torsor (then the "failure" IS the torsor structure); +1 posit otherwise | Krein/PT sector / spectral / antilinear |
| **K3 Sigma connection dressing** | v |-> holonomy of the bicomplex dressing W = 1.0 Sigma_09 + 0.7 Sigma_12 around the core family; S^3-cover -> U(128) | operator-grade-end-2026-07-20.md Sect. 5 (Discovery 1: all 91 so(9,5) generators J_quat-REAL; the K_S-forced i makes every honest even dressing J-ODD) | expected FAIL: algebra-valued (so(9,5) subset Cl-even), and J-odd by receipt | Test N, one commutator (power as above); receipt already says the dressing is not H-linear | 0 (but expected dead) | connection sector / algebra-side / Clifford-even |
| **K4 co-flip x commutant via the current bridge** | v |-> q(v) in Sp(1)_comm through the bridge tensor B: v |-> q built from the J^a bilinear (the current couples the index a to carrier bilinears -- the only frozen object bridging model-space directions to the commutant); S^3-cover -> Sp(1)_comm | W203 (J^a); sig_b5_habitat_probe.py Part C (co-flip); source-packet-coflip-holonomy-freeze (commit 32e3603) | open: is B Sp(1)-equivariant and nondegenerate? | bridge nondegeneracy: evaluate B on fixtures; kill if B vanishes or fails equivariance (Test N on the induced family); power: as above | 0 if B is forced; +1 if a frame isomorphism R^4_model = H_comm must be chosen (the naive "identify v with a quaternion" version pays this price) | record+torsor / bilinear / mixed grade |
| **K5 both-modes pairing transport (m1)** | continuity transport of the conserved indefinite pairing (V = K_S, mode exchange = J_quat) along a family; DOMAIN MISMATCH: m1's family lives over N2 degeneration rays, not the fiber core | m1-third-reading-2026-07-20.md; m1_third_reading_probe.py | fails as stated: wrong domain; needs a rays->core bridge built first | naturality-of-domain: no map S^3-cover -> ray family in frozen material | +1 minimum (the domain bridge is a new construction) | crossing sector / K_S-J_quat-equivariant / wall-grade |
| **K6 LITERATURE branch** | classification input, not a transport: BSU(2) is 3-connected => EVERY principal Sp(1)-bundle over S^3 or RP^3 is trivial; torsor identifications exist freely and are unique up to homotopy and degree +-1; S^3 with its Lie-group framing represents the generator nu | Steenrod; Adams J(X) IV (Lie framing of S^3 generates im J) | n/a (it is the naturality BACKGROUND) | none needed; it KILLS a candidate class instead: any Phase-1 node whose goal is "construct/classify the abstract torsor" is VACUOUS -- existence is classical and free | 0 | external / classical / stable |
| **K7 [PLANT -- negative control]** | v |-> K_S Lambda(v) K_S^(-1) ("record-weighted spin transport"): unitary family, correct deck monodromy, record-operator dressed -- looks plausible | constructed for this tree | KILLED: residual 2.00 (algebra-valued) | Test N killed it at cost ~0.1 s; the Z/2 shadow test did NOT (deck monodromy -I exact, 1.2e-16) -- see Section 3 | n/a | plant / algebra-side conjugate / rep-weight-blind by construction |

Ledger notes. (1) K1 and K4 share the record current as source; they are kept
as separate rows because K1 transports BY conservation while K4 uses the
current only as the model-space-to-commutant bridge tensor; if Phase-1 finds
the conservation rule and the bridge coincide, the rows merge. (2) K6
re-aims the whole tree: since torsor EXISTENCE is classical and free, every
surviving branch is really about NATIVITY (is the transport forced by frozen
material) and DEGREE (c mod 3) -- never about existence.

## 3. Negative control (counterfactual obligation)

The plant K7 (K_S-conjugated spin lift) was constructed to maximize surface
plausibility: it is unitary, deck-monodromy-correct (-I exact), and dressed
in the record operator K_S -- and it is PROVABLY rep-weight-blind (winding
is conjugation-invariant, so it equals R2's measured zero). Pipeline outcome
(tests/channel-swings/phase0_torsor_checks.py, exit 0):

- **Killed by: Test N** (commutant-valuedness), residual 2.00 against the
  algebra generators. **Cost: one commutator battery, ~0.1 s.**
- **NOT killed by the Z/2 shadow test** (deck monodromy -I to 1.2e-16) --
  a live demonstration of the verifier's point that the shadow is
  rep-weight-blind, and confirmation that the pipeline's FIRST real gate is
  Test N, not the shadow.

The pipeline kills its own plant. The tree stands.

## 4. Kill-ordered tree (cheapest-kill x prior plausibility)

Value floor reference: the build ID-1 would prevent/enable is the
unconditional order-3 mechanism (the largest single open payload in the
arena result). Any branch whose decisive test costs more than a medium
swing is parked.

**Node 0 (done, free) -- K6 literature.** Torsor existence classical.
CONSEQUENCE: prune all "construct the torsor" formulations; retarget every
branch at nativity + degree. No kill/survive fork -- it is background.

**Node 1 (small) -- K3 Sigma dressing, expected kill.** Decisive: Test N on
the dressing generator (one commutator battery; receipt operator-grade-end
Discovery 1 already types it J-ODD/algebra-side). KILL (expected): residual
O(1) -> K3 dead as an ID-1 candidate; feature-attribution datum: algebra-
side + Clifford-even => rep-weight-blind (matches R2, plant). SURVIVE
(unexpected): a commutant-valued component inside the dressing would be a
NEW frozen source for K1/K4 -- escalate its weight decomposition (Test W).

**Node 2 (small) -- K2 C-weld ambiguity shape.** Decisive: on the frozen D1
degenerate-anchor fixture, compute the admissible-C set's orbit structure
under the commutant: is it a FREE Sp(1)_comm-orbit? KILL: the set is bigger
than one commutant orbit (or not an orbit at all) -> no canonical weld
without a new posit -> K2 parked at import price +1. SURVIVE: the D1
"non-uniqueness failure" is exactly commutant-torsor freedom -- then the
S^3 family of admissible-C sets IS a native Sp(1)-torsor bundle over the
core, and ID-1's torsor half is supplied by the C-operator itself. Sets up:
Test W on the weld family (degree c), then the framed-fork commitment.
Prior: medium (the D1 receipt's failure shape -- "admissible continuum on a
diagonalizable, sign-blind degeneracy" -- is at least Sp(1)-shaped).

**Node 3 (small-medium) -- K4 bridge tensor.** Decisive: build B from the
J^a bilinear on fixtures (one contraction), check nondegeneracy and
Sp(1)-equivariance, run Test N on the induced family. KILL: B degenerate or
non-equivariant -> the only frozen model-space-to-commutant bridge fails ->
K4 dead AND K1's naturality prior drops (shared source). SURVIVE: q(v) is a
native torsor identification with degree +-1 -> MS clauses (a),(b),(c) all
land -> ID-1 CLOSES at minimal-sufficiency grade; sets up the residue
question (Section 5) and the framed-fork commitment as the only remaining
conditions. Prior: highest (the demand's own wording is realized by the only
bridge object the frozen ledger contains).

**Node 4 (medium) -- K1 conservation transport.** Decisive: define the
transport by J^a-conservation along the core family on fixtures; Test N;
then Test W. KILL: transport forced non-commutant (residual O(1)) or
degree 0. SURVIVE: independent second construction of MS -- corroborates
K4 or replaces it if K4 died. Run AFTER K4 (shared source; K4 is cheaper
and its kill informs this node).

**Node 5 -- K5 m1 pairing. FLOOR-FAIL: PARKED.** Its cheapest decisive test
requires first BUILDING a rays-to-core domain bridge (a new construction,
import price >= 1) -- more than the value its survival would add over
K1/K4 (it would deliver the same MS through a longer path). Do not scope
further unless Nodes 1-4 all die.

**Exhaustion clause (kill-defense discipline).** If Nodes 1-4 all KILL: run
the pre-declared reframe pass before any program-level conclusion -- the
enumeration above is candidates-from-frozen-material; a reframe that
explains the kills (e.g., "the commutant is reachable only through the
physics-side objects") must be attempted and priced before invoking
Section 6.

## 5. Joint dependency graph (Scout B dictionary-sensitivity)

Scout B owns the order-3-class -> integer-3 dictionary gate (H6 limit b)
and the reading fork (order vs subgroup-index vs residue/e-invariant).

- **If only the ORDER matters** (or the subgroup-index reading, which both
  8nu and 16nu satisfy identically): ALL surviving branches are equivalent
  in payoff; MS suffices; the {8nu vs 16nu} residue never needs pinning.
  Branches K1-K4: dictionary-INSENSITIVE at this level.
- **If the dictionary reads the RESIDUE / e-invariant (1/3 vs 2/3)**: every
  branch must ADDITIONALLY pin a native orientation of the S^3 cover (the
  +- sign), which NO current branch delivers (the full-carrier result is
  equally unpinned). Mark: K4/K1 residue-capable only if the bridge tensor
  B also fixes an orientation (possible -- B is built from a grade-1
  current, which is orientation-sensitive); K2 residue-capable only if the
  weld family is canonical including sign. This is the ONLY payoff
  difference between branches.
- **If Scout B lands the INDEX reading**: the occupant reads 8, not 3 --
  the entire order-3 line changes meaning regardless of any transport
  result here. That outcome feeds Section 6(b), not any single branch.
- Scout B's framing-reading verdict (operator-grade territory) gates ALL
  nodes identically (the R0_COND fork): no branch is differentially
  sensitive to it.

## 6. Program-level kill (pre-committed)

Abandon the ENTIRE order-3 line (not just a branch) if ANY of:

- **(a) Naturality exhaustion with reframe.** Nodes 1-4 all die by Test N/W,
  the Section 4 exhaustion-clause reframe pass fails to produce a priced
  alternative, AND it is shown that any commutant-valued transport on the
  frozen material requires positing the identification as a new N-item
  (import price >= 1 on every route). Then ID-1 is permanently an
  obstruction-spec (outcome shape ii), never a mechanism, and the line
  reverts to "located, not forced" with the occupant conditional forever.
- **(b) Dictionary closes against order.** Scout B proves the well-typed
  dictionary must read the subgroup-index (= 8) or a residue inconsistent
  with any native orientation -- the arena occupant then does not read 3
  under any surviving branch.
- **(c) Framed fork resolves negative.** A proof that stable framings on
  the fiber core can couple only to the metric/spin transport (i.e., the
  carrier reading of Pontryagin-Thom framing is not available to the
  program) -- then k = 64 is unreachable in principle: R2 = 0 becomes the
  final word and the arena stays empty of native occupants.

Condition (a) is this scout's own exhaustion; (b) and (c) are Scout B /
operator-grade deliverables. Any one suffices; none has fired.

## 7. Survivor-bias disclosure (what this tree cannot see)

- **Non-commutant nonzero transports.** The ledger enumerates ID-1
  candidates, which are commutant-valued BY DEFINITION. A native transport
  that is NOT commutant-valued but still winds nonzero (e.g., a grade-3 /
  torsion-type family -- operator-grade Discovery 1 shows grade-3 terms
  break S_VJ and carry forced i's) would be a DIFFERENT mechanism for the
  same arena, invisible here. Test N would (correctly, per ID-1's spec)
  kill it; nobody would notice its winding.
- **Physics-side constructions.** Per the GEOMETER-VS-PHYSICS fork
  discipline, a standard-field-side object (e.g., an instanton number of a
  dynamical gauge field) could occupy the arena; the enumeration is
  program-native-side only.
- **Kill-test power gaps.** Test N's power is demonstrated against
  algebra-valued impostors (R2, plant). Its power against MIXED candidates
  (commutant + algebra components) is undemonstrated: a mixed family could
  fail the battery while carrying a genuine commutant part. Phase-1 should
  project onto the commutant before killing, not after.
- **The framing reading itself may be wrong.** Whether the carrier
  transport acts on stable framings AT ALL is the framed-reading fork --
  Scout B / operator-grade territory (Section 6c). Every branch here is
  conditional on it; the tree cannot test it.
- **The C-04 rep/geometric fence.** The verifier's new control (geometric-3
  carrier H^192 gives the ZERO class) bounds every branch: if the true
  native carrier is ever retyped geometric-side, all branches die at once;
  no kill test here detects that retyping.

## Appendix: Phase-0 computations (receipts)

tests/channel-swings/phase0_torsor_checks.py -- ALL PASS, 9 checks, exit 0,
0.4 s, deterministic, on the frozen gen_sector_bridge rep. Command:
`python tests/channel-swings/phase0_torsor_checks.py`. Contents: [T] fixture
sanity (J_quat^2 = -1 exact, K_S Hermitian unitary); [N] naturality battery
power validation (R1 passes 0.0/0.0; R2 killed, residual 2.00; plant killed,
residual 2.00, while passing the Z/2 shadow test at 1.2e-16); [Z] adjoint of
-1 = identity (center-faithfulness excludes even-weight transports via the
existing deck-monodromy receipt); [M] minimal-sufficiency arithmetic
(order 3 iff 8|n and 3 not | n, n = 1..399; k = 64c in {0, 8nu, 16nu} with
order 3 iff 3 not | c; class set {8nu, 16nu} identical across all
qualifying n). No Phase-1 node was executed.
