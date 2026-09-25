#!/usr/bin/env python3
"""Independent controls and hostile mutations for K446."""

from __future__ import annotations

import copy
import json

from k446_k77_compatible_nilpotent_cohomology_obstruction import demo


def controls(result: dict) -> list[bool]:
    shared = result["shared_properties"]
    low = result["low_arrow_defect"]
    high = result["high_arrow_defect"]
    decision = result["decision"]
    return [
        result["classification"] == "BRIDGE_OR_SEMANTIC_BOUNDARY",
        result["direction"] == "observed_to_native",
        shared["complex_dimensions"] == [10752, 46592, 35840],
        shared["both_typed_projector_squares_hold"] is True,
        shared["D1_D2_zero"] is True,
        shared["closed_trace_halves_are_subcomplexes"] is True,
        shared["rank_defect_per_selected_carrier_line"] == 1,
        shared["source_or_action_selected"] is False,
        low["differential_ranks"] == [10752, 35770],
        low["cohomology_dimensions_H2_H1_H0"] == [0, 70, 70],
        low["defect_supported_in_one_boundary_half"] is True,
        high["differential_ranks"] == [10731, 35840],
        high["cohomology_dimensions_H2_H1_H0"] == [21, 21, 0],
        high["defect_supported_in_one_boundary_half"] is True,
        decision["boundary_compatibility_plus_nilpotence_implies_properness"] is False,
        decision["positive_degree_acyclicity_can_fail"] is True,
        decision["surviving_cohomology_computed_exactly"] is True,
        decision["current_native_inputs_select_between_K445_and_K446"] is False,
        decision["actual_action_coupling_tested"] is False,
        decision["physical_cohomology_constructed"] is False,
    ]


def valid(result: dict) -> bool:
    return all(controls(result))


def main() -> int:
    result = demo()
    assert valid(result)
    specs = [
        (("classification",), "SUPPORTED"),
        (("direction",), "native_to_observed"),
        (("shared_properties", "complex_dimensions"), [21, 91, 70]),
        (("shared_properties", "both_typed_projector_squares_hold"), False),
        (("shared_properties", "D1_D2_zero"), False),
        (("shared_properties", "closed_trace_halves_are_subcomplexes"), False),
        (("shared_properties", "rank_defect_per_selected_carrier_line"), 0),
        (("shared_properties", "source_or_action_selected"), True),
        (("low_arrow_defect", "differential_ranks"), [10752, 35840]),
        (("low_arrow_defect", "cohomology_dimensions_H2_H1_H0"), [0, 0, 0]),
        (("low_arrow_defect", "defect_supported_in_one_boundary_half"), False),
        (("high_arrow_defect", "differential_ranks"), [10752, 35840]),
        (("high_arrow_defect", "cohomology_dimensions_H2_H1_H0"), [0, 0, 0]),
        (("high_arrow_defect", "defect_supported_in_one_boundary_half"), False),
        (("decision", "boundary_compatibility_plus_nilpotence_implies_properness"), True),
        (("decision", "positive_degree_acyclicity_can_fail"), False),
        (("decision", "surviving_cohomology_computed_exactly"), False),
        (("decision", "current_native_inputs_select_between_K445_and_K446"), True),
        (("decision", "actual_action_coupling_tested"), True),
        (("decision", "physical_cohomology_constructed"), True),
    ]
    rejected = 0
    for path, value in specs:
        candidate = copy.deepcopy(result)
        target = candidate
        for key in path[:-1]:
            target = target[key]
        target[path[-1]] = value
        rejected += int(not valid(candidate))
    assert rejected == len(specs)
    print(json.dumps({"controls_passed": len(controls(result)), "hostile_mutations_rejected": rejected}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
