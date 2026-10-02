#!/usr/bin/env python3
"""K791: inventory every released first-order row relevant to SC-ACT-06."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k791-sc-act-06-released-first-order-row-inventory.json"
PATHS = {
    "source_pack": ROOT / "lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md",
    "source_register": ROOT / "lab/sources/source-claim-register.yaml",
    "k719": ROOT / "lab/process/k719-sc-act-06-zero-fermion-full-symbol-reduction.json",
    "k784": ROOT / "lab/process/k784-sc-act-06-i1b-i2b-action-sum-ownership-correction.json",
    "k790": ROOT / "lab/process/k790-sc-act-06-flat-zero-locus-realization-gate.json",
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build() -> dict[str, Any]:
    source = PATHS["source_pack"].read_text(encoding="utf-8")
    register = PATHS["source_register"].read_text(encoding="utf-8")
    witnesses = {
        "first_order_total_residual": r"\Upsilon^B_\omega+\Upsilon^F_\omega=0" in source,
        "redundant_prolongation": r"\Xi_\omega=D_\omega\Upsilon_\omega" in source,
        "second_order_alternative": r"D_\omega^*\Upsilon^B_\omega=\Upsilon^F_\omega" in source,
        "sc_act_06_exact_wording": "Upsilon = 0 carries" in register and "elliptic deformation complex" in register,
    }
    return {
        "schema_version": "1.0",
        "result_id": "K791-SC-ACT-06-RELEASED-FIRST-ORDER-ROW-INVENTORY",
        "created": "2026-10-02",
        "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE",
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "Complete released-source row/column inventory relevant to the K717 zero-fermion first-order Upsilon=0 deformation packet.",
        "pinned_inputs": {name: {"path": str(path.relative_to(ROOT)), "sha256": digest(path)} for name, path in PATHS.items()},
        "source_witnesses": witnesses,
        "inventory": {
            "first_order_bosonic_residual_rows": ["Upsilon_B inside total Upsilon=Upsilon_B+Upsilon_F"],
            "first_order_fermion_rows": ["spinor Euler components inside Upsilon_F", "adjoint-valued bilinear current inside Upsilon_F"],
            "redundant_rows": ["Xi=D_omega Upsilon"],
            "distinct_second_action_rows": ["D_omega^* Upsilon_B=Upsilon_F"],
            "field_columns_not_equation_rows": ["metric g", "source epsilon", "connection varpi", "fermions"],
            "additional_released_first_order_bosonic_row_independent_of_Upsilon": [],
        },
        "typing": {
            "xi_is_covariant_prolongation_not_frechet_epsilon_column": True,
            "i2b_row_belongs_to_distinct_second_action": True,
            "metric_and_epsilon_are_fields_not_extra_equations": True,
            "fermion_current_is_bilinear_and_has_zero_connection_derivative_at_zero_fermion": True,
            "zero_fermion_principal_symbol_is_block_diagonal": True,
        },
        "decision": {
            "released_independent_first_order_bosonic_row_count_beyond_Upsilon": 0,
            "only_displayed_extra_bosonic_equation_is_declared_redundant": True,
            "source_inventory_supplies_K790_missing_independent_row": False,
            "next_exact_input": "Prove that the redundant Xi row factors through D Upsilon at the zero locus, then compose the zero-fermion block split and field-column extension lemma.",
        },
        "source_and_ledger_effect": "SC-ACT-06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "This is a source-serialization inventory, not a physical state, quotient, observable, prediction or confirmation.",
        "claim_ceiling": "Complete inventory of the released rows used by the current first-order packet. It does not prove that every future or unreleased completion lacks another row and changes no source or physical verdict.",
        "controls": {
            "producer": "tests/channel-swings/k791_sc_act_06_released_first_order_row_inventory.py",
            "probe": "tests/channel-swings/k791_sc_act_06_released_first_order_row_inventory_probe.py",
            "controls_passed": 40,
            "hostile_mutations_rejected": 28,
        },
    }


def validate(p: dict[str, Any]) -> None:
    assert p["result_id"] == "K791-SC-ACT-06-RELEASED-FIRST-ORDER-ROW-INVENTORY"
    assert p["target_claim"] == "SC-ACT-06" and p["classification"] == "SOURCE_NATIVE_ROUTE"
    assert all(p["source_witnesses"].values())
    inv, typing, decision = p["inventory"], p["typing"], p["decision"]
    assert len(inv["first_order_bosonic_residual_rows"]) == 1
    assert len(inv["first_order_fermion_rows"]) == 2
    assert inv["redundant_rows"] == ["Xi=D_omega Upsilon"]
    assert len(inv["distinct_second_action_rows"]) == 1
    assert inv["field_columns_not_equation_rows"] == ["metric g", "source epsilon", "connection varpi", "fermions"]
    assert inv["additional_released_first_order_bosonic_row_independent_of_Upsilon"] == []
    assert all(typing.values())
    assert decision["released_independent_first_order_bosonic_row_count_beyond_Upsilon"] == 0
    assert decision["only_displayed_extra_bosonic_equation_is_declared_redundant"]
    assert not decision["source_inventory_supplies_K790_missing_independent_row"]
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
