#!/usr/bin/env sage-python
"""Independent controls and hostile mutations for K630."""

from __future__ import annotations

import copy
import json

from k630_k77_determinant_line_gauge_invariance import build


def controls(p: dict) -> list[bool]:
    t = p["gauge_invariance_theorem"]
    o = p["ownership_reconciliation"]
    d = p["decision"]
    return [
        p["classification"] == "BRIDGE_OR_SEMANTIC_BOUNDARY",
        p["direction"] == "observed_to_native",
        p["target_claim"] == "NONE-NOT-A-KILL",
        len(p["cross_characteristic_packets"]) == 2,
        t["invariant_slow_ratio_squares"] == [949, 1004],
        t["all_tested_source_and_ambient_gauges_preserve_obstruction"] is True,
        t["K629_family_obstruction_is_coordinate_artifact"] is False,
        t["K628_serialized_row_basis_witness_is_required_for_K629"] is False,
        all(packet["checks"]["combined_slow_ratio_is_invariant"] for packet in p["cross_characteristic_packets"]),
        all(packet["checks"]["fast_transports_transform_by_source_conjugacy"] for packet in p["cross_characteristic_packets"]),
        all(packet["checks"]["fast_determinants_are_invariant"] for packet in p["cross_characteristic_packets"]),
        all(packet["checks"]["at_least_one_fast_serialization_changes"] for packet in p["cross_characteristic_packets"]),
        all(packet["checks"]["slow_fast_obstruction_ratios_are_invariant"] for packet in p["cross_characteristic_packets"]),
        all(packet["checks"]["nonunit_obstruction_survives_every_tested_gauge"] for packet in p["cross_characteristic_packets"]),
        o["K629_family_obstruction_retracted"] is False,
        o["ambient_gauge_invariance_selects_a_positive_Gram"] is False,
        o["source_coordinate_invariance_selects_a_source_endomorphism"] is False,
        o["mixed_hessian_or_stationary_background_constructed"] is False,
        o["common_BV_Green_domain_constructed"] is False,
        d["K629_obstruction_survives_allowed_coordinate_changes"] is True,
        d["admissible_common_basis_or_pivot_change_reopens_K622_pairing_family"] is False,
        d["actual_K596_K598_packet_released"] is False,
        d["selected_source_action_rejected"] is False,
        p["source_and_ledger_effect"] == "none",
    ]


def mutate(p: dict, path: tuple[object, ...], value: object) -> None:
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
        (("gauge_invariance_theorem", "invariant_slow_ratio_squares"), [1, 1]),
        (("gauge_invariance_theorem", "all_tested_source_and_ambient_gauges_preserve_obstruction"), False),
        (("gauge_invariance_theorem", "K629_family_obstruction_is_coordinate_artifact"), True),
        (("gauge_invariance_theorem", "K628_serialized_row_basis_witness_is_required_for_K629"), True),
        (("cross_characteristic_packets", 0, "checks", "combined_slow_ratio_is_invariant"), False),
        (("cross_characteristic_packets", 0, "checks", "fast_transports_transform_by_source_conjugacy"), False),
        (("cross_characteristic_packets", 1, "checks", "fast_determinants_are_invariant"), False),
        (("cross_characteristic_packets", 1, "checks", "at_least_one_fast_serialization_changes"), False),
        (("cross_characteristic_packets", 1, "checks", "slow_fast_obstruction_ratios_are_invariant"), False),
        (("cross_characteristic_packets", 1, "checks", "nonunit_obstruction_survives_every_tested_gauge"), False),
        (("ownership_reconciliation", "K629_family_obstruction_retracted"), True),
        (("ownership_reconciliation", "ambient_gauge_invariance_selects_a_positive_Gram"), True),
        (("ownership_reconciliation", "source_coordinate_invariance_selects_a_source_endomorphism"), True),
        (("ownership_reconciliation", "mixed_hessian_or_stationary_background_constructed"), True),
        (("ownership_reconciliation", "common_BV_Green_domain_constructed"), True),
        (("decision", "K629_obstruction_survives_allowed_coordinate_changes"), False),
        (("decision", "admissible_common_basis_or_pivot_change_reopens_K622_pairing_family"), True),
        (("decision", "actual_K596_K598_packet_released"), True),
        (("decision", "selected_source_action_rejected"), True),
        (("source_and_ledger_effect",), "moved"),
    ]
    caught = 0
    for path, value in mutations:
        case = copy.deepcopy(payload)
        mutate(case, path, value)
        caught += int(not all(controls(case)))
    assert caught == len(mutations)
    print(json.dumps({"controls_passed": len(controls(payload)), "hostile_mutations_rejected": caught}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
