#!/usr/bin/env sage-python
"""Independent controls and hostile mutations for K625."""

from __future__ import annotations

import copy
import json

from k625_k77_canonical_projector_pairing_realization import BLOCK_NAMES, EXPECTED_RANKS, build


def controls(p: dict) -> list[bool]:
    t = p["real_pairing_theorem"]
    o = p["ownership_reconciliation"]
    d = p["decision"]
    rows = p["block_fingerprint"]
    return [
        p["classification"] == "BRIDGE_OR_SEMANTIC_BOUNDARY",
        p["direction"] == "native_to_observed",
        p["target_claim"] == "NONE-NOT-A-KILL",
        len(p["cross_characteristic_packets"]) == 2,
        p["cross_characteristic_packets"][0]["block_rows"] == p["cross_characteristic_packets"][1]["block_rows"],
        all(rows[name]["eigenspace_rank"] == EXPECTED_RANKS[name] for name in BLOCK_NAMES),
        all(rows[name]["restricted_pairing_rank"] == EXPECTED_RANKS[name] for name in BLOCK_NAMES),
        all(rank == 0 for row in rows.values() for rank in row["pairwise_cross_pairing_ranks"].values()),
        t["four_eigenspaces_are_H_Sigma_orthogonal"] is True,
        t["restricted_pairing_is_positive_definite_on_each_block"] is True,
        t["blockwise_H_Sigma_orthonormal_bases_exist"] is True,
        t["isometric_factorized_coordinate_map_exists"] is True,
        t["K441_rational_pair_rotations_pull_back_to_H_Sigma_isometries"] is True,
        t["K441_closed_trace_domain_and_Green_conjugation_pull_back"] is True,
        t["ambient_coordinate_map_is_unique"] is False,
        o["K623_projector_pairing_retracted"] is False,
        o["K624_H_Sigma_obstruction_retracted"] is False,
        o["K624_applies_to_canonical_projector_realization"] is True,
        o["K441_selects_this_realization_uniquely"] is False,
        o["canonical_projector_realization_is_action_owned_adapter"] is False,
        o["stationary_background_or_mixed_hessian_constructed"] is False,
        d["missing_ambient_pairing_bridge_constructed"] is True,
        d["canonical_K441_realization_available"] is True,
        d["all_K441_ambient_realizations_identified"] is False,
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
        (("direction",), "observed_to_native"),
        (("target_claim",), "SC-ACT-01"),
        (("block_fingerprint", "fast_outgoing", "eigenspace_rank"), 128),
        (("block_fingerprint", "slow_incoming", "restricted_pairing_rank"), 0),
        (("block_fingerprint", "fast_incoming", "pairwise_cross_pairing_ranks", "fast_outgoing"), 1),
        (("real_pairing_theorem", "four_eigenspaces_are_H_Sigma_orthogonal"), False),
        (("real_pairing_theorem", "restricted_pairing_is_positive_definite_on_each_block"), False),
        (("real_pairing_theorem", "blockwise_H_Sigma_orthonormal_bases_exist"), False),
        (("real_pairing_theorem", "isometric_factorized_coordinate_map_exists"), False),
        (("real_pairing_theorem", "K441_rational_pair_rotations_pull_back_to_H_Sigma_isometries"), False),
        (("real_pairing_theorem", "K441_closed_trace_domain_and_Green_conjugation_pull_back"), False),
        (("real_pairing_theorem", "ambient_coordinate_map_is_unique"), True),
        (("ownership_reconciliation", "K623_projector_pairing_retracted"), True),
        (("ownership_reconciliation", "K624_H_Sigma_obstruction_retracted"), True),
        (("ownership_reconciliation", "K624_applies_to_canonical_projector_realization"), False),
        (("ownership_reconciliation", "K441_selects_this_realization_uniquely"), True),
        (("ownership_reconciliation", "canonical_projector_realization_is_action_owned_adapter"), True),
        (("ownership_reconciliation", "stationary_background_or_mixed_hessian_constructed"), True),
        (("decision", "missing_ambient_pairing_bridge_constructed"), False),
        (("decision", "canonical_K441_realization_available"), False),
        (("decision", "all_K441_ambient_realizations_identified"), True),
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
