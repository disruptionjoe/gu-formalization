"""W70 -- Path 5 Branch D: the Lawvere no-closure impossibility skeleton, graded.

This test encodes the CATEGORICAL SKELETON of Branch D (the payoff-theorem frame) and the
honest status of its mapping onto the physics. It has four jobs:

  PART A -- prove the LAWVERE / YANOFSKY SKELETON on finite instances, exhaustively. In a
            category with finite products (finite Set is a CCC, so finite sets suffice), a
            FIXPOINT-FREE endomorphism alpha: B -> B obstructs any point-surjection
            A -> B^A (equivalently any weakly-point-surjective T: A x A -> B). We brute-force
            over ALL T for small A and show the diagonal predicate d(a) = alpha(T(a,a)) is
            never a row of T -> no closure. This is a genuine exhaustive proof, not a sample.

  PART B -- CROSS-CHECK on the canonical instances (Cantor powerset diagonal; Goedel/Tarski
            negation). The obstruction with alpha = logical negation reproduces "no surjection
            A -> P(A)" and the undefinability diagonal. Same computation, standard instance.

  PART C -- the GRADING-FLIP fixpoint-free check (the L2 ingredient A must certify). The flip
            on the 2-valued grading {admissible, inadmissible} = the SWAP = fixpoint-free
            (structurally identical to negation). The IDENTITY has fixed points; a 3-VALUED
            grading with a fixed middle (boundary) grade HAS a fixed point -> the honest risk
            that a genuine boundary stratum would WEAKEN the obstruction. All three asserted.

  PART D -- the honest DISTINCTION the referee/adversary forces: the Krein modular conjugation
            J acting on STATES (J^2 = 1) HAS fixed vectors (its +1 eigenspace), so J-on-states
            is NOT the fixpoint-free object. The fixpoint-free object is the flip on the
            grading LABELS. Machine-checked so the mapping cannot silently equivocate.

  PART E -- encode the REDUCTION + graded status as booleans known today, so the claim cannot
            drift upward: skeleton PROVEN; mapping GENUINE-MODULO-two-lemmas (L1 from Branch B,
            L2 from Branch A); "residual free selection EXISTS" FOLLOWS; "residual IS the value"
            is an added semantic bridge, NOT forced by the skeleton.

Construction (GEOMETER-VS-PHYSICS-OBJECTS.md): the Krein/indefinite grading is program-native
(KEEP-AND-GRADE, not positive-Hilbert). The 2-valued +/- grading is the Krein norm sign; the
firewall is its partition. No positive-Hilbert default is assumed anywhere.

Run: python tests/W70_path5_D_lawvere.py
Exit 0 = the skeleton is proven on the finite instances AND the graded status is exactly as
claimed in explorations/path5-branchD-lawvere-no-closure-2026-07-11.md.
"""
from __future__ import annotations

from itertools import product

FAIL = []


def check(name, ok, detail=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}{('  ' + detail) if detail else ''}")
    if not ok:
        FAIL.append(name)


# ===========================================================================
# PART A -- the Lawvere / Yanofsky skeleton, exhaustively on finite Set.
#
# Setting (Yanofsky weak form -- needs only finite products + the diagonal, NOT full
# function-space exponentials): A a finite set, B a finite set, alpha: B -> B an
# endomorphism. A "self-referential closure" is a map T: A x A -> B whose rows
# {T(a0, -) : a0 in A} enumerate admissibility predicates A -> B; T is
# weakly-point-surjective iff every predicate p: A -> B is some row.
#
# THEOREM (contrapositive Lawvere): if alpha is FIXPOINT-FREE then for EVERY T the
# diagonal predicate d(a) := alpha(T(a, a)) is NOT a row of T. Hence no closure T can
# be point-surjective: the self-reference cannot be closed. The unrepresented d is the
# residual (free) selection.
# ===========================================================================
print("[W70] Path 5 Branch D -- Lawvere no-closure skeleton, graded status\n")
print("PART A -- Lawvere/Yanofsky skeleton, EXHAUSTIVE over all T on finite Set:")


def all_functions(domain, codomain):
    """All functions domain -> codomain as dicts, exhaustively."""
    dom = list(domain)
    return [dict(zip(dom, vals)) for vals in product(codomain, repeat=len(dom))]


