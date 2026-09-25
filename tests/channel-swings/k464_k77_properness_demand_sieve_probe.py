#!/usr/bin/env python3
"""Independent controls and hostile mutations for K464."""

from __future__ import annotations

import copy

from k464_k77_properness_demand_sieve import DEMAND_ROWS, demo


def controls(packet):
    candidates = packet.get("candidate_packets", {})
    obligations = packet.get("sieve_obligations", {})
    decision = packet.get("decision", {})
    k445 = candidates.get("K445_structural_control", {}).get("assessment", {})
    low = candidates.get("K446_low_defect_control", {}).get("assessment", {})
    high = candidates.get("K446_high_defect_control", {}).get("assessment", {})
    gap = candidates.get("current_native_action_gap", {}).get("assessment", {})
    shape = candidates.get("abstract_action_complete_shape_control", {})
    return [
        ("schema", packet.get("schema_version") == "1.0"),
        ("id", packet.get("result_id") == "K464-K77-PROPERNESS-DEMAND-SIEVE"),
        ("classification", packet.get("classification") == "BRIDGE_OR_SEMANTIC_BOUNDARY"),
        ("direction", packet.get("direction") == "observed_to_native"),
        ("five demand rows", set(packet.get("demand_lineage", {})) == set(DEMAND_ROWS)),
        ("complete schema", len(packet.get("required_packet_fields", [])) == 16),
        ("typed squares", obligations.get("K444_both_typed_squares_required") is True),
        ("nilpotence", obligations.get("total_nilpotence_required") is True),
        ("rank or contraction", obligations.get("exact_ranks_or_adapted_contraction_required") is True),
        ("contrary excluded", obligations.get("K446_contrary_cohomology_must_be_excluded") is True),
        ("closed domain", obligations.get("closed_trace_domain_preservation_required") is True),
        ("partial rejected", obligations.get("partial_action_packet_rejected") is True),
        ("K445 structural", k445.get("classification") == "structurally_admissible_but_unselected"),
        ("K445 exact rank", k445.get("properness_witness_route") == "exact_ranks"),
        ("K446 low rejected", low.get("classification") == "rejected"),
        ("K446 low cohomology", "K446_contrary_cohomology_not_excluded" in low.get("rejection_reasons", [])),
        ("K446 high rejected", high.get("classification") == "rejected"),
        ("K446 high cohomology", "K446_contrary_cohomology_not_excluded" in high.get("rejection_reasons", [])),
        ("native gap rejected", gap.get("classification") == "rejected"),
        ("native gap missing", set(gap.get("missing_fields", [])) == {"D2_coefficient_ref", "D1_coefficient_ref"}),
        ("shape ready", shape.get("assessment", {}).get("classification") == "action_complete_ready_for_properness"),
        ("shape not actual", shape.get("packet", {}).get("control_is_actual_k77_action") is False),
        ("no coefficients", decision.get("actual_action_coefficients_serialized") is False),
        ("no physical cohomology", decision.get("physical_cohomology_constructed") is False),
        ("zero actual ready", decision.get("actual_action_complete_ready_packet_count") == 0),
        ("no structural selection", decision.get("structural_controls_do_not_select_an_action") is True),
        ("next owner packet", "owner-authenticated" in decision.get("next_exact_input", "")),
    ]


def main() -> int:
    packet = demo()
    base = controls(packet)
    mutations = [
        lambda d: d.__setitem__("schema_version", "0"),
        lambda d: d.__setitem__("result_id", "K446"),
        lambda d: d.__setitem__("classification", "PHYSICAL"),
        lambda d: d.__setitem__("direction", "native_to_observed"),
        lambda d: d.__setitem__("demand_lineage", {}),
        lambda d: d.__setitem__("required_packet_fields", []),
        lambda d: d["sieve_obligations"].__setitem__("K444_both_typed_squares_required", False),
        lambda d: d["sieve_obligations"].__setitem__("total_nilpotence_required", False),
        lambda d: d["sieve_obligations"].__setitem__("exact_ranks_or_adapted_contraction_required", False),
        lambda d: d["sieve_obligations"].__setitem__("K446_contrary_cohomology_must_be_excluded", False),
        lambda d: d["sieve_obligations"].__setitem__("closed_trace_domain_preservation_required", False),
        lambda d: d["sieve_obligations"].__setitem__("partial_action_packet_rejected", False),
        lambda d: d["candidate_packets"]["K445_structural_control"]["assessment"].__setitem__("classification", "action_complete_ready_for_properness"),
        lambda d: d["candidate_packets"]["K445_structural_control"]["assessment"].__setitem__("properness_witness_route", None),
        lambda d: d["candidate_packets"]["K446_low_defect_control"]["assessment"].__setitem__("classification", "structurally_admissible_but_unselected"),
        lambda d: d["candidate_packets"]["K446_low_defect_control"]["assessment"].__setitem__("rejection_reasons", []),
        lambda d: d["candidate_packets"]["K446_high_defect_control"]["assessment"].__setitem__("classification", "structurally_admissible_but_unselected"),
        lambda d: d["candidate_packets"]["K446_high_defect_control"]["assessment"].__setitem__("rejection_reasons", []),
        lambda d: d["candidate_packets"]["current_native_action_gap"]["assessment"].__setitem__("classification", "action_complete_ready_for_properness"),
        lambda d: d["candidate_packets"]["current_native_action_gap"]["assessment"].__setitem__("missing_fields", []),
        lambda d: d["candidate_packets"]["abstract_action_complete_shape_control"]["assessment"].__setitem__("classification", "rejected"),
        lambda d: d["candidate_packets"]["abstract_action_complete_shape_control"]["packet"].__setitem__("control_is_actual_k77_action", True),
        lambda d: d["decision"].__setitem__("actual_action_coefficients_serialized", True),
        lambda d: d["decision"].__setitem__("physical_cohomology_constructed", True),
        lambda d: d["decision"].__setitem__("actual_action_complete_ready_packet_count", 1),
        lambda d: d["decision"].__setitem__("structural_controls_do_not_select_an_action", False),
        lambda d: d["decision"].__setitem__("next_exact_input", "infer the action"),
    ]
    rejected = 0
    for mutate in mutations:
        candidate = copy.deepcopy(packet)
        mutate(candidate)
        rejected += int(not all(ok for _, ok in controls(candidate)))
    print(f"K464 EXACT CONTROL: {sum(ok for _, ok in base)}/{len(base)} pass")
    print(f"K464 HOSTILE MUTATIONS: {rejected}/{len(mutations)} rejected")
    return 0 if all(ok for _, ok in base) and rejected == len(mutations) else 1


if __name__ == "__main__":
    raise SystemExit(main())
