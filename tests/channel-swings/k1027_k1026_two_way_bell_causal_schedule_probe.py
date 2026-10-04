#!/usr/bin/env python3
"""Hostile mutations for K1027."""
from copy import deepcopy
from k1027_k1026_two_way_bell_causal_schedule import build, validate


def main():
    mutations = [
        ("required_relations", ["A to B"]),
        ("passing_schedule.0.certified", False),
        ("passing_schedule.0.margin", 8.0),
        ("passing_schedule.1.margin", 7.0),
        ("one_way_only_control.0.certified", False),
        ("one_way_only_control.1.certified", True),
        ("decision_rule", "one direction is enough"),
        ("station_separation_warning", "station distance certifies locality"),
        ("record_requirement", "keep totals"),
        ("scope", "proves universal locality"),
        ("ownership.physical_events_recorded", True),
        ("target_claim", "SC-ACT-06"),
    ]
    caught = 0
    for path, value in mutations:
        data = deepcopy(build())
        node = data
        parts = path.split(".")
        for part in parts[:-1]:
            node = node[int(part)] if part.isdigit() else node[part]
        key = parts[-1]
        if key.isdigit(): node[int(key)] = value
        else: node[key] = value
        try: validate(data)
        except AssertionError: caught += 1
    assert caught == len(mutations)
    print(f"K1027 hostile probes: {caught}/{len(mutations)}")


if __name__ == "__main__": main()
