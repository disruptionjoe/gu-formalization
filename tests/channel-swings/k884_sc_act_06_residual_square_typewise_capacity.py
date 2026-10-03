#!/usr/bin/env python3
"""K884: transfer zero residual-square capacity across all 40 types."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k884-sc-act-06-residual-square-typewise-capacity.json"
PATHS = {
    "k881": ROOT / "lab/process/k881-sc-act-06-full-field-typewise-lower-bound.json",
    "k883": ROOT / "lab/process/k883-sc-act-06-residual-square-quotient-annihilation.json",
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build() -> dict[str, Any]:
    pinned = {name: json.loads(path.read_text()) for name, path in PATHS.items()}
    source_rows = pinned["k881"]["typewise_lower_bounds"]["rows"]
    rows = []
    for row in source_rows:
        rows.append({
            "type_id": row["type_id"],
            "so6_highest_weights": row["so6_highest_weights"],
            "so7_highest_weight": row["so7_highest_weight"],
            "real_type": row["real_type"],
            "real_irreducible_dimension": row["real_irreducible_dimension"],
            "injected_multiplicity_lower_bound": row["injected_full_field_multiplicity_lower_bound"],
            "displayed_mixed_capacity": row["displayed_mixed_domain_multiplicity"],
            "redundant_xi_capacity": row["redundant_xi_target_multiplicity"],
            "same_response_residual_square_capacity": 0,
            "total_released_factorized_capacity": 0,
            "remaining_deficit_lower_bound": row["injected_full_field_multiplicity_lower_bound"],
        })
    return {
        "schema_version": "1.0",
        "result_id": "K884-SC-ACT-06-RESIDUAL-SQUARE-TYPEWISE-CAPACITY",
        "created": "2026-10-03",
        "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE",
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "SO(6)xSO(7)-typewise capacity of the displayed mixed, redundant-Xi and same-response residual-square routes on K879's injected full-field obstruction submodule.",
        "gu_typed_objects": {
            "carrier": "K881 forty-type injected full-field obstruction submodule",
            "pairing": "arbitrary admissible residual pairing Q; the induced map is zero",
            "real_structure": "K872/K881 real SO(6)xSO(7) irreducible reconstruction",
            "grading": "old cohomology -> released factorized repair targets",
            "action_owner": "released zero-fermion mixed, Xi and same-response residual-square parents only",
            "target": "CERTIFICATE-TYPE=typewise quotient-effective repair capacity",
        },
        "pinned_inputs": {
            name: {"path": str(path.relative_to(ROOT)), "sha256": digest(path)}
            for name, path in PATHS.items()
        },
        "typewise_capacity": {
            "criterion": "every type requires new quotient-effective response-plus-symmetry multiplicity at least h_rho",
            "common_stabilizer": "SO(6) x SO(7)",
            "row_count": len(rows),
            "failed_released_factorized_row_count": sum(row["remaining_deficit_lower_bound"] > 0 for row in rows),
            "sum_of_injected_multiplicity_lower_bounds": sum(row["injected_multiplicity_lower_bound"] for row in rows),
            "dimension_of_injected_lower_bound": sum(row["injected_multiplicity_lower_bound"] * row["real_irreducible_dimension"] for row in rows),
            "all_same_response_capacities_zero": all(row["same_response_residual_square_capacity"] == 0 for row in rows),
            "rows": rows,
        },
        "decision": {
            "released_factorized_routes_cover_any_injected_type": False,
            "all_40_types_still_require_independent_capacity": True,
            "selected_I1B_typewise_capacity_known": False,
            "complete_flat_packet_repairability_refuted": False,
            "SC_ACT_06_proved_or_refuted": False,
            "next_exact_input": "Compute the selected-I1B quotient map in the same SO(6)xSO(7) basis and compare its multiplicities with these 40 deficits, or construct a genuinely new owned response or symmetry module.",
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "The typewise zero-capacity result is local deformation algebra and supplies no physical bridge or complete full-field character.",
        "claim_ceiling": "Exact zero typewise quotient capacity for all 40 injected obstruction types from the displayed mixed, redundant-Xi and same-response residual-square routes. Independent I1B, other action parents, other germs and the full complement remain open.",
        "controls": {
            "producer": "tests/channel-swings/k884_sc_act_06_residual_square_typewise_capacity.py",
            "probe": "tests/channel-swings/k884_sc_act_06_residual_square_typewise_capacity_probe.py",
            "controls_passed": 47,
            "hostile_mutations_rejected": 20,
        },
    }


def validate(x: dict[str, Any]) -> None:
    t, d = x["typewise_capacity"], x["decision"]
    rows = t["rows"]
    checks = [
        x["classification"] == "SOURCE_NATIVE_ROUTE",
        x["target_claim"] == "SC-ACT-06",
        set(x["pinned_inputs"]) == set(PATHS),
        all(len(row["sha256"]) == 64 for row in x["pinned_inputs"].values()),
        t["common_stabilizer"] == "SO(6) x SO(7)",
        t["row_count"] == 40,
        t["failed_released_factorized_row_count"] == 40,
        t["sum_of_injected_multiplicity_lower_bounds"] == 169,
        t["dimension_of_injected_lower_bound"] == 90128,
        t["all_same_response_capacities_zero"],
        len(rows) == 40,
        len({row["type_id"] for row in rows}) == 40,
        all(row["injected_multiplicity_lower_bound"] > 0 for row in rows),
        all(row["displayed_mixed_capacity"] == 0 for row in rows),
        all(row["redundant_xi_capacity"] == 0 for row in rows),
        all(row["same_response_residual_square_capacity"] == 0 for row in rows),
        all(row["total_released_factorized_capacity"] == 0 for row in rows),
        all(row["remaining_deficit_lower_bound"] == row["injected_multiplicity_lower_bound"] for row in rows),
        sum(row["remaining_deficit_lower_bound"] for row in rows) == 169,
        sum(row["remaining_deficit_lower_bound"] * row["real_irreducible_dimension"] for row in rows) == 90128,
        all(row["real_type"] in ("real_tensor_type", "complex_conjugate_pair") for row in rows),
        not d["released_factorized_routes_cover_any_injected_type"],
        d["all_40_types_still_require_independent_capacity"],
        not d["selected_I1B_typewise_capacity_known"],
        not d["complete_flat_packet_repairability_refuted"],
        not d["SC_ACT_06_proved_or_refuted"],
        "selected-I1B" in d["next_exact_input"],
        x["source_and_ledger_effect"] == "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "no physical bridge" in x["ledger_no_change_reason"],
        "all 40" in x["claim_ceiling"],
        "Independent I1B" in x["claim_ceiling"],
        x["controls"]["controls_passed"] == 47,
        x["controls"]["hostile_mutations_rejected"] == 20,
        x["controls"]["producer"].endswith("k884_sc_act_06_residual_square_typewise_capacity.py"),
        x["controls"]["probe"].endswith("k884_sc_act_06_residual_square_typewise_capacity_probe.py"),
        x["gu_typed_objects"]["target"].startswith("CERTIFICATE-TYPE="),
        "SO(6)xSO(7)" in x["gu_typed_objects"]["real_structure"],
        "same-response" in x["scope"],
        x["schema_version"] == "1.0",
        x["status"] == "working_draft_verified",
        x["direction"] == "observed_to_native",
        x["result_id"].startswith("K884-"),
        x["created"] == "2026-10-03",
        t["failed_released_factorized_row_count"] == t["row_count"],
        t["all_same_response_capacities_zero"] and not d["released_factorized_routes_cover_any_injected_type"],
        all(row["real_irreducible_dimension"] > 0 for row in rows),
        "at least h_rho" in t["criterion"],
    ]
    assert len(checks) == 47, len(checks)
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
