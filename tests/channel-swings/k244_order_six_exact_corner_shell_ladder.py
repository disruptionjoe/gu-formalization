#!/usr/bin/env python3
"""K244: exact transformed-corner order-15 shell ladder and route audit."""
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
    K188, K204, K209, K224, K242, OUT as K243, PI_LOWER,
    boundary_union, row_fraction,
)

K213 = ROOT / "lab/process/k213-order-six-bessel-laplace-radial-elimination.json"
K218 = ROOT / "lab/process/k218-order-six-exact-angular-elimination.json"
OUT = ROOT / "lab/process/k244-order-six-exact-corner-shell-ladder.json"
ORDER = 15
TAIL_START = ORDER + 1
ctx.prec = 256

POLYNOMIAL_BRACKETS = {
    6: (fmpq(12, 10**27), fmpq(13, 10**27)),
    7: (fmpq(93, 10**27), fmpq(94, 10**27)),
    8: (fmpq(50, 10**26), fmpq(51, 10**26)),
    9: (fmpq(213, 10**26), fmpq(214, 10**26)),
    10: (fmpq(749, 10**26), fmpq(750, 10**26)),
    11: (fmpq(228, 10**25), fmpq(229, 10**25)),
}


def fraction_row(value: fmpq) -> dict[str, object]:
    value_q = Q(str(value))
    return {
        "numerator": value_q.numerator,
        "denominator": value_q.denominator,
        "decimal": f"{float(value_q):.12e}",
    }


def complete_homogeneous(ratios: list[fmpq], degree: int) -> fmpq:
    coefficients = [fmpq(1)] + [fmpq(0)] * degree
    for ratio in ratios:
        updated = [fmpq(0)] * (degree + 1)
        power = fmpq(1)
        for k in range(degree + 1):
            for old_degree in range(degree + 1 - k):
                updated[k + old_degree] += coefficients[old_degree] * power
            power *= ratio
        coefficients = updated
    return coefficients[degree]


def exact_corner(q: int) -> fmpq:
    """cosh(log(q))-1 = (q-1)^2/(2q)."""
    return fmpq((q - 1) ** 2, 2 * q)


