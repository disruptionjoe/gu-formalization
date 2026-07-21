---
title: "Node A -- the trit's symmetry group: S_3, not Z/3 (the three order-3 sectors are interchangeable; the label camp is live, a surviving cyclic clock is dead)"
status: active_research
doc_type: node_result
created: 2026-07-20
directed_by: "Joe direct chat, 2026-07-20 (pre-registered Node A: trit symmetry group)"
axiom: lab/process/boundary-adapter-standing-axiom.md
lane: 1
channel: TRIT-INTERPRETATION
binding: explorations/prereg-trit-symmetry-and-fork-2026-07-20.md (commit cafcbc7)
provenance_grade: node result (executes the bound Node A gate; asserts nothing beyond the cited frozen receipts + the exact group computation)
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# Node A -- the trit's symmetry group (S_3 vs Z/3)

Probe: `tests/channel-swings/trit_symmetry_node_a_probe.py` (deterministic,
exit 0, 3 [T] + 9 [E] + 4 [F] = 16 checks, < 1 s). Binding:
`explorations/prereg-trit-symmetry-and-fork-2026-07-20.md` (cafcbc7), Node A.

## The bound question

Does the trit's natural symmetry close to full **S_3** (all six permutations
of the three order-3 sectors -- the three are INTERCHANGEABLE, the label camp
is live) or only **Z/3** (three rotations, orientation survives, contradicting
triage)? Build from the frozen commutant/sector structure only.

## What the run finds -- OUTCOME A-S3

The group is **S_3 (order 6, nonabelian) = D_3**: the full symmetric group on
the three sectors. All six permutations are realized; A-S3 fires; A-Z3 does not.

### The group computation

The three sectors are the three cube-root eigenspaces / the order-3 class
action -- the N6 weight spaces {-2, 0, +2}, each 64-dimensional, labelled by
the Z/3 characters {1, omega, omega^2}. Two admissible frozen operations
permute them:

- **(R) ROTATION** -- the canonical Z/3, i.e. multiply the characters by omega.
  On the cube-root set this is the **3-cycle (0 1 2)** (order 3, fixed-point-
  free). It is the frozen commutant order-3 element; the planted SU(2)+ 2pi/3
  rotation that realizes the regular representation (`n6_fingerprint_probe.py`)
  is its concrete carrier.
- **(C) CONJUGATION** -- complex conjugation of the characters. On the cube-root
  set this is the **transposition (1 2)** (order 2): it fixes the trivial
  sector 0 and swaps omega <-> omega^2. It is admissible because the two frozen
  N4 characters differ by *exactly* complex conjugation (chi_D(a1) = omega,
  chi_B(a1) = omega^2; `n4_two_z3s_probe.py` admissible set = {Phi_D, Phi_B} =
  Aut(Z/3) = Z/2). The orientation-reversal defect recomputes to < 1e-12
  (triage af7425f cited it at 7e-16).

A 3-cycle together with a transposition generates all of S_3. The probe builds
the closure `<(0 1 2), (1 2)>`, machine-checks the group axioms on the full
multiplication table (closure, identity, inverses, associativity), and finds:

- |G| = 6, and G = the full Sym({0,1,2}) -- every one of the six permutations
  is realized;
- G is **nonabelian**: ROT o CONJ = (1 0 2) != (2 1 0) = CONJ o ROT;
- max element order = 3 (no order-6 element), so G is **not Z/6**;
- the only nonabelian group of order 6 is S_3 -> named exactly **S_3 = D_3**.

An independent route agrees on the nose: modelling the trit as an *unoriented*
3-cycle (undirected-edge / complete-graph invariant) and collecting every
permutation that preserves it yields the identical group, S_3. So the algebraic
route (generate from ROT + CONJ) and the combinatorial route (symmetries of the
unoriented triangle) converge.

### Why S_3 and not Z/3 (the decisive datum)

This is exactly the oriented-vs-unoriented triangle distinction. A **directed**
triangle (arrows 0->1->2->0) has symmetry group Z/3: rotations preserve the
arrows, reflections/conjugation reverse them and are *not* symmetries. An
**undirected** triangle has symmetry group S_3 = D_3. The triage already
established the trit is unoriented -- conjugation is admissible, both orderings
of the N4 character are frozen-equivalent, Olum r^2 = 1 mod 3 is orientation-
blind. An unoriented 3-cycle therefore carries the *full* S_3, and the extra
generator over Z/3 is precisely the frozen conjugation. The single load-bearing
number is the conjugation-admissibility defect (< 1e-12): it is what promotes
Z/3 to S_3.

## Controls (bound; demonstrated power)

- **CONTROL 1 -- planted DIRECTED 3-cycle registers Z/3-only.** Preserving the
  directed edges {(0,1),(1,2),(2,0)} admits exactly {e, (0 1 2), (0 2 1)}:
  order 3, NO transposition, named Z/3. A real chirality survives, exactly as
  it must.
