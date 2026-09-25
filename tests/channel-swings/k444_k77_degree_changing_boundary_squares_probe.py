#!/usr/bin/env python3
"""Independent controls and hostile mutations for K444."""

from __future__ import annotations

import copy
import json

from k444_k77_degree_changing_boundary_squares import demo


def controls(result: dict) -> list[bool]:
    theorem = result["general_theorem"]
    d21 = result["actual_arrow_counts"]["degree_2_to_1"]
    d10 = result["actual_arrow_counts"]["degree_1_to_0"]
    exact = result["exact_controls"]
    decision = result["decision"]
    return [
        result["classification"] == "BRIDGE_OR_SEMANTIC_BOUNDARY",
        result["direction"] == "observed_to_native",
        theorem["criterion_necessary_and_sufficient"] is True,
        theorem["k443_is_strict_special_case"] is True,
        d21["source_dimension"] == 10752,
        d21["target_dimension"] == 46592,
        d21["all_linear_maps_dimension"] == 500957184,
        d21["boundary_compatible_maps_dimension"] == 250478592,
        d21["off_diagonal_obstruction_dimension"] == 250478592,
        d10["source_dimension"] == 46592,
        d10["target_dimension"] == 35840,
        d10["all_linear_maps_dimension"] == 1669857280,
        d10["boundary_compatible_maps_dimension"] == 834928640,
        d10["off_diagonal_obstruction_dimension"] == 834928640,
        exact["compatible_representative_defect_rank"] == 0,
        exact["slow_exchange_representative_defect_rank"] == 2,
        exact["slow_exchange_actual_defect_rank"] == 128,
        exact["source_to_target_leak_rank"] == 64,
        exact["target_to_source_leak_rank"] == 64,
        decision["both_degree_changing_square_types_classified"] is True,
        decision["boundary_compatibility_implies_nilpotence"] is False,
        decision["boundary_compatibility_implies_properness"] is False,
        decision["actual_action_coupling_tested"] is False,
    ]


def valid(result: dict) -> bool:
    return all(controls(result))


def main() -> int:
    result = demo()
    assert valid(result)
    specs = [
        (("classification",), "SUPPORTED"),
        (("direction",), "native_to_observed"),
        (("general_theorem", "criterion_necessary_and_sufficient"), False),
        (("general_theorem", "k443_is_strict_special_case"), False),
        (("actual_arrow_counts", "degree_2_to_1", "source_dimension"), 21),
        (("actual_arrow_counts", "degree_2_to_1", "target_dimension"), 91),
        (("actual_arrow_counts", "degree_2_to_1", "all_linear_maps_dimension"), 500957183),
        (("actual_arrow_counts", "degree_2_to_1", "boundary_compatible_maps_dimension"), 250478591),
        (("actual_arrow_counts", "degree_2_to_1", "off_diagonal_obstruction_dimension"), 0),
        (("actual_arrow_counts", "degree_1_to_0", "source_dimension"), 91),
        (("actual_arrow_counts", "degree_1_to_0", "target_dimension"), 70),
        (("actual_arrow_counts", "degree_1_to_0", "all_linear_maps_dimension"), 1669857279),
        (("actual_arrow_counts", "degree_1_to_0", "boundary_compatible_maps_dimension"), 834928639),
        (("actual_arrow_counts", "degree_1_to_0", "off_diagonal_obstruction_dimension"), 0),
        (("exact_controls", "compatible_representative_defect_rank"), 1),
        (("exact_controls", "slow_exchange_representative_defect_rank"), 0),
        (("exact_controls", "slow_exchange_actual_defect_rank"), 64),
        (("exact_controls", "source_to_target_leak_rank"), 0),
        (("exact_controls", "target_to_source_leak_rank"), 0),
        (("decision", "both_degree_changing_square_types_classified"), False),
        (("decision", "boundary_compatibility_implies_nilpotence"), True),
        (("decision", "boundary_compatibility_implies_properness"), True),
        (("decision", "actual_action_coupling_tested"), True),
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
