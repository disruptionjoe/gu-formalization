#!/usr/bin/env python3
"""K737: dimension threshold for the open expanded-parent fork."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
PATHS = {
    "k735": ROOT / "lab/process/k735-sc-act-06-source-low-grade-i2b-rank-ceiling.json",
    "k736": ROOT / "lab/process/k736-sc-act-06-source-low-grade-bosonic-repair-obstruction.json",
    "parent_closure": ROOT / "lab/process/selected-k77-grade5-unitary-parent-euler-closure.json",
    "moving_parent": ROOT / "lab/process/selected-k77-moving-parent-bundle-observation-reduction.json",
}
OUTPUT = ROOT / "lab/process/k737-sc-act-06-expanded-parent-dimension-threshold.json"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build() -> dict[str, Any]:
    data = {name: json.loads(path.read_text(encoding="utf-8")) for name, path in PATHS.items()}
    low = data["k735"]["selected_low_grade_tangent"]
    cases = data["k736"]["exact_controls"]["cases"]
    closure = data["parent_closure"]["exact_result"]
    moving = data["moving_parent"]["global_carriers"]
    requirements = [row["minimum_new_rank_required_for_middle_exactness"] for row in cases]
    outside = [row["minimum_rank_required_outside_selected_low_grade"] for row in cases]
    candidates = []
    for name, dimension, ownership in (
        ("observed_conditional", low["observed_conditional_tangent"], "conditional conormal restriction or BV differential unowned"),
        ("selected_low_grade", low["source_native_y14_first_jet_total"], "selected low-grade source-native tangent"),
        ("grade_saturated_spin", closure["spin_total_with_metric_epsilon"], "proper Euler-closed rival; operative action projector unselected"),
        ("full_unitary", closure["unitary_total_with_metric_epsilon"], "source full-U parent; operative action parent unselected"),
    ):
        candidates.append({
            "candidate": name,
            "dimension": dimension,
            "ownership": ownership,
            "dimension_meets_nonnull_requirement": dimension >= requirements[0],
            "dimension_meets_native_null_requirement": dimension >= requirements[1],
            "dimension_meets_both_requirements": dimension >= max(requirements),
            "nonnull_dimension_margin": dimension - requirements[0],
            "native_null_dimension_margin": dimension - requirements[1],
            "actual_response_rank_proved": False,
            "middle_exactness_proved": False,
        })
    return {
        "schema_version": "1.0",
        "result_id": "K737-SC-ACT-06-EXPANDED-PARENT-DIMENSION-THRESHOLD",
        "created": "2026-10-01",
        "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE",
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "Dimension-only classification of certified selected and expanded K77 parent carriers against K720's exact repair thresholds; no parent is selected and no response rank is inferred from carrier dimension.",
        "pinned_inputs": {name: {"path": str(path.relative_to(ROOT)), "sha256": digest(path)} for name, path in PATHS.items()},
        "exact_thresholds": {
            "minimum_total_new_rank_nonnull": requirements[0],
            "minimum_total_new_rank_native_null": requirements[1],
            "selected_low_grade_ceiling": low["i2b_hessian_rank_ceiling"],
            "minimum_rank_outside_low_grade_nonnull": outside[0],
            "minimum_rank_outside_low_grade_native_null": outside[1],
            "spin_directions_outside_low_grade": closure["spin_total_with_metric_epsilon"] - low["source_native_y14_first_jet_total"],
            "unitary_directions_outside_low_grade": closure["unitary_total_with_metric_epsilon"] - low["source_native_y14_first_jet_total"],
        },
        "candidate_parent_classification": candidates,
        "ownership_controls": {
            "moving_spin_total_agrees": moving["moving_spin_total"] == closure["spin_total_with_metric_epsilon"],
            "full_unitary_total_agrees": moving["full_u_total"] == closure["unitary_total_with_metric_epsilon"],
            "moving_parent_selection": moving["selection"],
            "parent_closure_selection": data["parent_closure"]["parent_disposition"]["selection"],
            "dimension_is_not_response_rank": True,
            "dimension_is_not_action_ownership": True,
            "dimension_is_not_middle_exactness": True,
        },
        "decision": {
            "observed_and_selected_low_grade_parents_dimensionally_insufficient": True,
            "grade_saturated_spin_parent_dimensionally_capable": True,
            "full_unitary_parent_dimensionally_capable": True,
            "expanded_parent_action_selection_remains_open": True,
            "expanded_parent_actual_i2b_rank_remains_open": True,
            "source_global_SC_ACT_06_refuted": False,
            "next_exact_input": "Select or derive the operative expanded action parent on one stationary source-typed Euclidean germ, serialize its complete moving I2B response and actual gauge/redundancy maps, and prove response rank at least 98470/106634 before testing middle exactness.",
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "The expanded Spin and unitary carriers pass only a necessary dimension test. Their action ownership, stationary background, response rank, Euclidean reduction and symbol complex remain open.",
        "controls": {
            "producer": "tests/channel-swings/k737_sc_act_06_expanded_parent_dimension_threshold.py",
            "probe": "tests/channel-swings/k737_sc_act_06_expanded_parent_dimension_threshold_probe.py",
            "controls_passed": 46,
            "hostile_mutations_rejected": 39,
        },
        "claim_ceiling": "Exact dimension-only parent classification. No parent selection, response-rank lower bound, stationarity, Euclidean owner, ellipticity, source-status change, prediction, confirmation or physical verdict.",
    }


def validate(p: dict[str, Any]) -> None:
    t, rows, o, d = p["exact_thresholds"], p["candidate_parent_classification"], p["ownership_controls"], p["decision"]
    assert p["target_claim"] == "SC-ACT-06"
    assert t == {
        "minimum_total_new_rank_nonnull": 98470,
        "minimum_total_new_rank_native_null": 106634,
        "selected_low_grade_ceiling": 1571,
        "minimum_rank_outside_low_grade_nonnull": 96899,
        "minimum_rank_outside_low_grade_native_null": 105063,
        "spin_directions_outside_low_grade": 112322,
        "unitary_directions_outside_low_grade": 227906,
    }
    assert rows == [
        {"candidate": "observed_conditional", "dimension": 1131, "ownership": "conditional conormal restriction or BV differential unowned", "dimension_meets_nonnull_requirement": False, "dimension_meets_native_null_requirement": False, "dimension_meets_both_requirements": False, "nonnull_dimension_margin": -97339, "native_null_dimension_margin": -105503, "actual_response_rank_proved": False, "middle_exactness_proved": False},
        {"candidate": "selected_low_grade", "dimension": 1571, "ownership": "selected low-grade source-native tangent", "dimension_meets_nonnull_requirement": False, "dimension_meets_native_null_requirement": False, "dimension_meets_both_requirements": False, "nonnull_dimension_margin": -96899, "native_null_dimension_margin": -105063, "actual_response_rank_proved": False, "middle_exactness_proved": False},
        {"candidate": "grade_saturated_spin", "dimension": 113893, "ownership": "proper Euler-closed rival; operative action projector unselected", "dimension_meets_nonnull_requirement": True, "dimension_meets_native_null_requirement": True, "dimension_meets_both_requirements": True, "nonnull_dimension_margin": 15423, "native_null_dimension_margin": 7259, "actual_response_rank_proved": False, "middle_exactness_proved": False},
        {"candidate": "full_unitary", "dimension": 229477, "ownership": "source full-U parent; operative action parent unselected", "dimension_meets_nonnull_requirement": True, "dimension_meets_native_null_requirement": True, "dimension_meets_both_requirements": True, "nonnull_dimension_margin": 131007, "native_null_dimension_margin": 122843, "actual_response_rank_proved": False, "middle_exactness_proved": False},
    ]
    assert o["moving_spin_total_agrees"] and o["full_unitary_total_agrees"]
    assert o["moving_parent_selection"] == "OPEN_ACTION_PROJECTOR_OWNERSHIP"
    assert o["parent_closure_selection"] == "OPEN"
    assert o["dimension_is_not_response_rank"] and o["dimension_is_not_action_ownership"] and o["dimension_is_not_middle_exactness"]
    assert all(d[k] for k in (
        "observed_and_selected_low_grade_parents_dimensionally_insufficient",
        "grade_saturated_spin_parent_dimensionally_capable",
        "full_unitary_parent_dimensionally_capable",
        "expanded_parent_action_selection_remains_open",
        "expanded_parent_actual_i2b_rank_remains_open",
    ))
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
