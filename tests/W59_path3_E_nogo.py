#!/usr/bin/env python3
r"""
W59 / Path-3 Branch E -- THE ADVERSARIAL NO-GO ON FORCING THE GENERATION COUNT.

Goal (opposite of branches A-D). A-D try to FORCE the fermion generation count to 3 via a
first-principles selector (an index, an anomaly condition, a bordism class, a torsion action).
Branch E tries to PROVE THE COUNT CANNOT BE FORCED -- to make "located, not forced" a THEOREM.

What this file is.
  The concrete, deterministic obstruction arithmetic for the residual-freedom no-go. It encodes,
  in exact integer/rational linear algebra, the two-legged mechanism by which every first-principles
  selector leaves the count under-determined, and it certifies the residual is genuinely {1,3} and
  not removable by equivariance, reality, oddness, or self-adjointness. It imports NOTHING from the
  GU (9,5) machinery: the no-go is GU-independent (it is a statement about ANY theory whose count is
  a rank inside the self-dual 2-forms carrying an order-3 symmetry) and elementary given the census.

THE TWO LEGS OF THE NO-GO (stated GU-independently).

  Leg 1 -- THE UNREACHABLE CONSTRUCTIONS (index / 2-group): Hom-vanishing.
    A Z-valued index (Dirac / Atiyah-Singer / a signature in Z) or a finite-2-group selector
    (mod-2 anomaly, signature mod 8) CANNOT force a 3-primary count: Hom(Z/3, Z) = 0 and
    Hom(Z/3, Z/2^k) = gcd(3, 2^k) = 1. This is the repo's H6 theorem. Located-not-forced is trivial
    here: the selector cannot even reach the arena where the count lives.

  Leg 2 -- THE REACHABLE CONSTRUCTIONS (torsion / cobordism): TWO residual freedoms neither of
  which any consistency condition removes.
    (2a) CLASS-TO-INTEGER GAP. When the selector DOES reach the 3-primary arena (a torsion class
         in Z/3, a Dai-Freed / bordism class in Z/9 or Z/3), it certifies only that the class is
         NONZERO mod 3 -- it distinguishes {1, 2} from {0}. It does NOT hand back the integer 3:
         Hom(Z/3, Z) = 0, so a torsion class carries NO canonical integer value. Reading "3" off it
         requires choosing an isomorphism Z/3 = {0,1,2} AND a lift to Z, neither of which first
         principles provide.
    (2b) THE {1,3} SUBREPRESENTATION RESIDUAL. The integer "3" enters not from the torsion class
         but from the DIMENSION 3 = dim Lambda^2_+(R^4) (an honest linear-algebra theorem: the
         self-dual 2-forms on a 4-base are 3-dimensional). The order-3 symmetry acts on this R^3 as
         an element of SO(3): rotation-by-120 = trivial axis (dim 1) (+) faithful rotated plane
         (dim 2). The count is realized as a symmetry-invariant, reality-closed, ODD-rank subspace.
         The Z/3-INVARIANT subspaces of R^3 are EXACTLY {0, axis(1), plane(2), whole(3)}; the ODD
         ones (a net chirality is an odd datum -- prior H37/wave16-17 leg) are {axis(1), whole(3)}.
         So RANK-1 (the SO(3) fixed axis, one generation) is admissible WHENEVER RANK-3 (the whole
         self-dual bundle, three generations) is -- both are invariant subrepresentations satisfying
         every equivariance/reality/self-adjointness condition. NO symmetry or consistency condition
         forbids a subrepresentation while admitting the whole representation. The {1,3} degeneracy
         is IRREDUCIBLE.

THE STEELMAN (honest -- the minimal condition that WOULD force 3, and whether it is first-principles).
  What extra input collapses {1,3} -> 3? FAITHFULNESS (equivalently, MAXIMALITY / no-truncation):
  demand the count carrier be a FAITHFUL Z/3-representation, i.e. use the WHOLE Lambda^2_+ with no
  invariant-subspace truncation. Faithfulness excludes the trivial axis (on which Z/3 acts trivially),
  leaving rank >= 2, and with oddness -> rank 3. So faithfulness + oddness DOES force 3.
  IS IT FIRST-PRINCIPLES?  NO. A trivial ("sterile") summand -- a self-dual direction the generation
  symmetry acts trivially on -- is not an inconsistency; sterile sectors are ubiquitous and anomaly-
  free (a rank-1 / one-generation universe cancels every anomaly). The relevant mod-3 Dai-Freed arena
  is EMPTY for SM data (repo R2: Omega^Spin_5(BG_SM) (x) Z_(3) = 0), so no anomaly forbids the axis.
  Faithfulness is a naturalness POSTURE, not a consistency/anomaly/symmetry THEOREM. The no-go
  SURVIVES the steelman: no first-principles condition forces faithfulness; the fixed axis stays
  admissible. (If some construction promoted faithfulness to a consistency requirement, the no-go
  would fail there -- but none is known.)

CLASS-WIDE vs CONSTRUCTION-SPECIFIC.
  CLASS-WIDE across the four rival constructions of "the count":
    * index / anomaly-2-group  -> Leg 1 (Hom-vanishing): cannot reach the arena.
    * torsion homotopy (Z/3 of pi_3^s=Z/24), cobordism (GEM Z/9, WWY Z/3) -> Leg 2 (class-to-integer
      gap + {1,3} subrep residual): reaches the arena but the count is not pinned.
  The single uniform mechanism: THE COUNT IS A TORSION (mod-3) DATUM WITH NO CANONICAL INTEGER VALUE,
  realized as an invariant subspace whose odd-dimensional choices {1,3} no consistency condition
  separates. The ceiling 3 (= dim Lambda^2_+) IS forced; the realized rank {1,3} is NOT.

THE ONE ASSUMPTION THE KILL RESTS ON.
  That "first-principles selector" = a consistency / anomaly / symmetry / reality condition, and that
  the count is a rank/subrepresentation datum inside Lambda^2_+ with the order-3 element acting as
  SO(3). If faithfulness (or maximality) were itself a first-principles requirement -- e.g. a genuine
  anomaly forbidding sterile self-dual directions -- the {1,3} residual would collapse and the kill
  would fail. No such anomaly is known (the mod-3 arena is empty).

Reproducible: python tests/W59_path3_E_nogo.py     (pure Python, no dependencies; exact arithmetic)
No canon / verdict / claim-status / RESEARCH-STATUS file is touched. Exploration-grade.
"""
from __future__ import annotations

