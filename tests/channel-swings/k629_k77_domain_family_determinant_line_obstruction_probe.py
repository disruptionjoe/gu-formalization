#!/usr/bin/env sage-python
"""Independent controls and hostile mutations for K629."""

from __future__ import annotations

import copy
import json

from k629_k77_domain_family_determinant_line_obstruction import build


def controls(p: dict) -> list[bool]:
    t = p["determinant_line_theorem"]
    o = p["ownership_reconciliation"]
    d = p["decision"]
    return [
        p["classification"] == "BRIDGE_OR_SEMANTIC_BOUNDARY",
        p["direction"] == "observed_to_native",
        p["target_claim"] == "NONE-NOT-A-KILL",
        len(p["cross_characteristic_packets"]) == 2,
        t["family_parameter_group_dimension"] == 8192,
        t["combined_slow_ratio_squares"] == [949, 1004],
        t["both_fast_ratio_squares"] == [1, 1],
        t["every_K622_family_member_tested"] is True,
        t["alternative_domain_map_family_excluded_for_simultaneous_nondegenerate_block_isometry"] is True,
        t["positive_block_pairing_is_a_strict_excluded_subclass"] is True,
        t["K622_abstract_nonisometric_orbit_exists"] is True,
        all(packet["checks"]["both_slow_pairs_are_isomorphisms"] for packet in p["cross_characteristic_packets"]),
        all(packet["checks"]["both_fast_images_are_common_rank_128_subspaces"] for packet in p["cross_characteristic_packets"]),
        all(packet["checks"]["slow_pair_ratio_square_is_not_one"] for packet in p["cross_characteristic_packets"]),
        all(packet["checks"]["simultaneous_nondegenerate_block_isometry_is_impossible"] for packet in p["cross_characteristic_packets"]),
        o["K622_abstract_orbit_retracted"] is False,
        o["family_wide_pairing_obstruction_is_action_selection"] is False,
        o["source_owned_domain_map_or_Gram_constructed"] is False,
        o["mixed_hessian_or_stationary_background_constructed"] is False,
        o["common_BV_Green_domain_constructed"] is False,
        d["broader_K622_family_pairing_orbit_decided"] is True,
        d["K622_family_contains_pairing_preserving_repair"] is False,
        d["actual_K596_K598_packet_released"] is False,
        d["selected_source_action_rejected"] is False,
        p["source_and_ledger_effect"] == "none",
    ]


def set_path(p: dict, path: tuple[str, ...], value: object) -> None:
    cursor = p
    for key in path[:-1]:
        cursor = cursor[key]
    cursor[path[-1]] = value


def main() -> int:
    payload = build()
    assert all(controls(payload))
    mutations = [
        (("classification",), "SUPPORTED"),
        (("direction",), "native_to_observed"),
        (("target_claim",), "SC-ACT-01"),
        (("determinant_line_theorem", "family_parameter_group_dimension"), 4096),
        (("determinant_line_theorem", "combined_slow_ratio_squares"), [1, 1]),
        (("determinant_line_theorem", "both_fast_ratio_squares"), [949, 1004]),
        (("determinant_line_theorem", "every_K622_family_member_tested"), False),
        (("determinant_line_theorem", "alternative_domain_map_family_excluded_for_simultaneous_nondegenerate_block_isometry"), False),
        (("determinant_line_theorem", "positive_block_pairing_is_a_strict_excluded_subclass"), False),
        (("determinant_line_theorem", "K622_abstract_nonisometric_orbit_exists"), False),
        (("cross_characteristic_packets", "0", "checks", "both_slow_pairs_are_isomorphisms"), False),
        (("cross_characteristic_packets", "0", "checks", "slow_pair_ratio_square_is_not_one"), False),
        (("cross_characteristic_packets", "1", "checks", "simultaneous_nondegenerate_block_isometry_is_impossible"), False),
        (("ownership_reconciliation", "K622_abstract_orbit_retracted"), True),
        (("ownership_reconciliation", "family_wide_pairing_obstruction_is_action_selection"), True),
        (("ownership_reconciliation", "source_owned_domain_map_or_Gram_constructed"), True),
        (("ownership_reconciliation", "mixed_hessian_or_stationary_background_constructed"), True),
        (("ownership_reconciliation", "common_BV_Green_domain_constructed"), True),
        (("decision", "broader_K622_family_pairing_orbit_decided"), False),
        (("decision", "K622_family_contains_pairing_preserving_repair"), True),
        (("decision", "actual_K596_K598_packet_released"), True),
        (("decision", "selected_source_action_rejected"), True),
        (("source_and_ledger_effect",), "moved"),
    ]
    caught = 0
    for path, value in mutations:
        case = copy.deepcopy(payload)
        cursor = case
        for key in path[:-1]:
            cursor = cursor[int(key)] if isinstance(cursor, list) else cursor[key]
        key = path[-1]
        if isinstance(cursor, list):
            cursor[int(key)] = value
        else:
            cursor[key] = value
        caught += int(not all(controls(case)))
    assert caught == len(mutations)
    print(json.dumps({"controls_passed": len(controls(payload)), "hostile_mutations_rejected": caught}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
