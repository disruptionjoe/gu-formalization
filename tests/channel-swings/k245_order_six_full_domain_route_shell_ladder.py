#!/usr/bin/env python3
"""K245: full-domain K213/K218 route composition and order-17 shell ladder."""
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
from k243_order_six_budget_composition_q6_method_limit import (
    K188, K224, K242, PI_LOWER, boundary_union, row_fraction,
)
from k244_order_six_exact_corner_shell_ladder import (
    K213, K218, OUT as K244, complete_homogeneous, exact_corner, sinh_log,
)

OUT = ROOT / "lab/process/k245-order-six-full-domain-route-shell-ladder.json"
ORDER = 17
TAIL_START = ORDER + 1
ctx.prec = 256

POLYNOMIAL_BRACKETS = {
    11: (fmpq(2284, 10**26), fmpq(2285, 10**26)),
    12: (fmpq(6200, 10**26), fmpq(6201, 10**26)),
    13: (fmpq(15306, 10**26), fmpq(15307, 10**26)),
}


def fraction_row(value: fmpq) -> dict[str, object]:
    value_q = Q(str(value))
    return {
        "numerator": value_q.numerator,
        "denominator": value_q.denominator,
        "decimal": f"{float(value_q):.12e}",
    }


def tail_majorant(groups, q: int) -> tuple[fmpq, fmpq]:
    x_max = exact_corner(q)
    total = fmpq(0)
    maximum_ratio = fmpq(0)
    for rows, weight in groups.items():
        base_value = fmpq(1)
        ratios: list[fmpq] = []
        for row in rows:
            denominator = 256 + row.bit_count()
            base_value /= denominator
            ratios.append(x_max * row.bit_count() / denominator)
        ratio_ceiling = max(ratios) * fmpq(TAIL_START + 14, TAIL_START + 1)
        assert ratio_ceiling < 1
        maximum_ratio = max(maximum_ratio, ratio_ceiling)
        total += (
            abs(weight) * base_value
            * complete_homogeneous(ratios, TAIL_START)
            / (1 - ratio_ceiling)
        )
    return total, maximum_ratio


