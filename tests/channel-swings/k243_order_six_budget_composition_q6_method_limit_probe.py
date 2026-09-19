#!/usr/bin/env python3
"""Independent raw-allocation, boundary-source and Newton-tail replay for K243."""
from __future__ import annotations

from fractions import Fraction as Q
from math import factorial
import json

from flint import fmpq

from k242_order_six_third_shell_signed_taylor import (
    K185,
    TAIL_START,
    integrate_polynomial,
    log_polynomial_hash,
    moment_polynomials,
    orbit_groups,
    terms,
)
from k242_order_six_third_shell_signed_taylor_probe import raw_polynomials
from k243_order_six_budget_composition_q6_method_limit import (
    FULL_BUDGET,
    K188,
    K204,
    K209,
    K224,
    K242,
    OUT,
    PI_LOWER,
    Q6_POLYNOMIAL_UPPER,
    row_fraction,
)


def newton_h(ratios: list[fmpq], degree: int) -> fmpq:
    complete = [fmpq(1)]
    for n in range(1, degree + 1):
        complete.append(
            sum(
                (sum((ratio**k for ratio in ratios), fmpq(0)) * complete[n-k]
                 for k in range(1, n+1)),
                fmpq(0),
            ) / n
        )
    return complete[degree]


def independent_tail(groups, x_max: int) -> fmpq:
    total = fmpq(0)
    for rows, weight in groups.items():
        base = fmpq(1)
        ratios = []
        for row in rows:
            denominator = 256 + row.bit_count()
            base /= denominator
            ratios.append(fmpq(x_max * row.bit_count(), denominator))
        ratio = max(ratios) * fmpq(TAIL_START + 14, TAIL_START + 1)
        total += abs(weight) * base * newton_h(ratios, TAIL_START) / (1-ratio)
    return total


def main() -> None:
    manifest = json.loads(OUT.read_text())
    k185 = json.loads(K185.read_text())
    k188 = json.loads(K188.read_text())
    k224 = json.loads(K224.read_text())
    k242 = json.loads(K242.read_text())

    # Rebuild every K188 boundary row from its K185 sources rather than trust
    # the recorded combined rows.
    small_fraction = row_fraction(
        k188["small_radius_certificate"]["normalized_lower_tail_fraction_ceiling"]
    )
    boundary = fmpq(0)
    for group_id, source in k185["groups"].items():
        bounds = source["proof_safe_bounds"]
        whole = row_fraction(bounds["whole_group_global_ceiling"])
        face = row_fraction(bounds["any_simplex_coordinate_below_2^-180_group_ceiling"])
        tail = row_fraction(bounds["rho_greater_than_one_quarter_group_ceiling"])
        rebuilt = whole * small_fraction + face + tail
        recorded = row_fraction(
            k188["complete_group_propagation"]["groups"][group_id]["combined_known_boundary_group_ceiling"]
        )
        assert rebuilt == recorded
        boundary += rebuilt
    recorded_budget = manifest["known_budget_composition"]
    assert boundary == row_fraction(recorded_budget["k185_k188_boundary_union"])

    cube_q4 = fmpq(k224["combined_inner_first_second_cube_absolute_upper"])
    shell_q45 = fmpq(k242["complete_third_shell"]["absolute_upper"])
    remaining = FULL_BUDGET - boundary - cube_q4 - shell_q45
    assert remaining == row_fraction(
        recorded_budget["remaining_for_q_greater_than_5_and_unallocated_defects"]
    )

    # Raw allocations, not S6 orbit representatives, independently reproduce
    # both exact symmetric-cube log polynomials.
    items = list(terms(k185))
    raw = raw_polynomials(items)
    for q in (5, 6):
        cube = [fmpq(0)] * 9
        moments = moment_polynomials(q)
        for polynomial in raw:
            values = integrate_polynomial(polynomial, moments)
            for power, value in enumerate(values):
                cube[power] += value
        expected = manifest["q5_to_q6_signed_degree_zero_through_nine"]["cube_integrated_log_polynomial_sha256"][str(q)]
        assert log_polynomial_hash(cube) == expected

    groups = orbit_groups(items)
    tail_core = independent_tail(groups, 5)
    shell = manifest["q5_to_q6_inherited_orbit_tail"]
    assert str(tail_core) == shell["exact_core_majorant"]
    measure = fmpq(shell["exact_shell_measure"])
    tail = fmpq(2**8 * 256**6, factorial(5)) / PI_LOWER**8 * measure * tail_core
    assert tail == row_fraction(shell["normalized_upper"])

    # Hostile interpretations: the signed polynomial alone would pass, but the
    # complete unchanged method fails; omitting boundaries inflates the budget;
    # and K204/K209 explicitly withhold the derivative needed for an error addend.
    assert Q6_POLYNOMIAL_UPPER < remaining < tail
    omitted_boundary_remaining = FULL_BUDGET - cube_q4 - shell_q45
    assert omitted_boundary_remaining > remaining
    assert "no complete signed quotient derivative" in json.loads(K204.read_text())["claim_ceiling"]
    assert "no complete signed quotient error" in json.loads(K209.read_text())["claim_ceiling"]
    assert shell["result"] == "fails_composed_remaining_budget"
    print("[PASS] K243 independent boundary, raw-allocation and Newton-tail replay")


if __name__ == "__main__":
    main()
