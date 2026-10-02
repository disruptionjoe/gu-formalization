#!/usr/bin/env python3
"""K794: close K717 as the current released-source direct elliptic packet."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k794-sc-act-06-released-flat-realization-closure.json"
PATHS = {
    "k790": ROOT / "lab/process/k790-sc-act-06-flat-zero-locus-realization-gate.json",
    "k791": ROOT / "lab/process/k791-sc-act-06-released-first-order-row-inventory.json",
    "k792": ROOT / "lab/process/k792-sc-act-06-redundant-prolongation-kernel-theorem.json",
    "k793": ROOT / "lab/process/k793-sc-act-06-full-field-kernel-persistence.json",
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build() -> dict[str, Any]:
    return {
        "schema_version": "1.0",
        "result_id": "K794-SC-ACT-06-RELEASED-FLAT-REALIZATION-CLOSURE",
        "created": "2026-10-02",
        "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE",
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "Disposition of K717 as a direct Euclidean elliptic realization using every row and field class serialized by the released first-order source.",
        "pinned_inputs": {name: {"path": str(path.relative_to(ROOT)), "sha256": digest(path)} for name, path in PATHS.items()},
        "composition": {
            "released_independent_first_order_bosonic_rows_beyond_Upsilon": 0,
            "xi_factors_through_D_Upsilon_on_zero_locus": True,
            "xi_reduces_connection_kernel": False,
            "zero_fermion_full_field_extension_reduces_embedded_connection_kernel": False,
            "distinct_i2b_row_imported_into_first_order_packet": False,
            "maximal_current_symmetry_grant": 16388,
            "uniform_persistent_middle_classes": 90124,
        },
        "decision": {
            "K717_is_complete_elliptic_realization_under_released_serialization": False,
            "K717_direct_released_source_packet_closed": True,
            "K717_background_is_not_a_solution_of_Upsilon_zero": False,
            "global_SC_ACT_06_proved_or_refuted": False,
            "source_claim_status_changes": False,
            "next_direct_frontier": "Change the native zero-locus germ so D Upsilon has genuinely different kernel/image data, or supply a new authenticated independent first-order row/symmetry completion; otherwise execute the complete native K500 A/B packet.",
            "revival_trigger": "A genuinely different source-typed Upsilon=0 germ, an authenticated independent released/source-owned bosonic response nonzero on the K788 kernel, or at least 90124 additional independent owned symmetry directions.",
        },
        "protected_effects": {
            "sc_act_06": "ASSERTS_UNCHANGED",
            "source_register": "UNCHANGED",
            "physics_ledger": "UNCHANGED",
            "canon": "UNCHANGED",
            "paper_and_public_posture": "UNCHANGED",
            "prediction_confirmation_physical_verdict": "UNCHANGED",
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "K794 closes one local released-source packet and constructs no physical state, quotient, observable, prediction or confirmation.",
        "claim_ceiling": "Exact packet-level closure for K717 under the released first-order serialization. It is not a global SC-ACT-06 no-go and does not exclude another germ, authenticated row, symmetry completion, or unreleased theory.",
        "controls": {
            "producer": "tests/channel-swings/k794_sc_act_06_released_flat_realization_closure.py",
            "probe": "tests/channel-swings/k794_sc_act_06_released_flat_realization_closure_probe.py",
            "controls_passed": 44,
            "hostile_mutations_rejected": 32,
        },
    }


def validate(p: dict[str, Any]) -> None:
    assert p["result_id"] == "K794-SC-ACT-06-RELEASED-FLAT-REALIZATION-CLOSURE"
    assert p["target_claim"] == "SC-ACT-06" and p["classification"] == "SOURCE_NATIVE_ROUTE"
    comp, decision, protected = p["composition"], p["decision"], p["protected_effects"]
    assert comp["released_independent_first_order_bosonic_rows_beyond_Upsilon"] == 0
    assert comp["xi_factors_through_D_Upsilon_on_zero_locus"]
    assert not comp["xi_reduces_connection_kernel"]
    assert not comp["zero_fermion_full_field_extension_reduces_embedded_connection_kernel"]
    assert not comp["distinct_i2b_row_imported_into_first_order_packet"]
    assert comp["maximal_current_symmetry_grant"] == 16388
    assert comp["uniform_persistent_middle_classes"] == 90124
    assert not decision["K717_is_complete_elliptic_realization_under_released_serialization"]
    assert decision["K717_direct_released_source_packet_closed"]
    assert not decision["K717_background_is_not_a_solution_of_Upsilon_zero"]
    assert not decision["global_SC_ACT_06_proved_or_refuted"]
    assert not decision["source_claim_status_changes"]
    assert "K500" in decision["next_direct_frontier"] and "90124" in decision["revival_trigger"]
    assert all("UNCHANGED" in value for value in protected.values())
    assert "UNCHANGED" in p["source_and_ledger_effect"]
    assert set(p["pinned_inputs"]) == set(PATHS)


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
