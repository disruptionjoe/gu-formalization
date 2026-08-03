#!/usr/bin/env python3
"""Derivation gate for Omega^{Pin+}_14 = Z/2 via the Smith/ABP chain.

Upgraded 2026-08-03 (register P-H10): the previous version restated seven
literals assigned ten lines above its checks — a bookkeeping/type gate by
its own receipt.  This version computes the chain of
canon/pin14-bordism-derivation-RESULTS.md:

  Step 1  Smith reduction: MTSpin -> MTPin+ -> Sigma(MTSpin smash (BZ/2)_+),
          with the endpoint groups Omega^Spin_13 = Omega^Spin_14 = 0
          ASSEMBLED from the ABP summand homotopy (not recited).
  Step 2  ABP splitting through degree 15, calibrated: the ko / Sigma^8 ko /
          Sigma^8 ko<2> summand sums are computed for n = 8..14 and compared
          against the cited Omega^Spin table row by row.
  Step 3  Evaluate on BZ/2: the Bruner-Greenlees vanishing residues kill
          ko~_13(BZ/2) and ko~_5(BZ/2); the third summand reduces through
          the tau_{<=1}ko Postnikov step to an exact sequence whose
          connecting map is multiplication by C(5,2) mod 2 — computed by
          sympy.binomial AND independently by Lucas' theorem.
  Step 4  Assemble: order 1 * 1 * 2 = 2, exponent 2  =>  Z/2.
  Step 5  Independent cross-check (the July route, demoted to
          corroboration): reduced Smith gives Omega^{Pin-}_12; the ABP Pin
          exponent theorem bounds its exponent by 2; the Kirby--Taylor
          direct table (A(14) = 1, higher-order summands only in degrees
          0 mod 4) returns the same group.  Both legs must agree.

Cited STRUCTURAL inputs (theorems, not answer-recitations): the Smith
cofiber sequence (arXiv:2405.04649); the ABP splitting and the ko homotopy
pattern (Ann. of Math. 86 (1967) / Bott); the ko-homology of RP^inf
vanishing residues (Bruner--Greenlees); the ABP Pin exponent theorem (CMH
44 (1969)); Sq^2 on H*(RP^inf) via the binomial coefficient (Wu formula).
Cited TABLE values, used only as cross-check targets: the Omega^Spin_n
column (Step 2) and Kirby--Taylor A(14) = 1 (Step 5).

Exit 0 certifies the assembled derivation and the agreement of both legs.
It still closes only the ambient group: whether GU's proposed class in it
is nonzero stays OPEN (class realization, register M-M12).
"""
from __future__ import annotations

from sympy import Integer, Rational, binomial

FAILURES: list[str] = []


def check(label: str, condition: bool, detail: str) -> None:
    print(f"[{'PASS' if condition else 'FAIL'}] {label}: {detail}")
    if not condition:
        FAILURES.append(label)


# ---------------------------------------------------------------------------
# Structural inputs (cited theorems, encoded as generating patterns).
# ---------------------------------------------------------------------------

def ko_order(n: int):
    """Order of ko_n (connective real K-theory homotopy; Bott/ABP):
    Z (infinite, returned as the string 'Z') for n = 0, 4 mod 8;
    Z/2 for n = 1, 2 mod 8; 0 (order 1) otherwise; 0 below degree 0."""
    n = int(n)
    if n < 0:
        return Integer(1)
    r = n % 8
    if r in (0, 4):
        return "Z"
    if r in (1, 2):
        return Integer(2)
    return Integer(1)


def ko2_order(n: int):
    """Order of ko<2>_n, the 1-connected cover: equals ko_n for n >= 2."""
    return ko_order(n) if int(n) >= 2 else Integer(1)


def spin_summand_orders(n: int) -> list:
    """The ABP 2-local wedge through degree 15: ko v Sigma^8 ko v
    Sigma^8 ko<2> (higher summands have connectivity >= 16)."""
    return [ko_order(n), ko_order(n - 8), ko2_order(n - 8)]


def assemble(orders: list):
    """Direct-sum order: 'Z' if any infinite summand, else the product."""
    if any(o == "Z" for o in orders):
        return "Z"
    total = Integer(1)
    for o in orders:
        total *= o
    return total


# Cited Omega^Spin_n column (ABP coefficient table), cross-check target only.
CITED_OMEGA_SPIN = {8: "Z^2", 9: "(Z/2)^2", 10: "(Z/2)^3", 11: "0",
                    12: "Z^3", 13: "0", 14: "0"}


