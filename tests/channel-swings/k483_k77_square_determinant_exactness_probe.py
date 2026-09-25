#!/usr/bin/env python3
"""Independent controls and hostile mutations for K483."""

from __future__ import annotations

import copy

from k483_k77_square_determinant_exactness import assess, demo, determinant, matmul, matrix


def checks(packet):
    theorem = packet["theorem"]
    exact, defect, bad = packet["exact_control"], packet["rank_defect_control"], packet["non_nilpotent_control"]
    k77 = packet["K77_application"]
    return [
        packet["result_id"] == "K483-K77-SQUARE-DETERMINANT-EXACTNESS",
        packet["classification"] == "BRIDGE_OR_SEMANTIC_BOUNDARY",
        packet["direction"] == "observed_to_native",
        "equivalent" in theorem["criterion"],
        "independent and mandatory" in theorem["necessity"],
        "selects no action" in theorem["ceiling"],
        exact["D1_D2_zero"] is True,
        exact["concatenation"] == "[D2,D1^T]",
        exact["determinant"] == "1",
        exact["concatenation_invertible"] is True,
        exact["acyclic_certified"] is True,
        defect["D1_D2_zero"] is True,
        defect["determinant"] == "0",
        defect["acyclic_certified"] is False,
        bad["D1_D2_zero"] is False,
        bad["concatenation_invertible"] is True,
        bad["acyclic_certified"] is False,
        k77["dimensions_C2_C1_C0"] == [10752, 46592, 35840],
        k77["square_certificate_size"] == 46592,
        k77["native_matrices_present"] is False,
        k77["physical_cohomology_emitted"] is False,
    ]


def main() -> int:
    packet = demo()
    base = checks(packet)
    mutations = [
        lambda d: d.__setitem__("classification", "PHYSICAL"),
        lambda d: d["theorem"].__setitem__("criterion", "determinant heuristic"),
        lambda d: d["theorem"].__setitem__("necessity", "nilpotence optional"),
        lambda d: d["theorem"].__setitem__("ceiling", "selects an action"),
        lambda d: d["exact_control"].__setitem__("determinant", "0"),
        lambda d: d["exact_control"].__setitem__("acyclic_certified", False),
        lambda d: d["rank_defect_control"].__setitem__("acyclic_certified", True),
        lambda d: d["non_nilpotent_control"].__setitem__("acyclic_certified", True),
        lambda d: d["K77_application"].__setitem__("physical_cohomology_emitted", True),
    ]
    rejected = 0
    for mutate in mutations:
        candidate = copy.deepcopy(packet)
        mutate(candidate)
        rejected += not all(checks(candidate))
    invalid = 0
    cases = [
        lambda: assess(0, 1, 1, [], [[0]]),
        lambda: assess(1, 3, 1, [[1], [0], [0]], [[0, 1, 0]]),
        lambda: assess(1, 2, 1, [[1]], [[0, 1]]),
        lambda: matrix([[1, 2]], 2, 1),
        lambda: matmul([[1, 2]], [[1, 2]]),
        lambda: determinant([[1, 2, 3], [4, 5, 6]]),
    ]
    for case in cases:
        try:
            case()
        except ValueError:
            invalid += 1
    print(f"K483 EXACT CONTROL: {sum(base)}/{len(base)} pass")
    print(f"K483 HOSTILE MUTATIONS: {rejected}/{len(mutations)} rejected")
    print(f"K483 INVALID INPUTS: {invalid}/{len(cases)} rejected")
    return 0 if all(base) and rejected == len(mutations) and invalid == len(cases) else 1


if __name__ == "__main__":
    raise SystemExit(main())