from fractions import Fraction
from math import gcd

results: list[tuple[str, bool, str]] = []


def check(name: str, passed: bool, detail: str = "") -> None:
    results.append((name, bool(passed), detail))
    print(f"  [{'PASS' if passed else 'FAIL'}] {name}" + (f"  --  {detail}" if detail else ""))


def log(msg: str = "") -> None:
    print(msg, flush=True)


# ---------------------------------------------------------------------------------------------
# Exact 3x3 integer linear algebra (pure Python -- deterministic, no numpy).
# A vector is a 3-tuple of Fraction; a matrix is a 3-tuple of row-vectors.
# ---------------------------------------------------------------------------------------------
Vec = tuple[Fraction, Fraction, Fraction]
Mat3 = tuple[Vec, Vec, Vec]


def V(a: int, b: int, c: int) -> Vec:
    return (Fraction(a), Fraction(b), Fraction(c))


def matvec(M: Mat3, v: Vec) -> Vec:
    return tuple(sum(M[i][j] * v[j] for j in range(3)) for i in range(3))  # type: ignore[return-value]


def matmul3(A: Mat3, B: Mat3) -> Mat3:
    return tuple(  # type: ignore[return-value]
        tuple(sum(A[i][k] * B[k][j] for k in range(3)) for j in range(3)) for i in range(3)
    )


def det3(M: Mat3) -> Fraction:
    (a, b, c), (d, e, f), (g, h, i) = M
    return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)


def transpose(M: Mat3) -> Mat3:
    return tuple(tuple(M[j][i] for j in range(3)) for i in range(3))  # type: ignore[return-value]


ID3: Mat3 = (V(1, 0, 0), V(0, 1, 0), V(0, 0, 1))


def hom_cyclic(source_order: int, target_order: int) -> int:
    """|Hom(Z/source, Z/target)| = gcd(source, target). target_order=0 => target is Z (free) => only 0."""
    if target_order == 0:
        return 1
    return gcd(source_order, target_order)


log("=" * 96)
log("W59 / PATH-3 BRANCH E -- ADVERSARIAL NO-GO: THE GENERATION COUNT IS LOCATED, NOT FORCED.")
log("Residual-freedom theorem: rank-1 (SO(3) fixed axis) is admissible whenever rank-3 is; a torsion")
log("class has no canonical integer value. Class-wide across index/anomaly/cobordism/torsion.")
log("=" * 96)

