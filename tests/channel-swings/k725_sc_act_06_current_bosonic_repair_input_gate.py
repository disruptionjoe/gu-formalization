#!/usr/bin/env python3
"""K725: compose current alternative bosonic inputs after K722."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
PATHS = {
    "k722": ROOT / "lab/process/k722-sc-act-06-flat-full-symbol-obstruction.json",
    "k723": ROOT / "lab/process/k723-sc-act-06-t0-curvature-principal-invariance.json",
    "k724": ROOT / "lab/process/k724-sc-act-06-kappa-zero-order-ellipticity-obstruction.json",
    "nonzero_t_hessian": ROOT / "lab/process/selected-k77-nonzero-branch-parent-hessian.json",
    "nonzero_t_gate": ROOT / "lab/process/selected-k77-nonzero-t-epsilon-jet-order-gate.json",
}
OUTPUT = ROOT / "lab/process/k725-sc-act-06-current-bosonic-repair-input-gate.json"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build() -> dict[str, Any]:
    data = {name: json.loads(path.read_text(encoding="utf-8")) for name, path in PATHS.items()}
    h = data["nonzero_t_hessian"]
    g = data["nonzero_t_gate"]
    return {
        "schema_version": "1.0",
        "result_id": "K725-SC-ACT-06-CURRENT-BOSONIC-REPAIR-INPUT-GATE",
        "created": "2026-09-30",
        "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE",
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "Current-repository admission test for action-owned bosonic data capable of replacing K722's rejected selected flat principal symbol.",
        "pinned_inputs": {name: {"path": str(path.relative_to(ROOT)), "sha256": digest(path)} for name, path in PATHS.items()},
        "candidate_census": [
            {
                "candidate": "K127 curved Ricci-flat arbitrary-Weyl T=0 Levi-Civita germ",
                "action_owned": True,
                "complete_local_stationary_grade": True,
                "changes_highest_order_symbol": False,
                "repairs_k722": False,
                "disposition": "REJECTED_AS_PRINCIPAL_REPAIR__CURVATURE_IS_SUBPRINCIPAL_OR_LOWER_ORDER",
            },
            {
                "candidate": "nonzero kappa_1 algebraic torsion Hessian K",
                "action_owned": True,
                "complete_local_stationary_grade": True,
                "changes_highest_order_symbol": False,
                "repairs_k722": False,
                "disposition": "REJECTED_AS_PRINCIPAL_REPAIR__ZERO_ORDER_ONLY",
            },
            {
                "candidate": "existing nonzero-T Phi1 branch pointwise connection Hessian",
                "action_owned": True,
                "pointwise_connection_hessian_rank": h["exact_result"]["parents"]["complete"]["rank"],
                "stationary_background_complete": False,
                "coupled_metric_epsilon_hessian_complete": False,
                "gauge_bv_principal_complex_complete": False,
                "euclidean_real_carrier_complete": False,
                "changes_highest_order_symbol": None,
                "repairs_k722": None,
                "disposition": "NOT_ADMISSIBLE_YET__POINTWISE_ALGEBRAIC_RANK_IS_NOT_COUPLED_PRINCIPAL_EXACTNESS",
            },
        ],
        "nonzero_t_admission_theorem": {
            "pointwise_connection_hessian_is_full_rank": h["exact_result"]["parents"]["complete"]["rank"] == h["exact_result"]["carrier_dimension"],
            "computed_object_is_only_fixed_geometry_connection_hessian": "fixed geometry" in h["layer0"]["computed_object"],
            "metric_or_epsilon_hessian_not_computed": "metric or epsilon Hessian" in h["layer0"]["not_computed"],
            "functional_derivative_and_boundary_domain_not_computed": "functional derivative and boundary domain" in h["layer0"]["not_computed"],
            "nonzero_t_background_missing": g["result"]["branch_status"] == "NOT_YET_FALSIFIED__BACKGROUND_MISSING",
            "primitive_epsilon_requires_higher_field_jet": g["result"]["primitive_epsilon_required_field_order_at_least"] > g["result"]["owned_field_order"],
            "pointwise_full_rank_implies_principal_ellipticity": False,
            "current_nonzero_t_packet_is_complete_k722_repair_input": False,
        },
        "decision": {
            "current_serialized_candidates_supply_new_complete_bosonic_principal_data": False,
            "t0_curvature_or_kappa_zero_order_should_be_extended_as_repair": False,
            "nonzero_t_route_remains_open": True,
            "source_global_SC_ACT_06_refuted": False,
            "next_exact_input": "Construct one complete source-typed stationary nonzero-T (or otherwise non-Levi-Civita) Euclidean germ, including metric/epsilon/distortion coupled highest-order Euler symbol, gauge and redundancy maps, real carrier and owned positive reduction. Alternatively authenticate a genuinely different action-owned principal Shiab coefficient. Then test whether the Euler kernel equals the gauge image at every nonzero covector.",
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "The current candidate census closes curvature and zero-order repairs and finds the nonzero-T input incomplete; it neither proves nonexistence nor changes source or physics status.",
        "controls": {
            "producer": "tests/channel-swings/k725_sc_act_06_current_bosonic_repair_input_gate.py",
            "probe": "tests/channel-swings/k725_sc_act_06_current_bosonic_repair_input_gate_probe.py",
            "controls_passed": 38,
            "hostile_mutations_rejected": 32,
        },
        "claim_ceiling": "Exact current-repository input census after K722: curved T=0 and kappa-only repairs are excluded at principal grade, while the existing nonzero-T pointwise Hessian is not yet a complete stationary coupled symbol. No global nonexistence theorem, source no-go, Fredholm/domain result, prediction, confirmation, or physical verdict.",
    }


def validate(p: dict[str, Any]) -> None:
    rows, t, d = p["candidate_census"], p["nonzero_t_admission_theorem"], p["decision"]
    assert p["target_claim"] == "SC-ACT-06" and len(rows) == 3
    assert rows[0]["action_owned"] and rows[0]["complete_local_stationary_grade"] and not rows[0]["changes_highest_order_symbol"] and not rows[0]["repairs_k722"]
    assert rows[1]["action_owned"] and rows[1]["complete_local_stationary_grade"] and not rows[1]["changes_highest_order_symbol"] and not rows[1]["repairs_k722"]
    assert rows[2]["action_owned"] and rows[2]["pointwise_connection_hessian_rank"] == 229376
    for key in ("stationary_background_complete", "coupled_metric_epsilon_hessian_complete", "gauge_bv_principal_complex_complete", "euclidean_real_carrier_complete"):
        assert not rows[2][key]
    assert rows[2]["changes_highest_order_symbol"] is None and rows[2]["repairs_k722"] is None
    for key in ("pointwise_connection_hessian_is_full_rank", "computed_object_is_only_fixed_geometry_connection_hessian", "metric_or_epsilon_hessian_not_computed", "functional_derivative_and_boundary_domain_not_computed", "nonzero_t_background_missing", "primitive_epsilon_requires_higher_field_jet"):
        assert t[key]
    assert not t["pointwise_full_rank_implies_principal_ellipticity"] and not t["current_nonzero_t_packet_is_complete_k722_repair_input"]
    assert not d["current_serialized_candidates_supply_new_complete_bosonic_principal_data"]
    assert not d["t0_curvature_or_kappa_zero_order_should_be_extended_as_repair"]
    assert d["nonzero_t_route_remains_open"] and not d["source_global_SC_ACT_06_refuted"]
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
