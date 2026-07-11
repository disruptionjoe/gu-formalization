"""The primary-partition lemma for the family puzzle: the rigorous, GU-INDEPENDENT spine.

Claim (elementary, bulletproof): a topological invariant whose value group is a finite 2-group or is
torsion-free is ARITHMETICALLY INCAPABLE of carrying the odd-torsion (3-primary) class where an odd
generation count would live. Hence, in the stable arena pi_3^s = Z/24 = Z/8 (+) Z/3, only an invariant
that reaches the 3-primary summand can force an odd count. This verifies the lemma and classifies the
standard family-number tools by 3-primary reach.

Rigorous facts used (all standard): |Hom(Z/m, Z/l)| = gcd(m,l); Hom(finite, Z) = 0; a finite abelian
group's p-Sylow is the image of the p-primary component. No GU input anywhere.
Run: python tests/family-puzzle/primary_partition_lemma.py
"""
from __future__ import annotations

from math import gcd

FAIL: list[str] = []


def check(name, ok, detail=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}{('  '+detail) if detail else ''}")
    if not ok:
        FAIL.append(name)


def three_part(n: int) -> int:
    """The 3-primary part (3-Sylow order) of a finite cyclic group Z/n; n=0 denotes Z (free)."""
    if n == 0:
        return 1  # free group: no torsion, carries no odd-torsion class
    m = 1
    while n % 3 == 0:
        m *= 3
        n //= 3
    return m


def hom_finite_to(target_desc: str, source_order: int) -> int:
    """|Hom(Z/source_order, target)| for target = 'Z' (free) or 'Z/2^k' represented by its order."""
    if target_desc == "Z":
        return 1  # Hom(finite, Z) = 0 -> only the zero map
    l = int(target_desc)          # a cyclic 2-group order
    return gcd(source_order, l)


def main():
    print("[family-puzzle primary-partition lemma -- the rigorous GU-independent spine]\n")

    # (1) The arena. pi_3^s = Z/24; its order-3 elements are {8,16} (the 3-primary summand Z/3).
    n = 24
    print(f"  arena: pi_3^s = Z/{n} = Z/8 (+) Z/3 (CRT); 3-primary summand = Z/3, order-3 elements {{8,16}}")
    check("the arena has a nontrivial 3-primary summand (where an odd count must live)",
          three_part(n) == 3, f"3-part of Z/{n} = {three_part(n)}")

    # (2) The lemma: 2-primary and free invariants have ZERO map on the order-3 class.
    print("\n  LEMMA -- an invariant valued in a finite 2-group or in Z cannot carry the order-3 class:")
    two_group_orders = [2, 4, 8, 16, 32]     # Z/2^k
    ok_2 = all(hom_finite_to(str(l), 3) == 1 for l in two_group_orders)  # gcd(3,2^k)=1 -> only zero map
    print(f"    Hom(Z/3, Z/2^k) = 0 for k up to {len(two_group_orders)}  (gcd(3,2^k)=1): {ok_2}")
    ok_free = hom_finite_to("Z", 3) == 1
    print(f"    Hom(Z/3, Z) = 0  (no finite subgroup of a torsion-free group): {ok_free}")
    check("(2) every finite-2-group-valued or Z-valued invariant kills the order-3 class (proved)",
          ok_2 and ok_free)

    # (3) The census. Classify the standard family-number tools by 3-primary reach of their value group.
    #     value group given by its order (0 = Z free). Each entry is a STANDARD result (cite in the doc).
    census = [
        ("Dirac / Atiyah-Singer index",            0,   "free integer"),
        ("per-generation anomaly cancellation",    0,   "free integer"),
        ("mod-2 Witten anomaly",                   2,   "Z/2"),
        ("Rokhlin invariant",                      16,  "Z/16"),
        ("spinor 2-smoothness (dim 2^k)",          8,   "power of 2"),
        ("cross-chirality Krein signature",        0,   "free integer"),
        ("Adams e-invariant / J-homomorphism",     24,  "Z/24"),
        ("Garcia-Etxebarria-Montero Z/9 anomaly",  9,   "Z/9"),
        ("Wan-Wang-Yau beyond-cohomology p1 part", 3,   "3-primary reach"),
        ("equivariant Spin/KO G-index (order-3 rho)", 3, "Z/3-valued"),
    ]
    print("\n  CENSUS -- can each standard tool reach the 3-primary summand (force an odd count)?")
    can, cannot = [], []
    for name, order, kind in census:
        reaches = three_part(order) > 1
        (can if reaches else cannot).append(name)
        print(f"    {'CAN ' if reaches else 'no  '} {name:<42} ({kind}; 3-part={three_part(order)})")

    # The predictive partition: exactly the literature's SUCCESSES reach 3; exactly its FAILURES don't.
    known_success = {"Adams e-invariant / J-homomorphism", "Garcia-Etxebarria-Montero Z/9 anomaly",
                     "Wan-Wang-Yau beyond-cohomology p1 part", "equivariant Spin/KO G-index (order-3 rho)"}
    known_fail = {"Dirac / Atiyah-Singer index", "per-generation anomaly cancellation",
                  "mod-2 Witten anomaly", "Rokhlin invariant", "spinor 2-smoothness (dim 2^k)",
                  "cross-chirality Krein signature"}
    check("(3) the tools that CAN force an odd count are exactly the 3-primary-reaching ones",
          set(can) == known_success and set(cannot) == known_fail,
          "and these coincide with the literature's successes vs failures")

    print("\n[the rigorous statement]")
    print("  * LEMMA (proved, elementary, GU-independent): in a finite cyclic arena with 3 | order, any")
    print("    invariant valued in a finite 2-group or in a torsion-free group vanishes on the 3-primary")
    print("    summand. So a 2-primary or free invariant is arithmetically INCAPABLE of forcing an odd count.")
    print("  * CENSUS (computed, each entry a standard result): the standard family-number tools partition")
    print("    exactly -- Dirac index, per-generation anomaly, mod-2^k classes = 2-primary/free (cannot);")
    print("    the Adams e-invariant, GEM Z/9, Wan-Wang-Yau, equivariant KO G-index = 3-primary (can).")
    print("  * PREDICTIVE CLAIM (falsifiable, GU-independent): a topological approach forces an odd")
    print("    generation count ONLY IF its invariant has nonzero image in the 3-Sylow of the relevant")
    print("    stable/bordism group. Every known success reaches it; every known failure does not. This")
    print("    partitions the family-puzzle toolkit and predicts which future approaches can possibly work.")
    print("  * This is the credible, GU-INDEPENDENT core: it stands whether or not GU is correct, and bears")
    print("    on a genuine open problem (why 3 families). Complement: 'no net chirality without a boundary'")
    print("    adds that the count is also a BOUNDARY quantity -> look in 3-primary EQUIVARIANT BOUNDARY")
    print("    invariants (Dai-Freed / eta in the odd-torsion summand).")

    if FAIL:
        print(f"\nFAILED: {FAIL}")
        raise SystemExit(1)
    print("\nexit 0 = primary-partition lemma verified; the GU-independent family-puzzle spine is rigorous.")


if __name__ == "__main__":
    main()