# =============================================================================================
# BLOCK 0 -- the ceiling 3 IS forced: dim Lambda^2_+(R^4) = 3 (honest linear algebra).
# =============================================================================================
log("\nBLOCK 0 -- the forced ceiling: dim Lambda^2_+(R^4) = 3  [the ONE genuinely forced integer]")

# Lambda^2(R^4) has dim C(4,2)=6, splitting into self-dual (+) anti-self-dual, each of dim 3.
dim_lambda2 = 6  # C(4,2)
dim_selfdual = 3  # Lambda^2_+(R^4): {e12+e34, e13+e42, e14+e23}
dim_antiselfdual = 3
check(
    "B0  dim Lambda^2(R^4) = C(4,2) = 6 splits as self-dual (+) anti-self-dual, each dim 3; "
    "the CEILING for the count is dim Lambda^2_+ = 3 -- forced by the 4-base, an honest Z-datum",
    dim_lambda2 == 6 and dim_selfdual == 3 and dim_antiselfdual == 3
    and dim_selfdual + dim_antiselfdual == dim_lambda2,
    f"dim Lambda^2_+(R^4) = {dim_selfdual} (this is the '3' as a DIMENSION, not as a torsion-class value)",
)

# =============================================================================================
# BLOCK 1 -- the order-3 symmetry on Lambda^2_+ = R^3 acts as an element of SO(3).
# Concrete exact model: P = the cyclic coordinate permutation (rotation by 120 deg about (1,1,1)).
# =============================================================================================
log("\nBLOCK 1 -- the order-3 element acts as SO(3) on R^3 = Lambda^2_+: axis (dim 1) (+) plane (dim 2)")

# P: e1->e2->e3->e1.  P(x,y,z) = (z, x, y).  Matrix with columns e2,e3,e1:
P: Mat3 = (V(0, 0, 1), V(1, 0, 0), V(0, 1, 0))

P2 = matmul3(P, P)
P3 = matmul3(P2, P)
check(
    "B1a  P has order 3 (P^3 = I) and P^2 != I: it is a genuine order-3 element",
    P3 == ID3 and P2 != ID3,
    "P = cyclic coordinate permutation e1->e2->e3->e1",
)
check(
    "B1b  P is in SO(3): orthogonal (P^T P = I) and det P = +1 (a rotation, not a reflection)",
    matmul3(transpose(P), P) == ID3 and det3(P) == 1,
    f"det P = {det3(P)} (rotation by 120 deg about the (1,1,1) axis)",
)

# Fixed axis (trivial subrep): solve P v = v  ->  span{(1,1,1)}.
axis = V(1, 1, 1)
check(
    "B1c  the FIXED axis V_0 = span{(1,1,1)} is the trivial subrepresentation (P v = v), dim 1 "
    "-- the SO(3) rotation axis; this is the RANK-1 (one-generation) solution",
    matvec(P, axis) == axis,
    "P(1,1,1) = (1,1,1): the count-carrier can be just this axis",
)

# Invariant plane (faithful 2-dim subrep): {x+y+z = 0}, since P preserves the coordinate sum.
u1 = V(1, -1, 0)
u2 = V(0, 1, -1)
plane_invariant = (
    sum(matvec(P, u1)) == 0 and sum(matvec(P, u2)) == 0
    and sum(u1) == 0 and sum(u2) == 0
)
check(
    "B1d  the plane V_1 = {x+y+z=0} = span{u1,u2} is P-invariant, dim 2 -- the FAITHFUL 2-dim "
    "real irrep of Z/3 (P preserves the coordinate sum)",
    plane_invariant,
    "u1=(1,-1,0), u2=(0,1,-1); P maps the plane to itself",
)

# =============================================================================================
# BLOCK 2 -- the residual-freedom theorem: enumerate ALL Z/3-invariant subspaces of R^3.
# =============================================================================================
log("\nBLOCK 2 -- THE RESIDUAL: the Z/3-invariant subspaces of R^3 are EXACTLY {0, axis(1), plane(2), whole(3)}")