- **CONTROL 2 -- planted IDENTICAL blocks register S_3.** With no distinguishing
  invariant every permutation is a symmetry: full Sym({0,1,2}), order 6, S_3.
- **CONTROL 3 -- the orientation datum is load-bearing (power).** A classifier
  that ignores orientation (always adjoins conjugation) *misregisters* the
  directed plant as S_3 -- the known-wrong answer. The orientation-sensitive
  classifier separates directed (Z/3) from unoriented (S_3). The classifier is
  not broken.
- **CONTROL 4 -- opposite verdicts on the same three sectors.** The identical
  three sectors give Z/3 (oriented) vs S_3 (unoriented); the trit lands on S_3
  solely on the strength of the frozen conjugation defect, not by assumption.

Both bound plants register as pre-declared: the classifier discriminates.

## What it means for the label-vs-clock question

A-S3 firing means the three order-3 sectors are **interchangeable**: no
computable operation distinguishes "sector 1" from "sector 2" as a preferred
successor, because conjugation (which swaps them) is an admissible symmetry.
Concretely:

- **The label camp is live.** Three interchangeable things externally
  distinguished only by a label -- ZK coloring, MMO sharding, degenerate NN
  copies, consensus quorum -- is exactly the S_3 signature. Node B (B1) is the
  right next test: are the three generation-sectors structurally isomorphic
  copies?
- **The cyclic-clock reading is dead as an internal orientation.** A
  three-phase observer clock needs a preferred cycle direction (an oriented
  3-cycle, Z/3-only). S_3 says the orientation is not there. This confirms the
  triage's demotion of candidate 1 (role-rotation) and hardens candidate 3
  (observer clock) as, at best, downstream of uncomputable data and not an
  internal frozen structure.
- It does **not** by itself decide the copies/simplex fork -- that is Node B.
  S_3 is compatible with both the label camp (identical copies) and a
  fully-symmetric 2-simplex (the boundary of a triangle also carries S_3). A-S3
  rules out the *oriented* readings and hands the fork to B1/B2.

## Five-lens council (short, inline; research-only)

- **Standard-field theorist:** textbook and airtight. Three objects, a 3-cycle
  plus one transposition, generate S_3; the only groups of order 6 are Z/6 and
  S_3, and nonabelianness (checked) forces S_3. The conjugation generator is
  the frozen complex conjugation, not an inserted assumption.
- **Program-native (TaF/finality):** endorses reading the result as
  "orientation is absent," not "orientation is hidden." S_3 is the honest
  symmetry of an object with no computable arrow of succession; the clock
  reading is demoted by structure, not by preference.
- **Category theorist:** the automorphism group of the *set* of three sectors
  (with the unoriented cyclic incidence) is S_3; a directed cyclic structure
  would cut it to Z/3 = the rotation subgroup. The decisive invariant is edge
  orientation, and the two controls exhibit both sides. Correctly a symmetry-
  group question, cleanly answered.
- **Skeptic / kill-attorney:** the one place to attack is "is conjugation
  really admissible?" If a preferred orientation existed anywhere in the frozen
  data, A-Z3 would fire. It does not: chi_B == conj(chi_D) exactly and Olum is
  orientation-blind. The directed-plant control proves the classifier *can*
  return Z/3 when orientation is real -- so the S_3 verdict is not a rigged
  ceiling. No kill available; the demotion of the oriented readings stands.
- **Philosopher:** the trit is a THIRD that is a CYCLE with no arrow. S_3 is the
  precise statement of "interchangeable three" -- it says the three sectors have
  no intrinsic identities, only a label imposed from outside. That sharpens the
  open problem to Node B's label-vs-simplex fork and forecloses the internal
  clock.

## Receipts

- `tests/channel-swings/trit_symmetry_node_a_probe.py` -- exit 0; 3 [T] + 9 [E]
  + 4 [F] = 16 all pass; < 1 s. HEADLINE names the group (S_3 = D_3) and the
  fired outcome (A-S3). Group table, both controls, and the load-bearing
  conjugation defect are all in the run.
- Frozen inputs cited/recomputed: the three cube-root sectors and the canonical
  Z/3 rotation (`n6_fingerprint_probe.py`: commutant order-3 = {omega I,
  omega^2 I}, planted SU(2)+ rotation realizes the regular rep); the admissible
  freedom = Aut(Z/3) = Z/2 (`n4_two_z3s_probe.py`: admissible set {Phi_D,
  Phi_B}, differ by inversion); the unoriented finding (triage af7425f, defect
  7e-16, recomputed here < 1e-12).

## Boundary

Executes the bound Node A gate only. Asserts nothing beyond the cited frozen
receipts and the exact group computation. No claim/canon/posture movement. The
copies/simplex fork (Node B) is untouched here and runs regardless. A-S3 is a
symmetry-group verdict: it establishes interchangeability (label camp live,
oriented-clock dead), not which structural home (copies vs simplex) is right.
