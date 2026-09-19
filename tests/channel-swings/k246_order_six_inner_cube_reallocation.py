#!/usr/bin/env python3
"""K246: signed inner-cube replacement and renewed exact-route shell ladder."""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
from hashlib import sha256
import json
from math import factorial

from flint import arb, ctx, fmpq

from k242_order_six_third_shell_signed_taylor import (
    K185, ROOT, coefficient_hash, evaluate_log_polynomial,
    integrate_polynomial, log_polynomial_hash, moment_polynomials,
    orbit_groups, taylor_polynomials, terms,
)
from k243_order_six_budget_composition_q6_method_limit import K224, PI_LOWER, row_fraction
from k244_order_six_exact_corner_shell_ladder import OUT as K244, exact_corner, sinh_log
from k245_order_six_full_domain_route_shell_ladder import OUT as K245, tail_majorant

OUT = ROOT / "lab/process/k246-order-six-inner-cube-reallocation.json"
K242 = ROOT / "lab/process/k242-order-six-third-shell-signed-taylor.json"
ORDER = 17
TAIL_START = ORDER + 1
ctx.prec = 256

CUBE_BRACKET = (fmpq(3642, 10**32), fmpq(3643, 10**32))
SHELL_BRACKETS = {
    14: (fmpq(34913, 10**26), fmpq(34914, 10**26)),
    15: (fmpq(74471, 10**26), fmpq(74472, 10**26)),
}


def fraction_row(value: fmpq) -> dict[str, object]:
    value_q = Q(str(value))
    return {
        "numerator": value_q.numerator,
        "denominator": value_q.denominator,
        "decimal": f"{float(value_q):.12e}",
    }


def complete_row(polynomial_value, lower: fmpq, upper: fmpq,
                 groups, q: int, shell: bool) -> dict[str, object]:
    assert polynomial_value > arb(str(lower))
    assert polynomial_value < arb(str(upper))
    core_tail, ratio = tail_majorant(groups, q)
    measure = (sinh_log(q) ** 8 - sinh_log(q - 1) ** 8
               if shell else sinh_log(q) ** 8)
    tail_upper = (
        fmpq(2**8 * 256**6, factorial(5)) / PI_LOWER**8
        * measure * core_tail
    )
    return {
        "region": f"q={q-1}-to-q={q}" if shell else f"q<= {q}",
        "exact_x_max": str(exact_corner(q)),
        "signed_order_0_through_17_arb": str(polynomial_value),
        "strict_polynomial_lower": str(lower),
        "strict_polynomial_upper": str(upper),
        "tail_starts_at_total_degree": TAIL_START,
        "exact_core_tail_majorant": str(core_tail),
        "maximum_geometric_ratio": str(ratio),
        "exact_region_measure": str(measure),
        "normalized_tail_upper": fraction_row(tail_upper),
        "complete_lower": fraction_row(lower - tail_upper),
        "complete_upper": fraction_row(upper + tail_upper),
    }


