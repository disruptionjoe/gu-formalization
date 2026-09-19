#!/usr/bin/env python3
"""Independent orbit, Taylor, Newton-tail, and full-domain route replay for K245."""
from __future__ import annotations

from collections import defaultdict
from math import factorial
import json

from flint import fmpq, fmpq_mpoly_ctx

from k230_order_six_permutation_projection_probe import canonical, raw_entries
from k242_order_six_third_shell_signed_taylor import coefficient_hash
from k243_order_six_budget_composition_q6_method_limit import K188, PI_LOWER
from k244_order_six_exact_corner_shell_ladder import K213, K218, exact_corner, sinh_log
from k245_order_six_full_domain_route_shell_ladder import ORDER, OUT, TAIL_START


def independent_groups(items):
    groups = defaultdict(int)
    for weight, masks in items:
        groups[canonical(masks)] += weight
    return {rows: weight for rows, weight in groups.items() if weight}


def independent_polynomials(groups):
    """Rebuild the reciprocal-factor series from the independent raw orbit map."""
    ring = fmpq_mpoly_ctx.get([f"x{i}" for i in range(8)])
    variables = ring.gens()
    total = [ring.constant(0) for _ in range(ORDER + 1)]
    for rows, weight in groups.items():
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
    items = list(raw_entries())
    assert len(items) == 1864
    groups = independent_groups(items)
    assert len(groups) == 307
    independent = independent_polynomials(groups)
    expected_coefficients = manifest["expansion"]["degree_coefficient_sha256"]
    for degree, polynomial in enumerate(independent):
        assert coefficient_hash(polynomial) == expected_coefficients[str(degree)]

    for q in range(11, 14):
        row = manifest["shells"][str(q)]
        core = independent_tail(groups, q)
        assert str(core) == row["exact_core_tail_majorant"]
        measure = sinh_log(q) ** 8 - sinh_log(q - 1) ** 8
        tail = fmpq(2**8 * 256**6, factorial(5)) / PI_LOWER**8 * measure * core
        recorded = row["normalized_tail_upper"]
        assert tail == fmpq(recorded["numerator"], recorded["denominator"])
        assert exact_corner(q) < q - 1

    # The alternative route explicitly excises three regions. K213/K218 do not:
    # they consume all original signed terms, the full Gamma radius, and the
    # original complete simplex. This is route composition, not a smaller face bound.
    k188 = json.loads(K188.read_text())
    k213 = json.loads(K213.read_text())
    k218 = json.loads(K218.read_text())
    assert len(k188["domain_cover"]["regions"]) == 4
    assert "no rho<=1/4 restriction" in k213["core_tail"]["scope"]
    assert k213["counts"]["leibniz_terms"] == k218["terms"] == 1864
    assert "original uniform 13-simplex" in k218["object"]
    route = manifest["route_composition"]
    assert route["k185_k188_boundary_union_charged_on_exact_route"] is False
    assert route["k185_k188_boundary_union_required_if_excised_quotient_route_revived"] is True

    budget = manifest["exact_route_budget"]
    remaining = fmpq(budget["remaining_after_q12"]["numerator"], budget["remaining_after_q12"]["denominator"])
    q13_lower = fmpq(budget["q13_complete_lower"]["numerator"], budget["q13_complete_lower"]["denominator"])
    assert q13_lower > remaining
    assert budget["counterfactual_with_k185_k188_double_count"]["q11_lower_exceeds_remaining"] is True
    assert budget["result"] == "q11_and_q12_certified__q13_exceeds_current_exact_route_allocation"
    print("[PASS] K245 independent raw-orbit order-17, Newton-tail, and full-domain route replay")


if __name__ == "__main__":
    main()
