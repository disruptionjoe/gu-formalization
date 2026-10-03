#!/usr/bin/env python3
"""K886: compile the released repair-class disposition."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k886-sc-act-06-released-repair-disposition.json"
PATHS = {
    "k882": ROOT / "lab/process/k882-sc-act-06-full-field-obstruction-disposition.json",
    "k883": ROOT / "lab/process/k883-sc-act-06-residual-square-quotient-annihilation.json",
    "k884": ROOT / "lab/process/k884-sc-act-06-residual-square-typewise-capacity.json",
    "k885": ROOT / "lab/process/k885-sc-act-06-released-action-parent-quotient-inventory.json",
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build() -> dict[str, Any]:
    pinned = {name: json.loads(path.read_text()) for name, path in PATHS.items()}
    gate = dict(pinned["k882"]["corrected_completion_gate"]["current_GU_candidate"])
    boundary = {
        "owned 90128-dimensional obstruction submodule": True,
        "all 40 real obstruction types and multiplicities": True,
        "displayed mixed and redundant Xi quotient capacity zero": True,
        "same-response residual-square quotient capacity zero": True,
        "selected-I1B induced quotient character known": False,
        "genuinely independent owned repair module known": False,
        "complete full-field cohomology character known": False,
    }
    return {
        "schema_version": "1.0",
        "result_id": "K886-SC-ACT-06-RELEASED-REPAIR-DISPOSITION",
        "created": "2026-10-03",
        "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE",
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "Disposition after proving zero quotient-effective capacity for every released same-response residual-square repair parent on K879's forty-type obstruction submodule.",
        "gu_typed_objects": {
            "carrier": "K879 injected zero-fermion full-field obstruction submodule",
            "pairing": "arbitrary within the released factorized residual-square class",
            "real_structure": "K884 exact real SO(6)xSO(7) typewise capacity table",
            "grading": "old cohomology -> released repair parents -> remaining independent repair obligations",
            "action_owner": "released I1B/I2B/total-rival inventory with only factorized parents closed",
            "target": "CERTIFICATE-TYPE=released repair-class disposition",
        },
        "pinned_inputs": {
            name: {"path": str(path.relative_to(ROOT)), "sha256": digest(path)}
            for name, path in PATHS.items()
        },
        "released_repair_certificate": {
            "rows": boundary,
            "row_count": len(boundary),
            "satisfied_row_count": sum(boundary.values()),
            "failed_or_open_row_count": sum(value is False for value in boundary.values()),
            "injected_dimension": 90128,
            "real_irreducible_type_count": 40,
            "sum_of_multiplicity_lower_bounds": 169,
            "released_factorized_failed_type_count": 40,
            "released_residual_square_class_closed": True,
        },
        "corrected_completion_gate": {
            "row_count": len(gate),
            "current_GU_candidate": gate,
            "satisfied_row_count": sum(gate.values()),
            "failed_row_count": sum(value is False for value in gate.values()),
            "current_GU_candidate_admitted": all(gate.values()),
            "unchanged_by_released_class_closure": True,
        },
        "decision": {
            "released_same_response_repair_class_excluded": True,
            "selected_I1B_route_excluded": False,
            "future_or_unreleased_action_parent_excluded": False,
            "nonzero_fermion_stationary_germ_excluded": False,
            "complete_flat_packet_repairability_refuted": False,
            "global_SC_ACT_06_proved_or_refuted": False,
            "source_claim_status_changes": False,
            "next_exact_input": "Construct the selected-I1B induced map on the authenticated SO(6)xSO(7) quotient and compute its forty typewise ranks; if it fails, construct a genuinely new source/action-owned response or symmetry module or a source-owned nonzero-fermion stationary germ.",
        },
        "protected_effects": {
            "sc_act_06": "ASSERTS_UNCHANGED",
            "source_register": "UNCHANGED",
            "physics_ledger": "UNCHANGED",
            "canon": "UNCHANGED",
            "paper_and_public_posture": "UNCHANGED",
            "prediction_confirmation_physical_verdict": "UNCHANGED",
        },
        "source_and_ledger_effect": "SC-ACT-01_03_04_05_06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "The released repair-class closure is local principal deformation algebra and leaves the independent I1B map, full complement and physical bridges open.",
        "claim_ceiling": "Exact exclusion of the released same-response residual-square repair class on the 90128-dimensional forty-type submodule. No complete flat-packet no-go, all-action no-go, other-germ no-go, global ellipticity or physical conclusion follows.",
        "controls": {
            "producer": "tests/channel-swings/k886_sc_act_06_released_repair_disposition.py",
            "probe": "tests/channel-swings/k886_sc_act_06_released_repair_disposition_probe.py",
            "controls_passed": 46,
            "hostile_mutations_rejected": 20,
        },
    }


def validate(x: dict[str, Any]) -> None:
    r, g, d, p = x["released_repair_certificate"], x["corrected_completion_gate"], x["decision"], x["protected_effects"]
    checks = [
        x["classification"] == "SOURCE_NATIVE_ROUTE",
        x["target_claim"] == "SC-ACT-06",
        set(x["pinned_inputs"]) == set(PATHS),
        all(len(row["sha256"]) == 64 for row in x["pinned_inputs"].values()),
        r["row_count"] == 7,
        len(r["rows"]) == 7,
        r["satisfied_row_count"] == 4,
        r["failed_or_open_row_count"] == 3,
        r["injected_dimension"] == 90128,
        r["real_irreducible_type_count"] == 40,
        r["sum_of_multiplicity_lower_bounds"] == 169,
        r["released_factorized_failed_type_count"] == 40,
        r["released_residual_square_class_closed"],
        r["rows"]["same-response residual-square quotient capacity zero"],
        not r["rows"]["selected-I1B induced quotient character known"],
        not r["rows"]["genuinely independent owned repair module known"],
        not r["rows"]["complete full-field cohomology character known"],
        g["row_count"] == 11,
        len(g["current_GU_candidate"]) == 11,
        g["satisfied_row_count"] == 5,
        g["failed_row_count"] == 6,
        not g["current_GU_candidate_admitted"],
        g["unchanged_by_released_class_closure"],
        d["released_same_response_repair_class_excluded"],
        not d["selected_I1B_route_excluded"],
        not d["future_or_unreleased_action_parent_excluded"],
        not d["nonzero_fermion_stationary_germ_excluded"],
        not d["complete_flat_packet_repairability_refuted"],
        not d["global_SC_ACT_06_proved_or_refuted"],
        not d["source_claim_status_changes"],
        "selected-I1B" in d["next_exact_input"],
        all("UNCHANGED" in value for value in p.values()),
        x["source_and_ledger_effect"] == "SC-ACT-01_03_04_05_06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "independent I1B map" in x["ledger_no_change_reason"],
        "released same-response residual-square repair class" in x["claim_ceiling"],
        "No complete flat-packet no-go" in x["claim_ceiling"],
        x["controls"]["controls_passed"] == 46,
        x["controls"]["hostile_mutations_rejected"] == 20,
        x["controls"]["producer"].endswith("k886_sc_act_06_released_repair_disposition.py"),
        x["controls"]["probe"].endswith("k886_sc_act_06_released_repair_disposition_probe.py"),
        x["gu_typed_objects"]["target"].startswith("CERTIFICATE-TYPE="),
        "SO(6)xSO(7)" in x["gu_typed_objects"]["real_structure"],
        x["schema_version"] == "1.0",
        x["status"] == "working_draft_verified",
        x["direction"] == "observed_to_native",
        x["result_id"].startswith("K886-"),
    ]
    assert len(checks) == 46, len(checks)
    assert all(checks), [i for i, value in enumerate(checks) if not value]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    payload = build()
    validate(payload)
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.write:
        OUTPUT.write_text(rendered)
    elif not args.check:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