def generate() -> dict[str, object]:
    k224 = json.loads(K224.read_text())
    k242 = json.loads(K242.read_text())
    k244 = json.loads(K244.read_text())
    k245 = json.loads(K245.read_text())

    items = list(terms(json.loads(K185.read_text())))
    groups = orbit_groups(items)
    assert len(items) == 1864 and len(groups) == 307
    polynomials = taylor_polynomials(groups, ORDER)
    cube_coefficients: dict[int, list[fmpq]] = {}
    for q in (4, 13, 14, 15):
        moments = moment_polynomials(q, ORDER)
        cube_coefficients[q] = [fmpq(0)] * 9
        for polynomial in polynomials:
            values = integrate_polynomial(polynomial, moments)
            for power, value in enumerate(values):
                cube_coefficients[q][power] += value

    normalization = arb(2**8 * 256**6) / factorial(5) / arb.pi()**8
    cube_polynomial = normalization * evaluate_log_polynomial(cube_coefficients[4], 4)
    cube = complete_row(cube_polynomial, *CUBE_BRACKET, groups, 4, False)
    shells: dict[str, object] = {}
    for q in (14, 15):
        polynomial_shell = normalization * (
            evaluate_log_polynomial(cube_coefficients[q], q)
            - evaluate_log_polynomial(cube_coefficients[q - 1], q - 1)
        )
        shells[str(q)] = complete_row(
            polynomial_shell, *SHELL_BRACKETS[q], groups, q, True)

    full_budget = fmpq(1, 10**21)
    signed_cube_upper = row_fraction(cube["complete_upper"])
    q5_upper = fmpq(k242["complete_third_shell"]["absolute_upper"])
    q6_q10 = row_fraction(k244["budget_ladder"]["q6_through_q10_complete_upper"])
    inherited = {
        q: row_fraction(k245["shells"][str(q)]["complete_shell_upper"])
        for q in (11, 12, 13)
    }
    q14_upper = row_fraction(shells["14"]["complete_upper"])
    q15_lower = row_fraction(shells["15"]["complete_lower"])
    through_q13 = signed_cube_upper + q5_upper + q6_q10 + sum(inherited.values(), fmpq(0))
    remaining_after_q13 = full_budget - through_q13
    remaining_after_q14 = remaining_after_q13 - q14_upper
    assert remaining_after_q13 > q14_upper
    assert remaining_after_q14 > 0
    assert q15_lower > remaining_after_q14

    old_cube = fmpq(k224["combined_inner_first_second_cube_absolute_upper"])
    assert signed_cube_upper < old_cube / 10**7
    return {
        "schema_version": "1.0",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "input_sha256": {
            path.stem.split("-")[0]: sha256(path.read_bytes()).hexdigest()
            for path in (K185, K224, K242, K244, K245)
        },
        "object": (
            "Signed degree-seventeen replacement for the complete q<=4 cube "
            "and renewed K213/K218 exact-route shell ladder through q=15"
        ),
        "scope": (
            "Internal order-six finite-prefix integration algebra on the exact "
            "K213/K218 route; not a source action, physical state, quotient, or observable"
        ),
        "expansion": {
            "anchor_c": [1] * 8,
            "total_degree_inclusive": ORDER,
            "tail_start": TAIL_START,
            "raw_signed_terms": len(items),
            "retained_s6_orbits": len(groups),
            "degree_coefficient_sha256": {
                str(degree): coefficient_hash(polynomial)
                for degree, polynomial in enumerate(polynomials)
            },
            "cube_integrated_log_polynomial_sha256": {
                str(q): log_polynomial_hash(cube_coefficients[q])
                for q in (4, 13, 14, 15)
            },
        },
        "signed_inner_cube": cube,
        "shells": shells,
        "route_composition": {
            "k224_disposition": "historical_cellwise_absolute_ceiling_replaced_not_added",
            "proof": (
                "K224 and this certificate integrate the same complete K218 q<=4 "
                "cube with the same normalization. K224 took cellwise absolute "
                "enclosures before global signed summation; K246 instead sums all "
                "1,864 signed terms through degree seventeen and adds a rigorous "
                "absolute remainder. They are alternative enclosures of one region."
            ),
            "k224_historical_complete_cube_upper": fraction_row(old_cube),
            "k246_signed_complete_cube_upper": fraction_row(signed_cube_upper),
            "improvement_factor_lower_than": "1e-7_of_k224",
            "k224_charged_on_k246_route": False,
        },
        "exact_route_budget": {
            "full_absolute_budget": fraction_row(full_budget),
            "signed_q4_cube_upper": fraction_row(signed_cube_upper),
            "q4_to_q5_complete_upper_inherited": fraction_row(q5_upper),
            "q6_through_q10_complete_upper_inherited": fraction_row(q6_q10),
            "q11_complete_upper_inherited": fraction_row(inherited[11]),
            "q12_complete_upper_inherited": fraction_row(inherited[12]),
            "q13_complete_upper_inherited": fraction_row(inherited[13]),
            "remaining_after_q13": fraction_row(remaining_after_q13),
            "q14_complete_upper": fraction_row(q14_upper),
            "remaining_after_q14": fraction_row(remaining_after_q14),
            "q15_complete_lower": fraction_row(q15_lower),
            "q15_lower_to_remaining_after_q14": f"{float(Q(str(q15_lower / remaining_after_q14))):.12e}",
            "result": "q14_certified__q15_exceeds_reallocated_exact_route_budget",
        },
        "controls": (
            "The independent probe rebuilds the signed orbit expansion from raw "
            "allocations, replays every recorded polynomial hash and Newton h18 "
            "tail, and rejects K224 double-counting, an omitted tail, a full-cube "
            "versus shell measure swap, and a false pointwise S6 reading."
        ),
        "source_routing": (
            "SC-ACT-01/02 ASSERTS; SC-META-53 UNCERTAIN; LT-GR6b/LT-SM8 NEEDS. "
            "No source or physics-ledger row moves."
        ),
        "claim_ceiling": (
            "A sharper complete q<=4 enclosure, exact-route shell certification "
            "through q=14, and shellwise allocation exhaustion at q15. No lower "
            "bound on the original full order-six error, K215 impossibility, "
            "source action/state/domain, physics verdict, canon, paper, or public-posture change."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    result = generate()
    if args.write:
        OUT.write_text(json.dumps(result, indent=2) + "\n")
    budget = result["exact_route_budget"]
    print("[PASS] K246 signed q<=4 upper", budget["signed_q4_cube_upper"]["decimal"])
    print("[PASS] K246 q14 upper", budget["q14_complete_upper"]["decimal"])
    print("[PASS] K246 q15 allocation ratio", budget["q15_lower_to_remaining_after_q14"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
