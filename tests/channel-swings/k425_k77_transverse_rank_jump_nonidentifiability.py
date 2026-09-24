#!/usr/bin/env python3
"""K425 transverse rank-jump completion nonidentifiability."""

from __future__ import annotations

import argparse
import hashlib
import json
from typing import Any


def digest(value: Any) -> str:
    return hashlib.sha256(json.dumps(value, separators=(",", ":"), sort_keys=True).encode()).hexdigest()


def family(matching_jet_order: int) -> dict:
    exponent = matching_jet_order + 1
    return {
        "matching_jet_order": matching_jet_order,
        "coefficient": f"1-t^{exponent}",
        "base_value": 1,
        "base_derivatives_through_matching_order": [0] * matching_jet_order,
        "generic_rank": 70,
        "generic_kernel_dimension": 21,
        "rank_at_t_equals_1": 69,
        "kernel_dimension_at_t_equals_1": 22,
        "cokernel_dimension_at_t_equals_1": 1,
        "extra_fiber_relation_at_t_equals_1": True,
        "global_polynomial_extra_syzygy": False,
    }


def demo() -> dict:
    families = [family(order) for order in range(1, 9)]
    return {
        "schema_version": "1.0",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "native_to_native",
        "frozen_complex": {
            "map": "A0=[I_70 0_70x21]: R^91 -> R^70",
            "rank": 70,
            "kernel_dimension": 21,
            "cokernel_dimension": 0,
        },
        "constant_completion": {
            "coefficient": "1",
            "rank_everywhere": 70,
            "kernel_dimension_everywhere": 21,
        },
        "rank_jump_completions": families,
        "shared_frozen_data": {
            "all_base_maps_equal_A0": True,
            "arbitrarily_long_finite_transverse_jets_can_match_constant_completion": True,
            "homogeneous_orbit_transport_unchanged": True,
            "family_digest": digest(families),
        },
        "algebraic_boundary": {
            "polynomial_ring_is_domain": True,
            "fiber_relation_can_appear_at_rank_jump_without_global_polynomial_syzygy": True,
            "constant_rank_vector_bundle_extends_across_t_equals_1": False,
        },
        "decision": {
            "k419_frozen_complex_identifies_transverse_rank_behavior": False,
            "k422_homogeneous_transport_identifies_transverse_rank_behavior": False,
            "source_owned_transverse_family_still_required": True,
            "nonlinear_koszul_tate_properness_proved": False,
            "next_exact_input": "A source/action-owned transverse coefficient family and its nonlinear constraint functions through the first actual rank-changing stratum.",
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
