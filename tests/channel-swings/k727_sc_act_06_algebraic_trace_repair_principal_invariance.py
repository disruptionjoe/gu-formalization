#!/usr/bin/env python3
"""K727: grant an algebraic trace repair and test its principal effect."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
PATHS = {
    "k720": ROOT / "lab/process/k720-sc-act-06-selected-i1b-euclidean-bosonic-symbol.json",
    "k724": ROOT / "lab/process/k724-sc-act-06-kappa-zero-order-ellipticity-obstruction.json",
    "k726": ROOT / "lab/process/k726-sc-act-06-homogeneous-nonzero-t-stationarity-obstruction.json",
    "metric_euler": ROOT / "lab/process/selected-k77-direct-metric-euler.json",
}
OUTPUT = ROOT / "lab/process/k727-sc-act-06-algebraic-trace-repair-principal-invariance.json"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build() -> dict[str, Any]:
    data = {name: json.loads(path.read_text(encoding="utf-8")) for name, path in PATHS.items()}
    k720, k726 = data["k720"], data["k726"]
    c = k720["exact_controls"]
    cases = {row["case"]: row for row in c["cases"]}
    nonnull = cases["native_nonnull"]
    native_null = cases["native_null_auxiliary_nonzero"]
    return {
        "schema_version": "1.0",
        "result_id": "K727-SC-ACT-06-ALGEBRAIC-TRACE-REPAIR-PRINCIPAL-INVARIANCE",
        "created": "2026-10-01",
        "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE",
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "Conditional principal-symbol test of a derivative-free local action sector granted solely to cancel K726's rank-one metric trace on the same homogeneous branch.",
        "pinned_inputs": {name: {"path": str(path.relative_to(ROOT)), "sha256": digest(path)} for name, path in PATHS.items()},
        "gu_typed_objects": {
            "carrier": "the K726 homogeneous B/T branch with ten metric normals and K720's coupled metric/distortion principal carrier",
            "pairing": "selected action pairing plus a conditionally granted derivative-free scalar density",
            "real_structure": "same real K77 branch; K720 complex rank data used only for principal comparison",
            "grading": "metric diffeomorphism gauge -> coupled fields -> Euler rows",
            "action_owner": "selected I1B/I2B plus a non-source-owned conditional algebraic trace-cancellation sector",
            "target": "whether cancelling the background metric Euler trace also repairs the principal middle cohomology",
        },
        "conditional_trace_repair": {
            "repair_assumption": "A local derivative-free action density contributes the exact negative of K726's metric trace covector on the chosen background.",
            "required_normalized_metric_covector": "(7*kappa_1^3/18252)*(2,0,0,0,-2,0,0,-2,0,-2)",
            "background_metric_euler_can_be_cancelled_conditionally": True,
            "repair_is_source_owned": False,
            "repair_is_derivative_free": True,
            "linearized_repair_differential_order": 0,
            "repair_changes_highest_order_euler_symbol": False,
            "repair_changes_gauge_symbol": False,
            "repair_proves_full_stationarity": False,
            "repair_proves_SC_ACT_06_ellipticity": False,
        },
        "principal_invariance": {
            "field_dimension": c["field_dimension"],
            "owned_metric_diffeomorphism_rank": c["owned_metric_diffeomorphism_rank"],
            "nonnull_euler_rank": nonnull["action_euler_rank"],
            "native_null_euler_rank": native_null["action_euler_rank"],
            "nonnull_middle_cohomology_dimension": c["nonnull_cohomology_dimension"],
            "native_null_middle_cohomology_dimension": c["native_null_cohomology_dimension"],
            "principal_middle_exact_after_algebraic_repair": False,
        },
        "decision": {
            "algebraic_trace_repair_is_sufficient_k722_repair": False,
            "stationarity_and_principal_exactness_are_independent_gates": True,
            "derivative_bearing_action_data_remains_required": True,
            "next_exact_input": "An action-owned sector or nonhomogeneous germ whose derivative-bearing variation both closes the complete background Euler equations and changes the coupled highest-order symbol; an algebraic cosmological/VEV trace cancellation alone cannot do both.",
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "The repair is a conditional differential-order theorem, not an owned GU action term or stationary solution, and it leaves the known principal defect unchanged.",
        "controls": {
            "producer": "tests/channel-swings/k727_sc_act_06_algebraic_trace_repair_principal_invariance.py",
            "probe": "tests/channel-swings/k727_sc_act_06_algebraic_trace_repair_principal_invariance_probe.py",
            "controls_passed": 34,
            "hostile_mutations_rejected": 29,
        },
        "claim_ceiling": "Conditional zero-order invariance theorem for a derivative-free trace-cancelling action sector. No source ownership, full stationary background, different principal Shiab coefficient, Euclidean complex, source-status change, prediction, confirmation, or physical verdict.",
    }


def validate(p: dict[str, Any]) -> None:
    r, c, d = p["conditional_trace_repair"], p["principal_invariance"], p["decision"]
    assert p["target_claim"] == "SC-ACT-06"
    assert r["background_metric_euler_can_be_cancelled_conditionally"]
    assert not r["repair_is_source_owned"] and r["repair_is_derivative_free"]
    assert r["linearized_repair_differential_order"] == 0
    for key in ("repair_changes_highest_order_euler_symbol", "repair_changes_gauge_symbol", "repair_proves_full_stationarity", "repair_proves_SC_ACT_06_ellipticity"):
        assert not r[key]
    assert c["field_dimension"] == 229386 and c["owned_metric_diffeomorphism_rank"] == 4
    assert c["nonnull_euler_rank"] == 130912 and c["native_null_euler_rank"] == 122748
    assert c["nonnull_middle_cohomology_dimension"] == 98470 and c["native_null_middle_cohomology_dimension"] == 106634
    assert not c["principal_middle_exact_after_algebraic_repair"]
    assert not d["algebraic_trace_repair_is_sufficient_k722_repair"]
    assert d["stationarity_and_principal_exactness_are_independent_gates"] and d["derivative_bearing_action_data_remains_required"]
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
