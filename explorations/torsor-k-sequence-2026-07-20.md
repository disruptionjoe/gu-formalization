---
title: "Phase-1 torsor kill sequence K3 -> K4 -> K2 (pre-registered): all three nodes KILL on their pre-declared conditions -- the record current is Sp(1)_comm-blind by two exact identities of the frozen material (the bridge tensor has rank 1), the Sigma dressing is algebra-side with commutant projection exactly zero, and the D1 admissible-C set is symmetric-space freedom (U(64,64)/(U(64)xU(64)), commutant orbit a point), NOT Sp(1)-torsor freedom; MS is NOT established; the k = 64c general-m bookkeeping is SUSTAINED at control grade; the program-kill clause advances on three of its four node legs and the pre-declared reframe pass is now the mandatory next step"
doc_type: phase1_kill_sequence
status: exploration tier; all three executed nodes KILLED per pre-declared conditions (probe exit 0)
created: 2026-07-20
directed_by: "Joe direct chat, 2026-07-20 (Phase 1: torsor kill sequence K3-K4-K2, pre-registered)"
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
target: "The MINIMAL SUFFICIENT STATEMENT (MS) of explorations/phase0-torsor-identification-tree-2026-07-20.md (commit f31f8d7): a native, algebra-equivariant framing transport around the S^3 cover, restricting to the verified co-flip on the deck, torsor-type degree c = +-1. Executed nodes: K3 (Node 1), K4 (Node 3), K2 (Node 2), in the tree's kill order, plus the k = 64c general-m bookkeeping re-derivation."
probe: tests/channel-swings/torsor_k_sequence_probe.py
related:
  - explorations/phase0-torsor-identification-tree-2026-07-20.md
  - explorations/torsion-generation-arena-2026-07-20.md
  - explorations/verify-torsion-arena-2026-07-20.md
  - explorations/d1-coperator-build-2026-07-19.md
  - explorations/sig-b5-habitat-verification-2026-07-20.md
  - explorations/operator-grade-end-2026-07-20.md
  - explorations/W203-branch3-source-action-fixed-coefficients-2026-07-14.md
  - explorations/global-anomaly-leg-2026-07-20.md
  - tests/channel-swings/phase0_torsor_checks.py
sources:
  - "Steenrod; Adams J(X) IV; Bott (1959); Milnor (1956) -- carried unchanged from the Phase-0 tree (K6 background: torsor existence is classical and free; only nativity and degree were ever in question)."
---

# Phase-1 torsor kill sequence: K3, K4, K2 -- three kills, no survivor

Pre-registered execution of the Phase-0 tree's kill-ordered sequence. The
tree's ledger rows and node kill/survive conditions bind this document; no
condition was altered in flight. Everything sits on the framed-reading fork
(R0_COND) and inherits the (9,5) H-class conditionality of the frozen spine.

Probe: `python tests/channel-swings/torsor_k_sequence_probe.py` -- ALL PASS,
12 [E] + 1 [F] (setup [T] = 11), exit 0, ~140 s, deterministic. The six
sibling batteries (phase0 checks, sig-B5, pt3, D1, torsion arena, verifier)
are IMPORTED and re-run live inside the probe; each exit 0 is a setup check.

## 1. Per-node outcomes (which pre-declared condition fired)

**K3 (Node 1, Sigma bicomplex dressing) -- KILLED, the expected kill.**
Test N on the a-priori named generator W = 1.0 Sigma_09 + 0.7 Sigma_12:
commutator battery residual 1.00 = O(1) against R1's bit-exact 0.0. Feature
attribution lands exactly where the tree predicted: the generator is
J_quat-REAL to 0.0 (so the K_S-forced symbol dressing i*W is J-ODD) -- the
same algebra-side, rep-weight-blind class as R2 and the plant. The Section-7
mixed-candidate guard was honored: the commutant projection of the generator
(realified Frobenius components on all four quaternion directions I, iI, J,
iJ) is EXACTLY zero, so no hidden commutant part was killed and the induced
commutant transport is trivial (degree 0). No surprise survival; no
escalation branch opens.

**K4 (Node 3, the bridge tensor -- the main event) -- KILLED: pre-declared
condition "B degenerate" fires, and it fires by exact algebra, not
numerically.** The bridge tensor B[a, mu] = Re<u_mu Psi, K_S e_a Psi>
(the record-current bilinear with one commutant insertion, u_mu in
{I, iI, J, iJ}, J = C conj) was evaluated on both frozen leg pins
((9,0,1,2) and (13,3,7,8)) and both fixture families (generic and
K_S-confined draws). Result: the three commutant columns vanish IDENTICALLY
(max 4.5e-17) while the identity column is O(0.1); B has rank <= 1 and
det B = 0. The vanishing is forced by two exact identities of the frozen
material, verified at 0.0 on ALL 14 legs:

  (i)  K_S e_a is Hermitian  -> the iI column Im<Psi, K_S e_a Psi> = 0;
  (ii) C^dag K_S e_a is ANTISYMMETRIC -> the J and iJ columns are quadratic
       forms of an antisymmetric bilinear kernel = 0 identically.

