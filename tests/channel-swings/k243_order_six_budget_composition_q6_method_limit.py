#!/usr/bin/env python3
"""K243: compose the known order-six budget and test the q=6 shell method."""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
from hashlib import sha256
import json
from math import factorial

from flint import arb, fmpq

from k242_order_six_third_shell_signed_taylor import (
    K185,
    ROOT,
    TAIL_START,
    complete_homogeneous_ten,
    evaluate_log_polynomial,
    integrate_polynomial,
    log_polynomial_hash,
    moment_polynomials,
    orbit_groups,
    taylor_polynomials,
    terms,
)

K188 = ROOT / "lab/process/k188-order-six-small-rho-strip-wave.json"
K204 = ROOT / "lab/process/k204-order-six-core-moment-defect.json"
K209 = ROOT / "lab/process/k209-order-six-cubic-core-geometry.json"
K224 = ROOT / "lab/process/k224-order-six-second-shell-cost-stress.json"
K242 = ROOT / "lab/process/k242-order-six-third-shell-signed-taylor.json"
OUT = ROOT / "lab/process/k243-order-six-budget-composition-q6-method-limit.json"

FULL_BUDGET = fmpq(1, 10**21)
PI_LOWER = fmpq(31, 10)
Q6_POLYNOMIAL_LOWER = fmpq(12336, 10**30)
Q6_POLYNOMIAL_UPPER = fmpq(12337, 10**30)


def fraction_row(value: fmpq) -> dict[str, object]:
    q = Q(str(value))
    return {
        "numerator": q.numerator,
        "denominator": q.denominator,
        "decimal": f"{float(q):.12e}",
    }


def row_fraction(row: dict[str, object]) -> fmpq:
    return fmpq(int(row["numerator"]), int(row["denominator"]))


def boundary_union(k188: dict[str, object]) -> fmpq:
    groups = k188["complete_group_propagation"]["groups"]
    return sum(
        (row_fraction(row["combined_known_boundary_group_ceiling"])
         for row in groups.values()),
        fmpq(0),
    )


def generalized_tail_majorant(groups, x_max: int) -> tuple[fmpq, fmpq]:
    """K242's orbit tail with the cube corner c=1+x_max made explicit."""
    total = fmpq(0)
    maximum_ratio = fmpq(0)
    for rows, weight in groups.items():
        base_value = fmpq(1)
        ratios = []
        for row in rows:
            base = 256 + row.bit_count()
            base_value /= base
            ratios.append(fmpq(x_max * row.bit_count(), base))
        h10 = complete_homogeneous_ten(ratios)
        ratio_ceiling = max(ratios) * fmpq(TAIL_START + 14, TAIL_START + 1)
        assert ratio_ceiling < 1
        maximum_ratio = max(maximum_ratio, ratio_ceiling)
        total += abs(weight) * base_value * h10 / (1 - ratio_ceiling)
    return total, maximum_ratio


