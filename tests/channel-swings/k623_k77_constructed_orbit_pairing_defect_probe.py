#!/usr/bin/env sage-python
"""Independent controls and hostile mutations for K623."""

from __future__ import annotations

import copy
import json

from k623_k77_constructed_orbit_pairing_defect import BLOCK_NAMES, build


def controls(p: dict) -> list[bool]:
    t = p["pairing_theorem"]
    o = p["ownership_reconciliation"]
    d = p["decision"]
    rows = p["eigenblock_pairing_fingerprint"]
    return [
        p["classification"] == "BRIDGE_OR_SEMANTIC_BOUNDARY",
        p["direction"] == "observed_to_native",
        p["target_claim"] == "NONE-NOT-A-KILL",
        len(p["cross_characteristic_packets"]) == 2,
        all(packet["domain_reparameterization_rank"] == 128 for packet in p["cross_characteristic_packets"]),
        all(packet["domain_orthogonality_defect_rank"] == 96 for packet in p["cross_characteristic_packets"]),
        all(packet["projector_pairing_rank"] == 512 for packet in p["cross_characteristic_packets"]),
        t["domain_orthogonality_defect_rank"] == 96,
        t["block_pullback_gram_defect_ranks"] == [128, 128, 64, 0],
        t["block_order"] == list(BLOCK_NAMES),
        t["three_of_four_necessary_gram_identities_fail"] is True,
        t["K622_constructed_orbit_preserves_projector_pairing"] is False,
        t["arbitrary_domain_map_and_projector_pairing_isometric_orbit_excluded"] is False,
        t["projector_pairing_is_action_self_adjoint"] is True,
        t["projector_pairing_identified_with_K441_factorized_pairing"] is False,
        rows["fast_outgoing"]["pullback_gram_defect_rank"] == 128,
        rows["fast_incoming"]["pullback_gram_defect_rank"] == 128,
        rows["slow_outgoing"]["pullback_gram_defect_rank"] == 64,
        rows["slow_incoming"]["pullback_gram_defect_rank"] == 0,
        rows["slow_incoming"]["projector_pairing_isometry_necessary_gram_identity"] is True,
        o["K622_abstract_orbit_equivalence_retracted"] is False,
        o["K622_constructed_domain_map_is_source_selected"] is False,
        o["pairing_failure_supplies_action_owned_adapter"] is False,
        o["common_BV_Green_domain_constructed"] is False,
        o["nonzero_stationary_background_constructed"] is False,
        d["constructed_K622_witness_passes_pairing_gate"] is False,
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
        (("target_claim",), "SC-ACT-01"),
        (("pairing_theorem", "domain_orthogonality_defect_rank"), 0),
        (("pairing_theorem", "block_pullback_gram_defect_ranks"), [0, 0, 0, 0]),
        (("pairing_theorem", "block_order"), list(reversed(BLOCK_NAMES))),
        (("pairing_theorem", "three_of_four_necessary_gram_identities_fail"), False),
        (("pairing_theorem", "K622_constructed_orbit_preserves_projector_pairing"), True),
        (("pairing_theorem", "arbitrary_domain_map_and_projector_pairing_isometric_orbit_excluded"), True),
        (("pairing_theorem", "projector_pairing_is_action_self_adjoint"), False),
        (("pairing_theorem", "projector_pairing_identified_with_K441_factorized_pairing"), True),
        (("eigenblock_pairing_fingerprint", "fast_outgoing", "pullback_gram_defect_rank"), 0),
        (("eigenblock_pairing_fingerprint", "fast_incoming", "pullback_gram_defect_rank"), 0),
        (("eigenblock_pairing_fingerprint", "slow_outgoing", "pullback_gram_defect_rank"), 0),
        (("eigenblock_pairing_fingerprint", "slow_incoming", "pullback_gram_defect_rank"), 64),
        (("eigenblock_pairing_fingerprint", "slow_incoming", "projector_pairing_isometry_necessary_gram_identity"), False),
        (("ownership_reconciliation", "K622_abstract_orbit_equivalence_retracted"), True),
        (("ownership_reconciliation", "K622_constructed_domain_map_is_source_selected"), True),
        (("ownership_reconciliation", "pairing_failure_supplies_action_owned_adapter"), True),
        (("ownership_reconciliation", "common_BV_Green_domain_constructed"), True),
        (("ownership_reconciliation", "nonzero_stationary_background_constructed"), True),
        (("decision", "constructed_K622_witness_passes_pairing_gate"), True),
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