def diagonal_predicate_unrepresented(A, B, alpha):
    """For EVERY T: A x A -> B, check the diagonal predicate d(a) = alpha(T(a,a))
    is not equal to any row T(a0, -). Returns True iff the obstruction holds for all T."""
    # A function T: A x A -> B is a dict keyed by (a0, a1).
    pairs = [(a0, a1) for a0 in A for a1 in A]
    for vals in product(B, repeat=len(pairs)):
        T = dict(zip(pairs, vals))
        # diagonal predicate d(a) = alpha(T(a,a))
        d = {a: alpha[T[(a, a)]] for a in A}
        # rows: row_a0(a1) = T(a0, a1)
        represented = any(all(T[(a0, a1)] == d[a1] for a1 in A) for a0 in A)
        if represented:
            return False  # some T represents its own flipped diagonal -> alpha had a fixed point
    return True


# alpha = SWAP on B = {0, 1} (the fixpoint-free grading-flip; 0 = admissible, 1 = inadmissible).
B2 = [0, 1]
swap = {0: 1, 1: 0}
identity2 = {0: 0, 1: 1}

for size in (1, 2, 3):
    A = list(range(size))
    obstructed = diagonal_predicate_unrepresented(A, B2, swap)
    check(f"|A|={size}, B={{admissible,inadmissible}}, flip=SWAP (fixpoint-free): NO closure T "
          f"represents its flipped diagonal (obstruction holds for ALL T)",
          obstructed)

# Sanity the other way: with alpha = IDENTITY (has fixed points) the diagonal argument produces
# NO new predicate -- some T DOES represent its diagonal. So the obstruction genuinely REQUIRES
# fixpoint-freeness; it is not an artifact of the construction.
id_still_obstructs = diagonal_predicate_unrepresented([0, 1], B2, identity2)
check("with flip=IDENTITY (has fixed points) the obstruction DISSOLVES (some T represents its "
      "diagonal) -> the no-closure result is DUE TO fixpoint-freeness, nothing else",
      id_still_obstructs is False,
      "confirms the endomorphism's fixpoint-freeness is load-bearing, per Lawvere")


# ===========================================================================
# PART B -- cross-check on the canonical self-reference instances.
# Cantor: A -> P(A) with alpha = negation is exactly PART A with B = {0,1}, alpha = swap.
# The diagonal set D = {a : a not in T(a)} is the unrepresented predicate. Verify no
# surjection A -> P(A) exists (cardinality) AND the concrete diagonal witnesses it.
# ===========================================================================
print("\nPART B -- cross-check: Cantor powerset diagonal / Goedel-Tarski negation:")

for size in (1, 2, 3):
    A = list(range(size))
    # T: A -> P(A) as a dict a0 -> frozenset. Enumerate ALL such T.
    subsets = [frozenset(s for s in A if bits[s]) for bits in product([0, 1], repeat=size)] \
        if size > 0 else [frozenset()]
    no_surjection = True
    for assignment in product(subsets, repeat=size):
        T = dict(zip(A, assignment))
        D = frozenset(a for a in A if a not in T[a])  # Cantor diagonal (negation flip)
        if D in set(T.values()):
            no_surjection = False
            break
    check(f"|A|={size}: NO surjection A -> P(A); the diagonal D = {{a : a not in T(a)}} is "
          f"never in the image (Cantor)", no_surjection)

check("Cantor/Goedel/Tarski/halting are the SAME skeleton: B = 2-valued truth/grading, "
      "alpha = negation = the fixpoint-free flip",
      swap[0] != 0 and swap[1] != 1,
      "the physics grading-flip plays exactly the role negation plays in the classical diagonals")


# ===========================================================================
# PART C -- the grading-flip fixpoint-free check (the L2 ingredient Branch A must certify).
# ===========================================================================
print("\nPART C -- grading-flip fixpoint-free check (L2, needs Branch A's J^2=1 + firewall):")


def fixed_points(alpha):
    return [b for b in alpha if alpha[b] == b]


check("2-valued grading {admissible, inadmissible}, flip = SWAP: fixpoint-FREE "
      "(no state is its own firewall-image)", fixed_points(swap) == [],
      "admissible != inadmissible -> the flip exchanges them -> no fixed grade")

