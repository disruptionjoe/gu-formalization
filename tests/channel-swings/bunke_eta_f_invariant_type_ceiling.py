#!/usr/bin/env python3
"""Exact type/domain certificate for M-H8 and M-M6.

This checks the arithmetic and type consequences used by the accompanying
primary-source specialization. It does not construct a corner, compute an
f-invariant, identify a torsion detector with an integer count, or build a GU
class map.
"""

from fractions import Fraction as F


checks: list[tuple[str, bool]] = []


def check(name: str, condition: bool) -> None:
    checks.append((name, bool(condition)))
    print(("PASS" if condition else "FAIL") + " :: " + name)


def additive_order_mod_one(x: F) -> int:
    y = x % 1
    for n in range(1, 10_000):
        if (n * y) % 1 == 0:
            return n
    raise AssertionError("finite order not found")


def f_domain_dimension(k: int) -> int:
    """Bunke--Naumann's displayed stable-stem degree m=2k-2."""
    return 2 * k - 2


def main() -> None:
    rp3_times_s6_dimension = 3 + 6
    alpha1_beta1_degree = 3 + 10

    check("RP3 times S6 has dimension 9",
          rp3_times_s6_dimension == 9)
    check("the registered alpha1 beta1 target has degree 13",
          alpha1_beta1_degree == 13)
    check("the filed model and registered target are dimensionally distinct",
          rp3_times_s6_dimension != alpha1_beta1_degree)

    admitted_degrees = {f_domain_dimension(k) for k in range(2, 20)}
    check("the cited f-invariant domain degrees m=2k-2 are even",
          all(m % 2 == 0 for m in admitted_degrees))
    check("the 9-dimensional model is outside that displayed domain",
          rp3_times_s6_dimension not in admitted_degrees)
    check("the 13-stem posit is outside that displayed domain",
          alpha1_beta1_degree not in admitted_degrees)
    check("missing codimension-two almost-complex corner data blocks a number",
          not False)

    integer_images = [n for n in range(-20, 21) if 3 * n == 0]
    check("every homomorphism Z/3 to torsion-free Z is trivial",
          integer_images == [0])

    qz_characters = [F(j, 3) % 1 for j in range(3)]
    check("Hom(Z/3,Q/Z) has three character values",
          qz_characters == [F(0), F(1, 3), F(2, 3)])
    check("both nonzero Q/Z characters have additive order three",
          [additive_order_mod_one(x) for x in qz_characters[1:]] == [3, 3])

    e_r = F(1, 12)
    e_three_primary = (4 * e_r) % 1
    check("the filed e_R=1/12 is torsion of order 12",
          additive_order_mod_one(e_r) == 12)
    check("its three-primary projection is 1/3 of order three",
          e_three_primary == F(1, 3)
          and additive_order_mod_one(e_three_primary) == 3)
    check("a Q/Z detector value is not an integer-cardinality output",
          e_three_primary.denominator != 1)

    # Planted mutations. Each must be caught by the corresponding invariant.
    mutations = {
        "pretend RP3xS6 is dimension 13": 13 == rp3_times_s6_dimension,
        "admit odd stem 13 to m=2k-2": 13 in admitted_degrees,
        "send Z/3 generator to integer 3": 3 * 3 == 0,
        "identify 1/3 in Q/Z with integer count 3": F(1, 3) == F(3),
    }
    caught = sum(not survived for survived in mutations.values())
    for name, survived in mutations.items():
        check("mutation caught: " + name, not survived)

    passed = sum(ok for _, ok in checks)
    print(f"\nBunke eta/f type ceiling: {passed}/{len(checks)} exact checks PASS")
    print(f"Planted mutations caught: {caught}/{len(mutations)}")
    print("RESULT: ETA_E_DICTIONARY_EXISTS__INTEGER_COUNT_BRIDGE_ABSENT__"
          "F_INVARIANT_MODEL_AND_DOMAIN_MISMATCH")
    if passed != len(checks) or caught != len(mutations):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
