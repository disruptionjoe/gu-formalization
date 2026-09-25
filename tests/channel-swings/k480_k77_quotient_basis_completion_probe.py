#!/usr/bin/env python3
"""Independent controls and hostile mutations for K480."""

from __future__ import annotations

import copy

from k480_k77_quotient_basis_completion import assess_complex, demo, matmul, matrix


def checks(packet):
    theorem, exact, defect = packet["theorem"], packet["exact_control"], packet["rank_defect_control"]
    construction, k77 = packet["construction_control"], packet["K77_application"]
    return [
        packet["result_id"] == "K480-K77-QUOTIENT-BASIS-COMPLETION",
        packet["classification"] == "BRIDGE_OR_SEMANTIC_BOUNDARY",
        packet["direction"] == "observed_to_native",
        "full column rank" in theorem["fixed_D2"],
        "equivalent" in theorem["euler_zero"],
        "invertible A" in theorem["construction"],
        "does not select" in theorem["ceiling"],
        exact["ranks_D2_D1"] == [2, 2],
        exact["D1_D2_zero"] is True,
        exact["quotient_dimension_C1_mod_image_D2"] == 2,
        exact["homology_dimensions_H2_H1_H0"] == [0, 0, 0],
        exact["D1_descends_to_quotient_isomorphism"] is True,
        exact["acyclic"] is True,
        defect["ranks_D2_D1"] == [2, 1],
        defect["homology_dimensions_H2_H1_H0"] == [0, 1, 1],
        defect["acyclic"] is False,
        construction["det_A"] == 1,
        k77["dimensions_C2_C1_C0"] == [10752, 46592, 35840],
        k77["quotient_dimension_after_full_rank_D2"] == 35840,
        k77["required_descended_D1_rank"] == 35840,
        k77["native_D2_present"] is False,
        k77["native_D1_present"] is False,
        k77["physical_cohomology_emitted"] is False,
    ]


def main() -> int:
    packet = demo()
    base = checks(packet)
    mutations = [
        lambda d: d.__setitem__("classification", "PHYSICAL"),
        lambda d: d["theorem"].__setitem__("fixed_D2", "D2 arbitrary"),
        lambda d: d["theorem"].__setitem__("construction", "choose any D1"),
        lambda d: d["theorem"].__setitem__("ceiling", "selects the action"),
        lambda d: d["exact_control"].__setitem__("D1_D2_zero", False),
        lambda d: d["exact_control"].__setitem__("acyclic", False),
        lambda d: d["rank_defect_control"].__setitem__("acyclic", True),
        lambda d: d["construction_control"].__setitem__("det_A", 0),
        lambda d: d["K77_application"].__setitem__("physical_cohomology_emitted", True),
    ]
    rejected = 0
    for mutate in mutations:
        candidate = copy.deepcopy(packet)
        mutate(candidate)
        rejected += not all(checks(candidate))
    invalid = 0
    cases = [
        lambda: assess_complex(-1, 1, 1, [], [[0]]),
        lambda: assess_complex(1, 2, 1, [[1]], [[0, 1]]),
        lambda: assess_complex(1, 2, 1, [[1], [0]], [[0]]),
        lambda: matrix([[1, 2]], 2, 1),
        lambda: matmul([[1, 2]], [[1, 2]]),
    ]
    for case in cases:
        try:
            case()
        except ValueError:
            invalid += 1
    print(f"K480 EXACT CONTROL: {sum(base)}/{len(base)} pass")
    print(f"K480 HOSTILE MUTATIONS: {rejected}/{len(mutations)} rejected")
    print(f"K480 INVALID INPUTS: {invalid}/{len(cases)} rejected")
    return 0 if all(base) and rejected == len(mutations) and invalid == len(cases) else 1


if __name__ == "__main__":
    raise SystemExit(main())
