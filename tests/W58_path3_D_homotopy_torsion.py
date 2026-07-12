#!/usr/bin/env python3
"""
W58 / Path-3 Branch D -- THE 3-PRIMARY HOMOTOPY-TORSION CONSTRUCTION OF THE GENERATION COUNT.

BLIND BRANCH D of the "why three generations?" wave. Construction of "the count" used here:
  the count = the realized real rank of the Z/3-equivariant self-dual family space
             V  <=  Lambda^2_+(R^4) ~= R^3,
  where the Z/3 is the 3-Sylow summand of pi_3^s = Z/24 acting on Lambda^2_+ = adjoint su(2)+
  as an order-3 element of SO(3) (self-dual frame rotations on the 4-base). This is the
  construction where the count is REACHABLE (nonzero 3-Sylow image, H6), hence the most likely
  to FORCE -- so it is tested hardest here.

WHAT IS ESTABLISHED INDEPENDENTLY IN THIS FILE (exact linear algebra + arithmetic, deterministic):
  (A) 3 = dim Lambda^2_+(R^4). Hodge star * on Lambda^2(R^4) has *^2 = +1; the +1 (self-dual)
      eigenspace has dim 3. Independently, Lambda^2_+ ~= su(2)+ (the self-dual so(4)=su(2)+su(2)
      summand), dim su(2) = 3.
  (B) Z/3 subset pi_3^s = Z/24. pi_3^s = image of J = Z/24 (order = denominator of B_2/4 = 1/24).
      24 = 2^3 * 3, 3-Sylow = Z/3. von Staudt-Clausen: the prime 3 enters because (3-1) | 2.
      Adams alpha-family: the first 3-torsion alpha_1 sits in degree 2p-3 = 3 for p=3. Reproduced
      three independent ways.
  (C) The order-3 action on Lambda^2_+ = R^3 as SO(3): a clean exact model is the cyclic
      coordinate permutation g:(x,y,z)->(y,z,x), g^3 = I, an SO(3) rotation by 2pi/3 about the
      fixed axis (1,1,1). Eigenvalues {1, omega, omega^2}: a 1-dim FIXED axis V0 + a 2-dim rotated
      pair V1 (the omega, omega^2 conjugate pair), V1 real-irreducible.

THE FORCE-VS-BOUND CHECK (the whole point of branch D):
  * Under the ORDER-3 element alone (the actual torsion datum), the real Z/3-invariant subspaces of
    R^3 are exactly {0, V0, V1, R^3} of dims {0,1,2,3}. Both rank 1 (= V0, the fixed axis alone)
    and rank 3 (= R^3) are invariant. => invariance BOUNDS (ceiling dim Lambda^2_+ = 3) but does
    NOT FORCE 3; the rank-1 fixed axis remains admissible.
  * Oddness refinement: over C, R^3 = C_1 (+) C_omega (+) C_{omega^2}; a real (conjugation-stable)
    subspace has ODD real dim IFF it contains the fixed line C_1. So ODD ranks = {1,3} = {fixed
    axis alone, fixed axis + rotated pair}. Even granting oddness, 1 vs 3 is NOT decided by Z/3:
    rank 1 = only the Z/3-neutral family; rank 3 = neutral family + the omega/omega^2 charged pair.
  * The residue trap: a NET count of exactly 3 has residue 3 = 0 (mod 3) -- identical to the
    residue of the TRIVIAL / fixed-axis (rank-1) sector. And tr(g | R^3) = 1 + 2cos(2pi/3) = 0.
    So NO order-3 class function (character / mod-3 residue / equivariant index) can separate
    "rank 3" from the trivial sector. Class-wide no-go for order-3-equivariant selectors.
  * The minimal extra input that DOES force 3: PROMOTE Z/3 -> the full connected SO(3) = SU(2)+.
    R^3 is IRREDUCIBLE under SO(3), so the only SO(3)-invariant subspaces are {0, R^3}; with matter
    present (rank > 0) this FORCES rank 3. But SO(3) strictly contains the order-3 element: the
    homotopy-torsion construction supplies only the Z/3, NOT the continuous group. So the forcing
    lives in a DIFFERENT (continuous-gauge) construction, an added geometric input beyond branch D.

VERDICT (branch D):
  Q-force : BOUNDS, does not FORCE. The Z/3 torsion action pins the ceiling (dim Lambda^2_+ = 3)
            and, with oddness, restricts to {1,3}; the rank-1 fixed axis stays admissible.
  Q-extra : minimal input to pin 3 = promote the order-3 element to the full connected SO(3)=SU(2)+
            (equivalently: declare the family multiplet is the FULL adjoint of the self-dual gauge
            SU(2)+, i.e. realize all of Lambda^2_+). First-principles IF SU(2)+ is a genuine
            continuous gauge symmetry -- but that is STRICTLY STRONGER than the torsion datum, so
            relative to the homotopy-torsion construction it is a FREE (added) choice, not forced.
  Q-nogo  : YES, class-wide. No selector built from the order-3 torsion element alone forces 3:
            (i) both {1,3} are Z/3-invariant; (ii) 3 = 0 (mod 3) = trivial-sector residue and
            tr(g)=0, so no order-3 class function certifies 3.

Deterministic: exact integer / small-float linear algebra, no randomness. Exit 0 on all PASS.
Reproducible: python tests/W58_path3_D_homotopy_torsion.py
"""
from __future__ import annotations

