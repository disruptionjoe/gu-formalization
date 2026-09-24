#!/usr/bin/env python3
"""K428 L2 closed-range and Green boundary for the K425 rank jump."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction


def witness(n: int) -> dict:
    assert n > 0
    output_norm_squared = Fraction(1, 3 * n * n)
    return {
        "n": n,
        "input": "sqrt(n) times the indicator of [1-1/n,1]",
        "input_norm_squared": "1",
        "output_norm_squared": f"{output_norm_squared.numerator}/{output_norm_squared.denominator}",
        "output_norm": f"1/(sqrt(3)*{n})",
    }


def demo() -> dict:
    witnesses = [witness(n) for n in [1, 2, 4, 8, 16, 32]]
    return {
        "schema_version": "1.0",
        "classification": "BRIDGE_OR_SEMANTIC_BOUNDARY",
        "direction": "native_to_native",
        "scalar_multiplier": {
            "operator": "M_(1-t): L2([0,1]) -> L2([0,1])",
            "kernel_dimension": 0,
            "adjoint_kernel_dimension": 0,
            "range_dense": True,
            "range_closed": False,
            "range_proper_witness": "the constant function 1 is not in the range because 1/(1-t) is not L2",
            "bounded_below": False,
            "bounded_green_inverse_exists": False,
            "unit_input_witnesses": witnesses,
        },
        "full_70_by_91_family": {
            "global_kernel": "L2([0,1])^21 from the final 21 zero columns",
            "extra_global_l2_kernel": False,
            "range_dense_in_target": True,
            "range_closed": False,
            "unreduced_cokernel": "nonzero non-Hausdorff quotient",
            "reduced_cokernel_dimension": 0,
        },
        "decision": {
            "isolated_rank_jump_forces_nonzero_reduced_hilbert_cohomology": False,
            "isolated_rank_jump_can_destroy_closed_range": True,
            "smooth_and_hilbert_cokernels_agree_automatically": False,
            "green_domain_and_closed_range_are_load_bearing": True,
            "positive_physical_domain_constructed": False,
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