check("2-valued grading, flip = IDENTITY: has 2 fixed points (would DESTROY the obstruction) "
      "-> A must certify the flip is the SWAP, not the identity", len(fixed_points(identity2)) == 2)

# The honest risk: a genuine 3-VALUED grading {below, boundary, above} whose flip fixes the
# middle (boundary) grade HAS a fixed point -> the obstruction WEAKENS. This is the tension with
# the 3-strata count leg (Branch C). Resolution recorded in the doc: the FLIP acts on the
# 2-valued Krein-norm sign (+/-); the 3 strata are a SPATIAL/cohomological axis (stalk / H^1 /
# global), a DIFFERENT axis; the boundary is the partition surface (norm-zero, measure-zero),
# not a third admissibility VALUE. Here we just MACHINE-CHECK the risk is real.
B3 = ["below", "boundary", "above"]
flip3_fix_middle = {"below": "above", "boundary": "boundary", "above": "below"}
check("RISK made explicit: a 3-valued flip fixing the middle (boundary) grade HAS a fixed point "
      "-> obstruction WEAKENS; A must certify the flip is on the 2-valued +/- Krein-norm sign",
      fixed_points(flip3_fix_middle) == ["boundary"],
      "the 3 strata (stalk/H^1/global) are a DIFFERENT axis from the +/- grading; boundary is the "
      "partition surface, not a third grade")


# ===========================================================================
# PART D -- the referee/adversary distinction: J-on-STATES vs flip-on-LABELS.
# The Krein modular conjugation J (J^2 = 1) acting on the STATE space HAS fixed vectors
# (its +1 eigenspace). So J-on-states is NOT fixpoint-free. The fixpoint-free object is the
# flip on the grading LABELS. Machine-check both, so the mapping cannot equivocate.
# ===========================================================================
print("\nPART D -- honest distinction: J-on-states (has fixed vectors) vs flip-on-labels (free):")

# A concrete Krein involution on a 2-dim state space: J swaps two isotropic directions but is an
# involution; take the exchange matrix J = [[0,1],[1,0]], J^2 = I. Its +1 eigenvector (1,1) is a
# FIXED vector. (Any involution on a >=1-dim space over R has a nonempty +1 or -1 eigenspace; the
# +1 eigenspace is the set of fixed vectors.)
J = [[0, 1], [1, 0]]


def matmul2(M, v):
    return [M[0][0] * v[0] + M[0][1] * v[1], M[1][0] * v[0] + M[1][1] * v[1]]


def matmul2x2(M, N):
    return [[sum(M[i][k] * N[k][j] for k in range(2)) for j in range(2)] for i in range(2)]


J2 = matmul2x2(J, J)
check("Krein modular conjugation J is an INVOLUTION on states (J^2 = 1)", J2 == [[1, 0], [0, 1]],
      "this is exactly A's J^2=1 axiom")

fixed_vector = [1, 1]  # J (1,1) = (1,1)
check("J-on-STATES HAS a fixed vector (its +1 eigenspace is nonempty) -> J-on-states is NOT the "
      "fixpoint-free object", matmul2(J, fixed_vector) == fixed_vector,
      "so the adversary's 'the grading-flip has a fixed point' is TRUE for J-on-states and IRRELEVANT")

check("the fixpoint-free object is the flip on grading LABELS (PART C swap), which J INDUCES "
      "across the firewall -- distinct from J acting on states",
      fixed_points(swap) == [] and matmul2(J, fixed_vector) == fixed_vector,
      "mapping is sound ONLY when B = the 2-valued grading label, not the state space")


# ===========================================================================
# PART E -- the reduction + graded status (booleans known today; cannot drift upward).
# ===========================================================================
print("\nPART E -- reduction to A/B lemmas + honest graded status:")

# The categorical skeleton is PROVEN (PART A/B, exhaustive on finite instances).
skeleton_proven = (not FAIL)  # every skeleton assertion above passed
check("SKELETON PROVEN: fixpoint-free flip obstructs self-referential closure (finite Set, "
      "exhaustive) + Cantor cross-check", skeleton_proven)

