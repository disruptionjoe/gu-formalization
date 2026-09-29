#!/usr/bin/env python3
"""Independent controls and hostile mutations for K627."""

from __future__ import annotations

import copy
import json

from k627_k77_block_gauge_positive_pairing_nonselection import build


def controls(p: dict) -> list[bool]:
    t = p["pairing_nonselection_theorem"]
    o = p["ownership_reconciliation"]
    d = p["decision"]
    return [
        p["classification"] == "BRIDGE_OR_SEMANTIC_BOUNDARY",
        p["direction"] == "native_to_observed",
        p["target_claim"] == "NONE-NOT-A-KILL",
        t["block_ranks"] == [192, 192, 64, 64],
        t["block_positive_pairing_dimensions"] == [18528, 18528, 2080, 2080],
        t["total_positive_pairing_family_dimension"] == 41216,
        t["full_block_gauge_has_nonzero_invariant_symmetric_form"] is False,
        t["selecting_a_gram_is_a_gauge_reduction"] is True,
        t["K625_H_Sigma_is_one_projector_induced_point"] is True,
        t["K441_abstract_data_select_a_positive_gram"] is False,
        o["K625_canonical_realization_retracted"] is False,
        o["K626_embedding_gauge_retracted"] is False,
        o["full_gauge_nonselection_is_source_or_action_selection"] is False,
        o["orthogonal_reduction_is_supplied_by_K441"] is False,
        o["mixed_hessian_or_stationary_background_constructed"] is False,
        o["common_BV_Green_domain_constructed"] is False,
        d["abstract_K441_pairing_is_canonical_on_actual_carrier"] is False,
        d["extra_reduction_data_required_to_select_pairing"] is True,
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
        (("target_claim",), "SC-META-53"),
        (("pairing_nonselection_theorem", "block_ranks"), [192, 192, 64, 63]),
        (("pairing_nonselection_theorem", "block_positive_pairing_dimensions"), [18528, 18528, 2080, 2079]),
        (("pairing_nonselection_theorem", "total_positive_pairing_family_dimension"), 41215),
        (("pairing_nonselection_theorem", "full_block_gauge_has_nonzero_invariant_symmetric_form"), True),
        (("pairing_nonselection_theorem", "selecting_a_gram_is_a_gauge_reduction"), False),
        (("pairing_nonselection_theorem", "K625_H_Sigma_is_one_projector_induced_point"), False),
        (("pairing_nonselection_theorem", "K441_abstract_data_select_a_positive_gram"), True),
        (("ownership_reconciliation", "K625_canonical_realization_retracted"), True),
        (("ownership_reconciliation", "K626_embedding_gauge_retracted"), True),
        (("ownership_reconciliation", "full_gauge_nonselection_is_source_or_action_selection"), True),
        (("ownership_reconciliation", "orthogonal_reduction_is_supplied_by_K441"), True),
        (("ownership_reconciliation", "mixed_hessian_or_stationary_background_constructed"), True),
        (("ownership_reconciliation", "common_BV_Green_domain_constructed"), True),
        (("decision", "abstract_K441_pairing_is_canonical_on_actual_carrier"), True),
        (("decision", "extra_reduction_data_required_to_select_pairing"), False),
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
