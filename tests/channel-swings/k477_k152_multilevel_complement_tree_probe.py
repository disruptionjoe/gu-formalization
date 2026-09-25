#!/usr/bin/env python3
"""Independent controls and hostile mutations for K477."""

from __future__ import annotations

import copy
from fractions import Fraction

from k477_k152_multilevel_complement_tree import CertificateError, certify_tree, demo


def checks(packet):
    theorem, control, native = packet["theorem"], packet["four_leaf_control"], packet["native_release"]
    root = control["root"]
    return [
        packet["schema_version"] == "1.0",
        packet["result_id"] == "K477-K152-MULTILEVEL-COMPLEMENT-TREE",
        packet["classification"] == "INTERNAL_STRUCTURAL_ONLY",
        packet["direction"] == "observed_to_native",
        "every internal node" in theorem["composition"],
        "every leaf" in theorem["release"],
        "cannot supply" in theorem["ceiling"],
        control["target_threshold"] == "1",
        root["leaf_count"] == 4,
        root["internal_count"] == 3,
        root["depth"] == 2,
        root["left"]["floor_outward_interval"] == ["2", "2"],
        root["right"]["floor_outward_interval"] == ["3", "3"],
        root["cross_norm_upper"] == "1/2",
        root["cross_norm_square"] == "1/4",
        Fraction(root["floor_outward_interval"][0]) > 1,
        root["same_fixed_form"] is True,
        root["complete_partition"] is True,
        native["native_leaf_packets_present"] is False,
        native["native_cross_packets_present"] is False,
        native["native_complete_floor_emitted"] is False,
    ]


def main() -> int:
    packet = demo()
    base = checks(packet)
    mutations = [
        lambda d: d.__setitem__("classification", "PHYSICAL"),
        lambda d: d.__setitem__("direction", "native_to_observed"),
        lambda d: d["theorem"].__setitem__("composition", "one finite truncation"),
        lambda d: d["theorem"].__setitem__("release", "leaves optional"),
        lambda d: d["four_leaf_control"]["root"].__setitem__("leaf_count", 3),
        lambda d: d["four_leaf_control"]["root"].__setitem__("internal_count", 2),
        lambda d: d["four_leaf_control"]["root"].__setitem__("same_fixed_form", False),
        lambda d: d["four_leaf_control"]["root"].__setitem__("complete_partition", False),
        lambda d: d["four_leaf_control"]["root"]["left"].__setitem__("floor_outward_interval", ["1", "2"]),
        lambda d: d["native_release"].__setitem__("native_complete_floor_emitted", True),
    ]
    rejected = 0
    for mutate in mutations:
        candidate = copy.deepcopy(packet)
        mutate(candidate)
        rejected += not all(checks(candidate))
    leaf = {"floor": 3, "proof_ref": "leaf"}
    valid = {"same_fixed_form": True, "complete_partition": True, "cross_norm_upper": 1,
             "left": leaf, "right": {"floor": 4, "proof_ref": "right"}}
    invalid = 0
    cases = [
        ({"floor": 1, "proof_ref": "bad"}, 1),
        ({"floor": 3, "proof_ref": ""}, 1),
        ({**valid, "same_fixed_form": False}, 1),
        ({**valid, "complete_partition": False}, 1),
        ({**valid, "cross_norm_upper": -1}, 1),
        ({**valid, "cross_norm_upper": 4}, 1),
    ]
    for tree, threshold in cases:
        try:
            certify_tree(tree, threshold)
        except CertificateError:
            invalid += 1
    print(f"K477 EXACT CONTROL: {sum(base)}/{len(base)} pass")
    print(f"K477 HOSTILE MUTATIONS: {rejected}/{len(mutations)} rejected")
    print(f"K477 INVALID INPUTS: {invalid}/{len(cases)} rejected")
    return 0 if all(base) and rejected == len(mutations) and invalid == len(cases) else 1


if __name__ == "__main__":
    raise SystemExit(main())
