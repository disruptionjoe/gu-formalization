#!/usr/bin/env python3
"""K464 demand-lineaged fail-closed K77 properness packet sieve."""

from __future__ import annotations

import argparse
import copy
import json
from typing import Any


DEMAND_ROWS = {
    "QD-R1-1": "coherent alternatives and nonfactorizable composites",
    "QD-R1-2": "normalized positive physical event pairing",
    "QD-R1-3": "causal-domain local instruments and remote marginal invariance",
    "QD-R1-4": "reversible phase transport and open-system decoherence",
    "QD-R1-5": "gauge descent of effects, instruments and evolution",
}

REQUIRED_PACKET_FIELDS = (
    "packet_id",
    "demand_lineage",
    "action_owner_identified",
    "action_owner_ref",
    "D2_coefficient_complete",
    "D2_coefficient_ref",
    "D1_coefficient_complete",
    "D1_coefficient_ref",
    "typed_square_D2",
    "typed_square_D1",
    "total_nilpotence",
    "differential_ranks",
    "adapted_contraction",
    "cohomology_dimensions_H2_H1_H0",
    "closed_trace_domain_preserved",
    "control_is_actual_k77_action",
)

EXACT_ACYCLIC_RANKS = [10752, 35840]
ZERO_COHOMOLOGY = [0, 0, 0]


def classify_candidate(packet: dict[str, Any]) -> dict[str, Any]:
    """Classify only complete packet shapes; every uncertainty fails closed."""
    missing = [field for field in REQUIRED_PACKET_FIELDS if field not in packet]
    if missing:
        return {
            "classification": "rejected",
            "missing_fields": missing,
            "rejection_reasons": ["required_fields_missing"],
            "properness_witness_route": None,
        }

    reasons: list[str] = []
    lineage = packet["demand_lineage"]
    if not isinstance(lineage, list) or len(lineage) != len(DEMAND_ROWS) or set(lineage) != set(DEMAND_ROWS):
        reasons.append("incomplete_or_duplicated_QD_R1_1_through_5_lineage")
    if packet["typed_square_D2"] is not True or packet["typed_square_D1"] is not True:
        reasons.append("K444_typed_projector_square_failure")
    if packet["total_nilpotence"] is not True:
        reasons.append("total_nilpotence_not_proved")
    if packet["closed_trace_domain_preserved"] is not True:
        reasons.append("closed_trace_domain_not_preserved")

    exact_ranks = packet["differential_ranks"] == EXACT_ACYCLIC_RANKS
    adapted_contraction = packet["adapted_contraction"] is True
    zero_cohomology = packet["cohomology_dimensions_H2_H1_H0"] == ZERO_COHOMOLOGY
    if not (exact_ranks or adapted_contraction):
        reasons.append("no_exact_rank_or_adapted_contraction_witness")
    if not zero_cohomology:
        reasons.append("K446_contrary_cohomology_not_excluded")

    action_fields = [
        packet["action_owner_identified"] is True,
        bool(packet["action_owner_ref"]),
        packet["D2_coefficient_complete"] is True,
        bool(packet["D2_coefficient_ref"]),
        packet["D1_coefficient_complete"] is True,
        bool(packet["D1_coefficient_ref"]),
    ]
    if any(action_fields) and not all(action_fields):
        reasons.append("partial_action_custody_or_coefficient_packet")

    witness_route = "exact_ranks" if exact_ranks else "adapted_contraction" if adapted_contraction else None
    if reasons:
        return {
            "classification": "rejected",
            "missing_fields": [],
            "rejection_reasons": reasons,
            "properness_witness_route": witness_route,
        }
    if all(action_fields):
        return {
            "classification": "action_complete_ready_for_properness",
            "missing_fields": [],
            "rejection_reasons": [],
            "properness_witness_route": witness_route,
        }
    return {
        "classification": "structurally_admissible_but_unselected",
        "missing_fields": [],
        "rejection_reasons": [],
        "properness_witness_route": witness_route,
    }


def base_packet(packet_id: str) -> dict[str, Any]:
    return {
        "packet_id": packet_id,
        "demand_lineage": list(DEMAND_ROWS),
        "action_owner_identified": False,
        "action_owner_ref": "",
        "D2_coefficient_complete": False,
        "D2_coefficient_ref": "",
        "D1_coefficient_complete": False,
        "D1_coefficient_ref": "",
        "typed_square_D2": True,
        "typed_square_D1": True,
        "total_nilpotence": True,
        "differential_ranks": list(EXACT_ACYCLIC_RANKS),
        "adapted_contraction": True,
        "cohomology_dimensions_H2_H1_H0": list(ZERO_COHOMOLOGY),
        "closed_trace_domain_preserved": True,
        "control_is_actual_k77_action": False,
    }


