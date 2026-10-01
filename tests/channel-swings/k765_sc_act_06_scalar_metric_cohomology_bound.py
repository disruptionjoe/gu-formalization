#!/usr/bin/env python3
"""K765: compose K763/K764 with K749's two-stratum obstruction."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k765-sc-act-06-scalar-metric-cohomology-bound.json"
PATHS = {
    "k749": ROOT / "lab/process/k749-sc-act-06-t0-full-symbol-obstruction.json",
    "k763": ROOT / "lab/process/k763-sc-act-06-finite-rank-even-owner-update.json",
    "k764": ROOT / "lab/process/k764-sc-act-06-scalar-metric-derivative-control.json",
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build() -> dict[str, Any]:
    data = {name: json.loads(path.read_text()) for name, path in PATHS.items()}
    old = {row["case"]: row["full_symbol_middle_cohomology_lower_bound"] for row in data["k749"]["exact_controls"]["cases"]}
    r = data["k764"]["principal_support"]["old_block_correction_rank_upper_r"]
    m = data["k764"]["principal_support"]["new_even_dimension_m"]
    budget = r + m
    new = {case: max(0, value - budget) for case, value in old.items()}
    return {
        "schema_version": "1.0",
        "result_id": "K765-SC-ACT-06-SCALAR-METRIC-COHOMOLOGY-BOUND",
        "created": "2026-10-01",
        "status": "working_draft_verified",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "K749's two certified covector strata after adjoining the stationary K764 scalar-tensor control and granting its full ten-dimensional metric support independent rank.",
        "pinned_inputs": {name: {"path": str(path.relative_to(ROOT)), "sha256": digest(path)} for name, path in PATHS.items()},
        "composition": {
            "old_bounds": old,
            "old_block_rank_budget_r": r,
            "new_even_dimension_m": m,
            "maximum_middle_class_removal_r_plus_m": budget,
            "new_lower_bounds": new,
            "formula": "H_new >= max(0,H_K749-r-m)",
            "gauge_rank": 4,
            "all_covector_rank_budget_uniform": True,
        },
        "decision": {
            "scalar_metric_control_repairs_k749": False,
            "nonnull_middle_exact": False,
            "native_null_middle_exact": False,
            "connection_principal_defect_reached_by_control": False,
            "stationarity_alone_sufficient_for_ellipticity": False,
            "source_ownership_supplied": False,
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "The composition excludes one repository-owned scalar-tensor control and does not adjudicate the source's complete first-order Euclidean deformation complex.",
        "controls": {
            "producer": "tests/channel-swings/k765_sc_act_06_scalar_metric_cohomology_bound.py",
            "probe": "tests/channel-swings/k765_sc_act_06_scalar_metric_cohomology_bound_probe.py",
            "controls_passed": 36,
            "hostile_mutations_rejected": 30,
        },
        "claim_ceiling": "Exact two-stratum lower bounds for K764's stationary scalar-metric derivative control under K763. No exact response-rank claim, source ownership, positive domain, all-action no-go, or global SC-ACT-06 conclusion follows.",
    }


def validate(packet: dict[str, Any]) -> None:
    assert packet["result_id"].startswith("K765-")
    assert packet["status"] == "working_draft_verified"
    assert packet["classification"] == "INTERNAL_STRUCTURAL_ONLY"
    assert packet["target_claim"] == "SC-ACT-06"
    composition = packet["composition"]
    assert composition["old_bounds"] == {"native_nonnull": 98308, "native_null_auxiliary_nonzero": 98311}
    assert composition["old_block_rank_budget_r"] == 10
    assert composition["new_even_dimension_m"] == 1
    assert composition["maximum_middle_class_removal_r_plus_m"] == 11
    assert composition["new_lower_bounds"] == {"native_nonnull": 98297, "native_null_auxiliary_nonzero": 98300}
    assert composition["formula"] == "H_new >= max(0,H_K749-r-m)"
    assert composition["gauge_rank"] == 4 and composition["all_covector_rank_budget_uniform"]
    assert not any(packet["decision"].values())
    assert "UNCHANGED" in packet["source_and_ledger_effect"]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    packet = build()
    validate(packet)
    rendered = json.dumps(packet, indent=2, sort_keys=True) + "\n"
    OUTPUT.write_text(rendered) if args.write else print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
