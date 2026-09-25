#!/usr/bin/env python3
"""Independent controls and hostile mutations for K479."""

from __future__ import annotations

import copy

from k479_k77_unique_path_nilpotence_sieve import analyze_support, demo


def checks(packet):
    theorem, controls, k77 = packet["theorem"], packet["controls"], packet["K77_application"]
    possible = controls["cancellation_possible_support"]
    blocked = controls["unique_path_obstruction"]
    return [
        packet["result_id"] == "K479-K77-UNIQUE-PATH-NILPOTENCE-SIEVE",
        packet["classification"] == "BRIDGE_OR_SEMANTIC_BOUNDARY",
        packet["direction"] == "observed_to_native",
        "exactly one" in theorem["obstruction"],
        "at least two" in theorem["necessary_support_rule"],
        "do not prove" in theorem["ceiling"],
        possible["nonzero_two_step_pairs"] == 4,
        possible["unique_path_obstruction_count"] == 0,
        possible["support_nilpotence_possible"] is True,
        possible["nilpotence_proved"] is False,
        blocked["unique_path_obstruction_count"] == 1,
        blocked["unique_path_obstructions"][0] == {"source": 0, "target": 0, "path_count": 1, "middle_witnesses": [0]},
        blocked["support_nilpotence_possible"] is False,
        blocked["cancellation_coefficients_solved"] is False,
        k77["D2_shape"] == [46592, 10752],
        k77["D1_shape"] == [35840, 46592],
        k77["native_support_present"] is False,
        k77["native_nilpotence_emitted"] is False,
    ]


def main() -> int:
    packet = demo()
    base = checks(packet)
    mutations = [
        lambda d: d.__setitem__("classification", "PHYSICAL"),
        lambda d: d["theorem"].__setitem__("obstruction", "one path may cancel itself"),
        lambda d: d["theorem"].__setitem__("necessary_support_rule", "one path is enough"),
        lambda d: d["theorem"].__setitem__("ceiling", "support proves nilpotence"),
        lambda d: d["controls"]["cancellation_possible_support"].__setitem__("nilpotence_proved", True),
        lambda d: d["controls"]["unique_path_obstruction"].__setitem__("unique_path_obstruction_count", 0),
        lambda d: d["controls"]["unique_path_obstruction"].__setitem__("support_nilpotence_possible", True),
        lambda d: d["K77_application"].__setitem__("native_support_present", True),
    ]
    rejected = 0
    for mutate in mutations:
        candidate = copy.deepcopy(packet)
        mutate(candidate)
        rejected += not all(checks(candidate))
    invalid = 0
    cases = [
        (-1, 1, 1, [], [[0]], True),
        (1, 1, 1, [], [[0]], True),
        (1, 1, 1, [[1]], [[0]], True),
        (1, 1, 1, [[0]], [[1]], True),
        (1, 1, 1, [[0]], [[0]], False),
    ]
    for args in cases:
        try:
            analyze_support(*args)
        except ValueError:
            invalid += 1
    print(f"K479 EXACT CONTROL: {sum(base)}/{len(base)} pass")
    print(f"K479 HOSTILE MUTATIONS: {rejected}/{len(mutations)} rejected")
    print(f"K479 INVALID INPUTS: {invalid}/{len(cases)} rejected")
    return 0 if all(base) and rejected == len(mutations) and invalid == len(cases) else 1


if __name__ == "__main__":
    raise SystemExit(main())
