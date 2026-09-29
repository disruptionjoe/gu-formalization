#!/usr/bin/env sage-python
"""Independent controls and hostile mutations for K621."""

from __future__ import annotations

import copy
import json

from k621_k77_full_action_commutant_seed_adapter_obstruction import build


def controls(p: dict) -> list[bool]:
    t = p["commutant_theorem"]
    o = p["ownership_reconciliation"]
    d = p["decision"]
    rows = p["eigenblock_fingerprint"]
    return [
        p["classification"] == "BRIDGE_OR_SEMANTIC_BOUNDARY",
        p["direction"] == "observed_to_native",
        p["target_claim"] == "NONE-NOT-A-KILL",
        len(p["cross_characteristic_packets"]) == 2,
        p["cross_characteristic_packets"][0]["eigenblock_rows"] == p["cross_characteristic_packets"][1]["eigenblock_rows"],
        t["full_commutant_dimension"] == 81920,
        t["polynomial_functional_calculus_dimension"] == 4,
        t["distinct_roots_force_block_diagonal_commutant"] is True,
        t["fast_block_solution_affine_dimensions"] == [12288, 12288],
        t["slow_block_row_space_intersections"] == [0, 0],
        t["slow_block_row_space_joins"] == [128, 128],
        t["fixed_domain_commuting_adapter_exists"] is False,
        t["obstruction_location"] == "both rank-64 slow eigenspaces",
        rows["fast_outgoing"]["fixed_domain_commutant_transport_exists"] is True,
        rows["fast_incoming"]["fixed_domain_commutant_transport_exists"] is True,
        rows["slow_outgoing"]["fixed_domain_commutant_transport_exists"] is False,
        rows["slow_incoming"]["fixed_domain_commutant_transport_exists"] is False,
        rows["slow_outgoing"]["row_space_join_rank"] == 128,
        rows["slow_incoming"]["row_space_join_rank"] == 128,
        o["K620_polynomial_obstruction_retracted"] is False,
        o["full_commutant_is_action_owned_as_a_selected_adapter"] is False,
        o["fixed_domain_nonpolynomial_commutant_adapter_excluded"] is True,
        o["source_domain_reparameterization_tested"] is False,
        o["mixed_hessian_or_domain_adapter_excluded"] is False,
        o["nonzero_stationary_background_constructed"] is False,
        d["K619_common_module_retracted"] is False,
        d["K620_functional_calculus_obstruction_strengthened"] is True,
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
        (("commutant_theorem", "full_commutant_dimension"), 4),
        (("commutant_theorem", "polynomial_functional_calculus_dimension"), 81920),
        (("commutant_theorem", "distinct_roots_force_block_diagonal_commutant"), False),
        (("commutant_theorem", "fast_block_solution_affine_dimensions"), [0, 0]),
        (("commutant_theorem", "slow_block_row_space_intersections"), [64, 64]),
        (("commutant_theorem", "slow_block_row_space_joins"), [64, 64]),
        (("commutant_theorem", "fixed_domain_commuting_adapter_exists"), True),
        (("commutant_theorem", "obstruction_location"), "none"),
        (("eigenblock_fingerprint", "fast_outgoing", "fixed_domain_commutant_transport_exists"), False),
        (("eigenblock_fingerprint", "fast_incoming", "fixed_domain_commutant_transport_exists"), False),
        (("eigenblock_fingerprint", "slow_outgoing", "fixed_domain_commutant_transport_exists"), True),
        (("eigenblock_fingerprint", "slow_incoming", "fixed_domain_commutant_transport_exists"), True),
        (("eigenblock_fingerprint", "slow_outgoing", "row_space_join_rank"), 64),
        (("eigenblock_fingerprint", "slow_incoming", "row_space_join_rank"), 64),
        (("ownership_reconciliation", "K620_polynomial_obstruction_retracted"), True),
        (("ownership_reconciliation", "full_commutant_is_action_owned_as_a_selected_adapter"), True),
        (("ownership_reconciliation", "fixed_domain_nonpolynomial_commutant_adapter_excluded"), False),
        (("ownership_reconciliation", "source_domain_reparameterization_tested"), True),
        (("ownership_reconciliation", "mixed_hessian_or_domain_adapter_excluded"), True),
        (("ownership_reconciliation", "nonzero_stationary_background_constructed"), True),
        (("decision", "K619_common_module_retracted"), True),
        (("decision", "K620_functional_calculus_obstruction_strengthened"), False),
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