def sinh_log(q: int) -> fmpq:
    return fmpq(q * q - 1, 2 * q)


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
    k204 = json.loads(K204.read_text())
    k209 = json.loads(K209.read_text())
    k213 = json.loads(K213.read_text())
    k218 = json.loads(K218.read_text())
    k224 = json.loads(K224.read_text())
    k242 = json.loads(K242.read_text())
    k243 = json.loads(K243.read_text())

    items = list(terms(k185))
    groups = orbit_groups(items)
    assert len(items) == 1864 and len(groups) == 307
    polynomials = taylor_polynomials(groups, ORDER)
    cube_coefficients: dict[int, list[fmpq]] = {}
    for q in range(5, 12):
        moments = moment_polynomials(q, ORDER)
        cube_coefficients[q] = [fmpq(0)] * 9
        for polynomial in polynomials:
            values = integrate_polynomial(polynomial, moments)
            for power, value in enumerate(values):
                cube_coefficients[q][power] += value

    normalization = arb(2**8 * 256**6) / factorial(5) / arb.pi()**8
    shell_rows: dict[str, object] = {}
    cumulative_upper = fmpq(0)
    for q in range(6, 12):
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
        shell_lower = lower - tail_upper
        shell_upper = upper + tail_upper
        shell_rows[str(q)] = {
            "shell": f"q={q-1}-to-q={q}",
            "exact_x_max": str(exact_corner(q)),
            "signed_order_0_through_15_arb": str(polynomial_shell),
            "strict_polynomial_lower": str(lower),
            "strict_polynomial_upper": str(upper),
            "tail_starts_at_total_degree": TAIL_START,
            "exact_core_tail_majorant": str(core_tail),
            "maximum_geometric_ratio": str(ratio),
            "exact_shell_measure": str(measure),
            "normalized_tail_upper": fraction_row(tail_upper),
            "complete_shell_lower": fraction_row(shell_lower),
            "complete_shell_upper": fraction_row(shell_upper),
        }
        if q <= 10:
            cumulative_upper += shell_upper

    budget = k243["known_budget_composition"]
    opening_remaining = row_fraction(
        budget["remaining_for_q_greater_than_5_and_unallocated_defects"]
    )
    remaining_after_q10 = opening_remaining - cumulative_upper
    q11_lower = row_fraction(shell_rows["11"]["complete_shell_lower"])
    assert remaining_after_q10 > 0
    assert q11_lower > remaining_after_q10

    # K204/K209 price the optional common-reference cubature branch. K218's
    # exact identity instead cancels that reference and analytically integrates
    # the original uniform simplex before the K224/K242 shell calculation.
    assert "exact full-reference moments" in k204["claim_ceiling"]
    assert "common-reference" not in k218["identity"]
    assert "reference and residual cancel" in k218["identity"]
    assert "exact" in k218["identity"].lower()
    assert k213["normalization"].startswith("Multiply the identity by the original uniform simplex density")
    assert boundary_union(k188) == row_fraction(budget["k185_k188_boundary_union"])
    assert fmpq(k224["combined_inner_first_second_cube_absolute_upper"]) == row_fraction(
        budget["k224_core_through_q4"]
    )
    assert fmpq(k242["complete_third_shell"]["absolute_upper"]) == row_fraction(
        budget["k242_q4_to_q5_shell"]
    )

    return {
        "schema_version": "1.0",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "input_sha256": {
            path.stem.split("-")[0]: sha256(path.read_bytes()).hexdigest()
            for path in (K185, K188, K204, K209, K213, K218, K224, K242, K243)
        },
        "object": (
            "K218 exact signed rational-cosh core shells q=5 through q=11, "
            "with exact transformed corners and total-degree-15 orbit tails"
        ),
        "scope": (
            "Internal order-six finite-prefix integration algebra on the exact "
            "K218 route; not a source action, physical state, quotient or observable"
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
                for q in range(5, 12)
            },
            "exact_corner_theorem": (
                "For t in [0,log(q)], x=cosh(t)-1 is monotone and "
                "x_max=cosh(log(q))-1=(q-1)^2/(2q), not the coarse q-1."
            ),
        },
        "shells": shell_rows,
        "budget_ladder": {
            "opening_remaining_after_boundaries_and_q5": fraction_row(opening_remaining),
            "q6_through_q10_complete_upper": fraction_row(cumulative_upper),
            "remaining_allocation_after_q10": fraction_row(remaining_after_q10),
            "q11_complete_lower": fraction_row(q11_lower),
            "q11_lower_to_remaining_after_q10": f"{float(Q(str(q11_lower / remaining_after_q10))):.12e}",
            "result": "q6_through_q10_certified__q11_exceeds_current_remaining_allocation",
            "interpretation": (
                "Exact transformed corners plus order 15 certify every shell "
                "through q=10 inside K243's residual. The rigorous q=10-to-q=11 "
                "shell lower exceeds what remains after reserving those shell "
                "uppers. This exhausts the current allocation/certificate "
                "composition; it is not a lower bound on the full original "
                "order-six error because earlier upper allocations may be sharpened."
            ),
        },
        "route_composition": {
            "k204_k209_disposition": "alternative_common_reference_cubature_branch_not_additive_on_exact_k218_route",
            "proof": (
                "K204/K209 bound deletion, polynomial moment and Taylor errors "
                "for the K203/K208 common-reference quadrature. K213 cancels the "
                "common reference against the residual and K218 exactly integrates "
                "the original uniform simplex termwise. K224/K242 then integrate "
                "that exact K218 auxiliary integrand. An approximation error from "
                "the unused cubature branch is therefore not added to this exact "
                "branch. K185/K188 quotient, face, radial and small-radius transfer "
                "ceilings remain distinct and are retained in the composed budget."
            ),
            "k185_k188_boundaries_retained": True,
            "common_reference_derivative_owner_required_for_this_route": False,
            "common_reference_derivative_owner_required_if_k203_k209_route_revived": True,
        },
        "controls": (
            "The independent probe rebuilds all order-15 symmetric-cube moments "
            "from 1,276 raw allocations without S6 orbit projection, recomputes "
            "h16 by Newton power sums, checks the exact simplex identity, and "
            "rejects the coarse q-1 corner, omitted tail and additive K204/K209 interpretations."
        ),
        "source_routing": (
            "SC-ACT-01/02 ASSERTS; SC-META-53 UNCERTAIN; LT-GR6b/LT-SM8 NEEDS. "
            "No source or physics-ledger row moves."
        ),
        "claim_ceiling": (
            "Exact-route shell certificates through q=10, current-allocation "
            "exhaustion at q=11, and non-additivity of the unused K204/K209 "
            "cubature errors on K218 only. No K215 impossibility, complete prefix, "
            "source action/state/domain, physics verdict, canon, paper or public-posture change."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    result = generate()
    if args.write:
        OUT.write_text(json.dumps(result, indent=2) + "\n")
    print("[PASS] K244 q6-q10 shell ladder", result["budget_ladder"]["q6_through_q10_complete_upper"]["decimal"])
    print("[PASS] K244 q11 allocation ratio", result["budget_ladder"]["q11_lower_to_remaining_after_q10"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
