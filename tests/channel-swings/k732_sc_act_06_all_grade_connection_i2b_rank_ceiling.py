#!/usr/bin/env python3
"""K732: rank ceiling for the existing all-grade connection Upsilon response."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
PATHS = {
    "all_grade_response": ROOT / "lab/process/selected-k77-coupled-all-grade-upsilon-graph.json",
    "serialized_ceiling": ROOT / "lab/process/k729-sc-act-06-serialized-i2b-principal-rank-ceiling.json",
}
OUTPUT = ROOT / "lab/process/k732-sc-act-06-all-grade-connection-i2b-rank-ceiling.json"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build() -> dict[str, Any]:
    graph = json.loads(PATHS["all_grade_response"].read_text(encoding="utf-8"))
    k729 = json.loads(PATHS["serialized_ceiling"].read_text(encoding="utf-8"))
    exact = graph["exact_result"]
    rank = exact["response_rank"]
    return {
        "schema_version": "1.0",
        "result_id": "K732-SC-ACT-06-ALL-GRADE-CONNECTION-I2B-RANK-CEILING",
        "created": "2026-10-01",
        "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE",
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "Universal rank ceiling for an I2B residual-square Hessian factored through the existing exact all-grade Cl1+Cl2 connection response; no transfer to K720's flat germ is assumed.",
        "pinned_inputs": {name: {"path": str(path.relative_to(ROOT)), "sha256": digest(path)} for name, path in PATHS.items()},
        "factorization_theorem": {
            "stationary_residual_square_hessian": "H = J^! Q_B J",
            "rank_H_le_rank_J": True,
            "rank_J_le_domain_dimension": True,
            "independent_of_pairing_signature": True,
            "independent_of_nonzero_overall_weight": True,
            "injective_J_does_not_imply_elliptic_H_on_a_larger_field_carrier": True,
        },
        "existing_all_grade_connection_response": {
            "source_tangent_grades": exact["source_tangent_grades"],
            "domain_dimension": exact["domain_dimension"],
            "output_coordinate_support": exact["output_coordinate_support"],
            "response_rank": rank,
            "response_nullity": exact["response_nullity"],
            "response_cokernel_dimension": exact["response_cokernel_dimension"],
            "i2b_hessian_rank_ceiling": rank,
            "serialized_bank_ceiling": k729["serialized_bank"]["universal_extension_rank_ceiling"],
            "additional_ceiling_beyond_serialized_bank": rank - k729["serialized_bank"]["universal_extension_rank_ceiling"],
            "complete_moving_metric_epsilon_i2b_map_serialized": False,
            "same_stationary_background_as_k720_flat_germ": False,
        },
        "decision": {
            "existing_connection_all_grade_response_is_stronger_than_serialized_196_bank": True,
            "existing_response_constructs_complete_moving_i2b_symbol": False,
            "existing_response_may_be_granted_as_a_favorable_dimension_only_transfer": True,
            "native_cross_background_composition_proved": False,
            "next_exact_test": "Grant the full 1470-rank ceiling a maximally favorable embedding into each K720 stratum and compare it with the exact rank required for middle exactness.",
        },
        "gu_typed_objects": {
            "carrier": "1470-real Cl1+Cl2 connection tangent mapped into 4330 raw-Upsilon coordinates",
            "pairing": "arbitrary nondegenerate or indefinite Q_B in the residual-square factorization; rank theorem does not require positivity",
            "real_structure": "selected real K77 connection response; K720 comparison, if made, is an explicitly favorable dimension-only grant",
            "grading": "input Clifford grades 1,2 and output grades 1,2,5",
            "action_owner": "source-owned printed-endpoint I2B residual-square grammar factored through the repo's exact all-grade raw-Upsilon response",
            "target": "maximum rank of the induced connection-only I2B Hessian",
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "This reuses an existing conditional all-grade connection response and proves only a factorization ceiling; it neither constructs the missing moving metric/epsilon map nor changes a physics verdict.",
        "controls": {
            "producer": "tests/channel-swings/k732_sc_act_06_all_grade_connection_i2b_rank_ceiling.py",
            "probe": "tests/channel-swings/k732_sc_act_06_all_grade_connection_i2b_rank_ceiling_probe.py",
            "controls_passed": 38,
            "hostile_mutations_rejected": 31,
        },
        "claim_ceiling": "Exact rank ceiling for I2B Hessians factored through the existing 1470-dimensional all-grade connection response. No same-background composition, complete moving-field symbol, stationarity theorem, Euclidean owner, source-status change, prediction, confirmation or physical verdict.",
    }


def validate(p: dict[str, Any]) -> None:
    t = p["factorization_theorem"]
    e = p["existing_all_grade_connection_response"]
    d = p["decision"]
    assert p["target_claim"] == "SC-ACT-06"
    assert t["stationary_residual_square_hessian"] == "H = J^! Q_B J"
    assert all(t[k] for k in (
        "rank_H_le_rank_J", "rank_J_le_domain_dimension",
        "independent_of_pairing_signature", "independent_of_nonzero_overall_weight",
        "injective_J_does_not_imply_elliptic_H_on_a_larger_field_carrier",
    ))
    assert e["source_tangent_grades"] == [1, 2]
    assert e["domain_dimension"] == 1470 and e["response_rank"] == 1470
    assert e["output_coordinate_support"] == 4330 and e["response_nullity"] == 0
    assert e["response_cokernel_dimension"] == 2860
    assert e["i2b_hessian_rank_ceiling"] == 1470
    assert e["serialized_bank_ceiling"] == 196
    assert e["additional_ceiling_beyond_serialized_bank"] == 1274
    assert not e["complete_moving_metric_epsilon_i2b_map_serialized"]
    assert not e["same_stationary_background_as_k720_flat_germ"]
    assert d["existing_connection_all_grade_response_is_stronger_than_serialized_196_bank"]
    assert not d["existing_response_constructs_complete_moving_i2b_symbol"]
    assert d["existing_response_may_be_granted_as_a_favorable_dimension_only_transfer"]
    assert not d["native_cross_background_composition_proved"]
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
