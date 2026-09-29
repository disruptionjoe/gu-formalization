#!/usr/bin/env sage-python
"""Independent controls and hostile mutations for K620."""

from __future__ import annotations

import copy
import json

from k620_k77_action_functional_calculus_selection_obstruction import build


def controls(p: dict) -> list[bool]:
    m = p["module_projector_theorem"]
    a = p["seed_adapter_theorem"]
    o = p["ownership_reconciliation"]
    d = p["decision"]
    return [
        p["classification"] == "BRIDGE_OR_SEMANTIC_BOUNDARY",
        p["direction"] == "observed_to_native",
        p["target_claim"] == "NONE-NOT-A-KILL",
        len(p["cross_characteristic_packets"]) == 2,
        p["cross_characteristic_packets"][0]["eigenblock_rows"] == p["cross_characteristic_packets"][1]["eigenblock_rows"],
        m["functional_calculus_is_scalar_on_each_eigenspace"] is True,
        m["fast_eigenspace_ranks"] == [192, 192],
        m["common_module_fast_ranks"] == [128, 128],
        m["slow_eigenspace_ranks"] == [64, 64],
        m["common_module_slow_ranks"] == [64, 64],
        m["common_module_is_union_of_full_eigenspaces"] is False,
        m["polynomial_projector_with_image_common_module_exists"] is False,
        m["polynomial_projector_with_image_rank128_complement_exists"] is False,
        a["each_seed_meets_all_four_eigenspaces"] is True,
        a["corresponding_seed_maps_scalar_proportional_in_any_eigenspace"] is False,
        a["scalar_polynomial_p_with_pA_J0_equals_X_exists"] is False,
        a["arbitrary_commutant_or_domain_endomorphism_tested"] is False,
        a["mixed_hessian_bilinear_adapter_constructed"] is False,
        o["A_owns_four_spectral_projectors"] is True,
        o["A_owns_common_module_projector"] is False,
        o["A_owns_seed_identification"] is False,
        o["A_invariance_of_common_module_implies_action_selection"] is False,
        o["nonpolynomial_action_owned_adapter_excluded"] is False,
        o["moving_nonlinear_mixed_hessian_excluded"] is False,
        d["K619_common_module_retracted"] is False,
        d["common_module_selected_by_frozen_action"] is False,
        d["zero_form_and_moving_graph_seeds_identified"] is False,
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
        (("module_projector_theorem", "fast_eigenspace_ranks"), [128, 128]),
        (("module_projector_theorem", "common_module_fast_ranks"), [192, 192]),
        (("module_projector_theorem", "common_module_is_union_of_full_eigenspaces"), True),
        (("module_projector_theorem", "polynomial_projector_with_image_common_module_exists"), True),
        (("module_projector_theorem", "polynomial_projector_with_image_rank128_complement_exists"), True),
        (("seed_adapter_theorem", "each_seed_meets_all_four_eigenspaces"), False),
        (("seed_adapter_theorem", "corresponding_seed_maps_scalar_proportional_in_any_eigenspace"), True),
        (("seed_adapter_theorem", "scalar_polynomial_p_with_pA_J0_equals_X_exists"), True),
        (("seed_adapter_theorem", "arbitrary_commutant_or_domain_endomorphism_tested"), True),
        (("seed_adapter_theorem", "mixed_hessian_bilinear_adapter_constructed"), True),
        (("ownership_reconciliation", "A_owns_common_module_projector"), True),
        (("ownership_reconciliation", "A_owns_seed_identification"), True),
        (("ownership_reconciliation", "A_invariance_of_common_module_implies_action_selection"), True),
        (("ownership_reconciliation", "nonpolynomial_action_owned_adapter_excluded"), True),
        (("ownership_reconciliation", "moving_nonlinear_mixed_hessian_excluded"), True),
        (("decision", "K619_common_module_retracted"), True),
        (("decision", "common_module_selected_by_frozen_action"), True),
        (("decision", "zero_form_and_moving_graph_seeds_identified"), True),
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