def generate() -> dict[str, object]:
    k188 = json.loads(K188.read_text())
    k224 = json.loads(K224.read_text())
    k242 = json.loads(K242.read_text())
    boundary = boundary_union(k188)
    cube_q4 = fmpq(k224["combined_inner_first_second_cube_absolute_upper"])
    shell_q45 = fmpq(k242["complete_third_shell"]["absolute_upper"])
    known_total = boundary + cube_q4 + shell_q45
    remaining = FULL_BUDGET - known_total
    assert remaining > 0

    items = list(terms(json.loads(K185.read_text())))
    assert len(items) == 1864
    groups = orbit_groups(items)
    assert len(groups) == 307
    polynomials = taylor_polynomials(groups)
    cube_coefficients: dict[int, list[fmpq]] = {}
    for q in (5, 6):
        moments = moment_polynomials(q)
        cube_coefficients[q] = [fmpq(0)] * 9
        for polynomial in polynomials:
            values = integrate_polynomial(polynomial, moments)
            for power, value in enumerate(values):
                cube_coefficients[q][power] += value

    normalization = arb(2**8 * 256**6) / factorial(5) / arb.pi()**8
    polynomial_shell = normalization * (
        evaluate_log_polynomial(cube_coefficients[6], 6)
        - evaluate_log_polynomial(cube_coefficients[5], 5)
    )
    assert polynomial_shell > arb(str(Q6_POLYNOMIAL_LOWER))
    assert polynomial_shell < arb(str(Q6_POLYNOMIAL_UPPER))

    tail_core, ratio_ceiling = generalized_tail_majorant(groups, 5)
    shell_measure = fmpq(35, 12)**8 - fmpq(12, 5)**8
    tail_upper = (
        fmpq(2**8 * 256**6, factorial(5)) / PI_LOWER**8
        * shell_measure * tail_core
    )
    method_upper = Q6_POLYNOMIAL_UPPER + tail_upper
    assert tail_upper > remaining

    return {
        "schema_version": "1.0",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "input_sha256": {
            path.stem.split("-")[0]: sha256(path.read_bytes()).hexdigest()
            for path in (K185, K188, K204, K209, K224, K242)
        },
        "object": (
            "One outward order-six 1e-21 budget composed from the K185/K188 "
            "boundary union, K224 q<=4 core and K242 q=4-to-q=5 core shell; "
            "plus the unchanged K242 certificate class on q=5-to-q=6"
        ),
        "known_budget_composition": {
            "full_absolute_budget": fraction_row(FULL_BUDGET),
            "k185_k188_boundary_union": fraction_row(boundary),
            "k224_core_through_q4": fraction_row(cube_q4),
            "k242_q4_to_q5_shell": fraction_row(shell_q45),
            "known_total_through_q5_plus_boundaries": fraction_row(known_total),
            "remaining_for_q_greater_than_5_and_unallocated_defects": fraction_row(remaining),
            "known_fraction_of_full_budget": f"{float(Q(str(known_total / FULL_BUDGET))):.12e}",
            "remaining_fraction_of_full_budget": f"{float(Q(str(remaining / FULL_BUDGET))):.12e}",
            "theorem": (
                "K188's four-region cover explicitly permits adding its eighteen "
                "coherent-group boundary ceilings by union bound. K224 and K242 "
                "cover disjoint nested-cube core regions through q=5. Their three "
                "outward contributions therefore share one absolute 1e-21 budget."
            ),
        },
        "q5_to_q6_signed_degree_zero_through_nine": {
            "arb_256_bit": str(polynomial_shell),
            "strict_rational_lower": str(Q6_POLYNOMIAL_LOWER),
            "strict_rational_upper": str(Q6_POLYNOMIAL_UPPER),
            "cube_integrated_log_polynomial_sha256": {
                str(q): log_polynomial_hash(cube_coefficients[q]) for q in (5, 6)
            },
            "interpretation": (
                "The signed retained polynomial is tiny and positive, but it is not "
                "a complete shell enclosure without the degree-ten-and-higher tail."
            ),
        },
        "q5_to_q6_inherited_orbit_tail": {
            "starts_at_total_degree": TAIL_START,
            "cube_corner_x_max": 5,
            "exact_core_majorant": str(tail_core),
            "maximum_geometric_ratio": str(ratio_ceiling),
            "exact_shell_measure": str(shell_measure),
            "pi_lower": str(PI_LOWER),
            "normalized_upper": fraction_row(tail_upper),
            "complete_method_upper": fraction_row(method_upper),
            "method_upper_to_composed_remaining": f"{float(Q(str(method_upper / remaining))):.12e}",
            "result": "fails_composed_remaining_budget",
            "method_limit": (
                "The exact degree-nine signed part fits, but the unchanged absolute "
                "orbit tail is over two orders of magnitude above the composed "
                "residual. More output precision cannot repair this certificate; "
                "the tail order, anchor, reanchoring or cancellation method must change."
            ),
        },
        "unallocated_obligations": {
            "k204_k209_common_reference": (
                "K204/K209 provide exact geometry and conditional moment-defect "
                "coefficients, but their own claim ceilings withhold the complete "
                "signed normalized/coalescent derivative norm. They cannot yet be "
                "converted into a commensurate absolute error addend."
            ),
            "coalescent_core": "Complete normalized/coalescent signed derivative enclosure remains open.",
            "farther_prefix": "No q>5 shell is certified by K243.",
        },
        "controls": (
            "The independent probe rebuilds the boundary union from K185's group "
            "ceilings and K188's Gamma-six strip fraction, integrates all 1,276 raw "
            "allocation functions on q=5,6 without orbit projection, recomputes h10 "
            "by Newton power sums, and rejects polynomial-only, omitted-boundary and "
            "commensurate-raw-K209 interpretations."
        ),
        "source_routing": (
            "SC-ACT-01/02 ASSERTS; SC-META-53 UNCERTAIN; LT-GR6b/LT-SM8 NEEDS. "
            "No source or physics-ledger row moves."
        ),
        "claim_ceiling": (
            "Exact composition of already certified outward contributions and an "
            "exact failure of the unchanged degree-nine-plus-absolute-tail certificate "
            "on q=5-to-q=6. No lower bound on the signed shell, K215 impossibility, "
            "complete prefix, source action/state/domain, physics verdict, canon, "
            "paper or public-posture change."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    result = generate()
    if args.write:
        OUT.write_text(json.dumps(result, indent=2) + "\n")
    budget = result["known_budget_composition"]
    shell = result["q5_to_q6_inherited_orbit_tail"]
    print("[PASS] K243 composed remaining", budget["remaining_for_q_greater_than_5_and_unallocated_defects"]["decimal"])
    print("[PASS] K243 q6 method ratio", shell["method_upper_to_composed_remaining"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
