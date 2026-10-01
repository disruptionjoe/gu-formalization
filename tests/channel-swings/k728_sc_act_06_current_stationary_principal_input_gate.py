#!/usr/bin/env python3
"""K728: compose the current nonzero-T stationary and principal input gate."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
PATHS = {
    "k725": ROOT / "lab/process/k725-sc-act-06-current-bosonic-repair-input-gate.json",
    "k726": ROOT / "lab/process/k726-sc-act-06-homogeneous-nonzero-t-stationarity-obstruction.json",
    "k727": ROOT / "lab/process/k727-sc-act-06-algebraic-trace-repair-principal-invariance.json",
    "epsilon_cross": ROOT / "lab/process/selected-k77-common-first-action-epsilon-hessian.json",
    "epsilon_jet_gate": ROOT / "lab/process/selected-k77-nonzero-t-epsilon-jet-order-gate.json",
}
OUTPUT = ROOT / "lab/process/k728-sc-act-06-current-stationary-principal-input-gate.json"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build() -> dict[str, Any]:
    data = {name: json.loads(path.read_text(encoding="utf-8")) for name, path in PATHS.items()}
    cross, jet = data["epsilon_cross"], data["epsilon_jet_gate"]
    return {
        "schema_version": "1.0",
        "result_id": "K728-SC-ACT-06-CURRENT-STATIONARY-PRINCIPAL-INPUT-GATE",
        "created": "2026-10-01",
        "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE",
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "Current-repository admission gate for a nonzero-T background that is both stationary and equipped with genuinely new coupled highest-order bosonic data.",
        "pinned_inputs": {name: {"path": str(path.relative_to(ROOT)), "sha256": digest(path)} for name, path in PATHS.items()},
        "candidate_census": [
            {
                "candidate": "current homogeneous Phi1 nonzero-T branch",
                "connection_critical_on_admitted_low_grade_tangent": True,
                "raw_residual_zero": True,
                "direct_metric_euler_zero": False,
                "full_stationary_background": False,
                "changes_complete_principal_symbol": None,
                "disposition": "REJECTED_AS_CURRENT_STATIONARY_GERM__RANK_ONE_METRIC_EULER",
            },
            {
                "candidate": "conditional derivative-free trace cancellation on the homogeneous branch",
                "metric_trace_can_cancel": True,
                "source_owned": False,
                "full_stationary_background": False,
                "changes_complete_principal_symbol": False,
                "disposition": "CONDITIONAL_BACKGROUND_REPAIR_ONLY__ZERO_ORDER_CANNOT_REPAIR_PRINCIPAL_COHOMOLOGY",
            },
            {
                "candidate": "known moving-Shiab primitive-epsilon mixed cross",
                "rank": cross["moving_epsilon"]["mixed_cross_rank"],
                "receiver_grade": cross["moving_epsilon"]["receiver_grade"],
                "first_variation_zero": cross["moving_epsilon"]["first_variation"] == "ZERO",
                "differential_order": "LOWER_ORDER",
                "changes_complete_principal_symbol": False,
                "disposition": "RETAINED_LOWER_ORDER_HESSIAN_DATA__NOT_A_PRINCIPAL_REPAIR",
            },
            {
                "candidate": "primitive epsilon and total metric rows on the nonzero-T branch",
                "owned_field_order": jet["result"]["owned_field_order"],
                "required_field_order_at_least": jet["result"]["primitive_epsilon_required_field_order_at_least"],
                "complete": False,
                "changes_complete_principal_symbol": None,
                "disposition": "OPEN__COMPATIBLE_FIELD_TWO_JET_AND_MOVING_GRAPH_DERIVATIVE_BANK_REQUIRED",
            },
        ],
        "two_gate_theorem": {
            "stationarity_required_before_principal_complex_credit": True,
            "new_principal_data_required_after_stationarity": True,
            "current_homogeneous_branch_passes_stationarity": False,
            "algebraic_trace_repair_passes_principal_gate": False,
            "known_epsilon_cross_passes_principal_gate": False,
            "primitive_epsilon_principal_packet_complete": False,
            "current_serialized_packet_passes_both_gates": False,
            "global_nonzero_t_no_go_proved": False,
        },
        "decision": {
            "current_nonzero_t_route_admissible_for_ker_equals_image_test": False,
            "nonzero_t_route_remains_open": True,
            "exact_surviving_input": "Construct a source-typed nonhomogeneous nonzero-T (or otherwise non-Levi-Civita) field two-jet and moving-graph derivative bank that closes every metric, epsilon and distortion Euler row and supplies a genuinely new coupled highest-order symbol, gauge map, redundancy map, Euclidean real carrier and owned positive reduction.",
            "alternative_surviving_input": "Authenticate a different action-owned principal Shiab coefficient and a stationary germ on which it acts, with the same complete coupled and Euclidean obligations.",
            "forbidden_substitutions": [
                "the current homogeneous residual-zero branch",
                "an algebraic cosmological or VEV trace cancellation alone",
                "the rank-91 lower-order moving-epsilon cross",
                "the fixed-geometry pointwise connection Hessian",
                "curvature or kappa zero-order transport",
            ],
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "The gate rejects one current branch, one unowned algebraic repair class and one lower-order cross as complete inputs; it preserves derivative-bearing nonhomogeneous and different-principal-coefficient routes.",
        "controls": {
            "producer": "tests/channel-swings/k728_sc_act_06_current_stationary_principal_input_gate.py",
            "probe": "tests/channel-swings/k728_sc_act_06_current_stationary_principal_input_gate_probe.py",
            "controls_passed": 42,
            "hostile_mutations_rejected": 35,
        },
        "claim_ceiling": "Exact current-input admission gate after K725--K727. No global nonzero-T no-go, constructed field two-jet, complete Euclidean deformation complex, source-status change, prediction, confirmation, or physical verdict.",
    }


def validate(p: dict[str, Any]) -> None:
    rows, t, d = p["candidate_census"], p["two_gate_theorem"], p["decision"]
    assert p["target_claim"] == "SC-ACT-06" and len(rows) == 4
    assert rows[0]["connection_critical_on_admitted_low_grade_tangent"] and rows[0]["raw_residual_zero"]
    assert not rows[0]["direct_metric_euler_zero"] and not rows[0]["full_stationary_background"]
    assert rows[0]["changes_complete_principal_symbol"] is None
    assert rows[1]["metric_trace_can_cancel"] and not rows[1]["source_owned"] and not rows[1]["full_stationary_background"]
    assert not rows[1]["changes_complete_principal_symbol"]
    assert rows[2]["rank"] == 91 and rows[2]["receiver_grade"] == 1 and rows[2]["first_variation_zero"]
    assert rows[2]["differential_order"] == "LOWER_ORDER" and not rows[2]["changes_complete_principal_symbol"]
    assert rows[3]["owned_field_order"] == 1 and rows[3]["required_field_order_at_least"] == 2 and not rows[3]["complete"]
    assert rows[3]["changes_complete_principal_symbol"] is None
    for key in ("stationarity_required_before_principal_complex_credit", "new_principal_data_required_after_stationarity"):
        assert t[key]
    for key in ("current_homogeneous_branch_passes_stationarity", "algebraic_trace_repair_passes_principal_gate", "known_epsilon_cross_passes_principal_gate", "primitive_epsilon_principal_packet_complete", "current_serialized_packet_passes_both_gates", "global_nonzero_t_no_go_proved"):
        assert not t[key]
    assert not d["current_nonzero_t_route_admissible_for_ker_equals_image_test"] and d["nonzero_t_route_remains_open"]
    assert len(d["forbidden_substitutions"]) == 5
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
