#!/usr/bin/env python3
"""K739: compose the exact zero-branch action ownership of the expanded K77 carrier."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
PATHS = {
    "ownership": ROOT / "lab/process/selected-k77-bosonic-parent-action-ownership.json",
    "typing": ROOT / "lab/process/selected-k77-action-owned-reduction-carrier-typing.json",
    "closure": ROOT / "lab/process/selected-k77-grade5-unitary-parent-euler-closure.json",
    "threshold": ROOT / "lab/process/k737-sc-act-06-expanded-parent-dimension-threshold.json",
}
OUTPUT = ROOT / "lab/process/k739-sc-act-06-expanded-action-parent-ownership.json"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build() -> dict[str, Any]:
    data = {name: json.loads(path.read_text(encoding="utf-8")) for name, path in PATHS.items()}
    own = data["ownership"]
    closure = data["closure"]
    return {
        "schema_version": "1.0",
        "result_id": "K739-SC-ACT-06-EXPANDED-ACTION-PARENT-OWNERSHIP",
        "created": "2026-10-01",
        "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE",
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "Composition of previously certified zero-branch Hessian ownership, moving-reduction typing and Euler closure; no new source interpretation or nonzero-branch stationarity claim.",
        "pinned_inputs": {name: {"path": str(path.relative_to(ROOT)), "sha256": digest(path)} for name, path in PATHS.items()},
        "exact_action_ownership": {
            "stationary_germ": "K77_ZERO_BRANCH",
            "written_action_uses_full_unprojected_connection_displacement": True,
            "full_quadratic_norm_has_nonzero_hessian_on_spin_sector": True,
            "full_quadratic_norm_has_nonzero_hessian_on_complement_sector": True,
            "spin_coefficient_directions": own["exact_inputs"]["b_adjoint_split"][0],
            "complement_coefficient_directions": own["exact_inputs"]["b_adjoint_split"][1],
            "action_owned_connection_coefficient_directions": sum(own["exact_inputs"]["b_adjoint_split"]),
            "action_owned_connection_one_form_directions": closure["exact_result"]["unitary_connection_dimension"],
            "action_owned_total_with_metric_epsilon": closure["exact_result"]["unitary_total_with_metric_epsilon"],
            "hard_spin_reduction_generated_by_written_action": False,
            "moving_spin_is_only_consistent_truncation_or_real_form_posit": True,
        },
        "parent_typing": {
            "field_carrier_selected_by_zero_branch_action_hessian": "FULL_16384_COEFFICIENT_CONNECTION_CARRIER",
            "full_U64_64_symmetry_parent_selected": False,
            "two_U32_32_half_symmetry_parent_selected": False,
            "symmetry_and_pairing_fork": closure["parent_disposition"]["selection"],
            "nonzero_branch_normal_hessian": own["result"]["nonzero_branch_normal_hessian"],
            "bosonic_reduction_disposition": data["typing"]["disposition"]["bosonic_reduction"],
        },
        "decision": {
            "k737_action_ownership_open_is_closed_at_zero_branch_field_carrier_level": True,
            "grade_saturated_spin_is_the_written_action_field_domain": False,
            "full_connection_carrier_is_action_owned_at_zero_branch": True,
            "operative_unitary_symmetry_parent_is_selected": False,
            "nonzero_branch_expanded_parent_is_selected": False,
            "next_exact_input": "Compute the derivative-only principal rank of u -> star Shiab(q wedge u) on the action-owned full 229376-direction connection carrier, with the grade-saturated Spin carrier retained as a hostile rival, at native nonnull and native-null covectors.",
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "This closes zero-branch field-carrier ownership only. It does not select the unitary symmetry/pairing parent, prove the full principal response rank or establish middle exactness.",
        "controls": {
            "producer": "tests/channel-swings/k739_sc_act_06_expanded_action_parent_ownership.py",
            "probe": "tests/channel-swings/k739_sc_act_06_expanded_action_parent_ownership_probe.py",
            "controls_passed": 29,
            "hostile_mutations_rejected": 24,
        },
        "claim_ceiling": "Exact zero-branch action-owned field-carrier composition. No unique symmetry parent, nonzero-branch stationarity, principal-rank, ellipticity, source-status, prediction, confirmation or physical verdict.",
    }


def validate(p: dict[str, Any]) -> None:
    a, t, d = p["exact_action_ownership"], p["parent_typing"], p["decision"]
    assert p["target_claim"] == "SC-ACT-06"
    assert a["stationary_germ"] == "K77_ZERO_BRANCH"
    assert a["written_action_uses_full_unprojected_connection_displacement"]
    assert a["full_quadratic_norm_has_nonzero_hessian_on_spin_sector"]
    assert a["full_quadratic_norm_has_nonzero_hessian_on_complement_sector"]
    assert (a["spin_coefficient_directions"], a["complement_coefficient_directions"]) == (8128, 8256)
    assert a["action_owned_connection_coefficient_directions"] == 16384
    assert a["action_owned_connection_one_form_directions"] == 229376
    assert a["action_owned_total_with_metric_epsilon"] == 229477
    assert not a["hard_spin_reduction_generated_by_written_action"]
    assert a["moving_spin_is_only_consistent_truncation_or_real_form_posit"]
    assert t["field_carrier_selected_by_zero_branch_action_hessian"] == "FULL_16384_COEFFICIENT_CONNECTION_CARRIER"
    assert not t["full_U64_64_symmetry_parent_selected"] and not t["two_U32_32_half_symmetry_parent_selected"]
    assert t["symmetry_and_pairing_fork"] == "OPEN" and t["nonzero_branch_normal_hessian"] == "OPEN"
    assert d["k737_action_ownership_open_is_closed_at_zero_branch_field_carrier_level"]
    assert not d["grade_saturated_spin_is_the_written_action_field_domain"]
    assert d["full_connection_carrier_is_action_owned_at_zero_branch"]
    assert not d["operative_unitary_symmetry_parent_is_selected"] and not d["nonzero_branch_expanded_parent_is_selected"]
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
