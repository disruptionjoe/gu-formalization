#!/usr/bin/env python3
"""Independent controls and hostile mutations for K433."""

from __future__ import annotations

import copy
import json

from k433_k77_observed_boundary_holonomy_obstruction import demo


def checks(result: dict) -> list[bool]:
    theorem = result["cross_carrier_theorem"]
    bulk = result["exact_bulk_fixture"]
    cases = result["exact_cases"]
    matched = cases["matched_monodromy"]
    conjugate = cases["matched_conjugate"]
    mismatch = cases["mismatched_opposite_scalar"]
    obstruction = result["scoped_obstruction"]
    decision = result["decision"]
    return [
        result["classification"] == "BRIDGE_OR_SEMANTIC_BOUNDARY",
        result["direction"] == "native_to_observed",
        theorem["boundary_criterion"]
        == "B maps Dom(D_E,R_E) to Dom(D_F,R_F) iff C S_E=S_F C",
        theorem["invertible_criterion"]
        == "an invertible parallel boundary intertwiner exists iff S_E and S_F are conjugate",
        bulk["target_connection"] == "A_F(t)=0",
        bulk["map"] == "B(t)=H U(t)^T",
        bulk["map_invertible"] is True,
        bulk["bulk_covariant_intertwining_exact"] is True,
        matched["source_relative_holonomy"] == [["1", "0"], ["0", "1"]],
        matched["target_relative_holonomy"] == [["1", "0"], ["0", "1"]],
        matched["chosen_map_boundary_compatible"] is True,
        matched["parallel_boundary_intertwiner_space_dimension"] == 4,
        conjugate["source_relative_holonomy"] == [["0", "1"], ["-1", "0"]],
        conjugate["target_relative_holonomy"] == [["0", "-1"], ["1", "0"]],
        conjugate["chosen_map_boundary_compatible"] is True,
        conjugate["parallel_boundary_intertwiner_space_dimension"] == 2,
        mismatch["source_relative_holonomy"] == [["1", "0"], ["0", "1"]],
        mismatch["target_relative_holonomy"] == [["-1", "0"], ["0", "-1"]],
        mismatch["chosen_map_boundary_compatible"] is False,
        mismatch["parallel_boundary_intertwiner_space_dimension"] == 0,
        obstruction["only_parallel_boundary_intertwiner"] == "zero map",
        obstruction["bulk_intertwiner_still_exists"] is True,
        obstruction["obstruction_is_boundary_relative_not_bulk"] is True,
        decision["cross_carrier_boundary_compatibility_classified"] is True,
        decision["endpoint_twists_alone_are_not_the_invariant"] is True,
        decision["relative_holonomy_conjugacy_controls_invertible_descent"] is True,
        decision["mismatched_case_blocks_every_nonzero_parallel_boundary_map"] is True,
        decision["actual_corrected_observation_carrier_identified"] is False,
        decision["physical_boundary_projector_or_bfv_map_constructed"] is False,
    ]


def valid(result: dict) -> bool:
    return all(checks(result))


def main() -> int:
    result = demo()
    asserted_controls = checks(result)
    assert len(asserted_controls) == 29 and all(asserted_controls)
    mutations = []
    for path, value in [
        (("classification",), "SOURCE_NATIVE_ROUTE"),
        (("direction",), "observed_to_native"),
        (("cross_carrier_theorem", "boundary_criterion"), "endpoint twists must be equal"),
        (("cross_carrier_theorem", "invertible_criterion"), "always"),
        (("exact_bulk_fixture", "target_connection"), "A_F=A_E"),
        (("exact_bulk_fixture", "map"), "B(t)=H"),
        (("exact_bulk_fixture", "map_invertible"), False),
        (("exact_bulk_fixture", "bulk_covariant_intertwining_exact"), False),
        (("exact_cases", "matched_monodromy", "chosen_map_boundary_compatible"), False),
        (("exact_cases", "matched_monodromy", "parallel_boundary_intertwiner_space_dimension"), 0),
        (("exact_cases", "matched_conjugate", "chosen_map_boundary_compatible"), False),
        (("exact_cases", "matched_conjugate", "parallel_boundary_intertwiner_space_dimension"), 4),
        (("exact_cases", "mismatched_opposite_scalar", "chosen_map_boundary_compatible"), True),
        (("exact_cases", "mismatched_opposite_scalar", "parallel_boundary_intertwiner_space_dimension"), 1),
        (("scoped_obstruction", "only_parallel_boundary_intertwiner"), "H"),
        (("scoped_obstruction", "bulk_intertwiner_still_exists"), False),
        (("scoped_obstruction", "obstruction_is_boundary_relative_not_bulk"), False),
        (("decision", "cross_carrier_boundary_compatibility_classified"), False),
        (("decision", "endpoint_twists_alone_are_not_the_invariant"), False),
        (("decision", "relative_holonomy_conjugacy_controls_invertible_descent"), False),
        (("decision", "mismatched_case_blocks_every_nonzero_parallel_boundary_map"), False),
        (("decision", "actual_corrected_observation_carrier_identified"), True),
        (("decision", "physical_boundary_projector_or_bfv_map_constructed"), True),
    ]:
        candidate = copy.deepcopy(result)
        target = candidate
        for key in path[:-1]:
            target = target[key]
        target[path[-1]] = value
        mutations.append(candidate)
    rejected = sum(not valid(candidate) for candidate in mutations)
    assert rejected == len(mutations)
    print(json.dumps({"controls_passed": len(asserted_controls), "hostile_mutations_rejected": rejected}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