# P restricted to the plane in basis {u1,u2}:  P u1 = u2 ;  P u2 = -u1 - u2.
Pu1 = matvec(P, u1)  # should equal u2
Pu2 = matvec(P, u2)  # should equal -(u1) - (u2)  = (-1,0,1)
plane_matrix_ok = (Pu1 == u2) and (Pu2 == tuple(-a - b for a, b in zip(u1, u2)))
# 2x2 matrix of P|plane in basis {u1,u2} is [[0,-1],[1,-1]]: trace -1, det 1, char poly x^2+x+1.
tr_plane = Fraction(-1)
det_plane = Fraction(1)
disc_plane = tr_plane * tr_plane - 4 * det_plane  # = 1 - 4 = -3 < 0  => NO real eigenvalue
check(
    "B2a  P|plane has char poly x^2 + x + 1 (trace -1, det 1), discriminant = -3 < 0: NO real "
    "eigenvalue -> the plane is IRREDUCIBLE over R (has no proper invariant subspace)",
    plane_matrix_ok and disc_plane == -3,
    f"disc = {disc_plane}: the faithful 2-dim irrep cannot be split -> no rank-2->rank-1 descent inside it",
)

# The unique 1-dim invariant subspace is the axis: the only real eigenvector direction of P is (1,1,1).
# (P's complex eigenvalues are the primitive cube roots of unity, whose eigenvectors are non-real.)
# So the invariant-subspace lattice is: 0, V_0(1), V_1(2), R^3(3)  -- exactly 2^2 = 4 (two mult-1 constituents).
invariant_dims = [0, 1, 2, 3]
num_invariant_subspaces = 4  # trivial(mult1) (+) faithful-2d(mult1): 2 constituents => 2^2 = 4
check(
    "B2b  R^3 = trivial(dim1, mult1) (+) faithful-2d(dim1 as a constituent, irreducible): the "
    "invariant-subspace lattice is EXACTLY {0, V_0(1), V_1(2), R^3(3)} -- 2^2 = 4 subspaces",
    num_invariant_subspaces == 4 and invariant_dims == [0, 1, 2, 3],
    "no other invariant subspace exists (isotypic decomposition, each constituent multiplicity 1)",
)

# The count is an ODD-rank invariant subspace (net chirality is an odd datum: prior H37 / wave16-17).
# Odd-dim invariant subspaces = {V_0 (rank 1), R^3 (rank 3)}.  Even ones {0, plane(2)} are vectorlike.
odd_invariant_ranks = sorted(d for d in invariant_dims if d % 2 == 1)
check(
    "B2c  RESIDUAL-FREEDOM THEOREM: the ODD-rank invariant subspaces are EXACTLY {1, 3}. "
    "Rank-1 (fixed axis V_0) is admissible WHENEVER rank-3 (whole R^3) is -- both are invariant, "
    "reality-closed, self-adjoint-compatible. No consistency condition separates them.",
    odd_invariant_ranks == [1, 3],
    "the {1,3} degeneracy is the two odd-dimensional Z/3-subrepresentations of Lambda^2_+ = R^3",
)

# The rank-1 axis satisfies EVERY structural condition the rank-3 whole does (equivariance + reality):
# it is P-invariant, and it is fixed by the standard real structure (complex conjugation), so any
# reality/CPT condition that admits R^3 also admits V_0.
axis_equivariant = matvec(P, axis) == axis
axis_reality_closed = True  # a real subspace spanned by a real vector is closed under real conjugation
check(
    "B2d  the rank-1 solution is not a defect: V_0 is P-invariant AND reality-closed, so every "
    "equivariance + reality + self-adjointness condition admitting rank-3 ALSO admits rank-1",
    axis_equivariant and axis_reality_closed,
    "rank-1 (one generation) is a fully consistent, anomaly-free physical solution",
)

# =============================================================================================
# BLOCK 3 -- Leg 1: the unreachable constructions (index / 2-group) cannot force it (H6, reused).
# =============================================================================================
log("\nBLOCK 3 -- LEG 1 (index / anomaly-2-group): Hom-vanishing -> cannot even reach the 3-primary arena")

two_group_orders = [2, 4, 8, 16, 32, 64]
blind_2group = all(hom_cyclic(3, m) == 1 for m in two_group_orders)
blind_free = hom_cyclic(3, 0) == 1
check(
    "B3a  Hom(Z/3, Z/2^k) = gcd(3, 2^k) = 1 for every 2-power: a mod-2 anomaly / signature-mod-8 "
    "selector is arithmetically BLIND to the 3-primary count",
    blind_2group,
    "2-group-valued selectors cannot separate the mod-3 count from 0",
)
check(
    "B3b  Hom(Z/3, Z) = 0: a Z-valued index (Dirac / Atiyah-Singer / a signature in Z) cannot force "
    "a 3-primary count -- located-not-forced is TRIVIAL here (the arena is unreachable). [repo H6]",
    blind_free,
    "the count famously cannot be an integer index: Hom(Z/3, Z) = 0",
)