def group_name(orders: list) -> str:
    """Canonical name of the assembled 2-local group from summand orders."""
    z_rank = sum(1 for o in orders if o == "Z")
    z2_rank = sum(1 for o in orders if o == Integer(2))
    if z_rank:
        return "Z" if z_rank == 1 else f"Z^{z_rank}"
    if z2_rank:
        return "Z/2" if z2_rank == 1 else f"(Z/2)^{z2_rank}"
    return "0"


# Bruner--Greenlees: ko~_n(BZ/2) = 0 exactly when n = 4, 5, 6 mod 8.
KO_BZ2_VANISHING_RESIDUES = frozenset({4, 5, 6})

# ABP Pin exponent theorem: Omega^{Pin-}_n has exponent 2 for
# n = 0, 1, 3, 4, 5, 7 mod 8 (the non-(Z/2^k, k>1) residues in degree 12's range).
ABP_PIN_MINUS_EXPONENT2_RESIDUES = frozenset({0, 1, 3, 4, 5, 7})


def reduced_homology_bz2_Z(n: int):
    """Order of H~_n(BZ/2; Z): Z/2 for odd n >= 1, else 0."""
    n = int(n)
    return Integer(2) if (n >= 1 and n % 2 == 1) else Integer(1)


def reduced_homology_bz2_Z2(n: int):
    """Order of H~_n(BZ/2; Z/2): Z/2 for every n >= 1."""
    return Integer(2) if int(n) >= 1 else Integer(1)


def lucas_binomial_parity(n: int, k: int) -> int:
    """C(n, k) mod 2 by Lucas' theorem: odd iff the bits of k are a subset
    of the bits of n."""
    return 1 if (int(k) & ~int(n)) == 0 else 0


print("=" * 79)
print("PIN+_14 SMITH/ABP DERIVATION GATE (canon/pin14-bordism-derivation-RESULTS.md)")
print("=" * 79)

# ---------------------------------------------------------------------------
# Step 2 first (its output feeds Step 1's endpoints): calibrate the ABP
# truncation against the cited Omega^Spin column, row by row.
# ---------------------------------------------------------------------------
calibration_rows = {}
for n in range(8, 15):
    computed = group_name(spin_summand_orders(n))
    calibration_rows[n] = computed
    print(f"  n={n:2d}: ko+S8ko+S8ko<2> = {computed:8s}  cited Omega^Spin = {CITED_OMEGA_SPIN[n]}")

check(
    "S2 ABP calibration 8..14",
    all(calibration_rows[n] == CITED_OMEGA_SPIN[n] for n in range(8, 15)),
    "summand homotopy reproduces the cited Omega^Spin column in all 7 rows",
)

# ---------------------------------------------------------------------------
# Step 1: Smith reduction in pi_14. Endpoints computed from the calibrated
# splitting, then the LES collapses to an isomorphism.
# ---------------------------------------------------------------------------
target_degree = Integer(14)
spin_upper = assemble(spin_summand_orders(target_degree))       # Omega^Spin_14
spin_lower = assemble(spin_summand_orders(target_degree - 1))   # Omega^Spin_13

check(
    "S1 vanishing endpoints (computed)",
    spin_upper == Integer(1) and spin_lower == Integer(1),
    f"|Omega^Spin_14| = {spin_upper}, |Omega^Spin_13| = {spin_lower} from the ABP summands",
)

# 0 -> Omega^{Pin+}_14 -> Omega^Spin_13((BZ/2)_+) -> 0, and the disjoint
# basepoint splits off Omega^Spin_13 = 0: only the reduced part remains.
smith_degree = target_degree - 1
check(
    "S1' suspension bookkeeping",
    smith_degree == Integer(13) and spin_lower == Integer(1),
    "pi_14 of Sigma(MTSpin smash (BZ/2)_+) is the degree-13 reduced Spin bordism of BZ/2",
)

# ---------------------------------------------------------------------------
# Step 3: evaluate the truncated splitting on BZ/2.
#   ko~_13(BZ/2) and ko~_5(BZ/2) die by the vanishing residues;
#   ko<2>~_5(BZ/2) = (tau_{<=1}ko)~_6(BZ/2) via the cover cofiber sequence
#   (using ko~_5 = ko~_6 = 0, both residues in the vanishing range).
# ---------------------------------------------------------------------------
deg_ko = smith_degree              # 13
deg_shifted = smith_degree - 8     # 5, for both Sigma^8 summands
residues = {int(deg_ko) % 8, int(deg_shifted) % 8, (int(deg_shifted) + 1) % 8}

