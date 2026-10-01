#!/usr/bin/env python3
"""K746: compose K745 with the exact displayed fermion diagonal."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k746-sc-act-06-residual-square-full-symbol-obstruction.json"
PATHS = {
    "k745": ROOT / "lab/process/k745-sc-act-06-gauge-redundancy-obstruction.json",
    "k742": ROOT / "lab/process/k742-sc-act-06-expanded-displayed-full-symbol-test.json",
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build() -> dict[str, Any]:
    k745 = json.loads(PATHS["k745"].read_text(encoding="utf-8"))
    k742 = json.loads(PATHS["k742"].read_text(encoding="utf-8"))
    gauge_cases = {row["case"]: row for row in k745["exact_controls"]["cases"]}
    fermion_cases = {row["case"]: row for row in k742["exact_controls"]["cases"]}
    cases = []
    for name in ("native_nonnull", "native_null_auxiliary_nonzero"):
        bosonic = gauge_cases[name]
        fermion = fermion_cases[name]
        cases.append(
            {
                "case": name,
                "universal_bosonic_middle_cohomology_lower": bosonic["universal_middle_cohomology_lower"],
                "full_trace_bosonic_middle_cohomology": bosonic["full_trace_middle_cohomology"],
                "fermion_middle_cohomology_dimension": fermion["fermion_middle_cohomology_dimension"],
                "universal_full_symbol_middle_cohomology_lower": bosonic["universal_middle_cohomology_lower"],
                "full_trace_full_symbol_middle_cohomology": bosonic["full_trace_middle_cohomology"],
                "full_symbol_exact": False,
            }
        )
    return {
        "schema_version": "1.0",
        "result_id": "K746-SC-ACT-06-RESIDUAL-SQUARE-FULL-SYMBOL-OBSTRUCTION",
        "created": "2026-10-01",
        "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE",
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "Zero-fermion direct-sum composition of K745's pairing-independent bosonic obstruction with the displayed exact equation-(9.16) fermion diagonal.",
        "pinned_inputs": {name: {"path": str(path.relative_to(ROOT)), "sha256": digest(path)} for name, path in PATHS.items()},
        "composition_theorem": {
            "mixed_boson_fermion_principal_blocks_vanish": True,
            "displayed_fermion_candidate_is_exact": True,
            "middle_cohomology_is_direct_sum": True,
            "same_response_residual_pairing_can_repair_full_symbol": False,
            "source_global_SC_ACT_06_refuted": False,
        },
        "exact_controls": {"fermion_two_block_rank": k742["exact_controls"]["fermion_two_block_rank"], "cases": cases},
        "decision": {
            "k742_full_carrier_threshold_survivor_is_closed_for_same_response_residual_squares": True,
            "displayed_full_symbol_realization_is_elliptic": False,
            "different_action_owned_principal_response_or_background_remains_open": True,
            "next_exact_input": "Construct or authenticate a genuinely different action-owned principal response or stationary Euclidean germ with new image outside im(E_I1B)+im(J^T), together with its actual gauge/redundancy complex; do not vary only the residual pairing or weight on K740's response.",
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "The result excludes the frozen I1B plus every same-response residual-square repair, not every first-order-theory germ or principal packet.",
        "controls": {
            "producer": "tests/channel-swings/k746_sc_act_06_residual_square_full_symbol_obstruction.py",
            "probe": "tests/channel-swings/k746_sc_act_06_residual_square_full_symbol_obstruction_probe.py",
            "controls_passed": 34,
            "hostile_mutations_rejected": 29,
        },
        "claim_ceiling": "Exact displayed full-symbol realization obstruction. No all-background SC-ACT-06 no-go, source-status, prediction, confirmation or physical verdict.",
    }


def validate(packet: dict[str, Any]) -> None:
    assert packet["result_id"] == "K746-SC-ACT-06-RESIDUAL-SQUARE-FULL-SYMBOL-OBSTRUCTION"
    assert packet["classification"] == "SOURCE_NATIVE_ROUTE"
    assert packet["direction"] == "observed_to_native"
    assert packet["status"] == "working_draft_verified"
    assert packet["target_claim"] == "SC-ACT-06"
    theorem = packet["composition_theorem"]
    assert theorem["mixed_boson_fermion_principal_blocks_vanish"]
    assert theorem["displayed_fermion_candidate_is_exact"]
    assert theorem["middle_cohomology_is_direct_sum"]
    assert not theorem["same_response_residual_pairing_can_repair_full_symbol"]
    assert not theorem["source_global_SC_ACT_06_refuted"]
    cases = {row["case"]: row for row in packet["exact_controls"]["cases"]}
    nonnull = cases["native_nonnull"]
    null = cases["native_null_auxiliary_nonzero"]
    assert (nonnull["universal_full_symbol_middle_cohomology_lower"], null["universal_full_symbol_middle_cohomology_lower"]) == (98308, 98311)
    assert (nonnull["full_trace_full_symbol_middle_cohomology"], null["full_trace_full_symbol_middle_cohomology"]) == (98308, 106568)
    assert (nonnull["universal_bosonic_middle_cohomology_lower"], null["universal_bosonic_middle_cohomology_lower"]) == (98308, 98311)
    assert (nonnull["full_trace_bosonic_middle_cohomology"], null["full_trace_bosonic_middle_cohomology"]) == (98308, 106568)
    assert packet["exact_controls"]["fermion_two_block_rank"] == 1920
    for row in cases.values():
        assert row["fermion_middle_cohomology_dimension"] == 0
        assert not row["full_symbol_exact"]
    decision = packet["decision"]
    assert decision["k742_full_carrier_threshold_survivor_is_closed_for_same_response_residual_squares"]
    assert not decision["displayed_full_symbol_realization_is_elliptic"]
    assert decision["different_action_owned_principal_response_or_background_remains_open"]
    assert "UNCHANGED" in packet["source_and_ledger_effect"]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
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
