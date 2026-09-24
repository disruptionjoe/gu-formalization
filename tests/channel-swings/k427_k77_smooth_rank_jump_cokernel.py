#!/usr/bin/env python3
"""K427 smooth category boundary for the K425 rank-jump family."""

from __future__ import annotations

import argparse
import json


def evaluate_at_one(coefficients: list[int]) -> int:
    return sum(coefficients)


def divide_by_one_minus_t(coefficients: list[int]) -> list[int]:
    """Exact ascending-coefficient division when p(1)=0."""
    if evaluate_at_one(coefficients) != 0:
        raise ValueError("polynomial does not vanish at t=1")
    quotient: list[int] = []
    running = 0
    for coefficient in coefficients[:-1]:
        running += coefficient
        quotient.append(running)
    while quotient and quotient[-1] == 0:
        quotient.pop()
    return quotient


def multiply_by_one_minus_t(coefficients: list[int]) -> list[int]:
    if not coefficients:
        return [0]
    result = [0] * (len(coefficients) + 1)
    for index, coefficient in enumerate(coefficients):
        result[index] += coefficient
        result[index + 1] -= coefficient
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result


def demo() -> dict:
    samples = [[-1, 1], [2, -3, 1], [3, 0, -3], [1, -4, 6, -4, 1]]
    divisions = []
    for polynomial in samples:
        quotient = divide_by_one_minus_t(polynomial)
        assert multiply_by_one_minus_t(quotient) == polynomial
        divisions.append({"polynomial": polynomial, "quotient": quotient})
    return {
        "schema_version": "1.0",
        "classification": "BRIDGE_OR_SEMANTIC_BOUNDARY",
        "direction": "native_to_native",
        "family": {
            "map": "diag(1,...,1,1-t) on the first 70 columns of C-infinity(R)^91 -> C-infinity(R)^70",
            "generic_rank": 70,
            "rank_at_t_equals_1": 69,
            "fiber_kernel_dimensions": {"generic": 21, "t_equals_1": 22},
        },
        "smooth_global_result": {
            "kernel": "C-infinity(R)^21 from the final 21 zero columns",
            "extra_global_smooth_syzygy": False,
            "range": "vectors whose final component vanishes at t=1",
            "cokernel": "R via evaluation of the final component at t=1",
            "cokernel_dimension": 1,
            "hadamard_division": "f(1)=0 iff f=(1-t)g for a smooth g",
            "polynomial_controls": divisions,
        },
        "decision": {
            "rank_jump_creates_smooth_cokernel_class": True,
            "fiber_kernel_jump_creates_global_smooth_generator": False,
            "category_and_domain_are_load_bearing": True,
            "source_owned_transverse_family_supplied": False,
            "physical_bfv_cohomology_constructed": False,
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--demo", action="store_true")
    args = parser.parse_args()
    if not args.demo:
        parser.error("use --demo")
    print(json.dumps(demo(), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
