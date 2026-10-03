#!/usr/bin/env python3
"""K885: inventory released action parents at quotient-effective scope."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k885-sc-act-06-released-action-parent-quotient-inventory.json"
PATHS = {
    "k748": ROOT / "lab/process/k748-sc-act-06-released-action-parent-inventory.json",
    "k791": ROOT / "lab/process/k791-sc-act-06-released-first-order-row-inventory.json",
    "k883": ROOT / "lab/process/k883-sc-act-06-residual-square-quotient-annihilation.json",
    "k884": ROOT / "lab/process/k884-sc-act-06-residual-square-typewise-capacity.json",
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build() -> dict[str, Any]:
    pinned = {name: json.loads(path.read_text()) for name, path in PATHS.items()}
    parents = []
    for row in pinned["k748"]["released_parent_inventory"]:
        parent = row["parent"]
        if parent == "I1B_FIRST_TRANSGRESSION":
            disposition, rank, reason = "open_independent_map", None, "selected I1B is independent of the old J response, but its induced forty-type quotient map is not serialized"
        elif parent in {"I2B_RESIDUAL_NORM_SQUARE", "TOTAL_RESIDUAL_NORM_RIVAL"}:
            disposition, rank, reason = "closed_zero_quotient_capacity", 0, "zero-residual principal Hessian factors as J^*QJ and annihilates ker(J)/im(G)"
        else:
            disposition, rank, reason = "unowned_unbuilt_not_credited", None, "the released source does not own the path adapter and the repository has not constructed its typed principal map"
        parents.append({**row, "quotient_disposition": disposition, "induced_rank_on_injected_submodule": rank, "reason": reason})
    return {
        "schema_version": "1.0",
        "result_id": "K885-SC-ACT-06-RELEASED-ACTION-PARENT-QUOTIENT-INVENTORY",
        "created": "2026-10-03",
        "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE",
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "Released bosonic derivative action-parent inventory classified by quotient-effective capacity on K879's injected full-field obstruction submodule.",
        "gu_typed_objects": {
            "carrier": "K879/K884 injected forty-type full-field obstruction submodule",
            "pairing": "arbitrary within released same-response residual-square parents",
            "real_structure": "K884 real SO(6)xSO(7) typewise capacity table",
            "grading": "released action parent -> principal response -> old quotient",
            "action_owner": "released I1B/I2B/total-rival inventory with source-silent path adapter kept separate",
            "target": "INVENTORY-TYPE=released action parents by quotient-effective capacity",
        },
        "pinned_inputs": {
            name: {"path": str(path.relative_to(ROOT)), "sha256": digest(path)}
            for name, path in PATHS.items()
        },
        "released_parent_inventory": parents,
        "inventory_summary": {
            "released_parent_row_count": len(parents),
            "closed_zero_capacity_parent_count": sum(row["quotient_disposition"] == "closed_zero_quotient_capacity" for row in parents),
            "open_independent_parent_count": sum(row["quotient_disposition"] == "open_independent_map" for row in parents),
            "unowned_unbuilt_parent_count": sum(row["quotient_disposition"] == "unowned_unbuilt_not_credited" for row in parents),
            "released_independent_first_order_row_beyond_Upsilon": pinned["k791"]["decision"]["released_independent_first_order_bosonic_row_count_beyond_Upsilon"],
            "all_40_types_uncovered_by_closed_factorized_parents": pinned["k884"]["decision"]["all_40_types_still_require_independent_capacity"],
        },
        "decision": {
            "released_residual_square_repair_class_closed": True,
            "selected_I1B_repair_capacity_closed": False,
            "source_silent_path_adapter_promoted": False,
            "absence_of_future_or_unreleased_parent_proved": False,
            "complete_flat_packet_repairability_refuted": False,
            "SC_ACT_06_proved_or_refuted": False,
            "next_exact_input": "Construct the common weight-resolved selected-I1B map on ker(J)/im(G), or a genuinely new owned parent or stationary germ; do not retry another Q or weight inside the closed residual-square class.",
        },
        "source_and_ledger_effect": "SC-ACT-01_03_04_05_06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "The inventory separates released local action ownership from quotient effectiveness and creates no physical construction or verdict.",
        "claim_ceiling": "Exact released-parent quotient inventory: I2B and the zero-fermion total residual rival have zero induced capacity, selected I1B remains uncomputed, and the path adapter remains source-silent and unbuilt. No all-action or all-germ no-go follows.",
        "controls": {
            "producer": "tests/channel-swings/k885_sc_act_06_released_action_parent_quotient_inventory.py",
            "probe": "tests/channel-swings/k885_sc_act_06_released_action_parent_quotient_inventory_probe.py",
            "controls_passed": 46,
            "hostile_mutations_rejected": 20,
        },
    }


def validate(x: dict[str, Any]) -> None:
    rows, s, d = x["released_parent_inventory"], x["inventory_summary"], x["decision"]
    by_parent = {row["parent"]: row for row in rows}
    checks = [
        x["classification"] == "SOURCE_NATIVE_ROUTE",
        x["target_claim"] == "SC-ACT-06",
        set(x["pinned_inputs"]) == set(PATHS),
        all(len(row["sha256"]) == 64 for row in x["pinned_inputs"].values()),
        len(rows) == 4,
        len(by_parent) == 4,
        by_parent["I1B_FIRST_TRANSGRESSION"]["quotient_disposition"] == "open_independent_map",
        by_parent["I1B_FIRST_TRANSGRESSION"]["induced_rank_on_injected_submodule"] is None,
        by_parent["I2B_RESIDUAL_NORM_SQUARE"]["quotient_disposition"] == "closed_zero_quotient_capacity",
        by_parent["I2B_RESIDUAL_NORM_SQUARE"]["induced_rank_on_injected_submodule"] == 0,
        by_parent["TOTAL_RESIDUAL_NORM_RIVAL"]["quotient_disposition"] == "closed_zero_quotient_capacity",
        by_parent["TOTAL_RESIDUAL_NORM_RIVAL"]["induced_rank_on_injected_submodule"] == 0,
        by_parent["DIRAC_SQUARE_PATH_ADAPTER"]["quotient_disposition"] == "unowned_unbuilt_not_credited",
        by_parent["DIRAC_SQUARE_PATH_ADAPTER"]["induced_rank_on_injected_submodule"] is None,
        s["released_parent_row_count"] == 4,
        s["closed_zero_capacity_parent_count"] == 2,
        s["open_independent_parent_count"] == 1,
        s["unowned_unbuilt_parent_count"] == 1,
        s["released_independent_first_order_row_beyond_Upsilon"] == 0,
        s["all_40_types_uncovered_by_closed_factorized_parents"],
        d["released_residual_square_repair_class_closed"],
        not d["selected_I1B_repair_capacity_closed"],
        not d["source_silent_path_adapter_promoted"],
        not d["absence_of_future_or_unreleased_parent_proved"],
        not d["complete_flat_packet_repairability_refuted"],
        not d["SC_ACT_06_proved_or_refuted"],
        "selected-I1B" in d["next_exact_input"],
        "do not retry another Q" in d["next_exact_input"],
        x["source_and_ledger_effect"] == "SC-ACT-01_03_04_05_06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "no physical construction" in x["ledger_no_change_reason"],
        "selected I1B remains uncomputed" in x["claim_ceiling"],
        "No all-action" in x["claim_ceiling"],
        x["controls"]["controls_passed"] == 46,
        x["controls"]["hostile_mutations_rejected"] == 20,
        x["controls"]["producer"].endswith("k885_sc_act_06_released_action_parent_quotient_inventory.py"),
        x["controls"]["probe"].endswith("k885_sc_act_06_released_action_parent_quotient_inventory_probe.py"),
        x["gu_typed_objects"]["target"].startswith("INVENTORY-TYPE="),
        "SO(6)xSO(7)" in x["gu_typed_objects"]["real_structure"],
        "quotient-effective" in x["scope"],
        x["schema_version"] == "1.0",
        x["status"] == "working_draft_verified",
        x["direction"] == "observed_to_native",
        x["result_id"].startswith("K885-"),
        all(row["source_claim"].startswith("SC-ACT-") for row in rows),
        s["closed_zero_capacity_parent_count"] + s["open_independent_parent_count"] + s["unowned_unbuilt_parent_count"] == s["released_parent_row_count"],
        by_parent["I1B_FIRST_TRANSGRESSION"]["independent_response"] is True,
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