def generate() -> dict[str, object]:
    k185 = json.loads(K185.read_text())
    k188 = json.loads(K188.read_text())
    k213 = json.loads(K213.read_text())
    k218 = json.loads(K218.read_text())
    k224 = json.loads(K224.read_text())
    k242 = json.loads(K242.read_text())
    k244 = json.loads(K244.read_text())

    items = list(terms(k185))
    groups = orbit_groups(items)
    assert len(items) == 1864 and len(groups) == 307
    polynomials = taylor_polynomials(groups, ORDER)
    cube_coefficients: dict[int, list[fmpq]] = {}
    for q in range(10, 14):
        moments = moment_polynomials(q, ORDER)
        cube_coefficients[q] = [fmpq(0)] * 9
        for polynomial in polynomials:
            values = integrate_polynomial(polynomial, moments)
            for power, value in enumerate(values):
                cube_coefficients[q][power] += value

    normalization = arb(2**8 * 256**6) / factorial(5) / arb.pi()**8
    shell_rows: dict[str, object] = {}
    for q in range(11, 14):
        polynomial_shell = normalization * (
            evaluate_log_polynomial(cube_coefficients[q], q)
            - evaluate_log_polynomial(cube_coefficients[q - 1], q - 1)
        )
        lower, upper = POLYNOMIAL_BRACKETS[q]
        assert polynomial_shell > arb(str(lower))
        assert polynomial_shell < arb(str(upper))
        core_tail, ratio = tail_majorant(groups, q)
        measure = sinh_log(q) ** 8 - sinh_log(q - 1) ** 8
        tail_upper = (
            fmpq(2**8 * 256**6, factorial(5)) / PI_LOWER**8
            * measure * core_tail
        )
        shell_rows[str(q)] = {
            "shell": f"q={q-1}-to-q={q}",
            "exact_x_max": str(exact_corner(q)),
            "signed_order_0_through_17_arb": str(polynomial_shell),
            "strict_polynomial_lower": str(lower),
            "strict_polynomial_upper": str(upper),
            "tail_starts_at_total_degree": TAIL_START,
            "exact_core_tail_majorant": str(core_tail),
            "maximum_geometric_ratio": str(ratio),
            "exact_shell_measure": str(measure),
            "normalized_tail_upper": fraction_row(tail_upper),
            "complete_shell_lower": fraction_row(lower - tail_upper),
            "complete_shell_upper": fraction_row(upper + tail_upper),
        }

    full_budget = fmpq(1, 10**21)
    k224_upper = fmpq(k224["combined_inner_first_second_cube_absolute_upper"])
    k242_upper = fmpq(k242["complete_third_shell"]["absolute_upper"])
    exact_route_base = k224_upper + k242_upper
    boundary_amount = boundary_union(k188)
    q6_q10 = row_fraction(k244["budget_ladder"]["q6_through_q10_complete_upper"])
    q11_upper = row_fraction(shell_rows["11"]["complete_shell_upper"])
    q12_upper = row_fraction(shell_rows["12"]["complete_shell_upper"])
    q13_lower = row_fraction(shell_rows["13"]["complete_shell_lower"])
    remaining_after_q12 = full_budget - exact_route_base - q6_q10 - q11_upper - q12_upper
    assert remaining_after_q12 > 0
    assert q13_lower > remaining_after_q12

    # K185/K188 price excisions required by the determinant-quotient numerical
    # core. K213 instead starts from every original K185 signed permutation
    # term, integrates the full Gamma radius, and K218 integrates the full
    # original uniform simplex exactly. Those excisions are not made on K218.
    assert k213["counts"]["leibniz_terms"] == k218["terms"] == 1864
    assert "no rho<=1/4 restriction is imposed on the identity" in k213["core_tail"]["scope"]
    assert "original uniform simplex density" in k213["normalization"]
    assert "original uniform 13-simplex" in k218["object"]
    assert "exact for every finite positive auxiliary t" in k218["identity"]
    assert k188["domain_cover"]["regions"][2]["status"] == "OPEN_DETERMINANT_PRESERVING_INTERVAL_ERROR"

    opening_after_q5 = full_budget - exact_route_base
    boundary_charged_remaining = opening_after_q5 - boundary_amount - q6_q10
    q11_lower = row_fraction(shell_rows["11"]["complete_shell_lower"])
    assert q11_lower > boundary_charged_remaining

    return {
        "schema_version": "1.0",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "input_sha256": {
            path.stem.split("-")[0]: sha256(path.read_bytes()).hexdigest()
            for path in (K185, K188, K213, K218, K224, K242, K244)
        },
        "object": (
            "K213/K218 full-domain route composition and total-degree-17 "
            "K218 shell certificates q=10 through q=13"
        ),
        "scope": (
            "Internal order-six finite-prefix integration algebra on the exact "
            "K213/K218 route; not a source action, physical state, quotient, or observable"
        ),
        "route_composition": {
            "k185_k188_disposition": "alternative_excised_determinant_quotient_numerical_route_not_additive_on_exact_k213_k218_route",
            "proof": (
                "K185/K188 bound the face, small-radius, and large-radius regions "
                "removed to create a compact determinant-quotient numerical core. "
                "K213 instead applies the positive Bessel-Laplace representation "
                "to all 1,864 original signed K185 permutation terms and integrates "
                "the complete Gamma radius without a rho<=1/4 restriction. K218 "
                "then integrates the original uniform thirteen-simplex exactly for "
                "every finite positive auxiliary point. The exact route makes none "
                "of the K185/K188 excisions, so their union ceiling is not an "
                "additional error on K218. It remains valid if the excised quotient "
                "core route is revived."
            ),
            "k185_k188_boundary_union_alternative_route_amount": fraction_row(boundary_amount),
            "k185_k188_boundary_union_charged_on_exact_route": False,
            "k185_k188_boundary_union_required_if_excised_quotient_route_revived": True,
            "k204_k209_disposition_inherited": k244["route_composition"]["k204_k209_disposition"],
        },
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
                for q in range(10, 14)
            },
        },
        "shells": shell_rows,
        "exact_route_budget": {
            "full_absolute_budget": fraction_row(full_budget),
            "k224_plus_k242_through_q5": fraction_row(exact_route_base),
            "remaining_after_q5_without_alternative_route_excisions": fraction_row(opening_after_q5),
            "q6_through_q10_complete_upper_inherited": fraction_row(q6_q10),
            "q11_complete_upper": fraction_row(q11_upper),
            "q12_complete_upper": fraction_row(q12_upper),
            "remaining_after_q12": fraction_row(remaining_after_q12),
            "q13_complete_lower": fraction_row(q13_lower),
            "q13_lower_to_remaining_after_q12": f"{float(Q(str(q13_lower / remaining_after_q12))):.12e}",
            "result": "q11_and_q12_certified__q13_exceeds_current_exact_route_allocation",
            "counterfactual_with_k185_k188_double_count": {
                "remaining_before_q11": fraction_row(boundary_charged_remaining),
                "q11_lower_exceeds_remaining": True,
            },
        },
        "controls": (
            "The independent probe reconstructs the 307 retained S6 orbits directly "
            "from all 1,864 raw signed entries, rebuilds every degree-zero-through-seventeen "
            "coefficient polynomial from that independent orbit map, recomputes "
            "h18 by Newton power sums, checks the full-domain route endpoints, and "
            "rejects omitted-tail, re-added-boundary, and coarse-corner readings."
        ),
        "source_routing": (
            "SC-ACT-01/02 ASSERTS; SC-META-53 UNCERTAIN; LT-GR6b/LT-SM8 NEEDS. "
            "No source or physics-ledger row moves."
        ),
        "claim_ceiling": (
            "Exact-route removal of alternative K185/K188 excision costs, shell "
            "certificates through q=12, and current shellwise allocation exhaustion "
            "at q13. No lower bound on the original full order-six error, K215 "
            "impossibility, source action/state/domain, physics verdict, canon, "
            "paper, or public-posture change."
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
    print("[PASS] K245 exact-route q11/q12 upper", budget["q11_complete_upper"]["decimal"], budget["q12_complete_upper"]["decimal"])
    print("[PASS] K245 q13 allocation ratio", budget["q13_lower_to_remaining_after_q12"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
