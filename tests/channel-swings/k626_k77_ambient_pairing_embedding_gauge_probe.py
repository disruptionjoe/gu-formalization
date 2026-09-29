#!/usr/bin/env sage-python
"""Independent controls and hostile mutations for K626."""

from __future__ import annotations

import copy
import json

from k623_k77_constructed_orbit_pairing_defect import BLOCK_NAMES
from k626_k77_ambient_pairing_embedding_gauge import build


def controls(p: dict) -> list[bool]:
    t = p["embedding_gauge_theorem"]
    o = p["ownership_reconciliation"]
    d = p["decision"]
    packets = p["cross_characteristic_packets"]
    rows = [row for packet in packets for row in packet["shear_rows"].values()]
    return [
        p["classification"] == "BRIDGE_OR_SEMANTIC_BOUNDARY",
        p["direction"] == "native_to_observed",
        p["target_claim"] == "NONE-NOT-A-KILL",
        len(packets) == 2,
        all(set(packet["shear_rows"]) == set(BLOCK_NAMES) for packet in packets),
        all(row["nilpotent_rank"] == 1 for row in rows),
        all(row["checks"]["nilpotent_square_zero"] for row in rows),
        all(row["checks"]["explicit_inverse"] for row in rows),
        all(row["checks"]["commutes_with_action"] for row in rows),
        all(row["checks"]["commutes_with_all_projectors"] for row in rows),
        all(row["checks"]["changed_pairing_rank_512"] for row in rows),
        all(row["checks"]["action_self_adjoint_for_changed_pairing"] for row in rows),
        all(row["checks"]["all_projectors_self_adjoint_for_changed_pairing"] for row in rows),
        all(row["checks"]["zero_seed_normalized_traces_change"] for row in rows),
        all(row["checks"]["graph_seed_normalized_traces_change"] for row in rows),
        t["all_blockwise_changes_preserve_four_root_action_up_to_factorized_coordinates"] is True,
        t["K441_serializes_one_ambient_embedding"] is False,
        t["H_Sigma_is_a_canonical_projector_point_in_the_family"] is True,
        t["K624_normalized_trace_fingerprints_are_embedding_gauge_invariant"] is False,
        t["actual_carrier_shears_tested"] == 8,
        t["every_tested_shear_changes_both_seed_fingerprints"] is True,
        o["K625_canonical_realization_retracted"] is False,
        o["K624_H_Sigma_obstruction_retracted"] is False,
        o["K624_universalized_to_every_K441_embedding"] is False,
        o["K441_abstract_transport_selects_an_ambient_Gram"] is False,
        o["embedding_gauge_is_source_or_action_selection"] is False,
        o["pairing_gauge_constructs_mixed_hessian_or_stationary_background"] is False,
        d["canonical_projector_realization_classified"] is True,
        d["abstract_K441_pairing_alone_decides_K622_orbit"] is False,
        d["source_or_action_owned_embedding_required_for_broader_verdict"] is True,
        d["actual_K596_K598_packet_released"] is False,
        d["selected_source_action_rejected"] is False,
        p["source_and_ledger_effect"] == "none",
    ]


def set_path(p: dict, path: tuple, value: object) -> None:
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
        (("target_claim",), "SC-ACT-02"),
        (("cross_characteristic_packets", 0, "shear_rows", "fast_outgoing", "nilpotent_rank"), 2),
        (("cross_characteristic_packets", 0, "shear_rows", "fast_incoming", "checks", "nilpotent_square_zero"), False),
        (("cross_characteristic_packets", 0, "shear_rows", "slow_outgoing", "checks", "explicit_inverse"), False),
        (("cross_characteristic_packets", 0, "shear_rows", "slow_incoming", "checks", "commutes_with_action"), False),
        (("cross_characteristic_packets", 1, "shear_rows", "fast_outgoing", "checks", "commutes_with_all_projectors"), False),
        (("cross_characteristic_packets", 1, "shear_rows", "fast_incoming", "checks", "changed_pairing_rank_512"), False),
        (("cross_characteristic_packets", 1, "shear_rows", "slow_outgoing", "checks", "action_self_adjoint_for_changed_pairing"), False),
        (("cross_characteristic_packets", 1, "shear_rows", "slow_incoming", "checks", "all_projectors_self_adjoint_for_changed_pairing"), False),
        (("cross_characteristic_packets", 0, "shear_rows", "fast_outgoing", "checks", "zero_seed_normalized_traces_change"), False),
        (("cross_characteristic_packets", 1, "shear_rows", "fast_outgoing", "checks", "graph_seed_normalized_traces_change"), False),
        (("embedding_gauge_theorem", "all_blockwise_changes_preserve_four_root_action_up_to_factorized_coordinates"), False),
        (("embedding_gauge_theorem", "K441_serializes_one_ambient_embedding"), True),
        (("embedding_gauge_theorem", "H_Sigma_is_a_canonical_projector_point_in_the_family"), False),
        (("embedding_gauge_theorem", "K624_normalized_trace_fingerprints_are_embedding_gauge_invariant"), True),
        (("embedding_gauge_theorem", "actual_carrier_shears_tested"), 4),
        (("embedding_gauge_theorem", "every_tested_shear_changes_both_seed_fingerprints"), False),
        (("ownership_reconciliation", "K625_canonical_realization_retracted"), True),
        (("ownership_reconciliation", "K624_H_Sigma_obstruction_retracted"), True),
        (("ownership_reconciliation", "K624_universalized_to_every_K441_embedding"), True),
        (("ownership_reconciliation", "K441_abstract_transport_selects_an_ambient_Gram"), True),
        (("ownership_reconciliation", "embedding_gauge_is_source_or_action_selection"), True),
        (("ownership_reconciliation", "pairing_gauge_constructs_mixed_hessian_or_stationary_background"), True),
        (("decision", "canonical_projector_realization_classified"), False),
        (("decision", "abstract_K441_pairing_alone_decides_K622_orbit"), True),
        (("decision", "source_or_action_owned_embedding_required_for_broader_verdict"), False),
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