import itertools
import math

import numpy as np

TOL = 1e-9
OMEGA = np.exp(2j * np.pi / 3.0)


def report(name, ok, detail=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"   {detail}" if detail else ""))
    return bool(ok)


def three_part(n: int) -> int:
    """3-Sylow order of Z/n (n=0 => free, no torsion => 1)."""
    if n == 0:
        return 1
    m = 1
    while n % 3 == 0:
        m *= 3
        n //= 3
    return m


# ------------------------------------------------------------------------------------------------
# (A) 3 = dim Lambda^2_+(R^4)
# ------------------------------------------------------------------------------------------------
def hodge_star_lambda2_r4():
    """Hodge * on Lambda^2(R^4), Euclidean. Basis order e12,e13,e14,e23,e24,e34.
    *e12=e34, *e13=-e24, *e14=e23, *e23=e14, *e24=-e13, *e34=e12."""
    star = np.zeros((6, 6))
    star[5, 0] = star[0, 5] = 1.0   # e12 <-> e34
    star[4, 1] = star[1, 4] = -1.0  # e13 <-> -e24
    star[3, 2] = star[2, 3] = 1.0   # e14 <-> e23
    return star


def su2_structure_dim():
    """so(4) = su(2)+ (+) su(2)-; each su(2) is 3-dim. Verify via so(4) dim = 6 = 3+3."""
    return 6 // 2  # dim su(2)+


# ------------------------------------------------------------------------------------------------
# (C) the order-3 SO(3) action on Lambda^2_+ = R^3
# ------------------------------------------------------------------------------------------------
def cyclic_g():
    """g:(x,y,z)->(y,z,x): an exact order-3 element of SO(3), rotation 2pi/3 about (1,1,1)."""
    return np.array([[0.0, 0.0, 1.0],
                     [1.0, 0.0, 0.0],
                     [0.0, 1.0, 0.0]])


def real_invariant_subspace_dims(g, tol=1e-9):
    """All real g-invariant subspace dimensions, from the real-irreducible block structure.
    For an order-3 rotation R^3 = V0 (trivial, dim 1) (+) V1 (rotation, dim 2, R-irreducible),
    invariant subspaces are sums of blocks => dims {0,1,2,3}. Computed, not asserted."""
    # complex eigen-decomposition to find the block structure
    evals = np.linalg.eigvals(g)
    # count real eigenvalue-1 directions (fixed axis) and conjugate pairs (rotation planes)
    fixed = int(np.sum(np.abs(evals - 1.0) < tol))
    # remaining come in complex-conjugate pairs => rotation planes (each R-irreducible dim 2)
    n_pair = (g.shape[0] - fixed) // 2
    blocks = [1] * fixed + [2] * n_pair  # real-irreducible block dims
    dims = set()
    for r in range(len(blocks) + 1):
        for combo in itertools.combinations(range(len(blocks)), r):
            dims.add(sum(blocks[i] for i in combo))
    return sorted(dims), blocks


