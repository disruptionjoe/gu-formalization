#!/usr/bin/env python3
"""Independent controls and hostile mutations for K445."""

from __future__ import annotations

import copy
import json

from k445_k77_compatible_acyclic_coupling_family import demo


def controls(result: dict) -> list[bool]:
    construction = result["construction"]
    exact = result["exact_checks"]
    homology = result["homology"]
    decision = result["decision"]
    return [
        result["classification"] == "BRIDGE_OR_SEMANTIC_BOUNDARY",
        result["direction"] == "native_to_observed",
        construction["nontrivial_on_every_boundary_block"] is True,
        construction["source_or_action_selected"] is False,
        exact["D2_block_ratios"] == ["11/2", "13/3", "17/5", "19/7"],
        exact["D1_block_ratios"] == ["23/11", "29/13", "31/17", "37/19"],
        exact["G2_commutes_with_P2"] is True,
        exact["G1_commutes_with_P1"] is True,
        exact["G0_commutes_with_P0"] is True,
        exact["P1_D2_equals_D2_P2"] is True,
        exact["P0_D1_equals_D1_P1"] is True,
        exact["D1_D2_zero"] is True,
        exact["transported_contraction_identity"] is True,
        homology["complex_dimensions"] == [10752, 46592, 35840],
        homology["differential_ranks"] == [10752, 35840],
        homology["cohomology_dimensions"] == [0, 0, 0],
        homology["positive_degree_acyclic"] is True,
        homology["closed_trace_halves_are_subcomplexes"] is True,
        decision["nontrivial_boundary_compatible_nilpotent_completion_exists"] is True,
        decision["acyclicity_preserved_by_chain_isomorphism"] is True,
        decision["boundary_square_alone_selects_this_family"] is False,
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
        (("direction",), "observed_to_native"),
        (("construction", "nontrivial_on_every_boundary_block"), False),
        (("construction", "source_or_action_selected"), True),
        (("exact_checks", "D2_block_ratios"), ["1", "1", "1", "1"]),
        (("exact_checks", "D1_block_ratios"), ["1", "1", "1", "1"]),
        (("exact_checks", "G2_commutes_with_P2"), False),
        (("exact_checks", "G1_commutes_with_P1"), False),
        (("exact_checks", "G0_commutes_with_P0"), False),
        (("exact_checks", "P1_D2_equals_D2_P2"), False),
        (("exact_checks", "P0_D1_equals_D1_P1"), False),
        (("exact_checks", "D1_D2_zero"), False),
        (("exact_checks", "transported_contraction_identity"), False),
        (("homology", "complex_dimensions"), [21, 91, 70]),
        (("homology", "differential_ranks"), [21, 70]),
        (("homology", "cohomology_dimensions"), [0, 1, 0]),
        (("homology", "positive_degree_acyclic"), False),
        (("homology", "closed_trace_halves_are_subcomplexes"), False),
        (("decision", "nontrivial_boundary_compatible_nilpotent_completion_exists"), False),
        (("decision", "acyclicity_preserved_by_chain_isomorphism"), False),
        (("decision", "boundary_square_alone_selects_this_family"), True),
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