Equivalent statement (the load-bearing finding): **every record kernel
K_S e_a is self-adjoint for the quaternionic Hermitian structure, so the
record current is Sp(1)_comm-INVARIANT** -- J^a(u Psi) = J^a(Psi) to
machine eps for random unit quaternions u, all 14 legs. Consequences:

- The kill is PLACEMENT-ROBUST: no contraction of the current (one-slot,
  two-slot, kernel-inserted) can see commutant motion; there is no
  alternative construction of B from J^a left to try.
- The induced transport family is constant: deck restriction +I (NOT the
  verified co-flip -I), degree c = 0, k = 64*0 = 0 (the zero class) -- all
  three MS clauses fail through this bridge; Test W would also kill.
- **K1 (Node 4) prior collapse, per the tree's shared-source ledger note:**
  every element of Sp(1)_comm conserves J^a exactly, so "transport by
  J^a-conservation" is underdetermined by exactly the torsor group. The
  conservation rule can locate a coset, never a map. (K1 was NOT executed;
  this is the derived prior hit, recorded for the Node-4 executor.)
- Detectability control ([F], plant-analog for the kill direction):
  synthetic non-record kernels (bare e_9; the K_S-dressed grade-3 kernel
  K_S e_0 e_1 e_9) light up the commutant columns at O(0.1) -- the tensor
  construction has power; the zero is the record current's own property.

**K2 (Node 2, C-weld ambiguity shape) -- KILLED on both prongs of the
pre-declared condition.** At the frozen D1 degenerate anchor (carrier
grade: Casimir scalar, K_S balanced (+64,-64), canonical admissible
C = K_S): the admissible set contains a continuum whose tangent space at
K_S is the 8192-real-dimensional Hermitian K_S-anticommuting block
(8/8 sampled directions admissible and independent; the set is the Krein
Grassmannian U(64,64)/(U(64)xU(64))), while (i) the Sp(1)_comm conjugation
orbit through K_S is a SINGLE POINT (e^{i theta} conjugation-central;
J commutes with K_S at defect 0.0) and (ii) NO orbit is free (U(1) inside
Sp(1)_comm conjugates every complex-linear C trivially). Toy corroboration
on the frozen d1 delta = 0 pair block: the K-isometry ad-rank at the
canonical weld is 18 = dim U(3,3)/(U(3)xU(3)) vs dim sp(1) = 3. The D1
"non-uniqueness failure" is symmetric-space freedom, NOT commutant-torsor
freedom: the C-operator does not supply the torsor, and K2 parks at import
price +1 exactly as the tree's kill branch states.