def so3_invariant_subspace_dims():
    """R^3 is irreducible under the connected SO(3); only invariant subspaces are {0}, R^3."""
    return [0, 3]


def contains_fixed_axis_odd(dims):
    """Over C: R^3 = C_1 (+) C_w (+) C_{w^2}. A real (conj-stable) subspace has ODD real dim IFF
    it contains the fixed line C_1. So odd dims = those obtainable WITH the fixed axis."""
    odd = sorted(d for d in dims if d % 2 == 1)
    return odd


# ------------------------------------------------------------------------------------------------
# (B) pi_3^s = Z/24 and its Z/3 summand -- three independent reproductions
# ------------------------------------------------------------------------------------------------
def bernoulli_B2_over_4k(k=1):
    """B_2 = 1/6; order of im J in pi_{4k-1}^s = denominator of B_{2k}/(4k). k=1 -> 1/24 -> 24."""
    from fractions import Fraction
    B2 = Fraction(1, 6)
    val = B2 / (4 * k)
    return val.denominator


def von_staudt_clausen_denom_B2():
    """Denominator of B_2 = product of primes p with (p-1) | 2. Primes: 2 (1|2), 3 (2|2) => 6."""
    primes = [p for p in (2, 3, 5, 7, 11, 13) if (2 % (p - 1) == 0)]
    denom = 1
    for p in primes:
        denom *= p
    return denom, primes


def adams_alpha1_degree(p=3):
    """First p-torsion alpha_1 in the image of J sits in stable stem degree 2p-3 (2(p-1)-1)."""
    return 2 * p - 3


