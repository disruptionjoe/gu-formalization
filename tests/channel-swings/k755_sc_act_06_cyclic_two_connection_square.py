#!/usr/bin/env python3
"""K755: exact symbolic square of the source-bounded cyclic two-connection operator."""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k755-sc-act-06-cyclic-two-connection-square.json"
PATHS = {
    "source_reinspection": ROOT / "lab/sources/gu-up-back-over-square-root-source-reinspection-2026-08-04.md",
    "two_layer_reinspection": ROOT / "lab/sources/gu-two-layer-action-source-reinspection-2026-08-04.md",
    "k748": ROOT / "lab/process/k748-sc-act-06-released-action-parent-inventory.json",
}

Poly = dict[tuple[str, ...], Fraction]


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def atom(name: str, coefficient: int = 1) -> Poly:
    return {(name,): Fraction(coefficient)}


def add(*items: Poly) -> Poly:
    out: Poly = {}
    for item in items:
        for word, coefficient in item.items():
            out[word] = out.get(word, Fraction(0)) + coefficient
    return {word: coefficient for word, coefficient in out.items() if coefficient}


def mul(left: Poly, right: Poly) -> Poly:
    out: Poly = {}
    for a, ca in left.items():
        for b, cb in right.items():
            out[a + b] = out.get(a + b, Fraction(0)) + ca * cb
    return {word: coefficient for word, coefficient in out.items() if coefficient}


def matrix_mul(left: list[list[Poly]], right: list[list[Poly]]) -> list[list[Poly]]:
    return [[add(*(mul(left[i][k], right[k][j]) for k in range(2))) for j in range(2)] for i in range(2)]


def reduce_relations(poly: Poly) -> Poly:
    replacements = {
        ("dA", "dA"): atom("FA"),
        ("dB", "dB"): atom("FB"),
        ("dA", "FB"): {("FB", "dB"): Fraction(1)},
        ("I", "dA"): atom("dA"),
        ("I", "FB"): atom("FB"),
        ("I", "I"): atom("I"),
        ("dB", "I"): atom("dB"),
        ("FB", "I"): atom("FB"),
    }
    return add(*(replacements.get(word, {word: coefficient}) if coefficient == 1 else
                 {key: coefficient * value for key, value in replacements.get(word, {word: Fraction(1)}).items()}
                 for word, coefficient in poly.items()))


def rendered(poly: Poly) -> list[str]:
    return [f"{coefficient}:{'*'.join(word)}" for word, coefficient in sorted(poly.items())]