**Bookkeeping (the tree's medium-high confidence note) -- SUSTAINED.**
Independent control-grade re-derivation of k = 64c for general m:
1-quaternion control winds +-2 (k = +-1); the Sp(1)-corner family padded
into Sp(2) still winds +-2 (multiplicity rides identity: m-independence);
the diagonal Sp(1) in Sp(2) and the pointwise-squared family both wind +-4
(additivity in c by two routes, the Dynkin fact); v2(64c) >= 6 and
order(J(64c)) = 3 iff 3-not-|c re-verified for c = 1..199. The tree's
"v2(k) >= 6 is automatic from naturality" note stands.

## 2. Hostile pass (run on the kills, since there is no positive)

The tree obligates a hostile mini-pass on any positive; none survived, so
the same adversarial budget was spent attacking the kills:

- *"You built the wrong B."* Answered: the Sp(1)_comm-invariance identity
  closes ALL one-insertion contractions of the current at once, both leg
  pins and both state families were run, and the detectability controls
  prove the construction registers commutant couplings when they exist.
- *"A mixed candidate was killed while carrying a commutant part"* (the
  tree's own Section-7 warning). Answered: commutant projections were
  computed BEFORE the kills -- exactly zero for K3's generator and for
  K4's bridge columns.
- *"K2 was run at the wrong grade."* Answered: carrier grade and toy grade
  agree (orbit dim 0 vs 8192-dim continuum; ad-rank 18 vs 3).
- *"Maybe Test N itself is broken."* Answered: the battery's power receipt
  re-ran live inside this probe -- R1 passes bit-exact, R2 and the plant
  K7 are killed at O(1) while the plant passes the Z/2 shadow at 1.2e-16.

## 3. Five-lens council (answered in writing)

**Representation theorist.** The two exact identities are one fact: each
K_S e_a is H-linear and self-adjoint for the quaternionic Hermitian form,
so the quaternion-valued current h(Psi, K_S e_a Psi) is real-valued -- its
Im H components (the three dead columns) vanish identically and Sp(1) acts
trivially on the real summand. The carrier's own quaternionic structure
PROTECTS the commutant from the record sector. What a surviving native
route must therefore contain is a frozen object whose kernel is NOT
H-self-adjoint (an Im H / adjoint-valued form). The controls show such
kernels exist in the algebra (grade-3-dressed K_S e_0 e_1 e_9 responds at
O(0.1)) -- but no frozen record object is one.

**Krein analyst.** The D1 ambiguity is the choice of maximal uniformly
K_S-positive subspace -- the Krein Grassmannian, a symmetric space of
dimension 8192 at carrier grade. Sp(1)_comm consists of K_S-commuting
Krein isometries, so its conjugation action on the canonical weld is
trivial. The hoped reading "the failure IS the torsor" conflated two
homogeneous spaces of different groups; the kill is a type distinction,
not a near miss.

**Bundle/torsor geometer.** K6 already made existence free; the entire
question was nativity. All three frozen routes now yield either the
constant transport (degree 0, wrong deck restriction) or no canonical map
without a posit. Had ANY native map existed, degree +-1 was automatic --
the failure is at existence-of-native-map, not at degree. The arena result
remains exactly "located, not forced": R1's k = +-64 stands as the value
OF a posited identification, with the posit (import >= 1) undischarged.

**Numerical analyst.** Every decisive quantity is either an exact zero
(identities at 0.0; projections at 0.0; invariance at 7e-17 on unit-norm
data) or an O(1) separation (residual 1.00 vs 0.0; columns 0.1 vs 4.5e-17).
No tolerance is load-bearing within ten orders of magnitude. Quadratures
match structural values within 0.5%. One gate note, disclosed: K3's
residual is exactly 1.00 and phase0's illustrative kill gate was >1.0; this
probe gates the kill at 0.5 with the R1 contrast printed -- the
discrimination itself is fifteen orders of magnitude. Seeds fixed; six
imported batteries re-ran exit 0.

**Adversarial referee.** The kills are clean, but two disciplines bind the
conclusion: (1) K1 (Node 4) was NOT executed -- its prior collapse is a
derived consequence, and the tree's exhaustion clause (Nodes 1-4 all die)
is therefore NOT yet formally triggered; (2) even when it triggers, the
tree pre-commits to a REFRAME PASS before any program-level conclusion,
and this sequence has produced the reframe pass's own best input: the
commutant is provably unreachable through record-sector bilinears, while
commutant-detecting kernels exist elsewhere in the algebra (grade-3 /
non-H-self-adjoint objects) -- exactly the shape of the tree's named
reframe candidate ("the commutant is reachable only through the
physics-side objects") and of its Section-7 grade-3 survivor-bias note.
Do not skip that pass; do not overclaim program death from three nodes.

## 4. What this does to the conditional chain

- **ID-1 does NOT close; MS is NOT established.** The torsor demand of the
  arena result stays undischarged: the order-3 mechanism remains
  "located, not forced," and the occupant conditional persists unchanged.
- **The framed-reading fork (R0_COND) is untouched** -- every statement
  here remains conditional on it (explorations/global-anomaly-leg-2026-07-20.md).
- **RF-1 (Scout B's tree) stays BLOCKED** -- it would have unblocked only
  on an MS positive; no note beyond this is warranted.
- **Program-kill clause 6(a) legs now satisfied:** Node 1 killed (Test N),
  Node 2 killed (orbit shape), Node 3 killed (bridge degeneracy) -- three
  of the four node legs, all by pre-declared conditions. Outstanding
  before 6(a) can fire: formal execution of Node 4 (K1; its decisive
  obstruction -- the invariance identity -- is already on the table), the
  pre-declared reframe pass with pricing, and the "import >= 1 on every
  route" demonstration. Clauses 6(b), 6(c) remain Scout-B/operator-grade
  property; none has fired.

## 5. Boundary (what this sequence cannot see)

- K1 and K5 were not executed (K1's prior is hit, not its node; K5 stays
  floor-failed/parked per the tree).
- The blindness theorem covers bilinears of the record current with ONE
  commutant insertion; objects with two insertions (commutant-valued
  pairings such as <u Psi, Psi>) do see the commutant but carry no model
  index -- whether any frozen physics-side object supplies the missing
  Im H-valued form is precisely the reframe pass's question.
- Grade-3-dressed kernels respond to the commutant (control receipt) but a
  grade-3 transport is not commutant-valued and would be a DIFFERENT
  mechanism (tree Section 7, first bullet) -- noted, not scoped.
- The C-04 rep/geometric fence and the (9,5) H-class conditionality bound
  everything here exactly as they bound the tree.

## Receipts

- Probe: tests/channel-swings/torsor_k_sequence_probe.py -- ALL PASS,
  12 [E] + 1 [F] = 13 (setup [T] = 11 excluded), exit 0, ~140 s.
- HEADLINE: K3 KILLED (Test N, expected; commutant projection exactly 0),
  K4 KILLED (bridge tensor rank 1: the record current is Sp(1)_comm-blind
  by two exact identities -- deck +I, degree 0), K2 KILLED (admissible-C
  set is symmetric-space-sized, commutant orbit is a point, no free
  orbit); k = 64c general-m bookkeeping SUSTAINED. MS NOT established.
- Imported batteries re-run live, all exit 0: phase0_torsor_checks (0.1 s),
  sig_b5_habitat_probe (1.0 s), pt3_w229_membership_probe (3.6 s),
  d1_coperator_build_probe (0.1 s), torsion_arena_probe (73 s),
  verify_torsion_arena_probe (44 s).