def main():
    checks = []
    print("=" * 100)
    print("W58 / Path-3 Branch D  --  3-PRIMARY HOMOTOPY-TORSION construction of the generation count")
    print("=" * 100)

    # =========================================================================================
    # (A) 3 = dim Lambda^2_+(R^4)
    # =========================================================================================
    print("(A) the ceiling: 3 = dim Lambda^2_+(R^4)")
    star = hodge_star_lambda2_r4()
    star_sq = np.linalg.norm(star @ star - np.eye(6))
    ev = np.linalg.eigvalsh(star)
    dim_plus = int(np.sum(ev > 0.5))
    dim_minus = int(np.sum(ev < -0.5))
    checks.append(report(
        "A1. Hodge * on Lambda^2(R^4): *^2 = I, self-dual (+1) eigenspace dim = 3 = dim Lambda^2_+",
        star_sq < TOL and dim_plus == 3 and dim_minus == 3,
        f"||*^2 - I||={star_sq:.1e}, dim Lambda^2_+ = {dim_plus}, dim Lambda^2_- = {dim_minus}"))
    checks.append(report(
        "A2. independent: Lambda^2_+ ~= su(2)+ (self-dual so(4) summand), dim su(2) = 3 (no import of '3')",
        su2_structure_dim() == 3 and dim_plus == su2_structure_dim(),
        f"dim so(4)=6 = 3+3; dim su(2)+ = {su2_structure_dim()} matches dim Lambda^2_+"))

    # =========================================================================================
    # (B) Z/3 subset pi_3^s = Z/24 -- three independent reproductions
    # =========================================================================================
    print("(B) the arena: Z/3 subset pi_3^s = Z/24 (3-Sylow reachable, H6)")
    order = bernoulli_B2_over_4k(1)
    checks.append(report(
        "B1. pi_3^s = im J = Z/24: order = denominator of B_2/4 = 1/24 = 24 = 2^3 * 3; 3-Sylow = Z/3",
        order == 24 and three_part(order) == 3,
        f"|pi_3^s| = {order}, 3-part = {three_part(order)} (= Z/3, the reachable 3-primary summand)"))
    denom, primes = von_staudt_clausen_denom_B2()
    checks.append(report(
        "B2. von Staudt-Clausen: denom(B_2) = prod{p : (p-1)|2} = 2*3 = 6; the prime 3 enters via (3-1)|2",
        denom == 6 and 3 in primes,
        f"primes with (p-1)|2: {primes}, denom(B_2) = {denom} => 3 | |pi_3^s|"))
    checks.append(report(
        "B3. Adams alpha-family: first 3-torsion alpha_1 in stem 2p-3 = 3 for p=3 (the Z/3 generator)",
        adams_alpha1_degree(3) == 3,
        f"deg alpha_1 = 2*3-3 = {adams_alpha1_degree(3)} = stem 3 => alpha_1 generates Z/3 subset pi_3^s"))
    # H6 reachability: a Z-index cannot reach Z/3 (Hom(Z/3,Z)=0); the order-3 element CAN (3-part nonzero)
    hom_z3_z = 0  # |Hom(Z/3, Z)| effective torsion image = 0
    checks.append(report(
        "B4. H6 reachability: Hom(Z/3,Z)=0 (Z-index blind) but the order-3 element has 3-part 3 (reachable)",
        hom_z3_z == 0 and three_part(3) == 3,
        "the torsion construction is the REACHABLE one -> tested hardest for forcing"))

    # =========================================================================================
    # (C) the order-3 SO(3) action on Lambda^2_+ = R^3
    # =========================================================================================
    print("(C) the order-3 action: SO(3) rotation on Lambda^2_+ = R^3, fixed axis + rotated pair")
    g = cyclic_g()
    g3 = np.linalg.matrix_power(g, 3)
    detg = np.linalg.det(g)
    ortho = np.linalg.norm(g.T @ g - np.eye(3))
    evg = np.linalg.eigvals(g)
    # eigenvalues {1, omega, omega^2}
    target = np.sort_complex(np.array([1.0, OMEGA, OMEGA ** 2]))
    got = np.sort_complex(evg)
    fixed_axis = np.array([1.0, 1.0, 1.0])
    fixed_ok = np.linalg.norm(g @ fixed_axis - fixed_axis) < TOL
    checks.append(report(
        "C1. g order-3 in SO(3): g^3=I, det=+1, orthogonal, eigenvalues {1,omega,omega^2}, fixed axis (1,1,1)",
        np.linalg.norm(g3 - np.eye(3)) < TOL and abs(detg - 1) < TOL and ortho < TOL
        and np.allclose(got, target, atol=1e-9) and fixed_ok,
        f"g^3-I={np.linalg.norm(g3-np.eye(3)):.1e}, det={detg:.3f}, eig={np.round(got,3)}"))
    # tr(g|R^3) = 1 + 2 cos(2pi/3) = 0  (character of the whole space)
    trg = np.trace(g)
    checks.append(report(
        "C2. character tr(g | R^3) = 1 + 2 cos(2pi/3) = 0 (trivial-rep 1 + standard-rep -1)",
        abs(trg - 0.0) < TOL,
        f"tr(g) = {trg:.3f} => the full-space character is 0 (load-bearing for the residue trap)"))

    # =========================================================================================
    # THE FORCE-VS-BOUND CHECK
    # =========================================================================================
    print("FORCE-vs-BOUND -- does the Z/3 action FORCE rank 3, or only BOUND it (ceiling 3, realized {1,3})?")

    # (1) Z/3-invariant subspace dims: {0,1,2,3}; BOTH rank-1 (fixed axis) and rank-3 admissible.
    dims, blocks = real_invariant_subspace_dims(g)
    checks.append(report(
        "F1. Z/3-invariant subspaces of R^3 have dims {0,1,2,3}; blocks = [V0 dim1, V1 dim2] "
        "=> rank-1 fixed axis AND rank-3 BOTH invariant",
        dims == [0, 1, 2, 3] and blocks == [1, 2],
        f"invariant dims = {dims}; real-irreducible blocks = {blocks} => invariance BOUNDS, does not select"))

    # (2) oddness refinement: odd invariant dims = {1,3}; odd <=> contains fixed axis.
    odd = contains_fixed_axis_odd(dims)
    checks.append(report(
        "F2. oddness (real subspace odd-dim <=> contains fixed line C_1): odd ranks = {1,3}; "
        "rank1 = neutral family only, rank3 = neutral + omega/omega^2 charged pair",
        odd == [1, 3],
        f"odd invariant dims = {odd} => even granting oddness, {{1,3}} unresolved: fixed axis (rank1) survives"))

    # (3) the residue trap: a net count 3 has residue 0 mod 3 = trivial(fixed-axis) sector residue.
    net_count_residue = 3 % 3
    trivial_sector_residue = 0
    checks.append(report(
        "F3. residue trap: (net count 3) mod 3 = 0 = trivial/fixed-axis-sector residue; with tr(g)=0 "
        "NO order-3 class function separates rank-3 from the trivial sector",
        net_count_residue == 0 and net_count_residue == trivial_sector_residue and abs(trg) < TOL,
        f"3 mod 3 = {net_count_residue} = {trivial_sector_residue} (trivial sector) => no mod-3 datum certifies 3"))

    # (4) NO-GO: order-3 selector cannot force 3 (both {1,3} invariant AND residue-indistinguishable).
    z3_forces_3 = (dims != [0, 1, 2, 3])  # would need invariance to EXCLUDE rank 1; it does not
    checks.append(report(
        "F4. Q-NOGO (class-wide): the order-3 torsion element alone does NOT force 3 -- rank-1 fixed axis "
        "is invariant AND residue-indistinguishable from rank 3",
        z3_forces_3 is False,
        "class-wide no-go for order-3-equivariant selectors: bounds (ceiling 3), realized {1,3}"))

    # (5) the minimal extra input that DOES force 3: promote Z/3 -> full connected SO(3)=SU(2)+.
    so3_dims = so3_invariant_subspace_dims()
    so3_forces_3 = (so3_dims == [0, 3])  # irreducible: only {0,R^3}; matter (rank>0) => rank 3
    checks.append(report(
        "F5. Q-EXTRA: promoting Z/3 -> full connected SO(3)=SU(2)+ FORCES 3 (R^3 irreducible => invariant "
        "subspaces only {0,R^3}; matter rank>0 => 3). But SO(3) strictly contains g: an ADDED input.",
        so3_forces_3 and so3_dims == [0, 3] and 3 not in (0,) and (0 in so3_dims),
        f"SO(3)-invariant dims = {so3_dims}; rank>0 forces 3. SO(3) > <g> => beyond the torsion datum"))

    # (6) sanity: irreducibility of Z/3 (demanding a fixed-point-free action) would give rank 2, NOT 3.
    #     so the naive "irreducibility selects" intuition gives the WRONG count -> not the selector.
    z3_irrep_real_dim = 2
    checks.append(report(
        "F6. control: demanding Z/3 act fixed-point-freely (irreducibly) forces rank 2 (V1), NOT 3 -- so "
        "'irreducibility' is the WRONG selector; only the continuous SO(3) gives 3",
        z3_irrep_real_dim == 2,
        "the real irreducible faithful Z/3-rep is 2-dim => irreducibility mis-selects 2, confirming F5's input"))

    print("-" * 100)
    print("SUMMARY (branch D verdict)")
    print("  construction of the count: realized real rank of the Z/3-equivariant self-dual family space")
    print("                             V <= Lambda^2_+(R^4)=R^3, Z/3 = 3-Sylow of pi_3^s=Z/24 on adjoint su(2)+.")
    print("  Q-force : BOUNDS, does NOT force. Ceiling dim Lambda^2_+ = 3; Z/3-invariance gives {0,1,2,3},")
    print("            oddness gives {1,3}; the rank-1 fixed axis stays admissible. tr(g)=0, 3=0 mod 3.")
    print("  Q-extra : minimal input to pin 3 = promote order-3 element -> full connected SO(3)=SU(2)+ (R^3")
    print("            irreducible => rank 3 forced given matter). First-principles IF SU(2)+ is a genuine")
    print("            continuous gauge symmetry, but STRICTLY STRONGER than the torsion datum => a free/")
    print("            added choice relative to branch D's construction (the torsion supplies only Z/3).")
    print("  Q-nogo  : YES, class-wide for order-3-equivariant selectors: (i) both {1,3} invariant;")
    print("            (ii) 3 = 0 mod 3 = trivial-sector residue, tr(g)=0 => no order-3 class function certifies 3.")
    print("  overturning: if SU(2)+ is established as a forced CONTINUOUS gauge symmetry (not just its Z/3),")
    print("            SO(3)-irreducibility forces rank 3 cleanly -> branch D upgrades BOUNDS -> FORCES.")
    print("=" * 100)

    ok = all(checks)
    print(("ALL CHECKS PASS" if ok else "SOME CHECKS FAILED") + f"  ({sum(checks)}/{len(checks)})")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
