#!/usr/bin/env python3
"""Hostile mutations for K1677."""
import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def valid(data):
    c, d = data.get("packet_bound", {}), data.get("decision", {})
    return all([
        data.get("claim_id") == "K1677", "(2n^3+n)/3" in c.get("one_dimensional_count", ""),
        ">=c_g N^4" in c.get("lower_bound", ""), "O_g(alpha^2)" in c.get("profile_transfer", ""),
        "not constant" in c.get("scope_guard", ""), d.get("exact_cardinal_identity") is True,
        d.get("real_coordinate_multiplicity_preserved") is True,
        d.get("profile_weighted_fourth_mass_order_n4") is True,
        d.get("constant_multiplier_claimed") is False,
    ])


def main():
    source = json.loads((ROOT / "lab/process/k1677-cardinal-packet-l4-lower.json").read_text())
    mutations = [
        (("claim_id",), "K1676"), (("packet_bound", "one_dimensional_count"), "unknown"),
        (("packet_bound", "lower_bound"), "o(N4)"), (("packet_bound", "profile_transfer"), "arbitrary"),
        (("packet_bound", "scope_guard"), "constant"), (("decision", "exact_cardinal_identity"), False),
        (("decision", "real_coordinate_multiplicity_preserved"), False),
        (("decision", "profile_weighted_fourth_mass_order_n4"), False),
        (("decision", "constant_multiplier_claimed"), True),
    ]
    assert valid(source)
    for number, (path, value) in enumerate(mutations, 1):
        changed = copy.deepcopy(source); cursor = changed
        for key in path[:-1]: cursor = cursor[key]
        cursor[path[-1]] = value
        assert not valid(changed), number
        print(f"REJECT {number:02d}: hostile mutation")
    print(f"RESULT: REJECTED {len(mutations)}/{len(mutations)}")


if __name__ == "__main__": main()
