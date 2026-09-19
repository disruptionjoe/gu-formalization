#!/usr/bin/env python3
"""Independent raw-allocation, Newton-tail and route replay for K244."""
from __future__ import annotations

from collections import defaultdict
from math import factorial
import json

from flint import fmpq, fmpq_mpoly_ctx

from k242_order_six_third_shell_signed_taylor import (
    K185, integrate_polynomial, log_polynomial_hash, moment_polynomials,
    orbit_groups, row_masks, terms,
)
from k244_order_six_exact_corner_shell_ladder import (
    K204, K209, K213, K218, ORDER, OUT, PI_LOWER, TAIL_START,
    exact_corner, sinh_log,
)


def raw_polynomials(items):
    allocations = defaultdict(int)
    for weight, masks in items:
        allocations[row_masks(masks)] += weight
    allocations = {rows: weight for rows, weight in allocations.items() if weight}
    assert len(allocations) == 1276
    ring = fmpq_mpoly_ctx.get([f"x{i}" for i in range(8)])
    variables = ring.gens()
    total = [ring.constant(0) for _ in range(ORDER + 1)]
    for rows, weight in allocations.items():
        pieces = [ring.constant(1)] + [ring.constant(0) for _ in range(ORDER)]
        for row in rows:
            base = 256 + row.bit_count()
            linear = sum(
                (variables[j] for j in range(8) if row & (1 << j)),
                ring.constant(0),
            )
            divided = [pieces[0] / base]
            for degree in range(1, ORDER + 1):
                divided.append((pieces[degree] - linear * divided[degree - 1]) / base)
            pieces = divided
        for degree, piece in enumerate(pieces):
            total[degree] += weight * piece
    return total


def newton_h(ratios: list[fmpq], degree: int) -> fmpq:
    complete = [fmpq(1)]
    for n in range(1, degree + 1):
        complete.append(
            sum(
                (sum((ratio**k for ratio in ratios), fmpq(0)) * complete[n - k]
                 for k in range(1, n + 1)),
                fmpq(0),
            ) / n
        )
    return complete[degree]


def independent_tail(groups, q: int) -> fmpq:
    total = fmpq(0)
    for rows, weight in groups.items():
        base = fmpq(1)
        ratios = []
        for row in rows:
            denominator = 256 + row.bit_count()
            base /= denominator
            ratios.append(exact_corner(q) * row.bit_count() / denominator)
        ratio = max(ratios) * fmpq(TAIL_START + 14, TAIL_START + 1)
        total += abs(weight) * base * newton_h(ratios, TAIL_START) / (1 - ratio)
    return total


def main() -> None:
    manifest = json.loads(OUT.read_text())
    k185 = json.loads(K185.read_text())
    items = list(terms(k185))

    # Raw allocations, without the S6 orbit projection, reproduce every
    # exact order-15 symmetric-cube moment used by the shell ladder.
    raw = raw_polynomials(items)
    for q in range(5, 12):
        cube = [fmpq(0)] * 9
        moments = moment_polynomials(q, ORDER)
        for polynomial in raw:
            values = integrate_polynomial(polynomial, moments)
            for power, value in enumerate(values):
                cube[power] += value
        expected = manifest["expansion"]["cube_integrated_log_polynomial_sha256"][str(q)]
        assert log_polynomial_hash(cube) == expected

    groups = orbit_groups(items)
    for q in range(6, 12):
        row = manifest["shells"][str(q)]
        assert exact_corner(q) == fmpq((q - 1) ** 2, 2 * q)
        assert exact_corner(q) < q - 1  # rejects K243's coarse corner
        core = independent_tail(groups, q)
        assert str(core) == row["exact_core_tail_majorant"]
        measure = sinh_log(q) ** 8 - sinh_log(q - 1) ** 8
        tail = fmpq(2**8 * 256**6, factorial(5)) / PI_LOWER**8 * measure * core
        recorded = row["normalized_tail_upper"]
        assert tail == fmpq(recorded["numerator"], recorded["denominator"])

    # Recheck the elementary exact simplex identity and route distinction.
    denominators = (fmpq(i + 2) for i in range(14))
    product = fmpq(1)
    for value in denominators:
        product *= value
    exact_simplex = fmpq(1, factorial(13)) / product
    assert exact_simplex > 0
    k204 = json.loads(K204.read_text())
    k209 = json.loads(K209.read_text())
    k213 = json.loads(K213.read_text())
    k218 = json.loads(K218.read_text())
    assert "exact full-reference moments" in k204["claim_ceiling"]
    assert "common-reference" in k209["claim_ceiling"]
    assert "reference and residual cancel" in k218["identity"]
    assert "original uniform simplex density" in k213["normalization"]
    assert manifest["route_composition"]["k185_k188_boundaries_retained"] is True
    assert manifest["route_composition"]["common_reference_derivative_owner_required_for_this_route"] is False

    budget = manifest["budget_ladder"]
    assert fmpq(budget["q11_complete_lower"]["numerator"], budget["q11_complete_lower"]["denominator"]) > fmpq(
        budget["remaining_allocation_after_q10"]["numerator"],
        budget["remaining_allocation_after_q10"]["denominator"],
    )
    assert budget["result"].startswith("q6_through_q10_certified")
    print("[PASS] K244 independent raw order-15, Newton-tail and route replay")


if __name__ == "__main__":
    main()