def assessed(packet: dict[str, Any]) -> dict[str, Any]:
    return {"packet": packet, "assessment": classify_candidate(packet)}


def demo() -> dict[str, Any]:
    k445 = base_packet("K445-chain-conjugate-control")

    k446_low = base_packet("K446-low-arrow-defect-control")
    k446_low.update(
        differential_ranks=[10752, 35770],
        adapted_contraction=False,
        cohomology_dimensions_H2_H1_H0=[0, 70, 70],
    )
    k446_high = base_packet("K446-high-arrow-defect-control")
    k446_high.update(
        differential_ranks=[10731, 35840],
        adapted_contraction=False,
        cohomology_dimensions_H2_H1_H0=[21, 21, 0],
    )

    incomplete_native = base_packet("current-native-action-gap")
    incomplete_native.pop("D2_coefficient_ref")
    incomplete_native.pop("D1_coefficient_ref")

    action_shape = base_packet("abstract-action-complete-shape-control")
    action_shape.update(
        action_owner_identified=True,
        action_owner_ref="fixture-only#action-owner",
        D2_coefficient_complete=True,
        D2_coefficient_ref="fixture-only#D2",
        D1_coefficient_complete=True,
        D1_coefficient_ref="fixture-only#D1",
    )

    packets = {
        "K445_structural_control": assessed(k445),
        "K446_low_defect_control": assessed(k446_low),
        "K446_high_defect_control": assessed(k446_high),
        "current_native_action_gap": assessed(incomplete_native),
        "abstract_action_complete_shape_control": assessed(action_shape),
    }
    return {
        "schema_version": "1.0",
        "result_id": "K464-K77-PROPERNESS-DEMAND-SIEVE",
        "classification": "BRIDGE_OR_SEMANTIC_BOUNDARY",
        "direction": "observed_to_native",
        "demand_lineage": DEMAND_ROWS,
        "required_packet_fields": list(REQUIRED_PACKET_FIELDS),
        "sieve_obligations": {
            "K444_both_typed_squares_required": True,
            "total_nilpotence_required": True,
            "exact_ranks_or_adapted_contraction_required": True,
            "K446_contrary_cohomology_must_be_excluded": True,
            "closed_trace_domain_preservation_required": True,
            "partial_action_packet_rejected": True,
        },
        "candidate_packets": packets,
        "decision": {
            "actual_action_coefficients_serialized": False,
            "physical_cohomology_constructed": False,
            "actual_action_complete_ready_packet_count": 0,
            "structural_controls_do_not_select_an_action": True,
            "next_exact_input": "Supply one demand-lineaged, owner-authenticated, coefficient-complete K77 D2/D1 packet on the closed trace domain; then apply the typed-square, nilpotence and exact-rank/adapted-contraction tests without identifying finite control cohomology with physical states.",
        },
    }


def selftest() -> dict[str, int]:
    structural = base_packet("structural")
    action = base_packet("action")
    action.update(
        action_owner_identified=True,
        action_owner_ref="control#owner",
        D2_coefficient_complete=True,
        D2_coefficient_ref="control#D2",
        D1_coefficient_complete=True,
        D1_coefficient_ref="control#D1",
    )
    checks = [
        classify_candidate(structural)["classification"] == "structurally_admissible_but_unselected",
        classify_candidate(action)["classification"] == "action_complete_ready_for_properness",
    ]
    hostile = []
    for field in REQUIRED_PACKET_FIELDS:
        candidate = copy.deepcopy(structural)
        candidate.pop(field)
        hostile.append(classify_candidate(candidate)["classification"] == "rejected")
    for field in ("typed_square_D2", "typed_square_D1", "total_nilpotence", "closed_trace_domain_preserved"):
        candidate = copy.deepcopy(structural)
        candidate[field] = False
        hostile.append(classify_candidate(candidate)["classification"] == "rejected")
    candidate = copy.deepcopy(structural)
    candidate["differential_ranks"] = [10752, 35770]
    candidate["adapted_contraction"] = False
    hostile.append(classify_candidate(candidate)["classification"] == "rejected")
    candidate = copy.deepcopy(structural)
    candidate["cohomology_dimensions_H2_H1_H0"] = [0, 70, 70]
    hostile.append(classify_candidate(candidate)["classification"] == "rejected")
    candidate = copy.deepcopy(structural)
    candidate["action_owner_identified"] = True
    hostile.append(classify_candidate(candidate)["classification"] == "rejected")
    assert all(checks) and all(hostile)
    return {"positive_controls_passed": len(checks), "hostile_cases_rejected": len(hostile)}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--demo", action="store_true")
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args()
    if args.selftest:
        print(json.dumps(selftest(), sort_keys=True))
    else:
        print(json.dumps(demo(), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
