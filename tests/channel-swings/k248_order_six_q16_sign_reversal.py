#!/usr/bin/env python3
"""K248: first farther-shell sign-reversal discriminator at q=16."""
from __future__ import annotations

import argparse
import json
from fractions import Fraction as Q
from hashlib import sha256
from math import factorial

from flint import arb, ctx, fmpq

from k242_order_six_third_shell_signed_taylor import (
    K185,
    ROOT,
    coefficient_hash,
    evaluate_log_polynomial,
    integrate_polynomial,
    log_polynomial_hash,
    moment_polynomials,
    orbit_groups,
    taylor_polynomials,
    terms,
)
from k243_order_six_budget_composition_q6_method_limit import PI_LOWER
from k244_order_six_exact_corner_shell_ladder import (
    complete_homogeneous,
    exact_corner,
    sinh_log,
)
from k247_order_six_cumulative_q15_boundary import OUT as K247

OUT = ROOT / "lab/process/k248-order-six-q16-sign-reversal.json"
ORDER, TAIL_START, QLOW, QHIGH = 21, 22, 15, 16
POLYNOMIAL_LOWER: fmpq | None = fmpq(149972, 10**26)
POLYNOMIAL_UPPER: fmpq | None = fmpq(149973, 10**26)
ctx.prec = 256


def row(value: fmpq) -> dict[str, object]:
    q = Q(str(value))
    return {
        "numerator": q.numerator,
        "denominator": q.denominator,
        "decimal": f"{float(q):.12e}",
    }


def tail_majorant(groups) -> tuple[fmpq, fmpq]:
    x = exact_corner(QHIGH)
    total, maximum = fmpq(0), fmpq(0)
    for rows, weight in groups.items():
        base, ratios = fmpq(1), []
        for mask in rows:
            denominator = 256 + mask.bit_count()
            base /= denominator
            ratios.append(x * mask.bit_count() / denominator)
        ratio = max(ratios) * fmpq(TAIL_START + 14, TAIL_START + 1)
        assert ratio < 1
        maximum = max(maximum, ratio)
        total += (
            abs(weight)
            * base
            * complete_homogeneous(ratios, TAIL_START)
            / (1 - ratio)
        )
    return total, maximum


def generate() -> dict[str, object]:
    groups = orbit_groups(list(terms(json.loads(K185.read_text()))))
    assert len(groups) == 307
    polynomials = taylor_polynomials(groups, ORDER)
    cube_coefficients: dict[int, list[fmpq]] = {}
    for q in (QLOW, QHIGH):
        moments = moment_polynomials(q, ORDER)
        coefficients = [fmpq(0)] * 9
        for polynomial in polynomials:
            for power, value in enumerate(integrate_polynomial(polynomial, moments)):
                coefficients[power] += value
        cube_coefficients[q] = coefficients

    normalization = arb(2**8 * 256**6) / factorial(5) / arb.pi()**8
    polynomial = normalization * (
        evaluate_log_polynomial(cube_coefficients[QHIGH], QHIGH)
        - evaluate_log_polynomial(cube_coefficients[QLOW], QLOW)
    )
    core_tail, ratio = tail_majorant(groups)
    measure = sinh_log(QHIGH) ** 8 - sinh_log(QLOW) ** 8
    tail = (
        fmpq(2**8 * 256**6, factorial(5))
        / PI_LOWER**8
        * measure
        * core_tail
    )

    certified = POLYNOMIAL_LOWER is not None and POLYNOMIAL_UPPER is not None
    complete_lower = complete_upper = None
    if certified:
        assert polynomial > arb(str(POLYNOMIAL_LOWER))
        assert polynomial < arb(str(POLYNOMIAL_UPPER))
        complete_lower = POLYNOMIAL_LOWER - tail
        complete_upper = POLYNOMIAL_UPPER + tail
        assert complete_lower > 0

    result = {
        "schema_version": "1.0",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "input_sha256": {
            "k185": sha256(K185.read_bytes()).hexdigest(),
            "k247": sha256(K247.read_bytes()).hexdigest(),
        },
        "object": "complete signed K218 q=15-to-q=16 shell at total degree 21",
        "scope": (
            "exact K213/K218 internal order-six first farther shell; not a "
            "full-tail, full-error, source, or physics verdict"
        ),
        "expansion": {
            "order": ORDER,
            "tail_start": TAIL_START,
            "raw_terms": 1864,
            "orbits": len(groups),
            "degree_sha256": {
                str(i): coefficient_hash(p) for i, p in enumerate(polynomials)
            },
            "integrated_log_polynomial_sha256": {
                str(q): log_polynomial_hash(cube_coefficients[q])
                for q in (QLOW, QHIGH)
            },
        },
        "certificate": {
            "region": "q=15-to-q=16",
            "exact_x_max": str(exact_corner(QHIGH)),
            "signed_order_0_through_21_arb": str(polynomial),
            "strict_polynomial_lower": (
                str(POLYNOMIAL_LOWER) if certified else None
            ),
            "strict_polynomial_upper": (
                str(POLYNOMIAL_UPPER) if certified else None
            ),
            "exact_core_tail_majorant": str(core_tail),
            "maximum_geometric_ratio": str(ratio),
            "exact_shell_measure": str(measure),
            "normalized_tail_upper": row(tail),
            "complete_lower": row(complete_lower) if certified else None,
            "complete_upper": row(complete_upper) if certified else None,
        },
        "decision": {
            "certified": certified,
            "shell_strictly_positive": bool(certified and complete_lower > 0),
            "result": (
                "q16_shell_positive__first_farther_sign_reversal_not_found"
                if certified and complete_lower > 0
                else "scout_only"
            ),
        },
        "controls": (
            "Independent raw-orbit, moment, coefficient-hash and Newton h22 "
            "replay; hostile omitted-tail, cube-for-shell and full-tail "
            "globalization checks."
        ),
        "source_routing": (
            "SC-ACT-01/02 ASSERTS; SC-META-53 UNCERTAIN; "
            "LT-GR6b/LT-SM8 NEEDS. No source or ledger row moves."
        ),
        "claim_ceiling": (
            "Only the sign of the complete q=15-to-q=16 shell. A positive "
            "first farther shell is not a global tail sign theorem, full-error "
            "lower bound, K215 impossibility, pointwise sign, physics, canon, "
            "paper, or public-posture change."
        ),
    }
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    result = generate()
    if args.write:
        if not result["decision"]["certified"]:
            raise SystemExit("refusing to write an uncertified scout")
        OUT.write_text(json.dumps(result, indent=2) + "\n")
    print("[K248] q16 shell polynomial", result["certificate"]["signed_order_0_through_21_arb"])
    print("[K248] q16 shell tail", result["certificate"]["normalized_tail_upper"]["decimal"])
    if result["decision"]["certified"]:
        print("[PASS] K248 q16 shell", result["certificate"]["complete_lower"]["decimal"])
