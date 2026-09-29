#!/usr/bin/env sage-python
"""Independent controls and hostile mutations for K633."""

from __future__ import annotations

import copy
import json

from k633_k77_zero_form_polynomial_endomorphism_obstruction import build


def controls(p: dict) -> list[bool]:
    t = p["stabilizer_theorem"]
    o = p["ownership_reconciliation"]
    d = p["decision"]
    packets = p["cross_characteristic_packets"]
    return [
        p["classification"] == "BRIDGE_OR_SEMANTIC_BOUNDARY",
        p["direction"] == "observed_to_native",
        p["target_claim"] == "NONE-NOT-A-KILL",
        len(packets) == 2,
        all(x["seed_rank"] == 128 for x in packets),
        all(x["action_seed_rank"] == 128 for x in packets),
        all(x["seed_action_seed_join_rank"] == 256 for x in packets),
        all(x["seed_action_seed_intersection_rank"] == 0 for x in packets),
        all(x["nonconstant_quotient_coefficient_rank"] == 3 for x in packets),
        all(x["nonconstant_stabilizer_nullity"] == 0 for x in packets),
        t["functional_calculus_dimension"] == 4,
        t["representative_degree_bound"] == 3,
        t["nonconstant_quotient_classes_independent"] is True,
        t["polynomial_stabilizer_dimension"] == 1,
        t["polynomial_stabilizer_basis"] == ["identity"],
        t["every_polynomial_preserving_seed_image_is_constant_modulo_minimal_polynomial"] is True,
        t["every_induced_source_endomorphism_is_scalar"] is True,
        t["nontrivial_owned_source_endomorphism_obtained"] is False,
        o["K614_source_owned_injection_retracted"] is False,
        o["K619_common_action_module_retracted"] is False,
        o["K620_seed_adapter_obstruction_retracted"] is False,
        o["K632_current_composition_closure_sharpened"] is True,
        o["scalar_identity_counts_as_new_action_coefficient"] is False,
        o["arbitrary_commutant_or_mixed_hessian_excluded"] is False,
        d["frozen_action_polynomial_route_to_new_V128_endomorphism_closed"] is True,
        d["independently_owned_V128_endomorphism_found"] is False,
        d["actual_K596_K598_packet_released"] is False,
        p["source_and_ledger_effect"] == "none",
    ]


def set_path(p: dict, path: tuple[object, ...], value: object) -> None:
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
        (("cross_characteristic_packets", 0, "seed_rank"), 127),
        (("cross_characteristic_packets", 0, "action_seed_rank"), 127),
        (("cross_characteristic_packets", 0, "seed_action_seed_join_rank"), 128),
        (("cross_characteristic_packets", 0, "seed_action_seed_intersection_rank"), 1),
        (("cross_characteristic_packets", 0, "nonconstant_quotient_coefficient_rank"), 2),
        (("cross_characteristic_packets", 0, "nonconstant_stabilizer_nullity"), 1),
        (("stabilizer_theorem", "functional_calculus_dimension"), 5),
        (("stabilizer_theorem", "representative_degree_bound"), 4),
        (("stabilizer_theorem", "nonconstant_quotient_classes_independent"), False),
        (("stabilizer_theorem", "polynomial_stabilizer_dimension"), 2),
        (("stabilizer_theorem", "polynomial_stabilizer_basis"), ["identity", "A"]),
        (("stabilizer_theorem", "every_polynomial_preserving_seed_image_is_constant_modulo_minimal_polynomial"), False),
        (("stabilizer_theorem", "every_induced_source_endomorphism_is_scalar"), False),
        (("stabilizer_theorem", "nontrivial_owned_source_endomorphism_obtained"), True),
        (("ownership_reconciliation", "K614_source_owned_injection_retracted"), True),
        (("ownership_reconciliation", "K619_common_action_module_retracted"), True),
        (("ownership_reconciliation", "K620_seed_adapter_obstruction_retracted"), True),
        (("ownership_reconciliation", "K632_current_composition_closure_sharpened"), False),
        (("ownership_reconciliation", "scalar_identity_counts_as_new_action_coefficient"), True),
        (("ownership_reconciliation", "arbitrary_commutant_or_mixed_hessian_excluded"), True),
        (("decision", "independently_owned_V128_endomorphism_found"), True),
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
