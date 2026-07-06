#!/usr/bin/env python3
"""Independent check for the RS family generation-arena probe.

This re-derives the arithmetic behind
`tests/rs-function-space/family_generation_arena_probe.py` without importing it.
The check is intentionally narrow: all currently computed family/characteristic
numbers stay in the 2-primary arena, while the familiar `24 / 8 = 3` route is
kept visible as a forbidden target import rather than used as evidence.
"""
from __future__ import annotations

from fractions import Fraction


ASSERTS = 0


def check(condition: bool, message: str) -> None:
    global ASSERTS
    ASSERTS += 1
    assert condition, message


def z3_part(index_number: int) -> int:
    """Z/3 component of the reduced e-invariant numerator N in Z/24."""
    return (index_number % 24) % 3


def is_two_primary(index_number: int) -> bool:
    return z3_part(index_number) == 0


def rs_fiber_index(signature: int) -> Fraction:
    """Spin-3/2 / RS index on a spin 4-manifold: I_{3/2}=21*sigma/8."""
    return Fraction(21 * signature, 8)


def main() -> None:
    sigma_k3 = -16
    p1_tk3 = 3 * sigma_k3
    spinor_rank = 128
    spin_multiplier = spinor_rank // 8
    sym2_multiplier = 6

    bulk_rs = rs_fiber_index(sigma_k3)
    flat_twist_rank = 16
    flat_twisted_rs = flat_twist_rank * bulk_rs

    # Chern-Weil packet: p1(V)=p1(TK3)+p1(Sym^2)=7*p1(TK3), then multiply by dim(S)/8.
    p1_symmetric_square = sym2_multiplier * p1_tk3
    p1_v = p1_tk3 + p1_symmetric_square
    ch2_sx = spin_multiplier * p1_v
    ch2_sx_normalized = ch2_sx // 8
    aps_eta_step2 = 0

    honest_numbers = {
        "bulk I_3/2[K3]": int(bulk_rs),
        "flat rank-16 twist": int(flat_twisted_rs),
        "ch2(S_X)[K3]": ch2_sx,
        "ch2(S_X)[K3] / 8": ch2_sx_normalized,
        "RS boundary APS eta": aps_eta_step2,
    }

    print("=" * 84)
    print("Independent RS family generation-arena check")
    print("=" * 84)
    print(f"sigma(K3)={sigma_k3}; p1(TK3)=3*sigma={p1_tk3}")
    print(f"I_3/2[K3]=21*sigma/8={bulk_rs}")
    print(f"ch2(S_X)[K3]=(dim S/8)*(p1(TK3)+p1(Sym^2))")
    print(f"              ={spin_multiplier}*({p1_tk3}+{p1_symmetric_square})={ch2_sx}")
    print()

    for label, value in honest_numbers.items():
        arena = "2-primary" if is_two_primary(value) else "3-primary"
        print(f"  {label:<24} N={value:>6}  z3={z3_part(value)}  {arena}")
        check(is_two_primary(value), f"{label} unexpectedly reaches the Z/3 arena")

    chi_k3 = 24
    dead_count = chi_k3 // 8
    tangential_e_numerator = 2  # e_R=1/12=2/24, located but not a family index.
    external_flux_example = 1

    print()
    print("Controls and forbidden route")
    print(f"  forbidden chi(K3) import: chi={chi_k3}, chi/8={dead_count}")
    print(f"  tangential e_R numerator: N={tangential_e_numerator}, z3={z3_part(tangential_e_numerator)}")
    print(f"  external flux example:   N={external_flux_example}, z3={z3_part(external_flux_example)}")

    check(bulk_rs == -42, "bulk K3 RS index moved")
    check(flat_twisted_rs == -672, "flat twisted RS index moved")
    check(ch2_sx == -5376, "honest ch2(S_X)[K3] moved")
    check(ch2_sx_normalized == -672, "ch2 normalization moved")
    check(dead_count == 3, "forbidden chi/8 contrast should produce 3")
    check(ch2_sx != chi_k3, "honest ch2 must not collapse to chi(K3)")
    check(tangential_e_numerator not in honest_numbers.values(), "e_R control is not an internal family index")
    check(z3_part(tangential_e_numerator) != 0, "e_R control should detect the Z/3 arena")
    check(z3_part(external_flux_example) != 0, "external flux control should detect the Z/3 arena")

    print()
    print(f"[OK] independent arena check passed ({ASSERTS} asserts).")


if __name__ == "__main__":
    main()
