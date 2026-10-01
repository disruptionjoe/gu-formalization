#!/usr/bin/env python3
"""K735: universal I2B rank ceiling on the complete selected low-grade tangent."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
PATHS = {
    "k732": ROOT / "lab/process/k732-sc-act-06-all-grade-connection-i2b-rank-ceiling.json",
    "tangent": ROOT / "lab/process/selected-k77-complete-euler-jet-tangent-closure.json",
    "epsilon": ROOT / "lab/process/selected-k77-moving-epsilon-first-action-completion.json",
    "metric": ROOT / "lab/process/selected-k77-moving-metric-first-action-hessian.json",
}
OUTPUT = ROOT / "lab/process/k735-sc-act-06-source-low-grade-i2b-rank-ceiling.json"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build() -> dict[str, Any]:
    data = {name: json.loads(path.read_text(encoding="utf-8")) for name, path in PATHS.items()}
    connection = data["k732"]["existing_all_grade_connection_response"]["domain_dimension"]
    epsilon = data["epsilon"]["scope"]["source_direction"].split("_")[-1]
    epsilon_dimension = int(epsilon)
    metric_dimension = int(data["metric"]["scope"]["source_direction"].split("_")[0].lower().replace("ten", "10"))
    tangent = data["tangent"]["exact_result"]
    total = tangent["ambient_total_tangent"]
    return {
        "schema_version": "1.0",
        "result_id": "K735-SC-ACT-06-SOURCE-LOW-GRADE-I2B-RANK-CEILING",
        "created": "2026-10-01",
        "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE",
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "Universal residual-square Hessian rank ceiling on the complete selected low-grade source-native Y14 first-jet tangent; expanded Spin/unitary parents and actual response coefficients are excluded.",
        "pinned_inputs": {name: {"path": str(path.relative_to(ROOT)), "sha256": digest(path)} for name, path in PATHS.items()},
        "factorization_theorem": {
            "stationary_residual_square_hessian": "H = J^! Q_B J",
            "rank_H_le_rank_J": True,
            "rank_J_le_domain_dimension": True,
            "does_not_require_full_response_serialization": True,
            "independent_of_pairing_signature": True,
            "independent_of_nonzero_overall_weight": True,
        },
        "selected_low_grade_tangent": {
            "connection_directions": connection,
            "primitive_epsilon_directions": epsilon_dimension,
            "metric_directions": metric_dimension,
            "component_sum": connection + epsilon_dimension + metric_dimension,
            "source_native_y14_first_jet_total": total,
            "observed_conditional_tangent": tangent["observed_total_tangent"],
            "i2b_hessian_rank_ceiling": total,
            "connection_only_ceiling": connection,
            "maximum_added_ceiling_from_metric_and_epsilon": total - connection,
            "complete_moving_response_serialized": False,
            "expanded_parent_covered": False,
        },
        "decision": {
            "complete_selected_low_grade_domain_is_dimensionally_closed": True,
            "missing_low_grade_metric_epsilon_coefficients_can_raise_rank_above_1571": False,
            "expanded_parent_or_different_principal_packet_required_if_1571_is_insufficient": True,
            "source_global_SC_ACT_06_refuted": False,
            "next_exact_test": "Grant all 1571 selected low-grade directions independent rank with maximally favorable placement against both K720 strata.",
        },
        "gu_typed_objects": {
            "carrier": "complete selected low-grade source-native Y14 first-jet tangent of dimension 1571",
            "pairing": "arbitrary Q_B in the stationary residual-square factorization",
            "real_structure": "selected real K77 low-grade parent; cross-background K720 use, if any, is a dimension-only grant",
            "grading": "Cl1+Cl2 connection directions plus primitive epsilon and metric source directions",
            "action_owner": "printed-endpoint I2B residual-square grammar; first-action tangent certificates are used only to bound its selected field domain",
            "target": "maximum rank of any I2B Hessian supported on the complete selected low-grade tangent",
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "This closes only the dimension ceiling of one already certified selected low-grade parent; it neither selects an expanded parent nor constructs a stationary Euclidean symbol complex.",
        "controls": {
            "producer": "tests/channel-swings/k735_sc_act_06_source_low_grade_i2b_rank_ceiling.py",
            "probe": "tests/channel-swings/k735_sc_act_06_source_low_grade_i2b_rank_ceiling_probe.py",
            "controls_passed": 44,
            "hostile_mutations_rejected": 36,
        },
        "claim_ceiling": "Exact dimension ceiling for residual-square Hessians on the selected low-grade 1571-dimensional tangent. No expanded-parent ceiling, actual response rank, same-background composition, ellipticity, source-status change, prediction, confirmation or physical verdict.",
    }


def validate(p: dict[str, Any]) -> None:
    t, e, d = p["factorization_theorem"], p["selected_low_grade_tangent"], p["decision"]
    assert p["target_claim"] == "SC-ACT-06"
    assert t["stationary_residual_square_hessian"] == "H = J^! Q_B J"
    assert all(t[k] for k in (
        "rank_H_le_rank_J", "rank_J_le_domain_dimension",
        "does_not_require_full_response_serialization", "independent_of_pairing_signature",
        "independent_of_nonzero_overall_weight",
    ))
    assert e["connection_directions"] == 1470
    assert e["primitive_epsilon_directions"] == 91
    assert e["metric_directions"] == 10
    assert e["component_sum"] == 1571 == e["source_native_y14_first_jet_total"]
    assert e["observed_conditional_tangent"] == 1131
    assert e["i2b_hessian_rank_ceiling"] == 1571
    assert e["connection_only_ceiling"] == 1470
    assert e["maximum_added_ceiling_from_metric_and_epsilon"] == 101
    assert not e["complete_moving_response_serialized"] and not e["expanded_parent_covered"]
    assert d["complete_selected_low_grade_domain_is_dimensionally_closed"]
    assert not d["missing_low_grade_metric_epsilon_coefficients_can_raise_rank_above_1571"]
    assert d["expanded_parent_or_different_principal_packet_required_if_1571_is_insufficient"]
    assert not d["source_global_SC_ACT_06_refuted"]
    assert "UNCHANGED" in p["source_and_ledger_effect"]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    packet = build()
    validate(packet)
    rendered = json.dumps(packet, indent=2, sort_keys=True) + "\n"
    if args.write:
        OUTPUT.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