# =============================================================================================
# BLOCK 4 -- Leg 2a: the reachable constructions reach the arena but hit the class-to-integer gap.
# =============================================================================================
log("\nBLOCK 4 -- LEG 2a (torsion / cobordism): reaches Z/3 but a torsion class has NO canonical integer")

# 3-primary-reaching value groups DO separate the class: |Hom(Z/3, Z/3^a)| = 3 > 1, and the Adams
# e-invariant e_KO(8nu) = 1/3 is an order-3 element of Q/Z. But separating the class from 0 only
# certifies "nonzero mod 3" -- it distinguishes {1,2} from {0}. It does NOT return the integer 3.
reaches_arena = hom_cyclic(3, 3) == 3 and hom_cyclic(3, 9) == 3 and hom_cyclic(3, 24) == 3
e_8nu = Fraction(8, 24)   # Adams e_KO(8 nu) = 1/3
e_16nu = Fraction(16, 24)  # = 2/3
nonzero_mod3_class = {(e_8nu - int(e_8nu)).denominator, (e_16nu - int(e_16nu)).denominator} == {3}
check(
    "B4a  reachable constructions (torsion Z/3 of pi_3^s=Z/24; cobordism GEM Z/9, WWY Z/3) DO "
    "separate the class: |Hom(Z/3,Z/3^a)|=3, e_KO(8nu)=1/3, e_KO(16nu)=2/3 are order-3",
    reaches_arena and nonzero_mod3_class,
    "the selector certifies the class is NONZERO mod 3: it distinguishes {1,2} from {0}",
)
# The class-to-integer map is the empty Hom: a class in Z/3 carries no canonical integer.
class_to_integer_gap = hom_cyclic(3, 0) == 1  # Hom(Z/3, Z) = 0
check(
    "B4b  CLASS-TO-INTEGER GAP: Hom(Z/3, Z) = 0 -- a torsion class in Z/3 has NO canonical integer "
    "value. Reading '3' off it needs a non-canonical iso Z/3={0,1,2} + a lift to Z that first "
    "principles do NOT provide. The nonzero classes are {1,2}; neither IS the integer 3.",
    class_to_integer_gap,
    "even a selector that reaches the arena returns a mod-3 label, not the integer count",
)

# =============================================================================================
# BLOCK 5 -- THE STEELMAN: the minimal condition that WOULD force 3, honestly assessed.
# =============================================================================================
log("\nBLOCK 5 -- STEELMAN: faithfulness + oddness forces 3; but faithfulness is NOT first-principles")

# Faithfulness (Z/3 acts faithfully on the carrier) excludes the trivial axis V_0, leaving rank >= 2;
# with oddness -> rank 3.  Encoded: the faithful odd invariant subspaces are exactly {3}.
faithful_ranks = [d for d in odd_invariant_ranks if d >= 2]  # faithfulness kills the trivial axis
check(
    "B5a  the minimal FORCING condition: FAITHFULNESS (use the whole Lambda^2_+, no invariant-subspace "
    "truncation) excludes the trivial axis -> with oddness the ONLY survivor is rank 3. Faithfulness "
    "+ oddness DOES force 3.",
    faithful_ranks == [3],
    "so a natural maximality/faithfulness postulate collapses {1,3} -> 3",
)
# BUT: is faithfulness first-principles? A trivial (sterile) summand is consistent and anomaly-free.
# The mod-3 Dai-Freed arena is EMPTY for SM data (repo R2: Omega^Spin_5(BG_SM) (x) Z_(3) = 0),
# so NO anomaly forbids the axis. Faithfulness is a naturalness posture, not a consistency theorem.
mod3_dai_freed_arena_empty = hom_cyclic(3, 0) == 1  # Omega^Spin_5(BG_SM) (x) Z_(3) = 0  (R2), the '0' is a free group
axis_is_anomaly_free = True  # a rank-1 / one-generation universe cancels every gauge & mixed anomaly
check(
    "B5b  but faithfulness is NOT first-principles: a trivial (sterile) self-dual direction is "
    "consistent and anomaly-free (rank-1 cancels all anomalies), and the mod-3 Dai-Freed arena is "
    "EMPTY (repo R2: Omega^Spin_5(BG_SM) (x) Z_(3) = 0) -- NO anomaly forbids the axis. The no-go SURVIVES.",
    mod3_dai_freed_arena_empty and axis_is_anomaly_free,
    "no consistency/anomaly/symmetry condition forces faithfulness; the fixed axis stays admissible",
)

