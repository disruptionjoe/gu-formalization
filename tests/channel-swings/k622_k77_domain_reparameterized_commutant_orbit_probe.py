#!/usr/bin/env sage-python
"""Independent controls and hostile mutations for K622."""

from __future__ import annotations

import copy
import json

from k622_k77_domain_reparameterized_commutant_orbit import build


def controls(p: dict) -> list[bool]:
    t = p["orbit_theorem"]
    o = p["ownership_reconciliation"]
    d = p["decision"]
    rows = p["eigenblock_fingerprint"]
    return [
        p["classification"] == "BRIDGE_OR_SEMANTIC_BOUNDARY",
        p["direction"] == "observed_to_native",
        p["target_claim"] == "NONE-NOT-A-KILL",
        len(p["cross_characteristic_packets"]) == 2,
        all(packet["domain_reparameterization_rank"] == 128 for packet in p["cross_characteristic_packets"]),
        all(packet["checks"]["domain_reparameterization_matches_both_slow_rows"] for packet in p["cross_characteristic_packets"]),
        t["zero_seed_slow_row_pair_is_direct_sum"] is True,
        t["moving_seed_slow_row_pair_is_direct_sum"] is True,
        t["one_invertible_domain_reparameterization_matches_both_slow_rows"] is True,
        t["fast_rows_remain_full_after_reparameterization"] is True,
        t["invertible_commutant_and_domain_orbit_equivalence_exists"] is True,
        t["fixed_domain_commutant_adapter_exists"] is False,
        t["block_transport_affine_freedom_for_constructed_domain_map"] == 24576,
        t["orbit_equivalence_selects_unique_adapter"] is False,
        all(row["row_spaces_equal_after_domain_map"] for row in rows.values()),
        all(row["invertible_block_transport_exists"] for row in rows.values()),
        rows["fast_outgoing"]["block_transport_solution_affine_dimension"] == 12288,
        rows["fast_incoming"]["block_transport_solution_affine_dimension"] == 12288,
        rows["slow_outgoing"]["block_transport_solution_affine_dimension"] == 0,
        rows["slow_incoming"]["block_transport_solution_affine_dimension"] == 0,
        o["K621_fixed_domain_obstruction_retracted"] is False,
        o["domain_reparameterization_is_source_selected"] is False,
        o["commutant_transport_is_action_selected"] is False,
        o["orbit_equivalence_identifies_seed_constructions"] is False,
        o["pairing_or_Green_domain_preservation_proved"] is False,
        o["mixed_hessian_or_stationary_background_constructed"] is False,
        d["K619_common_module_retracted"] is False,
        d["full_abstract_commutant_orbit_is_nonempty"] is True,
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
        (("orbit_theorem", "zero_seed_slow_row_pair_is_direct_sum"), False),
        (("orbit_theorem", "moving_seed_slow_row_pair_is_direct_sum"), False),
        (("orbit_theorem", "one_invertible_domain_reparameterization_matches_both_slow_rows"), False),
        (("orbit_theorem", "fast_rows_remain_full_after_reparameterization"), False),
        (("orbit_theorem", "invertible_commutant_and_domain_orbit_equivalence_exists"), False),
        (("orbit_theorem", "fixed_domain_commutant_adapter_exists"), True),
        (("orbit_theorem", "block_transport_affine_freedom_for_constructed_domain_map"), 0),
        (("orbit_theorem", "orbit_equivalence_selects_unique_adapter"), True),
        (("eigenblock_fingerprint", "fast_outgoing", "row_spaces_equal_after_domain_map"), False),
        (("eigenblock_fingerprint", "fast_incoming", "invertible_block_transport_exists"), False),
        (("eigenblock_fingerprint", "fast_outgoing", "block_transport_solution_affine_dimension"), 0),
        (("eigenblock_fingerprint", "fast_incoming", "block_transport_solution_affine_dimension"), 0),
        (("eigenblock_fingerprint", "slow_outgoing", "block_transport_solution_affine_dimension"), 1),
        (("eigenblock_fingerprint", "slow_incoming", "block_transport_solution_affine_dimension"), 1),
        (("ownership_reconciliation", "K621_fixed_domain_obstruction_retracted"), True),
        (("ownership_reconciliation", "domain_reparameterization_is_source_selected"), True),
        (("ownership_reconciliation", "commutant_transport_is_action_selected"), True),
        (("ownership_reconciliation", "orbit_equivalence_identifies_seed_constructions"), True),
        (("ownership_reconciliation", "pairing_or_Green_domain_preservation_proved"), True),
        (("ownership_reconciliation", "mixed_hessian_or_stationary_background_constructed"), True),
        (("decision", "K619_common_module_retracted"), True),
        (("decision", "full_abstract_commutant_orbit_is_nonempty"), False),
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