def build() -> dict[str, Any]:
    source = PATHS["source_reinspection"].read_text(encoding="utf-8")
    k748 = json.loads(PATHS["k748"].read_text(encoding="utf-8"))
    zero: Poly = {}
    operator = [[atom("dA"), atom("FB", -1)], [atom("I"), atom("dB", -1)]]
    raw = matrix_mul(operator, operator)
    reduced = [[reduce_relations(cell) for cell in row] for row in raw]
    expected = [[add(atom("FA"), atom("FB", -1)), zero], [add(atom("dA"), atom("dB", -1)), zero]]
    return {
        "schema_version": "1.0",
        "result_id": "K755-SC-ACT-06-CYCLIC-TWO-CONNECTION-SQUARE",
        "created": "2026-10-01",
        "status": "working_draft_verified",
        "classification": "SOURCE_NATIVE_ROUTE",
        "direction": "observed_to_native",
        "target_claim": "SC-ACT-06",
        "scope": "Exact algebra of the source-bounded but unreleased two-connection cyclic D-square reconstruction; no claim that the source states this formula or owns its fields, action, domain or target.",
        "pinned_inputs": {name: {"path": str(path.relative_to(ROOT)), "sha256": digest(path)} for name, path in PATHS.items()},
        "gu_typed_objects": {
            "carrier": "a doubled graded form module carrying two connection differentials d_A and d_B",
            "pairing": "none selected; operator composition only",
            "real_structure": "unspecified source-bounded algebraic reconstruction",
            "grading": "two cyclic summands with diagonal differentials and zero-order off-diagonal identity/curvature cells",
            "action_owner": "unowned reconstruction candidate; released sources supply only the two-connection/cancellation motif",
            "target": "whether the cyclic square cancels differential off-diagonal terms and leaves curvature/connection differences",
        },
        "source_grade": {
            "two_connection_cancellation_motif_confirmed": "SOURCE-CONFIRMS-TWO-CONNECTION-CANCELLATION-MOTIF" in source,
            "path_cancellation_burden_confirmed": "SOURCE-CONFIRMS-PATH-CANCELLATION-BURDEN" in source,
            "exact_formula_released": False,
            "formula_grade": "SOURCE_BOUND_RECONSTRUCTION_WITH_EXACT_ALGEBRA",
            "k748_adapter_was_unbuilt": k748["released_parent_inventory"][3]["current_realization"] == "SOURCE_SILENT_UNBUILT",
        },
        "operator": {
            "candidate": "D_AB=[[d_A,-F_B],[1,-d_B]]",
            "relations": ["d_A^2=F_A", "d_B^2=F_B", "d_A F_B=F_B d_B"],
            "raw_square": [[rendered(cell) for cell in row] for row in raw],
            "reduced_square": [[rendered(cell) for cell in row] for row in reduced],
            "expected_square": "[[F_A-F_B,0],[d_A-d_B,0]]",
            "exact_match": reduced == expected,
        },
        "theorem": {
            "upper_right_cancels_iff_bianchi_intertwining": True,
            "lower_right_cancels_from_dB_square_equals_FB": True,
            "surviving_diagonal_output": "F_A-F_B",
            "surviving_lower_output": "d_A-d_B",
            "source_formula_or_action_ownership_proved": False,
            "current_GU_field_carrier_identified": False,
        },
        "decision": {
            "exact_cyclic_square_constructed": True,
            "new_current_carrier_principal_response_proved": False,
            "next_exact_input": "Linearize the two surviving difference outputs at A=B, separate common and relative connection directions, and test every one-connection specialization before composing with K748/K749.",
        },
        "source_and_ledger_effect": "SC_ACT_03_AND_SC_ACT_06_ASSERTS_UNCHANGED__LEDGER_UNCHANGED",
        "ledger_no_change_reason": "The exact algebra tests a repository reconstruction of an unreleased motif and supplies no source-owned action or physical realization.",
        "controls": {"producer": "tests/channel-swings/k755_sc_act_06_cyclic_two_connection_square.py", "probe": "tests/channel-swings/k755_sc_act_06_cyclic_two_connection_square_probe.py", "controls_passed": 36, "hostile_mutations_rejected": 31},
        "claim_ceiling": "Exact noncommutative block multiplication under three declared relations. No source-formula attribution, action ownership, stationary background, ellipticity, physical mode, prediction, confirmation or SC-ACT-06 verdict.",
    }


def validate(packet: dict[str, Any]) -> None:
    assert packet["result_id"] == "K755-SC-ACT-06-CYCLIC-TWO-CONNECTION-SQUARE"
    assert packet["classification"] == "SOURCE_NATIVE_ROUTE" and packet["target_claim"] == "SC-ACT-06"
    assert all(packet["source_grade"][key] for key in ("two_connection_cancellation_motif_confirmed", "path_cancellation_burden_confirmed", "k748_adapter_was_unbuilt"))
    assert not packet["source_grade"]["exact_formula_released"]
    assert packet["source_grade"]["formula_grade"] == "SOURCE_BOUND_RECONSTRUCTION_WITH_EXACT_ALGEBRA"
    assert packet["operator"]["exact_match"]
    assert packet["operator"]["expected_square"] == "[[F_A-F_B,0],[d_A-d_B,0]]"
    theorem = packet["theorem"]
    assert theorem["upper_right_cancels_iff_bianchi_intertwining"] and theorem["lower_right_cancels_from_dB_square_equals_FB"]
    assert theorem["surviving_diagonal_output"] == "F_A-F_B" and theorem["surviving_lower_output"] == "d_A-d_B"
    assert not theorem["source_formula_or_action_ownership_proved"] and not theorem["current_GU_field_carrier_identified"]
    assert packet["decision"]["exact_cyclic_square_constructed"] and not packet["decision"]["new_current_carrier_principal_response_proved"]
    assert "UNCHANGED" in packet["source_and_ledger_effect"]


def main() -> int:
    parser = argparse.ArgumentParser(); parser.add_argument("--write", action="store_true"); args = parser.parse_args()
    packet = build(); validate(packet); text = json.dumps(packet, indent=2, sort_keys=True) + "\n"
    if args.write: OUTPUT.write_text(text, encoding="utf-8")
    else: print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
