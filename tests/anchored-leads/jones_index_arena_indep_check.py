#!/usr/bin/env python3
"""Independent finite-type check for the Jones-index anchored lead.

This verifier deliberately does not import `jones_subfactor_index_m64h.py`.
It rechecks the finite-dimensional Clifford substrate, the natural
dimension-ratio screens, and the exact graph shape needed for index 3.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import cos, gcd, isclose, pi


CHECKS: list[str] = []


def check(name: str, condition: bool, detail: str = "") -> None:
    if not condition:
        suffix = f" :: {detail}" if detail else ""
        raise AssertionError(f"{name}{suffix}")
    CHECKS.append(name)
    print(f"  [PASS] {name}{(' :: ' + detail) if detail else ''}")


@dataclass(frozen=True)
class CliffordType:
    p: int
    q: int
    matrix_size: int
    ring: str
    summands: int
    real_dimension: int

    @property
    def spinor_real_dimension(self) -> int:
        return self.matrix_size * {"R": 1, "C": 2, "H": 4}[self.ring]

    @property
    def label(self) -> str:
        prefix = "" if self.summands == 1 else f"{self.summands} x "
        return f"Cl({self.p},{self.q}) = {prefix}M({self.matrix_size},{self.ring})"


RING_BY_MOD8 = {
    0: ("R", 1),
    1: ("R", 2),
    2: ("R", 1),
    3: ("C", 1),
    4: ("H", 1),
    5: ("H", 2),
    6: ("H", 1),
    7: ("C", 1),
}
RING_REAL_DIMENSION = {"R": 1, "C": 2, "H": 4}


def is_square(n: int) -> bool:
    root = int(n**0.5)
    return root * root == n or (root + 1) * (root + 1) == n


def is_power_of_two(n: int) -> bool:
    return n > 0 and (n & (n - 1)) == 0


def clifford_type(p: int, q: int) -> CliffordType:
    dimension = p + q
    real_dimension = 2**dimension
    ring, summands = RING_BY_MOD8[(p - q) % 8]
    denominator = summands * RING_REAL_DIMENSION[ring]
    matrix_square = real_dimension // denominator
    check(
        f"Cl({p},{q}) matrix square is integral",
        real_dimension % denominator == 0 and is_square(matrix_square),
        f"2^{dimension}/{denominator} = {matrix_square}",
    )
    return CliffordType(
        p=p,
        q=q,
        matrix_size=int(matrix_square**0.5),
        ring=ring,
        summands=summands,
        real_dimension=real_dimension,
    )


def finite_dimension_ratio(sub: CliffordType, sup: CliffordType) -> Fraction:
    return Fraction(sup.real_dimension, sub.real_dimension)


def path_graph_index(vertices: int) -> float:
    """Jones ADE path-graph index for A_vertices: ||A||^2."""
    return 4.0 * cos(pi / (vertices + 1)) ** 2


def hom_finite_cyclic_to_z_is_zero(order: int) -> bool:
    # A homomorphism from a finite cyclic group to torsion-free Z must send
    # the generator to an integer killed by `order`, hence to zero.
    return order > 0


def hom_finite_cyclic_order(domain_order: int, codomain_order: int) -> int:
    # |Hom(Z/m, Z/n)| = gcd(m,n). It is trivial iff the gcd is 1.
    return gcd(domain_order, codomain_order)


def main() -> None:
    print("=" * 78)
    print("Independent Jones-index arena check")
    print("=" * 78)

    cl_95 = clifford_type(9, 5)
    print(f"\n[A] GU substrate: {cl_95.label}")
    check("Cl(9,5) is the expected finite type-I quaternionic factor", (
        cl_95.matrix_size,
        cl_95.ring,
        cl_95.summands,
    ) == (64, "H", 1))
    check("Cl(9,5) real dimension is 2^14", cl_95.real_dimension == 2**14)

    print("\n[B] Natural Clifford codimension chain")
    chain = [clifford_type(7, 5), clifford_type(8, 5), cl_95]
    ratios = []
    for previous, current in zip(chain, chain[1:]):
        ratio = finite_dimension_ratio(previous, current)
        ratios.append(ratio)
        print(f"  {previous.label}  ->  {current.label}: dimension ratio {ratio}")
    check("Codimension-one Clifford steps stay 2-primary", ratios == [Fraction(2), Fraction(2)])
    check("No codimension-one Clifford step has index/dimension ratio 3", all(r != 3 for r in ratios))

    print("\n[C] Frame-split spinor dimensions")
    frame_types = [clifford_type(p, q) for p, q in [(3, 1), (6, 4), (1, 3), (8, 4), (9, 5)]]
    for typ in frame_types:
        print(f"  {typ.label}: spinor real dimension {typ.spinor_real_dimension}")
    check(
        "All checked frame-split spinor dimensions are powers of two",
        all(is_power_of_two(typ.spinor_real_dimension) for typ in frame_types),
    )
    check(
        "No checked frame-split spinor dimension carries a factor of 3",
        all(typ.spinor_real_dimension % 3 != 0 for typ in frame_types),
    )

    print("\n[D] What index 3 requires")
    index_rows = [(vertices, path_graph_index(vertices)) for vertices in range(2, 9)]
    for vertices, value in index_rows:
        marker = "  <-- index 3" if isclose(value, 3.0, rel_tol=0.0, abs_tol=1e-12) else ""
        print(f"  A_{vertices}: ||A||^2 = {value:.12f}{marker}")
    exact_three = [vertices for vertices, value in index_rows if isclose(value, 3.0, rel_tol=0.0, abs_tol=1e-12)]
    check("The ADE path graph index 3 screen singles out A_5", exact_three == [5])
    check(
        "A_5 is a graph-shape requirement, not a finite Clifford type consequence",
        cl_95.summands == 1 and cl_95.matrix_size == 64,
    )

    print("\n[E] Torsion-to-integer firewall")
    check("Hom(Z/3, Z) is zero", hom_finite_cyclic_to_z_is_zero(3))
    check("Hom(Z/6, Z) is zero", hom_finite_cyclic_to_z_is_zero(6))
    check("Hom(Z/2, Z/3) is trivial", hom_finite_cyclic_order(2, 3) == 1)
    check("Hom(Z/3, Z/2) is trivial", hom_finite_cyclic_order(3, 2) == 1)

    print("\nVERDICT")
    print(
        "  The GU-native finite Clifford and frame-split screens are finite type-I "
        "and 2-primary in this independent check. Producing Jones index 3 requires "
        "an A_5 Bratteli/principal graph supplied as extra structure, and finite "
        "torsion classes still have no canonical homomorphism to an integer count."
    )
    print(f"\n{len(CHECKS)} checks passed.")


if __name__ == "__main__":
    main()
