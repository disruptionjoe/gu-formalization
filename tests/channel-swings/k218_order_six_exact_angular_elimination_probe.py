#!/usr/bin/env python3
"""Independent finite-degree and signed assembly controls for K218."""
from __future__ import annotations

from collections import Counter
from fractions import Fraction as Q
from itertools import combinations_with_replacement
import json
from math import comb, factorial
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
P = ROOT / "lab/process"


def dirichlet_moment(indices: tuple[int, ...]) -> Q:
    counts = Counter(indices)
    result = Q(factorial(13), factorial(13 + len(indices)))
    for count in counts.values():
        result *= factorial(count)
    return result


def independent_series(u: tuple[Q, ...], order: int) -> list[Q]:
    """Binomial expansion integrated by original simplex factorial moments."""
    out = [Q(1)]
    for n in range(1, order + 1):
        moment = Q(0)
        for indices in combinations_with_replacement(range(14), n):
            multiplicity = Q(factorial(n))
            for count in Counter(indices).values():
                multiplicity /= factorial(count)
            product = Q(1)
            for i in indices:
                product *= u[i]
            moment += multiplicity * product * dirichlet_moment(indices)
        rising = Q(1)
        for k in range(n):
            rising *= 14 + k
        out.append(moment * rising / factorial(n))
    return out


def direct_product_series(u: tuple[Q, ...], order: int) -> list[Q]:
    coefficients = [Q(1)] + [Q(0)] * order
    for value in u:
        next_coefficients = [Q(0)] * (order + 1)
        for n, old in enumerate(coefficients):
            for k in range(order + 1 - n):
                next_coefficients[n + k] += old * value**k
        coefficients = next_coefficients
    return coefficients


def independent_signed_point(source: dict, coshes: tuple[Q, ...]) -> Q:
    catalog = source["exact_allocation_certificate"]["allocation_catalog"]
    total = Q(0)
    for entry in source["complete_face_hypergraph"]["entries"]:
        for term in entry["terms"]:
            masks = [int(m, 16) for m in catalog[term["allocation_id"]]["support_masks_hex"].split(",")]
            denominator = Q(1)
            for i in range(14):
                denominator *= 256 + sum((coshes[j] for j, mask in enumerate(masks)
                                          if mask & (1 << i)), Q(0))
            total += (term["leibniz_sign"] * entry["coefficient_product"]
                      * (2 if entry["left"] != entry["right"] else 1) / denominator)
    product = Q(1)
    for c in coshes:
        product *= c
    return total * 2**8 * 256**6 * product / factorial(5)


def main() -> None:
    manifest = json.loads((P / "k218-order-six-exact-angular-elimination.json").read_text())
    source = json.loads((P / "k185-order-six-duffy-face-tail-wave.json").read_text())
    u = tuple(Q(i % 5, 31) for i in range(14))
    lhs = independent_series(u, 4)
    rhs = direct_product_series(u, 4)
    assert lhs == rhs
    assert lhs[1] != Q(13, 14) * sum(u)  # exponent-13 plant
    # One exceptional denominator: integrate the Beta(1,13) density directly
    # after y=b+(a-b)z, expanding (a-y)^12; no Feynman identity is used.
    b, a = Q(7), Q(11)
    beta_direct = Q(13, (a-b)**13) * sum(
        (Q(comb(12, k) * (-1)**k) * a**(12-k)
         * (a**(k-13)-b**(k-13)) / (k-13))
        for k in range(13))
    assert beta_direct == Q(1, a * b**13)
    beta_coefficients = [Q(0)] * 5
    for n in range(5):
        beta_coefficients[n] = Q(1)
        for k in range(n):
            beta_coefficients[n] *= Q(1 + k, 14 + k)
        beta_coefficients[n] *= Q(factorial(13 + n), factorial(13) * factorial(n))
    assert beta_coefficients == [Q(1)] * 5  # (1-u z_0)^-14 -> (1-u)^-1
    assert beta_direct != Q(1, b**14)  # omitted exceptional load plant
    points = {
        "all_t_zero": (Q(1),) * 8,
        "all_t_log2": (Q(5, 4),) * 8,
        "alternating_zero_log2": tuple(Q(1) if j % 2 == 0 else Q(5, 4) for j in range(8)),
    }
    for name, c in points.items():
        assert str(independent_signed_point(source, c)) == manifest["exact_signed_point_rational_without_pi8"][name]
    assert manifest["ordered_terms_after_off_diagonal_doubling"] == 2928
    print("[PASS] independent Dirichlet/Beta coefficients, signed assembly and hostile controls")


if __name__ == "__main__":
    main()