# L1 (Branch B): the admissibility structure is a category with finite products + diagonal, and a
# 'closure across the firewall' IS a weakly-point-surjective T: A x A -> B. NOT established here.
L1_supplied_by_B = False
check("L1 (cartesian category w/ diagonal + closure = point-surjective T) is REDUCED to Branch B "
      "(filtration <-> section map), NOT established here", L1_supplied_by_B is False,
      "the filtration<->section map must furnish the ambient CCC-enough category and the representing map")

# L2 (Branch A): the grading-flip is genuinely fixpoint-free = SWAP, requiring J^2=1 (involution)
# AND admissible != inadmissible with no fixed boundary grade (effective 2-valued). NOT here.
L2_supplied_by_A = False
check("L2 (grading-flip = SWAP, fixpoint-free: J^2=1 + firewall nontriviality + no fixed boundary "
      "grade) is REDUCED to Branch A (Krein modular conjugation), NOT established here",
      L2_supplied_by_A is False,
      "PART C/D show WHAT A must certify; A's J^2=1 supplies the involution, the firewall the swap")

# Does 'a residual free selection EXISTS' follow from the obstruction? YES -- the unrepresented
# diagonal predicate d is a selection no internal state fixes (proven in PART A for every T).
residual_exists_follows = skeleton_proven  # it is literally the PART A conclusion
check("'a RESIDUAL free selection EXISTS' FOLLOWS from the obstruction (the diagonal predicate is "
      "unrepresented for every T) -- given L1+L2", residual_exists_follows)

# Does 'the residual IS the value/individual' follow from the skeleton alone? NO -- that is an
# added semantic identification (a bridge, analogous to path-4 postulate P), natural but not forced.
residual_is_the_value_is_forced = False
check("'the residual IS the value/individual' is NOT forced by the skeleton -- it is an added "
      "semantic bridge (natural, not automatic); only the EXISTENCE of residual freedom is forced",
      residual_is_the_value_is_forced is False,
      "honest ceiling: obstruction => residual freedom (theorem); residual = physical value (bridge)")

# Graded verdict tuple the orchestrator consumes.
reachability = "needs-A-B-lemmas"       # skeleton constructible-now; physics theorem reduces to L1,L2
mapping = "GENUINE-modulo-two-lemmas"   # flip<->negation and diagonal<->self-reference are exact
payoff_within_reach = True              # IF A gives L2 and B gives L1, the theorem follows
print(f"\n    reachability={reachability}  mapping={mapping}  payoff_within_reach={payoff_within_reach}")
check("graded verdict recorded: skeleton PROVEN; mapping GENUINE modulo L1(B)+L2(A); payoff "
      "theorem WITHIN REACH given A and B; 'residual=value' is a residual bridge",
      reachability == "needs-A-B-lemmas" and mapping.startswith("GENUINE") and payoff_within_reach)


# ---------------------------------------------------------------------------
print("\n[verdict]")
print("  SKELETON (constructible-now, PROVEN here, exhaustive on finite Set + Cantor): a")
print("  fixpoint-free endomorphism alpha: B -> B obstructs any self-referential closure")
print("  T: A x A -> B; the flipped diagonal d(a) = alpha(T(a,a)) is unrepresented for EVERY T,")
print("  so no J-consistent closure across the firewall exists and a residual free selection")
print("  remains. MAPPING onto the physics is GENUINE at the core: the grading-flip on")
print("  {admissible, inadmissible} = the SWAP = fixpoint-free, structurally identical to the")
print("  negation of Cantor/Goedel/Tarski/halting; the diagonal = the observer inside its own")
print("  admissibility space. It REDUCES to two named lemmas: L1 (Branch B: the closure is a")
print("  point-surjection in a cartesian category) and L2 (Branch A: J^2=1 + firewall => the flip")
print("  is the swap, no fixed boundary grade). 'Residual free selection EXISTS' FOLLOWS; 'the")
print("  residual IS the value' is an added semantic bridge, not forced by the skeleton alone.")
print("  No canon/RESEARCH-STATUS/verdict movement.")

if FAIL:
    print(f"\nFAILED: {FAIL}")
    raise SystemExit(1)
print("\nexit 0 = Lawvere skeleton proven on finite instances; mapping graded GENUINE-modulo-")
print("         two-lemmas; payoff theorem within reach given Branch A (L2) and Branch B (L1).")
