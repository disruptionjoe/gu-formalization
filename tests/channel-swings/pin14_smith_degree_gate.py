#!/usr/bin/env python3
"""Degree/bookkeeping gate for the Pin+_14 Smith reduction.

This is not a bordism engine.  It protects the exact-sequence shifts and the
strength of the conclusion drawn from the cited primary inputs:

  MTSpin -> MTPin+ -> Sigma(MTSpin smash (BZ/2)_+),
  MTSpin smash BZ/2 ~= Sigma MTPin-,
  Omega^Spin_13 = Omega^Spin_14 = 0,
  exponent(Omega^Pin-_12) = 2,
  Kirby--Taylor A(14) = 1 and higher-order Pin+ summands occur only in
  dimensions congruent to 0 mod 4.

The exponent input is the degree-12 specialization of
Anderson--Brown--Peterson's Pin theorem.  The last two inputs are the direct
Pin+ table on p. 446 of Kirby--Taylor (1990).  Exit 0 certifies only the
degree/table deduction, not the source theorems.
"""
from __future__ import annotations


def check(label: str, condition: bool, detail: str) -> None:
    print(f"[{'PASS' if condition else 'FAIL'}] {label}: {detail}")
    if not condition:
        raise AssertionError(label)


target_degree = 14
spin_left = 0       # Omega^Spin_14
spin_right = 0      # Omega^Spin_13
smith_bz_degree = target_degree - 1
pin_minus_degree = smith_bz_degree - 1
abp_exponent = 2 if pin_minus_degree % 8 in {0, 1, 3, 4, 5, 7} else None
kirby_taylor_a14 = 1
kirby_taylor_has_higher_order_summands = target_degree % 4 == 0

print("=" * 79)
print("PIN+_14 SMITH DEGREE GATE")
print("=" * 79)

check("S1 vanishing endpoints", spin_left == 0 and spin_right == 0,
      "Omega^Spin_14 = Omega^Spin_13 = 0")
check("S2 LES target degree", smith_bz_degree == 13,
      "Omega^Pin+_14 is isomorphic to Omega^Spin_13((BZ/2)_+)")
check("S3 basepoint summand vanishes", spin_right == 0,
      "only reduced Spin bordism of BZ/2 remains")
check("S4 reduced Smith suspension shift", pin_minus_degree == 12,
      "reduced Omega^Spin_13(BZ/2) = Omega^Pin-_12")
check("S5 ABP exponent residue", abp_exponent == 2,
      "12 = 4 mod 8, so the degree-12 Pin- group has exponent 2")
check("S6 Kirby--Taylor rank", kirby_taylor_a14 == 1,
      "A(14) = 1 gives exactly one Z/2 summand")
check("S7 no higher-order summands", not kirby_taylor_has_higher_order_summands,
      "14 is not 0 mod 4, so the table's other summands are absent")

print("\nVERDICT: PIN14-EXACT-Z2")
print("  Omega^Pin+_14 ~= Omega^Pin-_12 ~= Z/2.")
print("  This closes the ambient group, not the construction or nontriviality")
print("  of GU's proposed class in it.")
