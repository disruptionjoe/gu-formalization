#!/usr/bin/env python3
"""Sp(1) 2-primary Dai-Freed gate validator.

This is a front-page AHSS gate for the open global-anomaly lane. It checks the
untwisted spin AHSS line for Omega^Spin_15(BSp(1)), the Dai-Freed degree of a
14-dimensional fermionic theory.

Scope:
- It is not a full bordism-package computation.
- It does not claim anomaly cancellation.
- It does not decide the physical fermion content.
- It verifies whether the cheap Sp(1) 2-primary target has a visible E2 entry
  before any eta pairing is attempted.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import comb


ASSERTS = 0


def check(condition: bool, message: str) -> None:
    global ASSERTS
    ASSERTS += 1
    assert condition, message


@dataclass(frozen=True)
class SpinBordismTerm:
    free_rank: int
    torsion_orders: tuple[int, ...] = ()


# Standard low-degree spin-bordism table through the GU Dai-Freed degree.
OMEGA_SPIN: dict[int, SpinBordismTerm] = {
    0: SpinBordismTerm(1),
    1: SpinBordismTerm(0, (2,)),
    2: SpinBordismTerm(0, (2,)),
    3: SpinBordismTerm(0),
    4: SpinBordismTerm(1),
    5: SpinBordismTerm(0),
    6: SpinBordismTerm(0),
    7: SpinBordismTerm(0),
    8: SpinBordismTerm(2),
    9: SpinBordismTerm(0, (2, 2)),
    10: SpinBordismTerm(0, (2, 2, 2)),
    11: SpinBordismTerm(0),
    12: SpinBordismTerm(3),
    13: SpinBordismTerm(0),
    14: SpinBordismTerm(0),
    15: SpinBordismTerm(0),
}


def poincare_ranks(generator_degrees: list[int], max_degree: int) -> list[int]:
    """Ranks for a polynomial homology/cohomology ring with given generator degrees."""
    ranks = [0] * (max_degree + 1)
    ranks[0] = 1
    for degree in generator_degrees:
        next_ranks = [0] * (max_degree + 1)
        for total in range(max_degree + 1):
            copies = 0
            while total - copies * degree >= 0:
                next_ranks[total] += ranks[total - copies * degree]
                copies += 1
        ranks = next_ranks
    return ranks


def bsp_homology_ranks(rank_n: int, max_degree: int) -> list[int]:
    """H_*(BSp(n); Z) is torsion-free on polynomial generators in degrees 4,8,...,4n."""
    return poincare_ranks([4 * k for k in range(1, rank_n + 1)], max_degree)


def ahss_e2_line_for_bsp(rank_n: int, total_degree: int) -> list[dict[str, object]]:
    """E2 entries H_i(BSp(n); Omega^Spin_j(pt)) for i+j=total_degree.

    H_*(BSp(n); Z) is free, so tensoring with Omega^Spin_j simply repeats the
    free and torsion pieces by the homology rank.
    """
    h_ranks = bsp_homology_ranks(rank_n, total_degree)
    entries: list[dict[str, object]] = []
    for i in range(total_degree + 1):
        h_rank = h_ranks[i]
        if h_rank == 0:
            continue
        j = total_degree - i
        omega = OMEGA_SPIN.get(j, SpinBordismTerm(0))
        free_rank = h_rank * omega.free_rank
        torsion = tuple(order for order in omega.torsion_orders for _ in range(h_rank))
        if free_rank or torsion:
            entries.append(
                {
                    "i": i,
                    "j": j,
                    "h_rank": h_rank,
                    "free_rank": free_rank,
                    "torsion": torsion,
                }
            )
    return entries


def total_torsion(entries: list[dict[str, object]]) -> list[int]:
    torsion: list[int] = []
    for entry in entries:
        torsion.extend(entry["torsion"])  # type: ignore[arg-type]
    return torsion


def summarize_entries(entries: list[dict[str, object]]) -> str:
    if not entries:
        return "ALL ZERO"
    parts = []
    for entry in entries:
        torsion = entry["torsion"]
        torsion_label = "+".join(f"Z/{order}" for order in torsion) if torsion else "0"
        parts.append(
            f"(i={entry['i']}, j={entry['j']}, Hrank={entry['h_rank']}, "
            f"free={entry['free_rank']}, torsion={torsion_label})"
        )
    return "; ".join(parts)


def local_i16_gravity_coefficient(net_chirality: int) -> Fraction:
    """Pure gravitational p4 coefficient for the assumed 14D truncation."""
    dim_spinor = 64
    ahat_p4_coeff = Fraction(-1, 2_419_200)
    return dim_spinor * net_chirality * ahat_p4_coeff


def main() -> None:
    print("=" * 88)
    print("SP(1) 2-PRIMARY DAI-FREED GATE VALIDATOR")
    print("=" * 88)

    dai_freed_degree = 14 + 1
    check(dai_freed_degree == 15, "GU 14D Dai-Freed degree must be 15")

    print("\nInput: Omega^Spin_*(pt), low-degree table through 15")
    for degree, term in OMEGA_SPIN.items():
        for order in term.torsion_orders:
            check(order > 1 and order & (order - 1) == 0, f"torsion at {degree} must be 2-primary")
        label = f"Z^{term.free_rank}"
        if term.torsion_orders:
            label += " + " + "+".join(f"Z/{order}" for order in term.torsion_orders)
        print(f"  Omega^Spin_{degree:2d}: {label}")

    print("\nInput: H_*(BSp(1); Z) support")
    h_sp1 = bsp_homology_ranks(1, dai_freed_degree)
    supported = [i for i, rank in enumerate(h_sp1) if rank]
    print(f"  nonzero ranks through degree {dai_freed_degree}: {supported}")
    check(supported == [0, 4, 8, 12], "BSp(1) support through 15 must be 0,4,8,12")
    check(all(i % 4 == 0 for i in supported), "BSp(1) homology support must be divisible by 4")

    print("\nGate: total degree 15, BSp(1)")
    line15_sp1 = ahss_e2_line_for_bsp(1, dai_freed_degree)
    print(f"  {summarize_entries(line15_sp1)}")
    check(line15_sp1 == [], "untwisted BSp(1) total-degree-15 E2 line must be empty")

    print("\nControl: total degree 5, BSp(1), Witten-style 2-primary entry")
    line5_sp1 = ahss_e2_line_for_bsp(1, 5)
    print(f"  {summarize_entries(line5_sp1)}")
    check(total_torsion(line5_sp1) == [2], "BSp(1) degree 5 must expose a Z/2 control")

    print("\nControl: total degree 9, BSp(1), higher 2-primary entries")
    line9_sp1 = ahss_e2_line_for_bsp(1, 9)
    print(f"  {summarize_entries(line9_sp1)}")
    check(total_torsion(line9_sp1) == [2, 2, 2], "BSp(1) degree 9 must expose three Z/2 controls")

    print("\nNaive-rank control: total degree 15, BSp(32)")
    line15_sp32 = ahss_e2_line_for_bsp(32, dai_freed_degree)
    print(f"  {summarize_entries(line15_sp32)}")
    check(line15_sp32 == [], "BSp(32) total-degree-15 E2 line must also be empty")

    print("\nLocal I_16 boundary check, assumed truncated content")
    rank_0 = comb(14, 0)
    rank_1 = comb(14, 1)
    net_chirality = rank_0 - rank_1
    grav_coeff = local_i16_gravity_coefficient(net_chirality)
    balanced_coeff = local_i16_gravity_coefficient(0)
    print(f"  assumed net chirality: {rank_0} - {rank_1} = {net_chirality}")
    print(f"  gravitational p4 coefficient: {grav_coeff}")
    print(f"  chirally balanced control coefficient: {balanced_coeff}")
    check(net_chirality == -13, "assumed Omega^0/Omega^1 truncation should have net chirality -13")
    check(grav_coeff != 0, "assumed truncation keeps local gravitational I_16 channel nonzero")
    check(balanced_coeff == 0, "balanced content must remove this local gravitational channel")

    print("\nVerdict:")
    print("  Untwisted BSp(1) has no total-degree-15 E2 entry in this gate.")
    print("  The validator is non-vacuous: it detects BSp(1) 2-primary entries in degrees 5 and 9.")
    print("  This is a gate, not an anomaly-cancellation verdict; twists, physical content, and local I_16 remain separate.")
    print(f"  hard asserts passed: {ASSERTS}")


if __name__ == "__main__":
    main()
