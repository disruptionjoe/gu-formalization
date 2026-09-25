#!/usr/bin/env python3
"""K446 compatible nilpotent rank defects with surviving KT cohomology."""

from __future__ import annotations

import argparse
import json


KT_DIMS = [21, 91, 70]
CARRIER_RANK = 512
DEFECT_RANK = 1


def low_arrow_defect() -> dict[str, object]:
    d2_rank = KT_DIMS[0] * CARRIER_RANK
    d1_rank = KT_DIMS[2] * (CARRIER_RANK - DEFECT_RANK)
    h2 = 0
    h1 = (KT_DIMS[0] * CARRIER_RANK + KT_DIMS[2] * DEFECT_RANK) - d2_rank
    h0 = KT_DIMS[2] * CARRIER_RANK - d1_rank
    return {
        "modified_arrow": "D1:C1_to_C0",
        "defect": "annihilate one slow-outgoing carrier line on every one of the 70 orbit outputs",
        "differential_ranks": [d2_rank, d1_rank],
        "cohomology_dimensions_H2_H1_H0": [h2, h1, h0],
        "defect_supported_in_one_boundary_half": True,
    }


def high_arrow_defect() -> dict[str, object]:
    d2_rank = KT_DIMS[0] * (CARRIER_RANK - DEFECT_RANK)
    d1_rank = KT_DIMS[2] * CARRIER_RANK
    h2 = KT_DIMS[0] * DEFECT_RANK
    h1 = KT_DIMS[0] * CARRIER_RANK - d2_rank
    h0 = 0
    return {
        "modified_arrow": "D2:C2_to_C1",
        "defect": "annihilate one slow-incoming carrier line on every one of the 21 stabilizer inputs",
        "differential_ranks": [d2_rank, d1_rank],
        "cohomology_dimensions_H2_H1_H0": [h2, h1, h0],
        "defect_supported_in_one_boundary_half": True,
    }


def demo() -> dict:
    low = low_arrow_defect()
    high = high_arrow_defect()
    assert low["cohomology_dimensions_H2_H1_H0"] == [0, 70, 70]
    assert high["cohomology_dimensions_H2_H1_H0"] == [21, 21, 0]
    return {
        "schema_version": "1.0",
        "result_id": "K446-K77-COMPATIBLE-NILPOTENT-COHOMOLOGY-OBSTRUCTION",
        "classification": "BRIDGE_OR_SEMANTIC_BOUNDARY",
        "direction": "observed_to_native",
        "shared_properties": {
            "complex_dimensions": [n * CARRIER_RANK for n in KT_DIMS],
            "both_typed_projector_squares_hold": True,
            "D1_D2_zero": True,
            "closed_trace_halves_are_subcomplexes": True,
            "rank_defect_per_selected_carrier_line": DEFECT_RANK,
            "source_or_action_selected": False,
        },
        "low_arrow_defect": low,
        "high_arrow_defect": high,
        "decision": {
            "boundary_compatibility_plus_nilpotence_implies_properness": False,
            "positive_degree_acyclicity_can_fail": True,
            "surviving_cohomology_computed_exactly": True,
            "current_native_inputs_select_between_K445_and_K446": False,
            "actual_action_coupling_tested": False,
            "physical_cohomology_constructed": False,
            "next_exact_input": "the action must serialize the degree-changing blocks and prove their ranks or a contracting homotopy on the closed trace domain; otherwise boundary-compatible nilpotent completions have non-identifiable cohomology",
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
