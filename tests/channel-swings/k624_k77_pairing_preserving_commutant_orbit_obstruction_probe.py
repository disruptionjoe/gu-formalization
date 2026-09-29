#!/usr/bin/env sage-python
"""Independent controls and hostile mutations for K624."""

from __future__ import annotations

import copy
import json

from k623_k77_constructed_orbit_pairing_defect import BLOCK_NAMES
from k624_k77_pairing_preserving_commutant_orbit_obstruction import build


def controls(p: dict) -> list[bool]:
    t = p["simultaneous_congruence_theorem"]
    o = p["ownership_reconciliation"]
    d = p["decision"]
    packets = p["cross_characteristic_packets"]
    return [
        p["classification"] == "BRIDGE_OR_SEMANTIC_BOUNDARY",
        p["direction"] == "observed_to_native",
        p["target_claim"] == "NONE-NOT-A-KILL",
        len(packets) == 2,
        all(packet["block_order"] == list(BLOCK_NAMES) for packet in packets),
        all(packet["zero_seed"]["total_rank"] == 128 for packet in packets),
        all(packet["moving_seed"]["total_rank"] == 128 for packet in packets),
        all(packet["zero_seed"]["block_gram_ranks"] == [128, 128, 64, 64] for packet in packets),
        all(packet["moving_seed"]["block_gram_ranks"] == [128, 128, 64, 64] for packet in packets),
        all(
            all(row["trace_power_1_delta"] != 0 for row in packet["similarity_invariant_mismatches"])
            for packet in packets
        ),
        t["total_pullback_forms_are_nondegenerate"] is True,
        t["trace_is_similarity_invariant"] is True,
        t["all_four_first_traces_mismatch_at_both_primes"] is True,
        t["projector_pairing_preserving_commutant_and_domain_orbit_exists"] is False,
        t["abstract_nonisometric_K622_orbit_exists"] is True,
        t["pairing_model"] == "projector_induced_H_Sigma",
        t["K441_factorized_pairing_identification_serialized"] is False,
        o["K621_fixed_domain_obstruction_retracted"] is False,
        o["K622_abstract_orbit_equivalence_retracted"] is False,
        o["K623_specific_witness_failure_strengthened"] is True,
        o["projector_pairing_preserving_same_data_repair_excluded"] is True,
        o["different_action_owned_mixed_hessian_excluded"] is False,
        o["common_BV_Green_domain_constructed"] is False,
        o["nonzero_stationary_background_constructed"] is False,
        d["current_seed_identification_can_preserve_projector_pairing"] is False,
        d["K441_pairing_preservation_decided"] is False,
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
        (("target_claim",), "SC-CHI-51"),
        (("simultaneous_congruence_theorem", "total_pullback_forms_are_nondegenerate"), False),
        (("simultaneous_congruence_theorem", "trace_is_similarity_invariant"), False),
        (("simultaneous_congruence_theorem", "all_four_first_traces_mismatch_at_both_primes"), False),
        (("simultaneous_congruence_theorem", "projector_pairing_preserving_commutant_and_domain_orbit_exists"), True),
        (("simultaneous_congruence_theorem", "abstract_nonisometric_K622_orbit_exists"), False),
        (("simultaneous_congruence_theorem", "K441_factorized_pairing_identification_serialized"), True),
        (("ownership_reconciliation", "K621_fixed_domain_obstruction_retracted"), True),
        (("ownership_reconciliation", "K622_abstract_orbit_equivalence_retracted"), True),
        (("ownership_reconciliation", "K623_specific_witness_failure_strengthened"), False),
        (("ownership_reconciliation", "projector_pairing_preserving_same_data_repair_excluded"), False),
        (("ownership_reconciliation", "different_action_owned_mixed_hessian_excluded"), True),
        (("ownership_reconciliation", "common_BV_Green_domain_constructed"), True),
        (("ownership_reconciliation", "nonzero_stationary_background_constructed"), True),
        (("decision", "current_seed_identification_can_preserve_projector_pairing"), True),
        (("decision", "K441_pairing_preservation_decided"), True),
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
