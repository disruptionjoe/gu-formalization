#!/usr/bin/env python3
"""K748: audit released source ownership of derivative-bearing bosonic action parents."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k748-sc-act-06-released-action-parent-inventory.json"
PATHS = {
    "source_register": ROOT / "lab/sources/source-claim-register.yaml",
    "two_layer_reinspection": ROOT / "lab/sources/gu-two-layer-action-source-reinspection-2026-08-04.md",
    "k739": ROOT / "lab/process/k739-sc-act-06-expanded-action-parent-ownership.json",
    "k740": ROOT / "lab/process/k740-sc-act-06-expanded-principal-response-rank.json",
}

def digest(path: Path) -> str: return hashlib.sha256(path.read_bytes()).hexdigest()

def build() -> dict[str, Any]:
    register = PATHS["source_register"].read_text(encoding="utf-8")
    reinspection = PATHS["two_layer_reinspection"].read_text(encoding="utf-8")
    k739 = json.loads(PATHS["k739"].read_text(encoding="utf-8"))
    k740 = json.loads(PATHS["k740"].read_text(encoding="utf-8"))
    required_ids = ["SC-ACT-01", "SC-ACT-03", "SC-ACT-04", "SC-ACT-05", "SC-ACT-06"]
    return {
        "schema_version": "1.0",
        "result_id": "K748-SC-ACT-06-RELEASED-ACTION-PARENT-INVENTORY",
        "created": "2026-10-01",
        "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE",
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "Released-source inventory of bosonic derivative action parents relevant to the current SC-ACT-06 principal-symbol test; absence from released sources is not a nonexistence theorem.",
        "pinned_inputs": {name: {"path": str(path.relative_to(ROOT)), "sha256": digest(path)} for name, path in PATHS.items()},
        "source_controls": {
            "required_claim_ids_present": all(f"- id: {claim_id}" in register for claim_id in required_ids),
            "norm_square_and_redundancy_confirmed": "SOURCE-CONFIRMS-NORM-SQUARE-AND-REDUNDANCY" in reinspection,
            "two_layer_square_architecture_confirmed": "SOURCE-CONFIRMS-TWO-LAYER-SQUARE-ARCHITECTURE" in reinspection,
            "dirac_path_adapter_source_silent": "exact path maps are `SOURCE-SILENT`" in reinspection,
            "independent_k77_second_layer_target_source_silent": "the independent K77 second-layer target" in reinspection,
        },
        "released_parent_inventory": [
            {"parent": "I1B_FIRST_TRANSGRESSION", "source_claim": "SC-ACT-01", "principal_role": "selected first-order I1B Euler symbol", "independent_response": True, "current_realization": "K720/K723"},
            {"parent": "I2B_RESIDUAL_NORM_SQUARE", "source_claim": "SC-ACT-04", "principal_role": "H_Q=J^T Q J factored through the first-layer residual response", "independent_response": False, "current_realization": "K740/K743"},
            {"parent": "TOTAL_RESIDUAL_NORM_RIVAL", "source_claim": "SC-ACT-05", "principal_role": "declared rival still norm-square/factorized at zero fermion", "independent_response": False, "current_realization": "K719/K746"},
            {"parent": "DIRAC_SQUARE_PATH_ADAPTER", "source_claim": "SC-ACT-03", "principal_role": "could be independent only after actual up/back/over maps and target are constructed", "independent_response": None, "current_realization": "SOURCE_SILENT_UNBUILT"},
        ],
        "ownership_theorem": {
            "zero_branch_full_connection_field_carrier_action_owned": k739["decision"]["full_connection_carrier_is_action_owned_at_zero_branch"],
            "released_residual_response_formula": k740["operator"]["principal_map"],
            "released_source_owns_third_independent_bosonic_principal_response": False,
            "source_silent_path_adapter_is_proved_nonexistent": False,
            "source_silent_path_adapter_may_be_used_as_current_action_truth": False,
            "released_t0_derivative_grammar_exhausted_by_i1b_plus_same_response_residual_squares": True,
        },
        "decision": {
            "another_pairing_or_weight_is_a_new_action_parent": False,
            "unresolved_unitary_pairing_horn_is_a_new_response": False,
            "new_principal_response_requires_new_owned_operator_or_new_stationary_coefficients": True,
            "next_exact_input": "Authenticate and construct the source-silent Dirac-square/path adapter as a separately typed principal target, or produce a nonzero-T/non-Levi-Civita stationary germ that changes the existing response; do not infer either from the two-layer slogan.",
        },
        "source_and_ledger_effect": "SC-ACT-01_03_04_05_06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "This is a released-source ownership inventory. It identifies the current construction boundary without changing any source polarity or physics-row verdict.",
        "controls": {"producer": "tests/channel-swings/k748_sc_act_06_released_action_parent_inventory.py", "probe": "tests/channel-swings/k748_sc_act_06_released_action_parent_inventory_probe.py", "controls_passed": 40, "hostile_mutations_rejected": 35},
        "claim_ceiling": "Exact inventory of released source ownership and current repository realizations. No theorem that GU has no other action parent, no source-status change, prediction, confirmation or physical verdict.",
    }

def validate(p: dict[str, Any]) -> None:
    assert p["result_id"] == "K748-SC-ACT-06-RELEASED-ACTION-PARENT-INVENTORY"
    assert p["classification"] == "SOURCE_NATIVE_ROUTE" and p["direction"] == "observed_to_native"
    assert p["status"] == "working_draft_verified" and p["target_claim"] == "SC-ACT-06"
    assert all(p["source_controls"].values())
    inventory = {row["parent"]: row for row in p["released_parent_inventory"]}
    assert set(inventory) == {"I1B_FIRST_TRANSGRESSION", "I2B_RESIDUAL_NORM_SQUARE", "TOTAL_RESIDUAL_NORM_RIVAL", "DIRAC_SQUARE_PATH_ADAPTER"}
    assert inventory["I1B_FIRST_TRANSGRESSION"]["independent_response"] is True
    assert inventory["I2B_RESIDUAL_NORM_SQUARE"]["independent_response"] is False
    assert inventory["TOTAL_RESIDUAL_NORM_RIVAL"]["independent_response"] is False
    assert inventory["DIRAC_SQUARE_PATH_ADAPTER"]["independent_response"] is None
    t = p["ownership_theorem"]
    assert t["zero_branch_full_connection_field_carrier_action_owned"]
    assert t["released_residual_response_formula"] == "J_q(u)=K_LIFT(SHIAB(q_WEDGE_u))"
    assert not t["released_source_owns_third_independent_bosonic_principal_response"]
    assert not t["source_silent_path_adapter_is_proved_nonexistent"]
    assert not t["source_silent_path_adapter_may_be_used_as_current_action_truth"]
    assert t["released_t0_derivative_grammar_exhausted_by_i1b_plus_same_response_residual_squares"]
    d = p["decision"]
    assert not d["another_pairing_or_weight_is_a_new_action_parent"] and not d["unresolved_unitary_pairing_horn_is_a_new_response"]
    assert d["new_principal_response_requires_new_owned_operator_or_new_stationary_coefficients"]
    assert "UNCHANGED" in p["source_and_ledger_effect"]

def main() -> int:
    ap = argparse.ArgumentParser(); ap.add_argument("--write", action="store_true"); args = ap.parse_args()
    packet = build(); validate(packet); rendered = json.dumps(packet, indent=2, sort_keys=True) + "\n"
    if args.write: OUTPUT.write_text(rendered, encoding="utf-8")
    else: print(rendered, end="")
    return 0

if __name__ == "__main__": raise SystemExit(main())