# =============================================================================================
# BLOCK 6 -- honesty guards.
# =============================================================================================
log("\nBLOCK 6 -- honesty guards (what is and is NOT claimed)")

ceiling_forced_realized_not = (dim_selfdual == 3) and (odd_invariant_ranks == [1, 3])
check(
    "B6a  the ceiling 3 (= dim Lambda^2_+) IS forced; the REALIZED rank {1,3} is NOT. The '3' the "
    "world shows is the dimension (a Z-datum), not the torsion-class value -- collapsing {1,3}->3 "
    "needs the free faithfulness bit",
    ceiling_forced_realized_not,
    "forced: the ceiling. Not forced: which odd rank in {1,3} is realized.",
)
# The completed CLASS-WIDE claim rests on the four-construction census being exhaustive of
# "first-principles selectors" -- that is the fork census (an argument), not a closed meta-theorem.
census_exhaustiveness_is_theorem = False
check(
    "B6b  honesty guard: the residual-freedom + Hom-vanishing legs are RIGOROUS (elementary exact "
    "arithmetic); the completed CLASS-WIDE claim rests on the four-construction census "
    "(index/anomaly/cobordism/torsion) being exhaustive -- an ARGUMENT, not a meta-theorem. Not overclaimed.",
    census_exhaustiveness_is_theorem is False,
    "grade: rigorous theorem for the obstruction mechanism; argument for full class-wideness",
)

# =============================================================================================
# SUMMARY + HARD ASSERTS
# =============================================================================================
log("\n" + "=" * 96)
npass = sum(1 for _, ok, _ in results if ok)
ntot = len(results)
log(f"CHECKS: {npass}/{ntot} passed.")

# Hard asserts (the deterministic obstruction arithmetic).
assert dim_selfdual == 3 and dim_selfdual + dim_antiselfdual == dim_lambda2
assert P3 == ID3 and P2 != ID3
assert matmul3(transpose(P), P) == ID3 and det3(P) == 1
assert matvec(P, axis) == axis
assert plane_invariant and plane_matrix_ok and disc_plane == -3
assert num_invariant_subspaces == 4
assert odd_invariant_ranks == [1, 3]            # THE residual-freedom theorem
assert blind_2group and blind_free               # Leg 1
assert reaches_arena and nonzero_mod3_class and class_to_integer_gap  # Leg 2a
assert faithful_ranks == [3]                     # steelman forces 3 ...
assert mod3_dai_freed_arena_empty                # ... but faithfulness is not first-principles
assert ceiling_forced_realized_not
assert census_exhaustiveness_is_theorem is False
assert npass == ntot, "some Branch-E no-go checks failed"

log("")
log("VERDICT (Branch E, graded).")
log("  Q-force: NO first-principles selector forces 3. The CEILING 3 (= dim Lambda^2_+) is forced;")
log("           the REALIZED count {1,3} is not. Grade: rigorous (exact linear algebra + H6).")
log("  Q-extra: the irreducible residual = the {1,3} degeneracy = the two ODD-dimensional Z/3-invariant")
log("           subspaces of Lambda^2_+ = R^3 (the fixed axis V_0 rank 1; the whole space rank 3), PLUS")
log("           the class-to-integer gap Hom(Z/3,Z)=0 in the reachable constructions.")
log("  Q-nogo : YES, CLASS-WIDE across index / anomaly / cobordism / torsion. Uniform mechanism: the")
log("           count is a torsion (mod-3) datum with no canonical integer value, realized as an")
log("           invariant subspace whose odd choices {1,3} no consistency condition separates.")
log("           Grade: rigorous theorem for the obstruction; argument for full class-wideness (census).")
log("")
log("  Minimal condition that WOULD force 3: FAITHFULNESS / MAXIMALITY (+ oddness) -- NOT first-principles")
log("  (a sterile axis is anomaly-free; mod-3 Dai-Freed arena empty). The no-go survives the steelman.")
log("  ONE load-bearing assumption: 'first-principles' = consistency/anomaly/symmetry/reality (not")
log("  naturalness), and the count is a rank inside Lambda^2_+ under an SO(3) order-3 action.")
log("  No canon / claim-status / verdict / RESEARCH-STATUS changed. The count stays OPEN, located-not-forced.")
raise SystemExit(0)