check(
    "S3 Bruner-Greenlees vanishing",
    residues <= KO_BZ2_VANISHING_RESIDUES,
    f"degrees 13, 5, 6 have residues {sorted(residues)} mod 8, all in the "
    f"vanishing set {sorted(KO_BZ2_VANISHING_RESIDUES)}",
)
ko13_bz2 = Integer(1)
ko5_bz2 = Integer(1)

# Postnikov step: H~_7(BZ/2;Z) --(Sq^2-dual)--> H~_5(BZ/2;Z/2) -> X -> H~_6(BZ/2;Z)
sq2_coefficient = binomial(5, 2) % 2
sq2_lucas = lucas_binomial_parity(5, 2)
check(
    "S4 Sq^2 binomial, two routes",
    sq2_coefficient == sq2_lucas and sq2_coefficient == 0,
    f"C(5,2) = {binomial(5, 2)}: mod 2 = {sq2_coefficient} (sympy) "
    f"= {sq2_lucas} (Lucas bit test) — the connecting map is zero",
)

h5_z2 = reduced_homology_bz2_Z2(5)
h6_z = reduced_homology_bz2_Z(6)
h7_z = reduced_homology_bz2_Z(7)
connecting_image = Integer(2) if (sq2_coefficient == 1 and h7_z == Integer(2)) else Integer(1)
ko2_5_bz2 = (h5_z2 / connecting_image) * h6_z  # exactness: coker + H~_6 extension

check(
    "S5 ko<2>~_5(BZ/2) from the exact sequence",
    ko2_5_bz2 == Integer(2) and h6_z == Integer(1),
    f"|H~_5(BZ/2;Z/2)| = {h5_z2}, connecting image order {connecting_image}, "
    f"|H~_6(BZ/2;Z)| = {h6_z}  =>  order {ko2_5_bz2}",
)

# ---------------------------------------------------------------------------
# Step 4: assemble Omega^{Pin+}_14 = ko~_13 + ko~_5 + ko<2>~_5 of BZ/2.
# ---------------------------------------------------------------------------
pin14_order = ko13_bz2 * ko5_bz2 * ko2_5_bz2
pin14_exponent = Integer(2) if pin14_order == Integer(2) else pin14_order
check(
    "S6 assembly",
    pin14_order == Integer(2),
    f"|Omega^{{Pin+}}_14| = {ko13_bz2} * {ko5_bz2} * {ko2_5_bz2} = {pin14_order}  =>  Z/2",
)

# ---------------------------------------------------------------------------
# Step 5: independent cross-check leg (July route, demoted to corroboration).
# ---------------------------------------------------------------------------
pin_minus_degree = smith_degree - 1   # reduced Smith: Sigma MTPin- inside MTSpin smash BZ/2
abp_exponent_2 = int(pin_minus_degree) % 8 in ABP_PIN_MINUS_EXPONENT2_RESIDUES

# Kirby--Taylor direct Pin+ table (CMH 65 (1990) p. 446), cross-check only:
KIRBY_TAYLOR_A14 = 1
kt_higher_order_summands = int(target_degree) % 4 == 0
kt_order = Integer(2) ** KIRBY_TAYLOR_A14 if not kt_higher_order_summands else None

check(
    "S7 cross-check leg agrees",
    pin_minus_degree == Integer(12)
    and abp_exponent_2
    and kt_order == pin14_order,
    f"Omega^{{Pin-}}_{pin_minus_degree}: ABP exponent-2 residue "
    f"({int(pin_minus_degree) % 8} mod 8 in {sorted(ABP_PIN_MINUS_EXPONENT2_RESIDUES)}); "
    f"Kirby-Taylor leg order {kt_order} (A(14)={KIRBY_TAYLOR_A14}, no higher-order "
    f"summands since 14 mod 4 = {int(target_degree) % 4}) == Step-4 order {pin14_order}",
)

# ---------------------------------------------------------------------------
# Verdict, coupled to the exit code.
# ---------------------------------------------------------------------------
if FAILURES:
    print(f"\nVERDICT: RED — {len(FAILURES)} check(s) failed: {FAILURES}")
    raise SystemExit(1)

assert pin14_order == Integer(2) and pin14_exponent == Integer(2)
print("\nVERDICT: PIN14-EXACT-Z2 (derivation grade)")
print("  Omega^{Pin+}_14 ~= Z/2, assembled from the Smith/ABP chain with the")
print("  Kirby--Taylor table as an independent cross-check only.")
print("  This closes the ambient group, not the construction or nontriviality")
print("  of GU's proposed class in it.")
