#!/usr/bin/env python3
"""Hostile mutations for K1174."""
from copy import deepcopy
from k1174_factor_through_gauge_descendant_boundary import build, validate


def main():
    mutations = [
        ("theorem", None, "descendants add rank"), ("base_gauge_rank", None, 3),
        ("factor_through_combined_rank", None, 3), ("gauge_for_gauge_dimension", None, 0),
        ("independent_added_rank", None, 1), ("combined_with_independent_rank", None, 3),
        ("nonnull_pure_gauge_total_rank_floor", None, 98375), ("null_pure_gauge_total_rank_floor", None, 106539),
        ("factor_through_descendants_change_deficit", None, True), ("decision", None, "derivatives repair K132"),
        ("scope_boundary", None, "global absence theorem"),
    ]
    caught = 0
    for key, _, value in mutations:
        d = deepcopy(build())
        if key in d["exact_control"]: d["exact_control"][key] = value
        elif key in d["k132_application"]: d["k132_application"][key] = value
        else: d[key] = value
        try: validate(d)
        except (AssertionError, KeyError): caught += 1
    assert caught == 11
    print("K1174 hostile probes: 11/11")


if __name__ == "__main__": main()
