#!/usr/bin/env python3
"""K472 effective-complex properness compiler."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from typing import Any

from k471_k77_effective_homology_transfer import q, transfer


def compile_packet(a: Any, b: Any, c: Any, t: Any) -> dict[str, Any]:
    result = transfer(a, b, c, t)
    effective = result["effective"]
    return {
        "effective_differential": effective,
        "total_acyclic": effective != 0,
        "cohomology_dimensions": [0, 0] if effective != 0 else [1, 1],
        "determinant": result["pivot"] * effective,
    }


def demo() -> dict[str, Any]:
    positive = compile_packet("1/2", "1/3", "1/4", "1")
    obstructed = compile_packet("1/2", "1/3", "1/4", "1/18")
    small = compile_packet(0, "1/10", "1/10", "1/100")
    return {
        "schema_version": "1.0",
        "result_id": "K472-K77-EFFECTIVE-PROPERNESS-COMPILER",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "decision_contract": {
            "required_inputs": ["complete action-owned coefficients", "typed nilpotent squares", "closed-domain preservation", "base deformation retract", "invertible perturbation factors"],
            "properness_rule": "accept only when the exact transferred homology complex is acyclic",
            "obstruction_rule": "a nonzero transferred homology class rejects properness",
            "coefficient_smallness_alone_is_sufficient": False,
            "finite_control_is_native_action": False,
        },
        "positive_control": {
            "effective_differential": str(positive["effective_differential"]),
            "determinant": str(positive["determinant"]),
            "cohomology_dimensions": positive["cohomology_dimensions"],
            "admitted": positive["total_acyclic"],
        },
        "obstruction_control": {
            "effective_differential": str(obstructed["effective_differential"]),
            "determinant": str(obstructed["determinant"]),
            "cohomology_dimensions": obstructed["cohomology_dimensions"],
            "admitted": obstructed["total_acyclic"],
        },
        "smallness_counterexample": {
            "a": "0",
            "b": "1/10",
            "c": "1/10",
            "t": "1/100",
            "effective_differential": str(small["effective_differential"]),
            "cohomology_dimensions": small["cohomology_dimensions"],
            "small_coefficients_do_not_remove_base_homology": True,
        },
        "native_status": {
            "actual_action_packet_present": False,
            "native_properness_emitted": False,
            "physical_cohomology_claimed": False,
        },
    }


def main() -> int:
    argparse.ArgumentParser().parse_args()
    print(json.dumps(demo(), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
