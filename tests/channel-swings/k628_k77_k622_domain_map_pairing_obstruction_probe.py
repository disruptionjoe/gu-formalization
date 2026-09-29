#!/usr/bin/env sage-python
"""Independent controls and hostile mutations for K628."""

from __future__ import annotations

import copy
import json

from k628_k77_k622_domain_map_pairing_obstruction import build


def controls(p: dict) -> list[bool]:
    t = p["determinant_obstruction_theorem"]
    o = p["ownership_reconciliation"]
    d = p["decision"]
    packets = p["cross_characteristic_packets"]
    return [
        p["classification"] == "BRIDGE_OR_SEMANTIC_BOUNDARY",
        p["direction"] == "observed_to_native",
        p["target_claim"] == "NONE-NOT-A-KILL",
        len(packets) == 2,
        [packet["prime"] for packet in packets] == [1009, 1013],
        all(packet["domain_map_rank"] == 128 for packet in packets),
        all(packet["checks"]["all_transport_equations_verified"] for packet in packets),
        all(packet["checks"]["both_fast_seed_images_coincide"] for packet in packets),
        all(packet["checks"]["both_fast_blocks_obstruct_every_nondegenerate_restricted_pairing"] for packet in packets),
        all(packet["checks"]["slow_outgoing_obstructs_every_nondegenerate_block_pairing"] for packet in packets),
        all(packet["checks"]["slow_incoming_identity_transport_survives"] for packet in packets),
        all(packet["checks"]["at_least_three_blocks_obstruct"] for packet in packets),
        t["obstructed_blocks"] == ["fast_outgoing", "fast_incoming", "slow_outgoing"],
        t["unobstructed_blocks"] == ["slow_incoming"],
        t["K622_serialized_domain_map_preserves_some_nondegenerate_block_pairing"] is False,
        t["K622_abstract_nonisometric_orbit_exists"] is True,
        t["every_K622_family_member_tested"] is False,
        t["alternative_domain_map_family_excluded"] is False,
        o["K622_abstract_orbit_retracted"] is False,
        o["K624_H_Sigma_obstruction_retracted"] is False,
        o["K627_gauge_nonselection_retracted"] is False,
        o["serialized_map_all_pairing_obstruction_is_action_selection"] is False,
        o["source_owned_domain_map_or_Gram_constructed"] is False,
        o["mixed_hessian_or_stationary_background_constructed"] is False,
        o["common_BV_Green_domain_constructed"] is False,
        d["K622_serialized_witness_can_be_repaired_by_only_changing_positive_Gram"] is False,
        d["broader_K622_family_pairing_orbit_decided"] is False,
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
        (("cross_characteristic_packets",), payload["cross_characteristic_packets"][:1]),
        (("determinant_obstruction_theorem", "obstructed_blocks"), ["fast_outgoing"]),
        (("determinant_obstruction_theorem", "unobstructed_blocks"), []),
        (("determinant_obstruction_theorem", "K622_serialized_domain_map_preserves_some_nondegenerate_block_pairing"), True),
        (("determinant_obstruction_theorem", "K622_abstract_nonisometric_orbit_exists"), False),
        (("determinant_obstruction_theorem", "every_K622_family_member_tested"), True),
        (("determinant_obstruction_theorem", "alternative_domain_map_family_excluded"), True),
        (("ownership_reconciliation", "K622_abstract_orbit_retracted"), True),
        (("ownership_reconciliation", "K624_H_Sigma_obstruction_retracted"), True),
        (("ownership_reconciliation", "K627_gauge_nonselection_retracted"), True),
        (("ownership_reconciliation", "serialized_map_all_pairing_obstruction_is_action_selection"), True),
        (("ownership_reconciliation", "source_owned_domain_map_or_Gram_constructed"), True),
        (("ownership_reconciliation", "mixed_hessian_or_stationary_background_constructed"), True),
        (("ownership_reconciliation", "common_BV_Green_domain_constructed"), True),
        (("decision", "K622_serialized_witness_can_be_repaired_by_only_changing_positive_Gram"), True),
        (("decision", "broader_K622_family_pairing_orbit_decided"), True),
        (("decision", "actual_K596_K598_packet_released"), True),
        (("decision", "selected_source_action_rejected"), True),
        (("source_and_ledger_effect",), "moved"),
    ]
    caught = 0
    for path, value in mutations:
        case = copy.deepcopy(payload)
        set_path(case, path, value)
        caught += int(not all(controls(case)))
    assert caught == len(mutations)
    print(json.dumps({"controls_passed": len(controls(payload)), "hostile_mutations_rejected": caught}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
