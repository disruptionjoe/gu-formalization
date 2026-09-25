#!/usr/bin/env python3
"""Independent controls and hostile mutations for K456."""

from __future__ import annotations

import copy

from k456_k156_continuum_action_column_manifest import demo


def controls(packet):
    column = packet.get("column_decomposition", {})
    exchange = column.get("exchange_component", {})
    contract = packet.get("representation_contract", {})
    decision = packet.get("decision", {})
    return [
        ("schema", packet.get("schema_version") == "1.0"),
        ("id", packet.get("result_id") == "K456-K156-CONTINUUM-ACTION-COLUMN-MANIFEST"),
        ("classification", packet.get("classification") == "INTERNAL_STRUCTURAL_ONLY"),
        ("direction", packet.get("direction") == "observed_to_native"),
        ("carrier", packet.get("fixed_control", {}).get("seed_scope") == "K162_zero_bath_seed_orbits"),
        ("scalar", column.get("scalar_component", {}).get("complete_convergent_representation") is True),
        ("diagonal", column.get("matched_diagonal_component", {}).get("complete_convergent_representation") is True),
        ("term count", exchange.get("resolved_term_count") == 2958),
        ("digest", exchange.get("resolved_family_sha256") == "ee24469ef5c6bb8d606efe1d529b294cbc7097b14adc51df80a51627aa7eb686"),
        ("fields complete", exchange.get("unresolved_required_field_instances") == 0),
        ("tail", exchange.get("post_order_12_tail_norm_upper") == "3011499/838860800"),
        ("tail strict", exchange.get("post_order_12_tail_less_than_1_over_250") is True),
        ("column serialized", contract.get("complete_continuum_action_column_serialized") is True),
        ("not evaluated", contract.get("complete_continuum_action_column_numerically_evaluated") is False),
        ("column released", decision.get("K455_column_reference_released") is True),
        ("residual pending", decision.get("K455_residual_reference_released") is False),
    ]


def main() -> int:
    packet = demo()
    base = controls(packet)
    mutations = [
        lambda d: d.__setitem__("schema_version", "0"),
        lambda d: d.__setitem__("result_id", "K455"),
        lambda d: d.__setitem__("classification", "PHYSICAL"),
        lambda d: d.__setitem__("direction", "native_to_observed"),
        lambda d: d["fixed_control"].__setitem__("seed_scope", "arbitrary"),
        lambda d: d["column_decomposition"]["scalar_component"].__setitem__("complete_convergent_representation", False),
        lambda d: d["column_decomposition"]["matched_diagonal_component"].__setitem__("complete_convergent_representation", False),
        lambda d: d["column_decomposition"]["exchange_component"].__setitem__("resolved_term_count", 2957),
        lambda d: d["column_decomposition"]["exchange_component"].__setitem__("resolved_family_sha256", "bad"),
        lambda d: d["column_decomposition"]["exchange_component"].__setitem__("unresolved_required_field_instances", 1),
        lambda d: d["column_decomposition"]["exchange_component"].__setitem__("post_order_12_tail_norm_upper", "0"),
        lambda d: d["column_decomposition"]["exchange_component"].__setitem__("post_order_12_tail_less_than_1_over_250", False),
        lambda d: d["representation_contract"].__setitem__("complete_continuum_action_column_serialized", False),
        lambda d: d["representation_contract"].__setitem__("complete_continuum_action_column_numerically_evaluated", True),
        lambda d: d["decision"].__setitem__("K455_column_reference_released", False),
        lambda d: d["decision"].__setitem__("K455_residual_reference_released", True),
    ]
    rejected = 0
    for mutate in mutations:
        candidate = copy.deepcopy(packet)
        mutate(candidate)
        if not all(ok for _, ok in controls(candidate)):
            rejected += 1
    print(f"K456 EXACT CONTROL: {sum(ok for _, ok in base)}/{len(base)} pass")
    print(f"K456 HOSTILE MUTATIONS: {rejected}/{len(mutations)} rejected")
    return 0 if all(ok for _, ok in base) and rejected == len(mutations) else 1


if __name__ == "__main__":
    raise SystemExit(main())
